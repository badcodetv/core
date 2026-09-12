# Thread 01 — Ops: the OVH box, and everything off Kubernetes

You are in `~/projects/badcode/agent-bob`. Read `CLAUDE.md`, then `docs/ops.md` end to end (it is the
step-by-step guide, written 2026-09-11 and never executed), then `design/2026-09-11-ovh-compose-hosting.md`
§9 (order of work), §10 (decisions) and §11 (unverified claims).

## Goal

One OVH dedicated server (model RISE-L, Debian, RAID1 mirror, LVM thin pool, hourly restic backups to
Google Cloud Storage, Caddy in front, Tailscale for SSH) running **Agent Bob first**, then every app
currently on the Kubernetes cluster **except NoCode Works and Franchise Cloud** — those two are being shut
down the week of 2026-09-14 and stay where they are until then. Purpose: Agent Bob and Agent Wolf must be
reachable by Kai's friends so they can log in and test.

## What done looks like

1. `docs/ops.md` Steps 0–13 executed, each marked done in the file with the date and what was actually
   observed. Kai's manual test of Bob passes on the box over HTTPS with a valid certificate.
2. The first weekly restore drill runs green and the measured restore time is written into the design §4.5.
3. Part 4 of `docs/ops.md` ("moving the GKE apps") turned into a per-app migration plan under `design/`:
   for each of the remaining apps (booking system, badcode app + worker + n8n + Postgres 17 + Redis, forum,
   kellie, quoteright, panwww, zps-apps, the shared Postgres 9.6 and Redis), what moves, its disk actually
   used (`df -h` inside the pod — the plan says usage is unknown), its gotcha, and its order. Order already
   decided: small apps first, badcode next, **booking system last**. NoCode and Franchise Cloud are out of
   scope; write one line each saying so.
4. Then execute the migrations in that order, one app at a time, each with its own commit and a rollback
   note, DNS moved last per app.

## 🔴 Stop and ask Kai — never work around

- **Anything that costs money or creates an account**: ordering the server (§10 decisions must be answered
  by Kai first), the GCS bucket billing, healthchecks.io, Tailscale sign-up. Prepare everything, then stop
  with the exact click-path and wait.
- **Anything destructive on the live cluster**: scaling a deployment to zero, deleting a disk, changing
  DNS for a live domain. Show the command, the blast radius, and the rollback; wait for a yes.
- **The shared Postgres 9.6 upgrade path** (dump-and-restore versus `pg_upgrade`): propose, don't pick.
- Found in passing on 2026-09-11 and still unactioned: **several cert-manager renewals on GKE look stuck**
  (`nocode-domains`, `zps-apps`) and 9,147 old disk snapshots (~379 GB). Report both to Kai on your first
  reply; do nothing about them until asked.

## House rules

- Commit per step on `main` with the repo's sentence-style messages, staging only the files you touched.
  **Never push.** Other sessions may be working in this checkout.
- Every claim in a report is something you ran or read, with a command or `file:line`.
- Secrets go in Kai's password manager entry "OVH box", never in the repo, never in a chat message.
- Report in the Rundown style: TL;DR, plain terms, state checklist, what Kai must do next.

## First action

Read the three documents, then reply with: (a) the §10 decisions Kai must answer, phrased as pick-one
questions with your recommendation first; (b) Step 0's four account tasks as a checklist for Kai; (c) the
cert-manager and snapshot findings; (d) what you will do autonomously while waiting (drafting
`bootstrap.sh`, the per-app migration plan from a read-only survey of the cluster).
