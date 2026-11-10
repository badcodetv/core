# Priority Lane — clean-room research r1 (web only)

Dated 2026-11-10. Written from the open web and the one reference image (`../reference/look-ref-rainy-night-traffic.png`); no repo notes were read.
Evidence tiers: **[V]** verified from the source page itself · **[S]** several independent users/blogs agree · **[A]** single anecdote, or my own inference (labelled).

## 0. What the reference image actually is

Low, slightly tilted handheld view from a lane edge (a crash barrier cuts the bottom-right corner), shot into a jam of brake lights. The camera is focused mid-distance, with a soft foreground car on the left. Two sodium-orange street lamps bloom into the haze. Shadows and sky go teal/green-black rather than neutral black. The tarmac is wet, with long vertical red smears, not mirror reflections. Fog flattens the background into a pale band. There is clear grain, the frame is underexposed overall, and the blacks are lifted rather than crushed. Nothing is centred and nobody is the subject. (Description, mine.)

## 1. Prompting Nano Banana 2 for film-photo stills

- **[V]** Nano Banana 2 = Gemini 3.1 Flash Image; launched Feb 2026; supports 9:16 natively. Google's guide says: *"A simple list of keywords won't cut it; you need to describe the scene narratively."* Its formula: **[Subject] + [Action] + [Location/context] + [Composition] + [Style]**. Google suggests naming hardware for its look (e.g. "a Fujifilm camera for authentic color science", "a cheap disposable camera for a raw, nostalgic flash aesthetic"), lens/aperture ("shallow depth of field (f/1.8)"), and grade ("as if on 1980s color film, slightly grainy"; "cinematic color grading with muted teal tones"). Materials must be specific ("navy blue tweed", not "suit jacket"). On negatives it says: *"Describe what you want, not what you don't want (e.g. 'empty street' instead of 'no cars')."* It gives no recommended prompt length. — https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- **[V]** Google's photoreal template: "A photorealistic [type of shot] of a [subject] in a [setting]. [Description of the light]. Shot from a [camera angle] with a [lens type]." — https://aistudio.google.com/docs/image-generation ; https://developers.googleblog.com/en/how-to-prompt-gemini-2-5-flash-image-generation-for-the-best-results/
- **[S]** Naming a film stock and a vintage prime adds grain and breaks the smooth AI gradient. One worked example uses a fast stock "pushed two stops", grain, and "halation around light sources". — https://budgetpixel.com/blog/analog-neon-prompting-1990s-cyberpunk-street-photography ; https://z-image-astroblog.pages.dev/blog/nano-banana-image-prompting-the-5-layer-framework
- **[S]** Stacked hype words ("8K, HDR, ultra-detailed, hyper-real") push the image toward the glossy, over-processed look. Several guides say to keep to roughly 3–6 deliberate modifiers. — https://z-image-astroblog.pages.dev/blog/nano-banana-image-prompting-the-5-layer-framework ; https://magicshot.ai/blog/why-your-ai-images-still-look-fake-12-tells-and-how-to-kill-them
- **[S]** These are the AI-slop tells, each with the counter people report:
  - Waxy skin: ask for natural skin texture, pores and slight asymmetry.
  - Flat, even light: name one light source and its direction.
  - Everything sharp: name where focus falls and what is soft.
  - Shallow focus on every image is also a tell, so choose focus per shot.
  - Banning "wrinkles" can backfire and push the skin smoother.

  Sources: https://cloudinary.com/guides/image-generation/how-to-make-ai-images-look-real ; https://dev.to/pretty_lilac/i-studied-200-ai-image-prompts-to-figure-out-why-most-ai-photos-look-fake-heres-what-actually-245g
- **[A]** NB2 is said to be "more literal", rewarding precision and punishing ambiguity. — https://content.getdarwin.ai/en/nano-banana-2-prompt-guide-how-to-write-better-prompts
- **[A, my inference]** I found no source on centred, symmetrical composition, so this is an inference. Writing where the subject sits in the frame ("lower left, cut by the frame edge"), plus a foreground obstruction, should break the default centre.

## 2. The look: rainy night, sodium vs teal, film

- **[V]** CineStill 800T is balanced for 3200K tungsten. It has no anti-halation layer, which gives a red glow round bright point lights. Night streets under mixed sources (sodium, LED, neon) are its signature use, and it keeps sources varied rather than neutralising them. — https://www.uniquephoto.com/photoinsider/cinestill-800t-profile-tungsten-film-halation-glow-and-night-streets ; https://brooklynfilmcamera.com/blogs/guides/cinestill-800t-review-the-night-photography-film
- **[S]** Sodium lamps are near-monochromatic orange (589 nm for low pressure). Daylight film under sodium goes "orange and muddy", and tungsten stock keeps it warm but cleaner. Orange vs cool sky/shadow is the classic complementary contrast. — https://www.shopmoment.com/articles/cinestill-800t-first-impressions ; https://www.nationalparksatnight.com/blog/2019/4/20/the-color-of-night-the-proliferation-of-leds-and-its-effects-on-how-we-photograph
- **[A, my inference, unsourced]** Why the shadows go teal: tungsten balance pulls cool and mercury/LED sources toward cyan, while the sodium stays orange.
- **[V]** UK/EU cities have largely switched orange sodium to white LED, as astronaut before/after photos show. So orange sodium now reads as "a few years ago" or "film". — https://petapixel.com/2026/09/08/astronauts-before-and-after-photos-show-how-cities-switched-from-orange-to-white-light/
- **[S]** Rain turns every surface glossy and reflective at night, and practitioners say to embrace it. — https://www.35mmc.com/31/03/2019/my-dark-side-night-photography-with-cinestill-800t-film-by-christian-schroeder/ ; https://petapixel.com/2025/10/03/queen-of-the-night-cinestill-800t-film-feels-made-for-neon
- **[V] Photographers to look at** (verified to exist; the descriptions are from the sources):
  - **Christophe Jacrot**, Paris-based: cities under rain and snow, with books on Paris, Hong Kong and New York in the rain. He names Saul Leiter as an influence. — https://mymodernmet.com/christophe-jacrot-photography ; https://www.digitalcameraworld.com/features/i-find-the-dramatic-power-of-bad-weather-captivating-christophe-jacrot-explains-why-he-loves-to-take-photos-in-stormy-weather
  - **Saul Leiter**: shot through rain-streaked windows, with faces hidden by umbrellas or glass. His work is mostly by day, not night.

## 3. Vehicle interiors at night

- **[S]** The film rule for car interiors at night is "less is more". The main source is moving light outside the car, not a steady key inside:
  - Passing streetlight sweeps, with lamps gelled to match the street colour and dimmers ridden in time.
  - Headlight pairs, plus red-gelled taillights from cars behind.
  - Low dashboard-level practicals.
  - Interior fill about two stops under the key.

  Sources: https://cinematography.net/edited-pages/Nightime_Car_Interior.htm ; https://nofilmschool.com/2018/11-driverx-cinematography ; https://www.litepanels.com/en/applications/how-to-light-a-car-scene-at-night/
- **[S, secondary sources only]** *Bringing Out the Dead* (1999) was directed by Martin Scorsese and shot by Robert Richardson, ASC. The ASC article is reported to say:
  - The ambulance was lit for driving scenes on a process trailer, with up to half a dozen lights.
  - There was mostly no steady light inside the cab; the light simulated passing streetlights.
  - The look grew more extreme as the story went on.

  I could not open the ASC pages (404), so treat these details as unverified. — https://theasc.com/magazine/nov99/urban/pg1.htm (dead) ; https://variety.com/1999/film/reviews/bringing-out-the-dead-1117752257
- **[A, my inference, unsourced]** Practical sources for an ambulance:
  - The rear compartment has cold white overhead strips; blue beacon spill comes through the windows.
  - The cab has dash/instrument glow and the sodium sweep.
  - In a prompt, name each source and its colour, and let the face be half dark.

## 4. Vertical 9:16

- **[S]** Practitioner tips for vertical framing:
  - Push *into* depth rather than tracking sideways, and stack foreground, middle and back vertically.
  - Excess headroom reads as "wasted" faster in 9:16.
  - Keep faces and key action out of the bottom third (captions/UI); a rough rule is to keep text in the middle 60%.
  - Leave lead room ahead of movement.

  Sources: https://dev.to/cartney/vertical-video-composition-for-drama-the-2026-guide-567l ; https://www.adamsebire.info/vertical-film-festival/9-16-tips-and-tricks/
- **[A, my inference]** The reference frame is landscape. In 9:16 its natural translation is a deep corridor: lamp bloom high, the brake-light jam in the middle, and wet tarmac smears in the lower half.

## 5. Policy blocks (Flow / Nano Banana)

- **[V]** Google's published filter categories (Vertex Veo docs; the consumer Flow wording may differ) are Celebrity, Violence, Dangerous content, Child, Hate, Sexual, Toxic, Vulgar and Other. **Celebrity blocks photorealistic depictions of prominent people.** — https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/responsible-ai-and-usage-guidelines
- **[S]** Flow's "prominent people" error also fires falsely on fictional characters and cartoons. — https://discuss.ai.google.dev/t/critical-bug-google-flow-prominent-people-safety-filter-broken-systematically-blocking-all-fictional-character-generations/173121
  - **Politicians:** never name or describe a real one. A generic, fictional "minister in a dark suit" is the safe shape, but it can still false-trip.
- **[S]** There are two block stages: at the prompt (CONTENT_BLOCKED) and on the output image (IMAGE_SAFETY). The same prompt can pass one run and fail the next. — https://docs.apiyi.com/en/faq/nano-banana-image-failure ; https://yingtu.ai/en/blog/nano-banana-blocked-safety-filter
- **[S]** "Blood", "dead body" and "weapon" are reported keyword trips even in a legitimate context; "crimson/dark stain" is the usual swap. Nano Banana 2 reportedly added stricter rules for famous people (vendor claim, unverified with Google). — same sources.
- **Unknown (nothing found):** I found no reports either way on police, ambulances, uniforms or a masked figure specifically. **[A, inference]** Uniforms and vehicles alone are unlikely to trip. The risk rises when you combine a masked figure + police + injury (it reads as violence), and with wounds described graphically. Keep the patient's injury implied: a blanket, an oxygen mask, a monitor glow.

## Do / don't for prompt writers

**Do**
- Write one paragraph of scene in plain prose, in the order subject, action, place, framing, light, film.
- Name the stock and the result: "shot on CineStill 800T, red halation round the lamps, visible grain, underexposed, lifted blacks".
- Name every light source and its colour: sodium orange lamp, red brake lights, blue beacon spill, dashboard glow. Let everything else fall to teal-black.
- Say where focus falls and what is soft. Put something in the foreground: a barrier, a rain-streaked window, a blurred car.
- Place the subject off-centre and let the frame edge cut things. Allow a slight tilt, as if handheld.
- Write rain as consequence: "streaked red reflections on wet tarmac", "drizzle haze round the lamps".
- Frame 9:16 deep: the light up top, the action in the middle, wet ground below. Keep faces above the bottom third.

**Don't**
- Don't stack "8K, HDR, ultra-detailed, hyper-realistic, masterpiece".
- Don't use negations ("no cars") or ban the flaws you want.
- Don't put everything in sharp focus or use shallow focus on every frame.
- Don't centre the subject or make symmetrical heroic framing your default.
- Don't name or resemble a real politician.
- Don't write "blood", "dead" or "wound". Avoid pairing a masked figure with police and violence in one prompt.
- Don't describe perfect faces. If people are in shot, give them pores, tiredness and asymmetry, or keep them half in shadow.
