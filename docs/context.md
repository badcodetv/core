# How context works in this repo (the 2026-11-17 reset)

> Jack, with full permission from Kai (`docs/misc/2026-11-17-meeting.md`). The old setup, unchanged, is in
> `archive/messy-context-2026-11-17/` (CLAUDE.md and all 129 memory files).

## In five sentences (for Kai)

1. `CLAUDE.md` is now one page (7 KB, down from 31 KB, with memory down from 60+ rules to one line), and holds
   only what is true for every task: what BadCode is, the four ideas every piece serves, a few working rules,
   and where things live.
2. Every story and short has one short `badcode.md` at the top of its folder (current look, sound, rules and
   library pieces, no history, no other story named), and it is the only story file read before a prompt: the
   long `look.md` / `sound.md` stay as the record.
3. `docs/library/` is the tool shed (80 looks, 79 sounds and a `tricks/` page such as the Unsplash reference
   photo and the clean room); it applies to nothing until a story copies a piece into its `badcode.md`.
4. Starting a story, Claude proposes which library pieces to take in, and Jack or Kai picks: that is the new
   `new-story` / `new-short` step, and it is being tested on the Freddo Mortgage short.
5. Engine mechanics that used to live in Jack's private memory are now in the repo, in `docs/rules/`
   (flow, suno, voices, premiere, working), so both machines share them and nothing story-shaped rides along.

## What loads when

| When | What loads | Size |
| --- | --- | --- |
| Every session | `CLAUDE.md`, the one-line memory index, the skill descriptions | ~7 KB + ~1 line + descriptions |
| Working on a story | its `badcode.md` | 40-75 lines |
| Driving an engine | `docs/rules/<engine>.md` + that engine's skill | on demand |
| Setting up or restyling a story | `docs/library/` | on demand |
| A detail `badcode.md` points to | the story's `look.md` / `sound.md`, briefs, reviews | on demand |

## Why the earlier clean-ups leaked (what this one changes)

| Leak | Earlier fix | Why it still leaked | Now |
| --- | --- | --- | --- |
| Style in always-loaded files | 10-28: moved to `look.md` / `sound.md`; a lint | Memory kept 60+ rules, some carrying one story's look or sound (a sound spec, a costume, another story's look inside the clean-room rule) | Memory emptied; rules in `docs/rules/`, story items stay archived |
| The story's own file | — | `look.md` files run to 430 lines with superseded rules kept inline (strikethroughs, "from cut 8", old preambles) and several parts' looks in one file. The model grabs keywords from the dead parts too | `badcode.md`, current only; skills and `scripts/variations/round.py` read it first |
| Compulsory shared docs | 10-29: labelled examples | `docs/cinematography/` (compulsory before every prompt) treated one story's dark, monumental register as BadCode's own; `nano-banana-2.md` told "any story's preamble" to use a camera, stock and ISO; the voice guide said "change one field at a time from" one story's voice | Rewritten as conditional ("only if a story's look is...") |
| Film-look words | The lint | The lint did not know "35mm", "film grain", "Portra", "monumental", "baritone", and it lets any line that names a story through | Words added; `camera-vocabulary.md` labelled "a vocabulary, not a default" |

## What can still leak (be aware)

- 🔴 **Reference images and Flow projects.** Flow follows a reference image more than the prompt, so a reused
  reference or Character carries a look with it. The Flow MCP uses whichever project tab is open (it is not tied
  to a story), and whether a reference chip left over from an earlier generation rides into the next one is
  **untested**. Use one Flow project per story; Kai's parallel-tab rework of the Flow driver is the place to
  enforce it.
- ✅ **Kai's machine memory** got the same treatment on 2026-11-18: archived to
  `archive/messy-context-2026-11-17/memory-kai/` (136 files), engine rules moved into `docs/rules/` (new
  `youtube.md`), memory emptied to one file saying rules live in the repo.
- 🟡 **Shared engine docs still carry ~500 style words**, mostly labelled with the story they came from (voice
  names in the AI Studio guide, Suno settings measured on one story). They are read on demand, and a labelled
  example is still an example. `python3 scripts/style-lint.py --summary` lists them; fix them as they come up.
- 🟡 **Skill bodies are long** (~420 KB in all) and carry labelled examples. Each now says a story's examples are
  that story's, never a default.
- 🟡 **`badcode.md` goes stale** if a pick is written only into `look.md`. The rule: a pick updates `badcode.md`
  too (`docs/stories/STYLE.md`, `story-style` step 5). Several were already stale when written (the writers
  marked them "Unclear").
- 🟢 **The same-prompt hook** only echoes a phrase the new prompt already contains; it never adds one.

## Where to put a new rule

| It is about… | It goes in |
| --- | --- |
| One story | that story's `badcode.md` |
| How an engine behaves, or how to drive it | `docs/rules/<engine>.md` (or the engine manual, written as a fact) |
| How Jack and Kai like to work | `docs/rules/working.md` |
| A look, sound or method more than one story might want | `docs/library/` (a story takes it in by copying) |
| Every task, always | `CLAUDE.md`, one line, ask first |
