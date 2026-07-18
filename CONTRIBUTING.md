# Contributing to The Council

Thanks for wanting to make this better. The Council is a set of plain-text instruction files and two
small Python scripts, so contributing is approachable — no build step, no framework.

## Good first contributions

- **Sharper research prompts** — better search strategies in [`recon/scouts.md`](recon/scouts.md).
- **New domain lenses** — a category we don't cover well yet in
  [`reference/domain-lenses.md`](reference/domain-lenses.md) (climate, biotech, games, hardware...).
- **Better validation tests** — cheaper, sharper week-one experiments in
  [`templates/verdict-output.md`](templates/verdict-output.md).
- **Voice fixes** — catch any jargon or AI-slop that slips into the output
  ([`reference/voice.md`](reference/voice.md)).

## Ground rules that keep the council honest

Please keep these intact — they are the whole point:

1. **Early-stage rule.** Never add anything that asks the founder for revenue, sales, letters of
   intent, prepays, or customers. The council reasons from market research, not the founder's wallet.
2. **Honest in both directions.** Don't tilt it toward negative *or* positive. A build and a kill
   both have to be earned with evidence.
3. **Evidence-graded.** Claims are graded E0–E4 (see
   [`reference/constitution.md`](reference/constitution.md)). Keep that discipline.
4. **No dollar-sign-then-digit.** Write "200 dollars a month", never the symbol followed by a digit —
   the skill loader mangles it. There's a check for this below.

## Before you open a PR

Run the self-tests and the landmine check:

```bash
python3 scripts/score.py --self-test
python3 scripts/ledger.py --self-test
# should print nothing (no dollar-sign-then-digit anywhere):
grep -rnE '\$[0-9]' --include='*.md' --include='*.py' .
```

Keep changes focused — one idea per PR. Explain what problem it solves and, if you can, paste a
before/after from a real run.

## Reporting issues

Open an issue with the idea you ran (or a made-up one that reproduces it), what verdict you got, and
what you expected. Never paste anything private — your local ledger stays local for a reason.
