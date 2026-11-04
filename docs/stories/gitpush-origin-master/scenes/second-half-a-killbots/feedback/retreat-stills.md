# Retreat stills (scene A, beat 12, after the stand-down) — 2026-11-03

Kai's note on cut3-V10r (verbatim): *"This shot is just a bit rubbish and in terms of animated and also they're all too close to the door now we've done the stand down shift is much further away. So if we look at the previous scene, we're much further away from the door than we then animate them retreating. So I think we need a much wider shot of the tanks turning around and retreating. And, you know, the cinematography the animation is a bit wooden so it feels like we could do this in a slightly better way."*

The cut runs cut3-WA02 (the wide approach) → hud-12 over cut3-SD01 (braked dead halfway up the slope, STAND DOWN) → **this shot** (replacing cut3-V10r) → V3, Maddie: "That was close." These options keep the pack where SD01 left it, halfway up and well short of the door, and catch the turn beginning (bots at different angles, chalk scuffs) so a Veo/Omni animation has a turn to finish. Variable tested: the camera position (ridge-high wide, low long lens, aerial, wa-02's own camera, extreme wide from across the valley, the doorway).

Stills only, no video credit spent; Kai picks first. Files: `D:\badcode-videos\gitpush-origin-master\clips\second-half\stills\retreat\rt-NN.png` (sheet: `rt-sheet.jpg`; both candidates per option in `work/`). Model Nano Banana Pro, 16:9, Flow project f96cac0e, via flow_edit_image. References for every option, in order: `stills/wide-approach/wa-02.png`, `stills/stand-down/sd-01.png`, `moodboard/P1-patrol-blockbuster.jpg` (the canonical kill bot).

Same-prompt check: fresh.py flagged a 41-word near copy with the stand-down stills in every prompt; that is the story's locked 16mm and 16:9 suffix, kept on purpose. The reference-role opening clause is shared across rt-01/02/03/05 (and nearly rt-06), also on purpose.

## rt-01  (candidate p1-a)

**Idea:** High wide from the ridge beside the bunker looking down the slope: pack halfway down, one bot mid-pivot in a chalk crescent, two still facing uphill; door small top right.

```prompt
Using the first image for the chalk down, the grey light and the film look, the second image for the concrete bunker entrance with its shut green doors and how far down the slope the robots stopped, and the third image for the tracked robot's design: a high, wide view from up on the ridge beside the bunker, looking down and across the whole long slope. In the near corner of the frame, the turfed concrete shoulder of the bunker and a leaning fence post, the green doors just visible and small at the far right edge. Far below, halfway down the hillside, five tracked robots like the one in the third image are wheeling round where they stopped: two are already side-on and pointing back downhill, one is mid-pivot with a crescent of torn turf and white chalk under its tracks, the last two still face up the hill. A long empty stretch of grass lies between them and the doors. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

## rt-02  (candidate p2-a)

**Idea:** Low long lens from the grass at the foot of the down: the pack mid-turn coming back toward us, nearest bot swung about; door a notch on the skyline.

```prompt
Using the first image for the chalk down, the grey light and the film look, the second image for the concrete bunker entrance with its shut green doors and how far down the slope the robots stopped, and the third image for the tracked robot's design: a very low camera hidden in long grass at the foot of the down, a long telephoto lens looking straight up the slope, out-of-focus seed heads blurring across the bottom third. Halfway up the hill, five tracked robots like the one in the third image are turning round to come back down toward us: the nearest has swung fully about and its blunt nose faces the camera, the others are caught at different angles of the turn, tracks skewed, throwing small sprays of turf. Behind and far above them, the bunker entrance is a small grey notch on the skyline with its shut green doors, a great distance away. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

## rt-03  (candidate p3-a)

**Idea:** Steep aerial, reconnaissance-photo: five hairpin chalk scars where the pack pivoted at the halfway point, two bots already crawling away; door tiny at the top edge.

```prompt
Using the first image for the chalk down, the grey light and the film look, the second image for the concrete bunker entrance with its shut green doors and how far down the slope the robots stopped, and the third image for the tracked robot's design: an aerial view from high above the down, looking steeply down at the hillside like a reconnaissance photograph. The bunker entrance is a tiny concrete notch near the top edge of the frame. In the middle of the green slope, far below it, five small tracked robots like the one in the third image have stopped in a ragged line and are turning back: each has carved a pale curved scar of bare white chalk through the turf where it pivoted, the scars looping round like hairpins, two robots already crawling away downhill at the open end of their loops. Faint straight tread lines lead up the slope to the turning point and stop there. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

## rt-04  (candidate p4-a)

**Idea:** wa-02's own side-on long lens through the grass, later: the pack stalled halfway up, wheeling back down-left; door high right.

```prompt
Using the first image exactly for the camera position, the long-lens compression, the foreground grass and the concrete bunker entrance high on the upper right with its shut green doors, the second image for how far up the slope the robots stopped, and the third image for the tracked robot's design: the same far-off side-on view through the grass, later. The pack of five robots is no longer at the foot of the slope but stalled halfway up it, well below the bunker, and is wheeling round in a ragged line: the lead robot has turned through half a circle and points back down and to the left, the others are swinging round behind it at different angles, tracks skidding sideways and scuffing up chalk. A thin haze of dust hangs over them and drifts uphill toward the doors. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

## rt-05  (candidate p5-b)

**Idea:** Extreme wide from a neighbouring hill over a fence post and wire: the tiny pack fanning out and rolling back down the slope; door a speck near the crest.

```prompt
Using the first image for the chalk down, the grey light and the film look, the second image for the concrete bunker entrance with its shut green doors and how far down the slope the robots stopped, and the third image for the tracked robot's design: an extreme wide landscape from a neighbouring hill across a shallow valley, the whole down laid out under a huge low sky that fills the top half of the frame. In the foreground, a weathered fence post with a strand of rusted wire and a few tufts of sheep-cropped turf, sharp. Across the valley, the bunker entrance is a speck of grey concrete with shut green doors near the crest, and halfway down the long slope beneath it five tiny tracked robots like the one in the third image are breaking out of their line and swinging round to head back down, small pale streaks of chalk dust lifting where they turn. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

## rt-06  (candidate p6-a)

**Idea:** From the bunker doorway, long lens down the slope: the pack's backs as it files away downhill, the rearmost still slewing round in a curl of chalk.

```prompt
Using the first image for the chalk down, the grey light and the film look, the second image for the bunker's concrete and green blast doors and how far down the slope the robots stopped, and the third image for the tracked robot's design: the view from the bunker doorway itself, a long lens looking straight down the long slope. The rough edge of the concrete apron and a sliver of a green steel door frame the left edge of the shot, soft and close. Far down the hill, five tracked robots like the one in the third image have turned their backs on us and are rolling away downhill in a loose file, small and getting smaller, the rearmost still slewing round, its tracks gouging a white curl of chalk. Nothing but grass between us and them. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

---

# rt-01c: re-sealing rt-01b so the turn has already happened (2026-11-03)

**Why:** Kai picked rt-01. Its cleaned plate rt-01b was animated 4 times with Omni Flash, and every take drove the pack RIGHT, toward the door. The plate's bots have their noses pointing right, and Omni carries on with whatever heading a bot already has; it won't turn one round (`docs/google-flow/README.md`: "continue a state the first frame already shows"). So these stills re-seal the plate with every nose already down-left, toward the valley, plus fresh chalk scuffs and dust drifting up and right (where the bots came from).

Stills only, no video credit. One flow_edit_image call per option off `rt-01b.png` (not chained), with `moodboard/P1-patrol-blockbuster.jpg` as the second reference; Nano Banana Pro, 16:9, Flow project f96cac0e, channel 3. Files: `rt-01c-1.png` .. `rt-01c-3.png`, sheet `rt-01c-sheet.jpg` (rt-01b plus the three options), every candidate in `work/rt-01c-*`. **Quirk:** three calls returned an extra tile that was really one of the uploaded references (`rt-01c-1-a` = P1, `rt-01c-2r-a` and `rt-01c-3-a` = rt-01b, which diffs under 1 against the plate). Their cards are marked NOT A GENERATION.

Same-prompt check: fresh.py flagged the keep-everything-else tail as a 28-word near copy of the rt-01b turf edit. That is kept on purpose, because this is an edit of the same plate. The re-rolls share their reference and keep-clauses with each other, also on purpose.

## rt-01c-1 (candidate rt-01c-1-c): all four turned, spaced out

```prompt
Using the first image as the scene and the second image for the tracked robot's design, change only the four tracked robots: they have all finished turning round and are now rolling away down the hill, every robot's blunt nose and gun pointing down and to the left toward the valley in the lower left corner, their backs to the green doors at the top right. Spread them out in a loose, well-spaced line across the lower left of the slope, exactly four robots, no more. Under each one, a fresh curved scuff of bare white chalk and torn turf where its tracks pivoted, and a thin trail of pale dust drifting up and to the right behind them, back toward where they came from. Keep everything else in the image exactly the same: the high camera on the ridge, the long slope, the turf edge in the lower right, the bunker with its green doors small at the top right, the grey overcast light and the faded 16mm film grain, preserving the original style, lighting and composition.
```

## rt-01c-2 (candidate rt-01c-2r-b, from the re-roll): three turned, one finishing its pivot

First try (`work/rt-01c-2-a/b`) rejected: in a, the pack moved up toward the door; in b, the two left bots' guns pointed right. Re-rolled with each bot's position named and the guns explicit:

```prompt
Edit the first picture; the second picture shows what each tracked robot looks like. Turn the robots round so the pack is leaving: the two robots on the far left of the slope and the one beside the chalk ring now face away from the bunker, hull front, turret and gun barrel all aimed down-left toward the bottom left corner of the frame, rolling off downhill. The last robot, the one inside the white chalk crescent, is caught mid-pivot, three quarters of the way round, its front swinging down-left to join them, tracks tearing up white chalk and throwing a puff of dust. Four robots in total, all staying roughly where they are now, well below the doors. Behind each one a fresh pale scuff in the turf, and a faint haze drifting uphill and rightward where they came from. The rest of the picture does not change: same high viewpoint on the ridge, same hillside, same grassy edge bottom right, same small green bunker doors top right, same flat grey daylight and grainy faded 16mm texture.
```

## rt-01c-3 (candidate rt-01c-3r-a, from the re-roll): bunched, more dust

First try (`work/rt-01c-3-b/c`) rejected: only three bots visible, and in b the camera drifted. Re-rolled as a two-by-two block with "each one fully visible" and the camera pinned:

```prompt
Edit the first picture; the second picture shows what each tracked robot looks like. The pack has wheeled about and is pulling away bunched close together in a tight two-by-two block, four separate robots, each one fully visible with clear grass between them, hull fronts, turrets and gun barrels all aimed down-left toward the bottom left corner of the frame, the bunker at their backs. They sit on the left half of the slope roughly where they are now, well below the doors. The grass round them is ripped into overlapping loops of bare white chalk where they spun, and a big billow of pale chalk dust rolls off behind them, up and to the right, over the ground they just left. Leave the camera exactly as it is, the same high wide view from the ridge with the whole hillside, the grassy edge in the bottom right corner and the small green bunker doors fully in frame at the top right, in the same flat grey daylight and grainy faded 16mm texture.
```
