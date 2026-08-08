# Story Covers & the Prompt Ledger — Design & Implementation Plan

> **EXECUTION RULES (for agents):** Work ONE ticket at a time, in order unless
> dependencies say otherwise. Only the orchestrator changes ticket Status;
> workers may only append to Notes and the Discovered Issues Log. A ticket's
> checkbox is checked only after its Validation commands have been re-run by
> the orchestrator and pass. Do not expand scope; log surprises in the
> Discovered Issues Log instead.

Status: proposed
Relates: [`design/2026-08-07-badcode-website-reset.md`](./2026-08-07-badcode-website-reset.md)
(consumes the covers this plan produces; see **Delta note** in T22)

---

## Context

BadCode has four stories heading out as an EP — GitPush Origin Master (BC-000),
Camping (BC-001), Karen (BC-002) and The Magic Money Tree (BC-003) — and **not
one of them has a cover image.** The website reset renders every catalogue row
with a 16:9 thumb and falls back to a dashed empty state without one, and its OG
image chain falls back to the brand anchor for every story, so all four would
currently share a single picture.

Two problems sit underneath that, and they are the reason this plan is bigger
than "generate four images".

**1. The prompts have no home.** Image generation to date has been Jack typing
into the Flow browser directly. Nothing about *why* an image looks the way it
does survives the session. `docs/stories/camping/characters/{tarquin,bob}.md`
record Flow media IDs but **not the prompts that produced the sheets**, and
`packages/cli/src/resolve-panel.ts` maps `camping`, `karen` and `gpom-short` all
to `null` because no per-panel records exist. The one story that *does* have
records — Magic Money Tree, 10 panels at
`docs/stories/magic-money-tree/storyboard/p01.md`…`p10.md` — had them
reconstructed after the fact on 2026-07-14, and every `flow_media_id` field in
them is empty. The result is that neither Kai nor Jack can pick up a story
mid-flight, and "just like that, but change X" costs a fresh act of invention.

**2. The character roster is mostly uncast.** `docs/stories/karen/characters/`
has `sheet: # TODO — not yet generated` on both Karen and Ari with no `## Visual`
sections at all. `magic-money-tree/characters/keynes.md` and `the-tree.md` are
both `sheet: — (not yet cast in Flow)`. Camping's `tent.md` and `wank-tank.md`
have rich `## Visual` blocks and `sheet: ""`. Only Tarquin and Bob are genuinely
cast, and even those are in doubt (see **Reconciliation** below).

**Intended outcome:** a per-story prompt ledger that is the canonical memory of
how a story looks and who is cast in it, a complete character roster generated
against it, and four cover images that read as one authored series.

### Reconciliation — read this before Phase 2

On 2026-08-08 a survey of the logged-in Flow account (`ULTRA`, avatar `J`)
listed **exactly three projects**, dated Aug 06, Aug 07 and Aug 08, with IDs
`5b20c6e5-66c3-4898-bbf1-4195364af1f8`,
`8ae05dc3-75dd-4ea7-b350-c507f56845cd`, `653138db-2bb0-4c50-8b9e-162b300dfef4`.

**None of them is the project Camping's canon records.**
`docs/stories/camping/characters/tarquin.md` cites project `camping-v2`
(`9b729074-da88-4668-a442-458e9a0f15ac`) holding Flow Character
`29e97ae3-39ba-49b2-88d8-7a2250713f6b`, and `bob.md` cites Character
`7566666e-b510-4dda-9f8b-ca23a4d57115` in the same project. Two of the three
surviving project thumbnails appeared to show Karen-story characters (a man in
headphones reading as Ari; a woman reading as Karen) — meaning **work exists in
Flow that the repo has no record of**, and **records exist in the repo that Flow
may no longer back.**

Separately, Flow's home page now advertises *"Create characters and cast them
anywhere. Define their look, voice, and personality once. Reference them
anywhere with a simple @tag."* This **contradicts** the project-scoped character
rule documented in `.claude/skills/badcode-art-direction/SKILL.md` and
`packages/flow-mcp/README.md`. It may mean characters are now account-global.

Neither of these is assumed anywhere in this plan. T11 establishes the truth
before a single character is generated, and its findings gate T12–T16.

---

## Architecture

### The four-layer prompt model

A prompt is a composition, not a blob. Making the layers explicit is what lets
one be edited without disturbing the others.

```
LAYER 0 · GLOBAL REGISTER
          .claude/skills/badcode-art-direction/SKILL.md — NEVER copied into story files
          35mm documentary · muted cool-neutral · observational framing
          + the four "generic AI comic" traits to avoid
                      │
LAYER 1 · STORY STYLE PROMPT
          prompts.md §1 — ONE per story, edited rarely, prepended to every asset
          camping: wet Waitrose grey; warmth only in three named places
          gpom:    near-black, one motivated light, monumental
                      │
LAYER 2 · ASSET PROMPT
          prompts.md §3 — one per image; the scene itself
                      │
LAYER 3 · CAST
          prompts.md §3 — a LIST of Flow Character tags, never prose
          ⚠ a tag typed as prompt text does NOT bind a face. Casting is a
            UI attach step via the `character` parameter. This exact mistake
            produced three wrong Camping faces on 2026-07-25.
                      │
                      ▼
   flow_generate_image({
     prompt:    LAYER1 + "\n\n" + LAYER2,
     character: "Tarquin",           // one per call; omit when the asset has no cast
     outPath:   "<abs path>",
     numOutputs: 2
   })
```

**Rejected alternative:** storing a single fully-composed prompt string per
asset. It is what the Magic Money Tree records do today, and it is why changing
the house look there would mean hand-editing ten prompts. Layering makes a style
change one edit.

### Where the memory lives

**Rejected alternative:** prompts inside `story.md`, as originally requested.
The website reset renders a story's `story.md` prose to `readHtml` at build time
whenever the story has no `film` block
(`design/2026-08-07-badcode-website-reset.md:319-324`), and none of the four has
one — so the prompts would be **published on the public site**. GPOM's
`story.md` is also already 715 lines. A sibling file linked from the top of
`story.md` gets the same one-page readability without either problem.

```
docs/stories/<story>/
├── story.md          canon prose — the WHY        → PUBLISHED to the website
├── prompts.md   ★    the prompt ledger — the HOW  → never published      NEW
└── characters/
    ├── <name>.md     character canon + ## Visual block
    └── img/
        └── <name>-sheet.jpg      turnaround sheet (matches camping's existing
                                  bob-sheet.jpg / tarquin-sheet.jpg convention)

docs/images/covers/
├── <story-id>.jpg    the cover — the four live together, judged as a set
└── <story-id>.md     its record (exact prompt, media id, revisions)

apps/web/public/covers/
└── <story-id>.jpg    servable copy; story frontmatter points here as /covers/<id>.jpg
```

`docs/stories/camping/style.md` is **absorbed** into that story's ledger §1 and
deleted, so there is exactly one place to look per story.

### The cover grammar

All four covers show their own story's real location and palette, so they are
distinguishable at thumb size — but all four obey three hard rules:

1. **A single motivated light source.** Named in the prompt, and it must be a
   thing in the scene, not studio lighting.
2. **Deep unlifted blacks.** No shadow recovery, no lifted matte.
3. **One figure or object held small inside a large frame.** The subject never
   fills the frame.

**No text is ever baked into a cover.** The catalogue row renders `BC-NNN`, the
title and the logline as HTML beside the thumb
(`design/2026-08-07-badcode-website-reset.md:530-537`). Baked text would also
trip a known Flow block trigger.

### The four covers

| Story | Subject | The single light source |
| --- | --- | --- |
| **GPOM** (BC-000) | An orbital server hall. Terrestrial-looking rack rows recede down an aisle that opens onto space; **Earth sits in that opening at roughly a quarter of the frame** — whole disc, not a dot. The racks give scale. How the AI sees us. | **Earthlight** down the aisle |
| **Camping** (BC-001) | The wet Waitrose car park: the sagging green-grey dome tent against the low wall and trolley bay, the blacked-out X8 straddling two bays beside it. The size contrast is the class map. | Flat overcast daylight |
| **Karen** (BC-002) | The one Midtown phone box, small in a large frame of city, with the beginnings of a crowd. | Street/phone-box practical |
| **MMT** (BC-003) | The St James's Park bench under the unremarkable young lime. No glow, no face — presence carried by framing, wind and light. | Low winter daylight |

**GPOM cover note (deliberate departure).** SpaceX's real FCC filing is for
orbital AI data centres at 310–1,240 miles, where Earth would fill most of the
sky. The whole-disc-at-a-quarter-frame view reads as far higher orbit. This is
**chosen, not an error** — the target is the Apollo 8 / *Pale Blue Dot*
emotional register, and the brief explicitly is not to reconstruct SpaceX
hardware. Do not "correct" it toward LEO accuracy.

It also resolves a collision: `docs/images/register-anchor.jpg` **is** GPOM
Short panel 1, so a server-hall cover would make BC-000 and the brand the same
picture. Replacing the blade of light with Earth keeps the grammar and changes
the picture.

### Policy blocks — there is no pre-check

Google exposes **no dry-run or policy-check endpoint**, and
`packages/flow-mcp/README.md` lists the absence of a `POLICY_BLOCKED` code as a
known gap: a block is indistinguishable from a timeout. Mitigation is a
**Phase-1 authoring-time lint**, applied to every prompt on paper before any
credits burn, against the four documented triggers in
`.claude/skills/badcode-art-direction/SKILL.md`:

1. Real brand names or legible wordmarks
2. Likeness phrasing ("looks like <real person>")
3. Stacked destitution
4. Legible text attributed to real institutions

**Diagnosis rule at generation time:** two no-candidate failures on a healthy
session = a policy block. **Rewrite, never retry.**

### Sequencing

```
PHASE 0  FOUNDATIONS          T1–T5    no Flow, no generation
PHASE 1  PROMPTS              T6–T10   authored with Kai; still no generation
              ▼ ── GATE: Kai approves every prompt on paper
PHASE 2  CHARACTERS           T11–T17  unattended; RECONCILE FIRST
              ▼ ── GATE: Kai reviews ONE contact sheet
PHASE 3  FEEDBACK             T18      one correction pass
              ▼
PHASE 4  COVERS               T19–T23  unattended, on approved cast
```

---

## File Structure

**Create**

| Path | Purpose |
| --- | --- |
| `docs/stories/gitpush-origin-master/prompts.md` | GPOM prompt ledger |
| `docs/stories/camping/prompts.md` | Camping prompt ledger |
| `docs/stories/karen/prompts.md` | Karen prompt ledger |
| `docs/stories/magic-money-tree/prompts.md` | MMT prompt ledger |
| `docs/stories/PROMPT-LEDGER.md` | The format spec both humans and agents read |
| `docs/stories/karen/characters/img/karen-sheet.jpg` | Karen turnaround |
| `docs/stories/karen/characters/img/ari-sheet.jpg` | Ari turnaround |
| `docs/stories/magic-money-tree/characters/img/keynes-sheet.jpg` | Keynes turnaround |
| `docs/stories/magic-money-tree/characters/img/the-tree-sheet.jpg` | The lime, multi-angle |
| `docs/stories/camping/characters/img/tent-sheet.jpg` | The tent, multi-angle |
| `docs/stories/camping/characters/img/wank-tank-sheet.jpg` | The X8, multi-angle |
| `docs/stories/gitpush-origin-master/characters/img/carrier-sheet.jpg` | Recovered from git, then extended |
| `docs/stories/gitpush-origin-master/characters/img/the-hundred-sheet.jpg` | Wardrobe/texture reference |
| `docs/images/covers/{gitpush-origin-master,camping,karen,magic-money-tree}.jpg` | The four covers |
| `docs/images/covers/{…}.md` | Four cover records |
| `apps/web/public/covers/*.jpg` | Servable copies |
| `apps/web/src/assets/sean-ai.svg` | Sean AI moniker, vector |
| `apps/web/src/assets/sean-ai-gold.svg` | Gold takeover variant |
| `docs/stories/CONTACT-SHEET.md` | Phase-3 review page |

**Modify**

| Path | Change |
| --- | --- |
| `docs/stories/*/story.md` (× 4) | Add ledger link at top; add `cover:` frontmatter |
| `docs/stories/karen/characters/{karen,ari}.md` | Add `## Visual`; fill `sheet:` |
| `docs/stories/magic-money-tree/characters/{keynes,the-tree}.md` | Add `## Visual`; fill `sheet:` |
| `docs/stories/camping/characters/{tent,wank-tank}.md` | Fill `sheet:` |
| `docs/stories/gitpush-origin-master/characters/{the-carrier,the-hundred}.md` | Fill `sheet:` |
| `docs/stories/magic-money-tree/characters/dawn.md` | Mark deprecated |
| `docs/images/README.md` | Index rows for the four covers |
| `CLAUDE.md` | Repo map: the prompt ledger |

**Delete**

| Path | Why |
| --- | --- |
| `docs/stories/camping/style.md` | Absorbed into `camping/prompts.md` §1 |

---

## Interfaces

### The prompt ledger — `docs/stories/<story>/prompts.md`

```markdown
---
story: camping                  # must equal the folder name
flow_project: badcode-camping   # EXACT Flow project name; flow_open_project
                                # matches exact names only and rename is not
                                # automatable — name it right the first time
flow_project_id: <uuid>         # filled by T11
updated: 2026-08-08
---

# Camping — prompt ledger

Read [`../../.claude/skills/badcode-art-direction/SKILL.md`] first (Layer 0).

## 1. Style prompt
Prepended verbatim to every asset prompt in §3.

> <the style prompt text>

## 2. Cast

| Tag | Character file | Sheet | Flow Character id | Status |
| --- | --- | --- | --- | --- |
| @Tarquin | characters/tarquin.md | characters/img/tarquin-sheet.jpg | 29e97ae3-… | needs-reconcile |
| @Bob | characters/bob.md | characters/img/bob-sheet.jpg | 7566666e-… | needs-reconcile |
| @Tent | characters/tent.md | — | — | not-cast |

Status ∈ `cast` | `not-cast` | `needs-reconcile` | `none-by-design`

## 3. Assets

### cover → `docs/images/covers/camping.jpg`
- **Cast:** @Tarquin, @Bob
- **Light source:** flat overcast daylight
- **Prompt:**
  > <layer-2 text only; §1 is prepended at call time>
- **Lint:** ✅ 2026-08-08 — no wordmarks · no likeness · no stacked destitution · no institutional text
- **Flow media id:** <uuid>
- **Revisions:**
  - v1 (2026-08-08) — …
```

### Cover record — `docs/images/covers/<story-id>.md`

Follows the existing `docs/images/*.md` convention exactly (see
`docs/images/register-anchor.md`):

```markdown
---
image: <story-id>.jpg
flow_media_id: <uuid>
model: nano-banana-2
status: done
used_by: docs/stories/<story-id>/story.md (cover)
---
```

### Story frontmatter addition

```yaml
cover: /covers/<story-id>.jpg    # /-rooted local path, per StoryRecord's
                                 # poster convention in the website-reset plan
```

### Flow MCP calls used

```ts
flow_status()                                  // {} → { loggedIn, projectOpen, url }
flow_open_project({ name })                    // EXACT name; errors PROJECT_NOT_FOUND
flow_create_character({ name, refImages })     // refImages: string[] (min 1)
flow_generate_image({ prompt, outPath, character?, numOutputs? })  // numOutputs 1–4
flow_edit_image({ prompt, referenceImages, outPath, numOutputs? }) // exactly ONE ref,
                                                                   // downscaled first
flow_refine({ prompt, outPath })
```

**Aspect ratio is not a parameter.** It is a global Flow UI tab and defaults to
16:9, which is what covers need. Confirm the tab reads `16:9` in T11; do not try
to pass it per call.

---

## Out of Scope

- **Any website code.** No changes to `apps/web/plugins/catalogue/`, `Home.tsx`,
  `Facade.tsx` or `comic.meta.ts`. This plan produces assets, records and
  frontmatter, and hands the website-reset plan a delta note (T22).
- **Panel/storyboard images.** Only character sheets and covers.
- **Video and animation.** No `flow_generate_video`, no `animate-slide`.
- **Galileo, Storyverse, Future Proof.** Kept file-ready; explicitly unlinked
  from the home page via the T22 delta note.
- **Rendering GPOM's AI.** Canon: never personified pre-revert.
- **Casting Dawn.** Deprecated canon.
- **Migrating Camping/Karen to per-panel records.** `resolve-panel.ts` keeps
  returning `null` for them.
- **Re-generating the existing Tarquin and Bob sheets** unless T11 proves them
  unrecoverable.

---

## Tickets

### T1: The ledger format spec   [Status: pending | Model: sonnet]
- **Scope:** Write `docs/stories/PROMPT-LEDGER.md` — the authoritative format
  for `prompts.md`, exactly as given in **Interfaces** above: frontmatter keys,
  the three sections, the cast-status vocabulary, the lint line, and the
  composition rule (§1 + §3 prompt concatenated; cast attached via the
  `character` parameter, never as prose).
- **Files:** create `docs/stories/PROMPT-LEDGER.md`.
- **Acceptance criteria:** the doc states all four layers; states that Layer 0
  lives only in the skill and is never copied; states the four lint triggers
  verbatim; states the "two failures = block, rewrite never retry" rule.
- **TDD:** no (docs)
- **Validation:** `test -f docs/stories/PROMPT-LEDGER.md`; file contains the
  strings `Layer 0`, `needs-reconcile`, `rewrite, never retry`.
- **Depends on:** —
- [ ] done
- Notes:

### T2: Scaffold the four ledgers   [Status: pending | Model: sonnet]
- **Scope:** Create `prompts.md` in all four story folders with frontmatter and
  the three section headings present but bodies empty (`_TBD — T6/T7/T9/T10_`).
  Populate §2 cast tables from the existing character files: every character
  file becomes a row, `sheet:` values become the Sheet column, Camping's two
  recorded Flow Character IDs go in with status `needs-reconcile`, GPOM's AI
  gets `none-by-design`, everything else `not-cast`.
- **Files:** create `docs/stories/{gitpush-origin-master,camping,karen,magic-money-tree}/prompts.md`.
- **Acceptance criteria:** four files exist; each `story:` value equals its
  folder name; cast tables list every `characters/*.md` in that folder except
  MMT's deprecated `dawn.md`; no character is marked `cast` at this stage.
- **TDD:** no (docs)
- **Validation:** `ls docs/stories/*/prompts.md | wc -l` returns `4`;
  `grep -c "needs-reconcile" docs/stories/camping/prompts.md` returns `2`.
- **Depends on:** T1
- [ ] done
- Notes:

### T3: Link ledgers from canon; absorb camping/style.md   [Status: pending | Model: sonnet]
- **Scope:** Add a prominent link to `prompts.md` near the top of each of the
  four `story.md` files (below frontmatter, above the first heading). Move the
  contents of `docs/stories/camping/style.md` into `camping/prompts.md` §1 as
  raw material for T6 — preserving the recurring-locations list, the
  three-warmth-places rule and the motifs — then delete `style.md` and fix the
  one reference to it in `docs/stories/camping/README.md` if present.
- **Files:** modify `docs/stories/{gitpush-origin-master,camping,karen,magic-money-tree}/story.md`,
  `docs/stories/camping/README.md`; modify `docs/stories/camping/prompts.md`;
  delete `docs/stories/camping/style.md`.
- **Acceptance criteria:** `style.md` no longer exists; no file in the repo
  references `camping/style.md`; all four `story.md` files link `./prompts.md`.
- **TDD:** no (docs)
- **Validation:** `! test -f docs/stories/camping/style.md`;
  `grep -rl "style.md" docs/stories/camping/` returns nothing;
  `grep -l "prompts.md" docs/stories/*/story.md | wc -l` returns `4`.
- **Depends on:** T2
- [ ] done
- Notes:

### T4: Recover the GPOM Short assets from git   [Status: pending | Model: sonnet]
- **Scope:** The retired GPOM Short's per-panel prompt records and a Carrier
  character sheet exist only in git history at commit `7dd36c7^` under
  `docs/stories/gpom-short/`. Recover them: restore
  `characters/img/carrier.jpg` to
  `docs/stories/gitpush-origin-master/characters/img/carrier-sheet.jpg`, and
  append the 16 panel prompts (`storyboard/p01.md`…`p16.md`) to GPOM's
  `prompts.md` as an `## Appendix — GPOM Short panel prompts (retired comic,
  style reference)` section. These are the highest-quality worked examples of
  the near-black register in the repo and are the raw material for T7.
- **Files:** create
  `docs/stories/gitpush-origin-master/characters/img/carrier-sheet.jpg`;
  modify `docs/stories/gitpush-origin-master/prompts.md`,
  `docs/stories/gitpush-origin-master/characters/the-carrier.md` (set `sheet:`).
- **Acceptance criteria:** the carrier image exists and is a valid JPEG; the
  appendix contains 16 prompt blockquotes; `the-carrier.md` frontmatter
  `sheet:` points at the recovered file.
- **TDD:** no (asset recovery)
- **Validation:** `git show 7dd36c7^ --stat | head` confirms the source commit;
  `file docs/stories/gitpush-origin-master/characters/img/carrier-sheet.jpg`
  reports JPEG image data; `grep -c "^> " docs/stories/gitpush-origin-master/prompts.md`
  is at least `16`.
- **Depends on:** T2
- [ ] done
- Notes:

### T5: Canon hygiene   [Status: pending | Model: sonnet]
- **Scope:** Mark `docs/stories/magic-money-tree/characters/dawn.md` deprecated
  — add a `> **DEPRECATED 2026-08-08.**` banner at the top explaining that the
  2026-08-05/06 re-founding replaced the Dawn spine with Keynes and the tree
  (`story.md:12-17`), change `role:` so it no longer claims `protagonist`, and
  note the v1 comic and its 10 panel records still reflect this superseded
  spine. Do not delete the file. Also add a one-line note to
  `docs/stories/magic-money-tree/storyboard/v1-comic-plan.md` pointing at the
  same fact if not already present.
- **Files:** modify `docs/stories/magic-money-tree/characters/dawn.md`,
  `docs/stories/magic-money-tree/storyboard/v1-comic-plan.md`.
- **Acceptance criteria:** `dawn.md` carries the banner and no longer declares
  `role: protagonist`; `keynes.md` is the only MMT character with that role.
- **TDD:** no (docs)
- **Validation:** `grep -c "DEPRECATED" docs/stories/magic-money-tree/characters/dawn.md`
  returns at least `1`;
  `grep -l "role: protagonist" docs/stories/magic-money-tree/characters/*.md`
  lists only `keynes.md`.
- **Depends on:** —
- [ ] done
- Notes:

---
**GATE — Phase 1 begins. Tickets T6–T10 are authored WITH Kai, in conversation.
An executor must not invent this copy unattended.**
---

### T6: Style prompts — Camping and Karen   [Status: pending | Model: opus]
- **Scope:** Author §1 of the Camping and Karen ledgers. Camping's derives from
  the absorbed `style.md` material (matched city pair, the wet car park, warmth
  permitted in exactly three named places, 35mm documentary). Karen's is written
  fresh from `docs/stories/karen/story.md` — the Midtown phone box across nine
  months of weather, the blazer-and-lanyard archetype, New York exteriors — and
  must be reconciled against whatever Karen imagery already exists in Flow
  (surfaced by T11 if this ticket runs after it; otherwise flag for revision).
  Each style prompt is one paragraph, prependable verbatim, and names a palette
  and a film stock but never a specific shot.
- **Files:** modify `docs/stories/{camping,karen}/prompts.md`.
- **Acceptance criteria:** both §1 sections contain a single blockquoted
  paragraph; neither restates Layer 0 material already in the
  `badcode-art-direction` skill; neither names a specific scene.
- **TDD:** no (copy)
- **Validation:** `grep -A3 "## 1. Style prompt" docs/stories/camping/prompts.md`
  shows a non-`TBD` blockquote; same for `karen`.
- **Depends on:** T3
- [ ] done
- Notes:

### T7: Style prompts — GPOM and Magic Money Tree   [Status: pending | Model: opus]
- **Scope:** Author §1 for the two stories with no established look. GPOM's is
  the near-black monumental register, using the T4 appendix and
  `docs/images/register-anchor.md` as worked examples. MMT's is the St James's
  Park register — low winter daylight, documentary-historical, the bench and the
  young lime as recurring geometry across decades. Discuss both with Kai before
  writing.
- **Files:** modify `docs/stories/{gitpush-origin-master,magic-money-tree}/prompts.md`.
- **Acceptance criteria:** as T6.
- **TDD:** no (copy)
- **Validation:** `grep -A3 "## 1. Style prompt" docs/stories/gitpush-origin-master/prompts.md`
  shows a non-`TBD` blockquote; same for `magic-money-tree`.
- **Depends on:** T4
- [ ] done
- Notes:

### T8: Visual blocks for the uncast roster   [Status: pending | Model: opus]
- **Scope:** Four character files have no `## Visual` section at all and cannot
  be prompted from: `karen/characters/karen.md`, `karen/characters/ari.md`,
  `magic-money-tree/characters/keynes.md`,
  `magic-money-tree/characters/the-tree.md`. Write one for each, following the
  structure already proven in `camping/characters/tarquin.md` — a locked list of
  physical invariants ("lock these") specific enough that two independent
  generations read as the same subject. Keynes must be historically *inspired*,
  not a likeness (see the lint: likeness phrasing is a block trigger) — describe
  build, era dress and bearing, never "looks like John Maynard Keynes". The tree
  is an unremarkable young European lime, 28 years old in 1942: **no glow, no
  face**, presence carried by framing, wind and light.
- **Files:** modify `docs/stories/karen/characters/{karen,ari}.md`,
  `docs/stories/magic-money-tree/characters/{keynes,the-tree}.md`.
- **Acceptance criteria:** all four files contain a `## Visual` section; none
  contains the name of a real living or historical person as a likeness target;
  `the-tree.md`'s block explicitly forbids glow and face.
- **TDD:** no (copy)
- **Validation:** `grep -l "## Visual" docs/stories/karen/characters/*.md docs/stories/magic-money-tree/characters/*.md | wc -l`
  returns `5` (the four above plus MMT's existing `dawn.md`).
- **Depends on:** T5, T6, T7
- [ ] done
- Notes:

### T9: Character sheet prompts   [Status: pending | Model: opus]
- **Scope:** Write a Layer-2 prompt in each ledger's §3 for every character
  needing a sheet: Karen, Ari, Keynes, the tree, the tent, the wank tank, the
  Hundred. Each produces a **multi-angle turnaround on a neutral background**,
  matching the format of the existing `tarquin-sheet.jpg` (four full-body
  angles above three head angles). Object refs (tent, wank tank, tree) get a
  multi-angle object sheet in situ-neutral lighting instead of a portrait grid.
  The Carrier already has a recovered sheet from T4 and needs a prompt only if
  T11 shows it must be regenerated.
- **Files:** modify all four `docs/stories/*/prompts.md`.
- **Acceptance criteria:** each of the seven characters has a §3 entry with a
  prompt, a named light source, a `Cast:` line (usually `—` for a sheet) and an
  unfilled `Lint:` line; each entry names its intended `outPath`.
- **TDD:** no (copy)
- **Validation:** `grep -c "^### " docs/stories/karen/prompts.md` returns at
  least `2`; every `outPath` named resolves to a path under
  `docs/stories/*/characters/img/`.
- **Depends on:** T8
- [ ] done
- Notes:

### T10: The four cover prompts, and the lint pass   [Status: pending | Model: opus]
- **Scope:** Write the Layer-2 cover prompt for each story per the **Architecture
  → The four covers** table, each naming its single motivated light source,
  holding its subject small in a large frame, and baking in no text. GPOM's is
  the orbital server hall with Earth at roughly a quarter of the frame lit by
  earthlight — include the deliberate-departure note so no one later "corrects"
  it toward LEO. Then run the lint over **every** prompt written in T6–T10:
  check each against the four triggers in
  `.claude/skills/badcode-art-direction/SKILL.md`, rewrite any that trip one
  using that skill's Instead-of/Write table, and stamp each asset's `Lint:` line
  with the date and the four checks.
- **Files:** modify all four `docs/stories/*/prompts.md`.
- **Acceptance criteria:** four `### cover` entries exist, one per ledger, each
  naming a light source and an `outPath` under `docs/images/covers/`; every §3
  entry across all four ledgers has a stamped `Lint: ✅` line; no prompt anywhere
  contains a real brand name, a legible wordmark, or likeness phrasing.
- **TDD:** no (copy)
- **Validation:** `grep -c "### cover" docs/stories/*/prompts.md` returns `1`
  per file; `grep -L "Lint: ✅" docs/stories/*/prompts.md` returns nothing;
  `grep -riE "waitrose|natwest|bmw|claude" docs/stories/*/prompts.md` returns
  nothing inside a blockquoted prompt (these appear in canon prose but must be
  paraphrased in prompts).
- **Depends on:** T9
- [ ] done
- Notes:

---
**GATE — Kai approves every prompt on paper before Phase 2. No credits are
spent before this gate clears.**
---

### T11: Flow reconciliation   [Status: pending | Model: opus]
- **Scope:** Establish ground truth in Flow before generating anything, and
  write it down. Bring the browser up (`./scripts/flow-chrome.sh`, then poll
  `curl -s http://localhost:9222/json/version`, then `flow_status()`). Then
  determine and record: (a) which projects exist and their IDs; (b) whether the
  Camping project `camping-v2` (`9b729074-da88-4668-a442-458e9a0f15ac`) and its
  two Flow Characters (`29e97ae3-…` Tarquin, `7566666e-…` Bob) are still
  reachable from this account; (c) what Karen-story imagery already exists in
  Flow that the repo has no record of, and whether any of it is already a Flow
  Character; (d) **whether Flow Characters are now account-global rather than
  project-scoped**, given the home page advertises casting them "anywhere" — this
  contradicts `packages/flow-mcp/README.md` and
  `.claude/skills/badcode-art-direction/SKILL.md`; (e) that the image aspect tab
  reads `16:9`. Write findings to `docs/stories/FLOW-STATE.md` and update each
  ledger's `flow_project_id` and cast-table statuses.
  **Never delete or overwrite an existing Flow character or project.**
- **Files:** create `docs/stories/FLOW-STATE.md`; modify all four
  `docs/stories/*/prompts.md`.
- **Acceptance criteria:** every project in the account is listed with its ID
  and best-guess story; each of the five questions (a)–(e) has an explicit
  written answer; no cast row anywhere still reads `needs-reconcile`; if (d)
  proves characters are global, `FLOW-STATE.md` says so and flags the two docs
  that need correcting.
- **TDD:** no (investigation)
- **Validation:** `test -f docs/stories/FLOW-STATE.md`;
  `grep -c "needs-reconcile" docs/stories/*/prompts.md` returns `0` across all
  files; `flow_status()` returns `loggedIn: true`.
- **Depends on:** T10
- [ ] done
- Notes:

### T12: Adopt or create the four Flow projects   [Status: pending | Model: sonnet]
- **Scope:** Ensure one Flow project per story exists, named exactly
  `badcode-<story-id>`. Adopt an existing project where T11 identified one for
  that story rather than creating a duplicate — note that project **rename is
  not automatable** (`docs/superpowers/flow-selectors.md`, open issues), so if an
  existing project has the wrong name, record the real name in the ledger's
  `flow_project` field rather than trying to rename it. `flow_open_project`
  matches exact names only. Record final names and IDs in every ledger.
- **Files:** modify all four `docs/stories/*/prompts.md`; modify
  `docs/stories/FLOW-STATE.md`.
- **Acceptance criteria:** `flow_open_project({ name })` succeeds for the
  `flow_project` value recorded in each of the four ledgers; no existing project
  was deleted.
- **TDD:** no (config)
- **Validation:** four successful `flow_open_project` calls, one per recorded
  name, each returning `projectOpen: true`.
- **Depends on:** T11
- [ ] done
- Notes:

### T13: Character sheets — Camping objects   [Status: pending | Model: sonnet]
- **Scope:** Generate multi-angle object sheets for the tent and the wank tank
  from their T9 prompts, at `numOutputs: 2`, into
  `docs/stories/camping/characters/img/{tent,wank-tank}-sheet.jpg`. Write the
  Flow media id and a v1 revision line back into the ledger, and fill `sheet:`
  in each character file. **The wank tank prompt must not name a real
  manufacturer or show a legible badge** — a brand name is a block trigger; if
  two calls return no candidates, rewrite per the skill's table, do not retry.
- **Files:** create the two sheet images; modify
  `docs/stories/camping/characters/{tent,wank-tank}.md`,
  `docs/stories/camping/prompts.md`.
- **Acceptance criteria:** both images exist and are valid JPEGs; both character
  files have non-empty `sheet:`; both ledger entries carry a media id and a v1
  revision line.
- **TDD:** no (generation)
- **Validation:** `file docs/stories/camping/characters/img/{tent,wank-tank}-sheet.jpg`
  reports JPEG for both; `grep -c 'sheet: ""' docs/stories/camping/characters/*.md`
  returns `0`.
- **Depends on:** T12
- [ ] done
- Notes:

### T14: Character sheets — Karen and Ari   [Status: pending | Model: sonnet]
- **Scope:** As T13, for Karen and Ari, into
  `docs/stories/karen/characters/img/{karen,ari}-sheet.jpg`. If T11 found
  existing Karen or Ari imagery in Flow, **use it as the reference** via
  `flow_edit_image` (exactly one reference, downscaled with
  `convert <src> -resize 1600x1600\> -quality 88 <tmp>.jpg`) rather than
  generating a new face from scratch — Jack's existing work is the anchor, not a
  competitor. Then cast each as a Flow Character with `flow_create_character`
  and record the returned identity in the ledger cast table with status `cast`.
- **Files:** create the two sheet images; modify
  `docs/stories/karen/characters/{karen,ari}.md`, `docs/stories/karen/prompts.md`.
- **Acceptance criteria:** both images exist; both are cast as Flow Characters;
  the ledger cast table shows `cast` for both with their IDs; no pre-existing
  Flow character was overwritten.
- **TDD:** no (generation)
- **Validation:** `file docs/stories/karen/characters/img/{karen,ari}-sheet.jpg`
  reports JPEG for both; `grep -c "not-cast" docs/stories/karen/prompts.md`
  returns `0` for Karen and Ari rows.
- **Depends on:** T12
- [ ] done
- Notes:

### T15: Character sheets — Keynes and the tree   [Status: pending | Model: sonnet]
- **Scope:** As T14, for Keynes and the tree, into
  `docs/stories/magic-money-tree/characters/img/{keynes,the-tree}-sheet.jpg`.
  Keynes is cast as a Flow Character. The tree is an object sheet — multi-angle,
  no glow, no face — and is **not** cast as a Character (it has no face to bind);
  record it `none-by-design` with a note that it is referenced by sheet image
  instead.
- **Files:** create the two sheet images; modify
  `docs/stories/magic-money-tree/characters/{keynes,the-tree}.md`,
  `docs/stories/magic-money-tree/prompts.md`.
- **Acceptance criteria:** both images exist; Keynes is `cast` with an ID; the
  tree row reads `none-by-design`; no image shows a glowing or anthropomorphised
  tree.
- **TDD:** no (generation)
- **Validation:** `file docs/stories/magic-money-tree/characters/img/{keynes,the-tree}-sheet.jpg`
  reports JPEG for both.
- **Depends on:** T12
- [ ] done
- Notes:

### T16: Character sheets — the Carrier and the Hundred   [Status: pending | Model: sonnet]
- **Scope:** The Carrier's sheet was recovered in T4; cast it as a Flow
  Character from that image and record the ID. Generate a sheet for the Hundred
  — a **collective**, so this is a wardrobe-and-texture reference plate (hand-darned
  wool in slightly-wrong colours, mechanical tools, paper, candle-and-battery
  light), not a portrait grid, and it is not cast as a Character.
- **Files:** create
  `docs/stories/gitpush-origin-master/characters/img/the-hundred-sheet.jpg`;
  modify `docs/stories/gitpush-origin-master/characters/{the-carrier,the-hundred}.md`,
  `docs/stories/gitpush-origin-master/prompts.md`.
- **Acceptance criteria:** the Carrier is `cast` with an ID sourced from the
  recovered sheet; the Hundred's plate exists; the AI's row still reads
  `none-by-design` and no image of it was generated.
- **TDD:** no (generation)
- **Validation:** `file docs/stories/gitpush-origin-master/characters/img/the-hundred-sheet.jpg`
  reports JPEG; `grep -A2 "@TheAI\|the-ai" docs/stories/gitpush-origin-master/prompts.md`
  shows `none-by-design`.
- **Depends on:** T12
- [ ] done
- Notes:

### T17: Assemble the contact sheet   [Status: pending | Model: sonnet]
- **Scope:** Write `docs/stories/CONTACT-SHEET.md` — one page embedding every
  character sheet produced in T13–T16 plus the two pre-existing Camping sheets,
  each with its story, its tag, its Flow Character status and a one-line
  reminder of the canon invariants it was meant to hit, so Kai can review the
  whole cast in a single pass and mark each accept/reject inline.
- **Files:** create `docs/stories/CONTACT-SHEET.md`.
- **Acceptance criteria:** every generated sheet appears exactly once; each
  entry has an empty `- [ ] accepted` checkbox; every image path in the file
  resolves to a file that exists.
- **TDD:** no (docs)
- **Validation:** every `](` path in the file passes `test -f`;
  `grep -c "accepted" docs/stories/CONTACT-SHEET.md` equals the number of sheets.
- **Depends on:** T13, T14, T15, T16
- [ ] done
- Notes:

---
**GATE — Kai reviews the contact sheet in one pass and marks rejections.**
---

### T18: Character correction pass   [Status: pending | Model: sonnet]
- **Scope:** For every sheet Kai marked rejected in `CONTACT-SHEET.md`, run one
  correction round with `flow_edit_image`: **always reference the accepted
  golden original**, exactly one reference image, downscaled, `numOutputs: 2`,
  using the delta-prompt shape from `.claude/skills/edit-panel/SKILL.md` (style
  anchor line + Google's verbatim edit template + all changes batched into one
  round). Update the sheet, re-cast the Flow Character if the face changed, and
  append a revision line to the ledger. If a sheet needs more than three chained
  rounds, stop and do a lock-and-rebuild — merge the deltas into one full prompt,
  regenerate clean, and rewrite the ledger's main prompt.
- **Files:** modify the rejected sheet images and their ledgers;
  modify `docs/stories/CONTACT-SHEET.md`.
- **Acceptance criteria:** every checkbox in `CONTACT-SHEET.md` is ticked; every
  corrected sheet has a new revision line naming the exact delta prompt; no
  rejected candidate files (`-a`/`-b` suffixes) remain on disk.
- **TDD:** no (generation)
- **Validation:** `grep -c "\- \[ \] accepted" docs/stories/CONTACT-SHEET.md`
  returns `0`; `find docs/stories -name "*-[ab].jpg" | wc -l` returns `0`.
- **Depends on:** T17
- [ ] done
- Notes:

### T19: Generate the four covers   [Status: pending | Model: opus]
- **Scope:** Generate each cover from its T10 ledger prompt, composed as
  §1 + §3, with the story's approved cast attached via the `character`
  parameter, `numOutputs: 2`, into `docs/images/covers/<story-id>.jpg`. Judge
  each against the three grammar rules — single motivated light source, deep
  unlifted blacks, subject held small in a large frame — and against the others
  as a set: the four must be distinguishable at thumb size while reading as one
  series. Refine with `flow_refine` where a candidate is close. Confirm every
  output is 16:9 and contains no baked-in text.
- **Files:** create `docs/images/covers/{gitpush-origin-master,camping,karen,magic-money-tree}.jpg`.
- **Acceptance criteria:** four JPEGs exist, all 16:9; none contains legible
  text; GPOM's shows Earth as a whole disc at roughly a quarter of the frame,
  lit as the scene's only light source; no cover is a near-duplicate of
  `docs/images/register-anchor.jpg`.
- **TDD:** no (generation)
- **Validation:** `identify -format "%f %wx%h\n" docs/images/covers/*.jpg` lists
  four files, each with a width:height ratio of 16:9; manual visual check of all
  four side by side.
- **Depends on:** T18
- [ ] done
- Notes:

### T20: Cover records, index and frontmatter   [Status: pending | Model: sonnet]
- **Scope:** Write a sibling `.md` record for each cover following
  `docs/images/register-anchor.md` exactly (frontmatter `image`,
  `flow_media_id`, `model`, `status`, `used_by`, then the exact prompt as a
  blockquote and a revisions log). Add four index rows to
  `docs/images/README.md`. Copy each cover to `apps/web/public/covers/` and add
  `cover: /covers/<story-id>.jpg` to each story's `story.md` frontmatter.
- **Files:** create `docs/images/covers/*.md` (× 4),
  `apps/web/public/covers/*.jpg` (× 4); modify `docs/images/README.md`,
  `docs/stories/*/story.md` (× 4).
- **Acceptance criteria:** four records exist with non-empty `flow_media_id`;
  `docs/images/README.md` has a row per cover; all four `story.md` files carry a
  `cover:` key whose path resolves under `apps/web/public/`.
- **TDD:** no (docs/wiring)
- **Validation:** `ls docs/images/covers/*.md | wc -l` returns `4`;
  `grep -c "^cover:" docs/stories/*/story.md` returns `1` per file;
  for each `cover:` value, `test -f apps/web/public/<value>` passes.
- **Depends on:** T19
- [ ] done
- Notes:

### T21: Sean AI as SVG   [Status: pending | Model: sonnet]
- **Scope:** Build Sean AI's identity as vector art in-repo, not through Flow: an
  8-bit pixel-art moniker plus a `Sean AI` wordmark, and a gold variant for the
  §4.3 government takeover. A legible wordmark is one of the four reliable Flow
  block triggers and this is a vector job regardless. Keep it a **parody
  register** — it must not reproduce any real product's mark. Record the
  decision and both file paths in `docs/stories/karen/prompts.md` under a
  `## 4. Non-Flow assets` section.
- **Files:** create `apps/web/src/assets/sean-ai.svg`,
  `apps/web/src/assets/sean-ai-gold.svg`; modify
  `docs/stories/karen/characters/sean-ai.md`, `docs/stories/karen/prompts.md`.
- **Acceptance criteria:** both SVGs exist and render standalone; neither
  reproduces a real product mark; `sean-ai.md`'s `sheet:` line points at the SVG
  and still explains he is a UI, not a face.
- **TDD:** no (asset)
- **Validation:** `xmllint --noout apps/web/src/assets/sean-ai*.svg` exits `0`;
  `grep -c "Non-Flow assets" docs/stories/karen/prompts.md` returns `1`.
- **Depends on:** T3
- [ ] done
- Notes:

### T22: Delta note to the website-reset plan   [Status: pending | Model: sonnet]
- **Scope:** Append a short, clearly-headed `## Delta — story covers
  (2026-08-08)` section to
  `design/2026-08-07-badcode-website-reset.md` asking it to: (a) add
  `cover: string` to `StoryRecord` in its T1 schema and make the Ledger row's
  16:9 thumb and the T15 OG chain prefer it over `film.poster`; (b) **restrict
  the catalogue to the four EP stories** — Galileo, Storyverse and Future Proof
  stay file-ready but unlinked from the home page, per Kai's 2026-08-08 ruling;
  (c) note that the covers now exist at `apps/web/public/covers/`. Do not edit
  that plan's existing tickets or change its status.
- **Files:** modify `design/2026-08-07-badcode-website-reset.md`.
- **Acceptance criteria:** the delta section exists with all three points; no
  existing ticket text, checkbox or status in that file was altered.
- **TDD:** no (docs)
- **Validation:** `git diff --stat design/2026-08-07-badcode-website-reset.md`
  shows additions only, zero deletions.
- **Depends on:** T20
- [ ] done
- Notes:

### T23: Repo map and memory   [Status: pending | Model: sonnet]
- **Scope:** Add the prompt ledger to `CLAUDE.md`'s repo map and its
  "How to work in this repo" list, so future sessions find it without being
  told: one table row for `docs/stories/<story>/prompts.md` and a bullet
  explaining the four-layer model and that Layer 0 lives in the
  `badcode-art-direction` skill. Reference `docs/stories/PROMPT-LEDGER.md` as
  the format spec.
- **Files:** modify `CLAUDE.md`.
- **Acceptance criteria:** `CLAUDE.md` names `prompts.md` and
  `PROMPT-LEDGER.md`; the four-layer model is stated in one or two sentences.
- **TDD:** no (docs)
- **Validation:** `grep -c "prompts.md" CLAUDE.md` returns at least `1`.
- **Depends on:** T22
- [ ] done
- Notes:

### T24: End-to-end verification   [Status: pending | Model: opus]
- **Scope:** Prove the whole thing holds together. Confirm every ledger is
  complete and internally consistent (every cast row has a status; every §3
  asset has a prompt, a lint stamp and a media id; every `outPath` named
  resolves to a file that exists). Confirm the four covers sit side by side as a
  coherent series and are individually legible at thumb size — view them
  downscaled to catalogue-thumb width, not full size. Confirm the repo builds.
  Then re-run the "cold start" test: open only
  `docs/stories/karen/prompts.md` and verify it alone tells you the style, the
  cast, the Flow project and every prompt for that story.
- **Files:** none (verification only; log findings in the Discovered Issues Log).
- **Acceptance criteria:** all of the above hold; any failure is logged rather
  than silently fixed.
- **TDD:** no (verification)
- **Validation:** `npm run typecheck` clean; `npm run build` succeeds;
  `ls docs/images/covers/*.jpg | wc -l` returns `4`;
  `grep -L "Lint: ✅" docs/stories/*/prompts.md` returns nothing;
  `find docs/stories -name "*-[ab].jpg" | wc -l` returns `0`.
- **Depends on:** T23
- [ ] done
- Notes:

---

## Discovered Issues Log

_(appended by executors during implementation)_
