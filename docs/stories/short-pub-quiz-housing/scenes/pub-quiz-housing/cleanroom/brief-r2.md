# Brief: stills, round 2 (clean room): the shots of the short

You write image prompts for Google Flow (Nano Banana 2.1, image edits with reference images, portrait 9:16). Read only
this file and the images named below. Do your own web research where it helps (how pub-quiz nights are shot, how to
frame close-ups of hands, faces and paper). Write your output to the JSON file named at the end.

## The film
A 50-second vertical short. Quiz night in an old English pub. A quizmaster reads a question into a microphone; one table
of four huddles and whispers its answer so the next table can't hear, against the clock. The look is already chosen.
This round makes **the shots that tell the story**, in that look.

## The chosen look (attach these; they are the continuity)
- `/home/jackt/.cache/badcode-refs/pub-quiz-housing/pick-quizmaster.jpg`: the quizmaster. Keep his outfit exactly: brown
  tweed three-piece suit, tweed flat cap, navy roll-neck, gold rings over black leather gloves, the navy balaclava with a
  white ring and a red triangle. The Victorian bar with the clock behind him.
- `/home/jackt/.cache/badcode-refs/pub-quiz-housing/pick-table.jpg`: the table of four and the room. Keep these four people
  and their clothes exactly (the man in the old waterproof jacket, the plasterer with dried plaster dust, the man in the
  suit with a loosened tie, the young man in the hoodie), the dark wood bar, green leather stools, and the light: late
  night, direct on-camera flash, hard shadows.
- `/home/jackt/.cache/badcode-refs/pub-quiz-housing/mask-reference.jpg`: the balaclava design, for quizmaster shots only.

Because these images are attached, **never describe a person's face, age, skin or build**: say only who it is (by their
clothes, as above), what they are doing and their expression. Always say what the quizmaster wears.

## The shots (one prompt each, in story order)
1. **S01 The question.** The quizmaster at the bar, microphone to his mouth, a question card in his gloved hand; the room's
   tables in front of him, people looking up. Wide enough to see the pub.
2. **S02 The huddle starts.** The four pull their chairs in round the small table, heads together over one answer sheet.
3. **S03 The pen.** Close on the answer sheet and a hand writing a number with a short pencil; pints and crisp packets at
   the edge. Writing unreadable.
4. **S04 Crossed out.** The plasterer's dusty hand striking through the number; his face just in frame, insistent.
5. **S05 The beer mat.** The young man in the hoodie scribbling sums on a cardboard beer mat, brow knotted, lips moving.
6. **S06 Eavesdroppers.** The next table leaning in towards them, one man cupping an ear; the plasterer turning round to
   glare at them.
7. **S07 The banker.** The man in the suit, not looking up from his pint, unimpressed, mid-sentence, a small sneer.
8. **S08 Bob takes the pen.** The man in the old waterproof jacket quietly taking the pen and the sheet, the others
   watching him.
9. **S09 The nod.** The man in the suit reading the sheet the quiet man has turned to him, a small nod.
10. **S10 Pens down.** The quizmaster, microphone up, holding the answer card, looking out at the room.
11. **S11 The answer lands.** The four at the table frozen, looking at the quiet man's sheet.
12. **S12 The way out.** The young man in the hoodie asking something, open-handed; the man in the suit turning to him.

## Rules
- Portrait 9:16 photographs, matching the attached table photo's flash look (S01 and S10 match the quizmaster photo's warm
  bar light instead). Vary the framing across the twelve: wides, mediums, close-ups, over-the-shoulder.
- Quizmaster shots attach pick-quizmaster.jpg and mask-reference.jpg, and contain this sentence exactly: "The balaclava
  exactly as in the attached image: no holes, no skin, gloves." No skin anywhere on him.
- Table shots attach pick-table.jpg only.
- No text, lettering, logos or brand names anywhere; paper writing unreadable; beer pump badges blank.
- No real or famous person's likeness.
- Every prompt ends with "Thanks." on its own line. Under 110 words each.

## Output
Write `/home/jackt/projects/badcode/badcode/docs/stories/short-pub-quiz-housing/scenes/pub-quiz-housing/cleanroom/prompts-r2.json`:
```json
[{"id": "S01", "idea": "<one line>", "refs": ["<paths>"], "prompt": "<the prompt>"}, ...]
```
Twelve entries, S01-S12. In your final reply, one line per shot.
