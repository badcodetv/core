---
name: flow-calls-one-at-a-time
description: Jack 2026-11-17 "remember this for next time": never send Flow MCP calls in parallel; one flow_* call per message, wait for its result, check it, then the next
metadata:
  type: feedback
---

On 2026-11-17 (Priority Lane round 19) three `flow_edit_image` calls sent in one message collided in the single Flow browser: two failed (a download into a missing temp file, a click blocked by another call's overlay) and one ran on into the background. Re-run one at a time, all three worked.

**Why:** there is one Flow browser tab; parallel calls fight over its prompt box, uploads, overlays and downloads, and the results get crossed or lost.
**How to apply:** one `flow_*` call per message (stills and videos alike), wait for its result, run the reference-copy / physics check, then send the next. Writers and other non-Flow work can still run in parallel. See [[flow-unusual-activity-refresh-retry]], [[run-flow-runner-unsandboxed]].
