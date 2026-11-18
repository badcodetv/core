---
name: runmts-tmpdir-downloads
description: run.mts downloads fail with ENOENT /tmp/playwright-artifacts when the session's /tmp is sandboxed; run it with TMPDIR=$HOME/.cache/pw-tmp
metadata:
  type: reference
---
2026-11-04 (GPOM mv-ending): `scripts/scene/run.mts` submitted and Flow rendered, but every harvest failed `download.saveAs: ENOENT … /tmp/playwright-artifacts-*`, then the runner resubmitted the "missing" clips and looped on `FRAME_SOURCE_NOT_FOUND` for 45 min. Cause: the Chrome on the channel writes downloads to the real /tmp, which a sandboxed session can't see.

**How to apply:** launch the runner as `TMPDIR=$HOME/.cache/pw-tmp FLOW_CDP_PORT=<port> npx tsx scripts/scene/run.mts …`. If the log shows `download-retry` with ENOENT, kill it at once. Duplicate takes land in `video/inbox/dupes/` and are often usable extra takes. See [[flow-automation-integration]].
