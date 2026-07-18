# Domain lenses — judge each category by its own bar

A marketplace and a deep-tech idea fail for opposite reasons, so holding them to the same evidence
bar is malpractice. This file gives the judge (and every member) a **category-adaptive lens** to lay
ON TOP OF the shared rubric in `reference/constitution.md`. The five axes, the E0–E4 ladder, and the
25-point bands (≥20 BUILD · 13–19 PIVOT · ≤12 KILL) never change — only *where the scrutiny
concentrates* does: which axis carries the most weight, what strong pre-launch evidence looks like
here, and the one failure mode that kills most ideas of this shape.

## How to use this file

1. **Read the idea and the dossier, then classify** into the ONE primary category the idea lives in.
   Most ideas blend (a fintech marketplace, an AI-native dev tool) — name the **dominant** category
   (where the business will live or die), note the secondary lens in one line. Classify by *business
   model and failure surface*, not surface tech: "GPT for lawyers" billed per seat to firms is B2B
   SaaS wearing an AI hat — judge it as both, dominant lens first.
2. **Apply that lens on top of the shared rubric.** It tells you (b) what E3+ evidence to hunt for,
   (c) the typical killer to check the dossier for, (d) the cheap research test that resolves it, and
   (e) which axes to weight. It does NOT replace the axes or the ladder — it aims them.
3. **If the category's typical killer is present in the dossier, the judge MUST address it by name.**
   A marketplace verdict that never mentions cold-start, or an AI-wrapper verdict that never asks
   whether the model vendor eats it, is incomplete and gets sent back. Absence of the killer from the
   dossier is an `E3-absence` (unproven, not disproven) — weigh it, do not weaponize it.
4. **The lens can only lower confidence, never inflate a score.** A category's favorable axis (e.g.
   bottom-up distribution for dev tools) is not free points; it just moves the burden of proof to the
   axis that usually kills the category. Band overrides remain one-way downward.

---

## B2B SaaS / vertical SaaS

**(a) How to spot it.** Sells to businesses on a seat or subscription model; automates a workflow or
replaces a spreadsheet / manual role; buyer is often not the end user; pitched in ROI and
time-saved terms; frequently vertical-specific (tools built only for dentists, freight brokers, med
spas).

**(b) Strong pre-launch evidence (E3+).** Incumbents with live, real pricing that businesses
demonstrably pay (E4). Documented pain with the current way: one-star reviews of the incumbent,
forum threads about the workflow, job postings for the manual role the software would replace (E3).
A budget line that already exists in this function. Customers visibly duct-taping spreadsheets, Zapier,
and email to do the job today — a documented workaround is E3 proof the pain is real and unmet.

**(c) The typical killer.** *Vitamin, not painkiller* — a genuinely nicer tool for a workflow nobody
is urgently trying to fix, so it never clears the switching-cost hurdle. Its cousin: the buyer
already has a **good-enough module bundled inside an incumbent suite** (Salesforce, SAP, the EHR),
so the real competitor is "do nothing / use the thing we already pay for," and the long enterprise
sales cycle starves a startup before it finds product-market fit.

**(d) The right validation test.** No code needed: find where the target *already spends* on this
job. Count paid seats/pricing of the closest comparable (E4), read the incumbent's one-star reviews
to confirm the pain is switch-worthy rather than cosmetic, and scan job boards for the manual role
being automated. If nobody pays for a comparable and nobody staffs the manual job, the pain is
likely a vitamin.

**(e) Axis emphasis.** **Willingness-to-Pay** and **Wedge** dominate. B2B lives on an existing
budget line and a narrow beachhead vertical you can own before broadening. Pain must be *operational*
(costs money or bodies), not aesthetic. Distribution matters but is rarely the thing that kills it.

## Consumer / prosumer app

**(a) How to spot it.** Sold to an individual; app-store or web, usually freemium; success framed in
engagement/retention/DAU; habit, entertainment, self-improvement, or social; low price, high volume;
growth story leans on virality or content.

**(b) Strong pre-launch evidence (E3+).** Comparable apps showing real *retention* (public D30 or
DAU/MAU, app-store rank-history from public trackers) — engagement, not just downloads. Organic
demand you can measure: subreddit size, hashtag view counts, review volume on comparables (E3). A
behavior people **already do repeatedly** by hand (E3). A waitlist that *converts* is weak (E2);
existing habitual behavior is the real tell.

**(c) The typical killer.** *The retention cliff / no habit loop.* Consumers download and vanish;
there is no organic loop, so paid acquisition becomes a treadmill where CAC outruns a thin LTV. The
silent competitor is free and already installed — Notes, group chat, the browser — and "nice to
have" loses to boredom.

**(d) The right validation test.** Measure the closest comparable's *retention and demand*, not your
own idea's appeal: rank-history, category retention benchmarks, review sentiment. Then locate where
people perform the behavior today to test whether it is genuinely habitual or a one-off. A landing
page measures intent (E2) only — weight it low and never mistake signups for retention.

**(e) Axis emphasis.** **Distribution** and **Pain-as-frequency**. Consumer is a distribution game:
without an organic loop or a genuinely cheap channel, even a loved product dies of CAC. Pain here
means *how often and how automatically* people return, not how loud a survey was.

## Marketplace / two-sided platform

**(a) How to spot it.** Connects two distinct parties (buyers/sellers, riders/drivers, patients/
clinicians); earns a take-rate or commission; the pitch invokes liquidity and network effects; both
supply and demand must be present for a single transaction to happen.

**(b) Strong pre-launch evidence (E3+).** One side **already congregating off-platform** — trading
via Craigslist, Facebook groups, WhatsApp, or shared spreadsheets — which is E3 proof of latent
liquidity and a fragmented, disaffected incumbent. An underserved, reachable supply side. Unit
economics that already close at *small* scale, not only at some imagined national density.

**(c) The typical killer.** *Cold-start (chicken-and-egg) plus negative unit economics on the
constrained side, plus disintermediation.* Marketplaces die because neither side shows up before the
other, because the tolerable take-rate cannot cover CAC on the hard-to-acquire side, or because both
parties meet once on-platform then transact off it forever.

**(d) The right validation test.** Identify the **constrained side** (usually supply), then prove two
things cheaply: you can acquire it below the take-rate it will generate (find where it already
gathers, count it, estimate CAC), and the take-rate survives a real modeled transaction *after*
accounting for leakage. If the parties can easily transact without you, model how you stay in the
loop — or concede you can't.

**(e) Axis emphasis.** **Wedge** and **Distribution**, specifically *supply-side acquisition*. The
only marketplace wedge that works pre-launch is a single geography or vertical where you can
hand-build liquidity manually. WTP is whatever take-rate the market already tolerates — do not
assume you can raise it.

## Developer tool / infrastructure

**(a) How to spot it.** Sold to engineers as an API/SDK/CLI/library, often with an open-source core;
usage-based or seat pricing; the technical buyer is the user; framed around developer experience and
bottom-up adoption.

**(b) Strong pre-launch evidence (E3+).** Developers already hand-rolling the workaround: GitHub
stars on adjacent OSS, high StackOverflow question volume, internal tools people have built and
blogged about (all E3). A painful reliability or integration problem. Paid infra comparables devs
demonstrably expense (E4). Community pull in Discord/HN/issue threads.

**(c) The typical killer.** *Build-vs-buy and commoditization.* Engineers can plausibly build it in a
weekend, or it collapses into free OSS, or the cloud provider ships it as a checkbox (the "AWS
announces it" risk) — so willingness-to-pay evaporates even where adoption is strong. Its twin:
*adoption without monetization*, a beloved OSS project with no revenue path.

**(d) The right validation test.** Determine whether this job is *bought or built* today: search for
existing paid comparables and their pricing, gauge OSS traction of the nearest projects, and confirm
the hard part is genuinely hard (infra, scale, reliability) rather than a scriptable afternoon. Then
name the monetization path that adoption actually converts into — hosting, support, enterprise, or
quota.

**(e) Axis emphasis.** **Timing/Moat** and **Willingness-to-Pay**. Dev tools clone and commoditize
fast; the live question is what stops this from becoming a free feature. Distribution is favorably
bottom-up, so it rarely kills the idea — monetization and defensibility do.

## Deep tech / R&D / hardware

**(a) How to spot it.** Novel science or engineering; a physical device, new material, or new
process; long R&D timeline and heavy capital; patents/IP central; the framing is "*if* we can build
it" — technical risk sits *before* market risk.

**(b) Strong pre-launch evidence (E3+).** Feasibility signals first: published results or comparable
labs/companies hitting the milestones, a credible prototype spec, a defensible read on the physics.
A customer whose pain is severe enough to tolerate an unproven vendor. A manufacturing and
regulatory path that exists. Prior funding into the space is E4 of external technical conviction.

**(c) The typical killer.** *Technical risk that never resolves, or a working device with no
economically viable path.* Either the yield/cost/physics curve refuses to cooperate, or it works in
the lab but cannot hit the cost and scale the market requires — a "science project" whose timeline
and capital exceed what the team can survive.

**(d) The right validation test.** This is the one category where the killer is **technical, not
market**, so the cheap research test is a *feasibility and cost-at-scale teardown*: has anyone hit
these numbers, what is the theoretical limit, what killed prior attempts, and what is the projected
unit cost at volume versus the incumbent technology? Customer discovery comes *second*, after
feasibility clears.

**(e) Axis emphasis.** **Timing/Moat** (what enabling technology *just* changed to make this possible
now) and **Pain** (severe enough to adopt something unproven). WTP is usually obvious *if it works*;
feasibility is the gate. Do not over-weight Distribution this early — it is the wrong risk to
obsess over.

## Fintech / regulated (health, legal, finance)

**(a) How to spot it.** Moves money, or touches PHI/PII, or performs a licensed activity; lives
inside a compliance regime (HIPAA, SOC 2, KYC/AML, state licensing, bar rules); trust is
transaction-critical.

**(b) Strong pre-launch evidence (E3+).** A **clear regulatory path**: others already operate legally
in this exact niche and you can see how (E4). An incumbent charging for the compliant version. A
licensing or partner model that has precedent. Pain acute enough that customers accept compliance
friction. Best of all, evidence that the regulation itself *is* the wedge — a barrier that keeps
casual competitors out.

**(c) The typical killer.** *The regulatory/licensing wall, trust cold-start, and compliance-gated
distribution.* The idea is legal but unlicensable at startup scale, or it needs a bank/insurer/
clearinghouse partner who will not touch a pre-launch team, or trust barriers make CAC brutal — and
compliance cost lands *before* any revenue.

**(d) The right validation test.** Map the **regulatory path before anything else**: who operates
legally here today and under what license or partnership, what enforcement actions have killed peers,
and what the minimum viable compliance to transact actually is. The primary research artifact is a
*regulatory teardown*, not a customer survey — demand is confirmed only after the path exists.

**(e) Axis emphasis.** **Timing/Moat** (the regulatory moat cuts both ways — a barrier to you *and* to
followers) and **Distribution** (trust- and compliance-gated channels). WTP is usually strong in
finance and health; the gate is whether you can *legally reach and serve* the customer at all.

## AI-native / thin-wrapper

**(a) How to spot it.** The core value is a foundation-model call — "GPT for X," prompt orchestration,
a workflow built mostly around an LLM — with differentiation claimed through prompts, UX, or a thin
layer on top of a vendor model.

**(b) Strong pre-launch evidence (E3+).** A **defensible asset the model vendor cannot replicate**:
proprietary data, a deep workflow integration, a distribution lock, or regulated trust (E3 of a real
moat). A paid comparable proving WTP for the *outcome* (not the model). A wedge buried in a workflow
too small or too messy for the vendor to bother with. Real usage of a rough version beats any polished
demo.

**(c) The typical killer.** *The model vendor eats it — feature, not company.* The wrapper is a prompt
anyone can copy in an afternoon; the next model release absorbs the use case natively; there is no
data flywheel, no distribution lock, no switching cost; and inference cost crushes the margin. Zero
defensibility with real demand still equals zero durable business.

**(d) The right validation test.** Ask two questions and research them honestly: *what survives the
next model release*, and *what would the vendor have to acquire rather than build*? Inventory the
defensible asset explicitly. The cheap experiment: try to reproduce the core value with a single
afternoon of prompt engineering — if you can, so can everyone, and there is no company here yet.

**(e) Axis emphasis.** **Timing/Moat above all** — this is the category where moat is the whole game —
then **Wedge**. Pain and WTP are frequently real; the idea almost always dies on defensibility, not
on demand.

## Content / creator / media

**(a) How to spot it.** Value lives in content, audience, or community; monetized by ads,
subscription, or the creator economy; framed as a media brand, newsletter, channel, or creator tool;
audience-first thinking.

**(b) Strong pre-launch evidence (E3+).** An existing audience, or a proven niche with monetized
comparables — Substacks, channels, or media brands in the exact niche pulling real revenue (E4). A
distribution channel the founder can genuinely access. Content that *compounds* (search/evergreen)
rather than a treadmill. Engagement metrics of comparable creators (E3).

**(c) The typical killer.** *The content treadmill, undifferentiated audience, and platform
dependence.* Media dies from an unsustainable production cost per unit of audience, from commoditized
content nobody will pay for (ad CPMs never cover it), and from building on an algorithm/platform you
do not own that can throttle or cut you off overnight.

**(d) The right validation test.** Prove the niche *monetizes* and the distribution *compounds*: find
comparable creators/media in the exact niche, their revenue model, and their audience size, then test
whether the content is search/share-driven (owned, compounding) or algorithm-fed (rented). Put
production cost per piece next to monetization per piece — if that ratio is upside-down, no audience
size fixes it.

**(e) Axis emphasis.** **Distribution** and **Willingness-to-Pay**. Content is a distribution and
monetization game: an audience is easy to claim and hard to own, and most content carries near-zero
*direct* WTP (ads only). The real moat is an *owned* audience relationship the platform cannot sever.

---

## Cross-category warnings

These traps recur regardless of category. When one appears in a dossier, the judge should name it.

- **Big TAM is not a wedge.** A large market attracts incumbents and says nothing about your winnable
  first slice. TAM math is E1 — the weakest evidence on the ladder. A knife-edge beachhead you can
  actually own beats a billion-dollar spreadsheet every time.
- **A feature is not a company.** If the whole idea is a single feature, ask what stops the product it
  is a feature *of* from shipping it next quarter. This bites hardest in AI-wrapper, dev-tool, and
  B2B SaaS ideas.
- **Riding a platform you don't control.** App Store rules, a recommendation algorithm, a model
  vendor's API, a marketplace's data — rented distribution and rented moats can be revoked without
  warning. Recurs in consumer, content, AI-native, and dev-tool ideas.
- **The incumbent's good-enough feature.** You rarely need to beat a dedicated competitor; you need to
  beat the "good enough" module already bundled into the tool the customer *already owns* (Salesforce,
  Excel, the EHR, the Notes app). Switching cost is the silent killer of "objectively better" tools.
- **Intent is not behavior.** Surveys and waitlists are E2; usage is E3; money changing hands is E4.
  Every category over-weights "people said they'd want it." Repeated *unpaid* behavior or real
  spending on a comparable is the only signal that predicts.
- **Founder-market fit is an axis, not a formality.** "Why this team, why now" lives in Timing/Moat
  for a reason: a strong idea with no unfair distribution, insight, or timing advantage is a coin
  flip against everyone else who can read the same market.
