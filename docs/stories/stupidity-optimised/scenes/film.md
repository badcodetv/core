# Stupidity Optimised: the film, rough 1

Scene folder: [`film/`](./film/). Shots, stills and motion prompts are in `film/prompts.json`; replacements are in
`film/rerolls.json` and `film/video-jobs.json`. Media is in `clips/film/` inside the Premiere project folder.

## Premiere

**Project:** `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\optimised stupidity\optimised stupidity.prproj`
**Sequence:** `Optimised rough 1`, 1280×720 at 24fps, 576s (9:36)
**Built:** 2026-11-01 by session (bridge), bin `film`

| Track | What |
| --- | --- |
| V1 | 71 clips of 8s each in shot order 1 to 71, then `72b.jpg` held for 8s, 0→576, no gaps |
| A1 | Each clip's own Flow sound effects, 0→568. The last 8s are silent |

**Applied**
- `v0:71` Motion Scale, keyframed 93.1 to 102 eased: a slow push-in on the held still. Keyframe time on a still is
  source time, which starts at 3600, not 0. Two stray keyframes at 0 and 8 sit outside the clip and do nothing.
- A marker on the last 8s explains the held still.

**Outputs**
- Frames in `frames/`, checked by eye. Premiere saved them as `.png.png`, so the bridge reports `EXPORT_FAILED` after
  waiting 120s even though the frame exists.
- Render: none, as Jack works in Premiere only.

**Needs a human**
- No voices or narration yet, so nothing is cut to length. Every shot runs its full 8s.
- Shot order is the shot list, not a cut: no flashing ambulance-light transitions, and the Scene 15 replay is not built.
- On-screen labels are not added.

## Premiere, rough 2 (current)

**Sequence:** `Optimised rough 2`, 1280×720 at 24fps, 532s (8:52), built 2026-11-01 as a new sequence. Rough 1 is untouched.
Layout comes from `film/rough2-plan.json`, with cuts under 1.2s merged into the next shot when placed.

| Track | What |
| --- | --- |
| V1 | 72 shots in order, 91 clips. A shot shorter than its lines repeats from its start, which reads as a jump cut. Shot 72 is the held still with the same push-in |
| A1 | Each clip's own Flow sound effects, about -32 to -43 LUFS |
| A2 | 87 voice lines, one clip each, trimmed at silence only, levelled to about -16 LUFS with clip Volume |
| A3 | 7 music cues, baked to -32 LUFS, then +3 dB clip Volume, so about -29. Tracks and credit are in `../sound.md` |

**Checked:** no clip overlaps on any track and no gaps on V1. An offline mix was written to the scratchpad only, to measure
levels (voices -16.2, music -32.0 before the +3 dB). Gemini heard a 90s stretch of it and said every word was clear over the
music. It also said no music was audible at 5:40–5:58, which is why the music went up 3 dB. Not re-measured after that.

**Words:** each line was transcribed by Gemini and compared with `film/voice-lines.json`. Wrong takes were re-rendered up to
four times. Transcription is unreliable on one-word lines, so those are unproven. Still reading as different: 033 ("the
study the app sourced") and 052 ("verruca"). `by: claude` lines there are stand-ins, including the Scene 7 prophet lines and
"Got it"s, Scene 10's app line and "Oh my god. It works."

**Needs a human**
- Nobody has listened with real ears. Accents were only spot-checked (one narrator line read as Northern, not West Midlands).
- Mouths are not synced to the voices.
- Still missing: search-bar and app text, flashing ambulance-light transitions, the Scene 15 label replay.
- The "glitchy line" Jack reports could not be found: no line in the clip files on measurement across every clip, and none in
  exported Premiere frames. Next step is a screenshot from him.

## Picks and re-rolls

Claude chose every still and clip, as Jack asked on 2026-11-01. He has not reviewed them.

| Shot | Used | Why it differs from the first attempt |
| --- | --- | --- |
| 26 | `so-26-26b.mp4` | Flow returned nothing on the original motion, in which he chokes on pills. The softer motion worked. The cause is not confirmed |
| 41 | `so-41-41b.mp4` | The first still and clip had a second Brandon under the sink |
| 45 | `so-45-45b.mp4` | The first clip's ambulance became a white van marked POLICE and swung round |
| 65 | `so-65-65b.mp4` | `UPLOAD_REFUSED` three times; the same still re-saved at 1280 wide went through |
| 72 | `72b.jpg`, held | Jack asked for bloody shoes. Flow makes the still but fails every clip of it within seconds, across four submits and two motion prompts, so it is a held frame. `so-72-72.mp4` is a moving take with grubby trainers |
