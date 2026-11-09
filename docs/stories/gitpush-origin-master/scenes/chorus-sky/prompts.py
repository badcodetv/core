"""Round 1 prompts for the chorus "the sky, then the silence" (Kai, 9 Nov). Writes moodboard.json rows.
Full (a) and sky (b) shots are generated; empty (c) shots are edits of the full shot with the people removed."""
import json, pathlib
TAIL = ("Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, "
        "naturalistic motivated lighting, no lens flares, landscape orientation. 16:9 frame from a fictional near-future film, "
        "no captions, logos, brand names, lettering or readable on-screen text; every screen and billboard shows only abstract colour.")
SKY = ("Above them the whole sky is filled with thousands of small bright white lights slowly descending through low cloud, "
       "evenly spread like a vast silent meteor storm, and far off on the horizon bright flashes light up the underside of the clouds")
PLACES = [
 ('SB', 'Tokyo, Shibuya crossing',
  "The Shibuya scramble crossing in Tokyo at night, seen from a high window: thousands of people mid-crossing in every direction on wet tarmac under towering glowing screens, umbrellas, taxis waiting at the lights.",
  "Street level in the middle of the Shibuya scramble crossing in Tokyo at night: the whole crowd has stopped dead mid-crossing and every face is turned up, lit cold white from above. ",
  "umbrellas and a dropped shopping bag lie on the wet crossing, the screens still glow over the empty junction"),
 ('TS', 'New York, Times Square',
  "Times Square in New York at dusk, seen from the red steps: packed shoulder to shoulder with people, yellow cabs nose to tail, the giant screens glowing on every building.",
  "Low angle from inside the packed crowd in Times Square at dusk: everyone has stopped and is staring straight up, cab drivers out of their doors, faces lit cold white from above. ",
  "yellow cabs left with their doors open, the giant screens still playing colour to nobody"),
 ('PC', 'London, Piccadilly Circus',
  "Piccadilly Circus in London on a drizzly night, seen from across the junction: crowds around the statue fountain, red double-decker buses and black cabs, the curved wall of screens glowing.",
  "From the steps of the statue fountain at Piccadilly Circus on a drizzly night: the crowd and the people on the top deck of a red bus have all stopped to look up, faces lit cold white from above. ",
  "a red double-decker bus stands empty with its doors open, the curved screens still glowing over the deserted junction"),
 ('ST', 'A football stadium',
  "A packed British football stadium at night under floodlights, seen from the top of the highest stand: sixty thousand fans, a match in play on the bright green pitch.",
  "Inside a packed British football stadium at night: the players have stopped on the pitch and sixty thousand fans are standing, every face turned up past the floodlights. ",
  "the floodlights still blaze over empty seats and a deserted pitch, scarves and paper cups left in the stands"),
 ('MW', 'A motorway interchange',
  "Spaghetti Junction, a huge British motorway interchange near Birmingham at dusk, seen from high above: every lane on every level jammed solid with headlights and tail-lights.",
  "On a jammed British motorway interchange at dusk: drivers have got out of their cars and stand on the carriageways between stopped traffic, all looking up. ",
  "every car left where it stopped across every level, doors open, headlights still on, nobody anywhere"),
 ('CB', 'Rio, Copacabana',
  "Copacabana beach in Rio de Janeiro at sunset, seen from above the promenade: the beach and the wave-pattern pavement packed with people, the high-rise hotels glowing behind.",
  "On the crowded Copacabana promenade in Rio at sunset: the whole beach has stood up and turned to the sky, faces lit cold white from above. ",
  "towels, parasols and flip-flops left across the empty sand and the wave-pattern pavement, the hotel windows still lit"),
]
rows = []
for code, name, full, sky, empty in PLACES:
    rows.append([code, f'{code}1-a', 'full', f'{full} {TAIL}'])
    rows.append([code, f'{code}1-b', 'the sky', f'{sky}{SKY}. {TAIL}'])
    rows.append([code, f'{code}1-c', 'empty (edit of -a)',
                 f'Using the provided image, keep exactly the same framing, camera position, buildings, light and weather, '
                 f'but remove every single person: the place is completely deserted. {empty[0].upper() + empty[1:]}. '
                 f'A thin haze of dust drifts low across the ground. Keep everything else exactly the same, preserving the original style, lighting and composition.'])
LT = [
 ('a', 'meteor storm', 'thousands of small bright white lights slowly falling through the clouds, evenly spread like a vast silent meteor storm'),
 ('b', 'red formation', 'thousands of tiny red points of light hanging motionless in a perfectly even grid across the whole sky, like a constellation that should not be there'),
 ('c', 'beams', 'dozens of thin vertical beams of pale white light coming straight down through the cloud onto districts all across the city'),
 ('d', 'dark swarm', 'a vast dark swarm blotting out the stars from horizon to horizon, its edges glinting where the city lights catch it'),
]
for k, name, what in LT:
    rows.append(['LT', f'LT1-{k}', name,
                 f'A huge city skyline at night seen from a rooftop, a few people standing on the roof in silhouette looking up: {what}. {TAIL}'])
rows.append(['FC', 'FC1-a', 'faces', f'Close on a dense crowd of strangers of every age at night, all looking straight up, their faces lit cold white from above, mouths slightly open in awe and fear, rain on their coats. {TAIL}'])
rows.append(['FC', 'FC1-b', 'faces', f'Close on an old man and a young woman in a crowd at night, side by side, strangers, both looking up, faces lit cold white from above, his hand gripping her sleeve. {TAIL}'])
pathlib.Path(__file__).with_name('moodboard.json').write_text(json.dumps(rows, indent=1, ensure_ascii=False))
print(len(rows))
