---
name: project-overview
description: "What the BadCode repo is, its structure, and the relationship to the storyteller brainstorm repo"
metadata: 
  node_type: memory
  type: project
  originSessionId: 242b3d3d-3be1-4fde-b97e-085d6f07f235
---

`/home/kai/projects/badcode/badcode` is the canonical, publishable **BadCode** website — an art collective using stories (presented as scroll-driven comics) and drum & bass to push political/economic ideas. Fictional frame: a superintelligence from a dystopian future, sent back in time.

**GitPush Origin Master** is the overarching project title / large timeline everything hangs from (also an upcoming title track) — to be worked up much more. **EP1** is a deliberately-plain three-track *teaser* beneath it: **Camping, Karen Will Lead the Revolution, Emperor's New Coin** — each ships as comic + music track only (NO per-story AI agent for now; that's later/separate). Fire Sale & Out of the Jungle were dropped from EP1 to the in-development pool (not retired). Reworked 2026-06-02 — superseded the old four-track list (camping/karen/fire-sale/out-of-the-jungle).

Bootstrapped 2026-06-02 by mining the sibling brainstorm repo `/home/kai/projects/badcode/storyteller` (left untouched as the source). Structure: npm-workspaces monorepo — `apps/web` (Vite+React+TS SPA), `packages/comic` (`@badcode/comic`), `docs/`, `ideas/`. See `CLAUDE.md` and `docs/`.

The voice/vision docs were authored fresh from `storyteller/badcode/prompts/system/ideas.md` (the manifesto). See [[comic-library-design]] and [[content-migration-deferred]].
