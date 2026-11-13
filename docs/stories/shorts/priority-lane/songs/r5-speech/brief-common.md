You write the voice description for Suno's **Speech (beta)** model, which turns a script into spoken audio. Research the internet first: Suno's own Speech announcement and tutorial, recent reviews and practitioner guides from October and November 2026, and how British accents and voice types are best described to AI voice models. Base your work on what you find. Do not read any file on this machine except this brief.

## The job
A 14-second UK short. Night, rain. Inside an ambulance, two paramedics and the driver fight to save a dying old man. At a red light a police outrider stops them so a politician's car can cross. In the back of that car the minister is on the phone, furious about canapés. The patient flatlines.

Each role is generated on its own, **voice only, with Background music switched OFF**: no music, no sound effects (those are added separately in the edit). One speaker per take.

Jack, the director, on the last round: "the songs are american they should be english … there is no difference in voices between the ambulance lot and the politician". So:
- every voice is **English (British)**, never American
- the crew and the minister must sound like **different classes of people**
- it must feel like a real British TV hospital drama, urgent and human, not a cartoon

## The form you are writing for
- **Script:** the exact words, plain text (no brackets or tags inside the words).
- **Style / tone box:** one plain paragraph that describes the voice and the delivery. Write plain sentences, never bracketed accent words (testers found brackets confused it). Say what you want rather than listing what you don't want.
- **Vocal Gender:** Male or Female.
- **Variety:** Off (Exact style), Normal, High, Extra or Max.
- Background music: OFF (fixed).

## What to write
THREE genuinely different takes on your role: a different age, region, or way of delivering it for each (you choose, and justify each in a few words). For every take give the style box (40 to 90 words), the Vocal Gender, the Variety, and the script exactly as given below. You may only add punctuation to the script, for breath and pace (an ellipsis, a dash, an exclamation mark); never change a word.

## Output
Write JSON to the path you are given: {"research": ["url — takeaway", ...], "takes": [{"idea": "...", "style": "...", "gender": "Male|Female", "variety": "...", "script": "..."}, ...3], "notes": "anything the editor should know (optional)"}
