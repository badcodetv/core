/**
 * Timeline edits: insert, move, trim, remove, clone.
 *
 * Every one is a single `executeTransaction` labelled `BadCode: …`, so the user can undo our
 * work in the same steps they watched us take. Every one returns the refreshed dump, because a
 * clip ref (`v0:2`) is only meaningful against the state that produced it — an edit renumbers
 * everything after it on that track.
 */
import type { AudioClipTrackItem, VideoClipTrackItem } from 'premierepro'
import type { CommandHandler } from './index'
import {
  PanelError,
  activeProject,
  activeSequence,
  dumpSequence,
  intArg,
  numArg,
  ppro,
  resolveClip,
  resolveProjectItem,
  secondsToTick,
  selectionFor,
  withAction,
  withActions,
} from '../ppro'

const insert_clip: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const projectItem = await resolveProjectItem(project, String(args.item ?? ''))

  const time = secondsToTick(numArg(args.time, 'time'))
  const videoTrack = intArg(args.videoTrack, 0)
  const audioTrack = intArg(args.audioTrack, 0)
  const limitShift = args.limitShift === true
  const mode = args.mode === 'overwrite' ? 'overwrite' : 'insert'

  const editor = ppro.SequenceEditor.getEditor(sequence)
  withAction(project, `${mode} ${projectItem.name}`, () =>
    mode === 'insert'
      ? editor.createInsertProjectItemAction(projectItem, time, videoTrack, audioTrack, limitShift)
      : editor.createOverwriteItemAction(projectItem, time, videoTrack, audioTrack)
  )

  return dumpSequence(project, sequence)
}

const move_clip: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const clip = await resolveClip(sequence, String(args.clip ?? ''))
  const delta = numArg(args.deltaSeconds, 'deltaSeconds')

  // A move is expressed as an OFFSET, not a destination — Premiere has no "set start" that
  // ripples. Negative moves earlier.
  withAction(project, `move ${String(args.clip)} by ${delta}s`, () => clip.createMoveAction(secondsToTick(delta)))
  return dumpSequence(project, sequence)
}

const trim_clip: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const clip = await resolveClip(sequence, String(args.clip ?? ''))

  const edits: (() => import('premierepro').Action)[] = []
  // in/out are points INTO the source media; start/end are positions in the sequence. Applied in
  // that order so a caller can set both in one call and get the obvious result.
  if (typeof args.inPoint === 'number') edits.push(() => clip.createSetInPointAction(secondsToTick(args.inPoint as number)))
  if (typeof args.outPoint === 'number') edits.push(() => clip.createSetOutPointAction(secondsToTick(args.outPoint as number)))
  if (typeof args.start === 'number') edits.push(() => clip.createSetStartAction(secondsToTick(args.start as number)))
  if (typeof args.end === 'number') edits.push(() => clip.createSetEndAction(secondsToTick(args.end as number)))

  if (edits.length === 0) {
    throw new PanelError('INVALID_ARGS', 'trim_clip needs at least one of inPoint, outPoint, start, end.')
  }

  withActions(project, `trim ${String(args.clip)}`, edits)
  return dumpSequence(project, sequence)
}

const remove_clip: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const refs = Array.isArray(args.clips) ? (args.clips as string[]) : []
  if (refs.length === 0) throw new PanelError('INVALID_ARGS', 'remove_clip needs at least one clip ref.')

  // Resolve every ref BEFORE removing anything: removal renumbers the track, so resolving
  // lazily would make the second ref in the list mean a different clip than the caller meant.
  const items: (VideoClipTrackItem | AudioClipTrackItem)[] = []
  for (const ref of refs) items.push(await resolveClip(sequence, ref))

  const selection = await selectionFor(sequence, items)
  const editor = ppro.SequenceEditor.getEditor(sequence)
  const ripple = args.ripple === true

  withAction(project, `remove ${refs.join(', ')}`, () =>
    editor.createRemoveItemsAction(selection, ripple, ppro.Constants.MediaType.ANY, false)
  )
  return dumpSequence(project, sequence)
}

const clone_clip: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const clip = await resolveClip(sequence, String(args.clip ?? ''))

  const offset = secondsToTick(numArg(args.deltaSeconds, 'deltaSeconds'))
  const videoOffset = intArg(args.videoTrackOffset, 0)
  const audioOffset = intArg(args.audioTrackOffset, 0)
  const isInsert = args.mode !== 'overwrite'

  const editor = ppro.SequenceEditor.getEditor(sequence)
  withAction(project, `clone ${String(args.clip)}`, () =>
    editor.createCloneTrackItemAction(clip, offset, videoOffset, audioOffset, true, isInsert)
  )
  return dumpSequence(project, sequence)
}

export const clipCommands = {
  insert_clip,
  move_clip,
  trim_clip,
  remove_clip,
  clone_clip,
}
