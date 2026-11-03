# A · Kill bots: the wide approach (still options, 2 Nov 2026)

**Why:** Kai's note on the timeline, 2 Nov: the kill bots get far too close to the door in the close race
(`cut3-V9`, from `S4r-a`). He wants a much wider, zoomed-out shot of them racing at the bunker door from a long way off, still urgent, and
then the cut to the stand-down. The same shot may also serve `maddie-at-door` as the film the humans watch, so
some options are the kill bot's own view (POV).

**Stills only. No video was made.** Kai approves a plate before any video credit is spent.

- **Made:** 2 Nov 2026, a fresh Flow project `f96cac0e-9d56-43e0-aade-89f87deea2b8` ("Nov 02 - 16:20"),
  `flow_edit_image`, default model (Nano Banana Pro, 0 credits), 16:9, 2 candidates a call. No Character cast
  (same as cut 3: the place and the bots come from reference images).
- **References** (copied into the WSL filesystem before upload, per flow-automation law 20):
  - **Hillside, door, film look:** `clips/second-half/storyboard/cut3/S4r-a.jpg` (the still behind V9, the very
    shot this replaces, so it is the same place); `storyboard/cut3/S10-c.jpg` for option 6 (the door from above).
  - **Kill bots:** `clips/second-half/moodboard/P1-patrol-blockbuster.jpg` (the canonical reference, look.md §Cast).
  - **POV hull:** `clips/second-half/storyboard/cut3/S5-a.jpg` (the still behind V4, the on-board shot at the door).
- **Media:** `/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/stills/wide-approach/`: `wa-01.png` … `wa-06.png`,
  `wa-sheet.jpg` (numbered contact sheet), and every raw candidate in `work/p<n>-<a|b|c>.jpg`. Each still has its recipe card
  beside it and under `docs/provenance/cards/gitpush-origin-master/clips/second-half/stills/wide-approach/`.
- **Look:** A's exterior carries the 16mm suffix like S4r-a/S10, plus the house suffix (look.md, second-half suffixes).
- **Same-prompt check** (`scripts/variations/fresh.py`, also run by the hook): the only repeats flagged were the two
  suffixes above (the story's agreed second-half suffixes, kept on purpose) and stock phrases ("the top of the"). No body
  was a copy of an earlier prompt.

## The options

| Still | From | What it is | For |
| --- | --- | --- | --- |
| `wa-01` | `work/p1-b` | Very high aerial over the valley: five bots small at bottom left with long chalk-dust trails, the door small at upper right, a huge empty slope between | **A** (the clearest "a long way to go") |
| `wa-02` | `work/p2-b` | Long lens from far off to the side through blurred grass: the pack small and side-on along the foot of the slope in dust, the door a small notch high right | **A** |
| `wa-03` | `work/p3-b` | V9's own framing (low in the grass) pulled back: door smaller, pack mid-distance. Only a modest pull-back, but it cuts straight into V9 as "earlier in the same race" | **A** (the safe match) |
| `wa-04` | `work/p4-b` | **POV** from the kill bot's nose (S5-a's hull and tracks), racing across the down, door far on the hill, two bots alongside in dust | **Both**: POV film for the humans, and the on-board shot before V4's brake |
| `wa-05` | `work/p5-b` | **On board**, just behind and above the P1 turret, door far ahead, other bots' dust either side | **Both** (chase-cam rather than true POV) |
| `wa-06` | `work/p6-b` | From the parapet above the door, looking down the valley: the pack small and far off, racing up at us. The door itself isn't in frame (we're on top of it) | **Both**: reads as the bunker's security camera, so it suits the film the humans watch; for A it shows the distance from the door's side |

**Recommendation:** `wa-01` for A's wide shot (the distance is clearest and it's still plainly the same door and the same
bots), and `wa-04` for the POV film (it matches V4's hull, so the same POV can carry on into V4's brake and stand-down).

**Spares in `work/`:** `p1-a` (the aerial again, pack bunched lower left), `p4-c` (POV, the door a little closer),
`p6-c` (the parapet view, pack nearer and head-on).
**Rejects:** `p2-a` (bots face the camera, so they seem to drive away from the door), `p3-a` (as close as S4r-a: no
change), `p5-a` (door too close). **Duds:** `p4-a` (a copy of S4r-a) and `p6-a` (a copy of P1). Each came back as a
third candidate from a two-candidate call, the known one-in-three "reference copied back unchanged" fault
(second-half-cut3-shots.md). Nothing was policy-blocked.

**For animating later (not done):** the bots must keep the P1 shape across the move; on wa-01/02/06 only the bots and
dust move, so lock the camera and let Premiere do any push. wa-04/05 need Veo to move the world past a hull that stays
fixed.

## Prompts (exact, as sent)

Reference order is as listed for each prompt.

**Option 1 (wa-01), references S4r-a + P1-patrol-blockbuster:**

> Using the first image for the hillside, the concrete bunker entrance with its green blast doors and the film look, and the second image for the tracked military robots: a very high aerial shot looking down across a broad Wiltshire valley of rough pale grass. The bunker entrance from the first image is small, set into the green chalk down in the upper right of frame, its green doors shut. Far below it, in the lower left, a pack of five tiny tracked military robots like the one in the second image tears across the open valley floor in a loose line, each dragging a long white trail of chalk dust behind it. Between the pack and the door lies a huge empty stretch of grass and a rising slope: they still have a long way to go. Overcast grey daylight, flat light, no sun. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.

**Option 2 (wa-02), references S4r-a + P1-patrol-blockbuster:**

> Using the first image for the hillside, the bunker entrance with its green blast doors and the film look, and the second image for the tracked military robots: a long-lens shot from far off to the side, the distance compressed, heat shimmer and hanging dust softening the middle ground. A pack of five tracked military robots like the one in the second image crosses the frame from left to right at full speed along the bottom of a long grassy slope, side-on and small, their tracks throwing up chalk. High above them and far beyond, near the top of the down in the upper right, the concrete bunker entrance is a small grey notch with its shut green doors. The tops of out-of-focus long grass blur across the very bottom of frame. Overcast grey sky. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.

**Option 3 (wa-03), references S4r-a + P1-patrol-blockbuster:**

> Using the first image for the low camera in the long grass, the hillside, the bunker entrance and the film look, and the second image for the tracked military robots: the same place as the first image but seen from much further back down the hill. The camera sits low in long, wind-bent grass at the foot of a wide open down. A pack of four tracked military robots like the one in the second image races away from camera up the long empty slope, small in the middle of frame, long trails of dust streaming back towards us. At the very top of the down, far away and tiny against the grey sky, the concrete bunker entrance with its shut green blast doors. Most of the frame is open grassland and sky. The grass before the doors is clean, nothing burnt or wrecked. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.

**Option 4 (wa-04, POV), references S5-a + S4r-a:**

> Using the first image for the robot's own point of view, its angular armoured nose and the tops of its tracks in the bottom of frame, and the second image for the hillside and the bunker entrance: in natural colour, not red, the camera fixed low on the front of a tracked military robot racing at full speed across a wide open down. The bunker from the second image is far away, a small grey concrete notch with green doors near the top of the hill on the horizon, with a long empty slope of grass between it and us. Two more of the robots race alongside, small to the left and right, dragging dust. Grass and chalk streak past the lens with motion blur at the frame edges. Overcast grey daylight. A clean picture with no interface, no overlay, no tint. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.

**Option 5 (wa-05, on board), references P1-patrol-blockbuster + S4r-a:**

> Using the first image for the tracked military robot and its sensor turret, and the second image for the hillside, the bunker entrance and the film look: the view from high on the robot's own sensor turret, looking forward over its long armoured hull as it charges across open grassland. The hull and the back of the turret fill the bottom quarter of the frame, slightly out of focus. Far ahead, small and centred on the side of a green chalk down, the concrete bunker entrance with its shut green blast doors. A wide sweep of rough grass and a dusty track lie between. Dust boils up at the sides, the whole frame rattles with speed. Overcast grey daylight. A clean picture with no interface, no overlay, no tint. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.

**Option 6 (wa-06, from above the door), references S10-c + P1-patrol-blockbuster:**

> Using the first image for the concrete bunker entrance, its green blast doors and the grassy down, and the second image for the tracked military robots: a high, fixed security-camera view from the top of the bunker entrance, looking down and out over the long grassy slope in front of the doors and the wide valley beyond. The edge of the concrete parapet and a few weeds sit in the bottom of frame. Far away down in the valley, small, a pack of five tracked military robots like the one in the second image is racing up towards the bunker, each pulling a long trail of chalk dust, with a long empty stretch of grass still between them and the doors. Overcast grey daylight, slightly washed out. Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain. 16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.


## Video: wa-02 animated (2 Nov 2026)

Kai picked **wa-02** for A's wide approach (goes before the close race `cut3-V9` and the on-board stand-down `cut3-V4`).
Job: the pack races at the door, urgent, but stays far from it for the whole clip; never reaches it, reverses or turns.

- **How:** Flow project `f96cac0e` (where the still was made), **Omni 1.1 Flash, Frames, start frame only, 16:9, 6 s, count 1**,
  through the cut-3 runner's code (`scripts/gpom/second-half-video/run-cut3.mts`, run from a temporary copy pointed at this
  project, then deleted; jobs in `run-cut3.log`, spend in `run-cut3.ledger.json`). Price read before each Create: 10 credits a clip.
  **Spend: 20 credits** (balance 12,145 → 12,125). Each harvest md5-checked against every clip on disk (both new) and
  first-frame-matched to wa-02 (distance 17 for both; correct < 400).
- **Same-prompt check:** only habit phrases flagged: the lock line "The camera does not move." and the 24fps/180-degree shutter
  clause (take 1), both kept on purpose as proven mechanics, plus stock phrases ("the foot of the"). Neither body copies an earlier prompt.

| Clip | Motion prompt | Verdict |
| --- | --- | --- |
| `video/cut3-raw/cut3-WA02-r1-reject.mp4` | *The camera does not move, locked on a long lens from far off. The pack of tracked military robots races from left to right along the foot of the slope at full speed, tracks churning, thick chalk dust boiling up and drifting back behind them. They stay low on the slope, far below the small shut green doors high on the right. The long grass in the foreground whips in the wind. Shot at 24fps with a 180-degree shutter, so the speed smears. The camera does not move.* | **Reject.** Camera locked and the door never reached, but the bots **morph** from the P1 shape (boxy sensor head) into cannon-barrelled tanks by ~1.5 s, a big extra tank drives in from the left edge near camera, and by 5 s the dust swallows the whole pack |
| **`video/cut3-WA02.mp4`** (6.0 s, audio stripped; raw with audio `cut3-raw/cut3-WA02-r2-raw.mp4`) | *The camera does not move, locked on a distant long lens. The same five squat tracked robots, each topped by a boxy camera-sensor head, race side-on left to right along the foot of the slope at full speed, staying small and far away. Their tracks kick up long low trails of chalk dust that stream out behind them. The shut green doors stay high and distant on the hilltop. Foreground grass sways. The camera does not move.* | **Keeper.** Camera locked. The column of P1-shaped bots runs left to right along the foot of the slope in long low chalk-dust trails, staying small; the lead bot only creeps right under the door, which stays a small notch high on the right all clip. A sixth bot of the same shape joins at the left edge at ~1.75 s as the tail of the column (nearer, so bigger). No morph, no reversal, no merge. Naming the sensor head held the shape. The long lens makes the advance read slower than the dust says: Premiere can add a slow push if it needs more urgency |

Contact sheet: `video/cut3-WA02-sheet.jpg`. Recipe cards beside each file and under `docs/provenance/cards/…/second-half/video/`.
Not placed in Premiere, not added to `cut3.py` or `scene.json`.
