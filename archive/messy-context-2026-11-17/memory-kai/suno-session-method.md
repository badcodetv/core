---
name: suno-session-method
description: "2026-08-21 — docs/suno-gpt/session-method.md is the entry point for any multi-round song session; per-song history files open with a 'What this song taught' table"
metadata:
  type: project
---

The Suno toolkit gained a **method layer** on 2026-08-21, out of the 17-round Camping duet
re-cut. `docs/suno-gpt/files/*` holds *what is true about Suno*;
**`docs/suno-gpt/session-method.md`** holds *how to work*, and it is what to open before any
multi-round session on an existing song (a re-cut, a "this isn't right yet" loop, or picking
up a song someone else iterated on). The `suno-prompt` skill routes to it.

**The three layers it defines, which must stay separate or the toolkit rots:** the *sheet*
(`songs/<song>.md`, the boxes you paste), the *log* (`songs/<song>-prompt-history.md`, what
failed each round), and the *rules* (`docs/suno-gpt/files/`, true of Suno not of this song).
The sorting test: would this sentence still be useful on a different song?

**Convention, now expected of every song:** `<song>-prompt-history.md` opens with a **"What
this song taught"** table — what broke · why · the fix · where the general rule now lives.
An empty last column means a lesson that has not been promoted yet. Worked example, 17 rows:
`docs/stories/camping/songs/camping-prompt-history.md`.

**Why:** lessons were being learned per-song and left there, so the next song paid for them
again. The most expensive single lesson of the Camping session (~6 rounds) was procedural,
not factual: *when N wordings of one idea each fail differently, the category is wrong, not
the wording.* That belongs nowhere in a file about Suno's tag syntax.

**How to apply:** read it before iterating, not after. Its opening checklist — read the sheet
in full (never from memory; Kai edits between turns), read the song's summary table, skim the
known-unreliable list, grep Exclude *and* My Taste before adding any instrument, baseline
before changing anything — is the cheapest part and prevents most repeat work.
Related: [[suno-voice-playbook]], [[camping-duet-recut]].
