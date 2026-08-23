---
story: gitpush-origin-master
scene: 1
canon: story.md scenes 1-4 (the commit log · the log of the species · HEAD · the push)
flow_project_id: 7d3fafe4-36f3-4fbc-ba71-6c4c4d11b32f
status: shape approved, terminal register unbuilt
updated: 2026-08-21
---

# Scene 1 — Hong Kong and the push

> **LEDGER OF RECORD.** This file is what actually got made. The pre-production suggestion is
> [`prompts.md`](../prompts.md) §3b and it is **left as written** — the two documents never
> reconcile, and the gap between them is the record of how the scene was built.

**Approved cut:** `s01-ROUGH-MODERN.mp4` — 21.0s, 24fps, four beats.
Lives at `/mnt/d/badcode-videos/gitpush-origin-master/s01/final/`, not in the repo.

🔴 **This is an approved SHAPE, not a finished scene.** The terminal register — the commit log of
the species, `HEAD`, and the command typing itself — is not built. It is a post job composited onto
the plate, and it is the entire payload of canon scenes 2–4.

---

## What changed from the board, and why

| The board said | What got made | Why |
| --- | --- | --- |
| A grimy Hong Kong canyon, wet neon, derelict internet cafe | A **modern, prosperous** Hong Kong; a clean glass tower; a clean modern office floor | Kai, 2026-08-21. **Grime pre-loads the dystopia.** The point of scene 1 is that the world looked completely fine when the command got typed — a derelict city tells the audience the collapse already happened before the film has earned it |
| Six beats (city · shopfront · cafe interior · CRT at desk · HEAD · the push) | **Four** beats to the plate | The office shot already holds the CRT at mid distance, so the separate desk-distance beat was redundant |
| The CRT is one dead machine among many in a dead room | The CRT is **the one thing that does not belong** in a working modern office | A consequence of the modern ruling, and a better image: the command that ends the world gets typed on a machine nobody bothered to replace |
| B1 is a Veo job because the city moves | Correct, **and Veo handed us a camera move we could not prompt for** | See "The descent, free" below |

**Unchanged from the board:** the two traps held. Nothing was pushed through the interior (every
join is a cut), and no signage in any frame carries legible lettering.

---

## The cut, as built

| # | Beat | Source | Length | How it was made |
| --- | --- | --- | --- | --- |
| B1 | Descent into the city | `s01-hk-modern-b.jpg` | 8.0s | Veo 3.1 Fast, image→video, **reversed in post** |
| B2 | One lit floor in a black tower | `s01-tower-ext2-b.jpg` | 3.5s | ffmpeg — eased 1.07× push on the still |
| B3 | The office floor, and the one old machine | `s01-office-int-a.jpg` | 4.5s | ffmpeg — eased 1.06× push on the still |
| B3b | Push in to the CRT | `s01-office-int-a.jpg` | 8.0s | Veo 3.1 Fast, image→video, **screen killed in post** — `build_screen.py` |
| B4 | The terminal | B3b's **last frame** | 8.3s | Built in post — `build_terminal.py` |

**The push-in's landing frame IS the plate.** Rather than cut from the office to a separately
generated close-up — a different monitor in a different room — the push-in was shot and its last
frame extracted as `plate-1080.png`. The type composites onto the exact frame the move lands on, so
there is no join to hide. It is the scene-0 chaining technique run forwards instead of reversed,
and it retired `s01-crt-close-b.jpg` — which was **removed from the repo** on that basis. It was a
good plate and it made no frame of the film, and the rule is that only stills which reached the cut
are kept.

**Three stills are committed** to `storyboard/img/`: `s01-hk-modern-b`, `s01-tower-ext2-b`,
`s01-office-int-a`. Sixteen were generated. Everything else — the grimy set, the failed tower
exteriors, the retired close-up, 14 video takes and every intermediate frame sequence — stayed in
the scratch folder. Everything else — 12 video takes, 14 stills,
the superseded grimy set — stayed in the scratch folder.

---

## The plates

All Nano Banana Pro, 16:9, 1376×768. Prompts as sent are in [`prompts.md`](../prompts.md) §3b for
the superseded grimy set; the modern prompts that actually shot are below.

### B1 · `storyboard/img/s01-hk-modern-b.jpg`

Picked over candidate `-a`, the Victoria Harbour panorama from the Peak — which is the postcard
shot. This one sits *among* the towers with the harbour behind, and its foreground grid of lit
office windows **keeps the circuit-board rhyme with scene 0**, which opened on two blinking LEDs
on a board.

```prompt
Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation. A high wide night view over a modern Hong Kong: clean contemporary glass and steel towers rising in ordered ranks above the harbour, their facades lit evenly from within by office and apartment lighting in cool white and pale blue. The calm black water holds the reflections in long steady columns; a few small ferries move across it leaving clean wakes. Everything in frame is well-maintained, orderly and prosperous — no grime, no decay, no rust, no rubbish, no peeling surfaces, no dereliction, no visible poverty. Clear air and good visibility, a faint band of cloud lit from below by the city. Any signage is small, distant and its lettering illegible. Vast still composition, precise man-made geometry, deep clean blacks in the sky. No readable text, no logos, no fantasy effects.
```

### B2 · `storyboard/img/s01-tower-ext2-b.jpg`

**A first attempt was thrown away for framing defects, not content.** Prompted as "looking up from
a clean modern street at a tower", Flow returned one candidate with dark vertical mattes baked down
both sides and one as a **portrait image centred on a white 16:9 background**. The re-roll below
fixed it by framing horizontally across a neighbouring rooftop instead of looking up, and by adding
*"no borders, no letterboxing, no white margins"*.

```prompt
Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, wide horizontal landscape composition filling the whole frame edge to edge. A modern Hong Kong business district at night, photographed straight across from a neighbouring rooftop: the dark glass curtain-wall flank of a contemporary office tower runs across the frame, its floors almost entirely unlit and black. One single floor, low in the frame, is still lit from within — a long unbroken horizontal band of pale interior light, the only lit thing in the whole picture. Clean precise horizontal floor bands and mullions, well-maintained modern architecture, no grime, no rust, no decay, no dereliction. Beyond and below, other dark towers and a scatter of small distant city lights. No people. Any signage is small and its lettering illegible. Calm static observational framing, deep clean blacks. No borders, no letterboxing, no white margins. No readable text, no logos, no fantasy effects.
```

### B3 · `storyboard/img/s01-office-int-a.jpg`

The desks form a U receding to the single lit screen — **the orbital server-hall aisle from scene 0,
rebuilt clean.** The machine's room and the human room are the same shape, and neither of them
needed saying out loud. Picked over `-b`, which was cooler and read at dusk, so the CRT stopped
looking like the light source.

```prompt
Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation. The interior of a clean modern open-plan office floor at night, high up in a glass tower: two orderly rows of tidy white desks receding down a central aisle, each carrying a slim modern flat-panel monitor, every one of them dark and switched off. Grey carpet tiles, pale walls, a floor-to-ceiling window at the far end showing the lit city far below. The overhead lighting is off. In the middle of the frame, on one desk, sits a single old beige CRT computer monitor that does not belong with the others — it is switched on and glowing dark green, and it is the only light source in the room, picking out the nearest desk edges, a keyboard and a strip of carpet before everything falls away to deep unlifted black. The room is well-kept and modern — no grime, no rubbish, no decay, no clutter. No people. Calm static observational framing, precise geometry. No readable text on any screen, no logos, no fantasy effects.
```

### B4 · `storyboard/img/s01-crt-close-b.jpg` — **THE PLATE**

🔴 **Generated deliberately EMPTY.** B4, B5 and B6 are one locked-off monitor with different text on
it. A baked-in line would have given us a single frame and nothing to animate; an empty phosphor
field lets post own every glyph — the scroll, the acceleration, the slam-stop on *the model*, the
typing.

**The wording that got an empty screen, 4/4 candidates across two prompts:** enumerate the kinds of
mark, do not just say "blank" — *"absolutely no characters, no cursor, no writing, no icons and no
markings of any kind anywhere on it."*

Picked over `-a`, whose screen bled off the top and bottom of frame. This one keeps **all four
screen corners inside the frame**, which is what post needs to corner-pin onto.

```prompt
Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation. An old beige CRT computer monitor photographed from very close and dead straight on, square to the glass, so that the screen fills almost the entire frame and only a thin border of the scuffed beige casing is visible at the edges. The monitor is switched on and the screen is completely blank — an even dark green phosphor field with faint horizontal scanlines and gentle glass curvature, absolutely no characters, no cursor, no writing, no icons and no markings of any kind anywhere on it. Faint dust and fingerprints on the glass, a soft even green glow, a slight vignette toward the tube corners. The room behind is unseen. No people. Locked-off static camera, perfectly level and centred, calm and observational. No text anywhere in the image, no logos, no fantasy effects.
```

---

## The descent, free

The B1 take came back doing a slow smooth **crane upward** — not what was asked for, and no
deformation anywhere: the towers hold their shapes across all eight seconds. Wrong direction,
though. We have just come down from orbit at the end of scene 0, and rising again fights the
arrival.

**So it was reversed.** It is now a slow descent into the city, which is the move that was wanted
and could not be prompted for.

Reversal safety checked per [`post-production.md`](../../../flow/post-production.md) §2: the ferries
trail proper wakes when run backwards and read correctly at this scale, cloud drift and window
twinkle are direction-agnostic, and there is no smoke, dust, spark or drifting particulate in frame
to give it away.

```bash
ffmpeg -i s01-b1-hk-modern-a.mp4 -vf "reverse,scale=1280:720,fps=24,setsar=1,format=yuv420p" \
  -an -c:v libx264 -crf 20 -y n1.mp4
```

## 🔴 Veo animates what the plate gives it something to animate

The finding of this shoot, and it arrived as a correction.

The **grimy** night-alley plates would not move at all. Five takes, three plates, two prompt
strategies — one figure walked, and nothing else in any of them. Rain never appeared, twice, even
after it was named first and hard. The first reading was "Veo will not animate these plates."

The **modern** harbour plate moved immediately and well on the first attempt: ferries tracking with
visible wakes, thousands of windows twinkling, the water surface breaking and reforming, cloud
drifting. Same tier, same settings, same prompt shape.

**So it is not the tool, it is the plate.** Open water, distant traffic, cloud, and a large field of
small lights are all things Veo will move. Fine particulate — rain — on a dark, dense, high-detail
alley is not.

⚠️ A related trap that nearly hid this: **over-locking the camera freezes the world.** The first
prompts stacked *"no pan, no tilt, no zoom, no drift… nothing else moves at all"* and Veo froze the
entire clip, subject included. Name the moving thing first and hard, then lock the camera.

## ⚠️ Two measurement errors, both worth keeping

1. **`ffmpeg -ss` before `-i` is a fast seek and snaps to the nearest keyframe.** Two samples 0.2s
   apart returned *the same frame*, so every clip looked frozen. Put `-ss` after `-i` when
   measuring motion. The verdict happened to survive the corrected run, but B1 was nearly
   mis-scored as dead.
2. **The concat runaway.** Veo returns 24fps; ffmpeg's still-derived clips default to 25fps. Mixed
   in the concat *filter* it does not error — it produces an ever-growing file. This 21-second
   sequence reached **628MB and 105 minutes of CPU** before it was killed, while every one of its
   inputs was correct and under 4MB. Written up as
   [`post-production.md`](../../../flow/post-production.md) §3.6.

---

## 🔴 The monitor is OFF until we arrive

**Kai, 2026-08-21, on v1:** *"I was hoping just that the screen would be black, it would then turn
on to see green letters — that's what I meant by green screen."*

A genuine crossed wire, and worth writing down because it will recur: **Flow renders the CRT as a
flat chroma-key fill**, which is exactly what makes it keyable and is *not* something that should
ever survive to screen. v1 replaced it only during the terminal beat, so for the first twenty
seconds the film showed a monitor displaying nothing but chroma green.

`build_screen.py` walks every frame of the push-in, keys the fill, and turns the tube off — and the
room's green cast comes down with it, because the office is lit by that monitor.

### 🔴 Veo ANIMATES the screen brightening, which broke the first two attempts

The finding, and it took a second round of Kai's notes to surface: **the screen's saturation climbs
about 9× across the push-in.** At frame 1 it is a dim desaturated green; by frame 60 it is fully
saturated chroma. Measured:

| Frame | Fixed threshold caught |
| --- | --- |
| 0–40 | **0%** |
| 60 | 33% |
| 90 | 75% |
| 150 | 94% |

**A partial key on a flat fill is a ragged green blob**, which is exactly what it looked like. Two
rules came out of it, and the first version broke both:

1. **Soft key, on a ratio, with per-frame thresholds.** No fixed threshold can work when the thing
   you are keying changes by 9× while the room's own faint cast stays put. So the bounds are derived
   from each frame's own distribution — the screen is the top of it, the room is the middle — and
   then **smoothed over time**, because a threshold that jumps frame to frame flickers.
   ⚠️ `LO` must clear the room's median by a real margin: at the tightest point of this clip the two
   are only 3× apart, and keying into the room desaturates the whole office.
2. **Recolour the real pixels; never paste a synthetic screen over them.** Pasting a shape means
   inventing an edge, and an invented edge does not match the tube's real bezel shadow, corner
   rounding or anti-aliasing — Kai spotted it instantly as *"a black overlay on the monitor"*.
   Recolouring keeps every one of those for free.

**A switched-off CRT is not black.** R and B are untouched by the chroma fill, so their average is
the honest brightness underneath it — which gives a dark grey mirror still carrying the plate's own
shading and reflections, rather than a flat fill.

**Despill the edge.** Along the tube's anti-aliased boundary the greenness sits between the two
bounds, so those pixels are only partly keyed and keep some green — a thin green rim right around
the screen. Green is clamped to the other two channels across a slightly dilated band.

**And it made the scene better.** The monitor now **wakes up** when we arrive — a dot strikes, opens
to a line, opens vertically, overbrightens, settles, and the prompt fades up. That bookends exactly
against the switch-off at the other end: same grammar both ways, and two more places for a thunk.

⚠️ **Two plates, and they are not interchangeable.** `plate-1080.png` still carries the chroma fill
and is what the screen geometry is keyed out of; `plate-off-1080.png` is the processed version and
is what every terminal frame is built on. The dead-tube pixels are taken **verbatim** from it, which
is why the push-in→terminal join measures a mean difference of **0.88/255** — six times quieter than
two adjacent frames mid-push-in, which differ by 5.25. It is codec noise, not a cut.

## B4 — the terminal, built in post

`build_terminal.py`. Nothing on that screen is generated; every pixel of it is drawn.

**Font: Mx437 IBM VGA 9x16** — the actual VGA text-mode ROM typeface, from the Ultimate Oldschool
PC Font Pack (int10h.org, CC BY-SA). Sized so the 27-character line fills ~79% of the screen width,
which is far larger than an authentic 80-column prompt and deliberately so: the line is the title,
so it has to carry the frame.

**The screen is measured, not eyeballed.** The chroma fill is keyed out of the plate, and the mask
comes back **615×487 with the middle rows 130px wider than the top and bottom** — rounded-corner
CRT geometry. A quartic (`1 - k·c⁴`, k=0.248 horizontal / 0.104 vertical) fits it, and the type is
inverse-mapped through that, so it curves onto the glass instead of sitting on it.

**Beat.** Frame numbers are within B4; `t` is into the finished scene, which is what the audio
cuts against.

| Frames | t | What |
| --- | --- | --- |
| 0–19 | 19.50–20.33 | we arrive and sit on a dead tube |
| 20–21 | 20.33 | 🔊 **power on** — a dot strikes in the centre |
| 22–24 | 20.42 | it opens out into a horizontal line |
| 25–27 | 20.54 | the line opens vertically, overbright |
| 28–36 | 20.67–21.04 | brightness settles, the prompt fades up |
| 37–55 | 21.04–21.83 | `C:\>` and a blinking block cursor |
| 56–108 | 21.83–24.04 | 🔊 **22 characters land**, ~0.1s each |
| 109–142 | 24.04–25.46 | the hesitation — cursor blinking after the command |
| 143 | 25.46 | 🔊 **Enter.** Cursor drops to the next line |
| 143–171 | 25.46–26.67 | nothing happens |
| 172–175 | 26.67 | 🔊 **switch off** — picture squeezes to a bright line, blowing out |
| 176–177 | 26.83 | line closes to a centre dot |
| 178–191 | 26.92–27.50 | dot fades |
| 192–199 | 27.50–27.83 | black |

**Kai adds the audio.** Every 🔊 above is a cut point: the CRT thunk on, keystrokes under the
typing, the Enter, and the CRT thunk off.

### Four things that had to be got right

1. **The room spill has to come down with the screen.** The plate's office is lit by a *bright*
   chroma-green monitor. A dark terminal does not throw that much light, so the surround is
   neutralised in a feathered radius and relit to match — and goes out entirely when the tube dies.
2. **A dead tube is BLACK, not green.** First attempt left the plate's chroma green underneath, so
   the instant the collapsing picture stopped covering the screen, raw green flooded back.
3. **Dilate and feather the mask — never erode it.** The generated screen is a hard-edged fill, so
   replacing only the keyed pixels leaves a bright green rim right around the tube. Eroding makes it
   worse. Dilate past the edge and feather, so the phosphor tucks under the bezel shadow.
4. **Scanlines belong in screen space, not in the texture.** Striping the flat texture and then
   resampling it through the warp aliased into a visible moiré across the whole phosphor field.
   Evaluated per output pixel from its curved coordinate they follow the tube and cannot alias.

⚠️ **The settle cross-fade starts from the plate's MEASURED green**, not a guessed one, or frame 0
pops against the last frame of the push-in.

## What is still owed

- **A grade and a grain pass.** B1–B3 are 720p sources upscaled to 1080p; the terminal is
  composited natively. A light grain would unify them.
- **Narration.** Every beat length above is a guess; they get cut to the recorded voice.
- **Whatever follows the switch-off.** The dead tube is a transition *into* something.
- **Three canon questions**, all rulings only Kai can give — see [`prompts.md`](../prompts.md) §3b:
  whether the office is occupied, whose hands push (recommendation: nobody is at the keyboard and
  the command types anyway), and whether B4's hard cut carries the title card.

## Superseded — do not re-run

| Files (scratch only) | What it was | Why it died |
| --- | --- | --- |
| `s01-hk-wide-{a,b}`, `s01-cafe-ext-{a,b}`, `s01-cafe-int-{a,b}`, `s01-crt-plate-{a,b}` | The grimy set — neon canyon, derelict internet cafe | Grime pre-loads the dystopia (Kai, 2026-08-21) |
| `s01-b1-hk-wide-{a,b}`, `s01-b2-cafe-ext-{a,b}`, `s01-b2-cafe-ext-v2-{a,b}`, `s01-b3-cafe-int-{a,b}` | Veo attempts on the grimy plates | Essentially static — see the finding above |
| `s01-tower-ext-{a,b}` | First modern tower exterior | Baked-in matte border; portrait on a white field |
| `s01-ROUGH-SHAPE.mp4` | The grimy rough cut | Superseded by `s01-ROUGH-MODERN.mp4` |
| `TEST-crt-text-{a..d}.jpg`, `TEST-crt-push-{a,b}.mp4` | The 2026-08-21 capability retest | **Keep as reference** — they carry `git push origin master` correctly rendered 4/4, and give post the phosphor colour, glow radius and character weight to match |
