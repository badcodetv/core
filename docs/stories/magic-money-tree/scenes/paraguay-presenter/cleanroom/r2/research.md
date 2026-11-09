# Clean-room research r2: masked TV presenters in Nano Banana 2 (2026-11-09)

Web research only (no repo files read). Tags: **[official]** Google's own docs/blogs; **[tested]** someone reports doing it; **[opinion]** a guide's claim or my inference. Notes, not prompts.

## 1. Taking ONE element from a reference and leaving the rest

**What Google says**
- The reference formula is **[Reference images] + [Relationship instruction] + [New scenario]**: say what each reference *contributes* ("the sketch as the structure, the fabric sample as the texture"), then describe the new scene. Start with a strong verb for the main operation. [official] Google Cloud, "The ultimate Nano Banana prompting guide", 2026-03-06 — https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- Give each reference a role: "Use Image A for the character's pose, Image B for the art style…". Patterns, logos and artwork can be applied to objects "while preserving natural lighting and texture". The post lists no way to *exclude* things, so whatever has no role is implicitly meant to be left out. [official] blog.google, "7 tips… Nano Banana Pro", 2025-11-20 — https://blog.google/products/gemini/prompting-tips-nano-banana-pro/
- The high-fidelity template: "Using the provided images, place [element from image 2] onto [element from image 1]", and **describe the critical detail (face or logo) in words as well**. [official] AI Studio image-generation docs (undated, read 2026-11-09) — https://aistudio.google.com/docs/image-generation
- The same docs list **Nano Banana 2.1** (`gemini-nano-banana-2.1`) and split reference slots into *object* images (up to 10) and *character* images (up to 4). A logo-layout strip is an object/design reference, not a character. [official] same URL
- "Semantic negative prompts": describe what you want, not what you don't ("empty street", not "no cars"). Use camera language for composition. For complex scenes, build in steps. Give context and intent. [official] same URL; also the Cloud guide

**Applying this to our case** [opinion unless marked]
- Give the reference ONE job in one short sentence near the start, naming only the design: thin cream ring tracing the face edge, small flat red triangle inside it, high on the picture's right. Then restate the layout in plain words, because the docs say critical details should be described as well as attached [official]. A role sentence plus a description is about 30–45 words. Keep the rest of the prompt about the new man.
- Then give positive, specific values for everything the reference would otherwise supply: hood colour and material, clothes, background, light, crop. Each of those slots left empty is a slot the model fills from the reference. That is the usual cause of "it just copied the reference". [opinion; the Kaiber/Flick-style guides say name what to keep and describe only what changes or is missing — https://www.kdnuggets.com/nano-banana-practical-prompting-usage-guide, https://flick.art/docs/nano-banana-prompts]
- A strip of several heads can leak its *form* into the output: a grid, a row of heads, a tight crop, a flat backdrop. Say "a single man" and give a full scene and crop to push against that. [opinion]
- Copying shows up as the reference's hood colour, the same knit, the same head angle, or a plain backdrop. The cheapest fix is to name a material that sounds clearly different from the reference (e.g. sharkskin, velvet, quilted nylon, wet-look vinyl, bouclé) and a colour far from the strip's. [opinion]
- Word order: one third-party guide says earlier words weigh more [opinion, unverified] — https://www.eweek.com/news/google-nano-banana-2-cheat-sheet/ . So lead with "TV presenter + genre + set", not with the mask.
- Models re-colour logos "for visibility" by themselves (white on dark, black on light), so name the colours: cream ring, red triangle. [tested/anecdotal, via guide summaries] — https://chasejarvis.com/blog/how-to-add-texture-to-a-logo-with-nano-banana-pro/
- Forum reports say references are sometimes ignored (~20% in one dev's runs), and that no single prompt fixes it, so plan 2–3 rolls per image. [tested, forum] — https://discuss.ai.google.dev/t/nano-banan-pro-ignoring-prompt-and-reference-images/112781

## 2. What makes a still read as "TV presenter"

**Shared codes** (apply to all genres)
- Direct address: the presenter looks straight down the lens, which is TV's "direct mode of address". The interview rule is the opposite (guests look *off* lens), so lens-gaze is what separates the host from the guest. [official-ish, scholarship summary] — https://www.taylorfrancis.com/books/9780203496749/chapters/10.4324/9780203496749-30 ; https://insession.journalism.torontomu.ca/wp-content/uploads/2018/10/InterviewSetupandTIPS.pdf
- The standard anchor frame is a medium close-up cut around mid-chest or just below the armpits, with tight headroom and the lens at eye level. [opinion, training guides] — https://fiveable.me/tv-studio-production/unit-4/shot-sizes-framing/study-guide/qt1wjSPivRMN5Exy
- With a masked face there are no eyes to show the lens-gaze, so the **whole head and shoulders square to camera**, an open hand toward the lens, and a mid-sentence gesture have to carry the address. [opinion]
- Kit that says "broadcast": a hand mic with a **mic flag/cube** (square or triangular station block; Smithsonian holds a 1988 Telemundo "Canal 51" cube) [official museum] https://si.edu/object/canal-51%3Anmah_1848703 ; a clip-on lavalier on the lapel; a coiled earpiece wire; cue cards; clipboard; a floor monitor or autocue glass in the foreground. [opinion]
- Read the set as a set: the edges of the flats, a camera or light stand at frame edge, the audience lit in a darker zone, a floor with tape marks. [opinion]

**Genre menu (16), with tells**
1. **Evening news anchor**: seated behind a desk, hands folded on paper scripts, lapel mic, earpiece wire, slim blank monitor behind one shoulder, cool even key light. [opinion]
2. **Weather forecaster**: standing side-on to a large map wall with an arm sweeping across it, clicker in hand, never wearing the key colour (green/blue), with tighter framing that covers the map. Chroma walls are "one of the most common and oldest" uses of key. [official/trade] https://www.kiro7.com/news/how-does-weather-green-screen-work/43344659 ; touch-panel alternative https://www.newscaststudio.com/2022/08/05/abc-chicago-greg-dutra-touchscreen/
3. **US daytime game show**: pencil-thin Sony ECM-51 stick mic with cable trailing, cue cards held in the same hand, contestant podiums, chaser lights. "Barker… read the price without putting the microphone down." [tested/historical] https://www.museumofplay.org/blog/title/ ; https://aftermath.site/bob-barker-mic-gameshow-sony-ecm-51-match-game/
4. **Late-night monologue / desk**: wooden desk with a mug, guest couch beside it, painted or photo city-skyline backdrop, a band corner. [official/press] https://amp.cnn.com/cnn/style/article/late-night-set-design-history ; https://www.newscaststudio.com/2015/09/14/qa-behind-the-design-of-the-late-show-with-stephen-colbert/
5. **Latin American Saturday variety** (Sábado Gigante type): three hours live, a packed audience close behind, models, a sponsor jingle sung on air, a loud suit, a hand mic held high. [press] https://nexttv.com/news/53-years-hispanic-audiences-left-their-hearts-don-francisco-144162 ; https://www.wunc.org/2012-10-26/sabado-gigante-celebrates-50-with-lots-of-variety
6. **Home-shopping channel**: product on a turntable or held at chest, a price banner on about a quarter of the screen (viewer reports), kitchen or living-room set, warm, even soft light. [tested/viewer] https://community.qvc.com/t5/Suggestion-Box/Hosts-please-state-the-full-price-of-item-not-just-the-easy-pay/m-p/3893871
7. **Breakfast-TV sofa**: two-seat sofa, coffee mugs, a fake sunrise window, a tilted head, a lapel mic, saturated cheerful colours. [opinion]
8. **Children's TV**: kneeling at a child's height, a puppet or a giant felt prop, primary-colour flats, a big open-arm gesture. [opinion]
9. **Cooking show**: island counter, mirror or overhead hint, a wooden spoon raised mid-point, steam, apron over suit. [opinion]
10. **Nature documentary in the field**: crouched in long grass or by a riverbank, khaki shirt, a radio mic pack on the belt, a pointing hand, natural overcast light. [opinion]
11. **Pitch-side sports pundit**: stadium bowl behind, rain jacket or overcoat with a scarf, stick mic with a station flag, floodlights, crowd as soft dots. [opinion]
12. **Election-night results**: huge results wall or touchscreen map, a swingometer, shirtsleeves rolled at 2 a.m., a pointer, a dark studio with coloured blocks. [opinion]
13. **War/field correspondent**: flak vest marked PRESS, helmet under the arm, a dusty city, harsh daylight, a stick mic, a crooked stand-up framing. [opinion]
14. **Telethon**: phone bank of volunteers behind, a giant running-total board, bow tie loosened, a stage at night. [opinion]
15. **Music countdown show**: a number placard, a crowd of teenagers on raised platforms, neon tube lighting, a presenter pointing at the stage. [opinion]
16. **1950s live TV**: a pedestal camera and boom mic in frame, a sponsor's product on a pedestal, a painted flat backdrop, a big ribbon mic on a stand, a cigarette-company-era suit, black-and-white or early colour. [opinion]
17. **Vox-pop street reporter**: a busy pavement, a mic thrust at a passer-by (cropped), a camera-light flare, a scarf in the wind. [opinion]
18. **Infomercial**: a bright white kitchen set, a demo before/after, a lab coat or polo, both hands on the gadget. [opinion]

## 3. Avoiding "AI slop" in studio pictures

- Drop "hyper-realistic, 8k, flawless, masterpiece". Those words push toward a glossy CGI render. Other AI tells: waxy smoothness, symmetric faces, teal-orange grade, HDR halos, perfect light on everyone. [opinion, multiple guides] https://zsky.ai/blog/why-your-ai-images-look-fake ; https://cloudinary.com/guides/image-generation/how-to-make-ai-images-look-real
- Brief it like a photographer: camera, lens, aperture, light source. Google itself advises "photographic and cinematic language". [official + opinion]
- Studio-specific [opinion]: name a specific broadcast era and stock (e.g. 1980s video camera smear, 2000s SD broadcast frame grab, modern phone photo from the floor). Show the craft: gaffer tape on the floor, scuffed desk edge, a visible light stand, uneven spill, a monitor reflecting in the desk. Avoid "LED wall" and "futuristic studio", which give a generic glowing blue grid. Pick one real colour scheme per set.
- **On-screen text:** Google says small text and accurate spelling "may not work perfectly", and recommends generating the text first, then the image [official — blog.google 7 tips; AI Studio docs]. Exact words go in quotes with a named font style [official, Cloud guide]. In practice: keep screens blank, plain colour fields, or soft-focus abstract weather shapes; at most ONE short quoted word (2–6 letters) in a named font; no lower-thirds (add in Premiere). Mic flags and podium fronts: plain colour, or the quoted word. [opinion]

## 4. Masks without eye holes, gloves without bare fingers

- No direct source covers "stop adding eye holes". The closest is a template saying "avoid any visible facial features… keep the masked face area clean and opaque". [opinion] https://youmind.com/prompts/anime-face-mask-template-21143
- Google prefers positive phrasing [official], so describe the surface: "one continuous knitted surface from crown to collar, the face area as smooth and unbroken as the back of the head". Avoid naming "eyes", "eye holes" or "mouth" at all, because naming them summons them. [opinion]
- Naming a specific occlusion relationship helps the model. [opinion] https://www.gaga.art/blog/?p=1899
- **Gloves:** hands are still the weakest body part. Fixes are simple poses, cropping, or a prop that occupies the hand (mic, cue cards, spoon). Say the glove's material and colour and that it continues under the cuff. A high collar, polo neck or scarf covers the hood/collar join. [opinion] https://zsky.ai/blog/fix-ai-faces-looking-weird
- Flow's 16:9 at medium shot keeps the logo large enough to render. In wide shots the ring and triangle shrink and drift, so for wide genres (pitch-side, telethon) frame waist-up. [opinion]
