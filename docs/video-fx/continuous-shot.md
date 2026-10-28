# Continuous shot: one unbroken shot longer than a clip

A recipe, not a skill (folded in from the `continuous-shot` skill by the 2026-10-23 skills audit; the method behind it is [`hybrid-method.md`](./hybrid-method.md) §4). Used from `scene-animation` and `flow-prompt`.

Use it for one unbroken shot longer than a Flow clip (8 s): a travelling shot, a long walk-and-talk, a slow reveal. Omni clips are chained last frame to first frame and joined with no visible seam. Driving Flow is `flow-automation`, the words are `flow-prompt`, what the shot should be is `shot-craft`.

**One shot, many clips, no seam.** Built on GPOM second half cut 3, beat 0 (2026-10-20): Maddie rolls up the high street
towards a camera backing away at her speed, 47.75 s from six 8 s Omni clips, first try on every clip. The method is
[`docs/video-fx/hybrid-method.md`](./hybrid-method.md) §4 (chain, never pin an end frame); this is
the procedure and what went wrong.

## When to use it

- The beat is longer than 8 s and **cutting would break it**: a travelling shot, a long approach, a continuous talk.
- Something in the world moves the whole time. If only the camera moves, it is ffmpeg on one still, not Flow.
- **The camera may move** here (unlike most of our Veo work) if the move is steady and the subject stays the same size:
  "the camera tracks steadily backwards ahead of her at the same speed". The street regenerates as it slides past,
  and that is fine because it is meant to be new street.

## The procedure

1. **Start frame.** A real frame (from the plate or an existing clip's first frame), copied to a uniquely named file.
2. **One prompt for the whole chain**, motion only, the steady state stated as a continuing state: *"keeps tracking…
   keeps rolling towards the camera at the same pace, staying the same size in frame… It never stops."* Clip 1 may
   differ (it sets the move up: "turns to face the camera and rolls along after it"); clips 2…n are identical.
   Cast the subject's Flow Character by `@` on every clip (Frames mode has no reference slot; the `@` cast is the
   reference).
3. **Clip N**, Omni 1.1 Flash, Frames, start frame only, 8 s, x1 (`scripts/gpom/second-half-video/run-cut3.mts`, one
   job per run, so each clip is checked before the next is written).
4. **Last frame out:** `ffmpeg -sseof -0.5 -i clipN.mp4 -update 1 -q:v 1 clipN-last.jpg` (decode the last half-second
   and keep overwriting). ⚠️ `-sseof -0.05 … -frames:v 1` wrote **no file** on a 24 fps Omni clip.
5. **Check the join before paying for the next clip:** mean absolute grey difference between clip N's last frame and
   clip N+1's first, against the frame-to-frame step inside each clip, plus a six-frame strip across the boundary
   (A's last three, B's first three) that you look at. A good join is **below** the in-clip step (ours: 2.6–3.9
   against 4.2–7.8). Check the subject's identifying detail at full size on the last frame (Maddie's torn bunting).
6. **Next clip** from that last frame. Repeat.
7. **Join:** concat, dropping the first frame of every clip after the first (it duplicates the previous last frame, a
   one-frame freeze otherwise), re-encode at 24 fps, strip audio. Then scan the whole result: the step at every join
   should sit inside the shot's own range (ours: joins 3.6–5.2, shot median 3.5, max 5.3). No crossfade was needed;
   a 2–4 frame crossfade is the fallback for a join that fails.

## Failure modes actually hit

| What | Fix |
| --- | --- |
| **Generational drift.** Each clip starts from a re-encoded frame and re-renders it. Over six clips the warm, scuffed start went cold, grey and smooth; the robot's tyres widened. Gradual, so no join shows it, but first and last frames differ clearly | Keep chains to ~6 clips. Grade the chain back towards clip 1 with a ramped correction in post. Untested: re-anchoring with a still edited back to the original look |
| The harvester took the **previous** clip as the new one (its tile key was missing from the "before" snapshot) | md5 every harvest against every clip on disk; wait for no pending tiles, not for a new key (rebuild doc item 83) |
| `-sseof -0.05` produced no last frame | `-sseof -0.5 … -update 1` |

## Costs

Omni 1.1 Flash 8 s x1 = **12 credits** (read off the popover before each Create). Beat 0: 6 clips, 72 credits,
about 1.5 minutes per clip end to end, no re-rolls.
