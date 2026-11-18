---
name: new-image-skill
description: "new-image skill = the still-making METHOD (variety, casting, loop); since 2026-10-28 it holds no look — it reads the story's look.md"
metadata: 
  node_type: memory
  type: project
  originSessionId: 51142e6e-ba13-47f8-bed8-e41a41ec3af7
  modified: 2026-08-06T08:28:06.311Z
---
The **`new-image`** skill (`.claude/skills/new-image/SKILL.md`) makes any still for a story: variety
mode, casting, the plan→critique→generate→critique loop over the Flow MCP tools. **Since 2026-10-28 it
holds no look**: it reads the story's `docs/stories/<story>/look.md` ([[no-house-style]]). The two
registers it used to carry are GPOM's (and the people one also Camping's, Karen's, MMT's) and now live
in those look.md files; the anchor images in `docs/images/` are GPOM's anchors.

Conventions kept: destination asked per image (default `docs/images/<slug>.jpg`), `<slug>.md` beside
it with the exact prompt, `docs/images/README.md` as the catalogue. It launches Flow Chrome itself
(`./scripts/flow-chrome.sh`, wait for CDP :9222, `flow_status`).
