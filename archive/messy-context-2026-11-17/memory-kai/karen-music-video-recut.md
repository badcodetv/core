---
name: karen-music-video-recut
description: "2026-11-05 Kai: re-cut the Karen music video (\"Karen music\" sequence) on the beat — cartoon choruses, filmed-look verses; round 1 timeline page published"
metadata:
  node_type: memory
  type: project
  originSessionId: 5ad30780-f7f6-47a3-b420-f6a310a04acc
  modified: 2026-11-05T17:14:58.279Z
---

Kai's rule (2026-11-05): picture changes on the beat (89.1 BPM); **choruses + spy-riff break = cartoon** (hitchcock navy/amber register), **verses/intro/bridge/outro = filmed-look** footage from both Premiere projects. The story project (`karen-story/Karen vid_1.prproj`, sequence "Karen story") is NOT being re-cut — Kai likes it.

- Scene folder: `docs/stories/karen/scenes/music-video/` (song-map, catalogue, new-cartoon-shots, cut-r1-plan, scene.json). Assembler: `scripts/karen/mv_recut.py r1`. Media: `D:\badcode-videos\karen-music\clips\recut\` + `recut-cartoon\` (c01–c14).
- Timeline page (same link every round): https://claude.ai/artifact/BxoWfvnpr7AFeo3T4Hm7DE — r1 99 shots; r2 108 shots, no photographic Karen (Kai: more abstract), verse shots on the strong beat of each sung line, band in the gaps. Only 4 Karen-free band clips exist (searched D: + Drive). Not yet in Premiere; build as a NEW sequence (e.g. karen-music-r1), never touch "Karen music".
- Kai OK'd generating new hitchcock-style cartoon in Flow and let Claude pick stills itself ("I trust you… proceed autonomously") — a one-off waiver of [[still-approval-gate]] for this job.
- Gemini listen was run once with Kai's yes ([[listen-only-when-asked]]); its section times were checked against chroma repetition (it was 1.5 s late on chorus 2).

**How to apply:** next round = dump the page's `notes`, answer on the page, re-run the plan; then Premiere per scene-timeline. Related: [[timeline-page-stage-4]], [[no-split-brain]].

**Timing lesson (r2, measured):** the "strong beat" picked by loudest onset was the SNARE (beats 2/4), so verse cuts sat half a bar off; the kick (low-band percussive onset) marks beats 1/3, and Kai's drop at 27.33 s confirmed it (my cut was one beat early). r4 (2026-11-06): the CHORUSES had the same fault — their starts came from where the chorus music repeats, which lands on beat 2 (snare); each moved +1 beat (`inherit.shift`). Premiere: karen-music-r4 (r3 untouched). For any beat-cut: find the downbeat from the kick / a known musical event, never from overall onset loudness. Kai (r2 note) may prefer to cut by hand in Premiere to beat markers.

**DONE 2026-11-09:** final cut = Kai's own hand edit on Premiere sequence **karen-music-r4** (after round 5; r5 sequence is superseded). Brought back onto the page by `scripts/karen/mv_from_premiere.py` (cut-final, 105 shots). Uploaded to YouTube by Kai; master `karen-music/renders/karen-music-final-2026-11-09-4k-youtube.mp4`; karen-music folder synced to Drive ([[drive-sync-tool]]).
