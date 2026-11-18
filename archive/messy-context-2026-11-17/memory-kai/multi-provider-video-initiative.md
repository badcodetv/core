---
name: multi-provider-video-initiative
description: "PARKED 2026-08-12 — Seedance 2.5 second-provider plan; metered pricing loses to Google's Ultra allowance; no-shared-code ruling; revisit triggers"
metadata: 
  node_type: memory
  type: project
  originSessionId: 13f4bbd5-e641-4ef3-944d-1d8d0894ddb6
  modified: 2026-08-12T19:46:39.565Z
---

**PARKED by Kai, 2026-08-12.** Researched and planned, never built. Adding a **second
video/image provider** alongside Google Flow, prompted by Seedance 2.5 (ByteDance) having a
real HTTP API and reported audio-input support. Plan (park decision + revisit triggers at the
top): `design/2026-08-12-multi-provider-video.md`; research briefs:
`design/research/2026-08-12-seedance-2-5/`. Both committed on `feat/enc-program`.

**Why parked — re-run this argument before reopening.** Seedance is metered per second of
output; Google's **Ultra plan allowance is generous**, so iteration is free at the margin on
Flow and billed per attempt on Seedance. Verified pricing is **$1–5 per 10-second clip**
(BytePlus official ~$2.10–2.30 at 720p, ~$1.00 at 480p; fal.ai $4.73, exactly 2× the official
token rate). Which end of the range is right doesn't matter — six candidates to land one keeper
is $6–14 a shot. Do not re-quote fal's number alone as "the price"; that was an error in the
first pass of this analysis, corrected on the same day.

**Revisit only if:** Seedance ships >720p on a live schema; OR someone confirms an uploaded
audio track survives **verbatim** rather than only conditioning timing (~$6 of 480p clips
settles it); OR we need headless/unattended runs a browser puppet cannot do.

**Kai's ruling (load-bearing):** do NOT merge or refactor `@badcode/flow-mcp` to share code.
"One is a browser and the other is an API" — they will have very different opinions about how
interactions work. **The thing being ported is the tool list**, because that is the entire API
as far as a language model is concerned. New provider = new sibling package
(`packages/seedance-mcp`), zero imports, contract shared only as prose.

**Why:** forcing a CDP puppet and an async HTTP job queue through a common abstraction makes
both worse; the capability surface is the only part that has to match.

**How to apply:** when this resumes, measure any provider against the 17-tool flow-mcp surface
(§3 of the plan), not against flow-mcp's internals. Never propose a shared base class.

**Research verdicts that change the decision** (full detail + sources in the briefs):
- The audio question — whether a supplied track survives **verbatim** or only conditions
  timing/lip-sync — is **UNVERIFIED and not settleable from docs**. It is the reason the whole
  thread started, so it is gate **T0**: one ~$20 fal.ai test before anything gets built.
- Seedance 2.5 caps at **480p/720p** on every live schema; "30s 4K" is marketing.
- Seedance is **video-only**; stills/edits need Seedream 4.x / SeedEdit — a second integration.
  Likely best split: Flow (Nano Banana Pro) keeps images, Seedance takes video.
- **No server-side character object exists anywhere in the ByteDance stack.** Identity =
  re-attach reference images every call + bind them in prose. An uploaded reference never
  *named* in the prompt text is inert. Our character tools must be rebuilt client-side.
- Build against **fal.ai** first (card-and-go, real `@fal-ai/client` TS SDK); BytePlus direct
  is ~half price but needs business KYC and has no official Node SDK.
- Moderation is a face/voice **similarity** check against real public figures, not a topic
  filter — structurally kinder to BadCode's stylised fictional-archetype register than Flow's.
  See [[flow-policy-blocks]].

Related: [[flow-mcp-and-art-direction-initiative]], [[flow-video-modes]],
[[flow-script-hardening-initiative]].
