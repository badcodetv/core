I went through the picked take's page and a few sources on Suno prompting and psychedelic funk. Here's what I found and the five versions I'm proposing.

**What the research found**
- **The picked take's page:** dddd147b is titled brj-sr4-london-music-hall-talker-v6-w30, made on v6. The page only shows "psych, folk, funk" as tags, and the lyrics counter reads 3034/7500. The fresh listen says it opens on acoustic guitar picking and whistle, with the "Robbery!" gang chorus as the best moment. [suno.com/song/dddd147b…](https://suno.com/song/dddd147b-858d-42da-bd2f-9e316edab1b4)
- **What makes funk "psychedelic":** wah pedals, fuzz boxes, echo chambers and vocal distorters (Sly Stone took these from psych rock), plus acid-rock guitar, synths, and a focus on groove and texture over song form. Funkadelic's *Maggot Brain* is the landmark album. [Wikipedia – Psychedelic funk](https://en.wikipedia.org/wiki/Psychedelic_funk)
- **The gear behind it:** P-Funk's sound came from Eddie Hazel's fuzz lead on Big Muff, wah and phaser, and Bernie Worrell's clavinet run through wah and envelope filter as the rhythm backbone. An MXR Phase 90 added drama to simple rhythm parts. [Premier Guitar roundtable](https://www.premierguitar.com/artists/parliament-funkadelic-a-funk-guitar-roundtable), [Reverb – P-Funk gear](https://reverb.com/en-pt/news/the-essential-gear-of-parliament-slash-funkadelic)
- **Word order and instrument count:** Suno weights the first words of the Style box most. Long instrument lists can make the mix muddy, so name each layer by its job rather than piling them up. Suno responds well to named instruments like Hammond, clavinet, Moog bass and brass. [Soundverse](https://www.soundverse.ai/blog/article/how-to-write-effective-prompts-for-instrumental-music-on-sunoai-1313), [roo.beehiiv](https://roo.beehiiv.com/p/150-suno-ai-prompts-that-actually-work-in-2026), [Medium guide](https://medium.com/@abhisheksd2003/the-ultimate-suno-ai-prompt-guide-with-clear-tested-examples-2d827ffe8b3a)
- **Describing the voice:** spell it out in layers (role, register, texture, delivery, how it sits in the mix) rather than stacking adjectives. The Style box sets who is singing; the lyric tags shape the performance. [Jack Righteous – vocal direction](https://jackrighteous.com/ja/blogs/guides-using-suno-ai-music-creation/mastering-vocal-diversity-in-suno-a-detailed-tutorial-for-unique-sounds), [popularaitools – v6 vocals](https://popularaitools.ai/blog/suno-v6-vocal-prompts-expression-phrasing-2026)
- **Don't write "no sitar":** the Style box has no real negative, so just drop the word. "Sitar" is the most likely cause of the Indian opening, and the Exclude box already exists if it needs backup. [Medium guide](https://medium.com/@abhisheksd2003/the-ultimate-suno-ai-prompt-guide-with-clear-tested-examples-2d827ffe8b3a)

All five versions drop "Sitar" and keep English psych folk funk, 100 BPM, tin whistle, hand drums, the slinky funk bass, the talk-sung verses that break into a big sung chorus, and the grand gang backing vocals. Each one adds a different set of psych-funk layers and uses a different London singer. None of them shout, scream, rap fast or use an American accent.

```json
[
  {
    "name": "cockney-landlord-wah-clav",
    "idea": "Drop 'Sitar' from the box. The song opens on tin whistle over the groove, with nothing Eastern. The singer is a gravelly, older East London cockney baritone, a pub landlord who has seen it all: rough and amused, talking the verses in a slow, sly way, then opening into a cracked, warm music-hall belt on the chorus. Build the psych funk in layers: a wah-wah clavinet doing a tight rhythm part under the verses, then a fuzz lead guitar answering the chorus lines (Funkadelic style, as heard from an English pub). Keep the tin whistle, hand drums, slinky funk bass and the grand gang-vocal chorus."
  },
  {
    "name": "nasal-deadpan-phased-hammond",
    "idea": "Remove 'Sitar' and keep the opening on tin whistle and bass, so there's no Indian-sounding start. Change the singer to a reedy, nasal North London tenor with a dry, sardonic, deadpan delivery, like a bored satirist who smirks through the verses. On the chorus he lifts into a bright, sweet, theatrical melody. Add layers: a swirling phased Hammond organ in the verses, tape-echo repeats trailing the tin whistle, and tight brass stabs on the chorus. Keep the hand drums, slinky funk bass and big gang voices."
  },
  {
    "name": "brixton-baritone-dub-echo",
    "idea": "Cut 'Sitar' entirely and open on the tin whistle over hand drums and bass. The singer is a deep, warm South London baritone with a Brixton lilt: rich, rounded and unhurried, with laid-back spoken patter (slow, never rapped), then a soulful, full-throated sung chorus. The psych-funk layers lean towards dub and echo chambers: spring-reverb guitar skanks, a fuzz bass doubling the slinky bassline on the chorus, congas over the hand drums, and dub-delay throws at the ends of lines. Keep the gang voices behind the chorus."
  },
  {
    "name": "glam-crooner-moog-phaser",
    "idea": "Take out 'Sitar' so the intro is just tin whistle and groove, nothing Indian. Change the singer to a theatrical London glam crooner: a velvety high baritone with wide vibrato and a sneering, camp sideways delivery in the verses, then a huge, soaring showtune chorus with falsetto ad-libs. Add these layers: phaser rhythm guitar (Phase 90 swirl), a squelchy Moog synth bass under the slinky funk bass, and a falsetto backing choir plus string swells to make the chorus grand. Keep the hand drums and gang voices."
  },
  {
    "name": "market-barker-tape-flange-voice",
    "idea": "Drop 'Sitar'. The song starts with tin whistle over the funk groove. The singer is a husky, whisky-worn Thames Estuary market barker with a chuckle in his voice, selling the verses like stall patter at walking pace and then booming a big, warm, sing-along chorus. This is the most experimental take on the voice: double-tracked lead, tape flanging and a slapback echo on the verse vocal, with Sly-style vocal distortion only on the monologue asides. Add a full psych-funk stack: envelope-filter clavinet, wah guitar, a horn section and Mellotron flutes doubling the tin whistle. Keep the hand drums, slinky funk bass and gang chorus."
  }
]
```
