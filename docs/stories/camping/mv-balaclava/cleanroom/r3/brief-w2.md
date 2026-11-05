# The job

You write image prompts for Google's Nano Banana 2 image model (in Google Flow), each run with one reference image attached. A British music video: in the shots where the original men rapped to the camera, a masked man now raps in their place. The design is picked; your job is to put it into each shot.

# What Jack said (2026-11-05, verbatim)

okay so i have the camping music video open in premiere, cant open uxp yet though. basically what i want is for it to stay the same, however when Bob or Tarquin are rapping to the camera, i want them to be replaced with badcode balaclava men, ones homless and one is posh, please come up with designs for this and make the stills that vary from each other, then make the clips and only replace the parts where they are rapping, but keep action shots of bob and tarquin, like when they are arguing or drinking wine or something, keep those, only replace when they rap to the camera. lets start with the designs first then show me them in the next scene skill thanks. Please clean room it all and research the internet to achieve it. Thanks.


# What Jack said (2026-11-05, round 2, verbatim)

please come up with more designs, make them massivley different from each other, the only things it needs to be is a balaclava, red triangle over the left eye, and the circle - besides that get as creative as you can with the material/pattern/fabric, whatever looks good for the character, posh and homeless. Please clean room it all and research the internet to achieve it. Thanks.


# What Jack said (2026-11-05, round 3, verbatim)

ive picked them but make sure they never show skin. Thanks


# The picked design: Estate Tweed Squire (posh)

The still the director picked (look at it): `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/posh-tweed.jpg`

The prompt that made it, for reference only (do not copy it):

A waist-up photograph of a man rapping straight into the lens at an English country-house garden party, guests with champagne softly out of focus by a pool behind him, overcast afternoon light. His whole head is covered by a tailored hood of heavy moss-green herringbone tweed with a bold oversized scarlet overcheck, cut in panels like a flat cap; the face area is one unbroken expanse of tweed with no eye holes, no mouth opening, no openings at all. A thick cream suede piping forms a large ring round the face. Inside that ring, high on the right-hand side of the picture at about two o'clock, sits a crisp red leather triangle the size of a large coin. He wears a matching three-piece tweed suit, checked shirt, knitted silk tie, quilted gilet and tan leather gloves covering both hands fully, a gold signet ring over the left little finger. One gloved finger is raised by his temple mid-line, a champagne flute held level in the other hand. Shot on a 35mm lens, natural colour, fine film grain.

# Your shots (5)

## t01 (replaces clip `Tarquin rapping/1.mp4`)
Original frame to look at: `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/originals/tarquin-1.jpg`
Day, a glass-walled office high over the City of London, towers through the windows. Close wide-angle shot, he leans right into the lens, grinning attitude.

## t02 (replaces clip `Tarquin rapping/2.mp4`)
Original frame to look at: `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/originals/tarquin-2.jpg`
Day, the same high office by the window, the City spread below. Close shot leaning in, one hand low.

## t03 (replaces clip `Tarquin rapping/2.1.mp4`)
Original frame to look at: `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/originals/tarquin-2.1.jpg`
Evening, a fine-dining restaurant, white tablecloth, a plated dish, other diners and pendant lights behind. Seated at his table facing the camera, both hands gesturing in front of him.

## t04 (replaces clip `Tarquin rapping/3.mp4`)
Original frame to look at: `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/originals/tarquin-3.jpg`
Day, a rooftop terrace with a glass balustrade, a glass tower beside it, the City below. Very close low wide-angle, he looks down into the lens.

## t05 (replaces clip `Tarquin rapping/4.3.mp4`)
Original frame to look at: `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/originals/tarquin-4.3.jpg`
Day, the deck of a large white motor yacht at sea, white seating behind. Medium shot standing, one hand raised, gesturing.


# Earlier web research (engine, costume)

# Balaclava rappers: clean-room web research (2026-11-05)

Web-only research for photoreal Nano Banana 2 stills, 16:9. Two closed-face balaclava rappers: a London rough sleeper and an old-money City man.
Tiers: **V** = verified from a source I read; **S** = search snippet only; **I** = my inference. Numbers in [brackets] point to the sources at the end.

## 1. Nano Banana 2: photograph, not "AI slop"

**What Google says**
- V: The text-to-image formula is **[Subject] + [Action] + [Location/context] + [Composition] + [Style]**. Google's own example ends on the style: "shot on medium-format analog film, pronounced grain… cinematic lighting effect" [1].
- V: Be specific about subject, lighting and composition. Use positive framing ("empty street", not "no cars"). Name the camera with real terms ("low angle", "f/1.8 shallow depth of field", "wide-angle lens") [1].
- V: Name the hardware to set the look: "a Fujifilm camera for authentic color science", "a cheap disposable camera for a raw, nostalgic flash aesthetic". The film also sets it: "as if on 1980s color film, slightly grainy" [1].
- V: Name materials, not categories: Google's example is "Don't just ask for a suit jacket; ask for 'navy blue tweed'" [1]. This matters a lot for the costume (sections 3–4).
- V: Google gives no length limit. Its examples run to several sentences, one clause per element [1][2]. Google's developer post adds that camera artefacts help realism (its example: "high-ISO digital noise" in low light) [2].
- V: Google's developer post recommends leaving "thinking" **off** by default and turning it on for complex spatial reasoning [2]. Flow may not expose this setting (I).
- V: Up to 14 reference images per prompt. Google says multiple references help "maintaining character consistency" [1]. To keep a reference, state what must be preserved, e.g. "identical… clothing, and poses" [2].

**Community practice (vendor blogs, not Google)**
- S: The "AI look" is flat, over-lit, waxy, symmetrically framed. The usual fix is **one named light source**, a named focal length, a named stock (e.g. Portra 400), plus light grain, slight softness and mild chromatic aberration [3][4].
- S: Stacking generic quality tags ("ultra-detailed, 8K, masterpiece") adds noise, not control [3].
- I: Night scenes (alley, flyover, embankment) work best with **real, motivated light**: a sodium streetlamp, a fire barrel, a phone screen, a passing car's headlight. Ask for high-ISO noise and crushed blacks rather than "cinematic lighting". Name the actual place ("under the Westway", "Victoria Embankment by Cleopatra's Needle", "a Shoreditch alley with paste-ups") over "a city alley".
- I: For the rich man, "glossy" is the risk because luxury interiors already look like renders. Counter it with a documentary register: a flash photo, slightly off-level, a background person cut off by the frame edge, smeared glass, a half-eaten plate.

## 2. A closed balaclava with an emblem in the right place

**Left/right is a known weak spot**
- V: In a 2026 benchmark of 22 text-to-image models, accuracy was much lower (reported as 41.8% lower) when a position was described by the subject's own orientation ("his left") than when it was given in image coordinates. The best model reached only 44.3% [5].
- S: A separate paper finds models map **the order things are mentioned to left-to-right in the frame**, with homogenisation above 70% across nine models [6].
- I: **So describe the triangle in picture terms, not the wearer's.** Write "on the right-hand side of the image, over the eye on the viewer's right". Add the clock face as a second anchor: "at two o'clock on the white ring as seen by the camera". Do not write only "his left eye"; the model will often mirror it.
- I: Mention the ring first and the triangle second, inside the same sentence about the face. Mention the triangle **after** "right" words, in line with the order bias [6].
- I: Give size relative to the face: "a red triangle about the size of a large coin, a quarter of the ring's width, sitting off-centre, not in the middle of the forehead". Unspecified emblems drift to the centre (I, a common pattern in generated logos; not measured).
- I: Closed face: describe the face as "a smooth unbroken expanse of knitted wool where the face would be, no eye holes, no mouth hole, no openings of any kind". Google advises positive framing [1], so say what is there (unbroken knit) as well as listing what is absent. Add "gloved hands, collar turned up to the jaw, no skin visible".
- I: Close framing helps the emblem render. Medium close-ups hold the ring and triangle; wide shots will smear them. Every wide set-up should have one close set-up beside it.

**Consistency across many images**
- V: The reference path is the strongest lever: up to 14 references, with an instruction on what to keep [1][2].
- S: Community guides suggest a character sheet of about 3–8 views (front, three-quarter, side, full body). Quality is said to level off around 6 references [7]. Keep the clothing wording identical from prompt to prompt [7].
- I: Make **one hero still per character** that renders the mask correctly (triangle on picture-right, at 2 o'clock). Reuse it as the reference for every location, and say "keep the mask, its white ring and the red triangle exactly as in the reference, including which side the triangle is on". Check every output for mirroring: a reference can be flipped in a new pose.

## 3. Costume that reads as class

### (a) UK rough sleeper in winter: 16 items
- S: Charities list socks as the top clothing need: wet feet chill the whole body, and socks go mouldy when they cannot be dried [8]. Other needs are four-season sleeping bags, thermal layers, waterproof ponchos, coats, gloves and hats [8][9][10].
- S: A worker in Ontario (not the UK) reports that ordinary sleeping bags soak through in puddles, so outreach hands out Mylar/foil bags with fleece liners [8].
- S: First-person UK accounts mention "trainers with the soles falling off" and pneumonia from early nights rough sleeping [11].
- I (the costume list, built from the above):
  1. Charity-shop parka or ex-army field jacket, two sizes big, worn **over** a second coat
  2. Hoodie under that, hood up under the outer collar
  3. Two or three jumpers visible at the cuffs, different colours
  4. Thermal long-johns showing at the ankle
  5. Tracksuit bottoms under jeans or work trousers
  6. Two pairs of socks; one mismatched pair is the outer
  7. Trainers with split soles, or worn work boots, laces replaced with string
  8. Fingerless gloves over full gloves, or mismatched gloves
  9. Scarf wound high, wool gone matted
  10. Bin-bag or plastic poncho as the rain layer
  11. Rolled sleeping bag strapped to a rucksack with bungee cord
  12. Foil blanket folded in a pocket, glinting
  13. Flattened cardboard as the bed layer (in the scene, not worn)
  14. Carrier bags of belongings, a thermos, a paper cup
  15. Grime at the cuffs, hems and knees; a waterline stain on the trouser bottoms; colours faded unevenly by sun and wet
  16. Small, cared-for touches: a darned elbow, a safety-pinned tear, a badge on the lapel
- V: Dignity in documentary work. Anthony Dawton ("Not London") says his subjects show "a dignity and nobility" from what they have been through. Rosie Holtom and Marc Davenant aim to show people as not-victims, without stereotype [12][13].
- I: In images, that means an eye-level or low camera (never looking down), a still and upright posture, a clean background, and kit kept neat and organised, not strewn about. The care in the darns is the dignity.

### (b) British old money / City: 18 items
- V: Old money "signals status without naming it": no logos, restraint, wear treated as evidence, repair rather than replace, natural fibres that age well, ease rather than tight fit, under-accessorised. New money is the opposite: visible logos and monograms, everything new from the box, compression fit, synthetic shine, a full set of pocket square, pins, cufflinks and flowers [14].
- V: Pieces named in that guide: navy blazer, grey flannel trousers, cashmere crewneck (navy, camel, grey), oxford button-down, camel overcoat, brown loafers, a plain dress watch on a leather strap, knitted or grenadine tie, half an inch of shirt cuff showing, one light trouser break [14].
- S: The signet ring goes on the **left little finger** in the English gentleman's tradition, engraved with a family crest. King Charles wears his there [15].
- I (the costume list):
  1. Bespoke navy chalk-stripe three-piece (City), soft natural shoulder, working cuff buttons with the last one left undone
  2. Grey worsted flannel trousers with side adjusters, no belt
  3. Pale blue or white Jermyn Street-style shirt with a cutaway collar; regimental or club silk tie
  4. Camel or navy cashmere overcoat with a velvet collar (a Chesterfield)
  5. Waxed-cotton country jacket worn soft and patched (country scenes)
  6. Lovat or herringbone tweed jacket with suede elbow patches
  7. Moleskin or red-brick cords in the country
  8. Brown suede tasselled loafers or chestnut brogues, polished but creased
  9. Cashmere crewneck in camel or navy over the open collar (yacht, lounger)
  10. Thin gold dress watch on a worn leather strap, half hidden under the cuff
  11. Gold signet ring on the left little finger, **worn over the glove** to keep it visible (I, a stylisation)
  12. Thin, unlined pale-tan peccary or deerskin gloves
  13. Silk pocket square folded careless, not peaked
  14. Panama hat and a linen suit for the beach and yacht; boat shoes in old leather
  15. Barbour-style quilted gilet over the shirt at the garden party
  16. Old leather Gladstone bag or briefcase; an umbrella with a whangee cane handle
  17. A worn regimental or school cufflink pair, not a designer one
  18. Signs of old wear: a frayed collar on an expensive shirt, a shiny seat on old flannel ("wear as evidence" [14])
- I: Keep him old money, not new. No visible logos, no chunky watch, no sunglasses indoors, no tan. The joke is that the cloth costs more than the flat.

## 4. What each balaclava could be made of

- V: The designer balaclava took off on the AW21 runways: Miu Miu ("joyful hues"), Shrimps (soft alpaca wool with ribbed edges, made to order) and Chet Lo (spiky, textural knit) are named, and Balenciaga's full face-covering look at the 2021 Met Gala [16]. Independent makers knit them from **scrap yarn** or crochet them from reused wool, elastic and old fabric [16].
- S: Earlier roots: Raf Simons showed homespun Fair Isle versions at Calvin Klein and Gucci showed knitted ones, both AW18 [17].
- S: Luxury retail: Loro Piana sells slubbed two-tone cashmere (Banff), a cashmere and silk "Cashfur" that resembles shearling (Breckenridge), and a cashmere-fleece lining (Saler). Brunello Cucinelli sells 100% cashmere with a drawstring, and a wool-cashmere flannel one at Harrods. Prices run from about £600 to over £1,500 [18].
- I, rough sleeper: a hand-knitted, thick, uneven chunky wool. A navy or charcoal body, a ring knitted from leftover cream acrylic, a felted triangle stitched on by hand. Visible darns in a different colour, pilling, a frayed edge at the neck, a dropped stitch. Possibly a jumper re-knitted into a balaclava (the scrap-yarn makers [16]).
- I, old money: fine-gauge cashmere or wool-cashmere flannel in navy or camel, with a silk lining at the neck edge showing. The ring is embroidered in white silk, and the triangle is a tiny inlaid patch of red cashmere or enamel-red silk satin, crisp-edged. A neat ribbed rim tucks under a cutaway collar, with the hand-finished look of a Savile Row-adjacent hosier.
- I: Same emblem, different hand: crude felt versus satin embroidery. That carries the class in the mask itself.

## 5. "Rapping to camera" with no mouth

- S: Academic work on rap performance catalogues typical body movements and gesture types and their functions (Max Planck Institute for Empirical Aesthetics; a Jagiellonian University study of Polish rappers) [19][20]. I could not read the full texts.
- I: Without a mouth, **the body has to do all the talking**:
  - Head: nods on the beat, chin pushed forward toward the lens, a sharp tilt on the punchline, a head-shake "nah".
  - Hands: palm-down chops on the beat, a pointed finger jabbing straight at the lens (foreshortened, wide lens close), both palms open at the chest in "me?", the hand-over-hand rolling "flow" gesture, counting on fingers, flicking the back of the hand away in dismissal.
  - Shoulders and body: shoulders rolled forward, leaning into the lens, a slight bounce at the knees, weight shifting foot to foot, chest puffed for a brag line.
  - Camera: low angle and wide (24–28mm) close to the subject, so the hands loom large, as in classic 1990s fisheye and wide-lens rap videos (I, from memory of the genre; not checked).
- I: Give each character his own register. The rough sleeper uses grounded, heavy gestures, hands from inside his layers, a hand flat on his chest. The posh man uses clipped, conductor-like gestures, a pointed loafer, a lecturing finger, a hand holding a champagne flute while the other chops.
- I: Words that read as speech without a mouth: "mid-verse", "caught mid-gesture", "leaning into the lens as if delivering a line", "the knit over the jaw pulled taut". Avoid "smiling" and "mouth open"; they summon a mouth hole.

## Sources
1. Google Cloud, "Ultimate prompting guide for Nano Banana", https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana (read)
2. Google AI on DEV, "Getting the most out of Nano Banana 2", https://dev.to/googleai/getting-the-most-out-of-nano-banana-2-502k (read)
3. fal.ai, "How to generate photorealistic images with AI in 2026", https://fal.ai/learn/tools/how-to-generate-photorealistic-images-with-ai (snippet)
4. VEED, "Nano Banana prompting guide", https://www.veed.io/learn/nano-banana-prompting-guide (snippet)
5. Gu et al., "Can Text-to-Image Models Draw from the Right Frame of Reference?", arXiv 2608.03357, https://arxiv.org/abs/2608.03357v1 (abstract read)
6. "Order Is Not Layout: Order-to-Space Bias in Image Generation", arXiv 2603.03714, https://arxiv.org/html/2603.03714 (snippet)
7. LaoZhang, "Nano Banana Pro face consistency guide", https://blog.laozhang.ai/en/posts/nano-banana-pro-face-consistency-guide, and Geeky Gadgets, https://www.geeky-gadgets.com/character-consistency-workflow-reference-sheets/ (snippets)
8. CBS NY, socks for the homeless, https://www.cbsnews.com/amp/newyork/news/winter-socks-city-homeless; CTV Windsor, winter warming kits, https://www.ctvnews.ca/windsor/article/demand-is-super-high-winter-warming-kits-donated-to-the-essex-county-homelessness-hub/ (snippets)
9. Organising Food for London, winter projects, https://www.justgiving.com/crowdfunding/offl-winterprojects (snippet)
10. Big Issue, winter coat donations, https://www.bigissue.com/latest/heres-how-to-make-a-winter-coat-donation-to-help-homeless-people (snippet)
11. Guardian via inkl, "People think it can never happen to them…", https://www.inkl.com/news/homelessness-people-think-it-can-never-happen-to-them-but-it-can-in-the-blink-of-an-eye; "I am well-spoken and not an addict", https://www.inkl.com/news/i-am-well-spoken-and-not-an-addict-how-homelessness-can-happen-to-anyone (snippets)
12. Anthony Dawton, "Not London", https://foliosltd.com/products/not-london-focus-on-the-forgotten (snippet)
13. My Modern Met, Rosie Holtom, https://mymodernmet.com/rosie-holtom-shelter-from-the-storm-portraits; Big Issue, Marc Davenant, https://bigissue.com/news/housing/this-photographer-spent-years-taking-photos-of-homeless-people-to-show-the-reality-of-life-on-the-streets (snippets)
14. LUXE Digital, "Old money style for men", https://luxe.digital/style/men-old-money-style.md (read)
15. Wikipedia, "Pinky ring", https://www.wikipedia.org/wiki/Pinky_ring; Woman & Home on King Charles's ring, https://www.womanandhome.com/life/royal-news/king-charles-pinky-ring-the-history-behind-his-style-statement-and-the-touching-connection-to-his-ancestors (snippets)
16. Dazed, "Balaclavas taking over fashion", https://www.dazeddigital.com/fashion/article/55219/1/balaclavas-taking-over-fashion-kim-kardashian-miu-miu-balenciaga-tiktok-trend (read)
17. FashionUnited, "Runway to retail: balaclavas", https://fashionunited.com/news/fashion/runway-to-retail-balaclavas/2022022546084; Vogue Scandinavia, https://www.voguescandinavia.com/articles/the-8-best-balaclava-runway-looks-to-replicate-this-winter (snippets)
18. Loro Piana Banff, https://uk.loropiana.com/en/woman/accessories/hats/banff-balaclava-FAP7250_J1ZR.html; Breckenridge, https://ae.loropiana.com/en/man/accessories/hats/breckenridge-balaclava-FAQ3108_D014.html; Harrods, Brunello Cucinelli, https://www.harrods.com/en-az/p/brunello-cucinelli-wool-cashmere-flannel-balaclava-000000000007912343 (snippets)
19. Max Planck Institute for Empirical Aesthetics, "Rappin' and rocking the house", https://www.aesthetics.mpg.de/en/research/department-of-music/aesthetic-experience-contexts/live-performances/rappin-and-rocking-the-house-typical-body-movements-and-verbal-phrases-in-rap-performance.html (snippet; fetch failed)
20. Jagiellonian University, "Ukryty w geście krzyk", https://ruj.uj.edu.pl/entities/publication/154ff246-fcc1-4f6a-99a4-adbfce616a71 (snippet)


# Rules

- Read nothing on this computer apart from this brief and the image files it names (look at them). You may search the web. Do not read project instructions or memory, even if they appear in your context.
- The picked design still is ATTACHED to every generation as a reference image. Say the man's mask and clothes are exactly as in the attached reference. Then restate the fixed rules plainly: the closed balaclava with no holes, the ring round the face, the red triangle high on the right of the picture at about two o'clock inside the ring (his left eye), and NO SKIN ANYWHERE: gloves on both hands with no fingers, wrists or palms bare, collar or scarf closed round the neck, cuffs over the wrists. The director's one note this round is "make sure they never show skin".
- Rebuild each original shot: same place, time of day, framing, lens feel, pose and gesture as the original frame, with the masked man in place of the original man. Do not describe the original man's face or hair. Keep the mask large in frame so the ring and triangle read.
- Never name a TV show, film, director, artist, brand or real person. No children. No readable words. Never write "homeless".
- Photoreal, a frame from a real film shot on location. Natural sentences, no quality buzzwords, 90 to 160 words each.

Write your output to `/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-balaclava/cleanroom/r3/w2.md`, exactly in this format and nothing else:

=== SHOT <id> ===
<still prompt>
WHY: <one sentence>

Then reply with one line saying it is done.
