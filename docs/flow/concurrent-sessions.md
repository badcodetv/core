# Browser channels — one browser per Claude session, chosen for you

> **🔴 Ruled 2026-08-26 (Kai): nobody thinks about ports.**
> *"What I'm trying to avoid is having to think about which channel is currently open. By channel
> I simply mean available browser port, available browser profile, and merging those two into a
> thing called channel."*

**A channel is one CDP port plus one Chrome profile, merged into a single number.**

| Channel | CDP port | Profile |
| --- | --- | --- |
| 1 | 9222 | `.flow-profile` — the original, untouched |
| 2 | 9223 | `.flow-profile-9223` |
| N | 9221+N | `.flow-profile-<port>` |

Ask for a channel. Never pick a port.

---

## 1. How you use it

```bash
./scripts/browser-channel.sh claim
# -> CHANNEL=2 PORT=9223 LOGGED_IN=yes
```

That is the whole interface. It finds a browser that is running, unclaimed and signed in;
failing that any running unclaimed browser; failing that it **launches one**. Then work.

| Want | Command |
| --- | --- |
| A browser to work in | `./scripts/browser-channel.sh claim` |
| What is running? | `./scripts/browser-channel.sh list` |
| A specific one | `./scripts/browser-channel.sh up 2` |
| Which am I on? | `flow_channels`, or the `channel`/`port` fields on `flow_status` |
| Kill one | `./scripts/browser-channel.sh down 2` |

Inside a session, **Flow and Suno share the session's channel** — which is correct, and is what
they already did. Across sessions they never collide.

## 2. How the choosing works

**The flow MCP server resolves its own channel** on first use, and holds it for the process
lifetime. One Claude session runs one flow-mcp process, so one session gets one browser.

Resolution order, first hit wins:

1. **`FLOW_CDP_PORT`** — an explicit pin always beats discovery, and claims nothing (a pin is the
   user's instruction, not ours to own).
2. **A live lock this process already holds** — so repeated calls are stable.
3. **The lowest channel that is UP and unclaimed** → claim it.
4. **The lowest channel that is DOWN** → claim it and report `needsLaunch`.

`suno.mts` resolves the same way: `SUNO_CDP_ENDPOINT` → `FLOW_CDP_PORT` → the channel a live
session already holds → 9222.

### Locks, and why they cannot wedge anything

A lock is `.flow-channels/<n>.lock` holding `<pid> <owner>`, written by the **long-lived** process
that owns the channel — the MCP server. `browser-channel.sh` never writes one: it exits
immediately, so a lock in its name would be stale the moment it was created. It only *reads* them,
to avoid handing you a browser another session is using.

**A lock whose PID is gone is stale and is deleted on sight**, so a crashed session never wedges a
channel — that failure would make the whole abstraction worse than typing a port by hand.

🔴 **`process.kill(pid, 0)` throwing `EPERM` means the process EXISTS but belongs to another
user.** That is *alive*, not dead. Treating EPERM as dead would let one session steal a channel
another holds — caught by test, 2026-08-26.

## 3. It works, and here is the proof

Kai's assumption was that **Playwright** only allowed one browser at a time. It does not. Verified
live on this machine 2026-08-26:

- Two Chromium instances on **9223** and **9224**, separate `--user-data-dir`, both answering
  `/json/version` at the same time.
- One Node process ran `chromium.connectOverCDP()` against **both concurrently**, opened a page in
  each, read back different titles. `ISOLATED: YES`.
- `browser-channel.sh claim` launched a channel from cold and correctly reported `LOGGED_IN=yes`.
- `suno.mts status` connected through the resolved channel and read the create form back.

**Nothing needed building in Playwright.** The blockers were ours: three hard-coded `9222`s and
one hard-coded profile path.

| Thing | Was | Now |
| --- | --- | --- |
| `flow-chrome.sh` profile | 🔴 **hard-coded `.flow-profile`** — Chrome refuses to share a `user-data-dir` between running instances, so a second launch died or hijacked the first | one profile per port, plus a session-index argument and a refusal to double-launch on a live port |
| `packages/flow-mcp` | `FLOW_CDP_PORT` or 9222, fixed at module load | **resolves and claims a channel**; `flow_status` reports it; `flow_channels` lists them |
| `scripts/suno/suno.mts` | 🔴 hard-coded `http://localhost:9222` | resolves the session's channel |
| `.mcp.json` playwright | 🔴 hard-coded | `http://localhost:${FLOW_CDP_PORT:-9222}` |

## 4. 🔴 The costs, and they are real

**Each profile is a separate login.** Chrome cannot share a `user-data-dir` between running
instances, so a new channel starts logged out — one manual Google/Flow (and Suno) sign-in, which
then persists in that profile. **When `claim` reports `LOGGED_IN=no`, stop and ask the user to
sign in, naming the channel.** Do not relaunch: that just makes a second logged-out browser.

**Credits and rate limits are per account, not per browser.** Two sessions generating in Flow
spend from the same pool and can still be throttled by Google. Channels remove *our* bottleneck,
not Google's.

**The Premiere bridge is still strictly one.** One Premiere, one panel, one command in flight
(`premiere-automation` §2 law 1). Never two sessions on the timeline.

⚠️ **The Playwright MCP is pinned at session start** and cannot follow a channel change — its
`--cdp-endpoint` is expanded from `FLOW_CDP_PORT` when Claude Code spawns the server. The `flow_*`
tools and `suno.mts` follow the channel; `browser_*` does not. In practice this rarely matters,
because the skill's standing rule is **never puppeteer Flow by hand with the Playwright MCP**.

⚠️ **`.mcp.json` changes need a session restart.** The `${FLOW_CDP_PORT:-9222}` expansion was not
verifiable in-session — if a session's `browser_*` tools reach the wrong port, check that first.

⚠️ **`.flow-profile-*/` and `.flow-channels/` are git-ignored.** The profiles hold live Google
sessions. Never commit one.

## 5. What did not change

- **Default behaviour is identical.** Nothing set → channel 1 → port 9222 → `.flow-profile`,
  exactly as before. Nobody has to opt in.
- **`close()` on a `connectOverCDP` browser still only detaches** — it never kills the user's
  Chrome. That law is unchanged and still load-bearing.
- **One browser per session**, not many. The automation never has to guess which one it meant.

---

## Where this connects

- `.claude/skills/flow-automation/SKILL.md` §1 — getting a browser; `flow_channels` in §2
- `.claude/skills/suno-automation/SKILL.md` — Suno shares the session's channel
- `packages/flow-mcp/src/channel.ts` — the resolver, with 13 unit tests in `channel.test.ts`
- `scripts/browser-channel.sh` — the manager
- [`../suno-gpt/automation.md`](../suno-gpt/automation.md) — the Suno DOM map and its traps
