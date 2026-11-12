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

**a-behind-the-bench-noon** — Beat A, 1919, seen from directly behind the bench: two backs, one vast in a frock coat and top hat, one thin in khaki with a crutch propped against the slats and a single boot below. Loose, quick, confident pen line with little hatching, printed on yellowed newsprint, the noon sun overhead pooling short shadows under the seat. The rich man's head is turned slightly away, one arm thrown out sideways in a lazy wave-off; the soldier's head is bowed. Beyond them a sunny promenade with strollers in boaters, drawn lightly so the pair dominate; caption room in the pale path at the bottom.

Other writers are doing the other experiments (a-frost-park-from-above, a-crayon-dismissing-hand, b-flat-colour-hospital-night, b-two-eras-two-pens, b-over-the-nurse-shoulder, c-banknote-engraving-portrait, c-split-century-bench, c-alone-at-sunset-wide). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): a tall silk
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): for a caption
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): of any kind
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): silk top hat

Your previous draft:
```json
{
  "name": "a-behind-the-bench-noon",
  "prompt": "A tall vertical drawing, as if dashed off at speed with a dip pen and India ink for a 1919 weekly, then printed on cheap yellowed newsprint gone tea-coloured with age, the paper fibres and faint show-through visible. We look straight at the backs of two men on a wooden park bench, the viewer standing a few paces behind it at eye level. On the right sits an enormous rich man seen from behind: a broad black frock coat stretched across a back as wide as a wardrobe, rolls of neck spilling over a starched collar, a tall silk top hat tilted back, his head turned a little away from his companion as he flings one fat gloved arm out sideways in a bored, lazy flick of dismissal. On the left, a narrow young soldier in a creased khaki tunic and peaked cap, shoulders hunched, head hung low; a wooden crutch leans against the bench slats beside him and beneath the seat only one boot rests on the gravel, the other trouser leg pinned up short. The line is loose, fast and sure, mostly open contour with only a few strokes of hatching on the coat folds and the slats; flat midday sun straight overhead leaves small hard pools of black shadow directly under the bench and under each figure, and almost no shading elsewhere. Past the bench, a bright sunlit promenade with strollers in straw boaters and parasols and a row of trimmed trees, sketched in thin, sparse, pale lines so the two backs own the picture. The lower fifth of the frame is the empty pale gravel path, left clean for a caption to be laid on later. Palette: black ink on warm aged cream only. The drawing carries no lettering, no speech balloons, no labels and no artist's mark of any kind. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/a-behind-the-bench-noon.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/a-behind-the-bench-noon.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "a-behind-the-bench-noon". Reply with just the two paths.