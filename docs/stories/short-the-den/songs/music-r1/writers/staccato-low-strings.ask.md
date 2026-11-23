You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

please make dragons den like backround music. thanks

## What happened in earlier rounds (facts)

- The music goes under a 9:16 short that runs 42.8 seconds (rough cut 3): nine short spoken lines between 0.4 s and 32 s,
  then a 5 s end card with a fact, then a 5 s logo outro on a rainy window.
- Nothing has been run for this short's music before; no take exists.
- Every spoken line is a separate voice track laid over the music; the music must leave room for speech.

## This story's standing rules (the round is finding a new style, so only these bind)

## Story-only rules
- The script comes first; nothing is generated until Jack agrees it ([script.md](./script.md)). Lines are Claude's drafts until Jack or Kai rewrites them.
- The closing card is the NAO finding (Jack, 2026-11-23: "it should be about government investing going wrong, you showed
  me the original quote please use that"), read at source: NAO, Evaluating government spending (HC 860, Dec 2021), para 8:
  9 of 108 major projects, £35bn (8%) of £432bn, had plans for robust impact evaluation. Was Petrosino et al. 2013 (rough cuts 1-2).
- The nurse's numbers (one ward, six months, a tenth) are the joke's, never shown as a statistic.
- 🔴 Parody only: our own title on release (to decide), no show name, logo, theme or real person's face.

## Never write these

Dragons' Den
Dragons Den
Dragon
BBC

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**staccato-low-strings** — Describe a scene instead of genres: a hushed, high-stakes studio where a nervous entrepreneur pitches to stern, silent investors. The lead is a section of low cellos and basses playing short, clipped staccato strokes, with soft timpani rolls and one muted brass swell when the verdict lands. Ask for slow-burning orchestral TV-drama suspense around 100 BPM. Keep the violins out of the high melody so the speech isn't covered. Exclude synths, drum kit, choir and vocals.

Other writers are doing the other experiments (analog-synth-pulse, lone-piano-clock, industrial-hits-timeline). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-the-den/songs/music-r1/writers/staccato-low-strings.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-the-den/songs/music-r1/writers/staccato-low-strings.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "staccato-low-strings". Reply with just the two paths.