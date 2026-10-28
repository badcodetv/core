---
slug: risograph-two-colour
name: Risograph limited-colour print
kind: look
family: Print, poster and illustration
checked: 2026-10-28, references and engine notes (see Web check)
---

# Risograph limited-colour print

> Grainy, overprinted two- or three-colour illustration in fluorescent pink, blue, yellow, with deliberate misregistration.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

Riso printing is a stencil-duplicator process that lays down one spot ink per pass, so images are built from two to four layers of vivid ink whose overlaps create new colours. It became the look of independent zines, small-press comics and event posters in the 2010s. Its imperfections (grain, off-register layers, patchy fills) read as handmade and cheap, which is its political advantage: it looks like something the people made, not something a corporation bought.

## Signature traits

- Two to three flat spot inks only, e.g. fluorescent pink, teal-blue, sunshine yellow
- Overprint where colours overlap, producing a third dark tone (multiply blend look)
- Grain/halftone texture in fills; speckled, uneven ink density
- Layers off-register by a few pixels so outlines don't quite meet colour fills
- Uncoated, slightly warm paper tone
- Flat shapes, minimal outlines, simple geometric figures and bold type blocks
- Limited tonal range; no black unless an explicit third ink

## References

- *Spider-Man: Into the Spider-Verse* — Sony Pictures Animation, 2018. Mainstream film that uses halftone dots and deliberate colour misregistration as its look; shows the style in motion.
- *Hilda and the Troll (Hildafolk)* — Luke Pearson / Nobrow, 2010. Small-press picture-comic with a restricted overprinted palette in the riso-adjacent independent print mode. **(Corrected: Published 2010 by Nobrow as Hildafolk; retitled Hilda and the Troll in 2013 (Flying Eye). Year 2010 is for Hildafolk.)**
- *Kingdom* — Jon McNaught / Nobrow, 2014. British graphic novel of flat, limited-palette overprinted colour; shows how a limited palette can sustain a whole story. **(Unconfirmed on the web.)**
- *Print Club London riso poster output* — Print Club London, 2010s. UK print studio whose riso posters and zines define the contemporary look; useful as a visual reference rather than a single work. **(Unconfirmed on the web.)**

## What it carries

Warm, wry, DIY, youthful, punky-but-friendly. It carries satire, absurdity and quiet melancholy well. It fights against grandeur, scale and anything that needs realistic light.

## What it suits, and what it would undermine

Short, sharp satirical bits aimed at a young-to-middle reader: the cost-of-living joke, the landlord, the zero-hours contract. Cheap-looking is a feature: 'we made this ourselves'. It would undermine epic, monumental or horror-tinged material, and it is the wrong tone for a story that needs authority.

## Asking Flow (Nano Banana stills, Veo clips) for it

Nano Banana follows palette instructions well when colours are named exactly and limited: 'risograph print, only three inks: fluorescent pink, cobalt blue and yellow, overprint where they overlap, grainy ink texture, slight misregistration, uncoated paper'. Flat vector-ish shapes and 'no gradients, no outlines except where a layer shows' help. Exclude: 'photorealistic, gradients, soft shading, glossy, 3D, black outlines, painterly, lens blur'. For video, ask for 'flat shapes slide in layers, like cut paper, locked camera' and keep clips simple; Veo will often add depth of field or lighting that breaks the three-ink palette.

## How generators get it wrong

The common failure is the 'riso filter' look: a clean vector illustration with a noise overlay and gradients that a real riso could not print. Extra colours leak in (a fourth tint, black outlines, skin tones) and the overprint logic is faked with transparency that doesn't multiply. Fix by restating the ink count in every prompt and rejecting any plate with a colour outside it. In video, palette drifts after a few seconds and grain reads as digital noise that crawls.

## Production cost

Cheap in stills and very cheap to keep consistent, because a three-ink palette plus flat figures is easy to hold with a reference image. Motion works better than most print styles if you animate in layers in Premiere (slide, scale, fade), but Veo-generated motion tends to drift off-palette, so prefer short held shots with graphic transitions.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.

**Correction:** No separate negative field in Nano Banana; exclusions are prose inside the prompt. Palette-locking by naming exact inks is reasonable but undocumented.

Sources:
- <https://en.wikipedia.org/wiki/Hilda_(graphic_novel_series)>
