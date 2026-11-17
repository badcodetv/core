---
name: never-write-uniformity-words
description: In a Suno prompt, a uniformity word (never, throughout, from here to the end, every bar) is a flatness instruction — scope the guard to where the bug was instead
metadata:
  type: feedback
---

Found on Camping, 2026-09-21 (Jack: *"they all sound flat and boring"*): three clauses we had written to fix real bugs each told the record never to change. The rule, the table and the corollary (differentiate repeated section headers; make the last one `[Final Chorus]`) are in `docs/suno-gpt/files/suno-tag-mechanics.md` (~L245), promoted there the same day.

🔑 **Watch the words `never`, `throughout`, `from here to the end`, `every bar`, `start to finish`.** Scope the guard to where the bug actually was.

**Same family:** the Lyrics box out-votes the Style box on casting. When the cast or the arrangement changes, rewrite every section cue and assert the old words are gone in code (a no-op replace looks like success). Related: [[a-ban-loses-to-a-positive-instruction]].
