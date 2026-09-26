import json, os, re
# r85 — Jack 2026-09-26: "combining" r77 bundem take 2ffbd6b9 with "Psychedelic Desert Chill Beats" (youtube njwi8lK0jzU,
# ANATOLIAN PRODUCTION, 95 min). Four 60 s samples (2:00, 25:00, 50:00, 80:00) played + recorded, no download; heard by
# gemini-3-flash-preview (3.5-flash 429). All four agree: ~85–95 BPM swung/shuffled downtempo, plucked oud/saz lead in
# Hijaz / Phrygian-dominant over ONE drone chord, darbuka/riq/congas/shakers, round melodic sub (one sample upright bass),
# cavernous hall reverb + dub tape delay. Measured darker + wider than the take: centroid 1.2–2.2 kHz vs 3.85 kHz,
# side/mid -2..-5 dB vs -18 dB. The take (heard same way): 174 intro, reggae verses, wobble drops at 0:41/1:39/2:36,
# harsh mids, and a DOUBLE-TIME bridge at 2:08 (breaks Jack's rule — bans kept, bridge cue kept).
# Not carried: the reference's female / wordless vocals (canon casts men; words-only rule).
# Voice: r77's cast, but "gruff" -> "fiery" (Jack's r82 rule: no gravel words for Camping voices).
T='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp'; OUT=os.path.dirname(os.path.abspath(__file__))
r77=json.load(open(f'{T}/r77/bundem.json'))
LY=r77['lyrics'].replace('gruff ragga MC','fiery ragga MC')
HOOK=" The hook comes quick, a room of men saying it with him flat and low, words only. Every vocal sound is a word from the lyrics, nothing wordless anywhere. Two ragga dancehall MCs trade the verses, toasting, loud and in front, one fiery and raw, one clipped and cold, riding the slow half-time pulse, heavy and unhurried, every word clear."
EX=r77['exclude']+", brostep, screeching lead, bollywood, belly dance"
L={
 'desert-step': "Reggae dubstep at 140, half-time and swung: kick on the one, a dry cracking snare on the three, darbuka and riq rolling in the offbeats, a deep round sub walking under offbeat oud skanks. A plucked oud answers him in a Hijaz scale over one dark drone chord. Snare rolls build into drops where the sub swells into a slow, heavy, rounded wobble, then back to the riddim. Cavernous hall reverb, long tape echo on his line-ends, a dub breakdown to end."+HOOK,
 'desert-downtempo': "Psychedelic desert dub at 90, trip hop downtempo with a lazy swung shuffle: a muffled deep kick, a woody snare, darbuka, riq and shakers, a round melodic sub under a plucked oud playing Hijaz runs over one hypnotic drone chord. The bass swells into a heavy half-time dubstep weight for the hook, then falls back. Cavernous hall reverb, long dub tape echo, dusty, dark, wide and slow."+HOOK,
}
for k,s in L.items():
    d=dict(model='v6',title=f'camping-r85-{k}',workspace='camping-Jack',styleInfluence=75,weirdness=[40,60],durationSec=240,
           variety='off',maxMode=False,vocalGender='male',personalize=False,style=s,exclude=EX,lyrics=LY)
    for w in ('gravel','gruff','hoarse','rasp','bark','growl'):
        assert w not in (s+LY).lower(), (k,w)
    for w in ('oud','darbuka','riq','dubstep','reverb','hall','drone','trip hop','shaker'):  # nothing asked for is banned
        assert w not in [x.strip() for x in EX.split(',')], (k,w)
    assert re.sub(r'\[[^\]]*\]','',LY)==re.sub(r'\[[^\]]*\]','',r77['lyrics'])  # words identical
    assert len(s)<=1000 and len(EX)<=1000
    json.dump(d,open(f'{OUT}/{k}.json','w'),indent=1); print(k,len(s),len(EX))
