You write one image-to-video motion prompt for Google Flow (model: Omni 1.2 Flash, Frames mode: the still below is the first frame; 9:16 portrait; 4-5 seconds). Research the internet first on how to prompt image-to-video models well (locked camera, single continuous shot, describe motion positively, keep a face stable during a head turn). Do NOT read any file in this repository except the image named here.

Look at the still first (Read it): /home/jackt/.cache/badcode-scenes/same-bench/C3-a.jpg  (a fat rich man in a top hat alone on a park bench under a gas lamp, lifting his hat towards us; a lost silent horror film frame)

What the clip must do (the director's pick, verbatim): "Mid hat-tip, his head turns slowly to the empty seat beside him, as if someone new has just sat down off screen. Iris closes to black." (The iris close is done in the edit; your clip just ends on him looking at the empty seat.)

Rules:
- The camera does not move: say so at the start and the end. One continuous shot, no cuts.
- His face must stay the same face as he turns; his eyes stay hidden in the shadow of the hat brim; his mouth stays closed in the smile. Nobody speaks. No text appears. Nobody else appears in frame.
- Keep the silent-film look of the still (grain, flicker, black and white).
- Use timestamp brackets like [00:00-00:02] for the order of events. End with the word "Thanks."

Write ONLY a JSON object to /home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/cleanroom/clips-c.json with keys "C" (the motion prompt string) and "sources" (URLs you used). Reply with just the path.
