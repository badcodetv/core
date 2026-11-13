You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-13: "lets do suno for it all, but add background music as well that fits the scene thanks"

Jack, 2026-11-13: "i think build the track first then, animate it to the song if that makes sense, then put it on the timeline thanks"

## What happened in earlier rounds (facts)

- The track is the audio of a 14-second vertical short (BadCode Shorts, "Priority Lane"). The picture will be cut to this track afterwards.
- What we see, in order:
  - 0–5 s: inside a speeding ambulance at night in the rain, two masked paramedics fighting to save an old man, the driver shouting at the traffic.
  - 5–7 s: a red light, and a police motorcycle outrider holds up his glove. The ambulance stops.
  - 7–11 s: a politician's black car crosses slowly in front of it. He is on the phone, furious about canapés.
  - 11–14 s: back inside, the heart monitor flatlines. Silence. Black. Logo.
- Who says which line:
  - Paramedic 1 (a woman): "Sixty over thirty! Fucking hurry up, we're gonna lose him!"
  - Paramedic 2 (a man): "Sats dropping, he's peri-arrest!"
  - The driver: "Two minutes out! Get the fuck out of the way!"
  - Paramedic 2, at the red light: "Why have we stopped?!"
  - The minister, posh, muffled through the glass: "I said raspberry-shaped hors d'oeuvres!"
  - Paramedic 1, quiet: "Fifty over twen—", cut off by the flatline tone.
- Kai, 2026-11-13 meeting, on the shorts' audio: "these shorts have a rhythm to them that misses the music … I don't mean a tune … sounds that massively increase the richness of the message … Give me this guy screaming this, followed by a quick jab on a violin, followed by a meek little child with a little pattern of foreboding music behind it, smashed it. That's what the shorts should be." Also: "suno has a speech mode as well now."
- Kai on the ambulance: "I want casualty ER-level drama inside that ambulance … I want to feel that that guy's on death's door, and these heroes are trying desperately."
- Length: Suno v6 obeys a set Duration to about a second; Auto runs long. The target is about 14 s.

## This story's standing rules (the round is finding a new style, so only these bind)

## Rules for this story

- **Round 3 (2026-11-13): Suno makes all of the audio:** the crew's shouts in speech mode, the siren, the monitor and the flatline tone, and background music that fits the scene (Jack). The minister's line can be Suno's or Orus.
- **The whole track is about 14 s:** a dying man in an ambulance (0–5 s), held at a red light (5–7 s), the minister's car crossing (7–11 s), then the flatline, silence, and the logo on black (11–14 s). The picture is cut to the track.
- Swearing is said in full, never bleeped. If Suno refuses a word, swap the word.
- No speech in any Flow clip.

## Never

- A cheerful or comedic score: it must feel like real hospital-drama urgency.
- Music over the flatline: it ends in the tone and then silence.

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
Sixty over thirty! Fucking hurry up, we're gonna lose him!
Sats dropping, he's peri-arrest!
Two minutes out! Get the fuck out of the way!
Why have we stopped?!
I said raspberry-shaped hors d'oeuvres!
Fifty over twen—
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**analog-synth-chase** — An 1980s analog-synth thriller score: a racing sixteenth-note bass arpeggio, gated snare, dark pads, the siren played as a detuned synth wail. The crew are a young, rough, smoke-voiced woman screaming, a man who speaks low, fast and controlled until he breaks, and a driver with a strained, cracking, high shout. At the red light the arpeggio freezes on one held, filtered note that slowly closes; the minister is heard through a tinny car-phone filter, haughty and whiny. The flatline is a single pure synth sine, with no music under it, then black silence.

Other writers are doing the other experiments (casualty-string-pulse, fly-on-the-wall-cab, stab-and-silence, heartbeat-drums, child-and-choir). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Style boxes: on a single

Your previous draft:
```json
{
  "name": "analog-synth-chase",
  "style": "Mid-80s electronic action-thriller underscore, pre-MIDI hardware rig, voices talked and yelled over the cue, never sung. Fast 16th-note monosynth bassline pulsing at 150 BPM, slightly loose against the clock; booming gated snare with a short reverb tail on the backbeat; cold minor polysynth chords swelling beneath; a siren imitated by a detuned oscillator whooping up and down. British crew in the back of an ambulance: a hoarse, smoker-rasped girl in her twenties howling her numbers; a man reporting fast, flat and controlled until his voice splits; a driver straining and cracking up high. At the stop one struck cast-iron clank, then the pulse hangs on a single bass tone while a low-pass filter shuts it down to a murmur, percussion out. An upper-class man complains down a crackly, band-limited carphone, whining and entitled. Finale: one unwavering pure sine beep with nothing beneath it, then total quiet. Close-miked, frantic, rain on the roof.",
  "exclude": "singing, sung melody, chorus, rap, choir, upbeat, happy, funk, comedy, synthwave vocals, autotune, guitar solo, fade-out, music under the tone",
  "lyrics": "[Intro: monosynth 16ths racing, gated snare, oscillator siren]\n\n[Female, hoarse howl]\nSixty over thirty! Fucking hurry up, we're gonna lose him!\n\n[Male, quick flat report]\nSats dropping, he's peri-arrest!\n\n[Male driver, high strained yell]\nTwo minutes out! Get the fuck out of the way!\n\n[Break: metal clank, pulse hangs on one bass tone, filter shutting, no drums]\n\n[Male, voice splitting]\nWhy have we stopped?!\n\n[Posh man, crackly carphone]\nI said raspberry-shaped hors d'oeuvres!\n\n[Female, barely audible]\nFifty over twen—\n\n[Outro: lone sine beep, nothing else]\n\n[Silence]\n\n[End]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 45,
  "styleInfluence": 70,
  "vocalGender": null,
  "durationSec": 14,
  "maxMode": true
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/shorts/priority-lane/songs/r3-suno/writers/analog-synth-chase.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/shorts/priority-lane/songs/r3-suno/writers/analog-synth-chase.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "analog-synth-chase". Reply with just the two paths.