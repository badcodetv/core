# Jack's own words (verbatim, 2026-10-28, in the order he said them)

1. "for the bank robbery music video, now it has come all together, can we try a different style ... so the stly i want is still that gangster prohabition era, using the all the stuff from that time, but with a realistic style that merges with a noir/james bond opening sequence/colour full of lights, vibrancy and an interesting dream like art stlye, paint spray sprayed, i cant quite describe tjhe style i am looking for, but i want it to be mostly a realistic style, but the lights and colours are exarggerated and cinematic"

2. "so come up with a style, kind of like the city in the mans jacket, but it is psychedelic, where it constantly transitions settings in clever ways, say they are burning coal on the fire in the basment, then it zooms into the fire and zooms out to something on fire during a protest or something. also please keep the realistic style, but have psychedelic stlyes overlayed if you know what i mean, please come up with a bunch of differnt types of psychedelic stlyes that massively vary from each other."

3. "i like all of them, so lets use each psychedlic styles that fit each scene, also i want more pretty colourful lights and refelections, keeping with the realisictic stlye, intresting david lynch camera angles, no ai slop. lets do a similar story, but with more gangster and bank robbery imagery, like tommy guns, bank vaults, car chases with poilice, more stuff from the prohabition era that was fun and interesting, action packed. the underground speakeasys, people playing pool, the bands in the underground clubs, pplaying poker, stuff like that ... with pschedelic transicaitions and overlays over a realistic style that looks cinematic and visually pleasing and eye grabbing."

4. On the opening scene, quoting back a line he approved: "Car chase opens the film. A tommy gun sticks out of the getaway car's window, pointed at the sky."

5. His note on the opening scene as it was made: "it looks like ai slop, the cars teleport and the pschedelic trails/affects look too basic and simple. the setting looks very much like ai slop."

6. "Please avoid elements of “AI slop” (research the internet on how to do that.) Please optimise this prompt for Nano Banana 2.1/Omni Flash on Google Flow and research the internet on how to do that."

# Facts about the job (not style advice)

- The film is a music video for a song called "Bank Robbery". This is its opening shot. The lyric over it is a single shouted word: "Robbery!"
- Google Flow refuses any image or video with a gun pointed at a person. Pointed at the sky is fine.
- No readable words anywhere in the picture.
- The person making it pastes your prompts into Flow exactly as written.
- This round makes the STILL only (16:9).

# The staging for your shot

2. **From up on the elevated railway, looking down.** A strange, high, tilted angle through the iron sleepers and girders of the El, down onto the street below, where the getaway car swings round a corner with the gun up at the sky (so pointing toward the camera's height, not at anyone) and the police car's lamp just entering frame. Psychedelic layer to build: sparks from a passing train's wheels raining down past the lens, glowing streaks of molten colour in the foreground.

# What came back when the first three clean-room still prompts ran (2026-10-29, Nano Banana 2.1, 2 takes each)

An honest description of the six images, written by the person who ran them. These are the failures to beat.

- **Every frame is the same night:** heavy rain, every surface wet and mirror-glossy, wet cobbles shining edge to edge, mist/fog glowing pink and teal. It reads as a stock "neon noir" wallpaper, not a place.
- **The neon is generic and fake-period:** cocktail-glass shapes, arrows, a target circle, letter-like squiggles ("J", "Z") in hot pink / cyan / green on every building. 1920s streets did not look like a 1980s Miami strip.
- **The streets are symmetrical theme-park sets:** a vanishing-point street centred in frame, identical buildings both sides, lamp posts evenly spaced, nothing that could only be one city.
- **The puddle idea:** the oil-film rainbow came out as a neat sticker of colour; the gangster ended up *standing on the car's running board* posing with the gun like a poster, the police car parked behind.
- **The windscreen idea:** the composition is the strongest (driver's gloved hands, dashboard, the target car ahead), but the street beyond is the same glossy neon set, and the gun is posed.
- **The running-board idea:** closest to real (dented black body, gloved arm, a police car behind), but the "marbled reflections" became a few rainbow smudges on the paint: the psychedelic layer is weak and basic, as Jack said last time.
- Overall: competent, glossy, over-lit, too clean and too centred. Colour comes from decoration, not from light doing something strange.

# Nano Banana 2.1 in Flow: film frames, not AI slop (clean-room web research)

2026-10-29. Web only; no repo files read. Tiers: **[official]** Google/DeepMind docs or help; **[practitioner, tested]** someone shows side-by-side outputs; **[opinion]** a guide's advice with no test, or my own inference (marked "inference").

## 0. What Nano Banana 2.1 is

- Google's API docs list **Nano Banana 2.1, `gemini-nano-banana-2.1`**, as "update to Nano Banana 2 and the primary high-efficiency model"; Nano Banana 2 (`gemini-3.1-flash-image`) is now "previous generation". Up to 14 references (10 object refs); 1K/2K/4K; thinking levels minimal/medium/high (default medium); Image Search grounding. [official] [ai.google.dev image-generation](https://ai.google.dev/gemini-api/docs/image-generation)
- Release: reported 6 Oct 2026, rolled into Gemini app, AI Studio and **Flow**; Nano Banana 2 reportedly retired 29 Oct 2026. [opinion: press, no Google blog post found] [technews.tw](https://technews.tw/2026/10/07/google-nano-banana-2-1/), [Artlist](https://artlist.io/blog/nano-banana-2-1-what-changed/), [TestingCatalog: Flow build pointed to "Nano Banana 2.1", 27 Sep](https://www.testingcatalog.com/new-google-flow-build-now-points-to-nano-banana-2-1.md)
- What changed vs 2: better instruction following (counts right), **fewer unrequested extras** (2 invented a logo on a flag and a label on a tin; 2.1 left them plain), photorealism a tie, old prompts work unchanged. **If you relied on 2 inventing detail to fill space, 2.1 needs you to state it.** [practitioner, tested: 8 prompts, one run each] [GoEnhance](https://www.goenhance.ai/blog/nano-banana-2-1-vs-nano-banana-2)
- Inference [opinion]: 2.1 rewards a *specific* prompt more and fills a vague one with less, so "generic sets with nothing specific" is now mostly a prompt-content problem.
- Flow's help page names **Nano Banana Pro as the default** image model in the prompt box: check the model picker every time. [official] [Flow help](https://support.google.com/flow/answer/16894016?hl=en)

## 1. The slop tells, and the counter for each

The commonly cited list: waxy skin, symmetrical faces/compositions, over-smooth detail, teal-and-orange grade, HDR halos, generic creamy bokeh, perfect lighting on everyone, over-saturation, "too clean". [opinion] ([MagicShot 12 tells](https://magicshot.ai/blog/why-your-ai-images-still-look-fake-12-tells-and-how-to-kill-them), [dev.to, 200 prompts](https://dev.to/pretty_lilac/i-studied-200-ai-image-prompts-to-figure-out-why-most-ai-photos-look-fake-heres-what-actually-245g))

| Tell | Counter |
|---|---|
| Centred symmetry, "average" framing | Vagueness defaults to centred, flat, posed; name the camera position, distance and where the subject sits in frame. [opinion; anecdotal before/after in dev.to] |
| Everything wet and mirror-glossy | Models turn wet ground into a "mirror-smooth reflection plane"; ask for *pitted* surfaces, shallow oily puddles, debris, damp brick. Or simply describe dry ground: wetness is a genre default, not required. [opinion] [budgetpixel](https://budgetpixel.com/blog/analog-neon-prompting-1990s-cyberpunk-street-photography) |
| HDR even fill, lit-from-everywhere | Name **one** motivated hard source (a sign, a window, a lamp) plus "no ambient fill / deep blacks"; one light, consistent shadows. [opinion] same + MagicShot |
| Plastic skin, AI sheen | Pores, stray hair, wrinkles; lower saturation; grain. [opinion] |
| Too clean / theme park | Describe the *cause* of wear (coal soot, water damage, foot traffic), not "dirty". See §3. [opinion] |
| Quality buzzwords | "8K, masterpiece, hyper-realistic, cinematic" push toward glossy CGI; remove them. [opinion, several guides agree] [dropshot](https://aistudio.dropshot.io/en/blog/realistic-ai-image-prompts-free) |
| Teal-orange grade | Google's own guide *offers* "cinematic color grading with muted teal tones" as an example, which is how it became the default; name a specific palette instead. [official example; the counter is opinion] [Google Cloud guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) |
| Unasked additions (moon, sign, logo) | 2.1 adds fewer; state the sky/background positively ("overcast, starless, sodium-lit haze"). [tested + official positive framing] |

## 2. How Nano Banana 2 / 2.1 wants to be prompted

- **Narrative, not keyword lists.** "A narrative, descriptive paragraph will almost always produce a better, more coherent image than a simple list of disconnected words." [official] [Google Developers Blog](https://developers.googleblog.com/en/how-to-prompt-gemini-2-5-flash-image-generation-for-the-best-results/); "A simple list of keywords won't cut it." [official] Google Cloud guide.
- **Formula:** Subject + Action + Location/context + Composition + Style; photoreal template "A photorealistic [shot type] of [subject] in [setting]… lit by… Shot from [angle] with [lens]." [official] Cloud guide; [API docs](https://ai.google.dev/gemini-api/docs/image-generation).
- **Length:** no official limit; Google's examples are 3–6 sentences. Specificity beats length. [official examples; opinion on sweet spot] [dev.to](https://dev.to/pretty_lilac/i-studied-200-ai-image-prompts-to-figure-out-why-most-ai-photos-look-fake-heres-what-actually-245g)
- **Materiality:** "Don't just ask for a suit jacket; ask for 'navy blue tweed'." [official] Cloud guide.
- **Camera/lens/film language:** Google endorses it (angle, f/1.8, "low angle", camera body, "1980s color film, slightly grainy"). [official] Practitioners say it switches the model into "photography mode". [opinion] **No source tests whether stock-name stacking ("Portra 400, 35mm") now reads as a fake-film look**; inference [opinion]: use lens/angle/light as *instructions* with a reason, and treat film-stock names as one optional seasoning, not a preamble.
- **Negatives:** "Use positive framing… 'empty street' instead of 'no cars'." [official] Cloud guide + Vertex docs. No negative-prompt field exists in the API. [opinion: third party] Naming the unwanted thing puts it in the prompt.
- **Aspect ratio:** set it in Flow's control; also writable in text ("A cinematic 21:9 wide shot"). 1:1 to 21:9 supported; 2/2.1 add 4:1/8:1. [official] [Google blog, 7 tips](https://blog.google/products/gemini/prompting-tips-nano-banana-pro/)
- **References:** give each image a job: "Use Image A for the pose, Image B for the style, Image C for the environment." [official] 7 tips.
- **Text:** put wanted text in quotes with a font description; small text at 1K blurs. [official] To *avoid* text, say signs are "weathered, illegible" or keep them out of frame. [opinion]
- **"Photograph" → borders.** No source documents it. Inference [opinion]: "photograph" / "vintage photo" invokes the photo-as-object (print, border, Polaroid). Say "a frame from a 35mm feature film, full-bleed" or describe the shot without the noun.

## 3. Period-specific, lived-in 1920s

- Build the scene from **who lives there**: what they burn for heat, where they walk daily. [opinion] [Hailuo period-grime guide](https://hailuoai.video/knowledge/prompting-period-grime-weathering-guide)
- Prompt the **event that caused the wear**: "water-damaged joints" over "dirty wall"; layer structural (cracks, sagging), patina (rust, verdigris), recent human (handprints, tracked mud, fresh soot). [opinion] same.
- Name the **fuel**: coal soot is matte, crusted on windward brick; oil-lamp/tallow soot is greasy on ceilings. [opinion] same.
- Model-maker words ("pin wash", "dry brushing", "salt chipping") avoid texture-pack grime. [opinion] same.
- Anachronisms are common from simple prompts (Malmö University study). [practitioner/academic] [mau.se](https://mau.se/en/news/AI-produces-stereotypical-and-anachronistic-images-when-portraying-the-past/) Name the exact year and real objects of it.
- "1920s glamour" tools give the costume-party look; ask for ordinary, worn, mismatched clothes. [opinion]
- Inference [opinion]: with 2.1 inventing less, list 3–5 specific period props per set (a named make of car, the exact signage trade, a sawdust floor, a cigar-burned felt) rather than "1920s speakeasy".

## 4. Stylised/psychedelic colour that still reads as photographed

No source tests in-camera-effect prompts on Nano Banana. What exists:
- Glow as **optics**, not overlay: "subtle optical halation around bulbs", "vintage lens halation" reads as lens/film rather than a glow layer. [opinion] [budgetpixel](https://budgetpixel.com/blog/analog-neon-prompting-1990s-cyberpunk-street-photography)
- Colour from **sources in the scene**: neon signs as "the only hard light sources" with falloff, not "neon lighting". [opinion] same.
- Real techniques worth naming (physics the model can imitate): prism in front of the lens (doubled/ghosted edges, strongest on textured backgrounds) [practitioner] [DIYPhotography](https://www.diyphotography.net/prism-lens-photography-light-effects/); Vaseline smeared on a filter leaving a clear centre [practitioner] [Digital Camera World](https://digitalcameraworld.com/tutorials/camera-hacks-get-creative-blur-abstract-shots-and-soft-focus-effects-using-vaseline); in-camera double exposure (dark base, second frame fills shadows) [practitioner] [Wikipedia: freelensing](https://en.wikipedia.org/wiki/Freelensing), light leaks from freelensing; oil-and-dye "liquid light" projection onto set walls [practitioner] [Film-Tech](https://www.film-tech.com/ubb/f8/t003742.html).
- Inference [opinion]: the "flat ribbons pasted on top" come from asking for an *effect* ("psychedelic trails"). Ask instead for the *apparatus and where its light lands*: "a magenta gel on the lamp behind the bar, its spill catching cigarette smoke", "projected oil-and-dye swirls crawling over the faces and the wallpaper". Colour that has a surface to land on reads as photographed.

## 5. Inside Google Flow, for stills that will be animated

- Pick the model explicitly (Pro is the default). [official] [Flow help](https://support.google.com/flow/answer/16894016?hl=en)
- Ingredient references: plain/segmented background; location/style references free of extra subjects; consistent look across all ingredients; text prompt must "complement, not contradict" the inputs; `@name` for characters. [official] same.
- Frames: start/end frame plus a prompt describing the action between them. [official] same.
- Approve the still before spending on video; flaws in faces/hands get **intensified** in image-to-video; photoreal start frames give photoreal video; match aspect ratio to the output. [opinion, quoting Runway docs] [AI Film Contests](https://aifilmcontests.com/guide/first-frame-for-image-to-video)
- Inference [opinion] for the "cars teleport" note: a still that is ambiguous about direction (car centred, no road ahead, no motion cues) leaves the video model to guess. Compose start frames with readable direction of travel and space to move into; for a chase, use start + end frames so the move between them is defined.

## 6. Patterns shown working (not for this film)

1. **Photographer's paragraph**: shot type + subject + setting + single named light with direction + angle + lens, in prose. [official template] [API docs](https://ai.google.dev/gemini-api/docs/image-generation)
2. **Specific beats long**: "man in leather jacket, moody lighting" → "harsh overhead fluorescent, sharp shadows under the eyes, blurred industrial background"; the gain came from specificity. [practitioner, anecdotal before/after] [dev.to](https://dev.to/pretty_lilac/i-studied-200-ai-image-prompts-to-figure-out-why-most-ai-photos-look-fake-heres-what-actually-245g)
3. **Cause-of-wear shot**: "Wide shot of an 1880s London alley, heavy matte coal soot on red brick, damp cobbles with oily puddles…" [opinion, examples only] [Hailuo](https://hailuoai.video/knowledge/prompting-period-grime-weathering-guide)
4. **Role-assigned references**: "Use Image A for pose, B for style, C for environment." [official] [Google blog](https://blog.google/products/gemini/prompting-tips-nano-banana-pro/)
5. **Only-source lighting**: signs as the only hard light + no ambient fill + halation around bulbs + pitted wet ground. [opinion] [budgetpixel](https://budgetpixel.com/blog/analog-neon-prompting-1990s-cyberpunk-street-photography)

**Gaps:** no controlled test of film-stock language as a cliché, no test of in-camera psychedelic effects on Nano Banana, no Google blog post for 2.1 found. Testing these in Flow is the next step.

# Your task

Write ONE still-image prompt for Google Flow's Nano Banana 2.1 (16:9) for the staging you were given. Stills only this round; the video comes later from the picked still.

Rules of the job:
- Use the web research in this brief as your guide; you may also search the web yourself. Do not read any file on this computer apart from this brief.
- Beat every failure listed in "what came back in round 1". The director called the last batch "AI slop": glossy, over-lit, symmetrical, generic, with basic effects.
- Mostly realistic, specific, lived-in 1920s America; the light and colour exaggerated and strange; an odd, interesting angle. The psychedelic layer must come from something physically in or in front of the camera, and must be rich, not a few smudges.
- The gun points only at the sky. No readable words anywhere. Describe what you want rather than listing bans (the research says why), though a short closing line about no text is fine.
- Narrative prose, roughly 120–220 words. No quality buzzwords.

Output exactly this and nothing else:

=== STILL PROMPT (Nano Banana 2.1, 16:9) ===
<the prompt>
=== WHY (two sentences) ===
<why>
