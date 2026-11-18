---
name: animate-slide-initiative
description: "animate-slide skill — turn a comic slide into a Flow video; spec+plan+skill done, Flow video spike pending"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6453764a-0446-4742-9e6a-67720024912d
---

Initiative to weave Google Flow image→video (Veo) clips into comics: *"point at a comic, turn this slide into a video, here's the motion prompt."* The video half of the Flow automation work the image loop deferred. See [[flow-automation-integration]] and [[comic-authoring-roadmap]].

**Status:** MERGED to `main` via PR #4 (merge commit 1ff62d0, 2026-06-26). Branch `feat/animate-slide` is done.

**Key architecture finding (non-obvious):** comics wire animations via the **manifest + `resolveAnimation('anim/<key>')`** (Karen's proven path: a bucket folder `comics-v2/<comic>/anim/<key>/video.mp4` → `badcode assets-build` → renditions/poster/manifest → `<AnimationWidget>`), **NOT** via `comic.meta.ts`. The `comic-meta` `video` schema is unused and runtime-ignored (Karen's 9 live animations aren't declared there). So: **no `comic.meta.ts` change and no new CLI code** — `gsutil` + the existing `assets-build` cover everything. Playback (`AnimationWidget`/`VideoSource`) and asset processing already existed.

**Done (spike COMPLETE, 2026-06-25 — commit 97a594d):** spec, plan, the `animate-slide` skill, CLAUDE.md + make-comic discoverability, AND the Flow video spike. `docs/superpowers/flow-video.md` is recorded, and **Karen slide i38 is live as `anim/a12`** — a scroll-scrubbed Veo 3.1 Quality clip (1280×720, 24fps, 8s) with its narration bubble, verified rendering in the browser. Record: `docs/karen/storyboard/p38.md`.

**Flow video UI (recorded in flow-video.md):** agent Settings → Video model = Veo 3.1 Quality, aspect 16:9 (global default, not per-prompt). Upload via Add Media → Upload media (⚠️ Playwright MCP only allows uploads from under the repo root — stage in `.playwright-mcp/`, not `/tmp`). Hover the uploaded tile → More → **Animate** (image→video) → type motion prompt → Create → Approve the credit gate (100 credits/Quality clip). Harvest = same signed-URL trick as images, but a `<video>` source.

**Two traps corrected after real use:** (1) completion signal = resolve the media URL → `content-type: video/mp4` (NOT `videoWidth`, which stays 0; NOT the queue chat text, which lingers); (2) `assets-build -m` must be an ABSOLUTE path — `npm run --workspace @badcode/cli` runs from `packages/cli/`, so a relative `-m` writes the manifest to the wrong tree.

**Scratch convention:** `.flow-screenshots/` (gitignored PNGs + committed README) for browser captures. The skill remains bucket-pipeline-only (stops if manifest `basePath` isn't `comics-v2/<comic>`); Magic Money Tree is local/v1 and would need bucket migration first. Next time, `/animate-slide` can drive the whole loop using flow-video.md.

**Second slide + interactive co-view (2026-06-26, commit e0bb112):** Karen i05 (kitchen put-down) is now live as `anim/a13` (record `docs/karen/storyboard/p05.md`). The skill gained a **"Co-viewing the comic (interactive mode)"** section: it **auto-starts BOTH the dev server and `./scripts/flow-chrome.sh` as background processes** — the Playwright MCP **re-attaches to a freshly-launched browser with no session restart** (proven), so one shared WSLg Chromium is both what Kai watches and what Claude screenshots; scroll it and it scrolls on his screen. Workflow: browse comic together → pick slide → shape motion prompt in conversation → judge the harvested clip BEFORE the slow `assets-build` → build in → review scroll-scrubbed in the real comic.

**More Flow recipe findings (in flow-video.md):** video model setting **resets per project** (re-select Veo 3.1 Quality each session); a genuine failure reads **"Oops, something went wrong"** and **re-posts the Approve gate — must retry** (distinct from benign "scheduled in queue"; first i05 attempt failed, retry worked); relaunched Flow tabs throw a transient OAuthCallback error but a fresh `browser_navigate` is signed-in.
