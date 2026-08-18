# Platform controls

Models, credits, aspect, duration, and the surfaces beyond the prompt box.

> ⚠️ **This is the most volatile file in the toolkit.** Tiers, prices and feature
> gating change often and sources contradict each other. Verify in the live UI before
> planning a shoot around any row below. See the volatility list in
> [`README.md`](./README.md).

## 1. Model / feature matrix

| Model | Clip length | Ingredients→Video | Frames→Video (first) | Frames→Video (first+last) | Extend | Edit existing video |
| --- | --- | --- | --- | --- | --- | --- |
| Veo 3.1 Lite | 4/6/8s ✅ | ✅ (8s only) | ✅ | ✅ (2026-08-12) | ✅ **scene editor → Add Clip → Extend** (2026-08-18) | ✗ |
| Veo 3.1 Fast | 4/6/8s ✅ | ✅ (8s only) | ✅ | ✅ (2026-08-12) | **not present** (2026-08-12) | ✗ |
| Veo 3.1 Quality | 4/6/8s ✅ | ✅ (8s only) | ✅ | ✅ (2026-08-12) | not tested | ✗ |
| Gemini Omni Flash | 4/6/8s (**10s removed 2026-08-18**) | ✗ | ✅ | ✗ (2026-08-12) | not present (2026-08-12) | **not present** (2026-08-12) |

✅ **Clip length and first+last columns — VERIFIED live 2026-08-12.** First+last frame works on
**every Veo 3.1 tier**, not just Lite: the docs' "coming soon" for Fast and Quality is stale.
Omni Flash rejects a last frame (its End slot fills, then shows an error badge). A last frame
with **no** first frame is not a mode at all — Flow flags it invalid. A start+end clip was
generated on Fast and its two ends verified frame by frame. Details:
`docs/superpowers/flow-video.md` "Frames mode".

✅ **Clip length — same session** (`smoke-duration-model.ts`, by opening the
compose popover on each tier). Omni Flash offers 4/6/8/10s; Veo 3.1 Fast and Quality offer
4/6/8s and the **10s tab is absent from the DOM entirely**, not greyed out. Veo 3.1 Lite was
not opened, so its cell stays a claim.

⚠️ **SUPERSEDED 2026-08-18 for Extend — see §4, it lives in the scene editor's `Add Clip` menu.** The Edit-existing-video half of this still stands. Original finding: **Extend and Edit existing video — neither exists in this account's UI** (`smoke-tier-menus.ts`
+ `smoke-clip-detail.ts`, 2026-08-12, one clip generated per tier and its menus dumped). A
finished clip's own hover menu is the SAME eleven items on Veo 3.1 Fast, Veo 3.1 Lite **and Omni
Flash** — `Favorite · Reuse prompt · Add to scene · Add to prompt · Download · Rename · Share ·
Publish to YouTube · Set project cover · Flag output · Move to trash`. Not on the clip's page
either: clicking a clip opens the **scene editor** (`/edit/<sceneId>` — a timeline with `Add
Clip`), whose controls contain no Extend and no video Edit, and hovering the timeline reveals
none. Written "not present" rather than "false" deliberately: Google gates features per account
and per rollout, and this is one account on one day. But do not plan around either.

What Flow gives you *instead* of Extend is that scene editor: `Add Clip` chains footage on a
timeline. It is a much larger surface than a per-clip action and nothing in BadCode has needed
it — see `design/2026-08-12-flow-automation-coverage.md`.

⚠️ **Ingredients→Video is still transcribed from Google's documentation and has never been
tested by us.** Treat it as a claim awaiting verification; when you verify it, replace the cell
with the result *and the date you checked*. Every column settled so far was wrong in the docs,
which is the best argument for not trusting the rest.

**Plan the consistency strategy against this matrix, not against assumed parity.**
Sources disagree on the Extend row in particular — older help pages call Extend
Veo 2-only, the 3.1 announcement says audio now flows through it, and one community
report says it silently drops you to Veo 2 Fast with no audio. We could not find it at all.

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
- **Duration: 4 / 6 / 8s presets, no slider. 8s is now the cap on EVERY tier.**
  ⚠️ **Superseded 2026-08-18:** Omni Flash's 10s tab is **gone** — a live 10s request on
  Omni Flash returned `VIDEO_DURATION_UNAVAILABLE: no 10s tab on Omni Flash`. The 10s
  option verified on 2026-08-12 lasted under a week. Assume 8s until re-verified.
  Anything longer is frame-to-frame chaining or Scene Builder assembly. The control is in
  the **compose-bar popover's Video mode**, not the Settings panel — which is why we missed it
  for months. `flow_generate_video` takes `durationSeconds`; omitting it asserts 8s, because
  the setting persists on the project and would otherwise carry over silently.
- **Resolution is a separate upscale step after generation.** Generate at base for
  drafts; upscale only the final pick.
- Image aspect ratios are much richer — see [`image-prompting.md`](./image-prompting.md) §9.
  Note our observed still output is 1376×768 (ratio 1.792), near but not exactly 16:9;
  assert "landscape within 2%", never strict equality.

## 4. Scene Builder — and where Extend actually lives

Hover a clip → "Add to Scene", or click any clip to open `/edit/<sceneId>`. Inside:
arrange clips in sequence, drag to reorder, trim in/out with handles.

✅ **CORRECTION 2026-08-18 — Extend DOES exist. It is in here, not on the clip menu.**
The 2026-08-12 finding below ("Extend not present in this account") checked the clip's
hover menu and the scene editor's *visible* controls and concluded it was absent. It is
actually one level deeper: **scene editor → `Add Clip` button → dropdown menu**, whose
two items are:

| Menu item | What it does |
| --- | --- |
| `Add Clip` | insert an existing clip onto the timeline |
| **`Extend (Veo 3.1 - Lite)`** | **generate a continuation of the clip from its own end** |

⚠️ **Extend is pinned to Veo 3.1 Lite** — the cheapest tier (10 credits). You cannot
Extend at Fast or Quality. That is the real cost of using it over frame-chaining, and
it is a quality decision, not a convenience one.

Also live in the scene editor and easy to miss:

- **`Save Frame`** (player overlay, `add_photo_alternate`) — saves the current playhead
  frame straight into the project as an asset. This is the frame-to-frame chaining
  workflow **built in**; no download-and-ffmpeg round trip needed to get a start image
  for the next clip.
- **A prompt box — "Describe your edits" + `Create`**, with its own model picker
  (observed defaulting to Omni Flash). A generative edit surface on the scene itself.

**None of this is reachable from `@badcode/flow-mcp`** — there are no Scene Builder tools.
It is manual browser work until someone adds them.

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
