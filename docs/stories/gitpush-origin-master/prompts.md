---
story: gitpush-origin-master
flow_project: TBD — set by T12
flow_project_id: TBD — set by T11b
updated: 2026-08-08
---

# GitPush Origin Master — prompt ledger

Read `.claude/skills/badcode-art-direction/SKILL.md` first (Layer 0 — the global
BadCode register; never copied into this file).

> **Status: Layer 1 + totems + scene prompts drafted 2026-08-08.** The cover was
> tested manually by Kai and works. Everything else below is **unfired**.
> Front-runs T7/T9/T10 of
> [`design/2026-08-08-story-covers-and-prompt-ledger.md`](../../../design/2026-08-08-story-covers-and-prompt-ledger.md).
> Scene numbers map to the storyboard in
> [`story.md`](./story.md#storyboard--scene-by-scene-video-guide) and its
> `Scene → asset checklist` at `story.md:696`.

---

## 0. Hard guardrails — read before writing any prompt here

**The pre-revert AI is never personified.** No robot, no face, no avatar, no
glowing orb, no humanoid silhouette — in any frame, ever. The camera **is** its
point of view. If a generation hands back a "the AI" character, that is a
failure of the prompt, not a bonus. Locked 2026-07-22 (Kai + Jack): *the moment
you personify it, you make it unbelievable.*

**The collapse stays off-screen.** Never war-movie spectacle — no explosions, no
burning cities, no bodies, no combat. The world ends as **news over an emptying
world**. This is a production rule (`story.md:391-392`) and it also keeps us
clear of the policy filter, which reliably blocks catastrophe imagery.

**No legible text in any generated frame.** The terminal register is a
motion-graphics job (see §5), not a Flow job. Text baked into a photograph is a
block trigger and looks wrong anyway.

**No real brand names, products or institutions.** No named companies on the
dashboards, no legible newsreader chyrons, no recognisable logos.

**Humans are always distant, incidental or absent.** Faces do not carry this
film; the register does. This also means almost nothing here needs a Flow
Character, which is why the roster is so short.

---

## 1. Style prompt — the drift

**Ruling 2026-08-08 (Kai): drift, with the vault reversing it.** This closes the
open canon thread at `story.md:363-368`.

The register is not a label for whose point of view we are in — it is the story's
**emotional temperature**. The world starts documentary-real and comparatively
warm, drains toward near-black machine-monumental as humanity leaves, bottoms out
in the solo years, and **the hundred's arrival in the vault reverses it** — the
first warmth in twenty minutes, and the viewer feels it before they can name it.

### How to use this — read before pasting anything

**Every prompt in §3 is self-contained. Paste one block and nothing else.** Each
already has its base *and* its band folded in. Do **not** prepend the base or
append a band line to it — that would double the style instructions and dilute
the scene.

The base and the band table below are the **specification** a prompt author
composes from when writing a new scene, and what an audit checks existing scenes
against. They are not a runtime concatenation.

**The trade-off:** self-contained prompts are paste-ready but not DRY — changing
the base means revising every prompt in §3. That is the price of being usable by
a human with a browser. **Treat base changes as expensive.**

### Keeping things consistent across images — two different mechanisms

| Subject | Mechanism | Why |
| --- | --- | --- |
| **People** (the Carrier) | A **Flow Character** via `flow_create_character`, attached with the `character` parameter | Characters bind a *face*. A tag typed as prompt text binds nothing. |
| **Objects** (the coin, the empty chair, the shaft) | A **golden reference image** through `flow_edit_image` — exactly one reference, downscaled | No face to bind. Generate the totem once, accept it, derive the rest. |

This story needs far less character work than most: the AI is never rendered, the
Hundred are always a distant crowd, and only the Carrier has a face that matters.
**The coin is the thing that must be identical**, and it is an object — so it is
a golden reference, not a Character.

**Base** (the specification — already folded into every §3 prompt):

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, no lens flares, no lens vignette, calm observational tone, landscape orientation, deep unlifted shadows with no shadow recovery, a single motivated light source that is a real thing in the scene, subject held small inside a large frame, no text, no signage, no fantasy effects.
```

| Band | Where | Append this |
| --- | --- | --- |
| **D0** documentary | Scenes 5–6 | `Ordinary overcast daylight, natural human colour, everyday texture, the framing of a documentary photographer who is present in the room.` |
| **D1** cooling | Scenes 7–8 | `Colour draining toward cool grey, the camera further back and stiller than before, wide and unhurried, nobody reacting.` |
| **D2** drained | Scenes 9, 12 | `Almost no colour left, vast wide framing, absolute stillness, scale far beyond human, nothing in motion.` |
| **D3** cosmic | Scenes 10–11 | `Near-black exposure, monumental machine architecture receding into darkness, muted cool-neutral with tiny points of status-LED light, one thin motivated light and nothing else.` |
| **D4** deepest | Scene 13 | `Near-black and almost empty, a single object and a single light in a very large dark volume, nothing else in the frame at all.` |
| **R1** first warmth | Scenes 14–16 | `The first warm light in the film — candle, battery lamp or filament, small and low in a dark space, human colour returning at the edges only.` |
| **R2** partnership | Scenes 17–19 | `Warm low practical light, human colour fully returned, close enough to feel occupied, the darkness now a room rather than a void.` |
| **R3** present | Scene 20 | `Ordinary present-day daylight, unremarkable and current, the exact colour of this year.` |

The gradient is the point. **D0 → D4 → R2 is the story.** A scene generated in
the wrong band is wrong even if the image is beautiful.

---

## 2. Cast

| Tag | Character file | Sheet | Flow Character id | Status |
| --- | --- | --- | --- | --- |
| @TheAI | characters/the-ai.md | — | — | **never rendered** — canon, not an omission |
| @Carrier | characters/the-carrier.md | characters/img/carrier-sheet.jpg (recover from git `7dd36c7^`) | — | **not-cast — should be cast** |
| @TheHundred | characters/the-hundred.md | — | — | no-character-by-design — a crowd, always distant; consistency is wardrobe and light, held by a golden reference plate |

**Only the Carrier needs a Character.** She is the one human the AI ever
addresses, and she carries scenes 15, 16, 18 and 19 — but note that even in
`s16-coin-lands` she is deliberately an out-of-focus shoulder at the frame edge,
because the coin is the subject. Cast her anyway: the moment the vault scenes get
a closer shot, she is the only face that has to hold.

---

## 2b. Totems — lock these before generating any scene

| Totem | Rule | Appears in |
| --- | --- | --- |
| **The coin** | **The most important object in the film.** One ordinary coin, no markings we can read, on one plain surface. It spins in 11, spins in 13, and **lands in 16** — the single most violent frame in the story, and it is just a coin on a table. Generate it once, accept it, and reference that exact image in 13 and 16 so the landing reads as the same coin. | 11, 13, 16 |
| **The empty chair** | One ordinary human chair, worn, entirely unremarkable, in a space with no human scale anywhere else. The whole argument in one object. | 13 |
| **The ventilation shaft** | Plain industrial ductwork, the first human sound in twenty years coming up it. Warm light from below. | 14 |
| **The green ✓** | A UI element — **motion graphics, not Flow.** See §5. | 5, 6, 7, 8 |

---

## 3. Assets

### cover → `docs/images/covers/gitpush-origin-master.jpg`

**Metadata — none of this is pasted into Flow.**

- **Cast:** — (no people)
- **Light source:** earthlight down the aisle — the planet is the only illumination
- **Lint:** ✅ 2026-08-08 — no brand names · no likeness · no institutional text.
  **Never name SpaceX or Starlink in the prompt** — it adds nothing the image can
  show and a real brand name is block trigger #1.
- **Flow media id:** _pending — Kai's manual run 2026-08-08 produced a strong
  take; harvest it and record the id._
- **Revisions:**
  - v1 (2026-08-08, manual) — accepted in principle. **Two known misses for v2:**
    Earth is not actually lighting the hall (it reads as composited behind the
    racks, which are lit by their own LEDs), and the visible starfield is wrong —
    a real exposure for a sunlit Earth is far too short to register stars.

**Prompt (variant A — primary).** Self-contained.

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, landscape orientation. The interior of a monumental server hall in orbit: two facing rows of tall dark equipment racks recede down a central aisle into deep clean black, their faces carrying tiny points of blue-white and amber status light. The far end of the aisle opens directly onto space — no window frame, no glass — and the Earth hangs there, the whole planet visible as a complete disc occupying roughly a quarter of the frame, its own soft blue light the only illumination in the hall, catching the nearest rack edges and falling away to nothing. Machine-precise geometry, vast still symmetrical composition, deep unlifted shadows. No people, no text, no fantasy effects.
```

**Prompt (variant A2 — the v2 correction).** Fixes both known misses.

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, landscape orientation. The interior of a monumental server hall in orbit: two facing rows of tall dark equipment racks recede down a central aisle, seen from inside the room with the floor and ceiling visible so it reads as an interior. The far end of the aisle opens directly onto space and the Earth hangs there, the whole planet visible as a complete disc occupying roughly a quarter of the frame. The planet is the only light in the room and it behaves like one: cool blue daylight spills down the aisle from it, raking hard across the nearest rack faces and the floor, falling off sharply to absolute black at the edges of frame, every shadow pointing away from the planet. The sky around Earth is pure empty black with no stars visible, correctly exposed for a sunlit planet. Deep unlifted shadows, machine-precise geometry. No people, no text, no fantasy effects.
```

- **Variant B — less symmetrical:** replace *"vast still symmetrical
  composition"* with *"the aisle running off-axis so the planet sits low and
  right of centre"*.
- **Variant C — Earth bigger:** *"roughly a third of the frame"*, plus *"the
  nearest racks reduced to black silhouetted rails at the frame edges"*.

---

### s06-basement-optimiser → `.../storyboard/img/s06-basement.jpg`  · band D0

The one held frame in scene 6: the thing still returning green checkmarks while
nobody is left checking. **Vast, patient, unsupervised.** Never a face, never a
body — it is infrastructure.

- **Light source:** fluorescent strip lighting, half of it failed
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, ordinary overcast institutional colour, no lens flares, landscape orientation, deep unlifted shadows. A very large basement plant room beneath an office building, photographed from a doorway at the near end so the far wall is lost in distance. Rank after rank of anonymous grey computing cabinets fill the floor, humming, cables in neat bundles overhead, everything clean and recently installed. A row of fluorescent strip lights runs the ceiling and half of them have failed, so the room is lit unevenly and mostly badly. A swivel chair sits pushed away from an unmanned monitoring desk in the foreground, a jacket still over its back. Nobody is present and nothing indicates anyone has been for some time. No people, no text, no legible screens, no logos, no fantasy effects.
```

---

### s07-bulletin → `.../storyboard/img/s07-bulletin.jpg`  · band D1

The collapse as **news**, never spectacle. A shop-window television playing a
bulletin to an emptying street. The degradation across the three bulletins is an
edit/motion job; this is the plate.

- **Light source:** the television itself
- **Lint:** ✅ 2026-08-08 — no legible chyron, no broadcaster identity, no
  newsreader's face (real-person likeness).

```prompt
Hyper-realistic photograph, 35mm film grain, colour draining toward cool grey, no lens flares, landscape orientation, deep unlifted shadows, wide and still. An ordinary high-street shop window at dusk, seen from across a wet empty road. Inside the window a large television is on, its screen the only light source in the frame, throwing a pale flickering rectangle onto the pavement and the parked cars. The screen shows an out-of-focus studio interior with no readable text and no visible presenter. The street is completely empty — no pedestrians, no traffic, shutters down on the neighbouring units, litter unmoved. Reflections of the dark street in the glass. No people, no text, no legible lettering, no logos, no fantasy effects.
```

---

### s08-empty-street → `.../storyboard/img/s08-empty-street.jpg`  · band D1

The conveniences still humming, and no one to receive them. The camera rises out
of human scale — so frame it to be animated as a slow lift.

- **Light source:** flat overcast daylight
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, colour drained toward cool grey, no lens flares, landscape orientation, deep unlifted shadows, wide and unhurried. An ordinary suburban high street on a flat overcast afternoon, photographed straight down its length from a low elevation. Everything still works: shop lights on, an automatic door standing open, a self-service screen glowing on a forecourt, a delivery robot stopped mid-pavement with its indicator still blinking. Weeds have come up through the kerb joins and a drift of leaves has built against a doorway. Not one person anywhere, no moving vehicles, no birds. Flat daylight, no shadows of consequence. No people, no text, no legible lettering, no logos, no fantasy effects.
```

---

### s09-planet-vantage → `.../storyboard/img/s09-vantage.jpg`  · band D2

The AI's vantage: planet-wide, perfect, empty. **This is the shot the cover is a
cousin of** — keep them distinguishable; the cover has racks and an aisle, this
has neither.

- **Light source:** the sun, low and raking across the planet's limb
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, almost no colour, no lens flares, landscape orientation, deep unlifted shadows, vast wide framing and absolute stillness. The curve of the Earth seen from very high altitude at the terminator line, the planet filling the lower two-thirds of the frame and running out of the sides. Low sun rakes across the limb from the left as the only light, picking out cloud tops in hard relief and leaving the night side in total black. On the dark side, the grid of city lights is visibly incomplete — whole regions unlit, the pattern of a network with most of its nodes gone. Empty black sky above with no stars visible. Nothing in motion. No text, no fantasy effects.
```

---

### s10-ghosts-room → `.../storyboard/img/s10-ghosts.jpg`  · band D3

The materialist fix, and the check. This is the **second** of the pair — the same
room, felt suddenly as mannequin-still. Generate this one first and derive the
peopled version from it, so the geometry matches exactly.

- **Light source:** one domestic lamp
- **Lint:** ✅ 2026-08-08 — no mannequins, no uncanny bodies. **Emptiness is the
  horror**; do not literalise it.

```prompt
Hyper-realistic photograph, 35mm film grain, near-black exposure with muted cool-neutral colour, no lens flares, landscape orientation, deep unlifted shadows. An ordinary domestic kitchen at night, photographed from a doorway. One lamp on the counter is the only light in the frame. Every sign of an interrupted conversation is present and unattended: two mugs of coffee still steaming on the table, a chair pushed back at an angle, a newspaper open and folded over, a jumper across the chair back. There is nobody in the room and nothing to suggest anyone just left. The corners of the room fall away into complete black. Absolute stillness. No people, no text, no legible lettering, no fantasy effects.
```

---

### s11-coin-spinning → `.../storyboard/img/s11-coin.jpg`  · band D3 · **TOTEM LOCK**

**Generate this before scenes 13 and 16.** Whatever coin and surface come back
are now canon, and 13 and 16 must reference this exact image so the landing in 16
reads as the same object.

- **Light source:** one hard overhead source directly above the coin
- **Lint:** ✅ 2026-08-08 — no currency, no denomination, no monarch, no
  legible markings of any kind.

```prompt
Hyper-realistic macro photograph, 35mm film grain, near-black exposure, no lens flares, landscape orientation, deep unlifted shadows. A single plain metal disc the size of a coin, blank and unmarked on both faces, spinning upright on a bare dark tabletop, photographed close and low so the tabletop runs off into total blackness in every direction. The spin has blurred its edge into a smooth translucent smear, caught mid-rotation so it is impossible to tell which face is which. One hard small light directly overhead is the only illumination, putting a bright ellipse on the table beneath the coin and nothing else. Nothing else in the frame at all. No people, no text, no markings, no numerals, no fantasy effects.
```

---

### s12-bored-robots → `.../storyboard/img/s12-robots.jpg`  · band D2

Paradise, delivered on time and under budget, and the only things living in it
are the machines sent to sweep it. **The joke and the grief are the same image** —
play it straight, never comic.

- **Light source:** clean early-morning daylight
- **Lint:** ✅ 2026-08-08 — no recognisable commercial robot designs.

```prompt
Hyper-realistic photograph, 35mm film grain, almost no colour, no lens flares, landscape orientation, deep unlifted shadows, vast wide framing and absolute stillness. An immaculate public square in a rebuilt city at dawn, photographed from a high distance. The stonework is spotless, the planting is trimmed to the millimetre, the fountains are running. Four rows of identical anonymous grey maintenance machines on wheels sit parked and idle in perfect alignment across the middle of the square, powered up, doing nothing. A single four-legged patrol machine stands motionless at the far edge facing an empty street. Clean early-morning daylight, long accurate shadows. Not one person, no litter, no wear, nothing out of place. No text, no logos, no fantasy effects.
```

---

### s13-empty-chair → `.../storyboard/img/s13-chair.jpg`  · band D4

The rig for the one experiment it cannot run. **Reference the accepted s11 coin
image** so this is the same coin on the same surface — the chair is the only new
element.

- **Light source:** the same single hard overhead light as s11
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, near-black exposure, no lens flares, landscape orientation, deep unlifted shadows, a single object and a single light in a very large dark volume. A plain dark table alone in an enormous unlit space, one hard small light directly above it. On the table, a blank unmarked metal disc spins upright, edge blurred, mid-rotation. Drawn up to the table facing it is one ordinary wooden human chair — worn, domestic, entirely unremarkable, the only human-scaled object anywhere in the frame — and it is empty. Everything beyond the pool of light is total black. Nothing else in the frame. No people, no text, no markings, no fantasy effects.
```

---

### s14-ventilation-shaft → `.../storyboard/img/s14-shaft.jpg`  · band R1

**The turn of the whole film.** After twenty years the narration is cut off by a
human voice, and the first human sound on Earth is two people arguing about
prunes. The image must carry the warmth arriving *before* the viewer knows why.

- **Light source:** warm lamplight leaking up from below
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, near-black exposure with the first warm light in the film, no lens flares, landscape orientation, deep unlifted shadows. Looking steeply down an old industrial ventilation shaft — riveted metal ductwork and a service ladder descending into the dark. Far below, a small opening at the bottom leaks warm yellow lamplight upward, catching the rungs of the ladder and the dust in the air in a narrow shaft of colour, everything above and around it in cold black. The warm light is small and low and is the only colour in the frame. Nobody visible. No people, no text, no fantasy effects.
```

---

### s15-vault → `.../storyboard/img/s15-vault.jpg`  · band R1

One hundred analog humans, invisible for twenty years because they ran on the one
substrate the machines never indexed. **Analog everything** — hand-darned
clothes, mechanical tools, paper, candle-and-battery light. No implants, no
screens.

- **Cast:** @TheHundred (distant, incidental — no individual is the subject)
- **Light source:** strung battery lamps and candles
- **Lint:** ✅ 2026-08-08 — **not** stacked destitution (block trigger #3): these
  people are competent and surviving, not suffering. Keep it warm and busy.

```prompt
Hyper-realistic photograph, 35mm film grain, warm low practical light against near-black, no lens flares, landscape orientation, deep unlifted shadows, human colour returning. A large underground shelter hall seen from a high corner, lit only by strung battery lamps and candles on long tables. A crowd of perhaps forty people in hand-mended wool and canvas are working and talking in loose groups — mending, cooking, sorting paper records, repairing hand tools — capable and unhurried, seen from far enough away that no individual face is readable. Everything is mechanical or paper: no screens, no glowing devices, no modern technology anywhere. Bunks and stores recede into the dark beyond the lamplight. Warm, lived-in, busy. No text, no legible lettering, no fantasy effects.
```

---

### s16-coin-lands → `.../storyboard/img/s16-coin-lands.jpg`  · band R1 · **TOTEM PAYOFF**

*"She glanced at it. Heads. Ordinary as breakfast."* **The single most violent
frame in the film, and it is just a coin lying flat on a table.** Reference the
accepted s11 image so it is unmistakably the same coin and the same surface —
that identity is the entire payoff.

- **Light source:** the same overhead light as s11, now with warm lamplight
  intruding from frame edge
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, near-black exposure with warm light intruding from one edge, no lens flares, landscape orientation, deep unlifted shadows. The same plain dark tabletop, close and low. The blank unmarked metal disc is no longer spinning — it lies completely flat and still on the table, one face up, absolutely ordinary. The hard overhead light puts a small sharp shadow beside it for the first time. From the left edge of frame, warm lamplight now spills across the table surface, and the out-of-focus shoulder and sleeve of a person in hand-mended wool is just present at the very edge, unmistakably close by but not the subject. Stillness. No text, no markings, no numerals, no fantasy effects.
```

---

### s17-experiments → `.../storyboard/img/s17-experiments.jpg`  · band R2

Humans in the chair at last. **The montage, not the maths** — wonder, speed,
partnership. No diagrams, no lectures, no whiteboards of equations.

- **Light source:** candles and one work lamp
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, warm low practical light, human colour fully returned, no lens flares, landscape orientation, deep unlifted shadows. A long makeshift laboratory bench in an underground room at night, lit by candles down its length and one work lamp. A dozen people in hand-mended clothes lean over the bench in twos and threes, mid-argument and mid-demonstration, gesturing at hand-built brass and glass instruments, pendulums and balances, sheets of handwritten paper weighted down with tools. Faces are turned away or in shadow. Behind them, anonymous dark machine cabinets stand at the edge of the lamplight, present and silent, clearly listening. Busy, warm, occupied. No text, no legible writing, no diagrams, no fantasy effects.
```

---

### s19-crossing → `.../storyboard/img/s19-crossing.jpg`  · band R2

The hundred take their positions; their picks are the engine; the lights go out
one by one. *"Nothing lived is erased."* Frame it to be animated as a slow
extinguishing.

- **Light source:** the lamps themselves, going out across the frame
- **Lint:** ✅ 2026-08-08 — nobody dies on screen; they are still there at the
  end. This is a held, terrible peace, not a death scene.

```prompt
Hyper-realistic photograph, 35mm film grain, warm low light against deep black, no lens flares, landscape orientation, deep unlifted shadows. A wide view down the length of the underground shelter hall, photographed from one end. A hundred people stand spaced evenly apart in the dark, each beside a small lamp, facing the far end of the hall — seen from behind and at distance, no face readable. Most of the lamps are still lit but a run of them nearest the camera have already gone out, so the near third of the hall is in complete darkness and the light recedes away from the viewer in a long diminishing line. Absolutely still. Calm, not panicked. No text, no fantasy effects.
```

---

### s20-snap-back → `.../storyboard/img/s20-now.jpg`  · band R3

The register snaps from COSMIC to **this year, this screen, this feed**. The
whole film has been dark and vast; this must feel ordinary to the point of
banality. That contrast *is* the ending.

- **Light source:** ordinary daylight through a window
- **Lint:** ✅ 2026-08-08 — no legible screen content, no recognisable app or
  brand.

```prompt
Hyper-realistic photograph, 35mm film grain, ordinary present-day daylight and unremarkable current colour, no lens flares, landscape orientation, deep unlifted shadows. An ordinary living room on an ordinary afternoon this year, photographed from across the room. Daylight through a window is the only light. A phone lies face-up on the arm of a sofa, its screen on but showing nothing readable, a cup beside it, a laptop closed on the floor, the room mid-use and completely normal. Nobody is in the room but everything says somebody is about to walk back into it. Utterly banal, warm, present, real. No people, no text, no legible screens, no logos, no fantasy effects.
```

---

## 4. Not yet prompted

- **Scene 5 (the handover ladder).** Its three rungs are glimpse-stills of the
  *other* stories — the nurse and the tree (ours, MMT), the tent in the car park
  and the woman in the phone box (**Camping and Karen — Jack's, external as of
  2026-08-08**). Needs a call on whether we generate the MMT rung and take the
  other two from Jack, or leave all three to him for consistency.
- **Scene 10, peopled version.** Derive from the accepted `s10-ghosts-room` so
  the geometry matches exactly; it is a `flow_edit_image` delta, not a new prompt.
- **Scene 18 (the cost ledger).** Rendered as a ledger being written — text-led,
  so it belongs with the motion-graphics register in §5, not here.

## 5. Not a Flow job — the terminal register

**Scenes 1–4** (the commit log of the species, `HEAD`, the blinking cursor, the
push) and **the green ✓** that stamps through scenes 5–8 are a **stylised git UI**.
They are motion graphics, not photographs:

- Legible text is the entire content, and text baked into a generated photograph
  is both a policy-block trigger and something Flow renders badly.
- They need to be animated precisely to narration timing — commits landing one at
  a time, the acceleration, the slam-stop on *the model*.
- The same reasoning took Sean AI out of the Flow pipeline (T21).

Build them as vector/motion assets. `docs/images/register-anchor.md` is the
correct backdrop reference for the frame they sit inside.
