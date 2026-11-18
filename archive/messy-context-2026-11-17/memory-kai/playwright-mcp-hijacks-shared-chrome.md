---
name: playwright-mcp-hijacks-shared-chrome
description: "The Playwright MCP attaches over CDP to the SAME Chrome as Suno/Flow (port 9222); a subagent's browser_navigate replaced Kai's Suno tab 2026-09-30"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 22c13da8-afa2-462a-942b-f1036ffc3f5e
  modified: 2026-09-30T18:20:54.956Z
---

The `playwright` MCP in `.mcp.json` runs with `--cdp-endpoint http://localhost:${FLOW_CDP_PORT:-9222}`,
so it drives Kai's live Suno/Flow Chrome, not a private browser. On 2026-09-30 a research subagent
(fetching MMT document screenshots) called `browser_navigate` and it took over the Suno create tab —
any unsaved form was lost (Suno has no draft recovery).

**Why:** one Suno tab, ever (Kai); navigating away wipes the form.

**How to apply:** never give a subagent the Playwright MCP for general web screenshots. Use
`curl`/WebFetch for files, and a headless browser of its own (`npx playwright screenshot`, or
Playwright with a fresh `chromium.launch()`) for page captures. If the MCP must be used, open a
NEW tab first (`browser_tabs` new) and never navigate an existing one. See [[concurrent-browser-sessions]],
[[suno-check-form-mode]].
