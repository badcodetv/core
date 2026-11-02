# The Speakeasy Mint ALT: cast (Flow Characters)

Jack, 2026-10-28: *"I think we need to make the characters in Flow, so that they look consistent."*

Ten Flow Characters in project `706836d3` ("Oct 28 - 09:38"), each with a **Portrait** (head and shoulders, plain grey
backdrop, one soft key from the left) and a **Body** (full length, same backdrop). Both made on Nano Banana 2, 4:3, in
the realistic 1920s look of round 3; cream baked-in borders cropped off before upload (`~/.cache/sm-cast/crop.py`).
Created with `scripts/flow/.tmp/br-make-chars.mjs` (SM Mayor via the MCP: its name saved late, its body via
`flow_character_body`). Every face has specific ordinary features (no bare demographics: celebrity-likeness rule).

🔴 **When a Character is cast, describe nothing about how they look** (memory: never-describe-a-referenced-character):
only position, action and the face's muscles. The round-3 prompts describe the cast in prose; the clean round must
swap those descriptions for the Character.

| Character | Scenes | Portrait (the bits that identify them) |
| --- | --- | --- |
| **SM Mayor** | 7, 8, 12, 13, 14, 17, 18, 21, 27, 32 | tall skinny man, sixties, long narrow face, hollow cheeks, pencil-thin grey moustache, mole by left eye, bowler, black three-piece with wing collar, heavy gold mayoral chain |
| **SM The Baker** | 2, 3, 4, 8, 26 | heavy-set Black man, fifties, shaved head, short grey stubble beard, broken nose, double chin, sweat-stained white vest, flour |
| **SM Grandma** | 6, 28, 29 | frail white woman, eighties, deeply lined, mole on right cheek, pale blue eyes, a missing tooth, grey wool shawl over her head, darned brown cardigan |
| **SM Red Leader** | 17 | stocky white man, forties, ginger mutton-chops, freckles, gap teeth, brown tweed three-piece, red carnation |
| **SM Blue Leader** | 17 | white woman, forties, black bob with fringe, round face, heavy dark brows, plain blue cardigan over a white collared shirt, blue carnation |
| **SM Doorman** | 5 (+ any gang boss) | heavy-set white man, forties, pockmarked face, flattened boxer's nose, toothpick, grey fedora, navy chalk-stripe three-piece |
| **SM Lippy** | 11, 15, 20 | fat white man, thirties, slicked black hair, jowls, scar through top lip (⚠️ faint in the portrait), cigar, collarless shirt and braces |
| **SM Cop Walrus** | 22, 23 (+ 1, 14 cars) | American officer, fifties, huge grey walrus moustache, ruddy, peaked cap, long blue coat with brass buttons |
| **SM Cop Ginger** | 22, 23 | young lanky American officer, ginger sideburns, freckles, sticking-out ears, peaked cap, long blue coat |
| **SM Stoker** | 13, 24, 28 | muscular white man, thirties, shaved head, heavy brow, broken nose, cauliflower ear, soot-black vest, coal dust |

Exact prompts: in each image's recipe card (written by the Flow MCP) under `docs/provenance/cards/`.

## Ids (all verified 2026-10-28: Portrait + Body present)

SM Mayor `1d7b612d` · SM The Baker `69b039f0` · SM Grandma `8dbcb463` · SM Red Leader `d3a3258f` · SM Blue Leader `03aee168` ·
SM Doorman `c0977714` · SM Lippy `de246c80` · SM Cop Walrus `9d57df54` · SM Cop Ginger `42030448` · SM Stoker `a876253b`.

⚠️ Leftovers from failed attempts, not to be cast: **"SM Baker"** `28973903` (body only, its portrait upload hung at 99%
three times) and an empty **"Untitled character"** `fb7c4bf7`. Delete once Jack agrees.

## First cast test (2026-10-28): scene 13 with SM Mayor (`C13-a/b`)

The face held in both takes (bowler, long narrow face, grin), but **the gold mayoral chain was dropped in both**, the
known pattern: a Character binds the face, not the costume (`docs/google-flow/nano-banana-2.md`, 2026-10-15). Proven
fix (Barry, 5/5): attach the Character's portrait image as a reference too and write "dressed exactly as in his
portrait reference". That needs the hand "@" route (reference + Character in one prompt), not the MCP's `character`
parameter alone.
