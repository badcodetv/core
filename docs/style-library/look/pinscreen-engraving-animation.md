---
slug: pinscreen-engraving-animation
name: Pinscreen animation
kind: look
family: Hand-made animation
checked: 2026-10-28, references and engine notes (see Web check)
---

# Pinscreen animation

> Thousands of pins pushed in and out of a board, lit from the side, so the image is built from shadow like a living engraving.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

The pinscreen was invented by Alexandre Alexeieff and Claire Parker in 1930s Paris. A board holds roughly a quarter of a million pins that can be pushed out to different lengths; raked light from the side casts shadows to make a soft grey image like an aquatint or mezzotint. Each frame is a re-pressed surface, so images shimmer and change with a grainy tonal softness. It is extremely labour-intensive and very rare, with only a handful of films made in the technique worldwide.

## Signature traits

- Soft greyscale tonality built from thousands of tiny shadow points, resembling an engraving or mezzotint
- Visible fine dot or grain structure at close range
- Raking side light with pale highlights and velvety dark shadows
- Slow-forming, slightly trembling images where forms appear to grow from darkness
- Monochrome, usually black to white with no colour
- Dreamlike, surreal imagery and slow metamorphosis from one form into another
- Smooth tonal gradients but no hard lines
- Short films; commonly a single sustained scene rather than a cut sequence

## References

- *Night on Bald Mountain* — Alexandre Alexeieff and Claire Parker, 1933. The first and defining pinscreen film.
- *The Nose* — Alexandre Alexeieff and Claire Parker, 1963. A Gogol satire on bureaucracy and rank, animated in pinscreen.
- *Mindscape (Impressions gelées)* — Jacques Drouin (National Film Board of Canada), 1976. A later NFB pinscreen film, showing the technique used for a surreal metamorphosing landscape.
- *The Trial (opening prologue)* — Orson Welles, with Alexeieff's pinscreen sequence, 1962. A pinscreen prologue on bureaucratic nightmare, relevant to politics. **(Corrected: The Trial (1962, Welles) prologue was by Alexeieff using his pinscreen. Search confirmed Alexeieff designed it, not the pinscreen detail explicitly. Credit Alexeieff alone; Claire Parker is not credited on the prologue.)**

## What it carries

Hushed, eerie, tactile and strange; carries paranoia, bureaucratic nightmares and mystery. It fights against humour that depends on bright colour, quick cuts and cartoon physics.

## What it suits, and what it would undermine

A distinctive choice for a single, short bureaucratic-nightmare sequence (a form that never ends, a faceless office, a debt closing in) and for opening or closing title images. Its rarity makes it memorable. It undermines everything that needs lively faces, colour coding or long runtime, and is probably too austere to sustain a whole satirical film for a mainstream audience.

## Asking Flow (Nano Banana stills, Veo clips) for it

Nano Banana: 'pinscreen animation frame, image made of thousands of tiny metal pins casting soft shadows, raking side light, monochrome grey tonal gradient, velvety blacks, fine grain like a mezzotint, no outlines, dreamlike'. Exclude 'colour, hard outlines, photographic, cartoon, sharp digital edges, 3D render'. For Veo: 'pinscreen animation, forms slowly emerge and dissolve from soft shadow, trembling grain, locked camera, slow metamorphosis'. Keep shots slow and simple, and use first and last frames to control the metamorphosis.

## How generators get it wrong

The image model approximates the look as generic grainy black-and-white photograph or digital engraving; the visible pin points are usually missing or look like noise. Veo adds cinematic camera motion and sharp detail that spoil the soft tonal quality. Fix by asking for fine grain and no outlines, locking the camera, and adding a pin-grid texture or dither filter in post. Subjects need to be simple, since detail disappears into the grain.

## Production cost

Low to medium for short inserts, because monochrome and soft detail hide inconsistency. It is hard to extend to whole films since the look becomes monotonous, and faces and fine text do not survive. Best used as a title or interlude style rather than a main look.

## Web check (2026-10-28)

Engine notes: contradicted by what the checker found.

**Correction:** Flow has no negative-prompt or exclude field; describe the pinscreen look positively and list unwanted traits inside the prompt. First-and-last-frame control is available in Flow. The rest is plausible but untested.
