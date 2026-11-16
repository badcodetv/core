You are writing Suno v6 prompts for a song. Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

Jack, 2026-11-16 (the lyrics he pasted are in lyrics.txt): "use this, now reserch the internet and clean room it, on how to parody ten crack comandments beat and style and how to get biggies voice for suno. THansk"

## What happened in earlier rounds (facts)

- A BadCode short (9:16, phones), about 30 seconds. A parody of a famous 1997 New York rap song in which the rapper counts down ten street-hustle rules over a sparse, hard boom-bap beat, with a voice sample counting the numbers between rules. Here the rules are about who controls the money printer.
- Jack asked for the track to sound like that song's beat and style and the rapper's voice (the late Brooklyn rapper of the 1990s). Suno refuses real artist names: describe the sound, never name an artist, song or producer.
- 🔴 Parody of style, not a copy: no reproduction of the original beat, its samples or its melody. The era and genre feel are fine.
- Vocals ARE wanted on this one (Jack asked for the rap). The lyrics must be sung exactly as written in lyrics.txt.
- Duration set to 30 s on Suno v6.

## Never write these

Notorious
Biggie
B.I.G.
Ten Crack Commandments
DJ Premier

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "v6",
  "durationSec": 30
}
```

## The lyrics

Use these words exactly — do not change, add or remove any word or spelling. You may add section tags and short directions in square brackets. Keep every line.

```
Uh. Uh-huh.
Money printer manual. Page one. Take notes.

Number one: never tell 'em what you printed,
trillions out the back door, keep the ledger tinted.

Number four: never get high on your own supply,
banks took the first hit, now the rent's sky-high.

Number six: no credit? Nah, they live on the slate,
and you're paying it back in the price on your plate.

Number seven: keep the family out the business,
Treasury and the bank in one bed, God as my witness.

Number ten: no consignment, cash up front, that's law,
they took the bailout on tick and they ain't paid at all.

And the fix, from the future? Easy.
No hand on the printer.
```

## What to produce now

Not prompts yet. Propose exactly 6 experiments for this round. Each one is a genuinely different idea for how to answer the request — different from each other in the voice (who is singing and how — different performers, not one performer in different accents) and in how the music is asked for. A separate writer will turn each idea into one prompt, and none of them will see the others'
prompts, so make each idea complete and distinct on its own.

Write a short list of what your research found (with source URLs) to
`/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r1-rap/writers/ideas.notes.md`, and write ONLY a JSON array to
`/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/songs/r1-rap/writers/ideas.json`: objects with keys "name" (short kebab-case) and "idea"
(3–6 sentences). Reply with just the two paths.