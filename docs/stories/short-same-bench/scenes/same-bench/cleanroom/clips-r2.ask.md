You rewrite two image-to-video motion prompts for Google Flow (Omni 1.2 Flash, Frames mode: the still is the first frame; 9:16; 6 seconds) after the director's notes. Research the internet first on how to stop image-to-video models walking people through furniture and how to control the direction of a head turn. Do NOT read any file in this repository except the files named here.

Read the stills: /home/jackt/.cache/badcode-scenes/same-bench/B3-a.jpg and /home/jackt/.cache/badcode-scenes/same-bench/C3-a.jpg
Read the previous prompts (they made the clips the director noted): /home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/cleanroom/clips-ab.json (key "B") and /home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/cleanroom/clips-c.json (key "C").

The director's notes, verbatim:
- On B: "she walks through the bench redo this please thanks"  (in the clip the nurse stood up and walked backwards straight through the bench towards the hospital)
- On C: "he should look to the right not the left thanks"  (he turned his head to the left side of the frame; he must turn to the RIGHT-hand side of the frame, as the viewer sees it. Also, as he turned, his eyes came out of the hat's shadow and his face changed into an ordinary man: keep his eyes as black hollows in shadow and the same face all the way.)

Keep everything else the previous prompts asked for (locked camera, one continuous shot, the man's hand flick in B with his mouth closed, the silent-film look, no speech, no text, timestamps, ending with "Thanks.").

Write ONLY a JSON object to /home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/cleanroom/clips-r2.json with keys "B", "C" and "sources". Reply with just the path.
