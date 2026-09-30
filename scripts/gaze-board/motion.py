#!/usr/bin/env python3
"""The 46 motion prompts for the gaze, designed 2026-09-19 under the shot-craft skill.

🔴 REVISION 2, after Kai watched the first three and stopped the run:
    "in the stock market you've made everybody leap up and down, in the meeting they're
     all drinking champagne, and in the weather one there's a tornado out of nowhere.
     The idea here is to possibly be a bit more subtle."

He is right, and it is the mistake `stills.md` and `motion-and-cutting.md` both warn about:
a move (or a motion beat) only ever REVEALS drama that is already staged in the frame.
Used to manufacture drama it reads as exactly that. Revision 1 wrote each clip as a little
staged event - a toast completing, a floor erupting, a dust devil arriving - which is the
machine DIRECTING. This scene is the machine WATCHING.

The rules this revision runs on:
  1. CONTINUATION, NOT INVENTION. Only what the still already implies is allowed to move.
     Dry ground gets wind and haze, never a tornado. Nobody drinks unless already mid-drink.
  2. AMBIENT OVER EVENT. Air, light, cloth, steam, traffic, breath, weight shifting. No new
     objects entering frame, nothing toppling, no lights shutting off in banks.
  3. ONE SMALL HUMAN TRUTH per shot - a glance, a blink, someone looking away - not a beat.
  4. The eight seconds are a HELD BREATH, not a scene. Several prompts say so outright
     ("nothing dramatic happens"), which measurably calms Veo down.
  5. Camera discipline unchanged from revision 1, and the moves are gentler: the camera is
     LOCKED wherever there is a repeating near-field lattice (tower rows, ranks of seats,
     server aisles, the lamp field) because a camera travelling across one makes Veo redraw
     it. 11 of 46 move at all, and none of them hurry.
"""
STILLS = '/mnt/d/badcode-videos/gitpush-origin-master/clips/the-gaze/stills'
OUT = '/mnt/d/badcode-videos/gitpush-origin-master/clips/the-gaze/video'
FOLDERS = {'01':'01-grid','02':'02-dive','03':'03-soil-vast','04':'04-soil-farmer','05':'05-happiness-bus','06':'06-happiness-city','07':'07-water-reservoir','08':'08-water-queue','09':'09-birth-estate','10':'10-birth-kitchen','11':'11-dam-wall','12':'12-b1-exodus','13':'13-b2-towers','14':'14-b3-downs','15':'15-prices','16':'16-doorway','17':'17-school-run','18':'18-high-street','19':'19-playground','20':'20-ribbon','21':'21-summit','22':'22-sprinklers','23':'23-good-news','24':'24-photo-op','25':'25-build','26':'26-mansions','27':'27-power','28':'28-inside','29':'29-scar','30':'30-campus'}
TALL = {'T1-b':'01-grid-tall/00-b.jpg'}

# Stills that do not follow the `<folder>/<NN>-<a|b>.jpg` pairing, because they were shot later
# as one-offs rather than as an a/b pair. Kai picked these from a contact sheet on 2026-09-21.
EXTRA = {
    'X-launch': '31-launch/01.jpg',
    'X-harbour': '33-harbour/01.jpg',
    'X-kerb': '34-kerb/01.jpg',
}

LOCK = "The camera is locked off on a tripod and does not move at all. "

SHOTS = [
# --- BEAT 1 - THE EXECUTIVES ---------------------------------------------
('23-f1-b', "The camera does not move. A trading floor at the end of a good day. The men keep talking and shaking hands, unhurried; one turns his head to look at the boards, another leans back in his chair. On the wall of screens the figures refresh and the green lines tick upward a notch. Someone crosses the far side of the room. Nothing dramatic happens - the room is simply pleased with itself. Documentary, available light, fine film grain."),
('23-f2-b', "Almost no camera movement, the faintest drift inward. A boardroom at the end of a meeting. They hold their raised glasses and lower them slowly; one says something and the others half-smile; a man at the near end shifts in his chair and looks down at the table. On the wall screen the line holds where it is. Outside the window, cloud moves slowly behind the city towers. Quiet, unhurried, observed."),
('21-f5-b', "The camera does not move. Men in suits stand on dry ground behind tall glass, talking. Low wind moves dust along the ground and stirs the dead scrub. One gestures out across the land; another shifts his weight and looks away; a third drinks from a cup. Their reflections move faintly on the glass. Heat haze sits low over the ground. Nothing else happens."),
('21-f1-b', "The camera hovers, almost perfectly still. Ranked private jets on a desert apron in late afternoon. Heat haze shimmers off the tarmac. One small ground vehicle moves slowly along a taxiway. The long shadows of the tailfins lie across the concrete. Dust drifts off the desert beyond. Flat, observational aerial, no incident."),
('21-f3-b', "An almost imperceptible drift. A line of black cars waiting at a glass terminal. Cold exhaust drifts from the tailpipes. One man standing by a door shifts his weight; another looks off down the line. A figure walks unhurriedly toward the entrance. Reflections of slow cloud cross the glass above. Nothing dramatic happens."),
('22-f1-a', "A very slow lateral drift to the right. Sprinklers turn steadily on the green, throwing low arcs of water that drift as fine mist. The grass moves in the wind. Beyond it the dried lake bed lies still, faint dust lifting off it in the heat haze. Hard bright daylight. Calm, patient, unhurried."),
('21-f2-b', "The camera does not move. A packed conference hall during applause. The audience claps steadily, a few heads turning, one or two people leaning to speak to a neighbour, someone settling back into their seat. A figure stands at the distant lectern. Dust turns slowly in the beam of the follow-spot. Steady, ordinary, observed."),
('20-f1-a', "A very slow push in. The group stand together at the ribbon holding the scissors, holding the pose for the cameras, shifting slightly; one smiles and glances sideways. The photographers in the foreground adjust position and keep shooting. Dust blows low across the bare ground between camera and subject. Bright overcast light."),
('20-f3-b', "A slow push in along the blades. The scissors close on the red ribbon and it parts; the cut ends fall away and drift down out of frame. The gloved hand holds steady. Shallow depth of field, the corrugated wall behind soft. Unhurried, close, observed."),
('20-f5-b', "The camera does not move. Nobody is here. The discarded red ribbon lifts slightly in the wind and shifts on the carpet. The empty white chairs stand still; one rocks a little. Dust drifts low across the ground. The light dims slowly as cloud crosses the sun. Nothing else happens."),
('21-f4-b', "The camera does not move. The hall after everyone has gone. Loose paper and lanyards stir very slightly on the seats in the draught from the air conditioning. The distant stage stays lit and empty. The air is still. Nothing happens. Quiet, cold, observed."),
# --- BEAT 2 - THE BUILD --------------------------------------------------
('25-f4-b', "The camera holds still, high above the road. The convoy of lorries creeps forward slowly along the dirt haul road. Dust drifts up from their wheels and hangs in the air. Far away across the site the tower cranes turn slowly. Heat haze over the ground. Patient, unhurried, observational."),
('25-f3-a', "A very slow rise. The night construction site works under its floodlights - vehicles moving slowly through the mud, small figures crossing between them, a crane boom turning. Dust and exhaust drift through the beams. The floodlight halo glows steadily. Observed from a distance, unhurried."),
('25-f1-a', "The camera holds nearly still. Dawn over the site. The tower cranes turn slowly against the sky. Steam drifts from the plant, dust lifts gently off the haul roads, a truck crawls between the concrete cores. Low mist moves across the far edge of the site. The light warms slowly."),
('25-f2-a', "The camera is planted at the base and does not move, looking straight up the gap between the two concrete towers. Cloud drifts across the strip of sky above. Dust sifts down through the shafts of light. At the bottom the workers in hi-vis move about, small. Still, vertical, oppressive."),
('27-f1-b', "The camera does not move. A substation at dusk. Steam drifts from the vents, the cables sway very slightly in the wind, the lights in the control building glow steadily and one or two more come on. The sky deepens slowly behind the pylons. Nothing dramatic happens."),
('27-f2-a', "A very slow lateral drift. Four cooling towers release steady columns of steam that billow and lean in the wind. Vapour drifts across the plant below. The dawn light shifts slowly. Birds cross in the distance. Calm, enormous, unhurried."),
('27-f4-b', "The camera does not move. The turbine hall. The machines turn steadily with a low even vibration. Steam drifts from a joint along the row. Shafts of hard light come down through the high windows and dust turns slowly in them. Nobody is here. Steady, mechanical, observed."),
('28-f3-a', "The camera stands on the gantry and does not move. The server hall hums. Status lights flicker gently across the racks on both sides. Cold vapour drifts low along the floor. The blue light holds steady. Nobody is here. Still, cold, patient."),
('28-f4-b', "Extreme close on the control board, the camera absolutely static. The field of small red and green lamps flickers and shifts constantly in fine, complex patterns. Faint reflections move across the glass cover. Shallow depth of field, the far end of the board soft. Steady, intricate, alive."),
('T1-b', "The camera does not move. Sunrise between the enormous concrete towers. Low mist drifts over the small town below. Faint traffic moves along the road. A thin vapour plume from one tower bends slowly in the wind. The light warms as the sun lifts. Calm, vast, observed."),
# --- BEAT 3 - THE WEATHER AND THE SOIL -----------------------------------
('04-f3-a', "The camera does not move. Extreme close on the farmer's face. Dust drifts past him in the wind. He blinks slowly against it and breathes, the scarf over his mouth moving faintly. His eyes shift a little. Shallow depth of field, warm low sun. Nothing else happens."),
('02-f1-b', "A slow steady drift, the camera easing sideways and very gradually downward. The dust plume over the sea moves and spreads slowly. Cloud systems drift and stretch. The curve of the atmosphere holds. Vast, silent, unhurried."),
('02-f4-b', "A steady forward glide, the camera moving smoothly toward and over the cloud deck. Clouds pass beneath. Below, the wall of dust moves slowly across the farmland. Smooth, continuous, calm."),
('02-f3-a', "A slow steady forward drift through the dust. Particles drift past the lens. The pale disc of the sun holds, softening and brightening as the murk thickens and thins. Layers of haze pass through. Continuous, calm, enveloping."),
('04-f1-a', "The camera sits low and does not move. Dry topsoil lifts off the ploughed ground in thin ribbons and drifts away on the wind. Dust streams low across the field. The sun sits dim behind the haze. Steady wind, nothing sudden."),
# --- BEAT 4 - HOW IT IS GOING --------------------------------------------
('05-f2-b', "The camera does not move. The night bus is moving; the interior rocks gently and the street lights slide past the windows, moving softly across her face. She rests her head against the glass and breathes; her eyes close, then open. Rain runs down the window. The phone in her hand glows faintly."),
('05-f3-b', "The camera does not move. Seen from the wet street through the rain-streaked bus window. Drops run down the glass. Inside, he keeps looking at his phone, the screen lighting his face; he shifts slightly. Reflections of the street move across the glass. Steady rain."),
('05-f4-a', "The camera does not move. The bus is moving and everyone sways gently together with it. The nurse sleeps, her head moving with the motion. The man in hi-vis looks at his phone. Lights pass across the windows on both sides. Ordinary, tired, quiet."),
('07-f1-b', "The camera does not move. He leans on the walkway wall and smokes; the smoke drifts and curls away in the wind. He breathes out and shifts his weight slightly. Behind him the lit city sits steady under a faint haze, one or two windows changing. Calm, still, observed."),
('10-f2-a', "The camera does not move. The bare bulb sways very slightly and its light moves faintly on the damp ceiling and on them. She breathes, her hands against her face; he stays as he is, then shifts a little. The laptop glow holds steady on the table. The papers lie still. Nobody speaks."),
('10-f4-b', "The camera does not move. She sits on the edge of the bare mattress, breathing, and shifts her weight a little. She looks toward the window. Outside, faint light from the street moves slowly across the wall. The thin curtain stirs. Quiet, still."),
('15-f1-b', "The camera does not move. She holds the card to the self-checkout terminal and waits, watching the screen. Her expression settles. The man behind her shifts his weight and looks away. The strip lights hum steadily overhead. Other shoppers move slowly in the aisle behind. Ordinary, unhurried."),
('15-f4-b', "Extreme close, the camera static. The checkout belt moves slowly. A hand rests on the wrapped item, then draws it back a little. Another hand reaches in at the far end. Fluorescent light, shallow depth of field, no faces. Small, ordinary, tense."),
('16-f1-a', "The camera does not move. Shoppers walk past along the pavement, unhurried, not looking down. He pulls the blanket a little closer and lowers his head. The light is flat and grey. An ordinary street on an ordinary afternoon."),
('16-f3-b', "The camera does not move. He looks up toward the camera and holds it, then looks away. His breath shows faintly in the cold. Behind him, reflections move slowly across the lit shop window. He shifts his weight. Nothing else happens."),
('16-f5-a', "The camera does not move. Rain falls steadily on the wet pavement. The empty sleeping bag's fabric stirs slightly in the wind and the soaked cardboard darkens. Water runs along the gutter. The lit display behind the glass does not change. Nobody comes."),
# Swapped 2026-09-21 (was 17-f1-b / 17-f5-b): Flow REFUSES TO UPLOAD both of those stills,
# and five of the ten in this folder, because children are close and identifiable in them. It
# is a decision about the picture, so no prompt rewrite or retry reaches it. Kai picked these
# two replacements from the five Flow accepts; in both, the children are distant or reflected,
# which is also the better shot - the cost of the scene reads harder when they are small.
('17-f2-b', "The camera does not move. Rain beads and runs slowly down the mud-caked flank of the four-by-four filling the frame. Far behind it the children finish crossing and go out of shot, and the crossing warden lowers the sign, shifts her weight and steps back to the kerb. Water moves along the gutter. The vehicle does not move. Grey, wet, ordinary."),
('17-f4-b', "The camera does not move. The reflections of the children slide slowly along the curved black panel of the car and stretch as they pass, going out of frame one by one. A drop of rain runs down the paint and stops. The wing mirror holds still. Nothing else moves - they are only ever a reflection on it."),
('18-f1-a', "The camera does not move. Rain falls on the empty high street. A figure under an umbrella walks slowly away down the pavement. Water runs off the shutters. Reflections shift in the wet road. Nothing else happens."),
('18-f2-a', "The camera does not move. Three figures walk slowly along the boarded terrace in different directions. The single lit doorway stays lit. Rain falls steadily and runs off the boarded window frames. Grey light, an ordinary afternoon."),
('19-f1-a', "The camera does not move. The empty swings move slightly in the wind, each out of time with the others, the chains turning. The grass at the edges of the tarmac lays over in gusts. Cloud shadow moves slowly across the ground. No child appears."),
('19-f2-a', "The camera does not move. The rusted chain hooked up out of reach swings very slightly in the drizzle, water beading on it. The focus eases slowly through to the tower blocks behind until they resolve, and the chain softens. Drizzle drifts. Quiet, grey."),
('19-f3-a', "The camera does not move. The hazard tape flutters across the front of the fenced-off playground. The long grass moves in slow waves. The abandoned swings turn very slightly behind the fence. Cloud shadow crosses the houses behind. Grey daylight."),
('19-f4-a', "The camera does not move. Rain falls into the puddle beneath the rusted roundabout, rings spreading and overlapping. Drips run off the handrail. The roundabout turns very slowly and comes to rest. The grass behind moves in the wind. Nobody is here."),
('11-f4-a', "A slow steady rise and tilt upward, revealing the tide lines on the bank and the scale of the drained basin beyond. The last shallow water in the channel moves slightly. The dried mud lies still. Dust drifts faintly across the light. Calm, wide, final."),

# --- THE SPOILS - added 2026-09-21 -----------------------------------------
# 🔴 THESE THREE BELONG AFTER SHOT 2 IN THE CUT, not at the end. They are appended here only
# because this list's position IS the output filename (`NN-key.mp4`): inserting them in their
# true place would renumber all 46 clips, and Premiere holds those clips BY PATH, so a rename
# takes the whole built sequence offline. Premiere's `gpom-the-gaze-cut-46` carries the real
# order. Run them in the cut as: 01 trading floor, 02 boardroom, THESE THREE, then 03 onward.
#
# Kai's brief, 2026-09-21: "the whole point of these cuts is it's like everything's working
# well." So unlike every other shot in this scene, these carry NO visible cost in frame - the
# twenty shots of the montage are the cost, and Beat 1 is the case they answer. Descending
# scale on purpose: sky, then sea, then street.
('X-launch', "The camera does not move. The rocket continues to climb, slowly and steadily, the column of exhaust below it thickening and drifting sideways in the high air. Its reflection rises in the still water and breaks very slightly as the surface moves. The pale grass in the foreground stirs in a light wind. The sky warms. Serene, wide, unhurried - nothing dramatic happens."),
('X-harbour', "The camera does not move. The crew member keeps working, unhurried, polishing the same patch of brightwork and shifting his weight. The water moves gently against the quay and against the hulls, and the reflected light ripples slowly along the white side above him. Water runs from the hose across the wet stone. The row of yachts beyond stays still. Early, bright, quiet."),
('X-kerb', "The camera does not move. Fine rain falls through the light. Water beads and runs slowly down the polished flank of the car, and the gold of the shop windows slides very slightly along the paint as the drops move. Far down the empty street, headlights cross once and are gone. The lit windows do not change. Wet, still, expensive."),
]

def source(key):
    if key in TALL:
        return f'{STILLS}/{TALL[key]}'
    if key in EXTRA:
        return f'{STILLS}/{EXTRA[key]}'
    n, f, c = key.split('-')
    return f'{STILLS}/{FOLDERS[n]}/{int(f[1:])-1:02d}-{c}.jpg'

if __name__ == '__main__':
    import json, sys
    rows = [{'i': i+1, 'key': k, 'src': source(k),
             'out': f'{OUT}/{i+1:02d}-{k}.mp4', 'motion': m}
            for i, (k, m) in enumerate(SHOTS)]
    if len(sys.argv) > 1 and sys.argv[1] == 'json':
        print(json.dumps(rows, indent=1))
    else:
        for r in rows:
            print(f"{r['i']:02d} {r['key']:8s} {'MOVE' if not r['motion'].startswith('The camera is locked') else 'lock'}  {r['motion'][:70]}")
