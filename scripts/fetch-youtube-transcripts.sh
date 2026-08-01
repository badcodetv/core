#!/usr/bin/env bash
#
# fetch-youtube-transcripts.sh — bulk-harvest auto-caption transcripts from a
# YouTube channel into flat text files, for research/distillation.
#
# Built for the Suno research pass that fed docs/suno-gpt/ (the ChillPanic
# channel), but it is generic: point it at any channel with a keyword filter.
#
# Output is RESEARCH INPUT, not publishable material. Write it somewhere
# scratch — do not commit harvested transcripts to this repo.
#
# Usage:
#   scripts/fetch-youtube-transcripts.sh -c <channel-url> -o <outdir> [-f <regex>] [-x <regex>] [-j N]
#
# Options:
#   -c  Channel/playlist URL (required), e.g.
#         https://www.youtube.com/channel/UCj83I0PrbdTDmoUXBosTyXg/videos
#         https://www.youtube.com/@SomeHandle/videos
#   -o  Output directory (required). Creates <outdir>/{txt,vtt} + index files.
#   -f  Include filter: case-insensitive ERE matched against the title.
#       Omit to take every video on the channel.
#   -x  Exclude filter: case-insensitive ERE; applied after -f.
#   -j  Parallel workers (default 3). Keep it modest — YouTube rate-limits.
#   -l  List only: write the filtered index and exit without downloading.
#
# Example (what produced the Suno knowledge base):
#   scripts/fetch-youtube-transcripts.sh \
#     -c https://www.youtube.com/channel/UCj83I0PrbdTDmoUXBosTyXg/videos \
#     -o /tmp/suno-research \
#     -f 'suno|udio|ai music|ai song|prompt|stems|lyria' \
#     -x 'official (lyric|music|visualizer|audio)|\(Official'
#
# Requires yt-dlp (pip install yt-dlp).

set -uo pipefail

CHANNEL="" OUTDIR="" INCLUDE="" EXCLUDE="" JOBS=3 LIST_ONLY=0

while getopts "c:o:f:x:j:lh" opt; do
  case $opt in
    c) CHANNEL=$OPTARG ;;
    o) OUTDIR=$OPTARG ;;
    f) INCLUDE=$OPTARG ;;
    x) EXCLUDE=$OPTARG ;;
    j) JOBS=$OPTARG ;;
    l) LIST_ONLY=1 ;;
    h) sed -n '2,40p' "$0"; exit 0 ;;
    *) echo "See -h for usage." >&2; exit 2 ;;
  esac
done

[ -z "$CHANNEL" ] && { echo "error: -c <channel-url> is required (-h for help)" >&2; exit 2; }
[ -z "$OUTDIR" ]  && { echo "error: -o <outdir> is required (-h for help)" >&2; exit 2; }

YTDLP=$(command -v yt-dlp || echo "$HOME/.local/bin/yt-dlp")
[ -x "$YTDLP" ] || { echo "error: yt-dlp not found. pip install yt-dlp" >&2; exit 1; }

mkdir -p "$OUTDIR/txt" "$OUTDIR/vtt"
ALL="$OUTDIR/all-videos.txt"
SEL="$OUTDIR/selected-videos.txt"

# ---- 1. Enumerate the channel (flat, no per-video page fetches) -------------
if [ ! -s "$ALL" ]; then
  echo "==> Enumerating $CHANNEL"
  "$YTDLP" --flat-playlist --print "%(id)s|%(title)s|%(duration)s" \
           --no-warnings "$CHANNEL" > "$ALL" 2>/dev/null
fi
echo "==> $(wc -l < "$ALL") videos on channel"

# ---- 2. Filter by title ----------------------------------------------------
cp "$ALL" "$SEL"
[ -n "$INCLUDE" ] && { grep -iE "$INCLUDE" "$SEL" > "$SEL.tmp" || true; mv "$SEL.tmp" "$SEL"; }
[ -n "$EXCLUDE" ] && { grep -viE "$EXCLUDE" "$SEL" > "$SEL.tmp" || true; mv "$SEL.tmp" "$SEL"; }
echo "==> $(wc -l < "$SEL") selected -> $SEL"
[ "$LIST_ONLY" -eq 1 ] && exit 0

# ---- 3. Fetch captions + flatten VTT -> text -------------------------------
# One worker function, fanned out over N shards of the selection.
fetch_shard() {
  local list=$1
  while IFS='|' read -r id title dur; do
    [ -z "${id:-}" ] && continue
    [ -s "$OUTDIR/txt/${id}.txt" ] && continue

    "$YTDLP" --skip-download --write-auto-subs --sub-langs "en.*" --sub-format vtt \
             --no-warnings --quiet --retries 3 --sleep-requests 1 \
             -o "$OUTDIR/vtt/%(id)s.%(ext)s" \
             "https://www.youtube.com/watch?v=${id}" >/dev/null 2>&1

    local src
    src=$(ls "$OUTDIR"/vtt/"${id}".*.vtt 2>/dev/null | head -1)
    if [ -n "$src" ]; then
      {
        printf 'TITLE: %s\nVIDEO_ID: %s\nURL: https://www.youtube.com/watch?v=%s\nDURATION_S: %s\n\n' \
          "$title" "$id" "$id" "$dur"
        # drop cue timings, WEBVTT headers and inline karaoke tags, then collapse
        # the duplicated rolling-caption lines auto-subs are full of
        sed -e '/-->/d' -e '/^WEBVTT/d' -e '/^Kind:/d' -e '/^Language:/d' \
            -e 's/<[^>]*>//g' -e '/^[[:space:]]*$/d' "$src" \
          | awk '!seen[$0]++' | tr '\n' ' ' | fold -s -w 110
      } > "$OUTDIR/txt/${id}.txt"
      echo "ok   $id  $title"
    else
      echo "NOSUB $id  $title" | tee -a "$OUTDIR/failures.log"
    fi
  done < "$list"
}
export -f fetch_shard
export YTDLP OUTDIR

rm -f "$OUTDIR"/shard-*
split -n "l/$JOBS" "$SEL" "$OUTDIR/shard-"
for shard in "$OUTDIR"/shard-*; do
  fetch_shard "$shard" &
done
wait
rm -f "$OUTDIR"/shard-*

echo "==> done: $(ls "$OUTDIR"/txt/*.txt 2>/dev/null | wc -l) transcripts in $OUTDIR/txt"
[ -s "$OUTDIR/failures.log" ] && echo "==> $(wc -l < "$OUTDIR/failures.log") without captions (see failures.log)"
exit 0
