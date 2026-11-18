---
name: gpom-narration-scored
description: "GPOM narration = Suno v6 + badcode newsreader Voice + score in ONE take; 2026-09-17 the house style is LOCKED at the top of songs/narration-v6.md (short prompt, sparse cello/violin/piano swell, w35) — start every scene there"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bac0f72a-b2b9-4ac0-95a5-ff2cbadd5647
  modified: 2026-09-17T17:19:09.140Z
---

**Ruled 2026-09-16 by Kai:** GPOM narration stays on **Suno v6** with the `badcode newsreader`
Voice attached, and *"the music for the GitPush story is actually a feature"* — voice and score are
generated together. This overrides [[dry-and-separate-narration]] for GPOM.

**2026-09-17 — the style is LOCKED (Kai):** the dense Zimmer score of 09-16 lost. What won is a
short prompt: calm British newsreader over dark cello, violin and piano that start near-silent and
swell to a peak, one drum hit to end; one cue line on the lyrics, `[Build]` before the last three
lines, no per-line direction, v6, SI 75, AI 50, weirdness 35 (pair 20/35), Variety off. Scene 1 take
`5cd52d68` is on `gpom-s01` A3.

**2026-09-17 later — scenes 1+2 are ONE take (Kai: "we've nailed it"):** separately generated scenes didn't match
musically, and Extend joins still had seams. What won was regenerating both scenes as one lyric sheet in the locked
style: §22 `cut12-origin-master`, pick `544fe82f`, w10, Duration 90, on `gpom-s01` A4 at 0. Kai does the timing by hand.
Scene 2's words are now "…pushing themselves, from their origin... to a master. / Me." (the command is on screen,
not spoken). Default for following scenes: generate adjacent scenes together, and switch music at a scene cut only on purpose.
Weirdness 35 garbled scene 2, so use 10/20.

**Why:** long cue-heavy prompts made the voice invent words on v6; see [[suno-v6-simple-prompts]].

**How to apply:** ⚠️ superseded 2026-09-24 — start every new GPOM scene from the house style template
in `docs/stories/gitpush-origin-master/songs/narration.md` (see [[gpom-narration-file-layout]]); the
2026-09-17 locked style now lives in `songs/archive/narration-v6.md` as history. Words change only with Kai.

Related: [[suno-v6]], [[suno-voice-playbook]], [[gpom-short-cut]]
