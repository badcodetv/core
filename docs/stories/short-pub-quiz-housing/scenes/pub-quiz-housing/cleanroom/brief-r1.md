# Brief: stills, round 1 (clean room)

You write image prompts for Google Flow (Nano Banana 2.1, still images, portrait 9:16). Read only this file and the
images named below. Do your own web research. Write your output to the JSON file named at the end.

## The film
A 50-second vertical short set during a quiz night in an old English pub. A quizmaster reads a question into a
microphone; one table of four huddles and whispers its answer so the next table can't hear.

## What this round is for
To find **the look**: what the pub looks like and what the quizmaster looks like. Six prompts, each a different idea, so
the director can pick a direction. Make the six genuinely different from each other (light, lens, framing, time of night,
how busy the room is).

## The pub
A proper old English pub: dark wood, brass beer pumps, etched mirrors, patterned carpet, a fireplace or panelled walls,
low warm light. Not a modern bar, not neon, not an Irish theme bar, not American. Research what real traditional English
pubs look like (Victorian and Edwardian London pubs, old country pubs) and what a real weekday pub quiz night looks like
(answer sheets, short pencils, the quizmaster's microphone and a small speaker, pints and crisps on the tables).

Real photos to use as the **layout reference** for each prompt (the director found them on Unsplash). Each will be
attached to its Flow call, so Flow follows the room from the photo; your prompt says what happens in it and the light.
Do not copy any sign or lettering from them.
- `/home/jackt/.cache/badcode-refs/pub-quiz-housing/Q42GVPmNvy4.jpg`: a Victorian bar back with a clock and brass pumps
- `/home/jackt/.cache/badcode-refs/pub-quiz-housing/Vpbp6pl6oGQ.jpg`: a dark wood bar with green leather stools
- `/home/jackt/.cache/badcode-refs/pub-quiz-housing/jyAG98eMoZw.jpg`: a bar with a brass lamp and mirrored back shelves
- `/home/jackt/.cache/badcode-refs/pub-quiz-housing/FxO0uSQDeJk.jpg`: a dark corner, a red fringed lamp, a striped banquette
- `/home/jackt/.cache/badcode-refs/pub-quiz-housing/u5KnPb6SOj0.jpg`: a wood-panelled corner with wall lamps and small tables
- `/home/jackt/.cache/badcode-refs/pub-quiz-housing/8A4ZnQ9vxYg.jpg`: a busy pub, framed pictures on the walls (use the room only; never the people's faces)

## The quizmaster (prompts Q1, Q2, Q3)
A man in a full-face balaclava, dressed like a character from a late-1990s / 2000s London gangster-comedy film: research
that costume tradition (tweed three-piece suits, flat caps, long camel overcoats, open-collar shirts, sharp tailoring,
heavy rings worn over gloves). Each of Q1-Q3 is a different take on that wardrobe. **Never name any film, director, actor
or character in a prompt**: describe the clothes only.
- He stands at the bar or by a small table with a microphone on a lead and a sheaf of question cards.
- The balaclava: a second image is attached to these calls, `/home/jackt/.cache/badcode-refs/pub-quiz-housing/mask-reference.jpg`.
  Paste this sentence into each quizmaster prompt **exactly**: "The balaclava exactly as in the attached image: no holes, no skin, gloves."
- No skin anywhere: gloves on both hands, the balaclava's neck tucked into the collar, cuffs over the wrists.
  No robot parts, no metal, no lights.

## The table (prompts T1, T2, T3)
Four people huddled round one small table, heads close, whispering, one answer sheet in the middle:
- a plasterer in his forties, work clothes with dried plaster dust on them;
- a banker in his fifties in a good suit, tie loosened;
- a student of about twenty, in a hoodie;
- a man in his fifties, weathered, in an old waterproof jacket, quiet, the one holding the pen.
Ordinary, believable people, a mix of ethnicities; not models. The next table is visible behind, leaning slightly towards them.
No balaclava in T1-T3.

## Rules
- Portrait 9:16. Photographic, a real camera and lens; not illustration, not "cinematic" gloss.
- No text, lettering, logos or brand names anywhere (the answer sheet's writing unreadable; beer pump badges blank).
- No real or famous person's likeness.
- Every prompt ends with "Thanks." on its own line.
- Under 120 words each, plain sentences.

## Output
Write `/home/jackt/projects/badcode/badcode/docs/stories/short-pub-quiz-housing/scenes/pub-quiz-housing/cleanroom/prompts-r1.json`:
```json
[{"id": "Q1", "idea": "<one line>", "refs": ["<photo path>", "<mask path if a quizmaster>"], "prompt": "<the prompt>"}, ...]
```
Six entries: Q1, Q2, Q3, T1, T2, T3. Use each photo at most twice. In your final reply, list the six ideas in one line each.
