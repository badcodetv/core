# Your one brief

You are writing one prompt for one still image, for Google Nano Banana 2. Read only this file. Do not open any other
file in this repository, and do not search it. Do not use the web. Nobody will edit what you write: it runs verbatim.

## What the director asked for

"Please clean room everything only research the internet for varying realsitic cinematic styles that will fit this."

## The film

A dark British comedy with South Park's skit-after-skit comic logic, shot as realistic live-action-looking cinema.
Brandon, 22, is a lonely idiot in a small English town who follows online gurus and keeps hurting himself. His only
friend is Gary, a tired man of about fifty, who is secretly being paid to get close to him.

## The moment to draw

A cheap gym. Brandon lies on a bench press under a heavy barbell, looking up at Gary, completely trusting. Gary stands
over him at the head of the bench, hands under the bar, spotting him. Nothing has gone wrong yet. Both are clearly seen.

## The style you are writing for

Commit to this style fully, including how it dresses and casts the two men. It is one of ten, and each writer gets a
different one.

## 2. Kitchen Sink Monochrome

**Family:** British New Wave, 1960-61.

**References**
- Saturday Night and Sunday Morning (1960, Karel Reisz; Freddie Francis), shot largely on location in Nottingham.
- A Taste of Honey (1961, Tony Richardson; Walter Lassally), shot on location in Salford, Manchester and Blackpool.

**Physical look**
- **Format:** black and white, both films being catalogued as such. Grain, lens choices and the shape of the frame are **[unverified]**.
- **Framing:** real streets with the town behind the person. My proposal is wider shots than modern drama, so the town's rooflines and terraces sit over Brandon's head.
- **Light:** my proposal is overcast daylight outside and hard practical lamps inside.
- **Bodies:** ordinary faces, with young leads who look like they work for a living.
- **This film:** phones, the app and the data centre appear in a look that belongs to 1960. The anachronism is left unexplained.

**Why funnier or more frightening:** it gives a protein-shake idiot the dignity of an angry young man. The form promises a working-class hero who sees through everything, and Brandon sees through nothing. Screens glowing in monochrome also look properly alien.

**Honest risk:** it can read as a pastiche, or a film-school joke, within a minute. Black and white may also make the water and data centre argument feel historical when it needs to feel current. The audience may hold it at a respectful distance.

**Characters**
- **Brandon:** big ears, bad haircut, a tracksuit top zipped to the neck, like a boy in his dad's idea of smart.
- **Gary:** heavy brow, broken nose, donkey jacket over gym kit.
- **Giles:** smooth and pink-looking even in grey, a quilted gilet worn like a county squire's.

**Sources:**
[Saturday Night and Sunday Morning, Wikipedia](https://en.wikipedia.org/wiki/Saturday_Night_and_Sunday_Morning_(film)) ·
[A Taste of Honey, Wikipedia](https://en.wikipedia.org/wiki/A_Taste_of_Honey_(film))

## What the research says about the engine

# Nano Banana 2: photographic stills of ordinary people and places

Clean-room web research, 2026-11-01. No repo files read. Six web searches, plus page fetches.

**Grades**
- **[G]** official Google source
- **[T]** practitioner test with visible evidence
- **[A]** anecdote: a vendor guide or tutorial with no controls
- **[I]** my inference, not a finding

**How far to trust this**
- No source tests our subject (unhealthy, tired, plain people in bland rooms). The nearest evidence is one 64-year-old portrait and one messy bedroom.
- No controlled test of film stock, camera names, prompt length or imperfection wording on this model turned up. Those claims rest on Google's advice and vendor guides.
- Pages were read through a summarising fetch tool, so check any quote against the page before relying on its exact words.
- Not fully read: the last 20% of the getimg test (its fast-drafts section and verdict) and the last 14% of the DeepMind page. The Artlist guide refused the fetch (403) and was not read.

## Which model

| Claim | Grade | Source |
| --- | --- | --- |
| Nano Banana 2 is Gemini 3.1 Flash Image, released 2026-02-26, "the new default image generation model in Flow, available to all Flow users for zero credits" | G | [Google launch post, 2026-02-26](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) |
| **A newer model exists: Nano Banana 2.1** (`gemini-nano-banana-2.1`). The API docs say all new projects should use it | G | [Gemini API docs, read 2026-11-01](https://ai.google.dev/gemini-api/docs/image-generation) |
| 2.1 released 2026-10-06 as GA, with better visual quality, prompt adherence, multi-turn character consistency and text | Secondary report citing Google docs; primary page not opened | [Let's Data Science](https://letsdatascience.com/news/google-rolls-out-nano-banana-21-image-model-c6ac3b89) |
| 2.1 gains "subject consistency" and more natural-looking images | G (undated, marketing page) | [DeepMind 2.1 page](https://deepmind.google/models/gemini-image/flash/) |
| Nano Banana 2 Lite (2026-06-30) is built for speed and volume, and is "not optimized for multiple reference inputs" | G | [Google, 2026-06-30](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/), API docs above |

**Unverified: is 2.1 in Flow?** The DeepMind page offers it in Gemini and doesn't mention Flow, and I found no source saying it is there. An undated [Flow help page](https://support.google.com/flow/answer/16353334) says Flow defaults to Nano Banana Pro, which contradicts the launch post. **Look at the Flow model picker.** If 2.1 is there, test it against 2.

## The visible tells

Most of these come from the getimg test below, which covers models in general rather than this subject.

- **Smooth, young skin when age is asked for.** Models "betray a bias toward smooth, young skin". Waxy or plastic skin is worst on base Nano Banana. [T: getimg]
- **Hands and small objects** are "the classic failure mode". The newer models broke no hands in the flash test. [T: getimg]
- **Book spines and small print come out garbled.** Odd spines are "the single most common failure across the field", which matters for any lived-in room. [T: getimg] Google also warns that small text and fine details can fall short. [G: Nov 2025, predates Nano Banana 2]
- **Unrequested extras:** stray elements and added slogans. [T: getimg]
- **Over-etched, frozen eyebrows; oversaturated, CGI-like finish.** Seen in some other models, not specifically this one. [T: getimg]
- **The default polish:** vague prompts give "Clean skin, flattering light, perfectly symmetrical face". [A: Fliki]
- **Staged rooms.** getimg praises Nano Banana 2 for the "most un-staged" mess, which implies staging is the usual failure. [I]
- **Google sells the model on "vibrant lighting, richer textures and sharper details".** [G] For a bland office that is the wrong direction, so expect to have to pull it down. [I, untested]
- **Other likely tells, from my own judgement with no source:** everyone centred and facing the lens, even all-over light with no visible source, new clothes with no wear, tidy surfaces, and characters who are too good-looking for the brief. [I]

## Best evidence on realism

[getimg realism test](https://getimg.ai/blog/ai-realism-test-comparing-realistic-image-generation-models), published 2026-08-21, updated Oct 2026 to 25 models. **[T], with limits:** one generation per model per prompt, judged by the author, and getimg sells access to these models.

- Same prompts for every model, with prompt enhancement off. Nano Banana 2 and GPT Image 2.5 Flare were the only models rated Top on every prompt.
- Nano Banana 2.1 is "close behind" overall. It dropped to Strong on product and text but was **Top on all the people and room prompts**.
- **Aged portrait:** Nano Banana 2 gave "real age spots and pigmentation", and the man "reads as a real 60-year-old". 2.1 gave coarse beard hairs and natural ageing.
- **Flash street scene:** 2.1 "produced the most authentic snapshots, with real disposable-camera flash". Nano Banana 2 was "a little less gritty".
- **Messy room:** Nano Banana 2 was the "most convincingly un-staged". 2.1 took the "narrow, imperfect room" most literally.
- Nano Banana Pro rated lower on all of these (Strong or Fair). This is evidence against reaching for Pro on this subject. Base Nano Banana was among the weak.
- The prompts that worked named specifics: "natural pores, peach fuzz, tiny freckles and realistic skin variation"; "around 64"; "Flash photograph of four friends leaving a tiny underground club"; "narrow 1970s Mediterranean villa bedroom". They also carry glamour words ("fashion", "editorial", "charismatic"), so results on deliberately plain people may be worse. [I]

**Conflict resolved:** a search summary said this test rated Nano Banana 2 weak on skin. The page itself rates it Top and contains no such statement. Trust the page. Vendor praise elsewhere ("visible pores", "less plastic smoothing": [getimg review, 2026-02-27](https://getimg.ai/blog/nano-banana-2-review-whats-new-and-is-it-better)) has no method behind it, **[A]**.

## What works in the wording

**Structure and length**
- Write sentences that describe a scene, not keywords. "Describe the scene, don't just list keywords." [G: [API docs, updated 2026-10-26](https://ai.google.dev/gemini-api/docs/generate-content/image-generation); [Cloud guide, 2026-03-06](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana), which covers Nano Banana 2]
- Google's formula: Subject + Action + Location/context + Composition + Style. [G: Cloud guide]
- Google's photo template: "A photorealistic [type of shot] of a [subject description] in a [setting description]. [Description of the light]. Shot from a [camera angle] with a [lens type]." [G: API docs]
- "The more detail you provide, the more control you have." State what the image is for, and break complex scenes into steps. [G: API docs]
- Put the subject in the first 15 words. Don't target a length. [A: [Fliki, updated 2026-09-29](https://fliki.ai/blog/nano-banana-2-prompting-guide)] One guide in the search results caps adjectives at five, without evidence; I didn't open or identify it. **Length is untested.** Detail is advised, but concrete nouns and adjective pile-ups are probably different things. [I]

**Camera and film**
- Google endorses naming kit: "a Fujifilm camera for authentic color science, or a cheap disposable camera for a raw, nostalgic flash aesthetic", and "as if on 1980s color film, slightly grainy". [G: Cloud guide] The disposable-camera line is the closest official fit for us, and the flash test above supports it. [T, weakly]
- Use angle and lens language: "low-angle shot", "wide-angle lens", an f-stop. [G]
- One camera phrase per prompt: "Two different camera bodies in the same sentence will confuse the model". Portra 400 is a common suggestion. [A: Fliki; no test]
- **Unverified:** whether a named camera or stock does more than a plain description of grain and colour. I found no side-by-side test.

**Light**
- "Tell the model exactly how the scene is illuminated." [G: Cloud guide] Its examples are glamour setups (softbox, golden hour, chiaroscuro), and none cover ordinary rooms.
- Naming the actual source is the obvious extension: one overhead strip light, a skylight, a phone screen. getimg's Top portraits followed "window light on one side of the face", which is thin support. [T, weakly] The strip-light and skylight wording is [I].

**Materials and imperfections**
- Define what things are made of: not a suit jacket, but "navy blue tweed". [G: Cloud guide] This works for cheap materials too. [I]
- Name skin detail specifically. "Visible skin pores" and "retain pores" are recommended by [Morphed](https://morphed.app/blog/nano-banana-prompts) and [CyberLink](https://www.cyberlink.com/blog/ai-prompts/5176/best-nano-banana-prompts). [A: seen in search results only, not opened] getimg's specific skin wording did produce its best results. [T, weakly]
- "'Realistic' is a feeling, not an instruction." [A: Fliki]
- Imperfection wording (wear, stains, clutter, spots) has **no direct test**. The un-staged room and age-spot results suggest the model can do it when asked. [I]

**Iterating**
- "Don't expect a perfect image on the first try." Refine with follow-ups, and "be explicit about what to keep exactly the same". [G]
- "If it did not work after two tries, the prompt was the problem." [A: Fliki]

## What doesn't work or backfires

- **Keyword lists.** [G] Fliki's claim that they lose "60%" of quality has no stated basis. [A]
- **Listing what you don't want.** Google says to use positive framing: "empty street" instead of "no cars". [G] So describe worn skin rather than writing "no plastic skin". Practitioners still use negative lists such as "over-smoothing, plastic skin" ([Charlie Hills, 2025-10-26](https://charliehills.substack.com/p/how-to-prompt-nano-banana-pt2), original Nano Banana, predates the current model), with no comparison behind them. [A]
- **Contradictory styles or stacked cameras:** these give "a smeared hybrid". [A: Fliki]
- **Asking for small legible text in the background** (spines, posters). [T, G] Keep it out of frame or out of focus. [I]
- **"Hyperrealistic", "8K", "ultra-detailed":** I found **no test either way**. They are everywhere in sample prompts, and Google's own 2.1 page uses "hyper-realistic" in a macro example. The idea that they make images look more AI-made is plausible but unproven. Drop them because they describe no visible thing, and treat that as judgement, not a finding. [I]
- **"Cinematic" as a bare word:** Google uses it ("cinematic lighting effect") in a fashion example. No evidence on what it does to plain subjects. Say what makes it cinematic instead: framing, source, depth. [I]
- **Google's guides are not about our subject.** Their examples are fashion, products and golden hour, so copying their style phrases may pull towards gloss. [I]

## Keeping a character consistent

**Official [G]**
- "Include previously generated images in subsequent prompts to maintain consistency." [API docs]
- With references: [Reference images] + [Relationship instruction] + [New scenario]. [Cloud guide]
- Define each image's role: "Use Image A for the character's pose, Image B for the art style…" [[Google tips, 2025-11-20](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/), written for Pro, predates Nano Banana 2]
- Limits: up to 5 characters and 14 references in total, of which up to 10 are objects, for 2 and 2.1 [API docs]. The launch post says 5 characters and 14 objects. A secondary report says four characters for 2.1, which may be a mix-up with Lite. Stay under four and this doesn't matter.
- Google's caveat: "consistency across edits may vary". [Nov 2025, predates Nano Banana 2]
- 2.1's main claimed gain is here: subject and multi-turn consistency. Unmeasured beyond one test below.
- Multi-turn conversation is the recommended way to iterate. **Unverified whether Flow exposes this.**

**Practitioner**
- **"Describe what changes, not who."** Let the reference carry identity and say "the same woman". "Identity lives in the face and hair, not the clothing." A reference "only carries what it shows", so add views for backs and profiles, and use a sharp, unobstructed one. [A, with example images: [Runware docs, NB2 page dated 2026-02-26](https://runware.ai/docs/models/google-nano-banana-2/guides/character-consistency)]
- Single-generation reference test: Nano Banana 2 kept "curls, freckles, green eyes, and jaw" while rebuilding the scene, and 2.1 stayed "unmistakably the same person". Weaker models straightened the hair. [T: getimg]
- Logos and exact accessories still drift. Identical prompts can still vary in style and tone. [A: search results, sources not opened]
- Claimed plateau at about 6 references, degrading past 10. [A: one guide, no method; not opened]
- **Do not use:** "95%+ consistency", "DeepMind benchmark", "MIT study on 78% identity drift". These appear on vendor pages, and I couldn't trace them to a primary source. [Unverified]

**Inference, untested [I]**
- Make the reference plain too. A polished master portrait may carry its polish into every shot.
- Lock worn clothes with their own reference, since clothing isn't what the model holds.
- Generate each shot from one master reference rather than chaining from the last output, which may drift. This goes further than Google's advice and hasn't been tested.
- I found nothing on Flow's own Ingredients or Characters behaviour. Everything here comes from the API or other hosts.

## Cheap tests that would settle the gaps

Run one subject, several takes per arm, since single takes vary.

1. Nano Banana 2 vs 2.1, if 2.1 is in Flow.
2. Named camera or stock vs plain description of grain and colour vs neither.
3. Disposable or phone flash vs a named room light.
4. Short prompt vs long concrete prompt.
5. "Hyperrealistic, 8K" added vs left out.
6. Worn-skin wording vs "no plastic skin".


## Rules

- Write about what is visible. Full sentences, specific nouns, the actual light sources. No readable text, signs or logos.
- Invented people only. Do not name any real film, director, cinematographer, actor or photographer in the prompt.
- Keep it realistic: this has to look photographed.
- End the prompt with the word "Thanks."

## Output

Write one JSON file to /home/jackt/projects/badcode/badcode/docs/stories/stupidity-optimised/style/cleanroom/prompt-02.json with exactly {"aspect": "<one of 4:3, 16:9, 21:9, 1:1, 3:2>", "prompt": "<the prompt>"}.
Reply only with the path.
