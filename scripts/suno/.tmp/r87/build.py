import json, os, re
# r87 — Jack 2026-09-27: a reggae dubstep song from ONE reference and nothing else: Dub Zone, "Dub Reggae From the
# Roots | Organic Reggae Set & Dubwise Mix 2025" (youtube 6qtLueAbAj8, 65 min, 18 tracks). No Suno take as a base,
# no earlier prompt carried over (audited by carryover.py), every lane different, no structure cues.
# Heard by Gemini (gemini-3-flash-preview), five 60 s clips played on channel 1 (no download):
#  1:00 rockers ~70/140, militant middle-aged Jamaican singer, horn section lifts the hook, acoustic chop, organ bubble,
#       dub delay on line-ends, round deep sub · 17:00 steppers ~100, four-on-floor, tape delay on snare splashes,
#       brass synth hook · 30:00 one-drop ~82, acoustic, shaker + tambourine, folk guitar licks, male+female, very dry ·
#       43:20 steppers/ska ~140, full brass, bright and punchy, warm optimistic Caribbean singer · 56:20 one-drop 78,
#       shaker, sustained organ, flute-like lead, calm English pop singer, hall reverb, summery.
# Kept from outside the video: the Camping words (canon, byte-identical to r81/lyrics.txt) and Jack's standing
# never-double-time rule (one exclude term per lane, plus the positive pace in each voice sentence).
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
LYR=open(f'{T}/r81/lyrics.txt').read().strip()
L={
 'rockers': dict(
  style="Militant rockers reggae crossed with heavy dubstep at 140, felt at 70. Punchy dry kick on every beat, a sharp snare crack in a short plate, an acoustic guitar chopping the offbeat, a Hammond bubble ticking underneath, a brass section of trumpet and tenor sax blaring a defiant hook. Where the brass lifts, the floor splits open into a slow, enormous dubstep sub that swallows the room, then the rockers groove marches back. A middle-aged Jamaican roots singer, stern and prophetic, preaching every word with conviction, never hurrying, the tail of each line caught in quarter-note echo. Modern, clean, thick bottom end, crisp top.",
  exclude="double-time, acoustic folk, flute, synth brass, four-on-the-floor, lo-fi, tape hiss, spring reverb, siren, self-oscillating feedback"),
 'steppers': dict(
  style="UK sound system steppers, four-to-the-floor kick at 100 thudding like a heartbeat, rimshot on two and four, sixteenth hats, a monstrous sub-bass line built to shake a speaker stack, then dubstep weight: the sub slowly wobbles and growls under the steppers march. A brass synth stab answers each line, tape echo splashes off the snare, a siren wails through the breaks. A sound system deejay toasting over the riddim, chatting the words with swagger and fire, riding loose and relaxed on the pulse. Raw, heavy, near mono, built for a dance in a warehouse at three in the morning.",
  exclude="double-time, acoustic guitar, folk, flute, horn section, polished pop, hall reverb, singing, crooning, bright"),
 'barefoot': dict(
  style="Barefoot acoustic one-drop reggae at 80 that sits on a secret: a sub so deep you feel it more than hear it. Dry acoustic guitar skanking the offbeat, a second acoustic picking little folk licks, shaker and tambourine, kick and rim landing as one on beat three, no electric instruments. Under it, a dubstep sub-bass and a lumbering stomp creep in and grow until the whole campfire is shaking, then vanish. Two men trade the verses and meet on the hook, one warm and soulful, one plain and English, gentle, unhurried, close to the mic. Intimate, organic, bone dry, room sound.",
  exclude="double-time, horns, brass, synth, organ, siren, heavy wobble, growl bass, big room, electric guitar, toasting"),
 'dubwise': dict(
  style="Psychedelic dubwise, slow and heavy at 140 with a half-speed pulse, the mixing desk played like an instrument. A lazy one-drop, a rubbery sub-bass, organ chords and a flute-like lead that keep getting muted mid-phrase, spring reverb crashes, a tape echo left to feed back on itself until it screams, filters sweeping the whole band down to bass and kick. The dubstep is in the low end: a slow, deep, woozy sub wobble breathing under the echoes. A Rasta chanter, calm and trance-like, half-sung, half-spoken, drifting in and out of the echo, patient and laid back. Hazy, smoky, cavernous, analogue, full of holes and space.",
  exclude="double-time, brass section, horns, acoustic folk, four-on-the-floor, bright polished pop, big room, screeching lead, clean dry vocal"),
 'brassdrop': dict(
  style="Sunny big-band reggae meets modern dubstep, 140 bpm. Upstroke electric skank, a bouncing P-bass, a full horn section of trumpets, trombone and sax blasting bright riffs, a warm Hammond, tight bright drums. The horns set up every drop, then a crunching growl bass and huge half-time drums crash in and trade phrases with the brass, call and answer, before the sunshine returns. A soulful Caribbean singer, warm and optimistic, singing these grim words sweetly like a summer anthem, relaxed and behind the beat. Clean, bright, punchy, wide stereo, festival main stage.",
  exclude="double-time, acoustic, folk, flute, shaker, lo-fi, tape hiss, spring reverb, siren, dark ambient, toasting"),
}
for k,v in L.items():
    d=dict(model='v6',title=f'camping-r87-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[30,60],durationSec=240,
           variety='normal',maxMode=False,vocalGender='male',personalize=False,style=v['style'],exclude=v['exclude'],lyrics=LYR)
    assert '[' not in d['lyrics'] and len(d['style'])<=1000 and len(d['exclude'])<=1000, k
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(d['style']),len(d['exclude']))
