"""Cut A, "Jack's cut, fixed": cut 9 (edit-plan-r9.json) with Kai's notes applied and the cuts moved
onto the music's events. Writes plan-A.json.   python3 make-A.py && python3 validate.py plan-A.json
Each row: (approx start, clip, in, why). Starts snap to the nearest beat / half beat / strong hit."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
mm = json.load(open(HERE / 'music-map.json'))
B = mm['beats']
GRID = sorted(set([0.0] + B + [round((a + b) / 2, 3) for a, b in zip(B, B[1:])] + mm['strong_hits']))
END = mm['end']
SHIFT = 61.93  # chorus 1 -> chorus 2 (the line starts shift by 61.93-61.95)


def snap(t):
    g = min(GRID, key=lambda x: abs(x - t))
    assert abs(g - t) <= 0.06, (t, g)
    return g


def line_at(s, e):
    out = [l['text'] for l in mm['lines'] if l['start_snapped'] < e - 0.15 and l['end'] > s + 0.15 and 'Music' not in l['text']]
    return ' / '.join(out)


INTRO = [
    (0.0, 'k19m-a', 0.0, "calm open: the gang chilling on the girder (Kai's candidate for the very beginning)"),
    (4.063, 'k13m-b', 0.0, 'calm: deadpan finger-guns in the basement'),
    (5.979, 'y05-a', 0.5, 'calm: PLUM leaning on a barrel'),
    (7.941, 'y03-a', 0.0, "Jack's flurry, from 'Robbery!'"),
    (8.591, 'y04-a', 0.0, "Jack's flurry"),
    (9.218, 'z02y-b', 0.0, "Jack's flurry"),
    (9.868, 'z04-b', 0.0, "Jack's flurry, now ends ON the drop"),
    (10.833, 'a01m-a', 1.0, 'THE DROP: the six walk at us, picture changes exactly on it'),
    (13.711, 'k30m-a', 0.5, 'medium action (replaces z06y-b, which reads as rapping)'),
    (15.0, 'k04m-a', 0.0, "Jack's"),
    (16.289, 'k09m-a', 0.0, "Jack's, on a strong hit"),
    (17.264, 'k10-a', 0.0, "Jack's, on a strong hit"),
    (17.914, 'k12m-a', 0.0, "Jack's, on 'Dah dah'"),
    (18.564, 'k16-a', 0.0, "Jack's tommy-gun burst, moved before the words"),
]
VERSES_1_2 = [
    (20.178, 'h20-a', 2.5, 'first rapping shot the moment the words start (new crew clip)'),
    (22.105, 'q01-b', 0.0, 'KEEP (Kai: "I love this shot")'),
    (24.683, 'k27m-b', 0.0, "non-rap: the clerk at work, 'work can get paid' (k19m-a moved to the opening)"),
    (26.947, 'p02-a', 0.5, "Jack's Grand Central rap, on the line"),
    (29.187, 'z03-a', 0.0, 'KEEP (Kai: "good shot for this exact moment"), on "Nobody knows!"'),
    (31.161, 'h06-b', 1.0, "rapping crew the moment 'Means of production' kicks in (Kai's 32.8 note)"),
    (33.413, 'k21m-a', 0.0, "Jack's"),
    (34.691, 'k23-a', 0.0, "Jack's"),
    (35.968, 'y06-a', 0.0, 'money thrown around on "quantitative easing"'),
    (37.257, 'v07m-b', 1.0, 'grandma only on "grandma freezing"'),
    (38.556, 'c03g-b', 4.0, 'printing on "stimulus checks"'),
    (39.776, 'k29m-a', 0.0, "Jack's"),
    (41.111, 'h15-b', 1.0, "crew raps in the dining car on 'just about eating'"),
    (43.386, 'k01m-a', 0.5, 'explosion on "Sorry, did I interrupt your meeting?"'),
    (46.312, 'k36m-b', 0.0, "Jack's"),
    (47.926, 'q04-a', 0.0, 'KEEP (Kai: printing money, "perfect")'),
    (50.503, 'a01m-a', 4.0, "Jack's"),
    (51.78, 'h09-a', 0.5, 'crew raps in the bank hall (replaces a02m-a: extra man)'),
    (53.081, 'a03m-a', 0.0, "Jack's"),
    (53.731, 'x06-a', 0.0, "Jack's"),
    (54.358, 'x07m-b', 0.0, "Jack's, on a strong hit"),
    (55.658, 'd11-a', 2.6, "Jack's"),
    (56.959, 'd12-b', 0.0, "Jack's"),
    (58.224, 'p05-a', 0.0, "Jack's rap, held to the chorus (no early car)"),
]
CHORUS_1 = [
    (61.753, 'cn:rods3-b', 0.5, "car chase cut ON the first 'Robbery!' (Jack's order)"),
    (62.423, 'cn:safe2-c', 0.3, "Jack's chase"),
    (63.077, 'cn:chase1-a', 0.5, "Jack's chase, strong hit"),
    (63.739, 'cn:chase3-a', 1.0, "Jack's chase (safe4 dropped: wrong mask)"),
    (64.714, 'c02-a', 0.0, 'call the police: only while it is sung'),
    (66.316, 'cn:rods4-a', 2.2, 'chase tail'),
    (66.966, 'c03g-b', 0.5, 'basement: the red cellar press on "Debasement / in the basement"'),
    (69.532, 'q04-a', 3.2, 'printing on "Printer is burring"'),
    (70.484, 'k31-b', 2.0, 'underground: lowering into the vault'),
    (71.784, 'd11-a', 4.0, 'vault cash'),
    (72.423, 'k30m-a', 3.0, 'second half = basement: the safe room'),
    (73.723, 'k29m-a', 2.0, 'vault corridor'),
    (74.374, 'c02-a', 2.5, 'call the police: only while it is sung'),
    (76.637, 'z04-b', 2.0, 'bullet through the door'),
    (77.276, 'k13m-b', 3.0, 'basement distillery on "Debasement"'),
    (78.576, 'z06y-b', 2.5, 'basement vault on "in the basement"'),
    (79.841, 'k27m-b', 3.5, 'vault on "Printer is burring"'),
    (81.479, 'k31-b', 4.0, 'underground'),
]
VERSES_3_4 = [
    (82.977, 'k12m-a', 2.5, "Jack's: 'stacks of elastic cash' flung over the crowd"),
    (85.008, 'q05-b', 0.0, "Jack's: the magician flash on 'dyspraxic flash', on the line"),
    (86.634, 'k09m-a', 2.0, 'non-rap (k13m-b rested, used in the chorus)'),
    (87.934, 'k22m-b', 1.0, "Jack's train, now hand-cut with the crew (Kai's 90 s note)"),
    (89.188, 'h19-a', 0.0, 'crew raps'),
    (90.384, 'k22m-b', 2.6, "Jack's train again, on 'the right and the left'"),
    (91.463, 'h07-b', 2.0, 'crew looking down at us: witnesses'),
    (92.764, 'k16-a', 2.0, "Jack's"),
    (94.366, 'd06m-a', 0.0, 'KEEP (Kai: the dilution part)'),
    (96.99, 'k21m-a', 3.0, "Jack's"),
    (98.558, 'p12-a', 1.5, "distraction: the show on 'Distraction is the attraction'"),
    (100.496, 'x07m-b', 1.0, 'distraction: the raid while the crate goes out the back'),
    (102.005, 'h18-b', 2.0, 'distraction: crowd clapping, money falling'),
    (103.398, 'g08y-b', 0.0, "Jack's magician hand on 'Just look at the hand'"),
    (105.326, 'y06-a', 2.5, "Jack's pick, on the line"),
    (107.265, 'k30m-a', 4.5, "Jack's"),
    (108.263, 'a02m-a', 3.0, 'state level manipulation: the lobby cowers'),
    (110.504, 'd10-a', 0.0, 'KEEP EXACTLY HERE: the devil-horn radio booth'),
    (113.07, 'd11-a', 0.0, "the wheelbarrow on 'Stack up the vaults like a wheelbarrow'"),
    (115.647, 'a03m-a', 3.4, "Jack's"),
    (116.959, 'x06-a', 1.7, "Jack's"),
    (118.561, 'x07m-b', 3.5, "Jack's, on 'Biggie said, wait!'"),
    (120.186, 'q08-a', 0.0, 'the gramophone: Kai times it by hand in Premiere'),
    (122.741, 'd12-b', 2.0, "Jack's"),
]
BREAK_V5 = [
    (144.033, 'q09-a', 0.0, "Jack's Pablo Escobar shot, now cut on the line"),
    (146.634, 'x03m-b', 0.0, "Jack's pick, on the line"),
    (149.722, 'x04-a', 2.0, "Jack's pick, on the line"),
    (152.114, 'x02-a', 1.7, "Jack's pick, on the line"),
    (154.691, 'h02-a', 1.0, 'verse 5: new crew clip instead of repeats'),
    (156.944, 'z02y-b', 3.4, "Jack's"),
    (158.244, 'h12-a', 1.0, 'new crew clip (was z04-b, a repeat)'),
    (159.521, 'k23-a', 2.5, "'Bailin' out': MARINE bails out of the airship (replaces the train)"),
    (162.435, 'h11-b', 1.0, "crew in the snow: 'you don't feel winter'"),
    (165.024, 'p15-a', 0.0, "Jack's dining-car pick, on the line"),
    (167.602, 'y04-a', 2.5, "'a wealth gap': the fallen house"),
    (169.227, 'q12-b', 0.0, "Jack's"),
    (171.781, 'k04m-a', 3.0, "Jack's"),
    (174.057, 'p16-a', 2.0, "Jack's boxing ring, on 'expect them not to worry'"),
    (175.984, 'h17-b', 0.0, '2:56 TONE CHANGE: a completely different scene, fire and raining money on the bank steps'),
    (177.935, 'k16-a', 4.0, "'retribution, execution'"),
    (179.56, 'y03-a', 1.5, 'chandelier smash'),
    (180.547, 'v07m-b', 3.0, "'time to give, not just to take': the jacket given to the grandma"),
    (182.207, 'v11x-a', 0.0, 'KEEP (Kai: "excellent") and END on the man on the bank steps, held to 187.0'),
]

rows = INTRO + VERSES_1_2 + CHORUS_1 + VERSES_3_4
c2 = [(t + SHIFT, c, i, 'chorus 2 = chorus 1: ' + w) for t, c, i, w in CHORUS_1]
c2[0] = (123.716,) + c2[0][1:]
rows += c2 + BREAK_V5

plan = []
starts = [snap(r[0]) for r in rows] + [END]
for (t, clip, i, why), s, e in zip(rows, starts, starts[1:]):
    plan.append({'start': s, 'end': e, 'clip': clip, 'in': i, 'line': line_at(s, e), 'why': why})
for a, b in zip(plan, plan[1:]):
    assert a['clip'] != b['clip'], a
json.dump(plan, open(HERE / 'plan-A.json', 'w'), indent=1)
print(len(plan), 'shots')
