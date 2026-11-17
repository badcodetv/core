---
slug: low-poly-ps1-3d
name: Low-poly and PS1-era 3D
kind: look
family: Graphic and digital animation
checked: 2026-10-28, references and engine notes (see Web check)
---

# Low-poly and PS1-era 3D

> Chunky, faceted 3D with few polygons, flat-shaded or affine-warped textures, low resolution and a wobbling, unfinished feel.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

The look of 1990s console 3D (PlayStation, N64) and its modern revival. Early hardware had very few polygons, no perspective-correct textures (so textures swim and warp), vertex 'jitter', low-resolution textures and hard fog to hide the draw distance. A second branch is clean flat-shaded low-poly as a design choice (Superhot, 2016). Contemporary games have turned these limits into a style for horror, dread and bleak comedy. It is low-fi on purpose, which can make a systemic, impersonal world feel eerie and cheap in a way that suits some stories.

## Signature traits

- Visible polygon facets; characters made of a few dozen to a few hundred triangles, blocky hands, simple faces
- Low-resolution textures with sharp pixels and heavy dithering, sometimes affine texture warp on large surfaces
- Flat or vertex-lit shading with no soft shadows; hard, simple lighting
- Heavy distance fog in a single flat colour, with pop-in at the edge
- Limited colour palette and 15-bit-style colour banding
- Low-resolution frame (320 by 240 look) upscaled with hard pixel edges, sometimes with CRT scanlines or interlace
- Wobbly vertex jitter and stiff, simple animation with few keyframes
- Static, locked camera angles or slow, clumsy orbits

## References

- *Final Fantasy VII* — Square, 1997. The classic blocky low-poly character look, plus pre-rendered backgrounds, on original PlayStation hardware.
- *Crash Bandicoot* — Naughty Dog, 1996. Cartoon-friendly PS1 low-poly with vertex colours and simple lighting.
- *Superhot* — Superhot Team, 2016. Deliberate flat-shaded low-poly, with white, black and red as the entire palette; shows low-poly as stylish minimalism.
- *Lethal Company* — Zeekerss, 2023. A recent example of the PS1-style revival used for dark corporate-labour comedy, with workers sent into dangerous sites to meet quotas.

## What it carries

Eerie, cheap, nostalgic, deadpan and unsettling. It suits bleakly funny or dread-filled worlds and gives faceless institutions a hollow look. It fights against warmth, subtlety and human faces; no one will cry at a 200-triangle face.

## What it suits, and what it would undermine

Strong for: the machinery of a system, with workers as interchangeable blocks; corporate, bureaucratic or dystopian settings; and a viewer who grew up on games. 'The company town as a level you can't finish' is a natural fit. It would undermine: any story needing a recognisable performance from a face, or an emotional close-up with a real person's grief.

## Asking Flow (Nano Banana stills, Veo clips) for it

Use technical retro-3D terms: 'low-poly 3D render, original PlayStation graphics, flat shaded faceted polygons, low-resolution pixelated textures, texture warping, vertex jitter, dithering, heavy single-colour distance fog, no soft shadows, 320 by 240 resolution upscaled with hard pixels'. Nano Banana knows the idiom well. For Veo: 'low frame rate, stiff animation with few keyframes, locked camera, slow orbit'. Avoid: 'smooth surfaces, subsurface scattering, ray tracing, high-poly, realistic shadows, motion blur'. A deliberate post step helps more than prompting: downscale the finished clip with nearest-neighbour filtering, drop to 12 to 15 fps and add dithering in ffmpeg, so the retro quality is exact. Suno side: describe 'MIDI-style synth strings, tracker-like arpeggios, 8-bit and 16-bit console sounds, sampled choir' rather than a game or composer name.

## How generators get it wrong

The engines produce 'polished game render' not true low-poly: curves come out smooth, textures are detailed, and the 'low-poly' reads as a stylised Unreal render with a few angular edges. Insist on triangle counts and hard-pixel textures, and fix in post by downscaling. In video, Veo smooths vertex jitter and adds motion blur and fluid movement that no PS1 game ever had, and it often adds realistic lighting shifts. Faces come out too expressive and too detailed. Consistency is better than most styles because the models are blocky and simple, but small shapes still change from shot to shot.

## Production cost

Low to medium. The simple shapes are forgiving and the lo-fi look hides small errors. The main work is the post-processing pass (downscale, frame-rate drop, dithering), which can be a repeatable ffmpeg recipe applied to every clip, giving a consistent finish.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.

Sources:
- <https://en.wikipedia.org/wiki/Superhot>
- <https://en.wikipedia.org/wiki/Lethal_Company>
