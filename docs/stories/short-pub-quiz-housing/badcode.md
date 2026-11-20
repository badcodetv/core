# Pub Quiz: Housing

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode short (9:16 offered, not ruled; about 45-55 s, under 60): a pub quiz question about housing, and one table
whispering its answer against the clock so the next table can't hear. The argument is the short: each person brings what
they know from their own life and work. The point: homelessness already costs billions, spent renting rooms by the night
instead of on homes anyone owns. State: script draft 1 ([script.md](./script.md)), jokes blank for Jack and Kai.

## Look
- Status: EXPLORING (round 1 stills). A proper old English pub (Jack, 2026-11-20: "use unsplash for what the pub looks like,
  make it look like a proper english old pub"): dark wood, brass pumps, etched mirrors, low warm light; never neon, never
  modern. Layout references: Unsplash photos in `<media>/reference/unsplash/` (credits in `scenes/pub-quiz-housing/refs.json`).
- **The table reference is now `table-newbob-a`** (Jack's pick, 2026-11-20): Bob has his own face and a clean olive
  waterproof; the old one read as a famous actor. Faces must be big in a reference before a close-up (docs/rules/flow.md).
- **Picked (Jack, 2026-11-20):** quizmaster **Q1-a-fix-a** (brown tweed three-piece, tweed flat cap, navy roll-neck, gold
  rings over black gloves, navy mask; the Victorian bar with the clock); the table **T3-a-mix-a** (last orders, on-camera flash,
  from slightly above, the green-stool bar; a mixed table). Files in `<media>/stills/r1/` and `r2/`.
- **The quizmaster is BadCode in the balaclava**, dressed in a Guy Ritchie-film-style outfit (Jack, 2026-11-20). In prompts,
  describe the clothes only; never name a film, director, actor or character.
Flow project: `8fa2bbdc-7db6-49b9-893b-cc7b0bd06102` (shown in Flow as "Nov 20 - 11:57"). Stills: Nano Banana 2.1, 9:16.

## Sound
Voices LOCKED (Jack, 2026-11-20, voice page https://claude.ai/artifact/QJzVgufqaftKGgZQMZnpwo). Plain reads: no accent,
age or acting in the prompt; the accent is the voice. Huddle lines are whispered (a short style on those lines only).
- **Quizmaster (BadCode):** `voice_tihz6q1cbfus`, designed: "A Black British cab driver in his fifties from south London, with a deep, gravelly voice and a light accent, who speaks plainly." on `gemini-3.8-flash-tts`, plain.
- **Student:** `voice_ivtrurh0qn32`, designed: "A man of twenty from south London, with a light voice, who speaks plainly." on `gemini-3.8-flash-tts`, plain.
- **Plasterer:** `en-gb-advisor-5` (library, Manchester, 48) on `gemini-3.8-flash-tts`, plain.
- **Banker:** `en-gb-podcaster-11` (library, Liverpool, 57) on `gemini-3.8-flash-tts`, plain.
- **Bob:** Camping's Bob, at Jack's ask: `Algenib` with Camping's profile `docs/stories/camping/narration/profiles/bob-algenib.md`
  on `gemini-3.1-flash-tts-preview` (the model Camping used; still answering 2026-11-20, retired by Google). The
  same-prompt check flags it as MIXED/LEAK: deliberate.
Music: not decided. Any Suno track is music and sound only.

## Story-only rules
- The script comes first (Jack, 2026-11-20); nothing is generated until the script is agreed.
- Whispered, quick, factual: the table argues with reasons, not speeches. Kai: never preachy.
- Nobody at the table is a villain or a pupil, the banker included; Bob is never pitied.
- Numbers (England, MHCLG): councils spent £2.9 billion gross on temporary accommodation in 2025-26 (RO4 outturn, includes
  government housing-benefit money, England total estimated from 377 of 413 councils); £1.8 billion of it on B&Bs and
  nightly-paid lets. Say "B&Bs and nightly-paid lets", never "hotels" alone, never "all council money". Re-check for a
  newer year before posting.
- Bob is the Camping character; his place at the table is Jack's ask (2026-11-20).
- **Pollution, every round** (Jack, 2026-11-20: "please constantly check"): before reporting any round, run
  `scripts/variations/fresh.py --story short-pub-quiz-housing` over every new prompt, line and brief, and say the result in the reply.

## Library pieces in use (Jack, 2026-11-20)
- **Real photo as the look:** an Unsplash photo is attached to each Flow call as the layout; the prompt says what happens in
  it. New Flow pictures built from the photo, never an AI figure pasted into a real photo.
- **Clean room:** prompts are written by a sealed writer from one brief file plus fresh web research (`scenes/pub-quiz-housing/cleanroom/`).
- **The BadCode balaclava:** the quizmaster. Attach `docs/brand/balaclava/mask-reference.jpg` (staged under `~/.cache/`) and
  paste "The balaclava exactly as in the attached image: no holes, no skin, gloves." White ring, red triangle over his left
  eye (right of picture), gloves, no skin, no robot parts. Always say what he wears. Check the mask zoomed on every still.

## Where the detail is
- [README.md](./README.md) (Jack's pitch), [script.md](./script.md), rulings [scenes/pub-quiz-housing/picks.md](./scenes/pub-quiz-housing/picks.md)
