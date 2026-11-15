# Brief: one beat of a BadCode short, "The Envelope", Sting version (9:16)

You write image prompts for Google's Nano Banana 2 image model (in Google Flow). The image will be generated WITH a style reference image attached (a painted card from the same short), so the look is carried by the reference: describe the picture's content and staging, and name the look only briefly.

## The short
A 1930s backstreet betting parlour where the race is the election, told as a con in the manner of the 1973 film "The Sting". The voter is the mark. Four beats, each a painted 1930s magazine-cover-style chapter card (opaque gouache, flat poster colour, visible brush strokes, ochre / maroon / bottle green, an invented hand-lettered chapter title in a mustard band at the top):
- S1 "THE COUNTER": a dealer fans two envelopes, stamped "APPROVED BY THE CONSERVATIVE PARTY" and "APPROVED BY THE LABOUR PARTY", at even odds.
- S2 "THE PICK": a working man in a flat cap picks one in good faith; the dealer plays the fair host.
- **S3 "THE SWITCH": THIS BEAT. The reveal that the choice was rigged both ways: the same arms deal goes through whichever envelope he picks, with fresh money.**
- S4 "THE PAY-OFF": a BadCode figure pulls back the curtain on two suited men, blue tie and red tie, shaking hands over a stamped rifle crate. Line: "They're going to print the money and the weapon sales will still happen anyway, everything else is a distraction."

## The director's note on the current S3 (verbatim)
"this style but change it make it more like the sting. thanks"
The current S3 shows a mechanical cutaway: two ballot slots feed rubber-stamp machines into one crate labelled "ORDER No. 0417" beside stacks of money. The director likes the painted style but it doesn't feel like The Sting.

## Your task
1. Research fresh on the open web: how The Sting stages its cons and its switches (the moves, the props, the sleight of hand, the people in on it, how the film shows the audience the trick), its chapter-card structure and its vibe; also the classic switch moves of short cons (the shell game, the envelope switch / pigeon drop, the "poke" swap), which are the real-world sleight the film draws on.
2. Write THREE different S3 prompts (ids SW3-a, SW3-b, SW3-c), each a different staging idea of the switch that feels like The Sting, 60-110 words each, each ending with the word "Thanks." Each keeps the chapter title "THE SWITCH" in the band at the top, both stamps legible and exact, and the same arms order (you may keep "ORDER No. 0417") so the rig is readable at a glance on a phone.

## Hard lines
- Do not recreate the film: no actor's name or likeness, none of its characters, no copy of its real title cards, poster or artwork. Era, genre and vibe only; invent everything else.
- No real person's face or name; no party logos (parties appear only as the exact stamp text); no real banknote designs (invented notes, no dollar signs or real currency), no real brands.
- Faces may be shaded by hat brims; hands are fine. Vertical 9:16.
- The joke is on the people running the con, never on the working man.
- Read ONLY this brief; open no other file on this machine.

## Output
Write JSON to the path you are given: {"research": ["url — takeaway", ...], "notes": "...", "stills": [{"beat": "switch", "id": "SW3-a|b|c", "look": "<staging idea in a few words>", "prompt": "..."}]}
