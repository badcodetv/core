You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

the music should be like https://www.youtube.com/watch?v=LGD79pQY1kI dammed bo1 zombies, research this please. animate them please. thanks Please clean room it all and research the internet to achieve it. Thanks.

## What happened in earlier rounds (facts)

- The track is the whole audio of a ~17-second vertical short (BadCode Shorts, "The Malevolent Force"): buying bread at a British corner shop at night, shot like a haunting. No voice anywhere (Jack, 2026-11-16: "No voice, one end card"). Shorts Suno tracks are music and sounds only, never speech (Jack, 2026-11-15).
- The picture, in order (stills on cheap colour night film, fluorescent teal; each will be a short animated clip):
  - 0-2 s: the only lit corner shop on a dead terraced street at 3am.
  - 2-4 s: from inside, the glass door swings open by itself onto the black street.
  - 4-6 s: down the aisle, one fluorescent tube dead, the stockroom door half open onto black.
  - 6-10 s: one loaf on a bare shelf, label 50p; the tube flickers and on each flicker the label changes: £1, then £5. (Hits wanted on each flicker.)
  - 10-12 s: a convex security mirror: the aisle is empty, fresh blank banknotes scattered on the floor.
  - 12-15 s: the doorway, "BREAD £50" taped to the glass, the stockroom door wide open at the back with cold light pulsing; a chocolate bar on the mat, 10p crossed out, £12.
  - 15-17 s: end card, white text on black: "Based on true events. Coming to a shop near you." (a horror-trailer tagline; the joke lands here, so the music should land a final hit and then hang or cut).
- The point: inflation is a force you can't see; someone decides who gets the new money first, and you meet it last at the till. Never one person.
- No earlier music rounds for this short.

## The reference

- https://www.youtube.com/watch?v=LGD79pQY1kI : Jack names it "dammed bo1 zombies" (the "Damned" music from Call of Duty: Black Ops (2010) Zombies mode). Nobody has listened to it in this session; research what it is and how it sounds. Never name the game, its composer or the track in a Suno prompt.

Fetch its public page yourself as well, if it has one.

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "v6",
  "durationSec": 17
}
```

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**horror-trailer-strings** — A string ensemble horror-trailer cue: col legno tapping and sul ponticello tremolo violins build tension, with glassy harmonics on top and a low cello drone. Ask for it like a film composer's brief for a 17-second teaser, naming the techniques. The three flickers are three vicious string stabs with a braam-like low brass swell after the last; a final orchestral hit at 15 seconds, then the trailer silence and one high violin harmonic hanging.

Other writers are doing the other experiments (lone-reverb-piano, dying-music-box, distorted-industrial-theme, techno-through-the-wall, fluorescent-sound-design). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-malevolent-force/songs/r1-track/writers/horror-trailer-strings.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-malevolent-force/songs/r1-track/writers/horror-trailer-strings.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "horror-trailer-strings". Reply with just the two paths.