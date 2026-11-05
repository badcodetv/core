"""Round 8 (Jack 2026-11-05, notes on cut 7). y = a new, closer still for a wide action shot whose masks were too small to hold
(Jack: "fix the mask"), or for the getaway he called AI slop. Performer re-animations (masks drifting) go to the clip writer."""
import importlib.util, pathlib
_s = importlib.util.spec_from_file_location("r6shots", pathlib.Path(__file__).parent.parent / "r6" / "shots.py")
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
GANG = _m.GANG
STILLS = {
    "w1": [
        ("y01", "0:00", "intro (instrumental)", "THE GETAWAY OPENER, replaces z01 (a car bursting out of a garage through exploding hay bales, which Jack called AI slop). Use one of the three stagings in section 4 of the research, built to avoid its slop tells: the car already moving, one dominant motion, no smashing doors or flying debris. RUST drives. If masks are visible they must be large; a back-seat view where the masks face away is allowed."),
        ("y02", "0:25", "work can get paid though", "THE BURNOUT, replaces k07 (a high overhead shot of a black sedan sliding round a rain-slick crossroads at night in white tyre smoke, RUST at the wheel and BOTTLE leaning out of the window with a gun up; the masks were specks). Same gag, but framed so RUST's and BOTTLE's masks are large and face-on or three-quarter: e.g. low at the kerb as the car slides past close, or through the windscreen."),
        ("y03", "1:02", "Robbery, robbery!", "THE FLYING DIVE, replaces k03 (MARINE flying sideways through a bank lobby under a shattering chandelier, a Thompson in each fist pointed at the ceiling; the mask was small and dark). Same parody, framed close: his masked head and shoulders large in frame mid-dive, mask facing the lens, crystals falling behind."),
    ],
    "w2": [
        ("y04", "0:33", "standards bleeding, landlords needing", "THE HOUSE FRONT, replaces k18 (a silent-comedy gag: a two-storey timber house front has fallen flat around BOTTLE, who stands untouched in the open window frame, in a muddy street after a storm; he was a tiny figure). Same gag, framed closer and lower so BOTTLE fills more of the frame and his mask reads: the window frame around him, the fallen wall in the foreground."),
        ("y05", "1:06", "Call the police, it's a robbery", "THE SPLIT BARREL, replaces z05 (a masked robber in a mustard suit, PLUM, on a truck bed having shoved one oak whiskey barrel off; it lies split on the cobbles, whiskey spreading; the man was too small). Same moment, framed so the masked man is large: e.g. low beside the barrel looking up at him on the tailgate, or medium on him with the barrel in the foreground."),
        ("y06", "2:49", "Crime is asset inflation, passive creation", "THE BALLOON, replaces k24 (PLUM and BOTTLE in a gas-balloon basket above the clouds tipping banknotes out; the masks were small). Same gag, framed from the rim of the basket so both masks are large and face the lens, notes fluttering away below."),
    ],
}
