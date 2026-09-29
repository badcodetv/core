# Logo concept sheets — the Flow experiment

> **What this is.** One generated "concept sheet" per logo idea, made in Google Flow (Nano Banana 2,
> zero credits), so the ideas in [`direction.md`](./direction.md) and the research briefs can be
> looked at as pictures of a brand in use, not as descriptions. **These are pictures of logos, not
> logos** — the image model cannot produce the final vector file; the design session does that.
> The point is to *feel* each direction fast, then lean into the ones that work.
>
> **Words here, pictures there.** Exact prompts live in this file (the repo). The generated images
> live in the media scratch folder `/mnt/d/badcode-videos/brand/clips/logo-concepts/` — per the
> 2026-08-26/27 rulings, media out there, words in here. Winners get copied into
> [`sketches/`](./sketches/) downscaled, with a note of which prompt made them.

## The shared board format

Every sheet uses the same preamble so the ideas can be compared like for like. Nano Banana reads
prose, so it is written as a brief, not a tag list. Small text is asked for nowhere, because
Flow's 1K output blurs small type; the only words are the brand name.

```
BOARD = A logo concept presentation board for a brand called BADCODE, shown straight on and filling
the whole frame, rendered as clean flat vector graphics. The board is matte near-black. On the left
half, the logo mark alone, large. On the right half, four small mock-ups in a two-by-two grid showing
the same mark in use: a rounded-square phone app icon, a black twelve-inch record sleeve, a white
die-cut sticker on a black laptop lid, and a black T-shirt. Flat colour only: no gradients, no glow,
no drop shadows, no lens flare, no textures. Palette: near-black, cold off-white, and one warm signal
red. No captions, no labels, no annotations, and no words anywhere except the brand name where it is
described below.
```

The "acid" sheet (10) swaps the near-black board for the hi-vis colour; the last two (13, 14) are
not boards at all but the idea shown in the world.

## Round 1 — 14 sheets, 2 candidates each

Model **Nano Banana 2** · aspect **16:9** · `numOutputs: 2` · Flow project "Sept 29 - 16:59"
(id `220fcd6b-b363-4e78-a9a6-2f7b199c4bd0`) · output `…/logo-concepts/round-1/<NN−1>-a.jpg`,
`<NN−1>-b.jpg` (the batch tool numbers files from 0 — see the run log).

| NN | Idea | From |
| --- | --- | --- |
| 01 | End of the Line — line and lamp | direction.md A |
| 02 | End of the Line — with the fork | direction.md §8 |
| 03 | The Look — glancing machine eye | direction.md B |
| 04 | The Notice — type, full stop, catalogue number | direction.md C |
| 05 | Standby — one red square on a black plate | briefs 04, 16 |
| 06 | Pilot plate — machine nameplate with an indicator lamp | brief 13 |
| 07 | The empty slot — warning triangle with one red dot | brief 06 |
| 08 | Ninety-nine and one — a grid of a hundred dots | brief 04 |
| 09 | Seven rings — the round-letter lowercase name | brief 11 |
| 10 | Acid — the name is a colour, `#BADC0D` | brief 12 |
| 11 | The slit — a visor with the red at one end | briefs 09, 15 |
| 12 | The seal — a red disc with a slit of light cut through it | brief 07 |
| 13 | SOLD — the dot doing its political job, in a film frame | direction.md §8 |
| 14 | The lamp in the world — the mark as a photograph in the server hall | direction.md §7 |

### The exact prompts

Each is `BOARD` followed by the text below, unless it says otherwise.

**01 — End of the Line**
> THE MARK: one hair-thin vertical line of cold off-white light that starts at the very top edge of the black field and comes straight down, ending in a single solid red disc attached to its tip, like a lamp hanging on a wire. The line is very thin, the disc is small and flat, and the two are exactly centred on each other. THE NAME: beneath the mark, the word "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white, where the letter O is that same solid red disc and the thin line comes down from above to land in it.

**02 — End of the Line, with the fork**
> THE MARK: one hair-thin vertical line of cold off-white light that starts at the very top edge of the black field and comes straight down, ending in a single solid red disc attached to its tip, like a lamp hanging on a wire. Part-way down, a second fainter branch leaves the main line and curves away to the right, drawn as short warm gold dashes, and runs off the bottom of the field; the main line carries straight on down to the red disc. THE NAME: beneath the mark, the word "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white, where the letter O is that same solid red disc.

**03 — The Look**
> THE MARK: a thin cold off-white ring on the black field, and inside it a single solid red disc about a quarter of the ring's width, pushed hard against the inside of the ring at the upper right, as if a machine eye were glancing sideways rather than staring. No eyelid, no eyelashes, no white of the eye, no highlight: only the ring and the disc. THE NAME: the word "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white, set beside the ring.

**04 — The Notice**
> THE MARK: there is no symbol. The whole identity is the word "BADCODE" set in heavy, plain, condensed sans-serif capitals in cold off-white, followed by one solid red full stop the width of a letter stroke. Under it a thin off-white rule, and under the rule the short code "BC-004" in plain monospaced capitals, set like a catalogue number on a piece of paperwork.

**05 — Standby**
> THE MARK: a square near-black plate with a fine, slightly lighter edge, and on it one small solid red square placed low and to the right of centre, like the standby light on a television in a dark room. Nothing else on the plate. THE NAME: the word "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white, set below the plate.

**06 — Pilot plate**
> THE MARK: a rectangular black machine nameplate with a thin pale inset border and a small screw head in each corner. On the plate, one round solid red indicator lamp in the upper left, and beneath it the word "BADCODE" in wide, heavy stencil capitals in cold off-white, the kind cut into a metal plate. Nothing else on the plate.

**07 — The empty slot**
> THE MARK: an equilateral triangle outline pointing up, drawn in cold off-white with slightly rounded corners in the proportions of a road warning sign, and inside it a single solid red disc sitting where a warning sign's exclamation mark would be. No exclamation mark and no other pictogram. THE NAME: the word "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white, below the triangle.

**08 — Ninety-nine and one**
> THE MARK: a ten-by-ten grid of one hundred small dots, evenly spaced on the black field. Ninety-nine of the dots are dim grey; exactly one dot, in the seventh row and the third column, is solid warm red. THE NAME: the word "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white, below the grid.

**09 — Seven rings**
> THE MARK: the word "badcode" in lowercase, drawn in a geometric alphabet where every letter is built from the same circle and a straight stem, so the word reads as seven equal rings in a row with short stems: b, a, d, c, o, d, e. The letters are thin cold off-white outlines, except the letter o, which is a solid warm red disc. Very tight spacing. There is no other symbol and no other lettering.

**10 — Acid** *(replaces `BOARD`)*
> A logo concept presentation board for a brand called BADCODE, shown straight on and filling the whole frame, rendered as clean flat vector graphics. The whole board is a flat acid yellow-green, the colour of a high-visibility work vest. On the left half, the logo mark alone, large. On the right half, four small mock-ups in a two-by-two grid showing the same mark in use: a rounded-square phone app icon, a twelve-inch record sleeve, a die-cut sticker on a laptop lid, and a T-shirt, all in the same flat acid yellow-green with black lettering. Flat colour only: no gradients, no glow, no drop shadows, no textures. THE MARK: the word "BADCODE" in heavy, condensed, plain sans-serif capitals in solid black, where the letter O is a solid warm red disc. No captions, no labels, no annotations, and no words anywhere except the brand name.

**11 — The slit**
> THE MARK: a long thin horizontal slot drawn as a cold off-white outline on the black field, about six times wider than it is tall, like a letterbox or a visor, and inside it a solid red disc slightly taller than the slot, pushed to the far right end so that it overflows the slot's top and bottom edges. THE NAME: the word "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white, set directly above the slot at the same height as the slot.

**12 — The seal**
> THE MARK: a single solid warm red disc, with one thin vertical slit of the black background cut out of it, running from the top edge of the disc down to just short of its bottom edge, exactly on the centre line, like the impression of a rubber stamp. Nothing else. THE NAME: the word "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white, below the disc.

**13 — SOLD** *(replaces `BOARD`)*
> A still frame from a documentary film: a photograph of a plain water treatment works behind a chain-link fence under a flat grey English sky, shot on 35mm film with fine natural grain, muted cool-neutral palette, calm observational tone, no people. Stuck onto the image in its lower right corner, like the sticker beside a painting in a gallery, is one flat solid red disc. Beneath the photograph runs a black band, and on it in small cold off-white capitals the single word "SOLD". No other text anywhere.

**14 — The lamp in the world** *(replaces `BOARD`)*
> Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, landscape orientation. A monumental dark server hall lost in blackness, photographed from a distance: one thin vertical line of cool pale light hangs from the top of the frame to the middle of the frame, and at its lower end a single small red lamp glows, the only warm point in the picture, with faint out-of-focus points of light hanging in the darkness either side of it like distant status LEDs. Machine-precise geometry receding into deep clean black. No people, no text, no fantasy effects.

## Run log

**RESUME HERE (2026-09-29, before round 1 was fired).** Flow is signed in on channel 1. A fresh
project exists for this experiment: **id `220fcd6b-b363-4e78-a9a6-2f7b199c4bd0`** (Flow named it
"Sept 29 - 16:59"; open it by id). Nothing has been generated yet. Media folder:
`/mnt/d/badcode-videos/brand/clips/logo-concepts/round-1/`.

**How round 1 is to be run:** by ONE `flow-operator` sub-agent, not the main session, so the
generation output stays out of the main context. Sub-agents must run **one at a time** — the whole
session shares one browser, and a second Flow call while one is running kills both
(flow-automation law 16). The agent calls `flow_open_project({ id })`, then
`flow_generate_batch({ prompts: the 14 above in order, outDir, model: "Nano Banana 2",
aspect: "16:9", numOutputs: 2, resume: true })`, and reports `{ items, failed, partial }` plus the
file list. Any `POLICY_BLOCKED` entry is rewritten here (never retried unchanged); any other failure
means re-run the same list with `resume: true`. The main session then reviews **one contact
sheet** of all candidates, not 28 separate images, and records verdicts below.

### Round 1 — ran 2026-09-29 17:17–17:30 (sub-agent `logo-round-1`)

28/28 landed, no policy blocks, no re-runs, 789 s for the batch (≈28 s per image on the free
tier, slower than the ~12 s the automation notes quote). All 1376×768.

⚠️ **Files are 0-indexed:** the batch tool names by prompt index, so `00-a.jpg` = sheet 01 and
`13-b.jpg` = sheet 14 (file prefix = NN − 1). Left as generated so `resume` stays honest.
Contact sheets (every candidate, labelled): `round-1/contact-1.png` (01–07),
`round-1/contact-2.png` (08–14).

**Verdicts (Claude's first read, one look at the contact sheets — Kai rules):**

| NN | Idea | Read | Verdict |
| --- | --- | --- | --- |
| 01 | End of the Line | Both candidates read at every mock-up size; the line landing in the O of BADCODE is the strongest single image of the round. (a) keeps the brief's thin-line/small-lamp ratio; (b) has a fatter lamp. (a) renders mark + name as two drops side by side, which is busier than one | **Lead. Lean in.** |
| 02 | + the fork | Gold dashes read at display size and on the sleeve; dissolve on the sticker and icon | Display-only device, as `direction.md` §8 says. Keep, don't lead with it |
| 03 | The Look | Reads as a record button / loading glyph, not a glance; friendly rather than threatening. (b) misspelt it "BACODE" and invented a second ring | Park |
| 04 | The Notice | Cleanest of the round; the heavy condensed caps + red full stop + `BC-004` read as a British authority notice at every size | **Keep as the wordmark voice** (settles caps vs lowercase next to 09) — and a real fallback if no mark |
| 05 | Standby | Reads as a blank television / device outline with a light; quiet to the point of generic | Cut |
| 06 | Pilot plate | An object (a nameplate), not a mark; stencil caps = army-surplus cliché | Cut |
| 07 | The empty slot | Boldest survivor at sticker size; but it is the hazard-sign cliché, and reads as "danger" rather than "came back to warn you" | Reserve |
| 08 | Ninety-nine and one | Dot grid = every data start-up; the one red dot vanishes at icon/sticker size | Cut as a mark; the "one in a hundred" stays a story device |
| 09 | Seven rings | Round lowercase reads friendly fintech/kids' brand; (a) garbled the letters | Cut — but it is the visual proof for the caps ruling |
| 10 | Acid | Red O on hi-vis acid green is loud and works; the O came out as a tall oval in (a), which is its own idea | **Park as a merch colourway** (T-shirt/sticker), never the primary palette |
| 11 | The slit | Reads as a UI slider/toggle pushed to the red end — a meaning ("the dial turned all the way"), but a widget, not a logo | Cut |
| 12 | The seal | The surprise: a red disc with a vertical slit reads as a **slit-pupil eye** — the most threatening mark of the round, Kai's Terminator instinct straight. (b)'s tapered slit is the stronger. Risks: the *watcher* reading (`the-reader.md`), and the power-button glyph family | **Lean in, as the blade not the eye:** try the slit as *cold light passing through the lamp* — the house blade and the red lamp fused in one glyph that survives at 16 px |
| 13 | SOLD | The red sticker on a photograph of a public works + "SOLD" is a whole campaign format in one frame | **Keep as the campaign format**, independent of which mark wins |
| 14 | The lamp in the world | The mark rendered in the film's register *is* the film's register: the logo and the look are the same picture | The argument for direction A in one image |

### Round 2 — PROPOSED, not run (awaiting Kai's picks from round 1)

Same `BOARD` preamble unless marked, Nano Banana 2, 16:9, 2 candidates each, one sub-agent at a
time, output `round-2/` (0-indexed files again: `00-a.jpg` = R2-01).

**R2-01 — One drop** *(01 tightened: the name is the whole identity)*
> THE MARK AND THE NAME ARE ONE THING; there is no separate symbol. The word "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white sits in the lower half of the black field, and its letter O is a single solid red disc. One hair-thin vertical line of cold off-white light starts at the very top edge of the field and comes straight down to land exactly on the top of that red disc, so the O is a lamp hanging on a wire. Nothing else on the field.

**R2-02 — The blade through the lamp, threaded** *(12 read as light, not as a pupil)*
> THE MARK: one small solid red disc near the centre of the black field, and one hair-thin vertical line of cold off-white light that starts at the very top edge of the field and comes straight down through the exact centre of the disc, ending at the disc's bottom edge, so the disc looks threaded onto the line like a bead. THE NAME: beneath the mark, "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white, where the letter O is that same red disc with the same thin line running down through it.

**R2-03 — The blade through the lamp, pinned** *(the line carries on past the disc)*
> THE MARK: one small solid red disc near the centre of the black field, and one hair-thin vertical line of cold off-white light that starts at the very top edge of the field, comes straight down through the exact centre of the disc, and stops a short way below it, so the disc is pinned on the line. THE NAME: beneath the mark, "BADCODE" in heavy, condensed, plain sans-serif capitals in cold off-white, where the letter O is that same red disc with the same thin line running down through it and just past it.

**R2-04 — The seal in the world** *(replaces `BOARD`; does 12 read eye or lamp in the register?)*
> Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, landscape orientation. A monumental dark server hall lost in blackness, photographed from a distance. In the middle of the frame hangs one small round red light, split down its middle by a thin vertical dark line, the only warm point in the picture, with faint out-of-focus points of light hanging in the darkness either side of it like distant status LEDs. Machine-precise geometry receding into deep clean black. No people, no text, no fantasy effects.

**R2-05 — The drop, as three frames** *(replaces `BOARD`; the two-second ident felt as stills)*
> A storyboard strip of three identical square black frames side by side on a matte near-black board, rendered as clean flat vector graphics, no captions and no numbers. Frame one: a hair-thin vertical line of cold off-white light has just started down from the very top edge and reaches a quarter of the way down; the rest is black. Frame two: the same line now reaches two thirds of the way down, ending in nothing. Frame three: the line has stopped at the same point, and a single small solid warm red disc has lit at its tip, attached, like a lamp on a wire. Flat colour only, no glow, no gradients.

**R2-06 — Acid, merch only** *(replaces `BOARD`; 10 as the colourway it is)*
> A product photograph, straight on, of a folded heavy cotton T-shirt in flat acid yellow-green, the colour of a high-visibility work vest, lying on a plain near-black surface, and beside it a die-cut sticker in the same acid colour. Printed on the shirt's chest and on the sticker: the word "BADCODE" in heavy, condensed, plain black capitals, where the letter O is a solid warm red disc. No other print, no tags, no labels, and no text anywhere else.

### Kai's pick — 2026-09-29, after round 1

Kai's words: *"I really like B, the look, with the circle with the red dot in. It looks a bit like
a Death Star, it looks like an eyeball, I think we've got something there… a fully filled in red
dot… I really like the font, the bottom round lower case, as a icon and a single logo… I think we
should have the line slightly thicker."*

So, as understood (not yet a final ruling):
- **Icon:** The Look — a ring with a solid red dot pushed off-centre, upper right. Ring line
  thicker than the first sketch.
- **Name:** "badcode" in the round lowercase from the direction sheet's "voice of the name" cell,
  where the **o is a fully filled red dot** (not the ring-with-dot).
- This **overturns** `direction.md`'s recommendation (A, End of the Line, and heavy caps). The
  round-1 verdicts above were Claude's; Kai's pick wins.

Drawn out in `sketches/look-sheet.png` (script `look-sheet.mjs`): four ring weights, the name on
dark and white, side-by-side and stacked lock-ups, 128→16 px, the name shrinking, the eye-as-o
for the record, the never-in-the-middle rule, drawn badly, the ident, app icon, sticker, sleeve.
Clean references for a Flow mock-up round in `sketches/look/` (`look-icon`, `look-icon-on-white`,
`look-name`, `look-stacked`; ring weight = "thicker 2").

**Ring weight — Kai 2026-09-29: "thicker 3"** (ring line = 21/160 of the ring's radius, nearly
twice the first sketch). `look-sheet.mjs` `REF` updated; the lock-ups, small sizes, mock-up cells
and the `sketches/look/` references are regenerated at that weight.

**Clash check on The Look (Sonnet sub-agent, 5 searches, 2026-09-29).** No existing ring +
off-centre-dot mark surfaced; search results were mostly stock-logo pages, so this is "not found",
not "does not exist". Nearest risk: Big Brother UK's Daniel Eatock-era geometric eyes (2001–2025,
secondary sources, images NOT viewed) — low to medium. 2026's series moved to a realistic eye
(deadline.com, secondary). No documented Lucasfilm action over Death Star-like logos (Lucasfilm
holds "TINY DEATH STAR"; no broad "DEATH STAR" mark found). Stay clear of centred ring-dot marks
(Target, HAL 9000 — memory). **Owed, by a human:** eyeball eatock.com/2003/big-brother-4/,
/2005/big-brother-6/, /projects/big-brother-10-logo; UK IPO device-mark search, classes 9/41/42.

**Name check (Sonnet sub-agent, 7 searches, 2026-09-29).** No brand found whose "o" is a solid
red disc in lowercase geometric type. ⚠️ **Nearest, and it hits the icon, not the name:** Badoo's
2006–17 logo (dating app, now retired) — multicolour lowercase "badoo" whose first o is a big ring
holding a small solid red dot (medium). Rotring's wordmark: an o that is a dot inside a ring
(medium). Badoo's current logo: red lowercase, two-storey a, no symbol (low–medium). No other
"badcode" brand in round lowercase (badcode.dev = a bare heading, owner unknown).
**Rule it implies:** keep the ring-with-dot as the standalone icon; never put the ring-with-dot
inside the word (that is Badoo's old logo). The o in the name stays a solid dot — as Kai picked.
Fonts (if one is ever needed beyond our hand-drawn letters): TeX Gyre Adventor (GUST Font
Licence) is the free Avant Garde; URW Gothic's AGPL does not clearly cover logos or websites.
Red #e6291c on #050607 = 4.54:1 (3.06:1 simulated protanopia); logos are exempt from WCAG
contrast; #ff4633 would lift it to 5.96:1 / 4.16:1.

### Design session — the logo bench (2026-09-29)

Artifact: https://claude.ai/artifact/4Tf8nXY8RmRokTevDQ7cWe (source `tuner/index.html`). Sliders:
ring thickness, dot size, how far off centre, which way it looks, the red (four swatches), letter
weight and spacing of the name. Live proofs: hero, name on white, side-by-side, stacked, profile
pictures 128→16 px dark/light, browser tab, the name shrinking, app icon, sticker, sleeve, drawn
badly, the 2-second ident. **Save this version** writes to the artifact's db collection `saves`
(read it with ArtifactData `list`); the final SVGs get generated by script from the chosen save.

**Kai's save 1 (18:14):** ring 0.04 (hair-thin — Kai moved away from "thicker 3"), dot 0.245,
push 0.51, angle 55°, red #cc2b37 (the old logo's red), letter weight 0.30, spacing 0.26. Note:
the c sits too far from the red o. Fix in bench v2: new slider "pull the c toward the red o"
(`ck`, fraction of letter radius, default 0.35 — the c's open right side makes the gap look
bigger than it is); page now opens on save 1; ring slider floor lowered to 0.015.

### RULED — Kai, 2026-09-29 18:30: "I love this… it's perfect"

Bench save 2 (`52d1h96436mwhgdqjrj7`): ring 0.17, dot 0.245, push 0.51, angle 55°, red #cc2b37,
lw 0.30, tr 0.26, ck 0.42. Now canon in `docs/brand/README.md`; files in `docs/brand/logo/`
generated by `scripts/brand/build-logo.mjs`. Brace logo archived to `docs/brand/archive/2026-09-13-brace/`.
Next: Flow mock-ups from the real files; Jack's say; UK IPO search; wire into `apps/web`.
