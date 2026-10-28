// Usage: npx tsx packages/flow-mcp/src/smoke-characters-rebuilt.ts <stage> [args]
// Live proof for Characters on the rebuilt Flow (flow.google.com), mapped 2026-10-17.
// Stages (run against FLOW_SMOKE_PROJECT, or whatever project is open):
//   create <name> <portrait.jpg> [body.jpg] [info]   — make a Character (0 credits: uploads only)
//   body <name> <body.jpg> [out.jpg]                 — add a Body to an existing Character (0 credits)
//   info <name> <text>                               — set the Character info note, then read it back
//   list                                              — { name, id }[]
//   get <name> <outDir>                               — info + hasBody, harvest portrait/body
//   cast <name> <out.jpg> <prompt>                    — one Nano Banana 2 still with the Character cast
//   castedit <name> <ref.jpg> <out.jpg> <prompt>      — a reference image AND the Character
import { FlowClient } from './flow-client'

const [stage = 'list', ...args] = process.argv.slice(2)
const c = await FlowClient.connect()
try {
  if (process.env.FLOW_SMOKE_PROJECT) await c.openProject({ id: process.env.FLOW_SMOKE_PROJECT })
  if (stage === 'create') {
    const [name, portrait, body, info] = args
    console.log(await c.createCharacter(name!, [portrait!], { ...(body ? { bodyImage: body } : {}), ...(info ? { info } : {}) }))
  }
  if (stage === 'body') {
    const [name, body, out] = args
    console.log(await c.createCharacterBody(name!, 'full body', { bodyImage: body!, ...(out ? { outPath: out } : {}) }))
  }
  if (stage === 'info') {
    const [name, info] = args
    console.log(await c.setCharacterInfo(name!, info!))
    console.log(await c.getCharacter(name!))
  }
  if (stage === 'list') console.log(await c.listCharacters())
  if (stage === 'get') {
    const [name, dir] = args
    console.log(await c.getCharacter(name!, { portraitOutPath: `${dir}/portrait.jpg`, bodyOutPath: `${dir}/body.jpg` }))
  }
  if (stage === 'cast') {
    const [name, out, prompt] = args
    console.log(await c.generateImage(prompt!, out!, { character: name!, model: 'Nano Banana 2', aspect: '16:9', numOutputs: 1 }))
  }
  if (stage === 'castedit') {
    const [name, ref, out, prompt] = args
    console.log(await c.editImage(prompt!, [ref!], out!, { character: name!, model: 'Nano Banana 2', aspect: '16:9', numOutputs: 1 }))
  }
} finally {
  await c.close?.()
}
