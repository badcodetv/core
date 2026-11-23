You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-23, on the story-style page of seven sounds: "just make them in suno and skip this step going forward thanks"

Jack, earlier the same day, asked how the end should feel: "Swagger, then hope". On references: "You propose, I'll pick".
Jack, at setup: "have heavy oceans eleven references" (parody of the heist genre only).

The seven sounds shown on the page (one take each):
S1 1960s spy swagger · S2 hard funk groove · S3 British library cue · S4 the corner-shop break · S5 tiptoe cartoon caper · S6 colliery brass band · S7 clockwork pulse

## What happened in earlier rounds (facts)

- The music goes under a 9:16 short of about 18 seconds. Instrumental: music and sound only, no singing, no words.
- The picture, in order (locked): 0-3 s a back room, the plan on the wall, a finger taps the target twice; 3-6 s the crew
  of four walk out of smoke in slow motion, freeze on the last step; 6-8.5 s a laser-lit shop aisle, one ducks under a beam
  and reaches; 8.5-11 s the prize lifted up to the light, freeze; 11-14 s they stand frozen at a shop counter, a bulb
  sways, a snap zoom on the price tag at about 12.5 s (the price has gone up); 14-17 s a hand on a savings jar that has
  risen with the price; 17-18.5 s a logo in the snow, the end.
- The feel (Jack): swagger, then hope: slick heist feel, a deflating sting at about 12.5 s, then a lift from about 14 s
  that makes the ending feel like a win, then a clean button ending.
- A Liverpool man's voice says four short lines over the music (about 0-3, 6.5, 12, 15 s): the music must leave room.
- Nothing has been run in Suno for this short yet.

## This story's standing rules (the round is finding a new style, so only these bind)

## Story-only rules
- Jack and Kai write the jokes: beats say what each moment conveys; joke lines stay blank for them. The pitch's line
  ("It was 10p when we started planning.") is on the shorts list, not ruled.
- Parody of the genre only: never a film's title, logo, score, characters or any actor's likeness. The shop shows no real
  brand. The bar (Jack, 2026-11-23): a lookalike of the real purple frog wrapper, renamed **Freddoo**; never the maker's
  name or logo (cover it in post if Flow adds one).
- The prices (10p then, today's price) are read at source before they are said or shown.

## Never write these

Ocean's
Ocean's Eleven
David Holmes
John Barry
James Bond
Bond
Pink Panther
Mancini
Shaft
Freddo
Cadbury

## No lyrics

This is an INSTRUMENTAL: no voice, no singing, no words. Leave "lyrics" as an empty string ""; everything goes in the style and exclude boxes.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**library-cue** — British library cue: A 1970s KPM-style jazz-funk cue (Hammond, wah guitar, fuzzy bass, brass fanfare) that sounds like a TV caper from British telly. The sting on 39p is a 'tension' cue; the jar gets a 'Happy Ending' button. Why it fits: British where the heist genre is American, so it fits a corner shop and a Liverpool voice; it plays the joke as a cheap TV thriller. What it risks: Can tip into nostalgia telly and feel dated rather than slick; Jack asked for heavy heist-film swagger and this is its small-screen cousin.

Other writers are doing the other experiments (spy-swagger, hard-funk, corner-shop-break, tiptoe-caper, colliery-brass, clockwork-pulse). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Settings you choose per prompt: model "v6" or "v6-wild"; variety "off"/"normal"/"high"/"extra"/"max";
weirdness 0–100; styleInfluence 0–100; vocalGender "male"/"female"/null; durationSec 1–300; maxMode true/false.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Style boxes: a speaking voice

Your previous draft:
```json
{
  "name": "library-cue",
  "style": "1970s British TV library music, jazz-funk caper cue, instrumental, 100 BPM, swaggering and slick then hopeful. Opens on a hip tight drum break, punchy fuzz bass riff and choppy wah-wah guitar; Hammond organ stabs and a bold brass-and-flute fanfare on top. Sparse midsection with space left for a speaking voice. Sudden suspense sting: low brass swell, tremolo strings, cymbal scrape, then a hush. Then a warm major-key lift, bright horns and organ swelling into a cheerful happy-ending flourish, finishing on one clean brass hit. Vintage analogue tape, roomy studio, crisp and dry, small-screen thriller theme",
  "exclude": "vocals, singing, choir, spoken word, rap, lyrics, humming, modern trap drums, EDM, synthwave, orchestral film epic, lo-fi hiss, long fade out",
  "lyrics": "",
  "model": "v6",
  "variety": "normal",
  "weirdness": 30,
  "styleInfluence": 75,
  "vocalGender": null,
  "durationSec": 30,
  "maxMode": false
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-fredo-job/style/round-1/variations/writers/library-cue.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-fredo-job/style/round-1/variations/writers/library-cue.json`
with exactly these keys: name, style, exclude, lyrics, model, variety, weirdness, styleInfluence, vocalGender, durationSec, maxMode. "name" must be "library-cue". Reply with just the two paths.