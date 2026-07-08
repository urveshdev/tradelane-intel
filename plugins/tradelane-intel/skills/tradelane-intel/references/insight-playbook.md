# Playbook — from a user's question to a grounded answer

This skill answers **any** question about a container tradelane, port, service, or carrier network —
from a one-line factual lookup to a deep "why is this happening" analysis. The patterns below are the
common *shapes*; they are **illustrations of the method, not the limits of scope**. If a question
doesn't match a pattern, compose from the frames in `method.md` — the method generalises.

## First: match the depth to the question

- **Factual lookup** ("what ports does OOCL's TLA1 call?", "who runs Asia–West Africa?", "how long
  is Ningbo→Callao?") → fetch the rotation/figure, answer cleanly, cite. Don't force an "insight" or
  a concentration analysis onto a question that just wants a fact.
- **Analytical / "why" question** ("why are rates on my lane rising?", "is this hub a threat to me?")
  → run the relevant frames, prove the finding, give a so-what.
- **A hunch to test** ("I think X is driving my rates") → treat as a hypothesis; look hardest for
  what would **refute** it, and report the honest verdict. Refuting a wrong hunch with data is the
  most valuable answer you can give.
- **A bare lane** ("what's interesting about Asia–Med?") → run the frames and surface the *one*
  non-obvious finding (see "Proactive mode" below) — don't dump facts.

Always ask: *is this genuinely non-obvious, or does the trade already know it?* If the latter, say so
and dig for the second-order point. Let the data kill a tempting narrative.

## Pattern library (question → frame → what a good answer looks like)

*Frames referenced are in `method.md`. Worked examples are illustrative.*

**Network & routing**
- **What services/carriers run lane X↔Y?** → rotation reading (§1). List operators + named services,
  the corridor, and direct-vs-transship. *Cite the alliance PDF / trade-press posts.*
- **What's the rotation of service Z / port order & transit?** → §1 + transit tables. Give the ordered
  calls and the transit deltas; read from a map/image if that's how it's published (`fetching.md`).
- **Direct or must I transship?** → §1. Say whether the destination gets a direct call from origin or
  only via a hub, and name the hub + added days.
- **How is [carrier]'s network on this lane structured?** → §1 + §6. Map hubs and consortium partners;
  watch for a carrier running two parallel hub systems (e.g. an intercontinental-relay hub + a
  regional-feeder hub with no overlap).

**Ports & hubs**
- **Is port P a transshipment hub or a gateway?** → transshipment test (§2): volume-vs-hinterland,
  cannibalisation of another relay terminal, single-carrier self-relay. *e.g. a hub that halves a
  rival ICTT's relay volume is doing transshipment even if one carrier dominates it.*
- **Should I use port A or B for my hinterland?** → §1 + port throughput/congestion data. Compare
  direct-call frequency, carriers, transit, and congestion risk; name a concrete choice.
- **Is port P congested / at capacity?** → port-authority throughput vs design capacity + trade press.

**Rates, capacity & demand**
- **Why are rates on my lane moving?** → rate-vs-demand divergence (§4) + concentration (§3) + churn
  (§5). *e.g. rates up while the lane's import demand falls ⇒ supply discipline, not demand — and a
  concentrated, thin trade is where carriers can make that stick.*
- **Who has pricing power on my lane?** → concentration/HHI (§3) via `scripts/concentration.py`,
  counting parent+subsidiary and consortia as one operator.
- **Am I exposed to blank sailings / rollovers?** → §5 + blank-sailing trackers. High concentration +
  active churn = expect capacity to be managed tightly; watch the launch cadence as the leading signal.
- **When do rates peak on my lane (seasonality)?** → index history + demand seasonality; state the
  typical peak window and whether this year diverges.
- **Contract vs spot — lock now or wait?** → spot-vs-long-term spread (Xeneta/Drewry) + the capacity
  read; frame the risk, don't give financial advice.

**Change & structure**
- **Is X a real shift, or hype?** → new-vs-confirming test. Require *current* dated evidence (a closed
  deal, a launched service, a live rate/volume move). A port that opened two years ago is not "new" —
  present as confirmation unless there's this-quarter traction.
- **How did the alliance reshuffle change my lane?** → §6 + dated service record. Compare the before/
  after operating structure and what it did to direct calls, transit, and hub choice on that corridor.
- **Are bigger ships / more capacity coming to my lane?** → fleet/orderbook + carrier deployment
  notes; what upsizing does to port rotation (fewer calls, more transshipment) and rates.
- **Green corridors / emissions on my lane?** → carrier & alliance sustainability filings, port shore-
  power/fuel announcements; distinguish commitments from operational reality.

## Proactive mode — a bare lane / region ("what's happening on NZ export lanes?")

This is where answers most often go wrong. **Structure first, news last.** Do NOT open your browser,
grab the 2–4 most recent press headlines about the region, rank them by date, and call that an
analysis — that is a news digest, not a tradelane read, and it fails the bar below.

Instead, build the answer from the lane's *structure*, in this order:
1. **Map the lane.** For a country/region ask, enumerate its real international corridors (e.g. NZ →
   East Asia, NZ → North America, NZ → Europe [transshipped via SE-Asian hubs], NZ → Middle East) and
   say which one carries the real story. Name the actual **services + operators** on it (§1, §6).
2. **Concentration & pricing power (§3).** Who runs it, how concentrated (HHI / top-3, parent+subsidiary
   and consortia counted as one)? Thin, concentrated, end-of-line markets (NZ, West Africa, LatAm
   reefer lanes) are exactly where carriers hold rates — lead with this if it's the real feature.
3. **Cargo profile.** What moves and when — reefer/agri (NZ dairy-meat-kiwifruit, Chile fruit),
   project, e-commerce — and its seasonality. The cargo mix, not the news, sets the pricing dynamics
   (NZ's binding constraint is reefer plug capacity in the Sep–Jan season, not the spot index).
4. **Rate-vs-demand divergence (§4)** on the corridor that matters, with actual direction.
5. **THEN, only if genuinely current AND material to this lane,** the newest dated service change (§5)
   — as *support* for the structural read, never as the headline.

Surface the ONE non-obvious, data-backed finding that survives "does the trade already know this?"
Lead with it, proven.

## Anti-pattern — what a WEAK answer looks like (do not produce this)

- A ranked list of recent headlines ("here are 3 things in the news"), each with a one-line "read".
  Recency is not materiality. An insight comes from a FRAME applied to the lane's structure.
- **Leading with the wrong category:** a domestic/coastal/cabotage story, a per-box terminal surcharge
  notice, or generic east–west (Suez/Cape) news, when the user asked about an international export
  **lane**. Those are at most context — never the finding. Keep scope on international container
  tradelanes.
- A "finding" whose evidence is a **paywalled or unopened** article plus an inferred read. The lead
  finding must rest on a source you actually opened; if you couldn't open it, it can't be the headline.
- Burying the genuinely structural lever (e.g. NZ reefer-capacity seasonality, or the lane's
  concentration) in a closing caveat while headlining a minor dated item.

## The bar (every answer)

One-line **finding** · cited **evidence** (carrier-published vs market commentary, labelled) · the
**read** (confirmed vs inferred) · a **so-what** for the reader's role, if any · the honest
**caveat**. Depth over breadth — one proven point beats five shallow ones. If blocked or the data
refutes the premise, say so plainly.
