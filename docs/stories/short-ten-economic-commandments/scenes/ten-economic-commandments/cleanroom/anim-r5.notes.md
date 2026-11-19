# anim-r5 notes: sources and approach

## What the research said
- Google's Veo prompt guide (Vertex AI) defines a static or fixed shot as one where the camera "remains completely still". Each prompt opens with "Static locked-off camera, fixed shot" and ends with "The camera does not move at all."
- The Gemini Omni prompt guide says to ask for "static", "locked off" or "fixed" framing, and to say what should stay the same. So each prompt names the solid parts of the photo (buildings, columns, signs, bars) that stay rigid and exact.
- Veo best practices say the source image is the basis for everything that follows. Replicate's Veo image-to-video write-up says the model keeps the input's style without extra help. So the prompts describe motion only and say nothing about look or style.
- Veed's Veo 3.1 and Wan guides say to start with simple static shots and small, specific motions rather than big changes of perspective. Each prompt has one or two clear motions.
- Negative lists are kept out of the prompts. Instead, each prompt says in positive terms what stays the same (lettering unchanged, only torso and legs shown, background stays blurred, the figure "already there").

## Per-still notes
- U5-r10-bailout2: the photo shows only the colonnade. No skateboarder is visible, so neither prompt mentions one.
- U5-r3-press2, U5-vibe5, U5-vibe3, U5-vibe4: these photos already contain people. The prompts move only those people and keep blurred ones blurred. The boombox walker stays cropped at the torso.
- U5-vibe8: option a reveals the wall behind the taxi when it leaves, so it needs some invented background. Option b is the safer one.
- U5-r8-debase1 option a, U5-fix1 option b and U5-r4-supply2 option b are the "money gets weaker" or "lights out" readings.

## Sources
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice
- https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- https://deepmind.google/models/gemini-omni/prompt-guide/
- https://support.google.com/flow/answer/16353334
- https://ai.google.dev/gemini-api/docs/omni
- https://replicate.com/blog/veo-3-image
- https://dhl.veed.io/learn/veo-3-1-prompts
- https://www.veed.io/learn/wan-2-5-prompting-guide
