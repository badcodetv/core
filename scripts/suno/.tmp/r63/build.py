"""r63 — a third wave on the frozen spine. Four more worlds, four more voices.

Brief (Jack, 2026-09-21): *"Just keep going i dont want to influence this process negatively. Just
do more of whatever that was thanks."*

So: same spine, no narrowing, four textures we have not used. The colours already spent across
r59-r62 are strings, organ, thriller pizzicato, brass+timpani, harp/celesta/glass, wobble bass,
war drums, acid, riot noise, rave piano, male choir, dub siren and industrial metal. This wave adds
four that are new AND that carry something of the song's own subject with them.

🔑 One of them is chosen for the story, not just the sound. A British colliery BRASS BAND is the
sound of exactly the towns this song is about, and putting it over an amen break is the whole
argument of the record in one arrangement. That is the kind of choice the spine is stable enough to
allow now.
"""
import json, pathlib

OUT = pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r63')
BASE = json.loads((pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r61/wobble.json')).read_text())
LYR = BASE['lyrics']
DROP_LINE = "you keep on walking, through that Wait trose door"

LANES = [
  dict(
    key='brassband',
    drums="an amen assault, breaks tearing across whole bars, relentless",
    bass="A filthy distorted Reese under everything, driven until it clips",
    score=("A northern colliery brass band stabs hard and short in the holes the break leaves, "
           "cornets high and grieving over the drops, euphonium doubling the sub"),
    prod="Brass in a cold hall, breaks dry and dirty, the two worlds cut together",
    cast="A Durham grime MC, blunt and hard, against a cold clipped MC who sneers",
    ban="cimbalom, hammered dulcimer, distorted guitar, baritone saxophone, pipe organ, male choir, dub siren, rave piano, hoover, harp, celesta, tubular bells, muted piano, ticking pizzicato",
  ),
  dict(
    key='cimbalom',
    drums="chopped jungle breaks, rapid and rolling, fills across the bar",
    bass="A dark Reese growing meaner every section, distorted at the drops",
    score=("A hammered cimbalom rattles a minor figure in sixteenths against the break, a double "
           "bass sawing underneath: struck strings as percussion, never a melody on top"),
    prod="Close, wooden and nasty, hammers loud, slightly overdriven",
    cast="A Liverpool grime MC, quick and cutting, against a low deadpan MC",
    ban="brass band, cornet, euphonium, distorted guitar, baritone saxophone, pipe organ, male choir, dub siren, rave piano, hoover, harp, celesta, tubular bells, muted piano",
  ),
  dict(
    key='sludge',
    drums="mechanical chopped breaks, snares tumbling over each other",
    bass="A detuned palm-muted guitar figure doubling a distorted sub, low and slow",
    score=("The guitar never plays chords, only that figure, and a solo violin screams one line "
           "over each drop: guitar as bass, violin the only voice above the break"),
    prod="Heavy, downtuned, filthy, amp hum left in",
    cast="A Sheffield grime MC, flat and furious, half-shouting, against a high sarcastic MC",
    ban="brass band, cornet, euphonium, cimbalom, hammered dulcimer, baritone saxophone, pipe organ, male choir, dub siren, rave piano, hoover, harp, celesta, tubular bells",
  ),
  dict(
    key='barisax',
    drums="rolling jungle breaks, heavy and loose, amen fills at every turn",
    bass="A vast round sub with a growling mid-range over it, biting at the drops",
    score=("A baritone saxophone honks one ugly riff on the offbeats, a cello answering low "
           "down: the horn is rhythm, never a solo, never smooth"),
    prod="Raw and blaring, room horns against dry breaks, loud and ragged",
    cast="A Croydon grime MC, snarling and nasal, against a clipped contemptuous MC",
    ban="brass band, cornet, euphonium, cimbalom, hammered dulcimer, distorted guitar, pipe organ, male choir, dub siren, rave piano, hoover, harp, celesta, tubular bells, smooth jazz, saxophone solo",
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
    assert LYR.index('[Drop |') < LYR.index(DROP_LINE)
    assert 'newsreader' not in LYR and 'storyteller' not in LYR
    spec = {
        "style": s, "exclude": GUARD + ', ' + l['ban'], "lyrics": LYR,
        "model": "v6",
        "title": f"camping-r63-{l['key']}",
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
    print(f"{k:10} style={sl:4} exclude={el:4}")
