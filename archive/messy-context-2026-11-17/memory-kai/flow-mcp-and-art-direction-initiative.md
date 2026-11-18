---
name: flow-mcp-and-art-direction-initiative
description: "Re-architecting Flow image gen into an MCP server + art-direction skill; built on a worktree branch, pending live validation + merge"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1fef6160-9636-4a39-9042-804e976eafb2
---

Re-architecture of Google Flow generation, splitting mechanics from taste (inspired by the `frontend-design` plugin being pure-guidance). Replaces prose-driven Playwright puppeteering with:
- **`@badcode/flow-mcp`** — new TS workspace package (MCP server) exposing generic tools `flow_status`, `flow_generate_image`, `flow_refine`, `flow_generate_video`. Attaches to the existing logged-in Chrome over CDP `:9222` (still launched by `scripts/flow-chrome.sh`); harvests the signed CDN URL and writes with `fs` (no more curl/sandbox split).
- **`badcode-art-direction`** skill — frontend-design-style identity + calibration (avoid generic AI-comic look) + plan→critique→generate→critique loop; `make-comic` rewired to delegate image gen to it.

Decided **against a plugin**: project-scoped skills (`.claude/skills/`) + root `.mcp.json` already auto-activate in the repo; a plugin only adds value for cross-repo reuse/sharing (noted as future option). See [[flow-automation-integration]], [[comic-authoring-roadmap]], [[animate-slide-initiative]].

**State (2026-06-27):** MERGED to main and pushed to origin (merge commit `4a36c7a`). Built via a Sonnet workflow (10 TDD tasks); repo-wide typecheck + tests green. NOTE: after merging, the primary checkout needs `npm install` to pull the new deps (`playwright`, `@modelcontextprotocol/sdk`) or flow-mcp typecheck fails on missing modules. Worktree branch `worktree-feat+flow-mcp-and-art-direction` kept on disk.

**Still pending (need a logged-in Flow window):** the live smoke run (`npx tsx packages/flow-mcp/src/smoke.ts` after `./scripts/flow-chrome.sh`) and live selector-tuning of `flow-client.ts` `generateVideo` (credit gate, Veo model pre-select, `more_vert→Animate` attach) against the real UI — `flow-client.ts` is currently typecheck-gated only, written to the `docs/superpowers/flow-selectors.md` + `flow-video.md` contract. Reference/character consistency, motion art-direction, and aspect-ratio pinning are explicit future work.
