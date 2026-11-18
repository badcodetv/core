---
name: camping-karen-rework-initiative
description: From-scratch rework of Camping & Karen comics via the official pipeline; Camping-v2 Phase 1 canon complete
metadata: 
  node_type: memory
  type: project
  originSessionId: 1aebe093-8a60-439d-a350-468b1be20f04
---

Reworking the two imported comics (Camping, Karen) into faithful **parallel
`-v2` versions** rebuilt from scratch on the official pipeline (`make-comic` →
`flow-mcp` + `badcode-art-direction` → `@badcode/comic`), so each gets
pipeline-owned character sheets + per-panel prompt provenance. Originals stay
frozen as reference. Spec:
`docs/superpowers/specs/2026-06-27-camping-karen-from-scratch-rework-design.md`.

**Locked decisions:** full from-scratch art regen; Camping first (de-risk the
loop), then Karen; new `-v2` slugs; isolated git worktree
(`.claude/worktrees/camping-v2-rework`, branch `worktree-camping-v2-rework`);
house style is GLOBAL in the `badcode-art-direction` skill + a THIN per-comic
`style.md`; panel record = the art-direction skill's format; **commit per locked
image** during Phase 3.

**Phases:** 1 essence-capture (canon) → 2 character images → 3 panel images →
4 assemble → 5 animations (deferred, `animate-slide`).

**Status (2026-06-27):** Camping-v2 **Phase 1 COMPLETE** + **Phase 2 mostly done**
on the worktree. Phase 1: `docs/camping-v2/` has story, README, characters
(tarquin, bob, tent, wank-tank), thin style.md, storyboard index + p01–p20
(55→20 panels; ending = "Bob's grace"). Phase 2: harvested the existing
Tarquin/Bob sheets from Flow Images → `characters/img/*-sheet.jpg`; created a
dedicated **Flow project `camping-v2`** (`9b729074-da88-4668-a442-458e9a0f15ac`)
and registered official Flow Characters **@Tarquin** (`29e97ae3…`) and **@Bob**
(`7566666e…`) from those sheets. **Validated end-to-end:** p03 generated in
house style — plain-text `@tag` in the prompt binds the Character likeness;
documentary look on-brand.

**KEY LEARNINGS / gotchas:**
- Launch Flow via `./scripts/flow-chrome.sh` (WSL-side Chromium on CDP :9222) —
  NOT a Windows Chrome (its debug port isn't reachable from WSL; flow MCP returns
  NOT_RUNNING). I can launch it for the user as a background Bash.
- **Casting a character = attach a reference, NOT plain text.** In the prompt box
  type `@` → asset picker → pick "<Name> — Character" → Add to Prompt (a reference
  chip attaches) → then type the scene. Plain `@Name` text yields a GENERIC person
  (proven: camping-v2 p03 v2 = generic financier; v3 with the reference = real
  Tarquin). `flow_generate_image` only types text, so character panels need the
  reference attached via the Flow UI (Playwright) for now. Documented in the
  `badcode-art-direction` skill + `docs/superpowers/flow-selectors.md`.
- Direct-navigating Flow sub-routes (`/characters`) breaks the SPA — go via the
  home page and click the project tile.
- Keep only ONE Flow tab open or the flow MCP attaches to the wrong page.
- **`flow_generate_image` MCP tool is BROKEN vs live Flow UI** (`flow-client.ts:49`
  prompt-box locator times out; also must set Image mode — bar defaults to
  Video·8s). Until fixed, generate by driving the Playwright MCP UI. Fix this
  before Phase 3 scales to 20 panels.

**Phase 3 next:** generate the remaining 19 panels + the tent/wank-tank object
refs, via the `badcode-art-direction` loop, commit-per-locked-image. See
[[flow-mcp-and-art-direction-initiative]], [[animate-slide-initiative]].
