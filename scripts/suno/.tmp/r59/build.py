"""r59 — the translatable prompt: describe the SONG, not the box that made it. Then vary it hard.

Brief (Jack, 2026-09-21): *"with those generations, we lost the grime voice, the orchestral elements
and the overall vibe of the song we are trying to improve. please research the internet and put into
a prompt that is translatable from suno of the original song, and ask yourself using that prompt, to
see what could be improved and use all of the previous advice. also all of the last generations
sounded the same, i asked for different versions of the improved song that varied massively."*

🔴 WHAT r58 GOT WRONG. Told to "forget everything", it ran 1127446d's own boxes verbatim — and those
boxes cast *an older English storyteller* and *a BBC newsreader*, ban `piano`, and name no orchestral
instrument at all. So the grime voice and the violins were never asked for. The standing rule says
the opposite and it was in the repo the whole time: ALWAYS the grime voice, never the r19-reese cast,
even when building on that take.

🔑 THE FIX IS THE METHOD JACK NAMED: a prompt that is TRANSLATABLE FROM the song — a description of
what 1127446d actually SOUNDS like — not a re-run of the prompt that accidentally produced it. The
source's box is not a description of the song; the song is what drift made of it.

The description is assembled by the practitioner 5-element method (BPM / dominant texture / vocal
character / mood-era / production quirk — songsmith.studio, hookgenius) and filled in from the
measurement we already have of the liked take (§v6.39, `3eaed0b3`, per-2s band map):

  BPM               174 (measured 172 rising to 178)
  opening           0:00-0:22 quiet pitched material, harmonic 0.80-0.97 vs percussive 0.28-0.59:
                    a sad piano and a solo violin with almost no kit, the first verse rapped over it
  the drop          0:24-0:26, sub 0.36 -> 0.81 and percussive 0.40 -> 0.87 in TWO buckets: one bar
  🔑 the shape      THREE MORE breakdown/drop cycles at 0:54-1:06, 1:44-1:50, 2:08-2:12, biggest
                    section 1:50-2:06. The original is FOUR drops. Every rewrite we made had ONE -
                    which is the flatness, measured
  dominant texture  the rolling Reese sub and the chopped break; the piano owns the intro
  vocals           two English men, close and dry, storytelling, one gruff and raspy
  mood / era        night-bus melancholy, grimy, not glossy
  production quirk  narrow (correlation 0.90, side/mid -12.6 dB), bright (centroid 4.35 kHz),
                    loud and compressed (-14.2 LUFS, LRA 3.5)

THEN THE SELF-CRITIQUE — the description alone is not yet a good prompt. Everything learned in
r53-r58 is applied on top:

  1. FOUR drop cycles, written in.        <- the measured shape, and the anti-flatness fix at once
  2. The grime cast, back.                <- standing rule, lost in r58
  3. Orchestral instruments NAMED, with a job against the break. <- "cheap synth strings" alone
                                             produced violins only by luck
  4. No uniformity words.                 <- `never stops` / `throughout` = an instruction to be flat
  5. Controlled pace, never double-time.  <- "faster" overshot three rounds running
  6. The M3 comma out, `steady rap pace` out. <- the one thing he dislikes, and its literal cause
  7. The sung chorus written in.          <- an invention of Suno's that he likes
  8. No dancefloor sheen.                 <- r56 was "too dance-like"
  9. Dynamics asked for explicitly.       <- LRA 3.5 is squashed; say the quiet parts are quiet

AND THEN IT VARIES, MASSIVELY. Five lanes, each with a different orchestral family, a different
drum texture and a different production world. What they share is only what the song IS: the shape,
the words, the cast.
"""
import json, pathlib

OUT = pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r59')
R58 = json.loads((pathlib.Path('/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r58/chorus.json')).read_text())
LYR = R58['lyrics']          # source words + m3fix + the hook written in, from r58

CAST = ("Two English grime MCs: the first deep, gruff, South London, quiet and close at the start "
        "and hardening; the second clipped, cold, higher. Controlled flow on the 174 grid, hitting "
        "hard, never pausing mid-line, never double-time.")

LANES = [
  dict(
    key='violin',
    open="a sad piano and a lone violin",
    drums="chopped amen breaks, a rolling Reese sub, skippy two-step, fills at the turns",
    score=("A solo violin and a string section play with the break, not over it: the violin "
           "answers the MC between lines, the low strings saw the sub's notes"),
    prod="Raw, dry, close, narrow and bright, night-bus melancholy",
    ban="pipe organ, cathedral organ, harp, celesta, glass harmonica, vibraphone, tubular bells, timpani, war drums, low brass, trombone, tuba, muted piano, ticking pizzicato",
  ),
  dict(
    key='organ',
    open="a cathedral pipe organ and low strings",
    drums="hard techstep breaks, machine hats, a cold metallic Reese",
    score=("The organ holds one enormous minor chord under the drop and stabs on the offbeats "
           "elsewhere, low strings doubling the sub: the church and the break are one instrument"),
    prod="Cavernous, long reverb tails, huge low end, cold",
    ban="solo violin, string section, harp, celesta, glass harmonica, vibraphone, tubular bells, timpani, war drums, low brass, trombone, tuba, muted piano, ticking pizzicato",
  ),
  dict(
    key='clock',
    open="a muted piano and a ticking pizzicato",
    drums="cold skippy breaks, tight snares, a creeping Reese",
    score=("A pizzicato ostinato ticks sixteenths against the break like a clock, a muted piano "
           "answers the snare, a cello doubles the sub: thriller-cold timekeeping inside the drums, "
           "not atmosphere over them"),
    prod="Narrow, clinical, tense, sudden when loud",
    ban="pipe organ, cathedral organ, harp, celesta, glass harmonica, vibraphone, tubular bells, timpani, war drums, low brass, trombone, tuba, soaring strings, lush strings",
  ),
  dict(
    key='brass',
    open="a lone trombone and a struck timpani",
    drums="an amen assault, breaks tumbling and tearing, a filthy distorted sub",
    score=("Low brass stabs land in the holes the break leaves, timpani doubling every kick: "
           "percussion inside the kit, never a bed and never a tune"),
    prod="Overdriven and tape-hot, loud and dirty, like a dubplate cut too hard",
    ban="pipe organ, cathedral organ, harp, celesta, glass harmonica, vibraphone, tubular bells, solo violin, string section, muted piano, ticking pizzicato",
  ),
  dict(
    key='glass',
    open="a harp and a glass harmonica",
    drums="rolling liquid breaks, a deep round sub, warm and heavy, fills at every turn",
    score=("Harp arpeggios ring in the gaps between rapped lines, a celesta doubles the hi-hats, a "
           "bowed vibraphone holds under the drops: glass and metal as percussion with the break"),
    prod="Wide, airy and shimmering, deep warm bottom",
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
         "BBC newsreader, posh storyteller, "
         "orchestral bed, sustained string pad, ambient wash, epic trailer music, "
         "one steady level, static arrangement, happy, uplifting, major key, comedic, parody")


def style(l):
    return (
        # 1. what it IS — genre, tempo, key (first tokens carry the most weight)
        f"Dark UK drum and bass, 174 BPM, minor key, grime over it. "
        # 2. the opening, measured: 22 seconds of pitched material with almost no kit
        f"It opens on {l['open']} with almost no drums for twenty seconds, the first MC quiet and "
        f"close over them. "
        # 3. the drop — one bar, both hands at once
        f"Then the sub and the break arrive together in one bar and the record doubles in weight. "
        # 4. 🔑 THE SHAPE: four drop cycles, off the measurement. This is the anti-flatness fix
        f"It breaks down and slams back three more times, each bigger, the biggest two thirds "
        f"through; the quiet parts are quiet. "
        # 5. the drums of this lane
        f"Under the rap: {l['drums']}. "
        # 6. the score of this lane, with its job
        f"{l['score']}. "
        # 7. the hook Suno invented and Jack kept
        f"A sung chorus hook returns three times, the only sung thing. "
        # 8. production of this lane
        f"{l['prod']}. "
        # 9. cast
        + CAST)


rows = []
for l in LANES:
    s = style(l)
    e = GUARD + ', ' + l['ban']
    assert len(s) <= 1000, (l['key'], len(s), 'OVER BY ' + str(len(s) - 1000))
    spec = {
        "style": s, "exclude": e, "lyrics": LYR,
        "model": "v6",
        "title": f"camping-r59-{l['key']}",
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
    rows.append((l['key'], len(s), len(e)))

# BOLD check — the longest run any two lanes share must be the shape + the cast, nothing else
def longest_common(a, b):
    best = ''
    for i in range(len(a)):
        for j in range(len(a), i + len(best), -1):
            if a[i:j] in b:
                best = a[i:j]
                break
    return best

st = {l['key']: style(l) for l in LANES}
worst = ('', '', '')
for i, x in enumerate(LANES):
    for y in LANES[i + 1:]:
        c = longest_common(st[x['key']], st[y['key']])
        if len(c) > len(worst[2]):
            worst = (x['key'], y['key'], c)

for k, sl, el in rows:
    print(f"{k:7} style={sl:4} exclude={el:4}")
print(f"\nlongest shared run: {len(worst[2])} chars between {worst[0]} and {worst[1]}")
print(f"  -> {worst[2][:90]!r}")
