"""Parse round 5 writers' output (l1..l4, o1) into prompts-r5.json."""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
out = {}
for f in ["l1", "l2", "l3", "l4", "o1"]:
    for m in re.finditer(r"=== SHOT (\S+) ===\n(.*?)\nMOTION: (.*?)\nSECONDS: (\d+)\nWHY: (.*?)(?=\n=== SHOT|\Z)", (HERE / f"{f}.md").read_text(), re.S):
        out[m[1]] = {"writer": f, "prompt": m[2].strip(), "motion": m[3].strip(), "seconds": int(m[4]), "why": m[5].strip()}
json.dump(out, open(HERE / "prompts-r5.json", "w"), indent=1, ensure_ascii=False)
print(len(out), list(out))
