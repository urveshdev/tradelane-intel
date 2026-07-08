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

## Editorial standard (apply to every answer)

- **Evidence before narrative.** Let the data kill a tempting story; report the boring truth if
  that's what it says.
- **"New" needs current traction**, not a launch date. Else say "confirming the expected trend".
- **One proven point > five shallow ones.** Depth and proof over breadth.
- **Name the caveat.** Coverage gaps, proxy metrics (service-count vs TEU), single-source figures —
  state them; don't hide them.
- **Cite everything**, and separate carrier-published fact from market commentary.
