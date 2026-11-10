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
Other scripts: from localmap import story_dir, StoryNotMapped
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
    return stored


def main(argv):
    cmd = argv[1] if len(argv) > 1 else 'list'
    try:
        if cmd == 'get':
            print(story_dir(argv[2]))
        elif cmd == 'set':
            print(f"{argv[2]} -> {set_story(argv[2], ' '.join(argv[3:]))}")
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
