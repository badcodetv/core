# ffmpeg effects catalogue — the other half of the effect question

**The twin of [`../premiere/effects-catalogue.md`](../premiere/effects-catalogue.md).** That file
is what Premiere can do; this is what ffmpeg can do. **Asked "what effects could we apply?", the
answer is both files — never one.** Established 2026-08-26 (Kai): *"if I ask what effects we have
to browse, it should very much be a case of listing easily the effects inside ffmpeg and in
Premiere."*

Harvested live on this machine **2026-08-26**. Re-run `./scripts/ffmpeg-catalogue.sh` after any
ffmpeg upgrade — the counts below are the check.

| | |
| --- | --- |
| ffmpeg | **4.4.2** (Ubuntu 22.04, WSL) |
| Filters | **477** total · **319** video |
| frei0r plugins | **133** in `/usr/lib/frei0r-1/` |
| Plugin hosts enabled | `frei0r` (video) · `ladspa` + `lv2` (audio) · `libvidstab` · `libzmq` · `opencl` |

**Yes, ffmpeg has plugins.** `frei0r` is a whole second effect library, called as
`-vf frei0r=<name>:<param1>|<param2>`. Verified working 2026-08-26: `frei0r=glow:0.5`,
`frei0r=scanline0r`.

---

## 🔴 The eight things ffmpeg can do that Premiere cannot

This is the list that decides the lane. Everything here is a *capability gap*, not a preference.

| Want | Filter | Why not Premiere |
| --- | --- | --- |
| **Words on screen** | `drawtext` | 🔴 **Premiere's API cannot write a string at all.** `SimpleText` and MOGRT both throw `Illegal Parameter type`; an exported frame still read "Default Text" after the write appeared to succeed. **Any automated title must be built here.** ✅ verified |
| **Real blend modes** | `blend=all_mode=screen\|overlay\|multiply\|…` | Premiere's blend mode lives on the Opacity intrinsic; the API cannot enumerate the options and the integer for Screen has never been measured. Here it is a word. ✅ verified |
| **Per-pixel maths with time** | `geq` — has `X`, `Y`, `T`, `r(x,y)`, `lum(x,y)` | No equivalent anywhere in Premiere. Procedural flicker, moving light sweeps, gradients that travel — anything expressible as a formula. ✅ verified |
| **Flash-safety compliance** | `photosensitivity` | Nothing equivalent. **Run it on any strobe, alarm or glitch sequence before delivery.** ✅ verified |
| **Displacement / remapping by a map image** | `displace` · `remap` | Premiere has no displacement-map effect (that one lives in After Effects, which is not installed) |
| **Timed parameter changes mid-render** | `sendcmd` · `zmq` | Keyframes only, set by hand |
| **Two-pass stabilisation, headless** | `vidstabdetect` → `vidstabtransform` | Warp Stabilizer needs the GUI and an analysis pass no tool call can trigger |
| **Measurement you can assert on** | `signalstats` · `scdet` · `freezedetect` · `blackdetect` · `psnr` · `ssim` | Scopes are for looking at. These print numbers, which is what `scripts/delivery-qc.sh` is built on |

**And the reverse.** Premiere has 106 effects and 118 transitions with a real-time preview,
`Volumetric Rays` with a keyframeable light position, `Strobe`, `Echo Glow` and `Camera Shake` that
self-animate, and a human who can look at it and say no. **If a person will iterate on it by eye,
it belongs in Premiere.**

---

## Video filters, grouped by what you would actually ask for

### Colour and grade

| Want | Filter |
| --- | --- |
| **A LUT** | `lut3d` · `lut1d` · `haldclut` |
| Curves | `curves` (has presets: `vintage`, `darker`, `increase_contrast`…) |
| Levels by numbers | `colorlevels` · `lutyuv` · `lutrgb` · `lut` |
| Exposure / contrast | `exposure` · `eq` (contrast, brightness, saturation, gamma) |
| Per-channel mixing | `colorchannelmixer` — **the red-alert flood** |
| White balance | `colortemperature` · `colorbalance` · `colorcorrect` |
| Punch without clipping | `vibrance` · `colorcontrast` |
| Isolate / replace one colour | `selectivecolor` · `colorize` · `chromahold` · `colorhold` |
| Monochrome | `monochrome` · `hue=s=0` |
| Invert / negate | `negate` · `lutrgb` |
| Posterise / banding fix | `pseudocolor` · `deband` · `gradfun` |
| Tone-map HDR | `tonemap` · `zscale` |
| Broadcast-legal clamp | `limiter` |

### Grain, decay, "the transmission is failing"

| Want | Filter |
| --- | --- |
| **Grain** | `noise=alls=N:allf=t+u` |
| **CRT scanlines** | `frei0r=scanline0r` |
| **Analogue sync failure / roll** | `frei0r=nosync0r` · `frei0r=nervous` · `frei0r=baltan` · `frei0r=delaygrab` |
| **Digital corruption** | `frei0r=glitch0r` · `frei0r=tehroxx0r` |
| Chromatic split | `rgbashift` · `chromashift` · `frei0r=rgbsplit0r` |
| Frame-rate stutter | `framestep` · `fps` · `decimate` · `shuffleframes` |
| Trails / echo | `lagfun` · `tmix` · `tblend` · `frei0r=delay0r` |
| Heat-haze, melt, warp | `displace` · `geq` · `frei0r=distort0r` · `frei0r=elastic_scale` |
| Pixelate / censor | `pixelize` *(via `frei0r=pixeliz0r`)* · `boxblur` |
| Line-art | `edgedetect` · `sobel` · `prewitt` · `roberts` · `kirsch` · `frei0r=cartoon` |
| Emboss | `frei0r=emboss` · `convolution` |

### Light and bloom

| Want | Filter |
| --- | --- |
| **Bloom / glow** | `frei0r=glow` · `frei0r=softglow` · `frei0r=edgeglow` |
| Light trails painted over time | `frei0r=lightgraffiti` |
| Vignette | `vignette` · `frei0r=vignette` |
| Gradient / ramp overlay | `gradients` · `frei0r=cairogradient` · `frei0r=alphagrad` |
| A moving light sweep | `geq` with `T` — no plugin needed |

### Blur and focus

| Want | Filter |
| --- | --- |
| Gaussian | `gblur` · `avgblur` · `boxblur` |
| Directional / motion streak | `dblur` |
| Edge-preserving | `bilateral` · `smartblur` · `sab` |
| Sharpen | `unsharp` · `cas` (contrast-adaptive) |
| Denoise | `nlmeans` · `hqdn3d` · `atadenoise` · `fftdnoiz` · `bm3d` · `vaguedenoiser` · `owdenoise` |
| **Remove Veo's frame-to-frame luminance wobble** | `deflicker` |

### Movement, framing, geometry

| Want | Filter |
| --- | --- |
| **Eased camera move on a still — the workhorse** | `zoompan` (recipes: [`../flow/post-production.md`](../flow/post-production.md) §3.4) |
| Crop / pad / scale | `crop` · `pad` · `scale` · `scale2ref` |
| Rotate / shear / flip | `rotate` · `shear` · `transpose` · `hflip` · `vflip` |
| Corner-pin / 2.5D card | `perspective` · `frei0r=c0rners` · `frei0r=scale0tilt` |
| Lens distortion | `lenscorrection` · `v360` · `frei0r=defish0r` |
| Scroll | `scroll` |
| Stabilise | `vidstabdetect` + `vidstabtransform` · `deshake` |
| Optical-flow retime | `minterpolate` · `setpts` (plain retime) |
| Loop / hold / pad | `loop` · `tpad` · `reverse` · `trim` |

### Compositing and keying — how Flow elements get in

**The house route for fire, smoke, sparks and weather** stays: generate the element in Flow on pure
black, then key it. In ffmpeg that is one filter, and the Screen blend actually works here.

| Want | Filter |
| --- | --- |
| **Element on black over a plate** | `blend=all_mode=screen` — ✅ verified |
| Overlay with alpha | `overlay` |
| Key out luma | `lumakey` |
| Key out a colour | `colorkey` · `chromakey` |
| Kill green spill | `despill` |
| Matte from another stream | `maskedmerge` · `maskedclamp` · `alphamerge` · `alphaextract` |
| Premultiply fixes | `premultiply` · `unpremultiply` |
| Side by side / grid | `hstack` · `vstack` · `xstack` · `tile` |
| **Transitions between two clips** | `xfade` — 50+ named modes, headless |

### Text and generators

| Want | Filter |
| --- | --- |
| **Text, with exact timing** | `drawtext` — `enable='gte(t,N)'` per element gives typing, counters, timed captions |
| Boxes, grids, guides | `drawbox` · `drawgrid` |
| Burn in subtitles | `subtitles` · `ass` |
| Blank / colour source | `color` · `nullsrc` |
| Procedural texture | `gradients` · `cellauto` · `life` · `mandelbrot` · `sierpinski` · `frei0r=plasma` · `frei0r=partik0l` |
| Test patterns | `testsrc2` · `smptebars` · `rgbtestsrc` |

### Measurement and QC

`signalstats` · `blackdetect` · `freezedetect` · `scdet` · `cropdetect` · `psnr` · `ssim` ·
`vmafmotion` · `entropy` · `bitplanenoise` · `histogram` · `waveform` · `vectorscope` ·
`oscilloscope` · `datascope` · `showinfo` · `graphmonitor`

🟢 These are what make the delivery gate assertable rather than a look-and-hope. See
[`delivery.md`](delivery.md) and `scripts/delivery-qc.sh`.

### Audio

`ladspa` and `lv2` hosts are both enabled, plus `librubberband` (pitch/time). Native filters cover
the everyday: `loudnorm` (broadcast loudness), `acompressor`, `alimiter`, `highpass`/`lowpass`,
`afade`, `adelay`, `areverse`, `atempo`, `asetrate`, `aecho`, `afftdn` (denoise), `sidechaincompress`
(ducking narration under music).

🔴 **Premiere has no audio-transition API whatsoever** — so any audio crossfade done by tool call
happens here.

---

## The frei0r shelf, by register

Full list: `./scripts/ffmpeg-catalogue.sh --frei0r`. The ones worth remembering:

| Register | Plugins |
| --- | --- |
| **Decay / analogue** | `scanline0r` · `nosync0r` · `nervous` · `baltan` · `delaygrab` · `glitch0r` · `tehroxx0r` · `dither` |
| **Light** | `glow` · `softglow` · `edgeglow` · `lightgraffiti` · `vignette` · `alphaspot` |
| **Grade** | `curves` · `levels` · `three_point_balance` · `sopsat` · `primaries` · `balanc0r` · `saturat0r` · `coloradj_RGB` · `colortap` |
| **Geometry** | `c0rners` · `perspective` · `scale0tilt` · `defish0r` · `distort0r` · `elastic_scale` · `3dflippo` |
| **Keying** | `bluescreen0r` · `keyspillm0pup` · `spillsupress` · `select0r` · `alphaspot` · `mask0mate` · `bgsubtract0r` |
| **Blend modes as filters** | `screen` · `overlay` · `multiply` · `softlight` · `hardlight` · `burn` · `dodge` · `difference` · `lighten` · `darken` |
| **Procedural** | `plasma` · `partik0l` · `ising0r` · `cluster` · `lissajous0r` · `cairogradient` |
| **Stylise** | `cartoon` · `emboss` · `posterize` · `colorhalftone` · `pixeliz0r` · `sobel` · `sharpness` |

⚠️ **frei0r params are positional and normalised 0–1**, separated by `|`, and the plugin's own docs
are the only reference: `ffmpeg -h filter=frei0r` then read `/usr/lib/frei0r-1/`. Several plugins
require `format=rgb24` before them and `format=yuv420p` after — both verified calls above needed it.

---

## Where this connects

- [`../premiere/effects-catalogue.md`](../premiere/effects-catalogue.md) — **the other half.
  Always check both**
- [`hybrid-method.md`](hybrid-method.md) — which layer the effect belongs to, and why
- [`../flow/post-production.md`](../flow/post-production.md) — the recipe book, every command run
  on real BadCode footage
- [`delivery.md`](delivery.md) — the QC gate before anything ships
- `./scripts/ffmpeg-catalogue.sh` — re-harvest after an upgrade

**Provenance.** Inventory harvested live 2026-08-26 on ffmpeg 4.4.2. Items marked ✅ verified were
executed on a real plate that day; the rest are present in the build and grouped from the filter
list, not individually exercised. **Say which is which when it matters.**

---

## 🔴 `geq` traps — both cost a rebuild on GPOM cut 3 (2026-08-27)

`geq` is the most powerful filter in this catalogue and the one most likely to hand back
something plausible and wrong. Two silent failures, in order:

| Trap | What you see | The rule |
| --- | --- | --- |
| **`format=gbrp` swaps the channels** | an `r='…'` expression lands on the GREEN plane. Boosting a flame turned it lime — twice, additive then multiplicative, before the cause was obvious | **Modulate `lum` in `yuv444p`** and pass `cb`/`cr` through unchanged. Hue then cannot shift, by construction. `yuv444p` not `yuv420p`, so chroma coordinates line up with luma |
| **`geq` does not clamp — it wraps** | luma driven above 255 comes back near **0**, punching black speckles into the brightest part of whatever you are brightening | **Always `clip(expr, 0, 255)`** |

**The general lesson:** `geq` is unclamped per-pixel arithmetic with no type safety. Any
expression that can leave the range must say what happens at the range, and any expression
addressed to a named colour channel must be checked against a rendered frame — the plane mapping
is a property of the pixel format, not of the parameter name.

### The working shape, for reuse — one region breathing on a frozen plate

```bash
D='((X-623)*(X-623)+(Y-218)*(Y-218))'                       # squared distance from the target
M="(0.74*(exp(-${D}/200)+0.35*exp(-${D}/3200)))"            # tight core + soft glow, peak ~1.0
FL='(0.50+0.28*sin(6.2832*3.3*T)+0.16*sin(6.2832*7.9*T+1.1)+0.10*sin(6.2832*15.1*T+2.3))'
ffmpeg -loop 1 -i plate.jpg -t 12 -r 24 -vf "format=yuv444p,\
geq=lum='clip(lum(X,Y)*(1+${M}*(0.62*${FL}-0.36)),0,255)':cb='cb(X,Y)':cr='cr(X,Y)',\
scale=1920:1080:flags=lanczos,noise=c0s=7:c0f=t+u,format=yuv420p" -c:v libx264 -crf 15 out.mp4
```

**Three sines at incommensurate rates**, so the flicker never visibly repeats — one sine reads as
a pulsing lamp, not as fire. **`noise=…:allf=t+u` is not optional:** a locked plate with no moving
grain reads as a frozen JPEG, and the grain is what makes it read as footage.

⚠️ **When the thing to modulate is a scattered field rather than one spot** — hundreds of rack
lamps, each needing its own phase — `geq` is the wrong tool, because it cannot address a blob.
Build the mask in numpy (a **grey-opening top-hat** isolates small bright features and rejects
large ones for free, so ceiling strips and handrails exclude themselves), intersect it with a
colour test, label the blobs, give each its own phase and rate, and pipe raw frames into ffmpeg.
Worked example, 515 lamps:
[`../stories/gitpush-origin-master/scenes/plant-room-recut.md`](../stories/gitpush-origin-master/scenes/plant-room-recut.md) § B3.

### ⚠️ `vidstab` will not cancel a deliberate camera move

Measured 2026-08-27: `vidstabtransform` with `smoothing=0 relative=0` made a slowly-tracking Veo
clip **worse** (94px vertical). It smooths handheld shake. It cannot undo a translation carrying
real parallax, because near and far fields move by different amounts and no single 2D transform
fixes both. See [`../flow/video-prompting.md`](../flow/video-prompting.md) §9.
