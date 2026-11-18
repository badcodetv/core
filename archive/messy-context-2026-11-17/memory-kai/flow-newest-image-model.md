---
name: flow-newest-image-model
description: "2026-11-17 Kai: Flow stills use the NEWEST Nano Banana in the menu (now \"Nano Banana 2.1\"); \"Nano Banana 2\" is gone from Flow"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 32cfb6fe-976c-4d0c-b53b-4ec644a5fdb6
  modified: 2026-11-17T14:53:00.619Z
---

Stills in Flow use the newest Nano Banana in Flow's image menu: on 2026-11-17 that is **"Nano Banana 2.1"** (menu: Pro · 2 Lite · 2.1). "Nano Banana 2" no longer exists in the menu. A call naming it now fails with MODEL_NOT_IN_MENU, which lists the menu.

**Why:** Kai, 2026-11-17, after the Bank Robbery "her look" run failed on every prompt asking for "Nano Banana 2". The removal had been logged on 2026-10-19 (docs/flow/automation-2026-09-rebuild.md item 78) but never reached the skill or the tool.

**How to apply:** if a story's look.md or an old runner says "Nano Banana 2", use 2.1 and say so. When Flow adds a newer Nano Banana, switch to it and update the flow-automation skill line plus IMAGE_MODELS_HINT in packages/flow-mcp/src/flow-client.ts. This sits beside [[omni-1-2-default]] (the video model) and [[no-house-style]] (a model is not a look).
