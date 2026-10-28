"""Round 2 (2026-10-28): psychedelic overlays on a realistic base, 12 families + one transition pair.
Rule from omni-flash.md: never write psychedelic / surreal / trippy / neon / glowing / cinematic; name the physical thing."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
LEAD = "A realistic 1920s photograph on grainy colour film: real people with real skin, pores and stubble, in real places."
MAYOR = "a tall skinny man in a bowler hat with a heavy gold mayoral chain round his neck, a long narrow face, hollow cheeks and a pencil-thin grey moustache"
END = "Plain margins with no writing. Thanks."
P = [
 ('P1', 'Banknote engraving', 's5',
  "Over everything lies the fine engraved line work of a banknote: thousands of hair-thin curving parallel lines and rosettes printed in money-green and copper ink, wrapping round the contours of the face, the hat brim, the bricks and the cigarette smoke like a contour map, so the real scene looks printed on a dollar bill. Camera close at chest height, slightly below: a heavy-set gangster in a chalk-stripe suit and grey fedora, with a broad pockmarked face and a flattened boxer's nose, leans his mouth to the slot of a plain steel door, his face large and right of centre; through the slot, two wary eyes. Light: one bare bulb above the door; most of the frame in deep shadow."),
 ('P2', 'Brass kaleidoscope', 's12',
  f"Seen straight down from the ceiling, the scene is folded into six mirrored segments round a centre point, as if looked at through a brass kaleidoscope, the mirror seams crisp straight lines, each segment the same real photograph repeated so the whole frame becomes a gold-and-black star. The scene: a hidden basement print room where gangsters in pinstripe suits shovel coal into printing presses and sheets of banknotes fly up, and at the exact centre {MAYOR} dances with his arms flung out. Light: hanging brass lamps and the red-hot fireboxes; deep shadow between them."),
 ('P3', 'Liquid light show', 's17',
  f"Projected across the whole scene, coloured oil and water swim like a 1960s liquid light show: huge soft-edged blobs of amber, magenta and cobalt blue drift over the faces, suits and brick walls, merging and splitting, with thin dark rims where oil meets water. Underneath, the scene stays real: in a smoky basement dance hall {MAYOR} dances arm in arm with a ginger man with mutton-chop whiskers and a red carnation, and a woman with a black bob in a plain blue cardigan with a blue carnation, all three laughing. Camera at hip height, between the legs of a band in pinstripe suits in the foreground. Light: one white spotlight from above."),
 ('P4', 'Heat camera', 's24',
  "Shot through a heat camera: every surface is coloured by its temperature. The furnace and the stoker's arms blaze white and yellow, warm bodies run orange and red, the walls and the pipe climbing them fade from magenta to deep cold blue, and the top of the frame is icy violet-black. Every shape and detail is still a real photograph. A stoker in a vest, with a thick neck, a shaved head and a broken nose, shovels banknotes into the roaring mouth of a basement furnace; its heating pipe climbs the brick wall and stops dead at the ceiling. Camera low beside the furnace door, the shovel blade in the foreground."),
 ('P5', 'Infinite picture', 's13',
  f"The picture contains itself: the open furnace door at the centre shows, inside its fire, the same basement room again, smaller, with its own open furnace door, which holds the room again, smaller and smaller, spiralling inwards forever. {MAYOR[0].upper() + MAYOR[1:]} stands beside the furnace holding a coal shovel, and a smaller copy of him stands at every level of the spiral. A realistic 1920s basement: riveted pipes, brass gauges, a heap of coal. Light: only the fire; the rest in deep shadow."),
 ('P6', 'Silhouette windows', 's15',
  f"Two crowds face each other across a wet cobbled street at night, red scarves on the left and blue scarves on the right, shown as black silhouettes against a burning barrel between them. Inside every silhouette, as a double exposure, is the same hidden scene: a basement where a printing press throws banknotes into the air and {MAYOR} dances, lit hot amber and red. Around the silhouettes the street stays real: rain on the cobbles, the barrel's flames smeared in vertical streaks on the wet stones, a gas lamp. Camera low behind the barrel."),
 ('P7', 'Colour trails', 's15b',
  "Every moving thing leaves a trail of three or four afterimages behind it, each copy split into pure red, green and blue and fading, like a long exposure lit by repeated coloured flashes; everything standing still stays sharp and true. On a wet cobbled street at night under a gas lamp, a man in a red scarf and a man in a blue scarf shove each other, their swinging arms and flying hats smeared into coloured trails, while a calm gangster in a chalk-stripe suit with a scarred lip strolls past them with a canvas sack over his shoulder, perfectly sharp, with no trail at all. Camera low at the kerb."),
 ('P8', 'Melting world', 's21',
  f"The solid world is turning liquid: the mountain of rubber-banded money runs slowly downhill like warm honey, the brick vault walls sag and drip like candle wax, and the gold chain drips gold drops. Everything else is a realistic photograph. {MAYOR[0].upper() + MAYOR[1:]} lies back on top of the money, eyes half closed and glazed, a banknote resting on his chest. Camera low at the foot of the pile, dripping notes in the foreground. Light: one hanging brass lamp above, warm amber on the money; the vault behind falls to deep green shadow."),
 ('P9', 'Spray-tagged photo', 's30',
  "A long bread queue in the snow on a 1920s street at dawn: ordinary people of all ages, men and women, Black, white and South Asian, in worn coats, each holding money, a coin, a fistful, a bag, and at the back a wheelbarrow of notes. Sprayed over the photograph with aerosol paint: fluorescent pink and acid yellow overspray clouds, hard-edged stencilled halftone shapes, and long paint drips running down across the coats and the snow, as if someone tagged the photo on a wall. Faces stay real. Camera at waist height from the front of the queue, looking back along it. Light: grey dawn, and one lit shop window full of loaves under a plain blank sign."),
 ('P10', 'Op-art rings', 's6',
  "Concentric black and white rings ripple outward from her eye across the whole frame, bending the real picture like ripples on a pond, with one thin spiral of red running through them. Underneath, a realistic close-up: an old woman in a frozen attic, frost on her eyelashes and on the wool shawl over her head, breath steaming, a deeply lined face with a mole on her cheek, her hands cupped round one candle flame. Camera close, at the height of the candle. Light: the candle only."),
 ('P11', 'Newsprint dots', 's18',
  f"The photograph is breaking up into the coarse printing dots of a 1920s newspaper: at the edges of the frame the scene is nothing but huge cyan, magenta, yellow and black dots, shrinking towards the centre, where it becomes a fully realistic photograph. {MAYOR[0].upper() + MAYOR[1:]} grins into a big chrome radio microphone, reading from a script, a lit red lamp on the wall behind him. Camera low across the desk, the microphone large in the foreground. Light: a warm desk lamp under his face; the studio behind in deep shadow."),
 ('P12', 'Cut-crystal prism', 's8',
  f"Seen through a cut-crystal whiskey tumbler in the foreground, the middle of the frame breaks into a dozen faceted fragments, each a slightly shifted copy of the room edged with thin rainbow fringes; outside the glass the frame is a plain realistic photograph. A smoky back room: at a long table of whole hams and champagne, gangsters in pinstripes and {MAYOR} freeze mid-bite, forks in the air, all turned to the open door, where a heavy-set Black baker in a floury vest stands holding one small loaf. Light: one low brass lamp with a green glass shade over the table; the doorway cold blue."),
]
TX = [
 ('TX-a', 'Transition A: into the fire', 'tx',
  "Extremely close inside the mouth of a 1920s basement furnace: glowing coal and half-burnt banknotes curling and blackening, the flames rising in one tall tongue of fire in the exact centre of the frame, the black iron rim of the furnace door at the very edges. Light: only the fire, white-yellow at its heart, deep orange at the edges, black beyond."),
 ('TX-b', 'Transition B: out at the protest', 'tx',
  "A tall tongue of fire in the exact centre of the frame rises from a burning oil drum at a 1920s street protest at night; the flames fill the middle of the picture, white-yellow at the heart, and around them, softer, people in red scarves and blue scarves hold up blank placards, faces turned to the fire, and the wet cobbles carry the firelight in long streaks. Camera close to the drum at chest height. Light: only the fire and one distant gas lamp."),
]
rows = []
for sid, look, scene, body in P:
    rows += [['psy', f'{sid}-{c}', f'{sid} {look} (scene {scene[1:]})', f'{LEAD} {body} {END}', sid] for c in 'ab']
for sid, look, key, body in TX:
    rows += [[key, f'{sid}-{c}', look, f'{LEAD} {body} {END}', 'TX'] for c in 'ab']
r1 = [r for r in json.loads((HERE / 'moodboard.json').read_text()) if r[0] in ('slot', 'press')]
(HERE / 'moodboard.json').write_text(json.dumps(rows + r1, indent=1))
for sid, look, _, body in P + TX:
    print(f'### {sid}\n{LEAD} {body} {END}\n')
