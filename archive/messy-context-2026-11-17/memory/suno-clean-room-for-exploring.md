---
name: suno-clean-room-for-exploring
description: Jack 2026-10-22 — Suno prompts written inside the repo kept making the same song; exploring rounds now go through the variations skill, run verbatim
metadata:
  type: feedback
---

Jack, 2026-10-22: "remember that the repo and suno skills just make the same song, so it is useful to use the clean room or basic version." Learned on The Bank Robbery song: 400+ takes written inside the repo came out as one voice. Since 2026-10-28 the method is Kai's **`variations` skill** (`scripts/variations/round.py`, Suno and Flow); the old `sealed-writer.sh` / `sealed-round.py` are retired.

**What the round must keep (each one cost Jack a round when broken):**
- The writers get raw files only: the user's words verbatim, the lyric words, one fresh listen, the reference's own record. Never my paraphrase, never old listen logs or old prompts.
- Writers never see each other's prompts. A failed sameness gate is a STOP: send it back, never explain the shared part away.
- I never write, retype, edit or "improve" a prompt; the round runs verbatim. My checks are only that the lyric words are unchanged and that the story's own standing rules hold (they are in its `sound.md`).
- Vary the delivery category per prompt, never just the accent. A liked voice sentence moved onto another prompt loses its nationality.
- Agent-tool subagents spawned in the repo inherit CLAUDE.md and memory; "ignore them" does not unload them.

**How to apply:** read `docs/suno-gpt/same-song-traps.md` first; a new failure gets a row there and a guard in the script. The story's style lives in its `sound.md` ([[no-house-style-story-files]]). Suno's cookie banner covers Create (Reject All first). Related: [[bank-robbery-jack-song]].

**Update 2026-11-17:** the writers must be truly sealed: run them with `scripts/variations/sealed-writer.sh` or the `clean-room-writer` agent, never `general-purpose` (which loads CLAUDE.md + this memory). See [[sealed-writers-must-not-see-repo]].
