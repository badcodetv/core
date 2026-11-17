---
name: always-nano-banana-2-it-is-free
description: "Jack's standing rule for Flow stills — always Nano Banana 2, never Nano Banana Pro, because NB2 costs no credits"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4b0f0638-6a70-496a-92a0-7d2332b65cc8
  modified: 2026-10-01T17:09:27.582Z
---

For Flow still images always use **Nano Banana 2**. Never switch to Nano Banana Pro, even if he says "Nano Banana Pro 2" in a request (Flow has no model by that name; he means the free one).

**Why:** Jack, 2026-10-01, after I ran ten Magic Money Tree style tests on Pro (about 12 credits each by an unchecked third-party figure): "always use nb2 since it is free."

**How to apply:** pass `model: "Nano Banana 2"` on every `flow_generate_image` / `flow_generate_batch` call — the tool's default is Pro, so omitting it spends credits. If a frame seems to need Pro, say so and let him choose. Related: [[style-tests-stay-in-flow-prompts-in-repo]], [[use-omni-flash-not-veo]].
