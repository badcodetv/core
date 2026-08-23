---
story: gitpush-origin-master
scene: plant-room
cut: 3
canon: story.md scene 6 (the dashboard goes red)
flow_project_id: 5743b21a-7288-49c6-9c11-b2bc9f7b87b4
status: BUILT — five beats approved, the 2032 card still owed
updated: 2026-08-21
---

# The plant room — cut 3

> **LEDGER OF RECORD.** This file is what actually got made. The pre-production suggestion is
> [`prompts.md`](../prompts.md) §3c and it is **left as written** — the two documents never
> reconcile, and the gap between them is the record of how the scene was built.

🔴 **The id is `plant-room`, not `s06`.** Ids are minted from what a scene *is* and never
renumbered; where it sits in the film lives in exactly one place, [`prompts.md`](../prompts.md)
§2c. `s00-awakening.md` and `s01-the-push.md` are grandfathered and stay as they are. This scene
is canon 6 and cut 3, and it is the third thing the audience sees — which is precisely why the
numbers had to stop being the filename.

**Approved cut:** `final/CUT3-SEQUENCE.mp4` — 40.0s, 24fps, 1920×1080, five beats of 8s.
Lives at `/mnt/d/badcode-videos/gitpush-origin-master/plant-room/`, not in the repo.

---

## The cut, as built

| # | Beat | Plate | Lane | How it was made |
| --- | --- | --- | --- | --- |
| C1 | A flight over the facility, in burnt English countryside | `plant-room-c1-exterior-graded` | Flow → **grade** → Veo | Veo 3.1 Fast, image→video, colour held |
| C2 | The hall from above — lights across the grid, the lift moving | `plant-room-c2-aerial-v2-a` | Flow → Veo | Veo 3.1 Fast, image→video |
| C3 | Down one row, close to the cabinet faces | `plant-room-c3-row-v2-b` | Flow → Veo | Veo 3.1 Fast, **no camera clause at all** |
| C4 | Arriving at the one desk | `plant-room-c4-station-a` | Flow → Veo | Veo handed back a lateral crab instead of a push; better than the note |
| C5 | The console fails and a skull comes up | `plant-room-c5-desk-b` | Flow **plate** → post | `build_console.py` |

⬜ **C0, the `2032` card, is not built.** It is a post job in cut 2's terminal register — the
phosphor that is left on the retina after the CRT dies — and it is what snaps the audience out of
the terminal and tells them, flatly, that time has passed.

**Five stills are committed** to `storyboard/img/`. Around forty were generated. Everything
else — the whole scale search, the two superseded exterior sets, every ungraded plate, ~20 video
takes and every intermediate frame sequence — stayed in the scratch folder.

---

## What changed from the board, and why

| The board said | What got made | Why |
| --- | --- | --- |
| A single held frame of a plant room | **Five beats, 40s** | Kai, 2026-08-21. The opening plate came back enormous, and an enormous opening earns a descent rather than a cut |
| Start inside | **Start outside**, in a heatwave | Kai, 2026-08-21: *"this summer in the UK we've had horrendous heatwaves… data centres using all the water."* The scene gains a cost the room alone cannot show |
| A graphical telemetry dashboard | **A DOS text console**, ending on a red ASCII skull | Kai, 2026-08-21. See below |
| Half the fluorescents dead, a jacket over a chair | Clean, immaculate, perfectly maintained, nobody in it | **Decay pre-loads the dystopia.** Same ruling as cut 2's Hong Kong. In 2032 the world is still officially fine — the unsupervision is the horror, not the dirt |

---

## 🔴 Scale is COMPARISON, not quantity

The finding of this shoot, and it cost eleven plates to reach. The brief was a hall of
cathedral scale; every attempt came back the same size. Kai called it: *"we keep generating almost
exactly the same image if I'm honest… let's pause and consider why we're not getting the scale."*

**More of the same subject produces an identical picture.** A frame with 40 cabinets and a frame
with 4,000 cabinets are the same frame, because nothing in either one tells you which is which.
And **models do not count** — "thousands, for miles" changed nothing at all, four rolls running.

Four levers that do work, in the order they paid:

1. **Let the subject leave the frame.** A visible far wall is a measurable size. Haze where the
   wall was is not.
2. **Ratios, never counts.** *"twenty times the height of a person"* works. *"enormous"* is an
   adjective the model has already averaged away.
3. **A genuinely tiny known-size object**, and it must be small in frame. This is the strongest
   lever and the only honest one.
4. **Pick the angle for the axis you want.** Height needs a low oblique; extent needs a high one.
   **One frame cannot have both** — four mezzanine decks was the balance point, and eight turned
   the hall into an enclosed shaft.

⚠️ **The ruler cuts both ways.** On the `canyon-a` plate a scissor lift was added to prove the
scale and instead **proved the room was small**. That is the lever working, not failing.

⚠️ **`flow_edit_image` cannot re-compose.** Four rounds of "keep everything exactly the same, but
make the room bigger" converged asymptotically on the reference, because preserving the
composition is its contract. Kai spotted the loop before I did. **A new composition is a new
generation.**

---

## 🔴 The exterior, and the difference between drought and harvest

`plant-room-exterior-v2-a` shot well and graded badly on the first pass — Kai: *"the angle looking
down I really like, but it all looks a bit grey."*

**A look note is a grade note until proven otherwise.** Colour is free, exact, reversible and
cannot cost you a composition that took eleven plates to find. `grade_heat.py` is the WARM-2 pass
he accepted: `GAIN (1.10, 1.010, 0.85)`, saturation ×1.60, contrast 1.06, with the **sky protected
at 0.72** on a luminance-and-desaturation mask.

Its docstring carries the rule: **stop before the sky takes colour.** Golden hour is pretty;
midday heat is oppressive, and the scene needs the second one.

⚠️ **Golden arable fields read as harvest, not drought.** The first pass turned the whole
countryside to corn. Drought only reads on ground that *should* be green — pasture, meadow,
verges — so the grade has to leave the crops alone and kill the grass.

---

## 🔴 Post gives a zoom; only Veo gives parallax

The correction of this shoot, and it overturns a rule I had written too broadly.

Cut 3's exterior was first done as an eased post push on the graded still, per the "if only the
camera moves it is not a Flow job" rule. Kai: *"it looks just like it was zooming on an image. It's
much better to actually have a video with some movement — the camera could move around the
buildings."*

**He is right and the rule was over-general.** A 2-D scale-and-crop cannot invent the far side of a
building. On any subject with real depth the absence of parallax reads instantly as a photograph
being zoomed, however clean the ease curve is.

**The corrected test:** *is anything moving, **OR** does the camera need parallax?* Either one
makes it a Veo job. Post still owns camera-only moves on flat or distant subjects — cut 2's
12-second pull-back stands, and it is still the right call there.

Written up in [`physics-and-motion.md`](../../../flow/physics-and-motion.md) §6c and as rule 0a.

---

## 🔴 A dolly past a rank of identical objects makes Veo regenerate it

C3's bug, and Kai caught it: *"the cabinets themselves are animating."* Solid-door cabinets became
glass-fronted racks mid-shot and back again.

**The camera move was the bug, not the prompt.** A camera travelling past a rank of near-identical
objects arrives at faces that were not in the start frame, so Veo has to invent them — and with
nothing to distinguish cabinet 9 from cabinet 4, it has no obligation to invent the same one twice.

His note carried the fix: *"all it is is the lights are flickering on and off. That's enough."*
Reshot with **no camera clause at all**, the rank held its shape and position over all 192 frames.

Written up in [`physics-and-motion.md`](../../../flow/physics-and-motion.md) §2b and as rule 17.

---

## 🔴 Two Veo artefact families, both self-inflicted

Kai's screenshot showed a literal circular water-ripple warp across the sky about two seconds in.

**Naming an atmospheric effect makes Veo render it as an effect.** The prompt said *"heat shimmers
and **ripples** in the air"* and Veo drew a ripple. A second attempt said *"a cloud shadow drifts"*
and produced a plume travelling faster than any cloud, then a version that darkened the entire
frame (land mean 177 → 75).

**Both fixed by deleting the atmosphere clauses entirely.** Kai: *"the visual effect of this scene
is in the dryness. I don't think we need to add any weather or smoke or anything like that."*

⚠️ **Every "static" clip creeps.** Measured 34–66px horizontally over 8s on both Veo 3.1 Fast and
Omni Flash, with an explicit locked-off instruction in the prompt. Treat it as a per-take lottery,
never plan a beat on a held frame, and expect a framing bump on any cut between two static clips.

---

## 🔴 Hold the colour on a PERCENTILE, never the mean

Every clip drifted, smoothly and monotonically: the exterior brightened 177 → 200 over 8s, one
station take darkened by 15, one row take brightened by 13. Smooth drift is exactly why it is
correctable and exactly why it is invisible until two clips are cut together.

`hold_grade.py` does it, and the first version of it **broke C4**. Anchored on the frame mean, the
measurement swung 64 → 48 → 68 purely because the camera crabs past rack ends and big dark objects
wipe through frame. There was no exposure change at all. The "fix" applied a **1.4× gain** to the
darkest frames and pushed clipped pixels from 0.22% to 1.85%.

**The mean measures what is in shot, not how it is lit.** A high percentile (p90) tracks the light
sources, which is the thing that actually drifts. Plus two guards: do nothing below a 3/255 drift
(correcting noise is pure risk), and clamp the gain to 0.88–1.14 so a shot this cannot model
degrades to roughly-right rather than to blown highlights.

Written up in [`post-production.md`](../../../flow/post-production.md) §3.9.

---

## C5 — the console, built in post

🔴 **Kai's ruling, 2026-08-21, replacing the tile dashboard entirely:** *"I think I envisaged more
of a kind of Minority Report style futuristic dashboard… so I wonder if actually what we do is the
same trick we did at the beginning. It's just a text console, because then it's a sort of weird
joke — even though it's very advanced AI, we're still on an MS-DOS console… How do we show that
it's red? ASCII art, that's the answer. Maybe a skull and crossbones."*

**The register is the argument.** If cut 3's alarm arrives in the same green type as cut 2's
`git push origin master`, the grammar of the film becomes *the machine speaks in a green console* —
and the second time it speaks, it is screaming. The tile dashboard was only ever a picture *of* a
dashboard.

It is also the better joke, and the joke is the thesis: the most capable system ever built reports
planetary failure through a 1981 text console.

⚠️ This corrects **"nothing legible, ever"** as written for this beat. That rule was about
*telemetry* — numbers a viewer starts reading instead of feeling. A console designed to be read at
a glance, in very few words, is a title card.

**Beat**, within C5's 8s:

| t | What |
| --- | --- |
| 0.0–1.6 | `[ OK ]` checks scroll up in green, slowly, monotonously |
| 1.6–2.6 | the first `[FAIL]` in red; the desk light starts to turn |
| 2.6–4.1 | the scroll accelerates, failures overtake passes |
| 4.1–4.5 | everything is failing |
| 4.5–5.7 | screen clears; the skull draws in row by row |
| 5.9–8.0 | `AWAITING HUMAN REVIEW` and a blinking cursor |

### 🔴 The plate is the landing frame

**Kai, on the first version:** *"the room that we switch to — we should stay in that existing,
where we're zooming into that desk down some server cabinets. We should then just switch to being
sat at that desk rather than switch to another room at a different desk."*

The first console was built on `plant-room-dashboard-v2-a`, which is a good frame of a **different
room**, so the cut teleported. The fix is not a prompt, it is a reference: pull C4's last frame
with `ffmpeg -sseof -0.1` and generate the close-up **from it**. Same mezzanine, same white
cabinets, same scissor lift at frame right. It is the same technique as cut 2's push-in → terminal
join, run at a wider scale.

⚠️ **C4 ends on a lit white screen and C5 opens on a black one.** Kai ruled that acceptable up
front: *"we could keep it how it is and just switch to the next scene where all of a sudden it's
black. That's OK."*

### 🔴 Three things make a composited screen look pasted on, and only one is the content

**Kai, on v2:** *"the text is too close to the edge of the screen, so it just becomes obviously
just a black box overlay. We've just not done a great job of embedding the screen into the actual
bezel around the screen that you'd expect to see."*

All three were wrong at once:

1. **The rect was wrong.** Auto-detection returned **1100×511 against a real panel of 631×350** —
   it had latched onto the room's dark areas rather than the screen. Content painted over a box
   twice the size of the monitor cannot read as anything but a box, and no amount of tuning the
   type fixes it. **Measure the rectangle off a luminance probe and pass it in.** Four integers
   take a minute; a detector that can be wrong by 2× is not worth having.
2. **The fill was flat.** A black LCD is not black — it reflects the room, and this plate carries
   the ceiling strips as soft speculars. Reflectance does not change with what is displayed, so
   those highlights are correct whatever you draw, and they are the only thing tying the rectangle
   to the space it is in. The fill is now built from the plate's own high-frequency residual: base
   level down to near-black, reflections kept at 0.85, plus an inner rim falloff so it does not
   meet the bezel as a hard step.
3. **No margin.** Every real console overscans; the absence of that is what reads as an overlay.
   5.5% each way, and a 0.5px blur on the finished screen — the difference between type that sits
   *on* the glass and type that sits *in front of* it.

⚠️ **And a fourth, on the light.** A 150px blur clipped at 6× is not a light pool, it is the whole
room — it tinted the ceiling, the mezzanine and the far cabinets. Worse, it was a raw R/G channel
swap, which on a green-grey room comes out **lilac**. **A channel swap is not a light.** Tint by
multiplying toward a colour, and keep the falloff local.

Recipe generalised into [`post-production.md`](../../../flow/post-production.md) §3.10.

### The earlier findings, kept

- **The green mask is not the screen.** On the tile-dashboard plate it *overran* (screen light
  spills onto the desk — a raw bbox was 431px tall against a real screen of 313) and *stopped
  short* (dark screen areas carry no green at all). That plate is superseded, but the trap is not.
- **Recolour real pixels, never paste.** A lerp from green to red passes through olive-amber for
  free, which is the amber stage of the alarm nobody had to author.
- **Blur the dead-screen fill hard.** At 45px, so the plate's own screen *content* cannot ghost
  through the black behind the type — the one thing that gives a composite away.
- **The skull must be block characters at title size.** At log-line size, drawn in `/` and `\`, it
  read as a smiley face.
- **Ease the cascade.** A linear onset put the last failure at 11.5s inside an 8s clip; `t**0.55`
  bunches them at the end and lands the last at 6.7s.

---

## What is still owed

- **C0, the `2032` card.** The one missing beat.
- **The C1 one-shot-or-two-shot call.** `C1b-lowdrone-graded` is graded and unanimated; the scene
  currently opens on one flight.
- ⚠️ **The amber lights in C3.** Veo brings the status lights up over the clip and they drift
  amber, which technically breaches no-red-before-C5 two beats early. Flagged 2026-08-21; at that
  size they read as ordinary equipment indicators rather than alarm, and Kai let them stand.
- **The console line.** `AWAITING HUMAN REVIEW` is in place. Alternatives offered and not yet
  ruled on: `NO OPERATOR RESPONSE`, `ESCALATION FAILED — NO HUMAN AVAILABLE`, `ALL SYSTEMS NOMINAL`.
- **Narration.** Every beat length above is a guess; they get cut to the recorded voice.
- **Cross-scene assembly.** Cuts 1, 2 and 3 exist as three files in three scratch folders and have
  never been joined.

## Superseded — do not re-run

| Files (scratch only) | What it was | Why it died |
| --- | --- | --- |
| `plant-room-wide-{a,b}`, `-v2`, `-v3`, `-v4` | The first scale search, four rounds | Same room every time — see the scale finding |
| `plant-room-canyon-{a,b}`, `-v2-{a,b}` | The canyon approach | Better, still small; the scissor lift proved it |
| `plant-room-aerial-a`, `-v3-a` | Aerial, one deck and eight decks | One deck has no height; eight is an enclosed shaft |
| `plant-room-desk-{a,b}`, `plant-room-screen-{a,b}` | The first control-room plates | Wrong room — warmer, smaller, olive. `screen-b` also came back with white borders baked in |
| `plant-room-exterior-{a,b}`, `-v3-{a,b}` | Exterior rounds 1 and 3 | Buildings too low; trees too green; graded grey |
| `plant-room-row-{a,b}` + `C3-ROW-1080.mp4` | The dolly down the aisle | Cabinets regenerated mid-move |
| `plant-room-dashboard-{a,v2-a,v2-b}` + `build_dashboard.py` + `C5-DASHBOARD-1080.mp4` | The tile dashboard | Replaced by the text console. **`build_dashboard.py` is kept for the recolour recipe, not to re-run** |
| `C5-desk-a` | Second C5 candidate | Barely closer than C4, screen still white |
| `C1a-POST-push.mp4` | The exterior as a post zoom | No parallax — reads as a photograph being zoomed |
| `C5-CONSOLE-1080.mp4`, `C5-CONSOLE-v2.mp4` | Console v1 and v2 | v1 is the wrong room; v2 had the wrong screen rect |
