"""The shot list for the balaclava-gang round: plain facts of what each picture must show, from the
lyrics of `the version.wav` (times from song-transcript.json, loose). No prompt wording lives here.
Each family goes to one sealed writer. RAP = a gang member raps into the lens in this shot."""

GANG = """# The gang (who they are, in facts)

Six robbers. Each wears a hand-knitted wool balaclava of one colour, a sharp 1920s suit, black leather gloves, collar turned up. They are the same six all through the video, so keep each one's colours exactly:

- PLUM: plum balaclava with a cream ring, chalk-striped mustard-yellow three-piece suit. Broad. The vain one.
- BOTTLE: bottle-green balaclava with an oatmeal ring, brown tweed suit. Quiet, does the carrying.
- CRIMSON: crimson balaclava with a cream ring, charcoal pinstripe double-breasted suit, grey fedora on top of the mask. The loud one.
- MARINE: marine-blue balaclava with a cream ring, cream linen suit, two-tone shoes. Thin and fast.
- RUST: rust-gold balaclava with a black ring, black double-breasted suit, white tie. The driver.
- SILVER: silver-grey balaclava with a crimson ring, oxblood-red suit, bow tie. The tall one.

The mask, every time:
- Hand-knitted rib wool covering the whole head and neck, the neck tucked down inside the shirt collar.
- NO holes at all: no eye holes, no mouth hole, no nose. Unbroken knit where the face would be.
- A thin ring in a contrasting wool, chain-stitched round the face like the outline of a face, as wide as the face from brow to chin.
- One small solid red felt triangle with rounded corners, sewn inside the ring, high over the wearer's RIGHT eye. When he faces the camera, it is on the LEFT side of the picture. Same eye on every man in every shot.
- No skin shows anywhere: gloves on both hands, cuffs down over the wrists, collar up. Nothing human is visible, so he could be anything under there, but there is nothing mechanical either: no metal, no lights, no visor, no seams. Just cloth, wool and leather.
"""

RAP = """# Rapping to the camera

When a shot says RAP, one gang member (named) is rapping straight into the lens, close and wide-angle, mid-gesture: the director's words are "rapping to the camera and gesturing like eminem". Hands do the talking because the mask has no mouth: pointing into the lens, a flat hand chopping the beat, fingers counting, a fist to the chest, leaning right into the camera. The action of the line happens behind or around him. A man-sized face in the foreground does not stop the frame being wild."""

FAMILIES = {
    "w1": ("streets and the bank front, morning to noon", [
        ("a01", "0:00", "intro guitar", "All six gang members walk side by side straight toward the camera down a 1920s city street, Tommy guns resting on shoulders pointing at the sky, a bank's columns behind them.", False),
        ("a02", "0:08", "Robbery!", "The bank's big brass-and-glass front doors burst inward as the gang comes through; CRIMSON first, gun up at the ceiling, customers flinching.", False),
        ("v10", "0:44", "sorry, did I interrupt your meeting?", "A wood-panelled boardroom of old bankers in a meeting; the door has just swung open and MARINE stands in it, one gloved hand raised like a polite apology, the bankers frozen mid-cigar. RAP (MARINE).", True),
        ("v11", "0:46", "remember kids, the Fed is not your friend", "SILVER wags one gloved finger into the lens on the steps of a huge columned central-bank building. RAP (SILVER).", True),
    ]),
    "w2": ("homes and tenements, winter", [
        ("v06", "0:33", "standards bleeding, landlords needing", "A fat landlord in a fur-collared coat holds his palm out at a tenement doorway to a tired working family; BOTTLE leans on the door frame beside him. RAP (BOTTLE).", True),
        ("v07", "0:36", "grandma FREEZING", "Exactly this: an old grandmother in an unheated tenement flat, frost on the inside of the window, her breath visible, wrapped in three blankets, her cup of tea with ice on it, an empty grate. PLUM is kneeling and wrapping his mustard jacket round her shoulders.", False),
        ("v09", "0:41", "rent seeking? I'm just about eating", "CRIMSON at a bare kitchen table eating one single bean off a fork from an empty tin, a rent demand pinned to the wall. RAP (CRIMSON).", True),
        ("f03", "2:42", "own the printer and you don't fear winter", "Snow falling outside a tall window; inside a warm rich study, RUST sits in a leather armchair by a fire that is burning banknotes, his gloved feet up.", False),
    ]),
    "w3": ("the money and the printing press, a basement", [
        ("v12", "0:49", "it prints all the dollars that the government spends", "A huge iron printing press spitting sheets of banknotes into the air, BOTTLE feeding paper in, notes flying everywhere.", False),
        ("c03", "1:07", "debasement! it happened in da basement!", "The whole gang crammed in a brick basement round the printing press under one red bulb, all six facing the lens, fists up, chanting.", True),
        ("c04", "1:10", "printer is burning", "The printing press is on fire, banknotes catching and curling, smoke, and MARINE stands in front of it unbothered, rapping. RAP (MARINE).", True),
        ("d01", "1:23", "stacks and stacks of elastic cash", "A table piled with bricks of banknotes bound with rubber bands; PLUM fans a brick at the lens like a card trick.", True),
    ]),
    "w4": ("the bank lobby and vault", [
        ("c01", "1:02", "Robbery, robbery!", "All six gang members in a marble bank lobby, guns pointed up at the chandelier, shouting into a very wide lens close to them, customers face-down on the floor behind.", True),
        ("d11", "1:53", "stack up the vaults like a wheelbarrow", "BOTTLE pushes a wooden wheelbarrow overflowing with cash out of a round vault door, notes spilling.", False),
        ("e02", "2:27", "who has elastic bands, not plastic hands", "Close-up of two gloved hands snapping a rubber band round a fat brick of banknotes, on a vault counter.", False),
        ("v13", "0:52", "this fiat system is insistent on debt's existence", "SILVER sits on top of a mountain of bound ledgers and paper IOUs wrapped in chains, in a bank's archive room. RAP (SILVER).", True),
    ]),
    "w5": ("cars: hot rods and getaways", [
        ("a03", "0:13", "instrumental", "A black getaway sedan skids sideways round a city corner at speed, RUST at the wheel, MARINE on the running board holding on.", False),
        ("x01", "chorus 2", "action", "A running-board shootout: two 1920s sedans side by side at speed on a city avenue, gang members on the running board firing Tommy guns into the air, muzzle flash.", False),
        ("x02", "outro", "action", "Stripped-down 1920s hot rod roadsters racing flat out across a white dry lake bed at sunset, dust plumes, RUST driving the lead car.", False),
        ("x03", "verse 5", "action", "Night, a blizzard on a frozen river: a convoy of whiskey cars crossing the ice with their doors taken off, and the gang stepping out of the snow in front of them, Tommy guns up, headlights on them.", False),
    ]),
    "w6": ("the crowd and the street", [
        ("v03", "0:25", "work and get paid though, earning that dough", "Factory workers in overalls clocking in at a punch clock, a long line; CRIMSON walks the line rapping. RAP (CRIMSON).", True),
        ("v04", "0:27", "but where does it go? nobody knows!", "A worker opens his pay envelope and the notes blow out of it, down the street and in through the window of a bank; PLUM shrugs huge at the lens.", True),
        ("d03", "1:28", "mob, angry at their shitty little job", "An angry crowd of factory workers shaking fists at the gates of a smoking factory.", False),
        ("f08", "3:00", "it's time to give, not just to take", "The gang's open getaway car drives slowly through a poor street, MARINE and PLUM throwing handfuls of banknotes to cheering people.", False),
    ]),
    "w7": ("the theatre and the trick", [
        ("d02", "1:25", "distracted by a dyspraxic flash", "A press photographer's flash bulb goes off right in the lens; BOTTLE stumbles, dropping a sack of cash, white glare.", False),
        ("d07", "1:39", "distraction is the attraction", "A theatre stage: a magician sawing a woman in a box in the spotlight; in the audience's dark seats the gang is picking every pocket.", False),
        ("d08", "1:44", "divide and conquer, just look at the hand", "SILVER holds one gloved hand up right in front of the lens, open palm, as if doing a magic trick; behind, his other hand slides a wallet away. RAP (SILVER).", True),
        ("d10", "1:50", "it is the devil, with a radio station", "A 1920s radio studio lit red: CRIMSON at a big chrome radio microphone, and on the wall behind him his shadow has devil's horns. RAP (CRIMSON).", True),
    ]),
    "w8": ("height and danger", [
        ("d12", "1:56", "risk of default is really rather narrow", "MARINE edges along a narrow stone ledge on the side of a skyscraper high above the street, a sack of cash in one hand.", False),
        ("f01", "2:35", "and this right here is a next level scam", "The gang sits along a steel girder high above the city, legs dangling, counting cash. RAP (CRIMSON in front).", True),
        ("x04", "chorus 2", "action", "A steam mail train halted in the countryside, steam everywhere; the gang stands on the roof of the mail car throwing mail sacks down to the getaway car, chanting at the lens.", True),
        ("x05", "chorus 2", "action", "A police motorcycle cop with sidecar chases the gang's sedan down a hill street, the gang shooting into the air from the back window.", False),
    ]),
    "w9": ("water and liquor", [
        ("d06", "1:35", "institutional, dilutional, the usual", "A speakeasy barman pouring water into a whiskey bottle behind the bar; BOTTLE watches over the bar, unimpressed. RAP (BOTTLE).", True),
        ("v14", "2:01", "don't get high off your own supply", "RUST pushes away a glass of the gang's own bootleg moonshine offered by PLUM, in the room with their copper still. RAP (RUST).", True),
        ("x06", "chorus 2", "action", "A rum-runner speedboat at night tearing across a bay, a Coast Guard searchlight on it, crates of liquor in the stern, gang aboard.", False),
        ("x07", "break", "action", "A police raid on a roadhouse: cops smashing whiskey barrels with axes, liquor flooding the floor, the gang slipping out the back.", False),
    ]),
    "w10": ("the rich", [
        ("f02", "2:40", "'bail' and 'out' will never mean the same", "Exactly this: three bankers in top hats in a sinking rowing boat, bailing water out with buckets of banknotes.", False),
        ("f04", "2:45", "crime is asset inflation", "A huge hot-air balloon made of stitched banknotes inflating over a mansion lawn, the rich waving from its basket; SILVER looks up at it, arms folded.", False),
        ("f05", "2:51", "working people get paid in money ... print more", "A working man pushes a wheelbarrow full of banknotes to a bakery counter to buy one small loaf of bread; RUST behind him counts on his fingers. RAP (RUST).", True),
        ("f09", "3:04", "don't just eat cake", "A rich banquet: a dowager in pearls with a fork in a huge cake, and the gang lowering in through the skylight on ropes above her.", False),
    ]),
    "w11": ("the countryside and the factory", [
        ("v01", "0:20", "they say, ya can't make money from a tree", "An orchard: PLUM shakes a tree and banknotes rain down out of its branches instead of leaves. RAP (PLUM).", True),
        ("v02", "0:23", "each day, make hay, not free", "A hay field at harvest: BOTTLE forks a hay bale and it bursts open full of banknotes.", False),
        ("v05", "0:31", "means of production means a reduction", "A giant factory machine room, a factory owner in a top hat at the controls while workers shrink away; MARINE in front. RAP (MARINE).", True),
        ("v08", "0:39", "stimulus checks are next. Get wrecked!", "Paper cheques fluttering down from a high window over a crowded street like ticker tape; RUST snatches one out of the air.", False),
    ]),
    "w12": ("blame, police and the people", [
        ("d05", "1:33", "the right and the left both witness the theft / blaming each other", "Two men in the street jabbing fingers in each other's faces, arguing, while behind them the gang calmly walks off carrying the bank's safe.", False),
        ("c02", "1:04", "call the police, it's a robbery!", "A cop shouting into a police call box telephone on a street corner, while the gang's car tears past behind him.", False),
        ("f06", "2:56", "hungry people feed a revolution", "A long bread line of hungry people that turns, further down the street, into a march with torches; SILVER walking at the front. RAP (SILVER).", True),
        ("e03", "2:32", "standard plans are for the working man", "A tired worker with a lunch pail on a tram, and CRIMSON sitting beside him, both swaying with the tram. RAP (CRIMSON).", True),
    ]),
}
