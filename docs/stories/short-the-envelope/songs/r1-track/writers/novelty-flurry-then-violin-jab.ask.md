You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

cut it thanks

## What happened in earlier rounds (facts)

- The track is the whole audio of a 15-second vertical short (BadCode Shorts, "The Envelope"). The picture is already made and will be cut to this track: four painted 1930s chapter cards, each animated about 3.5 s.
  - 0–3.5 s THE COUNTER: a smooth dealer in a fedora at a backstreet betting counter fans two envelopes, one stamped APPROVED BY THE CONSERVATIVE PARTY, one APPROVED BY THE LABOUR PARTY, even odds.
  - 3.5–7 s THE PICK: an old working man in a flat cap wavers between the two envelopes; the dealer waits with open palms.
  - 7–10.5 s THE SWITCH: the dealer tips two bowler hats towards us, an envelope in each; under them sits one crate stencilled ORDER No. 0417 with fresh money on it; a shill behind grins and fans banknotes. Both choices lead to the same arms order.
  - 10.5–15 s THE PAY-OFF: a figure in a black balaclava pulls back a red curtain; behind it a man in a blue tie and a man in a red tie, mid-handshake over a crate of rifles, turn round, caught. Card text: EVERYTHING ELSE IS A DISTRACTION.
- The spoken line (Jack, 2026-11-15), said once, over the last card or across the last two: "They're going to print the money and the weapon sales will still happen anyway, everything else is a distraction." The speaker is BadCode, the narrator from a future that already went wrong: certain, dry, sarcastic, a little nurturing underneath.
- Jack wanted a "The Sting" switcheroo version (the 1973 con film): a 1930s con where the mark never knows. Jack on the music, 2026-11-15: invented period piano, not Joplin, not the film's score (nothing copied from the film).
- Kai, 2026-11-13 meeting, on the shorts' audio: "these shorts have a rhythm to them that misses the music … I don't mean a tune … sounds that massively increase the richness of the message … Give me this guy screaming this, followed by a quick jab on a violin, followed by a meek little child with a little pattern of foreboding music behind it, smashed it. That's what the shorts should be." Also: "suno has a speech mode as well now." Spoken lines, sound effects and music are made together in ONE Suno track.
- Length: Suno v6 obeys a set Duration to about a second; Auto runs long. The target is 15 s.

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- Nothing from The Sting (1973): no Joplin rags (The Entertainer etc.), no Marvin Hamlisch arrangements.

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
They're going to print the money and the weapon sales will still happen anyway, everything else is a distraction.
```

## Your experiment

Write ONE prompt for this experiment, and only this one:

**novelty-flurry-then-violin-jab** — Build it as a timed four-part cue, written out by seconds in the style and lyric boxes: 0–7 s a dazzling invented novelty-piano flurry (showy runs, glissandi, a cheeky vaudeville bounce) with a woodblock tick; 7–10 s the piano trips and doubles up as the hats tip, a cash register rings; at 10.5 s everything cuts to one sharp violin jab and a low cello drone. Over the drone a very deep, slow, gravelled elderly man, grandfatherly and unimpressed, says the line once with weary authority, a tiny pause before 'everything else is a distraction'. Ask for the music as a sequence of events and instruments (solo piano, then violin stab, cello drone) with section tags [Intro], [Break], [Spoken word], [End]. Exclude Joplin rags, ragtime, film score pastiche and sung vocals.

Other writers are doing the other experiments (radio-serial-organ-stings, stride-hustle-cabaret-hostess, back-room-whisper-upright). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-the-envelope/songs/r1-track/writers/novelty-flurry-then-violin-jab.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-the-envelope/songs/r1-track/writers/novelty-flurry-then-violin-jab.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "novelty-flurry-then-violin-jab". Reply with just the two paths.