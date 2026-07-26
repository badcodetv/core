# Running the marketing plan on Agent Orange

**Status:** v1, 2026-07-16. Designed against the Agent Orange product spec
(`agent-orange/docs/17-product-spec.md`, drafted 2026-07-15 — "the great simplification").
The plan itself is [`plan.md`](./plan.md); the seed prompt is
[`marketing-manager-prompt.md`](./marketing-manager-prompt.md); the worker container image is
specified in [`badcode-image.md`](./badcode-image.md).

BadCode marketing is the **first real Agent Orange use case**. This doc does two jobs: define
the worker fleet that runs the plan, and state exactly which Agent Orange capabilities we
depend on — including the ones not yet built (§2), which double as requirements to paste back
into an Agent Orange thread.

---

## 1. The contract we assume (from spec §s)

Everything below is in `docs/17-product-spec.md` unless marked as a gap in §2:

- **Worker** = `{name, description, system_prompt, mcp_config, enabled}` — a data row, not a
  process (spec §3, §6.1). A **job** is one session run for a worker, triggered by an event.
- **Job composition** (spec §6.2): core preamble + project prompt + worker prompt + memory
  briefing; MCP = core ∪ project ∪ worker. **The triggering event's payload is rendered as the
  first user message.** This is the load-bearing mechanic: the worker's prompt says who it is;
  the event text says what to do *right now*.
- **No built-in cron** (spec §8.5, §10). An external scheduler POSTs
  `POST /agent/events {type, payload}` with a project token. A "schedule" is therefore a list
  of `{cron expr, event type, payload text}` entries living outside Agent Orange. Per-trigger
  input text = the payload: `10:00 → "write the morning transmission"`, `17:00 → "write the
  evening slice caption"` — same worker, different instruction.
- **Memory** (spec §7): append-only labeled store, core MCP tools
  `memory_create / memory_search / memory_get`; rolling-summary briefing by convention (an
  archivist-style worker maintains `kind=rolling-summary` memories).
- **Events + subscriptions** (spec §8): `worker.finished` (payload includes the full
  transcript) and `worker.failed`; subscriptions route event → worker with optional payload
  filters; depth cap 8; per-project concurrency cap.
- **Prompt management tools** (spec §9): `worker_list`, `worker_prompt_read/write` (wholesale
  rewrite, auto-drops a `kind=prompt-revision` memory), `project_prompt_read/write`. This is
  how the consultant loop self-edits — spec §8.6's acceptance scenario *is* our consultant loop.
- **`request_human_attention`** (spec P6): the sanctioned way a background worker involves a
  human — notify a configured channel with a link to the session, end the turn, continue when
  the human's reply arrives as the next message in the thread. **Staged autonomy is purely a
  prompt edit** (spec P6, verbatim). No approval queues, no draft UI — deliberately.
- **Custom images per project** (spec atom 3, §4.3): stdio MCP servers run inside the
  container, so their binaries ship in the project base image — that's the BadCode image
  ([`badcode-image.md`](./badcode-image.md)).
- **Credentials** (spec §4.4): MCP config names env vars (`${X_API_KEY}`); the operator sets
  them once in the stack env + `AGENTKIT_MCP_ENV` allowlist. Social API keys never touch a DB
  or this repo.

## 2. Requirements back to Agent Orange (the paste-across list)

What this use case needs that the spec doesn't yet cover, in priority order. Items 4–5 are
already specified, just unbuilt — listed so the dependency is explicit.

1. **`request_human_attention` needs a real spec + implementation.** It's named in P6 as "(§9)"
   but §9's tool list doesn't define it. Needed shape: core MCP tool, args
   `(reason, summary_of_what_needs_deciding)`; effect: post to a per-project configured
   notification channel (email/webhook — operator config) a message containing the reason and
   a **link to the session thread in the Agent Orange UI**; the session ends its turn; the
   human opens the thread and whatever they type is delivered as the next message in that same
   session. This is the entire staged-autonomy mechanism — nothing else gets built for approval.
2. **Worker lifecycle as MCP tools.** §9 gives `worker_list` + `worker_prompt_read/write`, but
   the marketing-manager must *create* and *configure* workers from inside a session. Needed:
   `worker_create(name, description, system_prompt, mcp_config)`,
   `worker_update(name, description?, mcp_config?, enabled?)`, `worker_delete(name)` — same
   semantics as the §6.5 HTTP CRUD, exposed as core MCP tools (with the same
   `kind=prompt-revision`-style provenance memory on create/update).
3. **Schedule management reachable from inside a session.** Since cron is external by design,
   the manager needs an MCP surface over whatever the scheduler is:
   `schedule_list()`, `schedule_create(cron, event_type, payload)`,
   `schedule_update(id, …)`, `schedule_delete(id)`. Simplest honest implementation: a tiny
   scheduler sidecar (or systemd/cron wrapper) that owns a `schedules` list, ticks, and POSTs
   `/agent/events`; its config file is what the MCP tools edit. Without this, the manager can
   *propose* schedule changes via `request_human_attention` but not enact them — acceptable
   for week 1, not for the vision.
4. **Per-worker/session MCP plumbing** — spec Gap G1 / Track A. All social tools hang off this.
5. **Workers/memory/events/subscriptions layer** — spec Tracks C/D/E (all currently unchecked).
   The fleet below cannot exist until C1/C2, D1/D3, E1–E4 land.
6. **`emit_event(type, payload)`** (nice-to-have): lets a worker hand work onward explicitly
   (e.g. trend-scout finishes a brief → wake copywriter with *just the brief*, not the whole
   transcript). Workaround exists — subscribe copywriter to
   `worker.finished {worker: trend-scout}` and let it fish the brief from the transcript or
   memory — so this is quality-of-life, not blocking.
7. **Subscription tools already planned** (§9 mentions `subscription_list/create/delete` as
   core MCP): confirmed needed — the manager wires the consultant with them.

## 3. The worker fleet

Project: **`badcode`** (one Agent Orange project = the company; marketing is its first
department). Base image: the BadCode image. Project prompt: condensed BadCode identity +
voice rules + link/UTM conventions (shared by all workers).

Memory label conventions (project-wide, seeded as a `kind=convention` memory):
`kind` ∈ `brief | draft | posted | metric | lesson | strategy-change | convention |
rolling-summary | prompt-revision`, plus `campaign=<story>`, `platform=<platform>`,
`worker=<name>`.

| Worker | Goal (one line) | Key MCP tools (beyond core) | Runs |
| --- | --- | --- | --- |
| `marketing-manager` | Own the strategy; make the fleet match it; improve both. | worker/schedule/subscription mgmt, `request_human_attention` | daily reconcile + weekly self-critique |
| `trend-scout` | Find this week's real-world angles on each active moral core; write briefs to memory. | web search | Mon (funnel brief) + daily (engagement targets) |
| `copywriter` | Turn briefs/cores into platform-native posts in the narrator's voice. | web fetch (read links in briefs) | daily transmissions + per brief |
| `image-maker` | Brand stills for posts; exact Flow prompts when a human-attended session isn't available. | flow MCP (when attended), badcode CLI | per request (event from copywriter/manager) |
| `clip-maker` | Slice cores into shorts/teasers; produce edit plans per `music-video-short` contract. | badcode CLI, flow MCP (attended) | Tue/Fri/Wed slots |
| `publisher` | Take finished content live: stage-1 = `request_human_attention` for go/no-go, then post; log `kind=posted`. | social posting MCP servers, `request_human_attention` | per finished draft |
| `analyst` | Weekly metrics sweep per platform → `kind=metric` memories + a plain-english "what worked" note. | platform analytics MCP/APIs | Sun 18:00 |
| `secretary` | Inbox + community: check email every 2h, draft replies, manage the Transmissions list; collab outreach drafts (human-gated). | Gmail MCP, `request_human_attention` | every 2h |
| `consultant` | Read finished jobs against voice + strategy + analyst data; rewrite worker prompts with concrete lessons; record `kind=lesson`. | `worker_prompt_read/write` (core) | subscribed to `worker.finished` |
| `archivist` | Keep every worker's `kind=rolling-summary` briefing fresh (spec §7.4 convention). | memory tools (core) | subscribed to `worker.finished` |

Notes:

- **Roles are prompts, not code** (spec P2) — this whole table is data the manager maintains.
- `consultant` subscribes to `worker.finished` with no worker filter but its prompt tells it to
  sample (always review `publisher` and `copywriter`; skip `archivist`/`analyst` runs unless
  something looks off) — the "if this doesn't concern you, finish immediately" pattern from
  spec §8.3.
- Content that needs Flow/Suno generation is human-attended for now: the worker produces the
  brief + exact prompt and calls `request_human_attention`; Kai runs the generation on the
  logged-in machine ([`badcode-image.md`](./badcode-image.md) §3 has the honest matrix).

## 4. The schedule (external cron → events)

Every row is one scheduler entry: `{cron, event_type, payload}`. Event types are per-worker
(`run.<worker>`) with one subscription each (`run.<worker>` → `<worker>`); the payload is the
instruction. UK times.

| Cron | Event | Payload (the per-trigger instruction) |
| --- | --- | --- |
| `0 8 * * *` | `run.marketing-manager` | "Reconcile the workforce: make workers, subscriptions and schedules match your manifest. Report drift you fixed." |
| `0 19 * * 0` | `run.marketing-manager` | "Weekly review: read this week's metric + lesson memories; critique the strategy and your own system prompt; enact improvements (prompt edits, cadence changes) and record each as a strategy-change memory. Anything human-scale, request human attention." |
| `0 9 * * *` | `run.copywriter` | "Write the morning transmission (X, mirror to IG/TikTok text). In voice, off today's news if it serves." |
| `0 10 * * 1` | `run.trend-scout` | "Find this week's funnel angle on the active campaign's moral core. Write a brief memory (kind=brief) with links + suggested treatment." |
| `0 14 * * *` | `run.trend-scout` | "Surface 3–5 live threads/videos worth an in-voice reply today; brief memory for the copywriter." |
| `0 17 * * 2,5` | `run.clip-maker` | "Produce the next slice/serialization installment for the active campaign per the plan." |
| `0 12 * * 3` | `run.copywriter` | "Making-of piece: pull the latest panel revision story from the repo records and write it up." |
| `0 11 * * 4` | `run.trend-scout` | "Music/community day: playlist, repost and collab targets for the current track; brief for secretary outreach." |
| `0 */2 * * *` | `run.secretary` | "Please check the email and respond; anything needing a decision, request human attention." |
| `0 18 * * 0` | `run.analyst` | "Weekly sweep: pull per-platform numbers, write metric memories, and a short plain-english 'what worked / what died' note." |

Chaining that isn't scheduled: `worker.finished` subscriptions (consultant, archivist), and
copywriter → publisher via `worker.finished {worker: copywriter}` (or `emit_event` once it
exists).

## 5. Bootstrap — from nothing to the fleet

The chicken-and-egg answer: **the manifest lives in the manager's prompt, and the manager is
idempotent.**

1. **Human, once:** create the Agent Orange project `badcode`; set project settings (base
   image = BadCode image, project prompt, project-level MCP config); set the credential env
   vars + `AGENTKIT_MCP_ENV`; create ONE worker — `marketing-manager` — pasting
   [`marketing-manager-prompt.md`](./marketing-manager-prompt.md) as its system prompt; stand
   up the external scheduler with just the two manager entries (daily reconcile + weekly
   review).
2. **First reconcile run:** the manager reads its manifest, calls `worker_list`, finds nobody,
   and creates the entire fleet + subscriptions + remaining schedule entries. Because the
   procedure is *diff-then-fix*, the same daily event is also drift repair and rollout of
   manifest changes — creating the fleet and maintaining it are the same operation.
3. **Growth beyond the manifest:** the weekly self-critique reviews results and may add,
   retire, reschedule, or re-prompt workers — every change recorded to memory with reasoning,
   human-gated via `request_human_attention` while we're in stage 1.

Two standing loops, exactly as Kai framed it:
**reconcile** (fleet ≙ strategy) and **self-critique** (strategy ≙ results).

## 6. The staged-autonomy ladder

All stages are prompt wording — no features (spec P6).

| Stage | Publisher prompt says | Graduation trigger |
| --- | --- | --- |
| 1 (now) | "Before posting ANYTHING publicly, `request_human_attention` with the draft and wait for approval; treat the human reply as editorial direction." | Consultant + humans agree the voice is calibrated (~4–6 weeks of approvals with few edits). |
| 2 | "Post text posts, replies and reposts directly. Anything with video, third-party material, or a named person still requires human attention." | Clean run at stage 2; fair-use pieces consistently unremarkable. |
| 3 | "Post directly. Request human attention only for irreversible/risky calls (platform policy edges, anything targeting a person, spend)." | — (consultant + analyst remain the safety net; the weekly review can demote a stage as easily as promote) |

Stage changes are made by the manager editing the publisher's prompt via
`worker_prompt_write` — itself human-approved through `request_human_attention` until stage 3.
