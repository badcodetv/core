---
name: no-house-style-story-files
description: Kai 2026-10-28 — no BadCode house look or sound; every style rule goes in the story's look.md / sound.md, never in memory
metadata:
  type: feedback
---

Kai, 2026-10-28: BadCode has a narrator's voice and a logo, not a look or a sound. Style words saved in CLAUDE.md, memory or a skill description leaked into every prompt (why Bank Robbery songs came out as one voice, and why images drifted towards GPOM's dark look). Rules: `docs/stories/STYLE.md`.

**Why:** anything every session loads ends up in every prompt.

**How to apply:** when Jack picks or rules on a look or sound, write it into `docs/stories/<story>/look.md` or `sound.md` (LOCKED / EXPLORING / EMPTY), and keep only a pointer and the project state in memory. Exploring rounds go through the `variations` skill. After editing memory, run `python3 scripts/style-lint.py`. Related: [[suno-clean-room-for-exploring]], [[bank-robbery-mv-alt-style]].
