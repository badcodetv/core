---
name: stupidity-optimised-resume
description: "Stupidity Optimised: rough 4 BUILT 2026-11-02 (6:54, sped-up voices), unwatched; Gemini's cut suggestions in scenes/film.md 'Premiere, rough 4'; branch stupidity-optimised-script"
metadata:
  node_type: memory
  type: project
  originSessionId: dc1998c2-9211-4ed8-9fc6-3d2a2893310b
  modified: 2026-11-01T14:22:06.618Z
---

Jack and I wrote `docs/stories/stupidity-optimised/script.md` one scene at a time, on branch `stupidity-optimised-script` (the story is not on main). First pass finished 2026-11-01: the film ends on Scene 17, with Giles saying "Asset dealt with" (Jack's ruling). Scenes 8 and 18–25 are gone, kept at the bottom of the file. Scenes 9 and 11–16 are my drafts at his request. Still owed: the app's line in Scene 10 beat 1, names for Prophets 1 and 5. The narrator's promise in Scene 1 was removed at his request.

**Why:** he wants to write the jokes himself, see [[jack-writes-the-jokes]], which he confirmed by using the beat format here.

**How to apply:** show only the next scene's beat table, take his lines, tidy typos only, move on when he says "next". If he says "do this" or "write it", write the scene short and mark it as my draft. There is no Mum in this story (his ruling).

**Film rough 2 BUILT (2026-11-01):** Premiere `Optimised rough 2` in Jack's project: 72 shots, 87 voice lines, 7 Kevin MacLeod cues (CC BY, credit required, in `sound.md`), unheard by anyone human. Ledger: `docs/stories/stupidity-optimised/scenes/film.md`. Open: the glitchy line Jack sees, not in the files, needs his screenshot. Nothing committed yet.

**Rough 3 BUILT (2026-11-02 pm):** Premiere `Optimised rough 3` (9:26): app on phones (V3), 24 lip-synced shots (V2), the water block and label replay inserted, clip sound capped at -38 dB, m5/m6 longer. Nobody has watched it. Next = Jack's notes on rough 3. Ledger and open items: "Premiere, rough 3" in `docs/stories/stupidity-optimised/scenes/film.md`. Rebuild kit: `scripts/stupidity-optimised/rough3-plan.py` + `rough3-place.py`. Superseded by rough 4.

**Rough 4 BUILT (2026-11-02, late):** Jack said too long and too slow. `Optimised rough 4` = rough 3 with every voice faster (×1.08–1.3, pauses squeezed; ×2 sounded rushed), gaps halved, clip tails trimmed, lip sync and graphics re-timed to match: 9:26 → 6:54, nothing removed. Unwatched. Next = Jack's call on what to cut (Gemini's suggestions, unverified, in "Premiere, rough 4" in film.md). Rebuild kit: `fast-voices.py` → `rough4-plan.py` → `rough3-place.py`; `proxy.py` for a scratchpad watch copy. Nothing committed since 43af873.
