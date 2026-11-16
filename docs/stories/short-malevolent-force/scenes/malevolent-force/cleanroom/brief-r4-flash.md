# Brief: the lightning price-change shot, round 2 (clean room)

You write prompts for Google Flow: a still for **Nano Banana 2** (vertical 9:16), an image-edit instruction for Nano
Banana 2, and an image-to-video motion prompt for **Omni 1.2 Flash** (Frames mode: the still is the start frame; 8 s;
vertical 9:16). Research on the open web first. Read ONLY this brief and the images listed; open no other file on this
machine.

## What the director said (verbatim, Jack, 2026-11-16)
First: "we need a different video to show the bread and the freddo changing pice, it needs to be a flash of lightning like in a horror way, then it changes price, but the bread and freddo need to be somewhere else in the shop."
Then, on the first attempt (which used two separately generated stills, so the room changed between them): "the setting needs to stay the same before and after the lightning flash, literlly the only thing that chenges are the prices, also make it more zoomed in on the bread like that one we picked on the shelf."

## "Like that one we picked on the shelf"
`~/.cache/badcode/mf-anim/PR2-b.jpg` (look at it): a close shot of one loaf on a bare shelf with a price card. That is the
closeness wanted: the bread fills much of the frame. The look of the whole short: the director's reference photo
`/home/jackt/projects/badcode/badcode/docs/stories/short-malevolent-force/scenes/malevolent-force/reference/jack-r2-shop-doorway.png`
(cheap colour film at night, grain, soft focus, fluorescent teal). The other shots of the shop for matching:
`~/.cache/badcode/mf-anim/PR2-e.jpg`, `PR2-c.jpg`, `FO2-d.jpg`.

## The short (context)
Buying bread at a British corner shop at night, shot like a haunting, about 15 s, no voice, end card "Based on true
events. Coming to a shop near you." The ghost is inflation: prices climb and nobody is ever seen. **No person, face,
hand, figure or a person's shadow, ever.**

## How it will be built (fixed)
1. ONE still: the loaf of plain white sliced bread and a small purple chocolate bar (the "freddo": a cheap UK kids'
   chocolate bar; draw it **unbranded**: plain purple wrapper, no logo, no name), close, **somewhere other than the
   bread shelf** (e.g. a counter, a freezer lid, a window ledge, a crate: your call), with two price cards:
   bread **£5**, chocolate bar **10p**. The cards must be **flat, facing the camera, not overlapping anything, not
   bent, and clearly separate from the products**, so they can be swapped cleanly.
2. ONE image edit of that still: change only the card text, to bread **£50** and chocolate bar **10p crossed out with
   one line, £12 beside it**. The edited cards will be cut out and pasted onto the original still, so nothing else
   can change.
3. ONE motion clip from the still: camera locked, nothing in the room moves; the light is steady, then a lightning
   flash, horror style, at about 2 s (through a window or the door glass, a strong white-blue burst, at most two
   flashes, no more than 3 a second), then the light returns to **exactly** the same steady level as the start and
   holds still to the end. The prices are swapped in the edit on the brightest flash frame, so after the flash the
   room must look the same as before it.

## Hard facts
- No dialogue, no voices, no people. One continuous shot, no cuts. Text must not change during the clip.
- Nothing falling or flying. No real brands. End every prompt and the edit instruction with the word "Thanks."

## Your task
1. Research: Nano Banana 2 prompting for a candid colour-film night close-up with legible handwritten price cards;
   Nano Banana 2 / Gemini image editing for changing only text in an image while keeping everything else; Omni / Flow
   image-to-video for a locked, static shot with a single lightning flash and stable text.
2. Write THREE options (a, b, c): different places in the shop, all close on the bread like PR2-b.
3. Write JSON to `/home/jackt/projects/badcode/badcode/docs/stories/short-malevolent-force/scenes/malevolent-force/cleanroom/prompts-r4-flash.json`:
   `{"research": ["url — takeaway", ...], "notes": "...", "options": [{"id": "a", "place": "...", "label": "a few words", "still": "...", "edit": "...", "motion": "...", "risk": "..."}, ...3]}`
