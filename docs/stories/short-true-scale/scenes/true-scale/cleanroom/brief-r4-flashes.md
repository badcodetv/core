# Brief r4: the two emotional flashes in "True Scale" (a BadCode short, 9:16, ~14 s)

Read ONLY this brief and the images it names. Research on the open web first, fresh. You write prompts for Google's
**Nano Banana 2** image model, vertical 9:16.

## What the director said (verbatim, Jack, 2026-11-16)
"i think we just stick to graphics of the orginal idea, show the stats and the scale of the stats, with flashes of emotional
imagary like the bench, the happy home, maybe we incorpate bob from the camping story" … "i dont really know what to do with this
short, since just showing stats is boring, and if its emotional it might be seen as too left wing". Then, on this shape:
"lets do this":
1. **Bob on his bench** (flash, ~3 s): a regular bloke who lost it all in 2008, not "them".
2. 134,210 homeless households in England (a true-scale graphic, pull back).
3. **A warm, lit, happy home** (flash, ~2 s).
4. 303,185 long-term empty homes and 267,894 second homes beside them (graphic, pull back further).

## Who Bob is (from our film "Camping")
In 2008 Bob was a normal, nice guy, a middle manager, married. He lost everything (his wife died; the job went). Now, years later,
he lives in a tent in a supermarket car park, ignored by every customer walking past. He did not fall because he was lazy. He is
the viewer five bad years later: the flash must make the viewer see a regular bloke, not "a homeless person". His look is fixed by
his reference sheet, which will be attached to the generation: `/home/jackt/projects/badcode/badcode/docs/stories/camping/characters/img/bob-sheet.jpg`
(look at it). **Never describe his appearance, clothes, age or face in the prompt** (the reference carries it, and describing it
fights it): only where he is, what he is doing, his posture and expression, the light and the camera.

## The look
Night, cheap colour film, grain, cold fluorescent teal (reference photo:
`/home/jackt/projects/badcode/badcode/docs/stories/short-malevolent-force/scenes/malevolent-force/reference/jack-r2-shop-doorway.png`).
The happy home is the one warm thing in the film: it may break the teal on purpose (warm lamp light seen from outside, or inside),
so the contrast hurts. Not a lecture, not charity-advert misery: dignity, ordinariness, a beat of recognition.

## Rules
Vertical 9:16. No real brands (no supermarket names or logos), no real people, no readable text. The happy home: a family may be
shown, from behind, in silhouette, or soft at a distance (the image model often refuses close images of children). Every prompt
70-130 words, ends with the word "Thanks."

## Your task
Write THREE genuinely different options for your one flash (different angle, place, moment), and JSON to the path you are given:
{"research": ["url — takeaway"], "notes": "...", "stills": [{"beat": "<key>", "id": "<ID>-a|b|c", "look": "...", "prompt": "...", "uses_bob_reference": true|false}, ...3]}
