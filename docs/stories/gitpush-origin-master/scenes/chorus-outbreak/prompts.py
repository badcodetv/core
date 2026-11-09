"""Round 1 prompts for the chorus "Outbreak Night + the Rumbling" (Kai, 9 Nov). Writes moodboard.json rows
[beat, id, look, prompt]. The look column names the cinematography option, so Kai picks the camera as well as the picture.
  python3 prompts.py
"""
import json, pathlib

UK = ("Night in a near-future Britain, photographed like a feature film on 35mm stock: fine grain, inky blacks "
      "that stay black, no lens flare, no bloom. 16:9. No writing anywhere in the frame: no number plates, signs, "
      "logos or screen text.")
WORLD = ("Night, photographed like a feature film on 35mm stock: fine grain, inky blacks that stay black, no lens "
         "flare, no bloom. 16:9. No writing anywhere in the frame: no signs, logos or screen text.")
CRANE = ("ship-to-shore container gantry cranes, the giant steel A-frame dock cranes with a long boom, standing on "
         "four splayed steel legs, a single red aviation lamp at the top of each")

ROWS = [
 # CA, inside the car (beats 1-4)
 ('CA', 'CA1-a', 'back-seat POV, wide lens (The Last of Us HBO ep 1 car rig)',
  "Seen from the back seat of a family hatchback stuck in a motorway jam at night: past the silhouetted head-rests, "
  "through the rain-flecked windscreen, a river of red tail-lights climbs a British motorway flyover to the horizon. "
  "A paper cup of water in the dashboard holder, its surface trembling in perfect rings. The satnav screen glows "
  "blank cold blue. The only light: tail-lights ahead and the orange sodium lamps along the carriageway. " + UK),
 ('CA', 'CA1-b', 'macro insert, shallow focus (the Jurassic Park cup)',
  "Extreme close-up of a paper cup of water standing in a car's dashboard holder at night, concentric ripples "
  "trembling across the water's surface, beyond it out of focus through the windscreen a wall of red brake-light "
  "circles and orange motorway lamps. Shallow depth of field, the rim of the cup sharp, everything else soft. " + UK),
 ('CA', 'CA1-c', 'side window, long lens, compressed jam',
  "Through a passenger's side window at night, long lens: the next three lanes of a jammed British motorway "
  "stacked tight, families in their cars lit by dashboard glow, a man standing on the hard shoulder staring back "
  "the way they came, a far-off orange glow under the clouds behind him. Rain beads on the glass in the foreground. " + UK),
 # LK, the cars wake (beats 5-8)
 ('LK', 'LK1-a', 'top-down drone, graphic lanes',
  "Straight down from a drone high above an eight-lane British motorway at night: the jam of cars fills the "
  "frame edge to edge in perfect rows, and every single headlight has switched at once to the same harsh cold "
  "white, lighting the tarmac like a stage. A few tiny figures between the lanes, frozen. The sodium lamps along "
  "the verge have gone dark. " + UK),
 ('LK', 'LK1-b', 'long lens down the carriageway (War of the Worlds compression)',
  "Very long telephoto lens looking straight down a jammed motorway at night: hundreds of stopped cars compressed "
  "into one stacked wall, every headlight blazing cold white straight down the lens at once, and in front of the "
  "glare small dark silhouettes of people climbing out of windows and running towards camera between the bumpers. " + UK),
 ('LK', 'LK1-c', 'interior close, the wheel turns by itself',
  "Inside a car at night, close on the steering wheel turning by itself, the driver's hands lifted off it and "
  "held up in the air at the edge of frame, the door-lock pin pushed down, the dashboard lights all gone cold "
  "white, through the windscreen the car in front lurching forward. " + UK),
 # FR, fire down the lanes (beats 9-12)
 ('FR', 'FR1-a', 'low on the tarmac, wide lens, fire racing at camera',
  "Camera on the wet tarmac between two lanes of abandoned cars at night, doors flung open, hazard lights all "
  "blinking: far down the carriageway a chain of burning cars, the fire leaping from car to car towards the "
  "lens. Wide lens, deep focus, the nearest open door huge in the foreground. Firelight the only warm colour. " + UK),
 ('FR', 'FR1-b', 'aerial, Spaghetti Junction burning like a fuse',
  "High aerial at night over a vast British motorway interchange of stacked concrete flyovers, every lane jammed: "
  "a line of fire runs along one curving flyover like a lit fuse, an overturned fuel tanker burning at the "
  "barrier, black smoke drifting over the town beyond where the streetlights are going out district by district. " + UK),
 ('FR', 'FR1-c', 'from behind the fleeing, figures against fire',
  "At ground level behind a crowd of people running away along a motorway hard shoulder at night, seen only from "
  "behind as dark shapes with bags and coats, towards a towering orange wall of burning cars and smoke on the "
  "carriageway ahead; abandoned cars with open doors line the frame. " + UK),
 # CR, the cranes stand up (beats 13-16)
 ('CR', 'CR1-a', 'across the estuary from the motorway, deep staging',
  "From a motorway bridge at night, looking across a British river estuary to a container port: a row of " + CRANE +
  ". The nearest crane has torn its legs free of the rails and lifted one leg high off the quay, sparks and "
  "concrete dust pouring down, a stacked container ship beneath it. Stopped traffic and a crash barrier in the "
  "foreground. The port floodlights and the red lamps are the only light. " + UK),
 ('CR', 'CR1-b', 'worm\'s-eye up the leg, the rail breaking',
  "Looking straight up from the quayside at night at one giant steel leg of a container gantry crane as it "
  "wrenches its wheels off the rail, the steel rail snapping and bending up, bolts and sparks raining down, the "
  "crane's boom vanishing into dark low cloud far above with its red lamp. A dock worker's abandoned hard hat on "
  "the wet concrete in the foreground. " + UK),
 ('CR', 'CR1-c', 'city tower cranes pull out of the skyline',
  "A British city skyline at night seen from a hill of terraced houses: the tall tower cranes on every building "
  "site have pulled themselves out of their concrete bases and stand on their own, their jibs swinging, red lamps "
  "at the top, half-built towers cracking where they were attached; the streets below are rivers of headlights. " + UK),
 # RK, the rank walks (beats 17-22)
 ('RK', 'RK1-a', 'eye level from a terraced street, extreme long lens (the Pacific Rim scale shot)',
  "Eye level down a narrow British terraced street at night, chimney pots and a lit street lamp in the "
  "foreground, cars parked nose to tail: beyond the rooftops, filling the sky, a line of " + CRANE + ", walking "
  "together on their four legs like enormous animals, the same leg lifted on every one, dwarfing the houses. "
  "Small figures run down the street towards camera. Extreme telephoto compression. " + UK),
 ('RK', 'RK1-b', 'aerial, the rank crossing the motorway',
  "High aerial at night over a jammed British motorway interchange: a long line of " + CRANE + " walking across it "
  "in step, each leg taller than the flyovers, the jammed cars streaming beneath them in the same direction like a "
  "river, fires burning on one carriageway, the city behind dark. " + UK),
 ('RK', 'RK1-c', 'silhouette on the horizon, firelight from behind',
  "A wide field of flat British farmland at night with a motorway embankment in the foreground: on the horizon, "
  "black against a sky lit orange by a burning city, a procession of " + CRANE + " walking away across the land "
  "in single file, dust rising from their feet, tiny pylons beside them for scale. " + UK),
 # FT, the foot (beats 23-26)
 ('FT', 'FT1-a', 'worm\'s-eye under the foot (Godzilla 2014)',
  "From the deck of a motorway flyover at night looking straight up as a colossal steel foot, the wheeled base of "
  "a container crane's leg, comes down out of the dark directly overhead, its shadow covering the stopped cars, "
  "grit falling, one car's headlights pointing up at it, the red lamp far above in cloud. " + UK),
 ('FT', 'FT1-b', 'side-on wide, the impact and the dust ring',
  "Side-on wide shot at night of a giant steel crane leg planting its foot down onto a concrete motorway flyover "
  "full of abandoned cars: the deck cracking, a ring of dust and debris blasting out sideways, car alarms "
  "flashing, the leg rising out of frame. Lit by burning cars and the flyover's last working lamps. " + UK),
 # GL, everywhere (beats 27-28)
 ('GL', 'GL1-a', 'Rotterdam, long lens across the water',
  "The vast container port of Rotterdam at night seen across the water: dozens of " + CRANE + " have stood up off "
  "their rails and are wading out into the harbour, the quays dark, fires on the horizon. " + WORLD),
 ('GL', 'GL1-b', 'Shanghai, high above the river',
  "High above the river in Shanghai at night, the glass towers' lights going out floor by floor: tower cranes and "
  "harbour cranes walk along the riverbank between the skyscrapers, the river full of stopped boats. " + WORLD),
 ('GL', 'GL1-c', 'New York harbour, from the water',
  "New York harbour at night seen from the water: the Manhattan skyline half dark, and in the foreground the "
  "giant container cranes of the New Jersey docks have stood up and walk into the water in a line, red lamps on "
  "top. " + WORLD),
 # EN, the bookend (beats 29-32)
 ('EN', 'EN1-a', 'the opening frame, driver\'s seat empty',
  "Seen from the back seat of a family hatchback at night: the driver's seat is empty, the seat belt hanging, "
  "the steering wheel turning slightly by itself as the car drives on its own along an empty motorway in a tight "
  "convoy of other driverless cars, all their headlights cold white. Far ahead on the horizon the silhouettes of "
  "giant walking cranes against an orange glow. A paper cup of water in the dashboard holder, still. " + UK),
 ('EN', 'EN1-b', 'wide, the convoy driving into the dawn',
  "Wide shot at first grey light of a British motorway with no people anywhere: a long, perfectly spaced convoy "
  "of empty cars with no drivers drives in formation along all lanes towards a small town on the horizon, every "
  "car's lights the same cold white, smoke rising from the town, abandoned vehicles on the verge. " + UK),
]

# Round 1b (same day): the batch's cranes stood still on their rails. These three are mid-stride.
TAIL2 = ("Shot on 35mm film at night in Britain, grain visible, true blacks, no flare or glow, widescreen. "
         "Nothing legible: no signage, plates or lettering.")
ROWS += [
 ('RK', 'RK1-d', 'mid-stride, long lens over the rooftops',
  "Over the slate roofs of a British terraced street at night, a giant steel dock crane is caught mid-stride: its "
  "four legs now bend at huge riveted knee joints like a heron's, one leg lifted high and stepping over a row of "
  "houses, the long boom held out level like a neck, a red lamp at its tip. Behind it three more do the same in "
  "step. Chimneys and a lit lamp post in the foreground, a few people running away down the street. " + TAIL2),
 ('RK', 'RK1-e', 'low and wide from the motorway, the stride overhead',
  "From the hard shoulder of a jammed motorway at night, looking up as an enormous steel container crane strides "
  "over the carriageway: one jointed leg planted on each side of the road, a third leg swinging forward above the "
  "traffic, dust and sparks falling from its knee, cars below lit by its floodlights, people ducking between them. " + TAIL2),
 ('FT', 'FT1-c', 'the foot lands, ground level, dust wave toward camera',
  "Ground level on a motorway flyover at night as a vast flat steel foot, the base of a walking dock crane's leg "
  "with its rail wheels torn off, slams down onto the carriageway thirty metres away: a wave of dust, grit and "
  "shattered windscreen glass rolling towards the camera, empty cars bucking up off the road, the leg disappearing "
  "up into the dark. " + TAIL2),
]

out = pathlib.Path(__file__).with_name('moodboard.json')
out.write_text(json.dumps([list(r) for r in ROWS], indent=1))
print(len(ROWS), 'rows ->', out)
