"""Writes moodboard.json for the ALT style sweep: 8 styles x 2 test frames (scene 5 slot door, scene 13 press)."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
SCENES = {
 'slot': ("Camera low on the back stairs, looking up past a dark wooden banister post in the foreground left. "
          "A heavy-set gangster in a chalk-stripe three-piece suit and grey fedora, with a broad pockmarked face, a flattened boxer's nose "
          "and a toothpick, leans close to a plain steel door at the bottom of narrow brick back stairs and murmurs into its open slot, "
          "where only two wary eyes look out. He stands right of centre, his face large in frame. 1920s: bare brick, a fire bucket, "
          "a crate of empty milk bottles, a wet stone floor."),
 'press': ("Camera low at the height of the firebox, fresh banknotes scattered on the stone floor in the foreground. In a hidden 1920s "
          "basement print room, a huge cast-iron printing press throws sheets of banknotes into the air. Beside it a tall skinny man in a "
          "bowler hat with a heavy gold mayoral chain round his neck, a long narrow face, hollow cheeks and a pencil-thin grey moustache, "
          "shovels coal into the press's red-hot firebox, grinning. Behind him an exhausted stoker in a soot-black vest sits slumped against "
          "the brick wall. Riveted pipes, brass gauges, steam."),
}
DOUBLE = {'slot': 'the rooftops of a 1920s city at night under a small red moon',
          'press': 'banknotes whirling up through flames'}
STYLES = [
 ('S1', 'Noir neon', "A realistic 1920s film still on grainy film, in hard film-noir chiaroscuro with harsh high contrast, but with the colour pushed far beyond nature."
   , "Key: a red neon tube off frame left floods everything crimson; a cold cyan light from a high window cuts across in hard slats through a venetian blind. Most of the frame is in deep shadow; the brightest values are the red edges on the faces and the slats of light. Every wet surface carries each light as a smeared vertical streak."),
 ('S2', 'Spy titles', "A realistic period photograph staged like the opening titles of a 1960s spy film: the figures are almost photographic, but the space behind them dissolves into a flat flood of saturated colour, molten gold fading into deep magenta, with drifting smoke.",
   "One hard white spotlight from above. The figures are half in silhouette, cut out sharp against the colour; only the face nearest the camera is lit in full."),
 ('S3', 'Spray paint', "Mostly realistic, like a period film still, but made with aerosol spray paint: every light has a soft overspray halo, the edges of the frame fade into fine spray mist and speckle, and thin drips run down from the brightest colours. Faces stay realistic and detailed.",
   "Key: one sodium-orange lamp overhead. The shadows are filled with electric violet spray mist. Most of the frame is dark; the brightest values are the lamp and the faces it catches."),
 ('S4', 'Technicolor dream', "A realistic still from a 1950s three-strip Technicolor film: colour impossibly saturated, everything slightly too vivid, like a memory, with a hand-painted backdrop behind real people.",
   "Key: a hard theatrical spotlight from above right. Coloured gels on the set: rich scarlet on the near surfaces, the shadows lit deep emerald."),
 ('S5', 'Stage haze', "Realistic, but lit like a stage in a dream: thick haze hangs in the air and the light cuts through it in solid visible beams.",
   "A hot magenta beam from high left and an ice-blue beam from low right cross on the main figure; dust and smoke drift in the beams; everything outside them falls away to black."),
 ('S6', 'Double exposure', "A realistic still blended as a double exposure, like a 1960s spy-film title sequence: inside the silhouette of the main figure there is a second image of {double} in burning amber and red.",
   "Outside the silhouette, deep black shadow broken by hard gold light. The face nearest the camera stays realistic and readable."),
 ('S7', 'Painted light', "Everything is realistic and photographic except the light itself, which is painted: every lamp, flame and glow is laid on in thick smeared strokes of pure colour, cadmium orange, rose and turquoise, bleeding into the air like wet paint, dreamlike. Faces stay realistic.",
   "Most of the frame is in deep shadow; the painted lights are the brightest things in it."),
 ('S8', 'Airbrush poster', "A realistic 1970s airbrushed film-poster painting: smooth photographic airbrush gradients, chrome-bright highlights on metal and jewellery, real faces.",
   "A hot pink rim light from behind outlines the figures; the darkness fades from tangerine into ultramarine; one white key from the front left."),
]
rows = []
for sid, look, style, light in STYLES:
    for key, scene in SCENES.items():
        p = f"{style.format(double=DOUBLE[key])} {scene} {light} Plain margins with no writing. Thanks."
        rows += [[key, f"{sid}-{key}-{c}", f"{sid} {look}", p, sid] for c in "ab"]
(HERE / 'moodboard.json').write_text(json.dumps(rows, indent=1))
print(len(rows))
