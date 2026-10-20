# GPOM second half, cut 3: still options S1–S8

The new pictures that Kai's round 1 and 2 notes on the cut 2 timeline need
([`second-half-cut2-notes.json`](./second-half-cut2-notes.json): beats 9, 10b, 11, 12, 14a and 17). These are
**options for Kai to pick from**: 3–4 stills per shot. No video was made.

- **Made:** 20 Oct 2026, Flow project `be451638` (the second-half project), `flow_edit_image`, default model
  (Nano Banana Pro, 0 credits on this account), 16:9, 2 candidates per prompt. No Character was cast: N4 round 1
  showed the West Country Bot Character drags its high street into other places, so the place came from a
  reference image instead.
- **References** (copied into the WSL filesystem before upload, per flow-automation law 20):
  - **Maddie** in every shot she's in: `clips/simulation/stills/s3/s3-bot-00b-a.jpg`. The torn bunting is named in every prompt.
  - **Kill bots:** `moodboard/P1-patrol-blockbuster.jpg` (the tracked robot with the sensor turret, used in cut 2 and the
    patrol shots). **POV hull:** `moodboard/K5-pov-red-race.jpg`.
  - **Bunker exterior:** `storyboard/SB12c.jpg`, with its wrecks and smoke written out ("nothing burnt or wrecked").
    **Downs:** `moodboard/K9-downs-aerial.jpg`.
  - **Old lady:** `storyboard/cut2/N4r2-b.jpg` (+ `moodboard/M3-old-lady-blockbuster.jpg` on S7-p2).
    **Inside the bunker:** `storyboard/SBHELLOa.jpg`, `SBHELLOb.jpg`, `moodboard/B1-lived-tunnel-threads.jpg`.
- **Media:** `/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/storyboard/cut3/`, with options
  `S<n>-a…d.jpg`, a `S<n>-sheet.jpg` contact sheet per shot, and `manifest.json` (shot, beat, brief, and each option's
  file, prompt, references and note). Every raw candidate is in `cut3/work/` as `S<n>-p<prompt>-<a|b|c>.jpg`.

`{house}` = *"16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering
or on-screen text."* `{16mm}` = *"Styled as a 1980s British television drama shot on 16mm film: faded colour, soft
contrast, heavy grain."* (the same suffixes as cut 2). The bunker exterior shots carry `{16mm}` because SB12c and N2
do. S7 keeps N4's anamorphic look.

## 🔴 Found on this run: a one-reference edit returns an unchanged copy

A `flow_edit_image` with a **single** reference image (the bot alone) often came back with **three** candidates
instead of two. The extra one, always `-a`, was the reference picture almost unchanged, with the prompt ignored
(`S2-p2-a`, `S2-p3-a`, `S3-p1-a`, `S3-p2-a`). It happened once with two references as well (`S5-p1-a` is SB12c
again, wrecks and all). These are not late tiles from the batch before: each matches its own reference, and the files
after it are correct. **Look at every candidate: a three-candidate result from a two-candidate call has a dud in it.**
(Seen 5 times in 20 calls, n=1 session; not yet in the flow-automation skill's laws.)

## S1: beat 9a, The kill bot tears past Maddie

**Brief:** High camera steeply down onto the empty high street from beat 0; Maddie small mid-road; ONE kill bot bursting in at speed the moment before it swerves round her; dust.

**S1-p1, references s3-bot-00b-a + P1-patrol-blockbuster:**

> Using the first image for the place and the small robot, and the second image for the tracked military robot: a high camera looking steeply down from a first-floor window onto the same empty, ruined English high street, red-brick shops with broken windows, weeds in the cracked road, the church tower in the distance. In the middle of the road below, small in frame, the grey six-wheeled delivery robot from the first image trundles along, its amber beacon lit and its torn, faded cloth bunting hanging across its front wheels. From the bottom edge of frame one tracked military robot from the second image bursts in at speed, angled to swerve past it, a thick plume of dust and grit kicking up from its tracks. Overcast grey daylight. {house}

**S1-p2, references s3-bot-00b-a + P1-patrol-blockbuster:**

> Using the first image for the place and the small robot, and the second image for the tracked military robot: a very high, steep top-down angle from a rooftop, looking almost straight down onto the same empty English high street, cracked tarmac, faded road markings, weeds and rubble along the kerbs. The grey six-wheeled delivery robot from the first image is small in the middle of the road, its amber beacon lit and its torn, faded cloth bunting trailing across its front wheels. Entering fast from the left edge of frame, a single tracked military robot from the second image tears down the road towards it, motion-blurred, already angling to swerve round it, a long rooster tail of dust and grit thrown up behind its tracks. No other vehicles. Overcast grey daylight, long soft shadows. {house}

| Option | From | Note |
| --- | --- | --- |
| `S1-a` | `work/S1-p1-a` | Window-high, the bot bursts in from bottom right. Window-frame edges in frame (crop in post) and the reference's burnt wreck sits far down the street. |
| `S1-b` | `work/S1-p1-b` | Same set-up; bot fills more of the right side, more dust. Window frame and the far wreck as in a. |
| `S1-c` | `work/S1-p2-a` | Rooftop, near top-down. The kill bot cuts in from the left with a long dust tail; Maddie mid-road, bunting visible at full size. The steep angle the brief asks for. |
| `S1-d` | `work/S1-p2-b` | Same as c, the bot closer to her and the dust tail longer; a near miss. |

## S2: beat 9b, Whoa: Maddie in the dust

**Brief:** Maddie close-up in a settling cloud of dust just after the kill bot tore past, bunting flapping, a startled 'whoa' through lamp and posture.

**S2-p1, references s3-bot-00b-a:**

> Using the provided image for the robot and the street: a close shot at ground level of the same grey six-wheeled delivery robot, filling the right half of frame, engulfed in a thick cloud of dust and grit that is just beginning to settle after something tore past. Its torn, faded cloth bunting is blown sideways and flapping across its front wheels. Its body is tipped back slightly on its rear wheels and turned a little away, as if it flinched, and its amber beacon flares bright through the haze. Fine grit hangs in the air, catching the light. The ruined high street behind is soft and half hidden by the dust. Overcast grey daylight. {house}

**S2-p2, references s3-bot-00b-a:**

> Using the provided image for the robot and the street: a low, tight close-up of the front of the same grey six-wheeled delivery robot, camera at wheel height just in front of it, the robot's front corner and amber beacon filling the frame. A swirling cloud of dust is settling all around it after something raced past; grit pattering onto its scuffed lid. Its torn, faded cloth bunting flutters hard in the wind of the passing, one strip lifted into the air. The beacon blinks bright and startled through the dust. Deep in the soft background, a dust trail disappears down the ruined high street. Overcast grey daylight. {house}

**S2-p3, references s3-bot-00b-a:**

> Using the provided image, change only the moment: a thick, swirling cloud of grey-brown dust and grit now engulfs the same grey six-wheeled delivery robot and the road around it, settling after something tore past close by, and the camera is a little closer and lower. The robot is caught mid-flinch, its body rocked back on its rear wheels with its front wheels just lifting off the road, its amber beacon flaring bright through the haze. Its torn, faded cloth bunting stays where it is, hanging across its front wheels, and flaps hard in the passing wind. Grit pings off its lid. The street behind is half lost in dust. Keep the robot's shape, scuffs, beacon and bunting exactly the same, preserving the original style and lighting. {house}

| Option | From | Note |
| --- | --- | --- |
| `S2-a` | `work/S2-p1-a` | Low, three-quarter rear; dust cloud on the left, the beacon flaring. Bunting intact. |
| `S2-b` | `work/S2-p1-b` | Front three-quarter, bunting blown out and flapping, grit in the air. |
| `S2-c` | `work/S2-p3-b` | Original framing, dust engulfing her, grit flying off the lid. Reads as aftermath. |
| `S2-d` | `work/S2-p3-c` | Front wheels lifted off the road, rocked back: the flinch. The clearest 'whoa'. |

## S3: beat 11, The boss hotline

**Brief:** Close-up of the top of Maddie: a small hatch flipped open and a little special antenna extending, a tiny light on its tip.

**S3-p1, references s3-bot-00b-a:**

> Using the provided image for the robot: an extreme close-up of the top of the same grey delivery robot's scuffed metal lid, beside its amber beacon. A small square hatch in the lid has flipped open on a hinge, and out of it a slim, telescopic antenna is extending upward, a little spring-loaded aerial with a tiny glowing blue light on its tip. Fun, small, precise, like a gadget popping out. The ruined high street behind is a soft blur. Overcast grey daylight, shallow depth of field. {house}

**S3-p2, references s3-bot-00b-a:**

> Using the provided image for the robot: a close, slightly high three-quarter shot of the front top corner of the same grey delivery robot, its amber beacon glowing. Just behind the beacon, a little round hatch in the scuffed metal lid has popped open, its lid flipped back on a hinge, and a thin chrome telescopic antenna has sprung up out of it, three segments extended, a tiny red light glowing on its tip, the antenna still wobbling from the pop. A strip of the robot's torn, faded cloth bunting is just visible at the bottom edge of frame. The ruined high street behind is a soft blur. Overcast grey daylight, shallow depth of field. {house}

**S3-p3, references s3-bot-00b-a:**

> Using the provided image for the robot: a low close-up looking slightly up at the top of the same grey delivery robot's scuffed metal lid against the grey sky, its amber beacon glowing at one side. A small square hatch in the lid has just flipped open, and a short, springy chrome antenna with a little ball tip has popped up out of it, a tiny green light glowing on the tip, the antenna still quivering. Small, neat, a bit comical. The ruined high street's rooftops and church tower are a soft blur behind. Overcast grey daylight, shallow depth of field. {house}

| Option | From | Note |
| --- | --- | --- |
| `S3-a` | `work/S3-p1-b` | Square hatch, telescopic aerial with a blue tip light, beacon beside it. Very close; the street is a soft blur. |
| `S3-b` | `work/S3-p1-c` | Same idea, wider, the church tower behind; a little spring visible at the antenna's base. Blue tip. |
| `S3-c` | `work/S3-p2-b` | Round flip lid, chrome three-section aerial with a red tip; a strip of bunting along the bottom edge ties it to Maddie. |
| `S3-d` | `work/S3-p3-b` | Low angle against the sky, square hatch, a short springy antenna with a green tip. The most comical one. |

## S4: beat 10b, The pack closes on the door

**Brief:** The kill-bot pack racing up the chalk downs, close to the bunker; the blast door near and large ahead; low angle, dust trails, menace.

**S4-p1, references P1-patrol-blockbuster + SB12c + K9-downs-aerial:**

> Using the first image for the tracked military robots, the second image for the bunker entrance and the third for the chalk downs: a low-angle shot from the grass, close behind a pack of five tracked military robots like the one in the first image as they race up the steep grassy slope of the downs, thick dust trails boiling up behind their tracks. Close ahead of them, large in frame and set into the hillside, the concrete Cold War bunker entrance from the second image, its heavy green steel blast doors shut. The grass in front of the doors is clean and unburnt, nothing wrecked. Overcast grey sky, menace, speed. {16mm} {house}

**S4-p2, references P1-patrol-blockbuster + SB12c:**

> Using the first image for the tracked military robots and the second image for the bunker entrance: the camera low in the long grass right behind the last of a pack of tracked military robots like the one in the first image, its tracks and rear hull huge and close in the foreground, racing away up a steep chalk hillside, with three more of them ahead throwing up long trails of dust and chalk. Not far ahead, the concrete Cold War bunker entrance from the second image looms large over the pack, set into the grassy hill, its heavy green steel blast doors shut. The ground in front of the doors is clean grass, nothing burnt or wrecked. Overcast grey sky, menace, speed, motion blur on the grass. {16mm} {house}

**S4-p3, references P1-patrol-blockbuster + SB12c:**

> Using the first image for the tracked military robots and the second image for the bunker entrance: a low-angle shot from the grass at the side of a chalk track on the steep downs, as a pack of four tracked military robots like the one in the first image thunders past close to camera, one after another, heading up the hill towards the concrete Cold War bunker entrance from the second image, which is near now and large in the upper half of frame, its heavy green steel blast doors shut. The nearest robot is huge and partly cut off by the frame edge, its tracks churning chalk and dust; dust trails hang in the air behind the pack. The ground before the doors is clean grass, nothing burnt or wrecked. Overcast grey sky, menace. {16mm} {house}

| Option | From | Note |
| --- | --- | --- |
| `S4-a` | `work/S4-p1-a` | Side-on, the pack climbing the slope in a line towards the door; the bunker is upper right. |
| `S4-b` | `work/S4-p1-b` | Head-on to the door, bots spread across the slope in front of it. Less low. |
| `S4-c` | `work/S4-p2-a` | Ground level, one kill bot huge in the right foreground, three ahead trailing dust towards the door. The most menace. |
| `S4-d` | `work/S4-p3-b` | Low, a column of four on a chalk track up to the doors, the nearest cut by the left edge. Clean kill-bot design. |

## S5: beat 12, The kill bot's eye

**Brief:** The kill bot's own POV, camera low on its chassis, racing straight at the blast door; motion, dust; CLEAN plate (HUD added in ffmpeg).

**S5-p1, references K5-pov-red-race + SB12c:**

> Using the first image for the robot's own point of view and its armoured front hull, and the second image for the bunker entrance: in natural colour, not red, the camera mounted low on the front of a tracked military robot, its angular armoured nose and the tops of its tracks in the bottom of frame, racing straight up a grassy track towards the concrete Cold War bunker entrance from the second image. The heavy green steel blast doors fill most of the frame ahead, close now, set into the grassy hillside. Dust and grit fly up past the lens, the grass streaks with motion blur at the edges. The grass before the doors is clean, nothing burnt or wrecked. Overcast grey daylight. A clean picture with no interface, no overlay, no tint. {house}

**S5-p2, references K5-pov-red-race + SB12c:**

> Using the first image for the robot's own point of view and its armoured front hull, and the second image for the bunker's blast doors: in natural colour, not red, the camera low on the front of a tracked military robot charging at full speed, only metres from the bunker. The heavy green steel blast doors from the second image fill the whole frame ahead, edge to edge, their rivets, scratches and moss sharp, the concrete surround cut off at the frame edges. Its angular armoured nose and the tops of its tracks are in the bottom of frame, flinging up grass, dust and chalk that streak past the lens. Strong motion blur at the edges of frame. Overcast grey daylight. A clean picture with no interface, no overlay, no tint. {house}

| Option | From | Note |
| --- | --- | --- |
| `S5-a` | `work/S5-p1-b` | Armoured nose and tracks at the bottom, the whole bunker ahead with grass to either side. Strong motion blur. |
| `S5-b` | `work/S5-p1-c` | Same, a little closer, the doors larger. |
| `S5-c` | `work/S5-p2-a` | Metres away, the doors fill the frame, debris flying. Green hull, matching K5. |
| `S5-d` | `work/S5-p2-b` | Same as c, but the hull is a muddier brown that matches K5's hull less well. |

## S6: beat 14a, Maddie at the closed door

**Brief:** Maddie stopped in front of the plain closed bunker blast door in the hillside. No wreckage, no smoke. Quiet.

**S6-p1, references s3-bot-00b-a + SB12c:**

> Using the first image for the small robot and the second image for the bunker entrance: the grey six-wheeled delivery robot from the first image, its amber beacon lit and its torn, faded cloth bunting hanging across its front wheels, sits stopped on a grassy track in front of the concrete Cold War bunker entrance from the second image, small before the heavy green steel blast doors, which are shut. Seen from behind and a little to one side at ground level, the robot in the foreground facing the doors. The grass is clean and green, nothing burnt, nothing wrecked, no smoke, no other machines. Quiet, still, overcast grey daylight. {16mm} {house}

**S6-p2, references s3-bot-00b-a + SB12c:**

> Using the first image for the small robot and the second image for the bunker entrance: a wide, quiet shot of the concrete Cold War bunker entrance from the second image set into the grassy chalk hillside, its heavy green steel blast doors shut. On the clean grass just in front of the doors, the small grey six-wheeled delivery robot from the first image has stopped, side-on to camera, its amber beacon lit and its torn, faded cloth bunting hanging across its front wheels, the doors towering over it. Nothing burnt, nothing wrecked, no smoke, no other machines. Still air, overcast grey daylight. {16mm} {house}

| Option | From | Note |
| --- | --- | --- |
| `S6-a` | `work/S6-p1-a` | Maddie big in the left foreground, front three-quarter, the shut doors behind her. She faces camera, not the door. |
| `S6-b` | `work/S6-p1-b` | Same, closer and centred. |
| `S6-c` | `work/S6-p2-a` | Wide, the whole bunker in the hillside, Maddie small before the doors. Quiet, clean grass. |
| `S6-d` | `work/S6-p2-b` | Same as c, more sky, Maddie further right. The emptiest one. |

## S7: beat 17, The old lady among the crowd

**Brief:** Medium close-up on the old lady (N4r2-b look) among the crowd just inside the bunker, others in shadow/soft focus; mouth closed, neutral (for lip-sync); old-fashioned, dignified, unimpressed.

**S7-p1, references N4r2-b + SBHELLOb:**

> Using the first image for the old woman, her face, grey hair, glasses on a chain and green cable-knit cardigan, and for the film look, and the second image for the place: a medium close-up of the old woman standing just inside the whitewashed brick bunker tunnel from the second image, among a crowd of the bunker's people in worn jumpers and coats. She is framed from the chest up, slightly off-centre, arms folded, chin up, looking just off camera towards the doorway with a dignified, unimpressed expression, her mouth closed and relaxed, lips together. The people around her are in deep shadow and soft focus, faces unreadable. Cool grey daylight from the open doorway falls across her face from one side; the tunnel behind is dim. Anamorphic film frame, cool shadows, shallow depth of field. {house}

**S7-p2, references N4r2-b + M3-old-lady-blockbuster + B1-lived-tunnel-threads:**

> Using the first image for the old woman's face, grey hair, glasses on a chain and green cable-knit cardigan, the second image for her face in close-up and the film look, and the third image for the place: a medium close-up of the old woman standing in the front of a crowd inside the dim whitewashed brick bunker tunnel, framed from the waist up, facing three-quarters to camera, hands clasped in front of her, upright and composed, looking straight ahead with a steady, unimpressed gaze, her mouth closed and neutral. Behind and beside her the other people of the bunker are dark silhouettes and blurred shapes in shadow. One bare bulb above and grey daylight from the doorway light her face. Old-fashioned, dignified. Anamorphic film frame, cool shadows, shallow depth of field. {house}

**S7-p3, references N4r2-b + SBHELLOb:**

> Using the first image for the old woman's face, grey hair, glasses on a chain and green cable-knit cardigan, and the film look: a tight medium close-up, chest up, of the old woman standing inside the dim bunker tunnel, very shallow depth of field. She looks a little off camera, towards the doorway, dignified and unimpressed, chin lifted, her mouth closed and still, lips gently together. Grey daylight from the doorway lights one side of her face; the other falls into shadow. Behind her the bunker's people are only dark, heavily blurred shapes, their faces lost in shadow and bokeh. Anamorphic film frame, cool shadows. {house}

| Option | From | Note |
| --- | --- | --- |
| `S7-a` | `work/S7-p1-a` | Arms folded, chest up, the open doors behind; the crowd around her is dim but still fairly sharp. |
| `S7-b` | `work/S7-p2-a` | Waist up in the tunnel, hands clasped, the crowd as silhouettes under the lamp. Wider than an MCU. |
| `S7-c` | `work/S7-p3-a` | Profile, looking off to the doorway, the tunnel soft behind. Half her face is in the dark. |
| `S7-d` | `work/S7-p3-b` | Tight MCU, facing camera, the crowd only dark blurred shapes, mouth closed. Best for lip-sync. |

## S8: beat 17 rev, Maddie on the step

**Brief:** Maddie just inside the open blast door, from the old lady's eye line inside the bunker, daylight behind her.

**S8-p1, references s3-bot-00b-a + SBHELLOa:**

> Using the first image for the small robot and the second image for the bunker interior, the open doorway and the film look: standing height, from inside the whitewashed brick bunker tunnel, the eye line of a person among the crowd, looking slightly down the tunnel at the grey six-wheeled delivery robot from the first image, which has just rolled in and stopped on the concrete floor a few metres inside the open green steel blast doors, its amber beacon lit and its torn, faded cloth bunting hanging across its front wheels. Behind it, through the open doors, bright overcast daylight and a clean green grassy hillside, no smoke, nothing wrecked. The shoulders of people in worn coats frame the near edges of the shot, dark and soft. The robot is rim-lit by the daylight behind it. {16mm} {house}

**S8-p2, references s3-bot-00b-a + SBHELLOa:**

> Using the first image for the small robot and the second image for the bunker interior and the film look: from inside the whitewashed brick bunker tunnel, at the height of a person's eyes, looking down at a slight angle past the soft, dark shoulder and grey hair of an old woman in a green cable-knit cardigan in the near left of frame, to the grey six-wheeled delivery robot from the first image, which has stopped on the concrete floor just inside the open green steel blast doors, its amber beacon lit, its torn, faded cloth bunting hanging across its front wheels. Bright overcast daylight pours in behind it from the doorway, over a clean grassy hillside: no smoke, nothing wrecked. Long soft shadow of the robot stretches towards camera. {16mm} {house}

| Option | From | Note |
| --- | --- | --- |
| `S8-a` | `work/S8-p1-a` | Between dark coats, Maddie framed in the open doorway, kit and clutter on both sides; matches SBHELLO's tunnel. |
| `S8-b` | `work/S8-p1-b` | Clean white tunnel, two dark shoulders framing Maddie in the doorway. |
| `S8-c` | `work/S8-p2-a` | Over the old lady's shoulder (left), Maddie inside the doors, a long shadow towards camera. Bunting checked. |
| `S8-d` | `work/S8-p2-b` | Same, the lady's shoulder larger and Maddie closer to the door. Ties straight to S7. |
## Rejected (kept in `work/`, not offered)

| File | Why |
| --- | --- |
| `S2-p2-a`, `S2-p3-a`, `S3-p1-a`, `S3-p2-a`, `S5-p1-a` | The reference copied back unchanged (see above). No dust, no antenna, or SB12c's wrecks |
| `S2-p2-b`, `S2-p2-c` | The bunting moved up and wrapped round her lid. It must stay across the front wheels |
| `S3-p2-c` | The bunting came back as Union Jack flags |
| `S3-p3-a` | The "antenna" is a coiled spring on a plate; it doesn't read as an aerial |
| `S4-p2-b`, `S4-p3-a` | The nearest bot is a rusty old APC, not our kill-bot design |
| `S7-p1-b` | Same as S7-p1-a, and the crowd's faces are sharper. S7 had better options |

Nothing was policy-blocked and nothing timed out. 20 `flow_edit_image` calls, 45 candidates, 0 credits.

## Claude's picks (Kai picks the real ones)

| Shot | Pick | Why |
| --- | --- | --- |
| S1 | **S1-c** | The steep top-down the note asks for: the bot cuts in fast with a dust tail and Maddie is small mid-road. Nothing else in frame |
| S2 | **S2-d** | Front wheels lifted, rocked back in the dust. The 'whoa' reads from her posture alone |
| S3 | **S3-c** | The neatest pop-up gadget, and the bunting strip at the bottom edge tells you it's Maddie in a close-up |
| S4 | **S4-c** | Low, a kill bot huge in the foreground, the pack ahead, the door near: the most menace |
| S5 | **S5-c** | The door fills the frame and debris is flying; the green hull matches K5, so the red/green HUD flip will sit on it cleanly |
| S6 | **S6-c** | Small before a big shut door on clean grass. The quiet the beat wants, and it echoes the bunker establishers |
| S7 | **S7-d** | A tight MCU, mouth closed, facing camera, the crowd only blurred shapes: the best plate to lip-sync |
| S8 | **S8-d** | Over her shoulder, so it cuts straight back and forth with S7; Maddie lit by the doorway, bunting intact |

## Round 2 (20 Oct 2026, from Kai's picks)

Kai's picks, now final and not re-made: **S1-c, S2-c, S3-c, S5-a, S6-c**. Round 2 makes four new options each for S4r, S9 (new), S7r, S8r and S10 (new). It used the same project, model and rules. The new references are the picks themselves (`cut3/S4-c`, `S5-a`, `S6-c`, `S7-d`, `S8-d`) and `moodboard/K4-motorway.jpg` for the motorway. 22 calls in all, 0 credits, nothing blocked. One call (`S8r-p1`) came back **partial**, with 1 candidate of 2. The call after it was checked for a late-tile shift and its two files match their own prompt.

### S4r: beat 10b, The close race (round 2)

**Brief:** From S4-c: the big foreground kill bot removed; just the pack racing up the down to the bunker door, close now. Low camera in the grass.

**S4r-p1, references cut3/S4-c:**

> Using the provided image, change only one thing: remove the large tracked military robot in the right foreground entirely, and fill that space with more of the long grass and the dusty slope, so the low camera sits in the grass with nothing between it and the pack. Keep the three tracked military robots racing up the down towards the bunker, their dust trails, the concrete bunker entrance and its shut green blast doors, the sky and the grain exactly the same, preserving the original style, lighting and composition. {house}

**S4r-p2, references cut3/S4-c + P1-patrol-blockbuster:**

> Using the first image for the hillside, the bunker entrance, the film look and the low camera in the grass, and the second image for the tracked military robots: the camera low in the long grass on the down, with no robot near the camera. A pack of five tracked military robots like the one in the second image races up the slope away from camera towards the concrete bunker entrance with its shut green blast doors, which is close now and large in the upper part of frame. Long trails of dust and chalk boil up behind each of them. Overcast grey sky, menace, speed. {16mm} {house}

| Option | From | Note |
| --- | --- | --- |
| `S4r-a` | `work/S4r-p1-a` | A clean edit of S4-c: the foreground bot is gone, and three bots race up to the door with long dust trails. Faithful to Kai's pick. |
| `S4r-b` | `work/S4r-p1-b` | Almost the same as a (a second take of the same edit). |
| `S4r-c` | `work/S4r-p2-a` | Five bots, the nearest bigger in the middle of the frame. The pack is busier but the composition is the same. |
| `S4r-d` | `work/S4r-p2-b` | Closer to the door, which is big at the top of frame, with three bots in heavy dust. Which way they face is ambiguous: the nearest could read as coming towards camera. |

### S9: beat 10a, The far race (NEW)

**Brief:** The kill-bot pack racing at speed towards the distant downs, far from the bunker. Two across open Wiltshire fields, two down an empty, cracked, abandoned motorway, dust trails, the downs on the horizon.

**S9-p1, references P1-patrol-blockbuster + K9-downs-aerial:**

> Using the first image for the tracked military robots and the second image for the landscape: a wide, low shot across open Wiltshire farmland, overgrown fields of long pale grass and a broken hedge line, as a pack of six tracked military robots like the one in the first image races away from camera at full speed in a loose arrowhead, long trails of dust streaming behind them. Far off on the horizon the smooth green chalk downs rise under a heavy grey sky. No buildings near, no bunker in sight: they are still a long way off. Overcast, speed, menace. {16mm} {house}

**S9-p2, references P1-patrol-blockbuster + K4-motorway:**

> Using the first image for the tracked military robots and the second image for the abandoned motorway: a low, wide shot from the cracked tarmac of an empty, abandoned English motorway, weeds pushing up through the lanes and the central reservation overgrown, rusted dead cars shoved onto the hard shoulder. A pack of six tracked military robots like the one in the first image races away down the empty carriageway at full speed, long trails of dust kicking up behind them. Far ahead, where the motorway runs out to the horizon, the green chalk downs rise under a heavy grey sky. No signs, no gantries, no lettering. {16mm} {house}

**S9-p3, references P1-patrol-blockbuster + K4-motorway:**

> Using the first image for the tracked military robots and the second image for the abandoned motorway: a high shot from an old footbridge looking straight down the length of an empty, abandoned English motorway, cracked lanes, weeds and saplings through the tarmac, rusted dead cars pushed onto the hard shoulder and verges. Directly below and moving away from camera, a pack of six tracked military robots like the one in the first image races down the carriageway towards the horizon in two columns, long dust trails streaming back towards us. At the far end of the motorway the green chalk downs rise under a heavy grey sky. No signs, no gantries, no lettering. {16mm} {house}

| Option | From | Note |
| --- | --- | --- |
| `S9-a` | `work/S9-p1-a` | Fields: a low drone-height chase behind six bots in an arrowhead, the downs rolling across the horizon. |
| `S9-b` | `work/S9-p1-b` | Fields: lower, through a broken hedge line, the pack strung out with one big dust plume, the chalk downs beyond. |
| `S9-c` | `work/S9-p3-a` | Motorway: from a footbridge looking straight down the carriageway, six bots in formation, dead cars on both verges, the downs where the road ends. |
| `S9-d` | `work/S9-p2-b` | Motorway: a wider side angle, four bots crossing the lanes left to right in dust, the downs on the horizon. Spare: S9-p3-b (the same footbridge as c, with the bridge rail in shot). |

### S7r: beat 17, The old lady, from Maddie's eyes (round 2)

**Brief:** From S7-d: Maddie's POV from the doorway, so no bright opening behind her; the deep dim bunker interior, people receding, looking towards camera, wary, soft focus. Old lady unchanged, mouth closed.

**S7r-p1, references cut3/S7-d:**

> Using the provided image, change only the background behind the old woman: there is no doorway and no daylight behind her any more. Replace the bright opening with the deep, dim interior of the bunker: a long whitewashed concrete corridor receding into darkness, a single weak bulb far off, and more of the bunker's people standing further back, fading into shadow. The people in the background now face the camera, wary, watching, all in soft focus. The light on her face now comes from in front of her, cool and soft, as if from an open door behind the camera. Keep the old woman exactly as she is: her face, glasses on a chain, grey hair, green cable-knit cardigan, her pose and her closed, neutral mouth, preserving the original style and composition. {house}

**S7r-p2, references cut3/S7-d + B1-lived-tunnel-threads:**

> Using the first image for the old woman, exactly as she is, and the second image for the bunker's interior: the same framing of the old woman, her face, glasses on a chain, grey hair, green cable-knit cardigan and her closed, neutral mouth unchanged. Behind her, instead of a doorway, the dim, cluttered depth of the bunker tunnel from the second image, its arched whitewashed brick going back into darkness under a few weak hanging lamps, and a crowd of people in worn jumpers and coats standing at different depths behind her, all turned towards the camera, wary, soft and out of focus, the furthest lost in shadow. No bright window, no daylight opening anywhere behind her. Cool soft light falls on her face from the front. Anamorphic film frame, cool shadows, shallow depth of field. {house}

**S7r-p3, references cut3/S7-d:**

> Using the provided image, keep the old woman, the lens, the framing and the very shallow depth of field exactly as they are, with the background just as heavily blurred as it is now. Change only what is behind her: the bright doorway and the daylight are gone. Behind her now is the dark inside of the bunker, a dim concrete corridor going back into shadow with one faint, small lamp far away, and the blurred dark shapes of more people standing behind her, turned to face the camera, wary, their faces soft and unreadable in the blur. Nothing bright behind her head. Her face, glasses on a chain, grey hair, green cable-knit cardigan and closed, neutral mouth stay exactly the same, lit softly from the front. {house}

**S7r-p4, references cut3/S7-d + SBHELLOb:**

> Using the first image for the old woman, exactly as she is, and the second image for the bunker interior: the old woman's huge, tall double blast doorway is now behind the camera, so she is lit softly from the front by grey daylight, and behind her is only the dark bunker. A deep, dim concrete hall recedes behind her, and in it stand the bunker's people at several depths, turned towards the camera, wary, completely out of focus, soft dark shapes with the faintest catch of light on their faces, the furthest swallowed by shadow. No doorway, window or daylight behind her. Her face, glasses on a chain, grey hair, green cable-knit cardigan, pose and closed, neutral mouth are unchanged. Anamorphic film frame, cool shadows, extremely shallow depth of field. {house}

| Option | From | Note |
| --- | --- | --- |
| `S7r-a` | `work/S7r-p3-a` | Closest to S7-d: a dim concrete corridor, one small lamp, a crowd behind her facing camera, soft. No bright opening. |
| `S7r-b` | `work/S7r-p3-b` | The same, fewer and darker people, a lamp low behind her left shoulder. |
| `S7r-c` | `work/S7r-p4-a` | S7-d's brick tunnel kept, people at several depths facing camera, out of focus. The far end is a dim green door, not daylight. |
| `S7r-d` | `work/S7r-p1-b` | The most confrontational: a crowd packed close behind her in a narrow white corridor, all staring at camera. They are sharper than the brief asks. |

### S8r: beat 17 rev, Over her shoulder, the big doorway (round 2)

**Brief:** From S8-d: over the old lady's shoulder, a HUGE open blast doorway consistent with S6 (Maddie small against the big green double doors in the concrete portal), daylight and the green down beyond, bunting intact.

**S8r-p1, references cut3/S8-d + cut3/S6-c:**

> Using the first image for the old woman's shoulder and grey hair in the near left of frame, the bunker interior and the film look, and the second image for the robot and the scale of the blast doors: over the old woman's shoulder, looking out from inside the bunker towards a huge open blast doorway. The doorway is now much bigger: a massive concrete portal filling most of the frame's height and width, its two heavy green steel blast doors swung wide open, each door far taller than a person. Through it, bright overcast daylight and the green grassy down beyond. Small in the threshold, dwarfed by the doorway, the grey six-wheeled delivery robot from the second image, its amber beacon lit and its torn, faded cloth bunting hanging across its front wheels, its shadow stretching in across the concrete floor. Nothing burnt or wrecked outside. {16mm} {house}

**S8r-p2, references cut3/S8-d + cut3/S6-c + s3-bot-00b-a:**

> Using the first image for the old woman's shoulder and grey hair in the near left of frame and the film look, the second image for the robot and the green blast doors, and the third for the robot's exact design and bunting: a wider shot from deep inside the dim bunker, over the old woman's shoulder, looking up the concrete floor to an enormous open blast doorway, a great square concrete portal with its two towering green steel doors swung inward against the walls. The opening is bright with grey daylight and the green down beyond. The small grey six-wheeled delivery robot sits right in the threshold, tiny against the size of the doorway, amber beacon lit, torn faded cloth bunting across its front wheels, silhouetted and rim-lit. Nothing burnt or wrecked outside. {16mm} {house}

**S8r-p3:** the S8r-p1 prompt again (p1 came back partial).

| Option | From | Note |
| --- | --- | --- |
| `S8r-a` | `work/S8r-p1-a` | Big doors swung wide, Maddie in the threshold casting a long shadow in, the down rolling away behind. Her bun matches S8-d. |
| `S8r-b` | `work/S8r-p2-a` | A deep, clean concrete portal, doors open inward, Maddie small and centred. The most S6-like scale. |
| `S8r-c` | `work/S8r-p2-b` | Square portal, doors flat against the walls, Maddie silhouetted. The biggest doorway relative to her. |
| `S8r-d` | `work/S8r-p3-a` | Like a, but with heavier, rivetted doors and Maddie closer. Bunting checked at full size on all four. |

### S10: beat 12, The stand-down (NEW)

**Brief:** Outside the bunker, the kill-bot pack right at the blast doors (S6-c's door, S5-a's approach) has stopped and is turning round to roll away down the hill, dust settling, no damage anywhere. Wide enough to read as 'they turned back'.

**S10-p1, references cut3/S6-c + P1-patrol-blockbuster + cut3/S5-a:**

> Using the first image for the bunker entrance, its green blast doors and the hillside, the second image for the tracked military robots, and the third for the grassy approach: a wide shot of the concrete Cold War bunker entrance set into the grassy down, its heavy green steel blast doors shut and undamaged. Right in front of the doors, a pack of five tracked military robots like the one in the second image has stopped short, and they are turning round on the spot, pivoting on their tracks, the nearest already facing away from the doors and starting to roll back down the hill towards the camera. A haze of dust is settling around them. Nothing burnt, nothing broken, no smoke, no fire. Overcast grey daylight, an anticlimax. {16mm} {house}

**S10-p2, references cut3/S6-c + P1-patrol-blockbuster:**

> Using the first image for the bunker entrance, its green blast doors and the hillside, and the second image for the tracked military robots: a high, wide shot from further down the hill looking up at the concrete bunker entrance with its heavy green steel blast doors, shut and untouched. A pack of five tracked military robots like the one in the second image has come to a halt in a ragged line just in front of the doors, and has turned round: they are rolling away from the doors in single file down the grassy slope, the last one still swinging round. Tyre-like track marks curve in the grass where they turned, and dust drifts and settles in the still air. Nothing burnt, nothing broken, no smoke. Overcast grey daylight. {16mm} {house}

| Option | From | Note |
| --- | --- | --- |
| `S10-a` | `work/S10-p1-a` | Four bots stopped at the doors, the nearest already rolling down at camera. Dust hangs. The door is S6's. |
| `S10-b` | `work/S10-p1-b` | The same, the pack lined up at the door and the lead bot pivoting away. |
| `S10-c` | `work/S10-p2-a` | High and wide: the pack filing away in single file, with fresh track marks curving in the grass where they turned. Reads 'they turned back' at a glance. |
| `S10-d` | `work/S10-p2-b` | The same idea: the lead bot swings away right, with turning marks in the grass. |

### Round 2 rejects (in `work/`)

| File | Why |
| --- | --- |
| `S9-p2-a` | The pack drives towards camera, away from the downs: the wrong direction for "racing to the downs" |
| `S9-p3-b` | Fine, kept as a spare. The same footbridge as S9-c, with the rusty bridge rail in shot |
| `S7r-p2-a`, `S7r-p2-b` | The crowd behind her is sharp and fully lit. Kai liked S7-d's soft background, and these lose it |
| `S7r-p1-a` | The crowd's faces are sharp, and its people wear webbing and military kit, which is off-look |
| `S7r-p4-b` | The background men have their backs to camera, not facing Maddie |
| `S8r-p3-b` | The old lady changed: short bobbed hair instead of S8-d's bun, and she stands in the middle of frame |

### Claude's picks, round 2

| Shot | Pick | Why |
| --- | --- | --- |
| S4r | **S4r-a** | Exactly Kai's S4-c with the foreground bot gone: three bots and their dust trails converging on the door |
| S9 | **S9-c** | The motorway from the footbridge: a formation, dead cars on both verges, the road running straight at the downs |
| S7r | **S7r-a** | Closest to S7-d (same blur, same her), with the doorway swapped for a dark corridor full of wary faces |
| S8r | **S8r-b** | A huge, deep portal with Maddie small and centred, the scale of S6, and her bun matching S8-d |
| S10 | **S10-c** | The curving track marks plus the single-file retreat read "they turned back" without any explanation |

## Clips (batch 1, and batch 2 from Kai's round 2 picks)

Made 20 Oct 2026 in Flow project `be451638` (Jack's account), **Omni 1.1 Flash, Frames (start frame only), 16:9, 720p**,
one job at a time through [`scripts/gpom/second-half-video/run-cut3.mts`](../../../../scripts/gpom/second-half-video/run-cut3.mts)
(job specs in the log `run-cut3.log`; spend in `run-cut3.ledger.json`). Before every Create the runner read Flow's own
price label and refused anything over 20 credits a clip or over the cap (300, then 550 with batch 2): **8 s x1 = 12,
8 s x2 = 24, 6 s x2 = 20**. Balance **18,844 → 18,428 = 416 credits** (batch 1: 236 of 300; batch 2: 180 of 250). Every
harvest was md5-checked against every clip on disk and first-frame-matched to its plate (distances 3–19; correct < 400).
Veo audio stripped on every picture clip (originals with audio in `video/cut3-raw/`). Contact sheet `<clip>-sheet.jpg`
beside each. Media: `/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/video/`.

`West Country Bot` = the Character cast by `@` (street shots only; the bunker shots are uncast, because the Character
carries its high street with it).

| Clip | Beat | Plate | Cast | Credits | Motion prompt | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| `cut3-V1.mp4` | 9a | S1-c | no | 12 + 12 | *The camera does not move, locked high above the street. The tracked military robot speeds straight down the road, passes close beside the small grey robot without touching it, and drives on out of the bottom-left edge of frame, leaving a long plume of dust hanging behind it. As it passes, the small robot jolts and rocks on its wheels. The camera does not move.* | **Pass (take 2).** Passes close, exits bottom-left, dust hangs, she jolts; bunting kept. Take 1 (cast, "tears forward… swerves hard round", in `cut3-raw/cut3-V1-r1-reject.mp4`) **failed**: the tank drove into her and vanished in its own dust, and her bunting turned into bright multicoloured party flags flying off |
| `cut3-V2.mp4` | 9b | S2-c | yes | 12 | *The camera does not move. Thick grey-brown dust swirls and rolls around the small grey delivery robot. It rocks back on its rear wheels, its front wheels lifting off the road, then drops back down and settles. Its torn bunting flaps hard across its front wheels and its amber beacon flares. The dust slowly thins. The camera does not move.* | **Pass, with a note.** Dramatic: she leaps clear of the road on all six wheels, a strand of bunting streams off, she lands and settles; the bunting is back across her wheels at the end. Bigger than "rocks back" — Kai to say if it's too comic |
| `cut3-V3.mp4` | 11 | S3-c | yes | 12 | *Locked-off close-up; the camera does not move. The slim chrome antenna telescopes further up out of the open round hatch with a quick little jerk, one more segment sliding out and wobbling to a stop. The tiny red light on its tip starts blinking on and off. The amber beacon glows steadily. The camera does not move.* | **Pass, subtle.** The tip light blinks red throughout; the telescoping is a small jerk-and-wobble near 1.3 s, not a big extension |
| `cut3-V4.mp4` | 12 | S5-a | no | 12 | *The camera is fixed to the front of the racing tracked robot. It charges straight up the grassy track at the green blast doors, tracks churning up grass and chalk, then brakes hard and skids to a stop a few metres from the doors. A thick cloud of dust rolls forward past the camera and over the hull, then hangs in the air. Clean picture, no text, no overlay.* | **Pass.** Races in, sparks off the tracks as it brakes, stops metres short, dust rolls over the hull. No text. A dark round lens appears on the hull's nose at the stop |
| `cut3-V5.mp4` | 14a | S6-c | no | 12 | *The camera does not move. The small grey delivery robot sits still in front of the shut green blast doors, its amber beacon blinking twice. Then it turns to its left and drives smoothly away across the clean grass and out of the left edge of frame. The doors, the concrete and the hillside stay still. No dust. The camera does not move.* **Reversed in ffmpeg** (forward take in `cut3-raw/cut3-V5-forward.mp4`) | **Pass.** The plate already has her at the door, and Omni re-stages a subject the prompt contradicts (rebuild doc item 77), so the arrival was shot as a departure and reversed: she rolls in from the left, settles, the beacon blinks, and the clip ends exactly on Kai's still. She arrives facing slightly back the way she came (reversing in); nothing physical settles, so it reads forwards |
| `cut3-beat0-continuous.mp4` | 0 | first frame of `simulation/video/09-s3-robot.mp4` | yes, every clip | 6 × 12 | Clip 1: *The camera tracks steadily backwards up the high street ahead of the small grey delivery robot. The robot turns to face the camera and rolls along after it at the same speed, staying the same size in frame, the ruined shops sliding past on both sides. Its amber beacon pulses in a lively rhythm, as if it is chatting away. Its torn bunting sways across its front wheels. It never stops.* Clips 2–6: *The camera keeps tracking steadily backwards up the high street at the same speed. The small grey delivery robot keeps rolling towards the camera at the same pace, staying the same size in frame…* (rest as clip 1) | **Pass. 47.75 s, one unbroken travelling shot**, six clips each started from the previous clip's last frame, no crossfade. Join differences 2.6–3.9 against 4.2–7.8 inside the clips; in the joined file every join step sits inside the shot's own range. Bunting checked at every join. ⚠️ **Drift**: the colour slides from warm to cold grey and the robot gets smoother over the 48 s (gradual, no join shows it); a ramped grade back towards clip 1 is owed in post. Parts in `video/cut3-beat0/` (`chain-0N.mp4`, last frames, join strips) |
| `cut3-V8.mp4` | 10a | S9-c | no | 12 | *The camera does not move, locked on the footbridge. The pack of tracked military robots charges away down the abandoned motorway in formation at full speed, heading for the green downs on the horizon, long trails of dust boiling up behind their tracks and drifting back towards us. The dead cars on the verges stay still. The camera does not move.* | **Pass.** The formation pulls away down the carriageway into its own dust |
| `cut3-V9.mp4` | 10b | S4r-a | no | 12 | *The camera does not move, locked low in the grass. The three tracked military robots race up the slope at full speed, converging on the shut green blast doors of the bunker, long trails of dust and chalk streaming behind them. The long grass in the foreground whips in the wind. The camera does not move.* | **Pass.** Two more bots burst in from the frame edges past the camera and the pack converges on the door: more menace than asked, five not three |
| `cut3-V10.mp4` | 12 | S10-c | no | 12 | *The camera does not move, a locked wide shot. The tracked military robots at the bunker doors slow, the last one swings round on its tracks, and the whole pack files away down the grassy hill in single file, unhurried. The dust they raised drifts and settles in the still air. The shut green doors stay untouched. The camera does not move.* | **Pass.** The column files down the hill towards the camera along its track marks |
| `cut3-V11.mp4` | 17 rev | S8r-b | no | 12 | *The camera does not move. In the bright open doorway the small grey delivery robot waits, nudging a little way forward and back again on its wheels, its amber beacon pulsing gently as if it is talking. Its torn bunting sways across its front wheels. The old woman in the foreground stays almost still. The camera does not move.* | **Pass, quiet.** Small nudges, the beacon pulses, the old lady barely moves |

### Lip-sync (V7 Sandra and Derek, V12 the old lady), by the `lip-sync-dub` skill

Talking clips: Frames mode, the plate as start frame, the exact line after *"She says:"* / *"He says:"*, 2 candidates.
Sandra on `storyboard/SB07b.jpg` (her face to camera over Derek's shoulder; cut 2's beat 6 plate `B5` is too wide to
sync), Derek on `SB07c.jpg`, the old lady on `cut3/S7r-a.jpg`. Prompt shape:
*"The camera does not move. The furious woman in the cream jumper, facing the camera, points at the man and speaks to
him sharply. She says: <line> Then she presses her lips together and glares. The man with his back to the camera stays
still and silent."* (Derek: *"…throws his hands wide and shouts at the woman. He says: …"*; the old lady: *"…looks
steadily into the lens and speaks, calm and firm. She says: …"*.) Each clip's own audio was transcribed (faster-whisper,
small.en, CPU): **every kept candidate says the dub's words**; `L17-6b-a` said *"He can talk, talk"* and was dropped.
Mouths mapped with `scripts/lipsync/mouth-track.py` (new: a tracked 12 fps mouth strip, because the heads move); phrases
placed with `place-dub.py`, each on a mouth opening, tempo 1.0–1.3. The dub alone was transcribed for every shot (all
words survive). **The listen tool was not run** (Kai's standing rule), so the skill's check (b) for warble is owed to a
human ear.

Voice masters (`audio/cut3-lip/<line>-master.wav`; picks per the brief): 06-0 = p0 take **b** + 0.6 s + p1 take **a**;
07-0 **a**; 07-1 **b** (take a, the pick by length, transcribes as *"the world ends at sundry"*; b reads clean);
07-2 **b**; 17-0 **b**; 17-3 **a**; 17-6 p0 **a**, p1 **a**. Phrase tables and dubs beside them
(`cut3-lip-<line>-phrases.json`, `-dub.wav`, −20.5 LUFS).

| Shot (`video/`) | Candidate | Credits | Placement | Verdict |
| --- | --- | --- | --- | --- |
| `cut3-lip-6-0.mp4` | L06-0-a | 24 | "Derek." 0.03 · "You've left the seat up." 1.00 x1.03 · "Again." 3.44 x1.30 | Good fit. "Again" ends 0.1 s after the mouth shuts |
| `cut3-lip-7-0.mp4` | L07-0-a | 24 | whole line 0.03 x1.07 | Good: one long burst, one phrase |
| `cut3-lip-7-1.mp4` | L07-1-b (6 s) | 20 | 0.46 x1.00 | Good; ends 0.13 s after the mouth closes (x1.07 made "Sandra" sound like "sundry") |
| `cut3-lip-7-2.mp4` | L07-2-a | 24 | "Yeah," 0.02 · "the world ended." 0.98 · "Doesn't mean you get to stop having manners." 2.10 x1.10 | Good fit, three bursts, three phrases |
| `cut3-lip-17-0.mp4` | L17-0-a | 24 | "Your boss killed everyone we ever loved." 0.92 x1.20 · "We're not meeting him." 4.85 x1.30 | ⚠️ **Phrase 2 overruns** the mouth by about 0.3 s (her mouth burst is 0.7 s; the slow voice needs 1.0 s even at x1.30). **Cutaway candidate** for "…meeting him" (S8r reverse on Maddie), or re-shoot it as its own clip |
| `cut3-lip-17-3.mp4` | L17-3-b | 24 | whole line 1.42 x1.05 | Good |
| `cut3-lip-17-6a.mp4` | L17-6a-a (6 s) | 20 | "Well." 0.46 x1.30 · "At least you're honest about that." 2.00 x1.26 | Fits; "Well." ends 0.1 s late; a small silent mouth flicker at 1.1 s |
| `cut3-lip-17-6b1.mp4` | L17-6b1-b (6 s) | 20 | "He can talk. From" 0.33 x1.00 · "out there." 3.17 x1.30 | Good |
| `cut3-lip-17-6b2.mp4` | L17-6b2-b (6 s) | 20 | "You stay on the step." 1.42 x1.18 | Good |

17-6 was meant to be two clips (split at the pause). The first try at the second half (`L17-6b`, 24 credits, *"He can
talk. From out there. You stay on the step."* in one 8 s clip) **could not be placed**: Omni spoke it in about 2.7 s of
mouth against 4.7 s of voice. Re-shot, per the skill's step 2, as two 6 s clips (`17-6b1`, `17-6b2`), which fit. So
17-6 is **three** shots: `17-6a`, `17-6b1`, `17-6b2`. Each dubbed shot has a `-muted.mp4` twin (no audio) and a sheet;
the raw talking takes (with Omni's own audio) are in `video/cut3-lip-raw/`.
