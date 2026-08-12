# Platform controls

Models, credits, aspect, duration, and the surfaces beyond the prompt box.

> ⚠️ **This is the most volatile file in the toolkit.** Tiers, prices and feature
> gating change often and sources contradict each other. Verify in the live UI before
> planning a shoot around any row below. See the volatility list in
> [`README.md`](./README.md).

## 1. Model / feature matrix

| Model | Clip length | Ingredients→Video | Frames→Video (first) | Frames→Video (first+last) | Extend | Edit existing video |
| --- | --- | --- | --- | --- | --- | --- |
| Veo 3.1 Lite | 4/6/8s | ✅ (8s only) | ✅ | ✅ | ✅ (Veo 3.1 content only) | ✗ |
| Veo 3.1 Fast | 4/6/8s | ✅ (8s only) | ✅ | coming soon | ✗ | ✗ |
| Veo 3.1 Quality | 4/6/8s | ✅ (8s only) | ✅ | coming soon | ✗ | ✗ |
| Gemini Omni Flash | 4/6/8/**10s** | ✗ | ✅ | ✗ | coming soon | ✅ |

**Plan the consistency strategy against this matrix, not against assumed parity.**
Sources disagree on the Extend row in particular — older help pages call Extend
Veo 2-only, the 3.1 announcement says audio now flows through it, and one community
report says it silently drops you to Veo 2 Fast with no audio. Test it.

**Image models:** Nano Banana 2 Lite (free default) → Nano Banana 2 → **Nano Banana Pro**
(the one for legible in-image text, localized edits, 14 references / 5 identities,
2K–4K). Our flow-mcp client defaults to Pro and re-asserts it per generation, because
Flow's picker resets to Nano Banana 2 on every navigation.

## 2. Credits

Billed **per generation, not per request** — one click configured for 2 outputs bills
twice. Check the output count before a batch session.

| Item | Credits |
| --- | --- |
| Veo 3.1 Lite | 10 (5 Ultra) |
| Veo 3.1 Fast | 20 (10 Ultra) |
| Veo 3.1 Quality | 100 (all plans) |
| Omni Flash video edit | 40 flat; generation 15/20/25/30 for 4/6/8/10s |
| 1080p upscale | free on paid plans, unavailable on free tier |
| 4K upscale | 50 (Ultra only) |
| Nano Banana Pro | ~12 / 15 / 25 for 1K / 2K / 4K — **third-party figure, verify in-app** |

Free tier: 50 credits/day, refreshed by your first generation of the day. Paid: monthly
pool refreshed at billing-cycle start. **Nothing rolls over on either cadence, and there
are no à-la-carte top-ups** — a burst production month can hard-stall you until the
cycle turns.

**Workflow consequence:** iterate composition, action and camera on Lite or Fast, then
re-run the *identical* prompt once on Quality for the hero take. Budget roughly 8–12
clips including discards per 60 seconds of finished output.

## 3. Aspect ratio, duration, resolution

- **Video aspect ratio: 16:9 or 9:16 only.** Set it as a project default (prompt box →
  Settings) rather than per clip. ⚠️ These defaults **reset per project** — a fresh
  project comes up as Omni Flash.
- **Duration: 4 / 6 / 8s presets, no slider.** 10s only on Omni Flash. Anything longer is
  Extend chaining or Scene Builder assembly.
- **Resolution is a separate upscale step after generation.** Generate at base for
  drafts; upscale only the final pick.
- Image aspect ratios are much richer — see [`image-prompting.md`](./image-prompting.md) §9.
  Note our observed still output is 1376×768 (ratio 1.792), near but not exactly 16:9;
  assert "landscape within 2%", never strict equality.

## 4. Scene Builder

Hover a clip → "Add to Scene". Inside: arrange clips in sequence, drag to reorder, trim
in/out with handles, and Extend in place to continue a move.

**Generate short beats independently and assemble here.** Do not try to nail one long
single generation.

## 5. Insert / Remove / video edit

- **Insert** adds elements with automatically matched shadows and scene lighting.
- **Remove** reconstructs background as if the object was never there.
- **Omni Flash video edit** — select up to a 10-second segment, prompt a change ("Change
  the lighting to a cinematic sunset"), up to 3 conversational turns without losing
  context.

Reach for these when a single prop is wrong, rather than re-rolling a whole generation.

## 6. Seeds — there is no seed box

The only exposed control is **Regenerate** (same prompt, different seed), pitched for
"the composition is right but you want variation". Flow does not surface, pin, or let you
re-enter a seed value.

The Vertex API *does* accept a `seed` (uint32) for deterministic output; **Flow does
not expose it.** True reproducibility inside Flow does not exist — rerun the identical
prompt and accept stochastic drift. Plan the ledger around recording media ids, not
around being able to regenerate a past image.

## 7. Assets and organisation

Nestable **Collections** — drag one asset tile onto another to create one, drag assets
in. The Outputs panel toggles **Grid** (visual tiles) and **Batch** (sequential with
per-asset detail). `@` mentions pull a saved character, environment or asset into any
prompt.

## 8. The Flow Agent

A project-scoped conversational orchestrator: brainstorm and plan storyboards,
batch-generate variations, edit, rename and group assets.

**Agent queries are free; media it generates spends your credits.** The approval gate
can be set to **Never**, letting it spend autonomously without confirming each
generation — the correct setting for an unattended batch run and the wrong one
everywhere else. Conversations persist as per-project Sessions, and per-project **Agent
Instructions** act as a standing system prompt. Web only.

**Storyboard Studio** ("Make a Story") takes written prose and generates scene
breakdowns, dialogue, character/location/prop sheets, and storyboard panels with
suggested camera shots, all editable afterward. *Under-verified — mechanics confirmed
only via secondary coverage. Test before designing a skill around it.*

⚠️ Our flow-mcp client deliberately **leaves** Agent mode (`ensureImageMode` toggles out
of it) because direct generation is what the tools drive. If we ever want the Agent's
storyboarding, that's a new capability, not a flag.

## 9. Rate limits

**Google publishes no numeric rate limits for the Flow UI** — no requests/minute, no
concurrency cap, no cooldown. Community reports say requests are *rejected rather than
queued* at capacity, and recommend pacing manual batch submissions 30–60s apart and
waiting 15–30 minutes after a peak-time failure. That is folklore, not guidance, but it
costs nothing to follow.

Sustained volume also appears to trigger recaptcha challenges (observed during our own
camping recut). For genuinely high-volume automated work the official escalation is
**Vertex AI direct access** — Veo 3.1 via API, pay-per-use — which sidesteps the
credit and rate model entirely.
