---
name: narration-whole-blocks-never-trim-in-premiere
description: "Placing narration on a timeline — cut one file per speaker block at word boundaries outside Premiere, place whole; never split at pauses or trim in Premiere."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 081faf7f-d3be-420b-87f3-4338e46f4214
  modified: 2026-09-11T09:10:35.190Z
---

When putting narration on a Premiere timeline, cut **one WAV per script block** (a speaker's whole
turn) at word boundaries found by transcription (faster-whisper word timestamps + an energy map),
keep every internal pause exactly, and place each file **whole** with `premiere_insert_clip`
overwrite — no in/out points.

**Why:** Jack, 2026-09-11, after the 2026-09-10 build split at every ≥0.45s pause (including commas),
squeezed pauses, and mislabelled a piece so wrong words played over the wrong shot: *"keep the full
sentences and only cut them when they are done speaking, do not cut mid sentence… keep small pauses
and make it sound natural."* Premiere's in/out trim actions are also unreliable (in-point moves the
clip; out-point origin reported wrong).

**How to apply:** match lines to the script + what the clips visibly show, not repo shot lists.
Transcribe every render before trusting any line label. Re-transcribe each cut file to prove it
starts/ends on whole words. If words don't fit the picture, ask — never shorten pauses to force it.
Record in `docs/stories/<story>/narration/timeline-build.md`. See [[mark-unverified-claims-as-unverified]].
