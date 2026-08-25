# ffmpeg transitions, overlays, blend modes, chroma/luma key, masks

## What this covers

`xfade` (43 named transitions + custom `expr`, `offset`/`duration`, `acrossfade` audio pairing,
the "same size/fps/pixfmt" requirement); `overlay` (position expressions, timed
`enable=between(t,…)`); `blend`/`tblend`; `chromakey`/`colorkey`/`lumakey`;
`alphamerge`/`alphaextract`/`maskedmerge`; `geq`-driven procedural masks; picture-in-picture,
split screens, a PNG lower-third; `filter_complex` patterns for chaining these. Also notes
`ffmpeg-gl-transition` as a shader-based alternative to `xfade`.

**Not covered** (owned by `docs/flow/post-production.md`, referenced by section not repeated):
strip audio (§3.1), reverse (§3.2), ping-pong loop (§3.3), eased `zoompan` dolly (§3.4/3.4b),
last-frame extraction (§3.5), `concat` + fps/SAR normalisation (§3.6), `minterpolate` retiming
(§3.7), subtitle-crop rescue (§3.8), contact sheet (§3.9).

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Crossfade two clips | `xfade`+`acrossfade` | `xfade=transition=dissolve:duration=1:offset=T`, sound via `acrossfade` | free |
| Named wipe/slide/dissolve | `xfade transition=` | pick from the 43 below | free |
| Custom transition shape | `xfade transition=custom` | pixel-blend math in `expr=` | free |
| Shader transition (GLSL) | `ffmpeg-gl-transition` (3rd-party) | source-compiled `gltransition`, ~100 transitions | free, **not installed** |
| Picture-in-picture | `overlay`+`scale` | scale inset, `overlay=x=…:y=…` | free |
| Split screen | `crop`+`hstack`/`vstack` | crop each half, stack | free |
| Chroma-key a subject | `chromakey` | `color:similarity:blend`, YUV | free |
| Key a flat colour | `colorkey` | same shape, RGB, harder edge | free |
| Key by brightness | `lumakey` | `threshold:tolerance:softness` | free |
| Vignette | `vignette` | `angle=PI/4`, animatable | free |
| Blend two layers | `blend` / `tblend` (frame-to-frame) | `all_mode=screen:all_opacity=0.5` | free |
| Mask plumbing | `alphamerge`/`alphaextract`/`maskedmerge` | write/pull alpha, or blend via a 3rd mask stream | free |
| Procedural mask | `geq` | `lum='...'` → feed `alphamerge` | free |
| Lower-third from PNG | `overlay`+alpha PNG | `convert` builds it, timed `enable=between(t,a,b)` | free |
| Burned-in captions | `drawtext` | `fontfile=…:box=1:boxcolor=black@0.5` | free |

## Named tools

### xfade
Built-in video cross-fade — 43 named transitions indexed 0–42 (`fade`, `wipeleft/right/up/
down`, `slideleft/right/up/down`, `circlecrop`, `rectcrop`, `distance`, `fadeblack/white`,
`radial`, `smoothleft/right/up/down`, `circleopen/close`, `vertopen/close`, `horzopen/close`,
`dissolve`, `pixelize`, `diagtl/tr/bl/br`, `hlslice/hrslice/vuslice/vdslice`, `hblur`,
`fadegrays`, `wipetl/tr/bl/br`, `squeezeh/v`) plus `-1` (`custom`, hand-written `expr=`). Free,
ffmpeg core, confirmed via `ffmpeg -h filter=xfade` 2026-08-21. Stable since ffmpeg 4.3 (2020) —
later releases add names this 4.4.2 build lacks, check locally rather than trust a blog's list.

### acrossfade
`xfade`'s audio partner — cross-fades two audio streams so sound fades with picture. Free,
ffmpeg core, long-standing. Not auto-linked to `xfade`: matching `offset`/`duration` is manual.

### overlay
Composites one stream on another at a pixel position, with expressions (`main_w`, `overlay_w`,
`t`) and a timed `enable=` gate — the base primitive for PIP, lower-thirds, any layered
composite. Free, ffmpeg core, one of its oldest filters. GPU variants (`overlay_opencl/cuda/
qsv`) compiled in but unverified here (Traps).

### blend / tblend
`blend` mixes two streams frame-for-frame with a named mode per component (33 modes this
build — normal, screen, multiply, overlay, hardlight, difference, dodge, burn, more; full list
via `ffmpeg -h filter=blend`). `tblend` blends successive frames of *one* stream — motion-blur
ghosting. Free, ffmpeg core, stable since 2.x.

### chromakey / colorkey / lumakey
`chromakey` keys a colour in YUV space (green/blue-screen convention, forgiving of lighting
variance); `colorkey` keys an exact RGB value (harder edge, flat colour); `lumakey` keys by
brightness regardless of hue. All free, ffmpeg core; `colorkey_opencl` also compiled in,
unverified. `chromakey` is what most tutorials mean by "green screen in ffmpeg."

### alphamerge / alphaextract / maskedmerge / geq
The mask-plumbing family. `alphaextract` pulls a stream's alpha out as grayscale;
`alphamerge` writes a grayscale stream's luma into another's alpha — standard way to attach a
mask before `overlay`. `maskedmerge` composites via a third stream as blend weight, no alpha
needed. `geq` computes each pixel from an expression over `X,Y,W,H,T` — procedural masks with
no pre-rendered asset. All free, ffmpeg core, long-stable. `geq` is CPU-expensive (Traps).

### ffmpeg-gl-transition
Third-party filter (`github.com/transitive-bullshit/ffmpeg-gl-transition`) patching in
`gltransition`, driving GLSL shaders from [gl-transitions.com](https://gl-transitions.com) —
~100 transitions (book-flip, cube rotate, glitch) beyond `xfade`'s 43. Free/open-source (MIT).
Requires **compiling ffmpeg from source** with OpenGL headers — no `apt`/`pip` shortcut.
Confirmed **not installed** here 2026-08-21 (absent from `ffmpeg -filters`; no pip/npm package
found). Upstream maintenance is inconsistent — a dedicated build task, not a same-session ask.

### ImageMagick (convert)
Renders the lower-third PNG (alpha box + text) `overlay` times onto video. Free/open-source,
installed here as **v6.9.11-60 Q16** (`dpkg -l`, 2026-08-21). **`magick` (IM7) does not exist
on this box** — use `convert`/`mogrify`/`montage`. IM6 is security-patch-only upstream but
fully functional here.

## Automation hook

**Premiere side.** None of this maps to one match name — these are compositing graphs, not a
single filter. Crossfade → built-in **Cross Dissolve** (transitions are a separate registry
from `getMatchNames`, discover via the Transitions panel). Chroma key → **Ultra Key**, match
name `AE.ADBE Ultra Key` from general Adobe docs — **not verified against this install's live
`getMatchNames()` dump**, confirm before scripting. Blend modes → per-clip **Blend Mode**
property, not an effect. Lower-third → best as a **.mogrt** via the bridge's MOGRT-insert path,
not a PNG overlay. Anything else: **list effects, filter 'Key'/'Blend'/'Vignette'**, confirm live.

**ffmpeg side** — skeletons, all run this session against synthetic 1376×768/24fps clips unless
marked. `offset` is where in clip A's own timeline the fade starts; total length =
len(a)+len(b)-duration (confirmed exact: 4s+4s-1s=7s).

```bash
# xfade + acrossfade — TESTED
ffmpeg -i a.mp4 -i b.mp4 -filter_complex \
  "[0:v][1:v]xfade=transition=dissolve:duration=1:offset=3[v]" -map "[v]" -an out.mp4
ffmpeg -i a.wav -i b.wav -filter_complex "[0:a][1:a]acrossfade=d=1[a]" -map "[a]" out.wav

# picture-in-picture — TESTED
ffmpeg -i main.mp4 -i inset.mp4 -filter_complex \
  "[1:v]scale=344:192[pip];[0:v][pip]overlay=x=main_w-overlay_w-20:y=main_h-overlay_h-20[v]" \
  -map "[v]" -an out.mp4

# chromakey composite — TESTED
ffmpeg -i base.mp4 -i green.mp4 -filter_complex \
  "[1:v]chromakey=0x00FF00:0.1:0.1[keyed];[0:v][keyed]overlay=x=20:y=20[v]" -map "[v]" -an out.mp4

# geq radial mask -> alphamerge -> overlay — TESTED
ffmpeg -i a.mp4 -i b.mp4 -filter_complex \
  "[0:v]geq=lum='255*hypot(X-W/2,Y-H/2)/hypot(W/2,H/2)':cb=128:cr=128,format=gray[mask];\
   [1:v][mask]alphamerge[b_alpha];[0:v][b_alpha]overlay[v]" -map "[v]" -an out.mp4

# blend screen + split screen — TESTED
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "[0:v][1:v]blend=all_mode=screen:all_opacity=0.5[v]" -map "[v]" -an out.mp4
ffmpeg -i a.mp4 -i b.mp4 -filter_complex \
  "[0:v]crop=iw/2:ih:0:0[l];[1:v]crop=iw/2:ih:iw/2:0[r];[l][r]hstack=inputs=2[v]" -map "[v]" -an out.mp4

# PNG lower-third (built via ImageMagick convert) + drawtext caption — TESTED
ffmpeg -i clip.mp4 -i lt.png -filter_complex \
  "[0:v][1:v]overlay=x=20:y=main_h-overlay_h-20:enable='between(t,1,3)'[v]" -map "[v]" -an out.mp4
ffmpeg -i clip.mp4 -vf \
  "drawtext=fontfile=<font>:text='CAPTION':x=40:y=h-60:fontsize=28:fontcolor=white:box=1:boxcolor=black@0.5" -an out.mp4

# UNTESTED: colorkey/lumakey (same shape as chromakey), maskedmerge, ass subtitles
ffmpeg -i fg.mp4 -i bg.mp4 -filter_complex "[0:v]colorkey=0x00FF00:0.3:0.1[keyed];[1:v][keyed]overlay[v]" -map "[v]" -an out.mp4
ffmpeg -i a.mp4 -i b.mp4 -i mask.mp4 -filter_complex "[0:v][1:v][2:v]maskedmerge[v]" -map "[v]" -an out.mp4
ffmpeg -i clip.mp4 -vf "ass=captions.ass" -an out.mp4
```

## BadCode fit

- **Xfade on near-black 8s Veo clips:** `fade`/`dissolve`/`fadeblack` read as cinematic;
  geometric-fast ones (`pixelize`, `squeezeh/v`, diagonal wipes) read as template-video, fight
  the documentary tone — save for a deliberate glitch beat. 0.5–1s duration hides a join.
- **chromakey/colorkey vs near-black footage:** unaffected by base darkness, but Flow/Veo has no
  matte plate to key against — relevant only once compositing *generated* elements together
  (a light-sweep plate onto a base shot), not for isolating a real subject.
- **PIP / split-screen at 1376×768:** halving the frame halves resolution to 688px — same
  softness ceiling as the crop table in `post-production.md` §4. Budget as its own resolution cost.
- **geq masks / `vignette`:** computed, not sampled — costs nothing in sharpness, good fit for
  drawing the eye toward the "one thin light."
- **drawtext:** DejaVu Sans (installed) is generic, not a BadCode face — a placeholder until a
  brand font is sourced.

## Traps

- **xfade demands identical size, fps, and pixel format on both inputs**, or it fails loud
  immediately — confirmed 2026-08-21: `First input link main parameters (size 1376x768) do not
  match … (size 640x360)`. Same failure family as the SAR mismatch `post-production.md` §3.6
  documents for `concat` — normalise with `scale=…,fps=…,format=yuv420p` first.
- **`offset` is relative to input A's own timeline, not the output**; wrong arithmetic
  (`len(a)+len(b)-duration`) silently produces the wrong-length clip, no error. **`acrossfade`
  never auto-syncs to `xfade`** — match `duration`/`offset` by hand across the two graphs.
- **Version drift:** this 4.4.2 build enumerates exactly 43 named transitions + custom; later
  releases add names a newer doc page may assume — check `-h filter=xfade` locally.
- **OpenCL variants** (`xfade_opencl`, `colorkey_opencl`, `overlay_opencl`) are compiled in but
  WSL2 GPU passthrough was not smoke-tested — present in the binary, unproven end to end.
- **`ffmpeg-gl-transition` is not a package install** — source compile only, inconsistent
  upstream maintenance — a dedicated setup pass, not a same-day ask.
- **`geq` is CPU-heavy** — slower per frame than any other filter here; time it before a batch.
- **ImageMagick here is IM6 (`convert`), not IM7 (`magick`)** — a snippet assuming `magick`
  fails outright.

## Sources

- https://ffmpeg.org/ffmpeg-filters.html — 2026-08-21 — canonical xfade/overlay/blend/chromakey reference
- https://trac.ffmpeg.org/wiki/Xfade — 2026-08-21 — xfade transition gallery, previews per name
- https://helpx.adobe.com/premiere-pro/using/color-key-effects.html — 2026-08-21 — Ultra Key in Premiere
- https://ffmpeg.org/doxygen/4.4/group__lavfi.html — 2026-08-21 — confirms libavfilter version this build
- https://github.com/transitive-bullshit/ffmpeg-gl-transition — 2026-08-21 — gl-transitions patch, build-from-source
- https://gl-transitions.com — 2026-08-21 — shader library the gl-transition project draws from
- https://imagemagick.org/script/command-line-tools.php — 2026-08-21 — confirms IM6 binary naming
- Local ground-truth (2026-08-21): `ffmpeg -version/-filters/-h filter=xfade/-h filter=blend`, `dpkg -l | grep imagemagick`, plus live `ffmpeg`/`convert` runs against synthetic clips — every TESTED skeleton ran to completion, checked.

**Gap not closed:** no primary source confirms Adobe's exact match-name string for Ultra Key on
Premiere Pro 26.3.2 — `AE.ADBE Ultra Key` is carried from general Premiere/After Effects docs,
not verified against this install's own `getMatchNames()` dump.
