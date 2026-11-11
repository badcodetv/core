"""Cut E, "Energy curve": cutting speed follows loudness_per_bar and the strong hits.
python3 make-E.py  ->  plan-E.json"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
mm = json.load(open(HERE / 'music-map.json'))
pool = {p['ref']: p for p in json.load(open(HERE / 'pool.json'))}
END = mm['end']
B = mm['beats']
GRID = sorted(set(B + [round((a + b) / 2, 4) for a, b in zip(B, B[1:])] + mm['strong_hits']))
LINES = mm['lines']

EXACT = {10.82, 20.14}  # the drop and the first word: Kai's own times, both within 0.045 s of a half beat / beat

def snap(t):
    if t in EXACT:
        return t
    g = min(GRID, key=lambda x: abs(x - t))
    if abs(g - t) > 0.12:
        print(f'warning: {t} snapped far to {g}')
    return round(g, 4)

# (cut time, clip, in, why)   the shot runs from its time to the next shot's time
INTRO = [
    (0.0,    'k19m-a', 0.0, 'calmest: the lunch on the girder, one long hold (Kai: candidate for the very beginning)'),
    (5.979,  'y05-a',  1.5, 'still calm, deadpan lean, two-beat-plus hold'),
    (7.941,  'y04-a',  2.5, '"Robbery!" shout over a dead-calm Keaton dust-off'),
    (9.218,  'k13m-b', 1.0, 'louder bar: calm finger-guns in the basement, holding to the drop'),
    (10.82,  'k04m-a', 1.5, 'THE DROP: picture changes on 10.82, the swagger walk = first step up'),
    (12.411, 'a01m-a', 1.0, 'two-beat cuts on strong hits'),
    (13.711, 'k23-a',  0.5, 'medium action from 13 s'),
    (15.0,   'k22m-b', 0.5, 'medium action, louder bar'),
    (16.289, 'x06-a',  1.5, 'strong hit'),
    (17.264, 'a03m-a', 0.0, 'quickening on the hits into the words'),
    (17.914, 'k09m-a', 0.5, '"Dah dah" on the hit'),
    (18.564, 'k10-a',  0.0, 'hit'),
    (19.551, 'k36m-b', 0.0, 'lit fuse, the last breath before the words'),
]
VERSE12 = [
    (20.14,  'h19-a',  0.0, 'words start: step up, first rapping shot'),
    (21.455, 'k16-a',  0.0, 'E5 lamps burst, one beat'),
    (22.105, 'q01-b',  0.0, 'KEEP (24.5 s): Plum on the rooftop'),
    (24.683, 'x04-a',  1.5, 'bar line, mid-loud: two-bar-ish non-rap'),
    (26.598, 'p02-a',  2.0, 'strong hit: rapping on "earning that dough"'),
    (27.899, 'k21m-a', 2.0, 'hit: cash at the stern, "where does it go?"'),
    (29.187, 'z03-a',  1.0, 'KEEP (29.6 s): "Nobody knows!" bag shake'),
    (31.161, 'h06-b',  1.0, 'means of production: the workers on the scaffold, rapping'),
    (32.984, 'x07m-b', 1.5, 'hit, louder bar'),
    (34.331, 'h20-a',  2.0, 'hit: landlords, the tenement rooftop crew'),
    (35.968, 'k12m-a', 2.5, '"Quantitative easing": money thrown over the crowd'),
    (37.2565,'v07m-b', 1.0, '"grandma freezing" only on those words'),
    (38.556, 'c03g-b', 0.3, '"stimulus checks": the printing press'),
    (40.275, 'z04-b',  0.8, 'hit: "necks get wrecked"'),
    (41.111, 'h15-b',  1.0, 'quiet bar (0.45): long rapping hold, "just about eating" in the dining car'),
    (43.386, 'k01m-a', 0.0, 'quiet bar: the explosion on "did I interrupt your meeting?", long hold'),
    (46.312, 'h09-a',  0.5, '"the Fed is not your friend" in the banking hall'),
    (47.926, 'q04-a',  0.0, 'KEEP (49.9 s): printing money'),
    (50.503, 'a02m-a', 2.0, 'loudest verse bar (0.84): a cut every beat'),
    (51.154, 'y03-a',  1.0, 'beat cut, E4'),
    (51.78,  'h02-a',  1.0, '"fiat system": crew bouncing on the salt flat'),
    (53.069, 'k10-a',  1.5, 'hit, E4'),
    (54.358, 'a03m-a', 1.5, 'hit, E4'),
    (55.24,  'h18-b',  2.0, '"Oh, oh, oh": crowd and money falling, loud bar'),
    (56.308, 'k09m-a', 2.0, 'beat'),
    (57.585, 'x06-a',  3.0, 'beat, E4'),
    (58.224, 'z02y-b', 0.5, 'hit'),
    (59.536, 'p05-a',  0.0, '"Have resistance to the facts": quieter bar, held to the chorus'),
]
CHORUS1 = [
    (61.788, 'cn:chase1-a', 0.5, 'CHORUS: into the car chase on the first "Robbery!" (on the half beat by 61.86)'),
    (62.764, 'cn:safe2-c',  0.3, 'chase, beat'),
    (63.414, 'cn:chase3-a', 1.0, 'chase, beat'),
    (64.064, 'cn:rods4-a',  2.2, 'chase, beat'),
    (64.714, 'c02-a',       0.0, '"Call the police": only while it is sung'),
    (66.316, 'x06-a',       0.5, 'chase, one beat'),
    (66.966, 'c03g-b',      3.0, '"Debasement": basement printing press'),
    (68.2555,'k13m-b',      2.5, '"It happened in the basement"'),
    (69.195, 'q04-a',       2.5, 'hit: "Printer is burring" press room'),
    (70.484, 'z06y-b',      2.5, 'hit: vault corridor, loudest bar'),
    (71.146, 'k29m-a',      0.0, 'underground, beat'),
    (71.784, 'k30m-a',      1.0, 'hit: safe room'),
    (72.423, 'cn:chase3-a', 3.0, '"Robbery!" again: chase'),
    (73.073, 'cn:safe2-c',  2.0, 'chase, beat'),
    (73.723, 'cn:chase1-a', 2.0, 'chase, beat'),
    (74.374, 'c02-a',       1.5, '"Call the police": only while it is sung'),
    (76.6375,'a03m-a',      0.0, 'chase, one beat'),
    (77.276, 'k27m-b',      2.0, '"Debasement": the vault doorway'),
    (78.576, 'd11-a',       0.0, '"in the basement": wheelbarrow out of the vault'),
    (79.517, 'c03g-b',      1.5, 'hit: "Printer is burring"'),
    (80.829, 'k31-b',       0.5, 'quieter bar: lowering into the vault, longer'),
]
VERSE34 = [
    (82.106, 'd12-b',  1.5, 'chorus out, quietest bar of the middle (0.40): long calm hold, cash sack on the ledge'),
    (85.008, 'q05-b',  0.0, '"Distracted by a dyspraxic flash": the glove flash'),
    (86.831, 'k22m-b', 1.0, 'hit, mid bar, calm'),
    (87.934, 'h07-b',  2.0, '"Marked angry": crew jabbing down at the lens'),
    (89.188, 'k16-a',  2.5, 'loud bar (0.79): E5, one beat'),
    (89.838, 'a02m-a', 3.5, 'beat'),
    (90.384, 'h12-a',  1.0, 'hit: "the right and the left", crew before the balloon'),
    (91.463, 'y03-a',  3.0, 'hit, E4'),
    (92.1135,'k10-a',  3.0, 'half beat'),
    (92.764, 'h19-a',  2.5, '"Blaming each other": crew pointing'),
    (94.366, 'd06m-a', 0.0, 'KEEP (96.9 s): the dilution, quieter bar, long hold'),
    (96.99,  'k21m-a', 3.5, 'bar line: notes spilling'),
    (98.558, 'p12-a',  2.0, '"Distraction is the attraction": the stage show'),
    (99.509, 'k36m-b', 1.5, 'hit: cigars while the fuse burns'),
    (100.496,'x07m-b', 3.0, '"The intention is tension": police busy with barrels while Bottle walks the crate out the back'),
    (102.005,'h18-b',  3.0, 'hit: "between the factions", the crowd and the money'),
    (103.398,'k12m-a', 0.5, 'notes flung over the crowd, the misdirection'),
    (104.339,'g08y-b', 0.0, 'hit: "Just look at the hand", the magician palms a note'),
    (106.626,'k09m-a', 3.0, 'hit'),
    (107.265,'h06-b',  3.5, 'hit, louder bar'),
    (108.2635,'k27m-b',3.5, '"state level manipulation": hands up for the clerk'),
    (109.203,'h15-b',  3.0, 'beat'),
    (110.504,'d10-a',  0.0, 'KEEP (113.0 s): the devil with the radio station'),
    (113.07, 'd11-a',  2.0, 'hit: "Stack up the vaults like a wheelbarrow"'),
    (114.358,'h17-b',  0.0, 'hit: crew on the bank steps, money raining'),
    (115.647,'d12-b',  3.5, 'hit: "really rather narrow", the ledge'),
    (116.959,'x06-a',  0.0, 'beat'),
    (117.609,'a03m-a', 3.0, 'loud bar (0.84): beat cut'),
    (118.561,'h02-a',  3.0, '"Biggie said, wait!"'),
    (120.186,'q08-a',  0.0, 'GRAMOPHONE: Kai times it by hand in Premiere'),
    (122.741,'x02-a',  2.0, 'bar line: the roadster run into the chorus'),
]
BREAK_V5 = [
    (144.033,'q09-a',  1.0, 'BREAK: hit, "Pablo Escobar", the pause, long hold'),
    (146.634,'x03m-b', 0.5, 'quiet bar (0.56): long hold in the snow, nodding on the beat'),
    (149.722,'y06-a',  1.5, '"Stackin\' up the cash": pouring notes from the balloon'),
    (152.114,'k19m-a', 3.0, '"for the working man": the lunch on the girder'),
    (154.691,'h20-a',  3.0, 'verse 5: "a next level scam", louder bar'),
    (156.294,'k16-a',  3.0, 'loud bar (0.83): E5 beat'),
    (156.944,'h17-b',  2.0, '"All gotten gains"'),
    (158.224,'y03-a',  2.0, 'hit'),
    (158.894,'h06-b',  4.0, 'bar line'),
    (159.521,'k23-a',  0.0, 'hit: "Bailin\' out", sliding down from the blimp (not the train)'),
    (161.495,'z03-a',  4.0, 'still bailing: the rope ladder under the plane'),
    (162.435,'c03g-b', 4.0, '"Own a printer and you don\'t feel winter"'),
    (164.049,'x06-a',  3.5, 'loud bar (0.92): fastest stretch of the verse'),
    (165.024,'p15-a',  1.0, '"Crime is asset inflation": the dining car'),
    (166.65, 'k10-a',  3.5, 'beat'),
    (167.602,'h09-a',  2.0, '"Of a wealth gap": the banking hall'),
    (168.879,'k09m-a', 4.0, 'hit, loudest bar (1.0)'),
    (169.523,'a02m-a', 0.5, 'beat'),
    (170.179,'h12-a',  3.0, '"people get paid in money"'),
    (171.119,'k16-a',  4.5, 'hit'),
    (171.781,'q12-b',  3.0, '"not very funny when you print more": fingers wagging'),
    (172.768,'y03-a',  4.5, 'hit'),
    (173.398,'x04-a',  4.0, 'beat'),
    (174.057,'a03m-a', 4.5, '"expect them not to worry"'),
    (174.544,'k12m-a', 4.0, 'hit'),
    (175.009,'p16-a',  2.5, 'hit: the ring, last fast shot'),
    (175.984,'h11-b',  2.5, '2:56 TONE CHANGE: hardest switch, a world not seen before (night snow field), long hold'),
    (178.724,'k01m-a', 3.5, '"retribution, perhaps some execution": the slow walk from the fireball'),
    (180.547,'v07m-b', 3.0, '"It\'s time to give": the jacket over her shoulders'),
    (181.859,'v11x-a', 0.8, 'KEEP (183.5 s) and the end: the man on the bank steps, slow last hold to 187.0'),
]
SHIFT = 61.88
ch1 = [r for r in CHORUS1]
CHORUS2 = [(t + SHIFT, c, i, 'chorus 2 = chorus 1: ' + w.split(': ', 1)[-1]) for (t, c, i, w) in ch1]

ALL = INTRO + VERSE12 + CHORUS1 + VERSE34 + CHORUS2 + BREAK_V5
cuts = [(snap(t) if t > 0 else 0.0, c, i, w) for (t, c, i, w) in ALL]
plan = []
for k, (t, c, i, w) in enumerate(cuts):
    end = cuts[k + 1][0] if k + 1 < len(cuts) else END
    d = end - t
    secs = pool[c]['secs']
    if i + d > secs - 0.01:
        i = max(0.0, round(secs - d - 0.02, 3))
    ov = [(min(end, L['end']) - max(t, L['start_snapped']), L['text']) for L in LINES]
    ov = [o for o in ov if o[0] > 0.15]
    line = ' / '.join(x for _, x in sorted(ov, key=lambda o: -o[0])[:2]) if ov else ''
    plan.append({'start': round(t, 4), 'end': round(end, 4), 'clip': c, 'in': round(i, 3), 'line': line, 'why': w})
for a, b in zip(plan, plan[1:]):
    assert a['clip'] != b['clip'], (a, b)
    assert a['end'] > a['start']
json.dump(plan, open(HERE / 'plan-E.json', 'w'), indent=1, ensure_ascii=False)
print(len(plan), 'shots')
