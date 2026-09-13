#!/usr/bin/env bash
# Print the PULSE_SERVER a browser channel should play into, starting a private one if needed.
#
#   ./scripts/audio-server.sh          → e.g. unix:/mnt/wslg/PulseServer  or  unix:/tmp/badcode-pulse/native
#   ./scripts/audio-server.sh status   → which server answers, and why
#
# WHY (2026-09-13). WSLg's PulseAudio wedges: its socket still exists but nothing answers, and
# every pactl/ffmpeg call hangs. It happened on 2026-09-12 and again on 2026-09-13, and it silently
# killed recording (flow-chrome.sh launched Chrome with no sink). Recording does not need WSLg at
# all — a null sink on ANY PulseAudio server captures Chrome's audio before it reaches a speaker —
# so when WSLg does not answer within 3 s we start our own PulseAudio, private to this user, and
# use that instead.
#
# The cost is honest and small: on the private server the channel RECORDS but is not audible in
# WSL (there is no speaker behind it). Kai listens to Suno on Windows anyway; the recording is for
# Claude.
set -euo pipefail

WSLG="unix:/mnt/wslg/PulseServer"
DIR="/tmp/badcode-pulse"
PRIVATE="unix:$DIR/native"

answers() { PULSE_SERVER="$1" timeout 3 pactl info >/dev/null 2>&1; }

if [ "${1:-}" = "status" ]; then
  if answers "$WSLG"; then echo "WSLg: answers"; else echo "WSLg: NOT answering (wedged or absent)"; fi
  if answers "$PRIVATE"; then echo "private ($PRIVATE): running"; else echo "private: not running"; fi
  exit 0
fi

if [ -S /mnt/wslg/PulseServer ] && answers "$WSLG"; then
  echo "$WSLG"
  exit 0
fi

if ! answers "$PRIVATE"; then
  command -v pulseaudio >/dev/null 2>&1 || { echo "audio-server: WSLg is not answering and pulseaudio is not installed" >&2; exit 1; }
  mkdir -p "$DIR/state"
  rm -f "$DIR/native"
  # -n: skip default.pa (it probes ALSA/udev, which WSL has not got). The idle null sink is the
  # default, so a stream that is not routed anywhere still has somewhere harmless to go.
  env -u PULSE_SERVER PULSE_RUNTIME_PATH="$DIR" PULSE_STATE_PATH="$DIR/state" XDG_RUNTIME_DIR="$DIR" \
    timeout 10 pulseaudio -n --daemonize=yes --exit-idle-time=-1 --use-pid-file=yes \
      --log-target="file:$DIR/log.txt" \
      -L "module-native-protocol-unix socket=$DIR/native auth-anonymous=1" \
      -L "module-null-sink sink_name=badcode_idle" >&2
  for _ in 1 2 3 4 5 6 7 8 9 10; do answers "$PRIVATE" && break; sleep 0.3; done
  answers "$PRIVATE" || { echo "audio-server: started a private PulseAudio but it does not answer — see $DIR/log.txt" >&2; exit 1; }
  echo "audio-server: WSLg audio is not answering — using a private PulseAudio at $PRIVATE (records, not audible)" >&2
fi
echo "$PRIVATE"
