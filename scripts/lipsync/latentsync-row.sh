#!/usr/bin/env bash
# latentsync-row.sh <dir> <name>...   (2026-11-06, GPOM scene A round 19, Kai at3436)
# Redraws the mouth of each <dir>/<name>-in.mp4 to <dir>/<name>-voice.wav with LatentSync 1.6 (local GPU),
# writing <dir>/<name>-ls.mp4 and <dir>/gpu-times.txt. Run by a person (it executes the downloaded LatentSync code):
#   ! bash scripts/lipsync/latentsync-row.sh /mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/video/latentsync-r19 6-0 7d-0 7-0 7d-1 7-2
set -euo pipefail
LS=$HOME/.cache/badcode-latentsync/LatentSync
dir=$1; shift
export TMPDIR=$HOME/.cache/pw-tmp; mkdir -p "$TMPDIR"
cd "$LS"
for n in "$@"; do
  s=$(date +%s)
  .venv/bin/python -m scripts.inference --unet_config_path configs/unet/stage2_512.yaml \
    --inference_ckpt_path checkpoints/latentsync_unet.pt --inference_steps 20 --guidance_scale 1.5 --enable_deepcache \
    --video_path "$dir/$n-in.mp4" --audio_path "$dir/$n-voice.wav" --video_out_path "$dir/$n-ls.mp4" \
    --temp_dir "$TMPDIR/ls-$n" 2>&1 | grep -v -i warning | tail -3
  echo "$n $(( $(date +%s) - s ))s" | tee -a "$dir/gpu-times.txt"
done
