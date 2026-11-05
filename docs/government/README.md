# The BadCode Government

A cabinet of AI ministers that reads the news every morning, forms positions in BadCode's voice,
and grows over time. It is the government the UK would have if BadCode ran it, sent back from the
future. It has two public outputs:

1. **The manifesto** — one file per minister in [`manifesto/`](./manifesto/), always moving. The
   website's GOVT channel shows it, under the Future Proof promise.
2. **Statements** — short draft posts in [`statements/`](./statements/README.md). Nothing posts
   itself: Kai or Jack post them, or hand them to the marketing `chief-of-staff` skill.

It runs in **Bob** (`https://bob.box.badcode.tv`), project `badcode`. **Git is the source of truth**
for the whole government: every worker, every minister's brief and every schedule lives in this
folder, and a GitHub Action copies them into Bob on every merge. Nobody edits a prompt in Bob by
hand. Design and reasoning: [`design/2026-11-05-badcode-government.md`](../../design/2026-11-05-badcode-government.md).

**Nothing an agent writes reaches `main` without Kai or Jack merging it.** And a merged manifesto
change does **not** change badcode.tv until someone runs `./stack site deploy`.

## The cabinet

Ten posts. The post key is the file name, the memory label key and the `minister=` value.

| # | Post | Key |
| --- | --- | --- |
| 00 | Prime Minister (chairs) | `prime-minister` |
| 01 | Chancellor of the Exchequer | `chancellor` |
| 02 | Foreign Secretary | `foreign` |
| 03 | Home Secretary | `home` |
| 04 | Education | `education` |
| 05 | Defence | `defence` |
| 06 | Health | `health` |
| 07 | Work and Pensions | `work-pensions` |
| 08 | Housing | `housing` |
| 09 | Energy and Climate | `energy-climate` |

There is no Science/Technology post: AI and automation news goes to Work and Pensions and the
Chancellor.

**The cabinet is one agent, not ten.** One Opus session chairs as Prime Minister and speaks as each
minister in turn, from that minister's brief in [`ministers/`](./ministers/). The sync appends the
ten briefs to the cabinet's prompt under `## The ministers`, so a brief is the minister's whole
persona: change the brief, and the minister changes.

## The daily cycle

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

| Schedule | Worker | When | What it does |
| --- | --- | --- | --- |
| `gov-1-news` | `news-gatherer` | daily 05:00 | Runs the [`news-sweep`](./workflows/news-sweep.js) Workflow: 24 Sonnet researchers, one per beat, at most 6 web searches each, UK first and the world for its effect on the UK. Dedupes, then writes one `kind=news` memory per story and one `kind=news-digest`. Falls back to ordinary subagents in batches of 8 if the Workflow tool is missing. Skips the day if the digest already exists. |
| `gov-2-cabinet` | `cabinet` | daily 06:00 | Reads review comments on the open PR and acts on them first, then sits the cabinet over today's news and commits onto the rolling PR. Stops (with a notice) if today's digest is missing. |
| `gov-3-personnel` | `cabinet-secretary` | Sundays 20:00 | Reads the week's decisions, feedback and merges, and edits the minister briefs on the same rolling PR. A separate session on purpose: the editor does not mark its own work. |

Scheduled runs in one Bob project never overlap; they queue and run one at a time, so the cabinet
always waits for the gatherer. The names are numbered because after an outage Bob catches up
missed firings in schedule-name order. The gatherer and the Cabinet Secretary are separate
sessions from the cabinet: 24 researchers' raw output would crowd the cabinet's context, and an
editor should not judge its own work.

The workers are [`workers/news-gatherer.md`](./workers/news-gatherer.md),
[`workers/cabinet.md`](./workers/cabinet.md) and
[`workers/cabinet-secretary.md`](./workers/cabinet-secretary.md). Each one's live prompt in Bob is
[`shared.md`](./shared.md), a blank line, then the worker file's body (plus the briefs, for the
cabinet).

## The memory label scheme

Every worker reads and writes Bob memory with exactly these labels.

| Memory | Written by | Labels | Content |
| --- | --- | --- | --- |
| news item | gatherer | `kind=news`, `date=YYYY-MM-DD`, `topic=<topic>`, `region=uk\|world`, `weight=1\|2\|3`, and one key per post it concerns with value `y` (e.g. `health=y`) | headline; 3–5 sentence summary; why it matters to the UK; source URLs (at least one; two for weight 3) |
| digest | gatherer | `kind=news-digest`, `name=news-digest`, `date` | the day in ≤20 lines, each with its news memory id |
| decision | cabinet | `kind=decision`, `minister=<post>`, `date`, `action=manifesto\|statement\|both`, `pr=<number>` | what that minister decided and why, in its voice; the news ids it answers (only for ministers that acted) |
| minutes | cabinet | `kind=minutes`, `date`, `pr=<number>` (omit when no PR) | the meeting: who acted, who passed, clashes the PM settled, review comments answered, failures |
| feedback | cabinet | `kind=feedback`, `minister=<post>`, `pr=<number>`, `outcome=merged\|edited\|closed` | Kai's/Jack's review comments touching that minister; what changed between the PR and what was merged |
| personnel | Cabinet Secretary | `kind=personnel`, `minister=<post>`, `pr=<number>` | what changed in the brief and why, with evidence ids |

**Posts:** `prime-minister`, `chancellor`, `foreign`, `home`, `education`, `defence`, `health`,
`work-pensions`, `housing`, `energy-climate`.
**Topics:** `economy`, `work`, `welfare`, `housing`, `health`, `education`, `crime-justice`,
`migration`, `foreign`, `defence`, `energy-climate`, `tech-ai`.

The cabinet's read for each post is `label_selector: "kind=news,date=<today>,exists <post>"` with
`limit: 100`; a post's history is the newest 10 of `kind=decision,minister=<post>` and of
`kind=feedback,minister=<post>`. Search returns 500-character snippets, so readers call
`memory_get` on each id they need in full.

## The rolling PR

There is only ever **one** open government PR. You never have to look at more than one.

- Branch `government/rolling`, label `government`, title `Government: since YYYY-MM-DD` (the date
  of its first entry). The cabinet commits to it every morning; the Cabinet Secretary commits to it
  on Sundays. If nobody looks for a week, you find one PR holding a week of changes.
- **Each run rewrites the PR body**: a short summary of the whole PR on top, then a dated changelog,
  newest first, one entry per run, saying what each minister changed (or "nothing today") and which
  news memories it answers.
- Ministers read their current text **from the rolling branch**, so each day builds on the unmerged
  text and on any fixes you pushed to the branch yourself.
- **Your review comments steer it.** Every cabinet run first reads the comments added since its last
  entry and acts on each: it changes the files, or replies on the PR saying why not. Its replies
  start with `Cabinet:` (they post under the GitHub token's account, so that prefix is how you tell
  them apart).
- **Merging or closing ends it.** The next run reads the finished PR, writes `kind=feedback`
  memories per minister (what you changed, what you said), and starts a fresh `government/rolling`
  from `main`. **Closed means rejected**: the cabinet will not re-propose the same text unchanged.
- The cabinet only touches `docs/government/manifesto/*.md` and
  `docs/government/statements/<date>/*.md`; the Cabinet Secretary only touches
  `docs/government/ministers/*.md`. Neither ever edits `workers/`, `shared.md` or `schedules.json`:
  those change only by a human PR.
- Commits are authored `BadCode Government <government@badcode.tv>`.
- Cadence is daily for now; changing it is one line in [`schedules.json`](./schedules.json).

## How to review a government PR

You'll see a dot in Bob when the cabinet has finished: its message holds the PR link and a
three-line summary.

**Here, in Claude Code:**

```bash
gh pr list --label government          # there is only ever one open
gh pr view <n>                          # summary + changelog
gh pr diff <n>                          # the actual text
```

Then ask Claude to read the day's `decision` and `minutes` memories with the `bob` MCP
(`memory_search` with `kind=decision,date=<today>`, then `memory_get`) if you want the ministers'
reasoning. Then either:

- **merge it** (`gh pr merge <n> --squash`), which publishes the text to `main`; or
- **leave review comments** (inline on a line, or on the PR) and don't merge: the next cabinet run
  acts on every comment before anything else; or
- **push a fix yourself** to `government/rolling`: the cabinet builds on your text from then on; or
- **close it**: the cabinet reads that as rejection, writes it down, and starts again from `main`.

**In Bob:** open a plain chat in project `badcode` and ask it to review the open government PR
(`gh pr list --repo badcodetv/core --label government`), read the decisions, and leave comments or
merge on your say-so.

**Statements** in the PR are drafts. Post the ones you like by hand (or hand them to
`chief-of-staff`), then mark them `status: posted` with the `url:` (see
[`statements/README.md`](./statements/README.md)).

**Then deploy the site**, if the manifesto changed and you want badcode.tv to show it:
`./stack site deploy`. Merging alone does not change the live site.

## How to change a minister

Edit its brief in [`ministers/`](./ministers/) (`NN-<post>.md`, plain markdown, no front matter,
headed `### <Title> (<post>)`), open a PR, merge. The Action syncs it and the next cabinet run
speaks with the new brief. The Cabinet Secretary also proposes brief changes every Sunday, on the
rolling PR, with the evidence for each; merging that PR is what makes them live.

To change how the cabinet works (its procedure, not a persona), edit
[`workers/cabinet.md`](./workers/cabinet.md); for every worker at once, [`shared.md`](./shared.md).

## How to stop it

Set `"enabled": false` on the schedules in [`schedules.json`](./schedules.json) and merge. The
sync turns them off in Bob. Nothing is deleted: memories, the PR and the workers all stay.

## The sync (git to Bob)

[`scripts/government/sync-bob.mjs`](../../scripts/government/sync-bob.mjs) makes Bob match this
folder. The GitHub Action `.github/workflows/bob-sync.yml` runs it with `--apply` on every push to
`main` that touches `workers/`, `ministers/`, `shared.md`, `schedules.json` or the script itself
(and on demand: `gh workflow run bob-sync.yml`).

- Desired state: `shared.md` + each `workers/<name>.md` (the worker's name is the file name; a
  worker with `include: ministers` gets every brief appended under `## The ministers`) +
  `schedules.json`.
- It writes only what changed, records `git <short sha>: <subject>` as the reason on every worker
  version, and **never deletes**: anything in Bob that isn't in git is printed as
  `extra (not touched)`.
- It never touches Bob's project prompt: `badcode` is one project for all of BadCode, and its
  project prompt reaches every chat.
- Dry run locally (prints the plan, writes nothing):

  ```bash
  BOB_MCP_KEY=$(grep '^BOB_MCP_KEY_BADCODE=' ~/projects/badcode/bob/.env.box | cut -d= -f2) \
    node scripts/government/sync-bob.mjs
  ```

**One-time setup (Kai):** give the Action the Bob key, or every merge's sync fails:

```bash
gh secret set BOB_MCP_KEY_BADCODE --repo badcodetv/core
# paste the BOB_MCP_KEY_BADCODE value from ~/projects/badcode/bob/.env.box
```

and create the PR label once: `gh label create government --repo badcodetv/core`.

## Files

```
docs/government/
  README.md               this file
  shared.md               prepended to every government worker's prompt
  schedules.json          the three schedules (enabled flags live here)
  workers/                one file per Bob worker: front matter + system prompt
  ministers/NN-<post>.md  the ten briefs, appended to the cabinet's prompt
  workflows/news-sweep.js the gatherer's Workflow script
  manifesto/NN-<post>.md  the manifesto, one file per minister (what the site shows)
  statements/<date>/      draft statements, one file per minister per day
```
