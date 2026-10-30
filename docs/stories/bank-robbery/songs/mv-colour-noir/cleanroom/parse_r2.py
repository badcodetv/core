"""s1..4.md -> prompts-r2.json and v1..4.md -> clips.json. `run` is the writer's prompt, unchanged, plus Thanks."""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
stills, clips = {}, {}
for n in range(1, 5):
    for key, body in re.findall(r"=== SHOT (\w+) ===\n(.*?)(?==== SHOT|\Z)", (HERE / f"s{n}.md").read_text(), re.S):
        prompt, why = re.match(r"(.*?)\nWHY:\s*(.*)", body.strip(), re.S).groups()
        stills[key] = {"prompt": prompt.strip(), "why": why.strip(), "run": prompt.strip() + "\n\nThanks."}
    for key, body in re.findall(r"=== SHOT (\w+) ===\n(.*?)(?==== SHOT|\Z)", (HERE / f"v{n}.md").read_text(), re.S):
        prompt, ends, why = re.match(r"(.*?)\nENDS ON:\s*(.*?)\nWHY:\s*(.*)", body.strip(), re.S).groups()
        clips[key] = {"motion": prompt.strip(), "ends_on": ends.strip(), "why": why.strip(), "run": prompt.strip() + "\n\nThanks."}
(HERE / "prompts-r2.json").write_text(json.dumps(stills, indent=1, ensure_ascii=False))
(HERE / "clips.json").write_text(json.dumps(clips, indent=1, ensure_ascii=False))
print(len(stills), list(stills), len(clips), list(clips))
