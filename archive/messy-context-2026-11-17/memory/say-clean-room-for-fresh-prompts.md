---
name: say-clean-room-for-fresh-prompts
description: "Jack 2026-10-30 — the words \"clean room\" mean: web research only, sealed writers, no repo prompts or skill phrasing, prompts run verbatim, same-prompt check; the fix for the same-prompt bug"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 73bf0394-8c1a-47fb-b2e3-008f706c9a77
  modified: 2026-10-30T09:42:44.311Z
---

Jack, 2026-10-30: *"i dont want to have to remind you about the same prompt being made bug over and over, so what do i say so that you are aware of that"*. Answer given: he says **"clean room"**.

**Why:** prompts written inside the repo inherit habit wording from old prompts, skills and memory, so everything comes out the same.

**How to apply:** on "clean room", follow [[clean-room-stills-work]]: fresh web research, sealed writers who read only one brief file, run verbatim, `scripts/variations/fresh.py` afterwards, and don't load shot-craft or flow-prompt into the writing. For Bank Robbery MV stills, this is the default even if he doesn't say it. The current scene is `docs/stories/bank-robbery/songs/mv-colour-noir/`.

**Update 2026-11-17:** the writers must be truly sealed: run them with `scripts/variations/sealed-writer.sh` or the `clean-room-writer` agent, never `general-purpose` (which loads CLAUDE.md + this memory). See [[sealed-writers-must-not-see-repo]].
