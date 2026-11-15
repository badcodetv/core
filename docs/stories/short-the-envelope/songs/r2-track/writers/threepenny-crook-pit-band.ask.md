You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

never should be dialgogue on these suno tracks for shorts unless i ask specfically, please only do music and sounds, not dialogue. thanks

## What happened in earlier rounds (facts)

- The track is the whole audio of a 15-second vertical short (BadCode Shorts, "The Envelope"). The picture is already made and will be cut to this track: four painted 1930s chapter cards, each animated about 3.5 s.
  - 0–3.5 s THE COUNTER: a smooth dealer in a fedora at a backstreet betting counter fans two envelopes, one stamped APPROVED BY THE CONSERVATIVE PARTY, one APPROVED BY THE LABOUR PARTY, even odds.
  - 3.5–7 s THE PICK: an old working man in a flat cap wavers between the two envelopes; the dealer waits with open palms.
  - 7–10.5 s THE SWITCH: the dealer tips two bowler hats towards us, an envelope in each; under them sits one crate stencilled ORDER No. 0417 with fresh money on it; a shill behind grins and fans banknotes. Both choices lead to the same arms order.
  - 10.5–15 s THE PAY-OFF: a figure in a black balaclava pulls back a red curtain; behind it a man in a blue tie and a man in a red tie, mid-handshake over a crate of rifles, turn round, caught. Card text: EVERYTHING ELSE IS A DISTRACTION.
- The line (Jack, 2026-11-15) is NOT in the track: "They're going to print the money and the weapon sales will still happen anyway, everything else is a distraction." It is handled outside Suno; leave room for it over the last card (about 10.5-15 s) and keep that stretch sparse.
- Jack wanted a "The Sting" switcheroo version (the 1973 con film): a 1930s con where the mark never knows. Jack on the music, 2026-11-15: invented period piano, not Joplin, not the film's score (nothing copied from the film).
- Kai, 2026-11-13 meeting, on the shorts' audio: "these shorts have a rhythm to them that misses the music … I don't mean a tune … sounds that massively increase the richness of the message … Give me this guy screaming this, followed by a quick jab on a violin, followed by a meek little child with a little pattern of foreboding music behind it, smashed it. That's what the shorts should be." Also: "suno has a speech mode as well now." Sound effects and music are made together in ONE Suno track.
- Length: Suno v6 obeys a set Duration to about a second; Auto runs long. The target is 15 s.
- Jack, 2026-11-15, after round 1 (every take spoke the line): "never should be dialogue on these suno tracks for shorts unless i ask specifically, please only do music and sounds, not dialogue." So: INSTRUMENTAL, music and sound effects only, no voice, no speech, no singing, no words.
- Round 1 ideas (for reference, all spoke the line): a 1930s radio-serial organ-sting score with foley; a stride-piano hustle that stops dead; a detuned upright behind a wall in a back room; a novelty-piano flurry then a violin jab.

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

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**threepenny-crook-pit-band** — A 1928 Berlin crook-cabaret pit band in the Threepenny manner, not piano-led: a chugging banjo and a wheezing harmonium carry the hustle, a nasal alto saxophone is the lead voice that sidles round the two envelopes, and a muted trumpet answers it sarcastically. Foley sits inside the band: a paper flick as the envelopes fan, a coin set on a wooden counter, a timpani thud landing on the switch at 7 s. At 10.5 s the band cuts out mid-phrase, leaving a single held harmonium chord and one dry banjo pluck as the curtain goes back, sparse enough for a line over it. Instrumental, a sour minor-key march-foxtrot, the sound of respectable people cheating.

Other writers are doing the other experiments (hot-club-string-hustle, habanera-bandoneon-card-sharp, cartoon-studio-mickey-mouse-cue). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-the-envelope/songs/r2-track/writers/threepenny-crook-pit-band.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-the-envelope/songs/r2-track/writers/threepenny-crook-pit-band.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "threepenny-crook-pit-band". Reply with just the two paths.