---
name: badcode-government-live
description: "2026-11-05 BadCode government LIVE in Bob project `badcode` (marketing retired) — git-configured, one cabinet agent, one rolling PR, daily crons; Kai's focus is the machinery, not content yet"
metadata:
  node_type: memory
  type: project
  originSessionId: f8158cbc-70b9-4fb5-a0d9-281a6fd15295
  modified: 2026-11-05T17:49:52.771Z
---

Live since 2026-11-05. Bob project `badcode` replaced `marketing` (projects can't be renamed; marketing retired, 2 test chats kept). Local Claude Code reaches Bob via the `bob` MCP (local scope, key `BOB_MCP_KEY_BADCODE` in ~/projects/badcode/bob/.env.box, also a GitHub secret on badcodetv/core).

Design (plan: design/2026-11-05-badcode-government.md; files: docs/government/): 3 workers — news-gatherer (05:00, Workflow of 24 Sonnet researchers → labelled news memories), cabinet (06:00, ONE Opus session playing all ten ministers from briefs, Kai's choice over ten workers), cabinet-secretary (Sun 20:00, edits briefs). Exactly ONE open PR ever, branch `government/rolling`, label `government`, updated daily (Kai's rule). Merge to main → GitHub Action bob-sync.yml syncs workers/briefs/schedules into Bob. Site: badcode.tv GOVT 1 = the cabinet, /government/<post>/, teletext 401–410, read from docs/government/manifesto at build; **a push to main touching apps/site or the manifesto deploys** (site-deploy.yml, Cloudflare secrets set; Kai 2026-11-05 reversed 'a push never deploys'). So: merge the rolling PR → live site in ~1 min.

**Why:** Kai wants an autonomous government whose manifesto and statements evolve; 2026-11-05 he said the focus right now is the machinery and wiring, not the content.
**How to apply:** change the government by PR to docs/government/ (never edit Bob directly). Bob needed Agent SDK ≥0.3.280 for claude-opus-5-5 (pinned 0.3.300). Bob overrides git author via GIT_AUTHOR_* env. First sweep was thin (researchers didn't open dated pages) — fixed in PR #4; watch day-2 coverage. Related: [[parallel-thread-load]], [[chief-of-staff-marketing]].
