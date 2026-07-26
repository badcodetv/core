# The BadCode Agent Orange image

**Status:** v1 spec, 2026-07-16. "Image" here means the full worker environment: the Docker
image the `badcode` Agent Orange project launches sessions from, plus the MCP tools and Claude
skills available inside it. Fleet design: [`agent-orange.md`](./agent-orange.md).

Agent Orange runs stdio MCP servers *inside* the session container (spec §4.3), so anything a
worker needs must be baked into this image. Credentials are never baked — MCP config names env
vars (`${X_API_KEY}`), the operator sets them in the stack env + `AGENTKIT_MCP_ENV` allowlist
(spec §4.4).

## 1. Docker image contents

Base: `node:22` (Debian, not alpine — `sharp` needs glibc prebuilds).

- **The badcode repo** baked in at `/opt/badcode` (`git clone` at build; workers can
  `git pull` at session start for freshness — the repo is the content source of truth:
  canon, storyboards + prompt revision logs, voice docs, this marketing plan).
- `npm install` pre-run for all workspaces; `badcode` CLI on PATH
  (`packages/cli`, via `tsx`), `sharp` working.
- `.claude/skills/` present (they live in the repo — free).
- GCS access via `${GOOGLE_APPLICATION_CREDENTIALS}` env reference for `badcode push/pull` and
  `assets-build` against the bucket.
- Utilities: `git`, `ffmpeg` (clip slicing from downloaded masters), `imagemagick` (optional),
  `jq`, `curl`.

Built as an Agent Orange derived image per the layered-installations pattern
(`agent-orange/installations/`, `docs/16-derived-images.md`): `core` → `badcode`. The
Dockerfile lives with the Agent Orange project's installation, not in this repo.

## 2. What runs headlessly today (safe to give workers)

| Capability | How | Used by |
| --- | --- | --- |
| Resolve page → image + exact prompt + characters | `badcode panel` (JSON, no browser) | image-maker, clip-maker, copywriter (making-of) |
| Assemble/print generation prompts | `badcode prompt`, `badcode flow-prep` | image-maker |
| Asset pipeline: WebP variants + manifest | `badcode assets-build` | clip-maker, publisher prep |
| Bucket I/O | `badcode push / pull / status` | any |
| Comic scaffold from comic.json | `badcode generate` | (rare) |
| Site build/typecheck | `npm run build / typecheck` | (rare) |
| Read canon, storyboards, revision logs, voice docs | plain files in `/opt/badcode` | all content workers |
| Slice video/audio masters | `ffmpeg` | clip-maker |

## 3. What is NOT headless (the honest matrix)

| Capability | Why not | Interim pattern |
| --- | --- | --- |
| Flow image generation/editing (`flow_*` MCP) | Needs a logged-in Chrome on CDP :9222 with the Google/Flow ULTRA session (`scripts/flow-chrome.sh` on Kai's machine); login is manual by design | Worker produces the finished prompt + spec, `request_human_attention`; Kai runs it attended |
| Flow video (Veo) | Same, plus manual credit-approval gates | Same |
| Suno (music) | No API; `suno-prompt` skill outputs copy-paste blocks by design | Worker outputs the Suno prompt block; human pastes |
| Final video cuts | Deliberate human step (`music-video-short` contract ends at edit-plan) | Worker delivers edit plan + assets |

Future options (not commitments): expose Kai's logged-in Flow Chrome to workers over a
network-reachable CDP/MCP bridge (turns "attended" into "Kai's machine on"), or a persistent
authenticated browser container — an experiment with real session/ToS fragility, park it.

## 4. MCP surface for the project

Project-level `mcp_config` (all workers), per spec §5 — plus worker-level extras where noted
in the fleet table. Everything below needs the operator to obtain credentials once (env vars):

| Server | For | Notes / access reality |
| --- | --- | --- |
| Agent Orange core (memory, prompts, workers, subscriptions, schedules, `request_human_attention`) | all | served by agentd, non-overridable |
| Web search | trend-scout | any search MCP (e.g. Brave/SerpAPI-backed) |
| X/Twitter posting + metrics | publisher, analyst | API tier required for write access (paid); budget line item |
| Meta (Instagram + Facebook) | publisher, analyst | via Meta Business Suite app review; IG API needs the FB page link |
| YouTube Data API | publisher, analyst | upload quota is tight; uploads may stay human-attended anyway (big files) |
| TikTok Content Posting API | publisher, analyst | approval-gated program; fallback = drafts + human posts from phone |
| LinkedIn API | publisher | low priority; fallback = human posts the mirror |
| Gmail | secretary | inbox + outreach |
| Email list provider (Buttondown/Mailchimp) | secretary | Transmissions list |
| badcode CLI (already in-image; not an MCP server — Bash) | content workers | — |
| flow MCP (`packages/flow-mcp`) | image-maker, clip-maker | binaries in image, but functional only when a reachable logged-in Chrome exists (§3) |

**Pragmatic sequencing:** the platform APIs are the long pole (approvals, tiers, costs). Week 1
can run with ZERO social APIs: workers produce finished drafts and `request_human_attention`;
Kai/Jack post by hand. That's still the whole content engine running — the posting arm
automates platform-by-platform as credentials land. Wire in roughly this order:
X (fastest API) → Meta → YouTube → TikTok → LinkedIn.

## 5. Skills inside Agent Orange

The repo's skills assume an interactive human answering gates. Inside a worker session, the
*event payload* plays the human's role — the instruction text carries the decisions upfront.

| Skill | Fit | Adaptation |
| --- | --- | --- |
| `suno-prompt` | clean | pure text-out already |
| `new-image` | good | prompt-padding + critique loop works; generation step hits the Flow constraint (§3) |
| `edit-panel` | good | `badcode panel` resolution is headless; `flow_edit_image` needs attended Flow |
| `badcode-art-direction` | partial | the plan→critique loop reads well non-interactively; generation attended |
| `music-video-short`, `make-comic`, `animate-slide` | gated by design | keep human-in-the-loop; workers prepare stage inputs only |
| `new-idea`, `new-story` | n/a for marketing | content-creation side, stays with humans + Claude Code |

Workers should treat skills as recipes to read (`/opt/badcode/.claude/skills/*/SKILL.md`), not
interactive flows to invoke — the worker's own prompt + the skill text is enough.
