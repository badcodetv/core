# Recording what Chrome plays — findings, 2026-09-11

Status: experiment complete. A proper tool is not built yet. Relates:
[`2026-09-11-listen-mcp.md`](./2026-09-11-listen-mcp.md) (the describe-audio plan this feeds).

## Why

Claude can't hear. The listening plan gives it ears (Gemini through AI Studio), but it needs an
audio file, and **Suno downloads are human-only** because of the monthly allowance
(`docs/suno-gpt/automation.md:335`) — a cost rule, not a permission one. Recording the player's
output is simply **automating the Play button**: same request, same stream, one more play on the
song's count (Kai, 2026-09-12 — *"we're just automating pressing play"*). Releases still come from
the official download, because that is the master and the recording is a 125 kbps stream copy.

## The method (proven live)

```
pactl load-module module-null-sink sink_name=listen_cap     # a silent virtual speaker
PULSE_SINK=listen_cap ./scripts/browser-channel.sh claim suno   # Chrome's sound goes there
ffmpeg -f pulse -i listen_cap.monitor -ac 2 -ar 44100 raw.wav   # record the speaker
  (Playwright clicks the song page's "Play" button, waits for audio.duration, pauses)
kill -INT <ffmpeg>;  trim to the song;  pactl unload-module <id>
```

WSLg carries Linux sound to Windows over an RDP audio link. That link is lossy and quiet, which
is why the WSL Chrome sounds bad when you listen live. **The recording taps Linux audio before
that link.**

## What was measured

| Claim | Result |
|---|---|
| The chain adds no damage | ✅ 29 s pure tone: 0 glitches, THD+N −66 dB re signal, noise floor about −108 dB in 8–16 kHz |
| It's repeatable | ✅ two independent recordings of the same song are sample-identical, bar one 17-sample (0.4 ms) slip at about 2:14 |
| Stereo survives | ✅ a panned test tone kept a 16 dB L/R difference |
| Signed-in playback gets better audio | ❌ **No.** The same cloudfront `/1/clip/<id>.m4a` is served either way, and the audio is identical |
| What the player streams | ~125 kbps AAC (3,130,800 B for 200.8 s), **encrypted**, with the key fetched via `POST /api/mango/rights`. 🔴 Never try to decrypt it |
| A Suno download is triggered | ❌ **No.** No download or export request appears in the request logs (32 and 68 requests), and only Play was clicked |
| Side effects | Each recording adds one play to the song's public count. **Suno auto-plays the next song**, so stop at the duration and trim |
| The audible hiss | It's in Suno's audio, not the chain: 8–16 kHz sits at about −86 dB during the solo-synth intro and jumps by about 40 dB when the drums enter |
| Volume | One run came out 21 dB quieter than sent, so a real tool must pin the stream volume to 100% |

## Kai's preview filter

From an 8-way A/B over 30 s of the drop (low-passes at 14k, 11k, 8k and 6k; `afftdn` gentle and
strong; `anlmdn`), Kai picked **`lowpass=f=8000:poles=2,lowpass=f=8000:poles=2`**.

🔴 Apply it **only to the human preview copy**. The copy the listening tool measures and sends to
Gemini stays raw, or the brightness and loudness numbers are falsified.

## Open

- Whether a Windows browser receives a better stream is unverified (F12 → Network → `m4a`).
- The "one Suno tab" and "navigating wipes the create form" rules apply. The experiment navigated
  a fresh create tab, and a tool must check form state first.
