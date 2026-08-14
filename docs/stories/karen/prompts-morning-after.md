---
story: karen
kind: brief — written in-repo, not yet fired; replace with what was actually typed
engine: Nano Banana Pro (plates) — see the engine call below
flow_project: TODO — exact project name as it appears in Flow
updated: 2026-08-14
---

# Karen — the morning after

Plate prompts for the beat that ends Act 1: **Karen wakes with no phone and no
memory, gets to the phone box, and Susan aims her at the rest of the film.**
[`story.md`](./story.md#17-the-morning-after--new-the-end-of-act-1-get-this-right) §1.7.

> ## 🖐 A brief, not a record
>
> Same standing as [`prompts-river-drop.md`](./prompts-river-drop.md): written
> in-repo, unfired, expected to change. [`prompts.md`](./prompts.md) is the
> **ledger** — prompts Jack typed by hand, kept verbatim as a restore point — and
> nothing here may be mistaken for one.
>
> It inherits the ledger's conventions: the §1 `STYLE LOCK` pasted verbatim at the
> top of every plate, the casting rule (`**Cast:** @Karen` — never describe a
> face), no legible text anywhere, and the closing *"Thanks."* Section numbers
> continue the sequence at **§2h**.
>
> **Engine research does not live here.** The Nano Banana Pro and anti-slop
> findings this section produced are in
> [`docs/google-flow/nano-banana-2.md`](../../google-flow/nano-banana-2.md#third-pass--nano-banana-pro-and-the-anti-slop-toolkit).

---

## Why this scene is worth the care

§1.7 is *"the end of Act 1; get this right."* It is the hinge: everything from here
to the President taking a call on live TV is downstream of Susan's pep talk. It also
has to do something structurally awkward — **carry a phone conversation between two
people in two rooms**, which is a lot of shots for a scene with almost no action in it.

The design below solves that with **a matched pair**: Karen waking and Susan waking,
shot identically. Canon already calls for it — *"mirror of the shot we just did with
Karen (fun, cheap, works)"* — and it does three jobs at once. It cuts the scene
together, it gets the laugh, and it makes the two-rooms problem into the joke rather
than a problem.

**The one image that has to be great is [§2h.7](#2h7-the-last-frame-of-act-1--plate).**
It is the exit feeling — *I would not want to be the person who answers her next
call* — and it is the shot the statue at the end of the story rhymes with.

## The engine call: Nano Banana Pro, not NB2

`[untested]`, and reversible, but the reasoning is in
[`nano-banana-2.md`](../../google-flow/nano-banana-2.md#which-engine-for-badcode):

- NB2's reported failure is *"too sharp… too overly contrast… almost overexposed"*
  against Pro's *"a lot more natural."* **Over-sharpened and over-lit is a fair
  description of the AI look itself**, and the Karen register is a suppression of
  exactly that axis.
- Pro **reasons about the prompt before generating**, which is what the matched pair
  needs — §2h.4 is asking for a deliberate compositional rhyme, and that is an
  instruction a planning model can act on.
- The cost is a tighter rate limit. For seven plates, pay it.

**If Pro is rate-limited, drop to NB2 and watch the highlights**, not the faces.

## What is different about these prompts

Three deliberate departures from the §2g blocks, all from the 2026-08-14 research:

1. **Google's Nano Banana Pro slot order**, not our old six-slot shape:
   **Subject · Composition · Action · Location · Light · Style · Constraints.**
   Composition is promoted above Action, which is Pro's documented preference.
2. **⚠️ The scene blocks no longer restate texture.** No "grainy", no "halation", no
   "film grain" below the lock. Pro's rule is *"descriptive, not repetitive"*, and a
   *"focused short prompt can beat a long prompt with competing styles"* `[vendor]`.
   **The `STYLE LOCK` owns texture and optics; the scene block owns the world.** If a
   word is in the lock, it does not appear again underneath it.
3. **The four anti-slop counters the lock does not already buy** are now in every
   block, because they live in the world rather than in the capture:

   | Counter | How it shows up below |
   | --- | --- |
   | **environmental imperfection** | the dried water ring, the charging cable with nothing on it, the scaffolding, the smeared glass |
   | **mid-action, not posed** | "halfway up onto one elbow", "already turning away" |
   | **off-centre, not quite level** | stated in every Composition line |
   | **a foreground occluder** | the bedside table, the kiosk frame, the glass |

**Exclusions stay at one short clause — the lock's.** Do not add a second. Long
exclusion lists dilute, and the realism literature's instinct to stack them is the
one piece of its advice that fights Google's.

---

## The prompts — §2h

**Paste the §1 `STYLE LOCK` verbatim above each block**, then the block, then
*"Thanks."* — as with every plate in the ledger.

### 2h.1 The waking shot — plate

**Cast:** `@Karen`.

The scene's establishing image and **the master for the matched pair** — fire this
one first and accept it properly, because §2h.4 has to copy its geometry.

The story detail doing the heavy lifting is **the charging cable with nothing on the
end of it.** It plants the missing phone before she knows it is missing, it is the
kind of thing a real bedroom has, and it costs one clause.

```prompt
SCENE:

Subject: a woman lying half under a twisted duvet in a small bedroom, just surfaced from a heavy sleep, propped up on one forearm with her eyes still shut against the light.

Composition: 16:9, from the side at mattress height, the bed running across the frame; she sits off-centre to the right, the bedside table large and soft in the near foreground; the horizon of the mattress is not quite level.

Action: caught halfway up onto one elbow with the duvet still twisted around one leg — mid-movement, between lying down and sitting up.

Location: a small New York apartment bedroom in mid-morning; a bedside table holding a lamp, a drinking glass with a dried ring under it, a paperback face-down, and a charging cable coiled with nothing on the end of it; a camel cashmere cardigan dropped on the floor where it fell, one low-heel flat still on her foot, a structured leather handbag dumped on its side by the bed.

Light: a half-open venetian blind at the window camera-left throwing a hard ladder of daylight across the bed and up the wall behind her; the rest of the room in flat shadow; no other source.

Style: a still from a 35mm independent film — the last morning of the first act. Available light only, unretouched, natural skin texture.

Constraints: she is still in yesterday's cream blouse, slept in and pulled untucked, hair flattened on one side; keep every book spine, label and sign free of readable lettering.
```

### 2h.2 Where's my phone — plate

**Cast:** none. **No face in frame, so nothing to bind** — and per the standing rule
we do not cast a Character into a shot that has no face in it.

The whole beat is an **absence**, so the shot is the absence: everything a handbag
contains, tipped out, and no phone in it. Cheap, unblockable, and it reads at a
glance.

```prompt
SCENE:

Subject: the entire contents of a woman's handbag tipped out across a rumpled duvet, with her hands going through it.

Composition: 16:9, from almost directly above, close over the bed; the spill of objects sits low and left of centre with empty duvet filling the top right; the frame is slightly rotated off square; the edge of the upturned handbag crosses the bottom of frame out of focus.

Action: two hands mid-search, one pushing objects aside and the other lifting the empty bag by its base to shake it out.

Location: an unmade bed in mid-morning; the spill consists only of car keys on a luxury fob, a lipstick, folded receipts, sunglasses with one arm open, a packet of tissues, loose change, a hairbrush and a crumpled bar napkin — no phone among them.

Light: a hard ladder of daylight from a half-open blind falling across the duvet and the objects, the shadows long and low.

Style: a still from a 35mm independent film. Available light only, unretouched.

Constraints: cream blouse cuffs at the wrists, manicured nails, a camel cardigan sleeve at the edge of frame; keep every receipt, label, napkin and fob free of readable lettering.
```

> **How the absence is stated, and why.** *"The spill consists only of…"* plus an
> exhaustive inventory, then **one** short negation. An absence cannot be described
> positively, but an exhaustive positive list comes close, and `only` is a restriction
> these models handle well. A bare *"no phone anywhere"* is the construction Google's
> guidance warns against and it puts the word *phone* into the prompt as content.
> **Revised 2026-08-14** from the first version, which did exactly that.

### 2h.3 The phone box — plate · **reference-anchored**

**Cast:** `@Karen`. **Attach the phone booth reference image** — Kai has one
(2026-08-14), so this plate is reference-anchored rather than generated from nothing.

The icon of the entire story arrives here, and **the failure mode is the postcard.** A
lone figure in a phone box on a Manhattan street at golden hour is one of the most
generated images in existence. Every counter is in the frame: she is small and not
centred, the kiosk is scuffed and municipal, there is scaffolding and a bin, and the
light is flat mid-morning rather than golden anything.

> ### ⚠️ This plate is a design decision, not just a shot
>
> **Whatever kiosk comes back becomes the phone box for the rest of the story** —
> §2h.6 and §2h.7 sit inside it, Act 2 spends nine months in it, and Act 5's statue
> *is* it. Judge it as production design, not as a frame: if it is not a kiosk you
> would want cast in bronze at the end of the film, that is the reason to re-roll,
> not the composition.
>
> **Keep the accepted source file.** §2h.6 and §2h.7 want it attached the same way.
>
> ### Check the reference before attaching it
>
> Two documented anti-patterns, both cheap to avoid:
>
> - **Anyone in the photograph?** A location reference containing people gets read as
>   a *subject* reference — the model keeps the people and re-stages the location,
>   which is how the §2g clip failed four times. **Crop them out.** Same for a strong
>   distinctive background: crop tight to the kiosk.
> - **Legible signage on it?** Real payphone branding will come through, against the
>   standing no-readable-text rule. Crop, or expect to fight it.

**The `REFERENCE` block is the load-bearing part.** Nano Banana's documented shape is
`[Reference images] + [Relationship instruction] + [New scenario]`, and the middle term
is what stops the model treating the photo as the shot. It also has to say the style
does *not* come from the reference — an attached image anchors identity and content,
and the model will not assume your style unless the prompt states it.

```prompt
REFERENCE:

Use the attached image as the design reference for the phone kiosk only — its shape, proportions, height, panelling, glazing, colour and construction. Take the kiosk itself from that image and nothing else: not its camera angle, not its lighting, not its weather, not its surroundings, and not any people in it. Rebuild that same kiosk into the new scene described below, seen from the new angle described below. The finished frame carries the film look described in the style lock above, not the look of the attached photograph.

SCENE:

Subject: a woman in yesterday's clothes stepping into that scuffed street phone kiosk on a Midtown Manhattan corner.

Composition: 16:9 wide, from across the street at eye level, the figure small and well left of centre with the block rising out of the top of the frame; a scaffolding leg and a mesh bin cross the right foreground out of focus; the frame is very slightly tilted.

Action: already half inside the kiosk with one hand on the frame and her back three-quarters to camera, mid-stride rather than posed.

Location: a Midtown side street on an ordinary weekday mid-morning — pavement scaffolding with plywood hoarding, a mesh litter bin, a fire hydrant, steam lifting from a vent grate, delivery crates stacked against a shutter, two indifferent pedestrians passing without looking at her.

Light: flat overcast mid-morning daylight from a white sky, no direct sun; the kiosk interior a shade darker than the street.

Style: a still from a 35mm independent film — an ordinary street, an unremarkable morning. Available light only, unretouched.

Constraints: cream blouse untucked, camel cardigan slipped off one shoulder, tailored trousers, no coat, structured leather handbag; keep every sign, hoarding notice, plate, shopfront and kiosk marking free of readable lettering.
```

**What to watch, beyond the postcard:**

- **Did it import the photograph's light?** The `REFERENCE` block says take the kiosk
  and not the lighting, but a reference drags its own look in unless stopped. Sunny, or
  graded like your source photo, means that instruction did not land — sharpen it
  rather than rewriting the prompt.
- **Same kiosk from a new angle, or the same photo with a woman added?** The ask is a
  rebuild. If the composition has collapsed toward the reference's framing, the
  relationship instruction needs strengthening.
- **Is she too small to read?** She is deliberately minor in frame and the binding has
  little to work with. If she is unreadable, tighten the wide rather than enlarging her
  within it — §2h.6 is the close-up that confirms who it is, so this shot does not have
  to carry identification alone.
- **Worth one candidate at 21:9.** The engine offers it, we have never used it, and a
  small figure under a tall block is exactly the case where the 16:9 crop fights the
  scale. `[untested]`

### 2h.4 Susan wakes — plate, the mirror

**Cast:** `@Susan`. **Attach the accepted §2h.1 as a reference image.**

This is the joke, and the joke is entirely in the geometry: **the same shot, the other
woman.** It only lands if the framing is a copy, which is why the reference is attached
with an explicit role rather than described in prose.

**Two findings are being used at once here** — *"clearly define the role of each"*
reference image `[vendor]`, and the fact that Pro reasons about intent before it draws,
so telling it *why* the composition matters is worth the words:

> **Susan has her phone.** It is on the bedside table where Karen's charging cable was
> empty, and it is about to ring. That single swap is the scene's whole argument.

```prompt
SCENE:

Use the attached image for composition, camera height, lens and lighting geometry only — the same side-on framing at mattress height, the same off-centre placement, the same ladder of blind-light across the bed. This is the second half of a deliberate matched pair and should read as a rhyme with it. The room, the furnishings and the person are different.

Subject: a different woman asleep on her front in a different bedroom, one arm flung out across the mattress, not yet awake.

Composition: 16:9, matched to the attached image as above; the bedside table large and soft in the near foreground.

Action: still asleep and about to be woken — face turned into the pillow, one hand slack over the edge of the bed.

Location: a tidier apartment bedroom in mid-morning; a bedside table holding a lamp, a half-drunk mug, a paperback and a smartphone lying face-up and lit; an olive suede bomber over the back of a chair, jeans folded on the seat.

Light: a half-open venetian blind at the window camera-left throwing the same hard ladder of daylight across the bed; no other source.

Style: a still from a 35mm independent film. Available light only, unretouched, natural skin texture.

Constraints: keep every book spine, mug and label free of readable lettering.
```

**If the rhyme does not land, the fix is not this prompt** — it is to re-run it with
2h.1 attached *and* to say which parts drifted. Composition references degrade quietly.

### 2h.5 Susan takes the call — plate

**Cast:** `@Susan`.

The news lands here: *"Karen. Yesterday you got sacked. By an AI. And you dropped your
phone in the river."* Her sheet is explicit that **the affection has to read through
the bluntness** — if she plays contemptuous, the pep talk becomes mockery and the hinge
snaps. So: unimpressed, patient, awake about four seconds, faintly amused. Not withering.

```prompt
SCENE:

Subject: a woman sitting up against the headboard with a phone to her ear, four seconds awake, listening.

Composition: 16:9, from the side and slightly below at mattress height, her head and shoulders left of centre with the empty bedroom falling away to the right; the rumpled duvet crosses the bottom of the frame out of focus; not quite level.

Action: mid-listen with her free hand pressed flat over her eyes, already halfway through a slow sigh — the moment before she says the thing.

Location: the same tidier apartment bedroom, mid-morning; the bedside lamp, the half-drunk mug and the paperback still where they were.

Light: the same ladder of daylight from the half-open blind camera-left, striping across the headboard and her arm.

Style: a still from a 35mm independent film. Available light only, unretouched, natural skin texture.

Constraints: sleep-creased t-shirt, hair flattened on one side; her expression is unimpressed and patient rather than contemptuous, with the affection showing; keep every label and book spine free of readable lettering.
```

### 2h.6 The news lands — plate

**Cast:** `@Karen`.

Interior of the kiosk, and the counter-shot to 2h.5. She has just been told. **No
reaction acting** — the beat is the information arriving, not her performing shock.

The glass is doing the work: the street reflected across her means we are already
watching her from the outside, which is where the rest of the film watches her from.

```prompt
SCENE:

Subject: a woman inside a street phone kiosk with the receiver to her ear, seen through the glass from outside.

Composition: 16:9, close, from just outside the kiosk at eye level; she sits right of centre behind the glass with the reflected street laid across her; the aluminium kiosk frame crosses the left of the frame in hard foreground; slightly off level.

Action: gone still mid-call with the receiver held against her ear and her other hand flat on the little shelf, taking it in.

Location: the interior of a scuffed street kiosk — a worn steel shelf, a coiled metal handset cord, chipped paint, old adhesive marks on the panel where cards were peeled off, the Midtown street reflected in the glass.

Light: flat overcast daylight from outside, the interior a stop darker; a hard bright reflection of the white sky across the upper half of the glass.

Style: a still from a 35mm independent film — a woman receiving news through glass. Available light only, unretouched, natural skin texture.

Constraints: cream blouse untucked, camel cardigan off one shoulder; her expression is flat and absorbing rather than shocked; keep every notice, card slot, sticker and reflected sign free of readable lettering.
```

### 2h.7 The last frame of Act 1 — plate

**Cast:** `@Karen`. **This is the one that has to be great.**

The pep talk has landed. *"Then get ringing."* The exit feeling is **I would not want
to be the person who answers her next call** — so the image is not triumph, it is
**settling in**. Shoulders squared, weight down, the phone box already looking like
somewhere she lives.

Pulled back further than 2h.6 and shot from outside through the smeared glass, because
the story leaves her here and comes back nine months later. It should rhyme with the
statue at the end without anybody having drawn the statue yet.

```prompt
SCENE:

Subject: a woman standing in a street phone kiosk with the receiver to her ear, seen from outside through the smeared glass, the street reflected over her.

Composition: 16:9, from across the pavement at chest height, the kiosk standing whole in the frame and slightly left of centre with the empty street beside it; a scaffolding leg crosses the near right foreground out of focus; the frame very slightly tilted.

Action: settling in — shoulders squared and dropped, weight gone down into her heels, her free hand flat on the shelf and her handbag set down on the floor of the kiosk by her feet, as if the call has a long way to go.

Location: the Midtown side street outside the kiosk on an ordinary weekday morning — scaffolding, a mesh bin, steam off a vent, the block going up out of frame behind; the glass smeared with handprints and old adhesive marks; a pedestrian passing in the reflection without looking.

Light: flat overcast mid-morning daylight, a bright white sky reflected in the upper panes; the interior of the kiosk a stop darker than the street.

Style: a still from a 35mm independent film — the closing frame of the first act, a small figure committing to something enormous. Available light only, unretouched.

Constraints: cream blouse untucked, camel cardigan slipped off one shoulder, no coat; her posture reads as settled and immovable rather than triumphant; keep every notice, hoarding, sticker and reflected sign free of readable lettering.
```

---

## Fire order, and what to watch

1. **2h.1** — the master. Accept it properly; 2h.4 has to copy it.
2. **2h.4** — the mirror, with 2h.1 attached. **Fire it second**, while the master is
   fresh in the project and easy to attach. If the rhyme misses, everything downstream
   still works, but the scene loses its best joke.
3. **2h.7** — the closing frame. Fire it early rather than last: it is the one that
   matters most and the one most likely to need rounds.
4. **2h.3** → **2h.6** → **2h.7** — the kiosk, outside then in then out again. 2h.3 is
   reference-anchored on Kai's phone booth image and **its accepted output is the
   reference for the other two**, so fire them adjacent and attach it forward each
   time. The kiosk has to be the same object in all three, and in Act 2 and Act 5.
5. **2h.2**, **2h.5** — the two easy ones. Neither has a hard binding or a hard
   composition; they will come back fine.

**What to watch on 2h.1 / 2h.4:** whether the two frames actually rhyme. Put them side
by side — if you have to *explain* that it is the same shot, it is not.

**What to watch on 2h.3 / 2h.7:** whether it has gone postcard. If the light has turned
golden, the street has emptied, or the skyline has arranged itself prettily behind her,
the model has reverted to type. The counter is more ordinariness, not more instruction.

**What to watch everywhere:** the highlights and the skin. If plates come back glossy,
over-contrasted or plastic, that is the
[NB2 over-sharpening risk](../../google-flow/nano-banana-2.md#the-calibration-risk-nobody-flags)
and the answer is to move to Nano Banana Pro, not to add words.

**Two regenerations, then rewrite.** Established rule `[community]` — if the same
prompt has missed twice, the prompt is wrong, not unlucky.

## Still open

- **Susan's pep-talk wording** is unlocked in canon
  ([`characters/susan.md`](./characters/susan.md), `story.md` §1.7 — *structure locked,
  words open*). None of these plates depend on it, but the clips will.
- **Susan's reference register.** Her Character plates are clean e-commerce photography
  rather than the shared `STYLE LOCK` — flagged in her sheet and still owed a ruling.
  §2h.4 and §2h.5 are a gentler test of it than the §2g night exterior was: same
  daylight, same room type as Karen's. **If she and Karen look lit by the same window
  here, the divergence is fine and the ruling is "leave it."**
- **Whether Karen genuinely forgot the firing** stays deliberately unresolved in canon.
  Nothing in these plates commits either way, and nothing should.

## Sources

The engine research behind this section — Nano Banana Pro's planning behaviour, the
*"descriptive, not repetitive"* rule, and the anti-slop tell→counter table — is written
up with its citations in
[`docs/google-flow/nano-banana-2.md`](../../google-flow/nano-banana-2.md#third-pass--nano-banana-pro-and-the-anti-slop-toolkit).
It is all `[untested]` against our own Flow session.
