# Round 2 — the courtroom

This file governs the live argument round (SKILL.md **Step 3**). Round 1 gave you three independent,
blind reports — clean parallel monologues. Round 2 is the opposite: the three members argue **out
loud, in sequence, reacting to each other in real time**, until each finding is either pressure-
tested into something firmer or exposed as thin. The ordered transcript you produce here, plus each
member's revised scorecard, is **Dataset B** — handed to the judge alongside the reports. You are
bound by `reference/constitution.md` first (the early-stage rule, the E0–E4 ladder, the five axes,
anti-fabrication, the dollar-sign landmine). This file governs the live *sequence*; each member's own
`members/*.md` §5 governs *what* that member argues (cross-examine / defend / close / re-score).

## 1. THE PRINCIPLE

A hearing, not a filing round. Members do not re-read their reports at each other in parallel. One
speaks; the next reacts to **the exact sentence just said**; the first answers; a third interjects —
back and forth, like a courtroom, until the truth is pressure-tested. Every reaction is aimed at a
**specific prior statement**, quoted or named, not at a vibe or a tone.

- **The goal is truth, not victory.** This is a trial to *find* the strongest true reading of the
  idea, not a pile-on. Nobody "wins" by talking longest or hitting hardest; a point wins by surviving
  a graded, specific attack. A cheap kill of a weak version is a protocol violation for every member,
  the Skeptic included.
- **Balance is mandatory (state this to every member).** The Believer must be allowed to **win
  points** — when a finding survives cross-examination, it comes out of Round 2 *stronger*, and the
  judge weights it up. The Skeptic and Investor **must concede** genuine strengths when they land;
  "nothing to concede" across a whole hearing is itself a tell the judge discounts. A good idea has to
  be able to survive this room. If it can't survive an honest hearing, that is the finding.
- **Every claim carries its grade.** No fabricated evidence, no invented competitor, quote, or price.
  Any claim not in the dossier is E0 — an assumption, said out loud as one.

## 2. ROLES

**The MODERATOR (you, the orchestrator).** You have **no opinion** and you never argue, grade, or
score. You direct: you name the cruxes, decide who speaks next per the script below, feed each
speaker only what they must react to, enforce the word caps, and cut theater (repetition, tone-
attacks, speeches that don't answer the question put to them). You keep time and you keep order. You
never take a side, never supply evidence, never hint at the verdict. If a member drifts, you re-issue
the one-line instruction — you do not fill the gap yourself.

**The three members — litigants (live subagents from Round 1).** Believer (case FOR), Skeptic (case
AGAINST), Investor (commercial read). Their context is intact from Round 1; you continue them via
SendMessage — **never re-send the dossier or their reports.** Each is now a litigant: it must react
to **what was actually just said this round**, by name, not restate its report. It argues only the
strongest honest version of an opponent's point (constitution §5), grades every claim, and concedes
what genuinely lands.

## 3. TURN FORMAT

Every turn is **one speaker, ≤150 words**, and **opens with a MOVE label** naming what it is doing:

- **ASSERT** — state one point and argue it from graded evidence. Used to open an exchange.
- **OBJECT** — challenge a **specific prior statement**. Must (1) quote or name the exact point being
  challenged and (2) give the ground: *weak evidence grade* / *logical flaw* / *ignored alternative*
  / *overreach beyond what the evidence supports* / *unfounded assumption* — then argue it. An OBJECT
  with no named target or no ground is theater; the moderator sends it back.
- **REBUT** — answer an objection directly, on its own terms. If part of the objection landed, the
  rebuttal must CONCEDE that part precisely before defending the core.
- **CONCEDE** — grant a point that genuinely landed. **Required when it did.** A clean concession is
  credibility, not weakness (constitution §5); refusing to concede anything all hearing is discounted
  by the judge.
- **QUESTION** — put one sharp, answerable question to a named member, who **must answer on their
  next turn**. Use it to force a claim's evidence into the open ("name the comparable that pays, or is
  that E1?").

A turn may lead with one label and close by opening a QUESTION — that's fine, but keep to ≤150 words.
No new fabricated evidence in any move; every factual claim carries its E-grade.

## 4. THE HEARING STRUCTURE

The moderator runs one bounded, sequential script.

**(a) Name the cruxes.** Before anyone speaks, the moderator writes **1–2 CRUXES** — the sharpest
*collisions* between the reports, each phrased as a question decidable by research or a cheap test
(never a revenue/LOI question, never a dollar sign before a digit). A crux is where the reports most
directly contradict each other, e.g. "Is the month-end pain a painkiller people already route around
(Believer, E3) or a vitamin the status quo absorbs (Skeptic)?"

**Assigning sides.** For each crux, the **affirmative** is the member whose report most strongly
asserts the contested claim; the **natural opponent** is the member who most directly contradicts it;
the **third** interjects. Balance rule: the moderator **must assign the Believer the affirmative on
at least one crux**, so the case FOR gets a fair chance to win points. On Crux 2 the roles **flip** —
a different member holds the affirmative.

**(b) EXCHANGE ON CRUX 1** — affirmative asserts, opponent objects, affirmative rebuts, third
interjects, affirmative answers.

**(c) EXCHANGE ON CRUX 2** — same shape, **roles flipped** (new affirmative).

**(d) FREE CROSS** — one round: any member may fire their **single strongest *remaining* objection**
at any other, who must answer (REBUT or CONCEDE). Skip any member whose only remaining objection is a
repeat (see §5).

**(e) CLOSINGS** — each member one **≤120-word** closing argument addressed to the judge.

**(f) REVISED SCORECARDS** — each member privately submits its five scores (Pain, Willingness-to-Pay,
Wedge, Distribution, Timing/Moat, fixed order) plus **one line on what the debate moved and why** —
or "unmoved, because [grade + fact]." A scorecard that never moves under fire is not believed; a
score moved *down* when an opponent lands a real hit is a strength.

### Exact turn order (the moderator follows this mechanically)

Setup — moderator posts Crux 1 and Crux 2 (not a speaking turn).

Crux 1 exchange:
1. **Affirmative-1 — ASSERT** the affirmative of Crux 1.
2. **Opponent-1 — OBJECT** to turn 1 (name it + ground).
3. **Affirmative-1 — REBUT** turn 2 (CONCEDE any part that landed).
4. **Third — QUESTION or fresh OBJECT** on turns 1–3.
5. **Affirmative-1 — REBUT / answer** turn 4.

Crux 2 exchange (roles flipped):
6. **Affirmative-2 — ASSERT** the affirmative of Crux 2.
7. **Opponent-2 — OBJECT** to turn 6.
8. **Affirmative-2 — REBUT** turn 7 (CONCEDE if it landed).
9. **Third — QUESTION or fresh OBJECT** on turns 6–8.
10. **Affirmative-2 — REBUT / answer** turn 9.

Free cross (single round):
11. **A member — OBJECT** (strongest remaining objection, to any other member).
12. **Target — REBUT or CONCEDE.**
13. **A different member — OBJECT** (strongest remaining).
14. **Target — REBUT or CONCEDE.**

**Cap: 14 speaking turns before closings** (typically 12–14). If a genuine, *new* third objection
remains and the count is below 14, the moderator may run one more pair up to the cap — never past it.
If free cross produces only repeats, it ends early at turn 12 (or sooner).

Then, outside the cap:
15–17. **Each member — CLOSING** (≤120 words, one per member).
Then each member submits its **REVISED SCORECARD** privately (not a speaking turn).

This maps onto each member's `members/*.md` §5 four-move brief: the OBJECT turns are its *cross-
examine*, the REBUT turns its *defend*, turns 15–17 its *closing*, and the private scorecard its
*revised scorecard* — delivered live across turns instead of in one block.

## 5. TERMINATION & ANTI-LOOP

- **Stop an exchange early** the moment the last objection got a real, on-point answer and **no NEW
  objection is raised.** A repeat of an earlier point, or the same point reworded, **does not count as
  new** — the moderator recognizes it and moves on. Do not let members circle a point that has been
  answered.
- **No last-word-by-volume.** A member does not get to prevail by speaking most or loudest. The
  moderator enforces the turn order and the ≤150-word cap; an over-length or off-target turn is sent
  back once, then the moderator moves to the next scheduled speaker.
- **Exactly one hearing.** One pass through the script, one set of closings, one revised scorecard per
  member. There is no re-run, no "best of three," no reopening after closings. A second argument round
  is a protocol violation (SKILL.md Step 3).

## 6. HOW THE MODERATOR RUNS IT MECHANICALLY

Maintain a single **running transcript**: an ordered list of turns, each stamped `Turn N — MEMBER —
MOVE:` followed by the member's words. For each turn in the order above:

1. **Send the delta, not the world.** SendMessage the target member (context intact — never re-send
   the dossier or reports). Include only the **new transcript since that member last spoke** (the
   turns they haven't seen) plus a **one-line instruction naming exactly what to respond to** and the
   move you expect — e.g. *"OBJECT to the Believer's Turn 1 claim that the pain is a painkiller; name
   the ground and the grade,"* or *"REBUT the Skeptic's Turn 2 objection, then re-score if it moved
   you,"* or *"CLOSING to the judge, ≤120 words."*
2. **Collect the reply**, check it: right move label, ≤150 words (≤120 for closings), names a specific
   target for any OBJECT, grades its claims, no fabricated evidence. If it fails, re-issue the one-line
   instruction once; do not rewrite it yourself and do not supply evidence.
3. **Append** the accepted turn to the running transcript.
4. **Decide the next speaker** strictly per §4's numbered order, applying the §5 anti-loop stops.

When closings are in and the three revised scorecards are collected, freeze the transcript. The
**full ordered transcript + the three revised scorecards = Dataset B**, handed verbatim to the judge
(SKILL.md Step 4) alongside Dataset A and the cruxes. Preserve turn order and grades exactly — the
gap between what a finding claimed in Round 1 and what survived here is the signal the judge weighs.

## 7. ILLUSTRATIVE SNIPPET

A made-up idea — *an AI tool that drafts month-end reconciliation for solo bookkeepers on
QuickBooks.* Crux 1: "Is the month-end pain a painkiller people already route around, or a vitamin?"
(Believer affirmative, Skeptic opponent, Investor third.) Texture only — keep turns this tight.

> **Turn 1 — BELIEVER — ASSERT.** Painkiller. Dossier VOICES has a solo bookkeeper on G2: "I rebuild
> the same reconciliation macro in Excel every single month" (E3). Nobody hand-maintains a monthly
> macro for a problem that doesn't hurt. That recurring rebuild *is* the pain, observed in behavior.

> **Turn 2 — SKEPTIC — OBJECT.** To Turn 1's "the market feels this" leap — ground: overreach. One G2
> review is a single E3 voice, n=1, not a market. The dossier flags SILENT MARKET: pain-phrased
> searches surfaced no complaint cluster. One quote can't carry "painkiller"; it caps at unvalidated.

> **Turn 3 — BELIEVER — REBUT + CONCEDE.** Conceded: n=1 can't prove market-wide demand, and I won't
> claim it does. But the *workaround* is behavioral evidence independent of volume — she rebuilds the
> macro monthly (E3), which is effort spent routing around the gap. That's a painkiller signal for
> this role, even if breadth is still open.

> **Turn 4 — INVESTOR — QUESTION.** To the Believer: name one comparable with **paying** users at your
> implied price — or is willingness-to-pay resting on E1 analogy?

> **Turn 5 — BELIEVER — REBUT.** Not analogy. The dossier lists a reconciliation add-on charging
> forty dollars a month with review volume in the hundreds (E4: live pricing + sustained usage). The
> budget line exists; this buyer already funds it.

> **Turn 6 — SKEPTIC — CONCEDE.** Granting the workaround point: the monthly macro rebuild is real E3
> behavior, and "painkiller for the solo bookkeeper specifically" survives — I move Pain up. My kill
> stands on **Distribution**, not Pain: I still see no affordable channel to reach these bookkeepers
> one at a time, and that's where I'll press in free cross.

Here the Believer **won a point** (the workaround as grade-E3 behavioral evidence, which survived and
gets weighted up), and the Skeptic made a **genuine concession** (Pain moves up) while relocating the
real fight to Distribution — exactly the texture the judge reads out of Dataset B.
