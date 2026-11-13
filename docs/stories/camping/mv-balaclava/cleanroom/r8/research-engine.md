# Research: AI video rap-performance gestures (web, 2026-11-07)

Clean-room web research only (no repo notes read). The question: how to get Google Flow (Omni Flash / Veo 3.1) and similar image-to-video models to animate a person rapping to camera with real music-video gestures, not stiff, looping "AI slop".

Tiers: **[vendor]** official docs from the model maker · **[tested]** someone reports trying it, with results · **[reported]** a blog or forum claim with no test shown · **[inference]** my own reasoning.

**Overall: the evidence is thin.** I found no controlled test of rap-performance motion in any model. Almost all the specific advice comes from vendor-adjacent SEO blogs (atlabs, veo3gen/imaginary, invideo, higgsfield) that show templates, not results. The firmest sources are Google's and Runway's own docs, plus Kling's guide. I found no Reddit thread on rap gestures; the searches returned only mirror snapshots.

---

## 1. What makes performer motion look fake, and the reported fixes

| Symptom | Source / tier | Reported fix |
|---|---|---|
| Stiff, repetitive small motions; the figure "stands too still" | detection guides, e.g. [veed](https://www.veed.io/learn/how-to-tell-if-video-is-ai-generated) [reported] | — |
| The same generic movement in every clip (a loop across takes) | [invideo FAQ](https://invideo.io/faq/how-do-you-stop-the-same-motion-loop-from-repeating-in/) [reported] | Cause given: identical prompts and an unspecified action make the model fall back on "the same generic movement every time". Fix: give "a different specific action at every beat", vary the framing (close, mid, wide), write a movement note per shot (weight, hand position, gaze), generate about 5 takes and pick one |
| Stiffness from "describing a mood instead of filmable action" | [veo3gen shot-first](https://www.veo3gen.app/blog/veo-31-shot-first-prompting-a-10-minute-method-to-fix-stiff-motion-random-moves-) [reported] | Write physical verbs; change one variable per re-roll |
| No weight; gliding; no "small corrective movements" | [atlabs stiff-motion](https://www.atlabs.ai/blog/how-to-fix-stiff-character-movement-in-ai-videos-(step-by-step)) [reported] | Prompt "weight shift, follow through, and secondary motion"; example wording "shoulders relaxed, hands gesturing on the downbeats" |
| Long takes "drift back into stiffness" | atlabs (above) [reported] | Keep clips short, cut and regenerate |
| Quality and motion fall off near the end of a clip (freeze, melt, drift) | [cliprise failure fixes](https://www.cliprise.app/learn/guides/best-practices/ai-image-to-video-failure-fixes) [reported] | Trim the end; "a 3-second clip will almost always be more stable than a 10-second clip". Write the action as start → action → end state, so the model has somewhere to go |
| Morphing hands, mic fused into fingers, hands flickering | [higgsfield hands/faces](https://higgsfield.ai/blog/ai-video-hands-faces), detection guides [reported] | Keep gestures below the chin, don't let hands cover the face, avoid hand close-ups. Fallback: hands out of frame, carry emphasis with head nods ([eastondev Veo tips](https://eastondev.com/blog/en/posts/ai/20251207-veo3-video-quality-tips/) [reported]) |
| Over-acting: image-to-video models "over-act" rather than move subtly | Reddit mirror snapshot [reported] | Pin the motion with an end frame, or use motion transfer from a reference clip |
| "Wiggle": the subject barely moves | [imaginary 9-step](https://www.imaginary.app/blog/image-to-video-that-actually-moves-not-just-wiggles-a-9-step-troubleshooting-che) [reported] | High-commitment verbs (lift, turn, point, drop), not "subtly move" or "gently animate"; one primary motion; leave open space in the frame in the direction of the motion |

**Not found:** any source naming "hands hovering at chest height", "symmetric frontal framing" or "presenter gestures" as a documented tell. They are plausible, but **unsourced**. [inference] The "presenter" look probably comes from the model's training mass of talking-head and explainer footage: a frontal, centred, mid-shot plus "talking to camera" pulls toward that register. Avoid wording that summons it ("speaks to camera", "explains", "presents").

**The strongest fix people report for body performance is not prompting but motion transfer:** copy a real performance from a reference clip. atlabs: "copying a real performance beats describing one every time" [reported]. Kling Motion Control maps a reference video's performance onto a character in an image ([Kling guide](https://kling.ai/blog/kling-ai-motion-prompts-guide), [imagine.art](https://www.imagine.art/blogs/kling-motion-control-prompt-guide)) [vendor]. Google's own Omni examples include applying the pose and motion from a reference video to a character in an image (per [blog.google Omni](https://blog.google/intl/en-ie/products/gemini-omni/) and the secondary summaries) [vendor, via secondary]. In Flow, Omni Flash supports video-to-video ([Flow models page](https://support.google.com/flow/answer/16352836)) [vendor]. [inference] Filming 8 s of someone (anyone) rapping with real hands and feeding it as the motion reference is the highest-leverage option. Test it before relying on it.

## 2. How the first frame constrains the motion

- **Runway's official image-to-video guide** [vendor]: input images carry implied motion (motion blur, mid-action poses, directional lines), and a prompt that contradicts those cues takes more iterations. Their example: a "parked, motionless" car kept moving until the dust and blur were removed from the image. Source: [Runway help, Image to Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide). The page returned 403 to my fetch, so this is quoted from its search excerpt.
  - So the reverse should hold [inference, well supported by that example]: **a still caught mid-gesture, with motion blur on a hand, primes motion.** A clean, symmetric, hands-down still primes stillness.
- **Kling's tutorial** [vendor]: a source pose mid-motion (arm extended, leg lifted) "gives the animation step more to work with than a straight standing pose" ([Kling dance generator](https://kling.ai/topics/ai-dance-generator)). A third-party Kling 4.0 page: choose a first frame that "already implies motion" ([segmind](https://www.segmind.com/models/kling-4-image-to-video)) [reported].
- **Prompt and start frame must agree** [reported, imaginary]: if a mug is already at the lips, "lifts the mug" conflicts. Don't crop tight on hands or joints if you want gestures; leave open space in the direction of motion.
- **atlabs** [reported]: "avoid still first defaults when the shot needs real action."
- **Flow help** [vendor]: the "text prompt should complement, not contradict, your visual inputs", and should refer to the frames ([Create videos in Flow](https://support.google.com/flow/answer/16353334?hl=en)).
- **Off-centre, low or dutch angle, props:** no direct evidence found. [inference] A low-angle wide with slight fisheye is the genre's own grammar. A rap guide recommends "Low-angle, wide-angle lens shot of the rapper performing dynamically… slight fisheye" ([beatstorapon](https://beatstorapon.com/blog/the-new-frontier-rap-hip-hop-video-creation-with-google-veo-3/)) [reported, untested]. A prop (mic, chain, a hand on a cap brim) gives the hands a job and a contact point, which Kling's guide says keeps precise tasks readable [vendor, not rap-specific].
- **End frame:** first+last frames pin where a gesture lands, and curb over-acting [reported]. If the two frames disagree on camera position, the model invents a move to reconcile them [reported].

## 3. Prompt wording for rhythmic body performance

**What works (reported):**
- **Gesture anatomy** [vendor, Kling]: name the hand path, facial expression, timing, body orientation, and *who receives the gesture*; give speed and weight ("slow, deliberate" vs "frantic, rapid"). Break actions into "preparation, main action, and follow-through". Add secondary motion (cloth, chain swinging, hood). Pair the gesture with the facial expression and delivery so the two stay linked.
- **Distinct actions per segment** [vendor, Google]: Veo 3.1 supports timestamp prompting, `[00:00-00:02] … [00:02-00:04] …`, to direct sequenced action inside one 8 s clip ([Google Cloud Veo 3.1 guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)). Google's example uses it for shot changes; nobody I found reports it working for gesture-by-gesture choreography [thin].
- **Concrete subtle actions are named in Google's vocabulary** [vendor]: "a subtle nod, fingers tapping impatiently" ([Vertex prompt guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)).
- **One shot type + one camera move** [reported]: "Combine one shot type with one motion command". More than two camera instructions makes the model "split the difference" ([roo Omni guide](https://roo.beehiiv.com/p/google-omni-prompting-guide-every-technique-that-actually-works)). One primary motion, at most one subtle secondary (imaginary).
- **Too many actions = jumbled** [reported]: "Veo 3 gets confused with too many actions" ([veotutorials](https://veotutorials.substack.com/p/7-ways-to-get-better-results-with)). [inference] With 8–10 s, about 3–4 distinct gestures is the ceiling. Write them as a sequence with a beat each, not a list of adjectives.
- **Adjectives don't add motion:** when a clip freezes, "adding more adjectives usually makes it worse" (veo3gen) [reported].
- **Handheld:** imaginary advises "avoid 'handheld' if you're fighting wiggle" [reported]. [inference] In a performance shot, handheld camera shake can stand in for body energy the model didn't generate. If you use it, make the subject's motion the primary one, not the camera's.

**BPM / tempo:** no evidence that a typed BPM is followed by Veo, Omni or Kling. Seedance 2.0 locks motion to the beat only via an uploaded audio track; one guide says rhythm "doesn't survive translation to text" ([opus.pro](https://www.opus.pro/blog/sync-video-to-music-beats-seedance), [onemoreshot](https://www.onemoreshot.ai/blog/seedance-2-0-music-videos)) [reported]. Practical use of the BPM: plan cut points in the edit (at 88 BPM one beat = 0.68 s) [inference]. Omni Flash reportedly accepts audio input ([invideo Omni guide](https://invideo.io/blog/gemini-omni-flash-guide/)) [reported]; whether feeding the track drives on-beat body motion in Flow is **untested — worth one trial**.

**Example rap prompts found** (none come with shown results):
- K-hip-hop template: "stands center-frame with confident swagger, rhythmic head nods, and expressive hand gestures synced tightly to fast Korean rap flow" ([youmind](https://youmind.com/video-prompts/219)) [reported]. Note "center-frame" is the frontal default.
- Rap-duo template: "Dynamic camera movement, realistic facial expressions, natural body movement… energetic hip-hop music video style" ([viddo](https://viddo.ai/blog/rap-duo-video)) [reported]. Generic adjectives, which is the opposite of the specific-verb advice above.
- beatstorapon: "energetic hand gestures", "intense eye contact with camera", low-angle wide plus slight fisheye [reported]. It warns that "fast rap flows may not always align perfectly" in lip sync.

## 4. Google Flow / Veo / Omni Flash specifics

- **Models and frames** [vendor, [Flow models page](https://support.google.com/flow/answer/16352836)]: Omni Flash 1.2 does Frames to video (web), Ingredients, video-to-video and Extend (paid), 3–15 s. Omni Flash 1.1 and Veo 3.1 Fast/Quality retire 2026-12-05; Veo Extend was retired 2026-11-05.
- **Frames prompt = what changes** [vendor + reported]: Flow help says to describe "the action or transition that should happen between the frames". Community guides say not to re-describe the frame, because it creates competing instructions.
- **Omni official tips** (Google AI post, via [pasqualepillitteri](https://pasqualepillitteri.it/en/news/3513/mastering-gemini-omni-flash-video-prompting-guide)) [vendor, secondhand]: lean on real-world knowledge (cultural references, eras) instead of minute description; name the shot type, move and camera style ("one continuous shot", "push in"); edit iteratively and keep what works; change a character's pace or emotion with a direct instruction. [inference] "Real-world knowledge" suggests naming a recognisable performance register (a UK grime video, a "Fire in the Booth" session, 90s East Coast fisheye) may carry more motion vocabulary than describing gestures one by one. Untested.
- **Length:** the Omni conciseness rule is reported as "a focused sentence of about twenty words beats a generic paragraph" (attributed to the official guide, secondhand) [reported]. Google's Veo examples run 2–3 sentences [vendor]. They conflict with one blogger's "be as detailed as possible" ([Dinsmore, $400 of Veo 3 tests](https://alejandrodinsmore.substack.com/p/deep-dive-veo-3-i-spent-400-testing)) [reported; his tests are anecdotal]. Net: short and verb-dense beats long and descriptive.
- **Without motion cues, Omni defaults to a mostly static shot** (pasqualepillitteri) [reported].
- **Pacing edits:** Omni accepts conversational edits such as "Slow the motion of all elements by 40 percent"; make one change per turn (roo) [reported, untested].
- **Negatives:** Google says to describe the wanted state, not "no X"; list unwanted items as nouns rather than instructions [vendor].
- **Randomness:** the same prompt gives "terrible" then "perfect" results on retry (Dinsmore) [reported]. Budget several takes per shot.
- **Lip sync for rap:** Seedance 2.0 beat Kling 3.0 and Veo 3.1 on live-action lip sync in one comparison ([Curious Refuge](https://curiousrefuge.com/blog/ai-lip-sync-workflows)) [tested, single comparison]. A common workflow: body motion first, lip sync as a separate pass after (atlabs) [reported].

## Where the evidence is thin
- No tested source on rap or performer gestures in Veo/Omni specifically.
- Nothing found on chest-height hovering hands or symmetric framing as named failure modes.
- BPM in text: no evidence it works in any model; audio input works in Seedance (vendor claims); untested in Omni.
- Timestamp prompting for gesture sequences: documented for shots, not for choreography.
- The first-frame motion-cue effect has vendor backing (Runway, Kling) but no published A/B.
