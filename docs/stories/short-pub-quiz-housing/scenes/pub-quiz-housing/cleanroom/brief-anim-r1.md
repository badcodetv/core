# Brief: clip motion, round 1 (clean room)

You write motion prompts for Google Flow's video model **Omni 1.2 Flash**, image-to-video in **Frames** mode: the still
below is the first frame, the clip is **8 seconds**, portrait 9:16. Read only this file and the twelve images named
below. Do your own web research on how this model and image-to-video models in general behave (what makes motion look
real or fake, lip movement, small gestures, camera lock). Write your output to the JSON file named at the end.

## The film
A 50-second vertical short. Quiz night in an old English pub, late, lit by on-camera flash. A quizmaster in a balaclava
reads a question; one table of four whispers its answer so the next table can't hear, against a 30-second clock. The
voices are recorded separately and laid over the clips afterwards.

## The twelve shots (first frames)
All in `/home/jackt/.cache/badcode-refs/pub-quiz-housing/shots/`:
- `P01.jpg` The quizmaster at the bar reads the question into the microphone; the room looks up at him.
- `P02.jpg` The four huddle over the answer sheet; the young man in the hoodie whispers: "A hundred million? That's loads."
- `P03.jpg` Overhead: a hand writes a number on the answer sheet.
- `P04.jpg` The plasterer crosses the number out and whispers: "More. I've done three of them B&B jobs for the council this year. Every room, every night."
- `P05.jpg` The young man in the hoodie does sums on a beer mat, whispering: "Say fifty quid a night. Times three-sixty-five. Times a hundred thousand rooms?"
- `P06.jpg` The plasterer turns on the eavesdropping next table: "Fuck off, get your own answers." They lean back.
- `P07.jpg` The man in the suit, not looking up from his pint, sneers: "Paying by the night is the dearest way to buy anything. It's billions with a B. Keep up, you morons."
- `P08.jpg` The man in the olive waterproof quietly takes the pen and the sheet; the others go still and watch him.
- `P09.jpg` Over his shoulder: he turns the sheet; the man in the suit reads it and gives a small, grudging nod.
- `P10.jpg` The quizmaster: "Pens down." Then he reads the answer from the card.
- `P11.jpg` Overhead: the table frozen, staring at the sheet.
- `P12.jpg` The young man in the hoodie asks, open-handed: "So they rent the same rooms every year? Why don't they just own them?" The man in the suit turns to him.

## Write two options per shot
Two genuinely different ways for each, an option **a** and an option **b** (for example: a smaller, quieter performance
and a bigger one; or the motion carried by a different person or object). One clear action per option.

## Rules for every prompt
- Start with "The camera does not move." and end with "The camera does not move." then "Thanks." on its own line.
  (Camera moves are added later in editing.)
- One continuous shot, no cuts.
- At most three people moving; everyone else holds almost still. Name exactly one ambient motion (for example the
  froth settling in a pint, someone's breath, a lamp's flicker) so the rest of the frame settles.
- Where a person speaks in the shot, write the exact spoken words in the prompt, in quotation marks, as a quiet whisper,
  said once, starting about half a second in, mouth closing after (the voice is replaced later, so the lips must move to
  these words and nothing else). Where nobody speaks, ask for room sound only: a quiet pub murmur, glasses.
- The quizmaster's face is a balaclava with no mouth: he never needs lip movement; he gestures with the microphone and card.
- Keep everyone's face, clothes and the room exactly as in the still; describe only what they do and their expression,
  never their appearance.
- In a photographic look, fast movement blurs: add "shot at 24fps with a 180-degree shutter" where anything moves fast.
- No readable text, no new people entering, nobody standing up and leaving frame unless the shot needs it.
- Under 90 words each. Plain sentences. State what happens, positively.

## Output
Write `/home/jackt/projects/badcode/badcode/docs/stories/short-pub-quiz-housing/scenes/pub-quiz-housing/cleanroom/anim-r1.json`:
```json
[{"n": 1, "still": "P01", "options": [{"id": "a", "label": "<3-6 words>", "prompt": "<the prompt>"}, {"id": "b", "label": "...", "prompt": "..."}]}, ...]
```
Twelve entries. In your final reply, one line per shot naming the two options.
