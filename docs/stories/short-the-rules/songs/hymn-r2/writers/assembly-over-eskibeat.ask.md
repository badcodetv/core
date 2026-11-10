You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Kai, 2026-11-10 (before hearing round 1): "I'm just thinking that it feels like a combination of school hymn plus grimy, dystopian, I think we could find something quite cool, but let me hear what we've got first before we start to iterate on the sound."
Kai, 2026-11-10 (after hearing the round 1 whole-school take): "So it feels like possibly can we combine this with like a grind beat so it's like the comparison is odd so it's like yeah I quite I think the piano is slightly jarring but I like the school children singing it in a kind of blase hilarious way."

## What happened in earlier rounds (facts)

- Round 1 (hymn-r1) ran four ideas: a whole primary school singing with an upright piano; a solo cathedral boy treble with organ; one nervous seven-year-old girl alone with a small organ; an Edwardian Sunday-school class on a 1910 gramophone record with harmonium.
- Kai heard the whole-school take: he likes the school children singing it "in a kind of blase hilarious way"; the piano is "slightly jarring".
- Kai's "grind beat" is read as GRIME (UK grime/drill-adjacent beat, matching his earlier "grimy, dystopian"); not confirmed by him.
- The short is 20 seconds maximum, portrait; the four lines are the whole song; after the last line the picture goes silent for the window and the tear.

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
We can't afford a bed for you,
The purse is far too thin;
There is room on all those islands,
But you will sleep in a bin.
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**assembly-over-eskibeat** — Keep exactly what Kai liked: a whole primary-school assembly of around 200 children, aged 7 to 11, singing the hymn in flat, bored, London-accented unison, dutiful and blasé in the way of Another Brick in the Wall's school choir, recorded in an echoey school hall. Swap the piano out entirely for an early-2000s eskibeat grime instrumental at 140 BPM: a raw square-wave bass in short stabs, dry eski clicks on the off-beats, a sparse clap on 2 and 4, and one icy repeating synth stab, with lots of empty space. The children stay in strict hymn time, unaware of the beat, so the mismatch is the joke. The beat cuts dead after the last line ('sleep in a bin'), so nothing rings on. Exclude piano, organ, adult vocals, rap and pads.

Other writers are doing the other experiments (playground-clapping-drill, chopped-choir-sample-riddim, one-bored-kid-in-the-dark). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/hymn-r2/writers/assembly-over-eskibeat.notes.md`,
and write ONLY a single JSON object to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/hymn-r2/writers/assembly-over-eskibeat.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "assembly-over-eskibeat". Reply with just the two paths.