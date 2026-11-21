# Brief: clips round 1 (image to video)

You write motion prompts for Google Flow's video model (Omni 1.2 Flash, "Frames" mode: the still is the first frame;
8 seconds; 9:16). Each prompt says what MOVES, in order, from the first frame, and what stays still. Research first
(how image-to-video prompts are best written for a locked or slow camera; how a TV weather presenter moves), then write.

Write `anim-r1.json` in this folder: a list of `{"key", "still", "motion"}`, two DIFFERENT takes per still
(`<still>a`, `<still>b`, e.g. `F01a`, `F01b`). Look at each still (in the reference folder given to you) before writing.

## The short
A comedy played straight, real-looking, ~20 seconds. A TV weather forecast where the weather is the economy. The
camera pulls back to reveal a man in a suit off-set, blowing the map's clouds about with a plain desk fan. The cut
uses only about 2 to 4 seconds of each clip, so the action must start within the first second.

## Rules for every clip
- The presenter wears a balaclava: no mouth, so no lip movement, no talking face. He gestures and turns his head
  slightly; his mask keeps its exact pattern (white ring, red triangle over his own left eye).
- Words on the map stay readable and do not change spelling: only RENT, PRICES, WAGES and the tags THE TREASURY,
  BANK RATE, LANDLORDS' LOBBY, ENERGY FIRMS. No new text appears anywhere.
- The man with the fan does not speak.
- No new people enter. Faces keep their identity. No cuts inside a clip.
- Plain description of the motion; no camera brand words.

## The stills
- `F01` (forecast, wide): presenter beside the big map. The clouds drift across the map: RENT slides onto London;
  the presenter gestures at it with an open gloved hand. Camera still or a slow push-in.
- `F02` (pull-back): from behind the studio camera; presenter on the lit set at left, the man crouched with the fan
  off-set at right. The camera eases back/drifts to make the fan man the point; his fan runs, his hair and tie stir;
  on the screen the clouds slide the way the fan blows.
- `F03` (caught): the man crouched with the fan, looking up at the camera, sheepish. He holds the look, a little guilty
  shrug or half-smile, and keeps the fan running (blades blurred). Camera locked.
- `F04` (the way out): the map with the name tags on every cloud; presenter pointing up. The tags swing gently on
  their strings; he points from one tag to the next. Camera locked or a slight push-in. Words must stay sharp.
- `F05` (the button): the presenter holds the fan on the crouched man. The wind blasts the man: hair streams back, tie
  flaps, jacket flutters, he squints and leans away; the presenter stands perfectly still. Camera locked.
