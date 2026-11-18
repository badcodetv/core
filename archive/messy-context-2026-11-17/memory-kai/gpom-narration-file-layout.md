---
name: gpom-narration-file-layout
description: "2026-09-24: GPOM songs/narration.md = LIVE only (its narration settings + template + one atom per scene), history newest-first; mirrored in GPOM sound.md"
metadata:
  type: project
---

2026-09-24, Kai: the narration sheet had grown to thousands of lines of old rounds and he couldn't
read or hand-edit it. Reorganised on his rulings:

- `docs/stories/gitpush-origin-master/songs/narration.md` — **LIVE only**: scene table (Kai's
  scene numbers + aliases), GPOM's narration settings, GPOM's narration template, then per scene: pick + one atom.
- `songs/narration-history.md` — every round, **newest first**; log new rounds at the TOP. Next round is r55.
- `songs/archive/narration-v6.md` (r1–r41) and `songs/archive/narration-v5.5.md` (was `narration.md`).
  `narration-canonical.md` no longer exists.
- **GPOM's narration template = one template, four blanks** (PALETTE, FAMILY, ARC, ENDING drum|hollow) + one
  Exclude box. `python3 scripts/suno/narration-drift.py` reports drift; scene 1 is 🔒 frozen
  (picked before the template).
- **GPOM's narration settings = scene 2's pick:** Style Influence 50, Audio Influence 65, weirdness 25.
  The old "weirdness 10/20 only" rule is retired.

**Why:** Kai wants to open the live file, read it, and edit words by hand without a round-trip
through Claude, and he feared the Style box drifting between scenes.

**How to apply:** never put round logs in narration.md; never copy a live atom heading into the
history file (a duplicate atom is how stale words got generated, see [[gpom-datacentre-one-atom]]).
Run the drift check after any Style edit. Supersedes the locked style in [[gpom-narration-scored]].
