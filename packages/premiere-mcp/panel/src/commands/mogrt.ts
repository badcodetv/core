/**
 * Motion Graphics Templates.
 *
 * The odd one out among the mutations: `insertMogrtFromPath` is **not an Action**. It returns the
 * created track items synchronously, so it cannot go inside a `CompoundAction` and it leaves no
 * single `BadCode:` entry in Edit ▸ Undo. It still needs `lockedAccess`.
 *
 * 🔴 What it CANNOT do, measured 2026-08-22: set the template's text. An inserted MOGRT carries an
 * `AE.ADBE Text` component whose param 0 is `Source Text`, and writing it throws
 * `Illegal Parameter type` — the same refusal `AE.ADBE PPro SimpleText` gives. Its position,
 * scale, rotation and opacity DO write, through `premiere_set_param` like any other component.
 * So this tool places and positions; a human types the words. That is the intended division, not
 * a gap — see the `premiere-automation` skill §8.
 */
import type { CommandHandler } from './index'
import {
  PanelError,
  activeProject,
  activeSequence,
  dumpSequence,
  intArg,
  numArg,
  ppro,
  secondsToTick,
  strArg,
} from '../ppro'

const insert_mogrt: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)

  const path = strArg(args.path, 'path')
  const time = secondsToTick(numArg(args.time, 'time'))
  const videoTrack = intArg(args.videoTrack, 0)
  const audioTrack = intArg(args.audioTrack, 0)

  const editor = ppro.SequenceEditor.getEditor(sequence)

  let inserted: unknown = null
  let failure: unknown = null
  project.lockedAccess(() => {
    try {
      inserted = editor.insertMogrtFromPath(path, time, videoTrack, audioTrack)
    } catch (err) {
      failure = err
    }
  })

  if (failure) {
    throw new PanelError('INVALID_ARGS', `Premiere refused the template at ${path}: ${String(failure)}`)
  }
  // It returns an array of the created track items. An empty array or a null means Premiere
  // declined without throwing — which it does for a path it cannot read.
  const items = Array.isArray(inserted) ? inserted : []
  if (items.length === 0) {
    throw new PanelError(
      'INVALID_ARGS',
      `No template was inserted from ${path}. Check the path exists on the WINDOWS side and ends in .mogrt.`
    )
  }

  // Return the plain dump like every other mutation. What arrived shows up as `changed.added`
  // in the view — a title inserts one item, a template with audio inserts two.
  return dumpSequence(project, sequence)
}

export const mogrtCommands = {
  insert_mogrt,
}
