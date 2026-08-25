# Premiere 2026 built-in video effects catalogue

## What this covers

Every effect family Premiere Pro ships out of the box — no plugin, no subscription — as of the
25.5/26.x line (25.5, Sept 2025, reorganised 90+ effects/transitions into today's bins; 26.3.2 is
this project's version). Per family: the effects, what they're for, GPU acceleration, and the
internal **match name** a UXP script needs to apply them. Third-party plugins, AI panels and
UXP-vs-CEP mechanics are sibling briefs — named here only where they touch a native family.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
|---|---|---|---|
| Soften / defocus | Blur & Sharpen → Gaussian Blur | Drag, set blurriness | included |
| Motion blur on a still | Time → Pixel Motion Blur / Directional Blur | Pixel Motion Blur reads motion vectors; Directional Blur is a fixed streak | included |
| Grain-match AI footage | Noise & Grain → Noise | Amount + Type = Luminance for mono grain | included |
| Remove speckle | Noise & Grain → Median / Dust & Scratches | Radius 1–3px to avoid mush | included |
| Green-screen key | Keying → Ultra Key | Eyedropper Set Color, refine matte | included |
| Luma-based key | Keying → Luma Key / Track Matte Key | Use where dark background isolates subject | included |
| Stabilise AI-jitter | Warp Stabilizer | Apply, analyse, pick Smooth Motion | included |
| Corner-pin a screen insert | Distort → Corner Pin | Drag/keyframe 4 corner handles | included |
| Lens artefacts (flare, halation, bokeh) | Generate → Lens Flare; 25.5+ Stylize additions | Apply, reposition | included |
| Glitch/kaleidoscope transition | Transitions (25.5+) | Drag onto a cut, set duration | included |
| Colour grade | Color Correction (Lumetri) | out of scope — see native-ai brief | included |
| Script-apply/keyframe any effect | UXP `VideoFilterFactory` | `createComponent(matchName)`, set params | dev time |
| ffmpeg equivalent, no Premiere | ffmpeg filtergraph | `gblur`/`noise`/`chromakey`/`unsharp`/`eq` | free |

## Named tools

All entries below: Win + Mac, built-in, included free with Premiere Pro/Creative Cloud — no extra
cost (helpx + Videomaker, accessed 2026-08-21) — licence/platform not repeated per row.

### Blur & Sharpen
Gaussian Blur, Fast Box Blur, Camera Blur (Win only), Directional Blur, Sharpen, Unsharp Mask,
Reduce Interlace Flicker. Maturity: core since early Premiere; dependable, not exciting.

### Distort
Corner Pin, Lens Distortion, Magnify, Mirror, Spherize, Transform, Turbulent Displace, Twirl,
Wave Warp, Offset. Stable for years; Corner Pin is the one editors reach for most (2025-26 how-tos).

### Generate
4-Color Gradient, Lens Flare, Lightning, Ramp. Lightning needs no keyframing to animate; 25.5
layered in further bokeh/volumetric-ray/halation generators near this bin (CineD).

### Keying — Ultra Key
Professional chroma/luma keyer, successor to the older Chroma Key/Blue-Green Screen effects.
GPU-accelerated (Mercury Playback Engine page). De facto standard; reviews — including competitor
Boris FX's own blog — call it "good enough" for most green-screen work, reserving Primatte/Mocha
for hard edges.

### Noise & Grain
Median, Dust & Scratches (denoise), Noise, Noise Alpha (grain **add**, not reduce). No dedicated
modern film-grain generator beyond Noise was confirmed — a **gap**.

### Perspective
Basic 3D, Drop Shadow; bevel effects appear in some listings but are **unconfirmed** for 26.x.
Basic 3D is a cheap card-flip, not a real 3D camera.

### Stylize
Alpha Glow, Brush Strokes, Color Emboss, Find Edges, Mosaic, Posterize, Replicate, Roughen Edges,
Strobe Light, Glow (`ADBE Glo2`). Mostly a creative grab-bag; Mosaic/Posterize have genuine
documentary/redaction use (pixelate a face, band a gradient).

### Time
Echo, Pixel Motion Blur, Posterize Time, Time Warp; Time Displacement's Premiere-UI surfacing is
**unconfirmed**. Time Warp is the retime workhorse; Echo (ghost-trail compositing) is underused.

### Transform
Auto Reframe, Crop, Edge Feather, Horizontal/Vertical Flip (Offset moved here in the reorg).
Auto Reframe's AI engine may share cost infrastructure with Sensei/Firefly — verify if cost is
ever attributed to it specifically.

### Warp Stabilizer
The one stabilizer built in, via the shared AE codebase. GPU-accelerated (Mercury Playback Engine
docs). Standard first pass; Adobe Community bug threads (2020-2026) show it periodically breaks
on specific codec/proxy combinations — always preview the analysis before committing.

### Intrinsic components: Motion, Opacity, Time Remapping
Not bin effects — every clip carries these as **fixed effects** the moment it hits the timeline,
at the top of Effect Controls, and can't be removed.
- **Motion**: Position (X,Y), Scale (uniform % or split H/W), Rotation (unbounded degrees),
  Anchor Point, Anti-flicker Filter.
- **Opacity**: Opacity (%), Blend Mode.
- **Time Remapping**: right-click a clip → Speed (%), keyframeable ramps — distinct from the
  Time → Time Warp *effect* (which adds Trails, Shutter Angle). Don't conflate the two.

## Automation hook

**Premiere side.** Since 25.6+, UXP exposes a static `VideoFilterFactory` (Adobe's UXP reference,
2026-08-21):

```
VideoFilterFactory.getMatchNames()            → Promise<string[]>
VideoFilterFactory.getDisplayNames()           → Promise<string[]>  // same order as above
VideoFilterFactory.createComponent(matchName) → Promise<VideoFilterComponent>
```

Adobe's own worked examples are `'PR.ADBE Solarize'` and `'AE.ADBE Mosaic'` — the convention is
**`PR.ADBE …`** for a small Premiere-native set, **`AE.ADBE …`** for the majority ported from the
shared After Effects codebase. For anything not below: call `getMatchNames()` +
`getDisplayNames()` once, zip them, grep the display name (e.g. `"Blur"`) — don't guess the string.

| Effect | Match name | Confidence |
|---|---|---|
| Gaussian Blur / Directional Blur | `AE.ADBE Gaussian Blur 2` / `Motion Blur` | confirmed |
| Turbulent Displace / Twirl / Wave Warp | `AE.ADBE Turbulent Displace` / `Twirl` / `Wave Warp` | confirmed |
| Corner Pin / Mirror / Spherize / Magnify | `AE.ADBE Corner Pin` / `Mirror` / `Spherize` / `Magnify` | confirmed |
| Ramp / Lens Flare / 4-Color Gradient | `AE.ADBE Ramp` / `Lens Flare` / `4ColorGradient` | confirmed |
| Mosaic / Posterize / Find Edges / Glow | `AE.ADBE Mosaic` / `Posterize` / `Find Edges` / `Glo2` | confirmed |
| Echo / Posterize Time / Time Displacement | `AE.ADBE Echo` / `Posterize Time` / `Time Displacement` | confirmed |
| Drop Shadow / Ultra Key / Gradient Wipe | `AE.ADBE Drop Shadow` / `Ultra Key` / `Gradient Wipe` | confirmed |
| Solarize | `PR.ADBE Solarize` | confirmed (Adobe's example) |
| Color Replace / Gamma Correction / Extract / Color Pass / Lens Distortion / Levels | `PR.ADBE <name>` | **unconfirmed** — community forum only |
| Warp Stabilizer | `AE.ADBE SubspaceStabilizer` | **unconfirmed, low** — bug reports only |
| Motion / Opacity / Time Remapping | none — intrinsic `Component` properties, not filters | n/a |

**ffmpeg side.** TESTED 2026-08-21 against a synthetic 1376x768 clip in the scratchpad on this
box's ffmpeg 4.4.2:

```bash
ffmpeg -i in.mp4 -vf "gblur=sigma=8" out.mp4                          # TESTED — ~= Gaussian Blur
ffmpeg -i in.mp4 -vf "unsharp=5:5:1.0" out.mp4                        # TESTED — ~= Sharpen
ffmpeg -i in.mp4 -vf "noise=alls=20:allf=t" out.mp4                   # TESTED — ~= Noise (grain)
ffmpeg -i in.mp4 -vf "curves=preset=increase_contrast,eq=saturation=1.1" out.mp4   # TESTED — basic CC
ffmpeg -i in.mp4 -vf "chromakey=0x00ff00:0.1:0.1" -pix_fmt yuva420p out.mov         # TESTED — ~= Ultra Key
```

Reverse/ping-pong/eased-zoompan/retime/concat/crop recipes already live in
`docs/flow/post-production.md` — not repeated here.

## BadCode fit

Near-black 1376x768 8s Veo clips are already low-noise, low-detail, dark:

- **Noise/grain** is worth using deliberately — AI footage is often too clean; a light
  luminance-only grain pass helps it sit next to 35mm-documentary stills.
- **Blur** (Gaussian/Directional): push sigma conservatively — heavy blur smears a thin light
  source into a glow blob rather than a soft falloff. Test at export resolution, not a preview.
- **Ultra Key/chroma keying** is near-irrelevant here — no green screen in Flow footage, and
  luma-keying a near-black frame is fragile (luma bands overlap). Skip it.
- **Warp Stabilizer** crops in to stabilise, shrinking an already-fixed frame further — budget for
  that in framing before applying it to wide architecture shots.
- **Mosaic/Posterize** can *reduce* banding-looking artefacts in near-black skies if used as a
  controlled step rather than left as compression noise.
- **Lens Flare / Generate** fights the brand register directly — CLAUDE.md is explicit: "no lens
  flares." Don't apply this family to BadCode panels.

## Traps

- The `PR.ADBE`/`AE.ADBE` split is **community-sourced**, not Adobe-published exhaustive —
  Adobe's own doc gives only two worked examples. Verify at runtime with
  `getMatchNames()`/`getDisplayNames()`, don't hard-code the table.
- A formal **"Obsolete" effects category could not be confirmed** for 26.x — older keyers are
  known to be superseded by Ultra Key in practice, but no page enumerating a literal Obsolete bin
  was found. Say "superseded," not "removed."
- **GPU acceleration is documented only at the platform level** ("color correction, blur, and
  several transitions" per Adobe) — no per-effect table for 26.x exists in sources checked. The
  in-app accelerated-effect icon is the only reliable source.
- **ffmpeg filters are not pixel-identical** to their Premiere counterpart — `gblur` and Gaussian
  Blur use different kernels; `chromakey` and Ultra Key differ in matte quality. Use ffmpeg for
  headless "close enough" passes, not as a render oracle.
- `VideoFilterFactory` is new (documented "since 25.6") — a project supporting older 25.x installs
  needs an ExtendScript fallback or a hard version floor; not tested live here, doc-only.

## Sources

- [Effects and transitions reorganization](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/effects-and-transitions-reorganization.html) — 2026-08-21 — Adobe's bin renaming
- [Mercury Playback Engine (GPU)](https://helpx.adobe.com/in/premiere/desktop/get-started/download-and-install/mercury-playback-engine-gpu-accelerated-in-premiere-pro.html) — 2026-08-21 — which effect classes are GPU-handled
- [Every native effect you should know — Videomaker](https://www.videomaker.com/how-to/editing/editing-technique/every-adobe-premiere-pro-native-effect-you-should-know/) — 2026-08-21 — bin-by-bin roundup
- [Premiere Pro 25.5 built-ins — CineD](https://www.cined.com/premiere-pro-25-5-adds-90-built-in-effects-transitions-and-animations-plus-faster-playback/) — 2026-08-21 — Sept 2025 reorg notes
- [GPU Effects & Transitions SDK guide](https://ppro-plugins.docsforadobe.dev/gpu-effects-transitions/gpu-effects-transitions/) — 2026-08-21 — how a plugin declares GPU render path
- [AE first-party match names](https://ae-scripting.docsforadobe.dev/matchnames/effects/firstparty/) — 2026-08-21 — canonical `ADBE …` strings shared with Premiere
- [VideoFilterFactory — UXP API reference](https://developer.adobe.com/premiere-pro/uxp/ppro_reference/classes/videofilterfactory/) — 2026-08-21 — official method signatures, v25.6+
- [Effect Component Names thread](https://forums.creativeclouddeveloper.com/t/effect-component-names/10611) — 2026-08-21 — community match-name list, not Adobe-authoritative
- [Warp Stabilizer settings](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/warp-stabilizer-settings.html) — 2026-08-21 — parameter names
- [Noise & Grain effects](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/noise-and-grain-effects.html) — 2026-08-21 — Median/Dust & Scratches/Noise definitions
- ffmpeg filters — verified directly by running `gblur`/`noise`/`curves`/`chromakey`/`unsharp` against a synthetic 1376x768 clip, 2026-08-21
