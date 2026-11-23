# Research: a believable fall for the claw's-view clip (round 3)

## What went wrong in round 2 (from r2clip-LIMPPOVa.jpg)
- The house drifts down and sideways across several frames (about 1.5 s) instead of dropping, then keeps sliding and turning
  over the pile for the rest of the clip. Nothing in it looks heavy.
- The framing also changes: the pile looks smaller and further away after the first frames, so the camera zoomed or pulled back.
- In short, no acceleration, no clear moment of impact, no settle, and a camera that moves.

## Real physics of this fall
- Free fall over 0.30 m: t = sqrt(2h/g) = sqrt(0.6/9.81) = about 0.25 s. Impact speed is about 2.4 m/s.
  At 24 fps that is about 6 frames from release to contact. A real drop is over almost before you see it. Anything
  taking a second or more reads as slow motion or floating.
- A hollow plastic or resin house a few cm across weighs a few grams to a few tens of grams. Air drag is negligible over 30 cm,
  so it falls straight down. It keeps whatever slight tilt or spin it had at release and does not glide sideways.
- It lands on a loose heap (other houses, coins, rolled notes). Granular beds absorb most of the energy. Experiments on
  grain-filled bodies show the bounce collapsing after the first impact
  ([Sci. Rep. 2013, granular damping](https://orbi.uliege.be/bitstream/2268/151368/1/srep02158.pdf); [Wooster thesis on granular
  fills and rebound](https://physics.wooster.edu/wp-content/uploads/2021/08/Junior-IS-Thesis-Web_2019_Shideler.pdf)).
  Expect at most one small hop of a centimetre or so.
- Sequence on impact: one corner or eave hits first. The house tips or rolls part-way onto a side, nudges one or two
  neighbours or a coin, and comes to rest at an angle within about half a second. After that it stays completely still.
  It does not slide across the pile.
- Sound: a short hollow plastic clack, plus a brief metallic chink and slither as a few coins shift. The claw motor hums in the background.

## Prompting findings (Veo / Omni-style image-to-video)
- In image-to-video the image already fixes subject, light and style, so spend the words on motion
  ([Google Vertex Veo best practices](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice);
  [Veo prompt guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)).
- Floatiness comes from missing weight: objects move at a constant speed with no acceleration
  ([Luma](https://lumalabs.ai/news/prompt-realistic-ai-videos)). Use verbs that carry mass, like "plummets" and "drops like a stone"
  instead of "falls" or "floats" ([Hailuo, impact and gravity](https://hailuoai.video/knowledge/simulating-impact-prompting-debris-gravity)).
- Spell out the chain: loss of support, downward acceleration under gravity, first contact point, small rebound, damped
  settle, rest ([Pippit physics prompts](https://www.pippit.ai/blog/ai-physics-prompts-weight-momentum-impact)). Give a measured drop
  ("drops 30 cm"), the first contact point, a short stop distance and a timing line ("fast fall, sharp impact, quick
  rebound, damped stop") ([Physics Pass](https://www.imaginary.app/blog/the-physics-pass-prompt-9-lines-that-make-motion-look-real-in-veo3gen-runway-gen)).
- Models drift toward slow motion because small frame-to-frame changes are easier to keep consistent. Counter it with
  strong subject verbs and real-time cues, and never use "slowly", "gently" or "drifts"
  ([LTX on slow motion](https://ltx.io/blog/how-to-fix-slow-motion-in-ai-generated-video)).
- One main event per clip is safest ([Pippit](https://www.pippit.ai/blog/ai-physics-prompts-weight-momentum-impact)). Give the camera its own
  sentence and call it a static shot where the camera stays completely still
  ([Veo prompt guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide);
  [DreamHost Veo 3.1 guide](https://www.dreamhost.com/blog/veo-3-1-prompt-guide/)).
- Google advises describing the wanted result rather than stacking "no ..." phrases, so state stillness positively
  ("rests motionless", "the pile stays exactly as it is").
- Naming the mass alone helps less than naming its effects (speed, short contact, small dent in the pile). Naming real
  time ("at normal speed", "in a quarter of a second") anchors the pace. 8 s is far longer than the event, so
  the prompt must say what fills the remaining time: a held, motionless rest.
- Prompting reduces ambiguity but does not make a simulator. Plan to run several seeds per prompt and pick the best
  ([positioniseverything](https://www.positioniseverything.net/how-to-fix-inconsistent-motion-and-impossible-collisions-in-ai-video-prompts/)).

## How the four takes differ
- c: plain physics chain with numbers (30 cm, quarter-second, one hop, rest).
- d: impact-led. The release is instant and the beats are the corner strike, the tip onto its side and two coins knocked aside.
- e: "dropped like a stone" with heavy-object verbs, motion blur on the fall, and the house buried slightly into the heap.
- f: timing script with second marks (0-0.3 s drop, 0.3-1 s settle, 1-8 s still) to stop late sliding.
