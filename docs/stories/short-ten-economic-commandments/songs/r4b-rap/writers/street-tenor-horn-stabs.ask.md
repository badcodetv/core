You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-19, on the 29 s cut with jazz1 (three rules): "Rap all ten please and "Fix the rhythm" means sometimes he says the line too fast, and could sound a bit more like the actauly ten crack commandments song, but just use what we have as a template/inspiration."
Jack, 2026-11-19, on the lyric: "do "Uno", keep the rest please make the song thanks"
Jack, 2026-11-19: "Make sure there's no pollution, you don't have to copy the CNO thing mostly, just make it simple. Or do both actually, do the recommended new writers, same lyrics, all that stuff. And then do like an inspiration version. Thanks."
This round: the "inspiration version". A fresh, simple take inspired by the feel of a late-1990s New York boom-bap countdown record, unhurried. Not a copy of any record.

## What happened in earlier rounds (facts)

- Round 2 (2026-11-16): Jack picked jazz1 (Suno e4cb9be5), v6, Duration 20 s, came back 29.0 s; three rules numbered 1-3 plus the fix. Its Style box is keep.txt.
- 2026-11-17 meeting (Jack and Kai): the song says ten but shows fewer; "fix the rhythm; ten points if the length allows".
- 2026-11-19, Jack: rap all ten; "sometimes he says the line too fast"; "could sound a bit more like" the original song; use what we have as the template.
- The new lyric is ten rules plus a short intro and the fix: about 75 s at an unhurried pace. Each "Number ..." should land on its own beat with room before the line.
- Round 3 (2026-11-19) stopped at the gate after two rewrites: one Style box over 1,000 characters, a shared phrase, identical settings in every prompt. Nothing ran.

## This story's standing rules (the round is finding a new style, so only these bind)

## Story-only rules
- Never write "trousers a little too short" (or anything that bares ankles, wrists or neck) for the figure.
- When fixing masks, attach the still only: with the navy mask reference attached the masks turned navy.
- No real rapper or real currency in any still. Blur the fast-food logo on RU2-a-a if it is ever used.
- Check every clip at three frames for suit, cap, mask and no skin; a clip that turns side-on late is used from its start.
- The logo is a card at the tail, laid in by the edit. `marketing-gatekeeper` before posting.

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
  "durationSec": 75,
  "vocalGender": "male"
}
```

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
Uh. Money printer manual. Take notes.

Rule number Uno: never say how much you made,
doesn't matter anyway, since the gold went away.

Number two: never show 'em your next move,
cut the rate for the banks, hike it when you land.

Number three: never trust nobody with the press,
before Bernie gets made off face loss.

Number four: never get high on your own supply,
banks took the first hit, now the rent's sky-high.

Number five: never print where you sleep,
never let them owe the oats you reap.

Number six: no credit? Forget it,
let the junkie know you better forget that.

Seven, and nobody says it out loud:
keep your money and your assets apart, not in one crowd.

Number eight: hold none of it yourself,
debase 'em till the numbers go through.

Nine's the one they'd rather you skipped:
keep the auditors out, sporadic trips and you out.

Number ten: no consignment, cash up front, that's law,
they took the bailout in stride and they ain't paid it all.

And the fix, from the future? No hand on the printer.
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**street-tenor-horn-stabs** — A higher, nasal, slightly raspy young male tenor with a confident street-corner bark, punchy and rhythmic but never rushed: he states each number on its own, takes a breath, then delivers the line. Ask for the music as a scene and mood rather than an instrument list: a cold late-night New York block in 1997, tense and sly, built on a short brooding horn-and-strings sample that stabs once on every number, a heavy kick, and a cracking snare at around 90 BPM. Between rules, ask for a short instrumental turntable cut or record-scratch fill (no words) so the countdown feels like it is being counted off by the DJ. Use lyric directions like [punchy, deliberate, one bar per line] and keep the closing fix line alone over a stripped drop to just the drums.

Other writers are doing the other experiments (baritone-behind-the-beat, weathered-ledger-reader). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r4b-rap/writers/street-tenor-horn-stabs.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r4b-rap/writers/street-tenor-horn-stabs.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "street-tenor-horn-stabs". Reply with just the two paths.