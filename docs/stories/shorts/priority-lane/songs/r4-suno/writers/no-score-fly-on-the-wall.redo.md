You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-13, on round r3: "so the songs are american they should be english, do a few different cinematic dramtic styles, also there is no difference in voices between the ambulance lot and the politician. THanks Please clean room it all and research the internet to achieve it. Thanks."

Earlier, Jack, 2026-11-13: "lets do suno for it all, but add background music as well that fits the scene thanks"

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

## What happened last round (r3, 2026-11-13), facts only
- Five directions were made: TV hospital-drama strings, fly-on-the-wall documentary, stabs and silence, an 80s synth chase, and a child with a choir.
- Jack heard them and said:
  - every voice sounded **American**; they must be **English** (British, UK accents)
  - **the ambulance crew and the politician sounded the same**; they must be clearly different people
  - he wants **a few different cinematic, dramatic styles**
- Suno ignored the 15 s duration: the takes ran from 0:15 to 1:55. The editor will trim, but a short form helps.
- The cast, as it should sound:
  - **paramedics and driver:** ordinary working British NHS crew, regional English voices
  - **the minister:** a posh, plummy, upper-class English man in a car, entitled and petulant, muffled through glass

## This story's standing rules (the round is finding a new style, so only these bind)

## Rules for this story

- **Round 3 (2026-11-13): Suno makes all of the audio:** the crew's shouts in speech mode, the siren, the monitor and the flatline tone, and background music that fits the scene (Jack). The minister's line can be Suno's or Orus.
- **The whole track is about 14 s:** a dying man in an ambulance (0–5 s), held at a red light (5–7 s), the minister's car crossing (7–11 s), then the flatline, silence, and the logo on black (11–14 s). The picture is cut to the track.
- Swearing is said in full, never bleeped. If Suno refuses a word, swap the word.
- No speech in any Flow clip.

## Never

- A cheerful or comedic score: it must feel like real hospital-drama urgency.
- Music over the flatline: it ends in the tone and then silence.

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "v6",
  "durationSec": 14
}
```

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

**no-score-fly-on-the-wall** — The Pitt approach: almost no music, the drama carried by real sound. Fast monitor beeps, a two-tone UK ambulance siren (not an American wail), rain drumming on the roof, kit clattering. The only musical element is one low sub-bass drone that swells under the minister's car. The crew are a Scouse woman and a Geordie man, raw and overlapping, half-shouted rather than performed, with a Bristolian driver. The minister is a languid Old Etonian drawl in his twenties or thirties, a sneering tenor, muffled and tinny as if heard through a car window. The flatline tone holds, then silence. The style box asks for documentary realism, spoken, no singing, no melody.

Other writers are doing the other experiments (bbc-drama-strings-two-worlds, british-thriller-trailer-braams, line-of-duty-circling-piano, violin-jabs-and-garden-party, pomp-against-pulse). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Style boxes: spoken english voices

Your previous draft:
```json
{
  "name": "no-score-fly-on-the-wall",
  "style": "Unscored British observational TV, like an ER drama with the music stripped out, actuality audio captured in the back of an NHS ambulance on a wet night. Spoken English voices only, strong regional UK accents, nobody sings, no tune, no rhythm section. Sound effects do the work: frantic ECG beeping, old-school British two-pitch nee-naw horn, rain hammering the roof, suction and oxygen hiss, drawers and kit banging, engine revving hard. Crew talk over each other, ragged and breathless, half-yelled, never acted. Female paramedic from Liverpool, thick Scouse; male paramedic from Newcastle, broad Geordie; driver from Bristol, West Country burr. Contrast: a languid public-school toff, late twenties, nasal sneering tenor, received pronunciation, boxed-in and muffled like a voice behind a car window. One deep sub drone rises beneath the toff and nothing else musical. Final seconds: the heart machine locks into a single unbroken pitch, which cuts to total quiet. Short, 14 seconds.",
  "exclude": "American accent, US accent, American siren, US police wail, singing, melody, sung vocals, choir, strings, piano, drums, beat, rap, orchestral score, cinematic trailer, synth pads, upbeat, happy, comedy, music under the flatline, fade in, long intro",
  "lyrics": "[Spoken, unscored, mics inside a racing British ambulance, rain on the roof, two-tone nee-naw, ECG beeping fast]\n[Scouse woman, Liverpool paramedic, shouting over the siren]\nSixty over thirty! Fucking hurry up, we're gonna lose him!\n[Geordie man, Newcastle paramedic, talking over her, out of breath]\nSats dropping, he's peri-arrest!\n[Bristolian driver, West Country, bellowing at the traffic, horn blast]\nTwo minutes out! Get the fuck out of the way!\n[Brakes squeal, siren stops, engine idles, rain, ECG still racing]\n[Geordie man, disbelief]\nWhy have we stopped?!\n[Low sub drone rises. Plummy Old Etonian on his phone, bored and petulant, muffled behind car glass, another world]\nI said raspberry-shaped hors d'oeuvres!\n[Drone falls away. Scouse woman, quiet, almost to herself]\nFifty over twen—\n[Flatline, one long unbroken pitch]\n[Total quiet]\n[End]",
  "model": "v6",
  "variety": "normal",
  "weirdness": 30,
  "styleInfluence": 80,
  "vocalGender": null,
  "durationSec": 14,
  "maxMode": false
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/shorts/priority-lane/songs/r4-suno/writers/no-score-fly-on-the-wall.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/shorts/priority-lane/songs/r4-suno/writers/no-score-fly-on-the-wall.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "no-score-fly-on-the-wall". Reply with just the two paths.