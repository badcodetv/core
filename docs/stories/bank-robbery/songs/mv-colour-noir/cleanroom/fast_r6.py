"""Pre-render every row of cut-r6.json whose speed is not 1 (frame sampling, no interpolation), and point the row at the result.
The research says generate at a speed the model holds and speed up 130-200% in the edit. Run after cut_r6.py."""
import json, os, pathlib, subprocess
HERE = pathlib.Path(__file__).parent
FAST = "/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/noir/r6/fast"
os.makedirs(FAST, exist_ok=True)
rows = json.load(open(HERE / "cut-r6.json"))
for r in rows:
    if r["speed"] == 1: continue
    out = f"{FAST}/{r['n']:03d}-{r['clip']}.mp4"
    dur = r["end"] - r["start"]
    if not os.path.exists(out):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(r["inPoint"]), "-t", str(dur * r["speed"] + .1), "-i", r["src"], "-an",
                        "-vf", f"setpts=PTS/{r['speed']},fps=24", "-c:v", "libx264", "-crf", "14", "-preset", "fast", "-pix_fmt", "yuv420p", out], check=True)
    r["file"] = out; r["inPoint"] = 0
    print(r["n"], r["clip"], round(dur, 2))
json.dump(rows, open(HERE / "cut-r6.json", "w"), indent=0)
