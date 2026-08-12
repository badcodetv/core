# Seedance 2.5 Prompt Craft

Companion to `docs/flow/` (Google Flow/Veo toolkit) — same spirit, different platform. Seedance 2.5 is ByteDance's video model (BytePlus ModelArk / Volcano Engine), publicly launched 2026-07-31, API opened ~2026-08-07. Every claim below is tagged **OFFICIAL** (verified against BytePlus/ByteDance primary docs) or **COMMUNITY** (third-party docs/blogs/resellers), with a reliability word for community claims. Where briefs disagreed, both sides are shown as a **CONFLICT**.

A structural note that shapes this whole doc: BytePlus's own Seedance 2.5 doc pages (`docs.byteplus.com/en/docs/ModelArk/2607689` prompt guide, `/2607688` tutorial) render client-side and repeatedly returned only navigation shells to automated fetch — so "OFFICIAL" here means confirmed against readable primary text (the API schema page, the 1.0-pro and 2.0-series guides, the Content Pre-filter page), not that every corner of the 2.5-specific doc was inspected. Treat gaps as genuine, not as evidence of absence.

---

## 1. Bottom line

1. **Structure over length.** There's no official word-count target. Use the documented 3-level shape: one-sentence summary → timestamped shot list (1-second-granularity timecodes) → visual-consistency notes. Put camera motion and subject motion in **separate clauses** — merging them is a documented failure trigger (COMMUNITY, likely).
2. **Consistency is 100% reference-array, 0% character object.** Up to a shared pool of references (images/video/audio) addressed by position tags (`@Image1`, `@Video1`, `@Audio1` — OFFICIAL syntax) in prose. An uploaded reference that's never *named* in the prompt text is inert (COMMUNITY, likely).
3. **Chain the last frame for cross-shot continuity.** Extract clip N's final frame and feed it back as clip N+1's start/reference image — the `return_last_frame` API field (OFFICIAL) automates the extraction. This is the Seedance analogue of Flow's chained `generate_video({startImage})` pattern.
4. **Audio is genuinely native but the D&B-track question is unresolved.** `generate_audio` is a real, documented boolean (OFFICIAL). Whether an uploaded reference *track* survives verbatim in the output, versus only steering a synthesized track, is **UNVERIFIED** — settle this with a live test before committing a workflow to it.
5. **Moderation targets photoreal likeness of real public figures at output time, not stylization or political topic.** BadCode's near-black, non-photoreal, fictional-archetype register (the Emperor, generic oligarch caricatures) sits at the low-risk end of the documented filter (OFFICIAL mechanism + COMMUNITY inference). Naming or rendering an actual recognizable politician/billionaire does not — and ByteDance is already in real legal crossfire (Disney, Paramount, MPA, two US Senators) over exactly that.

---

## 2. Prompt structure

**OFFICIAL** — the documented anatomy is three levels, not a fixed 6-slot "formula" (that framing is COMMUNITY/blog synthesis layered on top of this real structure):

1. **One-Sentence Summary** — Subject + Location + Event + Genre/Style + Camera movement, in one sentence.
2. **Detailed Plot Description** — the shot sequence, written as a timeline with timestamps.
3. **Additional Notes** — visual-consistency details: camera angle, environment, atmosphere.

**Timestamp syntax (OFFICIAL, 2.5 doc):** base unit is 1-second intervals. Accepted forms: explicit ranges chained together (`0-3s: … 3-7s: … 7-15s: …` or `[0s-3s]`), point-in-time phrasing ("At the 5-second mark…"), relative phrasing ("After 3 seconds…"). Max clip length is 30s. For multi-panel/storyboard input, keep to **15 panels or fewer**.

**Fuller structural checklist (OFFICIAL, but sourced to the 2.0-series doc — not directly confirmed present in the 2.5 doc, treat as likely-inherited):** Subject (who) → Action (doing what) → Scene/environment (where) → Lighting & color tone → Camera movement (how shot) → Visual style → Image quality → Constraints (what to avoid). Same doc recommends explicit `Shot 1 / Shot 2 / Shot 3` sequencing, each shot = camera framing → subject actions/expressions → positioning → audio info.

**Subject-consistency tag (OFFICIAL, 2.0-series doc, likely-inherited to 2.5):** `Define [core features] in <Image/Video_N> as <Subject_N>` — pick 2–3 stable static features (clothing, hairstyle, appearance) — then reference the subject later as `<Subject_N>@<Image_N>`.

**Negative control is narrow and prose-based (OFFICIAL, verified for 2.5):** only documented for subtitles ("Do not add subtitles" / "No subtitles") and audio sub-channels ("No BGM; generate only environmental sounds and action sounds", "No audio"). No general `negative_prompt` field was found documented for 2.5 — negation is natural language, scoped to those two areas only.

**Community rule worth following anyway (COMMUNITY, likely):** positive restatement beats pure negation for behavior you want suppressed elsewhere ("stable low tracking camera with restrained movement" rather than "no chaotic camera") — one source frames this explicitly: *"Exclusions are not guarantees. They are criteria for review."*

### Worked template

```
[ONE-SENTENCE SUMMARY]
<Subject> in <location>, <event/action>, <genre/style>, <camera movement>.

[SHOT LIST — 1s-granularity timestamps]
0-4s: <camera clause>. <subject/action clause, separate sentence>.
4-9s: <camera clause — ONE move>. <subject/action clause>. Action begins only after <trigger event>.
9-15s: <camera clause>. <subject/action clause>.

[ADDITIONAL NOTES]
Camera angle: <e.g. eye-level, low-angle>.
Environment: <fixed details that must not drift>.
Atmosphere/lighting: <mood, color temperature>.
Preserve: <named invariant details — clothing, props, layout — across the whole clip>.
No subtitles. No BGM; environmental sound only. [only if you actually want silence/no text]
```

### Example 1 — near-black satirical single-subject shot (no dialogue)

```
A gaunt Emperor archetype in an ornate near-black throne room lit by one hard rim light,
satirical political-satire tone, slow push-in dolly.

0-5s: Camera holds static, waiting. He raises a printing block stamped with a coin sigil,
turning it slowly toward camera.
5-11s: Camera begins a slow ten-degree push-in only after the block stops turning. He lowers
the block and the light catches the coin sigil.
11-15s: Camera holds still. Ash begins to drift down past his shoulder and settles on the floor.

Camera angle: low-angle, eye-level with the throne base.
Environment: bare stone throne room, single visible light source, everything else in near-black.
Atmosphere: cold, monumental, still.
Preserve: crown shape, coin-sigil block, near-black palette with one warm rim light throughout.
No subtitles. No BGM; environmental sound only.
```

### Example 2 — multi-reference continuity shot (chained from a prior clip's last frame)

```
[Image1] is the last frame of the previous shot and is the starting state. The same figure
from [Image1] continues walking through a server-hall corridor, cinematic satire tone,
slow lateral tracking shot.

0-6s: Camera tracks left, parallel to the subject, half a stride behind. The figure from
[Image1] keeps the same coat, badge, and gait established in that frame.
6-15s: Camera continues the same tracking move at matching speed, no drift. The figure turns
to face a bank of humming server racks that were already visible in [Image1]'s background.

Camera angle: waist-height tracking, matching [Image1]'s camera height.
Environment: identical corridor, server racks, and floor markings as [Image1] — no new set elements.
Preserve: exact coat, badge, hair, and posture from [Image1] for the entire shot.
```

---

## 3. Parameter tokens & API knobs

**⚠️ CONFLICT flagged inline below where community sources contradict the verified official schema.** Do not invent parameters beyond what's listed here.

### Official API schema (OFFICIAL, verified — endpoint `POST /api/v3/contents/generations/tasks`, covers Seedance 1.0/1.5/2.0/2.5, some fields model-scoped as noted)

| Field | Type | Values / range | Scope |
|---|---|---|---|
| `model` | string | e.g. `dreamina-seedance-2-5-260628` | all |
| `content` | array | text / image / audio / video / sample-task-id parts | all |
| `resolution` | string | `480p` / `720p` / `1080p` / `4k` (varies by model) | all |
| `ratio` | string | `16:9` / `4:3` / `1:1` / `3:4` / `9:16` / `21:9` / `adaptive` | all |
| `duration` | integer | **[4, 30]s for Seedance 2.5**; [4,15]s for 2.0-series; [4,12]s for 1.5-pro | all |
| `frames` | integer | takes precedence over `duration` | **1.0-pro only** |
| `seed` | integer | default `-1`, range [-1, 2147483647] | **1.5/1.0 only** per this schema — see conflict below |
| `camera_fixed` | boolean | default `false` | **1.5/1.0 only** per this schema — see conflict below |
| `watermark` | boolean | default `false` — adds "AI Generated" watermark, lower-right | all |
| `callback_url` | string | optional | all |
| `generate_audio` | boolean | default `true` | **2.5 / 2.0 / 1.5-pro only** |
| `return_last_frame` | boolean | default `false` — use this for last-frame chaining, §5 | all |
| `safety_identifier` | string | max 64 chars | all |
| `priority` | integer | 0–9 | **2.5 / 2.0 only** |
| `service_tier` | string | `default` or `flex` (flex = 50% cost reduction, offline) | all |
| `execution_expires_after` | integer | [3600, 259200]s, default 172800 | all |
| `draft` | boolean | — | **1.5-pro only** |
| `output_format` | string | `mp4` (default) or `mov` | **2.5 only** — use `mov` for edit/extend tasks, recommended for audio-visual continuity |
| `omni_reference_task_type` | string | `auto` / `reference` / `edit` / `extend` | **2.5 only** |

**⚠️ CONFLICT — `camera_fixed`/`seed` and 2.5:** the verified official schema above scopes `camera_fixed` and `seed` to "Seedance 1.5/1.0 only," implying they are *not* exposed for 2.5. But COMMUNITY sources (aimlapi, a GitHub Seedance-2.5 prompt collection) describe `camera_fixed` (boolean, default false) as present and working on 2.5, worded as "biases the model toward a locked-off camera… the actual effect is not guaranteed." Unresolved — if you need a hard camera lock on 2.5, don't rely on the flag alone; reinforce with explicit prose ("static shot," "the camera never moves") regardless of which schema is accurate.

**⚠️ CONFLICT — `generate_audio` default:** official schema says default `true` for 2.5/2.0/1.5-pro (OFFICIAL). One COMMUNITY reseller doc (Segmind) states the default is `false` ("off unless you ask"); another Segmind page claims it defaults `true` only on video-edit/extend endpoints and isn't exposed at all on T2V/I2V/Omni-Reference endpoints. Don't assume a default — set it explicitly.

### Reference-asset tagging (OFFICIAL, verified for 2.5)

- In-prompt tags: `@Image1`, `@Video1`, `@Audio1` — numbered **per type**, not globally.
- Role assigned via a separate `content.role` field: `first_frame`, `last_frame`, `reference_image`, `reference_video`, `reference_audio`.
- Multi-asset binding is written in prose: e.g. *"Images 1–2 are Character 1 and correspond to Audio 1."*
- COMMUNITY note: third-party hosts (fal.ai, Runware) render the same idea as `[Image1]` in their own docs instead of `@Image1` — likely just each host's documentation style, not confirmed as an interchangeable literal syntax on ByteDance's own surface.
- Reference pool ceiling reported as **up to 50 total: 30 images / 10 video / 10 audio** (COMMUNITY, verified against fal.ai's and Segmind's own schemas, but not directly confirmed on a BytePlus/ByteDance-owned page — treat the exact numbers as third-party-corroborated, not primary-sourced).

### Older `--flag` in-prompt syntax — OFFICIAL, but for **Seedance 1.0-pro/pro-fast only**, NOT confirmed for 2.5

Format: text prompt + `--` command parameters appended inline.

```
--resolution 1080p --duration 5 --camerafixed false
```
(short forms: `rs`, `dur`, `cf`)

This mechanism was **not found** in the fetched Seedance 2.5 guide. For 2.5, resolution/duration/ratio/seed appear to be pure JSON request-body fields — do not append `--flags` inside a 2.5 prompt string.

### Dialogue/audio bracket syntax — CONFIRMED for 2.0-series only, claimed-but-unverified for 2.5

**OFFICIAL, verified for the 2.0-series doc:** `{text}` = dialogue, `<description>` = sound effects, `（description）` (full-width parens) = BGM, `【text】` = on-screen subtitles. Rule: don't mix Chinese/English within a dialogue line except proper nouns.

A targeted check of the 2.5 doc specifically found **no mention** of this bracket scheme — 2.5's own bracket usage there is limited to asset tags and timestamp ranges. COMMUNITY sources (Segmind, calling itself "the official Seedance 2.5 prompt guide" — it is not ByteDance-authored despite the title) claim the same four brackets carry over to 2.5, plus a rule that non-English dialogue needs a prefix line ("Dialogue language: British English, warm and low") before the `{}` block, and that dialogue (`{}`) and subtitles (`【】`) are separate channels — text in `{}` does not automatically appear on-screen. Treat all of this as **likely but unverified** for 2.5 until a primary source confirms it.

---

## 4. Camera & motion vocabulary

**All entries in this section are COMMUNITY** (no official Seedance 2.5 vocabulary list was found — the official docs specify *where* camera movement goes in the structure, not *which terms* the model recognizes). Reliability tiers below are pattern-matched across converging community sources (Runware, fal.ai, Elser), not a benchmark.

| Instruction | What Seedance does | Reliability |
|---|---|---|
| Push-in / dolly-in | Camera moves smoothly toward subject | Reliable |
| Pull-back / dolly-out | Camera moves away | Reliable |
| Truck left/right | Lateral camera move | Reliable |
| Tracking / follow shot (parallel or steadicam) | Camera moves with subject at matching speed | Reliable |
| Orbit/arc, quantified (e.g. "slow 180-degree orbit") | Circles the subject | Reliable **when given a numeric degree/speed** — unquantified "orbit" is weaker |
| Crane/boom up/down | Vertical camera move | Reliable |
| Pan/tilt (fixed-position rotation) | Reliable |
| Handheld ("organic subtle shake") | Adds natural sway/weight | Reliable |
| Gimbal ("smooth glide") | Smooth stabilized motion | Reliable |
| Static / locked-off / "static tripod shot" | Camera holds still | **Mixed** — prose alone works most of the time; for a hard guarantee, pair with the `camera_fixed` flag (itself only a soft bias per community reports) |
| Rack focus | Focus shifts between subjects | Mixed — depends on clear subject separation in frame |
| Dolly zoom / vertigo effect | Simultaneous zoom + dolly | Mixed — advanced/rare effect, reliability not well attested |
| Whip pan | Fast rotational blur | Mixed — fast-motion moves compound with the model's documented morphing risk during fast action (§7) |
| Bird's-eye / top-down | Reliable |
| Worm's-eye / low-angle | Reliable |
| FPV continuous long take | Extended first-person move | Mixed — longer, complex single moves are more prone to drift over a 30s clip |
| **Stacking multiple distinct camera moves in one clause** | Model flattens both, or ignores direction entirely | **Ignored** — documented failure trigger; pick ONE camera move per beat |
| **High-frequency micro-cues** (e.g. "shake three times a second") | "Fights the model rather than directing it" | **Ignored** — timing precision has a floor around ~1s, not frame-level |
| Camera + subject motion merged into one clause | Both axes get flattened | **Ignored/degraded** — always split into two clauses |

**Subtlety technique (COMMUNITY, likely):** quantify the move ("slow ten-degree clockwise arc," "half a car length behind") rather than relying on adjectives like "subtle" or "slow" alone. Tie the *start* of camera movement to a triggering event in the action ("camera does not pan until the ball has fully left both hands") rather than front-loading motion at 0s.

**Pacing on long (30s) clips (COMMUNITY, likely):** if you don't give the extra runway something concrete to do, "the extra time usually turns into waiting, repetition, or slow motion." State "natural real-time speed" explicitly if you don't want the model defaulting to slow-motion padding.

**Intensity control (COMMUNITY, likely):** no numeric "motion intensity" scalar exists in any documented API. Control amount of movement through prose adverbs (slowly/quickly/gently/violently/with large amplitude) or by swapping the motion *type* (handheld vs. gimbal vs. tripod) rather than trying to dial one type up or down.

---

## 5. Consistency discipline

**No structured character object exists.** Unlike Flow's `create_character`, Seedance's entire consistency mechanism is: pass reference images/video/audio into the array, then bind each one to a role **in prose**. (COMMUNITY, likely — corroborated independently by fal.ai and Runware schemas, though not read directly off a BytePlus-owned page.)

**Reference pool limits (COMMUNITY):**
- Up to ~50 references total: 30 images / 10 video / 10 audio.
- Multi-subject reliability: **1–8 image subjects reliable; 9–12 possible but reduced stability.** Video/audio subjects: **1–5 optimal; 6–10 unstable.**
- For 5+ subjects, use one clean reference view per subject rather than multi-angle reference sets per subject.

**Binding rule (COMMUNITY, likely):** address every subject explicitly by tag — *"The lead singer references [Image1]. The guitarist references [Image2]. Preserve each member's face, hair, and wardrobe from their reference."* Never leave an uploaded reference unaddressed in the prompt text — an unnamed reference is effectively inert. Don't let an image reference and a video reference try to do the same identity-anchoring job for one character.

**Invariant-noun rule (COMMUNITY, likely):** describe specific, named, invariant nouns (clothing items, props, physical details) rather than general adjectives, and close with an explicit preservation clause: *"Keep the same messenger, jacket, helmet, bottle, phone, clerk, counter, cooler, and store layout from first frame to last."*

**Seed (OFFICIAL field, COMMUNITY behavior claim):** `seed` is an optional integer, echoed in the API response — but same-seed + same-prompt is reported as *highly similar, not pixel-identical* (COMMUNITY, likely). Do not treat it as a hard lock. Also see the `camera_fixed`/`seed` scope conflict in §3.

### First+last frame mode (OFFICIAL field shape, COMMUNITY prompting practice)

The image-to-video path accepts both a start image and an optional end image in one call (`image_url` + `end_image_url` per third-party schemas — same feature shape as Flow's three-mode `generate_video` contract). Both images should share the same aspect ratio or the last frame gets stretched to fit.

**Prompting rule (COMMUNITY, likely):** state explicitly, in a separate line, which image is the first frame and which is the last, then describe **one continuous action** that bridges them. A combined "these two are first/last" sentence does not reliably bind either image to its role.

**Single-image (start-only) mode is the inverse rule:** describe *what changes*, not what's already visible — the reference image already establishes the subject; spend the prompt words on motion, camera, and sound instead of re-describing the static scene.

### Chaining shots across separate generate calls

This is the primary technique for continuity **across** clips (first+last-frame mode only solves continuity **within** one clip):

1. Generate clip N.
2. Extract its final frame — use `return_last_frame: true` (OFFICIAL field) to get this automatically, rather than manually screenshotting.
3. Feed that frame back in as `[Image1]` / the start image for clip N+1, with `content.role: first_frame` or `reference_image`.
4. Match pose, orientation, prop position, background geometry, camera height, lighting, and motion direction explicitly across the boundary in the next prompt's notes.

**Why this matters more than usual for Seedance:** the whole 30-second clip is generated in one native pass, not stitched from shorter segments — so *within* one call, consistency doesn't compound-drift the way frame-by-frame stitching does. But that single-pass mechanism does nothing for consistency *between* separate calls; last-frame chaining is what carries a character or scene from shot to shot (COMMUNITY, likely).

**Not-official caveat:** some third-party wrapper libraries (e.g. a GitHub "Seedance-2-API" project) advertise a `@character:<request_id>`-style character-sheet primitive built on top of the raw reference array. This is **client-side sugar invented by the wrapper, not part of ByteDance/Volcengine/BytePlus's own API** — there is no native character object, request-id identity store, or `@character:` tag on the official surface.

---

## 6. Audio

**Native co-generation is real (OFFICIAL, broad claim only):** ByteDance's own product page demonstrates multilingual speech and lip sync generated jointly with video. No official parameter-level docs (codec, sample rate, mono/stereo) were found for this — those specifics are undocumented anywhere checked.

**Toggle:** `generate_audio` (OFFICIAL field, boolean) — see the default-value conflict flagged in §3. Set it explicitly rather than relying on a default.

**Supplying your own audio as a reference (COMMUNITY, likely for the *feature*; specifics unverified):**
- Reported cap: up to 10 audio files, combined **≤30 seconds total** (not per-file), inside the shared 50-reference pool.
- What it reportedly does: *"An audio-only reference lets a single voice, music, or sound-effect track drive the pacing, beat-matching, and lip-sync of the shot"* — described as a real conditioning-of-timing effect, not just a style hint.
- Tag syntax reportedly mirrors image tags: `@Audio1`, addressed in prompt text ("sync the footsteps to @Audio1").

**🚩 The one fact that decides whether this workflow is usable for a D&B-driven video: UNVERIFIED.** No source — official or third-party — states whether an uploaded reference track is preserved **verbatim** as the rendered clip's output audio, or whether the model only uses it as a rhythm/style conditioning signal while synthesizing new (possibly re-interpreted, lower-fidelity) audio of its own. This is not settleable from documentation; it needs a hands-on test with live API access before committing a "cut motion to our existing master" pipeline to it.

**Dialogue convention (see §3 for full detail and the unverified-for-2.5 caveat):** `{}` for spoken dialogue, `<>` for SFX, `（）` (full-width) for BGM, `【】` for on-screen subtitles — confirmed OFFICIAL for the 2.0-series doc, claimed but unverified for 2.5. Dialogue and subtitles are separate channels; putting a line in `{}` does not make it appear as on-screen text — repeat it in `【】` if you want both.

**Silencing:**
- OFFICIAL, verified narrow negative-control phrases: *"Do not add subtitles" / "No subtitles"*, and *"No BGM; generate only environmental sounds and action sounds" / "No audio."*
- COMMUNITY, unverified: setting `generate_audio: false` is reported to suppress generated audio entirely at no cost difference — but given the default-value conflict in §3, verify this behavior directly rather than assuming.

**Language:** 2.5 supports native generation in 10+ languages (OFFICIAL, likely — worked examples in the doc are predominantly English, no stated quality differential between languages for 2.5 specifically). The 2.0-series bracket-dialogue rule explicitly warns against mixing Chinese/English within one dialogue line except for proper nouns — apply this if using the bracket syntax.

**For edit/extend/reference tasks:** set `output_format: mov` (OFFICIAL, 2.5-only field) — recommended specifically "for audio-visual continuity."

---

## 7. Failure modes & moderation

### The one confirmed official moderation mechanism

**OFFICIAL, likely:** BytePlus ModelArk's **Content Pre-filter** is a deep-learning face/voice-similarity check run against **generated output** (not just the prompt), matching against a reference set of public figures across five categories: **politics, sports, business, entertainment, media.** ByteDance states this is *"not a comprehensive block on prominent public figures"* (false negatives happen). Enterprise customers can register real-human likenesses for controlled use via a separate "Digital character library" — implying unregistered real faces default to restricted.

**What this means structurally:** the filter is keyed to *photoreal resemblance to a real identifiable person*, not to subject matter, topic, or viewpoint. **No evidence was found of a topic- or ideology-based political filter** (COMMUNITY, likely) — a fictional archetype ("the Emperor," a generic oligarch caricature) sits outside what this detector is built to catch, structurally, regardless of how pointed the satire is. A real, named, recognizable politician or billionaire rendered with photoreal likeness is a different matter entirely.

### How a block presents

**OFFICIAL, verified (fal.ai, a hosting provider):** generic HTTP 422 with `"type": "content_policy_violation"` — does **not** identify which category triggered it (violence/nudity/public-figure/etc.), and does not distinguish whether the prompt text, a reference image, or the generated output was the trigger point. fal's own docs confirm different partner backends apply different strictness for the same underlying model — moderation is not uniform across hosts.

**COMMUNITY, unverified:** on consumer-facing ByteDance surfaces (not the raw API), failures reportedly collapse into an undifferentiated "Generation Failed" message or a stuck progress bar — indistinguishable from a GPU/queue timeout. This is the **same operational trap already documented for Google Flow/Veo in this repo** (*"a policy block looks exactly like a timeout"*) — the same discipline likely transfers: **don't blind-retry a stall; rewrite the prompt instead.**

**COMMUNITY, unverified:** reference-image upload can itself be rejected before the prompt is evaluated ("Input Image May Contain a Real Person"-type errors), separately from output-stage checks.

### Real-world legal context (relevant to how seriously to take likeness rules)

**OFFICIAL/verified events, COMMUNITY characterization of the fix:** a viral Seedance-generated Tom Cruise/Brad Pitt fight clip and broader Hollywood-character generation triggered: MPA denouncement, a Disney cease-and-desist (2026-02-13), a Paramount Skydance infringement claim (Star Trek/South Park/Dora), and a US Senate letter (2026-03-16) demanding ByteDance shut the tool down. ByteDance responded it would "strengthen current safeguards." A since-paywalled report claims Seedance 2.5's moderation shifted toward **output-stage review** as a result — generate first, then refuse to serve if a protected likeness is recognized (secondhand via search snippet only, not independently confirmed).

### Rough hard/soft wall hierarchy (COMMUNITY, unverified — pattern-matched across multiple SEO/troubleshooting sites, not primary policy text)

1. **Hardest wall:** sexual/CSAM content — no known bypass, account-ban risk on repeat attempts.
2. **Porous-but-filtered:** real identifiable faces (celebrities, politicians) and copyrighted/trademarked characters — reported to be bypassable with stylized phrasing.
3. **Loosest wall:** violence/gore/weapons — reportedly keyword-list-based, biased toward English-vocabulary trigger words.

### Rewrite tactics

- **Stylize explicitly.** COMMUNITY sources converge (unverified at primary-source level, but consistent with the *official* face/voice-similarity mechanism, which is structurally weaker against non-photoreal art) that prompting "graphic novel," "illustrated," "animated," or "stylized" style reduces face/IP-filter trigger rate with no reported quality tradeoff for that register — this is directly favorable to BadCode's existing near-black, non-photoreal comic style.
- **Use fictional archetypes, not named real figures** — already BadCode's convention ("the Emperor," not a sitting head of state).
- **Positive restatement over pure negation** for behavior constraints — treat exclusions as "review criteria," not guarantees.
- **On a stall or generic failure, rewrite rather than retry** — the fal.ai 422 is explicitly non-retryable, and consumer-surface failures don't tell you what went wrong.
- **`seedance.ai` is not an official ByteDance/BytePlus/Volcengine property** (verified by direct fetch — it's an unrelated third-party product using the name). Don't cite its "content policy" page as ByteDance's actual policy; several other lookalike domains found during research (seedance2pro.io, seedance-2.app, etc.) are likely similarly unofficial.

---

## 8. Seedance vs Veo 3.1

**Benchmark data (OFFICIAL/verified — Artificial Analysis Video Arena, blind human-vote Elo, data as of 2026-08-02):** on the image-to-video board, **"Dreamina Seedance 2.0 720p" ranks #1 overall at Elo 1,199**; Veo 3.1 sits at Elo 1,085 (rank 10), Veo 3.1 Fast 1,077 (rank 12), Veo 3.1 Lite 1,066 (rank 16); Kling 3.0 1080p Pro at 1,077 (rank 13). Eight of the top ten entries on these boards are Chinese-lab models. **Seedance 2.5 does not yet appear as a distinct leaderboard entry** — its standalone Elo standing is unverified as of this research.

**Qualitative consensus (COMMUNITY, unverified — reads as SEO-comparison-site color, not benchmarked journalism):**
- **Seedance wins on:** scene/motion complexity, multi-shot character & product consistency, native joint audio-video generation, price-to-quality, and (2.5's headline) 30-second single-pass generation vs. the ~8–15s ceiling most rivals including Veo 3.1 need to stitch toward.
- **Veo 3.1 wins on:** single-continuous-shot cinematic polish and color grading, and audio/lip-sync fidelity for a hero shot.

**Practical guidance for this repo:**
- Reach for **Seedance** when the shot needs: a long single-pass sequence (up to 30s) with multiple internal beats, heavy multi-subject reference consistency in one call, or audio-driven pacing/dialogue baked in.
- Reach for **Veo 3.1** (the existing, better-mapped toolkit in `docs/flow/`) when the shot is a single hero take where cinematic polish/color grade matters most, or where you need the reliability-tiered camera vocabulary and known failure modes that Flow's toolkit already has solidly documented — Seedance's own camera vocabulary is comparatively under-attested (everything in §4 here is community pattern-matching, not benchmark-verified).
- **Pricing is not comparable across a single number.** fal.ai reports $0.24–0.68/sec depending on resolution/tier; OpenRouter lists Seedance 2.0 "from $0.067/sec"; Volcengine direct pricing converts to roughly $0.08–0.14/sec. These disagree by 3–10x — always confirm provider + resolution + tier before estimating cost, don't quote a bare per-second figure.

---

## 9. Sources

**OFFICIAL (BytePlus / ByteDance primary):**
- `docs.byteplus.com/en/docs/ModelArk/2607689` — Dreamina Seedance 2.5 prompt guide
- `docs.byteplus.com/en/docs/ModelArk/2607688` — Dreamina Seedance 2.5 tutorial
- `docs.byteplus.com/en/docs/ModelArk/1520757` — API video-generation task reference (full parameter schema)
- `docs.byteplus.com/en/docs/ModelArk/1631633` — Seedance 1.0-pro / pro-fast prompt guide (`--flag` syntax)
- `docs.byteplus.com/en/docs/ModelArk/2222480` — Dreamina Seedance 2.0-series prompt guide (bracket syntax, advanced formula)
- `docs.byteplus.com/en/docs/ModelArk/Content_Pre-filter`, `.../content_pre_filter_faq`, `.../2223965`, `.../2333565` — moderation mechanism
- `seed.bytedance.com/en/seedance2_5` — official product page
- `arxiv.org/html/2506.09113v1` — Seedance 1.0 technical report (training-side, not a prompting guide)
- `arxiv.org/pdf/2604.14148` — Seedance 2.0 technical report (VBench self-benchmarks vs. Kling/Sora2/Veo3.1)
- `en.wikipedia.org/wiki/Seedance_2.0` — IP/legal escalation timeline

**COMMUNITY (third-party hosts, resellers, journalism, SEO/blog):**
- `fal.ai/models/bytedance/seedance-2.5/*`, `fal.ai/learn/devs/seedance-2-5-prompting-guide`, `fal.ai/docs/documentation/model-apis/errors`
- `runware.ai/docs/models/bytedance-seedance-2-5/guides/*`
- `replicate.com/bytedance/seedance-2.5`
- `blog.segmind.com/*` (self-titled "official" guide — is not ByteDance-authored)
- `docs.aimlapi.com/api-references/video-models/bytedance/*`
- `github.com/Anil-matcha/*` — third-party wrapper libraries (character-sheet primitive explicitly non-official)
- `www.mindstudio.ai/blog/*` — independent hands-on review (morphing/decoherence, resolution cap discrepancy)
- `www.elser.ai/news/*`, `www.atlascloud.ai/blog/*`, `higgsfield.ai/blog/seedance-2-5` — independent/comparison testing
- `artificialanalysis.ai/video/leaderboard/image-to-video` — Elo arena (verified data, third-party benchmark)
- `the-decoder.com`, `technode.com`, `deadline.com` (paywalled, secondhand only), `nbcnews.com` — journalism
- `reapi.ai/blog/seedance-2-5-release-status`, `kie.ai/blog/seedance-2-5-release-deep-dive`, `cined.com/*` — release-status aggregation
- `openrouter.ai/bytedance/seedance-2.0` — pricing

**Explicitly flagged as NOT authoritative:** `seedance.ai` (unrelated third-party product, confirmed by direct fetch) and its lookalike-domain cluster (seedance2pro.io, seedance-2.app, seedance2-video.com, seedanceguide.com, etc.) — content-mill sites riding the model name, down-weighted throughout.