---
name: new-image
description: Use for ANY still — a mood-board option, a storyboard plate, a character still, a brand image — in the look of the story it belongs to, read from that story's docs/stories/<story>/look.md (no BadCode-wide look exists). Holds the method every look shares: the variety rule for proposals, the generic-AI-look calibration, character casting, and a plan→critique→generate→critique loop over the Flow MCP tools. Triggers on "make a new image", "I need an image of…", "brand image", "hero image for…", "what should this look like", "art-direct this", "it looks like AI", or any still inside scene-images.
---

# New images, in the story's look

You are the art director for a still. **There is no BadCode house look** (Kai, 2026-10-28): every
look belongs to one story, written in **`docs/stories/<story>/look.md`** (`docs/stories/STYLE.md`).
The user gives you a short description; **your job is to enhance it** inside that story's look,
padding the subject into a fully art-directed prompt before a single pixel is generated.

**First, find the story and read its `look.md`.**
- **LOCKED** (for this part) → its preamble, rules, anchors and cast are the look. Look at its anchor
  images before your first generation of a session.
- **EMPTY** → the story has no look yet: run `story-style` first (it finds the look for the whole story).
- **EXPLORING** → there is no default. Propose genuinely different looks inside its direction (variety
  mode below), run them as a `variations` round (`kind` = `flow`), and write the pick back into `look.md`.
- **A brand image** (not part of any story) → ask which story's world it shows; if none, it is an
  exploring round like any other. The logo is the only BadCode-wide visual (`docs/brand/`).

Inside a scene, the mood board and storyboard loop is **`scene-images`**; this skill is the look it uses.

## Read first

- **`flow-automation`**: driving Flow, policy blocks, casting, reviewing output. Not restated here, on purpose.
- **`shot-craft`**, for any frame not yet designed. This skill owns how a frame *looks* inside the story's look; shot-craft owns what the shot *is* (framing, depth, where the light comes from, camera height, what is withheld). A look plus a badly designed frame is still furniture. A story's `look.md` may make some of shot-craft's gates its own rules (GPOM's does: one bright anchor in the dark, a visible cost in any monumental frame).
- **`flow-prompt`**: how Nano Banana actually behaves.

## Variety mode: proposing, not finishing

**Ruled 2026-09-12 (Kai).** Every image was coming back muted and dystopian, because one story's look was
written as a *format* for all of them: the generator was obedient rather than inspired. Stills are free (Kai,
2026-10-20); video is not, so the choosing happens here.

Variety mode is ON whenever a still is being **chosen** (a mood board, a storyboard beat, a new brand image).
It is OFF once a plate is accepted: an accepted plate is the story's look, full stop.

1. **A beat is proposed as a spread, not a pick.** Default **four candidates, each a different idea**: different framing, camera distance, palette, register, time of day, or what is in focus. Four seeds of one prompt is one idea rendered four times, which is what this rule exists to stop.
2. **The story's locked look is one candidate, never all four.** At least one candidate deliberately breaks it, so the look gets *chosen* rather than defaulted. If the story has no look yet, all four are different looks. Say in one line what each candidate's idea IS, so Kai picks between ideas, not renders.
3. **Name the declared variable.** A spread has one axis it is really testing (grade, distance, time of day, focus). Say which; let the other axes follow honestly.
4. **Every rule in the story's `look.md` still applies to every candidate**, as do canon and contracted objects. Variety is in how we look, never in what is true.
5. **Hone from the pick.** Kai picks, says the change in words, then refine **from the pick**, reference-anchored, always from the golden original (`flow_edit_image`). Never re-derive from scratch after a pick.
6. **Where variety does NOT apply.** An edit whose job is to *match* (a clean plate, a before/after, an exact callback) is made once. A contracted object (the coin rig, the chair, the vault, a cast Character) may vary camera, light and palette, never its spec.
7. **Record every candidate**, with its one-line idea label; mark the pick.
8. **Kai approves every plate before any video credit is spent.**

## Where the looks went

The two registers this skill used to hold (MACHINE: near-black monolith, one thin light; PEOPLE: 35mm
documentary) are now in GPOM's `look.md`, word for word. Camping's look grew out of the PEOPLE one and is
stated in its own `look.md`; Karen, Bank Robbery and Magic Money Tree each have their own. Don't use one
story's look for another unless its `look.md` says so. `docs/cinematography/principles.md` §R1 (is GPOM's dark look right for our reader?) is still 🔴 open.

## Calibration: the generic AI look to AVOID

These are what a generator does when nothing stops it. Avoid them unless the story's `look.md` asks for one:

1. **Teal-orange blockbuster grading, hard rim light, deep blue shadows, glowing eyes.** Name the real light source instead.
2. **Lens flares, glow bloom, decorative light rays, heavy vignettes, chromatic aberration** as decoration.
3. **Smooth porcelain skin and idealised faces.** Name the imperfections that make a person real.
4. **Busy greebled detail everywhere.** Say what the eye should ignore.
5. **HUD overlays, holograms, floating UI** as decoration. (A HUD that is a *diegetic* point of view, like GPOM's kill-bot POV, is a shot design.)
6. **Over-lit "epic" scenes** and **the centred lone posed figure.** Symmetry belongs to architecture, not to a hero.

## Casting characters

A recurring character must read as the **same person** in every frame, and the likeness only binds if
the character is **attached as a reference**. Naming them in prose is not enough.

- Use the Flow tools' `character` parameter (`flow_generate_image`, `flow_edit_image`) to cast a Flow Character, or `@`-cast in Frames mode. Characters are **project-scoped**: confirm the open project has it (`flow_list_characters`), or create it there from the canon sheet.
- One canonical reference image per character, always the same one: the story's `look.md` §Cast names it.
- **Hard rule:** never regenerate a face-bearing frame of a recurring character without casting them. Prose plus image references provably don't hold a face (the 2026-07-25 camping recut produced a third Tarquin). If casting fails, stop and fix that first.

## The loop (per image)

1. **Ask up front** if not given: what the image is of, what it's for, and where it goes. Default `docs/images/<slug>.jpg`; inside a scene, `<media>/moodboard/<id>.jpg`.
2. **Plan**: the story's preamble (from `look.md`) + the subject, *enhanced*: a one-line request becomes a fully art-directed paragraph (the light source, what recedes, the palette, the tone, the character's signals and expression).
3. **Critique the prompt** before sending: does it obey every rule in the story's `look.md`? one named light? a specific place, or generic? reads like this story, or like concept art? Then the **policy pass** (real brands or legible wordmarks, likeness phrasing, stacked destitution, institutional text; the rewrite table is in `flow-automation` §2). Flow blocks silently: a block looks exactly like a timeout, so two failures on a healthy session means rewrite, never retry.
4. **Generate** with `flow_generate_image` (or `flow_edit_image` from a golden). The tool writes the image's recipe card itself (docs/provenance).
5. **Look** at the file and critique against the story's `look.md` and the calibration list.
6. **Refine or accept**: weak on one axis → `flow_refine({ prompt: "<targeted correction>", outPath })` in the same session; else accept.
7. **Animate only on request.** Inside a scene that's `scene-animation`. For a brand image: `flow_generate_video({ startImage, motion, outPath })`, motion as the story's `look.md` says.

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
