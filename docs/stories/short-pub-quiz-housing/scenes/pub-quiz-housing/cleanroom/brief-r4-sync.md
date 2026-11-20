# Brief: round 4 (clean room): talking clips for lip-sync, three new stills

You write prompts for Google Flow: still images (Nano Banana 2.1, image edits with reference images, portrait 9:16) and
image-to-video motion prompts (Omni 1.2 Flash, Frames mode: the still is the first frame). Read only this file and the
images named below. Do your own web research where it helps (how Omni/Veo-style models animate speech and lips, how a
whisper looks on a face, how a pour into a glass is filmed for a product shot). Write your output to the JSON file named
at the end.

## The film
A vertical short, about 50 seconds. Quiz night in an old English pub, lit by on-camera flash. One table of four whispers
its answer against the clock. The voices are recorded separately and laid over the clips afterwards, so **each talking
clip's mouth must move to exactly the words given, and nothing else**.

All images are in `/home/jackt/.cache/badcode-refs/pub-quiz-housing/` (shots in `shots/`).

## Part A: talking clips (motion prompts only; the stills already exist)
For each, the speaker whispers the exact words once, at a brisk, quick pace, starting about half a second in, then closes
the mouth and holds still. Everyone else holds almost still. The camera does not move. Write the words after
"He whispers:" with no quotation marks. **Do not end these prompts with "Thanks."** (the model speaks it aloud). Under 70 words.

| key | still | speaker (as seen in the still) | words |
| --- | --- | --- | --- |
| L02 | shots/P02.jpg | the young man in the dark hoodie | A hundred million? That's loads. |
| L03 | shots/P04.jpg | the bearded man in the plaster-dusted jacket | More. I've done three of them B&B jobs for the council this year. Every room, every night. |
| L04a | shots/P05.jpg | the young man in the dark hoodie | Say fifty quid a night. I don't know how much things are, |
| L04b | shots/P05.jpg | the young man in the dark hoodie | I only buy CBD ramen suppositories. Every night. A hundred thousand rooms? |
| L06 | shots/P06v5a.jpg | the bearded man in the plaster-dusted jacket (to the red-bearded man facing him) | Fuck off, get your own answers. |
| L08a | shots/P07.jpg | the man in the suit, not looking up from his pint | Paying by the night is the dearest way to buy anything. |
| L08b | shots/P07.jpg | the man in the suit, not looking up from his pint | It's billions with a B. Keep up, you morons. |
| L13 | shots/P12.jpg | the young man in the dark hoodie | So they rent the same rooms every year? Why don't they just own them? |
| L15 | shots/P04.jpg | the bearded man in the plaster-dusted jacket | Every year. And at the end nobody owns a single brick. |
| L16 | shots/P12.jpg | the man in the suit | So buy the bricks. |

L10 (Bob's line) is in Part C, from a new still.

## Part B: three new stills (still prompts)
1. **S08c Bob, close.** Attach `bob-face.jpg` (his face) and `pick-table-v2.jpg` (the room, the table and the others).
   Medium close-up at the table: the older man in the olive waterproof jacket, his face about a third of the frame, lit by
   the flash, the answer sheet and a short pencil in front of him, looking up from the sheet to the others with quiet
   certainty, mouth closed. The others are out of focus at the frame edge. Point at the references by role ("his face from
   the portrait", "the room from the pub photo").
2. **D04 The drunk, asleep.** Attach `drunk-face.jpg` (his face and clothes) and `pick-table-v2.jpg` (the room). The same
   drunk regular (sixty-three, thin sandy-grey comb-over, bushy grey eyebrows, big ears, red bulbous nose, grey stubble,
   brown corduroy jacket, mustard knitted tank top, checked shirt) asleep sitting on a green stool at the bar, his cheek
   propped on one hand, elbow on the bar, mouth open, a half-drunk pint beside him. Medium shot, believable and still:
   this is a real drunk man dozing, not a cartoon.
3. **G01 The empty pint glass.** Attach `pick-table-v2.jpg` (the bar and the light). A plain, clear, straight-sided pint
   glass, empty, standing upright on the dark wood bar, dead centre, filling the middle of the frame, front-on at the
   glass's own height. A beer tap just above and behind it. The glass's front is completely plain and clean (nothing
   printed: a logo is added later). Shallow focus, the pub warm and soft behind. Still, product-shot clean.

Rules for the stills: portrait 9:16; no text, lettering, logos or brand names anywhere (beer pump badges blank); no real
or famous person's likeness; every still prompt ends with "Thanks." on its own line; under 110 words.

## Part C: motion prompts for the new stills
- **L10** (from S08c): the older man in the olive waterproof whispers once, quietly, at a brisk pace, starting about half
  a second in: I know literally no one who's been in them. Then closes his mouth and holds still. Camera does not move.
  No "Thanks." at the end.
- **D04m** (from D04): asleep, his cheek slowly slides off his hand and his head drops and thunks onto the bar; he stays
  asleep. All in the first two seconds, then still. Real, small, believable movement; nothing flies; no one else moves.
  Camera does not move. Ends with "Thanks."
- **G01m** (from G01): beer pours from the tap into the glass and fills it to the top with a clean white head; the glass
  itself never moves, turns or changes shape, the camera never moves (a logo will be laid onto the glass afterwards, so
  the glass must stay exactly where it is). About six seconds. Ends with "Thanks."

## Output
Write `/home/jackt/projects/badcode/badcode/docs/stories/short-pub-quiz-housing/scenes/pub-quiz-housing/cleanroom/prompts-r4-sync.json`:
```json
{"talking": [{"key": "L02", "still": "P02", "motion": "..."}, ...],
 "stills": [{"id": "S08c", "refs": ["<full paths>"], "prompt": "..."}, ...],
 "motions": [{"key": "L10", "still": "S08c", "motion": "..."}, {"key": "D04m", "still": "D04", "motion": "..."}, {"key": "G01m", "still": "G01", "motion": "..."}]}
```
In your final reply, one line per item.
