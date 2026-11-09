# Choruses with people: picks and rulings

- **2026-11-06, Kai:** "1A, no eye, black". Chorus 1 = the opening's own people a week after the sackings. No robot army or eye in either chorus. Chorus 2 ends on black into the war.
- **2026-11-06, mood board round 1:** https://claude.ai/artifact/RuyCTKTbrHAqDeH4UvcxfE (65 stills, 13 beats; Flow project 7c30dbaf).
  - 5 edits came back as the reference unchanged and were set aside in `moodboard/rejected/` (TR1-b-a, TR1-c-a, BD1-b-a, BD1-c-a, DW1-b-a).
  - The helicopter and the blackout were re-rolled once (HE1-b, LO1-b); the first tries were too small or not dark enough.
  - Watch for animation: GR1-c and BD1-c-c have children in frame, and Flow video may refuse them.
- **2026-11-06, round 1 votes:** 12 This (no notes): TR1-b-c, BD1-b-c, DW1-a-a, CA1-a-a, SH1-a-a, SH1-b-a, GR1-a-a, GR1-c-b, BS1-a-a, HE1-a-b, LO1-b-b, EM1-b-a. Kai: *"treble the number of images… the same atmosphere, the same scene, just in a slightly different composition where we might be able to use both together"*. Round 2 = three new angles of each pick (36), edited from the pick itself.
- **2026-11-06, mood board round 2:** 34 new angles on the 12 picks. Made as `flow_edit_image` coverage from each pick; 12 came back as near-copies of the pick and went to `moodboard/rejected/`, then were remade from written descriptions (`r2-batch/`, ids -d/-e/-f).
  - BS2-a and HE2-a were refused twice (a close side view of the woman in the car; a couple looking up), so they're skipped.
  - Flow throttled mid-run with "We noticed some unusual activity". It cleared after a few minutes (documented in docs/flow/failure-modes.md).
  - Watch: GR2-e has children in frame.
- **2026-11-06, round 2 votes:** 26 This (no notes): TR1-b-c TR2-a TR2-c, BD1-b-c BD2-c, DW1-a-a DW2-d, CA1-a-a CA2-a CA2-e, SH1-a-a SH2-d, SH1-b-a SH2-f, GR1-a-a GR2-d GR2-f GR1-c-b, BS1-a-a BS2-f, HE1-a-b HE2-f, LO1-b-b LO2-e, EM1-b-a EM2-f.
- **2026-11-06, Kai ruling: one chorus, not two.** *"doubling the chorus is a mistake altogether"*.
  - Chorus 1 is now the zoom into the monitor itself. The robot chorus (01 GPOM start 62.58–74.08) is cut, and the music goes straight from the monitor into the bank takeover.
  - Chorus 2 is halved to a single pass of the chant, filled only with the 26 picks. The robots, the eye and every other chorus-2 shot are out.
  - Measured: chorus 2's two passes are identical, **11.037 s each (32 beats at 174 BPM)**, so cutting one pass is seamless. Chorus 1's exact downbeat could not be pinned by beat detection: Kai's markers sit about 0.2 s off the grid, and the detector is ambiguous by one beat.
- **2026-11-06, cut r1 built:** Premiere sequence `01 GPOM chorus r1` (guid ad514baf), bin of the same name.
  - Built as a drop-in for one chant pass, not yet placed inside 01 GPOM start.
  - The 26 picks in story order: money → shops → the flight → blackout → the empty motorway, then one beat of black. Mostly one beat each (8 frames); the openers of each group and the blackout get two beats.
  - Each still has a slow 4% push (ffmpeg); 265 frames in total (11.04 s).
  - A1 carries the matching chant pass of the song (source 113.917 s).
  - Order: `cut-r1-order.txt`. Media and preview: `D:\badcode-videos\gitpush-origin-master\clips\choruses-humans\cut-r1\` (`chorus-r1-preview.mp4`).
- **2026-11-06, Kai:** the cut is exactly one pass, the length of `01 GPOM chorus r1` (11.04 s). Use about half as many shots (~13), and animate **every** picked still "with significant movement", so there's a wide choice of clips to pick from.
  - 26 Veo 3.1 Fast clips, 4 s each, one per pick. Motions in `video-jobs.json`; media in `clips/choruses-humans/video/`.
- **2026-11-06, clips made:** 25 of 26 picks animated, plus 2 spare takes (TR2-a-2, BS1-a-a-2); ~35 Veo 3.1 Fast generations spent.
  - TR2-c is missing. Its still was refused at upload three times; a re-saved copy uploaded, but the tool handed back a stale clip (a byte-for-byte copy of LO2-e), so it was deleted.
  - The video tool saved many clips under the wrong job ("late tile shifts a batch"). The helper matched every clip's first frame to its still, renamed the files and rewrote 18 recipe cards (marked "harvest-shifted").
  - Clip page: https://claude.ai/artifact/YNw3nRctYVNgTaAfpMtGnU

## 8 Nov: clip picks → timeline round 1
- Kai marked This on 14 clips (feedback/clips-r1/picks): TR1-b-c, TR2-a, BD1-b-c, BD2-c, CA1-a-a, SH1-b-a, GR1-a-a, GR2-d, GR2-f, BS1-a-a, BS2-f, HE1-a-b, LO2-e, EM1-b-a. "we possibly have enough to work with here."
- Kai: chorus 1 loses its second half (cut from the monitor zoom straight to the banks); this sequence replaces the robots in chorus 2, cut to the first half of chorus 2's music.
- Cut (scripts/gpom/choruses/cut_humans.py): 2 beats a shot, GR1-a-a 4, black 2 = 32 beats / 265 frames; each clip enters at its motion peak. HE1-a-b had white Veo pillarbox bars, cropped in.
- Timeline page: https://claude.ai/artifact/8gX5wpQjdyW3krCtRV14jN
