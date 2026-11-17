---
name: flow-browser-launch-via-mcp
description: 2026-11-05 — never start the Flow Chrome from Bash (the command sandbox makes it render nothing); call flow_status and the flow MCP launches it
metadata:
  type: feedback
---

On 2026-11-05 the Flow browser was launched with `scripts/flow-chrome.sh` from a Bash call. Inside Claude's command sandbox Chromium loads no page at all (even `data:` URLs hang) and every `connectOverCDP` times out after 30s. Running it unsandboxed was refused. `mcp__flow__flow_status` launched its own browser outside the sandbox (`resolvedBy: needs-launch`), logged in, and scripts using `FlowClient.connect` worked at once.

**Why:** an hour went on debugging extensions, GPU and network flags before the real cause turned up.

**How to apply:** if CDP on 9222 is not up, call `flow_status` first; do not launch Chrome from Bash. If a CDP attach times out, check whether the browser was started from a sandboxed shell. See [[flow-unusual-activity-refresh-retry]].
