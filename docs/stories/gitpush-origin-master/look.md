# GitPush Origin Master — look

> The look for this story only. Read before any still or clip (new-image, scene-images,
> scene-animation, flow-prompt). Rules: [`docs/stories/STYLE.md`](../STYLE.md).

**Status:** LOCKED for every part already made (the music video, the off switch, the second half
A to E: see *Per part*). The look is **not one look**: it travels part by part, on purpose, and each
part's is recorded below. A new GPOM part with no look yet is EXPLORING (a variation round, picked by
Kai or Jack). One question is still open: whether the near-black monumental register works for our
reader ([`docs/cinematography/principles.md`](../../cinematography/principles.md) §R1, 🔴 open).

*(Written 2026-10-28 when BadCode stopped having a house look. The "BadCode register" that the
`new-image` skill used to carry (MACHINE: near-black monolith, one thin light; PEOPLE: 35mm
documentary) came from this story and lives here now, word for word. The prompt ledger
[`prompts.md`](./prompts.md) still holds the per-asset prompts; this file says what the look is.)*

## In one paragraph

GPOM is a transmission from the bad branch, so its home look is **the machine's world: near-black,
one thin motivated light, monumental machine architecture receding into darkness, LEDs the only
colour, calm and certain**, anchored on a dark server hall with a single blade of light. Around it,
the human world is **35mm documentary**: muted cool-neutral, naturalistic light, observational,
class-coded British places. Since the October restructure the film moves through **deliberately
different looks per part**: the music video's operatic set pieces (a robot choir in crimson hoods,
a ring-shaped eye on a mountain at sunset, then the same world at night), Swindon today in
overcast grey for the war, an advert-bright fake Swindon that glitches into the wreck, a 1980s BBC
16mm bunker, a clean bright futuristic clean room, and a photographic wet night on a bus that ends on
the Houses of Parliament in the rain. What holds it together: one named light in every frame, one
bright anchor in any dark frame, a visible cost in any monumental frame, the AI never given a body,
British places (and pounds, never dollars), and animation that is **dramatic**, not a twinkle.

## Preamble(s)

**Register 1, MACHINE: the AI's world and brand images** (verbatim from the `new-image` skill,
2026-10-28):

```prompt
hyper-realistic photograph, near-black exposure with deep unlifted shadows, a single thin motivated light source, monumental machine architecture receding into darkness, muted cool-neutral palette with tiny points of status-LED light, fine film grain, no lens flares, vast still symmetrical composition, calm observational tone
```

**Register 2, PEOPLE: the documentary look** (verbatim from the `new-image` skill; the skill said
this register was *"consistent across camping, magic-money-tree and karen"*, so Camping's
[`look.md`](../camping/look.md) carries its own copy):

```prompt
hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation.
```

For exterior or overcast frames add:

```prompt
late-70s/early-80s scanned film negative, subtle dust specks, gentle gate weave, vintage lens softness with mild halation around practical lights.
```

**The first-half base** (the "drift" base from [`prompts.md`](./prompts.md) §1, ruled by Kai
2026-08-08; every new-image prompt in the ledger has it folded in, and a band line appended per
scene, D0 documentary → D4 deepest → R1–R3 warmth returning; see §1 for the band table):

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, no lens flares, no lens vignette, calm observational tone, landscape orientation, deep unlifted shadows with no shadow recovery, a single motivated light source that is a real thing in the scene, subject held small inside a large frame, no text, no signage, no fantasy effects.
```

**The second-half suffix** (every second-half storyboard still,
[`scenes/second-half-storyboard-plan.md`](./scenes/second-half-storyboard-plan.md)):

```prompt
16:9 frame from a fictional near-future British film. Full-frame image, no captions, logos, lettering or on-screen text.
```

and on the 16mm frames:

```prompt
Styled as a 1980s British television drama shot on 16mm film: faded colour, soft contrast, heavy grain.
```

(The mood-board form of the 16mm line was longer: *"…faded colour, soft contrast, heavy grain,
slightly green shadows, like a BBC Cold War drama."*, [`scenes/second-half-moodboard.md`](./scenes/second-half-moodboard.md).)

## Rules for this story

**Register 1, MACHINE** (verbatim from the `new-image` skill):

1. **Darkness is the canvas.** Most of the frame is near-black, detail dissolving into shadow. What is lit is the argument.
2. **One thin light.** A single motivated source (a blade between racks, a slit under a vault door). The 2001-monolith nod: light as *presence*. Name it; never allow a second photogenic light the scene can't explain.
3. **Machine scale, cathedral framing.** Monumental geometry receding into black. Humans absent, or tiny enough to be a scale reference.
4. **Iconic composition is wanted here.** Symmetry and a centred vertical; the monolith stands in the middle.
5. **Muted cool-neutral; LEDs are the only colour.** Points of blue-white, amber, the rare red. No teal-orange, no colour washes.
6. **Received-from-the-future tone.** Evidence from the bad branch: calm, certain, already happened. If it looks like a movie poster, it's wrong.

**Register 2, PEOPLE** (verbatim from the `new-image` skill):

1. **35mm documentary film look.** Preamble: *hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation.* For exterior or overcast frames add: *late-70s/early-80s scanned film negative, subtle dust specks, gentle gate weave, vintage lens softness with mild halation around practical lights.*
2. **Warm only as argument.** Desaturated greens, slate greys, lifted blacks by default. Warmth (a fluorescent ward strip, a CRT glow, headlights gold through fog) only where the contrast carries meaning: opulence, menace, a reveal.
3. **Observational framing, not heroic.** Characters are found by the camera, not posed for it. Unusual angles (aerial, over-the-shoulder, a POV) encode class position, not just interest. Off-centre is the default here.
4. **The environment is the argument.** Specific UK class signifiers carry weight: a Waitrose car park, NHS-beige walls, a stack of bills on a kitchen table. Vague or fantasy-generic places undercut the story.
5. **Restraint in ordinary frames; scale only in reveals.** The contrast between registers is the argument; an ordinary frame that borrows a reveal's grandeur destroys it.
6. **Exhaustion and particularity.** Grey stubble, tired eyes, a lanyard, a charity-shop coat. Write the specific expression the beat needs; don't let AI defaults smooth it away.

**The gates, as GPOM uses them.** These are written as general craft in
`docs/cinematography/`; on GPOM they are rules:

- **One bright anchor inside the darkness, always.** Uniform near-black reads as a broken file, not
  as mood. In each dark frame name the one brighter region: a screen, a beacon, a seam, a blade of
  light ([`principles.md`](../../cinematography/principles.md) principle 11,
  [`frame.md`](../../cinematography/frame.md) §5). The banks recut put it as *"darkness reads
  as depth only with one brighter region (the screen in each room is that region)"*.
- **A visible cost in any monumental frame.** Scale, symmetry, a machine or an institution needs
  something or someone visibly paying, or it reads as celebration of the power it means to indict
  (principles.md gate 2 and principle 23). The second-half mood board had a whole "VC visible cost"
  concept for the clean room.
- **Name the light source in the world** (gate 3). One motivated source; never a second
  photogenic light the scene can't explain.
- **The visible-cost gate, in the fuller wording shot-craft used to carry** (moved here 2026-10-29):
  *Is there a visible cost in frame?* Mandatory on any monumental shot — scale, symmetry, a machine,
  an institution. Wreckage, exhaustion, a body that failed, someone the system is failing. Without
  one, the grammar of power reads as celebration of it, and meaning it ironically does not protect
  you. (The picture version of `the-reader.md`'s rule about naming the beneficiary.)
- **Never leave the foreground empty** — the most common cause of a flat frame, and it is free
  (from shot-craft, 2026-10-29).
- **Camera movement: default is nothing** in GPOM's still and documentary passages (not the dramatic
  animations below). A single moving shot in a still body of work lands with outsized force, and
  only if the stillness around it is real (*La Jetée*: 26 minutes of photographs, one moving shot).
  Motivated stillness is free; motivated movement is worth spending roughly once per sequence.
  Camera movement only: a locked-off frame full of working machinery does not spend the budget
  (from shot-craft, 2026-10-29).
- **A held still needs a reason to feel photographed** — a low-amplitude camera drift, one light
  changing, grain that lives; a still that truly holds still reads as a scanned photograph (from
  shot-craft, 2026-10-29).
- **R1 is open.** Nobody has evidence the near-black monumental register is right for a
  working-class UK reader, nor that social realism is the fix. Don't claim it settled in any canon
  file or public copy (principles.md §R1).

**Hard guardrails** ([`prompts.md`](./prompts.md) §0, locked 2026-07-22 by Kai and Jack, with what
changed since):

- **The AI is never personified.** No robot standing in for it, no face, no avatar, no glowing orb,
  no humanoid silhouette. The camera is its point of view. Since the second half it speaks through
  Maddie's speaker (her beacon pulses on his words); it still has no body, ever.
- **No legible text in a generated frame.** Text that appears or types is a post job (ffmpeg; the
  only lane that writes a string). Exception, retested 2026-08-21: Flow renders
  `git push origin master` on an old green CRT correctly, so Flow makes the plate and post animates
  the type. The kill-bot HUD is an ffmpeg text layer.
- **No real brand names, products or institutions**, no legible chyrons or logos.
- **Anchored in the UK**: pounds, never dollars (Kai, 17 Oct, the £50 banknote hall).
- **Flashes at 3 a second or fewer**; the simulation glitch runs a flash-safety pass
  (`ffmpeg photosensitivity`) before anything ships.
- **The collapse stays off-screen** was the original rule (no explosions, burning cities, bodies or
  combat). Later rulings narrowed it: Kai's downfall prompt pack (2026-09-22,
  [`scenes/downfall-flow-prompts.md`](./scenes/downfall-flow-prompts.md)) superseded it for those
  shots, and the war scene shows **wreckage, never a hit**, with **no humans at all**.

**Animating a GPOM plate.** Kai, 2026-09-13: *"when we do videos here we should make them
dramatic"*: a dive through cloud, a storm with a lightning flash, a hard push into the glass, not a
vague twinkle-and-haze on a locked camera. Offer dramatic options per shot up front. Method (from
the hybrid method, `docs/video-fx/hybrid-method.md`): lock Veo's camera and make the **world**
dramatic where the frame has a repeating grid (glass walls, racks), and let Veo move the camera
where there is none (aerials, cloud); Premiere moves the camera over locked clips. **Moving grain is
not optional on a locked plate**, or it reads as a frozen JPEG. **Few movers:** give the motion to
rain, haze, light and one actor. The motion is an argument: the machine that doesn't care, the
wealth piling while the room dims (from scene-animation, 2026-10-29).

**Calibration: the generic AI look to avoid** (verbatim from the `new-image` skill, "where the
subject leaves an axis free, do not spend it on these"):

1. **Teal-orange blockbuster grading, hard rim light, deep blue shadows, glowing eyes.** Name the real light source instead.
2. **Lens flares, glow bloom, decorative light rays, heavy vignettes, chromatic aberration.** Film grain and gate weave are allowed (analogue artefacts); flares are banned.
3. **Smooth porcelain skin and idealised faces.** Name the imperfections that make a person real.
4. **Busy greebled detail everywhere.** Most of a machine frame must actually be dark; say what dissolves into shadow.
5. **HUD overlays, holograms, floating UI.** The future here is racks, concrete and light. (A HUD that is a *diegetic* point of view, like GPOM's kill-bot POV, is a shot design, not decoration.)
6. **Over-lit "epic" scenes** and **the centred lone posed figure.** Symmetry belongs to architecture, not to a hero.

**Accepted plates are locked.** Hone from the pick with `flow_edit_image` off the golden original,
never re-derived from scratch; Kai approves every plate before video credits are spent.

## Anchors

| What | Where | Note |
| --- | --- | --- |
| **The register anchor** | [`docs/images/register-anchor.jpg`](../../images/register-anchor.jpg) (prompt: [`register-anchor.md`](../../images/register-anchor.md), Flow `a3a2bf57`) | Dark server hall, one thin vertical line of cool light, LED points. Was panel 1 of the GPOM Short comic (2026-07-02). Look at it before the first MACHINE generation of a session |
| **Anchor variant** | [`docs/images/server-hall-monolith.jpg`](../../images/server-hall-monolith.jpg) ([`server-hall-monolith.md`](../../images/server-hall-monolith.md), Flow `eb27d6ea`) | The hall slightly more readable; v1 was over-lit, one `flow_refine` to under-expose it, and the blade resolved into a door slit. A good worked example of "darker, one light" |
| **The cover** | prompt in [`prompts.md`](./prompts.md) §3b "cover" | An orbital server hall, racks down an aisle open to space, Earth a whole disc as the only light (Kai's vision, 2026-08-08). The file `docs/images/covers/gitpush-origin-master.jpg` the ledger names is **not in the repo**, and its Flow media id was never harvested |
| **Per-part stills** | `D:\badcode-videos\gitpush-origin-master\clips\<part>\` (mood boards, storyboards, picks) | Each part's picks are listed in its scene folder (`scenes/*/picks.md`, `scene.json`) |

## Cast

One canonical reference per recurring character, always the same one, attached as a reference or a
Flow Character. Never regenerate a face-bearing frame of a recurring character without casting it.
Media paths are under `D:\badcode-videos\gitpush-origin-master\clips\`.

| Who | Reference | Rule |
| --- | --- | --- |
| **The AI** | none, ever | Never rendered. Speaks through Maddie's speaker; the beacon pulses on his words |
| **Maddie**, the West Country delivery bot | `simulation/stills/s3/s3-bot-00b-a.jpg` (Kai's edit); Flow Character **`West Country Bot`** (project `be451638`, "Oct 17 - 18:57") | Dented boxy grey body, six chunky black wheels, amber beacon on a short stalk. **The torn, faded bunting on her wheel stays in every shot** (Kai, 17 Oct: *"a little detail that really resonates with me"*). **Exception from scene D's clean room onward:** gleaming clean like the humans in their clean suits, **no bunting at all**, not washed, not new (Kai, 23 Oct) |
| **The kill bots** | `second-half/moodboard/P1-patrol-blockbuster.jpg` (the tracked robot with the sensor turret); Flow Character **`Kill Bot`** | The other options read as tanks and stay unused |
| **Sandra** | `second-half/storyboard/SB07b.jpg` | — |
| **Derek** | `second-half/storyboard/SB07c.jpg` | — |
| **The old lady** | `second-half/storyboard/cut3/S7r-a.jpg` | Her close-up is the one anamorphic-blockbuster frame in the 16mm half (kept on purpose) |
| **The hundred** | none by design | Individuals sharing a room; consistency is wardrobe, blocking and light (`prompts.md` §2) |

Flow Characters also made 2026-10-17 in project `0558b1d5`: `Cream Jumper Woman` (portrait + body)
and `Green Jumper Man` (portrait only). Which human each one is was not recorded; check before using.

**Contracted objects** (vary camera, light and palette, never the spec):

- **The building** (the time machine's home): `second-half/moodboard/BL1-day.jpg`, the BL series.
  *"ONE fixed design: a long, low building of black glass, many times longer than it is tall, with
  one single thin horizontal seam of warm amber light running its whole length, set down in a fold
  between two green chalk downs, the only made thing in sight; no windows, no signs, no other
  lights"* (`scenes/second-half-*/scene.json`, cast `building`). `L11-exterior-night` is not this
  design and is not used.
- **The chairs**: locked to `second-half/moodboard/L3-wafer-pattern.jpg` (dark recliners in pools of
  light, square grid in a thin ring, cables to a round hub).
- **The ring eye** (the colossus): CO6, refined to EY1-b / EY4-c: the same eye and the same mountain
  in every shot; red rim dots light in sequence round the ring (the lights don't move); white
  aperture ([`scenes/opening-recut-picks.md`](./scenes/opening-recut-picks.md)).

## Places

- **The server hall / data centre**: the register anchor. Racks receding, one blade of light.
- **Hong Kong, the internet café and the CRT**: Earth from orbit → a wide Hong Kong → the café → the
  green CRT where `git push origin master` is typed (`prompts.md` §3a–3b; ownership text typed on the
  CRT in post).
- **The opening's rooms**: a rain-soaked plaza with server cabinets, one desk one box, a corner
  office in a tower, a trading floor, a banknote hall in £50s. In the banks part the same rooms are
  shown **empty**, each still an edit of its original.
- **The parade ground and the mountain**: rank on rank of robots in crimson hooded cloaks with red
  eyes, ships with searchlights, the ring eye on the summit.
- **Swindon**: today (motorways, roundabouts, high streets, fields) in the war; five years later as
  the bright fake high street and the same street wrecked (vape and betting shops gutted).
- **The bunker**: Cold War, Corsham-like, under a Wiltshire hill; whitewashed stone, green steel
  blast doors, cream enamel lamps, lived in for five years; the tiled lavatory.
- **The downs and the building**: overcast chalk downs, the black-glass slab with the amber seam.
- **The clean room**: chip-fab, lab, the wafer the size of a house, the chairs in the wafer's
  pattern. The AI built it; it is **not** in the bunker (the bunker → clean room contrast is the
  point).
- **The bus and the high street at night**: chip shop, betting shop, a closed bank, wet tarmac.
- **The Houses of Parliament** at night in the rain: the film's last shot.

## Never

- A body, face, orb, avatar or humanoid stand-in for the AI.
- Teal-orange grading, lens flares, glow bloom, decorative rays, heavy vignettes, HUDs or holograms
  as decoration (the kill-bot POV HUD is a shot design, not decoration).
- A second photogenic light the scene can't explain; uniform black with no bright anchor.
- A monumental frame with no visible cost.
- Dollars, real brands, legible institutional text generated in-frame.
- **Stop-motion** (Kai dislikes it, 16 Oct).
- Maddie redesigned between frames, or Maddie without her bunting before scene D (or with it after).
- A beam of light as spectacle on the building (CR6 rejected).
- Vague small animation: twinkling lights and drifting haze on a locked camera.

## Per part

In film order (the overview board, [`timelines.json`](./timelines.json)). Each part's own look
section is the authority; this is the summary.

| Part | Look | Status |
| --- | --- | --- |
| **Music video: opening, the push, the drop** (0:00) | Earth from orbit → Hong Kong → the café CRT; the opening's rooms in documentary 35mm (rain plaza, corner office, trader, £50 banknote hall); at the drop the operatic set piece: a robot choir at clone-army scale, red eyes, crimson hooded cloaks, then the ring eye on a mountain at **sunset**, the red dot travelling the ring on the beat. Kai: lean into Jeff Wayne's *War of the Worlds*, story and operatic. ([`scenes/opening-recut-picks.md`](./scenes/opening-recut-picks.md)) | LOCKED, in Premiere (Kai cuts it) |
| **The banks fall** (1:14) | The opening's rooms shown **empty** with money transferring, each still an edit of its original so the room matches exactly; a first-person camera-hood teleprompter matching the old presser's blue curtain, no humans in the press pack; one brighter region per room (the screen) ([`scenes/banks-recut/brief.md`](./scenes/banks-recut/brief.md)) | LOCKED, in Premiere |
| **Chorus 2** (1:47) | **Night** (chorus 1 was sunset, the sun has gone): night-blue arena, red robes, white searchlights, the eye's white aperture with red rim dots; closer and harder, then it moves; ends with the eye's beam crossing an empty town and whiting out the lens ([`scenes/chorus-2/brief.md`](./scenes/chorus-2/brief.md)) | Clips made; Kai's picks owed (timelines.json) |
| **War in Swindon** (2:09) | **Swindon today**, overcast grey English daylight, muted natural colour; **no humans anywhere, never a hit on screen** (drone swarms, empty motorways and roundabouts, the wreckage after); a drone-feed beat breaks it on purpose (grainy, grey or thermal) ([`scenes/war/brief.md`](./scenes/war/brief.md)) | LOCKED, cut by Kai |
| **Five years later: the off switch** (the simulation) | S1: the fake Swindon high street, **deliberately off-house: high-key, saturated, advert-bright** (the Parr counter-tradition), high summer sun from camera-left, the only frame like it in the film. Under 1 s **glitch** (the wreck showing through in bands, `rgbashift` + band blend + noise). S2: the same street, matched frame, wrecked, flat grey overcast, no sun. S3 on: the bot at her own height, the amber beacon the one warm point ([`scenes/simulation.md`](./scenes/simulation.md)) | LOCKED, in Premiere |
| **A · Kill bots** | Patrol = **grainy CCTV with a red HUD**; red vision = kill mode only; at the signal a big audio waveform band across the frame; the HUD is an ffmpeg text layer; the dead market town and the bunker gate ([`scenes/second-half-storyboard-plan.md`](./scenes/second-half-storyboard-plan.md)) | Picture made; round 4 notes in progress |
| **B · Maddie at the door** | **1980s BBC 16mm**: the bunker naturalistic and lived in, faded colour, soft contrast, heavy grain; the old lady's close-up is the one anamorphic-blockbuster exception | Picture made; round 2 notes in progress |
| **C · The walk out** | Overcast daylight on the downs, muted greens and greys, fine grain; carries B's exterior (S6-c), not full 16mm, so the cut is seamless; **the amber seam is the only warm colour** ([`scenes/second-half-c-walk-out/brief.md`](./scenes/second-half-c-walk-out/brief.md)) | LOCKED, signed off |
| **D · The clean room and the crossing** | **Clean, bright, futuristic**: cool white, crisp, a faint grain, the far end of the 16mm → futuristic travel; light from the hall's ceiling grid, the wafer's rainbow on faces, a pool of light under each chair; D14 the one exterior at dusk, the amber seam its only warm light; **Maddie gleaming, no bunting** ([`scenes/second-half-d-crossing/brief.md`](./scenes/second-half-d-crossing/brief.md)) | LOCKED, signed off |
| **E · The ending** | **Night, rain and photographic**, a deliberate break from both the clean room and the 16mm: the real world, ordinary, wet tarmac, sodium and shop light, the bus's lit top deck; the phone screens painted in-camera by Flow (no overlay); the last shot is the **Houses of Parliament at night in the rain** (pick E04p-a), camera locked, a slow push 100 → 106% ([`scenes/second-half-e-ending/brief.md`](./scenes/second-half-e-ending/brief.md), `cut-notes.json`) | LOCKED, signed off |

The second half's travel, in one line (Kai, 17 Oct): **the style travels from 1980s BBC 16mm to
futuristic.**

## History

- **The PEOPLE preamble is shared with Camping** (noted 2026-10-29, style-leak audit): Register 2 above is,
  word for word bar the orientation tail, Camping's *Objects and close details* preamble
  ([`../camping/look.md`](../camping/look.md)) — both copied from the `new-image` skill when it called this
  register *"consistent across camping, magic-money-tree and karen"*. There is no house look: each story
  keeps its own copy, and a change to one does not change the other.

- **2026-07-02:** the register anchor made as panel 1 of the GPOM Short comic; it became the
  "BadCode register" for every brand image. 2026-07-13: `new-image` skill, `server-hall-monolith`
  made.
- **2026-07-22:** the AI is never personified (Kai and Jack).
- **2026-08-08:** the drift ruling: documentary-warm → near-black machine → warmth returning with the
  hundred in the vault (`prompts.md` §1). The vault half was later cut (below), so the R bands no
  longer have scenes.
- **2026-08-21:** the "no text in frame" ruling overturned for the CRT; the green ✓ CI motif retired
  in favour of a colour turning red.
- **2026-09-12:** variety mode, because every image was coming back muted and dystopian: the
  register had been written as a format.
- **2026-09-13:** animate dramatically (Kai).
- **2026-09-19 to 10-26:** the gaze sequence (data centre → Swindon disaster epic) made, then
  retired from the film 2026-10-26.
- **2026-09-29:** the ghosts scene dropped for the simulation (bright fake Swindon → glitch → wreck,
  the bot).
- **2026-10-15:** the restructure. The D&B music video is the downfall; the coin, the vault, the
  experiments and the Carrier's back half go to the Storyverse. The Carrier's sheet
  (`characters/img/carrier-sheet.jpg`, Flow Character "Carrier") and the coin / empty chair /
  ventilation shaft totems (`prompts.md` §2b) are from that cut material.
- **2026-10-16 to 17:** the second-half mood board (https://claude.ai/artifact/UkcXHKhuY8f2rzV7FtQ6e5)
  tried seven styles per scene (1980s BBC 16mm, noir, painted matte, stop-motion miniature,
  anamorphic blockbuster, handheld documentary, advert-bright); Kai picked the 16mm → futuristic
  travel, the red HUD and the one fixed building, and ruled stop-motion out.
- **2026-10-17:** the opening recut: the weak bulletin shots replaced, robot choir and colossus at
  the drop, £50 not dollars.
- **2026-10-19 to 20:** banks recut (empty rooms), chorus 2 (night), the war (Swindon today, no
  humans).
- **2026-10-23:** Maddie gleaming with no bunting from scene D on; ending E now ends on the Houses
  of Parliament.
