"""clip-wN.md → clips.json and ../video-jobs.json (one 'extra' job per still: key <shot>-<take>, still <shot>r2-<take>)."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import FAMILIES
clips, jobs, missing = {}, [], []
for w in FAMILIES:
    f = HERE / f"clip-{w}.md"
    if not f.exists(): missing.append(w); continue
    parts = re.split(r"^=== CLIP (\S+) ===\s*$", f.read_text(), flags=re.M)
    for sid, body in zip(parts[1::2], parts[2::2]):
        m = re.split(r"^(ENDS_ON|WHY):\s*", body.strip(), flags=re.M)
        motion = m[0].strip(); d = dict(zip(m[1::2], [x.strip() for x in m[2::2]]))
        clips[sid] = {"writer": w, "motion": motion, "ends_on": d.get("ENDS_ON", ""), "why": d.get("WHY", ""), "run": motion + "\n\nThanks."}
moodboard = pathlib.Path(json.load(open(HERE.parent / "scene.json"))["media"]) / "moodboard"
for sid, c in clips.items():
    for t in "ab":
        if (moodboard / f"{sid}r2-{t}.jpg").exists():
            jobs.append({"key": f"{sid}-{t}", "n": 0, "still": f"{sid}r2-{t}", "motion": c["run"], "character": None, "why": f"mv-gang clip, writer {c['writer']}"})
json.dump(clips, open(HERE / "clips.json", "w"), indent=1, ensure_ascii=False)
json.dump({"extra": jobs}, open(HERE.parent / "video-jobs.json", "w"), indent=1, ensure_ascii=False)
print(len(clips), "clips;", len(jobs), "jobs; missing:", missing)
