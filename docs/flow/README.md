# Flow toolkit — prompting Google Flow

Platform knowledge for **Google Flow** (labs.google/fx/tools/flow): Veo for video,
Nano Banana for stills. Read on demand via the **`flow-prompt`** skill
(`.claude/skills/flow-prompt/`) — never reproduce it wholesale into a reply.

**This folder is platform-generic.** It describes how the *tool* behaves, true for
anyone using Flow. The BadCode look — 35mm documentary register, muted cool-neutral
palette, what a panel is allowed to be — lives in the skills and is deliberately
NOT here:

| Layer | Lives in |
| --- | --- |
| How Flow behaves (this folder) | `docs/flow/` |
| The comic register | `.claude/skills/badcode-art-direction/SKILL.md` |
| The brand-image register | `.claude/skills/new-image/SKILL.md` |
| Per-story style + prompts | `docs/stories/<story>/prompts.md` |

Same split as [`docs/suno-gpt/`](../suno-gpt/README.md) and the `suno-prompt` skill.

## Files

| File | What | Read when |
| --- | --- | --- |
| [`operating.md`](./operating.md) | **The operating block** — launching the browser, policy blocks, casting, which surface to reach for, how to review output | **First, before any flow call.** The six Flow-using skills point here instead of restating it |
| [`image-prompting.md`](./image-prompting.md) | Nano Banana / Pro still-image craft, editing, rendered text | Generating or editing any still |
| [`video-prompting.md`](./video-prompting.md) | Veo text→video, image→video, frames, audio, dialogue | Any motion work |
| [`camera-vocabulary.md`](./camera-vocabulary.md) | Shot/move/lens/lighting/grade terms, with reliability tiers | Writing the camera clause |
| [`consistency.md`](./consistency.md) | Characters, ingredients, references, continuity across shots | A character or object recurs |
| [`platform-controls.md`](./platform-controls.md) | Models, credits, aspect, duration, Scene Builder, the Agent | Planning a batch or a budget |
| [`failure-modes.md`](./failure-modes.md) | Policy blocks + rewrites; non-policy quality failures | A generation fails, or before writing a risky prompt |

---

## The 15 rules

1. **Write a brief, not a tag dump.** Full sentences, prose. Comma-stacked keywords,
   artist-name dumps and Midjourney weight syntax (`word::1.5`) do nothing here and
   actively degrade Nano Banana, which reasons over the prompt before rendering.
2. **When animating an existing still, describe the motion ONLY.** Never re-describe
   the subject, background or lighting the image already shows — redundant description
   makes the model regenerate instead of animate. Refer to the subject generically:
   "the woman", "the subject", "he".
3. **Front-load the shot.** Camera/framing first, then subject + action, then context,
   then style. Earlier clauses win when instructions compete. *(Corrected 2026-08-18: this
   ordering is **ours**. Google publishes a component list with no mandated sequence, though
   its worked examples do lead with the shot — `video-prompting.md` §1.)*
4. **One action, one camera move, per clip.** Two moves max; three is mush. If a shot
   isn't landing, delete a clause — don't add one.
5. **Iterate on the cheap tier, spend on the locked shot.** Veo 3.1 Lite = 10 credits,
   Fast = 20, Quality = 100. Never send an unproven prompt to Quality. ⚠️ **Except with a cast
   character** — Quality does not support Ingredients/References at all, so those shots top
   out at Fast, at 8 seconds (`platform-controls.md` §1).
6. **Pre-generate every still before you touch video.** A good first frame is most of
   a good clip.
7. **Dialogue: colon, not quotation marks, plus an explicit no-subtitles instruction.**
   Burned-in subtitles are a documented, only-partly-fixed Veo bug; quote marks read as
   "render this as text".
8. **Name every reference image's job in the prompt text.** Past two references the
   model will not infer roles.
9. **Reuse the *identical* wording for a character in every prompt.** Re-describing
   from memory is where drift starts.
10. **One clean element per reference image, plain background.** A crowded gorgeous
    photo loses to a tight cut-out. This single discipline fixes both identity drift
    and style bleed.
11. **Veo 3.1 audio is always on and cannot be turned off — state it anyway.** One line of
    dialogue, one SFX, one ambient bed. Not to get audio (BadCode strips it: `ffmpeg -an`,
    the track is Suno's) but because an unspecified soundscape hallucinates, and because the
    audio stage can kill an otherwise-good picture take. Expect to reroll audio independently
    of picture.
12. **Describe the absence positively.** "an empty street", not "no cars".
13. **Change exactly one variable per test generation**, and never chain an extension
    off an unreviewed clip — errors compound forward.
14. **Push past the airbrushed default with physical imperfections.** "visible pores
    and subtle skin microtexture", fine grain, faint light leak. Bare "photorealistic"
    gets you plastic.
15. **When a prompt is blocked, strip it to nothing and add words back one at a time** —
    and turn off Flow's "Enhance Prompt" first, because its auto-rewrite injects
    language that trips filters you never wrote.

---

## Provenance

### 2026-08-18 — the primary-source pass

The 2026-08-12 sweep below was a **web sweep**: ten agents over blogs, guides and
search-indexed excerpts, with Google's own pages only partly recovered because several are
JS-rendered SPAs. That gap is now closed. On 2026-08-18 every Google page below was fetched
and **read end to end**, and every file in this folder carries a `Sources` section naming
which of its claims came from where.

| Read at source | Settled |
| --- | --- |
| [Video generation prompt guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide) | The 10-component "Anatomy of a prompt"; truck / pedestal / aerial / rack focus, which we were missing; temporal elements; cinematic terms; the negative-prompt rule verbatim; the dialogue colon |
| [Generate videos with Veo 3.1 — Gemini API](https://ai.google.dev/gemini-api/docs/veo) | Audio always-on; per-model durations and resolutions; Extend = "the final second or 24 frames"; reference images are a *subject-identity* mechanism |
| [Image generation with Gemini](https://ai.google.dev/gemini-api/docs/image-generation) | Seven prompt templates we lacked, including comic panels and the 360 character view; "semantic negative prompts"; the real per-model reference caps |
| [Flow models & supported features](https://support.google.com/labs/answer/16352836?hl=en) | **The feature matrix, from Google.** Ingredients unsupported on Quality; Extend is Lite-only by design; 8s is the cap on every Veo tier |
| [Get started with Flow — FAQ](https://support.google.com/labs/answer/16353333?hl=en) | Failed generations aren't billed; rate limiting is real and documented; silent model auto-switching; the visible-watermark toggle |
| [Create videos](https://support.google.com/labs/answer/16353334?hl=en) · [Edit videos & build scenes](https://support.google.com/labs/answer/16935718?hl=en) · [The Flow Agent](https://support.google.com/labs/answer/17093911?hl=en) | Four reference mechanisms, not two; Scenebuilder can download a scene; the History panel is an in-app prompt ledger; Agent batch generation and image-bearing Agent Instructions |

**What it changed, in order of how much it costs to not know:**

1. **A cast character cannot be generated on Quality**, and forces 8s. Our matrix said
   otherwise. This one reshapes shot planning.
2. **Veo's audio cannot be disabled** — the correct move is `ffmpeg -an`, not prompt wording.
   We had been writing prompt language against a setting that doesn't exist.
3. **Not every empty result is a policy block.** Audio failure, rate limiting and
   unusual-activity all look identical over CDP and want the opposite response
   (`failure-modes.md` B0).
4. **Truck and pedestal** — two basic moves absent from our vocabulary, and the reason a
   "zoom" that should have been a travelling move reads flat.
5. **Flow silently swaps your model** when the selected tier lacks a feature you used.

**Also worth knowing but unexercised:** the Flow **Agent** can batch-generate variations and
carries per-project instructions *with a reference image*; **Omni Flash video-to-video editing**
can repair a finished clip (region-gated, likely not available to us); and Scenebuilder has a
**download**, which is how an Extend-grown scene becomes a file.

### 2026-08-12 — the web sweep

Gathered **2026-08-12** by a ten-agent parallel web sweep over Google Flow / Veo 3 &
3.1 / Nano Banana & Nano Banana Pro prompting, followed by an **adversarial
verification pass** in which every non-official claim was independently re-searched
and marked supported / unclear / refuted. 186 findings; 24 of 45 non-official claims
verified (the remaining 21 stay marked unverified in place).

**Source tiers.** *official* = Google Cloud Blog prompting guides, DeepMind model
guides, blog.google, support.google.com/flow, Vertex AI docs. *strong / anecdotal /
contested* = creator guides, Medium/Substack, community prompt repos, Google developer
forums.

**What verification changed:**

- **Refuted and removed** — specifying camera-move timing in seconds ("dolly in over
  0.5s"). Comparative testing found ~39% adherence; plain speed adverbs work better.
  `camera-vocabulary.md` now carries the opposite rule.
- **Refuted as folklore** — the viral `(thats where the camera is)` "magic phrase".
  Single-origin, echoed by content mills, absent from all Google docs. Treat every
  similar single-source magic phrase the same way.

**Gaps in the harvest.** Several `cloud.google.com` pages are JS-rendered SPAs that
returned nav skeletons; content was recovered via search-indexed excerpts and secondary
sources quoting them verbatim. Reddit and Discord were unreachable, so "community
consensus" here means convergence across independent blogs, not counted engagement.

**Refreshing:** re-run the same ten angles. Official-tier URLs are stable; the
platform-controls figures need a live in-app check.

## Known-unreliable / volatile

**Tier 1 — goes stale fastest, re-check before relying:**

- ✅ **RESOLVED 2026-08-18 — the model/feature matrix** in `platform-controls.md` is now
  Google's own published table, cross-checked against our live findings, with the two
  remaining disagreements named and adjudicated in place. It is no longer the most volatile
  thing here. Still re-check before a big shoot: Google changed the Omni Flash duration
  options inside a week.
- **All credit figures and plan names.** Prices conflict across sources. Nano Banana
  Pro's per-resolution cost is third-party, not Google-published.
- ✅ **RESOLVED — the ingredient cap is 3.** Flow's current help page says *"you can add up
  to three ingredients per prompt"*, and the Veo API says *"up to three asset images"*. The
  wrapper claims of 4–9 were wrong. (Separately, the *image* models have their own much larger
  reference caps — `image-prompting.md` §9.)
- **Storyboard Studio / "Make a Story"** — secondary coverage only.

**Tier 2 — weakly evidenced, treat as checklist not doctrine:** "naming a concept even
to negate it activates it" (real for image diffusion, undemonstrated for Veo); "keep
orbits partial, never 360°"; "dolly zoom is impressive but unreliable" (single source —
and the widely-quoted "22% success rate" traces to no real page); the identity-drift-to-
generic-avatar report (one forum thread); "curate exactly ~3 references"; opening an
Extend prompt by acknowledging prior motion; camera-brand names as style tokens *in
video*; the specific trigger-word substitution table in `failure-modes.md` (the
mechanism is corroborated, those exact mappings are one site's invention);
JSON-structured prompting (real practice, but the one hands-on comparison found no
quality advantage over good prose — use it for repeatability, not quality).

**All numeric performance claims** found in the sweep — "95% subtitle prevention",
"99.8% lip sync", "30%→80% hit rate", "40% of dialogue clips get subtitles" — are
unverifiable single-source figures. They appear nowhere in these files; listed here so
nobody re-imports them.

**Tier 3 — live contradictions we picked a side on:**

- **Quote marks vs colon for dialogue.** Google contradicts itself (Cloud Blog uses
  quotes; Vertex best-practices says use a colon). We default to **colon**, because the
  subtitle-burn-in bug is documented and quotes are the strongest "render as text"
  signal. Model-version-sensitive — fall back to quotes if colon fails to trigger speech.
- **Terse command-line prompting with a "Negative Constraints" block** (one guide)
  contradicts Google's conversational-prose guidance across both Veo and Nano Banana,
  and reads as Stable-Diffusion-era practice on a reasoning model. Default to prose,
  and **do not mix the two styles** — that underperforms either alone.
