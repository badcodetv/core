"""r62 — more in the same direction: four new colours on the settled spine.

Brief (Jack, 2026-09-21): *"Keep making more of this in this direction i liked a few of them."*

Nothing about the spine moves. What was asked for and kept:
  - the drumless sad-piano-and-violin opening, three lines only
  - 🔑 the drop landing ON "you keep on walking, through that Wait trose door", as a [Drop] TAG
  - four breakdown/drop cycles, the biggest two thirds in
  - an orchestral element with a JOB against the break, never a bed
  - the hook half sung, half shouted, a room chanting it back
  - two English grime MCs, controlled on the 174 grid, never double-time
  - aggression from delivery words, distortion and contrast

What varies, because that is the whole point of a wave: four orchestral/textural worlds we have not
tried, four bass designs, four new grime voices from four cities.

⚠️ The lanes Jack liked are not named yet — "a few of them" — so this round widens rather than
narrows. The moment he names IDs, the next round should do the opposite: one lane, deepened.

🔴 Inherited-exclude audit (the standing rule after `piano`, the uniformity clauses and `wobble
bass` were each caught banning the brief): `choir`, `rave stabs`, `hoover`, `dub siren` and
`industrial` all came off the ban list for the lanes that need them. `choir` in particular has been
banned in every Camping box since r19 and is this round's whole `choir` lane.
"""
import json, pathlib

OUT = pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r62')
BASE = json.loads((pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r61/wobble.json')).read_text())
LYR = BASE['lyrics']
DROP_LINE = "you keep on walking, through that Wait trose door"

LANES = [
  dict(
    key='hardcore',
    drums="chopped breakbeats in the 1992 hardcore way, amen fills at every turn",
    bass="A hoover bass howling under the drops, a deep sub beneath it, both overdriven",
    score=("Stabbed rave piano chords hammer the offbeats, a lone violin crying the same figure "
           "over them: the piano is percussion, hit like a drum"),
    prod="Loud, rowdy, dark, tape-hot, air horns at the turns",
    cast="A Bristol grime MC, low and rugged, barking the ends of bars, against a cold clipped MC",
    ban="pipe organ, male choir, dub siren, clanking metal, industrial percussion, harp, celesta, tubular bells, timpani, low brass, muted piano, ticking pizzicato",
  ),
  dict(
    key='choir',
    drums="an amen assault, breaks tearing across whole bars, relentless",
    bass="A filthy distorted Reese grinding under everything, driven until it clips",
    score=("A low male choir chants one dark line under every drop, a cello doubling the sub: "
           "voices as a bass instrument with the break, never a church pad"),
    prod="Enormous and grim, long tails on the voices, dirty low end",
    cast="A Yorkshire grime MC, flat, hard and menacing, against a high sarcastic MC",
    ban="rave piano, hoover, dub siren, clanking metal, industrial percussion, harp, celesta, tubular bells, timpani, low brass, muted piano, ticking pizzicato",
  ),
  dict(
    key='dubsiren',
    drums="rolling jungle breaks, heavy and loose, snares thrown into long delays at the turns",
    bass="A vast round sub under everything, a mid-range bass growling on the drops",
    score=("A cello saws the sub's own notes, a dub siren screaming across the drops, everything "
           "thrown into tape delay"),
    prod="Cavernous dub space, spring reverb, delay throws, heavy and dread",
    cast="A Nottingham grime MC, low and threatening, against a wiry fast-tongued MC who spits",
    ban="rave piano, hoover, male choir, clanking metal, industrial percussion, harp, celesta, tubular bells, timpani, low brass, muted piano, ticking pizzicato",
  ),
  dict(
    key='industrial',
    drums="mechanical chopped breaks, clanking metal hits doubling the snare, nothing loose",
    bass="A distorted machine bass, square and cold, biting at the drops",
    score=("Bowed metal and detuned strings grind against the break on every turn, a violin "
           "playing one hard figure in the gaps between lines"),
    prod="Cold, industrial and brutal, everything slightly clipped, no warmth",
    cast="An Essex grime MC, harsh and nasal, half-shouting, against a flat deadpan MC",
    ban="rave piano, hoover, male choir, dub siren, harp, celesta, tubular bells, timpani, low brass, muted piano, ticking pizzicato",
  ),
]

GUARD = ("club anthem, festival house, EDM, big room, four on the floor, house, commercial dance, "
         "glossy production, radio pop, jump up, "
         "double-time, rapid-fire, chopper rap, motormouth, breathless, frantic, "
         "laid-back, chill, mumbled, lazy flow, slow flow, steady rap pace, measured delivery, "
         "spoken word, rapping behind the beat, off-grid vocal, "
         "American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, "
         "female vocal, teenage voice, boyish voice, falsetto, Jamaican accent, ragga MC, "
         "BBC newsreader, posh storyteller, narrator voice, "
         "orchestral bed, sustained string pad, ambient wash, epic trailer music, "
         "one steady level, static arrangement, happy, uplifting, major key, comedic, parody")


def style(l):
    return (
        f"Dark aggressive UK drum and bass, 174 BPM, minor key, grime over it. "
        f"It opens on a sad piano and a lone violin, no drums, the first MC quiet and close for "
        f"three lines, so the drop lands like a punch. "
        f"Then bass and break slam in together in one bar, on the line 'you keep on walking'. "
        f"It breaks down and slams back three more times, each harder, the biggest two thirds in. "
        f"Under the rap: {l['drums']}. "
        f"{l['bass']}. "
        f"{l['score']}. "
        f"A hook returns three times, half sung half shouted, a room chanting it back. "
        f"{l['prod']}, night-bus melancholy under it. "
        f"{l['cast']}, both on the 174 grid, hitting hard, never pausing mid-line or "
        f"double-timing.")


rows = []
for l in LANES:
    s = style(l)
    assert len(s) <= 1000, (l['key'], len(s), 'OVER BY ' + str(len(s) - 1000))
    assert '[Drop |' in LYR and LYR.index('[Drop |') < LYR.index(DROP_LINE)
    assert 'newsreader' not in LYR and 'storyteller' not in LYR
    spec = {
        "style": s, "exclude": GUARD + ', ' + l['ban'], "lyrics": LYR,
        "model": "v6",
        "title": f"camping-r62-{l['key']}",
        "workspace": "camping-Jack",
        "styleInfluence": 75,
        "weirdness": [40, 60],
        "durationSec": 200,
        "variety": "off",
        "maxMode": False,
        "vocalGender": "male",
        "personalize": False,
    }
    (OUT / f"{l['key']}.json").write_text(json.dumps(spec, indent=2) + "\n")
    rows.append((l['key'], len(s), len(spec['exclude'])))

for k, sl, el in rows:
    print(f"{k:11} style={sl:4} exclude={el:4}")
