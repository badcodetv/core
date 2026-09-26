import json, os
# r79 — Jack 2026-09-26 on 3a433539 (= camping-r77-jamrock-v6-w40): likes it; try fusing the reggae
# with modern POP to modernise it / make it more palatable. Three lanes, frozen vocal spine, r77 lyrics
# byte-identical, lane clause first. Web research 2026-09-26: keep to the DARK/minor fusions (trap
# dancehall, Controlla, Lean On); pop-reggae (MAGIC!) and tropical house are major and beachy, and
# Listen of 3a433539 (docs/listening/log/2026-09-26-113303-…): dated = dull recessed top end, near-mono
# (corr 0.973), thin dry MIDI brass. Gemini's own pop advice (autotune, vocal chops, 16th-note hat rolls)
# is REJECTED — house rules: no autotune, nothing wordless, never double-time.
# guides say a bare "reggae pop" genre word waters down — so the pop comes mostly from production words.
R77='/home/jackt/projects/badcode/badcode/scripts/suno/.tmp/r77'
OUT=os.path.dirname(os.path.abspath(__file__))
src=json.load(open(f'{R77}/jamrock.json'))
SPINE=("The hook comes quick, a room of men saying it with him flat and low, words only. "
       "Every vocal sound is a word from the lyrics, nothing wordless anywhere. "
       "Two ragga dancehall MCs trade the verses, toasting, loud and in front, one gruff and raw, "
       "one clipped and cold, riding the slow half-time pulse, heavy and unhurried, every word clear.")
assert src['style'].count(SPINE)==1 and src['style'].endswith(SPINE)
R77_BED=src['style'][:src['style'].index(SPINE)].strip()
LANES={
 # A — smallest step: r77's riddim verbatim + pop PRODUCTION words only, no pop genre word.
 'poppolish': (R77_BED + " Polished radio-ready mix, crisp punchy compressed drums, the sub loud and round, "
   "a crisp open top end, wide stereo, a dark minor-key synth pluck hooking the loop, a wide warm pad "
   "lifting under every hook."),
 # B — dancehall pop (Shape of You / Work tempo), kept dark and minor. The only lane with the word "pop" as genre.
 'dancehallpop': ("Dark minor-key dancehall pop at 96: a bouncing dancehall drum pattern, tight snappy claps, "
   "a deep booming 808 sub, a moody marimba and plucked mallet riff looping in a minor key, "
   "sidechained synth chords pumping on the offbeat, crisp, polished and modern. A dub siren sweeps in at "
   "every section, tape delay thrown off his line-ends. A church organ answers at the turns."),
 # C — trap dancehall (Skillibeng / Controlla register): modern drums, still dark and minor.
 'trapdancehall': ("Dark trap dancehall at 92, half-time: a hard 808 sub gliding under the tune, a dancehall "
   "kick and snare bounce, crisp trap hi-hats kept steady and sparse, sidechained minor-key synth chords, "
   "a dark plucked mallet riff, a polished modern mix, loud and wide. Dub siren at every section, "
   "tape delay on his line-ends. A church organ answers at the turns."),
}
exc=src['exclude'].replace(', glossy production','')   # polish is what's being asked for
assert exc!=src['exclude']
exc+=', steel drums, ukulele, pan flute, beach, summer vibes, calypso'
for k,bed in LANES.items():
    d=dict(src); d['style']=bed+' '+SPINE
    d['exclude']=exc.replace(', trap,',',') if k=='trapdancehall' else exc   # trap IS that lane
    d['title']=f'camping-r79-{k}'
    assert d['lyrics']==src['lyrics']
    assert d['style'].endswith(SPINE) and d['style'].count(SPINE)==1
    assert len(d['style'])<=1000 and len(d['exclude'])<=1000, (k,len(d['style']),len(d['exclude']))
    json.dump(d, open(f'{OUT}/{k}.json','w'), indent=1)
    print(k, len(d['style']), len(d['exclude']), 'trap-banned' if ', trap,' in d['exclude'] else 'trap-allowed')
