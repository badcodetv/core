---
name: parallel-thread-load
description: "2026-09-12 — nine parallel Claude threads overwhelmed Kai within ~3 hours; cap concurrency, batch decisions, and have the orchestrator stay quiet unless an action is needed"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 23bf9342-5511-4372-aced-48bed7291a7c
  modified: 2026-09-12T15:43:13.616Z
---

On 2026-09-12 Kai launched nine parallel threads from one plan. By mid-afternoon eight were idle,
each waiting on a small decision from him, and the orchestrator was relaying every commit and status
change. Kai: "I'm kind of drowning here, too many threads, it's my fault ... we need to back off trying
to do as much stuff all in parallel at once." He stepped away; threads were parked with RESUME HERE
blocks in `design/2026-09-12-threads/status/`.

**Why:** the bottleneck is Kai's decision bandwidth, not agent throughput. Every thread ends its
free work at a human gate within an hour or two, so N threads = N simultaneous asks. Narrating
routine events (commits, status refreshes) added noise without value.

**How to apply:** default to 3-4 concurrent threads, chosen so at most one needs a credit/money
decision at a time; pre-collect a thread's likely questions into the launch brief so the first gate
is later; the orchestrator speaks only when an action is needed or Kai asks ("I'm back" → one
action), never per commit; when Kai says he is overwhelmed, park everything with a three-line
RESUME HERE and let him leave without loss. See [[work-board-2026-09-12]].
