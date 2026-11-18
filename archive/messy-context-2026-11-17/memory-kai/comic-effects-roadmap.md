---
name: comic-effects-roadmap
description: Creative direction + phased roadmap for comic visual effects; Tier A Phase 1 shipped
metadata: 
  node_type: memory
  type: project
  originSessionId: 0ae14cd0-ccb5-4210-a9f1-2a3bca8d4644
---

Creative direction for `@badcode/comic` visual effects, decided in brainstorming Jun 2026. Throughline: **"the reader is the projectionist of a film transmitted from a broken future."** Four pillars: cinematic spine + ~2–3 scripted interactive beats; **clean cinematic restraint** (effects serve, never shout — glitch/datamosh only as rare deliberate exceptions); everything scrubbed by scroll (effects, transitions, dialogue reveal); audio = optional DnB bed + scroll-triggered SFX stings (music never scrubbed).

**Why clean-cinematic, not glitchy:** Kai explicitly chose restraint over a loud signature — distinctiveness comes from voice/story/music, not visual gimmicks. Honor this in all future effect work.

Spec: docs/superpowers/specs/2026-06-18-comic-effects-creative-direction-design.md. Research palette: docs/comics/effects-palette-research.md. Architecture splits two ways: **Tier A** needs no new primitive (just a wider Effect context); **Tier B** is one keystone ogl WebGL `<canvas>` widget (textures + uniforms) that unlocks depth-parallax + shader grades.

- **Phase 1 — Tier A foundations** ✅ shipped (branch feat/comic-asset-pipeline). EffectContext `{scrollPercent, velocity, pointer, audio}` (back-compat 3rd arg to effect.apply; velocity live, pointer/audio null until later); scroll velocity via MotionContext; scroll-scrubbed SpeechBubble `reveal` segments + `typewriter`; cinematic transitions pushIn/dipToBlack/lightDissolve; opt-in grain+vignette overlay. Plan: docs/superpowers/plans/2026-06-18-comic-effects-phase1.md. NOTE: motion verified by tests/typecheck/build only — human visual check at a comic route still outstanding.
- **Phase 2 — A5 pointer-parallax + A6 audio layer** ⏳ pending (populate the reserved pointer/audio context channels).
- **Tier B — B1 ogl canvas primitive, B2 depth-map parallax (+asset-pipeline depth pass), B3 shader grades/transitions** ⏳ pending.

Distinct from [[comic-authoring-roadmap]] (SP1 ergonomics/skills). Built on the SP1 library + packages/comic/AUTHORING.md. Executed via sequential Sonnet Workflow agents (one per task, gated).

**Screenshot-review loop (shipped Jun 2026):** `scripts/capture-comic.mjs` drives headless Chromium against the running dev server, scrolls a comic in N steps, writes PNGs Claude reads. The `/comic-review` skill documents the look→edit→re-capture loop. No Browser MCP server is registered with the CLI (the browser-extension MCP isn't exposed to the session) — the self-driven harness replaces it and is reproducible. First demo: camping got grain/vignette, a scroll-scrubbed typewriter monologue, and a BadCode-narrator dip-to-black outro replacing the old empty placeholder final page (outro also reconciled into docs/camping/story.md). Note: typewriter/transition *feel* still wants a live human eyeball — static frames can land mid-window.
