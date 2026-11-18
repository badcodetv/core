---
name: flow-lipsync-not-latentsync
description: "2026-11-11 Kai dropped LatentSync (repainted mouths show); talking shots = Flow clips with the line in the prompt, lined up by scripts/lipsync/flow-align.py"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 33a4fdac-9db2-4eb1-a4f9-b5fb47322a30
  modified: 2026-11-11T18:17:00.317Z
---

Kai, 11 Nov 2026 (GPOM bridge r11): LatentSync "is not her actual natural mouth… back out of this approach… regenerate in flow". And: plain Flow "is where we started and the timing just drifts massively", so he wanted "a system of lining the timing up between the flow video and the audio".

**Why:** LatentSync repaints the mouth region and the artefacts read on screen. Omni's own audio does not follow its picture (0.45–0.7 s off), so placing a dub on Flow's audio or whisper times drifts.

**How to apply:**
- Make the talking clip in Flow with the spoken line in the prompt, paced to our voice take's length (starts ~0.5 s in, says it once, mouth shuts). Face front or three-quarter. Roll 2+ takes.
- Run `~/.cache/badcode-lips/venv/bin/python scripts/lipsync/flow-align.py <clip> <voice.wav> <out-dir> <name>` on each take: it measures the mouth (lips.py), places the voice phrase by phrase (place-dub.py), eases the picture ≤12% (picture-warp.py) and prints before/after offsets. Pick the take whose runs all land within −0.05 / +0.13 s.
- If none does, the line is heard over another shot (side-on talking is always off screen).
- Several Flow jobs sharing one start plate get their tiles mixed up: one missing job per plate per run.

Related: [[flow-late-tile-shifts-batch]], [[omni-1-2-default]].
