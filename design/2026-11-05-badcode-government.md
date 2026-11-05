# The BadCode Government in Bob — Design & Implementation Plan

> **EXECUTION RULES (for agents):** Work ONE ticket at a time, in order unless
> dependencies say otherwise. Only the orchestrator changes ticket Status;
> workers may only append to Notes and the Discovered Issues Log. A ticket's
> checkbox is checked only after its Validation commands have been re-run by
> the orchestrator and pass. Do not expand scope; log surprises in the
> Discovered Issues Log instead.

Status: proposed (review applied; reworked 2026-11-05 to one cabinet session + one rolling PR)
Relates: Bob project `badcode` (created 2026-11-05, replacing `marketing`; Bob repo commit `2efb663`);
Bob repo `~/projects/badcode/bob` (`badcodetv/bob`); this repo `badcodetv/core`;
site `apps/site/README.md`; Future Proof canon `docs/stories/future-proof/`.

## Context

BadCode (see `CLAUDE.md`) wants a **BadCode government**: a cabinet of autonomous AI ministers
that read the world's news every day, form positions in BadCode's voice, and grow over time. Two
public outputs: (1) an **ever-moving manifesto**, kept in git and shown on the website's GOVT
channel; (2) **social media statements**, drafted and posted by people.

It runs in **Bob** (`https://bob.box.badcode.tv`), BadCode's own service for running agent
sessions. Facts about Bob this plan relies on (all verified 2026-11-05):

- A Bob project has **workers** (an engine, a model, an effort and a system prompt, versioned in
  Postgres with a required *why*), a shared **project prompt**, **schedules** (cron + IANA timezone
  + first message + `keep_sessions`) and **memory** (`~/projects/badcode/bob/README.md`, "Workers
  and the project prompt" and "Bob's tools").
- **Scheduled runs in one project never overlap.** They queue in firing order and run one at a time
  (`bob/api/internal/store/schedules.go:155-180`, `NextQueuedRun`). So a 06:00 job always waits for
  a 05:00 job that is still running. This plan uses that for ordering.
- Missed firings catch up for 6 hours (`bob/api/internal/schedule/schedule.go:13`).
- **Memory**: append-only, at most 24 KB of content (`bob/api/internal/store/memories.go:30`), at
  most 32 labels, keys and values `[A-Za-z0-9._-]` and ≤63 characters
  (`bob/api/internal/labels/labels.go`). Search takes a kubectl-style selector (`k=v`, `k in (a,b)`,
  `exists k`, comma = AND; no OR), free text, `since`/`until` (`"24h"` works) and `latest_per`.
- Bob runs Claude through the Agent SDK with `permissionMode: 'bypassPermissions'` and Claude
  Code's preset prompt (`bob/runtime/src/claude.ts:14-32`). So the ordinary subagent tool and web
  search work today. The **Workflow** tool exists in the SDK (`0.3.274`); with `enableWorkflows` unset it
  follows "default by plan once the feature is available", so T1 sets it explicitly (`runtime/node_modules/@anthropic-ai/claude-agent-sdk/sdk.d.ts:6797-6813`).
- Each project container works in `/project/work` and can push to GitHub over https with
  `GITHUB_TOKEN` (Bob README, "Run it locally" onward). The `badcode` project's token is the old
  marketing token, which has already cloned `badcodetv/core`. The runtime image has **no `gh`**
  (`bob/runtime/Dockerfile:11`).
- An outside MCP client (this repo's Claude Code, a GitHub Action) can call Bob with
  `Authorization: Bearer <BOB_MCP_KEY_BADCODE>` at `https://bob.box.badcode.tv/mcp` (JSON-RPC
  `tools/call`, no `initialize` needed; verified with `curl`). The key is in
  `~/projects/badcode/bob/.env.box` and is registered in Kai's local `~/.claude.json` for this folder.
- A session's web searches share a budget of about 200, across all its subagents
  (memory note `websearch-budget-per-session`).

## Architecture

```
                       Bob project "badcode"   (all times Europe/London)
 ┌────────────────────────────────────────────────────────────────────────────┐
 │ 05:00  NEWS GATHERER (Opus) ──Workflow news-sweep.js──► 24 Sonnet researchers│
 │        one per beat; dedupe; label ─────────► ~30-60 news memories          │
 │                                                + 1 news-digest memory        │
 │ 06:00  CABINET (Opus, one session): chairs as PM, speaks as each of the     │
 │        ten ministers from its brief; reads review comments on the open PR   │
 │        ──► commits onto THE rolling PR ──► decision + minutes memories      │
 │        ──► request_human_attention (dot in Bob)                             │
 │ Sun 20:00  CABINET SECRETARY (Opus): week's decisions, merges, comments     │
 │        ──► edits minister briefs, commits onto the same rolling PR          │
 └────────────────────────────────────────────────────────────────────────────┘
          │ one rolling PR (updated daily)            ▲ workers + briefs + schedules
          ▼                                           │
   badcodetv/core ── Kai or Jack merge ──► GitHub Action bob-sync.yml
   (reviewed here in Claude Code, or in a Bob chat)    runs scripts/government/sync-bob.mjs
```

**Decisions (Kai, 2026-11-05):**

1. **Cabinet of ten**: Prime Minister; Chancellor of the Exchequer; Foreign Secretary; Home
   Secretary; Education; Defence; Health; Work and Pensions; Housing; Energy and Climate. There is
   no Science/Technology post: AI and automation news is labelled for Work and Pensions and the
   Chancellor.
2. **UK cabinet, world news.** It's the government the UK would have if BadCode ran it, sent back
   from the future. Researchers put UK news first and cover world events for their effect on the UK.
   Ministers speak in the BadCode narrator's voice (`docs/voice.md`) to the reader in
   `docs/marketing/the-reader.md`.
3. **One cabinet session plays all ten ministers** (Kai, 2026-11-05, on Claude's advice). One
   Opus session chairs as PM and speaks as each minister from its brief, so it sees the whole day's
   news at once, settles clashes in the room, and writes the PR itself: no hand-off through memory.
   Each minister's persona is a **brief** in git (`docs/government/ministers/`), appended to the
   cabinet's prompt by the sync, so personas stay distinct, reviewable and evolvable. It may hand a
   heavy draft to a subagent, but it decides. Rejected: ten minister workers plus a PM (ten
   contexts that never see each other, a memory hand-off, ten times the runs); one PR per minister.
   The news gatherer and the Cabinet Secretary stay separate sessions: research would crowd the
   cabinet's context, and an editor should not mark its own work.
4. **Human merge is the publish gate.** Nothing an agent writes reaches `main` without Kai or Jack
   merging it. The review can happen in local Claude Code (`gh pr view`, the `bob` MCP) or in a
   Bob chat.
5. **Statements are draft files in the PR.** Nothing posts automatically. People post them, or
   hand them to the marketing `chief-of-staff` skill.
6. **Git is the source of truth for the whole government**: every worker (engine, model, effort,
   labels, prompt) and every schedule live in `docs/government/`. The government's shared text
   (`docs/government/shared.md`) is **prepended to each government worker's prompt by the sync**,
   not written into Bob's project prompt: `badcode` is one project for all of BadCode, and its
   project prompt reaches every chat, so the sync never touches it. A GitHub
   Action syncs them into Bob on every merge, so a merged persona change reaches the live worker
   automatically. Rejected: editing prompts directly in Bob (invisible unless someone looks).
7. **HR is the Cabinet Secretary**, a separate worker that runs weekly and edits the minister
   briefs on the rolling PR. It isn't called "chief of staff", because that is the marketing skill's name.
8. **Fan-out uses Claude Code's Workflow tool**, enabled in Bob's runtime. If Workflow is
   unavailable, the gatherer falls back to parallel batches of the ordinary subagent tool, and its
   prompt carries both paths.
9. **The manifesto sits under Future Proof on the site.** GOVT 1 keeps the existing promise
   ("We promise to enact Future Proof") on top, then each minister's current line. Teletext 401 is the cabinet index
   and 402–411 carry one minister each. Ministers must serve Future Proof and never contradict it.
   Deployment stays manual (`./stack site deploy`).

**Models.** All three workers use `claude-opus-5-5`; the researchers use `claude-sonnet-5-5`.
Engine `claude` throughout.

### Memory label scheme (the contract every prompt uses)

| Memory | Written by | Labels | Content |
| --- | --- | --- | --- |
| news item | gatherer | `kind=news`, `date=YYYY-MM-DD`, `topic=<topic>`, `region=uk\|world`, `weight=1\|2\|3`, and one key per post it concerns with value `y` (e.g. `health=y`) | headline; 3–5 sentence summary; why it matters to the UK; source URLs (at least one; two for weight 3) |
| digest | gatherer | `kind=news-digest`, `name=news-digest`, `date` | the day in ≤20 lines, each with its news memory id |
| decision | cabinet | `kind=decision`, `minister=<post>`, `date`, `action=manifesto\|statement\|both`, `pr=<number>` | what that minister decided and why, in its voice; the news ids it answers (only for ministers that acted) |
| minutes | cabinet | `kind=minutes`, `date`, `pr=<number>` (omit when no PR) | the meeting: who acted, who passed, clashes the PM settled, review comments answered, failures |
| feedback | cabinet | `kind=feedback`, `minister=<post>`, `pr=<number>`, `outcome=merged\|edited\|closed` | Kai's/Jack's review comments touching that minister; what changed between the PR and what was merged |
| personnel | Cabinet Secretary | `kind=personnel`, `minister=<post>`, `pr=<number>` | what changed in the brief and why, with evidence ids |

**Posts** (label keys, file names and `minister=` values): `prime-minister`, `chancellor`,
`foreign`, `home`, `education`, `defence`, `health`, `work-pensions`, `housing`, `energy-climate`.
**Topics:** `economy`, `work`, `welfare`, `housing`, `health`, `education`, `crime-justice`,
`migration`, `foreign`, `defence`, `energy-climate`, `tech-ai`.

The cabinet's read for each post is `label_selector: "kind=news,date=<today>,exists <post>"` with
`limit: 100`; a post's history is the newest 10 of `kind=decision,minister=<post>` and of
`kind=feedback,minister=<post>`. **Search returns 500-character snippets**: every reader then calls
`memory_get` on each id it needs in full.

### The rolling PR (Kai, 2026-11-05: one PR to look at, ever)

- **There is never more than one open government PR.** Branch `government/rolling`, label
  `government`, title `Government: since YYYY-MM-DD` (the date of its first entry). The cabinet and
  the Cabinet Secretary both commit to it. If Kai and Jack don't look for a week, they find one PR
  holding a week of changes, not seven.
- **Each run updates it**: new commits on the branch, and the PR body **rewritten** with a short
  summary of the whole PR on top, then a dated changelog (newest first, one entry per run, each
  listing what each minister changed, or "nothing today", with the news ids it answers). `gh pr edit
  --body-file`. Ministers read their current text **from the rolling branch**, so each day builds
  on the unmerged text and on any fixups a reviewer pushed.
- **Review comments steer it.** Each cabinet run first reads the review comments added since its
  last entry and acts on each (changes the files, or replies on the PR saying why not).
- **Merged or closed ends it.** The next run reads the finished PR (comments, and what changed
  between its last commit and what was merged), writes `kind=feedback` memories per minister (never
  twice for the same `pr` and `minister`; check with `memory_search` first), deletes the remote
  branch if it still exists, and starts a fresh `government/rolling` from `origin/main`. A closed PR
  means rejected: the cabinet does not re-propose its text unchanged.
- **Never share a checkout.** `/project/work` is shared by every chat in the container. Writers
  work in their own worktree: `git -C /project/work/core fetch` then `git -C /project/work/core
  worktree add /project/work/gov-<run id> <origin/government/rolling or origin/main>`, and
  `git worktree remove` at the end. Readers use `git show origin/<branch>:<path>`. Commit with
  `-c user.name="BadCode Government" -c user.email=government@badcode.tv` (scheduled turns otherwise
  author as `schedule:<uuid>`). Push with `git push origin HEAD:government/rolling`.
- The diff touches only `docs/government/manifesto/*.md` and `docs/government/statements/<date>/*.md`
  (cabinet), or `docs/government/ministers/*.md` (Cabinet Secretary).
- **Cadence:** daily for now; changing it is one line in `schedules.json`.

## File Structure

**Bob repo (`~/projects/badcode/bob`):**

| Path | Action | Purpose |
| --- | --- | --- |
| `runtime/src/claude.ts` | Modify | pass `settings: { enableWorkflows: true, workflowSizeGuideline: 'large' }` to `query()` |
| `runtime/src/claude.test.ts` *or* an existing test file | Create/Modify | assert the options object carries the setting |
| `runtime/Dockerfile` | Modify | install the GitHub CLI (`gh`) from GitHub's apt repository |
| `README.md` | Modify | one paragraph under "Bob's tools": Workflows on, `gh` present |

**This repo (`badcodetv/core`):**

| Path | Action | Purpose |
| --- | --- | --- |
| `docs/government/README.md` | Create | how the government works, the label scheme, how to review the daily PR here or in Bob, how to change a minister |
| `docs/government/shared.md` | Create | text the sync prepends to every government worker's prompt: frame, UK lens, voice and reader rules, the cabinet, the label scheme, the git rules |
| `docs/government/workers/<worker>.md` ×3 | Create | front matter + system prompt: `news-gatherer`, `cabinet`, `cabinet-secretary` |
| `docs/government/ministers/NN-<post>.md` ×10 | Create | one brief per minister (persona, remit, watched topics); appended to the cabinet's prompt by the sync |
| `docs/government/schedules.json` | Create | the 3 schedules; `enabled: false` until T16 |
| `docs/government/workflows/news-sweep.js` | Create | the gatherer's Workflow script |
| `docs/government/manifesto/00-prime-minister.md` | Create | PM preamble (seed) |
| `docs/government/manifesto/01-chancellor.md` … `09-energy-climate.md` | Create | one per minister (seed), order: chancellor, foreign, home, education, defence, health, work-pensions, housing, energy-climate |
| `docs/government/statements/README.md` | Create | the statement draft format |
| `scripts/government/sync-bob.mjs` | Create | git → Bob sync (dry run by default, `--apply` to write) |
| `scripts/government/sync-bob.test.mjs` | Create | vitest unit tests (picked up by root `npm test`: `vitest run --dir scripts`) |
| `.github/workflows/bob-sync.yml` | Create | runs the sync on merge to `main` |
| `apps/site/build.mjs` | Modify | read `docs/government/manifesto/*.md` into `C.government.manifesto`; plain-text bodies for `/government` and `/text/401`–`411` |
| `apps/site/src/tv.js` | Modify | GOVT 1 lists ministers under the promise; teletext 401 index + 402–411; 400 points to 401 |
| `apps/site/README.md` | Modify | the manifesto now comes from `docs/government/manifesto/` |
| `CLAUDE.md` | Modify | a repo-map row for `docs/government/` and a one-line pointer: "a government PR → `docs/government/README.md`" |

## Interfaces

**Worker file** (`docs/government/workers/<name>.md`), where `<name>` is the Bob worker name
(`news-gatherer`, `cabinet`, `cabinet-secretary`):

```
---
engine: claude
model: claude-opus-5-5
effort: high
labels: role=cabinet
include: ministers
---
<system prompt, markdown, everything after the closing --->
```

`labels` is a comma-separated `k=v` list. Front-matter keys are only `engine`, `model`, `effort`,
`labels`, `include` (only value: `ministers`) and an optional `tools:` comma list. The parser is
hand-written (no YAML dependency). It rejects unknown keys and a missing `engine`.

**Minister brief** (`docs/government/ministers/NN-<post>.md`): plain markdown, no front matter,
starting `### <Title> (<post>)`. Briefs are not workers; the sync appends them to the cabinet.

**`schedules.json`:**

```json
[{ "name": "gov-1-news", "worker": "news-gatherer", "cron": "0 5 * * *",
   "timezone": "Europe/London", "keep_sessions": 14, "enabled": false,
   "message": "Run today's news sweep." }]
```

Schedules: `gov-1-news` (gatherer, `0 5 * * *`); `gov-2-cabinet` (`0 6 * * *`); `gov-3-personnel`
(Cabinet Secretary, `0 20 * * 0`). **The names are numbered on purpose:** after an outage, Bob's
catch-up queues every missed firing in one tick, in schedule-*name* order
(`bob/api/internal/store/schedules.go:94`, `ORDER BY s.project, s.name`), so names must sort in
pipeline order. The cabinet also checks today's digest exists and stops with a `notice` if not.
Each message names the job in one line. Every prompt carries the procedure, not the message.

**`sync-bob.mjs`:**

- CLI: `node scripts/government/sync-bob.mjs [--apply] [--only workers|schedules]`.
  Without `--apply` it prints the plan (create/update/unchanged per item) and exits 0.
- Env: `BOB_MCP_KEY` (required), `BOB_URL` (default `https://bob.box.badcode.tv/mcp`),
  `GITHUB_SHA` and a commit subject (from `git log -1 --format=%s`) for `why`:
  `"git <short sha>: <subject>"`.
- Calls Bob's MCP tools over JSON-RPC `tools/call` with headers `Authorization: Bearer`,
  `Content-Type: application/json`, `Accept: application/json, text/event-stream`,
  `X-Bob-Client: bob-sync`. It accepts a plain JSON reply or an SSE `data:` line. The tool result is
  `result.content[0].text`; `result.isError` is a failure.
- Tools used: `worker_list` (with no args for names; **with `{name}` per worker** for the full record:
  the bare list omits `prompt` and `tools`, `bob/api/cmd/bob/tools_workers.go:99`), `worker_create`,
  `worker_update` (**send every field**: omitted fields are cleared), `schedule_list`,
  `schedule_create`, `schedule_update`. Tool names live in `bob/api/cmd/bob/tools_*.go`.
- **Prompt assembly** (`assemblePrompt`): `shared.md` + a blank line + the worker file body; if the
  front matter says `include: ministers`, then `\n\n## The ministers\n\n` + every
  `docs/government/ministers/*.md` in file-name order, separated by blank lines. So a merged brief
  change updates the live cabinet worker on the next sync, which is how a persona change reaches Bob.
- Normalise absent `tools` to `[]`; ignore `id`, `created_at`, `changed_at`, `next_at`, `last_run`
  on schedule rows when comparing.
- Only changed items are written. It **never deletes**. A worker or schedule in Bob but not in git
  is printed as `extra (not touched)`.
- Exported pure functions for tests: `parseWorkerFile(text) → {engine, model, effort, labels, tools, include, prompt}`,
  `assemblePrompt(shared, worker, briefs) → string`,
  `planSync(desired, current) → [{kind, name, op: 'create'|'update'|'unchanged', body}]`,
  `parseMcpReply(bodyText) → result` (throws on a top-level JSON-RPC `error` **and** on
  `result.isError`; Bob replies with plain JSON).

**Workflow `news-sweep.js`:** follows the Workflow script API (load the `workflow-authoring`
skill before writing it). `export const meta = { name: 'news-sweep', description, phases:
[{title:'Research'},{title:'Merge'}] }`. The gatherer passes `args: {date: "YYYY-MM-DD"}`, and the script uses `args.date` (Workflow scripts cannot call `Date.now()` or an argless `new Date()`). Research: 24 `agent()` calls in `parallel()`, one per beat,
`model: 'sonnet'`, each told to run **at most 6 web searches** and return items under a schema
`{items:[{headline, summary, why_uk, sources[], region, topic, weight, posts[]}]}`. Merge: one
agent dedupes across beats and returns the final list. The script **returns** the list. The
gatherer session, not the workflow, writes the memories, so a workflow failure never leaves half a
day written. The 24 beats: UK economy and cost of living; UK jobs and wages; UK welfare and
pensions; UK housing and rents; NHS and care; UK schools and universities; UK crime and courts;
UK migration and asylum; UK energy bills; climate and weather; UK politics and Parliament; UK
local government; AI and automation; big business and markets; tax and public finances; US;
EU and Europe; Russia and Ukraine; Middle East; China and Asia-Pacific; Africa and Latin America;
defence and security; global trade and supply chains; science and technology.

**Bob's MCP from the gatherer.** `memory_create` with the labels above. One call per item, then
the digest.

## Out of Scope

- Posting to any social platform, and any posting tool in Bob.
- Deploying the website (`./stack site deploy` stays a manual human step).
- Changing Bob's API, schema, memory or schedule semantics. The Bob changes are only T1–T2.
- A Science/Technology minister, or posts beyond the ten.
- Deleting the retired `marketing` project's data, or `schedule_delete`/`worker_delete` in the sync.
- Backfilling past news, and any analytics on statements.
- Writing BadCode policy positions by hand. The seeds in T10 are deliberately thin; the ministers grow them.

## Tickets

### T1: Turn on Workflows in Bob's Claude driver   [Status: pending | Model: sonnet]
- **Scope:** In `~/projects/badcode/bob/runtime/src/claude.ts`, add `settings: { enableWorkflows:
  true, workflowSizeGuideline: 'large' }` to the `query()` options (beside `skills: 'all'`). Keep
  everything else identical. Add a one-paragraph note to the Bob README under "Bob's tools".
- **Files:** `runtime/src/claude.ts`; a test beside the existing runtime tests (`runtime/src/*.test.ts`);
  `README.md`.
- **Acceptance criteria:** the options object passed to `query` contains the setting (test it by
  extracting the options builder into an exported function, or by asserting on a mocked `query`);
  runtime tests pass.
- **TDD:** yes
- **Validation:** `cd ~/projects/badcode/bob/runtime && rm -rf dist && npm run build && npm test` → all pass.
- **Depends on:** —
- [ ] done
- Notes:

### T2: Add the GitHub CLI to Bob's runtime image   [Status: pending | Model: sonnet]
- **Scope:** Install `gh` in `runtime/Dockerfile` from GitHub's official apt repository (keyring
  at `/etc/apt/keyrings/githubcli-archive-keyring.gpg`), in the same layer style as line 11.
  `gh` reads `GITHUB_TOKEN` from the environment, so it needs no login step.
- **Files:** `runtime/Dockerfile`; `README.md` (mention `gh` in the same paragraph as T1).
- **Acceptance criteria:** the image builds; `gh --version` runs inside it.
- **TDD:** no
- **Validation:** `cd ~/projects/badcode/bob && ./stack build && docker run --rm --entrypoint gh bob-runtime:dev --version` → prints a version.
- **Depends on:** —
- [ ] done
- Notes:

### T3: Deploy Bob and prove Workflows, gh and the token   [Status: pending | Model: opus]
- **Scope:** Commit T1+T2 in the Bob repo on `main`, push, and `./stack deploy` (Kai must approve
  a production deploy; check no turn is running first, as in the Bob README). Then, through the
  local `bob` MCP, `chat_create` a plain chat (engine `claude`) in project `badcode` asking it to:
  (a) list its tools and say whether `Workflow` is among them; (b) run `gh --version`, then prove the token's own scopes (the `.permissions` field on a repo shows the
  *user's* role, not the token's): push a throwaway branch `government/token-test`, `gh pr create
  --draft` on it, `gh label list`, then close the PR and delete the branch; (c) run a tiny two-agent Workflow that returns
  `"ok"`.
- **Files:** none in this repo (Bob repo commits only).
- **Acceptance criteria:** Workflow is present and the tiny workflow returns `ok`. `gh` works. The
  throwaway draft PR was created and closed, which proves Contents, Pull requests and Issues write
  (labels need Issues). If the token cannot, stop and log it: Kai must widen the fine-grained token
  (`GITHUB_TOKEN_BADCODE` in `.env.box`) to Pull requests read/write on `badcodetv/core` and redeploy.
  If Workflow is absent, log it; the plan continues on the fallback path (Decision 8).
- **TDD:** no
- **Validation:** `chat_read` on the test chat shows (a)–(c) answered as above; `ssh ubuntu@box.badcode.tv 'sudo docker ps --filter name=bob-project-badcode'` shows the new tag.
- **Depends on:** T1, T2
- [ ] done
- Notes:

### T4: Government folder, README and statement format   [Status: pending | Model: sonnet]
- **Scope:** Create `docs/government/README.md`: what the government is; the cabinet and the
  daily cycle (diagram from Architecture); the memory label scheme table; the daily PR rules; **how
  to review a government PR** (there is only ever one open: locally `gh pr list --label government`,
  `gh pr view <n>`, and ask Claude to read the day's `decision` memories with the `bob` MCP; or leave
  a review comment on the PR and the next cabinet run acts on it; in Bob: open a plain chat in
  `badcode` and ask it to review the PR); how to change a minister (edit its brief, merge, the
  Action syncs it); how to stop the cabinet (set `enabled: false` in `schedules.json`, merge); and
  that **a merged manifesto PR does not change badcode.tv until someone runs `./stack site deploy`**. Create `docs/government/statements/README.md`: one file per
  minister per day at `statements/YYYY-MM-DD/<post>.md` with front matter `platform: x|instagram|tiktok|youtube|any`,
  `status: draft`, `answers: <news memory ids>`, then the post text; how a posted statement is
  marked (`status: posted`, `url:`).
- **Files:** `docs/government/README.md`, `docs/government/statements/README.md`.
- **Acceptance criteria:** every label, post name, topic and schedule name matches this plan exactly.
- **TDD:** no
- **Validation:** `grep -c "exists <post>\|government/rolling" docs/government/README.md` ≥ 2; `git diff --check`.
- **Depends on:** —
- [ ] done
- Notes:

### T5: The shared government prompt (shared.md)   [Status: pending | Model: opus]
- **Scope:** Write `docs/government/shared.md`, the text the sync prepends to every government worker's prompt (Bob's project prompt is left alone, Decision 6). Cover:
  who BadCode is and the frame (`CLAUDE.md` "What BadCode is"); this is a UK cabinet reading world
  news (Decision 2); the voice in one tight paragraph distilled from `docs/voice.md`; the reader
  and their traps from `docs/marketing/the-reader.md` (never "you've been duped", name the
  decision-maker, proportionality on immigration); the AI-disclosure rules from `docs/using-ai.md`;
  Future Proof as the government's founding promise (`docs/stories/future-proof/`,
  `apps/site/src/content.json` `government`), never to be contradicted; the cabinet (post names);
  the full memory label scheme; that only the cabinet and Cabinet Secretary touch git, always on the
  one rolling PR, and nothing posts itself; factual discipline (every claim about the world needs a source URL in the news memory;
  no invented quotes; real people named only for public acts). It must not set a sound or a look
  (CLAUDE.md "There is no house style"). At most about 1,500 words.
- **Files:** `docs/government/shared.md`.
- **Acceptance criteria:** contains the label scheme verbatim from this plan; contains the ten post
  names; no genre/palette/voice-actor words; `python3 scripts/style-lint.py` reports nothing new.
- **TDD:** no
- **Validation:** `python3 scripts/style-lint.py`; `wc -w docs/government/shared.md` ≤ 1600.
- **Depends on:** T4
- [ ] done
- Notes:

### T6: News gatherer prompt and the news-sweep Workflow   [Status: pending | Model: opus]
- **Scope:** Load the `workflow-authoring` skill. Write `docs/government/workflows/news-sweep.js`
  per Interfaces (24 beats, 6-search cap per researcher, schema, merge phase, returns the list;
  aim for about 150 searches in all). Write `docs/government/workers/news-gatherer.md` (front matter:
  `claude`, `claude-opus-5-5`, effort `medium`, labels `role=staff`). It stays a separate session from the
  cabinet: research is a different job, and 24 researchers' raw output would crowd the cabinet's context. The
  procedure: `cd /project/work`, clone `https://github.com/badcodetv/core.git` if missing, else
  `git -C core pull --ff-only`; check `memory_search kind=news-digest,date=<today>` and stop if
  today is already done; run the Workflow with `scriptPath:
  /project/work/core/docs/government/workflows/news-sweep.js`; **fallback** if the Workflow tool is
  absent or errors: run the same 24 beats as ordinary subagents in batches of 8 with the same caps;
  before writing, search `kind=news,date=<today>` (limit 100) and skip any headline already stored (so a re-run after a crash never duplicates); write one `kind=news` memory per item with the exact labels; write the digest last. If fewer than
  5 items survive, write the digest saying so.
- **Files:** `docs/government/workflows/news-sweep.js`, `docs/government/workers/news-gatherer.md`.
- **Acceptance criteria:** `node --check` passes on the script; `meta` is a pure literal; the 24
  beats and the topic list match this plan; the prompt names both paths and the idempotency check.
- **TDD:** no
- **Validation:** `node --check docs/government/workflows/news-sweep.js`; `grep -A3 "export const meta" docs/government/workflows/news-sweep.js | grep -c '\${\|\.\.\.\|('` → 0 (meta is a pure literal); `grep -c "args.date" docs/government/workflows/news-sweep.js` ≥ 1. (Front-matter parsing is checked in T11.)
- **Depends on:** T5
- [ ] done
- Notes:

### T7: The ten minister briefs   [Status: pending | Model: opus]
- **Scope:** Write `docs/government/ministers/NN-<post>.md` for all ten posts (`00-prime-minister`,
  then `01-chancellor` … `09-energy-climate` in the order of Decision 1). These are **briefs, not
  workers**: plain markdown, no front matter, each ≤300 words, headed `### <Title> (<post>)`. Each
  says what the department owns, which topics and label keys it watches, its starting temperament
  (each one distinct: different rhythm, different instinct, so ten voices never blur into one), and
  one BadCode-flavoured instinct drawn from the canon (Work and Pensions and the Chancellor own
  automation and "we can't afford it"; the PM chairs and protects Future Proof). Briefs are
  deliberately thin; the Cabinet Secretary grows them.
- **Files:** the ten files above.
- **Acceptance criteria:** ten files; each heading names its post key exactly; no front matter; no
  procedure text (procedure lives in `workers/cabinet.md`).
- **TDD:** no
- **Validation:** `ls docs/government/ministers/*.md | wc -l` → 10; `for p in prime-minister chancellor foreign home education defence health work-pensions housing energy-climate; do grep -q "($p)" docs/government/ministers/*-$p.md || echo MISSING $p; done` prints nothing; `git diff --check`.
- **Depends on:** T5
- [ ] done
- Notes:

### T8: The cabinet worker   [Status: pending | Model: opus]
- **Scope:** Write `docs/government/workers/cabinet.md` (front matter `claude`, `claude-opus-5-5`,
  effort `high`, labels `role=cabinet`, `include: ministers`). The cabinet is **one session that
  chairs as Prime Minister and speaks as each minister in turn**, using the briefs the sync appends
  to its prompt. Procedure, in order:
  1. Check today's digest exists (`kind=news-digest,date=<today>`); if not, `request_human_attention({message, notice: true})` and stop.
  2. Its own worktree, per the rolling-PR rules: on the open rolling branch if there is one, else a new one from `origin/main`.
  3. If there is no open rolling PR, run the feedback step on the most recently merged or closed one.
  4. If there is an open one, read every review comment since its last entry; act on each (change the files, or reply on the PR saying why not) before anything else.
  5. Read today's digest and news (`memory_search` then `memory_get`).
  6. Sit the cabinet: for each of the ten posts, read that post's news (`kind=news,date=<today>,exists <post>`) and the post's last 10 `decision` memories, then decide `none`, `manifesto`, `statement` or `both` **in that minister's voice from its brief**. It may hand a heavy draft to a subagent with the minister's brief and news, but it settles every decision itself.
  7. As PM, settle clashes (one government, one line; Future Proof wins) and rewrite `00-prime-minister.md` if the day warrants it.
  8. Write the files; commit; push; open or update the rolling PR (body rewritten: summary on top, dated changelog below).
  9. Write one `kind=decision` memory per minister that acted, and one `kind=minutes`.
  10. End with `request_human_attention({message: "<PR URL>\n<three-line summary>"})` (its only arguments are `message` and `notice`, `bob/api/cmd/bob/tools_attention.go`), or `notice: true` on a day with no changes.
  The cabinet never edits `workers/`, `ministers/`, `shared.md` or `schedules.json`.
- **Files:** `docs/government/workers/cabinet.md`.
- **Acceptance criteria:** it holds the rolling-branch name, the `government` label, the
  one-open-PR rule, the review-comment step, the feedback dedupe rule and the file allow-list.
- **TDD:** no
- **Validation:** `grep -c "government/rolling\|--label government\|request_human_attention\|exists <post>" docs/government/workers/cabinet.md` ≥ 4.
- **Depends on:** T5, T7
- [ ] done
- Notes:

### T9: The Cabinet Secretary worker   [Status: pending | Model: opus]
- **Scope:** Write `docs/government/workers/cabinet-secretary.md` (front matter `claude`,
  `claude-opus-5-5`, effort `high`, labels `role=staff`). It is deliberately a **separate** session
  from the cabinet: an editor judging the author, not the author marking its own work. Weekly
  procedure: its own worktree on the rolling branch (create the rolling PR if none is open, per the
  rules); for each of the ten posts, read the week's `decision`, `feedback` and `minutes` memories
  and the merged manifesto diffs (`git log --since=7.days -p -- docs/government/manifesto/`); decide
  whether the brief should change (positions that stuck, tone notes from review comments, lines that
  were cut, two ministers starting to sound alike); edit only `docs/government/ministers/*.md`;
  commit **onto the rolling PR** and add a "Personnel" entry to its body with evidence memory ids;
  write one `kind=personnel` memory per changed minister. If nothing warrants change, it makes no
  commit and writes a single `kind=personnel` memory with `minister=none`. No attention request:
  the cabinet's next run raises it.
- **Files:** `docs/government/workers/cabinet-secretary.md`.
- **Acceptance criteria:** names the edit boundary (`ministers/` only), the rolling branch and the
  memory kinds; it never opens a second PR.
- **TDD:** no
- **Validation:** `grep -c "government/rolling\|kind=personnel" docs/government/workers/cabinet-secretary.md` ≥ 2.
- **Depends on:** T5, T7
- [ ] done
- Notes:

### T10: Schedules and manifesto seeds   [Status: pending | Model: sonnet]
- **Scope:** Write `docs/government/schedules.json` with the 3 schedules in Interfaces, all
  `enabled: false`, `timezone: Europe/London`, `keep_sessions: 14` (`gov-3-personnel`: 8). Write
  the ten manifesto seeds in `docs/government/manifesto/`, with the same `NN-<post>.md` names as the
  briefs. `00-prime-minister.md` restates the Future Proof promise and the three pledges from
  `apps/site/src/content.json` `government.pledges`. Each minister file has front matter
  `title: <Department>` and `line: <one sentence>`, then a `## Position` heading with one placeholder
  sentence in BadCode's voice saying the minister has just been sworn in and is reading the news.
  That placeholder is deliberate seed copy, replaced by the first PR.
- **Files:** `docs/government/schedules.json`, `docs/government/manifesto/00-…09-*.md`.
- **Acceptance criteria:** `schedules.json` is valid JSON with 3 entries whose `worker` names match
  files in `workers/`; each manifesto file has `title` and `line`.
- **TDD:** no
- **Validation:** `node -e "const s=require('./docs/government/schedules.json');const fs=require('fs');console.log(s.length, s.every(x=>fs.existsSync('docs/government/workers/'+x.worker+'.md')&&x.enabled===false))"` → `3 true`.
- **Depends on:** T4, T6, T8, T9
- [ ] done
- Notes:

### T11: sync-bob.mjs   [Status: pending | Model: sonnet]
- **Scope:** Implement `scripts/government/sync-bob.mjs` per Interfaces (Node 22, no
  dependencies, ESM). Desired state = `shared.md` + every `workers/*.md` (worker name = file
  basename; `include: ministers` appends the briefs, see Interfaces) + `schedules.json`. Current
  state = `worker_list`, `schedule_list`. Compare prompt text, engine, model, effort, labels and tools for workers, and
  every field for schedules. Print one line per item. With `--apply`, write the changes.
  `worker_update` always sends all fields. Exit non-zero on any MCP error, after printing it.
- **Files:** `scripts/government/sync-bob.mjs`, `scripts/government/sync-bob.test.mjs`.
- **Acceptance criteria:** tests cover `parseWorkerFile` (good file; unknown key rejected; missing
  engine rejected; labels parsed; `include` parsed), `assemblePrompt` (shared + body; with
  `include: ministers`, the briefs appended in file order under `## The ministers`), `planSync`
  (create / update on prompt change / update when only a minister brief changed / update on a
  `shared.md` change / update on label change / unchanged / extra-in-Bob reported, never deleted;
  worker update body includes every field; absent tools equals `[]`), `parseMcpReply` (good result;
  top-level `error` throws; `isError` throws). A dry run against live Bob
  prints a plan and writes nothing.
- **TDD:** yes
- **Validation:** `npx vitest run scripts/government` → all pass; `BOB_MCP_KEY=$(grep '^BOB_MCP_KEY_BADCODE=' ~/projects/badcode/bob/.env.box | cut -d= -f2) node scripts/government/sync-bob.mjs` → lists 3 workers `create` and 3 schedules `create`; exit 0.
- **Depends on:** T10
- [ ] done
- Notes:

### T12: GitHub Action for the sync   [Status: pending | Model: sonnet]
- **Scope:** `.github/workflows/bob-sync.yml`: on `push` to `main` with `paths:
  docs/government/workers/**, docs/government/ministers/**, docs/government/shared.md,
  docs/government/schedules.json, scripts/government/sync-bob.mjs`, and `workflow_dispatch`. `concurrency: bob-sync`. Steps:
  checkout (fetch-depth 1), setup-node 22, `node scripts/government/sync-bob.mjs --apply` with
  `BOB_MCP_KEY: ${{ secrets.BOB_MCP_KEY_BADCODE }}`. Kai sets the secret once:
  `gh secret set BOB_MCP_KEY_BADCODE --repo badcodetv/core` (paste the key from
  `~/projects/badcode/bob/.env.box`). Write that step into `docs/government/README.md`.
- **Files:** `.github/workflows/bob-sync.yml`, `docs/government/README.md`.
- **Acceptance criteria:** the workflow file is valid; the README has the one-time secret step.
- **TDD:** no
- **Validation:** `npx --yes @action-validator/cli .github/workflows/bob-sync.yml` (or `gh workflow view bob-sync.yml` after push) → no errors.
- **Depends on:** T11
- [ ] done
- Notes:

### T13: Manifesto on the site   [Status: pending | Model: sonnet]
- **Scope:** In `apps/site/build.mjs`, read `docs/government/manifesto/*.md` (sorted), parse
  front matter (`title`, `line`) and body, and put them on `C.government.manifesto` before the page
  is built (the content object is embedded into the page the same way as now). Plain-text body for
  `/government` lists each title and line. Add `/text/401`–`/text/411` to the pages list
  (`build.mjs:55`). In `apps/site/src/tv.js`: GOVT 1 (`tv.js:118`) keeps the promise heading, then
  lists each minister's title and line; teletext 400 (`tv.js:149`) keeps the pledges and adds one
  compact line pointing to 401 (a teletext page is a fixed 40×24 box with `white-space: pre`, and 400
  already uses about 20 rows); 401 is the cabinet index (ten dotted lines: index
  on 401, ministers on 402–411); each minister page shows title, line and at most 14 wrapped body
  lines, then "MORE: badcode.tv/government"; add them to the page order (`tv.js:216`). Update `apps/site/README.md`.
- **Files:** `apps/site/build.mjs`, `apps/site/src/tv.js`, `apps/site/README.md`.
- **Acceptance criteria:** the build succeeds; `dist/government/index.html` contains every minister
  title; `dist/text/405/index.html` exists; no teletext page renders more than 24 rows. Markdown body is rendered as escaped text paragraphs
  (no raw HTML injection).
- **TDD:** no
- **Validation:** `node apps/site/build.mjs && grep -c "Chancellor\|Housing" apps/site/dist/government/index.html` ≥ 2 && `test -f apps/site/dist/text/405/index.html`; `./stack site preview` and check GOVT 1 and teletext 401 by eye.
- **Depends on:** T10
- [ ] done
- Notes:

### T14: Repo pointers   [Status: pending | Model: sonnet]
- **Scope:** Add a `docs/government/` row to the repo map in `CLAUDE.md` ("the BadCode government:
  one cabinet agent playing ten ministers in Bob project `badcode`; git is the source of truth;
  one rolling PR → its README") and one line in `docs/README.md`'s index.
- **Files:** `CLAUDE.md`, `docs/README.md`.
- **Acceptance criteria:** both link to `docs/government/README.md`; no genre/palette words added.
- **TDD:** no
- **Validation:** `python3 scripts/style-lint.py`; `git diff --check`.
- **Depends on:** T4
- [ ] done
- Notes:

### T15: First sync into Bob   [Status: pending | Model: sonnet]
- **Scope:** **First** Kai sets the GitHub secret (T12), so the merge's Action run does not fail.
  Create the PR label: `gh label create government --repo badcodetv/core`. Then merge T4–T14 to
  `main` (Kai reviews); the merge triggers the sync (or run `gh workflow run bob-sync.yml`).
  Confirm in Bob that the 3 workers and 3 disabled schedules exist (the project prompt is untouched).
- **Files:** none.
- **Acceptance criteria:** the Action run is green; `worker_list` shows `news-gatherer`, `cabinet`,
  `cabinet-secretary`; `schedule_list` shows 3 schedules, all disabled; every worker's prompt starts
  with `shared.md`; the cabinet's prompt ends with the ten minister briefs.
- **TDD:** no
- **Validation:** `gh run list --workflow bob-sync.yml --limit 1` → `completed success`; a second
  dry run of `sync-bob.mjs` prints everything `unchanged`.
- **Depends on:** T3, T12, T13, T14
- [ ] done
- Notes:

### T16: End-to-end: a dry run over two days, then switch on   [Status: pending | Model: opus]
- **Scope:** Day 1, by hand, with the local `bob` MCP `chat_create` (worker name, message as in
  `schedules.json`; long turns answer `running`, so poll `chat_read`): the gatherer, then the
  cabinet. Check: news memories carry the exact labels and source URLs, there is one digest, the
  cabinet opened the rolling PR on core touching only manifesto and statement files, `decision`
  and `minutes` memories exist, and Bob shows the Needs-you dot. Kai leaves **one review comment** on
  the PR and does **not** merge. Day 2 (or a re-run with a later `date`): gatherer, then cabinet
  again. Check it pushed to the **same** PR (no second PR), rewrote the PR body with a day-2 entry,
  and answered the review comment. Run the Cabinet Secretary once by hand and check its commit
  lands on the same rolling PR and the `## The ministers` text in Bob changes only after merge.
  Kai merges (proving the local review path in `docs/government/README.md`). Run the cabinet once
  more and check it starts a fresh rolling PR and writes `kind=feedback` from the merged one.
  Finally, set every schedule's `enabled: true` in `schedules.json` through a PR. The merge syncs it.
- **Files:** `docs/government/schedules.json` (enabled flags only).
- **Acceptance criteria:** every check above holds; at most one open `government` PR at any time;
  the sweep stayed within about 150 web searches (count the researchers' tool calls in
  `chat_read`); after the enabling merge, `schedule_list` shows all 3 enabled; the next 05:00 run
  completes unattended and the rolling PR has a new entry by about 08:00.
- **TDD:** no
- **Validation:** `memory_search label_selector="kind=news,date=<d>"` ≥ 5 hits with all labels;
  `gh pr list --repo badcodetv/core --label government --state open` → exactly 1; `npm test` and
  `node apps/site/build.mjs` still pass.
- **Depends on:** T15
- [ ] done
- Notes:

## Discovered Issues Log

(appended by executors during implementation)

- T11/T12 (executor): Bob schedule rows carry `worker` (name) and no `why`; only worker_create/update take `why`. schedule_update keeps omitted fields, so the sync sends all six anyway. Bare `worker_list` rows omit tools/prompt, so sync fetches each worker by name. `sync-bob.mjs` has an extra `--root <dir>` option (fixtures/tests) and validates that each schedule names a known worker. Tests were written in the same pass as the code, not strictly red-first. README one-time secret step (T12) is not written: docs/government/README.md belongs to another agent.

- **T6 (2026-11-05):** `node --check` is not a real syntax gate for Workflow scripts on Node 22.14:
  a file with `export` and a deliberate syntax error (`const x = (`) also exits 0, because Node's
  module-type detection short-circuits the check. A stronger check that does catch errors: strip
  `export ` from `export const meta` and compile the file as an async function body
  (`new (Object.getPrototypeOf(async function(){}).constructor)('args','agent','parallel','pipeline','phase','log','budget', src)`);
  `news-sweep.js` passes it and was also run end-to-end with stubbed `agent`/`parallel`
  (24 beats, failed beats, null merge → code fallback, `tech-ai` post rule, weight-3 downgrade,
  missing `args.date` throws). T11/T16 may want that as the gate.
- **T6 (2026-11-05):** deviation from the T6 scope text: the gatherer does **not** run
  `git -C core pull --ff-only`. `/project/work/core` is shared with other chats and may be on any
  branch or dirty, so it does `git -C core fetch origin main` and copies the script out with
  `git show origin/main:docs/government/workflows/news-sweep.js > /project/work/.gov-news/news-sweep-<today>.js`,
  then passes that path as `scriptPath`. The checkout's working tree is never touched.
- **T6 (2026-11-05):** T5's `shared.md` did not exist yet when T6 was written in this worktree;
  `news-gatherer.md` therefore restates the topics, posts and news-memory labels it needs rather
  than pointing at `shared.md`. If T5 lands with different wording, keep the two consistent.
- **T6 (2026-11-05):** the script's own clean-up (plain JS, after the merge agent) enforces the
  contract even if a model slips: unknown topics/posts and source-less items are dropped,
  `tech-ai` always gains `work-pensions` + `chancellor`, weight 3 with one source becomes 2. The
  merge agent also runs on `model: 'sonnet'` (the plan only fixed the researchers' model).

- **T8 (cabinet), feedback step runs every day, not only when no PR is open.** If the Cabinet
  Secretary opens a fresh rolling PR on Sunday night after a merge, a "only when none is open" rule
  would skip that merge's feedback forever. The step is idempotent through the `pr`+`minister`
  dedupe; a PR that touched no minister's files gets one `kind=feedback,minister=none` memory so it
  isn't re-read daily (same `minister=none` convention as `kind=personnel`).
- **T8, telling the cabinet's own PR comments apart.** Replies post under the `GITHUB_TOKEN` owner's
  account (likely Kai's), so author can't distinguish them. Cabinet replies start `Cabinet:` and
  the PR body's first line carries `<!-- government-rolling last-entry=<ISO> -->` to bound "comments
  since its last entry". Documented in the README.
- **T8, stale rolling branch.** Before deleting a leftover `government/rolling` with no open PR, the
  cabinet (and Secretary) compare its head with the last finished PR's `headRefOid`; if they differ
  (a run pushed then failed before `gh pr create`), it keeps the branch and opens the PR for it.
- **T10, manifesto `line:` values avoid `: `** (a colon-space breaks YAML-style parsing); the cabinet
  prompt tells it to keep the line colon-free. T13's parser should still split on the first colon only.
- **CLAUDE.md "Out of scope here" and docs/voice.md ("Agent / character voices") still say the
  BadCode government is built in a separate project.** That now contradicts `docs/government/`.
  Not changed (outside T14's scope); a one-line fix for whoever merges.
- **`docs/stories/future-proof/` is not on `main`** (it is untracked in the main checkout), so the
  prompts cite the committed canon `docs/stories/gitpush-origin-master/future-proof.md` instead.
