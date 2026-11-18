---
name: flow-script-hardening-initiative
description: "Live-hardening the @badcode/flow-mcp script layer against Flow's real UI (camping-v2) + the plan→batch→iterate workflow"
metadata: 
  node_type: memory
  type: project
  originSessionId: 193dbb28-fab5-4e4f-843c-d58235ffe686
---

Hardening `@badcode/flow-mcp` from contract-written-but-untrusted into live-validated, fast
Flow automation. Spec/plan: `docs/superpowers/specs/2026-06-30-flow-script-hardening-design.md`
+ `docs/superpowers/plans/2026-06-30-flow-script-hardening.md`. Built on worktree branch
`worktree-flow-script-hardening` (5 commits), NOT yet merged to main. Method: observe-then-codify
— drive each Flow action live via the Playwright MCP, capture the real selectors, codify into
`flow-client.ts`, prove with a `tsx` smoke run from the worktree. A Sonnet **Workflow** built the
offline scaffolding (pure-logic `project.ts`/`batch.ts` + tool wiring); the live recon/fix was done
inline.

**Live-validated on camping-v2 (proven with real harvested frames):** `flow_open_project`,
`flow_generate_image`, `flow_refine`, `flow_generate_batch` (the speed tool — one session, N slides),
`flow_create_character`, and generate-with-character via the `@` picker. The plan→batch→iterate
workflow is documented in the `make-comic` skill. **Video** (`generateVideo`): the end-to-end
image→video mechanism is PROVEN (a real 1.96MB MP4 was harvested), but the uploaded-still→Animate
tile-targeting (hover-to-reveal more_vert in a media-rich grid) is hardened-but-not-clean-revalidated
— honest caveat in `docs/superpowers/flow-video.md`.

**The root cause that made the old scripts untrusted:** Flow's `getByRole` accessible names
concatenate the Material-icon ligature with the label with **NO space** (`arrow_forwardCreate`,
`imageImage`), so every spike-era selector with a literal space matched nothing. Other live fixes:
SPA crashes on double-`goto` (use tile-click SPA nav), stale-frame harvest (wait for a NEW media
UUID vs a pre-submit snapshot), and the create-bar Agent-vs-generation mode toggle. All recorded in
`docs/superpowers/flow-selectors.md` + `flow-video.md`.

**Merge note:** after merging, the primary checkout must restart the Claude session so `.mcp.json`
relaunches the flow server from main with the new tools (`flow_open_project`,
`flow_create_character`, `flow_generate_batch`, `character` param). Test pollution left in camping-v2:
characters `SmokeRef`/`SmokeChar` (several) + assorted test frames/clips — clean up when convenient.
See [[flow-mcp-and-art-direction-initiative]], [[flow-automation-integration]],
[[camping-karen-rework-initiative]].
