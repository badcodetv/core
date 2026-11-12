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

**c-red-spot-repeated-benches** — Beat C, the button. A deep receding view down a long park path lined with identical benches, black ink and grease crayon with a single red spot colour; on every bench into the distance sits the same rich man in the same pose, top hat and red dollar-sign waistcoat, while the people beside him change from bench to bench across the years (a soldier, a factory girl, a miner, a nurse). The nearest bench is large in the foreground, the rest shrink to the vanishing point. Pale sky at the top for the caption.

Other writers are doing the other experiments (a-crosshatch-wide-autumn, a-grease-crayon-low-angle, a-two-colour-overhead, b-crosshatch-hospital-dusk, b-crayon-closeup-hands, b-laid-paper-rain, c-split-diptych, c-portrait-straight-to-camera). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): in the picture
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): of the frame
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): one trouser leg
- shares wording with other prompts in this round: Flow prompts: a caption no text no lettering
- shares wording with other prompts in this round: Flow prompts: caption no text no lettering no
- shares wording with other prompts in this round: Flow prompts: clear for a caption no text
- shares wording with other prompts in this round: Flow prompts: for a caption no text no
- shares wording with other prompts in this round: Flow prompts: is the only red thing in
- shares wording with other prompts in this round: Flow prompts: kept clear for a caption no
- shares wording with other prompts in this round: Flow prompts: no text no lettering no signature
- shares wording with other prompts in this round: Flow prompts: only red thing in the picture
- shares wording with other prompts in this round: Flow prompts: the only red thing in the

Your previous draft:
```json
{
  "name": "c-red-spot-repeated-benches",
  "prompt": "Portrait illustration drawn in coarse black grease crayon and loose pen line on cream newsprint with a toothy laid texture, every mark black except one flat printed red. A gravel park path runs straight away from the viewer in one-point perspective, its vanishing point a little above the middle of the frame, flanked by a row of bare elms and an unbroken line of identical wooden slatted benches that shrink smaller and smaller until they dissolve into a dot. On every single bench sits the same heavy-bellied rich man, copied exactly: tall black stovepipe hat, sagging jowls, cigar, legs crossed the same way, one gloved hand lifted in a bored dismissive flick, and a waistcoat stretched over his paunch printed solid red with a black dollar sign. He is the only red thing in the picture, so the red waistcoats form a dotted line that leads the eye down the path into the distance. The companion beside him changes on each bench: nearest us, large and filling the lower foreground, a weary nurse in shapeless scrubs with her hands folded in her lap; behind her a coal miner with a soot-smudged face and a lamp on his cap; further back a factory girl in a long apron and headscarf; far back, barely more than a few strokes, a soldier on a crutch with one trouser leg pinned up. Low eye-level view from the path, as if the viewer is the next person about to sit down. Even flat daylight, grainy crayon shading under the benches, heavy black hatching in the tree trunks, white paper left showing for highlights. The top third is an almost empty pale sky with only faint crayon grain, kept clear for a caption. No text, no lettering, no signature. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/c-red-spot-repeated-benches.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/c-red-spot-repeated-benches.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "c-red-spot-repeated-benches". Reply with just the two paths.