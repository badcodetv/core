---
name: government-vibe-desk
description: "2026-11-06 Kai: vibe-only control page for the BadCode government (emotion words per minister); \"apply the vibe tweaks\" → Vibe: PR on briefs"
metadata:
  node_type: memory
  type: project
  originSessionId: 336b038e-409a-42ac-ab79-83e566417049
  modified: 2026-11-06T19:48:34.810Z
---

Kai wanted a "vibe adjustment UI" for the government and ruled it **vibe only** (emotional words:
more deadpan / sarcastic / aggressive), not a full control room. Option A: page collects, Claude
edits briefs via git PR.

Page: https://claude.ai/artifact/FVp78gm6kSrWyVVj3NLpCA (db `dials/<post>` + `history`).
Procedure: the `government-vibe` skill (.claude/skills/government-vibe/SKILL.md). Kai 2026-11-06: this URL is THE official tone tool; improve it in place, never a second page. Builder: scripts/government/vibe-page/build.py.

**Why:** git stays the source of truth for the government ([[badcode-government-live]]).
**How to apply:** on "apply the vibe tweaks", run the government-vibe skill; dump dials to vibe/feedback/ first; branch government/vibe-<date>, never the rolling PR; commits start `Vibe:` so the Cabinet Secretary keeps them.

2026-11-06 later: page redesigned as a TweetDeck of draft posts (Nailed it / Needed more / Don't do that again) + Ministers tab + scorecard. Kai asked to "effect this feedback as much as we can" → five routes in the skill (Bob memory source=vibe-desk read by cabinet next morning; Vibe: PR on briefs; Cabinet Secretary weekly; shared.md when 3+ ministers; stuck/regressed report). Applying stays manual (on request) for now; auto-apply before 06:00 was deferred. PR #11 carries it all.
