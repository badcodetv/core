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
> A-road. Worth settling before the scene-3 verge shots have to match it.

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
