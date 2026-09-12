# Thread 08 — GPOM: the narration track, on Suno v6, dry and separate

You are in `~/projects/badcode/badcode`. Read `CLAUDE.md`, then
`docs/stories/gitpush-origin-master/songs/narration.md` (the v5.5 sheet, archived 2026-09-10: the
`badcode newsreader` Voice, weirdness 30 good / 60 broken for speech, words FROZEN, dry-and-separate
structure), `docs/suno-gpt/files/suno-v6.md` (all new work is v6; §3 is the one-word fix ladder),
`docs/suno-gpt/archive/v5.5-era.md` §5 (how a v5.5 sheet starts again on v6), `docs/suno-gpt/session-method.md`,
`docs/suno-gpt/automation.md` (§10 is the listening loop), and the scenes the narration covers:
`scenes/s00-awakening.md`, `s01-the-push.md`, `plant-room.md`, `bulletin.md`. Also read
`docs/stories/camping/narration/` for the sibling method (the camping narration went the same way).

## Goal

A v6 narration sheet for GPOM and, with Kai's yes per run, clean dry spoken takes for cuts 1–3 that Premiere
can lay under the picture. Dry-and-separate is law: **voice and music are never generated together**; the
bed is a flat loopable instrumental; events are one-shots; timing is made in Premiere. The words are
frozen — you may not change a syllable without Kai.

## What done looks like

1. `songs/narration-v6.md`: the new sheet, opening with the "What this song taught" table carried over
   (w60 breaks speech; the faint bed under the voice was the open problem; the newsreader Voice is spoken
   register only and its live display name is `badcode newsreader` — never type the internal label
   `BC-NEWSREADER` into Suno). State the v6 model, controls and Voice attachment per generation.
2. A dry-run of the first `explore` round, shown to Kai, not executed.
3. On each yes: the pair, recorded silently via `record` (no download spent), described with the
   listening tool if thread 05 has unblocked it, filed in `docs/listening/log/`, and the diagnosis written
   before any rewording. One variable per round.
4. Accepted takes noted in the sheet with their Suno IDs; Kai downloads by hand.

## 🔴 Gates

- **Suno is one session at a time and thread 05 (camping) owns it while it runs.** Prepare the sheet and
  the dry run; generate only when Kai says thread 05 has released Suno or is not running.
- Every 20-credit run needs Kai's explicit yes. `status` first; one Suno tab, ever; never navigate away
  from `suno.com/create`; check the form MODE before every fill (Cover state survives a fill); never
  automate a download. Personalize is always OFF (My Taste is retired).
- Attaching a Voice offers to overwrite the Style box: the answer is always **Keep Current**.
- The lyrics editor collapses lines on a programmatic fill: verify by counting paragraphs.

## House rules

Shared checkout: commit per round on `main`, stage only your files, never push, never switch branches.
Rundown style; gloss every scene and ticket.

## First action

Write `narration-v6.md` from the archived sheet and v6 rules, then reply with: the sheet's Style box,
excludes, controls and Voice plan; the dry-run command; and the question "has thread 05 released Suno?"
