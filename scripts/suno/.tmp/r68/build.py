import json, re, os
SRC='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r67/answer.json'
OUT=os.path.dirname(os.path.abspath(__file__))
r67=json.load(open(SRC))

CAST=("Two English grime MCs trade the verses, loud and in front, "
      "one gruff and raw, one clipped and cold, ")
TAIL=("aggressive but held back, low and murky, menace not volume, never raising their voices, "
      "fast and clear.")

HEAD=("UK grime MCs over jungle drum and bass, 174 BPM, D minor: chopped amen breaks, a deep round sub, "
      "handclaps, hats brushed back. ")
MID =("A beat of silence, then break and sub arrive on 'you keep on walking', controlled rather than louder; it falls to almost nothing and returns three more times, the quiet parts really quiet. ")
FOOT=("A church organ at the turns only. The room answers him low and close, half-spoken in unison, a pub not "
      "a stadium. Mixed with headroom, never brickwalled. ")

OPEN={
 'violin':"Opens with no drums: a felt piano on a slow falling figure, a lone violin over it, first MC close "
          "for three lines. ",
 'pizz':  "Opens with no drums: a felt piano on a slow falling figure, plucked cellos ticking under it, first "
          "MC close for three lines. ",
 'cello': "Opens with no drums: a felt piano on a slow falling figure, one low cello under it, first MC close "
          "for three lines. ",
}
ORCH={
 'violin':"The violin stays right through with a job: answering the MC at the end of every bar, "
          "doubling the bassline an octave up in the drops. Drums and sub loudest, piano and violin under "
          "them, never in front. ",
 'pizz':  "The plucked strings stay right through with a job: playing the break's own pattern back in short "
          "sixteenths, percussion not melody. Drums and sub loudest, piano and strings "
          "under them, never in front. ",
 'cello': "The cellos stay right through with a job: long bowed lines doubling the sub an octave up, "
          "weight from register not volume. Drums and sub loudest, piano and cellos "
          "under them, never in front. ",
}
STYLE={k: HEAD+OPEN[k]+MID+ORCH[k]+FOOT+CAST+TAIL for k in OPEN}

BASE=("autotune, pitch-corrected vocals, tuned vocals, vocoder, stacked harmonies, layered vocals, "
 "vocal doubles, gospel choir, EDM vocal, pop hook, anthemic chorus, singalong, football chant, cheesy, corny, "
 "stadium rock, euphoric, shouting, shouted vocals, hollering, bellowing, screaming, roaring, "
 "brickwalled, over-compressed, maximised, loudness war, wall of sound, sizzling hats, sibilant, harsh, "
 "abrasive, buried vocals, distant vocal, drowned in the mix, heavy vocal reverb, mumbled, double-time, "
 "chopper rap, motormouth, breathless, steady rap pace, lazy flow, slow flow, spoken word, trip hop, "
 "half-time drums, sparse percussion, drumless, slow build, distant drums, neurofunk, jump up, "
 "American accent, US rap, trap, female vocal, Jamaican accent, ragga MC, BBC newsreader, orchestral bed, "
 "symphony orchestra, string section, sustained string pad, lush pads, epic trailer music, major key")
CROSS={
 'violin':"pizzicato, plucked strings, cello section, upright bass",
 'pizz':  "solo violin, violin melody, legato strings, cello section",
 'cello': "pizzicato, plucked strings, solo violin, violin melody",
}
EXCLUDE={k: BASE+", "+CROSS[k] for k in OPEN}

SWAPS=[
 ("[Chorus | the gruff grime MC says each line, the room barks the last three words back flat and in unison, nobody sings]",
  "[Chorus | the gruff grime MC says each line, the room answers the last three words back low and close, half-spoken in unison, nobody sings and nobody shouts]"),
 ("[Chorus | the beat cuts dead for the first line, one bare hurt voice, then everything slams back bigger than the first chorus | the room barking the answers back, nobody sings]",
  "[Chorus | the beat cuts dead for the first line, one bare hurt voice, then everything returns fuller than the first chorus | the room answering low and close, nobody sings and nobody shouts]"),
 ("[Final Chorus | the biggest drop of the record, everything at once, the whole room barking every line straight back at him, nobody sings]",
  "[Final Chorus | the fullest moment of the record, everything at once, the whole room answering every line straight back at him low and close, nobody sings and nobody shouts]"),
 ("[gruff grime MC from here, hurt and insistent, fast but every word clear, riding the top of the break, landing hard on every beat, never rushing and never pausing mid-line]",
  "[gruff grime MC from here, hurt and insistent, aggressive but held back, low and murky, fast but every word clear, landing hard on every beat without raising his voice, never rushing and never pausing mid-line]"),
 ("[gruff grime MC, rising, hurt, voice close to cracking]",
  "[gruff grime MC, more insistent, hurt, voice close to cracking but never shouting]"),
 ("[Verse 2 | straight in, no break, the beat fuller than verse one | cold grime MC, fast but every word clear, clipped, cold and contemptuous, every consonant landing]",
  "[Verse 2 | straight in, no break, the beat fuller than verse one | cold grime MC, fast but every word clear, clipped, cold and contemptuous, quiet menace rather than volume, every consonant landing]"),
 ("[Bridge | straight in, no break, the beat at its heaviest | the two grime MCs trade lines fast and clear, close and overlapping, both hurt]",
  "[Bridge | straight in, no break, the beat at its fullest | the two grime MCs trade lines fast and clear, close and overlapping, both hurt, neither raising his voice]"),
 ("[Verse 1 | no drums and no instruments at all | gruff grime MC, quiet, close and bitter, three lines only]",
  "[Verse 1 | no drums, only the piano and the strings the track opens on | gruff grime MC, quiet, close and bitter, three lines only]"),
 ("[Drop | one beat of silence, then the break and the Reese hit together on this line, the opening voices gone, the drums alone and enormous]",
  "[Drop | one beat of silence, then the break and the Reese arrive together on this line, whole and controlled rather than louder]"),
]
def words_only(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
l=r67['lyrics']
for a,b in SWAPS:
    assert a in l, "CUE NOT FOUND: "+a[:70]
    l=l.replace(a,b)
assert words_only(l)==words_only(r67['lyrics']), "LYRIC WORDS CHANGED"
assert l.count('\n')==r67['lyrics'].count('\n')
for bad in ['barking','barks','enormous','slams back']: assert bad not in l, f"survived: {bad}"
assert l.count('grime MC')>=12
for k in EXCLUDE:
    assert 'air horns' not in EXCLUDE[k] and 'snarling' not in EXCLUDE[k], f"{k}: lifted ban still present"

keys=list(OPEN)
for k in keys: print(f"  {k}: style={len(STYLE[k])} exclude={len(EXCLUDE[k])}")
over=[k for k in keys if len(STYLE[k])>1000 or len(EXCLUDE[k])>1000]
assert not over, f"OVER CAP: {over}"
for k in keys:
    json.dump({"style":STYLE[k],"exclude":EXCLUDE[k],"lyrics":l,"model":"v6",
      "title":f"camping-r68-{k}","workspace":"camping-Jack","styleInfluence":75,
      "weirdness":[40,60],"durationSec":185,"variety":"off","maxMode":False,
      "vocalGender":"male","personalize":False}, open(os.path.join(OUT,k+'.json'),'w'), indent=1)
print("✅ wrote", len(keys), "specs · lyric lines", l.count(chr(10))+1)
