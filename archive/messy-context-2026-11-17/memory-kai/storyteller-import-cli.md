---
name: storyteller-import-cli
description: Storyteller comic import CLI (pull/generate) built 2026-06-10 on branch worktree-storyteller-import; e2e blocked on badcode.tv credentials
metadata: 
  node_type: memory
  type: project
  originSessionId: 0c5ecb3f-c093-4f0a-83d6-2dfb8799a502
---

The storyteller comic import tooling (plan `docs/superpowers/plans/2026-06-09-storyteller-comic-import.md`) was implemented 2026-06-10 in the worktree `.claude/worktrees/storyteller-import` (branch `worktree-storyteller-import`, 7 commits on top of 56b2065, final review: ready to merge). `npx badcode pull <url>` + `npx badcode generate <slug> [--force]` in `packages/cli`.

**Verified end-to-end 2026-06-10** after Kai fixed the `.env` password (earlier 403s were a bad password; login payload is `{email,password}`). Pulled the test comic 97a4cb4c… ("camping-kai"): 15 pages, 20 images, 702 animation frames (258MB). Generated TSX+meta, workspace typecheck clean, and all 15 pages render in the dev server (Shard, office/Tarquin speech bubble, Waitrose+BMW+tent, forest-road animation, empty-page placeholder).

Three real bugs surfaced only against live data (each a separate fix commit on the branch): (1) live API returns image `media.path` as ABSOLUTE GCS URLs but frame paths as relative keys → added `resolveAssetUrl`; (2) assets must be written under `apps/web/public/comics/` (Vite's public dir), not repo-root `public/`; (3) content-less "capsule-page" → generate now emits a NarrationBox placeholder so the TSX typechecks. 62 CLI tests pass.

**Asset policy (per Kai, 2026-06-16):** images/animation frames live permanently on the public GCS bucket. Tooling was changed so `generate` emits REMOTE bucket URLs (via resolveAssetUrl) and `pull` is config-only by DEFAULT (`--assets` to also download). So NO local image assets are committed. Verified: all bucket URLs return HTTP 200 with no auth (public bucket).

Storyteller stores every text-bubble as rich HTML (`<p><span style>`, `<strong>`, entities); added `htmlToText()` in generate so bubbles render clean plain text. (Inline styling like font/colour is dropped — curate in code later if wanted.)

Two rendering bugs found+fixed 2026-06-16 (root causes non-obvious): (1) Storyteller stores bubble `font_size` as px but tolerates tiny values (e.g. 1.2) and CLAMPS to [10,24]px at render (storyteller SpeechBubble.tsx getFontSize); generate was emitting it raw → 1.2px invisible text. Fixed with `clampFontSize` in generate.ts. (2) `@badcode/comic` useTransitions left the outgoing page painted (its `cancelled` cleanup flag, firing on every scroll dep-change, suppressed setOutgoing(null)) → scroll flicker / stuck layer; also replayed transitions for pages scrolled past. Fixed in two passes: (a) always clear outgoing on completion + instant-cut multi-page jumps (isInstantCut) — fixed stuck layers/stale-page replay; (b) the ACTUAL end-of-transition flicker = resetLayer cleared inline zIndex, React skips rewriting an unchanged zIndex prop, so both layers went z-index:auto and painted in DOM order → on scroll-UP the higher-index outgoing page flashed on top at the opacity-snap. Fix: resetLayer must NOT touch zIndex (React owns it via PageContext: current=2, outgoing=1). Bubble text now renders at 10px (faithful to storyteller; bump fontSize when curating).

Three comics imported + committed on branch `worktree-storyteller-import` (commit ca10441, since merged to main): camping-kai, karen-jack-test, camping-jack-test. They reference the bucket, are browsable by DIRECT URL `/comics/<slug>` (resolveComic in apps/web/src/home/comics.ts now renders any liveComics entry even without a timeline beat — Kai explicitly did NOT want them wired into the 3D home timeline). To resolve a comic NAME→UUID, `GET /api/v1/comics` (authed) lists all comics with config.name. Each comic still a raw scaffold: default effects, meta TODOs (meta not imported at runtime). `.env` gitignored — copy into a fresh worktree manually. Related: [[content-migration-deferred]], [[auto-push-on-commit]].
