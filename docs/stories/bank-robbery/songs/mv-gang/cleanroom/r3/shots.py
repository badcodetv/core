"""Round 3 (Jack 2026-11-04): the singer, action-movie parodies, big sarcastic stage gestures.
Plain facts per shot, no prompt wording. Each family goes to one sealed writer.
Groups: h = the singer (no reference, solo), k = action parody, g = gang gesture (both with the line-up reference)."""

GANG = """# The gang (who they are, in facts)

Six robbers, the same six all through the video. A reference image of all six is ATTACHED to every gang prompt: standing in a row facing the camera, left to right PLUM, BOTTLE, CRIMSON, MARINE, RUST, SILVER. Say in one plain sentence that the masks and suits are exactly as in the attached reference image, and name which men are in the shot. Do not describe the reference picture's wall or the row itself.

- PLUM: plum balaclava, chalk-striped mustard-yellow three-piece suit. Broad. The vain one.
- BOTTLE: bottle-green balaclava, brown tweed suit. Quiet, does the carrying.
- CRIMSON: crimson balaclava, charcoal pinstripe double-breasted suit, grey fedora on top of the mask. The loud one.
- MARINE: marine-blue balaclava, cream linen suit, two-tone shoes. Thin and fast.
- RUST: rust-gold balaclava, black double-breasted suit, white tie. The driver.
- SILVER: silver-grey balaclava, oxblood-red suit, bow tie. The tall one.

The mask, every time:
- Hand-knitted rib wool over the whole head and neck, the neck tucked inside the shirt collar. NO eye, nose or mouth holes.
- A large WHITE wool ring stitched round the whole face from brow to chin.
- One small solid red felt triangle with rounded corners, high inside the ring over the man's LEFT eye. Facing the camera it is on the RIGHT side of the picture, at about two o'clock. Same on every man in every shot.
- No skin anywhere: black leather gloves on both hands, cuffs over the wrists, collar up. Nothing mechanical either: no metal, lights, visor or seams on the mask.
"""

SINGER = """# The singer (facts; you are designing her)

The song's lead voice is a woman with a cockney accent, rapping and singing. The director wants her in the video throughout, rapping and singing to camera, "a harley quinn type character with a bat, with the badcode balaclava style". She must be an ORIGINAL character: the spirit (gleeful, chaotic, playful one second and dangerous the next, the bat as her prop) without copying any existing character. Never name any existing character in a prompt. Avoid every signature element listed in section 3 of the research: no red-and-black or two-tone split colours, no diamond or harlequin pattern, no jester hood or bells, no domino mask, no pigtails or bunches, no face paint, no mallet, no writing on the bat, no baseball-jersey-and-hot-pants look.

Her balaclava follows the same rule as the gang's: hand-knitted wool over the whole head and neck, no eye, nose or mouth holes, a large WHITE ring stitched round the whole face, one small solid red felt triangle with rounded corners high inside the ring over her LEFT eye (facing camera: the RIGHT of the picture, two o'clock). No skin and no hair show anywhere: gloves, stockings or sleeves cover everything. You choose the balaclava's colour; a hat or headpiece over it is fine. Her silhouette, costume, posture and the bat carry the whole character because there is no face.

Each of your two shots is a DIFFERENT design of her (a different costume idea, colour and setting), given below as a starting idea you may push further. She is alone in the frame or the gang is only a soft background. One still each: her rapping/singing to the camera mid-gesture with the bat, full figure or three-quarter so the costume reads.
"""

GLOSS = """# What the director wants now (facts from his notes)

- "Prohibition era glossyness": the glamour of a high-budget period film. Section 2 of the research says what that is (art deco materials, lacquered cars, chrome, crystal, satin, one hard key light, deep blacks) and how it differs from plastic "AI slop" (everything wet and shiny, airbrushed, evenly lit, generic). Earlier rounds: he hated AI slop, psychedelic effects, matching-colour crowds, people wandering in for no reason; he loved a specific place, one motivated light, real materials, colour in walls and clothes.
- "action movie scenes, as if they are parodied but with the badcode balaclava men": the big action-movie set piece played straight and too cool, with one deadpan or absurd touch that gives the joke away.
- Rappers "not gesturing enough, they kind of just point sometimes": big stage-rapper performance moves (section 4), caught at the extreme of the move, done sarcastically.
- Faults seen before: the red triangle drifting to the centre or the wrong eye; a bare hand; signs printing made-up words.
"""

FAMILIES = {
    # --- the singer: 5 writers x 2 designs ---
    "w1": ("the singer", [
        ("h01", "verse 1", "they say you can't make money from a tree", "Starting idea: a speakeasy chanteuse in a beaded, fringed knee-length evening dress, the bat resting across her shoulders, singing from a small speakeasy stage.", True),
        ("h02", "chorus", "call the police, it's a robbery", "Starting idea: a gangster's girl gone rogue in a man's pinstripe suit cut down to fit her, braces, a fedora over the mask, standing on a marble bank counter tapping the bat on her palm.", True),
    ]),
    "w2": ("the singer", [
        ("h03", "verse 3", "distraction is the attraction", "Starting idea: a vaudeville acrobat and strongwoman in a period stage costume with a short cape and tights, twirling the bat on a theatre stage in a spotlight.", True),
        ("h04", "verse 4", "it is the devil with the radio station", "Starting idea: an aviatrix in a leather flying coat, jodhpurs and boots, goggles pushed up on the mask, standing on the lower wing of a parked biplane, the bat pointed like a conductor's baton.", True),
    ]),
    "w3": ("the singer", [
        ("h05", "verse 5", "own a printer and you don't feel winter", "Starting idea: an heiress in a huge fur coat over a silk slip dress and long pearls, sprawled on a pile of stolen banknotes in a vault, the bat across her knees.", True),
        ("h06", "verse 2", "rent seeking, I'm just about eating", "Starting idea: a street tough in a flat cap and an oversized man's overcoat, a tape-wrapped bat, sitting on a tenement stoop with one foot up.", True),
    ]),
    "w4": ("the singer", [
        ("h07", "chorus", "debasement, it happened in the basement", "Starting idea: a cabaret showgirl with a tall feather headdress over the mask, sequins, using the bat like a cane in a kick, a speakeasy cabaret floor.", True),
        ("h08", "action", "Robbery!", "Starting idea: the getaway driver in a long leather duster and driving gloves, riding the running board of a speeding 1920s sedan, the bat held out, coat flying.", True),
    ]),
    "w5": ("the singer", [
        ("h09", "verse 5", "bailing out will never mean the same", "Starting idea: a widow in black lace mourning dress with a veil over the mask at a rich banker's funeral, leaning on the bat like a walking stick, mock grief.", True),
        ("h10", "verse 5", "it's time to give, not just to take", "Starting idea: a white dinner jacket, bow tie and top hat over the mask, the bat used as a showman's cane, at the top of a grand art deco staircase.", True),
    ]),
    # --- action parodies: 4 writers x 4 ---
    "w6": ("action-movie parodies: streets and banks", [
        ("k01", "3:07", "Robbery! (the outro)", "Trope: the slow walk away from an explosion. All six walk toward camera out of a bank as the vault blows behind them in a cloud of banknotes; nobody looks back; PLUM lights a cigar off a burning ledger.", False),
        ("k02", "0:08", "Robbery!", "Trope: the truck through the wall. A beer truck reverses through the brick wall of an empty bank lobby, bricks and barrels flying, RUST at the wheel, CRIMSON on the running board, gun up.", False),
        ("k03", "1:02", "Robbery, robbery!", "Trope: the slow-motion dual-wield dive. MARINE mid-air sideways across a marble bank lobby, a Tommy gun in each hand pointed at the ceiling, chandelier crystals raining.", False),
        ("k04", "0:13", "the music kicks in", "Trope: the V-formation power walk. All six walk a wet night street toward the lens under a glowing theatre marquee (no readable letters), coats flaring, CRIMSON at the point.", False),
    ]),
    "w7": ("action-movie parodies: cars and chases", [
        ("k05", "1:25", "distracted by a dyspraxic flash", "Trope: the leap between moving cars. SILVER jumps from the running board of one speeding Packard to another on a cobbled avenue, one hand holding nothing but his tie.", False),
        ("k06", "1:04", "call the police", "Trope: the car flip. A police Model T has flipped into a fruit stall, oranges in the air; the policeman climbs out unhurt shaking his fist; the gang's car speeds past.", False),
        ("k07", "0:25", "work can get paid though", "Trope: the handbrake turn. RUST slides a black running-board sedan sideways round a city corner, white-wall tyres smoking, BOTTLE leaning out the window, gun up.", False),
        ("k08", "2:57", "hungry people feed a revolution", "Trope: the impossible jump over an opening bridge. The gang's sedan in the air over a rising bascule bridge above a river, police cars stopped at the edge.", False),
    ]),
    "w8": ("action-movie parodies: water, rails, air", [
        ("k09", "2:44", "crime is asset inflation", "Trope: the boat chase. A mahogany rum-runner speedboat leaps a wake at night, a Coast Guard searchlight on it, crates bouncing, PLUM standing in the back like a captain.", False),
        ("k10", "1:44", "it is the devil with the radio station", "Trope: the train-roof run. BOTTLE and MARINE run along the roof of a steam express crossing a trestle, a sack of cash each, hats flying off behind.", False),
        ("k11", "3:20", "the end", "Trope: the plane escape. A tri-motor plane takes off from a field, a rope ladder dangling with SILVER on it waving, police cars far behind.", False),
        ("k12", "2:29", "stacking up the cash by the grand", "Trope: the money rain. Banknotes blow out of a sack in an open roadster speeding down a boulevard, falling on a delighted crowd, CRIMSON throwing handfuls.", False),
    ]),
    "w9": ("action-movie parodies: interiors", [
        ("k13", "1:37", "the intention is tension", "Trope: the Mexican stand-off, parodied. Five of the gang in a circle in a speakeasy, each aiming a gloved finger-gun at the next man, dead serious, all frozen; one is holding a banana the same way.", False),
        ("k14", "2:52", "passive creation of a wealth gap", "Trope: bullet time. A frozen instant over a casino table: a shattered champagne coupe, droplets, cards and chips in the air, PLUM mid-flip over the table.", False),
        ("k15", "2:14", "you know the real star", "Trope: the chandelier swing. MARINE swings across an art deco ballroom on a crystal chandelier, Tommy gun pointed up, dancers ducking.", False),
        ("k16", "1:37", "between the factions", "Trope: shooting out the lights. CRIMSON fires a Tommy gun along a row of hanging lamps in a long bank hall, the lamps bursting one after another, the hall dropping into silhouette.", False),
    ]),
    # --- gestures: 3 writers x 4 ---
    "w10": ("big sarcastic stage-rap gestures, part one", [
        ("g01", "0:20", "they say you can't make money from a tree", "PLUM raps into a wide lens close to him in a gilded bank vault, his flat gloved hand chopping down on the beat, the other on his hip, mock-lecturing.", True),
        ("g02", "0:27", "where does it go? nobody knows", "CRIMSON gives a huge exaggerated shrug into the lens, both palms up, head tilted far over, shoulders up to his ears, an empty cash drawer behind.", True),
        ("g03", "0:31", "means of production, means of reduction", "BOTTLE counts off points on his gloved fingers right up in the lens, leaning in, on a factory floor full of idle machines.", True),
        ("g04", "0:43", "sorry, did I interrupt your meeting?", "MARINE in a boardroom doorway, a gloved fist pressed to his heart far too long and a mock-solemn bow, the bankers frozen behind.", True),
    ]),
    "w11": ("big sarcastic stage-rap gestures, part two", [
        ("g05", "0:48", "it prints all the dollars that the government spends", "SILVER stands dead still by a roaring printing press doing a tiny limp 'raise the roof' with one hand, totally deadpan.", True),
        ("g06", "1:07", "debasement, debasement", "All six in a brick basement round the printing press, everyone's hands up together on the hook, mid-bounce, knees bent, in sync.", True),
        ("g07", "1:28", "the right and the left both witness the theft", "RUST, arms flung wide, points with both hands in opposite directions at the same time, wide stance on a street corner between two arguing crowds.", True),
        ("g08", "1:44", "just look at the hand", "PLUM holds one gloved hand up to the lens like a stage magician, fingers spread, while his other hand behind him slips a banknote into his pocket.", True),
    ]),
    "w12": ("big sarcastic stage-rap gestures, part three", [
        ("g09", "1:48", "it is state level manipulation", "CRIMSON lunges into a very wide lens close to camera shouting through a brass megaphone, one foot up on a crate of gin, in a rally hall with bunting.", True),
        ("g10", "2:01", "don't get high off your own supply", "MARINE wags one finger at the lens like a schoolteacher, his other hand on a stack of gin crates, a speakeasy bar behind.", True),
        ("g11", "2:34", "stand up plans are for the working man", "BOTTLE does a slow sarcastic clap, deadpan, sitting on a bank counter, legs swinging, the tellers' cages behind.", True),
        ("g12", "3:00", "it's time to give, not just to take", "SILVER on a speakeasy stage at a period chrome microphone on a stand, his elbow up gripping it, his free arm sweeping over the crowd, wide stance.", True),
    ]),
}

# --- round 3b (Jack 2026-11-04: "please come up with more parodied action scenes"), from research-more-action.md ---
MORE = {
    "w13": ("silent-era stunt parodies", [
        ("k17", "2:52", "crime is asset inflation", "Hanging off the clock face: PLUM hangs from the minute hand of a huge bank clock high above 1920s traffic, a cash bag in his other hand, checking his wristwatch against it. Plain clock face with tick marks, no numbers.", False),
        ("k18", "0:33", "standards bleeding, landlords needing", "The falling building front, the moment just after: a two-storey timber house front lies flat in a muddy street, dust settling, and BOTTLE stands untouched in the rectangular hole of its open window, straightening his tie.", False),
        ("k19", "2:32", "stand up plans are for the working man", "Lunch on the girder: all six sit in a row on a steel I-beam high over a 1920s city going up, legs dangling, rivet buckets beside them, passing round sandwiches and stacks of banknotes.", False),
        ("k20", "2:29", "stacking up the cash by the grand", "The wing walk: SILVER stands on the top wing of a flying biplane over cornfields, a cash bag in one hand, stepping across toward a second plane's wingtip just at the edge of the frame; his hat perfectly in place in the gale.", False),
    ]),
    "w14": ("Prohibition kit parodies: water and air", [
        ("k21", "1:23", "stacks and stacks of elastic cash", "Money overboard, daylight, wide: a rum-runner speedboat off the coast at dawn, CRIMSON and MARINE tipping a crate of banknotes over the stern, a mile-long wake of floating pale green paper behind, a patrol boat tiny on the horizon.", False),
        ("k22", "0:27", "earning that dough, but where does it go", "Hanging off the El: RUST stands on the outside step of an elevated-railway car rounding a curve above a city street, one hand on the grab rail, a cash bag in the other; a commuter inside hands him a ticket through the window.", False),
        ("k23", "1:48", "it is state level manipulation", "The airship drop: a blimp nudges the mooring mast on top of a skyscraper; one robber (MARINE) slides down a single line, the rest already standing on the observation deck. No name on the blimp.", False),
        ("k24", "2:49", "crime is asset inflation", "Ballast is money: a gas balloon high over the city, PLUM and BOTTLE in the basket throwing out sacks of banknotes to rise, already above the clouds, delighted.", False),
    ]),
    "w15": ("Prohibition kit parodies: on the ground", [
        ("k25", "1:38", "distraction is the attraction", "The instrument case: in a marble bank lobby SILVER has opened a violin case and, deadpan, is playing the violin, while behind him the others walk out with sacks of cash.", False),
        ("k26", "1:58", "risk of default is really rather narrow", "The axe raid: the gang sit at a card table in a speakeasy back room and keep playing as axe heads splinter through the wooden door and walls around them; CRIMSON holds up one finger, 'one moment'.", False),
        ("k27", "0:46", "remember kids, the Fed is not your friend", "The gold-vault glow: a huge round vault door swung open, golden light flooding out over PLUM and CRIMSON; inside there is no gold, only a startled clerk in a green eyeshade at a printing press.", False),
        ("k28", "2:39", "bailing out will never mean the same", "The motorcycle through the billboard: MARINE on a 1920s motorcycle has just burst through a painted roadside billboard (a smiling family picture, no words), leaving a cartoon-shaped hole of bike and rider.", False),
    ]),
    "w16": ("heist-film clichés", [
        ("k29", "1:35", "institutional, dilutional, the usual", "The bells on threads: five taut threads with one small brass bell each across a vault corridor; MARINE goes through like a ballet dancer, while BOTTLE behind him just walks straight through them.", False),
        ("k30", "0:51", "its fiat system is insistent on debt's existence", "Cut the red wire: a bundle of dynamite sticks with an alarm clock strapped on, against a bank safe; CRIMSON and RUST argue over three wires (red, blue, white) with pliers, SILVER beside them simply holding the clock's bell still with one finger. Nobody near anyone else, it is plainly a prop.", False),
        ("k31", "1:56", "risk of default", "The cut circle in the floor, after: looking up from inside a vault, a disc of floor has dropped through, and PLUM and BOTTLE sit on chairs on it, legs crossed, plaster dust falling round them through the round hole above.", False),
        ("k32", "1:32", "blaming each other is a sick little cover", "The mask under the mask: a robber dressed as a 1920s banker in a top hat holds a rubber banker's face mask he has just peeled off; underneath is his balaclava (SILVER).", False),
    ]),
    "w17": ("machines, rivers, fuses", [
        ("k33", "2:41", "own a printer and you don't feel winter", "Rolling under the closing vault door: a heavy steel shutter is coming down; BOTTLE has rolled under it and reaches back under the last gap to grab his hat.", False),
        ("k34", "2:35", "and this right here is a next level scam", "Off the bridge onto the barge: MARINE in his cream linen suit has just landed on a coal barge passing under a steel bridge, standing on the coal, spotless.", False),
        ("k35", "2:57", "it's not very funny when you print more", "The steamroller chase: a road-building steamroller chasing RUST down a street at walking pace; he walks at exactly the same pace, lighting a cigar.", False),
        ("k36", "3:04", "but for heaven's sake don't just eat cake", "Lighting cigars from the fuse: a sputtering fuse runs across a bank floor to the safe; all six bend to light their cigars off it as it passes.", False),
    ]),
}
FAMILIES.update(MORE)
