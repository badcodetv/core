---
name: comic-library-design
description: "Why @badcode/comic is code-first, and how its scroll engine works"
metadata: 
  node_type: memory
  type: project
  originSessionId: 242b3d3d-3be1-4fde-b97e-085d6f07f235
---

`@badcode/comic` (`packages/comic`) is a **code-first** scroll-driven comic library, deliberately inverting the storyteller repo's WYSIWYG/config-JSON approach. Authors compose typed React components (`<ScrollComic>`/`<Page>`/`<ImageWidget>`/`<SpeechBubble>`/`<SidePanelText>`) and drive animation with typed factory functions (`zoom({amount})`, `crossfade()`, `scrollIn()`) — no editor, no `page.config` string blob.

**Why:** the user wants freedom to plug anything into the front-end rather than being constrained by a UI that generates a data structure. The valuable scroll engine was kept; the editor UI, MUI/Emotion, GSAP (the engine never used it — it's raw scroll + Web Animation API), and Go-generated types were discarded.

Engine: a tall scroll track + `position: sticky` stage; scroll position maps to `(currentPage, perPageScrollPercent 0..1)`. Effects run via `useScrollEffect` (mutate `el.style`); transitions are WAAPI, fired on page change. Factory functions imported from subpaths: `@badcode/comic/effects`, `/transitions`, `/text`. Worked example: `apps/web/src/comics/camping/CampingComic.tsx`. See [[project-overview]].
