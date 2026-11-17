# Brief: round 2 mood-board stills for a BadCode short, "The Malevolent Force" (9:16, about 11-15 seconds)

You write prompts for Google's Nano Banana 2 image model (in Google Flow). These are stills for a mood board: the director picks the ones he likes.

## What the director said for this round (verbatim, Jack, 2026-11-16)
"The Malevolent Force lets continue with this. please use this as inspiration to make stills [the reference photo] make a bunch of varied ones that look like this image. Please clean room it all and research the internet to achieve it. Thanks."

## The reference photo (look at it: the path is given to you)
`docs/stories/short-malevolent-force/scenes/malevolent-force/reference/jack-r2-shop-doorway.png`

Plain facts about it, in case you can't open it: a vertical snapshot at night, taken from the pavement looking through the open glass door of a small corner shop / convenience store. Shot on colour film, not digital: visible grain, soft focus, slightly underexposed, a cold blue-teal cast over everything, fluorescent tubes inside blowing out a little. Inside: a wire spinner rack of crisps and snacks, a lit drinks fridge of bottled water, a big wall fan, clutter, a dirty rubber doormat. The frame of the doorway (metal door frames, a hand-printed paper sign taped to the glass, a fire-hydrant-ish post at the edge) surrounds the shop. Nobody is in it. It is ordinary, a bit lonely, and slightly eerie. Not staged, not lit by a photographer: an amateur's snapshot on cheap film.

**"Look like this image" means this photographic look**: cheap colour film at night, available light only, grain, teal/fluorescent cast, an unglamorous real shop, candid framing, no people posing. **"Varied" means different pictures inside that look**: different shops, angles, distances (street wide, doorway, aisle, counter close-up, insert of a price label), different times in the night, different small details. Do not copy the reference composition every time; at most one of your prompts may echo its doorway framing.

## The idea, in the makers' words
Kai and Jack, 2026-11-13 meeting: "make going to buy bread really scary." Buying bread made terrifying with horror-film music, at 50p → £1 → £5 → £50. The ghost is inflation, and the money printer is in the hands of whoever decides that day. From an earlier talk: The Conjuring 2, where you fear the old man, then find he is trapped by the nun. Jack: "the system is the nun, the mouthpiece is the old man." Kai: blaming one person makes it about money again; the evil should be a force you can't see. The Fredo (a cheap UK chocolate bar) is a running joke too.

**Point:** Inflation is not weather: someone decides who gets the new money first, and you meet it last, at the till. The evil is a force you can't see, never one person.

## The beats
- **A. 50p** (key `price50`, letters `PR`): A loaf of bread costs 50p. Already wrong somehow: horror-film dread in a corner shop.
- **B. £1 → £5** (key `climb`, letters `CL`): The next day £1, then £5, the shop darker each time; something unseen is in there.
- **C. £50** (key `force`, letters `FO`): £50. The ghost is inflation: the money printer in the hands of whoever decides that day, never seen.

## Facts the pictures depend on
- A British corner shop (UK, not American: UK plugs and signs, pound prices, a newspaper rack, a lottery-style stand is fine if unbranded).
- Price labels in shot must read exactly: 50p (beat A), £1 or £5 (beat B), £50 (beat C). A loaf of plain white sliced bread. A small unbranded purple chocolate bar may appear with its own rising price.
- The evil is a FORCE you can't see: never one person, never a face. At most a shadow, a flicker, an empty space that feels occupied, a door that has moved, a price that changed by itself, lights failing.

## Rules for every short
- BadCode is an art collective: a superintelligence from a future that went wrong, sending warnings back. Dark humour, total authority, nurturing underneath. The viewer is a working-class UK person the economy has failed: never mock them.
- No real person's face or name in any prompt. No real company names, logos or brands (signs and packets are invented or unreadable).
- Vertical 9:16, for phones.

## Your task
1. Research first, on the open web, fresh: how to get Nano Banana 2 (Gemini 3.1 Flash Image) to make a convincing amateur colour-film night snapshot rather than a glossy "AI" image (Google's own prompting guidance, recent practitioner write-ups); the look of night film photography of shops and storefronts (which stocks, how they render fluorescent light at night, what amateur exposure looks like); and how horror films and photographers make an empty ordinary place feel occupied.
2. Write FIVE prompts for your one beat (given to you), each 60-120 words, complete and standalone, each with a short "look" label (a few words naming the picture, e.g. the angle and the detail). All five in the reference's look, all five different pictures.
3. Every prompt ends with the word "Thanks."
4. Read ONLY this brief and the reference photo; open no other file on this machine.

## Output
Write JSON to the path you are given: {"research": ["url — takeaway", ...], "notes": "anything the editor must know", "stills": [{"beat": "<beat key>", "id": "<LETTERS>2-a..e", "look": "...", "prompt": "..."}, ...5]}.
