---
slug: machine-eye-street-view-cctv
name: Machine-eye photography (Street View, CCTV, dashcam)
kind: look
family: Photography traditions
checked: 2026-10-28, references and engine notes (see Web check)
---

# Machine-eye photography (Street View, CCTV, dashcam)

> Pictures taken by automated cameras with no photographer: blurred faces, stitched seams, timestamps and indifferent framing.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

Since the 2000s artists have mined images made by machines for their strange, accidental pictorial quality. Jon Rafman's The Nine Eyes of Google Street View (2011), Michael Wolf's A Series of Unfortunate Events (2011) and Doug Rickard's A New American Picture (2012) all treat Street View captures as street photography with no human behind the lens. CCTV and dashcam footage supply the same grammar: fixed wide angle, low resolution, timestamp overlays, fisheye distortion and unintentional drama. This is less an established genre than an emerging one, which is why it is the less obvious entry.

## Signature traits

- Fixed wide-angle or fisheye lens with barrel distortion and no composition intent
- Low resolution, compression blocks, blown highlights and murky shadows
- Timestamp, camera ID or watermark text burned into the frame corner
- Stitching seams, ghosted figures and doubled vehicles in panoramic captures
- Blurred faces and number plates from automatic privacy filters
- Static high or ceiling-mounted viewpoint looking down on shops, car parks, corridors and queues
- Washed-out colour, green or magenta cast in night vision, with infrared monochrome for dark scenes
- Human behaviour caught from a distance, absurd or sad because nobody is performing for the lens

## References

- *The Nine Eyes of Google Street View* — Jon Rafman, 2011. The first sustained art treatment of Street View captures as chance street photography.
- *A Series of Unfortunate Events* — Michael Wolf, 2011. Street View screenshots of accidents and odd moments, presented as a photo series.
- *A New American Picture* — Doug Rickard, 2012. Poor neighbourhoods rendered through low-resolution Street View, with the unsettling beauty of the medium.
- *Unfriended (feature film)* — Levan Gabriadze, 2014. A narrative film entirely told through screen capture, showing how machine-view formats can carry story.

## What it carries

Cold, voyeuristic, funny and uneasy. It carries surveillance, algorithmic management, automated decisions and the sense of being watched by something that does not care. It fights warmth and character intimacy.

## What it suits, and what it would undermine

Stories about workplace monitoring, warehouse and delivery gig work, benefit sanctions by algorithm, automated rent and credit decisions, or the superintelligence-from-the-future's own point of view. The BadCode premise is a machine looking back; this is how that machine would take pictures. Aim it at the people who deploy the cameras, not the technology. It undermines emotional performance scenes and hurts readability if the whole film is low-resolution.

## Asking Flow (Nano Banana stills, Veo clips) for it

Nano Banana can produce convincing versions of this when asked: 'CCTV still from a ceiling-mounted fisheye camera, low resolution, compression artefacts, timestamp text in the top-left, slight green cast, high angle, shop interior at night'. Keep overlay text short and simple; add or correct it in post. Negatives: 'no cinematic lighting, no shallow depth of field, no film grain, no beauty framing'. In Veo, ask for 'locked-off security camera, no camera movement, low frame rate feel, people move through the frame'. A static camera is what the model does most reliably, which makes this a cheap style to animate.

## How generators get it wrong

Generators make it look too good: crisp, well-composed and cinematic with a fake timestamp. A real machine view is badly framed, boring and low-quality, so say so. Overlay text and numbers are often garbled or inconsistent between shots. In video, models like to add camera motion and dramatic action, which breaks the grammar. Faces that should be blurred are often rendered sharply, so request obscured faces explicitly.

## Production cost

Cheap and consistent: a fixed camera and low quality hide many AI flaws, which is a real advantage. Character continuity matters little because faces are obscured. The cost is audience fatigue and clarity: it is hard to tell the audience who to care about, so it needs a narrator and cutaways to human-scale images.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.

**Correction:** Nano Banana has no negative field; write exclusions inline, preferably positively. Flow reportedly lacks a negative box. Garbled overlay text and Veo's static-camera reliability are plausible but undocumented.

Sources:
- <https://runware.ai/docs/models/google-nano-banana-2/guides/prompting>
- <https://www.veo3ai.io/blog/veo-3-negative-prompts-guide-2026>
