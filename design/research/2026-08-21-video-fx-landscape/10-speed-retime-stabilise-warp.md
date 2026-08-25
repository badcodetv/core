# Speed, retime, optical flow, stabilisation, morphing

## What this covers

Retiming a clip (speed ramps, slow-mo, freeze, reverse), the three ways Premiere invents frames it
doesn't have (Frame Sampling / Frame Blending / Optical Flow) and how they hold up on AI-generated
source, stabilising a shot (native Warp Stabilizer vs paid planar/gyro tools), and Morph Cut's
face-aware cross-dissolve. **Reverse, ping-pong looping, eased zoompan retime, and the resolution
ceiling are already in [`docs/flow/post-production.md`](../../../docs/flow/post-production.md)
§3.2–3.7 — not repeated here, only cited**, with additions the book doesn't cover: freeze frame,
planar/gyro stabilisation, `minterpolate` mode nuance, and the paid third-party tier.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Eased speed ramp inside one clip | Time Remapping (native) | *Show Clip Keyframes → Time Remapping → Speed*, drag rubber-band, add Bezier ease | included (CC) |
| Cheap speed change, near-static footage | Frame Sampling (native) | Default Time Interpolation mode — duplicates/drops frames, no analysis | included (CC) |
| Smoother slow-mo, moderate motion | Frame Blending (native) | Time Interpolation dropdown — cross-dissolves adjacent frames | included (CC) |
| Best-quality slow-mo, synthesised frames | Optical Flow (native) or Twixtor | *Time Interpolation → Optical Flow* (GPU); Twixtor for harder cases | included / £595 |
| Stabilise camera drift / rolling shutter | Warp Stabilizer, ffmpeg `libvidstab`, or Mercalli V6 | Drag effect onto clip, background-analyses, four Method tiers | included / free / ~£199–299 |
| Gimbal-grade stabilisation from gyro telemetry | ReelSteady | Needs a GoPro's recorded gyro metadata — **none exists on AI footage** | ~£99/yr |
| Seamless cut across two takes of one face | Morph Cut (native) | *Video Transitions → Dissolve →* drag onto the cut; face-tracking only | included (CC) |
| Reverse a clip | ffmpeg `reverse` | See `post-production.md` §3.2 | free |
| Freeze on a frame | ffmpeg `tpad` | Clone the last/first frame for N seconds | free |
| Stretch past the 8s Veo cap | ffmpeg `setpts`+`minterpolate` | See §3.7; mode choice matters more than shown there | free |

## Named tools

### Time Remapping (native Premiere)
Clip-level speed keyframing with Bezier ease handles, distinct from the simpler Speed/Duration
dialog. **Included** with Creative Cloud, no separate licence, Windows/Mac, built in, no install.
Reputation: functional but resented — a live 2026 Adobe Community feature request titled "Speed
Ramping in 2026: Premiere Pro Is Falling Behind" argues DaVinci Resolve and Final Cut do this with
fewer clicks and better curve handles.

### Time Interpolation: Frame Sampling / Frame Blending / Optical Flow (native)
Three modes in one dropdown (Clip Speed/Duration dialog). Frame Sampling repeats/drops frames
only; Frame Blending cross-dissolves neighbours; Optical Flow analyses motion vectors and
generates new in-between frames — best quality, GPU-hungry, and the one that can hallucinate
warped limbs or ghosting on fast/complex motion. **Included** with CC. Reputation (2025–26
tutorials, Filmora/WinX): Optical Flow for "clear cinematic or sports movement," Frame Blending
for quick soft slow-mo, Frame Sampling for time-lapse or minimal motion.

### Warp Stabilizer (native Premiere)
Four Method tiers, tried in order until enough trackable area exists for the one requested:
Subspace Warp (default, warps regions independently) → Perspective (whole-frame corner-pin) →
Position, Scale, Rotation → Position only. Also exposes Smoothness and four Framing modes
(Stabilize-only / Crop-Auto-scale / Crop-Fixed / Synthesize-Edges). **Included** with CC.
Reputation: the industry default, but the two-pass background analysis is slow and Subspace Warp
is the mode most likely to smear a moving subject against a static background (see Traps).

### Morph Cut (native Premiere)
A video transition (Effects → Video Transitions → Dissolve → Morph Cut), not a clip effect. Uses
face tracking + frame interpolation to blend two takes of the same face across a jump cut. Best on
wide, low-movement single-face shots; Adobe helpx (updated 2026-01-07) documents it as unreliable
on tight crops that clip the face, and 2026 Community threads report project-specific crashes.
**Included** with CC.

### Twixtor Pro (RE:Vision Effects)
**$595 USD, perpetual licence, optional paid upgrades** (revisionfx.com, accessed 2026-08-21).
Current version V8. Mac + Windows; plugs into Premiere Pro, After Effects, Media Composer, FCP.
Standard plugin installer, appears as a clip effect once installed. Reputation: the long-standing
gold standard for motion-estimation retiming — reviewers reach for it when native Optical Flow
warps too much on complex or fast motion.

### Mercalli V6 SAL (proDAD)
Pricing is **inconsistent across the vendor's own channels**, the same pattern the scout flagged
for Red Giant Universe. Reseller/coupon pages show $299 list with a 25%-off promo ($224.25);
prodad.com's own product page implies an MSRP nearer $199 for the Windows edition but the exact
figure sits behind a third-party checkout link (accessed 2026-08-21 — gap, not first-party
confirmed). Windows only. Ships as a standalone app *and* as plugins for Premiere Pro, DaVinci
Resolve, MAGIX, EDIUS, Vegas. Reputation: praised for CMOS rolling-shutter correction beyond what
Warp Stabilizer attempts.

### ReelSteady (GoPro)
**~$99/year** as a Premiere Pro plugin per a 2026 pricing summary; GoPro's own desktop app
("GoPro Player + ReelSteady") separately lists a **$99.99 one-time in-app purchase** for the same
module (source conflict, both accessed 2026-08-21 — flagged, not silently resolved). Windows/Mac.
Reputation: the reference tool for GoPro gyro-assisted stabilisation, beating general-purpose
stabilizers *only when gyro telemetry exists* — it does not on generated footage (see BadCode fit).

### ffmpeg `minterpolate` / `libvidstab` (free, already in the toolchain)
Ships in the WSL ffmpeg 4.4.2 build already in use (`--enable-libvidstab` confirmed via
`ffmpeg -version`). `minterpolate` is the free answer to Frame Sampling/Blending/Optical Flow;
`libvidstab`'s two-pass `vidstabdetect`/`vidstabtransform` is the free answer to Warp Stabilizer's
Position/PSR/Perspective tiers (no Subspace-Warp equivalent exists in ffmpeg).

## Automation hook

**Premiere side.** No public source confirmed a literal match-name string for any of these before
this session's search budget ran out — flagged as a gap, not asserted:

| Effect/transition | Type | Discovery step for the UXP bridge |
| --- | --- | --- |
| Warp Stabilizer | standard clip effect | `VideoFilterFactory.getMatchNames()`, filter for `"warp"` |
| Morph Cut | standard video transition | Transitions carry match names too; filter the transitions list for `"morph"` |
| Time Remapping / Time Interpolation | **clip property, not an effect** | Not reachable via `VideoFilterFactory` — lives on the `TrackItem`'s speed/keyframe data. Needs Premiere's scripting API (`TrackItem` speed methods), not the match-name route. **Gap: confirm which UXP/ExtendScript call exposes clip speed keyframes.** |
| Twixtor / Mercalli plugin effects | third-party, once installed | Same `getMatchNames()` filter by vendor name, after confirming the plugin loads under UXP |

**ffmpeg side.**

Freeze frame — **TESTED** (scratchpad, 1376×768 24fps synthetic clip):
```bash
ffmpeg -i in.mp4 -vf "tpad=stop_mode=clone:stop_duration=1" -an out.mp4
```

Two-pass stabilisation (the free Warp-Stabilizer-equivalent) — **TESTED**:
```bash
ffmpeg -i in.mp4 -vf vidstabdetect=shakiness=5:accuracy=15:result=transforms.trf -f null -
ffmpeg -i in.mp4 -vf vidstabtransform=input=transforms.trf:smoothing=30:zoom=0:optzoom=1 -an out.mp4
```

Retime quality-mode comparison (extends `post-production.md` §3.7, same base command, three
`mi_mode` values) — **TESTED**, all three ran clean on the 2s synthetic clip:
```bash
ffmpeg -i in.mp4 -vf "setpts=2.0*PTS,minterpolate=fps=24:mi_mode=dup"  -an out_dup.mp4    # = Frame Sampling
ffmpeg -i in.mp4 -vf "setpts=2.0*PTS,minterpolate=fps=24:mi_mode=blend" -an out_blend.mp4 # = Frame Blending
ffmpeg -i in.mp4 -vf "setpts=2.0*PTS,minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:vsbmc=1" -an out_mci.mp4 # = Optical Flow
```
Reverse, ping-pong loop, and the base retime skeleton: see `post-production.md` §3.2, §3.3, §3.7 —
not repeated here.

## BadCode fit

All source is **Veo 3.1, fixed at 24fps, 8s max, 1376×768 stills / 1280×720 video** — this changes
what each tool is *for* here versus a real-camera edit:

- **ReelSteady and any gyro-driven stabiliser are not applicable** — no camera, no gyro telemetry.
- **Optical Flow / Twixtor / `minterpolate mci` retiming is higher-risk on AI footage than on real
  footage.** These tools assume the motion they interpolate is physically real; Veo's own known
  artefact is implausible motion at the frame level, and motion-estimation invents *more* frames
  from already-uncertain motion. Contact-sheet every retimed AI clip (`post-production.md` §3.9)
  before trusting it. **Gap: no source found benchmarking Optical Flow on AI-generated vs
  camera-shot source — don't assert it behaves the same.**
  The 60fps-source slow-mo workaround some 2026 sources note for other models (Kling 3.0) does not
  apply — Veo 3.1 is fixed at 24fps generation, so any slow-mo comes from interpolation (risk
  above) or from post's eased zoompan on a still, which has no motion to misread at all.
- **Warp Stabilizer is mostly moot on near-black locked-off panel shots** — nothing to track, and
  its strongest use case (handheld drift) doesn't occur in footage never shot with a camera. It
  matters only where a *prompted* camera move needs to read smoother than it generated.
- **Morph Cut is a poor fit for the visual register** — its value is bridging near-identical takes
  of one real face; BadCode panels are wide, monumental-machine, near-black, rarely the tight
  talking-head cut it was built for.
- **Time Remapping/retime is the one genuinely useful category here**, to buy length past the 8s
  cap (`post-production.md` §3.7) — this brief's addition is choosing `mi_mode` deliberately
  rather than defaulting to `mci` everywhere.

## Traps

- **A stalled `minterpolate` render is genuinely slow, not blocked** — don't mistake it for a Flow
  policy-block-as-timeout (that's a Flow-side failure mode, unrelated here).
- **Warp Stabilizer + Time Remapping cannot be applied to the same clip directly** — multiple
  2025–26 Adobe Community threads confirm the fix is nesting: stabilise first, apply Time
  Remapping to the nested sequence.
- **Mercalli and Twixtor prices are not stable across a vendor's own pages** — the same pattern
  the scout flagged for Red Giant Universe. State source and date; don't silently normalise.
- **`minterpolate` is single-threaded** (ffmpeg community sources) — fine at 8s, plan for it above.
- **Optical Flow needs GPU acceleration to be interactive**; CPU-only, it can be far slower than
  Frame Blending for a similar-looking result on simple motion.

## Sources

- [Time interpolation methods — Adobe Premiere Pro Help](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/apply-time-interpolation-methods-to-adjust-clip-speed.html) — 2026-08-21 — defines the three modes
- [Warp Stabilizer settings — Adobe Premiere Pro Help](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/warp-stabilizer-settings.html) — 2026-08-21 — Method tiers, Framing options
- [Morph Cut overview — Adobe Premiere Pro Help](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/morph-cut-overview.html) — 2026-08-21 — face-tracking limits, updated Jan 2026
- [Twixtor — RE:Vision Effects](https://revisionfx.com/products/twixtor/premiere-pro) — 2026-08-21 — $595 perpetual, V8
- [Mercalli V6 SAL — proDAD](https://www.prodad.com/Video-Stabilization-for-Professionals/Mercalli-V6-SAL-97864,l-us.html) — 2026-08-21 — standalone plus NLE plugin
- [Speed Ramping in 2026 — Adobe Community](https://community.adobe.com/feature-requests-730/speed-ramping-in-2026-premiere-pro-is-falling-behind-1621274) — 2026-08-21 — live UX complaint thread
- [minterpolate filter — FFmpeg docs, verified via local 4.4.2](https://ffmpeg.org/ffmpeg-filters.html#minterpolate) — 2026-08-21 — mi_mode dup/blend/mci
- [State of AI Video Generation, Feb 2026 — Medium/Cliprise](https://medium.com/@cliprise/the-state-of-ai-video-generation-in-february-2026-every-major-model-analyzed-6dbfedbe3a5c) — 2026-08-21 — Veo 3.1 fixed 24fps
