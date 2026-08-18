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
>
> ### ⚠️ Every prompt ends with *"Thanks."* — plates and clips alike
>
> Reaffirmed by Kai 2026-08-18 after it slipped on the clips. **The last line of every block
> that gets pasted into Flow is `Thanks.` on its own line**, images and videos both. Where a
> prompt is pasted as two blocks (a `REFERENCE` block and then the `STYLE LOCK` + `SCENE`),
> only the **final** block carries it, because the two are one paste.


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

Thanks.
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

Thanks.
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

> ## ⛔ SUPERSEDED 2026-08-17 — this is no longer the canon kiosk
>
> **The phone box is now the one generated in
> [`prompts-act2-escalation.md` §2j.0](./prompts-act2-escalation.md#2j0-the-corner-with-karen-in-it--plate)** —
> a full-height glazed booth with a scuffed aluminium frame, rust bleeding down it, peeled
> adhesive marks, a real payphone unit and a coiled metal cord, standing beside a subway
> entrance with steel railings and green glass globes. Kai ruled 2026-08-17 that **the Act 1
> kiosk was a different box** and that Act 1 gets re-fired against the new one.
>
> **Re-fire list, in order: §2h.3 → §2h.6 → §2h.7**, each with the new
> [`REFERENCE` block](#the-reference-block-for-the-kiosk-re-fires) prepended and the §2j.0
> frame attached. Then **re-run §2h.6v off the new §2h.6 still** — that clip's prompt text
> does not change at all; only the attached image does.
>
> **The Location sentence in §2j.0 is now the kiosk's canon description in prose**, since
> §2j.0 was generated with no reference of its own.
>
> ### The re-fire recipe — ⚠️ **rewritten 2026-08-18**
>
> **The block that used to live here was a list of refusals** — *"not its camera angle, not its
> framing, not the woman's pose."* That shape cost three rounds on
> [§2j.11](./prompts-act2-escalation.md#2j11-she-is-alone-in-it--plate) before it was diagnosed.
> Three findings from that fight, all recorded in
> [`nano-banana-2.md`](../../google-flow/nano-banana-2.md#fourth-pass--making-it-obey-a-reference-vendor-community-2026-08-18):
>
> 1. **Never write a negative.** Say *"keep it exactly as it is"* and then list what changes.
>    A refusal puts the refused thing into the prompt.
> 2. **Never re-describe the set.** Enumerating the kiosk's parts is an instruction to *draw*
>    them, not to copy them, and it draws them slightly differently every time — which is
>    exactly the drift these re-fires exist to remove. **Point at the picture.**
> 3. **With a reference attached, the `STYLE LOCK` becomes a pointer.** §2j.0 was generated in
>    the lock, so the reference *is* the lock; six words beat two hundred. **Unattached plates
>    still paste it verbatim.**
>
> **So the recipe is now a two-part sentence, not a block:** *"Image 1 is the reference. Keep it
> exactly as it is — … Redesign nothing."* followed by a numbered list of **only** what differs,
> each item written with **magnitude and consequences** (a strong reference meets a one-word
> change halfway) and **framing rather than camera distance** (*"she is no more than a third of
> the frame's height"*, never *"a wide shot from across the street"* alone).
>
> **§2h.6 and §2h.7 get written the same way when they come up.**

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

**Cast:** `@Karen` — the Character **and** the accepted **§2j.0** still as image 1. Two
references, nothing else. **Engine:** Nano Banana Pro, 16:9, 3 candidates.

**The change-list is short because almost nothing changes.** §2j.0 is the same corner, the same
woman, the same clothes and the same flat overcast mid-morning. **This shot is the same picture
from further away, one moment earlier** — before she has picked up the phone. That is the whole
delta, and keeping it that small is the point of re-firing against a canon still.

```prompt
Image 1 is the reference. Keep it exactly as it is — the same kiosk, the same subway entrance and corner behind it, the same woman, the same clothes, the same flat overcast mid-morning light, and the same grainy super-8 film look. Redesign nothing.

Change three things:

1. Much wider framing. She is a small figure no more than a third of the height of the frame, well left of centre, and the block above her rises out of the top of the frame.

2. She is arriving, not calling. She is half inside the kiosk, caught mid-stride with one hand on the frame and her back three-quarters to the camera, and she is not holding the receiver yet.

3. A scaffolding leg and a mesh litter bin cross the right-hand foreground close to the lens and out of focus.

Two pedestrians pass along the pavement without looking at her. No readable lettering anywhere, and no border around the image.

Thanks.
```

**What to watch, beyond the postcard:**

- **Is it the same kiosk, part for part?** The entire reason for the re-fire. Rust, peeled
  adhesive, the payphone unit, the coiled cord, the green globes on the subway posts. Any
  redesign and Act 1 still does not match Act 2.
- **Did the framing actually widen?** A strong reference
  [meets its change-list halfway](./prompts-act2-escalation.md#2j11-she-is-alone-in-it--plate) —
  §2j.11 asked for night and got dusk, asked for closer and stayed put. If she comes back the
  same size as in image 1, the lever is a consequence it cannot fake: *"the whole kiosk and
  three floors of the building above it fit in the frame."*
- **Is she mid-stride, without the receiver?** The moment-earlier beat is the only thing
  distinguishing this shot from §2j.0. A woman on the phone here is just §2j.0 from further
  back.
- **Is she too small to read?** She is deliberately minor in frame and the binding has
  little to work with. If she is unreadable, tighten the wide rather than enlarging her
  within it — §2h.6 is the close-up that confirms who it is, so this shot does not have
  to carry identification alone.
- **Worth one candidate at 21:9.** The engine offers it, we have never used it, and a
  small figure under a tall block is exactly the case where the 16:9 crop fights the
  scale. `[untested]`

### 2h.3v She picks up the phone — clip

**Cast:** none — **Frames takes no Character, and there is no face in this shot.** **Attach:**
the accepted §2h.3 still as the **starting frame**. **Engine:** Gemini Omni Flash · **Frames to
Video** · 8s · native audio · **Enhance Prompt off**.

**Tab: Frames**, by the
[amended rule](../../google-flow/omni-flash.md#-the-tab-rule--amended-2026-08-18-ingredients-holds-identity-frames-holds-staging):
her back is three-quarters to camera so **there is no face to lose**, and what this shot cannot
survive losing is the kiosk a whole re-fire was spent matching. **Ingredients would re-stage it**,
which is exactly what it did to §2j.11v.

> ### This is the hand-off. Act 1 ends with a hand closing on a receiver.
>
> Everything before it is a woman being fired and then being told to complain. **The last thing
> Act 1 does is show her pick up the phone** — and then Act 2 is nine months of that phone. It
> wants no cleverness at all: one movement, then stillness, then the credits of the act.

**⚠️ The one risk is the receiver, and it is the
[occlusion round trip](../../google-flow/omni-flash.md#-objects-vanish-on-the-occlusion-round-trip)
again.** A handset travelling from a cradle up to an ear on the far side of a turned head is
precisely the move that lost §2j.9v's mug. **The fix here is not to avoid the motion — it is the
beat — but to constrain it:** *"the receiver stays visible the whole way and never passes out of
sight."* State the visibility, not the trajectory.

**Everything with text in it gets pinned rather than blanked.** The accepted still already
carries lettering on the litter bin and the ad panel; the standing rule is about *new* text
appearing, so the instruction is *"stays exactly as it is"*, not *"stays bare."*

**The street keeps moving, modestly.** Direct traffic on a dry street has held every time we
have asked for it; it is [traffic through a distorting
surface](../../google-flow/omni-flash.md) that fails. A frozen Midtown is a worse error than a
small risk here — the whole point of the act is that the city does not care.

```prompt
Use the attached image as the starting frame. One continuous shot.

Her hand closes on the receiver, lifts it off the hook and raises it to her ear in one unbroken movement. The receiver stays visible the whole way and never passes out of sight. She settles her weight onto both feet and stands there waiting, her back still three-quarters to the camera. She does not turn round.

The camera does not move. Traffic passes along the street beyond her and the two pedestrians on the pavement keep walking without looking at her. Everything else stays exactly where it is: the litter bin, the scaffolding and the kiosk do not change, and every sign, panel and notice stays exactly as it is.

Real-time pace, 24fps with a 180-degree shutter. Fine film grain.

Audio is the street: the clunk of the receiver coming off its hook, traffic, footsteps on the pavement and a bus pulling away somewhere out of shot. No dialogue.

Thanks.
```

**What to watch:**

1. **Does the receiver survive the trip?** The known failure. If it vanishes or reappears wrong,
   the fallback is to **stop the movement early** — *"she lifts the receiver off the hook and
   holds it at chest height"* — and let §2h.6 open with it already at her ear.
2. **Does she turn round?** She must not. Her turning makes it a different shot and puts a face
   in a clip that has no Character attached to hold one.
3. **Does the kiosk hold?** Frames pins frame 0, so a change here would be new information.
4. **Do the pedestrians make it across?** A walker vanishing mid-stride
   [has happened before](./prompts-act2-escalation.md#2j5v-rung-1-the-block--clip). If they
   glitch, cut them from the picture and leave the footsteps in the audio — that fix has worked
   twice.
5. **Is the receiver clunk there?** It is the sound of the whole film starting, and it is worth
   a re-roll on its own.

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

Thanks.
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

Thanks.
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

Thanks.
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

Thanks.
```

**Note every constraint is stated positively** — *"she stays lying face-down across the
bed"*, *"the camera is locked and still"*, *"audio is the room only"*. Negatives do not
work on Omni and actively backfire, so there is not a single "no" in the block.

> **✅ ACCEPTED 2026-08-16 — but read the tab line, because it is not the one this
> heading says.**
>
> **The text above is exactly what worked. It was fired in the Ingredients tab**, with
> the still attached and `@Susan` added — *not* in Frames, despite opening with
> *"the locked opening frame."* The Frames run of the same plate came back as a different
> woman.
>
> **So the accepted recipe is: Ingredients + the accepted still + the Character +
> Frame-shaped prompt text.** The *"locked opening frame"* wording appears to work as text
> reinforcement inside Ingredients, which is not what the research predicted — it says
> Ingredients re-stages and wants the scene written out in full. Here it did not re-stage.
>
> **⚠️ I got this wrong twice in one day and both errors were the same error.** First I
> declared *"a start frame does not hold a face"* from one Frames failure; then I
> retracted it from one success that turned out to be a different tab. **Generalising a
> capability claim from a single generation is the mistake** — every run is n=1 on a
> stochastic model. The discipline note now sits in
> [`omni-flash.md`](../../google-flow/omni-flash.md#frames-lost-the-face-ingredients-held-both-n1-each-way):
> record what was fired, in which tab, and what came back; promote nothing to a rule until
> it repeats with something else varying.

### 2h.4v-i Susan wakes to the phone — the long Ingredients block · **kept as reference**

> **Not needed — the short block above was accepted.** This one was written on the
> assumption that Ingredients must carry the whole staging in prose. **It did not turn out
> to be necessary**, which is itself the finding. Kept as the worked example of the
> full-length Ingredients shape, for the next shot that has no plate to start from.

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

Thanks.
```

**What to watch:** whether the room survives. If it comes back generic, that is Ingredients
doing what Ingredients does — **add room nouns to the text, do not insist on the image.**

**If she sits up**, cut the head-lift beat and let it be eyes-open plus the arm. **If the
phone slides or rattles unnaturally**, drop *"rattling faintly against the wood"* —
object motion is where it invents physics.

### 2h.5bv Susan explains, overhead — clip

**Engine:** Gemini Omni Flash · **Ingredients to Video** — the accepted §2h.5b overhead
attached **plus `@Susan`** · 8s · native audio · **Enhance Prompt off**.

**Same recipe as the accepted §2h.4v**, deliberately: Frame-shaped prompt text fired in
the Ingredients tab. It is the only combination that has produced an accepted clip in
this room, so nothing about it changes except the action.

Kai's brief, 2026-08-16: *annoyed and hungover, gesturing like she is explaining what
happened last night.*

> **⚠️ Not one emotion word is in the block.** *Annoyed* is the fastest route to an
> overacted face, and the **opposite-of-happy reflex** — reaching for a scowl — just gets
> you Angry Face, equally overacted
> ([`image-prompting.md` §4a](../../flow/image-prompting.md#4a-expressions--name-the-muscles-never-the-emotion)).
> What reads as annoyed is **a face doing almost nothing while the mouth keeps working**,
> plus **one blink held a beat longer than it needs to be.** That blink is the whole
> performance and it is the cheapest thing in the prompt.

Three other choices, each with a reason:

1. **The voice is indistinct.** Ask Omni for a line and it writes a script that will not
   match Susan's real dialogue when the VO goes on in post. Indistinct buys natural mouth
   movement with nothing to sync against — and at this distance overhead nobody is reading
   her lips. **The same logic as blurring signage rather than inventing a wordmark.**
2. **Exactly one ambient motion: dust in the light bar.** A locked overhead with nothing
   moving but the actor reads as a still with a person animated on top. A breathing beat
   was drafted and cut — `animate-slide`'s rule is *one* ambient motion, and competing
   ones are where these get muddy.
3. **The gesture is a wrist and a forearm, not a hand.** Fine finger articulation is the
   documented weak spot, and her arm is already up above her head in the plate, so the
   move starts from where it is instead of travelling across frame.

```prompt
Using the attached image as the locked opening frame, animate what happens next. Keep the room, the bedding, the light and her hair and clothes exactly as they are in the frame.

She stays sprawled across the bed throughout, exactly as in the frame, the phone held to her ear. She is talking, and she has been talking for a while. Her mouth moves with the words without exaggeration. Her eyes stay half-lidded and aimed at the ceiling, her brows relaxed and level. One slow blink, held a beat longer than it needs to be. Her free arm, resting above her head, lifts a few inches off the mattress — the wrist turning over so the palm faces up, the forearm making one small loose circle as she explains something — then drops back down where it was.

The camera is locked and still throughout, directly overhead. Available light only, real-time pace, and the camera is not helping — this is a fixed observational shot, not a composed one. Dust drifts through the bar of daylight lying across the bed. Shot at 24fps with a 180-degree shutter. Fine film grain.

Audio is the room only: her voice low, flat and indistinct under distant traffic through the window.

Thanks.
```

**What to watch: whether the gesture inflates.** If she starts conducting, cut *"the
forearm making one small loose circle"* and leave the wrist turning palm-up — **that alone
reads as explaining.** Second, whether she stays on the bed; she should not move off it.

> **Policy note.** *"Sprawled across the bed"* is deliberate — after §2h.4v was blocked on
> `gropes`, every bedroom block gets read back for words that look bad quoted next to the
> location. *"On her back"* was avoided for the same reason, and costs nothing since the
> frame already shows the pose.

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

Thanks.
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

### 2h.6 The news lands — plate · **re-fired against the canon kiosk**

**Cast:** `@Karen` — the Character **and** the accepted **§2j.0** still as image 1. Two
references, nothing else. **Engine:** Nano Banana Pro, 16:9, 3 candidates.

Interior of the kiosk, and the counter-shot to §2h.5. She has just been told. **No reaction
acting** — the beat is the information arriving, not her performing shock.

> ### ⚠️ Corrected 2026-08-18 (Kai): **the kiosk has no door, so there is no glass in front of her.**
>
> Round 1's block asked for the street *"reflected across the glass in front of her"* while the
> camera stood at the **open front**. There is nothing there to reflect in — and asking for a
> reflection where no surface exists is an invitation to **invent a glass door**, which is
> exactly the mechanism that
> [rebuilt the booth in §2j.11 round 2](./prompts-act2-escalation.md#2j11-she-is-alone-in-it--plate):
> *when the shot needs a surface the set does not have, the model builds the surface.*
>
> **The fix keeps the idea and moves the camera to where glass genuinely is** — the glazed
> **side** panel, with her in profile. A person can stand there, so the set survives. It also
> buys Act 1 its own angle rather than repeating §2j.11's three-quarter from the front.
>
> **And the geometry is now stated outright in the prompt** — *"the front of the kiosk is open,
> with no door and no glass across it"* — because a set fact left unsaid is a set fact the model
> gets to decide.

> ### ⚠️ Round 2 fired 2026-08-18 — *"it still has reflections where there isn't glass… it seems to do it naturally when you don't ask."*
>
> **Kai's second clause is the rule.** The reflection came back smeared across her hair and
> cheek as a double-exposure, because **naming a reflection makes it an effect to apply rather
> than a property of a surface.** Round 2 had already moved the camera to a real pane; that was
> not enough, because the instruction itself is the problem.
>
> ### The atmosphere family is rendered for free and overdelivers when named.
>
> **Reflections, dust, steam, haze, bokeh** — the engine puts them in unasked, because they are
> everywhere in the reference photography it learned from. **Name one and it becomes the subject
> of the shot.** Exactly the [dust
> lesson](./prompts-act2-escalation.md#2j9v-rung-4-the-speakerphone--clip), which was written up
> as a fact about particles when it was really a fact about atmosphere.
>
> **Note the asymmetry with weather, which is the mirror image**: weather nouns *underdelivered*
> and needed magnitude pushed at them (*"a full storm, not a light dusting"*). **Atmosphere
> needs deleting; weather needs shouting at.**
>
> **So round 3 deletes the reflection clause entirely and says nothing about glass at all.**
> Everything else in round 2 was right — profile, camera at the side, open front intact, no
> invented door — so nothing else changes.

> ### ⚠️ Kai, 2026-08-18: *"what camera shot is this supposed to be, because it is showing multiple."*
>
> **Fair, and the fault is a missing background.** The intended shot is one camera: **a medium
> close-up in profile, eye level, from the pavement at the side of the kiosk.** What came back
> read as several, and the reason is optical rather than mysterious —
>
> **a phone kiosk is a glass box.** Side-on, the lens looks *through* the near panel, past her,
> *through* the far panel, at the street — while the near panel reflects the street behind the
> camera. **Four image layers in one frame.** Real, but it reads as a double exposure instead of
> a shot.
>
> ### Give the camera a position **and** a background. A position alone is half a shot.
>
> Round 3 said where the camera stood and never said what was behind her, so the engine filled
> the background with everything available at once. **An undefined background stacks, the same
> way an [undefined surface grows
> text](../../google-flow/omni-flash.md).** The fix is one sentence naming a single soft
> backdrop, and dropping the extra foreground layer we did not need.
>
> **Name the shot type too.** Nano Banana's documented camera form is
> *"[shot type] of image 1"* — *"a medium close-up in profile"* is a thing it knows how to
> frame; *"the camera has moved round to the side and is close"* is a description of a tripod.

> ### The idea survives without any of the effects.
>
> **We are watching her from outside**, which is where the rest of the film watches her from —
> through glass, across a pavement, from a helicopter, from a room she is not allowed into. That
> reading comes from **where the camera is standing**, not from reflections laid over her face.

**Reference: §2j.0, not §2j.11.** Both are canon, but §2j.0 is the same time of day, the same
light and the same clothes, so **the only thing changing is the camera**. Do not attach both
stills; two references of the same set are a third opinion on it.

**§4a, hard: name the muscles, never the emotion.** *"She has just found out"* is the cue that
produces a woman doing Shocked. The muscles are what is actually devastating — a face that has
gone flat while it absorbs something.

```prompt
Image 1 is the reference. Keep it exactly as it is — the same kiosk, the same corner behind it, the same woman, the same clothes, the same flat overcast mid-morning light, and the same grainy super-8 film look. Redesign nothing.

The front of the kiosk is open, with no door and no glass across it, exactly as in image 1.

Change two things:

1. A medium close-up of her in profile, taken from the pavement at the side of the kiosk at her eye level. She fills the left half of the frame, facing out of the open front towards the right of the frame. Behind her is one soft out-of-focus background and nothing else: the far side of the kiosk and the street beyond it, all of it blurred, with nothing sharp anywhere except her.

2. She has gone completely still. The receiver is against her ear and her other hand is flat on the shelf. Her face is flat and absorbing rather than shocked — her mouth is closed, her jaw is loose, her eyebrows are level — and she is looking straight ahead out of the open front, not at the camera.

No readable lettering anywhere, and no border around the image.

Thanks.
```

**What to watch:**

1. **Does it read as one shot?** The round-3 failure. **Only her should be sharp**; if the
   street behind her is as crisp as her face, the layers stack again and it stops looking like
   a photograph of a person.
2. **Is her face clean?** No ghosting or double exposure across her hair and cheek. Reflections
   *in* the panel are fine; a reflection *over* her is the failure.
3. **Did it grow a door?** The front must still be open.
4. **Is she acting?** A dropped jaw, wide eyes, a hand to the mouth — reject. The line to add is
   *"her face barely changes at all."*
5. **Same kiosk?** Rust, peeled adhesive, the shelf, the coiled cord. It is why the re-fire
   exists.

> **Keep this still.** [§2h.6v](#2h6v-karen-listens-in-the-kiosk--clip) is re-run off it with
> **its prompt text completely unchanged** — only the attached image differs. That clip was
> already accepted against the old booth; it does not need rewriting, just re-firing.

### 2h.6v Karen listens in the kiosk — clip

**Cast:** none — **Frames takes no Character.** **Attach:** the accepted **§2h.6** still (the
profile with the blurred street) as the **starting frame**. **Engine:** Gemini Omni Flash ·
**Frames to Video** · 8s · native audio · **Enhance Prompt off**.

> ### ⚠️ Rewritten 2026-08-18 — §2h.6 is a different shot now, so its clip is too.
>
> The block below used to be **a push-in with an arc, fired off a wider still** — it says so
> itself: *"a push-in needs somewhere to travel from."* **The accepted §2h.6 is already a tight
> profile**, so there is nowhere to push from, and the arc would have to invent the far side of
> a kiosk the shallow focus has deliberately dissolved.
>
> **The old block is kept below the new one**, because its craft is still the best writing in
> this file on *how to make a camera move do something* — the reflection sliding off her face,
> the late settle, the four physical events that buy "confused" without an emotion word. **Reuse
> it on a shot that has room.**

> ### The blur is not just a look — it is protection.
>
> Kai kept this frame for the shallow focus, and it buys something the film has been fighting
> for all week: **blurred traffic has no geometry to get wrong.** Sharp vehicles have
> interpenetrated, vanished and [failed through
> glass](../../google-flow/omni-flash.md); a soft yellow shape drifting across a bokeh
> background is [formless
> motion](../../google-flow/omni-flash.md#why-falling-objects-fail-and-what-actually-fixes-it),
> which is the one kind these engines never break. **For once the street can stay alive on
> screen instead of being demoted to audio.**
>
> **So the focus itself has to be pinned**, because it is now doing real work: *"the focus stays
> on her face for the whole shot; the street behind her stays a soft blur."*

**Camera locked, and that is a decision.** A push-in on a shallow frame makes the engine re-rack
focus, and the blur is the thing being protected. **The motion budget goes entirely into her
face** — which is right for the beat anyway: this is the moment the news lands, and the news
lands on a person who has stopped moving.

**She does not speak.** She is receiving. It also removes the lip-sync risk from a profile
close-up, which is the shot type least able to survive it.

```prompt
Use the attached image as the starting frame. One continuous shot.

The focus stays on her face for the whole shot and the street behind her stays a soft blur.

She is listening. She breathes in and out once. Her eyes lower a little and come back up. She moves the receiver a small amount against her ear and settles it again. Her mouth stays closed, she does not speak, and she does not turn towards the camera.

The camera does not move. Behind her the blurred traffic drifts slowly across the frame as soft shapes of colour with no hard edges. Everything sharp in the frame stays exactly where it is: the payphone, the coiled cord and the kiosk frame do not move, and every sticker and mark on them stays exactly as it is.

Real-time pace, 24fps with a 180-degree shutter. Fine film grain.

Audio: a small indistinct voice talking on the line, too faint to make out any words, and the muffled sound of the street — traffic, footsteps and a bus somewhere out of shot. No dialogue from her.

Thanks.
```

**What to watch:**

1. **Does the background stay blurred?** The reason this still was kept. If the street sharpens
   up as the clip runs, the fallback is a consequence rather than a restatement: *"only her face
   is ever in focus; everything behind her is soft shapes of colour."*
2. **Does she speak?** She must not. A moving mouth in a profile close-up is the hardest thing
   in this film to get away with.
3. **Do the sharp props hold?** The payphone, the cord and the peeled stickers are the only
   hard-edged things in frame, which makes them the only things that can visibly break.
4. **Does the blurred traffic behave?** It should — formless motion is the safe kind. If it
   somehow does not, that is genuinely new information and worth recording, because it would be
   the first time.
5. **Is the voice on the line, not in the room?** The whole beat is information arriving from
   somewhere else.

---

<details>
<summary><strong>⛔ Superseded — the push-in-and-arc version, written for a wider still.</strong> Kept for its camera craft; reuse it on a shot with room to travel.</summary>


**Engine:** Gemini Omni Flash · **Ingredients to Video** — an accepted kiosk still of Karen
attached **plus `@Karen`** · 8s · native audio · **Enhance Prompt off**.

**Attach the wider kiosk still** (§2h.3 or §2h.7 framing), not the tight through-glass
§2h.6 close-up: this shot is a push-in and a push-in needs somewhere to travel from.

Kai's brief, 2026-08-17: *confused and actively listening, no exaggerated expressions;
start on her in the booth and slowly push in to her face.* The counter-shot to §2h.5bv —
Susan talks, Karen takes it.

> ### Round 1 fired 2026-08-17 — rejected on two counts
>
> | What round 1 said | What came back |
> | --- | --- |
> | `Traffic moves in the reflection behind her` | **"very strange"** — the vehicles in the glass |
> | a straight push-in, one move | technically correct and **boring** |
>
> **Reflected traffic is close to the worst ask there is.** A reflection is *geometry*, and
> [these models have no world model](../../google-flow/omni-flash.md#spatial-geometry-models-have-no-world-model) —
> the engine has to solve where a vehicle is, where its mirror image lands and how both
> move, every frame. It is the [falling-object problem](../../google-flow/omni-flash.md#why-falling-objects-fail-and-what-actually-fixes-it)
> wearing a different coat. **Round 2 cuts moving objects from the glass entirely** and
> keeps the traffic in the *audio*, where it costs nothing and reads free.
>
> **The ambient motion is now formless** — steam off a pavement vent. Formless motion has
> no geometry to get wrong, which is exactly why dust and steam keep turning up in these
> blocks.
>
> **And the fix for boring is not a busier camera, it is a camera that causes something.**
> Round 2 arcs as it pushes, so the kiosk upright sweeps through the near edge of frame and
> **the white sky reflection slides off the glass and gives up her face.** That is an event
> in the shot rather than a move performed at it — and it is the story in one gesture, since
> the whole film watches her through glass and this is where it gets inside.

> **⚠️ The camera paragraph is promoted above the action paragraph here**, which reverses
> §2h.4v and §2h.5bv. Omni Flash reads `push in` as one of its named camera phrases and
> **the first words set the shot grammar** `[runware]` — the same rule as
> [`camera-vocabulary.md` §1](../../flow/camera-vocabulary.md#rules), *"camera instruction
> goes first, as its own clause."* The frame-lock line still has to come first for
> identity, so camera takes second position. **Push-in is Tier 1, the safest move there is;
> the arc round 2 adds is Tier 2, "works, expect retries."** Two moves is the documented
> maximum — do not add a third.

**Confusion is bought with four physical events and no emotion word:**

1. **focus set past the glass** — the eyes are open and looking at nothing;
2. **one slow blink**;
3. **the mouth opens a fraction and closes again without a word** — *she starts to say
   something and doesn't* is what confused-and-listening actually looks like;
4. **a chin dip smaller than a nod.**

That third one is the whole performance. The wider research agrees with
[`image-prompting.md` §4a](../../flow/image-prompting.md#4a-expressions--name-the-muscles-never-the-emotion)
from the other direction: **over-specifying an expression is itself what produces
overacting** `[community]`, so four small events beat a paragraph of feeling.

Three other choices, each with a reason:

- **The reflection slides off her face as the camera closes.** One motivated change that
  only a real move could produce — it is the anti-scaling tell as much as an atmosphere
  clause.
- **The move settles a fraction late.** Round 1's *"the camera is not helping — a plain
  observational push-in, not a composed one"* was written for a locked-off frame and it
  argues with a move; it is gone. **Weight and drift replace it.** AI camera moves are
  unnaturally perfect, so an imperfect settle is the realism token a moving shot needs —
  the same job [the 180-degree shutter](../../google-flow/omni-flash.md#the-shutter-is-the-tell-nobody-prompts-for)
  does for motion blur.
- **Her hand does not move.** She is holding a receiver next to her face for the whole
  clip, which puts fingers in shot at the closest point. Motionless hands render;
  articulating ones are the documented weak spot.
- **The receiver voice is indistinct.** Same logic as §2h.5bv — Susan's real dialogue goes
  on in post, so there is nothing here to fail to match.

> **⚠️ "In one continuous shot" is not decoration.** Omni's documented default is to **cut** —
> left alone it builds a little sequence out of two or three angles, which is the single
> most likely way to lose a slow push. Say it in the opening line.

```prompt
Using the attached image as the locked opening frame, animate what happens next in one continuous shot. Keep the kiosk, the street, the glass, the light and her hair and clothes exactly as they are in the frame.

The camera pushes in and arcs at the same time. It starts exactly where the frame starts, then moves toward her and around to one side, slowly and steadily, so the street slides across behind her and the aluminium upright of the kiosk sweeps through the near edge of the frame and out of it. The bright white reflection of the sky slides off the glass as it goes and her face comes clear behind it. The move slows as it arrives and settles on a medium close-up of her face through the glass, a little off to one side of her. It carries the weight and drift of a real dolly and settles a fraction late. It is the only camera move in the shot.

She is listening, and she has been listening for a while. Her eyes are open and set on nothing, focused somewhere past the glass rather than on anything in the street. Her brows stay level, the inner ends drawing very slightly up and together once. One slow blink. Her lips are parted and stay parted; her mouth opens a fraction as if to say something, then closes again. Her chin dips once, barely — less than a nod. Her hand stays where it is on the receiver, still.

Available light only, real-time pace. Behind the kiosk, steam lifts and drifts from a vent grate in the pavement. The street itself is quiet and still. Any lettering on the kiosk and in the reflections stays soft and unreadable. Shot at 24fps with a 180-degree shutter. Fine film grain.

Audio is the street only: distant traffic somewhere out of shot, and the thin indistinct sound of a voice in the receiver, too faint to make out any words.

Thanks.
```

**What to watch:**

- **Whether the arc breaks it.** The one real risk in round 2: an arcing camera has to
  render the side of the kiosk it never saw, and unseen ground is where these
  [invent](../../google-flow/omni-flash.md#the-unrendered-region-rule--why-it-invented-a-shore).
  **The fallback is exact** — cut *"and around to one side"* and the *"sweeps through the
  near edge"* clause, keep the rest. That is round 1's straight push plus the reflection
  reveal and the settle, which was most of the improvement anyway.
- **Whether the push is a dolly or a zoom.** A real move changes perspective — the kiosk
  frame should widen past the edges of shot as you close. If the image only scales up, add
  *"the kiosk frame passes out of the sides of the frame as the camera comes in."*
- **Whether the face starts performing.** Cut the inner-brow clause first; it is the one
  line that can be read as an instruction to emote.
- **Whether the reflection swallows her.** If she ends behind white glare, replace the
  slide-off with *"the glass is clear over her face by the end of the move."*
- **Whether she speaks.** She is receiving, not talking. Dialogue coming back is the audio
  lottery — reroll, do not rewrite.

</details>

### 2h.7 The last frame of Act 1 — plate · **re-fired against the canon kiosk**

**Cast:** `@Karen` — the Character **and** the accepted **§2j.0** still as image 1. Two
references, nothing else. **Engine:** Nano Banana Pro, 16:9, 3 candidates.

**This is the one that has to be great.** The pep talk has landed — *"then get ringing"* — and
the exit feeling is **I would not want to be the person who answers her next call.** So it is
not triumph. It is **settling in**: shoulders down, weight in her heels, the bag on the floor,
the kiosk already looking like somewhere she lives.

> ### Round 1 fired 2026-08-18 — ✅ the angle, ⛔ the world.
>
> **Kai: *"I like the camera angle, keep that, but make it match the reference for the
> setting."*** The plinth idea landed exactly. What came back with it was **an open plaza**: the
> kiosk free-standing on an island, the subway entrance a long way off to the right, no
> scaffolding, and the whole thing shot on something close to a fisheye with the buildings
> bending.
>
> ### ⚠️ The camera demanded room the corner does not have — so it built the room.
>
> Third sighting of [the same
> mechanism](../../google-flow/nano-banana-2.md#6--if-the-camera-cannot-physically-stand-there-the-model-rebuilds-the-set):
> §2j.11 round 2 enlarged a booth to fit a camera inside it, §2h.6 grew a glass door to hold a
> reflection, and here **a low wide shot from across the pavement, with the whole building above,
> needs a plaza.** The canon corner has scaffolding on the near side and a subway entrance
> immediately behind — there is nowhere to stand and take that picture. **So the model moved the
> kiosk somewhere the picture was possible.**
>
> **Generalise it once more: the set gives way to whatever the shot requires.** Camera position,
> a reflective surface, and now *space* — if the framing implies room the reference does not
> have, the reference loses.
>
> ### ⚠️ The fix is one reference and a legal camera position — **ruled by Kai 2026-08-18**
>
> A draft of round 2 attached **two** stills with declared jobs (§2j.0 for the world, round 1's
> frame for the angle), on the documented ground that naming each image's role is the supported
> pattern. **Kai overruled it:** *"just describe the camera angle — too much extra info/images
> in the prompt seems to mess it up."*
>
> **That is consistent with everything this file has learned the hard way.** Prompt length
> correlates negatively with adherence; the keep-list drifted because it re-described a picture;
> §2j.11 only worked once it was cut to ~150 words. **A second image is more input competing for
> the same attention, and role labels do not make it free.** One reference, described relations
> kept to a minimum.
>
> ### So the camera has to be described in words that do not demand a plaza.
>
> Round 1's wording — *"a wide shot from across the pavement"* — is what bought the open space.
> **The replacement names a spot the reference actually contains: standing under the scaffolding,
> a few steps in front of the kiosk, camera down at knee height.** A photographer could be there.
>
> **Naming where the photographer stands beats naming what the shot looks like**, when the risk
> is the set. It converts an abstract framing into a position the model can check against the
> picture it was given.
>
> **And the lens gets named.** Naming a focal length does
> [more work than any other single addition](https://imagera.ai/blog/best-prompts-realistic-ai-images-2026),
> and it solves two problems here: **28mm keeps the low angle without the ultra-wide bend** —
> bent verticals are a slop tell — **and a narrower field is less world for the model to invent.**

> ### The design idea, unchanged: the kiosk is a plinth.
>
> The story leaves her here and does not come back for nine months, and **Act 5 puts a statue on
> this corner.** The closing frame of Act 1 should already have the shape of a monument in it
> without anybody having drawn a statue yet. Nobody needs to notice; it pays off four acts later.
> **It is also what keeps this from being §2h.3 twice** — that one is eye level with her small
> and arriving; this is low, closer, and she has stopped moving.

> ### The people stay in, and that is the canon note, not a hedge.
>
> §2j.0's ruling: *"'no crowd' does not mean an empty street — it means nobody is looking at
> her."* A deserted Midtown pavement at mid-morning reads post-apocalyptic. **The isolation here
> is that she is the only person on the street who has stopped.**

**Cast:** `@Karen` — the Character **and** the accepted **§2j.0** still as image 1. **One
reference, nothing else.** **Engine:** Nano Banana Pro, 16:9, 3 candidates.

```prompt
Image 1 is the reference. Keep it exactly as it is — the same kiosk, the same subway entrance immediately behind it, the same scaffolding, the same corner, the same woman, the same clothes, the same flat overcast mid-morning light, and the same grainy super-8 film look. Redesign nothing. It is a narrow Midtown side street and the kiosk stands against the pavement, not free in the middle of an open space.

Change two things:

1. A low-angle shot on a 28mm lens, taken from the pavement a few steps in front of the kiosk, standing under the scaffolding, with the camera down at about knee height looking up at her. The kiosk stands whole in the frame a little left of centre with her inside it, and the building behind it goes up out of the top of the frame. Vertical lines stay close to straight.

2. She has settled in. The receiver is against her ear, her free hand is flat on the shelf, her shoulders are squared and dropped, her weight is down in her heels, and her handbag is standing on the floor of the kiosk by her feet. Her chin is level and her face is doing nothing in particular.

Two pedestrians pass along the pavement without looking at her. Natural skin texture with visible pores and fine lines. No readable lettering anywhere, and no border around the image.

Thanks.
```

**What to watch:**

1. **Is the kiosk back on the corner?** The round-1 failure. Tells: **scaffolding on the near
   side, the subway entrance immediately behind it, a street rather than a plaza.** If it is
   free-standing on an island again, the framing is still asking for more room than the corner
   has — and the fix is to come **closer and tighter**, not to argue about the location.
2. **Is she holding the receiver?** Round 1 dropped it entirely. It is the whole reason she is
   standing there.
3. **Do the verticals stay straight?** 28mm should hold them. Bending buildings are the
   ultra-wide slop tell and they will fight the statue rhyme rather than serve it.
4. **Is the bag on the floor?** One prop carrying the entire idea — *she is going to be here a
   while.*
5. **Settled, not triumphant.** A lifted chin, a straightened back, a hand on the hip: reject.
   The posture is a woman getting comfortable, not a woman winning.

> ### After this, Act 1 is closed.
>
> The three kiosk re-fires — **§2h.3 → §2h.6 → §2h.7** — are done, §2h.3v and §2h.6v are cut
> off the new stills, and **the whole film is now standing in one phone box.**

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
