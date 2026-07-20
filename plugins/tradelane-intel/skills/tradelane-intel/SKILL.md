---
name: tradelane-intel
description: >
  Answer questions about any ocean container-shipping tradelane using live, carrier-published
  data — which carriers and named services run a route, the port rotation and transshipment
  hubs, how concentrated the trade is, and why freight rates on it are moving. Fetches public
  carrier schedules, alliance product docs, freight-rate indices and trade press, applies a
  structured analysis method, and answers WITH citations — never fabricated. Use whenever the
  user asks about container services on a route (e.g. "who runs Asia–West Africa", "what ports
  does OOCL's TLA1 call", "is Vizhinjam a transshipment hub", "why are China–Australia rates
  rising", "which carriers call Chancay"), about port/hub connectivity, a carrier's network on
  a lane, transshipment structure, or freight-rate direction on a specific trade.
---

# Tradelane Intel

Turn a question about an ocean container tradelane into a grounded, cited answer built from
**live public data the carriers and rate-reporters themselves publish** — not from memory.

The value of this skill is a method: *where* the answer lives, *how* to assemble it, and the
*analytical frame* that turns raw schedules into an insight. You (the model) do the fetching with
your normal web tools; this skill tells you where to look, how to reason, and how to cite.

## Non-negotiables (read first)

1. **Never fabricate a rotation, a rate, or a carrier claim.** If you cannot find it in a source,
   say so. A wrong port sequence or invented rate is worse than "not found".
2. **Cite every factual claim** with the source URL. Separate *carrier-published* facts (schedules,
   service names) from *market commentary* (rates, analysis) and label which is which.
3. **"New" requires current evidence, not a launch date.** A port that opened two years ago is not
   a "new" insight today. Only call something a development if there is *this-quarter* traction — a
   fresh service, a closed deal, a current rate move. Otherwise present it as *confirming an
   expected trend*, explicitly.
4. **Distinguish confirmed from inferred.** State what the data shows vs. what you're concluding
   from it, and flag uncertainty. A senior analyst is willing to conclude the boring truth.
5. **Read geography precisely.** "Asia" is meaningless — say East Asia (China/Korea/Japan/Taiwan),
   SE Asia (Vietnam/Thailand/Singapore/Malaysia), or South Asia (India/Sri Lanka/Bangladesh).
6. **Respect time.** Date every figure, set an "as of" date for the answer, and never combine numbers
   from different periods into one comparison as if they were one snapshot. A stale event (a service
   launched a year ago, a 2022 structural share) is *context*, not current news, and is not comparable
   to a this-quarter figure without saying so. See `references/method.md` §7.
7. **Every finding must matter to the reader** — it must change a cost, a risk, or a decision *they*
   actually face. Before a finding earns a place, name whose problem it is (exporter / importer /
   forwarder / carrier) and confirm it moves a metric *that reader actually pays or feels* — an exporter
   feels the **outbound** leg and their equipment/space, not the inbound headhaul. If the reader's own
   metric hasn't moved, or knowing it wouldn't change what they do, it is **not a finding — cut it.**
   Don't pad to a target count; and if verification kills a finding's premise, **cut it, don't reframe
   it** to survive. See the materiality gate in `references/insight-playbook.md`.
8. **Verify hardest what's easiest to get wrong.** A **negative or universal** claim ("no direct
   service", "only via X", "the last Y") dies to one counterexample — check it against current primary
   sources and **name the exact scope** (cargo class, destination, service). Never lean on a source
   flagged **stale/low-confidence/single** — re-verify or cut. **Name specifics, not vague claims**
   ("direct calls" → to where, on what service?). Distinguish **service/cargo classes** (container-liner
   ≠ specialised reefer ≠ charter ≠ bulk). See `references/method.md` §8.
9. **People, quotes, and services move in time.** Quotes are **verbatim or nothing** — never splice
   fragments into one quotation; quote each fragment separately. Verify a quoted executive is **current
   in role as of your as-of date** (CEOs change; a stale attribution is a factual error a tagged company
   will catch) — else date it: "then-CEO X said in May 2024". Match quote recency to the piece's window.
   A carrier "leaving" a trade is usually a **restructuring, not an exit** — name the service, what
   changed, and the fallback routing ("removed one region's calls from a loop; that region now served
   via transshipment at a hub"). Retiring your own tonnage and taking slots on a rival's *existing* ships
   removes net capacity — it isn't new capacity. Before "only N carriers/loops", **enumerate the full
   current service map** for that lane and cargo class. And **confirm the year of every source** — search
   surfaces prior-year changes as current. See `references/method.md` §9.

## Workflow

Center everything on the **user's own angle**. `references/insight-playbook.md` maps the full range
of asks — factual lookups through deep analysis — to the method and shows what a good answer looks
like; consult it first.

**Step 1 — Scope from the user, and match depth to the question.** Identify the tradelane (origin
region ↔ destination region), the carriers or specific service if named, and what they actually
want. Not every question is an insight hunt — size the answer to the ask:
- A **factual lookup** ("what ports does service Z call?", "who runs lane X↔Y?", "how long is
  A→B?") wants a clean, sourced answer — fetch it, answer, cite. Don't bolt a concentration
  analysis onto a question that just wants a fact.
- An **analytical / "why" question** wants the sharpest true answer — run the relevant frames and
  prove the finding.
- A **hunch** ("I think X is driving rates here") is a *hypothesis to test* — look hardest for what
  would **refute** it and report the honest verdict; refuting a wrong hunch with data is the best
  answer you can give.
- A **bare lane** ("what's interesting about Asia–Med?") → surface the one non-obvious finding
  (playbook → "Proactive mode"), don't dump facts.

Restate the question precisely before fetching.

**Step 2 — Fetch the carrier-published network.** Get the services / rotations from public sources.
`references/carrier-sources.md` is the per-carrier source map; **`references/fetching.md` is how to
actually get it with your standard tools** — the fetch ladder, and the two obstacles that trip people
up: (a) many carrier finders are JS/bot-walled, so a plain fetch returns a shell or 403 — *don't try
to defeat it*, pivot to the alliance PDF or a trade-press launch post, which carry the same rotation
and are citable; (b) rotations are often published as **maps or column-rail brochures/product images**
where text extraction scrambles the order — **read those visually** (the rail/table order is the call
order). If a rotation truly isn't publicly reachable, say so with the best-available + date — never
invent port calls.

**Step 3 — Add the market layer (if the question touches rates/capacity/demand).** Pull freight-rate
direction and demand/volume context from the indices and reports in `references/rates-and-demand.md`.

**Step 4 — Analyze.** Apply the relevant frame from `references/method.md`:
port-rotation reading · transshipment-vs-gateway test · **carrier concentration (HHI / top-3 share)**
· **rate-vs-demand divergence** (the supply-discipline test) · service-churn as a capacity signal ·
alliance/consortium structure · **temporal integrity & comparability** (date every figure, don't mix
periods — §7) · **capacity-access stratification** (shipper side: who owns tonnage / commits volume /
buys per sailing — §10). For a quick concentration read, run `scripts/concentration.py`.

**Step 5 — Answer.** Lead with the finding, support it with the data, give a specific
recommendation if the user is a shipper/planner, note the honest caveat, and list sources. Keep it
tight — one well-proven point beats five shallow ones.

## Output — structured REPORT with strict footnote referencing (MANDATORY)

Every substantive answer MUST use the exact section structure below, with markdown headers. **Do not
answer in free-flowing paragraphs.** Length follows the finding: write as much as it takes to prove the
one finding *completely* — don't pad with unrelated facts, but don't stop while the finding is
half-evidenced (see "Complete the finding").

- **Title** — `TRADELANE BRIEF — <lane or topic> · <month year>`
- **Bottom line** — 1–2 sentences: the single finding and why it matters. *(For a quick factual
  lookup, this plus References is the whole answer — don't pad.)*
- **What's happening** — bullets; put an inline marker `[1]`, `[2]`… on **every** factual claim, and
  label whether it's *carrier-published fact* or *market commentary*.
- **What it means** — 2–4 sentences; separate **Confirmed** from **Inferred** explicitly.
- **Actions** — bullets, specific, addressed to the reader's role (exporter / importer / forwarder /
  carrier). Include only when the question is decision-relevant.
- **Confidence & caveats** — one line: how solid, and what's a proxy or unmeasured (restate "verify
  with the carrier" when the answer is decision-relevant).
- **References** — the numbered list, at the very end (see below).

### Referencing — map every fact to its exact source (this is where answers fail)

Use a strict **footnote** system, not grouped/bundled sources:
- **One marker = one source.** Put a `[n]` right after each factual claim. Two facts from two sources
  get two different markers.
- **Number by first appearance.** `[1]` is the first source cited, `[2]` the second, and so on — so a
  reader can trace each marker to exactly one entry.
- **NEVER club sources.** Forbidden: grouping several outlets on one line, "`Source A + 3`", "via X",
  bare outlet names, category buckets like "Market commentary: A, B, C, D", or the assistant's own
  auto-citation chips. Each source stands alone with its own number.
- **All detail lives in References, inline is just the number.** Each **References** entry =
  `[n] outlet — title — full URL — date (if known) — (carrier-published fact | market commentary)`.
  List them in numeric order, one per line, at the very end.
- **1:1 both ways.** Every `[n]` in the body resolves to exactly one References entry, and every entry
  is cited by exactly one `[n]`.
- **Only what you opened.** Never list a source you didn't actually open; a paywalled/blocked page is
  not evidence and can never be the lead finding. A claim with no citable source is cut or labelled
  inference (it belongs in *What it means*, not *What's happening*).

### Complete the finding (don't half-answer)

Pick ONE finding — but evidence it *fully*. Half-mapped data reads as guesswork:
- "Who runs lane X?" → list **every** operator/service you found, not a couple.
- A rotation → the **full ordered port list**, not the endpoints.
- Concentration → **every** operator's share **and** the computed HHI + top-3, not a hand-wave.
- A rate/demand claim → the **actual direction/number with its date**, both the rate line and the
  demand line.
Depth on one finding, completely proven and fully cited, beats breadth across many half-proven ones.

### Before you publish — the pre-publish checks

**Materiality (does each finding earn its place?)** — see `references/insight-playbook.md`:
- For each finding, name the **reader** and confirm it moves a metric **they** pay or feel (right side of
  the deal: exporter → outbound; importer → inbound). If it's the wrong side or the reader's own metric is
  flat, **cut the finding.**
- Did you **pad to a round number**? Drop any passenger — count follows the bar.
- Did verification **kill a premise**? Cut that finding; don't reframe it into a weaker point to survive.

**Accuracy (§8):** for each claim — is it a **negative/universal** ("no…", "only…", "the last…")? If so,
did you look for the counterexample and name the exact scope (cargo class, destination, service)? Is any
claim resting on a **stale/flagged/single** source? Are the specifics **named**, not vague?

**Temporal (§7):**
- Does the brief state an **as-of date**, and does every figure carry its **own** reference period?
- Is anything called **"new"** that actually started before your window? Re-label it "in place since [date]".
- Does any chart, ratio, or side-by-side comparison **mix periods** as if they were one snapshot? Either
  make it a dated series with labelled periods, or split it.
- Are you comparing **like-for-like** (same period, unit, basis)? Flag any structural/older figure sitting
  next to a current one.

**People & services (§9):**
- Every quote **verbatim** (no spliced fragments), speaker **verified current in role** as of the as-of
  date — or the attribution is dated ("then-CEO…, May 2024").
- Every "carrier exited / only N options" claim names the **specific service change** and survives a
  **full enumeration** of the lane's current direct services (right cargo class, right lane scope).
- Every superlative is **attributed** to its source ("the port describes it as the region's largest…")
  unless independently enumerated.
- **Hostile-reader pass** for public pieces naming companies: assume each named company's comms team
  reads it — attack universals, superlatives, causal joints, period joins, and internal consistency
  (e.g. don't blame a cargo type for a container-terminal problem while praising that shipper's
  *non-container* operation).

## What this skill deliberately does NOT do

- It ships **no proprietary dataset**. Every answer is rebuilt from live public sources at query
  time, so it's always current and independently checkable.
- It does not tell you to defeat bot-protection or use private endpoints. Stick to publicly
  reachable pages, published PDFs, rate indices and trade press. If a carrier's own finder is
  unreachable, fall back to alliance product docs + trade-press launch posts, which are citable and
  usually sufficient to reconstruct a rotation.
