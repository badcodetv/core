#!/usr/bin/env bash
# Check a finished file against a platform's delivery spec, and against the things that go wrong
# in BadCode's register specifically.
#
#   scripts/delivery-qc.sh RENDER.mp4              # general checks only
#   scripts/delivery-qc.sh RENDER.mp4 shorts       # + YouTube Shorts spec
#   scripts/delivery-qc.sh RENDER.mp4 youtube|shorts|reels|tiktok
#
# 🔴 This proves YOUR encode is correct. It proves nothing about what the platform's own
# re-transcode does to it afterwards — and that re-encode is what the viewer actually sees.
#
# Needs ffmpeg/ffprobe only. Read-only: it never writes to the file it is given.
set -uo pipefail

FILE=${1:-}
PLATFORM=${2:-}
[ -z "$FILE" ] && { sed -n '2,12p' "$0" | sed 's/^# \?//'; exit 2; }
[ -f "$FILE" ] || { echo "no such file: $FILE" >&2; exit 2; }

PASS=0; WARN=0; FAIL=0
ok()   { printf '  \033[32mok  \033[0m %s\n' "$1"; PASS=$((PASS+1)); }
warn() { printf '  \033[33mwarn\033[0m %s\n' "$1"; WARN=$((WARN+1)); }
bad()  { printf '  \033[31mFAIL\033[0m %s\n' "$1"; FAIL=$((FAIL+1)); }

probe() { ffprobe -v error -select_streams "$1" -show_entries "$2" -of default=noprint_wrappers=1:nokey=1 "$FILE" 2>/dev/null | head -1; }

CODEC=$(probe v:0 stream=codec_name)
W=$(probe v:0 stream=width); H=$(probe v:0 stream=height)
PIXFMT=$(probe v:0 stream=pix_fmt)
CRANGE=$(probe v:0 stream=color_range)
CSPACE=$(probe v:0 stream=color_space)
CPRIM=$(probe v:0 stream=color_primaries)
CTRC=$(probe v:0 stream=color_transfer)
RFR=$(probe v:0 stream=r_frame_rate)
ACODEC=$(probe a:0 stream=codec_name)
ARATE=$(probe a:0 stream=sample_rate)
DUR=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$FILE" 2>/dev/null)
BR=$(ffprobe -v error -show_entries format=bit_rate -of default=nw=1:nk=1 "$FILE" 2>/dev/null)
FPS=$(python3 -c "n,d='${RFR:-0/1}'.split('/');print(f'{float(n)/float(d):.3f}' if float(d) else '0')" 2>/dev/null)
MBPS=$(python3 -c "print(f'{${BR:-0}/1e6:.2f}')" 2>/dev/null)

echo "$FILE"
echo "  ${CODEC:-?} ${W:-?}x${H:-?} @ ${FPS}fps  ${PIXFMT:-?}  ${DUR:-?}s  ${MBPS} Mbps  audio: ${ACODEC:-none} ${ARATE:-}"
echo

echo "colour tagging"
[ "$PIXFMT" = "yuv420p" ] && ok "pix_fmt yuv420p — every platform wants 4:2:0" \
  || warn "pix_fmt is ${PIXFMT:-unset}, not yuv420p — platforms transcode 4:2:2/10-bit anyway"
if [ -z "$CRANGE" ] || [ "$CRANGE" = "unknown" ]; then
  warn "color_range is UNTAGGED — the player guesses. Tag it explicitly"
else
  ok "color_range tagged $CRANGE"
fi
if [ "$CSPACE" = "bt709" ] && [ "$CPRIM" = "bt709" ] && [ "$CTRC" = "bt709" ]; then
  ok "BT.709 across space/primaries/transfer"
else
  warn "colour tags incomplete: space=${CSPACE:-unset} primaries=${CPRIM:-unset} transfer=${CTRC:-unset} — SDR delivery wants BT.709 on all three"
fi

echo
echo "levels — where BadCode's near-black register actually breaks"
STATS=$(ffmpeg -v error -i "$FILE" -vf "signalstats=stat=brng,metadata=print:file=-" -an -f null - 2>/dev/null)
YMIN=$(echo "$STATS" | awk -F= '/lavfi.signalstats.YMIN/{print $2}' | sort -n | head -1)
YMAX=$(echo "$STATS" | awk -F= '/lavfi.signalstats.YMAX/{print $2}' | sort -n | tail -1)
YLOW=$(echo "$STATS" | awk -F= '/lavfi.signalstats.YLOW/{print $2}' | sort -n | head -1)
if [ -n "$YMIN" ] && [ -n "$YMAX" ]; then
  echo "  luma range in content: YMIN=$YMIN YMAX=$YMAX"
  # 🔴 The trap from brief 19: -color_range is a TAG, not a rescale. Three ways it goes wrong,
  # and the untagged one is the one that actually shows up in BadCode's own renders.
  FULLCONTENT=0
  { [ "$YMIN" -lt 16 ] || [ "$YMAX" -gt 235 ]; } && FULLCONTENT=1
  if [ "$CRANGE" = "pc" ] && [ "$FULLCONTENT" = "0" ]; then
    bad "TAGGED FULL RANGE, CONTENT IS LIMITED — a player will stretch it and clip. Either retag -color_range tv, or convert for real with -vf 'scale=in_range=limited:out_range=full'"
  elif [ "$CRANGE" = "tv" ] && [ "$FULLCONTENT" = "1" ]; then
    bad "TAGGED LIMITED RANGE, CONTENT IS FULL — whites will clip. Fix with: -vf 'scale=in_range=full:out_range=limited' -pix_fmt yuv420p -color_range tv. BOTH halves of that scale filter are required — out_range alone is a silent no-op"
  elif { [ -z "$CRANGE" ] || [ "$CRANGE" = "unknown" ]; } && [ "$FULLCONTENT" = "1" ]; then
    bad "UNTAGGED, AND THE CONTENT IS FULL RANGE ($YMIN–$YMAX) — players default to assuming limited, expand it, and crush the shadows. This is the worst case for a near-black film and it is invisible until you check. Fix with: -vf 'scale=in_range=full:out_range=limited' -pix_fmt yuv420p -color_range tv"
  elif [ -z "$CRANGE" ] || [ "$CRANGE" = "unknown" ]; then
    warn "untagged, but the content is inside 16–235 so a limited-range assumption is harmless. Tag it anyway"
  else
    ok "tag and content agree"
  fi
  [ "$YMIN" -le 1 ] && warn "blacks reach $YMIN — shadow detail is already clipped before the platform re-encodes. Lift the floor a little"
else
  warn "signalstats returned nothing — could not read luma"
fi

BLACK=$(ffmpeg -v info -i "$FILE" -vf "blackdetect=d=0.2:pic_th=0.98:pix_th=0.10" -an -f null - 2>&1 | grep -c black_start)
[ "$BLACK" -gt 0 ] && warn "$BLACK near-black stretch(es) — check the head and tail are intentional" || ok "no unintended black stretches"
FREEZE=$(ffmpeg -v info -i "$FILE" -vf "freezedetect=n=-60dB:d=0.5" -an -f null - 2>&1 | grep -c freeze_start)
[ "$FREEZE" -gt 0 ] && warn "$FREEZE frozen stretch(es) — a stuck frame or a still held too long" || ok "no frozen frames"

echo
echo "audio"
if [ -z "$ACODEC" ]; then
  warn "no audio stream — Premiere usually adds a silent one on export; a genuinely silent upload is a choice, not an accident"
else
  LUFS=$(ffmpeg -v info -i "$FILE" -af ebur128=peak=true -f null - 2>&1 | grep -A4 'Integrated loudness' | awk '/I:/{print $2}' | tail -1)
  TP=$(ffmpeg -v info -i "$FILE" -af ebur128=peak=true -f null - 2>&1 | grep -A2 'True peak' | awk '/Peak:/{print $2}' | tail -1)
  if [ -n "$LUFS" ]; then
    echo "  integrated loudness ${LUFS} LUFS, true peak ${TP:-?} dBFS"
    python3 -c "import sys;sys.exit(0 if abs(float('$LUFS')+14)<=1.5 else 1)" 2>/dev/null \
      && ok "within 1.5 LU of the -14 LUFS platform consensus" \
      || warn "off the -14 LUFS target — platforms normalise, so this mostly costs you dynamics"
    python3 -c "import sys;sys.exit(0 if float('${TP:-0}')<=-1.0 else 1)" 2>/dev/null \
      && ok "true peak leaves headroom for the platform re-encode" \
      || warn "true peak above -1 dBFS — lossy re-encoding will clip it"
  else
    warn "could not measure loudness"
  fi
  [ "${ARATE:-0}" = "48000" ] && ok "48 kHz" || warn "sample rate ${ARATE:-?} — platforms want 48 kHz"
fi

if [ -n "$PLATFORM" ]; then
  echo
  echo "$PLATFORM spec"
  AR=$(python3 -c "print(f'{${W:-0}/${H:-1}:.4f}')" 2>/dev/null)
  vertical() { python3 -c "import sys;sys.exit(0 if abs($AR-0.5625)<0.01 else 1)"; }
  case "$PLATFORM" in
    youtube)
      [ "$CODEC" = "h264" ] && ok "H.264" || warn "codec $CODEC — YouTube wants H.264 High Profile"
      python3 -c "import sys;sys.exit(0 if ${MBPS}>=8 else 1)" && ok "${MBPS} Mbps clears the 1080p 8 Mbps guidance" \
        || warn "${MBPS} Mbps is under YouTube's 8 Mbps 1080p guidance — upload richer, they re-encode anyway"
      ;;
    shorts)
      vertical && ok "9:16" || bad "aspect ${AR} is not 9:16 — Shorts will pillarbox or crop it"
      [ "${H:-0}" -le 1920 ] && [ "${W:-0}" -le 1080 ] && ok "within 1080p" || warn "over 1080p — Shorts caps there"
      python3 -c "import sys;sys.exit(0 if float('${DUR:-0}')<=180 else 1)" && ok "under the 3-minute Shorts limit" \
        || bad "${DUR}s is over the 3-minute Shorts limit"
      ;;
    reels)
      vertical && ok "9:16" || warn "aspect ${AR} — Reels recommends 9:16"
      python3 -c "import sys;sys.exit(0 if ${MBPS}<=25 else 1)" && ok "${MBPS} Mbps under the 25 Mbps VBR ceiling" \
        || bad "${MBPS} Mbps exceeds Reels' 25 Mbps ceiling"
      python3 -c "import sys;sys.exit(0 if 3<=float('${DUR:-0}')<=900 else 1)" && ok "duration inside 3s–15min" \
        || bad "${DUR}s is outside Reels' 3s–15min window"
      ;;
    tiktok)
      # 🔴 Secondary source (Sprout Social), not TikTok's own spec page. TikTok re-transcodes everything.
      vertical && ok "9:16" || warn "aspect ${AR} — TikTok expects 1080x1920"
      python3 -c "import sys;sys.exit(0 if 23<=float('${FPS:-0}')<=60 else 1)" && ok "${FPS}fps inside 23–60" \
        || warn "${FPS}fps outside the 23–60 range"
      echo "  note: this spec is secondary-sourced; TikTok re-transcodes everything server-side"
      ;;
    *) echo "  unknown platform '$PLATFORM' — try youtube, shorts, reels or tiktok" ;;
  esac
fi

echo
printf '%d ok, %d warn, %d fail\n' "$PASS" "$WARN" "$FAIL"
[ "$FAIL" -gt 0 ] && exit 1 || exit 0
