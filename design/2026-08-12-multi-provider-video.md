# Multi-provider video & image generation

**Status: PARKED** (Kai, 2026-08-12) — researched, planned, not built. No code was written.
**Date:** 2026-08-12

> **Why parked.** The economics don't work yet. Seedance is metered per second of output;
> Google's Ultra plan gives us a generous token allowance, so **iteration is free at the
> margin on Flow and billed per attempt on Seedance**. That is the whole argument, and it
> holds even at the cheapest verified rate — because we don't make one clip, we make six and
> keep one. Add the unproven upside (§5b: 720p ceiling, no still images, no character object,
> and the audio feature that prompted this whole thread still unverified) and there is nothing
> here worth paying for today.
>
> **Revisit if any of these change:**
> 1. Seedance ships **1080p or better** on a live schema (today every one caps at 720p).
> 2. Someone confirms an uploaded audio track survives **verbatim** into the output rather
>    than only conditioning timing — the one capability Flow genuinely cannot match.
> 3. Our Google allowance stops covering the work, or we need **unattended/headless** runs
>    that a browser puppet can't do.
>
> Cheapest way to reopen door 2: ~six 480p clips, about **$6**. Not $20, and not at 720p.
> Everything below is preserved as-is for whoever picks this up.

## 1. The problem

We generate every comic panel, character reference and video clip through **Google Flow**,
driven by `@badcode/flow-mcp` — an MCP server that puppets a real logged-in Chrome over CDP.
It works well, and it is the only way to reach Veo 3.1 and Nano Banana Pro without an
enterprise contract. But it is a browser: it needs a logged-in window, it breaks when the DOM
drifts, it can't run headless on a schedule, and it is single-tenant by construction.

**Seedance 2.5** (ByteDance) has arrived with capabilities we want — notably, it is reported to
accept an **audio clip as input**, which for a collective that scores everything to its own
drum & bass would be a step change. More importantly it appears to be reachable over a **plain
HTTP API**, which removes the browser from the loop entirely.

So the real decision is not "add Seedance". It is: **we now need more than one video/image
provider, and the pipeline should not care which one it is talking to.**

## 2. The constraint that shapes everything (Kai's ruling, 2026-08-12)

> "I'm not that fussed by reusing code from flow-mcp. It would be almost better that we don't
> try to merge that code together — both will have very different opinions about how the
> interactions are. One is a browser and the other is an API. The things I'm trying to bring
> over are the *tool list* — because that's all of the things you can do as far as the
> language model is concerned."

**Therefore:**

- **No shared implementation.** No common base class, no extracted "driver" abstraction, no
  refactor of `flow-mcp`. A CDP puppet and an async HTTP job queue have nothing useful in
  common below the surface, and forcing them to share would make both worse.
- **`flow-mcp` is not touched.** It stays exactly as it is, on its own release track.
- **The thing we port is the *contract*** — the tool list, its argument shapes, and its error
  vocabulary. That is the entire API as far as an agent is concerned.
- Convergence, if any, happens later and only at the *skill* layer (a prompt-craft knowledge
  base per provider), never in the servers.

## 3. The contract to port — the flow-mcp tool list

This is the full capability surface of `@badcode/flow-mcp` as an LLM sees it (17 tools,
ground truth `packages/flow-mcp/src/server.ts`). Any new provider is measured against this
table, column by column. "Must" = the pipeline breaks without it.

### 3a. Session & bookkeeping — *browser-only, expected to vanish*

| Tool | What it does | Port? |
| --- | --- | --- |
| `flow_status` | Is the browser attached and logged in | ❌ meaningless for an API — replaced by a key/credit check |
| `flow_open_project` / `flow_list_projects` / `flow_create_project` | Flow's project container | ❌ an API has no project state; our own output dirs are the container |
| `flow_list_media` | Enumerate the project gallery | ⚠️ only if the provider stores assets server-side |

These four exist purely to manage Flow's stateful UI. A stateless API deletes most of this
category, which is the single biggest simplification on offer.

### 3b. Images — *must port*

| Tool | Arguments that carry meaning | Notes |
| --- | --- | --- |
| `flow_generate_image` | `prompt`, `outPath`, `character?`, `numOutputs 1–4`, `model`, `aspect` (14 ratios) | The everyday panel generator |
| `flow_edit_image` | `prompt`, `referenceImages[1–3, in practice 1]`, `outPath`, `numOutputs` (default 2), `character?` | Reference-anchored **delta** edit — always from the golden original, never a chained edit |
| `flow_refine` | `prompt`, `outPath` | Follow-up correction **carrying session context**. Cheap because it re-navigates nothing. An API has no session — this may become "re-send with the previous output as reference", which is a different, more expensive thing. Flag as a semantic gap. |
| `flow_generate_batch` | `prompts[≤20]`, `outDir`, `character?`, `resume?` | Serial batch with **resume-from-disk** — the property that makes long unattended runs survivable. Provider-agnostic; belongs in every server. |

### 3c. Video — *must port, this is the point of the exercise*

`flow_generate_video({ startImage?, endImage?, motion, model, aspect, count, durationSeconds })`

One tool, **three source modes** selected by which images are passed:

| Mode | Passed | Prompt should describe |
| --- | --- | --- |
| image→video | `startImage` | what MOVES |
| first+last frame | `startImage` + `endImage` | ONLY the camera move connecting them |
| text→video | neither | the whole shot |

Plus the per-tier capability rules we learned the hard way: `endImage` needs a Veo 3.1 tier;
10s clips are Omni Flash only; durations are a fixed set (4/6/8/10), not a slider. **Every
provider will have its own version of these rules, and they must fail *before* spending money**
— that discipline is worth more than the tool signature.

**Seedance-specific additions to design for:** an `audio` input parameter (if real), and
whatever multi-shot / multi-reference conditioning it exposes. These have no Flow equivalent,
so the contract has to *grow*, not just be mirrored.

### 3d. Characters — *the hard one*

Flow gives us a **server-side, named, reusable identity object**: a Character with a Portrait
view, an optional full-body view, and a free-text note the scene agent reads on cast. Seven
tools operate on it (`flow_create_character`, `..._from_media`, `flow_character_body`,
`flow_edit_character`, `flow_character_info`, `flow_list_characters`, `flow_get_character`).

This is almost certainly **not** something a raw API provides. If identity has to be
maintained by passing reference images on every call, then the equivalent must be built
**client-side**: a local character registry (name → reference images + body shot + info text)
that the server expands into per-call references. That is a real piece of design work and
probably the largest single item in the build.

### 3e. Errors — *the underrated part of the contract*

`flow-mcp` returns `{ error: true, code, message, hint }` with ~20 branchable codes. The two
that carry the most operational weight:

- **`POLICY_BLOCKED`** — a content refusal, distinguished from a timeout, returned in seconds,
  and **never retried**. More than half of our Flow prompts get silently policy-blocked, and
  the block looks exactly like a timeout unless you classify it. Any new provider needs the
  same treatment on day one or we will burn hours re-learning this.
- **Pre-flight capability errors** (`VIDEO_DURATION_UNAVAILABLE`, `VIDEO_FRAMES_UNAVAILABLE`,
  `ANIMATE_WRONG_SOURCE`) — refuse *before* generating, because a wrong-but-healthy-looking
  clip costs credits and is worse than a failure.

## 4. Research in flight

A 10-agent Sonnet web-research fan-out is running (workflow `wf_50b4adb3-b91`), in two tracks:

**Track A — API & providers**
1. First-party API (Volcengine Ark / BytePlus ModelArk): model ids, endpoints, auth, pricing, UK access
2. Third-party hosts (fal.ai, Replicate, Freepik, Kie.ai, WaveSpeed, Segmind, PiAPI, AI/ML API, …): price/unit, features exposed, signup friction
3. Feature matrix: video modes, first+last frame, multi-reference, audio input, durations, resolutions — head-to-head vs Veo 3.1
4. Image side (Seedream / SeedEdit): editing, multi-ref consistency, and whether any persistent Character equivalent exists
5. Integration engineering: job lifecycle, URL expiry, moderation codes, TS SDKs, existing open-source MCP servers

**Track B — prompt craft** (to become `docs/seedance/`, mirroring `docs/flow/`)
1. Official prompting guidance + in-prompt parameter tokens
2. Camera & motion vocabulary with reliability tiers
3. Character/style consistency across shots; first+last-frame practice
4. Audio — supplying a track vs. generating dialogue/SFX
5. Failure modes, moderation triggers, and honest Seedance-vs-Veo comparison

Findings land in §5–§7 below.

## 5. Findings

Full briefs: [`research/2026-08-12-seedance-2-5/api-and-providers.md`](./research/2026-08-12-seedance-2-5/api-and-providers.md)
and [`prompt-craft.md`](./research/2026-08-12-seedance-2-5/prompt-craft.md). 10 research agents,
387 tool calls, every claim tagged verified / likely / unverified with sources. Distilled:

### 5a. The good news

- **Seedance 2.5 is real and callable today.** Model ids `dreamina-seedance-2-5-260628`
  (BytePlus international, `ap-southeast-1`) and `doubao-seedance-2-5-260628` (Volcengine
  China). GA, not a waitlist. Multiple independent hosts confirm a working schema.
- **The API removes the browser.** `POST /api/v3/contents/generations/tasks` → task id →
  poll or webhook → signed video URL. Stateless, headless, schedulable. That alone is worth
  the exercise.
- **Video modes match our contract exactly.** Text→video, image→video, and first+last frame
  (`image_url` + `end_image_url`) are all first-class. Duration is 4–30s at **integer-second
  granularity**, against Flow's fixed 4/6/8/10 enum. Seven aspect ratios against our two.
- **References are far richer than Flow's.** Up to ~50 conditioning assets (reported 30
  image / 10 video / 10 audio) against `flow_edit_image`'s practical limit of **one**.
- **`return_last_frame: true`** hands back the closing frame of a clip — exactly the input
  needed to chain the next shot. Flow has no equivalent; we screenshot.
- **No signup wall on the resale route.** fal.ai and Replicate are card-and-go. The official
  BytePlus route needs business real-name verification and a $30 minimum balance.
- **Moderation is structurally kinder to us than Flow's.** BytePlus's Content Pre-filter is a
  face/voice *similarity* check against real public figures — it is not a topic filter. Our
  register (near-black, non-photoreal, fictional archetypes — the Emperor, not a sitting head
  of state) sits outside what it is built to catch. Given that >half our Flow prompts get
  silently policy-blocked, this could be the quiet win of the whole migration.

### 5b. The bad news — read before getting excited

🔴 **The audio feature that prompted this whole thread is UNVERIFIED in the way that matters.**
Two separate things exist and the research could not separate them from documentation alone:

- `generate_audio: true` (a real, documented boolean) makes the model synthesise its **own**
  audio — dialogue, lip-sync, SFX, ambience — jointly with the video. That is confirmed.
- `audio_urls` reference input (up to 10 files, reportedly ≤30s combined) conditions
  **pacing, beat-matching and lip-sync** to a supplied track.

**Nobody could establish whether an uploaded track survives verbatim into the output, or is
merely a timing/style signal while the model synthesises its own (re-interpreted, lower
fidelity) audio.** "Feed it our drum & bass master and get motion cut to it" is therefore
*plausible but unproven*. This is not settleable from docs. It needs one paid test clip.

🔴 **Resolution caps at 720p on every live schema checked.** The "native 30s 4K" line is
marketing; both the BytePlus schema and fal.ai's schema expose **480p / 720p only** — and
Seedance *2.0* on the same host exposes 1080p, so 2.5's live surface is currently *narrower*
than its predecessor. For a comic pipeline whose goldens are 5504×3072 stills, a 720p ceiling
is a genuine downgrade on the video side.

🔴 **Seedance does no still images at all.** It is video-only. Panels, character portraits and
delta edits would need **Seedream 4.x / SeedEdit** — a structurally separate model family
(same platforms, different endpoints, different prompt craft). "Replace Flow with Seedance" is
therefore two integrations, not one.

🔴 **No character object, anywhere in the ByteDance stack.** Confirmed independently for both
the video and image sides. Identity is maintained by re-attaching reference images every call
and binding them **in prose** (`@Image1` / `[Image1]` tags, plus an explicit "preserve the coat,
badge, hair from [Image1]" clause). Every one of our seven character tools has to be rebuilt
client-side. Third-party wrappers advertising a `@character:` primitive are inventing it.

⚠️ **Other contract gaps:** no session/`refine` (stateless — a follow-up means a fresh full
prompt re-referencing the prior asset, at full price); **no multi-output per call** (`count:
1–4` becomes N separate billed calls); no project/gallery concept; **no idempotency key** on
task creation, so a retried POST after a network timeout may bill twice.

⚠️ **Output URLs expire: 24 hours, max 100 downloads.** Harvest immediately; never store the
URL as a reference.

### 5c. Cost reality — the reason this is parked

**Verified first-hand 2026-08-12** (not agent-reported — read off the live pages):

| Route | 10s @ 480p | 10s @ 720p | Confidence |
| --- | --- | --- | --- |
| BytePlus official (¥70/M tokens) | ~**$1.00** | ~**$2.10–2.30** | High — their own worked example is ¥7.56 for 5s @720p |
| Replicate / Segmind | ~$1.03 | ~$2.31–2.40 | High — independently land on the official rate |
| fal.ai ($0.0214/1k tokens) | **$2.21** | **$4.73** | **Verified directly on the model page** |
| Atlas Cloud (flat $0.134/s) | $1.34 | $1.34 | Low — single source, site flagged for stale content |

**fal.ai charges exactly 2× the official token rate** ($21.40/M vs $10.70/M) — a clean markup,
which is what explains the whole spread. fal publishes its token formula,
`(height × width × duration × 24) / 1024`, and the arithmetic reconciles every figure above.

So the honest headline is **$1–5 per 10-second clip**, depending on provider and resolution —
not the $4.70 that an early draft of this document quoted from fal alone.

**It doesn't matter which end of that range is right.** Google's Ultra allowance makes Flow
iteration free at the margin; Seedance bills every attempt. Six candidates to land one keeper
is $6–14 a shot. That is the parking decision, and a cheaper provider does not change it.

**Resolved — the video-reference pricing contradiction.** BytePlus's own rate card charges
**¥42/M with video input vs ¥70/M without** — 40% cheaper per token, exactly as Segmind
claimed. Replicate's "~4× more expensive" is also true, because the *input* video's duration
counts toward billable tokens: the rate falls, the token count rises. Both were right about
different halves. No live key needed after all.

### 5d. Where Seedance actually beats Veo

On Artificial Analysis's blind image-to-video Elo (2026-08-02), **Seedance 2.0 720p ranks #1
at 1,199** against Veo 3.1 at 1,085. Seedance 2.5 is not yet a separate leaderboard entry.
Qualitative consensus: Seedance wins on multi-shot consistency, native joint audio, and the
30-second single-pass take; Veo 3.1 wins on single-hero-shot cinematic polish and grade.

**So the honest framing is not "Seedance replaces Flow."** It is: Seedance is the better tool
for long, multi-beat, reference-heavy, audio-bearing sequences that can run unattended;
Flow/Veo stays the better tool for the hero shot and for anything needing >720p.
That is an argument *for* multi-provider, not for migration.

## 6. Plan

### 6a. Shape — a sibling package, not a refactor

```
packages/flow-mcp/        # untouched. Browser. Veo 3.1 + Nano Banana Pro.
packages/seedance-mcp/    # new. HTTP. Seedance 2.5 (video) + Seedream 4.x (image).
docs/flow/                # existing prompt-craft KB
docs/seedance/            # new, mirrors it 1:1
```

Zero imports between the two packages. The **only** shared artifact is a written contract in
this document: same tool-name shape, same `{ error: true, code, message, hint }` envelope,
same `POLICY_BLOCKED` discipline. If a future third provider appears, it gets a third package.

There *is* one internal seam, and it is inside the new package only: a thin `providers/`
directory (`fal.ts`, `byteplus.ts`) behind a single `submit → poll → harvest` interface.
That is justified where a flow-mcp/seedance-mcp merger is not, because two async HTTP job
queues genuinely do share a shape — a browser and an HTTP client do not.

### 6b. Tool list — the ported contract

| New tool | Mirrors | Notes |
| --- | --- | --- |
| `seedance_status` | `flow_status` | Key present, credit balance, model reachable |
| `seedance_generate_image` | `flow_generate_image` | Seedream 4.x. `character` resolves via the local registry |
| `seedance_edit_image` | `flow_edit_image` | Seedream/SeedEdit; ref cap 10 rather than 1 |
| `seedance_generate_batch` | `flow_generate_batch` | **Port the resume-from-disk logic verbatim in spirit** — it is the single most valuable behaviour in flow-mcp and gets *better* here, because jobs can run concurrently instead of serially |
| `seedance_generate_video` | `flow_generate_video` | Same three source modes. Adds `durationSeconds` 4–30 int, 7 ratios, `audioRefs?`, `returnLastFrame?`, `generateAudio?` |
| `seedance_create_character` etc. | the seven character tools | Backed by the local registry (§6c) |
| — | `flow_refine` | **Dropped.** No session exists. Callers use `seedance_edit_image` against the golden instead; document the price difference rather than fake the ergonomics |
| — | `flow_*_project`, `flow_list_media` | **Dropped.** Our output directories are the project |

**Non-negotiable behaviours carried over:**
1. **Pre-flight capability refusals.** Reject a 1080p request, an out-of-range duration, or an
   unsupported mode *before* submitting. A wrong-but-healthy-looking clip is worse than an error.
2. **`POLICY_BLOCKED` as a distinct, never-retried code**, classified from fal's HTTP 422
   `content_policy_violation` and BytePlus's `SensitiveContentDetected` family.
3. **Harvest immediately** on success — 24h / 100-download expiry.
4. **Client-side dedup** on task creation, since there is no idempotency key.

### 6c. The character registry — the real build

Flow stores a Character server-side; Seedance does not. So we store it:

```
docs/stories/<story>/characters/<name>.json
  { name, refImages: [paths], bodyImage?, info, notes }
```

`seedance_create_character` writes the record and validates the references.
Every generation call that names a character then **expands** it: uploads (or URL-references)
the images, injects the positional tags, and appends the binding prose the research says is
mandatory — *an uploaded reference that is never named in the prompt text is inert.* That
expansion step is where our version has to be smarter than Flow's, and it is the part most
likely to need iteration.

Open question for Kai: reuse the existing `docs/stories/<story>/` character records and prompt
ledger as the registry, or keep a separate one? Reusing is tidier and matches the prompt-ledger
convention already in place.

### 6d. Build order — gated, cheapest risk first

- **T0 — Spike, before any package exists.** One fal.ai key, ~$20. Settle by experiment what
  documentation cannot: (a) **does a supplied audio track survive verbatim, or only condition
  timing** — the question the whole thread rests on; (b) is 1080p genuinely unavailable;
  (c) does a stylised BadCode prompt clear moderation that Flow blocks; (d) real per-clip cost.
  **Everything below is contingent on T0.** Ship a written verdict, not code.
- **T1 —** Package skeleton, `fal.ts` provider, `seedance_status`, `seedance_generate_video`
  in text→video mode only. Prove the loop end to end.
- **T2 —** The other two video modes + `returnLastFrame` + harvest-on-success + the error
  vocabulary. This is the point at which it can animate a finished panel.
- **T3 —** `docs/seedance/` authored from the prompt-craft brief, split to mirror `docs/flow/`
  (prompting, camera vocabulary with reliability tiers, consistency, failure modes, platform
  controls), plus a `seedance-prompt` skill alongside `flow-prompt`.
- **T4 —** Character registry + prose-binding expansion.
- **T5 —** Seedream image tools (`generate_image`, `edit_image`) — only if T0–T4 prove the
  stack is worth committing to for stills as well as video.
- **T6 —** Batch + resume, now concurrent rather than serial.
- **T7 (deferred) —** `byteplus.ts` direct provider as a cost optimisation, once volume
  justifies KYC and a hand-rolled client.

### 6e. Reference worth reading, not reusing

`leonaiuv/seedance-2-mcp` (npm, MIT, TypeScript) is a small existing MCP server hitting
Volcengine Ark with plain `fetch` — three tools, correct instincts about URL expiry. Read it
for the structural pattern; it is not production-grade and we should not depend on it.

## 7. Open questions for Kai

1. **Is the audio feature the point, or a bonus?** If it is the point, T0 is the whole ticket
   and everything else waits on its verdict.
2. **720p ceiling** — acceptable for comic-panel animation, or a blocker?
3. **Character registry** — fold into `docs/stories/<story>/`, or stand alone?
4. **Scope of T5** — do we want Seedream for stills at all, or does Flow keep the image side
   (Nano Banana Pro) while Seedance takes video only? That split may be the best of both.
