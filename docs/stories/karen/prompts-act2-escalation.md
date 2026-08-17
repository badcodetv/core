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

---

## The plates this section still owes

Sketched so the order is visible; each gets written one at a time, on request.

| § | Plate | Notes |
| --- | --- | --- |
| **2j.1** | Aerial over Midtown, rung 1 | ✅ written — the master |
| 2j.2–2j.4 | The same aerial in rain, snow, low winter sun | one line swapped each |
| 2j.5 | Rung 1 interior — the front desk | portrait of a functionary, not a conversation |
| 2j.6 | Karen in the box, intercut | §2h kiosk still attached; **no crowd** |
| 2j.7 | Rung 2 interior — the borough office | the ladder's second face |
| 2j.8 | Rung 3 interior — the councilman's assistant | |
| 2j.9 | Rung 4 interior — the Chief of Staff | the top of the on-screen ladder |
| 2j.10 | The newspaper easter egg | AI-taking-jobs headline, **background not foreground**; ideally the Camping prop paper. ⚠️ Legible headline text is the most reliable policy block there is — the line belongs in a `NarrationBox`, not in the image |
| 2j.11 | She is alone in it | the lone shot of her staring out of the box; the act's emotional exit |
