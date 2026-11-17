---
name: narration-not-lipsync
description: The 2026-10-15 meeting moved The Bank Robbery short and the Karen fix to narration — talking clips muted and dubbed per character, main narrator kept; other films not ruled
metadata:
  type: project
---

**Ruled by Jack and Kai, 2026-10-15:** The Bank Robbery short and the Karen fix move to **multi-narrator narration** (distinct voices, one per character or perspective), no lip-sync. Record: `docs/misc/2026-10-15-meeting.md`.

**Scope:** those two films. Money For Something's dialogue exception was not discussed; for any other film, ask — each story's `sound.md` records how it is voiced ([[no-house-style-story-files]]).

**Why:** viewers love the pictures and hate AI voices on talking characters (Jack's reading of comments on viral AI videos); Kai agreed our bar is higher. Lip-sync may come back later.

**Clarified by Jack, 2026-10-15 evening:** "Each character in their own voice, as a voice-over. dont change the videos, just mute the videos and use the [AI Studio generate-speech] text to speech for each character as they are talking ... whilst keeping our main narrator." So: keep the existing talking clips, mute them, dub each line in that character's own TTS voice where the mouth moves. Recipe: [[dubbed-talking-clips-recipe]]; worked example `scripts/bank-robbery/build-short2.py`. Related: [[never-dialogue-in-flow-videos]], [[bank-robbery-talking-clips-ingredients]].
