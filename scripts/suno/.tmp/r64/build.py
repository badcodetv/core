"""r64 — the canon round: classic D&B anthems x famous classical works, on the 1127446d spine,
with the AGGRESSION taken back out.

Brief (Jack, 2026-09-21/22): *"So all the last generations were way too aggressive. Please combine
the style of these [10 all-time D&B anthems] and these [10 famous classical works]. And make it
something that builds off of this https://suno.com/song/1127446d-... which is the original song."*

FOUR DECISIONS:

1. 🔴 THE AGGRESSION COMES OUT OF THREE PLACES, NOT ONE. r61-r63 put it in the Style box
   (`filthy distorted`, `amen assault`, `driven until it clips`), in the CAST sentence
   (`spitting fast, furious`, `voices close to cracking`) and in the LYRIC CUES (`half-shouting,
   snarling`, `rising to a roar`, `roaring over each other`). All three are rewritten here. Taking
   it out of only the Style box would have left two thirds of it in place.

2. 🔑 THE D&B LIST IS NOT ONE SOUND - IT IS TWO, AND THE BRIEF PICKS ONE. Jack's ten contains the
   atmospheric/intelligent end (Inner City Life, Atlantis, Brown Paper Bag, Shadow Boxing, Valley of
   the Shadows) and the heavy end (Planet Dust, Pacman, Mr Happy, Tarantula, Original Nuttah). The
   heavy end is neurofunk, techstep and jump-up - i.e. exactly what "way too aggressive" just
   rejected. So the round is weighted to the atmospheric five. STATED, not smuggled.

3. 🔑 EACH LANE = ONE D&B ARCHETYPE x ONE CLASSICAL ARCHETYPE, and the classical one is chosen for
   what it DOES structurally, not for being famous:
     - Bolero      = one figure, unchanged, built by ADDING INSTRUMENTS. That is a crescendo with no
                     distortion in it, which is the literal answer to "too aggressive".
     - Canon in D  = an eight-chord ground bass looping forever with violins spinning variations
                     over it. That is a D&B bassline written in 1680.
     - Moonlight / Clair de Lune = the melancholy solo piano that IS the opening Jack likes.
     - Toccata     = menace made of a big cold room and a low organ, not of clipping.
   Blue Danube is left out on purpose: 3/4 against a 174 4/4 grid fights the spine. Ode to Joy's
   choir and Four Seasons' solo violin are already spent (r62 male choir, the spine's own violin).

4. NO NAMES IN ANY BOX (`docs/suno-gpt/system-prompt.txt`). Every one of the twenty references is
   translated into production description. The table of translations lives in camping.md.

🔴 EXCLUDES AUDIT - the fourth time an inherited ban has been found fighting the brief:
     - `major key`  banned since r19. Canon in D IS D major. LIFTED in `groundbass`.
     - `pipe organ` banned in r61-r63. The Toccata IS an organ. LIFTED in `tunnel`.
     - `sustained string pad`/`ambient wash` banned. Goldie/Bukem pads ARE that. LIFTED in
       `innercity` only - Ruling 1's bed-scale bans (`orchestral bed`, `symphony orchestra`,
       `string section`) stay in all four, with the balance sentence as the guard.
     - `measured delivery` banned since r61 as anti-drag. "Too aggressive" makes it what we now
       want. LIFTED everywhere. `steady rap pace` stays banned - r58 proved that exact token drags.
"""
import json, pathlib, re

REPO = pathlib.Path('/home/jackt/projects/badcode/badcode')
OUT = REPO / 'scripts/suno/.tmp/r64'
CANON = REPO / 'docs/stories/camping/songs/camping.md'

# ── the frozen lyric words, lifted from the r61 shared block (r62/r63 reused it unchanged) ──────
md = CANON.read_text()
start = md.index('### r61 lyrics (shared')
LYR = re.search(r'```lyrics\n(.*?)\n```', md[start:start + 8000], re.S).group(1)
assert 'you keep on walking' in LYR and 'shatoe nerf doo pap' in LYR

# ── the cast sentence ───────────────────────────────────────────────────────────────────────────
# Ruling 2 (always the grime voice) is HELD: the pool word, the two-hander and the contrast pair
# are r43's proven sentence verbatim. Its back half - "both spitting fast, furious and emotional,
# voices close to cracking, rapid-fire on the 174 grid and never slowing for a punchline" - is the
# aggression AND the speed Jack has now rejected twice, so it is replaced per lane. Flagged as a
# deliberate, stated departure from a standing ruling, not an oversight.
CAST = ("Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped "
        "and cold, ")
GRID = "one syllable to the beat on the 174 grid, never rushed."

BALANCE = "Drums and sub are the loudest thing in the mix, {} sit under them, never in front. "

LANES = {}

# ── LANE 1 · innercity — Goldie's orchestral jungle x Moonlight Sonata / Clair de Lune ──────────
LANES['innercity'] = dict(
    style=(
        "Atmospheric orchestral drum and bass, 174 BPM, minor key, grime over it: soft "
        "time-stretched breaks smeared and blurred at their edges, a warm round sub that rolls "
        "rather than bites, hats brushed back in the mix. "
        "It opens with no drums: a slow melancholy piano figure alone and a lone violin, the first "
        "MC quiet and close for three lines. "
        "Break and sub arrive together on 'you keep on walking', then it lifts and settles three "
        "more times, each fuller. "
        "Under the rap the piano keeps turning that same dreamy figure over, one line at a time; "
        "warm analogue pads swell at the turns and fall away again; a solo violin answers the hook. "
        + BALANCE.format("the piano and the pads")
        + "Yearning and tender under the paranoia, soft-edged and reverberant, night-bus "
          "melancholy. " + CAST + "weary, " + GRID
    ),
    bans="pipe organ, church organ, upright double bass, jazz, swing, brushed jazz kit, Rhodes, "
         "harpsichord, flute, clarinet, saxophone, snare ostinato, sirens, acid synth, major key",
    lift="sustained string pad, ambient wash, lush pads, laid-back",
)

# ── LANE 2 · bolero — Shadow Boxing's minimal darkness x Ravel's accumulation ───────────────────
LANES['bolero'] = dict(
    style=(
        "Minimal dark drum and bass, 174 BPM, minor key, grime over it, built by accumulation: "
        "one sparse two-bar drum pattern and one coarse filtered synth figure, and "
        "each section adds a single new instrument playing that same figure while nothing already "
        "there gets any louder. "
        "It opens with no drums: a snare ticking quietly on its own and a lone violin, the first MC "
        "close for three lines. "
        "A deep clean unhurried sub enters on the line 'you keep on walking'. "
        "Then a flute takes the figure, then a clarinet, then a low saxophone, then the strings, "
        "then the room, the filter opening further at each turn. "
        + BALANCE.format("the melody instruments")
        + "Huge space, gut-punch sub, jaw-snapping snares, nothing distorted anywhere, cold and "
          "hypnotic, night-bus melancholy. " + CAST + "patient and deadly, " + GRID
    ),
    bans="pipe organ, church organ, Rhodes, upright double bass, jazz, swing, harpsichord, lush "
         "pads, sustained string pad, ambient wash, sirens, piano ballad, major key, laid-back",
    lift="",
)

# ── LANE 3 · groundbass — Roni Size's live jazz-step x Pachelbel's ground bass ──────────────────
LANES['groundbass'] = dict(
    style=(
        "Live jazz-step drum and bass, 174 BPM, warm and acoustic, grime over it: loose swinging "
        "breaks played like a real kit, brushes and rimshots, a Rhodes chording behind them. "
        "The bassline is a plucked upright double bass walking one eight-chord baroque cycle, the "
        "same descending steps coming round again every four bars. "
        "It opens with no drums: three violins weaving over that cycle and no bass yet, the first "
        "MC close for three lines. "
        "The kit and the double bass come in together on the line 'you keep on walking'. "
        "Each section one violin falls away and another enters spinning a new line over the cycle. "
        + BALANCE.format("the violins and the Rhodes")
        + "Serene chords under a bitter story, played by a real band in a warm room, night-bus "
          "melancholy. " + CAST + "conversational and weighty, " + GRID
    ),
    bans="pipe organ, church organ, sirens, time-stretched breaks, sustained string pad, ambient "
         "wash, lush pads, flute, clarinet, snare ostinato, wedding music, easy listening, "
         "sentimental, smooth jazz, elevator music, acid synth",
    lift="major key, laid-back",  # 🔴 the Canon cycle IS major - banning it kills the lane
)

# ── LANE 4 · tunnel — Valley of the Shadows' darkcore x Bach's Toccata and Fugue ────────────────
LANES['tunnel'] = dict(
    style=(
        "Dark cinematic drum and bass, 174 BPM, D minor, grime over it: a time-stretched break "
        "smeared and pitched down, layered three deep, a vast round sub with no distortion on it, "
        "long sci-fi siren stabs sweeping across the stereo field. "
        "It opens with no drums: a cathedral pipe organ alone playing a slow falling figure that "
        "hangs and decays, the first MC close for three lines. "
        "Break and sub arrive together on the line 'you keep on walking' and the room gets bigger "
        "three more times. "
        "Under the rap the organ holds one low pedal note against the siren, and its falling figure "
        "comes back a register higher at each turn. "
        + BALANCE.format("the organ")
        + "Stone-room reverb, enormous and cold, patient rather than violent, night-bus "
          "melancholy. " + CAST + "low and menacing without ever shouting, " + GRID
    ),
    bans="Rhodes, upright double bass, jazz, swing, brushed jazz kit, harpsichord, flute, clarinet, "
         "saxophone, lush pads, sustained string pad, ambient wash, snare ostinato, major key, "
         "laid-back",
    lift="",
)

# ── the shared exclude spine ────────────────────────────────────────────────────────────────────
BASE_PACE = ("double-time, rapid-fire, chopper rap, motormouth, breathless, frantic, steady rap pace, "
             "lazy flow, slow flow, chill, lo-fi beats, half time, tempo change, drifting tempo, "
             "rubato, rapping behind the beat, off-grid vocal, spoken word")
# 🔴 NEW THIS ROUND - the aggression named as a ban, in the four places it actually lives
BASE_AGGRO = ("distorted bass, clipping, overdriven, shouting, screaming, roaring, snarling, barking, "
              "war drums, air horns, hardcore, neurofunk, jump up, wobble bass, dubstep")
BASE_CAST = ("American accent, American vocal, US rap, trap, boom bap, autotune, female vocal, "
             "teenage voice, falsetto, Jamaican accent, ragga MC, male choir, BBC newsreader, "
             "posh storyteller, narrator voice")
# Ruling 1 - classical is a garnish or it is nothing. Bed scale only, never the bare instrument.
BASE_BED = ("orchestral bed, symphony orchestra, full orchestra, string section, chamber music, "
            "epic trailer music, brass braams, static arrangement")
BASE_REG = "happy, uplifting, comedic, novelty, parody"


def exclude_for(lane):
    parts = [BASE_PACE, BASE_AGGRO, BASE_CAST, BASE_BED, BASE_REG, lane['bans']]
    text = ", ".join(p for p in parts if p)
    for token in [t.strip() for t in lane['lift'].split(',') if t.strip()]:
        text = re.sub(r'(?<![\w-])' + re.escape(token) + r'(?![\w-])\s*,?\s*', '', text)
    return re.sub(r',\s*,', ',', text).strip().strip(',')


# ── the lyric cues, de-escalated. NOT ONE WORD OF THE LYRIC CHANGES - cues only. ────────────────
CUES = [
    ("[Drop | the bass and the whole break slam in on this line, everything at once, as hard as the record gets so far]",
     "[Drop | the bass and the break arrive together on this line, the first full weight of the record]"),
    ("[gruff MC from here, half-shouting, snarling and spitting every line, hitting hard on the beat, never pausing mid-line]",
     "[gruff MC from here, weary and direct, landing one syllable on each beat, hitting hard without raising his voice]"),
    ("[gruff MC, rising to a roar]",
     "[gruff MC, lifting, more insistent, still controlled]"),
    ("[gruff MC, a snarled bitter plea]",
     "[gruff MC, a quiet bitter plea]"),
    ("[Chorus | the hook, half sung and half shouted, a room of voices chanting it back over the break]",
     "[Chorus | the hook, sung, a room of voices joining in over the break]"),
    ("[Verse 2 | straight in, no break, the beat harder than verse one | cold MC, clipped, contemptuous, spitting every word]",
     "[Verse 2 | straight in, no break, the arrangement fuller than verse one | cold MC, clipped, precise and contemptuous, every consonant landing]"),
    ("[cold MC, rising to a shout, biting and vicious]",
     "[cold MC, sharper and colder, biting]"),
    ("[Chorus | the beat cuts dead for the first line, bare shouted voice, then everything slams back harder than the first chorus | half sung, half shouted]",
     "[Chorus | the beat cuts dead for the first line, one bare voice, then everything returns fuller than the first chorus | sung]"),
    ("[Bridge | straight in, no break, the beat at its heaviest | the two MCs trade lines, roaring over each other]",
     "[Bridge | straight in, no break, the arrangement at its fullest | the two MCs trade lines, close and overlapping]"),
    ("[Final Chorus | the biggest drop of the record, everything at once, the whole room shouting it | half sung, half shouted]",
     "[Final Chorus | the biggest moment of the record, everything at once, the whole room singing it | sung]"),
]

LY = LYR
for a, b in CUES:
    assert a in LY, 'NO-OP replace (cue not found): ' + a[:80]
    LY = LY.replace(a, b)

# words must be untouched: strip every bracket cue from both and compare
words = lambda t: "\n".join(l for l in t.split("\n") if not l.strip().startswith('['))
assert words(LY) == words(LYR), 'A LYRIC WORD CHANGED - verbatim rule broken'
for bad in ('roar', 'shout', 'snarl', 'slam', 'spitting', 'half-shouting', 'vicious'):
    assert bad not in LY.lower(), 'an aggression cue survived: ' + bad

# ── emit ───────────────────────────────────────────────────────────────────────────────────────
OUT.mkdir(parents=True, exist_ok=True)
styles = {}
for key, lane in LANES.items():
    style, exclude = lane['style'], exclude_for(lane)
    assert len(style) <= 1000, (key, 'style', len(style), 'OVER BY', len(style) - 1000)
    assert 'organ' not in exclude or key != 'tunnel'
    assert 'major key' not in exclude or key != 'groundbass'
    styles[key] = style
    (OUT / f'{key}.json').write_text(json.dumps({
        "style": style, "exclude": exclude, "lyrics": LY,
        "model": "v6",
        "title": f"camping-r64-{key}",
        "workspace": "camping-Jack",
        "styleInfluence": 75,
        "weirdness": [40, 60],
        "durationSec": 200,
        "variety": "off",
        "maxMode": False,
        "vocalGender": "male",
        "personalize": False,
    }, indent=2))
    print(f"{key:12} style={len(style):4}  exclude={len(exclude):4}")

# ── the BOLD-NOT-MEEK measurement (suno-automation: >40% shared run = meek, rewrite) ────────────
def longest_run(a, b):
    best = 0
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            best = max(best, k)
    return best

print("\nlongest shared run between Style boxes (>40% = meek):")
keys = list(styles)
worst = 0
for i, x in enumerate(keys):
    for y in keys[i + 1:]:
        n = longest_run(styles[x], styles[y])
        pct = 100 * n / min(len(styles[x]), len(styles[y]))
        worst = max(worst, pct)
        print(f"  {x:11} x {y:11} {n:4} chars = {pct:4.1f}%")
print(f"\nworst = {worst:.1f}%  -> {'BOLD' if worst < 10 else 'CHECK' if worst < 40 else 'MEEK'}")
print(f"lyrics: {len(LY)} chars, {len([l for l in LY.split(chr(10)) if l.strip()])} lines")
