---
name: content-migration-deferred
description: Storyteller idea-layer migration DONE 2026-07-15; what deliberately remains in the old repo
metadata: 
  node_type: memory
  type: project
  originSessionId: 2054a914-7570-4166-ac37-d28dfac438db
---

**Idea-layer migration is DONE (2026-07-15).** All 51 mineable ideas from the old
Storyteller repo (`~/projects/badcode/storyteller` — both `badcode/{songs,ideas,notes,prompts}`
and `kai/{songs,ideas,stories}`) were captured as individual `docs/ideas/<slug>.md` files
with rows in `docs/ideas/README.md`, which now doubles as the central content map
(inbox table + "Graduated & canon" pointers + "Not migrated" notes). Kai then triaged the
full set same day: 23 ideas kept (20 mined + 3 originals), 29 culled (deleted; names listed
in the README's "Culled at triage" note — re-mine from old repo if wanted), and the three
serial/parallel fragments merged into `serial-parallel-port.md`.

**Why:** consolidates all strewn content in one indexed place; development decisions happen
later via `new-story`.

**How to apply:** don't re-mine the old repo for *ideas* — the inbox is now the source.
What deliberately remains in the old repo (mine per-story, not into the inbox):
expanded per-story narratives in `badcode/prompts/{camping,karen,magic-money-tree,fire-sale,jungle}`
(e.g. Karen's SHAUN_AI plot, GEOFF ghost, Amazon jungle world — relevant to
[[camping-karen-rework-initiative]]), reusable assets (`prompts/system/`, camping
`style.md`, voice/production notes). NOTE: `badcode/songs/voice-instructions.md` contains
a live jammable.com credential — flagged to Kai 2026-07-15; never copy it.
