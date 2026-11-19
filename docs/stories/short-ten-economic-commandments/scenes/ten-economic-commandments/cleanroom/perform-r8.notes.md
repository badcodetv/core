# perform-r8 notes

22 prompts: 11 stills x 2 options. Option "a" is the big one (pointing at the lens, hard hand chops on the beat). Option "b" is the laid-back one (head nods, shoulder bounce, mic close under the mask).

## How the prompts are built
- They open with "Static locked-off camera" and close with "Camera stays locked off". Google's Veo prompt guide calls a static/fixed shot one where the camera stays completely still, and one third-party guide notes Veo 3.1 tends to add a subtle handheld drift unless you tell it otherwise. That's why the camera is pinned at both ends.
- In image-to-video the start frame already fixes his look, the lighting and the style (per Google's best-practice page), so each prompt gives only a short reference to the place and spends its words on motion. Every prompt ends with the same identity tail (face to camera, mask still, outfit unchanged, no skin, no new people, no text). Replicate's guidance is that repeating identical wording across generations keeps a character consistent.
- I found no source on syncing body motion to a beat in Veo. So the tempo is written as a concrete count ("slow 90 bpm", "on every beat") and tied to specific body parts (hand chops, nods, knee bounce, heel taps), not to vague words like "dances". Check the results in the edit. One guide reports Veo 3.1 follows specific step-by-step motion wording better than earlier versions did.
- Nothing about the face moves, and there are no mouth or lip-sync cues. All the rapping is done by the head, shoulders and hands.
- Background motion only comes from what the still already has: city lights (Empire State), the parked train and far-off commuters (subway), neon flicker (shop), leaves (columns), lamps (walkway), bare branches (court, stoop), the flag (stoop), and the mic cord (balcony).

## Per-still notes from looking at the images
- F6-r10-bailout2-b: the figure is small and no mic is clearly visible, so the prompts say "the hand at his chest" and "his lower hand" and don't mention a mic. The marble floor reflection should follow him.
- F6-vibe4-b: he is mid-stride, side-on, with no mic. With the camera locked, a walk would carry him out of frame within 8 s. So option a stops him at the door and option b has him strut on the spot. His head is already turned to camera, and the prompt holds it there. Hands are named "raised" and "lower", not left and right.
- F6-vibe7-a: the chain-link fence is in the foreground, so the prompts say it stays still to keep it from warping.
- F6-vibe8-a: he is small at the right edge, behind barriers. Option a lets him push off the taxi briefly and settle back.
- F6-vibe9-b: low angle from below, so "pointing down at the lens".
- Left/right hands are the subject's own and were checked against each still (mic hand vs pointing hand).

## Sources
- [Veo prompt guide (Google Cloud)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)
- [Veo best practices (Google Cloud)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice?authuser=1)
- [Ultimate prompting guide for Veo 3.1 (Google Cloud blog)](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1?authuser=2)
- [Using and prompting Veo 3 (Replicate)](https://replicate.com/blog/using-and-prompting-veo-3)
- [Veo 3.1 on Replicate](https://replicate.com/blog/veo-3-1)
- [Veo prompt guide (LTX)](https://ltx.io/blog/veo-prompt-guide)
- [Veo 3.1 image-to-video (VEED)](https://www.veed.io/ai-models/image-to-video/veo-3-1-img2vid)
- [Veo 3.1 prompt guide (Akool)](https://akool.com/blog-posts/google-veo-3-1-video-prompt-guide)
