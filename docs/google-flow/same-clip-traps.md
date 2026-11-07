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

## The over-correction (round 5 → 6, 2026-11-07)

Jack, after the "geography teacher" fix: *"he seems to float in the air, ai slop is present when he does anything"*.
The round-5 brief banned every calm word and asked the clip to "continue that energy", so the writers reached for travel and
size: prowling at the lens, jumps, lunges, squat-and-spring, wide frames with lots of floor. **[ours]** The engine cannot plant
feet that travel: they slide, the body glides and the face swells near the lens (`docs/stories/camping/mv-balaclava/cleanroom/r6/failures.md`).
The fix that worked (round 6) came from the reference performer, not from more or less energy: rooted on one spot, chest-up or
waist-up mostly, short hard gestures from the elbow and wrist, a handheld close camera, and on a wide, a hard shadow joined to the
feet. **[ours]**, research `docs/stories/camping/mv-balaclava/cleanroom/r6/research.md`.

- **Watch the reference the director names** and describe what the body does, frame by frame, before any writer starts.
- **A damper list is a guide, not a ban.** "Subtle handheld", counts and "stops dead" were right here; a ban on them caused the float.
- **No travel towards a locked camera** for a performer: it is the commonest float.

## Round 7 (2026-11-07): five prompt patterns, one still each

Jack picked the **T3 "locked medium, understated"** pattern (`docs/stories/camping/mv-balaclava/cleanroom/r7/research-prompts.md`) over a
handheld freestyle, a fisheye push-in, a phone take and timecoded accents, all from the same start frame. **[ours]** The phone-take
pattern drew a phone into the frame. My read before his pick: the start frame's pose (hands at the chest) set the gesture more than any
prompt did [inference, untested].
