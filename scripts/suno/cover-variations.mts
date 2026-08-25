/**
 * The Camping cover A/B set — ten style boxes, one variable each.
 *
 * The rules this file obeys, each bought with a failed round in docs/stories/camping/songs/camping.md:
 *
 *   HEAD and TAIL are byte-identical in all ten. `British post-punk spoken word` owns the
 *   vocalist pool and therefore the casting; the two voice sentences are what keep Bob and
 *   Tarquin two different men; the amen clause and `played straight` are the register. A
 *   variation that edits any of them is not testing a genre, it is testing four things at once.
 *
 *   Only the MIDDLE moves — the "Four steps" arrangement sentence. That is the layer sitting on
 *   top of the drum and bass, which is the thing we are actually auditioning.
 *
 *   The style box caps at 1000 characters and the accepted original runs 997. So a variation
 *   SWAPS a clause, never appends one: a maxed box outvotes its own vocal clauses.
 *
 *   Excludes are subtractive per variation. Half these genres are banned by the accepted
 *   exclude list, so asking for strings while still excluding `violins` produces the original.
 */

/** Casting + voices. Never edited. */
export const HEAD =
  'Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ' +
  'ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, ' +
  'smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British ' +
  'man: higher, clean, plummy BBC English, talking down from a wide room. '

/** Fills and register. Never edited. */
export const TAIL =
  ' Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling ' +
  'over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.'

/** The accepted round-17 exclude list. Variations remove from it, never add. */
export const EXCLUDE_BASE =
  'singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, crooning, clean sung melody, ' +
  'autotune, harmonies, grime MC, UK drill, road rap, trap, hip hop, young MC, American accent, American vocal, ' +
  'US rap, transatlantic, southern drawl, ragga MC, toasting, Jamaican accent, dancehall vocal, soprano, ' +
  'operatic vocals, vibrato, angelic voices, sustained vocal notes, female vocal, choir, orchestral strings, ' +
  'violins, cello, string section, piano, glockenspiel, brass band, marching band, oompah, dixieland, guitar solo, ' +
  'lead guitar, shredding, guitar strumming, power chords, acoustic guitar, wah, live rock band, epic trailer music, ' +
  'reggae, dub, ska, music hall, vaudeville, pantomime, ragtime, honky-tonk, liquid dnb, jump up, pop, lo-fi, ' +
  'jaunty, playful, whimsical, bouncy, comedic, novelty, parody, uplifting, major key, double time, tempo change, ' +
  'half-time, slow tempo'

export interface Variation {
  id: string
  name: string
  /** One line: what is under test. */
  thesis: string
  /** The "Four steps" sentence. The only thing that moves. */
  middle: string
  /** Exclude keywords lifted for this variation, and why. */
  lift: string[]
  liftWhy: string
}

export const VARIATIONS: Variation[] = [
  {
    id: 'cover-01-strings',
    name: 'Strings intro',
    thesis: 'A cold string section opens it, and the drop tears it away.',
    middle:
      'Four steps: a cold unaccompanied string section, violins and violas alone, one bleak sustained figure; ' +
      'then the voice over a low palm-muted electric guitar riff — distorted rock tone, one short ' +
      'figure repeating, never a solo, never chords, running under every vocal section; then a dry chopped ' +
      'breakbeat under the vocal, no bass; then the drop, strings and guitar out, kit at full weight, Reese sub ' +
      'and a screaming detuned wavetable lead cut against it.',
    lift: ['orchestral strings', 'violins', 'cello', 'string section'],
    liftWhy: 'the accepted list bans all four, so the strings would never arrive',
  },
  {
    id: 'cover-02-brass',
    name: 'Bitter brass',
    thesis: 'Horns take the job the guitar was doing.',
    middle:
      'Four steps: one long low detuned synth note; then the voice over a dirty brass section — trombone and ' +
      'baritone saxophone, one short figure repeating, never a solo, never a fanfare, running under every vocal ' +
      'section; then a dry chopped breakbeat under the vocal, no bass; then the drop, horns stabbing hard on the ' +
      'downbeat, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it, so brass and ' +
      'break are one piece of music.',
    lift: ['brass band'],
    liftWhy: '`marching band`, `oompah` and `dixieland` stay banned — they are what stops brass going comedy',
  },
  {
    id: 'cover-03-two-guitars',
    name: 'More guitar',
    thesis: 'The indie layer you already like, doubled. The safest variation.',
    middle:
      'Four steps: one long low detuned synth note; then the voice over two electric guitars — a low palm-muted ' +
      'riff underneath and a thin chorus-pedal jangle over the top, one short figure each, repeating, never a solo, ' +
      'never chords, running under every vocal section; then a dry chopped breakbeat under the vocal, no bass; then ' +
      'the drop, both guitars out, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it.',
    lift: [],
    liftWhy: 'nothing lifted — this variation lives entirely inside the accepted list',
  },
  {
    id: 'cover-04-blues',
    name: 'Blues',
    thesis: 'The riff becomes a bottleneck slide on a valve amp.',
    middle:
      'Four steps: one long low detuned synth note; then the voice over a dirty electric blues guitar — bottleneck ' +
      'slide, minor pentatonic, valve amp on the edge of breakup, one short figure repeating, never a solo, running ' +
      'under every vocal section; then a dry chopped breakbeat under the vocal, no bass; then the drop, guitar out, ' +
      'kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it.',
    lift: ['wah'],
    liftWhy: '`guitar solo`, `lead guitar` and `shredding` stay banned — the slide is a riff, not a lead break',
  },
  {
    id: 'cover-05-soul',
    name: 'Soul',
    thesis: 'A warm keys bed under cold words. Warmth is the variable, not the words.',
    middle:
      'Four steps: one long low detuned synth note; then the voice over a warm Hammond organ and Rhodes bed, minor ' +
      'chords held long, one short figure repeating underneath, never a solo, running under every vocal section; ' +
      'then a dry chopped breakbeat under the vocal, with a walking soul bassline moving under it; then the drop, ' +
      'keys out, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it.',
    lift: ['piano'],
    liftWhy: 'Rhodes and Hammond read as piano-family to the model; `major key` stays banned so it cannot go sunny',
  },
  {
    id: 'cover-06-shoegaze',
    name: 'Shoegaze wall',
    thesis: 'Verses stay dry and close; the drops become a wall of noise.',
    middle:
      'Four steps: one long low detuned synth note; then the voice over a low palm-muted electric guitar riff — ' +
      'distorted rock tone, one short figure repeating, never a solo, never chords, dry and close under every vocal ' +
      'section; then a dry chopped breakbeat under the vocal, no bass; then the drop, that same guitar swelling into ' +
      'an enormous reverbed wall of noise, kit at full weight, Reese sub cut against it.',
    lift: ['power chords'],
    liftWhy: 'a wall needs sustained chords; `guitar strumming` stays banned so it does not become an acoustic strum',
  },
  {
    id: 'cover-07-dub',
    name: 'Dub soundsystem',
    thesis: 'Bass first, everything else stripped, delay throwing the vocal across the bar.',
    middle:
      'Four steps: one long low detuned synth note; then the voice over a low palm-muted electric guitar riff, one ' +
      'short figure repeating, never a solo, with heavy tape delay throwing the end of every vocal line across the ' +
      'bar and spring reverb on the snare; then a dry chopped breakbeat under the vocal, sub bass first and ' +
      'everything else stripped out; then the drop, guitar out, kit at full weight, Reese sub and a screaming ' +
      'detuned wavetable lead cut against it.',
    lift: ['dub'],
    liftWhy: '`reggae`, `ska`, `ragga MC` and `Jamaican accent` stay banned — we want the mixing desk, not the genre',
  },
  {
    id: 'cover-08-folk',
    name: 'English folk intro',
    thesis: 'Something almost pretty opens it, and the drum and bass demolishes it.',
    middle:
      'Four steps: a lone acoustic guitar and mandolin, English folk, one plain pretty figure played completely ' +
      'alone; then the voice over a low palm-muted electric guitar riff — distorted rock tone, one short figure ' +
      'repeating, never a solo, never chords, running under every vocal section; then a dry chopped breakbeat under ' +
      'the vocal, no bass; then the drop, the acoustic gone, kit at full weight, Reese sub and a screaming detuned ' +
      'wavetable lead cut against it.',
    lift: ['acoustic guitar', 'guitar strumming'],
    liftWhy: 'both are banned outright, and the intro is nothing but an acoustic',
  },
  {
    id: 'cover-09-industrial',
    name: 'Industrial',
    thesis: 'No guitar anywhere. The coldest, most machine-like version.',
    middle:
      'Four steps: one long low detuned synth note; then the voice over metallic industrial percussion — struck ' +
      'steel, anvils and factory noise, one short figure repeating, never a solo, no guitar anywhere on this record; ' +
      'then a dry chopped breakbeat under the vocal, no bass; then the drop, kit at full weight, a distorted ' +
      'analogue bass and a screaming detuned wavetable lead cut against it, so synth and break are one piece of music.',
    lift: [],
    liftWhy: 'nothing lifted',
  },
  {
    id: 'cover-10-orchestral',
    name: 'Full orchestral',
    thesis:
      'Strings and horns carry the whole record. Rounds 1-14 abandoned this direction; this is the honest re-test.',
    middle:
      'Four steps: a cold string section and low brass alone, one bleak sustained figure; then the voice over ' +
      'strings and horns playing one short figure repeating, never a solo, never a fanfare, running under every ' +
      'vocal section; then a dry chopped breakbeat under the vocal, no bass; then the drop, the whole orchestra at ' +
      'full weight against the kit, Reese sub and a screaming detuned wavetable lead cut across it, so orchestra and ' +
      'break are one piece of music.',
    lift: ['orchestral strings', 'violins', 'cello', 'string section', 'brass band'],
    liftWhy: '`epic trailer music` stays banned — that is the clause holding this back from Hollywood',
  },
  // ── Round 11, 2026-08-25. Not part of the A/B: the merge of the two winners. ──
  {
    id: 'cover-11-dub-guitar',
    name: 'Dub + guitar',
    thesis:
      'Kai picked 07 Dub soundsystem, and liked 03 for the guitar. This is 07 with the second guitar from 03 — ' +
      'the dub desk (tape delay on the line ends, spring on the snare, sub first) over two guitars. Where the two ' +
      'disagreed at step three (dub: sub bass first; guitar: no bass) dub wins, because dub is the one that was chosen.',
    // 07's box ran 996 and 03's 973; the union was 1101. Trimmed to 990 by cutting only what the lyric cues
    // already say (`detuned`, `under the vocal`) and adjectives (`heavy`, `thin`, `electric`). Nothing cut
    // from casting, the `never a solo, never chords` guard, or `under every vocal section` (§4f).
    middle:
      "Four steps: one long synth note; then the voice over a low palm-muted guitar riff with a chorus-pedal " +
      "jangle over it, one short figure each, repeating, never a solo, never chords, under every vocal section, " +
      "tape delay throwing every line's end across the bar, spring reverb on the snare; then a dry chopped " +
      'breakbeat, sub bass first, nothing else; then the drop, guitars out, kit at full weight, Reese sub and a ' +
      'screaming wavetable lead cut against it.',
    lift: ['dub'],
    liftWhy: 'as 07 — `reggae`, `ska`, `ragga MC` and `Jamaican accent` stay banned; we want the mixing desk, not the genre',
  },
]

/** Drop the lifted keywords out of the accepted list, leaving the commas tidy. */
export function excludeFor(v: Variation): string {
  const keep = EXCLUDE_BASE.split(', ').filter((k) => !v.lift.includes(k))
  return keep.join(', ')
}

export const styleFor = (v: Variation) => HEAD + v.middle + TAIL

/**
 * What the take is called in Suno. Human-readable, because the point of the set is sitting and
 * listening to ten of them — a slug in the clip list tells you nothing at the moment it matters.
 * Kept under 48 characters: `listTakes` slices the row title there.
 */
export const titleFor = (v: Variation) => `Camping cover ${v.id.slice(6, 8)} - ${v.name}${SET}`

/**
 * Which run of the set this is. It exists because `create()` waits for two takes whose title
 * matches, and a re-run under the old titles would match the OLD takes instantly and return
 * without ever waiting for the new ones — ten Creates that all report success and are never
 * actually checked.
 *
 * v2 = the first set generated against the corrected lyrics. v1 inherited the source song's
 * older words and is superseded; it is left in the workspace rather than deleted, because
 * "the old lyrics sounded better here" is a finding we might yet want.
 *
 * Kept short and parenthesised: `listTakes` slices row titles at 48 characters, and its
 * `\s+v\d` splitter would eat a bare ` v2`.
 */
export const SET = ' (v4)'
// v3 = the lyric timing pass of 2026-08-25 (camping.md §4: `I want change...` + the performance cues).
// v4 = Kai's hand edit the same day: "pathetic" -> "it's pathetic", "sorroooooows," -> "sorrows," —
// a real word/spelling change, not just layout, so it earns its own suffix.
