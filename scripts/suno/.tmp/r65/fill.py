import sys, json, re, pathlib
rows = json.loads(re.search(r'\[.*\]', sys.stdin.read(), re.S).group(0))
g = {}
for r in rows: g.setdefault(r['title'], []).append((r['songId'], r['dur']))
def cell(d, w):
    v = g.get(f'camping-r65-tunnel2-d{d}-v6-w{w}', [])
    return ' · '.join(f'[{s[:8]}](https://suno.com/song/{s})' + (f' ({t})' if t else '') for s, t in v) or '—'
new = f"""### Generated 2026-09-22 — 4 Creates, 8 takes. Credits 9,380 → 9,340

| Duration | w40 | w60 |
|---|---|---|
| **175 s** — the faster half | {cell(175,40)} | {cell(175,60)} |
| **190 s** — the slower half | {cell(190,40)} | {cell(190,60)} |

✅ **Four Creates, four clean**, 10 credits each, balance read before and after every one.

⚠️ **One take missed its target and it matters for the listen.** Three of the four 175 s takes came
back at **2:55–2:57** against a 2:55 target, but `eabba79c` came back at **3:07** — a **12-second
overshoot**, only the second time in this song's history a set duration has missed by more than a
second or two (the first was r55 at 155 s). 🔑 **So `eabba79c` is not a clean member of the 175 s
cell**: it had twelve extra seconds to spread the same ~60 lines into, which is exactly the
condition that makes a take sound slow. **If the 175 s half reads as dragging, check the other three
before concluding anything.** ⬜ This is the second data point for the unverified r55 reading that a
target squeezing the words harder is likelier to be treated as a suggestion — but 175 s was clean
8/8 across r56, so the reading is now *less* well supported than it was, not more.

⬜ **Not heard.** Four questions, in order, because each one gates the next:
1. 🔑 **Are the drums back?** That is the round's whole point — every other fix is invisible if they
   are not.
2. **Does it drop on the Waitrose line**, with the beat of silence in front of it?
3. **Does the rap keep up** — and is 175 s or 190 s the right pace? This is the cleanest pacing A/B
   the song has ever had: the two cells are byte-identical apart from one number.
4. **Is the anger back without the aggression?** r43's cast sentence is whole again, and
   `clipping, overdriven, war drums, air horns, screaming, roaring` are still banned. If it now
   reads as too much again, the lever is the *cues*, not the cast sentence."""
p = pathlib.Path('docs/stories/camping/songs/camping.md'); md = p.read_text()
old = """### Generated 2026-09-22 — 4 Creates, 8 takes

⬜ **Pending** — table filled in on completion."""
assert old in md
p.write_text(md.replace(old, new, 1)); print('filled')
