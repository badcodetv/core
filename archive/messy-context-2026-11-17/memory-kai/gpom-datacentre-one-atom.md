---
name: gpom-datacentre-one-atom
description: GPOM data-centre narration lives in ONE block in songs/narration.md (was narration-canonical.md until 2026-09-24) — words, brass score and mood cues merged
metadata:
  type: project
---

2026-09-21, Kai's instruction: *"let's only have one version, please, because I just got confused
and edited the wrong version."* The data-centre scene (his scene 2, cut 3) had a words-only
`gpom-datacentre` block and a scored `gpom-datacentre-brass` copy; he edited the first while
generations ran from the second, so three rounds came back with superseded words. They are now
merged into a single `gpom-datacentre` atom in
`docs/stories/gitpush-origin-master/songs/narration.md` (renamed from narration-canonical.md 2026-09-24, see [[gpom-narration-file-layout]]).

**Why:** the sheet is the source of truth for a generation, so two copies of the same words is a
silent-wrong-output machine, not a redundancy.

**How to apply:** before any data-centre round, re-read that one block and diff it against what was
last generated — Kai edits live, mid-session. Never reintroduce a second lyric copy; the score and
the cues go *into* his block. The brass score is the opening take's Style box with four instrument
words swapped (cello→brass, violin→muted trumpet). See [[gpom-narration-scored]] and
[[suno-four-box-atom]].
