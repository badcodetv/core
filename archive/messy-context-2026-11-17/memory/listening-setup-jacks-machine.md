---
name: listening-setup-jacks-machine
description: Jack's machine needs LISTEN_MEDIA_ROOT overridden; GEMINI_API_KEY is in .env since 2026-09-24 but the listen MCP only reads it at startup.
metadata:
  type: project
---

On Jack's machine (`/home/jackt`) the Suno listening loop records, measures and — since
2026-09-24 — listens:

- `LISTEN_MEDIA_ROOT` must be set to `/mnt/c/Users/jackt/OneDrive/Desktop/suno-recordings` — the
  default is Kai's desktop and fails with EACCES. Jack's Desktop is OneDrive-redirected;
  `/mnt/c/Users/jackt/Desktop` does not exist.
- ✅ **`GEMINI_API_KEY` is in `.env`** (added 2026-09-24). 🔴 The listen MCP reads `.env` only
  at startup, so if `listen_status` says `apiKeySet: false`, reconnect `listen` via `/mcp` — or run
  `describe()` from a one-off tsx script (`scripts/suno/.tmp/describe-once.mts`, args: path lens
  start end question), which worked first time.
- 🔴 2026-09-26: `gemini-3.5-flash` returned **429 quota** on this key; `gemini-3-flash-preview` worked — run
  `GM=gemini-3-flash-preview npx tsx scripts/suno/.tmp/describe-model.mts <wav> music "" "" "<question>"`.
  (`gemini-2.5-flash*` are 404, retired.)
- `record` only finds takes visible on the create page: type the title into the **Search clips**
  box first for an older take — and **clear it before any Create**, or the new rows are hidden.
- WSLg's PulseAudio wedges here. `./scripts/audio-server.sh` starts the private server, then the
  channel **must be relaunched** (`browser-channel.sh down 1 && up 1`) because Chrome reads
  `PULSE_SINK` at launch.
- Installed 2026-09-18 (all were missing): `pulseaudio-utils`, `pulseaudio`, `ffmpeg`,
  `python3-pip`, and numpy/librosa/soundfile via `--break-system-packages`.

Full table: `docs/listening/automation.md` §0. Related: [[suno-account-is-kais-google-login]].
- 🔴 2026-09-27: `gemini-3-flash-preview` then ALSO hit 429 after ~15 calls in a day; `gemini-3.5-flash` worked again —
  alternate the two, and call them one at a time (parallel calls tripped the quota).
- 🔴 `record-yt-seg.mts` can capture a YouTube **mid-roll advert** inside a segment on long mixes (2026-09-27, Liquid Rasta:
  a clip "switched to a funky breakbeat" at 0:25, another was "tropical pop"). Ask Gemini "could this be an advert?" and
  discard those clips.
- 🔴 2026-09-27 later: 3.5-flash, 3-flash-preview AND 3.1-pro-preview all 429'd; **`gemini-3.5-flash-lite` still worked** (lower
  confidence — say so). `3-pro-preview` and `3.1-flash-preview` are 404. The describe tool's `tempo` measurement returned
  132.51 for five different clips — it is broken; use `librosa.beat.beat_track` directly (reggae reads double: ~130 = ~65).
