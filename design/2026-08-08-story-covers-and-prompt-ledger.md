# Story Covers & the Prompt Ledger — Design & Implementation Plan

> **EXECUTION RULES (for agents):** Work ONE ticket at a time, in order unless
> dependencies say otherwise. Only the orchestrator changes ticket Status;
> workers may only append to Notes and the Discovered Issues Log. A ticket's
> checkbox is checked only after its Validation commands have been re-run by
> the orchestrator and pass. Do not expand scope; log surprises in the
> Discovered Issues Log instead.

Status: proposed
Relates: [`design/2026-08-07-badcode-website-reset.md`](./2026-08-07-badcode-website-reset.md)
(consumes the covers this plan produces; see the delta note in T22)

---

## ⚠ SCOPE REVISION — 2026-08-08 (Kai). This overrides the tickets below.

**Camping and Karen are out of the image pipeline.** Their visuals are Jack's,
developed by hand in Flow outside this repo. We do not generate their character
sheets, panels or covers, and we do not attempt to reconstruct or replicate what
he has already made. Their **written canon remains ours and authoritative** —
only the image pipeline moved. Both story READMEs now carry a banner saying so.

**The image pipeline is now two stories: GitPush Origin Master (BC-000) and The
Magic Money Tree (BC-003).** These are the ones we grow into full prompt ledgers
ready to drive Flow.

Applied to the tickets below:

| Was | Now |
| --- | --- |
| Four prompt ledgers | **Two** — GPOM and MMT, both already hand-seeded with a cover prompt on 2026-08-08 |
| Four covers | **Two.** Camping's and Karen's covers come from Jack |
| Full roster, four stories | **GPOM + MMT only:** Keynes, the tree, the Carrier, the Hundred |
| T6, T13, T14, T21 | **Cancelled** — see each ticket |
| T3's `camping/style.md` absorption | **Cancelled.** Leave Camping's folder alone |
| "four" in any count | Read as **two** (T2, T10, T17, T19, T20, T24) |

The catalogue is still four rows — this only changes who produces the imagery.

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
`packages/cli/src/resolve-panel.ts:38-49` maps `camping`, `karen` and
`gpom-short` all to `null` because no per-panel records exist. The one story
that *does* have records — Magic Money Tree, 10 panels at
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

**None of them matches anything Camping's canon records.** Camping cites *three*
different project UUIDs, and they mean different things — do not conflate them:

| UUID | What it is | Cited at |
| --- | --- | --- |
| `9b729074-da88-4668-a442-458e9a0f15ac` | project `camping-v2` — holds the **Flow Characters** `29e97ae3-…` (Tarquin) and `7566666e-…` (Bob) | `tarquin.md:64-65`, `bob.md:58-59` |
| `8970bef9-0c6d-47f7-9aa0-8e4ad462eda8` | the project the **Tarquin sheet image** was harvested from (media `3bfdc65f-…`) | `tarquin.md:6-8` |
| `b5d76bd1-c989-4040-bc8c-8649cf77ca93` | the project the **Bob sheet image** was harvested from (media `cdabced2-…`) | `bob.md:6-8` |

Two of the three surviving project thumbnails appeared to show Karen-story
characters (a man in headphones reading as Ari; a woman reading as Karen) —
meaning **work exists in Flow that the repo has no record of**, and **records
exist in the repo that Flow may no longer back.**

Separately, Flow's home page now advertises *"Create characters and cast them
anywhere. Define their look, voice, and personality once. Reference them
anywhere with a simple @tag."* This **contradicts** the project-scoped character
rule at `.claude/skills/badcode-art-direction/SKILL.md:67` ("`@Tarquin` lives in
`camping-v2`"). It may mean characters are now account-global.

Neither of these is assumed anywhere in this plan. **T11a** establishes the truth
read-only before any prompt is finalised; **T11b** writes it into the ledgers.

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
          camping: wet supermarket-car-park grey; warmth only in three named places
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
     prompt:    <the stored, pre-composed prompt — paste-ready, see note below>,
     character: "Tarquin",           // one per call; omit when the asset has no cast
     outPath:   "<ABSOLUTE path>",   // ledgers record repo-relative; the caller
     numOutputs: 2                   // absolutises at call time (server.ts:92)
   })
```

**Reversed 2026-08-08 — prompts are stored PRE-COMPOSED, not concatenated.**
This plan originally rejected "a single fully-composed prompt string per asset"
because a style change would mean hand-editing every prompt. Writing the two real
ledgers reversed it, for one reason that outweighs the DRY argument: **the
dominant use is a human copying a block into a browser.** A prompt you have to
assemble from two places before pasting is a prompt that gets pasted wrong.

So: every stored prompt is self-contained and paste-ready, and **Layer 1 is the
specification a prompt author composes from**, not a runtime concatenation.
Layers 0–3 still describe how a prompt is *built*; they no longer describe how it
is *stored*. The cost is real and is stated at the top of each ledger — a Layer 1
change is now expensive, so settle the style before writing many assets.

Layer 3 is unaffected: cast is still attached via the `character` parameter and
is never folded into the prompt text.

### Candidate files — the naming trap

`packages/flow-mcp/src/candidates.ts:6-13`: when `numOutputs > 1`, the tool
writes `<name>-a.jpg`, `<name>-b.jpg` … and **never writes `<name>.jpg`.**
Every generation ticket in this plan therefore ends with an explicit
**pick-and-promote** step: choose the winner, `mv <name>-<x>.jpg <name>.jpg`,
delete the losers. Nothing downstream will find its input otherwise.

### Where the memory lives

**Rejected alternative:** prompts inside `story.md`, as originally requested.
`gitpush-origin-master/story.md` is already 715 lines and MMT's is 499, so a
ledger inside them is a bad page to navigate and mixes the *why* with the *how*.
A sibling file linked from the top of `story.md` gets the same one-page
readability with a clean separation. Secondary: the website reset renders a
story's `story.md` prose to `readHtml` at build time whenever the story has no
`film` block (`design/2026-08-07-badcode-website-reset.md:319-324`), so prompts
in `story.md` would leak onto the public site for any story that ever renders as
a read variant. (These four are expected to gain `film` blocks eventually — see
that plan's T5 at `:452-462` — so treat this as the lesser argument.)

```
docs/stories/<story>/
├── story.md          canon prose — the WHY        → published to the website
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

Subjects are stated here in the **paraphrase register** the lint requires — no
real brand names, no real model designations, no legible badges. The canon prose
names them; the prompts must not.

| Story | Subject | The single light source |
| --- | --- | --- |
| **GPOM** (BC-000) | An orbital server hall. Terrestrial-looking rack rows recede down an aisle that opens onto space; **Earth sits in that opening at roughly a quarter of the frame** — whole disc, not a dot. The racks give scale. How the AI sees us. | **Earthlight** down the aisle |
| **Camping** (BC-001) | A wet upmarket-supermarket car park: a sagging faded green-grey dome tent against a low wall and trolley bay, an oversized blacked-out luxury SUV (no legible badge) straddling two bays beside it. The size contrast is the class map. | Flat overcast daylight |
| **Karen** (BC-002) | One Midtown phone box, small in a large frame of city, with the beginnings of a crowd. | Street/phone-box practical |
| **MMT** (BC-003) | A London park bench under an unremarkable young lime. No glow, no face — presence carried by framing, wind and light. | Low winter daylight |

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
`packages/flow-mcp/README.md:89-90` lists the absence of a `POLICY_BLOCKED` code
as a known gap: a block is indistinguishable from a timeout. Mitigation is a
**Phase-1 authoring-time lint**, applied to every prompt on paper before any
credits burn, against the four documented triggers at
`.claude/skills/badcode-art-direction/SKILL.md:92-102`:

1. Real brand names or legible wordmarks
2. Likeness phrasing ("looks like <real person>")
3. Stacked destitution
4. Legible text attributed to real institutions

The Instead-of/Write rewrite table is at that file's `:106`.

**Diagnosis rule at generation time:** two no-candidate failures on a healthy
session = a policy block. **Rewrite, never retry.**

### Sequencing

```
PHASE 0  FOUNDATIONS          T1–T5, T11a   no generation; T11a is a read-only Flow survey
PHASE 1  PROMPTS              T6–T10        authored with Kai; still no generation
              ▼ ── GATE: Kai approves every prompt on paper
PHASE 2  CHARACTERS           T11b–T17      unattended
              ▼ ── GATE: Kai reviews ONE contact sheet
PHASE 3  FEEDBACK             T18           one correction pass
              ▼
PHASE 4  COVERS               T19–T24       unattended, on approved cast
```

T11a sits in Phase 0 deliberately: the Karen style prompt (T6) cannot be written
honestly without knowing what Karen imagery already exists in Flow.

---

## File Structure

**Create**

| Path | Purpose |
| --- | --- |
| `docs/stories/PROMPT-LEDGER.md` | The format spec both humans and agents read |
| `docs/stories/FLOW-STATE.md` | Ground truth about the Flow account (T11a) |
| `docs/stories/CONTACT-SHEET.md` | Phase-3 review page |
| `docs/stories/gitpush-origin-master/prompts.md` | GPOM prompt ledger |
| `docs/stories/camping/prompts.md` | Camping prompt ledger |
| `docs/stories/karen/prompts.md` | Karen prompt ledger |
| `docs/stories/magic-money-tree/prompts.md` | MMT prompt ledger |
| `docs/stories/karen/characters/img/karen-sheet.jpg` | Karen turnaround |
| `docs/stories/karen/characters/img/ari-sheet.jpg` | Ari turnaround |
| `docs/stories/magic-money-tree/characters/img/keynes-sheet.jpg` | Keynes turnaround |
| `docs/stories/magic-money-tree/characters/img/the-tree-sheet.jpg` | The lime, multi-angle |
| `docs/stories/camping/characters/img/tent-sheet.jpg` | The tent, multi-angle |
| `docs/stories/camping/characters/img/wank-tank-sheet.jpg` | The SUV, multi-angle |
| `docs/stories/gitpush-origin-master/characters/img/carrier-sheet.jpg` | Recovered from git |
| `docs/stories/gitpush-origin-master/characters/img/the-hundred-sheet.jpg` | Wardrobe/texture plate |
| `docs/images/covers/{gitpush-origin-master,camping,karen,magic-money-tree}.jpg` | The four covers |
| `docs/images/covers/{…}.md` | Four cover records |
| `apps/web/public/covers/*.jpg` | Servable copies |
| `apps/web/public/brand/sean-ai.svg` | Sean AI moniker, vector |
| `apps/web/public/brand/sean-ai-gold.svg` | Gold takeover variant |

**Modify**

| Path | Change |
| --- | --- |
| `docs/stories/*/story.md` (× 4) | Add ledger link at top; add `cover:` frontmatter |
| `docs/stories/camping/README.md` | Drop the `style.md` reference |
| `docs/stories/karen/characters/{karen,ari}.md` | Add `## Visual`; fill `sheet:` |
| `docs/stories/karen/characters/sean-ai.md` | Point `sheet:` at the SVGs |
| `docs/stories/magic-money-tree/characters/{keynes,the-tree}.md` | Add `## Visual`; fill `sheet:` |
| `docs/stories/magic-money-tree/characters/dawn.md` | Mark deprecated |
| `docs/stories/magic-money-tree/storyboard/v1-comic-plan.md` | Verify deprecation banner only |
| `docs/stories/camping/characters/{tent,wank-tank}.md` | Fill `sheet:` |
| `docs/stories/gitpush-origin-master/characters/{the-carrier,the-hundred}.md` | Fill `sheet:` |
| `docs/images/README.md` | Index rows for the four covers |
| `design/2026-08-07-badcode-website-reset.md` | Append the delta note (T22) |
| `CLAUDE.md` | Repo map: the prompt ledger |

**Delete**

| Path | Why |
| --- | --- |
| `docs/stories/camping/style.md` | Absorbed into `camping/prompts.md` §1 |

---

## Interfaces

### The prompt ledger — `docs/stories/<story>/prompts.md`

The status legend lives **only** in `PROMPT-LEDGER.md`, never in a per-story
file — it would otherwise pollute every `grep` over the cast tables.

```markdown
---
story: camping                  # must equal the folder name
flow_project: badcode-camping   # EXACT Flow project name; flow_open_project
                                # matches exact names only and rename is not
                                # automatable (flow-selectors.md:226)
flow_project_id: <uuid>         # filled by T11b
updated: 2026-08-08
---

# Camping — prompt ledger

Read `.claude/skills/badcode-art-direction/SKILL.md` first (Layer 0).

## 1. Style prompt
Prepended verbatim to every asset prompt in §3.

> <the style prompt text>

## 2. Cast

| Tag | Character file | Sheet | Flow Character id | Status |
| --- | --- | --- | --- | --- |
| @Tarquin | characters/tarquin.md | characters/img/tarquin-sheet.jpg | 29e97ae3-… | needs-reconcile |
| @Bob | characters/bob.md | characters/img/bob-sheet.jpg | 7566666e-… | needs-reconcile |
| @Tent | characters/tent.md | — | — | not-cast |

## 3. Assets

### cover → `docs/images/covers/camping.jpg`

**Metadata — none of this is pasted into Flow.**
- **Cast:** @Tarquin, @Bob
- **Light source:** flat overcast daylight
- **Lint:** ✅ 2026-08-08 — no wordmarks · no likeness · no stacked destitution · no institutional text
- **Flow media id:** <uuid>
- **Revisions:**
  - v1 (2026-08-08) — …

**Prompt.** Everything inside the fence is the prompt and nothing outside it is.

```prompt
<layer-2 text only, as ONE unwrapped line; §1 is prepended at call time>
```
```

Cast `Status` ∈ `cast` | `not-cast` | `needs-reconcile` | `none-by-design`.

### Cover record — `docs/images/covers/<story-id>.md`

Follows `docs/images/server-hall-monolith.md` (the newer of the two exemplars —
`register-anchor.md` predates the `used_by` key):

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
flow_create_character({ name, refImages })     // refImages: string[], min 1
flow_generate_image({ prompt, outPath, character?, numOutputs? })   // numOutputs 1–4
flow_edit_image({ prompt, referenceImages, outPath, character?, numOutputs? })
                                               // referenceImages min 1 / max 3 by schema,
                                               // but use EXACTLY ONE (README:31) — multi-ref
                                               // uploads reliably time out
flow_refine({ prompt, outPath })
```

**There is no tool that lists or creates Flow projects.** `server.ts` registers
eight tools and `flow_open_project` only *opens* by exact name. Project
enumeration (T11a) and project creation (T12) are therefore
`mcp__playwright__browser_*` steps against the CDP-attached browser, or manual
UI actions — not flow-mcp calls.

**Aspect ratio is not a parameter.** It is a global Flow UI tab and defaults to
landscape, which is what covers need. Note `docs/superpowers/flow-selectors.md:232`
logs aspect control as an open issue: real observed output is **1376×768
(ratio 1.792)**, near but not exactly 16:9. Assert "landscape within 2% of
1.778", never strict equality.

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
- **Re-generating the existing Tarquin and Bob sheets** unless T11a proves them
  unrecoverable.

---

## Tickets

### T1: The ledger format spec   [Status: pending | Model: sonnet]
- **Scope:** Write `docs/stories/PROMPT-LEDGER.md` — the authoritative format
  for `prompts.md`, exactly as given in **Interfaces**: frontmatter keys, the
  three sections, the cast-status vocabulary (which lives *here only*), the lint
  line, the composition rule (§1 + §3 concatenated; cast attached via the
  `character` parameter, never as prose), and the pick-and-promote rule for
  multi-candidate output.
- **Files:** create `docs/stories/PROMPT-LEDGER.md`.
- **Acceptance criteria:** the doc states all four layers; states that Layer 0
  lives only in the skill and is never copied; states the four lint triggers;
  states the "two failures = block, rewrite never retry" rule; states that
  `numOutputs > 1` writes `-a`/`-b` and never the bare name; and states the
  **copy-paste rule** — every prompt is a ` ```prompt ` fenced block written as
  one unwrapped line, everything outside the fence is metadata that is never
  pasted into Flow, and no prompt is ever stored as a blockquote (the `>`
  markers would be pasted verbatim into the prompt box).
- **TDD:** no (docs)
- **Validation:** `test -f docs/stories/PROMPT-LEDGER.md`;
  `grep -ic "rewrite, never retry" docs/stories/PROMPT-LEDGER.md` ≥ 1;
  `grep -c "needs-reconcile" docs/stories/PROMPT-LEDGER.md` ≥ 1.
- **Depends on:** —
- [ ] done
- Notes:

### T2: Scaffold the four ledgers   [Status: pending | Model: sonnet]
- **Scope:** Create `prompts.md` in all four story folders with frontmatter and
  the three section headings present but bodies empty (`_TBD — T6/T7/T9/T10_`).
  Populate §2 cast tables from the existing character files: every
  `characters/*.md` becomes a row **except** MMT's `dawn.md` (deprecated by T5).
  Camping's two recorded Flow Character IDs go in with status `needs-reconcile`.
  **`none-by-design` for GPOM's `the-ai.md` and Karen's `sean-ai.md`** (the
  latter is a UI, not a face — `sean-ai.md:5`). Everything else `not-cast`.
  Do **not** copy the status legend into these files.
- **Files:** create `docs/stories/{gitpush-origin-master,camping,karen,magic-money-tree}/prompts.md`.
- **Acceptance criteria:** four files exist; each `story:` value equals its
  folder name; no file contains the status legend; no character is `cast` yet.
- **TDD:** no (docs)
- **Validation:** `ls docs/stories/*/prompts.md | wc -l` returns `4`;
  `grep -c '^|.*needs-reconcile' docs/stories/camping/prompts.md` returns `2`;
  `grep -c '^|.*none-by-design' docs/stories/karen/prompts.md` returns `1`;
  `grep -c 'dawn' docs/stories/magic-money-tree/prompts.md` returns `0`.
- **Depends on:** T1, T5
- [ ] done
- Notes:

### T3: Link ledgers from canon; absorb camping/style.md   [Status: pending | Model: sonnet]
- **Scope:** Add a prominent link to `prompts.md` near the top of each of the
  four `story.md` files (below frontmatter, above the first heading). Move the
  contents of `docs/stories/camping/style.md` into `camping/prompts.md` §1 as
  raw material for T6 — preserving the recurring-locations list, the
  three-warmth-places rule and the motifs — then delete `style.md` and repoint
  its **five live references**: `docs/stories/camping/README.md:31` and
  `docs/stories/camping/story.md:232, 426, 429, 432`.
  **Do not touch** `docs/stories/camping/master-notes-2026-08-04.md:1149` (a
  verbatim Kai↔Jack transcript) or the historical spec at
  `docs/superpowers/specs/2026-06-27-*-design.md`.
- **Files:** modify `docs/stories/{gitpush-origin-master,camping,karen,magic-money-tree}/story.md`,
  `docs/stories/camping/README.md`, `docs/stories/camping/prompts.md`;
  delete `docs/stories/camping/style.md`.
- **Acceptance criteria:** `style.md` no longer exists; no live reference to it
  remains outside the transcript; all four `story.md` files link `./prompts.md`.
- **TDD:** no (docs)
- **Validation:** `! test -f docs/stories/camping/style.md`;
  `grep -rl "style.md" docs/stories/camping/ --exclude='master-notes-*.md'`
  returns nothing;
  `grep -l "prompts.md" docs/stories/*/story.md | wc -l` returns `4`.
- **Depends on:** T2
- [ ] done
- Notes:

### T4: Recover the GPOM Short assets from git   [Status: pending | Model: sonnet]
- **Scope:** The retired GPOM Short's per-panel prompt records and a Carrier
  character sheet exist only in git history at commit `7dd36c7^` under
  `docs/stories/gpom-short/` (confirmed present via `git ls-tree`). Recover them:
  restore `characters/img/carrier.jpg` to
  `docs/stories/gitpush-origin-master/characters/img/carrier-sheet.jpg`, and
  append the 16 panel prompts (`storyboard/p01.md`…`p16.md`) to GPOM's
  `prompts.md` as an `## Appendix — GPOM Short panel prompts (retired comic,
  style reference)` section. These are the best worked examples of the near-black
  register in the repo and are raw material for T7.
- **Files:** create
  `docs/stories/gitpush-origin-master/characters/img/carrier-sheet.jpg`;
  modify `docs/stories/gitpush-origin-master/prompts.md`,
  `docs/stories/gitpush-origin-master/characters/the-carrier.md` (set `sheet:`).
- **Acceptance criteria:** the carrier image exists and is a valid JPEG; the
  appendix contains 16 prompt blockquotes; `the-carrier.md` frontmatter `sheet:`
  points at the recovered file.
- **TDD:** no (asset recovery)
- **Validation:**
  `git ls-tree -r 7dd36c7^ --name-only | grep -c 'gpom-short/storyboard/p'` ≥ 16;
  `file docs/stories/gitpush-origin-master/characters/img/carrier-sheet.jpg`
  reports JPEG image data;
  `grep -c '^### ' docs/stories/gitpush-origin-master/prompts.md` ≥ 16.
- **Depends on:** T2
- [ ] done
- Notes:

### T5: Canon hygiene   [Status: pending | Model: sonnet]
- **Scope:** Mark `docs/stories/magic-money-tree/characters/dawn.md` deprecated —
  add a `> **DEPRECATED 2026-08-08.**` banner explaining that the 2026-08-05/06
  re-founding replaced the Dawn spine with Keynes and the tree
  (`story.md:12-17`), change `role:` so it no longer claims `protagonist`, and
  note the v1 comic and its 10 panel records still reflect this superseded
  spine. Do not delete the file. **Verify only** that
  `docs/stories/magic-money-tree/storyboard/v1-comic-plan.md:1-9` already carries
  its deprecation banner — it does; change nothing there unless it is missing.
- **Files:** modify `docs/stories/magic-money-tree/characters/dawn.md`;
  verify `docs/stories/magic-money-tree/storyboard/v1-comic-plan.md`.
- **Acceptance criteria:** `dawn.md` carries the banner and no longer declares
  `role: protagonist`; `keynes.md` is the only MMT character with that role.
- **TDD:** no (docs)
- **Validation:**
  `grep -c "DEPRECATED" docs/stories/magic-money-tree/characters/dawn.md` ≥ 1;
  `grep -l "role: protagonist" docs/stories/magic-money-tree/characters/*.md`
  lists only `keynes.md`.
- **Depends on:** —
- [ ] done
- Notes:

### T11a: Flow survey (read-only)   [Status: pending | Model: opus]
- **Scope:** Establish ground truth in Flow **before** any prompt is finalised,
  changing nothing. Bring the browser up (`./scripts/flow-chrome.sh`, poll
  `curl -s http://localhost:9222/json/version`, then `flow_status()`). Using
  Playwright MCP against the attached browser (there is no flow-mcp enumerate
  tool), determine and record: **(a)** every project, its ID and best-guess
  story; **(b)** whether each of Camping's three cited UUIDs is still reachable —
  the character project `9b729074-…` holding `29e97ae3-…`/`7566666e-…`, and the
  two sheet-source projects `8970bef9-…` and `b5d76bd1-…` (see the
  Reconciliation table; they are different kinds of thing); **(c)** what
  Karen-story imagery exists in Flow that the repo has no record of, and whether
  any of it is already a Flow Character; **(d)** whether Flow Characters are now
  account-global rather than project-scoped, given the home page advertises
  casting them "anywhere" — this contradicts
  `.claude/skills/badcode-art-direction/SKILL.md:67`; **(e)** what the image
  aspect tab currently reads. Write it all to `docs/stories/FLOW-STATE.md`.
  **Create nothing. Delete nothing. Overwrite nothing.**
- **Files:** create `docs/stories/FLOW-STATE.md`.
- **Acceptance criteria:** every project in the account is listed with its ID;
  each of (a)–(e) has an explicit written answer; if (d) proves characters are
  global, the file says so and names `badcode-art-direction/SKILL.md:67` as the
  doc needing correction; no Flow state was modified.
- **TDD:** no (investigation)
- **Validation:** `test -f docs/stories/FLOW-STATE.md`;
  the file contains the strings `(a)` through `(e)`;
  `flow_status()` returns `loggedIn: true`.
- **Depends on:** —
- [ ] done
- Notes:

---
**GATE — Phase 1 begins. T6–T10 are authored WITH Kai, in conversation. An
executor must not invent this copy unattended.**
---

### T6: Style prompts — Camping and Karen   [Status: CANCELLED 2026-08-08 — visuals developed externally by Jack]
- **Scope:** Author §1 of the Camping and Karen ledgers. Camping's derives from
  the absorbed `style.md` material (matched city pair, the wet car park, warmth
  permitted in exactly three named places, 35mm documentary). Karen's is written
  fresh from `docs/stories/karen/story.md` — the Midtown phone box across nine
  months of weather, the blazer-and-lanyard archetype, New York exteriors — **and
  must be reconciled against the Karen imagery T11a found in Flow**, which is the
  anchor rather than a competitor. Each style prompt is one paragraph,
  prependable verbatim, names a palette and a film stock, and never names a
  specific shot or a real brand.
- **Files:** modify `docs/stories/{camping,karen}/prompts.md`.
- **Acceptance criteria:** both §1 sections contain a single blockquoted
  paragraph; neither restates Layer 0 material already in the skill; neither
  names a specific scene or a real brand.
- **TDD:** no (copy)
- **Validation:** `grep -A3 "## 1. Style prompt" docs/stories/camping/prompts.md`
  shows a non-`TBD` blockquote; same for `karen`.
- **Depends on:** T3, T11a
- [ ] done
- Notes:

### T7: Style prompts — GPOM and Magic Money Tree   [Status: pending | Model: opus]
- **Scope:** Author §1 for the two stories with no established look. GPOM's is
  the near-black monumental register, using the T4 appendix and
  `docs/images/register-anchor.md` as worked examples. MMT's is the London-park
  register — low winter daylight, documentary-historical, the bench and the young
  lime as recurring geometry across decades. Discuss both with Kai before
  writing.
- **Files:** modify `docs/stories/{gitpush-origin-master,magic-money-tree}/prompts.md`.
- **Acceptance criteria:** as T6.
- **TDD:** no (copy)
- **Validation:** `grep -A3 "## 1. Style prompt" docs/stories/gitpush-origin-master/prompts.md`
  shows a non-`TBD` blockquote; same for `magic-money-tree`.
- **Depends on:** T4, T11a
- [ ] done
- Notes:

### T8: Visual blocks for the uncast roster   [Status: pending | Model: opus]
- **Scope:** Four character files have no `## Visual` section: Karen and Ari
  (genuinely thin — 1.8 KB / 1.3 KB, nothing to harvest) and Keynes and the tree
  (substantial prose and `signals:` frontmatter that should be **harvested**, not
  reinvented). Write a `## Visual` for each, following the structure proven in
  `camping/characters/tarquin.md` — a locked list of physical invariants specific
  enough that two independent generations read as the same subject. Keynes is
  historically *inspired*, **not a likeness** (likeness phrasing is block trigger
  #2): describe build, era dress and bearing, never "looks like John Maynard
  Keynes". The tree is an unremarkable young European lime, 28 years old in 1942:
  **no glow, no face**, presence carried by framing, wind and light.
- **Files:** modify `docs/stories/karen/characters/{karen,ari}.md`,
  `docs/stories/magic-money-tree/characters/{keynes,the-tree}.md`.
- **Acceptance criteria:** all four files contain a `## Visual` section; none
  names a real person as a likeness target; `the-tree.md`'s block explicitly
  forbids glow and face.
- **TDD:** no (copy)
- **Validation:**
  `grep -l "## Visual" docs/stories/karen/characters/*.md docs/stories/magic-money-tree/characters/*.md | wc -l`
  returns `5` (the four above plus MMT's pre-existing `dawn.md`).
- **Depends on:** T5, T6, T7
- [ ] done
- Notes:

### T9: Character sheet prompts   [Status: pending | Model: opus]
- **Scope:** Write a Layer-2 prompt in each ledger's §3 for every character
  needing a sheet: Karen, Ari, Keynes, the tree, the tent, the SUV, the Hundred.
  Each produces a **multi-angle turnaround on a neutral background**, matching
  `tarquin-sheet.jpg` (four full-body angles above three head angles). Object
  refs (tent, SUV, tree) get a multi-angle object sheet in neutral lighting
  instead of a portrait grid. The Carrier already has a recovered sheet from T4
  and needs a prompt only if T11a showed it must be regenerated.
- **Files:** modify all four `docs/stories/*/prompts.md`.
- **Acceptance criteria:** each of the seven has a §3 entry with a prompt, a
  named light source, a `Cast:` line (usually `—` for a sheet), an unfilled
  `Lint:` line, and a repo-relative `outPath` under
  `docs/stories/*/characters/img/`.
- **TDD:** no (copy)
- **Validation:** `grep -c "^### " docs/stories/karen/prompts.md` ≥ `3`
  (karen, ari, cover);
  `grep -ohP '→ `\K[^`]+' docs/stories/*/prompts.md | while read p; do test -e "$(dirname $p)" || echo "BAD $p"; done`
  prints nothing.
- **Depends on:** T8
- [ ] done
- Notes:

### T10: The four cover prompts, and the lint pass   [Status: pending | Model: opus]
- **Scope:** Write the Layer-2 cover prompt for each story per **Architecture →
  The four covers**, each naming its single motivated light source, holding its
  subject small in a large frame, and baking in no text. GPOM's is the orbital
  server hall with Earth at roughly a quarter of the frame lit by earthlight —
  include the deliberate-departure note so no one later "corrects" it toward LEO.
  Then lint **every** prompt written in T6–T10 against the four triggers at
  `badcode-art-direction/SKILL.md:92-102`, rewrite any that trip one using that
  file's `:106` table, and stamp each asset's `Lint:` line.
- **Files:** modify all four `docs/stories/*/prompts.md`.
- **Acceptance criteria:** four `### cover` entries exist, one per ledger, each
  naming a light source and an `outPath` under `docs/images/covers/`; every §3
  entry across all four ledgers has a stamped `Lint: ✅` line; **no blockquoted
  prompt** contains a real brand name, a legible wordmark, or likeness phrasing.
- **TDD:** no (copy)
- **Validation:** `grep -c "### cover" docs/stories/*/prompts.md` returns `1`
  per file; `grep -L "Lint: ✅" docs/stories/*/prompts.md` returns nothing;
  brand check — extract the fenced prompt blocks only and search those:
  `awk '/^```prompt$/{p=1;next} /^```$/{p=0} p' docs/stories/*/prompts.md | grep -iE 'waitrose|natwest|bmw|x8|spacex|starlink|claude' || echo CLEAN`
  (note: **no `-r`** — with `-r` and no path argument grep recurses the whole
  repo instead of reading stdin, and the check silently becomes meaningless)
  must print `CLEAN` (canon prose elsewhere in the file legitimately names these;
  only the prompts must be clean).
- **Depends on:** T9
- [ ] done
- Notes:

---
**GATE — Kai approves every prompt on paper before Phase 2. No credits are spent
before this gate clears.**
---

### T11b: Write reconciliation into the ledgers   [Status: pending | Model: sonnet]
- **Scope:** Apply T11a's findings: set every cast row's status to its true
  value, fill `flow_project_id`, and clear every `needs-reconcile`. If a recorded
  Flow Character is gone, mark it `not-cast` and note it in the ledger so T13–T16
  regenerate it; if it survives, mark it `cast`.
- **Files:** modify all four `docs/stories/*/prompts.md`.
- **Acceptance criteria:** no cast row anywhere still reads `needs-reconcile`;
  every row's status is justified by a line in `FLOW-STATE.md`.
- **TDD:** no (docs)
- **Validation:** `grep -c '^|.*needs-reconcile' docs/stories/*/prompts.md`
  returns `0` for every file (use `|| true`; `grep -c` exits 1 on no match).
- **Depends on:** T10, T11a
- [ ] done
- Notes:

### T12: Adopt or create the four Flow projects   [Status: pending | Model: sonnet]
- **Scope:** Ensure one Flow project per story exists, named `badcode-<story-id>`
  where a new one is created. **Project creation is a UI action** — use
  Playwright MCP against the attached browser; there is no flow-mcp create tool.
  Adopt an existing project where T11a identified one rather than creating a
  duplicate; since **rename is not automatable**
  (`docs/superpowers/flow-selectors.md:226`), record the project's *real* name in
  the ledger's `flow_project` field rather than trying to rename it.
  `flow_open_project` matches exact names only.
- **Files:** modify all four `docs/stories/*/prompts.md`, `docs/stories/FLOW-STATE.md`.
- **Acceptance criteria:** `flow_open_project({ name })` succeeds for the
  `flow_project` value recorded in each of the four ledgers; no existing project
  was deleted or renamed.
- **TDD:** no (config)
- **Validation:** four successful `flow_open_project` calls, one per recorded
  name, each returning `projectOpen: true`.
- **Depends on:** T11b
- [ ] done
- Notes:

### T13: Character sheets — Camping objects   [Status: CANCELLED 2026-08-08 — visuals developed externally by Jack]
- **Scope:** Generate multi-angle object sheets for the tent and the SUV from
  their T9 prompts at `numOutputs: 2`, then **pick and promote**: choose the
  winner, `mv <name>-sheet-<x>.jpg <name>-sheet.jpg`, delete the loser. Write the
  Flow media id and a v1 revision line into the ledger and fill `sheet:` in each
  character file. **The SUV prompt must not name a real manufacturer or model,
  or show a legible badge** — trigger #1. Two no-candidate calls = a block:
  rewrite per the `:106` table, do not retry.
- **Files:** create `docs/stories/camping/characters/img/{tent,wank-tank}-sheet.jpg`;
  modify `docs/stories/camping/characters/{tent,wank-tank}.md`,
  `docs/stories/camping/prompts.md`.
- **Acceptance criteria:** both promoted images exist as valid JPEGs; no `-a`/`-b`
  files remain; both character files have non-empty `sheet:`; both ledger entries
  carry a media id and a v1 revision line.
- **TDD:** no (generation)
- **Validation:**
  `file docs/stories/camping/characters/img/tent-sheet.jpg docs/stories/camping/characters/img/wank-tank-sheet.jpg`
  reports JPEG for both;
  `find docs/stories/camping -name '*-[ab].jpg' | wc -l` returns `0`;
  `grep -c 'sheet: ""' docs/stories/camping/characters/*.md` returns `0` (`|| true`).
- **Depends on:** T12
- [ ] done
- Notes:

### T14: Character sheets — Karen and Ari   [Status: CANCELLED 2026-08-08 — visuals developed externally by Jack]
- **Scope:** As T13, into `docs/stories/karen/characters/img/{karen,ari}-sheet.jpg`,
  including the pick-and-promote step. **If T11a found existing Karen or Ari
  imagery in Flow, use it as the reference** via `flow_edit_image` — exactly one
  reference, downscaled first with
  `convert <src> -resize 1600x1600\> -quality 88 <tmp>.jpg` — rather than
  generating a new face from scratch. Jack's existing work is the anchor. Then
  cast each with `flow_create_character` and record the identity in the ledger
  with status `cast`. **Never overwrite an existing Flow character.**
- **Files:** create the two sheet images; modify
  `docs/stories/karen/characters/{karen,ari}.md`, `docs/stories/karen/prompts.md`.
- **Acceptance criteria:** both promoted images exist; both are cast as Flow
  Characters; the `@Karen` and `@Ari` rows read `cast` with IDs; Sean AI's row
  still reads `none-by-design`; no pre-existing Flow character was overwritten.
- **TDD:** no (generation)
- **Validation:**
  `file docs/stories/karen/characters/img/karen-sheet.jpg docs/stories/karen/characters/img/ari-sheet.jpg`
  reports JPEG for both;
  `grep -E '^\| @(Karen|Ari) ' docs/stories/karen/prompts.md | grep -c 'not-cast'`
  returns `0` (`|| true`);
  `find docs/stories/karen -name '*-[ab].jpg' | wc -l` returns `0`.
- **Depends on:** T12
- [ ] done
- Notes:

### T15: Character sheets — Keynes and the tree   [Status: pending | Model: sonnet]
- **Scope:** As T14, into
  `docs/stories/magic-money-tree/characters/img/{keynes,the-tree}-sheet.jpg`,
  including pick-and-promote. Keynes is cast as a Flow Character. The tree is an
  object sheet — multi-angle, **no glow, no face** — and is **not** cast as a
  Character (there is no face to bind); record it `none-by-design` with a note
  that it is referenced by sheet image instead.
- **Files:** create the two sheet images; modify
  `docs/stories/magic-money-tree/characters/{keynes,the-tree}.md`,
  `docs/stories/magic-money-tree/prompts.md`.
- **Acceptance criteria:** both promoted images exist; Keynes is `cast` with an
  ID; the tree row reads `none-by-design`; no image shows a glowing or
  anthropomorphised tree.
- **TDD:** no (generation)
- **Validation:**
  `file docs/stories/magic-money-tree/characters/img/keynes-sheet.jpg docs/stories/magic-money-tree/characters/img/the-tree-sheet.jpg`
  reports JPEG for both;
  `find docs/stories/magic-money-tree -name '*-[ab].jpg' | wc -l` returns `0`.
- **Depends on:** T12
- [ ] done
- Notes:

### T16: Character sheets — the Carrier and the Hundred   [Status: pending | Model: sonnet]
- **Scope:** Cast the Carrier as a Flow Character **from the sheet recovered in
  T4** and record the ID; regenerate the sheet only if T11a showed it
  unusable. Generate a sheet for the Hundred — a **collective**, so this is a
  wardrobe-and-texture reference plate (hand-darned wool in slightly-wrong
  colours, mechanical tools, paper, candle-and-battery light), not a portrait
  grid, and it is not cast as a Character. Pick-and-promote as T13.
- **Files:** create
  `docs/stories/gitpush-origin-master/characters/img/the-hundred-sheet.jpg`;
  modify `docs/stories/gitpush-origin-master/characters/{the-carrier,the-hundred}.md`,
  `docs/stories/gitpush-origin-master/prompts.md`.
- **Acceptance criteria:** the Carrier is `cast` with an ID sourced from the
  recovered sheet; the Hundred's plate exists; the AI's row still reads
  `none-by-design` and no image of it was generated.
- **TDD:** no (generation)
- **Validation:**
  `file docs/stories/gitpush-origin-master/characters/img/the-hundred-sheet.jpg`
  reports JPEG;
  `grep -c '^|.*none-by-design' docs/stories/gitpush-origin-master/prompts.md` ≥ `1`;
  `find docs/stories/gitpush-origin-master -name '*-[ab].jpg' | wc -l` returns `0`.
- **Depends on:** T12
- [ ] done
- Notes:

### T17: Assemble the contact sheet   [Status: pending | Model: sonnet]
- **Scope:** Write `docs/stories/CONTACT-SHEET.md` — one page embedding all
  **ten** character sheets (Tarquin and Bob pre-existing; tent, SUV, Karen, Ari,
  Keynes, the tree, the Carrier, the Hundred produced by T4/T13–T16), each with
  its story, tag, Flow Character status and a one-line reminder of the canon
  invariants it was meant to hit, so Kai can review the whole cast in one pass.
- **Files:** create `docs/stories/CONTACT-SHEET.md`.
- **Acceptance criteria:** every sheet appears exactly once; each entry has an
  empty `- [ ] accepted` checkbox; every image path resolves to a real file.
- **TDD:** no (docs)
- **Validation:**
  `grep -c '\- \[ \] accepted' docs/stories/CONTACT-SHEET.md` returns `10`;
  `grep -oP '\]\(\K[^)]+' docs/stories/CONTACT-SHEET.md | while read p; do test -f "$p" || echo "MISSING $p"; done`
  prints nothing.
- **Depends on:** T13, T14, T15, T16
- [ ] done
- Notes:

---
**GATE — Kai reviews the contact sheet in one pass and marks rejections.**
---

### T18: Character correction pass   [Status: pending | Model: sonnet]
- **Scope:** For every sheet Kai left unticked, run one correction round with
  `flow_edit_image`: **always reference the accepted golden original**, exactly
  one reference image, downscaled, `numOutputs: 2`, using the delta-prompt shape
  at `.claude/skills/edit-panel/SKILL.md:40-59` (style anchor + Google's verbatim
  edit template + all changes batched into one round). Pick-and-promote, update
  the sheet, re-cast the Flow Character if the face changed, append a revision
  line. If a sheet needs more than three chained rounds, stop and lock-and-rebuild
  — merge the deltas into one full prompt, regenerate clean, rewrite the ledger's
  main prompt.
- **Files:** modify the corrected sheet images and their ledgers;
  modify `docs/stories/CONTACT-SHEET.md`.
- **Acceptance criteria:** every checkbox is ticked; every corrected sheet has a
  revision line naming the exact delta prompt; no candidate files remain.
- **TDD:** no (generation)
- **Validation:** `! grep -q '\- \[ \] accepted' docs/stories/CONTACT-SHEET.md`;
  `find docs/stories -name '*-[ab].jpg' | wc -l` returns `0`.
- **Depends on:** T17
- [ ] done
- Notes:

### T19: Generate the four covers   [Status: pending | Model: opus]
- **Scope:** Generate each cover from its T10 ledger prompt, composed as §1 + §3,
  with the approved cast attached via the `character` parameter, `numOutputs: 2`,
  then **pick and promote** to `docs/images/covers/<story-id>.jpg`. Judge each
  against the three grammar rules and against the others **as a set**: the four
  must be distinguishable at thumb size while reading as one series. Refine with
  `flow_refine` where a candidate is close. Record each returned `mediaId` and a
  v1 revision line on the `### cover` entry in that story's ledger.
- **Files:** create `docs/images/covers/{gitpush-origin-master,camping,karen,magic-money-tree}.jpg`;
  modify all four `docs/stories/*/prompts.md`.
- **Acceptance criteria:** exactly four JPEGs in `docs/images/covers/`, all
  landscape ≈16:9; none contains legible text; GPOM's shows Earth as a whole disc
  at roughly a quarter of the frame as the scene's only light source; no cover is
  a near-duplicate of `docs/images/register-anchor.jpg`; every `### cover` entry
  has a non-empty media id.
- **TDD:** no (generation)
- **Validation:** `ls docs/images/covers/*.jpg | wc -l` returns `4`;
  ratio check —
  `identify -format "%f %w %h\n" docs/images/covers/*.jpg | awk '{r=$2/$3; if(r<1.742||r>1.814){print "FAIL",$0; f=1}} END{exit f}'`
  exits `0` (1.778 ±2%, tolerating the observed 1376×768 = 1.792 per
  `flow-selectors.md:232`);
  `grep -c 'Flow media id: <uuid>' docs/stories/*/prompts.md` returns `0` (`|| true`);
  manual visual check of all four side by side at thumb width.
- **Depends on:** T18
- [ ] done
- Notes:

### T20: Cover records, index and frontmatter   [Status: pending | Model: sonnet]
- **Scope:** Write a sibling `.md` record for each cover following
  `docs/images/server-hall-monolith.md` (frontmatter `image`, `flow_media_id`,
  `model`, `status`, `used_by`, then the exact prompt as a blockquote and a
  revisions log). Add four index rows to `docs/images/README.md`. Copy each cover
  to `apps/web/public/covers/` and add `cover: /covers/<story-id>.jpg` to each
  story's `story.md` frontmatter.
- **Files:** create `docs/images/covers/*.md` (× 4), `apps/web/public/covers/*.jpg`
  (× 4); modify `docs/images/README.md`, `docs/stories/*/story.md` (× 4).
- **Acceptance criteria:** four records with non-empty `flow_media_id`;
  `docs/images/README.md` has a row per cover; all four `story.md` files carry a
  `cover:` key whose path resolves under `apps/web/public/`.
- **TDD:** no (docs/wiring)
- **Validation:** `ls docs/images/covers/*.md | wc -l` returns `4`;
  `grep -c "^cover:" docs/stories/*/story.md` returns `1` per file;
  `for f in docs/stories/*/story.md; do v=$(grep '^cover:' $f | sed 's|^cover: /||'); test -f "apps/web/public/$v" || echo "MISSING $v"; done`
  prints nothing.
- **Depends on:** T19
- [ ] done
- Notes:

### T21: Sean AI as SVG   [Status: DEFERRED 2026-08-08 — Karen's visuals are Jack's; revisit only if he asks for it]
- **Scope:** Build Sean AI's identity as vector art in-repo, not through Flow: an
  8-bit pixel-art moniker plus a `Sean AI` wordmark, and a gold variant for the
  §4.3 government takeover. A legible wordmark is trigger #1 and this is a vector
  job regardless. Keep it a **parody register** — it must not reproduce any real
  product's mark. Record the decision and both paths in
  `docs/stories/karen/prompts.md` under `## 4. Non-Flow assets`.
- **Files:** create `apps/web/public/brand/{sean-ai,sean-ai-gold}.svg`; modify
  `docs/stories/karen/characters/sean-ai.md`, `docs/stories/karen/prompts.md`.
- **Acceptance criteria:** both SVGs exist and render; neither reproduces a real
  product mark; `sean-ai.md`'s `sheet:` points at the SVG and still explains he
  is a UI, not a face.
- **TDD:** no (asset)
- **Validation:** `identify apps/web/public/brand/sean-ai.svg apps/web/public/brand/sean-ai-gold.svg`
  exits `0` and reports non-zero dimensions for both (ImageMagick rasterises SVG;
  `xmllint` is **not** installed on this machine);
  `grep -c "Non-Flow assets" docs/stories/karen/prompts.md` returns `1`.
- **Depends on:** T3
- [ ] done
- Notes:

### T22: Delta note to the website-reset plan   [Status: pending | Model: sonnet]
- **Scope:** Append a clearly-headed `## Delta — story covers (2026-08-08)`
  section to `design/2026-08-07-badcode-website-reset.md` asking it to: **(a)**
  add `cover: string` to `StoryRecord` in its **T2** ticket ("Frontmatter schema,
  parser and validator", `:386`; the interface is at `:253-258` — note T1 at
  `:363` is the tooling baseline, not the schema) and make the Ledger row's 16:9
  thumb and the T15 OG chain (`:676-685`) prefer it over `film.poster`;
  **(b) restrict the catalogue to the four EP stories** — Galileo, Storyverse and
  Future Proof stay file-ready but unlinked from the home page, per Kai's
  2026-08-08 ruling; **(c)** note the covers now exist at
  `apps/web/public/covers/`. Do not edit that plan's existing tickets or status.
- **Files:** modify `design/2026-08-07-badcode-website-reset.md`.
- **Acceptance criteria:** the delta section exists with all three points; no
  existing ticket text, checkbox or status was altered.
- **TDD:** no (docs)
- **Validation:** the file is **untracked**, so `git diff` is useless here.
  Snapshot first —
  `cp design/2026-08-07-badcode-website-reset.md /tmp/wr-before.md` — then after
  editing, `diff -u /tmp/wr-before.md design/2026-08-07-badcode-website-reset.md | grep -c '^-[^-]'`
  returns `0` (additions only).
- **Depends on:** T20
- [ ] done
- Notes:

### T23: Repo map and memory   [Status: pending | Model: sonnet]
- **Scope:** Add the prompt ledger to `CLAUDE.md`'s repo map and its "How to work
  in this repo" list: one table row for `docs/stories/<story>/prompts.md` and a
  bullet explaining the four-layer model and that Layer 0 lives in the
  `badcode-art-direction` skill. Reference `docs/stories/PROMPT-LEDGER.md` as the
  format spec.
- **Files:** modify `CLAUDE.md`.
- **Acceptance criteria:** `CLAUDE.md` names `prompts.md` and `PROMPT-LEDGER.md`;
  the four-layer model is stated in one or two sentences.
- **TDD:** no (docs)
- **Validation:** `grep -c "prompts.md" CLAUDE.md` ≥ `1`;
  `grep -c "PROMPT-LEDGER" CLAUDE.md` ≥ `1`.
- **Depends on:** T22
- [ ] done
- Notes:

### T24: End-to-end verification   [Status: pending | Model: opus]
- **Scope:** Prove the whole thing holds together. Confirm every ledger is
  complete and internally consistent (every cast row has a real status; every §3
  asset has a prompt, a lint stamp and a media id; every `outPath` resolves to a
  file that exists). Confirm the four covers sit side by side as a coherent series
  and are individually legible **at catalogue-thumb width, not full size**. Then
  run the cold-start test: open only `docs/stories/karen/prompts.md` and verify it
  alone tells you the style, the cast, the Flow project and every prompt for that
  story.
- **Files:** none (verification only; log findings in the Discovered Issues Log).
- **Acceptance criteria:** all of the above hold; any failure is logged rather
  than silently fixed.
- **TDD:** no (verification)
- **Validation:** `ls docs/images/covers/*.jpg | wc -l` returns `4`;
  `grep -L "Lint: ✅" docs/stories/*/prompts.md` returns nothing;
  `find docs/stories -name '*-[ab].jpg' | wc -l` returns `0`;
  `grep -c '^|.*needs-reconcile' docs/stories/*/prompts.md` returns `0` per file
  (`|| true`);
  `npm run typecheck` clean and `npm run build` succeeds — **regression tripwires
  only**: this plan touches no typechecked code, so they cannot fail *because* of
  it; the real web-facing check is T20's `cover:` path resolution.
- **Depends on:** T23
- [ ] done
- Notes:

---

## Discovered Issues Log

_(appended by executors during implementation)_
