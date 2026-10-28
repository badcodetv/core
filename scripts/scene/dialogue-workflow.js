export const meta = {
  name: 'dialogue-options',
  description: 'Ten writers each rewrite a scene\'s dialogue in one shape; one synthesis ranks them and writes three drafts per dialogue into options.json',
  whenToUse: 'scene-dialogue skill: options for one or more dialogues, to be picked on a dialogue page',
  phases: [
    { title: 'Shapes', detail: 'one writer per shape, all dialogues each', model: 'sonnet' },
    { title: 'Synthesis', detail: 'rank harshly, three combined drafts per dialogue, options.json', model: 'sonnet' },
  ],
}

// args: {
//   outdir:    'design/<date>-<story>-dialogue-<topic>'   (shape files and options.json land here)
//   title:     'GPOM dialogue options'                     (page heading)  · page_title: 'GPOM Dialogue Options'
//   brief:     the whole story-so-far + rules + what to read first, as one string
//   dialogues: [{ id:'d1', label, where, scene, target, now_from, now:[{who,line}], must, protected:[...] }]
//   shapes:    [['01-bone-dry', 'Bone-dry minimum: …'], …]   (default: the house ten, scene-dialogue skill)
// }
const A = args || {}
const OUT = A.outdir
if (!OUT || !A.brief || !(A.dialogues || []).length) throw new Error('args need outdir, brief and dialogues')

const SHAPES = A.shapes || [
  ['01-bone-dry', 'Bone-dry minimum: the fewest words that still carry every beat.'],
  ['02-picture-carries', 'The picture carries it: lean on what the audience has already seen and cut lines the images already say. Name any shot you rely on.'],
  ['03-plain-logic', 'The logic said plainly: a character reasons the argument out loud.'],
  ['04-comedy-first', 'Comedy first: bluntness and bad timing deliver the hard facts. The jokes carry the argument.'],
  ['05-other-side-wins', 'The other side wins: the resisting character sets the terms and the persuader concedes something.'],
  ['06-reversal', 'Reversal: the listener works out the point before the speaker can say it.'],
  ['07-chorus', 'The chorus: side characters voice the doubts, so the lead does not have to.'],
  ['08-place-is-argument', 'The place is the argument: one concrete detail of where they are makes the case.'],
  ['09-borrowed-craft', 'Borrowed craft: how great short films and TV compress exposition and persuasion (cite real examples briefly; NEVER invent quotes from them), applied here.'],
  ['10-ending-first', 'Ending first: write the last ten seconds so the next scene feels inevitable, then work backwards.'],
]

const DIAL = A.dialogues.map((d, i) => `DIALOGUE ${i + 1}: ${d.label} (${d.where}). TARGET: ${d.target}.
Current lines (from ${d.now_from}):
${d.now.map(l => `${l.who}: ${l.line}`).join('\n')}
It must: ${d.must}
${(d.protected || []).length ? 'Protected lines (keep verbatim if at all possible): ' + d.protected.map(p => `"${p}"`).join(' / ') : 'No protected lines.'}`).join('\n\n')

const BRIEF = `${A.brief}

Produce OPTIONS for the director to pick from. Do NOT edit any scene file, script or voice.

${DIAL}`

const RETURN = (file) => `WRITE ${file} in exactly this shape (the page builder splits on these headings):

# Shape <NN>: <your shape in a few words>

<one short paragraph: the approach you took, the same for every dialogue>

${A.dialogues.map((d, i) => `## Dialogue ${i + 1}: ${d.label}

- a table: Speaker | Line | Est. s, with a Total row;
- **Why it works.** one paragraph;
- **Cuts from current.** what goes;
- **Risk.** what could fail;
- **Protected lines.** which survive, and how if altered.`).join('\n\n')}

Push your shape to its extreme: the point is to find edges, not to be tasteful. Stage directions go in [square brackets] inside the line.
Then return the same markdown as your final text.`

phase('Shapes')
const results = await parallel(SHAPES.map(([key, shape]) => () =>
  agent(`${BRIEF}\n\nYOUR SHAPE: ${shape}\n\n${RETURN(`${OUT}/shape-${key}.md`)}`, { label: `shape:${key}`, phase: 'Shapes', model: 'sonnet' })
    .then(text => ({ key, shape, text }))))
const ok = results.filter(Boolean).filter(r => r.text)
log(`${ok.length}/${SHAPES.length} shapes returned`)

phase('Synthesis')
const bundle = ok.map(r => `## SHAPE ${r.key}: ${r.shape}\n\n${r.text}`).join('\n\n---\n\n')
const synth = await agent(`${BRIEF}

You are the SYNTHESIS writer. Below are ${ok.length} independent rewrites, each pushing one shape to its extreme, saved as ${OUT}/shape-<key>.md. First check every one of those files exists and starts "# Shape"; if one is missing, write it from that writer's text below.

1. Rank them HARSHLY, separately for each dialogue, against: the target length, whether the point lands without being stated, real resistance from whoever resists, character voices, no moral spoken aloud. Name what fails.
2. Write THREE combined drafts per dialogue, genuinely different from each other, each with a one-line bet (what it is betting on). Tag each line with the shape(s) it came from ("09"), "Kai" for a protected line, "all" for a line every shape kept. Estimated seconds per line and a total.
3. Under each draft, short notes: trims, protected lines kept, risks.
4. At most five open questions for the director.

Write ${OUT}/options.json (UTF-8, indent 1) in exactly this form, then return "done" and the drafts' names:
{"page_title": ${JSON.stringify(A.page_title || 'Dialogue Options')}, "title": ${JSON.stringify(A.title || 'Dialogue options')},
 "about": "<two sentences: what this page is and that nothing has changed yet>",
 "shapes": [{"id": "<NN>", "name": "<shape in 2-3 words>", "title": "<the file's # Shape heading without 'Shape NN: '>", "file": "${OUT}/shape-<key>.md"}],
 "dialogues": [{"id", "label", "where", "scene", "target", "now_from", "now": [{"who", "line"}]   (copy these from the brief),
   "drafts": [{"id": "1A", "name", "length": "about 19 s", "total": "~19 s", "bet", "lines": [{"who", "line", "tags": ["09"], "s": "2.5"}], "notes": ["…"]}],
   "ranking": [{"rank": 1, "shape": "<NN>", "length": "~16 s", "verdict": "…"}],
   "protected": {"columns": ["<each protected line, short>"], "rows": {"2A": ["verbatim", …]}}   (only where the dialogue has protected lines)}],
 "questions": [{"id": "q1", "text": "…"}]}
Draft ids are the dialogue number plus A, B, C. Do not change any scene file, script or voice.

${bundle}`, { label: 'synthesis', phase: 'Synthesis', model: 'sonnet' })

return { shapes: ok.map(r => r.key), missing: SHAPES.map(s => s[0]).filter(k => !ok.find(r => r.key === k)), synthesis: synth }
