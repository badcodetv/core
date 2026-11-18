---
name: homepage-atlas-initiative
description: "Active homepage rebuild \"The Atlas\" — worktree, spec, and Phase 1 plan locations + locked design decisions"
metadata: 
  node_type: memory
  type: project
  originSessionId: 96b816af-7256-4736-af3e-be40da6b82d9
---

Active initiative (started 2026-06-18): rebuild the BadCode homepage as **"The Atlas"** — a cinematic auto-fly-in that resolves into a free-roam, semantic-zoom star-chart of the GPOM fork.

**Where it lives:** git worktree at `.claude/worktrees/homepage-rewrite` on branch `worktree-homepage-rewrite` (branched from `feat/homepage-atlas`, which carries the committed spec).
- Spec: `docs/superpowers/specs/2026-06-18-badcode-homepage-design.md`
- Phase 1 plan: `docs/superpowers/plans/2026-06-18-homepage-atlas-phase1.md`

**Locked design decisions:** zoom-ladder mechanic (map→branch→story→content, semantic zoom IS navigation); songs-live-in-stories (map stays pure story, no music branch); Deep Field cosmos visuals read through a Cold Archive terminal HUD; auto-play skippable intro; drag+zoom+click-to-fly nav. Built on the existing R3F scene in `apps/web/src/home/` (new code under `home/atlas/`), reusing the existing `assets.manifest.json` pipeline for media plates in later phases. Phase 1 = the shippable map spine; Phase 2 = dioramas (video plates, portals, audio); Phase 3 = branch corridor + perf.

**2026-07-03 restructure:** the Atlas is no longer the homepage. It moved intact to
`/gitpush-origin-master` (route change only — the Atlas code under `home/atlas/` is
path-agnostic). `/` is now the **Transmission Index**: a lightweight 2D BadCode umbrella
landing page (`src/routes/BadCodeHome.tsx` + `src/home/landing/` + `src/home/catalog.ts`)
that maps ALL content — GPOM as flagship "ARC" card with an animated fork glyph, story +
music manifests with status stamps (RECEIVED/INCOMING/PENDING), and the physics texts.
Rationale: BadCode is the umbrella; GPOM had hijacked the whole site. Legacy `/#node`
links redirect; catalog derives status from `homeSteps` (single source of truth). New
`--signal: #e8c98a` token in index.css for INCOMING/PENDING stamps.

**2026-07-13 GPOM demoted to peer comic:** Kai's framing — the 3D Atlas is not "the site",
it's *one story*, and the 3D graph is just that story's rendering (like ScrollComic is
Camping's). Atlas now lives at `/comics/gitpush-origin-master`; `/gitpush-origin-master`
(+hash) and legacy `/#node` redirect there. Homepage hero "ARC" card + ForkGlyph deleted;
Stories = exactly four rows, GPOM first as **BC-000** (BC-004 gpom-short / BC-005
emperors-coin stay live at their routes but deliberately unindexed). New **CHANNELS**
section (YouTube/SoundCloud/Community) as URL-ready `incoming` placeholder rows in
`catalog.ts` (`Channel` type: goes live by setting `url` + `status:'received'`). Comic
back button simplified: always `← badcode` → `/`. New invariants test:
`src/home/catalog.test.ts`.

Relates to [[comic-library-design]] and [[progressive-comic-loading]].
