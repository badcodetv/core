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

**c-blue-hour-empty-horizon** — Beat C, the clean button frame for the logo: a very calm, minimalist seascape at blue hour, a perfectly flat still sea taking the bottom fifth of the vertical frame with a thin line of a distant low coast, and above it a huge smooth gradient of sky from deep indigo at the top to a faint warm glow at the horizon. One tiny warm light on the far coast, nothing else. Long exposure smoothness, no clouds, no birds, generous empty space in the upper and middle frame where a logo will sit. Quiet, hopeful after everything before it.

Other writers are doing the other experiments (a-aerial-wall-between, a-flash-banquet-left-standing, a-painted-bored-suburb, a-kerbside-furniture-deadpan, b-grey-tableau-office, b-fireside-public-information, b-flash-doorstep-closeup, b-standing-in-the-drained-pool). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): of the frame
- shares wording with other prompts in this round: Flow prompts: or lettering anywhere in the image

Your previous draft:
```json
{
  "name": "c-blue-hour-empty-horizon",
  "prompt": "A tall portrait photograph of open water just after sunset, taken from a low tripod at the edge of a calm estuary. The sea is glass: a two-minute exposure has erased every ripple, leaving a satin sheet of pale slate blue that fills only the lowest fifth of the frame and holds a soft, blurred mirror of the sky. Right on that low horizon lies a faint, flat sliver of distant shoreline, dark and featureless, and on it a single small amber pinprick, perhaps a lit window in a farmhouse miles away, whose glow lays one thin vertical smear across the still water. Everything above is empty air: an unbroken, seamless sky that deepens from ink-dark navy at the very top, through cobalt and a muted periwinkle, to a thin band of apricot warmth hugging the horizon. No clouds, no birds, no boats, no stars yet, no grain of detail anywhere in the upper two thirds, so the middle and top of the frame read as clean breathing room. Level horizon, wide normal lens, deep focus, gentle shadow detail, cool restrained palette with that one warm accent. Feels like the first quiet evening after a long storm: still, patient, quietly hopeful. No text, signs or lettering anywhere in the image.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r1/writers/c-blue-hour-empty-horizon.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r1/writers/c-blue-hour-empty-horizon.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "c-blue-hour-empty-horizon". Reply with just the two paths.