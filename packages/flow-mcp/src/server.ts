import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
import { z } from 'zod'
import { NAME, VERSION } from './version'
import { FlowClient } from './flow-client'
import { ok, fail, NOT_RUNNING_HINT, type ToolResult } from './result'
import { resolveChannel, releaseLock, surveyChannels, profileFor, type Resolution } from './channel'
import { fileURLToPath } from 'node:url'
import { dirname, resolve as resolvePath } from 'node:path'

/**
 * Cache the CDP attachment across tool calls: the stdio server process is long-lived, and
 * keeping the same Page preserves image-mode state and Flow's in-session context between
 * edit-loop rounds (as well as saving the attach + page discovery per call). A dead handle
 * (user restarted Chrome) is detected via isAlive() and retried once with a fresh connect;
 * close() on a connectOverCDP browser only detaches — it never kills the user's Chrome.
 */
let cached: FlowClient | null = null
const DISCONNECTED_RE = /Target closed|browser has been closed|Target page, context or browser has been closed|ECONNRESET/i

/**
 * Repo root, for the .flow-channels/ lock directory. src/ -> package -> packages/ -> root.
 */
const REPO_ROOT = resolvePath(dirname(fileURLToPath(import.meta.url)), '..', '..', '..')

/**
 * The channel this server process owns. Resolved once, lazily, then held for the process
 * lifetime — one Claude session, one browser. Nothing here asks the caller for a port: an
 * explicit FLOW_CDP_PORT still wins, but the default is discovery + a PID lock, so two
 * concurrent sessions land on different browsers without anyone choosing.
 */
let channel: Resolution | null = null

async function currentChannel(): Promise<Resolution> {
  channel ??= await resolveChannel(REPO_ROOT, 'flow')
  return channel
}

// Give the channel back when this session ends, so the next one can reuse the browser.
for (const sig of ['exit', 'SIGINT', 'SIGTERM'] as const) {
  process.on(sig, () => {
    if (channel && channel.how !== 'pinned') releaseLock(REPO_ROOT, channel.channel)
    if (sig !== 'exit') process.exit(0)
  })
}

async function withClient<T>(fn: (c: FlowClient) => Promise<T>): Promise<T> {
  const ch = await currentChannel()
  for (let attempt = 0; attempt < 2; attempt++) {
    if (cached && !cached.isAlive()) {
      await cached.close().catch(() => {})
      cached = null
    }
    cached ??= await FlowClient.connect(ch.endpoint)
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
  if (msg.startsWith('TIMEOUT')) return fail('TIMEOUT', msg, 'The message names a .txt/.png dump of what was on screen when the clock ran out. READ IT before retrying: two failure states have never been mapped (out of credits, rate limiting/captcha) and both surface as a plain timeout. If the dump shows one, add its exact wording to failure-card.ts so it aborts in seconds next time.')
  if (msg === 'PROJECT_NOT_FOUND') return fail('PROJECT_NOT_FOUND', 'No Flow project with that name.', 'Check the name in the Flow projects list, or use flow_list_projects/flow_open_project with id instead — name matching fails on a tile with no <a href>.')
  if (msg === 'PROJECT_ID_OR_NAME_REQUIRED') return fail('INVALID_ARGS', 'Provide id or name.', 'flow_list_projects returns id when derivable.')
  if (msg === 'CHARACTER_NOT_FOUND') return fail('CHARACTER_NOT_FOUND', 'No Character with that name in the open project.', 'Check the Characters tab; names are case-sensitive.')
  if (msg === 'BODY_EXISTS') return fail('BODY_EXISTS', 'That character already has a Body view.', 'Use flow_edit_character with target "body" to change it.')
  if (msg === 'NO_BODY') return fail('NO_BODY', 'That character has no Body view yet.', 'Create one with flow_character_body first.')
  if (msg === 'NO_PORTRAIT') return fail('NO_PORTRAIT', 'That character has no Portrait view.', 'Every character gets a Portrait from its founding reference image — this usually means the name resolved to the wrong character, or the editor failed to render before the tab was queried. Re-check the name with flow_list_characters.')
  if (msg === 'MEDIA_NOT_FOUND') return fail('MEDIA_NOT_FOUND', 'No project media matches that title.', 'Use the exact accessible name shown in the project gallery, not a file path or media id.')
  if (msg === 'ANIMATE_NOT_FOUND') return fail('ANIMATE_NOT_FOUND', 'No project media tile offered the Animate action.', 'The source still may not have finished uploading, or the tile is a video (whose menu has no Animate).')
  if (msg === 'ANIMATE_WRONG_SOURCE') return fail('ANIMATE_WRONG_SOURCE', 'Flow attached a different still than the one requested, so the clip was NOT generated.', 'Aborted deliberately before spending credits: animating the wrong frame returns a healthy-looking clip of the wrong picture. Retry; if it persists, the tile-to-control mapping in openAnimateMenu has drifted again.')
  // Duration errors carry their own detail after the code, so they pass the message through.
  if (msg.startsWith('VIDEO_DURATION_INVALID')) return fail('INVALID_ARGS', msg, 'Flow offers exactly 4, 6, 8 and 10 second clips — there is no slider.')
  if (msg.startsWith('VIDEO_DURATION_UNAVAILABLE')) return fail('VIDEO_DURATION_UNAVAILABLE', msg, 'Only Gemini Omni Flash makes 10s clips; every Veo 3.1 tier caps at 8s (confirmed live 2026-08-12 — the 10s tab is absent from the DOM, not merely disabled). Either drop to 8s or pass model "Omni Flash".')
  if (msg.startsWith('VIDEO_DURATION_NOT_APPLIED')) return fail('VIDEO_DURATION_NOT_APPLIED', msg, 'The duration tab was clicked but the config trigger never showed it — aborted before spending credits, because an ignored duration returns a healthy-looking clip of the wrong length. The tab names in the compose popover have probably drifted; re-map with packages/flow-mcp/src/smoke-duration.ts.')
  if (msg.startsWith('VIDEO_END_ONLY_UNSUPPORTED')) return fail('VIDEO_END_ONLY_UNSUPPORTED', msg, 'Flow has first-frame and first+last-frame generation, but not last-frame-alone (live-tested 2026-08-12 on Veo 3.1 Fast and Lite — the slot fills and is then flagged invalid). Pass a startImage as well, or describe the opening in the prompt and use text-to-video.')
  if (msg === 'NO_PROJECT_OPEN') return fail('NO_PROJECT_OPEN', 'No Flow project is open.', 'Open one with flow_open_project first — scene tools read the project id out of the current URL.')
  if (msg.startsWith('NOT_IN_SCENE')) return fail('NOT_IN_SCENE', msg, 'A scene id is the 36-character uuid after /edit/ in a Flow scene URL — clicking any clip in the project grid opens it. It is NOT the clip\'s media id.')
  if (msg.startsWith('SCENE_ID_INVALID')) return fail('INVALID_ARGS', msg, 'Copy the uuid after /edit/ in the Flow URL.')
  if (msg.startsWith('SCENE_EXTEND_EMPTY_PROMPT')) return fail('INVALID_ARGS', msg, 'Describe what happens next in the continuation.')
  if (msg.startsWith('SCENE_ADD_CLIP_MENU_NOT_OPEN')) return fail('SCENE_ADD_CLIP_MENU_NOT_OPEN', msg, 'Confirm you are in a scene editor (/edit/<sceneId>) with a loaded clip. If the timeline is there but the menu will not open, Flow has changed the control — re-map it before retrying.')
  if (msg.startsWith('SCENE_EXTEND_NOT_ARMED')) return fail('SCENE_EXTEND_NOT_ARMED', msg, 'Flow\'s Add Clip menu has probably drifted. Re-map it against the live scene editor before retrying; do NOT fall back to an ordinary generation, which silently produces a different shot.')
  if (msg.startsWith('SAVE_FRAME_NOT_FOUND')) return fail('SAVE_FRAME_NOT_FOUND', msg, 'Let the scene player load and paint a frame, then retry.')
  if (msg.startsWith('VIDEO_FRAMES_UNAVAILABLE')) return fail('VIDEO_FRAMES_UNAVAILABLE', msg, 'Only the Veo 3.1 tiers accept a LAST frame; Omni Flash rejects it (its End slot comes back with an error badge, live-confirmed 2026-08-12). Pass model "Veo 3.1 Fast" (or Lite/Quality), or drop endImage.')
  if (msg.startsWith('VIDEO_REFINE_NO_SOURCE') || msg.startsWith('VIDEO_REFINE_NO_PROMPT')) return fail('INVALID_ARGS', msg)
  if (msg.startsWith('VIDEO_REFINE_NOT_A_MEDIA_ID')) return fail('INVALID_ARGS', msg, 'Refine works on a clip that is already in the Flow project, addressed by the mediaId flow_generate_video returned — not by the .mp4 you saved. If you no longer have that id, list the project media with flow_list_media.')
  if (msg.startsWith('VIDEO_REFINE_NOT_RESTORED')) return fail('VIDEO_REFINE_NOT_RESTORED', msg, "Flow's per-clip Reuse prompt did not put the original prompt back in the compose bar, so there is nothing to refine FROM — aborted before spending credits. Re-map the clip menu with packages/flow-mcp/src/smoke-video-reuse.ts.")
  if (msg.startsWith('VIDEO_REFINE_FRAMES_LOST')) return fail('VIDEO_REFINE_FRAMES_LOST', msg, 'Setting durationSeconds cleared the source frame that Reuse prompt restored. Re-run without durationSeconds to keep the original clip length, or regenerate from the still with flow_generate_video.')
  if (msg.startsWith('CLIP_NOT_FOUND')) return fail('CLIP_NOT_FOUND', msg, 'The mediaId must be a CLIP in the project currently open. Open the right project with flow_open_project, and check the id with flow_list_media.')
  if (msg.startsWith('CLIP_MENU_NOT_FOUND') || msg.startsWith('CLIP_ACTION_NOT_FOUND')) return fail('CLIP_ACTION_NOT_FOUND', msg, "The clip's own hover menu did not offer that action. Re-map it with packages/flow-mcp/src/smoke-video-menu.ts. Note that Extend and video Edit are NOT among the actions Flow offers here — tested on Veo 3.1 Fast, Veo 3.1 Lite and Omni Flash on 2026-08-12, all eleven-item menus.")
  if (msg === 'FRAME_SLOTS_NOT_FOUND') return fail('FRAME_SLOTS_NOT_FOUND', 'The compose bar is not showing its Start/End frame slots.', 'The Frames source tab did not take, or Flow has renamed the "Swap first and last frames" control this code anchors on. Re-map with packages/flow-mcp/src/smoke-frames.ts.')
  if (msg.startsWith('FRAME_REJECTED')) return fail('FRAME_REJECTED', msg, 'Flow marked the frame invalid rather than accepting it — aborted before spending credits. Most often this is a last frame on a model that does not support one; check the model, and that the image file is a normal JPEG/PNG.')
  if (msg.startsWith('FRAME_NOT_ATTACHED')) return fail('FRAME_NOT_ATTACHED', msg, 'The upload finished but the picker never put it in the slot. Usually the media row was still resolving; retry once. If it persists, re-map the picker with packages/flow-mcp/src/smoke-frame-pick.ts.')
  if (msg === 'SUBMIT_FAILED') return fail('SUBMIT_FAILED', 'The prompt was typed but Flow never accepted the submit.', 'Usually a wedged compose bar — reload the project URL (twice; the first load can throw a client-side exception) and retry.')
  if (msg === 'NOT_IN_PROJECT') return fail('NOT_IN_PROJECT', 'The page is not inside a Flow project.', 'Open one with flow_open_project, or pass a project id.')
  if (msg === 'POLICY_BLOCKED') return fail('POLICY_BLOCKED', 'Flow flagged this generation as a possible policy violation — it will never complete no matter how long you wait.', 'Do NOT retry the same prompt. Rewrite it: check the reference image and any Character name/info fields, not just the prompt text (docs/flow/failure-modes.md §A2), then use the trigger list and rewrite table at docs/flow/failure-modes.md §A5-A6.')
  return fail('FLOW_ERROR', msg)
}

/**
 * Flow's documented image aspect ratios (docs/flow/image-prompting.md §9), Nano Banana 2's
 * extras included. Selector-confirmed against the live tab list (automation-images.md:172-174)
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
      const ch = await currentChannel()
      return await withClient(async (c) => ok({ ...(await c.status()), channel: ch.channel, port: ch.port, resolvedBy: ch.how }))
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_channels',
  {
    title: 'Browser channels',
    description:
      'List the browser channels — a channel is one CDP port plus one Chrome profile. Shows which are running, which are claimed by a live session, and which this session owns. Use it to answer "which browser am I on" and to find a free one; you never need to pick a port by hand.',
    inputSchema: {},
  },
  async () => {
    try {
      const mine = await currentChannel().catch(() => null)
      const rows = await surveyChannels(REPO_ROOT)
      return ok({
        mine: mine ? { channel: mine.channel, port: mine.port, resolvedBy: mine.how, needsLaunch: mine.needsLaunch } : null,
        channels: rows.map((r) => ({ ...r, profile: profileFor(r.channel), isMine: r.channel === mine?.channel })),
        launch: 'Launch a channel with: ./scripts/browser-channel.sh up <n>   (or `claim` to be given a free one)',
      })
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
      'which is normally a creation timestamp such as "Aug 12, 09:07 AM" (confirmed live). An empty name means the ' +
      'read-back failed and the real name is unknown; it is never a guess. Callers MUST use the returned name, and ' +
      'the returned id in preference to it. Ends with the new project open, ready for a generation call.',
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
      'Make a video and save the .mp4 to outPath. ONE tool, four source modes, chosen by which images you pass: ' +
      'startImage only = animate that still (the everyday path); startImage + endImage = generate the motion BETWEEN two ' +
      'stills (Flow\'s first/last frame feature — art-direct page N and page N+1 as clean stills and let the video carry ' +
      'only the move between them); neither = text-to-video from the prompt alone. An endImage with NO startImage is not a mode Flow has (it fills the slot, then marks it invalid — tested on Veo 3.1 Fast and Lite) and is refused up front. ' +
      '⚠️ WRITE THE PROMPT FOR THE MODE. With one still, describe WHAT MOVES. With a start AND an end frame, name ONLY the ' +
      'camera move that connects them — the two stills already carry the content, and adding scene description there makes ' +
      'drift worse (docs/flow/video-prompting.md §4). ' +
      '⚠️ endImage needs a Veo 3.1 tier: Gemini Omni Flash takes a first frame but REJECTS a last one (confirmed live ' +
      '2026-08-12) and the call fails before uploading anything. ' +
      'Asserts the Settings-panel video defaults (model, aspect, output count) before generating — they live on the ' +
      "project and RESET to Omni Flash on a fresh project, so this call always sets them rather than trusting whatever " +
      'was last selected. model defaults to "Veo 3.1 Fast" (20 credits/clip) when omitted — a deliberate middle tier, ' +
      'not the cheapest and not the most expensive. Other recorded options: "Omni Flash", "Veo 3.1 Lite" (10 credits), ' +
      '"Veo 3.1 Quality" (100 credits — ask for this explicitly; it costs 5x Fast and 10x Lite), ' +
      '"Veo 3.1 Lite[Lower Priority]". aspect defaults to "16:9" (matches most comic pages); pass "9:16" for portrait. ' +
      'count (1-4, default 1) sets how many candidate clips Flow generates in this turn — ALL of them are harvested, ' +
      'the first at outPath and the set under `candidates` with -a/-b/-c/-d suffixes. Two candidates cost one turn\'s ' +
      'WAIT (~110s) rather than two, so it is the cheapest way to buy a choice; it is not cheaper in credits. ' +
      'character casts a Flow Character in the clip, the same names flow_list_characters returns. ⚠️ The mechanism is ' +
      'proven but identity fidelity is not: for a character who must LOOK right, art-direct a still with the character ' +
      'and animate that (startImage) — the still pins the likeness in a way a text mention does not. ' +
      'durationSeconds sets the CLIP LENGTH — 4, 6, 8 or 10. Omitting it leaves Flow on whatever the ' +
      'project last used, which is normally its 8s default; every clip made before this parameter existed ' +
      'was 8s by accident rather than by choice, so state a length deliberately. Shorter is cheaper on Omni ' +
      'Flash (15/20/25/30 credits for 4/6/8/10s) and a 4s clip is often the right answer for a single comic ' +
      'beat. ⚠️ 10s is Omni Flash ONLY — on every Veo 3.1 tier the 10s option does not exist, and asking for ' +
      'it there fails immediately (before any credits are spent) rather than quietly returning 8s. ' +
      'Returns { path, mediaId } — plus via: "frames-fallback" when the startImage-only path degraded in a busy ' +
      'project and the first/last-frame composer carried the request instead. The clip is equally valid; the flag is ' +
      'there so a run that quietly took the slower route is visible, and it leaves one stray uploaded tile behind.',
    inputSchema: {
      startImage: z.string().min(1).optional(),
      endImage: z.string().min(1).optional(),
      motion: z.string().min(1),
      model: z.string().optional(),
      aspect: z.enum(['16:9', '9:16']).optional(),
      count: z.number().int().min(1).max(4).optional(),
      durationSeconds: z.union([z.literal(4), z.literal(6), z.literal(8), z.literal(10)]).optional(),
      character: z.string().min(1).optional(),
      outPath: z.string().min(1),
    },
  },
  async ({ startImage, endImage, motion, model, aspect, count, durationSeconds, character, outPath }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.generateVideo({
            motion,
            outPath,
            ...(startImage ? { startImage } : {}),
            ...(endImage ? { endImage } : {}),
            ...(model ? { model } : {}),
            ...(aspect ? { aspect } : {}),
            ...(count ? { count } : {}),
            ...(durationSeconds ? { durationSeconds } : {}),
            ...(character ? { character } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_refine_video',
  {
    title: 'Refine an existing video',
    description:
      '"Like that clip, but slower / darker / without the pan." Re-runs an EXISTING clip\'s turn with a new motion ' +
      'prompt and saves the new .mp4 to outPath. ' +
      'The point of this tool over flow_generate_video is that YOU DO NOT NEED THE SOURCE STILL: Flow\'s per-clip ' +
      '"Reuse prompt" restores the original prompt AND re-attaches the frame that clip was generated from, so a refine ' +
      'works days later from nothing but the clip\'s mediaId (live-proven 2026-08-12 — the refined clip opened on the ' +
      'original source frame and then followed the new prompt). ' +
      'mediaId is the id flow_generate_video RETURNED, not the .mp4 path you saved it to, and the clip must be in the ' +
      'project currently open. ' +
      'motion REPLACES the original prompt — write the whole new prompt, not a delta ("Slow pull back, the light fades ' +
      'down", not "but slower"). The prompt it replaced comes back as originalPrompt, so you can show the user what changed. ' +
      'Omit durationSeconds to keep the original clip\'s length, which is the normal case; passing one re-opens the ' +
      'compose popover and is refused if that clears the restored frame. ' +
      'Returns { path, mediaId, originalPrompt }.',
    inputSchema: {
      mediaId: z.string().min(1),
      motion: z.string().min(1),
      model: z.string().optional(),
      durationSeconds: z.union([z.literal(4), z.literal(6), z.literal(8), z.literal(10)]).optional(),
      outPath: z.string().min(1),
    },
  },
  async ({ mediaId, motion, model, durationSeconds, outPath }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.refineVideo({
            mediaId,
            motion,
            outPath,
            ...(model ? { model } : {}),
            ...(durationSeconds ? { durationSeconds } : {}),
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
      'Generate N images sequentially in ONE Flow session from an ordered list of prompts (e.g. every scene on a story\'s prompts.md). Saves <outDir>/<NN>.jpg per prompt (candidates get -a/-b… suffixes when numOutputs > 1 — see flow_generate_image). Use after planning all prompts up front. character casts a project Character (create one first with flow_create_character) into EVERY prompt in the batch, via the same mechanism flow_generate_image uses — pass per-scene character names as part of the prompt text instead if different prompts need different characters. model/aspect/numOutputs apply to the WHOLE batch (asserted once before the first prompt, not re-asserted per prompt). ' +
      'resume: true SKIPS any prompt whose output file is already on disk, and reports it as an item with skipped: true (its real dimensions are read back from the file; mediaId is empty, since that is unknowable without regenerating). This is how you restart a long run that died — same prompts, same outDir, nothing already paid for is paid for twice. It also means deleting one bad image and re-running regenerates exactly that one. '
      + 'Never throws away work already done: returns { items: BatchItem[], failed: BatchFailure[], partial: boolean }. `items` is every prompt that completed. `failed` is every prompt that did not, each as { index, prompt, code, error } — check `partial` before assuming the batch is done. A POLICY_BLOCKED prompt is recorded in `failed` and the batch CONTINUES to the next prompt (that verdict is about the one prompt, not the run); any other failure (TIMEOUT, SUBMIT_FAILED, …) is recorded and the batch STOPS there, since it likely means the page itself needs recovering — re-run from prompts.slice(items.length + failed.length) once fixed. Never retry a POLICY_BLOCKED entry unmodified; rewrite it per docs/flow/failure-modes.md. ' +
      'Capped at 20 prompts per call, up from the earlier cap of 8 (a schema choice, not a Flow limit) — batch is strictly serial, so a longer list is a longer call, not a heavier one, but there is no per-item timeout budget yet and a very long unattended call has its own failure modes (session drift, Flow rate-limiting/recaptcha on sustained volume per docs/flow/platform-controls.md §9). 20 comfortably covers one comic\'s worth of scene prompts while keeping worst-case call length bounded; split anything larger into multiple calls. ' +
      IMAGE_MODEL_DESC +
      ' ' +
      IMAGE_ASPECT_DESC,
    inputSchema: {
      prompts: z.array(z.string().min(1)).min(1).max(20),
      outDir: z.string().min(1),
      character: z.string().min(1).optional(),
      numOutputs: z.number().int().min(1).max(4).optional(),
      model: z.string().min(1).optional(),
      aspect: z.enum(IMAGE_ASPECTS).optional(),
      resume: z.boolean().optional(),
    },
  },
  async ({ prompts, outDir, character, numOutputs, model, aspect, resume }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.generateBatch(prompts, outDir, {
            ...(character ? { character } : {}),
            ...(numOutputs ? { numOutputs } : {}),
            ...(model ? { model } : {}),
            ...(aspect ? { aspect } : {}),
            ...(resume ? { resume } : {}),
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
      'List media in the open Flow project\'s asset picker (gallery): { title, kind, mediaId?, index }[]. This is how you obtain the exact mediaTitle that flow_create_character_from_media requires — that tool needs a title matching an existing gallery item\'s accessible name, and this is the only tool that can produce one (previously only recoverable from a DOM snapshot). Pass query to type into the picker\'s own search box first and narrow the scrape to matching tiles (e.g. a filename or a distinctive word from an auto-caption); pass limit to cap how many rows come back. title is recovered from Flow\'s own <img alt> where present, else derived from the picker\'s doubled accessible-name label. kind is classified from the trailing label ("Image", "Video", …). mediaId is present only when the tile\'s underlying src carries a getMediaUrlRedirect media id — treat it as optional. ⚠️ This call ASSERTS IMAGE MODE on the compose bar before reading, because the picker only lists what the current mode can use — read it in a video mode and a project full of clips reports zero videos (measured). Side effect: the default image model/count are re-asserted, which the next video call undoes automatically. Titles are NOT deduplicated: the gallery legitimately holds several items sharing the same auto-caption (repeat generations, uploads named the same), so every tile is returned in gallery order with its own index; use mediaId to disambiguate exact duplicates when one is present.',
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

server.registerTool(
  'flow_scene_open',
  {
    title: 'Open a Flow scene (Scene Builder)',
    description:
      "Open a clip's scene editor at /project/<projectId>/edit/<sceneId> — Flow's Scene Builder — and wait for its timeline to render. This is the surface that carries Extend, Save Frame and the scene-level prompt box, none of which exist on the compose bar. sceneId is the 36-character uuid AFTER /edit/ in a Flow scene URL; clicking any clip in the project grid navigates there, so it is the id a user pastes. It is NOT a media id — clip media ids never match scene ids, which is the usual source of confusion. The project id is read from the currently open project, so open the project first. Returns { projectId, sceneId, url }.",
    inputSchema: { sceneId: z.string().min(1) },
  },
  async ({ sceneId }) => {
    try {
      return await withClient(async (c) => ok(await c.openScene(sceneId)))
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_scene_extend',
  {
    title: 'Extend a clip into a longer scene (Scene Builder)',
    description:
      "Continue a clip from its own end using Flow's Extend. Unlike generating from a still, Extend hands the model the clip's own context, so motion, lighting and subject carry across the join. Use it for RUNWAY — a long continuous bed under narration — and use flow_generate_video with startImage/endImage when you need to control exactly where a shot lands.\n\n⚠️ IT DOES NOT PRODUCE A FILE. Extend appends a segment to a SCENE and navigates to /scene/<newId>; no new clip appears in the gallery and there is no mp4 to save, which is why this tool takes no outPath. Success is the scene getting longer, and that is what comes back: { sceneId, url, durationSeconds, previousDurationSeconds, addedSeconds }. To get an mp4 out, use the scene editor's Download control in the browser; to get stills out, use flow_scene_save_frame. (Learned the hard way 2026-08-18: waiting for a new clip made a successful Extend look like a 480s timeout.)\n\n⚠️ THE TIER IS NOT YOURS TO CHOOSE: Flow pins Extend to one model regardless of the compose bar (observed as Veo 3.1 Lite on 2026-08-18, on an account offering Fast and Quality freely). The tier used comes back as `model` — read it rather than assuming, and treat Extend as a quality trade. Observed adding ~7s per Extend, not the full 8.\n\nRuns inside the scene editor: pass sceneId, or call flow_scene_open first.",
    inputSchema: {
      prompt: z.string().min(1),
      sceneId: z.string().min(1).optional(),
    },
  },
  async ({ prompt, sceneId }) => {
    try {
      return await withClient(async (c) =>
        ok(await c.sceneExtend({ prompt, ...(sceneId ? { sceneId } : {}) })),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_scene_save_frame',
  {
    title: 'Save a frame from a scene (Scene Builder)',
    description:
      "Save the frame under the scene player's playhead into the project as an image asset, using Flow's own Save Frame control. This is the frame-to-frame chaining workflow built in: the saved frame lands in the gallery and can be used as the startImage of the next generation with no download, no ffmpeg and no re-upload. position 'end' parks the playhead at the clip's last frame first — which is the position chaining almost always wants — and 'current' (the default) takes wherever the playhead already sits. Runs inside the scene editor: pass sceneId, or call flow_scene_open first. Returns { mediaId?, position, playhead? }; mediaId is absent when the asset had not surfaced in the gallery scrape before the wait elapsed, which does not mean it failed to save.",
    inputSchema: {
      sceneId: z.string().min(1).optional(),
      position: z.enum(['current', 'end']).optional(),
    },
  },
  async ({ sceneId, position }) => {
    try {
      return await withClient(async (c) =>
        ok(
          await c.sceneSaveFrame({
            ...(sceneId ? { sceneId } : {}),
            ...(position ? { position } : {}),
          }),
        ),
      )
    } catch (err) {
      return toToolError(err)
    }
  },
)

server.registerTool(
  'flow_scene_extend_model',
  {
    title: 'Read which tier Extend is pinned to',
    description:
      "Report which model Flow currently pins Scene Builder's Extend to, WITHOUT generating anything. Extend arms rather than fires — Flow keeps its Create button disabled until the prompt box has text — so this is free to call, and it is the honest way to find out what an Extend would cost in quality before committing to one. Returns { model }, normalised to the compose bar's spelling (Flow writes the label hyphenated, e.g. \"Extend (Veo 3.1 - Lite)\" → \"Veo 3.1 Lite\"). model is null when Flow renders its unsubstituted \"{{modelName}}\" placeholder, a templating bug seen live on 2026-08-18 — null means 'could not read it', never 'no tier'.",
    inputSchema: { sceneId: z.string().min(1).optional() },
  },
  async ({ sceneId }) => {
    try {
      return await withClient(async (c) => ok(await c.sceneExtendModel(sceneId)))
    } catch (err) {
      return toToolError(err)
    }
  },
)
