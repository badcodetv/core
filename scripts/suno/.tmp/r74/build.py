import json, re, os
BASE='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r71/wordsonly.json'
OUT=os.path.dirname(os.path.abspath(__file__))
prev=json.load(open(BASE))

# The 0:11-0:21 passage of 36d0b981, as heard (docs/listening/log/2026-09-24-092430-...): one-drop
# at ~87, rim on the three, warm walking sub, offbeat organ skank, dark top, feedback delay + hall on
# the line-ends. The cast sentence is r71's verbatim — it made the voice Jack likes.
STYLE=("One-drop reggae riddim at 87 with ragga swing: a soft rim click on the three, "
 "a deep warm round sub walking a syncopated line, a clean warm organ skanking on every offbeat. "
 "Dark and warm, the top end rolled off, the ends of his lines thrown into feedback delay "
 "and a big hall reverb, plenty of space between his phrases, like a sound system taped off the desk. "
 "It opens on organ, sub and rim click alone with him quiet and begging, and the full riddim comes in on "
 "'you keep on walking'. The riddim drops out and slams back in at the turns. "
 "The hook comes quick, a room of men saying it with him flat and low, words only. Every vocal "
 "sound is a word from the lyrics, nothing wordless anywhere. "
 "Two English grime MCs trade the verses, loud and in front, one gruff and raw, one clipped and cold, "
 "eight-bar bursts traded between them, heavy and unhurried, every bar landing clean and on the grid, never "
 "hurried and never dragging.")

# Inherited bans audited: dropped `slow tempo, half time, slow flow, lazy flow, church organ` (each bans
# the passage itself). Added the jungle/D&B family (the drop is what he is asking to lose) and reggae's
# own SINGER family (genre names the music, not the voice). Toasting / ragga MC deliberately NOT banned:
# the passage's voice may be exactly that.
EXCLUDE=("ooh, oohs, ahhs, wordless vocals, vocal ad-libs, hype man, crowd shouts, whoops, vocal riffs, "
 "sung harmonies, shouting, screaming, roaring, American accent, US rap, trap, autotune, "
 "pitch-corrected vocals, female vocal, cheesy, steady rap pace, double-time, motormouth, major key, "
 "tempo change, happy, uplifting, glossy production, drum and bass, jungle, amen break, breakbeat, "
 "rolling breaks, snare roll, risers, build-up, EDM drops, reese bass, distorted bass, growl bass, "
 "neurofunk, jump up, wobble bass, dubstep, roots reggae singer, crooning, sung melody, lovers rock, "
 "reggaeton, tropical house, ska, brass band, oompah, orchestral bed, symphony orchestra, string section, "
 "grand piano")

def wo(t): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',t)).strip()
R=[("[Verse 1 | no drums yet | gruff grime MC, close and bitter]",
    "[Verse 1 | organ, sub and rim click only | gruff grime MC, quiet, close and begging, unhurried]"),
   ("[Drop | the amen drops on this line]", "[the full riddim comes in on this line]"),
   ("[Verse 2 | straight in, no break | cold grime MC, clipped and cold, fast and clear]",
    "[Verse 2 | straight in, no break | cold grime MC, clipped and cold, heavy and unhurried, every word clear]")]
lyr=prev['lyrics']
for a,b in R:
    assert lyr.count(a)==1, a
    lyr=lyr.replace(a,b)
assert wo(lyr)==wo(prev['lyrics']) and lyr.count('\n')==prev['lyrics'].count('\n')
for bad in ['amen','jungle','174','fast']:
    cues=' '.join(re.findall(r'\[[^\]]*\]',lyr)).lower()
    assert bad not in STYLE.lower() and bad not in cues, bad
print(f"style={len(STYLE)} exclude={len(EXCLUDE)} lyrics={len(lyr)}")
assert len(STYLE)<=1000 and len(EXCLUDE)<=1000
for dur in (190,230):
    json.dump({"style":STYLE,"exclude":EXCLUDE,"lyrics":lyr,"model":"v6",
      "title":f"camping-r74-onedrop{dur}","workspace":"camping-Jack","styleInfluence":75,
      "weirdness":[40,60],"durationSec":dur,"variety":"off","maxMode":False,
      "vocalGender":"male","personalize":False}, open(os.path.join(OUT,f"onedrop{dur}.json"),'w'), indent=1)
print("✅ r74: 2 specs, identical boxes, Duration 190 vs 230")
