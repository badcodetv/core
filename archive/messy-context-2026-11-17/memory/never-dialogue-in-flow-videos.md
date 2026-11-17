---
name: never-dialogue-in-flow-videos
description: Flow video prompts must ask for sound effects only, never dialogue — the narration is recorded separately and must not be competed with.
metadata:
  type: feedback
---

**Every Flow video prompt ends its audio line with `No dialogue, no music.` and asks only for
sound effects** — rain, tyres, wind, an engine, a trolley's wheels, a train.

**Why:** Jack records the narration himself afterwards. Any generated speech collides with it
and makes the clip unusable. Sound effects are the opposite — they are *wanted*, because
generated ambience makes the clip read as captured rather than rendered, and it sits
underneath narration without fighting it.

**How to apply:** write a specific, motivated SFX list for every clip — name what is actually
in the frame making the noise. Never write a line of speech, a voice, a shout or a
conversation into a prompt. Non-verbal human sound tied to an on-screen action is fine
(a laugh, a breath) as long as it carries no words.

⚠️ This **amends** Camping's standing rule in `docs/stories/camping/shot-list.md`, which read
*"never model-generated audio"* — generated SFX are now welcome; only dialogue is barred.
Related: [[one-shot-at-a-time-still-then-video]].

**Second exception, 2026-10-07:** Jack asked for dialogue in The Bank Robbery clips too ("make the videos in a david lynch way, add dialogue in them"). So the exceptions are Money For Something and The Bank Robbery; every other film keeps the rule. Recipe that works: Frames, the speaker's Character chip attached, `He says:` then the words, no quotation marks, about twelve words a clip. Record: `docs/stories/bank-robbery/clips-v3.md`.

**2026-10-15 meeting: the Bank Robbery exception is withdrawn.** Films move to multi-narrator narration with no on-screen speech ([[narration-not-lipsync]]). Money For Something was not discussed.

**2026-11-10, Jack: "never do flow speech, only do the ai google studio thing where we do the lip sync tool."** Said for the BadCode Shorts (Priority Lane), worded as never. Talking characters are muted Omni clips dubbed with AI Studio voices through the `lip-sync-dub` skill ([[dubbed-talking-clips-recipe]]).
