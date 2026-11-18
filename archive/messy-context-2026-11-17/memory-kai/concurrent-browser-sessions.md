---
name: concurrent-browser-sessions
description: 2026-08-26 — browser CHANNELS (port + profile merged into one number); the agent runs browser-channel.sh claim and never picks a port; flow-mcp self-resolves and PID-locks
metadata: 
  node_type: memory
  type: project
  originSessionId: bc002914-081e-46c9-a66e-3eafc232e0c4
  modified: 2026-09-13T13:18:46.314Z
---

**2026-08-26 (Kai ruling).** *"I never have to mess around with what session or port."* A
**channel** merges the two things nobody should track — CDP port and Chrome profile — into one
number. Channel 1 = 9222 + `.flow-profile` (unchanged); channel N = 9221+N with its own profile.

**The agent's only move: `./scripts/browser-channel.sh claim`.** It picks a running, unclaimed,
signed-in browser; else any running unclaimed one; else launches one. Prints
`CHANNEL=n PORT=p LOGGED_IN=yes|no|unknown`. **Never pick a port by hand.**

**flow-mcp resolves and claims its own channel** on first call and holds it for the process
lifetime (one Claude session = one flow-mcp process = one browser). Order: `FLOW_CDP_PORT` pin →
lock already held → lowest up+unclaimed → lowest down. `flow_status` reports channel/port;
`flow_channels` (new, 23rd tool) lists them. `suno.mts` resolves the same way so Suno shares the
session's browser.

**Locks** are `.flow-channels/<n>.lock` = `<pid> <owner>`, written only by long-lived processes;
stale PIDs are deleted on sight so a crash never wedges a channel. 🔴 `kill(pid,0)` throwing
**EPERM means alive** (another user's process) — treating it as dead would steal a channel.

**Proven live:** two Chromiums on 9223/9224 driven concurrently by one Playwright process,
isolated; `claim` cold-launched channel 1 and detected the login; `suno.mts status` read the form
back through the resolved channel. 240 tests pass, tsc clean. **Playwright was never the limit.**

**Real costs:** each profile is a **separate login** (say so, don't relaunch); credits/rate limits
are **per account**; the **Premiere bridge stays strictly one**; the **Playwright MCP is pinned at
session start** and cannot follow a channel change.

🔑 **2026-09-13 Kai ruling: branded Google Chrome on EVERY channel** (was: listening channel only).
`flow-chrome.sh` now prefers `google-chrome`; Chromium/Playwright bundle is fallback only. One-way
door per profile — pre-switch copies kept at `.flow-profile*.for-testing.bak/`. Switching lost the
saved logins (different cookie key), so each channel needs one re-sign-in.

Docs: `docs/flow/concurrent-sessions.md`. Code: `packages/flow-mcp/src/channel.ts` (+13 tests),
`scripts/browser-channel.sh`.

Related: [[flow-automation-integration]], [[suno-session-method]], [[premiere-bridge-initiative]]

**2026-09-28 SUPERSEDED — never run `claim` in a session.** flow-mcp now LAUNCHES its own held channel on first use (`ensureBrowser` in server.ts) and suno.mts does the same for that channel. `claim` skipped the MCP's locked-but-down channel and opened a second Chrome every cold session (Kai saw two windows). Just call `flow_status`. Uncommitted as of 2026-09-28; live one-window proof not yet run.

**2026-10-23:** a `/mcp` reconnect of `flow` in a session that wasn't doing Flow work (done only to load new code) attached that session's flow server to the shared Chrome on 9222 at 16:29. It took over the download path, and the gpom-second-half session's Flow helpers lost about an hour. **How to apply:** before asking Kai to reconnect `flow`, check whether another session is running Flow (`ListAgents`) and warn it, or wait until it's idle. A session that doesn't need Flow should leave the flow server disconnected.
