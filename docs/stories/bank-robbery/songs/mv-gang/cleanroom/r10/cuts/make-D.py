"""Cut D, "Breathing": long held phrases, punctuated by short crew-rapping bursts on the hooks.
python3 make-D.py  -> plan-D.json"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
mm = json.load(open(HERE / 'music-map.json'))
B = mm['beats']
GRID = sorted(set(B + [round((a + b) / 2, 3) for a, b in zip(B, B[1:])]))
END = mm['end']

def snap(t):
    g = min(GRID, key=lambda x: abs(x - t))
    assert abs(g - t) < 0.2, (t, g)
    return g

def line_at(t0, t1):
    # the sung line(s) heard during this shot
    hit = [l['text'] for l in mm['lines'] if 'Music' not in l['text'] and l['start_snapped'] < t1 - 0.15 and l['end'] > t0 + 0.15]
    return ' / '.join(hit)

S = []  # (start, clip, in, why)
def hold(t, clip, i, why):
    S.append((t, clip, i, why))
def burst(t0, t1, clips, why):
    # spread the cuts evenly over the grid points between t0 and t1 (beat / half-beat cuts)
    a, b = snap(t0), snap(t1)
    pts = [g for g in GRID if a - 1e-6 <= g < b - 1e-6]
    n = len(clips)
    for k, (c, i) in enumerate(clips):
        S.append((pts[round(k * len(pts) / n)], c, i, why))

# ---- intro: calm, then the drop on 10.82, medium action, no rapping
hold(0.0,    'k19m-a', 0.0, 'calm open: the gang chilling on the girder (Kai\'s candidate for the beginning)')
hold(5.991,  'k04m-a', 1.0, 'calm swagger stroll, still not robbing')
hold(10.832, 'z02y-b', 0.3, 'THE DROP: picture changes on 10.82, medium action')
hold(14.35,  'k09m-a', 1.0, 'medium action, building')
hold(17.926, 'a03m-a', 0.0, 'dah dah dah: the car skids in, wind-up to the words')
# ---- verse 1
hold(20.178, 'q01-b',  0.0, 'first rapping shot the moment the words start; held through 24.5 (keep)')
hold(24.683, 'k21m-a', 0.5, 'where does it go? notes spilling off the boat')
hold(29.187, 'z03-a',  0.5, 'keep at 29.6: Nobody knows!, rapping on the rope ladder')
hold(33.413, 'x07m-b', 1.0, 'standards bleeding: the liquor floods the floor')
hold(35.968, 'k12m-a', 2.5, 'quantitative easing: money flung over the crowd')
hold(37.257, 'v07m-b', 0.5, 'grandma freezing, only on those words')
burst(38.556, 41.111, [('c03g-b', 0.5), ('h06-b', 1.0), ('h17-b', 0.0), ('h19-a', 0.0)],
      'BURST, end of verse 1: printing on stimulus checks, then the crew')
# ---- verse 2
hold(41.111, 'p02-a',  1.5, 'rent seeking: Crimson rapping, sarcastic shrug')
hold(43.386, 'k01m-a', 0.0, 'did I interrupt your meeting? the explosion')
hold(46.312, 'q04-a',  0.0, 'keep at 49.9: printing money, held through the Fed lines')
hold(50.503, 'k30m-a', 0.5, 'fiat/debt: the dynamite safe, held tension')
hold(55.24,  'p12-a',  1.0, 'oh oh oh: all six on the jazz stage')
hold(58.236, 'p05-a',  0.0, 'held breath before the chorus: Crimson on the girder')
# ---- chorus 1 (template, repeated for chorus 2)
CH = []
def ch(t, clip, i, why): CH.append((t, clip, i, why))
for k, (c, i) in enumerate([('cn:chase3-a', 1.0), ('h02-a', 1.0), ('cn:safe2-c', 0.3), ('h18-b', 2.0)]):
    ch(61.788 + k * (63.089 - 61.788) / 4, c, i, 'BURST, Robbery! Robbery!: cut into the car chase on the first Robbery, crew among the cars')
ch(63.089, 'cn:rods4-a', 1.5, 'the chase, held')
ch(64.714, 'c02-a',      0.0, 'call the police, only while it is sung')
ch(65.991, 'cn:safe4-b', 0.3, 'basement half begins (Kai: excellent basement scene)')
ch(69.532, 'c03g-b',     2.0, 'printer is burring: the press in the cellar')
for k, (c, i) in enumerate([('h15-b', 1.0), ('h09-a', 0.5), ('h20-a', 2.5), ('h07-b', 2.0)]):
    ch(72.423 + k * (73.723 - 72.423) / 4, c, i, 'BURST, Robbery! Robbery!: crew half-beat cuts')
ch(73.723, 'k13m-b', 0.5, 'basement distillery, held through call the police / debasement')
ch(78.576, 'q04-a',  1.6, 'it happened in the basement / printer: printing, held')
for t, c, i, w in CH:
    hold(t, c, i, w)
# ---- verse 3
hold(82.779, 'q05-b',  0.3, 'stacks of cash / dyspraxic flash: the magician glove, held')
hold(87.934, 'x04-a',  1.5, 'the shitty little drop: sack dropped off the boxcar')
hold(90.384, 'h07-b',  1.0, 'right and left witness the theft: the crew looking down on us')
hold(95.016, 'd06m-a', 0.6, 'keep at 96.9: the dilution')
hold(98.558, 'y03-a',  1.0, 'distraction is the attraction: slow-motion spectacle')
burst(102.005, 104.339, [('h11-b', 0.5), ('p16-a', 2.0), ('h02-a', 3.5), ('x03m-b', 1.0)],
      'BURST, end of verse 3: divide and conquer, the factions flash past')
hold(104.339, 'g08y-b', 0.0, 'just look at the hand: the magician, held')
# ---- verse 4
hold(107.265, 'k27m-b', 1.0, 'state level manipulation: the clerk raises his hands')
hold(110.504, 'd10-a',  0.0, 'keep exactly here: the devil with the radio station')
hold(113.406, 'd11-a',  0.5, 'stack up the vaults like a wheelbarrow, held')
hold(118.561, 'h20-a',  2.0, 'Biggie said wait: Rust snaps the pocket watch')
hold(120.186, 'q08-a',  0.5, 'the gramophone (Kai times it by hand in Premiere)')
# ---- chorus 2 = chorus 1 shifted
for t, c, i, w in CH:
    hold(snap(t + 61.88), c, i, 'chorus 2 repeats chorus 1: ' + w)
# ---- break
hold(144.033, 'q09-a',  0.6, 'the break on the hit: Pablo Escobar, billiard hall, held')
hold(149.107, 'a01m-a', 0.3, 'stand up plans for the working man: the long slow walk')
# ---- verse 5 (new crew clips)
hold(154.691, 'h19-a',  0.5, 'next level scam: the crew under the marquee, held')
hold(159.521, 'k23-a',  0.0, 'bailin\' out: Marine slides down from the blimp (not the train)')
hold(162.435, 'h11-b',  2.0, 'own a printer and you don\'t feel winter: crew in the snow')
hold(165.024, 'k36m-b', 0.5, 'asset inflation / wealth gap: cigars, the fuse and the cake')
hold(170.179, 'h15-b',  0.5, 'paid in money / print more: the crew in the dining car')
burst(174.057, 175.984, [('h17-b', 2.0), ('q12-b', 3.0), ('h06-b', 3.0), ('h09-a', 1.5)],
      'BURST, end of verse 5: and expect them not to worry')
hold(175.984, 'h12-a',  0.5, '2:56 tone change: a completely different world, dawn meadow and balloon')
hold(180.547, 'v07m-b', 2.5, 'time to give: Plum gives grandma his jacket')
hold(182.543, 'v11x-a', 0.5, 'the man on the bank steps (excellent), held to the end')

plan = []
for k, (t, c, i, w) in enumerate(S):
    st = 0.0 if k == 0 else snap(t)
    en = END if k == len(S) - 1 else snap(S[k + 1][0])
    plan.append({'start': round(st, 3), 'end': round(en, 3), 'clip': c, 'in': i, 'line': line_at(st, en), 'why': w})
json.dump(plan, open(HERE / 'plan-D.json', 'w'), indent=1)
print(len(plan), 'shots')
