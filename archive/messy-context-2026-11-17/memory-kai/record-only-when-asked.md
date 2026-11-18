---
name: record-only-when-asked
description: "2026-09-18 Kai: never run suno.mts record off the back of a Create — recording is its own explicit step, only when Kai says record"
metadata:
  type: feedback
---

Generating Suno takes does **not** include recording them. `npx tsx scripts/suno/suno.mts record <id>` runs only when Kai asks in words ("record it", "get me that file", "put it in Premiere"), and then only for the take he picked.

**Why:** Kai, 2026-09-18: *"I want to make sure that recording is a very explicit step… I don't want, when we generate a track, to automatically record it. When I say record, is the only time we should ever run that skill."* It costs no credits, but it takes minutes per take, fills the media folder with takes nobody chose, and assumes the judging is done.

**How to apply:** a round ends when the takes exist, their titles, song IDs and suno.com links are reported, and the round is logged in the song sheet. Then stop. Written into `.claude/skills/suno-automation/SKILL.md` §"RECORD ONLY WHEN THE USER SAYS RECORD" and `docs/suno-gpt/automation.md` §10.

Pairs with [[listen-only-when-asked]]: generating is automatic; hearing and keeping are human-triggered. Related: [[suno-playback-recording]], [[gpom-narration-scored]].
