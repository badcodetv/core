"""r57 — de-danced, and three different attacks on FLATNESS.

Brief (Jack, 2026-09-21): *"those generations were too dance-like, please look through the prompt
for [1127446d] and try to add elements of the thriller song from before. please try and not make it
flat, they all sound flat and boring."*

🔴 THE DIAGNOSIS, and it is our own fault, in writing. Every box since r53 has carried:
      "the breaks never stop, not one bar"
      "the drums and the sub are the loudest thing in the mix throughout"
      "rapid-fire from here to the end"
   Those clauses were added to stop 12-14 s holes (r49) and a slow rap. What they actually say is
   *nothing changes for three minutes* — they are an instruction to be flat. The same trap is in
   this song's own history: the v5.5 sheet's "not flat" row found `one steady groove start to
   finish, never building, never dropping` doing exactly this, and the fix was GEARS.
   Supporting: "many AI tracks feel flat all the way through because every section sits at the same
   vocal weight" (HookGenius), and section tags alone do nothing unless they say HOW to move
   between sections.

   So: the uniformity clauses are GONE, and each lane carries one device against flatness.

The de-dance: r56 chased "like Chase and Status" into `rave stabs, club-ready, big polished
dancefloor`, which is the dance-like part. Kept: razor-sharp chopped breaks and the gnarly Reese —
the weight. Banned: the sheen (`rave, club anthem, festival, EDM, euphoric, anthemic, big room`).

Three lanes, one variable: WHICH anti-flatness device. Same spine, same words, same settings — this
is a controlled test, not a variety sweep.
"""
import json, pathlib

REPO = pathlib.Path('/home/jackt/projects/badcode/badcode')
OUT = REPO / 'scripts/suno/.tmp/r57'
LYR = json.loads((REPO / 'scripts/suno/.tmp/r56/d175.json').read_text())['lyrics']

# ── the 1127446d spine, in its own words, minus the clause Jack disliked ────
SPINE = ("A solid, punchy 174 BPM drum and bass beat, full breakbeats and a heavy rolling sub, "
         "never jump up: skippy two-step shuffles folded in, a dark Reese growing meaner "
         "every section, chopped amen fills at every section turn, cheap synth strings, night-bus "
         "melancholy. ")
# ── the thriller elements, each with a job inside the kit ───────────────────
THRILLER = ("A thriller score inside the drums: a pizzicato ostinato ticking against the break like "
            "a clock, a muted piano answering the snare, a cello doubling the sub. ")
CAST = ("Two English grime MCs trade verses, the first deep and gruff and South London, confident "
        "and unhurried, the second clipped and cold: controlled grime flow, one syllable to the "
        "beat with short staccato bursts, hitting hard, never rushed, never double-time.")

LANES = [
  dict(
    key='gears',
    device=("It moves in gears: piano and violin alone, then break and sub with no strings at "
            "all, then pizzicato and strings arriving together at the first chorus, verse two "
            "stripped back to the ticking and the sub, the bridge heaviest, the last chorus the "
            "piano over the break. Every section is louder or thinner than the one before. "),
    ban="",
    cues={
      "[Drop | the full breakbeat and the heavy rolling sub land at once, the pizzicato ticking on through them]":
        "[Drop | GEAR 2: the break and the heavy sub only, no strings anywhere yet]",
      "[Chorus | sung, big and melodic, the solo violin and the strings take the chorus over the break]":
        "[Chorus | GEAR 3: the pizzicato and the strings arrive for the first time, with the break | sung, big and melodic]",
      "[Verse 2 | straight in, no break, the beat bigger | cold MC, clipped and cutting, same controlled pace]":
        "[Verse 2 | GEAR 2 again: stripped back to the ticking pizzicato and the sub, strings gone | cold MC, clipped and cutting]",
      "[Bridge | the two MCs trade lines, the breaks at their heaviest, the cello under every line]":
        "[Bridge | GEAR 4, the heaviest the record gets: everything at once, cello under every line | the two MCs trade lines]",
      "[Chorus | sung, the last time, the sad piano and the solo violin return under the break]":
        "[Final Chorus | GEAR 5: the sad piano and the solo violin return over the break, the biggest moment | sung]",
    }),
  dict(
    key='cutouts',
    device=("Its dynamics come from taking things away: everything cuts out for a line before "
            "each chorus, leaving the voice bare, then the whole weight slams back on the "
            "downbeat. A bar of near-silence before the first drop, drums gone under the opening "
            "of the bridge. Nothing runs at one level for long. "),
    ban="",
    cues={
      "[Drop | the full breakbeat and the heavy rolling sub land at once, the pizzicato ticking on through them]":
        "[Drop | one bar of near-silence, then the full breakbeat and the heavy rolling sub slam in together]",
      "[Chorus | sung, big and melodic, the solo violin and the strings take the chorus over the break]":
        "[Chorus | the music cuts out under the first line, bare voice, then the whole weight slams back | sung, big and melodic]",
      "[Verse 2 | straight in, no break, the beat bigger | cold MC, clipped and cutting, same controlled pace]":
        "[Verse 2 | straight in on the downbeat, no gap | cold MC, clipped and cutting, same controlled pace]",
      "[Bridge | the two MCs trade lines, the breaks at their heaviest, the cello under every line]":
        "[Bridge | the drums drop out for the first two lines, bare voices and cello, then the break returns mid-line | the two MCs trade lines]",
      "[Chorus | sung, the last time, the sad piano and the solo violin return under the break]":
        "[Final Chorus | the music cuts out for one line, then the sad piano and the solo violin return over the break | sung, the biggest moment]",
    }),
  dict(
    key='conduct',
    device=("Every section is performed at a different weight and every layer sits at a "
            "different distance: sub at the bottom, break punching in the middle, piano the motif, "
            "strings wide and far behind, pizzicato only in the gaps between vocal lines. The "
            "voices go from close and half-spoken to a hard bitter edge. "),
    ban="",
    cues={
      "[Verse 1 | a lone sad piano and a solo violin, no drums at all | gruff MC, deep and close, quiet and emotional, unhurried]":
        "[Verse 1 | a lone sad piano and a solo violin, no drums at all | gruff MC, half-spoken, almost under his breath, right up on the mic]",
      "[Drop | the full breakbeat and the heavy rolling sub land at once, the pizzicato ticking on through them]":
        "[Drop | the full breakbeat and the heavy rolling sub land at once, the pizzicato in the gaps between lines only]",
      "[Chorus | sung, big and melodic, the solo violin and the strings take the chorus over the break]":
        "[Chorus | sung wide and far back, the strings behind it, the break punching in front | big and melodic]",
      "[Verse 2 | straight in, no break, the beat bigger | cold MC, clipped and cutting, same controlled pace]":
        "[Verse 2 | straight in, no break | cold MC, quiet and clipped at first, hardening line by line]",
      "[Bridge | the two MCs trade lines, the breaks at their heaviest, the cello under every line]":
        "[Bridge | the two MCs trade lines, rising to a hard bitter edge, cello under every line]",
      "[Chorus | sung, the last time, the sad piano and the solo violin return under the break]":
        "[Final Chorus | the biggest moment, sung full out, the sad piano and the solo violin over the break]",
    }),
]

BAN = ("rave, rave stabs, club anthem, festival, EDM, big room, euphoric, anthemic, four on the "
       "floor, house, commercial dance, radio dance, glossy club master, jump up, wobble bass, "
       "neurofunk, dubstep, "
       "double-time, rapid-fire, chopper rap, motormouth, breathless, frantic, sixteenth-note "
       "flow, laid-back, chill, mumbled, lazy flow, slow flow, half-time flow, spoken word, "
       "rapping behind the beat, off-grid vocal, half time, tempo change, drifting tempo, "
       "American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female "
       "vocal, teenage voice, boyish voice, falsetto, choir, Jamaican accent, ragga MC, "
       "orchestral bed, sustained string pad, ambient wash, epic trailer music, brass braams, "
       "one steady level, static arrangement, same all the way through, happy, uplifting, major "
       "key, comedic, novelty, parody")


def style(l):
    return SPINE + THRILLER + l['device'] + CAST


CHORUS2 = {
 'gears': "[Chorus | GEAR 3 again but heavier: the strings are back and the break rolls harder than the first chorus | sung, big and melodic]",
 'cutouts': "[Chorus | the drums cut dead for the first two words, then the whole weight slams back louder than the first chorus | sung, big and melodic]",
 'conduct': "[Chorus | sung harder and closer than the first time, more strained, the strings pushed wider behind it | big and melodic]",
}


def lyrics(l):
    t = LYR
    # the two mid-song choruses must NOT carry the same header: identical section cues are
    # themselves a documented cause of flatness (v5.5 sheet, "not flat" row).
    ch = "[Chorus | sung, big and melodic, the solo violin and the strings take the chorus over the break]"
    assert t.count(ch) == 2, t.count(ch)
    head, mid, tail = t.split(ch)
    t = head + l['cues'][ch] + mid + CHORUS2[l['key']] + tail
    for a, b in l['cues'].items():
        if a == ch:
            continue
        assert a in t, ('NO-OP replace', l['key'], a[:70])
        t = t.replace(a, b)
    # the uniformity cue goes in every lane: "from here to the end" is an instruction to be flat
    a = ("[gruff MC from here to the end, controlled and weighty, one syllable to the beat, "
         "hitting hard on the beat, never rushing]")
    assert a in t
    t = t.replace(a, "[gruff MC, controlled and weighty, one syllable to the beat, hitting hard, never rushing]")
    return t


rows = []
for l in LANES:
    s, ly = style(l), lyrics(l)
    assert len(s) <= 1000, (l['key'], len(s), 'OVER BY ' + str(len(s) - 1000))
    assert 'Final Chorus' in ly, l['key']
    spec = {
        "style": s, "exclude": BAN, "lyrics": ly,
        "model": "v6",
        "title": f"camping-r57-{l['key']}",
        "workspace": "camping-Jack",
        "styleInfluence": 80,
        "weirdness": [30, 60],
        "durationSec": 190,
        "variety": "off",
        "maxMode": False,
        "vocalGender": "male",
        "personalize": False,
    }
    (OUT / f"{l['key']}.json").write_text(json.dumps(spec, indent=2) + "\n")
    rows.append((l['key'], len(s), len(BAN), ly.count('\n') + 1))

for k, sl, el, lp in rows:
    print(f"{k:9} style={sl:4}  exclude={el:4}  lyricLines={lp}")
