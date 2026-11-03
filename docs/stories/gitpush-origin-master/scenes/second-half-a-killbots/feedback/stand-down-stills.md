# Stand-down stills (scene A, beat 12) — 2026-11-03

Kai's note on beat 12 (verbatim): *"The problem with this is the killbot is reversing. And so again, this is linked, I think, to the time before where we're too close to the door. So if we have this much further away from the door, racing towards the door, and then we switch to the kind of stand-down mode"*.

The shot under hud-12 (the flip from KILL MODE to STAND DOWN / NEW OBJECTIVE: SUSTAIN ORGANIC LIFE) was cut3-V4: the bot's-eye view over its own hull, driving right up to the green doors, then smoke and a lurch back (the reversing). The shot before it is now cut3-WA02 (pick wa-02). These options keep the door far off and make the bots **stop short**, never reverse. Variable tested: the camera position at the halt (V4's over-the-hull POV, the pack, a barrel view, wa-02's own camera, a skid close-up).

Stills only, no video credit spent; Kai picks first. Files: `D:\badcode-videos\gitpush-origin-master\clips\second-half\stills\stand-down\sd-NN.png` (sheet: `sd-sheet.jpg`; both candidates per option in `work/`). Model Nano Banana Pro, 16:9, Flow project f96cac0e. References: `work/v4-frame0.jpg` (V4 at 0.3 s), `stills/wide-approach/wa-02.png`, `moodboard/P1-patrol-blockbuster.jpg` (the canonical kill bot).

Same-prompt check: fresh.py flagged a 41-word near copy with wa-02 in every prompt; that is the story's locked 16mm and 16:9 suffix, kept on purpose. sd-04 also repeats wa-02's foreground-grass line, on purpose (same camera). The reference-role clause is shared across sd-01/02/05, also on purpose.

## sd-01  (candidate p1-a)

**Idea:** Over the hull (V4 framing), braked dead halfway up the slope; door small and centred under the HUD reticle; dust and clods thrown on ahead.

**References:** v4-frame0.jpg, wa-02.png, P1-patrol-blockbuster.jpg

```prompt
Using the first image for the robot's own point of view (its armoured grey hull and two rubber tracks at the bottom of frame, seen from just behind its sensor) and for the bunker entrance with its green blast doors, the second image for the long grassy chalk down, the overcast light and how far off the bunker is, and the third image for the tracked robot's design: the same view from behind the robot's hull, but it has just braked to a dead stop halfway up the long slope, far short of the bunker. The concrete entrance with its shut green doors is small and distant, centred on the skyline in the middle of the frame, with a long stretch of empty grass between us and it. Two fresh furrows of torn turf and chalk end abruptly under the front of the tracks, and the cloud of chalk dust the robot was throwing up keeps rolling forward past it, drifting on ahead up the slope. Clods of earth still falling, the tracks now still. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

## sd-02  (candidate p2-a)

**Idea:** Over the hull as the whole pack pulls up together across the slope; door a small notch far off.

**References:** v4-frame0.jpg, wa-02.png, P1-patrol-blockbuster.jpg

```prompt
Using the first image for the robot's own point of view (its armoured grey hull and two rubber tracks at the bottom of frame, seen from just behind its sensor) and for the bunker entrance with its green blast doors, the second image for the long grassy chalk down, the overcast light and how far off the bunker is, and the third image for the tracked robot's design: the view from behind the hull as the whole pack pulls up together. Either side of us, four more tracked robots like the one in the third image have stopped hard in a ragged line abreast across the hillside, noses dipped from braking, the dust they raised overtaking them and sliding on uphill. Far ahead and high up, the bunker entrance is a small grey notch with shut green doors on the skyline, a long way off. Nobody is moving. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

## sd-03  (candidate p3-b)

**Idea:** The bot's own view along its weapon barrel, door far off and sharp, dust drifting past (meant: barrel dipped as the stand-down gesture).

**References:** v4-frame0.jpg, wa-02.png, P1-patrol-blockbuster.jpg

```prompt
Using the first image for the bunker entrance with its green blast doors and the film look, the second image for the long grassy chalk down, the overcast light and the distance, and the third image for the tracked robot's design: the robot's own camera view looking out along its slim weapon barrel, which has dipped and now points down into the long grass a few metres in front of it, out of focus across the lower part of the frame. Beyond it, sharp and far away up the slope, the small concrete bunker entrance with its shut green doors sits in the middle of the frame on the skyline. A thin haze of chalk dust drifts past from behind, the robot standing still. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

## sd-04  (candidate p4-a)

**Idea:** wa-02's own long-lens side-on camera a moment later: the pack halted in a line mid-slope, door high right. Not a POV.

**References:** wa-02.png, P1-patrol-blockbuster.jpg

```prompt
Using the first image exactly for the camera position, the long-lens compression, the hillside and the concrete bunker entrance high on the upper right with its shut green doors, and the second image for the tracked military robots: the same far-off side-on view a moment later. The pack of five tracked robots has come to a halt together in a loose line in the middle of the slope, still well below and far from the bunker, turrets level and facing up the hill toward it. The chalk dust they were kicking up rolls on past them and drifts up the slope to the right, thinning out. The tops of out-of-focus long grass blur across the very bottom of frame. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

## sd-05  (candidate p5-a)

**Idea:** Over the hull, tracks dug in at the end of short skid marks, turf piled up ahead, door far (asked for a higher sensor-mast view; came back at V4 height).

**References:** v4-frame0.jpg, wa-02.png, P1-patrol-blockbuster.jpg

```prompt
Using the first image for the robot's own point of view (its armoured grey hull and two rubber tracks at the bottom of frame, seen from just behind its sensor) and for the bunker entrance with its green blast doors, the second image for the long grassy chalk down, the overcast light and how far off the bunker is, and the third image for the tracked robot's design: a higher view from the top of the robot's sensor mast, looking forward and down over the whole front of its hull and both tracks to the slope ahead. The robot has stopped dead on the open hillside: its tracks are buried a hand deep at the end of two short skid marks in the chalk, the turf piled up in front of them. The long grassy slope climbs away for a long distance to the bunker entrance, small and grey with its shut green doors, just right of centre near the skyline. A curtain of chalk dust from the hard stop drifts forward over the hull and on up the slope. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

## sd-06  (candidate p6-a)

**Idea:** Low corner camera: one track ground to a stop in a chalk gouge, door small in the distance.

**References:** v4-frame0.jpg, wa-02.png, P1-patrol-blockbuster.jpg

```prompt
Using the first image for the robot's rubber track, the bunker entrance with its green blast doors and the film look, the second image for the long grassy chalk down, the overcast light and how far off the bunker is, and the third image for the tracked robot's design: a low camera mounted at the robot's front corner, a hand's height above the turf. The heavy rubber track fills the left edge of the frame in sharp close-up, motionless, chalk and grass jammed in its treads, where it has just ground to a stop in a short gouge of white chalk. Dust and torn grass are still settling in the air. Far away up the long slope, small and in the middle of the frame, the concrete bunker entrance with its shut green doors on the skyline. Shallow focus on the track, the distance soft. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

