"""r6/clip-cwN.md -> r6/clips.json, and one job per shot in ../../video-jobs.json 'extra'."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).parent
SCENE = HERE.parents[1]
sys.path.insert(0, str(HERE))
from make_clip_briefs import JOBS
still = dict(JOBS)
clips = {}
for f in sorted(HERE.glob("clip-cw*.md")):
    parts = re.split(r"^=== CLIP (\S+) ===\s*$", f.read_text(), flags=re.M)
    for key, body in zip(parts[1::2], parts[2::2]):
        m = re.split(r"^(ENDS_ON|WHY):\s*", body.strip(), flags=re.M)
        d = dict(zip(m[1::2], [x.strip() for x in m[2::2]]))
        clips[key] = {"writer": f.stem[5:], "still": still[key], "motion": m[0].strip(), "ends_on": d.get("ENDS_ON", ""), "why": d.get("WHY", ""), "run": m[0].strip() + "\n\nThanks."}
(HERE / "clips.json").write_text(json.dumps(clips, indent=1, ensure_ascii=False))
vj = json.load(open(SCENE / "video-jobs.json"))
for key, c in clips.items():
    job = {"key": key, "n": 0, "still": c["still"], "motion": c["run"], "character": None, "why": f"mv-gang r6 rap-to-camera clip, writer {c['writer']}"}
    vj["extra"] = [j for j in vj["extra"] if j["key"] != key] + [job]
json.dump(vj, open(SCENE / "video-jobs.json", "w"), indent=1, ensure_ascii=False)
print(len(clips), "clips | missing:", [k for k in still if k not in clips])
