You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Kai, 2026-11-10: "I think that I also want there to be music in this short."
Kai, 2026-11-10: "I think a new Suno track just for this short is what I want because it's not about the bank robbery this, it's about rules breaking. And I think we can, it'd be interesting just to sort of discuss with you about music styles."
Kai, 2026-11-10: "I really like the idea of a school assembly hymn. This sounds really, really like a really good style. I think song words is a great idea... For the five, I think it's number two. Let's just lean into number two."
Kai, 2026-11-10: "we don't have long, right? I think we have maybe 20 seconds maximum. So, we don't need a huge amount of lyrics... And yeah, by song, I think I mean, like, short period of music."
Kai, 2026-11-10: "Hey Claude, yeah, please proceed with what you think is next. Let's go and have a look at a Suno example, it would be good."

## What happened in earlier rounds (facts)

- The short is 20 seconds maximum, portrait. The four lines are the whole song; the organ stops after the last line (silence for the window and the tear in the picture).
- Kai picked "school assembly hymn" (option 2 of five) from: hold music breaking into punk; school assembly hymn (children's choir and organ); marching snare; deadpan MC; rubber-stamp rhythm. The crowd/terrace turn that option 2 first had was dropped by Kai: no crowd.
- No Suno take has been made for this short yet.

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

**one-small-girl-nervous** — A single untrained girl of about seven, picked to sing in front of the assembly, sings the four lines alone: small, breathy, close to the microphone, a little hesitant, slightly off pitch on the high notes, but carrying the tune bravely. Under her a church chamber organ plays the hymn very quietly on one soft stop, simple four-part chords that follow her rather than lead, slowing when she slows. Ask for it as an intimate, dry, almost documentary recording, a child's solo at a school service, and exclude choir, polished vocals, reverb-heavy production, drums and strings. The organ lifts off after her last word and there is nothing after it.

Other writers are doing the other experiments (whole-school-upright-piano, solo-cathedral-treble, edwardian-sunday-school-78). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/hymn-r1/writers/one-small-girl-nervous.notes.md`,
and write ONLY a single JSON object to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/hymn-r1/writers/one-small-girl-nervous.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "one-small-girl-nervous". Reply with just the two paths.