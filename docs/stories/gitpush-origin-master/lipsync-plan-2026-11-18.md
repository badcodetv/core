# Lip-sync pass: plan (2026-11-18)

Kai, 18 Nov: "massively improve the lip syncing… the one thing that really throws everything out."
Method rules come from `.claude/skills/lip-sync-dub/SKILL.md` and `docs/rules/voices.md` (no LatentSync,
no speeding or slowing the picture, never chop a voice line into pieces, voice late not early).

## Which shots need it (found 18 Nov from the current cuts' edls + a frame of each line)

The music video half has no on-screen speech (newsreader only). In the story film, 18 human lines;
**12 show the speaker's face talking**, 6 are already mouthless (scope, wide crowd, chairs, hands).

| # | Scene (cut) | Line | Who | Shot |
| --- | --- | --- | --- | --- |
| 1 | A kill bots (d27) 129.2 s | row line 1 | Sandra | lip-6-0 |
| 2 | A 131.6 s | row line 2 | Derek | lip-7d-0 |
| 3 | A 133.7 s | row line 3 | Sandra | lip-7-0 |
| 4 | A 138.0 s | row line 4 | Derek | lip-7d-1 |
| 5 | A 140.0 s | row line 5 | Sandra | lip-7-2 |
| 6 | B the door (bridge r13) 12.1 s | "You mean... killing everybody." | old lady | br34b-in |
| 7 | C walk out (noaliens) 11.6 s | c4 line 0 | Sandra | c04r1-seat-t1 |
| 8 | C 14.2 s | "Doesn't bloody matter now, love." | Derek | c05r6-t1 |
| 9 | C 18.6 s | "We're not coming back, are we?" | Derek | c05r6-t1 |
| 10 | D crossing (r23) 4.4 s | "I hope this bloody plan works." | Sandra | D01h-t2 |
| 11 | D 32.1 s | d3 line 10 | old lady | D11c-t2a |
| 12 | D 44.0 s | d3 line 14 | Sandra | D08c-t2a |

Already mouthless, leave alone: B "They've blown up their own kill bot!" (scope), C "Bloody hell. Look at
that building." (wide), D "What is it?", d3 lines 13 and 16, "Are you ready for this?" (hands).

## The plan, per line

1. **Measure what's there (free).** `scripts/lipsync/row-measure.py` on each scene's current cut: how far
   each phrase is early or late, voice over a shut mouth. Gives a score to beat.
2. **Cross-fit what we already own (free).** Every earlier clip of the shot × every earlier voice take of
   the line, fitted whole (`voice-row-fit.py` style: onset + one tempo 0.97–1.15, never early). Kai's idea:
   one round's voice may sit better on another round's clip.
3. **Five new voice takes per line** (AI Studio, the cast voice locked in badcode.md, paid key, no cap),
   paced to sound natural, each transcribed so no word is lost.
4. **Five new talking clips per line** (Flow, Omni 1.2, Frames mode from the already-approved still, the
   exact words in the prompt, words sized to the voice's pace: about 5–6 s of voice per clip, no sign-off
   at the end of the prompt). Omni 1.2's lip-sync is not yet checked on this story: a guess it behaves like
   1.1; the first line tells us.
5. **Fit every pair** (5 voices × all clips) on the tracked mouth, score by onsets and b/p/m closures
   against the 12 fps mouth strip, keep the best three per line.
6. **A lip-sync picks page:** one tab per scene, each line shows what's in the film now beside the best
   three pairs, playing, with a pick and a note. Kai picks.
7. **Build the picks** into a new round of each scene's cut, then a new Premiere sequence per scene,
   swapped into `00 RENDER story`.

Order: scene A's row first (five lines, the worst-known, Kai at3436 "really bad"), then C, D, B.


## Update, 18 Nov evening: what works (scene A done)

Steps 3-5 changed after the breakthrough (method: top of `.claude/skills/lip-sync-dub/SKILL.md`):
clips first (5-10 per line on the tab pool, transcribed), a per-word table, then **re-voice the same words with pause tags
where the clips pause**, ranked by words inside -45..+125 ms. Kai picks by voice likeness as well as sync. Scene A picks:
`scenes/second-half-a-killbots/feedback/lipsync-picks-2026-11-18-r3.json`. Next: C, D, B with the same method.
