# The hybrid method — Veo animates the world, post moves the camera

> **🔴 Ruled 2026-08-26 (Kai): the lanes are LAYERS, not alternatives.**
> *"Veo is really good at animating things in a scene, and then we could do camera work inside
> Premiere. Let's make sure we've incorporated ffmpeg in that setup as well."*
>
> Every previous version of the lane table asked *which one*. That is the wrong question on any
> shot that needs both a living world and a moving camera — which is most of them. **Ask what each
> layer owns, then build all three.**

---

## 1. The stack

| Layer | Owns | Never asked to do |
| --- | --- | --- |
| **Veo (Flow)** | **The world moving inside a frame that never moves.** Fans turning, LEDs storming, plumes rising, cloth, water, crowds, faces, a machine working | Move the camera. Hold text legible through a move. Hit a timing mark |
| **Premiere** | **The camera, the cut and the grade** — keyframed push/pan/parallax, dissolves, the effect catalogue, compositing, anything a human iterates on by eye | Anything needing a string typed by the API (see §6). Blend modes by tool call |
| **ffmpeg** | **Anything that must be exact, procedural or headless** — timing maths, per-pixel effects, real blend modes, chaining, conform, delivery | Anything a person wants to nudge by eye |

**The order is Veo → Premiere → ffmpeg, but not strictly.** ffmpeg often runs first (building a
card, a plate, a chained source) and always runs last (the delivery encode and QC).

## 2. Why locking Veo's camera is the whole trick

Veo's most expensive failure mode is **regeneration**: as objects leave and enter frame it invents
their replacements, and it invents different ones. Measured on GPOM plant-room, 2026-08: a camera
travelling past ranks of server cabinets was clean at 0–4s and visibly broken by 6s. The same
model, holding still, is reliable.

**The failure is caused by camera translation, not by the subject.** So:

- **Lock the camera in the prompt** and Veo has almost no new geometry to invent. The bug cannot
  fire.
- **Do the move in post**, where it is a scale-and-crop on real pixels: rigid by construction,
  any length, exact easing, free, instant to re-try.

You get the smoke *and* the camera move, and neither tool is asked for the thing it is bad at.

**This subsumes the old §1 question in [`post-production.md`](../flow/post-production.md)** ("does
anything in the world move, or only the camera?"). That table is still right about a
camera-only move — it just stopped short. The full answer is:

| Does the world move? | Does the camera move? | Build |
| --- | --- | --- |
| no | no | one still, held. Add `Camera Shake` at Master ~10 so it reads as a camera, not a scan |
| no | yes | **post only** — no credit spent |
| yes | no | **Veo only**, locked camera |
| **yes** | **yes** | **🟢 the hybrid — Veo locked, then move the camera over the finished clip** |

## 3. Build order

1. **Settle the look as a still.** Non-negotiable and unchanged — see the stills-first rule in
   `flow-automation`. The plate is the contract.
2. **Name what moves in the world.** If nothing does, stop; this is a post shot.
3. **Generate in Veo with the plate as `startImage`, prompting motion only, camera explicitly
   locked.** Say *"the camera does not move"* — Veo drifts 34–66px over 8s even when told to hold,
   so a locked-off beat still gets stabilised or cropped in post.
4. **Design the camera move against the finished clip**, in Premiere on the `Motion` intrinsic
   (params `0 Position`, `1 Scale`, `5 Anchor Point` — all 0–1 fractions of frame), or in ffmpeg
   `zoompan` when the easing must be exact and repeatable.
5. **Layer the effects.** Catalogue: [`../premiere/effects-catalogue.md`](../premiere/effects-catalogue.md).
   ffmpeg-only capabilities: §6 below.
6. **Grade and grain last**, then the delivery gate ([`delivery.md`](delivery.md)).

### Make the move not read as a slideshow

A linear zoom on a still is the thing everyone means by "slideshow". Four fixes, and it is the
combination that works:

- **Hold first.** Give the frame 1–2s of real stillness before anything moves. A move that starts
  on frame 1 reads as a scan.
- **Ease, never ramp.** Accelerate in, decelerate onto the destination.
- **Parallax, not zoom.** Split the plate into depth layers and move them at different rates. A
  zoom magnifies a flat picture; parallax is the only thing that reads as *dimension*.
- **Two rates of change.** Something must change independently of the camera — a light travelling,
  a flicker, an element entering. One thing changing is a zoom; two is a shot.

And give the move a **destination** — something worth arriving at, ideally the frame that becomes
the next cut.

## 4. 🔴 Eight seconds is not a limit — chain the frames

**Standing rule: never shorten a beat because Veo caps at 8 seconds.** The cap is a per-generation
limit, not a shot limit.

**The mechanism.** Take the last frame of clip N and use it as the first frame of clip N+1. Each
clip starts from a real frame, so each stays rigid, and the join is invisible because the two
frames are identical.

```bash
# pull the last frame out of a clip
ffmpeg -sseof -0.05 -i clipN.mp4 -update 1 -frames:v 1 -q:v 2 lastframe.jpg
```

Inside Flow, `flow_scene_save_frame position:"end"` does the same and lands the frame in the
project as an asset — use that when the next generation needs to reference it.

**🔴 Chain, do not pin an end frame.** Frames-to-Video *interpolates between two pictures* — it is
a morph tool and Google documents it as one. Every inconsistency between the two images has to be
animated away somewhere, and that shows up as joins sliding and structures deforming. Measured on
GPOM scene 0: identical prompt and start image, the only change being `endImage` removed, went
from *"joins slide and deform throughout"* to *"completely rigid."* **Chaining buys rigidity;
pinning buys arrival.** Full write-up: [`../flow/video-prompting.md`](../flow/video-prompting.md) §4.

**The reversed variant, for a pull-back that lands exactly on an art-directed plate.** Proven on
GPOM scene 0, 2026-08-21 — a 16s continuous rigid pull-out. Shoot *push-ins* from the frame you
want to arrive at, chain them, then reverse each and concatenate in reverse order. Recipe:
[`../flow/post-production.md`](../flow/post-production.md) §3.4b.

⚠️ **A reversed clip only reads if nothing physical settles.** Dust, sparks, smoke and drifting
debris all read as running backwards. Blinking lights are safe — they are time-symmetric.

⚠️ **Normalise fps and SAR before any concat.** Veo returns 24fps; anything ffmpeg builds from a
still defaults to 25. Mixing them makes the join drift. §3.6 of `post-production.md`.

## 5. What we actually have in ffmpeg

Audited live **2026-08-26**, ffmpeg **4.4.2** (Ubuntu 22.04, WSL): **477 filters**, built with
`--enable-frei0r --enable-libvidstab --enable-ladspa --enable-lv2 --enable-libzmq --enable-opencl
--enable-frei0r --enable-libx264/x265/vpx/aom/dav1d`.

**Yes, ffmpeg has plugins.** `frei0r` is the big one — **~110 plugins** in `/usr/lib/frei0r-1/`,
callable as `-vf frei0r=<name>:<params>`. Verified working 2026-08-26: `frei0r=glow:0.5` and
`frei0r=scanline0r`.

Ones worth knowing, by what you would ask for:

| Want | frei0r plugin |
| --- | --- |
| CRT scanlines | `scanline0r` |
| Analogue sync failure / roll | `nosync0r` · `nervous` · `baltan` · `delaygrab` |
| Digital corruption | `glitch0r` · `tehroxx0r` |
| Bloom | `glow` · `softglow` · `edgeglow` |
| Light-painting trails | `lightgraffiti` |
| Lens / geometry | `defish0r` · `perspective` · `c0rners` · `scale0tilt` · `distort0r` |
| Keying and spill | `bluescreen0r` · `keyspillm0pup` · `spillsupress` · `select0r` |
| Grade | `curves` · `levels` · `three_point_balance` · `sopsat` · `primaries` · `balanc0r` |
| Procedural texture | `plasma` · `partik0l` · `ising0r` · `cluster` · `lissajous0r` |
| Vignette / mask | `vignette` · `mask0mate` · `alphagrad` · `alphaspot` |

### What ffmpeg does that Premiere cannot

This is the list that matters, because it is the reason ffmpeg stays in the stack rather than
being a conform step.

| Capability | Filter | Why Premiere can't |
| --- | --- | --- |
| 🟢 **Real blend modes by tool call** | `blend=all_mode=screen\|overlay\|multiply…` | Premiere's blend mode lives on the Opacity intrinsic and **the API cannot enumerate or reliably set the integers** — Screen has never been measured. In ffmpeg it is a named string. ✅ verified 2026-08-26 |
| 🟢 **Arbitrary per-pixel maths with a time variable** | `geq` (`X`,`Y`,`T`,`r(x,y)`) | No equivalent. This is procedural flicker, light sweeps, gradients that move — anything you can write as an expression. ✅ verified 2026-08-26 |
| 🟢 **Text with exact typing/timing** | `drawtext` + `enable='gte(t,…)'` | 🔴 **Premiere's API cannot write a string at all** — `SimpleText` and MOGRT both throw `Illegal Parameter type`. Render the card in ffmpeg. ✅ verified 2026-08-26 |
| 🟢 **Flash-safety compliance** | `photosensitivity` | Nothing equivalent. **Run it on any strobing or alarm sequence before delivery.** ✅ verified 2026-08-26 |
| 🟢 Displacement / remapping by a map image | `displace` · `remap` | Premiere has no displacement-map effect |
| 🟢 Timed parameter changes mid-render | `sendcmd` · `zmq` | Keyframes only, by hand |
| 🟢 Remove Veo's frame-to-frame luminance wobble | `deflicker` | No equivalent |
| 🟢 Two-pass stabilisation, headless | `vidstabdetect` + `vidstabtransform` | Warp Stabilizer needs the GUI and an analysis pass you cannot trigger by tool call |
| 🟢 Optical-flow retime | `minterpolate` | Premiere's Optical Flow is GUI-driven |
| 🟢 Denoise | `nlmeans` · `hqdn3d` · `atadenoise` | Only the VR denoiser is installed |
| 🟢 Measurement and QC | `signalstats` · `scdet` · `freezedetect` · `blackdetect` | Scopes are for looking at, not for asserting on |
| 🟢 Procedural sources | `gradients` · `cellauto` · `life` · `mandelbrot` · `noise` | No generators |
| 🟢 50+ headless transitions | `xfade` | Fine in Premiere, but not scriptable |

**And the reverse — what Premiere does that ffmpeg cannot** is just as load-bearing: 106 effects
and 118 transitions with a real-time preview, `Volumetric Rays` with a keyframeable light
position, `Strobe`, `Echo Glow` and `Camera Shake` that animate on their own, and a human who can
look at it and say no.

## 6. When the hybrid is the wrong answer

- **The camera move is the only movement.** Post only. Don't spend a credit.
- **The subject must stay rigid through a big scale change.** Chain push-ins and reverse them
  (§4) — Veo cannot hold rigidity through a pinned pull-back.
- **The thing really happened.** Source it — `find-footage`. Inventing it is worse and a lie.
- **It needs true 3D or planar tracking.** After Effects is not installed. Say so; don't design
  around it.

## 7. Worked example — GPOM cut 3, the plant room

Designed **2026-08-26**; the first full application of the method. Eight beats:

| Layer | Beats |
| --- | --- |
| **Veo, locked camera** | fan turning behind a louvre grille · LED storm down a rack aisle · rack lights up a vertical shaft · control-room console alive with no operator · gauge needles drifting · a control room in red-alert · vent plumes across a field of towers |
| **Premiere** | every camera move · `Volumetric Rays` with light position keyframed bottom-to-top so a beam climbs the shaft on an exact frame · `Strobe` in black-mode with random probability as a dying fluorescent · `Motion` param 4 rotating needle PNGs about a moved anchor · grade · grain in shadows only |
| **ffmpeg** | the typed `2032` card (`drawtext`, per-character `enable`) · frame chaining for the four beats over 8s · `photosensitivity` on the red-alert beat · conform and delivery |

**Nothing here was built when this file was written.** Record what actually happened in
[`../stories/gitpush-origin-master/scenes/plant-room.md`](../stories/gitpush-origin-master/scenes/plant-room.md)
and bring the corrections back to this file.

---

## Where this connects

- [`README.md`](README.md) — lane choice. **The lanes in that table compose; this file says how**
- [`../flow/post-production.md`](../flow/post-production.md) — the ffmpeg recipe book, all run on
  real BadCode footage. §3.4b is the chain; §3.5 pulls a last frame
- [`../flow/video-prompting.md`](../flow/video-prompting.md) §4 — why pinning an end frame deforms
  a rigid subject
- [`../premiere/effects-catalogue.md`](../premiere/effects-catalogue.md) — the 106 effects and 118
  transitions, with measured parameter indices
- [`../cinematography/motion-and-cutting.md`](../cinematography/motion-and-cutting.md) — whether
  the shot should move at all. **Decide that before this file, not after**
- [`delivery.md`](delivery.md) — the QC gate. `scripts/delivery-qc.sh` before anything ships

**Provenance.** Method ruled by Kai 2026-08-26. The ffmpeg audit, the frei0r inventory and the six
✅ capability checks were run live on this machine the same day. The Veo regeneration measurement
is from the GPOM plant-room shoot; the chained-reversed pull-out is from GPOM scene 0, 2026-08-21.
