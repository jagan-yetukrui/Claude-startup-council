#!/usr/bin/env python3
"""Deterministic scoring for the /council skill.

LLMs miscompute medians, totals, and band edges. This script does that arithmetic so the
verdict's numbers are never wrong. It takes the three members' REVISED (Round 2) scorecards and
the judge's own five scores, and returns per-axis member medians, the judge total, the verdict
band, the axes where the judge diverges from the member median by >= 2 (which the protocol says
must be justified or adopted), and an evidence-coverage confidence cap.

Usage:
    python3 scripts/score.py --members '<json>' --judge '<json>' [--coverage '<json>']
    python3 scripts/score.py --self-test

  --members : JSON list of exactly three scorecard objects (the members' revised scores).
  --judge   : JSON object, the judge's own five axis scores.
  --coverage: optional JSON object mapping each axis to the binding evidence grade
              ("E0".."E4") behind the judge's score; drives the confidence cap.

Each scorecard object uses the five axes (aliases accepted):
  pain, willingness_to_pay (wtp/payer), wedge, distribution, timing_moat (timing).
Scores are integers 1..5.

Output: a JSON object on stdout. Exit 0 on success, 2 on bad input.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys

AXES = ["pain", "willingness_to_pay", "wedge", "distribution", "timing_moat"]

# Accept human/legacy spellings so callers never have to remember the canonical key.
ALIASES = {
    "pain": "pain",
    "willingness_to_pay": "willingness_to_pay",
    "willingness-to-pay": "willingness_to_pay",
    "wtp": "willingness_to_pay",
    "payer": "willingness_to_pay",          # legacy axis name (pre early-stage reframe)
    "wedge": "wedge",
    "distribution": "distribution",
    "timing_moat": "timing_moat",
    "timing/moat": "timing_moat",
    "timing": "timing_moat",
    "moat": "timing_moat",
}

BANDS = [
    (20, 25, "BUILD IT"),
    (13, 19, "PIVOT"),
    (0, 12, "KILL IT"),
]


def _fail(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    print(json.dumps({"error": msg}), file=sys.stderr)
    sys.exit(2)


def normalize(card: dict, where: str) -> dict:
    """Map a raw scorecard (any accepted spelling) to canonical axes with int 1..5 values."""
    if not isinstance(card, dict):
        _fail(f"{where}: expected an object, got {type(card).__name__}")
    out: dict[str, int] = {}
    for k, v in card.items():
        key = ALIASES.get(str(k).strip().lower())
        if key is None:
            continue  # ignore unknown keys (e.g. a 'notes' field)
        try:
            iv = int(v)
        except (TypeError, ValueError):
            _fail(f"{where}: axis '{k}' has non-integer score {v!r}")
        if not 1 <= iv <= 5:
            _fail(f"{where}: axis '{k}' score {iv} out of range 1..5")
        out[key] = iv
    missing = [a for a in AXES if a not in out]
    if missing:
        _fail(f"{where}: missing axes {missing}")
    return out


def band_for(total: int) -> str:
    for lo, hi, name in BANDS:
        if lo <= total <= hi:
            return name
    return "KILL IT"


def confidence_cap(coverage: dict | None) -> dict:
    """Evidence-coverage confidence cap.

    Counts how many of the five axes are backed by E3+ evidence. A verdict resting mostly on
    E0-E1 cannot honestly be high-confidence, however decisive the score looks.
    """
    if not coverage:
        return {
            "cap": "unknown",
            "reason": "no coverage map supplied; judge sets confidence manually and states why",
        }
    grades = {}
    for k, v in coverage.items():
        key = ALIASES.get(str(k).strip().lower())
        if key:
            grades[key] = str(v).strip().upper()
    strong = sum(1 for a in AXES if grades.get(a, "E0") in ("E3", "E4"))
    if strong >= 4:
        cap = "high"
    elif strong >= 2:
        cap = "medium"
    else:
        cap = "low"
    return {
        "cap": cap,
        "axes_backed_by_E3_plus": strong,
        "reason": f"{strong}/5 axes rest on E3+ evidence; confidence may not exceed '{cap}'",
    }


def score(members: list, judge: dict, coverage: dict | None) -> dict:
    if not isinstance(members, list) or len(members) != 3:
        _fail("--members must be a JSON list of exactly three scorecards")
    cards = [normalize(m, f"members[{i}]") for i, m in enumerate(members)]
    j = normalize(judge, "judge")

    medians = {}
    divergences = []
    for a in AXES:
        vals = sorted(c[a] for c in cards)
        med = int(statistics.median(vals))  # 3 members -> middle value, always an int
        medians[a] = med
        if abs(j[a] - med) >= 2:
            divergences.append(
                {"axis": a, "judge": j[a], "member_median": med, "delta": j[a] - med}
            )

    judge_total = sum(j[a] for a in AXES)
    member_median_total = sum(medians.values())
    return {
        "axes": AXES,
        "member_scorecards": cards,
        "member_medians": medians,
        "member_median_total": member_median_total,
        "judge_scores": j,
        "judge_total": judge_total,
        "band": band_for(judge_total),
        "band_edge_watch": judge_total in (11, 12, 13, 14, 18, 19, 20, 21),
        "divergences_needing_justification": divergences,
        "confidence_cap": confidence_cap(coverage),
    }


def self_test() -> int:
    # KILL: low scores, thin evidence.
    r = score(
        [
            {"pain": 2, "wtp": 1, "wedge": 2, "distribution": 1, "timing": 1},
            {"pain": 3, "payer": 2, "wedge": 2, "distribution": 2, "timing": 1},
            {"pain": 2, "willingness-to-pay": 1, "wedge": 1, "distribution": 2, "moat": 2},
        ],
        {"pain": 2, "willingness_to_pay": 1, "wedge": 2, "distribution": 1, "timing_moat": 1},
        {"pain": "E3", "wtp": "E4", "wedge": "E1", "distribution": "E0", "timing": "E4"},
    )
    assert r["member_medians"] == {
        "pain": 2, "willingness_to_pay": 1, "wedge": 2, "distribution": 2, "timing_moat": 1
    }, r["member_medians"]
    assert r["judge_total"] == 7, r["judge_total"]
    assert r["band"] == "KILL IT", r["band"]
    assert r["confidence_cap"]["axes_backed_by_E3_plus"] == 3, r["confidence_cap"]
    assert r["confidence_cap"]["cap"] == "medium", r["confidence_cap"]

    # BUILD with a divergence and a band-edge watch.
    r2 = score(
        [
            {"pain": 5, "wtp": 4, "wedge": 4, "distribution": 4, "timing": 4},
            {"pain": 5, "wtp": 4, "wedge": 4, "distribution": 3, "timing": 4},
            {"pain": 5, "wtp": 2, "wedge": 4, "distribution": 4, "timing": 4},
        ],
        {"pain": 5, "willingness_to_pay": 2, "wedge": 4, "distribution": 4, "timing_moat": 5},
        None,
    )
    assert r2["judge_total"] == 20, r2["judge_total"]
    assert r2["band"] == "BUILD IT", r2["band"]
    assert r2["band_edge_watch"] is True, r2
    assert any(d["axis"] == "willingness_to_pay" for d in r2["divergences_needing_justification"]), r2
    assert r2["confidence_cap"]["cap"] == "unknown", r2
    print("score.py self-test: PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Deterministic council scoring.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Axis keys (aliases accepted, case-insensitive):\n"
            "  pain | willingness_to_pay (wtp, payer) | wedge | distribution | timing_moat (timing)\n"
            "Scores are integers 1..5. --members is a JSON list of THREE scorecards;\n"
            "--judge is one scorecard; --coverage maps axis -> E0..E4 for the confidence cap.\n\n"
            "Example:\n"
            "  python3 scripts/score.py \\\n"
            "    --members '[{\"pain\":4,\"wtp\":2,\"wedge\":3,\"distribution\":2,\"timing\":3},"
            "{\"pain\":3,\"wtp\":1,\"wedge\":2,\"distribution\":2,\"timing\":2},"
            "{\"pain\":3,\"wtp\":2,\"wedge\":2,\"distribution\":1,\"timing\":2}]' \\\n"
            "    --judge '{\"pain\":3,\"willingness_to_pay\":2,\"wedge\":2,\"distribution\":2,\"timing_moat\":2}' \\\n"
            "    --coverage '{\"pain\":\"E3\",\"wtp\":\"E4\",\"wedge\":\"E1\",\"distribution\":\"E1\",\"timing\":\"E3\"}'\n"
        ),
    )
    ap.add_argument("--members", help="JSON list of three member scorecards")
    ap.add_argument("--judge", help="JSON object: the judge's five axis scores")
    ap.add_argument("--coverage", help="JSON object: axis -> binding evidence grade (E0..E4)")
    ap.add_argument("--self-test", action="store_true", help="run internal checks and exit")
    args = ap.parse_args()

    if args.self_test:
        return self_test()
    if not args.members or not args.judge:
        _fail("both --members and --judge are required (or use --self-test)")
    try:
        members = json.loads(args.members)
        judge = json.loads(args.judge)
        coverage = json.loads(args.coverage) if args.coverage else None
    except json.JSONDecodeError as e:
        _fail(f"invalid JSON: {e}")
    print(json.dumps(score(members, judge, coverage), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
