---
slug: silhouette-shadow-animation
name: Silhouette shadow animation
kind: look
family: Hand-made animation
checked: 2026-10-28, references and engine notes (see Web check)
---

# Silhouette shadow animation

> Black cut-out figures on a glowing, coloured backdrop, with delicate lace-like detail and no interior faces.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

Pioneered by Lotte Reiniger in Germany in the 1920s, silhouette animation moves black jointed figures cut from card or lead foil on a back-lit glass table, shot from above, with coloured layered backgrounds. Because faces and interiors are absent, everything is told through outline, gesture and composition. Modern versions, notably by Michel Ocelot, use black silhouettes against richly coloured, ornamental tableaux. The look is graphic, fairytale and slightly formal.

## Signature traits

- Pure black figures with no interior detail, defined only by outline and fine cut-out lacework
- Back-lit translucent backgrounds in flat, glowing washes (amber, teal, rose) with paper-layer stratification
- Delicate fringe, filigree and pattern in clothing, foliage and architecture
- Gesture-driven acting: tilted heads, hands and posture carry emotion since there are no faces
- Strong horizontal staging, like a shadow theatre, with minimal camera movement
- Slight tremble of edges and joint-based movement of limbs
- Ornamental frames or borders and stage-like proscenium composition
- Silhouetted crowds that read instantly as masses

## References

- *The Adventures of Prince Achmed* — Lotte Reiniger, 1926. One of the oldest surviving feature-length animated films, defining the technique.
- *Princes and Princesses* — Michel Ocelot, 2000. Modern silhouette fables against rich coloured backdrops, with short parable-like stories.
- *Tale of the Fox / The Tale of the Fox* — Ladislas Starevich (with Irene Starewitch), 1937. Not silhouette itself, but a European puppet fable, useful for the fable register; included only as a cousin, so treat as secondary. **(Corrected: Starewicz's Le Roman de Renard (The Tale of the Fox): animation completed 1929-30, first released 1937 in Germany (UFA soundtrack), French release 1941. The 1937 date is defensible as first release; some sources say 1930 or 1941. Maker credit with Irene Starewitch is correct.)**
- *Azur & Asmar* — Michel Ocelot, 2006. Ocelot's richly ornamented work, helpful for seeing the lineage of the ornamental graphic approach. **(Corrected: Azur & Asmar (2006, Ocelot) is a CGI feature with ornamental flat design, not silhouette. As a lineage cousin only.)**

## What it carries

Fable-like, timeless, elegant and slightly sad; very good for allegory and mass scenes, faceless and anonymous in a way that can be chilling. It fights against close emotional drama, specific modern settings and anything needing recognisable faces, speech sync or brand logos.

## What it suits, and what it would undermine

Strong for parables about the many versus the few: crowds as black shapes, a tiny figure beneath a giant building, ownership and power as shadows. Faceless figures sidestep the problem of generating consistent characters and let any viewer fill in the face. It undermines contemporary, specific satire (named politicians, real brands, everyday kitchens) because the fairytale register floats everything into myth.

## Asking Flow (Nano Banana stills, Veo clips) for it

Nano Banana: 'silhouette cut-out animation, solid black paper figures with intricate lace-like cut details, no facial features, back-lit coloured paper backdrop in layered amber and teal washes, shadow theatre composition, flat staging'. Describe the layers by name (foreground black trees, mid-ground pale hills, glowing sky). Exclude 'gradient shading inside the figures, face details, realistic lighting, 3D, outline strokes, cel shading'. For Veo, 'silhouette puppet animation, rigid jointed black figures moving across a lit backdrop, minimal parallax, locked camera'. Keep one or two figures per clip.

## How generators get it wrong

Image models add interior detail, rim light, gradients or faces to supposedly pure silhouettes, and often drift to generic vector fantasy art or Disney-style flat illustration. Veo smears the black shapes and gives the figures fluid, rubbery motion and extra limbs, especially in crowds. Fix by repeating 'solid black, no interior detail', using single clear actions and locked camera, and compositing the layers in editing. Fine lacework gets blurred at video resolution.

## Production cost

Low to medium. Silhouettes hide the usual consistency problems, since a recognisable outline and costume shape suffice. Layered compositing in Premiere gives the cleanest result. The main costs are crowd shots, where Veo muddies shapes, and making the fine cutwork readable after compression.

## Web check (2026-10-28)

Engine notes: contradicted by what the checker found.

**Correction:** Flow has no negative-prompt or exclude field; repeat positive constraints ('solid black, no interior detail') and list unwanted elements inside the prompt. Everything else is plausible but untested.
