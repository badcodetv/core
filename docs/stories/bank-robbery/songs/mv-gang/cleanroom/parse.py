"""Parse the sealed writers' wN.md into prompts.json and the scene's moodboard.json rows."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import FAMILIES


def beat(sid):
    n = int(sid[1:])
    return {"a": "intro", "c": "chorus", "e": "break", "f": "verse5", "x": "action"}.get(sid[0]) or (
        "verse1" if sid[0] == "v" and n <= 9 else "verse2" if sid[0] == "v" and n <= 13 else
        "verse4" if sid[0] == "v" else "verse3" if n <= 8 else "verse4")


def main(r=""):
    meta = {s[0]: (w, *s[1:]) for w, (_, shots) in FAMILIES.items() for s in shots}
    prompts, rows, missing = {}, [], []
    for w in FAMILIES:
        f = HERE / f"{w}{r}.md"
        if not f.exists():
            missing.append(w); continue
        parts = re.split(r"^=== SHOT (\S+) ===\s*$", f.read_text(), flags=re.M)
        for sid, body in zip(parts[1::2], parts[2::2]):
            m = re.split(r"^WHY:\s*", body.strip(), flags=re.M)
            prompt, why = m[0].strip(), (m[1].strip() if len(m) > 1 else "")
            w_, t, line, pic, rap = meta[sid]
            prompts[sid] = {"writer": w, "t": t, "line": line, "beat": beat(sid), "prompt": prompt,
                            "why": why, "run": prompt + "\n\nThanks."}
            look = f"{t} · “{line}”"
            for k in "ab":
                rows.append([beat(sid), f"{sid}{r.replace('-', '')}-{k}", look, prompt])
    json.dump(prompts, open(HERE / f"prompts{r}.json", "w"), indent=1, ensure_ascii=False)
    json.dump(rows, open(HERE.parent / "moodboard.json", "w"), indent=1, ensure_ascii=False)
    print(len(prompts), "prompts;", "missing writers:", missing, "; ids not written:",
          sorted(set(meta) - set(prompts)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "")
