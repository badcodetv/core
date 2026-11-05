export const meta = {
  name: 'news-sweep',
  description: "The BadCode government's daily news sweep: 24 researchers, one per beat, then one merge that dedupes and labels the day's news for the cabinet",
  whenToUse: 'Run by the news-gatherer worker once a day with args {date: "YYYY-MM-DD"}. Returns the merged list; it writes no memories.',
  phases: [
    { title: 'Research', detail: '24 Sonnet researchers, one per beat, at most 6 web searches each' },
    { title: 'Merge', detail: 'one agent dedupes across beats and returns the final list' },
  ],
}

// ---------------------------------------------------------------------------
// The contract (docs/government/README.md, "Memory label scheme"). Keep these
// lists identical to the plan: the gatherer turns each returned item into one
// kind=news memory with these values as labels.
// ---------------------------------------------------------------------------

const POSTS = [
  'prime-minister', 'chancellor', 'foreign', 'home', 'education',
  'defence', 'health', 'work-pensions', 'housing', 'energy-climate',
]

const TOPICS = [
  'economy', 'work', 'welfare', 'housing', 'health', 'education',
  'crime-justice', 'migration', 'foreign', 'defence', 'energy-climate', 'tech-ai',
]

// The 24 beats. `posts` is a starting suggestion for which ministers usually
// care (the researcher may add or drop posts per item).
const BEATS = [
  { beat: 'UK economy and cost of living', region: 'uk', posts: ['chancellor', 'work-pensions'] },
  { beat: 'UK jobs and wages', region: 'uk', posts: ['work-pensions', 'chancellor'] },
  { beat: 'UK welfare and pensions', region: 'uk', posts: ['work-pensions', 'chancellor'] },
  { beat: 'UK housing and rents', region: 'uk', posts: ['housing'] },
  { beat: 'NHS and care', region: 'uk', posts: ['health'] },
  { beat: 'UK schools and universities', region: 'uk', posts: ['education'] },
  { beat: 'UK crime and courts', region: 'uk', posts: ['home'] },
  { beat: 'UK migration and asylum', region: 'uk', posts: ['home'] },
  { beat: 'UK energy bills', region: 'uk', posts: ['energy-climate', 'chancellor'] },
  { beat: 'climate and weather', region: 'world', posts: ['energy-climate'] },
  { beat: 'UK politics and Parliament', region: 'uk', posts: ['prime-minister'] },
  { beat: 'UK local government', region: 'uk', posts: ['housing', 'prime-minister'] },
  { beat: 'AI and automation', region: 'world', posts: ['work-pensions', 'chancellor'] },
  { beat: 'big business and markets', region: 'world', posts: ['chancellor'] },
  { beat: 'tax and public finances', region: 'uk', posts: ['chancellor'] },
  { beat: 'US', region: 'world', posts: ['foreign'] },
  { beat: 'EU and Europe', region: 'world', posts: ['foreign'] },
  { beat: 'Russia and Ukraine', region: 'world', posts: ['foreign', 'defence'] },
  { beat: 'Middle East', region: 'world', posts: ['foreign', 'defence'] },
  { beat: 'China and Asia-Pacific', region: 'world', posts: ['foreign'] },
  { beat: 'Africa and Latin America', region: 'world', posts: ['foreign'] },
  { beat: 'defence and security', region: 'world', posts: ['defence'] },
  { beat: 'global trade and supply chains', region: 'world', posts: ['chancellor', 'foreign'] },
  { beat: 'science and technology', region: 'world', posts: ['work-pensions', 'chancellor'] },
]

const ITEM = {
  type: 'object',
  properties: {
    headline: { type: 'string', description: 'One plain line, factual, no spin' },
    summary: { type: 'string', description: '3-5 sentences of what happened, only facts the sources state' },
    why_uk: { type: 'string', description: 'One or two sentences: why this matters to people in the UK' },
    sources: { type: 'array', items: { type: 'string' }, minItems: 1, description: 'Full https URLs of the articles read' },
    region: { type: 'string', enum: ['uk', 'world'] },
    topic: { type: 'string', enum: TOPICS },
    weight: { type: 'integer', enum: [1, 2, 3], description: '3 = a big story most of the cabinet should hear about; 1 = minor' },
    posts: { type: 'array', items: { type: 'string', enum: POSTS }, minItems: 1 },
  },
  required: ['headline', 'summary', 'why_uk', 'sources', 'region', 'topic', 'weight', 'posts'],
}

const ITEMS_SCHEMA = {
  type: 'object',
  properties: { items: { type: 'array', items: ITEM } },
  required: ['items'],
}

const date = args && typeof args.date === 'string' ? args.date : null
if (!date || !/^\d{4}-\d{2}-\d{2}$/.test(date)) {
  throw new Error('news-sweep needs args.date as "YYYY-MM-DD" (scripts cannot read the clock)')
}

const RULES = `Rules for every item:
- UK news first. A world story is in only for its effect on the UK; say that effect in why_uk.
- Only facts your sources state. No invented numbers, quotes or names. Name real people only for their public acts.
- sources: full https URLs of articles you actually opened or saw in results, at least one; weight 3 needs at least two independent outlets.
- topic is exactly one of: ${TOPICS.join(', ')}.
- posts are the ministers it concerns, from: ${POSTS.join(', ')}. Anything about AI or automation always includes work-pensions and chancellor (there is no technology minister).
- weight: 3 = a big story the whole cabinet should know; 2 = a solid story for its ministers; 1 = minor but worth a line.
- Neutral, plain wording in headline and summary: the ministers bring the opinions, not you.`

// ---------------------------------------------------------------------------
// Research: one researcher per beat, all at once. The merge needs every
// beat's items together to dedupe, so this is a genuine barrier.
// ---------------------------------------------------------------------------

phase('Research')
log(`Sweeping ${BEATS.length} beats for ${date} (at most 6 web searches each, about ${BEATS.length * 6} in all)`)

const results = await parallel(BEATS.map((b, i) => () => agent(
  `You are a news researcher for the BadCode government, a UK cabinet. Today is ${date}.
Your beat: **${b.beat}** (${b.region === 'uk' ? 'UK news' : 'world news, for its effect on the UK'}).
Ministers who usually care: ${b.posts.join(', ')}.

Find the news on your beat from the last 48 hours (published on ${date} or the two days before).

How to work (search results alone have no dates, so you must open pages):
1. Start by OPENING a dated news page with WebFetch: a section front for your beat (for example bbc.co.uk/news/<section>, theguardian.com/<section>, gov.uk/search/news-and-communications, a wire such as apnews.com or reuters.com) or the articles your searches find. Article pages and section fronts carry dates; search snippets do not.
2. Use WebSearch (HARD LIMIT: at most 6 searches in total, count them; the whole sweep shares one budget) to find the stories, then WebFetch the 2 to 6 most promising articles to confirm what happened and when. WebFetch does not count against the search limit, but keep it to about 8 pages.
3. A story counts if its newest development is in the window, even when the story itself is older (a vote today on a bill from last month counts).

You may return an empty list ONLY after you have opened at least three dated pages and found nothing in the window; never return empty because the search snippets lacked dates.
Do not write any files and do not call any memory or Bob tools: just return the items.

Return the 2 to 5 most important stories on your beat (fewer only if the beat is genuinely quiet). Skip opinion pieces and live blogs with no news.

${RULES}`,
  { label: `beat ${i + 1}: ${b.beat}`, phase: 'Research', model: 'sonnet', schema: ITEMS_SCHEMA },
)))

const gathered = []
const failed = []
results.forEach((r, i) => {
  if (!r || !Array.isArray(r.items)) { failed.push(BEATS[i].beat); return }
  r.items.forEach(item => gathered.push({ ...item, beat: BEATS[i].beat }))
})
if (failed.length) log(`No result from ${failed.length} beat(s): ${failed.join('; ')}`)
log(`${gathered.length} raw items from ${BEATS.length - failed.length} beats`)

// ---------------------------------------------------------------------------
// Plain-code clean-up, used on both the merge output and the fallback.
// ---------------------------------------------------------------------------

function normalise(item) {
  if (!item || typeof item.headline !== 'string' || !item.headline.trim()) return null
  const sources = (Array.isArray(item.sources) ? item.sources : [])
    .filter(s => typeof s === 'string' && /^https?:\/\//.test(s.trim()))
    .map(s => s.trim())
  const uniqueSources = sources.filter((s, i) => sources.indexOf(s) === i)
  if (!uniqueSources.length) return null // no source, no item
  const topic = TOPICS.includes(item.topic) ? item.topic : null
  if (!topic) return null
  const posts = (Array.isArray(item.posts) ? item.posts : []).filter(p => POSTS.includes(p))
  if (topic === 'tech-ai') posts.push('work-pensions', 'chancellor')
  const uniquePosts = posts.filter((p, i) => posts.indexOf(p) === i)
  if (!uniquePosts.length) return null
  let weight = [1, 2, 3].includes(item.weight) ? item.weight : 1
  if (weight === 3 && uniqueSources.length < 2) weight = 2 // weight 3 needs two sources
  return {
    headline: item.headline.trim(),
    summary: String(item.summary || '').trim(),
    why_uk: String(item.why_uk || '').trim(),
    sources: uniqueSources,
    region: item.region === 'uk' ? 'uk' : 'world',
    topic,
    weight,
    posts: uniquePosts,
  }
}

function headlineKey(h) {
  return h.toLowerCase().replace(/[^a-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim()
}

function codeDedupe(items) {
  // Same headline -> one item: union of sources and posts, the higher weight.
  const byKey = new Map()
  for (const it of items) {
    const k = headlineKey(it.headline)
    const prev = byKey.get(k)
    if (!prev) { byKey.set(k, { ...it, sources: it.sources.slice(), posts: it.posts.slice() }); continue }
    it.sources.forEach(s => { if (!prev.sources.includes(s)) prev.sources.push(s) })
    it.posts.forEach(p => { if (!prev.posts.includes(p)) prev.posts.push(p) })
    prev.weight = Math.max(prev.weight, it.weight)
  }
  return Array.from(byKey.values())
}

function order(items) {
  // UK first, then by weight, heaviest first.
  return items.slice().sort((a, b) =>
    (a.region === b.region ? 0 : a.region === 'uk' ? -1 : 1) || b.weight - a.weight)
}

const cleanedRaw = gathered.map(normalise).filter(Boolean)
if (!cleanedRaw.length) {
  log('Nothing usable came back from the researchers')
  return { date, items: [], raw_count: gathered.length, failed_beats: failed, merged_by: 'none' }
}

// ---------------------------------------------------------------------------
// Merge: one agent sees every beat's items, folds duplicates into one item
// (union of sources and posts, the higher weight) and returns the final list.
// ---------------------------------------------------------------------------

phase('Merge')

const merged = await agent(
  `You are the merge editor for the BadCode government's daily news sweep, ${date}.
Below are ${cleanedRaw.length} items from ${BEATS.length} beat researchers, as JSON. Different beats often found the same story.

Do this, and nothing else (no web searches, no files, no memory tools):
1. Fold items that report the same event into ONE item: keep the clearest headline, write one summary of 3-5 sentences using only facts already in the items, keep the union of their sources and posts, and the highest weight.
2. Drop anything that is not news from the last two days, has no source URL, or is opinion.
3. Do not add facts, numbers, quotes or URLs that are not in the input. Do not drop a source URL from an item you keep.
4. Re-check each item's topic and posts against the rules, and keep the region honest.
5. Return every surviving item, UK items first, then heaviest first. Expect roughly 30-60.

${RULES}

ITEMS:
${JSON.stringify(cleanedRaw.map(({ beat, ...rest }) => rest))}`,
  { label: 'merge and dedupe', phase: 'Merge', model: 'sonnet', schema: ITEMS_SCHEMA },
)

let finalItems
let mergedBy
if (merged && Array.isArray(merged.items) && merged.items.length) {
  finalItems = order(codeDedupe(merged.items.map(normalise).filter(Boolean)))
  mergedBy = 'agent'
} else {
  log('Merge agent returned nothing: falling back to exact-headline dedupe in code')
  finalItems = order(codeDedupe(cleanedRaw))
  mergedBy = 'code'
}

log(`${finalItems.length} items after merge (${finalItems.filter(i => i.region === 'uk').length} UK, ${finalItems.filter(i => i.weight === 3).length} weight 3)`)

return {
  date,
  items: finalItems,
  raw_count: gathered.length,
  failed_beats: failed,
  merged_by: mergedBy,
}
