# The Council

**Put your startup idea on trial before you spend six months building it.**

The Council is a skill for [Claude Code](https://claude.com/claude-code). You give it your idea in a
paragraph and your website. It runs real research, argues the idea out in a live courtroom, and hands
you one clear verdict — build it, reshape it, or walk away — with the reasoning a sharp advisor would
actually give you.

It is not a cheerleader and not a hater. It doesn't try to prove you right or wrong. It tests the
idea as hard as it can and tells you the truth, whichever way that falls. A strong idea earns a
confident "build it." A weak one earns an honest "walk away." Both have to be earned with evidence.

## Why it's different

- **It researches before it judges.** Three scouts read your site, hunt for real customer
  complaints, dig up the startups that already tried this and died, and map what comparable products
  charge. Every claim is graded by how solid the evidence is — real proof versus a hunch.
- **The agents actually argue.** A Believer, a Skeptic, and an Investor each write their own take,
  then face off in a live, turn-by-turn hearing. One makes a point, another objects to it, the first
  answers back. Weak arguments die under questioning instead of sitting unchallenged.
- **It's built for early stage.** It never asks you for revenue, signed letters of intent, or paying
  customers. You don't have those yet — that's the whole point. It reasons from the market, not from
  proof you can't have.
- **The verdict is plain English.** No jargon, no AI word-salad. One call, a scorecard, what's
  genuinely strong, what worries it most, and the cheapest test you can run this week to find out if
  you're right.
- **It keeps score of itself.** Every verdict is saved with a prediction. Come back after you run the
  test and it grades its own call right or wrong. Over time you can see how good its judgment is.

## Install

You'll need Claude Code and `python3`.

**Option A — clone straight into place:**

```bash
git clone <repo-url> ~/.claude/skills/council
```

**Option B — clone anywhere and link it:**

```bash
git clone <repo-url> council
cd council
./install.sh
```

Restart Claude Code. That's it.

## Use it

```
/council
Idea: <one paragraph — what it is, who it's for, how it might make money>
Website: <your URL, or "none">
```

It asks up to three quick questions to aim the research (never about sales), then runs. A full run
spins up a dozen-plus agents and does live web research, so give it a few minutes.

Come back later with **"I ran the test"** and it re-opens the case with your new findings, updates
the verdict, and records whether its first call held up.

## What you get

- **The call** — build it, reshape it, or walk away, in one sentence.
- **A scorecard** — five things that decide it (how badly it hurts, will anyone pay, can you get a
  foothold, can you reach them, why now / why you), each scored with a plain reason.
- **What's genuinely strong** and **what worries it most** — both, honestly.
- **The one thing that has to be true** for this to work.
- **What to do this week** — a specific, cheap research test with a clear pass/fail, plus the actual
  interview questions and outreach copy written out for you.
- **If you should reshape it** — one or two sharper versions you can run back through the Council.

## How it works

```
Intake     ->  clean up the idea, check if you've run it before
Research   ->  3 scouts build one evidence-graded brief
Reports    ->  Believer / Skeptic / Investor each write their case, blind to each other
Courtroom  ->  they argue it out, live, objecting to each other's points
Verdict    ->  a judge weighs it all and rules, in plain language
Ledger     ->  the call is recorded so it can be checked later
```

Under the hood it's a set of specialist instruction files plus two small Python scripts that do the
scoring math (so the numbers are never fudged). See [`reference/constitution.md`](reference/constitution.md)
for the rules every agent follows.

## Your privacy

The ledger — every idea you run and every verdict — is **yours and stays on your machine**. It's
excluded from the repo by `.gitignore` and is never uploaded. If you fork or share this repo, your
run history does not go with it.

## License

MIT. Use it, change it, ship it. See [`LICENSE`](LICENSE).
