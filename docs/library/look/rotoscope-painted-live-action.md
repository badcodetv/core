---
slug: rotoscope-painted-live-action
name: Rotoscope / painted-over live action
kind: look
family: Hand-made animation
checked: 2026-10-28, references and engine notes (see Web check)
---

# Rotoscope / painted-over live action

> Live-action footage traced or painted over frame by frame, so real movement wears a wobbly drawn skin.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

Rotoscoping, patented by Max Fleischer in 1915, traces animated lines over filmed performance. Modern versions use digital paint-over (as in Richard Linklater's films) or painted frames in oils (as in Loving Vincent). Real human timing and gesture remain, but surfaces swim and boil: lines wobble, colours slide across faces, and backgrounds shimmer. It produces an unsettled, dreamlike hyper-real feeling that sits between documentary and cartoon.

## Signature traits

- Real human body mechanics and facial timing under a loose drawn or painted skin
- Wobbling, boiling contour lines and flat colour patches that shift every frame
- Colour fields that slide independently of the underlying forms (a face-colour layer drifting off the head)
- Fluid, naturalistic camera moves (walks, handheld, dolly) that animation rarely affords
- Backgrounds that shimmer and swim more than foreground figures
- Muted, limited palette or a vivid, hallucinatory palette depending on treatment
- Often long conversational takes in ordinary rooms and streets
- Painted brushwork visible when each frame is an oil painting

## References

- *A Scanner Darkly* — Richard Linklater, 2006. Feature-length digital rotoscope of a dystopian surveillance story, showing how drifting paint-over suits paranoia.
- *Waking Life* — Richard Linklater, 2001. Many artists each paint over the same footage, so the look changes scene to scene, showing the technique's flexibility.
- *Take On Me (music video)* — a-ha, directed by Steve Barron, 1985. Pencil-sketch rotoscope hand-drawn over live action, a famous British-produced example.
- *Loving Vincent* — Dorota Kobiela and Hugh Welchman, 2017. Every frame an oil painting over filmed actors, the painted extreme of the approach.

## What it carries

Uneasy, intimate, dreamy and slightly paranoid; excellent for conversation, surveillance and unreliable reality. It fights against crisp slapstick, bold graphic punchlines and cuteness.

## What it suits, and what it would undermine

Fits stories where real behaviour matters: a council meeting, a call centre, a job interview, a surveillance-and-debt thriller. The drifting skin reads as 'this is real people but something is off', suitable for stories about systems quietly eating normal lives. It undermines broad cartoon satire, and it depends on having live-action source footage or very convincing generated motion.

## Asking Flow (Nano Banana stills, Veo clips) for it

Nano Banana: 'rotoscope animation still, live action figure painted over with loose wobbling ink contour lines and flat colour fills that slightly misregister the shapes, digital paint-over, visible brush or pen texture, muted limited palette'. For video, Veo can be asked for 'rotoscoped animation look, boiling outlines, flat colour patches, hand-traced from live action', but the best route is to generate a realistic clip first, then apply an edge-and-posterise or paint filter in post (ffmpeg or Premiere) to create the drifting colour fields. Exclude 'photorealistic skin, smooth gradients, CGI sheen, anime, 3D'.

## How generators get it wrong

Veo largely ignores the temporal wobble that defines this look and gives either clean photoreal footage or a stable cartoon with no boiling. The image model produces polished digital illustration rather than loose tracing. Fix by treating the style as a post-processing layer applied to realistic generated footage, and accepting that the 'sliding colour' effect needs filters or an editor's help. Faces also change identity between frames.

## Production cost

Medium to high. Needs realistic, consistent performances first (hard to keep character identity across takes), and then a filter pass that must be tuned per shot. Gives excellent realistic movement for free, but dialogue shots depend on lip-sync from generated or recorded footage.

## Web check (2026-10-28)

Engine notes: contradicted by what the checker found.

**Correction:** Flow has no negative-prompt or exclude field; describe the wanted painted look positively and list unwanted traits inside the prompt. The advice to generate realistic footage and apply a post filter is sensible and plausible-untested.
