---
title: Camping — the narration on the Premiere timeline
status: ⬜ NARRATION REMOVED 2026-09-11 at Jack's request — he is placing it by hand. A2–A4 and all markers cleared; V1/A1 left as below (with the +10s gap in scene 2). The 13 block files stay in the `narration blocks` bin for him to use. The rest of this file records the build that was removed.
project: `camping jack.prproj` — sequence **`0 synced`** (269.5s, 24fps). `0 synced Copy` = the 2026-09-10 build, untouched. `0` = the original backup.
source script: Jack's script (the 110-line paste, recovered from `~/.claude/paste-cache/fcf96ff845ac59af.txt`) — **not** `three-voice-script.md`
---

# What is on the timeline

**Jack's rulings:**
1. *The order of the script is the order it goes in.* (2026-09-10)
2. *Do not cut things from the narration — only the pauses between.* (2026-09-10)
3. 🔴 **Keep full sentences, cut only when they are done speaking, keep small pauses, make it sound
   natural. Group each speaker's lines and place them whole.** (2026-09-11)
4. *Use only the script and the clips on the timeline to decide where a line goes — not the repo.* (2026-09-11)
5. **Scene 2 overflow: push the crash later** (2026-09-11, chosen from three options).

| Track | What |
| --- | --- |
| **V1 + A1** | The same 37 clips in the same order. The crash and everything after it moved **+10.0s**; `5.mp4` moved +5s. Still in sync (checked: 0 mismatches) |
| **A2** | NARRATOR — 4 whole blocks |
| **A3** | BOB — 5 whole blocks |
| **A4** | TARQUIN — 4 whole blocks |

## 🔴 Why the 2026-09-10 build sounded wrong — three faults, all fixed

1. **It cut inside sentences.** It split at every pause ≥0.45s, which includes comma pauses
   (*"Tarquin here, | shorting…"*), then squeezed every pause to 0.32–0.35s. 34 slivers for 13 lines.
2. 🔑 **It put the wrong words in the wrong place.** Its "T2 *Twenty twenty-six*" clip (source
   `tarquin.wav` 11.04–17.0s) was really *"That is not callousness. That is good business. Rates go
   up a…"* — **`tarquin.wav` has no "Twenty twenty-six" take at all.** Proven twice by word-level
   transcription. T1 was chopped at 10.66s as a result.
3. **It trimmed in Premiere.** `createSetInPointAction` moves the clip, and the out-point is
   reported to be measured from the wrong origin
   ([Adobe community](https://community.adobe.com/questions-729/uxp-premiere-pro-how-to-slip-edit-a-videocliptrackitem-razor-blade-equivalent-1624762)).

## How it was cut this time

1. **Word timestamps** for all three renders (faster-whisper `medium.en`, CPU int8) plus an energy
   map (−45 dB, 10 ms windows). The transcript tells *which* words belong to which script block; the
   energy map tells *where the silence is*.
2. **One file per script block**, cut in Python (`wave` + numpy, no re-encode): from 0.15s before
   the first word to 0.30s after the last, never past the midpoint of the gap to the next block.
   **Every pause inside a block is kept exactly as rendered.** 15 ms fade at each edge.
3. **Every file re-transcribed** to prove it starts and ends on whole words. All 13 do (bar the two
   truncated renders, below).
4. **Placed whole** with `premiere_insert_clip` (overwrite) — **no in/out point ever set.**
   Premiere floors each clip's end to the frame grid (≤1 frame, always inside the silent tail).

Files: `camping jack/narration/blocks/NN <code> <speaker> - <words>.wav`, bin `narration blocks`.

| # | Block | Source | Source in → out | Timeline | Over |
| --- | --- | --- | --- | --- | --- |
| 01 | **N1** "2008 trading floors… without a scratch." | `nell.wav` | 0.16 → 20.45 | A2 0 → 20.25 | 2008 sand, skyline |
| 02 | **T1** "Leveraged E.T.F.s… good business." | `tarquin.wav` | 0.22 → 14.44 | A4 20.29 → 34.50 | starts on Tarquin's shot, runs into the floor |
| 03 | **N2** "Nice tie, mate." | `nell.wav` | 22.40 → 23.84 | A2 34.54 → 35.96 | trading floor |
| 04 | **N3** "Bob, a struggling middle manager… on TV." | `nell.wav` | 26.35 → 39.59 | A2 36.00 → 49.21 | lands on the cut to the car |
| 05 | **B1** "We had four days… a young fool I was." | `bob.wav` | 0.14 → 12.81 | A3 49.25 → 61.88 | car → laugh; last word 61.6, crash at 62 |
| 06 | **N4** "He's ditched the tie" 🔴 | `nell.wav` | 41.54 → 42.60 | A2 85.00 → 86.04 | Tarquin at the top of the Shard |
| 07 | **T3** "Rates go up a point… my bonus." | `tarquin.wav` | 14.65 → 22.62 | A4 91.00 → 98.96 | X8 → glass; "bonus" on the smile |
| 08 | **T4** "It is a tad chilly though…" | `tarquin.wav` | 22.73 → 25.49 | A4 107.00 → 109.75 | end of the smile-gone shot |
| 09 | **B2** "I used to hear… armchair manifestos aside…" | `bob.wav` | 14.29 → 33.73 | A3 110.00 → 129.42 | Waitrose → shoppers → tent |
| 10 | **T5** "I booked an emergency appointment… in the ca-" 🔴 | `tarquin.wav` | 25.92 → 29.28 | A4 132.29 → 135.63 | therapy two-shot (room left before it for N5) |
| 11 | **B3** "Why is he taking two spaces?" | `bob.wav` | 34.72 → 36.92 | A3 152.25 → 154.42 | X8 takes two bays (after T7's slot) |
| 12 | **B4** "Fucking wank tanks, if only I could have…" | `bob.wav` | 37.45 → 41.00 | A3 166.50 → 170.04 | Bob in the tent (after T8's slot) |
| 13 | **B5** "He came out of that tent… my word for it." | `bob.wav` | 42.17 → 49.00 | A3 221.50 → 228.29 | the newspaper |

## The new picture timing (after the +10s)

Scene 1 0–36 · scene 2 36–62 (**needs the hand stretch below**) · crash 62–70 · scene 4 70–88 ·
scene 5 88–110 · scene 6 110–130 · scene 7 130–150 · scene 8 150–179.5 · scene 9 179.5–214.5 ·
scene 10 214.5–221.5 · scene 11 221.5–229.5 · scene 12 229.5–269.5.

## Markers (19)

`SCENE 2 - stretch…` (36, 26s), `Scene 3 - the crash - SILENT` (62), `RE-RECORD N4` (85),
`RE-RECORD T5` (132.3), and `MISSING` T2, N5, T6, N6, T7, T8, N7, N8, T9, T10, T11, T12, N9, T13,
T14, each at the spot its line belongs and sized to its estimated length, with the line in the
comment.

🔑 **T2 was never flagged as missing before** — the old build thought it existed.

## Needs a human

- 🔴 **Stretch scene 2 by hand** (no speed API): right-click `4.mp4` (36s) ▸ Speed/Duration ▸
  Duration **00:00:13:00**, Ripple Edit **off**. Same for `5.mp4` (49s). Until then 44–49s and
  57–62s are black.
- 🔴 **Re-render N4 and T5 whole** — `nell.wav` stops on "tie" (still loud at the last sample) and
  `tarquin.wav` stops mid-word at "in the ca-". Neither was cut here; the renders end there.
- 🔴 **Record the 15 missing lines**, then drop each on its speaker's track at its marker.
- ⚠️ **Scene 8 will run ~2.5s long** once T7, T8 and N7 exist (estimated ~32s of speech for 29.5s of picture).
- ⬜ **Listen through once** — placed by transcript and measurement, not by ear.
- ⬜ **Levels and crossfades** — nothing mixed; there is no audio-transition API.
