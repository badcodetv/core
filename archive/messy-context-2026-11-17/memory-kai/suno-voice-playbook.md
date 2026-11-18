---
name: suno-voice-playbook
description: "2026-08-05 — Karen voice war distilled; suno-prompt skill now has a \"Getting a specific voice\" section; docs/suno-gpt/suno-voices.md is the merged evidence base"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9861d864-ed66-4376-b84a-5390f5c9b583
  modified: 2026-08-05T21:05:39.184Z
---
**Scope (2026-10-28):** the voices themselves are Karen's and Camping's (their `sound.md` files); what is general here is the engine fact that the genre word picks the singer, and the ladder as one option. See [[no-house-style]].


The eight-round fight to get Karen's whiny voice ("All Day to Complain") produced a general voice
playbook, merged 2026-08-05:

- **`docs/suno-gpt/suno-voices.md`** — both threads' learnings in full (was a staging doc, now the
  deep reference). Core discovery: the genre tag picks the *vocalist pool*; prompting can't jump
  pools — the fix is the Voice-transplant ladder (probe-farm in the voice's home genre → Remix →
  Voice with sub-region → apply with audio influence → two-pass Cover). Also: My Taste cannot be
  disabled, only replaced; the parenthesis slot escapes the genre's vocal prior.
- **`.claude/skills/suno-prompt/SKILL.md`** — flattened into a "Getting a specific voice" section,
  plus refinement-loop rules (re-paste all four boxes every round; stop prompting a vocal after ~2
  dead rounds) and an interview question for character leads.
- `docs/suno-gpt/files/suno-controls-and-workflows.md` §"My Taste" corrected against the live UI
  (there is no off switch).

**Why:** six rounds of style-prompt surgery could not move a vocal the genre prior owned; only the
saved-Voice transplant worked. The song file `docs/stories/karen/songs/all-day-to-complain.md`
carries the full round-by-round revision log. Related: [[karen-consolidation]].

**Bounded 2026-08-21 by the Camping duet re-cut — read this before reaching for the ladder.**
A saved Voice **binds the lead slot for the whole track; it has no section scope**, which is
exactly what made Bob and Tarquin sound like the same man on the released Camping take. So the
transplant ladder above is right for a *single* character lead and **wrong for two characters in
one generation**. For a duet, cast by contrast instead — pitch, texture, tradition, delivery,
age/class, room — and let the **genre tag** own the vocalist pool, since a pool carries a whole
performer (accent, age, class, race) as one package. A saved Voice becomes correct again only if
you generate each character separately and join in production. Evidence: `suno-voices.md` Thread 4
and `docs/stories/camping/songs/camping-prompt-history.md`.

**How to apply:** when any future track needs a character voice, the skill now handles it natively —
trust its escalation ladder instead of iterating style prompts. As of 2026-08-05 the Karen track had
the Voice working and the chorus recast as the institution's smooth choir (round 8), not yet final.
