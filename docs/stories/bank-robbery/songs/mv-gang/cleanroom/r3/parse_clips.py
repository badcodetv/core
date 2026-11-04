"""r3/clip-cwN.md -> r3/clips.json, and adds one job per picked still to ../../video-jobs.json 'extra' (key <shot>-<take>, still <shot>r3-<take>)."""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
SCENE = HERE.parents[1]
clips = {}
for f in sorted(HERE.glob("clip-cw*.md")):
    parts = re.split(r"^=== CLIP (\S+) ===\s*$", f.read_text(), flags=re.M)
    for key, body in zip(parts[1::2], parts[2::2]):
        m = re.split(r"^(ENDS_ON|WHY):\s*", body.strip(), flags=re.M)
        d = dict(zip(m[1::2], [x.strip() for x in m[2::2]]))
        clips[key] = {"writer": f.stem[5:], "motion": m[0].strip(), "ends_on": d.get("ENDS_ON", ""), "why": d.get("WHY", ""), "run": m[0].strip() + "\n\nThanks."}
(HERE / "clips.json").write_text(json.dumps(clips, indent=1, ensure_ascii=False))
vj = json.load(open(SCENE / "video-jobs.json"))
have = {j["key"] for j in vj["extra"]}
for key, c in clips.items():
    sid, t = key.split("-")
    job = {"key": key, "n": 0, "still": f"{sid}r3-{t}", "motion": c["run"], "character": None, "why": f"mv-gang r3 action clip, writer {c['writer']}"}
    vj["extra"] = [j for j in vj["extra"] if j["key"] != key] + [job]
json.dump(vj, open(SCENE / "video-jobs.json", "w"), indent=1, ensure_ascii=False)
print(len(clips), "clips:", " ".join(clips))
