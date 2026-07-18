<!-- Keep it focused: one idea per PR. -->

**What this changes and why**


**How it keeps the council honest** (check all that apply)

- [ ] Doesn't ask the founder for revenue / sales / LOIs / customers (early-stage rule)
- [ ] Doesn't tilt the verdict toward negative *or* positive — evidence decides
- [ ] Keeps the E0–E4 evidence grading discipline
- [ ] No dollar-sign-immediately-before-a-digit anywhere

**Checks run**

- [ ] `python3 scripts/score.py --self-test`
- [ ] `python3 scripts/ledger.py --self-test`
- [ ] `grep -rnE '\$[0-9]' --include='*.md' --include='*.py' .` prints nothing

**A before/after from a real run, if you have one**
