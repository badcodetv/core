import json, pathlib
g = json.loads(pathlib.Path('scripts/suno/.tmp/r64/takes.json').read_text())
SHORT = {
 'innercity': 'time-stretched breaks, a melancholy piano turning one figure, pads at the turns',
 'bolero':    'one figure, one more instrument each section, nothing gets louder',
 'groundbass':'an upright double bass walking a baroque cycle, three violins over it',
 'tunnel':    'a cathedral organ pedal, sirens, a break stretched and layered three deep',
}
def cell(lane, w):
    v = g.get(f'camping-r64-{lane}-v6-w{w}', [])
    return ' · '.join(f'[{s[:8]}](https://suno.com/song/{s})' + (f' ({d})' if d and d != 'null' else '') for s, d in v) or '—'
rows = '\n'.join(f"| `{l}` | {SHORT[l]} | {cell(l,40)} | {cell(l,60)} |" for l in SHORT)
new = f"""### Generated 2026-09-22 — 8 Creates, 16 takes. Credits 9,460 → 9,380

| Lane | Shorthand | w40 | w60 |
|---|---|---|---|
{rows}

✅ **Eight Creates, eight clean** — no `create:timeout`, no re-runs, 10 credits each exactly as v6 has
costed since r54. All sixteen came back **3:19–3:20** against the 200 s target, consistent with r48's
±1 s finding.

⬜ **Not heard.** The listening question is not "which lane is best" — it is **has the aggression
actually gone, and did anything come with it?** In order: does `bolero` build without ever getting
harsh (the accumulation idea is the round's real bet)? Does `groundbass` stay bitter now that the
chord cycle is major, or does it go sentimental — the one risk the lifted `major key` ban buys? Does
`tunnel` still feel like a threat with nothing distorted in it? And 🔴 **listen for what the cut cast
sentence cost**: if the MCs now sound bored rather than weary, r43's back half goes back in first."""
p = pathlib.Path('docs/stories/camping/songs/camping.md'); md = p.read_text()
old = """### Generated 2026-09-22 — 8 Creates, 16 takes

⬜ **Pending** — table filled in on completion."""
assert old in md
p.write_text(md.replace(old, new, 1)); print('filled')
