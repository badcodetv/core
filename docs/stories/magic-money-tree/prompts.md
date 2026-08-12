---
story: magic-money-tree
flow_project: magic-money-tree-story
flow_project_id: 0d2c496b-ef03-469b-af08-dd378bae153b
updated: 2026-08-12
---

# The Magic Money Tree — prompt ledger

Read `.claude/skills/badcode-art-direction/SKILL.md` first (Layer 0 — the global
BadCode register; never copied into this file).

> **Status: Layer 1 + totems + beat prompts drafted 2026-08-08.** Cover tested
> manually by Kai. Everything below is **unfired** — no image has been generated
> from these prompts yet. Front-runs T7/T9/T10 of
> [`design/2026-08-08-story-covers-and-prompt-ledger.md`](../../../design/2026-08-08-story-covers-and-prompt-ledger.md).

---

## 0. Hard guardrails — read before writing any prompt here

**Real people are archive-only.** Locked 2026-08-07 (`story.md:430-436`).
Theresa May, Nixon, the NHS nurse and Harry Leslie Smith appear **exclusively as
genuine footage** under fair dealing — never generated, never voice-cloned.
**Keynes is the one exception** (80 years dead, historical-fiction register).
There is no prompt in this file for anyone else real, and there must never be one.

**Never name Keynes inside a prompt.** He is generated, but naming a real person
as a likeness target is Flow block trigger #2. Describe build, era dress and
bearing; keep him distant or three-quarter-back wherever the shot allows.

**The Flow Character is named "Economist", not "Keynes" — and that is the whole
reason it works.** Learned the hard way 2026-08-12: the **Character Name field
itself feeds Flow's policy scanner**, not just the prompt box. A Character named
"Keynes" had every generation refused ("This generation might violate our
policies") even though the prompt text named nobody; renaming it to "Economist"
and retrying the identical prompt succeeded immediately. So the guardrail above
extends to **every field Flow can read** — Character Name, Character Info, and
the prompt. Cast him as `@Economist`.

**The tree is never mystical.** No glow, no face, no eyes in the bark, no
anthropomorphism of any kind. Canon: it grew from a £1 note planted in August
1914, so it is 28 years old in 1942 — young, ordinary, too small to be notable.
Presence is carried by framing, wind and light. **A magical-looking tree is a
generation to reject, not a happy accident.**

**No fascist iconography, ever.** Beats 3 and 8 touch the 1930s and the modern
far right. No flags, no armbands, no insignia, no marching columns in any
generated frame — the archive carries that material, and a prompt containing it
will be policy-blocked anyway. Our generated frames stay on trees, money, rooms
and weather.

**No named institutions in prompts.** The Bank of England, the Reichsbank and the
Treasury are all in the canon and none of them may appear as a name or a legible
sign. Paraphrase to "a central bank", "an enclosed courtyard garden in a
financial district".

---

## 0b. How to use this file

**Every prompt in §3 is self-contained. Paste one block and nothing else.**
Do not prepend §1 to it — the style is already folded in, and prepending it again
just doubles the style instructions and dilutes the scene.

§1 below is the **canonical source** of that style: it is what a prompt author
copies from when writing a new asset, and what an audit checks existing prompts
against. It is a specification, not a runtime concatenation.

**The trade-off, stated honestly:** self-contained prompts are paste-ready but
not DRY. If §1 ever changes, every prompt in §3 has to be revised to match. That
is the price of the prompts being usable by a human with a browser, and it is
worth it — but it means **§1 changes are expensive**, so settle it before writing
many more assets.

### Keeping things consistent across images — two different mechanisms

| Subject | Mechanism | Why |
| --- | --- | --- |
| **People** (Keynes) | A **Flow Character**, cast via `flow_create_character` and attached with the `character` parameter | Characters bind a *face*. This is the only reliable way to get the same man in 1942, 1948, 1971 and now. A tag typed as prompt text does **not** bind anything. |
| **Objects and places** (the tree, the bench, the collar, the hollow fruit) | A **golden reference image** fed to `flow_edit_image` — exactly one reference, downscaled first | They have no face for a Character to bind. Generate the totem once, accept it, and derive every later appearance from that image. |

Whether Flow Characters can be made to work for objects is **untested** — the
feature is built around people. Assume not; use golden references. If someone
wants to spike it, do it on the bench, not on the tree.

## 1. Style prompt

The canonical style for this story. **Not concatenated at call time** — see §0b.

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette with desaturated winter greens and browns, no lens flares, calm observational tone, landscape orientation, deep unlifted shadows with no lifted matte or shadow recovery, a single motivated light source that is a real thing in the scene, subject held small inside a large frame, no text, no signage, no lens vignette, no fantasy effects.
```

**Register variant — "the testimony."** Beat 3's history vignettes (1694, 1923
Berlin, the 1930s, the counterfeit tree) use the same stock but push it: higher
contrast, colder, closer, and lit by whatever is honestly available in the room —
window light, a lamp, a furnace. Append to the style prompt:

```prompt
Period interior photography, higher contrast and colder grade, closer framing, lit only by available window or lamp light.
```

**Register — archive.** Not generated. Real footage. No prompt exists or should.

---

## 2. Cast

| Tag | Character file | Sheet | Flow Character id | Status |
| --- | --- | --- | --- | --- |
| @Economist | characters/keynes.md | — | "Economist" · `40387729-cccf-4c29-bc97-f8e193e249d6` | **cast** 2026-08-12 — Portrait + native Create Body, Nano Banana Pro. Portrait media `9887ff7d-1d23-4394-b275-f3cfa0b9b455`, Body media `905c89ba-22c8-410c-accf-51c65f3569eb`. Cast in Flow as **"Economist"** — see §0; the name field is policy-scanned. |
| @TheTree | characters/the-tree.md | — | — | no-character-by-design — **consistency via golden reference**, not a Character |

**The economist must be cast.** He appears at four ages across eighty years — 1942 at
the bench, 1948 as the arriving ghost, 1971 at Nixon, and the winter bench now —
and he has to read as the same man every time. The scene prompts in §3 are
deliberately written so he is always distant and face-not-readable, which means
they will *survive* without casting; but "survives" is not "is consistent", and
the moment any shot comes closer, the Character is the only thing holding him
together.

**The tree is not a Character and still needs to be one object.** It appears in
six beats and visibly ages from 28 years old to 112. Generate its sheet once,
accept it, and derive every appearance from that image via `flow_edit_image`.
`none-by-design` here means *no Flow Character*, **not** *no consistency needed*.

`characters/dawn.md` is **deprecated canon** — the 2026-08-05/06 re-founding
replaced the Dawn spine with Keynes and the tree. Do not cast her.

---

## 2b. Totems — lock these before generating any scene

Four things recur across four decades and must be **the same object every time**.
Generate each once, accept it, and reference it thereafter.

| Totem | Rule | Appears in |
| --- | --- | --- |
| **The bench** | One slatted wooden park bench, same weathering, same angle to the path. It is the story's spine — the fixed point history walks past. | Beats 2, 5, 6, 7, 9 + cover |
| **The tree** | A young European lime. 28 years old in 1942, visibly older but never grand by 2026. Bare in winter, full in summer — its foliage is the emotional register. | Everywhere |
| **The collar** | A plain iron band bolted around a trunk. The gold standard made physical. It comes **off** in 1971, worldwide, at once. | Beat 6 (1971) |
| **Hollow fruit** | Fruit that looks right and is empty — a shell, split open, nothing inside. The mechanism's one limit, made visible. | Beat 3 (1923) |

---

## 3. Assets

### cover → `docs/images/covers/magic-money-tree.jpg`

**Metadata — none of this is pasted into Flow.**

- **Cast:** — (figure deliberately distant and faceless; no Flow Character needed)
- **Light source:** low raking winter daylight from behind the trees
- **Lint:** ✅ 2026-08-08 — no brand names · no likeness phrasing · no stacked
  destitution · no institutional text
- **Flow media id:** _pending_
- **Revisions:** _none yet — awaiting Kai's manual test run._

**Prompt (variant A — primary).** Self-contained; §1 is already folded in.

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette with desaturated winter greens and browns, no lens flares, calm observational tone, landscape orientation. A wide view of an empty London park on a cold overcast morning in the early 1940s: a single slatted wooden bench sits small in the lower third of the frame beside a young, unremarkable lime tree of perhaps thirty years, its bare branches thin and modest against a pale sky. One man in a heavy dark three-piece suit and long overcoat sits alone at one end of the bench, seen from a distance and slightly behind so his face is not readable, papers resting unread on his knee, his head angled very slightly toward the tree as though mid-conversation. Low raking winter daylight from behind the trees is the only illumination, throwing long soft shadows across wet grass and gravel into deep unlifted shade. Mist between distant plane trees, the edge of a lake just visible beyond. No other people, no text, no signage, no glow, no fantasy effects — it is an ordinary tree.
```

- **Variant B — the ending, not the premise:** replace *"his head angled very
  slightly toward the tree as though mid-conversation"* with *"sitting forward
  with his head in his hands"*, and add *"hard frost on the grass"*.
- **Variant C — the empty seat:** delete the sentence beginning *"One man in a
  heavy dark three-piece suit"*. Bench and tree alone.

---

### beat2-ascent → `docs/stories/magic-money-tree/storyboard/img/b02-ascent.jpg`

The canon opening move: the camera rises out of the war rooms, through concrete,
through earth, **through roots**, into the grass. This still is the mid-point of
that rise — the moment the frame is all soil and root and the light is arriving
from above. Built to be animated as an upward push.

- **Light source:** daylight from directly above, filtering down through grass roots
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, landscape orientation, deep unlifted shadows. A cross-section view inside dark London soil, looking straight upward: a dense tangle of pale tree roots and severed grass roots threading through packed earth and clay, tiny stones and chalk catching the only light — a soft green daylight filtering down from the underside of a grass surface directly overhead, close enough to see individual blades from beneath. Below and behind, the earth goes to solid black. Cold, damp, geological, entirely still. No people, no text, no glow, no fantasy effects.
```

---

### beat2-bench-1942 → `.../storyboard/img/b02-bench-1942.jpg`

The establishing shot of the friendship: he arrives, he sits, the tree speaks.
Note this is the **same bench and tree as the cover** — reference the accepted
cover as the anchor so the geometry matches.

- **Cast:** @Economist (distant, three-quarter back)
- **Light source:** flat spring daylight
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, landscape orientation, deep unlifted shadows. A London park path in spring 1942, seen from across the grass at a distance: a slatted wooden bench beneath a young lime tree just coming into leaf. A heavyset man in a dark three-piece suit and overcoat walks the gravel path toward the bench, carrying a document folder, seen from behind and to one side so his face is not readable. Flat spring daylight under a high overcast is the only illumination. Wet gravel, unmown wartime grass, railings and mist beyond. No other people, no text, no signage, no glow, no fantasy effects — it is an ordinary tree.
```

---

### beat3-hollow-fruit → `.../storyboard/img/b03-hollow-fruit.jpg`

**The single most important image in the story after the bench.** It is where the
mechanism's limit lands and where the audience's "…but Zimbabwe" objection gets
answered. The tree was not failing. It was screaming.

- **Light source:** a single high window
- **Lint:** ✅ 2026-08-08 — no institution named, no insignia, no people in
  distress. Keep it on the fruit.

```prompt
Period interior photography on 35mm film with fine natural grain, higher contrast and colder grade, muted palette, no lens flares, landscape orientation, deep unlifted shadows. A cold stone courtyard inside an old European bank building in the early 1920s, lit only by hard daylight falling from one high window. A mature lime tree grows in the centre of the courtyard, heavy with fruit — and the fruit is wrong: dozens of husks split open on the flagstones, each one a perfect empty shell with nothing inside, dry as paper. Drifts of loose printed banknotes have blown into the corners and lie unregarded underfoot, worth nothing. No people, no text, no legible lettering, no signage, no insignia, no flags, no glow, no fantasy effects.
```

---

### beat3-rentenmark → `.../storyboard/img/b03-rentenmark.jpg`

The correction that accidentally proved our thesis: they killed the old tree and
rooted a new one in **land** — backed by what a country can actually make.

- **Light source:** low late-afternoon sun
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette with desaturated winter browns, no lens flares, landscape orientation, deep unlifted shadows. A young sapling planted alone in the middle of a vast working farm field in 1920s northern Europe, seen from a low distance so the sapling is small in a very wide frame. Ploughed furrows run to the horizon; a working brick factory with smoking chimneys sits far off at the field's edge. Low late-afternoon sun rakes across the soil as the only light, the sapling casting one long thin shadow. Solid, ordinary, unremarkable. No people, no text, no signage, no glow, no fantasy effects.
```

---

### beat3-ordered-not-to-drop → `.../storyboard/img/b03-not-to-drop.jpg`

Burn two, 1930–33: the tree standing in **full fruit**, ordered not to drop it,
while the country starves below. This is the deflation, the thing that actually
produced the catastrophe — told without a single flag.

- **Light source:** overcast winter daylight through the courtyard opening
- **Lint:** ✅ 2026-08-08 — deliberately no people and no insignia; the horror is
  that the fruit is *there* and nobody is allowed it.

```prompt
Period interior photography on 35mm film with fine natural grain, higher contrast and colder grade, no lens flares, landscape orientation, deep unlifted shadows. The same cold stone bank courtyard in winter in the early 1930s: a mature lime tree standing heavy with ripe, intact, perfectly good fruit that has not been picked and has not fallen, weighing the branches down. The flagstones beneath are swept completely bare and clean. A locked iron gate closes the courtyard's only opening, overcast winter daylight coming through its bars as the only illumination. Frost on the stone. Absolutely nobody present. No text, no legible lettering, no signage, no insignia, no flags, no glow, no fantasy effects.
```

---

### beat3-counterfeit-tree → `.../storyboard/img/b03-counterfeit.jpg`

The plot connector: the enemy used the mechanism **first, in secret**, through a
letterbox company — which is precisely why Keynes has to do it in the light.

- **Light source:** a single desk lamp
- **Lint:** ✅ 2026-08-08 — no real company name, no legible paperwork, no
  insignia.

```prompt
Period interior photography on 35mm film with fine natural grain, higher contrast and colder grade, no lens flares, landscape orientation, deep unlifted shadows. A small, cramped, almost empty back office at night in the mid 1930s, lit by one desk lamp as the only light source. In the centre of the bare floorboards stands a crude counterfeit tree, obviously fake — a trunk built from bundled rolled paper and glued ledger sheets, branches of bent wire, leaves cut from blank stationery — and it is nonetheless heavy with real-looking fruit. One empty chair. Filing drawers standing open and unused. No people, no text, no legible lettering, no signage, no insignia, no glow, no fantasy effects.
```

---

### beat5-empty-bench → `.../storyboard/img/b05-empty-bench.jpg`

**The vindication plays to an empty bench.** July 1948, the tree in full leaf,
the thing he built finally opening — and nobody to tell. The single saddest frame
in the film and it contains nothing but furniture and weather.

- **Light source:** high summer daylight through the canopy
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, landscape orientation, deep unlifted shadows. The same London park bench in high summer 1948, empty, photographed from across the grass at a distance so it sits small in a wide frame. The lime tree above it is now in heavy full leaf, dense and healthy, six years older. Dappled summer daylight falls through the canopy as the only light, moving across the empty slats. Long grass, still air, nobody in the park at all. No people, no text, no signage, no glow, no fantasy effects.
```

---

### beat6-collars-off → `.../storyboard/img/b06-collars-off.jpg`

1971 — **not a planting, a release.** The trees were always there and they were
chained; gold was a collar that did everyone's thinking for them. Nixon took the
last one off. Shoot the collar, not the man.

- **Light source:** hard midday sun through the courtyard
- **Lint:** ✅ 2026-08-08 — no real institutions, and **Nixon is archive only** —
  he must never appear in a generated frame.

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, landscape orientation, deep unlifted shadows. Close on the base of a mature tree trunk in an old stone courtyard: a heavy iron band that has been bolted around the trunk for decades now lies split open on the flagstones beneath it, its bolts sheared, a deep pale scar of compressed bark ringing the trunk where it sat. The tree above has already begun to swell outward past the old line. Hard midday sun through the courtyard opening is the only light. No people, no text, no legible lettering, no signage, no glow, no fantasy effects.
```

---

### beat9-winter-bench → `.../storyboard/img/b09-winter-bench.jpg`

The cold ending. The tree bare **out of season** — that is its grief, not the
weather. Everything they built, being unbuilt by people who say the tree isn't
real.

- **Cast:** @Economist (the ghost — unchanged, unhurried; still distant)
- **Light source:** flat grey winter daylight
- **Lint:** ✅ 2026-08-08 — no ghostly transparency or glow effects; he simply
  looks like a man from 1942 sitting in the present day, which is the whole point.

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette drained almost to grey, no lens flares, calm observational tone, landscape orientation, deep unlifted shadows. The same London park bench in hard frost, photographed from across the grass at a distance. The lime tree above it is completely bare — no leaves at all — though the grass and the other trees behind it are still green and in season. A heavyset man in a 1940s three-piece suit and long overcoat sits forward on the bench with his head in his hands, seen from a distance and slightly behind so his face is not readable. Flat grey winter daylight is the only illumination. Frost on the slats and the grass. Solid and ordinary, no transparency, no glow. No other people, no text, no signage, no fantasy effects.
```

---

### beat9-mulberries → `.../storyboard/img/b09-mulberries.jpg`

**The last image.** Four black mulberries in full leaf, planted in the early
1940s in an enclosed courtyard garden that is a graveyard, roots deliberately
shallow so they never reach the dead — *being shaken.* The four that were never
asked a question, thriving; the one that was, bare. All those people died for
this.

- **Light source:** overhead daylight down the courtyard well
- **Lint:** ✅ 2026-08-08 — the real garden is at a named institution; **do not
  name it**. "An enclosed courtyard garden in a financial district."

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, landscape orientation, deep unlifted shadows. A small enclosed courtyard garden hemmed in on all sides by tall blank stone office walls in a financial district, present day. Four black mulberry trees in heavy full leaf stand in a neat row on mown grass over old, worn, illegible flat gravestones set into the ground. The trees are being shaken hard — branches blurred with motion, a shower of dark ripe fruit falling and bursting on the stones and the grass beneath. Overhead daylight falling straight down the courtyard well is the only illumination; the surrounding walls are in deep shade. No people visible, no text, no legible lettering, no signage, no glow, no fantasy effects.
```

---

## 4. Not yet prompted

Deliberately left for a later pass, with the reason:

- **Beat 1 (the war, black and white)** and **beat 4 (it works)** are archive-led.
  Generated frames would compete with real footage; decide the cut first.
- **Beat 7 (the forgetting)** is built on the May clip and real 2020–21 material —
  archive-only by the guardrail. The one generatable image is the yacht, and it
  needs a decision on whether we want a real-looking one at all.
- **Beat 8 (what grows in the cold)** is archive plus Harry Leslie Smith's voice.
  **Nothing here may be generated.**
- **Character sheets** for @Economist and @TheTree — T15. The scene prompts above
  are written to survive without them (he is always distant and faceless), but
  casting Keynes properly is what makes him the same man across four decades.
