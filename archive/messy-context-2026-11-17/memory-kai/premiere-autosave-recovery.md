---
name: premiere-autosave-recovery
description: "2026-10-19 lost-cut rescue — Premiere auto-saves every few minutes into \"<project dir>/Adobe Premiere Pro Auto-Save/\"; a .prproj is gzipped XML you can parse to see a sequence's clips per version"
metadata:
  node_type: memory
  type: reference
  originSessionId: 9c445eb7-43dc-4ec3-ad5e-f29c340d3554
  modified: 2026-10-19T12:59:22.111Z
---

On 2026-10-19 Kai used Save As to make a backup, kept working in the backup, then saved the backup over gpom-story.prproj, and the robot/parade/eye cut in gpom-s01 (62–82s) seemed lost.

It was in Premiere's auto-saves: `D:\badcode-videos\gitpush-origin-master\Adobe Premiere Pro Auto-Save\`. A new one is written every few minutes, named `<project>--<uuid>-<date>_<time>.prproj`. The 12:09 backup auto-save held the cut. Copies of every version from that day are in `_rescue-2026-10-19/`, and the good one was put beside the main project as `gpom-story-RECOVERED-1209.prproj`.

**How to apply:** when a cut "vanishes", first copy all the auto-saves somewhere safe. Then gunzip each .prproj and list the timeline clips in each version: walk Sequence → VideoTrackGroup → Track → TrackItem Start/End (254016000000 ticks per second) → SubClip Name. Never Save As over anything until the right version is found.

Kai's Save As trap: Save As switches the OPEN project to the new file. See [[premiere-bridge-initiative]].
