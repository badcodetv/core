---
name: timeline-index
description: 2026-11-13 Kai: ONE index page of every timeline page (KVLjAMnfz3NerFP9RQhxn6), built from scene.json; Karen/Camping/Bank Robbery stories now have pages
metadata:
  type: project
---
Kai asked (2026-11-13) for an index of all timeline artifacts across the films: https://claude.ai/artifact/KVLjAMnfz3NerFP9RQhxn6.
Built by `scripts/scene/build-timeline-index.py`; order in `docs/stories/timelines-index.json`; shorts auto-found.

**Why:** Kai prefers noting on timeline pages over manual Premiere; with 7 films + shorts he lost track of which page is which.
**How to apply:** whenever a timeline page is made or replaced, rebuild and republish the index to the same file path
(a story's `overview-board` is per-film; this is across films). Pre-timeline-tool films are brought on with
`scripts/scene/premiere-to-edl.py` (`--stem`, `--beats-from`) + a Premiere render. Check which sequence Kai has OPEN
before building: the Bank Robbery page was first built from cut 10 when he meant `bank robbery short - cut 7g`.
Related: [[timeline-page-stage-4]], [[overview-board-skill]], [[drive-sync]].
