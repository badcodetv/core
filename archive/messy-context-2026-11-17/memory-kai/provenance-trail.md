---
name: provenance-trail
description: 2026-10-23 Kai — every generated file leaves a recipe card; scene trail.json per publish; final.json per finished cut; going forward only, no backfill
metadata:
  type: project
---
Kai ruled 2026-10-23: keep a production trail good enough to rerun a whole story's exact prompts on a better video model later. The convention is docs/provenance/README.md (linked from CLAUDE.md and the new-scene skill). Tool: scripts/provenance/prov.py (card / trail / check / freeze). The TS twin is packages/flow-mcp/src/prov.ts.

**Why:** the new-scene loop (timeline feedback pages, see [[timeline-page-stage-4]]) produces many artifacts and their history was getting lost. Kai: the repo (GitHub) holds everything but the media; D: is backed up to Google Drive; the two together = everything. So the media living only on D: is fine.

**How to apply:** cards are written automatically by the Flow MCP generation tools, run.mts (via match.py), aistudio-tts.py and Suno `record`. Card anything else by hand. Run `prov.py trail` after every page publish, `check` before showing a cut, and `freeze` when Kai says a cut is done. Do NOT backfill older stories; Kai was explicit. The replay script is deliberately unbuilt until a better model arrives. The Flow MCP needs a /mcp reconnect to pick up the stamping.

Also 2026-10-23: each story's running order lives in docs/stories/<story>/timelines.json (built by scripts/provenance/build-timelines.py), which reads scene trail/boards/final automatically. See [[gpom-timelines-index]].

**2026-10-23, later: artifacts are the UI, the repo is the record (Kai).** Every page is built by a builder, and its command goes in the trail as `--rebuild`. Every read of a page's db is dumped raw first (`ArtifactData list … out_dir=$(prov.py feedback-dir <scene> --stage … --round N)`), then logged with `prov.py trail … --feedback --decided "<Kai's words>"`. A lost page is rebuilt, then refilled with `prov.py restore` (ArtifactData batch sets). The overview board shows the decisions under each page, so it doubles as the decision log.
