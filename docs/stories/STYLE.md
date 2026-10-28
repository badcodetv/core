# Style lives in the story — `look.md` and `sound.md`

**There is no BadCode house style** (Kai, 2026-10-28). BadCode has a narrator's voice (for words,
`docs/voice.md`) and a logo (`docs/brand/`). It has no house sound and no house look. Every story
finds its own, and writes it down in two files in its own folder:

- **`docs/stories/<story>/look.md`**: everything that steers a still or a clip for this story:
  palette, light, lens, preambles, gates, anchor images, cast references.
- **`docs/stories/<story>/sound.md`**: everything that steers a track or a voice for this story:
  genre, singer, narration voice, Style boxes, excludes, settings.

**Why:** a style written anywhere that every session loads (CLAUDE.md, memory, a skill's
description, a skill's defaults) ends up in every prompt. That is how 400+ Bank Robbery takes came
out as one voice, and how every image came back near-black. GPOM's look and sound had become
everybody's. Design: [`design/2026-10-28-no-house-style.md`](../../design/2026-10-28-no-house-style.md).

## The rule for every skill

**Before any prompt for a story (Suno, AI Studio, Flow stills, Flow video), read that story's
`look.md` or `sound.md`.** That file is the only place a style may come from.

- **The file says LOCKED for this part** → use it. Consistency inside a story is the point.
- **The file is empty, or says EXPLORING** → do not invent a default. Run a variation round
  (the `variations` skill): many genuinely different ideas, picked by Kai or Jack, and the pick
  is written back here.
- **A rule learned in one story** (a voice, a palette, a slider value) stays in that story's
  file. It goes into an engine manual (`docs/suno-gpt/`, `docs/flow/`, `docs/google-flow/`) only if
  it is a fact about how the engine behaves, written as a fact, never as "default to…".

What never goes in CLAUDE.md, memory or a skill description: a genre, a BPM, a palette, a
register, a preamble, a voice, a slider value. `scripts/style-lint.py` checks.

## Template: `look.md`

```markdown
# <Story> — look

> The look for this story only. Read before any still or clip (new-image, scene-images,
> scene-animation, flow-prompt). Rules: docs/stories/STYLE.md.

**Status:** LOCKED | EXPLORING | EMPTY — who picked it, when.

## In one paragraph
## Preamble(s)          ← verbatim, ready to paste; one per register if the story has several
## Rules for this story ← gates, what every frame must / must not do
## Anchors              ← reference images and picked stills (path or Flow media id)
## Cast                 ← one canonical reference image per recurring character
## Places               ← recurring locations and how they look
## Never
## Per part             ← scenes or sequences that deliberately differ
## History              ← what was tried and rejected, with pointers
```

## Template: `sound.md`

```markdown
# <Story> — sound

> The sound for this story only. Read before any Suno or voice prompt (suno-prompt,
> suno-automation, variations, scene-timeline voicing). Rules: docs/stories/STYLE.md.

**Status:** LOCKED | EXPLORING | EMPTY — who picked it, when.

## In one paragraph
## Tracks               ← per song: genre, singer(s), the picked take's Style box + exclude +
##                         settings verbatim, lyric file, take id
## Narration / voices   ← narrator and character voices: engine, voice name, direction, settings
## Rules for this story ← standing rules (e.g. "no screaming")
## Never
## History              ← what was tried and rejected, with pointers
```

Stories: [bank-robbery](./bank-robbery/) · [camping](./camping/) · [galileo](./galileo/) ·
[gitpush-origin-master](./gitpush-origin-master/) · [karen](./karen/) ·
[magic-money-tree](./magic-money-tree/) · [storyverse](./storyverse/)
