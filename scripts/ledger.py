#!/usr/bin/env python3
"""Deterministic ledger for the /council skill.

The ledger is the council's memory and its conscience: every verdict is recorded so tripwires are
enforceable across sessions, verdict-shopping (re-running until BUILD) is visible, and the council
can be shown to have been right or wrong later. It is APPEND-ONLY for verdicts — `calibrate` may
annotate a past line's outcome, but a past verdict is never rewritten.

Two artifacts per run:
  ledger/ledger.jsonl                 one compact JSON line per run
  ledger/<date>-<slug>.md             the full human-readable verdict record

Subcommands:
  lookup    --url URL [--idea TEXT]        find prior runs of the same idea (for retest mode)
  append    --run JSON [--body-file PATH]  validate + write the jsonl line and the per-run md
  calibrate --match KEY --result R         set a prior line's calibration (right/wrong/ambiguous)
  tally                                    print the running right/wrong record
  validate  --run JSON                     schema-check a run record without writing

All subcommands accept --ledger-dir to point at an alternate directory (used by --self-test).
Run `python3 scripts/ledger.py --self-test` to verify without touching the real ledger.
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import tempfile
from pathlib import Path

AXES = ["pain", "willingness_to_pay", "wedge", "distribution", "timing_moat"]
SCORE_ALIASES = {
    "pain": "pain", "willingness_to_pay": "willingness_to_pay",
    "willingness-to-pay": "willingness_to_pay", "wtp": "willingness_to_pay",
    "payer": "willingness_to_pay", "wedge": "wedge", "distribution": "distribution",
    "timing_moat": "timing_moat", "timing/moat": "timing_moat", "timing": "timing_moat",
    "moat": "timing_moat",
}
VERDICTS = {"BUILD IT", "PIVOT", "KILL IT"}
REQUIRED = ["date", "idea_one_liner", "url", "scores", "verdict"]


def default_ledger_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "ledger"


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (text or "idea").lower()).strip("-")
    return (s[:48] or "idea")


def normalize_scores(scores: dict) -> dict:
    if not isinstance(scores, dict):
        raise ValueError("scores must be an object")
    out: dict[str, int] = {}
    for k, v in scores.items():
        key = SCORE_ALIASES.get(str(k).strip().lower())
        if key is None:
            continue
        iv = int(v)
        if not 1 <= iv <= 5:
            raise ValueError(f"score '{k}'={iv} out of range 1..5")
        out[key] = iv
    missing = [a for a in AXES if a not in out]
    if missing:
        raise ValueError(f"scores missing axes {missing}")
    return out


def validate_run(run: dict) -> dict:
    """Return a normalized run dict or raise ValueError."""
    if not isinstance(run, dict):
        raise ValueError("run must be a JSON object")
    for f in REQUIRED:
        if f not in run:
            raise ValueError(f"run missing required field '{f}'")
    scores = normalize_scores(run["scores"])
    verdict = str(run["verdict"]).strip().upper()
    if verdict not in VERDICTS:
        raise ValueError(f"verdict '{run['verdict']}' must be one of {sorted(VERDICTS)}")
    total = run.get("total")
    computed = sum(scores.values())
    if total is None:
        total = computed
    elif int(total) != computed:
        raise ValueError(f"total {total} != sum of scores {computed}")
    norm = dict(run)
    norm["scores"] = scores
    norm["verdict"] = verdict
    norm["total"] = computed
    norm.setdefault("domain", None)
    norm.setdefault("load_bearing_assumption", None)
    norm.setdefault("tripwires", None)
    norm.setdefault("expiry", None)
    norm.setdefault("gate_question", None)
    norm.setdefault("confidence", None)
    norm.setdefault("calibration", None)
    return norm


def read_lines(ledger_dir: Path) -> list[dict]:
    f = ledger_dir / "ledger.jsonl"
    if not f.exists():
        return []
    rows = []
    for ln in f.read_text().splitlines():
        ln = ln.strip()
        if ln:
            try:
                rows.append(json.loads(ln))
            except json.JSONDecodeError:
                pass  # tolerate a hand-edited bad line rather than crash
    return rows


def write_lines(ledger_dir: Path, rows: list[dict]) -> None:
    f = ledger_dir / "ledger.jsonl"
    f.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def cmd_lookup(args, ledger_dir: Path) -> int:
    rows = read_lines(ledger_dir)
    url = (args.url or "").strip().lower()
    idea = (args.idea or "").strip().lower()
    hits = []
    for r in rows:
        r_url = str(r.get("url", "")).strip().lower()
        exact = url and r_url and (url == r_url or url.rstrip("/") == r_url.rstrip("/"))
        fuzzy = 0.0
        if idea and r.get("idea_one_liner"):
            fuzzy = difflib.SequenceMatcher(None, idea, str(r["idea_one_liner"]).lower()).ratio()
        if exact or fuzzy >= 0.6:
            hits.append({
                "date": r.get("date"), "verdict": r.get("verdict"), "total": r.get("total"),
                "url": r.get("url"), "idea_one_liner": r.get("idea_one_liner"),
                "calibration": r.get("calibration"), "gate_question": r.get("gate_question"),
                "match": "url" if exact else f"fuzzy:{fuzzy:.2f}",
            })
    print(json.dumps({"count": len(hits), "matches": hits}, indent=2, ensure_ascii=False))
    return 0


def cmd_append(args, ledger_dir: Path) -> int:
    run = validate_run(json.loads(args.run))
    ledger_dir.mkdir(parents=True, exist_ok=True)
    rows = read_lines(ledger_dir)
    rows.append(run)
    write_lines(ledger_dir, rows)

    slug = f"{run['date']}-{slugify(run.get('idea_one_liner') or run.get('url'))}"
    md_path = ledger_dir / f"{slug}.md"
    if args.body_file and Path(args.body_file).exists():
        body = Path(args.body_file).read_text()
    else:
        sc = run["scores"]
        body = (
            f"# Council verdict — {run.get('idea_one_liner','(idea)')}\n\n"
            f"- Date: {run['date']}\n- URL: {run['url']}\n"
            f"- Verdict: {run['verdict']} — total {run['total']}/25\n"
            f"- Domain: {run.get('domain')}\n- Confidence: {run.get('confidence')}\n"
            f"- Expiry: {run.get('expiry')}\n\n"
            f"## Scores\n"
            + "".join(f"- {a}: {sc[a]}\n" for a in AXES)
            + f"\n## The one thing that must be true\n{run.get('load_bearing_assumption')}\n"
            f"\n## Tripwires\n{run.get('tripwires')}\n"
            f"\n## Gate question\n{run.get('gate_question')}\n"
        )
    md_path.write_text(body)
    print(json.dumps({"appended": True, "jsonl": str(ledger_dir / 'ledger.jsonl'),
                      "record": str(md_path), "verdict": run["verdict"],
                      "total": run["total"]}, ensure_ascii=False))
    return 0


def cmd_calibrate(args, ledger_dir: Path) -> int:
    result = args.result.strip().lower()
    if result not in {"right", "wrong", "ambiguous"}:
        print(json.dumps({"error": "result must be right|wrong|ambiguous"}), file=sys.stderr)
        return 2
    key = args.match.strip().lower()
    rows = read_lines(ledger_dir)
    updated = 0
    for r in rows:
        hay = f"{r.get('date','')} {r.get('url','')} {r.get('idea_one_liner','')}".lower()
        if key in hay:
            r["calibration"] = result
            updated += 1
    if updated:
        write_lines(ledger_dir, rows)
    print(json.dumps({"updated": updated, "result": result}, ensure_ascii=False))
    return 0 if updated else 1


def cmd_tally(args, ledger_dir: Path) -> int:
    rows = read_lines(ledger_dir)
    counts = {"right": 0, "wrong": 0, "ambiguous": 0, "pending": 0}
    for r in rows:
        c = (r.get("calibration") or "pending")
        counts[c] = counts.get(c, 0) + 1
    scored = counts["right"] + counts["wrong"]
    record = (f"council record: {counts['right']} right, {counts['wrong']} wrong"
              f" across {scored} retested ideas"
              + (f" ({counts['ambiguous']} ambiguous, {counts['pending']} awaiting outcome)"
                 if counts['ambiguous'] or counts['pending'] else ""))
    print(json.dumps({"total_runs": len(rows), "counts": counts, "record": record},
                     indent=2, ensure_ascii=False))
    return 0


def cmd_validate(args, ledger_dir: Path) -> int:
    try:
        run = validate_run(json.loads(args.run))
    except (ValueError, json.JSONDecodeError) as e:
        print(json.dumps({"valid": False, "error": str(e)}), file=sys.stderr)
        return 2
    print(json.dumps({"valid": True, "total": run["total"], "verdict": run["verdict"]}))
    return 0


def self_test() -> int:
    with tempfile.TemporaryDirectory() as d:
        led = Path(d)
        run = {
            "date": "2026-07-18", "idea_one_liner": "AI follow-up emails for consultants",
            "url": "https://example.com", "verdict": "kill it",
            "scores": {"pain": 3, "wtp": 2, "wedge": 2, "distribution": 2, "timing": 2},
            "load_bearing_assumption": "consultants treat the edit as removable toil",
            "tripwires": "if <7 of 15 interviews show the pain unprompted -> KILL",
            "gate_question": "what did discovery interviews reveal?", "confidence": "medium",
        }
        class A: pass
        a = A(); a.run = json.dumps(run); a.body_file = None
        assert cmd_append(a, led) == 0
        assert (led / "ledger.jsonl").exists()
        assert list(led.glob("2026-07-18-*.md"))
        rows = read_lines(led)
        assert rows[0]["total"] == 11 and rows[0]["verdict"] == "KILL IT", rows[0]
        # lookup by url
        b = A(); b.url = "https://example.com"; b.idea = None
        assert cmd_lookup(b, led) == 0
        # calibrate + tally
        c = A(); c.match = "example.com"; c.result = "wrong"
        assert cmd_calibrate(c, led) == 0
        assert read_lines(led)[0]["calibration"] == "wrong"
        e = A()
        assert cmd_tally(e, led) == 0
        # reject a bad total
        bad = dict(run); bad["total"] = 99
        f = A(); f.run = json.dumps(bad)
        assert cmd_validate(f, led) == 2
    print("ledger.py self-test: PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Deterministic council ledger.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Run record JSON (for `append` / `validate`). Required: date, idea_one_liner, url,\n"
            "scores, verdict. Optional: total (checked against sum), domain, load_bearing_assumption,\n"
            "tripwires, expiry, gate_question, confidence, calibration.\n"
            "  scores keys: pain, willingness_to_pay (wtp/payer), wedge, distribution, timing_moat (timing) — each 1..5\n"
            "  verdict: 'BUILD IT' | 'PIVOT' | 'KILL IT'\n\n"
            "Examples:\n"
            "  python3 scripts/ledger.py lookup --url https://acme.com --idea 'ai email tool'\n"
            "  python3 scripts/ledger.py append --run '{\"date\":\"2026-07-18\",\"idea_one_liner\":\"...\",\n"
            "     \"url\":\"https://acme.com\",\"verdict\":\"KILL IT\",\n"
            "     \"scores\":{\"pain\":3,\"wtp\":2,\"wedge\":2,\"distribution\":2,\"timing\":2}}'\n"
            "     [--body-file path/to/full-verdict.md]\n"
            "  python3 scripts/ledger.py calibrate --match acme.com --result wrong\n"
            "  python3 scripts/ledger.py tally\n"
        ),
    )
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--ledger-dir", help="override the ledger directory")
    sub = ap.add_subparsers(dest="cmd")

    p = sub.add_parser("lookup"); p.add_argument("--url"); p.add_argument("--idea")
    p = sub.add_parser("append"); p.add_argument("--run", required=True); p.add_argument("--body-file")
    p = sub.add_parser("calibrate"); p.add_argument("--match", required=True); p.add_argument("--result", required=True)
    sub.add_parser("tally")
    p = sub.add_parser("validate"); p.add_argument("--run", required=True)

    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.cmd:
        ap.print_help(); return 2
    ledger_dir = Path(args.ledger_dir) if args.ledger_dir else default_ledger_dir()
    return {
        "lookup": cmd_lookup, "append": cmd_append, "calibrate": cmd_calibrate,
        "tally": cmd_tally, "validate": cmd_validate,
    }[args.cmd](args, ledger_dir)


if __name__ == "__main__":
    raise SystemExit(main())
