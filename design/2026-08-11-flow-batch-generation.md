# Flow batch generation — GPOM + MMT prompt ledgers → images

**Date:** 2026-08-11 · **Status:** planned, not started
**Goal:** fire every unfired prompt in the two prompt ledgers —
[`docs/stories/gitpush-origin-master/prompts.md`](../docs/stories/gitpush-origin-master/prompts.md)
and [`docs/stories/magic-money-tree/prompts.md`](../docs/stories/magic-money-tree/prompts.md) —
via the Flow MCP, characters first, then scenes, with Kai gating acceptances.

**Mandatory reading for the executing session:**
`.claude/skills/badcode-art-direction/SKILL.md` (Layer 0 register + the
policy-block trigger/rewrite table). Both prompts.md files, top to bottom —
especially §0 guardrails and §2b totem lock ordering. Do not rewrite the §3
prompts; they are linted and self-contained. Paste them verbatim.

---

## Capability check (done 2026-08-11)

- `flow_create_character(name, refImages[])` exists and is **live-validated**
  (camping-v2 hardening pass). Characters attach to `flow_generate_image` via
  the `character` param.
- `flow_generate_batch` has **no `character` param** and caps at 8 prompts —
  use individual `flow_generate_image` calls (numOutputs=2 for two candidates
  per turn, ~45–60s a round).
- **No project-creation tool.** `flow_open_project` errors on absent names.
  → **Manual step for Kai** (Phase 0): create two Flow projects, tell the
  session their exact names; record them in each prompts.md frontmatter
  (`flow_project`, closing the T11b/T12 TBDs).
- **One logged-in browser = strictly serial.** No parallel fan-out. One
  background agent works both queues in sequence.
- **Carrier sheet recovery:** the prompts.md pointer is stale. The real path is
  `git show 7dd36c7^:docs/stories/gpom-short/characters/img/carrier.jpg`
  (841 KB, verified present). Restore to
  `docs/stories/gitpush-origin-master/characters/img/carrier-sheet.jpg` and fix
  the pointer in prompts.md §2.
- Policy blocks look like timeouts (>half of unlinted prompts). These prompts
  are pre-linted, but on any TIMEOUT: **rewrite per the art-direction table,
  never blind-retry.** Use the `flow-operator` agent for browser
  preflight/reconnect mechanics.

## Out of scope (per the ledgers themselves)

- GPOM scenes 1–4 + the green ✓ — motion graphics (§5), not Flow.
- GPOM scene 5, scene 18, s10-peopled — deliberately unprompted (§4).
- MMT beats 1, 4, 7, 8 — archive-only by guardrail.
- Videos/animation — separate pass (`animate-slide`).

---

## Phase 0 — preflight (interactive, minutes)

1. `flow-operator`: launch Flow Chrome, CDP attach, `flow_status` green
   (Kai only needed if login expired).
2. Kai creates the two Flow projects; record names in both frontmatters.

## Phase 1 — characters (interactive)

| Character | Route |
| --- | --- |
| GPOM @Carrier | Recover sheet from git (above) → Kai confirms face still canon → `flow_create_character("Carrier", [sheet])` → **Create Body** (below). Done, 2026-08-11. |
| MMT @Keynes | No sheet exists (T15). Generate one via badcode-art-direction loop — 1940s build/era-dress/bearing, **never the name** (block trigger #2) — 2 candidates/round until Kai accepts → `flow_create_character("Keynes", [accepted])` → **Create Body**. |
| MMT @TheTree | **Not a Character** — the accepted MMT cover is the bench+tree golden reference. |
| GPOM @TheAI / @TheHundred | Never cast, by canon. |

**Every cast character gets a body pass, not just a portrait.** Flow's
Character object isn't fed an external turnaround sheet — it's built natively:
portrait, then the editor's **"Create Body"** button opens a second view and a
"Describe body and outfit…" prompt; fill it from the character's canon file
(build, clothing, signature details) and submit. The character then carries
both a Portrait and a Body reference, and `@name` casting draws on both.
Live-validated 2026-08-11 on Carrier (workshop full-body shot, correct navy
jumper + green darn + glasses-on-cord, matched canon on the first try).

**Model: Nano Banana Pro is now the automatic default** (`DEFAULT_MODEL` in
`flow-client.ts`, overridable per call or via `FLOW_MODEL`). Flow's picker
resets to Nano Banana 2 on every navigation, so the client re-asserts the model
on each generation rather than once per session. Pro is visibly sharper;
confirmed live 2026-08-11 on the Keynes portrait re-run.

### Tooling built 2026-08-11 — no more hand-driving the browser

The first two castings were done by hand through Playwright because the
character tools were broken; ~90% of that time went on DOM round-trips rather
than generation. That knowledge is now encoded in `@badcode/flow-mcp`, so each
of these is **one call, no browser steps**:

| Tool | Does |
| --- | --- |
| `flow_create_character` | Now takes optional `body`, `info`, `model` — casts the character *and* runs the native Create Body pass *and* fills Character Info in a single call. |
| `flow_character_body` | Adds the full-figure Body view to a Portrait-only character. |
| `flow_edit_character` | **Iterate on an existing character in place** — delta prompt against its Portrait or Body, preserving the bound identity instead of re-casting. |
| `flow_character_info` | Sets the free-text note Flow's scene agent reads. |

Full selector map and the failure modes behind each fix:
[`docs/flow/automation-images.md`](../docs/flow/automation-images.md)
("Characters, re-mapped live 2026-08-11"). Pure bits are unit-tested in
`compose.ts` / `compose.test.ts`.

**Character iteration loop (the standing workflow):** show Kai the current
Portrait/Body → he names the change in plain words → one `flow_edit_character`
call → show the result. No regeneration from scratch, no re-upload, and the
editor's own *Show history* is the undo.

**Character-sheet experiment (2026-08-11): a single `flow_edit_image` call
asking Flow to composite a 3-view (front/side/back) turnaround from one
portrait reference produced nothing** — no new candidate landed in the
gallery, consistent with either a policy block or a hard compositing-capability
limit (not just slow; waited well past the timeout with no result). Don't
retry this shape blind. **What works instead: Portrait + native "Create
Body"** — two separate, single-subject generations, each reliable. If deeper
angle coverage is ever needed, the fallback is N separate single-image
generations (front/side/back as distinct calls) fed together into
`flow_create_character`'s `refImages` array — untested but structurally sound,
since that array accepts multiple images by design.

Record Character ids/names in each prompts.md §2 table. **Gate: Kai approves
both characters before Phase 2.** Present candidates as a private contact-sheet
artifact (image + filename + which prompt), so approval is one glance.

## Phase 2 — scenes (background agent, serial, two waves)

Save candidates to a staging dir next to each target
(`…/storyboard/img/_candidates/<asset>-{a,b}.jpg`); the accepted candidate is
moved to the canonical path from prompts.md at gate time. After every asset:
append a revision line + Flow media id to its prompts.md entry (the ledger is
the memory — this is not optional).

**Wave 1 — anchors and independents** (~25–35 min browser time):

- GPOM: cover (variant **A2** — v2 corrections), s06, s07, s08, s09, s10,
  **s11-coin (TOTEM LOCK)**, s12, s14, s15, s17, s19, s20.
- MMT: **cover variant A (bench+tree ANCHOR)**, b02-ascent,
  **b03-hollow-fruit (courtyard anchor)**, b03-rentenmark, b03-counterfeit,
  b09-mulberries.

**Gate:** ping Kai with a contact sheet; Kai accepts/rejects per asset.
Rejections loop (rewrite or `flow_refine`) before wave 2 — wave 2 derives from
accepted anchors, so no anchor, no derivation.

**Wave 2 — derivations** (each `flow_edit_image`, exactly one reference,
downscaled, always from the accepted golden):

- GPOM from s11 coin: s13-empty-chair, s16-coin-lands (the payoff — must read
  as the same coin).
- MMT from cover: b02-bench-1942 (@Keynes), b05-empty-bench,
  b09-winter-bench (@Keynes).
- MMT from b03-hollow-fruit: b03-not-to-drop (same courtyard).

**Open question for wave 2:** `flow_edit_image` binds geometry but (assume) not
a Character; `flow_generate_image` binds the face but not the bench. The bench
prompts keep Keynes distant and face-unreadable, so default to **edit_image
(geometry wins)**; fall back to generate+character only if a shot reads wrong.
Decide per-shot at the gate, note the choice in the revision line.

**Final gate:** contact sheet of wave 2 → acceptances → move files into place →
commit (commits auto-push; treat as publishing).

## Execution shape in the harness

**All of it runs live in the driving session, foreground, not delegated to a
background agent.** Since one logged-in browser is strictly serial anyway,
there's no throughput to gain by backgrounding it — and running foreground
keeps Phase 1 and Phase 2 as one continuous interactive conversation: generate
(a character, or a wave's worth of scene candidates), stop, show the contact
sheet, get a yes/no/rewrite, move on. No pings, no separate background-agent
handoff. Do not use a multi-agent Workflow — one browser, no parallelism to
exploit.
