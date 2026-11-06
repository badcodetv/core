#!/usr/bin/env python3
"""Build the vibe desk (https://claude.ai/artifact/FVp78gm6kSrWyVVj3NLpCA).

Reads, from git:
  - the ten minister briefs, docs/government/ministers/NN-<post>.md (title, post key,
    Temperament, Guards against, Sounds like);
  - every draft post, docs/government/statements/<date>/<post>.md, from origin/main and,
    when a government PR is open, from its branch too (marked "in the open PR": what goes
    out next).
and writes docs/government/vibe/index.html from template.html. Then republish:

    python3 scripts/government/vibe-page/build.py [--no-fetch]

Nothing people type lives in the page source: per-post notes are in the artifact's db
(`notes/<date>_<post>`), per-minister dials in `dials/<post>`, applied changes in `history`.
The procedure is the government-vibe skill (.claude/skills/government-vibe/SKILL.md).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "docs/government/vibe/index.html"
TEMPLATE = Path(__file__).with_name("template.html")
GOV = "docs/government"
FIELDS = {"Temperament": "temperament", "Guards against": "guards", "Sounds like": "sounds"}


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, capture_output=True, text=True).stdout


def ls(ref: str, path: str) -> list[str]:
    try:
        return [l for l in git("ls-tree", "-r", "--name-only", ref, "--", path).splitlines() if l]
    except subprocess.CalledProcessError:
        return []


def show(ref: str, path: str) -> str:
    return git("show", f"{ref}:{path}")


def parse_brief(path: str, text: str) -> dict:
    head = re.match(r"### (.+?) \(([a-z-]+)\)", text)
    if not head:
        raise SystemExit(f"{path}: no '### Title (post)' heading")
    out = {"num": int(Path(path).name[:2]), "title": head.group(1), "post": head.group(2)}
    for para in re.split(r"\n\s*\n", text):
        m = re.match(r"\*\*(.+?):\*\*\s*(.*)", para.strip(), re.S)
        if m and m.group(1) in FIELDS:
            out[FIELDS[m.group(1)]] = " ".join(m.group(2).split())
    return out


def parse_statement(path: str, text: str) -> dict | None:
    m = re.match(r"(\d{4}-\d{2}-\d{2})/([a-z-]+)\.md$", path.split("statements/", 1)[1])
    if not m:
        return None
    meta, body = {}, text
    fm = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if fm:
        body = fm.group(2)
        for line in fm.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    date, post = m.groups()
    return {
        "id": f"{date}_{post}", "date": date, "post": post, "text": body.strip(),
        "platform": meta.get("platform", "any"), "status": meta.get("status", "draft"),
        "url": meta.get("url", ""),
        "answers": [a.strip() for a in meta.get("answers", "").split(",") if a.strip()],
    }


def open_pr() -> dict | None:
    try:
        out = subprocess.run(["gh", "pr", "list", "--label", "government", "--state", "open",
                              "--json", "number,headRefName,url"], cwd=ROOT, check=True,
                             capture_output=True, text=True).stdout
        prs = json.loads(out)
        return prs[0] if prs else None
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError):
        print("warning: could not ask GitHub for an open government PR; showing main only")
        return None


def main() -> None:
    if "--no-fetch" not in sys.argv:
        git("fetch", "-q", "origin")
    base = "origin/main"
    briefs = [parse_brief(p, show(base, p)) for p in sorted(ls(base, f"{GOV}/ministers")) if re.search(r"/\d\d-[a-z-]+\.md$", p)]

    posts: dict[str, dict] = {}
    for p in ls(base, f"{GOV}/statements"):
        s = parse_statement(p, show(base, p))
        if s:
            s["where"] = "main"
            posts[s["id"]] = s
    pr = open_pr()
    if pr:
        ref = f"origin/{pr['headRefName']}"
        for p in ls(ref, f"{GOV}/statements"):
            s = parse_statement(p, show(ref, p))
            if s and (s["id"] not in posts or posts[s["id"]]["text"] != s["text"]):
                s.update(where="pr", pr=pr["number"], prUrl=pr["url"])
                posts[s["id"]] = s

    order = {b["post"]: b["num"] for b in briefs}
    ordered = sorted(posts.values(), key=lambda s: (s["date"], -order.get(s["post"], 99)), reverse=True)

    def blob(x) -> str:
        return json.dumps(x, ensure_ascii=False, indent=1).replace("</", "<\\/")

    html = TEMPLATE.read_text()
    html = html.replace("/*__MINISTERS__*/[]", blob(briefs)).replace("/*__POSTS__*/[]", blob(ordered))
    html = html.replace("/*__BUILT__*/\"\"", json.dumps(git("rev-parse", "--short", base).strip()))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html)
    print(f"wrote {OUT.relative_to(ROOT)}: {len(briefs)} ministers, {len(ordered)} posts"
          + (f" (open PR #{pr['number']})" if pr else " (no open PR)"))


if __name__ == "__main__":
    main()
