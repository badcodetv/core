---
name: scene-dialogue
description: Use to REWRITE the spoken words of one or more BadCode scenes by options — ten writers each push one approach ("shape") to its extreme, one synthesis ranks them harshly and combines the best lines into three drafts per dialogue, and Kai reads and picks on a DIALOGUE PAGE (one tab per dialogue: what's in the cut now, three drafts with a pick button and a note on every line, every writer's version ranked underneath). Rounds run on his notes; picks go into the scene's script and on to voicing in scene-timeline. Sits beside scene-timeline: the words before the voices. Triggers on "dialogue options", "rewrite this dialogue", "this monologue is too long", "give me options for the lines", "tighten the doorstep / the intro", "rank the dialogue", "which draft", "read my dialogue notes", "reflow the dialogue".
---

# Scene dialogue: options → ranked → drafts → picked (BadCode)

**The words before the voices.** A scene's lines have one home (`script.json`, or the voice script a cut
uses); this skill is how they get rewritten when they aren't working. Then **`scene-timeline`** voices
them and puts them on the timeline page. Part of the scene editor (`new-scene`); usable on its own.

Kai, 2026-10-27, after the first round (GPOM's intro and doorstep): *"ranking and reflowing dialogue into
something else could be a skill that we put alongside the rest of the timeline editor skills."* He also
said the first page was hard to follow: the rankings did not link to the dialogue they ranked. **So the
page is built one tab per dialogue, and every ranking row opens that writer's version.** Never go back to
one long document. Kai, on seeing the tabbed page: *"That is so much better… this is brilliant."* Keep the
layout in §3 as it is; change it only on his word.

## When

- A speech is too long for the attention it gets (GPOM: a 55 s intro cut to under 20 s).
- A scene must land an argument without a lecture (the doorstep's game theory).
- Kai asks for options, or his timeline notes say "rewrite this" for more than a line or two. One line
  is a timeline note, answered on the timeline page; a whole dialogue is this skill.

## 1. Talk first: the brief

Agree with Kai, in one message he can answer quickly:

| What | Example (GPOM, 26 Oct) |
| --- | --- |
| **Which dialogues** (one or several; one page covers them all) | Maddie's intro (scene A beat 0), the doorstep (scene B) |
| **Target length** each | 20 s or less · about 60 s |
| **What each must still do** (the plants and payoffs) | she's friendly; he misses us; his worlds failed for want of consciousness; the patrol is out |
| **Protected lines**: Kai's words, kept verbatim if at all possible | "It runs on... well... you." |
| **Rules** | no stated moral; Maddie stays warm and West Country; the lady stays stern; the vote is off screen |
| **What's in the cut now**, and where it lives | `voice3.py` `MADDIE`; `second-half-b-the-door/script.json` |

The brief also names what the writers read first: `docs/voice.md`, `docs/marketing/the-reader.md`,
`docs/story-craft/principles.md`, the story's beats and `timelines.json`, and the scene's own script.

## 2. Run the writers

**`scripts/scene/dialogue-workflow.js`** is the workflow: ten writers (Sonnet), one per shape, each writing
every dialogue, then one synthesis writer. Running this skill counts as asking for the workflow. Run it with
`Workflow({scriptPath: "scripts/scene/dialogue-workflow.js", args: {...}})`, where `args` holds `outdir`,
`title`, `page_title`, `brief`, `dialogues` and optionally `shapes` (the file's header lists them). Nothing in a scene
changes; the writers only write options.

- `outdir` = `design/<date>-<story>-dialogue-<topic>/`. Each writer writes `shape-<NN>-<name>.md` there, and the
  synthesis writes **`options.json`**: the record the page is built from.
- **The house ten shapes** are the default: bone-dry · the picture carries it · the logic said plainly ·
  comedy first · the other side wins · reversal · the chorus · the place is the argument · borrowed craft ·
  ending first. Swap one when the scene calls for it (a comedy scene doesn't need "comedy first"). Each is
  pushed to its **extreme**: the point is to find the edges, as on Suno.
- 📎 A writer can return text without writing its file (GPOM's shape 07 did). The synthesis is told to
  check and fill in missing files. If one is still missing, recover it from the run's journal.

## 3. The dialogue page

```bash
python3 scripts/scene/build-dialogue.py <outdir>/options.json <outdir>.html [--notes <outdir>/notes-r<N>.json]
```

Publish `<outdir>.html` with `capabilities: {db:{}, user:{}}`. Republish to the **same file path** every
round so the link and the notes stay. What Kai gets:

- **A tab per dialogue** (scene and beat under its name), plus an *Open questions* tab.
- In each tab: **Now** (what's in the cut) and the **three drafts** as buttons, one shown at a time, or
  *Side by side*. Each draft shows its bet, its lines (speaker, words with stage directions greyed,
  seconds), its notes, a **Pick** button, a note for the draft and a note on any line.
- A chip on a line (`09`) names the writer it came from. Tapping it opens that writer below.
- **Ten writers, ranked for this dialogue**: rank, verdict and length. Each row opens that writer's
  whole version of the dialogue, with their approach folded above it.
- Built and checked at phone width. Look at it before publishing (a headless screenshot from a script, never
  the shared Chrome).

After publishing, add a line to each scene's trail:
`prov.py trail <scene-dir> --stage dialogue --round N --url <url> --what "dialogue options: <topic>" --rebuild "<the build command>"`.

## 4. Rounds

- **Dump the notes before reading them.** `ArtifactData list` on `notes`, with `out_dir` = `<outdir>/feedback/r<N>/`.
  Keys (from `build-dialogue.py`):
  - `top`: the whole page;
  - `d1`: one dialogue;
  - `d1-1A`: one draft;
  - `d1-1A-L3`: line 3 of that draft;
  - `d1-s09`: writer 09's version;
  - `pick-d1`: the draft id he picked;
  - `q1`: his answer to question 1.
- **A pick with no notes is a go** for that draft as written. A pick with line notes means that draft plus
  those changes. Lines noted from other drafts or writers mean mix them in.
- **Answer on the page.** Write `<outdir>/notes-r<N>.json` with:
  - `round`;
  - `plan`: your read, as short groups ending in *You decide*;
  - `replies`: one answer per note key;
  - `kai_round<N>`: a snapshot of his notes.
  
  Rebuild with `--notes` and republish. Each note then shows *Claude's read* under it.
- **When the next round needs new drafts**, edit `options.json` by hand (a new draft `1D`, a changed line)
  rather than rerunning ten writers. Rerun the workflow only when the brief itself changed.
- Log each ruling with `prov.py trail … --decided "<Kai's words>"`.

## 5. Into the scene

Once a dialogue is picked:
1. Write the lines into the scene's home for words: `script.json` lines with `by: kai` for his words and
   `by: claude` for drafted ones, or the cut's voice script (GPOM: `voice3.py`).
2. Record the pick in the scene's `scene.json`, under `dialogue`: `{page, options, picked, round}`.
3. Hand over to **`scene-timeline`**: voice the new lines, re-time the cut, and republish the timeline page.
   If the scene is in Premiere, the same round also lands as the next `…-r<N+1>` sequence: page and Premiere
   together, never one now and one later (scene-timeline, "No split brain").

## Worked example

GPOM, 26–27 Oct: `design/2026-10-26-gpom-dialogue-options/` (`options.json` plus ten `shape-*.md` files), with
the page at https://claude.ai/artifact/QtMCweEvwqFz6M8CUUdBiN. That first run used a one-off version of the
workflow, and its `options.json` was converted from the synthesis's markdown
(`design/2026-10-26-gpom-dialogue-options.md`). Later runs write `options.json` directly.
