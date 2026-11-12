You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

" #2 Same Bench: the 1919 fat cat tells a veteran "Forget it", then says it to a nurse on the same bench today. He hasn't aged a day." lets do this, using the art style, but lets change it slightly so it doesnt get copywrighted. THanks

please show me stills of this in the new scene skill and the dialogue skill thing thanks.

## What happened in earlier rounds (facts)

Round r1 (2026-11-12): nine separate writers, one prompt each. The sameness gate still failed after two rewrites, so nothing ran and no stills were made.
Phrases it flagged as shared between prompts included: "no words letters numbers signature or speech", "on the bench's left end lounges", "end of the bench sits a", "a tall portrait drawing in black", "signature anywhere in the image thanks".
Jack, asked whether to run r1 anyway or start fresh: "Fresh round".

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

**b-over-the-nurse-shoulder** — Beat B, today, from just over the nurse's shoulder: her blurred scrub shoulder and tied-back hair at the bottom edge, and the rich man's face and top hat filling the middle of the frame, mid-dismissal, eyelids half shut, cigar in the corner of his mouth, palm up toward her. Pen and ink with cool blue-grey wash, early morning after a night shift, low pale sun behind him rimming his hat. Behind him, small and lightly drawn, a city of glass towers. Clear sky above his hat for the caption.

Other writers are doing the other experiments (a-frost-park-from-above, a-crayon-dismissing-hand, a-behind-the-bench-noon, b-flat-colour-hospital-night, b-two-eras-two-pens, c-banknote-engraving-portrait, c-split-century-bench, c-alone-at-sunset-wide). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts: empty so words can be laid
- shares wording with other prompts in this round: Flow prompts: so words can be laid over
- shares wording with other prompts in this round: Flow prompts: words can be laid over it

Your previous draft:
```json
{
  "name": "b-over-the-nurse-shoulder",
  "prompt": "A tall hand-inked cartoon in the manner of a century-old newspaper drawing: springy steel-nib line work, scraped and corrected in places, faint graphite underdrawing still showing, on ribbed laid paper, with a watery wash of slate blue and pewter grey pooled into the shadows. The viewpoint sits right behind a hospital nurse on a park bench. Across the bottom edge, soft and smudged as if out of focus, run the rounded slope of her shoulder in washed-out scrubs and a loose bun of hair held by an elastic, only a few pale strokes. Dominating the middle of the frame, close and large, is the plump old-money gentleman sitting next to her: tall shiny stovepipe hat, high stiff collar, cheeks and double chin pressed over it, a waistcoat straining at its buttons. He is caught in the act of dismissing her, lids sagging to half-mast in boredom, a fat cigar wedged into one corner of his lips, one hand held out flat with the palm facing up at her as if there is nothing more to say. Dawn, the end of her night on the wards: a weak, low sun hangs just behind his head, outlining the hat's crown and brim and the tops of his shoulders in a thin glowing edge while his face sits in cross-hatched shade. Far off behind the bench, tiny and drawn with a few hairline strokes, stand glass-walled city skyscrapers. Above the hat, a wide band of bare pale sky with barely any wash, left empty so words can be laid over it in the edit. Nothing is written inside the drawing itself, no letters, no balloons, no initials. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/b-over-the-nurse-shoulder.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/b-over-the-nurse-shoulder.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "b-over-the-nurse-shoulder". Reply with just the two paths.