# Brief: three still prompts for a 15-second comedy short

You are writing prompts for Google Flow's image model (Nano Banana 2), which takes one text box and returns one picture.
Research on the web first: (1) what a UK high-street bank's mortgage-appointment room really looks like (furniture,
paperwork, screens, what the adviser wears) — look at real photos; (2) what a Cadbury Freddo looks like (a small
chocolate frog in a purple wrapper; describe it, don't rely on the brand name); (3) prompting advice for Nano Banana 2
in the MEDIUM you are given below.

## The short
A deadpan UK comedy. A bank mortgage adviser interviews Mr Davis, an ordinary middle-aged man, about a loan. It turns out
the mortgage is to buy a Freddo, the chocolate bar. The joke is that this is treated as a completely normal mortgage.
The adviser and Mr Davis are invented people; never name or suggest a real person.

## Three cuts (one prompt each)
1. **question** — the adviser across the desk, asking what the loan is for. Must read "serious mortgage meeting" at once.
2. **freddo** — Mr Davis answers; the small chocolate frog in its purple wrapper is in shot, tiny against the paperwork.
3. **punch** — the adviser takes it utterly seriously: the Freddo on the desk among loan forms, a calculator, a pen on a chain.

## Your medium
Write all three prompts in the medium named in the file `medium.txt` in this folder. Commit to it fully: name its
materials and process concretely (what it is made of, how it was made, its surface, its imperfections). Do NOT fall back
on film-photography words (film stock, grain, lens mm, halation) unless your medium IS photography.

## Rules
- Vertical 9:16. Put the facts of the shot first (who is where, facing which way, what is in their hands), then the
  medium in a sentence or two. 90-130 words per prompt.
- Describe only what should be in the picture. No text in the image except the word on a wrapper if your medium can do it.
- End every prompt with the word "Thanks."

## Output
Write `prompts.json` in this folder: a JSON list of three objects `{"beat": "question"|"freddo"|"punch", "look": "<6-word name of your look>", "prompt": "<the prompt>"}`.
