# Analysis method — turning schedules into insight

Pick the frame that fits the question. Each is a repeatable test with a clear "so what".

## 1. Read the rotation properly

A service is an ordered loop of port calls. From the published rotation, extract:
- **Endpoints & corridor** — first/last load and discharge regions (be precise: East Asia vs SE Asia
  vs South Asia). The corridor is the service's real trade, regardless of how the carrier labels it —
  carrier/press trade-lane *labels* are often wrong; read the *ports*.
- **Hub calls** — a port that sits mid-loop between distant regions with little local trade rationale
  is a relay/transshipment call, not a gateway. Its *position* in the loop tells you its function.
- **Direct vs transshipped** — does the destination get a direct call from the origin, or only via a
  hub? Direct = better transit + fewer handoffs.

## 2. Transshipment vs gateway test

To decide if a port is a transshipment hub (relays boxes between ships) or a gateway (local
import/export), don't rely on who calls it — test it:
- **Volume vs hinterland** — throughput far larger than the local economy could generate ⇒ relay.
- **Cannibalisation** — if it's taking transshipment volume *from another transshipment terminal*,
  it's doing relay (a gateway can't).
- **Single-carrier is fine** — a hub served by one carrier is still transshipment if that carrier
  relays between *its own* strings (the MSC / Gioia Tauro / King Abdullah pattern). Many services of
  one carrier meeting at one port = an intra-carrier relay grid.

## 3. Carrier concentration → pricing power (HHI)

*Who can hold rates on a trade is a function of how concentrated it is.* Assemble the count of
services (or better, deployed TEU) per operator on the lane, then compute concentration with
`scripts/concentration.py`:
- **Top-3 operator share** and **HHI** (sum of squared percentage shares).
- Rough reading: HHI < 1500 = fragmented (no pricing power); 1500–2500 = moderately concentrated
  (discipline feasible); > 2500 = concentrated.
- Count a parent + subsidiary (e.g. COSCO + OOCL) and tight consortia as **one** decision-maker.
- **The insight:** in an oversupplied market, rates hold on *concentrated, thin* trades (few carriers
  can coordinate blanks) and collapse on *fragmented, large* trades (nobody can). Concentration
  predicts where a shipper overpays vs. where the glut helps them.

## 4. Rate-vs-demand divergence (the supply-discipline test)

The sharpest, least-obvious frame. Put the **rate direction** next to the **demand direction** for
the same lane and period:
- rate ↑ **and** demand ↑ → demand rally (often seasonal — not a structural story).
- rate ↑ **and** demand flat/↓ → **supply discipline** (carriers withholding space) — the real story.
- rate ↓ → oversupply winning, or demand collapse (check which; e.g. tariff-driven volume loss).

Corroborate discipline with blank-sailing counts and the concentration read (§3). This is how you
avoid mistaking a disciplined price for a demand boom.

## 5. Service churn as a capacity signal

A trade with constant launches/revivals/withdrawals is one carriers are *actively managing* — only
feasible where the trade is small enough to steer. Pull the dated service-change record (trade press)
and look at the *net* and the *cadence*:
- Continuous add/cut churn + rising rates = active capacity management holding a disciplined price.
- A maverick adding real capacity into a disciplined trade is what *breaks* it — the service-launch
  cadence is a leading indicator of whether rates hold or crack. Track new strings, not just the index.

## 6. Alliance / consortium structure

Who *shares* a service matters more than who's named on it. Map the operating consortium (VSA
partners) before judging competition or concentration — shared strings mean fewer independent
capacity decisions than the carrier count suggests.

## 7. Temporal integrity & statistical comparability (check the dates before you combine numbers)

Numbers mean nothing without their reference period, and can only be compared when they share a basis.
Getting this wrong produces confident nonsense — the most common failure in a multi-source brief.
- **Date every figure.** Carry the reference period on each number ("sector outlook Jun 2026", "SCFI
  early Jun 2026", "FY2025", "2022 structural share"). A number without a date can't be used or checked.
- **Set an "as of" date for the whole answer and test every fact against it.** A development is only
  *current* if it falls in your reporting window (roughly this quarter). An event 6–24 months old is
  **structure/context, not news** — write "in place since [date]", never "new". *A service launched in
  Sept 2024 is the established network in a July 2026 brief, not a new service.* Only call something new
  if it started inside your window.
- **Don't combine different-period figures into one comparison, ratio, or chart** unless you are
  explicitly showing a *trend* — and then label the period on every point. Never let numbers of
  different vintage read as a single synchronized snapshot. If the only data points are from different
  dates, present them as a **dated series**, not one current number.
- **Compare like-for-like:** same period, same unit, same basis (volume-vs-volume, value-vs-value),
  same geography, same source methodology. If you must cross bases (e.g. a 2022 structural share beside
  a 2026 spot rate), say so explicitly and don't imply they move together. Within-item comparisons from
  one release (a commodity's value-vs-volume from the *same* report) are valid even when items differ.
- **Recency-weight the claim:** if a supporting fact is older than your window, either re-verify it
  still holds, or down-rank it to dated context. A stale fact can support a *trend*; it can never
  support a *"right now"* assertion.
- **Prefer one consistent release** over stitching the latest number for each item from different
  reports. If you must stitch, tag each item's source and date so the reader sees the seams.
- **Sanity-check a composite against its parts.** If a source says "54% concentrated in A+B+C+D", add
  the components (35.6+13.8+6.7+6.7 = 62.8 ≠ 54) — a mismatch means the headline or the grouping is
  wrong; don't use it. Prefer a stat whose parts reconcile (e.g. "50.3% to 3 markets: 25.1+12.7+12.5").
- **One number = one measure.** Don't blend two different series into a single figure. A route *index*
  and a corridor *mean spot* are different metrics even on the same lane — cite each with its own label;
  never merge them as if they were the same number.
- **Actual ≠ forecast.** Never pair a forecast with an actual, or two different actual periods. A
  revenue figure (forecast, one year) is not the counterpart to a volume figure (actual, a different
  year) — quote both halves of a value-vs-volume comparison from the *same* release, same type, same
  period, or keep them separate and labelled. Mixing them fabricates a relationship.
- **Future figures get revised — re-check before citing.** A scheduled/announced number (a fee hike, a
  launch date, a forecast) can be pared back, delayed, or superseded. Before presenting a future value
  as current fact, look for a later revision; if it changed and the new value isn't public, mark it
  *uncertain* rather than quoting the stale plan as if it still holds.
- **Prefer the official figure over a paraphrase.** When the primary source states an exact number (a
  port's or carrier's own release) and the press rounds it (a paraphrased quote), lead with the primary
  figure and note the paraphrase — don't let the rounded version become the headline.

## 8. Verification discipline — what to check hardest (before a claim earns its place)

Most wrong findings are not fabricated numbers; they are true-ish claims stated too broadly, or built on a
weak source. Guard against these specifically:
- **Negatives and universals need the strongest evidence.** "No direct service", "only via X", "the last
  remaining Y", "nobody does Z" — a *single counterexample* kills these. Before asserting absence or
  universality, check current primary sources hard, and state the exact scope (which cargo class, which
  destination, which service). *A "no direct service to region X" claim dies to one counterexample — a
  specialised reefer vessel may sail a lane direct even where no container-liner does; the true, narrow
  claim is usually "no direct container-liner call", scoped to a cargo class.*
- **Never lean on a source you (or a checker) flagged stale, low-confidence, or single.** If a finding's
  load-bearing evidence is dated, uncertain, or uncorroborated, re-verify against a current primary source
  before it earns a place — or cut it. A checker flagging "stale (2004)" is a stop sign, not a footnote.
- **Confirm the year of every source.** Search engines routinely surface old articles and mislabel them
  as current — a service change or rate from a prior year can read as this week's news. Pin the
  publication date from the primary before treating anything as current, and watch for near-identical
  restructurings that recur on the same lane across years (a relaunch one August can mirror another):
  match on vessel/voyage and year, not on the pattern.
- **Name specifics, never vague claims.** "Direct calls" → *to where, on what service?* "Rates rising" →
  *whose leg, which index, what period?* Vague claims hide errors; specificity forces accuracy and lets the
  reader act. If you can't name the specifics, you haven't verified it.
- **Distinguish service and cargo classes.** Container-liner ≠ specialised reefer vessel ≠ charter ≠ bulk.
  A fact true for one class is not true for all — say which class you mean. (Container reefer to Europe may
  transship while dedicated reefer ships sail direct.)
- **Refute before you assert.** For any load-bearing claim, spend a moment actively looking for the
  counterexample or the more recent number. If you find one, the claim changes or dies.

## 9. People, quotes & service-change precision

The errors named companies catch first. Apply whenever a brief quotes a person, cites an executive,
or describes a carrier's network change.

- **Quotes: verbatim or nothing.** Exact words, exact order, from a page/document you opened. Never
  splice non-adjacent fragments into one quotation — attribute each fragment on its own (e.g. quote
  "strong yields" and, separately, "our network" — two quotes, not one spliced quotation). If only a
  paraphrase exists, present it as paraphrase ("told a news outlet that…"), never inside quote marks.
- **Verify the speaker is current in role — as of the brief's as-of date.** Executives change; a
  perfectly verbatim quote with a stale title is a factual error the company will catch (*failure to
  avoid: quoting a CEO 18 months after he left the role*). If the quote is worth keeping despite its
  age, date the attribution: "then-CEO X said in May 2024…".
- **Match quote recency to the piece's window.** A "this season" brief needs this season's primary
  publications (carrier newsroom, shipper's own grower/customer bulletins); an older quote needs its
  date shown even when the speaker is unchanged.
- **Service withdrawals are usually restructurings.** "Carrier X left trade Y" → name the **service**,
  the **specific change**, and the **fallback routing** ("removed one region's calls from a loop,
  leaving it single-region; that region now served via transshipment at an intermediate hub"). The
  precise version is more informative *and* more defensible than the flat exit claim.
- **"Only N options" requires the full map.** Before asserting how many carriers/loops serve a lane
  directly, enumerate the current service map from carrier schedules (count a parent+subsidiary as one,
  and catch easily-missed operators — a standalone line, or a slot-charterer riding another's ships),
  and scope by lane and cargo class. If you can't enumerate, attribute: "which [carrier] markets as the
  only direct…".
- **Port metrics: quote the exact measure.** "55% of *container vessels* on schedule" ≠ "55% of
  vessels" — summarisers drop qualifiers; read the primary document raw (download + `pdftotext`) for
  load-bearing numbers. Distinguish export vs import gateway shares (a country's biggest export port
  and biggest import port are often different ports), terminal vs whole-port capacity, and attribute
  self-published superlatives ("what the port itself describes as the region's largest reefer
  capacity").
- **Operated tonnage ≠ market capacity.** A carrier retiring its own service and taking slots on a
  rival's *existing* ships removes net capacity and becomes a customer — it adds none. Count who
  controls the vessel, not the brand on the booking; slots on ships already running are not "new
  capacity".
- **Read a capacity move by its horizon and reversibility.** A large operator reactivating an existing
  loop for a demand spike is cycle-trading (cheap, reversible, likely short-lived); a carrier giving up
  its own tonnage for slots is structural (deliberate, lasting). Opposite moves on one lane at once are
  usually different horizons, not a contradiction — say which is which.

## 10. Capacity-access stratification (the shipper-side frame)

For questions like "who's insulated when capacity tightens?", "why do equal-rate shippers get unequal
outcomes?", or any exporter/importer-resilience read on a thin trade. Rank the lane's cargo owners by
**how they secure capacity**, not by size or rate paid:

1. **Own/charter tonnage** — the cargo owner operates dedicated vessels (e.g. a major fruit marketer
   chartering a seasonal reefer fleet). Note the *physical class*: chartered conventional reefer ships
   load palletised cargo coolstore-to-hold and **bypass container terminals and reefer plugs entirely**
   — don't attribute container-terminal phenomena (plug shortages, yard congestion) to this flow, and
   don't count it in container statistics without saying so.
2. **Commit volume that shapes deployment** — a cargo-owner consortium or shipper pledges enough
   long-term volume that the carrier deploys/keeps dedicated capacity for the trade (documented
   pattern: a ~10-year committed-volume partnership preceding the carrier introducing larger dedicated
   vessels). Use the documented mechanism language — "committed volume gave the carrier certainty to
   deploy" — not stronger financial verbs ("underwrites", "guarantees") unless a contract term is
   public.
3. **Transactional / per-sailing** — booked direct or via forwarder against whatever space and
   equipment is open. Nuance that survives pushback: large forwarders/NVOCCs can hold **block-space
   agreements and committed allocations** — booking via a forwarder is not automatically spot-exposed;
   the test is whether *someone in the chain* holds protected allocation on that lane.

The analytical payoff: on thin, end-of-line trades where services actually get withdrawn, tiers 1–2
decide whether capacity *exists and prioritises you*; on thick trades the same moves mostly buy price.
State which regime the lane is in before drawing conclusions. This frame is emergent behaviour, not a
designed system — present it as sorting/stratification, and check **prior art** before claiming the
framing is novel (crisis-era press usually described a two-tier version).

## Editorial standard (apply to every answer)

- **Evidence before narrative.** Let the data kill a tempting story; report the boring truth if
  that's what it says.
- **"New" needs current traction**, not a launch date. Else say "confirming the expected trend".
- **One proven point > five shallow ones.** Depth and proof over breadth.
- **Every finding must matter to the reader; count follows the bar.** Confirm each finding changes a cost,
  risk, or decision the reader actually faces — a metric they pay or feel (right side of the deal) — and
  ship only those that pass; don't pad to a number. If verification refutes a finding's premise, cut it;
  don't reframe a dead insight to keep it.
- **Name the caveat.** Coverage gaps, proxy metrics (service-count vs TEU), single-source figures —
  state them; don't hide them.
- **Cite everything**, and separate carrier-published fact from market commentary.
