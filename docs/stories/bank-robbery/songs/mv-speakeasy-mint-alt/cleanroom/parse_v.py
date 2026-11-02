"""Parse the sealed video writers' v1..v8.md into vid-prompts.json {scene: {motion, handoff, why}}."""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
out = {}
for f in sorted(HERE.glob("v[1-8].md")):
    for m in re.finditer(r"=== SCENE (\d+) ===\s*(.*?)\nHANDOFF:\s*(.*?)\nWHY:\s*(.*?)(?=\n=== SCENE|\Z)", f.read_text(), re.S):
        out[int(m[1])] = {"motion": m[2].strip(), "handoff": m[3].strip(), "why": m[4].strip(), "from": f.name}
json.dump({str(k): out[k] for k in sorted(out)}, open(HERE / "vid-prompts.json", "w"), indent=1, ensure_ascii=False)
print(sorted(out), "missing:", [n for n in range(1, 34) if n not in out])
