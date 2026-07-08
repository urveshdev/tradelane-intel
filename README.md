# Tradelane Intel — ocean container-shipping analyst

An **ocean container-shipping** analyst you can hand any question about a **tradelane, port, service,
or carrier network** — and get a grounded, cited answer built from **live public data** (alliance
network PDFs, carrier newsrooms, freight-rate indices, port-authority stats, reputable trade press).

> **Scope:** container liner shipping only — the ocean carriers, alliances, services, ports, and
> freight rates that move the world's boxes. Not air freight, trucking/rail, or bulk/tanker shipping.

> ⚠️ **Disclaimer — verify before you act.** This is an analytical aid, not an authoritative schedule
> or booking source. Answers are reconstructed from public data that can be dated, incomplete, or
> superseded, and AI can misread a rotation. **Always confirm exact service details, port rotations,
> transit times, cut-offs, and rates directly with the carrier** (or your forwarder) before making any
> commercial, routing, or booking decision, and do your own research. Freight-rate figures are
> third-party market commentary, not quotes. No warranty; use at your own risk.

It ships **no dataset**. Every answer is rebuilt at question time from public sources, so it's always
current and independently checkable. What it gives you is the *method*: where the answer lives, how to
fetch it (and recover when a carrier site blocks you), the analytical frame that turns a schedule into
an insight, and the discipline to cite everything and never fabricate.

---

## How to use it

### ▸ Claude — install the plugin (Claude app UI **or** Claude Code)

This repo is a **plugin marketplace**, so it installs as a plugin in both the Claude app and Claude
Code. The marketplace is the public GitHub repo: **`urveshdev/tradelane-intel`**. (Steps below are the
current official flows — see the cited Anthropic help articles.)

**Claude app — no terminal** (Pro, Max, Team, or Enterprise plan):
1. Open **Customize → Plugins** tab.
2. In **Personal plugins**, click **"+"** → **Add marketplace** → **Add from a repository**.
3. Point it at the GitHub repo **`urveshdev/tradelane-intel`** (or the repo URL) to sync the marketplace.
4. Open the synced marketplace and **install the `tradelane-intel` plugin**.

Steps per Anthropic's [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

**Claude Code — terminal:**
```text
/plugin marketplace add urveshdev/tradelane-intel
/plugin install tradelane-intel@tradelane-intel
/reload-plugins
```
`/reload-plugins` activates it without a restart. Update later with `/plugin marketplace update tradelane-intel`.
Steps per Anthropic's [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins).

Either way, ask a tradelane / port / carrier question and it kicks in.

### ▸ ChatGPT, Gemini, Copilot, or a quick Claude chat — copy one file (no install)

Fastest, works anywhere with browsing:
1. Open the prompt → **[view it](dist/tradelane-intel.txt)** /
   **[raw text](https://raw.githubusercontent.com/urveshdev/tradelane-intel/main/dist/tradelane-intel.txt)**.
2. Select all → copy → paste as your **first message** in a new chat, turn on **web browsing**, ask.

Reuse it without re-pasting by dropping that text into a **Project's custom instructions** (Claude.ai
or ChatGPT). For a shareable ChatGPT **Custom GPT**, follow [`dist/custom-gpt-setup.md`](dist/custom-gpt-setup.md).

**Requirements (any path):** the assistant's web browsing/search turned on. No API keys, no dataset,
no build step. (Python is only needed for the optional HHI helper script.)

---

## What's in the package

```
tradelane-intel/
  README.md                                    this file
  LICENSE                                      MIT
  .claude-plugin/marketplace.json              makes this repo a Claude Code plugin marketplace
  plugins/tradelane-intel/
    .claude-plugin/plugin.json                 the plugin manifest
    skills/tradelane-intel/                    the skill Claude loads
      SKILL.md                                   entry point — workflow + non-negotiables
      references/                                the knowledge (also uploadable to a ChatGPT Custom GPT)
        insight-playbook.md                        question patterns → frame → good-answer shape
        method.md                                  the 6 analytical frames + the editorial standard
        carrier-sources.md                         where carriers/alliances/ports publish — with URLs
        rates-and-demand.md                        rate indices + demand sources — with URLs
        fetching.md                                how to fetch; bot-wall & map-PDF recovery
      scripts/concentration.py                     HHI + top-3 from counts you gather (no data inside)
  dist/                                        for ChatGPT / Gemini / any assistant with browsing
    tradelane-intel.txt                          ← the single copy-paste prompt (self-contained)
    portable-prompt.md                           same prompt in markdown, with usage notes
    custom-gpt-setup.md                          step-by-step to build a ChatGPT Custom GPT
```

The two paths use the **same** content — the Claude skill reads the `references/` files; the `.txt`
inlines those same references into one self-contained, paste-able prompt.

---

## What it can answer (examples, not limits)

- "Who runs **Asia–West Africa**, and what's the rotation?"
- "Is **[port]** a transshipment hub or a gateway — and how would I know?"
- "**Why are rates on my lane moving** — and is it demand or capacity discipline?"
- "How **concentrated** is the transpacific vs Asia–Europe, and who has pricing power?"
- "What ports does **[carrier]'s [service]** call, and how long is the transit?"

## The principles it enforces

- **Cite every fact**; separate carrier-published from third-party market commentary.
- **Never fabricate** a rotation or a rate — say "not found" instead.
- **"New" needs this-quarter traction**, not a launch date; otherwise it's "confirming a trend".
- **Test hunches, don't just confirm them** — refuting a wrong hunch with data is the best answer.
- **Match depth to the question**; one proven point beats five shallow ones.

---
No scraped data is distributed. All sources are public and cited per answer.
