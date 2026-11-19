# minimal-swap-patient-cadence: notes

The control take. The kept box is unchanged except for two things:
1. The delivery clause. I removed "tumbled out in quick clusters" and "rolling into each other". In their place is an unhurried, patient talking cadence: each couplet spread over two whole bars, never crammed, with a breath at the end of every line.
2. One added phrase in the instrumental. Between rules the beat plays alone for a moment, then the barked number lands by itself on the downbeat.

Tempo stays at 88 BPM so this take tests delivery only. Ten couplets at two bars each, plus the intro, gaps and fix, comes to about 70-75 s at 88 BPM, which fits durationSec 75.

What shaped it:
- Section tags work as structural signposts. A cue goes directly above the lines it affects, with one delivery cue per section. So every rule gets its own section tag, followed by a single direction line before the "Number ..." line. https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/suno-ai-4-5-metatag-tutorial, https://dev.to/promptmaster/the-anatomy-of-a-suno-prompt-6-parts-that-make-or-break-a-track-1i63
- An instrumental tag between vocal sections opens real space, which is what "[one bar of beat]" after the intro and before the fix is for. https://dev.to/promptmaster/suno-metatags-the-structure-tricks-most-people-never-find-3cad
- Brackets are suggestions, not commands. Short tags hold up best, and v6 reportedly handles short behavioural clauses. That is why the directions are kept short. https://github.com/mttkllr/suno-field-guide
- Lower variety keeps the style tags tight, so this control take has variety "off" and styleInfluence 70. https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/where-to-put-your-suno-prompt-guide
- Sparse boom-bap beats usually have no chorus and put the rapper up front, so "no hook" stays. https://en.wikipedia.com/wiki/Boom_bap
- The exclude field targets the fault Jack heard: double-time and rushed flow.
