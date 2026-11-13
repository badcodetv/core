You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-13: "please do the suno stuff and put it on the timeline, also fix the clip tool thanks. Please clean room it all and research the internet to achieve it. Thanks."

Earlier, Jack, 2026-11-13: "lets do suno for it all, but add background music as well that fits the scene thanks"
Earlier, Jack, 2026-11-13 (on Suno Speech): "i heard there was a speech only tool on suno, can we do that instead, then we add the sound affects and music after."

## What happened in earlier rounds (facts)

- This round is the BACKGROUND SCORE ONLY for a 14-second vertical short (BadCode Shorts, "Priority Lane"). No voices and no sound effects in it: the dialogue is already recorded separately, and the siren, monitor, rain and flatline tone are made separately. The score sits UNDER shouted dialogue, so it must leave room for voices.
- The picture is already cut. What we see, in order:
  - 0–5.5 s: inside a speeding ambulance at night in the rain, two masked paramedics fighting to save an old man, the driver shouting at the traffic.
  - 5.5–7 s: a red light; a police motorcycle outrider raises his glove. The ambulance stops; a politician's black car glides across in front.
  - 7–10.5 s: the politician in the back of his car, comfortable, on the phone, furious about canapés.
  - 10.5–14 s: back inside, the heart monitor flatlines. The score must stop dead at the flatline (about 10.5–11 s). Silence. Black. Logo.
- The take is generated at 20 seconds so there is room to cut; only the first ~11 seconds are used.
- Last rounds (r3, r4) had voices in them; Jack said they sounded American and every voice the same, and voices were then moved out of Suno. Nobody has heard a score-only take for this short yet.

## This story's standing rules (the round is finding a new style, so only these bind)

## Rules for this story

- **Round 3 (2026-11-13): Suno makes all of the audio:** the crew's shouts in speech mode, the siren, the monitor and the flatline tone, and background music that fits the scene (Jack). The minister's line can be Suno's or Orus.
- **The whole track is about 14 s:** a dying man in an ambulance (0–5 s), held at a red light (5–7 s), the minister's car crossing (7–11 s), then the flatline, silence, and the logo on black (11–14 s). The picture is cut to the track.
- Swearing is said in full, never bleeped. If Suno refuses a word, swap the word.
- No speech in any Flow clip.

## Never

- A cheerful or comedic score: it must feel like real hospital-drama urgency.
- Music over the flatline: it ends in the tone and then silence.

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "v6",
  "durationSec": 20
}
```

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**percussion-only-ensemble** — A percussion ensemble with no melody at all: big floor toms and frame drums played by hand, metal scrapes, a bowed cymbal, and one low drone note for pitch. The lead performers are three drummers locked in an urgent 150 BPM pattern that sounds like a body being worked on, accenting off the beat so it never settles. Ask for it as a genre-first tag list ('cinematic tribal percussion score, no melody') plus one sentence about dynamics: thunderous in the ambulance, suddenly reduced to a single quiet rim tick at the red light and the politician's car, then a cold end with the drone cutting off mid-note. Exclude vocals, chanting, choir, humming, strings, piano, synth lead.

Other writers are doing the other experiments (subliminal-pulse-bed, shepard-rise-ticking, viola-tremolo-dread, uk-procedural-piano-motor, broken-cardiac-electronica). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/shorts/priority-lane/songs/r6-score/writers/percussion-only-ensemble.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/shorts/priority-lane/songs/r6-score/writers/percussion-only-ensemble.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "percussion-only-ensemble". Reply with just the two paths.