---
name: flow-hand-driven-not-automated
description: Kai drives Google Flow by hand (2026-08-16); but Jack (2026-10-21) wants Claude to run Flow itself and pick the best take.
metadata:
  type: feedback
---

Do **not** drive Google Flow through the browser/MCP automation by default when **Kai** is driving. Kai ruled on 2026-08-16 that it is too buggy and too slow to be worth it. Deliver **researched, copy-paste-ready prompts** instead and let Kai fire them in Flow.

**Why:** the Aug-2026 Flow redesign kept breaking the `@badcode/flow-mcp` client (character attach silently no-opping, stale selectors, page crashes), so each image cost several failed rounds. The prompt research is the part that has consistently produced accepted takes.

**How to apply:** for every plate, output one fenced block — the story's own preamble from its `look.md` if it has one (none is a default), then the scene, then `Thanks.` — with a short header above it stating cast (`@X` or none), time of day, and whether ingredients/frames or a reference image are attached. One plate at a time so Kai can edit before firing. Source the craft from [[flow-engine-research-goes-in-docs-google-flow]] (`docs/google-flow/`) and `docs/flow/`. Only touch the Flow automation if Kai asks for it explicitly.

**Jack, 2026-10-21 (Bank Robbery):** "just do the stuff in flow and we'll change it if it does not fit, just pick the best one." When **Jack** is driving, run the stills and clips through the Flow tooling yourself, choose the best candidate, put it on the timeline, and report what was picked and why. Handing him a paste block instead cost a round. Kai's 2026-08-16 rule above still stands for Kai.
