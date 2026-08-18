# Video prompting — Veo 3 / 3.1

Text→video, image→video, frames, audio and dialogue. Motion craft for
`animate-slide` and `music-video-short`.

## 1. The formula

`[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]`

Not every element every time — know them so you can add them deliberately. The formula
**constrains the model's improvisation**; it is not a requirement. A one-line prompt is
a legitimate opening move precisely because it shows you what Veo invents by default,
which you then override one clause at a time.

> **Official (all five parts):** "Medium shot, a tired corporate worker, rubbing his
> temples in exhaustion, in front of a bulky 1980s computer in a cluttered office late at
> night. The scene is lit by the harsh fluorescent overhead lights and the green glow of
> the monochrome monitor. Retro aesthetic, shot as if on 1980s color film, slightly
> grainy."

> **Official (camera-led):** "Crane shot starting low on a lone hiker and ascending high
> above, revealing they are standing on the edge of a colossal, mist-filled canyon at
> sunrise, epic fantasy style, awe-inspiring, soft morning light."

> **Official (mood-led):** "Close-up with very shallow depth of field, a young woman's
> face, looking out a bus window at the passing city lights with her reflection faintly
> visible on the glass, inside a bus at night during a rainstorm, melancholic mood with
> cool blue tones, moody, cinematic."

> **Official (pure world-building — no camera, no character direction, still a model
> example):** "A snow-covered plain of iridescent moon-dust under twilight skies.
> Thirty-foot crystalline flowers bloom, refracting light into slow-moving rainbows. A
> fur-cloaked figure walks between these colossal blossoms, leaving the only footprints
> in untouched dust."

## 2. Length — the resolved rule

Sources contradict each other: community guides say 3–6 sentences and that overlong
prompts get partly ignored; DeepMind's own guide showcases a ~1,100-word prompt as a
technique for maximum control.

**Ruling:** *dense and long* is different from *padded and long*. Length costs nothing
when every clause describes one coherent action in a single scene. What gets dropped is
repetition and **competing actions**. Default to 3–6 sentences and one atomic action per
clip; go long only when a single complex action genuinely needs that many distinct facts.

## 3. Image-to-video — the `animate-slide` case

**The rule that matters most: the source image already supplies subject, scene and
style, so describe only the motion.** Do not re-describe the character, the background
or the lighting. Redundant description gives the model competing signal about what the
frame should look like, and it drifts toward regenerating rather than animating.

- **Refer to the subject generically** — "the subject", "the woman", "he".
- **Source-image quality gates everything downstream.** Sharp, one clear subject,
  readable detail, enough negative space for the camera to move into.
- **An unspecified camera is NOT a still camera — corrected 2026-08-18.** This file used to
  say "Veo's default is near-static". That is wrong and it cost us real time. Leave the camera
  unstated and Veo *invents* behaviour — generic framing, a slow drift, a sway, an unrequested
  push-in. **Name the move every time.** When you want no move at all, say so explicitly:
  `static`, `locked-off`, `no camera movement`. Silence is not a request for stillness.
- **Name the subject motion too.** Separately from the camera: an unstated subject can come
  back near-frozen even while the camera is busy.
- **1–2 motion types maximum.** "Slow dolly in, leaves rustling, clouds moving, water
  rippling, light shifting" is five competing instructions.
- Get one axis working (camera *or* subject) before adding the other.
- **Partial animation:** name the moving element and the pinned one in the same
  sentence — "Rotate the shoe, keep everything else still." / "Animate only trees and
  sky; keep buildings static." / "background stays still and in focus".
- **Style lock is the one permitted exception to "don't re-describe":** a short clause
  like "Maintain the style of the image" or "Maintain the old indie film or VHS tape
  aesthetic" anchors treatment without giving the model content to regenerate.
- **Motion intensity is a three-tier vocabulary:** "Very subtle movement, minimal motion,
  nearly still" / leave unspecified / "Energetic movement, dynamic motion throughout".
  If it returns too subtle, add "Visible movement throughout."
- Ambient motion that reads cinematic without moving the subject: "subtle morning mist,
  light rays, otherwise still".
- **Debugging a bad animate: reduce scope.** Lock the subject, cut to one animated
  region, try a different aspect ratio. Adding corrective description makes drift worse.

> **Minimal and valid:** "Make him run!"

## 4. First / last frame (Frames to Video)

Three separate prompts. Each **still** prompt is a complete, self-sufficient scene
description. The **Veo** prompt names only the camera move connecting them, plus any
dialogue spanning the transition.

> **Official (all three):**
> *Start frame:* "Medium shot of a female pop star singing passionately into a vintage
> microphone. She is on a dark stage, lit by a single, dramatic spotlight from the front.
> She has her eyes closed, capturing an emotional moment. Photorealistic, cinematic."
> *End frame:* "POV shot from behind the singer on stage, looking out at a large,
> cheering crowd. The stage lights are bright, creating lens flare. You can see the back
> of the singer's head and shoulders in the foreground. The audience is a sea of lights
> and silhouettes. Energetic atmosphere."
> *Veo prompt:* "The camera performs a smooth 180-degree arc shot, starting with the
> front-facing view of the singer and circling around her to seamlessly end on the POV
> shot from behind her on stage."

**BadCode application: this is the panel-to-panel technique.** Art-direct page N and
page N+1 as clean stills, feed both into Frames mode, and let the video prompt carry
purely the connective camera language. Cheaper and far more controllable than asking
one generation to invent the journey.

## 5. Timestamp prompting — multi-beat inside one generation

Format: `[MM:SS-MM:SS] <shot description>. SFX: … Emotion: …`

> **Official:**
> "[00:00-00:02] Medium shot from behind a young female explorer with a leather satchel
> and messy brown hair in a ponytail, as she pushes aside a large jungle vine to reveal a
> hidden path.
> [00:02-00:04] Reverse shot of the explorer's freckled face, her expression filled with
> awe as she gazes upon ancient, moss-covered ruins in the background. SFX: The rustle of
> dense leaves, distant exotic bird calls.
> [00:04-00:06] Tracking shot following the explorer as she steps into the clearing and
> runs her hand over the intricate carvings on a crumbling stone wall. Emotion: Wonder and
> reverence.
> [00:06-00:08] Wide, high-angle crane shot, revealing the lone explorer standing small in
> the center of the vast, forgotten temple complex, half-swallowed by the jungle."

Use this for reveal → reaction → detail → pull-back inside 8 seconds. Use clip-chaining
([`consistency.md`](./consistency.md) §7) for continuity *across* 8-second windows.

## 6. Audio

**Prompt audio as its own scene layer** — labelled clauses placed after the visual
description:

- `SFX: thunder cracks in the distance`
- `Ambient noise: the quiet hum of a starship bridge`
- `Audio: Crunchy, sugary typing sounds, delighted giggles.`

Rules:

- **One line of dialogue + one primary SFX + one ambient bed.** A crowded soundscape is
  muddier and less controllable.
- **Specify audio even when you want near-silence** — unspecified audio invites
  hallucinated laughter and studio-audience noise. "completely silent except for distant
  traffic"; "quiet studio room tone, no music".
- **Tie SFX to a visible beat for sync:** "Add [sound] exactly when [visible action]
  happens. Keep it [volume/style]."
- **Music: describe mood, instrumentation and dynamics; never name an artist, song or
  brand-genre.** For BadCode this is mostly moot — **the track comes from Suno and is
  laid in post. Do not ask Veo to score anything.**
- In a timestamped multi-shot prompt, give each beat its **own** SFX line rather than one
  global note.
- **Ambience must not compete with dialogue.** One bed, kept low.
- **Budget audio rerolls separately from picture.** Audio is materially less reliable; a
  good visual take frequently arrives with garbled dialogue. If audio is close but not
  right, take the picture and re-voice in post rather than burning credits.

## 7. Dialogue — the resolved syntax

Google contradicts itself here. The Cloud Blog Veo 3.1 guide writes `A woman says, "We
have to leave now."`; the Vertex "Best practices for Veo" page says the opposite —
*"To prevent the model from rendering text in the video, use a colon (:) after the
speaker's action to denote speech and avoid using quotation marks."* Community consensus
sides with the colon.

**Default form:**

```
The man in the green coat says: We have to leave now.
(no subtitles, no captions, no on-screen text)
```

Plus, where a negative field exists: `subtitles, captions, on-screen text, text overlay,
burned-in text`.

Why: burned-in subtitles are a **documented, Google-acknowledged, only partially fixed**
Veo behaviour — the model learned captioning from caption-heavy training video, and
Google's on-record workaround is literally "try your prompt again". Quote marks are the
strongest available signal that a string should be *rendered*. Use quotes only if the
colon form fails to trigger speech at all; treat this as model-version-sensitive.

Other dialogue rules:

- **Attach voice, accent and tone immediately before the speech verb**, not trailing
  after the line: "Bigfoot says in a rough, deep, and booming Scottish male voice: …"
- **Name every speaker by a visual identifier every time they speak:** "The woman
  wearing pink says: …" / "The man with the glasses replies: …"
- **One punchy sentence per clip** — roughly 8 seconds of speech maximum. Longer runs
  rushed and slurred; too short leaves gibberish filler.
- **Spell uncommon names phonetically** ("foh-fur"). Relevant for BadCode's invented lore.
- **Screenplay form is officially attested too:** `Speaker: 'line'` labels work.
- **Lip sync:** anchor the visual first ("speaker faces camera for the line", "mouth
  movement matches the words without exaggerated expression"), then the line. Perfect lip
  sync is not always achievable — keep a re-voice-in-post fallback.
- If Veo keeps inserting dialogue you didn't ask for, don't write "silent" — write the
  actual intended soundscape.

## 8. Negatives — three channels, three syntaxes

| Channel | Syntax | Example |
| --- | --- | --- |
| Vertex API `negativePrompt` | Bare nouns. **Never** "no"/"don't"/instructive language | `wall, frame` · `people, animals` · `overhead lighting, bright colors` |
| Flow's negative field, where exposed | Short comma list, 3–7 items | `subtitles, captions, blur, shaky camera, distorted hands` |
| Inside the main prompt | Positive description of the end state | "a desolate landscape with no buildings or roads" · "low angle, ceiling out of frame" |

Google's guide does show a trailing list form inside the prompt ("no logos, no extra
text, no crowds") for removing *artifacts*, and that works. What does not work is
sentence-form prohibition ("don't include logos") or negating a whole subject category
("no people") — use framing or a positive empty-scene description instead.

### The failure this rule exists for (2026-08-18)

Naming the thing you don't want **summons it**. Three attempts at one shot, all three broken
by the same artefact:

| Attempt | What the prompt said about doors | Result |
| --- | --- | --- |
| v1 | nothing at all | a cabinet door swung open |
| v2 | "every door, panel and surface stays shut… nothing opens, swings, rotates" | doors swung open |
| v3 | the words door/panel/swing/rotate/open never appeared | doors swung open, wider |

Two lessons, and they are different:

1. **The negation in v2 was worse than useless** — it put "door", "swing", "rotate" and
   "open" into the prompt five times. That is this section's rule, and it was already written
   down here when the prompt was authored. It was read and ignored.
2. **But v3 proves wording was never the real lever.** The artefact survived a prompt that
   never mentioned it. See §9 — this was a capability limit, not a prompt defect, and no
   amount of rewriting was going to fix it. **Two identical failures with different wording
   means stop rewriting and question the shot.**

## 9. What Veo cannot do — reach for post instead

Some shots are not prompt problems. Recognising them early is worth more than any phrasing.

**Near-field parallax past flat parallel structures.** Dolly down a corridor, an aisle, a row
of columns or racks, and Veo fakes the parallax by *rotating the geometry* — surfaces hinge
open like doors as they pass. Measured 2026-08-18 across three prompts and two tiers; wording
made no difference. If a shot travels close past parallel flat surfaces, expect this.

**The rule that follows: a camera-only move on a still belongs in post, not in Veo.**

If nothing in the world actually moves — no cloth, no water, no crowd, no machine turning —
and the only motion is the camera (push, pull, pan, tilt, drift), then it is a scale-and-crop
on one image. Render it with ffmpeg or in the edit and you get:

| | Veo | Post |
| --- | --- | --- |
| Artefacts | hinging, morphing, invented motion | **none possible** — it is one image |
| Length | 8s hard cap | **any** |
| Resolution | 720p base | **source resolution** |
| Ease curve | whatever it feels like | exact |
| Cost | 10–100 credits per attempt | free, seconds |

Worked example: `docs/stories/gitpush-origin-master/storyboard/img/s00-pullback-post-12s.mp4`
— a 12s 1080p zoom-out that Veo failed at four times, rendered in one ffmpeg pass.

**Reserve Veo for shots where something in the world has to move.** That is what it is for,
and it is very good at it — the same session's orbital arc and atmospheric descent were both
single-take successes.

## 10. Meta-prompting

Google's own recommended pattern: ask Gemini to draft Veo prompts in batches of 5–10,
giving it (1) a specific task, (2) a precise format constraint, (3) concrete material
constraints ("foil paper or shiny paper", not "paper"), and (4) the emotional target.
Flow's help says the same: "Send Gemini your prompt, an image, or even a video and ask
it to write you new prompts."

This is essentially what a flow-driving skill does when it plans a wave of shot prompts.

## 11. Three things that reliably improve a prompt

Added 2026-08-18 from the external sweep; each is absent from the rest of this file.

**1. Replace speed adjectives with timestamps.** "Slow", "quickly" and "gradually" are
weakly honoured — the model has no scale to hang them on. A timestamped beat is unambiguous
about how long something takes:

> ❌ `a very slow push toward the planet`
> ✅ `[00:00-00:06] the camera pushes toward the planet, covering barely a third of the
>    distance in the whole shot`

**Live proof (2026-08-18, GPOM scene 0):** two takes of one prompt containing "slow
continuous dolly-in" — one crossed the whole move in 4.5s of an 8s clip, the other paced it
across the full 8. Same words, different speeds. The adjective did nothing; only the
timestamps in the sibling prompt held.

**2. Describe the physics, not just the subject.** Name how a thing *behaves* and the clip
stops looking synthetic: `smoke curls rather than billows`, `rain falling at 45 degrees`,
`the fabric settles a beat after she stops`. Material behaviour is where the uncanny lives.

**3. State the camera separately from the action.** Keep the camera clause and the subject
clause in separate sentences rather than braided into one. Veo parses both more reliably
when they are not competing inside a single instruction — and it makes the "one move per
clip" rule visible at a glance, because the camera clause is right there on its own.

## 12. Iteration discipline

- **Don't re-roll the same failing prompt.** Similar prompts yield near-identical
  outputs. Change a verb, a camera term, or the framing of the action.
- When a result is wrong, the productive revision is **subtraction** — remove
  content-description, cut to 1–2 motion instructions — before adding anything new.

---

## Sources

Platform behaviour in this file that is marked "verified live" comes from our own smoke tests
against Flow (`packages/flow-mcp/src/smoke-*.ts`) and is dated where it was checked. The
prompt-craft guidance was cross-checked against these on **2026-08-18**:

- [Ultimate prompting guide for Veo 3.1 — Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1) *(primary — Google's own)*
- [How to prompt Veo 3.1 — Replicate](https://replicate.com/blog/veo-3-1)
- [Veo 3.1 Prompt Guide — LTX](https://ltx.io/blog/veo-prompt-guide)
- [The ultimate prompting guide for Veo 3.1 — Atlabs](https://www.atlabs.ai/blog/the-ultimate-prompting-guide-for-veo-3-1)
- [Structuring Veo 3 Prompts for Better Motion Control — Eachlabs](https://www.eachlabs.ai/blog/structuring-veo-3-prompts-for-better-motion-control)
- [Veo 3 negative prompts: reducing artifacts and unwanted objects — Anakin](http://anakin.ai/blog/veo-3-negative-prompts-how-to-reduce-artifacts-and-unwanted-objects/)
- [30 Cinematic Camera Prompts for Veo 3 and Kling — Prompt Architects](https://prompt-architects.com/blog/25-30-cinematic-camera-prompts-for-veo3-and-kling)
- [Best Prompt Techniques for Veo 3.1 Video Output — Sider](https://sider.ai/blog/ai-tools/best-prompt-techniques-for-veo-3_1-video-output-a-field-guide-to-cinematic-control)

**Where they and we disagree, we win on platform mechanics and they win on prompt craft** —
our mechanics are measured on this account, and none of them have measured it; their craft
guidance is drawn from far more generations than we have run.
