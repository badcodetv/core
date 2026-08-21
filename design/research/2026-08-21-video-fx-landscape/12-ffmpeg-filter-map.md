# ffmpeg filter map: what exists, organised by editing need

## What this covers

A by-need index of ffmpeg's video filter graph for BadCode's pipeline (Flow/Veo 8s clips + 1376×768
stills → ffmpeg post → Premiere Pro). Baseline: **ffmpeg 4.4.2-0ubuntu0.22.04.1** (Ubuntu 22.04,
WSL), confirmed via `ffmpeg -filters`/`-h filter=<name>` on 2026-08-21. Every filter below was
verified present in that output unless flagged otherwise.

**Excluded — already owned by [`docs/flow/post-production.md`](../../../docs/flow/post-production.md):**
strip-audio, reverse, ping-pong loop, eased `zoompan` dolly + chained push-ins, last-frame
extraction, `concat` + the fps/SAR gotcha, retime via `minterpolate`, subtitle-crop rescue, contact
sheet (§3.1–3.9). Referenced by section here, not repeated.

**Version finding: nothing here needs a newer ffmpeg.** Every filter answering a need below —
including `xfade` (43 named transitions + custom `expr`, added 4.3), `zscale`, `vidstab*`,
`lut3d`/`haldclut`, `chromakey`/`colorkey`, `lenscorrection`, and every OpenCL/VAAPI/CUDA/QSV
variant — is already in this 4.4.2 build. The real 5.x/6.x/7.x-shaped gap is in **external tools
ffmpeg doesn't ship**: Real-ESRGAN, RIFE, VapourSynth, MLT `melt` — none installed here. Their
upgrade route is a fresh install, not a version bump (below).

**Deep dives:** colour grading, film grain, text/subtitles, transitions, overlay/keying/masks,
stabilisation, frame interpolation & AI upscaling, audio mixing, aspect-ratio delivery, QC scopes,
and procedural motion graphics get full treatment in briefs 13–18. Use this file to find the
filter name and cost tier fast, then jump to the deep dive for recipes and BadCode tuning.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Cut/trim | `trim`, `atrim` | Pick start/end or duration, drop the rest | free |
| Concat | `concat` filter/demuxer | §3.6 — normalise fps+SAR first | free |
| Scale | `scale`, `zscale` | Resize; `zscale` is colourspace-aware, prefer for grading | free |
| Crop | `crop` | Cut a rectangle; §3.8 uses it as subtitle rescue | free |
| Pad | `pad` | Letterbox/pillarbox bars | free |
| Aspect metadata | `setdar`/`setsar` | Fix display/sample aspect, no pixel change — needed before `concat` | free |
| Speed | `setpts` | `PTS/f` speeds up, `PTS*f` slows — §3.7 has the retime recipe | free |
| Reverse | `reverse`/`areverse` | §2 and §3.2 | free |
| Loop | `loop` filter | Repeat N frames; §3.3's ping-pong is the seamless alternative | free |
| Overlay/stack | `overlay`, `hstack`/`vstack`/`xstack` | Composite or tile streams; `xstack` runs §3.9's sheet | free |
| Blend | `blend`, `tblend` | Blend two streams, or a frame with its predecessor (trails, ghosting) | free |
| Colour grade | `curves`, `colorbalance`, `colorchannelmixer`, `colorlevels`, `colortemperature`, `eq`, `vibrance`, `lut3d`, `haldclut` | Full grading chain — deep dive 13 | free |
| Blur/sharpen | `gblur`, `boxblur`, `avgblur`, `unsharp` | Gaussian/box/average blur; `unsharp` sharpens by sign too | free |
| Noise/grain | `noise`, `frei0r` (grain0r etc.) | Procedural grain or a frei0r pass — deep dive 14 | free |
| Text | `drawtext` | Burn styled text via libfreetype/libfontconfig — deep dive 15 | free |
| Subtitles | `subtitles`, `ass` | Burn `.srt`/`.ass` via libass, incl. karaoke — deep dive 15 | free |
| Transitions | `xfade`, `acrossfade` | 43 named transitions + custom `expr`; pair with `acrossfade` — deep dive 16 | free |
| Stabilise | `vidstabdetect`+`vidstabtransform`, `deshake`, `deshake_opencl` | Two-pass feature-track, or single-pass — deep dive 17 | free |
| Interpolate | `minterpolate`, `fps` | Motion-compensated synthesis (§3.7's smear warning) vs plain conversion | free |
| AI interpolate/upscale | Real-ESRGAN, RIFE (ncnn-vulkan), VapourSynth+mvtools | Not ffmpeg filters, external binaries, none installed — deep dive 17/18 | setup cost |
| Keying | `chromakey`, `colorkey` | Green/blue-screen (YUV) vs exact-RGB keying — deep dive 18 | free |
| Masks | `alphamerge`, `maskedmerge` | Build alpha, or blend two streams through a third as mask | free |
| Vignette | `vignette` | Static/animated radial darkening — tested this session | free |
| Lens correction | `lenscorrection` | Rectify barrel/pincushion given k1/k2 coefficients | free |
| Time effects | `tblend`, `tmix`, `framestep`, `tpad` | Frame blend, N-frame average, frame skip, temporal pad | free |
| Hardware accel | `hwupload`/`hwdownload`, `scale_vaapi`/`_cuda`/`_qsv`, `*_opencl` | GPU scale/blur/denoise/xfade/colorkey — unverified on WSL2 | free |
| Declarative orchestration | MLT `melt`, VapourSynth | XML/Python graphs vs one long `filter_complex` — not installed — deep dive 18 | setup cost |

## Named tools

### ffmpeg (core)
The filter engine everything above runs on. Free, LGPL/GPL mixed per component. Already present,
`apt` 4.4.2-0ubuntu0.22.04.1. De facto standard; every filter cited is core/stable, none experimental.

### ImageMagick (`convert`)
Still-image CLI for rendering styled title cards/alpha PNG overlays. Free, ImageMagick licence.
Seen 2026-08-21. Already present — `imagemagick` 8:6.9.11.60 (IM6). **Use `convert`/`mogrify`,
not `magick`** — no IM7 binary here. 30+ years, ubiquitous.

### frei0r
~130-plugin bank (grain, light sweeps, glow) via ffmpeg's `frei0r`/`frei0r_src`. Free, GPL/LGPL
mix. `--enable-frei0r` confirmed compiled in. Mature but low-velocity upstream.

### Real-ESRGAN (`realesrgan-ncnn-vulkan`)
Learned super-resolution upscaler — answers post-production.md §4's resolution ceiling. Free, BSD
3-Clause. Seen 2026-08-21. Linux/Windows/macOS, Vulkan, no PyTorch needed. **Not installed** —
GitHub Releases binary. Original repo's last prebuilt tag is 2022-era; maintainer `nihui`
publishes newer builds — solid but low-velocity, check freshness before relying on it.

### RIFE (`rife-ncnn-vulkan`)
Real-time frame interpolation for true AI slow-motion, distinct from `minterpolate`'s motion
compensation. Free, MIT-family. Seen 2026-08-21. **Not installed** — GitHub Releases binary. Core
repo's last tag is 2022-10-29; Python wrapper ecosystem released into 2025 — current technique,
stale-looking flagship repo.

### VapourSynth
Python frame-scripting engine (mvtools, RIFE plugins) — deep-dive-18's declarative-pipeline
answer. Free, LGPL 2.1. Seen 2026-08-21. **Not installed** (`import vapoursynth` fails here) —
`apt`/`pip`/source. Active — R67 current, R66 added installer scripts + Python 3.12 support.

### MLT (`melt`)
XML-scene-graph engine behind Shotcut/Kdenlive; alternative to a long `filter_complex` string.
Free, LGPL. Seen 2026-08-21. **Not installed** (`which melt` empty) — `apt install melt` or
source. Active, 7.36.1 released 2025-12-31.

### Adobe Premiere Pro (UXP bridge target)
The edit surface downstream of all this; the UXP bridge drives it by effect "match name." Bundled
in Creative Cloud — UK price not confirmed live this session (search budget ran out); secondary
source gives US$22.99/mo single-app or US$69.99/mo CC Pro, seen 2026-08-21 — **approximate,
verify before quoting**. Subscription only, no perpetual tier.

## Automation hook

**Premiere side.** No match name was verified live against this install this session — a gap, not
an assumption. Documented discovery path (Adobe's UXP Premiere Pro API): `activeSequence` → walk
`VideoTrack.clips[i].components` → each component's `getMatchNames()`/`matchName` gives the exact
string the bridge needs (filter for `"Blur"`, `"Gaussian"`, `"Dissolve"`, etc.). Run that
enumeration once per effect before automating it — don't guess from a menu label.

**ffmpeg side — skeletons, not full recipes (full recipes live in the deep dives):**

```bash
# transition — TESTED (dissolve)
ffmpeg -i a.mp4 -i b.mp4 -filter_complex \
  "[0:v][1:v]xfade=transition=dissolve:duration=D:offset=T[v]" -map "[v]" out.mp4

# burned text — TESTED
ffmpeg -i in.mp4 -vf "drawtext=text='…':fontcolor=white:fontsize=N:x=…:y=…" out.mp4

# grade + vignette — TESTED
ffmpeg -i in.mp4 -vf "curves=preset=…,vignette=PI/5" out.mp4

# procedural grain — TESTED
ffmpeg -i in.mp4 -vf "noise=alls=N:allf=t" out.mp4

# green-screen key — TESTED (synthetic testsrc only, not real footage)
ffmpeg -i in.mp4 -vf "chromakey=0xRRGGBB:similarity:blend" out.mp4

# two-pass stabilise — UNTESTED
ffmpeg -i in.mp4 -vf vidstabdetect=shakiness=5:result=t.trf -f null -
ffmpeg -i in.mp4 -vf vidstabtransform=input=t.trf:smoothing=15 out.mp4
```

The five TESTED commands ran against synthetic `testsrc`/`testsrc2` clips at 1376×768/24fps in the
scratchpad — confirms the graph is well-formed on this build, not that it looks right on real
footage.

## BadCode fit

- Near-black, one-thin-light plates are **low dynamic range and noise-hungry**: `curves`/`eq`
  moves that read fine on a bright frame can crush shadow detail here — check a real dark frame.
- 1376×768 stills mean any resampling filter (blur, sharpen, noise) has less headroom than typical
  footage — see post-production.md §4 before stacking several resampling filters in one chain.
- `xfade`/`vignette`/`drawtext` are cheap and instant (seconds, CPU-only) — prefer them over a
  fresh Flow generation whenever the need is compositional, not generative (§1's core rule).
- OpenCL filters are compiled in but **WSL2 GPU passthrough was not smoke-tested this session** —
  don't build a step around `deshake_opencl`/`xfade_opencl` etc. without running one first.

## Traps

- **Don't assume a filter name from a newer blog post exists here.** `xfade`'s transition roster
  has grown across releases; check `ffmpeg -filters`/`-h filter=<name>` on *this* box first.
- **`magick` is not installed** — only IM6's `convert`/`mogrify`/`montage`; IM7 syntax will fail.
- **Real-ESRGAN and RIFE's flagship repos look abandoned** (last binaries 2022) even though the
  technique is current — verify a downloaded binary actually runs before trusting it.
- **Premiere price wasn't confirmed against live UK checkout** (search budget ran out mid-brief) —
  re-verify before quoting externally.
- **Match names weren't enumerated against this install** — guessing from a UI label is a common
  Premiere-scripting failure; run the discovery step first.

## Sources

- [ffmpeg.org — Filters Documentation](https://ffmpeg.org/ffmpeg-filters.html) — 2026-08-21 — official filter reference, all names/options
- [FFmpeg/FFmpeg Changelog, GitHub](https://github.com/FFmpeg/FFmpeg/blob/master/Changelog) — 2026-08-21 — confirms `xfade` added in 4.3
- [John Van Sickle — FFmpeg Static Builds](https://johnvansickle.com/ffmpeg/) — 2026-08-21 — static-build upgrade route, Ubuntu 22.04
- [UbuntuHandbook — Install FFmpeg 7.0 via PPA](https://ubuntuhandbook.org/index.php/2024/04/ffmpeg-7-0-ppa-ubuntu/) — 2026-08-21 — PPA upgrade route, 22.04/24.04
- [xinntao/Real-ESRGAN-ncnn-vulkan, GitHub](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan) — 2026-08-21 — licence, release status
- [nihui/rife-ncnn-vulkan, GitHub](https://github.com/nihui/rife-ncnn-vulkan) — 2026-08-21 — release status, platforms
- [mltframework/mlt Releases, GitHub](https://github.com/mltframework/mlt/releases) — 2026-08-21 — current `melt` version 7.36.1
- [vapoursynth.com](https://www.vapoursynth.com/) — 2026-08-21 — current release line, licence
- [Adobe — Premiere Pro UXP API reference](https://developer.adobe.com/premiere-pro/uxp/ppro-reference/) — 2026-08-21 — match-name discovery API
- [Adobe — Creative Cloud Plans](https://www.adobe.com/creativecloud/plans.html) — 2026-08-21 — official pricing page, UK not live-confirmed
