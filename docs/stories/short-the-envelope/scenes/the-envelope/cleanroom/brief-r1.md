# Brief: mood-board stills for a BadCode short, "The Envelope" (9:16, about 11-15 seconds)

You write prompts for Google's Nano Banana 2 image model (in Google Flow). These are first-look stills for a mood board: the director picks a look per beat.

## The idea, in the makers' words
Kai, 2026-11-13 meeting: an arms-deal envelope lands on a desk, stamped APPROVED BY THE CONSERVATIVE PARTY; the next one says APPROVED BY THE LABOUR PARTY. "The weapon sales will still happen, irrespective of who you choose." It sits next to Bank Robbery ("this is the distraction"). Kai's closing line: "They're going to print the money anyway."

**Point:** Some decisions don't change whoever you vote for; the vote is the distraction.

## The beats
- **A. Approved (1)** (key `tory`, letters `TO`, starts 0:00): An arms-deal envelope lands on a desk, stamped APPROVED BY THE CONSERVATIVE PARTY.
- **B. Approved (2)** (key `labour`, letters `LA`, starts 0:04): The next one lands: APPROVED BY THE LABOUR PARTY.
- **C. Anyway** (key `print`, letters `PT`, starts 0:08): "They're going to print the money anyway."

## What the director said for this job (verbatim)
"please make a selection of stills for each best short idea… like the horror one with the bread… Please clean room it all and research the internet to achieve it."

## Genre references to research
Political thrillers and spy-film inserts of documents landing on desks (House of Cards, Tinker Tailor, Le Carré adaptations), Whitehall interiors, arms-export licence paperwork (what a real UK export licence / MOD envelope looks like: buff envelopes, OHMS, crests — but invent the crest).
- Stamp wording must be exact and legible: beat A "APPROVED BY THE CONSERVATIVE PARTY", beat B "APPROVED BY THE LABOUR PARTY" (the parties' NAMES only, as text on a rubber stamp: no party logos, no real politician, no faces; hands at most). Beat B should rhyme with beat A (same desk, same envelope) so the cut lands.
- Beat C, "They're going to print the money anyway": a money printer / banknote press running regardless; no real banknote designs reproduced exactly (invent the notes).

## Rules for every short
- BadCode is an art collective: a superintelligence from a future that went wrong, sending warnings back. Dark humour, total authority, nurturing underneath. The target viewer is a working-class UK person whom the economy has failed: never mock them, name the decision-maker, never "you've been fooled".
- No real person's face or name in any prompt (no politicians, no rappers, no actors). No real company names, logos or brands.
- If a BadCode figure appears, it wears the BadCode balaclava; describe it with this sentence, verbatim: "The balaclava has no eye, nose or mouth holes, so no skin shows anywhere; a large white ring is stitched round the whole face, and one small red triangle with rounded corners, pointing down, sits high inside the ring on the right-hand side of the picture. Gloves on both hands; no robot parts."
- Vertical 9:16, for phones. This short has NO house look: find one. Your three prompts per beat must be genuinely DIFFERENT looks (different medium, era, palette, lens, lighting, staging), not three re-seeds of one idea. At least one should be photographic and at least one should break from realism.
- Google's Nano Banana 2 image model (in Google Flow): research how to prompt it (Google's own Gemini image guidance, recent practitioner write-ups) and how to avoid the glossy generic "AI look" (specific places, motivated light, real lens and film language, imperfection).

## Your task
1. Research first, on the open web, fresh: the model, the genre references this short leans on (named below), and any facts the visuals depend on.
2. Write THREE prompts per beat (nine in all), each 70-130 words, complete and standalone, each with a short "look" label (a few words naming the look).
3. Every prompt ends with the word "Thanks."
4. Read ONLY this brief; open no other file on this machine.

## Output
Write JSON to the path you are given: {"research": ["url — takeaway", ...], "notes": "anything the editor must know", "stills": [{"beat": "<beat key>", "id": "<LETTERS>1-a|b|c>", "look": "...", "prompt": "..."}, ...9]}. IDs: the beat's letters below + 1 + a/b/c (e.g. TO1-a).
