---
name: gpom-premiere-naming
description: "2026-11-04 Kai: GPOM live Premiere sequences are named \"NN GPOM <start|music end|story X name> rN\" in film order, plus two nested \"00 RENDER\" masters"
metadata:
  node_type: memory
  type: project
  originSessionId: d0d90f9d-ddbf-43a5-ae1b-16968b1f6d47
  modified: 2026-11-04T18:17:53.702Z
---

On 2026-11-04 Kai asked for the live sequences in gpom-story.prproj ("00 the film (live sequences)") to read in story order. He chose the format number + name + round. He also OK'd renaming his own sequence, but only its name; its contents stay untouched.

The names:
- 01 GPOM start (was gpom-1-track-and-off-switch: the track and the off switch, 4:40)
- 02 GPOM music end rN (music video only)
- 03 GPOM story A kill bots rN
- 04 GPOM story B bridge rN
- 05 GPOM story C walk out rN
- 06 GPOM story D crossing rN
- 07 GPOM story E ending rN

The two finished films are nested master sequences:
- **00 RENDER music video:** 01 up to 161.958 s, then 02.
- **00 RENDER story:** all of 01, then A, B, C, D, E.

The 720p scenes sit at Motion Scale 150 inside the 1080p masters.

**Why:** Kai wants to read the sequences in order and render each final video from its own combination of sequences.

**How to apply:**
- Name every new round in this format; never use the old gpom-N-X-name-rN style.
- When a scene gets a new round, swap it into the matching RENDER master at the same position, and shift any later clips if its length changed.
- Each scene.json premiere record keeps the old name under `was_named`.

Related: [[timeline-drives-premiere]], [[no-split-brain]], [[gpom-timelines-index]].
