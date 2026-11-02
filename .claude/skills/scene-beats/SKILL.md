---
name: scene-beats
description: Use to decide what one scene of a BadCode film IS before anything is generated — an interview, one or two questions at a time, that settles where it sits, the one sentence it argues, its beats (ending first), what makes each beat interesting, the cast with their reference images, and the look. Writes the scene's brief.md and scene.json. Stage 1 of new-scene. Triggers on "let's talk about <scene>", "what are the beats of <scene>", "brief for <scene>", "what should this scene be", "rough beats", "talk it through before we make anything".
---

# Scene beats (BadCode)

**Stage 1 of a scene.** Decide what the scene is and make it interesting, in conversation, before any
image is made. The next stage is **`scene-images`**; the whole loop is **`new-scene`**; the film it sits
in is the **`overview-board`**.

## Read first

- `docs/marketing/the-reader.md`: who the work is for. Name the beneficiary (advice, not a gate, since Kai's 2026-10-23 ruling), and never raise automation fear unaimed.
- The story's canon (`docs/stories/<story>/README.md`) and the scenes either side of this one.
- The story's overview board (`docs/stories/<story>/timelines.json`): this part's row and its `beat` are the starting sentence.
- **`story-craft`**: the sentence, but/therefore, every beat a step.

## The interview

This works like planning a feature: a back-and-forth, **one or two questions at a time**, never a
questionnaire. Kai often talks in long voice notes, so pull the decisions out of them and play them back.

Settle these before anything is generated:

1. **Where it sits.** Which film, between which scenes, and how long? Is the music fixed? If so, cut points follow the track: note the drop timecodes and the BPM (a beat is 60/BPM seconds).
2. **The one sentence.** What does this scene *argue*? Who benefits, by name or by role? (the-reader rules)
3. **The steps.** The rough sequence of what we see, each step changing something (but/therefore). Write the ending first.
4. **What makes it interesting.** Push past the first idea. For every beat, offer one bolder alternative: a different angle, a reveal, scale against a single human, a callback, or whatever the story's `look.md` makes a rule. Kai's best notes have come from contrast (on GPOM: "zoomed out, a vast parade ground", "a strobe, not a glow", "from outside, through the corner windows").
5. **Cast.** Which characters recur from elsewhere in the story? Find their canonical reference image and their Flow Character, if one exists (`flow_list_characters`). One reference per character, always the same one: the story's `look.md` §Cast names it.
6. **Look and sound.** Read the story's `look.md` and `sound.md` (`docs/stories/STYLE.md`) first; there is no house style. If the story's look is LOCKED, the scene uses it, or names a deliberate break and why. If it is EMPTY, stop and run `story-style` for the whole story first. If it is EXPLORING, list the genuinely different looks worth trying as filters on the board (the mood board is where the story's look gets found, via `variations`). Same for the music and voices the scene needs.
7. **What exists.** Clips or stills already on the timeline that stay, or that must be beaten (they go in `existing` as dashed cards).

## Output

- `docs/stories/<story>/scenes/<scene>/brief.md`: the sentence, the beats with timecodes, the cast with
  reference paths, the look, and what is kept.
- `scene.json`: the format is in **`new-scene`** ("Where things live"). Set `beats`, `styles`, `looks`,
  `existing`, `media` and `flow_project` here.
- **The overview board:** if the scene has no row in `timelines.json` yet, add one with its `beat` and
  `"scene": "scenes/<scene>"`, state `beats agreed`; rebuild and republish (the `overview-board` skill).

Play it back in plain words and get Kai's "yes" before `scene-images`.
