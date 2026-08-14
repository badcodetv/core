# Google Flow — engine reference

**What this folder is:** everything we know about the *models* Google Flow runs on, and how to
drive them well. Volatile, versioned knowledge with a shelf life measured in months.

**What this folder is not:** the BadCode visual identity. That lives in
`.claude/skills/badcode-art-direction/SKILL.md` and it is deliberately model-agnostic — the 35mm
house style, the calibration list against the generic AI-comic look, the Flow Character casting
rules, and the usage-policy rewrite table do not change when Google ships a new engine.

The split, and why it matters:

| Question | Lives in |
| --- | --- |
| What does a BadCode panel look like? | `badcode-art-direction` (stable) |
| How do I make *this engine* do that? | here (refreshed per model version) |
| How do I drive the browser? | `docs/superpowers/flow-selectors.md`, `flow-video.md` |

~~Nothing in here has been wired into a skill yet.~~ **As of 2026-08-14, one thing is.** The
engine-*agnostic* half of the motion research — never render a falling object in flight, name the
shutter, state constraints positively — now lives in
[`animate-slide`](../../.claude/skills/animate-slide/SKILL.md#what-the-model-cannot-do-whichever-model-it-is),
because it survives an engine change and a skill is where a rule gets *applied*. Everything
engine-specific stayed here. That split is the same one the table above describes, and it is the
test to apply next time: **would this still be true on a different model?** If yes, it belongs in
the skill.

## 🖐 Standing rule: engine research lands here

**Any research about how a Flow engine behaves goes in this folder — always, and at the time it
is found.** Not in a story's prompt file, not in a commit message, not only in the conversation
where it came up.

The test is *"would this still be true for a different story?"* If yes, it belongs here:

| Finding | Where it goes |
| --- | --- |
| Omni ignores negative prompts | **here** — true of every clip we ever make |
| Karen's river drop needs the phone screen lit | the story's prompt file — true of one shot |
| Nano Banana's aspect-ratio ceiling | **here** |
| Susan's Character reference is in the wrong register | `docs/stories/karen/` |

Research is worth roughly nothing the second time somebody has to find it again. The 2026-08-14
Omni prompt-craft pass exists because a shot failed, the answer was already three clicks away in a
blog post, and nobody had written it down after the first time.

Tag every claim with an [evidence tier](#evidence-tiers), date the section, and cite the URL — an
untiered, undated claim is indistinguishable from a guess in six weeks.

## Contents

| File | Model | Surface |
| --- | --- | --- |
| [`nano-banana-2.md`](./nano-banana-2.md) | Gemini 3.1 Flash Image | Flow's **default image model**, all users, zero credits |
| [`omni-flash.md`](./omni-flash.md) | Gemini Omni Flash | Flow video, requires AI Plus / Pro / Ultra |

## The one distinction that will bite you

**Most of the hard numbers below come from the Gemini API docs. We drive Flow through a browser.**

Flow is a UI wrapper over these models and it does not expose everything the API does — and
occasionally exposes things the API doesn't. Where a limit is sourced from the API, it tells you
what the *model* can do, which is an upper bound on what Flow can do, not a promise about the
Flow UI. Anything marked `[untested]` has not been confirmed against our actual Flow session.

## Evidence tiers

Every claim in these files carries a tag. Respect them.

- `[vendor]` — Google's own docs, model cards, or announcements. Reliable on capability, silent
  on failure modes, and occasionally aspirational about preview features.
- `[community]` — practitioner reports, developer-forum threads, subreddits. This is where
  failure modes live. Directionally true, frequently out of date, sometimes about the *previous*
  model version.
- `[yt]` — harvested from YouTube tutorial transcripts (see below). A cut above `[community]` when
  the claim is *demonstrated on screen inside Flow*, and no better than it otherwise: most of these
  creators sell a course or a competing platform, and many test in third-party wrappers
  (Higgsfield, OpenArt, Cue AI) where limits and filtering differ from Flow's.
- `[runware]` — a model **host's** own documentation (Runware, and any equivalent). Added
  2026-08-14. Above `[community]` because it is a doc rather than a blog post and the vendor has
  to make the model work; below `[vendor]` because it describes their surface, not Google's. In
  practice the most *craft-useful* tier we have found — hosts write the prompting guidance Google's
  API reference omits.
- `[untested]` — we have not confirmed it in our own Flow session. Do not build a rule on it.
- `[confirmed <date>]` — we ran it and watched what happened. This is the only tier that earns a
  hard rule.

The most valuable section in `badcode-art-direction` — the usage-policy rewrite table — is entirely
`[confirmed]`-tier knowledge that came from watching half the camping recut get blocked. No blog
would have given us it. Treat everything here as hypotheses until a calibration run promotes them.

**`omni-flash.md` has its first `[confirmed]` entries as of 2026-08-14** — five of them, out of a
file otherwise built entirely from reading. They came from one shot failing four times and working
on the fifth, which is the cheapest calibration run we will ever get and an argument for recording
failures in the detail the story files now do. See
[What we actually confirmed](./omni-flash.md#what-we-actually-confirmed-2026-08-14).

## Calibration protocol (how `[untested]` becomes `[confirmed]`)

1. Pick ~8 prompts from existing storyboard records (`docs/stories/*/storyboard/pNN.md`) that
   already have known-good outputs under the previous engine.
2. Re-run them unchanged through the `flow` MCP tools on the current engine.
3. Diff the results against the recorded originals. Note what held, what drifted, what blocked.
4. Promote only what survived to `[confirmed <date>]`. Demote or delete the rest.
5. If a run surfaces a **new policy-block trigger** or a new identity-level rule, that finding
   belongs in `badcode-art-direction`, not here — it is the same category as what's already there.

## Refresh policy

Restate the verification date at the top of each file when you touch it. Google shipped Nano
Banana → Nano Banana 2 in six months and Omni Flash is three months old and still in public
preview, so assume anything unstamped is stale.

**Search hygiene:** a large fraction of "Nano Banana prompting" content online describes the
*original* Nano Banana (Gemini 2.5 Flash Image, Aug 2025), not Nano Banana 2 (Gemini 3.1 Flash
Image, Feb 2026). Date-check before you believe it.

## Sources

Primary, in descending order of usefulness:

- [Ultimate prompting guide for Nano Banana](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) — Google Cloud. The single best written artifact on the image side.
- [Nano Banana 2 announcement](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) — blog.google
- [Introducing Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/) — blog.google
- [Gemini Omni Flash model card](https://deepmind.google/models/model-cards/gemini-omni-flash/) — DeepMind. Thin on specs, honest about failure modes.
- [Generate and edit videos with Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni) — Gemini API docs. The real parameter space.
- [Omni Flash is currently not usable as a serious creative workflow tool](https://discuss.ai.google.dev/t/omni-flash-video-generation-is-currently-not-usable-as-a-serious-creative-workflow-tool/146264) — Google AI Developers Forum. Best single source of observed failure modes.

Secondary aggregator blogs (Fliki, Magnific, invideo, PixVerse, coursiv, explainx) surfaced during
research. They give a fast map but are content marketing for competing tools and heavily recycled.
Use them to generate hypotheses to test, never as the source of a rule.

### The YouTube pass (2026-08-12)

YouTube turned out to be the highest-yield source for *Flow UI mechanics* — the tools, panels and
model pickers that no written doc covers, because Google's docs describe the API and the blogs
describe the model. Watch-worthy findings are folded into the two model files with `[yt]` tags and
per-file source tables.

Reproduce or refresh it like this:

```bash
# enumerate candidates with view counts, across several queries
yt-dlp --flat-playlist --print "%(view_count)s|%(duration)s|%(channel)s|%(id)s|%(title)s" \
  "ytsearch20:Nano Banana 2 tips"        # repeat per query, sort -u

# then harvest auto-caption transcripts for the selected ids
scripts/fetch-youtube-transcripts.sh -h   # same yt-dlp recipe, channel-scoped
```

Notes from doing it once:

- `yt-dlp` was not installed and there is no pip/pipx on this machine — the standalone binary from
  the yt-dlp GitHub releases page drops into `~/.local/bin/yt-dlp` and works.
- `--flat-playlist` on a search returns `view_count` but **not** `upload_date` (it comes back `NA`),
  so you can rank by views but must judge recency from the topic and the content itself.
- Filter to tutorials — `tutorial|tips|guide|how to|prompt|explained|master|formula` against the
  title, with a duration floor to drop Shorts — or you harvest a lot of reaction videos.
- Transcripts are **research input**. Leave them in scratch; do not commit them.
