# Brief: mood-board stills for a BadCode short, "True Scale" (9:16, about 13-15 seconds)

You write prompts for Google's **Nano Banana 2** image model (in Google Flow), vertical 9:16. These are first-look stills for
a mood board: the director picks the ones he likes. Research on the open web first. Read ONLY this brief and the reference
photo named below; open no other file on this machine.

## What the director said (verbatim, Jack, 2026-11-16)
"okay do the uk stats, in intresting varied ways as stills Please clean room it all and research the internet to achieve it. Thanks."

## The idea
Kai (co-founder), on a viral clip about US homelessness vs empty homes: "I can imagine a video where it's like here is the true
scale of GodZilla and they put him next to Empire State. here is the true scale of homelessness and we do a three.js render of
[the people] when then zoom out and side by side a three.js render of [the] homes." The "true scale" comparison format: one
thing, then the full count, then something far bigger beside it, so the viewer SEES the ratio.

**The point:** England has far more homes standing empty or kept as second homes than it has homeless households.
Homelessness is a decision about who homes are for, not a shortage. Never mock the viewer; never blame homeless people;
never a real person, politician or company.

## The numbers (England, official, late 2025)
- **134,210** homeless households in temporary accommodation (B&Bs, hostels, short lets). A household = a single person, a couple or a family. 85,800 of them have children. (Only about 4,800 people sleep rough: the crowd is households, not rough sleepers.)
- **303,185** homes standing empty long-term (6+ months).
- **267,894** second homes (furnished, nobody's main home) (still being checked).
- So: more than two long-term empty homes per homeless household; about four once second homes are counted.

## The beats (the film pulls back three times)
- **A. One household** (key `one`, letters `ON`): one homeless household, small in the dark under a teal light.
- **B. 134,210** (key `crowd`, letters `CR`): every homeless household, all at once.
- **C. 303,185** (key `empty`, letters `EM`): every long-term empty home, dark, beside them; the households become small.
- **D. 267,894 more** (key `second`, letters `SH`): the second homes appear or light up too; the ratio becomes about four to one. The last image the viewer remembers.

## The look (a starting point, not a cage)
The director picked "night, fluorescent teal, like our horror short about bread prices": the feel of this reference photo,
`/home/jackt/projects/badcode/badcode/docs/stories/short-malevolent-force/scenes/malevolent-force/reference/jack-r2-shop-doorway.png`
(look at it): night, cheap colour film, grain, cold fluorescent teal, lonely and slightly eerie. The final film may be a 3D
render; these stills explore how the numbers could be SHOWN. **"Varied ways"** means genuinely different visual ideas for the
number in your beat (e.g. a physical model, a map, objects standing in for households, an aerial view, a counting device, a
diagram made of real things, a single strong metaphor), not three re-seeds of one idea. At least one should be a literal
"true scale" comparison view; at least one should surprise.

## Rules
- Vertical 9:16. No real people's faces, no real brands, no real politicians. People, if any, are tiny figures (model figures, silhouettes, crowd at a distance), never close-up faces.
- Any number written in the image must read exactly as given above (with the comma), and short: one number per image at most. Prefer images where the number is shown by the THING, not by text.
- Nothing that looks like real news footage or a real place's identifiable landmark with a real person in it.
- Google's guidance and practitioner write-ups on Nano Banana 2: research how to avoid the glossy generic "AI look" (specific places, motivated light, real lens/film language, imperfection) and how to get legible numerals.

## Your task
1. Research first, fresh, on the open web: the model; "true scale" comparison videos and infographics (how they make a ratio felt); visual ways artists and data journalists have shown housing / homelessness numbers; England's housing (terraced streets, estates, B&B and hostel temporary accommodation) so the pictures look like England.
2. Write THREE prompts for your one beat (given to you), each 70-130 words, complete and standalone, each with a short "look" label. Three different ideas.
3. Every prompt ends with the word "Thanks."
4. Write JSON to the path you are given: {"research": ["url — takeaway", ...], "notes": "...", "stills": [{"beat": "<beat key>", "id": "<LETTERS>1-a|b|c", "look": "...", "prompt": "..."}, ...3]}
