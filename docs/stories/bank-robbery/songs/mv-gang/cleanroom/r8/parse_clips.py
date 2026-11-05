"""r8/clip-*.md -> r8/clips.json + jobs in ../../video-jobs.json 'extra'. Stills: performers from STILL below; y shots from <id>r8-<take>."""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent; SCENE = HERE.parents[1]
STILL = {"y01-b": "y01r8-b", "y02-a": "y02r8-a", "y03-a": "y03r8-a", "y04-a": "y04r8-a", "y05-a": "y05r8-a", "y06-a": "y06r8-a", "z02y-b": "z02r7-b", "p03y-b": "p03r6-b", "z06y-b": "z06r7-b", "g08y-b": "g08r5-b", "v05y-a": "v05r5-a"}
DROP = {"z02y-a", "q07y-b"}  # z02 take a's triangle sat off-centre; q07's masks are wrong in both takes (dropped from the cut)
clips = {}
for f in sorted(HERE.glob("clip-*.md")):
    parts = re.split(r"^=== CLIP (\S+) ===\s*$", f.read_text(), flags=re.M)
    for key, body in zip(parts[1::2], parts[2::2]):
        if key in DROP: continue
        m = re.split(r"^(ENDS_ON|WHY):\s*", body.strip(), flags=re.M)
        still = STILL.get(key) or key.replace("-", "r8-")
        clips[key] = {"writer": f.stem[5:], "still": still, "motion": m[0].strip(), "run": m[0].strip() + "\n\nThanks."}
(HERE / "clips.json").write_text(json.dumps(clips, indent=1, ensure_ascii=False))
vj = json.load(open(SCENE / "video-jobs.json"))
for key, c in clips.items():
    vj["extra"] = [j for j in vj["extra"] if j["key"] != key] + [{"key": key, "n": 0, "still": c["still"], "motion": c["run"], "character": None, "why": f"mv-gang r8 mask fix, writer {c['writer']}"}]
json.dump(vj, open(SCENE / "video-jobs.json", "w"), indent=1, ensure_ascii=False)
print(sorted(clips))
