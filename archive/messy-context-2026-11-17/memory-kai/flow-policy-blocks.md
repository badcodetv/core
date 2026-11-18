---
name: flow-policy-blocks
description: "Flow's usage filter silently blocks over half of BadCode image prompts and it looks exactly like a timeout — rewrite, never retry"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: efc1d01c-1efb-416c-ab81-d97091da67d0
  modified: 2026-07-25T19:19:33.723Z
---

Kai, 2026-07-25: **over half of Flow generations were being blocked for usage-policy violations, not timing out.** The block is visible in the Flow browser window but the MCP tools surface it as a generic timeout / missing candidate, so an agent cannot tell a blocked prompt from a slow one and wastes minutes retrying prompts that can never pass.

**Why:** this was the single biggest time sink of the camping recut. Kai raised it twice, explicitly asking that it be absorbed into the skills "so that we don't keep doing this mistake".

**How to apply:**
- **Diagnosis rule:** two no-candidate failures on a healthy session (`flow_status` fine, project loads, sibling prompts succeed) = policy block. Rewrite; do not retry.
- **The four triggers:** (1) real brand names, especially "legible" logos/wordmarks; (2) likeness phrasing — "same face, same bone structure"; (3) stacked destitution vocabulary (burn barrels + tent city + "gaunt") next to a real business; (4) legible text attributed to real institutions.
- **Rewrite:** invent near-miss brands (keep class signal, drop trademark), reframe faces as *character-design consistency*, stop asking for legible real text, soften degradation words. Load-bearing text belongs in a `NarrationBox`/bubble overlay, not baked pixels.

Written into: `.claude/skills/badcode-art-direction/SKILL.md` ("Usage-policy blocks" — the canonical section with a rewrite table), `packages/flow-mcp/README.md`, `.claude/agents/flow-operator.md` (stop-the-ladder rule), `.claude/skills/edit-panel/SKILL.md`, `.claude/skills/make-comic/SKILL.md`.

**Two open follow-ons:** (1) `@badcode/flow-mcp` should detect a block and return a distinct `POLICY_BLOCKED` code so callers rewrite instead of retry — not yet built; (2) accepted camping panels contain visible real supermarket signage — a brand-usage decision for publication, separate from generation. See [[camping-recut-initiative]].
