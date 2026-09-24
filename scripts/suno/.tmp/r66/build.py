import json, re, os, sys

SRC = '/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r65/d175.json'
OUT = os.path.dirname(os.path.abspath(__file__))
r65 = json.load(open(SRC))

CAST = ("Two English grime MCs trade the verses, loud and in front, "
        "one gruff and raw, one clipped and cold, ")
TAIL = "rapid-fire on the 174 grid and never slowing for a punchline."

STYLE = {}

STYLE['odejoy'] = (
 "Cinematic UK drum and bass, 174 BPM, D minor, grime over it: a warm rolling break, snare dry and close, "
 "a deep clean Reese fattening each section, tambourine on every beat. Opens with no drums: a grand "
 "piano alone on a slow falling figure, a lone violin over, first MC quiet and close for three lines, "
 "no bass. A beat of silence, then break and Reese land together on 'you keep on walking', the piano gone, "
 "the drums alone and huge. Four times it strips to nothing and returns fuller. One tune runs the "
 "record: the piano states it low and bare, each section hands it up an octave to a new instrument, cello, "
 "violin, then the whole room; minor throughout, major only in the last chorus. Drums and sub loudest, piano "
 "and violin under them, never in front. Loud, clean, open, nothing distorted. "
 + CAST + "both fast and hurt, voices close to cracking, " + TAIL)

STYLE['mars'] = (
 "Dark militaristic drum and bass, 174 BPM, D minor, grime over it: a crunching two-step roller, snare-led and "
 "stumbling, hats dry, one eerie synth horn stabbing across it, a huge clean sub. Opens "
 "with no drums: a timpani thudding a slow figure while violins hammer one dry rattling note with the wood of "
 "the bow, first MC low and close for three lines, no bass. A beat of silence, then roller and sub arrive "
 "together on 'you keep on walking', the strings gone, the drums alone and vast. It empties and fills three "
 "more times, each a semitone higher. Under the rap the wooden strings keep rattling against the snare, six "
 "horns holding one long flat note at the turns. Drums and sub loudest, strings and horns under them, never "
 "in front. Cold, metallic, immense, glockenspiel and tam-tam at the edges. "
 + CAST + "both fast and grim, teeth clenched, " + TAIL)

STYLE['fate'] = (
 "Riff-driven UK drum and bass, 174 BPM, C minor, grime over it: the record is one four-note figure, "
 "three short, one long. Short sharp violin stabs play it, a robotic square-wave bass plays it an octave "
 "down, the hats play its rhythm, brass stabs answer. Opens with no drums: those four notes alone on the "
 "violins, repeated and pulled apart, first MC close for three lines, no bass. A beat of silence, then "
 "break and bass hit that figure together on 'you keep on walking', the violins gone, the drums alone, "
 "massive. Three more times it falls to one stab and builds straight back. Every section the figure moves, "
 "inverted, up a third, cut in half, handed on, always those four notes. Drums and bass loudest, stabs under "
 "them, never in front. Tight, dry, mechanical, nothing distorted. "
 + CAST + "both fast and stinging, every syllable cut short, " + TAIL)

STYLE['chorale'] = (
 "Jungle-rooted UK drum and bass, 174 BPM, D minor, grime over it: breakneck chopped amen breaks, ragga "
 "swing, a deep round sub, handclaps on the backbeat. Opens with no drums and no instruments: a room of "
 "men singing the hook line together in bare block harmony, then the first MC close for three lines. A beat "
 "of silence, amen and sub hit together on 'you keep on walking', the voices gone, the drums alone and "
 "enormous. It empties and slams back three more times. Across the record the room answers the MC: he lands a "
 "line, they hit one word together in block harmony, one high voice running a fast line under before the "
 "next bar. A church organ holds chords at the turns only. Drums and sub loudest, voices under them, "
 "never in front. Big, clean, open, a stadium, nobody screaming. "
 + CAST + "both fast and raw-throated, half singing line ends, " + TAIL)

BASE = ("double-time, chopper rap, motormouth, breathless, steady rap pace, lazy flow, slow flow, spoken word, "
 "downtempo, trip hop, half time, half-time drums, sparse percussion, drumless, beatless, ambient, soundtrack, "
 "underscore, slow build, smeared drums, muffled drums, distant drums, tempo change, clipping, overdriven, "
 "harsh, abrasive, screaming, roaring, snarling, war drums, air horns, neurofunk, jump up, wobble bass, dubstep, "
 "American accent, US rap, trap, autotune, female vocal, Jamaican accent, ragga MC, BBC newsreader, "
 "narrator voice, orchestral bed, symphony orchestra, full orchestra, string section, epic trailer music, "
 "sustained string pad, ambient wash, lush pads, uplifting, comedic, novelty, parody")

CROSS = {
 'odejoy':  "pipe organ, church organ, timpani, col legno, brass stabs, square-wave bass, glockenspiel, tam-tam, "
            "male choir, gospel choir, wedding music, sentimental, easy listening",
 'mars':    "grand piano, piano ballad, tambourine, square-wave bass, brass stabs, church organ, male choir, "
            "gospel choir, amen break, handclaps, major key",
 'fate':    "grand piano, pipe organ, church organ, timpani, col legno, glockenspiel, tam-tam, tambourine, "
            "male choir, gospel choir, amen break, handclaps, major key",
 'chorale': "grand piano, timpani, col legno, glockenspiel, tam-tam, square-wave bass, brass stabs, "
            "violin stabs, tambourine, major key",
}

EXCLUDE = {k: BASE + ", " + v for k, v in CROSS.items()}

# ---- lyrics: r65's words, cues de-escalated -------------------------------
CUE_SWAPS = [
 ("[Verse 1 | a sad piano and a lone violin alone, no drums at all | gruff MC, quiet, close and bitter, three lines only]",
  "[Verse 1 | no drums at all, only the instrument the track opens on | gruff MC, quiet, close and bitter, three lines only]"),
 ("[Drop | one beat of silence, then the break and the Reese hit together on this line, the organ gone, the drums alone and enormous]",
  "[Drop | one beat of silence, then the break and the Reese hit together on this line, the opening instrument gone, the drums alone and enormous]"),
 ("[gruff MC from here, furious and hurt, fast and packed, riding the top of the break, hitting hard on every beat, never pausing mid-line]",
  "[gruff MC from here, hurt and insistent, fast and packed, riding the top of the break, landing hard on every beat, never pausing mid-line]"),
 ("[gruff MC, rising, angry, voice close to cracking]",
  "[gruff MC, rising, hurt, voice close to cracking]"),
 ("[Chorus | the hook, half sung and half shouted, a room of voices joining in over the break]",
  "[Chorus | the hook, half sung and half chanted, a room of voices joining in over the break]"),
 ("[Verse 2 | straight in, no break, the beat harder than verse one | cold MC, fast and clipped, sneering and angry, every consonant landing]",
  "[Verse 2 | straight in, no break, the beat fuller than verse one | cold MC, fast and clipped, cold and contemptuous, every consonant landing]"),
 ("[cold MC, sharper and colder, spitting the words]",
  "[cold MC, sharper and colder, biting]"),
 ("[Chorus | the beat cuts dead for the first line, one bare angry voice, then everything slams back bigger than the first chorus | half sung, half shouted]",
  "[Chorus | the beat cuts dead for the first line, one bare hurt voice, then everything slams back bigger than the first chorus | half sung, half chanted]"),
 ("[Bridge | straight in, no break, the beat at its heaviest | the two MCs trade lines fast, close and overlapping, both angry]",
  "[Bridge | straight in, no break, the beat at its heaviest | the two MCs trade lines fast, close and overlapping, both hurt]"),
 ("[Final Chorus | the biggest drop of the record, everything at once, the whole room with them | half sung, half shouted]",
  "[Final Chorus | the biggest drop of the record, everything at once, the whole room with them | half sung, half chanted]"),
]

lyrics = r65['lyrics']
for old, new in CUE_SWAPS:
    assert old in lyrics, "CUE NOT FOUND: " + old[:70]
    lyrics = lyrics.replace(old, new)

def words_only(t):
    return re.sub(r'\s+', ' ', re.sub(r'\[[^\]]*\]', '', t)).strip()

assert words_only(lyrics) == words_only(r65['lyrics']), "LYRIC WORDS CHANGED"
assert lyrics.count('\n') == r65['lyrics'].count('\n'), "LINE COUNT CHANGED"
assert 'furious' not in lyrics and 'angry' not in lyrics and 'shouted' not in lyrics

# ---- boldness check -------------------------------------------------------
def longest_common(a, b):
    best = 0
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i+k < len(a) and j+k < len(b) and a[i+k] == b[j+k]:
                k += 1
            if k > best: best = k
    return best

keys = list(STYLE)
worst = 0
for i in range(len(keys)):
    for j in range(i+1, len(keys)):
        n = longest_common(STYLE[keys[i]], STYLE[keys[j]])
        pct = 100*n/min(len(STYLE[keys[i]]), len(STYLE[keys[j]]))
        print(f"  shared {keys[i]}/{keys[j]}: {n} chars = {pct:.1f}%")
        worst = max(worst, pct)

for k in keys:
    print(f"  {k}: style={len(STYLE[k])} exclude={len(EXCLUDE[k])}")
    over = [k for k in keys if len(STYLE[k]) > 1000 or len(EXCLUDE[k]) > 1000]

assert not over, f"OVER CAP: {over}"
print(f"  worst shared = {worst:.1f}%  (cast sentence = {len(CAST)} chars)")
print(f"  lyrics lines = {lyrics.count(chr(10))+1}")

for k in keys:
    spec = {
      "style": STYLE[k],
      "exclude": EXCLUDE[k],
      "lyrics": lyrics,
      "model": "v6",
      "title": f"camping-r66-{k}",
      "workspace": "camping-Jack",
      "styleInfluence": 75,
      "weirdness": [40, 60],
      "durationSec": 175,
      "variety": "off",
      "maxMode": False,
      "vocalGender": "male",
      "personalize": False,
    }
    json.dump(spec, open(os.path.join(OUT, k + '.json'), 'w'), indent=1)
print("✅ wrote", len(keys), "specs to", OUT)
