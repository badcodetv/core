# Brief: By the Balls, clips round 1

You write motion prompts for Google Flow's Omni 1.2 Flash video model, Frames mode: each clip starts on the attached
still (`start-<SHOT>.jpg` in this folder), 8 seconds, 9:16. Read ONLY this brief and look at the stills it names.
Research freely how Omni / Veo-style image-to-video prompts are best written, and how claw machines move.

## The film's facts
- A young couple at a claw machine in a British arcade at night. Inside the machine: only small model houses and money
  (coins, banknotes); the prize is a small white two-storey house with a red roof. The claw grabs the house and goes limp.
- A masked arcade worker (BadCode) says one line to camera; it is recorded separately and laid over later. His mask has no
  mouth: he does not visibly talk. His mask keeps facing the camera the whole time and keeps its white ring and red
  triangle exactly as in the still.
- At the end he unlocks a hidden dial on the machine and four people's hands turn it together (a vote); then the claw holds.
- Every clip's sound: sound effects and room tone only (arcade machines, coins, the claw's motor, the chute), never any
  speech, singing or voices. Music is added later.
- Nothing readable appears: no text, logos or brand names.

## The shots (one prompt each, two genuinely different takes per shot, ids `<SHOT>a` and `<SHOT>b`)
- `PLAY` (start-PLAY.jpg): she works the joystick, the claw glides over the houses towards the white house; both lean in, hopeful.
- `GRAB` (start-GRAB.jpg): the claw closes round the white house and starts to lift it.
- `LIMP` (start-LIMP.jpg): at the top, the claw's prongs go slack and the house tumbles back onto the pile.
- `FACES` (start-FACES.jpg): the moment after: he rubs his forehead, she breathes out; small, real, deflated.
- `BADCODE` (start-BADCODE.jpg): he stands very still, facing the lens; at most a slight tilt of the head; the couple behind keep playing.
- `UNLOCK` (start-UNLOCK.jpg): he turns the key and swings the steel cover fully open, revealing the dial.
- `DIAL` (start-DIAL.jpg): the four hands turn the dial together; the needle swings all the way round.
- `WIN` (start-WIN.jpg): the couple lift the house out of the prize hatch, laughing.

## Rules
- Keep the camera nearly still (a slight push-in at most); keep each person's face and size as in the still.
- Describe what moves and what stays; never name the thing to leave out. Under ~110 words each. Each ends with one
  "Sound:" sentence (effects and room tone only). No sign-off at the end.

## Output
Write `anim-r1.json` in this folder: {"clips": [{"id", "still": "<SHOT>", "motion"}]}. Reply with one line.
