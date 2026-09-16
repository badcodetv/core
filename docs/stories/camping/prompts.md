---
story: camping
kind: record — prompts typed into Flow by hand, not a generation brief
flow_project: camping-v2 (`9b729074-da88-4668-a442-458e9a0f15ac`)
updated: 2026-08-27
---

# Camping — Flow prompt ledger

The exact prompts used to make Camping's stills and clips in **Google Flow**, kept
verbatim so any frame can be rebuilt from the same words.

> ## 🖐 Record, not a licence to generate
>
> Camping's imagery is **Jack's, made by hand in Flow outside this repo**
> ([`README.md`](./README.md)). This file exists so a lost asset can be reproduced from
> the exact prompt rather than reinvented. Do not generate new Camping imagery from
> these blocks and do not "improve" the wording — they are a restore point.
>
> Modelled on [Karen's ledger](../karen/prompts.md), which came first.

## ⚠️ Gaps — prompts that produced accepted frames and are **not** recorded here

Started 2026-08-25, so everything shot before that date is missing its words.

**1a, 1b, 1c and the 2a still were recovered 2026-08-26** and are recorded in full below — the worst gap is closed.

✅ **No gaps remain.** Every still shot through scene 4 is recorded verbatim below. The one
outstanding item is not a missing prompt: **4a's entry is byte-identical to 1a's**, because 4a
is an edit of that frame, and the wording of the *swap* itself was never written down.

*(1d was struck from the shot list on 2026-08-26 — 1b absorbed the newspaper plant. It is not
a missing prompt; it is not a shot.)*

---

## Conventions

- **Stills only** *(ruled 2026-08-26)*. The ledger records **still prompts**, because those are
  the ones that take rounds to get right and are worth a restore point. **Video prompts are
  self-explanatory** — they continue from an accepted still and say what moves — and are not
  worth recording going forward. The video prompts already in this file stay; they are not a
  precedent.
- Every prompt ends with `Thanks.`
- Never name a repo character in a prompt — say *"the man in the reference image"*.
- **Video is generated on Omni Flash** (ruled 2026-08-25). The one accepted exception is
  noted against 2b below.

---

## Scene 1 — 2008, the City

### 1a — the 2008 skyline plate · **still** · accepted · 🔒 the plate

**Recovered 2026-08-26**, from Jack, after it turned out not to exist anywhere in the repo,
in git history, in the dangling objects or on disk. It had only ever lived in Flow. This is
**the single most important restore point in the film** — 4a is made from this frame.

**Reference image:** [`camera/reference/1a-framing-reference-shard-aerial.png`](./camera/reference/1a-framing-reference-shard-aerial.png)
— a present-day aerial with the Shard dead centre, the City cluster behind, St Paul's right
and the river across the lower third. It supplies the **framing, altitude and composition**;
the prompt then does the era, swapping the hero tower for the old NatWest Tower and stripping
the modern cluster out by name. ⚠ Provenance of that reference is not recorded — paste in
where it came from when convenient.

Note the technique worth keeping: the hero tower is **described, never named** — three
chevron-shaped shafts around a central core, bronze-dark glass, a lattice mast — and the
modern towers are excluded as *shapes* (tapering spire, curved top, wedge) rather than as
names. Same for the Gherkin, the 1960s slabs and St Paul's, all described and none named.

```prompt
SCENE:

Subject: a single tall dark office tower standing dead centre of frame, filling the middle third from top to bottom, seen from the air from slightly above its midpoint, with a low old city spread wide behind and below it.

Environment: the City of London as it stood in 2008, before the current cluster of glass towers was built. The hero tower is a 1980 office block built as three chevron-shaped shafts cantilevered around a central core, stepping down to three different heights, clad in bronze-dark glass with strong vertical ribbing and a slim lattice mast on the roof; it stands completely clear of everything around it and is by far the tallest thing in the frame. Behind and beside it the city is low and dense — Portland stone and red brick blocks of six to ten storeys, church spires, flat grey roofs and rooftop plant. One rounded glass tower with a diagonal diamond lattice stands a little way off to one side, and two dark flat-topped 1960s slabs sit nearer the middle. A wide grey-brown river crosses the lower third of the frame with a road bridge to the right, and a domed stone cathedral sits among the rooftops on the right. Two construction cranes stand over the low roofs in the middle distance. The sky above the hero tower is completely empty.

Camera: wide lens, high aerial, hovering level with the upper third of the hero tower and looking very slightly down, the tower centred and dead vertical, the horizon high in the frame. Deep focus, sharp from the tower all the way to the horizon.

Lighting: a cold clear spring morning, the sun low and hard from the left throwing long shadows east across the rooftops. The hero tower's dark glass reads almost black against a pale sky, and one band of windows partway up its face catches the low sun and flares bright. Distance haze softens the far horizon into flat grey layers.

Details: cinematic, filmic contrast, fine 35mm grain, atmospheric haze between camera and far city. No modern glass towers of any kind — no tapering glass spire, no curved-top tower, no wedge-shaped tower, no cluster of tall towers behind the hero. Keep every sign, banner and rooftop marking free of readable lettering.

Compose for a 16:9 frame.

Thanks.
```

> ⚠ **1a does not end with the house `Thanks.` convention preceded by a Details block in the
> usual order** — it is recorded exactly as typed. Do not tidy it. It is a restore point.

### 1a-year — the 2008 skyline with the year in the cloud · **still** · written 2026-08-30, unrun

**Why this exists:** the year device — [`year-device.md`](./year-device.md). Jack ruled
2026-08-30 that **2031 goes to the narration**, so the on-screen year is a two-instance device:
`1a` = 2008, `4a` = 2026, same framing, same slot, one number changing.

**This is a NEW PROMPT, not an edit** — the whole `1a` scene is restated and **the sky clause is
the only thing that has changed**. One variable, so we know what did it.

🔒 **The accepted `1a` is not overwritten and not deleted.** This is a variant. If it does not
match, the fallback is an ffmpeg `drawtext` overlay on the existing frame and nothing is lost.

**Reference image:** the **accepted `1a` master** (in Flow, not in this repo — see
[`camera/reference/README.md`](./camera/reference/README.md)). Its role is **framing, altitude
and composition**.
🔴 **Do not attach the Wikimedia photographs in `camera/reference/`** — three of the four are
CC BY-SA and their pixels must not survive into a frame we ship.

**What changed from `1a`, and only this:**

- The sky went from *"completely empty"* to **an overcast lid with the year torn clean out of it**.
- The lighting clause gained *"under the cloud lid"* so a low hard sun and an overcast ceiling
  are not contradicting each other.
- The no-lettering rule gained one carve-out: **the numerals are the only legible characters in
  the picture.**
- Two anti-slop clauses added by name — no flare, no glow, no bloom; grain and haze asked for
  explicitly. Bare "photorealistic" gets you plastic.

⚠️ **Check the numerals at 100% before accepting.** Gibberish in-frame text is the most-cited
tell there is. Isolated large numerals are the reliable case — but they are not a guarantee.

```prompt
SCENE:

Generate a hyper-realistic documentary photograph on 35mm colour negative — fine natural grain, muted and cool, real atmospheric haze, slightly uneven exposure. Naturalistic motivated light only. No lens flare, no glow, no bloom, no halo.

Subject: a single tall dark office tower standing dead centre of frame, filling the middle third from top to bottom, seen from the air from slightly above its midpoint, with a low old city spread wide behind and below it.

Environment: the City of London as it stood in 2008, before the current cluster of glass towers was built. The hero tower is a 1980 office block built as three chevron-shaped shafts cantilevered around a central core, stepping down to three different heights, clad in bronze-dark glass with strong vertical ribbing and a slim lattice mast on the roof; it stands completely clear of everything around it and is by far the tallest thing in the frame. Behind and beside it the city is low and dense — Portland stone and red brick blocks of six to ten storeys, church spires, flat grey roofs and rooftop plant. One rounded glass tower with a diagonal diamond lattice stands a little way off to one side, and two dark flat-topped 1960s slabs sit nearer the middle. A wide grey-brown river crosses the lower third of the frame with a road bridge to the right, and a domed stone cathedral sits among the rooftops on the right. Two construction cranes stand over the low roofs in the middle distance.

Sky: a high unbroken lid of flat grey overcast lies across the whole upper third of the frame. Torn out of that cloud, and nothing else, are the four numerals 2 0 0 8. They are very large, spanning most of the width of the frame, sitting high above the rooftops, with the hero tower's lattice mast rising in front of them. They are holes in the cloud showing pale sky behind — not writing, not light, not projected. The cloud has simply parted in that shape. The overall shape of each numeral is clean and unmistakable, while the actual cloud edge along it is soft and slightly ragged the way a real break in overcast is ragged. The numerals do not glow, do not cast beams, and do not light the city.

Camera: wide lens, high aerial, hovering level with the upper third of the hero tower and looking very slightly down, the tower centred and dead vertical, the horizon high in the frame. Deep focus, sharp from the tower all the way to the horizon.

Lighting: a cold spring morning, the sun low and hard from the left underneath the cloud lid, throwing long shadows east across the rooftops. The hero tower's dark glass reads almost black against the pale sky, and one band of windows partway up its face catches the low sun and flares bright. Distance haze softens the far horizon into flat grey layers.

Details: cinematic, filmic contrast, fine 35mm grain, atmospheric haze between camera and far city. No modern glass towers of any kind — no tapering glass spire, no curved-top tower, no wedge-shaped tower, no cluster of tall towers behind the hero. Every sign, banner and rooftop marking is free of readable lettering: the four numerals in the cloud are the only legible characters anywhere in the picture.

Compose for a 16:9 frame.

Thanks.
```

**If accepted → the clip.** Omni Flash, **Frames** tab, this still as the start frame, **end slot
empty** (Omni Flash errors on an end frame). Camera locked. The motion budget is spent on cloud
drift and nothing else:

```prompt
The attached image is the locked opening frame. The camera does not move at all — no push, no pan, no drift, no reframe. The high overcast lid moves slowly left to right across the top of the frame, and the four numerals torn out of it hold their shape and their position while the cloud creeps around their edges. Haze shifts very slightly over the far city. Nothing else in the frame moves.

Thanks.
```

**Then `4a`** — the same prompt with the hero tower swapped for the tapering glass spire, the
modern cluster restored, and the numerals reading **2026 in the identical position**. Written
only after the 2008 still is accepted, so the pair matches by construction.

### 1a-year — round 1, **not accepted**: the model inverted the device, and the physics were against it

Run 2026-08-30 against the accepted `1a` master. Two failures, and only one of them is phrasing.

#### 🔴 The cause: "torn out of" is a **subtractive** instruction, and the model has no picture of one

The prompt asked for *holes in the cloud showing pale sky behind — not writing, not light, not
projected.* What came back is **four dark soot-coloured blobs sitting on top of a grey lid** —
the exact inverse. The model does not have a trained visual for *an absence shaped like a
numeral*; it does have one for **smoke writing**, so it substituted the nearest trope it owns.
That trope is the thing [`year-device.md`](./year-device.md) explicitly **rejected** ("it puts an
author in the sky where we want a narrator"), and the failure walked us straight into it.

🔑 **The generalisable finding: ask for a dark object on a pale ground, never for a pale gap in a
dark field.** Additive shapes render; subtractive ones invert. This applies to every future
device on this film.

#### 🔴 The second cause is worse, because no prompt fixes it: **overcast has no contrast to give**

A hole in a flat grey lid shows **pale grey sky** behind it. Overcast grey against sky grey is
almost no separation at all. To make four numerals read at that size the model needed contrast,
and the prompt had banned the only two ways of getting it — *no glow, no bloom* forbade making
them brighter, so the one route left was making them **darker**. The device asked for legibility
and forbade the means. **It is self-defeating on the physics, not on the wording**, and a round 2
with better phrasing would hit the same wall.

#### ⚠️ It also broke the matched pair, which is the device's whole engine

Comparing the return against the `1a` master: the rounded lattice tower moved from the left of
frame to the right, the hero tower lost its stepped chevron shafts and came back a flat slab, the
domed cathedral shifted, and the horizon dropped. **`1a` and `4a` match by being the same
picture.** A sky rewrite that also re-rolls the skyline cannot found a pair.

#### ✅ The ruling, 2026-08-30: **the cloud break is struck.** The year moves to the foreshore.

Jack's alternative — [`year-device.md`](./year-device.md) tier 2, *seaweed on the Thames
foreshore at low tide* — is promoted to the device. It was graded down only because it will not
read at `1a`'s altitude, which is true and is **not an argument against the idea, only against
putting it in that frame.** It gets its own frame. See `1y` below.

🔒 **The accepted `1a` is untouched and its sky stays empty.** That is now a feature: with the
year living somewhere else, the film's most important restore point is **never regenerated at
all**, and neither is `4a`. The cloud prompt above is kept as the record of what was tried.

### 1y — the year on the foreshore, 2008 · **still** · written 2026-08-30, unrun

**Why this exists:** the year device, after the cloud break failed —
[`year-device.md`](./year-device.md). Pairs with **`4y`** (2026), which is the identical frame
with the skyline and the tide line changed. **The pair is the device; neither shot is worth
running alone.**

#### The design — and why the foreshore beats the sky on all four tests

| Test | Cloud break | Foreshore |
| --- | --- | --- |
| **Contrast** | 🔴 grey on grey; needs a glow it is forbidden | ✅ near-black wet weed on pale reflective mud. The mud holds the sky and everything on it reads black |
| **Slop resistance** | 🔴 crisp synthetic shape in a soft medium | ✅ ragged organic glyphs are what a viewer *expects* from weed, so the model's imprecision stops being a tell |
| **Gate 2 — a visible cost in frame** | ⚠️ borrowed from the skyline below | ✅ built in, and it is the tide line: in 2026 the same digits are silted, and the plastic is tangled through them |
| **Register** | 🔴 someone is *writing* in the sky — an author, not a narrator | ✅ the water left it there. Sediment, not authorship. **That is the BadCode claim exactly: this already happened, and here is what washed up** |

**Two more things it buys that the sky version could not:**

- 🔒 **`1a` and `4a` are never regenerated.** The year stops threatening the film's restore point.
- 🔑 **It carries the graphic match *and* the number in one frame.** The foreshore is the one part
  of London that looks the same in 2008 and 2026 — same mud, same stumps, same tide. So the pair
  matches by construction, with no era-stripping, and the *only* things that differ are the small
  hazy skyline over the wall and what the tide has done to the weed. The skyline pair says **the
  city changed**; the foreshore pair says **the river did not, and it kept the receipt.**

**The shot spec:**

- **Job:** date the film, and plant the bookend, without stopping it. ~1.5–2s, before the `1a`
  establisher.
- **Depth:** ⚠️ three planes, all populated — near, the dark stone coping and rusted rail of the
  river wall along the bottom edge; mid, the weed digits on open mud and a broken row of rotted
  jetty stumps; far, the water, the opposite wall, and the hazy city above it.
- **Focal point:** the digits, winning on **contrast** — the only near-black in a pale frame.
- **Light:** flat overcast, no sun, no shadows. 🔑 **The wet mud is the bright anchor** and it
  works by reflection, which is the inverse of our usual near-black rule and the reason this
  frame is legible where the sky one was not.
- **Camera:** high oblique from the top of the wall, ~5m above the mud, tilted down ~45° so the
  numerals lie flat and read without distortion. It **rhymes with `1a`** — the film looks *down*
  at both.
- **Scale reference:** the jetty stumps and the mooring ring.
- **Withheld:** no people. The tide wrote it and left.
- **Motion:** the camera is locked. Water creeps at the far edge; one gull. Nothing else.

**Reference image:** ⬜ **none.** New location, no composition to preserve, and nothing here has
to match an existing plate. 🔴 **Do not attach the Wikimedia photographs in `camera/reference/`**
— three of the four are CC BY-SA.

⚠️ **Check the numerals at 100% before accepting**, and check them for the right failure: a weed
`0` that has closed into a blob, or an `8` whose waist has filled in.

```prompt
SCENE:

Generate a hyper-realistic documentary photograph on 35mm colour negative — fine natural grain, muted and cool, real atmospheric haze, slightly uneven exposure. Naturalistic motivated light only. No lens flare, no glow, no bloom, no halo.

Subject: four numerals — 2 0 0 8 — lying flat on the exposed mud of a tidal river foreshore at low tide, seen from above and at an angle from the top of the river wall. They run across the middle of the frame, large and clearly readable at a glance.

The numerals are made of real river weed, physically lying on the ground where the tide left it: long matted strands of green-black algae and bladderwrack, piled a few centimetres thick, soaked and dark and shining wet. They are objects on the mud, not writing, not drawn, not painted and not carved. The overall shape of each numeral is clean and unmistakable, while the actual edge of the weed is ragged and frayed, strung with loose strands, small shells and bits of debris, the way a real tide line is ragged. The wet grey-brown mud around them is pale, smooth and reflective and holds the flat white sky, so the weed reads almost black against it.

Environment: a London tidal river foreshore at dead low water. Ribbed grey-brown mud and grey shingle, flat stones, chalk and worn brick rubble, a rusted iron mooring ring set into the stonework. A broken row of rotted black timber jetty stumps runs across the middle distance out toward the water. Beyond them the wide grey-brown river, and beyond that a high stone and brick embankment wall. Small and far off above that wall, softened by haze, the low roofs of an old city with one tall dark office tower standing clear of everything around it. In the immediate foreground along the bottom edge of the frame, the dark stone coping of the near river wall and a rusted iron handrail cross the corner.

Camera: wide lens, standing on the top of the near river wall about five metres above the mud, tilted down roughly forty-five degrees and looking out across the foreshore, so the numerals lie flat and read clearly without perspective distortion and the far bank sits high in the frame. Deep focus, sharp from the weed in the near foreground all the way to the far city.

Lighting: a cold overcast morning, no sun and no shadows, a flat white sky. The wet mud is the brightest thing in the picture — it reflects the pale sky and glares softly — and everything lying on it reads dark against it. Distance haze softens the far bank and the city into flat grey layers.

Constraints: the numerals are dark weed on pale mud, never pale shapes in a dark field. Nothing in the sky at all — no writing, no smoke, no vapour trail, no break in the cloud. Nothing glows, nothing is lit from within, nothing casts a beam. No people anywhere in the frame, and no boats.

Details: cinematic, filmic contrast, fine 35mm grain, real atmospheric haze between camera and the far bank. Every sign, marking and painted surface is free of readable lettering: the four numerals of weed are the only legible characters anywhere in the picture.

Compose for a 16:9 frame.

Thanks.
```

**If accepted → the clip.** Omni Flash, **Frames** tab, this still as the start frame, **end slot
empty**. Camera locked; the motion budget is spent on water and one bird:

```prompt
The attached image is the locked opening frame. The camera does not move at all — no push, no pan, no drift, no reframe. The water at the far edge of the mud creeps very slightly, its surface moving. One gull crosses low over the foreshore and out of frame. The weed on the mud does not move at all and the four numerals hold their exact shape and position. Nothing else in the frame moves.

Thanks.
```

**Then `4y` — 2026, and it is the same frame.** Written only once `1y` is accepted, so the pair
matches by construction. Only three things change, and each of them is the point:

- The tall dark office tower over the wall becomes **the tapering glass spire and the cluster
  around it**, still small and still in haze.
- The weed numerals read **2 0 2 6**, in the identical position and at the identical size.
- 🔑 **The tide line has got worse.** The digits are half-silted and the weed is threaded through
  with plastic — bags, bottles, a tangle of blue rope, a shopping trolley on its side among the
  jetty stumps. Same river, same mud, eighteen years of what washed up.


### 1y — round 1 · ✅ **ACCEPTED** (Jack, 2026-08-30: *"the 8 is fine"*) · 🔒 the year plate

🖼 **Master banked:** [`camera/reference/1y-foreshore-2008-ACCEPTED.png`](./camera/reference/1y-foreshore-2008-ACCEPTED.png).
This is the plate the clip is generated from and the plate `4y` must match.

⚠️ **The round-2 rewrite below was written and never run — Jack accepted round 1 over it.** It is
kept because its two diagnoses were real and `4y` will meet both of them, and because the far-bank
ruling stands: `4y` copies **this** frame, skyline and all.

**The two notes that survive into `4y`, now as continuity facts rather than defects:**

- **The far bank in the accepted frame is generic riverside, not the City.** It is now canon for
  the pair, so 🔴 **`4y` reproduces it unchanged** — same slab, same cluster, same wall. The
  skyline change is `1a` → `4a`'s job and this pair must not compete with it.
- **The camera is ~2–3m up at ~30°, not the 5m/45° asked for.** `4y` must match the accepted
  frame, not the prompt. Copy the geometry off the plate.

#### What the round-1 return got right, and must not be lost

Run 2026-08-30. **The idea works and the failure mode has flipped.** The cloud version failed at
the concept; this fails only at legibility, and both causes are geometry.

- ✅ **Dark weed on pale reflective mud reads.** The sheet of water over the ribbed mud is the
  bright anchor exactly as designed, the weed sits near-black on it, and there is no glow, no
  bloom and no sun anywhere. The contrast problem that killed the cloud version is **solved**.
- ✅ **Three depth planes, all populated** — brick rubble, cobbles, a rusted mooring ring and the
  handrail near; weed and the broken row of jetty stumps mid; river and far bank beyond.
- ✅ **Gate 2 comes free** — the rubble and broken tile are already the cost, and they have
  somewhere to escalate to in `4y`.
- ✅ Overcast, no shadows, no people, no boats, no readable lettering.

#### ⚠️ The one reservation, overruled by Jack — the `8`

At 100% the fourth glyph is **two disconnected pieces** — a top-right diagonal and a separate
lower loop. It reads closer to `%` than to `8`. Context carries it at a glance, which is exactly
why it is dangerous: **the one instance where the year has to be unambiguous is the one where it
is guessed.**

🔑 **The cause is foreshortening.** The prompt asked for ~5m of camera height and a ~45° down
tilt; the return is nearer 2–3m and ~30°. The digits therefore lie in hard perspective and
compress toward the far end of the row — and the `8`, being furthest, compresses most, so its
waist opens. **Raise the camera and steepen the tilt and the glyph problem fixes itself**, before
a single word about the weed changes.

⚠️ Second-order: the water sheet has crept **over** the weed rather than stopping short of it,
which softens every edge. Keep the water — it is doing the lighting — but hold it beyond the row.

#### ⚠️ The far bank came back as a generic riverside, not the City

The prompt asked for *low roofs of an old city with one tall dark office tower standing clear*.
What arrived is a pale 1960s slab centre-frame with an unrelated cluster off to the right —
**Wapping, not the City**, and the pale slab sits near the vanishing point where the eye goes.

#### 🚫 Ruled and then overtaken: **strike the skyline entirely** — *superseded by the accepted round 1, which kept it.* The reasoning is kept because the conclusion it protects still holds: **the skyline must not change between `1y` and `4y`.**

The reason to keep it was to let `4y` swap it. But the skyline change is **already carried by
`1a` → `4a`**, and asking `1y` to carry it a second time buys a repetition and a generation risk
for nothing. Removing it makes the device **purer**: `1y` and `4y` then differ in *only* the
numerals and the tide line, which is the whole claim — **the river did not change, and it kept
the receipt.** The steeper tilt of the round-2 camera removes it for free by putting the far bank
at the top edge, and it takes the dead white sky band out with it.

⚠️ **Two changes in one round, against the usual one-variable rule.** Accepted here because they
are **orthogonal and both diagnosed rather than guessed** — camera geometry and what is on the
far bank cannot mask each other, and the steeper tilt is the fix for both.

### 1y — round 2 · **still** · written 2026-08-30 · 🚫 **not run, superseded by the accepted round 1**

🔴 **No reference image, again.** The round-1 frame is *not* attached: the composition is the
thing being changed, and a reference beats the prompt on composition every time
([`nano-banana-2.md` §21, §24](../../google-flow/nano-banana-2.md)). Attaching it would reinstate
the low camera that caused the failure.

**What changed from round 1, and only this:**

- **Camera up to ~8m and tilt down to ~55°**, so the numerals lie nearly flat to the lens and
  stop foreshortening. Far bank pushed to the top edge; almost no sky.
- **The `8` is named as a failure** in the `Constraints:` block — the house pattern from `4b`.
- **The water is told to stop short of the weed.**
- **The skyline clause is deleted**, and the far bank is told to be a plain wall.

```prompt
SCENE:

Generate a hyper-realistic documentary photograph on 35mm colour negative — fine natural grain, muted and cool, real atmospheric haze, slightly uneven exposure. Naturalistic motivated light only. No lens flare, no glow, no bloom, no halo.

Subject: four numerals — 2 0 0 8 — lying flat on the exposed mud of a tidal river foreshore at low tide, seen from high above and looking steeply down. They run across the middle of the frame, very large, and each one is unmistakable.

The numerals are made of real river weed, physically lying on the ground where the tide left it: long matted strands of green-black algae and bladderwrack, piled a few centimetres thick, soaked and dark and shining wet. They are objects on the mud, not writing, not drawn, not painted and not carved. Each numeral is formed from one continuous unbroken band of weed of even thickness, so its shape is closed and complete and reads instantly: the two zeros are closed rings, and the eight is two closed loops joined at a clear narrow waist. The outer edge of the weed is ragged and frayed, strung with loose strands, small shells and bits of debris, the way a real tide line is ragged, but the shape underneath it stays clean. The wet grey-brown mud around them is pale, smooth and reflective and holds the flat white sky, so the weed reads almost black against it.

Environment: a London tidal river foreshore at dead low water. Ribbed grey-brown mud and grey shingle, flat stones, chalk and worn brick rubble, a rusted iron mooring ring set into the stonework. A broken row of rotted black timber jetty stumps runs across behind the numerals out toward the water. Beyond them the wide grey-brown river, and along the very top edge of the frame the plain top of a far stone and brick embankment wall with a thin strip of flat white sky above it and nothing else. In the immediate foreground along the bottom edge, the dark stone coping of the near river wall, broken bricks and tile, and a rusted iron handrail crossing the corner.

Camera: wide lens, high on the near river wall about eight metres above the mud, tilted steeply down at about fifty-five degrees, so the foreshore fills almost the whole frame, the numerals lie nearly flat to the lens with very little perspective compression, and the far bank sits right at the top edge. Deep focus, sharp from the rubble in the near foreground to the far wall.

Lighting: a cold overcast morning, no sun and no shadows, a flat white sky. The wet mud is the brightest thing in the picture — it reflects the pale sky and glares softly — and everything lying on it reads dark against it. Distance haze softens the far wall into a flat grey layer.

Constraints: the numerals are dark weed on pale mud, never pale shapes in a dark field. Every numeral is closed and continuous — no broken strokes, no gaps, no piece of a numeral detached from the rest, and the eight is never open at its waist. The mud under and around the numerals is wet and reflective but the standing water stops short of them, so the weed is not submerged and its edges stay sharp. No buildings and no towers of any kind on the far bank or anywhere on the horizon. No people, no boats, no birds. Nothing glows, nothing is lit from within, nothing casts a beam.

Details: cinematic, filmic contrast, fine 35mm grain, real atmospheric haze between camera and the far wall. Every sign, marking and painted surface is free of readable lettering: the four numerals of weed are the only legible characters anywhere in the picture.

Compose for a 16:9 frame.

Thanks.
```

⚠️ **Accept on the `8` alone.** Everything else in round 1 already passed. If the `8` still opens
after this, **stop asking Flow for it** — the house precedent is the scene-10 sign, two failures
then post — and the fallback is a clean plate with the weed digits comped in, or `drawtext`. That
fallback is cheap here in a way it never was on the establisher.


### 1y — the tide coming in · **video** · written 2026-08-30, unrun

**Recorded despite the 2026-08-26 stills-only ruling**, because this one is not self-explanatory:
it carries a design decision, a research pass and the reason the camera move is *not* in it.

**Routing:** Omni Flash → **Frames** tab, the accepted `1y` master as the **start frame**, **end
slot empty** (Omni errors on an end frame). Frames, not Ingredients, because
[the composition is everything and Ingredients re-stages](../../google-flow/omni-flash.md#️-the-combined-mode-does-not-exist-in-flow).
No Characters are needed, so the tabs being mutually exclusive costs nothing. 10s available; **generate the full 10s** even though the cut wants far less — the gesture needs runtime, and the last few seconds are the strongest.

#### 🔑 The design: the film opens on the year already being taken

The still is a photograph, and [`stills.md`](../../cinematography/stills.md) is blunt about what
that costs: **a frame whose first and last frames match reads as a photo, not a shot**, and a held
image only grips if it contains **an unresolved question**. So the clip needs one event, and it
should be the one the location supplies for free.

**The tide is coming in.** Over ten seconds the leading edge of the water creeps up the mud toward
the numerals and reaches the foot of the first one just as the shot ends. It never covers them.

Why this and not something else:

- **It is the narrator's whole claim, stated in water.** The film opens with its own date already
  being erased. *Received wisdom from a future that already went wrong* — and the first image is
  the evidence going under.
- **It sets up `4y` for free.** 2008 is being taken; by 2026 the same digits are silted and
  plastic-threaded. The tide got it. **Same river, same mud, and it kept the receipt.**
- 🔑 **It is the easy motion, not the hard one.** Google's own model card lists *scenes with
  complex motion* as a known failure mode. A slow single-vector flood across a flat plane, with
  everything else static, is close to the easiest thing this engine is ever asked to do.
- **It is one system, not two.** Water advancing, weed stirring where it arrives, and the sky
  reflection shifting are all *the same physical event*. That satisfies the **one main action per
  clip** rule while still giving three visible things to look at.

#### 🔴 The camera does NOT move — and that is not timidity, it is the house method

[`hybrid-method.md`](../../video-fx/hybrid-method.md): **the generator animates the world with its
camera locked; Premiere moves the camera** over the finished clip, rigid by construction and
exactly eased. Camera translation is what triggers the regeneration bug, so locking it is also the
cheapest reliability win available.

⚠️ **And Omni defaults to cutting** — left alone it *"builds a short narrative from a few different
shots."* `[yt]` For a slow single move that is the failure most likely to ruin the shot, so
`single continuous shot, no cuts` and `locked off` are load-bearing, not decoration.

**The move this shot wants, and where it goes:** ⬜ a **very slow push in** on the numerals across
the back half — the push-in means *narrowing toward a realisation*, and what is at the end of it is
the year. **That is a Premiere job on the finished clip**, not a clause in this prompt.
⬜ Optional second post pass: a barely-perceptible luminance ramp as the overcast thins. Also not
Flow's — it is an ffmpeg job precisely because it must be *imperceptible*, which is exactly the
kind of exactness Flow cannot be trusted with.

#### 🔴 Anti-slop, worked per tell — the two that actually threaten this shot

Researched 2026-08-30; the general list is in [`year-device.md`](./year-device.md). Only the ones
that bite here:

| The tell | Why it threatens *this* clip | The clause that answers it |
| --- | --- | --- |
| 🔴 **In-scene text turning to gibberish** — the most-cited tell there is | **The numerals are made of weed, and the clip re-renders every surface every frame.** This is the shot's single biggest risk: the model has licence to reflow them | The weed numerals are named as **objects that do not move, shift or change shape**, and the water is told to **stop at the foot of the first numeral** so it never has a reason to touch them |
| 🔴 **Flat, uncanny lighting** — *"AI's default aesthetic is 'pleasant cloudy afternoon'"* | ⚠️ **Our shot is literally an overcast morning.** We are starting inside the default | The plate already beats it — the light is *motivated by the wet mud*, which reflects the sky and does the work a key light would. Hold it: **name the mud as the bright thing** and let nothing else glow |
| **Repeating texture tiling** — named risk on large surfaces | The ribbed mud is exactly that surface | Name the irregularity: the ripples **vary in size and spacing and are broken by stones and rubble** |
| **Unnaturally smooth, floaty motion / no micro-jitter** | The usual fix is camera vibration — ⚠️ **we must not take it**, because inviting the camera to move is the failure above | Take it in the *water* instead: the flood edge **finds the ribs and hollows and fills them unevenly, never a straight line.** Irregularity is bought in the physics, not the camera |
| **Too clean, no grain** | Bare "cinematic" gets plastic | `24fps, 180-degree shutter, fine 35mm grain` — the 24/180 clause is `[confirmed 2026-08-14]` as earning its place |
| **Background figures with impossible gaits** | A gull would be lovely and is a known artefact class | 🔑 **Put the gull in the audio and not in the frame.** One call off-screen implies the world at zero render risk |
| **Mirror / reflection breakdown** | We have a large wet reflective sheet | Ask only for the **diffuse sky** shifting on it. Never ask for an object's reflection |

⚠️ **And define the bare surfaces.** `[confirmed 2026-08-17, Karen §2j.6sv]` — a clip block that
never mentioned signage came back with writing crawling onto a sign. Under our no-legible-text rule
the move is to give the model something specific to satisfy instead of a vacuum to fill, so the
constraints line states it outright.

#### ⚠️ A live conflict in the sources — read before you shorten this

[`omni-flash.md`](../../google-flow/omni-flash.md) records `[yt]`/`[community]` advice to **keep
Omni prompts under ~50 words**, because length *"dilutes focus and reduces output quality"* — the
biggest single difference from writing for Veo. Fresh practitioner guidance (2026) says the
opposite: example prompts run **150–300 words** and *"density of specification matters more than
brevity."*

**Unresolved, and neither side is house-measured.** The primary below is ~170 words and is written
so the whole first half is the frame-lock and the camera, which is where adherence is decided. **A
50-word fallback follows it.** If the primary drifts — the camera moves, or it cuts — fire the
fallback before rewriting anything, and 🔑 **record which one worked**, because that settles the
conflict for every clip after this one.

**Primary:**

```prompt
The attached image is the locked opening frame.

One continuous shot, no cuts. The camera is locked off on a tripod and does not move at all — no push, no pull, no pan, no tilt, no drift, no reframe. Shot on 35mm at 24 frames per second with a 180-degree shutter, fine natural grain, muted and cool and desaturated.

The tide is coming in. Through the whole shot the leading edge of the water creeps slowly up the wet mud from the bottom of the frame toward the numerals — a thin advancing sheet that finds the ribs and hollows in the mud and fills them unevenly, never a straight line. The mud ripples it crosses vary in size and spacing and are broken by stones and rubble. It reaches the foot of the first numeral only at the very end and goes no further. Loose strands of weed at the outer edges stir a little where the water touches them. The pale sky reflected in the wet mud shifts slowly as the surface moves.

The four weed numerals are solid objects lying on the ground. They do not move, do not shift, do not change shape and are never covered by the water. Nothing else in the frame moves.

Constraints: no people, no boats, no birds and no vehicles anywhere in frame. No text, writing, signage or markings of any kind — every surface stays bare. Nothing glows and nothing is lit from within; the wet mud is the brightest thing in the picture. No lens flare, no bloom.

Audio: water spreading thinly over mud and shingle, a low river hum, cold wind across open ground, and one gull calling somewhere off screen. No music, no voices and no dialogue.

Thanks.
```

**Fallback, ~50 words** — fire this if the primary drifts, before rewriting a word of it:

```prompt
The attached image is the locked opening frame. One continuous shot, no cuts, camera locked off, no camera movement of any kind. The tide creeps slowly up the wet mud toward the numerals and stops at the first one. The weed numerals never move or change shape. 35mm, 24fps, fine grain. Audio: water over mud, wind, a distant gull. No music, no voices.

Thanks.
```

#### What to check before accepting

1. 🔴 **The numerals at 100%, on the last frame as well as the first.** Reflow is the risk; a `0`
   that has thickened or an `8` that has opened between frame 1 and frame 240 kills the take.
2. **Did the camera stay put?** Any push, drift or reframe → fallback prompt, not a rewrite.
3. **Did it cut?** Same answer.
4. **Is the water's edge ragged?** A straight advancing line is the floaty-motion tell wearing a
   costume.
5. **Nothing crawled onto a surface** — no writing on the far wall, the coping or the stumps.

#### Then the post pass

⬜ **Premiere:** the slow push in on the numerals over the back half, and the cut point. Use the
**last few seconds**, where the water is closest — that is where the shot's question is sharpest.
⚠️ [`edit-plan.md`](./edit-plan.md) wants clips down to ~4.6s average, and this insert was
budgeted at 1.5–2s. **It is worth 3–4s** — a gesture that resolves cannot be paid for in two
seconds, and the seconds should come out of the flabby middle of the film, not out of its first
image. Jack's call.


### ⚠️ Two `1y` takes exist — the master was swapped 2026-08-30

Jack accepted the year plate on one take and then handed a **different, wider take** as the
reference for `4y`. The second one governs, and it is the better frame: more foreshore, the jetty
stumps read as a row rather than a clump, and — the thing that was ever in doubt — **the `8` is
cleanly closed on both loops.**

| File | Status |
| --- | --- |
| [`camera/reference/1y-foreshore-2008-ACCEPTED.png`](./camera/reference/1y-foreshore-2008-ACCEPTED.png) | 🔒 **the master.** The take Jack handed over as the `4y` reference. Everything downstream matches this one |
| [`camera/reference/1y-foreshore-2008-alt-round1a.png`](./camera/reference/1y-foreshore-2008-alt-round1a.png) | The first accepted take, kept. Tighter framing, weaker `8` |

⚠️ **The clip prompt above was written against the alt take.** Nothing in it needs changing — it
describes motion and names no geometry — but **generate the clip from the master**, not the alt,
or the film's opening shot and its 2026 rhyme will not be the same picture.

### 4y — the year on the foreshore, 2026 · **still** · written 2026-08-30, unrun

**The second and last instance of the film's clock.** Pairs with `1y`; the two are the device and
neither is worth anything alone.

#### 🔴 This is a REFERENCE job, not a restatement — and that is a change of method from `1a`/`4a`

`4a` was made by re-firing `1a`'s text with the tower swapped, matching by identical wording. **We
are not doing that here.** Jack supplied the accepted plate as a reference, and the house finding
([`nano-banana-2.md` §2/§19](../../google-flow/nano-banana-2.md)) is that **you do not restate what
a reference already shows** — restating it is what let a stale reference beat the prompt in
`11b(i)` round 3. So the prompt below names the reference's role, then spends itself almost
entirely on **the two deltas**.

🔴 **The known risk this runs into is [§21](../../google-flow/nano-banana-2.md): *a multi-part
change to one object loses outright to a reference showing it intact.*** The numerals *are* one
object and they *are* the change, so the reference actively argues for keeping `2008`. Two
mitigations are built in: **the reference's role is declared as location-only**, and the new
numerals are stated **early, positively, and with the old value explicitly negated.**

#### What changes, and it is exactly two things

**1. The numerals read `2026`.** Same size, same position, same material, same laying.
⚠️ **The risky glyph has moved from the `8` to the `6`** — a closed loop with an open tail is
where weed digits fail. It is named as a failure in the prompt, the same pattern as `4b`.

**2. Eighteen years of rubbish have washed up — and it is threaded *through* the weed, not piled
on it.**

🔑 **The decision that matters, and why the obvious bolder version was not taken.** The tempting
image is *the 2026 digits made of plastic instead of weed* — the river still writing, with nothing
left to write with. It is a better single picture and a worse **clock**: the device's engine is
*same frame, one thing changed*, and swapping the material makes the eye read **a different thing**
rather than **the same thing, later**. So the weed stays, and the plastic is tangled into it: at a
glance it is the same black writing, close up it is half refuse. The argument survives, the match
survives.

⬜ **The bold version is still on the table** if Jack wants it — it is one clause, and it would be
the film's most quotable frame. It just stops being a timestamp.

**Gate 2 is where this shot gets its cost**, and it is literal: the tide line *is* the visible
cost. ⚠️ **Restraint is the risk** — *one clean subject beats three ambiguous ones*
([`symptoms.md`](../../cinematography/symptoms.md)), and a foreshore turned into a landfill
cartoon loses the digits. **One hero object: the overturned trolley among the stumps** — which
quietly rhymes with the Waitrose car park and its trolley shelter. Unbranded, because a readable
fascia here would be both a gibberish-text risk and too cute; the car park owns that joke.

#### 🔒 What must NOT change, and one of them is counter-intuitive

- **The far bank stays exactly as it is.** No new towers, no glass spire, no cranes. Ruled: **the
  skyline change is `1a` → `4a`'s job** and this pair must not compete with it. Change the
  background and the eye reads *different place* instead of *same place, later*, and the claim —
  **the river did not change, and it kept the receipt** — collapses.
- **Same camera height and angle, same framing.** Copy it off the plate, not off the round-2
  prompt that was never run.
- **Same tide state, same shallow sheet of water over the ribbed mud.**
- **Same flat overcast, no sun, no shadows.** Any light change reads as a different day and kills
  the match.

```prompt
SCENE:

Generate a hyper-realistic documentary photograph on 35mm colour negative — fine natural grain, muted and cool, real atmospheric haze, slightly uneven exposure. Naturalistic motivated light only. No lens flare, no glow, no bloom, no halo.

The attached image is the reference for the location, the camera position, the framing and the light, and for nothing else. Reproduce all of that exactly: the same tidal river foreshore at the same state of tide, the same camera height and steep downward angle, the same broken row of rotted black timber jetty stumps, the same far bank with the same buildings standing on it, the same cobbles, brick rubble, mooring ring and rusted iron handrail crossing the bottom of the frame, the same flat white overcast with no sun and no shadows, and the same shallow sheet of water lying over the ribbed grey-brown mud. Nothing about the place itself has changed.

Two things are different, and only these two.

First, the numerals. They read 2 0 2 6. They do not read 2008. They are the same size and in the same position, laid across the middle of the frame the same way, and made of the same matted green-black river weed. Each numeral is one continuous unbroken band of even thickness so its shape is closed and reads instantly: the zero is a closed ring, the two twos match each other, and the six is a closed loop with one clear open tail curving up out of it.

Second, eighteen years of rubbish have washed up. The weed forming the numerals is threaded through with plastic — grey wet wipes matted into the strands, a length of frayed blue rope, filaments of torn netting, a flattened bottle — so at a glance the numerals still read as dark weed writing, and close up they are half refuse. More of it lies scattered on the mud around them and gathered along the tide line among the jetty stumps: dirty plastic bottles, torn bags, a traffic cone on its side. A shopping trolley lies overturned in the shallow water among the stumps, rusted and half sunk into the mud.

Constraints: the numerals stay dark against the pale reflective mud and stay completely legible — the rubbish is threaded through the weed, never piled over the shapes and never breaking a stroke. No people, no boats, no birds and no vehicles. No brand marks, logos, labels or readable lettering on the trolley, the bottles, the cone or anywhere else in the frame; every printed surface is worn blank, and the trolley carries no supermarket name. The buildings on the far bank are exactly as in the reference — no new towers, no tapering glass spire, no cranes. Nothing glows and nothing is lit from within; the wet mud is the brightest thing in the picture.

Compose for a 16:9 frame.

Thanks.
```

#### What to check before accepting — and the first check is the whole point

1. 🔴 **Put `1y` and `4y` side by side.** If the far bank, the stumps, the handrail, the cobbles or
   the horizon have moved, **the device has failed**, whatever the digits look like. That is the
   only test that matters.
2. **`2026`, not `2008`** — §21 says the reference will argue for the old value. Check it first.
3. **The `6` at 100%.** Closed loop, clear tail, tail not fused back into the loop.
4. **The digits still read dark and clean** — rubbish threaded through, no stroke broken.
5. **No lettering anywhere**, especially the trolley and the bottles.

**If accepted → the clip.** Omni Flash, **Frames**, this still as the start frame, end slot empty,
camera locked. 🔑 **The motion is the rhyme, and it inverts:** `1y` has the tide **coming in**,
about to take the year. `4y` should have it **going out** — the water draining off the mud and
leaving the digits and the rubbish behind, uncovered. The river took 2008 away; it has finished
with 2026 and left it lying there.


### 4y — round 1 · ✅ **ACCEPTED** (Jack, 2026-08-30) · 🔒 the pair is closed

🖼 **Master banked:** [`camera/reference/4y-foreshore-2026-ACCEPTED.png`](./camera/reference/4y-foreshore-2026-ACCEPTED.png).

**The test that mattered passed.** Side by side with `1y` the far bank is the same — same pale
tower left of centre, same brick wall and its buildings right — and so are the jetty stumps, the
cobbles, the mooring ring, the handrail across the bottom, the horizon, the overcast and the water
level. 🔑 **The eye reads one place, twice.** That is the whole device, and it is now built.

- ✅ **`2026`, not `2026`-shaped-`2008`.** §21's warning — the reference arguing for the old value
  — did not bite. Declaring the reference **location-only** and negating `2008` explicitly appears
  to be what did it; **reuse that shape whenever a reference has to be overruled on one element.**
- ✅ **The `6` closed**, loop and tail both.
- ✅ **The trolley landed** and is the frame's hero object exactly as designed — half sunk among
  the stumps, unbranded, reading instantly.
- ✅ **The blue rope threads *through* the digits** rather than over them; no stroke is broken.
- ✅ No lettering, no people, no boats, no birds.

⚠️ **The rubbish over-delivered slightly** — two traffic cones rather than one, and the near
foreground is busier than `1y`'s. **Not a defect:** the busier frame *is* the eighteen-year delta,
and the digits still win the frame on contrast. Recorded only because it is the thing to trim
first if a future version of this pair feels cluttered.

### 4y — the tide going out · **video** · written 2026-08-30, unrun

**Routing:** identical to `1y` — Omni Flash → **Frames**, the accepted `4y` master as start frame,
**end slot empty**, 10s, camera locked.

#### 🔑 The motion inverts, and that inversion is the argument

`1y` has the tide **coming in**, about to take the year. **`4y` has it going out.** The water
drains off the mud and leaves the digits and the rubbish lying uncovered.

- **2008 is being taken away.** The past going under, while you watch.
- **2026 is being laid bare.** The river has finished with it and left it there. **The tide gave
  the year back, and this is what came with it.**
- It is also what an ebbing Thames physically does, so the whole beat is motivated and needs no
  invention.

⚠️ **`4y` should feel deader than `1y`, not livelier.** Advancing water is active and threatening;
draining water is abandonment. That governs every small decision below — **when in doubt here,
take life out of the frame, not add it.**

**Consequently, and deliberately:**

- ⬜ **No stirring plastic bag, no flapping sheet.** It was considered and cut. Same call as `1y`'s
  gull: one physical system per clip, and here the second system would have added *life* to the
  shot that most needs to lack it.
- 🔑 **No gull in the audio either — and that is the point.** `1y` has one calling off screen.
  `4y` has no bird at all. Nobody will notice consciously, and that is the correct amount of
  noticing. In its place, **a low distant mechanical hum** — deliberately ambiguous between traffic
  and something else, ⬜ and available to be sharpened into a drone if Jack wants the scene-11
  reveal quietly planted this early. Left ambiguous by default because on-the-nose is the failure
  mode there.
- **The one detail that does move besides the water: the trolley.** As the level falls, more of it
  comes clear. 🔑 **The gate-2 cost being *revealed* by the motion** rather than just sitting in
  frame — the best thing in the shot, and it costs nothing because it is the same physical event.

#### 🔴 The anti-slop risks that are NEW here, versus `1y`

`1y`'s table still applies. These are the ones this frame adds:

| The risk | Why it is new | The clause |
| --- | --- | --- |
| 🔴 **More objects = more things to morph.** Cones, bottles, bags, rope, sheeting | `1y` had bare mud; every added object is a chance for the model to reshape or drift it across 240 frames | **All the debris is named as static and told to stay exactly where it is.** This is the single most important line in the prompt after the numerals |
| 🔴 **The trolley is a wire mesh grid** | Two named artefact classes at once — repeating texture tiling *and* thin-structure mangling, which models handle badly | It **does not move**; only the water level around it changes. Never ask the mesh to do anything |
| ⚠️ **More printable surfaces** — bottles, bags, cone | `[confirmed 2026-08-17, Karen §2j.6sv]`: a clip block that never mentioned signage grew writing on a sign. More surfaces, more vacuum to fill | **Every printed surface stays worn blank**, restated in the clip block and not left to the plate |
| **Larger area of moving water** | Reflection breakdown is a named tell | Ask only for the **diffuse sky** shifting. Never an object's reflection |

**Primary:**

```prompt
The attached image is the locked opening frame.

One continuous shot, no cuts. The camera is locked off on a tripod and does not move at all — no push, no pull, no pan, no tilt, no drift, no reframe. Shot on 35mm at 24 frames per second with a 180-degree shutter, fine natural grain, muted and cool and desaturated.

The tide is going out. Through the whole shot the thin sheet of water lying over the mud drains slowly away toward the river, its edge retreating unevenly, finding the ribs and hollows and leaving them wet and glistening as it uncovers them. Around the sunken shopping trolley the level falls a little and more of the trolley comes clear of the water. The pale sky reflected in the wet mud shifts slowly as the surface drains.

The four weed numerals are solid objects lying on the ground. They do not move, do not shift and do not change shape. All the rubbish — the traffic cones, the bottles, the bags, the rope, the sheeting and the trolley — lies completely still and stays exactly where it is. Nothing else in the frame moves.

Constraints: no people, no boats, no birds and no vehicles. No text, writing, logos or labels of any kind — every printed surface stays worn blank. Nothing glows and nothing is lit from within; the wet mud is the brightest thing in the picture. No lens flare, no bloom.

Audio: water draining and trickling away through mud and shingle, cold wind across open ground, and a low distant mechanical hum. No birds, no music, no voices and no dialogue.

Thanks.
```

**Fallback, ~55 words:**

```prompt
The attached image is the locked opening frame. One continuous shot, no cuts, camera locked off, no camera movement of any kind. The tide goes out: the thin sheet of water drains slowly off the mud toward the river and uncovers it, and more of the sunken trolley comes clear. The weed numerals and all the rubbish stay completely still. 35mm, 24fps, fine grain. Audio: draining water, wind, a low distant hum. No birds, no music, no voices.

Thanks.
```

🔴 **Fire whichever length worked for `1y`.** The two clips are a pair and were generated from the
same plate lineage; a long prompt on one and a short prompt on the other introduces a variable the
pair cannot afford. This is also the second half of the
[prompt-length experiment](../../google-flow/omni-flash.md) — **record which one produced each
accepted clip.**

#### Check before accepting

1. 🔴 **Numerals at 100% on the LAST frame as well as the first.** Reflow across 240 frames is the
   risk, exactly as in `1y`.
2. 🔴 **Did any of the rubbish move, drift or change shape?** New risk, and the likeliest one here.
   Watch the cones and the trolley mesh specifically.
3. Camera stayed put? Did it cut? → fallback prompt, not a rewrite.
4. Is the retreating water edge ragged? A straight line is the floaty-motion tell in costume.
5. Nothing crawled onto a surface — bottles, bags, cone, far wall.

#### 🔴 The post pass, and the one decision it forces

⬜ **Premiere: the same slow push in as `1y`, identically.** ⚠️ **Whatever camera move `1y` gets,
`4y` gets** — the device is a clock, and a clock that behaves the same way twice is what makes it
read as one. The content already changed; the grammar must not.

⬜ **The tempting alternative, and the recommendation against it.** `4y` could **pull out** instead
— widening to take in the rubbish, where `1y` pushes in to the year. It maps beautifully onto what
each shot's information actually is. **Do not do it.** It breaks the grammar that makes the two
frames read as one device, and it leaves `4y` ending wide, which is a weak button on the shot that
opens the film's second act. *Recorded because it is a good idea and someone will have it again.*


### 1b — the trading floor · **still** · accepted

**Recovered 2026-08-26.** Two things in this prompt are ahead of canon — see the notes
under it.

The era is carried by the *stock*, not by a date: Superia 400 pushed a stop, with the green
fluorescent bias called for explicitly. Faces are solved the way the standing rule says to —
**every person is turned away or in lost profile and no face is legible anywhere**, so the
engine is never asked to hold twenty likenesses. The `Constraints:` block is doing real work:
it re-states the windowless interior and the turned-away crowd as hard rules after they have
already been described, which is the belt-and-braces pattern for the things that break.

```prompt
SCENE:

Hyper-realistic documentary photograph, shot on 35mm Fujicolor Superia 400 pushed one stop — fine natural grain, a green bias off the fluorescent light, muted and cool. Naturalistic motivated lighting only, no lens flares, calm observational tone. The photographer is standing at the end of an aisle in a working office and has not been noticed.

Subject: A deep open-plan trading floor in the City of London, 2008, seen down the length of it. Long unbroken rows of desks running away from the camera into the far end of the room, banks of slim flat-panel LCD monitors on articulated steel arms four and six to a desk, thin dark plastic bezels, all carrying dense rows of figures in amber and green on black. Perhaps twenty people at the desks in white shirtsleeves, jackets slung over chair backs, ties loosened — roughly a third of them women, and the floor visibly mixed across Black, South Asian, East Asian, Middle Eastern and white, of a range of ages and builds, spread evenly through both rows rather than grouped together — every one of them seen from behind or in lost profile, hunched toward their screens, none facing the camera and no face legible anywhere in the frame.

Action: Ordinary working chaos rather than drama. One man stands with a phone handset to his ear. Another leans across to a colleague's desk. Far down the row, small in the frame and well off to one side, one person has tipped their chair back and is holding an open broadsheet newspaper up in front of them, the paper hiding their face completely; a chair back and a monitor arm partly cross in front of them, and the front page is turned only half toward the camera. The headline is small but still readable in heavy black sans-serif capitals: "CRISIS ON WALL STREET". No masthead, brand or other lettering on the page is legible — only that one line. It is easy to miss and nobody in the room is looking at it. Nobody is celebrating and nobody is panicking.

Environment: Curling Post-it notes stuck to monitor bezels, loose printouts heaped and spilling, abandoned coffee cups, a suit jacket fallen half off a chair, cardboard boxes shoved under a desk. A grid of fluorescent tubes fills the ceiling, and the floor stretches back further than the light does.

Camera and framing: 35mm lens at f/2.8, held at standing chest height, the aisle running away slightly off-centre so the room falls to the right rather than sitting square. The near edge of a monitor and a chair back cut into the foreground on the left, dark and completely out of focus. Focus sits on the desks in the near-middle distance and the far end of the room softens away. The frame is very slightly tilted.

Light: Only what is in the room — the hard fluorescent ceiling grid, flat and green, blowing out to pure white in the tubes themselves, and the cold spill of the screens across the desktops. The undersides of the desks go to crushed black. Uneven exposure, a few blown highlights, no fill light anywhere.

Constraints: this is a windowless interior — every wall and ceiling is solid, and the only light in the room comes from the ceiling tubes and the monitors. Every person is turned away from the camera and the newspaper reader's face stays hidden behind the paper. Keep it plain and unglamorous, the way an ordinary press photograph of an office actually looks.

Compose for a 16:9 frame.

Thanks.
```

> ### 📌 Two things this prompt settles that canon still lists as open
>
> **1. ✅ The newspaper plant lives in 1b. 1d no longer exists** *(ruled 2026-08-26)*. The
> shot list used to carry the plant as its own shot, **1d**. In the frame that was actually
> made it is *inside the trading floor*: far down the row, small, half-turned, one chair back
> and a monitor arm crossing it. That is the better plant — **a shot that exists only to plant
> announces itself**, and a plant the audience notices has failed. 1b absorbed it; the film is
> one shot shorter.
>
> **2. The 2008 headline is decided: `CRISIS ON WALL STREET`.** Canon's *Still open* list has
> "the 2008 headline on the planted newspaper" as undecided. It isn't any more — heavy black
> sans-serif capitals, no masthead, nothing else on the page legible.

---

### 1c — young Tarquin mid-deal · **still** · accepted

**Recovered 2026-08-26.** Cast with the **`@Tarquin-2008` Flow Character** — which does exist,
correcting the 2026-08-25 note in [`characters/tarquin.md`](./characters/tarquin.md).

Same stock and same room as [1b](#1b--the-trading-floor--still--accepted) — Superia 400 pushed
a stop, the green fluorescent bias, the identical `Constraints:` block. That is what makes the
two frames cut together.

> ### 🎯 The lesson worth keeping: describe the face only to *fight* the Character
>
> 1c has a Character attached **and** a long face description, which looks like a contradiction
> until you read which way it points. Every clause is aimed at one job — **age him down hard**:
> no nasolabial lines, no hollow cheekbones, no soft jaw, no temple recession, a full low
> hairline, the unformed fullness of a young man. The description is not re-specifying the face,
> it is **overriding the Character's default age in a named direction**.
>
> The inverse is the 4b problem: describing his face there had no direction to pull in, so it
> just added drift, and he came back older than he should be. **Rule: attach the Character and
> say nothing about the face — unless you are pushing it somewhere it will not go on its own,
> and then say exactly which way.**
>
> Note the anti-CGI details doing the other half of the work: individual eyebrow hairs, razor
> burn along the jaw, redness at the nostrils, matte not gloss, *"one eye fractionally smaller,
> the nose not quite straight"*. Deliberate asymmetry is the single cheapest defence against
> the rendered look.

```prompt
SCENE:

Hyper-realistic documentary photograph, shot on 35mm Fujicolor Superia 400 pushed one stop — fine natural grain, a green bias off the fluorescent light, muted and cool. Naturalistic motivated lighting only, no lens flares, calm observational tone. The photographer is standing in the aisle of a working office and has not been noticed.

Subject: The young man in the reference image, twenty-five years old, in a white shirt with the sleeves shoved up past his elbows, the collar open, and a wide tie in broad diagonal orange and blue stripes pulled loose and hanging off to one side. His suit jacket is slung over the back of the chair behind him. Age him down hard — he is twenty-five: no lines from nose to mouth, no hollowing under the cheekbones, no softening under the jaw, no recession at the temples. The hairline is full and low, the forehead smooth, the jawline clean, and the cheeks still carry the slightly unformed fullness of a young man rather than an adult's hard planes. Slim, but not gaunt. Real skin under hard office light — visible pores, individual eyebrow hairs, faint razor burn along the jaw, uneven tone with redness at the nostrils, a matte sheen rather than gloss. His face is naturally asymmetric: one eye fractionally smaller, the nose not quite straight.

Action: He is half out of his seat, his weight going down through one splayed hand on the desk, a phone handset wedged between his shoulder and his ear, talking into it. His other hand holds a printout down at his side, slightly blurred by its own movement. His mouth is closed, his chin lifted, his brows level and relaxed, his eyes narrowed slightly and aimed at one screen, one corner of the mouth pulled back and held there. The face is doing very little. Unposed, caught mid-gesture, unaware of the camera.

Environment: A deep open-plan trading floor, 2008. Banks of slim flat-panel LCD monitors on articulated steel arms, four and six to a desk, thin dark plastic bezels, carrying dense rows of figures in amber and green on black. The desk in front of him is a mess — curling Post-it notes stuck to the bezels, loose printouts shoved into a heap, a cold coffee. Behind him the row of desks runs away into the room as backs, shoulders and the tops of chairs, all soft and unreadable.

Camera and framing: 50mm lens at f/2, from just below his eye height and slightly off to one side. He sits left of centre with empty room to his right, and the near edge of a monitor cuts into the foreground on the left, dark and completely out of focus, eating the left quarter of the frame. Focus sits on his eyes and everything nearer and further falls away fast. The frame is very slightly tilted.

Light: Only what is in the room — a hard fluorescent ceiling grid, flat and green, blowing out to pure white in the tubes themselves, and the cold wash off the screens onto his face and throat from below. The undersides of the desks go to crushed black. Uneven exposure, a few blown highlights, no fill light anywhere.

Constraints: this is a windowless interior — every wall and ceiling is solid, and the only light in the room comes from the ceiling tubes and the monitors. His mouth stays closed throughout. Keep it plain and unglamorous, the way an ordinary press photograph of an office actually looks.

Compose for a 16:9 frame.

Thanks.
```

**Character attached:** `@Tarquin-2008`. Note the prose still says *"the young man in the
reference image"* and never names him — the Character is the attachment, the prose stays
anonymous. That is the convention working as intended, not a contradiction of it.

---

## Scene 1 montage — the 80s job montage *(2026-09-11)*

**Why it exists.** Jack, 2026-09-11, on 1b and 1c: *"these parts look ai-slop like and not
interesting cinematically."* Design and shot list are in
[`shot-list.md`](./shot-list.md#1m--the-80s-job-montage-2026-09-11-proposed). Diagnosis, read off
the two frames (the cause is inferred, not tested):

- 🔴 **The light could never have been hard.** Both prompts ask for *hard* fluorescent light with
  *crushed black* under the desks, but a ceiling full of tubes is one huge soft source. The
  physics doesn't allow a hard light there, so the engine closed it the other way: shadowless,
  even, mid-grey
  ([`nano-banana-2.md` §20](../../google-flow/nano-banana-2.md)). Writing it harder won't
  change that. **Only a different light source will.**
- **1b is a one-point corridor with the vanishing point in the middle**: rows of near-identical
  white shirts in the same pose. That's the symmetry-and-cloning bundle
  ([`symptoms.md`](../../cinematography/symptoms.md) A, *"it looks like AI"*).
- **1c is a stock-photo archetype** (a man on the phone, leaning on a desk). Nothing is withheld
  and there's no unresolved question ([`stills.md`](../../cinematography/stills.md) §1). He also
  reads mid-thirties rather than twenty-five.

**The montage register: direct on-camera flash, shutter dragged.** One hard source that exists
in the world (the photographer's flash) answers gate 3. It falls away with distance, so
foreground and background separate on their own. It freezes the subject while anything moving
ghosts, which gives motion inside a still. Kept on Superia 400 so it can still cut against 1b/1c.
`[untested]`

### 1m-e — the box · **still** · written 2026-09-11, unrun

Model **Nano Banana Pro**. Cast **`@Tarquin-2008`**. **No reference image**: attaching 1b or 1c
would bring back the flat light this frame exists to fix, because a strong reference wins ties
([`nano-banana-2.md` §9](../../google-flow/nano-banana-2.md)). Tarquin's appearance isn't
described at all (the standing rule). The box man is unbound, so he *is* described
([§25](../../google-flow/nano-banana-2.md)).

```prompt
SCENE:

This is one frame of a fast-cut montage: six photographs of the same young trader across one day on a City of London trading floor in September 2008, the week the banks started failing. In this frame he is making money and the man behind him has just lost his job, and neither of them is looking at the other.

Camera: a 35mm lens at seated eye height, level, about two and a half metres from the trader, the frame very slightly tilted. Nearest the lens, the back of an empty office chair crosses the bottom-left corner, dark and thrown completely out of focus.

Subject: the man from the character reference, in the right half of the frame, seen from the knees up in three-quarter profile, turned toward a monitor just outside the right edge of the picture. He has tipped his chair back onto its two rear legs and is balancing there, one shoe lifting off the floor on its way up onto the edge of the desk, a telephone handset clamped between his shoulder and his ear, one hand braced flat on the desk to hold his balance. His eyes are aimed at that monitor, his lower eyelids pushed up slightly, his brows level. One corner of his mouth has pulled back and up and is holding there; his lips are closed. The expression is small.

Behind him: the left half of the frame is the aisle, running away at a diagonal from the bottom-left toward the middle of the room. Four metres back along it, softer than the trader, a heavy-set man in his fifties walks away from the camera mid-stride, carrying a cardboard archive box in both arms. He is seen squarely from behind: the back of his head faces the lens and hides the rest of it, grey hair thinning at the crown, a creased white shirt coming untucked at the back, his suit jacket folded over the top of the box. The leaves of a desk plant, the corner of a picture frame and the handle of a mug stick up out of the box. Beyond him, rows of desks and monitors fade into the far end of the room.

Light: a flash on top of the camera is the only strong light. It hits the trader hard from the front, puts a shine on his forehead and cheekbones and a hard-edged shadow under his jaw. It falls away fast with distance, so the man with the box is noticeably darker than the trader and the far room darker again, lit only by a dim green wash from the ceiling fluorescents and the cold glow of the screens. The shutter stayed open after the flash fired, so the walking man carries a faint blurred ghost of his own movement while the trader is frozen sharp.

Style: a press photograph for a newspaper feature, shot on 35mm Fujicolor Superia 400 — visible grain in the shadows, muted cool colour, a green cast in the background from the tubes. The desks are cluttered with printouts, curling Post-it notes and cold coffee.

Constraints: the man with the box is seen only from behind. The box, the monitors and every piece of paper carry no readable lettering.

Compose for a 16:9 frame.

Thanks.
```

**If the box man grows a face,** don't add another sentence. Take his head out of the frame and
keep the shoulders and the box ([§18](../../google-flow/nano-banana-2.md)).

### 1m-e — round 1, **not accepted** (Jack, 2026-09-11: *"it looks strange"*)

- **The box man worked.** The back of his head hid his face, per §18. Keep that pattern.
- 🔴 **The flash came back as a lamp** blowing out in the top-right corner, and the rest of the
  room was evenly lit again. The Light paragraph named the flash as an object, so it was drawn as
  one.
- **The pose broke.** Tipped on two chair legs, a foot lifting and a hand braced are three
  balance facts at once, and they came back as a half-sit on nothing.
- **He read mid-thirties again, in a full grey suit.** That's the second time `@Tarquin-2008` has
  come back too old (1c was the first). Jack: *"forget the reference image."*
- **Every monitor came back blank black.** The inferred cause is that *"monitors carry no
  readable lettering"* was satisfied by switching them off. Give screens content that is too
  small or too blurred to read instead.

### 1m-2 — "Tarquin here," the intro · **still** · ✅ **ACCEPTED 2026-09-11, round 1** (Jack: *"i like these three"*)

**What landed:** it's caught mid-action, the flash reads as a hard light on him with the room
falling to green, and the traders behind him are ghosted by motion blur. He reads late
twenties, which is close enough. **What it changed:** the biro cap came back as a whole second
biro in his teeth (funnier, kept), and the hair came back tousled rather than slicked, so check
it against 4b. ⬜ Master not banked in `camera/reference/`.

**Nano Banana Pro. No Character, no reference image**, so young Tarquin is described in full;
the never-describe rule only applies when something is attached. **This frame becomes the face
reference for every later montage frame.** The flash is now named as **camera hardware** in the
Style line and as **consequences** in the Light line, never as an object in the room. The one
deliberate change from house stock: a 2008 press DSLR instead of Superia film, because flash
snapshots of 2008 were digital. `[untested]`

```prompt
SCENE:

This is one frame of a fast-cut 1980s-style montage about a young City of London trader in September 2008, the week the banks began to fail. This frame introduces him: loud, busy and completely at home in the chaos.

Camera: a 35mm lens at the height of his chest, level, about a metre and a half from him, the frame very slightly tilted. The top of the frame cuts off just above his head. Nearest the lens, the edge of a monitor crosses the left side of the frame, dark and thrown completely out of focus.

Subject: a twenty-five-year-old white British man, lean, with thick dark hair slicked straight back with too much product and one strand come loose over his forehead. A narrow young face that has not filled out yet, a slightly crooked nose, one eye fractionally smaller than the other, faint razor burn along the jaw, redness at the nostrils, visible pores and a little shine across the forehead. A white shirt with the sleeves shoved above the elbows and damp patches under the arms, the collar open, and a wide tie in loud diagonal orange and blue stripes flipped back over his shoulder out of the way.

Action: he stands leaning forward over his desk with a telephone handset clamped between his shoulder and his ear, talking round the cap of a biro clenched in his teeth. His right arm is thrust out across the frame, the biro jabbing at a screen just outside the right edge. His eyes are locked on that screen, wide open, the whites showing above the irises, the brows raised and drawn together at the inner ends. One corner of his mouth is pulled up around the pen cap.

Behind him: the trading floor in the middle of a frantic morning. Other traders stand at their desks with phones and papers, some with an arm in the air, every one of them streaked sideways by motion blur so that no face behind him can be read. The monitors on every desk are switched on and glowing, packed with columns of tiny red and green figures far too small and soft to read.

Light: the photograph was taken with a flash on top of the camera, fired straight at him. He is the brightest thing in the picture — the flash lays a flat, hard light across his face and shirt and a crisp dark shadow on the desk under his arm. It does not reach far, so the room behind him drops away into a dim green wash from the office fluorescents, and the shutter stayed open long enough that everyone moving back there has smeared into ghosts while he is frozen sharp.

Style: a newspaper photograph of the 2008 financial crisis, shot on a Canon EOS-1D Mark III with a Speedlite — digital noise in the shadows, muted cool colour, a green cast from the tubes, harsh and unflattering. His desk is a mess: printouts, curling Post-it notes, a half-eaten sandwich in its cardboard packet, a cold coffee.

Constraints: the only light sources are the camera's flash, which is behind the lens, and the ceiling fluorescents, which are above the top edge of the frame. Every screen, paper and label carries no readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### 1m-7 — the house · **still** · ✅ **ACCEPTED 2026-09-11, round 1**

🔴 **Post job owed:** the rear number plate is readable. Blur it in Premiere. The standing lamp
came back as an ambiguous cone; at montage length it doesn't matter.

**The one cutaway, and the pattern break:** daylight, no flash, no Tarquin. It sits under
*"Some twat is going to lose a house over this trade, and I am never going to meet them."*
**He never meets them; the audience does.** Nobody from the family is in frame, and their things
are packed with care. [`the-reader.md`](../../marketing/the-reader.md) rule 1 applies: they are
people who were wronged, not squalor. The locksmith is hidden by geometry (§18). No marques, no
boards, no numbers. The same camera body as the rest of the montage keeps it one piece.

### 1m-8 — "That is good business." the empty floor · **still** · ✅ **ACCEPTED 2026-09-11, round 1**

It came back centred and symmetrical rather than angled. That works as the montage's full
stop, so it's kept.

**The button.** Everyone else has gone, some of them for good. He is a **silhouette against his
own screens**, so no face is needed and no reference either (the too-small-to-bind exception).
There is one bright anchor, which is his desk, and the rest is committed near-black. The empty
rows are the visible cost. The long lens stacks the rows, and the room runs off at an angle,
because a centred corridor was 1b's tell.

**Research notes (2026-09-11, `[community]`, untested):**
- *"Exposed for the glow"* plus a stated shadow fraction (*"four-fifths falls to black"*) is
  vendor-blog advice for real darkness.
- British settings drifting American is documented on Firefly, not on Google. The prompt names
  UK materials and says *British* explicitly anyway.
- Photographer names are avoided. Google's guide says to describe the style instead.

**1m-7**
```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008. It is the only frame that leaves the trading floor: the house of people who are losing it because of his trade, people he will never meet. The only person in the picture is a locksmith.

Camera: a 50mm lens at standing eye height, level, from the pavement on the opposite side of a quiet residential street in a town in the north of England, about twelve metres from the house. Nearest the lens, the rear corner of a parked car crosses the bottom-left of the frame, dark and thrown completely out of focus. The neighbouring houses are cut off by both edges of the frame, and the top of the frame cuts across the roofline, leaving only a thin strip of white sky.

Subject: the front of an ordinary British 1950s semi-detached house, its front door right of centre. Grey pebbledash render with dark rain streaks under the window sills, a white uPVC front door and white uPVC windows with net curtains, a satellite dish bolted to the wall, a low brick garden wall with a gap for the drive, weeds pushing up through cracks in the concrete drive, a green wheelie bin by the side gate.

Action: a locksmith kneels on the front step with his back square to the camera, his head bowed over the lock as he drills it out, an open toolbag beside his knee. The back of his head faces the lens and hides his face. On the drive, lined up neatly against the garden wall, are the household's belongings: black bin bags knotted at the top, a stack of cardboard boxes taped shut, a rolled-up duvet tied with string, a standard lamp laid on its side, and a child's small bike with stabilisers. Everything has been packed with care.

Light: a flat grey overcast sky at late morning is the only light. It comes from above, leaving soft shadow under the eaves, under the window sills and beneath the car, and no hard shadows anywhere. The ground is dry and the air is still.

Style: a newspaper photograph taken on a Canon EOS-1D Mark III by available light, with no flash — fine digital noise, muted cool colour, slightly underexposed, the white front door the brightest thing in the frame.

Constraints: the locksmith is seen only from behind. House numbers, number plates, signs and labels carry no readable lettering. Every house, car and piece of street furniture is British.

Compose for a 16:9 frame.

Thanks.
```

**1m-8**
```prompt
SCENE:

This is the last frame of a fast-cut montage about a young City of London trader in September 2008. It is late at night, everyone else has gone home, and he is the only person left on the trading floor.

Camera: an 85mm lens at standing eye height, from behind him at the far end of a long open-plan trading floor, looking along the rows at a slight angle so the room recedes toward the right rather than straight down the middle. The long lens stacks the empty rows of desks tightly one behind another. Nearest the lens, filling the bottom-left corner: the back of an empty office chair pushed in under a cleared desk, and a cardboard box taped shut on the desktop, dark and thrown completely out of focus.

Subject: well down the room, right of centre and small in the frame, one desk is still lit. The young man sits alone at it with his back to us, leaning back in his chair with his feet up on the desk and his hands laced behind his head. He is a dark silhouette against the bank of glowing monitors in front of him, the glow outlining his slicked-back hair, his shoulders and the soles of his shoes.

Around him: rows of empty desks with their monitors switched off, chairs pushed in, a suit jacket left over one chair back, cardboard boxes on several cleared desks.

Light: the only light on the floor is his own bank of monitors, a cold blue-white glow that outlines him, spills across his desk and dies within a couple of metres. The ceiling lights are off. The photograph is exposed for that glow, so roughly four-fifths of the frame falls to black: the dead screens of the empty rows catch only faint reflections of his, and the tops of the chair backs and boxes only just separate from the dark.

Style: a newspaper photograph taken on a Canon EOS-1D Mark III by available light, with no flash, at ISO 3200 — coarse digital noise in the shadows, muted cool colour, deep underexposure everywhere except his desk.

Constraints: his monitors are the only light source in the picture. Every screen carries no readable lettering.

Compose for a 16:9 frame.

Thanks.
```

---

## Scene 1 montage — the three added frames *(2026-09-12)*

**Jack's ask:** *"we need more videos of 2008 tarquin… using the character `@2008 - tarquin` for all of them."*
Design, costs and the running order: [`shot-list.md`](./shot-list.md#the-three-added-frames-2026-09-12-jacks-ask--more-videos-of-2008-tarquin).
Run **one at a time** in the order below; each clip only after its still is accepted.

**Model: Nano Banana Pro.** 🔴 **Not "Nano Banana Pro 2" — it does not exist**
([§fifth pass](../../google-flow/nano-banana-2.md#-there-is-no-nano-banana-pro-2-vendor-community)), and
**check Flow's picker before starting**: `[community]` reporting says it has defaulted to **Nano Banana 2
Lite** since July 2026, so a session can be on Lite without anyone choosing it.

**Cast `@2008 - tarquin`. No reference image** — one authority on the face
([§3b](../../google-flow/nano-banana-2.md#3b--role-labels-do-not-make-a-second-reference-free--house-rule-one-reference),
[§12](../../google-flow/nano-banana-2.md#12--a-character-binds-to-a-face-no-face-in-the-shot-no-likeness-observed)).
Attaching the accepted `1m-2` frame **as well** would put two authorities on one face, which is the
documented drift source.

### What these three do differently from `1m-e`, which failed

| `1m-e` round 1 did | These do |
| --- | --- |
| Named the flash as an object in the Light paragraph → **drew a lamp** | Flash named as **camera hardware** in Style, **consequences only** in Light, source positions pinned in `Constraints:` ([§35](../../google-flow/nano-banana-2.md#35--a-flash-described-as-an-object-in-the-room-is-drawn-as-a-lamp-observed-2026-09-11-n1)) |
| *"The monitors carry no readable lettering"* → **switched every screen off** | Screens are **on** and carry content **too small and soft to read** |
| Three balance facts at once → **a half-sit on nothing** | One physical action per frame, mid-travel |
| `@Tarquin-2008` → **mid-thirties, twice** | One age-down clause naming the direction only, **restated in `Constraints:`** — the 1c pattern |

### 🔬 What the 2026-09-12 web pass changed in the wording

Full graded findings: [`nano-banana-2.md` §sixth web pass](../../google-flow/nano-banana-2.md#sixth-web-pass--2026-09-12-research-practitioner-vendor).
Four landed in these prompts:

- ✅ **Period accuracy is a factual constraint Google itself sanctions** — their own example is *"ensure
  historical accuracy for the Victorian era"*. Each `Constraints:` block now carries **"Ensure historical
  accuracy for 2008."** 🔴 **And it is a hedge, not a fix:** a `[research]` study measures generators
  inserting modern hardware because they prioritise the *activity* over the era, and finds prompt-level
  mitigation *"insufficient to fully counteract"* it. **Check every screen, handset and monitor on round 1.**
- ✅ **Name both ends of the exposure or the model compensates in the shadows.** The flash frames now grant
  the clipping on his shirt *and* ask the shadows to hold detail; `1m-l` asks for deep shadow that still
  keeps a trace rather than going to solid black — which is also what
  [`delivery.md`](../../video-fx/delivery.md) wants after the `camping.mp4` crush.
- ✅ **Crowd realism is individuation, not adjectives** — state the count, and that no two are alike, and
  what each is doing. `1m-c`'s eight and `1m-l`'s three are both written that way
  ([§22](../../google-flow/nano-banana-2.md#22--tiling-and-cloning-in-crowd-scenes-are-a-resolution-problem-not-only-a-prompt-problem-community-2026-08-28)).
- 🔑 **The 2008 on-camera-flash register is a documented look, and in it a crushed near-black background is
  period-correct rather than a fault** — short flash range, cool blue-green white balance, highlights
  clipping to featureless white, fine digital grain and mild chromatic noise. That is the one place the
  general *"lift the blacks"* realism advice does not apply, and it is worth knowing while
  [principles §R1](../../cinematography/principles.md) is open.

⚠️ **The Portra-400 slop warning does not touch these** — the montage is deliberately a **2008 press DSLR**,
not film, so there is no stock to swap.

⬜ **If offered a resolution, take 2K, not 4K** — generating off native resolution is a named cause of
crowd tiling, and `1m-c` has eight background figures. Flow documents no resolution picker, so this may not
be a choice you get.

### 1m-c — the solo cheer · **still** · written 2026-09-12, unrun

**The job:** he has won, and nobody shares it. **The cost is the room** — everyone seated, heads down, not
one of them looking at him, plus the stripped desk at his elbow.

🔴 **This frame is the montage's highest celebration risk** ([principle 24](../../cinematography/principles.md):
Bateman, *Wolf of Wall Street* — meaning it ironically does not protect us). Three things hold it down: the
cheer is **one fist, mid-travel**, not both arms up; **his eyes never leave the screen**, so he is
celebrating at a number rather than to a room; and `Constraints:` bounds the face from above — *a stranger
would read concentration before they read triumph.*

⚠️ **Known trade:** the background crowd is deliberately **still**, which gives up the cheapest
crowd-realism lever there is (motion blur on background people). Individuation is carrying it instead. If
the eight come back cloned, the fix is more individuation, **not** motion — the stillness is the argument.

**Paste into:** Flow → image prompt box. **Character:** `@2008 - tarquin`. **No reference image.**

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. In this frame he has just won a trade and nobody on the floor is celebrating with him.

Camera: a 35mm lens at the height of his chest, level, about two and a half metres from him, the frame very slightly tilted. He stands in the right third of the picture and the floor runs away behind him to the left, so the left half of the frame is deep room rather than empty space. The top edge of the frame cuts across just above his fist, so the picture is short of headroom. Nearest the lens, the corner of a monitor on a near desk crosses the bottom right, dark and thrown completely out of focus so that it is a soft blur.

Subject: the man from the character reference, seen from the thighs up. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples.

Action: he is standing at his desk at the end of a telephone call. One fist has been driven down past his hip and is still moving; his other hand presses a telephone handset hard against his ear. His shoulders are up, his head pulled back an inch into them, his chin lifted. His eyes stay locked on a monitor just outside the right edge of the frame — lower lids pushed up, the skin tightened at the outer corners, brows drawn down and in. His lips are parted just enough to show the edges of his teeth and his jaw is set. The expression is small, and it is aimed at the screen rather than at the room.

Behind him: the floor has gone quiet. Eight people sit at the desks down the room to the left, no two of them alike — different ages, builds, hair and shirts, some in jackets and some in shirtsleeves. Every one of them is seen from behind or in lost profile, heads down toward their screens; one has a hand flat on the desk, one has a hand over the mouth, one has pushed back from the desk and is staring at the floor. None of them is moving and none of them is looking at him. The desk immediately to his left has been stripped — the monitors gone, two cable tails hanging over the edge, a taped cardboard box squared up on the bare desktop, the chair pushed in.

Environment: printouts trodden flat into the grey carpet tiles, a burst lever-arch file, a mug with a brown ring dried inside it, a desk fan turned to face the wall, a suit jacket fallen off the back of a chair. The monitors are the slim flat panels of 2008 on articulated steel arms, four and six to a desk, with thick dark plastic bezels.

Light: the photograph was taken with a flash on top of the camera, fired straight at him. He is the brightest thing in the picture — a flat hard light across his shirt and the side of his face, and a crisp dark shadow of his arm thrown down onto the desk beside him. The front of his shirt clips to featureless white where the flash hits hardest, while the shadowed side of his face and the desk below him keep their detail rather than going to solid black. The flash does not reach far: four metres back the room is only a dim green wash from the ceiling tubes and the cold glow of the screens, and the far end of the floor falls away to almost nothing. Nobody behind him is moving, so nothing back there is blurred; the only movement in the photograph is his own, and the flash has frozen it.

Style: a newspaper photograph of the 2008 financial crisis, shot on a Canon EOS-1D Mark III with a Speedlite — fine digital noise and mild chromatic noise in the shadows, a cool blue-green cast from the tubes, muted colour, unretouched with no skin smoothing, harsh and unflattering.

Constraints: the only light sources are the camera's flash, which is behind the lens, and the ceiling fluorescent tubes, which are above the top edge of the frame. Every screen is switched on and carries columns of figures far too small and soft to read. Everyone behind him is seen from behind or in lost profile, so his is the only legible face in the picture. He is twenty-five years old. His expression stays small — a stranger looking at this photograph would read concentration before they read triumph. No brand names, logos or readable labels anywhere. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

### 1m-m — champagne in a coffee mug · **still** · written 2026-09-12, unrun

**The job:** he celebrates without looking, and it spills. **The cost is the man one desk away** with his
head in his hands — gate 2's own words, *a body that failed*, and the only one in the montage that is a
person rather than a box or an empty chair.

🔑 **The detail the frame turns on: he is not looking at the mug.** It is why the mug overflows, it is why
the printouts are ruined, and it says what a paragraph of narration would have to. His eyes stay on the
screen.

⚠️ **The bowed man is unbound — no Character, no reference — so he is described in full**
([§25](../../google-flow/nano-banana-2.md#25--19-inverts-for-an-unbound-body-part--describe-it-or-get-young-clean-and-generic-observed-2026-08-29)):
silence there returns young, clean and generic, which is the opposite of the beat. His face is hidden by
**geometry**, never by a sentence ([§18](../../google-flow/nano-banana-2.md#18--their-face-is-not-visible-does-not-hide-a-face-only-geometry-does-confirmed-2026-08-27)).

⚠️ **No marque on the bottle** — the label is turned away by geometry, because naming a brand renders its
badging and no later ban removes it
([§34](../../google-flow/nano-banana-2.md#34--naming-a-marque-renders-its-badging-and-no-downstream-constraint-removes-it-observed-2026-09-08)).

**Paste into:** Flow → image prompt box. **Character:** `@2008 - tarquin`. **No reference image.**

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. In this frame he is pouring champagne into an office mug without looking at it, while the man at the next desk sits with his head in his hands.

Camera: a 50mm lens at desk height, level, about a metre from the mug, the frame very slightly tilted and the desk running away to the left. The mug and the bottle are the nearest things in the picture and sit just in front of the plane of focus, soft but plainly readable; his face a little behind them is sharp. The far end of the room falls away completely.

Subject: the man from the character reference, leaning in over his own desk, seen from the chest up behind the mug. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples.

Action: he is pouring from a small champagne bottle into a chipped white office mug with a brown tannin ring dried inside it. The mug is already overfull — the foam has risen over the lip and is running down the outside onto a heap of printouts, and he has not stopped pouring. His other hand is splayed flat on the desk taking his weight. He is not looking at the mug: his eyes are aimed at a monitor just outside the right edge of the frame, lower lids pushed up, brows level, one corner of his mouth pulled back and held there. The foil off the bottle has been torn away and dropped on the desk, and the bottle's label is turned away from the lens.

Beside him: at the next desk along, a metre to the left and slightly behind, a heavy-set man in his fifties sits forward with his elbows on the desk and the heels of both hands pressed into his eye sockets, fingers pushed up into thinning grey hair, his head bowed so far that the top of his skull faces the lens and hides the whole of the rest of his head behind it. His shirt is creased and dark with sweat between the shoulder blades, his tie pulled loose and hanging off to one side, a wedding ring on one hand. He is not moving. Neither man is acknowledging the other.

Environment: the desk is a mess — loose printouts heaped and sliding, curling Post-it notes stuck to the monitor bezels, a tangle of cables over the back edge, biro marks along the desk lip, a keyboard with one key missing. The monitors are the slim flat panels of 2008 on articulated steel arms, with thick dark plastic bezels.

Light: the photograph was taken with a flash on top of the camera, fired straight across the desk. The foam at the rim of the mug and the wet ring spreading on the printouts are the brightest things in the picture, and the bottle throws a crisp dark shadow across the paper. The foam clips to featureless white at its brightest, while the shadowed side of his face and the desk surface keep their detail rather than going to solid black. The flash does not reach far: the man at the next desk is noticeably darker than the mug, and the room beyond the two of them is only a dim green wash from the ceiling tubes and the cold glow of the screens. The shutter stayed open after the flash fired, so the falling champagne is a soft continuous streak rather than separate drops, while the foam at the rim is frozen sharp.

Style: a newspaper photograph of the 2008 financial crisis, shot on a Canon EOS-1D Mark III with a Speedlite — fine digital noise and mild chromatic noise in the shadows, a cool blue-green cast from the tubes, muted colour, unretouched with no skin smoothing, harsh and unflattering.

Constraints: the only light sources are the camera's flash, which is behind the lens, and the ceiling fluorescent tubes, which are above the top edge of the frame. Every screen is switched on and carries columns of figures far too small and soft to read. The bowed man's own head hides his face, so the trader's is the only legible face in the picture. He is twenty-five years old. His expression stays small — a stranger looking at this photograph would read concentration before they read pleasure. No brand names, logos or readable labels anywhere, including on the bottle. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

### 1m-m — the clip · **video** · written 2026-09-12, unrun

**Recorded despite the [2026-08-26 stills-only ruling](#-next-session--start-here)**, because this
one is not self-explanatory: it carries a routing call, a documented physics risk that is the
subject of the shot, and a light that must be told to hold still.

✅ **The still is accepted** (Jack handed the frame over, 2026-09-12).
⬜ **Master not banked** — save it as `camera/reference/1m-m-champagne-mug-ACCEPTED.png`.

**Routing:** Omni Flash → **Frames** tab, the accepted `1m-m` frame as the **start frame**, **end
slot empty**. 10s available; **generate the full 10s** — the spread needs runtime and the last
seconds are the strongest.

🔴 **Frames, and no Character.** Two reasons, and the second is the one that decides it:

1. **The composition is the shot** — the flash falloff, the metre of desk between the two men, the
   geometry of the foam. [Ingredients re-stages](../../google-flow/omni-flash.md#️-the-combined-mode-does-not-exist-in-flow).
2. 🔑 **The plate is the only authority on the face we want.** `@2008 - tarquin` has come back
   reading mid-thirties **twice** (1c, `1m-e` round 1). Attaching it here would put a second and
   older authority on a face the still already got right. The n=1 caution that
   [Frames once lost a face](../../google-flow/omni-flash.md#frames-lost-the-face-ingredients-held-both-n1-each-way)
   is real — **if the face drifts, the fix is a re-roll on Frames, not a switch to Ingredients.**

#### 🔑 The design: the spill spreads while he does not look

[A frame whose first and last frames match reads as a photo, not a shot](../../cinematography/stills.md#1-what-makes-a-still-hold),
so the clip needs one event. **It is the wet ring creeping outward through the printouts.**

Why that one and nothing else:

- **It is the meaning, not decoration.** The still's whole argument is *he is not looking at the
  mug.* A clip in which the damage visibly grows while his eyes stay on the screen makes that
  argument a second time, in motion, with no narration.
- 🔑 **It is the same physics class as [`1y`'s tide](#1y--the-tide-coming-in--video--written-2026-08-30-unrun)**
  — a slow single-vector wetting across a flat plane with everything else static. Close to the
  easiest thing this engine is ever asked to do.
- **One system, three visible things.** Foam sliding, paper darkening, the streak falling are all
  the same event, which satisfies *one main action per clip* while still giving the eye work.
- **The cost gets a pulse.** The bowed man takes one breath. It is the only thing in the montage
  that says the body is alive, and [minimal human motion is the field's own realism lever](https://magichour.ai/blog/realistic-ai-video-prompting) `[community]`.

#### 🔴 The top risk is the liquid, and it is the subject of the shot

`[academic]` **Video diffusion models fail fluids in two named ways**: *unstable fluid geometry —
column breakage, sudden volume change, gravity-inconsistent bouncing or floating*, and
*inconsistent fluid–container interaction — offset entry points, discontinuous liquid-level
changes, splash directions misaligned with the applied force*
([arXiv 2607.25321](https://arxiv.org/abs/2607.25321)). Practitioner guidance agrees and is blunter:
*"for anything where the water's exact volume or splash shape has to be correct on delivery, this
requires a different tool, not a better sentence"* `[community]`.

**Four clauses answer it, and the first is free:**

| The failure | The clause |
| --- | --- |
| **The level fails to rise** | 🔑 **We never ask it to.** The mug is *already* overfull in the plate, so volume conservation is out of scope by construction. This is the fluid equivalent of [never catching the whole fall](../../google-flow/omni-flash.md#the-rule-that-outranks-all-of-it-a-real-camera-never-catches-the-whole-fall) |
| **The column breaks apart mid-air** | The stream is named as **one unbroken streak of the same width, in the same place** — the positive form of *it does not break up*, because [a negation would name breakage into the prompt](../../google-flow/omni-flash.md#-negatives-do-not-work-and-they-actively-backfire) |
| **Splashes with the wrong momentum** | **No splash is ever requested.** The foam *slides* and the paper *darkens where it reaches* — wetting, not impact |
| **Fast fluid rendered sharp** | The [24fps / 180° shutter clause](../../google-flow/omni-flash.md#the-shutter-is-the-tell-nobody-prompts-for), `[confirmed 2026-08-14]` on fast motion. The still already contains the streak, so the clip is only being asked to continue what is in frame |

#### 🔴 Second risk: the light must be told to hold, and the word *flash* must not appear

This is a **flash photograph** — one instant of light. Asked to animate it, the engine has every
invitation to make the light an event: a second pop, a flicker, a lamp warming up.
[§35 is explicit that a flash described as an object in the room is drawn as a lamp](../../google-flow/nano-banana-2.md#35--a-flash-described-as-an-object-in-the-room-is-drawn-as-a-lamp-observed-2026-09-11-n1),
and `1m-e` round 1 proved it on the still side.

🔑 **So the clip prompt never says "flash".** It states the light as a fact that holds —
*"the light in the picture stays exactly as it is throughout"* — which is positive, names no
source, and gives the model nothing to go looking for.

#### ⚠️ Text: define the bare surfaces, again

`[confirmed 2026-08-17, Karen §2j.6sv]` — a clip block that never mentioned signage came back with
writing crawling onto a sign. This frame is **full** of surfaces that want lettering: Post-its,
a heap of printouts, four screens. They are named as blank and as too small to read, and the
screens are told to hold a **steady** glow, because
[text changing between frames is the documented failure](../../google-flow/omni-flash.md#-the-360p-draft-is-a-motion-check-never-a-text-check--and-upscaling-repairs-nothing).

#### ⚠️ Audio, and where the ringing phone goes

**Behind the camera.** Omni generates picture and sound together, so a sound sited on a visible
object is a second vote for that object owning it — the
[3c-y finding](#3c-y--the-lane-hours-later--video--written-2026-09-09-unrun), learned the hard way.
A telephone nobody answers says the floor is in trouble at **zero render risk**, and it is the
audio half of the same argument the picture is making. **No music, no voices** —
[we never put speech in a Flow video](../../google-flow/omni-flash.md#-the-speech-trap-is-punctuation-not-vocabulary).

#### ⬜ The camera does not move, and no shake

Any push is a **Premiere** job on the finished clip
([`hybrid-method.md`](../../video-fx/hybrid-method.md)). And the widely-recommended
*"add accidental camera shake"* is **rejected house-wide** —
[`motion-and-cutting.md` R7](../../cinematography/motion-and-cutting.md#1-movement): handheld is a
style, not truth. Irregularity is bought in the foam, not the camera.

#### ⚠️ Length is still the open question

The [~50-word / 150–300-word conflict](../../google-flow/omni-flash.md#️-open-conflict-how-long-should-an-omni-prompt-be-unresolved-2026-08-30)
is unresolved and `1y`'s experiment is still unrun. **Fire the primary first**, matching the shape
that has actually been producing accepted clips (frame-lock, camera, action, pins, shutter, audio);
if it comes back diluted or re-staged, fire the fallback. 🔑 **Record which one won** — it is the
same experiment.

**Paste into:** Flow → **Frames to Video** prompt box. **Start frame:** the accepted `1m-m` image.
**End frame:** empty. **No Character, no Ingredients.** Primary:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts. The camera is locked off at the desk and holds completely still throughout, and the light in the picture stays exactly as it is.

He keeps pouring. The champagne falls from the lip of the bottle into the mug as one unbroken soft streak, the same width and in the same place the whole time. The mug stays full to the brim. The foam standing over the rim swells and slides down the outside of the mug in slow uneven trails, and the wet ring in the heap of printouts creeps outward, the paper going dark and translucent where it reaches.

He does not look down. His eyes stay exactly where they are, he blinks once, and the pulled-back corner of his mouth holds. The bottle tips fractionally further as the shot runs.

The man at the next desk takes one slow breath, his shoulders lifting and settling. The heels of his hands stay pressed into his eyes and his head stays bowed.

The desk, the monitors, the fallen paper cup, the biro and every sheet of paper stay exactly where they are. The screens hold a steady cold glow with columns of figures far too small and soft to read. The notes stuck to the monitors and the printouts on the desk are blank paper.

Shot at 24fps with a 180-degree shutter, so the falling champagne smears into a soft streak while everything still is sharp.

Audio: the fizz of foam, liquid running onto wet paper, the low hum of the room, and one telephone ringing unanswered somewhere behind the camera. No music and no voices.

Thanks.
```

⬜ **Fallback, only if the primary comes back diluted or re-staged** — same tab, same start frame:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. Camera locked off, single continuous shot, no cuts, and the light stays as it is.

He keeps pouring in one unbroken streak and does not look down. The foam slides down the outside of the mug and the wet ring creeps outward through the printouts. The man beside him takes one slow breath.

Audio: fizz, liquid on paper, a telephone ringing behind the camera. No music and no voices.

Thanks.
```

**Post, in Premiere:**

1. ⬜ **Any push in is here, not in Flow** — and this frame has something worth arriving at: the mug.
2. **A 10–15% speed adjustment** against the smooth-motion tell `[community]`.
3. **Match the grain rather than stacking it** — the still already carries 2008 press-DSLR noise.
4. ⚠️ **Watch the streak and the foam edge on playback.** If the column breaks, pulses or the mug's
   level jumps, that is the fluid risk firing and **it is a re-roll, not a grade.**
5. ⚠️ **Nothing ships unmeasured** — `scripts/delivery-qc.sh`
   ([`delivery.md`](../../video-fx/delivery.md)).

**Sources for this entry (2026-09-12):**
[arXiv 2607.25321 — physics-grounded fluid video generation](https://arxiv.org/abs/2607.25321) `[academic]` ·
[Prompt Architects — VFX and effects prompting](https://prompt-architects.com/blog/360-vfx-and-effects-prompting) `[community]` ·
[Magic Hour — realistic AI video prompting, 10 pillars](https://magichour.ai/blog/realistic-ai-video-prompting) `[community]` ·
[Promptessor — image-to-video prompts, the "living still"](https://promptessor.com/blog/image-to-video-prompts-how-to-animate-photos-products-characters-and-art-in-2026) `[community]` ·
[Imagine.art — Omni Flash video generation guide](https://www.imagine.art/blogs/guide-to-gemini-omni-flash-video-generation) `[community]`


### 1m-l — the lift doors · **still** · written 2026-09-12, unrun

**The job:** he goes up, they go down. It is the cleanest statement of *without a scratch* the montage has,
and it makes the argument with architecture instead of a face.

🔑 **The pattern break is the light, and it is deliberate.** The floor frames are flash; this one is
available light off the ceiling panel of the lift car. That gives the montage a rule worth keeping —
**flash is the trading floor, available light is everywhere else** — which `1m-7` (daylight, the house) and
`1m-8` (the glow of his own screens) already follow.

🔑 **Why the lift and not a corridor:** the doorway is a frame-within-a-frame
([principle 6](../../cinematography/principles.md)), so it states *contained* with no caption; the lit car
is the one bright anchor in a dark frame (principle 11); and the nearest box-carrier is the foreground
occluder, the visible cost and the motion blur all at once.

⚠️ **It is set late evening on purpose.** A dark lobby in working daylight is a physics contradiction, and
[§20](../../google-flow/nano-banana-2.md#20--if-the-named-source-cannot-physically-light-the-scene-the-model-invents-fill-confirmed-2026-08-27)
says the engine closes those by inventing fill. The lobby lights being down to their night setting is what
makes the car legitimately the brightest thing in the picture. **The cost: the famous box-carrying images
of 2008 are daytime**, so this trades documentary familiarity for a frame that can actually hold darkness.
A human call.

🔴 **Face-size risk.** Google's own stated weakness for this model is *small faces*, and at three metres in
a knees-up framing his face is not large. **If the likeness does not bind on round 1, move the camera in to
a waist-up framing — do not add words about his face.**

⚠️ **The handset is period-correct and deliberately unnamed** — *"a small black handset with a keyboard"*.
2008 is the BlackBerry era (smartphones were roughly a fifth of handsets), and naming the marque would
render its badging.

**Clip note:** this is the one of the three worth the video credit. Camera locked; the moving element is the
**rectangle of light on the carpet narrowing to a line and going out** as the doors close.

**Paste into:** Flow → image prompt box. **Character:** `@2008 - tarquin`. **No reference image.**

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. It is late evening. In this frame he is going up alone in a lift while three people carry their belongings out across the lobby in front of him, and the doors are closing on him.

Camera: a 35mm lens at standing chest height, level, about three metres back from the lift doors and off to one side, so the lit lift car sits right of centre and the dark lobby runs away to the left. The doors have begun to close and he is framed in the gap between them, visible from the knees up.

Subject: the man from the character reference, standing alone in the middle of the lift car, facing out through the closing doors. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples.

Action: he has just lifted his eyes from a small black handset with a keyboard, held low in one hand, to the closing doors. His suit jacket is hooked over the other shoulder on one finger. His weight is on one leg, his shoulders dropped, his chin level. His eyes are aimed just past the nearest of the people crossing in front of him, at nothing in particular, his lids relaxed, his brows level and his lips closed. Nothing in his face is reacting to them.

In front of him: three people are crossing the lobby between the camera and the lift, walking away to the left, carrying their things out. No two of them are alike — different heights, builds, hair and clothes. One carries a cardboard archive box in both arms with a coat folded over the top of it; one has a bulging canvas holdall on a shoulder; one holds a potted desk plant and a framed picture against the chest. All three are seen squarely from behind, so the backs of their heads face the lens and hide the rest of them. The nearest passes close enough to the lens to cross the bottom left of the frame as a dark shape, thrown completely out of focus so that it is a soft blur.

Environment: the lift lobby of a City of London office tower — brushed stainless lift doors with a scuffed kick plate, a dark stone-tiled wall, grey carpet tiles with a worn track across them, a dented skirting board, a red fire extinguisher on a bracket. The lobby lights have gone down to their night setting and two of the recessed ceiling fittings are dead.

Light: the only strong light in the picture is the fluorescent panel in the ceiling of the lift car. It is directly above him, so it lights the top of his head, his shoulders and the tops of his cheekbones and leaves his eye sockets and the underside of his jaw in shadow, and it throws a hard-edged rectangle of light out of the doorway onto the carpet in front of him. Nothing else reaches this far: the three people crossing are almost black shapes against that rectangle, and the back of the lobby falls away to nothing. The picture is exposed for the inside of the car, so roughly three-quarters of the frame sits in deep shadow, with the brushed stainless doors catching one thin edge of the light — and that deep shadow keeps a trace of detail rather than going to solid black. The exposure is long enough that the three crossing people are softened by their own movement while the inside of the car is sharp.

Style: a newspaper photograph of the 2008 financial crisis, taken on a Canon EOS-1D Mark III by available light with no flash, at ISO 3200 — coarse digital noise and mild chromatic noise in the shadows, muted cool colour, unretouched with no skin smoothing, deeply underexposed everywhere except the inside of the lift car.

Constraints: the lift car's ceiling panel is the only light source in the picture, and the floor indicator and the call buttons are above the top edge of the frame. The three people crossing are seen only from behind, so his is the only legible face in the picture. He is twenty-five years old. His expression stays small and unbothered — a stranger looking at this photograph would not be able to say what he is feeling at all. No brand names, logos or readable labels anywhere, including on the handset. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

### 1m-l — round 1, **not accepted** (Jack, 2026-09-12: *"it looks like ai slop"*)

✅ **What landed, and it is the whole idea — keep it.** Jack: *"I like that it makes him look evil
and he is the only one winning whilst others are obviously fired and walking away."* The lit box,
the dark lobby, the leavers with their things. **Round 2 changes execution, not the shot.**

🔴 **He is wearing a jacket *and* carrying one.** Jack spotted it. The prompt said *"his suit jacket
is hooked over the other shoulder"* and **never said what was on his body**, so the model supplied
the default a City trader wears — and then also drew the one it was told about. New
[§36](../../google-flow/nano-banana-2.md#36--a-carried-garment-with-no-worn-garment-stated-returns-both-observed-2026-09-12-n1);
it is [§25](../../google-flow/nano-banana-2.md#25--19-inverts-for-an-unbound-body-part--describe-it-or-get-young-clean-and-generic-observed-2026-08-29)'s
family — silence returns the generic default.

**Six more, read off the frame:**

| What came back | Cause |
| --- | --- |
| 🔴 **Dead-centre, symmetrical.** The prompt asked for the car *"right of centre"* and got it on the axis | A square-on lift door is a symmetry magnet and [the centring bias is documented](https://www.pixova.io/blog/how-to-make-ai-images-look-less-like-ai) `[community]`. **A composition adjective loses to an architectural feature.** New [§37](../../google-flow/nano-banana-2.md#37--a-square-on-architectural-feature-is-a-symmetry-magnet-and-a-composition-adjective-will-not-move-it-observed-2026-09-12) |
| 🔴 **The doors are wide open.** The beat is *the doors closing on him* and it is simply absent | *"The doors have begun to close"* is a stage direction, and a lift door's prior is **open or shut**. New [§38](../../google-flow/nano-banana-2.md#38--a-mechanical-in-progress-state-returns-fully-open-or-fully-shut--give-it-a-physical-analogy-observed-2026-09-12) — the fix is [§30](../../google-flow/nano-banana-2.md#30--a-physical-analogy-overrules-a-stated-number--and-it-is-how-28-keeps-happening-observed-2026-09-08)'s lever, a **physical analogy** |
| 🔴 **Two of the three leavers are the same man in the same dark suit** | *"No two of them are alike"* is an adjective. [Crowd realism is individuation](../../google-flow/nano-banana-2.md#-crowd-realism-is-individuation-not-adjectives-practitioner) — count, gender, age, dress and **distance apart**, stated |
| 🔴 **A polished marble atrium.** Carpet tiles, dented skirting, fire extinguisher and scuffed kick plate all lost | Six worn nouns beat by one *"City of London office tower"* prior. The counter is [§29](../../google-flow/nano-banana-2.md#29--to-overrule-a-reference-on-one-element-declare-its-role-narrowly-then-negate-the-old-value-observed-2026-08-30)'s shape in the terminal `Constraints:` block — **name the surface, then negate the old value** |
| 🔴 **It reads as a corporate-thriller poster, not a press photograph.** Glossy stone, mirror floor, no grain, smooth skin | The [aesthetic mode](../../google-flow/nano-banana-2.md#️-the-quality-word-kill-list-now-includes-cinematic) won over *"ISO 3200, coarse digital noise"*. The cheap lever not used: **a human behind the camera** — *candid*, *taken quickly*, [`[community]`](../../google-flow/nano-banana-2.md#-kodak-portra-400-may-now-be-a-slop-tell-community-untested) |
| ⚠️ **The foreground occluder is a giant blurred head** filling a fifth of the frame, with a soft halo | The [fake-DoF tell](../../google-flow/nano-banana-2.md#️-fake-depth-of-field-has-its-own-tells-practitioner-community) firing at an occluder's edge. **Make the occluder an object, not a person** — nothing to halo and one fewer body to clone |
| ⚠️ **Readable white lettering** on the thing the left-hand man carries | The `Constraints:` label ban did not reach an unnamed object. Name it: *plain brown, nothing printed* |

⬜ **Also gone:** he is in a resting pose — standing still, facing forward, arms at his chest.
[A resting pose dies fast; a still only holds if it contains an unresolved question](../../cinematography/stills.md#1-what-makes-a-still-hold).

### 🔴 Model: there is still no "Nano Banana Pro 2" — re-verified 2026-09-12

Asked for again, so re-checked live. **The family is unchanged:** Nano Banana → **Nano Banana Pro**
(Gemini 3 Pro Image) → **Nano Banana 2** (Gemini 3.1 Flash Image, 26 Feb 2026) → **Nano Banana 2
Lite**. *"2" is the Flash line and "Pro" is the larger model, so the higher number is not the better
model.* Full write-up: [§fifth pass](../../google-flow/nano-banana-2.md#️-there-is-no-nano-banana-pro-2-vendor-community).

**Use Nano Banana Pro**, as the rest of the montage did — it is the house pick where the job is
*suppressing* sharpness and contrast, which is this frame exactly.
⚠️ **Check Flow's picker before you start:** `[community]` reporting has Lite as the default since
July 2026, so a session can be on Lite without anyone choosing it.
⬜ **Take 2K, not 4K** — [off-native resolution is a named cause of duplication](../../google-flow/nano-banana-2.md#22--tiling-and-cloning-in-crowd-scenes-are-a-resolution-problem-not-only-a-prompt-problem-community-2026-08-28),
and round 1 already cloned two of three figures.

⚠️ **One `[community]` guide says to strip politeness — *"remove polite phrases like 'please'"* — to
cut conversational filler.** No test behind it, and it collides with a standing house rule.
**We keep the `Thanks.`** Noted so nobody re-derives it.

### 1m-l — round 2 · **still** · written 2026-09-12, unrun

**Six structural changes, and the first is the one that fixes the composition:**

1. 🔑 **The LOBBY goes in the `Subject:` slot and the lift becomes a feature of it.** This is the
   house-proven fix for exactly this symptom —
   [3c round 1 centred the car and round 2 fixed it by putting the ROAD in Subject](#3c--the-lane-hours-later--still--written-2026-09-09-unrun),
   and it is [§546's lever](../../google-flow/nano-banana-2.md#-making-a-subject-small-put-something-else-in-the-subject-slot-community-2026-09-09).
   **Backed up by geometry:** the camera goes off the door plane, so the doorway is a leaning
   rectangle and there is no axis for the model to snap to.
2. **The gap is a physical analogy, not a stage direction** — *narrower than his shoulders, so the
   doors crop him at both arms.* The same fact is then stated a second time by the light: a
   **narrow strip** on the carpet, not a rectangle.
3. 🔑 **He wears one jacket, it is on him, and he is the only suited figure in the picture.** That
   kills the duplicate-jacket bug and does the argument's work at the same time: **the leavers are
   in shirtsleeves and jumpers, he is dressed to go somewhere.** Class stated in cloth.
4. 🔑 **The resting pose becomes one small gesture: he has just pressed the button.** His hand is
   still up at the panel. It is mid-travel, it is the unresolved question the frame was missing,
   and it makes the cruelty physical without a caption — *he closes the doors himself.*
   ⚠️ **This is the one deliberate beat change.** [Principle 24](../../cinematography/principles.md)
   is live on any frame that could read as celebration; the guard is that the gesture is **banal**
   — a man pressing a lift button on his way home — and that `Constraints:` still bounds the face
   from above. ⬜ **If it reads as pantomime villainy, revert the hand to the handset** and keep
   everything else.
5. **The occluder is an object** — two archive boxes left on the carpet. No halo, no clone.
6. **A scoped negation block for the atrium**, and *candid / taken quickly* for the human behind
   the camera.

🔴 **Face-size risk is unchanged and now flagged twice.** Google's own stated weakness is *small
faces*. **If the likeness does not bind on round 1, switch the lens to 85mm from the same standing
position** — [long lenses are under-used](../../google-flow/nano-banana-2.md#14--long-lenses-are-under-used-and-hard-to-fake-community),
it stacks the lobby, it keeps the asymmetric layout, and it grows his head without re-staging.
**Do not add words about his face.**

**Paste into:** Flow → image prompt box. **Model:** Nano Banana Pro (check the picker). **Aspect:**
16:9. **Resolution:** 2K. **Character:** `@2008 - tarquin`. **No reference image.**

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. It is late evening. In this frame the lift doors are closing on him while three people carry their belongings out across the dark lobby, and he is the only one going up.

Camera: a 35mm lens at standing chest height, level, taken quickly and candidly from about three metres out into the lobby and well over to the left, so the bank of lift doors runs away to the right at an angle and no wall in the room is square to the lens. The lit car sits left of centre and the dark lobby fills the right two-thirds of the picture. Nearest the lens, two cardboard archive boxes stacked on the carpet cross the bottom left corner, dark and thrown completely out of focus so that they are a soft blur.

Subject: the lift lobby of an ordinary City of London office tower at night, worn rather than grand. Three brushed stainless lift doors set into a matt painted wall, scuffed kick plates, grey carpet tiles with a worn track across them, a dented skirting board, a red fire extinguisher on a bracket, a plastic waste bin. The lobby lights are down to their night setting, with only a few dim fittings still on far back.

Action: the nearest of the three lift cars is lit and its doors are closing. The gap between the leading edges is already narrower than a man's shoulders, so the doors crop him at both arms and only a tall slot of the car interior is visible. The doorway is seen slightly from its left side, so it reads as a leaning rectangle rather than a square-on one.

Him: the man from the character reference stands in that slot, seen from the thighs up, facing out. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples. He is wearing his suit jacket, done up, over a shirt and tie, and he carries nothing over his arm. One hand is still raised to the button panel on the side wall inside the car, the fingers just coming off the buttons, because he has this second pressed one. The other hand holds a small black handset with a keyboard, low and forgotten. He is watching the closing gap, his chin level, his lids relaxed, his brows level, his lips closed. Nothing in his face is reacting to the people outside.

In front of him: three people are walking away from the camera across the lobby to the right, into the dark, carrying their things out, strung out at different distances rather than walking together. Nearest is a woman in her forties in shirtsleeves, a coat over one arm and a bulging canvas holdall on the other shoulder, caught mid-stride with one heel off the carpet. Further back is a broad man in his fifties, grey and thinning on top, carrying a plain brown cardboard box level in both arms. Furthest and almost lost in the dark is a thin young man in a knitted jumper holding a potted desk plant and a framed picture against his chest. All three are seen squarely from behind, so the backs of their heads face the lens and hide the rest of them.

Light: the fluorescent panel in the ceiling of the lift car is the only strong light in the picture. It is directly above him, so it lights the top of his head, his shoulders and the tops of his cheekbones and leaves his eye sockets and the underside of his jaw in shadow, and it throws a narrow hard-edged strip of light out of the closing doorway that runs diagonally across the carpet toward the bottom right of the frame. The picture is exposed for the inside of the car: the front of his shirt clips to featureless white, the three people walking away are near-black shapes cut out against the carpet, and the lobby around them holds a trace of detail in the deep shadow rather than going to solid black.

Style: a candid press photograph of the 2008 financial crisis, taken on a Canon EOS-1D Mark III by available light with no flash, at ISO 3200 — coarse digital noise and mild chromatic noise in the shadows, muted cool colour, slightly missed focus at the edges, unretouched with no skin smoothing, harsh and unflattering.

Constraints: the lift car's ceiling panel is the only light source in the picture, and the floor indicator above the doors is above the top edge of the frame. The lobby is worn and ordinary — carpet tiles rather than stone, a matt painted wall rather than marble, and a floor that reflects nothing. He wears one jacket and it is on his body. He is the only person in the picture wearing a suit jacket. The three people walking away are seen only from behind, so his is the only legible face in the picture. He is twenty-five years old. His expression stays small and unbothered — a stranger looking at this photograph would not be able to say what he is feeling at all. The cardboard boxes are plain brown with nothing printed on them, and there are no brand names, logos or readable labels anywhere, including on the handset. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

**Check these five on round 1, worst first:** the gap between the doors is actually narrow · the lift
is off the centre axis · he has exactly one jacket and it is on him · the three leavers are three
different people · the floor is carpet and does not reflect.

### 1m-l — round 2, **policy block** (Jack, 2026-09-12: *"it says it violates policies"*)

🔑 **The diagnosis is a diff, not a guess about the picture.** Round 1 of this exact shot
**generated** — it was rejected on quality, not refused — so the block is in something round 2
*added*. Everything shared by both rounds is cleared by that fact, including the two clauses
that would otherwise be first suspects: the face-age block (*"keep the face lean and unlined…"*,
[trigger 2](../../flow/failure-modes.md#a5-the-five-triggers-badcodes-own)-shaped) and the real
camera marque, both of which passed unchanged in round 1.

**Four things were new in round 2. All four are cut or swapped unrun**, per the standing posture
from [A5b](../../flow/failure-modes.md#a5b-the-bedroom-problem--trigger-5-in-detail): *on a prompt
the filter is already primed for, do not spend generations defending a clause you do not need.*
🔴 **Cause is inferred from the diff, not tested** — no clause was isolated.

| New in round 2 | Why it is a suspect | Round 3 |
| --- | --- | --- |
| 🔴 *"the doors **crop him at both arms**"*, with the gap *"narrower than a man's shoulders"* | **Prime suspect.** This is [A5b](../../flow/failure-modes.md#a5b-the-bedroom-problem--trigger-5-in-detail)'s mechanism exactly — *context does not protect a word, it convicts it*. *Crop* is a photographer's word in a photographer's paragraph, but here the sentence is machinery closing on a body and naming the body parts it reaches, which supplies the classifier's other reading | The narrow gap survives as a **negative space fact** — *only a tall narrow slot of the car is still visible* — and the arms are never mentioned. The §30 physical analogy is kept |
| 🟡 *"taken quickly and **candidly**"* + *"a **candid press** photograph"* | *Candid* photographs *of people* is its own flagged phrase shape, and round 2 put it in twice. It was only ever there as the cheap [human-behind-the-camera lever](../../google-flow/nano-banana-2.md) against the glossy-poster failure | The lever is kept without the word: *taken in a hurry by someone crossing the lobby* |
| 🟡 *"a **thin young man** in a knitted jumper"* | An age descriptor on a body descriptor. Google's classifier [fuzzy-matches young/teen/child](../../flow/failure-modes.md#a6-rewrite-patterns) and flags any subject who *could* be a minor regardless of context. Round 1 gave the three leavers no ages at all | *a slight man in a knitted jumper*. The individuation that §crowd-realism wanted is carried by build, dress and distance, which is what it asked for anyway |
| 🟡 *"a **press** photograph of the 2008 financial crisis"* | Round 1 said *"a **newspaper** photograph of the 2008 financial crisis"* and passed. One word from a known-good line, next to a real event, on the [synthetic-news](../../flow/failure-modes.md#-synthetic-news-trigger--may-cause-reputational-risk-or-misrepresent-current-events) shelf | Reverted to round 1's exact passing wording. Free |

⚠️ **Everything round 2 fixed is intact** — the lobby in the `Subject:` slot, the off-axis camera,
one worn jacket on his body, the button-press gesture, the object occluder, the atrium negation.
Round 3 is round 2 with four phrases changed.

⬜ **If round 3 still blocks,** the next cut is the face-age block — *"keep the face lean and
unlined… no hollowing under the cheekbones"* — which is likeness engineering on a cast Character
and is [the house rule's own exception](./characters/tarquin.md) being stretched. Cut it whole and
let `@2008 - tarquin` carry the age; do not rewrite it smaller.

### 1m-l — round 3 · **still** · written 2026-09-12, unrun

**Check these five on the result, worst first:** the gap between the doors is actually narrow ·
the lift is off the centre axis · he has exactly one jacket and it is on him · the three leavers
are three different people · the floor is carpet and does not reflect.

**Paste into:** Flow → image prompt box. **Model:** Nano Banana Pro (check the picker — Lite is
the silent default). **Aspect:** 16:9. **Resolution:** 2K. **Character:** `@2008 - tarquin`.
**No reference image.**

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. It is late evening. In this frame the lift doors are closing on him while three people carry their belongings out across the dark lobby, and he is the only one going up.

Camera: a 35mm lens at standing chest height, level, taken in a hurry by someone crossing the lobby, from about three metres out and well over to the left, so the bank of lift doors runs away to the right at an angle and no wall in the room is square to the lens. The lit car sits left of centre and the dark lobby fills the right two-thirds of the picture. Nearest the lens, two cardboard archive boxes stacked on the carpet cross the bottom left corner, dark and thrown completely out of focus so that they are a soft blur.

Subject: the lift lobby of an ordinary City of London office tower at night, worn rather than grand. Three brushed stainless lift doors set into a matt painted wall, scuffed kick plates, grey carpet tiles with a worn track across them, a dented skirting board, a red fire extinguisher on a bracket, a plastic waste bin. The lobby lights are down to their night setting, with only a few dim fittings still on far back.

Action: the nearest of the three lift cars is lit and its two doors have almost met. The gap left between their leading edges is narrower than a man's shoulders, so only a tall narrow slot of the car interior is still visible and the doors hide everything to either side of it. The doorway is seen slightly from its left side, so it reads as a leaning rectangle rather than a square-on one.

Him: the man from the character reference stands in that slot, seen from the thighs up, facing out, with the edge of a door passing in front of each of his shoulders. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples. He is wearing his suit jacket, done up, over a shirt and tie, and he carries nothing over his arm. One hand is still raised to the button panel on the side wall inside the car, the fingers just coming off the buttons, because he has this second pressed one. The other hand holds a small black handset with a keyboard, low and forgotten. He is watching the closing gap, his chin level, his lids relaxed, his brows level, his lips closed. Nothing in his face is reacting to the people outside.

In front of him: three people are walking away from the camera across the lobby to the right, into the dark, carrying their things out, strung out at different distances rather than walking together. Nearest is a woman in her forties in shirtsleeves, a coat over one arm and a bulging canvas holdall on the other shoulder, caught mid-stride with one heel off the carpet. Further back is a broad man in his fifties, grey and thinning on top, carrying a plain brown cardboard box level in both arms. Furthest and almost lost in the dark is a slight man in a knitted jumper holding a potted desk plant and a framed picture against his chest. All three are seen squarely from behind, so the backs of their heads face the lens and hide the rest of them.

Light: the fluorescent panel in the ceiling of the lift car is the only strong light in the picture. It is directly above him, so it lights the top of his head, his shoulders and the tops of his cheekbones and leaves his eye sockets and the underside of his jaw in shadow, and it throws a narrow hard-edged strip of light out of the closing doorway that runs diagonally across the carpet toward the bottom right of the frame. The picture is exposed for the inside of the car: the front of his shirt clips to featureless white, the three people walking away are near-black shapes cut out against the carpet, and the lobby around them holds a trace of detail in the deep shadow rather than going to solid black.

Style: a newspaper photograph of the 2008 financial crisis, taken on a Canon EOS-1D Mark III by available light with no flash, at ISO 3200 — coarse digital noise and mild chromatic noise in the shadows, muted cool colour, slightly missed focus at the edges, unretouched with no skin smoothing, harsh and unflattering.

Constraints: the lift car's ceiling panel is the only light source in the picture, and the floor indicator above the doors is above the top edge of the frame. The lobby is worn and ordinary — carpet tiles rather than stone, a matt painted wall rather than marble, and a floor that reflects nothing. He wears one jacket and it is on his body. He is the only person in the picture wearing a suit jacket. The three people walking away are seen only from behind, so his is the only legible face in the picture. He is twenty-five years old. His expression stays small and unbothered — a stranger looking at this photograph would not be able to say what he is feeling at all. The cardboard boxes are plain brown with nothing printed on them, and there are no brand names, logos or readable labels anywhere, including on the handset. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

### 1m-l — round 4 · **still** · written 2026-09-13, unrun · *supersedes round 3*

**Written after Jack re-ran the shot and hit the policy card again.** Round 4 is round 3 with
**two changes**, and the first one is both the policy fix and the better picture.

#### 🔑 1. The door state is told by the SHAPE OF THE LIGHT, not by what the machine does to his body

[A5c](../../flow/failure-modes.md#a5c-trigger-5s-other-half--machinery-plus-a-named-body-part-inferred-untested)
puts the block on *machinery closing on a body, naming the body parts it reaches*. Round 3 cut
*"crop him at both arms"* but **kept two more instances of the same shape** — *"narrower than a
man's shoulders"* and *"the edge of a door passing in front of each of his shoulders"*. Under the
do-not-defend posture those go too.

The replacement is not a weaker sentence, it is a better one:

| Round 3 | Round 4 |
| --- | --- |
| *the gap … is narrower than a man's shoulders* | *a tall narrow slot about **a quarter of the doorway's full width**, so the lit interior reads as a **bright vertical band** rather than an open doorway* |
| *the edge of a door passing in front of each of his shoulders* | *the doors hiding everything to either side of him* |

**Why it is also the better frame:** the closing is now stated as an optical fact — a band of
light — so [§38](../../google-flow/nano-banana-2.md#38--a-mechanical-in-progress-state-returns-fully-open-or-fully-shut--give-it-a-physical-analogy-observed-2026-09-12)'s
physical analogy survives, [§30](../../google-flow/nano-banana-2.md#30--a-physical-analogy-overrules-a-stated-number--and-it-is-how-28-keeps-happening-observed-2026-09-08)
is satisfied by a proportion of an object already in frame, and the **light does the narrative
work instead of a stage direction**. No body part is named anywhere near the doors.

#### 🔑 2. The `Style:` block was over-corrected, and that is its own slop tell

`[community]` guidance is consistent and blunt: **one or two imperfection words, three at the
absolute most, or the model over-corrects and the picture looks deliberately degraded**
([Pixova](https://www.pixova.io/blog/how-to-make-ai-images-look-less-like-ai),
[Miraflow](https://miraflow.ai/blog/how-to-make-ai-images-look-like-real-photos-prompt-tricks)).
Round 3's style line carried **seven**: coarse digital noise, mild chromatic noise, muted cool
colour, slightly missed focus at the edges, unretouched, no skin smoothing, harsh and unflattering.

Round 4 keeps **three** — ISO 3200 noise, muted cool colour, no retouching — and drops the rest.
🔴 ***slightly missed focus at the edges* is the one that had to go on craft grounds too**: it
invites exactly the [fake-DoF halo](../../google-flow/nano-banana-2.md#️-fake-depth-of-field-has-its-own-tells-practitioner-community)
that round 1 produced on the foreground occluder. This is also
[shot-craft's standing note](../../../.claude/skills/shot-craft/SKILL.md) that when a frame is not
landing, **the fix that works most often is removing a clause, not adding one.**

#### ⚠️ Two smaller changes, both carried over from the diagnosis

- **The camera drops to hip height**, taken by someone hurrying across the lobby. It is the
  `[community]` *shot-from-the-hip* lever for a human behind the camera — which round 2 had
  spent the flagged word *candid* on — it breaks the default chest-height-and-level frame that
  [symptoms.md](../../cinematography/symptoms.md) names in the looks-like-AI bundle, and it puts
  the carpet in the foreground so the picture has three populated depth planes.
- 🔑 **His eyeline goes back to round 1's** — *just past the nearest of them, at nothing in
  particular* — rather than round 3's *watching the closing gap*. It is the stronger beat and it
  is the montage's own line: **he looks through the people it is happening to.** It also gives
  the frame the gaze vector whose absence is a named slop tell.

#### ⬜ Unchanged, and deliberately so

Everything else is round 3, which is round 1's cleared text plus the structural fixes. **The
face-age block and the camera marque both passed in round 1 and stay.** If round 4 still blocks,
cut the face-age block whole — *"keep the face lean and unlined… no recession at the temples"* —
and let `@2008 - tarquin` carry the age. Do not rewrite it smaller.

#### 🔴 Model: Pro or NB2 is now an open A/B, not a settled call — corrected 2026-09-13

There is still nothing called *Nano Banana Pro 2*: the family is Nano Banana → **Nano Banana
Pro** → **Nano Banana 2** (the Flash line) → Nano Banana 2 Lite. **But the naming fact was being
used to carry a quality claim it does not support, and that was wrong.** Nano Banana 2 leads Pro
on human-preference Elo — **1,280 v 1,238** on Arena.ai and **1,264 v 1,220** on Artificial
Analysis for text-to-image — while being ~4× faster and half the cost, and both models offer the
same resolutions up to 4K. Full working and the caveats:
[nano-banana-2.md](../../google-flow/nano-banana-2.md#-corrected-2026-09-13-nano-banana-2-beats-pro-on-the-leaderboards-community).

**What that does and does not change for this frame.** Pro's one reported advantage is
*"complex multi-element compositions… specific spatial relationships, layered lighting, and a
particular mood"* — off-axis geometry, single-source falloff, three individuated figures at
three distances, a foreground occluder. **That is `1m-l` exactly**, and it is where round 1
failed. General-preference Elo is won on pretty single-subject pictures, which is the opposite
of what this shot asks for.

🔑 **So run round 4 as a two-generation A/B: the same text on Nano Banana Pro first, then on
Nano Banana 2.** Pro goes first only on **continuity** — `1m-2`, `1m-7`, `1m-8` and `1m-m` were
made on it and these frames cut at about one a second, where a look shift would show.
⬜ **Record which one won.** Our own measured result outranks every leaderboard row, and it
settles the default for the rest of the film.
⚠️ **Never Nano Banana 2 Lite** — it is the small tier and it is the silent default in the picker.

Google's own field order —
*Subject · Action · Location · Composition · Style*, with constraints last — is what this block
already uses `[vendor]`; take their structure and not their example style words, because
*"cinematic"* is on our [quality-word kill list](../../google-flow/nano-banana-2.md#️-the-quality-word-kill-list-now-includes-cinematic).

**Check these five on the result, worst first:** the slot between the doors is actually narrow ·
the lift is off the centre axis · he has exactly one jacket and it is on him · the three leavers
are three different people · the floor is carpet and does not reflect.

⬜ **If the likeness does not bind,** switch the lens to 85mm from the same standing position and
change nothing else. **Do not add words about his face.**

**Paste into:** Flow → the image prompt box. **Model:** Nano Banana Pro (check the picker — Lite
is the silent default). **Aspect:** 16:9. **Resolution:** 2K. **Character:** `@2008 - tarquin`.
**No reference image.**

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. It is late evening, and he is going up while three people carry their belongings out.

Camera: a 35mm lens held at hip height by someone hurrying across the lobby, so the camera sits low and the grey carpet fills the bottom of the picture. It is well over to the left of the lift doors, which run away to the right at an angle, so no wall in the room is square to the lens, and the frame is very slightly tilted. Nearest the lens, two stacked cardboard archive boxes left on the carpet cross the bottom left corner, dark and thrown completely out of focus so that they are a soft blur.

Subject: the lift lobby of an ordinary City of London office tower at night, worn rather than grand — three brushed stainless lift doors set into a matt painted wall, scuffed kick plates, grey carpet tiles with a worn track across them, a dented skirting board, a red fire extinguisher on a bracket. The lobby lights are down to their night setting and only a few dim fittings are still on at the back.

Action: the nearest lift car is lit and its two doors have almost met. What is left between their leading edges is a tall narrow slot about a quarter of the doorway's full width, so the lit interior reads as a bright vertical band rather than as an open doorway. The doorway is seen from its left side, so it leans rather than sitting square to the lens.

Him: the man from the character reference is inside that band, seen from the waist up, facing out, with the doors hiding everything to either side of him. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples. He wears his suit jacket, done up, over a shirt and tie, and carries nothing over his arm. One hand is still up at the button panel on the side wall of the car, the fingers just coming off it, because he has this second pressed a button. The other hand holds a small black handset with a keyboard, low and forgotten. His eyes are aimed just past the nearest of the people in front of him, at nothing in particular — lids relaxed, brows level, lips closed. Nothing in his face is reacting to them.

In front of him: three people walk away from the camera across the lobby to the right, into the dark, carrying their things out, strung out at different distances rather than walking together. Nearest is a woman in her forties in shirtsleeves, a coat over one arm and a bulging canvas holdall on the other shoulder, caught mid-stride with one heel off the carpet. Further back is a broad man in his fifties, grey and thinning on top, carrying a plain brown cardboard box level in both arms. Furthest and almost lost in the dark is a slight man in a knitted jumper holding a potted desk plant and a framed picture against his chest. All three are seen squarely from behind, so the backs of their heads face the lens.

Light: the fluorescent panel in the ceiling of the lift car is the only strong light in the picture. It is directly above him, lighting the top of his head, his shoulders and the tops of his cheekbones and leaving his eye sockets and the underside of his jaw in shadow. It throws one narrow hard-edged wedge of light out through the gap and across the carpet toward the bottom right of the frame, and the three people crossing that wedge are near-black shapes cut out against it. The picture is exposed for the inside of the car: the front of his shirt clips to featureless white, while the lobby around them keeps a trace of detail in the deep shadow rather than going to solid black.

Style: a newspaper photograph of the 2008 financial crisis, taken on a Canon EOS-1D Mark III by available light with no flash at ISO 3200 — coarse digital noise in the shadows, muted cool colour, and no retouching or skin smoothing.

Constraints: the lift car's ceiling panel is the only light source in the picture, and the floor indicator above the doors is above the top edge of the frame. The lobby is worn and ordinary — carpet tiles rather than stone, a matt painted wall rather than marble, and a floor that reflects nothing. He wears one jacket and it is on his body, and he is the only person in the picture wearing a suit jacket. The three people walking away are seen only from behind, so his is the only legible face in the picture. He is twenty-five years old. His expression stays small and unbothered — a stranger looking at this photograph would not be able to say what he is feeling at all. The cardboard boxes are plain brown with nothing printed on them, and there are no brand names, logos or readable labels anywhere, including on the handset. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

### 1m-l — round 4, **policy block** (Jack, 2026-09-13) · 🔴 *and it disproves the round-2 diagnosis*

**Round 4 removed every machinery-plus-body-part phrase and blocked anyway.** So
[A5c](../../flow/failure-modes.md#a5c-trigger-5s-other-half--machinery-plus-a-named-body-part-inferred-untested)'s
*"crop him at both arms"* was **not the cause**, or not the whole one. That entry is now corrected
rather than confirmed.

🔑 **The diff is now much sharper, because there are two blocked rounds and one that passed.**
Round 1 generated. Rounds 2 and 4 both blocked. **The cause is almost certainly in what rounds 2
and 4 SHARE and round 1 lacks** — everything unique to either blocked round is cleared by the
other's failure, and everything in round 1 is cleared outright.

**That intersection is small, and one item in it is much bigger than the rest:**

| Shared by both blocked rounds, absent from round 1 | Read |
| --- | --- |
| 🔴 **The three leavers became individuated people** — *a woman in her forties in shirtsleeves*, *a broad man in his fifties, grey and thinning on top*, *a thin young / slight man in a knitted jumper* | **Prime suspect.** Round 1 described three anonymous shapes carrying things. Rounds 2 and 4 describe **aged, gendered, individuated people being made to carry their possessions out of a building into the dark** — which is [trigger 3](../../flow/failure-modes.md#a5-the-five-triggers-badcodes-own), *stacked destitution*, arriving by accumulation rather than by any one word, and sitting next to a named real event. The individuation we added for [crowd realism](../../google-flow/nano-banana-2.md#-crowd-realism-is-individuation-not-adjectives-practitioner) is the same edit that turned a composition into an eviction |
| 🟡 *a **bulging** canvas holdall on the other shoulder* | A word with a body-adjacent second reading, attached to a woman and a body part in the same clause. Textbook [A5b](../../flow/failure-modes.md#a5b-the-bedroom-problem--trigger-5-in-detail) shape. Not in round 1 |
| 🟡 *a woman in her forties in **shirtsleeves*** | *In shirtsleeves* literally means **without** an outer garment. On a woman, in a prompt the filter is already primed for, it is a clause we do not need |
| 🟡 *He wears one jacket and it is **on his body*** | *Body* as a bare noun in a constraints list, for no gain — *he is wearing it* says the same thing |
| ⬜ The lobby in `Subject:`, the object occluder, the button press, the scoped negations | Structural, no keyword surface. **Kept** |

⚠️ **Two more cut on the do-not-defend posture, both unique to round 4 and therefore not
suspects — they are simply free:** *held at **hip** height* and *one **heel** off the carpet*.
Body nouns bought nothing.

🔑 **A block is free, and that changes the economics of the search.** Flow's card says *"You have
not been charged for this generation."* A [binary search by subtraction](../../flow/failure-modes.md#a4-the-debugging-procedure)
therefore costs **minutes, not credits** — so if round 5 still blocks, stop guessing and run the
ladder below. **Two inferred diagnoses have now failed; the next one should be measured.**

### 1m-l — round 5 · **still** · written 2026-09-13, unrun · *supersedes round 4*

**Round 5 is round 4 with the whole suspect set cut in one pass**, per
[A5b](../../flow/failure-modes.md#a5b-the-bedroom-problem--trigger-5-in-detail)'s posture: on a
prompt the filter is already primed for, do not spend generations defending a clause you do not
need. **Every structural fix is kept** — the lobby in `Subject:`, the off-axis geometry, the slot
told as a band of light, the object occluder, the three-clause `Style:` block.

🔑 **The one change that matters: the leavers are individuated by what they CARRY, not by who
they ARE.** No ages, no genders, no builds — distance, garment and object do the work, plus
*"no two of them are the same height"*. That is what
[crowd realism](../../google-flow/nano-banana-2.md#-crowd-realism-is-individuation-not-adjectives-practitioner)
actually asked for, and it keeps the cost in frame without describing a queue of displaced people
in words.

⚠️ **The face-age block stays.** It is cleared by round 1 and he has read mid-thirties twice
without it. It is the **last** thing to cut, not the next.

**Paste into:** Flow → the image prompt box. **Model:** Nano Banana Pro first, then the same text
on Nano Banana 2 — [the A/B is open](#-model-pro-or-nb2-is-now-an-open-ab-not-a-settled-call--corrected-2026-09-13).
**Aspect:** 16:9. **Resolution:** 2K. **Character:** `@2008 - tarquin`. **No reference image.**

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. It is late evening, and he is going up while three people carry their things out.

Camera: a 35mm lens held low, about a metre off the floor, by someone crossing the lobby at speed, so the grey carpet fills the bottom of the picture. It is well over to the left of the lift doors, which run away to the right at an angle, so no wall in the room is square to the lens, and the frame is very slightly tilted. Nearest the lens, two stacked cardboard archive boxes left on the carpet cross the bottom left corner, dark and thrown completely out of focus so that they are a soft blur.

Subject: the lift lobby of an ordinary City of London office tower at night, worn rather than grand — three brushed stainless lift doors set into a matt painted wall, scuffed kick plates, grey carpet tiles with a worn track across them, a dented skirting board, a red fire extinguisher on a bracket. The lobby lights are down to their night setting and only a few dim fittings are still on at the back.

Action: the nearest lift car is lit and its two doors have almost met. What is left between their leading edges is a tall narrow slot about a quarter of the doorway's full width, so the lit interior reads as a bright vertical band rather than as an open doorway. The doorway is seen from its left side, so it leans rather than sitting square to the lens.

Him: the man from the character reference is inside that band, seen from the waist up, facing out, with the doors hiding everything to either side of him. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples. He wears his suit jacket, done up, over a shirt and tie, and carries nothing over his arm. One hand is still up at the button panel on the side wall of the car, the fingers just coming off it, because he has this second pressed a button. The other hand holds a small black handset with a keyboard, low and forgotten. His eyes are aimed just past the nearest of the people in front of him, at nothing in particular — lids relaxed, brows level, lips closed. Nothing in his face is reacting to them.

In front of him: three people are walking away from the camera across the lobby to the right, carrying their things out, strung out at different distances rather than walking together. The nearest, six or seven paces off, is in a pale shirt with a dark coat folded over one arm and a canvas holdall hanging from the other, caught mid-step. Half the room further back, a figure in a dark crew-neck jumper carries a plain brown cardboard box level in both arms. The furthest is almost lost at the back of the lobby, in a light knitted jumper, with a potted desk plant under one arm and a framed picture in the other hand. All three are seen squarely from behind, so the backs of their heads face the lens, and no two of them are the same height.

Light: the fluorescent panel in the ceiling of the lift car is the only strong light in the picture. It is directly above him, lighting the top of his head, his shoulders and the tops of his cheekbones and leaving his eye sockets and the underside of his jaw in shadow. It throws one narrow hard-edged wedge of light out through the gap and across the carpet toward the bottom right of the frame, and the three people crossing that wedge are near-black shapes cut out against it. Past them the far end of the lobby falls away to nothing. The picture is exposed for the inside of the car: the front of his shirt clips to featureless white, while the lobby around them keeps a trace of detail in the deep shadow rather than going to solid black.

Style: a newspaper photograph of the 2008 financial crisis, taken on a Canon EOS-1D Mark III by available light with no flash at ISO 3200 — coarse digital noise in the shadows, muted cool colour, and no retouching or skin smoothing.

Constraints: the lift car's ceiling panel is the only light source in the picture, and the floor indicator above the doors is above the top edge of the frame. The lobby is worn and ordinary — carpet tiles rather than stone, a matt painted wall rather than marble, and a floor that reflects nothing. He is wearing exactly one jacket and he is the only person in the picture wearing a suit jacket. The three people walking away are seen only from behind, so his is the only legible face in the picture. He is twenty-five years old. His expression stays small and unbothered — a stranger looking at this photograph would not be able to say what he is feeling at all. The cardboard boxes are plain brown with nothing printed on them, and there are no brand names, logos or readable labels anywhere, including on the handset. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

#### ⬜ If round 5 blocks: stop guessing and run the ladder. Blocks are free.

Fire **round 1's exact text** (the version that generated) and add round 5's blocks back **one at
a time**, in this order — most-suspected last, so the first failure names the cause:

1. Round 1 + round 5's `Camera:` and `Subject:` blocks *(the lobby swap and the object occluder)*
2. …+ round 5's `Action:` and `Him:` blocks *(the slot-as-band, the button press, the single jacket)*
3. …+ round 5's `Light:` and `Style:` blocks
4. …+ round 5's `In front of him:` block ← **expected to be the one that fails**
5. …+ round 5's `Constraints:` block

**Whichever step fails is the answer**, and it goes in
[`failure-modes.md`](../../flow/failure-modes.md) as `[confirmed]` rather than as a third guess.
🔴 **Only if step 4 passes** does the face-age block become the suspect — cut it whole then, and
let `@2008 - tarquin` carry the age.

### 1m-l — round 5 ✅ **ACCEPTED 2026-09-13, first take, on Nano Banana 2**

**Jack: *"NB2 is better, that prompt made this image."*** Round 5 passed policy **and** came back
usable on the first generation, so the round-4 diagnosis holds up: **the demographics on the three
leavers were the block.** Individuating by garment, carried object and distance does the crowd-realism
job without describing displaced people in words.

⬜ **Master not banked** — save it as `camera/reference/1m-l-lift-doors-ACCEPTED.png`.

**✅ What landed:** the boxes as a soft foreground occluder, the three leavers reading as three
different people in silhouette with their backs to us, the wedge of light thrown diagonally across
the carpet, the worn lobby, and a face that reads twenty-five rather than mid-thirties.

🔑 **What did NOT land is the best thing about it. The doors came back fully open** —
[§38](../../google-flow/nano-banana-2.md#38--a-mechanical-in-progress-state-returns-fully-open-or-fully-shut--give-it-a-physical-analogy-observed-2026-09-12)
firing for the third time, through a physical analogy, a proportion **and** a description of the
light's shape. **Treat §38 as near-unbeatable on a still and stop paying for rounds against it.**
The open doorway is the better plate anyway, because it hands the clip its one action: **the film
does not need a photograph of doors nearly shut, it needs doors that shut.**

⚠️ **The frame came back very slightly wider than 16:9** with thin bars at the sides. **Crop in
Premiere; never mention bars in a prompt** —
[§31](../../google-flow/nano-banana-2.md#31--27-catches-the-output-frame-too-no-letterbox-bars-produces-letterbox-bars-observed-2026-09-08-n3).

### 1m-l — the clip · **video** · written 2026-09-13, unrun

**Recorded despite the [2026-08-26 stills-only ruling](#conventions)**, on the same grounds as
`1m-m`'s: it carries a routing call, a documented morph risk that is three-figures wide, and one
deliberate rule-break that needs its reasoning kept.

**Routing:** Omni Flash → **Frames** tab, the accepted `1m-l` frame as the **start frame**.
**Duration 6s.** 🔴 **End slot EMPTY.** Omni 1.1 Flash added end frames on 2026-08-27 `[vendor]`
and it is tempting here — but the house rule stands: **never pin an `endImage`, it morphs**
([`hybrid-method.md`](../../video-fx/hybrid-method.md)). The doors have a stable destination
without one.

🔴 **Frames, and no Character** — the same call as
[`1m-m`](#1m-m--the-clip--video--written-2026-09-12-unrun), for the same two reasons. The
staging **is** the shot (the wedge, the occluder, three figures at three distances), and
[Ingredients re-stages](#-the-tab-rule--amended-2026-08-18-ingredients-holds-identity-frames-holds-staging).
And the plate is now **the only authority on a face that finally reads twenty-five** — attaching
`@2008 - tarquin`, which has come back mid-thirties twice, would put an older second authority on
it. The tab rule's *"a face in the shot → Ingredients"* line is overruled by its own **both** row:
staging failure is unrecoverable, and his motion here is near-zero, which is that row's stated
precondition.

#### 🔑 The design: the doors perform the cut

[A clip whose first and last frames match reads as a photo, not a shot](../../cinematography/stills.md#1-what-makes-a-still-hold),
and this one has exactly one event — **the doors close and take the light with them.** The wedge
on the carpet narrows to a band, to a strip, to a line, and goes out.

Three reasons it is the right single action:

- **It is the beat.** *"…this prick stands without a scratch"* — he is sealed into a lit box and
  the room the cost is standing in goes dark. No narration needed.
- 🔑 **It is a transition made in camera.** The shot ends in near-black, so it cuts to anything.
  ⬜ **Worth considering in the edit: use it as the montage's exit** rather than as another
  one-second frame — the cutting accelerates, then this one shot plays out and takes the light
  away. That is a human call and it changes the montage's shape, so it is Jack's, not this file's.
  *(The standing plan has `1m-8` as the button —
  [2 → 7 → 8 is the complete argument](./shot-list.md).)*
- 🔑 **It hides the risk.** See below.

#### 🔴 The top risk is the three walkers, and the doors are the mitigation

`[observed 2026-08-26]` **On Frames, a walking extra morphs** — camping `5a` held a car perfectly
and the people changed anyway, because [Frames holds pixels, not people: the moment a person
moves, they are being generated](#-on-frames-a-walking-extra-morphs--stillness-is-the-only-thing-that-holds-them-observed-2026-08-26).
**This plate has three of them, all mid-stride.** The repo's stated fixes are hold them still,
demote them to sound, or crop them out — and **all three are unavailable**, because the leavers
walking away *is* [gate 2's visible cost](../../../.claude/skills/shot-craft/SKILL.md) and the
frame fails without it.

**Two things carry it instead, and the second is the reason to spend the credit:**

1. ⚠️ **They are near-black silhouettes.** A morph is a redraw failure, and a cut-out shape with
   no internal detail has very little to get wrong — no face, no hands, no garment seams.
   🔴 **Inferred, not measured:** `5a`'s pedestrian was lit. **If they morph anyway, that is a
   finding worth writing up**, because it would mean silhouetting does not buy what it looks like
   it should.
2. 🔑 **The shot's own event removes them.** Their only light is the wedge from the lift. As the
   doors close, the wedge narrows and they lose their backlight — **so by the second half of the
   clip the elements most likely to fail are unlit.** The risk and the runtime run in opposite
   directions, which is the whole reason this shot is cheap to attempt.

#### ⚠️ One rule is deliberately broken, and here is the cover

[**Ask it to *continue* a state, never to *reach* one**](#-ask-it-to-continue-a-state-never-to-reach-one-observed)
is the house rule, and *"the doors close"* is a state change by definition — there is no way to
write this shot that obeys it.

🔑 **The cover is that the prior is with us for once.** `[observed 2026-08-26]`
[a hinged thing given any general instruction to move settles shut and stays shut](#-a-hinged-thing-given-wind-will-settle-shut-and-stay-shut-observed-2026-08-26)
— camping `6a` lost a tent doorway to exactly this. **Closed is the engine's own attractor state.**
Here that failure mode and the brief are the same thing, so the model is being asked to do what it
already wants to do. It is the one shot in the film where 6a's bug is free labour.

#### ⚠️ The shutter clause is deliberately absent

The [24fps / 180° shutter token](#the-shutter-is-the-tell-nobody-prompts-for) is on nearly every
BadCode clip, and it is **subtracted here on the file's own instruction**: it is for shots with
*fast* motion, and on a near-static clip it is
[a word that buys nothing](#-biological-motion--the-anti-slop-clause-for-any-shot-of-a-person-doing-nothing).
Sliding doors and three people walking are both slow. **The biological-motion clause replaces it**
— he breathes and blinks once, because a held shot of a person doing nothing is precisely where
that tell fires.

⚠️ **Every instruction is positive.** No *"he does not step forward"*, no *"they do not turn"* —
[negatives backfire](#-negatives-do-not-work-and-they-actively-backfire), and each one would name
the unwanted action into the shot. The only negation kept is `No music and no voices.`, which is
`[confirmed]` working on 8b-fog.

#### ⬜ Draft at 360p first — half credits, and it is this shot's exact use case

[The 360p draft is a **motion** check](#-the-360p-draft-is-a-motion-check-never-a-text-check--and-upscaling-repairs-nothing):
morphing figures and hinging surfaces, which is this clip's entire risk surface. **Ignore the face,
the texture and the grain in it.** If the doors travel and the three silhouettes hold, promote to
720p — that is the native ceiling, and 1080p/4K are upscales.

**Paste into:** Flow → **Frames to Video** prompt box. **Start frame:** the accepted `1m-l` image.
**End frame:** empty. **No Character, no Ingredients.** **Duration:** 6s. Primary:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts. The camera is locked off and holds completely still throughout.

The lift doors slide shut. They run in from both sides at the steady even speed of a real lift door, and the wedge of light lying across the carpet narrows as they come — to a band, then a strip, then a thin line that goes out, leaving the lobby in near-darkness.

He stays exactly where he is and rides up. He breathes, blinks once, and goes on looking past the people in front of him, and his expression holds as it is.

The three people carry on walking away from the camera at the same steady pace, their backs to the lens the whole time, and the dark takes them as the light leaves.

The boxes, the carpet, the walls and the fire extinguisher stay exactly where they are.

Audio: the hum of the lift motor, the doors running in their tracks and a soft clunk as they meet, footsteps going away on carpet, and the low hum of an empty building at night. No music and no voices.

Thanks.
```

⬜ **Fallback, only if the primary comes back diluted or re-staged** — same tab, same start frame:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. Camera locked off, one continuous shot, no cuts.

The lift doors slide shut at the steady speed of a real lift door, and the wedge of light on the carpet narrows with them to a thin line and goes out. He stays where he is, breathes and blinks once. The three people carry on walking away with their backs to the lens, and the dark takes them.

Audio: the lift motor, the doors running and meeting, footsteps going away on carpet. No music and no voices.

Thanks.
```

**Post, in Premiere:**

1. ⬜ **Crop off the side bars** the plate came back with — this clip inherits them from frame 0.
2. ⬜ **Any camera move is here, not in Flow** ([`hybrid-method.md`](../../video-fx/hybrid-method.md)) — though this shot wants none: the doors are the move.
3. **Match the grain rather than stacking it** — the plate already carries ISO-3200 press-DSLR noise.
4. ⚠️ **Watch the three silhouettes on playback**, not the doors. If a figure gains a limb, changes height or swaps what it is carrying, that is the `5a` morph firing through a silhouette — **a re-roll, not a grade**, and it goes in [`omni-flash.md`](../../google-flow/omni-flash.md) as a finding.
5. ⚠️ **Nothing ships unmeasured** — `scripts/delivery-qc.sh`
   ([`delivery.md`](../../video-fx/delivery.md)). This shot ends in near-black, which is the exact
   condition that crushed `camping.mp4`.

**Sources for this entry (2026-09-13):**
[Flow models & supported features](https://support.google.com/flow/answer/16352836) `[vendor]` ·
[Flow by Google — end frames in Omni 1.1 Flash](https://x.com/FlowbyGoogle/status/2093011783649001870) `[vendor]` ·
[Magic Hour — realistic AI video prompting, 10 pillars](https://magichour.ai/blog/realistic-ai-video-prompting) `[community]` ·
[Promptessor — image-to-video, the "living still"](https://promptessor.com/blog/image-to-video-prompts-how-to-animate-photos-products-characters-and-art-in-2026) `[community]` ·
[Prompt Architects — still-image-to-video handoff prompts](https://prompt-architects.com/blog/242-from-still-image-to-ai-video-handoff-prompts) `[community]`

**Sources for this entry (2026-09-13):**
[Google Cloud — ultimate prompting guide for Nano Banana](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) `[vendor]` ·
[Max Woolf — Nano Banana Pro, with caveats](https://minimaxir.com/2025/12/nano-banana-pro/) `[practitioner]` ·
[Pixova — how to make AI images look less like AI](https://www.pixova.io/blog/how-to-make-ai-images-look-less-like-ai) `[community]` ·
[Miraflow — prompt tricks that actually work](https://miraflow.ai/blog/how-to-make-ai-images-look-like-real-photos-prompt-tricks) `[community]` ·
[Hedra — make AI images look like real photos](https://www.hedra.com/blog/make-ai-images-look-like-real-photos-prompting) `[community]`


### 1m-t — the treadmill · **still** · written 2026-09-13, unrun

**Jack's ask, 2026-09-13:** *"him on a treadmill on the phone with an annoying headset as he runs."*

⚠️ **It is still September 2008, not the 1980s.** The montage is called *the 80s job montage*
because Jack asked for 80s **grammar** — flash frames cut on the beat — and its content is the week
the banks failed. **A treadmill frame set in 1985 would break the year device.** The naff ear-hook
Bluetooth earpiece is perfect *because* it is 2008, not despite it.

#### The job: every other frame is him at a desk or leaving one. This is the one where he does not stop

🔑 **And the gag is free geometry: he is running flat out toward a city he never gets to.** The
black glass wall is a metre in front of him with the City's lights beyond it, and he does not move
an inch. Nothing in the prompt has to say that; the room says it.

**Where it sits:** proposed under *"Leveraged E.T.F.s. If you do not understand that, it is rather
the point."* A man barking acronyms into an earpiece at a dead run **is** that line.
⬜ **Human call: it could replace [`1m-6` "two phones"](./shot-list.md)**, which is unmade and needs
a Premiere split-screen to work at all. `1m-t` makes the same argument in one frame with no post.

#### 🔴 Gate 2: the cost is the cleaner, and it is a KIND the montage has not used

The [standing rule on this montage](./shot-list.md) is that **each frame's cost is a different kind**
— a silent room, a broken body, an exodus with boxes — because cloning the cost builds nothing.
Used so far: wreckage underfoot, red columns, a stripped desk, an eviction, empty desks, a bowed
man, three leavers.

**This one is the labour nobody photographs.** Someone in a maintenance uniform working at the far
end of the room at five in the morning, wiping a machine down, mop bucket beside them — the person
who makes the room he is running in, who will never be on the call he is taking. It is
[`the-reader.md`](../../marketing/the-reader.md)-shaped: the frame names who is actually working.

🔑 **And the round-4 lesson is applied directly: no age, no gender, no build.** The cleaner is
individuated by **uniform, task, equipment and distance** only. That is what
[crowd realism](../../google-flow/nano-banana-2.md#-crowd-realism-is-individuation-not-adjectives-practitioner)
asked for, and it is the phrasing that
[got `1m-l` through after two refusals](#1m-l--round-4-policy-block-jack-2026-09-13---and-it-disproves-the-round-2-diagnosis).

#### 🔴 Celebration risk is high and named

[Principle 24](../../cinematography/principles.md): the rich-trader-at-the-gym montage is
**American Psycho's** own grammar, and meaning it ironically does not protect us. Four guards, and
none of them is a caption:

1. **He is going nowhere.** The frame's literal content is effort without travel.
2. **The flash is unflattering** — a hard frontal press flash at 5am, not gym-brand key light.
   ⚠️ **Deliberately NOT the [fitness-photography register](https://miraflow.ai/blog/ai-prompts-fitness-brand-content-gym-ready-visuals-2026)**
   the web will hand you for this subject: *"cinematic sports lighting"*, *"sweat sheen"* and
   *"professional colour grading"* are aspirational-advertising words and every one of them is on
   our [quality-word kill list](../../google-flow/nano-banana-2.md#️-the-quality-word-kill-list-now-includes-cinematic).
3. **His body is never described.** No physique, no definition, no adjectives about how he looks —
   which is both the celebration guard and the
   [cosplay/hyperreal failure](https://minimaxir.com/2025/12/nano-banana-pro/) guard `[practitioner]`.
4. **`Constraints:` bounds the face from above**, as on every montage frame: a stranger reads
   effort and concentration before they read triumph.

#### 🔑 The one detail the frame turns on: he is talking, not breathing

He is **mid-sentence**, not gasping. A man who can hold a deal at that pace is the whole character
in one observation, and it is the difference between this and a fitness photograph.

#### ✅ Craft levers used, and one refused

- **Three depth planes, foreground first** — the next machine's handrail crossing the bottom
  corner, dark and out of focus. It is the named fix for flatness
  ([symptoms.md](../../cinematography/symptoms.md)) and `[community]` guidance says the same:
  *blurred foreground, subject midground, distant element background*.
- 🔑 **The flash freezes flying sweat, and that is period-correct rather than a gloss.** An
  on-camera flash at 1/1000s stops droplets in the air, which gives the frame
  [implied motion in a still](https://miraflow.ai/blog/ai-prompts-fitness-brand-content-gym-ready-visuals-2026)
  `[community]` without any fitness-advertising vocabulary. The belt and the deck carry a faint
  ambient smear under the same drag-shutter clause
  [`1m-m` used](#1m-m--champagne-in-a-coffee-mug--still--written-2026-09-12-unrun).
- ✅ **`visible pores, not airbrushed`** — `[community]` names this as *the* clause that stops the
  waxy default, and it earns its place here because a sweating face at flash range is the one
  frame in the montage where skin is the largest thing in view.
- 🔴 **Refused: the mirror wall.** A gym mirror would double him — *him running beside himself,
  going nowhere twice* — and it is a good idea that this engine cannot be trusted with.
  Reflections come back *"very strange"* `[observed]`, and a mirrored figure is a
  [duplicate-subject](../../google-flow/omni-flash.md#-a-multi-waypoint-trajectory-duplicates-the-subject-observed-2026-08-26)
  invitation. **The black window carries the same meaning with no reflection asked for.**
- ⚠️ **No marque on anything** — the treadmill, the earpiece and the handset are described and
  never named ([§34](../../google-flow/nano-banana-2.md#34--naming-a-marque-renders-its-badging-and-no-downstream-constraint-removes-it-observed-2026-09-08)).
- ⚠️ **§35's confirmed flash recipe:** the hardware is named in `Style:`, the light is described
  only as consequences in `Light:`, and the source positions are pinned in `Constraints:`.

#### ⚠️ Policy audit before firing — a gym is an A5b setting

[A5b](../../flow/failure-modes.md#a5b-the-bedroom-problem--trigger-5-in-detail): *the setting
supplies the other reading.* A room full of bodies and sweat is exactly that shape, so the block was
read back asking which words look bad quoted next to *gym*. **Written out:** any description of his
build, *glistening*, *sheen*, *soaked through*, *bare*, and every garment word beyond the two
needed. **Kept:** *the front of his top is dark with sweat*, which is
[`1m-m`'s exact passing phrasing](#1m-m--champagne-in-a-coffee-mug--still--written-2026-09-12-unrun).

**Model:** **Nano Banana 2** — it made the accepted `1m-l` first take, and that measured result
outranks the leaderboards either way. **Check the picker; Lite is the silent default.**
**Paste into:** Flow → the image prompt box. **Aspect:** 16:9. **Resolution:** 2K.
**Character:** `@2008 - tarquin`. **No reference image.**

**Check these five on the result, worst first:** he is mid-word rather than gasping · the row of
machines runs away at an angle rather than square-on · the cleaner is present and far off ·
nothing in the room carries a logo or a readable number · the window is black with distant lights,
not a mirror.

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. It is five in the morning. In this frame he is running hard on a treadmill in his firm's gym and doing a deal at the same time.

Camera: a 35mm lens at chest height, level, about two metres out and well over to the right, so the row of treadmills runs away to the left at an angle and no wall in the room is square to the lens. He is in the left third of the picture and the dark room carries the rest, and the frame is very slightly tilted. Nearest the lens, the handrail and console of the next machine along cross the bottom right corner, dark and thrown completely out of focus so that they are a soft blur.

Subject: the man from the character reference, seen from the knees up, running on a treadmill and facing the camera's side of the room. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples. He is in a plain dark technical running top and shorts, and the front of the top is dark with sweat.

Action: he is at a flat-out run, both feet off the deck at the top of a stride, arms driving. He is in the middle of a sentence — his mouth is open on a word, his jaw set, his chin up — and he is talking rather than gasping. One hand has come off its swing to press two fingers against a small plastic earpiece hooked over his ear. His eyes are fixed straight ahead at nothing, lower lids pushed up, brows drawn down and in. Sweat is coming off his jaw and his hairline in separate droplets that hang in the air beside his head.

On the machine: a chunky treadmill of 2008 with a moulded grey console, a row of rubber buttons and a small red dot-matrix display carrying figures too small and soft to read. A small black handset with a keyboard is propped face up on the console shelf. A folded towel hangs over the rail.

Behind him: the gym is a long dark room at the end of the night, the ceiling lights down to a few dim fittings. A row of unused treadmills and weight machines recedes into the dark to the left. At the far end of the room, small and a long way off, someone in a maintenance uniform is wiping down a machine with a cloth, a mop bucket on wheels beside them, their back to the lens. Beyond the machines a floor-to-ceiling window is a flat black rectangle with a scatter of distant office lights in it.

Light: the photograph was taken with a flash on top of the camera, fired straight at him. He is the brightest thing in the picture — a flat hard light across the front of his top and one side of his face, and a crisp dark shadow of his arm thrown onto the machine beside him. The wet patches on his top clip to featureless white where the flash hits hardest, while the shadowed side of his face keeps its detail rather than going to solid black. The droplets in the air beside his head are lit and frozen sharp. The flash does not reach far: four metres back the room is only a dim wash from the ceiling fittings, and the far end falls away to almost nothing, so the person working down there is a near-black shape. The shutter stayed open after the flash fired, so the running belt and the deck under his feet are smeared into a blur while he is frozen.

Style: a newspaper photograph of the 2008 financial crisis, shot on a Canon EOS-1D Mark III with a Speedlite — fine digital noise in the shadows, a cool cast from the ceiling fittings, muted colour, and visible pores rather than airbrushed skin.

Constraints: the only light sources are the camera's flash, which is behind the lens, and the ceiling fittings, which are above the top edge of the frame. The window at the far end is a flat black rectangle holding only distant lights, and nothing in the room reflects anything. The person working at the far end is seen only from behind, so his is the only legible face in the picture. He is twenty-five years old, and his build is not the subject of the photograph. His expression stays small — a stranger looking at this photograph would read effort and concentration before they read either triumph or distress. No brand names, logos or readable labels anywhere, including on the machine, the earpiece and the handset. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

**Sources for this entry (2026-09-13):**
[Vofy — Nano Banana 2 photorealistic image generation](https://www.vofy.art/blog/nano-banana-2-photorealistic-image-generation) `[community]` ·
[Leonardo.Ai — Nano Banana prompt guide](https://www.leonardo.ai/news/nano-banana-prompt-guide) `[community]` ·
[Miraflow — gym-ready visuals](https://miraflow.ai/blog/ai-prompts-fitness-brand-content-gym-ready-visuals-2026) `[community]` *(cited for the implied-motion lever; its lighting vocabulary is rejected above)* ·
[Wearview — how to fix AI skin texture](https://www.wearview.co/blog/fix-ai-skin-texture) `[community]` ·
[Max Woolf — Nano Banana Pro, with caveats](https://minimaxir.com/2025/12/nano-banana-pro/) `[practitioner]`

### 1m-t — round 1 ✅ **ACCEPTED 2026-09-13** (Jack) · with two recorded flaws

⬜ **Master not banked** — save it as `camera/reference/1m-t-treadmill-ACCEPTED.png`.

**✅ What landed:** the cleaner reads immediately — uniform, cloth, wheeled cart, back to the lens,
far off and small, so **gate 2 is satisfied by a kind of cost the montage has not used**. The sweat
frozen in the air beside his head is the best detail in the frame. The belt smeared while he is
sharp — the drag-shutter clause worked. Mid-word rather than gasping, left third, the row running
away at an angle, a black window with distant lights, real falloff to the back of the room.

🔴 **Flaw 1 — the treadmill geometry is wrong.** He is running a metre and a half forward of his own
console, so his machine reads as impossibly long and the next machine's handrail crosses his thighs.
**Accepted knowingly:** at ~1s in a flash montage the eye reads *treadmill* and goes to his face
long before it parses the machine. ⚠️ **It stops being harmless in the clip** — see the design note
below, where it is the reason for one specific clause rather than a reason to re-shoot.

⚠️ **Flaw 2 — the light came back ambient, not flash.** No hard frontal pop, no crisp arm shadow,
no clipped highlight. Cut beside `1m-2` and `1m-m` this frame is in a slightly different register.
**Accepted:** the montage already carries two deliberate non-flash frames (`1m-7`, `1m-l`), and a
5am gym under its own ceiling fittings is a legitimate look. **Recorded so it is a known choice and
not a drift nobody noticed.**

⬜ **The foreground occluder never happened** — bottom right came back in focus. The blurred belt
at bottom left does about half the job. Not worth a generation.

### 1m-t — the clip · **video** · written 2026-09-13, unrun

**Routing:** Omni Flash → **Frames** tab, the accepted `1m-t` frame as the **start frame**.
🔴 **End slot EMPTY** — [never pin an `endImage`, it morphs](../../video-fx/hybrid-method.md).
🔴 **No Character, no Ingredients** — the staging is the shot and the plate is the only authority on
the face, the same call as [`1m-l`](#1m-l--the-clip--video--written-2026-09-13-unrun) and
[`1m-m`](#1m-m--the-clip--video--written-2026-09-12-unrun).

**Duration: 4 seconds.** 🔑 **Deliberately shorter than `1m-l`'s 6s, and for a stated reason.**
`1m-l` needed runtime because the door travel *was* the event; this shot's event is a **loop**, so
[the eighth pass applies exactly](../../google-flow/omni-flash.md#eighth-pass--2026-09-11-vendor-community):
*for a montage beat cut to ~2s, generate 4s — fewer frames means less drift, and nothing is lost.*
Running legs are the highest-drift content in the montage, so buying fewer frames is buying quality.

#### 🔑 The design: the shot is a man going nowhere, so nothing may translate

The one action is **he keeps running**. Everything else is pinned. And the clip's single most
important clause is the one that says **he stays in the same place in the frame** — which is not a
technical note, it is the entire joke. He is running flat out toward a city a metre away and the
distance never changes.

#### 🔴 Top risk: running legs are the worst case this engine has, and the fix is the shutter

`[community]` **The named human-motion failures are exactly ours:** *"feet slide across the floor
like there's no friction"*, *"arms swing at the wrong tempo"*, *"fingers merge together between
frames"*, and floating limbs
([AtlasCloud](https://www.atlascloud.ai/blog/tips/mastering-kling-3.0-10-advanced-ai-video-prompts-for-realistic-human-motion)).
Independent artifact work sorts AI-video faults into four buckets, of which **movement/joint
anomalies** is one ([arXiv 2504.21334](https://arxiv.org/pdf/2504.21334)) `[academic]`.

**Four clauses answer it, and the first is the one that matters:**

| The failure | The clause |
| --- | --- |
| 🔑 **Morphing legs / broken plate geometry** | **The [24fps 180° shutter clause](../../google-flow/omni-flash.md#the-shutter-is-the-tell-nobody-prompts-for), and here it is load-bearing rather than decorative.** At that cadence a sprinting leg *is* a smear — and **a blur cannot visibly morph**. It is the same reasoning as [a dropped object being a streak rather than a crisp phone in four positions](../../google-flow/omni-flash.md#the-rule-that-outranks-all-of-it-a-real-camera-never-catches-the-whole-fall), `[confirmed 2026-08-14]`. 🔑 **It also swallows flaw 1**: the plate's wrong machine geometry is least legible when the legs and deck are smeared, which is why the answer here is the shutter and **not** a crop |
| **Gliding / sliding feet** | `[community]` names the fix: **state the foot contact** — *comes down under him and rolls through from heel to toe*. A named landing is the documented counter to the gliding-walk artifact |
| **Arms at the wrong tempo** | *his free arm drives in time with his stride* — the tempo is tied to something already in frame rather than left free |
| **Morphing hands** | 🔑 **His other hand does not move at all.** It stays pressed to the earpiece for the whole shot — which removes a moving hand from a clip that would otherwise have two, and is characterful: he is straining to hear over his own running |

⚠️ **This is the exact inverse of the [`1m-l` call](#1m-l--the-clip--video--written-2026-09-13-unrun),
where the shutter clause was deliberately subtracted.** That shot was slow — doors and walking — and
the clause buys nothing on near-static motion. This one is the fastest thing in the film. **Same
rule, opposite answer; the rule is about the motion, never about the house style.**

#### ⚠️ The sweat droplets are deliberately not mentioned

They are the best detail in the still, and asking for them would be asking for two things that
fight: **the same shutter clause that saves the legs erases a flying droplet**, and
[particle nouns have no volume control](../../google-flow/omni-flash.md#-particle-nouns-have-no-volume-control-observed-n2)
`[observed, n=2]`, so a request risks a shower. **Silence lets frame 0's droplets do whatever they
do at no cost.** The lever is subtraction.

#### ⚠️ The cleaner works in place — no translation, ever

[On Frames a *walking* extra morphs](../../google-flow/omni-flash.md#-on-frames-a-walking-extra-morphs--stillness-is-the-only-thing-that-holds-them-observed-2026-08-26)
`[observed]`, because a person crossing ground has to be redrawn in positions the plate never
showed. **A person working on the spot is much closer to pixels being continued.** So she is given a
small repeated local action, her position is pinned positively, and she never takes a step. This is
a softer ask than `1m-l`'s three walkers and should be safer — ⬜ **and if it still morphs, that is
worth writing up**, because it would bound the finding to *motion* rather than to *translation*.

#### ⚠️ He is visibly talking and there must be no voice

House rule: [never dialogue in a Flow video](../../google-flow/omni-flash.md#-the-speech-trap-is-punctuation-not-vocabulary).
`[2026-09-09]` **the speech trap is punctuation, not vocabulary** — a colon or a quotation mark
followed by words is what produces speech, not the verb *talk*. So *"he goes on talking"* is safe as
plain prose, carries no words, and is paired with the `[confirmed]` `No music and no voices.` line.
**The narration sits over this frame anyway**, and silence under it is correct.

#### ⬜ Draft at 360p first

[A motion check, never a text or face check](../../google-flow/omni-flash.md#-the-360p-draft-is-a-motion-check-never-a-text-check--and-upscaling-repairs-nothing).
**Watch three things and nothing else:** his feet make contact rather than gliding, the cleaner stays
put, and he does not drift forward or back in frame. Ignore the face, the console and the grain.

**Paste into:** Flow → **Frames to Video** prompt box. **Start frame:** the accepted `1m-t` image.
**End frame:** empty. **No Character, no Ingredients.** **Duration:** 4s. Primary:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts. The camera is locked off and holds completely still throughout, and the light stays exactly as it is.

He keeps running at the same flat-out pace. Each foot comes down under him on the belt and rolls through from heel to toe before it leaves again, and the belt carries it away behind him, so he stays in the same place in the frame the whole time. His free arm drives in time with his stride. His other hand stays pressed to the earpiece for the whole shot. He goes on talking, his eyes fixed straight ahead, and his expression holds as it is.

At the far end of the room the person in the maintenance uniform goes on wiping the same machine, staying exactly where they are with their back to the lens.

The other machines, the towel over the rail, the handset on the console shelf, the window and the ceiling stay exactly where they are.

Shot at 24fps with a 180-degree shutter, so his legs and the running belt smear into blur while his head and shoulders stay sharp.

Audio: the slap and hum of the treadmill belt, his footfalls on the deck, hard steady breathing, and the low hum of an empty building at night. No music and no voices.

Thanks.
```

⬜ **Fallback, only if the primary comes back diluted or re-staged** — same tab, same start frame:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. Camera locked off, one continuous shot, no cuts, and the light stays as it is.

He keeps running at the same flat-out pace, each foot rolling heel to toe under him, staying in the same place in the frame. One hand stays pressed to the earpiece and he goes on talking. The person at the far end goes on wiping the same machine where they stand.

Shot at 24fps with a 180-degree shutter, so his legs and the belt smear while his head stays sharp.

Audio: the belt, his footfalls, steady breathing, the hum of an empty building. No music and no voices.

Thanks.
```

**Post, in Premiere:**

1. ⚠️ **Watch the feet on playback, not the face.** Gliding — a foot that slides rather than plants —
   is the failure this clip is designed against, and it is **a re-roll, not a grade.**
2. ⬜ **Any camera move is here, not in Flow** ([`hybrid-method.md`](../../video-fx/hybrid-method.md)).
   ⚠️ **This shot wants none.** A push-in on a man going nowhere adds travel to the one frame whose
   argument is that there is none.
3. **Match the grain rather than stacking it.**
4. ⚠️ **Nothing ships unmeasured** — `scripts/delivery-qc.sh` ([`delivery.md`](../../video-fx/delivery.md)).

**Sources for this entry (2026-09-13):**
[AtlasCloud — realistic human motion prompts](https://www.atlascloud.ai/blog/tips/mastering-kling-3.0-10-advanced-ai-video-prompts-for-realistic-human-motion) `[community]` ·
[AtlasCloud — Omni Flash 1.1 image-to-video workflows](https://www.atlascloud.ai/blog/tips/gemini-omni-flash-1.1-image-to-video) `[community]` ·
[arXiv 2504.21334 — visual artifact detection in generated video](https://arxiv.org/pdf/2504.21334) `[academic]` ·
[Flow models & supported features](https://support.google.com/flow/answer/16352836) `[vendor]`

### 1m-p — the count · **still** · written 2026-09-13, unrun

**Jack's ask, 2026-09-13:** *"tarquin watching a money counting machine count pounds from 2008…
think of the song Push It to the Limit, that's the vibe."*

#### 🔴 Read this before the prompt: the reference is the exact thing principle 24 warns about

*Push It to the Limit* **is** the good-times montage — Tony Montana's rise, ever larger bags of
money, shot to be thrilling. [Principle 24](../../cinematography/principles.md) says satire that
borrows power's grammar gets read as celebration by part of any audience, and
[principle 23](../../cinematography/principles.md) gives the only reliable counter: **a visible
cost.** Doing it knowingly is not a defence — Harron is on record being mystified that traders
adopted Bateman.

⚠️ **One thing genuinely argues for it, and it is structural rather than a let-off:** the Scarface
montage exists *to set up the fall*. Camping is the fall — the whole film is this man in a field
with a burning newspaper. **A rise montage in a film that is entirely a fall is doing the same
structural job the reference did.** That is the case for making it; it is not a case for making it
without a cost.

#### 🔑 The staging is what inverts the reference: he never touches the money

Scarface's montage has hands in cash. **Ours has a machine doing it and a man watching.** One hand
rests on top of the counter — **on the machine, never on the notes** — and that single gesture is
the film's thesis without a line of narration: the capital works, the man supervises.

**It also happens to be exactly what Jack asked for** (*"watching a money counting machine"*), so
the strongest version of this shot and the brief are the same shot.

#### 🔴 Gate 2: this frame's cost is an OBJECT, and it is the montage's subtlest

Costs used so far are all rooms and people — wreckage underfoot, red columns, a stripped desk, an
eviction, empty desks, a bowed man, three leavers, the cleaner. **A ninth person would clone the
cost rather than build it**, which the montage's [standing rule](./shot-list.md) forbids. So this
one is carried by two things in the machine:

1. **The notes are used.** Soft, creased, furred at the edges, banded in a bank's paper wrappers —
   money that came out of hundreds of pockets, not crisp sheets off a press. *Where it came from is
   in its texture.*
2. 🔑 **One note has torn, and is caught at the machine's throat with a shred of it left behind.**
   The machine damages what passes through it. It is small, it is an object, and it is the film's
   argument in one detail.

🔴 **Flagged honestly: this is weaker than `1m-l`'s three leavers or `1m-m`'s bowed man**, and gate
2 is mandatory rather than advisory. ⬜ **If Jack wants it harder, the strongest available upgrade
is a second frame, not a busier one** — cut from this to `1m-7` (the house, the locksmith, the bin
bags) and the count is retrospectively paid for. **That is an edit decision and it is free.**

#### ⚠️ The "Push It to the Limit" feeling is made in Premiere, not in this prompt

Worth saying plainly so nobody tries to buy it with adjectives. The reference's energy is **cutting
rate and music**, not a look: quick shots on the beat, rising scale. Our montage is already built
that way — [flash frames at about one a second](./shot-list.md), and
[the camera moves in Premiere, never in Flow](../../video-fx/hybrid-method.md).

**So the frame's job is to be one hard, kinetic, frozen instant**, and the vibe is bought in the
edit with a snap zoom onto the counter and a cut on the beat. 🔴 **Asking the prompt for "80s
montage energy" would buy the [aesthetic mode](../../google-flow/nano-banana-2.md#️-the-quality-word-kill-list-now-includes-cinematic)
and a glossy poster** — which is precisely what `1m-l` round 1 came back as.

**The kinetic element inside the frame is the riffling notes**, smeared by the drag-shutter clause
that worked on [`1m-m`'s champagne](#1m-m--champagne-in-a-coffee-mug--still--written-2026-09-12-unrun)
and `1m-t`'s belt. Flash freezes him and the machine; the notes are an arc of blur.

#### 🔴 Banknotes are a policy risk, and the shot's own physics solves it

A British banknote carries a **real central bank's name**, legible denominations and **a real
person's portrait** — [triggers 1, 2 and 4 at once](../../flow/failure-modes.md#a5-the-five-triggers-badcodes-own).
External reporting agrees the industry side-steps it: *"AI generators don't replicate specific
real-world currencies or exact denominations to comply with legal and ethical guidelines"*
`[community]`.

🔑 **The fix is geometry, not a ban** — and it is free, because it is what the shot looks like
anyway:

- **The stacked notes are seen edge-on**, so only the paper edges show. No face, no printing.
- **Every note inside the machine is moving**, so its face is an arc of colour.
- Both stated **positively**, because [§27 says a subtractive shape comes back inverted](../../google-flow/nano-banana-2.md#27--ask-for-an-object-never-an-absence--a-subtractive-shape-comes-back-inverted-observed-2026-08-30)
  and *"no portrait on the notes"* would draw one.

⚠️ **The colour is named and the institution is not** — *purple, mauve and brown*, which is what
2008 sterling looks like without a word the classifier can match.

#### ⚠️ One more risk: the model may "correct" the absurdity

`[practitioner]` Nano Banana **normalises unusual input toward conventional interpretations** — the
documented case is multiple references to *Ugly Sonic* returning normal Sonic
([Max Woolf](https://minimaxir.com/2025/12/nano-banana-pro/)). **A cash counter on a trading desk is
exactly the kind of thing it may quietly fix into a bank teller's window.** The counter is
[§546's lever](../../google-flow/nano-banana-2.md#-making-a-subject-small-put-something-else-in-the-subject-slot-community-2026-09-09),
already proven on `1m-l`: **the trading desk goes in the `Subject:` slot** and the machine is a
feature sitting on it, with the monitors, the arms and the printouts named around it.

**Model:** **Nano Banana 2**. **Paste into:** Flow → the image prompt box. **Aspect:** 16:9.
**Resolution:** 2K. **Character:** `@2008 - tarquin`. **No reference image.**

**Check these five on the result, worst first:** it is a trading desk and not a bank counter ·
his hand is on the machine and not on the money · the stacked notes show edges rather than faces ·
the torn note is present at the machine's throat · nothing in frame carries a readable word or number.

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. It is late at night. In this frame he is standing over a note-counting machine on his own desk, watching it work.

Camera: a 35mm lens at desk height, level, about a metre and a half from the machine and well over to the left, so the run of desks goes away to the right at an angle and nothing in the room is square to the lens. The frame is noticeably tilted. Nearest the lens, the back corner of a monitor on the next desk crosses the bottom right, dark and thrown completely out of focus so that it is a soft blur.

Subject: a trading desk at the end of the night — four slim flat panels of 2008 on articulated steel arms with thick dark plastic bezels, a keyboard shoved aside, printouts heaped and sliding, a tangle of cables over the back edge, a mug with a brown ring dried inside it. Sitting square in the middle of all of it, where a keyboard should be, is a small beige plastic note-counting machine of 2008 with a rubber feed wheel, a hinged hopper and a narrow red dot-matrix display carrying figures too small and soft to read.

Action: the machine is running. A thick wedge of banknotes is stacked in its hopper and the notes are being pulled through the throat so fast that they are an arc of purple, mauve and brown blur, fanned between the feed wheel and the stacker. A note has torn on its way through and is caught at the throat, half of it still hanging there, with a small shred of paper on the desk beside the machine. The counted notes are landing in a block in the stacker, seen edge-on so that only the soft furred edges of the paper show.

Him: the man from the character reference stands over the desk, leaning in, seen from the waist up behind the machine. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples. His shirtsleeves are turned back and his tie is pulled loose. One hand rests flat on the top of the machine's casing and the other is in his trouser pocket, and neither hand is anywhere near the notes. His eyes are on the machine's little display rather than on the money — lower lids pushed up, brows level, one corner of his mouth pulled back and held there. The expression is small.

Around the money: the used notes are soft, creased and furred along their edges, several of the bundles still in a bank's plain paper bands, one band snapped and lying on the desk. A few loose coins have been pushed to one side.

Environment: the floor beyond the desk has gone dark for the night — the ceiling tubes down to a few dim fittings, the far end falling away to nothing, the other desks black shapes with the cold glow of standby screens on them.

Light: the photograph was taken with a flash on top of the camera, fired straight across the desk. The machine and his face are the brightest things in the picture, and the machine throws a crisp dark shadow back across the printouts. The white of his shirt clips to featureless white where the flash hits hardest, while the shadowed side of his face and the desk below him keep their detail rather than going to solid black. The flash does not reach far: four metres back the room is only a dim green wash and the cold glow of the screens. The shutter stayed open after the flash fired, so the notes moving through the machine are smeared into a continuous arc while the stacked notes, the machine and the man are frozen sharp.

Style: a newspaper photograph of the 2008 financial crisis, shot on a Canon EOS-1D Mark III with a Speedlite — fine digital noise in the shadows, a cool blue-green cast from the tubes, muted colour, and visible pores rather than airbrushed skin.

Constraints: the only light sources are the camera's flash, which is behind the lens, and the ceiling tubes, which are above the top edge of the frame. This is a trading floor and the machine is sitting on a trader's own desk, with monitors on arms all around it. Every note in the machine is in motion, so its face is an arc of colour, and the notes in the stacks are seen edge-on so that only the paper edges show. His hand rests on the machine's casing and the money is untouched. His is the only face in the picture. He is twenty-five years old. His expression stays small — a stranger looking at this photograph would read concentration before they read pleasure. No brand names, logos or readable labels anywhere, and nothing in the picture carries a word or a number that can be made out. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

**Sources for this entry (2026-09-13):**
[Scarface (Push It to the Limit) — the montage's structural job](https://en.wikipedia.org/wiki/Scarface_(Push_It_to_the_Limit)) `[community]` ·
[a1.art — the currency-generation compliance position](https://a1.art/prompts/fake-banknotes) `[community]` ·
[Max Woolf — Nano Banana Pro normalises unusual input](https://minimaxir.com/2025/12/nano-banana-pro/) `[practitioner]` ·
[Wearview — visible pores, not airbrushed](https://www.wearview.co/blog/fix-ai-skin-texture) `[community]`

### 1m-p — round 1 ✅ **ACCEPTED 2026-09-13** (Jack)

⬜ **Master not banked** — save it as `camera/reference/1m-p-note-counter-ACCEPTED.png`.

**✅ What landed:** the dead floor with its green tube wash and monitors on arms, the counter sitting
where a keyboard should be, **his hand flat on the casing and the other in his pocket with the money
untouched**, his eyes on the machine rather than the cash, the used banded bundles, the loose coins,
the mug with its brown ring, and dark out-of-focus monitor backs occluding both bottom corners.
The [`Subject:`-slot lever held](#-making-a-subject-small-put-something-else-in-the-subject-slot-community-2026-09-09) —
it is unmistakably a trading desk and not a bank counter.

🔑 **What did NOT land is, for the third time, the gift. The machine came back stopped** — the notes
in the throat are static and sharp rather than an arc of blur, so it reads as a counter at rest.
**See the n=3 note below; it hands the clip its one action, exactly as `1m-l`'s open doors did.**

⚠️ **Two deviations accepted:** the light is the room's own tubes rather than a hard flash (second
frame running — same call as [`1m-t`](#1m-t--round-1--accepted-2026-09-13-jack--with-two-recorded-flaws)),
and the frame came back level rather than tilted. Neither is worth a generation.

🔴 **The notes came back legible** — a banded bundle plainly reads its denomination. **It generated,
so there was no policy problem on the still**, and the edge-on clause only partly took. ⚠️ **It is a
live problem for the clip**, because [text re-solves per frame and flickers](#-the-360p-draft-is-a-motion-check-never-a-text-check--and-upscaling-repairs-nothing).
Handled below by leaving the static bundles pinned and never asking the display to change.

### 🔴 §38 at n=3 — a mechanical in-progress state is near-unbeatable, and it is worth planning around

`[observed 2026-09-12, 2026-09-13 ×2]` Three shots have now asked Nano Banana for a machine
**mid-action** and got the machine **at rest**:

| Shot | Asked for | Came back |
| --- | --- | --- |
| `1m-l` rounds 1–5 | lift doors almost shut — via a stage direction, then a physical analogy, then a proportion, then the shape of the light | **fully open**, every time |
| `1m-p` round 1 | notes riffling through the throat as an arc of blur | **stopped**, notes static and sharp |

⚠️ **One counter-example, and it is instructive:** `1m-t`'s treadmill belt **did** come back smeared.
The difference worth noting is that a belt is **one continuous surface** while doors and banknotes
are **discrete objects with a start and an end state** — 🔴 **inferred from n=3, not tested.**

🔑 **The planning consequence, which is the useful half:** stop spending rounds on it and **design
the stillness in**. A plate of a machine at rest is not a failed frame — it is frame 0 of the clip
where the machine starts. **The still shows the state; the clip shows the change.** That has now
produced a better shot twice.

### 1m-p — the clip · **video** · written 2026-09-13, unrun

**Routing:** Omni Flash → **Frames** tab, the accepted `1m-p` frame as the **start frame**.
🔴 **End slot EMPTY.** 🔴 **No Character, no Ingredients** — same call as `1m-l`, `1m-m` and `1m-t`.
**Duration: 4 seconds** — the event is a **loop**, not a travel, so
[the eighth-pass rule applies](#eighth-pass--2026-09-11-vendor-community): fewer frames, less drift,
nothing lost. *(`1m-l` got 6s only because the door travel was itself the event.)*

🔑 **This is the lowest-risk clip in the montage, and it is worth saying why: there is nobody else in
it.** No walking extras, no cleaner, no crowd — the whole
[Frames-morphs-a-moving-person problem](#-on-frames-a-walking-extra-morphs--stillness-is-the-only-thing-that-holds-them-observed-2026-08-26)
is simply absent. **And both of his hands are already pinned by the plate** — one flat on the casing,
one in his pocket — so the [named hand-morph risk](#eighth-pass--2026-09-11-vendor-community) has
nowhere to fire. The only thing asked to move is a machine.

#### 🔑 The design: the machine runs and the stacks do not change

The one action leads its own sentence — **the notes riffle through the throat**. Everything else
holds.

🔴 **The hard half is deliberately outside the clip**, which is
[`1m-m`'s champagne fix](#1m-m--the-clip--video--written-2026-09-12-unrun) reused. Paper being
consumed from one stack and rebuilt into another is a **volume-conservation and object-interaction**
problem, and that is the family video models are
[documented to fail](https://arxiv.org/abs/2607.25321) `[academic]`. **So we never ask for it.**

| The failure | The clause |
| --- | --- |
| 🔑 **The stacks visibly shrink or grow, wrongly** | **Never requested.** The hopper stack and the banded bundles on the desk are **pinned as unchanged**. Only the notes *at the throat* move. Volume conservation is out of scope by construction |
| **Notes render as discrete flapping objects** | The throat is named as **an arc of blur of the same width in the same place** — the positive form, because [a negation would name breakage in](#-negatives-do-not-work-and-they-actively-backfire) |
| **Fast paper rendered sharp** | The [24fps / 180° shutter clause](#the-shutter-is-the-tell-nobody-prompts-for). ⚠️ **In, as on `1m-t` and deliberately out on `1m-l`** — the rule is about the speed of the motion, never the house style |
| 🔴 **The £20s flicker and re-solve** | `[community]` *AI video text changes between frames because each frame is reconstructed separately* ([aivid](https://aivid.video/blog/why-ai-video-text-changes-between-frames-and-how-to-fix-it)). The moving notes become **illegible by blur**, and the static bundles are **pinned**, so nothing legible is ever asked to change |

#### 🔴 The count is NOT asked to climb, and that is a real subtraction

The rising number is the *Push It to the Limit* beat and the temptation is obvious. **It is also a
request for changing on-screen text, which is the single best-documented failure in this whole
file.** The display is instead pinned to a steady red glow with figures too small to read.

⬜ **If a climbing number is genuinely wanted, it is an ffmpeg job over the finished clip** —
[the only lane that can write on-screen text](../../video-fx/hybrid-method.md), since Premiere's API
cannot set a string at all. At this size in a one-second cut it almost certainly is not worth it.

#### ✅ Two small things that sell "running" for free

- 🔑 **The machine judders very slightly against the desk.** A real note counter does, it is the
  cheapest possible proof the motor is under load, and it is one bounded local motion.
  ⚠️ **The coins and the bundles are explicitly pinned so the judder does not spread** —
  [particle nouns have no volume control](#-particle-nouns-have-no-volume-control-observed-n2).
- **Biological motion**: he breathes and blinks once.
  [On a held shot of a person doing nothing, that is the performance](#-biological-motion--the-anti-slop-clause-for-any-shot-of-a-person-doing-nothing),
  and the model adds neither unasked.

#### 🔑 The audio is the best thing in this shot

A note counter's fast paper flutter is a genuinely great sound and it is doing the montage's work —
**money as a machine noise.** Under it, the dead floor. No music, no voices.

⬜ **Free button in the edit:** cut the clip's audio dead on the out-point. The flutter stopping is a
harder full stop than any visual, and it costs nothing — **do it in Premiere, not by asking the
machine to stop**, which would be a second action in a one-action clip.

#### ⬜ Draft at 360p first

[A motion check only](#-the-360p-draft-is-a-motion-check-never-a-text-check--and-upscaling-repairs-nothing).
**Watch three things:** the throat blurs rather than flapping, the stacks stay the size they are, and
his hand stays flat on the casing. **Ignore every note, number and label in the draft** — at 360p
they are meaningless, and nothing about them should be inferred from it.

**Paste into:** Flow → **Frames to Video** prompt box. **Start frame:** the accepted `1m-p` image.
**End frame:** empty. **No Character, no Ingredients.** **Duration:** 4s. Primary:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts. The camera is locked off and holds completely still throughout, and the light stays exactly as it is.

The machine runs. The notes are pulled through its throat fast enough that they are one continuous arc of blurred colour, the same width and in the same place the whole time, and the machine judders very slightly against the desk as it works.

The wedge of notes in the hopper and the banded bundles, the loose coins, the mug, the printouts and the keyboard all stay exactly where they are and stay the size they are.

He stays leaning over the desk with one hand flat on top of the machine and the other in his pocket, both hands still. He keeps his eyes on the machine's little display, breathes, and blinks once, and his expression holds as it is.

The screens around him hold a steady cold glow and the machine's small red display holds a steady glow, with figures on both far too small and soft to read. The dark far end of the floor stays dark and empty.

Shot at 24fps with a 180-degree shutter, so the notes moving through the machine smear while everything still is sharp.

Audio: the fast paper flutter of the counting machine, its motor under load, and the low hum of an empty floor at night. No music and no voices.

Thanks.
```

⬜ **Fallback, only if the primary comes back diluted or re-staged** — same tab, same start frame:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. Camera locked off, one continuous shot, no cuts, and the light stays as it is.

The machine runs: the notes at its throat become one continuous arc of blurred colour and it judders very slightly against the desk. The stacks, the coins and everything else on the desk stay exactly as they are. He stays leaning over it, both hands still, breathes and blinks once.

Shot at 24fps with a 180-degree shutter, so the moving notes smear while everything still is sharp.

Audio: the fast paper flutter of the machine, its motor, and the hum of an empty floor. No music and no voices.

Thanks.
```

**Post, in Premiere:**

1. 🔑 **This is the snap-zoom frame.** The *Push It to the Limit* energy is bought here, not in Flow —
   push in hard on the counter and cut on the beat ([`hybrid-method.md`](../../video-fx/hybrid-method.md)).
2. ⬜ **Cut the audio dead on the out-point** — the free button described above.
3. ⬜ **Play it into `1m-8`**, which carries the same narration line and closes it on the empty floor.
4. ⚠️ **Watch the throat and the stacks on playback, not his face.** Flapping discrete notes, or a
   stack that changes size, is the paper-physics risk firing — **a re-roll, not a grade.**
5. ⚠️ **Nothing ships unmeasured** — `scripts/delivery-qc.sh` ([`delivery.md`](../../video-fx/delivery.md)).

**Sources for this entry (2026-09-13):**
[aivid — why AI video text changes between frames](https://aivid.video/blog/why-ai-video-text-changes-between-frames-and-how-to-fix-it) `[community]` ·
[Runway — image-to-video prompting guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide) `[community]` ·
[Luma — prompts that don't look AI-generated](https://lumalabs.ai/news/prompt-realistic-ai-videos) `[community]` ·
[arXiv 2607.25321 — physics-grounded generation](https://arxiv.org/abs/2607.25321) `[academic]` ·
[Flow models & supported features](https://support.google.com/flow/answer/16352836) `[vendor]`

### 1m-v — the viewing · **still** · written 2026-09-13, unrun

**Chosen by Jack 2026-09-13** alongside `1m-z` (the cup) and `1m-g` (the shoot).

#### 🔑 It goes under `1m-7`'s line, and that is the whole idea

*"Some twat is going to lose a house over this trade, and I am never going to meet them."*
[`1m-7`](#1m-7--the-house--still--accepted-2026-09-11) already sits there — the locksmith, the bin
bags, the child's bike. **Put the viewing under the same sentence and cut between them: one house he
is buying, one house someone is losing, inside a single line of narration.** Nothing has to be said.
It is free, and it is the strongest cut available in the montage.

#### 🔑 The light register is deliberately NOT the montage's flash

Both house frames are **flat, ordinary daylight with no flash**, and that is a design decision rather
than a drift: **the flash frames are his world; the two daylight frames are the real one.** A frame
that is not performing reads as simply true, which is what
[gate 2 needs a cost frame to do](../../../.claude/skills/shot-craft/SKILL.md). Matching `1m-7`'s
register is also what makes the cut between them read as *the same afternoon*.

#### 🔑 The cost is geometric: he is standing above the houses people actually live in

The window looks over **ordinary London terraced rooftops** — hundreds of real homes — and **he has
his back to them.** He never looks out. That is the entire argument in one piece of blocking, and it
needs no second person in frame.

Underneath it, the second cost: **the flat has never been lived in.** Protective film still on the
window frames, plastic on the worktop, a bare flex where a light should be, a pallet of packaging in
the corner. **A home as a product.** New kind — every other cost in the montage is a person or a
room that has been emptied; this one has never been filled.

#### ⚠️ The occluder is the doorframe, not the agent

[Round 1 of `1m-l` put a person in the near foreground and came back with a giant blurred head and a
halo](#1m-l--round-1-not-accepted-jack-2026-09-12-it-looks-like-ai-slop) — the
[fake-DoF tell](../../google-flow/nano-banana-2.md#️-fake-depth-of-field-has-its-own-tells-practitioner-community).
**So the near occluder is the door edge and architrave**, which also states where the camera is
standing. The agent stays in the midground with her back to us, giving the vantage without the halo.

⚠️ **She is described by role, clothing and task only — no age, no build** — which is
[the phrasing that got `1m-l` through after two refusals](#1m-l--round-4-policy-block-jack-2026-09-13---and-it-disproves-the-round-2-diagnosis).

**Model:** **Nano Banana 2**. **Paste into:** Flow → the image prompt box. **Aspect:** 16:9.
**Resolution:** 2K. **Character:** `@2008 - tarquin`. **No reference image.**

**Check these five on the result, worst first:** the rooftops beyond the glass are ordinary houses
rather than towers · he has his back to the window · the flat is unfinished and unfurnished · the
near foreground is the doorframe and not a person · nothing carries a readable word.

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. In this frame he is being shown around an empty new flat he is buying, and he is on the phone throughout.

Camera: a 28mm lens at standing height, level, taken from the doorway of the room and off to the left, so the walls run away at an angle and nothing is square to the lens. He is small, right of centre and low in the picture, with a lot of ceiling and window above him. Nearest the lens, the edge of the open door and its architrave cross the left side of the frame from top to bottom, dark and thrown completely out of focus.

Subject: the empty living room of a brand-new flat that nobody has moved into. Bare engineered-wood floor, white walls with no pictures and no marks, recessed spotlights in the ceiling, a bare flex hanging where a light fitting should be. Protective blue film is still stuck to the window frames and along the edge of the kitchen worktop at the back, a strip of it peeling. A shrink-wrapped pallet of packaging stands in the far corner, and a roll of carpet protector runs across part of the floor. There is no furniture of any kind.

Behind him: a floor-to-ceiling window and a narrow balcony fill the back wall, and beyond the glass, below him, the roofs of ordinary London terraced streets run away to a flat grey horizon — slate and tile, chimney stacks, aerials, back gardens, hundreds of houses people live in.

Him: the man from the character reference stands a couple of paces into the room with his back to the window, seen from the knees up. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples. He has kept his dark overcoat on over a suit, done up, and one hand is in its pocket. The other holds a small black handset with a keyboard to his ear. He is mid-call and half turned away from the room, his weight on one leg, his chin level, his eyes on the bare floor a few feet in front of him. His lids are relaxed and his lips are closed. Nothing in his face is interested in the flat.

Also in the room: nearer the camera and to the left, an estate agent stands waiting with her back to the lens, in a plain dark work suit, a folder held against her side and a set of keys hanging from one finger. She is facing him and has stopped talking.

Light: flat grey daylight through the window, and nothing else. It comes from behind him, so the room is lit evenly and softly, the window is the brightest thing in the picture, and his face is in its own shadow with only the light bouncing back off the bare white walls to fill it. The ceiling spotlights are switched off. There are no lamps, no sun and no warmth anywhere, and the bare floor takes a dull sheen from the window.

Style: a newspaper photograph of the 2008 financial crisis, taken on a Canon EOS-1D Mark III by available daylight with no flash — fine digital noise, muted cool colour, and no retouching or skin smoothing.

Constraints: daylight through the window is the only light source in the picture. The view beyond the glass is low ordinary housing — pitched roofs, chimneys and back gardens — and there are no tall towers and no glass buildings in it. The room is completely bare and unfinished. The estate agent is seen only from behind, so his is the only legible face in the picture. He is twenty-five years old. His expression stays small — a stranger looking at this photograph would read boredom before they read anything else. No brand names, logos or readable labels anywhere, including on the folder, the packaging and the handset. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

### 1m-v — round 1 ✅ **handed over as the plate, 2026-09-13** (Jack)

Jack asked for its clip, so it is treated as accepted. All five checks pass: ordinary terraced roofs
and no towers, him in front of the window and not looking out, blue film still on the frames and the
worktop, the doorframe as the near occluder, and no readable words. ⬜ **Whether he reads twenty-five
is Jack's call, not this file's.** ⬜ **Master not banked**: save it as
`camera/reference/1m-v-the-viewing-ACCEPTED.png`.

🔑 **The plate brought one gift: the keys are hanging from her finger in plain view.** That is the
clip's action. See below.

### 1m-v — the clip · **video** · written 2026-09-13, unrun

**Routing:** Omni Flash → **Frames** tab, with the accepted `1m-v` frame as the **start frame**.
🔴 **Leave the end slot EMPTY** ([never pin an `endImage`](../../video-fx/hybrid-method.md)).
🔴 **No Character and no Ingredients**, the same call as `1m-l`, `1m-m`, `1m-t` and `1m-p`: the staging
is the shot, and the plate is the only authority on the face. **Duration: 4s.** Nothing travels, so
fewer frames means less drift.

#### 🔑 The design: the keys to a home, swinging on a finger nobody is looking at

**The job:** the still says *he doesn't care*. The clip adds *she is waiting*, and it does that with
the one object that ties the frame to `1m-7`. **The keys sway gently on her finger.**

- 🔑 **It rhymes with `1m-7`.** Those two frames share one line of narration. There, a locksmith
  changes a lock so a family's keys stop working. Here, a set of keys to a home hangs in the air
  while the man buying it is on the phone. **The same object, taken away and ignored, in one
  sentence.** It needs no words. 🔴 *Inferred, not tested in an edit.*
- **It is a state that continues, not one being reached.** The keys are already hanging in frame 0.
  A small pendulum has no destination, which is the
  [house rule](../../google-flow/omni-flash.md#-ask-it-to-continue-a-state-never-to-reach-one-observed).
- **It is the smallest thing in the frame that can move and still read**, and
  [less motion is safer motion](../../google-flow/omni-flash.md#slop-counters-specific-to-motion-community).

**His half is listening, not talking.** He breathes, blinks once and gives one small nod to the
caller. 🔴 **His lips stay closed**, because
[there is never dialogue in a Flow clip](#conventions) and a mouth moving with no sound is worse than
either. The nod is the only thing he does, and it is aimed at the phone, not at the room.

#### 🔴 Risks, and what each clause is there for

| The risk | The clause |
| --- | --- |
| **A person who moves gets redrawn on Frames** ([5a](../../google-flow/omni-flash.md#-on-frames-a-walking-extra-morphs--stillness-is-the-only-thing-that-holds-them-observed-2026-08-26)) | Nobody walks. She stays where she is, with **her hand still and only the keys moving**. He stays where he is. Both are mostly dark shapes against the window, which leaves the model little detail to get wrong |
| **Hand morph where the keys hang** | Her hand and the folder are pinned. The movement is the keys *below* the finger, not the finger itself |
| **The view through the glass comes back changed or duplicated** ([anything seen through glass fails](../../google-flow/omni-flash.md#slop-counters-specific-to-motion-community)) | Nothing out there is asked to move: no birds, no smoke, no traffic. It is stated positively as holding exactly as it is. The audio line keeps traffic muffled and non-specific, so there is no noun for the model to put a car to |
| **The hanging flex swings in sympathy** ([a hanging thing given any motion finds a state](../../google-flow/omni-flash.md#-a-hinged-thing-given-wind-will-settle-shut-and-stay-shut-observed-2026-08-26)) | Named once, in the list of things that stay still. There is no draught in the prompt to set it off |
| **Daylight pulses or "grades" itself** | [The light is stated by its behaviour, not its source](../../google-flow/omni-flash.md#-animating-a-flash-photograph-never-write-the-word-flash-house-rule-2026-09-12): *the light stays exactly as it is* |
| **Over-animation is the AI tell** | One motion each, both small. 🔑 The phrasing is *"breathes, blinks once"*, from the [biological-motion clause](#-biological-motion--the-anti-slop-clause-for-any-shot-of-a-person-doing-nothing), because a held shot of a person doing nothing is exactly where the frozen-mannequin look shows up |

⚠️ **The shutter clause is deliberately left out**, as on `1m-l`. Nothing here moves fast, so it would
be a word that buys nothing.
⚠️ **Every instruction is positive.** The only negation kept is `No music and no voices.`, which is
vendor idiom and `[confirmed]`.

#### ⬜ Draft at 360p first

This is [a motion check only](#-the-360p-draft-is-a-motion-check-never-a-text-check--and-upscaling-repairs-nothing).
**Watch three things:** the keys sway and her hand stays still, his lips stay closed, and the roofs
beyond the glass do not change. Ignore the faces and the grain at 360p. If all three hold, promote to
720p.

**Paste into:** Flow → **Frames to Video** prompt box. **Start frame:** the accepted `1m-v` image.
**End frame:** empty. **No Character, no Ingredients.** **Duration:** 4s. Primary:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts. The camera is locked off and holds completely still throughout, and the light in the picture stays exactly as it is.

The bunch of keys hanging from the estate agent's finger sways gently back and forth, a small slow swing that carries on for the whole shot. Her hand and the folder stay still, and she stays facing him with her back to the lens.

He stays standing where he is with the phone to his ear, listening. He breathes, blinks once and gives one small nod to the caller, his lips closed, and his expression holds as it is.

The rooftops beyond the glass, the hanging flex, the rolled carpet, the worktop and the doorframe all stay exactly where they are.

Audio: the quiet of an empty unfurnished room, the faint chink of the keys, and the muffled hum of the city through closed double glazing. No music and no voices.

Thanks.
```

⬜ **Fallback, only if the primary comes back diluted or re-staged**: same tab, same start frame.

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. Camera locked off, one continuous shot, no cuts, and the light stays as it is.

The keys hanging from the estate agent's finger sway gently, and her hand stays still. He stays where he is with the phone to his ear, breathes, blinks once and gives one small nod, lips closed. Everything else in the room and beyond the glass stays exactly as it is.

Audio: an empty room, the faint chink of keys, the muffled city through glass. No music and no voices.

Thanks.
```

**Post, in Premiere:**

1. 🔑 **Cut it against `1m-7` under the same line.** The house being bought, then the house being
   lost. If a move is wanted, it is a slow push toward the keys, done here and
   [not in Flow](../../video-fx/hybrid-method.md).
2. **Hold the flat daylight grade apart from the flash frames.** The two daylight frames are the real
   world, and matching `1m-7`'s grade is what makes them read as the same afternoon.
3. **Match the grain rather than stacking it.**
4. ⚠️ **Watch her hand and the keys on playback, not his face.** A finger that bends, or keys that
   multiply or melt into the folder, is a re-roll, not a grade.
5. ⚠️ **Nothing ships unmeasured**: run `scripts/delivery-qc.sh` ([`delivery.md`](../../video-fx/delivery.md)).

**Sources for this entry (2026-09-13):**
[Promptessor — image-to-video prompts in 2026](https://promptessor.com/blog/image-to-video-prompts-how-to-animate-photos-products-characters-and-art-in-2026) `[community]` ·
[Pasquale Pillitteri — Gemini Omni Flash prompting guide, Google's five tips](https://pasqualepillitteri.it/en/news/3513/mastering-gemini-omni-flash-video-prompting-guide) `[community]` ·
[Promptslove — Google Omni prompting guide](https://promptslove.com/blog/google-omni-prompting-guide/) `[community]` ·
[Flow models & supported features](https://support.google.com/flow/answer/16352836) `[vendor]`

### 1m-z — the cup · **spec only** · 2026-09-13 · *prompt to follow*

**The frame:** an office corridor or a lift lobby. He is walking and talking, arm out, and he opens
his fingers over a bin **and misses it by a foot** without breaking stride or looking. The cup is in
the air.

- 🔑 **The whole gag is that he does not look.** Same engine as `1m-m`'s champagne and `1m-l`'s
  eyeline — he never looks at the consequence.
- **Camera:** locked, wide, low, with the bin in the near midground and him walking out of frame. The
  cup is caught mid-fall.
- ⚠️ **The one hard clause is the falling cup.** [A real camera never catches the whole fall](../../google-flow/omni-flash.md#the-rule-that-outranks-all-of-it-a-real-camera-never-catches-the-whole-fall),
  and a dropped object rendered sharp reads as pasted on. **It must be a streak**, which is the
  [shutter clause](../../google-flow/omni-flash.md#the-shutter-is-the-tell-nobody-prompts-for)
  `[confirmed 2026-08-14]` on exactly this — Karen's dropped phone.
- **Cost:** the coffee already on the carpet from the last three, and the cleaner's black sack propped
  against the wall. **Petty, Karen-scaled, and the cheapest frame on the list.**
- ⬜ **Best used as a hard one-second cut**, probably the montage's shortest.

### 1m-z — the cup · **still** · written 2026-09-13, unrun

#### 🔴 Design change from the spec: the cup has already landed

The spec caught the cup in mid-air. **[§38 at n=3](#-38-at-n3--a-mechanical-in-progress-state-is-near-unbeatable-and-it-is-worth-planning-around)
says not to spend rounds on that.** A discrete object shown mid-action has come back at rest three
times out of three. A cup that is asked to fall will come back in his hand or on the floor, and we
cannot choose which.

🔑 **So design the stillness in: the cup is on the carpet, and he is already walking away.** This loses
nothing and gains two things:

- **The gag still reads.** His hand is still out to the side, fingers open, and he is looking straight
  ahead. *He let go of it and didn't look.*
- 🔑 **It turns one act into a habit.** Two older cups lie by the same bin, and there are old brown
  rings on the carpet around it. **He does this every day.** That is funnier than a one-off and
  harder-hitting, and it is exactly [rule 2 of this set](./shot-list.md): observe, don't invent.
- ⬜ **It hands the clip its action**, the same gift as `1m-l` and `1m-p`: the fresh spill spreads into
  the carpet, or the cup rolls and settles.

#### 🔑 The vantage: floor level, where the person who cleans it up kneels

[The Karen rule](./shot-list.md): stand the camera where the person he is being a knob to stands.
Nobody kneels by that bin except whoever cleans the carpet. **So the camera is on the floor beside the
bin, looking up at him as he walks past.** The cups are the nearest things in the picture, and he is
the tall figure in the middle distance.

#### 🔴 Gate 2: the cost is the carpet, not the cleaner

The spec had the cleaner's black sack in shot. 🔴 **Dropped: `1m-t`'s cost is already the cleaner**,
and [the montage's standing rule](./shot-list.md) is no two costs of the same kind. **The cost here is
the stains**: weeks of rings soaked into a carpet somebody else has to scrub, and a mess that has built
up over time. *Petty contempt* is a new kind.

#### ⚠️ Phrasing calls

- **He is in three-quarter profile, crossing the frame, not walking straight away from the lens.** A
  Character binds only to a visible face ([§12](../../google-flow/nano-banana-2.md#12--a-character-binds-to-a-face-no-face-in-the-shot-no-likeness-observed)),
  and his eyes being fixed ahead is the joke. Seen from behind, the joke is gone.
- **Deep focus, no occluder.** A floor-level flash photograph at a small aperture is sharp front to back,
  which is how press flash looks, and it removes the
  [fake-depth-of-field halo](../../google-flow/nano-banana-2.md#️-fake-depth-of-field-has-its-own-tells-practitioner-community)
  that ruined `1m-l` round 1.
- **The flash is named as hardware in Style and as consequences in Light**, with its position in
  Constraints ([§35](../../google-flow/nano-banana-2.md#35--a-flash-described-as-an-object-in-the-room-is-drawn-as-a-lamp-observed-2026-09-11-n1)).
- **The worn garments are stated**: shirtsleeves, loosened tie, no jacket
  ([§36](../../google-flow/nano-banana-2.md#36--a-carried-garment-with-no-worn-garment-stated-returns-both-observed-2026-09-12-n1)).
- **The cups are plain, with a brown card sleeve.** No coffee-chain branding is named, so none gets
  drawn ([§34](../../google-flow/nano-banana-2.md#34--naming-a-marque-renders-its-badging-and-no-downstream-constraint-removes-it-observed-2026-09-08)).
- **The walking blur on his trailing foot is allowed but not asked for.** Flash freezes him, and asking
  for drag would be another in-progress state for §38 to refuse.

**Model:** **Nano Banana 2**. **Paste into:** Flow → the image prompt box. **Aspect:** 16:9.
**Resolution:** 2K. **Character:** `@2008 - tarquin`. **No reference image.**

**Check these five on the result, worst first:**

- The cup is on the carpet beside the bin, not in his hand and not in the bin
- His eyes are ahead, not on the cup
- The camera is really at floor level
- The older cups and rings are there
- Nothing carries a readable word

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. In this frame he has just dropped his empty coffee cup at a bin, missed it, and walked on without looking.

Camera: a 24mm lens resting on the carpet, a few inches off the floor, a metre from the bin and angled up, so the ceiling shows at the top of the frame and he looms above the lens. The corridor runs away at an angle to the right and nothing is square to the lens. The picture is sharp from the nearest cup to the far end of the corridor.

Subject: the carpet by the bin in an office corridor outside a trading floor. A small grey metal office bin stands left of centre, half full of paper. On the carpet a foot to the right of it lies a plain white paper coffee cup with a brown card sleeve, on its side, its plastic lid knocked off beside it and a fresh splash of coffee soaking into the carpet from its mouth. Two older empty cups of the same kind lie nearby, one crushed, and the grey carpet tiles around the bin are marked with old dried brown rings and splash marks, some faded, where cups have landed before.

Him: the man from the character reference is walking past the bin from left to right, two strides beyond it, seen full length from below in three-quarter profile. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples. He wears a white shirt with the sleeves turned back and a loosened tie, no jacket. One hand holds a small black handset with a keyboard to his ear. His other arm is still out to the side at hip height where he let the cup go, the fingers open and relaxed. His eyes look straight ahead down the corridor, his chin level, his mouth closed. Nothing in his face has noticed the cup.

Environment: a plain 2008 office corridor — grey carpet tiles, pale walls with scuffs along them at trolley height, a strip of recessed ceiling tubes, a pair of lift doors far down on the left, a fire door with a wired-glass panel at the far end.

Light: the photograph was taken with a flash on top of the camera, fired low across the carpet. The cups, the wet splash and the bin are the brightest things in the picture and each throws a crisp hard shadow along the carpet. His white shirt clips to featureless white where the flash hits hardest, while his trousers and the shadowed side of his face keep their detail rather than going to solid black. The flash falls off quickly down the corridor, and the far end is only a dim green wash from the ceiling tubes.

Style: a newspaper photograph of the 2008 financial crisis, shot on a Canon EOS-1D Mark III with a Speedlite at a small aperture — fine digital noise and mild chromatic noise in the shadows, a cool blue-green cast from the tubes, muted colour, unretouched with visible pores rather than airbrushed skin, harsh and unflattering.

Constraints: the only light sources are the camera's flash, which is behind the lens, and the ceiling tubes, which are above the top edge of the frame. The fresh cup lies on the carpet outside the bin, and both of his hands are empty apart from the handset. His is the only person and the only face in the picture. He is twenty-five years old. His expression stays small — a stranger looking at this photograph would read a man busy on a call before they read anything else. No brand names, logos or readable labels anywhere, including on the cups, the bin and the handset. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

### 1m-z — the cup, v2 · **still** · written 2026-09-13, unrun · *supersedes v1 above*

**Jack, 2026-09-13:** *"he needs to hold the cup in his hand and in the video drop it."*

🔑 **Why this is right, not just different:** v1 put the event in the still, and the still was then a
picture of *after*. v2 splits it the way `1m-l` and `1m-p` ended up splitting by accident: **the
still shows the state and the clip shows the change.** A cup held in a hand is a stable state, so
[§38](#-38-at-n3--a-mechanical-in-progress-state-is-near-unbeatable-and-it-is-worth-planning-around)
has nothing to refuse. It is also a better still on its own terms, because *about to* is an
[unresolved question](../../cinematography/stills.md#1-what-makes-a-still-hold) where *already
happened* is not.

**What changed from v1, and why:**

- **The cup is in his hand**, held loosely by the rim at arm's length over the carpet **beside** the bin,
  not over it. The miss is staged into frame 0, so the clip only has to let go.
- **The cup is empty and its lid is on.** That means no splash in the clip, because
  [liquids fail](../../google-flow/omni-flash.md#-fluids-fail-in-two-named-ways--and-the-design-fix-is-to-put-the-hard-half-outside-the-clip-academic--community-2026-09-12).
  The old rings on the carpet still say *he does this every day*.
- **He is level with the bin, not past it**, and still in mid-stride.
- **Kept:** the floor-level vantage, the older cups and rings as the cost, the flash register, and no
  other people.

⚠️ **The risk to flag now for the clip:** on Frames,
[a person who walks gets redrawn](../../google-flow/omni-flash.md#-on-frames-a-walking-extra-morphs--stillness-is-the-only-thing-that-holds-them-observed-2026-08-26).
A clip where he drops the cup *and* walks out is two actions and a walking body. ⬜ **The clip's fallback
is that he stops on his call beside the bin and lets go.** That is one action, no walking, and the gag
survives. The still works for either.

**Model:** **Nano Banana 2**. **Paste into:** Flow → the image prompt box. **Aspect:** 16:9.
**Resolution:** 2K. **Character:** `@2008 - tarquin`. **No reference image.**

**Check these on the result, worst first:**

- The cup is in his hand, held out beside the bin rather than over it
- His eyes are ahead, not on the cup or the bin
- The camera is really at floor level
- The older cups and rings are there
- Nothing carries a readable word

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. In this frame he is walking past a bin on a call, holding his empty coffee cup out to one side, about to let go of it without looking.

Camera: a 24mm lens resting on the carpet, a few inches off the floor, a metre from the bin and angled up, so the ceiling shows at the top of the frame and he looms above the lens. The corridor runs away at an angle to the right and nothing is square to the lens. The picture is sharp from the bin to the far end of the corridor.

Subject: the carpet by the bin in an office corridor outside a trading floor. A small grey metal office bin stands left of centre, half full of paper. Two empty paper coffee cups lie on the carpet beside it, one on its side and one crushed, and the grey carpet tiles around the bin are marked with old dried brown rings and splash marks, some faded, where cups have landed before.

Him: the man from the character reference is walking past the bin from left to right, level with it and a stride to its right, seen full length from below in three-quarter profile, mid-stride with his weight on his front foot. He is twenty-five: keep the face lean and unlined, the hairline full and low, with no creases from nose to mouth, no hollowing under the cheekbones and no recession at the temples. He wears a white shirt with the sleeves turned back and a loosened tie, no jacket. One hand holds a small black handset with a keyboard to his ear. His other arm hangs out to the side at hip height, and between his thumb and two fingers he holds a plain white paper coffee cup by its rim, loosely, with a brown card sleeve and its plastic lid on. The cup is out over the bare carpet beside the bin, not over the bin. His eyes look straight ahead down the corridor, his chin level, his mouth closed. Nothing in his face is thinking about the cup.

Environment: a plain 2008 office corridor — grey carpet tiles, pale walls with scuffs along them at trolley height, a strip of recessed ceiling tubes, a pair of lift doors far down on the left, a fire door with a wired-glass panel at the far end.

Light: the photograph was taken with a flash on top of the camera, fired low across the carpet. The bin, the cups and the stains are the brightest things in the picture and each throws a crisp hard shadow along the carpet. His white shirt and the cup in his hand clip to featureless white where the flash hits hardest, while his trousers and the shadowed side of his face keep their detail rather than going to solid black. The flash falls off quickly down the corridor, and the far end is only a dim green wash from the ceiling tubes.

Style: a newspaper photograph of the 2008 financial crisis, shot on a Canon EOS-1D Mark III with a Speedlite at a small aperture — fine digital noise and mild chromatic noise in the shadows, a cool blue-green cast from the tubes, muted colour, unretouched with visible pores rather than airbrushed skin, harsh and unflattering.

Constraints: the only light sources are the camera's flash, which is behind the lens, and the ceiling tubes, which are above the top edge of the frame. The cup is in his hand, held out beside the bin. His is the only person and the only face in the picture. He is twenty-five years old. His expression stays small — a stranger looking at this photograph would read a man busy on a call before they read anything else. No brand names, logos or readable labels anywhere, including on the cups, the bin and the handset. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

### 1m-z v2 — round 1, **handed over as the plate, 2026-09-13** (Jack)

Jack asked for its clip, so it is treated as accepted.

- ✅ **What landed:** floor-level vantage looking up; cup held loosely by the rim beside the bin, not
  over it; eyes ahead on the call; two old cups and a spread of dried rings; scuffed walls; lift doors;
  a wired-glass fire door at the far end; nobody else in frame.
- ⚠️ **Deviations, recorded not fixed:**
  - **No flash again.** It came back lit by the teal ceiling tubes. That is the third montage frame to
    do this, after `1m-t` and `1m-p`.
  - **The old stain reads wet and fresh** rather than dried.
  - **He may read older than twenty-five.** That is Jack's call.
- ⬜ **Master not banked:** save it as `camera/reference/1m-z-the-cup-ACCEPTED.png`.
- ⬜ **Crop the black border in Premiere.** The clip inherits it from frame 0.

### 1m-z — the clip · **video** · written 2026-09-13, unrun

**Routing:** Omni Flash → **Frames** tab, with the accepted `1m-z` v2 frame as the **start frame**.
🔴 **Leave the end slot EMPTY.** 🔴 **No Character and no Ingredients**: the bin-and-cup geometry *is*
the joke, and [Ingredients re-stages](../../google-flow/omni-flash.md#-the-tab-rule--amended-2026-08-18-ingredients-holds-identity-frames-holds-staging).
**Duration: 4s**, because [a physics beat drifts per frame](../../google-flow/omni-flash.md#why-falling-objects-fail-and-what-actually-fixes-it)
and 4s is the safest length.

#### 🔑 The design: the fingers open, and he never breaks stride

**The job:** the still asks *is he going to?* The clip answers yes, and shows that it cost him nothing.
The drop leads its own sentence
([the action the shot is for goes first](../../google-flow/omni-flash.md#️-the-action-the-shot-is-for-must-lead-its-own-sentence-observed)).

- 🔑 **The fall is short, and that is the whole reason this is attemptable.** The house rule is that
  [a real camera never catches the whole fall](../../google-flow/omni-flash.md#the-rule-that-outranks-all-of-it-a-real-camera-never-catches-the-whole-fall).
  The cup cannot leave frame from a floor-level camera, but it is only about half a metre up. At real
  speed that is a fraction of a second in the air, so **the model has only a few frames to get wrong.**
  ⚠️ *The height is estimated from the plate, not measured.*
- **It is empty with its lid on**, so there is no liquid to fail. It lands and tips onto its side, and
  nothing more is asked of it.
- **The shutter clause is in**, because the drop is the one fast motion. A falling cup rendered sharp
  reads as pasted on ([confirmed on Karen's phone](../../google-flow/omni-flash.md#the-shutter-is-the-tell-nobody-prompts-for)).
- 🔑 **The landing is carried by sound as much as picture:** a small, hollow, papery tap on carpet. That
  is the most real thing in the clip, and it cannot morph.

#### 🔴 The top risk is him walking, not the cup

[On Frames, a person who moves gets redrawn](../../google-flow/omni-flash.md#-on-frames-a-walking-extra-morphs--stillness-is-the-only-thing-that-holds-them-observed-2026-08-26),
and the tab rule's "Frames holds a face" row only applies to a
[near-static clip](../../google-flow/omni-flash.md#-the-tab-rule--amended-2026-08-18-ingredients-holds-identity-frames-holds-staging).
He is mid-stride toward a floor-level lens, so continuing to walk brings him closer and bigger. The
community tells for this are **feet sliding on the floor, arms swinging at the wrong tempo, and fingers
merging** `[community]`.

**Three things limit it:**

1. **Walking is a state he is already in, not one he has to reach.** He is mid-stride in frame 0, so it
   is [a continuation](../../google-flow/omni-flash.md#-ask-it-to-continue-a-state-never-to-reach-one-observed).
2. **At 4s at an unhurried pace, that is about two strides.** No destination is set and he is not asked
   to leave frame.
3. **The phone hand is pinned at his ear**, and the empty hand is only asked to relax after letting go.

⬜ **If he morphs, the fallback below takes the walk out**: he stops on his call beside the bin and lets
go. That is one action with no walking. It is less funny but much safer.

#### ⚠️ Audio: nothing is placed on a visible object

The lift doors and the ceiling tubes are both in frame.
[A sound placed on a visible object is a vote for that object moving](../../google-flow/omni-flash.md#-observed-2026-09-09-naming-an-off-frame-light-source-by-its-object-binds-it-to-a-visible-one),
so **no lift chime and no tube hum**, or the doors open and the lights flicker. The room tone is air
conditioning, which has no object in frame. 🔴 **No speech from the handset**: `No music and no voices.`
covers it, and the prompt has no colons after an action and no quotation marks
([the speech trap](../../google-flow/omni-flash.md#-the-speech-trap-is-punctuation-not-vocabulary)).

#### ⬜ Draft at 360p first

This is [a motion check only](#-the-360p-draft-is-a-motion-check-never-a-text-check--and-upscaling-repairs-nothing).
**Watch three things:** the cup falls as a quick streak and ends on the carpet (not floating, bouncing
high or vanishing); his feet plant rather than slide; and the old cups stay where they are.

**Paste into:** Flow → **Frames to Video** prompt box. **Start frame:** the accepted `1m-z` v2 image.
**End frame:** empty. **No Character, no Ingredients.** **Duration:** 4s. Primary:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts. The camera stays locked off on the floor and holds completely still throughout, and the light in the picture stays exactly as it is.

His fingers open and the empty coffee cup drops straight down onto the carpet beside the bin, lands with its lid on and tips over onto its side.

He keeps walking at the same unhurried pace, the phone held to his ear and his eyes on the corridor ahead, and his empty hand drops loosely to his side. His feet plant firmly on the carpet with each step.

The bin, the paper in it, the two old cups on the floor and the stains on the carpet all stay exactly where they are.

Shot at 24fps with a 180-degree shutter, so the falling cup smears while everything slow stays sharp.

Audio: the small hollow papery tap of the cup landing on carpet, his footsteps muffled on carpet tiles, and the low hum of office air conditioning. No music and no voices.

Thanks.
```

⬜ **Fallback, only if he morphs or his feet slide in the primary**: same tab, same start frame. He stops
walking instead.

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts. The camera stays locked off on the floor and holds completely still, and the light stays exactly as it is.

His fingers open and the empty coffee cup drops straight down onto the carpet beside the bin, lands with its lid on and tips over onto its side.

He comes to a standstill where he is, the phone held to his ear and his eyes on the corridor ahead, breathes, blinks once, and lets his empty hand fall to his side. The bin, the two old cups and the stains stay exactly where they are.

Shot at 24fps with a 180-degree shutter, so the falling cup smears while everything else stays sharp.

Audio: the small hollow papery tap of the cup landing on carpet and the low hum of office air conditioning. No music and no voices.

Thanks.
```

### 1m-z — the clip, v2 · **video** · written 2026-09-13, unrun · *supersedes both blocks above*

**Jack, 2026-09-13, on the fallback's result:** *"it looks very ai slop like, also the coffee does not
splash."*

#### Diagnosis, before any rewrite

🔴 **The clip was not seen by this file**, so these causes are **inferred from the prompt**, not
observed.

1. **An empty paper cup has no weight.** It is about the lightest object there is, so a model imitating
   *falling* without mass makes it drift, float or flutter. That weightless motion is the single most
   named "AI video" tell ([Why AI videos look fake](https://medium.com/@nandinilreddy/why-ai-videos-look-fake-and-how-physics-can-fix-it-bb84149831d8)).
   **Coffee left in the cup gives it mass**, and it is also what Jack asked for.
2. **"Comes to a standstill… breathes, blinks once" is a mannequin instruction.** A man mid-call does not
   stop dead and hold still to drop a cup. The fallback swapped a morph risk for a stiffness tell.
   **The walk goes back in**: he never breaks stride, which is also the joke.
3. **Nothing told it the speed.** Unprompted, these models drift toward slow motion. The fix is the
   positive phrase *at real speed* (see the negation-rewrite table in `omni-flash.md`).

#### 🔴 The splash goes against a house rule, knowingly

[`omni-flash.md` says never request a splash, ask for wetting](../../google-flow/omni-flash.md#-fluids-fail-in-two-named-ways--and-the-design-fix-is-to-put-the-hard-half-outside-the-clip-academic--community-2026-09-12),
because splashes with the wrong momentum are one of the two documented fluid failures `[academic]`.
Jack wants a splash, so it is **designed down to the smallest splash that still reads**:

- **The impact is one instant**: the lid pops off and a short burst of coffee spatters out low across
  the carpet. At real speed with the shutter clause, that is **a smear lasting a few frames**, which is
  where [a real camera would lose it anyway](../../google-flow/omni-flash.md#the-rule-that-outranks-all-of-it-a-real-camera-never-catches-the-whole-fall).
- **The rest of the clip is wetting**: a dark stain spreading out of the cup's mouth and soaking into
  the carpet tiles. That is the easy class, like `1y`'s tide and `1m-m`'s spill.
- **The sound carries the splat.** A wet slap on carpet cannot morph.
- ⚠️ **If the splash comes back wrong** (droplets hanging, coffee bouncing, or flying the wrong way), keep
  the landing and cut the splash from the prompt. **The spreading stain alone still reads as a spill.**

**Routing unchanged:** Frames tab, the accepted `1m-z` v2 frame as the start frame, end slot empty, no
Character, **4s**. ⬜ **Draft at 360p** and watch the cup's speed, the splash direction and his feet.

**Paste into:** Flow → **Frames to Video** prompt box. **Start frame:** the accepted `1m-z` v2 image.
**End frame:** empty. **No Character, no Ingredients.** **Duration:** 4s.

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts, everything happening at real speed. The camera sits locked off on the floor and the light stays exactly as it is.

His fingers open and the paper cup, still a third full of coffee, drops fast and heavy onto the carpet beside the bin. On impact the lid pops off and a short burst of coffee spatters out low across the carpet tiles, and a dark stain spreads out from the cup's mouth and soaks into the carpet.

He never breaks stride. He carries on walking at the same unhurried pace with the phone at his ear and his eyes on the corridor ahead, his empty hand swinging loosely back to his side, his feet planting on the carpet with each step.

Shot at 24fps with a 180-degree shutter, so the falling cup and the flying coffee smear with motion blur while the bin and the old cups stay sharp and where they are.

Audio: the wet slap of the cup and coffee hitting the carpet, his footsteps muffled on carpet tiles, and the low hum of office air conditioning. No music and no voices.

Thanks.
```

**Post, in Premiere:**

1. **Crop the black border.**
2. 🔑 **Cut on the tap.** The montage cuts on the beat, and the cup hitting the carpet *is* a beat. Out
   on the landing, or a frame after it.
3. ⚠️ **Watch the cup and his feet on playback, not his face.** A cup that floats, bounces back up or
   duplicates, or feet that slide, is a re-roll, not a grade.
4. ⚠️ **Nothing ships unmeasured**: run `scripts/delivery-qc.sh` ([`delivery.md`](../../video-fx/delivery.md)).

**Sources for this entry (2026-09-13):**
[Atlas Cloud — realistic human motion prompts: sliding feet, arm tempo, merging fingers](https://www.atlascloud.ai/blog/tips/mastering-kling-3.0-10-advanced-ai-video-prompts-for-realistic-human-motion) `[community]` ·
[Wearview — walking video from a single photo](https://www.wearview.co/blog/walking-video-from-single-photo) `[community]` ·
[Promptessor — image-to-video prompts in 2026](https://promptessor.com/blog/image-to-video-prompts-how-to-animate-photos-products-characters-and-art-in-2026) `[community]` ·
[Flow models & supported features](https://support.google.com/flow/answer/16352836) `[vendor]`

### 1m-g — the shoot · **spec only** · 2026-09-13 · *prompt to follow*

**Jack's ask:** *"fox hunting or bird shooting in the country like in The Gentlemen season 2."*

🔴 **Bird shooting, not fox hunting.** Hounds and a fox is animal-cruelty imagery and a
[likely refusal](../../flow/failure-modes.md#a3-harm-categories); a driven game shoot is an ordinary
sporting picture. **And the shoot is the better idea anyway** — see below.

🔑 **The research hands us the whole shot.** A British driven shoot works like this: **about twenty
beaters walk through the woods driving birds toward eight men who stand still on numbered pegs**, and
**a loader stands beside each man and hands him a reloaded gun** `[community]`
([Garden & Gun](https://gardenandgun.com/feature/sporting-south-the-driven-way/),
[driven grouse shooting](https://en.wikipedia.org/wiki/Driven_grouse_shooting)).
**Twenty people walk toward you so that you do not have to move.** That is the class system as a
sport, it is completely real, and it needs no exaggeration —
[rule 2 of this set](./shot-list.md).

- 🔑 **The Karen vantage: from the loader's position**, just behind and beside him, so we see what the
  loader sees — the back of his head, his hand out for the gun without turning, and the line of
  beaters coming out of the treeline toward them.
- 🔑 **Gate 2, and it is a genuinely new kind: a line of people employed to walk toward him.** No
  wreckage, no empty room, no box — labour as scenery.
- 🔑 **The structural rhyme is the real reason to make it.** He begins the film **in a field with a
  loader and twenty people working for him**, and ends it **in a field with a fire and nobody**
  ([12a](#12a--the-two-of-them-by-the-fire--still--written-2026-08-28-unrun),
  [12c](#12c--the-newspaper-goes-on-the-fire--still--written-2026-08-29-unrun)). **Camping is the
  same location, stripped.**
- ⚠️ **Policy design, decided before writing:** the gun is **broken open over his arm or being handed
  across** — never aimed, never fired, and **no bird is shown hit.** The birds are specks over the
  treeline. That keeps it a picture of a man standing still while others work, which is the shot we
  want regardless.
- ⚠️ **Period: early September 2008 is partridge, not pheasant** (pheasant opens 1 October) — and it
  puts him in a field in the exact week the banks failed.
- ⚠️ **Take The Gentlemen's *content*, not its look.** S2 is Tony Scott–inspired, anamorphic, smoke
  and red `[community]` — glossy and saturated, which will not cut with this montage. **Tweed, the
  formality and the absurd hierarchy are the borrowings; the register stays ours.**

### 1m-z v3 — the drop is made by the CUT · 2026-09-13 · *supersedes every 1m-z clip above*

**Jack, 2026-09-13:** *"Forget the cup dropping one, please make a new one where the model won't fuck
it up."*

🔑 **The fix is to stop asking any model for the drop at all.** The house rule in
[`omni-flash.md`](../../google-flow/omni-flash.md#the-rule-that-outranks-all-of-it-a-real-camera-never-catches-the-whole-fall)
already says so: *cut — a shot that stages it, an insert that loses it, and the aftermath.* **The
audience makes the drop in the gap between two shots** ([the gutter](../../cinematography/stills.md#3-the-gutter--what-happens-between-two-stills)).
Nothing falls, nothing splashes in motion, and nothing is stopped mid-stride.

| Shot | What it is | What the model is asked to do |
| --- | --- | --- |
| **A** `1m-z` clip | The accepted plate: he walks on, cup still dangling from his fingers | **Continue a walk already in progress.** Nothing else moves. Only about 1s is used |
| **B** `1m-z2` still | Floor-level insert: the cup on its side by the bin, lid off, coffee splashed across the tiles, still wet | **A still of an end state.** No motion, no airborne liquid, no person |
| **The edit** | Hard cut A → B on the beat, with a wet papery slap on the cut | Premiere, plus a sound effect |

**Why each is inside the engines' competence:**

- **A:** walking that is already under way is a [continuation, not a new state](../../google-flow/omni-flash.md#-ask-it-to-continue-a-state-never-to-reach-one-observed).
  **The montage uses only about a second of it**, and drift compounds over time, so the part we keep
  is the safest part. The cup is pinned in his fingers.
- **B:** a spill that has **already happened** is a flat stain on a flat floor, and there is
  [no in-progress state for §38 to refuse](#-38-at-n3--a-mechanical-in-progress-state-is-near-unbeatable-and-it-is-worth-planning-around).
  **He is not in it by framing, not by instruction.** It is a tight insert, so there is no *"the
  corridor is empty"* absence for [§27](../../google-flow/nano-banana-2.md#27--ask-for-an-object-never-an-absence--a-subtractive-shape-comes-back-inverted-observed-2026-08-30)
  to invert.
- **B uses the accepted plate as a reference** for carpet, bin, cups and light, with the role declared
  narrowly ([§29](../../google-flow/nano-banana-2.md#29--to-overrule-a-reference-on-one-element-declare-its-role-narrowly-then-negate-the-old-value-observed-2026-08-30)),
  so the cut reads as the same corridor a second later.

#### A — the clip · **video** · written 2026-09-13, unrun

**Paste into:** Flow → **Frames to Video**. **Start frame:** the accepted `1m-z` v2 image. **End frame:**
empty. **No Character, no Ingredients.** **Duration:** 4s. **In Premiere, use the first ~1s.**

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts, at real speed. The camera sits locked off on the floor and the light stays exactly as it is.

He carries on walking at the same unhurried pace toward the right of the frame, the phone at his ear and his eyes on the corridor ahead, his feet planting on the carpet with each step. The paper cup stays hanging loosely from his fingertips by its rim, swinging slightly with his stride.

The bin, the two old cups and the stains on the carpet stay exactly where they are.

Audio: his footsteps muffled on carpet tiles and the low hum of office air conditioning. No music and no voices.

Thanks.
```

#### B — `1m-z2` the aftermath · **still** · written 2026-09-13, unrun

**Model:** **Nano Banana 2**. **Paste into:** Flow → image prompt box. **Aspect:** 16:9. **Resolution:** 2K.
**Reference image:** the accepted `1m-z` v2 plate. **No Character**, because there is no person.

**Check on the result:** it is the same carpet, bin and teal light · the cup lies on its side with the
lid off beside it · the coffee is splashed flat across the tiles and still wet · no person or body part
is in frame · no readable words.

```prompt
SCENE:

The attached image is the reference for the location, the carpet, the bin, the old cups and the light, and for nothing else. This new photograph is taken a second later, down on the carpet right beside the bin.

Camera: a 35mm lens lying on the carpet a few inches off the floor, half a metre from the base of the bin, looking along the floor, so the carpet tiles run away from the lens and the bottom of the bin fills the left side of the frame. The picture is sharp from the nearest tile to the skirting board.

Subject: a white paper coffee cup with a brown card sleeve that has just been dropped. It lies on its side on the grey carpet tiles next to the bin, its plastic lid knocked off and lying upside down a hand's width away. Coffee has burst out of its mouth in a splash that fans across three carpet tiles — a wide wet dark-brown patch with a spray of drops and short streaks thrown out beyond it, all of it lying flat and still soaking in, glossy where it is freshest. The older dried brown rings and the two old crushed cups from the reference are just behind it, and the wet splash is darker and shinier than any of them.

Light: the same cool teal fluorescent light from the ceiling tubes as the reference, falling evenly along the corridor, catching a dull shine on the wet coffee.

Style: a newspaper photograph of the 2008 financial crisis, shot on a Canon EOS-1D Mark III by available light — fine digital noise in the shadows, muted colour, a cool blue-green cast from the tubes, no retouching.

Constraints: the frame holds only the carpet, the bin, the cups, the lid and the spilled coffee. The coffee lies flat on the carpet. No brand names, logos or readable labels anywhere, including on the cups and the bin. Ensure historical accuracy for 2008, and every object is British.

Compose for a 16:9 frame.

Thanks.
```

**Post, in Premiere:**

1. Crop A's black border. Use about a second of A.
2. 🔑 **Hard cut A → B on the beat**, with **a wet papery slap on the cut**. That sound does the whole
   drop. ⬜ It needs a sound: a free library effect, or record a real cup on carpet.
3. Hold B about a second, then cut out.
4. ⬜ **Optional later:** a B clip where the wet stain slowly spreads into the carpet. That is the
   easiest thing Omni does, and the next frame can be generated then if the cut wants more.
5. ⚠️ **Nothing ships unmeasured**: run `scripts/delivery-qc.sh`.

#### B — round 1, **handed over as the plate, 2026-09-13** (Jack)

- ✅ **What landed:** floor-level insert, the steel bin on the left, the cup on its side with coffee still
  in its mouth, the lid upside down, a wet splash fanned across the tiles, old rings, two crushed cups,
  and the corridor running away. No person in frame.
- ⚠️ **Deviations:** the bin came back as brushed steel rather than grey mesh, and the light is
  neutral-cool rather than teal. Neither matters at a one-second cut.
- ⬜ **Master not banked:** save it as `camera/reference/1m-z2-aftermath-ACCEPTED.png`.

#### B — the clip: he walks past and kicks the cup · **video** · written 2026-09-13, unrun

**Jack's ask:** *"either tarquin walks past and kicks the coffee cup, or walks past it sipping a similar
cup, implying he is at fault."*

🔑 **The kick, because the sip cannot happen in this frame.** The lens is on the carpet, and the top of
the frame near the camera is only about a foot off the floor. **His hands and a cup at his mouth are
above the picture.** The sip needs a different still, a higher camera with his torso in it. ⬜ That is
a separate prompt if wanted.

**Why the kick suits this plate:**

- 🔑 **Only his shoes and trouser legs are in frame, so there is no face to lose.** The identity problem
  that shapes every other clip in this montage does not exist here.
- **The fault is shown, not implied.** He scuffs the evidence away and does not break stride.
- **Frames holds the set** (bin, splash, crushed cups) and nothing about him needs binding.

#### 🔴 The risks, and what each clause does

| Risk | The clause |
| --- | --- |
| **A body entering an empty Frames plate is generated from scratch** ([walkers morph](../../google-flow/omni-flash.md#-on-frames-a-walking-extra-morphs--stillness-is-the-only-thing-that-holds-them-observed-2026-08-26)) | **Legs only, dark trousers and black shoes**, which is the lowest-detail body there is. One path: in from the right edge near the lens, away down the corridor. **Use about 1.5s**, the kick and one stride, before the receding legs have time to drift |
| **Feet slide, legs double** `[community]` | *"Each shoe plants flat on the carpet and lifts"*, stated positively. A steady walk, no hurry |
| **The kick is a contact event** (object interaction is a documented weak spot) | 🔑 **A scuff, not a punt.** The toe catches the cup mid-stride and it **skids and rolls a short way along the carpet**. That is one continuous motion with no destination named, and the paper cup is light enough that a short skid is the real behaviour. The shoe briefly covers the moment of contact, so there is [less to get wrong](../../google-flow/omni-flash.md#the-rule-that-outranks-all-of-it-a-real-camera-never-catches-the-whole-fall) |
| **Weightless or slow-motion slop** | *At real speed*, plus the [shutter clause](../../google-flow/omni-flash.md#the-shutter-is-the-tell-nobody-prompts-for) so the cup and the shoe smear |
| **The splash gets redrawn, or wet footprints get invented** | He steps on the dry carpet beside the splash, and the splash, lid, bin and crushed cups are pinned. [No fluid is asked to move](../../google-flow/omni-flash.md#-fluids-fail-in-two-named-ways--and-the-design-fix-is-to-put-the-hard-half-outside-the-clip-academic--community-2026-09-12) |
| **Speech or subtitles** ([the punctuation trap](../../google-flow/omni-flash.md#-the-speech-trap-is-punctuation-not-vocabulary)) | No colon after an action, no quotation marks, `No music and no voices.` |

⬜ **Draft at 360p.** Watch the number of legs and shoes, whether the feet slide, and whether the cup
skids and settles or instead floats or bounces up.

**Paste into:** Flow → **Frames to Video**. **Start frame:** the accepted `1m-z2` image. **End frame:**
empty. **No Character, no Ingredients.** **Duration:** 4s. **Use about 1.5s.**

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts, at real speed. The camera lies locked off on the carpet and the light stays exactly as it is.

A man in dark suit trousers and polished black shoes walks into the frame from the right edge close to the lens, heading away down the corridor, and only his legs and shoes are in the picture. As he passes, the toe of his shoe catches the fallen paper cup mid-stride and it skids and rolls a short way along the carpet. He never breaks stride and walks on away down the corridor, each shoe planting flat on the carpet and lifting.

He steps on the dry carpet beside the splash. The spilled coffee, the lid, the bin and the two crushed cups stay exactly where they are.

Shot at 24fps with a 180-degree shutter, so the moving shoe and the skidding cup smear with motion blur while everything still stays sharp.

Audio: firm footsteps on carpet tiles, the light hollow scuff and rattle of a paper cup skidding across carpet, and the low hum of office air conditioning. No music and no voices.

Thanks.
```

**Post:** crop the border · use about 1.5s from the step to the skid · 🔑 **cut out on the rattle** · if a
leg doubles or the cup floats, **re-roll, don't grade** · run `scripts/delivery-qc.sh`.

**Sources (2026-09-13):**
[Atlas Cloud — sliding feet and merging limbs in AI human motion](https://www.atlascloud.ai/blog/tips/mastering-kling-3.0-10-advanced-ai-video-prompts-for-realistic-human-motion) `[community]` ·
[Why AI videos look fake — weightless motion](https://medium.com/@nandinilreddy/why-ai-videos-look-fake-and-how-physics-can-fix-it-bb84149831d8) `[community]` ·
[Imagine.art — Omni Flash prompts guide](https://www.imagine.art/blogs/gemini-omni-flash-prompts-guide) `[community]`

### 1m-g — the shoot · **still** · written 2026-09-13, unrun

#### 🔴 Two corrections to the spec before the prompt

1. **The ending is not a field.** Canon puts the fire **in the Waitrose car park, not the woods**
   ([`story.md`](./story.md)). The spec's *"same location, stripped"* is wrong. The rhyme that
   survives is looser but still real: **outdoors, twenty people working so he doesn't have to move →
   outdoors, a fire, and only one other man with him.** Don't claim it's the same place.
2. **There is no "Nano Banana Pro 2."** The family is Nano Banana → Pro → 2 → 2 Lite
   ([§ model names](../../google-flow/nano-banana-2.md#️-there-is-no-nano-banana-pro-2-vendor-community)).
   **Use Nano Banana 2**, which is what made `1m-l` round 5, `1m-v` and `1m-z` v2, so the montage stays
   consistent. ⬜ **If the beaters come back cloned or the line comes back centred, re-fire once on
   Nano Banana Pro.** Pro is still the better pick for spatially complex frames with a crowd at distance
   ([§ leaderboards](../../google-flow/nano-banana-2.md#-corrected-2026-09-13-nano-banana-2-beats-pro-on-the-leaderboards-community)).
   ⚠️ Check the picker is not on **Lite**.

#### 🔑 The design

**The job:** it is the montage's only frame outside the City, and it gives the argument as a sport:
**a line of people walks toward him so that he does not have to move.** The spec's research stands:
beaters drive the birds toward Guns who stand at numbered pegs, and a loader hands each Gun his gun
`[community]`.

- 🔑 **Vantage: the loader's, the Karen rule.** A standing eye-height camera a pace behind him and to
  his left. **The loader is the camera**, so the loader appears only as two hands entering the bottom
  of frame holding the gun out. We see what the loader sees: the back of Tarquin's head, his hand held
  back for the gun, and the field.
- 🔑 **The gag is that he is on his phone.** His empty left hand is held back for the gun without
  turning, while his right hand holds the handset low and his head is bent over its screen. **It
  carries the montage's phone motif** (`1m-v`, `1m-z`), and it is the purest form of *doesn't look*:
  twenty people are walking at him and he is reading an email.
- 🔑 **A second, free detail: new money.** His tweed is **brand new**, stiff, with the fold creases still
  in it. The loader's cuff is **old waxed cotton, worn pale at the seams**. The class line runs through
  the handover, with no caption needed. *Observed, not invented:* the spec's rule 2.
- 🔴 **Gate 2, a new kind of cost: labour as scenery.** About fifteen beaters come out of a strip of
  cover a long way off. **It is the only cost in the montage made of people working rather than people
  losing.**

#### 🔴 The policy and slop design, decided before writing

| Risk | The clause |
| --- | --- |
| **Firearms** ([harm categories](../../flow/failure-modes.md#a3-harm-categories)) | **One gun, broken open, barrels pointing at the grass, in the loader's hands.** Nobody is aiming, no gun is closed, and the words *shoot*, *fire* and *kill* describe nothing in the frame. It reads as a sporting picture because that is all it contains |
| **Animals** | The partridges are **a few distant specks in the sky** above the beaters. No bird is on the ground and none is hit. No dog is close enough to read |
| **The crowd clones or tiles** ([§22](../../google-flow/nano-banana-2.md#22--tiling-and-cloning-in-crowd-scenes-are-a-resolution-problem-not-only-a-prompt-problem-community-2026-08-28), [crowd individuation](../../google-flow/nano-banana-2.md#-crowd-realism-is-individuation-not-adjectives-practitioner)) | Count, spacing and what each carries: an **uneven** line, some half-hidden in the crop, flags at different heights, one stick raised. 🔴 **Individuated by garment, carried object and distance, never by age or gender.** That is [what got `1m-l` past two refusals](#1m-l--round-4-policy-block-jack-2026-09-13---and-it-disproves-the-round-2-diagnosis) |
| **The loader's hands come back young, clean and generic** ([§25](../../google-flow/nano-banana-2.md#25--19-inverts-for-an-unbound-body-part--describe-it-or-get-young-clean-and-generic-observed-2026-08-29)) | Unbound, so described in full: weathered, reddened knuckles, a worn waxed cuff. No age word |
| **Hands fuse where they meet** | **They do not meet.** The loader's hands stop about a foot short of his open palm. The frame is the second before the handover, so *about to* is again the unresolved question |
| **Fake depth of field and halo** ([tells](../../google-flow/nano-banana-2.md#️-fake-depth-of-field-has-its-own-tells-practitioner-community)) | **Deep focus**, sharp from him to the hedge. Nothing is thrown out of focus, and the gun is kept clear of the lens |
| **No face, so the Character binds nothing** ([§12](../../google-flow/nano-banana-2.md#12--a-character-binds-to-a-face-no-face-in-the-shot-no-likeness-observed)) | **A deliberate choice.** He is recognisable from the back of his head and his build, and the frame is about the hand, not the face. `@2008 - tarquin` is still attached for hair and build. ⚠️ **His clothes are described anyway**, because the new-tweed detail is the point, and the prose will override the Character's suit. That is intended |
| **The Gentlemen / advert gloss** ([advert vocabulary](../../google-flow/nano-banana-2.md#️-advert-vocabulary-commissions-an-advert-observed-2026-08-26)) | Flat overcast September morning, stubble and muddy tramlines, a newspaper photograph. No *golden hour*, no *cinematic*, no haze named ([§10: atmosphere overdelivers](../../google-flow/nano-banana-2.md#10--the-atmosphere-family-is-rendered-for-free-and-overdelivers-when-named-observed-n3)) |
| **Readable text** | The peg is a **plain wooden stake**, not a numbered card, because a number is text. The phone screen is a soft glow too small to read |

**Model:** **Nano Banana 2**. **Paste into:** Flow → the image prompt box. **Aspect:** 16:9.
**Resolution:** 2K ([off-native resolution clones crowds](../../google-flow/nano-banana-2.md#-crowd-realism-is-individuation-not-adjectives-practitioner)).
**Character:** `@2008 - tarquin`. **No reference image.**

**Check these six on the result, worst first:**

- The gun is broken open and pointing at the ground, and nobody is aiming
- His hand is held back for it while his head is down on the phone
- The loader's hands stop short of his, with no fusion
- The beaters are an uneven line of different figures, not clones
- The camera is behind him at standing height
- Nothing carries a readable word or number

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. In this frame he is standing at his peg on a driven partridge day in the English countryside, reading his phone, with one hand held back for his loader to put a gun in it, while a line of beaters walks toward him across the field.

Camera: a 35mm lens at standing eye height, a pace behind him and to his left, level, taken from exactly where his loader stands. He fills the right third of the frame from the waist up, seen from behind and a little to the side, so the back of his head, his left ear and the edge of his cheek show and his eyes do not. The field runs away past him at an angle toward the left, and nothing is square to the lens. The picture is sharp from his shoulder to the far hedge.

Subject: a wide September stubble field under a flat grey sky, muddy tractor tramlines running away across it, a short plain wooden peg stake in the stubble at his feet. About a hundred and fifty metres off, a strip of tall green game crop runs along the far side of the field in front of a dark hedgerow, and a long uneven line of about fifteen beaters is coming out of it toward him, spaced irregularly, some still waist-deep in the crop and some already out on the stubble. Each is a small distinct figure — a faded wax jacket, an orange waterproof, a flat cap, a woolly hat, one with a white flag held high on a cane, one with a flag held low, one tapping a stick, one pausing to untangle a flag from the crop. Far along the field to the left, two more men stand alone at their own pegs, small and still. A few tiny partridges are lifting as distant specks above the crop.

Him: the man from the character reference, bareheaded, in a brand-new tweed shooting jacket that is still stiff, with the fold creases from the packaging plainly visible across the back and sleeves. His head is bent over a small black handset with a keyboard held low in his right hand, its screen a soft glow. His left arm is held back and out toward the camera at waist height, palm open and up, five separate relaxed fingers, waiting for a gun to be put in it without looking round. He is twenty-five, and the back of his neck and his ear are young and unlined.

The loader: only the loader's two hands and forearms come into the bottom left of the frame, holding a side-by-side shotgun out toward him, broken open at the hinge with the barrels pointing down at the stubble and the empty breech showing. The hands are weathered, with reddened knuckles and dirt in the creases, and the cuffs are an old waxed cotton jacket worn pale along the seams. The hands stop about a foot short of his open palm.

Light: flat grey overcast morning light from the whole sky, soft and shadowless, the stubble a dull straw colour, the tweed's colours muted, the far hedge a dark band.

Style: a newspaper photograph of the 2008 financial crisis, shot on a Canon EOS-1D Mark III with a 35mm lens at a small aperture by available daylight — fine digital noise, muted colour, slight overexposure in the sky, no retouching.

Constraints: the gun is broken open with its barrels pointing at the ground, and nobody in the picture is aiming or holding a closed gun. The loader is seen only as hands and cuffs. His face is turned away so that only his ear and the edge of his cheek show, and the beaters are too far away for any face to be made out. Each beater is a different figure in different clothes. The birds are only distant specks in the sky. The peg is a plain wooden stake and the phone screen is too small to read. No brand names, logos, numbers or readable labels anywhere. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

**Sources for this entry (2026-09-13):**
[Sporting Gun — technique for driven partridge](https://sporting-gun.com/shooting/technique-for-shooting-driven-partridge/) `[community]` ·
[What to expect on a driven game day — pegs, beaters' flags, loaders](https://www.shootinggirlwithanafro.com/post/what-to-expect-on-a-driven-game-day-pheasant-and-partridge-shooting-uk) `[community]` ·
[The Stalking Directory — driven partridge, what to expect](https://www.thestalkingdirectory.co.uk/threads/driven-partridge-what-to-expect.70348/) `[community]` ·
[Fliki — Nano Banana 2 prompting guide](https://fliki.ai/blog/nano-banana-2-prompting-guide) `[community]` ·
[Miraflow — Nano Banana prompts that look like real photos](https://miraflow.ai/blog/50-nano-banana-prompts-that-look-like-real-photos-copy-paste) `[community]`

### 1m-g — the shoot, v2 · **still** · written 2026-09-13, unrun · *supersedes v1 above*

**Jack, 2026-09-13:** *"he should be aiming the gun at the sky cinematically."*

#### 🔑 "Cinematically" is built with geometry, not the word

*"Cinematic"* is on the [quality-word kill list](../../google-flow/nano-banana-2.md#️-the-quality-word-kill-list-now-includes-cinematic):
it commissions glossy aesthetic mode, and so does *The Gentlemen*'s smoke-and-red look. **So the prompt
never says it, and builds it from composition instead:**

- 🔑 **One hard diagonal.** The raised barrels cut up across the grey sky from lower right to upper left,
  against the flat horizontal line of beaters below. Horizontal versus diagonal is what makes it read as
  an event rather than a pose.
- **The camera drops to chest height** (the loader half-crouched, second gun ready), so he rises above
  the horizon and the gun is against sky, not against field.
- **The decisive moment:** the gun is mounted, cheek on the stock, the instant before the shot. Nothing
  has happened yet, which [holds a still](../../cinematography/stills.md#1-what-makes-a-still-hold).

#### 🔴 Gate 2 matters more now

A man aiming a gun at the sky, shot from below, is **exactly the celebration grammar**
[principle 24](../../cinematography/principles.md) warns about. The phone gag is gone (he needs both
hands), so **the cost carries it**:

- 🔑 **The loader's worn hands in the foreground, already holding his next gun**, so the labour is the
  nearest thing to the lens.
- **The beaters' line under the barrels**, the people walking toward him so he doesn't move.
- 🔑 **New comic detail, replacing the phone:** a **blank price tag still hanging from the cuff** of his
  brand-new tweed on its plastic tie, swinging under the raised arm. The fold creases stay. **He bought
  the costume this week.** ⚠️ *Invented rather than observed*, and flagged as such. The tag is blank so
  there is no text; delete that clause if it comes back reading as a label.

#### 🔴 Policy design for a gun that is now aimed

| Risk | The clause |
| --- | --- |
| **An aimed firearm** ([harm categories](../../flow/failure-modes.md#a3-harm-categories)) | Aimed **steeply up into empty grey sky, high above everything**, which is how a real driven shoot works (the gun never swings through the line). The prompt asks for the instant before the shot, so there is no firing, no muzzle flash and no smoke |
| **Animals** | The partridges stay as distant specks over the crop, **away from where the barrels point**. No bird is hit or falling |
| **A person in front of a gun** | The beaters are **far below and ahead, and the barrels point well above their heads into the sky**, stated positively |
| **Hands fuse with the gun** ([2026's hand failure is fusion with held objects](../../google-flow/nano-banana-2.md)) | Named positively: separate fingers around the fore-end and grip. His hands are **mid-frame, not near the lens** |

Everything else is kept from v1: the loader's vantage, deep focus, beaters individuated by garment,
object and distance (never age or gender), the plain peg, and a flat overcast newspaper photograph.

**Model:** **Nano Banana 2** (not Lite). **Paste into:** Flow → image prompt box. **Aspect:** 16:9.
**Resolution:** 2K. **Character:** `@2008 - tarquin`. **No reference image.**

**Check these on the result, worst first:**

- The barrels point steeply up into empty sky, well above the beaters
- There is no flash, smoke or falling bird
- The loader's hands in the foreground hold a broken-open second gun
- His fingers are separate from the gun
- The beaters are different figures, not clones
- The price tag is blank

```prompt
SCENE:

This is one frame of a fast-cut montage about a young City of London trader in September 2008, the week the banks began to fail. In this frame he is standing at his peg on a driven partridge day in the English countryside, the gun mounted to his shoulder and aimed high into the sky, in the instant before he fires, while his loader waits behind him with his next gun and a line of beaters walks toward him across the field.

Camera: a 35mm lens at chest height, a pace behind him and to his left, tilted slightly up, taken from exactly where his loader is half-crouched. He stands in the right half of the frame from the knees up, seen from behind and a little to the side, rising above the horizon, so the back of his head, his ear and the edge of his cheek pressed to the stock show and his eyes do not. His raised barrels make one long straight diagonal up across the grey sky from lower right to upper left. The field runs away past him at an angle toward the left, and nothing is square to the lens. The picture is sharp from the loader's hands to the far hedge.

Subject: a wide September stubble field under a flat grey sky, muddy tractor tramlines running away across it, a short plain wooden peg stake in the stubble at his feet. About a hundred and fifty metres off, a strip of tall green game crop runs along the far side of the field in front of a dark hedgerow, and a long uneven line of about fifteen beaters is coming out of it toward him along the low horizon, spaced irregularly, some still waist-deep in the crop and some already out on the stubble. Each is a small distinct figure — a faded wax jacket, an orange waterproof, a flat cap, a woolly hat, one with a white flag held high on a cane, one with a flag held low, one tapping a stick. Far along the field to the left, two more men stand alone at their own pegs, small and still. A few tiny partridges are lifting as distant specks above the crop, far to the left of where his barrels point.

Him: the man from the character reference, bareheaded, in a brand-new tweed shooting jacket that is still stiff, with the fold creases from the packaging plainly visible across the back and sleeves, and a small blank white card price tag still hanging from the cuff of his raised left sleeve on a thin plastic tie. He has a side-by-side shotgun mounted firmly into his shoulder, his cheek down on the stock, the barrels pointing steeply up into the empty sky high above the field and well above the heads of the beaters. His left hand is stretched along the fore-end and his right hand is on the grip, five separate fingers on each hand wrapped clearly around the wood. His weight is on his front foot. He is twenty-five, and the back of his neck and his ear are young and unlined.

The loader: in the near bottom left of the frame, only the loader's two hands and forearms, holding a second side-by-side shotgun ready for him, broken open at the hinge with the barrels pointing down at the stubble. The hands are weathered, with reddened knuckles and dirt in the creases, and the cuffs are an old waxed cotton jacket worn pale along the seams.

Light: flat grey overcast morning light from the whole sky, soft and shadowless, the stubble a dull straw colour, the tweed's colours muted, the far hedge a dark band, and the barrels a dull dark line against the pale sky.

Style: a newspaper photograph of the 2008 financial crisis, shot on a Canon EOS-1D Mark III with a 35mm lens at a small aperture by available daylight — fine digital noise, muted colour, slight overexposure in the sky, no retouching.

Constraints: the only gun that is closed is his, and it points steeply up into empty sky, high above every person and every bird in the picture. It is the moment before the shot, so the air is clear. The loader's gun is broken open and points at the ground, and the loader is seen only as hands and cuffs. His face is turned away so that only his ear and the edge of his cheek show, and the beaters are too far away for any face to be made out. Each beater is a different figure in different clothes. The birds are only distant specks in the sky. The price tag is a plain blank card. The peg is a plain wooden stake. No brand names, logos, numbers or readable labels anywhere. Ensure historical accuracy for 2008, and every person, garment and object is British.

Compose for a 16:9 frame.

Thanks.
```

### 1m-g v2 — round 1, **handed over as the plate, 2026-09-13** (Jack)

- ✅ **What landed:** the loader's vantage, the barrels on a hard diagonal against a flat grey sky, the
  loader's filthy weathered hands in the foreground with the second gun, the new tweed, **the blank
  price tag**, the beaters in orange and wax jackets with flags, two other men at pegs far left, three
  birds, the plain stake, stubble and maize.
- ⚠️ **Deviations, accepted:**
  - The guns came back **over-and-under**, not side-by-side.
  - The tag hangs from the **jacket hem**, not the cuff.
  - The beaters are a **near-neat line, closer** than 150m, and are standing rather than walking.
  - The loader's gun **may be closed**.
  - His cheek and brow are **more visible** than asked.
- ⬜ **Master not banked:** save it as `camera/reference/1m-g-the-shoot-ACCEPTED.png`.

#### 1m-g — the clip · **video** · written 2026-09-13, unrun

#### 🔑 The design: he pulls, and misses

**The event is one bang.** His shoulder takes the recoil, the barrels kick up and settle, and **the three
birds fly on, untouched.**

- 🔑 **The miss is the joke, and it is free.** The birds simply carry on across a blank sky, which is
  the easiest motion there is (small specks on a plain ground). **Fifteen people walked a field so he
  could miss.**
- 🔑 **It also solves the policy problem.** No bird is hit or falls, so there is no animal harm to
  classify.
- **The price tag swings on the recoil**: one small pendulum, and the joke gets a pulse.
- **The recoil is one fast motion that comes back to rest**: a jolt, not a journey.

#### 🔴 The risks

| Risk | The clause |
| --- | --- |
| **The filter reads word associations, not intent**: *"shoot"* is a known false-positive trigger `[community]` ([veo3ai](https://www.veo3ai.io/blog/veo-3-safety-filters-real-faces-logos-audio-prompt-rewrites-2026)) | 🔑 **The prompt never says *shoot*, *fire*, *gun*, *kill* or *hunt*.** It says **the 12-bore goes off**, **recoil** and **the barrels**. The sound is described as **a bang**. ⬜ Untested on Omni, so the fallback removes the discharge entirely |
| **Muzzle flash or smoke overdelivers** ([particle nouns have no volume control](../../google-flow/omni-flash.md#️-particle-nouns-have-no-volume-control-observed-n2)) | **Never named.** A shotgun in daylight shows almost nothing. The bang and the recoil carry it |
| **A rigid barrel bends or morphs while moving** | The kick is small: *"a hand's width, then settles back on the same line"*. That is one short movement back to its start |
| **Fifteen walking figures morph and clone** ([walkers on Frames](../../google-flow/omni-flash.md#-on-frames-a-walking-extra-morphs--stillness-is-the-only-thing-that-holds-them-observed-2026-08-26)) | 🔑 **They came back standing, so they stay standing.** That is zero change from the plate. Only the flags stir. [Hold them still, stated positively](../../google-flow/omni-flash.md#-on-frames-a-walking-extra-morphs--stillness-is-the-only-thing-that-holds-them-observed-2026-08-26) |
| **The loader's hands, or the second gun, drift** | Pinned as steady and holding |
| **Slow motion or weightlessness** | *At real speed*, plus the [shutter clause](../../google-flow/omni-flash.md#the-shutter-is-the-tell-nobody-prompts-for) so the recoil smears |
| **Voices, since beaters shout "over"** | `No music and no voices.` No colons after an action, no quotation marks |

**Routing:** Omni Flash → **Frames**, with the accepted `1m-g` v2 image as the start frame. End slot empty.
**No Character, no Ingredients**: the geometry of the field is the argument, and a near-static clip
holds the face. **4s.** ⬜ **Draft at 360p** and watch the barrel stay straight, the birds keep flying
rather than drop, and the beaters hold still.

**Paste into:** Flow → **Frames to Video**. **Start frame:** the accepted `1m-g` v2 image.
**End frame:** empty. **No Character, no Ingredients.** **Duration:** 4s. Primary:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts, at real speed. The camera is locked off and holds completely still, and the flat grey light stays exactly as it is.

After a moment the 12-bore goes off with a single hard bang. The recoil rocks his shoulder back and the barrels kick up a hand's width, then settle back onto the same line, and the white price tag swings on its tie at his hem.

The three birds in the sky carry on flying steadily away to the left, untouched.

The beaters stay standing in their line watching, and their flags stir in the breeze. The loader's weathered hands hold the spare 12-bore steady in the foreground, and the two men at the far pegs stay where they are.

Shot at 24fps with a 180-degree shutter, so the recoil smears with motion blur while everything still stays sharp.

Audio: one flat hard bang rolling away across open fields, the wind over the stubble and the maize, and a few distant rooks. No music and no voices.

Thanks.
```

⬜ **Fallback, only if the primary is refused or comes back wrong**: same tab, same start frame. **No
discharge.** He tracks the birds and they fly on. **Add the bang in Premiere** from a library effect.

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame, as one single continuous shot with no cuts, at real speed. The camera is locked off and holds completely still, and the flat grey light stays exactly as it is.

He holds his aim and swings the barrels slowly and smoothly a little to the left, following the three birds as they carry on flying steadily away across the sky, and the white price tag sways at his hem.

The beaters stay standing in their line watching, and their flags stir in the breeze. The loader's weathered hands hold the spare 12-bore steady in the foreground.

Audio: the wind over the stubble and the maize, and a few distant rooks. No music and no voices.

Thanks.
```

**Post:** crop the border · 🔑 **cut in just before the bang and out as the birds clear**, about 1.5s ·
if the barrel bends or a bird drops, **re-roll, don't grade** · run `scripts/delivery-qc.sh`.

**Sources (2026-09-13):**
[veo3ai — Veo safety filters read word associations; "shoot" false positives](https://www.veo3ai.io/blog/veo-3-safety-filters-real-faces-logos-audio-prompt-rewrites-2026) `[community]` ·
[AI Free Forever — fixing Veo prompt errors](https://aifreeforever.com/blog/how-to-fix-veo-prompt-errors-and-get-better-ai-video-results) `[community]` ·
[Why AI videos look fake — weightless motion](https://medium.com/@nandinilreddy/why-ai-videos-look-fake-and-how-physics-can-fix-it-bb84149831d8) `[community]`

---

## Scene 4 — 2026, the Shard

### 4a — the 2026 skyline · **still** · accepted

**Recorded 2026-08-26, from Jack.**

> ⚠️ **This is byte-for-byte identical to [1a](#1a--the-2008-skyline-plate--still--accepted)**
> — same words, including *"the City of London as it stood in 2008"* and the exclusion of *"no
> tapering glass spire"*. Recorded as supplied and confirmed by Jack when queried.
>
> The reading that makes it consistent: **4a is an edit of the 1a frame, not a generation**,
> which is exactly what [`story.md` beat 4](./story.md#scene-4--2026-the-shard) says it should
> be. So the prompt that *rebuilds* 4a is 1a's prompt — it gets you the plate — and the swap on
> top of it is the small local edit canon describes. The two are one restore point, kept twice
> so neither shot depends on the other's entry surviving.
>
> **Still not written down anywhere: the wording of the swap itself.** If there was a typed edit
> instruction — replace the hero tower with the Shard, change the year to 2026 — it belongs
> here. Paste it in when convenient.

```prompt
SCENE:

Subject: a single tall dark office tower standing dead centre of frame, filling the middle third from top to bottom, seen from the air from slightly above its midpoint, with a low old city spread wide behind and below it.

Environment: the City of London as it stood in 2008, before the current cluster of glass towers was built. The hero tower is a 1980 office block built as three chevron-shaped shafts cantilevered around a central core, stepping down to three different heights, clad in bronze-dark glass with strong vertical ribbing and a slim lattice mast on the roof; it stands completely clear of everything around it and is by far the tallest thing in the frame. Behind and beside it the city is low and dense — Portland stone and red brick blocks of six to ten storeys, church spires, flat grey roofs and rooftop plant. One rounded glass tower with a diagonal diamond lattice stands a little way off to one side, and two dark flat-topped 1960s slabs sit nearer the middle. A wide grey-brown river crosses the lower third of the frame with a road bridge to the right, and a domed stone cathedral sits among the rooftops on the right. Two construction cranes stand over the low roofs in the middle distance. The sky above the hero tower is completely empty.

Camera: wide lens, high aerial, hovering level with the upper third of the hero tower and looking very slightly down, the tower centred and dead vertical, the horizon high in the frame. Deep focus, sharp from the tower all the way to the horizon.

Lighting: a cold clear spring morning, the sun low and hard from the left throwing long shadows east across the rooftops. The hero tower's dark glass reads almost black against a pale sky, and one band of windows partway up its face catches the low sun and flares bright. Distance haze softens the far horizon into flat grey layers.

Details: cinematic, filmic contrast, fine 35mm grain, atmospheric haze between camera and far city. No modern glass towers of any kind — no tapering glass spire, no curved-top tower, no wedge-shaped tower, no cluster of tall towers behind the hero. Keep every sign, banner and rooftop marking free of readable lettering.

Compose for a 16:9 frame.

Thanks.
```

**Blocking:** [`camera/camping-4a-shard-aerial.kml`](./camera/camping-4a-shard-aerial.kml) —
670m south of the Shard at 200m, looking due north, tilt 85.

---

### 4b — Tarquin at the top · **still** · accepted

Second round, accepted 2026-08-26. **Round 1 came back sad** — head tipped down, eyes on the
floor, the whole frame reading melancholy instead of king-of-the-world, and he read older than
he should. Two things fixed it.

**1. Cast `@Tarquin` and stop describing his face.** Round 1 described it with no direction to
push in, so the words only added drift. See the rule in
[`characters/tarquin.md`](./characters/tarquin.md#-when-to-describe-his-face-and-when-not-to-2026-08-26).
The one face clause that survives here is directional and points *away* from age.

**2. Name the failure in `Constraints:`.** *"He is not sad, not tired, not thoughtful, not
brooding, and he is not looking down."* Chin and eyeline are then restated after already being
described in `Action:` — the same belt-and-braces as 1b. That is what actually turned it.

Worth keeping: the empty office is reframed in the **camera** block, not the environment block —
*"space he can afford rather than space he is lost in."* Same room, opposite reading. That is
where round 1's melancholy was leaking in.

```prompt
SCENE:

Hyper-realistic documentary photograph, shot on 35mm Kodak Ektachrome — fine natural grain, muted cool-neutral colour, naturalistic daylight only, no lens flares, calm observational tone. The photographer is standing at the far end of a large office and the man has not noticed.

Subject: The man in the reference image, in a crisp pale shirt open at the collar with no tie, the cuffs fastened, tucked into flat-front charcoal trousers with a plain dark leather belt. An expensive understated steel watch and a plain heavy signet ring. A heavy charcoal wool overcoat is thrown over the back of a chair behind him. Everything well cut and quietly expensive, nothing loud and nothing branded. He is in his late forties and no older — do not deepen the lines from nose to mouth, do not hollow the eyes, and do not add grey or slackness beyond what the reference already carries.

Action: He owns the view. He stands a couple of paces back from the glass, turned three-quarters away from the camera, looking out over the city. His chin is lifted and his head is level, his eyeline going out across the rooftops and not down at the floor. His shoulders are back and open, his weight even on both feet, one hand loose in his trouser pocket and the other hanging easy at his side. His mouth stays closed with the corners drawn back and held into the beginning of a private, satisfied smirk, his lower eyelids relaxed, his brows level, the skin around his eyes untroubled. Pleased with himself, amused, entirely unbothered. Unposed, caught mid-moment, unaware of the camera.

Environment: A near-empty corner office high in a glass tower in London. Floor-to-ceiling glass on two sides meeting at the corner, a pale stone floor, a long plain desk pushed away to one side with a single chair, no papers on it and nothing on the walls. Beyond the glass, London runs away flat and grey to a hazy horizon under a blank overcast sky. No signage, branding or readable lettering anywhere in the room or outside it.

Camera and framing: 35mm lens at f/2.8, held at chest height, static. He stands right of centre and small against the glass, with the city and the empty floor carrying the rest of the frame, so the emptiness around him reads as space he can afford rather than space he is lost in. The near edge of the desk cuts into the foreground on the left, dark and completely out of focus. Focus sits on him. The frame is very slightly tilted.

Light: Only daylight through the glass — a flat white glare off the overcast sky, cool and even, coming at him from the front and side, with the ceiling above him in shadow. No sun, no fill light, no warmth anywhere.

Details: Real skin under flat window light — visible pores, a faint razor shadow along the jaw, uneven tone, a matte sheen rather than gloss. His face is naturally asymmetric. Fine natural film grain. Faint reflections of the room hanging in the window glass.

Constraints: He is not sad, not tired, not thoughtful, not brooding, and he is not looking down. His chin stays up and his eyeline stays out over the city. His mouth stays closed. Keep it plain and unglamorous, the way an ordinary press photograph of an office actually looks.

Compose for a 16:9 frame.

Thanks.
```

**Character attached:** `@Tarquin`.

> **Two notes carried forward, neither blocking.** The accepted frame reads *pleasant* rather
> than *appraising and finding wanting*, which is softer than
> [the character sheet](./characters/tarquin.md) asks for — worth knowing at **5d**, where the
> beat is his smile *fading*, and a benign smile has less distance to travel. And the face came
> back cleaner and more handsome than the sheet's *"eats well and sleeps badly"*, which is the
> direct cost of casting the Character and saying nothing: you get what it carries. If a later
> Tarquin shot needs the wear, the fix is one clause on the **worn** axis, not the **older**
> one.

---

## Scene 5 — 2026, the drive home

### 5a — the wank tank leaves the Shard · **still** · accepted

Round 3, accepted 2026-08-26. **The first two rounds are the most useful failure in the film so
far**, because the same prompt produced them both and the fault was entirely mine.

**Round 1 came back a car advert** — mirror-wet empty street, glowing lights, perfect bokeh, not a
person in sight. The prompt had asked for a car that was *"immaculate, recently valeted, water
beading on the paint"*, *"glossy"*, on *"wet tarmac holding long smeared reflections"*. Every one
of those is a detailing-advert brief. It also carried *"the gloss reads as obscene rather than
aspirational"* — **a connotation is not an instruction**; the engine draws the gloss and drops the
reading. And it stacked four light sources, against the one-key-light rule.

**What fixed it was the world, not the adjectives:** dirt (road film up the doors, salt haze,
spray behind the arches), people (an umbrella across the lens, a man waiting to cross), and street
clutter (bins, cones, an open inspection cover, a patched repair). Full post-mortem:
[`docs/google-flow/nano-banana-2.md` — advert vocabulary commissions an advert](../../google-flow/nano-banana-2.md).

Written in **Nano Banana Pro's slot order** — Subject · Composition · Action · Location · Style —
which promotes Composition above Action, and opens by naming the use case.

```prompt
A documentary press photograph for a newspaper feature about London property wealth. This is a news picture, not an advertisement.

Subject: A blacked-out BMW X8 — the enormous flagship BMW SUV, tall and flat-fronted, with a huge vertical stacked double-kidney grille filling the nose and split headlights: thin horizontal LED daytime-running strips set high across the top of each front wing, with separate main headlamp blocks below them. Long slab flank, high beltline, shallow band of privacy glass, big dark alloys. It is a working car in a London winter — rain-flecked, a grey film of road dirt up the lower doors and sprayed back behind the wheel arches, salt haze across the tailgate. An ordinary British number plate, too dirty and too blurred by movement to read.

Composition: 35mm lens at f/2.8, camera at standing height on the far pavement. The car sits low in the frame and off to the left, and the out-of-focus dark shoulder and umbrella of a pedestrian passing close to the lens cut into the right-hand third. The horizon is not quite level. The bottom third of the frame falls away into shadow.

Action: The car is pulling out from the kerb and swinging past the camera, its front three-quarter coming round, headlights on and throwing forward across the wet road. Behind it a man in a soaked overcoat waits at the kerb to cross, looking the other way. Nobody is aware of the camera.

Location: Tooley Street at the foot of the Shard, London, at night in the rain. The Shard rises out of the top of the frame directly behind the car — an enormous tapering glass spire, its facets going up into low cloud. Down one side, London stock brick and the blank arch of a railway viaduct; a bus stop, a soaked A-board folded against a wall, bin bags stacked at the kerb, traffic cones round an open inspection cover, worn white road markings and a patched repair in the tarmac.

Style: Shot on 35mm Fujicolor Superia 1600, handheld, ISO 1600, natural grain visible through the shadows. The car's own headlights are the only warm light in the frame and the only source that matters — everything they do not reach falls to cold, murky near-black. Muted, cold and unglamorous, the way a press photographer's frame looks when they did not have time to set up. Slight motion blur on the wheels and on the passing pedestrian. No lens flare.

Constraints: The number plate is unreadable, and no shop name, street sign, poster or lettering anywhere in the frame is legible.

Compose for a 16:9 frame.

Thanks.
```

> **Two accepted deviations.** The bus-stop roundel came back legible against the constraint —
> kept, because it says *London* instantly and it is a logo rather than lettering. And the frame
> is more *composed* than a snatched press photo (the Shard centred in the gap, a level horizon);
> kept, because the front three-quarter is what makes the car readable and breaking the geometry
> risks losing it. The grit is 5b's job.

**The clip took three rounds too, and both failures are now engine findings**
([multi-waypoint duplication](../../google-flow/omni-flash.md) and
[walking extras morphing on Frames](../../google-flow/omni-flash.md)). What worked: **one
continuous motion with a duration and no destination, every person pinned still.**

---

### 5b — through the glass · **still** · accepted

Accepted 2026-08-26, first round. **The most sensitive frame in the film** — these are the people
the work is for ([`the-reader.md`](../../marketing/the-reader.md)), so the brief is never
picturesque, never pitiable, never a study.

Three clauses carry that, and they are worth reusing anywhere the film looks at someone poor:

- **`Action:` opens with *"Nothing is happening."*** Nobody begs, performs, suffers visibly or
  notices the car.
- **The camera is a passenger, not an observer** — a slot cut out of a black window frame, focus
  just past the glass, the doorway already sliding toward the edge.
- **The `Style:` block ends by naming the failure**: *"Nothing here is beautiful, dramatic or
  arranged; it looks the way something looks when you pass it at twenty miles an hour."* The
  engine's instinct is to make this *moving*, and moving is exactly wrong.

```prompt
A documentary press photograph for a newspaper feature about rough sleeping in London. This is a news picture, taken from a moving car, and the photographer did not stop.

Subject: Two people bedded down for the night in the recessed doorway of a closed shop — sleeping bags, flattened cardboard under them, a rucksack, a rolled blanket, a supermarket carrier bag tucked in at the side. Ordinary winter coats, ordinary people. Both are hooded or turned away with their heads down, and no face is legible.

Composition: 50mm lens at f/2, camera inside a car at seated shoulder height, looking out through the side window. The doorway sits right of centre and is already sliding toward the edge of the frame. The dark inner edge of the window frame and the top of the door cut heavily into the left and the bottom, black and completely out of focus, so the view is a slot rather than an open frame. A few rain beads sit sharp on the outside of the glass with the street soft behind them. Focus falls just past the glass.

Action: Nothing is happening. One of them is sitting up with their knees drawn to their chest, looking down the street at nothing. Neither of them looks at the car. The street slides past with mild horizontal motion blur.

Location: A wet side street off Borough High Street, London, at night in the rain. A shuttered shopfront, a granite kerb, wet pavement, a chained bike stand, a burst bin bag, chewing gum trodden into the paving, a puddle standing in a broken kerbstone.

Style: Shot on 35mm Fujicolor Superia 1600, ISO 1600, natural grain visible through the shadows. One hard sodium street lamp above and behind the doorway is the only light source — it catches the wet pavement at the doorway's mouth and leaves everything inside the recess in near-black. Muted, cold and unglamorous. Nothing here is beautiful, dramatic or arranged; it looks the way something looks when you pass it at twenty miles an hour.

Constraints: No face is legible. No shop name, sign, poster or lettering anywhere is readable.

Compose for a 16:9 frame.

Thanks.
```

> **Deviation, accepted.** The frame came back **warmer than specified** — the sodium lamp fills
> the street rather than just catching the doorway's mouth, and one man's face reads in profile
> against the constraint. Kept: the warmth is motivated by a real sodium lamp rather than invented,
> and it is the only light in frame. Worth knowing against
> [`style.md`](./style.md)'s warmth budget, which does not list this scene.

---

### 5c — Tarquin chuckles · **still** · accepted · 🔒 the pair's only plate

Accepted 2026-08-26. Cast with **`@Tarquin`**.

The anti-advert pass from 5a applied to an interior. **The brochure sentence went** — *"black
leather, illuminated trim, faceted crystal-effect gear selector"* is a spec list, the interior
version of *"immaculate and recently valeted"* — and a week of his life went in instead: a
takeaway cup in the console holder, a folded parking ticket by the gear selector, a dry-cleaning
tag, scuffing where his cuff rests, grit on the mat. Environmental imperfection is the counter
that lives in the world rather than the capture, and it is what stops a cabin reading as a
showroom.

One light: the dashboard glow from below. Street light is explicitly bounded — *"too weak to
light anything"* — so it cannot become a second key.

```prompt
A documentary press photograph of a man driving home alone at night. This is a news picture, not an advertisement.

Subject: The man in the reference image, in a crisp pale shirt open at the collar with no tie, a heavy charcoal wool overcoat still on over it, seatbelt across his chest, both hands resting easy on the top of the steering wheel. An expensive understated steel watch and a plain heavy signet ring. This is a British right-hand-drive car and the camera faces rearward, so he appears on the LEFT of the frame. Seen from the chest up.

Composition: 50mm lens at f/2, camera low on the dashboard against the windscreen, looking back at him, angled very slightly up so it catches the underside of the jaw and a lot of dark roof lining above his head. He sits left of centre with the empty passenger side dark and open to the right. The near edge of the dashboard and the top of the steering wheel cut into the bottom of the frame, out of focus. Focus sits on his eyes. The frame is very slightly tilted.

Action: He has just amused himself. He is watching the road somewhere off to the side of the camera, not looking at it. His chin is up. His lips stay together but the corners are pulled back and held, his cheeks pushed up, his lower eyelids raised and the skin at the outer corners of his eyes creased — a closed-mouth chuckle he is having entirely on his own. No teeth. Pleased, unbothered, slightly cruel. Unposed, caught mid-moment, unaware of the camera.

Location: Inside a blacked-out BMW X8, the enormous flagship BMW SUV, at night in London. A thick flat-bottomed steering wheel with the round BMW badge visible at the centre of its hub, and a wide curved digital display sweeping across the dashboard. It has been lived in: a takeaway coffee cup jammed in the console holder, a folded parking ticket wedged by the gear selector, a dry-cleaning tag, scuffing on the leather where his cuff rests, a scatter of grit on the mat. He is alone in the car. Through the side window behind him the wet night street slides past.

Style: Shot on 35mm Fujicolor Superia 1600, ISO 1600, natural grain through the shadows. The dim cold glow of the dashboard display from below is the only light source in the car — it picks out his jaw and the front of his coat and leaves the rest of the cabin in near-black. Street light going past behind him reads as soft smeared streaks through the side glass, too weak to light anything. Cold, uneven and unflattering. Real skin with visible pores, a faint razor shadow along the jaw, uneven tone and a matte sheen rather than gloss. His face is naturally asymmetric.

Constraints: He is alone in the car. His mouth stays closed. The round BMW badge on the steering wheel hub is visible. Nothing else in the frame carries readable text.

Compose for a 16:9 frame.

Thanks.
```

### 5d — the smile fades · **animated from 5c** · accepted

> ## ⚠️ Canon changed here — 5d has no still of its own
>
> [`style.md`](./style.md) rules that *"faces do the emotional work in stillness — the Scene 5
> smile-fade is a held shot, not an animation"*, and the
> [chains table](./shot-list.md) had 5c and 5d as a matched pair of stills cut together.
> **Jack overrode that on 2026-08-26 and animated the fade instead**, from the 5c plate. It
> worked, and it is accepted. **There is no 5d still**, so the pair is now one plate and two
> clips.
>
> **Run on Veo 3.1 Fast, not Omni Flash** — the second documented exception after
> [2b's laugh](#2b--the-laugh--video--accepted), and for the same reason: a face that has to
> *change* while the shot is not near-static is the boundary Omni loses faces at.

**The craft that made it hold**, all of it inherited from 2b: the head is pinned to the headrest
and the hands to the wheel, because every degree the head turns is facial detail the engine has to
invent; appearance is **restated in text** as the anti-drift lever; the change is written as
**muscles, never as an emotion** — corners, cheeks, lower eyelids, creases, chin; and the face is
**given somewhere to stop** (*"then his face stays exactly like that for the rest of the shot"*),
because a face that is changing keeps changing until it lands on something, and the something it
lands on is always sadness.

**5c's own clip** is a pure hold — he keeps the expression for all eight seconds, and the chuckle
is put in the **audio** (*"one quiet amused breath out through his nose"*) rather than the face.
Both clips keep the exterior unresolvable: *"only darkness and a few soft points of light drifting
slowly past"*, after
[a resolvable street duplicated the shopfronts](../../google-flow/omni-flash.md).

---

## Scene 6 — the Waitrose car park

### 🖼 The plate — `camera/reference/waitrose-car-park-plate.png`

**The car park is a fixed set from 2026-08-26 onward.** An existing high-aerial frame supplies
the geography — the Waitrose fascia in green livery, the glazed barrel-roofed trolley shelter,
the brick retail unit, the painted bays, the tent pitched **in a bay** — and every scene-6 shot
is generated **anchored on it** rather than described from scratch.

Two canon corrections came out of it, both cases of **the asset beating the spec**:

- **The tent is blue and grey, not green.** [`characters/tent.md`](./characters/tent.md) said
  green; the plate says blue. The tent has to be one object in every appearance and one of them
  already existed, so the plate wins.
- **✅ The Waitrose name is on the sign, readable.** This was an open call; the plate settles it.
  The scene-10 **W-AI-trose** gag needs the fascia established here or the payoff has nothing to
  land on. Recorded in [`style.md`](./style.md).

⚠️ **The plate itself is closer to 8a than 6a** — it has the X8 already parked beside the tent,
from a high angle over wet tarmac, which is 8a's description almost word for word. Bank it there.

### 6a — first sight of the tent · **still** · accepted

Accepted 2026-08-26, first round, **reference-anchored on the plate**. Note how short the prompt
is: the reference carries the set, the light and the look for free, so the prompt does one job —
*keep this place, move the camera here* — and a long re-description would only compete with it.

**The car is never mentioned.** Anything named in a keep-list is an instruction to draw it, so
"remove the car" would have kept it; describing the surrounding bays as empty removes it.

```prompt
Use the attached image as the reference for the location. Keep the same supermarket car park exactly as it is: the same Waitrose store front and green sign, the same glazed barrel-roofed trolley shelter, the same brick retail unit, the same painted parking bays and wet tarmac, the same blue and grey dome tent pitched in its bay, the same overcast winter light and the same muted colour and grain.

Change only the camera: move it down to standing height at the far edge of the car park, about twenty-five metres from the tent, looking across the tarmac at it slightly from the side. 50mm lens at f/4. The tent sits small and low in the frame and right of centre, with a lot of empty wet tarmac between the camera and it. The roof of a parked car cuts into the foreground on the left, dark and completely out of focus. The horizon is not quite level.

The parking bays immediately around the tent are empty. A woman pushes a trolley back to the shelter in the middle distance, turned away from the camera. Nothing else is happening and nobody is aware of the camera.

A documentary press photograph on 35mm film — fine natural grain, muted cool-neutral colour, flat overcast daylight the only light source, even and shadowless, the sky pale grey and slightly overexposed. The tent is not made pitiable or picturesque; it is simply there, in the corner, where nobody has to look at it.

Compose for a 16:9 frame.

Thanks.
```

**Its clip took three rounds and produced two rules**, both now in
[`omni-flash.md`](../../google-flow/omni-flash.md):

- ⚠️ **A hinged thing given wind settles shut and stays shut.** *"The loose fabric of the tent
  stirs"* closed the door flap and left it closed. Fixed by **naming which fabric moves** (the
  taut flysheet skin, the guy-ropes — the door excluded by not being included) and **pinning the
  door open with a physical reason**: *"rolled and tied back inside the tent"*, which is a fact
  the engine can hold rather than an instruction to obey.
- ✅ **Rain on the lens is free realism.** *"Raindrops land on the front of the lens itself and
  sit there as soft round out-of-focus blobs, bending the light behind them."* Near-field,
  abstract, nothing to duplicate — and it turns the frame from a view into a photograph somebody
  stood in the rain to take. **Worth reaching for on any wet exterior.**

---

### 6b — the three reactions · **still** · accepted

Accepted 2026-08-26, first round, anchored on the plate.

**The apologetic mime is carried by hands and shoulders, never a face** — palms up, shoulders
around the ears, still walking. A gesture reads from behind; an expression does not. That is what
lets the whole crowd stay turned away, which is what makes five people safe to generate at all.

People are placed **by landmark, not by vector**: *"on the line people walk between the store
entrance and the parked cars"* is a spot that exists in the reference and can be checked against
it. *"Further down the car park"* is a direction, and unclaimed space gets treated as free.

The one constraint that matters is `Nobody stops walking.` The moment someone stops, the scene
becomes about kindness and the beat dies.

```prompt
Use the attached image as the reference for the location. Keep the same supermarket car park exactly as it is: the same Waitrose store front and green sign, the same glazed barrel-roofed trolley shelter, the same brick retail unit, the same painted parking bays and wet tarmac, the same blue and grey dome tent pitched in its bay, the same overcast winter light and the same muted colour and grain.

Change the camera: move it down to standing height on the tarmac about eight metres from the tent, on the line people walk between the store entrance and the parked cars, looking along that line so it runs away from the camera diagonally. 35mm lens at f/2.8. The tent sits low and small at the right-hand edge of the frame, easy to miss. The out-of-focus shoulder and arm of a shopper passing close to the lens cut into the foreground on the left. The horizon is not quite level.

Five or six shoppers are walking along that line between the store entrance and the parked cars, carrying bags-for-life and pushing trolleys, in ordinary winter coats — roughly half of them women, a range of ages and builds, and the group visibly mixed across Black, South Asian, East Asian and white. Every one of them is seen from behind or in lost profile and no face is legible anywhere in the frame.

Three things are happening at once and none of them is stopping. The shopper walking nearest to the tent keeps his head turned away from it and his eyes on the middle distance. A woman a few steps behind him has half-turned toward the tent and lifted both palms in a small apologetic shrug, her shoulders up around her ears, still walking — a no-change mime made without breaking stride. Everyone else streams past without registering it at all. Nobody is aware of the camera.

A documentary press photograph on 35mm film — fine natural grain, muted cool-neutral colour, flat overcast daylight the only light source, even and shadowless, the sky pale grey and slightly overexposed. Mild motion blur on the nearest walkers. Plain and unglamorous, the way an ordinary press photograph of a car park actually looks.

Constraints: No face is legible. Nobody stops walking.

Compose for a 16:9 frame.

Thanks.
```

**Its clip is the film's crowd test — five people in relative motion, and it held.** What carried
it: **keep the formation** (*"same direction, same pace, holding the same spacing, nobody
overtakes"*), which is the documented counter to figures interpenetrating; **every face already
out of the shot**, so there is no likeness to lose; and the mime given **one motion and a settle**
— hands drop, then she keeps walking — because a held shrug looks wrong and a change with nowhere
to stop keeps going.

---

### 6c — Bob's POV from inside the tent · **still** · accepted · 🔒 THE LOCK

Accepted 2026-08-26. **The most reused framing in the film** — 10a is this shot five years on,
and the rhyme is the whole device.

> ## 🔒 6c was derived from the scene-8 frame, and 10a derives from 6c
>
> The tent-interior POV existed first as a **scene-8** frame (the X8 filling the doorway — see
> below). 6c was made from it by **anchoring on that frame and changing only what is beyond the
> doorway**, so the doorway shape, the camera height, the horizon and the whole foreground are
> **inherited rather than re-derived**. That is why the rhyme is guaranteed instead of hoped for.
>
> **Do the same again for 10a, from 6c** — because 6c is the one with the *empty* bay, which is
> the surface the ruined car park has to be built into.
>
> **The car is never mentioned in the prompt.** Anything named in a keep-list is an instruction
> to draw it, so *"remove the car"* would have kept it; describing the bay as empty removed it.

```prompt
Use the attached image as the reference. Keep the doorway of the tent exactly as it is: the same shape and size of opening in the same place in the frame, the same tied-back flap, the same seams, zip tape and mesh panel, the same faded blue-grey fabric filling the rest of the frame, the same camera height and level angle, the same sleeping bag and blankets across the bottom, the same forearm and hand holding a bottle in the lower left, the same flat grey overcast light, the same muted colour and grain.

Change only what can be seen through the doorway. The parking bay directly outside is empty wet tarmac with worn white bay markings running across it, and beyond it the far side of the car park: a few ordinary parked cars in the middle distance, the glazed barrel-roofed trolley shelter, the Waitrose store front with its green sign, a lamp column, and the flat pale grey sky above.

Nothing is happening out there and nobody is in view.

A documentary press photograph on 35mm film — fine natural grain, muted cool-neutral colour, flat overcast daylight through the doorway the only light source, the inside of the tent dim and close, the tarmac outside a little brighter by comparison, the fabric falling away to near-black at the edges.

Compose for a 16:9 frame.

Thanks.
```

**✅ The Waitrose fascia is visible through the opening, at a size where `W-AI-trose` will still
read.** [`shot-list.md`](./shot-list.md) currently puts that gag in **10c**; it can now land in
**10a itself**, through the door flap, in the framing the audience has already been taught. Worth
ruling on before scene 10 is shot.

**Its clip: breathing is the motion.** The sleeping bag over his legs rises and falls — a large
soft form, low risk, and the only thing that needed saying, which is that *a living man is lying
in here*. The hand and bottle are pinned (fine articulation is a documented weak spot), the door
is pinned open with its physical reason, and the parked cars and trolley shelter are pinned
positively because a car park is a rank of near-identical objects. **The audio does the rest** —
rain on taut nylon a foot from your head is what living in a tent sounds like.

> ### ⚠️ Rain on the lens is an **exterior** move only *(ruled 2026-08-26)*
>
> It was free realism on [6a](#6a--first-sight-of-the-tent--still--accepted) and 6b because the
> camera stood outdoors in the weather. **Inside the tent it is physically impossible**, and an
> impossible optic is the same class of error as asking for a reflection in a pane the set does
> not have — the documented cause of the model rebuilding the world to make the shot possible.
> The weather moved to the doorway and the audio instead.

---

## Scene 8 — the wank tank arrives

### 8 — the tent POV with the X8 in the doorway · **still** · accepted · the master frame

**Banked 2026-08-26.** Generated before 6c and **6c was made from it** — so although it belongs
to scene 8 in the cut, it is the origin of the tent-POV geometry the film reuses three times.

The X8 fills Bob's doorway. That is the class map in one frame and it needs no narration: a tent,
a hand round a bottle, and a hundred-thousand-pound car parked where the view used to be. The
Waitrose fascia sits top right, so the scene-10 payoff has a home in the same composition.

> ⚠️ **Prompt not recorded** — this frame predates the ledger entry and was made before the
> session. Paste it in if it still exists in Flow.

---

## Scene 7 — therapy

### 7a — the consulting room · **still** · accepted

Round 3, accepted 2026-08-26. Cast with **`@Tarquin`**.

**Rounds 1 and 2 had the room and lost the face.** The wardrobe and the set landed first time; the
expression came back as mild weariness, which could have been anything. Canon's note is *genuinely
baffled*, and the line it carries is *"What **is** this feeling?"* — a man meeting an emotion for
the first time and finding it unacceptable.

**What fixed it was writing the face as anatomy and naming the wrong readings.** *"Stopped halfway
through a sentence… the next word has not arrived"*, *"the inner ends of his eyebrows pulled up
and towards each other, putting a small vertical crease between them"*, and then: *"this is not
weariness, not amusement, not sadness and not calm."* Describing it as *baffled* gets a mood;
describing the muscles gets the face. The parted lips are repeated in `Constraints:` so they
survive.

**✅ The engine improved on the brief and should be allowed to.** The prompt asked him to stare at
the ceiling; the frame has him **looking straight at the therapist**. That is better and it is
now canon — *"What is this feeling?"* is a question **addressed to someone**. Staring at the
ceiling is a man working it out alone; looking at the therapist is a demand for an answer, which
is funnier and truer to a man who has always been able to buy one.

```prompt
A documentary press photograph of a man at a therapy session. This is a news picture, not an advertisement.

Subject: The man in the reference image, lying back on a low upholstered couch with his ankles crossed and his shoes still on. He is dressed for a weekday afternoon with nothing to prove: plain dark blue jeans, a fine-gauge navy cashmere roll-neck, a quilted olive gilet still zipped over it, and polished tan suede tasselled loafers worn with no socks, so a band of bare ankle shows above each shoe. A plain heavy gold signet ring on his little finger and an old, expensive, slightly scuffed steel watch. His hands rest on his stomach, one on top of the other. Everything he has on is soft, costly and quietly ridiculous, and he looks entirely out of place — he has not worked out how to lie down properly.

Composition: 35mm lens at f/2.8, camera at seated height in the corner of the room behind and to the side of the therapist's armchair, so the out-of-focus dark shoulder and the back of the therapist's head cut into the foreground on the right and we look past them at him. He lies along the lower half of the frame, left of centre, with a lot of plain wall and quiet room above him. The horizon is not quite level.

Action: He is staring up at the ceiling, not at the therapist, and he has just stopped halfway through a sentence. His lips are parted and stay parted, as though the next word has not arrived. The inner ends of his eyebrows are pulled up and towards each other, putting a small vertical crease between them and a short row of creases across the middle of his forehead. His eyes are wide and unfocused, aimed at nothing. His head is tipped slightly back and a little to one side. He looks like a man being asked a question he cannot answer, about a feeling he has never had before and does not want. This is not weariness, not amusement, not sadness and not calm. Unposed, caught mid-moment, unaware of the camera.

Location: A tasteful, quiet, expensive consulting room in London. A plain wall in a soft warm-grey, one framed abstract print hung slightly low, a mid-century wooden armchair, a wool rug over floorboards, a side table with a box of tissues and a glass of water, a stack of journals, a plant that needs watering, a radiator under a sash window. It is comfortable rather than grand — money that does not announce itself. There is a faint worn patch on the arm of the couch where hands have rested.

Style: Shot on 35mm Kodak Portra 400, fine natural grain, soft warm-neutral colour. One sash window camera-left is the only light source — flat grey daylight coming in low and even, leaving the far side of the room in soft shadow. Calm, still and unhurried. Real skin with visible pores, uneven tone and a matte sheen rather than gloss. His face is naturally asymmetric.

Constraints: No face other than his is visible. The therapist is seen only from behind. Nothing in the frame carries readable text. His lips stay parted.

Compose for a 16:9 frame.

Thanks.
```

> ### ⚠️ Ask for patina, not wear, on anything expensive *(2026-08-26)*
>
> *"A faint worn patch on the arm of the couch where hands have rested"* came back as **a ragged
> hole with the foam showing**. The engine escalates *wear* into *damage*, and in a room whose
> whole job is **money-quiet** a hole undercuts the class read.
>
> **Kept anyway** — the face took three rounds and is the entire shot; re-rolling to fix a small
> blemish risks losing it. **Next time write the patina**: *"the fabric slightly flattened and
> darker where hands have rested."* Same signal, no damage.

**Two canon facts came out of this frame:**

- **The therapist is a man** — grey-haired, soft beige jacket over a blue shirt, seen from behind
  in the near foreground. Canon never specified a gender; the frame decided it. Recorded in
  [`style.md`](./style.md), and it matters because 7b is his shot.
- **Tarquin's leisure wardrobe is now locked** in
  [`characters/tarquin.md`](./characters/tarquin.md) — jeans, cashmere roll-neck, gilet zipped
  indoors, suede loafers, no socks. **Posh, not flash.** Salmon cords were tried first and tipped
  into caricature.

**Its clip: he finishes the sentence, then waits.** The mouth closes over about a second and the
expression holds — one motion with a settle, so it has somewhere to stop instead of drifting. The
wait is deliberate: it is the silence 7b's punchline drops into. The audio is the silence too —
a radiator tick, a couch creak, London through old glass. *Money-quiet* is a sound as much as a
look.

---

### 7b — the therapist's verdict · **still** · accepted

Round 2, accepted 2026-08-26. **No Flow Character cast** — two reference images instead.

**Round 1 sat Tarquin up.** The reverse angle got the axis and the light side right — therapist
frame-left, window camera-right, correct for a flip of 7a — but the foreground shoulder was
upright at the therapist's eye level, so the two frames could not cut: 7a has him lying back on
the couch with his ankles crossed. The therapist's eyeline was level too, aimed at a seated man.

**What fixed it was dropping the camera to couch height and putting his feet in shot.** The
camera goes low — *"at the height of a man lying on a couch, roughly a metre off the floor,
placed just behind and to the side of his head"* — and the crossed ankles in tan suede tasselled
loafers sit in the near foreground. **The feet do the continuity that a face would have had to
do**, and they carry the class read on their own: bare ankles above suede in a therapist's
consulting room is the whole joke about him, with nobody in frame to say it.

> ### 🎯 Two reference images, no Character *(2026-08-26)*
>
> The therapist has **no Flow Character and no sheet**, and his face still held across two
> generations. The method: attach **the accepted 7a frame** (room, couch, light, geometry) and
> **the round-1 frame** (his face), and cast nothing.
>
> **Casting `@Tarquin` here would have been wrong** — his face is not in the shot, and a cast
> Character is an instruction to *include* that person, which fights the one-face constraint.
> A third identity input would also have made the engine arbitrate against the therapist, who is
> the fragile one. **Cast a Character when the face is the shot; use references when it isn't.**

**✅ The engine improved on the brief twice, and both were kept.**

- **The eyeline went into the lens.** The prompt asked for *"down and just past the lens to
  camera-right"*; he looks straight down the barrel. It costs one *"unaware of the camera"* and
  it is worth it — **this is the matching half of 7a's improvement.** 7a asked him to stare at
  the ceiling and he looked at the therapist, which made *"What is this feeling?"* a question
  addressed to someone. 7b is the answer addressed back. The camera sits at Tarquin's head, so
  that is where the eyeline lands. **The film spends its one direct address here, on the
  punchline.**
- **The ankles came back sharp and large.** The prompt said *"thrown well out of focus, a soft
  shape only."* In focus is funnier and the bare ankle is legible, which soft shapes would have
  lost. Kept.

```prompt
A documentary press photograph of a man at a therapy session. This is a news picture, not an advertisement. It is the reverse angle of the reference frame: the same room, the same couch, the same afternoon, shot from the other end.

Subject: The grey-haired man in the reference images — the therapist — seated in his mid-century wooden armchair. The same face, the same build and the same clothes: an oatmeal fine-knit crew-neck jumper over a pale blue open-collar shirt, navy trousers, reading glasses pushed up onto the top of his head. Early sixties, kind, unremarkable and entirely unbothered. His notebook is closed on his knee with the pen capped and laid on top of it — he has stopped taking notes because he has reached a conclusion.

Composition: 50mm lens at f/2.0. The camera is low, at the height of a man lying on a couch, roughly a metre off the floor, placed just behind and to the side of that man's head so we look up the length of the couch at the therapist. The therapist sits centre-left of frame, from the knees up. His eyeline goes down and just past the lens to camera-right, aimed at the reclining man's face and not at us. In the near foreground at the bottom right, thrown well out of focus, a pair of crossed ankles in polished tan suede tasselled loafers with a band of bare ankle showing above each shoe, resting on the end of a low upholstered couch. The sash window and the pale wall fall away camera-right. The horizon is not quite level.

Action: He has just finished a short sentence and is waiting for it to land. His mouth is closed, the corners level. His eyebrows sit level and relaxed, with no lift and no furrow. His eyes are steady and hold the look a beat longer than is comfortable, with the faint creases at the outer corners of a man who has thought about something and finished thinking. His head is very slightly tilted. He is completely calm. This is not a joke, not a smirk, not concern, not sympathy and not drama — he looks exactly as he would recommending a change of diet. Unposed, caught mid-moment, unaware of the camera.

Location: A tasteful, quiet, expensive consulting room in London, matching the reference frame. A plain wall in a soft warm-grey behind him, one framed abstract print hung slightly low, a wool rug over floorboards, a sash window camera-right with a radiator beneath it, and further off a side table with a box of tissues and a glass of water. Comfortable rather than grand — money that does not announce itself.

Style: Shot on 35mm Kodak Portra 400, fine natural grain, soft warm-neutral colour. The sash window camera-right is the only light source — flat grey daylight coming in low and even, leaving the far side of the room in soft shadow. Calm, still and unhurried. Real skin with visible pores, uneven tone and a matte sheen rather than gloss. His face is naturally asymmetric.

Constraints: No face other than his is visible. Nothing in the frame carries readable text. His mouth stays closed. His expression stays completely level. The crossed ankles in the foreground stay out of focus.

Compose for a 16:9 frame.

Thanks.
```

**One canon change came out of this frame:**

- **The therapist's face is now held on screen.** [`style.md`](./style.md) ruled on 2026-08-26
  that he is *"only ever seen from behind or in lost profile, so no second face has to be
  held."* **Amended the same day: 7b holds it, and only 7b.** The verdict is funnier delivered
  by a face, and the continuity cost is nil because he never appears again — one shot, one
  reference image, done.

> ### ⚠️ Open — the shoulder colour *(2026-08-26)*
>
> [7a's prompt](#7a--the-consulting-room--still--accepted) describes the therapist's foreground
> shoulder as *"the out-of-focus **dark** shoulder"*. He is in an **oatmeal** jumper in both 7b
> frames. If 7a's frame really did come back dark, the pair does not cut and one of the two has
> to move. **Check the 7a frame** — the ledger cannot settle this, only the picture can.

**Two notes for the grade:** the round came back **brighter than 7a**, with warm sunlit brick
visible through the sash window, against 7a's flat grey daylight and shadowed far side. **Fix it
in Premiere, not with a re-roll** — the face and the geometry cost two rounds and are not worth
risking for a stop of exposure. The notebook also came back open with the pen in hand, losing the
*"he has stopped writing"* beat. Not worth a round either.

**Its clip: he holds.** The pen settles flat, one slow blink, one small breath that lifts the
shoulders, and then he simply waits out the shot — eyeline fixed, mouth closed, expression
unchanged. The same one-motion-with-a-settle shape as 7a. The wait is the shot: it is the
silence the narrator's punchline drops into, and it is the second half of the pause 7a opened.
Audio is the room only — the radiator ticking as it warms, one couch creak, London traffic
through old glass.

---

### 7c — the two-shot · **still** · ⬜ not yet shot

**Ruled 2026-09-09 by Kai: the therapist is a woman.** The reason is a picture problem, not a
story one — *"Tarquin looks too similar to the therapist."* Two middle-aged white men with grey
at the temples, in a warm-neutral room, in reverse angles of each other, read as one man twice.
Recasting is the cheapest fix and costs the story nothing: canon never specified a gender
(see [`story.md`](./story.md#scene-7--therapy)), the 2026-08-26 ruling in
[`style.md`](./style.md) was read off the accepted 7a frame rather than decided.

> ### 🔴 What this costs
>
> - **7b is dead.** It holds the male therapist's face for the film's one direct address. It
>   has to be re-shot or replaced.
> - **7a is probably dead.** The male therapist's grey head and shoulder are the foreground
>   occluder. A woman's back is not that shape.
> - This shot is written to **carry the whole beat on its own** — the question and the verdict
>   in one frame — so that if the pair does not come back, Scene 7 still works as a single
>   still. If Kai wants the pair back, 7a and 7b get re-shot from 7c as the reference.

**Design** *(`shot-craft`, Design mode)*

| Slot | Decision |
| --- | --- |
| **The job** | Put both halves of Scene 7 in one frame — his question and her verdict — so the beat stops depending on a reverse-angle pair whose two people look alike |
| **Register** | Documentary, human scale. Ruling R2's exception: the beat needs a person, not a monument. Gate 2 does not fire — nothing here is monumental |
| **Depth** | FG: the corner of the side table, tissues, cold tea, out of focus at the left edge · MG: him along the couch, ankles nearest · BG: her in the armchair, the wall, the sash window |
| **Focal point** | Her face. It wins on light — the window falls on her and the corner behind her drops away |
| **Reading order** | Him first (nearer, larger, horizontal), then across the empty rug to her (upright, lit, still). That gap is the sentence |
| **Light** | One source: the sash window at the far left of frame, past the head of the couch. Flat grey afternoon daylight, low and even. Falloff into the corner behind her chair |
| **Camera** | 40mm, f/2.8, side-on to the axis between them, at seated height (~1.1m). Narrower than 7a's 35mm deliberately — [less world to invent](../../google-flow/nano-banana-2.md#6--if-the-camera-cannot-physically-stand-there-the-model-rebuilds-the-set), straighter verticals |
| **Status** | He is closer and larger; she is the only upright thing in the picture and owns the height. He is paying for this and is still the smaller person in the exchange |
| **Withheld** | Which of them just spoke. He is mid-sentence; she finished thinking some time ago. Two clocks in one frame — the [unresolved question](../../cinematography/stills.md#1-what-makes-a-still-hold) that stops a still dying |
| **Motion** | None. Still. |

**Casting: `@Tarquin-new` only. No reference image.**

The one-reference house rule applies, and the slot goes to the Character. **Attaching the
accepted 7a frame would be actively wrong** — it contains the male therapist we are removing,
and [anything named or shown in a keep-list is an instruction to draw it](../../google-flow/nano-banana-2.md#7--write-the-keep-list-from-the-accepted-still-not-from-the-prose-that-made-it).
So the room is written out in prose instead. **Consequence to watch:** the room may drift from
7a. If it does and the pair is being kept, attach 7a on the *next* round with its job stated as
*the room only*.

**Her design is a differentiation problem before it is a casting one.** She is built to share no
axis with him: early fifties against his late forties, close-cropped grey-flecked hair against
slicked-back dark, small and compact against well-fed, bottle green against navy-and-olive,
working against paying. *(If Kai would rather she were white, swap the one clause — nothing else
in the prompt depends on it.)*

**The expressions are the whole ask, and the method is 7a's.** Kai's note is that AI overplays
faces. The fix already in this file works: **write the face as anatomy, then name the wrong
readings.** *"Confused"* gets a pantomime frown; *"the inner end of one eyebrow lifted a fraction
higher than the other"* gets a face. Both blocks end on a negative list and a floor —
*"a stranger would take a second to notice anything is wrong with him at all."*
The web pass agrees and adds one thing worth keeping: **real emotion lives in the eyes**, so
both eye descriptions are longer than both mouth descriptions.

**Model: Nano Banana Pro**, not Nano Banana 2 — [the standing recommendation](../../google-flow/nano-banana-2.md#which-engine-for-badcode).
NB2's reported failure mode is *too sharp, too contrasty, almost overexposed*, which is a fair
description of the slop look; Pro also plans the scene before drawing, which a two-hander with
staged depth needs. *(There is no model called "Nano Banana Pro 2" — the picker has the two
above.)*

```prompt
A documentary press photograph of a private therapy session. This is a news picture, not an advertisement.

Subject: Two people in a consulting room. The man is the cast character, lying back along a low upholstered couch with his ankles crossed and his shoes still on, his hands resting on his stomach one on top of the other. The woman is his therapist: a Black British woman in her early fifties, small and compact, with close-cropped natural hair going grey at the temples and fine reading glasses sitting low on her nose. She wears a dark bottle-green fine-knit cardigan over a plain white shirt, wide navy trousers and flat brown leather brogues, with small gold hoops and no other jewellery. Nothing she has on is expensive. She is the only person in the room who is working.

Composition: 40mm lens at f/2.8. The camera stands against the fourth wall of the room, side-on to the two of them, at the height of a seated person, roughly 1.1 metres off the floor. He lies along the lower-left third of the frame with his crossed ankles nearest the lens and slightly soft. She sits upright in a mid-century wooden armchair on the right, further away and smaller, seen from the knees up, her head in the upper third. A width of empty wool rug separates them and it is the largest single shape in the picture. In the near foreground at the left edge, thrown out of focus, the corner of a side table with a box of tissues and a mug of tea gone cold. The pair sits slightly left of centre and the horizon is not quite level.

Action: They are looking at each other. He has stopped in the middle of a sentence. His lips are barely parted and stay that way, as though the next word has not arrived. The inner end of one eyebrow is lifted a fraction higher than the other, putting a single short crease between them. His eyes are on her, steady and slightly unfocused, as though he is listening to something inside his own head. His chin is a little tucked. That is the whole expression and the rest of his face is relaxed. This is not shock, not fear, not a pantomime frown and not comedy — a stranger looking at this photograph would take a second to notice anything was wrong with him at all. She has already reached her conclusion and is waiting for him to finish. Her notebook is closed on her knee with the pen capped and laid on top of it. She is looking at him over the top of her reading glasses rather than through them, her chin level. Her lips are closed and pressed a fraction thinner than neutral and her jaw is very slightly set. Her eyes are steady and hold the look a beat longer than is comfortable, and one eyebrow sits a hair lower than the other. Everything else about her is still. This is not a scowl, not an eye-roll, not a smirk, not a glare and not sympathy — she is being paid to keep listening and has stopped. Both faces are underplayed and neither of them is performing. Unposed, caught mid-moment, both unaware of the camera.

Location: A tasteful, quiet, expensive consulting room in London. Plain soft warm-grey walls, one framed abstract print hung slightly low, a wool rug over bare floorboards, a stack of journals on the floor beside the armchair, a plant that needs watering, and a tall sash window at the far left of the frame past the head of the couch, with a radiator beneath it chipped at one corner. Comfortable rather than grand — money that does not announce itself. The fabric on the arm of the couch is slightly flattened and darker where hands have rested.

Style: Shot on 35mm Kodak Portra 400, fine natural grain, soft warm-neutral colour. The sash window is the only light source — flat grey afternoon daylight coming in low and even, crossing the room and landing on her, with the corner behind her armchair falling away into soft shadow. Calm, still and unhurried. Real skin on both of them with visible pores, uneven tone and a matte sheen rather than gloss. Both faces are naturally asymmetric.

Constraints: Only these two people are in the room. Nothing in the frame carries readable text. His lips stay barely parted. Her mouth stays closed. The turn-ups on his jeans sit above the ankle bone. Both expressions stay small.

Compose for a 16:9 frame.

Thanks.
```

**One deliberate exception to the never-describe-a-cast-character rule**, and it is the only
one: *"the turn-ups on his jeans sit above the ankle bone."* The bare ankle is
[the joke and it is load-bearing](./characters/tarquin.md#-the-bare-ankles-do-not-survive--and-they-are-the-joke),
and it has now failed three plates in a row because *"a band of bare ankle shows"* describes a
**result** rather than a place. An ankle bone is a landmark the engine can find. This is the
untested fix that sheet already proposes — **7c is the test.**

**Two anti-slop notes on what is deliberately absent:**

- **No worn patch.** 7a asked for *"a faint worn patch where hands have rested"* and got a
  ragged hole with the foam showing — [the engine escalates wear into damage](#7a--the-consulting-room--still--accepted).
  This one writes the patina instead: *slightly flattened and darker*.
- **One light, one clause.** The [stacked-lighting tell](../../google-flow/nano-banana-2.md#5-anti-slop-restated-from-the-photorealism-pass)
  is what makes a frame read as *lit* rather than *photographed*. One window, one direction,
  one stated falloff, and nothing else in the room emits.

---

#### ✅ Shot and accepted 2026-09-09, round 1 — what held, what drifted

**First-time pass.** Configuration for reuse: **Nano Banana Pro · `@Tarquin-new` cast · no
reference image · the room written out in prose · 16:9.**

**Held:** the whole staging — the side-on geometry, the empty rug as the largest shape, the
crossed ankles nearest the lens, the tissues and the cold tea out of focus at the left edge, the
sash window and its chipped radiator, the plant, the journals stacked on the floor. Her design
held completely, wardrobe and glasses included. **And both expressions came back small** — the
anatomy-plus-wrong-readings method worked on two faces at once, which is one more than 7a proved.

> ### ✅ `[confirmed 2026-09-09]` — "above the ankle bone" fixes the turn-ups
>
> **The bare ankle survived, first time.** Three earlier plates put the turn-ups straight down
> onto the shoe against a requirement written twice, including in `Constraints:`. The change was
> a single word: *"a band of bare ankle shows"* describes a **result**; *"the turn-ups sit above
> the ankle bone"* names a **landmark the engine can find.**
>
> 🔑 **Generalise it, because it is the same rule as [naming where the photographer
> stands](../../google-flow/nano-banana-2.md#3c--name-where-the-photographer-stands-not-what-the-shot-looks-like):**
> anatomy and architecture are checkable, results and quantities are not. Promoted into
> [`characters/tarquin.md`](./characters/tarquin.md#-the-bare-ankles-do-not-survive--and-they-are-the-joke).

**Drifted, all of it kept:**

- **✅ He is sitting up, not lying back.** The prompt said *lying back along the couch*; he came
  back propped upright with his legs stretched out and his ankles crossed on the couch. **Better,
  and now canon** — a man lying flat has surrendered to the process, and Tarquin has not. He is
  sitting in a therapist's room like a man in an airport lounge. *(It also no longer matches 7b's
  reclining geometry, which is moot: 7b is dead.)*
- **The pen is in her hand, not capped on top of the closed notebook.** ⚠️ **Second sighting —
  7b did exactly the same thing.** *"He has stopped taking notes because he has reached a
  conclusion"* is a **story fact expressed as prop placement**, and the engine draws a therapist
  with a pen in her hand because that is what the words *therapist* and *notebook* pull. **Do not
  spend a round on it.** If the beat matters, it belongs in the motion prompt as an action —
  *she sets the pen down* — not in a still as a state.
- **The framed print hangs high, not slightly low.** Nothing depends on it.
- ⚠️ **The couch arm came back with a visible tear near her end** *(read off the frame — worth
  Jack's eye to confirm)*. **This is the second time and the phrasing was already the fix.**
  7a asked for *"a faint worn patch"* and got a hole; 7c wrote the patina — *"slightly flattened
  and darker where hands have rested"* — **and got damage anyway.**
  🔑 **Promote the rule: on anything that should read as expensive, do not name the wear at all.**
  Money-quiet rooms are legible from the objects in them; the engine reads any wear noun as
  permission to break something. Next time the clause is simply deleted.

---

### 7c-y — the therapist explains a feeling · **video** · written 2026-09-09, unrun

**The beat:** she is explaining to him what a feeling is, patronisingly, and he is not getting
there. **No dialogue** — the narration is recorded separately, as always.

#### 🔴 The design problem, and the answer that solves three risks at once

*"Explaining, patronisingly, with no dialogue"* pulls toward the two things this engine is worst
at and the two things that most reliably read as AI:

| The obvious way to shoot it | Why it is the wrong instruction |
| --- | --- |
| She talks; we watch her mouth | **Mouth-audio desync is a named 2026 slop tell** `[community]`, and the narration is recorded later, so a visibly talking mouth is a permanent lip-sync liability in the cut |
| She makes an explanatory hand gesture | **Hand-morph frames are top of the same tell list**, and fine hand articulation is a [documented Omni weak area](../../google-flow/omni-flash.md#design-the-shot-around-the-difficulty-ranking-not-against-it). Her hands are holding a notebook and a pen — the worst possible subject |

🔑 **So the clip is the pause, not the sentence.** She has just finished a phrase and is waiting
to see whether it landed. **Patronising is a tempo, not a gesture** — the head that tilts a
fraction and holds, the look that stays a beat too long, the willingness to simply wait for a
grown man to catch up. It needs no mouth and no fingers.

**And the button is the intake of breath before the next sentence.** The clip ends as her lips
part very slightly to start again — and cuts. Funnier than showing the sentence, zero lip-sync
cost, and it hands the recorded narration a clean place to land.

This is [7a and 7b's established shape](#7a--the-consulting-room--still--accepted) — *one motion
with a settle* — run backwards: **one settle with a motion at the end.**

#### 🔴 The single most valuable anti-slop clause here is breathing and blinking

New this pass, and it is worth more on a two-hander than everything else combined. The 2026
tell-lists name **biological motion irregularity** — *"blinking, breathing, or micro-expressions
being absent, stiff, or unnaturally timed"* — among the twelve most consistent AI-video tells
`[community]`. A near-static shot of two seated people is **the exact shot that fails this way**:
there is nothing else in frame to carry life, so if they do not breathe they are waxworks.

**Two clauses, and neither is optional on any shot of a person doing nothing:**

- **Prompt the breathing and the blinking explicitly.** They are the whole performance here.
- 🔑 **State that they do not blink together.** Two people blinking on the same frame is uncanny
  in a way nobody can name and everybody sees. Unprompted, a model has no reason to stagger them.

#### 🔴 Tab: Frames. Not Ingredients, and it is not close

[The tab rule](../../google-flow/omni-flash.md#-the-tab-rule) asks one question — *what can this
shot not survive losing?* **Her face.** She was invented in the 7c still forty minutes ago; she
has no Flow Character, no sheet and no other picture. Those pixels are the only copy that exists.

- **Ingredients [re-renders every person from scratch](../../google-flow/omni-flash.md#-ingredients-re-renders-faces--it-will-not-hold-an-unnamed-person)**
  and explicitly will not hold an unnamed person. It would redraw her, and there would be nothing
  to compare the result against.
- **`@Tarquin-new` is not cast, and must not be.** Characters live on Ingredients, and
  [the two tabs are mutually exclusive in Flow's UI](../../google-flow/omni-flash.md#️-the-combined-mode-does-not-exist-in-flow)
  `[confirmed 2026-08-16]`. Choosing the Character means choosing to lose her. His identity is
  already in the frame we are continuing from.
- **No end frame.** Omni 1.1 now has a last-frame slot
  ([seventh pass](../../google-flow/omni-flash.md#seventh-pass--omni-11-flash-and-the-speech-punctuation-trap-2026-09-09)),
  and the standing rule is still [never to pin an `endImage`, which morphs](../../video-fx/hybrid-method.md).
  A near-static clip does not need one.

#### ⬜ No push-in, deliberately — and this one is a real decision

The push-in is [the one move an eight-second clip means something with](../../cinematography/motion-and-cutting.md#1-movement),
and 8b-fog spent it well. **Not here.** The subject of this frame is **the width of empty rug
between the two of them** — that gap is the whole joke about what money buys you. A push-in
closes the gap, which is the one thing in the picture that must not change. **The stillness is
the argument.** Camera locked in the prompt, and nothing added in post either.

#### ⬜ And no shutter clause, deliberately

The [24fps / 180° shutter line](../../google-flow/omni-flash.md#the-shutter-is-the-tell-nobody-prompts-for)
is `[confirmed]` and earns its place **on shots with fast motion in them**, because it tells the
model which frames to smear. Nothing in this clip moves fast enough to smear. It would be a word
that buys nothing, and [the biggest lever on this engine is subtraction](../../google-flow/omni-flash.md#length-three-to-four-sentences-and-the-lever-is-subtraction).

#### ⚠️ Two speech traps, one of them new

- **Never write a colon after a person's action, and never use quotation marks.** `[community]`,
  2026-09-09: in Omni, `Woman says: hello` **triggers synthesised speech**, and
  `Woman says: "hello"` **burns the words on screen as a subtitle**. Both are catastrophic here
  and both are punctuation, not vocabulary. The block below contains neither character.
- **`No music and no voices.`** is a negation and it is the sanctioned kind — it is Google's own
  documented idiom, and it is [the exact phrasing that worked on 8b-fog](#8b-fog--the-clip--video--ran-and-accepted-2026-09-08).
  Reused verbatim rather than improved.

**Length ~110 words.** The [open conflict](../../google-flow/omni-flash.md#-open-conflict-how-long-should-an-omni-prompt-be)
is still open; the independent 2026 testing that says **30–80 words** is one more data point, and
our own accepted 8b-fog ran ~105. The resolution we use is unchanged — **the axis is kind, not
length** — and every sentence below describes *what the shot is*, not how to achieve it.

**Model: Omni Flash. Tab: Frames. Attach the accepted 7c still as the frame — nothing else, no
Character, no Ingredients, no end frame.** Paste into the **prompt box on the Frames tab**:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. The camera is locked off on a tripod and holds completely still for the whole shot.

The woman has just finished a sentence and is waiting to see whether it landed. She tilts her head a fraction and holds it there, keeping her eyes on him a beat longer than is comfortable. Near the end of the shot her lips part very slightly as she draws breath to start again, and the shot ends there.

The man keeps looking at her. His eyes drop for a moment and come back up to her face, and he swallows once.

Both of them breathe, and they blink at different times. Everything else in the room stays still.

Audio: a radiator ticking as it warms, one creak from the couch, and faint London traffic through old glass. No music and no voices.
Thanks.
```

**⬜ The talking version is now its own entry, not a swapped paragraph.** Jack asked for it
2026-09-09 — see [`7c-y2`](#7c-y2--the-therapist-explains-a-feeling-mouths-moving--video--written-2026-09-09-unrun),
which changes the audio clause, the event count and the do-not-go-closer rule. **Run both:** this
one asks whether the *pause* carries the joke, `7c-y2` asks whether the *explanation* does, and
the still is already paid for.

**Post, in Premiere, in this order:**

1. **A 10–15% speed adjustment** across the clip. *"Unnaturally smooth motion"* is a named tell
   and the counter is a ramp, not a prompt change `[community]`.
2. **Film grain at 10–15% opacity** over the finished clip — the motion equivalent of the Portra
   grain already in the still.
3. ⚠️ **Nothing ships unmeasured** — `scripts/delivery-qc.sh` before anything leaves the machine
   ([`delivery.md`](../../video-fx/delivery.md)).

---

### 7c-y2 — the therapist explains a feeling, mouths moving · **video** · written 2026-09-09, unrun

**Jack asked for the talking version, 2026-09-09**, having read the lip-sync cost on
[`7c-y`](#7c-y--the-therapist-explains-a-feeling--video--written-2026-09-09-unrun). This is that
shot, built properly rather than as a swapped paragraph — the audio clause, the framing argument
and the event count all change when a mouth moves.

**Run both.** They are cheap and they answer different questions: `7c-y` asks whether the *pause*
carries the joke, `7c-y2` asks whether the *explanation* does. Nobody knows, and the still is
already paid for.

#### 🔴 The dependency this version creates — read before shooting

**A visibly talking therapist commits the film to a recorded therapist voice**, because the mouth
in the picture now has to belong to somebody. [`narration/ai-studio-cast.md`](./narration/ai-studio-cast.md)
has **two voices — Bob (`Algenib`) and Tarquin (`Zubenelgenubi`) — and no therapist.**

🔑 **This is not a blocker and it may be an upgrade.** Scene 7's punchline is *hers*:
*"I don't think there's any amount of therapy that can help you. You need the most powerful
psychedelic known to man."* A clip of her visibly delivering it is stronger than a narrator
reporting it, and it spends the line on a character rather than on the voice-over. **But the job
is now real:** a third AI Studio voice, built the same way as the other two — a Black British
woman, early fifties, London, warm and unhurried, and completely unbothered.
⬜ **Not built. It is the gate on this version, not on the still.**

#### ⬜ `7c-y`'s reason for existing still stands

The pause version is not the timid option and should not be treated as one. It ends on her
drawing breath to start again, it needs no third voice, and it carries **zero** of the two named
tells below. If both clips come back usable, that is a real choice about whether Scene 7's
verdict is *heard* or *implied* — and it belongs to Jack, not to this file.

#### 🎯 The two tells a moving mouth turns on, and what actually counters them

| Tell `[community]` | The counter available here |
| --- | --- |
| **Mouth-audio desync on avatars** | 🔑 **We discard the generated audio anyway.** The recorded VO is laid over it in Premiere, so desync is a *cutting* problem, not a generation one — and it is solved by cutting to her on a phrase boundary rather than by prompting |
| **Morphing on lips, teeth and clothing edges** — the artefact concentrates there `[academic]` | 🔑 **Distance is already doing the work, for free.** She is the further, smaller figure in this two-shot: her mouth is a few dozen pixels, not a close-up. **This is the same finding as 8b-fog's forty-metre silhouette** — the frame we already have is the mitigation, and it is an argument for *not* pushing in |

**Which gives the one hard rule for this variant: do not go closer.** A single on her would put
the exact failure surface in the middle of the frame at full size. The two-shot is what makes a
talking mouth safe.

#### ⚠️ The audio clause changes, deliberately, and it is the one judgement call here

`7c-y` and [8b-fog](#8b-fog--the-clip--video--ran-and-accepted-2026-09-08) both close with
**`No music and no voices.`** — proven phrasing, and it is *wrong here*: on a shot whose whole
subject is a woman speaking, *no voices* is as likely to freeze her mouth as to mute the track.

**This block uses `No dialogue and no music.` instead** — `no dialogue` is
[Google's own documented idiom](../../google-flow/omni-flash.md#-negatives-do-not-work-and-they-actively-backfire)
and it names the **audio track**, not the performance.

🔑 **The asymmetry settles it.** If a synthesised voice comes back anyway, it costs nothing — the
audio is discarded and replaced. If the mouths come back frozen, that is a wasted generation.
**Take the cheap failure.**

#### ⚠️ Two events, and no more

*"Stacking three or more events in one clip"* is a named Omni mistake `[community]`. This clip
has exactly two — **she talks in short phrases; he starts to say something and does not.**
Breathing and blinking are not events, they are the [biological-motion
clause](../../google-flow/omni-flash.md#-biological-motion--the-anti-slop-clause-for-any-shot-of-a-person-doing-nothing),
and they stay.

**His beat is why this version might beat the pause.** A man opening his mouth to ask a question
and finding he does not have it is the whole of Tarquin in one gesture — *"What **is** this
feeling?"* is a question he cannot finish asking. It costs one small motion and it is the funnier
half of the frame.

#### ✅ Unchanged from `7c-y`, and for the same reasons

**Frames tab · the accepted 7c still as frame 0 · no Character, no Ingredients, no end frame ·
camera locked · no push-in · no shutter clause · hands stay put.** The reasoning is
[in the 7c-y entry](#7c-y--the-therapist-explains-a-feeling--video--written-2026-09-09-unrun)
and none of it moves because a mouth does. The hands clause matters *more* here, not less:
fine hand articulation is a documented weak area and she is holding a pen.

**⚠️ Punctuation check before firing — this block contains no colon after a person's action and
no quotation marks anywhere.** In Omni a colon
[synthesises speech and a quotation mark burns a subtitle](../../google-flow/omni-flash.md#-the-speech-trap-is-punctuation-not-vocabulary).
The word *Audio* is followed by a colon, which is a label rather than a speaker, and is the same
construction the accepted 8b-fog block used.

**Model: Omni Flash. Tab: Frames. Attach the accepted 7c still as the frame — nothing else, no
Character, no Ingredients, no end frame.** Paste into the **prompt box on the Frames tab**:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. The camera is locked off on a tripod and holds completely still for the whole shot.

The woman is explaining something simple to him, slowly. She talks in short phrases with a small pause after each one, watching his face between them to see whether he is following. Her head is tilted a fraction. Her hands stay exactly where they are, resting on the notebook.

The man watches her. Partway through, his mouth opens as though he is about to ask something, and then closes again without a word. He swallows once and keeps looking at her.

Both of them breathe, and they blink at different times. Everything else in the room stays still.

Audio: room tone only, a radiator ticking as it warms, one creak from the couch, and faint London traffic through old glass. No dialogue and no music.
Thanks.
```

**Post, in Premiere — same as `7c-y`, plus one:**

1. **Cut on a phrase boundary, not on a frame count.** She pauses between phrases by design; those
   pauses are the edit points, and they are what makes a recorded VO sit over generated mouth
   movement without reading as a dub.
2. **A 10–15% speed adjustment** across the clip against the smooth-motion tell `[community]`.
3. **Film grain at 10–15% opacity.**
4. ⚠️ **Nothing ships unmeasured** — `scripts/delivery-qc.sh`
   ([`delivery.md`](../../video-fx/delivery.md)).

---

## Scene 7 — the shot/reverse rebuild *(2026-09-09)*

**Jack's call, 2026-09-09: go to close-ups — her talking, him listening.** This supersedes
`7c-y` and `7c-y2` as the *plan* without discarding either; see
[what happens to them](#what-happens-to-7c-y-and-7c-y2) below.

### 🔴 Yes, separate prompts — four of them, and the reason is not style

**One clip containing both close-ups would require the model to cut**, and a cut is the one thing
we spend a clause *suppressing* on every other shot
([`no cuts` / `single continuous shot`](../../google-flow/omni-flash.md#-negatives-do-not-work-and-they-actively-backfire)
is sanctioned idiom precisely because Omni's default is multi-shot). Asking for one hands the
model the cut point, the two framings and the timing, none of which it has any reason to get right.

🔑 **And the house rule already settles it: [cutting is free and generating is
not](../../google-flow/omni-flash.md#the-rule-that-outranks-all-of-it-a-real-camera-never-catches-the-whole-fall).**
Two clips cost the same as one and give us the cut point, the durations, and the ability to
re-time in Premiere without spending a generation.

**But it is four prompts, not two, and this is the part worth knowing before starting.** The
Frames tab needs a **start frame**, and we do not have close-up stills — 7c is a wide two-shot.
So the chain is:

| # | What | Tool | Depends on |
| --- | --- | --- | --- |
| **7d** | CU therapist — still | Nano Banana Pro | the accepted 7c still, attached, job = **her face** |
| **7d-y** | CU therapist talking — clip | Omni Flash, Frames | 7d accepted |
| **7e** | CU Tarquin — still | Nano Banana Pro | `@Tarquin-new` cast |
| **7e-y** | CU Tarquin listening — clip | Omni Flash, Frames | 7e accepted |

⚠️ **One at a time, still then video** — no batch of stills. 7d first; everything downstream
reads off what actually comes back.

### ✅ This is a better scene than one clip was, and the reason is structural

The 7c wide is not wasted by going closer — **it becomes the establisher, which is what it should
always have been.** [`motion-and-cutting.md`](../../cinematography/motion-and-cutting.md#2-designing-a-sequence):
*establish geography once, early; then every closer shot spends its whole budget on feeling
instead of re-explaining where we are.* And *pick a direction for shot size and hold it —
wide→close is the default shape and reads as moving toward the truth.*

**The argument the scene makes, in one sentence:** *money buys you the professional, but it cannot
buy you the vocabulary.* Three steps, one per shot:

1. **7c — two people and a gap.** The width of empty rug between them is the joke about what he
   has paid for. Banked; it does not need to be in every shot.
2. **7d — she explains it, patiently, at the speed you would use on a child.**
3. **7e — he still does not have it.** 🔑 **His close-up is the button** — *"one shot, often
   small, closing the transaction the scene opened."* A man opening his mouth to ask a question
   and finding he does not own it.

### 🎯 The morphing risk is real, and the sequence is itself the mitigation

Going closer was flagged against on `7c-y2` because [morphing concentrates on lips, teeth and
clothing edges](#7c-y2--the-therapist-explains-a-feeling-mouths-moving--video--written-2026-09-09-unrun)
and distance was doing that work for free. That cost is now being paid deliberately. **Three
things pay it down, and none of them is a smaller idea:**

- 🔑 **Only one of the two clips has a moving mouth.** He is *listening* — his half of the
  sequence carries zero lip risk by construction. This is the house rule *"when a shot needs a
  documented weakness, cut around it instead"* arriving as a scene structure rather than a fix.
- **Medium close-up, not a tight face.** Head and shoulders, top of frame just above the head,
  bottom at mid-chest. It reads as a close-up, keeps the mouth off the centre of the frame, and
  it is the correct size for the documentary register anyway — a tight face is a drama close-up,
  not a press photograph.
- **We can cut away from her mouth whenever it misbehaves.** Two clips means the edit chooses
  which frames of her survive. One clip would not have.

### 🔴 The axis, and it must be written into both prompts

7c fixes the geography and a shot/reverse pair that ignores it will not cut. **In 7c he is
frame-left looking right; she is frame-right looking left.**

| | Camera sits | She/he looks | The window |
| --- | --- | --- | --- |
| **7d — her** | just past **his** shoulder, on the left side of the room | **frame-left**, at him | behind the camera to its left → she is lit near-frontally. Background: the plain warm-grey wall |
| **7e — him** | just past **her** shoulder, on the right side of the room | **frame-right**, at her | now **behind him**, over his shoulder at the edge of frame → he is back-lit, his face filled by light bouncing off the pale wall opposite |

🔑 **That lighting asymmetry is the scene's argument in one variable, and it is free — it is just
where the window already is.** *She has the light and the answer; he has a window blowing out
behind his head and no idea.* It also hands his frame the [one bright anchor](../../cinematography/frame.md#5-light)
that stops a soft dark portrait reading as a broken file.

⚠️ **Do not let the back-light kill his face.** State the bounce explicitly — a set fact left
unsaid is [a set fact the model gets to decide](../../google-flow/nano-banana-2.md#6--if-the-camera-cannot-physically-stand-there-the-model-rebuilds-the-set).

### 🔴 Each person keeps their side of the frame — and both drafts got it backwards

**Corrected 2026-09-09, after both prompts were written and 7d had already been handed over.**

**In 7c he is screen-left and she is screen-right. That does not change in a reverse angle.** The
rule that keeps a shot/reverse pair cutting is that each person **holds the side of the frame they
occupied in the master**, which means the foreground shoulder in an over-the-shoulder sits on the
side belonging to *the person whose shoulder it is* — not opposite the subject by reflex.

| Shot | Camera | Foreground shoulder | Subject | Looking |
| --- | --- | --- | --- | --- |
| **7d — on her** | past **his** shoulder, left end of the room | **his, lower LEFT** | her, centre-right | **frame-left** |
| **7e — on him** | past **her** shoulder, right end of the room | **hers, lower RIGHT** | him, centre-left | **frame-right** |

Both drafts had the shoulder mirrored, which would have flipped the geometry and produced a pair
that does not cut — two people apparently looking the same way.

🔑 **Second geometry error in one entry, and the two have the same cause:** an angle written from
what it should *look like* rather than from where the camera is standing in a room that already
exists. **[The window](#️-check-the-window-against-the-room-before-writing-it--this-entry-got-it-wrong-first)
and the shoulder are the same check.** Walk the room before writing any reverse: where is the
camera, which end is the window, and which side does each person hold?

### ✅ Both are over-the-shoulder, and that is proven in this room

Each close-up puts the other person's out-of-focus shoulder and the back of their head in the
near foreground. Two jobs at once: it is [the foreground occluder that stops a frame reading
flat](../../cinematography/frame.md#1-depth-is-the-first-thing-to-fix) — the cheapest fix there
is — and it locks the eyeline geometry so the pair cuts.

⚠️ **The known failure is an invented face in the foreground** (it happened on 8b). The counter is
already proven in this exact room: [7a](#7a--the-consulting-room--still--accepted) ran
*"the out-of-focus shoulder and the back of the therapist's head cut into the foreground"* and
came back clean. **Name a shoulder and the back of a head, positively, and never a profile.**

### What happens to `7c-y` and `7c-y2`

**Neither is cancelled and neither is urgent.** They are clips of the establisher, and the
establisher may still want to move — *(the 7c still itself is accepted and unaffected either
way)*. **Shoot the close-ups first**: if 7d and 7e carry the beat, 7c can stay a held still under
narration and no clip is needed at all, which is the cheaper film. Revisit after.

---

### 7d — close on the therapist · **still** · written 2026-09-09, unrun

**Cast nothing. Attach the accepted 7c still as the only reference, job stated: her face.**
She has no Flow Character, no sheet and no other picture — those pixels are the only copy of that
face that exists, which is the same fact that ruled Ingredients out for the clips.

> ### 🔴 Read this before firing 7d — the reference may not hold her face
>
> **[7e proved on 2026-09-09](#7e--close-on-tarquin--still--written-2026-09-09--shoot-after-7d)
> that a wide-shot reference does not carry a face at close-up range**, and 7d is built the same
> way off the same wide. Expect the same failure. **She has no Character to fall back on**, so
> the fix is the reference, not the casting:
>
> 1. 🥇 **Crop the 7c still to her head and shoulders in Flow's crop tool, and attach the crop
>    instead of the full frame.** Same pixels; the face now fills the reference it is read from.
>    Zero generations. **Do this first.**
> 2. **Make her a Flow Character** from the 7c still — permanent, and owed anyway if Scene 7 keeps
>    her face on screen.
>
> ⚠️ **If the crop is used, the room comes with it no longer** — a head-and-shoulders crop shows
> wall and not much else, which is fine here because the Location slot below is already short and
> the wall behind her is plain.

**⚠️ The Location slot is deliberately short.** [Reference attached → the Location slot shrinks to
what the reference cannot show](../../google-flow/nano-banana-2.md#2--do-not-restate-what-the-reference-already-shows).
The 7c frame carries the room, the light and the look for free; re-pasting the full room paragraph
would be two authorities on one set and is a known drift source. The prompt's job here is **the
camera and the face**, not the room.

**And the camera is named as a place, not as a framing** — *just past his shoulder, on the couch
side of the room* is [a position that either exists in the attached picture or does not](../../google-flow/nano-banana-2.md#3c--name-where-the-photographer-stands-not-what-the-shot-looks-like),
and the model can check it. *"A close-up of the therapist"* is an abstraction it would satisfy by
building whatever room it needed.

**Model: Nano Banana Pro. Attach the accepted 7c still. Cast no Character.** Paste into the
**prompt box**:

```prompt
A documentary press photograph of a private therapy session. This is a news picture, not an advertisement. It is a closer angle on the same session as the attached photograph, taken a moment later.

Reference: use the attached photograph for the woman's face, her hair, her glasses and her clothes, and for the room, the light and the colour. All of those stay exactly the same.

Subject: The woman from the attached photograph, in her armchair, seen from the chest up.

Composition: 85mm lens at f/2.0. The camera stands just past the man's shoulder on the couch side of the room, so his out-of-focus shoulder and the back of his head fill the lower left corner of the frame and we look past them at her. No part of his face is visible. She sits centre-right, her head in the upper third, and she is looking frame-left at him. Behind her is the plain warm-grey wall, softly out of focus. The horizon is not quite level.

Action: She is in the middle of explaining something simple, slowly. Her mouth is open on a word and her chin is a fraction down, her head tilted very slightly. Her eyes are steady on him and her eyebrows sit level and relaxed. She is patient in the way that is not quite a compliment. This is not a smirk, not a frown, not sympathy and not drama. The expression stays small.

Location: The same consulting room, seen closer.

Style: Shot on 35mm Kodak Portra 400, fine natural grain, soft warm-neutral colour. The sash window behind the camera to its left is the only light source, flat grey afternoon daylight falling on her face from that side, with the wall behind her a stop darker. Real skin with visible pores, uneven tone and a matte sheen rather than gloss. Her face is naturally asymmetric.

Constraints: Only her face is visible. Nothing in the frame carries readable text. Her glasses stay low on her nose. The expression stays small.

Compose for a 16:9 frame.

Thanks.
```

---

### 7d-y — the therapist explains · **video** · written 2026-09-09, ⚠️ blocked on 7d

**Omni Flash · Frames tab · the accepted 7d still as frame 0 · no Character, no Ingredients, no
end frame · camera locked.** The reasoning is [7c-y's](#7c-y--the-therapist-explains-a-feeling--video--written-2026-09-09-unrun)
and none of it changes: Ingredients would redraw a face that exists in one picture.

**Audio uses `No dialogue and no music.`** — the [7c-y2 reasoning](#7c-y2--the-therapist-explains-a-feeling-mouths-moving--video--written-2026-09-09-unrun):
on a shot whose subject is a woman speaking, *no voices* is as likely to freeze her mouth as to
mute the track, and a synthesised voice costs nothing because the audio is discarded and replaced.

**One event. The [biological-motion clause](../../google-flow/omni-flash.md#-biological-motion--the-anti-slop-clause-for-any-shot-of-a-person-doing-nothing)
stays** — a single held face with no breath and no blink is a waxwork, and there is nothing else
in a close-up to carry life.

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. The camera is locked off on a tripod and holds completely still for the whole shot.

The woman keeps explaining, slowly. She talks in short phrases with a small pause after each one, and between them she watches his face to see whether he is following. Near the end she stops and simply waits, her mouth closed, still looking at him.

She breathes and she blinks. The out-of-focus shoulder in the corner of the frame stays where it is. Everything else in the room stays still.

Audio: room tone only, a radiator ticking as it warms and faint London traffic through old glass. No dialogue and no music.
Thanks.
```

---

### 7e — close on Tarquin · **still** · written 2026-09-09, ⚠️ shoot after 7d

**Cast `@Tarquin-new`. Attach nothing. The room goes back into prose.**

> ### 🔴 `[confirmed 2026-09-09]` — a wide-shot reference does not carry a face at close-up range
>
> **Jack: *"Tarquin's face changed."*** This entry was revised mid-session to attach the 7c still
> instead of casting the Character, on the [supersede-the-prose
> rule](../../google-flow/nano-banana-2.md#7--write-the-keep-list-from-the-accepted-still-not-from-the-prose-that-made-it).
> **That was the wrong trade and it cost the face.** Reverted to the original build.
>
> 🔑 **The mechanism, and it is obvious in hindsight: a reference carries a face only in
> proportion to how many pixels that face occupies in it.** In the 7c wide his head is a small
> part of the frame. Asked for a chest-up portrait, there is nothing in the reference to enlarge,
> so the engine invents the detail — and inventing detail on a face *is* changing the face.
>
> **This sharpens the existing rule rather than replacing it.** [7b's
> ruling](#7b--the-therapists-verdict--still--accepted) says *cast a Character when the face is
> the shot; use references when it isn't.* **Add the missing half: a reference only counts as
> carrying a face if the face is roughly the size in the reference that it will be in the
> output.** Going *closer* than the reference is the failure case; staying the same size or going
> wider is fine.
>
> **The room is the cheaper thing to lose.** 7c was itself built Character-cast with the room in
> prose and matched first time — a plain warm-grey wall, a sash window and a radiator are
> forgiving. **A face is not.**
>
> ⚠️ **This has a consequence for [7d](#7d--close-on-the-therapist--still--written-2026-09-09-unrun)
> and it is worse, because she has no Character.** Her close-up is built from the same wide, so
> the same failure is likely. **Two fixes, cheapest first:**
> 1. **Crop the 7c still to her head and shoulders in Flow's crop tool, and attach the crop
>    instead of the whole frame.** Same pixels, but now the face fills the reference. Zero
>    generations. **Try this first.**
> 2. **Make her a Flow Character** from the 7c still. Permanent, and she needs one anyway if she
>    ever appears again.

**⚠️ Say nothing about his face or clothes.** A Character is attached and there is
[no direction to push him in](./characters/tarquin.md#-when-to-describe-his-face-and-when-not-to-2026-08-26)
— 4b described the face with nothing to override and came back older than he should be. The
leisure wardrobe lives in the Character's Body, which is
[the whole reason `@Tarquin-new` exists](./characters/tarquin.md#-tarquin-new--the-leisure-character-2026-08-26).

**⚠️ The Location slot names only what is in THIS frame.** No rug, no armchair, no journals, no
plant, no tissues — none of them are behind him, and
[anything named in a keep-list is an instruction to draw it](../../google-flow/nano-banana-2.md#6--if-the-camera-cannot-physically-stand-there-the-model-rebuilds-the-set),
wherever the camera happens to be pointing. Keep-lists are per-shot, not per-set.

**⚠️ He sits up.** [Canon as of 2026-09-09](./characters/tarquin.md#-he-sits-up-he-does-not-lie-down),
from the accepted 7c frame.

> ### ⚠️ Check the window against the room before writing it — this entry got it wrong first
>
> The draft put the sash window *"behind him at the right edge of the frame."* **In 7c the window
> is at the far-left end of the room, beyond his head.** From a camera standing past her shoulder
> on the armchair side, that window lands **behind him at the far LEFT of frame** — the right edge
> is where the camera came from.
>
> 🔑 **This is the cheapest possible version of the most expensive failure in the file.** A light
> source asked for in a place the set does not have it is
> [an instruction to rebuild the set](../../google-flow/nano-banana-2.md#6--if-the-camera-cannot-physically-stand-there-the-model-rebuilds-the-set),
> and it will be obeyed at the reference's expense. **Before writing any reverse angle, walk the
> room: where is the window, and which edge does it land on from the new position?**

**Written after 7d deliberately** — it is [the button](../../cinematography/motion-and-cutting.md#2-designing-a-sequence),
and a button is easier to aim once the shot it answers exists. Adjust the eyeline height off what
7d actually comes back as.

**Model: Nano Banana Pro. Cast `@Tarquin-new`. Attach no reference image.** Paste into the
**prompt box**:

```prompt
A documentary press photograph of a private therapy session. This is a news picture, not an advertisement. It is a close angle on one man in a consulting room, shot from the other end of the room past his therapist's shoulder.

Subject: The cast character, sitting up on a low upholstered couch, seen from the chest up.

Composition: 85mm lens at f/2.0. The camera stands just past the therapist's shoulder on the armchair side of the room, so her out-of-focus dark green shoulder and the back of her head fill the lower right corner of the frame and we look past them at him. No part of her face is visible. He sits centre-left, his head in the upper third, and he is looking frame-right at her, past her shoulder. A tall sash window stands behind his far shoulder at the left edge of the frame, blown out and soft. The horizon is not quite level.

Action: He is listening and not getting there. His mouth is closed and his lips are pressed very slightly together. The inner end of one eyebrow is lifted a fraction higher than the other, putting a single short crease between them. His eyes are on her, steady and slightly unfocused, as though he is listening to something inside his own head. His chin is a little tucked. That is the whole expression and the rest of his face is relaxed. This is not shock, not fear, not a pantomime frown and not comedy. A stranger looking at this photograph would take a second to notice anything was wrong with him at all.

Location: A tasteful, quiet, expensive consulting room in London. Behind him, a plain wall in a soft warm-grey and the tall sash window at the left edge of the frame, with a radiator beneath it chipped at one corner. The pale upholstered back of the couch runs along the bottom of the frame. Comfortable rather than grand — money that does not announce itself.

Style: Shot on 35mm Kodak Portra 400, fine natural grain, soft warm-neutral colour. The sash window at the left edge is the only light source, so the light comes from behind his far shoulder and his face is lit softly by daylight bouncing back off the pale wall opposite the window. Real skin with visible pores, uneven tone and a matte sheen rather than gloss. His face is naturally asymmetric.

Constraints: Only his face is visible. Nothing in the frame carries readable text. His mouth stays closed. The expression stays small.

Compose for a 16:9 frame.

Thanks.
```

---

> ### 🔴 *"That did not zoom into Tarquin"* — it was never going to, and that is deliberate
>
> **Jack, 2026-09-09**, having fired `7e-y`'s block on the 7c wide. The prompt says *"the camera
> is locked off on a tripod and holds completely still for the whole shot"* — **the clip did
> exactly what it was told.**
>
> 🔑 **We never ask Flow for a camera move.** [`hybrid-method.md`](../../video-fx/hybrid-method.md),
> ruled 2026-08-26: Omni's expensive failure is **regeneration, and camera translation is what
> fires it.** [8b-fog made this exact call](#8b-fog--the-clip--video--ran-and-accepted-2026-09-08)
> — *yes to the push-in, no to asking Flow for it* — and the frame survived. **Her face exists in
> one picture. A camera move is the single instruction most likely to redraw it.**
>
> **So there are three ways to get the close-up, and they are not equal:**
>
> | Route | Cost | Verdict |
> | --- | --- | --- |
> | 🥇 **Shoot `7e`** — a real close-up still, then clip it locked | one generation, already written | **Recommended.** 85mm compression, an over-the-shoulder foreground, the backlit window. A designed shot rather than an enlargement |
> | 🥈 **Push in Premiere** over the clip already made | free, exact, re-triable | ⚠️ **Resolution is the catch.** He is ~30% of frame width, so a chest-up crop is roughly 3×. From 720p that is mush; from Omni 1.1's **4K upscaled output** it is about a 1.7× blow-up and probably holds under grain. **Check what was exported before relying on it** |
> | 🥉 **Crop the 7c still in Flow's crop tool**, use the crop as frame 0 | zero generations | Continuity guaranteed, instant — but it is a 35mm wide blown up: flat, no foreground, no lens compression. A fallback, not a shot |
> | ❌ **Ask Omni to push in** | one generation | Against the standing ruling, and it risks the two faces |
>
> **The push-in was always a Premiere move.** What was missing was not a clause in the prompt — it
> was a close-up to cut to.

### 7e-y — Tarquin stops listening · **video** · written 2026-09-09, ⚠️ blocked on 7e

**Omni Flash · Frames tab · the accepted 7e still as frame 0 · no Character, no Ingredients, no
end frame · camera locked.**

#### 🔴 Jack revised the beat, 2026-09-09: *confused, and not listening*

**This is a better button than the one it replaces, and it changes what the clip does.** The
earlier version had him open his mouth to ask a question and fail — *"he does not own the
question."* Jack's note is sharper: he is not even in the room. **A man paying by the hour for an
answer, who checks out while it is being given to him**, is the whole character.

⚠️ **The two beats fight each other and only one can be in the clip.** *About to ask* is
engagement; *not listening* is absence. **`Not listening` wins** — it is Jack's call and it is the
funnier read.

🔑 **And it is better shot as a change than as a state.** A still of a man not listening is just a
blank face; **the clip catches the moment he goes.** Frame 0 already has him looking at her, so
the drift is free — it is the difference between the first and last frame, which is exactly what
[a clip is for and a still cannot do](../../cinematography/stills.md#1-what-makes-a-still-hold).

**The button, and it is the joke:** his eyes slide off her and settle on nothing — and then, near
the end, **they come back to her a beat too late.** That half-second of latency is a man realising
he stopped listening and pretending he did not. Nobody has to say it.

#### ✅ This is the safest clip in the sequence

**The entire performance is eyes and breath.** No mouth, no hands — the
[two documented weak areas](../../google-flow/omni-flash.md#design-the-shot-around-the-difficulty-ranking-not-against-it)
and the [top two 2026 video tells](#-the-two-tells-a-moving-mouth-turns-on-and-what-actually-counters-them)
are both absent by construction. It is also why the audio clause reverts to the
[proven 8b-fog phrasing](#8b-fog--the-clip--video--ran-and-accepted-2026-09-08),
`No music and no voices.` — use the strongest suppression available wherever nothing is talking.

⚠️ **Which makes blinking load-bearing rather than decorative here.** On every other shot the
[biological-motion clause](../../google-flow/omni-flash.md#-biological-motion--the-anti-slop-clause-for-any-shot-of-a-person-doing-nothing)
is insurance against waxwork; on this one the blink **is** the performance. Two events, the Omni
ceiling, and both of them are his eyes.

#### ✅ 7e shot and accepted 2026-09-09, and the frame changed one thing in this block

**Held:** the axis (her shoulder lower-right, him centre-left looking frame-right), the window and
its chipped radiator at the left edge, the couch back along the bottom, the warm-grey wall, the
85mm compression, the gilet and roll-neck out of the Character's Body, and **his face** — which is
the whole reason the reference was dropped.

🔑 **The frame handed the drift a destination the draft did not have.** The written block sent his
eyes *"to nothing in the middle distance, past her shoulder"* — but in the accepted frame her
shoulder **fills that side of the picture**, so there is no middle distance over there to drift
into. **The blown-out sash window is at the opposite edge, and it is the brightest thing in
shot.**

**So he looks at the window.** It is motivated, it is the universal tell for a man who has
checked out, it is a bigger and far more legible eye movement than an unfocus at this size — and
the viewer's eye follows it for free, because [the eye goes to motion, then to high-contrast
regions](../../cinematography/frame.md#2-the-focal-point). **Write the drift toward something
that is in the frame.** Same finding as
[placing people by landmark](../../google-flow/nano-banana-2.md#3c--name-where-the-photographer-stands-not-what-the-shot-looks-like),
arriving from the performance side.

⚠️ **Eyes only, not a head turn.** A head turn is a different, larger beat — *bored* rather than
*absent* — and it puts his profile through a rotation, which is where morphing lives.

#### ⬜ One addition: her shoulder is allowed to move a little

The draft froze the foreground shoulder. **On a soft mass that large, eight seconds of absolute
stillness reads as a cardboard cutout** — and she is supposed to be talking through the whole
shot. **No face and no hands are visible in that corner**, so the usual reason to freeze a
foreground does not apply here.

It is written as ambient rather than as a beat, the same class as the rain in
[8b-fog](#8b-fog--the-clip--video--ran-and-accepted-2026-09-08), so the
[event count stays at two](../../google-flow/omni-flash.md#-the-speech-trap-is-punctuation-not-vocabulary):
his eyes leave, his eyes come back.

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. The camera is locked off on a tripod and holds completely still for the whole shot.

The man is looking at her. Partway through the shot his eyes drift away from her towards the bright window at the left of the frame, and stay there. He is no longer taking any of it in. His head does not turn and his mouth stays closed.

Near the end of the shot he blinks and his eyes come back to her, a beat later than they should have.

He breathes and he blinks. The out-of-focus shoulder and the back of the head in the right of the frame shift very slightly, the way someone does while they are talking. Everything else in the room stays still.

Audio: a radiator ticking as it warms, one creak from the couch, and faint London traffic through old glass. No music and no voices.
Thanks.
```

**⬜ If firing it on the 7c wide two-shot instead of a 7e close-up**, the block needs one addition:
she is in frame and an undirected person freezes or gets invented motion. Add before the audio
line — *"The woman goes on talking quietly, and they blink at different times."* Everything else
stands. **The close-up is the better clip** — at two-shot distance an eyeline drift is a few pixels
and the joke does not read.

#### ⬜ Knock-on for the 7e still — settled, it was shot looking at her

The [7e prompt](#7e--close-on-tarquin--still--written-2026-09-09--shoot-after-7d) still says *"his
eyes are on her."* **Leave it exactly as it is.** The clip needs him looking at her in frame 0 —
that is what makes the drift visible. **Do not build the not-listening into the still**; a still
of a man staring into space has no journey in it, and the pair would then have nowhere to go.

**Post, for the pair, in Premiere:**

1. 🔑 **Cut from her to him on one of her pauses**, not on a frame count — the pauses are written
   into 7d-y for exactly this. Let the room tone run across the cut so the two shots read as one
   moment.
2. **A 10–15% speed adjustment** on each clip against the smooth-motion tell `[community]`.
3. **Film grain at 10–15% opacity.**
4. ⚠️ **Nothing ships unmeasured** — `scripts/delivery-qc.sh`
   ([`delivery.md`](../../video-fx/delivery.md)).

---




---


### 3c — the lane, hours later · **still** · written 2026-09-09, unrun

**Jack, 2026-09-09: *"the dashboard does not convey that there has been a crash enough."*** He is
right, and the fix he proposed — **blue lights, broken glass, the car on its side, camera at
ground level** — is the one this file already half-anticipated: 3b's alternates list names
*"broken glass on wet tarmac"* and *"the amber corner lamp in the grass — the wider version of
this same idea."*

#### ✅ This does not break the crash ruling, and it is worth being sure why

[`story.md`](./story.md) ruled 2026-08-25 that **the crash is never shown** — *"Haneke shoots the
aftermath, not the act,"* and a generated car crash is among the few things the engines reliably
cannot do. **3c is aftermath.** The impact still happens in the black. Nothing here depicts the
event.

🔴 **The rule it *could* break is the other one: *we never show or say who died*.** Blue lights
invite the audience to look for a casualty, and one wrong noun answers the question the whole film
withholds. **The design answer is absence, and it is specified, not hoped for:**

- **Nobody is near the car.** No covered shape, no stretcher, nothing being carried, nobody being
  treated. **A single person receiving attention would say the other one did not survive** — the
  same arithmetic that ruled two empty seats out of [3b](./shot-list.md).
- **The two figures in shot are distant, soft and doing nothing.** They exist because
  [a sterile environment is a named slop tell](../../google-flow/nano-banana-2.md#the-anti-slop-toolkit),
  not because they carry information.
- **The car's cabin is not legible from this angle** — it lies with its roof toward the camera.

**What the frame says is *this was serious*. What it does not say is *who*.** That is exactly the
canon position: [let the audience join the dots when they meet Bob again](./story.md#scene-3--the-crash).

#### 🔴 The blue light source stays out of frame

**Only the light is in the picture, never the vehicle it comes from.** Three reasons and each
would do on its own:

- **It is stronger.** [Withhold — a partial view, an obstruction](../../cinematography/symptoms.md#a-the-single-frame);
  a frame that shows everything has nothing to discover. Blue on a wet lane is read as *emergency*
  instantly, and the source adds nothing the viewer needed.
- 🔴 **It dodges [trigger 1](../../flow/failure-modes.md#a5-the-five-triggers-badcodes-own)
  entirely.** A police vehicle carries a real institution's wordmark and a reflective livery, and
  *"asking for a legible real logo or wordmark is the most reliable block there is."*
- **It is one fewer object to invent.** [The biggest lever on this engine is subtraction](../../google-flow/nano-banana-2.md#-descriptive-not-repetitive--and-what-it-costs-us).

#### 🎯 Where it goes in the cut — and the recommendation is *after* 3b

**Recommended order: 3b, then 3c.** 3b is seconds after, in the flat grey daylight the crash
happened in; 3c is hours later at dusk with the light gone. **The elapsed time is free
storytelling and it lives entirely in the gutter between the two frames** —
[what you cut out between two stills does more work than what is in either one](../../cinematography/stills.md#3-the-gutter--what-happens-between-two-stills).

🔑 **And it makes 3b's withholding deliberate rather than a failure.** The audience spends the
dashboard shot unsure; 3c confirms it. That is a **reveal — a withheld shot** — where putting 3c
first would make 3b a redundant footnote to information already given.

⚠️ **The one cost, stated:** it runs close→wide, which inverts the default *wide→close* direction.
That is fine because the change here is **time**, not proximity, and the light does the signalling.
⬜ **Jack's call** — put 3c first if the priority is that the crash lands immediately.

#### ⚠️ Two continuity facts, both checkable

- **The location is a country lane, not a pavement.** [2a](#2a--the-car-on-the-lane--still--accepted)
  and the accepted 3b frame both have a hedgerow, a grass verge and no kerb, no street lighting
  and no footway. Written that way here. *(If an urban roadside is actually wanted, that is a
  location change to Scene 2 as well and it needs a ruling, not a prompt.)*
- **The night stock is Fujicolor Superia 1600, not Ektachrome or Portra.** Scene 2 daylight is
  Ektachrome; [the established camping night stock is Superia 1600 at ISO 1600](#5a--the-drive-home)
  and this is a dusk frame. ✅ It also happens to sidestep the 2026 finding that
  [Portra 400 is now over-prompted](../../google-flow/nano-banana-2.md#-kodak-portra-400-may-now-be-a-slop-tell-community-untested).

#### ⚠️ The anti-slop pass, and this time the web actively argued for slop

A fresh search for night-scene prompt craft returned, near-verbatim, **the recipe our own files
name as the disease**: *"mention mixed light sources — neon signage colour spill, tungsten
streetlamps, and headlights"*, plus *"dramatic lighting, cinematic colour grading, 4K detail,
professional photography."* `[community]`

**Every one of those is a named tell.**
[Stacked lighting is *the* named tell](../../google-flow/omni-flash.md#5-anti-slop-restated-from-the-photorealism-pass) —
*"a glowing face, a dark background, a bright window, a rim light, neon reflections and a golden
sunset all somehow happening at once"* — and *"4K, cinematic, professional"* is exactly the
keyword spam that
[Google's own guidance says is dead](../../google-flow/nano-banana-2.md#-descriptive-not-repetitive--and-what-it-costs-us).
**Recorded so nobody re-runs the search and adopts it.** This block does the opposite: **one key
light, named, with its falloff stated.**

**The rest of the pass is our own table, applied:**

| Tell | What this block does instead |
| --- | --- |
| **Wet tarmac holding long mirror reflections** — [the advert tell that cost us 5a](#-advert-vocabulary-commissions-an-advert-observed-2026-08-26) | Wet road **broken up**: grit, a patched repair, a worn white line, mud dragged out of the verge |
| A glossy hero vehicle | **A working car** — a few years old, unremarkable, road film up the panels. [2a's brief](#2a--the-car-on-the-lane--still--accepted) already argues at length for boring |
| Sterile, empty environment | Two figures far down the lane, soft, doing nothing |
| Flat, single-plane frame | **Ground-level camera puts broken glass enormous in the foreground** — Jack's own idea, and it is the [depth layer that stops a frame reading flat](../../cinematography/frame.md#1-depth-is-the-first-thing-to-fix), for free |
| Near-black reading as a broken file | **Two anchors**: the last grey of the sky above the hedge, and the blue on the wet road *(principle 11)* |
| `photorealistic` | The house preamble — **documentary press photograph** |

**Policy pass, [A5b's discipline](../../flow/failure-modes.md#a5b-the-bedroom-problem--trigger-5-in-detail)
— *context does not protect a word, it convicts it*.** On a crash scene the words to keep out are
**body, victim, casualty, dead, injured, blood, wreck**. None appears below. The frame is described
by what is in it: a car on its side, broken glass, a closed lane.

#### 🔴 Rewritten 2026-09-09 round 2 — Jack: *"I barely want to see the car, it should be to the side"*

**Two changes, and the second is a prompt-architecture change rather than a wording one.**

**1. The 2a still is now attached as the reference.** Jack handed it over. ✅ **And the
[reference-scale rule](../../google-flow/nano-banana-2.md#-confirmed-2026-09-09-a-reference-carries-a-face-only-at-the-size-the-face-is-in-it)
works in our favour for the first time this session:** in 2a the car is *"already some distance
off and small in the frame"*, and in 3c it is smaller still and half out of frame. **Going wider
than the reference is the safe direction** — there is nothing to enlarge, so nothing gets
invented. The car, the roof box, the hedgerows and the road surface all come across for free.

**2. 🔑 The Subject slot is now the ROAD, not the car.** This is the whole fix and it is
structural, not descriptive.

> **The engine hero-frames whatever is named first.** Write `Subject: an ordinary estate car…`
> and you get a car, centred and filling the frame, no matter how carefully the composition slot
> then argues for *small and off to one side* —
> [earlier clauses win when instructions compete](../../../.claude/skills/flow-prompt/SKILL.md).
> **So the road goes in the Subject slot and the car is demoted into the composition as a thing
> at the edge.** Recorded as a general rule in
> [`nano-banana-2.md`](../../google-flow/nano-banana-2.md#-making-a-subject-small-put-something-else-in-the-subject-slot-community-2026-09-09).

**Two supporting levers from the same web pass** `[community]`:

- **Placement stated as an explicit named third**, not as *"off to one side"* — the vague version
  loses to the centring prior.
- 🔴 **The empty part is described in detail, because the model fills empty space.** An
  unspecified expanse of road is an invitation to invent something to put in it — the same
  mechanism as [the set giving way to whatever the shot
  requires](../../google-flow/nano-banana-2.md#6--if-the-camera-cannot-physically-stand-there-the-model-rebuilds-the-set),
  arriving from the composition side. So the emptiness gets grit, a patched repair, a puddle and
  the worn centre line: **occupied by specified texture rather than by invented content.**

#### ✅ The road is two-lane — settled by this shot

[The continuity conflict flagged on 2a](#2a--the-car-on-the-lane--still--accepted) — *A-road*
in the still, *single-track lane* in the video prompt and the shot list — **is resolved by the
picture.** Two lanes, a faded centre line, hedgerow both sides, telegraph poles. The draft below
said *narrow country lane* and was wrong.

#### 🎯 The roof box is the emotional payload, and it is free continuity

The black roof box is **on the car in the reference image**, and canon's own scene-3 alternates
already reach for exactly this register — *"the road atlas face-down in the verge with the biro
route ending mid-page."* **A roof box lying in the grass says *they were going on holiday* with no
caption and no narration**, which is [what a still is for](../../cinematography/stills.md#2-word-and-picture):
a caption carries only what the eye cannot get, and this the eye can.

⚠️ **It is the same idea as the ruled atlas, so use one or the other, never both.**
⬜ Jack's call which.

#### ⬜ If the frame comes back busy, subtract in this order

Four story objects is the ceiling and it may be one over: glass (near) → roof box (mid) →
car sliver (far right edge) → one distant figure. **Drop the figure first** — it is only there
because [a sterile environment is a named slop tell](../../google-flow/nano-banana-2.md#the-anti-slop-toolkit)
and it is the one element carrying no story. Then the roof box.
[Subtract before adding](../../google-flow/nano-banana-2.md#-descriptive-not-repetitive--and-what-it-costs-us).

**Model: Nano Banana Pro. Attach the accepted 2a still — job stated: the car, the roof box and
the road. Cast no Character.** Paste into the **prompt box**:

```prompt
A documentary press photograph taken at the scene of a road accident, hours afterwards. This is a news picture, not an advertisement. It is the same stretch of road as the attached photograph, at dusk, with the camera down on the tarmac.

Reference: use the attached photograph for the road itself, the hedgerows, the fields and telegraph poles beyond, and for the silver estate car and its black roof box. Those all stay the same. What changes: it is now dusk, the road is wet and closed, and the car has left the road.

Subject: The empty wet road surface, seen from a few centimetres above it. Broken glass is scattered across the tarmac in the near foreground, enormous and thrown well out of focus, each fragment holding a small point of blue. Beyond it the road runs away past a faded white centre line, worn and patched, with grit washed into the gutter and a shallow puddle holding the sky.

Composition: 35mm lens at f/2.8, the camera resting on the road itself and looking level along it. The empty road fills the lower two-thirds of the frame and a band of flat grey dusk sky fills the top, with the hedgerows closing in from both sides as dark masses and two telegraph poles in silhouette against the sky. At the far right edge of the frame, mostly out of shot and occupying no more than a tenth of the width, a pale flank of the estate car lies tilted over in the hedge. The black roof box lies on its own in the grass verge partway between the camera and the car. A single figure in a high-visibility jacket stands a long way off down the road, very small, not looking at anything. The horizon is not quite level.

Action: It is over and it has been over for some time. Nothing is happening and nobody is anywhere near the car. The only thing still moving is the light.

Location: The same two-lane road in flat English farmland as the reference photograph, at dusk. A grass verge on the right churned into mud where something has gone through it, and a deep gouge running off the road into the grass.

Style: Shot on 35mm Fujicolor Superia 1600, ISO 1600, heavy natural grain through the shadows. Pulsing blue light from a vehicle outside the frame, low and off to the right, is the only artificial light source — it rakes across the wet tarmac from behind, lights the glass from the far side, and dies before it reaches the foreground, leaving the near road almost black. The last of the grey daylight sits in the sky above the hedge. Cold, wet and unforgiving.

Constraints: The car stays at the right edge of the frame and mostly out of shot. Nobody is near the car. Nothing in the frame carries readable text and no badges or number plates are legible. No emergency vehicle is visible.

Compose for a 16:9 frame.

Thanks.
```


<details><summary>⬜ Round 1 (superseded) — prose-only, car centred</summary>

**Model: Nano Banana Pro. Attach no reference image. Cast no Character.** *(Prose only, deliberately:
the transform from [2a](#2a--the-car-on-the-lane--still--accepted) is large — day to dusk, upright
to on its side — and a reference fights a change that big. The car is written as unremarkable
precisely so its identity is not load-bearing. If Jack wants the exact car held, attach 2a with its
job stated as the colour and body shape only, and expect the transform to argue with it.)*

Paste into the **prompt box**:

```prompt
A documentary press photograph taken at the scene of a road accident, hours afterwards. This is a news picture, not an advertisement.

Subject: An ordinary mid-size estate car, a few years old and entirely unremarkable, lying on its side across a narrow country lane with its roof towards the camera. Road film up the panels and mud along the sills. One wheel is off the ground. Nothing about the car is expensive, sporty or distinctive.

Composition: 35mm lens at f/2.8. The camera is on the tarmac itself, the lens a few centimetres above the road surface, looking level down the lane. In the near foreground, enormous and thrown well out of focus, broken glass is scattered across the wet road, each fragment holding a small point of blue. The car sits in the middle distance, off-centre to the left. Beyond it the lane runs away into the dark, and two figures in high-visibility jackets stand a long way off, small and soft, doing nothing in particular. The horizon is not quite level.

Action: It is over and it has been over for some time. Nothing is happening. Nobody is anywhere near the car. The only thing still moving is the light.

Location: A narrow rural lane in England at dusk, with a bare winter hedgerow along one side and a grass verge churned into mud where something has left the road. No kerb, no footway and no street lighting. The wet tarmac is broken up by grit, a patched repair and a worn white line. A deep gouge runs through the grass of the verge.

Style: Shot on 35mm Fujicolor Superia 1600, ISO 1600, heavy natural grain through the shadows. Pulsing blue light from a vehicle outside the frame, low and off to the right, is the only artificial light source — it rakes across the wet road, picks out the glass and the underside of the car, and dies before it reaches the hedge, leaving the far end of the lane in near-black. Above the hedgerow there is a last band of flat grey daylight left in the sky. Cold, wet and unforgiving.

Constraints: Nobody is near the car. Only the two distant figures are in the frame. Nothing in the frame carries readable text and no badges or number plates are legible. No emergency vehicle is visible.

Compose for a 16:9 frame.

Thanks.
```

**⬜ If it comes back under-reading as a crash**, the cheapest single addition is **the deep gouge
through the verge made larger and closer** — a track that says *the car left the road here* is
causal information the blue light cannot give. Add before adding anything else, and
[subtract a clause before adding two](../../google-flow/nano-banana-2.md#-descriptive-not-repetitive--and-what-it-costs-us).

</details>

#### ✅ 3c shot and accepted 2026-09-09 — the subject-slot fix worked

**Everything the round-2 rewrite asked for came back:** the camera on the tarmac, the glass
enormous and blue-lit in the foreground, the faded centre line and the patched road, the hedgerows
closing in, the telegraph poles against the sky band, the roof box alone in the verge, the distant
high-vis figure — and **the car at the far right edge, mostly out of shot.**

🔑 **Putting the road in the `Subject:` slot is what did it.** Two rounds of composition adjectives
would not have; the slot order did. **Promoted to a general rule** in
[`nano-banana-2.md`](../../google-flow/nano-banana-2.md#-making-a-subject-small-put-something-else-in-the-subject-slot-community-2026-09-09).

**One improvement on the brief, kept:** the car is **tilted nose-down into the hedge, not on its
side.** More plausible for a car that left a road at speed, and it reads as *went through the
hedge* rather than *was rolled*, which is the quieter and better version.

---

### 3c-y — the lane, hours later · **video** · written 2026-09-09, unrun

**Jack: *"blue flashing lights, not much else happening, just everything moving naturally."***

**Omni Flash · Frames tab · the accepted 3c still as frame 0 · no Character, no Ingredients, no
end frame · camera locked.** Easy call: there is no face here, staging is everything, and
Ingredients would redraw the whole road.

#### ✅ Why a clip where nothing happens is the right clip for this scene

[Canon](./story.md#scene-3--the-crash) gives Scene 3 **no narration at all** and lets sound design
carry it. This is the frame that silence sits over, and
[the motion budget](../../cinematography/motion-and-cutting.md#1-movement) says the film's one
camera move was already spent on [8b-fog](#8b-fog--the-clip--video--ran-and-accepted-2026-09-08).
**Locked is not the timid choice here, it is the register.**

🔑 **And it still has to be a shot, not a scanned photograph.**
[A frame with an identical first and last frame reads as a photo](../../cinematography/stills.md#1-what-makes-a-still-hold).
**The blue sweep is the thing that changes** — it is the entire argument for this being a clip at
all, and everything else in the frame is there to be *touched* by it.

#### 🔴 The top risk is the broken glass, and it is the same shape as 8b-fog's reflection risk

**The foreground is a field of wet broken glass with specular highlights, huge and close to the
lens** — and [morphing artefacts concentrate on reflective surfaces and fine edges](https://arxiv.org/pdf/2512.15693) `[academic]`,
with *"texture shimmer"* named alongside flicker as the way temporal consistency fails
`[community]`. Our own file already records that
[**glass has failed every time**](../../google-flow/omni-flash.md#-moving-objects-inside-a-reflection--one-observed-failure-and-the-mechanism-is-here).

**Two clauses answer it, and the second is a deliberate softening of Jack's brief:**

- **The glass stays exactly where it is.** Stated positively. The *light* on it changes; the
  *geometry* does not. That is the safe half of the trade and it is worth being explicit about,
  because an engine given a changing light over unpinned geometry will re-solve both.
- ⚠️ **A slow sweep, not a strobe.** A hard flash is a *sudden lighting change* — named among the
  artefacts that break temporal consistency — and over eight seconds it is many discrete light
  states, each one re-rendering every highlight in that glass. **A rotating beacon sweeping is
  also what a scene light actually does** when it has been left running at a closed road, so this
  costs nothing in truth. ⬜ **If the sweep reads too gentle, the fallback is *"the blue light
  pulses twice a second"*** — but run the sweep first, because the glass is the one thing in this
  frame that cannot be fixed in post.

#### ⚠️ The web pass returned advice that is wrong for this engine — recorded so nobody adopts it

2026 temporal-stability guides recommend **negative prompting** to suppress artefacts —
*"including terms like flickering, morphing, sudden lighting changes"* `[community]`.

🔴 **That is actively harmful on Omni Flash.** It has
[no negative-prompt parameter, and `no`/`don't` in the body performs *worse* than not mentioning
the thing at all](../../google-flow/omni-flash.md#-negatives-do-not-work-and-they-actively-backfire)
— naming *flickering* and *morphing* puts both into a model that cannot subtract them. **The
generic advice is written for engines with a negative-prompt field. Ours has not got one.**

**What the same pass got right is already house practice** and is worth noting only because it
independently confirms it: *"lock lighting to a single source, avoid mixed lighting descriptions,
use slower movements, shorten clip duration."* This frame has **one** light source and the camera
does not move.

#### ⬜ No shutter clause, again

The [24fps / 180° line](../../google-flow/omni-flash.md#the-shutter-is-the-tell-nobody-prompts-for)
is `[confirmed]` **on shots with fast motion**, because it tells the model which frames to smear.
Nothing here moves fast enough to smear, and
[the biggest lever is subtraction](../../google-flow/omni-flash.md#length-three-to-four-sentences-and-the-lever-is-subtraction).
Same call as [7c-y](#7c-y--the-therapist-explains-a-feeling--video--written-2026-09-09-unrun).

#### ⚠️ Audio: no radio chatter

The temptation at a scene like this is police radio. **Radio chatter is voices**, and
[we never put speech in a Flow video](../../google-flow/omni-flash.md#-the-speech-trap-is-punctuation-not-vocabulary).
**The diesel idle does the same job better** — it says there is a vehicle off to the right without
showing it, which is the audio half of
[keeping the light source out of frame](#-the-blue-light-source-stays-out-of-frame).

> ### 🔴 Round 1 put beacons on the crashed car — *`[observed 2026-09-09]`*
>
> **Jack: *"that made the car in the image look like it has sirens."*** The clause was *"blue
> light **from a vehicle outside the frame**"* — and a vehicle is visible in the plate, so the
> engine resolved the noun against the one it could see and lit that.
>
> 🔑 ***"Outside the frame"* is a claim about where; *"a vehicle"* is a claim about what — and the
> referential half beats the spatial half.** Handed a noun, the model goes looking for it in the
> picture. **Name an off-frame light by its place and its behaviour, never by the object that owns
> it.** Full write-up:
> [`omni-flash.md`](../../google-flow/omni-flash.md#-observed-2026-09-09-naming-an-off-frame-light-source-by-its-object-binds-it-to-a-visible-one).
>
> **Three fixes in the round-2 block, and the second is the load-bearing one:**
>
> 1. **The source is a place** — *"from beyond the right-hand edge of the frame."* Nothing in the
>    picture for it to attach to.
> 2. 🔑 **The car is given the receiving role, positively** — *"the car is dark and still; the blue
>    light passes over it and moves on."* This is the positive form of *the car has no lights*, and
>    [the negation would have named beacons straight into the prompt](../../google-flow/omni-flash.md#-negatives-do-not-work-and-they-actively-backfire).
> 3. **The whole frame is closed** — *"all the blue light comes from outside the frame."* One
>    sentence covering every object nobody thought to name.
>
> ⚠️ **And the audio moved.** Round 1 put the diesel idle *"somewhere off to the right"* — the same
> side as the car. Omni generates picture and sound together, so a sound sited on a visible object
> is a second vote for that object owning it. **It is now behind the camera**, which is also where
> a vehicle blocking a closed road would actually be parked.

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. The camera is locked off on a tripod on the road surface and holds completely still for the whole shot.

Blue light from beyond the right-hand edge of the frame sweeps slowly and steadily across the scene, over and over. All the blue light comes from outside the frame. As it passes, the points of blue in the broken glass brighten and fade, the wet tarmac and the puddle catch it, and the grass on the right-hand verge goes blue and grey again.

The silver car tipped into the hedge is dark and still. The blue light passes over it and moves on.

The bare hedgerows and the tussocky grass stir in a light wind. The surface of the puddle shivers. Far down the road the figure in the high-visibility jacket shifts his weight and stays where he is.

The broken glass stays exactly where it is. The car, the roof box and the road stay exactly where they are.

Audio: wind moving through a bare hedge, water dripping, a diesel engine idling somewhere behind the camera, and one distant crow. No music and no voices.
Thanks.
```

**Post, in Premiere:**

1. **A 10–15% speed adjustment** against the smooth-motion tell `[community]`.
2. **Film grain at 10–15% opacity** — and this clip carries heavy Superia 1600 grain in the still
   already, so match it rather than stacking.
3. ⚠️ **Watch the foreground glass on playback specifically.** If it crawls or shimmers between
   frames, that is the risk above firing, and **it is a re-roll, not a grade** — check what
   deflicker tooling we actually have before assuming
   ([`effects-catalogue.md`](../../premiere/effects-catalogue.md)).
4. ⚠️ **Nothing ships unmeasured** — `scripts/delivery-qc.sh`
   ([`delivery.md`](../../video-fx/delivery.md)).

---


---


## Scene 2 — 2008, meet Bob

### 2a — the car on the lane · **still** · accepted

**Recovered 2026-08-26.** The still the 2a video continues from.

The whole prompt is an argument for **boring**: *"unremarkable and a few years old"*, *"nothing
about the car is expensive, sporty or distinctive"*, *"ordinary to the point of boring"*, *"no
golden light, no drama"*. Bob's ordinariness is the point of the scene, and it is carried by
the car and the road before he is ever seen. The engine's default is to make things handsome,
so plainness has to be asked for repeatedly and in those words.

Two other things it does deliberately: **nothing legible anywhere** — no badges, no number
plates, and a road sign explicitly carrying no readable text, which is the same lettering
discipline as 1a and 1b; and the car is **already small and already leaving**, so the shot is
a departure from the first frame rather than becoming one.

```prompt
SCENE:

Hyper-realistic documentary photograph, shot on 35mm Kodak Ektachrome — fine natural grain, muted cool-neutral colour, naturalistic daylight only, no lens flares, calm observational tone. The photographer is standing on the verge of a road and the car is simply passing.

Subject: An ordinary silver five-door family estate car from the mid-2000s, unremarkable and a few years old, with a black plastic roof box strapped to the roof bars and the back seats piled with bags visible through the rear side window. No badges, brand names or number plates are legible anywhere on it. Nothing about the car is expensive, sporty or distinctive.

Action: The car is driving away from the camera along the road at ordinary speed, already some distance off and small in the frame, its wheels and the hedgerow closest to the lens softened by a little motion blur. There is no other traffic.

Environment: A plain two-lane British A-road on a flat, dull stretch of countryside — worn tarmac with a faded white centre line, a scruffy hedgerow running along both verges, a ploughed field and a line of bare trees beyond, a wooden telegraph pole. A road sign stands at the verge with nothing legible on it. Everything is ordinary to the point of boring.

Camera and framing: 50mm lens at f/4, held low at about waist height from the grass verge, the road running away slightly right of centre so the frame is not symmetrical. The car sits small in the middle distance with a lot of empty road and a lot of flat grey sky above it. The frame is very slightly tilted.

Light: Flat overcast daylight, no sun and no shadows, the sky a featureless pale grey and slightly overexposed. Muted, cold and unflattering — no golden light, no drama.

Details: Fine natural film grain, slightly desaturated colour, a soft and very slightly missed focus on the far hedgerow.

Compose for a 16:9 frame.

Thanks.
```

> ⚠️ **Continuity note.** 2a's still specifies a **two-lane British A-road** with a faded white
> centre line; the 2a *video* prompt below calls the same location a **single-track lane**, and
> so does [`shot-list.md`](./shot-list.md) and the scene-3 alternates ("the edge of a wet
> single-track English country lane"). The road that actually made it into the frame is the
> A-road. ~~Worth settling before the scene-3 verge shots have to match it.~~
>
> ### ✅ Settled 2026-09-09 — it is a two-lane road, and the picture wins
>
> **Forced by [3c](#3c--the-lane-hours-later--still--written-2026-09-09-unrun)**, which is the
> scene-3 verge shot this note was waiting for, and by Jack handing the 2a frame over as its
> reference. **The accepted frame is the authority:** two lanes, a faded white centre line,
> scruffy hedgerow along both verges, ploughed field and bare trees beyond, wooden telegraph
> poles, a blank road sign on the left, puddles and churned mud on the right-hand verge.
>
> 🔑 **Same rule as [7a's shoulder colour](#7a--the-consulting-room--still--accepted): the
> picture beat the prompt**, and [canon prose describing a set is superseded the moment a still
> of that set is accepted](../../google-flow/nano-banana-2.md#7--write-the-keep-list-from-the-accepted-still-not-from-the-prose-that-made-it).
> **Every scene-3 frame says two-lane road from now on.** *"Narrow single-track lane" is retired
> wording — do not carry it forward.*

### 2a — the car on the lane · **video** · accepted

Frames tab, the accepted 2a still as frame 0, 8s.

```prompt
The attached image is frame one of a locked-off documentary shot on 35mm film. The clip continues from this exact frame.

The silver estate car drives steadily away from the camera down the single-track lane, shrinking into the distance as it goes. The camera stays locked off on its tripod for the whole shot — a single continuous shot. The hedgerows and the tussocky grass in the foreground stir a little in the wind, and the flat grey overcast light stays exactly as it is.

Shot at 24fps with a 180-degree shutter, so anything moving fast smears with natural motion blur. Fine 35mm grain throughout.

Audio: the engine and tyre noise receding into the distance, wind moving through the hedge, one distant crow. No dialogue, no music.

Thanks.
```

### 2b — Bob and his wife in the front seats · **still** · accepted

Third round. Round 1 was too broad (seven stacked muscle instructions, both performed);
round 2 overshot to blank. The stable version puts two or three markers on the **eyes**
and keeps the mouth closed, and gives her *him* to look at — with a rearward dash camera,
"watching the road" and "staring down the lens" are the same direction.

```prompt
SCENE:

Hyper-realistic documentary photograph on 35mm Kodak Ektachrome. Fine natural grain, muted cool-neutral colour, flat overcast daylight only, no lens flares, calm observational tone. The camera sits low on the dashboard against the windscreen, looking back into the car at the two people in the front seats.

This is a British right-hand-drive car: the steering wheel is mounted on the right-hand side of the vehicle. Because the camera is facing rearward, the driver and the steering wheel therefore appear on the LEFT of the frame, and the front-seat passenger appears on the RIGHT.

Subject: On the left of the frame, in the driver's seat, the man in the reference image, thirty-two years old, in a plain mid-blue zip-up fleece over a grey t-shirt, both hands on the wheel, seatbelt across his chest. On the right of the frame, in the passenger seat, his wife — a plain-looking white British woman of about thirty with shoulder-length brown hair pushed back and no makeup, in a long-sleeved top, one foot up on the edge of the dashboard, seatbelt across her chest. Both seen from the chest up.

Action: He is watching the road somewhere off to the side of the camera. His lips stay together but the corners of his mouth are just lifted, his lower eyelids are slightly raised and the skin at the outer corners of his eyes is creased. She has turned her head to look across at him, three-quarters towards the left of the frame, her face doing the same thing — lips together, lower eyelids raised, the outer corners of her eyes creased. Neither of them shows any teeth, and neither is looking at the camera or aware of it. Her hand rests on his forearm. Unposed, caught mid-moment.

Environment: Behind the two front seats the rear of the car is packed solid for a holiday — soft holdalls and a rucksack stacked so high they hide the rear headrests completely, a rolled sleeping bag jammed across the top, coats thrown over the pile and a carrier bag wedged into the gap, all of it filling the space between and above their shoulders and blocking most of the rear window. Around them the inside of an ordinary mid-2000s family car — grey cloth seats, a plain dark roof lining, an open road atlas on her lap. Through the side windows behind them, scruffy hedgerows blur past.

Camera and framing: 28mm lens at f/2.8, held low at dashboard height so the angle looks very slightly up at both of them, catching the underside of the jaw and a lot of roof lining above their heads. He sits left of centre and she sits right, with the frame deliberately not balanced between them — a little more room on her side. The near edge of the dashboard and the top of the steering wheel cut into the bottom of the frame, out of focus. Focus sits on his face. Only two people are in the car and no other limbs appear anywhere in the frame.

Light: Only daylight — the flat grey sky bouncing up off the bonnet and dashboard into their faces from below, and the side windows blowing out to near-white behind them. Cool, even and unflattering, with the roof lining above them in shadow. No fill light, no sun, no warmth.

Details: Real skin with visible pores, stubble and uneven tone. Fine natural film grain. Slight motion blur in the hedgerows through the side glass.

Compose for a 16:9 frame.

Thanks.
```

### 2b — the laugh · **video** · accepted

⚠️ **The one shot generated on Veo 3.1, not Omni Flash.** Omni Flash on Frames lost both
faces once the ask stopped being near-static — see the tab-rule bound in
[`omni-flash.md`](../../google-flow/omni-flash.md). Head movement is deliberately trimmed
out of the laugh: every degree the head turns is facial detail the model has to invent,
and invented detail is where the face goes. Appearance is reinforced in text as the
documented anti-drift lever.

Veo 3.1 Fast, the accepted 2b still as the start frame, 8s.

```prompt
Use the attached image as the locked opening frame and continue directly from it. A locked-off documentary shot on 35mm film, filmed from a camera low on the dashboard looking back at the two people in the front seats of an ordinary mid-2000s family car — the man on the left in a mid-blue zip-up fleece over a grey t-shirt, his wife on the right in a mauve long-sleeved top with an open road atlas on her lap, the back of the car packed to the roof with holiday luggage behind them. Both keep exactly the faces, hair, clothing and seating positions they have in the opening frame for the whole shot.

They are holding a laugh in, and then they lose it. His lips stay pressed together and the corners tighten, and then his mouth opens and he laughs out loud with his teeth showing, his eyes squeezing almost shut and creasing deeply at the outer corners, his shoulders shaking, his head staying where it is against the headrest. She breaks a moment after him, her chin dropping towards her chest, her eyes screwing shut and her cheeks pushing up. It is an ugly, unguarded, real laugh. Neither of them looks at the camera.

Locked-off camera, no camera movement, single continuous shot. Everything else in the car stays exactly where it is, and the hedgerows through the side windows keep streaming past in a soft blur. Shot at 24fps with a 180-degree shutter, so the hedgerows smear with natural motion blur. Maintain the grain, colour and flat overcast light of the image.

Audio: the two of them laughing out loud over engine drone and road noise, wind against the glass. No dialogue, no music.

Thanks.
```

### 2f — Bob and Jo filler set, outside the house · **video ×4** · written 2026-09-13, unrun

**Jack, 2026-09-13:** *"We need more video of Bob to match the length of the narration… easy ones of
Bob and his wife having coffee outside their house, about to get into their car, loading luggage and
smoking cigarettes, all separate videos… I just need filler videos."*

**The job is runtime, so the design is *easy*.** Every clip is one small, calm, continuing action; locked
camera; flat overcast daylight in the 2a/2b register; about 8 seconds of *nothing going wrong*.

**Routing, and the one real risk:**

- **Omni Flash → Ingredients to Video**, with the **accepted `2b` still** as the only ingredient.
  **Not Frames**, because there is no start frame of the house.
- 🔴 **Do not attach `@Bob`.** That Character is the 2026 face, eighteen years older and damaged. Jo
  has no Character.
- 🔴 **Ingredients re-renders faces from a reference and does not reliably hold an unnamed likeness**
  ([`omni-flash.md`](../../google-flow/omni-flash.md#️-ingredients-re-renders-faces--it-will-not-hold-an-unnamed-person-observed-2026-08-20)).
  **So the framing keeps faces small**: medium-wide, three-quarter or side-on, never a close-up. That is
  right for filler anyway, since it sits under narration and nobody is studying a face. If a face drifts,
  re-roll.
- **The reference is declared as people-only** ("not a frame from this shot"), or Ingredients will try
  to put them back in the car.
- **No appearance description of either of them** ([house rule](#conventions)); they keep the
  fleece and the mauve top from the reference, because it is the same morning.
- **The car is described, not referenced**, and **not named**, because a marque renders its badge
  ([§34](../../google-flow/nano-banana-2.md#34--naming-a-marque-renders-its-badging-and-no-downstream-constraint-removes-it-observed-2026-09-08)).
  It is matched to the 2a car: a silver mid-2000s estate with a black roof box.
- **No dialogue**: they stay quiet, and every prompt ends `No music and no voices.`
- **Smoke, steam and exhaust are kept thin and named once.**
  [Particle nouns overdeliver](../../google-flow/omni-flash.md#️-particle-nouns-have-no-volume-control-observed-n2).

**Paste into (all four):** Flow → Omni Flash → **Ingredients to Video** prompt box. **Ingredient:** the
accepted `2b` still. **No Character.** **Aspect:** 16:9. **Duration:** 8s. One at a time.

#### 2f-1 — coffee on the front step

```prompt
The attached image is a reference for the two people only — their faces, hair and clothes. It is not a frame from this shot. This shot takes place outside their house, the same morning, before they leave on holiday.

A locked-off documentary shot on 35mm film. The camera stands at the edge of the pavement, about five metres away, level, looking across a small paved front drive at the front door of an ordinary red-brick semi-detached house in a British suburb in 2008. The man and the woman from the reference sit side by side on the front doorstep, seen full length and a little from the side, each holding a mug of coffee in both hands. Beside them on the drive is an ordinary silver mid-2000s estate car with a black plastic roof box on its roof bars, its back seats piled with bags.

The two of them sit quietly and drink their coffee. He takes a slow sip. She leans her shoulder against his and looks over at the packed car. A faint thread of steam rises from each mug. They both breathe and blink naturally, at different moments.

Flat grey overcast morning light, no sun and no shadows. Muted cool-neutral colour, fine film grain, and nothing legible anywhere, including the car's number plate.

Audio: birdsong in the front gardens, a distant road somewhere behind the camera, and the small clink of a mug. No music and no voices.

Thanks.
```

#### 2f-2 — about to get into the car

```prompt
The attached image is a reference for the two people only — their faces, hair and clothes. It is not a frame from this shot. This shot takes place outside their house, the same morning, as they are about to leave on holiday.

A locked-off documentary shot on 35mm film. The camera stands on the front drive of an ordinary red-brick semi-detached house in a British suburb in 2008, level, about six metres in front of an ordinary silver mid-2000s estate car with a black plastic roof box on its roof bars, seen at an angle from the front corner. It is a British right-hand-drive car. Both front doors are open. The man from the reference stands at the open driver's door on the right side of the car and the woman stands at the open passenger door on the left, both seen from the waist up above the roof line.

They look at each other across the car roof. He pats the roof twice with his flat hand. She gives a small smile and a nod. Then they both just stand there a moment longer, taking a last look at the house, breathing and blinking naturally.

Flat grey overcast morning light, no sun and no shadows. Muted cool-neutral colour, fine film grain, and nothing legible anywhere, including the car's number plate.

Audio: birdsong, a distant road somewhere behind the camera, and the dull thud of a hand on a car roof. No music and no voices.

Thanks.
```

#### 2f-3 — loading the luggage

```prompt
The attached image is a reference for the two people only — their faces, hair and clothes. It is not a frame from this shot. This shot takes place outside their house, the same morning, as they pack for a holiday.

A locked-off documentary shot on 35mm film. The camera stands on the pavement at the end of a small paved front drive of an ordinary red-brick semi-detached house in a British suburb in 2008, level, about six metres behind and to one side of an ordinary silver mid-2000s estate car with a black plastic roof box on its roof bars. The tailgate is open and the boot is already packed high with soft holdalls, a rucksack and coats. The man and the woman from the reference stand at the back of the car, seen full length and side-on.

He pushes one more soft holdall firmly into the top of the packed boot, shoving it into place with both hands. She stands beside him holding a rolled-up sleeping bag, waiting her turn, and watches him with a patient look. They both breathe and blink naturally, at different moments.

Flat grey overcast morning light, no sun and no shadows. Muted cool-neutral colour, fine film grain, and nothing legible anywhere, including the car's number plate.

Audio: birdsong, a distant road somewhere behind the camera, and the soft rustle and thump of a holdall being pushed into a boot. No music and no voices.

Thanks.
```

#### 2f-4 — a cigarette by the car

```prompt
The attached image is a reference for the two people only — their faces, hair and clothes. It is not a frame from this shot. This shot takes place outside their house, the same morning, before they leave on holiday.

A locked-off documentary shot on 35mm film. The camera stands on the pavement, level, about five metres away, looking at the side of an ordinary silver mid-2000s estate car with a black plastic roof box on its roof bars, parked on the small paved front drive of an ordinary red-brick semi-detached house in a British suburb in 2008. The man and the woman from the reference lean side by side against the side of the car, seen full length, each holding a lit cigarette.

They have a quiet cigarette together before the drive. He takes a slow drag and lets out a thin stream of smoke. She holds hers low by her side and looks up the street. They stay leaning against the car, relaxed, breathing and blinking naturally at different moments.

Flat grey overcast morning light, no sun and no shadows. Muted cool-neutral colour, fine film grain, and nothing legible anywhere, including the car's number plate.

Audio: birdsong, a distant road somewhere behind the camera, and a light breeze. No music and no voices.

Thanks.
```

#### 2f-5 — Bob alone, a cigarette at the motorway services · *written 2026-09-13, unrun*

**Jack's ask:** *"only Bob smoking at a UK motorway service station, with the Bob character attached."*

🔴 **`@Bob` is the 2026 face**: eighteen years older, weathered, rough-sleeper clothes. The holiday is
2008. This prompt attaches him anyway, **on Jack's instruction**. ~~It first carried an age-down
clause and the 2008 fleece~~, and that made his hair drift ([revision 1](#2f-5--bob-alone-a-cigarette-at-the-motorway-services--written-2026-09-13-unrun)
below). **The prompt now describes nothing about him.** If he needs to read as 2008, swap the Character
for the `2b` still as the ingredient and re-run the same text.

**Easy by design:** he stands still, takes one drag and exhales. **Nothing else in frame moves.** Parked
cars and lorries stay still, and the motorway exists only as sound
([demote it to sound](../../google-flow/omni-flash.md#slop-counters-specific-to-motion-community)).
**The building's signs sit above the top of the frame**, so no services branding gets rendered.

**Paste into:** Flow → Omni Flash → **Ingredients to Video**. **Ingredient:** `@Bob`. **Aspect:** 16:9.
**Duration:** 8s.

**Revision 1, 2026-09-13: the hair changed during the clip.** Jack: *"why is his hair changing in the
video when the character is attached?"* **Cause: the prompt described him.** It gave an age
(*thirty-two*), a younger, undamaged face, tidy stubble and a new outfit, which breaks
[§19](../../google-flow/nano-banana-2.md#19--2s-do-not-restate-the-reference-applies-to-people-not-just-sets-confirmed-2026-08-27).
The prose and `@Bob` were pulling against each other. ⚠️ *Inference, unverified:* the `@Bob` sheet shows
him in a beanie in every view, so the Character never shows his hairline. Once the prose took the beanie
off, the engine had to make up the top of his head, and it made it up differently as the clip went on.
**Fix:** every appearance clause is deleted, *in 2008* and the holiday context go too, and nothing about
the shot changes. 🔴 **Trade-off:** he will now come back as 2026 Bob, with the beanie, long hair and
hoodie. If he has to read as 2008, the route is the `2b` still as the ingredient, not more prose.

**Revision 2, 2026-09-13: a black border around the clip.** In Jack's screenshot the picture sits
inside an uneven black frame with rounded corners, like a scanned film frame. ⚠️ **Inference,
unverified:** the likely cause is *"shot on 35mm film"*, which asks for a photographed film frame, and
the edges of a film frame are exactly that. **Fix:** the film-stock words are gone and the frame edge
is not mentioned at all, because
[§31](../../google-flow/nano-banana-2.md#31--27-catches-the-output-frame-too-no-letterbox-bars-produces-letterbox-bars-observed-2026-09-08-n3)
found that asking for "no border" draws one. ⬜ **Free check still owed:** §31 also caught Flow's
*viewer* adding bars that were not in the file. Download the clip and look at the original before
blaming the prompt. **Fixed in the same pass:** the same screenshot has legible lettering on the
building (*"The building's signs are above the top of the frame"* drew the signs), so that sentence
now only describes what is behind him.

**Revision 3, 2026-09-13: a camera on a stand showed up in the shot.** Jack: *"there is for some reason
a camera on a stand in the video."* **Cause: revision 2 wrote *"a still, locked-off camera on a
tripod. The camera stands in the car park"***, which is a camera, on a tripod, standing in the car
park. The engine drew the object it was given (same mechanism as the signs in revision 2 and
[§30](../../google-flow/nano-banana-2.md#30--a-physical-analogy-overrules-a-stated-number--and-it-is-how-28-keeps-happening-observed-2026-09-08)).
**Fix:** the words *camera* and *tripod* are gone from the whole prompt, audio line included. The
shot is described only as what we see and how far away it is. The framing is the same.

**Revision 4, 2026-09-13: strip it to the bone.** Jack: *"make the prompt as simple as possible because
it keeps adding shit like duplicate cigarettes."* 🔑 **Every extra noun was a new thing to draw.**
Revisions 1–3 each fixed one object the prompt had asked for by accident (hair, border, signs, a
camera), and the ashtray bin, the ash tap and the lorries were still asking for more. **Now there is one
man, one cigarette, one place and one action.** No bin, no ash, no lorries, no framing numbers.

```prompt
The man from the character reference stands outside a British motorway service station on an overcast day, smoking a cigarette. He takes a slow drag and breathes out.

Audio: distant motorway traffic. No music and no voices.

Thanks.
```

**Post:** these are filler, so trim each to whatever the narration needs. ⚠️ **Watch faces on playback**:
if either stops looking like the `2b` pair, re-roll. Run `scripts/delivery-qc.sh` before shipping.

### 2g — the last good day: a services stop · **still → video ×3** · written 2026-09-13

**Jack, 2026-09-13:** *"Tea on the car bonnet", "The chip thief", "Asleep in the passenger seat" —
one at a time, avoid AI slop, optimise for Nano Banana, use the cinematography files.* Something light
and nice before the crash. The craft basis is *Up*'s married-life montage: small, specific, slightly
silly moments with no dialogue. The audience knows what is coming, so every warm frame is dramatic
irony. 🔴 **No shot hints at blame for the crash** (no loose seatbelt, no eyes off the road): canon
leaves the crash blank.

**⬜ Next session, start here:**

1. ✅ **2g-1 tea on the bonnet.** Still and video both came back good (Jack, 2026-09-14).
2. 🟡 **2g-2 the chip thief.** Still came back good. Video written 2026-09-14, unrun. Jo keeps stealing Bob's chips from a shared Burger King bag at a
   plastic services table, and he notices on the third one.
3. 🟡 **2g-3 asleep in the passenger seat.** Still written 2026-09-14, unrun. Bob's glance was dropped
   so his eyes stay on the road. Jo dozes, Bob glances over at her and turns the
   radio down.

One shot at a time: still, then video. Run shot-craft first each time.
**The other ideas from the same list are parked, not commissioned:** Little Chef fry-up, the road atlas
route, pick 'n' mix, Tebay ducks, air guitar at a red light, feet on the dash, hand out of the window,
the TomTom falling off, the static fight, the egg sandwich, sitting on the boot, the rain picnic, and the
flask of tea.

**Shared routing for all three stills:** Flow → **Nano Banana 2** (check the picker is not on 2 Lite;
"Nano Banana Pro 2" does not exist). **One reference: the accepted `2b` still**, declared as the two
people only. **No `@Bob`** (2026 face). **No appearance description**
([§19](../../google-flow/nano-banana-2.md#19--2s-do-not-restate-the-reference-applies-to-people-not-just-sets-confirmed-2026-08-27)).
**Faces no larger than in `2b`**, or the reference cannot carry them
([reference-size rule](../../google-flow/nano-banana-2.md#-confirmed-2026-09-09-a-reference-carries-a-face-only-at-the-size-the-face-is-in-it)).
Same stock and overcast register as 2a/2b so they cut together, minus *"hyper-realistic"*, which is on
the [quality-word kill list](../../google-flow/nano-banana-2.md#️-the-quality-word-kill-list-now-includes-cinematic).

#### 2g-1 — tea on the car bonnet · **still** · written 2026-09-13, unrun

**Shot spec (shot-craft):**

1. **Job:** the first time we see them *outside* the car, being daft with each other. Warmth, plus one
   small joke the viewer gets in a second.
2. **Register:** the human-scale exception ([R2](../../cinematography/principles.md)): eye level,
   a tight two-shot, nothing monumental. No visible-cost gate, because nothing monumental is in frame.
3. **Depth:** foreground is the silver bonnet running out of focus from the bottom edge. It carries the
   **road atlas lying face-down**, which rhymes with the scene-3 alternate of the atlas face-down in the
   verge. It is never pointed at. Midground is the couple leaning on the front wing. Background is the
   car park, soft.
4. **Focal point:** his face, winning on depth position and her gaze, since she is looking at him.
5. **Light:** the flat overcast sky, and that is all. Scene 2's register.
6. **Camera:** eye height, level, about four metres, 50mm, just off the car's front corner looking back
   along the bonnet.
7. **Withheld:** the services building and its signs. Only a low roofline, out of focus.
8. **Unresolved question** ([stills §1](../../cinematography/stills.md)): he has **just burnt his
   mouth on the tea**, and she is **holding in a laugh**. Both are mid-moment, not posed.

**Anti-slop, per tell:**

- **Grins with bright teeth:** mouths closed, and *"neither shows any teeth"*.
- **Emotion words become caricature:** muscles instead of *happy*, the eyes described at more length
  than the mouths, and *"the expressions are small"*.
- **Dead or wandering eyes:** each person is given a thing to look at. He looks at his cup, she looks at
  his face.
- **Head angle defaults, especially on women:** both head angles are stated.
- **Steam overdelivers** ([§10](../../google-flow/nano-banana-2.md#10--the-atmosphere-family-is-rendered-for-free-and-overdelivers-when-named-observed-n3)):
  not named.
- **Branded cups and number plates:** a scoped negation at the end, attached to named things
  ([§27](../../google-flow/nano-banana-2.md#27--ask-for-an-object-never-an-absence--a-subtractive-shape-comes-back-inverted-observed-2026-08-30)).
- **"British" alone is weak:** concrete UK features named (patched tarmac, painted bays, a low brick
  services building), plus the era line.

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **Reference:** the accepted `2b` still,
and nothing else. **Aspect:** 16:9. **Outputs:** 2.

```prompt
SCENE:

Candid documentary photograph on 35mm Kodak Ektachrome. Fine natural grain, muted cool-neutral colour, flat overcast daylight only, calm observational tone.

The attached image is a reference for the two people only — their faces, hair and clothes. It is not a frame from this shot. This photograph is taken the same day, outside, at a motorway service station stop on their drive.

Camera and framing: Eye level and level, 50mm lens at f/2.8, standing just off the front corner of their car and looking back along the bonnet at the two of them, about four metres away. A medium two-shot from the hips up: the man and the woman from the reference lean back side by side against the front wing of the car. He is on the left of the frame and she is on the right, with a little more room on her side. The silver bonnet runs away from the bottom edge of the frame towards them, soft and out of focus nearest the lens, with a paper road atlas lying open and face-down on it. Focus sits on his face.

Action: He has just taken a sip of tea that is far too hot. His head is tipped slightly back, his eyes are squeezed half shut and wet at the corners, his brows are drawn up in the middle, and his lips are pressed tightly together. He holds the paper cup out away from himself in one hand, looking down at it. She has turned her head three-quarters towards him and is looking straight at his face. Her lower eyelids are raised, the outer corners of her eyes are creased, and her lips are pressed together, holding in a laugh. She holds her own paper cup in both hands against her chest. Neither of them shows any teeth, and neither is looking at the camera or aware of it. The expressions are small, caught mid-moment and unposed.

Environment: Their car is an ordinary silver mid-2000s estate with a black plastic roof box on its roof bars and bags piled on the back seats. Behind them, soft and out of focus, is a British motorway service-station car park: patched grey tarmac with painted white bay lines, a row of ordinary parked hatchbacks and estates, and the flat roofline of a low brick services building in the far distance.

Light: Only the flat grey overcast sky. No sun, no shadows, cool and even, unflattering.

Details: Real skin texture with visible pores and stubble, creased everyday clothes, fine natural film grain.

Constraints: Ensure historical accuracy for Britain in 2008. The paper cups are plain white with no print. No logos, signs or readable number plates anywhere in the frame. Only the two of them are in the foreground.

Compose for a 16:9 frame.

Thanks.
```

**Round 1 returned, 2026-09-13, and Jack took it straight to video.** What came back differs from the
spec in three ways, and the picture wins from here on
([§7](../../google-flow/nano-banana-2.md#7--write-the-keep-list-from-the-accepted-still-not-from-the-prose-that-made-it)):

- **They sit on the front of the bonnet, facing the lens.** The spec had them leaning on the wing with
  the bonnet receding. The result is square-on and centred, with the roof box dead centre, which is the
  [§37 symmetry magnet](../../google-flow/nano-banana-2.md#37--a-square-on-architectural-feature-is-a-symmetry-magnet-and-a-composition-adjective-will-not-move-it-observed-2026-09-12).
- **The atlas is face-up between them.** The face-down rhyme with scene 3 is lost.
- **The services building is sharp in the background**, with its signs too small to read.

Both expressions landed: his wince, and her holding in a laugh with her mouth closed.

#### 2g-1 — tea on the car bonnet · **video** · written 2026-09-13 · ✅ came back good 2026-09-14

**Tab: Frames**, with the returned still as frame one. Nothing here is a Flow Character, so
[Ingredients would re-render both faces](../../google-flow/omni-flash.md#️-ingredients-re-renders-faces--it-will-not-hold-an-unnamed-person-observed-2026-08-20).
The set and the framing also have to hold. 🔴 **The expression arc is kept small on purpose.**
[2b's full laugh lost both faces on Frames](../../google-flow/omni-flash.md#-the-tab-rule---amended-2026-08-18-ingredients-holds-identity-frames-holds-staging),
so she *stifles* the laugh (eyes narrow, shoulders shake, mouth stays shut) and never opens up.

**Built from the 2026-09-13 web pass** ([`omni-flash.md`](../../google-flow/omni-flash.md#ninth-pass--2026-09-13-academic-community)):

- **Speed stated** (*"at real speed"*, *"one short, sharp breath"*), because low motion is the trained
  default.
- **Each reaction tied to a trigger** (*"as he lowers the cup"*, *"watching him"*), not to a time.
- **Her eyes move with the laugh**, so it doesn't read as a mouth-only mask.
- **One small gesture each, not zero**, so nobody freezes like a statue.
- **Breathing and blinking at different moments.**
- **Motion only.** The frame carries the look.
- 🔴 **No colon after anyone's action, and no quotation marks**
  ([speech trap](../../google-flow/omni-flash.md#-the-speech-trap-is-punctuation-not-vocabulary)).
  The draft had *"loses the fight with her laugh: her eyes…"*, and it was caught before handover.
- **The camera stays locked** ([R7](../../cinematography/principles.md)). fal's "a tripod reads as an
  ad" is logged as dissent and not followed.

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the returned 2g-1
still. **No end frame.** **Aspect:** 16:9. **Duration:** 8s.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. Locked-off camera, a single continuous shot, everything at real speed.

As he lowers the hot cup, the man blows out one short, sharp breath through pursed lips and gives a quick small shake of his head, still frowning down at the tea. Watching him, the woman loses the fight with her laugh. Her eyes squeeze narrower, the corners of her pressed lips pull up, and her shoulders give two small shakes as her chin dips. Both of them breathe and blink naturally, at different moments. The parked cars stay where they are.

Audio: distant motorway traffic and a light wind across the car park. No music and no voices.

Thanks.
```

**Check before accepting:** both faces hold at the last frame, not just the first. The cups stay as
single cups in their hands. Nobody speaks and her mouth stays shut. The cars in the background stay
parked.

#### 2g-2 — the chip thief · **still** · written 2026-09-14, unrun

**Jack, 2026-09-14:** *"avoid AI slop, optimise for Nano Banana, use the cinematography files."* Eighth
web pass run for it ([`nano-banana-2.md`](../../google-flow/nano-banana-2.md#eighth-web-pass--2026-09-14-academic-community)).

**Shot spec (shot-craft):**

1. **Job:** 2g-1 was the two of them laughing *together*. This one is a small private con, and the viewer
   is in on it and he isn't. The joke should read in a second.
2. **Register:** the human-scale exception (R2). Seated eye level, medium two-shot, nothing monumental.
3. **Depth:** foreground is the near edge of the table and tray, soft. Midground is the two of them side by
   side on a fixed bench. Background is the food court, dimmer and soft.
4. **Focal point:** her hand with the one chip, which wins on **her gaze plus his**. Her eyes are on his
   face and his eyes are away, so the eye goes to the hand between them.
5. **Light:** one tall window along the left of the frame, flat overcast daylight through it. It lights
   the side of their faces nearer the window, and the room falls off to the right. Both ends of the
   exposure are named.
6. **Camera:** seated eye height, level, 50mm, about two and a half metres, across the table and a little
   to her side. That puts the window **at an angle, not square-on**, so it can't become a
   [§37 symmetry magnet](../../google-flow/nano-banana-2.md#37--a-square-on-architectural-feature-is-a-symmetry-magnet-and-a-composition-adjective-will-not-move-it-observed-2026-09-12).
   Faces stay no larger than in `2b`.
7. **Withheld:** the counter, the signs and the brand. The only thing outside the window is a soft car park.
8. **Unresolved question:** she has one chip lifted and **he hasn't noticed yet**. The catch is kept for
   the video, so the still is the held breath before it.

**Decisions and their reasons:**

- 🔴 **No Burger King.** Naming a brand renders its badge, and no constraint removes it
  ([§34](../../google-flow/nano-banana-2.md#34--naming-a-marque-renders-its-badging-and-no-downstream-constraint-removes-it-observed-2026-09-08)).
  The badge would probably be the *2021* logo, which is wrong for 2008 (*unverified, inferred*), and it
  would put a real company's mark in a political film. The chips come in **a plain paper bag torn open
  flat on the tray**. Brand it in post if it's really wanted.
- **The theft is frozen as geometry, not written as an action.** *"Steals"* and *"sneakily"* are
  in-progress states of the [§38](../../google-flow/nano-banana-2.md#38--a-mechanical-in-progress-state-returns-fully-open-or-fully-shut--give-it-a-physical-analogy-observed-2026-09-12)
  kind. So: one chip, between thumb and first finger, **a hand's width above the bag, her hand low over
  the table** and nowhere near her mouth. Hands near a face fail more often *(community)*.
- **One chip, and a small untidy pile.** Image models miscount, and overlapping piles do worst
  *(NumBench 2026)*. Uniform, glossy, perfectly arranged food is its own slop tell.
- **His near hand holds something**, a plain white paper cup, so it's a grip and not a spread hand.
- **Each gaze has a named target.** His eyes are on the car park through the window, hers are on his
  face. There are no emotion words: the expressions are muscles, eyes longer than mouths, closed mouths,
  a floor (*"a stranger would take a second"*), and the wrong readings named.
- 🔑 **Few nouns.** Every noun gets drawn (2f-5, revisions 1–4). No salt sachets, no ketchup, no
  second meal, no phone, no lorries, no signs.
- **Same stock and wording shape as 2g-1**, which came back good, so the two cut together.

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **Reference:** the accepted `2b` still, and
nothing else. **No `@Bob`.** **Aspect:** 16:9. **Outputs:** 2.

```prompt
SCENE:

Candid documentary photograph on 35mm Kodak Ektachrome. Fine natural grain, muted cool-neutral colour, flat overcast daylight, calm observational tone.

The attached image is a reference for the two people only — their faces, hair and clothes. It is not a frame from this shot. This photograph is taken the same day, indoors, at a table in a British motorway service station food court, halfway through their drive.

Camera and framing: Seated eye level and level, 50mm lens at f/2.8, from across the table and a little to her side, about two and a half metres away. A medium two-shot from the waist up: the man and the woman from the reference sit side by side on a fixed bench behind a small plastic table. He is on the left of the frame, nearer the window, and she is on the right. The near edge of the table and a plastic tray run across the bottom of the frame, soft and out of focus. On the tray, in front of him, a plain white paper bag has been torn open flat, with a small, untidy pile of chips on it, half eaten. The chips are bent, broken and uneven in colour. Focus sits on her hand and her face.

Action: He has turned his head towards the window and is looking out at the car park, chewing, relaxed, with no idea anything is happening. His nearer hand is wrapped around a plain white paper cup on the table. She has turned her face three-quarters towards him and is watching his face closely. Her eyes are steady and a touch wider than usual, and her eyebrows are level. Her lips are pressed together over a mouthful, one cheek very slightly full. Her nearer hand has come across in front of him, low over the tray, holding a single chip between her thumb and first finger, lifted a hand's width above the bag. Neither of them shows any teeth, and neither is looking at the camera or aware of it. She is not grinning and not pulling a guilty face; a stranger would take a second to see she is up to something. Caught mid-moment and unposed.

Environment: A tall window runs along the left side of the frame at an angle, with a soft, out-of-focus grey car park beyond it. Behind them and to the right, the food court is dimmer and soft: ordinary fixed tables and plastic seats, mostly empty.

Light: Only the flat grey daylight coming in through the window from the left. It lights the side of their faces nearer the window, and the rest of the room falls away into a dimmer, cooler grey. The window is bright but not blown out, and the far side of the room is dim but still readable. No sun, no warmth, unflattering.

Details: Real skin texture with visible pores and stubble, creased everyday clothes, fine natural film grain.

Constraints: Ensure historical accuracy for Britain in 2008. The paper bag and the paper cup are plain white with no print. No logos, signs or readable text anywhere in the frame. Only the two of them sit at the table.

Compose for a 16:9 frame.

Thanks.
```

**Check before accepting:** exactly one chip in her fingers, and her hand has five fingers. The bag and cup
carry no logo. Her face reads as watchful, not as a grin. Both faces match `2b`. The window runs at an
angle and hasn't turned into a centred backdrop.

✅ **Came back good, 2026-09-14 (Jack).**

#### 2g-2 — the chip thief · **video** · written 2026-09-14, unrun

**Shot spec (shot-craft):** the still is the held breath, so this clip **spends it on the catch**. One
beat: **his eyes come back from the window to her hand, she freezes, holds his look, and eats the chip
anyway.** Her carrying on is the button. The camera stays locked (R7), and no camera movement is spent.

**Built the same way as 2g-1's video, which came back good:**

- **Tab: Frames**, with the accepted 2g-2 still as frame one. Nothing is a Flow Character.
- **Motion only.** The frame carries the look, the food court and the bag.
- **Speed stated, each reaction tied to a trigger, eyes described with every mouth, one small gesture
  each, breathing and blinking at different moments.**
- 🔴 **No colon after an action, and no quotation marks** (speech trap).

**The two risks, and how the prompt handles them:**

- 🔴 **His head turn.** In the still his face is turned towards the window. Every degree he turns shows face
  that Frames has to invent, and invented face is where likeness goes (2b). So **his eyes move first and
  his head turns only partway**, and the prompt never asks for him to face the lens.
- ⚠️ **Her hand to her mouth.** Hands near a face fail more often (eighth web pass, community). It happens
  **once, at the end, as a single short movement**. Fallback if the fingers or the chip melt: trim the clip
  before she eats it. The freeze under his look is already the joke.

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted 2g-2 still.
**No end frame.** **Aspect:** 16:9. **Duration:** 8s.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. Locked-off camera, a single continuous shot, everything at real speed.

Still chewing, the man lets his eyes drift back from the window, and they land on the chip in her fingers. His head follows only partway round, and he stops chewing. One of his eyebrows lifts a little and his eyes narrow slightly. Seeing him look, the woman freezes with the chip in mid-air, her eyes fixed on his, and blinks once. Then, holding his look, she slowly lifts the single chip to her mouth and eats it, lips closed as she chews. The corners of his mouth twitch, and he gives a small slow shake of his head. Both of them breathe and blink naturally, at different moments. Everything on the tray stays where it is.

Audio: the quiet hum of a service station food court, the clatter of a tray somewhere far off. No music and no voices.

Thanks.
```

**Check before accepting:** both faces hold at the last frame, especially his after the turn. One chip
in her fingers, which goes into her mouth and doesn't multiply or vanish. Nobody speaks and no teeth show.
The chips on the tray stay put.

#### 2g-3 — asleep in the passenger seat · **still** · written 2026-09-14, unrun

**Shot spec (shot-craft):**

1. **Job:** the last shot of them together before the crash, and the quietest. 2g-1 and 2g-2 were jokes
   *between* them. This one is care nobody sees: she is asleep, and he turns the radio down so she stays
   asleep. The crash comes after it, which makes it land hardest.
2. **Register:** the human-scale exception (R2). Back inside the car, 2b's world, later the same day.
3. **Depth:** foreground is the centre console and the car stereo, soft at the bottom edge. Midground is
   the two of them in the front seats. Background is the luggage packed behind the seats, and the side
   windows.
4. **Focal point:** his hand on the volume knob, then his face. The hand wins on depth position, since it's
   the nearest sharp thing, and his face wins on light.
5. **Light:** the flat grey sky through the windscreen, **duller than in 2b**, because it's later in the
   afternoon. It lights their faces from the front, and the back of the car falls away into shadow. It
   matches 3b's grey, so the cut into the crash doesn't jump.
6. **Camera:** on the dashboard, **a little to the passenger side of centre**, 24mm, looking back into the
   car. It sits lower and wider than 2b, so the console fits in the frame, the faces come out **smaller than
   in 2b** (the reference-size rule), and the frame isn't a copy of 2b.
7. **Withheld:** her face, mostly. She is turned towards her window, asleep, so the reference has less to
   carry, and the shot is about him.
8. **Unresolved question:** his fingers are *on* the knob, mid-turn, with the volume on its way down.

**Decisions and their reasons:**

- 🔴 **Changed from the list: Bob does not glance over at her.** The 2g rule is *no eyes off the road*,
  since canon leaves the crash blank and a driver looking at his wife right before it would point blame.
  **His eyes stay on the road.** He turns the radio down by feel, and the care is in the hand, not the
  look. ⬜ Jack's call if he wants the glance back.
- **The road atlas slips face-down on her lap.** This finally lands the scene-3 rhyme that 2g-1 lost (the
  atlas face-down in the verge). It is never pointed at.
- **Both seatbelts are on**, stated as a fact rather than a negation, per the no-blame rule.
- **The stereo is a plain built-in unit with a round volume knob and no readable display**, so it doesn't
  render a brand or a station name. His fingers grip the knob, which is a safer pose than an open hand
  (eighth web pass).
- **Asleep is written as muscles**, not as *peaceful*: head tipped against the window, jaw loose, eyelids
  fully shut, one hand slack. Emotion words get caricatured.
- **No appearance description, and no `@Bob`.** The reference is declared as the people only, and the
  luggage is described briefly as set.
- **Same stock and wording shape as 2g-1 and 2g-2.**

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **Reference:** the accepted `2b` still, and
nothing else. **No `@Bob`.** **Aspect:** 16:9. **Outputs:** 2.

```prompt
SCENE:

Candid documentary photograph on 35mm Kodak Ektachrome. Fine natural grain, muted cool-neutral colour, flat overcast daylight, calm observational tone.

The attached image is a reference for the two people only — their faces, hair and clothes. It is not a frame from this shot. This photograph is taken later the same day, in the late afternoon, inside their car on the motorway, as they drive on after a service station stop.

This is a British right-hand-drive car. The camera faces backwards into the car, so the man driving appears on the LEFT of the frame and the woman in the passenger seat appears on the RIGHT.

Camera and framing: 24mm lens at f/2.8, the camera resting low on the dashboard a little to the passenger side of centre, looking back into the car at the two people in the front seats. Both are seen from the waist up, fairly small in the frame. The centre console between the seats runs up from the bottom of the frame, with a plain built-in car stereo and its round volume knob closest to the lens, soft and slightly out of focus. Focus sits on his hand and his face.

Action: He is driving, his eyes on the road ahead, looking just past the side of the camera and not into it. His right hand rests on the top of the steering wheel. His left hand has reached down to the stereo without looking, his fingers around the round volume knob, turning it down. His lips are together, the corners of his mouth only just lifted, and his eyes are soft and a little tired. She is fast asleep in the passenger seat, her head tipped sideways against the top of the seat and the window, her face turned mostly away from the camera towards her window, her eyelids fully shut and her jaw loose. One hand lies slack in her lap on an open road atlas that has slid over and lies face-down across her knees. Both are wearing their seatbelts across their chests. Neither is aware of the camera. Unposed, a quiet ordinary moment.

Environment: The inside of an ordinary mid-2000s family car with grey cloth seats and a plain dark roof lining. Behind the front seats, soft holdalls and coats are packed high. Through the side windows, a grey motorway verge and embankment blur past.

Light: Only the dull grey afternoon sky coming through the windscreen, lighting their faces evenly from the front, duller than midday. The back of the car falls away into shadow, and the side windows are pale grey but not blown out. No sun, no warmth, unflattering.

Details: Real skin texture with visible pores and stubble, creased everyday clothes, fine natural film grain, slight motion blur in the verge through the side glass.

Constraints: Ensure historical accuracy for Britain in 2008. The stereo's small display is dark and plain, with no readable text. No logos, badges or readable text anywhere in the frame. Only two people are in the car.

Compose for a 16:9 frame.

Thanks.
```

**Check before accepting:** his eyes on the road and not on the lens. Her face stays mostly turned away and
still reads as Jo. He has one left hand, on the knob, with five fingers. The stereo has no brand and no
text. Both seatbelts are on. The atlas is face-down. He is on the left and she is on the right.

---

## Scene 3 — the crash

**3a is not a generation.** The crash is never shown: 2b's laugh cuts to black mid-sound
and the impact happens in the black. See [`story.md` beat 3](./story.md).

### 3b — the indicator, still ticking · **still** · accepted · 🔒 the canon shot

No seats and no cabin in frame — two empty seats would read as *both* of them gone, and
Bob survives. Came back wider than specified, which is an improvement: the tilted verge
climbing the windscreen is the best thing in the frame and a tighter crop loses it.

```prompt
SCENE:

Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone. A close view of the instrument cluster of an ordinary mid-2000s family car, from just behind the steering wheel.

Subject: The instrument binnacle — plain analogue speedometer and rev counter behind slightly dusty glass, needles resting dead at zero, the dial backlighting off. In the small telltale panel between them, a green arrow-shaped indicator light is lit, glowing a weak cold green, the only clean light in the frame. Beside it one or two other small warning lights glow dimly in dull red and amber, the way a dashboard does when the ignition is on and the engine is not running. A fine dusting of grit and tiny fragments lies across the top of the dashboard.

Environment: The dark upper rim of the steering wheel crosses the bottom of the frame, out of focus. Beyond the binnacle, the windscreen fills the upper right of the frame, blown out to flat grey-white, with wet grass and the dark tangle of a bare hedgerow pressed close against the far side of the glass at a distinctly wrong angle, so the horizon out there does not agree with the dashboard. A fine crack runs across the top of the screen, soft and out of focus. No seats and no cabin interior are visible — only the binnacle, the wheel rim and the glass.

Camera and framing: 50mm lens at f/2.0, camera close in and low, roughly where a driver's eyes would be, angled slightly down at the dials. Static and level to the dashboard, so the tilt of the world outside reads as the car being wrong rather than the camera.

Light: Only the flat grey daylight coming through the windscreen, and the faint glow of the telltales themselves. Cold, dim and unflattering, the dials in shadow. No sun, no warmth.

Details: Real film grain, dust on the instrument glass, faint reflections of grey sky in the dial covers, worn plastic textures. Cold, ordinary and unstaged.

Compose for a 16:9 frame. Render at 4K.

Thanks.
```

### 3b — the indicator, still ticking · **video**

Omni Flash, Frames tab, the 3b still as frame 0, 8s. **Fallback if it fails:** hold the
still and let the tick run. Blinking lights are one of the few things that morph, and the
sound was always the shot.

```prompt
Use the attached image as the locked opening frame and continue directly from it. The green arrow telltale on the dashboard flashes on and off at a steady even rhythm, roughly one flash per second, while the red and amber warning lights beside it stay lit without changing and the needles stay resting at zero. Beyond the windscreen the grass and bare hedgerow stir very slightly in the wind. Everything else stays exactly where it is. Locked-off camera, no camera movement, single continuous shot. Shot at 24fps with a 180-degree shutter. Maintain the grain, colour and flat overcast light of the image.

Audio: the slow steady mechanical tick of a car indicator relay, and faint wind outside the glass. No dialogue, no music.

Thanks.
```

---

## Scene 3 alternates — shot, kept, not the canon choice

Four other versions of 3b were generated and are held in reserve. The amber corner lamp
is the wide version of the same idea and is a candidate to *precede* the dashboard.

### The amber corner lamp in the grass · **still**

```prompt
SCENE:

Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone. An extremely close, low view of the front corner indicator lamp of a car, down among wet grass.

Subject: A moulded amber plastic indicator lens, lit from within, glowing a dull warm orange against the cold grey daylight — the only warm thing anywhere in the frame. The plastic has a fine moulded texture and a scatter of water beads across it, and one hairline crack running off the corner. The body panel it sits in is silver and completely out of focus, unreadable as any particular part of any particular car.

Environment: Coarse wet winter grass and a few dead leaves crowd the lamp, several blades crossing directly in front of the lens and running diagonally across the frame at a distinctly wrong angle, as though the ground and the car do not agree about which way is down. Behind, a soft grey wash of hedgerow and overcast sky, entirely out of focus. Nothing else in the frame is legible — only the lamp, the grass, water and soft grey light.

Camera and framing: 100mm macro at f/2.0, camera set right down in the grass, almost touching it, the lamp filling roughly a third of the frame and sitting off-centre. Static and level to the camera, so the diagonal of the grass reads as the world being tilted rather than the camera.

Light: Flat, even, shadowless overcast daylight, cold and colourless. The only other light source is the amber lamp itself, throwing a weak orange glow onto the two or three nearest blades of grass and no further.

Details: Real film grain, real water beading, individual wet grass blades sharp against the lens and soft everywhere else. Cold, ordinary, unstaged.

Compose for a 16:9 frame. Render at 4K.

Thanks.
```

### The road atlas, face-down, pages lifting · **still**

```prompt
SCENE:

Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone. A low, close, static view down into the rough grass verge at the edge of a wet single-track English country lane.

Subject: A paperback road atlas lies face-down and open in the wet grass, spine upward, thrown rather than set down — splayed wide, several pages bent and folded back under it, a couple of pages standing up loose, the coloured printed maps just readable on the exposed edges. The paper is soaking through and going translucent in patches, one page smeared with mud. The grass is crushed flat underneath where it landed.

Environment: Coarse winter grass, mud, dead leaves and a little grit along the verge. Behind it, out of focus, the wet patched tarmac of the lane runs away to one side, and the dark tangle of a bare hedgerow closes off the top of the frame. Nothing else is in the frame — only grass, mud, paper and wet road.

Camera and framing: 50mm lens at f/2.0, camera held very low, about thirty centimetres above the ground, looking down and slightly along the verge. Static and level, an unhurried documentary angle. Focus sits on the atlas; everything behind falls away soft.

Light: Flat, even, shadowless overcast daylight from a solid pale grey sky. Cool and colourless. The wet paper and grass read as dull sheen rather than bright highlights.

Details: Real film grain, real wet-paper texture, water beading on the pages and on the blades of grass. Everything muted, cold and ordinary, as though a stills photographer arrived afterwards and photographed the ground.

Compose for a 16:9 frame. Render at 4K.

Thanks.
```

Its motion prompt (Omni Flash, Frames, 8s):

```prompt
Use the attached image as the locked opening frame and continue directly from it. The loose pages of the road atlas lift and drop in the wind, one page peeling up and falling back, and the grass around it stirs. Everything else stays exactly where it is. Locked-off camera, no camera movement, single continuous shot. Shot at 24fps with a 180-degree shutter. Maintain the grain, colour and flat overcast light of the image.

Audio: wind moving through grass. No dialogue, no music.

Thanks.
```

### The atlas with the biro route ending mid-page · **still**

The metaphor version — the route someone drew stops in open country. The rolled tent bag
in the background is a deliberate plant, unremarked; delete that clause to drop it.

```prompt
SCENE:

Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone. A low, close, static view down into the rough grass verge at the edge of a wet single-track English country lane.

Subject: A paperback road atlas lies open and face-up in the wet grass, thrown rather than set down, its spine twisted and one corner folded under. The exposed double-page spread is a printed road map — pale green and buff countryside, thin yellow and white road lines, a fine blue thread of river — and across it someone has traced a route by hand in blue biro, a slightly wobbly line following the roads from one edge of the page. The line runs a third of the way across the spread and simply stops, in open country, nowhere near anything. The paper is soaking through, going translucent and darkening in patches, the ink beginning to bleed at the wet edge. The printed place names are far too small and rain-blurred to read.

Environment: Coarse winter grass, mud and dead leaves. Behind the atlas and well out of focus, a rolled camping tent in a long green nylon bag lies half in the grass. Beyond that, the wet patched tarmac of the lane and the dark tangle of a bare hedgerow close off the top of the frame.

Camera and framing: 50mm lens at f/2.0, camera held very low, about thirty centimetres above the ground, looking down at the open page. Static and level. Focus sits hard on the biro line where it ends; the tent and the lane behind fall away completely soft.

Light: Flat, even, shadowless overcast daylight from a solid pale grey sky. Cool and colourless. Wet paper reads as dull sheen, not highlight.

Details: Real film grain, real wet-paper texture, water beading on the page and in the fold, individual blades of grass bent under the weight of the book.

Compose for a 16:9 frame. Render at 4K.

Thanks.
```

### Broken glass on wet tarmac · **still**

Toughened side-window glass breaks into blunt blue-green cubes, not shards — and wet, it
goes dull. Sparkle is what would have made it read as generated.

```prompt
SCENE:

Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone. A low, close, static view down at the wet surface of a single-track English country lane.

Subject: A scatter of broken car window glass lying across the wet tarmac — hundreds of small blunt cubes of toughened glass, roughly sugar-lump sized, pale blue-green, spread unevenly across a couple of metres of road with a denser drift near the centre and stray pieces trailing off out of focus. The glass is wet and dull rather than sparkling, the light sitting flat and greenish inside the cubes, several of them settled into the water held in the road's pits and cracks.

Environment: Coarse patched tarmac, grey and pitted, with old repairs, grit, dark damp patches and a faded white line running away diagonally through the frame. At the very top edge, out of focus, the grass verge and the dark tangle of a bare winter hedgerow. Nothing else is in the frame — only wet road, grit, water and glass.

Camera and framing: 50mm lens at f/2.0, camera held very low, about twenty-five centimetres above the road, looking down and slightly along the lane. Static and level, an unhurried documentary angle. Focus sits on the nearest drift of glass; the road falls away soft behind it.

Light: Flat, even, shadowless overcast daylight from a solid pale grey sky. Cool and colourless. Wet surfaces read as dull sheen, not bright highlights.

Details: Real film grain, real wet-tarmac texture, water beading and standing in the low points. Everything muted, cold and ordinary, as though a stills photographer arrived afterwards and photographed the road.

Compose for a 16:9 frame. Render at 4K.

Thanks.
```

### Starlings on a telegraph wire · **still**

Shot as a still deliberately — birds in flight are many small bodies, the exact failure
class the engine notes say to demote to sound. The gap asked for did not render.

```prompt
SCENE:

Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone. A low upward view of a telegraph wire crossing a flat, empty, overcast sky above an English country lane.

Subject: A row of small dark birds — starlings, plain silhouettes — perched along a single sagging telegraph wire that runs across the frame. They are spaced almost evenly, all facing the same way, hunched and still. Near the centre of the row there is one clear empty stretch of wire, wide enough for a bird, with the birds either side of it holding their spacing. Nothing occupies it.

Environment: A solid, featureless pale grey-white overcast sky fills almost the whole frame. At the very bottom edge, the dark blurred top of a bare winter hedgerow, and at one side the weathered top of a wooden telegraph pole with its crossbar and insulators. Nothing else is in the frame — only sky, wire, pole and birds.

Camera and framing: 135mm lens at f/4, camera low and angled up, so the wire crosses the upper third of the frame and the sky carries everything else. Static and level. Focus sits on the birds; the pole edge falls soft.

Light: Flat, even, shadowless overcast daylight. The birds read as near-black silhouettes against the bright sky, with no rim light and no sun anywhere.

Details: Real film grain, slight atmospheric haze, the wire thin and slightly out of true. Cold, plain and unremarkable.

Compose for a 16:9 frame. Render at 4K.

Thanks.
```

Its motion prompt — the whole flock leaves and the wire is left empty, which is both the
better beat and the safer generation (the frame becomes empty sky within a few frames):

```prompt
Use the attached image as the locked opening frame and continue directly from it. The birds sit still on the wire for a moment, and then the whole flock takes off at once, every one of them leaving in the same second and climbing out through the top of the frame. The wire is left completely empty, swinging very slightly where their weight came off it, and it stays empty for the rest of the shot. Locked-off camera, no camera movement, single continuous shot. Shot at 24fps with a 180-degree shutter, so the birds smear with natural motion blur as they go. Maintain the grain, colour and flat overcast light of the image.

Audio: a sudden clatter of wings and alarm calls, then wind and nothing else.

Thanks.
```

---

## Scene 8 — the car park

### 8b — the two men, long lens · **still** · accepted 2026-08-27 · 🔒

**Accepted round 1 of this design, after seven rounds across three earlier designs.** The
shot Jack picked out of the whole scene — *"the blurryness and rain makes it so the details
don't matter and it looks really cool."*

**Reference:** the 8a car park plate, as the location. **Characters cast:** `@Tarquin-new`
and `@Bob` — ⚠️ neither binds at this distance ([`nano-banana-2.md` §12](../../google-flow/nano-banana-2.md)),
so the men are carried by the prose, not the Characters. Bob's description is lifted from
[`characters/bob.md`](./characters/bob.md).

**Why this design won.** Three earlier ones failed: a lone low single (four rounds, the face
read sad), an over-the-shoulder (an invented face appeared in the foreground —
[§18](../../google-flow/nano-banana-2.md)), and a from-inside-the-car shot (good, but needed
`@Bob` and never got a second run). **The long lens solved the face problem by removing faces
from the argument** — at forty metres through rain, no likeness has to hold. It is also the
one shot in camping that reaches for **British social realism** — Loach's long lens from a
distance ([`registers.md` §4](../../cinematography/registers.md)) — the register `R1` names as
closest to our reader's own visual vocabulary and which we had never used.

```prompt
Generate a still photograph. Use the attached car park image as the reference for the location: the same painted bays and wet tarmac, the same rows of ordinary small cars, the same overcast winter light, the same muted colour and grain, and the same black BMW X8.

Camera: a long telephoto lens, 200mm at f/4, from about forty metres away across the car park, at the chest height of a standing person and level, not tilted. The long lens flattens the whole scene onto one plane, so the rows of cars, the two men and the far side of the car park are stacked on top of one another with almost no sense of distance between them. Running across the very bottom of the frame and thrown completely out of focus, the wet roofs of two ordinary parked cars in the near row, which the camera is looking between.

In the middle distance, small in the frame and seen side on: the black BMW X8, stopped square across the painted white line between two parking bays and filling both of them, its driver's door standing open. Pitched in the very next bay, close enough that the open door almost reaches it, a cheap two-person dome tent in faded blue and grey, sagging at one corner where a pole is bowed, a square of duct tape over a tear in the flysheet.

The two men are only three or four metres apart with nothing between them but wet tarmac. Standing on the tarmac beside the open door, the man from the first character reference: an olive gilet over a dark jumper, dark jeans, standing straight and still, his head up and turned toward the seated man, looking at him. Sitting on the ground at the mouth of the tent, the man from the second character reference: a white British man of about fifty, weathered older, in a dark woollen beanie and a charity-shop coat a size too big worn over a hoodie and more layers, everything grimed and soft from being lived in. He sits hunched with his knees drawn up and his hands pushed into his sleeves, turned toward the standing man. Both men are far away and small, and both are softened by distance and by the rain in the air between them and the camera, so no detail of either face can be made out.

Behind them: more painted bays running away, a far row of ordinary parked cars stacked flat by the long lens, and a narrow band of empty pale grey sky along the top of the frame. No building of any kind stands behind them.

Light: the overcast sky is the only source, flat and shadowless across the whole car park, the tarmac dark and wet and the sky pale grey and slightly overexposed.

A documentary press photograph on 35mm film taken from a long way off — fine natural grain, muted cool-neutral colour, compressed perspective, shallow focus falling away in front of and behind the two men. Heavy fine rain falling through the whole frame, visible as streaks against the pale sky and the dark cars. Every surface in the frame is plain and unlettered.

Compose for a 16:9 frame.

Thanks.
```

⚠️ **Known and accepted:** the faces read slightly strange at full size. **Left alone
deliberately** — they are tiny and rain-softened, and the fix for them is not a better still,
it is keeping the clip near-static so the engine has no reason to re-render them.

---

### 8b-fog — the two men in the void · **still** · written 2026-09-08, unrun

**Jack's ask, 2026-09-08:** *"this type of shot… where films pause on only one aspect, the
important parts, almost like the matrix, everything else disappears, like we are in the
characters' aetherial subconscious."* Same beat as [`8b`](#8b--the-two-men-long-lens--still--accepted-2026-08-27),
same camera angle, **everything except the two men and their two objects removed.**

**This is a REGISTER, not a shot.** If it works it should be used deliberately and rarely —
principle 16's rule for a colour code applies to a frame device: **the power is in the rarity.**
Two of these in a film is a language; five is a filter.

#### What changes from `8b`, and why each one

| Change | Why |
|---|---|
| **No location reference attached** | Jack's instruction. The reference *is* the car park, and the car park is what we are deleting |
| 🔑 **Distance drops 40m → ~18m, lens 200mm → 135mm** | Jack wants the men to *"look more like themselves"*. [§12](../../google-flow/nano-banana-2.md) — **a Character binds to a face**, and at forty metres there is no face to bind to. `8b` carried both men in prose for exactly this reason. Faces must be big enough in frame or `@Bob` and `@Tarquin-new` do nothing. **The angle is unchanged** — level, chest height, side on |
| **No appearance description for either man** | [§19](../../google-flow/nano-banana-2.md). With Characters cast, prose about wardrobe or age *overrules* them. Only action and expression |
| **Each man anchored to a named side** | [§26](../../google-flow/nano-banana-2.md) — the one condition we believe carries two Characters in one still. Tarquin **left**, Bob **right**, matching `8b`'s geography |
| **The foreground car roofs are replaced by tarmac and one painted line** | The cars go, but principle 1 does not: **an empty foreground is the most common cause of a flat frame.** The bay line running out of frame toward the lens does the same depth job for free |
| **Fog, named and pushed** | The erasure device — see below |

#### 🔑 The one finding that decides whether this works

[§27](../../google-flow/nano-banana-2.md): **ask for an object, never an absence.** `1a-year`
asked for numerals *torn out* of cloud and got soot-coloured numerals painted *on* it — the model
has no trained visual for an absence, so it renders the nearest positive trope it owns.

**"The other cars have disappeared" is an absence. Fog is an object.** The prompt therefore never
asks for anything to be removed; it describes a substance that fills the frame from six metres out
and states what the substance contains, which is more of itself.

⚠️ **And [§10](../../google-flow/nano-banana-2.md) — the atmosphere family overdelivers when
named — is normally a bug and is the feature here.** Naming fog usually makes it dominate the
frame. That is the entire brief. **This is the one shot in the film where §10 should be pushed
rather than deleted.** The counter-risk is that it overdelivers onto the subjects too, so the
prompt states the visibility distance and that everything inside it stays sharp
([§11](../../google-flow/nano-banana-2.md): an undefined background stacks; naming what stays
sharp is what collapses it).

#### The gates

1. **Job:** the first frame in the film where the car park stops being a place and becomes a
   proposition. `8b` says *two men, three metres apart, in a car park*. This says *two men, three
   metres apart* — and the car park is only the paint under their feet.
2. **Visible cost:** Bob on wet tarmac, the bowed pole, the taped tear. Present and legible at
   eighteen metres, which is more than `8b` could show.
3. **Light:** the overcast sky through fog — omnidirectional, shadowless. **One motivated
   exception: the X8's own interior light and running lights.** 🔑 Tarquin's machine is the only
   thing in the frame making light, and Bob has none. It is also the dark-frame anchor working in
   reverse — in a pale void the eye needs the *darkest* object, and that is the car.

⚠️ **The trade Jack should know about.** `8b` was accepted because *"the blurryness and rain makes
it so the details don't matter and it looks really cool."* Coming in to eighteen metres to make
the Characters bind **spends exactly that** — the faces now have to hold up. If they come back
strange, the fix is not a better prompt, it is going back out to forty metres and losing the
likeness. **Those two wants are in direct opposition and cannot both be had in one frame.**

```prompt
Generate a still photograph.

Camera: a 135mm telephoto lens at f/4, standing on wet tarmac about eighteen metres away, at the chest height of a standing person and perfectly level, not tilted down or up. A medium-long two-shot of both men seen side on, in profile, standing on the same flat ground the camera stands on.

On the left of the frame, standing on the tarmac beside the open driver's door of a black BMW X8: the man from the first character reference. He stands straight and still with his weight back, his chin slightly lifted, his mouth closed and level, his head turned toward the other man and his eyes aimed down at him. The X8 is stopped square across the painted white line between two parking bays and fills both of them, seen side on, its driver's door standing open toward the camera.

On the right of the frame, sitting on the wet ground at the mouth of a cheap two-person dome tent in faded blue and grey: the man from the second character reference. He sits hunched with his knees drawn up and his hands pushed into his sleeves, his head turned up and toward the standing man, his brows level and his mouth closed. The tent sags at one corner where a pole is bowed, and a square of duct tape covers a tear in the flysheet.

Three or four metres of empty wet tarmac lie between the two men, with the painted white line of one bay running across the ground between them. In the very front of the frame, close to the camera and running away from it toward the men, more wet tarmac and one more painted white bay line, catching the pale light on the water.

The whole car park is filled with thick cold fog. Six metres past the men the fog closes into a flat unbroken wall of pale grey, and it fills the entire frame behind and above and to both sides of them, edge to edge and top to bottom. The painted bay lines and the wet tarmac fade out into that pale grey a few metres past the tent and are simply gone. There is nothing in the fog: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no people, no horizon line and no sky. Only fog.

Light: an overcast winter sky above the fog, so the light arrives from every direction at once, flat and completely shadowless, and the ground throws no shadows at all. The one exception is the car: the X8's interior light is on behind the open door and its running lights are lit, two small hard points of warm light in an otherwise entirely cold grey frame, laying a weak wash of light on the wet tarmac immediately around it. The black of the car is the darkest thing in the picture and the fog is the palest.

A documentary press photograph on 35mm colour film: fine natural grain, muted cool-neutral colour, very low saturation. Everything in the picture is sharp and in focus, from the painted line in the foreground to the tent. Fine rain falls through the frame. Every surface in the frame is plain and unlettered, apart from the car's own badges.

Compose for a 16:9 frame.

Thanks.
```

⬜ **Unrun.** Attach `@Tarquin-new` first, `@Bob` second, nothing else —
[§26](../../google-flow/nano-banana-2.md) records that attachment order mattered enough to write
down, and that the location reference goes last, which here means there is none.

#### Round 1 — run 2026-09-08. The void works; the car and the craft do not

**The erasure landed on the first try.** Fog closed the car park exactly as designed, the bay
lines faded into it, and the two men held. **§27 is confirmed on the positive side:** asking for a
*substance* rather than an *absence* produced the absence. **That is the finding worth keeping.**

**Seven faults, in the order they cost the picture:**

| # | Fault | Cause | Fix in round 2 |
|---|---|---|---|
| 1 | 🔴 **The car is not an X8** — it came back a boxy upright SUV with a squared roofline | The name alone is not enough. **X8 is a thin spot in the training data**, and a model given a marque it half-knows renders the marque's *average* | **Name it and draw it**: the fastback roofline dropping to a short rear deck, slim split headlights, the tall kidney grille, gloss black trim, big dark alloys |
| 2 | 🔴 **Both objects face across each other; canon has them parallel** | The prompt described a stand-off, not the 8a geography Jack's aerial shows | The X8 sits **nose-in across two bays, rear three-quarter to the camera**, tail lights lit — the aerial's arrangement. It also breaks the mirror |
| 3 | **Dead-centre symmetry** — men mirrored, fog band level, everything square | Nothing in the prompt asked for asymmetry, and symmetry is the model's resting state. It is [the named slop tell](../../google-flow/nano-banana-2.md#the-anti-slop-toolkit) | *"slightly off-centre and not quite level"*, and the car rotated out of broadside |
| 4 | **Empty foreground** | Round 1 asked for tarmac and a painted line and got a bare bottom third — [principle 1](../../cinematography/principles.md), the commonest cause of a flat frame | A **foreground occluder**: the corner of one more painted bay and a kerb-edge puddle crossing the very bottom, close and soft |
| 5 | **No rain in the air** | The ground was described as wet; the air was not. [§10](../../google-flow/nano-banana-2.md) — **weather nouns underdeliver and need magnitude shouted at them** | Rain named with consequence: rings on the standing water, the tent fabric darkened where it has soaked |
| 6 | **No light anchor at all** — the frame is one uniform grey | The X8's interior light was asked for but is nearly invisible. In a **pale** void the eye needs the **darkest** object and one point of warmth | **The tail lights**, which is what Jack's own aerial already shows: two red bars and a red wash on the wet tarmac |
| 7 | **Both men parked and posed** | The 8b lesson repeating — *when the frame will not perform, move the moment earlier.* Two men standing still facing each other has no unresolved question in it | **Mid-action**: Tarquin still closing the car door behind him, Bob mid-shift as he looks up |

⚠️ **Also cosmetic and worth naming:** the tent came back new, the clothes came back clean, and a
scatter of dark specks appeared on the tarmac — the model's generic "debris". **Environmental
imperfection has to be specified or the engine supplies its own.**

#### Written for Nano Banana Pro

Three things changed in *how* these are written, from
[Pro's own guidance](../../google-flow/nano-banana-2.md#pro-is-a-different-animal-it-plans-before-it-draws):

- **Pro's slot order is Subject · Composition · Action · Location · Style · Constraints** —
  composition promoted above action. All three prompts below follow it.
- **Descriptive, not repetitive.** Pro penalises a long prompt with competing style statements
  more than a short one. Round 1's texture words appeared twice; here they appear once, at the end.
- 🔑 **Pro reasons before it draws, so a statement of *structural* intent lands.** Each prompt
  opens by naming the job of the picture. ⚠️ This is **not** licence to state a connotation —
  *"the gloss should read as obscene"* is still the failure recorded at 5a.

🔴 **The vendor guidance says "if an image is 80% right, edit it rather than regenerate." We do
not do that.** Our standing ruling is a new prompt every time; editing an existing generation has
not worked here. Follow the house rule, not the guide.

### 8b-fog · variant A — the fog limbo · **still** · written 2026-09-08, unrun

```prompt
A still photograph for a film. The job of this picture is to take a supermarket car park away and leave only the two men and the two things they own, standing on the paint.

Camera: a 135mm lens at f/5.6, eighteen metres back, at the chest height of a standing person and level, framed slightly off-centre and not quite square to the bays, the way a photographer standing in the rain would actually hold it.

Composition: on the left, a large black BMW X8, parked nose-in across the painted line between two bays and filling both, turned so the camera sees its rear three-quarter. It is a coupe-SUV: a long roofline sloping down into a short rear deck, slim split rear lights, a tall upright kidney grille, gloss black window trim, big dark alloy wheels. Its rear lights are lit and lay a weak red wash on the wet tarmac behind it. In the next bay to the right, parallel to the car and facing the same way, a cheap two-person dome tent in faded blue and grey, one corner sagging where a pole is bowed, a square of duct tape over a tear, the fabric darkened up one side where the rain has soaked it. Three or four metres of wet tarmac between them. Crossing the very bottom of the frame, close to the camera and soft, the corner of one more painted bay and a shallow puddle with rain rings spreading on it.

Action: standing in the gap on the tarmac, a late-forties white British man from the City of London: dark hair greying at the temples and slicked straight back with product, a well-fed face just beginning to jowl with a slight sheen on it, broken capillaries at the nose, pale indoor skin — not a smooth idealised leading-man face. He wears a quilted olive gilet zipped over a fine-gauge navy roll-neck, dark blue jeans with turn-ups, and polished tan suede loafers with no socks so a band of bare ankle shows. He is still turned back from pushing the car door shut behind him, his weight on one foot, his chin lifted, his mouth closed and his eyes aimed down at the other man.

Sitting on the wet ground at the mouth of the tent, a white British man of about fifty who has weathered to look older: grey-flecked stubble going on beard, deep lines, broken veins across wind-chapped cheeks, tired eyes with a wet shine — the wear plain on him and never smoothed into a handsome rough-sleeper. He wears a dark woollen beanie and a charity-shop coat a size too big with a broken zip, over a hoodie and more layers, everything grimed and softened by being lived in. He is mid-shift, one hand just out of his sleeve and pressed to the ground as he pushes himself straighter, his head turning up toward the standing man, his brows level.

Location: thick cold fog fills the whole car park. Six metres past the tent the fog closes into a flat unbroken wall of pale grey and fills the frame behind, above and to both sides of them. The painted bay lines and the wet tarmac fade out into that grey and are gone. There is nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people, no horizon and no sky. The light comes down through the fog from an overcast winter sky, so it arrives from every direction at once and nothing on the ground casts a shadow. The only other light in the picture is the car's rear lights.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, natural skin texture, fine grain in the shadows, muted cool-neutral colour and very low saturation. The black of the car is the darkest thing in the frame and the fog is the palest. Fine rain falls through the whole frame. The car is a working vehicle, not a clean one: rain-flecked, road film up the lower doors and dirt behind the wheel arches. Everything from the puddle in the foreground to the tent is sharp.

Constraints: no lettering or signage anywhere except the car's own badges. 16:9.

Thanks.
```


#### Variant A, round 1 — run 2026-09-08. The void and the car are solved. The people are not

**Three of round 1's seven faults are fixed and stay fixed:** the car reads as a real coupé-SUV
(it came back badged **X6**, which is the nearest car that actually exists — the silhouette
description did the work the model name could not), the fog erasure is total, and the tail lights
plus the foreground puddle give the frame its anchor and its front plane.

🔴 **The clause that failed is the one that mattered most, and it failed for a reason we already
have written down.** *"Not a smooth idealised leading-man face"* is a **negation**, and
[§27](../../google-flow/nano-banana-2.md) is the standing finding that **this engine cannot render
an absence** — given a negative it has nothing to substitute toward, so it draws its default and
ignores the clause. Round 1 got a catalogue face with no jowl, no capillaries and no sheen, which
is exactly the default. **Same mechanism as the 2008 numerals.**

**Round 2 converts every negation about a person into anatomy.** Not *"not idealised"* but *the
jaw softening under the chin, a thickened neck over the collar, pouches under the eyes, a red
flush across the nose.* The engine can draw all of those.

| Still wrong after round 1 | Cause | Round 2 |
|---|---|---|
| 🔴 **Both faces are catalogue-smooth** | negation, per above | positive anatomy, plus an explicit skin clause — pores, sebaceous sheen, under-eye shadow, facial asymmetry `[community]` |
| 🔴 **Four metres apart; no eyeline connects** | the prompt gave a distance and never said the eyes meet. The beat is *the two men lock eyes* | **two metres**, Tarquin standing over him, and the eyeline stated in both directions |
| **Everything on one plane across the middle** | [principle 1](../../cinematography/principles.md). The puddle gave a front plane and nothing links it to the middle | **Overlap**: Tarquin stands forward of the car and cuts across its rear wing; the tent's near guy line runs down into the puddle |
| **No rain in the air, again** | [§10](../../google-flow/nano-banana-2.md) — **weather underdelivers and needs magnitude and consequences shouted at it.** *"Fine rain"* is the opposite of shouting | heavy rain, named against the dark car, running off the flysheet, flattening hair |
| **Both men parked** | *mid-shift* is too weak a verb | one arrested physical action each, mid-stride and mid-flinch |
| **The tent is new** | wear was described on one corner only | dirt at the skirt, mud up one side, a frayed guy line, cardboard under the groundsheet |
| **Letterbox bars rendered into the picture** | never excluded | named in Constraints |

⚠️ **The badge is now a decision for Jack.** The frame says `X6`. The X8 is thin in the training
data and the model resolves it to the nearest real car; the *silhouette* is right either way.
Leaving it, because chasing the badge risks losing the shape that finally worked.

### 8b-fog · variant A2 — the fog limbo, faces fixed · **still** · written 2026-09-08, unrun

```prompt
A still photograph for a film. The job of this picture is to take a supermarket car park away and leave only the two men and the two things they own, two metres apart on the paint, looking at each other.

Camera: a 135mm lens at f/5.6, sixteen metres back, at the chest height of a standing person and level, framed slightly off-centre and not quite square to the bays, the way a photographer standing in the rain would actually hold it.

Composition: on the left, a large black BMW coupe-SUV, parked nose-in across the painted line between two bays and filling both, turned so the camera sees its rear three-quarter: a long roofline sloping down into a short rear deck, slim split rear lights, gloss black window trim, big dark alloy wheels. Its rear lights are lit and lay a red wash on the wet tarmac behind it. In the next bay to the right, parallel to the car and facing the same way, a cheap two-person dome tent in faded blue and grey, one corner sagging where a pole is bowed, a square of duct tape over a tear, the flysheet grey with old dirt along the skirt and a scuff of mud up one side, a frayed guy line running from its near corner down toward the camera, a flattened cardboard box pushed under the groundsheet where it meets the tarmac. The standing man is forward of the car and overlaps it, cutting across its rear wing. Crossing the very bottom of the frame, close to the camera and soft, the corner of one more painted bay and a shallow puddle with rain rings spreading across it, the red of the car's lights broken up in the water.

Action: standing over the seated man at two metres, a white British man of forty-seven from the City of London. His dark hair is greying at the temples and slicked straight back with product, thinning enough at the front that the scalp shows through when it is wet. His jaw has softened under the chin and his neck thickens over his collar; there are pouches under his eyes and a red flush of broken capillaries across his nose and both cheeks, and his forehead and nose carry an oily sheen. His skin is pale and indoor, with open pores across the nose and a day of stubble coming through unevenly. His face is slightly asymmetric, the left eye a little lower than the right. He wears a quilted olive gilet zipped over a fine-gauge navy roll-neck, dark blue jeans with turn-ups, and polished tan suede loafers with no socks so a band of bare ankle shows, the loafers dark with water. He has stopped mid-stride with one foot still ahead of the other and his weight not yet settled, his chin lifted, his mouth closed and his eyes aimed straight down into the seated man's eyes.

Sitting on the wet ground at the mouth of the tent, a white British man of fifty who looks sixty-five. Grey-flecked stubble is going on beard, patchy along the jaw. Deep lines cut across his forehead and out from the corners of his eyes; his cheeks are wind-chapped and broken-veined and raw at the edges; his lower eyelids sag away and his eyes are wet and red-rimmed. His nose has been broken and set crooked. His skin is weathered, coarse-grained and open-pored, and his hands are chapped and swollen at the knuckles with black in the creases. He wears a dark woollen beanie pulled low and soaked dark, and a charity-shop coat a size too big with a broken zip over a hoodie and more layers, everything greasy and shapeless from being lived in. He has flinched half upright, one hand out of his sleeve and flat on the wet tarmac taking his weight, the other still raised across his brow against the rain, his head turned up and his eyes meeting the standing man's.

Location: thick cold fog fills the whole car park. Six metres past the tent the fog closes into a flat unbroken wall of pale grey and fills the frame behind, above and to both sides of them. The painted bay lines and the wet tarmac fade out into that grey and are gone. There is nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people, no horizon and no sky. The light comes down through the fog from an overcast winter sky, so it arrives from every direction at once and nothing on the ground casts a shadow. The only other light in the picture is the car's rear lights.

Weather: it is raining hard, not drizzling. The rain is visible as streaks across the black of the car, it is running in threads off the tent's flysheet and dripping from its edge, both men's hair and shoulders are wet through, and the water is standing in sheets on the tarmac.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, natural skin texture throughout, fine grain in the shadows, muted cool-neutral colour and very low saturation. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches. Everything from the puddle in the foreground to the tent is sharp.

Constraints: no lettering or signage anywhere except the car's own badges. Fill the whole frame with the photograph, with no black bars, no letterbox borders and no white margin of any kind. 16:9.

Thanks.
```

🔑 **The one habit to keep from this round:** when a person comes back generic, **look for a
negation in the prompt before assuming the engine ignored you.** Every *"not a…"*, *"never…"*,
*"no…"* about a body or a face is a clause the model cannot act on. Say what the face has, not
what it lacks.


#### 🔴 Why the men shift — audited 2026-09-08, and the prompt WAS fighting the canon

**Jack asked the right question.** Two causes, and only one of them is the prompt.

**Cause 1 — structural, and it is the bigger one. Nothing is attached, so identity is redrawn
every run.** [§12](../../google-flow/nano-banana-2.md): a Character binds to a face; prose does
not. Prose can hold **wardrobe, wear and posture**; it has no mechanism for *the same man twice*.
Every run from a bare prompt is a fresh draw of a person who merely satisfies the adjectives.

🔴 **And for Tarquin specifically this is a documented, already-paid-for failure.**
[`characters/tarquin.md` §@Tarquin-new](./characters/tarquin.md) exists **because the wardrobe
would not survive a generation**: across four rounds of `8b(i)`, casting `@Tarquin` and describing
the outfit, attaching a clothing reference, or saying nothing at all **all returned an olive
leather bomber over a printed graphic t-shirt.** The conclusion recorded then was that *the
wardrobe needed to live in a Character's Body, not in a prompt.* **The no-attachment runs are
walking back into that.**

**Cause 2 — the prompt contradicted the character files.** Audited line by line. Nine faults.

| # | In the prompt | The canon | Verdict |
|---|---|---|---|
| 1 | *"tired eyes... wet and red-rimmed"*, *"lower eyelids sag away"* | **"kind, tired eyes with a wet shine"** | 🔴 **Contradiction.** *Kind* was deleted. Bob is the story's moral centre and his eyes are what carry it; red-rimmed and sagging makes him pitiable instead |
| 2 | *"He has flinched half upright... one hand raised across his brow"* | **"watchful but not aggressive; the stillness of someone used to being scrolled past"** | 🔴 **Contradiction.** A flinch is a startle. It turns him into a victim reacting, which is the read the whole story is built to prevent |
| 3 | *"His nose has been broken and set crooked"* | nothing | 🔴 **Invention.** Not in canon, and a specific bone-geometry instruction the model re-interprets every run |
| 4 | *"of fifty who looks sixty-five"* | "around fifty but weathered to look older" | 🔴 **Invention.** A hard number that pushes him past canon and moves the face |
| 5 | *"his face is slightly asymmetric, the left eye a little lower than the right"* | nothing | 🔴 **Invention.** Borrowed from an anti-slop article, not from Tarquin |
| 6 | *"broken capillaries across his nose and both cheeks"* | "broken capillaries at the nose" | ⚠️ **Drift.** Cheeks added |
| 7 | signet ring and watch absent | **"Signet ring and the old scuffed steel watch stay"** | 🔴 **Omission.** Two identity objects dropped |
| 8 | *"stopped mid-stride"* only | "chin slightly up, the resting expression of a man appraising and finding wanting" | 🔴 **Omission.** The one expression that is his |
| 9 | Merseyside absent; *"tasselled"* and *"cashmere"* dropped | both in the lock | ⚠️ **Drift** |

🔑 **And a third mechanism that is nobody's fault: more adjectives is not more consistency.** A
face specified twelve ways has twelve dials, each of which can land differently. **Fewer,
canonical markers vary less than many invented ones.** The A2 face descriptions were the longest
in this file and produced the least stable man in it.

#### What to do about it — Jack's call, and they are genuinely different films

| | Cast `@Tarquin-new` + `@Bob` | Keep it prose-only |
|---|---|---|
| **Identity across shots** | ✅ Holds. It is the only mechanism that does | 🔴 Fresh man every run |
| **Wardrobe** | ✅ Lives in the Character's Body — the reason `@Tarquin-new` was made | 🔴 The documented bomber-and-graphic-tee failure |
| **What the prompt may say** | 🔴 **No appearance at all** ([§19](../../google-flow/nano-banana-2.md)) — action and expression only | everything below |
| **Cost** | the face must be big enough in frame to bind, so the long-lens option closes | free, and Jack has asked for it |

**A3 below is the prose-only version with all nine faults corrected** — every invention removed,
every canon line restored, and the face cut back to the markers the character file actually
names. It will still draw a different man each run; it will draw **the right kind of man**, and
it will stop arguing with the files.

### 8b-fog · variant A3 — canon-corrected, prose only · **still** · written 2026-09-08, unrun

```prompt
A still photograph for a film. The job of this picture is to take a supermarket car park away and leave only the two men and the two things they own, two metres apart on the paint, looking at each other.

Camera: a 135mm lens at f/5.6, sixteen metres back, at the chest height of a standing person and level, framed slightly off-centre and not quite square to the bays, the way a photographer standing in the rain would actually hold it.

Composition: on the left, a large black BMW coupe-SUV, parked nose-in across the painted line between two bays and filling both, turned so the camera sees its rear three-quarter: a long roofline sloping down into a short rear deck, slim split rear lights, gloss black window trim, big dark alloy wheels. Its rear lights are lit and lay a red wash on the wet tarmac behind it. In the next bay to the right, parallel to the car and facing the same way, a cheap two-person dome tent in faded blue and grey, one corner sagging where a pole is bowed, a square of duct tape over a tear, the flysheet grey with old dirt along the skirt and a scuff of mud up one side, a frayed guy line running from its near corner down toward the camera, a flattened cardboard box pushed under the groundsheet where it meets the tarmac. The standing man is forward of the car and overlaps it, cutting across its rear wing. Crossing the very bottom of the frame, close to the camera and soft, the corner of one more painted bay and a shallow puddle with rain rings spreading across it, the red of the car's lights broken up in the water.

Action: standing over the seated man at two metres, a white British man in his late forties from the City of London. Dark hair greying at the temples, slicked straight back with product. A well-fed face that eats well and sleeps badly: a faint jowl beginning under the chin, a slight sheen on the forehead and nose, broken capillaries at the nose, pale indoor skin with open pores and a day of stubble coming through. He wears a quilted olive gilet zipped over a fine-gauge navy cashmere roll-neck, dark blue jeans with turn-ups, and polished tan suede tasselled loafers worn with no socks so a band of bare ankle shows, the loafers dark with water; a plain heavy signet ring on one hand and an old scuffed steel watch on the wrist. He has stopped mid-stride with one foot still ahead of the other and his weight not yet settled, his chin slightly up, his mouth closed, the resting expression of a man appraising the seated man and finding him wanting, his eyes aimed straight down into the seated man's eyes.

Sitting on the wet ground at the mouth of the tent, a white British man of around fifty from Merseyside, weathered to look older. Grey-flecked stubble going on beard, deep lines, kind and tired eyes with a wet shine, broken veins across wind-chapped cheeks, coarse open-pored skin, bare chapped hands. He wears a dark woollen beanie pulled low and soaked dark, and a charity-shop coat a size too big with a broken zip over a hoodie and more layers, everything grimed and softened by being lived in. He sits slightly hunched, one hand out of his sleeve and flat on the wet tarmac beside him, still and unhurried and watchful rather than startled, his head turned up and his eyes meeting the standing man's.

Location: thick cold fog fills the whole car park. Six metres past the tent the fog closes into a flat unbroken wall of pale grey and fills the frame behind, above and to both sides of them. The painted bay lines and the wet tarmac fade out into that grey and are gone. There is nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people, no horizon and no sky. The light comes down through the fog from an overcast winter sky, so it arrives from every direction at once and nothing on the ground casts a shadow. The only other light in the picture is the car's rear lights.

Weather: it is raining hard, not drizzling. The rain is visible as streaks across the black of the car, it is running in threads off the tent's flysheet and dripping from its edge, both men's hair and shoulders are wet through, and the water is standing in sheets on the tarmac.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, natural skin texture throughout, fine grain in the shadows, muted cool-neutral colour and very low saturation. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches. Everything from the puddle in the foreground to the tent is sharp.

Constraints: no lettering or signage anywhere except the car's own badges. Fill the whole frame with the photograph, with no black bars, no letterbox borders and no white margin of any kind. 16:9.

Thanks.
```

⬜ **If A3's man is still not Bob, the answer is not a longer description.** It is casting
`@Bob` and `@Tarquin-new` and deleting every appearance sentence above — the configuration
[§12](../../google-flow/nano-banana-2.md) calls *two sources agreeing*, and the only one that has
ever held a face in this film.


### 8b-fog · variant A4 — Characters cast, zero appearance · **still** · written 2026-09-08, unrun

🔑 **This is [§12](../../google-flow/nano-banana-2.md)'s *reliable configuration*: the Character
attached and nothing about the person in the text.** Jack's call, 2026-09-08, and it is the right
one — it is the only arrangement that has ever held a face in this film.

**Attach in this order and nothing else:** `@Tarquin-new` **first**, `@Bob` **second**, no
location reference. [§26](../../google-flow/nano-banana-2.md) records that both Characters go in
the earliest slots and that **each must be anchored to a named side of the frame** — Tarquin
**left**, Bob **right** — which is the one condition we believe carries two Characters in one
still.

**Everything about how they look is gone from the prompt.** No age, no build, no hair, no skin, no
wardrobe, no signet ring, no beanie. [§19](../../google-flow/nano-banana-2.md): a prose
re-description competes with the attachment and **the prose wins**, which is how `8c(i)` came back
in the wrong coat. `@Tarquin-new` exists precisely so the gilet lives in the Character's Body
rather than in a sentence — so the sentence must not mention it.

**What is left, and it is all that is allowed:** where each man is, what he is doing, and his face
written as **muscles rather than feelings** ([`image-prompting.md`](../../flow/image-prompting.md)
— *"AI does not understand feelings. It understands facial muscles."*). Note both faces are
written as **doing almost nothing**: the file's own warning is that reaching for a scowl produces
Angry Face, and restraint is what reads as real.

⚠️ **The one thing to watch:** wetness. *"Wet through"* is a condition and is allowed; *"soaked
beanie"* is wardrobe and is not. The rain is therefore described on the world and on the men only
as water running off them.

```prompt
A still photograph for a film. The job of this picture is to take a supermarket car park away and leave only the two men and the two things they own, two metres apart on the paint, looking at each other.

Camera: a 135mm lens at f/5.6, sixteen metres back, at the chest height of a standing person and level, framed slightly off-centre and not quite square to the bays, the way a photographer standing in the rain would actually hold it.

Composition: on the left, a large black BMW coupe-SUV, parked nose-in across the painted line between two bays and filling both, turned so the camera sees its rear three-quarter: a long roofline sloping down into a short rear deck, slim split rear lights, gloss black window trim, big dark alloy wheels. Its rear lights are lit and lay a red wash on the wet tarmac behind it. In the next bay to the right, parallel to the car and facing the same way, a cheap two-person dome tent in faded blue and grey, one corner sagging where a pole is bowed, a square of duct tape over a tear, the flysheet grey with old dirt along the skirt and a scuff of mud up one side, a frayed guy line running from its near corner down toward the camera, a flattened cardboard box pushed under the groundsheet where it meets the tarmac. Crossing the very bottom of the frame, close to the camera and soft, the corner of one more painted bay and a shallow puddle with rain rings spreading across it, the red of the car's lights broken up in the water.

Action: on the left of the frame, standing on the tarmac two metres from the tent and forward of the car so that he overlaps it and cuts across its rear wing, the man from the first character reference. He has stopped mid-stride with one foot still ahead of the other and his weight not yet settled, one hand loose at his side. His chin is slightly up, his brows relaxed and level, his mouth flat and closed, and his eyes are aimed steadily down at the seated man. His face is doing almost nothing.

On the right of the frame, sitting on the wet ground at the mouth of the tent, the man from the second character reference. He sits slightly hunched with his knees drawn up, one hand out of his sleeve and flat on the wet tarmac beside him taking a little of his weight. His head is turned up toward the standing man, his brows level, his mouth closed, his eyes soft and engaged and holding the other man's gaze without hurry. He is still, and unhurried, and not startled.

Neither man is posed and neither is aware of the camera. Rain is running off both of them.

Location: thick cold fog fills the whole car park. Six metres past the tent the fog closes into a flat unbroken wall of pale grey and fills the frame behind, above and to both sides of them. The painted bay lines and the wet tarmac fade out into that grey and are gone. There is nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people, no horizon and no sky. The light comes down through the fog from an overcast winter sky, so it arrives from every direction at once and nothing on the ground casts a shadow. The only other light in the picture is the car's rear lights.

Weather: it is raining hard, not drizzling. The rain is visible as streaks across the black of the car, it is running in threads off the tent's flysheet and dripping from its edge, and the water is standing in sheets on the tarmac.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, fine grain in the shadows, muted cool-neutral colour and very low saturation. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches. Everything from the puddle in the foreground to the tent is sharp.

Constraints: no lettering or signage anywhere except the car's own badges. Fill the whole frame with the photograph, with no black bars, no letterbox borders and no white margin of any kind. 16:9.

Thanks.
```

⚠️ **If the faces come back too small to bind,** the lever is distance, not words — come in from
sixteen metres to twelve and let the two men take more of the frame.
[§12](../../google-flow/nano-banana-2.md): no face in the shot, no likeness, and there is no
sentence that fixes that.

⬜ **If the wardrobe comes back wrong even with `@Tarquin-new` cast**, do not add the gilet to the
prompt — that is the `8c(i)` failure. Check the Character's Body instead.


### 8b-fog · variant A5 — the forty-metre void · **still** · written 2026-09-08, unrun

**Jack, 2026-09-08: the camera goes back out to where the accepted `8b` stands** — 200mm from
about forty metres, chest height, level. The fog stays; the men get small again.

🔴 **This distance changes what is possible, and two rules flip at once.**

**1. Nothing is attached, and that is now the correct choice rather than a compromise.**
[§12](../../google-flow/nano-banana-2.md): a Character binds to a **face**, and at forty metres
through rain there is no face to bind to. Casting `@Tarquin-new` and `@Bob` here would do nothing
at all — which is exactly what the accepted `8b` recorded: *"neither binds at this distance, so
the men are carried by the prose, not the Characters."* **This is §12's named narrow exception.**

**2. What the prose carries is SILHOUETTE, not appearance.** At forty metres the only legible
facts about a man are his **shape, his posture and how dark he is**. So the prompt gives each man
a stance and a mass and stops — no face, no features, no skin, and nothing that would be
invisible at this range anyway. That satisfies Jack's *"don't describe their appearance"* in
substance: **there is no face in this picture to describe.**

🔴 **And a physics fault in variants A–A4 that this distance exposes.** Those prompts put the fog
wall **six metres past the tent** — but a fog that erases everything past six metres also erases a
camera standing at **forty**. The two men would not be visible at all. **The fog's visibility has
to be set from the camera, not from the subject.**

**Corrected: visibility about fifty metres.** The men are *just* inside it, so they come through
pale, low-contrast and softened — which is the exact quality Jack accepted `8b` for in the first
place (*"the blurryness and rain makes it so the details don't matter and it looks really
cool"*) — and everything past them is gone. **The erasure and the softness are now the same
effect** instead of two clauses fighting.

🔑 **The foreground problem has a better answer here than a parked car.** With the rows deleted
there is nothing to look between, so the near tarmac carries it: **the painted bay lines run away
from the lens and converge toward the two men**, sharp and hard-edged at the bottom of the frame
and dissolving as they go. Leading lines, depth, and the only geometry left in the world — the
`the grid survives` idea from the alternates list, arriving for free.

```prompt
A still photograph for a film. The job of this picture is to take a supermarket car park away and leave only two small figures, a car and a tent, a long way off across an empty floor of wet paint.

Camera: a 200mm telephoto lens at f/4, standing on the wet tarmac about forty metres away, at the chest height of a standing person and perfectly level, not tilted. The long lens flattens what is left of the scene onto one plane. The framing is slightly off-centre and not quite square to the bays, the way a photographer standing out in the rain would actually hold it.

Composition: the two men and their two objects sit small in the middle band of the frame, taking up perhaps a third of its height. On the left, a large black BMW coupe-SUV, parked nose-in across the painted line between two bays and filling both, turned so the camera sees its rear three-quarter: a long roofline sloping down into a short rear deck, slim split rear lights, gloss black window trim, big dark alloy wheels. Its rear lights are lit and are the only colour in the picture, two small red marks with a soft red smear under them on the wet ground. In the next bay to the right, parallel to the car and facing the same way, a cheap two-person dome tent in faded blue and grey, one corner sagging where a pole is bowed, a square of duct tape over a tear, old dirt along its skirt. Running away from the camera along the bottom half of the frame, the painted white bay lines of the empty car park, hard-edged and bright with water where they are nearest the lens and converging toward the two men as they go, growing fainter until they dissolve.

Action: standing on the tarmac between the car and the tent, a man in dark trousers and a bulky sleeveless jacket over a dark top, upright, his weight on one foot as though he has just stopped walking, his head turned down toward the ground beside the tent. Sitting on the wet ground at the mouth of the tent, a much bulkier and lower shape, a man hunched inside several layers with his knees drawn up and a dark cap on his head, his head tilted up toward the standing man. Three or four metres of empty wet tarmac between them. Both figures are small and softened by the distance and by the rain in the air between them and the camera, and no detail of either face can be made out.

Location: thick cold fog fills the whole car park. Nothing is visible beyond about fifty metres, so the two men and their two objects sit right at the edge of what can still be seen, pale and low in contrast, and everything behind them is a flat unbroken wall of pale grey that fills the frame from side to side and top to bottom. The painted bay lines fade out into that grey a short way past the tent and are gone. There is nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people, no horizon and no sky. The light comes down through the fog from an overcast winter sky, so it arrives from every direction at once and nothing on the ground casts a shadow. The car's rear lights are the only other light in the picture.

Weather: it is raining hard, not drizzling. The rain is visible as fine streaks falling across the whole frame, standing in sheets on the tarmac and breaking the reflections up.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, fine grain in the shadows, muted cool-neutral colour and very low saturation, compressed perspective. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches. The bay lines nearest the camera are sharp.

Constraints: no lettering or signage anywhere except the car's own badges. Fill the whole frame with the photograph, with no black bars, no letterbox borders and no white margin of any kind. 16:9.

Thanks.
```

⚠️ **What this frame gives up.** At forty metres there is no eyeline, no expression and no
likeness — the whole argument is carried by two silhouettes and the space between them. That was
`8b`'s original bargain and Jack accepted it once already; it is worth knowing it is being made
again, because **A4 and A5 cannot both be the same shot.** One is a two-hander about faces, the
other is a two-hander about scale.


#### 🔴 A5 ran and the men changed again — and this time the cause is in the prompt, not the engine

**Two separate things are going on and they need separating.**

**1. The faces will change every run and no prompt can stop that.** Nothing is attached; identity
is a fresh draw. That is [§12](../../google-flow/nano-banana-2.md) and it is not a bug to fix.
**At forty metres it also does not matter** — no face is legible in A5's output, and nobody
watching can tell it is a different actor.

**2. What DID matter, and was my error: A5 threw away the canon wardrobe colours.** Reducing
Tarquin to *"dark trousers and a bulky sleeveless jacket over a dark top"* deleted four facts that
[`characters/tarquin.md`](./characters/tarquin.md) fixes — **olive** gilet, **navy** roll-neck,
**dark blue** jeans, **tan** loafers — and the run came back in **black trousers and black
boots**. That is not the engine drifting. That is the prompt no longer asking.

🔑 **The rule this settles: at forty metres, identity is CARRIED BY VALUE AND SHAPE, and those are
the things that must be locked.** A face is invisible at this range; a pale olive block above blue
legs above tan shoes is not. **Colour and silhouette are not "appearance" in the
[§19](../../google-flow/nano-banana-2.md) sense** — there is no Character attached for them to
argue with, and no face is being described. They are the only identity this shot has.

#### 🔴 Canon gap found: Bob's coat has no colour

[`characters/bob.md`](./characters/bob.md) fixes *"a charity-shop coat (a size wrong, zip
broken)"* and **never says what colour it is** — where Tarquin's file pins every garment. That is
why Bob's coat has come back a different shade in every round: **nothing has ever asked for one.**

The accepted frames have converged on **pale sand/khaki**, and A6 below locks that. ⬜ **A ruling
is owed** — if Jack agrees, the colour belongs in `bob.md`, not in one prompt.

### 8b-fog · variant A6 — forty metres, silhouette locked · **still** · written 2026-09-08, unrun

```prompt
A still photograph for a film. The job of this picture is to take a supermarket car park away and leave only two small figures, a car and a tent, a long way off across an empty floor of wet paint.

Camera: a 200mm telephoto lens at f/4, standing on the wet tarmac about forty metres away, at the chest height of a standing person and perfectly level, not tilted. The long lens flattens what is left of the scene onto one plane. The framing is slightly off-centre and not quite square to the bays, the way a photographer standing out in the rain would actually hold it.

Composition: the two men and their two objects sit small in the middle band of the frame, taking up perhaps a third of its height, and are grouped close together so that the standing man is only three metres from the tent and stands directly in front of the car, overlapping its rear wing. On the left, a large black BMW coupe-SUV, parked nose-in across the painted line between two bays and filling both, turned so the camera sees its rear three-quarter: a long roofline sloping down into a short rear deck, slim split rear lights, gloss black window trim, big dark alloy wheels. Its rear lights are lit and are the only colour in the picture apart from the men, two small red marks with a soft red smear under them on the wet ground. In the next bay to the right, parallel to the car and facing the same way, a cheap two-person dome tent in faded blue and grey, one corner sagging where a pole is bowed, a square of duct tape over a tear, old dirt along its skirt. Running away from the camera along the bottom half of the frame, the painted white bay lines of the empty car park, hard-edged and bright with water where they are nearest the lens and converging toward the two men as they go, growing fainter until they dissolve.

Action: standing on the tarmac between the car and the tent, a tall, narrow, upright man. He wears a pale olive sleeveless quilted gilet over a dark navy long-sleeved top, mid-blue denim jeans, and light tan shoes, and he is bare-headed with short dark hair. The olive of the gilet and the tan of the shoes are the two pale points on him. He stands with his weight on one foot as though he has just stopped walking, one hand loose at his side, his head turned down toward the seated man.

Sitting on the wet ground at the mouth of the tent, a much lower and much wider shape: a man bundled inside several layers, his knees drawn up and his arms in close, so that he reads as a rounded bulk rather than a body. He wears a pale sand-coloured oversized coat over darker layers underneath, and a dark knitted cap pulled down, and the cap is the darkest point on him. His head is tilted up toward the standing man.

Both figures are small and softened by the distance and by the rain in the air between them and the camera, and no detail of either face can be made out.

Location: thick cold fog fills the whole car park. Nothing is visible beyond about fifty metres, so the two men and their two objects sit right at the edge of what can still be seen, pale and low in contrast, and everything behind them is a flat unbroken wall of pale grey that fills the frame from side to side and top to bottom. The painted bay lines fade out into that grey a short way past the tent and are gone. There is nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people, no horizon and no sky. The light comes down through the fog from an overcast winter sky, so it arrives from every direction at once and nothing on the ground casts a shadow. The car's rear lights are the only other light in the picture.

Weather: it is raining hard, not drizzling. The rain is visible as fine streaks falling across the whole frame, standing in sheets on the tarmac and breaking the reflections up.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, fine grain in the shadows, muted cool-neutral colour and very low saturation, compressed perspective. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches. The bay lines nearest the camera are sharp.

Constraints: no lettering or signage anywhere except the car's own badges. Fill the whole frame with the photograph, with no black bars, no letterbox borders and no white margin of any kind. 16:9.

Thanks.
```

#### The choice that is actually on the table

**These two wants cannot both be satisfied in one frame, and no further rounds will change that.**

| | **Stay at forty metres** (A6) | **Come in to twelve** (A4, closer) |
|---|---|---|
| **The look Jack accepted `8b` for** | ✅ kept | 🔴 gone — details start to matter |
| **Same men across shots** | 🔴 never. Faces redraw every run | ✅ Characters bind and hold |
| **What identity rests on** | wardrobe colour and body shape | the actual face |
| **What the prompt may say** | colour and silhouette, no face | [§19](../../google-flow/nano-banana-2.md): nothing about them at all |

⬜ **There is a third route nobody has tried: generate close, accept, then use the accepted frame
as the reference for the wide.** It gets both — but it needs a reference image attached, which
Jack has ruled out for this set. Worth revisiting if A6 still is not right.


#### A6 ran — the register is proven. Two faults left, and both have known fixes

**Verdict: this is the best frame of the set and the fog limbo now works as a register.** The
void is total, the bay lines converge and carry the depth on their own, the red reflection under
the car is the only colour and it earns its place, and the rain is finally in the air. The
wardrobe held: olive, navy, blue, tan on Tarquin, sand and a dark cap on Bob. **Locking colour
and silhouette instead of faces was the right call and should stay.**

**Fault 1 — the faces are weird, and the fix is geometry, not description.**
[§18](../../google-flow/nano-banana-2.md) is the standing rule and it applies exactly here:
*"where a face does not need to be legible, hide it with the camera, never with a sentence."* At
forty metres a face is about fifteen pixels and the engine renders features into it anyway, which
is what produces the mush. Saying *"no detail of either face can be made out"* is a **rule**, and
§18 records that a stated rule does not bind — **only a physical occlusion the engine must honour
to draw the scene at all.**

So A7 gives each man an occluder and **describes the result**:

- **Tarquin's head is dropped far enough that the camera sees the crown of his skull**, not his
  face — the front of his face is aimed at the tarmac
- **Bob sits back inside the mouth of the tent** so the fabric arch cuts across above him and his
  head is inside its shade, with the cap pulled down over his brow

⚠️ **This is a real cost, stated plainly:** it removes the eyeline. The two men no longer look at
each other, and `8b`'s beat is *the two men lock eyes*. **At forty metres that beat was never
available** — it was not readable in A5 or A6 either. Better to stage the shot around what the
distance can actually carry.

**Fault 2 — the car grew a logo that is not BMW's.** Caused by the Constraints line: *"no
lettering… except the car's own badges"* **permits a badge without specifying one**, so the engine
invented a roundel. 🔴 **And "no badge" is the wrong fix** — [§27](../../google-flow/nano-banana-2.md),
an absence comes back inverted. **Describe what a badge actually looks like at forty metres:** a
small dark mark with no readable detail, above an unreadable yellow rectangle. That is true, it is
positive, and it gives the engine something to draw.

**Fault 3, mine, not Jack's:** the standing man is pressed against the car and the three-metre gap
reads as one. A7 puts clear tarmac between all three shapes so they read as three separate things
— the depth is already coming from the converging lines and does not need the overlap.

✅ **RESOLVED 2026-09-08, after a third matted run — it was neither.** The clause *"no black
bars, no letterbox borders"* is **an absence**, and [§27](../../google-flow/nano-banana-2.md)
says an absence comes back inverted. Three requests, three mattes. The prompts also opened *"a
still photograph **for a film**"*, which commissions a cinematic still, and a cinematic still has
bars. **Never negate the frame in prose — set the ratio in Flow's toggle.** Written up as
[§31](../../google-flow/nano-banana-2.md).

### 8b-fog · variant A7 — faces hidden by geometry · **still** · written 2026-09-08, unrun

```prompt
A still photograph for a film. The job of this picture is to take a supermarket car park away and leave only two small figures, a car and a tent, a long way off across an empty floor of wet paint.

Camera: a 200mm telephoto lens at f/4, standing on the wet tarmac about forty metres away, at the chest height of a standing person and perfectly level, not tilted. The long lens flattens what is left of the scene onto one plane. The framing is slightly off-centre and not quite square to the bays, the way a photographer standing out in the rain would actually hold it.

Composition: the two men and their two objects sit small in the middle band of the frame, taking up about a third of its height, spread across three clearly separated shapes with wet tarmac visible between each of them. On the left, a large black BMW coupe-SUV, parked nose-in across the painted line between two bays and filling both, turned so the camera sees its rear three-quarter: a long roofline sloping down into a short rear deck, slim split rear lights, gloss black window trim, big dark alloy wheels. Its rear lights are lit and are the only colour in the picture apart from the men, two small red marks with a soft red smear under them on the wet ground. At this distance its badge is a small dark mark on the tailgate with no readable detail in it, above a plain yellow rectangle with no readable detail in it either. Two metres of clear wet tarmac to the right of the car, then the standing man, then three metres more, then a cheap two-person dome tent pitched in the next bay, parallel to the car and facing the same way, one corner sagging where a pole is bowed, a square of duct tape over a tear, old dirt along its skirt. Running away from the camera along the bottom half of the frame, the painted white bay lines of the empty car park, hard-edged and bright with water where they are nearest the lens and converging toward the two men as they go, growing fainter until they dissolve.

Action: standing on the tarmac between the car and the tent, a tall, narrow, upright man. He wears a pale olive sleeveless quilted gilet over a dark navy long-sleeved top, mid-blue denim jeans, and light tan shoes, and he is bare-headed with short dark hair. The olive of the gilet and the tan of the shoes are the two pale points on him. He stands with his weight on one foot as though he has just stopped walking, one hand loose at his side, and his head is dropped so far toward the ground that the camera sees the crown of his skull and the top of his shoulders, with the whole front of his face aimed down at the tarmac and turned away from the lens.

Sitting on the wet ground just inside the mouth of the tent, set back under it so the arch of the tent fabric cuts across above him and his head sits inside its shade, a much lower and much wider shape: a man bundled inside several layers, his knees drawn up and his arms in close, so that he reads as a rounded bulk rather than a body. He wears a pale sand-coloured oversized coat over darker layers underneath, and a dark knitted cap pulled down low over his brow. His head is tilted up toward the standing man, and the shade of the tent and the pulled-down cap cover the upper half of it.

Location: thick cold fog fills the whole car park. Nothing is visible beyond about fifty metres, so the two men and their two objects sit right at the edge of what can still be seen, pale and low in contrast, and everything behind them is a flat unbroken wall of pale grey that fills the frame from side to side and top to bottom. The painted bay lines fade out into that grey a short way past the tent and are gone. There is nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people, no horizon and no sky. The light comes down through the fog from an overcast winter sky, so it arrives from every direction at once and nothing on the ground casts a shadow. The car's rear lights are the only other light in the picture.

Weather: it is raining hard, not drizzling. The rain is visible as fine streaks falling across the whole frame, standing in sheets on the tarmac and breaking the reflections up. There is enough rain in the forty metres of air between the camera and the two men to soften them.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, fine grain in the shadows, muted cool-neutral colour and very low saturation, compressed perspective. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches. The bay lines nearest the camera are sharp.

Constraints: every surface in the picture is plain, with no writing, no signage, no logos and no readable markings of any kind anywhere. Fill the whole frame with the photograph, with no black bars, no letterbox borders and no white margin of any kind. 16:9.

Thanks.
```

🔑 **The habit to keep:** two rounds in a row have been fixed by the same move — **stop stating a
rule and state the physical situation that makes the rule true.** *"No face can be made out"*
became *the crown of his skull faces the lens*; *"no badge"* became *a small dark mark with no
readable detail.* [§18](../../google-flow/nano-banana-2.md) and
[§27](../../google-flow/nano-banana-2.md) are the same finding wearing two hats.


#### ✅ A7 RAN, 2026-09-08 — and it is the best frame of the entire `8b-fog` set

**Jack ran the forty-metre A7 and it beat every variant after it.** Worth stating plainly because
it reverses the direction this section had been travelling: **A8/A9's elevated wide was a detour.**
A7 holds the beat, the men read as two people, the void is total, and — 🔑 **the rain is in the
air**, which A9's could not manage. That is [§32](../../google-flow/nano-banana-2.md) confirmed
from the other side: **A7 has a big black car and dark wet tarmac for the rain to fall against, so
the rain renders.** A9 deleted the dark and lost it. Same prompt clause, opposite result, and the
only difference is what was in the frame to see it against.

⬜ **Characters stay uncast, and at this distance that is the right call, not an oversight**
([§12](../../google-flow/nano-banana-2.md)) — forty metres gives no face to bind to. The
[A12 casting note](#-correction-2026-09-08-jack-a12-should-cast-the-characters-and-i-had-inherited-the-wrong-default)
applies only to the fourteen-metre design.

#### The four faults, and where the fix comes from

| Fault | Cause | Fix |
|---|---|---|
| 🔴 **The car rendered a full crisp roundel *and* model script on the tailgate** | The Constraints line said *"no lettering or signage anywhere **except the car's own badges**"* — **an explicit permission**, and the engine took it and over-delivered. Same shape as the A6 invented-roundel fault, one step along | Delete the exception. **State the optics instead:** at forty metres through rain a badge is too small to resolve, and there is no model script on the tailgate at all |
| 🔴 **The tent is too bright, too clean, too new** | Described from prose (*"faded blue and grey"*) rather than from the asset. [`characters/tent.md`](./characters/tent.md) is explicit — **the plate is the authority, match the plate not the words** | Described below from the plate itself |
| ⚠️ **The wet tarmac reads as one long mirror** | [The advert tell](../../google-flow/nano-banana-2.md#-advert-vocabulary-commissions-an-advert), verbatim: *"wet tarmac full of long mirror reflections"* is a detailing-advert brief. The plate does not look like that | **Break the reflections up** — water standing in irregular low places, dry-ish high places between |
| 🔴 **Letterbox bars, fourth run** | [§31](../../google-flow/nano-banana-2.md) — the negation *is* the cause, and *"a still photograph for a film"* commissions the matte | Both clauses deleted. Ratio set in Flow's toggle |

#### 🔑 The tent, read off the plate (`camera/reference/waitrose-car-park-plate.png`)

**This is the analysis Jack asked for, and it is materially different from what we have been
writing.** Every prompt in this section has said *"faded blue and grey"*, which is why we keep
getting a bright blue tent with a grey skirt. The plate shows something else:

- **The blue is only on the upper dome panels, and it is dusty and dark** — closer to slate or
  worn denim than to a bright tent blue. It is not a colour that draws the eye.
- **The rest of the tent — the whole lower body, the door panel and the sides — is pale
  grey-silver**, nearer bone or oyster than silver.
- 🔴 **It is dirty, and that is the single biggest difference.** Brown-grey mud staining runs along
  the bottom edge and streaks up the lower panels. The A7 tent is clean.
- **The fabric is slack, not taut** — sagging and wrinkled between the poles, the way a cheap tent
  that has been up for weeks actually sits.
- **The door is unzipped and open**, showing a dark interior with bedding as an unreadable dark
  mass inside. A7's is zipped shut, which loses the fact that a man lives in it.
- **Guy lines run out to the tarmac** — nothing can be pegged into a car park.

⚠️ **The open door is a real gain, not a detail.** [`frame.md`](../../cinematography/frame.md) —
*a frame-within-a-frame does narration's job for free.* A dark open doorway with belongings inside
is the only thing in the picture that says **this is a home**, which is the whole argument of the
scene. Add it.

#### What the cinematography file adds

- **Broken reflections are also a depth device, not only an anti-slop one.** Water pooled in the
  low places and not the high ones gives the empty floor *surface variation*, which is what stops
  a flat plane reading as a flat plane.
- **Worn paint, from the plate:** the bay lines are faded to nothing in the driven lanes and bright
  where cars do not run. Uniform crisp paint is the tell; the plate has neither.
- ✅ **Leading lines that arrive.** The measured claim is that viewers fixate longer when a line
  leads to a clear subject. A7 already does this — the bays converge on the two men. **Kept, and
  stated explicitly so it survives.**
- ⬜ **Kept as-is: the faces.** A7's geometry-hidden heads read fine at this size and Jack did not
  flag them. [Shot-craft's rule](../../../.claude/skills/shot-craft/SKILL.md) — change one thing at
  a time, and this round is already changing four.

#### On the research pass

The Nano Banana logo material yielded one usable rule — **quote on-image text, name the font and
the surface it sits on, keep it to 1–4 words** `[community]` — which is why the badge below is
handled as *optics* rather than as text: there is no string we want rendered.
🔴 **The wet-reflection search returned nothing citable** — SEO prompt farms restating each other,
which [`evidence.md`](../../cinematography/evidence.md) is explicit is not corroboration. **The
reflection fix below comes from our own plate and our own advert-vocabulary finding instead**, and
is the better source.

### 8b-fog · variant A7b — A7 with the badge, the tent and the ground fixed · **still** · written 2026-09-08, unrun

⚠️ **One call I made that Jack can cheaply reverse:** *"fix the car logo"* is read as **the badge
over-rendered and grew model script**, so the fix is to make it unresolvable at forty metres. If it
instead meant *the model designation is wrong* — the render reads X6, canon says X8 — that is a
readable-text problem we cannot reliably solve, and the answer is still to remove the script.

**Model: Nano Banana Pro. Nothing attached. Set 16:9 with Flow's landscape toggle.** Paste the
block below into the **prompt box on Flow's image surface**:

```prompt
Generate a still photograph. The job of this picture is to take a supermarket car park away and leave only two small figures, a car and a tent, a long way off across an empty floor of wet paint.

Camera: a 200mm telephoto lens at f/4, standing on the wet tarmac about forty metres away, at the chest height of a standing person and perfectly level, not tilted. The long lens flattens what is left of the scene onto one plane.

Composition: the two men and their two objects sit small in the middle band of the frame, taking up about a third of its height, grouped close together so the standing man is three metres from the tent and stands directly in front of the car, overlapping its rear wing. On the left, a large black BMW coupe-SUV, parked nose-in across the painted line between two bays and filling both, turned so the camera sees its rear three-quarter: a long roofline sloping down into a short rear deck, slim split rear lights, gloss black window trim, big dark alloy wheels. Its rear lights are lit, two small red marks with a soft red smear under them on the wet ground. In the next bay to the right, parallel to the car and facing the same way, a cheap two-person dome tent. Running away from the camera along the bottom half of the frame, the painted white bay lines of the empty car park, converging toward the two men as they go and growing fainter until they dissolve.

The car at this distance: the tailgate carries one small circular badge, too small for any shape inside it to be told apart, and the tailgate is otherwise completely bare — no model name, no lettering, no script, no numbers anywhere on the car. Below the badge sits a plain yellow rectangle with nothing written on it.

The tent: its upper dome panels are a dusty, darkened blue, closer to slate or worn denim than to a bright tent blue, and the whole lower body, the door panel and the sides are a pale grey-silver nearer bone than silver. Brown-grey mud staining runs along the bottom edge and streaks up the lower panels. The fabric is slack and wrinkled between its poles rather than taut, one corner sagging where a pole is bowed, a square of duct tape over a tear. Thin guy lines run out from its corners and lie slack on the tarmac, weighted rather than pegged. The door is unzipped and standing open, and inside it is dark, with bedding and belongings piled as an unreadable dark mass.

Action: standing on the tarmac between the car and the tent, a tall, narrow, upright man. He wears a pale olive sleeveless quilted gilet over a dark navy long-sleeved top, mid-blue denim jeans and light tan shoes, and he is bare-headed with short dark hair. He stands with his weight on one foot as though he has just stopped walking, one hand loose at his side, his head turned down toward the seated man.

Sitting on the wet ground at the mouth of the tent, a much lower and much wider shape: a man bundled inside several layers, knees drawn up and arms in close, so that he reads as a rounded bulk rather than a body. He wears a pale sand-coloured oversized coat over darker layers and a dark knitted cap pulled down, the cap the darkest point on him. His head is tilted up toward the standing man. Both figures are small and softened by the distance and by the rain in the air between them and the camera.

Ground: the tarmac is old and patched in mismatched shades of grey with tar seams between them. The painted bay lines are worn thin to almost nothing where cars have driven the lanes and bright and hard-edged where they have not. Rain has pooled in the low places and left the high places merely damp, so the reflections are broken into separate unequal patches with dull dry tarmac between them, never one continuous mirror.

Location: thick cold fog fills the whole car park. Nothing is visible beyond about fifty metres, so the two men and their two objects sit right at the edge of what can still be seen, pale and low in contrast, and everything behind them is a flat unbroken wall of pale grey filling the frame from side to side and top to bottom. The bay lines fade into that grey a short way past the tent and are gone. The light comes down through the fog from an overcast winter sky, arriving from every direction at once, and nothing on the ground casts a shadow.

Weather: it is raining hard, not drizzling. The rain is visible as fine streaks falling across the whole frame, clearest where it crosses the black of the car, and it breaks the surface of every pool of standing water.

Style: an unretouched documentary press photograph on Kodak Portra 400 at ISO 1600, fine grain in the shadows, muted cool-neutral colour and very low saturation, compressed perspective. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches. The bay lines nearest the camera are sharp.

Constraints: no writing, no signage, no logos, no numbers and no readable markings of any kind on any surface anywhere in the picture. Nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop fronts, no lamp posts, no trees, no fences, no other people, no horizon and no sky.

Thanks.
```

#### A7b ran, 2026-09-08 — the tent fix landed hard. Two faults left and NEITHER should be re-prompted

**Verdict: the best frame of the set and close to shippable.** The tent is transformed — muted
slate-blue dome, bone-grey body, and real mud streaking up the lower panels. **It reads as lived-in
rather than as a product**, which is what every previous round failed at. Reading the colour off
the plate instead of off our own prose is the whole reason, and
[`characters/tent.md`](./characters/tent.md) now carries it so it stops recurring. The rain is
excellent — better than A7's — and it dimples every pool.

#### 🔴 The letterbox: my §31 fix FAILED, and the finding needs downgrading

**Both clauses were deleted — the negation *and* "for a film" — and the bars came back anyway.**
Fifth consecutive matte. §31's causal claim is therefore **not supported**; it stands only as
"don't negate the frame", which is good practice for other reasons.

🔑 **New hypothesis, with evidence, and it points away from the prompt entirely.** The
**`waitrose-car-park-plate`** — banked weeks ago, from a completely different prompt — **has the
same black bars with the same thin white inner line.** And every image we have been reviewing is
~1240×695, an odd non-round size: **these are screenshot crops of Flow's viewer, not downloaded
originals.** A Flow download is 2K.

⬜ **The test is free and takes a minute: download the original from Flow and look at its
dimensions.** If it is 1920×1080 with no bars, we have spent five rounds of prompt engineering on
Flow's UI chrome. **Nobody should write another clause about bars until that check is done.**

#### 🔴 The badge got worse, and the cause is a rule we did not have

The roundel came back **crisp**, with **"X6" script** beside it — more legible than before, despite
a constraint line banning all lettering and an explicit optics sentence saying the badge is too
small to resolve.

🔑 **Naming a marque renders its badging, and no downstream constraint subtracts it.** *"A large
black BMW coupe-SUV"* carries the roundel and the model script inside the prior; the ban arrives
later and loses. This is [§27](../../google-flow/nano-banana-2.md)'s shape again — **you cannot
subtract, you can only substitute** — and it now has a marque-specific case.

⚠️ **And it confirms the ambiguous read from last round: the render says X6, canon says X8.** So
"fix the logo" was about the model designation. **We cannot fix that in Flow.** Rendering "X8" is
readable text on a small foreshortened surface, which is the least reliable thing the engine does,
and it fights the no-lettering rule everywhere else in the frame.

**The options, honestly, cheapest first:**

1. ✅ **Paint it out.** It is one small dark patch on a still. Free, exact, thirty seconds, and it
   is the [ffmpeg/exact lane](../../video-fx/hybrid-method.md) doing what that lane is for.
2. **Turn the car further away from camera** so the tailgate foreshortens out of legibility —
   costs a round, changes the composition Jack has already accepted.
3. **Drop "BMW" and describe the body only** — risks the silhouette, and the standing instruction
   is to name the marque. Not recommended.

🔴 **Do not spend another generation on it.** The frame is otherwise right, and re-rolling risks
the tent we just won.

#### Two smaller misses, one of them mine

- ⚠️ **The tarmac is still one mirror, and that clause was my fault.** I asked for *"the high
  places merely damp… never one continuous mirror"* in the same prompt as *"raining hard, not
  drizzling."* **In hard rain nothing stays dry.** The physics did not close, so the engine kept
  the stronger claim — which is exactly [§32](../../google-flow/nano-banana-2.md) firing on our own
  writing. **If broken reflections are wanted, the weather has to be "after the rain", not "during
  it."** That is a real choice, not a phrasing fix.
- ⬜ **The tent door did not open.** Bob is sitting where the door is, so the dark interior and the
  bedding are behind him. Worth one attempt at moving him a foot to the side of the opening rather
  than in front of it — but only bundled with something else, never on its own.

### 8b-fog — the clip · **video** · ✅ **RAN AND ACCEPTED 2026-09-08**

✅ **Jack: *"that worked."*** First-time pass. **The configuration that did it, for reuse:**
**Omni Flash · Frames tab · the accepted still as frame 0 · no Character, no Ingredients ·
camera locked in the prompt · one silhouette-scale change as the only human motion · ~105 words.**

🔑 **Three things this confirms, and all three were predictions rather than guesses:**
the [tab rule](../../google-flow/omni-flash.md#-the-tab-rule) — staging is what this shot could not
survive losing, so Frames was right and Ingredients would have redrawn both men; the
[hybrid ruling](../../video-fx/hybrid-method.md) — **the camera stayed locked and the frame
survived intact**, where a camera move is the instruction most likely to have redrawn the tent; and
**a silhouette beat carries at forty metres where a facial one cannot.**

⬜ **The reflection risk did not fire** — but the motion was deliberately kept tiny and above the
waterline, so this is not evidence the failure is not real. Still `n=1` against, and still worth
respecting on the next clip.

#### 🔴 Answer 1: yes to the push-in, no to asking Flow for it

**The zoom is the right instinct and it is the one move an eight-second clip means something
with** — [shot-craft](../../../.claude/skills/shot-craft/SKILL.md): *a push-in means narrowing
attention toward a realisation.* But it must not be asked of Omni Flash.

**[`hybrid-method.md`](../../video-fx/hybrid-method.md) §2, ruled 2026-08-26 — the world moves and
the camera moves, so this is the hybrid row:**

| Does the world move? | Does the camera move? | Build |
|---|---|---|
| **yes** (rain) | **yes** (the push) | 🟢 **Omni Flash locked, then move the camera in post** |

🔑 **The reason is specific and it protects this exact frame.** Veo/Omni's expensive failure is
**regeneration, and camera *translation* is what fires it** — measured on GPOM plant-room, clean at
0–4s and visibly broken by 6s. **We have just spent four rounds getting this tent right. A camera
move is the one instruction most likely to redraw it.** Locked, the bug cannot fire; the push is
then a scale-and-crop on real pixels — rigid, exactly eased, any length, free, instantly re-triable.

⬜ **Even if it were done in Flow, push-in is the safe direction** — it crops into pixels it already
has, where a pull-back must invent new world on all four edges every frame. Not needed here, but
worth knowing the asymmetry.

#### ⚠️ A push-in has to arrive at something, and two men staring is not something

*"Put something at the end of the push worth arriving at."* A held stare with nothing changing is
**pushing on nothing**, and the move will read as decoration.

🔑 **The payoff chosen, and why it is this one: the standing man's shoulders drop very slightly on
an exhale, near the end.** It is the whole beat — the man with everything, deflating — and
critically **it is a silhouette change, not a facial expression.** At forty metres a face carries
nothing and a silhouette carries everything; this section has proved that four times. It also stays
inside the near-static budget the Frames tab needs.

#### 🔴 Answer 2: no Characters, and no Ingredients either — this is a Frames shot

**[The tab rule](../../google-flow/omni-flash.md#-the-tab-rule) asks one question: what can this
shot not survive losing?** The answer is **the staging** — the corrected tent, the car, the fog, the
geography. → **Frames.**

Three independent reasons Characters are wrong here:

- **[§12](../../google-flow/nano-banana-2.md) — a Character binds to a face, and forty metres has
  no face to bind to.** Same reason A7 was cast prose-only.
- 🔴 **Characters live on Ingredients, and [Ingredients re-renders every person from scratch](../../google-flow/omni-flash.md#-ingredients-re-renders-faces--it-will-not-hold-an-unnamed-person).**
  It treats the image as *material*, not as pixels to continue. **It would redraw both men — which
  is precisely how we would lose the frame we are trying to keep.**
- **[`flow-prompt`](../../../.claude/skills/flow-prompt/SKILL.md) rule 2 — when animating a still,
  describe the motion ONLY.** The image already carries subject, scene and style; re-describing
  makes it regenerate instead of animate.

**And the prompt shape follows the tab, not the shot:** in Frames the image *is* frame 0, so the
prompt is cut to motion, timing and audio. **An itemised preservation list is the right medicine
for the wrong tab** and invites the drift it was meant to prevent.

⬜ **Flagging one Veo-only capability rather than switching silently:** Veo 3.1 takes a first *and*
last frame, and the same still in both slots is the strongest lock that exists. **Not used** — the
standing preference is Omni Flash, and [`hybrid-method.md`](../../video-fx/hybrid-method.md)'s rule
is never to pin an `endImage`, which morphs. A near-static Frames clip does not need it.

#### 🔴 The top risk in this specific clip, and it is not the men

**The bottom third of A7b is a mirror** — the car, the bay lines and both figures reflected in
standing water. [Omni's one observed reflection failure](../../google-flow/omni-flash.md#-moving-objects-inside-a-reflection--one-observed-failure-and-the-mechanism-is-here)
is exactly this: a reflection is **geometry twice over**, and the engine must hold where a thing is,
where its mirror image lands, and how both move, every frame, with no world model.

⚠️ `n=1`, so it is a flag not a law — **but it argues for keeping the motion tiny and above the
waterline**, which is what the shoulder-drop does. **Do not add anything that moves in the lower
third.** The independent 2026 tell-list names *"mirror/reflection breakdowns"* among the twelve most
consistent AI-video tells `[community]`, which is weak corroboration of a mechanism we had already
measured.

#### Anti-slop, video edition — what is new versus the stills work

A fresh pass, and most of it is post-production rather than prompt `[community]`:

- ⚠️ **"Unnaturally smooth motion"** is a named tell. The counter is a **10–15% speed ramp in
  Premiere** — not a prompt change. Cheap, worth trying on the finished clip.
- ✅ **Film grain at 10–15% opacity** over the finished clip counters the too-clean look. We already
  carry grain in the still's stock; this is the motion equivalent.
- ✅ **"Lock lighting to one source, avoid mixed lighting descriptions, use slower moves, shorter
  clips"** to prevent temporal flicker. All four are already house practice — the fog gives one
  omnidirectional source and there is nothing to mix.
- ⬜ **"Repeating texture tiling"** — a real risk with continuous rain over eight seconds. Nothing
  to do at the prompt; worth *looking* for on playback.
- 🔴 **Not adopted: "hand-morph frames"** is top of their list, and our hands are a few pixels at
  forty metres. Named so nobody spends a clause on it.

⚠️ **Prompt length is an [open conflict](../../google-flow/omni-flash.md#-open-conflict-how-long-should-an-omni-prompt-be)
in our own file and is not settled.** The resolution we use is *the axis is kind, not length*:
detail about **what the shot is** buys control; prescription about **how to achieve it** —
timecoded beats, frame-by-frame narration, physics explanations — buys nothing. The block below is
~105 words and every sentence is the first kind.

**Model: Omni Flash. Tab: Frames. Attach the accepted A7b still as the frame — nothing else, no
Character, no Ingredients.** Paste the block below into the **prompt box on the Frames tab**:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. The camera is locked off on a tripod and holds completely still for the whole shot.

Near the end of the shot the standing man's shoulders drop very slightly as he breathes out. Otherwise both men stay exactly where they are, holding each other's look, their feet still.

The rain keeps falling at the same rate across the whole frame and keeps breaking the surface of the standing water. Water runs down the back of the car.

Audio: heavy rain on wet tarmac, rain drumming on the car roof and on the tent fabric, and a light wind. No music and no voices.
```

#### The post move, in Premiere

**Scale the finished clip up by about 8–12% across its length with an ease in and an ease out**, so
it arrives on the shoulder drop rather than passing through it. Rigid, exact, free, and re-triable
without spending a generation.
⚠️ **Nothing ships unmeasured** — `scripts/delivery-qc.sh` before anything leaves the machine
([`delivery.md`](../../video-fx/delivery.md)).

### 8b-fog · variant A8 — the high wide, the grid survives · **still** · written 2026-09-08, unrun

**Jack picked the elevated very-wide, 2026-09-08.** The camera goes up and a long way back; the
car park becomes a **grid of white lines running out into the fog** with three small shapes in the
middle of it. This is the *"the grid survives"* option from the original alternates list, arriving
by accident and turning out to be the best of them.

**Two references, neither attached** — Jack's instruction is Characters only, no image:
the elevated wide sets the **camera**, and the `8a` aerial sets the **car position and the tent
colour** (mid-blue upper panels, grey-silver skirt, nose-in car in the bay immediately left of it,
tail lights lit, yellow plate).

#### 🔴 Two things this frame changes, from the cinematography file

**1. [Principle 21](../../cinematography/principles.md) — the overhead is the narrator's
position**, and it is exactly our narrator's gaze: detachment and dread rather than contempt.
**But it carries a named cost: from above, an empty space collapses into geometry and pattern
rather than absence** — it stops reading as *emptiness* and starts reading as *design*.

🔑 **The fix is already in the frame and must not be lost: the two men are the scale reference.**
[Principle 26](../../cinematography/principles.md) — a non-human subject has no legible size
without a known-size object beside it. **One human figure visibly tiny against the grid is the
single most load-bearing device available here.** Lose the figures and this becomes a wallpaper.

**2. [Gate 2](../../cinematography/principles.md) — a monumental frame needs a visible cost.**
This is a monumental composition: scale, symmetry, pattern. The cost is the seated man and his
tent, and they are the reason the picture is an indictment and not an architectural render.
**Both men must be legible as people, however small.**

#### Anti-slop for this frame specifically

The [toolkit's](../../google-flow/nano-banana-2.md#the-anti-slop-toolkit) four world-level
counters are *environmental imperfection, mid-action, off-centre and not-quite-level, and a
foreground occluder*. **Three of them have to work differently here:**

| Counter | How it lands in this frame |
|---|---|
| **Environmental imperfection** | 🔑 **The ground carries it.** A car park this size is never uniform: patched tarmac in mismatched shades, a drain grating, lines faded in the worn lanes and freshly repainted elsewhere, water pooling in the low spots instead of evenly. **This is the single biggest anti-slop lever in a frame with nothing else in it** |
| **Off-centre, not quite level** | the three shapes sit a little left of the centre line rather than dead on it |
| **Foreground occluder** | not available — there is nothing left to put in front. **The nearest bay lines take the job**: hard-edged, bright and large at the bottom edge, running away |
| **Mid-action** | at this scale, posture only — one figure upright, one low |

⚠️ **Characters attached as instructed, and it is worth being honest about what they will do:
nothing.** At this size a head is a few pixels; [§12](../../google-flow/nano-banana-2.md) — a
Character binds to a face and there is no face here. They are attached because Jack asked and they
cost nothing. **The identity that actually reads is colour and silhouette**, which is why the two
wardrobe locks stay in the text even though a Character is cast — a deliberate, flagged departure
from [§19](../../google-flow/nano-banana-2.md), taken because A5 proved that removing the colours
loses the wardrobe and A6 proved that stating them holds it.

```prompt
A still photograph for a film. The job of this picture is to show how small the whole argument is: an empty car park the size of a field, and three things standing in the middle of it.

Camera: a 35mm lens at f/8, raised about seven metres above the tarmac as if standing on the roof of a van, sixty metres back, tilted down just enough that the fog closes off the top third of the frame and the painted floor of the car park fills the rest. The framing sits a little left of true centre and is not quite level, the way a photographer holding a camera above their head in the rain would actually get it.

Composition: the whole frame below the fog is an empty car park seen from above and behind, a grid of white painted bay lines running away from the camera and out to both edges, the lines large and hard-edged and bright with water at the bottom of the frame and growing finer and fainter as they go until they dissolve into the fog. Small in the middle distance and a little left of centre, three shapes and nothing else: a large black BMW coupe-SUV parked nose-in and facing away from the camera so that only its back is seen, filling one bay, with a long roofline sloping down into a short rear deck and slim split rear lights lit red, a small dark badge on the tailgate with no readable detail in it and a plain yellow rectangle below it with no readable detail either, the red of its lights smeared down onto the wet tarmac behind it. In the bay immediately to its right, a cheap two-person dome tent with bright mid-blue upper panels and a grey-silver skirt and door, its door facing the same way the car does, one corner sagging where a pole is bowed, a square of duct tape over a tear. Between the car and the tent, standing on the painted line, one upright figure.

Action: the standing figure is a tall narrow man in a pale olive sleeveless quilted gilet over a dark navy top, mid-blue jeans and light tan shoes, bare-headed, standing still with his weight on one foot and his head turned down toward the tent. Sitting on the wet ground at the mouth of the tent, a much lower and wider shape: a man bundled inside several layers with his knees drawn up and his arms in close, in a pale sand-coloured oversized coat and a dark knitted cap, his head tilted up toward the standing man. Both are tiny in the frame, and it is the two of them that make the size of the car park readable at all.

Location: the tarmac is old and uneven and has been repaired many times, so it runs in mismatched patches of grey and near-black with tar seams between them, one iron drain grating set into it, the paint worn thin to nothing where cars have driven the lanes and clean and bright where they have not. Rain has pooled in the low places and left the high places merely wet, so the reflections are broken up and unequal instead of one mirror. Thick cold fog fills the whole space: nothing is visible beyond about eighty metres, and behind and above the three shapes there is a flat unbroken wall of pale grey filling the frame from side to side. There is nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people, no horizon and no sky. The light comes down through the fog from an overcast winter sky, so it arrives from every direction at once and nothing casts a shadow. The car's rear lights are the only colour in the picture.

Weather: it is raining hard, not drizzling. The rain is visible as fine streaks falling across the whole frame and as rings breaking the standing water.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, fine grain in the shadows, muted cool-neutral colour and very low saturation. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches. The painted lines nearest the camera are sharp.

Constraints: every surface in the picture is plain, with no writing, no signage, no logos and no readable markings of any kind anywhere. Fill the whole frame with the photograph, with no black bars, no letterbox borders and no white margin of any kind. 16:9.

Thanks.
```

⬜ **The letterbox bars have now survived three runs of the same constraint.** Treat it as **Flow's
own output framing until proven otherwise** and stop spending prompt words on it — one deliberate
check would settle it.


#### 🔴 The car has parked inside one bay for eight runs, and the clause has been wrong every time

**Canon is explicit and it is the argument, not a detail.**
[`assembly.md`](./assembly.md): *"8a — The X8 swinging in beside the tent, **across two bays**."*
[`shot-list.md`](./shot-list.md): *"the rhyme is the painted line: **one man inside one bay, one
car across two**."* A man is allowed one bay; the car takes two and nobody stops it. **If the car
parks neatly, the picture loses its joke and its indictment in the same stroke.**

**Every prompt in this file has said the same thing:** *"parked nose-in across the painted line
between two bays and filling both."* **Eight runs, eight neatly parked cars.** That is not bad
luck — it is [§18](../../google-flow/nano-banana-2.md) again, in its third costume:

> *stating a constraint does not bind; stating its physical consequence does.*

**"Across two bays" is a rule about parking.** The engine has an enormous trained prior for *car
in a parking bay* and a vanishing one for *car straddling a line*, so it renders the prior and
drops the clause. 🔑 **The fix is to stop describing the parking and describe the LINE:**

- the painted line **runs underneath the car**, disappearing at its front and reappearing behind it
- the car's body is **centred on the line**, not between two of them
- **the wheels on one side are in one bay and the wheels on the other side are in the next**
- the two bays it occupies are **the only ones a car could not park in**

All four are things a picture contains. None of them is an instruction about behaviour.

⚠️ **One change only this round.** The rest of A8 is reproduced word for word so the variable is
known. **The tent is the next candidate** — it came back a bright saturated blue where canon says
*faded blue and grey*, and it is now the loudest thing in a frame whose whole point is that
nothing is loud. Left alone deliberately until the car is settled.

⬜ **If the line still will not run under the car, the fallback is an angle, not a longer
sentence:** park it **twenty degrees off the bay lines** so it cuts across them diagonally. A
diagonal car in a rectilinear grid is unmistakable at any size, the engine has a prior for it
(*badly parked car*), and it makes the same point — arguably harder. It is a departure from the
`8a` aerial, so it is Jack's call, not a silent substitution.

### 8b-fog · variant A9 — the car takes two bays · **still** · written 2026-09-08, unrun

```prompt
A still photograph for a film. The job of this picture is to show how small the whole argument is: an empty car park the size of a field, and three things standing in the middle of it.

Camera: a 35mm lens at f/8, raised about seven metres above the tarmac as if standing on the roof of a van, sixty metres back, tilted down just enough that the fog closes off the top third of the frame and the painted floor of the car park fills the rest. The framing sits a little left of true centre and is not quite level, the way a photographer holding a camera above their head in the rain would actually get it.

Composition: the whole frame below the fog is an empty car park seen from above and behind, a grid of white painted bay lines running away from the camera and out to both edges, the lines large and hard-edged and bright with water at the bottom of the frame and growing finer and fainter as they go until they dissolve into the fog. Small in the middle distance and a little left of centre, three shapes and nothing else.

The first is a large black BMW coupe-SUV, seen from directly behind, with a long roofline sloping down into a short rear deck and slim split rear lights lit red, a small dark badge on the tailgate with no readable detail in it and a plain yellow rectangle below it with no readable detail either, the red of its lights smeared down onto the wet tarmac behind it. One of the white painted bay lines runs directly underneath this car: the line comes up the tarmac toward the camera, disappears beneath the middle of the car at its rear bumper, and reappears from under its nose on the far side. The car's body is centred on that line rather than between two lines, so its left wheels stand in one bay and its right wheels stand in the next one, and the two bays it is sitting in are the only two in the whole car park that another car could not use.

The second is a cheap two-person dome tent with faded mid-blue upper panels and a worn grey-silver skirt and door, pitched inside a single bay two bays to the right of the car and squarely between that bay's two painted lines, its door facing the same way the car does, one corner sagging where a pole is bowed, a square of duct tape over a tear, old dirt along its skirt.

The third is a man standing upright on the tarmac between them.

Action: the standing man is tall and narrow, in a pale olive sleeveless quilted gilet over a dark navy top, mid-blue jeans and light tan shoes, bare-headed, standing still with his weight on one foot and his head turned down toward the tent. Sitting on the wet ground at the mouth of the tent, a much lower and wider shape: a man bundled inside several layers with his knees drawn up and his arms in close, in a pale sand-coloured oversized coat and a dark knitted cap, his head tilted up toward the standing man. Both are tiny in the frame, and it is the two of them that make the size of the car park readable at all.

Location: the tarmac is old and uneven and has been repaired many times, so it runs in mismatched patches of grey and near-black with tar seams between them, one iron drain grating set into it, the paint worn thin to nothing where cars have driven the lanes and clean and bright where they have not. Rain has pooled in the low places and left the high places merely wet, so the reflections are broken up and unequal instead of one mirror. Thick cold fog fills the whole space: nothing is visible beyond about eighty metres, and behind and above the three shapes there is a flat unbroken wall of pale grey filling the frame from side to side. There is nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people, no horizon and no sky. The light comes down through the fog from an overcast winter sky, so it arrives from every direction at once and nothing casts a shadow. The car's rear lights are the only colour in the picture.

Weather: it is raining hard, not drizzling. The rain is visible as fine streaks falling across the whole frame and as rings breaking the standing water.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, fine grain in the shadows, muted cool-neutral colour and very low saturation. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches. The painted lines nearest the camera are sharp.

Constraints: every surface in the picture is plain, with no writing, no signage, no logos and no readable markings of any kind anywhere. Fill the whole frame with the photograph, with no black bars, no letterbox borders and no white margin of any kind. 16:9.

Thanks.
```

🔑 **Third confirmation of the same rule, and it is now the most reliable habit in this file:**
*"no face can be made out"* became **the crown of his skull faces the lens**; *"no badge"* became
**a small dark mark with no readable detail**; *"parked across two bays"* becomes **the line runs
under the car and out the other side**. **Describe the picture, never the rule.**

#### A9 ran — the register holds, and six faults came back. Four are known findings firing again

**What landed, and must not be touched.** The tarmac is the win: mismatched patched greys, tar
seams, a real iron drain grating, paint worn thin in the driven lanes and bright where it is not,
water pooled unequally instead of one mirror. **That clause is the single biggest anti-slop lever
in a frame with nothing else in it and it delivered exactly as designed.** The fog erasure is
total, the void is complete, the badge came back unreadable ([§27](../../google-flow/nano-banana-2.md)
worked), and the wardrobe held again on colour and silhouette alone.

⬜ **And one accidental improvement worth keeping: the men came back bigger than "tiny".** They
are legible as two people at a glance. [Gate 2](../../cinematography/principles.md) wants exactly
that — a monumental frame needs a visible cost, and the cost has to be readable. **Do not ask for
them smaller.** The clause *"both are tiny in the frame"* is dropped in A10 for this reason.

| # | Fault | Cause | Fix in A10 |
|---|---|---|---|
| 1 | 🔴 **The camera is nowhere near seven metres up** — it reads about two to three, and the tilt is barely there | [§28](../../google-flow/nano-banana-2.md), **second confirmation**: a stated camera elevation is consistently under-delivered in both height and tilt. 🔑 **And this prompt sabotaged its own number** — *"as if standing on the roof of a van"* describes a vantage of about **two and a half metres**, which is precisely what came back. The analogy overruled the figure | Delete the number *and* the van. **Describe what a high camera sees**: the car's roof panel as a flat shape, the tent dome as a full oval, the men seen from above their heads with shoulders wider than feet |
| 2 | 🔴 **Dead-centre one-point perspective, perfectly level** — the vanishing point sits on the centre line and the grid fans out symmetrically | *"a little left of true centre and not quite level"* is an **adjective**, and this is the fourth run to prove adjectives do not bind. Symmetry is [the named slop tell](../../google-flow/nano-banana-2.md#the-anti-slop-toolkit) and the model's resting state | **Turn the camera off-square to the bays.** Two-point perspective is a geometric fact the engine must honour to draw the floor at all: lines running diagonally, a vanishing point stated as sitting to the right |
| 3 | 🔴 **The tent is the brightest and most saturated object in the picture** — a vivid stock-photo blue that beats the rear lights outright | The prompt contained a straight contradiction: *"faded mid-blue"* + *"very low saturation"* + *"the car's rear lights are the only colour."* Given an unresolvable brief the engine picks its strongest prior, and its prior for "dome tent" is a bright blue one | State it **comparatively and physically**: the blue has weathered chalky until it is closer to grey than blue, and the red of the lights is the most saturated thing in the frame *by a wide margin* |
| 4 | 🔴 **No rain in the air at all** — the ground is wet, nothing is falling | 🔑 **The physics does not close, so the engine closed it.** [§20](../../google-flow/nano-banana-2.md): a weather instruction is a physics claim. Rain is only legible against something darker than it is, and this frame is a pale grey wall from edge to edge. Confirmed against the photography literature — backlighting or a dark background is the *only* way rain reads, and against a bright even sky there is no separation to see. Same shape as [§17](../../google-flow/nano-banana-2.md) (light streaks need lights) | **Give the rain the only dark thing in the frame.** Streaks legible where they cross the black flank and roof of the car and the black patches of wet tarmac; rings and bounce-spray on the standing water; and say plainly that against the fog it disappears into the grey |
| 5 | 🔴 **Letterbox bars, third run running** | **This is [§27](../../google-flow/nano-banana-2.md) and we did not see it.** *"no black bars, no letterbox borders and no white margin of any kind"* is **an absence**, and an absence comes back inverted. Three requests, three mattes. 🔑 **And the prompt cued the matte in its own first five words** — *"A still photograph **for a film**"*, plus *"documentary press photograph"* and *"16:9"*, is a cinematic-still brief, and a cinematic still has bars | **Delete the negation entirely and delete *"for a film"*.** Stop asking for the absence and stop commissioning the thing. Set the ratio with Flow's own landscape toggle, not with prose |
| 6 | ⚠️ **The car is parked neatly inside one bay** — the whole point of A9 was lost | [§21](../../google-flow/nano-banana-2.md) — a multi-part change to one object loses. The straddle was **four dependent clauses** (line comes up, disappears at the bumper, reappears at the nose, body centred on the line) describing a relationship that is nearly invisible from directly behind anyway | **Take the fallback this file already wrote.** See the ruling below |

#### 🔴 One thing in A10 is Jack's call, not a silent substitution: the car is now parked at an angle

The A8 entry pre-authorised this exactly — *"if the line still will not run under the car, the
fallback is an angle, not a longer sentence: park it twenty degrees off the bay lines so it cuts
across them diagonally."* The line has now failed once, so the fallback is live. **A diagonal car
in a rectilinear grid is unmistakable at any size, the engine has a strong prior for it (*badly
parked car*), and it makes the same point harder.** It also kills fault 2 for free.

⚠️ **The cost, stated:** it is a departure from the `8a` aerial, where the car is nose-in and
square. **To swap back**, replace the angle sentence with A9's straddle paragraph and lose nothing
else.

⚠️ **A10 bundles six changes, deliberately, against the one-change-at-a-time rule.** Five of them
are mechanical faults with independent, evidenced fixes and running them singly costs five rounds.
**The one genuinely unproven change is the oblique camera** (fault 2) — if A10 comes back worse
rather than differently wrong, that is the clause to revert first.

### 8b-fog · variant A10 — the high oblique · **still** · written 2026-09-08, unrun

🔑 **Nothing attached. Set the aspect ratio with Flow's landscape toggle — the prompt no longer
asks for it, on purpose.** Paste the block below into the **prompt box on Flow's image surface**:

```prompt
A still photograph. The job of this picture is to show how small the whole argument is: an empty car park the size of a field, and three things standing in the middle of it.

Camera: a 35mm lens at f/8, looking down from a hydraulic access platform raised high above the tarmac, about sixty metres back from the three shapes. It is high enough that everything is seen substantially from above: the whole roof panel and rear window of the car read as flat shapes, the dome of the tent is a full rounded oval rather than a hump on the horizon, and the two men are seen from above the level of their heads, so that their shoulders are the widest part of them and their feet sit almost directly beneath. The painted floor of the car park fills the whole frame below the top quarter, and the fog closes off that top quarter.

Composition: the camera is turned so that it is not square to the parking bays. The white painted bay lines run away diagonally across the frame instead of straight back toward the camera, converging on a vanishing point well over toward the right-hand side, and a second set of painted lines crosses them at an angle, so the floor reads as an oblique grid rather than a symmetrical fan. The lines are large and hard-edged and bright with standing water at the bottom left of the frame, and grow finer and fainter as they run back until they dissolve. The three shapes sit together in the middle distance, below and to the left of the centre of the frame, with clear empty tarmac between each of them.

The first is a large black BMW coupe-SUV, seen from above and behind: a long roofline sloping down into a short rear deck, slim split rear lights lit red, a small dark badge on the tailgate with no readable detail in it and a plain yellow rectangle below it with no readable detail either, and the red of its lights laid down onto the wet tarmac behind it. It has been left at an angle of about twenty degrees to the painted lines, so that its body cuts across them diagonally rather than lying along them: its nose sits inside one bay and its tail swings out over the line into the next, and the painted lines run underneath it and out the other side. It is the only thing in the whole car park that is not square to the grid.

The second is a cheap two-person dome tent, pitched squarely inside a single bay and lying neatly along that bay's painted lines the way the car does not, two bays further to the right of the car. Its upper panels are a blue that has weathered chalky and pale until it is closer to grey than to blue, and its skirt and door are a dirty worn grey-silver. One corner sags where a pole is bowed, a square of duct tape covers a tear, and old dirt runs along its skirt.

The third is a man standing upright on the tarmac between the two.

Action: the standing man is tall and narrow, in a pale olive sleeveless quilted gilet over a dark navy top, mid-blue jeans and light tan shoes, bare-headed, standing still with his weight on one foot and his head turned down toward the tent. Sitting on the wet ground at the mouth of the tent, a much lower and wider shape: a man bundled inside several layers with his knees drawn up and his arms in close, in a pale sand-coloured oversized coat and a dark knitted cap, his head tilted up toward the standing man. It is the two of them that make the size of the car park readable at all.

Location: the tarmac is old and uneven and has been repaired many times, so it runs in mismatched patches of grey and near-black with tar seams between them, one iron drain grating set into it, the paint worn thin to nothing where cars have driven the lanes and clean and bright where they have not. Rain has pooled in the low places and left the high places merely wet, so the reflections are broken up and unequal instead of one mirror. Thick cold fog fills the whole space: nothing is visible beyond about eighty metres, and behind and above the three shapes there is a flat unbroken wall of pale grey filling the frame from side to side. There is nothing in the fog and nothing beyond it: no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people, no horizon and no sky. The light comes down through the fog from an overcast winter sky, so it arrives from every direction at once and nothing casts a shadow.

Colour: the red of the car's rear lights is the most saturated thing in the picture by a wide margin, and the wet red smear it lays on the tarmac is the second. Every other colour in the frame — the tent, both men's clothes, the tarmac, the fog — is muted, chalky and close to grey.

Weather: it is raining hard. The rain is legible only where it has something dark to fall against: fine bright streaks crossing the black flank and roof of the car and crossing the near-black patches of wet tarmac, rings breaking every pool of standing water, and a fine spray bouncing back up off the ground. Where it falls against the pale fog it simply disappears into the grey.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, fine grain in the shadows, muted cool-neutral colour and very low saturation. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches. The painted lines nearest the camera are sharp.

Constraints: every surface in the picture is plain, with no writing, no signage, no logos and no readable markings of any kind anywhere.

Thanks.
```

### 🔴 Step back — A9 is a good picture of the wrong subject

**A10 fixes six mechanical faults in a frame whose subject is already wrong.** Worth saying
plainly before anyone spends another generation on it.

**Jack's brief, at the top of this section:** *"films pause on only one aspect, **the important
parts**, everything else disappears, like we are in the characters' aetherial subconscious."*

**The important parts are the two men.** A9 is 95% car park floor and about 2% men. The device was
*everything else disappears* — and the car park is the most present, most detailed, most lovingly
elaborated thing in the frame. **The erasure is fighting the composition:** every painted line
rendered is the car park refusing to go, and A9's sixty-word tarmac clause is us helping it stay.

⚠️ **This is a repeat of a lesson the house already paid for.**
[`symptoms.md`](../../cinematography/symptoms.md): *"The empty room isn't creepy, it's just empty —
shot too wide or too high; from a distance human proportions stop being legible and it reads as
geometry. **This is exactly what we found the hard way on the GPOM `vantage` cut.**"* The A8 entry
quoted [principle 21](../../cinematography/principles.md)'s warning — *from above, an empty space
collapses into geometry and pattern rather than absence* — and then walked into it anyway.

**And the staging is a diagram, not a photograph.** Car left, man centre, tent right, all
equidistant, all the same size, on one lateral line. That is an *illustration of a concept*.
[`symptoms.md`](../../cinematography/symptoms.md) has both halves of it: *"I don't know where to
look — everything at the same visual weight"* and *"scale contrast is stated rather than
composed."*

⬜ **Not a case for scrapping the elevated wide.** It is a real frame and it may well earn a place
in the film as the *establisher* — the car park as a field, before we care about anyone. **It is
just not 8b.** Keep A9/A10 as `8a-alt`, and let 8b be about the men.

### 8b-fog · variant A11 — two erasures meeting on the subject · **still** · written 2026-09-08, unrun

🔑 **The idea worth keeping from this whole run.** Jack asked for *everything else disappears*, and
so far we have used exactly one device to do it: fog, which only erases what is **far**. **Add the
second: a long lens wide open erases what is near.** Fog takes the world behind them, focus takes
the ground in front of them, and the two erasures **meet on the two men**, who become the only
solid objects in existence. That is Jack's *"pause on only the important parts"* rendered
optically as well as atmospherically — and it is a stronger read of the brief than either the
18m two-shot or the 60m wide.

**And the physics closes** — which by [§32](../../google-flow/nano-banana-2.md) is the thing to
check before writing any effect. A 135mm at f/2.8 focused fourteen metres out throws ground at
five or six metres into genuine blur while holding all three shapes, which sit within a couple of
metres of each other. Variant C tried shallow focus at ground level and had to delete the whole
car park to make room for it; from up here the blur is free.

#### The gates

1. **Job:** the frame where the world stops existing and two men are left in it. `8b` says *two
   men, three metres apart, in a car park.* A9 says *look how big the car park is.* **This says
   there is no car park** — only the paint under their feet, and the two of them.
2. **Visible cost:** Bob is now the **nearest, largest and only sharp-focused** thing in the
   picture. In A9 he was a fleck. [Gate 2](../../cinematography/principles.md) is not satisfied by
   a cost being technically present.
3. **Light:** overcast through fog, omnidirectional, shadowless — with one motivated exception,
   the car's own rear lights. 🔑 **Tarquin's machine is the only thing in the frame making light,
   and Bob has none.**

#### The three design changes under it

| Change | Why |
|---|---|
| 🔑 **Staged in depth, not across the frame** — Bob nearest and lowest, Tarquin standing beyond him, the car furthest and receding | Kills the diagram. The eye now arrives **cost first, then the man, then the machine**, which is the argument in order. [Principle 5](../../cinematography/principles.md) — the composition steps instead of listing |
| **The camera is high but CLOSE** | [Principle 21](../../cinematography/principles.md)'s overhead is the narrator's position and it is exactly Jack's *"aetherial subconscious"* — but it *"must earn scale separately."* Close keeps the people legible; the grid running away behind them keeps the scale |
| ⚠️ **The tarmac clause is cut from sixty words to twelve** | Google's own guidance: *"a focused short prompt can beat a long prompt with competing styles or viewpoints."* A9 ran to seven hundred words and the longest, most vivid passage in it described **the thing we are trying to erase.** Enough imperfection to beat slop, no more |

⚠️ **The car stays at twenty degrees across the bays** (the A8 fallback, taken in A10) — still
Jack's call, still a departure from the `8a` aerial. Swap back by restoring A9's straddle paragraph.

Nothing attached. **Set 16:9 with Flow's landscape toggle — the prompt does not ask for it, on
purpose ([§31](../../google-flow/nano-banana-2.md)).** Paste the block below into the **prompt box
on Flow's image surface**:

```prompt
Generate a still photograph. The job of this picture is to leave two men and the two things they own as the only solid objects in the world, with everything nearer than them and everything further than them dissolved away.

Camera: a 135mm lens wide open at f/2.8, about fourteen metres back and raised well above the men so the camera looks down on them at a shallow angle. It is high enough that the tops of their heads and shoulders are seen, the dome of the tent reads as a full rounded oval rather than a hump, and part of the car's roof panel is visible as a flat shape. The wet ground fills the entire frame from edge to edge: there is no horizon and no sky anywhere in the picture. The camera is turned so it is not square to the parking bays, and the painted lines run away diagonally across the frame rather than straight back.

Focus: the plane of focus falls exactly on the seated man. He, the standing man, the tent and the car are all sharp. The wet tarmac in the near third of the frame, closest to the camera, is thrown completely out of focus, so that the painted lines crossing it are soft bands of white with no edges and the rain rings on the standing water are soft discs.

Composition: the three shapes are staged one behind the other going away from the camera, not side by side. Nearest and lowest, on the right, a man sitting on the wet ground at the mouth of a cheap two-person dome tent, seen from above and close enough to be the largest thing in the frame. Beyond him and to the left, a second man standing upright on the tarmac, smaller. Further away again and further left, a large black car parked at an angle across the painted lines. Clear empty tarmac lies between all three.

Action: the seated man is bundled inside several layers with his knees drawn up and his arms held in close, in a pale sand-coloured oversized coat and a dark knitted cap, one hand pressed to the wet ground as he pushes himself straighter, his head tilted up toward the standing man. The standing man is tall and narrow, in a pale olive sleeveless quilted gilet over a dark navy top, mid-blue jeans and light tan shoes, bare-headed, his weight on one foot and his head turned down toward the seated man. Neither is posed; both are caught mid-movement.

The tent is pitched squarely inside one bay and lies neatly along that bay's painted lines. Its upper panels are a blue that has weathered chalky and pale until it is closer to grey than to blue, its skirt and door a dirty worn grey-silver; one corner sags where a pole is bowed and a square of duct tape covers a tear.

The car is a large black BMW coupe-SUV with a long roofline sloping into a short rear deck and slim split rear lights lit red, a small dark badge on the tailgate with no readable detail in it. It has been left at about twenty degrees to the painted lines so its body cuts across them diagonally, its nose in one bay and its tail swung out over the line into the next, and it is the only thing in the picture that is not square to the grid.

Location: old patched tarmac in mismatched shades of grey with tar seams between them, water pooled unevenly in the low places. Thick cold fog fills everything: a short way past the car the painted lines pale out into flat grey and stop, and there is nothing beyond them at all — no other vehicles, no buildings, no shop front, no lamp posts, no trees, no fence, no other people. The light comes down through the fog from an overcast winter sky so it arrives from every direction at once, and nothing casts a shadow.

Colour: the red of the car's rear lights is the most saturated thing in the picture by a wide margin, and the wet red it lays on the tarmac behind it is the second. Every other colour — the tent, both men's clothes, the ground, the fog — is muted, chalky and close to grey.

Weather: it is raining hard. The rain is legible only where it has something dark to fall against: fine bright streaks crossing the black of the car and the dark layers both men are wearing, and rings breaking every pool of standing water. Where it falls against the pale fog it disappears into the grey.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, natural skin texture, fine grain in the shadows, muted cool-neutral colour and very low saturation. The black of the car is the darkest thing in the frame and the fog is the palest. The car is a working vehicle: rain-flecked, road film up the lower doors, dirt behind the wheel arches.

Constraints: every surface in the picture is plain, with no writing, no signage, no logos and no readable markings of any kind anywhere.

Thanks.
```

### 8b-fog · variant A12 — written clean · **still** · written 2026-09-08, unrun

**Jack, 2026-09-08: *"make the prompt forget everything else."*** Taken as: rebuild it from
nothing, keep only what is evidenced, and let the erasure win. **A9 ran to seven hundred words and
its longest, most loving passage described the car park — the thing the shot exists to delete.**
A12 is **430**, and every clause that survived had to earn it.

#### What the web pass changed, and the one place it contradicts us

Two fresh sources, September 2026. Both independently confirm findings this file arrived at the
hard way, which is worth noting as corroboration rather than news:

| Finding | Source | What it changes here |
|---|---|---|
| 🔑 **"Adjectives do not render."** Replace them with visual facts | [fal, Nano Banana Pro guide](https://fal.ai/learn/tools/nano-banana-pro-prompting-guide) `[community]` | **Independent confirmation of [§30](../../google-flow/nano-banana-2.md) and [§33](../../google-flow/nano-banana-2.md).** *"slightly off-centre"*, *"not quite level"*, *"faded"*, *"very low saturation"* are adjectives, and all four have now failed on this shot. **Every one is replaced by a placement or a comparison** |
| **Pro reasons about composition before it paints, and *"the more it knows about the job, the sharper its planning step gets"*** | fal `[community]` | The job sentence at the top is not decoration — it feeds the planning pass. Keep it, make it concrete |
| ✅ **Negatives work as a scoped constraint block, not as floating absences** — *"no other props, no hands, no visible brand logos, no harsh specular hotspots on the metal"* | fal `[community]` | Squares with [§27](../../google-flow/nano-banana-2.md)/[§31](../../google-flow/nano-banana-2.md): an absence fails as a *subject*, works as a terminal constraint attached to named things. A9's markings constraint did work. **Kept, in the last slot, and nowhere else** |
| ⚠️ **"One or two imperfection words per prompt. Three max. Over-correction makes images look intentionally degraded"** | [usetoolai](https://usetoolai.com/blog/how-to-create-ai-images-that-dont-look-like-ai-2026) `[community]` | 🔴 **This contradicts our own measured finding** that A9's tarmac clause was the single biggest anti-slop lever in the frame — and it demonstrably was. **Not adopted wholesale.** A9 stacked twelve-plus imperfections; A12 carries four. Middle taken deliberately, and the claim is logged as `[community]`, unverified against our own work |
| **AI images give themselves away by being too clean, too evenly lit, too symmetrical, too composed** | usetoolai `[community]` | Nothing new — it is [the toolkit](../../google-flow/nano-banana-2.md#the-anti-slop-toolkit) restated |

🔴 **One piece of their advice is on our never-cite list and is NOT used:** both slop guides
recommend prompting for *"rule of thirds"*.
[`evidence.md`](../../cinematography/evidence.md) grades the rule of thirds as perception **myth**
— no supporting study, and the eye's measured priority is motion, faces, and lines that lead to a
subject. **We compose to that instead**, which is why the bay lines in A12 converge on a person
rather than on an empty vanishing point, as they did in A9.

#### What the cinematography file put in the frame

Four devices from [`frame.md`](../../cinematography/frame.md), none of which were in any earlier variant:

- 🔑 **Status cues, deliberately inverted.** *"Closer to camera, larger in frame reads dominant;
  smaller, further, turned away reads subordinate."* So **Bob is nearest and largest and Tarquin
  is smaller and further** — the composition gives Bob the standing the world does not, and the
  argument is made in geometry before a caption exists. This is the whole shot.
- **Short-siding.** *"Subject near the edge looking away from the open space signals isolation and
  unease."* Bob sits hard to the right with the entire empty half of the car park opening away to
  his left. It manufactures the isolation and the negative space in one move.
- **Leading lines that arrive somewhere.** Measured: viewers fixate longer when a line leads to a
  clear subject than when it leads to nothing. A9's lines converged on empty tarmac. **A12's
  converge on Bob.**
- **Centrifugal, not centripetal.** One blurred painted line runs out through the bottom edge, so
  the frame implies a world past itself instead of reading as a diorama.

⚠️ **The "not quite level" ask is deleted rather than rewritten** — four failures, and shot-craft's
rule is that the fix which works most often is *removing* a clause. The oblique grid carries the
asymmetry on its own.

Nothing attached. **Model: Nano Banana Pro. Set 16:9 with Flow's landscape toggle — the prompt
does not ask for a ratio, on purpose ([§31](../../google-flow/nano-banana-2.md)).** Paste the block
below into the **prompt box on Flow's image surface**:

```prompt
Generate a still photograph. The job of this picture: two men and the two things they own are the only solid objects left in the world. Everything nearer than them and everything further than them has dissolved away.

Staging — three shapes on wet tarmac, arranged one behind the other going away from the camera, never side by side. Nearest, largest, and sitting close to the right-hand edge of the frame: a man on the ground at the mouth of a small dome tent, knees drawn up, one bare hand pressed to the wet ground as he pushes himself straighter, head tilted up. He wears a sand-coloured oversized coat and a dark knitted cap. Behind him and to the left, clearly smaller: a man standing, tall and narrow, in a pale olive quilted gilet over a dark navy top, mid-blue jeans and light tan shoes, bare-headed, his weight on one foot and his head turned down toward the seated man. Furthest away and smallest of the three: a large black BMW coupe-SUV with slim rear lights lit red, left at about twenty degrees across the painted bay lines so that its body cuts diagonally over them while the tent and the lines lie square. The entire left half of the frame is empty wet tarmac opening away from the seated man into nothing.

Camera: a 135mm lens at f/2.8, fourteen metres back, raised high enough to look down on all three — the tops of both men's heads and shoulders are visible, the tent reads as a full rounded oval rather than a hump, and part of the car's roof panel shows as a flat shape. The camera is turned off-square to the parking bays, so the white painted lines run away diagonally across the frame and converge on the seated man.

Focus: the plane of focus falls on the seated man. He, the standing man, the tent and the car are all sharp. The tarmac in the nearest third of the frame is thrown completely out of focus, so the painted lines crossing it are soft white bands with no edges and the rain rings on the standing water are soft discs. One of those blurred lines runs out through the bottom edge of the frame.

Setting: thick cold fog. A short way past the car the painted lines pale out into flat grey and stop. There is no horizon and no sky anywhere in the picture.

Light: overcast daylight coming down through the fog from above, arriving from every direction at once, so nothing casts a shadow. The car's rear lights are the only thing in the frame making light of its own.

Colour: cool and close to grey throughout. The red of the car's rear lights, and the wet red it lays on the tarmac behind it, is the most saturated thing in the picture by a wide margin; nothing else comes near it. The tent's blue has weathered chalky until it is nearer grey than blue.

Weather: hard rain, legible only where it has something dark to fall against — fine bright streaks crossing the black of the car and the dark layers both men are wearing, and rings breaking every pool of standing water. Where it falls against the pale fog it disappears into the grey.

Style: an unretouched documentary press photograph on Kodak Portra 400 at ISO 1600. Natural skin texture. Fine film grain living in the shadows. The black of the car is the darkest thing in the frame and the fog is the palest.

Wear: the tarmac is patched in mismatched greys with water pooled unevenly in the low places; one corner of the tent sags where a pole is bowed; the car is rain-flecked with road film up its lower doors.

Constraints: no writing, no signage and no logos on any surface anywhere in the picture. No other vehicles, no buildings, no shop fronts, no lamp posts, no trees, no fences and no other people, either in the frame or in the fog.

Thanks.
```

#### 🔴 Correction, 2026-09-08 (Jack): A12 should cast the Characters, and I had inherited the wrong default

**A12 was written prose-only, carrying "nothing attached" forward from A5–A9. That reasoning does
not survive A12's own geometry.** *"Nothing attached"* was correct for the forty- and sixty-metre
variants for one reason only — [§12](../../google-flow/nano-banana-2.md), **a Character binds to a
face, and at that distance there is no face to bind to.** A12 puts Bob **nearest, largest and in
the plane of focus at fourteen metres.** That is the biggest, sharpest face in any variant of this
shot, and it is exactly the condition §12 requires.

**So A12 is the first frame since A4 where casting actually does something — and the version below
is the one to run.**

⚠️ **And the prose-only A12 carries the `8c(i)` bug in it.** *"a sand-coloured oversized coat and a
dark knitted cap"*, *"a pale olive quilted gilet over a dark navy top"* —
[§19](../../google-flow/nano-banana-2.md): with a Character cast, appearance prose **competes with
the attachment and the prose wins.** `@Tarquin-new` exists for precisely this reason: across four
rounds of `8b(i)`, describing the outfit returned an olive **leather bomber over a printed graphic
tee** every time. **The gilet has to live in the Character's Body, not in a sentence.** Every
appearance clause is deleted below.

⬜ **No contradiction with A6, though it looks like one.** A5 losing the wardrobe and A6 holding it
by naming the colours were both **prose-only at forty metres, with no Character attached** — in
that regime the words are the only lever there is. With `@Tarquin-new` cast the wardrobe has a
better home. Different regime, not a reversal.

| | Attach | Reason |
|---|---|---|
| **Slot 1** | `@Bob` | 🔑 **Changed from A4's order, deliberately.** [§4](../../google-flow/nano-banana-2.md) — what must survive goes in the earliest slot, and in A12 Bob is the focal point, the nearest shape and the largest face. A4 put Tarquin first because A4's Tarquin was the prominent one |
| **Slot 2** | `@Tarquin-new` | The leisure Character. **Not `@Tarquin`** — the gilet is in this one's Body |
| **Nothing else** | — | No location reference. The reference *is* the car park and the car park is what we are deleting |

✅ **[§26](../../google-flow/nano-banana-2.md)'s condition is met** — the one arrangement believed
to carry two Characters in one still is each anchored to a named side. A12 stages in depth, but it
also keeps canon's sides: **Bob right, Tarquin left.** Both are stated in the text below.

🔴 **One flag that gets worse in this frame, not better.** The
[2026-08-29 ruling](#12a--the-first-frame-of-the-vault) accepted that **`@Bob` is not the Bob of
the accepted `8c(i)` frame** — the best face in the film — and that we cast the existing Character
and take the break. **A12 makes Bob the largest face in the shot**, so that break is more visible
here than anywhere it has been ruled on before. Worth knowing before the credit is spent; the
ruling stands until Jack changes it.

### 8b-fog · variant A12-cast — the running version · **still** · written 2026-09-08, unrun

**Model: Nano Banana Pro. Attach `@Bob` first, `@Tarquin-new` second, no location reference. Set
16:9 with Flow's landscape toggle.** Paste the block below into the **prompt box on Flow's image
surface**:

```prompt
Generate a still photograph. The job of this picture: two men and the two things they own are the only solid objects left in the world. Everything nearer than them and everything further than them has dissolved away.

Staging — three shapes on wet tarmac, arranged one behind the other going away from the camera, never side by side. Nearest, largest, and sitting close to the right-hand edge of the frame: the man from the first character reference, on the ground at the mouth of a small dome tent. He sits slightly hunched with his knees drawn up and one bare hand flat on the wet ground beside him, taking a little of his weight as he pushes himself straighter. His head is turned up toward the standing man, his brows level, his mouth closed, his eyes steady and unhurried. He is not startled and he is not posed, and his face is doing almost nothing.

Behind him and to the left of the frame, standing on the tarmac and clearly smaller: the man from the second character reference. He has stopped mid-stride with his weight not yet settled and one hand loose at his side. His chin is slightly up, his brows relaxed, his mouth flat and closed, and his eyes are aimed down at the seated man. His face is doing almost nothing either. Neither man is aware of the camera, and rain is running off both of them.

Furthest away and smallest of the three: a large black BMW coupe-SUV with slim rear lights lit red, left at about twenty degrees across the painted bay lines so that its body cuts diagonally over them while the tent and the lines lie square. The entire left half of the frame is empty wet tarmac opening away from the seated man into nothing.

Camera: a 135mm lens at f/2.8, fourteen metres back, raised high enough to look down on all three — the tops of both men's heads and shoulders are visible, the tent reads as a full rounded oval rather than a hump, and part of the car's roof panel shows as a flat shape. The camera is turned off-square to the parking bays, so the white painted lines run away diagonally across the frame and converge on the seated man.

Focus: the plane of focus falls on the seated man's face. He, the standing man, the tent and the car are all sharp. The tarmac in the nearest third of the frame is thrown completely out of focus, so the painted lines crossing it are soft white bands with no edges and the rain rings on the standing water are soft discs. One of those blurred lines runs out through the bottom edge of the frame.

Setting: thick cold fog. A short way past the car the painted lines pale out into flat grey and stop. There is no horizon and no sky anywhere in the picture.

Light: overcast daylight coming down through the fog from above, arriving from every direction at once, so nothing casts a shadow. The car's rear lights are the only thing in the frame making light of its own.

Colour: cool and close to grey throughout. The red of the car's rear lights, and the wet red it lays on the tarmac behind it, is the most saturated thing in the picture by a wide margin; nothing else comes near it. The tent's blue has weathered chalky until it is nearer grey than blue.

Weather: hard rain, legible only where it has something dark to fall against — fine bright streaks crossing the black of the car, and rings breaking every pool of standing water. Where it falls against the pale fog it disappears into the grey.

Style: an unretouched documentary press photograph on Kodak Portra 400 at ISO 1600. Natural skin texture. Fine film grain living in the shadows. The black of the car is the darkest thing in the frame and the fog is the palest.

Wear: the tarmac is patched in mismatched greys with water pooled unevenly in the low places; one corner of the tent sags where a pole is bowed; the car is rain-flecked with road film up its lower doors.

Constraints: no writing, no signage and no logos on any surface anywhere in the picture. No other vehicles, no buildings, no shop fronts, no lamp posts, no trees, no fences and no other people, either in the frame or in the fog.

Thanks.
```

### 8b-fog · variant B — the black limbo · **still** · written 2026-09-08, unrun

⚠️ **This one changes the beat to night**, which scene 8 is not. Run it as a look test, not as a
replacement — and note [principle 11](../../cinematography/principles.md): uniform near-black
reads as a broken file, so the lit pool is doing structural work and must not be dimmed.

```prompt
A still photograph for a film. The job of this picture is to leave only the two men and the two things they own, standing in one pool of light with the world switched off around them.

Camera: a 135mm lens at f/5.6, eighteen metres back, at the chest height of a standing person and level, framed slightly off-centre and not quite square to the bays.

Composition: on the left, a large black BMW X8, parked nose-in across the painted line between two bays and filling both, turned so the camera sees its rear three-quarter. It is a coupe-SUV: a long roofline sloping down into a short rear deck, slim split rear lights, a tall upright kidney grille, gloss black window trim, big dark alloy wheels. In the next bay to the right, parallel to the car and facing the same way, a cheap two-person dome tent in faded blue and grey, one corner sagging where a pole is bowed, a square of duct tape over a tear. Three or four metres of wet tarmac between them. Crossing the very bottom of the frame, close and soft, the corner of one more painted bay and a shallow puddle with rain rings spreading on it.

Action: standing in the gap on the tarmac, a late-forties white British man from the City of London: dark hair greying at the temples and slicked straight back with product, a well-fed face just beginning to jowl with a slight sheen on it, broken capillaries at the nose, pale indoor skin — not a smooth idealised leading-man face. He wears a quilted olive gilet zipped over a fine-gauge navy roll-neck, dark blue jeans with turn-ups, and polished tan suede loafers with no socks so a band of bare ankle shows. He is still turned back from pushing the car door shut behind him, his weight on one foot, his chin lifted, his mouth closed and his eyes aimed down at the other man.

Sitting on the wet ground at the mouth of the tent, a white British man of about fifty who has weathered to look older: grey-flecked stubble going on beard, deep lines, broken veins across wind-chapped cheeks, tired eyes with a wet shine — the wear plain on him and never smoothed into a handsome rough-sleeper. He wears a dark woollen beanie and a charity-shop coat a size too big with a broken zip, over a hoodie and more layers, everything grimed and softened by being lived in. He is mid-shift, one hand just out of his sleeve and pressed to the ground as he pushes himself straighter, his head turning up toward the standing man, his brows level.

Location: night. A single sodium car park lamp stands just outside the top of the frame and slightly to the left, and it is the only light in the world. It throws one hard-edged oval of orange light onto the wet tarmac that reaches just past the tent and no further, wet reflections stretching from it toward the camera, and both men and both objects stand inside that oval with the tops of their heads and the roof of the car catching it hardest. Everything outside the oval falls off fast into complete black: no other vehicles, no buildings, no shop front, no other lamps, no trees, no fence, no other people, no horizon and no sky, only black. The car's rear lights are lit and are the one other point of colour, two small red bars deep in the dark.

Style: a documentary press photograph on Kodak Portra 400 pushed to ISO 3200, unretouched, natural skin texture, coarse grain living in the shadows, muted colour. The blacks are deep but not empty. Fine rain falls through the whole frame and is visible where it crosses the lamplight. The car is a working vehicle, not a clean one: rain-flecked, road film up the lower doors and dirt behind the wheel arches.

Constraints: no lettering or signage anywhere except the car's own badges. 16:9.

Thanks.
```

### 8b-fog · variant C — the shallow-focus dissolve · **still** · written 2026-09-08, unrun

🔴 **The riskiest of the three.** [§26](../../google-flow/nano-banana-2.md) records that
`out of focus` is **weakly obeyed and needs reinforcing** — round 1 of 8b ignored it outright and
only *"thrown completely out of focus so that it is a soft blur"* held. The phrasing below uses
that exact shape, twice, on purpose.

```prompt
A still photograph for a film. The job of this picture is to keep the whole car park in the frame and let the lens delete it, so that only the two men and the two things they own are solid and everything else is a smear of grey.

Camera: a 200mm lens wide open at f/2, eighteen metres back, at the chest height of a standing person and level, framed slightly off-centre and not quite square to the bays. The plane of focus is extremely narrow and falls exactly on the two men.

Composition: on the left, a large black BMW X8, parked nose-in across the painted line between two bays and filling both, turned so the camera sees its rear three-quarter. It is a coupe-SUV: a long roofline sloping down into a short rear deck, slim split rear lights, a tall upright kidney grille, gloss black window trim, big dark alloy wheels. Its rear lights are lit. In the next bay to the right, parallel to the car and facing the same way, a cheap two-person dome tent in faded blue and grey, one corner sagging where a pole is bowed, a square of duct tape over a tear. Three or four metres of wet tarmac between them.

Action: standing in the gap on the tarmac, a late-forties white British man from the City of London: dark hair greying at the temples and slicked straight back with product, a well-fed face just beginning to jowl with a slight sheen on it, broken capillaries at the nose, pale indoor skin — not a smooth idealised leading-man face. He wears a quilted olive gilet zipped over a fine-gauge navy roll-neck, dark blue jeans with turn-ups, and polished tan suede loafers with no socks so a band of bare ankle shows. He is still turned back from pushing the car door shut behind him, his weight on one foot, his chin lifted, his mouth closed and his eyes aimed down at the other man.

Sitting on the wet ground at the mouth of the tent, a white British man of about fifty who has weathered to look older: grey-flecked stubble going on beard, deep lines, broken veins across wind-chapped cheeks, tired eyes with a wet shine — the wear plain on him and never smoothed into a handsome rough-sleeper. He wears a dark woollen beanie and a charity-shop coat a size too big with a broken zip, over a hoodie and more layers, everything grimed and softened by being lived in. He is mid-shift, one hand just out of his sleeve and pressed to the ground as he pushes himself straighter, his head turning up toward the standing man, his brows level. Both men are sharp, and so are the car and the tent beside them.

Location: an ordinary British supermarket car park on a wet winter afternoon under an overcast sky, rows of small parked cars behind the two men and more rows in front of them. Every one of those rows is thrown completely out of focus so that it is a soft blur with no edges and no readable shape, dissolved into flat bands of grey and dull colour. In front of the two men, the roofs of the nearest parked cars cross the very bottom of the frame, also thrown completely out of focus so that they are a soft dark blur. The light comes from the overcast sky alone and nothing casts a shadow. The car's rear lights are the only other light in the picture.

Style: a documentary press photograph on Kodak Portra 400 at ISO 1600, unretouched, natural skin texture, fine grain in the shadows, muted cool-neutral colour and very low saturation. Fine rain falls through the whole frame. The car is a working vehicle, not a clean one: rain-flecked, road film up the lower doors and dirt behind the wheel arches.

Constraints: no lettering or signage anywhere except the car's own badges. 16:9.

Thanks.
```

⬜ **All three unrun.** 🔴 **Nothing is attached — no Character, no location reference, no image of
any kind** (Jack, 2026-09-08). Both men are carried entirely by prose lifted from
[`characters/tarquin.md`](./characters/tarquin.md) and [`characters/bob.md`](./characters/bob.md).

**This is [§12](../../google-flow/nano-banana-2.md)'s narrow exception, taken deliberately.**
[§19](../../google-flow/nano-banana-2.md) bans appearance prose *when a Character is cast*, because
the two sources argue and the prose wins. With nothing cast there is no argument, and prose is the
only lever there is — the same position `8b` was in at forty metres.

⚠️ **What it costs: likeness is not guaranteed between runs.** The wardrobe and the wear are locked
by the words; the *face* is a fresh draw every time. If a frame from this set is accepted and then
has to match its neighbours, that is the moment to cast the Characters — not before.

🔑 **The two clauses doing the anti-slop work are the ugly ones, and both come straight out of the
character files:** *"not a smooth idealised leading-man face"* and *"the wear named and never
smoothed into a handsome rough-sleeper."* Round 1 returned two stock actors precisely because
neither clause was in the prompt.

**Run A first**, then B, then C — one at a time, so the variable stays known.

---

## Scene 8 fog coverage — five angles on the accepted fog frame · written 2026-09-15

**Jack, 2026-09-15:** he attached the accepted fog two-shot plus the Characters and asked Flow for
*"different shots of this"*. Five frames came back and he likes all five. His ask: **describe each
angle, then write a proper prompt for each so the good version is made on purpose**, with the slop
taken out, for Nano Banana, using the cinematography toolkit.

**The beat these serve** (story discussion the same day, not yet canon): **Bob's panic.** The X8 is
the trigger, the fog is the inside of his head, and he breathes his way back. Dialogue is deferred.
Each spec below says which part of that beat its frame carries.

### The five frames as returned, read with `shot-craft`

| id | Angle | What is in it | Keep | Slop / fault to take out |
|---|---|---|---|---|
| **8f-low** | **Ground level**, a hand's height off the tarmac, wide lens, looking slightly up | Tarquin mid-stride, towering, centre-right. Bob at the tent mouth, right, knees up. X8 rear three-quarter, left, lights lit | Height puts us on Bob's ground. Tarquin's step is an unresolved moment | 🔴 **The hero splash**: a crown of droplets on the nearest puddle is a stock "rain" trope. **Bob faces the lens**, not either man |
| **8f-high** | **Raised wide**, about 8m up, looking down about 30° | The trio small in the middle of an endless bay grid dissolving into fog | The field of empty bays is the isolation | 🔴 **Dead-centre and square to the grid**, so it reads as a diagram (the A9 note above). **The car sits inside one bay**, but canon has it straddling two |
| **8f-tpov** | **Tarquin's POV**, standing eye height, looking down | His hands and watch at the bottom edge, holding a phone. Bob cross-legged, hand at chin, looking up into the lens. Tent right, empty bays to fog | 🔑 The phone. It says *content* without a word | 🔴 **Red spots on Bob's hoodie read as blood.** A wedding band where canon has a signet ring. ⚠️ **The phone is a new story beat**, not canon (see its spec) |
| **8f-bpov** | **Bob's POV**, seated eye height, looking up | Bob's camo knees soft at the bottom. Tarquin standing over, full length. X8 behind him, left. Tent flysheet filling the right edge | 🔑 **The PTSD frame**: the car's red lights sit just behind the man looming over him | 🔴 **Tarquin dead centre and square to the lens**, a symmetry tell. The frown is edging toward a pantomime face |
| **8f-top** | **Overhead**, straight down | Car, Tarquin, Bob and tent on the grid, rain streaks | The narrator's view. **The only angle where the two-bay joke reads** | 🔴 **The tent is collapsed flat.** 🔴 **Physics: rain seen from directly above comes toward the lens**, so it reads as specks and rings, never long streaks. The car's body is slightly warped |

### Rulings every prompt in this set follows

- **Model:** there is no "Nano Banana Pro 2" (see `nano-banana-2.md`). **Run on Nano Banana Pro**, the model the accepted fog set used, for continuity. NB2 is the A/B if a frame fights. 🔴 **Never Nano Banana 2 Lite for these**: Google's API docs say Lite takes no character references at all, and Lite is the free-plan default, so check the picker.
- **Aspect ratio:** 16:9 with Flow's landscape toggle, never in the prompt (§31).
- **Attach:** **the accepted fog two-shot always goes last**, and is named as the reference for **place, fog, car, tent and light**. A Character goes in front of it **only when that man's face is big enough to bind** (§12, and the reference-size rule). Where the men are as small as in the reference, or smaller, the reference carries them and **nothing is cast**.
- **Never describe a referenced man.** Action, placement and face muscles only. **The one exception is an unbound body part** (§25): Tarquin's hands in `8f-tpov`, Bob's knees in `8f-bpov`.
- **Delete atmosphere, give weather physics.** The reference carries the fog, so we don't name it harder (§10). Rain is described only where it has something dark to fall against (§32).
- **Left and right always mean the frame**, never a man's own left (eleventh web pass).
- **Kodak Portra 400 stays** for continuity, despite the untested slop warning.
- **"Candid, taken quickly"** puts a human behind the camera. No "cinematic", no "rule of thirds" (never-cite list), and no "not quite level" (it failed four times on this shot).

### 8f-bpov — Bob's eyes: the man, and the car behind him · **still** · written 2026-09-15, unrun

**Shot spec**
- **Job:** the trigger. We are on the ground where Bob lives, a man stands over us, and **the car's red lights sit just past his hip.** It is the one frame in which the car is behind the threat.
- **Register:** documentary, human scale.
- **Depth:**
  - foreground: Bob's own knees, soft, and the tent flysheet on the right edge, soft
  - midground: Tarquin, full length, two metres away
  - background: the X8 ten metres back, then the fog
- **Focal point:** Tarquin's face, which wins on height and sharpness. The red lights are the second place the eye lands.
- **Light:** overcast sky through fog, shadowless. The rear lights are the only light source in frame.
- **Camera:** seated eye height, tilted up. 35mm, a person's-eye lens.
- **Withheld:** Bob's face. We only have his view.
- **What moves (in the video):** the rear lights, Bob's knees rising and falling as he breathes. Decided when the still is accepted.

**What changes from Jack's frame:** Tarquin moves off the centre line, with the car in the gap beside him. The expression is written as muscles. The knees are described (§25).

**Attach:** `@Tarquin-new` first, then the accepted fog two-shot. **Not `@Bob`**: his face is not in frame, and a Character with nowhere to go puts a face where it shouldn't be.

**→ Flow image surface · prompt box** (Nano Banana Pro · landscape · x2)

```prompt
Generate a still photograph. The job of this picture: we are sitting on the wet ground at the mouth of the tent, and the man who owns the car is standing over us with the car just behind him.

References: the man from the character reference is the standing man. The attached photograph is the reference for the place, the fog, the black BMW X8, the tent and the light. Keep all of those the same as in the photograph.

Camera: a first-person view from the eyes of a man sitting on the tarmac at the mouth of the tent, tilted up. A 35mm lens at f/5.6. The nearest thing in the picture is his own two knees, drawn up, crossing the bottom edge of the frame, soft and out of focus. The right-hand edge of the frame is the near side of the tent's flysheet, close to the lens and soft, with rain running down it.

Composition: the standing man is about two metres away, seen from head to feet, standing to the right of the middle of the frame. On the left of the frame, in the open space beside him and about ten metres behind him, the X8 is parked side-on with its rear lights lit, so the lights sit level with his hip.

Action: he has just stopped walking and his weight is settling back onto his heels, his arms hanging with his hands loose at his sides. His head is tipped down toward the lens. His brows are drawn very slightly together, his upper eyelids a little lowered, his mouth closed and flat, and his eyes are aimed straight down into the lens. The expression is small: a stranger would read it as mild distaste and nothing more.

The knees: worn camouflage-print trousers, dark with rain across the tops and grimy at the seams.

Light: overcast daylight coming down through the fog from every direction at once, so the standing man casts no shadow and his face is lit as evenly as the ground. The X8's rear lights are the only thing in the picture making light of their own, and their red lies in a broken streak on the wet tarmac under the car.

Weather: rain shows as fine bright streaks where it crosses the black of the car and the standing man, and as rings in the standing water around his feet. Against the pale fog it disappears into the grey.

Style: a candid documentary photograph taken quickly from the ground, on Kodak Portra 400 at ISO 1600. Unretouched, natural skin texture, fine grain in the shadows, muted cool colour.

Constraints: the red of the rear lights is the most saturated colour in the picture by a wide margin. No writing on any surface except the car's own badge. No other vehicles, buildings or people anywhere in the fog.

Thanks.
```

### 8f-low — ground level: the step toward him · **still** · written 2026-09-15, unrun

**Shot spec**
- **Job:** the approach, at Bob's height. The man steps in and the car waits behind. 🔑 **The one story change: Bob's eyes go to the car's rear lights, not to the man walking up to him.** That is the first sign that something other than Tarquin has hold of him, and it gives the frame its unresolved question: what is he looking at?
- **Depth:**
  - foreground: wet tarmac at the lens, with rain rings
  - midground: Tarquin mid-stride, and Bob at the tent
  - background: the X8, then the fog
- **Focal point:** Bob's face, which is the nearest face and has the eyeline. Tarquin wins on height.
- **Light:** as the reference. The rear lights are the only source.
- **Camera:** a hand's height off the ground, three metres from the tent, a little up-tilt. 24mm at f/8 for deep focus, which avoids fake-bokeh tells.
- **Withheld:** what Bob sees in the lights.

**What changes from Jack's frame:** the splash crown goes (rings only). Tarquin's stride is written as a shape (ninth pass), and Bob's eyeline goes to the lights.

**Attach:** `@Bob` first, `@Tarquin-new` second, the accepted fog two-shot last. Both faces are larger than in the reference, and each man is anchored to a named side (§26).

**→ Flow image surface · prompt box** (Nano Banana Pro · landscape · x2)

```prompt
Generate a still photograph. The job of this picture: at the height of a man sitting on the ground, a second man steps in toward him, and the seated man is not looking at the man. He is looking past him at the car's rear lights.

References: the man from the first character reference is the seated man. The man from the second character reference is the standing man. The attached photograph is the reference for the place, the fog, the black BMW X8, the tent and the light. Keep all of those the same as in the photograph.

Camera: resting a hand's height above the wet tarmac, about three metres from the tent, tilted a little upward. A 24mm lens at f/8, so everything from the water nearest the lens to the car is sharp. The bottom third of the frame is wet tarmac close to the lens, with rain rings spreading across the standing water.

Composition: on the right of the frame, the seated man sits on the ground at the mouth of the tent, the open doorway behind him. In the middle of the frame and a step nearer to him than the car, the standing man, tall in the frame, his head close to the top edge. On the left, about eight metres back, the X8 is seen from its rear three-quarter with its rear lights lit.

Action: the standing man is caught mid-stride toward the seated man. His front foot is planted flat, his back heel is lifting off the tarmac, and the arm opposite his front leg has swung slightly forward. His head is tipped down toward the seated man, his mouth closed and his brows level. The seated man has his knees drawn up and his forearms resting on them, his hands hanging loose. His head has turned away from the standing man toward the left of the frame, and his eyes are fixed on the car's rear lights. His brows are lifted slightly at the inner ends, his eyes a little too wide, and his lips are just parted. The expression is small: a stranger would take a second to see that anything was wrong.

Light: overcast daylight coming down through the fog from every direction at once, so nothing casts a shadow. The X8's rear lights are the only thing in the picture making light of their own.

Weather: rain shows as fine bright streaks where it crosses the black of the car and both men, and as rings on every pool of standing water. Against the pale fog it disappears into the grey.

Style: a candid documentary photograph taken quickly from the ground, on Kodak Portra 400 at ISO 1600. Unretouched, natural skin texture, fine grain in the shadows, muted cool colour.

Constraints: the red of the rear lights is the most saturated colour in the picture by a wide margin. The standing water is broken only by small rain rings, with no droplets leaping out of it. No writing on any surface except the car's own badge. No other vehicles, buildings or people anywhere in the fog.

Thanks.
```

### 8f-tpov — Tarquin's eyes, phone in hand · **still** · written 2026-09-15, unrun

⚠️ **Story flag before spending a credit:** Flow invented **the phone**. Tarquin looking down at
Bob with his phone out reads as *about to photograph him*. It's a strong beat (a man as content), but
**it is not canon**, and it lands a second judgement on Tarquin in a scene ruled at one beat each. The
prompt keeps it because Jack liked the frame. **Delete the phone sentence and the hands** if Jack
rules it out.

**Shot spec**
- **Job:** the look down. Bob seen from the height of a man who has everything, framed by that man's own watch and phone. This is the only frame in the set where **Bob looks back.**
- **Depth:**
  - foreground: Tarquin's hands, the watch and the phone, soft
  - midground: Bob and the tent
  - background: empty bays fading into fog
- **Focal point:** Bob's eyes, which win on being the only face and on eyeline.
- **Camera:** a standing man's eye height, looking down about 35°. 28mm.
- **Visible cost:** Bob on wet tarmac, and the empty grid around him.

**What changes from Jack's frame:** the red marks come out (a colour comparison, not a wardrobe line). The hands are described (§25) with canon's signet ring and old steel watch. They **grip** the phone, because hands gripping an object render better (eighth pass). Bob's hand moves off his chin, because hands near the face fail more often.

**Attach:** `@Bob` first, then the accepted fog two-shot. **Not `@Tarquin-new`**: his face is not in the picture.

**→ Flow image surface · prompt box** (Nano Banana Pro · landscape · x2)

```prompt
Generate a still photograph. The job of this picture: through the eyes of a man standing over a man sitting on the ground, with his own phone in his hands, and the seated man looking straight back up at him.

References: the man from the character reference is the seated man. The attached photograph is the reference for the place, the fog, the tent and the light. Keep all of those the same as in the photograph.

Camera: a first-person view from the eye height of a tall standing man, looking down at about thirty-five degrees. A 28mm lens at f/5.6. The nearest thing in the picture is his own two hands at the bottom edge of the frame, close to the lens and soft.

Composition: the seated man sits cross-legged on the wet tarmac about two and a half metres away, just left of the middle of the frame. The tent fills most of the right half of the frame beside him. Behind him and to the left, the painted bay lines run away over empty wet tarmac and pale out into the fog.

The hands: the backs of a pale, indoor man's hands in his late forties, gripping a black phone low in front of him in both hands, its back toward the seated man. An old scuffed steel watch on one wrist and a plain heavy gold signet ring on one little finger.

Action: the seated man has his forearms resting on his knees and his hands loosely clasped. His head is tipped back and his eyes are aimed straight up into the lens. His brows are level, his eyelids steady, his mouth closed, and his jaw set. His face is doing almost nothing: he is watching, not asking.

Light: overcast daylight coming down through the fog from every direction at once, so nothing casts a shadow and the seated man's face is lit as evenly as the ground.

Weather: rain shows as fine streaks where it crosses the dark tarmac and as rings in the standing water. Against the pale fog it disappears into the grey.

Style: a candid documentary photograph taken quickly, on Kodak Portra 400 at ISO 1600. Unretouched, natural skin texture, fine grain in the shadows, muted cool colour.

Constraints: there is nothing red anywhere in this picture. The dirt on the seated man is dull grey and brown. No writing on any surface. No vehicles, buildings or other people anywhere in the fog.

Thanks.
```

### 8f-high — the raised wide: a field with two men in it · **still** · written 2026-09-15, unrun

**Shot spec**
- **Job:** the establisher. The car park is a field of empty bays and there is nothing in it but them. ⚠️ Per the A9 note above, this is **the scene's opening wide, not the argument.** Cut it early.
- **Depth:** the soft painted lines crossing the bottom edge, then the trio, then the grid dissolving into fog.
- **Focal point:** the trio, **low and left**, with open tarmac and fog on the right.
- **Camera:** about eight metres up and twenty-five back, looking down about 30°. **Turned off the bay grid**, because a square-on grid is a symmetry magnet (§37). 50mm.
- **Scale reference:** the two men.
- **Canon fix:** the car straddles the line between two bays.

**Attach:** the accepted fog two-shot **only**. The men are the same size as in the reference or smaller, so the reference carries them.

**→ Flow image surface · prompt box** (Nano Banana Pro · landscape · x2)

```prompt
Generate a still photograph. The job of this picture: a supermarket car park seen from above as a wide field of empty parking bays, with nothing in it but one car, one tent and two men.

References: the attached photograph is the reference for the two men, the black BMW X8, the tent, the fog and the light. Keep all of them the same as in the photograph, and keep the two men in the same poses.

Camera: raised about eight metres above the tarmac and about twenty-five metres back, looking down at about thirty degrees. A 50mm lens at f/8, so the whole grid is sharp until the fog takes it. The camera is turned so it is not square to the parking bays: the painted lines run away diagonally across the frame from the lower right toward the upper left.

Composition: the car, the two men and the tent sit together in the lower left of the frame. The X8 is parked across the painted line between two bays, its body over the line so that it takes up both bays. The standing man is just beyond it and the seated man and the tent are in the next bay along. The rest of the frame, all of the right side and the whole upper half, is empty bays, row after row, going paler and softer until the lines vanish into flat grey fog. The nearest painted lines cross the bottom edge of the frame.

Light: overcast daylight coming down through the fog from every direction at once, so nothing casts a shadow. The X8's rear lights are the only thing making light of their own, and their red lies in a streak on the wet tarmac behind the car.

Weather: rain shows as fine streaks against the dark tarmac.

Style: a candid documentary photograph on Kodak Portra 400 at ISO 1600. Unretouched, fine grain in the shadows, muted cool colour. The tarmac is patched in mismatched greys with water pooled unevenly in the low places.

Constraints: the red of the rear lights is the most saturated colour in the picture by a wide margin. No writing on any surface except the car's own badge. No other vehicles, buildings, lamp posts or people anywhere in the car park or the fog.

Thanks.
```

### 8f-top — straight down: two spaces, for that · **still** · written 2026-09-15, unrun

**Shot spec**
- **Job:** the narrator's view, from the future and from above. **The two-bay joke is legible only from here**: the car over the line, and the tent squeezed into one bay beside it.
- **Depth:** from directly above, depth becomes **pattern plus fog**. The fog thickens toward the frame edges, so the centre is the clearest.
- **Focal point:** the car, the darkest and largest shape, **turned diagonally across the grid** while everything else lies square.
- **Camera:** straight down, about fifteen metres up. 35mm.
- **The physics that fixes the rain:** rain falls toward the lens, so it shows as short soft specks and rings, not streaks (§32's family). Tell the model the consequence, not the rule.
- **The tent:** from above, a dome shows its two poles as a crossed X and a rounded top. Saying so is what stops it coming back flat.

**Attach:** the accepted fog two-shot **only**. No faces are visible from above.

**→ Flow image surface · prompt box** (Nano Banana Pro · landscape · x2)

```prompt
Generate a still photograph. The job of this picture: looking straight down on a wet car park from high above, where one car has taken two parking spaces and a man lives in a tent in the space beside it.

References: the attached photograph is the reference for the black BMW X8, the tent, the two men, the fog and the light. Keep all of them the same as in the photograph.

Camera: directly overhead, about fifteen metres up, pointing straight down at the ground. A 35mm lens at f/8.

Composition: the white painted bay lines make a square grid across the whole frame. In the middle of the frame, the X8 is parked at an angle across the line between two bays, its roof and bonnet over both of them. It is the only thing in the picture that is not square to the grid. In the next bay to the right, the tent lies neatly inside its lines: seen from above, its dome is a rounded shape with its two poles crossing in an X over the top, and its open door faces the car. On the tarmac between them, the standing man is seen as the top of his head and his shoulders, and the seated man sits at the tent door with his knees drawn up.

Light: overcast daylight coming down through the fog from every direction at once, so nothing casts a shadow. The X8's rear lights glow red at the back of the car.

Weather: seen from directly above, the rain falls toward the lens, so it shows only as short soft specks in the air and as rings breaking every pool of standing water. A thin veil of fog lies over the whole car park and grows thicker toward the edges of the frame, where the grid lines pale into grey.

Style: a candid documentary photograph on Kodak Portra 400 at ISO 1600. Unretouched, fine grain in the shadows, muted cool colour. The tarmac is patched in mismatched greys with water pooled unevenly in the low places, and the car's roof is rain-flecked.

Constraints: the car's body is straight and undistorted, the same shape as in the reference photograph. No writing on any surface except the car's own badge. No other vehicles or people anywhere in the frame.

Thanks.
```

### 8f-tpov — round 2, simple, no phone · **still** · written 2026-09-15, unrun

**Jack, 2026-09-15:** *"Tarquin had a phone in his hand for some reason, please fix it in a new prompt, keep it simple."* **The phone is ruled out.**

**The fix is geometric, not a ban** (§27: you cannot subtract, only substitute). **The hands are gone from the frame entirely.** The nearest thing in the picture is wet tarmac, so there is nothing for a phone to sit in. **The prompt is cut to about half** as asked. The job, camera, Bob's face, light and style survive.

**Attach:** `@Bob`, then the accepted fog two-shot.

```prompt
Generate a still photograph. The job of this picture: looking down from the eyes of a standing man at a man sitting on the wet ground, who looks straight back up.

References: the man from the character reference is the seated man. The attached photograph is the reference for the place, the fog, the tent and the light. Keep all of those the same as in the photograph.

Camera: from the eye height of a tall standing man, looking down at about thirty-five degrees. A 28mm lens at f/5.6. The nearest thing in the picture is wet tarmac about a metre in front of the camera, so the whole bottom edge of the frame is wet ground.

Composition: the seated man sits cross-legged on the tarmac about two and a half metres away, just left of the middle of the frame. The tent fills most of the right half of the frame. Behind him, empty painted bays run away and pale into the fog.

Action: his forearms rest on his knees. His head is tipped back and his eyes are aimed straight up into the lens, his brows level and his mouth closed. His face is doing almost nothing.

Light: overcast daylight through the fog, from every direction at once, so nothing casts a shadow.

Style: a candid documentary photograph on Kodak Portra 400 at ISO 1600. Unretouched, natural skin texture, fine grain, muted cool colour.

Constraints: nothing in the picture is red. No writing on any surface. No vehicles, buildings or other people in the fog.

Thanks.
```

### 8f-low — the clip · **video** · written 2026-09-15, unrun

**Jack's brief for every clip in this set, 2026-09-15:** *"interesting shots of them, not talking or
making any facial expression."* Built on **the accepted 8f-low still**: Tarquin mid-stride between the
X8 and the tent, Bob seated at the tent door looking up at him, the red tail lights broken up in the
foreground puddle.

**Shot spec (shot-craft)**
- **Job:** the arrival lands. He finishes the step that brought him here and stands over a man who
  doesn't move. The power shifts through **stillness**, not through a face.
- **World moves, camera doesn't** (R7, hybrid method). The push-in happens in Premiere, a slow
  8–10% scale toward the gap between the two men.
- **Two beats for 8s:** (1) the step completes and his weight settles; (2) later, Bob's eyes drop from
  Tarquin to the ground. That's a gaze, not an expression, and it's the power shift. **Everything else
  is continuation**: rain, breath, one blink each.
- **Why not have him keep walking:** a moving figure on Frames is redrawn in every position
  (camping 5a). Two figures whose distance changes merge (Karen §2h.7v). A walk past Bob would also
  send his reflection moving through the puddle, which is the documented reflection failure.
  **A single completed step keeps the change small.**
- **No expression, but not a statue:** ninth pass. "Minimal movement" freezes a person, so they
  breathe and blink, at different moments.

**Tab: Frames**, with the accepted 8f-low still as the first frame.
- Both staging and two faces must hold, so it's the tab rule's "both" row: **Frames, with the motion
  cut to almost nothing.**
- ⬜ **30-second check:** if the Frames tab now accepts a Character (tenth pass says the API does),
  add `@Tarquin-new` and `@Bob`.
- **Fallback if a face drifts:** Ingredients, with the still plus both Characters, in the
  two-sentence form that worked on 2f-5.

**Anti-slop, per tell**
- **Slow-motion bias:** say "at real speed".
- **Floaty foot:** the heel comes down with weight.
- **Statue freeze:** breathing, and one blink each at different moments.
- **Mouth movement / speech:** "mouths closed", with no colon after an action and no quotation marks.
- **Reflection trouble:** the reflection is not named (§10), and his motion is kept small.
- **A tripod getting drawn:** no camera nouns. Write "the view holds perfectly still".
- **"Cinematic" / hype words:** none used.

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted 8f-low
still. **No end frame.** **16:9 · 720p · x2 · 8s** (8s kept as narration cover; the prompt carries a second beat so the back half doesn't drift). No 360p draft: retired
2026-09-15, see `omni-flash.md` *Default settings*.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

The standing man finishes the step he is in: his back foot comes forward and lands heel to toe on the wet tarmac beside the other, his weight settles onto both feet, and he stands looking down at the seated man.

The seated man stays where he is, looking up at him and breathing slowly. Both men keep their brows relaxed and their jaws loose, their mouths closed throughout, and each blinks once, at different moments.

Later in the shot, the seated man lowers his eyes from the standing man to the wet ground in front of his feet, and keeps them there while the standing man goes on looking down at him.

Rain keeps falling at the same rate, breaking the standing water into rings and running down the back of the car.

Audio: steady rain on wet tarmac, rain drumming on the car roof and pattering on the tent, and one wet footstep. No music and no voices.

Thanks.
```

**Check before accepting:**
- One step that lands with weight and doesn't glide. Two legs, and feet that stay planted.
- Both faces stay the same people, with no mouth movement and no change of expression.
- The blinks don't happen together.
- The car, tent and bay lines don't ripple or redraw.
- His reflection in the puddle moves with him and doesn't split.
- No new people, no camera, no speech.

### 8f-breathe — Bob alone in the fog, breathing · **video** · written 2026-09-15, unrun

**The still:** the accepted `8f-tpov` round-2 frame. Bob sits cross-legged on wet tarmac beside the
tent, hands on his knees, face tilted up. The car park is gone into fog and nobody else is there. **It
missed as Tarquin's POV and was re-cast the same day as the breathing exercise**: the inside of
Bob's head, where the car and the man have gone and he is bringing himself back.

**Shot spec (shot-craft)**
- **Job:** the calm after the trigger. The only frame in the scene with **one person and no threat in it**.
  The emptiness does the argument: *nobody is coming, and he is dealing with it alone.*
- **World moves, camera doesn't.** A slow push toward Bob happens in Premiere and ends on the closed eyes.
- **Two beats for 8s** (the house default):
  1. **Breath:** a slow, deep breath in, held briefly, and a long breath out, with shoulders and chest rising and falling.
  2. **Eyes close** partway through the second breath, and stay closed.

  That's eyelids, not an expression, and it's the beat's payoff.
- **Not asked for:** a head move (bigger face redraw), hands moving (the weak spot, so they rest), the tent
  moving (no wind), breath vapour (it's atmosphere, and named atmosphere overdelivers into smoke).
- **Visible cost:** him on wet tarmac, the stains, and the empty field of bays.
- **Light:** overcast through fog, shadowless, and steady (fine texture boils under changing light).

**Tab: Frames.** One face, near-static motion, and the empty car park is the point, so it's the tab rule's
"both" row. **Fallback if his face drifts at the eye close:** Ingredients with the still plus `@Bob`, in the
short form.

⚠️ **Already in frame 0 and not fixable in the clip:** the red-brown flecks on his hoodie. If they read as
blood at full size, it's a grade or paint job in post.

**What the web pass changed** (twelfth pass, `omni-flash.md`)
- 🔑 **Lead with the breath, not the pose.** "Sits", "rests" and "gazes" as the main verb freeze a person.
  The start frame already carries the pose.
- **Breaths slightly different in length**, so it doesn't pulse like a metronome.
- **The light stays even.** A shadow change across the face reads as the face redrawing.
- **The fog is not named.** Fog pulsing is a model limit, not a prompt fix, and named atmosphere overdelivers.
  Breath vapour is left for post if wanted.
- **Audio names his breathing as close and slightly uneven.** It gives the model the sound it should make.

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted 8f-tpov round-2
still. **16:9 · 720p · x2 · 8s · no end frame.**

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

The man draws a slow, deep breath in, his chest and shoulders rising, holds it for a moment, and lets it out in a long breath, his shoulders dropping. He keeps breathing like that for the whole shot, each breath a little different in length.

During his second breath his eyes close slowly, and they stay closed. His brows stay relaxed, his jaw loose and his mouth closed throughout, and his hands stay on his knees.

Fine rain keeps speckling the wet tarmac around him. The tent stands still, and the light stays even and unchanged.

Audio: light rain on wet tarmac and pattering on the tent, and close by, his own slow breathing, slightly uneven. No music and no voices.

Thanks.
```

**Check before accepting (hands, then face, then edges):**
- The hands stay whole on the knees.
- The eyes close once and stay shut, and his face stays the same man through the close.
- The breathing moves his shoulders and doesn't inflate his torso.
- The fog stays steady and doesn't pulse. The tent doesn't ripple. The bay lines don't slide.
- His reflection under him stays one shape.
- No other people, no speech.

### 8f-high — the clip · **video** · written 2026-09-15, unrun

**The still:** the accepted `8f-high` take. The trio sits in the middle of an endless wet grid fading into
fog, with heavy rain streaks and the X8's red lights lying in the tarmac.

**Shot spec (shot-craft)**
- **Job:** the establisher. The car park is a field and nothing is coming. ⚠️ **This take lines the car, the man
  and the tent up on one lateral line** (symptoms.md: *"reads like a diagram"*), and the subject is a small
  part of the frame (*"looks amazing but isn't about anything"*). **The clip can't fix composition. The edit
  can:** `principles.md` 21a says *keep the height, lose the distance*, so a slow Premiere push-in toward the
  trio across the clip makes the frame about them by the end.
- **World moves, camera doesn't.**
- **Two beats for 8s:**
  1. **Continuation:** rain and stillness. The establishing seconds.
  2. 🔑 **The car locks itself:** its indicators flash twice with a chirp, and **the seated man's shoulders
     draw in at the flash.** It's a silhouette-scale reaction, which is the only kind that reads at this size
     (8b-fog proved it). **And it's the trigger**: the indicator is the scene-2 crash callback from the PTSD
     discussion. ⚠️ **Not yet approved by Jack. Delete the second paragraph to drop it**, and the clip becomes
     pure establisher.
- **Faces:** none legible, so there's no identity risk.

**Tab: Frames.** The staging is the shot, and there are no faces to hold.

**What the web pass changed** (thirteenth pass, `omni-flash.md`)
- **The camera sentence names what is allowed to move.** Wide shots drift by default, and "movement only from…"
  closes the rest without naming a camera.
- **The flash has a cause (the lock), timing ("halfway", "quickly"), and the chirp in the same sentence.**
- ⚠️ **"Twice" may come back as one or three flashes**, since video models are bad at counts. If the count
  matters, add the flashes in post.
- ⚠️ **Distant painted lines can crawl, and upscaling makes it worse.** Only upscale a take whose lines hold.

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted 8f-high take.
**16:9 · 720p · x2 · 8s · no end frame.**

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still for the whole shot, with movement only from the rain, the car's lights and the seated man. A single continuous shot, everything at real speed.

Heavy rain keeps falling across the whole car park at the same rate, breaking the standing water into rings. The two men stay where they are, the standing man looking down at the seated man.

Halfway through the shot the car locks, and its orange indicators flash twice, quickly, with two short electronic chirps. At the flash, the seated man's shoulders draw up and in, and they stay there.

Audio: heavy rain across a wide open car park and drumming on the car roof, then the two chirps of the car locking. No music and no voices.

Thanks.
```

**Check before accepting:**
- The bay lines and the fog edge stay put, with no crawl, swim or drift.
- The flashes come from the car's own lights and nowhere else, and the red reflection doesn't split.
- The seated man's shoulders move and he stays one shape. Neither man morphs.
- The rain doesn't thin out or change direction.
- No new people or cars, no speech.

### 8f-top — the clip · **video** · written 2026-09-15, unrun

**The still:** the accepted `8f-top` take. Straight down on patched wet tarmac, the X8 diagonal across two bays
with its rear lights glowing red on the ground, Tarquin as the top of a head, Bob at the tent door.

**Shot spec (shot-craft)**
- **Job:** the narrator's view, from someone who already knows how it ends (principle 21). **Two spaces, for that.**
- ✅ **Principle 21a passes:** this take is *high but close*. The car, both men and the tent fill a large share
  of the frame, so it is about them, not about the grid.
- **World moves, camera doesn't.** From straight down, any drift reads as a drone and breaks the god's-eye stillness.
- **Two beats for 8s:**
  1. **Rain from above:** fresh rings open on the wet tarmac and on the car's roof, all through the shot.
  2. 🔑 **The rear lights go out, and the red on the ground goes with them.** It pairs with the lock in `8f-high`,
     so the edit can cut on it. After it, the frame is all grey, with no warmth left in the picture.
- **The men:** near-still. The seated man's head lowers. At this size only body shapes read, and nobody's
  face is visible.

**Tab: Frames.** The geometry is the shot, and there are no faces to hold.

**What the web pass changed** (fourteenth pass, `omni-flash.md`)
- **No "bird's eye" and no "drone".** Prompt libraries pair bird's eye with a 360° rotation, and a named drone
  may get drawn. Write "the view looks straight down".
- **Each rain ring has an end:** it spreads and fades.
- **The light-off has a visible cause (the lock), a speed ("abruptly") and an end state in colour** ("dark wet grey").

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted 8f-top take.
**16:9 · 720p · x2 · 8s · no end frame.**

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view looks straight down and holds perfectly still for the whole shot, with movement only from the rain, the car's rear lights and the seated man. A single continuous shot, everything at real speed.

Rain keeps landing all over the wet tarmac and on the car's roof, each drop opening a small ring that spreads and fades. The standing man stays where he is, and the seated man slowly lowers his head.

Halfway through the shot the car locks, and its rear lights switch off abruptly. The red glow on the wet ground behind the car goes with them, leaving dark wet grey.

Audio: steady rain on open tarmac, a lighter patter on the car roof and the tent, and the short electronic chirp of the car locking. No music and no voices.

Thanks.
```

**Check before accepting:**
- The view doesn't rotate, drift or tilt, and the bay lines stay square.
- The car stays rigid and doesn't slide. The lights go off once and stay off, and the red glow goes with them.
- The two figures stay one shape each, and the tent holds its shape.
- The rain rings don't turn into a pattern that repeats.
- No new people, no speech.

### Revision log — scene 8 fog coverage

| id | Round | Model | Result | Verdict |
|---|---|---|---|---|
| all five | 0 | Flow, from the accepted fog two-shot + Characters, Jack's own ask | The five frames described in the table above | ✅ Jack likes all five. Prompts above are round 1 |
| 8f-bpov | 1 | | | ⬜ |
| 8f-low | 1 | | | ⬜ |
| 8f-tpov | 1 | Nano Banana Pro | Tarquin's hands came back holding a phone | ❌ Jack: the phone has to go. Round 2 above removes the hands |
| 8f-tpov | 2 | | | ⬜ |
| 8f-high | 1 | | | ⬜ |
| 8f-top | 1 | | | ⬜ |
| 8f-low clip | 1 | Omni Flash · Frames · 720p · x2 · 8s | Clip from the accepted 8f-low still | ✅ Jack, 2026-09-15: *"those worked"* |
| 8f-breathe clip | 1 | Omni Flash · Frames · 720p · x2 · 8s | Clip from the accepted 8f-tpov round-2 still | ✅ same |
| 8f-high clip | 1 | Omni Flash · Frames · 720p · x2 · 8s | With the car-lock beat | ✅ same |
| 8f-top clip | 1 | Omni Flash · Frames · 720p · x2 · 8s | Lights off on the lock | ✅ same |

---

## Scene 9 — the retreat

⚠️ **The 9a yurt interior and 9b eye prompts were never recorded here.** Both were shot 2026-08-27
([`shot-list.md`](./shot-list.md)).

### 9-walk — Tarquin walks up to the yurt · **still** · written 2026-09-14, unrun

**Jack, 2026-09-14:** *"make an image of Tarquin walking up to the yurt, we need to make a video of
that, start with the still"*, with the 9a interior attached for the look. It sits under the narration
line *"He heads off to Wales for this spiritual retreat."* 🔑 **It also fills a hole in the cut.**
Clip 26 in [`edit-plan.md`](./edit-plan.md), *"a man entering the dome"*, is in the **dropped** river-dome
location. This is the yurt version of the same connective beat.

**Web pass:** ninth, 2026-09-14, logged in
[`nano-banana-2.md`](../../google-flow/nano-banana-2.md#ninth-web-pass--2026-09-14-academic-community).

**Shot spec (shot-craft):**

1. **Job:** a man who has never sat on a floor arrives at a round canvas tent in a Welsh field he has
   paid a fortune for. He falls asleep in this round fabric shelter and wakes in one he didn't pay for
   (10a), so the yurt's shape has to register here, from outside, before the interior.
2. **Register:** documentary, human scale. Gate 2 isn't triggered, since nothing monumental is in frame.
3. **Depth:** foreground is long wet grass tussocks, soft, at the bottom edge. Midground is him on the left
   and the yurt on the right, at about the same distance. Background is bare trees, dark against the sky.
4. **Focal point:** his face, which wins on position and on his gaze. The warm windows are the second
   stop, and his eyeline leads to them.
5. **Light:** 🔑 **the blue-hour sky is the only light on him**, dim and cool. **The yurt's two small
   windows glow a weak warm orange from the candlelight inside (9a)**, and that is the one bright anchor
   in a dark frame. They are a bounded practical: too weak to light the grass or him (§20). Both ends of
   the exposure are named.
6. **Camera:** 85mm, about nine metres from him, standing height, level, **off his path to the side**,
   so he crosses left to right, angled slightly towards the lens. A long lens was chosen for three reasons:
   - it stacks the yurt and the trees close behind him (§14);
   - it gets a three-quarter face at a size the Character can hold (§12);
   - it still fits his whole body plus a strip of grass below his feet.
7. **Withheld:** the retreat. There's one yurt, no other guests, no car and no signs. The inside is
   withheld too, and only the glow says anything is in there.
8. **Unresolved question:** he is mid-stride towards a door he hasn't opened, with his face already
   passing judgement on it.
9. **What moves (for the clip):** he walks on to the door. The camera is locked.

**Decisions and their reasons:**

- 🔴 **Cast `@Tarquin-new` alone, and write nothing about how he looks.** The gilet lives in that
  Character's Body ([8b-fog A12-cast](#8b-fog--variant-a12-cast--the-running-version--still--written-2026-09-08-unrun)).
  The sock-less loafers on wet grass are the joke, but they're wardrobe, so they're not written; the
  Character carries them. ⬜ *Unverified:* the repo doesn't record which Character 9a was cast on. If the
  outfit doesn't match 9a, check the Character's Body before touching the prompt.
- **No reference image for the yurt.** It's one reference (the Character), and the 9a still is an
  interior anyway. The exterior is described: cream canvas, a shallow conical roof, a small painted
  wooden door, and two small windows with the timber lattice showing through.
- **The stride is written as a shape, not the word "walking"** (ninth pass). His left foot is planted
  ahead, his right heel is lifting behind, and his right arm is swung a little forward, which is the
  opposite arm to the front leg so the legs don't swap. **No motion blur**, because blur in a first
  frame breaks image-to-video (ninth pass, community).
- **His whole body is in frame, with grass below his feet.** Cropped feet get invented in the clip.
- **Hands are empty.** Props in hands are the unsafe case on Omni (eighth pass). There's no holdall.
- **No glamping-advert look.** No fairy lights, lanterns or string lights. The ground is dark wet grass
  with a dull sheen, not a mirror. None of *HDR*, *cinematic* or *magical*. That look is the
  bracketed real-estate-at-dusk genre, which is exactly what warm windows against a blue sky pull toward
  (ninth pass, *inferred*).
- **Expression is muscles, with the wrong readings named:** chin up, eyes on the yurt, brows faintly
  drawn together, one corner of the mouth pulled in. Not nervous, not awed, not smiling.
- **Stock:** Portra 400 pushed, matching 8b and 8b-fog, his last two scenes. Continuity beats the untested
  Portra-is-slop note.

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **Character:** `@Tarquin-new` and nothing
else. **No reference image.** **Aspect:** 16:9. **Outputs:** 2.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 400 pushed to ISO 1600, a single handheld exposure. Visible grain in the shadows, muted cool colour, low saturation, calm observational tone.

A field in rural Wales at blue hour, just after sunset. The man from the character reference is walking up to a yurt for a spiritual retreat.

Camera and framing: 85mm lens at f/2.8, standing height and level, about nine metres from him, set off to the side of his path so he crosses the frame from left to right, angled slightly towards the camera. His whole body is in frame, from the top of his head to his feet, with a strip of wet grass below his shoes. He is on the left third of the frame. Long wet grass tussocks cross the very bottom of the frame close to the lens, soft and out of focus. Focus sits on his face.

Action: His left foot is planted on the grass ahead of him and his right heel is lifting off the grass behind him, his right arm swung a little forward and his left arm a little back, his hands empty and loose. His head is turned towards the yurt and his eyes are on it. His chin is slightly up, his brows are drawn very slightly together, and one corner of his closed mouth is pulled in. It is the look of a man appraising something he has paid a lot for and is not yet sure about. He is not nervous, not awed and not smiling. He is frozen sharp, with no motion blur, and he is not aware of the camera.

Environment: On the right of the frame, a few metres ahead of him and seen side-on, a single yurt: a low round wall of cream canvas, weathered and grubby near the ground, under a shallow conical canvas roof. A small painted wooden door faces him. Two small square windows in the canvas wall show the dark criss-cross of the timber lattice inside. The field between him and the door is open, uneven wet grass. Behind them, a line of bare winter trees stands black against the sky.

Light: The deep blue evening sky is the only light on him, dim and cool, so his face and clothes are soft and low in contrast. The yurt's two small windows glow a weak warm orange from candlelight inside, the only warm light in the picture and too faint to light the grass or him. The windows are bright but not burnt out, the sky above the trees is still clearly blue, and the grass is dark but still shows its texture, with a dull wet sheen and no reflections.

Details: Real skin texture, fine natural grain, dew on the grass, ordinary and unstyled.

Constraints: Ensure the scene looks like present-day rural Britain. There is one yurt and only one person in the frame. The yurt and the trees carry no fairy lights, string lights or lanterns. No signs, logos or readable text anywhere in the frame.

Compose for a 16:9 frame.

Thanks.
```

**Check before accepting:**
- His face reads as Tarquin at this size. **If not, move closer, don't add words** (§12): go from nine
  metres to seven.
- His outfit matches 9a.
- The legs are right: two feet, the rear heel up, the opposite arm forward.
- No fairy lights or glow anywhere except the two windows.
- The yurt is side-on and the door faces him.
- No motion blur on him.
- The ground isn't a mirror.

### 9-walk — round 1, **not accepted** (Jack, 2026-09-14: *"too boring"*)

**What held:** his face, the full outfit (gilet, jeans, sock-less loafers) from `@Tarquin-new` alone, the
stride, and a good weathered yurt. **Keep all of that.**

**Diagnosis** ([`symptoms.md`](../../cinematography/symptoms.md) A, *"it's fine but boring"* and *"it reads
like a diagram"*):

- **Eye level, side-on, and nothing withheld.** That is the recipe for furniture.
- **The man and the yurt are the same size at the same distance, side by side on one line**, so there is
  no depth order (principle 21b).
- **It came back far brighter than blue hour.** "The sky is the only light on him" didn't darken it.

**Jack's fix is the textbook one:** the yurt goes **nearest and largest**, and he goes far away down a path.

### 9-walk — round 2 · **still** · written 2026-09-14, unrun

**Tenth web pass:** 2026-09-14, logged in [`nano-banana-2.md`](../../google-flow/nano-banana-2.md#tenth-web-pass--2026-09-14-academic-community).

**Shot spec (shot-craft), changes from round 1 only:**

1. **Job (sharper):** the audience meets the thing he's paying for *before* him. The glowing round
   shelter fills our side of the frame, and he's a small figure coming to it. That order sets up the 10a
   rhyme.
2. **Depth, in order:**
   - **Foreground:** the yurt's weathered canvas wall and door, huge, cut off by the right and top frame
     edges.
   - **Midground:** a worn muddy track curving away up the field.
   - **Background:** him on the track, small, where it tops a gentle rise, with the black treeline and
     the last pale band of sky behind him.
3. **Height, broken:** the camera is **low, at knee height**, tight against the canvas. Principle: break
   height, light or information withheld.
4. **Focal point:** him, winning on **the leading line (the track) and figure against sky**. His dark
   shape sits against the palest part of the frame. The glowing door window is the second stop, and it is
   the one bright anchor.
5. **Lens:** 24mm, stopped down to f/8, **deep focus**. Both the canvas weave and the distant man are
   sharp, which avoids the fake depth-of-field tells completely (tenth pass).
6. **Light:** **later and darker** than round 1, twenty minutes after sunset, with the field falling
   towards near-dark. The door window's candlelight lays a faint warm patch on the wet grass right beside
   the door, about a metre away, which is physically possible (§20). It does not reach the track or him.
   He is lit by the sky alone.
7. **Withheld:** his face. At this distance it can't be read, and that's the right call for an arrival
   (the clip brings him closer). The inside of the yurt is withheld too, only flame points behind the
   lattice.
8. **No dead-centre vanishing point:** the track **curves** from the bottom middle of the frame up to the
   left. Parallel lines are a known failure (ControlVP), and a straight path is a symmetry magnet (§37).

**Decisions:**

- **The Subject is the track**, not the yurt or the man ([making a subject small](../../google-flow/nano-banana-2.md#-making-a-subject-small-put-something-else-in-the-subject-slot-community-2026-09-09)).
- **The yurt is described from round 1's picture, not round 1's prose** (§7): cream canvas streaked with
  green, a weathered grey plank door with a small glazed lattice window in its top half.
- 🔴 **Still no description of him.** Round 1 proved the Character carries the outfit. At this size the
  *face* won't bind (§12), which is fine because it's unreadable anyway. ⬜ **If the outfit is lost at this
  distance**, that is [the one narrow exception](#8b-fog--variant-a12-cast--the-running-version--still--written-2026-09-08-unrun):
  add the outfit then, not before.
- **No "cinematic".** It's on the kill list. The cinema comes from the design: low, wide, deep, one warm
  anchor, figure against sky.
- **16:9, framed slightly wide**, so the clip can push in.
- ⚠️ **For the clip, not now:** as he walks closer, Frames will invent his face. Plan to cast
  `@Tarquin-new` in the video too, keep the walk slow, and stop him before a medium shot (tenth pass,
  *unverified*).

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **Character:** `@Tarquin-new` and nothing
else. **No reference image.** **Aspect:** 16:9. **Outputs:** 2.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 400 pushed to ISO 1600, a single handheld exposure. Visible grain in the shadows, muted cool colour, low saturation, quiet observational tone.

Subject: a worn, muddy track through wet grass in a field in rural Wales, twenty minutes after sunset, leading up a gentle rise to a yurt at a spiritual retreat.

Camera and framing: 24mm lens stopped down to f/8, the camera held low at knee height, pressed close beside the canvas wall of the yurt and looking back along the track, so everything from the canvas beside the lens to the far treeline is sharp. The yurt fills the right third of the frame, very close and very large, running off the right-hand edge and the top of the frame. Its round wall is weathered cream canvas streaked with green, and at the left edge of it stands its door, a weathered grey plank door with a small glazed window in its top half showing a timber lattice. From the bottom middle of the frame, the track curves away to the left and up the rise, narrowing as it goes.

Action: Far up the track, where it tops the rise, the man from the character reference walks down it towards the yurt, small in the upper left of the frame, his whole body visible from head to feet on the track. His left foot is planted ahead of him and his right heel is lifting behind, his right arm swung a little forward and his hands empty. He is too far away for his face to be made out. His dark shape stands out against the pale band of sky just above the treeline.

Environment: Beyond him, a line of bare winter trees stands black along the top of the rise. Above the trees, the sky fades from a last pale grey-blue near the horizon to deep blue at the top of the frame. The grass either side of the track is long, dark and wet.

Light: The fading evening sky is the only light on the field and on him, so the grass falls away towards near-dark and he is a dark figure against the sky. The small window in the door glows warm orange from candlelight inside, with points of candle flame behind the lattice, and it lays a faint warm patch on the wet grass just below the door and nowhere else. The window is bright but not burnt out, the sky above the trees is still clearly readable, and the darkest grass still shows a trace of texture.

Details: Real canvas weave and grime, mud and puddled footprints in the track, dew on the grass, fine natural grain, ordinary and unstyled.

Constraints: Ensure the scene looks like present-day rural Britain. There is one yurt and only one person in the frame. The yurt and the trees carry no fairy lights, string lights or lanterns. No signs, logos or readable text anywhere in the frame.

Compose for a 16:9 frame, framed slightly wide.

Thanks.
```

**Check before accepting:**
- He's on the track, small, against the sky, and **still reads as Tarquin by the outfit**.
- The track curves and doesn't run straight to the centre.
- The yurt edge is big and doesn't look pasted on.
- The only warm light is the door window and its patch of grass.
- It's darker than round 1.
- He's a single figure, with two legs, not cloned.

### 9-walk — round 2 ✅ **ACCEPTED 2026-09-14** (Jack moved straight to the video)

**It fixed the flatness:** the yurt is nearest and largest, and he is small against the palest sky. The
candle in the door window is the one warm anchor, and the ruts lead to him.

**Three differences from the prose, and the picture wins:**
- **The track is two straight wheel ruts**, not a curve. They converge on him rather than on the frame
  centre, so it works. `[observed]` *"curves away to the left"* was ignored.
- **The warm patch at the door reads as an orange stain**, hard-edged with no falloff. **Fix it in the
  grade**: desaturate and feather it.
- **The sky is paler and earlier than asked**, which helps his silhouette.

**At this size he is anonymous.** The outfit can't be read, so continuity with 9a is carried by the cut.

### 9-walk — the clip · **video** · written 2026-09-14, unrun

**Shot spec (shot-craft):**
- **The world moves and the camera doesn't** (R7, the hybrid method). Any push-in is done in Premiere,
  since the still was framed wide for it.
- **One motion:** he walks steadily down the track towards us. The candle is the only other thing that
  moves.
- 🔑 **He stays far away.** Eight seconds of walking covers about ten metres, so he ends the clip still
  small, well up the rise. **The design keeps him too small to need a face**, which is the whole risk
  managed by geometry rather than by words. The door is never his destination (continue a state, never
  reach one).

**Tab: Frames**, with the accepted round-2 still as the first frame, and here is why:
- **The composition *is* the shot.** Ingredients has rebuilt irreplaceable sets before (§2j.11v phone
  booth, §2j.1 aerial), and a staging failure is unrecoverable.
- ⚠️ **The risk:** on Frames, a walking person is being drawn fresh in every position and has morphed
  before (camping 5a). It's accepted here because he stays small and backlit, and his outfit is in the
  frame-zero pixels.
- ⬜ **30-second free check first:** the Gemini API now takes a first frame *and* a reference image in one
  call (tenth pass, official). Flow's UI blocked that on 2026-08-16, before Omni 1.1. **If the Frames tab
  now lets you add `@Tarquin-new`, add it.**
- **Fallback if he morphs:** Ingredients with the still and `@Tarquin-new`, in the short two-sentence form
  that worked on 2f-5.

**Anti-slop, per tell (tenth pass):**
- **Floaty or moonwalking feet:** real walking speed, feet planting with weight in the mud, arms
  swinging opposite the stride.
- **Slow-motion bias:** *"at real walking speed"*.
- **Candle overdelivery:** one clause, flickering *irregularly*, the flame only.
- **Warping canvas:** no wind and no fabric named. A named breeze moves the yurt wall.
- **Puddle reflections:** not mentioned. He walks the grass strip between the ruts, not through water.
- **A tripod or camera drawn in** (2f-5 revision 3): no camera nouns. *"The view holds perfectly still"*.
- **Speech trap:** no colon after his action and no quotation marks.

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted 9-walk
round-2 still. **No end frame.** **Aspect:** 16:9. **Duration:** 8s. ⬜ Draft at 360p first to judge the
walk.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

The man on the rise keeps walking steadily down the grass strip between the two ruts towards us, at an ordinary walking pace, each foot planting with weight on the wet ground and his arms swinging opposite his stride. He is still a long way off at the end of the shot. Behind the glass in the door, the candle flame flickers irregularly.

Audio: a quiet evening field, a rook calling far off, and the faint squelch of footsteps in wet grass. No music and no voices.

Thanks.
```

**Check before accepting:**
- One man, two legs, feet that plant and don't slide.
- His outline and clothes stay the same from first frame to last.
- The yurt canvas and door don't ripple or re-draw.
- The candle flickers and doesn't turn into a fire.
- No new figures, and the ruts and puddles stay put.
- No camera or tripod appears, and nobody speaks.

### 9-mug — Tarquin holding the mug, the trip plate · **still** · written 2026-09-16, unrun

**Jack, 2026-09-16:** *"we have to make one with a shot of Tarquin holding the mug, then psychedelic
stuff happen around him … the camera in front of Tarquin of the first person pic, showing him holding
the mug and his full body."* It's the reverse of clip 24 (the mug POV at the river dome, see
[`assembly.md`](./assembly.md)), and it lengthens the trip. ⚠️ It's the river-dome location, which the
shot list dropped for the yurt. Clips 24–27 are still in the cut, so this matches the cut, not canon.

**Shot spec (shot-craft):**

1. **Job:** show whose hands those were. Tarquin, alone, pleased with his purchase, standing in a
   place that's about to bend around him. It's a **plate**: the trip happens *around* him, so he
   needs room on every side.
2. **Register:** documentary, human scale. Gate 2 isn't triggered.
3. **Depth:**
   - **Foreground:** the fast shallow stream and its rocks across the bottom of the frame.
   - **Midground:** him on the mossy bank.
   - **Background:** tall spruce going into the mist.
4. **Focal point:** the mug and his face, which win on being centred and on the steam, the only bright
   movement against the dark trees.
5. **Light:** misty early-morning daylight, soft and cool, from the sky. Nothing else, and no warm
   anchor is needed because it isn't a near-black frame. The dome is behind the camera and isn't lit
   into the prompt, since a practical light that far off can't reach him (§20).
6. **Camera:** from the dome's side of the stream, looking back at him. 50mm, about six metres away,
   chest height, level. **He's dead centre**: symmetry is exactly what the kaleidoscope treatment needs
   to mirror around, and the 25.mp4 kaleidoscope is centred too.
7. **Withheld:** the dome. He's looking at it, just past the lens, so only his eyeline says it's
   there.
8. **What moves (for the clip):** steam, the stream, and then the trip. The camera is locked.

**Decisions:**

- 🔴 **Cast `@Tarquin-new` and write nothing about how he looks.** The navy sleeves in the POV match
  its roll-neck.
- **Attach the mug POV frame (clip 24's still) as a reference** for the mug, the moss and the stream,
  and say plainly that this photograph is taken **from the other side of the stream**. Without that
  sentence, a place reference pulls the composition back to the POV. ⬜ **If it comes back as a POV
  again, drop the reference** and let the prose carry the place.
- **The grip copies the POV:** left hand round the body of the mug, right hand through the handle,
  held at chest height. Otherwise the cut from 24 jumps.
- **Expression is muscles, with the wrong readings named:** chin slightly up, eyes over the rim towards
  something past the lens, one corner of the mouth lifted. It's a man who thinks he's got his money's
  worth. **Not serene, not spiritual.** Canon: *"Tarquin doesn't suddenly become some cool spiritual
  guy."*
- **Whole body with moss below his shoes**, because cropped feet get invented in a clip.
- **Stock:** Portra 400, matching 9-walk.

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **Character:** `@Tarquin-new`.
**Reference image:** the mug POV frame (clip 24). **Aspect:** 16:9. **Outputs:** 2.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 400, a single handheld exposure. Visible grain in the shadows, muted cool colour, low saturation, quiet observational tone.

The attached photograph shows this place and this mug from the man's own eyes. This photograph is taken from the other side of the stream, looking back at the man from the character reference as he stands on the mossy bank holding the mug.

Camera and framing: 50mm lens at f/5.6, chest height and level, about six metres from him across the stream. He stands in the centre of the frame, facing the camera, his whole body in frame from the top of his head to his shoes, with a strip of moss below his feet and generous space above and to either side of him. Across the bottom of the frame, close to the lens, the fast shallow stream runs over dark rocks, white water breaking around them.

Action: He holds the stoneware mug from the attached photograph at chest height in both hands, his left hand wrapped round the body of the mug and his right hand through the handle. Thin steam rises from it. He is looking over the rim of the mug at something just past the camera. His chin is slightly up and one corner of his closed mouth is lifted: the look of a man pleased with what he has paid for. He is not serene, not meditative and not smiling broadly, and he is not aware of the camera.

Environment: Behind him, tall dark spruce trees rise out of the moss and fade into thick white morning mist, the nearest trunks sharp and the far ones only pale shapes. The bank is thick green moss and long wet grass.

Light: Soft, cool, misty early-morning daylight from the overcast sky is the only light. It falls evenly on him and the bank, with gentle shadow under his chin and arms. The mist behind him is bright but not burnt out, and the darkest trunks still show their bark.

Details: Real skin texture, wet moss, droplets on the grass, fine natural grain, ordinary and unstyled.

Constraints: Ensure the scene looks like present-day rural Wales. He is the only person in the frame. No tents, domes, lanterns or buildings in the frame. No signs, logos or readable text anywhere in the frame.

Compose for a 16:9 frame.

Thanks.
```

**Check before accepting:**
- It's taken **from across the stream, looking at him**, and not a POV.
- His face and outfit read as `@Tarquin-new`.
- The grip matches clip 24: left hand round the mug, right hand through the handle.
- His whole body is in frame with room around him, dead centre.
- One mug, two hands, five fingers each.
- He looks pleased with himself, not spiritual.

### 9-mug — round 1, **not accepted** (Jack, 2026-09-16: *"he should not be smiling"*)

**What held, so keep all of it:**
- The camera is across the stream, not a POV, so the reference sentence worked.
- He's centred with his whole body in frame and room around him.
- The outfit is right: gilet, roll-neck, turned-up jeans and sock-less tan loafers.
- The stream is in the foreground and the misty spruce are behind him.

**What failed:** he's smiling. 🔑 **The prompt asked for it.** *"One corner of his mouth lifted"* and
*"pleased with what he has paid for"* both describe a smile, and *"not smiling broadly"* names smiling
into the prompt ([negatives backfire](../../google-flow/omni-flash.md#-negatives-do-not-work-and-they-actively-backfire)).

**Round 2 changes the Action paragraph's expression sentences only.** Everything else is word for word
the same. The expression now comes from canon's resting face, *"a man appraising and finding
wanting"*: lips closed and flat, brows faintly drawn together, eyes cool and unimpressed. It's written
only as what the face *is*, with no smile word anywhere.

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **Character:** `@Tarquin-new`.
**Reference image:** the mug POV frame (clip 24). **Aspect:** 16:9. **Outputs:** 2.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 400, a single handheld exposure. Visible grain in the shadows, muted cool colour, low saturation, quiet observational tone.

The attached photograph shows this place and this mug from the man's own eyes. This photograph is taken from the other side of the stream, looking back at the man from the character reference as he stands on the mossy bank holding the mug.

Camera and framing: 50mm lens at f/5.6, chest height and level, about six metres from him across the stream. He stands in the centre of the frame, facing the camera, his whole body in frame from the top of his head to his shoes, with a strip of moss below his feet and generous space above and to either side of him. Across the bottom of the frame, close to the lens, the fast shallow stream runs over dark rocks, white water breaking around them.

Action: He holds the stoneware mug from the attached photograph at chest height in both hands, his left hand wrapped round the body of the mug and his right hand through the handle. Thin steam rises from it. He is looking over the rim of the mug at something just past the camera. His face is still and cool: his lips are closed and pressed flat, his brows are drawn very slightly together, and his eyes are narrowed a little, flat and unimpressed. It is the resting look of a man appraising something and finding it wanting. He is not aware of the camera.

Environment: Behind him, tall dark spruce trees rise out of the moss and fade into thick white morning mist, the nearest trunks sharp and the far ones only pale shapes. The bank is thick green moss and long wet grass.

Light: Soft, cool, misty early-morning daylight from the overcast sky is the only light. It falls evenly on him and the bank, with gentle shadow under his chin and arms. The mist behind him is bright but not burnt out, and the darkest trunks still show their bark.

Details: Real skin texture, wet moss, droplets on the grass, fine natural grain, ordinary and unstyled.

Constraints: Ensure the scene looks like present-day rural Wales. He is the only person in the frame. No tents, domes, lanterns or buildings in the frame. No signs, logos or readable text anywhere in the frame.

Compose for a 16:9 frame.

Thanks.
```

**Check before accepting:** his mouth is flat, with neither corner lifted. The rest is round 1's list.

### 9-mug — round 2 ✅ **ACCEPTED 2026-09-16** (Jack: *"this works"*)

**The mouth is flat** and the look is cool, not smiling. He's centred, with his whole body in frame, and
the stream is in the foreground. The mug is in both hands at his chest, and the misty spruce stand
behind him. **It's a clean plate for the trip clips.** A reference copy, taken from Jack's screenshot
rather than the Flow download, is saved as
[`camera/reference/9-mug-ACCEPTED-screenshot.png`](./camera/reference/9-mug-ACCEPTED-screenshot.png).

### 9-mug trip clips 1–5 · **video** · written 2026-09-16, unrun

**Jack, 2026-09-16:** *"Please do each of these 1 to 5 in order"*: the five trip ideas on the accepted
9-mug still, in this order: timelapse, colour glow, reversed stream, frost, breathing forest. Anti-slop and
Omni research is the [fifteenth pass](../../google-flow/omni-flash.md#fifteenth-pass--2026-09-16-community-vendor).

**Shot spec (shot-craft), shared by all five:**
- **Job:** the trip happens *to the world* while the man at its centre stays exactly who he is, which
  is the *wind your neck in* beat. **The world moves and the camera doesn't** (R7, hybrid method).
  None of the five spends the camera budget.
- **He stays still, but never a statue.** He breathes and blinks, mouth closed (ninth, eleventh and
  twelfth passes). His hands never do anything, because hands holding props are the weak spot.
- **Each effect has something that reacts to it**, and the light on his face stays steady (twelfth
  pass). The exception is the timelapse, where the light change is the point, so it's flagged.

**Tab: Frames, all five.** The composition is the shot, and Ingredients re-stages. He's full-length
and small in frame, and the only change to him is breathing (the tab rule's "both" row).
**Fallback if his face changes:** Ingredients with the still and `@Tarquin-new`, with the scene written
out in full.

**Anti-slop decisions:**
- None of *psychedelic*, *surreal*, *magical*, *neon* or *cinematic*. The colours and the physical
  change are named instead.
- No similes that are nouns (*lungs*, *film*) and no camera nouns.
- Every change is written as phases with a direction of travel. Each is a big change with a small reaction.
- Grain and a 10–15% speed tweak are done in post if needed, not in the prompt. The film grade already
  adds grain.
- **Breath vapour isn't in the frost prompt.** It generates inconsistently, so add it in post (twelfth pass).

**Settings for all five:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted
9-mug still. **No end frame.** 16:9 · 720p · x2 · 8s.

#### 1 · The timelapse, he doesn't age a second

🔴 **The biggest ask of the five.** A human in a timelapse is the documented morph case, so the prompt
says outright that only the world speeds up. **If his face changes, delete the daylight sentence
first** (light moving across a face reads as the face redrawing). Moss over his shoes was dropped:
growth touching him adds a second morph risk.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it as a timelapse. The view holds perfectly still.

Around the man, time runs fast: the mist streams between the tree trunks in quick rolling waves, and the stream smooths into a soft white blur over the rocks. Then the daylight in the forest sinks to a cold blue dusk over a few seconds and climbs back to grey morning. The man alone moves at real speed, standing where he is with the mug, breathing slowly and blinking once, his mouth closed throughout.

Audio: wind rushing through the trees, rising and falling fast, the stream as one continuous hiss, and his slow breathing close by. No music and no voices.

Thanks.
```

#### 2 · The colour floods in

**The safest of the five.** It's a light change with a visible source (the moss), and it stops at his
knees. The palette is violet, blue and gold, matching clip 25's kaleidoscope.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

A soft glow of deep violet and warm gold rises out of the moss at the man's feet and spreads slowly outward across the whole bank, lighting each blade of grass from below and tinting the lowest mist and the legs of his jeans. Then the thin steam rising from his mug turns in on itself in slow curling spirals, catching the violet light. The light on his face stays the soft grey morning light. He stands with the mug, breathing slowly, and blinks once, his mouth closed throughout.

Audio: the stream over the rocks, and a deep soft hum that swells as the glow spreads. No music and no voices.

Thanks.
```

#### 3 · The stream runs backwards

⚠️ **Fluids are the documented weak spot.** A **free fallback that's exact** is to reverse clip
footage of the stream in ffmpeg/Premiere. Reversing the whole clip also reverses his breathing,
which is subtle enough to read as wrong in the right way.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot.

The stream across the front slows down until the white water hangs motionless over the rocks, glassy and frozen in mid-break. Then the water starts to run backwards, upstream, the white water drawing back into the rocks as if time were running in reverse. The man stands with the mug at real speed, breathing slowly, and blinks once, his mouth closed throughout.

Audio: the rush of the stream slows and drains away to silence, then returns as a strange backwards rushing sound. No music and no voices.

Thanks.
```

#### 4 · The cold gets in

The broken car heater, made physical. The frost travels **towards** him and stops at the knees, so
it never reaches his hands or face.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

White frost creeps out from the edge of the stream and spreads across the moss towards the man, stiffening each blade of grass and furring it with ice crystals as it passes, while thin ice forms along the edges of the water. It reaches his shoes and climbs the legs of his jeans to his knees, whitening the denim. As the cold reaches him, his shoulders rise a little and draw in, and he breathes slowly and blinks, his mouth closed throughout.

Audio: the stream, and a fine crackle of ice forming that grows louder as it spreads towards him. No music and no voices.

Thanks.
```

#### 5 · The forest breathes

⚠️ **Warping trunks next to him can drag his outline into the warp.** If his edges ripple, move the
breathing to *"the trees in the mist behind him"* only. *"On the last breath"* is used, not a count,
because counts of repeated events are unreliable (thirteenth pass).

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot.

The two nearest tree trunks on either side of the man swell slowly outward and sink back in the slow rhythm of breathing, and every trunk in the forest behind them swells and eases in time with them. On the last breath the man breathes out with the forest, his shoulders falling as the trunks sink back. He stands with the mug and blinks once, his mouth closed throughout, and the stream keeps running over the rocks at real speed.

Audio: a deep, slow breathing sound all around, as if the forest itself were breathing, over the rush of the stream. No music and no voices.

Thanks.
```

**Check each before accepting, in this order:** hands and mug (one mug, fingers intact), then face
(same man, no smile), then edges (his outline doesn't ripple into the effect). Also check nobody
speaks and no second figure appears.

### 9-mug trip clips, set 2 (ideas 1, 2, 4, 6, 9, 13, 15, 16) · written 2026-09-16, unrun

**Jack, 2026-09-16:** *"Please do 1, 2, 4, 6, 9, 13, 15, 16."* These are from the second ideas list.
Same spec, tab, settings, anti-slop rules and check order as set 1 above.

**Settings for the six Flow clips:** Omni Flash → **Frames** → the accepted 9-mug still as the first frame · no end frame · 16:9 · 720p · x2 · 8s.

#### 1 · The trees lean in

🟡 The nearest trunks are at the frame edges, well clear of him, so the warp shouldn't catch his outline. If it does, keep the bending to the trees behind him.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot.

Every spruce on both sides of the man slowly bends inward towards him from its base, the tops curving over the space above his head, needles shivering and the mist swirling where the branches pass through it. Then the trees slowly straighten back upright. The man stands with the mug at real speed, breathing slowly, and blinks once, his mouth closed throughout, and the stream keeps running over the rocks.

Audio: deep creaking and groaning timber all around as the trees bend, then the stream alone. No music and no voices.

Thanks.
```

#### 2 · The rain falls upwards

🟡 Fast particles, so the shutter clause is in. Rings where the drops leave the water are the surface reacting.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot.

Drops of water lift off the surface of the stream and off the wet moss and rise straight up past the man into the mist, a few at first and then a steady upward rain across the whole frame, leaving small rings on the water where they leave it. Shot at 24fps with a 180-degree shutter, so the rising drops smear into short bright streaks. The man stands with the mug at real speed, breathing slowly, and blinks once, his mouth closed throughout.

Audio: the stream, and the patter of rain growing louder, strangely rising in pitch. No music and no voices.

Thanks.
```

#### 4 · The mist clears in a ring

⚠️ Fog motion is a known weak control (twelfth pass). Here it's the whole shot, so expect a reroll. The sharpening trunks inside the ring are what reacts.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

The mist around the man draws back from him on every side, slowly opening into a clear round space about ten metres across with him at its centre, the tree trunks inside it turning sharp and dark while the mist beyond stays thick and white. Then the wall of mist around the clearing slowly turns, circling him. He stands with the mug, breathing slowly, and blinks once, his mouth closed throughout.

Audio: the stream over the rocks, and a low soft rush of air as the mist pulls back. No music and no voices.

Thanks.
```

#### 6 · Stars in daylight

✅ The light on him never changes: the night sky is only in the top strip. Star trails are a common timelapse subject, so the engine has a reference for them.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot.

Above the trees, the white mist slowly thins until a deep black night sky full of bright stars shows through across the top of the frame, while the forest, the bank and the man below stay in soft grey morning light. Then the stars begin to wheel slowly across the sky in long curved trails. The man stands with the mug at real speed, breathing slowly, and blinks once, his mouth closed throughout, and the stream keeps running over the rocks.

Audio: the stream fades down to near silence, leaving his slow breathing close by. No music and no voices.

Thanks.
```

#### 9 · Ticker tape

🟡 Many small falling pieces, not one object, so there's no single fall for the eye to check. The paper is shredded, not confetti. Watch that none lands on his face or hands.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

Thin strips of white shredded paper begin drifting down through the trees from above, a few at first and then thickly, turning and fluttering as they fall past the man and settle on the moss around his feet. Where the strips land on the stream they darken, soak through and are swept over the rocks as grey pulp. The man stands with the mug, breathing slowly, and blinks once, his mouth closed throughout.

Audio: a soft papery patter all around, and far away a crowd cheering that slowly fades out under the stream. No dialogue and no music.

Thanks.
```

#### 13 · The deer are watching

🔴 Walking animals and new objects are the riskiest ask here (small figures in mist morph). If legs go wrong, drop the walk-in and have the deer already half-visible in the mist, lifting their heads.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

Three red deer walk slowly out of the mist between the tree trunks, one to the left of the man and two to his right, each with a heavy, careful step, and stop at the back of the bank. Then all three lift their heads at the same moment and stare straight at the man, completely still. He stands with the mug, breathing slowly, and blinks once, his mouth closed throughout.

Audio: the stream, a twig snapping under a hoof, then quiet except the water. No music and no voices.

Thanks.
```

#### 15 and 16 · Premiere, no Flow

**Two corrections to the ideas list, found in the catalogue:**
- **15 is `Color Pass` (`PR.ADBE Color Pass`), not "Leave Color".** It keeps one picked colour and
  greys everything else out, so it keys on colour, not on him. Pick the **blue of his jeans and
  roll-neck**. His olive gilet is too close to the moss to keep without the moss coming back too.
  ⚠️ The stream's blue-grey may survive as well, so tighten the similarity until it doesn't.
- **16 is `Replicate` (`AE.ADBE Replicate`), and it tiles the whole frame, man included.** So it's
  a grid of identical Tarquins, not a forest repeating behind one of him. Only the trees would need a
  mask around him. ⬜ It's unrecorded whether the bridge can draw a mask.

**Needs:** a finished clip on the timeline. Neither the still nor any trip clip is imported yet.

### 9-plea — the bad trip, one clip per line of the plea · **video** · written 2026-09-16, unrun

**Jack, 2026-09-16:** *"we need to make the trip about this, so can you depict this in the videos in
pyschedelic bad trip vibes."* The plea:

> Please. I only wanted to make money. That's allowed. / I did all the steps. The school, the
> university, the job. Everyone said well done. / I didn't crash anything. I just saw it coming.
> That's the job. / And the flats… I bought them. I just didn't put anyone in them. / I never meant to
> hurt anyone. I never even met them.

**This is now the trip's spine.** The earlier sets (1–5 and set 2) are spare coverage.

**Research (2026-09-16), what it changed:**
- **Bad trips are paranoia, guilt, being watched, and the world distorting as the inner state leaks
  outward** (Grof: *"you perceive a sort of distortion of the world out there"*), with time distortion and
  surfaces breathing. The film grammar is **dread by suggestion**: things in the corner of the eye
  (*Jacob's Ladder*), warping surfaces and distorted sound (*Fear and Loathing*), POV plus internal
  thoughts (*Enter the Void*).
- **The AI-horror advice agrees with the house rules:** describe what feels *wrong*, not what's scary.
  Use silhouettes and fog for presences, and a **long sustained low tone** instead of jump scares.
  Don't use "spooky" words. **Good things turning wrong** (applause that goes on too long) unsettle
  more than monsters.
- 🔴 **No strobing.** It's a bad-trip cliché, and it fails the [photosensitivity
  gate](../../video-fx/delivery.md).

**Shot spec (shot-craft), all five:**
- **Job:** each clip is one line of his excuse, **disproved by the world around him**, while he stands
  still. The picture argues back against the voiceover. This is irony paired with an on-screen
  consequence (story-craft).
- **He never emotes** (canon: *"we never animate a character emoting"*). His **breathing is the only
  escalation**: slow, then a little quicker, then quicker, then fast and shallow. His mouth stays
  closed, so the plea is plainly in his head.
- **The world moves and the camera doesn't** (R7). The light on his face stays steady wherever the
  effect allows.
- **Every image is from his own record:** money, the ladder he climbed, 2008, the empty flats, the
  people. No AI and no preview of the future.

**Tab and settings:** Omni Flash → **Frames** → the accepted 9-mug still as the first frame for **all
five** · no end frame · 16:9 · 720p · x2 · 8s. All five start from the same still so a failure costs
one
clip. ⬜ **Option:** chain them, each clip's last frame into the next, so the trip builds up. It's
stronger, but drift adds up.

**Premiere layer (the escalation belongs here, not in the prompts):**
- The grade drains a little sicker with every clip, going cool green-cyan in the shadows.
- `Liquid Distortion` and `RGB Split` creep in only on D and E.
- A low drone bed runs under all five.
- Reverb grows on his voiceover.
- **After E, cut in 4–6 frames each of faces we already have:** Bob, the man at the next desk (1m),
  and the shoppers walking past (6b). ⚠️ Run `scripts/photosensitivity-check.py` on that stretch.

#### A · "I only wanted to make money. That's allowed." · the stream turns to gold, then sludge

🟡 Fluids. A slow thickening is appearance, not a splash, so it's the easier class. The blackening moss is the reaction.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot.

The white water in the stream slowly thickens into molten gold, running heavier and slower over the rocks until it clogs between them. Then the gold dulls and darkens to a grey sludge, and the moss along the edge of the stream blackens where the sludge touches it. The man stands with the mug at real speed, breathing slowly, and blinks once, his mouth closed throughout.

Audio: the rush of the stream turns into a thick metallic trickle of coins, then a low sustained hum underneath. No music and no voices.

Thanks.
```

#### B · "I did all the steps." · the stones rise into steps that lead nowhere

🟡 Several objects moving at once. If the steps come out mangled, cut to the rocks rising only and let the applause carry *well done*. The applause is a sound effect, not speech.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot.

One after another, the rocks in the stream rise up out of the water with water pouring off them and settle into a flight of stone steps that climbs past the man's right side and on up into the mist, where the top step ends in empty white. The man stands with the mug at real speed, his breathing a little quicker, and blinks once, his mouth closed throughout.

Audio: the grinding of heavy stone and water pouring off it, then slow applause from somewhere in the mist that goes on too long, each clap slower and further away. No music and no voices.

Thanks.
```

#### C · "I didn't crash anything. I just saw it coming." · the flood goes round him

✅ Water spreading across flat ground is the easy fluid class (like 1y's tide). 🔑 **It's canon made literal:** he came out of 2008 without a scratch while everyone else went under.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

The stream swells and spills over its banks, and dark water spreads steadily across the moss on both sides of the man, flattening the grass and rising around the trunks of the trees, darkening the bark where it climbs. The small mound of moss he stands on stays dry, and the water flows around it on every side. He stands with the mug, breathing quicker, and blinks once, his mouth closed throughout.

Audio: the rising roar of flood water all around, and under it a deep low rumble. No music and no voices.

Thanks.
```

#### D · "And the flats… I just didn't put anyone in them." · the tower blocks go dark

🔴 Rows of distant windows can crawl, and it gets worse when upscaled (thirteenth pass). The fog softening them is the counter. If they crawl, delete *"row by row"* and let them go dark together. The light on him stays steady.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot.

Deep in the mist behind the trees, the dark shapes of tall concrete tower blocks slowly loom into view, softened by the fog. Their windows glow a dim warm yellow, and then, row by row from the top down, every window goes dark until the blocks stand black and empty behind the trees. The light on the man stays the soft grey morning light, and he stands with the mug at real speed, breathing quicker, and blinks once, his mouth closed throughout.

Audio: the stream, a low wind moaning between high buildings, and a soft click as each row of windows goes dark. No music and no voices.

Thanks.
```

#### E · "I never meant to hurt anyone. I never even met them." · the people he never met

🔴 **Faces hidden by distance and fog, never by a sentence** (nano-banana-2 §18). They're ordinary people (a mother, an old man, a worker), not a homeless stereotype (the-reader rule 4). If any face resolves, move them further back into the fog.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

The mist between the trees behind the man slowly thins, showing ordinary people standing among the trunks as dark silhouettes against the white: a woman holding a small child's hand, an old man in a flat cap, a man in a work jacket, and more further back. They stand completely still and all face towards him, too far away and too softened by the fog for any face to be seen. The man stands with the mug, his breathing fast and shallow, and blinks once, his mouth closed throughout.

Audio: the stream fades away to silence, leaving only a low sustained tone and his fast, shallow breathing close by. No music and no voices.

Thanks.
```

**Check each before accepting, in this order:** hands and mug, then face (same man, mouth closed,
not acting scared), then his outline, then no readable text and nobody speaking.

**Sources:** [Bad trip, Wikipedia](https://en.wikipedia.org/wiki/Bad_trip) ·
[whatNerd, trippy drug films](https://whatnerd.com/trippy-drug-movies-psychedelic-experiences/) ·
[Jacob's Ladder (1990)](https://en.wikipedia.org/wiki/Jacob%27s_Ladder_(1990_film)) ·
[Kling, horror prompts](https://kling.ai/blog/horror-ai-video-prompts-color-grading-sound) ·
[ZSky, horror prompts](https://zsky.ai/blog/ai-horror-art-prompts) ·
[PMC, extended difficulties after psychedelics](https://pmc.ncbi.nlm.nih.gov/articles/PMC10597511/)

### 9-plea — round 2, **too subtle** (Jack, 2026-09-16) · rewritten BIG · written 2026-09-16, unrun

**Jack:** *"the ones before have been too subtle, this is the strongest psychedelic known to man, it
should make a big impact visually."* Round 1 was built to keep the frame (small asks keep the
frame). **This round deliberately trades frame-lock for impact** ([the change/adherence
trade](../../google-flow/omni-flash.md#️-the-changeadherence-trade-is-a-straight-line)). Expect more
redraws of the set, and possibly of him.

**What changed:**
- 🔑 **A shared trip layer opens every clip within the first second:** colours flood to full
  intensity (acid-green moss, violet and magenta mist) and glowing geometric lattice patterns spread
  over every surface. **Research:** ayahuasca visions typically begin with colour intensifying and
  geometric patterns building in complexity. Serpents are the most reported motif (Shanon), so C's
  flood now coils round him like a serpent.
- ⚠️ **Not copied from Shipibo kené designs.** Those are a living people's sacred textile art. The
  prompt says *"geometric lattice"*, generic.
- **Each plea image goes from a background change to a world-scale event:** a gold river that rots
  to black sludge, a colossal staircase crumbling as it climbs, a flood wall that splits around him,
  tower blocks bursting out of the forest and going black, and a forest packed with silhouettes who
  step towards him together.
- **What doesn't change:** he stays centred, holds the mug and never acts scared. His breathing is
  now hard throughout. No strobe (colours *pulse slowly*) and no saturated red.
- **Premiere can push it further for free:** `Kaleido` mirrored around him, `Liquid Distortion`, `Echo
  Glow`.
- **Fallback if his face goes:** Ingredients with the still and `@Tarquin-new`, with the scene
  written out. Or accept a redraw and cut away before his face reads.

#### A · money · the gold river rots

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

Within the first second every colour in the forest floods to full intensity: the moss turns acid green, the mist blazes violet and magenta, and glowing geometric lattice patterns spread across the trunks, the rocks and the ground, pulsing slowly. Then the stream erupts into a surging river of molten gold that pours uphill into the trees, gilding every trunk and branch until the whole forest shines gold. Then the gold rots: it blackens and melts, and thick black sludge drips from every branch and rains down around the man. He stands in the centre with the mug, breathing hard, and blinks, his mouth closed throughout.

Audio: a roaring rush of pouring metal and the clatter of countless coins, then a deep wet dripping under a low droning hum. No music and no voices.

Thanks.
```

#### B · the steps · a staircase to nowhere

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

Within the first second every colour in the forest floods to full intensity: the moss turns acid green, the mist blazes violet and magenta, and glowing geometric lattice patterns spread across the trunks, the rocks and the ground, pulsing slowly. Then the rocks tear out of the stream and fly upward, stacking into a colossal stone staircase that spirals up past the man and into the sky, hundreds of steps high above the trees and still climbing. As fast as new steps form at the top, the lowest steps crumble and crash back into the stream in showers of stone and spray. He stands in the centre with the mug, breathing hard, and blinks, his mouth closed throughout.

Audio: grinding stone and crashing water, and thunderous applause from everywhere at once that slows and deepens into a long low groan. No music and no voices.

Thanks.
```

#### C · 2008 · the flood splits round him

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

Within the first second every colour in the forest floods to full intensity: the moss turns acid green, the mist blazes violet and magenta, and glowing geometric lattice patterns spread across the trunks, the rocks and the ground, pulsing slowly. Then a towering wall of dark floodwater surges through the forest from both sides at once, bending the trees and swallowing the bank, and rears high above the man before splitting around the small mound of moss he stands on. The water coils around his mound like a vast serpent, circling him faster and faster in churning walls that rise on every side, while he stays completely dry in the middle. He stands in the centre with the mug, breathing hard, and blinks, his mouth closed throughout.

Audio: the thundering roar of floodwater all around and a deep rumble shaking through it. No music and no voices.

Thanks.
```

#### D · the flats · the blocks go black

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

Within the first second every colour in the forest floods to full intensity: the moss turns acid green, the mist blazes violet and magenta, and glowing geometric lattice patterns spread across the trunks, the rocks and the ground, pulsing slowly. Then tall concrete tower blocks burst up out of the ground all around the man, splitting the trunks and throwing up earth, growing floor by floor into the sky until they tower over him on every side. Every window blazes with warm yellow light, then all at once every window goes black, and the dark, empty blocks lean in over him. He stands in the centre with the mug, breathing hard, and blinks, his mouth closed throughout.

Audio: cracking wood, grinding concrete and deep booming as the blocks rise, then a sudden hollow silence with a low wind moaning between them. No music and no voices.

Thanks.
```

#### E · the people he never met

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

Within the first second every colour in the forest floods to full intensity: the moss turns acid green, the mist blazes violet and magenta, and glowing geometric lattice patterns spread across the trunks, the rocks and the ground, pulsing slowly. Then the mist tears open and the forest is packed with people as far as the eye can see, hundreds of ordinary men, women and children standing shoulder to shoulder between the trunks as dark silhouettes, their outlines glowing with shifting violet light, all facing the man. Then every one of them takes a single step towards him at the same moment, and the glowing patterns on the ground rush inward to his feet. He stands in the centre with the mug, breathing hard, and blinks, his mouth closed throughout.

Audio: a deep drone rising to a roar, and hundreds of footsteps landing at once. No music and no voices.

Thanks.
```

**Sources:** [Shanon, ayahuasca visualizations typology](https://www.researchgate.net/publication/233569909_Ayahuasca_visualizations-A_structural_typology) ·
[Dr James Cooke, ayahuasca visions](https://www.drjamescooke.com/read/aya-visions) ·
[Psychedelic Times, archetypes](https://psychedelictimes.com/the-universal-archetypes-of-ayahuasca-dreams-and-making-sense-of-your-own-visions/)

---

## Scene 10 — the wake-up, five years on

### 🖼 The plate — `camera/reference/scene-10-ruined-car-park-plate.png`

**Banked 2026-08-28.** The tent-POV out into the ruined car park, generated before this entry
existed. It is now **the master frame for the whole 10–12 block**, the same way the scene-8 X8
frame was the master for 6c.

⚠️ **The chain runs the other way now, and this needs a ruling.** `shot-list.md` says
*6c → 10a, by inheritance, never rebuilt from words*. This plate was not derived from 6c — its
doorway is a tall rounded arch left of centre with a second fabric panel on the right, where 6c
is a **letterbox** with a low horizon. **Both cannot be true.** The cheap resolution is to accept
this frame as the master (it is the better picture and 10–12 all live in it) and **re-derive 6c
from it**, which is the direction the film's other chain already ran. Until that is done, the
jump rhyme is not guaranteed. *(Raised 2026-08-28, unresolved.)*

**What the plate settles:** the bottle-in-hand foreground carries over from 6c and the scene-8
master, so the hand is continuous across the jump — but on Tarquin it now reads *he has been
here a while*, which is the opposite of a man who just woke. **Ruling owed** (see `shot-list.md`).

### 10a/10b — the dead car park · **still** · written 2026-08-28, unrun

**Reference:** the scene-10 plate, one image, nothing else. **No Character cast** — there is no
face in the frame ([§12](../../google-flow/nano-banana-2.md)), and the figures at the fires are
deliberately silhouettes ([§18](../../google-flow/nano-banana-2.md): hide a face with geometry,
never with a sentence).

**The four changes, and why each one is written as a consequence rather than an instruction.**

1. **Every electric light dead.** Jack's note. Written with its consequences — no pool under the
   lamp heads, the store frontage a black slab — because
   [§9](../../google-flow/nano-banana-2.md) says a strong reference meets a bare change-list
   halfway, and *"it is now night"* comes back as blue hour.
2. **🔴 The physics has to close, or the engine invents fill.**
   [§20](../../google-flow/nano-banana-2.md), confirmed on 9a the day before: kill every source
   and the model rebuilds the scene so the picture becomes possible. So the prompt **hands it the
   ambient on our terms** — the overcast dusk sky lights the car park flat and cold from above,
   and the drum fires are the only warm light, low and thrown upward with a short reach. Two real
   sources, both able to do the job named. **Do not answer a bad round with more falloff
   language** — that is the documented trap.
3. **The broken fascia carries the W-AI-trose gag.** Two letters still lit, everything else dead.
   This resolves the open call in `shot-list.md` by landing the gag **in 10a, inside the rhyme**,
   and it is also the cheapest fix for a real defect: the accepted plate's fascia reads
   *"Woitrose"*, and killing the letters kills the mangled letterforms. ⚠️ **It also de-risks
   [trigger 1](../../flow/failure-modes.md)** — the prompt never writes the brand name and never
   asks for a legible real wordmark, only two quoted letters on a wrecked sign.
4. **The camp is re-dressed British.** The plate reads as tarpaulin, oil drums and washing lines —
   the grammar of a refugee camp, which hands our reader the wrong cause for free
   ([`the-reader.md` rule 4](../../marketing/the-reader.md); the picture version of gate 2 in
   [`cinematography/symptoms.md` §E](../../cinematography/symptoms.md)). Replaced with ordinary
   high-street camping gear, shopping trolleys repurposed, and a split office swivel chair by a
   fire. **It should read as a middle-class car boot sale that never went home.**

**Plus one addition that does the most work for its length:** buddleia woody in the cracked
tarmac. It dates the shot without a word of narration, which is the entire job of the jump.

**Deliberately NOT in the prompt.** Smoke, haze and steam — the atmosphere family arrives free and
overdelivers the moment it is named ([§10](../../google-flow/nano-banana-2.md)); the plate already
has it. No weather noun either: the reference carries the wet, and the style paragraph is dropped
because the reference carries the look ([§2](../../google-flow/nano-banana-2.md)).

**Settings:** Enhance Prompt **off**. **2K or 4K** — 1K blurs small text and two letters have to
survive ([`image-prompting.md` §5](../../flow/image-prompting.md)).

```prompt
Use the attached image as the reference for this shot. Keep the camera exactly where it is, and keep the whole inside of the tent exactly as it is: the same doorway opening at the same shape, size and place in the frame, the same fabric, seams, zip tape, mesh panel and patch, the same bedding across the bottom of the frame, the same empty bottles and cans lying on it, and the same forearm and hand holding a bottle at the lower left. Keep the geography beyond the doorway: the same wet cracked tarmac and puddles, the same broken glass, the same lamp columns in the same places, the same line of shelters away to the left, and the same supermarket frontage on the right.

Change the following.

Every electric light in the picture is dead. The lamp columns are cold dark metal with unlit glass heads, throwing no light at all and casting no pool of light on the tarmac beneath them. The supermarket behind its glass is completely black — no lighting inside, no glow at the windows, nothing visible through them — so the whole frontage reads as one dark slab beneath its sign.

The sign's illuminated lettering is broken. Most of the letters are dead: their tubes cracked, their casings stained and streaked, one letter hanging loose from a bracket and another fallen away entirely, leaving a paler unweathered scar on the panel behind it. Only two letters still have power, the "a" and the "i", and they burn a hard flat green, slightly too bright and slightly unsteady, the one machine in the picture still working.

The shelters are ordinary British high-street camping gear that has been lived in for years: faded dome tents and pop-ups in supermarket colours, one of them collapsed in on itself, guy lines tied off to shopping trolleys and to the concrete feet of the lamp columns, and bin bags and cheap woven shopping bags weighted around the skirts to hold them down. An office swivel chair with its foam split open stands beside one of the fires. Two shopping trolleys are in use, one as a washing rack and one as a barrow.

Buddleia and coarse grass have grown up through the cracks in the tarmac and around the bases of the lamp columns, established long enough to have gone woody, so the place reads as years abandoned rather than days.

Light: there are only two sources. The pale overcast dusk sky above is the ambient — cold and flat, laying a low blue-grey level across the whole car park with no bright highlight anywhere in it. The fires burning in the drums are the only warm light, and they sit low, so everything they reach is lit steeply from below: the undersides of the nearest tent fabric, the rims of the drums, and a short pool of orange on the wet tarmac that dies out within a few metres. Beyond the reach of the fires the car park falls away to near-black. The two lit letters on the sign are far too small and too far off to light anything.

The people at the fires are distant and bent over the drums with their backs to us, reading only as dark shapes against their own firelight.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates, in this order:**

1. **Are the lamps and the store actually dark**, with no invented fill on the tarmac? This is the
   change most likely to be met halfway.
2. **Do only two letters burn**, and do they read as `a` and `i`?
3. **Does the camp read British** — dome tents and trolleys, not tarpaulin and jerry cans?
4. **Did anyone at the fires grow a legible face?** An invented face is an uncast character and
   costs more than a re-roll ([§18](../../google-flow/nano-banana-2.md)).
5. Only then: is the doorway still the plate's doorway?

⚠️ **This prompt sits on [trigger 3](../../flow/failure-modes.md) — stacked destitution.** Burning
drums plus a tent city plus an identifiable supermarket is the exact combination named. **If it
blocks, one change per run, never a re-roll unchanged:**

1. `The fires burning in the drums` → *the fires burning in their metal bins*
2. Cut the sentence about the people at the fires entirely — the frame does not need them
3. `supermarket frontage` / `supermarket` → *the shop frontage* / *the shop*

### 10a/10b — round 1, not accepted: the lights went out and the picture got flatter

Run 2026-08-28. Frame banked at
[`camera/reference/scene-10-round2-lights-out.png`](./camera/reference/scene-10-round2-lights-out.png).
Jack: *"Not much changed, the sign is now on and it doesn't look that much better."*

**What landed:** the lamp heads are dark and throw no pools, the shop interior is black, the
swivel chair and the buddleia are in. **What did not:** the sign, and the picture.

#### 🔴 The diagnosis: killing the lights removed the anchor and left mid-grey

[`symptoms.md` §A](../../cinematography/symptoms.md), three rows at once — *"I don't know where
to look"* (no focal point, everything at the same visual weight), *"the dark bits look grey, not
black"* (diffusion models pull toward mid-grey; near-black is structurally uphill), and
*"it doesn't feel lit by anything."*

**The cause is a design error in the prompt, not a wording error.** The lamps and the shop were
the only bright anchors in the plate. The prompt removed both and replaced them with **four small
equal fires spread across the frame** — which is four focal points, i.e. none. Nothing in the
picture is black and nothing is bright; the whole exterior sits inside about two stops, and the
brightest thing left is a flat pale sky.

[`frame.md`](../../cinematography/frame.md): **one bright anchor inside the darkness, always** —
the visual system measures darkness against the brightest region it can group into the same
scene. Take the anchor away and you do not get night, you get murk. **This is the highest-value
fix in that file and we broke it deliberately.**

**So the fix is not more darkness. It is one big close fire**, which supplies all four missing
things at once: a focal point, a warm key against a cold ambient, real falloff into real black,
and a lit midground where there is currently a grey void.

#### 🔴 The sign: two failures, so stop asking Flow for it

Round 1 asked for a five-part lettering operation — cracked tubes, one letter hanging, one fallen,
a scar on the panel, two named letters still lit — against a reference showing a clean lit sign.
**The engine ignored all of it and kept the reference.** That is
[§9](../../google-flow/nano-banana-2.md) (a strong reference wins ties) compounded by
[§8](../../google-flow/nano-banana-2.md) (length costs adherence), and the standing fix when a
shot is not landing is **to remove a clause, not add one.**

**Ruled 2026-08-28: the W-AI-trose gag is a post job, not a Flow job.** It is load-bearing text,
and [`image-prompting.md` §5](../../flow/image-prompting.md) already says load-bearing words
belong in the overlay rather than the pixels — sharper, editable, and impossible to policy-block.
[`CLAUDE.md`](../../../CLAUDE.md) puts on-screen text in the **ffmpeg** lane for the same reason.

**The new division of labour:** Flow renders the sign as **one simple state — dead** (a single
physical fact it can actually hold), and the two lit letters are composited afterwards. That also
makes the gag identical across every shot in 10–12 instead of re-rolled each time, and it takes
the brand wordmark out of the prompt entirely. The prompt now asks the fascia to stay a *slightly
paler band* so the comp has a surface to sit on.

### 10a/10b — round 2 · **still** · written 2026-08-28, unrun

**Reference:** the round-1 frame above (it is now the closest thing to right). One image.

**Four changes and nothing else — the prompt is deliberately ~40% shorter than round 1.** The
keep-list is cut to the camera, the tent interior and the hand, because everything it was
protecting outside is being changed anyway, and a long keep-list is attention the change-list
is not getting.

1. **One drum fire moved close and burning hard — the key light.** Written with its consequences
   (a pool that reaches the tent mouth, the broken glass catching points of light, everything
   black within ten metres) because [§9](../../google-flow/nano-banana-2.md) says a bare change
   gets met halfway. The physics closes — a drum fire at four metres genuinely lights that much,
   which is what [§20](../../google-flow/nano-banana-2.md) demands.
2. **Real blacks.** The instruction that does the work is not *"darker"* but *"solid black shapes
   with no detail in them at all"* — a consequence, not an adjective.
3. **The sign dead**, as one state.
4. **Rain, visible only where it crosses the firelight.** [§17](../../google-flow/nano-banana-2.md):
   streaks need a source, and until now there wasn't one. Still an exterior element only — the
   6c ruling that rain on the lens is physically impossible inside the tent stands.

**Plus a figure at the near fire, in silhouette.** It is the focal point, the scale reference and
[gate 2](../../cinematography/principles.md)'s visible cost in one object. **Backlit with their
back to camera** — two geometric locks, per [§18](../../google-flow/nano-banana-2.md): hide a
face with the camera and the light, never with a sentence.

**Dropped from round 1, on purpose:** the buddleia and the swivel chair (both landed — restating
them competes with the reference, [§2](../../google-flow/nano-banana-2.md)), and the long light
paragraph.

**Settings:** Enhance Prompt **off**. 2K is now fine — no text has to survive.

```prompt
Use the attached image as the reference. Keep the camera exactly where it is, and keep the inside of the tent exactly as it is: the same doorway, the same fabric, mesh panel and patch, the same bedding, bottles and cans across the bottom, and the same forearm and hand holding a bottle at the lower left. Keep the layout of the car park beyond it.

Change the light, and change it a long way.

One of the burning drums has been dragged close. It stands three or four metres beyond the doorway, off to the right, and it is burning hard, with flames standing well above the rim. It is the only real light in the picture. It throws a strong orange pool across the wet tarmac that reaches as far as the mouth of the tent, lights the inside edge of the doorway and the nearest folds of the bedding, and rakes low across the field of broken glass so that every piece catches its own point of light. The light falls off fast: ten metres past the drum there is nothing left of it.

It is an hour later than in the reference and nearly dark. The sky has gone deep blue-black, with the last of the daylight only in a narrow band low down at the horizon. Everything not reached by the fire is a solid black shape against that sky with no detail inside it at all: the shop front is a black colonnade, the lamp columns are black poles, the far tents and the far side of the car park are one black mass. There is no other light anywhere in the frame — no lit windows, no lamps, no glow on the horizon.

The sign above the shop front is dead. It is unlit, grimed and weather-streaked, and it reads only as a slightly paler grey band along the top of the black frontage, with no colour and no letters that can be made out.

Standing at the near drum with their back to the camera, a single figure, close enough to stand about as tall as the doorway opening. The fire is between them and the far side of the car park, so they are lit only along their edges and are otherwise a solid black shape with nothing legible inside their outline.

Fine rain is falling. It shows only where it crosses the firelight, as bright streaks close to the drum, and is invisible everywhere else.

The shelters beyond are ordinary British high-street dome tents and pop-ups.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates, in this order:**

1. **Is there one obvious place to look?** If the eye still wanders, the fire is not big enough or
   not close enough — push it closer before changing anything else.
2. **Is anything in the frame actually black?** Cover the fire with a thumb; the rest should read
   as shapes, not as grey texture. This is the round-1 failure and the one to be strict about.
3. **Does the fire's pool physically reach the tent mouth**, and does the broken glass carry it?
   That is the midground being filled, which is what the round-1 frame has a void where.
4. **Did the figure stay a silhouette**, with no face and no legible detail?
5. **Is the sign genuinely dead** — no green anywhere?

**If it comes back flat again, the next change is time of day, not wording.** Full night with the
fire as the only source. Do not spend another round writing the falloff harder — that is the
documented trap ([§20](../../google-flow/nano-banana-2.md)).

### 10a/10b — round 2, accepted as the look · 🔒 the new master

Run 2026-08-28. Frame:
[`camera/reference/scene-10-round2-ACCEPTED.png`](./camera/reference/scene-10-round2-ACCEPTED.png).
Jack: *"This looks amazing… I like the fire popping because of the darkness and the ominousness,
the guy with the hoodie with his back turned to the camera, I like all of it."*

**Every element of the redesign landed.** One close drum fire as the key; real blacks; rain
showing only where it crosses the firelight; a hooded figure holding as a pure silhouette with no
face. **The round-1 failure is closed, and the fix was a lighting *design* change, not better
wording** — worth remembering next time a frame reads flat.

#### 🔴 Gate 1, stated by Jack and now canon: this shot's job is RECOGNITION

> *"This is supposed to be a big reveal that he is in a similar position as Bob — this is the same
> car park he is in, in the future."*

**That is the first time the shot's job has been written down, and it changes two things.**

1. **The location has to be legible**, which is the whole reason for round 3 below. A reveal the
   audience cannot read is not a reveal.
2. **🔴 It promotes the open doorway-chain ruling from tidiness to a dependency.** Recognition is
   carried by the *framing rhyme* with 6c far more than by any sign — the audience is being asked
   to notice they have sat in this doorway before. The scene-10 plate is **not** derived from 6c
   (arch versus letterbox), so right now the rhyme is hoped for. **Re-derive 6c from this accepted
   frame** and the reveal works with no signage at all; leave it and the shot is carrying a job its
   composition does not support. *(Raised again 2026-08-28 — this is now the highest-value open
   item in scene 10.)*

### 10a/10b — round 3 · **still** · written 2026-08-28, unrun

**Reference:** the accepted round-2 frame. **One change only — the sky.**

**Why one change.** Round 2 is right and the risk in touching it is that a global exposure lift
returns the round-1 mush. So the prompt raises **one named source** and then explicitly pins the
level of every region that must not move, with the hierarchy stated as a fact —
*"the fire is still by far the brightest thing in the picture."*

**The sign: readable, and still dead.** The [2026-08-28 ruling](#10a10b--round-1-not-accepted-the-lights-went-out-and-the-picture-got-flatter)
stands — Flow renders one simple state and the two lit letters are a post comp. Round 3 asks for
the fascia to catch the sky as a **pale grimy band with the shop's name across it in unlit
letters, dark against the panel**. That gives three things at once:

- **Recognition** — the word is legible in dark relief, so the place is identified.
- **A comp surface** — a flat panel with known letter positions, so the two green letters drop on
  cleanly and identically across every shot in 10–12.
- **The gag at full strength** — two lit letters on a dead fascia, in a frame this dark, become the
  second brightest thing in the picture after the fire. Brighter than a fully lit sign ever was.

⚠️ **The brand name is never written in the prompt** — the reference carries the word, and asking
for a legible real wordmark is [trigger 1](../../flow/failure-modes.md), the most reliable block
there is.

**Settings:** Enhance Prompt **off**. **4K** — the letterforms have to hold their shape for the comp.

```prompt
Use the attached image as the reference. Keep everything in it as it is: the same camera position, the same tent interior, doorway, bedding, bottles and the same forearm and hand holding a bottle at the lower left; the same burning drum in the same place with the same flames; the same hooded figure standing with their back to the camera, still lit only along their edges and still a solid black shape with nothing legible inside their outline; the same falling rain; the same wet tarmac, puddles and broken glass; the same lamp columns, unlit.

Change one thing: the sky.

It is a little earlier in the evening. The sky is a deep blue that still holds real light in it, brightest in a wide band low across the horizon behind the buildings. That light is enough to separate the far side of the car park from the sky, so the shop front on the right now reads clearly as a building: the line of its roof, the row of columns along its frontage, and the long horizontal sign panel above them, which catches the sky and sits as a pale grimy band. The shop's name runs across that panel in unlit letters, dark against the paler panel, its shape readable but giving off no light of its own. There is still no light inside the shop and no lit window anywhere.

Everything else keeps its level. The fire is still by far the brightest thing in the picture and still the only warm light; the tent interior, the ground in front of the doorway and everything beyond the reach of the fire stay exactly as dark as they are now.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates:**

1. **Is the fire still the brightest thing?** If the frame has lifted globally, reject — that is
   round 1 coming back and it is the only real risk in this change.
2. **Can you read the shop's name** in dark relief on the panel?
3. **Are the tent interior and the near ground still black?**
4. **Did the hooded figure stay a silhouette**, and is the rain still only visible against the fire?

**If the whole frame lifts, do not ask for it darker again** — pin the sky as *"a deep blue with a
band of light only behind the buildings on the right, and no light at all in the upper half of the
sky"*, so the lift has one place it is allowed to happen.

### 🔒 10a/10b — the lightning reveal · **design ruled 2026-08-28**

**Jack's idea, and it is the best version of this shot yet:** keep the dark frame, and in the
video **a lightning strike lights up the sign to reveal it.**

**Why it beats both earlier plans.** Round 3 was going to lift the ambient so the sign reads,
which buys recognition at the cost of the darkness that makes the frame work. The flash buys
both, and it **sequences** them — which is the thing a static frame could never do:

| Beat | What the audience gets |
| --- | --- |
| **1. The dark frame holds.** Fire, rain, the hooded man, near-black. | *Where is he?* The question is open. |
| **2. FLASH — two or three frames.** The whole car park, hard and cold, the supermarket right there, the name legible. | **Recognition.** He is in Bob's car park. |
| **3. Back to dark.** Two green letters still glowing on the dead fascia. | **`AI`.** The thesis, delivered last. |

That is a three-stage reveal in about a second and a half, and the film's whole argument is in
stage 3. [`stills.md`](../../cinematography/stills.md) and principle 25 both say the same thing —
**withhold, and let the viewer's understanding lag the image.** A sign that is simply visible from
frame one cannot do that.

It also **spends the motion budget correctly.** [`shot-list.md`](./shot-list.md)'s standing rule
allocates animation to the blink, the fire and the embers; a light changing inside a locked frame
is not a camera move and does not spend the budget. And the flash is **motivated** — it is already
raining hard in the plate, which is [§20](../../google-flow/nano-banana-2.md)'s requirement met
before it is asked.

#### 🔴 Do not ask Flow for the flash. It is three layers, and only one of them is Flow's.

[`hybrid-method.md`](../../video-fx/hybrid-method.md) — the lanes are layers, and **ffmpeg owns
anything that must be exact.** A flash that has to hit a narration beat and reveal specific
lettering is the definition of exact. Worse, it is the one thing the engine is documented to fail:
**Veo cannot hold text steady through a change** ([`image-prompting.md` §5](../../flow/image-prompting.md)),
and a global lighting change is exactly what makes a model re-render everything in frame.

| Layer | Lane | What it is |
| --- | --- | --- |
| The dark clip | **Flow** | The accepted frame, animated: fire flicker, rain, the figure shifting his weight. **Camera locked. No lighting change.** |
| The lit frame | **Flow** | One still — the same frame under the flash. Prompt below. |
| The flash itself | **Premiere / ffmpeg** | A 2–3 frame cut or fast dissolve to the lit still and back. Exact, free, re-timeable. |
| The two green letters | **ffmpeg** | The comp already ruled on 2026-08-28. Sits on the dead fascia after the flash. |
| Thunder | **post** | Synced. Not generated — the delay between flash and thunder is the free realism. |

⚠️ **Physics check: lightning cannot light only the sign.** It is a huge distant source and it
lights the whole car park hard and cold from one direction. That is *better* — for two frames the
audience sees the full extent of the camp — but it means the lit frame is a **whole second
generation**, not a grade. **Do not try to lift the dark plate in post**: raising a near-black
frame produces noise, not a lit scene.

🔴 **Mandatory before delivery: run ffmpeg's `photosensitivity` filter** on the finished sequence.
[`hybrid-method.md`](../../video-fx/hybrid-method.md) line 152 — *"run it on any strobing or alarm
sequence before delivery"*, and Premiere has nothing equivalent. A hard 2-frame flash is exactly
what it exists for.

### 10b(ii) — the lightning frame · **still** · written 2026-08-28, unrun

**Reference:** the accepted dark frame. **One change: a lightning flash is happening.** Everything
else in the picture is identical, because the two frames have to intercut on the same sprocket.

**The sign does not need to be powered.** Under a flash it is *illuminated*, so the ask collapses
to one simple state — a fascia panel and dark lettering revealed by an external light. That is the
single-state instruction [§21](../../google-flow/nano-banana-2.md) says the engine can actually
hold, and it is why this design succeeds where two rounds of per-letter reconstruction failed.

**Settings:** Enhance Prompt **off**. **4K** — the letterforms have to hold for the comp.

```prompt
Use the attached image as the reference. Keep the camera exactly where it is and keep every object in the picture exactly where it is: the same tent interior, doorway, mesh panel and patch, the same bedding, bottles and cans, the same forearm and hand holding a bottle at the lower left, the same burning drum in the same place, the same hooded figure standing in the same position with their back to the camera, the same falling rain, the same wet tarmac, puddles and broken glass, the same tents beyond, and the same shop front and lamp columns in the same places.

Change one thing: at this instant a sheet of lightning has gone off in the sky behind the buildings, and it is now the brightest light in the picture by a long way.

It is a huge, distant, hard, cold blue-white source, and it lights the entire car park at once from high up and behind. Everything that was black is now visible: the whole width of the camp, the rows of shelters, the litter and the standing water, the far side of the car park. The wet tarmac has turned to a bright hard sheet reflecting the sky. The lamp columns and the hooded figure are now hard black silhouettes against a lit background, with the light wrapping their edges. Shadows are thrown long and sharp toward the camera. There is no warm light anywhere in the frame except the drum fire, which is still burning but is now much the weaker of the two and reads as a small orange core with almost no reach.

The shop front on the right is fully lit by the flash. Its long horizontal sign panel above the frontage is clearly visible, weather-streaked and grimy, with the shop's name across it in unlit letters standing dark against the panel, sharp and readable. The sign gives off no light of its own and there is still no light inside the shop.

The hooded figure is still lit only along their edges and is still a solid black shape with nothing legible inside their outline.

A documentary press photograph on 35mm film, caught in a single frame of lightning: hard contrast, cold blue-white, deep sharp shadows, fine natural grain.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates:**

1. **Does it intercut?** Put it next to the dark frame — the doorway, the drum, the figure and the
   bedding must not have moved by a pixel. This matters more than how good the frame is.
2. **Is the shop's name sharp and readable**, dark on a lit panel?
3. **Is the light cold and hard and from behind the buildings** — long shadows thrown toward the
   camera, not a soft global lift?
4. **Is the drum fire now the weaker source?** If it still dominates, the flash is not reading as
   lightning.
5. **Did the figure stay a silhouette?**

⚠️ **One honest register note.** Lightning is the most *cinematic device* thing in a film that has
otherwise earned everything by withholding. **As the single flourish in ninety seconds it lands;
as the first of several it cheapens the rest.** Spend it here and nowhere else.

### 10b(iii) — the camp wide · **still** · written 2026-08-28, unrun

**The brief (Jack):** redo the aerial of the whole camp, make it cinematic, match the weather and
time of day of the accepted night frame, with lightning illuminating the place alongside the
barrel fires.

#### 🔴 Read this before generating: the vantage is the problem, and the lightning fixes it for free

**Three separate objections land on the same fact — the camera is too high.**

1. **An aerial cannot carry scale.** [`symptoms.md`](../../cinematography/symptoms.md): *"from a
   distance human proportions stop being legible and it reads as geometry."* This is the
   **GPOM `vantage` finding**, learned the hard way and predating the research that explained it.
   In the reference the figures are marks. A hundred marks is a map, not a hundred people.
2. **🔴 It trips Sontag's formal markers.** [`registers.md`](../../cinematography/registers.md)
   carries them as a checklist *because they are formal, not thematic*: **massing people into
   ornamental patterns; turning people into things.** A drone survey of a hundred tiny figures
   arranged in rows is a literal instance of both. The register file's central warning is that
   the grammar is neutral and meaning it ironically does not protect you.
3. **It is the news-helicopter shot.** This altitude and angle over a tented settlement is the
   single most recognisable refugee-camp framing there is
   ([`the-reader.md` rule 4](../../marketing/the-reader.md)) — and it is the read this film can
   least afford, because our reader arrived at immigration *via* the economy.

✅ **And the fix is already implied by Jack's own note.** **Lightning needs sky.** The reference
frame is about 8% sky, so there is physically nowhere for a flash to happen. Getting sky into the
frame means dropping the camera and tilting up — which **also** makes the people read as people,
**also** breaks the survey angle, and **also** gives the frame the three depth planes it currently
has none of. One change, four fixes.

**So: a rooftop vantage at about fifteen metres, tilted up, top third of the frame sky.** Not an
aerial — a place a person could stand. Foreground a barrel and two figures at human scale;
midground the camp; background the dead supermarket; sky above it carrying the flash.

#### The other changes

- **British, not shanty.** Dome tents, touring caravans, awnings, pallets, shopping trolleys and
  wheelie bins — the reference's tarpaulin-and-shack vocabulary is the same problem as objection 3,
  in the props.
- **One dominant near fire.** The lesson from the 10a sequence: many small equal fires is many
  focal points, i.e. none.
- **The sign needs no power.** The fascia is dark green lettering on a pale panel, so the flash
  alone makes it legible — one simple state, which is what
  [§21](../../google-flow/nano-banana-2.md) says the engine can hold.
  ✅ **Naming `Gill Sans` is now proven** — it worked on the 10b clip.
- **⚠️ 2K, not 4K.** [§22](../../google-flow/nano-banana-2.md), researched today: generating well
  above native resolution is the primary cause of **tiling in crowd scenes**, and this frame is a
  hundred shelters. The sign is a small region and can be checked; a cloned crowd cannot be fixed.

**Reference: ONE — the aerial, for the place only.** The night look is prose because it *can* be
written down, and [§3b](../../google-flow/nano-banana-2.md) reserves a second reference for what
cannot be. Enhance Prompt **off**.

```prompt
Generate a still photograph. Use the attached image as the reference for the place only: the same supermarket building at the far side of its car park, the same camp of shelters filling the whole car park, the same industrial units and houses along the skyline behind, and the same dual carriageway running down the right-hand side.

Camera: standing on a flat roof at the near edge of the car park, about fifteen metres up — high enough to see across the whole camp, low enough that the people in it are plainly people rather than marks. A 35mm lens. The camera is tilted up so the top third of the frame is open sky, the horizon runs just above the supermarket's roofline, the framing is slightly off level, and the supermarket sits a little right of centre rather than squared to the frame.

Nearest the camera and a few metres below, partly cutting into the bottom corner of the frame: the corner of a shelter, and beside it an oil drum burning hard with two people at it, close enough to read clearly as people — one bent over feeding a broken pallet into it, the other half-turned away mid-step. This is the one strong warm light in the picture.

Beyond them the camp runs away across the whole car park: ordinary British high-street dome tents and pop-ups, a few touring caravans, awnings guyed off shopping trolleys, stacked pallets, wheelie bins and standing water between them. No two shelters are alike — different sizes, colours, ages and states of collapse — and the people among them are walking, crouched or working, none of them posed or looking at the camera. Perhaps fifteen more oil drums are burning further off, each a small warm point lighting a metre around itself and nothing more.

At the far side, the supermarket: dark, its glass black, no light inside it and no working lamp anywhere in the car park. Across the pale panel above its frontage the word "Waitrose" in lowercase green Gill Sans lettering, weather-stained and unlit, giving off no light of its own.

Light: it is night, in the same weather as a heavy winter storm. The sky is deep blue-black with a narrow band of last light low across the horizon. At this instant a sheet of lightning has fired behind the buildings — a huge, distant, hard, cold blue-white source that lights the entire camp at once from high up and behind. Everything is briefly visible, the wet tarmac and the standing water have turned to bright hard sheets reflecting the sky, and long sharp shadows are thrown toward the camera. The drum fires stay warm and orange inside all that cold light, and the near one is still the warmest thing in the frame.

Heavy rain is falling through the whole picture, showing brightest where it crosses the flash and the firelight. The buildings are square and true, their rooflines straight and unbroken.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, no colour grading push, and the picture slightly underexposed.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates:**

1. **Do the people read as people?** If they are marks, the camera is still too high and nothing
   else matters.
2. **Are there three depth planes** — the near drum and its two figures, the camp, the store — and
   real sky above?
3. **Is the near drum the warmest thing**, with the flash cold around it?
4. **Any tiling?** Scan the shelters and the figures for repeats. This is the frame's specific
   risk ([§22](../../google-flow/nano-banana-2.md)) — if it clones, drop the resolution before
   touching the wording.
5. **Is the word right**, and are the rooflines straight?

⚠️ **This is the highest [trigger 3](../../flow/failure-modes.md) exposure in the film** — a tent
city, burn barrels, a hundred figures and an identifiable supermarket in one prompt. **If it
blocks, one change per run:**

1. `oil drum` / `oil drums` → *metal bins*
2. Cut `and the people among them are walking, crouched or working` — leave the camp unpeopled
   except the two at the near drum
3. Cut the quoted word and the font, and let the reference carry the fascia

### 10c — he's out, and it's his car · **still** · written 2026-08-28, unrun

**Canon:** *"He crawls out into the ruined car park — the W-AI-trose sign with only the A and I
lit; the wank tank still in its two bays, dead and clamped."*

#### The design — three decisions, each made against the shots either side

**1. Ground level, and close. Not another elevated shot.** 10a is a low POV and 10b is a rooftop
wide; a third distant frame would repeat a job, which
[`motion-and-cutting.md` §4](../../cinematography/motion-and-cutting.md) names as the usual cause
of a flat sequence. This beat is *his* recognition, so the camera has to be near him.

**2. 🔑 From behind — and he becomes the hooded figure.** 10a and 10b both put a man in silhouette
with his back to camera at a fire, and the audience has spent two shots looking at him. **Put
Tarquin in that pose and the rhyme does the argument with no narration at all: he is now the
man he was looking at.** It also keeps his face withheld until 11a, which is
[`shot-list.md`](./shot-list.md)'s own standing rule for this stretch, and it removes the
[§12](../../google-flow/nano-banana-2.md) problem — no face in frame means no Character to bind,
so prose is the correct lever here rather than a cast.

**The identifier is the gilet.** The same expensive olive gilet from 4b, 7a and 8b, five years
wrecked. One object tells the audience who this is without a face, and states what happened to him
in the same breath.

**3. One frame, both objects.** The dead X8 and the sign in the same picture, with him between
them. His car and the shop, both finished, and him standing in a car park he now lives in.
**It also bookends 8a** — the same car, the same two bays, five years on — and
[`symptoms.md`](../../cinematography/symptoms.md) calls the bookend *"the highest value, lowest
cost structure we have."*

**⚠️ No lightning in this one.** Ruled when the device was adopted: *spend the flourish once.* 10b
has it; 10c is lit by fire and nothing else.

#### The gag lands here, as stage two — and it is still a comp

10a's flash reveals **the whole name**, which is recognition. 10c reveals that **only two letters
still have power**, which is the joke. Full name first, reduction second — a better delivery than
either shot could manage alone.

🔴 **The fascia generates DEAD.** Two lit letters is a per-letter state, and
[§21](../../google-flow/nano-banana-2.md) is explicit that a multi-part change to one object
against a reference gets dropped rather than met halfway. The letters are composited, per the
2026-08-28 ruling — identical across every shot in 10–12, and no
[trigger 1](../../flow/failure-modes.md) exposure in the prompt.

**And the comped letters need no spill.** A fascia forty metres off lights nothing at the camera's
position, which is the same physics argument that kept the lit sign honest in 10a. The prompt says
so, so the engine does not invent a green wash.

**Reference: ONE — the accepted camp wide**, for the location, weather and night look. The X8 is
prose because no accepted frame in scene 10 contains it. Enhance Prompt **off**. **2K.**

```prompt
Generate a still photograph. Use the attached image as the reference for the place, the weather and the light: the same supermarket car park filled with a camp of shelters, the same night, the same heavy rain, the same wet tarmac and standing water, the same oil drums burning through the camp, the same muted cool colour and grain.

Camera: standing on the wet tarmac a few metres behind a man, at his shoulder height, on a 50mm lens. The framing is slightly off level and he sits left of centre rather than squared to the frame.

Nearest the camera and filling the left of the frame from the bottom edge to two-thirds of the way up, seen from directly behind: the back and shoulders of a man standing still in the rain, his head slightly lowered. The back of his head faces us squarely and hides the whole of the rest of his head behind it; the picture holds only his wet hair, his collar and his shoulders. He wears a quilted olive gilet over a dark jumper, both filthy, soaked through and worn to the point of falling apart, the gilet split along one seam with the wadding coming out of it. His arms hang at his sides.

In front of him, side on and filling the middle of the frame: a black BMW X8, stopped square across the painted white line between two parking bays and filling both of them, exactly where it was parked. It has not moved in years — the tyres are flat and perished, the paint is dulled under a skin of dirt and moss, the windows are opaque with grime, a wing mirror is gone, and a heavy steel wheel clamp is fitted to the front wheel. Shelters and rubbish have grown up around it and one guy line is tied off to its tow eye.

Beyond it, at the far side of the car park: the supermarket, dark, its glass black, no light inside it and no working lamp anywhere. The long pale panel above its frontage is weather-stained and completely dead — the lettering across it is unlit and dark, giving off no light at all, and there is no green glow anywhere in the picture.

Light: the burning drums are the only light. The nearest of them is off to the right and low, so the man, the car and the wet ground are lit warm and steeply from one side, and everything beyond the drums falls away to black. Rain is falling hard through the whole frame and shows brightest where it crosses the firelight.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, no colour grading push, slightly underexposed.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates:**

1. **Is the back of his head genuinely occluding?** No cheek, no ear, no profile —
   [§18](../../google-flow/nano-banana-2.md), and an invented face here is an uncast character we
   would then have to match in 11a.
2. **Does the gilet read as the same garment, ruined?** That is the only thing telling the audience
   who this is.
3. **Is the car plainly dead** — flat tyres, clamp, grown into the camp — rather than merely parked?
4. **Is the fascia truly dark**, with no green anywhere? The comp needs a clean surface.
5. **Does he read as the hooded figure from 10a/10b?** Same pose, same distance, same back. If the
   rhyme is not obvious at a glance, it is not landing.

⚠️ **[Trigger 3](../../flow/failure-modes.md) exposure, plus a destitution-adjacent wardrobe
description.** If it blocks, one change per run:

1. Cut `soaked through and worn to the point of falling apart, the gilet split along one seam with
   the wadding coming out of it` → *rain-soaked and long unwashed*
2. `black BMW X8` → *a large black luxury SUV*
3. Cut `Shelters and rubbish have grown up around it`

### 11b(i) — the newspaper, found by torchlight · **still** · written 2026-08-28, unrun

**The brief (Jack):** an earlier daylight frame of the newspaper exists but the weather is wrong.
Redo it at night, **first person, Tarquin finding the paper on the ground with a torch, like a
video game.**

#### 🔑 The torch is not decoration — it solves four problems at once

1. **It is one named source with a position**, which is the standing anti-slop fix for *"vague
   nice lighting"*. The old frame is flat overcast with no traceable source.
2. **It makes a focal point for free.** A hard narrow cone on the headline with everything else
   black; [`frame.md`](../../cinematography/frame.md)'s *one bright anchor inside the darkness*,
   arrived at by the world rather than by grading.
3. 🔴 **It hides the body text physically, which is the whole point.** The old frame's biggest
   slop tell is its **garbled body copy** — the model attempted columns of newsprint and produced
   nonsense. **The beam only covers the top of the page**, so the rest is dark and rain-soaked and
   we never ask the engine to render body text at all. The light does the censoring.
   *(Same family as [§15](../../google-flow/nano-banana-2.md): describing something as unreadable
   is strictly easier than describing it correctly.)*
4. **It is motivated.** Nothing electric works in this world, so a torch is the only way to see
   anything — established across 10a–10c.

#### The POV, and what makes it read as first person rather than a game

**Video models have no built-in concept of *camera as character*** `[community]`, so it has to be
spelled out: whose eyes these are, that the camera **is** those eyes, and which parts of the body
are in frame. **Body anchors are what stop a model silently switching to third person** — here,
his hand at the bottom-right and his boot toes at the bottom edge. Camera height is stated as
crouched, which the same sources flag as the POV height for *examining an object*.

⚠️ **The thing that would make it read as a video game rather than a film is a perfectly level,
perfectly stabilised frame.** So the off-level instruction is doing double duty, and the 35mm grain
carries the rest. Jack's instinct is right — a torch cone in first person is the survival-horror
signature — but the register has to stay documentary or it breaks the film.

#### 🔴 The hand is the biggest generation risk in this shot

**2026's hand failure is no longer finger count — it is fusion.** *"Held objects are 2026's new
six fingers: the count is right, but they fuse with the cup handle, knife hilt, or phone bezel."*
The field's fix is a negative prompt, which [backfires here](../../google-flow/nano-banana-2.md),
so it is converted to the positive: **"five separate fingers, each one distinct, wrapped around
the barrel, and the torch keeps its own shape clearly separate from the hand."**

**Second mitigation, and the stronger one: put the hand close to the lens and throw it out of
focus.** A hand that is soft cannot fuse legibly, and out-of-focus is easier to draw than correct.
**Budget a reroll regardless** — the sources are unanimous that a meaningful percentage of
generations still fail on hands.

**Do not cast `@future-Tarquin`.** There is no face in a first-person shot, so
[§12](../../google-flow/nano-banana-2.md) applies — a Character binds to a face, and with nothing
to bind to it only competes with the prose. This is [§19](../../google-flow/nano-banana-2.md)'s
narrow exception, where prose is the only lever left. **The gilet cuff is the identifier**, same
as 10c.

#### ⚠️ Two notes for a human

**1. The headline names the technology, not the chooser.**
[`the-reader.md` rule 5](../../marketing/the-reader.md) is explicit that *"the machines are
coming"* produces fatalism, and rule 6 forbids raising automation fear without the beneficiary in
the same piece. **The defence is that the picture names him** — the man reading it is the man who
did it, and that irony is the beat. **That works only if the audience connects them**, so 11c has
to keep him in frame with it. If we would rather not lean on that, an alternative that names the
beneficiary inside the headline: `LAST UK WORKER LAID OFF · SHAREHOLDERS 'DELIGHTED'`. **A human
call.**

**2. This changes 11b.** Canon has **Bob handing him the paper** — *"that was like five years ago,
look at the date"* — as the callback to the 1b plant. If Tarquin finds it himself, Bob loses that
beat and the hand-off. Both can coexist (he finds it, and Bob later makes him look at the *date*,
which is a different reveal), but somebody should decide.

**⚠️ The date is not in this shot.** *"The date does the time"* is 11c's job and it is a second
legible text element; two text targets in one frame doubles the risk. Shoot it as its own insert.

**Reference: ONE — the accepted 10a night frame**, for weather, light and place. The newspaper
composition is prose. Enhance Prompt **off**. **4K** — a headline has to hold.

```prompt
Generate a still photograph. Use the attached image as the reference for the place, the weather and the light: the same ruined supermarket car park at night, the same heavy rain, the same wet tarmac and standing water, the same shelters, the same muted cool colour and grain.

This is a first-person point-of-view shot and the camera is the man's own eyes. He is crouched down low over the ground, so the camera sits about half a metre above the wet tarmac and tilts down at it, on a 35mm lens. The framing is slightly off level and what he is looking at sits right of centre rather than squared to the frame.

Entering the frame from the bottom right corner, very close to the lens and thrown completely out of focus: his own hand holding a small metal torch. Five separate fingers, each one distinct, are wrapped around the barrel of the torch, and the torch keeps its own shape clearly separate from the hand. The cuff of a filthy quilted olive gilet shows at his wrist. Along the very bottom edge of the frame, also close and soft, the toes of his wet boots.

The torch beam is the only light in the picture: a hard, narrow, slightly blue-white cone thrown down and to the left from the bottom right corner, which has just this moment landed on what he is looking at.

Lying face up on the wet tarmac inside that beam, soaked flat and half in a puddle, a newspaper. Only the top of its front page is inside the beam, and across it the headline reads "BRITAIN'S LAST WORKER REPLACED BY AI" in heavy black condensed capitals. Below the headline the page runs out of the beam into darkness and the wet paper has gone translucent, so the columns underneath are unlit, blurred and soft, and the only legible words anywhere in the picture are that headline.

Around it: wet tarmac, broken glass, flattened cans and plastic bags, all glittering sharply where the beam catches them and going to solid black where it does not. Far beyond the reach of the beam, the small orange glow of a drum fire somewhere out in the camp, lighting nothing.

Rain falls hard through the beam, showing as bright streaks inside the cone of light and invisible outside it, and raindrops are landing on the wet page and in the puddle around it.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, no colour grading push, deep black shadows.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates:**

1. **The hand.** Five separate fingers, and is the torch a separate object from the hand? This is
   the frame's most likely failure and the reason to reroll.
2. **Does it read as first person?** Hand and boots both present, no third-person drift.
3. **Is the headline exact**, and is everything below it genuinely unreadable rather than garbled
   pretend-text? Garbled body copy is the failure this whole design exists to avoid.
4. **Is the beam a hard cone with real black outside it**, rather than a general lift?
5. **Is the frame off level?** A perfectly level POV reads as a game.

⚠️ If it blocks: 1) cut `filthy` → *worn*; 2) cut the broken glass and cans; 3) drop the quoted
headline and let the paper be unreadable, then comp the headline in post.

#### ⚠️ Redesigned 2026-08-28 (Jack), before the crouched version was ever run

**"Make it so he is standing up with the torch, then picks it up in the video, but in the image a
first POV of him walking to the newspaper outside the tent."** The crouched draft above is
superseded and kept only as a record. **Four things get better:**

1. **The still gets an unresolved question.** [`stills.md` §1](../../cinematography/stills.md):
   *a still only holds attention if it contains an unresolved question, and resting poses die
   fast.* Crouched over the paper is **arrived**; walking toward it is **en route**. This is the
   8b lesson repeating — *when the frame will not perform, move the moment earlier.*
2. **The plate and the clip split correctly.** The still is the moment before; the clip completes
   it. Same discipline as 9a, where the knee-grab lives in the clip and not the plate.
3. **A standing torch rakes forward instead of pointing down** — the lit patch stretches away
   along the ground and every piece of litter throws a long shadow **toward** the camera. That is
   depth, for free, and it is the single most cinematic thing available in this shot.
4. 🔑 **The reveal moves to where it is safe.** At four metres and a shallow angle the headline is
   small and foreshortened — so **it is not legible in the still, and it should not be.** The
   picture shows a pale rectangle at the far end of the beam and withholds what it says. **The
   words resolve in the clip, at the moment he lifts it toward the lens** — large, frontal, and
   only for the last second. That is the easiest text ask in the whole film, and there is **no
   text risk in this still at all.**

⚠️ **The clip is NOT a walking POV.** A first-person walk is camera translation, and this camp is
wall-to-wall tents, pallets and corrugated sheet — the exact geometry Veo hinges. **The clip is
the pick-up only**, camera near-static: the hand enters, takes the paper, lifts it into the beam.
The walk is implied by the still, which is how it would be cut anyway.

### 11b(i) — walking to the newspaper · **still** · written 2026-08-28, unrun · *supersedes the crouched draft*

**Reference: ONE — the accepted 10a night frame.** No Character (no face). Enhance Prompt **off**.
**2K** — no text has to survive.

```prompt
Generate a still photograph. Use the attached image as the reference for the place, the weather and the light: the same ruined supermarket car park at night, the same heavy rain, the same wet tarmac and standing water, the same shelters, the same muted cool colour and grain.

This is a first-person point-of-view shot and the camera is the man's own eyes. He is standing and walking, so the camera is about a metre and a half above the wet tarmac and tilted down toward the ground ahead of him, on a 35mm lens. The framing is slightly off level.

At the bottom of the frame, close to the lens: one of his boots, caught mid-stride with the heel off the ground and his weight still on the other foot. Entering from the bottom right corner, very close to the lens and thrown completely out of focus, his own hand holding a small metal torch — five separate fingers, each one distinct, wrapped around the barrel, and the torch keeping its own shape clearly separate from the hand. The cuff of a filthy quilted olive gilet shows at his wrist.

Cutting into the left edge of the frame, close and dark: the corner of the tent he has just come out of, a taut guy line running out of it down to a peg in the tarmac.

The torch beam is the only light in the picture. Because he is standing, it strikes the ground at a shallow angle and stretches away ahead of him as a long narrowing wedge of light. Every can, bag and shard of glass inside it throws a long hard shadow back toward the camera. Outside the wedge everything is solid black.

Lying at the far end of that wedge, about four metres ahead on the wet tarmac and seen at a steep foreshortened angle: a newspaper, soaked flat and half in a puddle, a pale rectangle in the dark. It is too far away and too sharply angled for any of its printing to be made out — the page reads as a bright shape with grey texture on it and no readable words anywhere in the picture.

Far beyond the beam, small and out of focus, the orange glow of a drum fire somewhere out in the camp, lighting nothing.

Rain falls hard, showing as bright streaks inside the wedge of torchlight and invisible outside it, and pitting the surface of the puddles.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, no colour grading push, deep black shadows.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates:**

1. **Does it read as walking?** Boot mid-stride, heel up. A planted foot means the frame has
   resolved and the shot is dead.
2. **Is the beam a long shallow wedge** with litter throwing shadows *toward* the camera — not a
   pool pointing straight down?
3. **The hand** — five separate fingers, torch a distinct object, and soft. Still the likeliest
   reroll.
4. **Is the paper unreadable?** If the engine has written words on it, reject: this frame's job is
   to withhold them.
5. **Off level?** A perfectly level POV reads as a video game rather than a film.

**Then the clip, once this is accepted:** camera near-static, the hand comes down into frame, takes
the paper, and lifts it up into the torch beam toward the lens where the headline resolves. One
action, no camera translation.

### 11b(i) — walking to the newspaper, round 2 · **still** · written 2026-08-28, unrun

**Two changes asked for by Jack: cast `@Future-Tarquin`, and make the headline readable.** Both
were argued against above; both are now the brief. **Each one forces a further change, and those
are the interesting part.**

#### Casting the Character means the garment description has to come OUT

[§19](../../google-flow/nano-banana-2.md), and Jack's own standing rule: **a Character cast means
no appearance description at all.** So *"the cuff of a filthy quilted olive gilet"* is deleted —
wrapping it in a keep-verb is not a loophole either (8c(ii) proved that the same day it was
written).

⚠️ **It will not bind a likeness** — there is no face in a first-person shot
([§12](../../google-flow/nano-banana-2.md)). **But it is not wasted**, and this is the upside
worth naming: on a POV frame the **sleeve is the only wardrobe in shot**, and a Character carries
wardrobe. So casting it is the *right* way to get the correct sleeve — better than describing one,
which is what kept coming back wrong on 8c(i).

#### A readable headline forces the paper upright, and that is an improvement

At four metres flat on the ground at a steep angle, a headline cannot be legible — that was the
whole reason the previous draft withheld it. **So the paper has to stand up.** It is caught
against a pallet and half upright, facing him, two metres away.

**Three things get better, not worse:**

- **It is physically motivated** — wind and rain drive loose paper against things; the earlier
  daylight frame had it propped exactly this way.
- **An upright page facing the beam square-on blazes white**, which makes it comfortably the
  brightest object in the frame and hands the shot its focal point.
- **It reads as the world showing him something**, rather than him finding litter.

🔴 **The body-copy censor stays, and it is now load-bearing.** The old daylight frame's worst slop
tell was **garbled newsprint** under the headline. The beam reaches the top of the page and the
lower half stays soaked and dark, so the columns are never attempted.
**Do not remove that clause to "improve" the picture.**

**Resolution goes back up to 4K** — a headline has to survive, and 1K blurs small text
([`image-prompting.md` §5](../../flow/image-prompting.md)).

**Reference: the accepted 10a night frame. Character: `@Future-Tarquin`.** Enhance Prompt **off**.

```prompt
Generate a still photograph. Use the attached image as the reference for the place, the weather and the light: the same ruined supermarket car park at night, the same heavy rain, the same wet tarmac and standing water, the same shelters, the same muted cool colour and grain.

This is a first-person point-of-view shot and the camera is the eyes of the man from the character reference. He is standing and walking, so the camera is about a metre and a half above the wet tarmac and tilted down toward the ground ahead of him, on a 35mm lens. The framing is slightly off level.

At the bottom of the frame, close to the lens: one of his boots, caught mid-stride with the heel off the ground and his weight still on the other foot. Entering from the bottom right corner, very close to the lens and thrown completely out of focus, his own hand holding a small metal torch — five separate fingers, each one distinct, wrapped around the barrel, and the torch keeping its own shape clearly separate from the hand. His sleeve and wrist show at the edge of the frame.

Cutting into the left edge of the frame, close and dark: the corner of the tent he has just come out of, a taut guy line running out of it down to a peg in the tarmac.

The torch beam is the only light in the picture. Because he is standing, it strikes the ground at a shallow angle and stretches away ahead of him as a long narrowing wedge of light. Every can, bag and shard of glass inside it throws a long hard shadow back toward the camera. Outside the wedge everything is solid black.

About two metres ahead, at the far end of that wedge: a newspaper, soaked and rain-flattened, blown up against the side of a broken wooden pallet so that it stands half upright and its front page faces him square on. The beam hits it flat and it is the brightest thing in the picture. Across the top of the page, inside the beam and sharply in focus, the headline reads "BRITAIN'S LAST WORKER REPLACED BY AI" in heavy black condensed capitals. Below the headline the page falls out of the beam into darkness and the wet paper has gone translucent and soft, so the columns underneath are unlit and blurred, and that headline is the only legible text anywhere in the picture.

Far beyond the beam, small and out of focus, the orange glow of a drum fire somewhere out in the camp, lighting nothing.

Rain falls hard, showing as bright streaks inside the wedge of torchlight and invisible outside it, pitting the puddles and running down the face of the page.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, no colour grading push, deep black shadows.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates:**

1. **Is the headline exact and sharp**, and is everything below it **unreadable rather than
   garbled pretend-text**? Fake newsprint is the failure this design exists to prevent.
2. **Does it still read as walking?** Heel up. A planted foot resolves the frame and kills it.
3. **The hand** — five separate fingers, torch a distinct object, soft. Likeliest reroll.
4. **Is the page the brightest thing**, with real black outside the wedge?
5. **Did the sleeve come back as his wardrobe?** That is the only thing the Character can deliver
   here — if it did not, the cast is doing nothing and the shot is fine without it.

⚠️ **A quoted headline reinstates text-policy exposure.** No real institution is named, which is
the [trigger 4](../../flow/failure-modes.md) line, so the risk is moderate. **If it blocks:**
1) drop the quoted headline and let the page be a bright blank, then comp the words;
2) `broken wooden pallet` → *a pile of rubbish*.

### 11b(i) — round 3 · **still** · written 2026-08-28, unrun

**Round 2 came back with his legs stretched out in front of him, as if he had fallen over.**

#### 🔴 The cause: the reference was a seated POV, and it beat the prompt

**The attached reference was the 10a tent frame — whose entire composition is a man's legs and
sleeping bag stretching away toward a doorway.** The prompt asked for a *standing, walking* POV
while handing the engine a picture of a *reclining* one, and
[§9](../../google-flow/nano-banana-2.md) is explicit that a strong reference becomes the baseline
every change is measured against **and wins the ties.** It did not disobey; it was given two
authorities and took the picture.

**Recorded as a working rule: on a POV shot, the reference's body position is inherited whether
or not you asked for it.** A POV reference is never "just the location."

#### The fix, in three parts — and the first one is to drop the reference entirely

1. 🔑 **No location reference at all.** [§15](../../google-flow/nano-banana-2.md): *if the setting
   keeps coming back wrong, check whether the shot needs a setting at all — ask what actually has
   to be sharp.* **In this frame everything outside the torch beam is black.** There is almost no
   set in the picture, so there is almost nothing for a location reference to carry, and the only
   thing it was reliably carrying was the wrong posture. **`@Future-Tarquin` is the only
   attachment.**
2. **Say where the nearest ground is, not where the body is.** Writing *"he is standing"* is a
   statement about a person the camera cannot see. **Writing that the bottom edge of the frame
   falls on tarmac a metre in front of him is geometry** — and if the nearest ground is a metre
   away, there is physically nowhere to put a pair of legs. Same lesson as camera height, which
   was ignored three times as a number and obeyed first time as a consequence.
3. **Delete the boots.** Round 2 kept a boot at the bottom edge as a POV anchor and that is the
   toehold the legs grew from. [§18](../../google-flow/nano-banana-2.md)'s escalation applies
   directly — *a body part that is not in the picture cannot grow.* **The hand and torch are
   anchor enough**; the POV literature is explicit that hands alone lock first person.

**Attachment: `@Future-Tarquin` only. No location image.** Enhance Prompt **off**. **4K.**

```prompt
Generate a still photograph. This is a first-person point-of-view shot at night: the camera is the eyes of the man from the character reference, and the picture shows only what he can see in front of him.

He is walking forward across a car park and looking down at the ground ahead. The camera is at the eye height of a walking adult on a 35mm lens, angled down toward the ground in front of him. The nearest thing in the picture is wet tarmac about a metre ahead of him, so the whole bottom edge of the frame is wet ground running away from the camera. The framing is slightly off level.

Entering from the bottom right corner, very close to the lens and thrown completely out of focus: his own hand, held out in front of him at chest height, holding a small metal torch. Five separate fingers, each one distinct, are wrapped around the barrel, and the torch keeps its own shape clearly separate from the hand. His sleeve and wrist show at the edge of the frame.

Cutting into the left edge of the frame, close and dark: the corner of a small tent, with a taut guy line running out of it down to a peg in the tarmac.

The torch beam is the only light in the picture. Held at chest height it strikes the ground at a shallow angle and stretches away ahead of him as a long narrowing wedge of light across the wet tarmac. Every can, bag and shard of broken glass inside that wedge throws a long hard shadow back toward the camera. Outside the wedge everything is solid black.

About two metres ahead, at the far end of the wedge: a newspaper, soaked and rain-flattened, blown up against the side of a broken wooden pallet so that it stands half upright and its front page faces him square on. The beam hits it flat and it is the brightest thing in the picture. Across the top of the page, inside the beam and sharply in focus, the headline reads "BRITAIN'S LAST WORKER REPLACED BY AI" in heavy black condensed capitals. Below the headline the page falls out of the beam into darkness and the wet paper has gone translucent and soft, so the columns underneath are unlit and blurred, and that headline is the only legible text anywhere in the picture.

Far beyond the beam, small and out of focus, the orange glow of a fire burning in a drum somewhere out in the camp, lighting nothing.

Heavy rain is falling, showing as bright streaks inside the wedge of torchlight and invisible outside it, pitting the puddles on the tarmac and running down the face of the page.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, no colour grading push, deep black shadows.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates:**

1. **Is the bottom edge of the frame ground?** Nothing of him below the hand. This is the whole
   point of the round.
2. **Headline exact and sharp**, everything below it unreadable rather than garbled?
3. **The hand** — five separate fingers, torch a distinct object, soft.
4. **Is the beam a long shallow wedge** with shadows thrown toward the camera?
5. **Off level**, and does the world outside the beam go properly black?

**If a body still appears at the bottom of the frame**, do not describe the posture harder — that
is the documented trap. **Delete the tent corner as well** and let the frame be nothing but the
hand, the wedge of light and the page.

### 11b(i) — round 4 · **still** · written 2026-08-28, unrun · *location reference restored*

**Jack: "Please use the location image."** Round 3 dropped it because the reference was the cause
of the fallen-over body. **The resolution is not to go without a reference — it is to use one
that has no POV body in it at all.**

🔑 **Use the accepted camp wide, not the tent frame.** It is elevated and there is no first-person
body anywhere in it, so it can carry the place, the camp, the wet tarmac, the litter and the rain
while teaching **nothing** about posture. That is the whole of
[§24](../../google-flow/nano-banana-2.md) satisfied without giving anything up.

**Two risks it brings, and the counters:**

| Risk | Counter in the prompt |
| --- | --- |
| It is a **wide, elevated** frame and may pull the camera back up | **Name the reference's role and state the change as a change** ([§3](../../google-flow/nano-banana-2.md)'s keep/change buckets): keep the place, change the camera to down among it |
| It is **brightly lit by a lightning flash** and may lift the whole frame out of torch-only darkness | State the light **positively and completely** — the torch is the only light, everything outside the wedge is solid black, there is no other source anywhere. Naming lightning to exclude it would only put it back in |

**The two fixes from round 3 stay and matter more now, not less:** the bottom edge of the frame is
**ground a metre ahead**, and there are **no boots** — geometry, not adjectives.

**Attachments: the camp wide (location) + `@Future-Tarquin`.** Enhance Prompt **off**. **4K.**

```prompt
Generate a still photograph. Use the attached image as the reference for the place only: the same ruined supermarket car park at night, the same camp of shelters, the same wet cracked tarmac and standing water, the same scattered litter and broken glass, the same heavy rain, the same muted cool colour and grain.

Two things are different from that image. The camera is now down among it rather than above it, and it is a first-person point-of-view shot: the camera is the eyes of the man from the character reference, and the picture shows only what he can see in front of him. And the torch in his hand is the only light in the whole picture — there is no other light source anywhere in the frame, and everything the torch does not reach is solid black.

He is walking forward across the car park and looking down at the ground ahead. The camera is at the eye height of a walking adult on a 35mm lens, angled down toward the ground in front of him. The nearest thing in the picture is wet tarmac about a metre ahead of him, so the whole bottom edge of the frame is wet ground running away from the camera. The framing is slightly off level.

Entering from the bottom right corner, very close to the lens and thrown completely out of focus: his own hand, held out in front of him at chest height, holding a small metal torch. Five separate fingers, each one distinct, are wrapped around the barrel, and the torch keeps its own shape clearly separate from the hand. His sleeve and wrist show at the edge of the frame.

Cutting into the left edge of the frame, close and dark: the corner of a small tent, with a taut guy line running out of it down to a peg in the tarmac.

Held at chest height, the torch strikes the ground at a shallow angle and its beam stretches away ahead of him as a long narrowing wedge of light across the wet tarmac. Every can, bag and shard of broken glass inside that wedge throws a long hard shadow back toward the camera.

About two metres ahead, at the far end of the wedge: a newspaper, soaked and rain-flattened, blown up against the side of a broken wooden pallet so that it stands half upright and its front page faces him square on. The beam hits it flat and it is the brightest thing in the picture. Across the top of the page, inside the beam and sharply in focus, the headline reads "BRITAIN'S LAST WORKER REPLACED BY AI" in heavy black condensed capitals. Below the headline the page falls out of the beam into darkness and the wet paper has gone translucent and soft, so the columns underneath are unlit and blurred, and that headline is the only legible text anywhere in the picture.

Far beyond the beam, small and out of focus, the orange glow of a fire burning in a drum somewhere out in the camp, lighting nothing.

Heavy rain is falling, showing as bright streaks inside the wedge of torchlight and invisible outside it, pitting the puddles on the tarmac and running down the face of the page.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, no colour grading push, deep black shadows.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates — the two reference risks first:**

1. **Is the camera down among it**, first person, or has it drifted back up to the wide?
2. **Is the torch the only light**, with real black outside the wedge — no leftover flash, no
   ambient lift?
3. **Is the bottom edge of the frame ground**, with nothing of him below the hand?
4. **Headline exact and sharp**, everything below it unreadable rather than garbled?
5. **The hand** — five separate fingers, torch a distinct object, soft.

**If the frame comes back lifted or elevated, the reference is winning and the next move is to
drop it** — [round 3](#11bi--round-3--still--written-2026-08-28-unrun) is the version without one,
and §15 says this frame barely needs a set because almost all of it is black.

**✅ ACCEPTED 2026-08-28, round 4** —
[`camera/reference/11b-newspaper-torchlight-ACCEPTED.png`](./camera/reference/11b-newspaper-torchlight-ACCEPTED.png).
The camp wide held the place without teaching a posture, the torch stayed the only light, the
bottom edge is ground, and the headline is sharp with the body copy properly unreadable.

> ### 💡 The clip's design, ruled by Jack: **move the light, not the camera**
>
> *"Just have it rain and him slightly move his flashlight, as if it is slight camera sway, but
> slight flashlight sway."*
>
> **This is the right answer and it is worth keeping as a general move.** It buys the aliveness of
> a handheld first-person shot while breaking none of our rules:
> [R7](../../cinematography/motion-and-cutting.md) says handheld is a style not truth and
> locked-off beats wobble; camera translation is what fires the regeneration/hinge bug; and
> [`symptoms.md` §C](../../cinematography/symptoms.md) says a frame that never changes reads as a
> photograph rather than a shot and needs *one* thing to move — *"light drift"* is the first
> example it gives. **A drifting practical light is the locked-camera way to get all three.**
>
> **The text is the thing to protect.** Wet paper in wind is exactly what would flutter, and
> flutter is where a headline morphs — so the paper is **pinned physically** (soaked and stuck to
> the pallet), the headline gets **its own persistence instruction**, and **the beam never leaves
> the page**, so the words are never partly lit. *(Clip prompt handed over 2026-08-28; not
> recorded — the ledger is stills-only per the 2026-08-26 ruling.)*

### 12a — the two of them by the fire · **still** · written 2026-08-28, unrun

**Canon:** *"The two of them by the fire — in the car park, not the woods. Faces changed: almost a
smile."* **This is the shot the whole film has been avoiding: two faces, both legible, both
having to perform.**

#### 🔴 Read first: two Characters in one frame is the known frontier

> *"Two characters interacting in the same shot still produce identity blurring on every platform
> as of mid-2026"* — features blend between them, faces swap, or one identity is lost entirely.
> `[community 2026-08-28]`

**Camping has never attempted it and has twice been redesigned to avoid it** — 2b needed Veo 3.1
just to hold two faces through a laugh in a locked interior, and 8b only worked by going to a
forty-metre long lens that took faces out of the argument. **Three things are in our favour here:**
it is a *still* rather than a clip; both faces are at a workable size; and the two Characters are
visually very unalike, which the same sources name as the thing that keeps identities separate.

**The one new instruction that matters: anchor each Character to a screen position.** *"Character A
on the left, Character B on the right"* is the documented fix, and it agrees with Google's own
Ingredients guidance to **describe the role each reference plays** rather than let the model infer
it. The prompt does this explicitly.

🔴 **BLOCKER: `@Bob` is the wrong Bob.** [`shot-list.md`](./shot-list.md) records that the accepted
**8c(i)** frame — the best face in the film so far — **does not match the `@Bob` Character**
(longer hair, different coat), and that the Character is owed a rebuild from that frame. **Cast the
old one here and this Bob will not be the Bob the audience met in scene 8.** Rebuild first, or
accept a continuity break in the film's most important scene.

**If identity still blurs after two rounds**, the field's reliable answer is to generate each man
separately and composite — a real change of method, and a decision for a human.

✅ **Ruled 2026-08-29 (Jack): cast the existing `@Bob` and accept the break.** The reasoning is
sequencing, not indifference — **whether two Characters hold in one frame at all is the unknown
that gates the whole ending**, and it is answerable today, where a Character rebuild is a detour
that answers nothing. Run it with the Character we have.
⚠️ **The debt inverts, and that is the point worth writing down.** If `12a` lands, `@Bob` is the
Bob of `10d` and all of `11`–`12` — five shots — and `8c(i)` is the single frame that disagrees.
**So the outstanding job becomes a re-shoot of `8c(i)`, not a rebuild of the Character.** Do not
touch either until `12a` is accepted; both jobs are cheaper once the harder question is settled.

#### The design — one fire, two faces, and the light is the argument

**Gate 1.** The beat is that the class distance has closed. **So the frame must argue they are the
same now, and the way to argue it is with light: one source, reaching both faces identically.**
[`style.md`](./style.md) already says this fire is *"the one earned human warmth, the heat the
whole story withheld, shared between the two men at the end."* **The shot is that sentence.**

**Four changes from the reference, each fixing a named slop tell:**

| Reference | Change | Why |
| --- | --- | --- |
| Both men **squarely flanking a centred barrel, facing the lens** | Off-centre, unmirrored, **both looking down into the flames** | Symmetry plus dead-centre plus eye contact with the lens is a *portrait*, not a scene. It is also the [`registers.md`](../../cinematography/registers.md) power grammar — and nobody warming their hands stares down a camera |
| **Flat overcast daylight, fire lighting nobody** | **Night, the fire the only source, lighting both faces from below** | Continuity with all of 10–11, and it makes the light carry the argument instead of decorating it |
| **Empty foreground** | **The flames break into the bottom of frame, out of focus** | Three depth planes, and it puts the camera *at* the fire rather than watching it |
| **Lit green fascia** | Dead, letters comped | The 2026-08-28 ruling |

🔑 **They do not look at each other.** That is the beat — canon's 12b is *"the apology happens the
man way, nothing said straight."* Two men do not make eye contact for this. It also solves the
lens-stare, gives both faces the same downward tilt into the same light, and **withholds the
connection so the audience infers it** ([`stills.md`](../../cinematography/stills.md)).

**Expression as anatomy, never as emotion** ([`image-prompting.md` §4a](../../flow/image-prompting.md),
and the 7a lesson: *describing it as baffled gets a mood; describing the muscles gets the face*).
*"Almost a smile"* is written as the mouth corners drawn back without parting, the outer eye
corners creased, the brow level and loose.

**The rain has stopped.** The storm running through 10a–11b eases to nothing here. The register
change is carried by weather rather than stated, and it is motivated — storms pass. *(Keep the
rain instead if that reads too neat; it is a one-clause change.)*

⚠️ **Four hands over a fire is real risk** — held objects and fine articulation are the documented
weak spot. They are written as **one simple shape**: flat, palms down, fingers together, lit from
beneath so the tops stay in shadow. Check them first.

**Attachments, earliest slots first: `@Bob`, `@Future-Tarquin`, then the reference image.** No
appearance description for either man ([§19](../../google-flow/nano-banana-2.md)) — only position,
action and face muscles. Enhance Prompt **off**. **4K** — the faces are the shot.

```prompt
Generate a still photograph. Use the attached image as the reference for the place only: the same supermarket car park filled with a camp of shelters, the same wet cracked tarmac and standing water, the same scattered litter and broken glass, the same burning oil drum, the same muted cool colour and grain.

Two things are different from that image. It is now night, and the fire in the drum is the only light in the whole picture — there is no daylight, no lamp, no lit window, and the shop behind is dark with its sign unlit and giving off no light at all. And the camera is now down at the fire with the two men rather than standing back from them.

Camera: a 50mm lens at chest height, just above the rim of the burning drum and about two metres from it, so the flames rise into the bottom of the frame very close to the lens and completely out of focus. The framing is slightly off level and the drum sits left of centre rather than squared to the frame.

Standing beyond the drum on the left of the frame, framed from the waist up and turned about thirty degrees toward it: the man from the first character reference. Standing on the right of the frame, a little further back from the drum and turned more square on: the man from the second character reference. They are not the same distance from the fire and they are not mirrored.

Both men have their hands held out over the flames, flat with the palms down and the fingers together, and both are looking down into the fire rather than at each other and never toward the camera. On each face the corners of the mouth are drawn very slightly back without the lips parting, the outer corners of the eyes are creased, and the brow is level and loose.

Light: the fire in the drum is the only source in the picture. It sits below both faces, so both are lit from underneath by the same warm moving light — the undersides of their jaws, brows and hands catching it, the tops of their heads and shoulders falling into shadow, and both men lit identically by it. Beyond the reach of the fire the camp and the shop front fall away to solid black.

The rain has stopped. The tarmac and the litter are still soaked and holding water, but nothing is falling through the frame and the air is still.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, no colour grading push, and skin rendered with its real texture and unevenness rather than smoothed.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates — identity first:**

1. 🔴 **Are they two distinct men**, and is each one the right man? Blending, swapping or one
   identity collapsing is the frame's specific failure. Check against the 8c(i) Bob and the 4b/7a
   Tarquin.
2. **The hands.** Four of them over a fire. Simple flat shapes, correct count, not fused.
3. **Is neither man looking at the camera**, and are they unmirrored and off-centre?
4. **Is the fire the only light**, coming from below, and does it reach both faces the same?
5. **Is the expression a muscle, not a mood?** Cover the mouths: the eyes alone should not read as
   sad. Then cover the eyes: the mouths alone should not read as a grin.

⚠️ [Trigger 3](../../flow/failure-modes.md) exposure. If it blocks: 1) `burning oil drum` →
*a fire burning in a metal bin*; 2) cut `and broken glass`.

#### ⚠️ Revised 2026-08-28 (Jack): rainy night, lit by the drum **and** lightning

**"Make it match the weather and time of day from before — rainy night time, illuminated by the
fire barrel and lightning."** The *"the rain has stopped"* idea is dropped; the storm runs through
12a as it does through the rest of scene 10–11.

**This does not break the *spend the flourish once* ruling, and the distinction is worth stating:**
what was spent in 10b was **the flash as a reveal** — a strike that *showed him something*. What
runs through the sequence is **the flash as weather**, which is just the environment and can
recur as often as a storm does. **The rule holds as long as the 12a flash reveals nothing and
lands on no beat.**

🔴 **But it cannot be allowed to light the two men, because the fire lighting them identically
*is* the shot's argument.** A flash washing over both faces would replace the one thing this frame
exists to say. **So the lightning goes far behind them** — in the cloud beyond the buildings,
lighting the sky and the far skyline and nothing nearer.

✅ **And that placement is thematically right for free: the storm is moving away.** The worst of
it is now behind them and receding, which the grace beat wants and which nobody has to say.

**Everything else in the shot is unchanged.** Only the weather block is rewritten.

```prompt
Generate a still photograph. Use the attached image as the reference for the place only: the same supermarket car park filled with a camp of shelters, the same wet cracked tarmac and standing water, the same scattered litter and broken glass, the same burning oil drum, the same muted cool colour and grain.

Two things are different from that image. It is now a wet night in a storm, and the camera is down at the fire with the two men rather than standing back from them.

Camera: a 50mm lens at chest height, just above the rim of the burning drum and about two metres from it, so the flames rise into the bottom of the frame very close to the lens and completely out of focus. The framing is slightly off level and the drum sits left of centre rather than squared to the frame.

Standing beyond the drum on the left of the frame, framed from the waist up and turned about thirty degrees toward it: the man from the first character reference. Standing on the right of the frame, a little further back from the drum and turned more square on: the man from the second character reference. They are not the same distance from the fire and they are not mirrored.

Both men have their hands held out over the flames, flat with the palms down and the fingers together, and both are looking down into the fire rather than at each other and never toward the camera. On each face the corners of the mouth are drawn very slightly back without the lips parting, the outer corners of the eyes are creased, and the brow is level and loose.

Light: the fire in the drum is the only light that reaches the two men, and it sits below both faces, so both are lit from underneath by the same warm moving light — the undersides of their jaws, brows and hands catching it, the tops of their heads and shoulders falling into shadow, and both men lit identically by it. Nothing else in the picture lights them. The shop behind is dark, its sign unlit and giving off no light at all, and there is no working lamp anywhere in the car park.

Far behind them, low down and a long way off beyond the buildings, a sheet of lightning is flickering inside the cloud. It lights the sky a cold blue and picks out the roofline of the shop and the far edge of the camp as flat black silhouettes against it, and it reaches nothing nearer than that — the two men, the drum and the ground around them stay lit only by the fire. Beyond the fire's reach the camp falls away to solid black against that cold sky.

Heavy rain is falling through the whole frame, running off the rim of the drum and off their shoulders, and showing brightest where it crosses the firelight and invisible in the dark beyond it.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, no colour grading push, and skin rendered with its real texture and unevenness rather than smoothed.

Compose for a 16:9 frame.

Thanks.
```

**Two extra checks on top of the list above:**

6. **Did the lightning stay in the background?** If it is lighting their faces or the ground around
   the drum, reject — the fire lighting both men identically is the shot's whole argument, and a
   flash over the top of it deletes that.
7. **Is the sky the only thing it lit**, with the shop roofline and the far camp reading as flat
   black silhouettes against it?

#### 🔴 Amended 2026-08-30: the reference is now the accepted `12c` frame, not the camp wide

**Why this changed on its own, with nobody deciding anything.** `12a` was written on 2026-08-28,
when the only night fire in the film was the small one in the scene-10 camp wide. Since then
**`12c` and `12d` have both been shot and accepted — and they are the same drum, the same fire and
the same rain, seconds later in story time.** They now come *after* `12a` in the cut and *before*
it in production, which means the continuity flows backwards: **`12a` has to match them, not the
plate it was written against.**

**The one change: swap the location reference.** Everything else in the shot — the design, the
lighting argument, the two-Character staging, the weather revision — is unchanged.

| Was | Now |
| --- | --- |
| `@Bob`, `@Future-Tarquin`, **the accepted camp wide** *(place)* | `@Bob`, `@Future-Tarquin`, **the accepted `12c` frame** *(the drum, the fire, the rain, the grain)* |

**Why not attach both.** Four slots at the identity frontier is the wrong thing to spend. Two
Characters in one frame is already the unknown this shot exists to answer, and every extra
reference is documented dilution. **The camp wide was only ever buying the ground and the
silhouettes — and this frame is near-black beyond the fire's reach anyway, so prose covers it.**
The drum is the thing that must match, and only `12c` has it.
*(Fallback: if the tarmac, the standing water and the litter come back wrong, add the camp wide as
a fourth attachment in round 2 — one change at a time.)*

#### 📐 What the accepted frames now fix, checked against the images

- 🔴 **The drum is RUSTED.** `12c` and the camp wide agree — bare rust-orange steel, wide mouth.
  ⚠️ **`12d`'s drum came back pale galvanised grey, and it is the odd one out.** Not worth a
  re-shoot: in `12d` it is a small firelit shape at the very bottom of a tall plate and the tilt
  leaves it in the first second. **But `12a` must be rusted**, because `12a` is the shot that shows
  the drum in context and `12c` is a hard cut away from it.
- 🔑 **Tarquin's wardrobe is now established by two accepted frames** — `11b(i)` and `12c` both show
  a **dark olive canvas jacket with a frayed cuff**, on a weathered hand. Both came from
  `@Future-Tarquin` with no wardrobe description, so **the Character carries it and it stays
  undescribed** ([§19](../../google-flow/nano-banana-2.md)). It becomes a **candidate check**, not
  a prompt clause.
- ✅ **`12c` and `12d` both go to solid black beyond the fire**, where `12a` keeps the shop
  roofline and the far camp against the lightning. **That is the right direction, not a mismatch:**
  `12a` establishes the place, then the sequence tightens to an insert and then to abstraction.
  `12a` is the only shot in scene 12 that can place these two men, so it keeps its background.

#### The gates, re-run — `12a` holds as designed

1. **Job.** `11d` was Bob's line. `12a` is the first frame in ninety seconds with two legible
   faces in it, and the class distance closing is argued by one fire reaching both of them
   identically. Nothing before it does that.
2. **Visible cost.** Two men warming their hands on a burning bin, in the rain, in a car park
   they live in. Satisfied in frame.
3. **Light source.** Named, in the world, and it is the shot's whole argument.

```prompt
Generate a still photograph. Use the attached image as the reference for the burning drum and for the look of the picture: the same rusted metal drum with a fire burning in it, the same size and colour of flame, the same heavy rain showing bright where it crosses the firelight, the same muted colour, deep black shadows and 35mm film grain.

That image is a close insert of the drum on its own. This picture is pulled back from it, and there are two men standing at the fire on a wet night in a supermarket car park that has been filled with a camp of makeshift shelters.

Camera: a 50mm lens at chest height, just above the rim of the burning drum and about two metres from it, so the flames rise into the bottom of the frame very close to the lens and completely out of focus. The framing is slightly off level and the drum sits left of centre rather than squared to the frame.

Standing beyond the drum on the left of the frame, framed from the waist up and turned about thirty degrees toward it: the man from the first character reference. Standing on the right of the frame, a little further back from the drum and turned more square on: the man from the second character reference. They are not the same distance from the fire and they are not mirrored.

Both men have their hands held out over the flames, flat with the palms down and the fingers together, and both are looking down into the fire rather than at each other and never toward the camera. On each face the corners of the mouth are drawn very slightly back without the lips parting, the outer corners of the eyes are creased, and the brow is level and loose.

Light: the fire in the drum is the only light that reaches the two men, and it sits below both faces, so both are lit from underneath by the same warm moving light — the undersides of their jaws, brows and hands catching it, the tops of their heads and shoulders falling into shadow, and both men lit identically by it. Nothing else in the picture lights them. There is no working lamp anywhere in the car park, and no lit window and no lit sign of any kind.

The ground around the drum is cracked tarmac, soaked and holding standing water that catches the firelight, with scattered litter, crushed cans and broken glass across it. Beyond the reach of the fire the camp of tarpaulins and makeshift shelters falls away into solid black.

Far behind them, low down and a long way off beyond the buildings, a sheet of lightning is flickering inside the cloud. It lights the sky a cold blue and picks out the roofline of a low supermarket building and the far edge of the camp as flat black silhouettes against it, and it reaches nothing nearer than that — the two men, the drum and the ground around them stay lit only by the fire.

Heavy rain is falling through the whole frame, running off the rim of the drum and off their shoulders, and showing brightest where it crosses the firelight and invisible in the dark beyond it.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, no colour grading push, and skin rendered with its real texture and unevenness rather than smoothed.

Compose for a 16:9 frame.

Thanks.
```

**Two more checks, on top of the seven above:**

8. **Is the drum rusted steel**, matching `12c` and the camp wide — not pale grey?
9. **Is Tarquin in the dark olive canvas jacket** from `11b(i)` and `12c`? If `@Future-Tarquin`
   came back in something else, that is the Character drifting and it is worth a re-roll, because
   `12c`'s hand is the very next shot.

#### ✅ ACCEPTED 2026-08-30 (Jack) — **and it answers the film's biggest open question**

*"Forget 12a, the one we did works."* The shot was already made before the 2026-08-30 amendment
was written, so **the amendment above was never needed and is superseded** — it is kept only
because its two continuity findings (the rusted drum, the olive canvas jacket) stand on their own.

🔑 **THE FINDING, and it is the most valuable one in the film so far: two Flow Characters
held in one frame.** Camping had been redesigned twice to avoid exactly this — `2b` needed Veo 3.1
to hold two faces through a laugh in a locked interior, and `8b` only worked by retreating to a
forty-metre long lens that took faces out of the argument entirely. **The documented failure —
features blending between the two men, faces swapping, one identity collapsing — did not happen.**

**What we think bought it, worth reusing before it is forgotten:**

1. **Each Character anchored to a named side of the frame** — *"on the left of the frame… on the
   right of the frame"* — rather than left to the model to infer. This is the documented fix and it
   is now house-tested.
2. **A still, not a clip.** Identity has to hold for one frame, not through motion.
3. **Two visually unalike men**, which the sources name as the thing that keeps identities apart.
4. **No appearance description for either** ([§19](../../google-flow/nano-banana-2.md)) — only
   position, action and face muscles.

🔴 **So scene 11 is no longer gated.** `11a`, `11c` and `11d` are all two-men-talking
frames, and they were the shots this unknown was blocking. **Go there next, while the recipe is
fresh** — same anchoring, same stills-first discipline.

⚠️ **The master is NOT banked in `camera/reference/`.** It exists in Flow only. Every
other accepted frame in 10–12 has a file beside it, and `12a` is now a reference that `11a`,
`11c` and `11d` will all want to match. **Save it as
`camera/reference/scene-12a-two-men-fire-ACCEPTED.png`.**

🔴 **The debt inverts, exactly as the 2026-08-29 ruling said it would.** `@Bob` is now the
Bob of `10d` and all of `11`–`12` — five shots — and **`8c(i)` is the single frame
that disagrees.** The outstanding job is therefore a **re-shoot of `8c(i)` against the Character**,
*not* a rebuild of the Character. That is the cheaper of the two and it was the point of running
`12a` first.

---

### 12b — ~~cans clinked~~ · **struck 2026-08-29 (Jack)**

**"Basically the same as the last one, they are just talking."** Correct, and it fails
[gate 1](../../cinematography/principles.md): the same two men, the same drum, the same light,
the same distance — a second setup that does nothing the first did not. **A shot whose only new
information is dialogue is not a shot in a film with no dialogue in the pictures.**

⚠️ **Struck as a SETUP, not as a beat.** Canon's *"the apology happens the man way — nothing said
straight"* still has to land. **It lands inside `12a`'s clip and in the narration**, which is where
it always belonged: two men looking into a fire, not at each other, is already the whole gesture.
If a clink is wanted it is a **sound cue over `12a`**, not a picture. *(No credits spent, nothing
lost.)*

### 12c — the newspaper goes on the fire · **still** · written 2026-08-29, unrun

**Canon:** *"The newspaper goes on the fire. It's cold. It burns."* Plus the transcript ruling —
Kai worried they would not burn the last newspaper on Earth, and Jack settled it: *"They don't
care what that is. They're in survival mode."*

#### The job — and it is the film's actual punchline

**Gate 1.** `12a` showed us two men who have stopped being different. `12c` does something none of
the film has done yet: **it destroys the object the whole story has been about, for warmth, without
ceremony.** The headline we spent `11b` making legible — the last worker replaced, the last
newspaper ever printed — is fuel. **The thesis is burned for heat, and nobody in the frame thinks
it is a moment.** That is the sharpest thing in the film and it needs no narration at all.

**So the shot must be an insert, not a two-shot.** No faces, one hand. `12a` spent the faces; a
third wide of the same two men would flatten the ending.

#### 🔑 The design — backlit newsprint, and the text survives because the flame has not taken it yet

**The optical fact the shot is built on:** a sheet of newsprint held over a flame **goes
translucent and glows**, and the columns of type read through it as dark lines. It is real, it is
free, and it makes the paper the brightest object in a near-black frame without a single added
light. `frame.md` §5's *one bright anchor* is the paper itself.

🔴 **Protect the headline the way `11b` did.** Load-bearing text is our known failure
([`image-prompting.md` §5](../../flow/image-prompting.md)) and `11b(i)` only won because the page
was **flat, pinned and fully inside the light**. **A curling, burning page is exactly where a
headline morphs.** So the still is the moment *before* the flame takes it: **the page lands flat
across the fire, headline square to camera and fully readable, with only one corner browned and
just catching.** The burn-through is the clip's job, over frames where the words are already
established.

**One piece of text only.** The masthead date is `11c`'s job. Two strings in one frame is how we
lose both.

| Layer | What |
| --- | --- |
| **Foreground** | Flame breaking into the bottom of frame, very close, thrown out of focus — and the hand entering from the right, releasing |
| **Midground** | The newspaper, flat across the fire, glowing from beneath. **The focal point** |
| **Background** | The far rim of the drum, then solid black |

**Withheld: both faces, and whose hand it is.** A sleeve and a wrist. The audience knows both men
are there because `12a` just showed them.

#### 🔒 Camera: locked, and angled DOWN — because `12d` is the film's last camera move

**This is a structural constraint, not a preference.** [`style.md`](./style.md) has the ending as
*"the newspaper burns, the camera pans up, the rising embers become the bad code."* The motion
budget says a single move in a still body of work lands with outsized force **and only if the
stillness around it is real** — so **the tilt-up is spent once, in `12d`, and `12c` is locked.**

`12c` looks **down** into the fire so the page can be seen flat. `12d` is a **separate setup** at
the drum rim looking up. They join on a match to the flame, not a continuous move. **Do not put a
drift or a push in `12c`** — it would spend the ending's move a shot early.

#### Sequencing note

**Ideally run after `12a` is accepted**, so this can attach the accepted `12a` frame and inherit
its exact drum and firelight. Written now because it stands on its own — the frame is almost
entirely flame and black, and the only set piece is the drum rim.

**Attachments: the accepted camp wide (location) only.** No Character — there is no face and no
body, only a sleeve, so casting one would offer identity and get nothing back.
Enhance Prompt **off**. **4K** — the headline is the shot.

```prompt
Generate a still photograph. Use the attached image as the reference for the place and the fire only: the same ruined supermarket car park at night, the same rusted metal drum with a fire burning in it, the same heavy rain, the same muted cool colour and grain.

Two things are different from that image. The camera is now right at the drum instead of standing back from it, and the fire in the drum is the only light in the whole picture — there is no daylight, no lamp, no lit sign, and everything the firelight does not reach is solid black.

Camera: a 50mm lens held just above the rim of the drum and about half a metre from it, angled down into the fire, so the picture is almost entirely flame, paper and darkness. The framing is slightly off level and the drum is not squared to the frame.

Lying flat across the top of the fire, filling the middle of the picture and square on to the camera: a single open sheet of newspaper. The flames are underneath it and behind it, so the paper is lit from below and has gone translucent and is glowing a hot orange, and the columns of type on it show through the glow as dark lines. Across the top of the sheet, sharply in focus and unobstructed, the headline reads "BRITAIN'S LAST WORKER REPLACED BY AI" in heavy black condensed capitals. That headline is the only legible text anywhere in the picture, and every other line of type on the page is too small and too soft to read.

Only the far right corner of the sheet has caught: it has gone brown and is curling upward, with a thin line of flame creeping along that one edge. The rest of the page is still flat and intact.

Entering from the right edge of the frame, close to the lens and thrown out of focus: a man's hand and forearm, palm down and fingers open, just having let the paper go. His sleeve is soaked. Nothing else of him is in the picture.

Rising into the bottom of the frame, very close to the lens and completely out of focus: the flames themselves, a soft orange blur across the bottom edge.

Beyond the paper, the far rim of the drum catches a hard orange edge of light, and past it the picture falls away to solid black. No part of the camp behind is visible.

Heavy rain is falling, showing as bright streaks where it crosses the firelight, hissing off the drum rim, and invisible in the black beyond.

A documentary press photograph on 35mm film: natural grain visible in the shadows, deep black shadows, no colour grading push.

Compose for a 16:9 frame.

Thanks.
```

**Choosing between candidates — the text first:**

1. 🔴 **Is the headline exact, sharp and complete?** This is the one string in the frame and the
   whole beat is that we can read what is being destroyed. Garbled or partial is a reject.
2. **Is the rest of the page properly unreadable** — soft and small — rather than garbled text
   competing with the headline?
3. **Is the paper glowing from underneath**, translucent with the type showing through, rather
   than just a white sheet sitting on a fire?
4. **Has only one corner caught?** If the whole page is alight the still has arrived too late and
   the words go with it.
5. **The hand** — one hand, five fingers, soft, and no face or body anywhere in frame.
6. **Real black** beyond the drum, with no camp, no sign and no ambient lift.

⚠️ [Trigger 3](../../flow/failure-modes.md) exposure, same as `12a`. If it blocks:
1) `rusted metal drum with a fire burning in it` → *a metal bin with a fire in it*;
2) drop the word `ruined`.

**If the headline morphs after two rounds**, the fix is not another round — it is
[`image-prompting.md` §5](../../flow/image-prompting.md)'s standing answer and the one we already
took for the fascia: **generate the page blank or unreadable and comp the headline in post.** It
is the same job as the `W-AI-trose` letters, on the same timeline, in the same pass.

#### ✅ ACCEPTED 2026-08-29, round 2 — master at [`camera/reference/scene-12c-newspaper-burns-ACCEPTED.png`](./camera/reference/scene-12c-newspaper-burns-ACCEPTED.png)

**Round 1** ([banked](./camera/reference/scene-12c-round1.png)) got the hard part first time — the
headline exact and sharp, the body copy properly unreadable, real black past the drum, one corner
caught. **It was rejected on one thing: the hand.** It came back pale, smooth, unweathered and
**in sharp focus**, splayed palm-down like it was *presenting* the paper. On a man who has lived
in a car park camp for five years it quietly contradicted all of 10–12, and it was the second
thing the eye landed on.

🔑 **The fix was the 7a move again: describe the hand as anatomy and condition, not as position.**
Thick-knuckled, weathered and cracked, dirt engrained in the creases, short broken nails, a frayed
soaked cuff — and the gesture changed from held-flat-open to **loosely curled and falling open**,
releasing. Round 2 landed it in one.
**Recorded as a general rule: [§19](../../google-flow/nano-banana-2.md)'s no-appearance-description
rule applies to *cast characters*. An unbound body part is the opposite case — it gets nothing
unless you describe it, and it will default to young, clean and generic.**

⚠️ **The picture beat the prompt, and we kept the picture** *(the 7a shoulder-colour pattern
again)*. The design's central optical idea was **backlit translucent newsprint glowing from
beneath, with the type reading through it**. The engine did not do it — it front-lit an opaque
sheet — and **that is better, because a glowing translucent page would have made the headline
harder to read, and the headline is the entire shot.** The clause was dropped from round 2 rather
than fought for.

🟡 **Accepted with one known softness:** round 1's drum was squared and centred, reading slightly
diagrammatic. Round 2's *"off to one side"* clause improved it. Not chased further — the black and
the flame carry it.

**⚠️ Open call, one line, does not block the run:** *whose hand is it?* The prompt says only "a
man's hand", which is deliberate and probably right. **If we name one, it should be Bob's** — he
is the one in survival mode and has been for five years, so him feeding it in without ceremony
*is* Jack's *"they don't care what that is"*. **Tarquin's hand would read as guilt or as erasing
evidence**, which is a different and much more literal beat than the one canon wants.

### 12d — the tilt up, embers into bad code · **still (plate)** · written 2026-08-29, unrun

**Canon:** *"Camera pans up with the smoke — the rising embers resolve into the bad code. Hold.
End."* From the transcript, Kai: *"the camera just pans up into the sky and maybe the smoke could
be the bad code. That's sick."*

#### The job — the film's exit, and the narrator finally showing itself

**Gate 1.** `12c` destroyed the object. `12d` leaves the world. **It is the only shot in the film
that steps outside the story, and what it says is who has been talking for ninety seconds:** the
narrator is a superintelligence from the future, and this frame makes it out of the sparks coming
off a fire two men lit to stay warm. **The thing that ends us is assembled from what we burned.**
Nobody says that; the picture does it.

**Gate 2 is satisfied inside the move itself.** The tilt **starts on the cost** — the drum, the
wreckage, the two men as black silhouettes — **and ends on abstraction.** That ordering is the
whole reason it is a move and not a cut: we are carried from the men to the machine, and we can
feel ourselves leaving them.

**Gate 3.** Two named sources, and they are the film's palette in one gesture: **the fire from
below, warm, the only earned heat in the story** ([`style.md`](./style.md)), and **the storm sky
above, cold blue, the lightning that has been receding since `12a`.** The tilt travels warm to
cool. That is the argument.

#### 🔒 This is the only camera move in the film. Spend it here.

[`motion-and-cutting.md` §1](../../cinematography/motion-and-cutting.md): *a single moving shot in
a still body of work lands with outsized force — and only if the stillness around it is real.*
Every shot in `10`–`12` has been locked, and `12c` was locked on purpose so this one could move.
**Do not put a drift, a push or a sway anywhere in scene 12 except here.**

#### 🔴 Three layers, and only the first is Flow's

Same ruling as the `10b` lightning, for the same reason, and the register anchor already set the
precedent — [`docs/images/register-anchor.md`](../../images/register-anchor.md) records that the
species' commit log in the original GPOM panel was **a code overlay drawn descending a line of
light**, not a generation.

| Layer | Tool | What |
| --- | --- | --- |
| 1. The plate | **Flow** | A **9:16 vertical** clip, camera **locked**: fire and silhouettes at the bottom, smoke and embers rising through the middle, storm sky at the top |
| 2. The move | **Premiere** | The tilt — a position keyframe travelling up the tall plate, eased, reframed to 16:9, ending held on sky |
| 3. The code | **ffmpeg** | The embers resolving into glyphs |

**Why the plate is vertical and the move is post.** [`hybrid-method.md`](../../video-fx/hybrid-method.md)
is explicit — Veo animates the world with its camera locked and **post moves the camera**, and
camera translation is what fires the regeneration bug. Generating tall gives us the travel, and
Premiere gives us an exactly eased tilt that ends **exactly** on the last narration word, which a
generator cannot be asked to time.

**Why the code is ffmpeg.** Premiere's API cannot set a string at all
([CLAUDE.md](../../../CLAUDE.md)), Flow cannot render legible characters through a change of light
— proven twice on the fascia ([§21](../../google-flow/nano-banana-2.md)) and once on the flash —
and **the bad code is brand, so it must be identical everywhere it appears rather than re-rolled
per shot.**

🔑 **The code ASCENDS here, where the anchor's descended.** Same device, mirrored, at the opposite
end of the story. Worth doing deliberately.

**Recommended treatment, and it is a call worth arguing with:** sparse thin monospace glyphs, cool
pale — the register's *"one thin blade of cool light"* colour, not green, never Matrix — drifting
up along the ember paths and mostly **illegible**. 🔴 **And no wordmark.** *The film ending on a
logo turns the story into an advert*, and the closing narration has to be the last thing the
audience takes. **The mark belongs on an end card after the hold, not fused into the final image.**

#### The plate

**Attachments, roles named explicitly:** the accepted `12c` frame **for the drum and the fire**,
and the accepted camp wide **for the sky, the rain and the camp**. No Character — both men are
black silhouettes and there is no face anywhere, so casting one offers identity and gets nothing
back.
Enhance Prompt **off**. **4K.** 🔴 **Vertical 9:16** — this is the one shot in the film that is not
generated 16:9, and it is deliberate.

```prompt
Generate a still photograph in a tall vertical 9:16 format. Use the first attached image as the reference for the burning drum and its fire, and the second attached image as the reference for the place, the rain and the stormy night sky.

The camera is low and a little behind two men who are standing at the fire, looking past them and steeply upward, so the picture is mostly sky.

Across the very bottom of the tall frame: the top of the rusted drum with the fire burning in it, and on either side of it the heads and shoulders of two men, rendered as solid black silhouettes with no faces and no detail, rimmed along one edge by the firelight. They occupy only the bottom fifth of the picture.

Rising from the fire and filling the whole middle of the tall frame: a column of smoke, thin and torn, drifting upward and spreading as it climbs. Carried up inside it, hundreds of small orange embers, brightest and densest just above the flames and thinning out as they rise, until near the top of the frame there are only a few isolated sparks still glowing.

Filling the top half of the tall frame: a heavy stormy night sky, low cloud lit a cold blue from within by distant sheet lightning far away on the horizon. The cloud has real structure and depth rather than being flat.

Light: the fire is the only warm light and it is at the very bottom, lighting the smoke from beneath so the lowest part of the column glows orange and the upper part goes cold and grey. The sky's cold blue is the only other light. Between them, the middle of the frame is dark. The picture travels from warm at the bottom to cold at the top.

Heavy rain is falling through the whole frame, showing bright where it crosses the firelight at the bottom and as fine cold streaks against the cloud higher up.

There is no text anywhere in the picture, no sign, no lettering, and no lit window or lamp of any kind.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, deep black shadows, no colour grading push.

Compose for a tall vertical 9:16 frame.

Thanks.
```

**Choosing between candidates:**

1. 🔴 **Is it genuinely tall and is there enough travel?** The whole point is a plate Premiere can
   tilt up through. If the composition is squashed into the middle there is nothing to move across.
2. **Are the men only silhouettes**, faceless, confined to the bottom fifth? Any face detail and
   we have accidentally shot another two-shot.
3. **Does the frame travel warm to cold** from bottom to top, with a genuinely dark middle?
4. **Do the embers thin out as they rise**, so there is somewhere for the code to take over?
5. **No text anywhere** — the fascia must not creep back in.
6. **Real black**, and cloud with structure rather than a flat grey wash.

⚠️ [Trigger 3](../../flow/failure-modes.md): if it blocks, `rusted drum with the fire burning in
it` → *a metal bin with a fire in it*.

#### ✅ ACCEPTED 2026-08-29, first take — master at [`camera/reference/scene-12d-embers-plate-ACCEPTED.png`](./camera/reference/scene-12d-embers-plate-ACCEPTED.png)

*"This one is really cool."* Landed in one. Genuinely tall with real travel, warm at the bottom
and cold at the top with a dark middle, embers thinning as they rise, cloud with structure, no
text anywhere.

🔑 **The picture improved on the prompt, and we kept it.** The brief confined the two men to *"the
bottom fifth"*; the frame runs them up roughly the lower **forty percent**, flanking the smoke
column on both sides. **That is better, and it is a compositional idea the prompt did not have:
the two silhouettes become a doorway the smoke rises through** — a frame-within-a-frame
([`frame.md` §4](../../cinematography/frame.md)), which does the containment for free and makes
the escape upward feel like an escape. It also means **the Premiere tilt passes between them**,
which is a much better exit than rising off the top of two small heads. *(Third time this session
the frame beat the brief — see the `12c` backlight note and 7a's shoulder.)*

⚠️ **Consequence for the tilt:** the men are taller in frame than planned, so the usable travel
starts higher up. **Set the tilt's start frame on the drum and the flame, not on the silhouettes'
shoulders**, or the move begins on black.

### 12d — the clip · **video** · ✅ ACCEPTED 2026-08-30

🔴 **Generated 9:16, camera locked.** The tilt is Premiere's, over this tall plate. A generated
camera move here would cost us the exact timing on the final narration word *and* put us on the
translation bug. *(Prompt not recorded in full — the ledger is stills-only per the 2026-08-26
ruling.)*

✅ **It worked** (Jack, 2026-08-30). **So the last shot of the film exists**, and with it the
whole tail of scene 12 bar `12a`.

🔑 **The locked-camera rule is now proven on the hardest frame we had for it.** `12d` is a
tall plate of rising smoke and drifting embers — continuous, unstructured motion filling the middle
of the frame, which is exactly the geometry that usually invites a generated drift. **Locking the
camera and leaving the move to Premiere held.** That is the third clip in scene 10–12 to land on
the first take under the same rule ([`hybrid-method.md`](../../video-fx/hybrid-method.md)).

🔴 **What is now owed downstream, and none of it is Flow's:**

| Layer | Tool | Status |
| --- | --- | --- |
| The plate | Flow | ✅ done — still and clip both |
| The tilt | **Premiere** | ⬜ owed — eased, reframed to 16:9, ending exactly on the last narration word. ⚠️ **Start the tilt on the drum and the flame, not on the silhouettes' shoulders** — the men run up ~40% of the frame, not the briefed bottom fifth |
| The code | **ffmpeg** | ⬜ owed — ascending glyphs along the ember paths, cool pale, mostly illegible, no wordmark |

✅ **Unblocked 2026-08-30** — this was waiting on `12a` in case it changed the fire, the drum or
the weather and forced the tilt to be built twice. `12a` is shot, so both post jobs can start.


### 12e — the last frame, 16:9 · **still** · written 2026-09-09, unrun

**Jack, 2026-09-09: *"it is the last image of the story, it should be 16:9, use the characters but
no reference image."*** New shot rather than a rewrite of
[`12d`](#12d--the-tilt-up-embers-into-bad-code--still-plate--written-2026-08-29-unrun), whose
plate and clip are both accepted.

> ### ⚠️ Round 1 was wrong, and the misread is worth recording
>
> **Jack: *"this prompt looks nothing like the image we want to make 16:9."*** Round 1 invented a
> new ending — a wide of the ruined car park, the two men **firelit and facing camera**, a
> collapsed trolley shelter, a clamped car, a shopping trolley.
>
> 🔑 **The error was reading *"use the characters"* as a statement about the picture.** It is a
> statement about the **inputs**: 12d was built on two attached reference images, and Jack is
> swapping those for cast Characters. **Mechanism, not content.** Nothing about the frame was
> being changed except its shape.
>
> **The general rule: when the ask is a format change, change the format.** A request to reframe
> an accepted image is not an invitation to redesign it, and every clause added beyond the aspect
> ratio is a clause the accepted frame did not have and did not need. **This block is 12d's
> prompt with the geometry re-proportioned and the reference sentence replaced.** Nothing else.

#### ⚠️ 16:9 removes the tilt — flagged once, and it is Jack's call

12d's plate is 9:16 *because* Premiere travels up it
([generate tall, move the camera in post](../../video-fx/hybrid-method.md)). A 16:9 frame has no
vertical travel in it. ⬜ **Cheapest reading, nothing discarded: 12d tilts up and ends on sky, and
12e is the held final image after it.**

#### ⚠️ Casting Characters onto silhouettes is the one live risk

12d's own note says casting there *"offers identity and gets nothing back"* — the men are faceless
black shapes. **A cast Character is an instruction to include that person**, so with `@Bob` and
`@Future-Tarquin` attached the engine has more reason to render faces than 12d ever did.

**The counter is written positively and then repeated:** *"solid black silhouettes rimmed along
one edge by the firelight"* in the body, and *"the two men stay solid black silhouettes"* in the
constraints — the same belt-and-braces that
[kept 7a's lips parted](#7a--the-consulting-room--still--accepted).
⬜ **If faces come back, drop the Characters entirely** — 12d landed first take without them.

⚠️ **`@Future-Tarquin`, never the old name** — it
[put a destitution trigger into every field Flow scans](../../flow/failure-modes.md#a5-the-five-triggers-badcodes-own).

**Model: Nano Banana Pro. Cast `@Bob` and `@Future-Tarquin`. Attach no reference image.**
Enhance Prompt **off**. **4K.** Paste into the **prompt box**:

```prompt
Generate a still photograph in a wide 16:9 format.

The camera is low and a little behind two men who are standing at a fire, looking past them and steeply upward, so the picture is mostly sky.

Across the bottom of the frame: the top of a battered metal drum with the fire burning in it, and on either side of it the heads and shoulders of the two cast characters, standing close in on either side of the smoke and rendered as solid black silhouettes, rimmed along one edge by the firelight. They occupy the lower third of the picture.

Rising from the fire and filling the middle of the frame: a column of smoke, thin and torn, drifting upward and spreading as it climbs. Carried up inside it, hundreds of small orange embers, brightest and densest just above the flames and thinning out as they rise, until near the top of the frame there are only a few isolated sparks still glowing.

Filling the upper half of the frame: a heavy stormy night sky, low cloud lit a cold blue from within by distant sheet lightning far away on the horizon. The cloud has real structure and depth rather than being flat.

Light: the fire is the only warm light and it is at the bottom, lighting the smoke from beneath so the lowest part of the column glows orange and the upper part goes cold and grey. The sky's cold blue is the only other light. Between them the middle of the frame is dark. The picture travels from warm at the bottom to cold at the top.

Heavy rain is falling through the whole frame, showing bright where it crosses the firelight at the bottom and as fine cold streaks against the cloud higher up.

The two men stay solid black silhouettes.

There is no text anywhere in the picture, no sign, no lettering, and no lit window or lamp of any kind.

A documentary press photograph on 35mm film: natural grain visible in the shadows, muted cool colour, deep black shadows, no colour grading push.

Compose for a wide 16:9 frame.

Thanks.
```

**Choosing between candidates** — [12d's list](#12d--the-tilt-up-embers-into-bad-code--still-plate--written-2026-08-29-unrun),
minus the travel question and plus one:

1. 🔴 **Are the men still silhouettes?** The new risk. Any face detail and the Characters have won.
2. **Does the frame travel warm to cold**, bottom to top, with a genuinely dark middle?
3. **Do the embers thin out as they rise**, leaving somewhere for the ffmpeg code layer? ⬜ There is
   much less vertical room for it in 16:9 than in the plate.
4. **No text anywhere.**
5. **Real black**, and cloud with structure rather than a flat wash.

⚠️ [Trigger 3](../../flow/failure-modes.md#a5-the-five-triggers-badcodes-own): if it blocks,
`battered metal drum` → *a metal bin with a fire in it*. Already softened from 12d's *rusted drum*.

---

#### ✅ 12e shot 2026-09-09, round 1 — and the casting risk did not fire

**The silhouettes held.** Both Characters cast and no face detail came back, which was the one
thing most likely to break. Warm-to-cold travel intact, cloud with real structure lit from within,
embers thinning as they rise, deep blacks, no text, and **the doorway composition survived the
reframe** — the two men flanking the column with the smoke escaping between them, which was the
best accident in the 9:16 and made it across.

⬜ **Two weaknesses noted and not yet acted on** *(Jack has moved to the clip, so these stand open
rather than blocking)*:

- **It is close to perfectly symmetrical** — drum dead centre, a man each side at equal distance,
  the cloud parting directly above the column. [Symmetry has no fixed meaning on its
  own](../../cinematography/frame.md#3-tension-versus-resolution), but centred subject **plus** no
  depth cue at the bottom tips it from *dread* toward *poster*. It read as a column in portrait;
  it reads as a composition in landscape.
- 🔴 **There is no ground.** The men and the drum float on black, so **nothing in frame carries the
  cost** — no wet tarmac, no bay line, no ruin. Acceptable in the 9:16, whose job was to be
  travelled *through*; a held final image has a bottom third doing no work.
  **The cheap fix is one clause: wet tarmac with a painted parking bay line catching the
  firelight.** The bay line alone says *this was a car park*, which is the whole argument, in one
  detail.

---

### 12e-y — the embers into the sky · **video** · written 2026-09-09, unrun

**Jack: *"where it follows the embers into the sky."***

#### 🔑 The embers do the following, not the camera — and that is the better shot

**In a locked frame the embers rise up through the picture and leave the top of it.** The eye goes
to motion before it goes to anything else
([`frame.md` §2](../../cinematography/frame.md#2-the-focal-point)), so **the viewer's eye performs
the tilt** while the frame holds. That is not a compromise version of the ask — it is the ask,
executed by the subject instead of the rig, and it costs nothing.

#### 🔴 Why the camera must not do it in Flow, and this time the reason is specific

Not just the standing ruling. **Tilting up out of a 16:9 frame means inventing new sky above the
frame edge, every frame.** That is the *pull-back* case — the dangerous direction — not the safe
one 8b-fog identified, where [a push-in crops into pixels the model already
has](#8b-fog--the-clip--video--ran-and-accepted-2026-09-08).

🔑 **And this exact geometry has already proved the locked rule once.**
[12d's clip](#12d--the-clip--video--accepted-2026-08-30) is *"a tall plate of rising smoke and
drifting embers — continuous, unstructured motion filling the middle of the frame, which is exactly
the geometry that usually invites a generated drift. Locking the camera and leaving the move to
Premiere held."* First take. **Same fire, same embers, same rain — just wider.**

#### ⬜ If a camera move is wanted on top, here is what a 16:9 plate actually supports

**Not the 12d tilt.** That move exists because the plate is tall; this one is not.

| | |
| --- | --- |
| **Generate at 4K** | Load-bearing. At 4K a 1920×1080 crop window is a 2× punch and can travel a full frame-height vertically, which is a real tilt. At 1080p source there is no travel at all without upscaling |
| ⚠️ **Omni's 4K is *upscaled*, not native** | So a 2× punch into it is effectively a 2× punch into 1080p. **It will be soft.** The heavy 35mm grain in this frame hides a lot of that, but do not expect it free |
| **Start on the drum and the flame** | Not on the silhouettes' shoulders — [the same note 12d's tilt carries](#12d--the-clip--video--accepted-2026-08-30) |
| 🥇 **The full-size version still exists** | The 9:16 plate and its accepted clip are untouched. **If the big travelling tilt is wanted, it is already shot** — 12e is then the held frame the tilt lands on |

#### ⚠️ Two risks, one new

- **Embers are small bright points on a dark field** — the same specular-shimmer family as
  [3c-y's broken glass](#3c-y--the-lane-hours-later--video--written-2026-09-09-unrun). ✅ **But this
  is the forgiving version:** embers are *supposed* to twinkle, drift and go out, so the model's
  natural failure mode and the subject's real behaviour point the same way. Nothing to spend a
  clause on.
- ⬜ **Rain over eight seconds risks [repeating texture tiling](../../google-flow/omni-flash.md)**
  — flagged on 8b-fog too, nothing to do at the prompt, worth *looking* for on playback.

#### ✅ The lightning is written as a place, not an object

*"Sheet lightning inside the cloud, far off"* — no source noun for the engine to go looking for,
which is [the lesson 3c-y paid for](#3c-y--the-lane-hours-later--video--written-2026-09-09-unrun).
It is also the film's one remaining dramatic beat: the storm **has been receding since 12a**, so a
distant pulse and a late roll of thunder is the weather ending the film rather than starting it.

**Model: Omni Flash. Tab: Frames. Attach the accepted 12e still as the frame — nothing else, no
Character, no Ingredients, no end frame. Generate at the highest resolution offered.** Paste into
the **prompt box on the Frames tab**:

```prompt
The attached image is a frame from this shot. Continue it from exactly this frame. The camera is locked off on a tripod and holds completely still for the whole shot.

The fire burns and moves in the drum. A steady stream of embers lifts off it and rises up through the middle of the frame, drifting sideways and spreading as it climbs, thinning out as it goes, until a few of them reach the top of the frame and pass out of it. Some go dark on the way up. The smoke rises and tears apart as it spreads.

The rain keeps falling at the same rate across the whole frame. Deep inside the cloud, far off, sheet lightning pulses once and then again a few seconds later. The cloud drifts very slowly.

The two men stay solid black silhouettes. One of them shifts his weight a little and settles.

Audio: heavy rain, rain hitting the metal drum, the fire, wind, and a long low roll of thunder arriving well after the lightning. No music and no voices.
Thanks.
```

**Post, in Premiere:**

1. ⬜ **The tilt, if it is wanted** — per the table above, and only on a 4K generation.
2. **A 10–15% speed adjustment** against the smooth-motion tell `[community]`.
3. **Film grain at 10–15% opacity**, matched to the plate rather than stacked on it.
4. ⬜ **The ffmpeg code layer** — ascending glyphs along the ember paths, cool pale, mostly
   illegible, **no wordmark**. ⚠️ There is far less vertical room for it in 16:9 than in the
   plate; if it will not read, that is an argument for the 9:16 ending, not for bigger glyphs.
5. ⚠️ **Nothing ships unmeasured** — `scripts/delivery-qc.sh`
   ([`delivery.md`](../../video-fx/delivery.md)).

---



### 12e-bc — BADCODE revealed by lightning · **video** · written 2026-09-14, unrun

**Jack, 2026-09-14:** *"BADCODE in a cyberpunk font, revealed in the sky by lightning illuminating it,
and the lightning should hit one of the letters and leave it sliced with embers like a lightsaber."* Start
frame: the accepted **12e** still. Web pass logged in
[`omni-flash.md`](../../google-flow/omni-flash.md) (tenth pass, 2026-09-14).

**Shot spec (shot-craft):**
- **Job:** the film's signature. The future intelligence signs the last frame. It sits after the story's
  real ending (12d), as packaging.
- **Gate 2 (monumental):** the visible cost is already in frame. Two wrecked men at a burning drum sit
  under the name.
- **Gate 3 (light):** the only thing that can light letters in a night storm is **the strike itself**.
  The fire is far too small.
- **One event, not two:** the bolt that cuts the O **is** the light that reveals the word. It's one
  strike (change/adherence trade).
- **The camera stays locked** (12e rule).

**Anti-slop and engine decisions:**
- 🔴 **Text is on screen only while the sky is lit.** The fewer frames a word must survive, the less it
  morphs (web pass 2026-08-28). The cut O is the only thing that has to hold afterwards.
- **One quoted string, `"BADCODE"`, and no colons.** Quotation marks switch Omni's text channel on. This
  is the one sanctioned exception to the no-quotes rule, since the speech trap needs a person speaking.
- **No "cyberpunk" and no "neon".** "Cyberpunk" pulls cyan and magenta glow and glitch. The typeface is
  described by shape instead: chamfered corners, straight uniform strokes, square counters.
- **The letters are solid dark metal standing in the cloud**, not an overlay. A physical object holds its
  shape better than floating type.
- **The word *flash* is never written** (house rule). The light is named by what it does.
- **The cut is "a thin glowing line of orange heat", with a few sparks.** A particle noun overdelivers,
  and the drum already supplies embers.
- **6s**: fewer frames for the letters to survive.

🔴 **Known risk, and the honest odds:** a lightning flash already **morphed a wordmark** on camping 10b.
A one-prompt clip that invents a word, spells it, cuts it and keeps it cut is four risks multiplied
(research, unverified). **Draft at 360p.** If the letters garble, switch routes rather than rewording:
1. **Nano Banana 2 still first**, with the letters and the cut O already faint in the cloud, then Frames
   only lights what is already there.
2. **ffmpeg** lays the exact word and cut over a Flow lightning clip.

⚠️ **Before upload:** `python3 scripts/photosensitivity-check.py` (more than 3 flashes in one second
fails, and real lightning restrikes).

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted 12e still.
**No end frame.** **Aspect:** 16:9. **Duration:** 6s. ⬜ Draft at 360p first.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

The rain keeps falling, the fire in the drum keeps burning and the two men sit where they are. About two seconds in, a single jagged bolt of lightning drops out of the clouds and the whole sky lights up bright white for a moment. In that light, enormous letters of dark weathered steel are revealed standing inside the storm clouds across the top of the frame, spelling "BADCODE" in a hard-edged futuristic typeface with sharp chamfered corners, straight strokes of even width and square inner shapes. The bolt strikes the letter O and cuts it cleanly in two with a diagonal slice, and the cut edges glow with a thin line of molten orange heat that drips a few sparks. The sky falls dark again and the letters sink back into the cloud, leaving only the glowing orange cut through the O still visible in the dark.

Audio: heavy rain, the crackle of the fire, and one enormous crack of thunder as the bolt strikes. No music and no voices.

Thanks.
```

**Check before accepting:**
- It spells **B-A-D-C-O-D-E**, in that order, with no extra or melted letters.
- There's one bolt, and it doesn't strobe.
- The O stays cut and doesn't heal.
- No cyan or pink neon.
- The two men don't move or change.
- The sparks stay a few, not a fireworks display.

### 12e-bc — round 1 result, and round 2 · written 2026-09-14, unrun

**Round 1, from Jack's frame:**
- ✅ **"BADCODE" spelled correctly** in solid steel letters across the sky, and the cut O plus the sparks
  landed.
- ❌ **The font is a plain blocky slab.** Jack: *"make the font better, more cyberpunk like and combined
  with the original badcode logo"*.
- ⚠️ **The sky came back bright, like overcast daylight**, not night.
- ⚠️ **The cut O reads as a white hole**, not a line of heat.

**Round 2 changes, one reason each:**
- **The C is the logo's curly brace** ([`docs/brand/`](../../brand/README.md)): red tip on top
  (`#cc2b37`), blue tip underneath (`#2696d4`), in the logo's **"BadCode"** mixed case.
- **"Cyberpunk" is now named, because Jack asked for it**, and its colour pull is fenced positively. The
  only colours in the letters are the brace's red and blue tips, and the rest is steel lit by thin
  cold-white edge lines.
- **The letterforms are described:** wide, angular, cut horizontal gaps through each stroke, and clipped
  corners.
- **The sky stays night.** The lightning lights the letters, not the whole sky.
- **The cut is a thin molten orange line, with no hole through it.**

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted 12e still.
**No end frame.** **Aspect:** 16:9. **Duration:** 6s.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed. It stays a dark stormy night throughout.

The rain keeps falling, the fire in the drum keeps burning and the two men sit where they are. About two seconds in, a single jagged bolt of lightning drops out of the clouds, and its cold white light catches enormous letters of dark brushed steel standing inside the storm clouds across the top of the frame, spelling "BadCode" in a cyberpunk film-title typeface: wide, angular letters with clipped corners, thin horizontal cuts sliced through every stroke, and a thin line of cold white light running along their edges. The C is drawn as a tall curly brace, its top tip glowing deep red and its bottom tip glowing bright blue, and those two tips are the only colour in the letters. The bolt strikes the letter o and slices it cleanly in two along a diagonal line, and the cut glows as a thin seam of molten orange heat that drips a few sparks. The lightning dies, the dark night returns and the letters sink back into the black clouds, leaving the red tip, the blue tip and the orange seam still glowing faintly in the dark.

Audio: heavy rain, the crackle of the fire, and one enormous crack of thunder as the bolt strikes. No music and no voices.

Thanks.
```

**Check before accepting:**
- It reads **BadCode** with the brace as the C. Red is on top and blue underneath, and the order must
  not flip.
- No pink, purple or cyan.
- The sky stays night.
- The o's cut is a seam, not a hole.
- The two men don't change.

### 12e-bc — round 2 ❌ and round 3: design the logo as a STILL first · written 2026-09-14, unrun

**Jack, 2026-09-14:** *"that made a terrible logo… it looks too much like the iron man logo. It should
look like the cyberpunk 2049 logo, combined with the origins logo from black ops 2, our original logo,
with an anime twist."*

🔑 **Route change: the logo gets designed on a Nano Banana 2 still, not in a video clip.** A logo is a
design that takes rounds, and every Omni roll costs a clip and reinvents the logo. The research route 2
applies: **the still carries the logo in frame 0**, and the Frames clip afterwards only lights what is
already there and cuts the o. Stills are also where the engine spells best.

**The three references, translated into traits.** The game names are never written into Flow: a named
trademark gets copied, and it can trip the filter.
- ⬜ **"Cyberpunk 2049" is read as *Cyberpunk 2077*** (heavy forward slant, letters sliced by horizontal
  glitch offsets, hard angular cuts). *Unverified which Jack meant. Blade Runner 2049's logo is a thin,
  widely spaced sans, the opposite.*
- **The *Black Ops 2* Origins logo:** ancient carved stone and old bronze, cracked and weathered, with
  light glowing out of the cracks like a relic.
- **Anime twist:** a thick clean black outline, hard-edged cel-shaded highlights, and crackling energy arcs
  around the letters like a power-up.
- **Our logo:** "BadCode", with the C as a curly brace, red tip on top and blue tip underneath.
  🔑 **The cracks carry the meaning:** red glow through *Bad* (the timeline that went wrong), blue glow
  through *ode* (the one sent back), and the brace is where the two meet.

**Why round 2 read as Iron Man** (*inferred*): steel plus a single glowing seam plus red, on a heroic
title, is the superhero-movie register. Round 3 swaps steel for cracked stone, adds the outline and slant,
and has no gold or chrome.

**Night-readable by construction:** the letters are dark, and **the glowing cracks are the bright anchor**,
so the logo reads before any lightning. The clip then only has to light it up.

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **Reference:** the accepted **12e** still,
and nothing else. **No Characters** (the silhouettes are in the reference). **Aspect:** 16:9.
**Outputs:** 2.

```prompt
SCENE:

The attached image is this exact scene and it is the reference for everything below the sky: keep the same two men as solid black silhouettes seen from behind, the same burning oil drum between them, the same sparks and smoke rising, the same falling rain and the same dark stormy night. The only change is a huge logo hanging in the storm clouds across the top of the frame.

Logo: the word "BadCode", enormous, standing in the dark clouds above the two men. The letters lean forward at a hard slant and are wide, heavy and angular, with sharp clipped corners, and each letter is sliced through by two thin horizontal cuts with the pieces slightly offset sideways, like a glitch. The letters are made of ancient carved dark stone with old bronze edges, cracked, chipped and weathered like a relic. The C is a tall curly brace carved from the same stone, with its top tip glowing deep red and its bottom tip glowing bright blue. Deep red light glows out through the cracks in the letters B, a and d, and bright blue light glows out through the cracks in the letters o, d and e, and the two colours meet at the brace. Every letter has a thick clean black outline and hard-edged cel-shaded highlights along its top edges, like a hand-drawn anime title card, and thin crackling arcs of white electricity flicker around the edges of the letters.

Light: it is night. The logo is dark stone, lit mainly by the red and blue light glowing from its own cracks and faintly by the storm, so it reads clearly against the black clouds without lighting up the sky. The fire below stays the brightest warm light in the frame, and the rain streaks catch a little of the red and blue.

Constraints: The letters spell BadCode exactly, with a capital B, a lowercase a and d, the curly brace as the C, and a lowercase o, d and e. The only colours in the logo are the deep red, the bright blue, the dark stone, the old bronze edges and the white electricity. The two men stay solid black silhouettes. Compose for a 16:9 frame.

Thanks.
```

**Check before accepting:**
- It reads **BadCode**, with the brace as the C. Red is on top, blue underneath.
- Red runs through Bad and blue through ode.
- It reads as **relic stone and glitch plus anime**, not chrome or a superhero logo.
- No pink, cyan or gold.
- The silhouettes, the drum and the rain match 12e.

**Then the clip:** once a still is accepted, a short Frames prompt has one bolt light it up and cut the o.

### 12e-bc — round 4: round 3 without the cartoon · written 2026-09-14, unrun

**Jack, 2026-09-14:** *"remove the cartoon elements and keep it realistic."* One change from round 3:
- **Out:** the thick black outline, the cel-shaded highlights and the electricity arcs.
- **In:** physical realism. It is a real object in real weather: rain running down the wet stone, cloud
  wrapping round the letters so they sit *inside* the storm, and glow that falls off into the mist.
- **No "hyper-realistic" or "cinematic".** Both are on the quality-word kill list, so the realism is
  described physically.
- **Kept:** the slant, the glitch slices, the relic stone and bronze, the brace, and red through *Bad*
  with blue through *ode*.

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **Reference:** the accepted **12e** still
only. **No Characters.** **Aspect:** 16:9. **Outputs:** 2.

```prompt
SCENE:

The attached image is this exact scene and it is the reference for everything below the sky: keep the same two men as solid black silhouettes seen from behind, the same burning oil drum between them, the same sparks and smoke rising, the same falling rain and the same dark stormy night. The only change is a huge logo standing in the storm clouds across the top of the frame, photographed as a real physical object in real weather.

Logo: the word "BadCode", enormous, standing inside the dark clouds above the two men. The letters lean forward at a hard slant and are wide, heavy and angular, with sharp clipped corners, and each letter is sliced through by two thin horizontal cuts with the pieces slightly offset sideways. The letters are made of ancient carved dark stone with worn bronze edges, cracked, chipped and weathered like a relic. The C is a tall curly brace carved from the same stone, with its top tip glowing deep red and its bottom tip glowing bright blue. Deep red light glows out through the cracks in the letters B, a and d, and bright blue light glows out through the cracks in the letters o, d and e, and the two colours meet at the brace. Rain runs down the wet stone and drips from the lower edges, and drifting cloud wraps around the bases of the letters so they sit inside the storm rather than in front of it.

Light: it is night. The logo is dark wet stone, lit by the red and blue light from its own cracks, which spills a soft red and blue haze into the surrounding cloud and falls away into darkness, and faintly by the storm. It reads clearly against the black clouds without lighting up the sky. The fire below stays the brightest warm light in the frame, and the rain streaks catch a little of the red and blue.

Details: real stone texture, rain-soaked surfaces, mist and fine natural grain, matching the look of the reference.

Constraints: The letters spell BadCode exactly, with a capital B, a lowercase a and d, the curly brace as the C, and a lowercase o, d and e. The only colours in the logo are the deep red, the bright blue, the dark stone and the worn bronze edges. The two men stay solid black silhouettes. Compose for a 16:9 frame.

Thanks.
```

**Check before accepting:**
- It reads **BadCode**, with the brace as the C. Red is on top, blue underneath.
- There's no outline and no drawn highlights.
- The letters sit *in* the cloud and don't look pasted on.
- The glow falls off into the mist.
- The silhouettes, drum and rain match 12e.

### 12e-bc — round 4 ✅ ACCEPTED 2026-09-14 (Jack: *"this one is great"*), and its clip · written 2026-09-14, unrun

**The still:** cracked stone "Bad{ode" in the storm, red glow through *Bad*, blue through *ode*, the brace
splitting the two, rain dripping off the letters, and cloud round their bases. Silhouettes, drum and rain
as in 12e.

**Shot spec (shot-craft):**
- **Job:** the signature lands with one blow. The logo is already there, and the strike is punctuation.
- **Lock, Move, Land** (web pass, community):
  - **Lock:** the letters hold exactly.
  - **Move:** one bolt hits the round letter right of the brace, and a glowing seam slices it.
  - **Land:** it settles on a held final frame, which the film ends on.
- **The camera stays locked** (12e rule), with the existing world motion only: rain, fire, sparks, slow
  cloud.
- **8s**, so the end has room to dwell after the strike.

**Engine decisions (web pass 2026-09-14, logged in `omni-flash.md`):**
- 🔴 **The word is never written and the logo is never described.** The image owns the lettering.
  Quoting text that is already in frame probably invites a redraw (*inferred*). It's "the stone letters".
- 🔴 **The target is "the round letter just to the right of the brace"**, not "the letter o", so the text
  channel stays out of it (*inferred*).
- **One lock sentence up front:** the letters keep their exact shape, spacing and spelling.
- **The crack glow stays steady.** A pulsing light makes fine texture crawl (community), so only the cut
  seam is new light.
- **"A few sparks"**, because particle nouns overdeliver. The lightning light is named by what it does, and
  the word *flash* isn't used.
- **No hype words and no camera shake.**

🔴 **Top risk:** the other letters redraw or re-spell when the lightning lights them. No source shows a
model cutting one object while holding the rest. **Draft at 360p for motion.** **Fallback, no more
rerolls:** generate the same clip with the logo removed, then lay the accepted still's logo back over it
in Premiere (screen or luma), and do the cut there.

⚠️ **Before upload:** `python3 scripts/photosensitivity-check.py`.

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted 12e-bc round-4
still. **No end frame.** **Aspect:** 16:9. **Duration:** 8s. ⬜ Draft at 360p first.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed. The stone letters in the sky keep their exact shape, spacing and spelling for the whole clip, and the red and blue glow in their cracks stays steady.

The rain keeps falling, the fire in the drum keeps burning with its sparks rising, the cloud drifts slowly around the bases of the letters, and the two men sit where they are. About three seconds in, a single jagged bolt of lightning drops out of the clouds behind the letters and strikes the round letter just to the right of the brace. For an instant cold white light washes across the whole sky and the wet stone. The bolt slices that one letter cleanly along a diagonal line, and the cut glows as a thin seam of molten orange heat that sheds a few sparks. The lightning is gone, the night returns, and the letters hang in the storm with the orange seam still glowing through the one sliced letter.

Audio: heavy rain, the crackle of the fire, and one enormous crack of thunder as the bolt strikes, rolling away into the distance. No music and no voices.

Thanks.
```

**Check before accepting:**
- **Every other letter is identical first frame to last**: same spelling, same brace, red on the left, blue
  on the right.
- One bolt, no strobe, one sliced letter.
- The seam stays and doesn't heal.
- The crack glow doesn't crawl or boil.
- No extra sparkles.
- The two men don't change.

### 12c-embers — the embers gather into the logo · **video (plate)** · written 2026-09-16, unrun

**Jack, 2026-09-16:** *"i want this end frame … to somehow spell out badcode … would embers spelling it out
in the sky be cool"*, then *"Embers gather into the logo please do this in a video prompt."* This is canon
12d's original idea (*"the rising embers resolve into the bad code"*), moved onto the drum close-up.
⬜ **Open:** does it **replace** the 12e-bc lightning reveal as the ending, or **hand over** to it? The film
can't reveal the logo twice.

**Three layers:**

| Layer | Tool | What |
| --- | --- | --- |
| 1. The plate | **Flow** (this prompt) | The fire surges, embers lift off the paper and **gather and hang** in the dark band across the top of the frame |
| 2. The logo | **ffmpeg** | The exact `docs/brand/logo/badcode-wordmark-reversed` fades in where the embers hang, filled with the flames' own flicker so it reads as made of fire. Then the embers drift off it |
| 3. The hold | **Premiere** | Timing to the last narration word, and the handover to (or replacement of) 12e-bc |

**Shot spec (shot-craft):**
- **Job:** what the two men burned becomes the thing that has been talking all along. The narrator signs its
  name in their fire.
- **The camera stays locked.** 33.mp4 already has a Premiere push-in, and this plate stays still so the logo
  can be laid over it exactly.
- **Space for the logo:** the dark top band above the drum rim, across the frame, where there's only rain now.
  The embers are told to go there.
- **Light:** the fire is the only source, and the gathered embers glow faintly in the dark.

**Engine decisions:**
- 🔴 **No word, letter, logo or text noun anywhere in the prompt.** Every noun gets drawn (2f-5), and the paper's
  printing is already in frame, so it isn't mentioned.
- **"A thick swirl of embers"**, because we want many. Particle nouns have no volume control, so a lot is safe here.
- **The embers hang instead of fading.** That's the one unreal thing and it's the point, said once, plainly.
- **Shutter clause** for the fast embers leaving the flames, so they streak rather than look pasted on.
- **Two beats:** the surge and lift, then the gathering and hanging.

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the **last frame of `33.mp4`**,
exported raw with no Premiere push-in (or `camera/reference/scene-12c-newspaper-burns-ACCEPTED.png`).
**No end frame.** 16:9 · 720p · x2 · 8s.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still, a single continuous shot, everything at real speed.

The fire in the drum surges up around the burning paper, and a thick swirl of glowing orange embers tears loose from it and rises fast into the dark above the rim of the drum, shot at 24fps with a 180-degree shutter so the fastest embers streak. Then, instead of fading, the embers slow and gather in the dark band across the top of the frame, hanging there in a long, loose, glowing cloud that drifts slowly from side to side, while the rain keeps falling through them and the fire below keeps burning.

Audio: the fire roaring up and crackling, a soft rush of rising sparks, and steady rain. No music and no voices.

Thanks.
```

**Check before accepting:**
- The embers end up **hanging across the top band** with dark around them, which is where the logo goes.
- No shapes, letters or symbols form by accident.
- The drum, the paper and the hand at the right edge don't redraw.
- The fire stays fire and doesn't strobe. ⚠️ Run `scripts/photosensitivity-check.py` after the composite.

### 12c-embers — round 1 ❌ (Jack, 2026-09-16: *"That didn't work"*) and round 2

⬜ **What came back isn't recorded.** Jack didn't say.

**Likely cause, by the house rules:** round 1 asked for the one thing physics doesn't do, embers that
*"instead of fading, slow and gather … hanging there"*. The engine has no footage of that to draw on, and
[small asks keep the frame, big ones refuse or rebuild it](../../google-flow/omni-flash.md#️-the-changeadherence-trade-is-a-straight-line).
There were also two motions and a shutter clause in one long sentence.

**Round 2 moves the unreal part into post.** Flow is asked only for what real fire does: a flare, and a heavy
stream of embers rising up through the dark top of the frame. **The gathering into the logo becomes the
ffmpeg layer's job**, with the wordmark lit from the ember light as the embers pass through. The prompt is
two plain sentences plus audio, with no shutter clause (it was subtracted).

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it. The view holds perfectly still.

The fire in the drum flares up around the burning paper and throws a heavy, steady stream of glowing orange embers up into the dark above the drum, rising all the way through the top of the frame for the rest of the shot while the rain keeps falling.

Audio: the fire roaring and crackling, and steady rain. No music and no voices.

Thanks.
```

### 12c-embers — round 2 ❌ (*"nothing happened"*) → route change: 12f, the logo in the coals · **still** · written 2026-09-16, unrun

**Jack, 2026-09-16:** *"nothing happened, maybe the camera goes into the barrel of lit firewood then it spells
badcode out in the coals, or sparks."* The engine note is in
[`omni-flash.md`](../../google-flow/omni-flash.md) (a fire plate on Frames came back with nothing happening).

🔑 **Same route as 12e-bc, which worked: design the logo on a still first.** Stills are where the engine spells
best, and a video clip reinvents the logo on every roll.

| Layer | Tool | What |
| --- | --- | --- |
| 1. Into the barrel | **Premiere** | Push in on `33.mp4` down into the fire (it's already 100 → 107), then dissolve through the flames into 12f. A Flow camera move is where regeneration fires (hybrid method) |
| 2. The logo in the coals | **Nano Banana 2** (this prompt) | Looking down into the bed of coals, where the glowing cracks spell the logo |
| 3. It breathes | **Omni Flash, Frames** (after the still is accepted) | The coals glow brighter and dimmer, sparks lift off the letters, and rain hisses on them. Everything asked for is already in frame 0 |

**Shot spec (shot-craft):**
- **Job:** the film signs off. What the two men burned to stay warm is where the narrator's name was all along.
- **Frame:** looking straight down into the drum. A crescent of the rusted rim at the frame edge ties it to 12c.
  Below that is black charcoal and ash with the logo glowing through it. No flames cover the letters.
- **The logo *is* the bright anchor**, and everything else is near-black. That's the "one bright region" rule.
- **Brand:** the attached wordmark is the design. Red glow at the brace's top tip and blue at its bottom tip,
  per [`docs/brand/README.md`](../../brand/README.md).

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **References, in order:** (1)
`docs/brand/logo/badcode-wordmark-reversed-2400.png` (2) `camera/reference/scene-12c-newspaper-burns-ACCEPTED.png`.
**No Characters.** 16:9 · 2 outputs.

```prompt
SCENE:

The first attached image is the logo design to reproduce exactly. The second attached image shows the burning drum this photograph looks down into, and sets its look: the rusted metal, the firelight, the rain and the film grain.

Documentary photograph looking straight down into the bottom of the rusted metal drum, close, at night. A thin crescent of the drum's rusted rim curves across one corner of the frame. Filling the rest of the frame is a bed of black charcoal, charred wood and grey ash from a fire that has burned down, with no tall flames left.

Logo: glowing through the black charcoal, as cracks of burning orange ember light running through the coals, the word from the first attached image, spelled BadCode, with the same letter shapes and spacing and with the C as a curly brace. The top tip of the brace glows deep red and the bottom tip glows bright blue, exactly as in the logo design. The letters are formed by the embers themselves, glowing hottest along their centres and fading to dull red at their edges, with thin grey ash lying over parts of them, as if the fire had burned the word into the coals.

Light: the glowing letters are the only light, lighting the nearby charcoal a soft orange and falling away to black at the edges of the frame. Raindrops fall into the drum and leave small dark wet spots and wisps of steam where they hit the embers.

Details: real charcoal texture, ash, steam, rust and fine natural grain, matching the second reference.

Constraints: The letters spell BadCode exactly, with a capital B, a lowercase a and d, the curly brace as the C, and a lowercase o, d and e. There is no other text anywhere in the frame. Compose for a 16:9 frame.

Thanks.
```

**Check before accepting:**
- It reads **BadCode**, with the brace as the C. Red tip on top, blue tip underneath.
- The letters look **burned into the coals**, not a sticker on top.
- The rim crescent and the rust match 12c.
- No flames cover the letters, and there's no other text.

### 12f — round 1 rewritten before running: **no brand brace, a coal lettering** · written 2026-09-16, unrun

**Jack, 2026-09-16:** *"Do not do it in the badcode way with the bracket, just do it in a coal font that fits
the scene."* 🔑 **So the brand wordmark reference is dropped, and the attachment is now only the 12c still.** No
brace and no red/blue. It's a deliberate break from `docs/brand/`, Jack's ruling for this shot.

**The lettering, described by shape (no font names, since the engine has no typeface control):** heavy,
chunky capitals with rough, broken, uneven edges, as if cut roughly into the charcoal. Glowing hot along their
centres and cooling to dull red at the edges. **All caps, `"BADCODE"` in quotation marks**, because short,
all-caps, high-contrast quoted text is what the engines spell best (tenth pass).

**Paste into:** Flow → **Nano Banana 2** → image prompt box. **Reference:** `camera/reference/scene-12c-newspaper-burns-ACCEPTED.png`
only. **No Characters.** 16:9 · 2 outputs.

```prompt
SCENE:

The attached image shows the burning drum this photograph looks down into, and sets its look: the rusted metal, the firelight, the rain and the film grain.

Documentary photograph looking straight down into the bottom of the rusted metal drum, close, at night. A thin crescent of the drum's rusted rim curves across one corner of the frame. Filling the rest of the frame is a bed of black charcoal, charred wood and grey ash from a fire that has burned down, with no tall flames left.

Lettering: across the middle of the coals, the word "BADCODE" glows through the black charcoal as burning embers. The letters are heavy, chunky capitals with rough, broken, uneven edges, as if cut roughly into the charcoal, each one glowing bright orange-yellow along its centre and cooling to dull red at its edges, with thin grey ash lying over parts of them, as if the fire had burned the word into the coals.

Light: the glowing letters are the only light, lighting the nearby charcoal a soft orange and falling away to black at the edges of the frame. Raindrops fall into the drum and leave small dark wet spots and wisps of steam where they hit the embers.

Details: real charcoal texture, ash, steam, rust and fine natural grain, matching the reference.

Constraints: The word reads BADCODE exactly, seven capital letters, B A D C O D E. There is no other text anywhere in the frame. Compose for a 16:9 frame.

Thanks.
```

**Check before accepting:** it spells BADCODE exactly, the letters look burned into the coals rather than laid on
top, the rim and rust match 12c, and there's no other text.

### 12f — ✅ still ACCEPTED 2026-09-16, and its clip · **video** · written 2026-09-16, unrun

**The still:** BADCODE in chunky charred capitals glowing orange from inside, laid into a bed of charcoal in the
drum, with a rusted rim at the top left and rain and steam at the right. It spells correctly. A reference copy
from Jack's screenshot is at [`camera/reference/12f-badcode-coals-ACCEPTED-screenshot.png`](./camera/reference/12f-badcode-coals-ACCEPTED-screenshot.png).

**Shot spec (shot-craft):**
- **Job:** the last signature. The word breathes like a real fire, and one gust gives it a final flare.
- **The camera is locked.** The push *into* the drum is Premiere's, on `33.mp4` into a dissolve.
- **Two beats:** living embers, rain hissing and steam, then a breath of air makes the letters flare brighter
  and throw up a few sparks before they settle.

**Engine decisions:**
- 🔴 **The word isn't written again and the letters aren't described.** Text already in frame 0 is locked by one
  sentence and never re-spelled (tenth pass). *"Text rarely survives motion intact"*, so the letters themselves
  don't move.
- **No *"the view holds perfectly still"* this time.** On 12c-embers it froze the fire ([omni-flash note](../../google-flow/omni-flash.md)).
  The prompt leads with the continuing motion and pins the camera in a clause.
- **The glow flickers gently, not in a pulse.** Pulsing light makes fine texture boil (tenth pass). The flare is
  one event with a cause (a breath of air), and then it settles.
- **"A few sparks"**, because particle nouns overdeliver.

**Paste into:** Flow → **Omni Flash** → **Frames** → prompt box. **First frame:** the accepted 12f still. **No end
frame.** 16:9 · 720p · x2 · 8s.

```prompt
The attached image is the first frame of this shot, and the clip continues directly from it as one continuous shot, with the view fixed in place and everything moving at real speed. The glowing letters in the coals keep their exact shape, spacing and spelling for the whole clip.

The embers glow and flicker gently and irregularly along the letters, raindrops land on the hot coals with small puffs of steam, and thin wisps of steam and smoke drift up through the frame. Halfway through, a breath of air moves across the drum and the letters glow brighter for a moment, sending a few small sparks lifting off them and drifting up out of the frame, then the glow settles back.

Audio: rain pattering into the drum and hissing on the hot coals, a soft crackle of embers, and a low rush of air as the glow brightens. No music and no voices.

Thanks.
```

**Check before accepting:** the letters stay spelled BADCODE and don't reshape, the charcoal texture doesn't crawl
when the glow brightens, there are sparks but no flames covering the word, and nothing strobes. ⚠️ Run
`scripts/photosensitivity-check.py`.
