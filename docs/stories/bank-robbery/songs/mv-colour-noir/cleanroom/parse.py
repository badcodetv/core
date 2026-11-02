"""w1..8.md -> prompts.json. `run` is the writer's prompt, unchanged, plus Thanks."""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
KEYS = {1: "den", 2: "bridge", 3: "chase", 4: "pov", 5: "safe", 6: "mask", 7: "city", 8: "rods"}
out = {}
for n, key in KEYS.items():
    for num, body in re.findall(r"=== SHOT (\d+) ===\n(.*?)(?==== SHOT|\Z)", (HERE / f"w{n}.md").read_text(), re.S):
        m = re.match(r"(.*?)\nWAY OUT:\s*(.*?)\nWHY:\s*(.*)", body.strip(), re.S)
        prompt, way, why = (s.strip() for s in m.groups())
        out[f"{key}{num}"] = {"beat": key, "prompt": prompt, "way_out": way, "why": why, "run": prompt + "\n\nThanks."}
(HERE / "prompts.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(len(out), {k: len(v["prompt"].split()) for k, v in out.items()})
