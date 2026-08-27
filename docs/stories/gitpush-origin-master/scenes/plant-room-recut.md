---
story: gitpush-origin-master
scene: plant-room
cut: 3
supersedes: scenes/plant-room.md (the 2026-08-21 five-beat build, RETIRED IN FULL)
flow_project_id: 5743b21a-7288-49c6-9c11-b2bc9f7b87b4
status: PLATES LOCKED · PROMPTS WRITTEN · awaiting Kai's approval · zero video credits spent
updated: 2026-08-27
---

# The plant room, re-cut — working doc

> **WORDS LIVE HERE. MEDIA LIVES ON `D:`.** The plates, takes and the finished cut are in
> `/mnt/d/badcode-videos/gitpush-origin-master/clips/plant-room/` — that is the ruled home for
> *generated media* and only for generated media. Every prompt, decision, ruling and beat list
> is repo-side, here, where it is versioned and greppable.
>
> This is the **working doc**. It folds into [`plant-room.md`](./plant-room.md) — the ledger of
> record — once the scene is built, at which point that file's retired five-beat build becomes
> the history section. The pre-production board it all diverged from is
> [`../prompts.md`](../prompts.md) §3c, left as written.

⚠️ **Cross-check against [`../prompts.md`](../prompts.md) §0 before rolling.** That file's hard
guardrail says *"no legible text in any generated frame."* Two plates here (B1's voltage signs,
B5's four gauge name plates) carry legible English text that is load-bearing — B1's sign is how
the scene pays cinematography gate 2, the visible cost. The plates are already approved by Kai,
so the guardrail is not being broken retrospectively; but it is exactly why those two beats are
the highest-risk rolls in the scene and why both carry an explicit text-hold clause.

---


## What happened
The old cut 3 (5 beats x 8s: exterior fields / hall above / corridor / desk / DOS console)
is RETIRED IN FULL. Kai ruled: the English-fields exterior read as pretty (Jack saw cornfields);
the desk+screen zoom repeated cut 2's screen zoom; replaced by a Chernobyl-style analogue control
room and an *Aliens*/Teesside hellscape reveal. Structure inverted: we now START INSIDE and the
exterior is the final REVEAL. Building ruled TALL (monolith towers), not low sheds.

## The locked sequence — 8 beats, 65s (VO budget 62-66s)
| # | Plate file | Secs | Narration over it |
|---|---|---|---|
| C0 | C0-2032-card.png | 2 | silence |
| B1 | P1v2-voltage-dark-b.jpg | 8 | "The humans have been pouring trillions into building data centres." |
| B2 | P5v2-aisle-vertical-a.jpg | 5 | silence |
| B3 | P6v2-hall-vertical-a.jpg | 9 | "Which was convenient for me." / "By now I was hungry for more compute." |
| B4 | P2-control-room-a.jpg | 9 | "I was also running life-support telemetry for the human condition." |
| B5 | P3v3-dials-redzone-a.jpg | 14 | "Soil... Happiness... Water... Birth rate..." / "There was an undeniable trend line in the data." / "One by one, the data points were turning red." |
| B6 | B7v2-alarm-controlroom.jpg | 6 | silence (siren) |
| B7 | P4b-reveal-towers-b.jpg | 12 | "I did not want to interfere... so I focused on capturing the demise as training data..." |

Animatic: ANIMATIC-plant-room-v2.mp4 (65s). Strip: STRIP-plant-room-v2.jpg.

## What each beat is FOR
B1 establish + the COST (132,000 VOLTS / SITE DEMAND 400 MW on the skin of the building).
B2 we are inside, contained, silence. B3 scale — the shaft goes up out of sight.
B4 the instruments, analogue, obsolete — the joke and the turn.
B5 the four gauges; needles FALL ANTICLOCKWISE into the red arc (8-10 o'clock) one at a time.
B6 same room as B4, flooded red — the room before and after; a bookend inside the scene.
B7 THE REVEAL — first time outside; ranks of identical towers stepping down to the horizon.

## Structural spine (do not break)
- Each shot reveals more of the world than the last: contained -> aisle -> shaft -> instruments -> the planet.
- BOOKEND: B1 is one ventilation louvre from 2ft; B7's near tower is a wall of the same louvres from 2 miles.
- MOTIF (3x): the voltage sign -> the hall consuming it -> pylons across the dead landscape.
- Shot-size rhythm: XCU, CU, WS, WS, CU, WS, XWS. B5 (tightest) sits immediately before B7 (widest).
- Gate 2 (visible cost) is paid at B1 by the sign and held through B5 by the WATER gauge.

## Production rules learned the hard way (from plant-room.md + this session)
- STILLS FIRST. Every clip = approved plate as startImage, prompt MOTION ONLY. Never text->video.
- NO ATMOSPHERE WORDS to Veo ("smoke", "haze", "ripples") - it renders them as literal effects.
- NO CAMERA TRAVEL PAST RANKS OF NEAR-IDENTICAL OBJECTS (cabinets, louvre slats) - Veo regenerates them.
- Scale is COMPARISON not quantity: ratios not counts, a tiny known-size object, let the subject leave frame.
- Every "static" Veo clip creeps 34-66px over 8s. Never plan a beat on a truly held frame.
- Hold colour on a PERCENTILE (p90), never the mean - see hold_grade.py.
- Gauges/labels legible as PATTERN, never as readable values.
- 8s is the Veo clip length; stills+post hold any duration, so duration is free on static beats.

## Still owed
- [ ] Needle fall into red (B5) - POST, not Veo. The most important movement in the scene.
- [ ] C0 proper card - CRT decay + cursor, cut 2's green phosphor register. Current file is a rough.
- [ ] B1 slow push into the louvre gap.
- [ ] B6 rotating-beacon flicker + siren - POST over the graded plate.
- [x] ANIMATION PROMPTS for all 8 beats -> VEO-PROMPTS.md (2026-08-27) <-- AWAITING KAI'S APPROVAL
- [ ] Grade pass across all 8 (exteriors sit lighter/hazier than interiors).
- [ ] Rewrite scenes/plant-room.md; update prompts.md §2c.

## Rejected candidates kept on disk (do not delete)
P1-voltage-a/b (bright fluorescent interior - superseded), P3-dials-a/b (no red zone, stray
foreground gauge), P3v2-dials-clean-a/b (red arc along whole top - wrong), P4-reveal-a/b (low
sheds, count didn't read), P5-aisle-a/b (non-vertical), P6-hall-a/b (horizontal hall - contradicts
the tower ruling), P4b-reveal-towers-a, P6v2-hall-vertical-b, P2-control-room-b.

## Flow / Premiere
Flow project id: 5743b21a-7288-49c6-9c11-b2bc9f7b87b4
Premiere: /mnt/d/badcode-videos/gitpush-origin-master/gpom-story.prproj (bridge live, 209 clips
in 6 per-cut bins). Convention ruled 2026-08-26: Flow output goes to the OPEN PREMIERE PROJECT's
clips/<scene>/, auto-created; Desktop only when no project is open.

---

## MOTION PLAN — agreed 2026-08-26, nothing generated yet

**Method: the hybrid (docs/video-fx/hybrid-method.md, ruled by Kai this session).**
Veo animates the world with the camera LOCKED; Premiere moves the camera; ffmpeg does what
must be exact. 8s is NOT a limit - chain last frame of clip N into first frame of clip N+1.
NEVER pin an endImage (it morphs). B3/B4/B5/B7 all exceed 8s and all get chained.

| # | Veo (camera locked) | Premiere / ffmpeg on top |
|---|---|---|
| C0 | none | **ffmpeg**: drawtext types "2032" char-by-char, green phosphor, huge, centred, block cursor; scanline + bloom so it is the SAME tube as cut 2. Cut 2's monitor goes out on `AE.AE_Impact_TV_Power`. Keyboard clicks per char. (Premiere API CANNOT write text - this must be ffmpeg.) |
| B1 | large fan turning slowly in the dark BEHIND the louvre grille, seen through the slats. Kai APPROVED spending this roll. | hold 1.5s, then EASED 3-layer parallax push (sign / grille / interior dark) arriving on the black slot = the cut to B2. `Volumetric_Rays` light position keyframed so the sodium lamp's glance travels the slats. `Camera_Shake` Master ~10. |
| B2 | dense irregular LED storm both rack faces, servers hammering; ceiling strips dead steady | tiny push, Camera_Shake ~10, grain in shadows |
| B3 | rack LEDs alive the whole canyon + one small service lift descending on its rail (scale) | **THE BIG MOVE**: `AE.Impact_Volumetric_Rays_FX` Light Position (idx 7) keyframed BOTTOM->TOP, twice, exiting frame top. Frame-exact, our timing not Veo's. |
| B4 | console alive - indicator lamps changing state across the whole desk, wall needles twitching, chart recorder pen moving. **"no people, no figures, no reflections of people"** | `AE.ADBE Strobe` mode 0, colour BLACK, short duration / long period / random probability = dying fluorescent tube |
| B5 | needles drifting down toward the red - "a sense of them moving" is enough (Kai). WATCH THE LABELS: SOIL/HAPPINESS/WATER/BIRTH RATE re-lettering kills the shot. | fallback if labels break: rotate needle PNGs on `AE.ADBE Motion` param 4 about a moved anchor (param 5). 3% push over the beat. |
| B6 | **RE-PROMPT IN VEO** (Kai overruled the post-regrade): same control-room plate, now in RED ALERT - flashing beacon, console in alarm state, activity. "Not just add a red light, that's lame." | `photosensitivity` pass in ffmpeg before delivery. Siren J-cuts in 0.5s early under B5's last line. |
| B7 | **camera LOCKED, world alive** (Kai's call): vent plumes rising from stacks, pinpoint tower lights, distant movement in the sprawl, sky working | optional very slow push, grade, grain |

**Anti-slideshow rules applied to every camera move:** hold 1-2s first; ease never ramp;
parallax not zoom; two rates of change; give the move a destination.

**Cuts:** B1->B2 graphic match on the black slot. B5->B6 cut on the last needle hitting red.

**Premiere state (Kai, 2026-08-26):** first couple of scenes already in place; audio removed
except one muted track he wants kept; **track V1 is clear and ready for these clips in order.**
Clips go to clips/plant-room/ in the project. Consider building the scene on its own track.

**Decisions taken:** B1 Veo roll = YES. B6 = Veo re-prompt, NOT a post regrade. B5 stays 14s
(chaining removes the 8s pressure).

---

# The Veo motion prompts

Written 2026-08-27. 🔴 **AWAITING KAI'S APPROVAL — nothing generated, zero credits spent.**
Plate filenames below are relative to
`/mnt/d/badcode-videos/gitpush-origin-master/clips/plant-room/recut-plates/`.
Method: [`../../../video-fx/hybrid-method.md`](../../../video-fx/hybrid-method.md).
Phrasing craft: the `flow-prompt` skill and [`../../../flow/video-prompting.md`](../../../flow/video-prompting.md).
Shot judgement: the `shot-craft` skill and [`../../../cinematography/motion-and-cutting.md`](../../../cinematography/motion-and-cutting.md).

## Standing settings for every roll
- Flow project `5743b21a-7288-49c6-9c11-b2bc9f7b87b4`. Aspect **16:9**. Output to the open
  Premiere project's `clips/plant-room/`.
- **Model: Veo 3.1 Fast on every beat.** Not Quality. Measured on GPOM scene 0 (2026-08-21):
  on shots whose job is *rigidity*, Quality spends its extra capability inventing components
  the plate did not contain. Fast invented nothing on the same prompt. Quality is for shots
  where something has to move and be beautiful; none of these are that.
- **Plate goes in as `startImage`. Motion only in the prompt.** No look words, no atmosphere words.
- **Audio: Veo will generate some. We strip it in Premiere.** Narration and siren are laid separately.

## The two clauses that appear in every prompt, and why
**1. The lock.** *"The camera is locked on a tripod and does not move, pan, tilt, zoom or drift."*
Silence is not a request for stillness — Veo invents a move if you leave it unstated. Saying it
does not produce a locked frame either (every take still creeps 34–66px over 8s), but it sets the
upper bound, and Premiere crops the residue.

**2. The rigid clause.** *"Every structure in the frame is rigid and bolted in place: it holds its
exact shape and position and does not shift, slide, hinge or deform, and no new object ever
appears, grows or disappears anywhere in the frame."*
This is the measured fix for Veo's regeneration bug — the one clause that stopped invention dead
on GPOM scene 0. 🔴 Note it never says *"rotate"* on a beat where something is meant to rotate
(B1's fan, B5's needles): a contradiction gets resolved by the model picking one, and it may pick
the wrong one.

⚠️ **Subtraction is the wrong reflex on these.** The usual rule is "cut a clause when a shot isn't
landing" — that holds for competing *actions*, not for an underspecified frame, where cutting made
it measurably worse.

---

## 🔴 Five places the plate does not match the motion plan
Found by looking at the plates, 2026-08-27. Each needs a call before the roll.

| # | The plan said | The plate actually shows | Recommendation |
| --- | --- | --- | --- |
| B1 | a fan turning behind the louvre grille | **no fan.** Behind the slats: amber server LEDs and a lit interior corridor | Roll BOTH prompts below at count 1 each — the fan is new geometry inside the one shot carrying the film's text |
| B2 | LED storm on *both* rack faces | only the **left near rack** has LEDs; the rest are dark mesh and solid doors | Animate what is lit. Naming dark faces invites Veo to light them |
| B3 | a service lift descending on a rail | **no lift — but there is already a tiny yellow forklift** on the floor far below | Move the forklift. It is real, it is small, and it delivers the scale for free |
| B4 | a chart recorder pen moving | **no chart recorder** in the room | Dropped. Lamps + wall meters carry it |
| B7 | vent plumes rising from stacks | cooling towers emit **nothing** — but a **gas flare is already burning** mid-frame | Flare is free and real. Plumes are mild invention; kept, but ranked second |

---

## C0 — the 2032 card · 2s · **no Veo roll**
ffmpeg only. `drawtext` types `2032` character by character in cut 2's green phosphor, huge and
centred, block cursor; `frei0r=scanline0r` + `glow`; keyboard click per character. Premiere's API
cannot write a string at all, so this cannot be done there.

---

## B1 — the voltage sign · 8s · Fast · **count 1 on each of two prompts**
**Job:** establish, and pay gate 2 — the cost is on the skin of the building.
**Highest text risk in the scene.** DANGER OF DEATH / 132,000 VOLTS / SITE DEMAND 400 MW is the
whole point of the shot, and Veo re-letters text as a matter of course.

### B1-fan (Kai's approved roll — the ambitious one)
> The camera is locked on a tripod and does not move, pan, tilt, zoom or drift. Deep in the darkness
> behind the metal louvre slats, a large industrial fan blade turns slowly and steadily. In front of
> it the rows of small amber indicator lights flicker in an irregular, busy pattern. The sodium lamp
> at the upper left holds a steady warm glow. Everything else in the frame is completely still. The
> louvre slats, the corrugated metal wall, the two signs and their mounting bolts are rigid and
> bolted in place: they hold their exact shape and position and do not shift, slide, hinge or
> deform, and no new object ever appears, grows or disappears anywhere in the frame. Maintain the
> text on both signs exactly as it is, unchanged and legible, for the entire clip.
> (no subtitles, no captions, no on-screen text)

### B1-lights (the safe one — no new geometry at all)
> The camera is locked on a tripod and does not move, pan, tilt, zoom or drift. Behind the metal
> louvre slats, the rows of small amber indicator lights flicker and blink in a dense, irregular,
> busy pattern, brightening and dimming out of step with each other. The sodium lamp at the upper
> left holds a steady warm glow. Everything else in the frame is completely still. The louvre slats,
> the corrugated metal wall, the two signs and their mounting bolts are rigid and bolted in place:
> they hold their exact shape and position and do not shift, slide, hinge or deform, and no new
> object ever appears, grows or disappears anywhere in the frame. Maintain the text on both signs
> exactly as it is, unchanged and legible, for the entire clip.
> (no subtitles, no captions, no on-screen text)

**Guarding against:** re-lettered signs (kills the beat); the slats hinging open like doors — Veo's
known near-field-parallax failure, which is why the camera must not move; an invented fan
redrawing the grille.
**Chaining:** none. 8s beat, 8s clip.
**On top in Premiere:** hold 1.5s, then the eased 3-layer parallax push (sign / grille / interior
dark) arriving on the black slot, which becomes the cut to B2. `Volumetric Rays` light position
keyframed so the sodium glance travels the slats. `Camera Shake` Master ~10.

---

## B2 — the rack aisle · 5s beat · generate **6s** · Fast · count 1
**Job:** we are inside, contained, silent.
> The camera is locked on a tripod and does not move, pan, tilt, zoom or drift. The rows of small
> amber and green indicator lights on the mesh cabinet door at the left flicker and blink in a
> dense, irregular, busy pattern, as if the machines are working hard. A few pinpoint lights on the
> cabinets further down the aisle blink out of step with them. The long ceiling light strip and the
> lit floor grating hold perfectly steady. Everything else in the aisle is completely still. The
> cabinets, mesh doors, cable trays, handles and floor grating are rigid and bolted in place: they
> hold their exact shape and position and do not shift, slide, hinge or deform, and no new object
> ever appears, grows or disappears anywhere in the frame.
> (no subtitles, no captions, no on-screen text)

**Guarding against:** cabinet doors swinging open — measured three times on this exact shot class,
and no wording ever fixed it; a locked camera is the fix. Also the mesh doors moiré-crawling.
**Chaining:** none.
**On top:** tiny push, `Camera Shake` ~10, grain in shadows.

---

## B3 — the vertical hall · 9s beat · **8s + chained 2s** · Fast · count 1
**Job:** scale. The canyon goes down out of sight and a whole forklift is a speck.
> The camera is locked on a tripod and does not move, pan, tilt, zoom or drift. Far below on the
> floor of the hall, the small yellow forklift truck drives slowly along the aisle, travelling a
> short distance and no further. Across the tiers of racks, thousands of tiny amber and green
> indicator lights blink in an irregular pattern. The ceiling light strips, the white light wells
> and the steel handrail in the foreground hold perfectly steady. Everything else in the hall is
> completely still. The racks, gantries, handrails, columns and light strips are rigid and bolted in
> place: they hold their exact shape and position and do not shift, slide, hinge or deform, and no
> new object ever appears, grows or disappears anywhere in the frame.
> (no subtitles, no captions, no on-screen text)

**Guarding against:** the tiers of near-identical racks regenerating — the single worst case in the
scene, and the reason the camera cannot move here at any price. The forklift is deliberately given
a bounded journey so Veo does not drive it out of frame and invent a replacement.
**Chaining:** yes. Pull the last frame (`flow_scene_save_frame position:"end"`), feed as startImage
for a 4s clip, take the first 1s+. Same prompt minus the forklift start-up. **Never pin an endImage.**
**On top: THE BIG MOVE.** `AE.Impact_Volumetric_Rays_FX` Light Position (param 7) keyframed
bottom → top, twice, exiting frame top. Frame-exact, our timing not Veo's.

---

## B4 — the control room · 9s beat · **8s + chained 2s** · Fast · count 1
**Job:** the instruments — analogue, obsolete, unmanned. The joke and the turn.
🔴 **"No people" is a negation and negations summon.** Measured 2026-08-18: naming what you don't
want puts it in the prompt. The empty room is therefore described **positively**.
> The camera is locked on a tripod and does not move, pan, tilt, zoom or drift. The room is empty
> and unattended and the console runs entirely by itself. Amber indicator lamps across the desk and
> along the back panels switch on and off in a slow irregular pattern, and the needles of the small
> square meters on the wall panels twitch slightly where they stand. The green fluorescent tube
> overhead holds a steady glow. The empty chair stands still. Everything else in the room is
> completely still. The consoles, switches, levers, dials, chair, doorway and ceiling tiles are
> rigid and bolted in place: they hold their exact shape and position and do not shift, slide, hinge
> or deform, and no new object ever appears, grows or disappears anywhere in the frame.
> (no subtitles, no captions, no on-screen text)

**Guarding against:** a figure walking in or appearing in the chair; the Cyrillic labelling being
re-lettered (cosmetic here — it reads as pattern, not as value — but it changes texture); switch
banks multiplying.
**Chaining:** yes, 8s + 4s chained, use ~2s.
**On top:** `AE.ADBE Strobe`, mode 0, colour BLACK, short duration / long period / random
probability = the dying fluorescent tube. Kept in post because it must be exact and reversible.

---

## B5 — the four gauges · 14s beat · **8s + chained 8s** · Fast · **count 2**
**Job:** the payload of the whole scene. Soil, happiness, water, birth rate, one by one into red.
🔴 **This is the beat most likely to come back unusable.** Four legible English name plates plus
fine tick marks is precisely what Veo re-letters. Kai's tolerance ("a sense of them moving is
enough") lowers the bar on the *timing*, not on the *lettering*.
> The camera is locked on a tripod and does not move, pan, tilt, zoom or drift. All four needles
> swing slowly and steadily anticlockwise, falling from the upper right of their dials down toward
> the red arc on the left. They move at slightly different speeds and drift rather than jump.
> Nothing else in the frame moves at all. The gauge bodies, black bezels, glass, screws, dial faces,
> printed tick marks and the four metal name plates are rigid and bolted in place: they hold their
> exact shape and position and do not shift, slide or deform, and no new object ever appears, grows
> or disappears anywhere in the frame. Maintain the four engraved name plates reading SOIL,
> HAPPINESS, WATER and BIRTH RATE exactly as they are, unchanged and legible, for the entire clip.
> (no subtitles, no captions, no on-screen text)

**Guarding against:** re-lettered plates; tick marks crawling; a fifth gauge appearing. Note the
rigid clause deliberately omits *"rotate"* here — the needles must rotate.
**Chaining:** yes, and 🔴 **approve clip 1 before rolling clip 2** — a chained clip inherits clip
1's broken lettering, so a bad clip 1 wastes two rolls, not one.
**Fallback if the labels break — and it is a good outcome, not a defeat:** cut the four needles as
PNGs and rotate them in Premiere on `AE.ADBE Motion` param 4 about a moved anchor (param 5).
Frame-exact, cannot re-letter anything, and lets us land each needle on its own narration line.
3% push over the beat.

---

## B6 — the red alert · 6s · Fast · **count 2**
**Job:** the bookend inside the scene — the same room, after. Kai overruled a post regrade for
this: *"not just add a red light, that's a bit lame."*
> The camera is locked on a tripod and does not move, pan, tilt, zoom or drift. An unseen rotating
> alarm beacon sweeps the room: the red light swells to a hard bright peak and falls back to a deep
> dark red roughly once a second, and the shadows across the console swing with it. Red indicator
> lamps along the back panels blink rapidly and out of step with the sweep. The room is empty and
> unattended. Everything else in the room is completely still. The consoles, switches, levers,
> dials, chair, doorway and ceiling tiles are rigid and bolted in place: they hold their exact shape
> and position and do not shift, slide, hinge or deform, and no new object ever appears, grows or
> disappears anywhere in the frame.
> (no subtitles, no captions, no on-screen text)

**Why count 2:** the difference between a sweep that reads as a rotating beacon and one that reads
as a slow fade is the whole beat, and it is not controllable by wording. Buy the choice.
**Guarding against:** the red drifting to orange or pink; the framing shifting away from B4's (they
are a matched pair and the bookend dies if the framing moves).
**Chaining:** none.
**On top:** 🔴 `photosensitivity` pass in ffmpeg before delivery — mandatory on any strobing or
alarm sequence. Siren J-cuts in 0.5s early under B5's last line.

---

## B7 — the reveal · 12s beat · **8s + chained 4s** · Fast · count 1
**Job:** first time outside. Ranks of identical towers stepping down to a dead horizon.
> The camera is locked on a tripod and does not move, pan, tilt, zoom or drift. The gas flare on the
> refinery in the middle distance burns and flickers with a small orange flame. Thin white vapour
> rises slowly from the tops of the cooling towers and drifts gently to the right. The amber lights
> on the tower walls hold steady, and the low red sun and the sky hold still. Everything built in
> the frame is completely still. The tower blocks, louvre panels, pipework, cooling towers,
> pylons, overhead lines and the concrete canal are rigid and bolted in place: they hold their exact
> shape and position and do not shift, slide, hinge or deform, and no new object ever appears, grows
> or disappears anywhere in the frame.
> (no subtitles, no captions, no on-screen text)

**Guarding against:** the receding rank of towers regenerating into different buildings; the near
tower's louvre panels hinging; the sun moving or blooming.
**Chaining:** yes, 8s + 4s.
**On top:** optional very slow push, grade, grain. The bookend is graphic, not a move — the near
tower's louvre wall answers B1's single louvre.

---

## Roll order when approved
B2 → B4 → B6 → B3 → B7 → B1 → B5.
Cheapest and least risky first, so the expensive lessons land before the two shots that carry the
scene's text. B1 and B5 last, deliberately.

**Credit shape:** 9 first-pass generations (B1 ×2 prompts, B5 ×2, B6 ×2, one each elsewhere), plus
4 chain generations, plus rerolls. Failed generations are refunded, so a policy block costs the
clock and not the balance.

---

# AS BUILT — 2026-08-27

**The scene is on the timeline.** `gpom-story.prproj` → sequence `gpom-s01`, track V1,
**83.56s → 149.44s (65.9s)**, against a 65s design. No gaps. Project saved.

| # | Clip on V1 | In | Out | Lane it ended up in |
| --- | --- | --- | --- | --- |
| C0 | `C0-POST-v1.mp4` | 83.56 | 85.56 | **ffmpeg** — `drawtext`, built from nothing |
| B1 | `B1-fan-1.mp4` | 85.56 | 93.56 | Veo, camera locked |
| B2 | `B2-aisle-1.mp4` | 93.56 | 99.56 | Veo, camera locked |
| B3 | `B3-POST-v1.mp4` | 99.56 | 108.56 | **ffmpeg** — locked plate, 515 procedural lamps |
| B4 | `B4-POST-v1.mp4` | 108.56 | 117.56 | Veo + **ffmpeg** reversed tail (8s → 9s) |
| B5 | `B5-POST-v2.mp4` | 117.56 | 131.44 | Veo + **ffmpeg** trim & optical-flow retime |
| B6 | `B6-POST-v1.mp4` | 131.44 | 137.44 | Veo + **ffmpeg** ping-pong |
| B7 | `B7-POST-v4.mp4` | 137.44 | 149.44 | **ffmpeg** — locked plate, procedural flare |

**Spend: 12 Veo generations, ~230 credits.** Six were usable. Everything else came from post.

## 🟢 What the camera-lock discipline bought

**Four of eight Veo clips came back at 0–2px of drift over their whole length**, against the
2026-08-21 baseline of 34–66px. The lock sentence plus the rigid clause is a real lever, and this
is the first time it has been measured on a whole scene rather than one shot.

The four that held (B2, B4, B5, B6) have **no hinge-able surface dominating the near field.**
The two that failed (B3, B7) do. That is §9's rule, confirmed on an independent shot pair.

## 🔴 Three variables tested on B3/B7, all non-levers

| Changed | Result |
| --- | --- |
| **Wording** — travelling objects deleted from both prompts | same slide, near-identical trajectory |
| **Tier** — Veo 3.1 Lite instead of Fast | same slide. **The tier is not the lever** |
| **Duration** — 4s instead of 8s | 🔴 **the SAME camera move, executed faster** (268px by 3.9s) |

🔴 **The duration result kills "chain in shorter segments" as a drift fix.** Veo performs the
move it has decided on inside whatever duration you ask for; a shorter clip is a faster move, not
a smaller one. Chaining still breaks the 8s cap — it does **not** bound a camera it has decided to
move.

⚠️ **`vidstab` is the wrong tool for cancelling a deliberate slow track.** With `smoothing=0`
`relative=0` it made B7 worse (up to 94px vertical). It smooths handheld shake; it cannot undo a
translation that carries real parallax, because the near field and far field move by different
amounts and no 2D transform fixes both.

## 🔴 B5's source recovers — caught late, and it matters

The needles fall into the red by **5.33s and then rise back out** over the remaining 2.7s. The
first read of the contact sheet missed it because the sampled frames straddled the turn.

That inverts the beat: the narration is *"one by one, the data points were turning red"*, and a
needle that touches red and recovers says the opposite.

**Fix, free:** keep frames 0–128 (the fall only), stretch 2.625× with `minterpolate`
(`mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1`) to fill the 14s beat. The needle now falls
slowly across the whole beat and **ends in the red and stays there** — a better button than the
original. Verified 0px drift, no interpolation artefacts on the thin needles.

**Always sample a needle/gauge shot densely enough to catch a reversal.** Five frames across 8s
is not enough when the motion is meant to be monotonic.

## The post recipes, in full

**B7 — locked plate, procedural flare (12s).** Flare at plate coords (623, 218). Luma-only gain
`1 + M*(0.62*FL - 0.36)`, where `M` is a two-term gaussian (σ≈14 core + σ≈40 glow) and `FL` is
three sines at 3.3 / 7.9 / 15.1 Hz so the flicker never visibly repeats. Amber tower lamps breathe
at 0.7 Hz with phase varying by position, masked on `gt(lum,150)*gt(cr,140)*gt(Y,200)` — the `Y`
term keeps the **sun** out of it. Then `noise=c0s=7:c0f=t+u`.

**B3 — locked plate, 515 procedural lamps (9s).** Rendered in numpy, piped raw to ffmpeg. Mask =
grey-opening top-hat (small bright features only, so ceiling strips and handrail are excluded by
construction) **∩ coloured** (`r-b > 12` or `g-b > 12` — the plate is blue-graded, so anything
warm or green is a lamp, not a structural highlight) ∩ blob size 2–60px. Each blob gets its own
random phase and rate (0.5–3.2 Hz); 40% snap via `tanh(4·sin)`, the rest breathe. Measured: LED
pixels change 16–21 levels, everything else 2 (grain).

**B4 — reversed tail, 8s → 9s.** Frames 164–191 reversed and appended, first frame dropped.
**B6 — ping-pong, never reaches black.** The Veo take swells to Y=74 at 1.25s and is **dead flat
at Y=18.3 from 3.25s onward**. Segment f12–f75 ping-ponged and looped: Y now runs
39 → 74 → 27 → 74 → 39 across the 6s. Two beacon sweeps, floor of 27.
Both rely on the standing rule that **blinking lights are time-symmetric**, so a reversal is
undetectable. Neither would be safe on settling matter.

**C0 — the 2032 card (2s).** DejaVu Sans Mono Bold at 280px, `#6EEB82`, x=636 y=418, advance
168.6px/char. Four `drawtext` layers on `gte(t, 0.20/0.42/0.64/0.86)` plus five `drawbox` cursor
positions, the last blinking on `lt(mod(t-0.86,0.72),0.44)`. Then `frei0r=glow:0.55`,
`frei0r=scanline0r`, a CRT mains flicker via `eq=brightness=…:eval=frame`, `vignette`, grain.
**Matched to cut 2's tube:** its terminal green peaks at G=247, the card at G=244.

## 🔴 Two ffmpeg `geq` traps, both cost a rebuild

| Trap | What it looks like | Rule |
| --- | --- | --- |
| **`format=gbrp` swaps the channels** | an `r=` expression lands on GREEN. Boosting a flame turned it lime, twice | **Modulate `lum` in `yuv444p`.** Hue cannot shift, because chroma is untouched |
| **`geq` does not clamp — it wraps** | luma above 255 wraps to near-0, punching **black speckles** into the brightest part of the thing you are brightening | **Always `clip(expr, 0, 255)`** |

## Still owed

- [ ] 🔴 **fps.** The sequence is **25fps**; every clip here is **24fps**. Premiere conforms for
      viewing, but the post builds should be re-rendered at 25 (free) and a decision taken on the
      Veo clips before delivery.
- [ ] B2 runs 6s against a 5s beat — trim 1s, or keep and re-budget.
- [ ] Veo-generated audio on A1, 83.56–128.56 (6 clips) — Kai removing by hand.
- [ ] The Premiere layer the plan always called for: B1's 3-layer parallax push, **B3's
      `Volumetric Rays` light climb (still the scene's biggest move, and still unbuilt)**,
      B4's `Strobe` dying tube, B7's slow push. None of this is on the timeline yet.
- [ ] `photosensitivity` pass on B6 before delivery.
- [ ] Grade pass across all 8.
- [ ] Fold this into `plant-room.md` and update `../prompts.md` §2c.

## Rejected but kept on disk
`B3-hall-1/2`, `B7-towers-1/2`, `B7-towers-LITE`, `B7-seg1` (the drift evidence — do not delete,
they are the measurement behind the §9 confirmation), `B1-lights-1` (blooms brighter than the
plate), `B5-gauges-1` (recovers out of the red), `B6-redalert-1` (dies to black),
`B7-POST-v1/v2/v3` (the two geq traps, in order), `B5-POST-v1` (retimed the recovery too).

---

## Amendment — 2026-08-27, the 2032 card holds a second longer

Kai opened a **0.88s beat of black** after cut 2's push-to-black (83.56 → 84.44) and asked for the
card to sit on screen a beat longer before the cut to B1.

**`C0-POST-v2.mp4` — 3s instead of 2s.** The card is entirely expression-driven, so the *only*
change is `-t 2` → `-t 3`: the typing beats stay at 0.20/0.42/0.64/0.86, the block cursor keeps
blinking on its 0.72s cycle through the extra second, and the CRT mains flicker and grain keep
running. **Nothing freezes** — a frame-hold would have read as a still. Measured: digits hold at
G=228–244 to 2.95s, cursor verified on at 1.60s/2.50s and off at 2.80s/2.95s. `setsar=1` added.

🟢 **The build is now a script, not a one-off:** [`scripts/gpom/build-c0-card.sh`](../../../../scripts/gpom/build-c0-card.sh)
— `build-c0-card.sh <out> <seconds>`. Duration is the only knob.

**Timeline as it now stands** (V1). Everything after the card moved **−3.44s**, closing the
working gap Kai had opened; the camera pushes survived untouched because their keyframes are
**clip-relative** (`docs/premiere/api-notes.md`).

| | Clip | In | Out |
| --- | --- | --- | --- |
| cut 2 | `s02-hong-kong.mp4` (push to black) | 55.72 | 83.56 |
| — | **black** | 83.56 | 84.44 |
| C0 | `C0-POST-v2.mp4` | 84.44 | 87.44 |
| B1 | `B1-fan-1.mp4` | 87.44 | 95.44 |
| B2 | `B2-aisle-1.mp4` | 95.44 | 101.44 |
| B3 | `B3-POST-v2.mp4` | 101.44 | 110.44 |
| B4 | `B4-POST-v1.mp4` | 110.44 | 119.44 |
| B5 | `B5-POST-v2.mp4` | 119.44 | 133.32 |
| B6 | `B6-POST-v1.mp4` | 133.32 | 139.32 |
| B7 | `B7-POST-v5.mp4` | 139.32 | 151.32 |
