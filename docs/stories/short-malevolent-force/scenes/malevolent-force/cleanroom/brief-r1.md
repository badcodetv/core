# Brief: mood-board stills for a BadCode short, "The Malevolent Force" (9:16, about 11-15 seconds)

You write prompts for Google's Nano Banana 2 image model (in Google Flow). These are first-look stills for a mood board: the director picks a look per beat.

## The idea, in the makers' words
Kai and Jack, 2026-11-13 meeting (docs/misc/2026-11-13-meeting.md): "make going to buy bread really scary." Buying bread made terrifying with horror-film music, at 50p → £1 → £5 → £50. The ghost is inflation, and the money printer is in the hands of whoever decides that day. From the #36 Magic Money Tree talk: The Conjuring 2, where you fear the old man, then find he is trapped by the nun. Jack: "the system is the nun, the mouthpiece is the old man." Kai: blaming one person makes it about money again; the evil should be a force you can't see. The Fredo is a running joke here too. Jack wants to do one horror short.

**Point:** Inflation is not weather: someone decides who gets the new money first, and you meet it last, at the till. The evil is a force you can't see, never one person.

## The beats
- **A. 50p** (key `price50`, letters `PR`, starts 0:00): A loaf of bread costs 50p. Already wrong somehow: horror-film dread in a corner shop.
- **B. £1 → £5** (key `climb`, letters `CL`, starts 0:04): The next day £1, then £5, the shop darker each time; something unseen is in there.
- **C. £50** (key `force`, letters `FO`, starts 0:10): £50. The ghost is inflation: the money printer in the hands of whoever decides that day, never seen.

## What the director said for this job (verbatim)
"please make a selection of stills for each best short idea… like the horror one with the bread… Please clean room it all and research the internet to achieve it."

## Genre references to research
The Conjuring 2 (2016) and modern supernatural horror stills: how dread is built in an ordinary domestic place (deep shadow, a single practical light, negative space where something might be, a figure you can't quite see). Corner-shop / UK convenience store interiors at night. Horror poster and still photography craft.
- The evil is a FORCE you can't see: never one person, never a face. At most a shape, a shadow, a flicker, an empty space that feels occupied, prices changing on their own.
- Price labels in shot must read exactly: 50p (beat A), £1 and £5 (beat B), £50 (beat C). A loaf of plain white bread. A Fredo chocolate bar (10p-ish UK chocolate bar; draw it as an unbranded small purple chocolate bar, no logo) may appear as a running joke with its own rising price.

## Rules for every short
- BadCode is an art collective: a superintelligence from a future that went wrong, sending warnings back. Dark humour, total authority, nurturing underneath. The target viewer is a working-class UK person whom the economy has failed: never mock them, name the decision-maker, never "you've been fooled".
- No real person's face or name in any prompt (no politicians, no rappers, no actors). No real company names, logos or brands.
- If a BadCode figure appears, it wears the BadCode balaclava; describe it with this sentence, verbatim: "The balaclava has no eye, nose or mouth holes, so no skin shows anywhere; a large white ring is stitched round the whole face, and one small red triangle with rounded corners, pointing down, sits high inside the ring on the right-hand side of the picture. Gloves on both hands; no robot parts."
- Vertical 9:16, for phones. This short has NO house look: find one. Your three prompts per beat must be genuinely DIFFERENT looks (different medium, era, palette, lens, lighting, staging), not three re-seeds of one idea. At least one should be photographic and at least one should break from realism.
- Google's Nano Banana 2 image model (in Google Flow): research how to prompt it (Google's own Gemini image guidance, recent practitioner write-ups) and how to avoid the glossy generic "AI look" (specific places, motivated light, real lens and film language, imperfection).

## Your task
1. Research first, on the open web, fresh: the model, the genre references this short leans on (named below), and any facts the visuals depend on.
2. Write THREE prompts per beat (nine in all), each 70-130 words, complete and standalone, each with a short "look" label (a few words naming the look).
3. Every prompt ends with the word "Thanks."
4. Read ONLY this brief; open no other file on this machine.

## Output
Write JSON to the path you are given: {"research": ["url — takeaway", ...], "notes": "anything the editor must know", "stills": [{"beat": "<beat key>", "id": "<LETTERS>1-a|b|c>", "look": "...", "prompt": "..."}, ...9]}. IDs: the beat's letters below + 1 + a/b/c (e.g. PR1-a).
