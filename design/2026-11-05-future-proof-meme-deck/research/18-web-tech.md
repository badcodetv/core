# 18 - Web tech for a meme slideshow that is also video

4 searches used of 8. Solidity: P = primary, S = secondary, H = hearsay/unverified.

## Repo facts (checked locally, primary)
- apps/web: Vite ^5.4, React ^18.3, TS ^5.6, three ^0.169, @react-three/fiber ^8.17, @react-three/drei ^9.114, gsap ^3.12. R3F + GSAP are already installed.
- Node 22.14, ffmpeg on PATH. playwright ^1.49 exists in flow-mcp/listen-mcp (not apps/web).
- R3F v8 pairs with React 18. v9 needs React 19. Do NOT upgrade for this; stay on the v8 line (never mix lines).

## Versions (as of search; re-check `npm view` before pinning)
| Tool | Finding | Source | Solidity |
|---|---|---|---|
| reveal.js | npm latest 6.0.1; 6.0.0 added an official React wrapper, Vite build, ships own TS types, .esm.js renamed .mjs; last 5.x = 5.2.1 | https://socket.dev/npm/package/reveal.js/overview/6.0.1 | S |
| Slidev | Built-in recording + camera view (embedded or two separate files), presenter mode, export PDF/PPTX/PNG; no MP4 export found. Version unconfirmed (mirror showed 0.49.x, stale) | https://sli.dev/features/recording , https://sli.dev/guide/exporting | P (docs, as snippets) / version H |
| R3F / drei | v9 + drei 10 pair with React 19 (Dec 2025 examples PR: fiber 9.4.2, drei 10.7.7, React 19.2.3); current may be newer | https://r3f.docs.pmnd.rs/tutorials/v9-migration-guide , https://github.com/pmndrs/examples/pull/95 | P / S |
| Playwright capture | built-in recordVideo is real-time, VP8 ~1 Mbps, not reproducible. A newer `page.screencast` `onFrame` hook exists (version claim inconsistent in the post) | https://dev.to/mutsuntsai/replacing-playwrights-hardcoded-vp8-encoder-a-deep-dive-into-pagescreencast-43ee | S |
| Deterministic capture | puppeteer-capture uses CDP HeadlessExperimental + virtual clock (Puppeteer only) | https://cdn.jsdelivr.net/npm/puppeteer-capture@1.58.0/README.md | S (vendor) |
| Spectacle | NOT researched (budget); no claim made | - | - |

## Options compared
- **reveal.js 6**: best built-in speaker view (notes, timer, second window), keyboard, vertical stacks, fragments, auto-animate, `?print-pdf`. 3D scene per slide = mount a canvas by hand in slide-ready events. Fine, but a second framework beside React.
- **Slidev**: Vue/Markdown, own Vite app. Great authoring and recorder, but Vue in a React monorepo = separate app, and the three.js scenes need Vue wrappers. Skip.
- **Spectacle**: React-native but no evidence gathered; skip unless asked.
- **Custom React + R3F deck (recommended)**: ~150 lines own the deck: slide array, index in URL hash (`#/7`), keyboard (arrows, space, PageUp/Down, F fullscreen, N notes, P presenter), step "fragments" per slide, `<Canvas>` per 3D slide, GSAP/CSS for memes. Each slide is a React component, so memes, three.js scenes and captions share one tree. Matches the existing stack and the project's "code-first, scripted" habit (comic lib).

## Recommended stack
1. **New route in apps/web** (e.g. `/future-proof`) or sibling package `packages/deck` (generic engine, no story look, mirroring how `@badcode/comic` is generic). Story look lives in `docs/stories/.../look.md`, not the engine.
2. React 18 + R3F 8 + drei 9 + GSAP (all installed). Add nothing for core. Optional: `zustand` for step state (tiny).
3. **One shared WebGL context**: render 3D slides in a single fixed `<Canvas>` behind the DOM slides and swap scene by index (drei `<View>` or conditional groups). Mounting many Canvases leaks contexts and hitches on advance.
4. **Time-driven animation**: drive every scene from a `t` value (a clock the deck owns), never `Date.now()`/raw rAF. This single rule makes video capture deterministic later.
5. **Presenter mode**: `BroadcastChannel` between `/future-proof` and `/future-proof/presenter` (current slide, step, notes, timer). No server.
6. **Slide data as JSON/TS** (`slides.ts`: id, spoken line, meme asset, scene id, steps) so the skill can generate decks and a talk-to-camera script from the same source.
7. **Memes**: static PNG/WebP/MP4 under public/; text overlaid as live HTML (Impact-style text drawn by CSS) so templates stay editable and 9:16 re-layout is free. Licensing of source images is a separate question (do not hotlink; keep a credits list).

## Recording / video (two lanes)
- **Lane A, talk to camera (fast)**: OBS (or Slidev-style recorder idea) with deck in a browser source/window chroma or picture-in-picture, Kai advances by keyboard. Real time, no engineering. Use for the first cut.
- **Lane B, deterministic render (polished/shorts)**: `/future-proof?render=1&slide=7&fps=30` exposes `window.__setT(seconds)` and `window.__ready`. A Node script (Playwright, already in monorepo) loops frames: `__setT(i/fps)` -> `page.screenshot()` (or `canvas.toDataURL`) -> pipe PNG/JPEG to `ffmpeg -framerate 30 -i - -c:v libx264 -crf 18 -pix_fmt yuv420p`. Slower than real time but frame-exact. Do not use Playwright `recordVideo` (real-time, VP8, low bitrate). `page.screencast onFrame` is a middle option; verify it exists in the installed Playwright first.
- **Layers fit the repo's hybrid method**: deck frames (or silent clip per slide) go to Premiere as clips; voice/talk footage is laid over there.
- **9:16 shorts**: same deck, `?aspect=9x16`: a CSS container sized 1080x1920 (Playwright `viewport`, deviceScaleFactor 1) with a per-slide `layout.vertical` override; R3F camera uses `aspect`-aware framing (fit by width). Design memes with a centre-safe region so one slide serves 16:9 and 9:16; accept a dedicated vertical layout for text-heavy slides. Shorts = one slide (or 3) per clip, auto-cut from slides.ts.
- Export also PDF (`window.print` stylesheet) for a downloadable deck, and PNG per slide for socials.

## Artifact-hosted prototype
- Artifact = single self-contained HTML (<=16MB, scripts only from cdnjs/jsdelivr/unpkg with pinned versions). Fastest prototype: **vanilla JS deck + three.js from cdnjs (pin an exact r1xx version) with a hand-written ~100-line deck engine** (same keyboard/hash/presenter logic). Skip React/R3F there (no build step; JSX needs a transform).
- reveal.js from jsdelivr also works in an Artifact (pinned 5.2.1 is safest; 6.x moved to .mjs paths), but a custom engine keeps the data model identical to apps/web.
- Keep `slides.ts` data format portable: Artifact reads a JSON blob, apps/web imports the same JSON. Prototype in Artifact, then port scenes to R3F (three code mostly transfers; R3F is a thin wrapper).
- Artifacts use localStorage only for per-viewer convenience; presenter sync across windows works via BroadcastChannel within one origin. Cross-device remote needs the artifact `db` capability (load artifact-capabilities skill).

## Recommendation in one line
Custom React deck in apps/web on the existing R3F v8 + GSAP stack (data-driven slides.ts, time-driven scenes, BroadcastChannel presenter view), OBS for the first talk-to-camera cut, a Playwright + ffmpeg frame-stepped renderer for exact 16:9 and 9:16 exports, and a vanilla three.js Artifact for the first throwaway prototype.

## Open / unverified
- Current Slidev, Spectacle, Playwright and three.js release numbers; run `npm view <pkg> version`.
- Whether `page.screencast` exists in Playwright installed here.
- Whether a React 19 + R3F 9 upgrade of apps/web is wanted (not needed for this).
