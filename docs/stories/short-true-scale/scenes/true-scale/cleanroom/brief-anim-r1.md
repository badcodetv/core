# Brief: animate five stills for "Nearest Wins" (a BadCode short, 9:16), clean room

You write image-to-video motion prompts for Google Flow's **Omni 1.2 Flash** in **Frames** mode: each still below is the clip's
start frame; clips are **8 seconds, vertical 9:16**. Research the model and the craft on the open web first. Read ONLY this brief
and the five images; open no other file on this machine.

## What the director said (verbatim, Jack, 2026-11-16)
"once the stills are more diverse then we will animate them thanks" … "done thanks carry on". Standing: "Please clean room it all
and research the internet to achieve it."

## The scene (about 25 s, pub quiz night)
The quizmaster asks the tiebreaker ("How many homes in England have been empty six months or more?"); a loud table shouts "Fifty
thousand, tops!"; she reads the answer, 303,185 (plus 267,894 second homes) and "Nearest… table nine. Bob."; a lad asks "How'd you
know that?"; Bob, who lives in a tent, says "I sleep opposite one."; he hands the meat-raffle prize to the next table and leaves.
Voices are recorded separately and laid on in the edit.

## The stills, in order (look at each)
1. `~/.cache/badcode/ts-anim/NW7-1-a.jpg`: the quizmaster lifts a sheet, mic in hand, the regulars listen. (She speaks here.)
2. `~/.cache/badcode/ts-anim/NW6-2b1.jpg`: wide across the shouting room; Bob alone in the corner, writing. (The loud table shouts.)
3. `~/.cache/badcode/ts-anim/NW6-3a.jpg`: the quizmaster holds up the answer, 303,185; foreground groans. (She speaks.)
4. `~/.cache/badcode/ts-anim/NW7-4-a.jpg`: Bob has stood up behind his "300,000" sheet; the room turned toward him. (A lad asks; Bob answers.)
5. `~/.cache/badcode/ts-anim/NW6-5a2.jpg`: Bob sets the meat-raffle prize down for the next table.

## Hard facts
- **The model's audio is not used and there is no speech from it.** Where someone talks, their mouth may move naturally as if speaking (we sync the voice later), but write no dialogue in the prompt.
- **Camera locked** in every clip (any push is added in the edit); say so.
- **Text and numbers must not change**: the "303,185" and "300,000" sheets stay exactly as they are.
- Few movers (about three people moving at most; the rest sit still or barely shift). One clear action per clip, happening in the first 4 seconds.
- Nothing thrown or falling in the air. No cuts: one continuous shot. Keep the look: cheap colour film, grain, warm pub light, teal rain.
- No real brands, no real people. Every prompt ends with the word "Thanks."

## Your task
Research Omni 1.2 Flash / Flow image-to-video prompting (start-frame fidelity, locked camera, natural talking mouths, stable text).
Write ONE motion prompt per still, 60-110 words. JSON to
`/home/jackt/projects/badcode/badcode/docs/stories/short-true-scale/scenes/true-scale/cleanroom/anim-r1.json`:
`{"research": ["url — takeaway"], "notes": "...", "frames": [{"n": 1, "still": "NW7-1-a", "job": "one line", "prompt": "...", "risk": "..."}, ...5]}`
