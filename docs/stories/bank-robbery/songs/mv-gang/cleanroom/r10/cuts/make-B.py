"""Cut 10, plan B: strict alternation (rapping line / story line / rapping line ...).
python3 make-B.py  -> plan-B.json"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
mm = json.load(open(HERE / 'music-map.json'))
b = mm['beats']
GRID = sorted(set(b + [round((x + y) / 2, 3) for x, y in zip(b, b[1:])] + mm['strong_hits']))
def snap(t):
    return min(GRID, key=lambda g: abs(g - t))

# (start, clip, in, line, why)   R = rapping to camera, A = story/action
INTRO = [
    (0.0,    'k19m-a', 0.2, '', 'calm open: the gang at lunch on the girder (Kai\'s pick for the very beginning)'),
    (3.727,  'k13m-b', 1.0, '', 'calm: chilling in the basement distillery'),
    (5.979,  'y05-a',  0.5, '', 'calm: Plum leaning on a barrel, deadpan'),
    (7.941,  'y04-a',  2.6, 'Robbery!', 'the shout: Buster Keaton house front, first quick change'),
    (9.218,  'k23-a',  0.0, '', 'quick: Marine on the blimp rope'),
    (9.868,  'a01m-a', 1.0, '', 'quick: the six walk in, still calm'),
    (10.832, 'k10-a',  0.0, '', 'THE DROP: picture changes on it, wide train on the trestle'),
    (12.098, 'k09m-a', 1.0, '', 'building: speedboat spray'),
    (13.711, 'z02y-b', 0.5, '', 'medium action from 13.7: car swerves the cart'),
    (14.35,  'a02m-a', 2.0, '', 'medium action: Crimson strides into the lobby'),
    (16.289, 'k29m-a', 0.0, '', 'limbo under the bell threads'),
    (17.264, 'x06-a',  1.0, '', 'speedboat, quick'),
    (17.914, 'a03m-a', 3.5, 'Dah, dah, dah, dah', 'sedan by the greengrocer'),
    (18.564, 'k04m-a', 2.0, 'Dah, dah, dah, dah', 'swagger walk to the lens, into the words'),
]
VERSES_1_2 = [
    (20.178, 'q01-b',  0.5, "They say, you can't make money from a tree / Let's see each day, make hay not free", 'R: first rap on the first word, held two lines so the 24.5 keeper stays'),
    (25.356, 'k19m-a', 4.0, 'Ayy, work can get paid though', 'A: workers counting notes on the beam'),
    (26.947, 'h06-b',  1.0, 'Earning that dough, but where does it go?', 'R: crew on the rooftop scaffold, lunch pail'),
    (29.187, 'z03-a',  1.0, 'Nobody knows!', 'A: keeper, the rope ladder under the plane'),
    (31.161, 'h20-a',  0.8, 'Means of production, means of reduction / Standards bleeding, landlords needing', 'R: crew rap the moment the words kick in (Kai 32.8), held two lines'),
    (35.968, 'k12m-a', 2.5, 'Quantitive easing', 'A: money flung over the crowd on QE'),
    (37.257, 'v07m-b', 0.8, 'grandma freezing', 'A: grandma only on her words'),
    (38.556, 'c03g-b', 0.5, 'Simulus checks and necks get wrecked / Rent seeking, I\'m just about eating', 'R: the gang rapping round a printing press on stimulus checks'),
    (43.386, 'k01m-a', 0.0, 'Sorry, did I interrupt your meeting?', 'A: the explosion behind the bank steps'),
    (46.312, 'q04-a',  0.0, 'Remember kids, the Fed is not your friend / It prints all the dollars that the government spends', 'R: keeper, printing money (49.9)'),
    (51.78,  'k27m-b', 1.5, "It's fiat system", 'A: the clerk raises his hands'),
    (53.069, 'x06-a',  3.0, 'is insistent on debts existence', 'A: split on the strong hit, the speedboat runs'),
    (55.24,  'h02-a',  0.5, 'Oh, oh, oh', 'R: crew on the salt flats'),
    (59.536, 'k16-a',  0.0, "Have resistance to the facts I'm stating", 'A: tommy gun at the lamps, into the chorus'),
]
CHORUS = [
    (61.753, 'cn:safe2-c', 0.3, 'Robbery! Robbery!', 'chase on the first Robbery, not early'),
    (63.077, 'cn:chase3-a', 1.0, 'Robbery! Robbery!', 'chase on the strong hit'),
    (64.714, 'c02-a',  0.0, "Call the police, it's a robbery", 'call box only while it is sung'),
    (66.316, 'cn:rods4-a', 2.2, '', 'chase, the river channel'),
    (66.966, 'k13m-b', 3.3, 'Debasement, debasement', 'basement'),
    (68.255, 'z06y-b', 2.5, 'It happened in the basement', 'basement vault corridor'),
    (69.532, 'c03g-b', 3.7, "Printer is burring, now now what's a burring?", 'printing'),
    (71.784, 'k29m-a', 2.0, '', 'underground vault corridor'),
    (72.423, 'cn:chase1-a', 0.5, 'Robbery! Robbery!', 'chase'),
    (73.723, 'cn:rods2-b', 1.0, '', 'chase from the tower'),
    (74.374, 'c02-a',  2.2, "Call the police, it's a robbery", 'call box only while it is sung'),
    (76.637, 'cn:rods3-b', 0.5, '', 'chase, headlight'),
    (77.276, 'k30m-a', 3.0, 'Debasement, debasement', 'basement safe room'),
    (78.576, 'k31-b',  4.0, 'It happened in the basement', 'down through the floor into the vault'),
    (79.517, 'q04-a',  3.3, "Printer is burring, now now what's a burring?", 'printing presses'),
    (82.106, 'd11-a',  4.0, '', 'cash out of the vault'),
]
CHORUS_END = 82.977
VERSES_3_4 = [
    (82.977,  'k21m-a', 1.5, 'Stacks and stacks of elastic cash', 'A: the crate of notes'),
    (85.008,  'q05-b',  0.0, 'Distracted by a dyspraxic flash', 'R: the magician\'s glove flash'),
    (87.934,  'k31-b',  1.5, 'Marked angry at the shitty little drop', 'A: the floor drops into the vault'),
    (90.384,  'h19-a',  0.0, 'The right and the left both witness the theft', 'R: crew under the marquee'),
    (92.764,  'z04-b',  0.5, 'Blaming each other is a sick little cover', 'A: taking cover as the bullet punches through'),
    (95.016,  'd06m-a', 0.3, 'Institutional, dilutional, the usual', 'R: keeper, the watered-down bottle (96.9)'),
    (98.558,  'k36m-b', 0.0, 'Distraction is the attraction', 'A: cigars, a fuse and a wedding cake'),
    (100.496, 'h07-b',  2.0, 'The intention is tension', 'R: crew in a ring jabbing down at the lens'),
    (102.005, 'x07m-b', 1.0, 'Between the factions,', 'A: distraction: police axe barrels while the crate goes out the back'),
    (103.085, 'k23-a',  3.0, 'divide and conquer', 'A: distraction: five watch the rope while Marine slips down'),
    (104.339, 'g08y-b', 0.0, 'Just look at the hand', 'R: the magician\'s hand'),
    (105.326, 'k04m-a', 3.7, "It's not your standard propaganda", 'A: the swagger walk'),
    (106.626, 'h17-b',  0.5, 'Worth a couple grand, ah!', 'R: crew on the burning bank steps, notes raining'),
    (108.263, 'k30m-a', 0.5, 'It is state level manipulation', 'A: fingers on the clock and the wires'),
    (110.504, 'd10-a',  0.0, 'It is the devil with the radio station', 'R: keeper, the devil-horn booth, exactly here'),
    (113.081, 'd11-a',  0.0, 'Stack up the vaults like a wheelbarrow', 'A: the wheelbarrow of cash'),
    (115.647, 'h09-a',  0.3, 'Risk of default is really rather narrow', 'R: crew in the banking hall'),
    (118.561, 'd12-b',  1.5, 'Biggie said, wait!', 'A: waiting on the narrow ledge'),
    (120.186, 'q08-a',  0.5, "Rockin' 97 / Don't get high off your own supply", 'R: the gramophone, Kai times it in Premiere'),
]
BREAK_V5 = [
    (144.033, 'q09-a',  1.2, 'You know the real star is Pablo Escobar', 'R: billiard hall, now on the line start'),
    (146.634, 'x04-a',  0.5, 'Who has elastic bands, not plastic hands', 'A: the sack off the boxcar'),
    (149.722, 'h18-b',  2.0, "Stackin' up the cash by the grand", 'R: crew in the street, money falling'),
    (152.114, 'k22m-b', 1.0, 'Stand up plans are for the working man', 'A: the commuter reads his paper (the train here, not at 161)'),
    (154.691, 'h15-b',  1.0, 'And this right here is a next level scam', 'R: crew in the dining car'),
    (156.944, 'y05-a',  3.0, 'All gotten gains, no need to explain', 'A: Plum pats the barrel, deadpan'),
    (159.521, 'y06-a',  1.0, "Bailin' out will never mean the same", 'R: the bail-out, notes poured out of the balloon (replaces the train)'),
    (162.435, 'k36m-b', 3.0, "Own a printer and you don't feel winter", 'A: cigars round the safe, warm'),
    (165.024, 'h12-a',  1.0, 'Crime is asset inflation, passive creation', 'R: crew before the inflating balloon'),
    (167.602, 'a03m-a', 0.0, 'Of a wealth gap that drives the situation', 'A: the sedan ploughs the greengrocer'),
    (170.179, 'p05-a',  0.5, "Rockin' people get paid in money", 'R: Crimson on the girder'),
    (171.781, 'k12m-a', 0.0, "So it's not very funny when you print more", 'A: notes flung from the roadster'),
    (174.057, 'q12-b',  1.5, 'And expect them not to worry', 'R: finger-wag on the pier'),
    (175.984, 'y03-a',  0.5, 'Hungry people feed a revolution', 'A: 2:56 tone change: slow-motion flight through the chandelier'),
    (177.935, 'h11-b',  2.0, "Then it's retribution, perhaps some execution", 'R: a new world: crew in the snow at night'),
    (180.547, 'v07m-b', 3.0, "It's time to give, not just to take", 'A: Plum gives grandma his jacket'),
    (182.486, 'v11x-a', 0.5, "But for heaven's sake / Don't just eat cake", 'R: keeper, the man on the bank steps, held to the end'),
]
END = mm['end']

shots = INTRO + VERSES_1_2 + CHORUS
# chorus 2 repeats chorus 1, shifted onto chorus 2's own beats
shots += VERSES_3_4
c2_end = BREAK_V5[0][0]
for s, clip, inn, line, why in CHORUS:
    t = snap(s + 61.93)
    if c2_end - t < 0.3:
        continue
    shots.append((t, clip, inn, line, 'chorus 2 repeats chorus 1: ' + why))
shots += BREAK_V5

plan = []
for i, (s, clip, inn, line, why) in enumerate(shots):
    e = shots[i + 1][0] if i + 1 < len(shots) else END
    plan.append({'start': round(s, 3), 'end': round(e, 3), 'clip': clip, 'in': inn, 'line': line, 'why': why})
for a, b2 in zip(plan, plan[1:]):
    assert a['clip'] != b2['clip'], (a, b2)
json.dump(plan, open(HERE / 'plan-B.json', 'w'), indent=1)
print(len(plan), 'shots')
