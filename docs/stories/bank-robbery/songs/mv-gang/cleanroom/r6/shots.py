"""Round 6 (Jack 2026-11-05): the gang rapping straight at the camera in cinematic Prohibition places,
moving like a famous early-2000s Detroit rapper live on stage. Plain facts per shot, no prompt wording.
p = performance. Four sealed writers, four shots each; every shot a different kind of place."""
import importlib.util, pathlib
_s = importlib.util.spec_from_file_location("r3shots", pathlib.Path(__file__).parent.parent / "r3" / "shots.py")
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
# the six men and the mask rule, unchanged since round 5; the reference is now the line-up with enlarged heads
GANG = _m.GANG.replace("standing in a row facing the camera, left to right PLUM, BOTTLE, CRIMSON, MARINE, RUST, SILVER.",
    "standing in a row facing the camera, left to right PLUM, BOTTLE, CRIMSON, MARINE, RUST, SILVER, with each mask's face shown up close in the bottom half. Say the masks are copied exactly from the close-ups.")

GLOSS = """# What the director wants (facts from his words)

- Stills of the gang RAPPING STRAIGHT AT THE CAMERA, "at cinematic cool prohibition era places". The man looks into the lens and performs to the viewer.
- "rapping like eminem does live in the early 2000s, with how they gesture": the stage body language in section 1 of the research, caught at the peak of one move. Never name him or any real person in the prompt; describe the body only. No obscene gestures.
- Sarcastic and too cool, with one deadpan touch (section 4) that gives the joke away. Not a cartoon.
- He loved before: a specific real-feeling place, one motivated light, real materials, colour in walls and clothes, glossy high-budget period film. He hated: generic AI gloss (everything wet and shiny, airbrushed, evenly lit), psychedelic effects, matching-colour crowds, people standing around for no reason.
- Faults seen before: the red triangle drifting to the centre of the mask or onto the wrong eye; a bare hand; signs printing made-up words; masks too small in frame to read.
- A period microphone on a stand or in the hand is allowed where it makes sense (a stage, a radio studio) or as the joke; elsewhere the hands are free to gesture.
"""

FAMILIES = {
    "w1": [
        ("p01", "0:20", "They say, you can't make money from a tree", "PLUM alone", "a speakeasy bar"),
        ("p02", "0:27", "Earning that dough, but where does it go?", "CRIMSON alone", "a grand railway terminal concourse"),
        ("p03", "0:36", "Quantitative easing, grandma freezing", "BOTTLE alone", "a late-night diner"),
        ("p04", "0:46", "Remember kids, the Fed is not your friend", "SILVER alone", "an art deco hotel lobby"),
    ],
    "w2": [
        ("p05", "0:59", "Have resistance to the facts I'm stating", "all six", "the steel girders of a skyscraper going up, high over the city"),
        ("p06", "1:04", "Call the police, it's a robbery", "all six", "a marble bank lobby, mid-robbery"),
        ("p07", "1:23", "Stacks and stacks of elastic cash", "RUST alone", "a garage full of lacquered getaway cars"),
        ("p08", "1:30", "The right and the left both witness the theft", "MARINE alone", "a tenement alley with fire escapes, at night"),
    ],
    "w3": [
        ("p09", "1:39", "Distraction is the attraction", "CRIMSON and PLUM together", "the stage of a movie palace in front of the screen"),
        ("p10", "1:50", "It is the devil with the radio station", "SILVER alone", "a 1920s radio broadcasting studio"),
        ("p11", "2:01", "Don't get high off your own supply", "MARINE alone", "a river dock at night, a rum-running boat unloading"),
        ("p12", "2:16", "Call the police, it's a robbery", "all six", "a packed jazz club, on the bandstand"),
    ],
    "w4": [
        ("p13", "2:24", "You know the real star is Pablo Escobar", "RUST alone", "a back-room gambling den"),
        ("p14", "2:32", "Stand up plans are for the working man", "BOTTLE alone", "a barbershop"),
        ("p15", "2:44", "Crime is asset inflation, passive creation", "PLUM alone", "a luxury Pullman dining car on a moving train"),
        ("p16", "2:55", "Hungry people feed a revolution", "all six", "the ring of a smoky boxing gym"),
    ],
}
