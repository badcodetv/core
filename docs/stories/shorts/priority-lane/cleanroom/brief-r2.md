# Sealed brief: Priority Lane clips, round 2 (2026-11-11)

You write Google Flow video prompts (model: Omni 1.2 Flash, image-to-video from ONE start frame, 8 seconds, vertical 9:16).
Read ONLY this file. Do not read any other file in the repository.

## The start frame (the same still for both shots)
A TV news reporter stands still in the foreground facing the camera, mid-chest up, holding a grey microphone in a gloved
hand. He wears a black knitted balaclava with a white ring and a red triangle on the face, and a dark coat. Wet city
street at night, rain, an orange streetlamp above. Behind him, soft and out of focus, at a junction: a yellow-and-green
UK ambulance with blue lights, two police motorbikes with riders in hi-vis, dark cars, distant traffic lights.
Never describe his appearance in the prompt (the still carries it); only position, action and what happens around him.

# Priority Lane clips: what came back (baseline for clean room r2, 2026-11-11)

Jack's notes on rough cut 1 (verbatim):
- at 0:08, reporter shot: "The ambulance randomly changes direction. Please fix it, thanks. Please clean room it all and research the internet to achieve it. Thanks."
- at 0:17, button shot: "same here thanks"

What the two clips did (start frame = the reporter still: masked reporter foreground, wet junction at night, yellow-and-green ambulance with blue lights and police motorbikes behind, soft focus):
- Shot 3 (reporter, ambulance should wait): the ambulance starts sideways-on, moves, then appears turned to face the camera, then sits further away. It reads as turning round on the spot.
- Shot 5 (button, ambulance should drive away): the ambulance turns to face camera, then shrinks into the distance. The direction it faces flips mid-move, so it seems to drive backwards.
- Both: the reporter himself is steady, with no morph. The fault is only the background vehicle.
- Flow behaviour on this still: long, detailed prompts were silently refused about 10 times (no clip, nothing returned). This bare prompt went through: "The camera does not move. The man stands still holding the microphone. Behind him, the yellow van drives away. Rain falls. No dialogue, no music. Thanks."

## The research (fresh web research for this job)
## Research r2: the ambulance that turns round (2026-11-11)

This is web research only. No repo files were read. Grades: **OFFICIAL** means Google docs, **REPORTED** means a creator or user source (linked), **GUESS** means my own inference.

### 1. Why the vehicle flips direction mid-clip

- **REPORTED:** Every current text-to-video and image-to-video model, closed commercial ones included, produces "reversal" bloopers: motion running the wrong way, or a possible but improbable path. The suspected causes are training clips that were time-reversed (forwards/backwards augmentation), or clips that were already reversed in the training data. None of this is confirmed by the labs. [Unite.AI, "Why AI video sometimes gets it backwards"](https://www.unite.ai/why-ai-video-sometimes-gets-it-backwards/), on [VideoPhy-2](https://arxiv.org/pdf/2503.06800).
- **REPORTED:** In Veo 3 image-to-video (Gemini app), a car "instantly transforms from sideways to backwards to forward". The author got a better take from a more structured prompt, and from simply re-rolling. [intelligencebyintent](https://intelligencebyintent.com/insights/the-director-in-the-machine-moving-beyond-the-prompt-to-take-control-of-ai-content)
- **REPORTED (paper):** Text alone is too ambiguous to fix a motion path. VLIPP solves this by planning a trajectory with a separate model before generating. [arXiv 2503.23368](https://arxiv.org/html/2503.23368v1)
- **REPORTED:** When the prompt and the start image disagree, the model can oscillate between the two states. [veo3gen troubleshooting](https://www.veo3gen.app/blog/image-to-video-that-actually-moves-not-just-wiggles-a-9-step-troubleshooting-che)
- **GUESS:** The background ambulance is small, defocused and seen at an ambiguous angle, so the model cannot tell its front from its back. The words "drives away" can then be satisfied either by turning the vehicle round or by reversing it. Each extra mover (bikes, police cars, passing traffic) is another interpretation that can drift.

### 2. Prompt techniques that hold a direction

- **OFFICIAL:** In image-to-video, the image already supplies subject, scene and style, so the prompt should be "the motion you want to see" ([Vertex best practices](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice)). Omni wants "specific motion descriptions"; "make it move" does worse ([Omni API docs](https://aistudio.google.com/docs/omni.md.txt)).
- **OFFICIAL:** Camera motion over a static scene is "the simplest and most reliable way to add dynamism" ([Vertex best practices](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice)). Google's Omni camera words include "static", "locked off" and "fixed angle" (Google AI tips, 26 May 2026, as reproduced by [pillitteri.it](https://pasqualepillitteri.it/en/news/3513/mastering-gemini-omni-flash-video-prompting-guide); REPORTED copy of an OFFICIAL post).
- **REPORTED:** State each object's position relative to the camera, and keep the camera on one side ("the 180 axis never flips"), so "nothing flips sides partway through". Too many movers means "five or six interpretations running at once; one drifting is enough to break the scene". [Higgsfield](https://higgsfield.ai/blog/ai-video-prompt-mistakes)
- **REPORTED:** Name the path across the frame ("left to right", "away from camera"). Unqualified verbs vary wildly. [Kling blog](https://kling.ai/blog/ai-video-prompt), [Higgsfield](https://higgsfield.ai/blog/ai-video-prompt-mistakes)
- **OFFICIAL:** Timestamped segments (`[00:00-00:04] … [00:04-00:08] …`) direct timing inside one generation. [Google Cloud Veo 3.1 guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- **GUESS (untested):** Describe the vehicle by what the camera sees, for example "its rear doors and red tail lights face the camera". Then describe the end state, for example "by the end it is small, far down the road". That leaves only one reading. For shot A, write the ambulance as parked with its lights flashing, and put all the motion in the passing traffic.

### 3. Negative phrasing

- **OFFICIAL (Veo):** "Not recommended: using instructive language or words such as 'no' or 'don't'." Describe the wanted thing positively. [Vertex Veo prompt guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide), and [Veo 3.1 guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1): "a desolate landscape with no buildings" rather than "no man-made structures".
- **OFFICIAL (Omni):** Omni has no negative-prompt field. Negatives go in the main prompt ("Do not do X"), and "simple negative prompts" are fine. [Omni API docs](https://aistudio.google.com/docs/omni.md.txt)
- **GUESS:** For Omni, a short negative is not banned, but "does not turn around" still puts the words "turn around" into the prompt. Lead with the positive state ("keeps driving straight away, rear to camera"). Add one short negative only if takes keep flipping.

### 4. Fallbacks other than the prompt

- **OFFICIAL:** Flow with Omni 1.1 Flash has start and end frames ([Google blog](https://blog.google/innovation-and-ai/models-and-research/google-labs/new-creative-controls-google-flow/)). In the API, first+last interpolation runs 3 to 10 s, and any single clip runs 3 to 15 s ([Omni API docs](https://aistudio.google.com/docs/omni.md.txt)). For shot B: make an end still in which the ambulance is gone or tiny far down the road, rear-on. **REPORTED:** big spatial leaps between the two frames cause interpolation artefacts ([eachlabs](https://www.eachlabs.ai/blog/veo-3-1-first-and-last-frame-guide)).
- **GUESS:** A shorter clip (4 to 6 s) gives the vehicle less time to wander, and we can trim any take to the clean stretch before the flip.
- **GUESS:** Plate method. Generate the reporter with the ambulance kept static (shot A is mostly this already). Make the departure as a separate background-only clip, or fake it in Premiere (the ambulance layer scaled down and blurred). Our own rule bans AI people in real footage; it says nothing against AI-on-AI layers.
- **REPORTED:** Re-rolling the same prompt often fixes it ([intelligencebyintent](https://intelligencebyintent.com/insights/the-director-in-the-machine-moving-beyond-the-prompt-to-take-control-of-ai-content)).

### 5. Prompt length and silent refusals

- **OFFICIAL:** Omni filters both the input prompt and the generated video, the filters "vary by region", and violating prompts "are blocked" ([Omni API docs](https://aistudio.google.com/docs/omni.md.txt)). Google publishes no length limit (Vertex: "You don't need to use all elements in every prompt").
- **REPORTED:** Blocks often arrive as vague messages ("I can't generate that…", "something went wrong") or as empty output, which is easy to mistake for a bug ([agentpedia](https://agentpedia.codes/blog/why-gemini-omni-flash-refuses-your-clips), [Google AI forum](https://discuss.ai.google.dev/t/omni-video-editing-instantly-rejects-harmless-prompts-in-flow-and-gemini-app/147152)). Known triggers: real-looking or prominent people, minors, "sensitive acts". Fix by rewriting only the risky element ([laozhang](https://blog.laozhang.ai/en/posts/veo-3-flow-failed-generation)).
- **REPORTED:** A specific sentence of about twenty words beats a generic paragraph ([pillitteri.it](https://pasqualepillitteri.it/en/news/3513/mastering-gemini-omni-flash-video-prompting-guide)).
- **GUESS:** Long prompts fail more because they contain more words that can trip a filter (emergency, police, crash, injury, a "news report" about a real-looking place), not because of their length. Each added word is another chance to hit one.

### What a prompt writer should do

- Keep it short: one or two sentences, about 20 to 40 words, written as motion only. The still already carries the look.
- Lock the camera ("static, locked-off shot") and give the reporter a minimal action, so the ambulance is the only story in the background.
- Shot A: make the ambulance a non-mover ("parked, blue lights flashing, stays in place") and give all the motion to one stream of traffic in one named direction ("cars pass left to right").
- Shot B: name the ambulance's orientation and path against the frame ("rear doors toward the camera, it pulls straight ahead down the road, away from us"), and say where it ends ("small in the distance, then gone").
- Cut the other movers in shot B: write the police bikes and cars as stationary, or leave them out.
- State everything positively. If takes still flip, add at most one short negative ("it never turns").
- If two or three re-rolls still flip, switch to start + end frame (an end still with the road empty or the ambulance tiny), or use a 4 to 6 s clip and trim, or composite the departure in Premiere.
- If a prompt is silently refused, strip the emergency and news words first (police, emergency, accident, breaking), not the motion. Then run `fresh.py` before sending.

## The task
Write prompts for two shots. Each prompt must be SHORT (aim for 20-45 words; the long ones were silently refused),
plain, positive, camera locked, the reporter holding still, no speech and no music, and end with the word "Thanks."
Avoid the words police, siren, emergency, masked and news; call the ambulance "the yellow ambulance" or "the yellow van".

- **Shot 3, "the ambulance waits":** the reporter holds still while, behind him, the ambulance stays exactly where it is,
  blue lights flashing, and a line of dark cars slides past in one direction. The ambulance must not move at all.
- **Shot 5, "the ambulance finally goes":** the reporter holds still while the ambulance behind him finally drives
  straight away from the camera, down the road, its back to us the whole way, getting smaller until it is gone.
  It must keep one direction from start to finish.

Write TWO different prompts per shot (A and B) that take genuinely different approaches, informed by the research.
Return JSON only: {"shot": <3 or 5>, "prompts": [{"id": "A", "approach": "...", "prompt": "..."}, {"id": "B", ...}]}
