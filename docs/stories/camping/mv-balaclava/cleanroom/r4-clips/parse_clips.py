"""w1-w4.md → clips.json and ../../video-jobs.json (one 'extra' job per picked still: key <shot>, still <shot>r3-<pick>)."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from make_clip_briefs import PICK, WRITERS
clips, jobs = {}, []
for w in WRITERS:
    parts = re.split(r"^=== CLIP (\S+) ===\s*$", (HERE / f"{w}.md").read_text(), flags=re.M)
    for sid, body in zip(parts[1::2], parts[2::2]):
        m = re.split(r"^(ENDS_ON|WHY):\s*", body.strip(), flags=re.M)
        motion = m[0].strip(); d = dict(zip(m[1::2], [x.strip() for x in m[2::2]]))
        clips[sid] = {"writer": w, "motion": motion, "ends_on": d.get("ENDS_ON", ""), "why": d.get("WHY", ""), "run": motion + "\n\nThanks."}
for sid in PICK:
    c = clips[sid]
    jobs.append({"key": sid, "n": 0, "still": f"{sid}r3-{PICK[sid]}", "motion": c["run"], "character": None,
                 "why": f"balaclava rap clip r4, writer {c['writer']}"})
json.dump(clips, open(HERE / "clips.json", "w"), indent=1, ensure_ascii=False)
json.dump({"extra": jobs}, open(HERE.parent.parent / "video-jobs.json", "w"), indent=1, ensure_ascii=False)
print(len(clips), "clips;", len(jobs), "jobs")
