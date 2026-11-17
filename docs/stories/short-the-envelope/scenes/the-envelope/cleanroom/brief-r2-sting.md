# Brief: a "Sting switcheroo" version of a BadCode short, "The Envelope" (9:16, about 12-18 seconds)

You design the beats and write image prompts for Google's Nano Banana 2 image model (in Google Flow). These are first-look stills for a mood board: the director picks a look per beat.

## The short as it stands
Kai, 2026-11-13: an arms-deal envelope lands on a desk, stamped APPROVED BY THE CONSERVATIVE PARTY; the next one says APPROVED BY THE LABOUR PARTY. "The weapon sales will still happen, irrespective of who you choose."

**The closing line (Jack, 2026-11-15, exact):** "They're going to print the money and the weapon sales will still happen anyway, everything else is a distraction."

**Point:** some decisions don't change whoever you vote for; the vote is the distraction.

## What the director asked for (verbatim)
"please maybe do a 'the sting' switcharoo version of this and research the internet for what that is, then match the style and story to fit this and their vibe thanks. Please clean room it all and research the internet to achieve it."

## Your task
1. **Research first, fresh, on the open web:** what "The Sting" (the 1973 film) is, how its con and its switcheroo reveal work (who is really conning whom, how the audience is fooled along with the mark), and its look and vibe (era, setting, how it is structured and titled, its music, its costume and colour). Also what a "switcheroo" is, and the classic short cons it draws on. Also how to prompt Nano Banana 2 well and avoid the glossy generic AI look.
2. **Design the switcheroo version in 3 or 4 beats** (total 12-18 s). The voter is the mark. It must still be about the envelopes and the two stamps, and its reveal must be the switch: the choice between the two was rigged, the same deal goes through either way. The last beat carries the closing line above (it will be spoken; you may also put it on screen). Use the con-film structure and vibe as you found it, but the story is ours.
3. **Three prompts per beat**, each a genuinely DIFFERENT look that still fits that film's world and vibe (e.g. different medium, lens, staging, palette: one photographic, one that breaks from realism, and a third of your choice). Keep the look letters consistent across beats (all the "a" stills share one look, all the "b" another, all the "c" a third), so the director can pick one column and it cuts as one short. 70-130 words each, complete and standalone, each ending with the word "Thanks."

## Hard lines
- **Do not recreate the film.** No actor's name or likeness, none of its characters, no copy of its real title cards, poster, artwork or music. Its era, genre and vibe are fair game; the art, people and words must be invented.
- No real person's face or name (no politicians, no actors). No real party logos: the parties appear ONLY as the exact stamp text "APPROVED BY THE CONSERVATIVE PARTY" and "APPROVED BY THE LABOUR PARTY", legible. No real companies, brands or exact real banknote designs (invent them).
- Characters are anonymous types (a dealer, a mark, men in suits); hands are fine. If a BadCode figure appears, describe it with this sentence verbatim: "The balaclava has no eye, nose or mouth holes, so no skin shows anywhere; a large white ring is stitched round the whole face, and one small red triangle with rounded corners, pointing down, sits high inside the ring on the right-hand side of the picture. Gloves on both hands; no robot parts."
- BadCode is an art collective presenting as a superintelligence from a future that went wrong. Dark humour, total authority, nurturing underneath. The viewer is a working-class UK person the economy has failed: the joke is on the people running the con, never on the viewer; never "you've been fooled". Name the decision-makers.
- Vertical 9:16.
- Read ONLY this brief; open no other file on this machine.

## Output
Write JSON to the path you are given:
{"research": ["url — takeaway", ...],
 "notes": "how the con works in your version, and anything the editor must know",
 "beats": [{"key": "<short lowercase key>", "letters": "<2 capital letters, not TO, LA or PT>", "at": "0:00", "name": "<letter>. <title>", "blurb": "<what happens, one or two sentences>"}],
 "looks": {"a": "...", "b": "...", "c": "..."},
 "stills": [{"beat": "<beat key>", "id": "<LETTERS>2-a|b|c", "look": "<look label>", "prompt": "..."}]}
Beat name letters run S1, S2, S3 (e.g. "S1. The set-up"). IDs: the beat's letters + 2 + a/b/c (e.g. ST2-a).
