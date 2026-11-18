---
name: suno-playback-recording
description: "2026-09-11 proven — record any Chrome audio silently via a PulseAudio null sink in WSLg; Suno preview copies without the download button; Kai's preview filter = 8 kHz low-pass"
metadata: 
  node_type: memory
  type: project
  originSessionId: c1009392-aace-4273-8105-aa95d9dd4862
  modified: 2026-09-11T15:17:43.328Z
---

**Proven live 2026-09-11 (session "claude-can-hear").** Any sound the WSL Chrome plays can be recorded silently and in stereo:
`pactl load-module module-null-sink sink_name=listen_cap` → launch Chrome with `PULSE_SINK=listen_cap` (works through `PULSE_SINK=listen_cap ./scripts/browser-channel.sh claim suno`) → `ffmpeg -f pulse -i listen_cap.monitor` → Playwright clicks Play → stop at `audio.duration` → `kill -INT` ffmpeg → unload the module. The recording taps Linux audio BEFORE the WSLg→Windows RDP link (that link is why WSL Chrome sounds bad live).

**Kai's ruling:** recordings are allowed as **preview copies only** — an experiment, releases still go through Suno's official download. This is a narrow exception beside the no-automated-download rule ([[suno-four-box-atom]] era rules; `docs/suno-gpt/automation.md:335`), because it spends no download allowance.

Facts measured:
- Suno's player streams an **encrypted** ~125 kbps AAC `.m4a` from cloudfront; the key comes from `POST /api/mango/rights`. Never try to decrypt it.
- **Signed-in playback gets the identical file** as logged-out (sample-for-sample) — signing in buys no quality.
- Chain noise floor −108 dB; two independent runs identical bar one 0.4 ms slip. The audible hiss is in Suno's audio (follows the drums, absent in quiet intros).
- Each play bumps the song's public play count; **Suno auto-plays the next song** — stop at duration and trim.
- In one test the sink attenuated 21 dB — lock volume to 100% in a real tool.

**Kai's preview filter (2026-09-11):** `lowpass=f=8000:poles=2` applied twice (picked from an 8-way A/B over 14k/11k/8k/6k low-passes and afftdn/anlmdn denoisers). Apply ONLY to the human preview copy — never to the copy the listening tool measures/sends to Gemini.

Related: the listen-mcp plan `design/2026-09-11-listen-mcp.md` (describe-audio tool, awaiting approval); a "recorder" tool is proposed but not planned yet. [[suno-one-session-at-a-time]] [[suno-check-form-mode]]
