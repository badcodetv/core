---
name: agent-enc-and-whatsapp-channel
description: "2026-09-12 Kai rulings — agent-enc is a storage-only repo (Bob git-projection target, no UI/login); Kai's WhatsApp becomes a Bob connection by reusing Platinum's WAHA session; Richard thread ingested through the channel, ENC workers designed after"
metadata: 
  node_type: memory
  type: project
  originSessionId: 23bf9342-5511-4372-aced-48bed7291a7c
  modified: 2026-09-12T10:41:55.075Z
---

Ruled by Kai on 2026-09-12 (orchestration session; plan in badcode
`design/2026-09-12-threads/03-agent-bob-three-projects.md`):

- **`~/projects/badcode/agent-enc`** is a new repo that is *only* the persistent storage layer of the
  Emperor's New Coin project on Agent Bob: workers read/write configuration and documents there;
  humans use Bob's own console. It is NOT like agent-wolf (no app, no UI, no login). Mechanism = Bob's
  git projection (`agent-bob/docs/21-git-projection.md`): DB is the only ordered truth, git is render-out
  and import-in; the memory log is not in the repo.
- **WhatsApp channel = Kai's WhatsApp only**, reusing Platinum's WAHA container as-is
  (`~/projects/bayesprice/Platinum` `waha` service, NOWEB engine, session `default`, API key =
  Platinum's `SYSTEM_SECRET`, linked device = Kai's own account). Kai is happy for the one session to
  serve both. "The token" is the API key + the linked session in the `waha-data` volume on Platinum's
  production host; Bob calls it where it runs. WAHA free tier reads (message webhook + chat history).
- **Order:** W0 proof (send to self, read the Richard thread) → Stage 1 project + connector → Stage 2
  ingest the Richard thread *through the channel* as named documents (no static export) → Stage 3
  design the ENC workers from what Richard says. The 03 session runs W0, not the orchestrator.
- Relevant unmerged work: `feat/project-connections` (checkout `agent-bob-connections`, 32 commits;
  T12/T14/T15 pending). Thread 02 owns merging it.

**Why:** WhatsApp is where the coin's working knowledge lives; a live channel beats a paste, and the
storage repo makes the project reviewable as files.
**How to apply:** don't propose a UI for agent-enc; don't propose a second WhatsApp number; see
[[work-board-2026-09-12]], [[enc-artwork-not-ecosystem]], [[agent-orange-initiative]].
