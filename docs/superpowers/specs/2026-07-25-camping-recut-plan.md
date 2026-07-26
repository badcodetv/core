# Camping recut — 24 slides + stinger — execution plan

**Date:** 2026-07-25 · **Status:** approved creative, ready for execution
**Owner:** Kai · **Executors:** parallel workflow agents (Opus), one human-gated Flow lane

---

## 1. Context

The live camping comic (`apps/web/src/comics/camping`, 53 pages, assets on bucket
`comics-v2/camping-jack-test`) is a Storyteller-era import: too long, a
choose-your-own-ending structure that separates Tarquin from Bob exactly when the
story needs them together, and no recorded prompts for any panel.

This plan recuts it to **24 slides + 1 stinger** in three movements —
**JUDGE (1–9) · SEE (10–15) · BECOME (16–25)** — bookended on the tent-door POV.
The creative pass (structure + irony) is **locked**; see §3 for the final table.
Core devices: the two-parking-spaces mirror, "let's circle back" as the trip's
exit incantation, the retreat that delivers what it advertised, the W-**AI**-trose
sign, and Bob's name as the emotional payoff.

**What this is NOT:** the camping-v2 from-scratch rework
(`docs/camping-v2/`, worktree `camping-v2-rework`) continues separately. This
recut edits the **live v1 comic** and reuses its existing bucket assets.

---

## 2. Decisions (locked — do not relitigate in tickets)

| # | Decision | Rationale |
|---|---|---|
| D1 | Storyboard records live in **`docs/camping/storyboard/`** (new dir, gpom-short format) | v1 canon dir owns the live comic; camping-v2 is a separate initiative |
| D2 | Slide 25 (ATM stinger) is a **still image** edited from the `a12` poster frame, not a video | menu text is baked into the video; a card reads better as a stinger |
| D3 | Slide 23 is a **light edit of `i31`**, not a recomposition | `i31` already rhymes with `i07` (frontal, cross-legged in tent mouth) — only the shoes + Bags for Life need adding |
| D4 | New/edited images get **new asset keys `img/i34.png`–`img/i39.png`** | never overwrite golden originals |
| D5 | The vocative duel is **"sir" → "mate"** (drop "old boy" from slide 20) | shorter, cleaner class hit |
| D6 | `badcode panel` gets wired for camping (`STORY_DIRS` → `docs/camping`) | unlocks edit-panel for all future camping iteration |
| D7 | Unused v1 assets stay on the bucket, unreferenced | harmless; no cleanup risk |
| D8 | Optional-tier easter eggs (flyer, tote, barrel stencil) are **deferred** unless image rounds go fast | first to drop per creative review |
| D9 | No commits without Kai's say-so | commits auto-push (publishing) |

---

## 2b. What actually shipped — review outcome (2026-07-25)

The §3 table below is the **plan as approved**. Executing and then reviewing it in the
browser changed three things; the storyboard index
(`docs/camping/storyboard/index.md`) is the accurate as-built map.

1. **The comic is 24 pages, not 25.** Spec slide 12 (a second, near-identical wide yurt
   frame) was cut in review — two near-identical frames back to back is exactly the
   scroll stall this recut exists to remove. Its "Daddy's hunting rifle" thought moved
   onto slide 11 as the middle of three staged beats (hold 2.2 → 3.0). **Every page from
   12 onward is numbered one lower than in §3.** Archived: `storyboard/_cut/`.
2. **Slides 2, 3, 4 and 7 were regenerated** (`img/i40`–`i43`). The plan assumed v1's
   city panels were usable. They were not: v1's city Tarquin is a visibly different,
   older man than the retreat/camp Tarquin, which breaks the story's central mirror.
   The four city panels are now internally consistent. Note that Flow will not
   *reproduce* a face — policy-compliant prompting forbids likeness phrasing — so the
   city man still differs from the camp man. That residual gap sits on the multi-year
   collapse between the two, where a changed face is narratively motivated; the yurt
   (same weekend, no time jump) was the indefensible one, hence the cut.
3. **Slide 7 lost the tent and the SUV.** Every prompt placing the tent beside the
   expensive car was policy-blocked (4 attempts, 2 phrasings), as was an edit swapping
   the car. The accepted frame keeps the face, the contempt and the two straddled bays,
   and carries his eyeline off-frame into slide 8's answering POV. Vehicle continuity
   was traded for face continuity deliberately.

Also changed in review: `fontSize` 10 → 14 on all bubbles (10 is unreadable at the
library's 18 default), and the vision's second narration box moved off the tent-self's
face. See §9 for the policy-block lessons, now written into the skills.

## 3. Locked creative spec — the 25 slides

Movements: **JUDGE 1–9 · SEE 10–15 · BECOME 16–25.**
`hold` values are starting points; TUNE flags mean coordinates need browser tuning.
Bubble syntax: `[appearAt-start, appearAt-end]` · type `S`=speech, `T`=thought, `N`=narration/BadCode.

| # | asset | shot | bubbles (exact text) |
|---|---|---|---|
| 1 | `anim/a01` | Shard, dusk drone push-in. `zoom(1.3)`, `transition=null`, hold 2.8 | — |
| 2 | `img/i02.png` | Boardroom, rising chart. hold 1.6 | S "Let's circle back to synergise our bandwidth…" |
| 3 | `img/i03.png` | Lift lobby, applause. hold 1.8 | S "Tarquin, you've done it again. How do you do it?" · S "Easy. You just have to have a Winning Mentality™." |
| 4 | `img/i04.png` | Lobby, weekend chat. hold 2.8 | S "What are you up to this weekend, mate?" · S "A retreat in Wales." · S "What, camping?" · S "Glamping. There's a difference of about £400 a night." · T "He is so cool…" |
| 5 | `anim/a02` | X7 on the night street, Shard behind. hold 2.8 | T "Another week of impressing these morons. A chimp could do what they do." · T "Three grand to meet myself this weekend. Worth every penny." |
| 6 | `anim/a04` | Aerial: the X7 pulls in beside the tatty tent. hold 1.6 | — |
| 7 | **NEW `img/i34.png`** | Ground level: Tarquin sneering down at the tent; behind him the X7 **straddles two bays**, plate `T4RQ 1N`. hold 2.0 | T "Two parking spaces. For that." · T "Get a job, you piece of—" |
| 8 | `img/i05.png` | POV inside Bob's tent, bottle in hand, X7 in the doorway. hold 2.0 | T "At least acknowledge we're getting rained on by the same shitty weather." |
| 9 | `img/i07.png` | Bob in the tent, hat, bottle. hold 2.2 | T "I remember 2008 like it was yesterday. The crash. Everyone lost something — I lost her." |
| 10 | `anim/a06` | Forest road, headlights through rain. hold 1.4 | — |
| 11 | `img/i11.png` | Yurt, candle circle. hold 2.2 | S "I'm Moonwhisper Ascending. I'm here to cleanse my soul — and research my new book, *The Wound That Teaches*." · S (off-frame) "Drink deep. The medicine finds whatever you brought with you." |
| 12 | `img/i12.png` | Tarquin's face in the circle. hold 1.6 | T "I should have brought Daddy's hunting rifle." |
| 13 | `anim/a08` | Full psychedelic repaint, neon river, fireflies. `trip()`, hold 1.8 | T "Fuck me, that kicked in quick." |
| 14 | **NEW `img/i35.png`** | **THE VISION** — Tarquin floats above the car park; the man looking back up from the tent doorway is himself. `trip()`, hold 3.2 | N "You came here to meet yourself." · N "He's been outside Waitrose the whole time." · N "Let's circle back." |
| 15 | **NEW `img/i36.png`** | Directly overhead: Tarquin asleep curled on the forest floor, framed like a parking bay. hold 1.8, `transition=null` into 16 (wake = hard cut) | — |
| 16 | **EDIT `img/i37.png`** (from `i16`) | Wake POV out the tent door: burning camp; **dead clamped X7** in the slide-8 spot; Waitrose sign with **only A and I lit**. hold 2.2 | T "…Wales. I was in Wales." |
| 17 | `img/i18.png` | Newspaper at his boots: "BRITAIN'S LAST WORKER REPLACED BY AI." hold 1.8 | — |
| 18 | `img/i19.png` | Reading it by the burn barrel. hold 2.0 | T "I said a chimp could do it." · T "It didn't even need the chimp." |
| 19 | `anim/a10` | Aerial: the whole car park is a tent city. hold 1.6 | — |
| 20 | `img/i21.png` | Bob and Tarquin either side of the barrel. hold 2.8 | S "Cold ain't it? Haven't seen you in some time." · S "You parked next to me once, I think. Big black thing. Took two spaces." · S "I don't know what to do. For the first time in my life, I genuinely— …Sir. Can you help me?" |
| 21 | `img/i21.png` (repeat, reverse beat) | Same frame; the name beat gets its own page. hold 2.4 | S "Bob. My name's Bob, mate." |
| 22 | `img/i22.png` | Tarquin alone, hands over the flame. hold 2.4 | S (off) "Don't show weakness — they can smell it. Blade under your pillow. This ain't Eton." · T "Nothing's up to me anymore." |
| 23 | **EDIT `img/i38.png`** (from `i31`) | Tarquin drinking in the tent, framed as Bob was in slide 9; **polished Oxfords paired outside the flap**, possessions in **Waitrose Bags for Life**. hold 2.6 | — (the composition is the line) |
| 24 | `anim/a13` | "Badcode" in the puddle. hold 2.4 | — |
| 25 | **EDIT `img/i39.png`** (from `a12` poster) | Stinger card: `EMPLOYMENT COLLAPSE SURVIVAL MENU / ▸ STAY PUT` + footer `THANK YOU FOR BANKING WITH US.` `fadeOutFadeIn` in, hold 2.4 | — |

**Cut from v1:** i01, i06, i08, i09, i10, i13, i14, i15, i17, i20, i23–i30, i32, i33,
a03, a05, a07, a09, a11, a12(video), the empty TODO page, the grave-digger, Charles
as a named speaker, and both dead-end branches.

---

## 4. Work breakdown — waves and tickets

### Dependency graph

```
WAVE 0 (parallel)     WAVE 1 (parallel ×25)     WAVE 2 (serial lane)      WAVE 3                WAVE 4
T-CANON-1             T-SLIDE-01 … T-SLIDE-25   T-IMG-1 … T-IMG-6         T-CODE-1 (comic)      T-VERIFY-1
T-SCAFFOLD-1     →                          →   (Flow, HUMAN-GATED)   →   T-CODE-2 (pipeline) → T-VERIFY-2
T-RESOLVER-1                                                              T-CODE-3 (map/meta)   HUMAN REVIEW
```

- WAVE 1 tickets are trivially parallel (one file each, no shared state).
- WAVE 2 is **one serial lane**: a single Flow browser session; `flow_*` MCP tools
  must not be driven by two agents at once. Each image is **HUMAN-GATED** — Kai
  accepts/rejects candidates (edit-panel style, 2 candidates/round). This lane
  cannot be fire-and-forget.
- T-CODE-1 needs WAVE 1 done (records are its source of truth). T-CODE-2 needs
  WAVE 2 images accepted. Bubble positions are finalized in T-VERIFY-2.

### WAVE 0 — canon + scaffolding

**T-CANON-1** — Update `docs/camping/story.md`: add a "Recut (2026-07)" section
stating the three-movement structure, the locked ironies (two spaces / circle
back / meet yourself / name beat), and that §3 of this spec is the beat list.
Canon is source of truth; the comic is derived. Do not delete the original beats —
mark them superseded.

**T-SCAFFOLD-1** — Create `docs/camping/storyboard/index.md`: table of p01–p25 →
asset key, status (`reused` / `new` / `edit`), one-line shot. Copy the format of
`docs/gpom-short/storyboard/index.md`.

**T-RESOLVER-1** — `packages/cli/src/resolve-panel.ts`: change `camping: null` to
`camping: 'docs/camping'` in `STORY_DIRS`; extend its test to resolve a camping
page once records exist (fixture is fine). Run the package tests.

### WAVE 1 — per-slide records (25 parallel tickets)

**T-SLIDE-NN** (one per slide): write `docs/camping/storyboard/pNN.md` in the
gpom-short record format (frontmatter: `panel`, `characters`, `flow_media_id`,
`model`, `status`, `asset_key`; body: `**Scene:**`, `**Prompt:**`,
bubble script, `**Revisions:**`). Rules:

- **Reused assets** (slides 1–6, 8–13, 17–22, 24): `status: shipped`,
  `asset_key` from §3, `flow_media_id:` empty, prompt section reads
  `Prompt unrecorded (Storyteller-era import). Golden original:
  https://storage.googleapis.com/badcode-storage/comics-v2/camping-jack-test/<key>`.
  Bubble script copied **exactly** from §3 + §5 (coordinates, staging).
- **New/edit slides** (7, 14, 15, 16, 23, 25): `status: planned`, target
  `asset_key` (i34–i39), and the **full Flow prompt from §6 verbatim** — the
  image lane executes from the record, not from this spec.
- Every record ends with a `Revisions:` list, `- v0 (2026-07-25) — recut spec`.
- Agents must read `docs/gpom-short/storyboard/p01.md` as the template first.

### WAVE 2 — image lane (serial, human-gated)

Six tickets, executed **in this order** (hardest creative first while attention
is fresh; edits later because they're mechanical):

| ticket | key | kind | base / references |
|---|---|---|---|
| T-IMG-1 | i35 | generate (the vision, slide 14) | refs: `img/i12.png` (retreat Tarquin), `anim/a03` poster or `img/i17.png` (aerial car park), `img/i07.png` (man-in-tent framing) |
| T-IMG-2 | i34 | generate (the sneer, slide 7) | refs: `img/i03.png`/`img/i04.png` (city Tarquin), `anim/a04` poster (car park geometry), `img/i06.png` (tent + X7 staging) |
| T-IMG-3 | i36 | generate (forest sleep, slide 15) | refs: `img/i25.png` (Tarquin asleep on forest floor — closest existing), `img/i24.png` (jacket) |
| T-IMG-4 | i37 | edit of `i16` golden | golden: `img/i16.png`; X7 ref: `img/i05.png` |
| T-IMG-5 | i38 | edit of `i31` golden | golden: `img/i31.png`; rhyme ref: `img/i07.png` |
| T-IMG-6 | i39 | edit of `a12` poster frame | golden: `derived/anim/a12.poster.webp` (fetch full-res poster) |

Process per ticket: `badcode-art-direction` loop (plan → generate 2 candidates →
Kai picks or redirects → iterate). Reference-anchored via `flow_edit_image` where
a golden exists; `flow_generate_image` + refs otherwise. On acceptance: download
full-res, save to `docs/camping/storyboard/img/pNN.<ext>`, update the record
(`status: done`, `flow_media_id`, revision line). Preflight/recovery via the
`flow-operator` agent (flow-chrome.sh + CDP poll + `flow_status`).

**Optional tier (deferred, D8):** i22 flyer ("GRIEF CIRCLE — first session free —
Moonwhisper Ascending"), i11 tote ("RETURN TO YOURSELF"), i21 barrel stencil
("WINNING MENTALITY™").

### WAVE 3 — code

**T-CODE-1** — Rewrite `apps/web/src/comics/camping/CampingComic.tsx` to the §3
page list. **Mandatory reading first: `packages/comic/AUTHORING.md`.** Keep
`createComic(manifest)`, `trip()` from local `effects.ts`, `zoom` import.
Bubble text/coords/staging come from the WAVE-1 records (§5 coordinates as
starting values). Holds/transitions/effects per §3. Slide 21 repeats `i21`
deliberately (name beat). Slide 25 is an `ImageWidget` still. Remove the TODO
placeholder page. Typecheck must pass with the new manifest keys — coordinate
with T-CODE-2 on key names (i34–i39 as in §3).

**T-CODE-2** — Asset pipeline: **first read `packages/cli/src/assets-build.ts`
and `push.ts` to confirm invocation** (do not guess). Add the six accepted
originals under the pipeline's source location for `camping`, run assets-build
so `assets.manifest.json` gains `img/i34.png`–`img/i39.png` (thumbhash + derived
low/high), and push originals + derived to
`comics-v2/camping-jack-test/`. Verify each new key serves 200 from the bucket.

**T-CODE-3** — Regenerate `page-map.json` for the new 25-page order (fixing the
existing off-by-one), and update `comic.meta.ts` assets only where trivially
mechanical; otherwise leave the stub and note it in the ticket result.

### WAVE 4 — verification

**T-VERIFY-1** — `npm run typecheck && npm run build` from root, green.

**T-VERIFY-2** — `npm run dev`, drive the comic with playwright MCP: screenshot
every page at 2–3 scroll positions; check every bubble against §5 (position,
staging, legibility over the art); tune coordinates in the TSX; confirm slide 15→16
cuts hard, 13/14 trip() runs, 25 fades in; re-screenshot after tuning. Post the
final screenshot set for Kai's review. **HUMAN GATE: Kai approves in browser
before any commit (D9).**

---

## 5. Bubble coordinates (starting values)

Existing coordinates are from the live TSX (proven against the art); NEW values
are composition-based estimates — TUNE in T-VERIFY-2.

| slide | bubble | x | y | type/tail | appearAt | source |
|---|---|---|---|---|---|---|
| 2 | circle back | 34.45 | 34.42 | S, none | [0,1] | existing |
| 3 | done it again | 54.10 | 72.77 | S, none | [0,0.5] | existing |
| 3 | Winning Mentality™ | 50.48 | 21.76 | S, bottom | [0.45,1] | existing |
| 4 | weekend, mate? | 18.48 | 55.44 | S, none | [0,0.25] | existing |
| 4 | retreat in Wales | 48.48 | 72.06 | S, top | [0.2,0.45] | existing |
| 4 | What, camping? | 18.48 | 40.00 | S, none | [0.45,0.65] | NEW |
| 4 | Glamping. £400. | 48.48 | 25.00 | S, bottom | [0.6,0.85] | NEW |
| 4 | He is so cool… | 64.77 | 19.68 | T, none | [0.8,1] | existing pos |
| 5 | chimp | 35.79 | 52.55 | T, none | [0,0.5] | existing |
| 5 | three grand | 60.00 | 30.00 | T, none | [0.5,1] | NEW |
| 7 | two spaces | 30.00 | 25.00 | T, none | [0,0.45] | NEW |
| 7 | get a job | 32.00 | 40.00 | T, none | [0.5,0.9] | NEW |
| 8 | same shitty weather | 69.90 | 47.15 | T, none | [0.1,0.7] | existing pos |
| 9 | 2008 / the crash | 18.89 | 39.06 | T, none | [0.1,0.8] | existing |
| 11 | Moonwhisper | 63.55 | 22.29 | S, none | [0,0.5] | existing |
| 11 | drink deep | 30.00 | 60.00 | S, none | [0.55,1] | NEW |
| 12 | Daddy's rifle | 36.29 | 21.99 | T, none | [0.1,0.8] | existing |
| 13 | kicked in quick | 15.47 | 75.02 | T, none | [0.1,0.8] | existing |
| 14 | meet yourself | 50.00 | 15.00 | N, none | [0.15,0.45] | NEW |
| 14 | outside Waitrose | 50.00 | 80.00 | N, none | [0.45,0.75] | NEW |
| 14 | let's circle back | 78.00 | 88.00 | N, none, small | [0.8,1] | NEW |
| 16 | I was in Wales | 25.00 | 20.00 | T, none | [0.5,1] | NEW |
| 18 | chimp could do it | 52.68 | 21.39 | T, none | [0.1,0.5] | existing pos |
| 18 | didn't need the chimp | 30.00 | 35.00 | T, none | [0.55,1] | NEW |
| 20 | cold ain't it | 17.89 | 24.98 | S, none | [0,0.35] | existing |
| 20 | took two spaces | 15.64 | 45.81 | S, none | [0.35,0.65] | existing pos |
| 20 | sir, can you help me | 80.69 | 34.57 | S, none | [0.65,1] | existing |
| 21 | Bob. My name's Bob, mate. | 15.64 | 45.81 | S, top-right | [0.1,0.6] | existing pos |
| 22 | this ain't Eton | 15.64 | 55.24 | S, none | [0,0.5] | existing |
| 22 | nothing's up to me | 75.00 | 30.00 | T, none | [0.6,1] | NEW |

---

## 6. Flow prompts (verbatim into records; image lane executes from records)

House register for camping (NOT the monolith brand register): *hyper-realistic
cinematic film still, 35mm, fine natural grain, overcast British light, muted
cold palette, wet surfaces, no lens flares, no fantasy effects (except i35), 16:9.*
Character anchors: **city Tarquin** = navy suit/dark overcoat, mid-40s, groomed
(`i03`/`i04`); **retreat Tarquin** = olive field jacket over grey marl (`i12`,
`i24`); **future Tarquin** = same jacket, gaunt, stubbled (`i19`, `i26`);
**Bob** = beanie, sandy beard, layered khaki hoodie (`i07`, `i21`).

### T-IMG-1 · `i35` · slide 14 — the vision
> Psychedelic vision, cinematic film still, 35mm. A man in an olive field
> jacket floats horizontally in a deep teal-and-violet void, seen slightly from
> above, looking down. Far below him, a rain-soaked supermarket car park seen
> from high overhead, its edges bending and rippling like a reflection in
> water; drifting bioluminescent fireflies. In the car park, one battered grey
> dome tent glows warm amber from inside — the only warm light in the frame.
> Sitting in its open doorway, lit like a small portrait and looking straight
> up at the floating man, is the same man — the same face — gaunt, bearded,
> wrapped in blankets. The two mirrored figures face each other vertically
> across the fall. Photoreal-surreal, muted apart from the teal/violet wash and
> the single amber tent.

Acceptance: both faces read as the same man; the tent is the only warm point;
vertical mirror composition survives a 720p downscale. Expect the most rounds
of any ticket — budget for it.

### T-IMG-2 · `i34` · slide 7 — the sneer
> Cinematic film still, 35mm, overcast British drizzle. Ground-level medium
> shot in a supermarket car park: a polished man in his mid-40s in a dark
> navy overcoat stands beside a black BMW X7, caught mid-stride, looking down
> and to camera-left at a battered grey dome tent pitched on the tarmac, lip
> curled in contempt. Behind him the X7 is parked at an angle **across two
> marked parking bays, white lines clearly visible under its wheels**, number
> plate reading T4RQ 1N. Waitrose storefront soft-focus green in the
> background, wet tarmac reflections, muted cold palette, natural light.

Acceptance: the straddled lines are legible without being pointed at; plate
reads T4RQ 1N; Tarquin matches the `i03`/`i04` city look.

### T-IMG-3 · `i36` · slide 15 — forest sleep
> Cinematic film still, 35mm, cold dawn mist. Directly overhead top-down shot:
> a man in an olive field jacket asleep on his side on dark wet forest floor,
> curled small among roots and dead leaves, arms tucked in. Two pale fallen
> birch branches lie on the ground running parallel, one either side of him,
> faintly suggesting the white lines of a parking bay. Muted palette, the
> man small in the frame, quiet and still.

Acceptance: reads first as forest, the bay-lines rhyme only on a second look.

### T-IMG-4 · `i37` · slide 16 — wake POV (edit of `i16` golden)
> Same image, same composition, same weather. Two changes only. (1) On the
> Waitrose fascia sign in the background, every letterform is dead and dark
> except the letters "A" and "I", which still glow supermarket-green. (2) In
> the car park visible through the tent doorway, where a parking bay shows,
> add a derelict black BMW X7 — flat tyres, moss along the window seals, a
> yellow wheel clamp on the front wheel, a faded yellow-and-black penalty
> notice under the wiper, number plate T4RQ 1N. Keep every other element
> identical to the reference.

Acceptance: A+I lighting reads at low-res; the X7 sits where it stood in `i05`;
no drift elsewhere in the frame.

### T-IMG-5 · `i38` · slide 23 — the becoming (edit of `i31` golden)
> Same image, same composition, same palette. Two additions only. (1) On the
> wet tarmac just outside the tent flap, bottom of frame, a pair of polished
> black Oxford shoes placed neatly side by side, toes aligned. (2) Among the
> bedding inside the tent, two green Waitrose "Bag for Life" tote bags used as
> luggage, wordmark legible. Keep the man, tent and background identical.

Acceptance: shoes read as deliberate ritual, not debris; bags legible at 720p.

### T-IMG-6 · `i39` · slide 25 — stinger card (edit of `a12` poster)
> Same image: the rusted CRT survival-menu machine in the car park. Changes:
> the pale highlight bar moves from "FLEE TO FOREST." to "STAY PUT." so STAY
> PUT is the selected option; beneath the menu list, add one smaller line of
> the same phosphor CRT type: "THANK YOU FOR BANKING WITH US." Keep the
> screen's scratches, grime and glow identical.

Acceptance: menu still reads EMPLOYMENT COLLAPSE SURVIVAL MENU; footer is
smaller than the options; nothing else moves.

---

## 7. Orchestration notes (for the session that runs this)

- **WAVE 0 + WAVE 1** are one workflow: 3 setup agents, then fan out 25
  record-writers (`pipeline` over slide packets; each prompt = the ticket text +
  §3 row + §5 rows + §6 prompt for its slide; schema-checked return of the file
  path written). Any workflow-size guideline is overridden by Kai's explicit
  request for per-slide parallelism.
- **WAVE 2 is not a workflow.** It is an interactive edit-panel-style session
  (one Flow browser, Kai in the loop per round). Run it in the main loop with
  `flow-operator` for preflight/recovery.
- **WAVE 3** is 2–3 sequential agents (records → code; images → pipeline).
- **WAVE 4** main loop + playwright, Kai approves, then (and only then) commit.
- Any agent touching comic code reads `packages/comic/AUTHORING.md` first; any
  agent touching records reads `docs/gpom-short/storyboard/p01.md` first.

## 8. Verification checklist (definition of done)

- [ ] 25 records in `docs/camping/storyboard/`, index complete, prompts verbatim
- [ ] `badcode panel camping 14` resolves (record + prompt + golden path)
- [ ] 6 images accepted by Kai, recorded with `flow_media_id` + revision logs
- [ ] `assets.manifest.json` has i34–i39; bucket serves all six (200s)
- [ ] `CampingComic.tsx` = 25 pages, typecheck + build green
- [ ] Playwright scroll-through screenshots reviewed; bubbles tuned
- [ ] Kai approved in browser; committed only after approval

---

## 9. Flow usage-policy blocks — the lesson from this build

More than half of all Flow generations in this build were **blocked by the usage
filter, not slow**. Over CDP a block is indistinguishable from a timeout (no
candidates, generic error), so the retry ladder burns ~90 s per attempt on prompts that
can never pass. This was the single largest time sink of the recut.

**Confirmed triggers, from this build's evidence:**

| Evidence | Trigger |
| --- | --- |
| 4 blocks across 2 phrasings on slide 7 | **Destitution beside wealth in one frame** — the tent next to the expensive car. Remove the tent, the same prompt passes. This is a *composition* trigger, not a word choice. |
| Edit of the passing slide-7 frame blocked | **A reference image that itself carries real brand signage** poisons an otherwise clean delta prompt. |
| First 3 attempts of the build | Real brand name + marque + number plate + likeness phrasing stacked in one prompt. |
| Yurt regeneration, 5 attempts | Blocked, alongside a **recaptcha challenge** — sustained volume also throttles the session. |

**Rules now written into the tooling** (canonical section:
`.claude/skills/badcode-art-direction/SKILL.md` → "Usage-policy blocks", with a rewrite
table; mirrored in `packages/flow-mcp/README.md`, `.claude/agents/flow-operator.md`,
`edit-panel`, `make-comic`):

- Two no-candidate failures on a healthy session = **rewrite, never retry**.
- Invent near-miss brands; never ask for a *legible* real wordmark.
- Phrase faces as **character-design consistency**, never "same face/bone structure".
- Don't stack destitution signals, and don't put them in frame with luxury.
- Load-bearing text belongs in a `NarrationBox`/bubble overlay, not baked pixels.

**Open follow-ons:** (1) `@badcode/flow-mcp` should detect a block and return a distinct
`POLICY_BLOCKED` code instead of a timeout; (2) accepted panels carry visible real
supermarket signage — a **brand-usage decision for publication**, separate from
generation, and one for Kai before release.
