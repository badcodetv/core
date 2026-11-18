---
name: stories-consolidation-2026-08
description: "2026-08-06 stories tidy-up: 4 canonical story folders, story.md only (storyboard.md merged in), emperors-coin folded into MMT as a crypto, gpom-short folder deleted"
metadata: 
  node_type: memory
  type: project
  originSessionId: e5595eb9-a899-4787-b9fc-e02482a424e8
  modified: 2026-08-06T08:28:17.305Z
---

2026-08-06 tidy-up (Kai): `docs/stories/` now holds exactly four folders —
camping, gitpush-origin-master, karen, magic-money-tree — and each story keeps
**one `story.md`, never a `storyboard.md`** (matching the `new-story` skill
layout; `storyboard/` directories of Flow panel records are separate and stay).

- **camping + karen:** `storyboard.md` (Jack's scene-by-scene video guide) was
  merged verbatim into `story.md` as a "# Storyboard" section — in karen it is
  the winning canon ("if anything disagrees, the storyboard wins"). Master-notes
  transcripts live inside each folder (`master-notes-YYYY-MM-DD.md`).
- **magic-money-tree:** deprecated v1 Dawn `storyboard.md` archived to
  `storyboard/v1-comic-plan.md`.
- **emperors-coin:** no longer a story — it becomes a **cryptocurrency** that
  cross-promotes MMT. All fable material preserved at
  `docs/stories/magic-money-tree/emperors-new-coin.md`; its jump-up song at
  `songs/magic-money-tree-jump-up.md`. The `/comics/emperors-coin` coming-soon
  web stub was left untouched.
- **gpom-short:** story folder **deleted entirely** (Kai's call, mid-session —
  first moved under gitpush-origin-master/short/, then deleted to avoid
  confusion; panel records only in git history). The live comic at
  `/comics/gpom-short` stays. Its p01 became the brand register anchor at
  `docs/images/register-anchor.{jpg,md}` ([[new-image-skill]] repointed);
  `badcode panel gpom-short` now errors NO_RECORDS (resolve-panel STORY_DIRS →
  null); flow-mcp smoke-edit default ref → MMT p04.

**Why:** stories were split confusingly across story.md/storyboard.md and
non-story folders. **How to apply:** new stories get `story.md` only; put video
production guides in a Storyboard section of `story.md`, not a separate file.
