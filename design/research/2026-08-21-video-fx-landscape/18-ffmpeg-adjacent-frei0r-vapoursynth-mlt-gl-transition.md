# Adjacent CLI/post tools: frei0r, VapourSynth, MLT/melt, ffmpeg-gl-transition, ImageMagick, Python

## What this covers

What sits *next to* `ffmpeg` in a scripted pipeline: a plugin bank ffmpeg loads
(frei0r), a scriptable engine for temporal/AI work ffmpeg can't do alone
(VapourSynth), a declarative timeline CLI that could replace hand-rolled
`filter_complex` (MLT/`melt`), a shader-transition patch for ffmpeg itself
(ffmpeg-gl-transition), still-image/per-frame tools (ImageMagick, Pillow), Python
orchestration (MoviePy), code-driven motion graphics (Remotion, Motion Canvas), and
timeline interchange (OpenTimelineIO). None of this repeats
[`docs/flow/post-production.md`](../../../docs/flow/post-production.md) (strip-audio,
reverse, ping-pong, zoompan dolly, chained push-in, last-frame, concat/fps-SAR,
minterpolate retime, subtitle-crop, contact sheet).

All claims below were checked live on this box (Ubuntu 22.04.5 LTS, ffmpeg 4.4.2,
Python 3.12.12) on 2026-08-21, not assumed.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Extra grain/glitch/distort filters beyond ffmpeg's built-ins | frei0r | `apt install frei0r-plugins`, `-vf frei0r=<name>:<params>` | free |
| Procedural texture with no source frame | frei0r_src | `-f lavfi -i frei0r_src=size=1280x720:filter_name=<gen>` | free |
| True AI frame interpolation (RIFE) for slow-mo | VapourSynth + vs-rife | `.vpy` script piped via `vspipe \| ffmpeg` | free, real setup |
| Motion-compensated denoise/restoration | VapourSynth (mvtools) | same `.vpy` route | free, real setup |
| Declarative timeline instead of hand-built `filter_complex` | MLT `melt` | `melt a.mp4 b.mp4 -mix 25 -mixer luma -consumer avformat:out.mp4` | free |
| Reusable/versioned edit definition | MLT XML | `melt … -consumer xml:scene.mlt` | free |
| Shader transitions beyond xfade's 43 | ffmpeg-gl-transition | custom-built ffmpeg, `-filter_complex gltransition=source=<shader>.glsl` | free, you maintain the fork |
| Styled text/PNG overlay, batch stills, montage | ImageMagick `convert`/`montage` | `convert -size WxH xc:none -annotate 0 "TEXT" out.png` | free, installed |
| Procedural per-frame masks/gradients in Python | Pillow | `Image.new`/`ImageDraw`, feed frames to ffmpeg | free, installed |
| Data-driven cut/concat orchestration in Python | MoviePy 2.0 | `pip install moviepy`; wraps ffmpeg | free |
| Code-driven title cards / data graphics → video | Remotion (React) | `npx create-video@latest`, `npx remotion render` | free ≤3 people, else $100+/mo |
| Code-driven 2D/vector animation | Motion Canvas (TS) | `npm init @motion-canvas@latest` | free (MIT) |
| Round-trip an edit plan between tools | OpenTimelineIO | `pip install OpenTimelineIO` | free |

## Named tools

### frei0r
Plugin API + bundled effects — **133 `.so` plugins confirmed** after
`apt install frei0r-plugins` (`ls /usr/lib/frei0r-1/ | wc -l`). Free; per-plugin
open-source licences (the project *website* is CC-BY-NC-SA, not necessarily the
plugin code). Install: `sudo apt install frei0r-plugins` (Ubuntu 22.04 universe,
`1.7.0-2build1`). Mid-2000s vintage, stable, the standard bank Kdenlive/Shotcut ship.
⚠️ The scout expected a `grain0r` generator — **it does not exist in this 1.7.0
build**. What exists: `grain_extract`/`grain_merge` (compositing ops, not a
generator) and `rgbnoise` (a real noise generator, tested below).

### VapourSynth
Python-scripted frame server: a `.vpy` script defines a filter graph, `vspipe`
streams frames into `ffmpeg`. Free, MIT. Install: `pip install vapoursynth` (per
vendor site) — **not installed here**, and not in Ubuntu's apt at all. Value over
ffmpeg: `mvtools` (motion-compensated temporal filtering) and RIFE-family AI
interpolators (a *further* separate plugin, `vs-rife`/`vs-mlrt`, often GPU-backed).
Long-running (R76+), the encoding community's standard — but every layer here is a
separate install, none present today.

### MLT / melt
Multitrack A/V composition framework; `melt` is its CLI — producers, filters,
transitions, a consumer, serializable to XML. Powers Shotcut and Kdenlive. Free,
GPL/LGPL. Install: `sudo apt install melt` (Ubuntu 22.04 universe, `7.4.0-1build1`
— **not installed today**). Actively maintained (vendor cites v7.40.0 with
OpenFX/HDR support), over a decade inside two mainstream open NLEs.

### ffmpeg-gl-transition
Patches ffmpeg source to add a `gltransition` filter running a GLSL shader from the
gl-transitions gallery — a far bigger transition library than `xfade`'s 43, at the
cost of a shader-per-transition instead of a name. Free, MIT. Install: patch
ffmpeg's source, `./configure --enable-opengl --enable-filter=gltransition
--extra-libs='-lGLEW -lEGL'`, rebuild — replaces the system binary; not attempted
here. 720★/131 forks per its own repo page but no recent-activity evidence found —
a known working recipe, not an actively developed project.

### ImageMagick (`convert`/`mogrify`/`montage`)
Per-frame/per-still raster CLI. **Already installed**: `6.9.11-60 Q16`. Note the
binary is `convert` — IM7's `magick` does not exist on this box. Free, Apache 2.0.
Maturity: decades old, no surprises.

### Pillow
Python imaging library for procedural per-frame drawing. **Already installed**:
`12.1.1`. Free, MIT-CMU. Standard, stable API.

### MoviePy
Python clip-object API wrapping ffmpeg as a subprocess (cut/concat/composite).
**Not installed** (`ModuleNotFoundError`). Free, MIT. Current major version 2.0
(dated 2025-01-26 on its own docs) — a breaking rewrite from 1.x, so pre-2025
snippets may be stale syntax. Actively maintained through the rewrite.

### Remotion
React framework rendering code-defined compositions to video — fits data-driven
title cards or parametrised templates. **Licence gate is headcount, not
revenue**: free/unlimited commercial use ≤3 people (covers BadCode today);
Company licence $100+/month past that. Seen 2026-08-21 on the vendor's own site,
not independently corroborated. Install: `npx create-video@latest`. Maturity:
5M+ monthly npm installs, 56k GitHub stars per vendor claim — self-reported.

### Motion Canvas
TypeScript, code-driven 2D/vector animation — lighter, more editor-like than
Remotion. Free, MIT, no paid tier found. Install: `npm init @motion-canvas@latest`.
Smaller/younger than Remotion; fits vector motion graphics over video compositing.
⚠️ motioncanvas.io returned HTTP 403 to the fetch tool this pass — the above relies
on prior knowledge, not a freshly re-verified source.

### OpenTimelineIO
Interchange format + API for editorial cut data (clips, timing, transitions,
markers) — not an editor. Free, Apache 2.0 (Academy Software Foundation). Install:
`pip install OpenTimelineIO` — **not installed** (`ModuleNotFoundError`). **Gap**:
Premiere or MLT/`melt` adapter support was not established from its docs page this
pass — unconfirmed, not absent.

## Automation hook

None of these are Premiere effects/transitions/MOGRTs, so UXP match names don't
apply — they're pre-Premiere, CLI-side steps that hand Premiere a finished file.

```bash
# frei0r vignette — TESTED 2026-08-21 (320x180 lavfi still -> valid PNG)
ffmpeg -loop 1 -i still.png -t 1 -vf "frei0r=vignette:0.5|0.5" -frames:v 1 out.png

# frei0r rgbnoise (closest to a "grain" generator in this plugin set) — TESTED
ffmpeg -loop 1 -i still.png -t 1 -vf "frei0r=rgbnoise:0.3" -frames:v 1 out.png

# melt: two-clip luma mix, then render — UNTESTED (melt not installed this pass)
melt a.mp4 out=49 -track -blank 24 b.mp4 -transition luma in=25 out=49 a_track=0 \
  a_track=1 -consumer avformat:out.mp4 vcodec=libx264

# ImageMagick styled text-on-alpha PNG — TESTED (produced a 1027-byte PNG)
convert -size 1280x720 xc:none -pointsize 48 -fill white -gravity center \
  -annotate 0 "TITLE TEXT" title.png

# ffmpeg-gl-transition — UNTESTED (needs a custom-built ffmpeg, not attempted)
ffmpeg -i a.mp4 -i b.mp4 -filter_complex \
  "gltransition=duration=1:offset=3:source=crosswarp.glsl" out.mp4

# VapourSynth -> ffmpeg pipe — UNTESTED (module not installed this pass)
vspipe --y4m script.vpy - | ffmpeg -i - -c:v libx264 -crf 18 out.mp4
```

## BadCode fit

- **frei0r**: `rgbnoise` and `vignette` are the two useful ones on near-black
  footage — blend `rgbnoise` in at low opacity (straight, it reads as sensor noise,
  not film grain), `vignette` reinforces the one-thin-light framing. Verified clean
  at 320×180; no reason to expect trouble at 1280×768.
- **VapourSynth/RIFE**: real upside for §3.7's minterpolate-smear problem, but it's
  setup work (core + a GPU-backed RIFE plugin, none installed). Pilot off the
  critical path, not under a deadline.
- **MLT/`melt`**: worth evaluating past ~3–4 clips with mixed transitions (XML
  reads better than a growing `filter_complex` string), but none of
  post-production.md's existing recipes (fps/SAR normalisation, the reversed-chain
  trick) have a documented `melt` equivalent — adopting it means re-deriving them.
- **ImageMagick/Pillow**: solid fit for titles — already installed, and the
  `text-titles` gap in post-production.md is real.
- **Remotion/Motion Canvas**: overkill for one title card (drawtext/ImageMagick
  covers that); real fit is a *recurring, parametrised* graphic reused every
  release — a lower-third, an end-card.
- **Avoid**: chasing gl-transition's shader gallery for novelty — `xfade`'s 43
  built-ins (already present, no build step) suit the restrained BadCode register
  better than most gl-transitions demo-reel entries.

## Traps

- frei0r's plugin roster is distro/version-specific — the 133-count and missing
  `grain0r` are for `1.7.0-2build1` on Ubuntu 22.04 only; check the actual box.
- MoviePy 1.x vs 2.0 (Jan 2025) is a breaking rewrite — date any snippet first.
- VapourSynth, `melt`, and a gl-transition-patched ffmpeg are **all uninstalled**
  here — each is a real dependency chain, not a one-liner.
- Remotion's licence boundary is headcount (≤3 people), not revenue — recheck
  before adding collaborators (Kai + Jack = 2, fine today).
- OpenTimelineIO's Premiere/MLT adapter support is unconfirmed — don't plan a
  round-trip through it without checking the adapters list first.

## Sources

- https://frei0r.dyne.org/ (→ https://dyne.org/frei0r) — accessed 2026-08-21, frei0r API and licence
- https://ffmpeg.org/ffmpeg-filters.html#frei0r — accessed 2026-08-21, frei0r/frei0r_src syntax
- https://www.mltframework.org/ + /docs/melt/ — accessed 2026-08-21, MLT overview and melt CLI syntax
- http://www.vapoursynth.com/ — accessed 2026-08-21, VapourSynth capabilities and install route
- https://github.com/transitive-bullshit/ffmpeg-gl-transition — accessed 2026-08-21, build steps, MIT licence
- https://zulko.github.io/moviepy/ — accessed 2026-08-21, MoviePy 2.0 (2025-01-26), MIT licence
- https://www.remotion.dev/ — accessed 2026-08-21, licence tiers and pricing (vendor-stated)
- https://opentimelineio.readthedocs.io/en/latest/ — accessed 2026-08-21, OTIO purpose; adapters unconfirmed
- Local `apt-cache policy frei0r-plugins`/`melt` — 2026-08-21, confirmed Ubuntu 22.04 versions, uninstalled
- Local `ffmpeg -vf frei0r=vignette/rgbnoise` + `convert -annotate` runs — 2026-08-21, confirmed working syntax

**Gaps not closed**: frei0r plugin binaries' individual licences (site licence
≠ necessarily plugin code); OTIO's real Premiere/MLT adapter coverage;
ffmpeg-gl-transition's actual maintenance activity (only star/fork counts found);
VapourSynth+RIFE was researched, not executed (no module, no GPU interpolation
plugin); Motion Canvas licence/pricing came from prior knowledge after its site
403'd the fetch — worth a direct spot-check before being quoted as fact.
