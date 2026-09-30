"""r65 — the tunnel fix: the drum and bass back in front, the anger back in the voice, the drop
placed with silence in front of it, and the pace bracketed on the one lever we can prove.

Brief (Jack, 2026-09-22): *"it is an angry song, with emotion in the voice, just not too aggressive,
dont lose completely. camping-r64-tunnel-v6-w60 this one is not bad, it needs work. The drum and
bass has gone basically, it needs to drop on 'you keep on walking, through that Wait trose door'.
And then the grime rapping needs to stay fast and keep up with the pace of the drum and bass."*

Single-variable round. The style fix is constant across every cell; the ONE thing that varies is
Duration, because Duration is the only pacing lever this song has ever proved obeyed.

🔴 FOUR CAUSES OF "THE DRUM AND BASS HAS GONE", ALL WRITTEN BY US IN r64:

  1. The drums were described as soft. `a time-stretched break smeared and pitched down, layered
     three deep` is Valley of the Shadows' technique, but as a PROMPT it reads "blur the drums".
     -> the drums now lead the box: fast chopped amen breaks, snares cracking dry and close.
  2. The production sentence killed it. `Stone-room reverb, enormous and cold, patient rather than
     violent`. Our own rule: mix and production language decides how a record sounds. "Patient
     rather than violent" is an instruction to not be drum and bass.
     -> `Dry, close and loud, the room only on the organ.`
  3. 🔴 WE BANNED THE BASS. `distorted bass` was in r64's exclude list. A REESE IS A DISTORTED BASS,
     and Jack's own favourite take (1127446d) is r19 `reese`. Fifth ban found fighting the brief,
     and the first one we wrote ourselves in the same round we broke.
  4. `a vast round sub with no distortion on it` positively instructed a characterless bass.

🔴 TWO CAUSES OF "THE RAPPING NEEDS TO STAY FAST":

  1. `one syllable to the beat on the 174 grid, never rushed` = 2.9 syllables/sec, a slow rap. DnB's
     perceived pulse is half-time (87) while the drums sprint at 174 - so "one syllable to the 174
     beat" reads to the model as the SLOW pulse. The MC should ride the fast top of the break.
  2. 🔴 DURATION 200 s. The sheet already ruled 195 s "too slow" at r55. r64 ran SLOWER than the
     value already judged too slow. -> bracketed at 175 s and 190 s, r56's measured pair.

🔑 WHY THE DROP DIDN'T LAND. The `[Drop]` tag is there (r60 placed it, r64 kept it). What was missing
is the CONTRAST: a drop hits because of what is removed before it, not what arrives at it. So gear
one is organ alone with NO bass anywhere, then one beat of silence, then break and Reese together
with the organ GONE - two reveals on one beat, and the thing that arrives is the drums by themselves.

🔑 ANGER BACK IN THE VOICE, NOT IN THE PRODUCTION. Jack: "angry, with emotion in the voice, just not
too aggressive." That is exactly the r61 split - aggression comes from DELIVERY, not from distortion
or from more syllables. So r43's proven cast sentence goes back in VERBATIM AND ENTIRE (the back half
was flagged in r64 as the first line to restore), while `clipping, overdriven, war drums, air horns,
screaming, roaring` stay banned. Angry voice, clean record.
"""
import json, pathlib, re

REPO = pathlib.Path('/home/jackt/projects/badcode/badcode')
OUT = REPO / 'scripts/suno/.tmp/r65'
CANON = REPO / 'docs/stories/camping/songs/camping.md'

# ── start from r64's lyric block (r61 words, de-escalated cues) and put the anger back ──────────
md = CANON.read_text()
start = md.index('### r64 lyrics (shared')
LYR = re.search(r'```lyrics\n(.*?)\n```', md[start:start + 8000], re.S).group(1)
assert 'you keep on walking' in LYR and 'shatoe nerf doo pap' in LYR

STYLE = (
    # 1. FRONT-LOADED: the drums are the first thing the model reads. Front-loading is the
    #    documented fix for an element that got ignored.
    "Heavy rolling UK drum and bass, 174 BPM, D minor, grime over it: the drums are the record, "
    "fast chopped amen breaks, snares cracking dry and close, hats sprinting, a filthy Reese "
    "growing meaner every section. "
    # 2. gear one - and the thing that makes a drop work is what is ABSENT here
    "It opens with no drums: a cathedral pipe organ alone on a slow falling figure, the first MC "
    "close and bitter for three lines, no bass at all. "
    # 3. the drop, placed, with silence in front of it and the organ removed at it
    "Then one beat of silence and the break and the Reese hit together on 'you keep on walking', "
    "the organ gone, the drums alone and enormous. "
    # 4. the four-cycle shape, with the quiet parts actually quiet
    "It cuts to almost nothing and slams back three more times, each bigger; the quiet parts "
    "really quiet. "
    # 5. the organ demoted to a garnish at the turns (Ruling 1) + the balance stated
    "Under the rap the organ returns only at the turns, a low pedal note and a siren; drums and "
    "bass far louder. "
    # 6. production - the sentence that decides the record
    "Dry, close and loud, reverb only on the organ, night-bus melancholy. "
    # 7. 🔑 r43's proven cast sentence, verbatim and ENTIRE - the emotion half restored
    "Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and "
    "cold, both spitting fast, furious and emotional, voices close to cracking, rapid-fire on the "
    "174 grid and never slowing for a punchline."
)

EXCLUDE = (
    # the too-fast end stays banned - r55 proved `double-time` + 155 s is "way too fast"
    "double-time, chopper rap, motormouth, auctioneer delivery, breathless, "
    # 🔴 `rapid-fire` is NOT banned any more: it is r43's own word for the liked delivery, and it is
    #    in the cast sentence above. Banning it was banning the brief.
    # the too-slow end, reinforced - this is the fault being fixed
    "steady rap pace, measured recital, lazy flow, slow flow, half-time flow, chill, laid-back, "
    "rapping behind the beat, off-grid vocal, spoken word, "
    # 🆕 the "where did the drum and bass go" bans, naming the r64 failure directly
    "downtempo, trip hop, half time, half-time drums, sparse percussion, drumless, beatless, "
    "ambient, soundtrack, underscore, slow build, washed out, smeared drums, muffled drums, "
    "distant drums, "
    # grid guards
    "tempo change, drifting tempo, rubato, "
    # 🔑 the aggression stays banned in the PRODUCTION only - never in the voice
    "clipping, overdriven, war drums, air horns, screaming, roaring, barking, hardcore, "
    "neurofunk, jump up, wobble bass, dubstep, "
    # cast guards
    "American accent, American vocal, US rap, trap, boom bap, autotune, female vocal, teenage "
    "voice, falsetto, Jamaican accent, ragga MC, male choir, BBC newsreader, posh storyteller, "
    "narrator voice, "
    # Ruling 1 - classical is a garnish. Bed scale only; `pipe organ` stays UNBANNED, it is the lane
    "orchestral bed, symphony orchestra, full orchestra, string section, chamber music, epic "
    "trailer music, sustained string pad, ambient wash, lush pads, static arrangement, "
    # register
    "major key, happy, uplifting, comedic, novelty, parody"
)

# ── the cues: the anger back, the drop given its silence, the flow told to keep up ──────────────
CUES = [
    ("[Drop | the bass and the break arrive together on this line, the first full weight of the record]",
     "[Drop | one beat of silence, then the break and the Reese hit together on this line, the organ gone, the drums alone and enormous]"),
    ("[gruff MC from here, weary and direct, landing one syllable on each beat, hitting hard without raising his voice]",
     "[gruff MC from here, furious and hurt, fast and packed, riding the top of the break, hitting hard on every beat, never pausing mid-line]"),
    ("[gruff MC, lifting, more insistent, still controlled]",
     "[gruff MC, rising, angry, voice close to cracking]"),
    ("[gruff MC, a quiet bitter plea]",
     "[gruff MC, a bitter plea, voice breaking]"),
    ("[Chorus | the hook, sung, a room of voices joining in over the break]",
     "[Chorus | the hook, half sung and half shouted, a room of voices joining in over the break]"),
    ("[Verse 2 | straight in, no break, the arrangement fuller than verse one | cold MC, clipped, precise and contemptuous, every consonant landing]",
     "[Verse 2 | straight in, no break, the beat harder than verse one | cold MC, fast and clipped, sneering and angry, every consonant landing]"),
    ("[cold MC, sharper and colder, biting]",
     "[cold MC, sharper and colder, spitting the words]"),
    ("[Chorus | the beat cuts dead for the first line, one bare voice, then everything returns fuller than the first chorus | sung]",
     "[Chorus | the beat cuts dead for the first line, one bare angry voice, then everything slams back bigger than the first chorus | half sung, half shouted]"),
    ("[Bridge | straight in, no break, the arrangement at its fullest | the two MCs trade lines, close and overlapping]",
     "[Bridge | straight in, no break, the beat at its heaviest | the two MCs trade lines fast, close and overlapping, both angry]"),
    ("[Final Chorus | the biggest moment of the record, everything at once, the whole room singing it | sung]",
     "[Final Chorus | the biggest drop of the record, everything at once, the whole room with them | half sung, half shouted]"),
]

LY = LYR
for a, b in CUES:
    assert a in LY, 'NO-OP replace (cue not found): ' + a[:80]
    LY = LY.replace(a, b)

words = lambda t: "\n".join(l for l in t.split("\n") if not l.strip().startswith('['))
assert words(LY) == words(LYR), 'A LYRIC WORD CHANGED - verbatim rule broken'
assert 'roar' not in LY.lower(), 'roaring is the too-far end and stays out of the cues'
assert 'one beat of silence' in LY and 'the organ gone' in LY, 'the drop lost its contrast'

assert len(STYLE) <= 1000, ('style', len(STYLE), 'OVER BY', len(STYLE) - 1000)
assert len(EXCLUDE) <= 1000, ('exclude', len(EXCLUDE), 'OVER BY', len(EXCLUDE) - 1000)
# the r64 faults must not survive into r65
for gone in ('smeared', 'patient rather than violent', 'no distortion', 'one syllable to the beat'):
    assert gone not in STYLE, 'an r64 fault survived in the style box: ' + gone
assert 'distorted bass' not in EXCLUDE, 'the Reese ban came back'
assert 'rapid-fire' not in EXCLUDE and 'rapid-fire' in STYLE, 'rapid-fire must be asked for, not banned'
assert 'pipe organ' not in EXCLUDE and 'pipe organ' in STYLE

OUT.mkdir(parents=True, exist_ok=True)
for dur in (175, 190):
    (OUT / f'd{dur}.json').write_text(json.dumps({
        "style": STYLE, "exclude": EXCLUDE, "lyrics": LY,
        "model": "v6",
        "title": f"camping-r65-tunnel2-d{dur}",
        "workspace": "camping-Jack",
        "styleInfluence": 75,
        "weirdness": [40, 60],
        "durationSec": dur,
        "variety": "off",
        "maxMode": False,
        "vocalGender": "male",
        "personalize": False,
    }, indent=2))

print(f"style   = {len(STYLE)}")
print(f"exclude = {len(EXCLUDE)}")
print(f"lyrics  = {len(LY)} chars, {len([l for l in LY.split(chr(10)) if l.strip()])} lines")
print("cells   = d175/d190 x w40/w60 = 4 Creates, 8 takes")
