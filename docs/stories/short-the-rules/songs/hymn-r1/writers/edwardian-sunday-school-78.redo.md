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

**edwardian-sunday-school-78** — A Sunday-school children's choir recorded around 1910 on a shellac 78 record: twenty children singing in unison with crisp Edwardian diction, accompanied by a wheezing pedal harmonium pumped a little unevenly. Ask for the music through its period and its recording: acoustic-era horn recording, narrow mid-range, surface crackle and hiss, slight speed wobble, no bass, no modern production. A brisk, upright Victorian hymn tune in common metre (about 92 bpm), sung with cheerful moral certainty as if it were a lesson in good conduct. Three harmonium chords as an introduction, the four lines once, a final amen-style cadence on the last word, then only the crackle of the run-out groove.

Other writers are doing the other experiments (whole-school-upright-piano, solo-cathedral-treble, one-small-girl-nervous). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: lyric [directions] (shared by most of the round): the last word

Your previous draft:
```json
{
  "name": "edwardian-sunday-school-78",
  "style": "1910 acoustic-horn gramophone record, shellac 78 rpm, mono. Edwardian Sunday-school children's choir, about twenty boys and girls singing in strict unison, clipped precise Edwardian English diction, bright and dutiful. Pedal harmonium, reedy and breathy, pumped slightly unevenly so the chords swell and sag. Brisk upright Victorian hymn tune, common metre, major key, 92 bpm, sung with cheerful moral certainty like a lesson in good manners. Boxy mid-range only, roughly 250 Hz to 2.5 kHz, no low end, small reflective room, surface crackle and hiss, gentle speed wobble.",
  "exclude": "drums, percussion, bass, sub bass, modern production, stereo, reverb wash, synth, pipe organ, piano, strings, adult vocals, solo singer, crowd, cheering, autotune, pop",
  "lyrics": "[Intro: three slow harmonium chords, record crackle]\n\n[Verse: children's choir in unison, brisk and upright]\nWe can't afford a bed for you,\nThe purse is far too thin;\nThere is room on all those islands,\nBut you will sleep in a bin.\n\n[Amen cadence on the last word, harmonium holds then stops]\n\n[Outro: silence, only the crackle of the run-out groove]\n\n[End]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 35,
  "styleInfluence": 75,
  "vocalGender": null,
  "durationSec": 20,
  "maxMode": false
}
```

Write a short note on what shaped it (with source URLs) to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/hymn-r1/writers/edwardian-sunday-school-78.notes.md`,
and write ONLY a single JSON object to `/home/kai/projects/badcode/badcode/docs/stories/short-the-rules/songs/hymn-r1/writers/edwardian-sunday-school-78.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "edwardian-sunday-school-78". Reply with just the two paths.