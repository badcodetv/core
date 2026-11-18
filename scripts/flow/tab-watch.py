#!/usr/bin/env python3
"""Watch the Flow tab budget while a run happens, then say what really ran at once (Kai, 2026-11-18).

The Flow queue and scripts/scene/pool.mts share 10 tab SLOTS (.flow-queue/slots/0..9, one owner.json per
slot taken). This samples every 2 s: which slots are held and by whom, how many Flow tabs the browser
really has open, and whether the download lock is held. The report gives the peak, the time spent at each
level, who held slots, and any breach (more than 10 slots, or more Flow tabs than slots can explain).

    python3 scripts/flow/tab-watch.py watch LOG [--minutes N] [--port 9222]   # Ctrl-C or N minutes to stop
    python3 scripts/flow/tab-watch.py report LOG

It only reads: it never touches a slot, a lock or a tab. Whether each FILE is the right one is a separate
check (transcribe a clip, look at a still): this measures the concurrency, not the content.
"""
import json, os, sys, time, urllib.request
from collections import Counter, defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HOME = os.environ.get('BADCODE_FLOW_QUEUE_HOME', os.path.join(REPO, '.flow-queue'))
MAX_TABS = 10


def alive(pid):
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def owner(d):
    try:
        return json.load(open(os.path.join(d, 'owner.json')))
    except Exception:
        return None


def sample(port):
    slots = []
    for n in range(MAX_TABS):
        o = owner(os.path.join(HOME, 'slots', str(n)))
        if o:
            slots.append({'n': n, 'who': o.get('who', '?'), 'pid': o.get('pid'), 'alive': alive(o.get('pid', 0))})
    try:
        pages = json.load(urllib.request.urlopen(f'http://localhost:{port}/json/list', timeout=2))
        flow = [p for p in pages if p.get('type') == 'page' and 'labs.google' in p.get('url', '')]
        tabs = len(flow)
    except Exception:
        tabs = None  # browser down
    dl = owner(os.path.join(HOME, 'locks', 'download'))
    return {'t': time.time(), 'slots': slots, 'flowTabs': tabs, 'downloadLock': bool(dl)}


def watch(log, minutes, port):
    end = time.time() + minutes * 60 if minutes else None
    print(f'watching slots in {HOME} and the browser on port {port}; writing {log}', flush=True)
    last = None
    with open(log, 'a') as f:
        while end is None or time.time() < end:
            s = sample(port)
            f.write(json.dumps(s) + '\n'); f.flush()
            line = f"slots {len(s['slots'])}/{MAX_TABS}  flow tabs {s['flowTabs']}"
            if line != last:
                print(time.strftime('%H:%M:%S'), line, flush=True)
                last = line
            time.sleep(2)


def owner_kind(who):
    return 'pool' if who.startswith('pool') else 'queue' if who.startswith('q') or 'queue' in who else who.split()[0]


def report(log):
    rows = [json.loads(l) for l in open(log) if l.strip()]
    if not rows:
        print('no samples'); return
    rows.sort(key=lambda r: r['t'])
    busy = [r for r in rows if r['slots']]
    span = rows[-1]['t'] - rows[0]['t']
    level = Counter()
    for a, b in zip(rows, rows[1:]):
        level[len(a['slots'])] += b['t'] - a['t']
    peak = max(len(r['slots']) for r in rows)
    peak_at = next(r for r in rows if len(r['slots']) == peak)
    tabs = [r['flowTabs'] for r in rows if r['flowTabs'] is not None]
    holders = defaultdict(float)
    for a, b in zip(rows, rows[1:]):
        for s in a['slots']:
            holders[s['who']] += b['t'] - a['t']
    mixed = [r for r in rows if len({owner_kind(s['who']) for s in r['slots']}) > 1]
    breaches = [r for r in rows if len(r['slots']) > MAX_TABS]
    # Flow tabs the slots can't explain: the session's own tab + a pool setup tab are allowed on top.
    extra = [r for r in rows if r['flowTabs'] is not None and r['flowTabs'] > len(r['slots']) + 2]
    dead = sorted({s['who'] for r in rows for s in r['slots'] if not s['alive']})

    def hm(sec):
        return f'{int(sec // 60)}m{int(sec % 60):02d}s'

    print(f'Watched {hm(span)} ({len(rows)} samples, every ~2 s); slots held for {hm(sum(v for k, v in level.items() if k))}.')
    print(f'PEAK: {peak} of {MAX_TABS} slots at once ({time.strftime("%H:%M:%S", time.localtime(peak_at["t"]))}); '
          f'browser Flow tabs peaked at {max(tabs) if tabs else "n/a (browser not seen)"}.')
    print('Time at each level (slots held: time):')
    for k in sorted(level):
        bar = '#' * max(1, round(40 * level[k] / span)) if span else ''
        print(f'  {k:>2}: {hm(level[k]):>7}  {bar}')
    print('Holders (slot owner: time held):')
    for who, sec in sorted(holders.items(), key=lambda x: -x[1]):
        print(f'  {who}: {hm(sec)}')
    print(f'Pool and queue holding slots at the same time: {"yes, " + hm(len(mixed) * 2) if mixed else "no"}')
    print(f'Breaches of the {MAX_TABS}-slot cap: {len(breaches)}')
    print(f'Samples with more Flow tabs than slots explain: {len(extra)}' + (
        f' (worst: {max(r["flowTabs"] for r in extra)} tabs vs {min(len(r["slots"]) for r in extra)} slots)' if extra else ''))
    if dead:
        print(f'Slots still held by a dead process (freed on next take): {", ".join(dead)}')
    print('VERDICT: ' + ('PASS: never above the cap' if not breaches and not extra else 'CHECK: see breaches above')
          + ('' if busy else ' (but nothing ever took a slot: was the run on?)'))


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == 'watch':
        minutes = float(a[a.index('--minutes') + 1]) if '--minutes' in a else 0
        port = int(a[a.index('--port') + 1]) if '--port' in a else 9222
        try:
            watch(a[1], minutes, port)
        except KeyboardInterrupt:
            pass
    elif len(a) == 2 and a[0] == 'report':
        report(a[1])
    else:
        print(__doc__); sys.exit(2)
