---
name: edit-panel-loop
description: Fast iterative panel-image editing (page → prompt+golden → flow_edit_image 2 candidates) — shipped & live-validated 2026-07-14
metadata: 
  node_type: memory
  type: project
  originSessionId: 236b91b4-5d52-4364-b54e-2146660271fc
---

The "take page 4 and shift the apple left" loop shipped 2026-07-14 (built same day as
planned, live smoke passed twice: 56s then 43s for upload + x2 edit + harvest of both
candidates).

Pieces: `flow_edit_image` MCP tool (reference-image ingredients + numOutputs 1–4,
persistent cached CDP client in server.ts), `badcode panel <comic> <page>` CLI resolver
(needs `asset_key` frontmatter in `docs/<story>/storyboard/pNN.md` — backfilled for
gpom-short + magic-money-tree; camping/karen are record-less V1 imports → clean error),
`.claude/skills/edit-panel/` (the loop: always edit from the golden original, Google
"change only X, keep everything else" template, user picks A/B), `.claude/agents/flow-operator.md`
(sonnet low-effort, preflight/recovery only — deliberately lean; main convo drives MCP calls).

**Why the old way was slow:** hand-puppeteering references via Playwright MCP + Playwright
actionability stalls. On this WSLg rig coordinate-based clicks are untrustworthy —
in-page/native-event recipes per control type are in `docs/superpowers/flow-selectors.md`
("Click reliability on WSLg") and encoded in flow-client.ts helpers. Anti-degradation:
never chain edits; re-reference the clean golden each round ([[flow-script-hardening-initiative]]).

Open ends:
- **MCP server restart needed** for `flow_edit_image` to appear as a tool in a session
  whose `flow` server predates the change.
- `flow_open_project` has a KNOWN ISSUE: the projects grid can render div tiles with no
  `<a href>` (breaks the scrape → PROJECT_NOT_FOUND). Workaround documented; edit loop
  doesn't need a specific project. Also project rename via title textbox resists automation
  (test project is stuck named "Jul 14, 04:53 PM" though smoke expects "edit-smoke" — the
  smoke falls back to the currently-open project, so it still runs).
- camping-v2 records get `asset_key` when its comic ships (its images don't exist yet).
- `generateVideo` still uses the filechooser path (latent multi-client conflict) — port
  to direct `setInputFiles` when it next breaks.
- Optional: 3-round degradation control experiment never run (research-backed policy
  encoded instead).
