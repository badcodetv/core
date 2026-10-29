---
name: variations
description: Use to get genuinely DIFFERENT options for a story's Suno song or Flow still/clip — one ideas writer proposes N different ideas, N separate writer subagents each write one prompt without seeing the others, a sameness gate sends back any shared wording, and the passed round runs verbatim. Driven by scripts/variations/round.py. Triggers on "try variations", "explore a new voice / sound / look", "try different ones", "experiment", "give me options that aren't the same", "everything sounds/looks the same", "variation round", "refine this take but change the voice", or any EXPLORING round inside suno-prompt, suno-automation, new-image or scene-images.
---

# Variations: options that are actually different

**Why this exists.** Ask one writer for six options and you get one idea six times. Bank Robbery's
song went 400+ takes as one voice (`docs/suno-gpt/same-song-traps.md`). Jack built the fix on
2026-10-24; Kai turned it into this skill on 2026-10-28 once the house style was removed from
CLAUDE.md, memory and the skills (`docs/stories/STYLE.md`). What is left is the part that makes
variety: **separate writers who cannot copy each other, and a gate that refuses shared wording.**

**You do not write the prompts. Not one word of them.** You collect raw inputs, spawn writers,
run the gate, and run the round. Every step where the session paraphrases, retypes or "tidies"
a prompt is a step where the round converges again.

## When to use it, and when not

| Situation | Use |
| --- | --- |
| The story's `look.md` / `sound.md` is EMPTY (no look or sound at all) | not this skill first: `story-style` finds the direction (it then uses this skill for its test stills) |
| The story's `look.md` / `sound.md` is EXPLORING for this part | **this skill, `explore`** |
| "try different voices / looks", "it all sounds the same" | **this skill** |
| A liked take, change only one thing (the voice, the light) | **this skill, REFINE** (`keep.txt`) |
| The part is LOCKED and you're making the next shot or scene in it | not this skill: write from the story file (`new-image`, `suno-prompt`) |
| Fix one word, one bar, one detail of a take | not this skill: `suno-prompt` §3 ladder / `flow_edit_image` |

## The round folder

Make a folder beside the work (Suno: `docs/stories/<story>/songs/<round>/`; Flow:
`docs/stories/<story>/scenes/<scene>/variations/<round>/`). Put in **raw files only**:

| File | What | Rule |
| --- | --- | --- |
| `ask.md` | the human's message | **verbatim**: paste it, never summarise it |
| `kind` | `suno` or `flow` | |
| `story` | the story's slug | **required**: its `sound.md` / `look.md` goes into the brief verbatim. A round for no story says so with an empty `nostory` file instead |
| `explore` | empty file | finding a new style: only the story file's *Rules* and *Never* sections go in |
| `lyrics.txt` | Suno: the lyric words, no tags | the gate checks every word survives |
| `subject.md` | Flow: what the frame shows | the beat, from the scene's brief, verbatim |
| `listen.md` | ONE fresh listen of the reference | the listener's text verbatim; never an old log |
| `reference.md` | the reference's URL + the engine's stored record | raw |
| `facts.md` | what was run last time, what the human said | facts and quotes only, no theories |
| `keep.txt` | REFINE: the liked take's own box | verbatim from the engine's record, never from our notes |
| `forbid.txt` | phrases no prompt may contain | e.g. the story's *Never* list |
| `preamble.txt` | a LOCKED preamble from the story's file | verbatim; every prompt must start with it, and its words are exempt from the gate |
| `locked-settings.json` | settings the story's file LOCKS for this part, e.g. `{"model": "Nano Banana 2", "aspect": "16:9"}` | only what the file says is locked; every prompt must use them, and the all-identical-settings check skips them |
| `count` | how many | default: the ideas writer chooses (6–10, refine 4–6) |

## The loop

```
python3 scripts/variations/round.py brief <dir>    # brief.md + writers/ideas.ask.md
```
1. **Ideas writer.** Spawn ONE subagent (Agent tool, `general-purpose`) with exactly this prompt:
   `Read <dir>/writers/ideas.ask.md and do exactly what it says.` It writes `writers/ideas.json`.
2. `python3 scripts/variations/round.py asks <dir>` — one `writers/<name>.ask.md` per idea.
3. **Writers, all at once.** Spawn one subagent per ask file **in a single message**, each with
   only `Read <path>.ask.md and do exactly what it says.` None sees another's text.
4. `python3 scripts/variations/round.py gate <dir>`
   - ✅ → `round.json` + `round.gate` (a stamp; an edited round will not run).
   - The gate fails: a voice phrase shared by two prompts (Suno), a 6-word run shared by two, **any
     3-word phrase shared by more than half the round** (both kinds; keep.txt, preamble.txt and
     function-word runs exempt), and **a round where every prompt has identical settings** (keys in
     `locked-settings.json` aside). Flow writers choose `model` and `aspect` per prompt too.
   - 🟡 → `writers/<name>.redo.md` for each offender: spawn one subagent per redo file
     (`Read <path>.redo.md and do exactly what it says.`), then gate again.
   - 🔴 STOP after two rewrites. Tell the human. **No override exists, on purpose.**
5. **Show the round before spending.** Each prompt's one-line idea (from `ideas.json`), the
   settings, and for Suno the dry run: `python3 scripts/variations/round.py run <dir> <title>`.
6. **Run it.**
   - Suno: `python3 scripts/variations/round.py run <dir> <title> --yes` (`--only a,b` retries a
     Create that timed out, still from the stamped round). Mechanics: `suno-automation`.
   - Flow: first `python3 scripts/variations/round.py check <dir>` (verifies the gate stamp; exit 1 =
     the round was edited, do not run it). Then one `flow_generate_image` per `round.json` prompt,
     **text verbatim**, with that prompt's own `model` and `aspect`, count 1.
     Stills are free; video asks Kai first (`scene-animation`).
7. **Pick, then write it back.** The human picks. The pick (its prompt verbatim, the take or media
   id, the settings) goes into the story's `sound.md` / `look.md`, and Status moves to LOCKED for
   that part. That is the only way a style enters the repo.

## Never

- Never write, edit, merge or "improve" a writer's prompt. Never splice a liked sentence from one
  prompt onto another (trap 7).
- Never put old prompts, old listen logs, or `docs/suno-gpt/` / `docs/flow/` rules in the folder.
  The writers research the engine on the web; the brief tells them not to read the repo.
- Never ask one writer for all N prompts (trap 6). Never re-run a failed gate by editing the JSON.
- A new way a round fails → add a row to `docs/suno-gpt/same-song-traps.md` **and** a check to
  `round.py` or `sameness.py`. A trap with only a sentence of advice gets repeated.
