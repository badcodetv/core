# lone-piano-clock — notes

What shaped it:

- **The style box is written as a short producer's brief, not a list of tags**, and kept to about 100 words. The order is genre and tempo, then the lead instrument, the clock, the drone, the feel, and finally the mix. Guides say v6 follows one clear genre and a few signature instruments better than a pile of competing adjectives. They also say Exclude should name specific things you can hear and only marks a soft boundary, so all the positive direction stays in the style box.
  - https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/optimize-suno-v6-style-of-music-prompt
  - https://github.com/mttkllr/suno-field-guide
  - https://pastebin.com/RK06uiKL
  - https://suno.com/release-notes/exclude-styles
- **Instrumental with empty lyrics:** guides say mixing instrumental and vocal modes is a common cause of stray "ghost" vocals. So the prompt adds voice-like terms (choir, humming, spoken word) to Exclude on top of vocals, and vocalGender is null.
- **Tempo and space:** Splice's dramedy guide gives about 90 BPM as the sweet spot between suspense and comedy. It also says lots of space between notes holds that balance, which matches the brief's 90 BPM clock. The prompt asks for long rests and a very low, sparse mix so the nine spoken lines can sit on top.
  - https://splice.com/blog/?p=40993
- **Deadpan as parody:** Lawson's book on comedy film music describes a "serious" dramatic underscore used straight as a parody of that same underscore, and dissonance as a deliberate ironic device. That is why the minor-second cluster is written as a "raised eyebrow" against an otherwise poker-faced repeated note.
  - https://radar.brookes.ac.uk/radar/file/0edb43b4-5356-4f93-a8a3-33d0f4ea3fe2/1/Seriously%20funny%20music%20-%209783031334214%20-%202023%20-%20Lawson.pdf
- **The clock:** this follows the ticking-clock-as-deadline idea, and library cues that pair sparse piano with a literal tick. The prompt asks for a real, dry, close mechanical clock locked to the beat.
  - https://nofilmschool.com/2018/06/interstellars-ticking-clock-hiding-suspense-plain-sight
  - https://www.musou.gr/music/album/warner-chappell-pm/colour-tv/CTV1315-counterclock-minimal-investigative-underscore
- **Settings:**
  - Model v6 (not wild), because restraint is the whole point.
  - variety "off", so the wording stays close to what was written.
  - Low weirdness (20) and high styleInfluence (80).
  - 60 s, which covers the 42.8 s cut with room to trim.
  - maxMode off.
- **Exclude:** this lists the brief's four (strings, drums, synth leads, vocals) plus close cousins (orchestra, cymbals, arpeggiator, risers and drops) that would fill the silence.
