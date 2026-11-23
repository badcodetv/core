# Brief: By the Balls, cast portraits and stills, round 1

You write prompts for Google Flow, Nano Banana 2.1, 9:16 portrait stills. Read ONLY this brief and look at the images
it names (all in this folder). Research freely on the web how British amusement arcades look at night, how claw
machines are built (the claw, the glass box, the prize chute, the joystick and button, the coin slot), and how the
people asked for below dress and look.

## The story's facts
- A short film: a young couple feeds coins into an arcade claw machine. The prize in the glass is a small model of a
  house (a little two-storey family house, like a toy or a dolls' house, about the size of a shoebox) sitting among soft
  toys. The claw grabs the house, lifts it, then goes limp at the top and drops it. Again and again.
- A masked figure (BadCode) stands beside the machine and speaks one line to camera.
- At the end, a dial on the front of the machine is turned by the couple and the people queuing behind them, and the
  claw finally holds the house and drops it in the prize chute.
- The couple, in the director's words, verbatim: "make sure the young couple look like stereotypical millenials thanks".
  Decide for yourself, from your research, what that means for each of them (age, hair, clothes, accessories, phone,
  coffee, tote bag…), and make them two clearly different people with a few features of their own (nose, hair, brows,
  glasses or not). Ordinary people: never like any famous person.
- No readable text, logos, brand names or real characters (no famous cartoon or game characters among the soft toys).
  Text is added later.

## The look: one line
Real-looking photographs, shot in a real British amusement arcade at night; each still follows its reference photo's
layout and light, and the prompt says what changes.

## Images in this folder
- `ref-play.jpg` (a person at a claw machine, side-on, the joystick in front), `ref-claw.jpg` (the claw over the prizes,
  close), `ref-machine.jpg` (a whole claw machine from the front: glass box above, panel and chute below),
  `ref-badcode.jpg` (a person standing among claw machines, facing the camera), `ref-panel.jpg` (a close-up of a
  machine's control panel).
- `mask-reference.jpg` and `mask-wording.txt`: the BadCode balaclava. Every prompt that shows BadCode attaches
  `mask-reference.jpg` and pastes the text of `mask-wording.txt` verbatim.

## What to write
1. **Portraits first** (one each, head and shoulders, face about a third of the frame, plain soft light, a dark arcade
   blurred behind): `CAST-HER`, `CAST-HIM`, `CAST-BADCODE` (BadCode: decide what he wears below the mask, something
   that fits an arcade; gloves). These become the references for every later still.
2. **Stills, two genuinely different takes per shot** (ids `<SHOT>-a`, `<SHOT>-b`). Each still attaches its reference
   photo and the portraits of whoever is in it; when a portrait is attached, never describe that person's appearance,
   only what they do and their expression. Point at a reference by role ("the woman from the portrait").
   - `PLAY` (ref-play): the couple at the machine, side-on, one hand on the joystick, faces lit by the machine, hopeful.
   - `GRAB` (ref-claw): inside the glass, close: the claw closing round the little house among the soft toys.
   - `LIMP` (ref-machine): the claw at the top of the glass box, prongs hanging open, the little house falling back.
   - `FACES` (ref-play): the couple, closer, the moment the house drops: deflated.
   - `BADCODE` (ref-badcode + CAST-BADCODE + mask-reference): BadCode standing beside the claw machine, looking into the
     lens; the couple small and soft-focus behind.
   - `DIAL` (ref-panel): the front panel of the claw machine, close: one big round dial with a pointer, set into the
     panel beside the joystick; several hands of different people reaching to turn it together. No text on the dial.
   - `WIN` (ref-machine + the couple's portraits): the little house in the prize chute at the bottom of the machine, the
     couple's hands reaching in, delighted.

## Rules
- One paragraph per prompt, your own words, under ~120 words. 9:16.
- Describe only what should be in the picture; never name the thing to leave out.
- No sign-off at the end of a prompt.

## Output
Write `prompts-r1.json` in this folder:
{"portraits": [{"id", "prompt", "attach": []}], "stills": [{"id", "shot", "prompt", "attach": ["<file names in this folder, or CAST-HER / CAST-HIM / CAST-BADCODE>"]}]}
Reply with one line.
