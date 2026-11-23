# Brief: The Fredo Job, crew portraits and stills, round 1

You write prompts for Google Flow, Nano Banana 2.1, 9:16 portrait stills. Read ONLY this brief and look at the images
it names (all in this folder). Research freely on the web how slick heist films of the 2000s stage their crews and
their plans (the slow line-up walk, sharp tailoring, the plan on a wall, laser grids, the precise grab), how a British
corner shop / newsagent looks inside at night, and how a split-flap departure board looks.

## The story's facts
- A short film. A crew of four masked figures plans a stylish, deadly serious heist, as if robbing a casino vault. The
  target: one small, cheap chocolate bar shaped like a frog, in plain gold foil, in a glass jar on a British corner
  shop counter. When they started planning it cost very little; by the time they pull the job off, the price has gone
  up nearly four times.
- The ending shows a better way: money that keeps up with prices. Three ideas are being tried (shots WAY-A, WAY-B,
  WAY-C below); make each one clear without words.
- The director, verbatim: "have heavy oceans eleven references". Use the genre's look and staging only (the cool
  tailored crew, the line-up, the plan, the precision); never a film's title, its characters, any actor's face or likeness,
  its logo or its posters.
- The crew: every member wears the BadCode balaclava (below), so no faces. Make the four clearly different by build,
  height and outfit (decide from your research: think sharp, varied heist-crew tailoring), and give each a trade shown by
  a prop (for example a drill case, a laptop, a coil of rope, a stopwatch; your call). Gloves on every hand.
- No readable text, numbers, logos or brand names anywhere: price tags, the board and the pay slip are blank, words are
  added later. No real chocolate brand: the bar and wrapper are plain.

## The look: one line
Real-looking photographs that follow each reference photo's layout and light, staged like a slick 2000s heist film.

## Images in this folder
- `ref-board.jpg` (a blueprint on a table under a lamp), `ref-crew-a.jpg` (silhouettes walking down a dark corridor),
  `ref-crew-b.jpg` (people walking away through haze), `ref-aisle.jpg` (a dim shop corner with jars on shelves),
  `ref-jar.jpg` (glass jars on a counter in a dark shop), `ref-shelf.jpg` (a crowded shop shelf), `ref-counter.jpg` (a
  shopkeeper behind a counter with jars), `ref-flap.jpg` (a split-flap board).
- `mask-reference.jpg` and `mask-wording.txt`: the BadCode balaclava. Every prompt that shows a crew member attaches
  `mask-reference.jpg` and pastes the text of `mask-wording.txt` verbatim.

## What to write
1. **Portraits first:** `CAST-CREW-a` and `CAST-CREW-b`, two different takes: the four crew members standing in a row,
   full length, plain dark background, even light, facing the camera. These become the crew's reference.
2. **Stills, two genuinely different takes per shot** (ids `<SHOT>-a`, `<SHOT>-b`). Each still attaches its reference
   photo, plus `CAST-CREW` and `mask-reference.jpg` whenever the crew is in it. When CAST-CREW is attached, never
   describe the crew's clothes, only what they do ("the crew from the reference image").
   - `BOARD` (ref-board): the plan: a floor plan of a corner shop on a table or wall, the jar circled, photos and string;
     gloved hands pointing.
   - `CREW` (ref-crew-a for -a, ref-crew-b for -b): the four walk towards the camera in a line, slow and cool.
   - `LASER` (ref-aisle): the shop at night, a grid of thin red laser beams in front of the counter, one crew member
     bending through it.
   - `GRAB` (ref-jar): close: a gloved hand lifting one gold-foil frog bar out of the glass jar, the other bars below.
   - `TAG` (ref-shelf): the crew members staring at a small blank price tag on the jar, deadpan.
   - `WAY-A` (ref-flap): a split-flap board with two rows ticking up side by side (one for the price, one for the pay),
     blank flaps mid-flip; one crew member watches, relaxed.
   - `WAY-B` (ref-counter): no heist: one crew member at the counter in daylight, paying with coins for the frog bar; an
     ordinary shopkeeper (invent them, ordinary person, never like anyone famous) serving.
   - `WAY-C` (ref-jar): a clear savings jar of coins beside the jar of frog bars, the coin level up to the same height
     as the bars; a gloved hand dropping in one more coin.

## Rules
- One paragraph per prompt, your own words, under ~150 words. 9:16.
- Describe only what should be in the picture; never name the thing to leave out.
- No sign-off at the end of a prompt.

## Output
Write `prompts-r1.json` in this folder:
{"portraits": [{"id", "prompt", "attach": []}], "stills": [{"id", "shot", "prompt", "attach": ["<file names in this folder, or CAST-CREW>"]}]}
Reply with one line.
