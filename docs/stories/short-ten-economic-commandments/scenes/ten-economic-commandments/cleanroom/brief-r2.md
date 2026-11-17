# Brief: round 2 stills for a BadCode short, "Ten Economic Commandments" (9:16), clean room

You write prompts for Google's **Nano Banana 2** image model (in Google Flow). These stills set the world and the
character of the short; the director picks from them. Research first, on the open web, fresh. Read ONLY this brief and
the reference images named below; open no other file on this machine.

## What the director said (verbatim, Jack, 2026-11-16)
"use these for the setting, make the badcode guy look like andrew callaghan, with the suit and the hat. please make the
stills, Please clean room it all and research the internet to achieve it. Thanks."

## The short
A parody of a famous 1997 New York rap song about ten street-hustle rules, turned on the money printer: "never get high
on your own supply" means whoever holds the printer helps themselves to the fresh money first. The fix: no human hand
controls the printer. From the makers' meeting: the evil is a force you can't see, a system, not one villain.
The BadCode figure delivers the commandments, like a street MC / street reporter, out in the city.
Beats: **A. The commandments** (`rules`, letters `RU`) · **B. Own supply** (`supply`, `SU`) · **C. No human hands** (`fix`, `FX`).

## The setting: four reference photos (look at each)
- `~/.cache/badcode/tec-refs/ref1-fence-bench.png`: a 1980s New York street portrait, three young people on a bench in
  front of a chain-link fence and payphone booths, warm late sun, faded film colour, street style posing.
- `~/.cache/badcode/tec-refs/ref2-subway-watermarked.png`: a subway platform, a train blurring past, commuters in
  motion blur, one still figure seen from behind. 🔴 It carries stock-site watermarks: **never attach this one**;
  describe its idea in words instead.
- `~/.cache/badcode/tec-refs/ref3-street-crowd.png`: a crowded city street at dusk, long lens, one man sharp among
  blurred passers-by, orange traffic lights as bokeh, tall buildings fading into haze.
- `~/.cache/badcode/tec-refs/ref4-bridge-street.png`: a cobbled street between brick warehouses with a huge steel
  suspension bridge tower framed at its end, low winter sun, deep shadow, film grain.
You may attach refs 1, 3 and 4 as setting/style references (say in your output which, per prompt), or describe them.

## The BadCode guy
The director wants him dressed like a well-known American comedian-interviewer (look him up: **Andrew Callaghan**, of
the street-interview show; his trademark outfit). Take **only the outfit and the posture**: the oversized thrift-shop
suit, the hat, the long-foam street-interview microphone if it fits. 🔴 Never write that person's name, or any real
person's name, in a prompt, and never describe a face: the figure's face is fully covered by the BadCode balaclava.
Describe the balaclava with this sentence, verbatim:
"The balaclava has no eye, nose or mouth holes, so no skin shows anywhere; a large white ring is stitched round the whole face, and one small red triangle with rounded corners, pointing down, sits high inside the ring on the right-hand side of the picture. Gloves on both hands; no robot parts."
The hat sits on top of the balaclava; the gloves cover the hands (no skin anywhere).

## Rules
- No text, lettering, logos or brand names anywhere unless a prompt deliberately needs a short line of words (spell it
  out exactly); the reference photos contain brands: leave them out.
- No real person's face or name. Bystanders are invented and varied (age, ethnicity, build).
- Vertical 9:16. Make the stills genuinely DIFFERENT from each other (lens, time of day, place among the four settings,
  staging, how much of the city vs the figure), not re-seeds. Avoid the glossy generic AI look: real lens and film
  language, motivated light, imperfection, as the references are.
- Every prompt ends with the word "Thanks."

## Your task
Six prompts, two per beat, 70-130 words each, each with a short "look" label and which refs (1, 3, 4, or none) to attach.

## Output
JSON to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/scenes/ten-economic-commandments/cleanroom/prompts-r2.json`:
`{"research": ["url — takeaway"], "notes": "...", "stills": [{"beat": "rules|supply|fix", "id": "RU2-a|RU2-b|SU2-a|SU2-b|FX2-a|FX2-b", "look": "...", "refs": [1,3], "prompt": "..."}]}`
