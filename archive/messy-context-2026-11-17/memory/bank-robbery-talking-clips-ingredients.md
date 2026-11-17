---
name: bank-robbery-talking-clips-ingredients
description: For Bank Robbery dialogue, make talking clips in Ingredients with the still as scene and the speaker's Character attached, one speaker a clip; Frames gave wandering accents
metadata:
  type: project
---

On 2026-10-09 Jack said cut 6 still had American accents. Re-making nineteen lines in **Ingredients mode** (the still as the scene, the speaker's Flow Character attached for its saved voice, the accent named inside the speech clause, one speaker a clip) got every one heard as British by the listening model, and kept the still's framing in most. Frames mode had been used before and the accents wandered.

**Why:** Google's Flow help says a custom voice attaches only to Ingredients generations. Our result fits that but only a machine has listened; Jack has not yet confirmed by ear.

**How to apply:** for any new Bank Robbery talking clip use `scripts/bank-robbery/br-clips-v7.mjs` with `mode: ingredients`. Attach every Character who is visible, or the others get replaced by strangers. Keep pistols and "newsreader at a protest" wording out, or Flow refuses. Record: `docs/google-flow/omni-flash.md` (2026-10-09) and `docs/stories/bank-robbery/stills-v7.md`. See [[bank-robbery-resume]], [[bank-robbery-cast-flow-characters]], [[never-dialogue-in-flow-videos]].

**Parked 2026-10-15:** the meeting moved the films to narration only, no talking clips ([[narration-not-lipsync]]). Keep the recipe for if lip-sync returns.

**Update 2026-10-18 (short cut 4):** since the films moved to muted clips with TTS dubs ([[narration-not-lipsync]]), the accent reason for Ingredients is gone. Ingredients rebuilt the room on 2 of 9 café clips (a prompt naming a TV got a TV and lost the painting); Frames held the still exactly. For a clip that will be dubbed, use Frames with "talks" and no line. Record: `docs/google-flow/omni-flash.md`, 2026-10-18.
