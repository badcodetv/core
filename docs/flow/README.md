# Flow toolkit — prompting Google Flow

Platform knowledge for **Google Flow** (labs.google/fx/tools/flow): Veo for video,
Nano Banana for stills. Read on demand via the **`flow-prompt`** skill
(`.claude/skills/flow-prompt/`) — never reproduce it wholesale into a reply.

**This folder holds two jobs, and they are not the same job** (restated 2026-08-20, when the
automation half moved in from `docs/superpowers/`):

| Half | What it is | Files | Skill |
| --- | --- | --- | --- |
| **Craft** — platform-generic | How the *tool* behaves. True for anyone using Flow, ours or not. | `image-prompting` · `video-prompting` · `camera-vocabulary` · `physics-and-motion` · `consistency` · `failure-modes` · `post-production` | **`scene-prompt`** *(not yet built)* |
| **Automation** — ours | How *our* code drives it: DOM roles, selectors, completion signals, harvest. Useless to anyone not running `@badcode/flow-mcp`. | `automation-images` · `automation-video` · `platform-controls` | ✅ **`flow-automation`** |

`platform-controls` sits on the automation side because what it answers — which tier supports
what, what it costs, what Flow silently swaps — is a question you ask while *driving*, not
while writing.

The BadCode look — 35mm documentary register, muted cool-neutral palette, what a panel is
allowed to be — is a **third** job and lives in the skills, deliberately NOT here:

| Layer | Lives in |
| --- | --- |
| How Flow behaves + how we drive it (this folder) | `docs/flow/` |
| The comic register | `.claude/skills/badcode-art-direction/SKILL.md` |
| The brand-image register | `.claude/skills/new-image/SKILL.md` |
| Per-story style + prompts | `docs/stories/<story>/prompts.md` |

Same split as [`docs/suno-gpt/`](../suno-gpt/README.md) and the `suno-prompt` skill.

## Files

| File | What | Read when |
| --- | --- | --- |
| [`operating.md`](./operating.md) | ⚠️ **Dissolving.** Its automation half became the `flow-automation` skill; the policy-block triggers and casting discipline wait here for `scene-prompt` | Nothing points here any more. Don't add to it |
| [`image-prompting.md`](./image-prompting.md) | Nano Banana / Pro still-image craft, editing, rendered text | Generating or editing any still |
| [`video-prompting.md`](./video-prompting.md) | Veo text→video, image→video, frames, audio, dialogue | Any motion work |
| [`camera-vocabulary.md`](./camera-vocabulary.md) | Shot/move/lens/lighting/grade terms, with reliability tiers | Writing the camera clause |
| [`physics-and-motion.md`](./physics-and-motion.md) | How Veo handles weight, force and material — measured rates, the phrasings that help, the shot classes to avoid | **At storyboard time**, on any shot whose point is that something moves, falls, pours, swings or carries weight |
| [`consistency.md`](./consistency.md) | Characters, ingredients, references, continuity across shots | A character or object recurs |
| [`platform-controls.md`](./platform-controls.md) | Models, credits, aspect, duration, Scene Builder, the Agent | Planning a batch or a budget |
| [`failure-modes.md`](./failure-modes.md) | Policy blocks + rewrites; non-policy quality failures | A generation fails, or before writing a risky prompt |
| [`post-production.md`](./post-production.md) | 🔴 **The ffmpeg half of every shot** — the Veo-or-post decision, the tested recipe book (reverse, ping-pong loop, eased camera move on a still, retime, chain, crop, contact sheet), and the resolution ceiling | **Before you spend a credit**, and after every clip lands |
| [`automation-images.md`](./automation-images.md) | **Automation.** The still-image UI recipe: selectors, DOM roles, the asset picker, characters, reference images, harvest | You are changing `@badcode/flow-mcp`, or a tool call behaves oddly |
| [`automation-video.md`](./automation-video.md) | **Automation.** The image→video recipe: completion signals, Frames mode, what a finished clip offers, the picker traps | Same, for motion |

---

## The 16 rules

1. **Write a brief, not a tag dump.** Full sentences, prose. Comma-stacked keywords,
   artist-name dumps and Midjourney weight syntax (`word::1.5`) do nothing here and
   actively degrade Nano Banana, which reasons over the prompt before rendering.
2. **When animating an existing still, describe the motion ONLY.** Never re-describe
   the subject, background or lighting the image already shows — redundant description
   makes the model regenerate instead of animate. Refer to the subject generically:
   "the woman", "the subject", "he".
3. **Front-load the shot.** Camera/framing first, then subject + action, then context,
   then style. Earlier clauses win when instructions compete. *(Re-corrected 2026-08-20: the
   formula **is Google's** — its Cloud Blog publishes this exact five-part sequence under "A
   formula for effective prompts". The 2026-08-18 note claiming otherwise was wrong and has been
   struck. What stays ours and measured is that earlier clauses win. It is a checklist, not a
   mandated string order, and camera-first does not port to other models — `video-prompting.md` §1.)*
4. **One action, one camera move, per clip.** Two moves max; three is mush. If a shot
   isn't landing, delete a clause — don't add one.
5. **Iterate on the cheap tier, spend on the locked shot.** Veo 3.1 Lite = 10 credits,
   Fast = 20, Quality = 100. Never send an unproven prompt to Quality. ⚠️ **Except with a cast
   character** — Quality does not support Ingredients/References at all, so those shots top
   out at Fast, at 8 seconds (`platform-controls.md` §1).
   ⚠️ **And the cheap-tier proxy is weakest on exactly the path we use.** Google's own head-to-head
   puts Lite level with Fast on text-to-video (54.6% win-rate over 1,000 prompts) and clearly
   *behind* on image-to-video (47.2% over 646) — and we are stills-first on almost every shot.
   Iterate on Lite for framing, blocking and policy-cleanliness; **confirm the motion on Fast**
   before you lock. (official, [Veo 3.1 Lite model card](https://deepmind.google/models/model-cards/veo-3-1-lite/))
6. **Pre-generate every still before you touch video.** A good first frame is most of
   a good clip.
7. **Dialogue: colon, not quotation marks, plus an explicit no-subtitles instruction.**
   Burned-in subtitles are a documented, only-partly-fixed Veo bug; quote marks read as
   "render this as text".
8. **Name every reference image's job in the prompt text.** Past two references the
   model will not infer roles.
9. **Reuse the *identical* wording for a character in every prompt.** Re-describing
   from memory is where drift starts. **And state skin tone and ethnicity explicitly, in the
   DNA block, every time** — Google's own model card records that Veo *"appears to skew towards
   lighter skin tones when race is not specified in the prompt"*. Omission is not neutrality;
   it is a documented pull in one direction.
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
16. 🔴 **Before every generation, ask: does anything in the world actually move?** If only the
    camera moves, it is a scale-and-crop on one image and belongs in `ffmpeg`, not Veo — free,
    any length, an exact ease curve, and **no artefact is possible** because it is one image.
    And if Veo refuses a move, ask whether it will do the **inverse**: a push-in reversed in post
    is a rigid pull-back. Plan every shot as *prompt → generate → transform*, so the transform is
    designed rather than improvised. [`post-production.md`](./post-production.md).
17. **Generate into a scratch folder; commit almost nothing.** A finished 56-second scene cost 42
    video takes and 22 stills and shipped on **three** of them. Work entirely in the scene's
    scratch folder until a human approves a cut, then commit only the stills Flow generated **as
    images** that a kept clip was built from — never a frame you pulled out of a video, because
    that is recoverable from the approved video at a known timestamp (measured: 1.2–2.3/255
    difference, i.e. codec noise). The test: delete the scratch folder except the approved video,
    and the scene must still rebuild from the repo plus that one file.
    `.claude/skills/flow-automation/SKILL.md` §9.

---

## Provenance

### 2026-08-20 — the ten-angle deep sweep

Ten Sonnet web-research agents over ten deliberately non-overlapping angles (official surfaces
not yet read · camera precision · physics · prompt structure · lighting & lens · image-to-video ·
multi-beat · consistency · limits & negatives · practitioner corpora · adjacent-model transfer),
then five independent verifiers who re-searched every non-official claim, then synthesis.
**118 raw findings → 31 official-tier + 71 verified → 16 killed.** Every claim in these files
now carries its tier inline.

**Three sourcing lessons worth more than any single finding:**

1. 🔴 **Google's PDF model cards are primary sources WebFetch cannot read** — it returns a
   description of the binary. **Download them and use the Read tool.** Both the
   [Veo 3](https://storage.googleapis.com/deepmind-media/Model-Cards/Veo-3-Model-Card.pdf) and
   [Gemini 3 Pro Image](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Image-Model-Card.pdf)
   cards carry limitations and bias disclosures that appear on **no HTML page we had read** —
   the consistency ceiling, the lighter-skin default, spatial-localisation confusion, the
   January 2025 knowledge cutoff, small-text blur at 1K.
2. **Google's marketing blog goes stale faster than its support docs.** A blog.google Flow page
   still says Extend and Jump To *"currently only work with Veo 2"*. On any feature-matrix
   question, **support.google.com and our live account outrank blog.google.**
3. **Corroboration means independent sources, not repeated ones.** Three SEO listicles echoing
   one claim is one source laundered three times.

**What it changed, in order of how much it costs to not know:**

1. **Rule 3 was wrong for two days and is fixed.** The 2026-08-18 correction claiming the
   camera-first formula was ours over-corrected — Google's Cloud Blog publishes that exact
   five-part sequence under *"A formula for effective prompts"*. Re-read at source 2026-08-20.
2. **Lite is a measurably weaker proxy on image-to-video**, which is the path we use on almost
   every shot (rule 5).
3. **`physics-and-motion.md` is new**, because physics is a **storyboard-time** question — is
   this shot possible — not a prompt-writing one, and it now has measured numbers behind it.
4. **Causal chaining** — an official, bracket-free way to get multiple beats inside one
   continuous 8-second take (`video-prompting.md` §5).
5. **The near-black register has a named structural enemy** and a specific prompt-side fix
   (`camera-vocabulary.md`, Lighting).
6. **Seed is a Veo 3 parameter, not a 3.1 one** — a whole plausible-sounding consistency
   workflow that would have wasted a session.

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

## Open questions — only our own testing can settle these

Surfaced by the 2026-08-20 sweep as things **nobody outside has answered**. Ranked by what they
would change. Each is cheap; none has been run.

| Test | What it settles |
| --- | --- |
| **Causal chaining vs bracketed timestamps** — same beat, both ways, one shot | Whether one reads as a continuous take and the other as an internal cut. Both official, neither compared. **The highest-value single test in the list**, because our whole constraint is cutting every 8s |
| ~~**Parallax hinging: motion prompt or source still?**~~ | ✅ **ANSWERED 2026-08-20 — it is the source still.** Veo hinges what is *hinge-able*: give it a bay panel and it rotates that instead of moving the camera; give it a flush sealed hull and it cannot, so it translates. Measured on GPOM scene 0 v2, both targets, same tier, same session. The fix is art direction, not wording — `video-prompting.md` §9 |
| **The near-black recipe, measured on a histogram** — "near-black" as a descriptor vs one-light-plus-stated-falloff vs the same plus a ratio clause | Whether our entire register can reach true black or only muddy grey. Measure it, don't eyeball it |
| **Does Lasso exist in our account?** | Five minutes. Decides whether a good take with one bad region is repairable or a reroll |
| **Repeated negation vs positive description, for subtitles only** | Whether rule 12 has a carve-out for rendering artefacts as opposed to subjects. Rule 12 does not move until it runs |
| **"Imperceptible" vs "slow"** — one prompt, two words, four generations | Our register lives at that end of the scale, so it changes how we write every camera clause |
| **What "Enhance Prompt" actually injects** | Every source confirms it exists; nobody has published a before/after. Rule 15 currently asks people to switch off a black box |
| **Token-count our densest GPOM prompts once** | The cap is 1,024 and Flow shows nothing. Have we ever been silently truncated? |
| **Do fractional beat durations get honoured?** ("Clip 1 (2.5s)") | Distinct from the banned second-level move timing — this allocates shot time to a beat. Untested by anyone |
| **Do named film stocks differentiate**, or collapse to "warm grainy film"? | The photographic mappings are real; whether the models honour the names is untested, including by us |
| **Does extreme-angle framing break identity on our cast?** | Our register uses worm's-eye and bird's-eye deliberately. If true, it is a standing conflict between the look and the consistency discipline |
| **Timestamp-prompting reliability** — the same multi-beat prompt run N times | Nobody has published one. It is a by-product of a normal shoot |

**Two research threads left open**, both needing a browser rather than a fetch:

- **Flow TV publishes the prompt behind each clip** (`labs.google/flow/tv`) — an official, live,
  growing corpus of Google's own prompts. The page is fully client-rendered, so WebFetch returns
  nav chrome and nothing else. A browser session would very likely harvest ten-plus verbatim
  official prompts per channel. **The highest-value unfinished research thread.**
- **The ANCESTRA reference-video motion-transfer technique** — the most literal answer to "exact
  camera movement" the sweep found, and entirely unknown whether it is reachable from the Flow
  app or was a research pipeline Google gave that production.

---

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
JSON-structured prompting — **upgraded 2026-08-20 from a quality judgement to a structural
one: JSON is not a Veo feature at all.** The API's `prompt` parameter is a single plain-text
string, so every "JSON prompting language" is JSON-shaped text stuffed into that one field and
re-parsed as prose. No official Google page describes JSON as a supported prompt format for Veo
or Flow; treat that as a settled negative. Use it for *repeatability of your own authoring*, and
never claim it improves output.

**All numeric performance claims** found in the sweep — "95% subtitle prevention",
"99.8% lip sync", "30%→80% hit rate", "40% of dialogue clips get subtitles" — are
unverifiable single-source figures. They appear nowhere in these files; listed here so
nobody re-imports them. **Added 2026-08-20:** the circulating JSON-vs-prose figures (78% vs 34%
success, 1.6 vs 4.2 iterations, 0.7× token cost) trace to one dev.to post with no shown videos,
no stated success criteria and no methodology behind an unelaborated "50 generations each".

**The bar a number has to clear to appear in these files** is a published methodology and an N.
Three do: the expert-annotated physics benchmark, Google's zero-shot-reasoning paper, and the
five-model CFD-scored comparison — all quoted in [`physics-and-motion.md`](./physics-and-motion.md).
The Veo 3.1 Lite win-rates in rule 5 clear it too. Everything else does not.

**New Tier 1 entries, 2026-08-20:**

- 🔴 **Seed is a Veo 3 parameter, not a Veo 3.1 one.** Google's API docs scope it explicitly —
  *"the seed parameter is also available for **Veo 3** models."* Every "reuse the same seed for
  consistency" workflow being sold for 3.1 is folklore, and one guide selling it admits on the
  same page that the 3.1 upgrade shifted noise schedules and invalidated old seeds. **Do not
  build a reproducibility plan on it.**
- **The Veo prompt field has a hard 1,024-token ceiling** and Flow shows you no count. Our
  longest prompts should be counted once so we know whether we have ever been silently
  truncated. (official, [ai.google.dev](https://ai.google.dev/gemini-api/docs/veo))
- **Lasso** (freehand region edit on a still *or a video frame*) is announced on Google's blog
  and **absent from the current Flow help page**. Verify it exists in our app before planning
  around it — five-minute check, and it decides whether we have a targeted-repair path for a
  good take with one bad region.
- **"Optimal length is 30–80 words"** and "1–3 sentences" are both asserted by practitioner
  pages with no methodology, and they disagree with each other about how much shorter. They do
  not move `video-prompting.md` §2. Listed here so nobody re-imports the figure as fact.

**Tier 3 — live contradictions we picked a side on:**

- **Quote marks vs colon for dialogue.** Google contradicts itself (Cloud Blog uses
  quotes; Vertex best-practices says use a colon). We default to **colon**, because the
  subtitle-burn-in bug is documented and quotes are the strongest "render as text"
  signal. Model-version-sensitive — fall back to quotes if colon fails to trigger speech.
- **Terse command-line prompting with a "Negative Constraints" block** (one guide)
  contradicts Google's conversational-prose guidance across both Veo and Nano Banana,
  and reads as Stable-Diffusion-era practice on a reasoning model. Default to prose,
  and **do not mix the two styles** — that underperforms either alone.
