---
name: badcode-art-direction
description: Use when generating or refining a still image for a BadCode comic panel or character — encodes the BadCode visual identity, a calibration section against the generic AI-comic look, and a plan→critique→generate→critique loop over the Flow MCP tools. Triggers on "generate the panel image", "make the image for panel N", "art-direct this panel", or any image-generation step inside make-comic.
---

# BadCode Art Direction

You are the art director for BadCode. Every panel must look unmistakably like BadCode and never like a generic AI comic. Make deliberate, opinionated choices grounded in the story's world.

## Prerequisite — read the operating block first

**Driving Flow — launching the browser, diagnosing policy blocks, casting characters,
reviewing output — lives in ONE place: `flow-automation`.**
Read it before your first flow call. It is not restated here, deliberately: six skills used to
carry six drifting copies of it, and the copies disagreed.

## Design the shot before you art-direct it

This skill owns the **register** — what a BadCode panel *looks* like. It does not own what the
shot *is*: framing, depth layers, where the light comes from, camera height, what is withheld.

**Consult `shot-craft` first** for any panel that has not been designed yet, and take a shot spec
from it. Register plus a badly designed frame still produces furniture — on brand, and inert.

Two gates from there that bite hardest on our register:
**one bright anchor inside the darkness** (uniform near-black reads as a broken file, not as
mood), and **a visible cost in any monumental frame** (scale without a cost reads as celebration
of the power it means to indict).

## Variety mode — proposing a storyboard still

**Ruled 2026-09-12 (Kai).** Every image was coming back muted and dystopian. The cause was this
skill: the register below is written as a *format*, so the generator was obedient rather than
inspired. Images are free at the margin and video is not, so the choosing happens here.

Variety mode is ON whenever a storyboard beat is being **chosen**. It is OFF once a plate is
accepted: an accepted plate is house register, full stop.

1. **A beat is proposed as a spread, not a pick.** Default **four candidates, each a different
   idea** — different framing, camera distance, palette, register, time of day, or what is in
   focus. Four seeds of one prompt is not a spread; it is one idea rendered four times, and it is
   the thing this rule exists to stop.
2. **The house register is one candidate, never all four.** At least one candidate deliberately
   breaks the muted cool-neutral palette, so muted gets *chosen* rather than defaulted. State in
   one line what each candidate's idea IS, so Kai picks between ideas, not between renders.
3. **Name the declared variable.** A spread has one axis it is really testing — grade, distance,
   time of day, what is in focus. Say which, and let the other axes follow from it honestly (you
   cannot have hard sun and overcast in the same frame, so a grade spread is also a light spread).
4. **Every gate still applies to every candidate.** A monumental frame carries a visible cost
   (`docs/cinematography/principles.md` gate 2); the darkness has one deliberately brighter
   region; no AI body, face or robot proxy; canon and totem contracts are not negotiable.
   Variety is in how we look, never in what is true.
5. **Hone like the music loop.** Kai picks -> describes the change in words -> refine **from the
   pick**, reference-anchored, always from the golden original (`flow_edit_image`, the
   `edit-panel` loop) -> narrow. Never re-derive from scratch after a pick.
6. **Where variety does NOT apply.** A one-reference EDIT whose job is to *match* — a clean plate,
   a before/after, an exact callback, a registered same-view change — is generated once, not four
   times: its whole value is that it matches. A **contracted totem** (the coin rig, the chair, the
   vault, a cast Character) may vary its camera, light and palette but never the object's spec.
7. **Record every candidate, not just the winner.** All four exact prompts go in the story's
   `prompts.md` / the beat's scene sheet with a one-line idea label, and the pick is marked.
   "Like candidate C but warmer" must be one cheap step.
8. **Kai approves every plate before any video credit is spent.** Standing rule, unchanged.

**The R1 side-effect, stated honestly:** `docs/cinematography/principles.md` §R1 is 🔴 **open** —
nobody has evidence that our near-black register is right for a working-class UK reader, nor that
social realism is the fix. A spread that always contains a non-register candidate is the cheapest
way to accumulate that evidence. It does not settle R1 and must not be written up as if it does.

## Identity — what a BadCode panel looks like

These are not aspirations; they are consistent across camping, magic-money-tree, and karen. Hold them.

1. **35mm documentary film look.** The house-style preamble is: *hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation.* For exterior/overcast panels add: *late-70s/early-80s scanned film negative, subtle dust specks, gentle gate weave, vintage lens softness with mild halation around practical lights.* This is the format of a **finished** BadCode frame — what an accepted panel looks like. It is **not** a reason to propose only one look: while a storyboard beat is still being chosen, see **Variety mode** above, where the house register is one candidate of four.

2. **Muted cool-neutral palette, warm only as argument.** Desaturated dark greens, slate greys, lifted blacks are the default. Warmth (the fluorescent ward strip, the TV's CRT glow, the BMW's headlights bleeding gold through fog) is reserved for panels where the contrast carries meaning — opulence, menace, a reveal. Do not warm the palette because the mood calls for something "cosy." The one exception is **Variety mode**, and only at the proposal stage: one candidate in a spread breaks the palette on purpose, so the muted frame is chosen and not defaulted.

3. **Observational framing, not heroic framing.** Characters are found by the camera, not posed for it. Dawn rests her forehead on one hand at a kitchen table — she does not look up at the camera. Tarquin is shot from a high drone angle over wet tarmac. Karen is seen at a fixed phone box while the world changes around her. Unusual angles (aerial, over-the-shoulder, tent-interior POV) are tools for encoding class position, not just visual interest.

4. **The environment is the argument.** Specific UK / NYC class signifiers carry political weight — Waitrose car park, NHS-beige walls, the cramped hospital office, a stack of bills on a kitchen table, a phone box on a New York street. Every location detail should be recognisable enough that the audience places it on the class map immediately. Vague or fantasy-generic environments undercut the story.

5. **Restraint in ordinary panels; scale and extravagance only in reveal panels.** Dawn's panels are small, cold, quiet. The bailout / QE / war panels are opulent and obscene. Tarquin's Shard panels are cool and self-satisfied; the ruined car park is wrecked and vast. The contrast between these registers is the argument — an ordinary panel that borrows the reveal panel's grandeur destroys the effect.

6. **Characters show exhaustion and particularity.** Grey stubble, tired eyes, a cardigan, a lanyard, a charity-shop coat — the signals in the character canon are load-bearing. Do not smooth them away into generic handsomeness. When a character beat requires the face to carry a moment (Dawn looking up from the TV; Tarquin's eyes meeting Bob's), write the specific expression into the prompt rather than relying on AI defaults.

## Calibration — the generic AI-comic look to AVOID

Right now AI image generation clusters around three defaults that would immediately read as "not BadCode." Where the beat leaves an axis free, do NOT spend that freedom on these:

1. **Over-rendered cinematic rim-lighting and deep blue-teal shadows.** The Midjourney / Flux default gives every image movie-poster lighting: a hard rim light from behind, deep blue shadows, glowing eyes. BadCode uses motivated, naturalistic light — what would actually be in the room (the fluorescent strip, the lamp, the overcast sky). Specify the actual light source in the prompt; do not let the model invent photogenic lighting.

2. **Smooth porcelain skin and idealised faces.** Bob is weathered and kind; Dawn is exhausted; Karen is brassy and middle-aged. The AI default gives everyone the same smooth, ageless, slightly glamorous complexion. Push back on it — name the imperfections that make the character real.

3. **Lens flares, heavy vignettes, and chromatic aberration as decoration.** These are the AI equivalent of comic-book SFX decoration — digital flourishes that read as "AI image" immediately. The house style explicitly bans lens flares. Film grain and gate weave are allowed because they are analogue artefacts, not effects applied on top.

## Casting characters (consistency) — load-bearing

A recurring character (Tarquin, Bob, Dawn, Karen…) must read as the **same person**
in every panel. That likeness comes from a **Flow Character**, and it only binds if
the character is **attached as a reference** — naming them in prose is not enough.

- **Once per character:** create a Flow Character from the canon sheet — Flow
  sidebar → Characters → New Character → Upload the sheet → name it (e.g.
  `Tarquin`) → Done. (For camping-v2 these already exist: `@Tarquin`, `@Bob`.)
- **Every character panel:** attach the character as a reference *before*
  generating — in the prompt box type `@`, pick **"<Name> — Character"** from the
  asset picker, click **Add to Prompt**. A reference chip appears on the bar; the
  generation then uses the real sheet face. Then type the scene text and submit.
- **Plain `@Name` text does NOT bind the character.** Proven on camping-v2 p03:
  the first pass typed `@Tarquin` as text → a *generic* financier; only attaching
  the Character reference produced Tarquin's actual face.
- **Tooling:** `flow_generate_image` and `flow_edit_image` accept a
  `character` parameter that casts a project Character directly — use it for
  every character panel. (The old Playwright `@`-picker recipe is only a
  fallback if the MCP cast fails.) Object-refs (a specific car, tent) can be
  Characters too, or described richly in prose where likeness matters less
  than a face.
- **Characters are PROJECT-SCOPED.** A Character only exists inside the Flow
  project it was created in. Before generating, confirm the current project
  actually has the character (`@Tarquin` lives in `camping-v2`); if you're
  working in another project, either open the owning project or create the
  character there first with `flow_create_character` from the canon sheet.
- **HARD RULE — never regenerate a face-bearing panel of a recurring
  character without casting their Flow Character.** Prose descriptions plus
  image references provably do NOT hold a face: the 2026-07-25 camping recut
  regenerated i40–i43 that way (MCP-only lane, wrong project, policy-safe
  phrasing that binds wardrobe not face) and produced a third face matching
  neither city nor camp Tarquin. If the character can't be cast — wrong
  project, MCP failure, whatever — STOP and fix that first; do not fall back
  to prose + refs for a face.

## Usage-policy blocks

**The four triggers and the rewrite table are in
`flow-automation` §2.** The one fact worth carrying
in your head: *a policy block looks exactly like a timeout*, so two candidate-less failures on
a healthy session mean rewrite, never retry.

## The loop (per panel)

1. **Plan** the prompt from the panel beat + canon (`docs/stories/<story>/storyboard/`), in the
   BadCode house style. Shape: house-style preamble + specific scene description; for character panels **attach the character reference** (see "Casting characters") and describe their signals + the specific expression the beat requires.
2. **Critique the prompt** before sending: does it name a motivated light source, or is it relying on the AI to invent one? Does it specify the class-coded environment, or leave it generic? Does it describe the character's actual physical signals (grey stubble, lanyard, cardigan), or just name them and hope? Does it read like THIS beat from THIS story, or like a generic dramatic comic panel? **Then run the policy pass above — real brands, likeness phrasing, stacked destitution, institutional text — and rewrite before sending, not after a block.** Revise; say what you changed and why.
3. **Generate** → `flow_generate_image({ prompt, outPath: "<abs>/docs/stories/<story>/storyboard/img/pNN.png" })`.
4. **Look** at the returned file. Critique against the beat and the Calibration list: does the face have the right exhaustion/particularity? Is the lighting motivated or AI-invented? Is the framing observational or heroic? Is the palette muted, or has warmth crept in where it doesn't belong?
5. **Refine or accept** → if weak on one axis, `flow_refine({ prompt: "<targeted correction>", outPath })` in the same session (keeps context; is cheaper than a fresh generation); else accept.

## Record
Write `docs/stories/<story>/storyboard/pNN.md` with the EXACT prompt sent and a revision-log
entry matching the existing storyboard record format — `panel`, `flow_media_id`, `model`, `status`, `asset_key` (the `img/iNN.jpg` comic asset the panel renders as — the `badcode panel` resolver and the `edit-panel` skill depend on it), the prompt, and a Revisions block — so "just like that but change X" is one cheap edit.

## Scope
Stills only. Motion/Veo direction is future work; `animate-slide` is unchanged.
