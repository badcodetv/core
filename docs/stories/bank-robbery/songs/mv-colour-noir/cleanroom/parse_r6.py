"""Parse round 6 writers' output (r1-r3, x1, b1, a1) into prompts-r6.json."""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
out = {}
for f in ["r1", "r2", "r3", "x1", "b1", "a1"]:
    for m in re.finditer(r"=== SHOT (\S+) ===\n(.*?)\nMOTION: (.*?)\nSECONDS: (\d+)\nWHY: (.*?)(?=\n+=== SHOT|\Z)", (HERE / f"{f}.md").read_text(), re.S):
        out[m[1]] = {"writer": f, "prompt": m[2].strip(), "motion": m[3].strip(), "seconds": int(m[4]), "why": m[5].strip()}
json.dump(out, open(HERE / "prompts-r6.json", "w"), indent=1, ensure_ascii=False)
print(len(out), list(out))
