---
name: flow-moved-to-flow-google-com
description: "2026-09-13 — Google rebuilt Flow at flow.google.com (Angular); flow-mcp re-mapped same day for stills/edit/refine/framed video (commits f2d9df3, ff1df80); characters, list_media, refine_video, Scene Builder still UNMAPPED"
metadata: 
  node_type: memory
  type: project
  originSessionId: bc002914-081e-46c9-a66e-3eafc232e0c4
  modified: 2026-09-13T14:03:53.791Z
---

Google rebuilt Flow (React → Angular) and moved it to `flow.google.com` on/before 2026-09-13.
It looked like the branded-Chrome switch ([[concurrent-browser-sessions]]) broke Flow — it did not.

**Fixed same day** (commits f2d9df3, ff1df80, live-proven via `packages/flow-mcp/src/smoke-rebuild.ts`
on free tiers): status, list/open/create project, generate_image, edit_image, refine, generate_video
(start frame; start+end). **Still unmapped** — throw `FLOW_REBUILD_UNMAPPED`: all character tools,
list_media, refine_video, Scene Builder, casting a character. Batch + text-only video coded, not run.

Source of truth: `docs/flow/automation-2026-09-rebuild.md` (10 traps + credit table).

**Why:** the biggest traps are silent — old media URL returns HTML with 200; tile src is a re-encode
(harvest only via More options → Download → Original size); an upload still "Uploading" lets Add to
prompt attach a DIFFERENT image; a bare refine prompt makes an unrelated picture.
**How to apply:** after editing flow-mcp, `/mcp` reconnect `flow`. Free test tiers: Nano Banana 2
images and Veo 3.1 Lite [Lower Priority] video are 0 credits. Two scratch projects
("Sep 13 - 14:40", "Sep 13 - 14:42") hold smoke output. Related: [[flow-automation-integration]]


**2026-10-17: Characters RE-MAPPED** (create, body, list, get, info, casting into stills; video cast coded not run). Still unmapped: create_from_media, edit_character, list_media, refine_video, Scene Builder. Findings: docs/flow/automation-2026-09-rebuild.md items 63–73 (stage doesn't redraw after upload → reload; name/info save only on Done; server-side upload refusal visible only in the maseQ RPC). Smoke: packages/flow-mcp/src/smoke-characters-rebuilt.ts.
