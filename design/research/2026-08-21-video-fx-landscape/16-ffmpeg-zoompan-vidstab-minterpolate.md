# ffmpeg motion: Ken Burns beyond zoompan, stabilisation, frame interpolation, retime

## What this covers

Everything [`post-production.md`](../../../docs/flow/post-production.md) doesn't: rotation and
perspective as camera moves (not just `zoompan`'s pan/scale), parallax from independently-panned
still layers, removing *unwanted* shake (§3's moves are rigid by construction — this is an
artefact you didn't ask for), true frame interpolation beyond §3.7's retime-to-beat-8s use,
`tblend`/`tmix` as motion blur, the real limits of `setpts`/`atempo`, and the upscale routes §4
leaves open — Lanczos/spline resampling vs. learned super-resolution (Real-ESRGAN) vs. the paid
route (Topaz Video AI).

Commands below ran on this box (WSL2, ffmpeg 4.4.2) against a synthetic 1280×720/24fps clip and a
1376×768 still standing in for Flow output; TESTED means run here. Nothing needing Vulkan/ncnn or
a licensed app was run — marked UNTESTED, a setup task rather than a one-liner.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Rotation/dutch-angle drift on a clip or still | `rotate` | angle in radians, `t`-driven expr for a slow tilt | free |
| Perspective correction or a fake keystone push | `perspective` | remap the 4 corners, `sense=source` or `destination` | free |
| Parallax from layered cutout PNGs | `overlay` + independent `crop`/pan per layer | fg layer pans faster than bg layer, same duration | free |
| Remove unwanted shake, best quality | `vidstabdetect` → `vidstabtransform` (libvidstab, two-pass) | pass 1 writes a `.trf`, pass 2 warps against it | free |
| Remove shake, one-pass, cruder/faster | `deshake` | single filter, no analysis file | free |
| True slow-mo (synthesise, don't duplicate) | `minterpolate mi_mode=mci` | motion-compensated interpolation | free, slow |
| Cheap fps conversion, no smear risk | `minterpolate mi_mode=dup` / `fps` filter | duplicates/drops frames only | free, instant |
| Retime a clip's own playback speed | `setpts=PTS/factor` | factor > 1 speeds up, < 1 slows down | free |
| Retime narration/audio speed | `atempo` (chain for extreme ratios) | documented range 0.5–100, quality holds ~0.5–2 | free |
| Fake motion blur on a re-timed or fast move | `tblend`/`tmix` | average/blend N successive frames | free |
| Upscale a still before `zoompan` | `scale flags=lanczos` or `zscale filter=spline36` | resampling only, no detail recovery | free |
| Upscale with learned detail recovery | Real-ESRGAN (`realesrgan-ncnn-vulkan`) | separate binary, needs Vulkan; NOT installed here | free tool, GPU setup |
| Commercial upscale + interpolate + stabilise suite | Topaz Video AI | GUI app, Windows/Mac | $299–699/yr |

## Named tools

### `rotate` / `perspective`
Core libavfilter filters. `rotate`: angle in radians, constant or `t`-varying, with
`fillcolor`/`bilinear` options. `perspective`: remaps the four corners via `x0..x3/y0..y3`,
`sense=source|destination`. **Free**, ffmpeg core, seen 2026-08-21, any platform ffmpeg runs on,
no install beyond ffmpeg. Stable plumbing, no reputation issues in 2025–26 coverage.

### `vidstabdetect` / `vidstabtransform` (libvidstab)
Two-pass stabiliser: pass 1 analyses motion into a `.trf` file, pass 2 warps against it. **Free**,
LGPL, confirmed compiled in (`--enable-libvidstab`). Linux/Mac via package manager, Windows via a
full/GPL ffmpeg build. Regarded as the closest free equivalent to Premiere's Warp Stabilizer, and
the two-pass design generally beats single-pass `deshake` on real camera shake.

### `deshake`
Single-pass stabiliser — rectangular motion search against the previous frame, no analysis file.
**Free**, ffmpeg core, seen 2026-08-21. Faster than vidstab, fewer knobs (no global path
smoothing), cruder result. A `deshake_opencl` variant is also compiled in, GPU-accelerated in
principle but **unverified on WSL2** per the scout notes.

### `minterpolate`
Core motion-interpolation filter, three `mi_mode`s: `dup` (duplicate, instant, choppy), `blend`
(cross-dissolve, instant, can ghost), `mci` (motion-compensated, synthesises real intermediate
frames, far slower). **Free**, ffmpeg core, seen 2026-08-21 — post-production.md §3.7 already uses
it for retime; this brief adds the mode choice and real timing below.

### RIFE (`rife-ncnn-vulkan`)
Neural frame-interpolation binary, ncnn+Vulkan, no CUDA/PyTorch needed. **Free**, MIT-style,
github.com/nihui/rife-ncnn-vulkan, seen 2026-08-21. **Not installed here.** Popular in the
enthusiast slow-motion community (powers SVP) and regarded as sharper than classic optical-flow,
but still liable to warp on complex or low-contrast motion. Needs Vulkan — unproven on this box,
same as OpenCL.

### Real-ESRGAN (`realesrgan-ncnn-vulkan`)
Learned super-resolution binary, ncnn+Vulkan, image-native (video needs an extract/upscale/reassemble
wrapper). **Free**, github.com/xinntao/Real-ESRGAN-ncnn-vulkan, seen 2026-08-21 — actively
maintained (issues through Dec 2025). **Not installed here.** Same Vulkan caveat as RIFE.

### Topaz Video AI
Commercial upscale/interpolate/stabilise suite, GUI-only. **$299/yr Personal or $699/yr Pro,
subscription, seen 2026-08-21** — perpetual licence retired for new buyers October 2025; a lapsed
subscription locks the app entirely. Windows/Mac — the Premiere edit box already runs Windows 11,
sidestepping the WSL2 GPU question. Reviewed as the commercial standard for this category in
2025–26 coverage, at real recurring cost.

### `tblend` / `tmix`
Core temporal-blend filters — `tblend` blends each frame with the previous (`average` for a blur
look), `tmix` averages a windowed N frames with weights. **Free**, ffmpeg core, seen 2026-08-21.

### `scale` (Lanczos) / `zscale` (spline36)
`scale` is libswscale-based (`flags=lanczos`); `zscale` uses `libzimg` for colourspace-aware
resizing (`filter=spline36`). Both **free**, ffmpeg core; `zscale` confirmed compiled in
(`--enable-libzimg`). Neither recovers detail — both resample, same softness math as §4.

## Automation hook

**Premiere side.** Warp Stabilizer's match name is **`AE.ADBE SubspaceStabilizer`** (per Adobe's
Premiere Effect Component documentation — a v12-era snapshot, not this exact 26.3.2 build, so
re-check against `VideoFilterFactory.getMatchNames()` before relying on it). Rotation/scale as a
discrete effect has no confirmed match name here — discovery step: filter installed effects for
`"Transform"`/`"Basic 3D"`. **Time remapping / speed ramps are not a `VideoFilterFactory` effect at
all** — they live on the clip's own speed/duration and Time Interpolation properties (Frame
Sampling / Frame Blending / Optical Flow), so the bridge needs to target that clip component, not
an effect match name.

**ffmpeg side** — skeletons only, all TESTED on this box unless marked otherwise:

```
ffmpeg -i in.mp4 -vf "rotate=0.02:c=black" out.mp4                       # rotate
ffmpeg -i in.mp4 -vf "perspective=x0=0:y0=0:x1=W-20:y1=10:x2=0:y2=H:x3=W:y3=H-10" out.mp4
ffmpeg -loop 1 -i bg.png -loop 1 -i fg.png -filter_complex \             # parallax
 "[0:v]crop=1280:720:x='(in_w-1280)*t/8'[bgc];
  [1:v]crop=1280:720:x='(in_w-1280)*t/8*1.6'[fgc];[bgc][fgc]overlay[v]" -map "[v]" out.mp4
ffmpeg -i in.mp4 -vf vidstabdetect=shakiness=8:result=t.trf -f null -    # vidstab pass 1
ffmpeg -i in.mp4 -vf "vidstabtransform=input=t.trf:zoom=0:smoothing=10" out.mp4  # pass 2
ffmpeg -i in.mp4 -vf "deshake=rx=32:ry=32" out.mp4                       # single-pass stab
ffmpeg -i in.mp4 -vf "setpts=PTS/0.6,minterpolate=fps=25:mi_mode=mci" out.mp4  # true slow-mo
ffmpeg -i in.mp4 -vf "tblend=all_mode=average" out.mp4                   # motion blur
ffmpeg -i in.mp4 -vf "tmix=frames=3:weights='1 2 1'" out.mp4             # motion blur, windowed
ffmpeg -i still.jpg -vf "scale=2752:1536:flags=lanczos" up.png           # resample upscale
ffmpeg -i still.jpg -vf "zscale=w=2752:h=1536:filter=spline36" up2.png   # colourspace-aware
ffmpeg -i in.wav -filter:a "atempo=1.6667" out.wav                       # audio retime

realesrgan-ncnn-vulkan -i frame.png -o up.png -n realesrgan-x4plus       # UNTESTED, not installed
rife-ncnn-vulkan -0 f1.png -1 f2.png -o mid.png                          # UNTESTED, not installed
```

**Measured timings on this box**, 8s 1280×720 clip, CPU only: `vidstabdetect` 0.7s,
`vidstabtransform` 1.4s, `deshake` 2.9s, `minterpolate mi_mode=dup` 0.7s, `mi_mode=blend` 1.0s,
**`mi_mode=mci` 37.8s** — roughly 4.7× the clip's own duration, wall-clock, per 8s→13.2s retime.
Budget accordingly for a whole scene; `mci` is not close to realtime on this hardware.

## BadCode fit

**Stabilisation solves a problem BadCode mostly doesn't have.** Veo's camera is generative and
mostly locked-off or a deliberate dolly by prompt, not handheld — vidstab/deshake exist for
human-operator wobble. Test on a real take first; if needed, both `vidstabtransform`'s `zoom` and
`crop=black` eat into the resolution headroom §4 already treats as scarce — a real trade, not a
free fix.

**`mci` interpolation is a genuine risk on the near-black register.** Motion estimation needs
contrast to find matching blocks — `vidstabdetect`'s own `mincontrast` option exists to *discard*
low-contrast regions for that reason, and the same class of problem applies to `minterpolate`'s
motion search on a dim, muted-palette frame. Expect smear or blocking in shadow-heavy footage;
check a contact-sheet frame (§3.9, exposure-lifted) before trusting any `mci` output.

**Upscaling has no free lunch here either.** `scale`/`zscale` are resampling, not detail recovery —
same softness curve as §4's table. Real-ESRGAN/RIFE are the genuinely unexplored routes (Vulkan
never confirmed on this WSL2 box). Topaz sidesteps that by running natively on the Windows 11 edit
box already in the pipeline — worth one live trial before ruling any upscale route in or out.

**Parallax needs alpha-channel layers Flow doesn't produce.** Veo/Nano Banana output is flat video
or a flat still — this only applies once there's a separately-composited cutout asset, not to raw
Flow output as-is.

## Traps

- `vidstabtransform`'s default `crop=keep` leaves visible borders; `crop=black` is explicit but
  then needs `zoom` budgeted to hide it — resolution that doesn't come back.
- `mi_mode=mci` is not fast — 37.8s wall-clock for one 8s clip here. Never assume near-realtime.
- `atempo`'s documented range is 0.5–100, but quality degrades outside roughly 0.5–2×; chain
  multiple stages for a bigger ratio rather than one extreme value.
- `zscale` respects colourspace/transfer characteristics via `libzimg`; `scale` does not — prefer
  `zscale` for anything graded afterward (see the colour-grading brief).
- RIFE/Real-ESRGAN need a Vulkan driver check and a binary download, not `apt install` — a real
  setup task, not a one-liner alongside the native filters.
- Topaz's licensing changed under everyone in October 2025: no one-time purchase for new users —
  carry the $299–699/**year**, not a one-off cost.

## Sources

- https://ffmpeg.org/ffmpeg-filters.html — accessed 2026-08-21 — confirms vidstab/minterpolate/tblend
- https://github.com/nihui/rife-ncnn-vulkan — accessed 2026-08-21 — RIFE ncnn-vulkan binary source
- https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan — accessed 2026-08-21 — actively maintained through 2025–26
- https://costbench.com/software/ai-video-generators/topaz-video-ai/ — accessed 2026-08-21 — $299/$699 per year pricing
- https://helpx.adobe.com/si/premiere-pro/how-to/stabilize-handheld-footage.html — accessed 2026-08-21 — official Warp Stabilizer usage doc
- https://premiereonscript.com/wp-content/uploads/2018/03/Premiere-v12-Effect-Documentation.pdf — accessed 2026-08-21 — Warp Stabilizer match name, dated snapshot
