---
name: camping-trailer-resume
description: "NEWEST 2026-11-12 pm — Camping trailer 2 BUILT in Premiere (camping trailer two men.prproj, seq trailer two men r1), awaiting Jack's watch; resume at docs/marketing/camping-serial-plan.md"
metadata:
  node_type: memory
  type: project
  originSessionId: a67615b1-c7da-4451-9777-558938626e0b
  modified: 2026-11-12T14:48:16.955Z
---

State at end of 2026-11-12 (Jack's session):
- Jack rejected straight slices of the Camping film ("don't feel like shorts") and asked for fast trailers ([[clips-from-a-story-are-trailers]]). Three rough trailers went on https://claude.ai/artifact/SUr7Uzc2BqpGyYibafGus9 (db collection `picks`); Jack kept **t2 Two men, one car park** (31.6 s), no vote on t1/t3.
- Jack's calls: film's own audio + bass hits (no new music), letterbox 16:9 inside 9:16 with text, project in `Desktop\Youtube Vids\animation\shorts\camping-trailer-two-men\`.
- All Premiere pieces are cut in that folder's `cut\` (video, text overlays as ProRes alpha .mov, audio, place.js, plan.json).
- **BUILT in Premiere 2026-11-12 pm**: sequence `trailer two men r1` in `shorts\camping-trailer-two-men\camping trailer two men.prproj`, 43 clips, frames checked, saved. Next = Jack watches and notes it; then export + delivery-qc (nothing uploaded).
- Open: is the trailer added to the shorts list (`docs/marketing/badcode-shorts.md`)? Not asked yet. The press/campaign "amplifier" contact list (~30 UK targets, shorts-growth.md §7) was started and stopped by Jack; restart only if he asks.
- Rebuild tools: `design/camping-serial/build_trailers.py` (rough previews), `premiere_pieces.py` (Premiere pieces), word timings `design/camping-serial/camping-words.json` (faster-whisper; venv was in the session scratchpad, reinstall with `pip install faster-whisper` and load audio as a numpy array, PyAV's open() signature mismatches).
