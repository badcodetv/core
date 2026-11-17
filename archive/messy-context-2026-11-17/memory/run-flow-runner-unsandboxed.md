---
name: run-flow-runner-unsandboxed
description: Run scripts/scene/run.mts (and any Flow download) with the Bash sandbox off, or every clip renders, bills and then fails to download (ENOENT playwright-artifacts)
metadata:
  type: feedback
---

2026-11-16 (Malevolent Force clips): run.mts started inside the Bash sandbox rendered 10 clips, lost every download (`download.saveAs: ENOENT … /tmp/playwright-artifacts-*`), thought the wave failed and resent the same five jobs, billing them twice. The files were in `~/Downloads` under Flow's titles (3 copies each), readable only unsandboxed.

**Why:** the browser writes downloads outside the sandbox's private /tmp (docs/flow/automation-2026-09-rebuild.md item 28).

**How to apply:** always launch run.mts with `dangerouslyDisableSandbox: true`. If it happens anyway, don't re-run: take the files from `~/Downloads` by time (newest grid tile first) and write recipe cards with `prov.py card`. Do not run Suno or a flow MCP batch while run.mts or another Flow download is in flight: a Suno run attaching to the same Chrome broke a Flow image download (2026-11-16). WSLg audio was wedged on 2026-11-16 too: `suno.mts record` needs Chrome relaunched onto the private PulseAudio (scripts/audio-server.sh, then pkill the 9222 Chrome and flow_status). Suno's workspace picker also fails on the first try after each Create; round.py aborts safely, retry with --only.
