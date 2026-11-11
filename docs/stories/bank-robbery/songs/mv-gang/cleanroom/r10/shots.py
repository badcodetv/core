"""Round 10 (Kai 2026-11-11): the WHOLE gang rapping at the camera like a modern drill crew, each shot in a place
already in the film, adjusted slightly. h = hype. Plain facts per shot, no prompt wording.
Each shot attaches two pictures: a frame of the place from the film (places/<id>.png) and the gang line-up card."""
import importlib.util, pathlib
_s = importlib.util.spec_from_file_location("r6shots", pathlib.Path(__file__).parent.parent / "r6" / "shots.py")
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
GANG = _m.GANG.replace("A reference image of all six is ATTACHED to every gang prompt:",
    "Two pictures are attached to every prompt. One is a frame of the PLACE, taken from the film. The other is the gang's line-up card:")
# (id, the place as it is in the film, the adjustment)
SHOTS = {
  "w1": [
    ("h01", "the 1920s marble bank lobby, brass-and-glass front doors just burst open, morning light pouring in, customers and clerks about", "the doors stay wide behind them; the gang now stands in a tight pack on the marble just inside, performing to the lens while the customers keep their hands up"),
    ("h02", "a cracked white dry lake bed at golden hour, stripped-down 1920s roadsters racing, dust plumes, mountains behind", "the roadsters are parked in a rough arc behind them, dust still settling; the gang performs on the lake bed in front of the cars"),
    ("h03", "a varnished mahogany speedboat at night on a black bay, searchlight beam, city lights on the far shore", "the boat is tied up at a wooden jetty, searchlight sweeping behind; the gang performs on the jetty boards with the boat beside them"),
    ("h04", "a black steam train crossing a high timber trestle in late afternoon, big white steam plume, open country below", "the train has stopped on a siding; the gang performs on the ground beside the locomotive, steam rolling round their legs"),
  ],
  "w2": [
    ("h05", "a 1920s elevated railway, a wooden train car on the curve overhead, hard midday sun slicing through the steel beams, cobbled street below", "the gang performs on the station platform of the elevated railway, the train car standing with its doors open behind them"),
    ("h06", "a steel I-beam high over a 1920s city under construction, early morning gold sun, skyscraper frames behind", "the gang performs standing on a wide plank-decked floor of the steel frame, beams and the city behind them, nobody near an edge"),
    ("h07", "a skyscraper's art-deco observation deck at blue hour, an airship overhead, Manhattan lights below", "the gang performs on the observation deck, the city glittering behind them, the airship still in the sky"),
    ("h08", "inside a deep steel bank vault, the huge round vault door open, a bank clerk at a desk, warm lamplight", "the gang performs in the open mouth of the round vault door, the clerk at his desk sitting very still"),
  ],
  "w3": [
    ("h09", "a vast 1920s marble bank hall, brass teller cages down both sides, hanging globe lamps", "the gang performs in the centre aisle between the teller cages, the clerks' heads just visible behind the brass bars"),
    ("h10", "a 1920s roadhouse during a police raid, seen from the rafters, policemen in long blue coats, barrels and broken bottles", "the raid has frozen: the gang performs on the bar floor among the barrels while the policemen behind stand motionless, truncheons lowered"),
    ("h11", "a frozen river at night in a blizzard, black 1920s sedans with headlamps on, the gang in the snow", "the gang performs in front of the sedans, headlamps behind them cutting through the falling snow"),
    ("h12", "a wicker gas-balloon basket high above a sunlit sea of white cloud", "the gang performs on a grassy launch field at dawn with the half-filled balloon swelling behind them, ropes pegged down"),
  ],
  "w4": [
    ("h13", "a silver corrugated-metal trimotor plane over green farmland in summer", "the plane stands on a grass airfield behind them, propellers still; the gang performs on the grass in front of its nose"),
    ("h14", "a cramped 1920s radio studio padded with quilted maroon fabric, one deep-red lamp, a chrome microphone, a devil-horned shadow on the wall", "the studio is a little bigger: all six crowd round the chrome microphone, performing past it into the lens, their shadows huge on the padded wall"),
    ("h15", "a luxury 1920s Pullman dining car, white tablecloths, lamps on each table, a steward in a white jacket, countryside through the windows", "the gang performs in the aisle of the dining car, the steward holding his tray perfectly still behind them"),
    ("h16", "a 1920s newspaper press hall, rotary presses running, wide paper webs racing overhead", "the gang performs on the floor between the presses, paper webs racing over their heads"),
  ],
  "w5": [
    ("h17", "the granite steps of a columned bank at dusk, an explosion of flame and banknotes in the doorway behind", "the gang performs on the steps, banknotes still drifting down around them, the glow of the fire behind"),
    ("h18", "a 1920s city boulevard at dusk, theatre marquees lit, crowds, a cream open roadster, banknotes in the air", "the gang performs on the boulevard in front of the roadster, the crowd behind watching, marquee lights blazing"),
    ("h19", "a rain-wet cobbled street at night under a blazing theatre marquee, the gang walking at the lens in a V", "the gang has stopped walking: they hold their V formation on the wet cobbles and perform to the lens under the marquee"),
    ("h20", "a tar rooftop at dawn beside a wooden water tower, city brick towers behind", "the gang performs on the rooftop round the foot of the water tower, sunrise behind the city"),
  ],
}
