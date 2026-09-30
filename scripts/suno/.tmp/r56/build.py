"""r56 — 1127446d x thriller, with the pacing walked BACK.

Brief (Jack, 2026-09-21): *"so combine this https://suno.com/song/1127446d-... with the thriller
versions, anytime ive asked for it to be faster it has gone rapidly which is way to fast. add more
classical music elemets, make the drum and bass like chase and status, the grime rapper should be
like stormzy."*

Four instructions, four decisions:

1. COMBINE = the 1127446d spine + the thriller score. From 1127446d (r19 `reese`, recovered off the
   song page): the drumless piano-and-solo-violin opening, a solid punchy 174 with full breakbeats
   and a heavy rolling sub, skippy two-step shuffles folded in, a Reese that grows meaner every
   section, chopped amen fills at the turns, cheap synth strings, night-bus melancholy, the sung
   chorus. From r55 `thriller`: the pizzicato ticking against the break like a clock, the muted
   piano answering the snare, the cold low string.

2. 🔴 THE PACING GOES BACKWARDS. "Anytime I've asked for it to be faster it has gone rapidly which
   is way too fast" — r53/r54/r55 escalated `rapid-fire` -> `double-time` -> `eighth notes with
   sixteenth bursts`, and overshot. Every speed word is now REMOVED from the Style box and BANNED
   in the excludes, and the flow is described as controlled instead: one syllable to the beat with
   short staccato bursts. Duration comes back up from 155 s and is bracketed, 175 and 190, because
   duration is the lever that actually moves the delivery (195 = too slow, 155 = way too fast).

3. MORE CLASSICAL, and it is still given a job: cello doubling the sub, string figures on the
   section turns, the solo violin over the drops. The only thing still banned is the BED.

4. NO ARTIST NAMES IN THE BOX (our own rule, `docs/suno-gpt/system-prompt.txt`: never the artist,
   song, album or band name). Both references are translated into description:
   - Chase & Status -> big polished UK dancefloor d&b, razor-sharp chopped breaks, gnarly bass,
     rave stabs and sirens, huge anthemic drops, club-ready master, jungle and garage roots.
   - Stormzy -> a deep, gruff South London voice, confident, weighty and direct, hitting hard on
     the beat, conversational then staccato, never frantic.
"""
import json, pathlib

REPO = pathlib.Path('/home/jackt/projects/badcode/badcode')
OUT = REPO / 'scripts/suno/.tmp/r56'
LYR = json.loads((REPO / 'scripts/suno/.tmp/r55/thriller.json').read_text())['lyrics']

STYLE = (
    # 1. the drums: 1127446d's own mechanics, in the big polished dancefloor register
    "Big polished UK dancefloor drum and bass, 174 BPM, minor key: razor-sharp chopped breaks, "
    "skippy two-step, a gnarly Reese meaner every section, amen fills at the turns, rave stabs, "
    "club-ready. "
    # 2. the opening he loves, with the thriller clock creeping in under it
    "It opens with no drums: a lone sad piano and a solo violin, the first MC quiet and close for "
    "three lines, a ticking pizzicato creeping in till the drop. "
    # 3. the score, with a job each, inside the kit
    "Then the score sits inside the drums: pizzicato ticking against the break like a clock, "
    "muted piano answering the snare, a cello doubling the sub, string figures on the turns, "
    "the solo violin over the drops, cheap synth strings behind. "
    # 4. unity + balance
    "Strings and breaks are one piece of music, not a soundtrack over a track; drums and sub "
    "loudest. Night-bus melancholy. A sung chorus hook three times. "
    # 5. the cast, recast in the deep London register, and the flow DE-escalated
    "Two English grime MCs trade verses: the first deep, gruff, South London, confident and "
    "unhurried, the second clipped and cold. Controlled grime flow, one syllable to the beat with "
    "short staccato bursts, hitting hard, on the 174 grid, never double-time, never rushed."
)

EXCLUDE = (
    # the new bans: every speed word we have been escalating since r53
    "double-time, rapid-fire, chopper rap, motormouth, auctioneer delivery, breathless, frantic, "
    "hyperspeed rap, sixteenth-note flow, speed rap, "
    # the old delivery bans stay: slowness is still banned as delivery, never as tempo
    "laid-back, chill, mumbled, lazy flow, slow flow, half-time flow, measured recital, spoken "
    "word, rapping behind the beat, off-grid vocal, "
    # grid guards
    "half time, tempo change, drifting tempo, rubato, "
    # cast guards
    "American accent, American vocal, Southern drawl, US rap, trap, boom bap, autotune, female "
    "vocal, teenage voice, boyish voice, falsetto, choir, Jamaican accent, ragga MC, "
    # the sound this lane must not become
    "jump up, wobble bass, neurofunk, dubstep, lo-fi, tape hiss, muddy mix, "
    # classical is WANTED now - only the bed is banned
    "orchestral bed, sustained string pad, ambient wash, epic trailer music, brass braams, "
    "happy, uplifting, major key, comedic, novelty, parody"
)


def lyrics():
    t = LYR
    PAIRS = [
        ("[Verse 1 | a ticking pizzicato ostinato alone, no drums at all | gruff MC, close and quiet but already at full speed]",
         "[Verse 1 | a lone sad piano and a solo violin, no drums at all | gruff MC, deep and close, quiet and emotional, unhurried]"),
        ("[Verse 1 continues — no pause, the same MC carrying straight on | the ticking speeding up and a low string sliding upward into the drop]",
         "[Verse 1 continues — no pause, the same MC carrying straight on | a ticking pizzicato creeping in under the piano, the breaks rolling closer]"),
        ("[Drop | the cold skippy break and the creeping Reese come in, the pizzicato ticking on through]",
         "[Drop | the full breakbeat and the heavy rolling sub land at once, the pizzicato ticking on through them]"),
        ("[gruff MC, double-time from here to the end, two syllables a beat, straight into the next line with no pause]",
         "[gruff MC from here to the end, controlled and weighty, one syllable to the beat, hitting hard on the beat, never rushing]"),
        ("[Verse 2 | straight in, no break, the beat bigger | cold MC, double-time, two syllables a beat, sharp and cutting]",
         "[Verse 2 | straight in, no break, the beat bigger | cold MC, clipped and cutting, same controlled pace]"),
        ("[Chorus | sung, big and melodic, the pizzicato and the strings take the chorus with the break]",
         "[Chorus | sung, big and melodic, the solo violin and the strings take the chorus over the break]"),
        ("[Bridge | the two MCs trade lines at full speed, the breaks at their heaviest, the piano answering every snare]",
         "[Bridge | the two MCs trade lines, the breaks at their heaviest, the cello under every line]"),
        ("[Chorus | sung, the last time, the ticking pizzicato returns under the break]",
         "[Chorus | sung, the last time, the sad piano and the solo violin return under the break]"),
    ]
    for a, b in PAIRS:
        assert a in t, 'NO-OP replace (a cue from another round would survive): ' + a[:70]
        t = t.replace(a, b)
    return t


LY = lyrics()
assert len(STYLE) <= 1000, ('style', len(STYLE), 'OVER BY ' + str(len(STYLE) - 1000))
assert 'double-time' not in LY and 'full speed' not in LY, 'a speed cue survived'
assert 'a lone sad piano and a solo violin' in LY

for dur in (175, 190):
    spec = {
        "style": STYLE, "exclude": EXCLUDE, "lyrics": LY,
        "model": "v6",
        "title": f"camping-r56-thrillerreese-d{dur}",
        "workspace": "camping-Jack",
        "styleInfluence": 80,
        "weirdness": [30, 60],
        "durationSec": dur,
        "variety": "off",
        "maxMode": False,
        "vocalGender": "male",
        "personalize": False,
    }
    (OUT / f"d{dur}.json").write_text(json.dumps(spec, indent=2) + "\n")

print(f"style={len(STYLE)}  exclude={len(EXCLUDE)}  lyricLines={LY.count(chr(10))+1}")
print("specs: d175.json d190.json")
