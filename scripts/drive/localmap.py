#!/usr/bin/env python3
"""Which LOCAL folder holds each story, on THIS machine.

Every machine keeps its own answer in badcode.local.json at the repo root (gitignored), under "stories":
    {"stories": {"karen-music": "C:\\Users\\Jack\\OneDrive\\Desktop\\YouTube vids\\Karen music vid", ...}}
The story names (keys) are shared: they are the keys of scripts/drive/folders.json, which says which Google
Drive folder each story is. Nothing guesses a local folder: a story with no entry is an error that asks.

Paths are stored in the form the person gives (a Windows path, or a Mac/Linux one) and turned into the form
the running shell needs: C:\\x -> /mnt/c/x in WSL, /c/x in Git Bash, unchanged elsewhere.

    python3 localmap.py get  <story>          print this machine's folder for <story> (exit 3 if not set)
    python3 localmap.py set  <story> <path>   record it (the folder must exist)
    python3 localmap.py list                  every story in folders.json and its folder here
    python3 localmap.py path <path>           a path from a cut file / scene.json, as THIS machine finds it
    python3 localmap.py check <file.json>...  is every file a cut / scene.json names here? (exit 1 if any missing)
                                              Use this, never `ls` on a raw path, before saying media is missing.

Sharing cuts and timelines between machines. Cut files (edl.json), scene.json and the like hold FULL paths,
written on whichever machine made them: /mnt/d/badcode-videos/karen-music/clips/x.mp4 on Kai's,
/mnt/c/Users/jackt/.../Karen music vid/clips/x.mp4 on Jack's. Each story in folders.json lists its "homes":
every folder it has lived in, on anyone's machine (`where` adds yours; commit folders.json after). A tool that
loads such a file passes it through localize(): any path inside one of a story's homes is re-pointed at this
machine's folder for that story, keeping its form (D:\\x stays Windows, /mnt/d/x stays WSL). Paths are
translated as they are read, never rewritten in the files, so nothing churns in git. A path into a story this
machine hasn't mapped is left as it is (the tool then reports the missing file, and you `where` the story).
Other scripts: from localmap import story_dir, StoryNotMapped, localize, localize_path, story_relpath
"""
import json, os, pathlib, platform, re, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
LOCAL = REPO / 'badcode.local.json'
FOLDERS = HERE / 'folders.json'
NOT_MAPPED = 3


class StoryNotMapped(KeyError):
    pass


def _env():
    if os.path.isdir('/mnt/c') or 'microsoft' in platform.release().lower():
        return 'wsl'
    if re.match(r'(MINGW|MSYS|CYGWIN)', platform.system().upper()):
        return 'gitbash'
    return 'posix'


def to_shell(p: str) -> str:
    """A stored path -> the form this shell can open."""
    m = re.match(r'^([A-Za-z]):[\\/](.*)$', p)
    if not m:
        return p
    rest = m[2].replace('\\', '/')
    env = _env()
    if env == 'wsl':
        return f'/mnt/{m[1].lower()}/{rest}'
    if env == 'gitbash':
        return f'/{m[1].lower()}/{rest}'
    return p


def to_stored(p: str) -> str:
    """What a person typed -> the form we keep (Windows paths stay Windows, so Premiere can read them too)."""
    p = p.strip().strip('"').rstrip('/\\')
    m = (re.match(r'^/mnt/([a-z])/(.*)$', p) or re.match(r'^/([a-z])/(.*)$', p)) if _env() != 'posix' else None
    if m:
        return f'{m[1].upper()}:\\' + m[2].replace('/', '\\')
    return p


def _load():
    return json.loads(LOCAL.read_text()) if LOCAL.exists() else {}


def stories() -> dict:
    return json.loads(FOLDERS.read_text())['folders']


def _posix(p: str) -> str:
    """Any absolute form -> the /mnt/x/... (or Mac/Linux) form, for comparing paths across machines."""
    m = re.match(r'^([A-Za-z]):[\\/](.*)$', p)
    return f'/mnt/{m[1].lower()}/' + m[2].replace('\\', '/') if m else p


_HOMES = None


def _homes():
    """[(home, story)], longest first, so a nested folder wins over its parent."""
    global _HOMES
    if _HOMES is None:
        _HOMES = sorted(((_posix(h).rstrip('/'), k) for k, v in stories().items() for h in v.get('homes', [])),
                        key=lambda x: -len(x[0]))
    return _HOMES


def _starts(path: str, home: str) -> bool:
    if path.startswith('/mnt/'):  # Windows drives: case doesn't matter ("Youtube Vids" == "YouTube vids")
        path, home = path.lower(), home.lower()
    return path == home or path.startswith(home + '/')


def localize_path(p):
    """One path from a shared file -> where this machine keeps it. Anything else comes back unchanged."""
    if not isinstance(p, str) or not (p.startswith('/') or re.match(r'^[A-Za-z]:[\\/]', p)):
        return p
    w = _posix(p)
    for home, story in _homes():
        if _starts(w, home):
            mine = _load().get('stories', {}).get(story)
            if not mine:
                return p
            rest = w[len(home):]
            if re.match(r'^[A-Za-z]:', p):  # keep the Windows form for Windows tools (Premiere)
                return to_stored(mine) + rest.replace('/', '\\')
            return to_shell(mine) + rest
    return p


def story_relpath(p):
    """A path on anyone's machine -> (story, path inside that story's folder, '/'-separated), or (None, None).
    The same clip gives the same answer on every machine, so use it to recognise a file across machines."""
    if not isinstance(p, str):
        return None, None
    w = _posix(p)
    for home, story in _homes():
        if _starts(w, home):
            return story, w[len(home):].lstrip('/')
    mine = {_posix(to_shell(v)).rstrip('/'): k for k, v in _load().get('stories', {}).items()}
    for home in sorted(mine, key=len, reverse=True):
        if _starts(w, home):
            return mine[home], w[len(home):].lstrip('/')
    return None, None


def localize(obj):
    """Every path inside a loaded JSON value (dicts, lists, strings), re-pointed for this machine."""
    if isinstance(obj, dict):
        return {k: localize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [localize(v) for v in obj]
    return localize_path(obj)


def _paths(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from _paths(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _paths(v)
    elif isinstance(obj, str) and (obj.startswith('/') or re.match(r'^[A-Za-z]:[\\/]', obj)):
        yield obj


def check_file(path) -> int:
    """Every absolute path in a JSON file, localized, checked on disk. Prints a summary; returns the missing count."""
    paths = sorted(set(_paths(json.loads(pathlib.Path(path).read_text()))))
    missing, unmapped = [], []
    for p in paths:
        here = to_shell(localize_path(p))
        if os.path.exists(here):
            continue
        story, _ = story_relpath(p)
        (unmapped if story and not _load().get('stories', {}).get(story) else missing).append((p, here, story))
    print(f'{path}: {len(paths)} paths, {len(paths) - len(missing) - len(unmapped)} found here, '
          f'{len(missing)} missing, {len(unmapped)} in a story this machine has not mapped')
    for p, here, story in missing:
        print(f'  missing  {here}' + (f'   (story {story}: not pulled yet, or excluded, e.g. renders/)' if story else '   (in no story: written for one machine only)'))
    for p, here, story in unmapped:
        print(f'  NOT SET  {p}   -> drive.sh where {story} "<folder>"')
    return len(missing) + len(unmapped)


def story_dir(story: str) -> str:
    known = stories()
    if story not in known:
        raise KeyError(f"unknown story '{story}': it has no row in scripts/drive/folders.json")
    p = _load().get('stories', {}).get(story)
    if not p:
        raise StoryNotMapped(story)
    return to_shell(p)


def set_story(story: str, path: str) -> str:
    if story not in stories():
        raise KeyError(f"unknown story '{story}': add its Drive folder to scripts/drive/folders.json first")
    stored = to_stored(path)
    if not os.path.isdir(to_shell(stored)):
        raise FileNotFoundError(f"no such folder on this machine: {path}")
    cfg = _load()
    cfg.setdefault('stories', {})[story] = stored
    LOCAL.write_text(json.dumps(cfg, indent=2) + '\n')
    # and the shared list of the story's homes, so cut files written here open on every other machine
    home = _posix(to_shell(stored)).rstrip('/')
    shared = json.loads(FOLDERS.read_text())
    homes = shared['folders'][story].setdefault('homes', [])
    if not any(_starts(home, _posix(h).rstrip('/')) and _starts(_posix(h).rstrip('/'), home) for h in homes):
        homes.append(home)
        _write_folders(shared)
        print(f"added this machine's folder to {story}'s homes in scripts/drive/folders.json: commit and push it",
              file=sys.stderr)
    return stored


def _write_folders(c):
    """folders.json, one story per line (stays readable as it grows)."""
    rows = ',\n'.join(f'  {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}' for k, v in c['folders'].items())
    head = {k: v for k, v in c.items() if k != 'folders'}
    body = json.dumps(head, indent=1, ensure_ascii=False)[:-2]
    FOLDERS.write_text(body + ',\n "folders": {\n' + rows + '\n }\n}\n')


def main(argv):
    cmd = argv[1] if len(argv) > 1 else 'list'
    try:
        if cmd == 'get':
            print(story_dir(argv[2]))
        elif cmd == 'set':
            print(f"{argv[2]} -> {set_story(argv[2], ' '.join(argv[3:]))}")
        elif cmd == 'path':
            print(localize_path(' '.join(argv[2:])))
        elif cmd == 'check':
            return 1 if sum(check_file(f) for f in argv[2:]) else 0
        elif cmd == 'list':
            mine = _load().get('stories', {})
            for k, v in stories().items():
                print(f"{k:24} Drive: {v['drive_name']!r:28} here: {mine.get(k, 'NOT SET (ask where it lives)')}")
        else:
            print(__doc__); return 1
    except StoryNotMapped as e:
        print(f"NOT SET: which folder on this machine holds '{e.args[0]}'? "
              f"Record it with: scripts/drive/drive.sh where {e.args[0]} \"<folder>\"", file=sys.stderr)
        return NOT_MAPPED
    except (KeyError, FileNotFoundError) as e:
        print(str(e).strip('"'), file=sys.stderr); return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
