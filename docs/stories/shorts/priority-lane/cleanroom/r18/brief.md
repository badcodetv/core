# Brief round 18: every still of the short, rebuilt from real photos

You write image prompts for Google Flow's Nano Banana 2. Read ONLY this file, `geometry.md`, and the images listed
below (open each). Research the web if useful. No real person's name anywhere.

## The film in plain facts
A 20-second vertical (9:16) satirical short, rainy night in London. Inside an ambulance paramedics are losing a patient.
They pass a bus stop with a minister's SAVE OUR NHS poster. Police hold a junction so the minister's convoy can cross;
the ambulance is stopped. The minister, in the back of his car, chats on the phone. The patient flatlines.

## The method (the director's ruling)
Each shot is built ON a real photo: in Flow the photo is attached as a reference image, and the prompt says to keep that
photo's real layout, proportions, camera position and light, and only change or add what the shot needs. Write it as:
"Keep the real layout, perspective and lighting of the reference photo; [then what to add or change]". Describe only
what should be in the picture (never name the thing to leave out). Under ~200 words per prompt. The shot's facts first.

## The look: one line
Night in the rain, like a real 35 mm film photo: wet tarmac, sodium-orange street lamps, cold teal shadows, blue
emergency lights.

## Rules
- Vertical 9:16. No readable text anywhere except the poster's SAVE OUR NHS. End every prompt with "Thanks."
- Any traffic or vehicle position must obey geometry.md (UK: keep LEFT; driver on the RIGHT).

## The shots: write 2 prompts each (ids <code>-a, <code>-b) into `prompts.json`, plus a field "refs" listing the
image file names to attach for that prompt (exactly as named below)

1. **LS18 · Losing him.** Reference: `/home/jackt/.cache/pl-refs/us/u_C53CnEp-hsU.jpg` (a real ambulance interior with crew). Two UK paramedics in
   dark green uniforms and surgical masks work over a patient on the stretcher, the monitor racing, urgency.
2. **PB18 · His poster, from the bus-stop seat.** References: `/home/jackt/.cache/pl-refs/us/u_csDVMvtsS50.jpg` (a real bus shelter at night: bench,
   lit blank ad panel, the road beyond) AND `/home/jackt/.cache/pl-refs/us/PA12-a.jpg` (the poster artwork). Put "the poster from the second
   reference image, reproduced exactly, the same man's face" into the lit panel, big and readable; make it night rain;
   a UK ambulance (yellow-green Battenburg, blue lights) coming toward the camera in the lane nearest the shelter's kerb,
   the kerb on its left. Do not describe the man or the poster.
3. **CD18 · The cordon, from above.** References: `/home/jackt/.cache/pl-refs/us/u_uCn2fI8PdZQ.jpg` (a real elevated view along a London road) AND
   `/home/jackt/.cache/pl-refs/us/u_lVsmbu6rQRc.jpg` (a real motorcade with police outriders, seen from above). Night rain; the junction exactly as
   geometry.md: the ambulance at its stop line in the left half with its back to us, a police line of white motorcycles
   and hi-vis officers across our side, the convoy (led by outriders like the second photo) CROSSING left to right in
   the far half of the junction, the oncoming queue on the right held by police.
4. **HD18 · Held, from the ambulance cab.** References: `/home/jackt/.cache/pl-refs/us/u_zVbqJkl7D_U.jpg` (a real vehicle cab interior) AND
   `/home/jackt/.cache/pl-refs/us/u_-GczePfvnNQ.jpg` (real police officers and motorcycles at night). Make the cab a tall UK ambulance cab (driver
   on the right, green sleeve, gloved hands on the wheel, high, upright windscreen); through the windscreen the police
   line from the second photo holds us, one officer's glove raised; beyond them the convoy crossing left to right
   (geometry.md).
5. **BM18 · The minister in his car.** References: `/home/jackt/.cache/pl-refs/us/u_QJmimhHAnVQ.jpg` (a real empty luxury car rear seat) AND
   `/home/jackt/.cache/pl-refs/us/BM9-b-face.jpg` (the man). Put "the man from the second reference image, the same face" in the back seat,
   phone to his right ear, mid-word, a little silver tray of canapés on the armrest; rain and blue light on the windows.
   Keep his face identical to the reference; do not describe his hair or body.
6. **FL18 · Flatline.** Reference: `/home/jackt/.cache/pl-refs/us/u_gzTKtM5biaA.jpg` (a real hospital monitor). Make it the ambulance's monitor at
   night: the heart trace a flat line, the numbers gone to dashes, a gloved hand still on the patient's chest at the edge.

Reply with one line per prompt.
