---
name: progressive-comic-loading
description: "Status of the progressive/lazy comic image-loading work — pipeline shipped, runtime loader pending"
metadata: 
  node_type: memory
  type: project
  originSessionId: c364a5d1-6f57-45b0-8a62-e97ec013e458
---

Effort to fix the sluggish scroll-comic viewer (e.g. `/comics/camping-jack-test`, 3,540 full-res JPGs). Design split into two subsystems sharing one contract (a path-keyed `assets.manifest.json`):

- **Spec:** `docs/superpowers/specs/2026-06-16-progressive-comic-loading-design.md`
- **Plan 1 (offline asset pipeline):** `docs/superpowers/plans/2026-06-16-comic-asset-pipeline.md` — **DONE & merged to `main`** (as of 2026-06-16). New `@badcode/comic-manifest` types package + a path-based `badcode assets-build --src <bucket-subfolder> --manifest <path>` CLI command in `@badcode/cli` (Sharp → low 720w / high 1920w WebP + ThumbHash, uploads to `derived/`, emits manifest). Storyteller-agnostic (no comic IDs). Smoke-tested live against GCS: 7.8 MiB PNG → 135 KiB high / 23.5 KiB low.
- **Plan 2 (runtime loader): NOT yet built.** Spec section B: `createComic(manifest)`/`resolve()` in `@badcode/comic`, progressive `ImageWidget` (thumb→low→high), `AnimationWidget`, shared priority scheduler with abort/LRU eviction.

**ANIMATION DIRECTION CHANGED (2026-06-17) — animations should be VIDEO, not frame sequences.** Validated by a throwaway spike at `apps/web/public/spike/` (git-ignored mp4s; `index.html` self-contained, mp4box via esm.sh CDN). Findings: WebCodecs→`<canvas>` scroll-scrubbing is smooth (incl. windowed on-demand GOP decode + LRU eviction on a 242-frame clip, bounded memory) and ~10× smaller than shipping WebP frames (732 KB vs ~30 MB). Naive `<video>.currentTime` is janky unless re-encoded all-keyframe (bigger). Recommended encode: 480p-ish proxy, H.264, `-g 12 -bf 0` (no B-frames → decode order = presentation order). Source `video.mp4` exists for `a17f2cc4` comics but NOT `bebf53aa` (frames only) → pipeline needs a frames→video re-encode step. NEXT: revise the spec for video animations (an animation = ONE manifest entry, killing the per-frame bloat), then build Plan 2's `AnimationWidget` = WebCodecs windowed decode→canvas with a fallback for unsupported browsers.

Key decisions: ThumbHash stored as **compact base64 of raw hash bytes (~28 chars)**, decoded to a data-URI client-side in Plan 2 (NOT a pre-decoded data-URI — that bloated the manifest ~100×). Idempotency keys on variant presence + prior manifest, not content hash — use `--force` after editing a source in place (content-hash is future work).

Open: the legacy `camping-jack-test` comic's images span **3 storyteller UUID prefixes** (`bebf53aa` 2828, `a17f2cc4` 709, `ae0cc252` 3), so it doesn't map to one `--src`. The intended end state is migrating each comic's assets into a dedicated `comics-v2/<slug>/` bucket folder. Full resize run not yet done (only the 3-image `ae0cc252` smoke test, whose `derived/` + manifest are now in that legacy prefix). See [[storyteller-import-cli]], [[comic-library-design]].
