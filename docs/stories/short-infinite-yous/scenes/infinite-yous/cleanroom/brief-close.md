# Brief: stills for "closing the timelines into one" ("Infinite Yous", shot C, 9:16)

You write prompts for Google Flow's Nano Banana 2 image model. These are STILLS for the edit (no video): the editor cuts between them on the beat.

## The film
A 15-second UK satirical short, vertical 9:16, for phones. Late at night a drunk lad in his early twenties, car keys up, says "One version of me gets home fine" (he has read that there are infinite versions of him in parallel universes, so nothing he does matters). The screen splits: five versions of him side by side in tall vertical strips divided by thin bright lines, each a slightly different him. Then a figure in a balaclava and a white science lab coat grabs the dividing lines and squeezes them together, crushing the versions back into one, the original, and says "There's only one." Then he boots him into a taxi. Cut to the logo.

## The director's words (verbatim)
"him closing the multivers-timelines into one is just an image fix that, please fix it all thanks."
Earlier, on this shot: "use the maybe, but combine it with the five tall vertical strips so it matches up. also badcode guy should look more like a scientist also should never show skin."

## The images (open all three)
- The split, already in the film: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/infinite-yous/moodboard/SP1-a.jpg (five strips of the lad, thin bright dividers).
- The current squeeze still: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/shorts/infinite-yous/moodboard/SQ2-a.jpg (the scientist gripping two dividing lines). Its fault: his safety goggles sit OVER the mask's white ring and red triangle and hide them. And nothing is squeezed yet.
- The mask reference: /home/jackt/projects/badcode/badcode/docs/brand/balaclava/mask-reference.jpg — the balaclava has no eye, nose or mouth holes, so no skin shows; a large white ring is stitched round the whole face, and one small red triangle with rounded corners sits high inside the ring on the right-hand side of the picture (over his LEFT eye). Gloves on both hands. No robot parts.

The editor will ATTACH SP1-a, SQ2-a and the mask reference to each generation (up to three images). Say in each prompt how to use them (e.g. "the five strips and lad from the first image, the scientist from the second, the mask exactly as the third"), and do not otherwise describe what the lad or the scientist look like.

## Your task
1. Research first, on the open web, fresh: how to prompt Nano Banana 2 / Gemini image editing with several reference images (Google's own guidance, recent practitioner write-ups); how split-screen / "multiverse collapse" frames are designed in film and motion graphics (how to show many becoming one in a single still); how to keep a costume detail (a mask motif) faithful from a reference.
2. Write a SEQUENCE of THREE stills the editor can cut between on the beat, each 70-130 words, vertical 9:16, the night-bokeh look of SP1-a:
   - C1: the scientist steps in and grips the dividing lines in both gloved fists, the five strips still open (the mask's ring and triangle fully visible; goggles pushed up on his forehead or gone).
   - C2: mid-squeeze: he hauls the lines together, the strips crushed narrow and bending, the five lads squashed towards the middle, light flaring where the lines bunch.
   - C3: one: the lines gone, one lad alone and whole, blinking, the scientist beside him with his hands open, the frame calm.
3. Every prompt ends with the word "Thanks." No readable text anywhere. No real names of people, films or companies.
4. Read ONLY this brief and the three images; open no other file on this machine.

## Output
Write JSON to the path you are given: {"research": ["url — takeaway", ...], "notes": "anything the editor must do", "stills": [{"id": "C1", "idea": "...", "attach": ["SP1-a", "SQ2-a", "mask"], "prompt": "..."}, ...3]}
