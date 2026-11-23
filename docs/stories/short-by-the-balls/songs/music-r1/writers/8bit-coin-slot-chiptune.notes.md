# 8bit-coin-slot-chiptune: what shaped it

- Voices follow the classic home-console sound chip layout: pulse (square) channels carry the melody, the triangle
  channel sits an octave down and works as bass, and the noise channel's white-noise mode is used for drum-like hats.
  The prompt names those three voices plainly so the model stays small and bleepy rather than filling out with synths.
  https://en.wikipedia.org/wiki/Ricoh_2A03 , https://www.nesdev.org/wiki/APU_basics
- Limited-channel arcade sound means a coin sound and a melody note compete for the same room, so the coin blips and
  credit chimes are placed on the offbeats, worked into the rhythm instead of laid on top.
  https://pixelartnerds.pages.dev/content/evolution-arcade-sound-design
- Early arcade music started as single-voice square-wave jingles, which backs up asking for short separate jingles
  (the falling lose cue, the jackpot fanfare) rather than one through-composed tune.
  https://www.giantbomb.com/profile/alianger/blog/
- Suno guidance: put unwanted elements in the Exclude box, not as "no X" in Style; leave lyrics empty for an
  instrumental; for jingles, skip verse/chorus structure. A precise style field pairs with a strong Style Influence,
  and Weirdness only needs raising when results feel generic, hence styleInfluence 80 and weirdness 35.
  https://blakecrosley.com/blog/suno-style-field-style-influence , https://hookgenius.app/learn/suno-negative-prompting/ ,
  https://github.com/mttkllr/suno-field-guide
- Room for the spoken line: the two near-silent bars between the lose jingle and the jackpot (about 3 seconds at
  150 BPM) are where the line sits. Duration is set to 20 seconds so the whole cue fits the short.
