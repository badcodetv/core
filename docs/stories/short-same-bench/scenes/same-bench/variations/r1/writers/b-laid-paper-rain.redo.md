You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

" #2 Same Bench: the 1919 fat cat tells a veteran "Forget it", then says it to a nurse on the same bench today. He hasn't aged a day." lets do this, using the art style, but lets change it slightly so it doesnt get copywrighted. THanks

please show me stills of this in the new scene skill and the dialogue skill thing thanks.

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- AI likeness of a real person.

## Never write these

The war is over my boy
Rollin Kirby
Kirby

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

## Your experiment

Write ONE prompt for this experiment, and only this one:

**b-laid-paper-rain** — Beat B, today. A medium-wide shot in the rain, drawn with pen line over strongly textured laid paper so the grey tone comes from the paper grain and fine diagonal rain strokes, not wash. The rich man sits dry under a big black umbrella he holds only over himself, top hat intact, waving the nurse off; she sits in the rain in scrubs and a thin cardigan, a tote bag on her lap. Puddles and a modern bus shelter behind. Open sky band above for the caption.

Other writers are doing the other experiments (a-crosshatch-wide-autumn, a-grease-crayon-low-angle, a-two-colour-overhead, b-crosshatch-hospital-dusk, b-crayon-closeup-hands, c-split-diptych, c-portrait-straight-to-camera, c-red-spot-repeated-benches). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): for a caption

Your previous draft:
```json
{
  "name": "b-laid-paper-rain",
  "prompt": "Upright newspaper-cartoon drawing made only with a black dip pen on heavy cream laid paper whose ribbing stays visible across the whole sheet: wide-spaced chain lines running top to bottom and close fine laid lines crossing them, the ink catching on the raised ribs and skipping the hollows, so every mid-tone comes from that broken striped grain plus hundreds of thin parallel rain strokes all slanting the same way down to the right, irregularly spaced, some dashed and overlapping, with no brush wash and no flat grey areas. The present day, a medium-wide view from seated height of an ordinary slatted park bench on shining wet tarmac. On the left sits a portly, double-chinned plutocrat wearing a high black stovepipe hat, a buttoned frock coat straining over his paunch and a gold fob dangling at his belly, bone dry under a huge black umbrella tilted to shelter him and nobody else, one gloved hand flapping lazily toward the woman beside him to wave her away, lids drooping, nose in the air. On the right, beyond the dripping rim of his umbrella, a worn-out nurse in hospital scrubs and a thin knitted cardigan sits soaked and hunched, wet hair stuck to her cheeks, a cloth tote bag clutched on her knees, eyes on him. Behind the bench, rain rings spread across puddles that reflect the bench legs, and a modern bus shelter of glass panels and steel posts is sketched in sparse fine outline. Dull overcast daylight with no shadows to speak of; the umbrella canopy is the only solid black mass. Black ink on cream paper and nothing more. The upper third is left as open ribbed paper crossed only by faint falling streaks, kept clear for a caption. No lettering, no words on the shelter, no signature on the sheet. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/b-laid-paper-rain.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/b-laid-paper-rain.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "b-laid-paper-rain". Reply with just the two paths.