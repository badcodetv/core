"""Redraw mouths with LatentSync 1.5, loading the model once for a whole list of clips.

jobs.json: [{"id": "l01", "video": "/abs/in.mp4", "audio": "/abs/in.wav", "out": "/abs/out.mp4"}, ...]
A job whose out file exists is skipped, so a killed run restarts where it stopped. A failed
clip (usually no face found) is logged and the run carries on. Results go to <jobs>.log.jsonl.

Run it from the LatentSync checkout, under a memory cap (it needs about 8.4 GB of RAM):

  cd ~/.cache/badcode-latentsync
  sudo systemd-run --scope -q --uid=1000 --gid=1000 -E HOME=$HOME -E PATH=/usr/local/bin:/usr/bin:/bin \
    -p MemoryMax=8500M -p MemorySwapMax=16G --working-directory=$PWD \
    $PWD/.venv/bin/python /path/to/latentsync-batch.py jobs.json
"""
import json
import os
import shutil
import sys
import time
import traceback

import torch
from accelerate.utils import set_seed
from diffusers import AutoencoderKL, DDIMScheduler
from DeepCache import DeepCacheSDHelper
from omegaconf import OmegaConf

sys.path.insert(0, os.getcwd())
from latentsync.models.unet import UNet3DConditionModel  # noqa: E402
from latentsync.pipelines.lipsync_pipeline import LipsyncPipeline  # noqa: E402
from latentsync.whisper.audio2feature import Audio2Feature  # noqa: E402

jobs_path = sys.argv[1]
jobs = json.load(open(jobs_path))
todo = [j for j in jobs if not os.path.exists(j["out"])]
print(f"{len(jobs)} jobs, {len(todo)} to do", flush=True)
if not todo:
    sys.exit(0)

config = OmegaConf.load("configs/unet/stage2.yaml")
dtype = torch.float16 if torch.cuda.get_device_capability()[0] > 7 else torch.float32
audio_encoder = Audio2Feature(
    model_path="checkpoints/whisper/tiny.pt",
    device="cuda",
    num_frames=config.data.num_frames,
    audio_feat_length=config.data.audio_feat_length,
)
vae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse", torch_dtype=dtype)
vae.config.scaling_factor = 0.18215
vae.config.shift_factor = 0
unet, _ = UNet3DConditionModel.from_pretrained(
    OmegaConf.to_container(config.model), "checkpoints/latentsync_unet.pt", device="cpu"
)
unet = unet.to(dtype=dtype)
pipeline = LipsyncPipeline(
    vae=vae, audio_encoder=audio_encoder, unet=unet, scheduler=DDIMScheduler.from_pretrained("configs")
).to("cuda")
helper = DeepCacheSDHelper(pipe=pipeline)
helper.set_params(cache_interval=3, cache_branch_id=0)
helper.enable()
print("model loaded", flush=True)

with open(jobs_path + ".log.jsonl", "a") as log:
    for job in todo:
        started = time.time()
        temp_dir = f"temp-{job['id']}"
        # The pipeline builds an unquoted ffmpeg command, so its output path must have no spaces.
        partial = os.path.abspath(f"part-{job['id']}.mp4")
        row = {"id": job["id"]}
        try:
            set_seed(job.get("seed", 1247))
            pipeline(
                video_path=job["video"],
                audio_path=job["audio"],
                video_out_path=partial,
                num_frames=config.data.num_frames,
                num_inference_steps=job.get("steps", 20),
                guidance_scale=job.get("guidance", 1.5),
                weight_dtype=dtype,
                width=config.data.resolution,
                height=config.data.resolution,
                mask_image_path=config.data.mask_image_path,
                temp_dir=temp_dir,
            )
            shutil.move(partial, job["out"])
            row["ok"] = True
        except Exception as error:
            traceback.print_exc()
            row.update(ok=False, error=str(error)[:300])
        shutil.rmtree(temp_dir, ignore_errors=True)
        torch.cuda.empty_cache()
        row["seconds"] = round(time.time() - started, 1)
        print(row, flush=True)
        log.write(json.dumps(row) + "\n")
        log.flush()
