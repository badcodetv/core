# Camping — where the year lives

> **What this is:** the design for a single, consistent on-screen year across the film, written
> 2026-08-30 in answer to Jack's ask — *"a consistent place where we show what year it is."*
> Craft research behind it: [`../../cinematography/on-screen-time.md`](../../cinematography/on-screen-time.md).
> **Nothing here is executed.** Canon wins over anything on this page until Jack rules.

## 🔑 The finding that changes the question

**Camping already has a year device, and it is a good one.** Canon has held it since 2026-08-24:

- `1a` — the City skyline, NatWest Tower dominant, **a huge "2008"**, *"the sky above the hero
  tower is completely empty."* The empty sky is not an accident; it is a slot.
- `4a` — **the same plate, edited.** The Shard replaces the tower, the number reads **"2026"**.
  Canon: *"the swap **is** the timestamp"* — an edit, not a second generation, because two
  independent skylines will not match.
- `style.md` calls this **the matched city pair** and lists it first under *motifs to hold*.

So the film's clock is **family 4 — the graphic match** (same frame, twice, something changed)
with **family 2 — a fixed slot** riding on top of it. That is the strongest combination
available and it is already half-built.

## 🔴 The problem is the third year, not the first two

**2031 is carried by the newspaper**, in a field, at night, in a man's hand. Different
mechanism, different place, different size — at the exact moment the film's biggest reveal
lands. Two legs of a three-legged device.

⚠️ **This is not an argument for stripping the newspaper.** Canon's *one prop, two jobs* is
right and the date must land in Bob's hand. The question is only whether the film's **clock**
speaks a third time, and where.

---

## ✅ Ruled by Jack, 2026-08-30 — 2031 goes to the narration

**The third date is spoken, not shown.** Bob's *"look at the date"* and the narration carry
2031; **the newspaper stops being a clock and goes back to being a prop.** It still does its
other job — the headline — and Tarquin still reads it.

**So the on-screen year is a two-instance device**, and both instances are the City:
**2008 (`1a`)** and **2026 (`4a`)**. Same framing, same slot, one number changing. That is a
cleaner device than three legs and it costs no new scene.

⬜ **Open:** whether the scene-11 City return still happens *without* a number on it — a dark
Shard doing the reach-back to scene 4 on pictures alone. Cheaper than it was, and no longer
load-bearing for the clock.

---

## 🔴 Ruled 2026-08-30, after the cloud break was run and failed: **the year goes to the foreshore**

The cloud-break prompt was run against the accepted `1a` master and **came back inverted** — four
dark soot-coloured blobs sitting *on* the grey lid instead of four holes torn *through* it. Full
diagnosis in the ledger:
[`prompts.md` — 1a-year round 1](./prompts.md#1a-year--round-1-not-accepted-the-model-inverted-the-device-and-the-physics-were-against-it).
Two causes, and **only the first is a phrasing problem**:

1. 🔑 **"Torn out of" is a subtractive instruction and the model has no picture of one.** It has a
   picture of *smoke writing*, so it substituted that — the exact register this file rejected.
   **Generalisable rule: ask for a dark object on a pale ground, never a pale gap in a dark
   field.** Additive renders; subtractive inverts.
2. 🔴 **Overcast has no contrast to give.** A hole in a grey lid shows *grey sky*. To make the
   digits read the model needed separation, and the prompt had banned brightening them, so it
   darkened them instead. **The device asked for legibility and forbade the means.** No round 2
   fixes that.

And it **re-rolled the skyline** while it was there — the lattice tower crossed the frame, the
hero tower lost its chevrons. A sky rewrite that also moves the buildings cannot found a matched
pair.

### ✅ So: the seaweed idea is promoted from tier 2 to the device

Tier 2's objection was **true but narrow** — *the river is a thin band at `1a`'s altitude*. That
is an argument against putting it in **that frame**, not against the idea. It gets its own frame:
a low-oblique foreshore insert at 2008 and the identical one at 2026, `1y` and `4y`, written up in
[`prompts.md`](./prompts.md#1y--the-year-on-the-foreshore-2008--still--written-2026-08-30-unrun).

**Why it wins on all four grading criteria this file set:**

- **Legible** — near-black wet weed on pale reflective mud. The mud holds the flat sky and works
  as the bright anchor, so everything laid on it reads black. The opposite of the sky problem.
- **Survives animation** — the weed does not move at all. Water creeps at the far edge, one gull.
- **Gate 2 is built in** — the cost *is* the tide line: in `4y` the same digits are silted and the
  plastic is threaded through them.
- **Slop-resistant** — ragged organic glyphs are what a viewer expects from weed, so the model's
  imprecision stops being a tell instead of being one.

**Two things it buys that the cloud version could not:**

- 🔒 **`1a` and `4a` are never regenerated.** The film's most important restore point stops being
  at risk from the clock.
- 🔑 **One frame carries the graphic match *and* the number.** The foreshore is the part of London
  that looks the same in both years, so the pair matches by construction — the only differences
  are the small hazy skyline over the wall and what the tide has done. **The skyline pair says the
  city changed; the foreshore pair says the river did not, and it kept the receipt.**

⚠️ **Cost:** two stills and two clips, and it adds cuts to a film that
[`edit-plan.md`](./edit-plan.md) says is already 122s over on picture. Each insert is ~1.5–2s and
should come **out of** the establisher's runtime, not on top of it.

---

## The menu — ways the year can live in the City frame

**The constraint that kills most ideas:** `1a` is a **high aerial, long view** — the hero tower
fills the middle third, the city is small, and the river is a thin band across the lower third.
**Anything below rooftop height will be too small to read.** That is the whole verdict on the
seaweed idea, and on most of the good ones.

Graded on four things: **legible at this distance · survives being animated · passes gate 2 (a
visible cost in frame) · does not read as AI slop.**

### 🥇 Tier 1 — works at this distance

- **A break in the cloud, shaped like the year.** An overcast lid over the city with the digits
  cut clean out of it. **Not glowing, not written — an absence.** The narrator warping the sky
  over a city it is about to describe, which is exactly what a superintelligence narrating from
  the future would do. ✅ Big · ✅ clouds are *supposed* to move, so animation drift becomes
  motivated behaviour rather than a defect · ✅ soft organic form is the opposite of the
  crisp-synthetic slop tell. **Cost comes from the skyline below, not the device.**
- **The year written in the lit windows of the hero tower.** Office lights left on at night
  spell it out. ✅ **Gate 2 is built into the device** — 2008 and 2026 fully lit, and if the
  scene-11 return happens the tower is dark and the number is gone. 🔑 It is the same argument
  as scene 4's empty flats: *the lights were always on in buildings nobody lives in.*
  ⚠️ Highest slop risk on the list — a window grid is a repeating texture and small digits are
  gibberish-text bait, the two most-cited tells. Would need to be large and to be checked hard.
- **Scaffold netting on a tower carrying the year.** Corporate hoarding wrap, the way London
  actually looks. ✅ **Historically anchored** — the August 2008 reference photograph has
  Broadgate Tower in scaffold and cranes ([`camera/reference/README.md`](./camera/reference/README.md)).
  ✅ Decays beautifully across instances: crisp banner → rewrapped → shredded. ⚠️ Printed
  lettering is the format most likely to come back malformed.
- **A tower crane's jib, the year on the counterweight.** Same historical anchor, same decay
  (2031: the crane still there, rusted, nothing built). ⚠️ Small at this distance.

### 🥈 Tier 2 — needs a different, closer framing

Each breaks the matched-pair rule, which is the device's whole engine. **Only worth it if the
year gets its own insert shot rather than riding the establisher.**

- **Seaweed and algae on the Thames foreshore at low tide** *(Jack's idea)* — genuinely good and
  genuinely slop-resistant: irregular organic glyphs are what a viewer *expects* from weed, so
  the model's imprecision stops being a tell. 🔴 **But at `1a`'s altitude the river is a thin
  band and it will not read.** Wants a low riverside frame of its own. ✅ **It got one — ruled
  2026-08-30, this is now the device.** See above.
- **Barges and lighters moored in the shape of the digits.** Same problem, same fix.
- **The year in the tide line / reflected in the water** — upright in 2008, broken in 2031.
- **A share-price board or ticker on a building face**, the year in falling red figures. Dead-on
  for what this film is about. ⚠️ Legible screen text in *video* is the single most reliable
  slop tell there is, and it is a post job by our own standing ruling.

### 🚫 Rejected

| Idea | Why |
| --- | --- |
| **Skywriting / contrail** | Whimsical. Wrong register, and it puts an author in the sky where we want a narrator |
| **Drone swarm** | Anachronistic in 2008 — the device has to work in both years or it is not a device |
| **Constellation / stars** | Our city shots are daylight and dusk |
| **The year as the gap in the skyline** | Too abstract to read as a number |
| **Anything glowing, luminous or lens-flared** | See the slop rules below |

---

## 🔴 Avoiding the AI-slop read

The 2026 field consensus on what gives generated video away, and what each one means for this
shot. Sources at the foot of the file.

| The tell | The rule here |
| --- | --- |
| **Gibberish in-scene text** — the most-cited tell of all | 🔑 **Numbers in isolation are the best case**: a large, isolated numeral renders far more reliably than a phrase. Four digits, huge, nothing else legible anywhere in the frame. And **check every generation at 100%** |
| **Text that will not hold still in video** | 🔴 Our own standing ruling: **lettering is a post job.** If the number must be pixel-stable, it is `drawtext`, not Flow. **A cloud gap is exempt** — clouds are meant to move |
| **Flat, too-even, uncanny lighting** | Name one source and claim the falloff. `1a` already does: *sun low and hard from the left, long shadows east.* Keep it |
| **Over-saturated synthetic palette** | Muted, cool, unforgiving — camping's `style.md` already bans warmth outside three named places |
| **Plastic sheen, no grain, no noise** | Ask for the film stock and the imperfection **by name**: fine 35mm grain, atmospheric haze, uneven exposure. Bare "photorealistic" gets you plastic |
| **Unnaturally smooth, floaty motion** | Lock the camera. Move only what physically moves — cloud, haze, one aircraft |
| **Repeating texture tiling** | The risk in the window-grid option specifically. Break it with a named irregularity |
| **Applied-feeling lens flares** | 🚫 Never ask for one. `1a` gets its highlight from one band of windows catching the sun — motivated, not decorative |
| **Perfect symmetry** | The digits are cut out of weather. Weather is not symmetrical |

---

## How to run it in Flow — Omni Flash, and which tab

**Google's own guidance for both video tabs:** the text prompt must **complement, not contradict**
the visual inputs; it must **reference** the frames or ingredients supplied; keep it **direct,
not stuffed**; plain English, no keywords, no weighting, no negative prompts. For **Frames to
Video** specifically: *describe the action or transition between the frames.* For **Ingredients**:
give references on plain backgrounds, keep a consistent look across them, and **state the role
each reference plays**.

**Our routing rule** ([`../../google-flow/omni-flash.md`](../../google-flow/omni-flash.md),
confirmed 2026-08-16):

| What must survive | Tab |
| --- | --- |
| **The composition** — an accepted plate, a geometry, a camera position | **Frames** |
| Only a person's identity | **Ingredients** |

**Here the composition is everything**, so: **Frames**, with the accepted still as the start
frame, end slot empty (Omni Flash errors on an end frame), camera locked, 10s available.

⚠️ **The two tabs are mutually exclusive in Flow's UI.** No characters are needed in this shot,
so that costs us nothing.

🔴 **Do not attach the Wikimedia reference photographs as ingredients.** Three of the four are
**CC BY-SA** — if their pixels survive into the frame the licence has a claim on the film.
Ruled in [`camera/reference/README.md`](./camera/reference/README.md). **The ingredient is our
own accepted `1a` master, which lives in Flow, not in this repo.**

### Step 1 — the still (do this one first, alone)

Nano Banana, with the **accepted `1a` master attached as the reference image**. It is a **new
prompt, not an edit** — the whole scene is restated and the sky clause is the only thing that
has changed. The full paste-ready prompt is in
[`prompts.md`](./prompts.md#1a-year--the-2008-skyline-with-the-year-in-the-cloud--still--written-2026-08-30-unrun).

⚠️ **`1a` is the film's most important restore point.** This generates a **variant**; the
accepted `1a` is not overwritten and not deleted. If the variant does not match, the fallback is
a `drawtext` overlay on the existing frame and nothing is lost.

### Step 2 — the clip

Only once the still is accepted. Omni Flash, **Frames**, the accepted still as start frame,
locked camera, motion budget spent on **cloud drift only**.

### Step 3 — `4a`

Same prompt, the Shard swapped for the hero tower, the modern cluster restored, **the digits
2026 in the identical position**. Written only after the 2008 still is accepted, so the two
match by construction.

---

## What is owed a human ruling

- [x] ~~Three legs or two?~~ **Ruled 2026-08-30: two. 2031 goes to the narration.**
- [x] ~~🔴 **Which device** — cloud break, lit windows, or scaffold netting.~~ **Ruled
      2026-08-30 after the cloud break was run and inverted: neither. The year moves off the
      establisher entirely and onto a Thames foreshore insert pair** (`1y` / `4y`). See above.
- [ ] **Does the scene-11 City return still happen**, without a number, for the scene-4 reach-back?
- [ ] **Does `4a` still exist?** [`edit-plan.md`](./edit-plan.md): *`4a` is not on the timeline.*
- [x] ~~**Is regenerating `1a` acceptable at all**~~ **Moot — the foreshore route never touches
      `1a` or `4a`.** The remaining fallback if `1y` will not render clean weed digits is an
      ffmpeg `drawtext` overlay on the foreshore plate, which is a far softer landing than
      overlaying the establisher.

## Sources

- [Create videos in Flow — Ingredients to Video and Frames to Video](https://support.google.com/flow/answer/16353334?hl=en) · [Google's 5 tips for Flow](https://blog.google/innovation-and-ai/products/flow-video-tips/) · [Flow models & supported features](https://support.google.com/labs/answer/16352836?hl=en)
- [AI slop: 12 tells that a video was made by AI](https://www.opus.pro/blog/ai-slop-aesthetic-12-tells) · [How to tell if a video is AI-generated](https://www.veed.io/learn/how-to-tell-if-video-is-ai-generated) · [10 visual signs an image was made by AI (2026)](https://imagera.ai/blog/is-this-ai-generated-how-to-tell-2026) · [5 telltale signs a photo is AI-generated](https://insight.kellogg.northwestern.edu/article/ai-photos-identification)
- [Nano Banana Pro text rendering — isolated numerals are the reliable case](https://blog.picassoia.com/how-nano-banana-pro-handles-text-in-images) · [Nano Banana Pro text accuracy review](https://bluefx.net/blog/nano-banana-pro-review-95-percent-accurate-text/) · [Improving Nano Banana text-rendering accuracy](https://help.apiyi.com/en/nano-banana-text-rendering-consistency-guide-en.html)
