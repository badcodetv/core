# Pub Quiz: Democracy

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode short (9:16, aim 25-35 s), the second episode of the Pub Quiz series, at Jack's ask (2026-11-21): the same
pub, table, quizmaster and voices. A quiz question shows people splitting from their party when they get to choose one
issue at a time; the table argues it out. The point: you shouldn't have to take a whole party for five years, and some
countries already vote issue by issue. State (2026-11-21): **rough cut 1**, 34.7 s, on https://claude.ai/artifact/DEKaVZRAwX8driT4buhyBW. Rebuild: `scripts/shorts/pqd_sync.py` then `scripts/shorts/pqd_cut.py --round 1`. Owed: music, room sound, export.

## Made fast (Jack, 2026-11-21: "the quickest way possible")
- Reuse before making: Bob, three locked voices and the pint-glass outro already exist. New clips only where a line
  needs a face that says it.
- Lines spoken plainly, never whispered.
- Few on-camera talkers: lines over wides, reactions and backs of heads wherever the mouth needn't show; the
  quizmaster's mouth is under the mask, so his lines need no sync.
- The script is agreed before anything is generated; the page notes are read before every rebuild.

## Look
Status: EXPLORING (stills round 1). Jack, 2026-11-21: "it should be a english countryside pub this time", "use unsplash".
- An English countryside pub, evening: low dark beams, flagstones, small wooden tables, warm lamps; the outside an
  ivy-covered stone pub on a village street. Layouts: Unsplash `lX31bAy6ML0` (main room), `R6ddisVdIfU` (the quiz table),
  `ULysA-AxywY` (the bar end), `5Ns22AXZ0D4` (outside); credits in `scenes/pub-quiz-democracy/refs.json`. No readable words.
- **The quizmaster:** BadCode in the balaclava as an over-the-top American stereotype (Jack: "american streotypical
  version"; Jack 2026-11-21: "make his mask denim"): a faded blue denim balaclava (white ring, red triangle over his left eye), white cowboy hat, blue denim western shirt with pearl snaps, bolo tie, big silver buckle, black gloves,
  a microphone. No sunglasses (they hide the triangle). Describe the clothes only; never name a person, film or character. For his shots attach his denim portrait, not the navy mask reference (it turns the mask navy); to fix a mask, edit the still and change only the cloth. On a turned head check WHICH EYE the triangle is over, not which side of the picture it sits (two picked stills had it on his right eye).
- **The table:** the Florida tourist (white American woman ~55, highlighted blonde bob, turquoise fleece over a pink
  polo), the Swiss bloke (white, ~40, neat brown hair, trimmed beard, rimless glasses, navy gilet over a grey jumper),
  the one-party voter (Black British man ~70, grey hair and moustache, brown tweed jacket, checked shirt, knitted tie),
  and Bob (his portrait `bob-face.jpg`, from the series).
- Portraits first, big face, one per person, attached to every shot of them; name every extra (age, hair, clothes).
Flow project: `8fa2bbdc-7db6-49b9-893b-cc7b0bd06102` (the series' project). Stills Nano Banana 2.1, 9:16; clips Omni 1.2 Flash, Frames, 8 s.

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
