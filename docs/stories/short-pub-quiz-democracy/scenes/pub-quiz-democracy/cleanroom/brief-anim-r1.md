# Brief: motion prompts, clips round 1

You write image-to-video motion prompts for Google Flow's video model (Omni 1.2 Flash, Frames mode: the still is the
first frame), 9:16, 8 seconds, no audio used (voices are added later, so mouths must move with the exact words given).
Look at each still before writing. Research how to prompt this kind of model for lip movement and small, real
performance if you need to.

Write `anim-r1.json` in this folder: a list of `{"key", "still", "motion"}`, TWO different takes per clip (keys
`<CLIP>a`, `<CLIP>b`; vary the performance, never the people or the room). `still` is the still's id below.

## Rules for every prompt
- The camera stays locked off unless the clip says otherwise. The room, the light and every person stay as in the
  still: nobody new arrives, no face changes, no text appears anywhere.
- A speaking person says EXACTLY the words given, in quotes, at a natural brisk pace, then stops and listens. Only the
  speaker's mouth moves for words; everyone else listens and reacts (eyes, small nods), mouths closed.
- Real, small, believable performance: a pub, not a stage. No big theatrical gestures unless written.
- The quizmaster wears a denim balaclava with a white ring round the face and a red triangle over his left eye: he
  has no visible mouth, so he speaks with his head and hands only. The mask keeps facing the camera, the ring and the
  triangle never change or move to the other eye.
- End each prompt with the line `Thanks.`

## The clips (still id: what happens)
- `P01` QUESTION: the quizmaster at the front lifts the microphone and asks his question, one gloved finger up, a
  little swagger; the drinkers in front look up from their sheets toward him. (His words, for timing only, no mouth:
  "Round two. Florida, twenty twenty. They voted Trump. What else did they vote for, same ballot?")
- `P02` TABLE: everyone at the table turns to look at the tourist (centre, turquoise fleece). She says "I plead the
  Fifth." with a sheepish little smile, hands up a touch. The others stare at her.
- `P03` TOURIST: the tourist says "I liked both things." sincerely, with a small shrug, as if it's obvious.
- `P04` VOTER A: the older man in the tweed jacket says "So they wanted both?" puzzled, leaning in.
- `P04` VOTER B (key `P04B`): the same man says "You can't just like things. You get the whole party. Five years."
  firmly, one hand flat on the table on "whole party", proud and stubborn.
- `P05` SWISS: the man in glasses and the navy gilet says "Back home we vote on each thing. We had a vote on cow
  horns." calmly and matter-of-fact, a tiny shrug on "cow horns".
- `P06` BOB: the man in the olive waterproof says "So why can't we?" quietly, deadpan, then a small look round at the
  others.
- `P07` BAR: the tourist at the bar says "Can I get the crisps but not the nuts?" to the quizmaster beside her; the
  quizmaster turns his head to her and answers with a slow shake of the head and a gloved hand gesture (his words,
  for timing only, no mouth: "Comes as a set."). The barman pauses mid-pour.
- `P08` WHY: the whole pub shouts "Why?!" at the quizmaster at once, everyone's mouth open on the same word, hands
  thrown up, some half-standing; the quizmaster shrugs slowly, gloved palms up.
- `P00` OUTSIDE: the pub at dusk, almost still: lamplight flickers in the windows, a little mist drifts over the road,
  a very slow push in toward the door.
