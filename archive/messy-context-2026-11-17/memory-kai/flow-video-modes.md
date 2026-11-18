---
name: flow-video-modes
description: "Live-settled Flow video facts: source modes, duration/count in the compose popover, refine via Reuse prompt, characters in video, and the picker traps"
metadata:
  node_type: memory
  type: project
  originSessionId: d21d9736-2e38-4cc1-82fc-af495fa3424b
  modified: 2026-08-12T20:13:03.415Z
---

Facts about Flow's video composer that cost real time to learn, all settled by clicking
(2026-08-12). Full write-up: `docs/superpowers/flow-video.md`.

- **One composer, four source modes.** `startImage` alone = Animate; `startImage`+`endImage` =
  first/last frame; neither = text-to-video. **End-only does not exist** — the slot fills and is
  then flagged invalid. First+last works on **every Veo 3.1 tier**, not just one, and Omni Flash
  rejects a last frame.
- **The per-turn controls live in the compose-bar popover, not the Settings panel.** Duration
  (4/6/8/10s, 10s Omni-Flash-only) AND output count (x1–x4). The Settings panel's equivalents are
  defaults that the popover overrides — which is exactly how `count` came to be silently ignored:
  a `count: 2` request produced one clip and left the trigger reading `x1`.
- **Animate leaves the bar in AGENT mode**, which has no config popover at all. Toggle out via
  the `Agent` pill; the attached source chip survives it.
- **Refine = the clip's own `Reuse prompt`**, which restores prompt + **source still** + Frames
  mode. So `flow_refine_video` needs nothing but the clip's `mediaId`.
- **Extend and video Edit do not exist** in this account, on any tier. Clicking a clip opens the
  **scene editor** (`/edit/<sceneId>`, a timeline with `Add Clip`) instead.
- **A Character CAN be cast in a video turn** (`flow_generate_video({ character })`) — but that
  proves the mechanism, not the likeness. For a face that must stay right, animate an
  art-directed still.

**The picker traps, which break workflows rather than single calls:**

- Video mode has **no `add_2 Create` button**, so the asset picker was unreachable after any clip
  — 90s timeouts on `flow_list_media`, character creation and every reference attach. The `@` key
  opens the same picker in every mode; that is the fallback now.
- **The picker lists only what the current mode can USE.** In video mode: zero clips. `listMedia`
  asserts image mode before reading.
- A clip tile is `img[alt="Video thumbnail"]` at rest and **hover SWAPS it for the `<video>`** —
  so the hover target and the card anchor cannot be the same element.

See [[flow-wave-b-validation]], [[flow-policy-blocks]], [[flow-automation-integration]].
