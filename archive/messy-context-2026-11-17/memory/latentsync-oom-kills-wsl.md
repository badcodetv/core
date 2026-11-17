---
name: latentsync-oom-kills-wsl
description: "LatentSync lip-sync runs use 8GB+ system RAM; an out-of-memory kill used to take down all of WSL, disconnecting Zed and every Claude session"
metadata:
  node_type: memory
  type: project
  originSessionId: 12aac96a-7bee-40e4-8e6a-96c59dd87ba5
  modified: 2026-10-31T10:35:57.782Z
---

On 2026-10-31 Zed kept disconnecting from Ubuntu. Three LatentSync test runs (09:39, 09:47, 10:15) were each followed by a drop within minutes. The 10:21 one is proven by the kernel log: Python at 6.4GB RAM + 1.3GB swap was OOM-killed, then systemd stopped all of `init.scope`, which holds Zed's server and every session. The two earlier drops match on timing only; their logs did not survive.

Fix applied: `OOMPolicy=continue` drop-ins in `/etc/systemd/system/init.scope.d/` and `system.conf.d/`, plus `C:\Users\jackt\.wslconfig` (memory=10GB, swap=20GB, needs `wsl --shutdown` to apply).

**Why:** RAM ran out, not the RTX 4070's VRAM. A failed lip-sync run is now meant to die alone, so a killed run says the job needs more memory or shorter clips.

**How to apply:** Before running LatentSync, check `free -h` shows the new limits; run one clip at a time. If Zed drops again, check `journalctl -b -1 | grep -i oom` first.
