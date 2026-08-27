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

> **🔴 This is HALF the answer. Its twin is [`../video-fx/ffmpeg-catalogue.md`](../video-fx/ffmpeg-catalogue.md)**
> — 319 video filters and the 133-plugin frei0r shelf. Ruled 2026-08-26 (Kai): asked what effects
> we have, **list both, never one.** And eight things live only there — most importantly
> **text**, because Premiere's API cannot write a string at all (see § *Text and graphics*).

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

🔴 **`AE.ADBE PPro SimpleText` cannot be given its words. Measured 2026-08-22, confirmed with
pixels.** It was previously recorded here as the route to a title without a template. It is not.

| Index | Param | Default | Writable? |
| --- | --- | --- | --- |
| 0 | *(blank)* | false | — |
| 1 | Position | `[0.5, 0.88]` | ✅ |
| 2 | Justification | 1 | ✅ |
| 3 | Size | 40 | ✅ **verified** |
| 4 | Opacity | 40 | ✅ **verified** |
| 5 | `" "` — **the text itself** | *unreadable* | 🔴 **NO** — `Illegal Parameter type` |

Writing Size 120 and Opacity 100 landed. Writing the string threw, and the exported frame still
read **"Default Text"** in 120pt at full opacity — the styling took, the words did not.

**So a title is handwork.** Apply and position Simple Text from here if you like, then say *"type
the words into the Effect Controls panel"*. Or place a MOGRT and hand over the same way — see
[`mogrt-catalogue.md`](mogrt-catalogue.md). This is the `premiere-automation` skill §8 case, and
per Kai's ruling of 2026-08-21 it is a fine answer, not a gap to engineer around.

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

## Blend modes — measured, 2026-08-22

**Settled live.** A three-band plate (RGB 64 / 128 / 192) on V1 under a solid 128 grey on V2, every
integer swept, a frame exported per step, luma measured per band with `ffmpeg signalstats`.

### 🔴 `AE.ADBE Opacity` param **1** is the live Blend Mode. Param **2** does nothing.

With param 1 pinned to Multiply, param 2 was set to 1, 5, 10 and 22 and the rendered frame was
**byte-identical every time** (43/71/99). A separate 20-value sweep of param 2 also never changed
the picture. **Always write index 1.**

### The integers

Identified where the arithmetic matches exactly. Predicted values are in encoded Y (limited range),
which is what `signalstats` reports.

| Integer | Mode | Measured Y (64/128/192 band) |
| --- | --- | --- |
| 1 | Color Burn | 16 / 18 / 128 |
| 2 | Color Dodge | 127 / 235 / 235 |
| 5 | Difference | 71 / 16 / 71 |
| 9 | Hard Mix | 16 / 235 / 235 |
| 13 | Linear Burn | 16 / 17 / 72 |
| **14** | **Linear Dodge (Add)** | 181 / 235 / 235 |
| **17** | **Multiply** | 43 / 71 / 99 |
| **18** | **Normal** *(the default)* | 126 / 126 / 126 |
| **22** | **Screen** | 153 / 181 / 208 |
| 25 | Subtract | 16 / 16 / 71 |
| 3 or 4 | Darken *(both render identically here)* | 71 / 126 / 126 |
| 11 or 12 | Lighten *(both render identically here)* | 126 / 126 / 181 |

**22 (Screen) and 14 (Add) are the ones that matter** — they are the one-call route for
compositing a Flow element shot on black. Recipe:
[`recipes.md`](recipes.md) § *Fire, smoke, sparks*.

⚠️ **What this plate could not separate.** The test overlay is 50% grey and the plate is greyscale,
so every mode that is neutral at 50% (Soft Light, Vivid Light, Linear Light, Pin Light) and every
mode that needs colour (Hue, Saturation, Color, Luminosity) rendered as the base untouched —
values 0, 8, 10, 15, 19, 20, 21, 23, 24, 27 all read 71/126/181. Values 6, 7 and 16 rendered
identically to Normal. **Distinguishing those needs a colour plate and a non-50% overlay.**

---

## Parameter indices, measured 2026-08-22

### 🔴 Every Impact effect shares a boilerplate, and the real controls start at index 4

`0 Error occurred` · `1 Controls` · `2 ""` · `3 Seed` — then the actual controls — then a trailing
block of `_ Overlay Mode`, `_ Overlay Info`, `_ Applied Version`, `_ Sequence Width/Height/Pixel
Ratio`. **Anything prefixed `_` is internal; leave it alone.** This is why Vignette reports 27
params and has 13 you would ever touch.

### Vignette — `AE.Impact_Vignette_FX` (27 params)

| Index | Param | Default |
| --- | --- | --- |
| 4 | **Vignette** *(the amount)* | 100 |
| 5 | Width | 80 |
| 6 | Height | 80 |
| 7 | Scale | 100 |
| 8 | Angle | 0 |
| 9 | Center | `[0.5, 0.5]` |
| 10 | Roundness | 100 |
| 11 | Feather | 50 |
| 12 | Color | 🔴 unreadable (writable) |
| 13 | Softness | 20 |
| 14 | Chromatic Aberration | 20 |
| 15 | Opacity | 100 |
| 16 | Master | 100 |

### Noise — `AE.ADBE_Noise_FX` (23 params)

| Index | Param | Default |
| --- | --- | --- |
| 3 | Seed | 0 |
| 4 | **Intensity** | 50 |
| 5 | Shadows | 75 |
| 6 | Midtones | 75 |
| 7 | Highlights | 75 |
| 8 | Uniform Intensity | true |
| 9 | Saturation | 50 |
| 10 | Blend Mode | 4 |
| 11 | Master | 100 |
| 12 | Preserve Alpha | true |

🟢 **Separate Shadows / Midtones / Highlights is the BadCode control.** Grain only in the shadows
is exactly the near-black register — and it is also the banding defence before upload
([`docs/video-fx/delivery.md`](../video-fx/delivery.md)).

### RGB Split — `AE.Impact_RGB_Split_FX` (24 params)

| Index | Param | Default |
| --- | --- | --- |
| 4 | **Horizontal Split** | 1 |
| 5 | Vertical Split | 0 |
| 6 | Depth Split | 0 |
| 7 | Vertigo | 0 |
| 8 | Channel Shift | 0 |
| 9 | Feather | 0 |
| 10 | Position | `[0.5, 0.5]` |
| 11 | Lightness | 0 |
| 12 | Softness | 0 |
| 13 | Edge Behavior | 0 |

### Volumetric Rays — `AE.Impact_Volumetric_Rays_FX` (32 params)

| Index | Param | Default |
| --- | --- | --- |
| 4 | **Intensity** | 60 |
| 5 | Highlights Only | 60 |
| 6 | Ray Length | 75 |
| 7 | **Light Position** | `[0.5, 0.25]` |
| 8 | Softness | 10 |
| 9 | Edge Rays | 0 |
| 10 | Volumetric Fog | 25 |
| 11 | Fog Size | 50 |
| 12 | Fog Speed | 20 |
| 13 | Caustics | 0 |
| 14 | Caustics Speed | 50 |
| 15 | Color | 🔴 unreadable (writable) |
| 16 | Colorize | 0 |
| 17 | Vibrance | 20 |
| 18 | Desaturate | 0 |
| 19 | Chromatic Aberration | 20 |
| 20 | Blend Mode | 1 |
| 21 | Source Opacity | 100 |

🟢 **`Light Position` (index 7) plus `Highlights Only` is the one thin light** — the BadCode
register in two parameters.

---

### Strobe Light — `AE.ADBE Strobe` (8 params) · measured 2026-08-24

| Index | Param | Default |
| --- | --- | --- |
| 0 | Strobe Color | 🔴 unreadable (writable) — **defaults to WHITE** |
| 1 | Blend With Original | 0 |
| 2 | **Strobe Duration (secs)** | 0.5 |
| 3 | **Strobe Period (secs)** | 1 |
| 4 | Random Strobe Probablity | 0 |
| 5 | **Strobe** (mode) | 0 |
| 6 | Strobe Operator | 0 |
| 7 | Random Seed | 0 |

🔴 **Mode `1` ("Makes Layer Transparent") does not render at all** — verified byte-identical to
baseline across a full period. **Mode `0` replaces the whole frame with Strobe Color.**

🟢 **Flicker-to-black is mode 0 with Strobe Color set to black** — one effect instead of hand
cutting, and the house alternative to slicing a track into 4-frame pieces:

```
params: { "0": {r:0,g:0,b:0}, "2": 0.04, "3": 0.2, "5": 0 }   // 1 frame black in every 5 @ 25fps
```

🔴 **Duration >= period disables it.** Duration 0.2 with period 0.2 renders as no effect at all.
Full write-up in [`api-notes.md`](api-notes.md).

## Open questions — answer these live and record the answer here

| Question | Why it matters | How to settle it |
| --- | --- | --- |
| Which integers are Soft Light, Overlay, Hue, Saturation, Color, Luminosity? | Completeness; none is load-bearing | Re-sweep with a **colour** plate and an overlay that is not 50% grey |
| Is 3 or 4 Darken, 11 or 12 Lighten? | Cosmetic | Same colour re-sweep |
| ~~Can a **MOGRT's** params be written?~~ | **ANSWERED 2026-08-22.** Placement, position, scale, rotation and opacity: **yes**. The text itself: **no** — `Illegal Parameter type`. [`api-notes.md`](api-notes.md) | T11 — closed |

---

*Harvested 2026-08-21 from Premiere Pro 26.3.2. Re-run `premiere_list_effects` and
`premiere_list_transitions` after any Premiere update — the counts here (106 / 118) are the
check.*

### Echo Glow — `AE.Impact_Echo_Glow_FX` (35 params) · measured 2026-08-24

| Index | Param | Default |
| --- | --- | --- |
| 4 | **Anchor** | `[0.5, 0.5]` |
| 5 | **Steps** | 8 |
| 6 | **Intensity** | 80 |
| 7 | Highlights Only | 60 |
| 8 | **Range** | 75 |
| 10 | **Speed** | 5 |
| 12 | Outline | 50 |
| 13 | Falloff | 25 |
| 15 | Color | 🔴 unreadable (writable) |
| 21 | Chromatic Aberration | 10 |
| 23 | Source Opacity | 100 |

🟢 **Anchor + Range + Speed are the three that matter.** Unlike Volumetric Rays it **animates on
its own** (Speed 5 by default), so a held shot gains motion with no keyframing — which is why it
beat Rays on the camping music video's stage plate.

🔴 **At defaults, Wonder Glow, Glint and Mirror are near-invisible** on a bright plate (measured
same session). Echo Glow is the one of that family that reads immediately.

### VR Digital Glitch — `AE.Mettle SkyBox Digital Glitch` (38 params) · measured 2026-08-24

🔴 **Indices 0–6 are 360/VR plumbing, not the look** (Frame Layout, Field of View, Point of
Interest). On flat footage, leave them.

| Index | Param | Default |
| --- | --- | --- |
| 7 | **Master Amplitude** | 100 — the single "how much" dial |
| 9 | **Color Distortion** | 50 |
| 10 | **Geometry Distortion X** | 50 |
| 11 / 12 | Geometry Distortion Y / Z | 0 |
| 13 | Distortion Complexity | 40 |
| 14 | Distortion Rate | 50 |
| 15 / 16 | Distortion / Color Evolution | 0 |
| 26 | Sub Influence | 95 |
| 31 | Noise Strength | 0 |
| 37 | Random Seed | 0 |

🟢 **Master Amplitude (7) scales the whole effect** — one number from destroyed to a hint.

🔴 **Random Seed (37) defaults to 0 on every clip**, so two glitched clips corrupt *identically*.
Vary it per clip.

### Camera Shake — `AE.Impact_Camera_Shake_FX` (47 params) · measured 2026-08-25

🔴 **This one breaks the Impact index-4 rule.** The real controls start at **7**, and there is a
second boilerplate block in the middle (indices 32–38) as well as the usual tail.

| Index | Param | Default | What it does |
| --- | --- | --- | --- |
| 3 | Scale | 50 | Prescale — only live if `Apply Prescale` (2) is on |
| 7 | Seed | 0 | Reroll the shake pattern |
| 9 | Camera Mode | 1 | — |
| 10–24 | Strafe / Stride / Roll ×5 | varies | ⚠️ **Five unlabelled triplets** — see below |
| 25 | Lean (deg) | 0 | — |
| 26 | **Variation** | 20 | How irregular the motion is |
| 27 | **Stabilize** | 25 | Pulls back to centre; higher = less drift |
| 28 | **Speed** | 100 | Frequency — judder vs sway |
| 29 | **Auto Scale** | `true` | Scales up to hide edges |
| 30 | **Master** | 100 | Global amount |
| 31 | Edge Behavior | 0 | Only matters with Auto Scale off |
| 34 | Enable Motion Blur | `true` | — |
| 35 | **Motion Blur** | 20 | Strong at default on an already-blurred source |

🔴 **Strafe / Stride / Roll appear FIVE times (10–24) and the API cannot tell them apart.** The
group labels Premiere shows in the UI are the blank-named params, so all five triplets read
identically over the bridge. **Which is amplitude and which is frequency is unproven.** Drive it
from **Master (30)** and **Speed (28)** instead, unless someone maps the triplets by hand in the GUI
and records the answer here.

🟢 **Leave Auto Scale (29) on.** Measured live on a 1.16s close-up at full defaults: no black edges
at any sampled frame despite large displacement. It costs a slight crop in — which is worth knowing
if the shot has to match framing with untreated neighbours.

🟢 **It animates on its own**, like Echo Glow and unlike Volumetric Rays — no keyframing needed for
a held shot. Verified across two frames 0.4s apart: framing and blur both changed.

⚠️ **Defaults are strong.** On a plate that already carries motion blur they compound. For a hit
rather than a handheld wander: Master ~70, Speed ~160, Stabilize ~40, Motion Blur ~12.
