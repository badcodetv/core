"""r58 — back to the source. Five variations around 1127446d itself.

Brief (Jack, 2026-09-21): *"Please forget everything and just focus on this one
[1127446d]. Try and make variations of this, you have complete freedom to try and make the best
possible song using that as inspiration."*

🔑 THE METHOD THIS ROUND USES, AND WHY IT IS DIFFERENT FROM r53-r57.
Five rounds tried to WRITE IN the things Jack likes about 1127446d — the piano opening, the
violins, the sung chorus — because the repo had proved those were **accidents**: drift at weirdness
60 against a prompt that banned `piano`, demanded a full beat from bar one, and contained no chorus.
Every one of those rounds moved further from the take he likes. So this round inverts the method:
**run the source's own boxes, keep the drift space open, and change ONE thing per lane.**

The boxes below were scraped live off `suno.com/song/1127446d-...` today, in a new tab, and checked
character by character against the sheet's recovered copy. 🆕 **The Lyrics box has never been stored
in this repo before** — only described. It is stored now.

What the source actually is, as data:
  - Style 805 chars, Exclude 438 chars, Lyrics 64 lines, NO chorus anywhere.
  - `[Intro - 4 bars | a solid, full drum and bass beat ... no vocal yet]` - the drumless piano
    opening Jack loves is a direct disobedience of this cue.
  - `piano`, `slow tempo`, `half time`, `tempo change` are all BANNED - and the piano and the
    build-then-drop shape arrived anyway.
  - The one thing he dislikes has a literal cause in the box: the M3 line carries a **comma**
    (`the only thing I'm changing, is the lane in my M3`) and the voice cue says **`steady rap
    pace`**, three times. Punctuation is the brake (`lyric-craft.md`).

The five lanes, one change each:
  source  - verbatim. The control. Auto duration, because the source itself was made on Auto.
  m3fix   - the ONLY thing Jack dislikes, fixed minimally: the comma out, `steady rap pace` ->
            `the same pace all the way, never pausing mid-line`. Nothing else moves.
  unban   - m3fix, plus the four self-defeating bans removed and the `[Intro]` cue DELETED, so the
            opening he loves has room to happen rather than having to fight the box.
  chorus  - unban, plus the hook Suno invented written in as real [Chorus] sections.
  wide    - the source verbatim at weirdness 75/85. Drift made this take; this asks for more of it.
"""
import json, pathlib

OUT = pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r58')
SRC = json.loads((OUT / 'source.json').read_text())
STYLE, EXCLUDE, LYRICS = SRC['style'], SRC['exclude'], SRC['lyrics']

BASE = dict(model="v6", workspace="camping-Jack", styleInfluence=70, variety="off",
            maxMode=False, vocalGender="male", personalize=False)


def rep(text, a, b):
    assert a in text, 'NO-OP replace: ' + a[:70]
    return text.replace(a, b)


# ── m3fix: the comma is the pause, and `steady rap pace` is the drag ────────
def m3fix(style, lyrics):
    lyrics = rep(lyrics, "the only thing I'm changing, is the lane in my M3",
                         "the only thing I'm changing is the lane in my M3")
    assert lyrics.count('steady rap pace') == 6, lyrics.count('steady rap pace')
    lyrics = lyrics.replace('steady rap pace', 'the same pace all the way, never pausing mid-line')
    style = rep(style, "rapping his lines at a steady rap pace over the beat, not double time and not half time",
                       "rapping his lines at the same pace the whole way over the beat, never pausing mid-line, not double time and not half time")
    return style, lyrics


# ── unban: stop the box fighting the things he likes ───────────────────────
def unban(exclude, lyrics):
    for t in ('piano', 'slow tempo', 'half time', 'tempo change'):
        assert t in exclude
        exclude = ', '.join(x for x in (e.strip() for e in exclude.split(',')) if x != t)
    # Deleting a mention beats describing its absence (suno-tag-mechanics): with the [Intro] cue
    # gone, nothing insists on a full beat in bar one, which is what the piano had to fight.
    i = lyrics.index('\n')
    assert lyrics.startswith('[Intro')
    return exclude, lyrics[i + 1:]


# ── chorus: the hook Suno invented, written in ─────────────────────────────
HOOK = ("[Chorus | sung, the hook, the beat and the strings together]\n"
        "I can't live like this forever\n"
        "I can't live like this forever\n"
        "I might be insane but I do want change\n"
        "I can't live like this forever")


def chorus(lyrics):
    lyrics = rep(lyrics, "please sir, can I fuckin, have some more?",
                 "please sir, can I fuckin, have some more?\n" + HOOK)
    lyrics = rep(lyrics, "now please let me drink my shatoe nerf doo pap",
                 "now please let me drink my shatoe nerf doo pap\n" + HOOK)
    lyrics = rep(lyrics, "and by the time it hits, we'll be gone\n[end]",
                 "and by the time it hits, we'll be gone\n"
                 + HOOK.replace('[Chorus | sung, the hook, the beat and the strings together]',
                                '[Final Chorus | sung, the biggest moment, the strings over the break]')
                 + "\n[end]")
    return lyrics


lanes = {}

# 1 ── the control, exactly as it was made
lanes['source'] = dict(style=STYLE, exclude=EXCLUDE, lyrics=LYRICS,
                       weirdness=[40, 60], durationSec=None)

# 2 ── the one dislike, fixed
s2, l2 = m3fix(STYLE, LYRICS)
lanes['m3fix'] = dict(style=s2, exclude=EXCLUDE, lyrics=l2, weirdness=[40, 60], durationSec=200)

# 3 ── + the box stops fighting the drift
e3, l3 = unban(EXCLUDE, l2)
lanes['unban'] = dict(style=s2, exclude=e3, lyrics=l3, weirdness=[40, 60], durationSec=200)

# 4 ── + the invented hook, named
lanes['chorus'] = dict(style=s2, exclude=e3, lyrics=chorus(l3), weirdness=[40, 60], durationSec=200)

# 5 ── the source, with more of the drift that made it
lanes['wide'] = dict(style=STYLE, exclude=EXCLUDE, lyrics=LYRICS,
                     weirdness=[75, 85], durationSec=None)

for key, l in lanes.items():
    spec = {**BASE, **l, "title": f"camping-r58-{key}"}
    if spec['durationSec'] is None:
        del spec['durationSec']          # omitted => the loader sets Duration to Auto, as the source was
    assert len(spec['style']) <= 1000, (key, len(spec['style']))
    (OUT / f"{key}.json").write_text(json.dumps(spec, indent=2) + "\n")
    print(f"{key:7} style={len(spec['style']):4} exclude={len(spec['exclude']):4} "
          f"lines={spec['lyrics'].count(chr(10))+1:3} w={l['weirdness']} "
          f"dur={l['durationSec'] or 'Auto'}")
