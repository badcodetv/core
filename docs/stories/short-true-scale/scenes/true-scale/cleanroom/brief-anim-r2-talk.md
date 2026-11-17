# Brief: talking clips for "Nearest Wins" (a BadCode short, 9:16), clean room

You write image-to-video prompts for Google Flow's **Omni 1.2 Flash** in **Frames** mode (the still is the start frame; 8 s;
vertical 9:16). Research Omni / Flow talking-head and lip-sync prompting on the open web first. Read ONLY this brief and the three
images; open no other file on this machine.

## What the director said (verbatim, Jack, 2026-11-16)
On fixing the lip sync: "reshoot thanks". Standing: "Please clean room it all and research the internet to achieve it."

## Why
The voices are recorded separately (we lay them on afterwards). The first clips were made with no words in the prompt, so the
mouths move at random. These new clips must have each speaker's mouth say **exactly these words**, so the recorded voice fits.

## The clips (look at each still)
- **1a** from `~/.cache/badcode/ts-anim/NW7-1-a.jpg`: the quizmaster (the woman with the mic, sheet raised) says: Tiebreaker! Nearest wins the meat raffle.
- **1b** from the same still: the quizmaster says: How many homes in England have been empty six months or more?
- **3a** from `~/.cache/badcode/ts-anim/NW6-3a.jpg`: the quizmaster (holding up the 303,185 sheet) says: Three hundred and three thousand. Not counting two hundred and sixty-seven thousand second homes.
- **3b** from the same still: the quizmaster says: Nearest... table nine. Bob.
- **4** from `~/.cache/badcode/ts-anim/NW7-4-a.jpg`: the young man in the hi-vis vest, turned toward the standing man, says: How'd you know that? Then the standing man with the rucksack (he is Bob) answers: I sleep opposite one.

## Hard facts (each one learnt the hard way)
- Write the line as `She says: <words>` / `He says: <words>`, **with no quotation marks**, the exact words above and nothing else said. Nobody else in the frame talks.
- **Do NOT end the prompt with "Thanks."** (or any sign-off): Omni speaks it aloud.
- The speaker talks at a natural, unhurried pace and the words fill most of the clip; the mouth is clearly visible and lit.
- Camera locked, one continuous shot, no cuts. Few movers: the speaker, a small reaction from one or two listeners.
- Text and numbers in the frame do not change (the 303,185 and 300,000 sheets).
- Keep the look: cheap colour film, grain, warm pub light, teal rain on the windows. No real brands, no real people.

## Output
JSON to `/home/jackt/projects/badcode/badcode/docs/stories/short-true-scale/scenes/true-scale/cleanroom/anim-r2-talk.json`:
`{"research": ["url — takeaway"], "notes": "...", "clips": [{"key": "01a", "still": "NW7-1-a", "words": "...", "prompt": "..."}, ... for 01a, 01b, 03a, 03b, 04]}`
Each prompt 50-100 words.
