"""Parse the sealed writers' wN.md into prompts.json and the scene's moodboard.json rows."""
import json, pathlib, re

HERE = pathlib.Path(__file__).parent
WRITERS = {"w1": "rough", "w2": "rough", "w3": "posh", "w4": "posh"}


def main():
    prompts, rows, missing = {}, [], []
    for w, beat in WRITERS.items():
        f = HERE / f"{w}.md"
        if not f.exists():
            missing.append(w); continue
        parts = re.split(r"^=== DESIGN (\S+) ===\s*$", f.read_text(), flags=re.M)
        for did, body in zip(parts[1::2], parts[2::2]):
            body = body.strip()
            name = re.match(r"NAME:\s*(.+)", body)
            body = re.sub(r"^NAME:.*\n", "", body).strip()
            m = re.split(r"^WHY:\s*", body, flags=re.M)
            prompt, why = m[0].strip(), (m[1].strip() if len(m) > 1 else "")
            nm = name.group(1).strip() if name else did
            prompts[did] = {"writer": w, "beat": beat, "name": nm, "prompt": prompt, "why": why,
                            "run": prompt + "\n\nThanks."}
            for k in "ab":
                rows.append([beat, f"{did}-{k}", f"{did} · {nm} — {why}", prompt])
    json.dump(prompts, open(HERE / "prompts.json", "w"), indent=1, ensure_ascii=False)
    json.dump(rows, open(HERE.parent / "moodboard.json", "w"), indent=1, ensure_ascii=False)
    print(len(prompts), "prompts; missing writers:", missing)


if __name__ == "__main__":
    main()
