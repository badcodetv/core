# Seedance 2.5 API — Decision Brief for Multi-Provider Video/Image MCP

## 1. Bottom line

- **Yes, API-accessible today** — live and callable, confirmed via BytePlus ModelArk/Volcengine Ark direct docs *and* independently via fal.ai's working schema. Briefs disagree on the exact launch date (see §2) but agree it is GA, not beta/waitlist, as of 2026-08-12.
- **From where**: official first-party route is BytePlus ModelArk (intl, `ap-southeast-1`) or Volcengine Ark (China-only, `cn-beijing`) — same model, different model-ID string and region. A UK company can sign up on BytePlus with a non-Chinese business certificate; Volcengine mainland is the harder KYC wall.
- **At what cost**: official token pricing (~$0.10/s @480p, ~$0.23/s @720p, no video-ref) is the cheapest tier. Third-party resellers cluster into an "at-cost" band matching that (fal.ai, Replicate, OpenRouter, CometAPI, Segmind) and a "margin-added" band 1.5-3x higher (PiAPI, WaveSpeed).
- **With what missing**: no still-image generation/editing (separate Seedream/SeedEdit models), no persistent server-side Character object anywhere in the ByteDance stack, no session-based refine, no per-call multi-output, no official Node/TS SDK for the video task API — all four are real gaps against the existing Flow MCP contract.
- **Biggest unresolved conflict**: two briefs directly disagree on whether video-reference input costs *more* (Replicate: ~4x) or *less* (Segmind: ~40% cheaper) than plain text/image input — this must be tested per-provider, not assumed.

## 2. Does Seedance 2.5 exist as claimed

**Verified, converging across all five briefs**: Seedance 2.5 is real, is ByteDance's flagship video model, is distinct from 1.0/1.5/2.0, and has a live, publicly callable API (not beta/waitlist) as of today. Confirmed independently via BytePlus/Volcengine's own docs (brief 1), a working fal.ai reseller schema (brief 3), and multiple third-party aggregator listings (brief 2).

**Launch-date timeline is contradicted across briefs** — not reconciled here, reported as-is:
- Brief 2: FORCE conference announcement 2026-06-23 → BytePlus API opened 2026-07-16 → Dreamina/enterprise route ~2026-07-31/08-07.
- Brief 5: cites the *same* `seed.bytedance.com` announcement blog post but dates it 2026-07-31, and describes API access at that time as still "coming soon."
- Brief 1: describes the API as fully public starting 2026-08-07, 14:00 UTC+8, based on Chinese press dating the launch to that day, and explicitly calls several "coming soon" blog posts (kie.ai, atlascloud, evolink) stale/wrong as of 2026-08-12.
These are not necessarily mutually exclusive (staged rollout), but no brief reconciles them — treat "exact GA date" as unsettled.

**Resolution ceiling contradicts marketing, but briefs agree with each other here**: both brief 1 and brief 3 independently confirm the *live* API caps output at 480p/720p only — "native 30s 4K," repeated across marketing/SEO blogs, is (UNVERIFIED) against the actual schema. Brief 3 additionally flags that Seedance 2.0's own fal.ai endpoint exposes 1080p, meaning 2.5's live surface is currently a narrower resolution ceiling than its own predecessor on the same platform.

**Model IDs (verified, consistent across briefs 1 and 5)**: `dreamina-seedance-2-5-260628` (BytePlus intl) / `doubao-seedance-2-5-260628` (Volcengine China) — same underlying model, different brand string + region.

## 3. Provider comparison table

| Provider | Model slug | Price + unit | Features exposed | Async pattern | Signup friction | Verdict |
|---|---|---|---|---|---|---|
| **BytePlus ModelArk** (official, intl) | `dreamina-seedance-2-5-260628` | $10.70/M tokens (no video ref) / $6.40/M (w/ video ref) ≈ $0.10/s@480p, $0.23/s@720p (5s example) | Full param set: 30 img/10 video/10 audio refs, first+last frame, native audio, 4-30s, 480p/720p only | POST create → GET poll `.../tasks/{id}`; optional webhook `callback_url` (3 retries, unsigned — build own auth) | Business real-name verification (non-Chinese cert accepted per brief 1); min $30 balance or resource pack to activate model | Cheapest at-cost; no official Node/TS SDK (Python/Go/Java only) — must hand-roll fetch |
| **Volcengine Ark** (official, China) | `doubao-seedance-2-5-260628` | Same token pricing | Same schema | Same lifecycle | Harder KYC — China national ID/passport friction reported (UNVERIFIED, third-party-sourced only) | Avoid unless already China-facing |
| **fal.ai** | `bytedance/seedance-2.5/{text-to-video,image-to-video,reference-to-video}` | $0.0214/1000 tokens ≈ $0.22/s@480p, $0.47/s@720p (no video ref) | 3 dedicated endpoints; `end_image_url` = first+last frame; full ~50-ref budget; `generate_audio` bool | `fal.subscribe()` (queue+poll wrapper) or manual `fal.queue.submit`/`status`/`result`; webhooks supported | None — pay-as-you-go, card only, `end_user_id` for B2B | **Best-documented; real, confirmed-working `@fal-ai/client` TS SDK** |
| **Replicate** | `bytedance/seedance-2.5` | $0.1028/s@480p, $0.2312/s@720p (no video ref); $0.4304/s@480p, $0.9676/s@720p (with video ref — ~4x, conflicts with Segmind below) | Adaptive AR, native 30s, native audio; ref cap stated as 30 img+10 video+10 audio | Standard Replicate prediction API (`replicate.run()` polls internally); official `replicate` npm client; webhook events filter | None — normal Replicate account | Second choice; mature SDK ecosystem, confirmed Node code sample |
| **OpenRouter** | `bytedance/seedance-2.5` | $0.1028/s (no resolution breakdown published) | OpenAI-compatible base URL swap | Not documented on page | Not documented | Live per direct fetch, but **added after** OpenRouter's own launch list (which only named 2.0/2.0-Fast/1.5-Pro) — treat as newer/less battle-tested |
| **WaveSpeed AI** | `bytedance/seedance-2.5/{text-to-video,-turbo,image-to-video,-turbo,-spicy,video-edit,-turbo,video-extend}` | $0.18/s@480p, $0.36/s@720p; video-edit $0.11/s | Full endpoint family incl. "spicy" (less-restricted) and video-extend | POST returns prediction ID; GET polls (recommend 2s→5-10s backoff) | Single WaveSpeed key covers all models | Pricier (margin-added tier), but most endpoint variety |
| **Segmind** | `https://api.segmind.com/v1/seedance-2.5` | $10.97/M tokens (text/image input, ~$0.10-0.11/s@480p, ~$0.239-0.240/s@720p); $6.56/M (video input, ~40% *cheaper* — conflicts with Replicate's "4x more expensive" claim) | `duration` 4-30 int, `resolution` 480p/720p, 7 aspect ratios; audio free | **Genuinely synchronous** — single blocking POST, MP4 returned in-body, no job ID/polling (unique among all providers surveyed) | None documented | Simplest integration if a held-open connection for minutes is acceptable |
| **PiAPI** | `seedance-2.5` / `seedance-2.5-less-restriction` | $0.15/s@480p, $0.35/s@720p standard; +10% less-restriction | Only 9 img/3 video/3 audio refs (well below the ~50 ceiling elsewhere); audio ref requires an image/video ref alongside it | Not documented on page (PiAPI's platform norm elsewhere is async task-based) | Not documented | Fallback specifically for content-policy blocks (named "less-restriction" lever) |
| **CometAPI** | `doubao-seedance-2-5` → maps to `dreamina-seedance-2-5-260628` | Mirrors BytePlus token rates ($10.70/$6.40 per M) | OpenAI-compatible drop-in across 500+ model catalog | Explicitly documented async: task IDs, polling, callbacks, durable storage, retry rules | Standard CometAPI account | Page dated 2026-07-31 said "coming soon" — **re-verify live status before use** |
| **Runware** | `bytedance:seedance@2.5` (AIR-style ID) | ~$0.66-2.96/generation (not broken out per-second) | `TTL` field on output (expiry, window unquantified) | `async` per docs | Not documented | Workable but least-documented of the confirmed-live group |
| Kie.ai / Eachlabs / Pollo AI / ImagineArt | — | Not independently verifiable — pages return 403 to fetch or only secondhand blog estimates | Claimed live | Not documented | Not documented | **Do not commit without a live signup test** — none survived direct verification |

**Excluded / do not build against right now**: Higgsfield (2.5 explicitly "coming soon," only 2.0 family live). Novita AI (carries no Seedance model at all — only Seedream/image). Freepik/Magnific (consumer app prices Seedance 2.5, but the developer API reference does not list it). AI/ML API (docs stop at 2.0, marketing implies availability but no docs page exists). Any "official docs" repo/site not on a ByteDance/BytePlus/Volcengine domain (e.g. a GitHub repo styled as "the official Seedance 2.5 API doc" was found to actually be marketing for a paid reseller gateway positioned to bypass content moderation — treat any such source as untrusted, not documentation).

## 4. Capability matrix vs our Flow tools

| Our capability | Seedance/ByteDance equivalent | Gap |
|---|---|---|
| `generate_image` | **None.** Seedance has no still-image output surface at all — that's Seedream 4.0/4.5/5.0, a structurally separate model family, same platforms | Total — requires separate integration of Seedream |
| `edit_image` (1-3 ref, delta edit) | **None on Seedance.** Seedream v4/v4.5 `edit` endpoints accept up to 10 `image_urls`; SeedEdit 3.0 is single-reference-only, purpose-built for portrait/background/lighting edits | Different model family; Seedream's ref cap (10) exceeds ours (1-3), but it's a separate integration |
| `refine` (session, carries context) | **None.** Stateless async job API — no session/conversation/thread concept anywhere documented | Total — would need to reconstruct a new full prompt referencing the prior asset and resubmit, losing implicit context-carry |
| `generate_batch` (≤20, resume) | No native batch/resume endpoint. Seedream's `sequential_image_generation` gets coherent-set output but caps at 15 images/call and is images-only, not video | Our client-side batch/resume logic is portable as-is (fires N jobs, tracks state); no provider-side help |
| **Characters** (create/body/edit/info/list/get, castable identity) | **No persistent server-side identity object exists anywhere in the ByteDance stack** — confirmed independently for both Seedance (video) and Seedream/SeedEdit (image) across two separate briefs. Only substitute: re-attach the same reference image URL(s) every call, or a single-call "sequential"/reference-to-video batch that's consistent only within that one request. One third-party reseller (MuAPI, not ByteDance) bolts on a paid "character sheet" convenience layer | Total — must build our own local character record (golden ref image + description string) and re-attach it on every call |
| `generate_video`: image-to-video | Seedance `image-to-video` endpoint, `image_url` param | Matches |
| `generate_video`: first+last frame | Seedance `image-to-video` with `image_url` + `end_image_url` in the same call | Matches (Veo does this too via `image`+`lastFrame`) |
| `generate_video`: text-to-video | Seedance `text-to-video` endpoint | Matches |
| duration (4/6/8/10s fixed enum) | 4-30s, integer-second granularity, or `auto` | Seedance exceeds range; ours is a fixed enum, theirs is continuous-int — reimplement as a min/max/step control, not an enum |
| aspect ratio (16:9\|9:16) | 7 options: auto, 21:9, 16:9, 4:3, 1:1, 3:4, 9:16 | Seedance strictly exceeds our video AR set |
| `count` (1-4 outputs/call) | **No per-call multi-output parameter found on any Seedance schema (2.0 or 2.5).** Every call returns exactly one video | Total — must fire N separate calls to emulate |
| audio | See §5 | Seedance is strictly *ahead* of our current Flow/Veo contract, which has no audio-input mechanism at all |
| error model (`POLICY_BLOCKED`, `TIMEOUT`, tier errors) | Typed content-moderation codes exist (`SensitiveContentDetected` family, `PolicyViolation`, `PrivacyInformation`, `DeepFake`) roughly analogous to `POLICY_BLOCKED`; `execution_expires_after` (1-72h) bounds worst-case run time in place of a client `TIMEOUT`; no documented per-tier capability-error taxonomy | Different shape — needs a translation layer, not a port |
| `list_media`/`list_projects`/`open_project`/`create_project` | **None.** Job API returns only a signed video URL — no gallery/project concept | Total — need our own asset-tracking layer, and it must download the asset promptly: the URL is valid 24h and downloadable at most 100 times before it dies |

## 5. The audio question

What supplying an audio clip actually does (confidence: **likely**, per brief 3, corroborated by brief 5's documented size limits for the same field):

- `generate_audio` (bool, default **true**) triggers the model's **own** native joint audio/dialogue/lip-sync generation, synchronized with the video in one pass. Put spoken dialogue **in double quotes inside the text prompt** and the model performs it in its own synthesized voice with matching lip movement — you write the line as text, you do not supply a voice recording to be dubbed.
- `audio_urls` (up to 10, on the `reference-to-video` endpoint only, per brief 3/likely; size-limited to <15MB, wav/mp3, 2-30s per brief 5) is a **reference input** for rhythm/timing/mood conditioning — closer to a temp-track/timing guide than literal dialogue dubbing.
- **No parameter anywhere in any brief describes "upload this exact voice recording and get a character lip-synced to precisely that audio track."** That specific dubbing use case is (UNVERIFIED) / likely not supported as such — this needs a live generated-sample test to confirm, not schema inspection.
- For contrast: Veo/Flow has no audio-input mechanism at all (only a `generateAudio` boolean, native generation only) — Seedance adds capability here rather than merely matching our existing contract.

## 6. Integration shape

Confirmed lifecycle (brief 5, most detailed source):

1. `POST .../contents/generations/tasks` with `{model, content[], resolution, ratio, duration, ...}` → returns `{id, status:"queued", ...}` immediately (non-blocking).
2. Either poll `GET .../tasks/{id}` (status: `queued → running → succeeded|failed|cancelled|expired`) or register `callback_url` for webhook notification on status change (3 retry attempts, 5s confirmation window expected — **no documented HMAC signature**, build your own auth on the receiver).
3. On `succeeded`, response includes `content.video_url` (+ optional `last_frame_url`) — **valid 24h, downloadable at most 100 times**. Download immediately; do not store the URL as a long-term reference.
4. `execution_expires_after` (default 172800s/48h, range 1h-72h) bounds worst-case in-flight time.
5. **No idempotency key or safe-retry mechanism documented** for the create-task POST — a retried POST after a network timeout may create a second, separately-billed task. Build client-side dedup.
6. No official Node/TS SDK for this endpoint (brief 1) — Python/Go/Java only. Practical Node/TS paths, both with confirmed working examples (brief 5):

```typescript
// Option A — fal.ai (@fal-ai/client, confirmed working)
import { fal } from '@fal-ai/client';

const result = await fal.subscribe('bytedance/seedance-2.5/image-to-video', {
  input: {
    image_url: startImageUrl,
    prompt: 'A slow dolly-in. "This is the line, spoken and lip-synced."',
    end_image_url: endImageUrl,        // first+last frame, same call
    resolution: '720p',                 // '480p' | '720p' only
    duration: '10',                     // 'auto' | '4'..'30'
    aspect_ratio: '16:9',
    generate_audio: true,
  },
  logs: true,
  onQueueUpdate: (u) => console.log(u.status),
});
// result.data.video.url — download within 24h / 100 downloads

// Option B — raw fetch against BytePlus ModelArk directly (no official SDK)
const create = await fetch('https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks', {
  method: 'POST',
  headers: { Authorization: `Bearer ${process.env.ARK_API_KEY}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({ model: 'dreamina-seedance-2-5-260628', content: [...], resolution: '720p', duration: 10 }),
});
const { id } = await create.json();
// poll GET .../tasks/{id} until status === 'succeeded', then download content.video_url immediately
```

A small real open-source reference exists (`leonaiuv/seedance-2-mcp`, npm `seedance-2-mcp`, MIT, TS, 7 stars) — 3 MCP tools (`seedance_create_task`, `seedance_check_task`, usage guide), plain `fetch()` against Volcengine Ark directly, `ARK_API_KEY`/`ARK_BASE_URL` env vars, and its own README independently warns the URL expires — worth reading as a structural pattern, not production-grade.

## 7. Recommendation

**Build against fal.ai first**, both surveying briefs converge on this independently:

- Confirmed, working `@fal-ai/client` npm package with a real code sample (brief 5) and the most complete, best-documented schema of any provider surveyed (brief 3's entire feature matrix is sourced from fal.ai because it was the only surface that yielded a real, fetchable schema).
- Pricing sits in the at-cost cluster (~$0.22/s@480p, ~$0.47/s@720p) — at "tens of clips/week" this is trivial spend, no subscription commitment, no credit-expiry risk.
- No business-account/KYC gate — pay-as-you-go with a card, unlike the official BytePlus route's real-name verification requirement.
- Exposes the full ~50-reference budget and both first+last-frame and reference-to-video modes.

**Replicate as close second / fallback** — equally no-KYC, well-known Node SDK, native webhook support with a documented events filter; its main open question is the video-reference pricing multiplier (see §8) which needs verifying before committing to it for reference-heavy workloads.

**PiAPI's `-less-restriction` variant** as the documented fallback specifically for content-policy blocks — this org's own Flow experience shows policy blocks are a common, recurring failure mode, and PiAPI is the one provider in this survey that names that lever directly (at a ~10% price premium).

**Do not build against**, for now: Higgsfield (not live), Novita (no Seedance), Freepik/Magnific (API doesn't expose it), AI/ML API (docs don't cover 2.5), and Kie.ai/Eachlabs/Pollo/ImagineArt (no verifiable pricing/schema survived direct fetch — require a live signup check first).

**Defer the official BytePlus/Volcengine direct route** as a later cost-optimization once volume justifies the KYC friction and hand-rolled-fetch maintenance burden (no official Node SDK) — it is the cheapest per-token but the most integration work.

## 8. Open questions needing a live API key

- Whether the direct BytePlus ModelArk API for 2.5 is actually live for a *new* customer today, given the "coming soon" language in earlier-dated sources vs GA-looking docs as of Aug 11-12 (contradicted across briefs 1, 2, 5).
- **Whether video-reference input costs more or less than plain input** — Replicate claims ~4x more expensive; Segmind claims ~40% cheaper; fal implies a discount. Directly contradictory across three briefs, must be tested per-provider.
- The exact 30-image/10-video/10-audio per-type reference split for 2.5 — only "up to 50 total" was independently confirmed in a raw schema fetch; the split is inferred from converging but uncited secondary sources.
- Whether 1080p/4K is available *anywhere* for 2.5 despite the headline marketing claim — every live schema checked caps at 720p.
- Whether 2.5 supports true multi-shot/scene-cut generation within one call, or is strictly a single continuous shot — directly contradicted between sources (CineD: single shot; MindStudio: multi-shot), unresolved.
- Whether reference audio can genuinely dub an exact supplied voice recording with lip-sync, vs. only text-prompt-driven TTS dialogue — schema-level only, no generated-sample test exists in any brief.
- **Exact numeric RPM/concurrency limits for Seedance 2.5 specifically** — brief 1 states explicit published numbers (600 RPM/10 concurrency enterprise; 180 RPM/3 individual); brief 5 states no provider publishes 2.5-specific numeric limits anywhere and it must be discovered empirically. Directly conflicting, needs a live account to settle.
- Whether the create-task POST supports any idempotency-key/dedup mechanism for safe retries after a network timeout (none found in docs fetched).
- Whether the webhook (`callback_url`) payload is signed/authenticated in any way (undocumented).
- The real direct-from-ByteDance (non-marked-up) price, since fal's resale rate is roughly 2x BytePlus's own token rate at the same resolution.
- Whether Volcengine mainland genuinely blocks passport-only individual KYC for a UK company (brief 1 flags this as third-party-sourced only, not confirmed against an official Volcengine signup doc).
- Exact minimum-token-consumption floor table for video-reference inputs (referenced by BytePlus docs via a gated Lark/Feishu spreadsheet, never fetched).
- Output URL retention/expiry windows for fal, Replicate, WaveSpeed, PiAPI, and CometAPI — none published on their pages (only BytePlus's own 24h/100-download limit and Runware's unquantified `TTL` field are documented at all).
- CometAPI's actual live status today, given its own page's 2026-07-31 "coming soon" dateline.

## 9. Sources

**Official (BytePlus/Volcengine)**
- https://docs.byteplus.com/en/docs/ModelArk/1520757 — create-task schema, model IDs, activation gate
- https://docs.byteplus.com/en/docs/ModelArk/1521309 — retrieve-task schema, URL expiry (24h/100 downloads)
- https://docs.byteplus.com/en/docs/ModelArk/1330310 — model catalog, sibling IDs, rate limits (1.0/2.0)
- https://docs.byteplus.com/en/docs/ModelArk/1298459 — auth (Bearer vs AK/SK)
- https://docs.byteplus.com/en/docs/ModelArk/1544106 — pricing worked examples
- https://docs.byteplus.com/en/docs/ModelArk/1848593 — rate-limit/backoff guidance
- https://docs.byteplus.com/en/docs/ModelArk/1541595 — official SDK list (Python/Go/Java only)
- https://docs.byteplus.com/en/docs/ModelArk/1330626 — OpenAI-compatibility scope (chat only)
- https://docs.byteplus.com/en/docs/ModelArk/1299023 — full error-code taxonomy
- https://docs.byteplus.com/en/docs/ModelArk/2191806 — region/base-URL detail
- https://docs.byteplus.com/en/docs/modelark/1885708 — file size/format limits
- https://docs.byteplus.com/en/docs/ModelArk/1099320 — token pricing detail
- https://docs.byteplus.com/en/docs/modelark/1553576, https://docs.byteplus.com/en/docs/ModelArk/1587798 — 1.0/2.0 rate limits
- https://docs.byteplus.com/en/docs/Account/sign-up-and-verify-byteplus-account, https://docs.byteplus.com/en/docs/Account/real-name-verification — KYC
- https://docs.volcengine.com/docs/82379/1520757?lang=zh — China-side mirror
- https://www.volcengine.com/article/37883, https://www.volcengine.com/docs/82379/1529797 — cost-control (Chinese-language, unverified in English)
- Seedream/SeedEdit: https://docs.byteplus.com/en/docs/ModelArk/1824718, https://docs.byteplus.com/api/docs/ModelArk/1541523, https://docs.byteplus.com/en/docs/ModelArk/1824691

**Reseller/aggregator platforms**
- https://fal.ai/models/bytedance/seedance-2.5/text-to-video, /image-to-video, /reference-to-video, /llms.txt variants; https://fal.ai/learn/tools/what-is-seedance-2-5; https://github.com/fal-ai/seedance-2.0-api
- https://replicate.com/bytedance/seedance-2.5, /api/api-reference
- https://openrouter.ai/bytedance/seedance-2.5; https://openrouter.ai/blog/announcements/video-generation/
- https://wavespeed.ai/seedance-2-5-api, https://wavespeed.ai/collections/bytedance
- https://www.segmind.com/models/seedance-2.5/pricing; https://blog.segmind.com/seedance-2-5-api-quickstart-generate-your-first-30-second-video-in-10-minutes/; https://blog.segmind.com/seedance-2-5-api-pricing-5-clips-tested-real-costs/
- https://piapi.ai/seedance-2-5; https://piapi.ai/blogs/seedance-2-5-vs-seedance-2-0
- https://www.cometapi.com/seedance-2-5-api-pricing/; https://apidoc.cometapi.com/
- https://runware.ai/docs/models/bytedance-seedance-2-5; https://runware.ai/seedance-2-5
- Not-live/excluded: https://novita.ai/models?category=video; https://higgsfield.ai/blog/seedance-2-5-pricing-2026; https://docs.magnific.com/api-reference/image-to-video/overview; https://docs.aimlapi.com/api-references/video-models/bytedance/seedance-2.0
- Unverified pricing: https://kie.ai/seedance-2-5; https://www.eachlabs.ai/bytedance/seedance-2-0; https://pollo.ai/hub/seedance-2-5-api; https://www.imagine.art/features/seedance-2-5
- Untrusted (flag, do not use as documentation): https://github.com/ZeroLu/seedance2.5-API

**Comparison / official competitor (Veo)**
- https://ai.google.dev/gemini-api/docs/veo
- https://ai.google.dev/gemini-api/docs/pricing

**Integration reference**
- https://github.com/leonaiuv/seedance-2-mcp; https://www.npmjs.com/package/seedance-2-mcp
- https://github.com/AceDataCloud/SeedanceMCP; https://github.com/ckz/volcengine-seedream-img-mcp; https://github.com/volcengine/ark-cli; https://github.com/SamurAIGPT/seedance-2-generator
- https://github.com/volcengine/volc-sdk-nodejs

**Existence/announcement**
- https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- https://en.wikipedia.org/wiki/Seedance_2.0
- https://www.techtimes.com/articles/320683/20260716/seedance-25-api-live-bytedances-30-second-ai-video-carries-unresolved-copyright-risk.htm
- https://www.cined.com/bytedance-seedance-2-5-api-goes-live-30-second-single-shot-clips-50-reference-inputs-and-3d-camera-blockouts/
- https://m.sohu.com/a/1059970070_100117963