---
name: sealed-writers-must-not-see-repo
description: 2026-11-17 tested: general-purpose subagents load all of CLAUDE.md + the memory index, so "clean room" writers were not sealed; use scripts/variations/sealed-writer.sh or the clean-room-writer agent; lean on Unsplash real photos
metadata:
  type: feedback
---

Jack asked (2026-11-17) to stop "stuff in the repo affecting the prompts … it's just a merry-go-round" and to look where no one had looked. Found: a `general-purpose` subagent sees the full CLAUDE.md and this memory index (probe, 2026-11-17), so every clean-room writer since Kai's 2026-10-28 switch to subagents was reading other stories' looks and rules. Jack's original 2026-10-24 fix (writers as `claude -p` in an empty /tmp) is restored as `scripts/variations/sealed-writer.sh` (CLAUDE_CODE_DISABLE_CLAUDE_MDS=1, CLAUDE_CODE_DISABLE_AUTO_MEMORY=1, temp folder; tested blank). `.claude/agents/clean-room-writer.md` (omitClaudeMd: true) does the same as a subagent after a session restart.

**Why:** the leak came back through memory growth; the sameness gate and fresh.py only catch it after the fact.
**How to apply:** every clean-room / variations writer runs sealed; the brief is raw inputs + geometry map + one look line. For real-world scenes start from Unsplash photos (`scripts/scene/unsplash-refs.py`), Jack: "the Unsplash fix does seem to solve a lot of these problems". Keep this index lean: story details belong in the story's files, not here. See [[rounds-clear-the-board]], [[clean-room-stills-work]].
