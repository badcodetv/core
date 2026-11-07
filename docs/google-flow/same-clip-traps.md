# Same-clip traps: why every performer came out a "geography teacher"

Jack, 2026-11-07, on the Camping balaclava rappers (`camping balaclava 1`): *"i asked for the balaclava guy to rap and gesture
like eminem on stage, he kind of raps and gestures like a geography teacher ... is there something in the prompt or in the repo
that is affecting it and making the same prompt over and over like before, i thought we fixed that"*.

The twin of `docs/suno-gpt/same-song-traps.md`, for Flow clips. Evidence tiers: **[ours]** = seen on our own clips;
**[vendor]** / **[reported]** = from the web research `docs/stories/camping/mv-song2/cleanroom/research-stage-rap.md`.

## What was carrying it (found 2026-11-07)

The clean room (fresh web research + sealed writers) was breached by things passed in as "facts":

1. **Recycled research.** The Camping rap-clip briefs pasted in `bank-robbery/songs/mv-gang/cleanroom/research-clips.md`,
   written 2026-11-03 for Bank Robbery's *action* clips. Its anti-morph advice is right for a car or a safe and wrong for a
   performer: "subtle evolution rather than dramatic change", "one primary motion", "keep the gesture vocabulary small: one
   repeated move", "his right hand chops down on each beat, four times ... then stop", "one action finishes by ~4 s and then
   holds". Six Bank Robbery brief scripts and the Camping one all fed it to their writers. **[ours]**
2. **A copied brief script.** `camping/mv-balaclava/cleanroom/r4-clips/make_clip_briefs.py` was cloned from the Bank Robbery
   one, so the same frame ("keep the head facing the lens", "the camera stays still ... say so") came along. **[ours]**
3. **A director's note from another video.** Every brief quoted Jack's "everything is so exaggerated please make it simple"
   (said about the colour-noir video's *action*) next to "rapping ... like eminem". Writers took the safe half. **[ours]**
4. **"Match the original."** Writers were told to rap "with the same energy and the same kind of gestures as the original"
   clip, and the originals were Bob and Tarquin *talking* to camera. **[ours]**
5. **The mask-drift rule** ("keep the head facing the lens; nods and leans are fine") was stated as a hard fact, so the body
   was built around a still head. **[ours]**
6. **The stills.** Close-ups and chest-up frames, two seated, no microphone: an image-to-video clip can only move what the
   first frame shows. **[ours]**; a cramped start frame gives stiffer motion **[reported]**.
7. **A habit sentence.** "Locked-off camera, framing holds; the editor adds any camera move" sits in 169 past prompts.
   `fresh.py` flagged it every round and it was "kept on purpose" every round. **[ours]**
8. **The engine's default.** Google describes subject animation as "subtle, lifelike actions" and treats the camera as the
   main source of dynamism **[vendor]**; with the camera locked, energy has to be written into the body or none arrives.

## The rules this leaves (loose guides, per the rules-are-a-loose-guide ruling)

- **Fresh research per job.** Never paste another round's or another story's research file into a brief. If old research is
  useful, a new researcher reads the web again; at most, cite the old file's URLs.
- **Never quote a director's note about a different video.** Quote only what was said about this one.
- **Never "match the original" when the original is what is being replaced for being wrong.**
- **Performance clips start from a performance still:** medium-wide or full, knees up, room above a raised arm, a prop in the
  hand (a microphone), the pose already mid-move, low angle. A close-up only lets the head move.
- **Write the energy into the body** when the camera is locked: committed verbs, the knee bounce, the stage prowl, what the
  free hand does on the rhyme. Keep the anti-morph advice for objects.
- **Run `scripts/variations/fresh.py`** — it now also lists DAMPERS (subtle, minimal, "then stops", "square to the lens",
  "four times"...). A damper on a performer needs a reason.
