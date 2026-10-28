#!/usr/bin/env python3
"""Work out what each harvested clip actually IS, by looking at its first frame.

Why this exists: once several Veo generations are in flight at once, nothing in Flow tells you
which finished clip came from which prompt. The gallery is virtualised so position means
nothing, and Flow's auto-titles collide badly (four playground shots, three power stations).
But image-to-video means a clip's FIRST FRAME is its source still, so the mapping is in the
pixels — no ordering assumption, no DOM, no title parsing.

Measured 2026-09-20 on real clips: a correct match scores 35-61 and its runner-up is
1800-7000, so the two populations are three orders of magnitude apart and the threshold below
is not a fine judgement call.

    python3 scripts/gaze-board/match_clips.py                 # report coverage of all 46
    python3 scripts/gaze-board/match_clips.py --apply         # rename into cut order too

A still may legitimately match SEVERAL clips (a re-roll of a shot we already had). The gallery
lists newest first and the harvester numbers in that order, so the lowest-numbered file is the
most recent generation and wins; the others are parked in inbox/dupes rather than deleted,
because every one of them is paid for.
"""
import os
import pathlib
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import motion  # noqa: E402

ROOT = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/the-gaze')
INBOX = ROOT / 'inbox'
OUT = pathlib.Path(motion.OUT)
DUPES = INBOX / 'dupes'
APPLY = '--apply' in sys.argv

# Anything worse than this is not a match at all. See the measured populations above.
THRESHOLD = 400


def sig(path, is_video):
    """A 32x32 grayscale of the frame, flat. Small enough to be instant, big enough to be sure."""
    with tempfile.NamedTemporaryFile(suffix='.pgm', delete=False) as t:
        tmp = t.name
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', str(path)]
    if is_video:
        cmd += ['-frames:v', '1']
    subprocess.run(cmd + ['-vf', 'scale=32:32', '-pix_fmt', 'gray', tmp], check=True)
    data = pathlib.Path(tmp).read_bytes()
    os.unlink(tmp)
    # Skip the PGM header: magic, width, height, maxval.
    i, tok = 0, 0
    while tok < 4:
        while i < len(data) and data[i:i + 1].isspace():
            i += 1
        while i < len(data) and not data[i:i + 1].isspace():
            i += 1
        tok += 1
    return list(data[i + 1:i + 1 + 1024])


def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)


order = {k: i + 1 for i, (k, _) in enumerate(motion.SHOTS)}
stills = {k: sig(motion.source(k), False) for k, _ in motion.SHOTS}

clips = sorted(INBOX.glob('*.mp4')) + sorted(OUT.glob('*.mp4'))
best = {}          # clip -> (distance, key)
for c in clips:
    try:
        s = sig(c, True)
    except subprocess.CalledProcessError:
        print(f'UNREADABLE {c.name}')
        continue
    d, k = min((dist(s, ks), k) for k, ks in stills.items())
    best[c] = (d, k)

# Group by the still each clip claims, closest first.
byshot = {}
for c, (d, k) in best.items():
    if d <= THRESHOLD:
        byshot.setdefault(k, []).append((d, c))
for k in byshot:
    byshot[k].sort()

have, missing = [], []
for key, _ in motion.SHOTS:
    n = order[key]
    hits = byshot.get(key, [])
    if hits:
        have.append(key)
        extra = f'  (+{len(hits) - 1} more)' if len(hits) > 1 else ''
        print(f'  {n:02d} {key:9s} OK   {hits[0][1].name:16s} d={hits[0][0]:6.1f}{extra}')
    else:
        missing.append(key)
        print(f'  {n:02d} {key:9s} ---  MISSING')

unmatched = [c.name for c, (d, _) in best.items() if d > THRESHOLD]
print(f'\n{len(have)}/{len(motion.SHOTS)} present, {len(missing)} missing')
if missing:
    print('MISSING:', ' '.join(missing))
if unmatched:
    print('UNMATCHED CLIPS (nothing in the cut looks like these):', ' '.join(sorted(unmatched)))

if APPLY:
    # 🔴 TWO PHASES, and the second one only ever moves files PARKED BY THE FIRST.
    #
    # The single-phase version renamed straight into cut order while still iterating, so a path
    # could mean different content at different points in the same loop: a file that was already
    # sitting at its final name could be picked up as another shot's candidate, moved out, and
    # then dropped into inbox/dupes as a "loser" of a shot it had actually WON. Measured
    # 2026-09-21 on 19-f3-a, whose finished clip ended up in dupes while the cut reported the
    # shot missing - which, without this script's own report to contradict it, reads as a clip
    # we never rendered and invites paying for it a second time.
    #
    # So: park every file that is going to move under a unique temporary name first, then place
    # the parked files. Nothing is ever read after it has been written, and no file is deleted.
    DUPES.mkdir(parents=True, exist_ok=True)
    STAGE = INBOX / 'staging'
    STAGE.mkdir(parents=True, exist_ok=True)

    plan = []     # (parked path, destination path)
    parked = 0
    for key, hits in byshot.items():
        dst = OUT / f'{order[key]:02d}-{key}.mp4'
        for rank, (_, clip) in enumerate(hits):
            # Rank 0 goes to its place in the cut; every other take is kept, never deleted,
            # because each one is paid for.
            target = dst if rank == 0 else DUPES / clip.name
            if clip.resolve() == target.resolve():
                continue
            hold = STAGE / f'{parked:04d}.mp4'
            parked += 1
            clip.replace(hold)
            plan.append((hold, target))

    # Anything already standing in a destination is a previous take, not a casualty: park it.
    for hold, target in plan:
        if target.exists() and target.parent == OUT:
            target.replace(DUPES / f'prev-{target.name}')
    for hold, target in plan:
        if target.exists():
            target = DUPES / f'prev-{target.name}'
        hold.replace(target)

    try:
        STAGE.rmdir()
    except OSError:
        print(f'WARNING: {STAGE} not empty - a move did not complete, nothing was deleted')
    print(f'applied -> {OUT}  ({len(plan)} moved)')
