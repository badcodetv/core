You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

keep experimenting with stills and stlyes, i want the rich fat cat to look ominous almost like a horror silent hill style Please clean room it all and research the internet to achieve it. Thanks.  thanks

## What happened in earlier rounds (facts)

Mood board round 1 (2026-11-12) showed nine takes on a 1910s pen-and-ink editorial cartoon look: a frosty park from above, a grease-crayon close-up of his dismissing hand, from behind the bench at noon, a flat-colour poster outside a hospital at night, him as an old cut-out in a rainy modern bus stop, over the nurse's shoulder, a banknote engraving portrait, a torn page 1919/today, him alone at sunset. Jack left no votes or notes on it.
Jack's next message, verbatim, is ask.md.

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- AI likeness of a real person.

## Never write these

The war is over my boy
Rollin Kirby
Kirby
Silent Hill
Pyramid Head
Konami

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

## What the picture shows

A BadCode Short, about 14 seconds, three beats. Mood board round 1: spread the round across all three beats (three stills per beat), each a genuinely different take on the look.

The art style: a 1910s pen-and-ink newspaper editorial cartoon (the inspiration is a 1919 Life magazine cartoon of a top-hatted fat cat on a park bench telling a one-legged soldier "The war is over my boy. Forget it."). Jack: use that art style, but change it so it is not a copy. Our own characters, poses, bench, park and composition; never recreate that panel.

Beat A (1919, the veteran): a park bench; a fat, top-hatted rich man sits beside a wounded soldier just back from the war (one leg, crutch). The rich man waves him off: "Forget it."
Beat B (today, the nurse): the same bench, the same rich man, identical and unaged, top hat and all; beside him now a tired nurse in scrubs. He waves her off the same way: "Forget it."
Beat C (the button): he hasn't aged a day. The same man, every time.

The rich man must look exactly the same in A, B and C (he becomes the reference for every later frame). Portrait 9:16. Leave room for a caption. No text or lettering drawn in the image.

Round 2 direction (Jack, 2026-11-12): the rich fat cat must look OMINOUS, almost horror: the dread of a foggy, rusting, nightmare-town survival-horror game. Take that feeling and translate it into this short; do not recreate any specific game's monsters, characters, places or imagery. The comedy of the short stays, the cartoon roots can stay or be pushed, but he should frighten.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**b-low-poly-short-draw-distance** — Beat B, today, in the look of a late-1990s console survival-horror game: low-poly 3D, warping blurry textures, dithered colour gradients, and fog so close that the park ends a few metres past the bench. A fixed high corner camera looks down like a security angle. The nurse in scrubs sits in a small cold pool of light, rendered in the same crude low-poly as everything else; the rich man beside her in top hat and frock coat is the one thing drawn in crisp, high detail, his hand half raised in a wave-off, which makes him wrong. Greenish-grey 4 a.m. palette, with the fog at the top for the caption.

Other writers are doing the other experiments (a-fog-swallowed-park, a-gaslamp-silent-film-still, a-his-shadow-arrives-first, b-blurred-behind-the-nurse, b-crosshatched-grin-closeup, c-black-painting-on-plaster, c-the-only-still-thing, c-rust-dust-wasteland). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): anywhere in the
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): man in a
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): of the frame
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): one gloved hand
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): rich man in
- shares wording with other prompts in this round: Flow prompts: a fat rich man in a
- shares wording with other prompts in this round: Flow prompts: sits a fat rich man in
- shares wording with other prompts in this round: Flow prompts: the top third of the frame

Your previous draft:
```json
{
  "name": "b-low-poly-short-draw-distance",
  "prompt": "A screenshot from a late-1990s home-console horror game, captured at 4 a.m.: a park bench seen from a fixed camera bolted high in a corner, angled steeply down like a security feed. The whole world is crude low-polygon 3D at a low native resolution: chunky blocky shapes with hard faceted edges, tiny smeared textures stretched and bent across the polygons so the bench slats, the path and the grass swim and kink, colour gradients broken into a fine checkered dither, faint jagged pixel steps on every edge. A thick wall of greenish-grey fog starts only a few metres behind the bench and swallows everything else; the top third of the frame is nothing but that dithered fog, empty and flat. On the bench a tired nurse in pale scrubs sits hunched in a small cold circle of light from an unseen lamp, built from the same handful of coarse polygons as everything else, her face a blurred, low-detail texture. Beside her, wrong, sits a fat rich man in a black top hat and a frock coat, rendered in sharp, high-detail realism as if pasted in from a far better machine: every crease in the wool, the gloss on the silk hat, the fleshy folds of his jowls, a small fixed smile, glassy eyes looking straight up into the camera. One gloved hand is half raised beside her in a lazy wave of dismissal. His crispness against the smeared world is the horror. Palette of sick grey-green, wet concrete and bruised olive, the nurse's pool of light a weak sodium-cold white. No text, no interface, no lettering anywhere in the image. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r3/writers/b-low-poly-short-draw-distance.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r3/writers/b-low-poly-short-draw-distance.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "b-low-poly-short-draw-distance". Reply with just the two paths.