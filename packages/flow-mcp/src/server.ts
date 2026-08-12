import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
import { z } from 'zod'
import { NAME, VERSION } from './version'
import { FlowClient } from './flow-client'
import { ok, fail, NOT_RUNNING_HINT, type ToolResult } from './result'

/**
 * Cache the CDP attachment across tool calls: the stdio server process is long-lived, and
 * keeping the same Page preserves image-mode state and Flow's in-session context between
 * edit-loop rounds (as well as saving the attach + page discovery per call). A dead handle
 * (user restarted Chrome) is detected via isAlive() and retried once with a fresh connect;
 * close() on a connectOverCDP browser only detaches — it never kills the user's Chrome.
 */
let cached: FlowClient | null = null
const DISCONNECTED_RE = /Target closed|browser has been closed|Target page, context or browser has been closed|ECONNRESET/i

async function withClient<T>(fn: (c: FlowClient) => Promise<T>): Promise<T> {
  for (let attempt = 0; attempt < 2; attempt++) {
    if (cached && !cached.isAlive()) {
      await cached.close().catch(() => {})
      cached = null
    }
    cached ??= await FlowClient.connect()
    try {
      return await fn(cached)
    } catch (err) {
      const msg = err instanceof Error ? err.message : String(err)
      if (attempt === 0 && DISCONNECTED_RE.test(msg)) {
        await cached.close().catch(() => {})
        cached = null
        continue
      }
      throw err
    }
  }
  throw new Error('unreachable')
}

function toToolError(err: unknown): ToolResult {
  const msg = err instanceof Error ? err.message : String(err)
  if (msg.includes('ECONNREFUSED') || msg === 'NO_CONTEXT') {
    return fail('NOT_RUNNING', 'Could not attach to Chrome on the CDP port.', NOT_RUNNING_HINT)
  }
  if (msg === 'TIMEOUT') return fail('TIMEOUT', 'Flow did not finish generating in time.')
  if (msg === 'PROJECT_NOT_FOUND') return fail('PROJECT_NOT_FOUND', 'No Flow project with that name.', 'Check the name in the Flow projects list, or use flow_list_projects/flow_open_project with id instead — name matching fails on a tile with no <a href>.')
  if (msg === 'PROJECT_ID_OR_NAME_REQUIRED') return fail('INVALID_ARGS', 'Provide id or name.', 'flow_list_projects returns id when derivable.')
  if (msg === 'CHARACTER_NOT_FOUND') return fail('CHARACTER_NOT_FOUND', 'No Character with that name in the open project.', 'Check the Characters tab; names are case-sensitive.')
  if (msg === 'BODY_EXISTS') return fail('BODY_EXISTS', 'That character already has a Body view.', 'Use flow_edit_character with target "body" to change it.')
  if (msg === 'NO_BODY') return fail('NO_BODY', 'That character has no Body view yet.', 'Create one with flow_character_body first.')
  if (msg === 'NO_PORTRAIT') return fail('NO_PORTRAIT', 'That character has no Portrait view.', 'Every character gets a Portrait from its founding reference image — this usually means the name resolved to the wrong character, or the editor failed to render before the tab was queried. Re-check the name with flow_list_characters.')
  if (msg === 'MEDIA_NOT_FOUND') return fail('MEDIA_NOT_FOUND', 'No project media matches that title.', 'Use the exact accessible name shown in the project gallery, not a file path or media id.')
  if (msg === 'ANIMATE_NOT_FOUND') return fail('ANIMATE_NOT_FOUND', 'No project media tile offered the Animate action.', 'The source still may not have finished uploading, or the tile is a video (whose menu has no Animate).')
  if (msg === 'SUBMIT_FAILED') return fail('SUBMIT_FAILED', 'The prompt was typed but Flow never accepted the submit.', 'Usually a wedged compose bar — reload the project URL (twice; the first load can throw a client-side exception) and retry.')
  if (msg === 'NOT_IN_PROJECT') return fail('NOT_IN_PROJECT', 'The page is not inside a Flow project.', 'Open one with flow_open_project, or pass a project id.')
  if (msg === 'POLICY_BLOCKED') return fail('POLICY_BLOCKED', 'Flow flagged this generation as a possible policy violation — it will never complete no matter how long you wait.', 'Do NOT retry the same prompt. Rewrite it: check the reference image and any Character name/info fields, not just the prompt text (docs/flow/failure-modes.md §A2), then use the trigger list and rewrite table at docs/flow/failure-modes.md §A5-A6.')
  return fail('FLOW_ERROR', msg)
}

/**
 * Flow's documented image aspect ratios (docs/flow/image-prompting.md §9), Nano Banana 2's
 * extras included. Selector-confirmed against the live tab list (flow-selectors.md:172-174)
 * for exactly two: "16:9" and "4:3". The rest are wired through the identical `ensureImageMode`
 * tab-matching path (which needs no icon-name knowledge, just the ratio text) but are UNTESTED
 * against the real DOM — flag any failures for Wave B live validation.
 */
const IMAGE_ASPECTS = [
  '1:1', '3:2', '2:3', '3:4', '4:3', '4:5', '5:4', '9:16', '16:9', '21:9', '1:4', '4:1', '1:8', '8:1',
] as const

const IMAGE_MODEL_DESC =
  'Override the image model for this call only (defaults to "Nano Banana Pro"). Recorded tiers, ' +
  'sharpest first: "Nano Banana Pro", "Nano Banana 2", "Nano Banana 2 Lite". Per docs/flow/README.md ' +
  'rule 5 ("iterate on the cheap tier, spend on the locked shot"), prefer Lite while iterating on a ' +
  'prompt and switch to Pro only for the generation you intend to keep.'

const IMAGE_ASPECT_DESC =
  'Override the output aspect ratio for this call only. Omitting it leaves the project\'s current ' +
  'aspect untouched (Flow\'s own default is "16:9", and unlike video there is no reset-per-project ' +
  'landmine here, so there is nothing to assert when this is omitted). Selector-confirmed: "16:9" and ' +
  '"4:3"; the remaining values in the list are Flow-documented ratios wired through the same tab-click ' +
  'path but not yet live-validated.'

const server = new McpServer({ name: NAME, version: VERSION })

server.registerTool(
  'flow_status',
  {
    title: 'Flow status',
    description: 'Check whether the Flow browser is attached and logged in.',
    inputSchema: {},
  },
  async () => {
    try {
      return await withClient(async (c) => ok(await c.status()))
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_open_project',
  {
    title: 'Open project',
    description:
      'Open an existing Flow project. Pass id OR name (at least one is required; id wins if both are given). ' +
      'Prefer id when you have it: it navigates straight to `/project/<id>`, sidestepping the projects grid entirely — ' +
      'the robust option, and the only reliable one when a tile has lost its clickable <a href> (a known, recorded ' +
      'Flow bug; flow_list_projects returns such a tile with name but no id, for exactly this reason, so id is not ' +
      'always obtainable — get it from flow_create_project at creation time, or from the Flow URL bar). ' +
      'name matches a tile\'s visible title exactly (case-insensitive) by scanning the projects grid; it fails with ' +
      'PROJECT_NOT_FOUND on an href-less tile even though the project exists and is healthy — switch to id in that case.',
    inputSchema: { name: z.string().min(1).optional(), id: z.string().min(1).optional() },
  },
  async ({ name, id }) => {
    if (!name && !id) {
      return fail('INVALID_ARGS', 'Provide id or name.', 'flow_list_projects returns id when derivable; id is the reliable path when a tile has no <a href>.')
    }
    try {
      return await withClient(async (c) => {
        await c.openProject({ ...(id ? { id } : {}), ...(name ? { name } : {}) })
        return ok(await c.status())
      })
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_list_projects',
  {
    title: 'List Flow projects',
    description:
      'List every project tile on the Flow projects grid: { name, id?, href? }[]. Use this to find a project id for ' +
      'flow_open_project (the reliable re-open path) or to discover what already exists before flow_create_project. ' +
      "id is derived from the tile's href and omitted when it cannot be derived. This is the known, recorded " +
      'Flow bug where a project tile renders without a clickable <a href> at all — that tile still ships with its ' +
      'name so the list stays useful, but you cannot open it by id (fall back to flow_open_project with name, which ' +
      'itself will fail PROJECT_NOT_FOUND on the same tile — re-navigate to the project by URL from browser history ' +
      'instead if you have it). A partial list is returned rather than an error.',
    inputSchema: {},
  },
  async () => {
    try {
      return await withClient(async (c) => ok(await c.listProjects()))
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_create_project',
  {
    title: 'Create a new Flow project',
    description:
      'Create a brand-new Flow project via the "New project" button. Returns the ACTUAL { id, name } — id is reliable ' +
      '(read from the resulting /project/<id> URL), but name is BEST-EFFORT: naming a Flow project via its title ' +
      'textbox is documented as un-automatable (a fill and a keystroke attempt both revert on blur), so this tool ' +
      'attempts the rename you asked for, then reads back and returns whatever the project is ACTUALLY called — ' +
      'which may still be "Untitled Project" or similar. Callers MUST use the returned name, never assume the ' +
      'requested one stuck. Ends with the new project open, ready for a generation call.',
    inputSchema: { name: z.string().min(1).optional() },
  },
  async ({ name }) => {
    try {
      return await withClient(async (c) => ok(await c.createProject(name)))
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_generate_image',
  {
    title: 'Generate image',
    description:
      'Generate an image in Flow from a prompt and save it to outPath (absolute). Pass character to cast a project Character (created via flow_create_character) for cross-slide consistency. numOutputs (1-4, default 1) generates variants in one turn, saved with -a/-b… suffixes and returned as candidates[]. ' +
      IMAGE_MODEL_DESC +
      ' ' +
      IMAGE_ASPECT_DESC +
      ' Returns { path, mediaId, width, height }.',
    inputSchema: {
      prompt: z.string().min(1),
      outPath: z.string().min(1),
      character: z.string().min(1).optional(),
      numOutputs: z.number().int().min(1).max(4).optional(),
      model: z.string().min(1).optional(),
      aspect: z.enum(IMAGE_ASPECTS).optional(),
    },
  },
  async ({ prompt, outPath, character, numOutputs, model, aspect }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.generateImage(prompt, outPath, {
            ...(character ? { character } : {}),
            ...(numOutputs ? { numOutputs } : {}),
            ...(model ? { model } : {}),
            ...(aspect ? { aspect } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_edit_image',
  {
    title: 'Edit image with reference',
    description:
      'Generate edited variant(s) of an existing image: uploads referenceImages (absolute local paths) as prompt ingredients, applies the delta prompt, and saves numOutputs (default 2) candidates to outPath with -a/-b… suffixes. Reference the ORIGINAL/golden image, not a previous edit output — chained edits accumulate artifacts. Phrase the prompt as: "Using the provided image, change only <X> to <Y>. Keep everything else in the image exactly the same, preserving the original style, lighting, and composition." ' +
      IMAGE_MODEL_DESC +
      ' ' +
      IMAGE_ASPECT_DESC +
      ' Returns { candidates: [{ path, mediaId, width, height }], partial? }.',
    inputSchema: {
      prompt: z.string().min(1),
      referenceImages: z.array(z.string().min(1)).min(1).max(3),
      outPath: z.string().min(1),
      numOutputs: z.number().int().min(1).max(4).optional(),
      character: z.string().min(1).optional(),
      model: z.string().min(1).optional(),
      aspect: z.enum(IMAGE_ASPECTS).optional(),
    },
  },
  async ({ prompt, referenceImages, outPath, numOutputs, character, model, aspect }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.editImage(prompt, referenceImages, outPath, {
            ...(numOutputs ? { numOutputs } : {}),
            ...(character ? { character } : {}),
            ...(model ? { model } : {}),
            ...(aspect ? { aspect } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_refine',
  {
    title: 'Refine last image',
    description:
      'Send a follow-up correction in the SAME Flow session and save the new image to outPath. Relies entirely on the ' +
      "session's existing state (project, canvas, compose bar) — it does not re-open or re-navigate anything, which is " +
      'what makes it cheap in a tight edit loop. model/aspect are optional and, when BOTH are omitted (the normal case), ' +
      'change nothing about that: no mode assertion runs at all, identical to calling this tool with no such params. ' +
      'Pass either one only when you deliberately want to switch tier or aspect for this follow-up turn — ' +
      IMAGE_MODEL_DESC +
      ' ' +
      IMAGE_ASPECT_DESC +
      ' Returns { path, mediaId }.',
    inputSchema: {
      prompt: z.string().min(1),
      outPath: z.string().min(1),
      model: z.string().min(1).optional(),
      aspect: z.enum(IMAGE_ASPECTS).optional(),
    },
  },
  async ({ prompt, outPath, model, aspect }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.refine(prompt, outPath, {
            ...(model ? { model } : {}),
            ...(aspect ? { aspect } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_generate_video',
  {
    title: 'Generate video',
    description:
      'Animate an image (image→video / Veo). Uploads imagePath, applies the motion prompt, saves the .mp4 to outPath. ' +
      'Asserts the Settings-panel video defaults (model, aspect, output count) before generating — they live on the ' +
      "project and RESET to Omni Flash on a fresh project, so this call always sets them rather than trusting whatever " +
      'was last selected. model defaults to "Veo 3.1 Fast" (20 credits/clip) when omitted — a deliberate middle tier, ' +
      'not the cheapest and not the most expensive. Other recorded options: "Omni Flash", "Veo 3.1 Lite" (10 credits), ' +
      '"Veo 3.1 Quality" (100 credits — ask for this explicitly; it costs 5x Fast and 10x Lite), ' +
      '"Veo 3.1 Lite[Lower Priority]". aspect defaults to "16:9" (matches most comic pages); pass "9:16" for portrait. ' +
      'count (1-4, default 1) sets how many candidate clips Flow generates in this turn. Returns { path, mediaId }.',
    inputSchema: {
      imagePath: z.string().min(1),
      motion: z.string().min(1),
      model: z.string().optional(),
      aspect: z.enum(['16:9', '9:16']).optional(),
      count: z.number().int().min(1).max(4).optional(),
      outPath: z.string().min(1),
    },
  },
  async ({ imagePath, motion, model, aspect, count, outPath }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.generateVideo(imagePath, motion, outPath, {
            ...(model ? { model } : {}),
            ...(aspect ? { aspect } : {}),
            ...(count ? { count } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_generate_batch',
  {
    title: 'Generate image batch',
    description:
      'Generate N images sequentially in ONE Flow session from an ordered list of prompts. Saves <outDir>/<NN>.jpg per slide. Returns BatchItem[]. Use after planning all slide prompts up front. model/aspect apply to the WHOLE batch (asserted once before the first prompt, not re-asserted per prompt). ' +
      IMAGE_MODEL_DESC +
      ' ' +
      IMAGE_ASPECT_DESC,
    inputSchema: {
      prompts: z.array(z.string().min(1)).min(1).max(8),
      outDir: z.string().min(1),
      model: z.string().min(1).optional(),
      aspect: z.enum(IMAGE_ASPECTS).optional(),
    },
  },
  async ({ prompts, outDir, model, aspect }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.generateBatch(prompts, outDir, {
            ...(model ? { model } : {}),
            ...(aspect ? { aspect } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_list_media',
  {
    title: 'List project media',
    description:
      'List media in the open Flow project\'s asset picker (gallery): { title, kind, mediaId?, index }[]. This is how you obtain the exact mediaTitle that flow_create_character_from_media requires — that tool needs a title matching an existing gallery item\'s accessible name, and this is the only tool that can produce one (previously only recoverable from a DOM snapshot). Pass query to type into the picker\'s own search box first and narrow the scrape to matching tiles (e.g. a filename or a distinctive word from an auto-caption); pass limit to cap how many rows come back. title is recovered from Flow\'s own <img alt> where present, else derived from the picker\'s doubled accessible-name label. kind is classified from the trailing label ("Image", "Video", …). mediaId is present only when the tile\'s underlying src carries a getMediaUrlRedirect media id — treat it as optional. Titles are NOT deduplicated: the gallery legitimately holds several items sharing the same auto-caption (repeat generations, uploads named the same), so every tile is returned in gallery order with its own index; use mediaId to disambiguate exact duplicates when one is present.',
    inputSchema: {
      query: z.string().min(1).optional(),
      limit: z.number().int().min(1).optional(),
    },
  },
  async ({ query, limit }) => {
    try {
      return await withClient(async (c) =>
        ok(await c.listMedia({ ...(query ? { query } : {}), ...(limit ? { limit } : {}) })),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_create_character',
  {
    title: 'Create character',
    description:
      'Create a reusable Flow Character from one or more reference image paths (absolute), for cross-slide consistency, and optionally complete it in the SAME call: pass body to add the full-figure Body view (Flow\'s native "Create Body" pass — describe build, posture and outfit) and info to fill the free-text note Flow\'s scene agent reads. A character with both a Portrait and a Body binds identity far better than a portrait alone. Cast it later with the character parameter, or "@" in a prompt. Returns { name, bodyMediaId?, bodyPath? }.',
    inputSchema: {
      name: z.string().min(1),
      refImages: z.array(z.string().min(1)).min(1),
      body: z.string().min(1).optional(),
      info: z.string().min(1).optional(),
      bodyOutPath: z.string().min(1).optional(),
      model: z.string().min(1).optional(),
    },
  },
  async ({ name, refImages, body, info, bodyOutPath, model }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.createCharacter(name, refImages, {
            ...(body ? { body } : {}),
            ...(info ? { info } : {}),
            ...(bodyOutPath ? { bodyOutPath } : {}),
            ...(model ? { model } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_create_character_from_media',
  {
    title: 'Create character from existing project media',
    description:
      'Like flow_create_character, but the reference is a media item ALREADY IN the project gallery (e.g. a prior generation) instead of a fresh file upload — use this when the reference came from Flow itself, since re-uploading a harvested image can 400. mediaTitle is the option\'s accessible name shown in the gallery (Flow\'s auto-caption, e.g. "Man sitting with open book"), not a file path or media id. Same optional body/info/model/bodyOutPath as flow_create_character. Returns { name, bodyMediaId?, bodyPath? }.',
    inputSchema: {
      name: z.string().min(1),
      mediaTitle: z.string().min(1),
      body: z.string().min(1).optional(),
      info: z.string().min(1).optional(),
      bodyOutPath: z.string().min(1).optional(),
      model: z.string().min(1).optional(),
    },
  },
  async ({ name, mediaTitle, body, info, bodyOutPath, model }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.createCharacterFromMedia(name, mediaTitle, {
            ...(body ? { body } : {}),
            ...(info ? { info } : {}),
            ...(bodyOutPath ? { bodyOutPath } : {}),
            ...(model ? { model } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_character_body',
  {
    title: 'Add character body view',
    description:
      'Add the full-figure Body view to an existing Character that only has a Portrait, via Flow\'s native "Create Body" pass. description should cover build, posture, outfit and setting. Errors BODY_EXISTS if it already has one — use flow_edit_character to change that. Returns { path, mediaId }.',
    inputSchema: {
      name: z.string().min(1),
      description: z.string().min(1),
      outPath: z.string().min(1).optional(),
      model: z.string().min(1).optional(),
    },
  },
  async ({ name, description, outPath, model }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.createCharacterBody(name, description, {
            ...(outPath ? { outPath } : {}),
            ...(model ? { model } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_edit_character',
  {
    title: 'Edit an existing character',
    description:
      'Iterate on an EXISTING Character in place: applies a delta prompt to its Portrait (default) or Body view through the character editor. Use this for "same character, but <change>" instead of re-creating from a new reference image — it preserves the identity Flow has already bound, and each round is recoverable via the editor\'s Show history. Phrase as a delta ("give him a heavier overcoat; keep the face, lighting and framing identical"). Returns { path, mediaId, target }.',
    inputSchema: {
      name: z.string().min(1),
      prompt: z.string().min(1),
      target: z.enum(['portrait', 'body']).optional(),
      outPath: z.string().min(1).optional(),
      model: z.string().min(1).optional(),
    },
  },
  async ({ name, prompt, target, outPath, model }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.editCharacter(name, prompt, {
            ...(target ? { target } : {}),
            ...(outPath ? { outPath } : {}),
            ...(model ? { model } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_character_info',
  {
    title: 'Set character info',
    description:
      "Set (or replace) a Character's free-text note — personality, mannerisms, how it should be framed. Flow's own scene agent reads this when the character is cast, so it does not need repeating in every prompt. Returns { name }.",
    inputSchema: {
      name: z.string().min(1),
      info: z.string().min(1),
    },
  },
  async ({ name, info }) => {
    try {
      return await withClient(async (c) => ok(await c.setCharacterInfo(name, info)))
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_list_characters',
  {
    title: 'List project characters',
    description:
      'Enumerate the open Flow project\'s Characters as { name, id }[]. There was previously no way to discover what Characters exist — flow_get_character/flow_edit_character/flow_character_body/flow_character_info all require an exact, case-sensitive name and throw CHARACTER_NOT_FOUND on a mismatch with no way to learn the right one. Call this first when a name is uncertain.',
    inputSchema: {},
  },
  async () => {
    try {
      return await withClient(async (c) => ok(await c.listCharacters()))
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_get_character',
  {
    title: 'Read back a character',
    description:
      'Read an existing Character without changing anything: its free-text info note, whether it has a Body view yet (hasBody), and the media id of each view it does have. Pass portraitOutPath and/or bodyOutPath (absolute) to also harvest that view to disk — this is the "show me the current portrait" tool that had no path behind it before. Strictly non-destructive: the info field is read, never filled or submitted. Errors CHARACTER_NOT_FOUND if the name (case-sensitive) doesn\'t match — use flow_list_characters to check. Returns { name, info, hasBody, portraitMediaId?, bodyMediaId? }.',
    inputSchema: {
      name: z.string().min(1),
      portraitOutPath: z.string().min(1).optional(),
      bodyOutPath: z.string().min(1).optional(),
    },
  },
  async ({ name, portraitOutPath, bodyOutPath }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.getCharacter(name, {
            ...(portraitOutPath ? { portraitOutPath } : {}),
            ...(bodyOutPath ? { bodyOutPath } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

const transport = new StdioServerTransport()
await server.connect(transport)
