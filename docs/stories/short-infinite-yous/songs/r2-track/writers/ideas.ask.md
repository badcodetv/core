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

## What to produce now

Not prompts yet. Propose exactly 6 experiments for this round. Each one is a genuinely different idea for how to answer the request — different from each other in the voice (who is singing and how — different performers, not one performer in different accents) and in how the music is asked for. A separate writer will turn each idea into one prompt, and none of them will see the others'
prompts, so make each idea complete and distinct on its own.

Write a short list of what your research found (with source URLs) to
`/home/jackt/projects/badcode/badcode/docs/stories/short-infinite-yous/songs/r2-track/writers/ideas.notes.md`, and write ONLY a JSON array to
`/home/jackt/projects/badcode/badcode/docs/stories/short-infinite-yous/songs/r2-track/writers/ideas.json`: objects with keys "name" (short kebab-case) and "idea"
(3–6 sentences). Reply with just the two paths.