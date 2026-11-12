You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

"Hello, I'm BadCode: "I'm from the future. It didn't go well."" lets mess around with this. THanks

Answers to the questions: who is BadCode on screen = "Mix of both" (open on the future that went wrong, then cut to the balaclava figure for the punchline); angle = "Deadpan intro" (polite and calm, the understatement is the joke); shape and look = "9:16, explore looks".

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- AI likeness of a real person.

## Never write these

robot
cyborg

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

## What the picture shows

A BadCode Short, about 9 seconds, three beats. Mood board round 1: spread the round across the beats (about four stills for A, four for B, one or two for C), each a genuinely different look. BadCode presents itself as a superintelligence from a future where humanity careered into disaster (greed, runaway inequality, politics that could not keep up with AI); it has come back to warn us. Dark humour, total authority, deadpan.

Beat A (the future, voice over "Hello. I'm from the future."): the future that went wrong, glimpsed and never explained. Show the aftermath of a society that failed itself, not monsters or robots attacking: what is left when greed won.
Beat B ("It didn't go well."): cut to BadCode itself: a figure in a balaclava looking straight into the camera, deadpan, calm, a little polite. The balaclava is a plain knitted ski mask; on it, around the LEFT eye hole (the wearer's left), a thin white ring, and a small red triangle with rounded corners pointing down, sitting inside the ring at about 2 o'clock. No skin visible, gloved hands, no robot parts. Where they are and how they are shot is yours to choose.
Beat C ("Watch this space."): the button; the BadCode logo is added afterwards in the edit, so leave a calm, uncluttered frame.

Portrait 9:16. No text, signs or lettering drawn in the image.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**b-standing-in-the-drained-pool** — Beat B, tying the future to the figure: BadCode stands alone, upright and perfectly centred, at the deep end of a drained, cracked luxury swimming pool with brown leaves and a broken sun lounger at its bottom; the empty villa looms pale above the pool edge. Shot from slightly low at the shallow end with a 28mm lens, symmetrical, deep focus, under a flat white overcast sky. Plain dark knitted balaclava with a thin white ring around the wearer's left eye hole and a small rounded red triangle inside at about 2 o'clock pointing down; gloved hands clasped behind the back like a tour guide. Muted, chalky palette; the stillness is the joke.

Other writers are doing the other experiments (a-aerial-wall-between, a-flash-banquet-left-standing, a-painted-bored-suburb, a-kerbside-furniture-deadpan, b-grey-tableau-office, b-fireside-public-information, b-flash-doorstep-closeup, c-blue-hour-empty-horizon). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts: buttoned to the collar and dark

Your previous draft:
```json
{
  "name": "b-standing-in-the-drained-pool",
  "prompt": "Vertical photograph taken from the dry floor of the shallow end of a long empty villa pool, looking straight down its length toward the deep end; 28mm lens held a little below head height so the floor slopes away and up, strict mirror symmetry, everything sharp from the near tiles to the house. The pool has been dry for years: faded turquoise mosaic split by fine cracks and darker tidemarks, a drift of crisp brown leaves along the drain, a white plastic sun lounger lying on its side with a leg snapped off. Exactly central, in the lowest part of the deep end, one person stands at attention and looks into the lens with calm, courteous patience, hands clasped behind the back in black leather gloves like a guide waiting for a tour group. They wear a plain matte black wool balaclava that hides all skin, an unremarkable dark overcoat buttoned to the collar and dark trousers. On the balaclava, a fine white circle is traced around the left eyehole, the wearer's own left, and within that circle, up toward the top right where two would sit on a clock face, a tiny crimson triangle with rounded tips points down. Over the coping behind them the villa fills the top of the frame dead centre: pale peeling render, closed shutters, a bare terrace with one dried-out palm in a pot. Sky a uniform white overcast, light soft and shadowless. Chalky muted colours of bone, washed-out aqua, dust grey and dry-leaf brown; the crimson triangle is the one strong colour. Very still, formal and politely absurd. No water, no other people, no visible skin, no writing, numbers or pool depth markings anywhere.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r1/writers/b-standing-in-the-drained-pool.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r1/writers/b-standing-in-the-drained-pool.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "b-standing-in-the-drained-pool". Reply with just the two paths.