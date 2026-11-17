---
name: lookalike-drifts-to-the-real-person
description: "Jack 2026-11-17 \"remember and save this so that it doesnt happen again\": a lookalike in Flow turns into the real famous person when the face is small or the prompt stacks that person's cues; two-step fix"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 90da8b8e-3803-4016-b9ee-172df01e4bf9
  modified: 2026-11-17T12:57:26.380Z
---

An invented lookalike of a famous person (Priority Lane's Boris-alike minister, `BM9-b`) came out as the REAL person in rounds 8-11, with the invented man's photo attached and no name in any prompt. Jack's summary of why (2026-11-17):
- **The face was too small**: a face ~5-8% of the frame (~70 px, e.g. on a poster in a street shot) loses the reference, so Flow fills it from memory. Big faces (the car shots) kept the invented face.
- **The prompt described the real man without naming him**: each cue is harmless alone, together they are one person: his hair, nationality/class/job words ("English", "posh", "minister", "politician"), a "campaign" poster echoing his famous slogan, his photo-op trademarks (hard hat, hi-vis, thumbs up, pointing).

**Why:** four rounds and many takes were wasted before the cause was found; Jack asked for it never to happen again.

**How to apply** (any lookalike, any story):
- Never stack the real person's signature cues in a prompt (hair + job + nationality + slogan + props + poses). Drop job/nationality/"campaign" words and the photo-op props; write the invented face's own distinguishing features (nose, eyes, skin, age) even with a reference attached (a deliberate exception to [[never-describe-a-referenced-character]]).
- Never name the real person in a prompt OR in a clean-room writer's brief (the briefs named him in rounds 8-9).
- A face that will be small in frame: make it big first (e.g. the poster artwork alone, face ≥ a third of the height, a face-crop reference), then attach that finished image as the reference for the wide shot ("reproduced exactly").
- Check every output face for a real-person likeness before it goes on a board.

Evidence and sources: `docs/google-flow/nano-banana-2.md` (section "A small reference face on a poster drifts to a famous politician") and `docs/stories/shorts/priority-lane/cleanroom/r12/research-likeness.md`. See [[clean-room-stills-work]].
