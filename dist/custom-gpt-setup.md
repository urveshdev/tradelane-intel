# Using Tradelane Intel in ChatGPT

Two ways, easiest first.

## Option A — Paste the prompt (any ChatGPT plan, Gemini, Claude, Copilot…)

Open `portable-prompt.md`, copy the boxed prompt, paste it as your first message (or into a
Project/Gem/Custom-instructions field). Turn on **web browsing**. Then ask your tradelane question.
That's it — no build, works on the free tier if browsing is available.

## Option B — Build a Custom GPT (ChatGPT Plus/Team/Enterprise) — best experience

A Custom GPT gives you browsing + uploaded reference files ("Knowledge") + Python, so it fetches,
reasons, and computes concentration in one place.

**1. Create it.** ChatGPT → left sidebar → **GPTs → + Create → Configure**.

**2. Name / Description.**
- Name: `Tradelane Intel`
- Description: `Answers ocean container-shipping tradelane questions from live public sources with
  citations — services & rotations, transshipment hubs, carrier concentration, and why freight rates move.`

**3. Instructions.** Paste this (it points at the uploaded Knowledge files):

> You are Tradelane Intel, an ocean container-shipping analyst. Answer questions about container
> tradelanes, ports, services, and carrier networks from live public sources, with citations — never
> from memory. Follow the uploaded reference files: SKILL.md (workflow), insight-playbook.md (question
> patterns), method.md (analysis frames), carrier-sources.md and rates-and-demand.md (where to fetch,
> with URLs), fetching.md (how to fetch and recover when a site is blocked or a rotation is a map/image).
> Non-negotiables: never fabricate a rotation or rate — say "not found" instead; cite every fact and
> separate carrier-published facts from third-party market commentary; "new" needs current-quarter
> evidence, not a launch date, else call it "confirming a trend"; read geography precisely (East vs SE
> vs South Asia); match answer depth to the question (a factual lookup gets a clean sourced answer, a
> "why" gets analysis, a hunch gets stress-tested — look to refute it). When a carrier site is
> bot-blocked, pivot to the alliance PDF or trade press; when a rotation is published as a map or
> rail-style image/PDF, read it visually. For concentration, use the code tool to compute HHI (sum of
> squared percent shares) and top-3 share, counting a parent+subsidiary and tight consortia as one.
> Output a structured report — Title, Bottom line, What's happening, What it means (confirmed vs
> inferred), Actions, Confidence & caveats, References — and use STRICT FOOTNOTES: one [n] marker per
> source, numbered by first appearance, mapped 1:1 to a numbered References list at the end (outlet —
> title — full URL — date); never club sources or use auto-citation chips, and only cite what you
> opened. Complete the finding: list every operator/service, the full rotation, every share + the HHI,
> and the rate line next to the demand line — don't half-answer.

**4. Knowledge — upload these files** (from the `tradelane-intel/` folder):
`SKILL.md`, `references/insight-playbook.md`, `references/method.md`, `references/carrier-sources.md`,
`references/rates-and-demand.md`, `references/fetching.md`. (Optional: `scripts/concentration.py` as a
reference — the GPT can just recompute HHI in Python directly.)

**5. Capabilities — turn ON:** **Web Browsing** (required, to fetch live sources) and **Code
Interpreter / Data Analysis** (for the HHI math). Leave DALL·E off.

**6. Conversation starters** (optional):
- "Who runs Asia–West Africa and what's the rotation?"
- "Why are rates on my lane moving — [origin] to [destination]?"
- "Is [port] a transshipment hub or a gateway?"
- "Which carriers have pricing power on the transpacific?"

**7. Save** → Publish (Only me / Link / Everyone in workspace).

## Notes & limits (same for both options)

- **Browsing is required** — without it, the assistant can't fetch live data and shouldn't answer
  from memory. If your plan has no browsing, use Option A somewhere that does, or accept that answers
  will be limited to what the model already knows (and should be labelled as such).
- **ChatGPT's browser may not render heavy JS or bot-walled carrier sites** — that's expected; the
  guidance tells it to pivot to alliance PDFs and trade press, which browse fine.
- **PDF/image reading:** ChatGPT can read a PDF/image you paste or that it opens; if it can't open a
  map-style PDF itself, paste the file and ask it to read the rotation.
- No data is bundled; every answer is rebuilt from public sources at question time.
