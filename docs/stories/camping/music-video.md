# Camping — music video (Premiere cut)

The Premiere cut of the "Camping" track, built by Kai on the bridge. Distinct from the
story video in [`story.md`](./story.md#storyboard--scene-by-scene-video-guide), which is
Jack's and is shot from the storyboard.

## Premiere

**Project:** `/mnt/d/badcode-videos/camping-music/camping.prproj`
**Sequence:** `camping` — 1920×1080 @ 25 fps, 236.4s, one sequence in the project
**Read:** 2026-08-24 by session (bridge). **Nothing in this cut was built by the session** —
it is Kai's hand cut; the session only surveyed it and ran an effect trial.

| Track | Clips | Span | What |
| --- | --- | --- | --- |
| V1 | 0 | — | empty |
| V2 | 10 | 22.28 → 43.56 | `12/6/4/8/13/10.mp4` |
| V3 | 35 | 0 → 27.52 | the flicker track — mostly `clips/2.mp4`, plus `badcode guy/8.mp4` holds |
| V4 | 13 | 1.48 → 43.56 | `badcode guy/8,9.mp4` · `bob rapping/1,1.1,2.mp4` |
| A1–A5 | 60 | various | **all muted** |
| A6 | 1 | 0 → 236.4 | the only live audio |

**Picture ends at 43.56s of a 236.4s sequence.** Everything after is music over black.
Zero transitions on 58 video clips — all hard cuts. One unnamed marker at 22.08s.

### The flicker, measured

V3 carries four dense flicker runs — **0→1.44s, 5.6→6.84s, 11.2→12.2s, 18.4→19.12s** — plus a
sparser tail at 19.24–20.84. Built entirely by **hand cutting**, no effect on any clip
(Opacity + Motion intrinsics only). The pattern:

```
v2:0  on=4f          v2:4  on=4f  gap=0f
v2:1  on=4f  gap=1f  v2:5  on=4f  gap=1f
v2:2  on=3f  gap=1f  v2:6  on=3f  gap=1f
v2:3  on=4f  gap=1f  v2:7  on=4f  gap=1f
```

🟢 **V4 is deliberately empty under every flicker run** — its clips end exactly where a run
begins (v3:2 ends 11.2, run starts 11.2). So the gaps read as **black**, not as the layer
below. That is structure, not accident, and it is what makes the effect a strobe rather than
an intercut.

### Findings

- 🔴 **Posterize Time is NOT this effect.** It holds frames — motion goes chunky, the picture
  never leaves. It cannot produce the black gaps. Different tool for a different job.
- ✅ **`AE.ADBE Strobe` in mode 0 with Strobe Color set to black reproduces it in one effect** —
  proven live on `v2:8`, frame exported and measured at 1 unique colour, `#000000`.
  `params: { "0": {r:0,g:0,b:0}, "2": 0.04, "3": 0.2, "5": 0 }` = 1 black frame in 5 at 25 fps.
  Full parameter table and the mode-1 trap: [`../../premiere/api-notes.md`](../../premiere/api-notes.md).
- ⚠️ **The trade-off is regularity.** Strobe Light is uniform; the hand cut is 4f/4f/3f/4f with a
  dropped gap. That irregularity is the feel, and a periodic strobe flattens it. Recommendation
  on 2026-08-24: use Strobe Light for *new* runs, leave the existing four alone.

### 🔴 Photosensitivity — open, needs a human ruling

The flicker is a full-frame flash to black roughly **every 5 frames (~5 per second), sustained
over a second at a time**. The Ofcom / WCAG 2.3.1 threshold is **3 per second**. Four runs
exceed it. Options: stretch to 1-in-8 frames, use a dark frame instead of full black, or
restrict the flicker to part of the frame. **Not decided.**

### Effect trial, 2026-08-24

Nine effects applied one at a time to `v2:8` (`badcode guy/8.mp4`, 2.72→5.6s, unobstructed),
a frame exported at 4.0s, then each effect removed. Timeline returned to exactly 238
components / 2947 params — **as found**.

Contact sheet: `/mnt/d/badcode-videos/camping-music/frames/fx/contact-sheet.png`
(full-res tiles alongside it as `00-baseline.png` … `08-volumetric-rays.png`).

| Effect | Verdict on this plate (a wall of BADCODE monitors, DJ, crowd) |
| --- | --- |
| **Volumetric Rays** | 🟢 **The standout.** Every monitor throws a shaft. Exactly the house register |
| **RGB Split** | 🟢 Strong for D&B, but H=18 is a full psychedelic wash — dial to ~4–6 and keyframe to a snare |
| **Posterize** | 🟢 Crushes to near-black, monitors stay lit. Quietly very BadCode |
| **Turbulent Displace** | 🟡 Melts the monitor wall into a bulge — reads as signal degrading |
| **Find Edges** | 🟡 Inverts to white blueprint. Breaks the near-black register unless chased with Invert |
| **Color Pass** | 🟡 Went near-mono — the default target colour is not in this frame. Needs the colour picked |
| **Wave Warp** | 🔴 Chevrons the monitors. Reads cheap |
| **Mosaic** | 🔴 Loses everything. Only usable as a 2–3 frame stab |

## Effect trial on the live cut — 2026-08-24 (V5 / V6)

The 5.6→6.84s flicker run (V3 clips `v2:9`…`v2:15`) was **cloned twice, unchanged, to V5 and V6
at identical timings** so the treatments can be A/B'd with the track eye icons. **V3 was not
touched** — the original run is intact underneath.

| Track | Clips | Effect | Settings |
| --- | --- | --- | --- |
| **V5** | `v4:0`…`v4:6` | `AE.ADBE Posterize` | defaults |
| **V6** | `v5:0`…`v5:6` | `AE.Impact_RGB_Split_FX` | param **4** (Horizontal Split) = **6** |

**Clone recipe** — `deltaSeconds: 0`, `mode: "overwrite"`, `videoTrackOffset: 2` for V5 and `3`
for V6. Overwrite is load-bearing: `insert` would ripple the whole track. No linked audio was
duplicated (audio clip count held at 61 throughout).

**Verified by exported frame:**

| Frame | Bytes | What it proves |
| --- | --- | --- |
| `frames/fx/run-posterize-5.64.png` | 156,809 | Posterize live (baseline picture is ~760 KB) |
| `frames/fx/run-rgbsplit-5.64.png` | 846,475 | RGB Split live and on top |
| `frames/fx/run-gap-5.78.png` | 9,215 | **The gap is still black** — the flicker survived the clones |

Comparison sheet: `frames/fx/run-compare.png`.

**Read by eye, 2026-08-24:**
- **Posterize on this plate reads as a bold flat-colour poster** — mustard and grey banding on the
  concrete. Note it behaves *differently* here than on the monitor-wall plate, where it crushed
  toward near-black. The plate's brightness decides which you get.
- **RGB Split at 6 is still fairly strong on this shot** — the source already carries motion blur,
  which compounds it. **3–4 is probably the number** if it is meant to read as a hit rather than a
  wash.

⚠️ **V6 sits above V5, so RGB Split wins while both are visible.** Toggle the eye icons to compare.
There is no track-mute tool on the bridge — that toggle is hand work.

🔴 **Not saved.** These edits were live in Premiere and left unsaved on purpose, so the whole trial
can be walked back with undo if it is not wanted.

## Volumetric Rays on the lighting shot — 2026-08-24

The stage/monitor-wall shot ("the lighting up") runs **8.08 → 11.2s** and is cut across two
tracks — `v2:16` on V3 (8.08→9.88) then `v3:2` on V4 (9.88→11.2), both `badcode guy/8.mp4`.
Both halves were cloned to **V5** at identical timings and given Volumetric Rays.

| Track | Clips | Effect | Settings | Span |
| --- | --- | --- | --- | --- |
| **V5** | `v4:7` · `v4:8` | `AE.Impact_Volumetric_Rays_FX` | **defaults** (Intensity 60, Light Position `[0.5, 0.25]`) | 8.08 → 11.2 |

Clone offsets differ because the sources are on different tracks: **+2** for `v2:16` (V3→V5),
**+1** for `v3:2` (V4→V5). Both `mode: "overwrite"`, `deltaSeconds: 0`.

**Verified by exported frame, both halves read by eye:**

| Frame | Bytes | What it shows |
| --- | --- | --- |
| `frames/fx/rays-9.0.png` | 791,633 | wide — full rig, every lamp and monitor throwing a shaft |
| `frames/fx/rays-10.5.png` | 751,968 | tighter — TV-headed DJ silhouetted, crowd back-lit |

🟢 **Defaults are right on this plate** — it was the same source as the 2026-08-24 effect trial,
so the setting was already proven before it was applied.

⚠️ **It lifts the blacks.** Volumetric Fog (param **10**, default 25) hazes the whole frame, which
reads as atmosphere here but is a move away from the near-black register. If the shot needs to sit
back down: drop param 10 toward 10, or Intensity (param **4**) from 60 to ~40. **Not changed** —
the brighter read may well be the right call for a stage shot in a D&B video.

## Second effect trial — the stage plate, 2026-08-24

Run on the clip Kai had selected: **`v2:0` on V3, 3.92→5.72, `badcode guy/8.mp4`** — almost
certainly the rays clone from earlier (same 1.8s duration, same source), moved down to V3 and
repositioned by hand. **Volumetric Rays was removed from it at Kai's request.**

Eight effects applied one at a time, frame exported at **4.8s**, each removed after. Clip returned
to 284 components — as found, no effect on it now.

Contact sheet: `frames/fx2/contact-sheet.png`.

| Effect | Verdict on this plate |
| --- | --- |
| **Echo Glow** | 🟢 **The standout swap for rays.** Lamps smear into hard radiating streaks — same idea, more graphic and more aggressive |
| **VR Digital Glitch** | 🟢 Heavy corruption, RGB fringing, torn blocks. The *transmission is failing* register, straight up |
| **Light Leaks** | 🟢 Washes the whole frame teal/cyan. Not a light effect so much as a **mood change** — good for one moment, not a run |
| **VR Chromatic Aberrations** | 🟡 Rainbow fringing on every edge. Reads as a prism lens; works well *under* something else |
| **Directional Blur** | 🟡 Vertical smear, image essentially gone. **Stab only** — 2–3 frames, or as a pseudo-transition |
| **Wonder Glow** | 🔴 At defaults, barely distinguishable from baseline on this plate |
| **Glint** | 🔴 Slight diffusion haze, no real read |
| **Mirror** | 🔴 Near no-op at defaults — needs its reflection centre and angle set by hand to do anything |

🔴 **Three of the eight do almost nothing at defaults** (Wonder Glow, Glint, Mirror). That is a
property of the defaults, not the effects — but it means "drag it on and look" will read as
*broken* rather than *subtle*. Set their parameters or skip them.

🔴 **The timeline moved between sessions.** V3 dropped 35→27 clips, V6 went 7→20, V5 gained a
transition. **Every clip ref recorded earlier in this file is stale** — re-read before acting on
any of them.

## Echo Glow applied — 2026-08-24

**Accepted by Kai** as the replacement for Volumetric Rays on the stage plate.

| Clip | Track | Span | Effect | Settings |
| --- | --- | --- | --- | --- |
| `v2:0` | V3 | 3.92 → 5.72 | `AE.Impact_Echo_Glow_FX` | **defaults** |

**Verified across the whole clip** — frames at 4.0s, 4.8s and 5.5s, read by eye
(`frames/fx2/echo-across-clip.png`). It holds, and it **animates**: the echo pattern is dense
at the head and calmer by 5.5s, driven by `Speed`.

### Echo Glow — `AE.Impact_Echo_Glow_FX` (35 params), measured 2026-08-24

Real controls start at index 4, per the Impact boilerplate rule.

| Index | Param | Default | What it does |
| --- | --- | --- | --- |
| 4 | **Anchor** | `[0.5, 0.5]` | Where the echoes radiate from |
| 5 | **Steps** | 8 | How many echoes |
| 6 | **Intensity** | 80 | Overall strength |
| 7 | Highlights Only | 60 | Restricts it to the bright areas |
| 8 | **Range** | 75 | How far the echoes throw |
| 9 | Offset | 0 | |
| 10 | **Speed** | 5 | Animation rate — this is why it moves |
| 11 | Spin | 0 | |
| 12 | Outline | 50 | |
| 13 | Falloff | 25 | |
| 14 | Softness | 10 | |
| 15 | Color | 🔴 unreadable (writable) | |
| 16 | Colorize | 20 | |
| 17 | Ambient Color | 🔴 unreadable (writable) | |
| 18 | Ambient Amount | 10 | |
| 19 | Vibrance | 10 | |
| 20 | Desaturate | 0 | |
| 21 | Chromatic Aberration | 10 | |
| 22 | Blend Mode | 0 | |
| 23 | Source Opacity | 100 | |
| 24 | Edge Repeat | true | |

🟢 **`Anchor` (4) + `Range` (8) + `Speed` (10) are the three that matter.** Anchor decides where
the light comes from, Range how far it throws, Speed whether it pulses or sits still.

🟢 **Speed is the reason to prefer this over Volumetric Rays on a music video** — it moves on its
own, so a held shot stops feeling static without any keyframing.

## VR Digital Glitch applied — 2026-08-24

**Accepted by Kai.** Applied to the clip he had selected.

| Clip | Track | Span | Effect | Settings |
| --- | --- | --- | --- | --- |
| `v3:1` | V4 | 6.84 → 8.08 | `AE.Mettle SkyBox Digital Glitch` | **defaults** |

Source `badcode guy/9.mp4`. Nothing sits above it in that window, so it reads. Verified by frame
at 7.4s, read by eye (`frames/fx2/glitch-applied-7.4.png`): torn blocks, rainbow fringing on every
edge, displaced scan bands. **Heavy and aggressive at defaults** — squarely the *transmission is
failing* register.

⚠️ **The selection was a linked A/V pair** — `getSelection()` returned two items, the video clip
and its audio (Volume / Channel Volume intrinsics). **Always filter to the video item** before
applying a video effect.

### VR Digital Glitch — `AE.Mettle SkyBox Digital Glitch` (38 params), measured 2026-08-24

🔴 **Indices 0–6 are 360/VR plumbing, not the look** — Frame Layout, Horizontal/Vertical Field of
View, Point of Interest. Leave them alone on flat footage.

| Index | Param | Default | What it does |
| --- | --- | --- | --- |
| 7 | **Master Amplitude** | 100 | **The single dial for "how much".** Drop this first |
| 9 | **Color Distortion** | 50 | The rainbow fringing |
| 10 | **Geometry Distortion X** | 50 | Horizontal tearing |
| 11 / 12 | Geometry Distortion Y / Z | 0 | Off by default |
| 13 | Distortion Complexity | 40 | How fine the torn blocks are |
| 14 | Distortion Rate | 50 | How fast it churns |
| 15 / 16 | Distortion / Color Evolution | 0 | Animate these for a seeded drift |
| 26 | Sub Influence | 95 | Secondary layer of corruption |
| 31 | Noise Strength | 0 | Off — raise for added grain-static |
| 37 | Random Seed | 0 | Change to get a different pattern on another clip |

🟢 **`Master Amplitude` (7) is the one to reach for.** Everything scales off it, so a single
number takes it from destroyed to a hint.

🔴 **Reuse warning: `Random Seed` (37) defaults to 0 on every clip**, so two glitched clips in a
row corrupt *identically*. Change the seed per clip or the repeat is visible.

## Restoring the running clip on V5 — 2026-08-24

Kai had removed the running clip (`clips/2.mp4`) from V5, leaving a **3.08s hole at 11.04 → 14.12**
and orphaning a cross dissolve he wanted back.

**Done:** cloned an existing `clips/2.mp4` instance down from V6 (`videoTrackOffset: -1`,
`deltaSeconds: 11.04`, `mode: "overwrite"`) then `trim_clip({ end: 14.12 })` to stretch it across
the gap. V5 now reads `v4:0` 8.08→11.04 · **`v4:1` 11.04→14.12 (2.mp4)** · `v4:2` 14.12→16.28.

🔴 **Insert-from-project-item was the wrong tool here.** `clips/2.mp4` is 10s long, so
`premiere_insert_clip` at 11.04 in overwrite mode would have laid 10s down and **destroyed the
clip at 14.12**. Cloning an existing timeline instance and trimming avoids that entirely.

⚠️ **The new clip is hidden for its first 1.24s.** V6 carries the posterized flicker run at
11.04→12.28, and V6 is above V5. The running clip only becomes visible from **12.28**.

🔴 **The cross dissolve could NOT be restored — this is hand work.** `add_transition` was refused
twice, from both sides of the cut, and an exported frame confirmed a hard cut at 14.12. Full
write-up: [`../../premiere/api-notes.md`](../../premiere/api-notes.md).

🔴 **One transition of unknown identity is still on V5.** It is not at `v4:2`'s start. It cannot be
read, located or safely searched for — see the api-note. **Kai should find it by eye and decide.**

## Needs a human

- **The photosensitivity call** above — the only decision that could affect distribution.
- **Audio: A1–A5 are all muted, A6 alone is live.** Deliberate, or left over from a solo pass?
  Not established.
- **Audio crossfades**, if any are wanted — no API exists for them at all; they are hand work.
- **Any title text** — `Simple Text` styling is writable, the words are not.

## Camera Shake on the scream close-up — 2026-08-25

**Applied at Kai's request** to the clip he had selected in Premiere.

| Clip | Track | Span | Source | Effect | Settings |
| --- | --- | --- | --- | --- | --- |
| `v3:3` | V4 | 13.00 → 14.16 (1.16s / 29f) | `clips/badcode guy/8.mp4`, in-point 3.2 | `AE.Impact_Camera_Shake_FX` | **defaults** |

The plate is an extreme close-up of the scream against a stadium crowd, with a gentle push-in
already baked into the source. Before this the clip carried **Opacity + Motion only** — Scale 100,
Position centred, no keyframes.

**Why this clip:** `badcode guy/8.mp4` appears three times in the cut — 8.08s (Volumetric Rays),
**13.00s (was bare)**, 15.24s (Volumetric Rays). It was the only untreated one of the three.
Camera Shake was chosen over matching the rays because **nothing else in the sequence shakes**, and
a 29-frame full-volume scream is where a physical hit pays.

**Verified by exported frame, read by eye:**

| Frame | Bytes | What it shows |
| --- | --- | --- |
| `scratchpad/sel-13.5.png` | 1,994,088 | **before** — the bare clip at 13.5s |
| `scratchpad/shake-default-13.5.png` | 1,948,211 | same timecode, frame displaced and motion-blurred |
| `scratchpad/shake-default-13.9.png` | 2,165,325 | framing shifted again, blur lighter — **it animates** |

🟢 **Auto Scale (param 29, default `true`) holds** — no black edges at either sample, despite the
amplitude. That is what makes defaults usable here without a compensating Motion scale.

⚠️ **Defaults are strong on this plate.** Master 100 with Motion Blur 20 smears the crowd
noticeably, and Auto Scale crops in a touch, so framing no longer matches the other two `8.mp4`
appearances exactly. Fine as a one-shot accent; would not survive being used as a run. The dials if
it needs pulling back: **Master (30)** 100 → ~70, **Speed (28)** 100 → ~160 for judder rather than
sway, **Stabilize (27)** 25 → ~40 to kill the drift, **Motion Blur (35)** 20 → ~12.

🔴 **Not saved.** Left live in Premiere on purpose so it can be walked back with undo.

### Camera Shake — `AE.Impact_Camera_Shake_FX` (47 params), measured 2026-08-25

Impact boilerplate as usual at both ends; the real controls sit from index 7. **Strafe / Stride /
Roll each appear five times** (indices 10–24) as five unlabelled triplets — the group headers
Premiere shows in the UI are the blank-named params, so the triplets cannot be told apart from the
API alone. **Which triplet is amplitude and which is frequency is unproven** — drive the effect
from `Master` and `Speed` instead unless someone maps them by hand in the GUI.

| Index | Param | Default | What it does |
| --- | --- | --- | --- |
| 3 | Scale | 50 | Prescale, only live with `Apply Prescale` |
| 7 | Seed | 0 | Reroll the shake pattern |
| 9 | Camera Mode | 1 | — |
| 10–24 | Strafe / Stride / Roll ×5 | see note | Five unlabelled triplets; mapping unproven |
| 25 | Lean (deg) | 0 | — |
| 26 | **Variation** | 20 | How irregular the motion is |
| 27 | **Stabilize** | 25 | Pulls the frame back to centre; higher = less drift |
| 28 | **Speed** | 100 | Frequency — judder vs sway |
| 29 | **Auto Scale** | `true` | Scales up to hide edges. 🟢 Leave on |
| 30 | **Master** | 100 | Global amount. The one dial to reach for first |
| 31 | Edge Behavior | 0 | Only matters with Auto Scale off |
| 34 | Enable Motion Blur | `true` | — |
| 35 | **Motion Blur** | 20 | Strong at default on a blurred source |

🔴 **The timeline has moved again since the 2026-08-24 entries.** As read on 2026-08-25 the
sequence has **six video tracks** (V1 empty, V2 10, V3 9, V4 11, V5 4, V6 34) and 68 video clips —
V5/V6 are no longer the A/B trial tracks described above. **Every clip ref recorded earlier in this
file is stale.** Re-read before acting on any of them.

⚠️ **A1–A5 remain muted, A6 only.** The selected clip's own linked audio (`a2:2`) is on a muted
track, so the scream itself is not heard. Flagged to Kai on 2026-08-25; **not changed** — presumed
deliberate.
