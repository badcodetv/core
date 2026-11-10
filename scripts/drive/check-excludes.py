#!/usr/bin/env python3
"""Safety net for exclude.txt: is any file the sync skips actually USED by a Premiere project?

    python3 scripts/drive/check-excludes.py <local story folder>

Lists every local file that rclone's exclude rules leave out (`rclone ls --exclude-from` vs plain), then
searches each .prproj in the folder (gzipped XML) for its filename. A hit means the other machine would open
the project to "Link Media": the rule is too wide, so fix exclude.txt rather than the project. Prints nothing
when all is well. Runs at the end of `drive.sh status` and before every push. Exit 1 on a hit.
"""
import gzip
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
SKIP_DIRS = ('Adobe Premiere Pro', '.bridge')


def listing(root, *extra):
    out = subprocess.run(['rclone', 'lsf', '-R', '--files-only', str(root), *extra], capture_output=True, text=True)
    return set(out.stdout.splitlines()) if out.returncode == 0 else None


def main(root):
    root = pathlib.Path(root)
    every = listing(root)
    kept = listing(root, '--exclude-from', str(HERE / 'exclude.txt'))
    if every is None or kept is None:
        print('check-excludes: could not list the folder', file=sys.stderr)
        return 0
    skipped = [p for p in every - kept if not any(p.startswith(d) or f'/{d}' in p for d in SKIP_DIRS)
               and not p.endswith(('.prlock', '.pek', '.cfa', 'Thumbs.db', 'desktop.ini', '.DS_Store'))]
    if not skipped:
        return 0
    text = ''
    for pr in root.rglob('*.prproj'):
        if any(d in str(pr) for d in ('Auto-Save',) + SKIP_DIRS):
            continue
        try:
            text += gzip.open(pr).read().decode('utf-8', 'ignore').lower()
        except OSError:
            text += pr.read_bytes().decode('utf-8', 'ignore').lower()
    used = sorted(p for p in skipped if pathlib.PurePosixPath(p).name.lower() in text)
    if used:
        print(f'🛑 exclude.txt skips {len(used)} file(s) a Premiere project uses; the other machine would get "Link Media":')
        for p in used[:20]:
            print('   ', p)
        print('   Narrow the rule in scripts/drive/exclude.txt (never exclude a clip the project arranges).')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
