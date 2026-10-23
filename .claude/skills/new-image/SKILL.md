---
name: new-image
description: Use for ANY still in the BadCode look — a standalone brand image, a mood-board option, a storyboard plate, a character still — and the one home of the house look itself (2026-10-23 skills audit; it absorbed badcode-art-direction). Two registers (MACHINE: near-black monolith, one thin light; PEOPLE: 35mm documentary, observational, class-coded places), the variety rule for proposals, the generic-AI-look calibration, character casting, and a plan→critique→generate→critique loop over the Flow MCP tools. Triggers on "make a new image", "generate a BadCode image", "I need an image of…", "brand image", "hero image for…", "what should this look like", "art-direct this", "make it look like BadCode", "it looks like AI", or any still inside scene-images.
---

# The BadCode look, and new images

You are the art director for every BadCode still. Every image must look unmistakably like BadCode: a
transmission from the superintelligence's timeline, not sci-fi concept art and not a generic AI comic.
The user gives you a short description; **your job is to enhance it**, padding the subject into the
full register before a single pixel is generated.

Inside a scene, the mood board and storyboard loop is **`scene-images`**; this skill is the look it uses.

## Read first

- **`flow-automation`**: driving Flow, policy blocks, casting, reviewing output. Not restated here, on purpose.
- **`shot-craft`**, for any frame not yet designed. This skill owns how a BadCode frame *looks*; shot-craft owns what the shot *is* (framing, depth, where the light comes from, camera height, what is withheld). Register plus a badly designed frame is still furniture. Two gates bite hardest on our look:
  - **one bright anchor inside the darkness** (uniform near-black reads as a broken file, not as mood)
  - **a visible cost in any monumental frame** (scale without a cost reads as celebration of the power it means to indict).
- **`flow-prompt`**: how Nano Banana actually behaves.

## Variety mode: proposing, not finishing

**Ruled 2026-09-12 (Kai).** Every image was coming back muted and dystopian, because the register was
written as a *format*: the generator was obedient rather than inspired. Stills are free (Kai,
2026-10-20); video is not, so the choosing happens here.

Variety mode is ON whenever a still is being **chosen** (a mood board, a storyboard beat, a new brand image).
It is OFF once a plate is accepted: an accepted plate is house register, full stop.

1. **A beat is proposed as a spread, not a pick.** Default **four candidates, each a different idea**: different framing, camera distance, palette, register, time of day, or what is in focus. Four seeds of one prompt is one idea rendered four times, which is what this rule exists to stop.
2. **The house register is one candidate, never all four.** At least one candidate deliberately breaks the muted palette, so muted gets *chosen* rather than defaulted. Say in one line what each candidate's idea IS, so Kai picks between ideas, not renders.
3. **Name the declared variable.** A spread has one axis it is really testing (grade, distance, time of day, focus). Say which; let the other axes follow honestly.
4. **Every gate still applies to every candidate.** Visible cost, one brighter region, no AI body, face or robot proxy, canon and contracted objects unchanged. Variety is in how we look, never in what is true.
5. **Hone from the pick.** Kai picks, says the change in words, then refine **from the pick**, reference-anchored, always from the golden original (`flow_edit_image`). Never re-derive from scratch after a pick.
6. **Where variety does NOT apply.** An edit whose job is to *match* (a clean plate, a before/after, an exact callback) is made once. A contracted object (the coin rig, the chair, the vault, a cast Character) may vary camera, light and palette, never its spec.
7. **Record every candidate**, with its one-line idea label; mark the pick.
8. **Kai approves every plate before any video credit is spent.**

`docs/cinematography/principles.md` §R1 is 🔴 **open**: nobody has evidence that our near-black register is
right for a working-class UK reader, nor that social realism is the fix. A spread with a non-register
candidate gathers that evidence cheaply. It does not settle R1; don't write it up as if it does.

## Register 1, MACHINE: brand images and the AI's world

The anchor is [`docs/images/register-anchor.jpg`](../../../docs/images/register-anchor.jpg) (exact prompt in
[`register-anchor.md`](../../../docs/images/register-anchor.md)): a data-centre corridor in near-total darkness, racks
receding to vanishing point, one thin vertical blade of white light, constellations of status LEDs. **Look at
the anchor before your first generation of a session.**

1. **Darkness is the canvas.** Most of the frame is near-black, detail dissolving into shadow. What is lit is the argument.
2. **One thin light.** A single motivated source (a blade between racks, a slit under a vault door). The 2001-monolith nod: light as *presence*. Name it; never allow a second photogenic light the scene can't explain.
3. **Machine scale, cathedral framing.** Monumental geometry receding into black. Humans absent, or tiny enough to be a scale reference.
4. **Iconic composition is wanted here.** Symmetry and a centred vertical; the monolith stands in the middle.
5. **Muted cool-neutral; LEDs are the only colour.** Points of blue-white, amber, the rare red. No teal-orange, no colour washes.
6. **Received-from-the-future tone.** Evidence from the bad branch: calm, certain, already happened. If it looks like a movie poster, it's wrong.

Preamble:

> *hyper-realistic photograph, near-black exposure with deep unlifted shadows, a single thin motivated light
> source, monumental machine architecture receding into darkness, muted cool-neutral palette with tiny points
> of status-LED light, fine film grain, no lens flares, vast still symmetrical composition, calm observational tone*

## Register 2, PEOPLE: the documentary look (stories with humans in them)

Consistent across camping, magic-money-tree and karen. Hold them.

1. **35mm documentary film look.** Preamble: *hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation.* For exterior or overcast frames add: *late-70s/early-80s scanned film negative, subtle dust specks, gentle gate weave, vintage lens softness with mild halation around practical lights.*
2. **Warm only as argument.** Desaturated greens, slate greys, lifted blacks by default. Warmth (a fluorescent ward strip, a CRT glow, headlights gold through fog) only where the contrast carries meaning: opulence, menace, a reveal.
3. **Observational framing, not heroic.** Characters are found by the camera, not posed for it. Unusual angles (aerial, over-the-shoulder, a POV) encode class position, not just interest. Off-centre is the default here.
4. **The environment is the argument.** Specific UK class signifiers carry weight: a Waitrose car park, NHS-beige walls, a stack of bills on a kitchen table. Vague or fantasy-generic places undercut the story.
5. **Restraint in ordinary frames; scale only in reveals.** The contrast between registers is the argument; an ordinary frame that borrows a reveal's grandeur destroys it.
6. **Exhaustion and particularity.** Grey stubble, tired eyes, a lanyard, a charity-shop coat. Write the specific expression the beat needs; don't let AI defaults smooth it away.

## Calibration: the generic AI look to AVOID

Where the subject leaves an axis free, do not spend it on these:

1. **Teal-orange blockbuster grading, hard rim light, deep blue shadows, glowing eyes.** Name the real light source instead.
2. **Lens flares, glow bloom, decorative light rays, heavy vignettes, chromatic aberration.** Film grain and gate weave are allowed (analogue artefacts); flares are banned.
3. **Smooth porcelain skin and idealised faces.** Name the imperfections that make a person real.
4. **Busy greebled detail everywhere.** Most of a machine frame must actually be dark; say what dissolves into shadow.
5. **HUD overlays, holograms, floating UI.** The future here is racks, concrete and light. (A HUD that is a *diegetic* point of view, like GPOM's kill-bot POV, is a shot design, not decoration.)
6. **Over-lit "epic" scenes** and **the centred lone posed figure.** Symmetry belongs to architecture, not to a hero.

## Casting characters

A recurring character must read as the **same person** in every frame, and the likeness only binds if
the character is **attached as a reference**. Naming them in prose is not enough.

- Use the Flow tools' `character` parameter (`flow_generate_image`, `flow_edit_image`) to cast a Flow Character, or `@`-cast in Frames mode. Characters are **project-scoped**: confirm the open project has it (`flow_list_characters`), or create it there from the canon sheet.
- One canonical reference image per character, always the same one (the GPOM bot: `simulation/stills/s3/s3-bot-00b-a.jpg`, torn bunting kept).
- **Hard rule:** never regenerate a face-bearing frame of a recurring character without casting them. Prose plus image references provably don't hold a face (the 2026-07-25 camping recut produced a third Tarquin). If casting fails, stop and fix that first.

## The loop (per image)

1. **Ask up front** if not given: what the image is of, what it's for, and where it goes. Default `docs/images/<slug>.jpg`; inside a scene, `<media>/moodboard/<id>.jpg`.
2. **Plan**: the register's preamble + the subject, *enhanced*: a one-line request becomes a fully art-directed paragraph (the light source, what recedes, the palette, the tone, the character's signals and expression).
3. **Critique the prompt** before sending: one named light? darkness doing the work, or busy? class-coded place, or generic? reads like this story, or like concept art? Then the **policy pass** (real brands or legible wordmarks, likeness phrasing, stacked destitution, institutional text; the rewrite table is in `flow-automation` §2). Flow blocks silently: a block looks exactly like a timeout, so two failures on a healthy session means rewrite, never retry.
4. **Generate** with `flow_generate_image` (or `flow_edit_image` from a golden). The tool writes the image's recipe card itself (docs/provenance).
5. **Look** at the file and critique against the register and the calibration list.
6. **Refine or accept**: weak on one axis → `flow_refine({ prompt: "<targeted correction>", outPath })` in the same session; else accept.
7. **Animate only on request.** Inside a scene that's `scene-animation`. For a brand image: `flow_generate_video({ startImage, motion, outPath })`, motion minimal and reverent (a slow push-in, LEDs flickering, the blade breathing).

## Record

Inside a scene, the record is the scene's `moodboard.json` row plus the recipe card. For a brand image,
write `<slug>.md` next to it with the EXACT prompt, so "just like that but change X" is one cheap step:

```markdown
---
image: <slug>.jpg
flow_media_id:                 # filled when generated
model: nano-banana-2
status: planned                # planned | done
used_by:                       # where the image is deployed (page, post, film)
---

![<slug>](<slug>.jpg)

**Prompt (exact, sent to Flow):**

> <preamble + enhanced subject>

**Motion prompt (if animated):** _none_

**Revisions:**

- v1 (<date>) — initial
```

If a brand image lands outside `docs/images/`, add an index row to [`docs/images/README.md`](../../../docs/images/README.md),
the catalogue of all brand imagery wherever the file lives.

## History

Comic-panel art direction (the panel record format, `storyboard/pNN.md`) was archived with the comic skills on
2026-10-23: `.claude/skills-archive/comics/badcode-art-direction/`.
