"""Video round 1 (2026-10-28): Omni Flash motion prompts for the 33 picked stills. House rules: camera locked (Premiere
moves it), one main motion + one ambient, shutter named, ~60 words, saturated colours, sound effects only, fire burns
steady (the K3a cut failed the flash check on flickering flames), no 'flash'/'burst' words (silent block in K3a s14),
nothing rendered in long flight (paper drifts, never falls far)."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
LOCK = "The camera does not move."
TAIL = "Shot at 24fps with a 180-degree shutter, so fast movement smears with natural motion blur. No dialogue. The camera does not move."
M = {
 1: ("The black sedan and the police car roar round the corner towards the camera, their red, green and blue colour trails smearing behind them; rain spits on the wet cobbles and the red lamp over the doorway glows steady.", "Engines roaring, tyres hissing on wet cobbles, a police bell ringing."),
 2: ("The baker leans his whole weight into the dough and kneads it slowly, the green banknote pattern stretching with it; flour drifts through the orange oven light.", "Dough slapping on wood, the oven's low roar."),
 3: ("The black and white rings ripple slowly outward across the frame; the moth on the palm opens and closes its wings once; the fingers curl slightly round the coins.", "A low hum, coins clinking softly."),
 4: ("Far below, the small figure climbs one step up the spiral stairwell; the bare bulbs on each landing glow steady; the landlord's open palm stays still.", "Slow footsteps echoing up a stairwell."),
 5: ("The man in the fedora murmurs into the slot, his lips barely moving; the eyes in the slot narrow; smoke curls up from his cigarette through the cyan slats of light.", "A muffled murmur, distant jazz behind the door."),
 6: ("Her breath rolls out in slow white-hot clouds through the blue and violet attic; the small candle flame burns steady and yellow between her hands.", "Wind moaning, ice creaking in the beams."),
 7: ("Envelopes drift down onto the iron grate and slide between the bars into the dark; up on the amber balcony the man keeps flinging them; the crowd's hands reach.", "Crowd roaring, paper fluttering, rain dripping into the drain."),
 8: ("Everyone at the table stays frozen; only the cigar smoke curls up through the green lamplight and the lamp sways very slightly on its chain.", "A clock ticking in silence."),
 9: ("The old man strikes the cue ball and it rolls straight towards the camera across the green felt; the coloured oil blobs drift slowly over the room; the band plays.", "A sharp cue click, balls rolling, a jazz band."),
10: ("The men in pinstripes walk towards the camera through the vault door carrying empty sacks; the clerk's pen hovers; daylight slats lie still across the marble.", "Footsteps on marble, a pen scratching."),
11: ("The blowtorch roars blue-white and the steel door sags and drips molten orange onto the marble; sparks skitter across the floor; the guard stands still.", "A roaring blowtorch, hissing metal, sparks crackling."),
12: ("The whole gold-and-black kaleidoscope turns slowly clockwise round its centre while banknotes drift and the man at the centre dances with his arms out.", "A brass jazz band, presses thumping, a crowd cheering."),
13: ("The man in the bowler tips a shovel of coal into the firebox and the glow brightens to a steady orange; banknotes slide out of the press; smoke drifts through the gold and magenta.", "Coal rattling, the press thumping, fire roaring."),
14: ("The white smoke cloud billows and rolls across the bandstand while the man holds his arms up; behind it the getaway car pulls away from the bank steps trailing red, green and blue smears.", "A gasp from the crowd, a car engine revving away."),
15: ("The two men in red and blue scarves shove each other, smeared into red, green and blue trails; the man with the sack strolls calmly towards the camera, perfectly sharp; the plain banners wave.", "Shouting crowd, a police bell far off, rain."),
16: ("The two mirror-image men shout nose to nose, their jaws working; rain streaks down through the gas lamp's light; the seam down the middle stays perfectly still.", "Two men shouting, rain hammering."),
17: ("The three dance arm in arm, laughing, swaying from side to side; the amber, magenta and blue oil blobs swim slowly over them; glasses rise behind.", "A hot jazz band, laughter, glasses clinking."),
18: ("The man at the microphone reads and grins, his head bobbing; the red lamp burns steady; in the doorway the man counts banknotes; the printing dots at the edges pulse gently.", "A warm radio hum, paper rustling, notes riffling."),
19: ("The couple lean closer to the radio; the black and white rings ripple slowly out from its speaker across the kitchen; the amber dial glows steady; snow falls past the window.", "A crackling radio voice too faint to understand, snow ticking on glass."),
20: ("The fat man heaves the barrow up the plank, straining; the stacks of money on it wobble; behind him the others wheel their barrows on.", "Wheelbarrow wheels creaking on wood, grunting."),
21: ("The mountain of money slides slowly downhill like warm honey and the walls drip; the banknote on his chest lifts gently with each slow breath.", "Slow dripping, a contented sigh."),
22: ("The two officers lean in, sweeping their torch beams across the oven; behind them the men in bakers' hats stand perfectly still and smile innocently.", "Torches clicking, an oven door creaking, a nervous cough."),
23: ("The two officers walk away down the wet street with loaves under their arms, tipping their caps; the trapdoor's green glow pulses gently; the burning images inside them shimmer.", "Footsteps fading on wet cobbles, a distant whistle."),
24: ("The stoker heaves another shovel of banknotes into the furnace and the white-hot glow swells steadily; the purple and blue walls stay cold.", "A roaring furnace, a shovel scraping."),
25: ("The gold-and-black kaleidoscope turns slowly round its centre while hands count stacks and snap rubber bands round them.", "Rubber bands snapping, notes riffling, a card deal."),
26: ("The baker tips the last coins from his envelope onto the counter; the shopkeeper's hand slides them away; the pink and yellow paint drips run slowly down.", "Coins clattering on wood, a till drawer ringing."),
27: ("The man bails frantically, throwing banknotes overboard with each scoop; the boat sinks a little lower; the coloured reflections tremble on the black water.", "Water sloshing, a bucket scooping, distant city traffic."),
28: ("Left: the men by the furnace wipe sweat as the white-orange fire roars. Right: the tiny flame by the old woman gutters lower and shivers.", "A roaring furnace on the left, a thin icy wind on the right."),
29: ("Snow falls steadily past the open building; the lamps on each floor glow steady, warm gold at the bottom and cold blue at the top.", "Muffled jazz from deep below, wind and snow."),
30: ("The whole queue shuffles forward one step through the snow; breath steams; the pink and yellow paint drips run slowly down.", "Feet crunching on snow, coughing, wind."),
31: ("The crowd pours down the narrow stairs towards the camera; the man at the front swings his lantern; the red lamp over the door glows steady.", "Many footsteps thundering down stone stairs."),
32: ("The cake trembles on the silver tray in the mayor's shaking hands; the black and white rings ripple slowly outward; the crowd's lanterns sway.", "A held breath, the furnace roaring, a nervous laugh."),
33: ("Banknotes blow slowly along the empty wet cobbles past the abandoned car; the red moon hangs still above the rooftops.", "Wind, paper skittering, total silence beneath."),
}
ao = json.loads((HERE / 'animation-options.json').read_text())
for f in ao['frames']:
    mot, snd = M[f['n']]
    o = f['options'][0]
    o['idea'] = mot
    o['veo_prompt'] = f"{LOCK} {mot} {TAIL} Sound: {snd}"
(HERE / 'animation-options.json').write_text(json.dumps(ao, indent=1))
(HERE / 'video-jobs.json').write_text(json.dumps({'option': 'a', 'duration': 8, 'skip': [], 'extra': []}, indent=1))
print(max(len(f['options'][0]['veo_prompt'].split()) for f in ao['frames']), 'words max')
