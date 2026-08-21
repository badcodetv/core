# Consistency — characters, references, continuity

Keeping the same person, object and place across many generations. This is the hardest
part of Flow and the one where discipline beats cleverness.

## 1. The mechanisms — there are four, not two

Corrected 2026-08-18 against Flow's own help pages. These are **separate modes selected from
the compose bar's model menu**, not variations on one idea, and picking the wrong one is why a
reference sometimes appears to do nothing.

| Mechanism | Where | What it is | Use when |
| --- | --- | --- | --- |
| **Characters** (`@Name`) | type `@` in the prompt box | A saved entity — face/body reference set, voice, personality — reusable across prompts without re-uploading. `@me` inserts your own avatar. | A recurring lead across many shots |
| **Ingredients** | model menu → **Video Ingredients** | Reference images attached per generation (character / object / location-or-style), cap 3 | A one-off composition, or a scene needing a specific prop and setting |
| **Frames** | model menu → **Video Frames** | A start image and/or an end image the clip must begin and end on | You have already art-directed the endpoints |
| **Voices** | model menu → Omni Flash → **Add Voices** | A named voice (`@Voice: Andrew`) or a custom one built from a preset plus a "Voice Performance" description | Never, for us — our audio is Suno's |

🔴 **Ingredients cost you the Quality tier and the short durations.** Google's feature matrix
marks Ingredients/References → Video as **not supported on Veo 3.1 Quality**, and **8s only**
on Lite and Fast. So any shot with a cast character is a Fast shot at 8 seconds — there is no
Quality hero take of a character, and no 4s character beat. Plan for it; don't discover it.
See [`platform-controls.md`](./platform-controls.md) §1.

**Voice references only work on generations that already use ingredients** — Google's help says
any other kind of generation returns an error.

**On the API side** (not Flow) the same idea is narrower and worth knowing as the model's
actual contract: *"Provide up to three asset images of a single person, character, or
product. Veo preserves the subject's appearance in the output video."* Reference images are a
**subject-identity** mechanism first. Using them to carry a location or a grade is us borrowing
the slot, and it is the weaker use.

Building a Character: Characters tab → upload or generate images → name → optional voice
→ Done. **Two views minimum** is best practice: a detailed headshot for face and
expression, plus a full-body shot naming outfit specifics ("dark navy sweater and cargo
pants"). Reference inline as `@CaptainZoro walking through a futuristic city`. `@` also
pulls any saved asset into a prompt.

Google claims face, clothing and voice "remain strictly consistent across multiple
generations". Treat that as the intent, not a guarantee — see §6.

**BadCode note.** Our `flow_create_character` tool runs this whole flow in one call,
including the native Create Body pass. And per our own hard-won lesson: **the Character
Name field is policy-scanned**, so a Character named after a real person will have every
generation refused regardless of prompt text. See [`failure-modes.md`](./failure-modes.md).

⚠️ **There is no seed lever on 3.1.** Google scopes the parameter explicitly — *"Note that the
seed parameter is also available for **Veo 3** models. It doesn't guarantee determinism, but
slightly improves it."* Every fixed-seed reproducibility workflow being sold for Veo 3.1 is
folklore, and one of the guides selling it admits on the same page that the 3.1 upgrade shifted
noise schedules and invalidated old seeds. **Do not plan cross-shot consistency around it.**
(official, [ai.google.dev](https://ai.google.dev/gemini-api/docs/veo))

## 2. Reference-image hygiene — the highest-leverage discipline

This is the shared root cause of **identity drift** *and* **style bleed**. Google names
neither failure; the fix is the same for both.

- **One element per image, plain or segmented background.** A tight clean cut-out beats
  a gorgeous crowded photo. Location and style references must not contain extra
  subjects unless you mean them.
- **Consistent look and feel across the whole ingredient set.** A subject shot in flat
  studio light dropped into a moody night plate looks pasted on. Either choose
  references whose lighting and angle already agree, or explicitly prompt the lighting so
  the model re-lights the subject.
- **Curate by function, not preference.** Neutral front views are the best identity
  anchors. Dramatic cinematic reference images hide anatomy and make *worse* anchors —
  the beautiful shot is usually the wrong reference.
- **Your text prompt must complement, never contradict, the visual inputs.**

**Two drift triggers beyond reference hygiene**, and one of them bites us specifically:

- *"**Avoid Extreme Angles.** Extreme angles like bird's-eye or worm's-eye views make it
  difficult for the AI to recognize facial features, causing subsequent shots to lose accuracy."*
- *"**Maintain Consistent Lighting.** Sudden lighting changes affect the AI's character
  recognition… If you must change scenes, try to keep lighting conditions similar or use
  transition shots as buffers."*

🔴 Single source, personal anecdote, no A/B — **a hypothesis to try, not settled fact.** But the
BadCode register uses worm's-eye and bird's-eye deliberately, so if it is true we have a standing
conflict between the look and the consistency discipline, and only our own multi-shot chain can
settle it. (single-source,
[eastondev.com](https://eastondev.com/blog/en/posts/ai/20251207-veo3-character-consistency-guide/))

## 3. Naming reference roles in the prompt

Past two references the model will not infer which image supplies what. Two attested
patterns:

> **Official (preamble form):** "Using the provided images for the detective, the woman,
> and the office setting, create a medium shot of the detective behind his desk."
> **Same references reused for the reply shot:** "Using the provided images for the
> detective, the woman, and the office setting, create a shot focusing on the woman."

> **Numbered form:** "The woman from reference image 1, holding the coffee cup from
> reference image 2, walking through the rainy neon street from reference image 3."
> **Template:** "The [element] from reference image [#], [action], [camera move],
> [mood/lighting]."
> **Style transfer:** "The subject from image 1 rendered in the painterly visual style of
> image 2."
> **Ingredient-as-subject (official):** "The woman, whose torso is the lava lamp, walks
> down the foggy street."

**Order matters** — the model treats earlier images as higher priority when elements
compete. Put the character first.

The canonical three-slot pattern is **Subject/Character** (locks identity) +
**Environment/Setting** (locks the world) + **Style/Texture** (sets the grade). Don't
fill three slots with three competing subjects.

**You do not have to fill all three slots.** *"Two strong, distinct images often beat three
competing ones."* / *"Three references that each fight for the lead role produce mush. Often two
strong, complementary ingredients — one subject, one scene — give a cleaner result."*
(practitioner, [veo3ai.io](https://www.veo3ai.io/blog/veo-3-1-ingredients-to-video-guide-2026))

**The role-naming pattern converges across model families**, which is why it is craft and not a
Flow quirk — MiniMax/Hailuo H3 guidance is *"Image 1 for mood, Image 2 for the talent, Image 3
for the product"*, the same shape as Flow's Subject/Environment/Style and OpenAI's labelled
Dialogue block. (practitioner, unverified this pass,
[inreels.ai](https://www.inreels.ai/blog/minimax-h3-prompt-guide))

## 4. Character DNA — the copy-paste block

Document each character once and paste the block **verbatim, unchanged** into every
prompt: age, face shape, hair colour and style, skin tone, notable features, primary
outfit plus alternates, textures and colours.

> "John, a man in his 40s with short brown hair, wearing a blue jacket and glasses,
> looking thoughtful"
> "Mei, 30s, shoulder-length black hair, round glasses, mustard cardigan."

Do the same for the scene — environment, lighting, palette, lens, camera motion,
weather, time of day — repeated per prompt to prevent slow colour creep across a
sequence.

**And select the exact same ingredient image for the character in every prompt.**
Google states this explicitly.

*(This is what a `docs/stories/<story>/characters/*.md` file is for. The canon file is
the DNA block; copy it, don't paraphrase it.)*

🔴 **State skin tone and ethnicity explicitly, in the block, every time.** Google's own Veo 3
model card records that *"Veo 3 appears to skew towards lighter skin tones when race is not
specified in the prompt"*, alongside *"risks of semantic bias where particular terms are
spuriously correlated with representation of particular demographics."* **Omission is not
neutrality** — it is a documented pull in one direction, and it is what a fresh generation
regresses toward when the reference stops holding. (official,
[Veo 3 model card](https://storage.googleapis.com/deepmind-media/Model-Cards/Veo-3-Model-Card.pdf))

**The per-view identity-lock phrase family** practitioners use, varying slightly by angle while
treating clothing and environment as the deliberately variable axis: *"preserve facial identity"*
/ *"keep identity"* (front) / *"preserving exact identity"* (side profile) / *"preserve identity
cues"* (back). The fuller front-view form is *"Keep identity, facial structure, and realistic
skin texture consistent"*. (corroborated — eleven shown images across profiles, wardrobe variants
and environments, [rundiffusion.com](https://www.rundiffusion.com/nano-banana-2-consistent-character-images))

### More than one character in one reference

Nothing here previously covered holding a **group** consistent at once. The attested template
fixes attire plus identity for the whole group and leaves expression and angle free per
character:

> *"Keep the person's facial features exactly the same as Image 1."*
> *"Keep the attire and identity consistent for all 3 characters, but their expressions and
> angles should vary throughout."*

*(corroborated, authored by Google's own Gemini developer advocate with example images shown,
[dev.to/googleai](https://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n))*

## 5. Multi-angle character sheets

For hard shots, generate a **character sheet** first — one image containing a direct
frontal view, a 45° three-quarter and a 90° profile, plus a back view if wardrobe
matters — and feed all views together as one reference set, paired with the short
written identity anchor. Expect roughly 80% consistency on first try even with a good
sheet; plan one reroll.

⚠️ **We have tried and failed at this.** Asking Flow to composite a multi-view turnaround
from one portrait in a single `flow_edit_image` call produces *nothing* — no candidate
ever lands. What works instead is **Portrait + native "Create Body"**, two separate
single-subject generations. The untested fallback for deeper angle coverage is N separate
single-image generations fed together into `flow_create_character`'s `refImages` array.
See `docs/flow/automation-images.md`.

**Build the whole reference library up front, in one structured batch, before any production
shot** — *"Profile documentation (front, side, back views)"* → *"Professional wardrobe
variants"* → *"Environmental stock scenes"* — rather than generating references reactively as
drift appears. This reframes our one-off character sheet as **pre-production**. (corroborated —
images shown for all three phases,
[rundiffusion.com](https://www.rundiffusion.com/nano-banana-2-consistent-character-images))

**A concrete turnaround grid to try on top of Portrait + Create Body** — *"two rows, four
full-body standing views on top (front, left profile, right profile, back) and three close-up
portraits underneath"*. Harmless if it does not pan out; our single-call composite attempt
failed, so treat this as a layout to test, not a fix. (content-mill,
[freeaivideohub.com](https://www.freeaivideohub.com/character-sheets))

## 6. Drift is a probability, not a bug

Reference images **reduce** visible drift; they do not guarantee an identical character.
Budget rerolls and manual QA on any hero character shot.

Review in a hierarchy: silhouette at thumbnail size → face geometry → material and
texture detail → behaviour. Reviewers should be checking collars, coat texture, eye
spacing and apparent age, not just "is it the same face".

**Google says the ceiling is real, not a technique gap.** The Gemini 3 Pro Image model card
states plainly that *"character consistency is not always perfect between input images and
generated output image"*, and the Veo 3 model card — explicitly scoped to cover *"Veo 3 and
subsequent versions"* — says *"While Veo 3 demonstrates incredible progress, creating realistic,
dynamic, or intricate videos, maintaining complete consistency throughout complex scenes or those
with complex motion, remains a challenge."* Every discipline in this file is right and still will
not close the gap to zero. **Budget a best-of-N pick on any shot where a face has to match
exactly.** (official, [Gemini 3 Pro Image model card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Image-Model-Card.pdf)
and [Veo 3 model card](https://storage.googleapis.com/deepmind-media/Model-Cards/Veo-3-Model-Card.pdf))

## 7. Continuity across clips

**Extend** — *"finalizes the final second or 24 frames of your video and continues the
action"* (Google's wording). It sees **only that last second**; everything earlier in the clip
is invisible to the continuation.

⚠️ **Extending forecloses repair.** *"You can't apply other edit modes such as insert, remove,
and camera to extended video clips."* Fix the prop, then extend — never the other way round.

⚠️ **Extend runs at Veo 3.1 Lite whatever tier the source was.** A Quality clip continued by
Extend continues at Lite. This is why BadCode cuts every 8 seconds instead.

- Pick an end frame with a readable silhouette, planted feet, no fast camera move.
- Change **one** thing per extension. Never location + performance + camera at once.
- **Never chain off an unreviewed clip.** Every accepted continuation becomes the source
  evidence for the next, so a small error compounds fast. If drift appears, roll back to
  the last approved clip — a later extension will not repair it.

**Compare with Sora, because the difference explains our discipline.** OpenAI's own cookbook:
*"The model uses the full original clip as context, which helps maintain scene continuity."*
Veo sees only the final second. **Sora has a structural safety net; we do not** — which is
exactly why every continuation has to restate character, outfit, background, lighting and sound
in full, and why a Sora-derived intuition about extension will mislead here. (first-party OpenAI
documentation, [developers.openai.com](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide))

**Jump To** — moves a character or object to a **completely new setting** while
preserving appearance from the previous shot. This is the cut; Extend is the continuous
take.

**Frame-to-frame chaining** — documented by Google, not just a community workaround, and the
more controllable option. When a clip finishes, save its final frame as an asset (pause on the
frame → hover → **Save frame**; or `flow_scene_save_frame`, which will park the playhead at the
end for you), then start the next clip
with Frames to Video using that frame as the start. Re-state character, outfit,
background, lighting and sound in every new prompt or it drifts. Flow exports the stacked
clips as one continuous download.

**A carried-forward clause for the cut point**, packaging both disciplines into one line:

> *"Continue from the previous scene with the same character, same outfit, same hairstyle, same
> face, same body proportions, same color palette, same art style, and same lighting direction.
> The character now [new action]."*

*(practitioner, template only, [bigprompthub.com](https://www.bigprompthub.com/character-consistency-video-prompt/))*

Carry audio across the cut deliberately — crossfading "from loud roar of the water to
wind whistling" sells continuity as much as picture does.

## 8. Locations are references too

Generate one clean plate of the setting, save it, and re-cite it **by name** ("the office
setting") in every subsequent prompt instead of re-describing the room. Same mechanism
and same discipline as characters.

*(BadCode: this is exactly the "golden reference" rule already in our prompt ledgers for
objects and places that have no face for a Character to bind — the bench, the tree, the
coin.)*

**And textures are a reusable ingredient class too, in Google's own words** — *"Control the
scene by maintaining the integrity of your setting and the objects within it. You can also reuse
an object, backgrounds **or textures** across scenes."* / *"Combine disparate elements — like
characters, objects, textures and stylized backgrounds — into a cohesive, high-impact clip."*
(official, [blog.google](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/))

## 9. Compositing into live footage

Veo has a named **"add object"** capability distinct from Ingredients casting: supply the
live-action clip, a text prompt describing the addition, and a defined region, and it composites
generated content in while holding the rest of the frame consistent. Google's ANCESTRA account
describes giving Veo *"the live-action footage, a text prompt describing the scene, and a defined
area for adding the baby,"* *"keeping everything else consistent."* Used in the finished film.

Absent from every prompting guide and, until now, from this file. Untested by us and unknown
whether it is reachable from the Flow app. (official,
[blog.google](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/ancestra-behind-the-scenes/))

---

## Sources

Re-checked at source **2026-08-18**.

- [Create videos in Google Flow](https://support.google.com/labs/answer/16353334?hl=en) — characters (`@Name`, `@me`), Video Ingredients, Video Frames, voice references, and the ingredient-hygiene best practices quoted in §2 ("provide subject or product references on a plain or segmented background"; "make sure location and style references don't contain extra subjects"; "your text prompt should complement, not contradict, your visual inputs"; "a consistent look and feel across all your ingredient images helps the model blend them more effectively").
- [Edit videos & build scenes in Google Flow](https://support.google.com/labs/answer/16935718?hl=en) — Extend, Save frame, the History panel, Scenebuilder.
- [Learn about Google Flow models & supported features](https://support.google.com/labs/answer/16352836?hl=en) — the Quality/ingredients exclusion and the 8s constraint in §1.
- [Generate videos with Veo 3.1 — Gemini API](https://ai.google.dev/gemini-api/docs/veo) — reference images as a subject-identity mechanism ("up to three asset images of a single person, character, or product"), Extend semantics, first/last frame.
- [Image generation with Gemini](https://ai.google.dev/gemini-api/docs/image-generation) — the iterative 360-view character technique behind §5, and per-model reference caps (see [`image-prompting.md`](./image-prompting.md) §9).

§2's discipline is **Google's own published best practice**, not folklore — which is worth
knowing, because it is also the single highest-leverage habit in this file and the easiest to
skip when a gorgeous crowded reference is right there.

**Added by the 2026-08-20 ten-angle sweep:**

- [Veo 3 model card — DeepMind](https://storage.googleapis.com/deepmind-media/Model-Cards/Veo-3-Model-Card.pdf) · [Gemini 3 Pro Image model card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Image-Model-Card.pdf) — the consistency ceiling in Google's own words, and the documented lighter-skin default. 🔴 **WebFetch cannot read these PDFs; download and Read.**
- [ANCESTRA behind the scenes — blog.google](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/ancestra-behind-the-scenes/) — the "add object" live-footage compositing path (§9).
- [Ingredients to Video — blog.google](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/) — textures as a reusable ingredient class.
- [Sora 2 prompting guide — OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) — Sora extends with the full clip as context; Veo sees one second. The contrast is why §7's restate-everything rule is structurally required here.
- Secondary, phrasing only: [rundiffusion.com](https://www.rundiffusion.com/nano-banana-2-consistent-character-images) *(eleven shown images)* · [dev.to/googleai](https://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n) *(Google DevRel, shown examples)* · [veo3ai.io](https://www.veo3ai.io/blog/veo-3-1-ingredients-to-video-guide-2026) · [eastondev.com](https://eastondev.com/blog/en/posts/ai/20251207-veo3-character-consistency-guide/) *(the extreme-angle hypothesis — untested, and it conflicts with our register)*
