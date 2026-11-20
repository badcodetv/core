# Brief: stills, round 3 (clean room): the drunk regular, a running gag in three cutaways

You write image prompts for Google Flow (Nano Banana 2.1, image edits with reference images, portrait 9:16). Read only
this file and the images named below. Do your own web research where it helps (how slapstick is staged so it reads in
one glance, how a drunk man sits and slumps, how a fall is caught mid-moment in a still). Write your output to the JSON
file named at the end.

## The film
A vertical short, about 45 seconds. Quiz night in an old English pub: one table of four whispers its answer against the
clock. The look is chosen. This round adds **one new background character, a very drunk regular at the bar**, seen in
three short cutaways that get worse each time. He is pure physical comedy, harmless and silly; nobody is hurt and he is
never pitiful. He does not speak.

## The room (attach to every prompt)
- `/home/jackt/.cache/badcode-refs/pub-quiz-housing/pick-table-v2.jpg`: the room and the light. Keep the dark wood bar,
  the green leather stools with brass footrails, the bottles behind the bar, the bare wooden floor, and the light: late
  night, direct on-camera flash, hard shadows. **Do not include any of the four people at the table in this photo**, and
  not the man at the back table either: the drunk is somebody new.

## The drunk regular (invent him fully, so he is nobody famous)
Write him once in D00 and keep him word for word the same in D01-D03: a specific age (fifties or sixties), hair, face
features that are ordinary and particular (not handsome, not a type), and his clothes (a pub regular's, nothing that
matches the four at the table: no waterproof jacket, no suit, no hoodie, no plaster dust). No real or famous person's
likeness; never name or hint at anyone.

## The shots
1. **D00 Portrait.** Head and shoulders, his face big in frame, sat at the bar on a green stool, pint in front of him, eyes
   half shut, cheerfully sozzled. This is the reference for his face; it will be attached to D01-D03.
2. **D01 Leaning.** After the question is read. Wider: him on a green stool at the bar, already leaning badly to one side,
   pint held level with great concentration. Funny in one glance.
3. **D02 Sliding.** Mid-quiz. Same spot: he has slid most of the way off the stool, one arm hooked over the bar, legs
   splayed, still trying to look casual, pint still upright.
4. **D03 Going over.** At "pens down". The moment of the fall: the stool tipping, him going backwards, the pint flying
   with beer in the air; frozen at the peak. Slapstick, not painful.

## Rules
- Portrait 9:16 photographs, matching the attached photo's flash look and grain. D01-D03 are medium or wide so the whole
  gag reads; vary the angle across them.
- D00 attaches the room photo only. D01-D03 attach the room photo and D00 (say which is which by role: "the room from
  the pub photo", "his face from the portrait").
- Name every other person who appears (age, hair, clothes), or keep the bar empty around him; never "a crowd".
- No text, lettering, logos or brand names anywhere; beer pump badges blank; no branded packets.
- Every prompt ends with "Thanks." on its own line. Under 110 words each.

## Output
Write `/home/jackt/projects/badcode/badcode/docs/stories/short-pub-quiz-housing/scenes/pub-quiz-housing/cleanroom/prompts-r3-drunk.json`:
```json
[{"id": "D00", "idea": "<one line>", "refs": ["<paths>"], "prompt": "<the prompt>"}, ...]
```
Four entries, D00-D03 (for D01-D03 list the portrait as "D00" in refs). In your final reply, one line per shot.
