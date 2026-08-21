# ffmpeg colour: LUTs, curves, grain, film emulation, black-and-white

## What this covers

Colour-and-texture, end to end: 3D/1D LUTs (`.cube`), tone curves, shadow/mid/highlight balance,
channel mixing (mono/sepia), levels, white-balance by Kelvin, brightness/contrast/gamma/
saturation, hue, procedural and overlay film grain, a halation/bloom approximation, vignette,
HDR tonemapping, and the range/gamma tagging traps at the ffmpeg↔Premiere boundary.
`post-production.md` never touches colour — its scope is framing and timing (§§3.1–3.9) — so
this brief is additive, not overlapping.

## What's possible

| Need | Tool/route | How | Cost |
| --- | --- | --- | --- |
| Graded look from a `.cube` | `lut3d` | `lut3d=file=look.cube:interp=tetrahedral` | free |
| Look baked as an image | `haldclut` | `[0][1]haldclut`, 2nd input is the Hald PNG/video | free |
| 1D LUT | `lut1d` | `lut1d=file=look.cube` (also `.csp`) | free |
| Hand-tuned tone curve / vintage | `curves` | `curves=preset=vintage` or custom points | free |
| Shadow/mid/highlight colour cast | `colorbalance` | `rs=-.15:bs=.2:rh=.15:bh=-.1` | free |
| True-luma monochrome | `colorchannelmixer` | `.3:.4:.3:0:...` (docs' own recipe) | free |
| Fast monochrome | `hue` | `hue=s=0` | free |
| Sepia | `colorchannelmixer` | documented sepia coefficients | free |
| Black/white point levels | `colorlevels` | `rimin=.04:...:rimax=.96:...` | free |
| Warm/cool by Kelvin | `colortemperature` | `temperature=5000:mix=.5` | free |
| Brightness/contrast/sat/gamma | `eq` | `contrast=1.1:saturation=.85:gamma=1.05` | free |
| Procedural 35mm grain | `noise` | `alls=12:allf=t+u` | free |
| Real scan-texture grain | plate + `blend`/`overlay` | screen-blend a 4K grain clip over footage | free plates; paid packs |
| Grain, no plate file | `geq` | per-pixel expression with `random(1)` | free |
| Halation / bloom | `gblur` + `blend` | bright-pass → blur → `blend=screen` | free |
| Lens vignette | `vignette` | `angle=PI/4` (`mode=backward` to lift) | free |
| Tonemap HDR to SDR | `zscale`+`tonemap`+`zscale` | linearise → `tonemap=hable` → re-tag bt709 | free |
| Fix washed-out Premiere round-trip | explicit colour tags | `-color_range tv -color_primaries bt709 ...` | free |
| Whole film-stock emulation | Dehancer / FilmConvert | install plugin, pick stock | $, see Named tools |

## Named tools

### `lut3d` / `lut1d` / `haldclut`
Apply a pre-computed colour transform. `lut3d` reads `.cube`/`.3dl`/`.dat`/`.m3d`/`.csp`; `lut1d`
reads `.cube`/`.csp`; `haldclut` takes the LUT as a second video/image input instead of a file.
Free, ffmpeg core, confirmed present, stable for years — the standard `.cube` consumer in the
grading-tooling ecosystem. [ffmpeg.org §11.153–11.154, §11.117]

### `curves`
Photoshop/GIMP-style per-channel tone curve (natural-cubic or PCHIP spline). 11 presets: `none,
color_negative, cross_process, darker, increase_contrast, lighter, linear_contrast,
medium_contrast, negative, strong_contrast, vintage`; also imports a Photoshop `.acv` file. Free,
ffmpeg core. [ffmpeg.org §11.50]

### `colorbalance` / `colorchannelmixer` / `colorlevels` / `colortemperature`
Four grading primitives, all free ffmpeg core, all confirmed present. `colorbalance`: red-cyan/
green-magenta/blue-yellow per shadow/mid/highlight. `colorchannelmixer`: remixes each output
channel as a weighted R/G/B/A sum — the documented route to true-luma monochrome and sepia.
`colorlevels`: per-channel black/white points (Photoshop Levels). `colortemperature`: white
balance in Kelvin (1000–40000). [ffmpeg.org §11.28/31/36/40, 2026-08-21]

### `eq` / `hue`
`eq`: brightness/contrast/saturation/gamma in one pass, plus a highlight-protecting
gamma_weight. `hue`: rotates hue, scales saturation (`s=0` = fast monochrome via internal luma,
distinct from `colorchannelmixer`'s documented weights). Free, core. [ffmpeg.org §11.82, §11.130]

### `noise` / `geq` (procedural grain)
`noise`: seeded per-pixel noise, strength 0–100, flags for averaged/patterned/temporal/uniform.
`geq`: arbitrary per-pixel expression — grain from nothing, no plate file, slower, hand-tuned.
Both free, core. [ffmpeg.org §11.181, §11.111]

### Overlay grain plates (paid and free)
Real scanned-film grain as a video plate, composited with `overlay`/`blend`. Free: tdcat.com's
DCI 4K ProRes 422 plates (8/16/35mm); Pixabay's royalty-free 4K library. [tdcat.com, pixabay.com]

### Dehancer Film (Premiere/AE plugin)
Film-stock emulation bundling grain/halation/bloom/vignette/defringe as one effect. Seen
2026-08-21: subscription $12–99/mo by tier; perpetual "Pro" $449; cut-down "Lite" perpetual $199.
[dehancer.com/pricing, dehancer.com/shop/aepr/pro]. Reviewed as the more "authentic scan" option
vs FilmConvert [theotivity.com] — not verified here.

### FilmConvert Nitrate (Premiere/AE/Resolve/FCP plugin)
Film-stock emulation keyed to the shooting camera. Seen 2026-08-21: $149 perpetual (one-time);
Black Friday 2025 was $89; Pro-owner upgrade $29. [filmconvert.com/nitrate, filmconvert.com/
purchase, 4kshooters.net 2025-11-28]

### Premiere native: "Noise & Grain" effect
Premiere's built-in grain effect, named exactly **"Noise & Grain"** in Adobe's reference (dated
2025-08-22) — "adds random pixels... simulating the look of older cameras." This is the effect
the UXP bridge needs a match name for; Adobe documents the feature, not the internal string.
[helpx.adobe.com/premiere/.../noise-and-grain-effects.html]

### Premiere native: Lumetri Color "Input LUT"
Basic Correction's **Input LUT**: "select a preset LUT, or a custom LUT that you saved" — the
documented GUI path for a `.cube` in Premiere. No published match name for setting it directly.
[helpx.adobe.com/premiere-pro/using/color-workflows.html]

## Automation hook

**Premiere side.** Neither "Noise & Grain" nor Lumetri's "Input LUT" has a published match name
(Adobe documents the feature, not the UXP/ExtendScript string). Discovery step: call
`VideoFilterFactory.getMatchNames()`, filter for `'Noise'`, `'Grain'`, `'Lumetri'`. A historic
ExtendScript-era name for the old grain tool was `AE.ADBE Noise HLS` [Premiere v12 docs —
unverified against 26.3.2, flag stale]; the current effects' names weren't found anywhere
public, so the discovery step above is the source of truth here, not this brief.

**ffmpeg side** — every skeleton ran against a synthetic near-black test still/clip in the
scratchpad (not real Flow footage), confirmed error-free:

```bash
# TESTED curves
ffmpeg -i in.png -vf "curves=preset=vintage" out.png

# TESTED colorbalance
ffmpeg -i in.png -vf "colorbalance=rs=-.15:bs=.2:rh=.15:bh=-.1" out.png

# TESTED colorchannelmixer (monochrome, documented weights)
ffmpeg -i in.png -vf "colorchannelmixer=.3:.4:.3:0:.3:.4:.3:0:.3:.4:.3" out.png

# TESTED colorlevels
ffmpeg -i in.png -vf "colorlevels=rimin=.039:gimin=.039:bimin=.039:rimax=.96:gimax=.96:bimax=.96" out.png

# TESTED colortemperature
ffmpeg -i in.png -vf "colortemperature=temperature=5000:mix=.5" out.png

# TESTED eq
ffmpeg -i in.png -vf "eq=contrast=1.1:saturation=.85:gamma=1.05" out.png

# TESTED hue (fast monochrome)
ffmpeg -i in.png -vf "hue=s=0" out.png

# TESTED lut3d
ffmpeg -i in.png -vf "lut3d=file=look.cube:interp=tetrahedral" out.png

# TESTED noise
ffmpeg -i in.mp4 -vf "noise=alls=12:allf=t+u" -c:v libx264 -crf 18 out.mp4

# TESTED geq (procedural grain, no plate file)
ffmpeg -i in.mp4 -vf "geq=lum='lum(X,Y)+(random(1)-0.5)*24':cb='cb(X,Y)':cr='cr(X,Y)'" \
  -c:v libx264 -crf 18 out.mp4

# TESTED vignette
ffmpeg -i in.png -vf "vignette=angle=PI/4" out.png

# TESTED halation approx (bright-pass, blur, screen-blend over base)
ffmpeg -i in.png -filter_complex \
  "[0:v]split=2[base][blur];[blur]eq=brightness=-.2:contrast=2.0,gblur=sigma=18[glow];\
   [base][glow]blend=all_mode=screen:all_opacity=.5" out.png

# TESTED tonemap HDR->SDR (input must already be colour-tagged, see Traps)
ffmpeg -i in.mp4 -vf \
  "setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709,\
   zscale=transfer=linear,tonemap=hable,zscale=transfer=bt709,format=yuv420p" \
  -c:v libx264 -crf 18 out.mp4

# TESTED explicit output tagging (the Premiere round-trip fix, see Traps)
ffmpeg -i in.mp4 -vf "format=yuv420p" \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv \
  -c:v libx264 -crf 18 out.mp4
```

`haldclut`'s two-input syntax and HDR tonemapping on a *real* Flow clip are both **UNTESTED** —
no HDR Flow footage was on hand, and per §4 of `post-production.md` Flow returns SDR only today,
so tonemap is future-proofing, not a current need.

## BadCode fit

- **Near-black punishes noise-floor errors.** Apply grain last, right before encode — keep
  `alls` under ~15 on shadow-heavy plates; 12 read clean on the near-black test still.
- **`colorbalance`'s shadow lane is where the look lives** — a small cool `rs`/`bs` push reads
  as "the one thin light" without re-prompting Flow for a colder key.
- **1376×768 has no headroom for halation** — `sigma=18` softens broadly at this res; keep
  sigma at 8–12 or mask the bright-pass tighter, or the light reads as fog.
- **Vignette's default centre rarely matches Flow's off-centre lights** — set `x0`/`y0` per shot.
- **Prefer `colorchannelmixer` monochrome over `hue=s=0`** for deliberate black-and-white — the
  mixer's weights are documented print convention; `hue=s=0` is just internal luma.
- **Grain plates beat procedural noise for hero-length shots** — a free 4K plate (tdcat.com)
  reads more like scanned film than `noise` at Flow's native resolution.

## Traps

- **Untagged colour metadata is the biggest round-trip bug.** Confirmed live: untagged ffmpeg
  output reports `color_range/space/transfer/primaries=unknown` via `ffprobe`; adding
  `-color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv` fixes it. Premiere
  guesses when tags are missing — always tag explicitly on output.
- **`tonemap` hard-fails on untagged input**: `code 3074: no path between colorspaces` —
  confirmed live. Fix: `setparams=color_primaries=...:color_trc=...:colorspace=...` first, or
  tag the source (previous trap).
- **tv (16–235) vs pc (0–255) range is a separate axis from primaries/transfer** — a file can be
  correctly tagged `bt709` and still be wrong-range; `-color_range tv/pc` and
  `zscale=range=full|limited` are the levers, wrong direction crushes or washes out blacks.
  [w3.org public-png list 2024, 2026-08-21 — background, not authoritative]
- **Heavy grain before `format=yuv420p` gets chroma-averaged** and can shift colour — grain last.
- **`eq gamma` and `colorlevels` are not interchangeable** — one's a power curve, one a linear
  remap; stacking both compounds rather than substitutes.
- **`haldclut`'s second input must be a Hald identity image or lossless video**, or the CLUT
  degrades before it's applied.
- **No version-drift risk** — every filter here is core-stable and confirmed present on this
  exact 4.4.2 build; unlike `xfade`'s roster, nothing needs a version cross-check.

## Sources

- [ffmpeg.org — Filters Documentation](https://ffmpeg.org/ffmpeg-filters.html) — 2026-08-21 — curves/lut3d/colorbalance/eq/noise/tonemap/zscale definitions
- [dehancer.com/pricing/monthly](https://www.dehancer.com/pricing/monthly), [dehancer.com/shop/aepr/pro](https://www.dehancer.com/shop/aepr/pro) — 2026-08-21 — Dehancer subscription and perpetual prices
- [filmconvert.com/nitrate](https://www.filmconvert.com/nitrate), [filmconvert.com/purchase](https://www.filmconvert.com/purchase) — 2026-08-21 — Nitrate perpetual price, one-time model
- [4kshooters.net, 2025-11-28](https://www.4kshooters.net/2025/11/28/save-up-to-40-on-filmconverts-full-suite-the-ultimate-film-look-tools-now-cheaper-than-ever/) — 2026-08-21 — Nitrate Black Friday sale price
- [helpx.adobe.com — Noise and grain effects](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/noise-and-grain-effects.html) — 2026-08-21, dated 2025-08-22 — confirms "Noise & Grain" name
- [helpx.adobe.com — Color grading workflows](https://helpx.adobe.com/premiere-pro/using/color-workflows.html) — 2026-08-21 — confirms Lumetri "Input LUT"
- [tdcat.com/downloads/filmgrain](https://tdcat.com/downloads/filmgrain) — 2026-08-21 — free DCI 4K film-grain plates
- Local: `ffmpeg -version`/`-filters` plus live test runs, scratchpad — 2026-08-21 — every TESTED command and both traps reproduced directly
