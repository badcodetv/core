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
>
> **⚠️ Ruled 2026-08-16 (Kai): these are fired by hand, not by the automation.**
> Driving Flow through `@badcode/flow-mcp` cost more rounds than it saved after the
> August redesign. **The blocks below are therefore the deliverable** — each one is
> the complete thing to paste, `STYLE LOCK` + `SCENE:` + *"Thanks."*, with the cast,
> the time of day and whether anything is attached stated above it. Do not silently
> assume a reference image is attached; say so, per plate.

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

**Cast:** `@Susan`. **No reference image** — see the ruling below.

This is the joke, and the joke is entirely in the geometry: **the same shot, the other
woman.** It only lands if the framing is a copy.

> **Susan has her phone.** It is on the bedside table where Karen's charging cable was
> empty, and it is about to ring. That single swap is the scene's whole argument, and a
> candidate that loses the phone is a reroll.

> **⚠️ Rewritten 2026-08-16, after §2h.5 was accepted.** The original block predated
> Susan's flat existing, and is superseded on three counts:
>
> 1. **The room is no longer generic.** It was *"a tidier apartment bedroom"*; it is now
>    the established terracotta pre-war walk-up, copied verbatim from the accepted §2h.5
>    Location line. Two shots of the same bedroom have to describe the same bedroom.
> 2. **The camera clause is now stated the way §2h.5 stated it** — with focal length and
>    aperture, as its own lever. That is the version that finally landed after three
>    rounds of being ignored, and a matched pair only cuts together if the lens is
>    identical in both prompts.
> 3. **No frame-tilt request.** *"Not quite level"* came back level three for three on
>    §2h.5. Treat it as something Nano Banana Pro does not honour and get it in the edit.
>
> **Kai ruled 2026-08-16: no reference image, describe the room instead.** The earlier
> draft attached the accepted §2h.1 for composition. Dropping it removes the one real
> risk on this plate — **Karen's face bleeding out of the attached frame into Susan's
> shot** — and the room is proven to work from prose alone, three candidates for three on
> §2h.5. The cost is that the rhyme now rides entirely on the Camera and Composition
> clauses. **If the angle wanders, re-fire; do not add words.**

```prompt
SCENE:

Subject: a woman in her late thirties with long dark brown wavy hair parted in the centre and falling just past her shoulders, asleep on her front, one arm flung out across the mattress, minutes before the phone wakes her.

Camera: low-angle shot from her side at mattress height, 35mm at f/2, the near edge of the bed close to the lens.

Composition: 16:9. She lies right of centre. The room falls away to the left toward the window. The bedside table sits large and soft in the near foreground.

Action: still asleep, face turned into the pillow, mouth slightly open, one hand slack over the edge of the bed, the duvet kicked half off one leg.

Location: a small rented pre-war New York apartment bedroom, mid-morning. The walls are painted a deep terracotta burnt-sienna, with the ornate ceiling moulding and picture rail left chalky off-white and thickened by many layers of paint. A painted cast-iron radiator under the window. Worn narrow-strip parquet floor. Through the half-open venetian blind, a black iron fire escape and the brick wall of the building opposite, close enough to touch. Mismatched second-hand furniture: a bentwood chair with an olive suede bomber slung over it, jeans folded on the seat, a chest of drawers that does not match the bedside table. Paperbacks stacked on the floor beside the bed. A trailing pothos on the windowsill. The bedside table holds a lamp, a half-drunk mug, a pressed-out blister pack, a tangled charger cable, and a smartphone lying face-up with its screen lit.

Light: a hard ladder of daylight through the half-open venetian blind camera-left, striping across the headboard and her back. No other source. Uneven exposure, the window blown out behind the blind.

Style: a still from a 35mm independent film. Available light only. Hyper-realistic skin texture with visible pores and subtle imperfections. A faint smear on the lens, subtle handshake blur.

Constraints: hair fallen across her face, a pillow crease, dull skin, a sleep-creased t-shirt. Unposed and unaware of the camera. Keep every label, book spine and blister pack free of readable lettering.
```

**Note the placement is `right of centre, room falling left`** — the same way round as
§2h.5, and for the same reason: it must not fight `light … camera-left`. See the prompt
bug recorded under §2h.5.

> **✅ FIRED AND ACCEPTED 2026-08-16.** Fired by hand by Kai with `@Susan` cast, no
> reference image, and it landed. **This frame is now the room reference for everything
> else set in Susan's flat** — kept in-repo at
> [`img/2h4-susan-wakes-ACCEPTED.png`](./img/2h4-susan-wakes-ACCEPTED.png) so the record
> is self-contained; the copy to attach in Flow is the one in the project.
>
> **Two things the generation gave us that the prompt did not ask for, and both are
> keepers:**
>
> 1. **She fell asleep in yesterday's jeans and t-shirt.** A better hangover signal than
>    anything written — it says she did not get as far as undressing. **Carry it into
>    every later shot in this room as continuity.**
> 2. **The light came from frame right, not `camera-left`.** The window and fire escape
>    sit right of frame with the ladder of blind-light striping the wall at left. The
>    directional instruction was overruled by the model's own room layout. Downstream
>    prompts should **describe the frame as it actually is** rather than repeat
>    `camera-left`, which removes the fight recorded under §2h.5 rather than managing it.

### 2h.5a Susan explains — plate, **reference-anchored**

**Cast:** `@Susan`. **Attach the accepted §2h.4 frame** — role named in the prompt: the
room, the light and her clothing, *not* the camera.

Written 2026-08-16 at Kai's request. A minute into the call, mid-explanation —
*"Karen. Yesterday you got sacked. By an AI. And you dropped your phone in the river."*
It sits between §2h.5 (she answers) and the pep talk.

**Unlike §2h.4, the reference and the casting reinforce each other here.** The attached
frame contains Susan, and `@Susan` is bound — two signals for the same person instead of
the competing ones that made 2h.4 risky.

**The camera is deliberately different from §2h.4** — closer, and moved round toward the
foot of the bed. Same size and angle would be a jump cut; a change in both is a cut.

> **⚠️ The failure mode on this plate is the gesture getting big.** *"Gesturing while
> explaining"* is very close to the prompt that produces a stock-photo woman mid-
> presentation, which is the posed-and-stiff tell from the anti-slop table. Four clauses
> hold it down: **palm turned up, fingers loose, a few inches off the duvet, shoulders
> stay dropped.** The hand is explaining and the rest of her has not agreed to it. If a
> candidate comes back with the arm up and animated, **cut the gesture smaller** — do not
> add hangover words, which is the §4a trap.

```prompt
SCENE:

Use the attached image for the room, the wall colour, the furniture, the daylight and her clothing only — the same terracotta bedroom, the same bed, the same window and fire escape at frame right, the same clothes she fell asleep in. This is the next shot in the same continuous scene, a minute later. The camera position is different and is described below.

Subject: a woman in her late thirties with long dark brown wavy hair parted in the centre, slept on and tangled across one side of her face, still in yesterday's pale t-shirt and blue jeans, propped up on one elbow in the same bed with a phone held to her ear, mid-sentence, telling someone something they have not heard yet.

Camera: medium shot from her side, the lens a little above mattress height and moved round toward the foot of the bed, 50mm at f/2. The rumpled duvet crosses the near foreground, close and out of focus.

Composition: 16:9. She fills the left half of the frame, head toward the left. The window and the fire escape sit at frame right, the ladder of blind-light falling across the wall behind her. The bedside table is cut by the right edge.

Action: she has got as far as one elbow and no further. Her free hand is lifted a few inches off the duvet, palm turned up, fingers loose and slightly curled — a small flat gesture that has not left the bed, caught mid-word. Her lips are parted mid-sentence. Her eyes are half-lidded and aimed at nothing in particular, well past the person she is talking to. Her brows are relaxed and level. Her shoulders stay dropped.

Location: the same small rented pre-war New York apartment bedroom, mid-morning — terracotta burnt-sienna walls, chalky off-white ceiling moulding and picture rail, a painted cast-iron radiator, worn narrow-strip parquet, a bentwood chair with an olive suede bomber slung over it, and a bedside table holding a lamp, a half-drunk mug, a pressed-out blister pack, a pint glass of water and a tangled charger cable.

Light: daylight through the half-open venetian blind at frame right, striping the wall behind her. No other source. Uneven exposure, the window blown out behind the blind.

Style: a still from a 35mm independent film. Available light only. Hyper-realistic skin texture with visible pores and subtle imperfections. A faint smear on the lens, subtle handshake blur.

Constraints: a pillow crease across one cheek, hair stuck to the side of her face, dull skin, dry lips, one eye open slightly wider than the other, the t-shirt slept in and rucked. Unposed and unaware of the camera. Keep every label, book spine and blister pack free of readable lettering.
```

**Second thing to watch: whether she sits further up than one elbow.** The read is that
the news is casual to her and catastrophic to Karen — **she does not sit up for this.**

### 2h.5b Susan explains, overhead — plate, **reference-anchored** `[accepted]`

**Cast:** `@Susan`. **Attach the accepted §2h.4 frame** — room, bedding, light and
clothing only; the camera is completely different.

Kai's call, 2026-08-16: the same beat from directly overhead, *"like from the perspective
of her ceiling fan."* Accepted first time —
[`img/2h5b-susan-overhead-ACCEPTED.png`](./img/2h5b-susan-overhead-ACCEPTED.png).

**The angle is Tier 1** in [`camera-vocabulary.md`](../../flow/camera-vocabulary.md) —
bird's-eye is dependable. **The register is the problem**, because that file also says
what it reads as: *"bird's-eye = surveillance or flat-lay."* We want the surveillance
half. Four clauses push it off flat-lay and all four earned their place:

> **the bed runs diagonally · cropped by two edges · she lies off-centre, head nearer one
> corner · a held overhead of someone at their lowest, not a flat-lay**

That last one is an **intent** clause, and it is there because Nano Banana Pro reasons
about the prompt before drawing — telling it *what kind of shot this is* is an
instruction a planning model can act on.

> **⚠️ The clause that did the most work is in `Light`, not `Composition`:**
> *"the bars breaking and bending over every fold in the duvet."* Straight bars across a
> flat plane is what a fake overhead looks like; **bars that deform tell you there is a
> real three-dimensional mess underneath.** Steal this for any top-down.

> **A rejected idea, recorded so nobody re-adds it.** The first draft asked for *"the soft
> shadow of a ceiling fan blade across the foot of the bed"* to buy depth relief. **Kai
> cut it** — the fan was only ever his way of describing where the camera goes, and a
> literal fan in shot is set dressing nobody asked for. **The honest replacement is
> physical:** from directly overhead the floor sits about a metre further from the lens
> than she does, so at f/2.8 it falls soft on its own. Depth from the optics, not a prop.

```prompt
SCENE:

Camera: a bird's-eye shot looking straight down from ceiling height directly above the bed, 24mm at f/2.8, the bedding sharp and the floor beyond it falling soft because it sits further from the lens. Nothing of the ceiling is in frame.

Use the attached image for the room, the wall colour, the bedding, the parquet floor, the daylight and her clothing only — the same terracotta bedroom, the same bed, the same clothes she fell asleep in. This is the same continuous scene, seen from above.

Subject: a woman in her late thirties with long dark brown wavy hair fanned and knotted across the pillow, still in yesterday's pale t-shirt and blue jeans, sprawled on her back across the bed with a phone held to her ear, mid-sentence.

Composition: 16:9. This is a held overhead of someone at their lowest, not a flat-lay. The bed is not square to the frame — it runs diagonally across it and is cropped by two edges, with the worn parquet floor and the corner of the bedside table showing at one side. She lies off-centre, her head nearer one corner than the middle, the empty half of the mattress open beside her.

Action: she has sprawled rather than settled. One leg is out from under the duvet and hanging off the edge of the bed, the other tangled in it. One arm is flung up above her head, the back of the hand resting open on the mattress. Her other hand holds the phone loosely to her ear, the elbow dropped flat. Her head is turned to one side on the pillow. Her lips are parted mid-word. Her eyes are half-lidded and unfocused. Her brows are relaxed and level. Her jaw is slack between words.

Location: the same small rented pre-war New York apartment bedroom, mid-morning. Rumpled cream bedding, a twisted duvet, worn narrow-strip parquet showing beyond the foot of the bed, yesterday's shoes kicked off at odd angles on the floor, and the bedside table at the frame edge holding a lamp, a half-drunk mug, a pressed-out blister pack, a pint glass of water and a tangled charger cable.

Light: hard daylight through a half-open venetian blind out of frame, throwing a ladder of bright bars diagonally across the bedding and across her body, the bars breaking and bending over every fold in the duvet. The rest of the bed is in flat shadow. No other source.

Style: a still from a 35mm independent film. Available light only. Hyper-realistic skin texture with visible pores and subtle imperfections. A faint smear on the lens, subtle handshake blur, mild wide-angle stretch toward the corners.

Constraints: hair stuck to one cheek, dull skin, dry lips, the t-shirt slept in and rucked up at the waist, one sock on and one off. Unposed and unaware of the camera. Keep every label and blister pack free of readable lettering.
```

### 2h.4v Susan wakes to the phone — clip

**Engine:** Gemini Omni Flash · **Frames to Video**, the accepted §2h.4 as the **start
frame** · **no character ingredient** · 8s · native audio.

> **⚠️ Mode is an exclusive choice, and Kai confirmed it at the UI on 2026-08-16:
> Flow will not let you attach `@Susan` to a start frame.** Recorded in
> [`omni-flash.md`](../../google-flow/omni-flash.md#️-the-combined-mode-does-not-exist-in-flow),
> where it retires the `[runware]` "combined mode" claim.
>
> **It costs nothing here.** The start frame *is* Susan — her face, in position, in the
> right light — which is a stronger identity anchor than a reference tile. The tile
> exists for shots where nothing on screen shows her yet. Going to Ingredients to get the
> binding would have re-staged the room and thrown away the composition the whole shot
> is built on.

**The design decision: she never reaches the phone.** Fine hand articulation is the
model's documented weak spot, and the table sits past her hip from where her head is — a
clean grab is the hardest thing available *and* would read as staged even rendered
perfectly. So the clip ends on the blind grope.

> **This is the river-drop rule again, one scene later: render the reach, not the
> contact.** It is also the better performance. Hungover irritation is a blind swat, not
> a clean pick-up.

> **⚠️ The first version of this block was POLICY-BLOCKED, 2026-08-16.** The word was
> **`gropes`** — *"her hanging arm swings up and gropes blindly along the edge of the
> mattress"* — in a scene where a woman is lying on a bed. Nothing in the shot is
> remotely sexual; the classifier scans keywords, and **the setting supplied the second
> meaning.** Written up as trigger 5 in
> [`failure-modes.md` §A5b](../../flow/failure-modes.md#a5b-the-bedroom-problem--trigger-5-in-detail).
>
> Three changes went in. Only the first is diagnosis; the other two are insurance, and
> that is the right posture on a scene the filter is already primed for:
>
> | Was | Now | Why |
> | --- | --- | --- |
> | `gropes blindly along` | `feels its way along` | the suspected trigger |
> | `lying on her front` | `lying face-down across the bed` | adjacent, costs nothing |
> | `…and one dry breath in through her nose` | *(cut from the audio)* | a breath track over a woman on a bed buys nothing |
>
> **And turn Enhance Prompt off first.** Flow's auto-rewrite injects language you never
> wrote, and a plain prompt that blocks is often blocked for the enhancer's words.

```prompt
Using the attached image as the locked opening frame, animate what happens next. Keep the room, the bedding, the light and her hair and clothes exactly as they are in the frame.

She stays lying face-down across the bed throughout, exactly as in the frame. On the bedside table at frame right the phone screen lights and starts to buzz, rattling faintly against the wood. She stays still for a beat. Then her eyes open. Nothing else on her face moves. Her head lifts an inch off the mattress, turns a few degrees toward the sound, and drops back down onto it. Her hanging arm swings up and feels its way along the edge of the mattress toward the noise, patting at the bedding, still searching as the clip ends.

The camera is locked and still throughout. Available light only, real-time pace, and the camera is not helping — this is a fixed observational shot, not a composed one. Shot at 24fps with a 180-degree shutter, so the arm smears with natural motion blur as it swings. Fine film grain.

Audio is the room only: the low buzz of a phone vibrating on a wooden table and distant traffic through the window.
```

**Note every constraint is stated positively** — *"she stays lying face-down across the
bed"*, *"the camera is locked and still"*, *"audio is the room only"*. Negatives do not
work on Omni and actively backfire, so there is not a single "no" in the block.

> **❌ THIS VERSION FAILED — the Frames run came back as a different woman entirely.**
> 2026-08-16, Kai: *"she looks completely different."* The block above is kept as the
> record of what was fired, not as a brief.
>
> **The composition held and the face did not**, which is the sharpest limit we have
> found on the Frames tab and it disproves the reasoning written here two days earlier.
> **Frames buys composition, and composition only** —
> [`omni-flash.md`](../../google-flow/omni-flash.md#️-a-start-frame-does-not-hold-a-face),
> `[confirmed 2026-08-16]`. Since Flow will not let you attach a character to a start
> frame, **there is currently no way to get both on this engine.**
>
> **The rule that comes out of it: ask which one the shot cannot survive losing.** Susan's
> face is on screen and has to be hers, so this is an Ingredients shot. See §2h.4v-i below.

### 2h.4v-i Susan wakes to the phone — clip, **Ingredients**

**Engine:** Gemini Omni Flash · **Ingredients to Video** · `@Susan` **and** the accepted
§2h.4 still, both roles named in the first line · 8s · native audio · **Enhance Prompt
off**.

The same shot, re-routed after the Frames run lost her face. **The trade is exact and
worth stating both ways round:** Ingredients keeps the person and re-stages the ground,
where Frames kept the ground and lost the person.

**Which is why this block is three times longer.** In reference mode the text carries the
staging — a motion-only prompt leaves the model nothing to hold and it invents a scene.
The room paragraph deliberately **reuses the nouns from the §2h.4 image prompt**, per the
finding that keeping ~80% of descriptive keywords identical between shots sharing a
setting is what stops the environment drifting.

> **⚠️ The reference has Susan in it, so it is a dual-role image** — location and subject
> at once, which [`omni-flash.md`](../../google-flow/omni-flash.md#3--a-location-reference-must-not-contain-subjects)
> warns against. The model resolves that by **keeping the person and treating the room as
> loose atmosphere.** Here that is the right way round — the face is what we came for —
> but it is why the room description is doing so much work.

```prompt
Using the provided image as the reference for the bedroom and for how she is lying in it, and @Susan as the woman in the bed, create an eight-second shot.

The room is a small rented pre-war New York apartment bedroom in mid-morning: walls painted deep terracotta burnt-sienna, chalky off-white ceiling moulding and picture rail, a painted cast-iron radiator under the window, worn narrow-strip parquet, a bentwood chair with an olive suede bomber slung over it, and through a half-open venetian blind a black iron fire escape and the brick wall of the building opposite. A hard ladder of daylight comes through the blind at frame right and stripes the wall behind the bed. There is no other light. The bedside table at frame right holds a lamp, a half-drunk mug, a pressed-out blister pack, a tangled charger cable and a phone lying face-up.

Susan lies face-down across the rumpled cream bedding, head toward frame left, her long dark brown wavy hair parted in the centre and tangled across one side of her face, still in yesterday's pale t-shirt and blue jeans, one arm hanging off the near edge of the bed. She is asleep.

The phone screen lights and starts to buzz, rattling faintly against the wood. She stays still for a beat. Then her eyes open. Nothing else on her face moves. Her head lifts an inch off the mattress, turns a few degrees toward the sound, and drops back down onto it. Her hanging arm swings up and feels its way along the edge of the mattress toward the noise, patting at the bedding, still searching as the clip ends.

The camera is locked and still throughout, at mattress height from the side of the bed, wide enough to hold the whole bed and the bedside table. Available light only, real-time pace, a fixed observational shot rather than a composed one. Shot at 24fps with a 180-degree shutter. Fine film grain.

Audio is the room only: the low buzz of a phone vibrating on a wooden table and distant traffic through the window.
```

**What to watch:** whether the room survives. If it comes back generic, that is Ingredients
doing what Ingredients does — **add room nouns to the text, do not insist on the image.**
If it comes back as Susan in roughly the right room, take it; the identity is the thing
the other tab could not give.

**If she sits up**, cut the head-lift beat and let it be eyes-open plus the arm. **If the
phone slides or rattles unnaturally**, drop *"rattling faintly against the wood"* —
object motion is where it invents physics.

### 2h.5 Susan takes the call — plate

**Cast:** `@Susan`.

The news lands here: *"Karen. Yesterday you got sacked. By an AI. And you dropped your
phone in the river."* Her sheet is explicit that **the affection has to read through
the bluntness** — if she plays contemptuous, the pep talk becomes mockery and the hinge
snaps. So: unimpressed, patient, awake about four seconds, faintly amused. Not withering.

> **✅ FIRED AND ACCEPTED 2026-08-14 — candidate B of round 5.** Nano Banana Pro,
> `@Susan` cast **and verified**, 16:9, 3 candidates, no reference image. The block below
> is what was actually sent; it is a record now, not a brief.
>
> **Rounds 1–4 were all generated UNCAST and nobody knew.** `addCharacterToPrompt` was
> silently no-opping — every step best-effort, none of them throwing — so Flow returned a
> plausible stranger each time and the tool result looked like a success. That is why the
> woman changed between rounds, and why *"reinforce her hair in text"* appeared to help:
> with no binding attached, the prose was the *only* thing describing her.
>
> **The client now verifies the chip and throws `CHARACTER_ATTACH_FAILED` instead**
> (`packages/flow-mcp`, 2026-08-14). This round is the first with a genuine binding, and
> the face matches the Character tile for the first time.
>
> **Keep the hair clause anyway.** It costs nothing and it is what the reference research
> prescribes for drift — but it is now belt *and* braces rather than the only thing
> holding her together.

**Round 1 came back wrong in a way worth keeping**, because the cause was one clause:

| Round 1 said | What it produced |
| --- | --- |
| `her free hand pressed flat over her eyes` | **eyes shut, wincing — she read as hungover and in pain**, not listening |
| `from the side and slightly below at mattress height` (buried in Composition) | a front-on shot at seated eye level; the camera note was ignored |
| *(no imperfection tokens)* | a soft, pretty, show-home-tidy room — the plastic default |

**Susan's job in this beat is to be the one who is fine.** She is patient, unimpressed
and fond; the pain is Karen's. Round 2 fixed it with four changes, all straight out of
[`docs/flow/image-prompting.md`](../../flow/image-prompting.md):

1. **Eyes open and unfocused**, hand moved up into her hairline. One word — *open* —
   turned a wince into listening. **The single highest-value edit on this plate.**
2. **Camera promoted to its own clause with focal length and aperture** (§3's four
   levers): `low-angle shot from her side at mattress height, 35mm at f/2`. Stated as a
   lever it landed; buried in Composition it did not.
3. **Imperfection tokens** (§4 — "the model defaults to studio-perfect"):
   `hyper-realistic skin texture with visible pores`, `a faint smear on the lens`,
   `subtle handshake blur`, `uneven exposure, the window blown out behind the blind`.
4. **Environmental imperfection** — yesterday's jeans on the floor, a tangled charger
   cable, a mug going cold. The room stopped looking staged.

```prompt
SCENE:

Subject: a woman in her late thirties with long dark brown wavy hair parted in the centre and falling just past her shoulders, slept on and flattened on one side, sitting up against a headboard with a phone held to her ear, four seconds awake, listening to someone else talk.

Camera: low-angle shot from her side at mattress height, 35mm at f/2, the near edge of the bed close to the lens.

Composition: 16:9. She sits right of centre. The room falls away to the left toward the window. The rumpled duvet crosses the bottom of the frame, close and out of focus.

Action: she has not sat up and has not moved since it rang. She lies low in the bed with the phone resting against her ear, held by a hand that stays where it fell. Her other forearm is draped across her forehead just above her eyes. Her eyes are half-lidded and slow, aimed at the ceiling rather than at anything in the room. Her brows are relaxed and level. Her mouth is flat and slightly open. Her jaw is slack.

Location: a small rented pre-war New York apartment bedroom, mid-morning. The walls are painted a deep terracotta burnt-sienna, with the ornate ceiling moulding and picture rail left chalky off-white and thickened by many layers of paint. A painted cast-iron radiator under the window. Worn narrow-strip parquet floor. Through the half-open venetian blind, a black iron fire escape and the brick wall of the building opposite, close enough to touch. Mismatched second-hand furniture: a bentwood chair with an olive suede bomber slung over it, a chest of drawers that does not match the bedside table. Paperbacks stacked on the floor beside the bed. A trailing pothos on the windowsill. The bedside table holds a lamp, a half-drunk mug going cold and a tangled charger cable. Yesterday's jeans are on the floor where they were stepped out of.

Light: a hard ladder of daylight through the half-open venetian blind camera-left, striping across the headboard and her arm. No other source. Uneven exposure, the window blown out behind the blind.

Style: a still from a 35mm independent film. Available light only. Hyper-realistic skin texture with visible pores and subtle imperfections. A faint smear on the lens, fine grain, subtle handshake blur.

Constraints: a pillow crease across one cheek, hair stuck flat to the side of her face, dull skin, dry lips, one eye open slightly wider than the other, sleep-creased t-shirt. Unposed and unaware of the camera. Keep every label, book spine and blister pack free of readable lettering.
```

### Round 6 — she is wrecked, and the face does almost nothing

Kai: *more hungover, lying there like she is injured, not pleased to take the call.*
Three changes, and the third is a craft rule now written up in
[`docs/flow/image-prompting.md` §4a](../../flow/image-prompting.md#4a-expressions--name-the-muscles-never-the-emotion).

1. **She stops sitting up.** Flat on her back, low in the bed, forearm draped across her
   forehead, the phone held by *"a hand that stays where it fell."* Posture carries the
   hangover so nothing on the face has to.
2. **The state moves into the world.** A pressed-out blister pack and a half-drunk pint
   of water on the bedside table say it more reliably than any adjective on a face.
3. **⚠️ No emotion word appears in the prompt at all.** Not *hungover*, not *annoyed*,
   not the previous draft's *"weary and patient."* Only muscles: half-lidded eyes aimed
   at the ceiling, brows relaxed and level, mouth flat and slightly open, slack jaw.

> **Why that last one matters.** *"AI does not understand feelings. It understands
> facial muscles."* Naming a feeling is what produces the overacted AI face — ask for
> *sad* and you get a crying face. The trap on this particular beat is the
> **opposite-of-happy** reflex: reaching for a scowl to convey displeasure just gets you
> Angry Face, equally overacted. **Not-pleased-to-take-the-call reads truest as a face
> doing almost nothing.**

**Candidate B is the take**, and it is the first time the camera clause landed exactly —
lens level with her head on the pillow — which is worth noting after three rounds of it
being quietly ignored. C is the alternate: same read, camera a little higher, mouth
slightly more open.

### Susan's flat is not Karen's flat — round 3, at Kai's direction

Round 2's bedroom was generic and read as the same flat as Karen's. **That flattens the
one joke this pair of shots exists to tell.** Canon calls §2h.4 a *"mirror of the shot
we just did with Karen"* — and the rhyme is supposed to live in the **camera**, not the
room. Identical framing across two clearly different apartments is funny; identical
framing across two identical rooms is just a repeated shot.

**The class distance is already in canon and should be visible.** Karen is *"a rich
middle-class American woman"* with a country-club register — cashmere, a luxury key fob,
a structured leather handbag. Susan is late-30s New York, dry and lived-in: an olive
suede bomber, jeans, brown leather sneakers. **She rents a pre-war walk-up.**

The nine nouns that did the work, and they are all cheap:

> painted **cast-iron radiator** · a **fire escape** and the brick wall of the building
> opposite, close enough to touch · **worn parquet** · thick painted-over **ceiling
> moulding** · a **bentwood chair** · **mismatched second-hand furniture** ·
> **paperbacks stacked on the floor** · a **trailing pothos** · yesterday's jeans where
> they were stepped out of

**Save these for Karen's flat's opposite number.** Whatever her bedroom gets on a
re-shoot should be expensively bland where this is characterful — the contrast is the
point, and it costs nothing to write.

> **⚠️ A prompt bug worth not repeating.** Round 3's candidates all put her **right** of
> centre with the room falling **left** — the mirror of what the Composition line asked
> for. That is not the model ignoring left/right (round 2 honoured it): it is that
> `light … camera-left` and `she sits left of centre` were **fighting**, since obeying
> both would have put her in front of the window. The model resolved it sensibly.
> **When a placement instruction keeps flipping, check it isn't arguing with the light.**
> Round 4 simply stopped fighting it — the recorded prompt now says *right of centre,
> room falling left*, and it lands every time.

### Round 4 — the walls, and the drift `[accepted]`

Two more notes from Kai, both fixed in the block above.

**The room still read as Karen's flat**, because *"a small rented pre-war New York
apartment"* was doing all the differentiating work and the walls were still landlord
off-white — the same neutral as every generic bedroom. **Colour is the fastest way to
make two rooms read as two rooms.** The walls are now a deep terracotta burnt-sienna
with the moulding left chalky off-white, which does three things at once: it is
unmistakably a renter's own paint choice, the pre-war architecture stays legible against
it, and **the olive suede bomber pops** instead of disappearing. That last point is why
this is terracotta and not the obvious deep green — green would have swallowed her one
wardrobe signal.

**Susan was not in every candidate.** Character drift, which `docs/flow/consistency.md`
calls *"a probability, not a bug — budget a reroll on hero shots."* The counter that
worked, and it is the one the reference research already prescribed: **reinforce hair
and build in text, never the face.** The Subject line now carries *"late thirties, long
dark brown wavy hair parted in the centre, falling just past her shoulders."*

> **This is not a breach of the casting rule and the distinction matters.** The rule
> forbids describing a **face** in prose, because a described face competes with the
> Character binding. Hair, age and build **reinforce** it. After adding one hair clause,
> all three candidates came back recognisably Susan where the round before had drifted.

**Candidate C carries the trailing pothos** that B lost, and is the warmer, tighter
read. B has more architecture — moulding, picture rail, herringbone parquet, radiator
and fire escape all legible at once — which is why it is the take.

**Two notes for the next plate in this room.** Candidate **C** mirrored the composition
(her right of centre, room falling left) and gave the *best* camera of the three — a
true low side angle, with dust visible in the light beam. If a reverse of this setup is
ever needed, C is the reference to attach. And **the "few degrees off level" never
landed on any candidate** — three for three came back level, so treat frame tilt as
something Nano Banana Pro does not honour and get it in the edit instead.

> **⚠️ Susan's register question is now answered.** Her Character references are clean
> e-commerce photography rather than the shared `STYLE LOCK`, and
> [`characters/susan.md`](./characters/susan.md) has been waiting on a ruling. **The
> binding held** — she came back recognisably herself under a hard blind-light grade,
> across all three candidates. **The divergence is fine; the ruling is "leave it."**

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
