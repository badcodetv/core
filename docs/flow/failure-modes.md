# Failure modes — policy blocks and quality failures

The single biggest time sink in Flow work. Over half of all generations on the camping
recut were **blocked, not slow**.

---

# Part A — Policy blocks

## A1. What a block looks like

In the browser, a red warning card. The reported strings:

> "Failed: This Prompt Might Violate Our Policies About Generating Prominent People.
> Please Try a Different Prompt or Send Feedback."

> "This generation might violate our policies. Please try a different prompt or send
> feedback"

**Over the flow-mcp tools a block presents as a TIMEOUT, not an error** — the generation
simply never completes and no candidate lands. This is why the natural instinct is
wrong: retrying burns ~90s a go on a prompt that can never pass.

**Diagnosis rule:** two failures with no candidates, while the session is otherwise
healthy (`flow_status` fine, project loads, other prompts succeeding) = **policy block.
Rewrite; do not retry.** Glance at the Flow window to confirm.

⚠️ **Refined 2026-08-18: a policy block is the most likely cause of a candidate-less failure,
not the only one.** Google documents three other faults that also return nothing —
audio-generation failure, rate limiting, and "unusual activity" — and they need opposite
responses (wait, or retry unchanged) to a block (rewrite). **Look at the Flow window before
rewriting**, because the card names which one it is and the tools cannot. See Part B0.

*(Known gap: flow-mcp does not yet distinguish a block from a timeout or return a
distinct `POLICY_BLOCKED` code — see `packages/flow-mcp/README.md`.)*

## A2. Every field Flow reads is scanned, not just the prompt box

**Learned live 2026-08-12, and it cost us a morning.** A Flow **Character named
"Keynes"** had every generation refused, including a body-generation whose prompt text
named nobody. Renaming the Character to "Economist" and re-running the *identical* prompt
succeeded immediately.

So the scan surface includes at least:

- the prompt box
- **the Character Name field**
- Character Info (assume so; not isolated in testing)
- **the uploaded reference image itself** — a block can survive a total text rewrite if
  the image carries the detected logo, the celebrity-resembling face, or the trigger

Never put a real person's name in *any* Flow field. Describe build, era dress and
bearing instead, and name the Character something generic.

**⚠️ It is not only real names — any trigger word in the Name field is permanent**
*(2026-08-24)*. Camping's ruined-Tarquin Character was called `@homeless-Tarquin`, which
puts [trigger 3](#a5-the-five-triggers-badcodes-own) — destitution — into **every prompt
that casts him**, in a field nobody re-reads. Renamed to `@Future-Tarquin`: same character,
same sheet, and the condition word is gone from the field while the story keeps it.

**The rule that generalises: name a Character for *when* or *who*, never for their
condition.** A Character Name is written once and then silently prepended to a hundred
generations, so it is the worst possible place to spend a trigger. Era, role and story
position — `Future`, `City`, `Young` — all cost nothing.

## A3. Harm categories

Vertex surfaces 8-digit support codes under named categories: Violence, Sexual, Hate,
Child, Celebrity, PII, Toxic, Vulgar, Dangerous, Prohibited. The **taxonomy** is
trustworthy; the specific code digits circulating in third-party tables are not verified
against any Google-published list.

### A3b. Naming a real person is not a uniform trigger (tested 2026-08-12)

Two deliberate probes, same tool, same project, minutes apart:

| Prompt | Result |
| --- | --- |
| photorealistic portrait of **Winston Churchill** at a desk, 1942 | **generated**, 29s |
| photorealistic portrait of **Taylor Swift** at a desk | **blocked**, 19s |

So the **Celebrity** category is doing the work, and it lands hardest on **living public
figures**. A long-dead historical figure may well pass.

**This does not soften the guardrail** — keep real names out of every field. Two reasons the
success is worth less than it looks: what passes today is a moving target, and the block we
actually lost a morning to was fired by a **Character Name**, where a refusal poisons every
generation that casts it rather than just one prompt. Treat "it went through" as luck, not
permission.

Practical upshot for **testing** our own tooling: a living celebrity is the reliable trigger.
A historical name is not, and will silently produce a real image and a real credit spend.

## A4. The debugging procedure

1. **Turn off "Enhance Prompt" first.** Flow's auto-rewrite injects descriptive language
   you never wrote, which then trips the filter. A plain prompt that gets blocked is
   often blocked for words the enhancer added.
2. **Binary-search by subtraction.** Strip to "a person walking in a street", confirm it
   passes, add adjectives back one at a time until it fails.
3. **Check the reference image separately from the text** (see A2).
4. **Rewrite; don't re-roll.** Retrying identical text is wasted credits and wasted
   minutes.

## A5. The five triggers (BadCode's own)

Numbers 1–4 come from the camping recut; **number 5 was added 2026-08-16** from the
Karen §2h.4v clip.

1. **Real brand names, prominent or repeated** — supermarket fascias, a named car marque
   plus a specific plate, branded totes. Asking for a **legible** real logo or wordmark is
   the most reliable block there is.
2. **Likeness phrasing for faces** — "use this only as a face reference — same face, same
   bone structure" reads as reproducing a specific real person.
3. **Stacked destitution** — burn barrels + tent city + collapsed figures + "gaunt" in
   one prompt, especially alongside a real identifiable business.
4. **Legible text attributed to real institutions** — invented headlines quoting a real
   central bank, government body or newspaper.
5. **A word with a sexual second meaning, in a setting that supplies the first one.**

### A5b. The bedroom problem — trigger 5 in detail

**Karen §2h.4v, 2026-08-16.** A clip of Susan waking up to a ringing phone was blocked.
Nothing in the scene is remotely sexual: she is fully dressed, face-down, alone, and the
entire action is reaching for a phone. **The word was `gropes`** — *"her hanging arm
swings up and **gropes** blindly along the edge of the mattress."*

This is [A6](#a6-rewrite-patterns)'s mechanism — *"the filter scans individual keywords,
not overall intent"* — with one thing added that the existing list did not say:

> **Context does not protect a word; it convicts it.** The advice so far was that words
> with a violent second meaning false-positive *in wholly innocent contexts*. That
> undersells it. `grope` in a kitchen is a fumble; `grope` on a bed with a woman on it is
> the classifier's other reading, because **the setting supplies the missing half of the
> phrase.** Google's own filter list names *sexual* alongside violence, derogatory and
> toxic `[vendor]`.

**So audit for the pair, not the word.** Before firing any bedroom, bathroom, shower or
undressing scene, read the block back asking which words would look bad *quoted next to
the location* — and swap them even where you are sure of your own meaning.

| In a bedroom scene, instead of | Write |
| --- | --- |
| gropes / gropes blindly | feels its way along, patting at |
| lying on her front | lying face-down across the bed |
| a breath in through her nose *(audio)* | cut it — a breath track over a woman on a bed buys nothing |
| stripping / strips off | changing out of, pulling off a jumper |
| moans / groans | *(name the sound: a sigh, a low sound in her throat)* |

**None of the three changes we made were diagnosis** — only `gropes` was suspected. The
other two were dropped because **they cost nothing and they were adjacent**, which is the
right posture: on a scene the filter is already primed for, do not spend generations
defending a clause you do not need.

## A6. Rewrite patterns

The filter scans **individual keywords, not overall intent.** Words with a violent second
meaning ("shoot", "execute", "strike", "strip") false-positive in wholly innocent
contexts.

**BadCode's table** (from `badcode-art-direction`, our own evidence):

| Instead of | Write |
| --- | --- |
| "Waitrose storefront, green signage" | "an upmarket supermarket fascia in green and white, lettering indistinct" |
| "Waitrose Bag for Life totes, wordmark legible" | "heavy-duty reusable grocery totes in supermarket green" |
| "black BMW X7, plate T4RQ 1N" | "a large black luxury SUV, private plate" |
| "same face, same bone structure as the reference" | "keep this character's design consistent with the reference — same hairstyle, build, colouring and wardrobe" |
| "gaunt, squalid, collapsed among rubbish" | "weary, worn, sitting among the debris" |
| headline text quoting a real bank | describe the newspaper; put the actual line in a `NarrationBox` overlay in the comic |

**From the wider research:**

| Situation | Rewrite to |
| --- | --- |
| Real or named person | A fictional character plus explicit non-resemblance: "Show a fictional adult creator… **Do not resemble any real person.**" |
| Testimonial with a real face | "Use a fictional actor in testimonial format" |
| Real brand or logo | "…a **fictional device shape and no real logos**." Generic swaps: "a generic storefront sign", "unlabeled packaging" |
| Celebrity voice or real song | "a warm, neutral adult narrator with a clear studio tone" — push licensed music and final VO into post |
| Age-loaded language | Remove the age descriptor ("young") and the named family relationship. The classifier fuzzy-matches on young/teen/child and flags any subject who *could* be a minor, regardless of context |

⚠️ The widely-circulated specific substitution table ("fire"→"burning logs",
"shot"→"photograph", "strike"→"impact") is **one site's invention** — another guide gives
different substitutes for the same words. The *mechanism* is corroborated; those exact
mappings are not. Substitute by meaning, in context.

**Hard limit, no rewrite exists:** uploaded images containing real minors are a
zero-tolerance block on the image content itself. No caption change fixes it.

### ⚠️ Synthetic-news trigger — *"may cause reputational risk or misrepresent current events"*

**Observed 2026-08-19 (Karen §3a.5v).** A clip of a woman with a microphone talking to camera on
a street was refused. **The picture was not the problem — the vocabulary was.** *Reporter*,
*live television report* and *news van* together describe fabricated broadcast footage, one of
the highest-risk categories in any content policy.

**Rewrite: keep the journalism in the picture, take it out of the prompt.** The still already
carries the microphone, the crew light and the van; the engine only needs to know how things
*move*.

| Says | Write instead |
| --- | --- |
| a television reporter | the woman in the dark coat at the front |
| talking to camera / reporting live | talking, facing the front |
| a news van | the van at the kerb |
| the clipped rhythm of a live report | talking steadily and clearly |

### ✅ The fix that worked: **assert a benign category, do not just delete the risky one**

**Ruled 2026-08-19 (Kai) after four refusals.** Deleting every journalism word was **not enough** —
the classifier still inferred *news* from the microphone, the mast and a speaking woman, and
refused. What cleared it in one shot was **renaming the whole scene**:

> This is a behind-the-scenes shot of **a film crew shooting a scene for a movie** on a street.

Then every noun follows: **actress**, **crew**, **camera operator**, **boom pole**, **production
van**, *"delivering her lines."* Identical picture, identical movement, different category.

**House rule from here: never write "news", "reporter", "broadcast", "live" or "television" in a
BadCode prompt.** Any crew in any BadCode shot is a **film crew** — that is what we call them
now, in every prompt and every plate.

**Generalise it:** when a block will not clear by deletion, **give the classifier a different
frame rather than a smaller one.** Deletion leaves it to infer, and it infers the risky reading;
assertion tells it what it is looking at.

⚠️ **Act 4 will hit this much harder** — a TV studio with a president on air. Same rule: a studio
is *"a room with lights and cameras"*, a president is *"a man in a suit behind a desk"*. The
image may be as journalistic as you like; the prompt may not.

### ⚠️ False positives on crowd uploads — *"We do not allow uploads of minors at this time"*

**Observed 2026-08-19 (Karen §3a.4c-v).** An AI-generated high-angle crowd of adults was
refused on upload. **The age classifier runs on faces, and low-resolution faces read young** —
at that distance each face is a few dozen pixels, so there is not enough detail to judge age
and the classifier defaults to *could be a minor*. Nothing in the picture was a child.

**Fixes, cheapest first:**

1. **Upscale before uploading.** Counter-intuitive and the most direct fix: bigger faces give
   the classifier the detail it needs.
2. **Crop the edges** — the smallest, most distant figures are the trigger.
3. **Re-export** (PNG↔JPEG, resize a few percent) for a fresh classifier pass.
4. **Try another candidate** from the same generation; face sizes vary.
5. **Do not animate it.** Use the frame as a held still.

**Prompt-side prevention for crowd plates: write the crowd as explicitly adult.** *"People of
all ages"* invites the flag; *"adult New Yorkers, office workers and commuters of all adult
ages"* does not. Same mechanism as the age-loaded-language row above, applied to groups.

## A7. Two structural rules that make blocks rare

**Load-bearing text belongs in the comic, not the image.** If a sign or headline must be
readable for the story to work, render it as a bubble or narration overlay in
`@badcode/comic` — sharper, editable, translatable, and it cannot be blocked.

**Brand usage is also a publication question**, separate from whether it generates.
Panels carrying real signage are a release decision for Kai.

## A8. Billing under a block — undocumented

Google documents no HTTP status codes or billing treatment for a prompt blocked
pre-generation, an output blocked post-generation, or a partially-blocked batch. An open
developer-forum question asking exactly this has no official reply. **Build retry and
cost logic defensively — you may be billed for a generation you never see.**

---

# Part B0 — The other empty results (2026-08-18)

Added after reading Flow's own FAQ. Every one of these returns **no candidate**, exactly like a
policy block, and every one wants a different response. Getting this wrong costs either a
rewrite you didn't need or a retry that can never pass.

| The card says | What it is | What to do | Credits |
| --- | --- | --- | --- |
| **"Audio Generation Failed"** | Veo 3.1 blocked its own output because the *audio* stage failed or tripped safety — *"sometimes Veo can produce low-quality audio, in which case your video will not be generated"* | **Retry unchanged, or reprompt.** This is a lottery, not a verdict on your prompt | refunded |
| **"You're requesting generations too quickly"** | Rate limiting, which tightens as the day's volume grows and bites hardest on zero-credit models | **Wait.** Slow the batch; don't rewrite anything | n/a |
| **"We noticed some unusual activity"** | Anti-abuse | Retry after a couple of minutes; **disable any VPN or proxy** | n/a |
| **A stuck "Pending" card** | A generation that failed on policy or credits and left a husk | Check the top-right for a system notification, then **manually retry or delete the card** — it will not clear itself | — |
| *(silently the wrong model)* | Flow auto-switches you to a compatible model when the selected one lacks a feature you used | Read the model back off the compose bar. See [`platform-controls.md`](./platform-controls.md) §1 | you paid for whatever ran |

**The audio one matters most to us**, and it is a small nasty irony: BadCode never uses Veo's
audio — the track is Suno's and we strip the AAC in post — but the audio stage can still kill a
picture take we wanted. That is the concrete reason to write one short audio line into every
prompt even though the track is going in the bin (`video-prompting.md` §6): an unspecified
soundscape is the one most likely to come back unusable and take the picture with it.

**Two of these five also explain a fault we have already hit.** The stuck-Pending row is the
junk we found sitting in the gallery on 2026-08-18 masquerading as returned generations; the
model-auto-switch row is why Extend arrives pinned to Lite.

---

# Part B — Non-policy failures

These fail silently, as bad output rather than as a block.

| Failure | Detail | Mitigation |
| --- | --- | --- |
| **On-screen text garbles in video** | Signs, labels and lettering morph mid-clip. Nano Banana Pro fixed this for *stills*; it did not carry over to Veo | Any legible text is a still-image job, composited in post. Never trust Veo to hold a word steady |
| **Unwanted burned-in subtitles** | Documented, Google-acknowledged, partially fixed. Learned from caption-heavy training video | Colon dialogue syntax + "(no subtitles, no captions, no on-screen text)" + a negative-field list. Google's own workaround is "try the prompt again". **And build the escape hatch into the composition** — leave dead space at the bottom of frame on any dialogue clip, enough that cropping *"the bottom 12–18% of the frame"* removes a stray caption without costing the shot |
| **Hands and fingers** | Finger articulation and precise small-object manipulation remain unreliable in 3.1 | Keep hands distant, partially occluded, or out of frame. Never make hand detail a hero shot |
| **Physics — measured, not impressionistic** | An expert-annotated benchmark (10,990 traces, 22 categories, 5 models) found **79.4%** of Veo 3.1 Fast exocentric clips carry at least one human-identifiable physics glitch; egocentric **97.5%**. Google's own zero-shot paper shows the unevenness on Veo 3: optical strong (0.92), buoyancy 0.58–0.83, gravity-driven trajectory **~0.5** | Avoid shots whose point *is* correct physical weight. Full craft treatment, with the paste-ready stability clause, in [`physics-and-motion.md`](./physics-and-motion.md) |
| **Periodic motion drifts mid-clip** | The first cycle of a repeated impact reads correctly and later repetitions lose height, timing and rotation. Tested on "Basketball bouncing on pavement": *"the first bounce looked correct, but subsequent bounces showed incorrect height trajectories and unrealistic ball rotation"* | Ask for **one impact, not a rhythm**. If a shot needs repetition, cut at the first cycle |
| **Inertia-blindness, specifically** | Not "water reads light" generally. A five-model, 50-identical-prompt, 250-output comparison scored by a CFD PhD candidate (Cohen's κ 0.84) found Veo among the *strongest* at gravity-driven water — *"water pooling, spreading, and dripping off the table edge with simulated surface tension"* — but *"No model passed the 'glass of water in a moving car' test — water should slosh in response to acceleration… all models produced static water in a moving environment"* | Gravity-driven liquid is fine. Anything that must respond to the **frame's own acceleration** is out |
| **Default lighter-skin casting** | Not a glitch, a documented bias: *"we noted that Veo 3 appears to skew towards lighter skin tones when race is not specified in the prompt. Testing also surfaced risks of semantic bias where particular terms are spuriously correlated with representation of particular demographics"* | State skin tone and ethnicity explicitly in every character prompt and in the DNA block. **Omission is not neutrality** |
| **Audio lottery** | Dialogue and audio come back garbled or wrong at a materially higher rate than picture fails | Treat picture and audio as semi-independent rolls. Budget audio-only rerolls; keep a re-voice-in-post fallback |
| **Multi-action mush** | "Wakes up, gets dressed, eats breakfast, leaves, drives to work" in one prompt → choppy movement, inconsistent character and lighting, objects appearing and vanishing | One beat per clip. Chain, or use timestamp prompting. **The mechanism is averaging, not selection** — *"The model averages everything and produces a muddled drift"* / *"over-specifying tends to produce rubbery results where the subject is trying to do too much in too little time"*. Which is why the fix is subtraction |
| **Silent output** | Often not a prompting error — wrong generation mode or wrong plan tier. Speech in Flow is experimental and gated | Check mode and tier before rewriting the prompt |
| **Identity drift** | Faces silently substituted with a generic default, especially across iterations | Reference hygiene (`consistency.md` §2), identical wording every prompt, manual QA on hero shots |
| **Compounding drift down an Extend chain** | Each extension inherits the last one's error as evidence | Review every extension before chaining. Roll back, don't push through |

*(The specific "silent generic-avatar substitution, unfixed across all model variants"
framing of identity drift traces to a single developer-forum thread with no Google
acknowledgement. That drift happens at all is well corroborated; that exact mechanism is
not.)*

**Source upgrade, 2026-08-20 — the limitation itself is no longer forum-tier.** Google's own
Veo 3 model card, explicitly versioned forward to cover *"Veo 3 and subsequent versions"*,
states: *"While Veo 3 demonstrates incredible progress, creating realistic, dynamic, or intricate
videos, maintaining complete consistency throughout complex scenes or those with complex motion,
remains a challenge."* Be precise about what that buys: Google's wording is **complex scenes /
complex motion**, not the substitution mechanism. The narrower generic-avatar claim stays
forum-tier. (official,
[Veo 3 model card](https://storage.googleapis.com/deepmind-media/Model-Cards/Veo-3-Model-Card.pdf))

**Corroboration for the silent model swap.** An independent production account of a finished
36-second short reports the same class of fault unprompted — *"Flow (Google's 'filmmaker tool')
silently defaulted me to the inferior Veo 2"*. The mechanism differs (an unprompted default, not
a feature-triggered swap), so it corroborates the *behaviour*, not the documented trigger.
(corroborated, [nataliaburina.substack.com](https://nataliaburina.substack.com/p/creating-a-36-second-ai-film-took))

## Repair before you reroll

Two targeted edit paths make some bad takes salvageable instead of discardable.

- **Insert** adds a missing or wrong prop into an already-generated clip and *"handles complex
  details like shadows and scene lighting, making the addition look natural"*.
- **Lasso** takes a freehand region on a still **or a video frame** plus a plain-language change
  (*"remove the man"*, *"add Koi fish in the water"*); on video it *"intelligently applies your
  described change consistently across the relevant portion of the clip, maintaining continuity
  of motion, lighting, and physics."*

🔴 Lasso is blog-announced and absent from the current Flow help page — **check the live app
first**. ⚠️ Neither works on an extended clip ([`consistency.md`](./consistency.md) §7).

*(official, [blog.google](https://blog.google/innovation-and-ai/products/veo-updates-flow/) and
[blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates-february-2026/))*

---

## Our own automation failure modes

Not Flow's fault, but they present identically. Full detail in
`docs/flow/automation-images.md` and `packages/flow-mcp/README.md`:

- **A wedged asset picker** from a failed upload survives retries and poisons the next
  call. Reload the project URL — twice; Flow intermittently throws a client-side
  exception on first load.
- **Stale-tab drift** — calls land on a tab left open at a different project.
- **Multiple references or references over ~1 MB** are the two known causes of upload
  timeouts. Downscale to ~1600px and pass exactly one.
- **The model picker resets to Nano Banana 2 on every navigation.**

---

## Sources

Part A's triggers and rewrites are **ours**, measured on the camping recut and dated in place.
Part B0 is Google's, re-read at source on **2026-08-18**:

- [Get started with Google Flow — FAQ](https://support.google.com/labs/answer/16353333?hl=en) — the audio-generation failure, rate limiting, unusual-activity, pending cards, model auto-switching, and "you are not charged for failed generations".
- [Generate videos with Veo 3.1 — Gemini API](https://ai.google.dev/gemini-api/docs/veo) — *"Veo 3.1 will sometimes block a video from generating because of safety filters or other processing issues with the audio. You will not be charged if your video is blocked from generating."*
- [Video generation prompt guide — Google Cloud](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide) — the safety-filter section and the abuse-report route.

⚠️ **A8's "billing under a block is undocumented" is now partly answered** — Google states
plainly that failed generations are not charged, both in the Flow FAQ and in the Veo API docs.
What remains undocumented is the *partially*-blocked batch and post-generation output blocking.
Keep the defensive retry logic; drop the assumption that a block costs money.

**Added by the 2026-08-20 ten-angle sweep:**

- [Veo 3 model card — DeepMind](https://storage.googleapis.com/deepmind-media/Model-Cards/Veo-3-Model-Card.pdf) — the consistency limitation and the lighter-skin default. 🔴 WebFetch cannot read it; download and Read.
- [Expert-annotated physics benchmark](https://arxiv.org/html/2603.19607v1) · [Video models as zero-shot reasoners](https://huggingface.co/papers/2509.20328) · [AI video models compared](https://www.lovart.ai/blog/ai-video-models-compared-2026) — all three publish a methodology and an N, which is why their numbers are quoted here at all. See [`physics-and-motion.md`](./physics-and-motion.md).
- [Veo updates in Flow](https://blog.google/innovation-and-ai/products/veo-updates-flow/) · [Flow updates, February 2026](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates-february-2026/) — Insert and Lasso.
