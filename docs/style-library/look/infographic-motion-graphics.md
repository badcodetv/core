---
slug: infographic-motion-graphics
name: Infographic and data motion graphics
kind: look
family: Graphic and digital animation
checked: 2026-10-28, references and engine notes (see Web check)
---

# Infographic and data motion graphics

> Charts, maps, icons, figures and typography animated to show an economic argument as a moving diagram.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

The explainer tradition: animated data and diagrams that make an abstract system visible. Its lineage runs from Isotype pictograms in the 1930s through title design to Hans Rosling's moving bubble charts in the BBC's The Joy of Stats (2010), RSA Animate's hand-drawn whiteboard talks (2010), and independent explainers. For economics it is the most direct form: money flowing between boxes, queues of icons, a bar that keeps growing. Money as Debt (Paul Grignon, 2006) is an early online example of an animated argument about the money system. Its strength is clarity and authority, its weakness is that data does not feel like a story.

## Signature traits

- Flat vector shapes, icons and pictograms on a plain or lightly textured ground
- A tight palette of 3 to 5 colours with one accent colour reserved for the problem (e.g. red for the part being taken)
- Animated charts: bars growing, lines drawing, bubbles moving across axes, counters ticking up
- Typography as a main element: large numerals, labelled arrows, kinetic text timed to the narration
- Maps and diagrams that zoom, pan and re-label; flows drawn as moving arrows or particle streams
- Simple 'ease in, ease out' motion on shapes: slide, scale, wipe, with clean timing and no extraneous movement
- One idea per shot, and every shot ends on a clear labelled state
- Optional human-hand drawing layer (whiteboard) with a marker hand sketching as the narrator speaks

## References

- *The Joy of Stats: '200 Countries, 200 Years, 4 Minutes'* — Hans Rosling / BBC Four, 2010. The standard for moving data as storytelling: animated bubbles showing inequality and growth over two centuries. **(Corrected: The 4-minute clip is from the BBC Four documentary The Joy of Stats (2010), presented by Hans Rosling; fine as stated, but the film's maker is Wingspan Productions for BBC; clip is commonly titled '200 Countries, 200 Years, 4 Minutes'.)**
- *RSA Animate: 'Changing Education Paradigms'* — Cognitive Media (Andrew Park) for the RSA, 2010. Hand-drawn whiteboard animation timed to a spoken argument; the model for drawing-while-talking.
- *Money as Debt* — Paul Grignon, 2006. An independent animated explainer on how the money supply is created, showing the form can reach a mass online audience.
- *The Story of Stuff* — Annie Leonard / Free Range Studios, 2007. Simple illustrated animation making a systems argument about production and waste to millions of viewers.

## What it carries

Clear, authoritative, impersonal, cool. It carries the 'here is how the trick works' register superbly and gives sarcasm a natural deadpan home in a mock-neutral chart. It fights against emotion and character: nobody cries at a bar chart.

## What it suits, and what it would undermine

Strong for: the mechanism beats, e.g. where the money goes, how a rent rise compounds, who owns what; for short inserts inside a different main style; and for building trust in a number. It would undermine: a whole film told in this style with no people, and any claim not backed by a real figure, since an invented number dressed as data is a credibility trap with this audience.

## Asking Flow (Nano Banana stills, Veo clips) for it

Describe as design: 'flat vector infographic style, clean icons and pictograms on a plain off-white ground, limited palette of navy, grey and one red accent, large bold sans-serif numerals, labelled arrows, bar chart with three bars of rising height'. Nano Banana renders legible text and clean shapes better than most image models, so supply the exact words you want ('£4.2bn', 'RENT') in quotes and keep them short. For Veo: 'clean motion-graphics animation, bars grow upward, elements slide in with ease, locked camera, no morphing of text'. Avoid: 'photorealistic, 3D render, clutter, decorative gradients, stock-photo people, paragraphs of text'. The reliable route is to generate only the style frames and icons in Flow and build the animation and all the numbers in Premiere or with code (ffmpeg drawtext, or a chart rendered from real data) rather than asking Veo to animate figures. Suno side: describe 'minimal electronic pulse, plucked synth, soft click percussion, ticking clock' for a data-explainer bed.

## How generators get it wrong

The image model will invent data: bars with no consistent scale, labels that do not match the shapes and numbers that look plausible but mean nothing; never rely on a generated chart for a real figure. Text accuracy decays with length, so keep labels to a few words. Veo morphs text and numerals while animating (digits change shape mid-clip), redraws bars wrongly and adds camera movement. The 'corporate flat people' look (the oversized-limbs vector style used by tech companies) is the default and reads as bland, and it is easy to drift into. Fix: build charts from real data in code, use Flow for style plates and icons only, and set type in post.

## Production cost

Low in generation but needs real design/assembly effort: the reliable approach is a template (palette, type, icon set) applied by hand or script to each shot. Consistency is excellent when the elements are built in post. Every figure needs a source, so research cost is higher than for any other style here.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.
