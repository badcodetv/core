# Consistency — characters, references, continuity

Keeping the same person, object and place across many generations. This is the hardest
part of Flow and the one where discipline beats cleverness.

## 1. The two mechanisms

| Mechanism | What it is | Use when |
| --- | --- | --- |
| **Characters** (`@Name`) | A saved entity — face/body reference set, voice, personality — reusable across prompts without re-uploading | A recurring lead across many shots |
| **Ingredients** | Reference images attached per generation (character / object / location-or-style), cap ~3 | A one-off composition, or a scene needing a specific prop and setting |

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
See `docs/superpowers/flow-selectors.md`.

## 6. Drift is a probability, not a bug

Reference images **reduce** visible drift; they do not guarantee an identical character.
Budget rerolls and manual QA on any hero character shot.

Review in a hierarchy: silhouette at thumbnail size → face geometry → material and
texture detail → behaviour. Reviewers should be checking collars, coat texture, eye
spacing and apparent age, not just "is it the same face".

## 7. Continuity across clips

**Extend** — continues the same action, generating from the **final second** of the
previous clip.

- Pick an end frame with a readable silhouette, planted feet, no fast camera move.
- Change **one** thing per extension. Never location + performance + camera at once.
- **Never chain off an unreviewed clip.** Every accepted continuation becomes the source
  evidence for the next, so a small error compounds fast. If drift appears, roll back to
  the last approved clip — a later extension will not repair it.

**Jump To** — moves a character or object to a **completely new setting** while
preserving appearance from the previous shot. This is the cut; Extend is the continuous
take.

**Frame-to-frame chaining** — the community workaround, and the more controllable
option. When a clip finishes, save its final frame as an asset, then start the next clip
with Frames to Video using that frame as the start. Re-state character, outfit,
background, lighting and sound in every new prompt or it drifts. Flow exports the stacked
clips as one continuous download.

Carry audio across the cut deliberately — crossfading "from loud roar of the water to
wind whistling" sells continuity as much as picture does.

## 8. Locations are references too

Generate one clean plate of the setting, save it, and re-cite it **by name** ("the office
setting") in every subsequent prompt instead of re-describing the room. Same mechanism
and same discipline as characters.

*(BadCode: this is exactly the "golden reference" rule already in our prompt ledgers for
objects and places that have no face for a Character to bind — the bench, the tree, the
coin.)*
