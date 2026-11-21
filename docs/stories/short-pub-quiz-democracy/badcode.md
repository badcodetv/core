# Pub Quiz: Democracy

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode short (9:16, aim 25-35 s), the second episode of the Pub Quiz series, at Jack's ask (2026-11-21): the same
pub, table, quizmaster and voices. A quiz question shows people splitting from their party when they get to choose one
issue at a time; the table argues it out. The point: you shouldn't have to take a whole party for five years, and some
countries already vote issue by issue. State: script draft 1 ([script.md](./script.md)), nothing generated.

## Made fast (Jack, 2026-11-21: "the quickest way possible")
- Reuse before making: the cast, the pub, the voices and the outro already exist (below). New clips only where a line
  needs a face that says it.
- Lines spoken plainly, never whispered.
- Few on-camera talkers: lines over wides, reactions and backs of heads wherever the mouth needn't show; the
  quizmaster's mouth is under the mask, so his lines need no sync.
- The script is agreed before anything is generated; the page notes are read before every rebuild.

## Look
Same pub and cast as the first Pub Quiz (Jack's ask). A proper old English pub: dark wood, brass pumps, etched mirrors,
low warm light; never neon, never modern. Status: LOCKED (inherited).
- Cast portraits (attach to every shot of that person), in the Pub Quiz: Housing media folder: Bob `stills/r6/bob-face-a.jpg`,
  the plasterer `stills/r5/plasterer-face-a.jpg`, the student `stills/r3/S05-a.jpg`, the banker `stills/r3/S07-a.jpg`,
  the quizmaster `stills/r1/Q1-a-fix-a.jpg`. Table reference `table-newbob-a`.
- The quizmaster is BadCode in the balaclava, in a brown tweed three-piece, tweed flat cap, navy roll-neck, gold rings
  over black gloves. Describe the clothes only; never name a film, director, actor or character.
- Faces must be big in a reference before a close-up; name every extra person (age, hair, clothes).
- Reusable clips (Pub Quiz: Housing media `video/`): quizmaster asks `pq-01a-P01`, quizmaster reads the answer `pq-10a-P10`,
  the huddle `pq-02b-P02`, from above `pq-11b-P11`, the student stung `pq-05a-P05`, the pour `pq-G01ma-G01`.
Flow project: `8fa2bbdc-7db6-49b9-893b-cc7b0bd06102` (the series' project, Jack's ask). Stills Nano Banana 2.1, 9:16; clips Omni 1.2 Flash, Frames, 8 s.

## Sound
Voices LOCKED (the same cast). Plain reads: no accent, age or acting in the prompt. Style "fast, brisk" on every line.
- Quizmaster (BadCode): `voice_tihz6q1cbfus` on `gemini-3.8-flash-tts`.
- Student: `voice_ivtrurh0qn32` on `gemini-3.8-flash-tts`.
- Plasterer: `en-gb-advisor-5` on `gemini-3.8-flash-tts`.
- Banker: `en-gb-podcaster-11` on `gemini-3.8-flash-tts`.
- Bob: `Algenib` with the profile `docs/stories/camping/narration/profiles/bob-algenib.md` on `gemini-3.1-flash-tts-preview`
  (Jack's ask; the same-prompt check flags it MIXED/LEAK, deliberate).
Music: not decided. Pub room bed from the no-dialogue clips' own sound, kept low under the voices.

## Story-only rules
- Jack and Kai write the jokes; every joke slot stays blank until they fill it.
- Nobody at the table is a villain or a pupil; Bob is never pitied; never preachy.
- Facts only from [`../../ideas/you-can-pick-and-choose.md`](../../ideas/you-can-pick-and-choose.md), re-checked before posting.
  Florida 2020: the $15 minimum wage passed with 60.8% ("sixty-one percent" rounds it) on the ballot where Trump won the
  state. Switzerland: about four national voting days a year.
- No AI likeness of a real politician: Trump is named, never shown.
- Run `scripts/variations/fresh.py --story short-pub-quiz-democracy` over every new prompt and line, and say the result.

## Library pieces in use
- **Real photo as the look:** an Unsplash pub photo as the layout for any new Flow picture; never an AI figure pasted into a real photo.
- **Clean room:** new prompts written by a sealed writer from one brief file.
- **The BadCode balaclava:** the quizmaster. Attach `docs/brand/balaclava/mask-reference.jpg` and paste "The balaclava
  exactly as in the attached image: no holes, no skin, gloves." Check the mask zoomed on every still.

## Where the detail is
- [README.md](./README.md), [script.md](./script.md), rulings [scenes/pub-quiz-democracy/picks.md](./scenes/pub-quiz-democracy/picks.md)
