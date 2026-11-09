# Clean-room research: the balaclava presenter (Nano Banana 2.x stills → Omni Flash)

Web research only, 2026-11-09. Tags: [official] = Google docs/blog; [tested] = hands-on test or measured study with examples; [opinion] = blog, vendor or forum opinion, or this researcher's own synthesis (says so where it is).

## 0. Which model

- Nano Banana 2 = Gemini 3.1 Flash Image (announced 2026-02-27). **Nano Banana 2.1** (`gemini-nano-banana-2.1`) shipped 2026-10-06 and is rolling out to Flow among other surfaces. Google lists 1K/2K/4K output "with improved realism", better prompt adherence and multi-turn character consistency, up to 14 references (4 characters, 10 objects), and a fix for tiling artifacts on wide ratios at 2K/4K. [official] https://aistudio.google.com/docs/models/gemini-nano-banana-2.1 ; launch coverage https://www.techrepublic.com/article/news-google-nano-banana-2-1-image-editing-pricing/
- Gemini 3.1 Flash Image was scheduled for API shutdown 2026-10-29, with 2.1 as its replacement. [opinion, press report] https://letsdatascience.com/news/google-rolls-out-nano-banana-21-image-model-c6ac3b89
- A Flow web build pointed to "Nano Banana 2.1" from 2026-09-27. [opinion, build sleuthing] https://testingcatalog.com/new-google-flow-build-now-points-to-nano-banana-2-1
- **Check in the Flow model menu which one "Nano Banana 2" now resolves to.** Not verified here.

## 1. Photoreal without the "AI slop" look

What Google says:
- Structure: **[Subject] + [Action] + [Location/context] + [Composition] + [Style]**. Write it as narrative sentences: "a simple list of keywords won't cut it." [official] Google Cloud, "The ultimate Nano Banana prompting guide", 2026-03-06, https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- Name materials, not categories: "Don't just ask for a suit jacket; ask for 'navy blue tweed.'" [official] same.
- Camera bodies change the rendering: "cheap disposable camera" (raw, nostalgic flash), "Fujifilm" (colour science), "GoPro" (distortion). Also film and grade cues, e.g. "as if on 1980s color film, slightly grainy". [official] same.
- Phrase it positively: "empty street", not "no cars". [official] same.
- Photoreal template: "A photorealistic [shot type] of [subject] in [setting]. [Light]. Shot from a [camera angle] with a [lens type]." Aspect ratio can go in the prompt text. [official] https://aistudio.google.com/docs/image-generation
- Iterate in multi-turn conversation rather than re-rolling from scratch. [official] same.
- Google gives no word count. Its examples are 2–5 sentences. A third-party 2.1 guide recommends "a short brief in full sentences… one clear scene works best". [opinion] https://morphic.com/resources/how-to/nano-banana-2-1-guide (2026-10-06; its examples were made on NB2, not 2.1)

Tells, and what works against them:
- "hyperrealistic", "8K", "4K", "ultra-detailed" push the image toward a game-render or plastic look. Naming a real camera, lens and light works better. [opinion, consistent across many guides] e.g. https://askyourpdf.com/blog/ai-prompts-for-realistic-photos
- Uniform sharpness front to back is a giveaway. Real photos have one focal plane and falloff. [opinion] https://cloudinary.com/guides/image-generation/how-to-make-ai-images-look-real
- "Perfect / flawless / beautiful / symmetrical" produce influencer sheen. Ask for imperfection on purpose: wear, mess, stray objects, uneven light. [opinion/tested by one creator] https://reddit.sentinel-team.org/posts/1rg8o43/snapshots/2026-03-02T19%3A47%3A23.618387Z
- NB2 outputs described as "a mix of CGI, digital drawing and over-processed photography": exaggerated micro-detail, harsh outlines, oversharpening. [opinion] https://reddit.sentinel-team.org/posts/1rflxt2/snapshots/2026-02-27T15%3A22%3A02.187305Z ; https://10b-ai-blog-frontend.pages.dev/blog/fix-nano-banana-errors
- One report says NB2 at 2K/4K came out blurry and washed out while 1K was fine, so compare the sizes before committing. [opinion, single forum report] https://discuss.ai.google.dev/t/nano-banana-2-2k-4k-outputs-are-blurry-and-washed-out-while-1k-works/171851
- **Flow-specific:** one user found the same wrong lighting and shadow kept coming back across 100+ prompts in one Flow project. It went away in a **fresh blank project**, or with a prefix telling Flow to ignore project memory. Project context appears to leak into new generations. [tested, one user, 2026-07-30] https://discuss.ai.google.dev/t/how-to-fix-persistent-shadow-loops-asymmetrical-skin-tones-on-flow-flow-nb2-pro/176678
- Centred, symmetrical "studio" composition is itself a slop tell. Off-centre framing and a cluttered, specific location read as observed rather than generated. [opinion, researcher synthesis of the above]

## 2. Putting a small mark on a specific side

- A 2026 benchmark of 22 text-to-image models, including Gemini 2.5 Flash Image, 3 Pro Image and 3.1 Flash Image, found models **default to the image/viewer frame**. When a prompt used the subject's own left/right ("his left hand") on a figure facing camera, 74% of generations put the object on the literal *image* side named. Left/right relations had the biggest error of any relation tested. Camera-view phrasing beat subject-frame phrasing in every model (closed models: 50.6% vs 29.1%). [tested] https://huggingface.co/papers/2608.03357 (arXiv 2608.03357, ~Aug 2026)
  - Practical reading: for a face-on presenter, the wearer's LEFT eye is **image right**. Say "on the right side of the image / frame right". Never say "his left" alone, because the model will probably put it on image left. [opinion, researcher inference from the tested result]
- Forum reports: "on the viewer's left" cannot be misread, "his left" can. Anchoring to a landmark ("above the eye nearest the window") or describing it as part of the object's anatomy can work better than left/right words. [opinion] https://community.openai.com/t/image-gneration-is-great-but-struggles-with-left-right-direction/1245598 ; https://techcommunity.microsoft.com/discussions/microsoft-copilot/ai-image-generator-repeated-mistakes/4463578
- The 2.1 guide says left and right get mixed up and recommends anchoring positions to objects. [opinion] https://morphic.com/resources/how-to/nano-banana-2-1-guide
- Logos drift even when the prompt says "keep exactly the same". Prompting alone does not reliably reproduce a specific brand mark. Supplying the mark as a separate reference image with a stated role is the usual workaround. [opinion, forum + vendor] https://discuss.ai.google.dev/t/how-to-keep-logo-intact-on-a-product-image/106665 ; https://helpcenter.kaiber.ai/articles/0681742-put-your-logo-on-a-product-in-kaiber-canvas
- Nothing found tests "solid vs outline" or clock-position phrasing. Untested ideas: name the fill ("filled solid red felt", "a solid patch, no hollow centre"), give it a size against a landmark ("thumbnail-sized"), and describe the ring as off-centre to the triangle. [opinion, researcher, untested]
- Flipped outputs: the mark can be fixed afterwards with a horizontal flip only if nothing else asymmetric is in shot (text, wine hand). Note this as a fallback. [opinion]

## 3. Real textile: knit, embroidery, appliqué

- Google's own advice to name materials exactly applies here: yarn type, gauge, stitch. [official] Cloud guide above.
- Tells of AI knitwear (written by a knitter): stitch columns don't line up; stitches at impossible widths ("k1.5" ribs); motifs vary between repeats; ribbing runs both ways; colour changes look **painted on** instead of knitted, duplicate-stitched or sewn; edges and collars become tangled loops; no shaping or decreases at the crown. [tested, examples, 2025-06-26] https://jaggedlines.substack.com/p/identifying-ai-generated-knitwear
  - So: give the construction (rib-knit, crown decreases, seam), and make the ring and triangle a **separate layer**: felt appliqué with a visible edge stitch, or chunky embroidery thread. A colour change in the knit is where models fake it. [opinion, researcher inference]
- Imperfection words lift realism in textiles: pilling, stray fibres, loose thread, uneven stitch, fuzz catching backlight, "soft fuzzy nap", "visible slubs". [opinion] https://www.promptzone.com/zenja/tactile-magic-mastering-felt-and-yarn-art-prompts-3dg2.md ; https://selfielabstudio.com/blog/ai-image-prompts-creating-convincing-fabric-textures-20260206
- A flat-looking logo on fabric is a giveaway. The mark should follow the curvature of the head and the folds, pick up the cloth's shading, and sit slightly raised. Keep the effect subtle. [opinion, vendor] https://agent.vizard.ai/how-to/make-a-logo-sit-on-fabric-instead-of-looking-pasted-on.html (updated 2026-10-10)
- Wool is matte. A rim or backlight shows the fuzz halo, while flat front light kills the texture. [opinion, general photography]

## 4. No skin anywhere; no holes in the mask

- Nothing found tests this directly. The model's prior is strong: gallery prompts describe balaclavas almost always with eye or mouth openings ("eyes visible through narrow slits", "two distinct eye holes or an additional hole for the mouth"). Expect holes by default. [tested-ish, observed in public galleries] https://www.krea.ai/feed/a-low-angle-cinematic-portrait-of-a-masked-figure-standing-aedbe031-6612-5475-8cd6-07cad8058e22 ; https://youmind.com/en-US/nano-banana-pro-prompts?id=11707
- Google's advice to describe what you want positively suggests describing the surface itself: "a continuous unbroken knitted surface where the face would be". Repeating "no eye holes" can summon them. [official principle + opinion on application] Cloud guide above.
- A reference image of a hole-less hood, given one stated role ("use only for the hood's shape"), is the strongest lever offered by the tools: 14 refs, each with a purpose. [official capability; application is opinion] https://aistudio.google.com/docs/models/gemini-nano-banana-2.1
- For skin: name every boundary as clothing ("gloved hands", "collar buttoned to the hood", "cuffs past the wrist"). Gloves holding a wine glass are a stress point for hand anatomy, and hands are the most common artefact site, so check them. [opinion] https://cloudinary.com/guides/image-generation/how-to-make-ai-images-look-real
- Flow text prompts have no negative field. Exclusions go in the prose, and Omni does the same. [opinion] https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide

## 5. A menu of real low-budget TV registers (genuinely different)

Each comes with what makes it read as real. The sources cover the shows. The camera and lighting notes are researcher synthesis unless tagged.

1. **US public-access cable, 1985–95** (Wayne's World was a satire of it). Folding table, a bedsheet or carpet backdrop, one or two fixed tripod camcorders, an overhead fluorescent wash, hand-lettered sign. Real tells: video-camera clipping on the white areas, a slightly soft image, colour bleed on reds (red bleeds on consumer formats). https://www.avclub.com/wayne-s-world-and-the-democratization-of-tv-from-public-1798163524 ; chroma bleed: https://www.digitalfaq.com/forum/video-restore/9303-chroma-bleed-problem.html [opinion]
2. **Parody of public access, shot "badly on purpose"** (Tim and Eric): "never feeling polished or in control", awkward performance, technical mistakes, obsolete tech. https://nofilmschool.com/tim-and-eric-change-tv ; Sconce chapter: https://dhjhkxawhe8q4.cloudfront.net/nyupress-wp/wp-content/uploads/2020/03/31141647/Tim-and-Eric_Sconce_HTWTV.pdf [opinion]
3. **Pirate signal intrusion** (Max Headroom hijack, Chicago, 1987-11-22). A masked figure in front of a swivelling corrugated-metal sheet, one harsh lamp, distorted audio, unstable picture. This is the closest real precedent for a masked anonymous presenter. https://en.wikipedia.org/wiki/Max_Headroom_signal_hijacking [opinion, well-documented]
4. **Tacky regional "luxury" chat show** (the Knowing Me Knowing You parody of a "top international hotel" set): sofa, chair and table centre stage, a fountain, foliage, a hot tub. Over-dressed, cheap aspiration. https://partridge.fandom.com/wiki/Knowing_Me,_Knowing_You [opinion]
5. **1990s broadcast studio on Betacam SP** (the industry standard to the late '90s): cleaner colour than consumer tape, but interlace combing on motion, highlight clipping, and comet-tail smear behind bright lights on CCD and tube cameras. https://en.wikipedia.org/wiki/Betacam ; https://forum.videohelp.com/showthread.php?p=2328387 [opinion]
6. **Living-room set**: chairs, bookshelves, a fake window. A common cheap format. https://www.newscaststudio.com/2008/02/28/83 [opinion]
7. **Dated 1970s den**: dark wood panelling and bad wallpaper. https://www.pajiba.com/tv_reviews/ranking-the-athome-backdrops-of-all-the-latenight-hosts.php [opinion]
8. **DIY "cardboard and duct tape" set**, chosen to look cheap. https://www.dvinfo.net/forum/open-dv-discussion/14391-extra-extra-no-budget-set-design.html [opinion]
9. **Small Latin American cable or community channel** (Paraguay has many small local channels: Trece, Unicanal, TV Chaqueña…). No visual source was found for their studio look, so don't assert one. https://en.wikipedia.com/wiki/Television_in_Paraguay [gap]
10. **Disposable-camera flash still** (Google's own example of a "raw, nostalgic flash" register): a behind-the-scenes snapshot look rather than a broadcast frame. [official] Cloud guide.

## 6. Making the still a good Omni Flash start frame

- Flow help: in Frames mode, describe the **action or transition** and do not re-describe the frame. "Your text prompt should complement, not contradict, your visual inputs." For ingredients, use subjects on a plain or segmented background. Voice references work only with Ingredients. [official] https://support.google.com/flow/answer/16353334
- DeepMind's prompt guide: decide wide, medium or close first; use "static / locked off" for a stable camera; ask for "one continuous shot" or a "oner". Extensions run in 10 s steps up to 40 s. [official, undated] https://deepmind.google/models/gemini-omni/prompt-guide/
- The model keeps what the source image already contains (subject, framing, style), so frame the still as the shot you want. Clear, high-quality stills give better consistency. [opinion, API vendors] https://www.eachlabs.ai/google/gemini-omni-flash/google-gemini-omni-1-1-flash-image-to-video
- Without "single continuous shot", Omni may invent a multi-shot mini-edit. Describe the audio, or it may add music. Undefined on-screen text gets invented. Keep tracked subjects to three or fewer. Make one change per turn: drift builds after about 4 edits. [opinion, guide, Omni 1.1 Aug 2026] https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide
- Not sourced, researcher's craft suggestions: leave headroom and space around the gloved hands so gestures don't leave the frame; keep the wine glass and hands fully in frame and unoccluded; give the head enough pixels for the triangle to survive motion; avoid heavy grain or blur in the still, which video models tend to "clean up" or animate as boiling. [opinion, unverified]
