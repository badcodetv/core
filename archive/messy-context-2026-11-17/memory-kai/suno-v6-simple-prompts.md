---
name: suno-v6-simple-prompts
description: "GPOM narration finding on Suno v6 (short box + one cue beat dense cues); its numbers live in GPOM's sound.md"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bac0f72a-b2b9-4ac0-95a5-ff2cbadd5647
  modified: 2026-09-17T12:39:32.283Z
---
**Scope (2026-10-28):** learned on GPOM's narration; the numbers are GPOM's and live in `docs/stories/gitpush-origin-master/sound.md`. The engine fact (v6 mangled words under a long cue-heavy box) is in `docs/suno-gpt/files/suno-v6.md` ([[no-house-style]]).

On Suno v6, GPOM narration with a ~1,000-char style box, emotional bracket cues on every line and weirdness 40/60 came back with mangled and invented words (rounds r6/r7; dropping Audio Influence 50→35 did not fix it). A ~200-char style box, a single top cue, no per-line direction and weirdness 10 gave clean words — Kai: "that sounds perfect" (r8).

**Why:** v5.5 obeyed dense bracket architecture; v6 seems to get confused by it. Which of the three changes mattered most is not yet separated.

**How to apply:** for v6 spoken narration, start from the short r8 recipe (narration-v6.md §11) and build up one element at a time (§12 onward), rather than porting the long v5.5-style cue-heavy atoms. Related: [[suno-v6]], [[gpom-narration-scored]].
