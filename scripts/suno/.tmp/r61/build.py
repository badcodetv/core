"""r61 — the aggression, four ways. Baddadan-grade, on the 1127446d spine.

Brief (Jack, 2026-09-21): *"we have lost the aggression, like the song baddadan by chase and status
it should be like that, remember to use the original song as a point of reference."*

🔑 TWO THINGS HAD TO BE SEPARATED FIRST, because conflating them is what cost r55.
AGGRESSION IS NOT SPEED. Jack has said "way too fast" once and "lost the aggression" once, and the
temptation is to answer the second with the first. Aggression here comes from **delivery words**
(the r37/r46 finding in this repo: snarl, spit, bark, hiss, venomous, shouting the punchlines),
from **distortion and bass design**, and from **contrast** — the quiet three-line opening is what
makes the drop violent. The pacing guards stay exactly as they are: controlled, never double-time.

TRANSLATING "BADDADAN" WITHOUT NAMING IT (our rule: never the artist, song, album or band name):
  - breakneck jungle-leaning d&b, "all gas, no brakes", classic jungle's deep bass and chopped
    drums with contemporary MC vocals (Songfacts, Ticketmaster)
  - 🔑 the bass is the sound: **two sawtooth oscillators a fifth apart, LFO-modulated, distorted**,
    for a growling wobble (transmissionsamples' teardown). We have had `wobble bass` BANNED in
    every Camping exclude list since r19, inherited from the source's own box. That ban is the
    single most direct contradiction of what Jack just asked for, and it is lifted in every lane.
  - acidy resonant synths, air horns and rave sirens, MC chants traded between voices
  - the ragga MCs on that record are English (Flowdan is East London), so the grime cast rule and
    the Jamaican-accent ban both stand: the menace is written as DELIVERY, not as an accent.

KEPT FROM THE ORIGINAL, as Jack asked — `1127446d` stays the reference:
  the drumless sad-piano-and-violin opening for three lines; the drop landing ON "you keep on
  walking, through that Wait trose door"; four breakdown/drop cycles; an orchestral element with a
  job against the break; the hook; night-bus melancholy underneath the violence.

Four lanes = four kinds of aggression, so "aggressive" is not one guess.
"""
import json, pathlib

OUT = pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r61')
BASE = json.loads((pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r60/violin.json')).read_text())
LYR = BASE['lyrics']
DROP_LINE = "you keep on walking, through that Wait trose door"

LANES = [
  dict(
    key='wobble',
    open="a sad piano and a lone violin",
    drums="breakneck jungle breaks chopped to ribbons, an amen assault at every turn",
    bass=("The bass is the record: two detuned sawtooths a fifth apart, an LFO wobbling them open "
          "and shut, distorted until it growls"),
    score="Hard string stabs on the drops, a solo violin screaming over the top",
    prod="Loud, distorted and raw, air horns and sirens at the turns",
    cast=("A deep menacing East London grime MC half-shouting and spitting venom, against a cold "
          "clipped MC"),
    ban="pipe organ, harp, celesta, glass harmonica, tubular bells, timpani, war drums, low brass, muted piano, ticking pizzicato, acid synth, 303",
  ),
  dict(
    key='wardrums',
    open="a sad piano and a lone violin",
    drums="an amen assault, breaks tearing across whole bars, war drums doubling every kick",
    bass="A filthy distorted Reese grinding underneath, driven until it clips",
    score="A violent staccato string ostinato saws sixteenths against the break, timpani on the turns",
    prod="Martial, brutal and relentless, mixed hot and dirty",
    cast=("A hoarse Birmingham grime MC barking and roaring the ends of bars, against a flat cold "
          "MC who hisses"),
    ban="pipe organ, harp, celesta, glass harmonica, tubular bells, muted piano, ticking pizzicato, acid synth, 303, wobble bass lead",
  ),
  dict(
    key='acid',
    open="a sad piano and a lone violin",
    drums="chopped jungle breaks, rolling and rapid, fills that tear across the bar",
    bass="A screaming resonant acid line over a deep distorted sub, squealing at the drops",
    score="A lone violin screams over the drops and low strings saw the sub's notes",
    prod="Acidic, shrill and nasty, everything slightly overdriven",
    cast=("A wiry nasal North London grime MC, snarling, against a low deadpan MC who mutters "
          "threats"),
    ban="pipe organ, harp, celesta, glass harmonica, tubular bells, timpani, war drums, low brass, muted piano, ticking pizzicato",
  ),
  dict(
    key='riot',
    open="a sad piano and a lone violin",
    drums="raw chopped breaks, snares tumbling over each other, no space left in the bar",
    bass="A distorted sub and a growling mid-range bass, clipping at the peaks",
    score="Low brass stabs punch the holes in the break and the strings shriek on the turns",
    prod="Pirate-radio raw, clipping and shouting, sirens and a crowd roaring at the drops",
    cast=("A South London grime MC shouting over the beat, ragged and furious, against a clipped "
          "contemptuous MC"),
    ban="pipe organ, harp, celesta, glass harmonica, tubular bells, timpani, war drums, muted piano, ticking pizzicato, acid synth, 303",
  ),
]

# 🔴 wobble bass, EDM drops and crowd noise come OUT of the ban list — all three were inherited from
# the source's own exclude box and all three are the sound Jack is now asking for.
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
        f"It opens on {l['open']}, no drums, the first MC quiet and close for three lines, "
        f"so the drop lands like a punch. "
        f"Then bass and break slam in together in one bar, on the line 'you keep on walking'. "
        f"It breaks down and slams back three more times, each harder, the biggest two thirds in. "
        f"Under the rap: {l['drums']}. "
        f"{l['bass']}. "
        f"{l['score']}. "
        f"A hook returns three times, half sung half shouted, a room chanting it back. "
        f"{l['prod']}, night-bus melancholy under it. "
        f"{l['cast']}, both on the 174 grid, hitting hard, never pausing mid-line or "
        f"double-timing.")


def lyrics(l):
    t = LYR

    def rep(a, b):
        nonlocal t
        assert a in t, 'NO-OP replace: ' + a[:70]
        t = t.replace(a, b)

    rep("[Verse 1 | a sad piano and a lone violin alone, no drums at all | gruff MC, quiet and close, three lines only]",
        "[Verse 1 | a sad piano and a lone violin alone, no drums at all | gruff MC, quiet, close and bitter, three lines only]")
    rep("[Drop | the sub and the whole break slam in on this line, the violin and strings arriving with them]",
        "[Drop | the bass and the whole break slam in on this line, everything at once, as hard as the record gets so far]")
    rep("[gruff MC, controlled and weighty, hitting hard on the beat, never pausing mid-line]",
        "[gruff MC from here, half-shouting, snarling and spitting every line, hitting hard on the beat, never pausing mid-line]")
    rep("[gruff MC, rising, never a scream]", "[gruff MC, rising to a roar]")
    rep("[gruff MC, a weary bitter plea]", "[gruff MC, a snarled bitter plea]")
    rep("[Chorus | sung, the hook, the break and the score together]",
        "[Chorus | the hook, half sung and half shouted, a room of voices chanting it back over the break]")
    rep("[Verse 2 | straight in, no break, the beat bigger than verse one | cold MC, clipped and cutting]",
        "[Verse 2 | straight in, no break, the beat harder than verse one | cold MC, clipped, contemptuous, spitting every word]")
    rep("[cold MC, rising, biting and bitter]", "[cold MC, rising to a shout, biting and vicious]")
    rep("[Chorus | the beat drops out for the first line, bare voice, then it all slams back louder than the first chorus | sung]",
        "[Chorus | the beat cuts dead for the first line, bare shouted voice, then everything slams back harder than the first chorus | half sung, half shouted]")
    rep("[Bridge | straight in, no break, the beat at its biggest | the two MCs trade lines]",
        "[Bridge | straight in, no break, the beat at its heaviest | the two MCs trade lines, roaring over each other]")
    rep("[Final Chorus | the biggest drop of the record, everything at once | sung]",
        "[Final Chorus | the biggest drop of the record, everything at once, the whole room shouting it | half sung, half shouted]")

    assert "never a scream" not in t and "quiet and close, three" not in t
    assert t.index("[Drop |") < t.index(DROP_LINE)
    return t


rows = []
for l in LANES:
    s, ly = style(l), lyrics(l)
    assert len(s) <= 1000, (l['key'], len(s), 'OVER BY ' + str(len(s) - 1000))
    for banned in ('wobble bass,', 'EDM drops', 'crowd noise'):
        assert banned not in GUARD, banned
    spec = {
        "style": s, "exclude": GUARD + ', ' + l['ban'], "lyrics": ly,
        "model": "v6",
        "title": f"camping-r61-{l['key']}",
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
    print(f"{k:9} style={sl:4} exclude={el:4}")
