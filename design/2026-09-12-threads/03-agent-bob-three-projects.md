# Thread 03 — Agent Bob: the first three real projects

You are in `~/projects/badcode/agent-bob`. Read `CLAUDE.md`, `docs/product/17-product-spec.md` (§8.8 is
the BadCode marketing manager, the first real use case), `docs/product/10-topology-library.md`,
`docs/product/12-composition-playbook.md`, `docs/product/19-scenario-library.md` and
`docs/18-workers-memory-events.md`. For the story side read, in the BadCode repo
(`~/projects/badcode/badcode`): `docs/marketing/README.md` and `docs/marketing/the-reader.md` (who the
work is for — binding on anything the marketing manager posts), `docs/coins/emperors-new-coin.md` (the
claim ledger for the coin — every sentence about the coin is checked against it) and
`design/2026-08-12-enc-architecture-decision.md`. The coin's own repo is `~/projects/enc/coin`.

## Goal

Define, then run, the initial workflow for three projects on Agent Bob:

1. **Emperor's New Coin** — Kai is building this with Richard. The working knowledge is in their WhatsApp
   thread, which Kai will paste or summarise. Until that arrives, draft the project from the repo's
   design docs and mark every assumption.
2. **The BadCode government** — the per-story agents. Note `docs/product/17-product-spec.md` line 33: it
   was previously scoped as a *separate* project. Kai now wants it running on Bob. Confirm the scope on the
   first reply: which stories, which roles.
3. **The BadCode marketing manager** — spec §8.8; the BadCode repo's `docs/marketing/` is its source of
   truth, and its stage-1 rule is human-approved posts only (`request_human_attention` before anything
   public).

## What Kai actually wants to see (this is the product requirement)

At the start of a project the user has a conversation with the architect to set a goal; the architect
then coordinates a team; real events happen; the team turns out to be not quite right. The user wants to
**see the architect's decisions far sooner than normal, see its reaction to each event, and adjust the
team.** So for each project define:

- the goal statement and charter (the architect interview's inputs);
- the expected first team (workers, prompts, tools, wiring) as a *prediction* we will compare against
  what the architect actually proposes;
- three to five **real events** we expect in week one, and what a correct architect reaction looks like;
- what the operator needs on screen to judge those reactions quickly (this feeds the console; file gaps
  as tickets, don't build them here);
- the token budget for the project (operator-only, low default — Kai's 2026-09-11 rule).

Deliverable: `design/2026-09-12-first-three-projects.md` with one section per project in that shape,
plus a ticket list. Then, once thread 02 reports Bob stable, bootstrap each project on the local stack
(`mock` first) and run its interview; record the architect's actual decisions next to the prediction.

## A WhatsApp channel for Bob — Kai's WhatsApp only, reusing Platinum's session

**Kai's ruling, 2026-09-12: reuse the Platinum WAHA session as-is.** The BayesPrice tech group has three
members and receives the automated "cache cleared" messages, so the linked device is Kai's own WhatsApp
account. Kai is happy for that one session to serve both Platinum and Bob. No second number.

What exists, in `~/projects/bayesprice/Platinum`: the `waha` service in `docker-compose.yml` (image
`devlikeapro/waha`, engine NOWEB, session `default`, production profile only, auth persisted in the
external Docker volume `waha-data`), called by `goapi/pkg/chatops/client.go` with `POST /api/sendText`
and header `X-Api-Key` (the key is `SYSTEM_SECRET` in Platinum's env — read it on the host where it
runs; never paste it into a chat, a commit or a file in this repo). Be precise about what "the token"
is: **two things**. The API key is only a password for the container. What makes it Kai's WhatsApp is
the *linked session* in the `waha-data` volume on Platinum's production host, and that cannot be copied
around. Bob must **call that container where it runs** (over Tailscale once thread 01 exists; over an SSH
tunnel for the test). WAHA's free tier receives as well as sends: a webhook on the `message` event and
`GET /api/{session}/chats/{chatId}/messages`, both supported on NOWEB.

### Ticket W0 — prove it (first, before any design)

1. Find Platinum's production host and the WAHA container. Platinum's `ops.md` and
   `docs/preview-environments.md` describe the compose profiles; the container is named
   `platinum-production-waha`. Open a tunnel to its port 3000. Confirm `GET /api/sessions` shows
   `default` as `WORKING`, and `GET /api/sessions/default/me` returns Kai's number — that line settles
   whose account it is.
2. **Send a message to Kai from Kai.** `POST /api/sendText` with `chatId` = Kai's own number in WAHA's
   form (`<countrycode><number>@c.us`) and text `Bob WhatsApp test <timestamp>`. Show the command and
   wait for Kai's yes; Kai confirms it arrived on the phone.
3. **Read the Richard thread.** `GET /api/default/chats` to find Richard's chat id, then
   `GET /api/default/chats/<id>/messages?limit=50`. Report only the count, the date range, and the first
   line of the three most recent messages. Store nothing yet.
4. Write into this ticket's Notes: whether read works on the free tier as the docs claim, the chat id
   format, any rate limit or engine quirk, and the exact commands. If read fails on NOWEB, try the
   WEBJS engine on a *second* WAHA container with its own volume before concluding — do not change
   Platinum's container, it serves BayesPrice alerts.

Only after W0 passes: design the connector as **"Kai's WhatsApp"**, a single-tenant channel, explicitly
not a general anyone-can-connect mechanism. A webhook from WAHA into Bob's event spine
(`docs/product/04-events-and-schedules.md`) turns messages from an allowlisted set of chats (the Richard
thread first) into events and memory; Bob replies only through `request_human_attention`-style drafts
until Kai says otherwise. State the trust boundary in the ticket: the session reads *every* chat on Kai's
phone, so the allowlist is enforced in our code; the WAHA URL and key live only in Bob's env on the box;
and a shared session means a Platinum outage or a WhatsApp re-link affects Bob too.

### Agent ENC — a storage repository, not an application (Kai's ruling, 2026-09-12)

The coin project gets its own repository, **`agent-enc`**, beside `agent-bob` and `agent-wolf`. It is
**not** like Agent Wolf: no UI, no login, no API. It is the **persistent storage layer** of the ENC
project on Bob — the place Bob's workers read configuration from and write configuration to, and the
place the project's documents accumulate. Humans manage the project through **Bob's own console** (log
in, talk to the architect and the workers, use the connectors); the repository is what they and the
workers share.

Bob already has the mechanism: **the git projection** (`docs/21-git-projection.md`). Point a project at a
repository and subfolder; the database stays the only place writes are ordered, and git is two doors —
*render* out (every prompt, worker, schedule, grant and named document as files) and *import* in (a
human edits a file or merges a pull request, Bob folds it). "Project as code" (§7) bootstraps a whole
project from the folder. Two consequences to state in the design, not discover later: **the memory log
is not in the repo** (only named documents are; a bootstrapped project arrives with no past), and the
DB, not the repo, is the source of truth. So `agent-enc` is the project's *rendered current state and
document store*, and that is exactly what Kai asked for.

Also relevant and **unmerged**: the project-connections work on branch `feat/project-connections`
(checkout `~/projects/badcode/agent-bob-connections`, 32 commits ahead of `main`; T1–T11 and T13 done,
T12 wire `/connect/` into agentd, T14 the operator guide and T15 end-to-end still pending). Connections
are how a worker gets a grant to an external service, and T11 already renders grants into the git
projection. The WhatsApp channel should be a *connection* in that sense, not a one-off. Coordinate with
thread 02 before merging it; do not merge it yourself.

### The three stages, in order

**Stage 1 — stand the project up with WhatsApp connected.**
- Create `~/projects/badcode/agent-enc` (git init, `README.md` saying what it is and is not, the
  subfolder layout the git projection expects, a licence matching the others).
- Create the `enc` project on the local Bob stack (`mock` first), point its git projection at the repo,
  render once, and confirm the files appear.
- Add the WhatsApp connection: WAHA's webhook on the `message` event → Bob's event spine, filtered by an
  allowlist of chat ids held in the project's configuration (so it renders into `agent-enc` and is
  reviewable), plus a read tool over `GET /api/default/chats/<id>/messages` for history. Sending stays
  behind `request_human_attention`.
- Done when: a message Kai sends in an allowlisted chat appears as an event in the `enc` project and the
  connection's configuration is visible as a file in `agent-enc`.

**Stage 2 — ingest the Richard thread through the channel.**
- No static export. The channel is the ingestion: add Richard's chat id to the allowlist, run the history
  read over the whole thread (paged), and land it as **named documents** in the project (so it renders
  into `agent-enc` and survives a bootstrap) — one document per month, or per topic if the thread is
  short, each with dates and the two speakers named. Kai says yes before the pull.
- Done when: the thread is readable in `agent-enc` and Kai has skimmed it for anything that must not be
  there.

**Stage 3 — design the ENC workers from what Richard says.**
- Only now design the team. Read the ingested thread; write
  `design/2026-09-12-first-three-projects.md` § Emperor's New Coin in the shape above (goal and charter,
  predicted first team, week-one events and correct reactions, what the operator needs on screen, the
  budget) as "what Kai and Richard have agreed" with dates, plus the open questions the thread leaves.
- Kai reviews before it becomes the charter; then run the architect interview and record its actual
  decisions beside the prediction.

The government and marketing-manager projects follow the same pattern (a storage repo each, or a
subfolder of `agent-enc`'s sibling — propose, don't decide) once Stage 3 has shown the shape works.

## 🔴 Ask Kai

- Before W0 step 2: show the send command and wait — it posts to Kai's phone.
- Before Stage 2's history pull of the Richard thread: a yes. It lands as named documents in the `enc`
  project, rendered into `agent-enc`; there is no separate raw export.
- Before Stage 1 touches `feat/project-connections`: agree with thread 02 who merges it.
- The Richard WhatsApps as a paste only if W0 fails; until then draft the coin section from the repo's
  design docs and say clearly what is invented.
- The government's scope (which stories, which roles).
- Before any billable run (`./stack … up` against the real model).

## House rules

Shared checkout: commit per ticket on `main`, stage only your files, never push, don't switch branches.
Every claim cites a file or a command. Rundown style. Nothing the marketing manager drafts goes public
without a human; nothing about the coin contradicts the claim ledger ("no admin key" unqualified is false).

## First action

Read the documents, then reply with the three project sections drafted at outline depth, the assumptions
marked, and the two questions above.
