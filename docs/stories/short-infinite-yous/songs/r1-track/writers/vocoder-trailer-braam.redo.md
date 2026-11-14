You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

done then do the suno sounds and music in one thanks

## What happened in earlier rounds (facts)

- The track is the whole audio of a 15-second vertical short (BadCode Shorts, "Infinite Yous"). The picture will be cut to this track afterwards. Jack wants the spoken lines, the sound effects and the music made together in ONE Suno track.
- What we see, in order (Jack's idea, his words: "it starts with that line, and it shows multiple versions of him on the same screen, they all split off, then the badcode balaclava guy in a science lab coat grabs all of the lines separating the different versions, squeezes them into one the original version, says there is only one and kicks him into a cab, it cuts to the badcode logo and name screen, when taxi headlights illuminate it and car beeping happens, but not overly annoying just in a cinematic way."):
  - 0–3 s: a drunk lad after a night out in a city at night, car keys in his hand: "There's infinite versions of me. One of them gets home fine."
  - 3–6 s: many versions of him on one screen, splitting apart into separate strips.
  - 6–10 s: a figure in a balaclava and a white lab coat grabs the lines between the strips and squeezes them back into one lad: "There's only one."
  - 10–13 s: he boots the lad into a waiting taxi.
  - 13–15 s: the logo on a wall, lit by passing taxi headlights, with a car horn "not overly annoying, just in a cinematic way".
- Who says which line:
  - The lad (drunk, young, British): "There's infinite versions of me. One of them gets home fine."
  - The masked figure (calm, certain): "There's only one."
- The point: the drink-drive message. There is one of you, and one mum waiting up. The short is against drink-driving.
- Kai, 2026-11-13 meeting, on the shorts' audio: "these shorts have a rhythm to them that misses the music … I don't mean a tune … sounds that massively increase the richness of the message … Give me this guy screaming this, followed by a quick jab on a violin, followed by a meek little child with a little pattern of foreboding music behind it, smashed it. That's what the shorts should be." Also: "suno has a speech mode as well now."
- Kai on this short, 2026-11-13: "That's brilliant, like, no changes. Just do that."
- Length: Suno v6 obeys a set Duration to about a second; Auto runs long. The target is 15 s.

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "v6",
  "durationSec": 15
}
```

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
There's infinite versions of me. One of them gets home fine.
There's only one.
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**vocoder-trailer-braam** — Hybrid movie-trailer sound design: rising Shepard-tone riser, ticking clock, heavy braam brass hits. The lad is a fast, breathless, nervous-giggly teenager rattling off his line. The masked figure is the superintelligence itself: a pitched-down, vocoded, slightly robotic voice that sounds enormous and certain, landing 'There's only one.' on a huge low impact with everything else sucked out. The final two seconds are a trailer title-card hit layered with a car horn and headlights-swoosh whoosh, cinematic not annoying.

Other writers are doing the other experiments (violin-jab-music-box, garage-pulse-cut-dead, lab-theremin-documentary, terrace-chant-collapse, choir-of-yous-to-one). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Style boxes: spoken word not
- shares wording with other prompts in this round: Style boxes: voice forward mix

Your previous draft:
```json
{
  "name": "vocoder-trailer-braam",
  "style": "hybrid movie trailer sound design, spoken word not sung, two voices, endless Shepard-tone riser climbing, dry ticking clock that speeds up, heavy low brass braam hits, sub-bass drop, vocoded pitched-down machine voice, voice-forward mix, hard cut to silence before the last line, trailer title-card slam, distant city car horn, headlight swoosh whoosh",
  "exclude": "singing, sung chorus, melody, refrain, rap, rhyme, autotune on the lad, guitar, piano ballad, EDM drop, four-on-the-floor, laughter track, comedy",
  "lyrics": "[Intro: Shepard-tone riser starts, fast clock ticks]\n[Spoken: young British lad, drunk, breathless, nervous giggle, rattling it off fast]\nThere's infinite versions of me. One of them gets home fine.\n[Riser peaks, ticking races, braam hit, then dead silence]\n[Spoken: vocoded machine voice, pitched down an octave, slow, enormous, certain]\nThere's only one.\n[Huge low impact, everything else gone]\n[Outro: trailer title-card hit, car horn, headlights whoosh past, ring out]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 55,
  "styleInfluence": 75,
  "vocalGender": "male",
  "durationSec": 15,
  "maxMode": false
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-infinite-yous/songs/r1-track/writers/vocoder-trailer-braam.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-infinite-yous/songs/r1-track/writers/vocoder-trailer-braam.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "vocoder-trailer-braam". Reply with just the two paths.