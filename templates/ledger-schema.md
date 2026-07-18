# Ledger schema

The ledger is the council's memory and its conscience. Two artifacts per run, both under
`ledger/` (relative to the skill base directory). It is **append-only for verdicts** — a past
verdict is never rewritten; `scripts/ledger.py calibrate` only annotates a line's outcome.

Never hand-write these files. Always go through `scripts/ledger.py` — it validates the record,
checks the total against the sum of scores, and keeps the two artifacts in sync. Run
`python3 scripts/ledger.py --help` for the authoritative interface.

## 1. `ledger/ledger.jsonl` — one compact line per run

```json
{
  "date": "2026-07-18",
  "idea_one_liner": "one-sentence neutralized description of the idea",
  "url": "https://example.com",
  "scores": {"pain": 3, "willingness_to_pay": 2, "wedge": 2, "distribution": 2, "timing_moat": 2},
  "total": 11,
  "verdict": "KILL IT",
  "domain": "B2B SaaS",
  "load_bearing_assumption": "the single thing that must be true",
  "tripwires": "the pre-registered signal thresholds + deadline",
  "expiry": "stale after 2026-10-10 or first E4 event",
  "gate_question": "the one real-world question before any re-run",
  "confidence": "medium",
  "calibration": null
}
```

Field notes:
- **scores** — the five axes, integers 1–5. Aliases accepted by the script: `wtp`/`payer` →
  `willingness_to_pay`, `timing` → `timing_moat`. The judge's own scores go here (not the
  member medians).
- **total** — optional on input; the script computes it from the scores and rejects a mismatch.
- **verdict** — exactly `BUILD IT`, `PIVOT`, or `KILL IT`.
- **calibration** — `null` until a retest resolves it, then `right` / `wrong` / `ambiguous`.
  This is the only field ever changed after write, and only via `calibrate`.

> Backward compatibility: early entries may use the old axis key `payer` (now `willingness_to_pay`)
> and a revenue-based gate question from before the early-stage reframe. The script reads them
> correctly via aliasing. Never rewrite a past entry — the ledger is honest history, including the
> calls the council later revised.

## 2. `ledger/<date>-<slug>.md` — the full human record

Written by `append`. If you pass `--body-file PATH`, that file's contents become the record (use
this to store the complete verdict output verbatim). Otherwise the script writes a compact record
from the JSON fields. The shareable artifact, if the founder wants one, renders from this file so a
later retest can update the same artifact.

## Lifecycle

```
cold run   -> ledger.py append   (writes jsonl line + md record, calibration: null)
retest     -> ledger.py lookup   (find the prior run by url/idea)
           -> ledger.py calibrate (set the prior line's calibration from the test result)
           -> ledger.py append    (write the retest as a new line)
anytime    -> ledger.py tally     (the running right/wrong record, surfaced in output)
```
