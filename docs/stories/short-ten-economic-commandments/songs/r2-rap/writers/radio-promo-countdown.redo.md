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

**radio-promo-countdown** — Lean on the beat's origin as a radio countdown promo: a 1996 New York hip-hop radio drop turned into a song, the turntable cutting a booming hype-man voice that counts one, two, three, four, five, each number scratched in on the downbeat. The rapper: deep, raspy, heavyset Brooklyn voice, menacing but relaxed, like he's explaining the rules to a younger dealer across a table, a slight smile in it. Beat: stripped boom bap, hard snare, single dark piano stab, 90 BPM, short intro 'Uh. Uh-huh.' ad-lib dry and close. Raise weirdness a little to let the scratch section breathe.

Other writers are doing the other experiments (chest-voice-literal, drums-first-dj-cuts, jazz-phrasing, mafioso-menace, exclude-the-wrong-voice). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Style boxes (shared by most of the round): behind the beat
- shares wording with other prompts in this round: Style boxes (shared by most of the round): coast boom bap
- shares wording with other prompts in this round: Style boxes (shared by most of the round): east coast boom
- shares wording with other prompts in this round: lyric [directions] (shared by most of the round): beat drops out

Your previous draft:
```json
{
  "name": "radio-promo-countdown",
  "style": "1996 New York FM hip-hop radio countdown jingle grown into a full rap track, 90 BPM east coast boom bap, stripped and dry. Turntable cuts scratch a booming hype-man voice shouting each number on the downbeat, chopped short, crackle on the edges. Raw dusty kick, hard cracking snare, closed hats barely there, one dark low piano stab per bar, deep sub bass under it, lots of empty space. Male rapper: deep heavy chest voice, husky rasp, big-framed Brooklyn drawl, unhurried and menacing with a smile in it, conversational like schooling a younger hustler across a kitchen table, lands slightly behind the beat, clear diction, mic close and dry, no reverb, no harmonies, no hook singing",
  "exclude": "trap hi-hats, 808 rolls, autotune, sung chorus, melodic rap, female vocals, choir, strings, reverb wash, EDM, lo-fi chill, jazz saxophone, high-pitched voice, fast double-time, modern pop sheen",
  "lyrics": "[Intro: dry close ad-lib, record crackle]\nUh. Money printer manual. Take notes.\n\n[Turntable scratch: hype-man voice cuts in the number one]\n[Verse: deep, relaxed, behind the beat]\nNumber one: never tell 'em what you printed,\ntrillions out the back door, keep the ledger tinted.\n\n[Turntable scratch: hype-man voice cuts in the number two]\nNumber two: never get high on your own supply,\nbanks took the first hit, now the rent's sky-high.\n\n[Turntable scratch: hype-man voice cuts in the number three]\nNumber three: no consignment, cash up front, that's law,\nthey took the bailout on tick and they ain't paid at all.\n\n[Beat drops out, spoken, slight smile]\nAnd the fix, from the future? No hand on the printer.\n\n[End: one last scratch, cut to silence]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 58,
  "styleInfluence": 72,
  "vocalGender": "male",
  "durationSec": 20,
  "maxMode": false
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r2-rap/writers/radio-promo-countdown.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r2-rap/writers/radio-promo-countdown.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "radio-promo-countdown". Reply with just the two paths.