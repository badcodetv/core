---
slug: charcoal-erasure-drawing
name: Charcoal drawing and erasure animation
kind: look
family: Hand-made animation
checked: 2026-10-28, references and engine notes (see Web check)
---

# Charcoal drawing and erasure animation

> A single charcoal drawing continually redrawn and smudged, so each frame leaves ghost traces of what was there before.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

A less obvious technique associated with the South African artist William Kentridge from the late 1980s. He makes one large charcoal and pastel drawing, photographs it, then erases and alters parts of it before photographing again, leaving smeared ghost marks of earlier states. Paper, charcoal dust and the history of every change stay visible. It is a political animation tradition, used to depict apartheid-era Johannesburg, mining capital and violence, with occasional flashes of red or blue pencil and cut-in documentary footage.

## Signature traits

- Black charcoal lines and heavy smudged tonal areas on cream paper
- Ghosting: pale residue of earlier drawings visible under the current one after erasure
- Occasional single colour accent (red or blue pencil) against monochrome
- Rough, gestural lines with visible hand pressure and rubbed-out edges
- Low, irregular frame rate with each state held for a beat, giving a flicker
- Transforming objects: a telephone becomes a bird, a landscape becomes a mine
- Frame framed like a drawing on a wall, sometimes with the artist's hand or the paper edge visible
- Landscape and architecture treated as heavy tone, with small figures

## References

- *Johannesburg, 2nd Greatest City After Paris* — William Kentridge, 1989. The first of the Soho Eckstein and Felix Teitlebaum films, a charcoal animation about property, wealth and apartheid-era inequality.
- *Mine* — William Kentridge, 1991. A mine owner in bed while the mine's workers are shown below ground, a direct image of capital and labour, which is the core of the BadCode argument.
- *Felix in Exile* — William Kentridge, 1994. Mixes erasure animation with survey and landscape imagery to depict erased history.
- *Stereoscope* — William Kentridge, 1999. Shows the later, more complex use of the technique with doubled images and moving charcoal.

## What it carries

Serious, haunted, political, with dry bitterness; capable of grim comedy through transformation and understatement. It fights against cuteness, brightness, bounce and fast-moving jokes.

## What it suits, and what it would undermine

Strong for stories about capital, property and labour where the argument needs gravity: a rich man and a worker, a mine, a housing market, the erasure of a community. The ghosting of prior states literally visualises what has been removed. It is a poor fit for light comedy, character-driven farce and anything meant to look warm and cosy, and it risks seeming art-gallery solemn to a pub audience unless the script is plain and punchy.

## Asking Flow (Nano Banana stills, Veo clips) for it

Nano Banana: 'charcoal drawing on cream paper, heavy smudged black tonal areas, visible erased ghost marks, gestural rough lines, a single red pencil accent, drawn by hand, paper grain, edge of the paper visible, no colour except one accent'. Exclude 'digital illustration, clean vector lines, gradients, colour, comic book inking, photographic'. For Veo, 'charcoal animation, drawing is repeatedly erased and redrawn, smudge trails, low frame rate flicker, locked camera on the sheet of paper'. For best results use two-state clips: start frame and end frame images with a smudged transformation between them (image-to-video with first and last frame).

## How generators get it wrong

Image output usually comes out as clean digital sketch or engraving-style illustration with crisp even lines, losing the dusty smudge and ghost marks. Veo tends to animate as smooth crossfade or live drawing-on with a hand, rather than erase-and-redraw states. Fix by using start-and-end frame images, each prepared to show ghost residue, and by adding a low frame-rate flicker in post. Over-long clips drift into generic moving sketch.

## Production cost

Medium. A monochrome palette and loose drawing hide consistency problems, and the first-and-last frame workflow gives good control for transformations. The cost is in preparing deliberate pairs of stills and in resisting the default clean-sketch look. Dialogue is not natural here, so narration over images is the intended mode.

## Web check (2026-10-28)

Engine notes: contradicted by what the checker found.

**Correction:** Flow has no negative-prompt or exclude field; describe the charcoal look positively and list unwanted elements inside the prompt. First-and-last-frame video in Flow does exist and is a sensible approach.
