You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-16, on round 1 (12 takes): "none of them sound like biggie or the ten crack commandments, please make it as close as possible. also it goes from like 1 to 4 to 7 or something, make it in order as in 1 2 3 4 or however many there are and change the lyrics accordingly. Please clean room it all and research the internet to achieve it. Thanks."
Jack, 2026-11-16, straight after: "also we need to make it shorter, those song were like 47 secs, how many secs can all platforms allow short wise thanks"

## What happened in earlier rounds (facts)

- A BadCode short (9:16, phones), about 30 seconds: a parody of a famous 1997 New York rap song in which the late Brooklyn rapper counts down street-hustle rules ("commandments") over a sparse, hard, dark boom-bap beat, with a voice sample counting the numbers between the rules. Here the rules are about who controls the money printer.
- Round 1 (6 directions x2, v6, 30 s) ran six DIFFERENT voices on purpose (heavy baritone, old gravel, a Queens woman, a hungry young voice, a radio countdown, noir strings with a spoken delivery). Jack's verdict, verbatim: "none of them sound like biggie or the ten crack commandments, please make it as close as possible."
- So this round has ONE target: as close as possible to that rapper's voice and delivery and that song's beat and feel. The six writers differ in HOW they get there (which features they name, tempo, production words, weirdness), not in where they are going. Research the original song's production (tempo, drums, the counting sample, the loop, the mix) and the rapper's voice and flow in detail.
- Suno refuses real artist, song and producer names: describe the sound in plain features only.
- 🔴 Parody of style, not a copy: no reproduction of the original beat's samples, loop or melody (a copyright claim would block the short). Match the era, tempo, drum sound, mood and the delivery as closely as the description allows.
- Vocals ARE wanted (Jack asked for the rap). The lyrics are sung exactly as written in lyrics.txt, numbered one to three in order.
- Duration 20 s on Suno v6 (Jack, 2026-11-16: "we need to make it shorter, those song were like 47 secs"). Round 1 takes ran 30-47 s against a 30 s setting: keep it tight.

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
  "durationSec": 20
}
```

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
Uh. Money printer manual. Take notes.

Number one: never tell 'em what you printed,
trillions out the back door, keep the ledger tinted.

Number two: never get high on your own supply,
banks took the first hit, now the rent's sky-high.

Number three: no consignment, cash up front, that's law,
they took the bailout on tick and they ain't paid at all.

And the fix, from the future? No hand on the printer.
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**exclude-the-wrong-voice** — Get there by subtraction as much as addition, because round 1 drifted: a short positive box (deep heavyset Brooklyn male rapper, plummy wheezy chest voice, laid-back conversational flow, 1997 New York boom bap, 90 BPM, dark jazz keys loop, hard drums, scratched number count) and a long, specific exclude list built from what round 1 produced: gravel old man, female vocals, youthful high voice, radio announcer, strings, spoken word, trap hi-hats, lo-fi chill, autotune. Use bracket tags in the lyrics only for [Intro], [Scratch: count], [Verse] and [Outro]. Low weirdness, high style influence.

Other writers are doing the other experiments (chest-voice-literal, drums-first-dj-cuts, jazz-phrasing, radio-promo-countdown, mafioso-menace). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Style boxes: in a shouted

Your previous draft:
```json
{
  "name": "exclude-the-wrong-voice",
  "style": "1997 New York City hip hop, dusty sampled boom-bap, 90 BPM, no hook. Short minor-key electric piano phrase looping cold and sparse, thick swung kick, cracking snare, a DJ scratching in a shouted number before each rule. Big portly Brooklyn male MC, deep chest-heavy baritone with a breathy wheeze, plush rounded tone, relaxed talky cadence that drags a hair late on the snare then catches up, cool menace, dry close-miked vocal",
  "exclude": "gravelly old man voice, female vocals, high youthful voice, radio announcer, orchestral strings, spoken word poetry, trap hi-hats, 808 rolls, lo-fi chill, autotune, sung chorus, backing vocals, big reverb",
  "lyrics": "[Intro]\nUh. Money printer manual. Take notes.\n\n[Scratch: count]\n[Verse]\nNumber one: never tell 'em what you printed,\ntrillions out the back door, keep the ledger tinted.\n\n[Scratch: count]\n[Verse]\nNumber two: never get high on your own supply,\nbanks took the first hit, now the rent's sky-high.\n\n[Scratch: count]\n[Verse]\nNumber three: no consignment, cash up front, that's law,\nthey took the bailout on tick and they ain't paid at all.\n\n[Outro]\nAnd the fix, from the future? No hand on the printer.",
  "model": "v6",
  "variety": "off",
  "weirdness": 10,
  "styleInfluence": 85,
  "vocalGender": "male",
  "durationSec": 20,
  "maxMode": false
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r2-rap/writers/exclude-the-wrong-voice.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r2-rap/writers/exclude-the-wrong-voice.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "exclude-the-wrong-voice". Reply with just the two paths.