---
id: magic-money-tree
title: "Edit plan — The Future He Never Saw"
status: planned, not executed
updated: 2026-09-29
narration: storyboard.md as rebuilt 2026-09-28 (19 scenes, five movements, planned 15:10)
footage: footage.md sections 7, 11 and 12
---

# Edit plan — *The Magic Money Tree: The Future He Never Saw*

**What this file is.** The paper edit. Every line of the working narration, in order, paired with
the picture that sits under it, where that picture lives on disk, the in-point inside the source,
and what we do to it. A later session with Premiere open executes this top to bottom and should not
need to make a creative decision it cannot find here.

**What it is not.** It does not change the words; [`storyboard.md`](./storyboard.md) owns those, and
its §5 guardrails bind everything below. It does not clear rights; [`footage.md`](./footage.md) does.
If this file and either of those disagree, they win and this file gets corrected.

**Status, 29 September 2026: planned only.** No Premiere project exists for this film yet. Nothing
here has been put on a timeline.

---

## 0. How to read and execute this plan

### 0.1 Timing

- **Clock** = position on the finished timeline, `mm:ss`. Scene start times come from the
  storyboard's allowances (§3 running order): they add up to **15:10**.
- **Narration is not recorded yet.** Timings are planned at the storyboard's pace (about 105 words a
  minute including pauses). When the real voice exists, **the voice sets the cut**: slide each
  picture block to its line's marker and trim; do not stretch the voice to fit the pictures.
- **Source in-points marked `≈`** come from archive.org's thumbnail contact sheets (one frame every
  30 or 60 seconds; the number in a thumbnail's name is its second offset). They get you to the
  right minute. **Pin the exact frame at execution** with `premiere_export_frame` and look.
  In-points without `≈` were frame-checked in an earlier pass.

### 0.2 The sequence

| Setting | Value | Why |
| --- | --- | --- |
| Project | `D:\badcode-videos\magic-money-tree\magic-money-tree.prproj` (create it) | House layout: `<mediaRoot>/<story>/` |
| Sequence | `mmt-rough-cut-v1`, **1920×1080, 25 fps**, square pixels | Most of the archive is British PAL at 25 fps. The American reels (29.97) are conformed and will be interpreted; that is fine for archive |
| V1 | Archive picture: film and stills | The film is mostly this |
| V2 | Overlays: documents over picture, headline crops, the debt chart | Keeps V1 clean to re-cut |
| V3 | Cards: verb cards, date cards, quotation cards, credits | Rendered as PNG, see §0.4 |
| V4 | Labels that must never be separated from their shot: `ILLUSTRATION`, `AMERICAN FOOTAGE`, `RECONSTRUCTION` | Guardrail, see §0.5 |
| A1 | Narration (scratch, then final) | |
| A2 | Music bed (Suno, later) | We make our own. **No archive audio ever**: the conforms are silent by design |
| Markers | One per narration line, named with the line's first four words | So the voice can be dropped in and every block snapped to it |

**Bins**, one per movement, each holding its scenes' folders: `1 Pride`, `2 Craftsman`, `3 Build`,
`4 Misuse`, `5 Statement`, plus `cards`, `_library`. **Never import `clips/_masters/`**: those
originals still carry their soundtracks, which are not ours to use.

### 0.3 The house treatments (named once, used everywhere below)

| Name | What | How |
| --- | --- | --- |
| **FILM-43** | 4:3 archive film, placed honestly | Scale to fill the height (1080), keep 4:3, black pillars. Never stretch, never crop to 16:9 by default. For a 768×576 or 720×576 conform that is Motion scale ≈ **187.5%** on the height; check with `export_frame` |
| **PUSH** | Slow push-in on a still | Scale from fit to fit × 1.12 over the whole hold, `bezier`. Recipe: *a push-in, a pan, a fade* |
| **DRIFT** | Slow lateral move on a wide still | Position x 0.46 → 0.54 over the hold, `linear` |
| **INSET** | A small still (≈800 px) shown as a document, not a plate | Scale ≤ 100% of native so it never upscales past 1.35×; centre on a near-black ground; a 2 px off-white border reads it as a print. Do not PUSH it past 1.05 |
| **DOC** | A document page or headline crop | On V2 over a darkened V1 (V1 opacity 35%); PUSH very slowly to the one line that matters |
| **HOLD** | No move | For the one still that must be looked at: Keynes, scene 08 |
| **DIP** | Dip to black, 12 frames | Between movements only |
| **XD** | Cross-dissolve, 8 to 12 frames | Inside a scene when time moves; hard cuts otherwise |
| **GRADE-BW** | One look for all black-and-white archive | Lumetri: lift blacks to about 16 (never crush; `camping.mp4` shipped crushed), gentle contrast, no tint. Colour films (the cartoons, *Festival in London*) are left in colour: the colour is the post-war feeling |

### 0.4 Cards are rendered, not typed

Premiere's API cannot set text (recipes: *text on screen without a template*). So **every card below
is rendered as a 1920×1080 PNG by ffmpeg** before the edit, into `clips/cards/`, and placed on V3
like a still. One card style for the whole film: off-white type on near-black, one typeface, set
large; the date left of the dot, the verb right of it. The full list of cards is §7.

### 0.5 Rules that bind the picture (from the storyboard and the rulings)

1. **Label what is not what it looks like.** American footage under a British line carries
   `AMERICAN FOOTAGE` on V4 or does not go under that line. The builder of scene 03 is an
   `ILLUSTRATION`. The yacht of scene 11a is an `ILLUSTRATION`. Nothing generated is ever passed off
   as archive, and no living person is ever generated.
2. **No photograph of Baroness Mone** (Kai, 29 September). Headline crops only, the `--headline-only`
   files, which exclude each paper's photograph. Every headline is credited on screen by paper and date.
3. **The NHS and the war were paid by tax, borrowing and rationing.** No printing-press imagery under
   anything before 2009.
4. **Capra and newsreel compilations mix actuality with staged inserts.** A human looks at every
   Dunkirk and war shot before it is kept (footage.md §2b).
5. **Archive audio is never used.** The picture is free; the music and commentary are not.
6. **Credits are owed** for the OGL, Open Justice and CC-BY items. They go in the end credits, §8,
   and where marked, on screen with the item.

---

## 1. Movement 1 — Pride (00:00 – 01:30)

### Scene 01 — Get them off the beach · 00:00 – 00:35

Source: `clips/s01-dunkirk/gov.fdr.25.4.picture-only.mov` (*Divide and Conquer*, part 4, 1943; the
evacuation block is **03:56 – 05:20**, frame-checked).

| Clock | Narration | Picture · source in-point | Treatment |
| --- | --- | --- | --- |
| 00:00 | *(black, 1 s, then the first frame)* | 03:40 animated map, "DUNKIRK" top left | FILM-43, fade up 1 s |
| 00:03 | "Dunkirk. 1940." | continue the map to 03:50 | Card `1940 · DUNKIRK` is **not** used: the map says it |
| 00:06 | "More than 338,000 British and Allied troops evacuated from the beaches and harbour." | 04:04 destroyers line astern | FILM-43 |
| 00:12 | "Naval ships. Merchant crews. Little boats." | 04:44 troops boarding from the water → **04:52 small vessel from above, full of troops** | cut on each noun |
| 00:17 | "People helping people get out alive." | **05:00 British troops on deck, faces to camera** | hold 3 s |
| 00:21 | "A defeat, and an extraordinary rescue." | 04:12 exhausted soldier in profile | |
| 00:25 | "Britain remembers the getting-home part." | 05:08 – 05:20 troops disembarking among civilians | this shot returns in scene 14 |
| 00:30 | "This is about what came after." | last frame of 05:20 held | XD to scene 02 |

🔴 Execution check: confirm each kept shot is actuality, not a dramatised insert (§0.5 rule 4).

### Scene 02 — Home to what? · 00:35 – 01:30

Sources: `clips/s02-home-to-what/` stills; *A Diary for Timothy* (1945, Crown Film Unit) in
`clips/s14-a-life-to-get-back-to/DiaryForTimothy.picture-only.mov`; *Your Very Good Health* (1948).

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 00:35 | "When the war ends, there will still be homes to rebuild," | `HU36188-balham-bus-crater.jpg` (5163 px) | PUSH toward the bus |
| 00:40 | "work to find, people getting ill." | `HU36157-bomb-damage-london.jpg` | INSET-sized, DRIFT |
| 00:44 | "Britain will owe about two and a half times what it earns in a year." | Card **DEBT-1**: `1945 · DEBT ≈ 2½ × A YEAR'S INCOME` over black | V3, hold 5 s. The number returns in 10b |
| 00:50 | "In 1948 it will open the NHS anyway." | *Your Very Good Health* ≈ 05:00 (the map of Britain filling with hospitals) | FILM-43, colour |
| 00:55 | "Almost seventy years later, a nurse will ask about her pay and hear that there is no magic money tree." | Card **QT-TEASE**: `2017 · "THERE ISN'T A MAGIC MONEY TREE"` | V3. The payoff is scene 11 |
| 01:03 | "Both of those things happened in the same country." | split: left the 1948 map frame, right the 2017 card, 2 s | V2 over V1 |
| 01:07 | "One economist helped explain the first. He did not live to see it." | `clips/s08-keynes-dies/Keynes_Martin-monks-house.jpg` | slow PUSH, 1.00 → 1.06 only |
| 01:14 | "John Maynard Keynes." | same still | name card lower third `JOHN MAYNARD KEYNES · 1883–1946` |
| 01:18 | "This is the future he never saw." | *Diary for Timothy* ≈ 02:00 (the newborn) | hold; **title card** `THE FUTURE HE NEVER SAW` at 01:24, 6 s, DIP to movement 2 |

---

## 2. Movement 2 — The Craftsman (01:30 – 04:20)

### Scene 02a — Germany, 1923 · 01:30 – 02:20

All stills, `clips/s02a-germany-1923/`, all 5,000 px and over. No free film of 1923 exists.

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 01:30 | "Germany. 1923. Seventeen years before Dunkirk." | Card `1923 · GERMANY` | V3, 2 s |
| 01:33 | "War debts, reparations and a political crisis have strained the state." | `In a Berlin Bank LCCN2014716642.jpg` | PUSH |
| 01:39 | "It borrows from its central bank, which creates the money." | `GER-110-Reichsbanknote-500 Million Mark (1923).jpg` | DRIFT across the note |
| 01:44 | "Then the Ruhr is occupied and production stalls." | `French enter Essen LCCN2014715614.tif` → `13-1-23 Essen patrouille de dragons.jpg` | cut, PUSH on the dragoons (8460 px) |
| 01:51 | "The state pays the workers anyway. More notes. Fewer goods." | `GER-116-…10 Billion Mark` → `GER-127a-…500 Billion Mark` → `Reichsbanknote Zwanzig Milliarden Mark…` | three hard cuts on "More notes", "Fewer", "goods": the numbers climbing are the joke nobody has to say |
| 01:57 | "In some places people are paid daily, and hurry to spend it before the prices change." | `Berlin - la foule assiège la voiture d'un boulanger…btv1b9024458p.jpg` (the bread crowd, 7000 px) | PUSH into the crowd |
| 02:05 | "The currency collapses." | `Gov't notice of French Invasion at Essen LCCN2014715615.jpg` | HOLD, 2 s |
| 02:08 | "That is one thing you can do with a money tree. You can shake it." | **Verb card** `1923 · SHAKE` | V3, hard cut in, 3 s |
| 02:13 | "The money falls. There is nothing underneath it to buy." | back to the bread crowd, wider framing | slow DRIFT, XD out |

Credits owed on screen: none required. End credits: Library of Congress, Bain; BnF Gallica, Agence
Rol and Agence Meurisse; National Numismatic Collection, Smithsonian.

### Scene 03 — The unemployed builder and the unbuilt house · 02:20 – 03:15

Sources: the 1931 London stills; *What A Life!* (1949) for a queue; the illustration (to be made).

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 02:20 | "The early 1930s bring the opposite disaster. Falling prices. Closed works. Queues for a job." | `7-10-31, manifestation des chômeurs à Londres (CNews)…btv1b53249445h.jpg` (London, 7 Oct 1931) | PUSH; lower third `LONDON · 1931` |
| 02:29 | *(continue)* | the sibling still (`…arrestation d'une femme…`) | cut |
| 02:33 | "Picture it small. An unemployed builder." | **ILLUSTRATION 03-A**: the builder, idle, in a yard (to make, §6) | V4 label `ILLUSTRATION` |
| 02:37 | "A family needing a house." | ILLUSTRATION 03-B: a family at a window of a crowded room | |
| 02:40 | "The materials, for this example, in the yard." | ILLUSTRATION 03-C: bricks stacked | |
| 02:44 | "The builder can build. The family needs a home. Nothing happens." | 03-A, 03-B, 03-C again, each 1 s, then an empty plot | hard cuts, then hold on emptiness |
| 02:50 | "Need isn't a paying order." | the empty plot held | |
| 02:53 | "That is the second thing you can do. You can starve it." | **Verb card** `1930s · STARVE` | V3, 3 s |
| 02:57 | "Keynes challenged the idea that an economy would reliably put everyone to work by itself." | `What A Life!` ≈ 03:00 (the street queue of men in hats) | FILM-43. 🔴 It is 1949 satire, not 1930s actuality: use it only as texture under Keynes's idea, never under "1930s" |
| 03:05 | "When private spending falls short, government can commission useful work." | *We Work Again* (WPA, 1937) ≈ first work sequence, `clips/s03-unemployed-builder/gov.fdr.352.1.4.picture-only.mov` | V4 label `AMERICAN FOOTAGE · 1937` |
| 03:10 | "The builder hasn't suddenly acquired moral character. He's acquired a customer." | ILLUSTRATION 03-D: the builder at work on the plot | the joke lands on the cut to 03-D |

### Scene 04 — The word "actually" · 03:15 – 04:20

Sources: `clips/s04-the-word-actually/` (MOI 1944 stills, ≈800 px); *London Airport* (1949).

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 03:15 | "That doesn't mean ordering a million houses makes them appear." | ILLUSTRATION 03-D with a thousand plots multiplying | or a plain card if the illustration is not made |
| 03:20 | "If the bricks are missing, make bricks." | *Brick Pavements* (USDA 1937), the brick-laying process, `clips/s04…/BrickPavements.picture-only.mov` | FILM-43, `AMERICAN FOOTAGE · 1937` on V4 (it is process, not place, but label it anyway) |
| 03:24 | "If the skills are missing, train people." | `Technical School- Training at Tottenham Polytechnic…D21395.jpg` | INSET |
| 03:27 | "Those take time too." | `…Grenadier Guardsmen Build Emergency Housing…D25712.jpg`, D25714 | INSET, XD between |
| 03:31 | "And if everyone is already busy, more money doesn't build more homes. It bids up the price of the ones there are." | *London Airport* ≈ 03:30 – 04:30 (earth moved, a labourer laying, a truck tipping) | FILM-43 |
| 03:40 | "Keynes named that limit himself." | Keynes still, tighter crop | HOLD |
| 03:43 | "Demand beyond what the country can physically supply is, he said, 'the proper meaning of inflation'." | **Quote card KEYNES-1**: *"…the proper meaning of inflation."* `KEYNES · 1942` | V3. 🔴 Collate against the printed page before lock (storyboard open item) |
| 03:52 | "Inside that limit: 'Anything we can actually do we can afford.'" | **Quote card KEYNES-2**: *"Anything we can actually do we can afford."* | V3, hold 5 s: this card returns in scene 13 |
| 04:00 | "'Actually' is carrying quite a lot of the sentence." | same card, the word **actually** brightens alone | a second PNG with only that word lit, cut on "Actually" |
| 04:05 | "That is the third thing you can do. You can plant it." | **Verb card** `1942 · THE RULE · PLANT` | V3, 3 s |
| 04:10 | "In work that can actually be done." | `Post War Planning…Repairing Bomb Damaged Housing D24219.jpg` (bricklayers) | INSET, DIP to movement 3 |

---

## 3. Movement 3 — The Build (04:20 – 09:20)

### Scene 05 — Britain did pay for the war · 04:20 – 05:15

Source: `clips/s05-britain-paid/gov.ntis.ava06858vnb1.picture-only.mov` (*Know Your Ally: Britain*,
1943–44). The tax sequence is at **38:45 – 39:30** (frame-checked). The rest of the reel is
unindexed; build a contact sheet at execution to find the rationing and war-production shots.

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 04:20 | "Britain didn't fight the war by discovering a cupboard of free money." | the reel's home-front sequence (find: factory floor) | FILM-43, `AMERICAN FILM · 1944` lower third (it is an American film *about* Britain; say so once) |
| 04:25 | "It taxed. Borrowed. Directed production. Rationed goods." | four shots, one per verb (find: ration books, factory, shipping) | hard cuts on the verbs |
| 04:31 | "Relied on overseas supplies and support." | convoy shots from the same reel | |
| 04:34 | "People paid in work, in foregone comforts, and in losses no budget can measure." | *Pop Goes the Weasel* (1948) ≈ 03:00 (the gun crew) → `HU49414-battersea-girls-rubble.jpg` | FILM-43, then PUSH |
| 04:43 | "Keynes worked on the finances. He proposed taxes and deferred pay to hold spending down while production went to war." | `TNA-CO1069-778-3-loan-signing…jpg` is 1945, **wrong year**: use the Keynes still instead, or the reel's Treasury exterior if it has one | INSET |
| 04:52 | "Inflation was the thing he was trying to prevent." | Card `1940 · PLANT` | V3, 3 s |
| 04:56 | "An American army film of the time put Britain's tax rates on the screen. The highest went to the people with the most." | **38:45 – 39:30**: "EXCESS PROFITS TAX 100%", "HIGH INCOME TAX 97½%" | FILM-43. 🔴 The narrator says no figure until they are checked (footage.md open item 6b). **First "who paid" beat** |
| 05:08 | "Winning would leave another job: organising the peace." | `HU41808-ve-day-celebrations.jpg` (a glimpse forward) | PUSH, XD |

### Scene 06 — A job after the uniform · 05:15 – 05:55

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 05:15 | "Before victory, Churchill's coalition accepted responsibility for maintaining 'a high and stable level of employment' after the war." | **DOC card WHITE-PAPER**: the 1944 Employment Policy White Paper, the quoted line (typeset from Hansard/OPL text) | V3; credit line OPL |
| 05:24 | "Not just finding people something to do in uniform. Making civilian work a public responsibility." | *Diary for Timothy* ≈ 17:00 (a man laying bricks on scaffolding) | FILM-43 |
| 05:31 | "Beveridge's proposals and plans for a national health service were part of the argument about the peace too." | `clips/s06-job-after-uniform/LSE-1383-demand-the-beveridge-plan-1944.jpg` | PUSH down the poster |
| 05:39 | "Keynes wasn't building this future alone." | *Charley's March of Time* (1948) ≈ 02:30 – 04:30 (the road through history) | FILM-43 colour |
| 05:44 | "And a promise on paper still needed a government to carry it out." | back to the White Paper card, the line dims | XD |

### Scene 07 — Victory does not come with a roof · 05:55 – 06:45

Sources: `clips/s07-victory/`: *V-E Day in Piccadilly* (`111-adc-4267`, last ≈45 s, from ≈09:27);
*War Pictorial News 213* (`gov.archives.arc.39216`, part 3, Buckingham Palace crowds, unindexed);
*Allied Victory Parade* (1946); *What A Life!*; the stills.

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 05:55 | "In 1945 Britain wins." | `111-adc-4267` ≈ 09:27 – 10:10, London crowd | FILM-43. 🔴 Confirm it is Piccadilly before keeping |
| 06:00 | "Voters elect Attlee's Labour government." | `TR2876-crowd-ministry-of-health.jpg` (colour, Whitehall) | PUSH. No free election film exists |
| 06:04 | "The celebration does not come with a roof." | `HU49414-battersea-girls-rubble.jpg` | slow PUSH toward the rubble |
| 06:08 | "Debt is enormous. Supplies are short. Rationing continues." | *What A Life!* ≈ 03:00 (the queue) and ≈ 05:00 (the office piled with forms) | FILM-43 |
| 06:15 | "But the war's end releases people and production for civilian work." | *Diary for Timothy*, the miner sequence (find: between ≈ 17:00 and ≈ 30:00) | |
| 06:19 | "Taxes and borrowing remain part of the answer; so do external finance and the difficult business of paying for imports." | *War Pictorial News 213*, docks or shipping if present, else `NARA-531280-ve-day.tif` | |
| 06:26 | "Keynes negotiates an American loan, then defends it in Parliament." | `TNA-CO1069-778-3-loan-signing-1945-orig.jpg` (799 px, Keynes at the table) | INSET |
| 06:31 | "Still finding time to tell a fellow peer: 'I have never heard statistics so funny.'" | **Quote card KEYNES-3** | V3. Light touch: this is the craftsman's wit |
| 06:36 | "The country doesn't wait to clear its entire debt before rebuilding. Debt is a burden. It isn't a veto." | *Allied Victory Parade* (1946), the march past | FILM-43, XD |

### Scene 08 — 21 April 1946 · 06:45 – 07:10

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 06:45 | "Keynes died on 21 April 1946." | Keynes still | **HOLD**, no move, full 25 s. Card `21 APRIL 1946` fades up and away |
| 06:50 | "The NHS would open more than two years later. He had seen victory. He would not see this." | same | |
| 06:58 | "We don't know what he would have made of everything that followed. Other people had the work to do." | same, fade to black over the last 2 s | music drops out; the only silent picture in the film |

### Scene 09 — The promise gets a working day · 07:10 – 08:00

Sources: *Your Very Good Health* (1948), *A Diary for Timothy* (1945), the leaflet.

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 07:10 | "Attlee's government, with Aneurin Bevan as Health Minister, established the NHS." | *Your Very Good Health* ≈ 00:30 (the Halas & Batchelor title) → ≈ 01:00 (Charley's street) | FILM-43, colour |
| 07:16 | "It took legislation, negotiation and people turning up to work." | *Diary for Timothy* ≈ 04:00 (a ward of beds) | GRADE-BW |
| 07:21 | "On 5 July 1948, existing hospitals and services became part of a new settlement:" | Card `5 JULY 1948 · PLANT` | V3, 3 s |
| 07:26 | "care available to everyone, free at the point of use." | `clips/s09-nhs-opens/INF-2-66-02-NHS-diagram-leaflet.jpg` | DOC, PUSH to the line *"It will provide you with all medical, dental and nursing care"* (storyboard picture note). OGL credit on screen |
| 07:34 | "Not free to provide. The staff and suppliers still had to be paid." | *Your Very Good Health* ≈ 06:30 (the trolley labelled CHARLEY) | |
| 07:40 | "Public funding changed who faced the bill." | *Pop Goes the Weasel* ≈ 08:00 (mother and baby at the clinic window) | FILM-43 |
| 07:46 | "A nurse could get on with the work." | *Diary for Timothy* ≈ 08:00 (a nurse at a bedside) | |
| 07:51 | "A patient could get on with getting better." | *Your Very Good Health* ≈ 07:30 – 08:00 (Charley falls out of the tree and is treated) | the lift of the film: let it run |

### Scene 10 — The key in the door · 08:00 – 08:35

Sources: *New Town* (1948), *Pop Goes the Weasel* (1948), *The Proud City* (1945), the 800 px stills.

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 08:00 | "Councils commissioned homes." | *New Town* ≈ 01:30 (the slum street) → ≈ 03:00 (the estate plan) | FILM-43 colour |
| 08:05 | "Builders built them." | *Pop Goes the Weasel* ≈ 07:00 (builders on a roof) | |
| 08:08 | "Families moved in." | *New Town* ≈ 06:30 (a house, a figure at the door) | |
| 08:11 | "Not everyone got a home. Not overnight. But the building continued." | `MOW-T4550-prefabricated-houses.jpg`, `MOW-T59586-newton-aycliffe-new-town.jpg` | INSET, XD between |
| 08:18 | "Under the Conservatives, Harold Macmillan made housing a major priority too." | Macmillan portrait (Anefo, CC0, `clips/s10b-outgrown/…910-7302.jpg`) | PUSH. Credit Anefo / Nationaal Archief |
| 08:23 | "They disagreed about plenty. Large-scale council building wasn't confined to one party." | *New Town* ≈ 07:30 (terraces on the green) | |
| 08:29 | "A key in a front door is a fairly practical sort of patriotism." | `MOW-T51849-designs-for-the-peoples-house.jpg` | INSET, HOLD. The line lands on stillness |

### Scene 10b — Outgrown · 08:35 – 09:20

The movement's payoff. Sources: *Pop Goes the Weasel*, *Festival in London* (1951, colour),
*Wonder Jet* (1950), *Charley Junior's School Days* (1949), *London Airport* (1949), and our chart.

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 08:35 | "And the debt? It was never cleared." | Card DEBT-1 returns | V3 |
| 08:38 | "In pounds, it kept rising." | **CHART 10b**, frame 1: the debt in pounds, a line rising 1946–1973 | V2, own chart from OBR data, animated left to right |
| 08:41 | "The economy rose faster." | CHART frame 2: the economy's line overtakes | |
| 08:44 | "People were housed, treated and in work." | *Festival in London* ≈ 01:00 – 02:00 (crowds, colour) → *Charley Junior's School Days* ≈ 04:00 (the new school) → *Wonder Jet* ≈ 18:00 (the foundry) | three cuts on "housed", "treated", "work" |
| 08:50 | "For twenty years, unemployment averaged under two in a hundred." | Card `1950–1969 · UNEMPLOYMENT UNDER 2 IN 100` | 🔴 secondary source; verify before lock |
| 08:55 | "For twenty-seven years running, the debt shrank against the size of the country." | CHART frame 3: debt as a share of the economy, falling | the picture the scene exists for |
| 09:01 | "Not by magic. Budgets were tight." | *Pop Goes the Weasel* ≈ 00:30 (the two men on the bench) | |
| 09:05 | "Interest was held below inflation, so lenders and savers carried part of the bill. Quietly." | same bench, the man in overalls ≈ 04:30 | the second "who paid" hint |
| 09:12 | "Britain did not shrink to fit its debt. It outgrew it." | Card `1946–1973 · PLANT` then *London Airport* ≈ 09:00 (the control tower, finished) | DIP to movement 4 |

---

## 4. Movement 4 — The Misuse (09:20 – 12:40)

Register change: present tense, colour photographs, no film. The archive warmth is gone on purpose.

### Scene 10a — New money, a particular purpose · 09:20 – 10:15

Sources: `clips/s10a-new-money/` (stills, if the Commons retry landed them; see §6).

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 09:20 | "2008. The banking system is failing." | `Northern Rock Queue.jpg` (2007) | PUSH. Credit "Dominic Alves, CC BY 2.0" |
| 09:24 | "Government buys bank shares, makes loans and gives guarantees to keep it standing." | `Lehman Brothers-NYC-20080915.jpg` | DRIFT. Credit "Robert Scoble, CC BY 2.0". 🔴 It is New York: the line is about Britain's rescue, so the shot is "the crisis", not "the rescue"; keep it short |
| 09:30 | "In March 2009 the Bank of England does something else." | `Bank-of-England.jpg` (7200 px) | PUSH. Credit "acediscovery, CC BY 4.0" |
| 09:34 | "It creates new money, electronically, and uses it to buy bonds." | **DIAGRAM 10a**: one transaction, Bank → new money → buys a bond from a fund | V2, own diagram; animated in three steps |
| 09:41 | "This is new money. The Bank says so itself." | **Quote card BOE-1**: the Bank's own sentence, attributed `BANK OF ENGLAND · 2014` | quotation, not a copy of the Bank's graphics (its site is non-commercial) |
| 09:46 | "Most money, in fact, is made by ordinary banks when they lend. There was never a fixed national pot." | `Threadneedle Street doors, Bank of England.jpg` | HOLD |
| 09:53 | "The Bank's new money probably prevented a worse slump." | `Bank of England Facade.jpg` | |
| 09:58 | "It also lifted the price of things people already owned." | Card `2009 · SHAKE` | V3 |
| 10:05 | "Good news, if you owned some." | back to the Northern Rock queue, reframed on the people | the line lands on the ordinary faces |

### Scene 11 — The promise requires another shift · 10:15 – 11:25

Question Time is BBC-owned. This plan uses **cards** (Kai's ruling on clip or card is still owed;
if he chooses the clip, it replaces the QT cards one for one at the same clock).

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 10:15 | "2010. Borrowing is very high." | `Chancellor of the Exchequer George Osborne (6128163568).jpg` (2011) | PUSH. Credit "Foreign and Commonwealth Office, CC BY 2.0" |
| 10:19 | "The case for cutting is one every household understands: you can't keep spending money you haven't got." | the Red Book, June 2010, cover and one page | DOC. Credit OGL |
| 10:27 | "The Coalition chooses tax rises and spending restraint. Mostly restraint." | `Budget 2014; Chancellor George Osborne…jpg` (960 px) | INSET |
| 10:32 | "Public-sector pay is frozen for two years, then held to about one per cent." | Card **PAY**: `2010–2017 · PAY FROZEN, THEN ~1%` | V3 |
| 10:38 | "So the Bank is creating money while the Treasury is holding it back. Same country. Same years." | split screen: Bank of England left, the Red Book right | V2 |
| 10:45 | "2017. Question Time. Nurses ask the Prime Minister about pay." | `Theresa May (2016).jpg` (official portrait) | PUSH. Credit OGL |
| 10:50 | "One says her payslip matches the one she had in 2009." | Card **PAYSLIP**: a typeset payslip, 2009 and 2017 side by side, identical | V3, our own graphic, no real person's document. 🔴 Payslip line is secondary-sourced: check against the clip |
| 10:56 | "Theresa May says she recognises the job they do." | Card **QT-1**: her words, exact, `BBC QUESTION TIME · 2 JUNE 2017` | V3 |
| 11:02 | "Then she says there isn't a magic money tree that we can shake." | Card **QT-2**: *"…there isn't a magic money tree that we can shake…"* | V3, hold 4 s. Her verb is the film's verb: let "shake" sit |
| 11:08 | "You can print the money." | Card `2017 · STARVE` | V3 |
| 11:12 | "You can't print the nurse. She was already there." | *Diary for Timothy* ≈ 15:00 (the nurse walking the patient on crutches, 1945) | FILM-43. The same kind of nurse, seventy years earlier. Hold |

### Scene 11a — Money was found · 11:25 – 13:00

The scandal scene. **Legal guardrails in storyboard §3 scene 11a are mandatory.** No photograph of
Baroness Mone. Headlines are the `--headline-only` crops in
`clips/s11a-money-was-found/press/`, each credited on screen. Say **£122m** (the court's figure),
never £148m, never "fraud", never "Tory peer" as current. **Get the legal read before this scene is
cut, not after.**

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 11:25 | "2020. Covid. Money is found. In days." | `10 Downing Street COVID-19 press conference, 20 March 2020.png` | INSET (960 px). Credit OGL |
| 11:30 | "The Treasury borrows hundreds of billions. The Bank creates hundreds of billions more." | Card `2020 · BORROWED + CREATED` | V3 |
| 11:36 | "Some of what government spends keeps wages paid. That part is planted." | Card `2020 · PLANT` | V3. Say it fairly: the furlough worked |
| 11:42 | "Some goes down a priority lane, for suppliers recommended by ministers, MPs and peers." | headline `2022-01-12--bbc--govt-ppe-vip-lane-unlawful-court-rules--headline-only.png` | DOC. 🔴 That ruling concerned two other firms: the picture illustrates "the lane", not this company |
| 11:50 | "One company is a few weeks old. It wins contracts worth two hundred and three million pounds." | Contracts Finder notice, £122,000,000 (screenshot to capture, §6) → the second notice, £80,850,000 | DOC, PUSH to each figure. Credit OGL |
| 11:58 | "The gowns can't be used." | `Ambassador Earl Miller…PPE gown shipment…jpg` | INSET, `AMERICAN PHOTOGRAPH` label: generic gowns only |
| 12:01 | "A court orders a hundred and twenty-two million repaid." | the judgment page, `caselaw.nationalarchives.gov.uk/ewhc/comm/2025/2486` (screenshot to capture) → headline `2025-10-01--bbc--high-court-mone-linked-company-breached-contract--headline-only.png` | DOC. Credit "Contains information licensed under the Open Justice - Licence v2.0." |
| 12:07 | "The company goes into administration the day before the judgment." | Card `30 SEPT 2025 · ADMINISTRATION` then `1 OCT 2025 · JUDGMENT` | V3, two cards, hard cut |
| 12:12 | "Baroness Mone had told the government she would not benefit." | Card: the date and the substance of her May 2020 assurance, attributed | V3 |
| 12:17 | "She later said on television that she stood to benefit from about sixty million." | headline `2023-12-17--bbc--mone-admits-stands-to-benefit-60m--headline-only.png` | DOC. Her own words: the safest card in the scene |
| 12:23 | "She denies any wrongdoing." | same headline, dimmed | hold 2 s: the denial gets its own beat |
| 12:26 | "The following spring, a company run by the supplier's owner of record bought a yacht." | **ILLUSTRATION 11a-Y**: a large sailing yacht, plainly drawn, not the real vessel (to make, §6) + `2024-07-18--boatinternational--lady-m-yacht-auction--headline-only.png` | V4 `ILLUSTRATION`. 🔴 Never a photograph of a different "Lady M" (there are three) |
| 12:33 | "No court has connected those facts. We are only reading the dates." | Card: three dates in a column: `MAY 2020 · CONTRACT` / `MAY 2021 · YACHT` / `OCT 2025 · JUDGMENT` | V3, the dates appear one by one |
| 12:40 | "In the 1940s, the people with the most paid the most." | *Know Your Ally: Britain* 38:45 (the tax cards, a second's reprise) | FILM-43 |
| 12:45 | "In the 2010s, the nurse paid." | Card PAYSLIP reprise | V3 |
| 12:49 | "In 2020, some of the people with the most got paid." | Card `2020 · SHAKE` | V3, hard cut, 3 s, then DIP to movement 5 |

Skip in this scene (from the press pass): LBC's "fire sale" headline (fraud and bribery framing);
Good Law Project (a campaigner, not a paper); the June 2026 liquidators' claims unless attributed on
screen as *claims*. The July 2026 Covid inquiry headline (£10bn wasted) is available, but the inquiry
found "no evidence of cronyism or corruption" in the final awards: never pair it with a line implying
corruption.

---

## 5. Movement 5 — The Statement (13:00 – 15:10)

### Scene 12 — They knew about the magic · 13:00 – 13:35

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 13:00 | "Go back to 1948." | *Your Very Good Health* ≈ 01:00, colour | FILM-43, XD |
| 13:03 | "Two months after the NHS opened, its own pamphlet told the public: 'no fairy wand was waved on July 5th'." | **DOC**: TNA `MH 55/965`, the September 1948 pamphlet (🔴 **not on disk**: fetch, §6) | PUSH to the line. Credit OGL |
| 13:13 | "New hospitals, doctors and nurses had not appeared overnight." | *Diary for Timothy* ≈ 04:00 (the ward) | |
| 13:18 | "They knew there was no magic. They built it anyway." | *London Airport* ≈ 03:00 (workers laying) | |
| 13:24 | "The absence of magic wasn't the end of the discussion. It was the beginning of a job list." | *New Town* ≈ 03:00 (the plan) | |

### Scene 13 — You plant it · 13:35 – 14:25

The recall montage. Each verb brings back its pictures, fast.

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 13:35 | "So. She was right. You can't shake it." | QT-2 card (0.5 s) → the 1923 bread crowd → `500 Billion Mark` note | hard cuts |
| 13:40 | "People have tried." *(or Kai's August "Nobody ever has": his ruling owed)* | Card `2020 · SHAKE` flash | |
| 13:43 | "You can't starve it either. That has been tried too." | ILLUSTRATION 03-A (the idle builder) → PAYSLIP card | |
| 13:48 | "A household can't create money, or raise a tax. A country can." | Bank of England → the 1944 tax card | |
| 13:54 | "So a country can do the third thing. You plant it." | Card `PLANT` alone, no date | V3, 3 s |
| 13:58 | "There is a magic money tree." | black, 1 s | the only line over black |
| 14:00 | "Keynes knew how to use it." | Keynes still | HOLD |
| 14:03 | "You plant it in work." | *Your Very Good Health* (the hospital map) → *New Town* (the key-in-the-door house) → `MOW-T51849` | three cuts |
| 14:08 | "Britain did, owing more than it ever had. Then it outgrew the debt." | CHART 10b, final frame | V2 |
| 14:15 | "'Anything we can actually do we can afford.'" | Quote card KEYNES-2 returns | V3, hold to 14:25 |

### Scene 14 — A life to get back to · 14:25 – 14:50

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 14:25 | "Keynes never saw the NHS open. Other people did." | *Diary for Timothy* ≈ 04:00 → ≈ 08:00 | GRADE-BW |
| 14:30 | "And every day after that, other people made it work." | *Diary for Timothy* ≈ 15:00 (nurse walking the patient) | let it run |
| 14:36 | "We began with getting people home." | Dunkirk `gov.fdr.25.4` 05:08 – 05:20 (disembarking) | FILM-43: the first scene's last shot |
| 14:40 | "A country worth coming home to still needs building." | *Diary for Timothy* ≈ 36:00 (the baby, the film's end) | |
| 14:45 | *[Quieter.]* "There should be a life to get back to." | hold, fade to black over 3 s | music resolves. Then 2 s of black: the film has ended |

### Scene 15 — One more thing · 14:50 – 15:10

The coda. After the black. No archive. **Brand imagery made in Flow** (§6): the BadCode register,
near-black, one light, machines that build.

| Clock | Narration | Picture | Treatment |
| --- | --- | --- | --- |
| 14:50 | "One more thing." | **FLOW 15-A**: a single seed in dark soil, one thin light | fade up |
| 14:53 | "The limit was what we can actually do." | Quote card KEYNES-2, the word *actually* lit | V3 |
| 14:57 | "Machines are about to move it." | FLOW 15-B: machine arms building, calm, not menacing | (optional "I would know." here: Kai's ruling owed) |
| 15:01 | "Borrowing to build was a good bet in 1945. It is a better one now." | FLOW 15-C: a sapling where the seed was | |
| 15:06 | "Not shaken. Not starved. Planted." | three verb cards: `SHAKEN` / `STARVED` / `PLANTED`, one word each, the last held | cut to black, then credits |

---

## 6. What must exist before the edit can start

| # | Item | For | Status 2026-09-29 | Who / how |
| --- | --- | --- | --- | --- |
| 1 | The Premiere project and sequence | all | ⬜ not created | `premiere_create_sequence`, settings §0.2 |
| 2 | Picture-only conforms of every film | all | 🟡 conform job running; see footage.md §12 | ffmpeg, already scripted |
| 3 | Commons stills for 03, 04, 07, 10a, 10b, 11, 11a | 03–11a | 🟡 retry running after a rate limit | script in the session scratchpad |
| 4 | All cards in §7, rendered as PNG | throughout | ⬜ | ffmpeg `drawtext`, one style |
| 5 | CHART 10b (debt in pounds vs economy; debt as share) | 10b, 13 | ⬜ | own chart from OBR public data; verify the figures at source first |
| 6 | DIAGRAM 10a (one QE transaction) | 10a | ⬜ | own graphic |
| 7 | Screenshots: the judgment page; both Contracts Finder notices | 11a | ⬜ | browser, crop to the figures |
| 8 | TNA `MH 55/965` pamphlet image | 12 | ⬜ not downloaded | TNA page, OGL |
| 9 | Flow illustrations 03-A to 03-D (builder, family, bricks, building), 11a-Y (yacht), 15-A to 15-C | 03, 04, 11a, 13, 15 | ⬜ | `flow-prompt` + `badcode-art-direction`; **Kai approves every plate** before any video credit |
| 10 | A contact sheet at 10-second spacing for *Know Your Ally: Britain* 00:00–38:00 | 05 | ⬜ | to find the rationing and factory shots |
| 11 | A scratch narration | timing | ⬜ | AI Studio voice or Suno per house method, **only when asked** |
| 12 | The scene 11a legal read and fact re-check | 11a | 🔴 owed | a human lawyer; litigation is live |
| 13 | Kai's open rulings: QT clip or cards; "People have tried" vs "Nobody ever has"; "I would know." | 11, 13, 15 | 🔴 owed | Kai |

## 7. Card list (render all, one style)

Verb and date cards: `1923 · SHAKE` · `1930s · STARVE` · `1942 · THE RULE · PLANT` · `1940 · PLANT` ·
`5 JULY 1948 · PLANT` · `1946–1973 · PLANT` · `2009 · SHAKE` · `2017 · STARVE` · `2020 · PLANT` ·
`2020 · SHAKE` · `PLANT` · `SHAKEN` · `STARVED` · `PLANTED` · `1923 · GERMANY` · `21 APRIL 1946` ·
`30 SEPT 2025 · ADMINISTRATION` · `1 OCT 2025 · JUDGMENT` · the three-date column (11a).

Data cards: DEBT-1 · `1950–1969 · UNEMPLOYMENT UNDER 2 IN 100` · PAY · `2020 · BORROWED + CREATED`.

Quotation cards (exact words, attributed): KEYNES-1 · KEYNES-2 (and its *actually*-lit variant) ·
KEYNES-3 · WHITE-PAPER · BOE-1 · QT-TEASE · QT-1 · QT-2 · the May 2020 assurance (11a).

Labels (V4): `ILLUSTRATION` · `AMERICAN FOOTAGE · 1937` · `AMERICAN FILM · 1944` ·
`AMERICAN PHOTOGRAPH` · `LONDON · 1931`. Lower thirds: `JOHN MAYNARD KEYNES · 1883–1946`.
Title: `THE FUTURE HE NEVER SAW`.

## 8. End credits (owed; exact strings from footage.md and docs/footage/)

Archive film: US National Archives and Records Administration; FDR Presidential Library; Crown
copyright (expired), Central Office of Information and Crown Film Unit, via The National Archives and
the Internet Archive; Prelinger Archives. Photographs: Imperial War Museum collections via Wikimedia
Commons (Crown copyright expired); Library of Congress, Bain Collection; Bibliothèque nationale de
France, Gallica (Agence Rol, Agence Meurisse); National Numismatic Collection, Smithsonian; LSE
Library; Nationaal Archief / Anefo; Dominic Alves (CC BY 2.0); Robert Scoble (CC BY 2.0);
acediscovery (CC BY 4.0); Rev Stan (CC BY 2.0); Foreign and Commonwealth Office (CC BY 2.0).
Licences: "Contains public sector information licensed under the Open Government Licence v3.0."
"Contains Parliamentary information licensed under the Open Parliament Licence v3.0." "Contains
information licensed under the Open Justice - Licence v2.0." Headlines quoted for criticism and
review: BBC News, and each other paper shown, with dates. **Reconcile against the final cut: credit
only what is used.**

## 9. The execution run, in order (for the session that has Premiere)

1. `premiere_status`; confirm the media root is `D:\badcode-videos`.
2. Confirm items 1 to 9 of §6 exist; stop and say which do not.
3. Create the project and sequence (§0.2); create the bins; import each scene folder into its bin
   (`premiere_import`, per clip, never a concat: house ruling 2026-08-24). Never import `_masters`.
4. Lay markers for every narration line at its planned clock.
5. Movement by movement: place V1 in order, trim to the planned durations from the in-points above,
   apply the treatments, then V2, V3, V4. **After each scene, `premiere_export_frame` at three points
   and look.**
6. Leave a marker note wherever an in-point marked `≈` needed a judgement, so Kai can check it.
7. Save; export a low-resolution review render; run nothing through `delivery-qc.sh` until the real
   narration is in.
