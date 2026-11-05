"""Round 7 (Jack 2026-11-05, notes on cut 6): fix the noted shots with new stagings, and more rapping to camera for a good mix.
Plain facts per shot, no prompt wording. z = fix (a new version of a noted shot), q = new rap-to-camera shot.
Clip-only fixes (no new still): v05 (the spin teleports) and v11 (gesture must match "don't just eat cake") go to the clip writers."""
import importlib.util, pathlib
_s = importlib.util.spec_from_file_location("r6shots", pathlib.Path(__file__).parent.parent / "r6" / "shots.py")
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
GANG = _m.GANG

FIXES = {
    "w1": [
        ("z01", "0:02", "intro (instrumental)", "THE GETAWAY, replaces k02: the gang's black 1920s getaway sedan (or truck) bursting out of somewhere at speed, RUST at the wheel. Jack's note: the driver's mask disappears in motion. Every masked face in frame must be large enough to read, facing the camera or three-quarter, the driver's face clearly visible through the windscreen or side window."),
        ("z02", "0:09", "intro (instrumental)", "TWO IN THE CAR, replaces k06: two of the gang (choose) in the front of a moving 1920s car in a city street chase, a near-miss with a fruit cart or a policeman. Jack's note: both had the wrong masks. Closer framing, both masks big and readable."),
        ("z03", "0:42", "Sorry, did I interrupt your meeting?", "THE PLANE, replaces k11: one robber (choose) hanging from a rope ladder under a low-flying 1920s trimotor or biplane over fields, cash bag in one hand. Jack's note: the mask was wrong; it was tiny in frame. Frame him close enough that the mask reads (the plane can be partly in frame)."),
    ],
    "w2": [
        ("z04", "0:18", "intro (instrumental)", "THE DOOR, replaces k26 (axes breaking a door down, which looked fake). Jack: \"maybe just have bullets fly through the door and woods flying everywhere, but no ai slop … or come up with a version of this that wont mess up in flow\". Use section 3 of the research: pick the staging most likely to look real and hold up when animated."),
        ("z05", "1:06", "Call the police, it's a robbery", "THE BARRELS, replaces a shot of whiskey barrels tumbling off a truck at a chasing car that looked like AI slop. A new, simpler staging of barrels (whiskey, Prohibition) being used to stop pursuit or spilling, chosen from the research for realism."),
        ("z06", "1:09", "Debasement, it happened in the basement", "THE SAFE, replaces a shot of a safe being chained to a car and pulled out of a brick wall, which looked awful. A new, more believable staging of the gang getting a bank safe (or its contents) out, chosen from the research."),
        ("z07", "1:30", "The right and the left both witness the theft", "MARINE IN THE ALLEY, replaces p08 (MARINE rapping to camera mid-bounce in a tenement alley at night, two old men in windows watching). Jack: \"the guy in the middle is a giant … try a different version of this that looks realistic\". Normal human scale against doors, windows and fire escapes; the line's idea (two sides watching the theft) can stay or change."),
    ],
}
RAP = {
    "w3": [
        ("q01", "0:22", "Let's see each day, make hay not free", "PLUM", "a rooftop by a wooden water tower over the city at dawn"),
        ("q02", "0:31", "Means of production, means of reduction", "BOTTLE", "a car assembly line with a half-built 1920s car body"),
        ("q03", "0:41", "Rent seeking, I'm just about eating", "CRIMSON", "a landlord's rent office with a ledger and a queue of tenants"),
        ("q04", "0:48", "It prints all the dollars that the government spends", "SILVER", "a newspaper press room, presses running"),
    ],
    "w4": [
        ("q05", "1:25", "Distracted by a dyspraxic flash", "MARINE", "the wings of a vaudeville stage, a chorus line behind"),
        ("q06", "1:35", "Institutional, dilutional, the usual", "RUST", "the marble steps of a courthouse"),
        ("q07", "1:53", "Stack up the vaults like a wheelbarrow", "all six", "a bank vault, wheelbarrows of cash"),
        ("q08", "2:00", "Biggie said, wait! / Rockin' 97", "PLUM and CRIMSON", "a 1920s radio-and-gramophone shop, a wall of horn speakers"),
    ],
    "w5": [
        ("q09", "2:24", "You know the real star is Pablo Escobar", "RUST", "a pool hall, green baize, a single hanging lamp"),
        ("q10", "2:37", "All gotten gains, no need to explain", "BOTTLE", "a grand hotel kitchen at night, copper pans"),
        ("q11", "2:42", "Own a printer and you don't feel winter", "SILVER", "a snowy city street by a coal brazier, people warming hands"),
        ("q12", "2:51", "So it's not very funny when you print more", "all six", "the deck of a Hudson river ferry, skyline behind"),
    ],
}
