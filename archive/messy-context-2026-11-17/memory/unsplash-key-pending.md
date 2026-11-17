---
name: unsplash-key-pending
description: Unsplash API key LIVE since 2026-11-17 (production tier, 5000 req/hr); scripts/scene/unsplash-refs.py works, offer photo options in scenes
metadata:
  type: project
---

2026-11-17: Jack put the Unsplash keys in `.env` (as `export UNSPLASH_...=` lines; the script now accepts the `export ` prefix). Live test passed: HTTP 200, rate limit 5000/hour (production tier, so the app was approved).

**Why:** the real-photo step of new-scene / scene-beats / scene-images (`scripts/scene/unsplash-refs.py`) was blocked from 2026-11-13 waiting on Unsplash's review.
**How to apply:** use the script for reference-photo options instead of asking Jack to paste photos. Only the Access Key is used; the Secret Key also sits in `.env` (not needed by anything). Jack 2026-11-17: the licence question for using them in Flow "doesn't matter, we'll figure it out later": do not raise it. See [[meeting-2026-11-13]].
