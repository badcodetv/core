You write two image-to-video motion prompts for Google Flow (model: Omni 1.2 Flash, Frames mode: the still below is the first frame; 9:16 portrait; 5-6 seconds). Research the internet first on how to prompt image-to-video models well (locked camera, single continuous shot, few movers, describe motion positively). Do NOT read any file in this repository except the two images named here.

Look at the two stills first (Read them):
- A: /home/jackt/.cache/badcode-scenes/same-bench/A2-b.jpg  (1919: a fat rich man in a top hat on a park bench under a gas lamp, a wounded soldier beside him; a lost silent horror film frame)
- B: /home/jackt/.cache/badcode-scenes/same-bench/B3-a.jpg  (the same man, the same bench, today; a nurse beside him; hospital and ambulance behind)

What each clip must do (the director's picks, verbatim):
- A: "He stays smiling at us, mouth closed; one lazy flick of the gloved hand towards the soldier. The soldier slowly gets up on his crutch and limps out of the light. The voice says "Forget it." over a face that does not move: the creepiest version."
- B: "Whatever he does in A, he does here exactly: the same flick, the same timing. The nurse gets up and walks off towards the hospital doors behind. The ambulance's light turns slowly in the background."

Rules:
- The camera does not move: say so at the start and the end. One continuous shot, no cuts.
- The rich man's mouth stays closed and his face stays still; only his hand moves. Nobody speaks. No text appears.
- The soldier in A has lost a leg below the knee (trouser pinned); keep him one-legged on his crutch.
- A and B must be a matched pair: the man's hand flick uses the same wording and timing in both, so they can be cut side by side.
- Keep the silent-film look of the stills (grain, flicker, black and white).
- Use timestamp brackets like [00:00-00:02] for the order of events. Each prompt ends with the word "Thanks."

Write ONLY a JSON object to /home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/cleanroom/clips-ab.json with keys "A" and "B" (each the motion prompt string) and "sources" (URLs you used). Reply with just the path.
