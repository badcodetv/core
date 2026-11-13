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

**violin-jabs-and-garden-party** — Kai's brief taken literally: every shout from the crew is answered by one vicious stabbed violin jab, like punctuation, with a dark low cello drone underneath. The crew are a ragged West Country woman and a Lancashire man, with a Cumbrian driver: rural, northern and south-western working voices, very unlike London. When the minister's car crosses, the score turns into a twee, dainty harpsichord-and-string-quartet minuet, the music of a garden party, faintly heard as if from inside his car. He is a fruity, pompous, port-soaked old Tory gentleman, posh and indignant about canapés. Then the minuet is cut off by the flatline tone and silence.

Other writers are doing the other experiments (bbc-drama-strings-two-worlds, no-score-fly-on-the-wall, british-thriller-trailer-braams, line-of-duty-circling-piano, pomp-against-pulse). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/shorts/priority-lane/songs/r4-suno/writers/violin-jabs-and-garden-party.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/shorts/priority-lane/songs/r4-suno/writers/violin-jabs-and-garden-party.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "violin-jabs-and-garden-party". Reply with just the two paths.