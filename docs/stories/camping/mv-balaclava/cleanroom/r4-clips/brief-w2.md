# The job

You write image-to-video motion prompts for a music video: two masked men rap to camera in a UK rap song about homelessness and wealth. Each prompt animates one approved still for 8 seconds.

# What the director has said, word for word

"basically what i want is for it to stay the same, however when Bob or Tarquin are rapping to the camera, i want them to be replaced with badcode balaclava men, ones homless and one is posh ... then make the clips and only replace the parts where they are rapping". On the masks: "make sure they never show skin". And today: "basically just anything with them talking to the camera is rapping, just replace those ones".

On clips for a sister video with the same masks: "everything is so exaggerated please make it simple" · "cars pop in and out of frame, please keep it simple" · "ai slop lets just remove this one". He wanted the masked men "rapping to the camera and gesturing like eminem".

# Facts about these clips

- A UK rap song about two men, one homeless and one rich, each rapping a verse to camera. Each still becomes the FIRST frame of an 8-second clip (Google Flow, its fast video model, 16:9, 720p). It replaces an existing rap-to-camera clip, cut to the song, so it should rap with the same energy and the same kind of gestures as the original (the strip shows the original clip, two frames a second, left to right, top row first).
- The masked men have no mouth and no eyes: rapping is hands, head and shoulders on the beat. Hands do the words.
- The mask must keep its shape the whole clip: a white ring round the face and a small red triangle high on the right side of the picture, over his left eye. That triangle drifts or slides in motion if the head turns a lot, so keep the head facing the lens; nods and leans are fine. Gloves stay on, no skin anywhere, ever.
- The camera stays still in the clip; the editor adds camera moves. Say so.
- No speech or singing in the clip audio; the song goes on top. Ambient sound is fine.
- Nothing new enters the frame; everything in the background stays what it is.

# Your 3 shots

## s05 — the rough sleeper (a full grey duct-tape hood)
Picked still (the first frame): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/moodboard/s05r3-b.jpg
The original clip it replaces, as a strip: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/originals/strip-s05.jpg
The cut shows up to 8.8 s of it in one go.
The still's prompt was:
Night under a London flyover, a medium shot at eye level, 35mm lens, the man walking toward the camera slightly off-centre right. His tape hood, bomber jacket, scarf and gloves are exactly as in the attached reference: a closed grey tape face with no holes, the white ring around it, and the red triangle high on the right-hand side of the picture at about two o'clock, over his left eye. Mid-stride, one gloved hand swinging down hard on the beat, the other loose at his side, shoulders turned. Black gloves on both hands, jacket cuffs over the wrists, scarf closed to the jaw, no skin. Behind on the left an oil drum burns with tall flame; small domed tents sit under the concrete deck between pillars covered in blurred unreadable graffiti; flattened cardboard and a bin bag on the ground. Firelight and cold sodium, grain.

## s06 — the rough sleeper (a full grey duct-tape hood)
Picked still (the first frame): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/moodboard/s06r3-b.jpg
The original clip it replaces, as a strip: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/originals/strip-s06.jpg
The cut shows up to 6.2 s of it in one go.
The still's prompt was:
Night on the Thames embankment in London, a medium shot at seated eye level, 35mm lens. The man sits on the pavement with his back against the granite river wall, a small green dome tent beside him on the right, a foil tray of coins at his feet, the lit dome of St Paul's across the water behind him between iron lamp posts. His tape hood, bomber jacket, scarf and gloves are exactly as in the attached reference: a sealed grey tape face with no openings, the white ring around it, and the red triangle high on the right-hand side of the picture at about two o'clock, over his left eye. Both gloved hands open and spread toward the lens, mid-verse. Black gloves on both hands, cuffs over the wrists, scarf closed at the neck, dark trousers over boots, no skin. Globe lamps, cold night, grain.

## m12 — the rough sleeper (a full grey duct-tape hood)
Picked still (the first frame): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/moodboard/m12r3-b.jpg
The original clip it replaces, as a strip: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/originals/strip-m12.jpg
The cut shows up to 1.0 s of it in one go.
The still's prompt was:
Night under a concrete flyover, a medium shot from hip to just above the head, 35mm lens at chest height, the man standing centre facing the camera. His tape hood, bomber jacket, scarf and gloves are exactly as in the attached reference. The face is closed grey tape with no eye holes and no mouth hole; the white ring circles it, and the red tape triangle sits high on the right-hand side of the picture at about two o'clock, over his left eye. Weight on one leg, chin up, both gloved hands hanging low and loose in front of his thighs, fingers splayed, about to drop into the next bar. Black gloves on both hands, jacket cuffs over the wrists, scarf closed at the jaw, no skin. On the left of frame an oil drum burns high, throwing warm light across him; graffiti-covered pillars blurred beyond reading behind. Grain, crushed blacks.


# Web research

# Clean-room research: image-to-video clips (Omni Flash in Flow; Veo 3.x Fast as nearest documented relative)

Web only, 2026-11-03. Tags: [vendor] = Google or the tool maker; [tested] = someone ran it and reported results; [reported] = blogs, forums, press; [inference] = my reasoning, not evidence. **Thin** = one weak source.
Overall caveat: Google has published no prompting guide for Omni Flash itself (none found). Most of what follows is Veo documentation plus third-party blogs. Every rule here is a starting point to test.

## 1. Writing the prompt

- Image-to-video: the start image sets character, lighting and style. Describe **only the motion**. Re-describing subject, background or lighting "confuse[s] the model and lead[s] to poor results" [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice
- Call subjects by general terms ("the man", "they", "the figure on the left") rather than re-describing them [vendor] (same URL).
- Three motion kinds, which can be combined: camera move over a static scene, subject animation, environment animation [vendor] (same URL). In practice, pick one primary [reported, below].
- One focused moment per clip. Chaining several events "often leads to muddled or incomplete videos" [vendor] (same URL).
- Text-to-video formula: [Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]. In image-to-video, keep cinematography and action, and drop the rest because the image supplies it [vendor + inference] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- Camera vocabulary Veo documents: static, pan, tilt, dolly, truck, pedestal, zoom, crane, aerial, handheld, whip pan, arc. Zoom changes focal length and "the camera itself doesn't move." Some advanced angles and lenses are "not officially supported" [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide
- Short clips: aim for "subtle evolution rather than dramatic change" [vendor] (same URL).
- Length: aim for one storyboardable change, not more text. Stacks of adjectives and do-everything action lists produce "wiggle" and drift [reported] https://www.imaginary.app/blog/image-to-video-that-actually-moves-not-just-wiggles-a-9-step-troubleshooting-che
- Write the action as start → end → hold ("one action only: X, then stop") so the model knows when to stop. The start image must show the start state, or the model oscillates between states [reported] (same URL).
- Don't combine a big subject motion with a big camera move: they compete [reported] (same URL).
- Avoid "handheld" and "shaky": they produce jitter. Use a locked tripod or one slow, stabilised dolly or slider [reported] (same URL).
- Omni Flash: one blog says to put camera direction at the end, in 3–8 words [reported, thin] https://framia.converge.ai/page/en-US/news/gemini-omni-flash-prompt-guide
- Omni Flash: write a director's shot brief, not keywords, and state the audio every time, because sound is generated in the same pass [reported] https://www.atlabs.ai/blog/ultimate-gemini-omni-flash-prompting-guide-2026
- Timestamps: Google's Veo 3.1 guide documents `[00:00-00:02] shot…` blocks for **multi-shot** sequences in one generation [vendor] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1. For a one-action clip from a still, timestamps add cuts and beats, which is the opposite of what's wanted. Untested on Omni Flash [inference].
- Negative phrasing: Veo says "describe what you don't want to see" as a plain list ("wall, frame"), and avoid "no" and "don't" [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide. The 3.1 guide prefers positive restatement: "a desolate landscape with no buildings or roads" over "no man-made structures" [vendor] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- Negatives are weaker than positives in general (researcher quoted) [reported] https://www.technologyreview.com/2025/07/15/1120156/googles-generative-video-model-veo-3-has-a-subtitles-problem/. Omni Flash has no negative-prompt field, so phrase constraints positively [reported] https://www.atlabs.ai/blog/ultimate-gemini-omni-flash-prompting-guide-2026
- Audio: "Clearly specify if you want audio" and put audio in sentences separate from the visuals [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide. Use the labels `SFX: …` and `Ambient noise: …` [vendor] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- No speech: there is no documented "no dialogue" switch. Name the soundtrack fully (SFX, ambience, music) and include no quoted line or speaker [inference]. Google Labs support said speech can trigger burnt-in subtitles, so silence also protects against text [reported] https://www.technologyreview.com/2025/07/15/1120156/googles-generative-video-model-veo-3-has-a-subtitles-problem/
- If a figure must "rap" in silence, the model may invent vocals to match the mouthing. A mask with no mouth reduces this. Untested [inference].

## 2. Identity, costume, small details; stopping morph, extras, teleporting, text

- Add short locks: "Background stays the same; no new objects appear", "Wardrobe unchanged", "Keep [X] consistent" [reported] https://www.imaginary.app/blog/image-to-video-that-actually-moves-not-just-wiggles-a-9-step-troubleshooting-che
- Localise the motion ("Primary motion: right hand. Torso and background remain static") to cut warping elsewhere [reported] (same URL).
- Morphing mostly comes from too much motion. Use one primary motion and at most one subtle secondary [reported] https://blog.segmind.com/veo-3-image-to-video-guide/
- Logos and emblems warp, hands distort and shapes morph "after about two seconds" in single-image animation generally [reported, thin, vendor blog] https://www.atlascloud.ai/blog/tips/gemini-omni-flash-1.1-image-to-video. Keep the emblem large, front-on and sharp in the still, and keep the mask's surface out of the motion (no head turns) [inference].
- Omni Flash consistency "can drift during large scene changes or fast camera moves". Use a reference image for important subjects [reported] https://www.atlabs.ai/blog/ultimate-gemini-omni-flash-prompting-guide-2026
- For reuse across clips, Google advises repeating the same verbatim character description and changing only the action [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice. This conflicts with the image-to-video "don't re-describe" rule. Resolve it by repeating only a short identity lock line, not the full look [inference].
- Ingredients/reference images exist to "maintain a consistent aesthetic across multiple shots" [vendor] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- In one 9-shot test, Omni Flash's recurring flaw was an "abrupt zoom or framing jump". Hands and object physics mostly held, with no morphing [tested, small sample] https://community.trypencil.com/public/blogs/we-put-gemini-omni-flash-to-the-test-2026-07-13. Write "locked-off camera, framing holds" to counter it [inference].
- Text: Veo adds garbled subtitles even when told not to, mostly when there's speech [reported] https://www.technologyreview.com/2025/07/15/1120156/googles-generative-video-model-veo-3-has-a-subtitles-problem/. Blogs report "no subtitles / on-screen text" lines helping only partly. The fallback is cropping the bottom 12–18% [reported, thin] https://www.veo3ai.io/blog/veo-3-remove-subtitles-captions-fix-2026
- In the dialogue format, a colon with no quotation marks keeps words from being rendered as on-screen text [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice. Irrelevant if there's no speech.
- Extra people: no source found with a tested fix beyond the "no new objects / background stays the same" lock. Frame the still with every figure already in it, and don't ask anyone to enter [inference].
- Teleporting vehicles: no source addresses it directly. Likely causes are a vehicle half out of frame in the still, plus a camera move with no stated direction. Fix: the vehicle starts fully in frame, travels one stated direction ("moves left to right across frame and exits frame right"), and the camera is locked or does a single pan following it [inference].

## 3. Hand-gesture performance with a covered face

- No verified source on beat-timed gesture prompting was found (**thin**). A Veo prompt page shows chained big gestures with hand tension [reported, thin] https://apidog.com/vi/blog/google-veo-3-prompt-theory
- In Omni Flash tests, finger snaps hit contact with audio in sync, and typing rhythm looked "natural and varied, not looped" [tested] https://community.trypencil.com/public/blogs/we-put-gemini-omni-flash-to-the-test-2026-07-13. This suggests rhythmic hand action is within reach.
- The same test saw hands "alternated between a loose fist and an open palm instead of snapping" on one shot [tested] (same URL). Keep the gesture vocabulary small: one repeated move.
- Describe the gesture as a physical cycle with a count, not a mood. Example: "his right hand chops down on each beat, four times, forearm stays level, left hand stays at his chest" [inference, built from the "one action, then stop" rule above].
- Tie motion to sound in a separate SFX/music sentence ("a steady boom-bap drum beat; each hand chop lands on the kick drum"). Veo documents sound synced to actions [vendor] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1. Beat-to-gesture sync is untested [inference].
- No face means the head and shoulders carry the rhythm: a nod on the beat, shoulders rolling, leaning into the lens on the last bar [inference].
- The mask can't "speak", so don't ask for mouthing. Ask for the body to deliver it ("rapping" may invent a mouth or vocals) [inference].

## 4. Physical-looking motion and effects

- Video models' physical understanding is "severely limited, and unrelated to visual realism" (DeepMind Physics-IQ, pre-Veo-3 models) [tested] https://vision.insait.ai/publications/do-generative-video-models-understand-physical-principles/. A 2026 survey still finds "a clear gap between visual fluency and physical consistency" [tested] https://arxiv.org/pdf/2510.04978
- Omni Flash handled viscous fluids (toothpaste, chocolate) convincingly, with cause and effect holding [tested, small sample] https://community.trypencil.com/public/blogs/we-put-gemini-omni-flash-to-the-test-2026-07-13. Water spray and smoke are probably safer than rigid objects in flight [inference].
- Describe the force and the response step by step (as with "dough flattens gradually, pin rotates") [tested] (same URL). For example: "the boat's bow lifts, a sheet of spray fans out behind and falls back to the water".
- Physics words like "flowing realistically" are suggested, and a sample negative list is: "motion blur, distortion, warping, face morphing, inconsistent lighting, background shifting, unnatural physics, floating objects" [reported] https://www.veed.io/learn/veo-3-1-guide
- Motion blur: "subtle motion blur" can be prompted. "180-degree shutter" is a general film concept with no documented Veo effect [reported] https://morphic.com/ai-glossary/motion-blur. Too little blur gives the hyper-sharp "video" look, too much smears [reported] (same URL). Use it for vehicle passes and muzzle flashes, and test it [inference].
- Muzzle flash: one short flash per shot, "a single burst of flame at the muzzle, brief, then smoke drifts". A stream of fire, flying shells or visible bullets invites invented physics [inference].
- Falling banknotes: many small objects in flight is the classic multiply/float failure. Describe a few notes, slow, flutter and settle, or keep them out of the action [inference; the "floating objects" item in the negative list above is reported].
- Vehicles: modern cars appear when the model fills in unseen traffic. Keep only the period vehicle in frame and name the period ("a 1920s Ford Model T hot rod") [inference]. No source found on period-car drift.
- Sparks: describe them as short-lived and falling with gravity ("sparks drop and die out") [inference].

## 5. Refusals

- Veo's filter categories with support codes are Child, Celebrity, Video safety, Dangerous content, Hate, Other, Prohibited, Third-party, Sexual, Toxic, Violence and Vulgar. There's no separate weapons category [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/responsible-ai-and-usage-guidelines
- Google's prohibited-use policy bans "violence or the incitement of violence". It allows exceptions for "educational, documentary, scientific, or artistic considerations" [vendor] https://policies.google.com/terms/generative-ai/use-policy
- Flow states it has precautions around minors and uploaded photos of people, and that "certain queries might not be generated" [vendor] https://support.google.com/flow/answer/16353333?hl=en
- Filters score the whole prompt in context, and screen the output frames as well as the prompt. A clean prompt can fail after generation [reported] https://freevisualtools.com/blog/sora-veo-content-violation-fix/
- Reported trigger words: gun, weapon, shoot/shot, fight, attack, blood, explode/blast, tied/bound/captured. Suggested swaps include "stylized prop", "dynamic action scene", "bright flash", "standing beside" [reported] (same URL).
- Practical phrasing for this film [inference]: "a 1920s drum-magazine submachine gun prop", "he fires into the air, a bright flash at the muzzle" (no target, no person hit), "the gang empties the vault" rather than "robbery at gunpoint". Keep guns pointed away from people.
- Child is the touchiest category. "Young", and naming family relationships, triggered code 17301594 on an adult-plus-child image [reported] https://freevisualtools.com/blog/sora-veo-content-violation-fix/. Keep crowd and bystander stills free of children [inference].
- Elderly people and crowds: no source found that names them as triggers (**no evidence**).
- Debug method: strip the prompt to its core and add parts back one at a time [reported] https://chasejarvis.com/blog/how-to-fix-veo-3s-sensitive-content-warning/

## 6. Clip length vs drift

- Veo 3.1 offers 4, 6 or 8 s clips [vendor] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- Omni Flash in Flow: one guide lists 4, 6 or 10 s [reported] https://quantrimang.com/google-flow-model-ai-tao-video-216971. Others give 3–10 s at up to 720p [reported] https://help.artlist.io/hc/en-us/articles/37099208586013-Gemini-Omni-Flash
- Morphing appears "after about two seconds" in single-image animation [reported, thin] https://www.atlascloud.ai/blog/tips/gemini-omni-flash-1.1-image-to-video. Kling guides say 3–5 s is that model's sweet spot [reported] https://fal.ai/learn/devs/kling-o1-prompt-guide
- For longer content, generate separate short clips and cut them together, rather than stacking beats in one clip [reported] https://www.imaginary.app/blog/image-to-video-that-actually-moves-not-just-wiggles-a-9-step-troubleshooting-che and https://www.atlabs.ai/blog/ultimate-gemini-omni-flash-prompting-guide-2026
- 6 s with one action that finishes by ~4 s and then holds gives the edit a clean out-point, and leaves less runway for drift [inference].


# Rules

- Read nothing on this computer apart from this brief and the images listed for your shots (open and look at each one). You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, artist or real person. No readable words.
- One motion prompt per shot, 40 to 90 words, plain sentences, describing only the motion (the still supplies the look). Write each shot differently: what this man in this place would do.

Write to `/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-balaclava/cleanroom/r4-clips/w2.md` exactly in this format and nothing else:

=== CLIP <id> ===
<motion prompt>
ENDS_ON: <what the last frame shows>
WHY: <one sentence>

Then reply with one line saying it is done.