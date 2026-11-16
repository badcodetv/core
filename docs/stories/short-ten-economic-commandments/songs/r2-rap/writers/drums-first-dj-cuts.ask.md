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

**drums-first-dj-cuts** — Lead with the producer side: the prompt is mostly about the beat, chopped boom-bap drums sliced and re-layered, drums 'harder than nails', a minimal two-bar loop of dark Rhodes chords, deep sub bassline under it, and a DJ scratching the numbers one to five on the turntable between verses like a radio countdown. Tempo 92 BPM, mono-ish 90s mix, MPC grit. The rapper is described in fewer, punchy words: obese-sounding deep male Brooklyn rapper, slow, cool, conversational. Put a [Scratched count: one] style direction in brackets before each rule (and note the risk Suno sings it). Medium weirdness.

Other writers are doing the other experiments (chest-voice-literal, jazz-phrasing, radio-promo-countdown, mafioso-menace, exclude-the-wrong-voice). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r2-rap/writers/drums-first-dj-cuts.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r2-rap/writers/drums-first-dj-cuts.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "drums-first-dj-cuts". Reply with just the two paths.