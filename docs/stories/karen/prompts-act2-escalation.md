---
story: karen
kind: brief — written in-repo, fired by hand; each block is the deliverable
engine: Nano Banana Pro (plates) → Gemini Omni Flash (clips)
flow_project: TODO — exact project name as it appears in Flow
updated: 2026-08-17
---

# Karen — Act 2, the Great Escalation

Plate prompts for **the core of the film**: Karen climbs the management ladder from a
Midtown phone box over nine months.
[`story.md`](./story.md#act-2--the-great-escalation-the-core-of-the-film) §Act 2, and its
storyboard is the song — [`songs/all-day-to-complain.md`](./songs/all-day-to-complain.md).

> ## 🖐 A brief, not a record
>
> Same standing as [`prompts-morning-after.md`](./prompts-morning-after.md):
> [`prompts.md`](./prompts.md) is the **ledger**; this is not one. It inherits the
> conventions — the §1 `STYLE LOCK` pasted verbatim at the top of every plate, the casting
> rule (`**Cast:** @Karen` — never describe a face), no legible text, the closing
> *"Thanks."* Section numbers continue at **§2j** (2a–2i are taken).
>
> **Ruled 2026-08-16 (Kai): fired by hand, not by the automation.** Each block below is the
> complete thing to paste, with cast, time of day and attachments stated above it.
>
> **Order of work, ruled 2026-08-17 (Kai): all the plates first, then the clips.** Every
> §2j block is a still until that changes.
>
> **Engine research does not live here** — it goes to
> [`docs/google-flow/`](../../google-flow/README.md).

---

## What makes this section hard

Not the shots. **The repetition.** The formula runs 3–4 times and the whole bet is that the
audience *clocks the pattern* — aerial, zoom down, functionary, Karen, zoom out, weather
changed, next building. Rung for rung with the song.

That inverts the usual instruction. Normally variety is the goal and drift is the enemy;
**here sameness is the point.** The aerial has to be recognisably the same shot every time,
so the later rungs are **re-fires of the accepted §2j.1 block with exactly one line
swapped** — the Light line. Keeping ~80% of the descriptive wording identical between
shots that share a setting is the documented defence against environmental drift, and here
it is also the joke.

**The three structural constraints from `story.md`, restated as production rules:**

| Canon rule | What it means for a prompt |
| --- | --- |
| *"The phone box is a fixed point"* | Every Karen intercut re-uses the accepted §2h kiosk still as a reference. The box never moves; the world changes around it. |
| *"No crowd yet — she is completely alone in this act"* | No onlookers in any Karen plate. The pavement behind her is ordinary and indifferent. |
| *"The narrator does the talking"* | The functionary plates are **portraits, not dialogue**. Who they are at which rung is the whole content. |

---

## The prompts — §2j

**Paste the §1 `STYLE LOCK` verbatim above each block**, then the block, then *"Thanks."*

### 2j.1 Aerial over Midtown, rung 1 — plate · **the master** · **reference-anchored**

**Cast:** none. **Time:** flat overcast mid-morning — the same day and the same weather Act
1 ends in, so it cuts straight out of §2h.7. **Attached:** a cropped **Google Earth**
screenshot, one image (recipe below). **Engine:** Nano Banana Pro, 16:9, 3 candidates.

**Fire this one first and accept it properly.** Three later aerials are re-runs of it.

> ### The failure mode has a name here: the drone shot
>
> Golden hour, the Empire State centred, a glassy skyline receding into a flare. Three
> counters are built into the block, and they are worth stating because they generalise to
> every aerial we will ever write:
>
> 1. **No sky and no skyline.** The frame is filled with city. A skyline is what a postcard
>    *is*; rooftops are what a city actually looks like from above — water towers, tarred
>    seams, HVAC plant, roof huts. **The mess on top is the anti-slop.**
> 2. **Helicopter on a long lens, not a drone.** Drone-stock is the aesthetic the model
>    defaults to, and it is also fiction — you cannot fly a drone over Midtown. Naming the
>    helicopter and the long lens buys **compressed perspective and haze between camera and
>    far blocks**, which is the atmospheric depth cue AI aerials characteristically lack
>    `[community]`.
> 3. **Scale references and a real instant.** Aerial-photography guidance is unanimous that
>    cars and people are what make an aerial read as a place rather than a model. Hence
>    **traffic held at one red light while the cross street moves** — true of a real city at
>    a real moment, and never true of a rendering.

**One production note:** the tower sits **off-centre with air around it**, because the video
pass has to push down into it. A centred building leaves the move nowhere to go.

#### The Google Earth recipe — Kai's call, 2026-08-17

**Anchor the aerial on real geography instead of an invented one.** This is the strongest
anti-slop move available for a city shot: the model stops *composing* a city and starts
rebuilding one, and the framing decision moves out of the prompt and into a viewport where
you can actually see it.

**Where.** Third Avenue between E 46th and E 50th, Midtown East — canon-correct (the song
puts the box at Lexington & Third) and four blocks of plain 1970s–80s office slabs, water
towers and tarred roofs.

> **⚠️ Do not drift south or west.** The Chrysler Building, Grand Central, One Vanderbilt,
> the Waldorf's twin towers, Citigroup Center's angled crown and the Seagram Building are
> all within a few blocks. **One of them in frame and the shot is a postcard again.**

**The camera, set numerically** — paste into the address bar rather than flying it by hand:

```
https://earth.google.com/web/@40.75390,-73.97150,20a,900d,35y,340h,40t,0r
```

| Token | Means | Nudge if… |
| --- | --- | --- |
| `900d` | camera distance, metres | roofs unreadable → `600d`; more haze depth → `1400d` |
| `40t` | tilt; `0t` straight down, `90t` horizon | **sky at the top of frame → lower it.** 45 is the ceiling |
| `340h` | heading | spin until the avenue cuts corner to corner; ~320h–20h all work |
| `35y` | field of view | leave it — 35° approximates the long lens the block asks for |

Coordinates are approximate. Check the street labels on screen and slide a block until you
find a tower you like.

**Compose the screenshot; do not just take one.** The prompt now says *keep this viewpoint*,
so the framing rules move into Earth: target tower **off-centre with air around it**, avenue
diagonal, **no sky and no horizon**, a nearer rooftop clipping a bottom corner, browser
window roughly 16:9.

**Then crop off every bit of Google UI, especially the bottom attribution strip.** Legible
text in a reference comes through into the generation, and
[Flow scans the uploaded image as well as the prompt](../../flow/failure-modes.md#a2-every-field-flow-reads-is-scanned-not-just-the-prompt-box).
Downscale to ~1600px on the long edge; one image, not several.

**What the reference must not bring.** Earth gives real geometry, real massing, real
framing. It also brings three things the `REFERENCE` block refuses by name:

1. **Its light.** The 3D tiles have shadows **baked in** from capture, often hard midday
   sun. We want flat overcast. This is the most likely way the plate comes back wrong.
2. **Its texture.** Satellite-derived mesh is smeared and plasticky — the exact look we are
   already fighting.
3. **Its melted buildings.** Earth's 3D droops at every edge. The block tells the model to
   treat that as source artefact and rebuild the architecture properly, which is the one
   instruction here that has no precedent in our other reference-anchored plates.

**Grab a second screenshot while you are in there** — the same tower lower and closer. That
is the zoom target for the clip and the exterior the rung-1 interior has to sit inside.

##### ⚠️ Round 1 of the screenshot, 2026-08-17 — too high, and the river got in

Kai's first pass came back from several thousand metres out, looking east over Midtown East
with **the East River, Roosevelt Island, the Queensboro Bridge and the UN grounds** all in
frame. Tilt and no-sky were right; distance and heading were not.

**The diagnostic is one question: can you pick out individual water towers?** If not, the
reference is giving the model anonymous grey blocks — which is what it would have invented
unaided, so the screenshot is buying nothing. **Rooftop clutter is the whole reason we are
shooting the roofs instead of the skyline.**

The correction was **closer and steeper**: `650d` and `30t`, heading `300h` to put the river
behind the camera. Steeper does the landmark exclusion by itself — at 30° the far edge of
frame is a few blocks away, so there is no distance for a famous crown to appear in.

**The pre-shoot checklist, in order:** individual water towers legible · no water, bridge or
park in frame · no distinctive crowns on the far edge (Citigroup Center is the one to watch
north of 53rd) · one plain slab off-centre with room around it · roughly 16:9, Earth UI
cropped off.

*(The too-wide frame is worth keeping. That altitude is roughly where the end of each
rung's zoom-out lands, and the weather changes read best that far back — it is just not the
master.)*

##### ✅ Ruled 2026-08-17 (Kai): **keep the wide frame.** It is the master.

The concern above was raised and overruled, and the ruling is a good one for a reason the
checklist missed: **the river edge makes the frame unmistakably Manhattan without the
skyline postcard**, and it gives the weather changes somewhere big to happen. The
close-and-steeper recipe stays on file for the rung-2/3/4 aerials if we ever want variety —
but §2j.1 is the wide view, and the block was rebuilt around it rather than swapped onto it.

**What the altitude changes, and it changes three things:**

1. **The detail budget moves to the grain of the grid.** No rooftop clutter is legible at
   this height, so the realism has to come from **density** — roofs in a hundred shades of
   grey and brown, traffic in short broken lines, steam standing over two or three
   buildings. Density is the texture now.
2. **The landmarks stay in, demoted rather than banned.** The bridge, the island and the UN
   grounds are *in the reference*. **Never write a constraint that fights the attached
   image** — that conflict is a reliable route to a mushy compromise. The block gives them a
   role instead: *ordinary working infrastructure at the edge of frame, not a view.*
3. **Water is now the main slop risk.** AI water defaults to glittery, teal and sparkling,
   and that one failure turns the plate into tourism. The Light line pins it **flat matte
   grey, no sparkle, no reflected colour.**

**⚠️ The likeliest reject is the sun.** The screenshot carries hard baked-in shadows down
the west face of every tower — the strongest signal in the image, and it argues with the
flat-overcast instruction. Sharpen the refusal; do not rewrite the scene.

**And the likeliest quality failure is density mush** — forty blocks is a lot to rebuild at
once, and it goes to copy-paste blocks and soup where the haze starts. Check at 100%. The
honest fix is a **tighter crop of the same screenshot**: same geography, same ruling, fewer
blocks to build.

**Mechanical note:** the screenshot is ~2.6:1. Crop to **16:9** with the Earth UI off both
bottom corners, centred so the dark tower sits off-centre with room around it — that is the
building the clip pushes down into.

*(The screenshot is an internal composition reference. The deliverable is a rebuild, not the
photograph.)*

```prompt
REFERENCE:

Use the attached image as the layout reference — the street grid, the block sizes, the footprints and relative heights of the buildings, the line of the river and the bridge, and above all the viewpoint and the framing. Keep that geography and that framing exactly. Take nothing else from it: not its colour, not its lighting, not its shadows, not its weather, not its time of day, and not its surface texture.

The attached image is a satellite-derived three-dimensional view, so its buildings are soft and melted at the edges, its rooftops are flattened and its streets are smeared. Treat all of that as an artefact of the source: rebuild the same buildings as real architecture with clean edges, straight parapets and sharp rooflines, rebuild the roofs with real rooftop machinery, water towers and vents on them, and rebuild the streets as real streets with real vehicles in them.

Rebuild that view of the city as a photograph made from a helicopter, in the light described below. The finished frame carries the film look described in the style lock above, not the look of the attached image.

SCENE:

Subject: Midtown Manhattan seen from high above on an ordinary weekday morning, with one plain dark office tower standing alone above the lower blocks near the middle of the frame.

Composition: 16:9, the viewpoint and framing of the attached image kept as they are — a steep high angle looking down and across the grid, the city filling the whole frame with no sky and no horizon in it, the river running along one edge, the far blocks receding into haze; the frame is very slightly tilted.

Action: an ordinary weekday instant — traffic strung along the avenues in short broken lines and held at the lights on the cross streets, one boat drawing a slow wake on the river, steam standing in thin plumes above two or three roofs.

Location: forty blocks of ordinary Manhattan — flat tarred roofs in a hundred shades of grey and brown, timber-framed water towers, rooftop plant and bulkheads and vents, fire escapes down the older blocks, two construction sites under orange netting with tower cranes over them, and at the edge of the frame a bridge and a river island reading as ordinary working infrastructure rather than as a view.

Light: flat overcast mid-morning daylight from a white sky, no direct sun and no long shadows; the river flat matte grey with no sparkle and no reflected colour; the street canyons several stops darker than the roofs.

Style: a still from a 35mm independent film, shot from a helicopter on a long lens — compressed perspective, haze thickening with distance, available light only, unretouched, documentary rather than promotional.

Constraints: ordinary commercial and residential architecture throughout, unglamorised; keep every rooftop sign, hoarding, advertisement and vehicle livery free of readable lettering.
```

> **The block above is round 2 — the wide, reference-anchored version.** Round 1's
> unanchored block (a tight rooftop frame, no reference, no river) is superseded and has
> been removed rather than kept, because two blocks under one heading is how the wrong one
> gets fired. The close-and-steeper **Earth camera recipe** above is what survives of it,
> and it is still the right recipe if a later rung wants a tighter aerial.

> ### Fired 2026-08-17 — round 2 came back strong. Three rulings owed.
>
> **Density did not mush**, which was the real risk: forty blocks rebuilt, the grid holds,
> the far distance stays coherent, traffic reads correctly on the riverside expressway, and
> it delivered the boat and its wake. **The water came back flat and matte** — that risk
> did not materialise either. **The sun did not land as hard shadow**, against expectation.
>
> **1. The `STYLE LOCK` did not land — and canon says that is correct.** No grain, no
> halation, no vignette, no super-8: a clean photographic aerial. A photographic reference
> pulls hard toward photographic realism and the lock lost. But
> [`story.md`](./story.md#act-2--the-great-escalation-the-core-of-the-film) asks for
> *"Aerial Manhattan — **photoreal**, looking down over the city."*
>
> **So promote the accident to a device: the god's-eye shots are photoreal; Karen's world
> is super-8.** The camera is objective above the city and degraded down in it with her.
> Free, and it means something. **But it has to be deliberate and consistent across all
> four aerials**, or it reads as two shots that do not match. *(If Kai wants the grain
> instead, that is a post pass over the whole act, not a re-fire.)*
>
> **2. ⚠️ The zoom target is a hero building.** The obvious target — the dark slab, dead
> centre, alone, air around it — is a distinctive luxury tower, and **the joke of the ladder
> is that none of these places are special.** Two options, and this decides the rung-1
> interior as well: use it and read it as a corporate HQ (easiest; the composition is
> already built round it), or nominate one of the dull mid-height blocks left of centre, so
> the zoom becomes *"and in this completely unremarkable building…"* — funnier, more
> on-message, less for the push to lock onto. **Ruling owed before the interior is written.**
>
> **3. The foliage will fight the snow variant.** Full summer leaf, green lawns. Fine for
> rung 1; when the Light line changes to snow, **the reference will keep pushing summer**,
> so bare trees have to be stated in the Location line rather than implied by the weather.
> Recorded now so it is not diagnosed as a random failure later.

**What to watch, in the order these are likely to fail:**

1. **The sun.** The reference carries hard baked-in shadows down the west face of every
   tower. **Most likely reject.** Sharpen the refusal; do not rewrite the scene — the same
   lesson as §2h.3.
2. **The water.** Sparkle, teal, or a mirror finish means postcard. Flat matte grey or
   re-roll.
3. **Density mush.** Forty blocks is a lot to rebuild at once; it fails as copy-paste blocks
   and soup where the haze starts. Check at 100%. The fix is a **tighter crop of the same
   screenshot**, not more words.
4. **Is the target tower still legible?** It has to survive as one identifiable object — the
   clip pushes down into it and the rung-1 interior lives inside it.
5. **Did it copy the mesh instead of rebuilding it?** Soft, drooping, subtly wrong buildings
   mean it treated the screenshot as the shot. That is the relationship instruction failing,
   and the fix is strengthening it rather than adding detail elsewhere.
6. **The traffic.** Vehicles are where aerial renders fall apart — floating, mis-scaled,
   facing the wrong way down a one-way avenue.

**On acceptance**, the three weather variants are this block with **only the Light line
changed** (rain → snow → low winter sun), plus whatever the wet or snow-covered roofs
demand in the Location line. Written when the master lands.

### 2j.1v The descent, rung 1 — clip · **the master**

**Cast:** none. **Attach:** the accepted §2j.1 aerial. **Engine:** Gemini Omni Flash ·
**Ingredients to Video** · 8s · native audio · **Enhance Prompt off.** Same recipe as the
accepted Act 1 clips — Frame-shaped prompt text fired in the Ingredients tab.

> ### The design decision: **it never arrives.**
>
> Eight seconds cannot carry a camera from this altitude down to one building, and forcing
> it buys the two things Omni is worst at — **an accelerating move**, and **façades it has
> to invent** because the plate never showed them
> ([the unrendered-region rule](../../google-flow/omni-flash.md#the-unrendered-region-rule--why-it-invented-a-shore)).
>
> **So the descent is still going when the clip ends and the cut does the arriving.** It is
> [*render the reach, not the contact*](../../google-flow/omni-flash.md#the-rule-that-outranks-all-of-it-a-real-camera-never-catches-the-whole-fall)
> applied to a camera move instead of an object, it is how a documentary would cut it, and
> it happens to serve the story — the film keeps not getting there.

**⚠️ No film grain in this block**, unlike every Act 1 clip. The
[photoreal-aerials ruling](#fired-2026-08-17--round-2-came-back-strong-three-rulings-owed)
means the clip has to match the plate it starts from. **The 24fps/180-degree shutter clause
stays** — that is motion realism, not texture, and the two are separable.

**The ambient motion is ranked by risk**, deliberately: the boat and its wake are the safest
thing moving (slow, single, unambiguous direction), the steam is formless, and the traffic
is the one most likely to misbehave at this scale.

```prompt
Using the attached image as the locked opening frame, animate what happens next in one continuous shot. Keep the city, the light, the weather and the framing exactly as they are in the frame.

The camera descends. It starts exactly where the frame starts, high over the city, and moves slowly and steadily down and forward toward the dark tower standing alone near the middle of the frame, which grows larger in frame as the camera closes on it. The shot stays high throughout and the descent is still going when the clip ends. The move carries the small float and drift of a long lens shot from a helicopter. It is the only camera move in the shot.

Below, the city goes on with its morning: traffic creeps along the avenues and along the riverside expressway, one boat draws a slow white wake up the river, and thin plumes of steam stand and drift above two or three rooftops.

Available light only, real-time pace, flat overcast daylight from a white sky. Haze hangs between the camera and the far blocks. Shot at 24fps with a 180-degree shutter.

Audio is the city from a long way up: a low wash of distant traffic and steady wind.
```

**What to watch:**

1. **Whether it arrives anyway.** The tower filling frame at the end means it accelerated,
   and the façades will break up. Add *"the tower is still small in the frame when the clip
   ends"* — **stated as a fact about the last frame, not as a limit on the move**, because
   [negatives backfire on Omni](../../google-flow/omni-flash.md#-negatives-do-not-work-and-they-actively-backfire).
2. **Whether it cuts.** The likeliest structural failure — a descent is exactly the shape
   Omni wants to chop into three angles. *"In one continuous shot"* is in the opening line
   for that reason; if it still cuts, reroll rather than rewrite.
3. **The traffic and the boat.** Vehicles this small are cheap to get wrong. **If the
   traffic misbehaves, drop the traffic clause** and let the boat and the steam carry it.
4. **Whether the city holds still underneath.** Buildings should keep their positions and
   grow with perspective. Blocks sliding relative to each other is warping, not moving.

**Accept it as a master, like the plate.** The other three rungs are this clip with the
weather changed and a different tower named.

### 2j.5 Rung 1 interior, the front desk — plate · **the template**

**Cast:** none. **Time:** mid-morning, same day. **Attached:** nothing. **Engine:** Nano
Banana Pro, 16:9, 3 candidates. **Register: super-8 `STYLE LOCK`** — inside Karen's world,
so it is grainy. The aerials are the photoreal ones.

> ### ✅ Ruled by acceptance, 2026-08-17: rung 1 is inside the dark slab.
>
> The [hero-building question](#fired-2026-08-17--round-2-came-back-strong-three-rulings-owed)
> answered itself when §2j.1v was accepted — the clip descends into that tower, so the
> interior is in that tower. Read it as a corporate HQ. **The dull-building joke moves to
> rung 2**, where it costs nothing.

**This plate is a template.** Rungs 2, 3 and 4 are this shot with the room and the person
changed, so the grammar is worth getting right once:

1. **The camera always stands where Karen cannot.** Every rung is shot from the **visitor's
   side of the desk, at standing eye level**, from the position of someone who has come to
   ask for something. Karen is never in the room — she is in a phone box across town — but
   **the camera is always in the room, at the counter, being ignored.** The section's joke,
   rendered as a camera position.
2. **What escalates is the furniture, not the shot.** Laminate at rung 1; carpet and a
   nameplate at rung 2; wood panelling and a window with a view by rung 4. Same lens, same
   distance, same eye level, so the ladder reads without being announced.
3. **The performance is one thing: they are not looking at the call.** Eyes on the monitor,
   hand on the mouse, mid-sentence in something they say forty times a day. **No rudeness** —
   rudeness makes it a scene about a bad person, and it is not. It is about a system where
   nobody is unkind and nothing can happen.
4. **No emotion words.** Per [§4a](../../flow/image-prompting.md#4a-expressions--name-the-muscles-never-the-emotion)
   the smile is described as muscles — *mouth corners lifted, nothing moving around the
   eyes.* That sentence is the entire portrait.

```prompt
SCENE:

Subject: a woman in her early fifties who has worked the same reception desk for eleven years, sitting behind the counter of an office lobby in a headset with a slim boom microphone, a call already in progress. She is an ordinary looking woman with an unremarkable face, a heavy build and no styling: greying hair pulled back with flyaway strands escaping around the headset band, reading glasses pushed up on her head, dry lips, visible pores and fine lines, a shine across her forehead and nose, a plain unironed blouse with the collar sitting crooked, a lanyard twisted so the badge faces the wrong way.

Composition: 16:9, a medium shot on a 50mm lens at f/2.8, taken from the far side of the counter at standing eye level and off to one side; she sits well right of centre with the empty run of the counter going away to the left; the near edge of the counter crosses the bottom of the frame close and thrown out of focus; the frame is tilted a few degrees off level.

Action: she is mid-word, saying something she says forty times a day. Her eyes are on the monitor to one side, not on the call. Her mouth is open on the word and the rest of her face is doing nothing at all — her cheeks are still, there is no movement around her eyes, and she is not smiling. One hand rests on a mouse.

Location: the lobby of a 1980s office tower that has been half refurbished — dark polished stone floor and dated stone cladding behind, newer steel turnstiles that do not match it, a laminate counter chipped along its front edge, a takeaway coffee cup standing in a dried brown ring, a curling stack of unclaimed visitor passes, old blu-tack marks on the wall panel behind her.

Light: one source only — cold daylight from the street glazing off to her right, raking across her face from the side so her pores and lines catch micro-shadow and the far side of her face falls into shade; the ceiling panels above are off; the front of the counter is dark.

Style: a documentary photograph on 35mm film, made for a newspaper story about office work rather than for the company; unretouched, no beauty retouching, natural skin with real texture; candid, caught rather than composed.

Constraints: keep the wall panel, visitor passes, screens, lanyard and every notice free of readable lettering; no border or frame edge around the image.
```

**Two notes before firing:**

- **The *"Hello, I'm —"* title is a `NarrationBox`, not text in the image.** Same rule as the
  newspaper: [load-bearing text belongs in the overlay](../../flow/failure-modes.md#a7-two-structural-rules-that-make-blocks-rare),
  where it is sharp, editable and unblockable.
- **Watch the hands.** One hand on a mouse is the least articulated hand pose available and
  it still does the storytelling. If the fingers come back mangled, **move the hand flat onto
  the counter** rather than trying to prompt the fingers right.

**What to watch: whether they are looking at the call.** Someone gazing warmly into the
middle distance means the plate has become *a nice receptionist* and the point is gone. The
eyes go on the screen.

> ### Round 1 fired 2026-08-17 — rejected as AI slop, and most of it was the prompt's fault
>
> **Three clauses in round 1 asked for the picture that came back:**
>
> | Round 1 wrote | Why it produced slop |
> | --- | --- |
> | *"a young front-desk worker"* | **a summons for stock photography** — that phrase's centre of gravity is a photogenic twenty-something in a headset, smiling at a screen |
> | *"flat overhead ceiling panels"* | **it prompted the flat light.** Pores and fine lines exist only as micro-shadow; flat overhead erases them. Every realism guide says directional sidelight `[community]` |
> | nine props in one Location line | **a long list gets deduplicated to generic nouns** — the model kept "coffee cup, plant, badge printer" and binned "scuffed", "dried ring", "tired" |
>
> Two failures were the model's own: **the smile** came back warm and eye-crinkling despite
> *"no movement around the eyes"* (the overacted-positive default), and **a film border was
> burned into the frame** — excluded by the §2.5 lock but not by §1's.
>
> **The highest-leverage fix was casting.** Rung 1 is now a woman in her early fifties who
> has worked the desk eleven years. It kills the stock attractor at the root, and it is
> truer: **the first person in Karen's way is not a gatekeeper, it is someone with no power
> at all.**
>
> **Round 2's other changes:** one named side light with the ceiling panels off · pores,
> fine lines, forehead shine, flyaway hair, dry lips — and **no "flawless", "beautiful" or
> "8k" anywhere**, since one such word undoes every texture term `[community]` · 50mm at
> f/2.8 so the lobby falls off · a half-refurbished 1980s lobby, because mismatch reads as
> real where a new glass box reads as a set · four props, each with its wear stated ·
> *"not smiling"* said three ways · *"no border or frame edge"* in Constraints rather than
> mutating the lock.
>
> **What landed in round 1 and did not change:** eyes on the screen, hand on the mouse, the
> counter and monitor as foreground occluders.
>
> **✅ Round 2 accepted 2026-08-17.**

### 2j.5v Rung 1, the block — clip

**Cast:** none. **Attach:** the accepted §2j.5 still. **Engine:** Gemini Omni Flash ·
**Ingredients to Video** · 8s · native audio · **Enhance Prompt off**.

> **⚠️ This is the first clip in the story with no Flow Character to bind the face.** Every
> accepted clip so far has been Ingredients + still + `@Character`, the still holding the
> staging and the Character holding the identity. **Here the still does both** — the
> [dual-role reference](../../google-flow/omni-flash.md#3--a-location-reference-must-not-contain-subjects)
> case. So identity is the risk, and **if she comes back as a different woman, retry the
> identical text in the Frames tab**: Frames is the mode that pins the opening frame, and
> there is no Character binding here for it to lose.

**The camera stays locked**, and that is a rhythm decision as much as a safety one: the
god's-eye camera travels, **the camera at the counter just stands there being ignored.**

**The performance is one gesture — a small shake of the head while she is still talking.**
That is the block made physical. She is not refusing Karen; she is saying no to something
she stopped hearing three sentences ago.

> ### Round 1 fired 2026-08-17 — the background walker vanished mid-stride
>
> Exactly the documented failure: *"background people appearing and vanishing."* **Not
> fixable by describing him better** — the fix is to stop asking for one.
>
> **The replacement is a house rule now, used twice: when a moving element fails, demote it
> to sound.** The reflected traffic in [§2h.6v](./prompts-morning-after.md#2h6v-karen-listens-in-the-kiosk--clip)
> went the same way. **The turnstile beep stays in the audio**, so the lobby still reads as a
> place people pass through — we simply never render them. A beep never grows a second leg.
>
> **The empty lobby is stated positively** — *"empty and still, and stays empty for the whole
> shot"* — because a "no people" instruction is the exact shape of negative
> [Omni inverts](../../google-flow/omni-flash.md#-negatives-do-not-work-and-they-actively-backfire).
> One small human beat replaces the lost motion: she shifts in the chair.

```prompt
Using the attached image as the locked opening frame, animate what happens next in one continuous shot. Keep the lobby, the counter, the light and her hair, glasses, headset and clothes exactly as they are in the frame.

She stays exactly where she is, talking. She is mid-sentence and she has said this before. Her mouth moves with the words without exaggeration and her eyes stay on the monitor to one side. Once, while she is still talking, she gives one small shake of the head, barely a movement. Her hand on the mouse shifts it an inch and settles. She shifts her weight in the chair once and settles again. Between phrases her mouth closes flat and her cheeks stay still.

The lobby behind her is empty and still, and stays empty for the whole shot.

The camera is locked and still throughout, at the far side of the counter. Available light only, real-time pace. Shot at 24fps with a 180-degree shutter. Fine film grain.

Audio is the lobby only: her voice low, flat and indistinct, the click and rattle of a keyboard, a double beep from the turnstile somewhere behind her, and the room tone of a hard-floored lobby.
```

**⚠️ The grain is back in this block**, unlike [§2j.1v](#2j1v-the-descent-rung-1--clip--the-master). This is Karen's world, so the super-8 register applies; the aerials are the photoreal ones. **Check the register per shot** — it is now a real fork in the checklist rather than a constant.

**What to watch:**

1. **Is it still her?** Drift lands entirely on the still. A different woman → re-run in Frames,
   identical text.
2. **Does the smile come back?** Round 1's failure gets a second chance at the animation
   stage. The mouth closing flat between phrases is the counter.
3. **Whether it invents someone anyway.** *"Stays empty for the whole shot"* does a
   negative's job without being one. If a figure still materialises at the turnstiles, the
   next lever is **cropping the reference so the turnstiles are out of frame** — nothing can
   hallucinate a walker into a wall.
4. **The mouse hand.** An inch is deliberately small. If fingers smear, drop the hand clause
   and let the head shake be the only motion.

---

## The plates this section still owes

Sketched so the order is visible; each gets written one at a time, on request.

| § | Plate | Notes |
| --- | --- | --- |
| **2j.1** | Aerial over Midtown, rung 1 | ✅ **fired and accepted 2026-08-17** — the master |
| **2j.1v** | The descent, rung 1 — clip | ✅ written — the clip master; it never arrives |
| 2j.2–2j.4 | The same aerial in rain, snow, low winter sun | one line swapped each |
| **2j.5** | Rung 1 interior — the front desk | ✅ **fired and accepted 2026-08-17, round 2** — **the interior template**; the camera stands where Karen cannot |
| **2j.5v** | Rung 1, the block — clip | ✅ written — one head shake, locked camera, **no Character to hold the face** |
| 2j.6 | Karen in the box, intercut | §2h kiosk still attached; **no crowd** |
| 2j.7 | Rung 2 interior — the borough office | the ladder's second face; **the dull-building joke lands here** |
| 2j.8 | Rung 3 interior — the councilman's assistant | |
| 2j.9 | Rung 4 interior — the Chief of Staff | the top of the on-screen ladder |
| 2j.10 | The newspaper easter egg | AI-taking-jobs headline, **background not foreground**; ideally the Camping prop paper. ⚠️ Legible headline text is the most reliable policy block there is — the line belongs in a `NarrationBox`, not in the image |
| 2j.11 | She is alone in it | the lone shot of her staring out of the box; the act's emotional exit |
