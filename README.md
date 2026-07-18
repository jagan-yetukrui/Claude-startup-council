<div align="center">

# ⚖️ The Council

### Put your startup idea on trial before you spend six months building it.

A [Claude Code](https://claude.com/claude-code) skill. Give it your idea in a paragraph and your
website. It runs real research, argues the idea out in a live courtroom, and hands you one clear
verdict — build it, reshape it, or walk away — with the reasoning a sharp advisor would actually give.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Claude Code skill](https://img.shields.io/badge/Claude%20Code-skill-8A2BE2)
![Made with agents](https://img.shields.io/badge/agents-11%2B%20per%20run-orange)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

It is not a cheerleader and not a hater. It doesn't try to prove you right or wrong. It tests the
idea as hard as it can and tells you the truth, whichever way it falls. A strong idea earns a
confident **build it**. A weak one earns an honest **walk away**. Both have to be earned with
evidence — never a reflex.

## Contents

- [What a verdict looks like](#what-a-verdict-looks-like)
- [Why it's different](#why-its-different)
- [Setup](#setup)
- [Using it](#using-it)
- [Updating](#updating)
- [Removing it](#removing-it)
- [What you get](#what-you-get)
- [How it works](#how-it-works)
- [Your privacy](#your-privacy)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

## What a verdict looks like

A trimmed real run on *"a tool that auto-drafts and monitors SOC 2 evidence for tiny B2B startups."*

> ### ⚖️ THE CALL
> **BUILD IT** — the money question is already answered: companies pay Vanta and Drata thousands a
> year to solve exactly this pain, and the tiny-team end of that market is genuinely thin right now.
> This is a fragile build, though. It rides on one bet: that you can reach small startups before
> Vanta walks a cheap tier down to them.
>
> | What I looked at | Score | In plain words |
> |---|---|---|
> | How badly it hurts | 5 | Founders say it straight: "we lost an enterprise deal because we didn't have SOC 2 yet." |
> | Will anyone pay | 5 | Vanta charges 7,000–25,000 a year and has thousands of customers. The budget already exists. |
> | Can you get a foothold | 3 | Real seam — incumbents skew enterprise — but "cheaper Vanta" is a price gap, not a moat. |
> | Can you reach them | 3 | The soft spot. Thousands of tiny startups, no obvious repeatable channel yet. |
> | Why now / why you | 4 | Enterprises now demand SOC 2 from tiny vendors. You're an ex-auditor. Real, but no lasting wall yet. |
>
> **Total: 20 / 25.**
>
> **What I'd do this week:** don't build anything. Talk to twelve founders who hit a SOC 2 wall in
> the last six months. If fewer than seven faced it recently, treat it as a no. If you can't even
> get twelve on a call through your own network in a week, that's the loudest no of all — it means
> the distribution problem is exactly as bad as you feared.

No jargon, no AI word-salad. One call, a scorecard, what's genuinely strong, what worries it most,
and the cheapest test to find out if you're right.

## Why it's different

- **It researches before it judges.** Three scouts read your site, hunt real customer complaints,
  dig up the startups that already tried this and died, and map what comparable products charge.
  Every claim is graded by how solid the evidence is — hard proof versus a hunch.
- **The agents actually argue.** A Believer, a Skeptic, and an Investor each write their own take,
  then face off in a live, turn-by-turn hearing. One makes a point, another objects, the first
  answers back. Weak arguments die under questioning instead of sitting unchallenged.
- **Built for early stage.** It never asks you for revenue, letters of intent, or paying customers.
  You don't have those yet — that's the point. It reasons from the market, not from proof you can't
  have.
- **Honest in both directions.** A council that kills everything is as useless as one that blesses
  everything. A build and a kill each have to be earned with evidence.
- **Plain-English verdict.** Written like a person talking to you, not a machine generating a report.
- **It keeps score of itself.** Every verdict is saved with a prediction. Run the test, come back,
  and it grades its own call right or wrong. Over time you see how good its judgment actually is.

## Setup

You need [Claude Code](https://claude.com/claude-code) and `python3`.

**Clone it straight into your skills folder:**

```bash
git clone https://github.com/jagan-yetukrui/Claude-startup-council.git ~/.claude/skills/council
```

Restart Claude Code. Done — run `/council`.

> Prefer to keep the repo elsewhere? Clone it anywhere, then run `./install.sh` — it links the skill
> into `~/.claude/skills/council` and runs the built-in self-tests.

## Using it

```
/council
Idea: <one paragraph — what it is, who it's for, how it might make money>
Website: <your URL, or "none">
```

It asks up to three quick questions to aim the research (never about sales), then runs. A full run
spins up a dozen-plus agents and does live web research, so give it a few minutes.

Come back later with **"I ran the test"** and it re-opens the case with your new findings, updates
the verdict, and records whether its first call held up.

## Updating

```bash
cd ~/.claude/skills/council && git pull
```

Your saved run history is untouched — it lives in a folder git ignores. Restart Claude Code to pick
up the new version.

## Removing it

```bash
rm -rf ~/.claude/skills/council
```

If you installed with `./install.sh` (a symlink), remove the link and then the repo:

```bash
rm ~/.claude/skills/council        # the symlink
rm -rf /path/to/where/you/cloned   # the repo itself
```

## What you get

- **The call** — build it, reshape it, or walk away, in one sentence.
- **A scorecard** — five things that decide it (how badly it hurts, will anyone pay, can you get a
  foothold, can you reach them, why now / why you), each scored with a plain reason.
- **What's genuinely strong** and **what worries it most** — both, honestly.
- **The one thing that has to be true** for this to work.
- **What to do this week** — a specific, cheap research test with a pass/fail number, plus the
  actual interview questions and outreach copy written out for you.
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

Under the hood it's a small system of specialist instruction files plus two Python scripts that do
the scoring math, so the numbers are never fudged:

| Piece | Job |
|---|---|
| [`SKILL.md`](SKILL.md) | The spine — the running order Claude follows. |
| [`reference/constitution.md`](reference/constitution.md) | The rules every agent obeys. |
| [`reference/scoring-rubric.md`](reference/scoring-rubric.md) | How each of the five scores is earned. |
| [`reference/anti-sycophancy.md`](reference/anti-sycophancy.md) | Keeps the verdict honest both ways — no flattery, no reflexive doom. |
| [`reference/domain-lenses.md`](reference/domain-lenses.md) | Judges a marketplace and a deep-tech idea by different bars. |
| [`reference/voice.md`](reference/voice.md) | Makes the final answer read like a human, not an AI. |
| [`recon/scouts.md`](recon/scouts.md) | The three research scouts. |
| [`members/`](members/) | The Believer, Skeptic, and Investor briefs. |
| [`debate/courtroom.md`](debate/courtroom.md) | The live, turn-by-turn hearing. |
| [`judge/judge-protocol.md`](judge/judge-protocol.md) | How the judge rules. |
| [`scripts/`](scripts/) | Deterministic scoring and the run ledger. |

## Your privacy

The ledger — every idea you run and every verdict — is **yours and stays on your machine**. It's
excluded by `.gitignore` and never leaves your computer. Fork or share this repo and your run
history does not go with it.

## FAQ

**Does it need an API key?** No. It runs inside Claude Code and uses its web access for research.

**Will it just tell me my idea is bad?** No — that was a deliberate design goal. It's built to be
honest in both directions and will give a confident "build it" when the evidence is there. See
[`reference/anti-sycophancy.md`](reference/anti-sycophancy.md).

**Is my idea sent anywhere?** Only to the web searches the research step runs, the same as any
Claude Code session. Your verdicts are saved locally and never uploaded.

**Can I tune it?** Yes — it's all plain-text instruction files. Edit any of them and the change
takes effect on your next run.

## Contributing

Issues and pull requests are welcome — sharper research prompts, new domain lenses, better test
recipes. See [CONTRIBUTING.md](CONTRIBUTING.md).

If it saved you from a bad six months (or gave you the push to build), **star the repo** — it helps
other founders find it.

## License

MIT — use it, change it, ship it. See [LICENSE](LICENSE).
