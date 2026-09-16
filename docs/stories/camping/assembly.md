# Camping — the Premiere assembly map

> **What this is:** what is actually on the timeline, clip by clip, matched to the shot IDs in
> [`shot-list.md`](./shot-list.md). Built 2026-08-30 by rendering a frame from the middle of every
> clip and looking at it — **not** inferred from filenames or dates.
>
> **Project:** `Camping Comic/Camping Video NEW!/camping vid.prproj`
> **Sequence:** `camping assembly` — 1920×1080, **24fps**, V1 + A1
> **Source:** `new clips/1.mp4 … 34.mp4`
> **Runtime:** 272s (4:32)

## Status

- ✅ **All 34 files in `new clips/` are on the timeline.** Folder and timeline diffed — identical,
  nothing missing, nothing extra.
- ✅ **Laid down in numeric order**, contiguous, no gaps and no overlaps.
- ✅ **Every clip is FULL LENGTH** — `inPoint 0`, no shortening, nothing trimmed. All 8s except
  `1.mp4` (10s) and `21.mp4` (6s). *Deliberate, so narration can be laid against the whole take
  and the trim happens afterwards.*

## The map

| # | Shot | What is in the frame | Note |
| --- | --- | --- | --- |
| 1 | **1a** | City skyline, old NatWest Tower, Gherkin, St Paul's | ✅ |
| 2 | **1b** | Wide trading floor, rows of screens, shirtsleeves | ✅ **swapped into canon order 2026-08-30** — `3.mp4` now plays second |
| 3 | **1c** | One man at a trading desk, on the phone, holding a document | ✅ `2.mp4` now plays third |
| 4 | **2a** | The car on the lane, luggage on the roof | ✅ |
| 5 | **2b** | Bob and his wife in the front seats, laughing | ✅ |
| 6 | **3b** | Dashboard binnacle, green indicator telltale lit | ✅ |
| 7 | **4b** | Tarquin at the top of the Shard, London below | ✅ |
| 8 | **5a** | The black X8 pulling away, the Shard behind | ✅ |
| 9 | **5b** | Through the car glass — shuttered shopfronts, wet street | ✅ |
| 10 | **5c** | Tarquin driving, smiling at his own joke | ✅ |
| 11 | **5d** | Same setup, the smile gone | ✅ one plate, two clips |
| 12 | **6a** | Waitrose car park through a rainy windscreen, the tent | ✅ |
| 13 | **6b** | Shoppers walking past the tent to the doors | ✅ |
| 14 | **6c** | 🔒 Tent POV out at the car park, bottle in hand | ✅ the locked framing |
| 15 | **7a** | Tarquin on the therapist's couch | ✅ |
| 16 | **7b** | The therapist in his chair, Tarquin's ankles foreground | ✅ |
| 17 | **8a** | The X8 swinging in beside the tent, across two bays | ✅ |
| 18 | **8b** | The two men, long lens, car and tent | ✅ |
| 19 | **8c(i)** | Bob in the tent mouth, face to camera | ✅ |
| 20 | **8c(ii)** | Tarquin by the car, Bob's shoulder foreground | ✅ |
| 21 | ❓ **unlisted** | Aerial, a car on a wet road through pine forest | 🔴 no shot ID in the repo |
| 22 | **9a** | Yurt interior, the group sitting round candles | ✅ |
| 23 | **9b** | Macro eye, pupil | ✅ |
| 24 | ❓ **unlisted** | POV hands round a mug, dome pod by a river, mist | 🔴 no shot ID |
| 25 | ❓ **unlisted** | The same POV gone kaleidoscopic — the trip lands | 🔴 no shot ID |
| 26 | ❓ **unlisted** | A man stepping into the lit dome pod | 🔴 no shot ID |
| 27 | **9c?** | Dome interior looking out at the river, bed foreground | ⚠️ probably the *eyes close* |
| 28 | **10a** | Tent POV at night — rain, drum fire, hooded figure | ✅ |
| 29 | **10b** | The camp wide from the rooftop, Waitrose, fires | ✅ |
| 30 | **11b(i)** | The newspaper on a pallet, found by torchlight | ✅ |
| 31 | **12a(i)** | The two men at the drum, hands over the flames | ⚠️ see *the 12a light* |
| 32 | **12a(ii)** | The two men at the drum, facing each other | ⚠️ see *the 12a light* |
| 33 | **12c** | The newspaper burning on the fire | ✅ |
| 34 | **12d** | The embers plate, 9:16 | ⚠️ pillarboxed until the tilt is built |

## What the assembly reveals

### 🔴 `4a` is not on the timeline

[`shot-list.md`](./shot-list.md) records *"**4a — the skyline swap.** Done 2026-08-26"*, and the
cut goes `3b → 4a → 4b`. **The timeline goes `3b` (clip 6) straight to `4b` (clip 7).**

**This matters more than a missing shot usually would.** `4a` is *"1a with the NatWest Tower
replaced by the Shard, year reads 2026 — the skyline is the timestamp."* It is how the audience is
told eighteen years have passed. Without it we cut from a 2008 crash to a man at the top of the
Shard and the time jump is carried by nothing.

**Either the clip was never exported, or it is outside `new clips/`.** Check the older `clips/`
folder before re-making anything.

### ✅ The scene-1 swap — DONE 2026-08-30

Canon is `1a` skyline → **`1b` the trading floor** → **`1c` young Tarquin mid-deal**. **As
assembled, the timeline ran `1a → 1c → 1b`** — skyline, then one man on the phone, then the wide
floor.

✅ **Ruled by Jack 2026-08-30: swapped to canon order.** `3.mp4` (the floor) now plays at 10s,
`2.mp4` (the man) at 18s. **The timeline and the shot list agree again**, and this was the only
place in the whole assembly where the order disagreed with canon.

⚠️ **Two mechanical facts learned doing it, and both will bite the next re-order:**

1. **`premiere_move_clip` does not move a clip's linked audio.** The video went and the audio
   stayed, so the take desynced. **Move `v0:n` and `a0:n` as separate calls, always.**
2. **A move silently dropped `narration.mp3` off A2 entirely** — not reported, just gone from the
   returned state. **Re-check every other track after any move**, and re-insert what vanished.

### ⚠️ Scene 9 is much bigger on the timeline than in canon

The shot list gives scene 9 three beats — `9a`, `9b`, `9c`. **The timeline has seven clips
(21, 22, 23, 24, 25, 26, 27)**, four of which have no shot ID anywhere in the repo: the forest
drive, the mug POV, the kaleidoscopic trip, and entering the dome.

⚠️ **They are also the wrong location.** The shot list records *"Scene 9 moved indoors — the
river-bank clearing is dropped for a yurt"*, and clip 22 is that yurt. **But 24, 26 and 27 are a
geodesic dome pod by a river** — the dropped version, still in the cut. Clip 21 is 6 seconds and
predates the entire project (3 Aug), so it is almost certainly sourced rather than generated.

**Nothing is wrong with the footage; the record is just missing.** Either these earn shot IDs and
go into the shot list, or they come out. Right now scene 9 is the least documented part of the film
and the most footage.

### 🔴 The `12a` light does not match `12c` or `12d`

**`12a` is on the timeline as two clips (31 and 32) and both are in flat overcast daylight** — grey
sky, the camp evenly lit, the drum fire a small bright spot that is not lighting anybody's face.
**`12c` (33) and `12d` (34) are deep night**, black beyond the firelight.

So the end of the film runs **daylight → pitch dark → pitch dark**, on the same fire, minutes apart
in story time.

⚠️ **It also runs the wrong way against scene 10.** `10a` and `10b` (28, 29) are dusk-dark. `12a`
is *brighter* than them, so the film gets lighter as it ends and the time of day moves backwards.

🔑 **Worth knowing what this means about the design.** The written `12a` prompt asked for night,
the fire as the only light, both faces lit from underneath, both men looking down into the flames
and never at each other, camera down at the drum with flames breaking into the bottom of frame.
**What is on the timeline is the opposite of all five** — daylight, a centred drum, both men
standing square to it, and in clip 32 they are looking straight at each other. It is much closer to
the *reference image* than to the brief, which is the failure mode
[`nano-banana-2.md`](../../google-flow/nano-banana-2.md) already names.

✅ **The §26 finding still stands, and it is the important one:** two Characters, two faces, one
frame, both identities held. That was the unknown, and it is answered either way.

**Three ways out, and it is a human call:**

1. **Grade `12a` down** to night in Premiere. Cheapest. It will not invent the underlighting, so
   the faces stay lit from the wrong direction — but at a cut it may be enough.
2. **Re-shoot `12a`** against the written prompt, now anchored on the accepted `12c` frame.
   Expensive in a scene that is otherwise finished.
3. **Move the fire scene earlier** so the light is motivated, and let `12c`/`12d` be later. Changes
   the cut, not the footage.

## Not on the timeline, and known

`10c`, `10d`, `11a`, `11c`, `11d` — all recorded as unshot. `9b`'s clip and `9c` were owed as of
the last session and scene 9's extra footage may already cover them.
`3a` (cut to black), `3c` (silence) and `5e` (narration) are not generations and never will be.
`12b` and `12e` are struck.

---

## Premiere — grade, effects and markers pass (2026-09-05, by session over the bridge)

**Project:** `Camping Comic/Camping Video NEW!/camping vid.prproj`
**Sequence:** `camping assembly` — 1920×1080 @ **24fps**, **209.92s (3:29.9)**, 39 clips on V1
**Scope:** Jack asked for exactly four things — effects, transitions, markers, grade — plus a
ruling on music. Nothing else on the timeline was touched: **no clip was moved, trimmed, added or
removed.**

⚠️ **The map above is out of date.** The cut is now 39 clips / 209.9s, not 34 / 272s. Two clips
that did not exist when it was written are in: **`0.mp4` = `1y`** (2008 foreshore, opens the film)
and **`6.5.mp4` = `4y`** (2026 foreshore, at 27.79s, where `4a` was missing). Both verified by
exported frame. Narration `narration/1-fixed.wav` (48 kHz stereo, **156.56s**) is laid on A2 in 13
chunks and **every second of it is used** — source out-point 156.54s.

### Applied

| What | Where | Exactly |
| --- | --- | --- |
| **Grain** | 🔵 **all 39 clips** | `AE.ADBE Noise2` · param **0 = 4** (percentage), param **1 = false** (monochrome) |
| **Night grade** | `v0:35` `v0:36` (`12a(i)`/`12a(ii)`) | `AE.ADBE Lumetri` · **14** Temperature −12 · **19** Exposure −0.8 · **20** Contrast +10 · **21** Highlights −20 · **22** Shadows −12 · **24** Blacks −8 |
| **Vignette** | `v0:32`–`v0:37` (scenes 10–12) | `AE.Impact_Vignette_FX` · **4** Vignette 100 · **11** Feather 60 · **14** Chromatic Aberration 0 · **16** Master 35 |
| **Fade up from black** | `v0:0` (`1y`) | Opacity (component 0, param 0) 0 @ 0.0s → 100 @ 0.75s, bezier |
| **Fade to black** | `v0:38` (`12d`) | Opacity 100 @ 6.0s → 0 @ 7.96s, bezier |
| **Markers** | 17, whole timeline | scene heads + `LAST NARRATION WORD` @ 197.21 + the `12d` pillarbox note |

🔴 **Keyframe times above are CLIP-RELATIVE, not sequence time.** Sequence-time keyframes render
nothing at all, silently — see [`api-notes.md`](../../premiere/api-notes.md).

**Why grain is on every clip and not just the dark end:** it is a *delivery* requirement, not a
look. 8-bit gives 256 steps, a dark gradient occupies a thin slice of them, and the steps show as
banding after YouTube's encode; randomised noise breaks the step edge
([`delivery.md`](../../video-fx/delivery.md) §near-black). Putting it only on scenes 10–12 would
also have made a visible texture step at 168.04s. **Denoising a near-black sequence on the way out
makes banding worse — never do it.**

**Why the vignette stops at `v0:37`:** `v0:38` (`12d`) is still a pillarboxed 9:16 plate, so a
vignette would darken the black bars rather than the picture. **It goes on once the tilt is built.**

**Why no dissolves were added:** hard cuts are the register, and canon calls the `3a` crash a *cut*
to black. Also mechanical — **13 clips sit at full source length, so they have no handles**; a
dissolve on one of those is silently written as a single-sided frame-hold, which reads as a freeze.
`AE.AE_Impact_Luma_Fade` (dissolve into black) is the one to reach for if we change our minds.

**Verified by eye:** frame at **186s** exported and read — `12a` now reads night, fire is the key
on both faces, shadows present and not crushed. Also read: 1.5s (`1y`), 31s (`4y`), 170s (`10a`),
206s (`12d`).

### 🎵 Music — ruled, and the answer is no

**The "Camping" track is not missing from this cut; it has its own project** —
`/mnt/d/badcode-videos/camping-music/camping.prproj`, Kai's hand cut, 236.4s.
[`music-video.md`](./music-video.md) states plainly that it is *distinct from the story video*.
**A3 stays empty and that is correct.**

🔴 **What canon actually asks for here is sound design, and NONE of it is on the timeline:**

- **Scene 3a, the crash** — `story.md` L325: *"Sound design carries this scene (impact, then
  silence)."* L489: *"sound design only."* A1 and A2 are both silent across the 23.29–23.67 gap.
- **Scene 12, the clink** — `narration-brief.md`: *"The clink is a sound cue, not a picture."*

A score bed under the wordless stretches is **an open call for Jack**, not a canon one.

### Needs a human

- 🔴 **Audio crossfades.** 39 butt-cut clips on A1 with no dissolves anywhere. **There is no audio
  transition API at all** — not a gap in our tools, a gap in Adobe's. Hand-drag Constant Power.
- 🔴 **`scripts/delivery-qc.sh` cannot run: ffmpeg is not installed in this WSL.** Nothing ships
  measured until it is. This is the film whose last render went out full-range with no colour tag.
- 🟡 **The grade was judged on exported frames, not scopes** — no UXP API exposes Lumetri Scopes.
  Eyeball it in the program monitor; `delivery.md` is blunt that a dark frame must never be
  eyeballed alone, so the rendered-file check is the real gate.
- 🟡 **Grain at 4 is a starting value.** One `premiere_set_param` per clip to change it.
- ⬜ **Not saved by the session** — every change is its own `BadCode:` undo entry, so review then
  save, or step back through them.

## Premiere — `camping jack` · the 27 → 28 blink (2026-09-14)

**Project:** `…/Camping Video NEW!/camping jack/camping jack.prproj` · **Sequence:** `0 synced` (1920×1080 @ 24)
**Built by:** a session over the bridge, following the eyelid recipe in
[`docs/premiere/api-notes.md`](../../premiere/api-notes.md) (two Linear Wipes, upper lid heavier).

| Clip | Timeline | What it is |
| --- | --- | --- |
| `v0:50` `27.mp4` | 214.583 → 217.625 | Dome POV from the bed, so the eyes **close** here |
| `v0:51` `28.mp4` | 217.625 → 222.125 | Tent POV, so the eyes **open** here |

**Chain on both clips:** `2 AE.ADBE Gaussian Blur 2` · `3 AE.ADBE Linear Wipe` (upper lid: angle 180,
feather 240) · `4 AE.ADBE Linear Wipe` (lower lid: angle 0, feather 190). Keyframes are all bezier and
**clip-relative**.

- **27, close with a droop and a flutter.** Upper wipe: 1.617→0, 2.117→45, 2.367→32, 2.917→78.
  Lower wipe: 0, 18, 12, 42 at the same times. Blur: 1.617→0, 2.917→60.
- **28, open with a half-blink.** Upper wipe: 0.2→78, 0.55→48, 0.75→62, 1.4→0. Lower wipe: 42, 22, 28, 0
  at the same times. Blur: 0→60, 1.7→0.

**Looked at:** exported frames at 216.9, 217.3 and 218.15 show soft lids and an off-centre slit. The
wiped area decodes as transparent (alpha 0), so it plays black on V1.

**Needs a human**
- ⬜ **Scrub 216–219.5 at speed** and judge the timing. Every number above is a first pass.
- ⬜ **No exposure dip yet.** The recipe's Lumetri ramp to −2 stops, leading the lids, was left out.
- ⬜ **The lid edge is straight** (a Linear Wipe limit, not solved).
- ⬜ **Not undone:** a first Crop-based attempt was added and then removed. Undo history holds both, so
  don't step back further than the `Linear Wipe` entries.
- ⬜ **Saved** by the session at the end.

## Premiere — `camping jack` · one grade, camera moves, invisible cuts (2026-09-14)

**Project:** `…/Camping Video NEW!/camping jack/camping jack.prproj` · **Sequence:** `0 synced` (1920×1080 @ 24, 254.33s, 59 clips on V1)
**Built by:** a session over the bridge, for Jack's three picked jobs. **No clip was moved, trimmed, added or removed.**

### 🔙 How to undo it

| Scope | Do |
| --- | --- |
| **Everything** | Close the project, then replace `camping jack.prproj` with `backups/camping jack.pre-grade-moves-cuts.2026-09-14.prproj` (the file as it stood before this session touched it) |
| **One job, this Premiere session** | Edit ▸ Undo. Every write is a `BadCode:` entry: grade = 3 per batch (`Lumetri on…`, `Noise2 on…`, `values on…`) × 5 batches + 2 test entries on `v0:52`; each keyframe and transition is its own entry |
| **One job, later** | Grade: remove components `Lumetri Color` + `Noise` from each clip. Moves: clear Motion Scale/Position keyframes on the 7 clips below. Cuts: `premiere_remove_transition` at `end` of `v0:24` `v0:44` `v0:47` `v0:57`; clear Opacity keyframes on `v0:24` |

`backups/camping jack.post-grade-moves-cuts.2026-09-14.prproj` is the saved result.

### 1 · One grade for the whole film

**On all 59 clips**, appended last in the chain (after the blink's wipes on `v0:50`/`v0:51`):

| Effect | Params (by index) |
| --- | --- |
| `AE.ADBE Lumetri` | **16** Saturation 88 · **20** Contrast −6 · **21** Highlights −12 · **40** Faded Film 10 |
| `AE.ADBE Noise2` | **0** Amount 3 (%) · **1** false (monochrome) |

**Why these four:** the mismatch between the clips was the *ends* of the histogram, not the middle — AI clips arrive with inconsistent crushed blacks and clipped whites. Faded Film + a touch of negative contrast gives every clip the same soft black floor, Highlights −12 the same roll-off, Saturation 88 pulls the louder generations toward the muted register (`shot-list.md`: *muted, cool, unforgiving*). No temperature shift — it would have flattened the fire's warmth, which is an argument, not decoration.

**Measured** — a mid-clip frame of every clip before and after, 480×270, full table in `camping jack/frames/grade-measure-2026-09-14.txt`:

| Across 59 clips (mean) | Before | After |
| --- | --- | --- |
| % of frame below 16 | 14.6 (sd 14.6) | **10.8** (sd 11.9) |
| % above 235 | 3.4 (sd 5.6) | **2.7** (sd 4.4) |
| p5 | 15.2 | **20.3** |
| median | 86.4 | 86.0 — mid-tones untouched |

Worst crush is still the night car interiors and the `11b` torch frame (`v0:30` `v0:31` `v0:38` `v0:52`, 37–45% below 16, were 46–52%) — by design, they are night, and each has its bright anchor. No clip got darker. Read by eye on a contact sheet: night still reads night.

### 2 · Subtle camera moves (Motion, component 1 — keyframes clip-relative, all bezier)

| Clip | Shot | Move | Why |
| --- | --- | --- | --- |
| `v0:0` `0.mp4` | `1y` 2008 foreshore | Scale 100 @ 0 → 104 @ 2.625 | the year device |
| `v0:25` `6.5.mp4` | `4y` 2026 foreshore | **identical** 100 @ 0 → 104 @ 2.625 | canon: *whatever push 1y gets, 4y gets identically* |
| `v0:27` `7.mp4` | Tarquin at the Shard window | hold to 1.0, 100 → 106 @ 7.958 | the man at the top; attention narrows |
| `v0:37` `15.3.mp4` | Tarquin in session | hold to 1.0, 100 → 105 @ 5.958 | the realisation beat |
| `v0:45` `22.mp4` | yurt interior | hold to 1.0, 100 → 105 @ 7.958 | holds through the dissolve in, then drifts |
| `v0:56` `33.mp4` | `12c` newspaper burning | hold to 0.5, 100 → 107 @ 6.667 | arrives on the headline |
| `v0:57` `35.mp4` | end: storm, silhouettes, fire | Scale 112 → 100 and Position y 0.45 → 0.50, both 0.417 → 4.0 | **the owed `12d` tilt-up**, from the fire to the sky, landing exactly on `52.mp4`'s framing before the dissolve |

⚠️ **The tilt is a compromise.** `12d` was designed on a 9:16 plate with real vertical travel; the cut now ends on the 16:9 `35.mp4`, which has none, so the move is a 12% overscan tilt that pulls out as it rises. Offset stays inside the overscan margin the whole way (0.05 vs 0.06) — **checked: no uncovered edge on any exported frame.**

**Not moved, on purpose:** the tent POV pair (`v0:34` `14.mp4` / `v0:52` `30.mp4`, the locked 6c→10a rhyme), the blink clips (`v0:50`/`v0:51` — Motion would scale the lids with the picture), and everything short. No handheld drift — `motion-and-cutting.md` §1 (*handheld is not truth*), and seven moves is already the budget.

### 3 · Invisible cuts

All `ADBE Film Dissolve` (gamma-linear, so a dark frame doesn't dip muddy mid-blend):

| Edge | Duration · alignment | Cut | Why |
| --- | --- | --- | --- |
| end of `v0:24` `5.5.mp4` | 1.0s · 0 (all after the cut) | crash aftermath → `4y` 2026 foreshore @ 69.92 | **the eighteen-year jump** — the wrecked car ghosts into 2026 |
| end of `v0:44` `51.mp4` | 1.0s · 0 | walk to the yurt → yurt interior @ 187.58 | outside becomes inside |
| end of `v0:47` `24.mp4` | 1.0s · 0 | mug POV → the kaleidoscope @ 204.58 | the trip lands |
| end of `v0:57` `35.mp4` | 1.5s · 0.5 (centred) | storm → BadCode logo @ 249.79 | the logo resolves out of the storm |

Alignment 0 is used where the incoming clip starts at in-point 0 (no head handles) — every outgoing clip has ≥1.6s of tail. **All two-sided; verified by frame.**

**The crash (3a):** the existing 0.75s black gap at 65.125–65.875 stays exactly as it was, **entered on a hard cut** (a crash doesn't dissolve). New: `v0:24` fades **up out of the black** — Opacity (component 0, param 0) 0 @ 0 → 100 @ 0.708, bezier — so the aftermath surfaces rather than snapping on. Measured: alpha 87/255 at 66.2s.

### Looked at

Frames in `camping jack/frames/look-check/` at 65.0, 65.5, 66.2, 67.0 (crash) · 187.4, 188.08, 204.4, 205.08, 249.8 (dissolves) · 245.5, 247.4, 249.2 (tilt) · 78.7/85.5, 238.9/244.9 (pushes) · 1.3/2.6, 70.0/72.5 (1y/4y) · 216.9, 217.3, 218.15 (blink — alpha identical to the pre-grade frames, so the grain didn't break the lids).

### Needs a human

- ⬜ **Watch it at speed.** Every value is a first pass judged on stills. Moves in particular only read in motion.
- ⬜ **The crash beat is 0.75s of black.** Kept, not lengthened — lengthening means rippling every track, and the narration is synced. If it should be longer, that's a hand edit.
- ⬜ **Delivery QC still can't run** — no ffmpeg in WSL. `scripts/delivery-qc.sh` before upload.
- ⬜ **No audio crossfades** at the four dissolves (no API). A1's clip audio butt-cuts under them.

### 1b · Grade pushed stronger — same day, at Jack's request

Jack watched the light pass and didn't notice it. **Same two effects on all 59 clips, stronger values** (read back on every clip):

| Effect | Light pass (above) | **Now** |
| --- | --- | --- |
| `AE.ADBE Lumetri` 16 Saturation | 88 | **75** |
| 20 Contrast | −6 | **−10** |
| 21 Highlights | −12 | **−22** |
| 40 Faded Film | 10 | **20** |
| 110 Vignette Amount | 0 | **−1.2** |
| `AE.ADBE Noise2` 0 Amount | 3 | **5** |

| Across 59 clips (mean) | Original | Light | **Stronger** |
| --- | --- | --- | --- |
| % below 16 | 14.6 | 10.8 | **9.1** |
| % above 235 | 3.4 | 2.7 | **1.2** |
| median | 86.4 | 86.0 | **79.1** — the vignette and highlight pull |

**No clip is more crushed than its original.** The blink's alpha is unchanged. Table: `camping jack/frames/grade-measure-stronger-2026-09-14.txt`.

**Undo just this step:** put the "Light pass" column back, or restore `backups/camping jack.post-grade-moves-cuts.2026-09-14.prproj`. The saved result is `backups/camping jack.post-stronger-grade.2026-09-14.prproj`.

### 1c · The grade and grain carried to the new clips — 2026-09-16

**Jack:** *"please do it for the rest of them."* The timeline had grown to **67 video clips** (66 on V1 and 1 on V2),
and **14 had no grade**. Each got the 1b values exactly: `AE.ADBE Lumetri` 16 → 75 · 20 → −10 · 21 → −22 ·
40 → 20 · 110 → −1.2, then `AE.ADBE Noise2` 0 → 5 · 1 → false, both appended last.

| Ref | Clip | Starts |
| --- | --- | --- |
| `v0:40` `v0:41` `v0:42` `v0:43` | `53` `54` `56` `55` | 151.3 · 159.8 · 167.8 · 169.7 |
| `v0:48` | `57` | 208.8 |
| `v0:53`–`v0:59` | `58` `59` `60` `64` `62` `63` `65` | 236.3 → 280.4 |
| `v0:65` | `66` | 309.2 |
| `v1:0` (V2) | `56` | 157.3 |

**Verified from the state file:** all 67 clips carry both effects, every Lumetri has identical parameter values
(one group of 67), and every Noise does too (one group of 67). The first new Lumetri was diffed parameter by
parameter against a graded clip and matched. It is still the last pair in every chain.

**Undo:**
- **Everything:** `backups/camping jack.pre-grade-new-clips.2026-09-16.prproj`, saved immediately before.
- **In session:** Edit ▸ Undo, 28 `BadCode:` entries, 2 per clip.

⚠️ The timeline has changed since 1b (runtime 254 → 317s, transitions 4 → 2), so the ref tables in the
sections above are stale.

**Needs a human:** watch 151–317s at speed. The V2 clip (`56.mp4` over `53`/`54`) is graded on its own layer.
If it's a blend or partial overlay rather than a full cover, check it doesn't look double-graded.
