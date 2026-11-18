---
name: youtube-mcp
description: 2026-11-11 Kai: YouTube channel managed via our own youtube MCP (Data API v3); uploads private, going public stays a human click
metadata:
  type: project
---

2026-11-11 Kai asked to stop hand-driving YouTube Studio. Built `packages/youtube-mcp` (8 tools: status, list, get, upload, update, thumbnail, playlists, categories) + `docs/youtube/` (README setup, channel.json snapshot, log.jsonl).

**Why:** Kai only wants the *management* of the growing video set automated; he explicitly said going private→public does NOT need automating.

**How to apply:** upload private by default; only set unlisted/public/publishAt when Kai or Jack asks for that video. `containsSyntheticMedia` is required on upload (using-ai.md disclosure). 2026-11-12: CONNECTED (Cloud project "Bad Code YouTube" on Kai's account, sign-in as badcode.tv@gmail.com, channel Badcode @badcode-tv). Procedure = `youtube-channel` skill. Kai 2026-11-12: AI label on EVERY video (default on; youtube_label_ai); titles are Kai/Jack's call; descriptions+tags written for growth from repo playbooks. API accepts containsSyntheticMedia but never reads it back → log.jsonl is the record. Related: [[chief-of-staff-marketing]], [[no-spoilers-in-public-blurbs]].
