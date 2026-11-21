# Brief: stills round 1 (portraits and story shots)

You write image prompts for Google Flow's image model (Nano Banana 2.1), 9:16 portrait. Each prompt is an EDIT that
receives the reference images listed for it; the prompt says what is in the new picture and points at each reference
by role ("the pub layout from the photo", "the tourist's face from her portrait"). Research the place and the people
on the web first (English countryside pubs, what such rooms and their regulars look like), then write.

Write the result to `prompts-r1.json` in this folder: a list of `{"id", "prompt", "refs": [file names]}`, two
DIFFERENT takes per id (ids `<ID>-a`, `<ID>-b`; vary the framing or moment, not the people or the room).

## The short
A pub quiz in an English countryside pub, evening. A quizmaster asks a question about voting; a table of four argues.
Comedy, played straight: real people, real pub, warm low light, nothing glossy, nothing like an advert.

## The room (references: Unsplash photos, used as the layout only; make a new picture of the same kind of room)
- `lX31bAy6ML0.jpg`: low dark ceiling beams, flagstone floor, wooden tables and chairs, warm lamps. The main room.
- `R6ddisVdIfU.jpg`: heavy timber beams, a small round wooden table and spindle-back chairs. The quiz table.
- `ULysA-AxywY.jpg`: beams over white walls, wooden benches. The bar end of the room.
- `5Ns22AXZ0D4.jpg`: the outside: an ivy-covered stone pub on a village street.
Never readable words anywhere: no pub names, signs, chalkboard writing, labels, logos or brand names on anything.

## The people (one big portrait each first: head and shoulders, the face large and sharp, the pub soft behind)
Name every person in every prompt by age, hair and clothes. Each has their own distinct clothes so they never merge.
- **QUIZMASTER (QM):** BadCode, in a balaclava, dressed as an over-the-top American stereotype: a white cowboy hat,
  a blue denim western shirt with pearl snap buttons, a bolo tie, a huge silver belt buckle, black gloves. Holds a
  microphone. Refs for him always include `mask-reference.jpg`, and every prompt with him must contain this sentence
  exactly: "The balaclava exactly as in the attached image: no holes, no skin, gloves." The mask: a navy knitted
  balaclava with a white ring around the face and a red triangle over his left eye (the right of the picture). No skin
  anywhere: gloves, long sleeves, collar closed up to the mask. No sunglasses (they would hide the triangle). Say what he
  wears; never name a real person, film or character.
- **TOURIST (T):** a white American woman of about 55 from Florida, on holiday: a sun-faded tan, highlighted blonde
  bob, a turquoise fleece zipped up over a pink polo, a lanyard-free bum bag; friendly, a bit out of place.
- **SWISS BLOKE (S):** a white Swiss man of about 40 who works in England: short neat brown hair, a trimmed beard,
  rimless glasses, a navy quilted gilet over a grey merino jumper; tidy and calm.
- **ONE-PARTY VOTER (V):** a Black British man of about 70, retired: short grey hair, grey moustache, a brown tweed
  jacket over a checked shirt and a knitted tie; proud, stubborn, likeable.
- **BOB:** a man of about 50, already cast: use `bob-face.jpg` for his face and clothes exactly; never change him.

## The ids (two takes each)
Portraits first (refs: the room photo `lX31bAy6ML0.jpg` for the background, plus the mask for QM):
- `QM`: the quizmaster portrait. `T`: the tourist portrait. `S`: the Swiss bloke portrait. `V`: the voter portrait.

Story shots (refs: the room photo named + the portraits of everyone in the shot; write the portrait file as
`portrait-QM.jpg`, `portrait-T.jpg`, `portrait-S.jpg`, `portrait-V.jpg`, `bob-face.jpg`, the picked portraits will be
saved under those names):
- `OUT` (ref `5Ns22AXZ0D4.jpg`): the pub from outside at dusk, windows glowing. No people needed.
- `QMASK` (`lX31bAy6ML0.jpg`, QM): the quizmaster standing at the front of the room with the microphone, asking the
  question; tables of drinkers in front of him, seen from behind or the side (name two or three of them).
- `TABLE` (`R6ddisVdIfU.jpg`, T, S, V, Bob): the four round the small table with an answer sheet and pints; T, S, V and
  Bob all clearly visible; everyone else turns to look at the tourist. Stage it so all four faces read.
- `TCU` (`R6ddisVdIfU.jpg`, T): close-up of the tourist at the table, talking, the others' shoulders at the edge.
- `VCU` (`R6ddisVdIfU.jpg`, V): close-up of the voter at the table, talking, indignant.
- `SCU` (`R6ddisVdIfU.jpg`, S): close-up of the Swiss bloke at the table, talking, calm.
- `BCU` (`R6ddisVdIfU.jpg`, Bob): close-up of Bob at the table, talking quietly.
- `BAR` (`ULysA-AxywY.jpg`, T, QM): the tourist at the bar ordering, the quizmaster standing beside her at the bar,
  facing her. One barman behind the bar (name him).
- `WHY` (`lX31bAy6ML0.jpg`, QM): the whole pub, every drinker turned towards the quizmaster at the bar, mid-shout,
  arms out; name at least six of them (age, hair, clothes), a mix of ages, men and women, at least two not white.

## Rules for every prompt
- Plain description of what is in the picture: who, where, doing what, the light. No camera brand or film stock words.
- Each face from its portrait, named by role. Faces big enough to read.
- 9:16 vertical. No text. No famous faces: if a face could be a known actor, change it.
