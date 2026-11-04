"""Parse round-3 writers (r3/wN.md) into cleanroom/prompts-r3.json and the scene's moodboard.json rows.
  python3 parse.py [w1 w2 …]   (default: every writer whose file exists)"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import FAMILIES
BEAT = {"h": "singer", "k": "action", "g": "gestures"}
ws = sys.argv[1:] or [w for w in FAMILIES if (HERE / f"{w}.md").exists()]
meta = {s[0]: (w, *s[1:]) for w, (_, shots) in FAMILIES.items() for s in shots}
out = HERE.parent / "prompts-r3.json"
prompts = json.loads(out.read_text()) if out.exists() else {}
rows = []
for w in ws:
    parts = re.split(r"^=== SHOT (\S+) ===\s*$", (HERE / f"{w}.md").read_text(), flags=re.M)
    for sid, body in zip(parts[1::2], parts[2::2]):
        m = re.split(r"^WHY:\s*", body.strip(), flags=re.M)
        prompt, why = m[0].strip(), (m[1].strip() if len(m) > 1 else "")
        _, t, line, pic, rap = meta[sid]
        prompts[sid] = {"writer": w, "t": t, "line": line, "beat": BEAT[sid[0]], "prompt": prompt, "why": why, "run": prompt + "\n\nThanks."}
        for k in "ab":
            rows.append([BEAT[sid[0]], f"{sid}r3-{k}", f"{sid} · {t} · “{line}”", prompt])
out.write_text(json.dumps(prompts, indent=1, ensure_ascii=False))
(HERE.parents[1] / "moodboard.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
print(len(prompts), "prompts,", len(rows), "board rows; missing:", sorted(s for s in meta if meta[s][0] in ws and s not in prompts))
