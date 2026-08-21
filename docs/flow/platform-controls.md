# Platform controls

Models, credits, aspect, duration, and the surfaces beyond the prompt box.

> ⚠️ **This is the most volatile file in the toolkit.** Tiers, prices and feature
> gating change often and sources contradict each other. Verify in the live UI before
> planning a shoot around any row below. See the volatility list in
> [`README.md`](./README.md).

## 1. Model / feature matrix

✅ **Settled 2026-08-18 against Google's own published matrix**, which we had never read. It
resolves most of what this file used to hedge about — and it disagrees with us in one place
that matters. Verbatim from *Learn about Google Flow models & supported features*:

| Feature | Veo 3.1 Lite | Veo 3.1 Fast | Veo 3.1 Quality | Gemini Omni Flash |
| --- | --- | --- | --- | --- |
| Text → Video | 4/6/8s | 4/6/8s | 4/6/8s | 4/6/8/**10s** |
| Frames → Video (first) | 4/6/8s | 4/6/8s | 4/6/8s | 4/6/8/**10s** |
| Frames → Video (first + last) | 4/6/8s | 4/6/8s | 4/6/8s | coming soon |
| **Ingredients / References → Video** | **8s only** | **8s only** | 🔴 **No** | 4/6/8/10s, + character/avatar & voice refs |
| Video → Video editing | No | No | No | up to 10s |
| **Extend** | **8s only** | No | No | coming soon |

Both aspect ratios (16:9, 9:16) everywhere it is supported at all. Google's footnote on Extend:
*"All Veo 3.1 8s videos can be extended, but you must use Veo 3.1 Lite to extend them."*

⚠️ **Do not pick Omni Flash for image→video on rank alone.** It sits ~280 Elo above Veo 3.1 on
the public image-to-video board, and in a live A/B on a BadCode plate that lead produced **no
measurable quality gain** — detail retention was a tie and identity held equally. `Veo 3.1 Fast`
remains the `flow_generate_video` default. Evidence, bounds and the numbers:
[`video-prompting.md`](./video-prompting.md) §3, *Leaderboard rank does not transfer to our
register*. Omni Flash also ignored `count` in that run (returned 1 of 2, `partial: true`).

### The three rows that change how we work

🔴 **1. Casting a character rules out Quality entirely.** Ingredients/References → Video is
marked **No** on Veo 3.1 Quality. Our old table claimed all three Veo tiers supported it, and
that was wrong. So the tier ladder in rule 5 of the README — *iterate on Lite, spend on
Quality for the hero take* — **does not apply to any shot with a cast character.** For those,
Fast is the ceiling, and the hero take is a Fast take. Plan the look accordingly rather than
discovering it on the shot you cared about.

🔴 **2. Ingredients force 8 seconds.** Cast a character and 4s and 6s disappear. There is no
short character clip.

🔴 **3. Extend is Lite-only by design, not by accident.** We found this live on 2026-08-18 —
the menu item reads `Extend (Veo 3.1 - Lite)` and offers no tier picker — and assumed a
rollout quirk. It is the documented behaviour. Extending an 8s Quality clip continues it *at
Lite*, which is a quality cliff in the middle of a shot. Kai's ruling stands: **cut every 8
seconds instead.**

### Where Google and our own eyes disagree

| Claim | Google | Us, live | Ruling |
| --- | --- | --- | --- |
| Omni Flash 10s | 4/6/8/**10s** | **10s tab absent from the DOM** (2026-08-18); a 10s request returned `VIDEO_DURATION_UNAVAILABLE`. It was present 2026-08-12. | **Assume 8s.** Our account is the one we generate on. Re-check before planning a 10s beat. |
| Omni Flash video → video editing | supported, up to 10s | not present in this account (2026-08-12) | Google's help page for it says *"this feature is only available in certain countries"* — that is the likely explanation, and it means **don't design a workflow on it from the UK.** |
| First+last frame on Fast and Quality | supported | supported — verified frame by frame | Agreed. Older docs saying "coming soon" for those tiers are stale. |
| Extend on Fast/Quality | No | not present | Agreed. |

**8 seconds is the hard cap on every Veo tier** — that is Google's own table, not just our
measurement. The only 10s in Flow is Omni Flash, which is not Veo, and which our account
currently doesn't offer it on either.

### Flow silently swaps your model

*"If we detect you're trying to use a feature that is not available in your selection, we'll
default you to a compatible model."* This is the mechanism behind both the Extend pin and the
Quality/ingredients exclusion — **you do not always generate on the tier you selected.** Read
the model back off the compose bar before a spend you care about; don't trust the tier you set
a navigation ago. (Our flow-mcp client already re-asserts the image model per generation for
the same reason.)

**Image models in Flow:** Nano Banana 2 Lite (the free default) → Nano Banana 2 (standard) →
**Nano Banana Pro** (complex designs, accurate detail, professional control; the default for
Ultra subscribers). Our flow-mcp client defaults to Pro and re-asserts it per generation,
because Flow's picker resets on every navigation.

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

**Officially settled 2026-08-18:**

- **You are not charged for a failed generation.** Including one killed by the audio stage —
  Flow's FAQ says the credits are refunded. So a policy block and an audio failure both cost
  time, not money; the thing to protect is the clock, not the balance.
- **Google publishes no price list.** *"Model costs are evolving fast. You can find the latest
  costs in the product when you select a model"* — prompt box → Settings. Every figure in the
  table above is therefore third-party or observed, and the table is a planning aid, not a
  quote.

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
it is a quality decision, not a convenience one. **Confirmed as documented behaviour**, not a
rollout quirk — see §1.

**What Extend actually does, per Google:** *"Extend finalizes the final second or 24 frames of
your video and continues the action."* Two consequences worth knowing before you reach for it:

- It only sees the **last second**. Everything earlier in the clip is invisible to the
  continuation, which is why an end frame with a readable silhouette and settled motion
  extends well and a mid-whip-pan frame does not.
- *"Voice is not able to be effectively extended if it's not present in the last 1 second of
  video."* Irrelevant to us — our audio is Suno's — but it explains a whole class of
  community complaints about extensions going silent.

Also: *"You can't apply other edit modes such as insert, remove, and camera to extended video
clips."* Extending forecloses the repair tools. Do the surgery first, extend after.

Also live in the scene editor and easy to miss:

- **`Save Frame`** (player overlay, `add_photo_alternate`) — saves the current playhead
  frame straight into the project as an asset. This is the frame-to-frame chaining
  workflow **built in**; no download-and-ffmpeg round trip needed to get a start image
  for the next clip.
- **A prompt box — "Describe your edits" + `Create`**, with its own model picker
  (observed defaulting to Omni Flash). A generative edit surface on the scene itself.

**None of this is reachable from `@badcode/flow-mcp`** — there are no Scene Builder tools.
It is manual browser work until someone adds them.

✅ **A scene can be downloaded.** Flow's help lists Scenebuilder's capabilities as: arrange
clips in sequence, reorder, trim in/out with the handles, preview the whole sequence, and
**download a scene**. That closes the question this file left open on 2026-08-18 — an Extend
produces a longer *scene* rather than a clip file, and the way that scene becomes an mp4 is
Scenebuilder's own download, not a per-clip one. Not automated: `@badcode/flow-mcp` has no
download tool, so it is a manual click.

**Also documented and easy to miss:** the **History panel** on any clip keeps *"all previous
versions of the video and the prompts you used to generate them"* — an in-app prompt ledger.
It is the recovery path when a prompt didn't make it into `docs/stories/<story>/prompts.md`,
and a reason to prefer editing a clip over re-rolling from scratch.

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

**Verified against Google's Agent help page 2026-08-18** — every claim above holds, plus:

- **Agent queries are free but daily-quota'd.** Free is not unlimited; the quota is on queries,
  separate from the credits its generations spend.
- **Agent Instructions accept a reference image**, not just text. That makes them a standing
  art-direction brief for a project, which is much closer to what `badcode-art-direction`
  does than we assumed.
- It can **batch-generate** on request — *"Give me 5 variations of this video with different
  lighting"* is Google's own example — and rename, group into Collections, and archive assets.
- Sessions are per-project and persist; deleting one clears the chat, not the media.
- Web/PC only.

**Storyboard Studio** ("Make a Story") takes written prose and generates scene
breakdowns, dialogue, character/location/prop sheets, and storyboard panels with
suggested camera shots, all editable afterward. *Under-verified — mechanics confirmed
only via secondary coverage. Test before designing a skill around it.*

⚠️ Our flow-mcp client deliberately **leaves** Agent mode (`ensureImageMode` toggles out
of it) because direct generation is what the tools drive. If we ever want the Agent's
storyboarding, that's a new capability, not a flag.

## 9. Rate limits

**Rate limiting is real and officially documented — upgraded from folklore 2026-08-18.**
Flow's FAQ names the error and the mechanism:

> *"To balance the available resources for all users and prevent abuse of our platform, we may
> rate-limit the number of generations you can make, particularly for zero-credit models. After
> you've made a large number of generations in a day, the number of generations you can make
> within a minute will decrease."*

So the throttle **tightens as the day's volume grows**, and it bites hardest on free models.
A batch that ran fine this morning can stall this afternoon on the same account — that is
expected behaviour, not a fault to debug.

Google still publishes no *numbers* — no requests/minute, no concurrency cap, no cooldown. Community reports say requests are *rejected rather than
queued* at capacity, and recommend pacing manual batch submissions 30–60s apart and
waiting 15–30 minutes after a peak-time failure. That is folklore, not guidance, but it
costs nothing to follow.

Sustained volume also appears to trigger recaptcha challenges (observed during our own
camping recut). For genuinely high-volume automated work the official escalation is
**Vertex AI direct access** — Veo 3.1 via API, pay-per-use — which sidesteps the
credit and rate model entirely.

## 10. Watermarking — a publication decision, not a setting

**Every** Flow output — Veo, Omni, Nano Banana — carries an invisible **SynthID** watermark.
That is not optional and not removable, and it is the honest half of
[`docs/using-ai.md`](../using-ai.md): our published work is detectable as AI-generated whether
or not we say so, so the disclosure position costs us nothing we still had.

**A *visible* watermark is separate and is a toggle**: profile picture menu → "Visible
watermarking". It is applied automatically and unavoidably for users in **India, South Korea
and Vietnam**.

Check the toggle before generating anything destined for publication — a visible watermark
baked into a comic panel or a music-video clip is a re-generation, not a fix.

## 11. Browser requirement

Flow wants a **Chromium-based browser** (Chrome, Edge); Google says other browsers "may work"
but are not optimised and may show bugs. Our `scripts/flow-chrome.sh` already satisfies this —
noted here so nobody "helpfully" ports the automation to Firefox.

---

## Sources

Re-checked at source **2026-08-18**. Figures marked third-party stay third-party; everything
in §1 is now Google-published or measured by us, with the date and which is which.

- [Learn about Google Flow models & supported features](https://support.google.com/labs/answer/16352836?hl=en) — the §1 matrix, verbatim.
- [Get started with Google Flow](https://support.google.com/labs/answer/16353333?hl=en) — plans, credits FAQ, failed-generation refunds, rate limiting, model auto-switching, watermarking toggle, browser requirement.
- [Create videos in Google Flow](https://support.google.com/labs/answer/16353334?hl=en) — ingredients, frames, characters, voices, the Agent prompt box, best practices.
- [Edit videos & build scenes in Google Flow](https://support.google.com/labs/answer/16935718?hl=en) — Extend, Omni Flash video editing, Save Frame, Scenebuilder and its download.
- [Use the Google Flow Agent](https://support.google.com/labs/answer/17093911?hl=en) — §8.
- [Generate videos with Veo 3.1 — Gemini API](https://ai.google.dev/gemini-api/docs/veo) — Extend semantics, per-model durations/resolutions, API-side limits.

⚠️ **The API is a different surface from Flow and its numbers do not transfer.** The Gemini
API offers 1080p and 4K at 8s, extension to ~148s, and a `seed` — none of which Flow exposes.
Quoting an API capability as a Flow capability is the single easiest way to plan a shoot around
something that does not exist here.
