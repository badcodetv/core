# Brief: Priority Lane round 11 (common to every writer)

You write image prompts for Google Flow's Nano Banana 2 (a still-image model). Read ONLY this file and your own
shot brief in this folder. Do not open any other file in the repository. Research the web freely (how Nano Banana 2
handles text, faces, reflections, crowds; what the real-world things in your shot look like in the UK).

## The film, in plain facts
- A ~20-second vertical (9:16) satirical short. Rainy night in London. Inside an ambulance, paramedics shout that they
  are losing the patient. Police have closed a junction so a government minister's car can cross; the ambulance is
  held. The minister, on the phone in the back of his car, is arranging a trip. The patient dies.
- The minister is an invented man with a look described only by the reference image attached in Flow. Never write a real
  person's name, never a real party's name, logo or colours, never "looks like <real person>".
- The look of the whole film: a real 35 mm colour-negative film photo taken at night in the rain, not CGI. Wet tarmac,
  sodium-orange street lamps, cold teal shadows, visible film grain, slight halation, blue emergency lights cutting
  through. Ordinary London streets. Never glossy, clean, daylight or "cinematic CGI".

## Rules for every prompt
- One prompt = one paragraph, written fresh in your own words. Vertical 9:16. Photo-real.
- Name every light source in the scene.
- No readable text anywhere except what your brief asks for (no plates, signs, route numbers, logos).
- Faces and hands must be natural; no extra fingers.
- End every prompt with the word "Thanks."

## Output
Write a JSON array of objects `{"id", "look", "prompt"}` to the file your brief names. `look` is a 2-5 word name for the
idea. Each prompt in your file must be a genuinely different idea (camera, staging, light), not a reworded copy.
Reply with one line per prompt: id, look, and what makes it different.
