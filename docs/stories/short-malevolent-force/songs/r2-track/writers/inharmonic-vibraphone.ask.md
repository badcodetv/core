You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

look at the picks and make the music more like ambient silent hill music thanks

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
- Round 1 (2026-11-16): six instrumental directions modelled on the Black Ops 1 zombies "Damned" theme (lone reverb piano, dying music box, distorted industrial, techno through the wall, horror-trailer strings, shop-hum sound design), two takes each. Jack picked none and said: "make the music more like ambient silent hill music".
- Jack's picked clips (the picture is settled): the shop on the street with its lights dipping; the glass door swinging wider by itself; the aisle with the stockroom door opening; the 50p loaf as the tube browns out and comes back; the convex mirror rocking. The last shot is being remade: a flash of lightning, horror style, and the bread and the chocolate bar change price, somewhere else in the shop.
- The Duration box read 15 s last round even when 17 was asked; about 15 s is fine.

## The reference

- Jack, 2026-11-16: "ambient silent hill music" (the Silent Hill video game series' ambient/industrial soundtrack). Research what that sound is. Never name the game, its composer or any track in a Suno prompt.
- Round 1's reference (what he moved on from): the Black Ops 1 zombies theme "Damned", https://www.youtube.com/watch?v=LGD79pQY1kI.

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

**inharmonic-vibraphone** — The lead performer is a vibraphone and tuned bells played with soft mallets, slightly out of tune with each other so the notes beat and shimmer against one another, with long open reverb that makes a small shop sound like a vast empty hall. Ask for it in technical timbre words: dark timbre, inharmonic overtones, beating harmonics, dense spectral fullness, slow attack, no tempo. A grinding low noise rises slowly underneath the bells and thickens; on the flickers single bells are struck harder. At the end one dissonant cluster is hit together and left to decay. Exclude drums, vocals, guitar, orchestra, bright major.

Other writers are doing the other experiments (rust-foundry-percussion, detuned-bell-piano, shortwave-static-signal, lonely-reverb-guitar, siren-and-pulse). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-malevolent-force/songs/r2-track/writers/inharmonic-vibraphone.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-malevolent-force/songs/r2-track/writers/inharmonic-vibraphone.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "inharmonic-vibraphone". Reply with just the two paths.