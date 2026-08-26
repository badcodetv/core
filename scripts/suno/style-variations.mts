/**
 * The Camping STYLE set — ordinary Create mode, nothing attached, and EVERY input varying.
 *
 * ─────────────────────────────────────────────────────────────────────────────────────────────
 * WHY THIS IS NOT AN A/B, AND WHY THAT IS RIGHT THIS TIME
 *
 * `cover-variations.mts` moved one clause per round. That was correct while we were converging
 * on an accepted record, and it is wrong now: after fourteen rounds every take still sounds like
 * the same record, so the question is no longer "which clause wins" but "is there another record
 * in here at all". You cannot answer that by moving one clause. This is a SCOUTING round — all
 * five inputs move together, seven genuinely different records come back, and we give up
 * attribution to get range. Attribution comes back in the next round, on whatever survives.
 *
 * ─────────────────────────────────────────────────────────────────────────────────────────────
 * 🔴 THE THING THAT WAS ACTUALLY HOLDING EVERY ROUND IN PLACE
 *
 * `camping-cover.md` §7 blamed the resemblance on HEAD/TAIL and the unchanged words. It missed
 * the biggest one. `My Taste` is applied to EVERY generation, cannot be turned off, and ours
 * says, in these words:
 *
 *     "ranting and talking over the beat rather than singing"
 *     "half-shouting and half-muttering"
 *     "Ranted spoken word over sung melody, every time."
 *     "dark UK drum and bass and neurofunk at 174 BPM"
 *     "No orchestral instruments and no piano anywhere."
 *
 * So a Style box asking for a sung vocal was arguing with a global box that says ranted EVERY
 * TIME; an orchestral box was arguing with a global ban on orchestral instruments; and neurofunk
 * was never removed by taking it out of the Style box, because it was in two places. Three of
 * the seven variations would have been dead on arrival and we would have concluded the genres
 * did not work.
 *
 * 🔴 AND THE LYRIC CUES SAID IT AGAIN, SECTION BY SECTION
 *
 * The lyric block is the only SECTION-SCOPED box we have (camping.md §4f), and it carries
 * `gravelly ranting voice` four times, `[shouting]`, `[shout, full chest]`, `[shout, cracking,
 * begging]`, `the guitar drops out here`, `the same guitar riff returns underneath` and `neuro
 * bass growling underneath`. Inline and positional beats global, so those cues would have
 * overruled the Style box in exactly the sections we care about.
 *
 * Hence `cues` below. It rewrites the bracket lines and NEVER the words — `style-ab.mts` asserts
 * that, by stripping every `[...]` line from both and refusing to run if the lyrics differ.
 * camping.md §4 stays the source of truth for what is sung; this only changes how.
 *
 * ─────────────────────────────────────────────────────────────────────────────────────────────
 * The one input deliberately NOT varied is Duration, and that is evidence, not laziness: rounds
 * 13-14 targeted 200s and got 4:07-4:24 back, so the control is a suggestion Suno mostly ignores
 * and varying it would add noise without adding range. Pinned at 200 for all seven.
 */

/** Fills and register. Not under test — but no longer duplicating the amen cue in the lyrics. */
export const TAIL =
  ' Every four bars the drums tear into a chopped amen roll, snares tumbling over each other, ' +
  'loud up front. Grim and bitter, played straight, steady tempo.'

/** The accepted round-17 exclude list. Variations subtract from it, never add. */
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

/**
 * The two men are the one thing that never varies. Bob is weathered and northern-ish and broke;
 * Tarquin is plummy and comfortable. That is story canon, not style — a variation that collapses
 * them into one performer is not a different record, it is a different song.
 */

/**
 * Every substring below is an exact quote from a bracket line in camping.md §4. A variation
 * supplies replacements for the ones its world contradicts; anything it omits stays as written.
 * Keys are the sheet's own words so a drifting sheet fails loudly instead of silently no-opping
 * — `style-ab.mts` checks that every key it is asked to replace was actually found.
 */
export type CueMap = Record<string, string>

export interface Variation {
  id: string
  name: string
  /** One line: what this record is, and what it is escaping. */
  thesis: string
  /** Genre anchor. Front of the box — Suno weights the front hardest. */
  genre: string
  /** Casting and delivery. The clause that was pinned through all fourteen cover rounds. */
  voice: string
  /** The "Four steps" arrangement sentence. */
  middle: string
  /** The full My Taste replacement. Account-wide — style-ab.mts backs the house profile up first. */
  taste: string
  /** Section-scoped rewrites of the bracket cues. Words are never touched. */
  cues: CueMap
  lift: string[]
  liftWhy: string
  weirdness: number
  styleInfluence: number
}

/** Performance-cue rewrites shared by every variation that is not shouting its way through. */
const UNSHOUTED = (spoken: string, loud: string, cracked: string, held: string, sneer: string): CueMap => ({
  '[shout, full chest]': `[${loud}]`,
  '[shouting]': `[${spoken}]`,
  '[shout, cracking, begging]': `[${cracked}]`,
  '[change tone to spoken word]': `[${held}]`,
  '[mocking falsetto sneer]': `[${sneer}]`,
})

/** The dub + guitar arrangement Kai chose at round 11. The spine of the three voice probes. */
const DUB_GUITAR =
  'Four steps: one long low synth note; then the voice over a low palm-muted guitar riff with a ' +
  'chorus-pedal jangle over it, one short figure each, repeating, never a solo, never chords, ' +
  'under every vocal section, tape delay throwing every line end across the bar, spring reverb ' +
  'on the snare; then a dry chopped breakbeat, sub bass first, nothing else; then the drop, ' +
  'guitars out, kit at full weight, Reese sub and a screaming wavetable lead cut against it.'

/** The dub world's taste, shared by the four variations built on that spine. */
const DUB_TASTE = (vocals: string) =>
  `Vocals: ${vocals} Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: UK drum and bass at 174 BPM, minor key, mixed like a dub soundsystem. Sub bass first and loudest, everything else stripped back around it. Tape delay throwing the end of every vocal line across the bar, spring reverb on the snare, hand-swept filters. One low palm-muted electric guitar riff with a chorus-pedal jangle over it, repeating, never a solo. Dry chopped breakbeats and chopped amen rolls that tear across a whole bar every few bars, loud and right at the front, then straight back into the groove. Space used as an instrument: one sound at a time, nothing playing that does not need to.

Register: bleak, bitter and angry, played completely straight. Whatever is funny lives in the words alone — the music never winks.

Subject: British class, money, work, and the people the economy left behind.`

export const VARIATIONS: Variation[] = [
  {
    id: 'style-s1-metal',
    name: 'Metal',
    thesis:
      'Down-tuned high-gain guitars carry the whole record and STAY IN through the drop — metal and ' +
      'break as one piece, not a handover. A shout that is a rock shout, not an MC shout.',
    genre: 'Heavy metal crossed with UK drum and bass, 174 BPM, minor key —',
    voice:
      ' hoarse half-sung British rock vocal on top, snarled on a loose melody, never rapped. Verse ' +
      'one, a weathered British man in his fifties: low, gravelly, smoke-worn, cracked. Verse two, ' +
      'a well-spoken British man: higher, clean, plummy BBC English, from a wide room.',
    middle:
      'Four steps: one down-tuned guitar chord ringing out alone; then the voice over a down-tuned ' +
      'palm-muted high-gain metal riff, one short figure repeating, never a solo, never a chord ' +
      'progression, under every vocal section; then a dry chopped breakbeat under the vocal, no ' +
      'bass; then the drop, guitars staying in at full weight, power chords slamming on the ' +
      'downbeat against the kit, Reese sub and a screaming lead cut across it.',
    taste: `Vocals: hoarse half-sung British rock — two white British men in their late forties and fifties, snarling on a loose melody over the beat, never rapping and never chanting. They must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic. The other is higher, clean and plummy BBC English, from a wide room.

Music: heavy metal crossed with UK drum and bass at 174 BPM, minor key. Down-tuned palm-muted high-gain guitars running as a repeating riff under every vocal, never a solo. Dry chopped breakbeats and chopped amen rolls that tear across a whole bar every few bars, loud and right at the front. At the drop the guitars stay in and slam power chords with the kit, so guitars and break are one piece of music. Rolling Reese bass and deep sub underneath. Arrangements that climb in steps and hold their weight back until the drop.

Register: bleak, bitter and angry, played completely straight. Whatever is funny lives in the words alone — the music never winks.

Subject: British class, money, work, and the people the economy left behind.`,
    cues: {
      'gravelly ranting voice': 'hoarse half-sung rock voice',
      'well-spoken posh voice': 'clean high British rock voice',
      'one long low detuned synth note, completely alone, held and slowly filtering open':
        'one down-tuned guitar chord ringing out alone, held and slowly filtering open',
      'the low synth note holds underneath': 'the guitar chord rings out underneath',
      'no drums, no bass, no guitar': 'no drums, no bass, no synth',
      'the guitar drops out here': 'the guitars stay in and slam power chords with the kit',
      'the wavetable lead tears in over the break': 'the guitars scream over the break',
      'the same guitar riff returns underneath, unchanged': 'the same metal riff returns underneath, unchanged',
      'neuro bass growling underneath': 'the guitars heavier and more distorted underneath',
      'the guitar riff sparser and quieter here, still one repeating figure, never a tune':
        'the guitar palm-muted and quiet here, one repeating figure, never a tune',
      'voice, guitar and bass dissolve into static': 'voice, guitar and bass dissolve into feedback',
      '[change tone to spoken word]': '[half-sung, held]',
      '[mocking falsetto sneer]': '[high sneering rock falsetto]',
    },
    lift: ['power chords', 'live rock band', 'singing', 'melodic vocal', 'vocal melody'],
    liftWhy:
      '`guitar solo`, `lead guitar` and `shredding` stay banned — it is a riff, never a lead break. ' +
      'Three singing bans lifted because the delivery is half-sung; `autotune` and `harmonies` stay',
    weirdness: 55,
    styleInfluence: 80,
  },
  {
    id: 'style-s2-orchestral',
    name: 'Orchestral, sung',
    thesis:
      'The furthest point from anything we have made: a real tune, two unshowy sung voices, and an ' +
      'orchestra that plays THROUGH the drop instead of getting out of its way.',
    genre: 'Orchestral drum and bass, 174 BPM, minor key —',
    voice:
      ' sung British vocal on top, a real melody, weary and unshowy, no rapping anywhere. Verse one, ' +
      'a weathered British man in his fifties: low baritone, gravelly, smoke-worn, singing rough and ' +
      'flat. Verse two, a well-spoken British man: higher, clean, plummy BBC English, singing coldly.',
    middle:
      'Four steps: a cold string section and low brass alone, one bleak sustained figure; then the ' +
      'voice over that orchestra with a low palm-muted guitar riff underneath, one short figure each, ' +
      'repeating, never a solo, under every vocal section; then a dry chopped breakbeat under the ' +
      'vocal, no bass; then the drop, strings and horns staying in at full weight, guitar still ' +
      'riffing, Reese sub and a screaming lead cut across it.',
    taste: `Vocals: sung British male voices — two white British men in their late forties and fifties, singing a real melody, weary and unshowy, never rapping and never ranting. They must stay two different men. One is a low gravelly smoke-worn baritone singing rough and flat. The other is higher, clean and plummy BBC English, singing precisely and coldly.

Music: orchestral drum and bass at 174 BPM, minor key. A cold string section and low brass carrying the whole record, playing one bleak sustained figure and staying in at full weight through the drop, so orchestra and break are one piece of music. A low palm-muted electric guitar riff underneath, repeating, never a solo. Dry chopped breakbeats and chopped amen rolls that tear across a whole bar every few bars, loud and right at the front. Rolling Reese bass and deep sub. Bleak and cold, never triumphant, never cinematic.

Register: bleak, bitter and angry, played completely straight. Whatever is funny lives in the words alone — the music never winks.

Subject: British class, money, work, and the people the economy left behind.`,
    cues: {
      'gravelly ranting voice': 'weary sung baritone',
      'well-spoken posh voice': 'high clean sung voice',
      'one long low detuned synth note, completely alone, held and slowly filtering open':
        'a cold string section and low brass alone, one bleak sustained figure',
      'the low synth note holds underneath': 'the strings hold underneath',
      'no drums, no bass, no guitar': 'no drums, no bass, no synth',
      'the guitar drops out here': 'the orchestra stays in at full weight',
      'the wavetable lead tears in over the break': 'the horns tear in over the break',
      'the same guitar riff returns underneath, unchanged': 'the strings return underneath, unchanged',
      'neuro bass growling underneath': 'the whole orchestra heavier and more distorted',
      'the guitar riff sparser and quieter here, still one repeating figure, never a tune':
        'a single cello holding underneath, sparse and quiet, never a tune',
      ...UNSHOUTED(
        'sung loud and flat',
        'sung out, full chest',
        'sung cracking, begging',
        'held, one long sung note',
        'mocking falsetto, sung',
      ),
      '[whisper, conspiratorial]': '[almost whispered, sung under the breath]',
    },
    lift: [
      'orchestral strings', 'violins', 'cello', 'string section', 'brass band',
      'singing', 'sung verses', 'sung chorus', 'melodic vocal', 'vocal melody', 'vocal hooks',
      'crooning', 'clean sung melody', 'sustained vocal notes',
    ],
    liftWhy:
      'the whole point of this one is the two things the accepted list bans hardest. `epic trailer ' +
      'music`, `uplifting` and `major key` stay banned — those are what hold it back from Hollywood. ' +
      '`autotune`, `soprano`, `operatic vocals`, `vibrato`, `angelic voices`, `female vocal`, `choir`, `harmonies` and `pop` all stay',
    weirdness: 45,
    styleInfluence: 85,
  },
  {
    id: 'style-s3-blues',
    name: 'Blues',
    thesis:
      'Bottleneck slide and Hammond as the whole instrumental atmosphere around the words, at 174, ' +
      'with the slide staying in through the drop. A drawl instead of a rant.',
    genre: 'Electric blues crossed with UK drum and bass, 174 BPM, minor key —',
    voice:
      ' low drawled half-sung British vocal on top, behind the beat, never rapped. Verse one, a ' +
      'weathered British man in his fifties: low, gravelly, smoke-worn, drawling flat. Verse two, a ' +
      'well-spoken British man: higher, clean, clipped BBC English, half-sung and precise.',
    middle:
      'Four steps: one bottleneck slide figure alone on a humming valve amp; then the voice over a ' +
      'dirty electric blues guitar — bottleneck slide, minor pentatonic, valve amp on the edge of ' +
      'breakup, one short figure repeating, never a solo, under every vocal section, a Hammond organ ' +
      'holding underneath; then a dry chopped breakbeat under the vocal, no bass; then the drop, the ' +
      'slide staying in against the kit at full weight, Reese sub cut across it.',
    taste: `Vocals: low drawled half-sung British male voices — two white British men in their late forties and fifties, drawling behind the beat on a loose melody, never rapping and never ranting, and never American. They must stay two different men. One is low, gravelly and smoke-worn, drawling flat. The other is higher, clean and clipped BBC English, half-sung and precise.

Music: electric blues crossed with UK drum and bass at 174 BPM, minor key. A dirty bottleneck slide guitar in minor pentatonic on a valve amp at the edge of breakup, one short figure repeating under every vocal, never a solo. A Hammond organ holding long minor chords underneath. Dry chopped breakbeats and chopped amen rolls that tear across a whole bar every few bars, loud and right at the front. At the drop the slide stays in against the kit at full weight. Rolling Reese bass and deep sub. Grimy, hungover, British.

Register: bleak, bitter and angry, played completely straight. Whatever is funny lives in the words alone — the music never winks.

Subject: British class, money, work, and the people the economy left behind.`,
    cues: {
      'gravelly ranting voice': 'low drawling half-sung voice',
      'well-spoken posh voice': 'clipped half-sung English voice',
      'one long low detuned synth note, completely alone, held and slowly filtering open':
        'one bottleneck slide figure alone, a valve amp humming behind it',
      'the low synth note holds underneath': 'the valve amp hums underneath',
      'no drums, no bass, no guitar': 'no drums, no bass, no organ',
      'the guitar drops out here': 'the slide guitar stays in over the break',
      'the wavetable lead tears in over the break': 'the slide guitar tears in over the break',
      'the same guitar riff returns underneath, unchanged': 'the same slide figure returns underneath, unchanged',
      'neuro bass growling underneath': 'the organ and slide heavier and more distorted',
      'the guitar riff sparser and quieter here, still one repeating figure, never a tune':
        'the slide sparse and quiet here, one repeating figure, never a solo',
      ...UNSHOUTED(
        'half-sung, raised',
        'drawled hard, full chest',
        'half-sung, cracking, begging',
        'drawled, half-sung',
        'mocking falsetto drawl',
      ),
    },
    lift: ['wah', 'piano', 'singing', 'melodic vocal', 'vocal melody', 'crooning'],
    liftWhy:
      'Hammond reads as piano-family to the model (cover-05). `guitar solo`, `lead guitar` and ' +
      '`shredding` stay banned so the slide is a riff. 🔴 `American accent`, `American vocal` and ' +
      '`southern drawl` STAY BANNED — this is the one variation whose genre will pull the accent west',
    weirdness: 35,
    styleInfluence: 75,
  },
  {
    id: 'style-s4-dub',
    name: 'Dub + guitar (the control)',
    thesis:
      '🔴 THE CONTROL, and the most valuable take in the set. Round 11\'s winning arrangement, ' +
      'unchanged — but with no audio attached, the taste rewritten and the ranting cues gone. It is ' +
      'the only one that tells us how much of fourteen rounds of sameness was the globals, not the genre.',
    genre: 'Dub soundsystem drum and bass, 174 BPM, minor key —',
    voice:
      ' spoken British vocal on top, close-miked and conversational, phrased across the bar and ' +
      'never locked to the beat, low projection, never rapped. Verse one, a weathered British man in ' +
      'his fifties: low, gravelly, smoke-worn, bone dry. Verse two, a well-spoken British man: ' +
      'higher, clean, plummy BBC English, talking down from a wide room.',
    middle: DUB_GUITAR,
    taste: DUB_TASTE(
      'spoken British male voices, close-miked and conversational, phrased across the bar and never locked to the beat, low projection, never ranted and never rapped.',
    ),
    cues: {
      'gravelly ranting voice': 'gravelly spoken voice, conversational, never ranted',
      'neuro bass growling underneath': 'the sub bass growling underneath',
      ...UNSHOUTED(
        'raised, but still spoken',
        'spoken hard, full chest',
        'spoken cracking, begging',
        'slower, flatter, spoken',
        'mocking falsetto sneer',
      ),
    },
    lift: ['dub'],
    liftWhy: '`reggae`, `ska`, `ragga MC` and `Jamaican accent` stay banned — the mixing desk, not the genre',
    weirdness: 40,
    styleInfluence: 75,
  },
  {
    id: 'style-s5-halfsung',
    name: 'Dub, half-sung',
    thesis: 'The dub spine with sprechgesang. The halfway house off the rant — melody that keeps falling back into speech.',
    genre: 'Dub soundsystem drum and bass, 174 BPM, minor key —',
    voice:
      ' half-sung British vocal on top, sprechgesang, talk-sung on a loose weary melody that slides ' +
      'back into speech, never rapped. Verse one, a weathered British man in his fifties: low, ' +
      'gravelly, smoke-worn, singing flat and cracked. Verse two, a well-spoken British man: higher, ' +
      'clean, plummy BBC English, singing precisely from a wide room.',
    middle: DUB_GUITAR,
    taste: DUB_TASTE(
      'half-sung British male voices, sprechgesang, talk-sung on a loose weary melody that keeps sliding back into speech, never ranted and never rapped.',
    ),
    cues: {
      'gravelly ranting voice': 'gravelly half-sung voice, sprechgesang',
      'well-spoken posh voice': 'well-spoken posh voice, half-sung',
      'neuro bass growling underneath': 'the sub bass growling underneath',
      ...UNSHOUTED(
        'half-sung, raised',
        'half-sung out, full chest',
        'half-sung, cracking, begging',
        'talk-sung, held',
        'mocking falsetto, half-sung',
      ),
    },
    lift: ['dub', 'singing', 'sung verses', 'melodic vocal', 'vocal melody', 'clean sung melody'],
    liftWhy:
      'the accepted list bans singing six ways, so a half-sung ask would just regenerate the rant. ' +
      '`autotune`, `harmonies`, `vibrato`, `operatic vocals`, `choir` and `female vocal` all stay banned',
    weirdness: 50,
    styleInfluence: 70,
  },
  {
    id: 'style-s6-sung',
    name: 'Dub, fully sung',
    thesis:
      'The dub spine with a real tune. Pairs with S2: the same singing, one grand and cold, one ' +
      'intimate and stripped — so if singing works we learn which world it wants.',
    genre: 'Dub soundsystem drum and bass, 174 BPM, minor key —',
    voice:
      ' sung British vocal on top, a real melody, baritone, weary and unshowy, no rapping anywhere. ' +
      'Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, singing rough ' +
      'and flat. Verse two, a well-spoken British man: higher, clean, plummy BBC English, singing ' +
      'precisely and coldly from a wide room.',
    middle: DUB_GUITAR,
    taste: DUB_TASTE(
      'sung British male voices, a real melody, baritone, weary and unshowy, no rapping and no ranting anywhere on this record.',
    ),
    cues: {
      'gravelly ranting voice': 'weary sung baritone',
      'well-spoken posh voice': 'high clean sung voice',
      'neuro bass growling underneath': 'the sub bass growling underneath',
      ...UNSHOUTED(
        'sung loud and flat',
        'sung out, full chest',
        'sung cracking, begging',
        'held, one long sung note',
        'mocking falsetto, sung',
      ),
      '[whisper, conspiratorial]': '[almost whispered, sung under the breath]',
    },
    lift: [
      'dub', 'singing', 'sung verses', 'sung chorus', 'melodic vocal', 'vocal melody',
      'vocal hooks', 'crooning', 'clean sung melody', 'sustained vocal notes',
    ],
    liftWhy:
      'every singing ban lifted, because this variation IS singing. `autotune`, `harmonies`, ' +
      '`soprano`, `operatic vocals`, `vibrato`, `angelic voices`, `female vocal`, `choir` and `pop` stay banned',
    weirdness: 45,
    styleInfluence: 80,
  },
  {
    id: 'style-s7-halftime',
    name: 'Dub, half-time delivery',
    thesis:
      'Still spoken, but at half the beat\'s rate. Tests the diagnosis head-on: the MC read comes ' +
      'from syllables landing on a 174 grid, so take the grid away and change nothing else.',
    genre: 'Dub soundsystem drum and bass, 174 BPM, minor key —',
    voice:
      ' spoken vocal on top, delivered at half the speed of the beat, long vowels, dragging behind, ' +
      'one phrase every two bars, never rapped. Verse one, a weathered British man in his fifties: ' +
      'low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC ' +
      'English, talking down from a wide room.',
    middle: DUB_GUITAR.replace(
      'then a dry chopped breakbeat, sub bass first, nothing else;',
      'then a dry chopped breakbeat at full 174, sub bass first, nothing else;',
    ),
    taste: DUB_TASTE(
      'spoken British male voices delivered at half the speed of the beat — long vowels, dragging behind, one phrase every two bars, never ranted and never rapped, while the drums stay at full 174.',
    ),
    cues: {
      'gravelly ranting voice': 'gravelly spoken voice, half the speed of the beat',
      'well-spoken posh voice': 'well-spoken posh voice, half the speed of the beat',
      'neuro bass growling underneath': 'the sub bass growling underneath',
      'full-weight drum and bass carries straight on': 'full-weight drum and bass carries straight on at full 174',
      ...UNSHOUTED(
        'raised, but still spoken and slow',
        'spoken hard and slow, full chest',
        'spoken cracking, begging, slow',
        'slower still, flatter',
        'mocking falsetto sneer',
      ),
    },
    lift: ['half-time'],
    liftWhy:
      '🔴 the risky lift — `half-time` is banned precisely because it half-times the DRUMS. Only ' +
      'the vocal should slow, which is why the middle, the taste AND the verse-2 cue all say full 174. ' +
      'If the kit drags, this is why, and the answer is to say it a fourth time or drop this variation',
    weirdness: 30,
    styleInfluence: 85,
  },
]

/** Drop the lifted keywords out of the accepted list, leaving the commas tidy. */
export function excludeFor(v: Variation): string {
  return EXCLUDE_BASE.split(', ').filter((k) => !v.lift.includes(k)).join(', ')
}

export const styleFor = (v: Variation) => v.genre + v.voice + ' ' + v.middle + TAIL

/** Kept under 48 characters — `listTakes` slices row titles there. */
export const titleFor = (v: Variation) => `Camping ${v.id.slice(6, 8).toUpperCase()} ${v.name}${SET}`

/**
 * Which run of the set this is. `create()` waits for two takes whose title matches, so a re-run
 * under unchanged titles would match the OLD takes and report success without generating.
 * Bump on every lyric, cue or layout change. s1 = the first non-cover set, on camping.md §4 as of v6.
 */
export const SET = ' (s1)'
