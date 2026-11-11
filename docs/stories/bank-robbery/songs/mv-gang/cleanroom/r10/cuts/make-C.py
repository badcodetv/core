"""Cut C, "On the words": a cut at the start of every sung line (start_snapped), each line given the
clip whose picture best shows what it says; crew rapping where nothing does. Writes plan-C.json."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
mm = json.load(open(HERE / 'music-map.json'))
END = mm['end']

# (start, clip, in, line, why)
INTRO = [
    (0.0,    'k19m-a', 0.0, '', 'calm open: the gang at lunch on a girder (Kai: candidate for the very beginning)'),
    (4.063,  'y05-a',  0.5, '', 'still calm: PLUM pats a barrel, deadpan'),
    (7.941,  'k27m-b', 1.0, 'Robbery!', 'the word "robbery": a clerk slowly raises his hands, still calm'),
    (10.832, 'k36m-b', 0.0, '', 'THE DROP: a lit fuse starts racing to the safe'),
    (13.711, 'z02y-b', 0.5, '🎶 Music 🎶', 'medium action: the getaway car swerves'),
    (16.3,   'k10-a',  0.0, '', 'medium action on the strong hit: sprinting along the train roofs'),
    (17.914, 'k09m-a', 1.0, 'Dah, dah, dah, dah', 'speedboat run-up into the words'),
]
VERSES_1_2 = [
    (20.178, 'h12-a',  0.5, "They say, you can't make money from a tree", 'crew raps the moment the words start; meadow, nearest thing to a tree'),
    (22.756, 'q01-b',  0.651, "Let's see each day, make hay not free", 'KEEP (Kai at 24.5): same frame as cut 9 at 24.5'),
    (25.356, 'k19m-a', 4.1, 'Ayy, work can get paid though', 'workers on a girder counting their pay'),
    (26.947, 'y06-a',  0.5, 'Earning that dough, but where does it go?', 'cash poured out of a sack into the clouds: where does it go'),
    (29.187, 'z03-a',  0.0, 'Nobody knows!', 'KEEP (Kai at 29.6): the cash bag shaken off a plane'),
    (31.161, 'h06-b',  1.0, 'Means of production, means of reduction', 'crew on a work scaffold with a lunch pail: the workers are the means of production'),
    (33.413, 'x07m-b', 0.0, 'Standards bleeding, landlords needing', 'liquor bleeding across the floor'),
    (34.691, 'h20-a',  2.0, 'landlords needing', 'second thing on a strong hit: the tenement roof, RUST snaps his watch shut (rent day)'),
    (35.968, 'k12m-a', 0.5, 'Quantitive easing, grandma freezing', 'quantitative easing = money flung over a crowd (Kai)'),
    (37.257, 'v07m-b', 0.5, 'grandma freezing', 'grandma freezing only on her words (Kai); beat, no strong hit in the line'),
    (38.556, 'q04-a',  4.3, 'Simulus checks and necks get wrecked', 'stimulus checks = the presses printing (Kai)'),
    (40.275, 'k16-a',  0.5, 'necks get wrecked', 'second thing on a strong hit: the lamps get wrecked'),
    (41.111, 'p05-a',  0.0, "Rent seeking, I'm just about eating", 'BOTTLE eating on the girder while CRIMSON raps'),
    (43.386, 'k01m-a', 0.3, 'Sorry, did I interrupt your meeting?', 'the explosion (Kai): fireball behind the bank'),
    (46.312, 'h09-a',  0.5, 'Remember kids, the Fed is not your friend', 'the Fed = the banking hall; crew points at you'),
    (48.576, 'q04-a',  0.3, 'It prints all the dollars that the government spends', 'KEEP (Kai at 49.9): printing money, "perfect"'),
    (51.78,  'd11-a',  3.5, "It's fiat system is insistent on debts existence", 'fiat money: cash bundles in the vault'),
    (53.069, 'k30m-a', 1.0, 'debts existence', 'second thing on a strong hit: the dynamite clock ticking on the safe (the debt clock)'),
    (55.24,  'h11-b',  0.0, 'Oh, oh, oh', 'no picture for "oh": crew rapping in the snow'),
    (59.536, 'p02-a',  3.0, "Have resistance to the facts I'm stating", 'CRIMSON stating it: finger jabs, shrug, point at you'),
]
# chorus 1 shots keyed by line index; chorus 2 takes the same clips, same ins, on its own line starts
CHORUS = [
    ('cn:chase1-a', 0.5, 'Robbery! Robbery!', 'into the car chase on the first "Robbery!" (Kai)'),
    ('c02-a',       0.0, "Call the police, it's a robbery", 'call the police, held only while it is sung (Kai)'),
    ('k31-b',       1.5, 'Debasement, debasement', 'de-basement: the floor lowers them into the vault'),
    ('cn:safe4-b',  0.5, 'It happened in the basement', 'the "excellent basement scene" (Kai at 130.5)'),
    ('c03g-b',      0.0, "Printer is burring, now now what's a burring?", 'the printer in the red cellar'),
    ('cn:chase3-a', 1.0, 'Robbery! Robbery!', 'back to the chase'),
    ('x07m-b',      2.5, "Call the police, it's a robbery", 'the police arrive: axes in the barrels'),
    ('z06y-b',      1.5, 'Debasement, debasement', 'basement vault corridor, the stolen safe'),
    ('k13m-b',      1.0, 'It happened in the basement', 'the basement distillery'),
    ('c03g-b',      2.9, "Printer is burring, now now what's a burring?", 'the printer again, its later stretch'),
]
C1_STARTS = [61.788, 64.714, 66.966, 68.255, 69.532, 72.423, 74.374, 77.276, 78.576, 79.841]
C2_STARTS = [123.716, 126.642, 128.894, 130.183, 131.471, 134.374, 136.301, 139.215, 140.504, 141.793]
VERSES_3_4 = [
    (82.977, 'k21m-a', 3.0, 'Stacks and stacks of elastic cash', 'a crate of cash on the speedboat'),
    (85.008, 'q05-b',  0.0, 'Distracted by a dyspraxic flash', "MARINE's glove snaps open like a magician's flash"),
    (87.934, 'x04-a',  1.0, 'Marked angry at the shitty little drop', 'the drop: BOTTLE drops the sack off the boxcar'),
    (90.384, 'k27m-b', 4.0, 'The right and the left both witness the theft', 'a witness with a robber at his left and right'),
    (91.463, 'z06y-b', 3.5, 'both witness the theft', 'second thing on a strong hit: left and right either side of the stolen safe'),
    (92.764, 'h19-a',  0.0, 'Blaming each other is a sick little cover', 'blame: the crew all pointing fingers'),
    (95.016, 'd06m-a', 0.65, 'Institutional, dilutional, the usual', 'KEEP (Kai at 96.9): the barman dilutes the bottle'),
    (98.558, 'p12-a',  2.0, 'Distraction is the attraction', 'the distraction: a stage show with band and crowd'),
    (100.496,'k30m-a', 3.5, 'The intention is tension', 'tension: pliers tugged between them over the wires'),
    (102.005,'h07-b',  1.5, 'Between the factions, divide and conquer', 'no picture for factions: crew in a ring, jabbing down at you'),
    (104.351,'g08y-b', 0.0, 'Just look at the hand', "the magician's waving hand while the other pockets a note"),
    (105.326,'h18-b',  2.0, "It's not your standard propaganda", 'the show under the marquees, crowd clapping'),
    (106.626,'k12m-a', 2.5, 'Worth a couple grand, ah!', 'a couple of grand flung from the car'),
    (108.263,'q09-a',  0.8, 'It is state level manipulation', 'RUST at the snooker table, sweeping hand, manipulating'),
    (110.504,'d10-a',  0.0, 'It is the devil with the radio station', 'KEEP (Kai at 113.0): the devil-horn shadow in the radio booth'),
    (113.406,'d11-a',  0.0, 'Stack up the vaults like a wheelbarrow', 'a wheelbarrow of cash out of the vault'),
    (115.647,'d12-b',  2.0, 'Risk of default is really rather narrow', 'narrow: MARINE on a ledge high over the street'),
    (118.561,'h02-a',  1.0, 'Biggie said, wait!', 'no picture: crew raps on the salt flats'),
    (120.186,'q08-a',  1.0, "Rockin' 97 / Don't get high off your own supply", 'the gramophone shop: held over both lines so Kai can time the gramophone moment in Premiere'),
]
BREAK_V5 = [
    (144.033,'x06-a',  1.0, 'You know the real star is Pablo Escobar', 'Escobar: a smuggling speedboat under the searchlight'),
    (146.634,'k21m-a', 0.3, 'Who has elastic bands, not plastic hands', 'elastic bands: banknote bundles in a crate'),
    (149.119,'g08y-b', 2.5, 'not plastic hands', "second thing on a strong hit: the magician's gloved hand"),
    (149.722,'h17-b',  0.0, "Stackin' up the cash by the grand", 'banknotes raining on the crew'),
    (152.114,'x03m-b', 1.0, 'Stand up plans are for the working man', 'stand up: three stand in the blizzard, chopping on the beat'),
    (154.691,'h15-b',  1.0, 'And this right here is a next level scam', 'the scam lives first class: crew in the dining car'),
    (156.944,'a02m-a', 2.0, 'All gotten gains, no need to explain', 'ill-gotten gains: the bank lobby taken'),
    (159.521,'k23-a',  0.0, "Bailin' out will never mean the same", 'bailing out: MARINE slides down a rope from the blimp (instead of the train, Kai)'),
    (162.435,'q04-a',  3.55,"Own a printer and you don't feel winter", 'own a printer: the presses'),
    (163.074,'h11-b',  4.05, "don't feel winter", 'second thing on a beat: crew rapping warm in the snow'),
    (165.024,'h12-a',  3.4, 'Crime is asset inflation, passive creation', 'inflation: the balloon inflating behind the crew'),
    (167.602,'x02-a',  1.0, 'Of a wealth gap that drives the situation', 'drives: RUST drives the roadster, the pack falling behind'),
    (170.179,'h18-b',  0.3, "Rockin' people get paid in money", 'money falling on a cheering crowd'),
    (171.781,'q12-b',  2.5, "So it's not very funny when you print more", 'not funny: the crew wags its fingers, then points'),
    (174.057,'y04-a',  2.0, 'And expect them not to worry', "not worried: BOTTLE dusts his lapel in the fallen house"),
    (175.984,'h17-b',  2.6, 'Hungry people feed a revolution', 'THE TONE CHANGE (2:56): fire in the bank doorway, a whole new scene'),
    (177.935,'k16-a',  1.5, "Then it's retribution, perhaps some execution", 'execution: the tommy gun, glass and sparks'),
    (180.547,'y06-a',  2.8, "It's time to give, not just to take", 'give: the empty sack held out to you'),
    (183.554,'v11x-a', 1.3, "But for heaven's sake / Don't just eat cake", 'KEEP (Kai at 183.5): the man on the bank steps mimes the cake slice; held to the end'),
]

rows = list(INTRO) + list(VERSES_1_2)
rows += [(s, c, i, l, w) for s, (c, i, l, w) in zip(C1_STARTS, CHORUS)]
rows += list(VERSES_3_4)
rows += [(s, c, i, l, w + ' (chorus 2 = chorus 1)') for s, (c, i, l, w) in zip(C2_STARTS, CHORUS)]
rows += list(BREAK_V5)

plan = []
for k, (s, c, i, l, w) in enumerate(rows):
    e = rows[k + 1][0] if k + 1 < len(rows) else END
    plan.append({'start': round(s, 3), 'end': round(e, 3), 'clip': c, 'in': round(i, 3), 'line': l, 'why': w})
json.dump(plan, open(HERE / 'plan-C.json', 'w'), indent=1, ensure_ascii=False)
print(len(plan), 'shots')
