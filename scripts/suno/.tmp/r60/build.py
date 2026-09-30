"""r60 — the drop lands on "you keep on walking", and a different grime voice in every lane.

Brief (Jack, 2026-09-21): *"'you keep on walking, through that Wait trose door' this is where the
drum and bass 'drop' should happen. Redo all of those with that in mind, also mix up the grime voice
in each generation."*

🔴 AND A BUG FOUND WHILE DOING IT. Every lane since r58 inherited the SOURCE's lyric cues, which
say, in the Lyrics box, in writing:

    [Verse 1 | THE FULL BEAT ROLLING UNDER HIM FROM THE FIRST LINE | the first man, gravelly raspy
     voice, ..., AN OLDER ENGLISH STORYTELLER, not half time]
    [Verse 2 | ... | the second man, A BBC NEWSREADER VOICE, clipped and cold]

So while the Style box asked for two grime MCs over a drumless piano opening, the Lyrics box was
asking for a full beat from bar one and casting a storyteller and a newsreader. **That is why the
grime voice kept disappearing** — the two boxes were fighting, and the lyric labels are the ones
sitting right next to the words being performed. Every cue is rebuilt from scratch here.

The two changes Jack asked for:

1. THE DROP IS PLACED, not described. A `[Drop]` section tag now sits immediately before
   "you keep on walking, through that Wait trose door", so the first three lines are the drumless
   piano opening and the beat lands on that line. A section TAG is what makes Suno re-decide the
   arrangement - an inline adjective does not (`suno-tag-mechanics.md`).

2. A DIFFERENT GRIME VOICE PER LANE. Five different English grime registers, each still grime, each
   with its own second voice for contrast. The lyric labels stay the same two short fixed labels in
   every lane (`[gruff MC]` / `[cold MC]`) because one fixed label per character is what keeps a
   voice from drifting; the DESCRIPTION varies in the Style box, which is where casting belongs.

Kept from r59: the four-drop shape measured off the liked take, the orchestra with a job against
the break, controlled pace, no uniformity words, no dancefloor sheen, the sung chorus.
"""
import json, pathlib

OUT = pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r60')
LYR = json.loads((pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r59/violin.json')).read_text())['lyrics']

DROP_LINE = "you keep on walking, through that Wait trose door"

LANES = [
  dict(
    key='violin',
    open="a sad piano and a lone violin",
    drums="chopped amen breaks, a rolling Reese sub, skippy two-step, fills at the turns",
    score=("A solo violin and a string section play with the break, not over it: the violin "
           "answers the MC between lines, the low strings saw the sub's notes"),
    prod="Raw, dry, close, narrow and bright, night-bus melancholy",
    cast=("A deep gravelly South London grime MC, weighty and unhurried, trading with a clipped, "
          "cold, sneering London MC"),
    drop_cue="the sub and the whole break slam in on this line, the violin and strings arriving with them",
    ban="pipe organ, cathedral organ, harp, celesta, glass harmonica, vibraphone, tubular bells, timpani, war drums, low brass, trombone, tuba, muted piano, ticking pizzicato",
  ),
  dict(
    key='organ',
    open="a cathedral pipe organ and low strings",
    drums="hard techstep breaks, machine hats, a cold metallic Reese",
    score=("The organ holds one enormous minor chord under the drop and stabs on the offbeats "
           "elsewhere, low strings doubling the sub: the church and the break are one instrument"),
    prod="Cavernous, long reverb tails, huge low end, cold",
    cast=("A harsh, wiry East London grime MC, nasal and fast-tongued in the old pirate-radio way, "
          "trading with a flat, deadpan, quietly menacing MC"),
    drop_cue="the sub and the whole break slam in on this line, the organ landing on the same beat",
    ban="solo violin, string section, harp, celesta, glass harmonica, vibraphone, tubular bells, timpani, war drums, low brass, trombone, tuba, muted piano, ticking pizzicato",
  ),
  dict(
    key='clock',
    open="a muted piano and a ticking pizzicato",
    drums="cold skippy breaks, tight snares, a creeping Reese",
    score=("A pizzicato ostinato ticks sixteenths against the break like a clock, a muted piano "
           "answers the snare, a cello doubles the sub: thriller-cold timekeeping inside the "
           "drums, not atmosphere"),
    prod="Narrow, clinical, tense, sudden when loud",
    cast=("A low, almost-spoken North London grime MC, menacing and held back, trading with a "
          "sharp, high, sarcastic MC who cuts every line short"),
    drop_cue="the sub and the whole break slam in on this line, the pizzicato ticking straight through it",
    ban="pipe organ, cathedral organ, harp, celesta, glass harmonica, vibraphone, tubular bells, timpani, war drums, low brass, trombone, tuba, soaring strings, lush strings",
  ),
  dict(
    key='brass',
    open="a lone trombone and a struck timpani",
    drums="an amen assault, breaks tumbling and tearing, a filthy distorted sub",
    score=("Low brass stabs land in the holes the break leaves, timpani doubling every kick: "
           "percussion inside the kit, never a bed and never a tune"),
    prod="Overdriven and tape-hot, loud and dirty, like a dubplate cut too hard",
    cast=("A hoarse, roaring Birmingham grime MC who shouts the end of every bar, trading with a "
          "cold, clipped, bored and superior MC"),
    drop_cue="the sub and the whole break slam in on this line, brass and timpani landing with them",
    ban="pipe organ, cathedral organ, harp, celesta, glass harmonica, vibraphone, tubular bells, solo violin, string section, muted piano, ticking pizzicato",
  ),
  dict(
    key='glass',
    open="a harp and a glass harmonica",
    drums="rolling liquid breaks, a deep round sub, warm and heavy, fills at every turn",
    score=("Harp arpeggios ring in the gaps between rapped lines, a celesta doubles the hi-hats, a "
           "bowed vibraphone holds under the drops: glass and metal as percussion with the break"),
    prod="Wide, airy and shimmering, deep warm bottom",
    cast=("A Manchester grime MC who half-sings between the rapped lines, melodic and unhurried, "
          "trading with a crisp, brittle, sarcastic MC"),
    drop_cue="the sub and the whole break slam in on this line, the harp ringing across the top",
    ban="pipe organ, cathedral organ, timpani, war drums, low brass, trombone, tuba, muted piano, ticking pizzicato, solo violin, string section, distorted, industrial",
  ),
]

GUARD = ("rave, club anthem, festival, EDM, big room, euphoric, anthemic, four on the floor, house, "
         "commercial dance, glossy production, radio pop, jump up, wobble bass, dubstep, "
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
        f"Dark UK drum and bass, 174 BPM, minor key, grime over it. "
        f"It opens on {l['open']} with no drums at all, the first MC quiet and close over them for "
        f"three lines. "
        f"Then the sub and the break slam in together in one bar, on the line 'you keep on walking'. "
        f"It breaks down and slams back three more times after that, each bigger, the biggest two "
        f"thirds through; the quiet parts are quiet. "
        f"Under the rap: {l['drums']}. "
        f"{l['score']}. "
        f"A sung chorus hook returns three times, the only sung thing. "
        f"{l['prod']}. "
        f"{l['cast']}, both controlled and on the 174 grid, hitting hard, never pausing mid-line, "
        f"never double-time.")


def lyrics(l):
    t = LYR

    def rep(a, b):
        nonlocal t
        assert a in t, 'NO-OP replace: ' + a[:70]
        t = t.replace(a, b)

    # 1 ── the opening: no drums, and the SOURCE's "full beat from the first line" cue destroyed
    rep("[Verse 1 | the full beat rolling under him from the first line | the first man, gravelly "
        "raspy voice, the same pace all the way, never pausing mid-line, an older English "
        "storyteller, not half time]",
        f"[Verse 1 | {l['open']} alone, no drums at all | gruff MC, quiet and close, three lines only]")

    # 2 ── 🔑 THE DROP, placed on the line Jack named
    rep(DROP_LINE,
        f"[Drop | {l['drop_cue']}]\n"
        "[gruff MC, controlled and weighty, hitting hard on the beat, never pausing mid-line]\n"
        + DROP_LINE)

    # 3 ── every remaining source label replaced with the two fixed grime labels
    rep("[the first man, gravelly raspy voice, the same pace all the way, never pausing mid-line, "
        "rising, never a scream]", "[gruff MC, rising, never a scream]")
    rep("[the first man, gravelly raspy voice, the same pace all the way, never pausing mid-line, "
        "a weary bitter plea]", "[gruff MC, a weary bitter plea]")
    rep("[Verse 2 | straight in, no break | the beat builds, bigger than verse one | the second "
        "man, a BBC newsreader voice, clipped and cold]",
        "[Verse 2 | straight in, no break, the beat bigger than verse one | cold MC, clipped and cutting]")
    rep("[the second man rising, biting and bitter]", "[cold MC, rising, biting and bitter]")
    rep("[Bridge | straight in, no break | the two men trade lines, the beat at its biggest]",
        "[Bridge | straight in, no break, the beat at its biggest | the two MCs trade lines]")
    rep("[the first man, gravelly raspy voice, the same pace all the way, never pausing mid-line]",
        "[gruff MC]")
    rep("[the second man]", "[cold MC]")
    rep("[both men together]", "[both MCs together]")

    # 4 ── the other three impact points, so the record keeps moving (the measured four-drop shape)
    first, second = t.split("[Chorus | sung, the hook, the beat and the strings together]")[0], None
    parts = t.split("[Chorus | sung, the hook, the beat and the strings together]")
    assert len(parts) == 3, len(parts)
    t = (parts[0]
         + "[Chorus | sung, the hook, the break and the score together]"
         + parts[1]
         + "[Chorus | the beat drops out for the first line, bare voice, then it all slams back "
           "louder than the first chorus | sung]"
         + parts[2])
    rep("[Final Chorus | sung, the biggest moment, the strings over the break]",
        "[Final Chorus | the biggest drop of the record, everything at once | sung]")

    assert "storyteller" not in t and "newsreader" not in t and "the first man" not in t
    assert t.index("[Drop |") < t.index(DROP_LINE)
    return t


rows = []
for l in LANES:
    s, ly = style(l), lyrics(l)
    assert len(s) <= 1000, (l['key'], len(s), 'OVER BY ' + str(len(s) - 1000))
    spec = {
        "style": s, "exclude": GUARD + ', ' + l['ban'], "lyrics": ly,
        "model": "v6",
        "title": f"camping-r60-{l['key']}",
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
    rows.append((l['key'], len(s), ly.count('\n') + 1))

for k, sl, lp in rows:
    print(f"{k:7} style={sl:4} lyricLines={lp}")
print("\ncues, violin lane:")
for line in lyrics(LANES[0]).split('\n'):
    if line.startswith('['):
        print('  ' + line)
