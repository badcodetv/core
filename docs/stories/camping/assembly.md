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
