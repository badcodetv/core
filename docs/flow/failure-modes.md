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

## A5. The four triggers (BadCode's own, from the camping recut)

1. **Real brand names, prominent or repeated** — supermarket fascias, a named car marque
   plus a specific plate, branded totes. Asking for a **legible** real logo or wordmark is
   the most reliable block there is.
2. **Likeness phrasing for faces** — "use this only as a face reference — same face, same
   bone structure" reads as reproducing a specific real person.
3. **Stacked destitution** — burn barrels + tent city + collapsed figures + "gaunt" in
   one prompt, especially alongside a real identifiable business.
4. **Legible text attributed to real institutions** — invented headlines quoting a real
   central bank, government body or newspaper.

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

# Part B — Non-policy failures

These fail silently, as bad output rather than as a block.

| Failure | Detail | Mitigation |
| --- | --- | --- |
| **On-screen text garbles in video** | Signs, labels and lettering morph mid-clip. Nano Banana Pro fixed this for *stills*; it did not carry over to Veo | Any legible text is a still-image job, composited in post. Never trust Veo to hold a word steady |
| **Unwanted burned-in subtitles** | Documented, Google-acknowledged, partially fixed. Learned from caption-heavy training video | Colon dialogue syntax + "(no subtitles, no captions, no on-screen text)" + a negative-field list. Google's own workaround is "try the prompt again" |
| **Hands and fingers** | Finger articulation and precise small-object manipulation remain unreliable in 3.1 | Keep hands distant, partially occluded, or out of frame. Never make hand detail a hero shot |
| **Physics** | Water splashes read too light, cloth doesn't respond to movement, momentum doesn't transfer | Avoid shots whose point *is* correct physical weight — a whip crack, a heavy drop, billowing fabric |
| **Audio lottery** | Dialogue and audio come back garbled or wrong at a materially higher rate than picture fails | Treat picture and audio as semi-independent rolls. Budget audio-only rerolls; keep a re-voice-in-post fallback |
| **Multi-action mush** | "Wakes up, gets dressed, eats breakfast, leaves, drives to work" in one prompt → choppy movement, inconsistent character and lighting, objects appearing and vanishing | One beat per clip. Chain, or use timestamp prompting |
| **Silent output** | Often not a prompting error — wrong generation mode or wrong plan tier. Speech in Flow is experimental and gated | Check mode and tier before rewriting the prompt |
| **Identity drift** | Faces silently substituted with a generic default, especially across iterations | Reference hygiene (`consistency.md` §2), identical wording every prompt, manual QA on hero shots |
| **Compounding drift down an Extend chain** | Each extension inherits the last one's error as evidence | Review every extension before chaining. Roll back, don't push through |

*(The specific "silent generic-avatar substitution, unfixed across all model variants"
framing of identity drift traces to a single developer-forum thread with no Google
acknowledgement. That drift happens at all is well corroborated; that exact mechanism is
not.)*

---

## Our own automation failure modes

Not Flow's fault, but they present identically. Full detail in
`docs/superpowers/flow-selectors.md` and `packages/flow-mcp/README.md`:

- **A wedged asset picker** from a failed upload survives retries and poisons the next
  call. Reload the project URL — twice; Flow intermittently throws a client-side
  exception on first load.
- **Stale-tab drift** — calls land on a tab left open at a different project.
- **Multiple references or references over ~1 MB** are the two known causes of upload
  timeouts. Downscale to ~1600px and pass exactly one.
- **The model picker resets to Nano Banana 2 on every navigation.**
