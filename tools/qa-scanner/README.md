# qa-scanner: catch defects in AI stills and clips before a person sees them

Made for bp-videos (2026-11-25) after a reviewer kept finding obvious faults (extra arms, people floating, shirt
numbers, pasted-in crowds, all-white crowds) that the assistant had shown without fixing. A vision model (Gemini)
answers ONE yes/no question per checklist item, on the whole frame plus four zoomed quarters (small faults only show
when zoomed). Clips (mp4/mov/webm under 15 MB) are sent whole and judged on the clip checklist.

## Needs
- Python 3 and Pillow (`pip install pillow`). No other packages: it calls the Gemini REST API directly.
- `GEMINI_API_KEY` in the environment or in a `.env` in the project (it looks in the current folder and upward).
- Models tried in order: gemini-3.5-flash, gemini-3-flash-preview, gemini-2.5-flash (edit MODELS in qa.py).

## Use
    python3 qa.py checklists/generic.json shot1.jpg shot2.jpg clip.mp4 [--ref reference.jpg] [--prompt "what it was meant to show"] [--json report.json]

Prints PASS/FAIL per file and, for each failed item, what it saw, where, and the fix. Exit code 1 if anything fails.
`--ref` adds a reference image (a set, a character, a product) for the "matches the reference" question.

## The rule that makes it useful (the fix loop)
1. Scan every take as it lands, before showing anyone.
2. A failing take is FIXED, not reported: surface faults (text, logos, colours) by a short edit; people faults
   (anatomy, floating, pasted-in, diversity, counts) by regenerating from words with the findings written in.
3. Scan again. Up to three passes per shot; then show the best take and name any flag that remains.
4. Every new fault a reviewer names becomes a new checklist item, so it is caught next time.

## Known limits (tested on bp-videos rounds)
- Strong: limbs, extra arms, numbers/logos, pasted people, headcount shortfalls, morphing and duplicated objects in clips.
- Weaker: physics. A general "anything wrong?" missed a levitating jump; the specific feet-and-shadow question caught it.
  Ask specific questions.
- It is not deterministic: the same image can pass once and fail once on a borderline item. For a final pick, a 2-of-3
  vote is safer (run it three times).
- Some flags are judgement calls (e.g. a stadium "resembling" a real one); a person decides those.
- Research and sources: RESEARCH.md.

## Files
qa.py · checklists/generic.json (start here) · checklists/example-womens-football.json (a full project checklist) ·
RESEARCH.md
