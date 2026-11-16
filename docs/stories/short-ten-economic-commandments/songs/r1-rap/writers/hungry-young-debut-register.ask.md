You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-16 (the lyrics he pasted are in lyrics.txt): "use this, now reserch the internet and clean room it, on how to parody ten crack comandments beat and style and how to get biggies voice for suno. THansk"

## What happened in earlier rounds (facts)

- A BadCode short (9:16, phones), about 30 seconds. A parody of a famous 1997 New York rap song in which the rapper counts down ten street-hustle rules over a sparse, hard boom-bap beat, with a voice sample counting the numbers between rules. Here the rules are about who controls the money printer.
- Jack asked for the track to sound like that song's beat and style and the rapper's voice (the late Brooklyn rapper of the 1990s). Suno refuses real artist names: describe the sound, never name an artist, song or producer.
- 🔴 Parody of style, not a copy: no reproduction of the original beat, its samples or its melody. The era and genre feel are fine.
- Vocals ARE wanted on this one (Jack asked for the rap). The lyrics must be sung exactly as written in lyrics.txt.
- Duration set to 30 s on Suno v6.

## Never write these

Notorious
Biggie
B.I.G.
Ten Crack Commandments
DJ Premier

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "v6",
  "durationSec": 30
}
```

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
Uh. Uh-huh.
Money printer manual. Page one. Take notes.

Number one: never tell 'em what you printed,
trillions out the back door, keep the ledger tinted.

Number four: never get high on your own supply,
banks took the first hit, now the rent's sky-high.

Number six: no credit? Nah, they live on the slate,
and you're paying it back in the price on your plate.

Number seven: keep the family out the business,
Treasury and the bank in one bed, God as my witness.

Number ten: no consignment, cash up front, that's law,
they took the bailout on tick and they ain't paid at all.

And the fix, from the future? Easy.
No hand on the printer.
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**hungry-young-debut-register** — A young, hungry nineteen-year-old rapper in a higher, slightly nasal register, voice still raw at the edges, eager and fast, pushing the beat and running out of breath at line ends. Ask for the music with technical gear words: 12-bit sampler crunch, swung MPC drums at 92 BPM, filtered bassline, chopped dusty piano stab, vinyl crackle, mono-ish early-90s mix. Raw demo-tape energy rather than polished album sound.

Other writers are doing the other experiments (heavy-baritone-ledger-drawl, old-gravel-mob-accountant, queens-woman-hard-snare, radio-countdown-promo, noir-strings-spoken-sermon). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r1-rap/writers/hungry-young-debut-register.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r1-rap/writers/hungry-young-debut-register.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "hungry-young-debut-register". Reply with just the two paths.