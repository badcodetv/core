import json, re, os

SRC = '/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r66/chorale.json'
OUT = os.path.dirname(os.path.abspath(__file__))
r66 = json.load(open(SRC))

CAST = ("Two English grime MCs trade the verses, loud and in front, "
        "one gruff and raw, one clipped and cold, ")
TAIL = "both spitting fast but every word clear, never rushing and never slowing for a punchline."

HEAD = ("UK grime MCs over jungle drum and bass, 174 BPM, D minor: breakneck chopped amen breaks, a deep round "
        "sub, handclaps on the backbeat. ")
MID  = ("A beat of silence, then amen and sub hit on 'you keep on walking', the voices gone, the drums alone "
        "and enormous. It empties and slams back three more times. ")
FOOT = ("A church organ holds chords at the turns only. Drums and sub loudest, voices under them, never in "
        "front. Big, clean and open, nobody screaming. Vocals bone dry and right at the front, above the drums, "
        "every word audible. London pirate-radio energy. ")

OPEN = {
 'terrace': "Opens with no drums and no instruments: a crowd of men chanting the hook on one flat note, dry "
            "and untuned, then the first MC close for three lines. ",
 'answer':  "Opens with no drums and no instruments: one MC says the hook flat and close, a room barking the last "
            "three words back, then three lines more. ",
 'raw':     "Opens with no drums and no instruments: one man alone singing the hook rough, flat and cracked, "
            "nobody with him, then the first MC close for three lines. ",
}
HOOK = {
 'terrace': "Every hook is that crowd on one flat note in unison, shouted not sung, never harmonised, never "
            "tuned. ",
 'answer':  "Across the record the room answers him: he lands a line, they bark one word back flat in unison. "
            "Nobody sings a note. ",
 'raw':     "Every hook is that one man alone, no voices behind him, no harmony; the lift comes from the drums. ",
}

STYLE = {k: HEAD + OPEN[k] + MID + HOOK[k] + FOOT + CAST + TAIL for k in OPEN}

BASE = ("autotune, pitch-corrected vocals, tuned vocals, vocoder, stacked harmonies, layered vocals, "
 "vocal doubles, gospel choir, EDM vocal, pop hook, anthemic chorus, singalong, cheesy, buried vocals, "
 "distant vocal, drowned in the mix, heavy vocal reverb, mumbled, double-time, chopper rap, motormouth, "
 "breathless, steady rap pace, lazy flow, slow flow, spoken word, trip hop, half-time drums, "
 "sparse percussion, drumless, slow build, distant drums, harsh, abrasive, screaming, roaring, snarling, "
 "air horns, neurofunk, jump up, American accent, US rap, trap, female vocal, Jamaican accent, ragga MC, "
 "BBC newsreader, orchestral bed, symphony orchestra, string section, major key")

CROSS = {
 'terrace': "sung chorus melody, lead singer, crooning, vibrato, falsetto",
 'answer':  "sung chorus melody, lead singer, crooning, vibrato, falsetto",
 'raw':     "male choir, crowd vocals, gang vocals, group vocals, audience chant",
}
EXCLUDE = {k: BASE + ", " + CROSS[k] for k in OPEN}

# ---- lyrics ---------------------------------------------------------------
BASE_SWAPS = [
 ("[Verse 1 | no drums at all, only the instrument the track opens on | gruff MC, quiet, close and bitter, three lines only]",
  "[Verse 1 | no drums and no instruments at all | gruff grime MC, quiet, close and bitter, three lines only]"),
 ("[Drop | one beat of silence, then the break and the Reese hit together on this line, the opening instrument gone, the drums alone and enormous]",
  "[Drop | one beat of silence, then the break and the Reese hit together on this line, the opening voices gone, the drums alone and enormous]"),
 ("[gruff MC from here, hurt and insistent, fast and packed, riding the top of the break, landing hard on every beat, never pausing mid-line]",
  "[gruff grime MC from here, hurt and insistent, fast but every word clear, riding the top of the break, landing hard on every beat, never rushing and never pausing mid-line]"),
 ("[gruff MC, rising, hurt, voice close to cracking]",
  "[gruff grime MC, rising, hurt, voice close to cracking]"),
 ("[gruff MC, a bitter plea, voice breaking]",
  "[gruff grime MC, a bitter plea, voice breaking]"),
 ("[Verse 2 | straight in, no break, the beat fuller than verse one | cold MC, fast and clipped, cold and contemptuous, every consonant landing]",
  "[Verse 2 | straight in, no break, the beat fuller than verse one | cold grime MC, fast but every word clear, clipped, cold and contemptuous, every consonant landing]"),
 ("[cold MC, sharper and colder, biting]", "[cold grime MC, sharper and colder, biting]"),
 ("[Bridge | straight in, no break, the beat at its heaviest | the two MCs trade lines fast, close and overlapping, both hurt]",
  "[Bridge | straight in, no break, the beat at its heaviest | the two grime MCs trade lines fast and clear, close and overlapping, both hurt]"),
 ("[gruff MC]", "[gruff grime MC]"),
 ("[cold MC]", "[cold grime MC]"),
 ("[both MCs together]", "[both grime MCs together]"),
]
CHORUS_SWAPS = {
 'terrace': [
  ("[Chorus | the hook, half sung and half chanted, a room of voices joining in over the break]",
   "[Chorus | the hook chanted flat on one note by a crowd of men, dry and untuned, shouted not sung, no harmony]"),
  ("[Chorus | the beat cuts dead for the first line, one bare hurt voice, then everything slams back bigger than the first chorus | half sung, half chanted]",
   "[Chorus | the beat cuts dead for the first line, one bare hurt voice, then everything slams back bigger than the first chorus | the crowd back in, chanted flat on one note, no harmony]"),
  ("[Final Chorus | the biggest drop of the record, everything at once, the whole room with them | half sung, half chanted]",
   "[Final Chorus | the biggest drop of the record, everything at once, the whole crowd chanting it flat on one note, no harmony and no tuning]"),
 ],
 'answer': [
  ("[Chorus | the hook, half sung and half chanted, a room of voices joining in over the break]",
   "[Chorus | the gruff grime MC says each line, the room barks the last three words back flat and in unison, nobody sings]"),
  ("[Chorus | the beat cuts dead for the first line, one bare hurt voice, then everything slams back bigger than the first chorus | half sung, half chanted]",
   "[Chorus | the beat cuts dead for the first line, one bare hurt voice, then everything slams back bigger than the first chorus | the room barking the answers back, nobody sings]"),
  ("[Final Chorus | the biggest drop of the record, everything at once, the whole room with them | half sung, half chanted]",
   "[Final Chorus | the biggest drop of the record, everything at once, the whole room barking every line straight back at him, nobody sings]"),
 ],
 'raw': [
  ("[Chorus | the hook, half sung and half chanted, a room of voices joining in over the break]",
   "[Chorus | one man alone singing the hook rough, flat and cracked, no other voices and no harmony]"),
  ("[Chorus | the beat cuts dead for the first line, one bare hurt voice, then everything slams back bigger than the first chorus | half sung, half chanted]",
   "[Chorus | the beat cuts dead for the first line, then everything slams back bigger than the first chorus | still the one raw cracked voice, alone, no harmony]"),
  ("[Final Chorus | the biggest drop of the record, everything at once, the whole room with them | half sung, half chanted]",
   "[Final Chorus | the biggest drop of the record, everything at once behind him, but still one raw cracked voice on top, alone and untuned]"),
 ],
}

def words_only(t):
    return re.sub(r'\s+', ' ', re.sub(r'\[[^\]]*\]', '', t)).strip()

LYR = {}
for k in OPEN:
    l = r66['lyrics']
    for old, new in BASE_SWAPS + CHORUS_SWAPS[k]:
        assert old in l, f"{k}: CUE NOT FOUND: {old[:70]}"
        l = l.replace(old, new)
    assert words_only(l) == words_only(r66['lyrics']), f"{k}: LYRIC WORDS CHANGED"
    assert l.count('\n') == r66['lyrics'].count('\n'), f"{k}: LINE COUNT CHANGED"
    assert 'half sung' not in l and 'half chanted' not in l, f"{k}: old hook cue survived"
    assert l.count('grime MC') >= 12, f"{k}: grime labels not applied"
    LYR[k] = l

keys = list(OPEN)
for k in keys:
    print(f"  {k}: style={len(STYLE[k])} exclude={len(EXCLUDE[k])} lyricLines={LYR[k].count(chr(10))+1}")
over = [k for k in keys if len(STYLE[k]) > 1000 or len(EXCLUDE[k]) > 1000]
assert not over, f"OVER CAP: {over}"

for k in keys:
    json.dump({
      "style": STYLE[k], "exclude": EXCLUDE[k], "lyrics": LYR[k],
      "model": "v6", "title": f"camping-r67-{k}", "workspace": "camping-Jack",
      "styleInfluence": 75, "weirdness": [40, 60], "durationSec": 185,
      "variety": "off", "maxMode": False, "vocalGender": "male", "personalize": False,
    }, open(os.path.join(OUT, k + '.json'), 'w'), indent=1)
print("✅ wrote", len(keys), "specs")
