# Brief: animate a BadCode rap short, "Ten Economic Commandments" (9:16), clean room

Research on the open web first (Google Flow's **Omni 1.2 Flash** image-to-video, Frames mode; and Google's **Nano Banana 2** for stills; and how to avoid the glossy "AI slop" look). Read ONLY this brief and the images named below; open no other file on this machine.

## What the director said (verbatim, Jack, 2026-11-16)
On the fire-escape wide: "you need to ffix this one it looks terrible and like ai slop thanks". Standing: "Please clean room it all and research the internet to achieve it."

## The short
A 29-second parody of a famous 1990s New York rap countdown song, turned on the money printer. A masked figure (BadCode) in a baggy beige suit and cap delivers it around New York. The track (already made) runs:
- 0-5 s intro: "Money printer manual. Take notes."
- 5-10 s rule one: "never tell 'em what you printed, trillions out the back door…"
- 10-15 s rule two: "never get high on your own supply, banks took the first hit, now the rent's sky-high"
- 15-21 s rule three: "no consignment… they took the bailout on tick and they ain't paid at all"
- 21-24 s the fix: "No hand on the printer."  then the beat out to 29 s.

## Job 1: two new stills to replace the fire-escape wide (look at `~/.cache/badcode/tec-anim/slop-FX4-2-b.jpg`: the director called it AI slop)
The idea stays: the lone masked figure, small, in a real New York street under the steel bridge, holding his microphone out to nobody (the fix: nobody's hand on it). Make it look like a real photograph taken by a person: real lens, real light, imperfection, not a postcard. Two genuinely different takes (`FX5-a`, `FX5-b`), Nano Banana 2, 9:16, 70-130 words each, ending with the word "Thanks.".

The figure, always: a baggy beige suit with FULL-LENGTH trousers to the shoes, black socks, a black roll-neck under the jacket, a plain cap with no logo, black gloves running into the cuffs. **No skin anywhere.** The balaclava, described with this sentence verbatim:
"The balaclava has no eye, nose or mouth holes, so no skin shows anywhere; a large white ring is stitched round the whole face, and one small red triangle with rounded corners, pointing down, sits high inside the ring on the right-hand side of the picture. Gloves on both hands; no robot parts."
No text, logos or brand names. No real person's name or likeness.

## Job 2: one motion prompt for each picked still (look at each image in `~/.cache/badcode/tec-anim/`)
`RU4-1-b` (doorstep, chalkboard), `RU4-2-a` (red studio), `RU4-3-a` (fence bench with two locals), `RU4-5-b` (dusk crowd, mic held out), `SU4-1-a` (subway platform, fanning banknotes), `SU4-3-b` (bridge street, notes falling), `FX4-1-b` (night streetlight, empty gloved hands raised). The still is the start frame; 8 s; Omni 1.2 Flash; vertical 9:16.
- 1990s rap-video energy: the figure moves with the beat (a nod, a lean, a gesture), the world moves around him. Each clip one continuous shot, no cuts.
- **Nobody speaks, sings or mouths words** (the voice is added later; the mask has no mouth anyway). Sound effects only.
- **Every mask keeps facing the camera** the whole time; the white ring and red triangle stay visible and unchanged.
- No skin ever appears; nothing in the frame changes text or numbers (the chalkboard stays as it is).
- 40-90 words each. **Do NOT end a motion prompt with "Thanks."** or any sign-off.
- Say for each which part of the track it is for (intro / rule one / two / three / fix / outro).

## Output
JSON to `/home/jackt/projects/badcode/badcode/docs/stories/short-ten-economic-commandments/scenes/ten-economic-commandments/cleanroom/anim-r1.json`:
`{"research": ["url — takeaway"], "notes": "...", "stills": [{"id": "FX5-a", "prompt": "..."}, {"id": "FX5-b", "prompt": "..."}], "clips": [{"still": "RU4-1-b", "part": "intro", "prompt": "..."}, ...7]}`
