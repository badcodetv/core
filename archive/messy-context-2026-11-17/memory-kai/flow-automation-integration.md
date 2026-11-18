---
name: flow-automation-integration
description: How the Google Flow browser-automation integration works — proven setup + the image-harvest trick
metadata: 
  node_type: memory
  type: project
  originSessionId: 1bc8f17a-67db-41e5-91e5-cc49aa754a18
---

Google Flow image generation is driveable end-to-end from Claude Code, proven 2026-06-25 (branch feat/flow-automation-spike). This is the SP3 "Flow automation loop" (see [[comic-authoring-roadmap]]).

**Setup (WSL-specific):** `./scripts/flow-chrome.sh` launches Playwright's bundled Linux Chromium (no system Chrome in WSL) via WSLg with `--remote-debugging-port=9222 --user-data-dir=.flow-profile --no-sandbox`. Login persists in `.flow-profile/` (gitignored). The `@playwright/mcp` server (project `.mcp.json`, `--cdp-endpoint http://localhost:9222`) attaches to it — so Claude drives Kai's logged-in session. Windows-side chrome.exe is unusable (CDP port not reachable under default WSL NAT). The `.mcp.json` only loads on Claude Code startup, so a new session / `claude --resume` is needed after it's added (resume reloads MCP + restores thread). Launch Chrome **detached** (`setsid`), else it dies with the session.

**Flow UI is agent-driven**, not a prompt+refs+Generate form: a chat textbox ("What do you want to create?") + `arrow_forward Create` submit. A plain "Generate a single image: <scene>" produces ONE image (not best-of-N) — so selection is **generate → judge → follow-up correction in the same session**, not pick-from-grid. Account is ULTRA (full models). Built-in "Make a Story"/"Develop a storyboard" agentic modes exist. References/consistency via left-sidebar Characters / Add Media (own spike still pending — biggest quality risk for a multi-frame comic).

**Image harvest trick (the key enabler):** generated `<img>.src` = `labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=<uuid>`. In-page fetch fails (CORS). Use Playwright `page.request.get(url)` (server-side, carries cookies) → `resp.url()` returns a **signed, publicly-fetchable** `https://flow-content.google/image/<uuid>?Expires&Signature` CDN URL → `curl` it to disk. No UI download, no image bytes through model context. NOTE: `browser_run_code_unsafe` sandbox has no `require`/`import`/`fs` — only `page`; do file writes in the deterministic CLI or via shell curl.

Recipe doc: `docs/superpowers/flow-selectors.md`. First harvested frame: `.flow-profile/tmp/spike-frame.jpg` (excellent on-brief Camping image).

**End-to-end proven 2026-06-25:** first whole comic auto-built through the pipeline — "The Magic Money Tree" (NHS nurse Dawn; manufactured-scarcity idea). idea → canon (docs/magic-money-tree/) → 10-panel storyboard → Dawn set up as a Flow **Character** (excellent cross-panel consistency) → 10 frames generated + harvested → assembled `@badcode/comic` scroll comic, live at `/comics/magic-money-tree`, verified rendering. Branch feat/flow-automation-spike. Per-panel routine that worked: run_code fill prompt + click `arrow_forward Create` → wait ~28s → run_code `page.evaluate` to find newest getMediaUrlRedirect img + `page.request` resolve signed URL → curl to `apps/web/public/comics/<slug>/img/iNN.jpg`. Frames in public/ (createComic `{baseUrl:''}`); bucket/assets-build migration is a follow-up. Agent-driven Flow generates 1 img/request and held documentary realism well except the one surreal panel (money tree) which went illustrative.
