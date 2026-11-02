"""Round 5 placement. Picks + mouth spans read from each take's strip and own audio; song times are Whisper's word times (loose), mouth placed 0.08 s
before the sung word so the voice lands just after it opens. The song can't stretch, so the picture is retimed by frame sampling, no interpolation (departure
from lip-sync-dub's "don't slow the picture", say so), capped at 0.667-1.25x. Where the mouth finishes more than 0.3 s before the phrase ends, the rest is a
cutaway. Writes plan-r5.json and retimed clips: python3 place_r5.py <lipsync video dir> <fit dir>"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).parent
VIDEO, FIT = sys.argv[1], pathlib.Path(sys.argv[2])
FIT.mkdir(parents=True, exist_ok=True)
LEAD, CAP_SLOW, CAP_FAST, MIN_CUT = 0.08, 0.667, 1.25, 0.3
# id: take, mouth on, mouth off, song word start, song phrase end
PICKS = {
    "l01": ("a", 1.40, 3.00, 66.50, 70.00), "l02": ("a", 1.67, 4.25, 70.20, 74.30),
    "l03": ("a", 1.22, 3.00, 140.34, 143.50), "l04": ("a", 1.33, 4.42, 143.72, 147.70),
    "l05": ("b", 0.62, 2.96, 154.52, 158.10), "l06": ("a", 1.25, 3.12, 158.26, 162.20),
    "c1": ("a", 1.10, 3.12, 177.04, 179.90), "c2": ("a", 0.62, 3.44, 180.04, 183.20), "c3": ("a", 0.70, 3.18, 183.34, 186.00),
    "c4": ("a", 1.70, 3.42, 186.08, 188.00), "c5": ("a", 1.84, 5.42, 188.12, 191.15),
    "e1": ("a", 0.70, 2.62, 199.76, 202.35), "e2": ("a", 0.76, 3.08, 202.40, 205.70),
    "e3": ("a", 1.06, 4.60, 206.10, 209.40), "e4": ("a", 1.18, 4.30, 209.50, 213.15),
    "f1": ("a", 0.83, 2.40, 220.48, 222.30), "f2": ("a", 0.54, 2.70, 222.38, 225.50), "f3": ("b", 0.70, 2.15, 225.58, 227.75),
    "f4": ("a", 0.74, 3.30, 227.80, 230.15), "f5": ("a", 1.00, 2.60, 230.18, 231.90), "f6": ("a", 1.46, 4.54, 231.92, 235.05),
    "f7": ("a", 0.60, 2.62, 235.12, 238.25), "f8": ("a", 0.75, 4.10, 238.32, 241.95),
}
BLOCKS = [(["l01", "l02"], 76.38), (["l03", "l04"], 147.92), (["l05", "l06"], 162.33), (["c1", "c2", "c3", "c4", "c5"], 191.21),
          (["e1", "e2", "e3", "e4"], 213.17), (["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"], 242.0)]
overrides = json.load(open(HERE / "picks-r5-overrides.json")) if (HERE / "picks-r5-overrides.json").exists() else {}
PICKS.update({k: tuple(v) for k, v in overrides.items()})
plan = []
for ids, block_end in BLOCKS:
    for n, pid in enumerate(ids):
        tag, on, off, word, end = PICKS[pid]
        if tag == "?": raise SystemExit(f"no take for {pid}")
        speed = max(CAP_SLOW, min(CAP_FAST, (off - on) / max(end - word, .1)))
        src = f"{VIDEO}/{pid}-{tag}.mp4"
        dst = FIT / f"{pid}-{tag}-fit.mp4"
        if not dst.exists():
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-an", "-vf", f"setpts=PTS/{speed:.4f},fps=24", "-c:v", "libx264", "-crf", "12", "-preset", "slow", "-pix_fmt", "yuv420p", str(dst)], check=True)
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(dst)], capture_output=True, text=True).stdout)
        mouth_at = word - LEAD
        clip_zero = mouth_at - on / speed  # timeline time of the fit file's first frame
        next_word = PICKS[ids[n + 1]][3] - LEAD if n + 1 < len(ids) else block_end
        mouth_end = clip_zero + off / speed
        slot_start = max(clip_zero, word - LEAD - .1)
        cut = None
        slot_end = min(next_word, clip_zero + dur)
        if next_word - mouth_end > MIN_CUT:
            slot_end = round(mouth_end + .1, 3)
            cut = [slot_end, round(next_word, 3)]
        plan.append(dict(id=pid, take=tag, file=str(dst), speed=round(speed, 3), start=round(slot_start, 3), end=round(slot_end, 3), inPoint=round(slot_start - clip_zero, 3),
                         mouth_at=round(mouth_at, 3), mouth_end=round(mouth_end, 3), song_end=end, cutaway=cut))
json.dump(plan, open(HERE / "plan-r5.json", "w"), indent=1)
for p in plan:
    print(p["id"], p["take"], "x%.2f" % p["speed"], p["start"], p["end"], "in", p["inPoint"], "mouth", p["mouth_at"], p["mouth_end"], "song_end", p["song_end"], "cut", p["cutaway"])
