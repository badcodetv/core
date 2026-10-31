"""Round 6 sealed briefs (Jack, 2026-10-31, jack-r6.md). r1-r3 keep the lip-sync settings and change the people; n1 adds sung lines through the verses; b1 redoes the band singing; a1 is the action, including the 23 s safe and the 2:15 race. Each writer reads one brief only."""
import pathlib
HERE = pathlib.Path(__file__).parent
research = (HERE / "research-r6.md").read_text()
jack = (HERE / "jack-r6.md").read_text()
MASK = [l for l in (HERE / "make_briefs_r2.py").read_text().splitlines() if l.startswith('MASK = """')][0].split('"""')[1]

VERDICT = """# What Jack has said about clips so far, word for word

"so many barrels fall and morph and change alonside other objects, please just keep this one simple" · "the cars teleport" · "everything is so exaggerated please make it simple" · "there are cars on the river" · "it looks like a modern car" · "cars pop in and out of frame, please keep it simple" · "ai slop lets just remove this one" · on the safe: "two safes appear and morph, make it simple" · on the race: "the cars should be racing at high speed, not just going for a drive".

So: the action is already happening in the still. In the clip, one plain thing moves. Everything else keeps its shape. Nothing enters or leaves the frame. Speed comes from what streaks past, not from the car changing place in frame."""

LOOK = """# The film

A music video set in 1920s Prohibition America, in what we call colourful noir: saturated coloured light in deep shadow, glossy, lights and reflections everywhere, each shot with its own pair of colours. Cinematic and cool, real-looking, never cartoonish. It gets cut fast to the beat, so each shot plays one to four seconds."""

SINGING = """# How the singing shots get used

The song's vocal is laid over the clip afterwards and a tool redraws the mouth to it. That tool needs: one main face that fills at least a third of the frame height, facing us front-on or three-quarter, lit clearly on the mouth, clean-shaven or stubbled, with nothing in front of the mouth or chin (no hand, cigar, collar, microphone or gun), and the head moving only a little. The danger is around him: behind, beside, or reflected. He sings the line through it as though it is nothing. Other people in the frame sit further back and smaller."""

RULES = """# Rules

- Read nothing on this computer apart from this brief{extra}. You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, director, artist or real person in a prompt. No children. No readable words anywhere in the picture.
- Guns are allowed as held, period Thompsons and revolvers, pointing up or away, never at the camera or at anybody. Nobody is wounded and there's no blood. Violence is property: glass, barrels, cars, fire, sparks, money.
- Period-correct 1920s cars, clothes, hats and lights. The picture fills the frame edge to edge.
- Each shot differs from the others in angle, lens and light. Natural prose, no quality buzzwords, about 60 to 130 words for a still.
- MOTION is an image-to-video prompt, under 50 words, starting with what the camera does, then one plain thing that moves.{motion_extra}

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<still prompt>
MOTION: <motion prompt>
SECONDS: <4 or 6>
WHY: <one sentence>

Then reply with one line saying it is done.
"""
SUNG = " Then the line in exactly this form, no quotation marks: `He sings: <line>` (a crew: `The men shout together: <line>`). Say nobody else sings."

# id, setting to keep, who is in it now, the line
REDO = {
 "r1": [
  ("l01", "riding the running board of a speeding long black sedan at night, shop neon streaking along the door, a drum-fed gun held straight up", "a lean Black man of about 35, high cheekbones, a narrow clean-shaven face, dove-grey fedora", "don't be hating on the credit rating"),
  ("l02", "standing in the back of an open touring car running beside an armoured money truck, banknotes whirling, strings of bulbs above a wet street", "a stout, round-faced Italian American of about 45 with a gap in his front teeth, hat knocked back", "or have resistance to the facts I'm stating"),
  ("f1", "crouched by a burst beer barrel at a fake police roadblock on a country road at night, a stopped flat-bed truck behind, beer spreading across the road", "a skinny, jug-eared Irish American of about 22 in a too-big police tunic and peaked cap", "crime is asset inflation"),
  ("f2", "seen through the open window of a moving sedan in a bootleg convoy on a wet highway, headlights of the truck behind caught in a chrome wing mirror", "a Chinese American man of about 50 in round wire glasses, a three-piece suit and a homburg, thin-faced and neat", "passive creation of a wealth gap"),
  ("e3", "the driver of an open roadster at a level crossing at night, a smashed gate on the bonnet, sparks and locomotive steam behind, pink signal light", "a huge bull-necked Polish American of about 40, flat nose, cauliflower ear, flat cap", "and this right here is a next level scam"),
  ("c1", "a crew shouting beside a crashed getaway sedan burning against a lamp post under a teal theatre marquee, in a narrow side street", "three men who look nothing alike: a very tall thin Black man of 60, a short fat bald white man of 45 with his hat in his hand, a wiry young Mexican American of 20", "Robbery, robbery!"),
 ],
 "r2": [
  ("l03", "at the spoked wheel of a rum-runner's speedboat racing through night fog, a blue searchlight behind him", "a broad-faced Black seaman of about 55, grey stubble, navy watch cap", "it is state level manipulation"),
  ("l04", "on the deck of a low grey rum boat at night, a column of water from a warning shot behind his shoulder lit red and pink, a green running lamp beside him", "a pale, red-haired, freckled Irish American of about 30 with a boxer's split eyebrow, black fedora", "it is the devil with a radio station"),
  ("f3", "rowing a skiff at water level at night, the crew's own boat burning against a timber pier behind, fire on the water", "a slim Filipino American deckhand of about 28, hatless, soaked hair, wide cheekbones", "that drives the situation"),
  ("f4", "seen from high in the rigging of a schooner at night, looking up past the lens, sacks of bottles swung over the side and motorboats below", "a barrel-chested Portuguese American of about 60, heavy brow, big ears, tweed cap pushed back", "working people get paid in money"),
  ("e4", "sitting in the open door of a boxcar in a wet freight yard at night, whiskey crates behind, magenta and green signal lights in steam", "a very thin, elegant Black Pullman porter of about 65, white hair, sunken cheeks, bow tie undone", "ill gotten gains, no need to explain"),
  ("c2", "a crew shouting in a timber dock warehouse under strings of bulbs, barrels behind, guns held up at the rafters", "three men who look nothing alike: an enormous Samoan-looking dock worker of 35, a tiny old Jewish bookkeeper of 70 with thick glasses, a sharp-jawed Italian American of 25 with slick hair", "Call the police, it's a robbery!"),
 ],
 "r3": [
  ("c3", "a crew in a raided speakeasy, ankle-deep in spilled liquor on a mirror-like floor, axes held high, deep red and teal light", "four men who look nothing alike: a giant Swedish-looking blond of 30, a bald Black man of 50 with grey stubble, a small hook-nosed man of 60, a chubby baby-faced man of 19", "Debasement! Debasement!"),
  ("c4", "a crew at the foot of cellar steps with sparks showering on the right and deep blue light on the left, overcoats, guns low", "three men who look nothing alike: a long-faced Black man of 40 in a white fedora, a square-headed German American of 55 with duelling scars, a Greek American of 25 with heavy eyebrows", "It happened in da basement!"),
  ("c5", "three printers in ink-black aprons crowded together in a cellar print shop, a counterfeit press on fire behind them", "three men who look nothing alike: a stooped Jewish printer of 70 with wild white hair, a young Black apprentice of 18, a beefy red-faced Irish American of 45", "Printer is burning, now now what's occurring?"),
  ("e1", "in the foreground of an armoured truck hold-up on a city street at night, rear doors hanging open, split sacks, banknotes in the air, teal neon", "a dapper Cuban American of about 35 with a thin face and a cream fedora", "stacking up the cash by the grands"),
  ("e2", "on a rain-soaked iron fire escape during a chase, one arm flung wide, a window bursting beside him, magenta neon rain", "a tall gaunt Black man of about 45, sharp jaw, soaked homburg", "standard plans are for the working man"),
  ("f7", "in a grand marble bank hall at midnight, the round vault door blown open behind him, smoke, one red alarm lamp, gun held up", "a stocky Korean American of about 40 with a square jaw, bowler hat", "hungry people feed a revolution"),
  ("f8", "on a tar rooftop at night in front of a bullet-riddled wooden water tank spraying jets of water, purple neon behind, a Thompson held up on his far side", "a young, pretty-faced, soft-featured Italian American of about 24, hat tipped too far back", "then it's retribution, perhaps some execution"),
 ],
}
NEW = [
 ("n01", "They say, ya can't make money from a tree", "a fat, jolly white banker of 60 in a white dinner jacket, on the deck of a private yacht at night, a burning launch behind him"),
 ("n02", "work and get paid though, earning that dough", "a soot-faced Black foundry worker of about 40, in a steel mill at night, molten orange pour behind him, gang of men smaller behind"),
 ("n03", "but where does it go? nobody knows!", "a thin Jewish tailor of about 55 with a tape round his neck, in a back room as masked robbers empty his till in the background"),
 ("n04", "means of production means a reduction", "a broad Polish American factory hand of about 30, on a stopped assembly line of Model T bodies, a red warning lamp turning"),
 ("n05", "quantitative easing, grandma freezing!", "a Chinese American laundry owner of about 65, thin, behind a frosted window on a snowy night, steam behind, a coal stove gone out"),
 ("n06", "stimulus checks are next. Get wrecked!", "a young Black racing mechanic of about 24, at a crash-strewn dirt track at night, a hot rod on fire behind him, floodlights"),
 ("n07", "sorry, did I interrupt your meeting?", "an elegant Mexican American gunman of about 35 at the head of a long boardroom table, in the doorway smoke, bankers diving under it in the far background, red and gold light"),
 ("n08", "remember kids, the Fed is not your friend", "a craggy Irish American beat cop of about 58, bent toward the lens under a streetlamp, a paddy wagon burning at the end of the street"),
 ("n09", "this fiat system is insistent on debt's existence", "a wiry Italian American bookmaker of about 45, at a wall of chalk boards and ticker tape in a raid, tape flying, green shades"),
 ("n10", "stacks and stacks of elastic cash", "a huge Black enforcer of about 35 in a pale suit, between walls of banded banknote bundles in a basement counting room, pink and green lamps"),
 ("n11", "mob, angry at their shitty little job", "a wild-eyed Greek American dockworker of about 28, in a torch-lit crowd of strikers at the gates of a mill, smoke, an overturned car, crowd out of focus"),
 ("n12", "blaming each other is a sick little cover", "a slick Jewish radio announcer of about 40 at a big period carbon microphone held low at his chest, a smashed studio window behind him"),
 ("n13", "distraction IS the attraction", "a Black stage magician of about 50 in tails, in a burning vaudeville theatre, a spotlight on him, curtains on fire behind"),
 ("n14", "divide and conquer, just look at the hand", "a silver-haired German American card sharp of about 65, at a card table with a raid behind him, one empty open hand held out to the side"),
 ("n15", "stack up the vaults like a wheelbarrow", "a sweating stocky Puerto Rican man of about 38, wheeling a wheelbarrow of bullion through a vault corridor, sirens' red light"),
 ("n16", "who has elastic bands not plastic hands", "an old Colombian-looking gentleman of about 70 in a planter's white linen suit, in a greenhouse at night lit violet and amber, quiet, nothing happening but a moth at a lamp"),
 ("n17", "own the printer and you don't fear winter", "a bald Russian American counterfeiter of about 60, in a fur collar, in front of a press in a snow-drifted warehouse, blue daylight lamp and an orange brazier"),
 ("n18", "it's time to give, not just to take", "a young Black preacher of about 30 in a plain dark suit, on the steps of a soup kitchen at night, a long breadline behind him out of focus, warm lamp and cold blue"),
]
BAND = """The band stays the same people in every shot, in both places. THE SINGER is a Flow Character attached to the picture: never describe his looks or clothes, just write "the singer". The rest, always in these words: a Black upright bass player of about 60, tall and white-haired; a slim woman drummer of about 35 with bobbed black hair; a tubby young Italian American trumpeter of about 25; a wiry fingerpicking guitarist of about 70, bald,. The song's voice is one gravelly man, and the choruses are a gang chant, so in chorus shots the singer leads and the others shout along."""
BANDSHOTS = [
 ("d1", "the mob boss's den: a burgundy lounge, footlights along a small stage. The singer alone, close, low, footlights under his chin", "Robbery, robbery!"),
 ("d2", "the den: the singer big in the foreground, drummer and trumpeter behind him shouting", "Call the police, it's a robbery!"),
 ("d3", "the basement corridor behind the den: brick, pipes, a furnace door open with fire on the left, magenta and green light down the far end, the band on a bench shouting, the singer standing nearest us", "Debasement! Debasement!"),
 ("d4", "that corridor, from low by the furnace, the singer lit orange on one side and green on the other", "It happened in da basement!"),
 ("d5", "the den: bass player and singer sharing a light, a roulette wheel out of focus in front", "Printer is burning, now now what's occurring?"),
 ("d6", "the den: the guitarist's hands on the strings huge in the foreground, the singer sharp behind", "stacks and stacks of elastic cash"),
 ("b1", "under an iron bridge at night by the river: a car's big round headlamp blazing just out of frame on one side, the singer close, city lights on black water behind him out of focus", "Robbery, robbery!"),
 ("b2", "a brick road tunnel under the bridge with faded teal mosaics: two parked black sedans' headlights light the band in a row, the singer closest", "Call the police, it's a robbery!"),
 ("b3", "the wet cobbled quay at night: the singer big, the band behind him, the river red and green with reflections", "Debasement! Debasement!"),
 ("b4", "low on the quay: singer and trumpeter shoulder to shoulder shouting up, the bridge's girders above, rain", "It happened in da basement!"),
 ("b5", "the tunnel, from behind the bass player's shoulder, the singer facing us, lit by a headlamp", "Printer is burning, now now what's occurring?"),
 ("b6", "the bridge pier: drummer behind a small kit on the cobbles, the singer singing beside her, a stopped car's lamps behind", "own the printer and you don't fear winter"),
]
ACTION = [
 ("safe1", "A car pulling a safe out of a wall. There was a clip: a yellow 1920s sedan in a brick alley under one lamp, a masked driver leaning out of the window, a chain to one small green safe. It went wrong because two safes appeared and morphed. Make it simple: exactly one safe, chain tight, it slides out of the broken wall and across the cobbles. Nothing else. A locked camera."),
 ("rods4", "Two old-school 1920s hot rods, one teal, one black, racing flat out down a concrete river channel under arched bridges at dusk. Jack's words on the last one: 'the cars should be racing at high speed, not just going for a drive'. Use the research on speed. Close to the car, the world tearing past. Exactly two cars and they keep their shape."),
 ("a1", "A chase: the front wheel and running board of a 1920s car fill the frame, wet cobbles smeared under it, red light raking the tyre."),
 ("a2", "A chase: lens almost on the road, the tail of a 1920s car ripping away from us, neon streaks on the wet surface."),
 ("a3", "The getaway driver seen through the side glass at full speed, bands of coloured light sliding over his face, the world outside a blur. He is a sharp-faced man of about 30, gloves on the wheel, and his mouth is shut."),
 ("a4", "A static kerb camera with a lamp post beside the lens: a 1920s roadster blasts past and is gone in under a second, spray hanging."),
 ("a5", "A long-lens pan on a 1920s roadster at speed: car sharp, the lit storefronts behind a coloured smear."),
 ("a6", "Tyre smoke rolling across a low lens on a dark street, one 1920s headlamp burning through it, a car just about to leap off."),
 ("a7", "A robber in a BadCode balaclava fires a Thompson straight up at a bank's ornate ceiling: muzzle flash lights the wool, plaster dust drifts down, marble behind."),
 ("a8", "Two robbers in BadCode balaclavas run out of a bank's brass doors toward the lens carrying sacks, alarm lamp flashing red and white behind. Just the two."),
 ("a9", "The back seat of an open touring car at full speed at night: a robber in a BadCode balaclava holds a split sack and banknotes pour away behind the car into the coloured dark."),
 ("a10", "A police motorcycle rider of the 1920s, big and close beside us at speed, seen from a car's running board, his red lamp flaring, street lights streaking."),
 ("a11", "Lens low beside one small green safe being dragged on a chain down a cobbled street at speed: only the safe, the chain, and a wide fan of sparks, the road a streak."),
 ("a12", "A flatbed printing press close-up in a cellar: sheets of banknotes flying through it, flames reflected in the steel. The printer is burning."),
 ("a13", "First person, from the driver's seat of a 1920s roadster: gloved hands fight the big wheel, a wet night street with neon pouring toward us, the bonnet vibrating."),
 ("a14", "Night, a level road beside a dark river: two 1920s black sedans side by side at speed in long lens, door to door, sparks where they touch, lights streaking behind."),
]
def write(name, title, body, extra="", motion_extra=""):
    t = "# What Jack said\n\n" + jack + "\n" + VERDICT + "\n\n" + LOOK + "\n\n# Web research\n\n" + research + "\n" + f"# Your task\n\n{title}\n\n{body}\n\n" + RULES.format(extra=extra, motion_extra=motion_extra, out=HERE / (name + ".md"))
    (HERE / f"brief-{name}.md").write_text(t)
for name, shots in REDO.items():
    rows = "\n".join(f"- `{i}`. Setting, keep this: {s}. Who is in it now: {w}. Sung words: {l}" for i, s, w, l in shots)
    write(name, "Jack loved these singing scenes and their settings and vibes, but the same man keeps turning up, so each one is shot again with different people. Write a still and a motion prompt per shot. Keep the setting. Use the person given, described by what can't average out: age, build, face shape, nose, ears, teeth. Don't use the words handsome or rugged. In a crew shot give each man his own place, height and action.", SINGING + "\n\n" + rows, motion_extra=SUNG)
write("x1", "New singing shots, one line each, sprinkled through the verses. Each is its own small action scene or situation in the 1920s, given below. Write a still and a motion prompt per shot.", SINGING + "\n\n" + "\n".join(f"- `{i}`. {w}. Sung words: {l}" for i, l, w in NEW), motion_extra=SUNG)
write("b1", "The band, singing. All the band shots are redone so that they actually sing. Write a still and a motion prompt per shot.", SINGING + "\n\n" + BAND + "\n\n" + "\n".join(f"- `{i}`. {s}. Sung words: {l}" for i, s, l in BANDSHOTS), motion_extra=SUNG)
write("a1", "Action shots with no singing. Write a still and a motion prompt per shot, and use the research on speed and on keeping props simple. A fast cut uses one to three seconds. Exactly the number of cars, safes and people named, and say so in the motion prompt.", "The robbers' masks:\n\n" + MASK + "\n\n" + "\n".join(f"- `{i}`. {s}" for i, s in ACTION))
print("ok", len(NEW), sum(map(len, REDO.values())), len(BANDSHOTS), len(ACTION))
