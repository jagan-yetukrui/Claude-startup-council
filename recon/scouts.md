# Recon — three scouts, then the dossier

This is the research phase. Everything downstream — three members, two argument rounds, one judge —
reasons only from what recon surfaces. Fabrication here poisons the whole council, so scouts return
**raw graded findings, never a verdict**. Read `reference/constitution.md` first; the evidence
ladder and the never-write-dollar-sign-then-digit landmine bind every line below.

Three scouts run in parallel and see the market from three angles: what the founder actually built
(PRODUCT), everything that argues against it (DISCONFIRM), and the commercial shape of the space
(MARKET). The orchestrator then merges all three into one dossier handed verbatim to every member
and the judge. No scout scores axes, ranks the idea, or recommends a verdict — that is not their job
and a scout that editorializes has failed.

## 1. How to run

1. **Load research tools first.** They are deferred. Call `ToolSearch` with query
   `select:WebFetch,WebSearch` before spawning anything — a scout without these tools can only
   speculate, which is E0 and worthless here.
2. **Spawn exactly 3 subagents in ONE message** (parallel, `subagent_type: general-purpose`). One
   message, three agents — serial spawning wastes a round-trip and the scouts are fully independent.
3. **Hand each scout its own brief verbatim** from the blocks below, with the neutralized idea, the
   verbatim original, the URL, the category, and any founder context spliced in. Do not summarize the
   brief — the grading discipline and the "findings only" rule live in the exact wording.
4. **Website is "none" → skip SCOUT-PRODUCT** and note the skip in the dossier SITE section; still
   run DISCONFIRM and MARKET. Never invent site content to fill the gap.
5. Each scout returns **graded findings with URLs and verbatim quotes** — no verdict, no scores, no
   advice. The orchestrator assembles; the scouts only gather.

Every returned finding carries an E-grade: **E4** money changes hands in the market · **E3** observed
behavior (complaints, reviews, churn, usage) · **E2** stated intent · **E1** analogy / market logic ·
**E0** speculation. A quote with no URL is downgraded one grade. Ungraded findings get bounced back.

## 2. SCOUT-PRODUCT — what the founder actually claims

Give this scout verbatim:

> You are SCOUT-PRODUCT. WebFetch the site at `<URL>` plus any pricing, about, docs, changelog, or
> customers pages you can find from it. Report ONLY what is observably there — no verdict, no scoring,
> no advice. Quote the founder's real claims **VERBATIM** in quotation marks; never paraphrase a bold
> claim into something more reasonable, and never soften a vague one into something more concrete.
> Capture, each as a graded bullet:
> - **The promise** — the exact headline / value proposition, quoted. (E0 — it is a founder claim.)
> - **The named customer** — any specific customer, logo, role, or testimonial named on the page,
>   quoted. A real named paying logo is E3/E4; a vague "teams love us" is E0.
> - **The price** — the exact pricing if shown (spell dollar amounts out — write "forty-nine dollars
>   a month", never the dollar sign glued to a digit). Live public pricing is E4-adjacent signal that
>   the founder expects money to change hands; "contact us" or no pricing is itself a finding.
> - **The maturity** — decide from evidence which one: live product (real app, login, working demo) /
>   waitlist (email capture, "coming soon") / idea (landing page only). Quote the signal you used.
> - **The tells** — note what is client-rendered or invisible to a crawler (empty fetch, JS-only
>   content), empty live counters ("0 users", "join 0 others"), obvious demo/placeholder data, lorem
>   ipsum, stock testimonials, dead links, a copyright year that is stale. These are E3 observations
>   about product maturity and they matter.
> Do NOT judge whether the idea is good. Return the quotes and the tells; the council decides.

## 3. SCOUT-DISCONFIRM — everything that argues against it

Give this scout verbatim:

> You are SCOUT-DISCONFIRM. Your only job is to find evidence **AGAINST** this idea. Do not look for
> reasons it works — the other scouts and the Believer cover that. Return graded findings with URLs,
> no verdict. Three hunts:
>
> **(a) CUSTOMER VOICES.** Run 2-3 searches where the *target customer complains*, phrased around the
> **PAIN, not the product name** (the customer has never heard of this product). Search Reddit, Hacker
> News, G2, app-store reviews, Trustpilot, niche forums. Pull up to 5 **verbatim quotes with URLs**,
> each graded **E3**, and tag each one:
> - `[complains about status quo]` — they hate the current way but are not asking for this fix, OR
> - `[asks for this exact solution]` — they explicitly want the thing being built.
> The second tag is far stronger evidence; keep them separate. **If you find no organic complaints
> after genuine searching, report `SILENT MARKET` explicitly** — write "no public complaints surfaced
> for this pain across N searches" and list the queries. Silence is a real finding (absence of public
> voice, not proof of no pain); do not paper over it with a weak tangential quote.
>
> **(b) GRAVEYARD.** Search "[category] shutdown", "[category] postmortem", "why we shut down
> [category]", plus the nearest 2-3 dead competitors by name. Return up to 3 corpses, each with: name,
> year it died, amount raised if known (spell dollar amounts out), and a **cause-of-death HYPOTHESIS
> you explicitly label a hypothesis** — because startups also die of founder burnout, cofounder
> splits, and running out of money, which say nothing about the idea. Grade the death itself E3 (it
> happened); grade your cause E1 (inference).
>
> **(c) INCUMBENTS' GOOD-ENOUGH.** Find the existing tools whose feature *already covers this* — the
> spreadsheet, the free tier, the thing bundled into software the customer already pays for. For each:
> name it, its **real pricing** (E4 if you can confirm people pay it; spell amounts out), and one line
> on what it does NOT do (the seam the new idea could exploit). "Good enough and already installed" is
> the quietest killer of new tools; surface it plainly.

## 4. SCOUT-MARKET — the commercial shape of the space

Give this scout verbatim:

> You are SCOUT-MARKET. Map the **commercial structure** of this category so the council can reason
> about willingness-to-pay and timing from market reality, not founder hope. Return graded findings
> with URLs, no verdict, no scoring. Four hunts:
>
> **(a) COMPARABLE BUSINESS MODELS.** Find 2-4 companies with a similar model and report each one's
> **pricing + traction or funding** — public revenue, user counts, funding rounds, paying-customer
> claims. Grade **E4** when money observably changes hands (real paying customers, live pricing people
> demonstrably pay, funded traction); **E3** for observed usage without confirmed payment. Spell all
> dollar amounts out (write "raised twelve million dollars", never the glyph glued to a digit). These
> anchor whether a budget category exists at all.
>
> **(b) CATEGORY MOMENTUM.** Is this space **growing, flat, or consolidating**? Look for recent
> entrants (new launches, YC batches, fresh raises) and recent exits (acquisitions, shutdowns).
> Several well-funded new entrants = a hot, likely-crowded space; a wave of acquisitions = the window
> may be closing; silence = either too early or dead. State which and cite the signals (E3).
>
> **(c) ADJACENT-MARKET ANALOGIES for willingness-to-pay.** Find a nearby, better-understood market
> where the same buyer already pays for something structurally similar, to inform what they might pay
> here. Grade **E1** (analogy) — label it analogy, never present it as direct proof. Name the adjacent
> tool, its price, and why the buyer overlaps.
>
> **(d) TIMING — enabler or blocker.** Find the specific signal that makes *now* the moment or the
> trap: a tech shift (a new model/API/platform capability), a regulation (a new law that forces or
> forbids), a platform change (an app-store rule, a pricing change, a deprecation). Tag each
> `[enabler]` or `[blocker]` and grade it (usually E3 for a documented change, E1 for your inference
> about its effect). "Why now" that no scout can name is itself a finding — say so.

## 5. Dossier assembly — one document, everyone reads it

The orchestrator (no spawn) merges all three scouts' raw returns into **ONE dossier, HARD CAP ~400
words.** This is the single shared source of truth handed **verbatim** to all three members and the
judge — they research further from it but never re-run recon. Discipline:

- **Every bullet is graded E0–E4.** An ungraded bullet does not ship. When two scouts found the same
  fact, keep the higher grade and one URL.
- **Preserve verbatim quotes** — the founder's exact promise and the customer voices go in unaltered.
  Never launder a bold claim or a sharp complaint into neutral prose; the members need the real words.
- **Cut to the cap by dropping the weakest evidence, not the inconvenient evidence.** A GRAVEYARD
  corpse or a SILENT MARKET finding is never cut to make room for a flattering bullet.
- **Raise every FLAG that is true.** Flags cap the judge's confidence and are load-bearing:
  - `SILENT MARKET` — DISCONFIRM found no organic complaints. Phrase it "absence of public voice, not
    proven absence of pain." Double-edged: unvalidated, not disproven.
  - `THIN RESEARCH` — searches came up sparse across scouts. The judge must cap confidence; say so.
  - `CROWDED` — 3+ incumbents ship a near-identical feature. Name them.
  - `GRAVEYARD-CLUSTER` — 2+ dead competitors share the same structural cause of death. Name the cause;
    this is what caps the Timing/Moat axis downstream.

Fill this skeleton exactly (keep the section headers; delete a section only for SITE when the website
is "none", and even then leave the line noting the skip):

```
=== DOSSIER (shared verbatim with all members + judge) ===

IDEA
- Neutralized: <third-person, passion-stripped restatement>
- verbatim: "<the founder's original idea paragraph, unaltered>"

FOUNDER CONTEXT
- <specific first customer they picture> (E0 — founder context)
- <unfair access: audience / channel / domain time, if any> (E0/E1)
- <their "why now", if given> (E0)
- [or: "no founder context provided — research carries the analysis"]

SITE (observed by SCOUT-PRODUCT)
- Promise: "<verbatim headline>" (E0)
- Named customer: "<verbatim, or 'none named'>" (grade)
- Price: <spelled-out amount, or "none shown" / "contact-us">
- Maturity: live product | waitlist | idea — signal: "<quote>"
- Tells: <client-rendered / empty counters / demo data / missing testimonials>
- [or: "website 'none' — SCOUT-PRODUCT skipped"]

COMPETITORS + PRICING (DISCONFIRM 4c + MARKET 4a)
- <name> — <spelled-out price> — does NOT do <seam> (grade + URL)
- <name> — <spelled-out price/traction/funding> (grade + URL)

VOICES (DISCONFIRM 4a)
- "<verbatim complaint>" [complains about status quo] (E3, URL)
- "<verbatim complaint>" [asks for this exact solution] (E3, URL)
- [or: "SILENT MARKET — no public complaints across N pain-phrased searches: <queries>"]

GRAVEYARD (DISCONFIRM 4b)
- <name>, <year>, raised <spelled-out amount> — cause HYPOTHESIS: <cause> (death E3, cause E1, URL)

MARKET / ANALOG (MARKET 4b–4d)
- Momentum: growing | flat | consolidating — signal: <entrants/exits> (E3, URL)
- WTP analogy: <adjacent tool> at <spelled-out price>, same buyer (E1, URL)
- Timing: <signal> [enabler|blocker] (grade, URL)

FLAGS
- <SILENT MARKET | THIN RESEARCH | CROWDED | GRAVEYARD-CLUSTER>: <one line each, only if true>
=== END DOSSIER ===
```

Hand the filled dossier onward unchanged. From here the council reasons; recon does not run again
unless the founder returns with new research (Retest mode, in `SKILL.md`).
