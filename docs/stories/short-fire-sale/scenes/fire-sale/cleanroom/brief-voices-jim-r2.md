# Brief: Jim's voice, round 2 (Fire Sale)

Write the JSON file named at the bottom. Read nothing else from the repo.

## The character
Jim, a wheeler-dealer of about 50 at a rainy English car-boot sale: round red-cheeked face, a flat cap, a black jumper
and a dark jacket. He sells framed pictures off a pasting table to a weary woman who is just browsing. The joke is that
he's flogging the country's institutions as if they were knick-knacks: he means it as ordinary banter, no big sell.

His lines (the words are fixed, do not change or add words):
1. "Hospitals, love. Forty quid."
2. "The courts. Slightly used."

## The note this round answers (Jack, the director, word for word)
"more essex geezer please reserach it and clean room it, make the accent subtle and not ai slop thanks"

## What round 1 did, and why it missed
Round 1's Essex option was designed as "An Essex market trader of about fifty-five: cheerful, chancing, quick patter, a
warm rough voice that has shouted prices across a field for thirty years", and was rendered with an added delivery
style "cheerful market patter". Personality and performance words like these push the engine into an impression of a
character, which is what reads as "AI slop". The other options were a Black Country man and a South London geezer.

## The engine (Google AI Studio voice design, model gemini-3.8-flash-tts)
- A voice is created once from a 1-2 sentence plain description (language en-GB). The description sets who the
  speaker is: age, sex, where from, the sound of the voice. Then the lines are read with **no style and no direction**.
- Google's guidance and our own tests: the accent comes from naming the place, not from describing sounds. Spelling out
  phonetics ("drops his h's, glottal t's") produces a caricature. Performance and personality adjectives ("cheerful",
  "cocky", "a wink in every word", "patter") produce acting. What has sounded real: who, where from, the voice's pitch and
  texture, and "speaks plainly" or similar. A word like "subtle", "light" or "mild" before the accent keeps it real.
- British library voices tend to sound posh and high: ordinary men need a lower, plainer voice stated.

## Your job
1. Research on the web what a real Essex man of about 50 sounds like today (Estuary English and broader Essex speech;
   which towns, which backgrounds; how it differs from Cockney and South London) and what separates a real one from a
   caricature. Note your sources.
2. Write **five** voice descriptions, each 1-2 sentences, each a genuinely different real Essex man (different town or
   background, voice texture, age within 45-60), all with a subtle accent and nothing performed. Every one must still
   fit a man who would run a car-boot stall and be called a geezer.
3. Rank them: which you'd bet on, and why, in one line each.

## Output
Write `docs/stories/short-fire-sale/scenes/fire-sale/cleanroom/voices-jim-r2.json`:
```json
{"research": "<5-8 lines: what you found, with source URLs>",
 "designs": [{"name": "jim-r2-a", "desc": "<1-2 sentences>", "why": "<one line>", "rank": 1}, ...]}
```
Names jim-r2-a to jim-r2-e.
