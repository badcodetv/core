---
name: no-house-style
description: "2026-10-28 Kai: there is NO BadCode house style; each story's look and sound live only in docs/stories/<story>/look.md + sound.md; nothing stylistic in CLAUDE.md, memory or skill descriptions"
metadata:
  type: feedback
---

**Ruled 2026-10-28 by Kai:** BadCode has a narrator's voice (words) and a logo, and no house sound or
look. Drum & bass is one track's choice, not BadCode's identity; the near-black monolith and 35mm
documentary looks are GPOM's. Every story's style lives in `docs/stories/<story>/look.md` and
`sound.md` (templates: `docs/stories/STYLE.md`); every skill reads them before any prompt.

**Why:** Jack found Suno prompts converged (400+ Bank Robbery takes, one voice) because rules loaded in
every session (CLAUDE.md, memory, skill descriptions) leaked into every prompt; his fix ran writers in
an empty folder. Kai: remove the pollution instead of routing round it.

**How to apply:** never write a genre, palette, register, preamble, voice or slider value into a
memory, CLAUDE.md or a skill description; write it into the story's file and point to it. EMPTY story
file → the `story-style` skill (interview → options from `docs/style-library/` + one invented → picking
page → write back; Kai asked for it 2026-10-28 so each story's identity is strong but its own).
EXPLORING → the `variations` skill (separate writers + sameness gate). Never a default. Only
story-style may point at the library (the lint fails otherwise: a menu everyone reads is a house style).
Check with `python3 scripts/style-lint.py`. Design: `design/2026-10-28-no-house-style.md`.
Related: [[suno-four-box-atom]], [[new-image-skill]].
