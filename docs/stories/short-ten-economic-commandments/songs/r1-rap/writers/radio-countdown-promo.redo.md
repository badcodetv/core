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

**radio-countdown-promo** — Built as a late-night New York radio countdown bit, nodding to the beat's own origin as a radio promo: a smooth, mellow, almost whispered deep male MC raps the rules, while a separate brash radio-DJ voice shouts each 'Number one / four / six / seven / ten' like a chart countdown. Ask for the music as a station segment: a looping dark keys riff, crisp boom-bap drums, a short rising sci-fi countdown blip before each number, radio compression on the DJ voice only. Two clearly different voices, the MC never sings.

Other writers are doing the other experiments (heavy-baritone-ledger-drawl, old-gravel-mob-accountant, queens-woman-hard-snare, hungry-young-debut-register, noir-strings-spoken-sermon). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: lyric [directions]: shouts the number

Your previous draft:
```json
{
  "name": "radio-countdown-promo",
  "style": "Late-night 1997 New York FM radio countdown segment, rapped. Two separate voices, never blended. Voice A, the MC: deep male rapper, smooth and unhurried, mellow, close-mic near-whisper, conversational menace, lazy-perfect timing behind the beat, rapped never sung. Voice B, the radio DJ: brash hype host who only barks the chart numbers, loud and excited, squashed AM-radio compression and slapback on his voice alone. Music: around 90 BPM boom-bap, crisp dusty snare and thick kick, a looping minor jazz electric-piano riff, dark and sparse, low upright-style bass, vinyl hiss. Before every number a short rising sci-fi synth countdown blip, then a hard drum drop back in. Station ident feel, segment ends on a tape-stop.",
  "exclude": "singing, sung chorus, melodic hook, autotune, trap hi-hats, 808 glide, choir, female vocals, pop, EDM, rock guitar, record scratches",
  "lyrics": "[Intro: late-night radio station ident, dark keys loop, MC low and close to the mic]\n[MC, whispered]\nUh. Uh-huh.\nMoney printer manual. Page one. Take notes.\n\n[Countdown blip] [Radio DJ shouts the number, MC raps the rest]\nNumber one: never tell 'em what you printed,\ntrillions out the back door, keep the ledger tinted.\n\n[Countdown blip] [Radio DJ shouts the number, MC raps the rest]\nNumber four: never get high on your own supply,\nbanks took the first hit, now the rent's sky-high.\n\n[Countdown blip] [Radio DJ shouts the number, MC raps the rest]\nNumber six: no credit? Nah, they live on the slate,\nand you're paying it back in the price on your plate.\n\n[Countdown blip] [Radio DJ shouts the number, MC raps the rest]\nNumber seven: keep the family out the business,\nTreasury and the bank in one bed, God as my witness.\n\n[Countdown blip] [Radio DJ shouts the number, MC raps the rest]\nNumber ten: no consignment, cash up front, that's law,\nthey took the bailout on tick and they ain't paid at all.\n\n[Outro: beat drops to keys only, MC spoken, almost whispered]\nAnd the fix, from the future? Easy.\nNo hand on the printer.\n[Station sign-off sting, cut]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 35,
  "styleInfluence": 70,
  "vocalGender": "male",
  "durationSec": 30,
  "maxMode": true
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r1-rap/writers/radio-countdown-promo.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r1-rap/writers/radio-countdown-promo.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "radio-countdown-promo". Reply with just the two paths.