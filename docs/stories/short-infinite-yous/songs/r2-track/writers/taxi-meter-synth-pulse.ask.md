You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

done then do the suno sounds and music in one thanks

(after round r1-track, which had the spoken lines in it:)
there should be no lyrics in these suno tracks please try again thanks

## What happened in earlier rounds (facts)

- The track is the audio bed of a 15-second vertical short (BadCode Shorts, "Infinite Yous"): the sound effects and the music together in ONE Suno track (Jack: "do the suno sounds and music in one"). No lyrics, no voice, no words (Jack, after the first round: "there should be no lyrics in these suno tracks"). The picture will be cut to this track afterwards.
- What we see, in order (Jack's idea, his words: "it starts with that line, and it shows multiple versions of him on the same screen, they all split off, then the badcode balaclava guy in a science lab coat grabs all of the lines separating the different versions, squeezes them into one the original version, says there is only one and kicks him into a cab, it cuts to the badcode logo and name screen, when taxi headlights illuminate it and car beeping happens, but not overly annoying just in a cinematic way."):
  - 0–3 s: a drunk lad after a night out in a city at night, car keys in his hand.
  - 3–6 s: many versions of him on one screen, splitting apart into separate strips.
  - 6–10 s: a figure in a balaclava and a white lab coat grabs the lines between the strips and squeezes them back into one lad.
  - 10–13 s: he boots the lad into a waiting taxi.
  - 13–15 s: the logo on a wall, lit by passing taxi headlights, with a car horn "not overly annoying, just in a cinematic way".
- The point: the drink-drive message. There is one of you, and one mum waiting up. The short is against drink-driving.
- Kai, 2026-11-13 meeting, on the shorts' audio: "these shorts have a rhythm to them that misses the music … I don't mean a tune … sounds that massively increase the richness of the message … followed by a quick jab on a violin, followed by a meek little child with a little pattern of foreboding music behind it, smashed it. That's what the shorts should be."
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

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**taxi-meter-synth-pulse** — A retro-futurist synth cue from the narrator's own future: a ticking analogue sequencer pulse like a taxi meter or indicator click, a glassy arpeggio that fractures into many detuned copies (one per version of him) and then is quantised back into a single clean arpeggio with a bitcrush-snap, a gated-reverb tom hit for the kick into the cab, and an ending on a warm analogue pad chord with a low cinematic horn swell and headlight swoosh. The performer is a modular/analogue synth player, 1980s sci-fi score in feel but cold and precise. Ask for it with BPM (about 120, dropping out at 13 s) and synth names rather than a genre tag. Exclude vocals, vocoder, talkbox, guitar, orchestra.

Other writers are doing the other experiments (solo-violin-jab-music-box, club-thump-through-the-wall, pizzicato-caper-to-solemn-brass, sound-design-only-foley-score, lullaby-piano-to-silence). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-infinite-yous/songs/r2-track/writers/taxi-meter-synth-pulse.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-infinite-yous/songs/r2-track/writers/taxi-meter-synth-pulse.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "taxi-meter-synth-pulse". Reply with just the two paths.