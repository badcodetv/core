/**
 * Getting pixels out: a still frame, or the whole sequence.
 *
 * The panel's half is deliberately thin — it is handed fully-resolved **Windows** paths and does
 * nothing but call Premiere. Every decision about *where* a file goes belongs to the server,
 * which is the only side with a filesystem.
 *
 * 🔴 **Neither export is an Action**, so neither runs in a transaction and neither appears in
 * Edit ▸ Undo. Nothing to undo — they write files, they do not change the project.
 *
 * 🔴 **Both resolve BEFORE the file has finished being written.** Measured live: a frame export
 * resolved at 8394ms, the file appeared at 8498ms and was still growing (672KB of an eventual
 * 831KB), settling at 8704ms. The server polls for a stable size afterwards; do not treat the
 * promise resolving as "the file is ready".
 */
import { PanelError, activeProject, activeSequence, numArg, ppro, secondsToTick, strArg } from '../ppro'
import type { CommandHandler } from './index'

const export_frame: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project, typeof args.sequence === 'string' ? args.sequence : undefined)

  const filename = strArg(args.filename, 'filename')
  const dir = strArg(args.dir, 'dir')
  const time = secondsToTick(numArg(args.time, 'time'))

  const frameSize = await sequence.getFrameSize()
  const width = typeof args.width === 'number' ? Math.trunc(args.width) : (frameSize?.width ?? 1920)
  const height = typeof args.height === 'number' ? Math.trunc(args.height) : (frameSize?.height ?? 1080)

  const written = await ppro.Exporter.exportSequenceFrame(sequence, time, filename, dir, width, height)
  if (!written) {
    throw new PanelError(
      'EXPORT_FAILED',
      `Premiere refused to export a frame of "${sequence.name}" at ${String(args.time)}s to ${dir}\\${filename}.`
    )
  }
  return { path: `${dir}\\${filename}`, time: numArg(args.time, 'time'), width, height, sequence: sequence.name }
}

const export_sequence: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project, typeof args.sequence === 'string' ? args.sequence : undefined)

  const outputFile = strArg(args.outputFile, 'outputFile')
  const preset = strArg(args.preset, 'preset')
  // `exportFull` is Premiere's word for "the whole sequence"; false means honour in/out points.
  const exportFull = args.exportFull !== false

  const manager = ppro.EncoderManager.getManager()
  const started = await manager.exportSequence(
    sequence,
    ppro.Constants.ExportType.IMMEDIATELY,
    outputFile,
    preset,
    exportFull
  )
  if (!started) {
    throw new PanelError(
      'EXPORT_FAILED',
      `Premiere refused to export "${sequence.name}" to ${outputFile}. Check the preset is readable and the ` +
        'output directory exists.'
    )
  }
  return { path: outputFile, sequence: sequence.name, exportFull }
}

export const exportCommands = {
  export_frame,
  export_sequence,
}
