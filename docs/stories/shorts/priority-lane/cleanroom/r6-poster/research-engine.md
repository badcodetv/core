# Engine research: poster still + poster-to-car transition (web, 2026-11-14)

Tiers: **A** = official docs or tested by many; **B** = several practitioners agree; **C** = one source or an anecdote. Most of what is out there is vendor blogs; nothing official covers our exact shot.

## 1. Short headline on a poster in a photo-real scene

- Google's own guide: put the exact words **in quotes** and **describe the typeface** ("bold, white, sans-serif"). Text comes out best if you settle the wording first, then ask for the image. **A** ([Google Cloud guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana))
- Quoted text is set as written, capitals and punctuation included; anything unquoted gets reworded. One quoted string per line, in reading order. Give each line a position and a *relative* size ("large headline across the bottom third") rather than point sizes. Name the type class ("heavy condensed sans serif"). **B** ([Runware text guide](https://runware.ai/docs/models/google-nano-banana-2-1/guides/text-and-layouts.md), [Morphed](https://morphed.app/blog/nano-banana-prompts-for-posters))
- Keep it to 1-4 words. Claimed accuracy figures disagree badly (~95% for 1-4 words vs ~64% overall), so plan for a few rolls. **C** ([Morphed](https://morphed.app/blog/nano-banana-2-prompts), [eWeek](https://www.eweek.com/news/google-nano-banana-2-cheat-sheet/))
- In a photograph, say the poster is **in sharp focus** (shallow depth of field, poster sharp). Text that is small, far away or at an angle is where it breaks. **B** (Runware above)
- Ways it fails: one letter wrong (the commonest, and it ruins the file); extra text you didn't ask for (small print, a web address). Say "no other text" if you want none. **B**
- Fixing it: if only the slogan is wrong, a targeted edit ("change 'X' to 'Y'") is the vendor advice. But our standing rule is a new prompt every time, never an edit, so the fallback is to re-roll, or set the slogan in Premiere over a blank poster. **B**

## 2. Keeping the man's identity on a printed poster

- Google's recipe is: reference image(s) + how they relate + the new scene, e.g. "Use the man in the attached image as the photograph printed on the poster…". Up to 14 references allowed. **A** (Google guide)
- **Don't describe his face.** The reference carries who he is; spend the words on what changes. Open with "the same man from the reference image". Name only the details that must survive (e.g. "same dark coat, same phone to his right ear"). **B** ([Runware consistency](https://runware.ai/docs/models/google-nano-banana-2/guides/character-consistency.md), [Framia](https://framia.converge.ai/page/en-US/blog/nano-banana-2-character-consistency)). Matches our house rule.
- Use **one sharp, uncluttered reference**. A dark, noisy night-car frame passes his identity on less well than a clean portrait. Consider making a clean, evenly lit headshot of him first and referencing that as well. **B**
- Ways it drifts: each request is a fresh interpretation; anything missing from the reference gets guessed; a chain of edits ("edit the edit") wears the likeness down. Always go back to the original reference. **B** ([UD.hk](https://www.ud.hk/en-US/resources/ai/2026-06-29-nano-banana-consistent-characters), [Recapio](https://recapio.com/digest/how-to-create-consistent-characters-with-nano-banana-ai-tools-increase-character-consistency-by-more))
- Restyling keeps the identity (watercolour, 3D), so a "printed, halftone, glossy campaign portrait" treatment should too. **C** (Runware)

## 3. Making it read as a PRINT behind glass

- No tested recipe exists for "rain + glass + lightbox". What turns up is mockup prompts: "street-level photograph of a glass bus shelter with an illuminated advertising poster", "large-format backlit poster, clean framing, natural reflections". **C** ([Krea example](https://www.krea.ai/feed/an-illuminated-bus-shelter-stands-on-a-dark-city-street-at-8effbf99-bb5b-5100-83ac-6c44af0547dd), [Adobe Stock desc.](https://stock.adobe.com/images/clean-and-minimalist-mock-up-of-a-blank-bus-shelter-in-an-urban-area-generative-by-ai/986430017))
- Our inference (**unverified**): name the *object* before the person ("a backlit poster in the shelter's advertising case **showing** a campaign photo of the man…"), and add the physical evidence that it is flat: aluminium frame, even glow from behind, the street's reflections on the glass in front, raindrops on the glass, print grain or halftone up close. Describing a person first risks him standing in the shelter.

## 4. Frames mode: poster to the man in the car

- Flow's start + end frame control for Omni 1.1 Flash shipped 27 Aug 2026. Google advises testing a frame pair cheaply before rendering it properly. **A** ([Google blog](https://blog.google/innovation-and-ai/models-and-research/google-labs/new-creative-controls-google-flow/)). (Our own rule is no 360p drafts; that rule wins.)
- **Match the two frames:** same aspect ratio, same camera logic, lighting from the same direction, subject in the same place and size. The more that differs, the worse the warping. So the poster close-up should crop the poster photo to the **same framing and pose** as the car still: same head size, same eye line, same hand and phone. **B** ([Magic Hour](https://magichour.ai/blog/first-frame-last-frame-ai-video), [Flick](https://flick.art/tools/first-and-last-frame), [Easy AI](https://easyaigenerated-web.vercel.app/help/video-tools/image-to-video-first-last-frame))
- **Prompt only the change**, one action, one camera move: "[subject] [single action]. The camera [one move]. The shot ends on the supplied closing frame." Re-describing what the frames already show gives the model rival instructions. **B** (Magic Hour, [skills.sh Flow guide](https://skills.sh/krishamaze/skills/google-flow-prompting))
- Morph transitions (logo A to logo B, real person to cartoon) are a known use, but testers report mixed results. Budget for several rolls. **B** ([DataCamp](https://www.datacamp.com/tutorial/veo-3-1-complete-guide-with-examples))
- Ways it fails: (a) a lazy **cross-fade**; one Veo 3.1 tester found adding "no crossfade" helped (**C**, [Atlabs](https://www.atlabs.ai/blog/the-ultimate-prompting-guide-for-veo-3-1)); (b) a **snap**, where it jumps to the end frame too early (**B**); (c) the **face changes in the middle** even when both ends match, so scrub the middle frames (**B**, Magic Hour).
- Fallback if the morph won't come clean (our inference, **unverified**): do it in Premiere. Push in on the poster still, then cut on the matched pose, or give it a short dissolve. A matched pose makes even a plain cut read as the same man.

## 5. Policy: political posters, slogans, "NHS"

- No public Google rule bans election-style imagery in Nano Banana. Brennan Center (22 Oct 2026) found Gemini/Nano Banana 2.1 made realistic election images and refused nothing. NewsGuard found Nano Banana Pro made images of real politicians. **B** ([Brennan](https://brennancenter.org/our-work/analysis-opinion/major-ai-models-are-more-willing-ever-create-fake-election-images), [NewsGuard](https://www.newsguardtech.com/?p=32058))
- Google's Prohibited Use Policy bans content *designed to deceive* about democratic processes, and deepfakes of real people. An invented man in a satire is outside both, but a real party logo or a real politician's face is where blocks or risk begin. **A** ([policy](https://policies.google.cn/terms/generative-ai/use-policy?hl=en))
- A claim that Nano Banana 2 made "public figures" a formal blocked category is unconfirmed. **C** ([laozhang blog](https://blog.laozhang.ai/en/posts/gemini-image-generation-people-restriction))
- I found **nothing** on "NHS" as a trigger word. Not known; test it.
