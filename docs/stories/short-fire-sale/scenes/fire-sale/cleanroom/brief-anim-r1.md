# Brief: clips round 1 (image to video)

You write motion prompts for Google Flow's video model (Omni 1.2 Flash, "Frames" mode: the still is the first frame;
8 seconds; 9:16; it also makes sound, and a person can speak a line). Each prompt says what MOVES, in order, from the
first frame, what stays still, and the sound. Research first (how image-to-video prompts are best written for a locked
or slow camera, and how to get one clear spoken line with a natural mouth), then write.

Write `anim-r1.json` in this folder: a list of `{"key", "still", "motion"}`, two DIFFERENT takes per still
(`<still>a`, `<still>b`, e.g. `S01a`, `S01b`). Look at each still (in the reference folder given to you) before writing.

## The short
A comedy played straight, real-looking, ~25 seconds. A rainy English car-boot sale where a wheeler-dealer sells the
country's institutions as framed pictures. A heavy rich man arrives in a long black car with his sweating clerk and buys
the lot. The weary woman who passed by sits at home with her phone. At a village auction in a marquee, the clerk bids
£150,000; a masked auctioneer stops him: the limit is now fifty pounds, the same as everyone, and the whole tent holds up
£50 paddles. The cut uses 2 to 4 seconds of each clip, so the action starts within the first second.

## Rules for every clip
- Speech: ONLY where a still below gives a line, said once, clearly, in an English accent, mouth matching. Nobody else
  talks. Background: light rain, a murmur of a crowd, no music.
- Words in a picture (tags, "PURCHASES", "£150,000", "£50", "29") stay readable and spelled the same; no new text.
- The masked auctioneer keeps his balaclava exactly as it is (white ring, red triangle over his own left eye); no skin
  ever shows on him. He has no mouth, so he does not visibly speak.
- No new people enter. Faces keep their identity. No cuts inside a clip. The black car never gains a badge or ornament.
- Plain description of the motion; no camera brand words.

## The stills
- `S01` (the car boot): the woman in the olive parka walks towards the camera through the drizzle, glancing at stalls,
  unimpressed. A slow backward drift with her.
- `S02` (hospitals): the dealer in the flat cap holds up the framed hospital picture to the camera and says, cheerfully:
  "Hospitals, love. Forty quid." Rain drips off the gazebo.
- `S03` (the courts): the dealer holds up the framed gavel picture, shrugs and says: "The courts. Slightly used."
- `S04` (the car): the long black car rolls slowly towards and past the camera through the mud; people at the stalls turn
  to stare.
- `S05` (arrival): the heavy bald man steps out of the car under the chauffeur's umbrella, plants his cane, looks around
  smugly; the thin clerk scurries after him with the clipboard.
- `S06` (all of it): the heavy man, hand on the clerk's shoulder, says slowly and smugly: "All of it." The clerk, sweating,
  writes faster on the clipboard.
- `S07` (home): the woman on the sofa looks at her phone, its light on her face; she slowly lowers her mug of tea and
  stares. Rain runs down the window. Nobody speaks.
- `S08` (the auction): the clerk raises paddle 29 a little higher, wearily; a murmur in the tent.
- `S09` (the auctioneer): the masked auctioneer lifts his gloved palm in a calm "stop", then brings the gavel down once
  on the lectern. (His line is added later; he does not move a mouth.)
- `S10` (same as everyone): behind the heavy man and the clerk in the front row, more and more ordinary people raise
  their £50 paddles; the heavy man turns round, outraged. The auctioneer at the edge stays still.
