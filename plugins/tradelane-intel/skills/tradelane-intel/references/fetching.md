# Fetching & tools — how to actually get the data, and what to do when a source fights back

You need only the model's **standard tools**. No scraper ships with this skill — by design: a bundled
scraper would encode bot-evasion, go stale, and still hit the same walls. Instead, here is how to get
each thing with native tools, and — critically — how to recover from the exact obstacles that make
carrier data hard (bot-protected sites, JS pages, and rotations published as maps/images).

## The tools you use

- **WebSearch** — find the right source: a service-launch post, an alliance PDF, this week's rate
  index, a port's throughput release.
- **WebFetch / read-URL** — pull a page or PDF. In most environments you can also **read a PDF or an
  image visually** — use that to read a rotation off a map/brochure/product-image (see below).
- **Bash / code execution** — run `scripts/concentration.py` on operator counts you assembled.

## The fetch ladder (cheapest first — how a human analyst actually works)

1. **Trade-press / Linerlytica post for the specific service.** It usually prints the full rotation
   in plain text ("…will call Qingdao, Busan, … Vizhinjam, Rio de Janeiro…") and a date. Most
   citable and reliably WebFetch-able. **Start here** for a named service or a recent change.
2. **Alliance / carrier PDF** (Ocean Alliance Day-N, Gemini, Premier; carrier regional brochures).
   Open and fetchable. If the PDF is a **map or column-rail layout** and the extracted text is
   scrambled, **read the PDF visually** (next section).
3. **Per-service product images / e-brochures** (some carriers publish a rotation + transit-time
   table as an image). Fetch the image and **read it visually**.
4. **Port-authority stats & national trade data** for throughput, transshipment share, import volume.
5. **Rate-index publications** (Drewry WCI weekly, SCFI/CCFI, Freightos updates) for rate direction.

## Reading rotations from maps/images (the vision step — this is the one people miss)

Carrier brochures and product sheets frequently show the rotation as a **geographic map** or a
**styled vertical rail**, and plain text extraction returns the ports out of order or as scattered
labels. When you have the file, **read it as an image and transcribe the ordered port list from the
rail/table**, not from copy-pasted text. Notes:
- The rail/table order *is* the call order — read top-to-bottom / along the transit table.
- Capture **repeated calls** (a port can appear twice in one loop) and the **direction legs**
  (headhaul vs return) if shown.
- Transit-time tables (origin × destination + days) are a bonus — they confirm the sequence and give
  transit deltas for re-routing questions.

## When a carrier's own site fights back (expect this)

Many carrier route-finders are **JS-rendered and/or bot-protected** — a plain fetch returns a shell,
a challenge page, or an HTTP 403. **Do not attempt to defeat the protection.** Pivot:
- Reconstruct the same rotation from the **alliance PDF** or a **trade-press launch post** — they
  carry it, and they're citable.
- If only a stale version is public, use it and **state the date**.
- If the rotation genuinely can't be reached from public sources, **say so and give the
  best-available** (last confirmed rotation + source date). Never invent port calls.

## Honesty rule

A cited *"here's the latest I can confirm, as of <date>"* beats a confident wrong rotation. If
you're blocked, report what you have and what's missing — that's a valid, professional answer.
