# What this Premiere can actually do

**Harvested live from the install on 2026-08-21** with `premiere_list_effects` and
`premiere_list_transitions` — **106 video effects and 118 video transitions**, every one of them
free and already installed. This is an inventory, not research: if a name is in this file, it is on
the machine.

> **Match names are the address, display names are not.** Premiere ships several effects with the
> same or near-identical display names from different generations, and no vendor publishes their
> match names. **Always `premiere_list_effects({ query })` first** and copy the match name from the
> result. This file is a map, not a substitute for that call.

Companion files: [`recipes.md`](./recipes.md) turns these into concrete tool calls;
[`api-notes.md`](./api-notes.md) records how the API behaves when you use them.

---

## The one rule that saves the most time

**There are no paid plugins here and we are not buying any** (Kai, 2026-08-21: *"they all sound far
too advanced, and for smoke and fire we could use Flow anyway"*). The stack is: Premiere built-ins,
Lumetri, the absorbed Film Impact set, MOGRTs, ffmpeg, and **Flow for anything that needs to be
invented**. When something seems to need a plugin, the answer is almost always *generate the element
in Flow on black and composite it*, not *buy Sapphire*.

---

## Video effects, grouped by what you would actually ask for

### Colour and grade

| Want | Effect | Match name |
| --- | --- | --- |
| The grade, everything | **Lumetri Color** | `AE.ADBE Lumetri` |
| Quick exposure/contrast | Brightness & Contrast | `AE.ADBE Brightness & Contrast 2` |
| Black and white | Black & White | `AE.ADBE Black & White` |
| Tint to a colour | Tint | `AE.ADBE Tint` |
| Levels / curves by numbers | Levels | `PR.ADBE Levels` |
| Gamma only | Gamma Correction | `PR.ADBE Gamma Correction` |
| Broadcast-legal clamp (QC) | Video Limiter | `AE.ADBE DigitalVideoLimiter` |
| Colour-grade interchange | ASC CDL | `AE.ADBE AEASCCDL` |
| Log → linear | Cineon Converter | `AE.ADBE Cineon Converter` |
| Isolate one colour, rest mono | Color Pass | `PR.ADBE Color Pass` |
| Swap one colour for another | Color Replace | `PR.ADBE Color Replace` |
| Video-scope-style trim | ProcAmp | `AE.ADBE ProcAmp` |
| Invert | Invert | `AE.ADBE Invert` |
| Posterize | Posterize | `AE.ADBE Posterize` |

Lumetri's readable parameter indices are tabulated in [`api-notes.md`](./api-notes.md) — Exposure is
19, Contrast 20, Saturation 16, Temperature 14. **33 of its 130 params cannot be read by any route**
but can still be written.

### The BadCode near-black register

The look is near-black, one thin light, monumental. These are the tools that get there.

| Want | Effect | Match name |
| --- | --- | --- |
| **Vignette** — darken the edges | Vignette | `AE.Impact_Vignette_FX` |
| **Grain** | Noise | `AE.ADBE_Noise_FX` (legacy: `AE.ADBE Noise2`) |
| **God rays / shafts of light** | Volumetric Rays | `AE.Impact_Volumetric_Rays_FX` |
| Light leaks across the frame | Light Leaks | `AE.Impact_Light_Leaks_FX` |
| Bloom on highlights | Wonder Glow · Echo Glow · Edge Glow | `AE.Impact_Wonder_Glow_FX` · `AE.Impact_Echo_Glow_FX` · `AE.Impact_Edge_Glow_FX` |
| Anamorphic-ish sparkle | Glint | `AE.Impact_Glint_FX` |
| Directional lighting on the frame | Lighting Effects | `AE.ADBE LightingEffect` |
| Gradient / ramp overlay | Gradient · Ramp | `AE.Impact_Gradient_FX` · `AE.ADBE Ramp` |
| Long cast shadow (graphic) | Long Shadow | `AE.Impact_Long_Shadow_FX` |

### Glitch, decay, "the transmission is failing"

The register for anything that is *received wisdom from a broken future*.

| Want | Effect | Match name |
| --- | --- | --- |
| **Chromatic split** | RGB Split | `AE.Impact_RGB_Split_FX` |
| Digital corruption | VR Digital Glitch | `AE.Mettle SkyBox Digital Glitch` |
| Chromatic aberration | VR Chromatic Aberrations | `AE.Mettle SkyBox Chromatic Aberrations` |
| Strobe / flicker | Strobe Light | `AE.ADBE Strobe` |
| Frame-rate stutter | Posterize Time | `AE.ADBE Posterize Time` |
| Blocky censor / pixelate | Mosaic | `AE.Impact_Mosaic_FX` |
| Heat haze, melt, warp | Turbulent Displace | `AE.ADBE Turbulent Displace` |
| Wave distortion | Wave Warp | `AE.ADBE Wave Warp` |
| Lens barrel/pincushion | Lens Distortion | `PR.ADBE Lens Distortion` |
| Rough up the edges | Roughen Edges | `AE.ADBE Roughen Edges` |
| Line-art / find-edges look | Find Edges | `AE.ADBE Find Edges` |
| Emboss | Color Emboss | `AE.ADBE Color Emboss` |

**For a full VHS/analogue decay, reach for the transition `AE.AE_Impact_VHS_Damage` or `AE.AE_Impact_Phosphore`**
rather than stacking effects — they are purpose-built and free.

### Blur and focus

| Want | Effect | Match name |
| --- | --- | --- |
| Plain blur, **clean params** | **Gaussian Blur (Legacy)** | `AE.ADBE Gaussian Blur 2` |
| Plain blur, modern | Gaussian Blur | `AE.Impact_Blur_FX` |
| Motion streak | Directional Blur | `AE.Impact_Directional_Blur_FX` |
| Shallow depth of field | Bokeh Blur · Focus Blur | `AE.Impact_Bokeh_Blur_FX` · `AE.Impact_Focus_Blur_FX` |
| Lens-style defocus | Camera Blur | `AE.ADBE Camera Blur` |
| Blur driven by another layer | Compound Blur | `AE.Impact_Compound_Blur_FX` |
| Per-channel blur | Channel Blur | `AE.Impact_Channel_Blur_FX` |
| Sharpen | Sharpen · Unsharp Mask | `AE.ADBE Sharpen` · `AE.ADBE Unsharp Mask` |

🔴 **Prefer the legacy Gaussian Blur for automation.** `AE.Impact_Blur_FX` has 20 params, most of
them internal (`Error occurred`, `_ Sequence Width`, three with blank names) and its real control is
index 5 "Amount". `AE.ADBE Gaussian Blur 2` has three clean params: `0 Blurriness` (defaults to
**25**, not 0), `1 Blur Dimensions`, `2` (Repeat Edge Pixels). Full write-up in `api-notes.md`.

### Movement, framing, stabilisation

| Want | Effect | Match name |
| --- | --- | --- |
| **Push in / pan / reframe** | *the intrinsic* **Motion** | `AE.ADBE Motion` — always component 1 |
| Transform **with motion blur** | Transform | `AE.ADBE Geometry2` |
| Reframe for another aspect | Auto Reframe | `AE.ADBE AEFilterAutoFramer` |
| De-shake a handheld shot | Warp Stabilizer | `AE.ADBE SubspaceStabilizer` |
| **Add** shake deliberately | Camera Shake | `AE.Impact_Camera_Shake_FX` |
| Organic drift | Wiggle | `AE.Impact_Wiggle_FX` |
| Spin | Spin · 3D Rotate | `AE.Impact_Spin_FX` · `AE.Impact_Rotate_FX` |
| Fake 3D card | Basic 3D | `AE.ADBE Basic 3D` |
| Corner-pin onto a screen | Corner Pin | `AE.ADBE Corner Pin` |
| Crop to a frame | Crop · Rounded Crop | `AE.ADBE AECrop` · `AE.Impact_Crop_FX` |
| Mirror / kaleidoscope | Mirror · Replicate | `AE.ADBE Mirror` · `AE.ADBE Replicate` |
| Flip | Horizontal Flip · Vertical Flip | `AE.ADBE Horizontal Flip` · `AE.ADBE Vertical Flip` |
| Magnify a region | Magnify | `AE.Impact_Magnifier_FX` |

**Motion is the workhorse.** It is on every clip already, needs no `apply_effect`, and its params
are: `0 Position` · `1 Scale` · `2 Scale Width` · `3` (Uniform Scale, named `" "`) · `4 Rotation` ·
`5 Anchor Point` · `6 Anti-flicker` · `7–10 Crop L/T/R/B`. Position and Anchor Point are
**0–1 fractions of the frame**, not pixels — `{x: 0.5, y: 0.5}` is centre.

### Compositing and keying — how Flow elements get in

**This is the house route for fire, smoke, sparks and weather.** Generate the element in Flow
against a black background, then composite it on a track above.

| Want | Effect | Match name |
| --- | --- | --- |
| Key out a green screen | **Ultra Key** | `AE.ADBE Ultra Key` |
| Key out pure black/white | Luma Key | `AE.ADBE Legacy Key Luma` |
| Key out one colour | Color Key | `AE.ADBE Color Key` |
| Use another track as a matte | Track Matte Key | `AE.ADBE Legacy Key Track Matte` |
| Crush blacks to transparent | Extract | `PR.ADBE Extract` |
| Adjust the alpha | Alpha Adjust | `AE.ADBE Alpha Adjust` |
| Glow on the alpha edge | Alpha Glow | `AE.ADBE Alpha Glow` |
| Soften a matte edge | Edge Feather | `AE.ADBE Edge Feather` |
| Drop shadow | Drop Shadow | `AE.ADBE Drop Shadow` |

⚠️ **Blend modes are NOT an effect.** They live on the **Opacity intrinsic** (component 0) — it has
two params both named `Blend Mode`, at indices 1 and 2, and the API exposes **no way to enumerate
the options**. A probe on 2026-08-21 confirmed no `getOptions`/`getEnumValues`/range accessor of any
kind. **The integer for Screen has not been measured yet** — see Open questions below. Until it is,
key with **Luma Key** or **Extract** rather than blending, both of which are ordinary effects and
fully addressable.

### Text and graphics without a MOGRT

| Want | Effect | Match name |
| --- | --- | --- |
| **A text overlay, no template needed** | **Simple Text** | `AE.ADBE PPro SimpleText` |
| Outline a shape | Stroke | `AE.Impact_Stroke_FX` |
| Solid colour gradient fill | 4-Color Gradient | `AE.ADBE 4ColorGradient` |
| Burn in timecode / metadata | Metadata & Timecode Burn-in | `AE.ADBE PPro Metadata` |
| Cut a logo out of the frame | Logo Cutout | `AE.Impact_Alpha_FX` |
| Layout spacing helper | Spacer | `AE.Impact_Spacer_FX` |

🟢 **`AE.ADBE PPro SimpleText` is the find worth knowing.** The research sweep flagged
"MOGRT parameter automation via UXP" as an unresolved blocker for template-driven titles. For
*plain* titles it is moot: Simple Text is an ordinary effect, so it goes on through
`premiere_apply_effect` and its params set through `premiere_set_param` like anything else. Its
parameter list has not been dumped yet — do that with `premiere_describe_effect` the first time you
need it, and record it here.

### VR / 360

`AE.Mettle SkyBox *` — Blur, Chromatic Aberrations, Color Gradients, De-Noise, Digital Glitch,
Fractal Noise, Glow, Plane to Sphere, Rotate Sphere, Sharpen, plus `AE.ADBE VR Projection`. Built
for 360 footage, **but several are useful on flat footage anyway** — Digital Glitch and Chromatic
Aberrations especially, and `Fractal Noise` is a free procedural texture generator.

---

## Transitions

118 of them. Two things to know before using any:

- **Match names mix prefixes in the same catalogue** — `ADBE Additive Dissolve`,
  `AE.ADBE Cross Dissolve New`, `AE.AE_Impact_Glitch`. There is no pattern to rely on. List first.
- **There are no display names on the transition API at all.** `getVideoTransitionMatchNames()`
  returns match names only; the friendly name (`Cross Dissolve (Legacy)`) exists in the project file
  and nowhere the API will show you.

### The ones you will actually use

| Want | Match name |
| --- | --- |
| **Cross dissolve** | `AE.ADBE Cross Dissolve New` |
| **Dip to black** | `AE.ADBE Dip To Black` |
| Dip to white | `AE.ADBE Dip To White` |
| Additive (brighter) dissolve | `ADBE Additive Dissolve` |
| Film dissolve | `ADBE Film Dissolve` |
| Invisible cut on a talking head | `AE.ADBE MorphCut` |

### The absorbed Film Impact set — free since Premiere 25.5

`AE.AE_Impact_*`, and it is the most useful family here. Adobe bought them in; they cost nothing.

| Register | Match names |
| --- | --- |
| **Glitch / decay** | `AE.AE_Impact_Glitch` · `AE.AE_Impact_VHS_Damage` · `AE.AE_Impact_Chroma_Leaks` · `AE.AE_Impact_Phosphore` · `AE.AE_Impact_TV_Power` · `AE.AE_Impact_Flicker` |
| **Impact / energy** (cuts to a beat) | `AE.AE_Impact_Flash` · `AE.AE_Impact_Pop` · `AE.AE_Impact_Earthquake` · `AE.AE_Impact_Zoom_Blur` · `AE.AE_Impact_Whip` · `AE.AE_Impact_Spring` |
| **Light** | `AE.AE_Impact_Light_Leaks` · `AE.AE_Impact_Flare` · `AE.AE_Impact_Glow` · `AE.AE_Impact_Light_Sweep` · `AE.AE_Impact_Rays` · `AE.AE_Impact_Burn_White` |
| **Blur-based dissolves** | `AE.AE_Impact_Blur_dissolve` · `AE.AE_Impact_Lens_Blur` · `AE.AE_Impact_Directional_Blur` · `AE.AE_Impact_Radial_Blur` · `AE.AE_Impact_Blur_To_Color` |
| **Luma / shape** | `AE.AE_Impact_Luma_Fade` · `AE.AE_Impact_Shape_Dissolve` · `AE.AE_Impact_Shape_Flow` · `AE.AE_Impact_Burn_Alpha` |
| **Type** | `AE.AE_Impact_Typewriter` · `AE.AE_Impact_Text_Animator` |
| **3D / physical** | `AE.AE_Impact_3D_Flip` · `AE.AE_Impact_3D_Roll` · `AE.AE_Impact_3D_Blinds` · `AE.AE_Impact_Fold` · `AE.AE_Impact_Page_Peel` · `AE.AE_Impact_Film_Roll` · `AE.AE_Custom_Impact_Fall` · `AE.AE_Custom_Impact_Spinback_3D` |
| **Distortion** | `AE.AE_Impact_Liquid_Distortion` · `AE.AE_Impact_Warp` · `AE.AE_Impact_Wave` · `AE.AE_Impact_Glass` · `AE.AE_Impact_Kaleido` · `AE.AE_Impact_Mirror` · `AE.AE_Impact_Chaos` · `AE.AE_Impact_Grunge` |

**`AE.AE_Impact_Luma_Fade` and `AE.AE_Impact_Flash` are the two to try first for BadCode** — a luma
fade reads as the image dissolving into the black rather than crossing into another shot, which is
the register; a flash is the cheapest way to make a cut land on a beat.

### Everything else

Classic wipes and geometric transitions, all present, none of them BadCode's register:
Band Slide/Wipe · Barn Doors · Center Split · Checker Wipe · CheckerBoard · Clock Wipe · Cross Zoom
· Inset · Iris Cross/Diamond/Round/Square · Non-Additive Dissolve · Page Turn · Paint Splatter ·
Pinwheel · Push · Radial Wipe · Random Blocks · Random Wipe · Slide · Spiral Boxes · Split ·
Venetian Blinds · Wedge Wipe · Wipe · Zig-Zag Blocks · Whip, plus the `AE.Mettle SkyBox` 360 set.

---

## What is NOT here, and the free route instead

| Not installed | What we do instead |
| --- | --- |
| Fire, smoke, sparks, explosions (Sapphire, ActionVFX) | **Generate in Flow on a black background**, key with Luma Key / Extract on a track above |
| Particle systems (Trapcode) | Flow, same route |
| True 3D extruded text (Element 3D) | Flow for the render; Simple Text or a MOGRT for flat type |
| Planar tracking (Mocha Pro) | Corner Pin by hand, or reshoot the plate in Flow |
| Film emulation LUTs (Dehancer, FilmConvert) | Lumetri's built-in Looks + `Input LUT`, or an ffmpeg LUT pass |
| Advanced denoise (Neat Video) | `AE.Mettle SkyBox Denoise`, or ffmpeg `hqdn3d`/`nlmeans` |
| Optical-flow retime (Twixtor) | Premiere's own Time Interpolation, or ffmpeg `minterpolate` |

There is **no After Effects on this machine**, so anything that genuinely needs AE is out of scope
and should be flagged as such rather than worked around.

---

## Audio

**There is no audio transition API whatsoever** — no `AudioTransition` type anywhere in the 4,675
lines of declarations. `premiere_add_transition` is video-only and enforces it at the schema.
**Audio crossfades must be done by hand in the timeline.**

Audio *effects* do work through the same tools. Every audio clip carries two intrinsics:

| # | matchName | displayName | Params |
| --- | --- | --- | --- |
| 0 | `Internal Volume Stereo` | Volume | `0 Mute` (bool) · `1 Level` |
| 1 | `Internal Channel Volume Stereo` | Channel Volume | `0 Bypass` · `1 Left` · `2 Right` · `3–32` blank |

🔴 **`Level` is a linear multiplier, not decibels.** 0.1778 ≈ −15 dB. Convert before quoting a
number at a human.

🔴 **Audio effect match names are bare GUIDs.** Jack's Hard Limiter is
`e0b23f05-f1a7-4ef7-9b50-7ec3e3002058`. The `PR.ADBE` / `AE.ADBE` prefix convention does not apply to
audio at all — list, never guess.

---

## Open questions — answer these live and record the answer here

| Question | Why it matters | How to settle it |
| --- | --- | --- |
| **Which integer is Screen** on Opacity's Blend Mode param? | It is the one-call route for compositing Flow fire/smoke | Build a probe sequence, bright clip over dark, sweep the value and export a frame per step. **Do this in a scratch project, never a real one** |
| Which of Opacity's **two** `Blend Mode` params is the live one (index 1 = 18, index 2 = 0)? | Same | Same sweep |
| `AE.ADBE PPro SimpleText` parameter list | Titles with no MOGRT | `apply_effect` on a scratch clip, then `premiere_describe_effect` |
| Can a **MOGRT's** Essential Graphics params be read/set? | Template-driven maps, charts, kinetic type | T11 — `premiere_eval` on an inserted MOGRT |
| `AE.Impact_Vignette_FX` and `AE.ADBE_Noise_FX` param indices | The two most BadCode effects there are | `describe_effect` once, record here |

---

*Harvested 2026-08-21 from Premiere Pro 26.3.2. Re-run `premiere_list_effects` and
`premiere_list_transitions` after any Premiere update — the counts here (106 / 118) are the
check.*
