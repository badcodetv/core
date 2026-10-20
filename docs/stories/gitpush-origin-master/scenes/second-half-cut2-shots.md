# GPOM second half, cut 2: the new shots N1–N4

The four new pictures that cut 2 part 1 (beats 0–18) needs, from the `cut2.shots` block in
[`second-half-audio-plan.json`](./second-half-audio-plan.json). Kai waived the still-approval gate for
N1–N4 (19 Oct 2026), so Claude picked the stills. N5 (the door re-roll) is optional and was not made.

- **Flow project:** `be451638` (the second-half project, which holds the **West Country Bot** Character).
- **Stills:** `flow_edit_image`, **Nano Banana 2** (0 credits; Pro was not used because it bills), 16:9,
  2 candidates each, from the plate each brief names. Bot shots carry `s3-bot-00b-a.jpg` as a reference
  and cast the West Country Bot Character. The torn bunting stays.
- **Clips:** Omni 1.1 Flash, Frames (start frame only), 16:9, 720p, 8 s, x1, camera locked, motion-only prompt.
- **Media:** stills in `/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/storyboard/cut2/`,
  clips as `/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/video/cut2-N<k>.mp4`, each with a
  `-sheet.jpg` contact sheet.

House suffix on every still (the same as the second-half storyboard): *"16:9 frame from a fictional
near-future British film. Full-frame image, no captions, logos, lettering or on-screen text."* The 16mm
ones also carry: *"Styled as a 1980s British television drama shot on 16mm film: faded colour, soft
contrast, heavy grain."* Below, `{16mm}` and `{house}` stand for those two sentences.

## N1 — beat 13, the bunker reaction

**Plate:** `storyboard/SB07a.jpg` (frame 7, the row in the lavatory).

**Still prompt (edit, reference SB07a):**

> Using the provided image, change only the moment: the woman in the cream jumper and the man in the dark
> green jumper have frozen mid-argument, her pointing arm and his spread hands still raised, and both now
> look straight up at the ceiling, startled. A haze of dust and grit sifts down from the cracked ceiling
> through the light of the fluorescent tube. At the right edge of frame two other people in worn jumpers
> have stopped in the doorway and look up at the ceiling too. Keep both faces, hair and jumpers, the white
> tiles, the black drain pipe, the toilet cubicle and the fluorescent light the same, preserving the
> original style, lighting and composition. {16mm} {house}

**Motion prompt:** see the ledger below.

## N2 — beat 14a, Maddie at the wrecked machines

**Plates:** `storyboard/SB12c.jpg` (frame 12's aftermath: three wrecks smoking before the shut doors) and the
bot reference `clips/simulation/stills/s3/s3-bot-00b-a.jpg`; Character **West Country Bot** cast.

**Still prompt (edit, references SB12c + s3-bot-00b-a):**

> Using the first image for the place and the second image for the robot: a low, close shot at ground
> level on the scorched track in front of the concrete bunker entrance in the grassy hillside, the green
> blast doors shut in the background. Three wrecked tracked military robots lie tipped on their sides,
> blackened and smoking. In the foreground the small grey six-wheeled delivery robot from the second
> image, its amber beacon lit and the torn, faded bunting hanging across its front wheels, races up the
> track towards the doors, kicking up dust and grit, the camera low and close beside it. Overcast grey
> daylight, drifting smoke. {16mm} {house}

## N3 — beat 14b, the tannoy

**Plate:** `storyboard/SBDOORa.jpg` (the bunker tunnel, for the place, the light and the residents).

**Still prompt (edit, reference SBDOORa):**

> Using the provided image for the place, the light and the film look: a low-angle shot in the same
> whitewashed brick bunker tunnel. High on the curved wall hangs an old Cold War tannoy loudspeaker horn,
> painted cream, chipped and dusty, its cable clipped along the wall. One bare bulb burns beside it and
> the rest of the tunnel is dim. Below it, the heads and shoulders of the bunker's people in worn jumpers
> and coats turn up towards the horn, waiting. {16mm} {house}

## N4 — beat 17, the old lady blocks the way

**Plates:** `moodboard/M3-old-lady-blockbuster.jpg` (frame 17's old lady) and the bot reference
`s3-bot-00b-a.jpg`; Character **West Country Bot** cast. Frame 17 is the blockbuster look, so N4 keeps it.

**Still prompt, angle A (Maddie's eye line), edit, references M3-old-lady-blockbuster + s3-bot-00b-a:**

> Using the first image for the woman and the film look, and the second for the robot: a low-angle shot
> from just above the floor, at the height of the small delivery robot, looking up at the old woman from
> the first image — the same face, grey hair, glasses on a chain and green cable-knit cardigan — standing
> just inside the open green blast doors with her arms folded, blocking the way and looking down. Behind
> her the heavy doors stand open onto grey daylight and drifting smoke. The top of the robot from the
> second image, its amber beacon and a strip of torn bunting, sits soft in the bottom corner of frame.
> Anamorphic film frame, cool shadows, shallow depth of field. {house}

**Still prompt, angle B (hers), same references:**

> Using the first image for the woman and the film look, and the second for the robot: over the old
> woman's shoulder, looking down at the small grey six-wheeled delivery robot from the second image on the
> concrete floor just inside the open green blast doors, its amber beacon lit, the torn faded bunting
> across its front wheels, smoke and grey daylight behind it. Her folded arm and the green cable-knit
> cardigan fill the near edge of frame, soft. Anamorphic film frame, cool shadows, shallow depth of field.
> {house}

### N4 round 2 (the rewrite that won)

Round 1 (`N4-a`, `N4-b`, `N4-rev`, Character cast + bot reference) failed on two counts: the bot
reference and the Character carried their **ruined high street and church tower** in through the doors
(the bunker is in a hillside), and the old lady stood far off, not over Maddie. Rewritten, not re-rolled:
no Character, and the bot-and-place reference swapped for **N2-a** (the bot in front of this bunker).

**Angle A (Maddie's eye line), references M3-old-lady-blockbuster + N2-a:**

> Using the first image for the old woman, her face, grey hair, glasses on a chain and green cable-knit
> cardigan, and for the film look, and the second image for the place outside: a dramatic low-angle shot
> from floor level, looking steeply up at the old woman standing close over the camera, framed from her
> knees to the top of her head, arms folded, glaring down into the lens. She stands just inside the
> bunker's open green steel blast doors; behind her, through the doorway, the scorched track and the
> grassy hillside from the second image under grey daylight, with smoke drifting across. In the bottom
> corner of frame, the soft out-of-focus glow of an amber beacon. Anamorphic film frame, cool shadows,
> shallow depth of field. {house}

**Angle B (hers), same references, 1 candidate:**

> Using the first image for the old woman and the film look, and the second image for the robot and the
> place outside: over the old woman's shoulder, looking down at the small grey six-wheeled delivery robot
> from the second image, close to her feet on the concrete floor just inside the bunker's open green steel
> blast doors, its amber beacon lit and the torn faded bunting hanging across its front wheels. Behind it,
> through the doorway, the scorched track and the grassy hillside with smoke drifting in grey daylight. Her
> grey hair, shoulder and green cable-knit cardigan fill the near edge of frame, soft. Anamorphic film
> frame, cool shadows, shallow depth of field. {house}

## Ledger: what was made, picks and why

Stills made 19 Oct 2026, Nano Banana Pro (the compose bar read *"Generating will use 0 credits"* at Pro
x2, so the brief's Pro was used; the MCP's `"Nano Banana 2"` no longer exists in the menu, which now lists
**Nano Banana Pro · Nano Banana 2 Lite · Nano Banana 2.1**).

| Shot | Candidates (in `storyboard/cut2/`) | Pick | Why |
| --- | --- | --- | --- |
| N1 | `N1-a`, `N1-b` | **N1-b** | Dust visibly falling through the tube light; both keep the row's gestures; the two onlookers read as separate people. In `a` the onlookers crowd her. |
| N2 | `N2-a`, `N2-b` | **N2-a** | Low and close, as the brief asks; the bot is big in frame, bunting and beacon intact, wrecks smoking either side of the doors. In `b` the bot is small and mid-frame. |
| N3 | `N3-a`, `N3-b` | **N3-a** | One bulb, low light, the horn large and unmistakable, faces turned up under it. `b` lights the whole tunnel. |
| N4 | `N4-a`, `N4-b`, `N4-rev` (round 1, rejected), `N4r2-a`, `N4r2-b`, `N4r2-rev` | **N4r2-b** (Maddie's eye line); **N4r2-rev** kept as the reverse | `r2-b`: she is close, arms folded, glasses on, the hillside and the wrecks behind, the beacon in the corner. `r2-a` keeps her small in the doorway. `r2-rev` is the clean reverse (bot, bunting, hillside) for the exchange; it stays a still. |

Clips: Omni 1.1 Flash, Frames (start only), 16:9, 720p, 8 s, x1, through `scripts/gpom/second-half-video/run.mts`
with `GPOM_CUT2=1` (shot list and motion prompts in `shots.py` → `CUT2_SHOTS`). N2 casts the West Country Bot
by `@` mention; N1, N3 and N4 have no bot body in frame and are uncast.

### The clips (19 Oct 2026, one wave, every shot first try, no re-rolls)

Run: `GPOM_CUT2=1 FLOW_CDP_PORT=<flow channel port> WAVE=4 MAX_WAVES=1 npx tsx scripts/gpom/second-half-video/run.mts`
(log: `scripts/gpom/second-half-video/run-cut2.log`). All four submitted on attempt 1 and rendered in under 3 minutes.
Each clip was named by its first frame against its plate (`match.py`: distances 8–20, where a correct match is under 400).
None matches an older clip's md5. Veo audio stripped (`-c:v copy -an`), as on the rest of the second half.

| Clip | Plate | Cast | Contact sheet verdict |
| --- | --- | --- | --- |
| `video/cut2-N1.mp4` | N1-b | no | Dust and a burst of plaster drop through the tube light; the pair stay frozen with their arms up, and the onlookers turn. The camera holds. Keep. |
| `video/cut2-N2.mp4` | N2-a | West Country Bot (`@`) | The bot races away up the track throwing dust, bunting flapping, and stops at the doors. The wrecks keep smoking. Keep. |
| `video/cut2-N3.mp4` | N3-a | no | The bulb flickers and dims and the faces hold on the horn. The flicker is subtle, so a Premiere flicker on the words can sit on top. Keep. |
| `video/cut2-N4.mp4` | N4r2-b | no | She holds her ground with her arms folded and her jaw set. The beacon pulses in the corner, and the smoke and fire grow on the wrecks behind her. Keep. |

Credits: 4 Omni 1.1 Flash 8 s clips (about 12 each by the 2026-09 popover reading, about 48 in all, not re-read today); stills 0.
