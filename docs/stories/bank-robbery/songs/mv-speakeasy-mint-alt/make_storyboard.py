"""ALT storyboard (2026-10-28): my pick per scene first, the runner-up second; one animation idea per frame + the
match-cut out of it (from make_rows_r3.S). Camera locked in Omni; Premiere moves the camera (hybrid method)."""
import json, importlib.util, pathlib
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location('r3', HERE / 'make_rows_r3.py'); r3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r3)
PICK = {1:['A01-a','A01-b'],2:['B02-a','B02-b'],3:['A03-b','A03-a'],4:['A04-a','A04-b'],5:['B05-a','B05-b'],6:['B06-a','B06-b'],
 7:['B07-b','B07-a'],8:['B08-a','B08-b'],9:['A09-b','A09-a'],10:['A10-a','A10-b'],11:['B11-b','B11-a'],12:['B12-a','B12-b'],
 13:['B13-b','B13-a'],14:['B14-b','B14-a'],15:['B15r-a','B15-a'],16:['A16-b','A16-a'],17:['B17-b','B17-a'],18:['B18-b','B18-a'],
 19:['A19-b','A19-a'],20:['B20-a','B20-b'],21:['B21-a','B21-b'],22:['B22-a','B22-b'],23:['B23-b','B23-a'],24:['B24-a','B24-b'],
 25:['A25-b','A25-a'],26:['B26-a','B26-b'],27:['B27-b','B27-a'],28:['B28-b','B28-a'],29:['B29-b','B29-a'],30:['A30-b','A30-a'],
 31:['A31-b','A31-a'],32:['B32-b','B32-a'],33:['A33-a','A33-b']}
MOVE = {1:"The sedan and the police car tear through the corner, their colour trails smearing; rain on the cobbles.",
 2:"The baker kneads the dough, leaning his weight in; flour drifts in the oven light.",
 3:"The coins and the moth drop into the palm; the rings ripple outward from them.",
 4:"The landlord's open palm stays still; far below, the baker climbs one step; the bulbs flicker.",
 5:"The doorman murmurs into the slot; the eyes in the slot narrow; smoke from his cigarette curls.",
 6:"Her breath steams white-hot in the heat-camera colours; the candle flame trembles.",
 7:"Envelopes flutter down onto the grate towards the lens; flashbulbs pop on the balcony.",
 8:"Frozen table; only the cigar smoke drifts and the lamp sways slightly; the baker stands still.",
 9:"The old gangster strikes the cue ball; it rolls straight at the lens; the oil blobs drift.",
 10:"The gangsters walk towards the camera with their sacks; the clerk's pen hovers.",
 11:"The blowtorch flame roars; the steel drips like wax; sparks bounce on the marble.",
 12:"The kaleidoscope turns slowly; banknotes rain; the mayor dances at the centre.",
 13:"The mayor shovels coal into the glowing firebox; notes spit out of the press; smoke drifts.",
 14:"The magnesium flash pops and the smoke billows; the getaway car pulls away with its colour trails.",
 15:"The two men shove, trailing colour; the gangster strolls past, sharp; banners wave.",
 16:"The two mirror-image men shout nose to nose; rain falls; the seam stays still.",
 17:"The three dance arm in arm, laughing; the oil blobs swim across them; glasses raised.",
 18:"The mayor grins and reads into the microphone; the dots at the edges pulse; the man in the doorway counts cash.",
 19:"The couple lean in to the radio; the rings ripple out from the speaker; the dial glows.",
 20:"The fat gangster heaves the barrow up the plank; stacks wobble.",
 21:"The money slides like honey; the walls drip; the note on his chest lifts on his breath.",
 22:"The two officers peer in with their torches, baffled; the bakers stand innocently behind.",
 23:"The officers walk away tipping their caps; the trapdoor glows green; the double exposure burns.",
 24:"The stoker shovels banknotes into the furnace; the heat colours flare as the fire roars.",
 25:"The kaleidoscope turns; hands count and snap bands; a rat nibbles.",
 26:"The baker tips his pay onto the counter; the shopkeeper's hand reaches; paint drips run.",
 27:"The mayor bails frantically; banknotes splash; the boat sinks lower; the oil blobs drift.",
 28:"Left: the gangsters sweat by the roaring furnace. Right: the last tiny flame gutters by grandma.",
 29:"Snow falls; one lamp per floor flickers; the furnace glows at the bottom.",
 30:"The queue shuffles forward one step in the snow; paint drips run.",
 31:"The crowd pours down the stairs towards the camera; the lantern swings.",
 32:"The cake trembles on the tray in the mayor's shaking hands; the rings ripple.",
 33:"Banknotes blow across the empty cobbles; the red moon above; nothing else moves."}
acts = [{'id': k, 'title': v, 'beats': []} for k, v in r3.ACTS.items()]
frames, opts = [], []
for n, act, lyric, layer, args, tx, body in r3.S:
    frames.append({'n': n, 'act': act, 'title': f'{n:02d} {lyric[:60]}', 'look': layer, 'line': lyric, 'stills': PICK[n], 'anim': n})
    opts.append({'n': n, 'job': lyric[:60], 'options': [{'id': 'a', 'label': 'locked camera, one motion',
      'idea': MOVE[n], 'lanes': 'Omni animates the world with the camera locked; Premiere moves the camera; the layer is in the still',
      'veo_prompt': f'The camera does not move. {MOVE[n]} Shot at 24fps with a 180-degree shutter. No dialogue. The camera does not move.',
      'cut': f'Transition out: {tx}', 'seconds': 8, 'risk': ''}]})
(HERE / 'storyboard.json').write_text(json.dumps({'acts': acts, 'frames': frames}, indent=1))
(HERE / 'animation-options.json').write_text(json.dumps({'sequence_notes': [
  {'rule': 'Lock the camera in Omni; Premiere moves it', 'why': 'hybrid method', 'source': 'docs/video-fx/hybrid-method.md'},
  {'rule': 'Every scene change is a match cut on a shared shape', 'why': "Jack 2026-10-28: 'constantly transitions settings in clever ways'", 'source': 'script-alt.md'},
  {'rule': 'Stills use the Flow Characters + portrait reference', 'why': 'a Character binds the face, not the costume', 'source': 'cast.md'}],
  'frames': opts}, indent=1))
print(len(frames))
