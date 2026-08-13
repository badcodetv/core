import {
  type AssetView,
  type EncAsset,
  type EncConfig,
  assetView,
  formatDuration,
  formatEnc,
  formatShare,
} from '@badcode/enc'
import { shortAddress } from '@badcode/chain-react'
import type { PublicKey } from '@solana/web3.js'
import { Counter } from './Counter'
import type { EncActions } from './useEncActions'

/**
 * The Imperial Gazette: ten columns, sold by the month.
 *
 * One mechanism serves all ten slots — the program does not branch on which is
 * which — so everything that distinguishes them is either a genesis parameter
 * (the price ladder, fixed as a share of the money supply) or presentation,
 * which is this file. The chain records; the gallery chooses.
 */

/**
 * What each slot is, in newspaper furniture.
 *
 * **Provisional.** The real names are written into the assets at deployment and
 * become permanent when the upgrade authority is burned; only the two ends are
 * settled — masthead dearest, classified cheapest — and the ladder in between
 * is fixed as parts per million of the money supply, which is why the ratios
 * never move however much they print.
 */
const FURNITURE = [
  'Classified',
  'Small ads',
  'Obituaries',
  'Letters',
  'Announcements',
  'Business',
  'Features',
  'Editorial',
  'Leader',
  'Masthead',
]

/** What a column says when nobody has ever written in it. */
const EMPERORS_DEFAULT_COPY =
  'THE EMPEROR HAS NOTHING TO SAY. HE SAYS IT EVERY MONTH, IN THIS SPACE, AND CHARGES A RISING PRICE FOR THE PRIVILEGE OF SAYING SOMETHING ELSE.'

function Redacted() {
  // The pen writes one fixed marker and no text of its own, so there is nothing
  // to render but the shape of what is gone.
  return (
    <p className="gz-redacted" aria-label="This column has been struck by the editor">
      <span style={{ width: '38%' }} />
      <span style={{ width: '72%' }} />
      <span style={{ width: '55%' }} />
    </p>
  )
}

/**
 * Where this price is in its thirty-day walk to the new supply.
 *
 * Read off the endpoints rather than assumed: this said "still climbing" for
 * every unarrived price until 2026-08-13, which is the forbidden claim wearing
 * a status label — M2 fell in 6.1% of the months in the record, and a burn
 * walks the reserve *down* over exactly the same window.
 */
function travelling(view: AssetView): string {
  if (view.arrived) return 'arrived'
  if (view.priceTo > view.priceFrom) return 'still climbing'
  if (view.priceTo < view.priceFrom) return 'still falling'
  return 'not moving'
}

function Column({
  view,
  supply,
  actions,
}: {
  view: AssetView
  supply: bigint
  actions: EncActions
}) {
  return (
    <article className={`gz-column${view.index === 9 ? ' gz-column-lead' : ''}`}>
      <header className="gz-column-head">
        <p className="gz-furniture">{FURNITURE[view.index]}</p>
        <p className="gz-slot">Slot {String(view.index).padStart(2, '0')}</p>
      </header>

      {/* Two decimal places, not six: the price moves by whole ENC a second at
          this scale, so the tick is visible without setting a headline in
          micro-units. The exact figure is one hover away, and it is the same
          number the chain settles against. */}
      <p className="gz-price" title={`The auction reserve, exactly: ${formatEnc(view.price)} ENC`}>
        {formatEnc(view.price, { fractionDigits: 2, padFraction: true })} <span>ENC</span>
      </p>
      <p className="gz-price-note">
        {formatShare(view.price, supply)} of all the money there is · {travelling(view)}
      </p>

      <div className="gz-body">
        {view.spiked ? (
          <Redacted />
        ) : view.copy === null ? (
          <p className="gz-copy gz-copy-default">{EMPERORS_DEFAULT_COPY}</p>
        ) : (
          <p className="gz-copy">{view.copy}</p>
        )}
        <p className="gz-byline">
          {view.spiked
            ? 'Struck by the editor, this edition.'
            : view.copy === null
              ? 'Never written in.'
              : view.copyFiled
                ? 'Filed this edition.'
                : 'Standing from an earlier edition.'}
        </p>
      </div>

      <dl className="gz-facts">
        <div>
          <dt>Held by</dt>
          <dd>{view.heldByEmperor ? 'The Emperor' : shortAddress(view.holder.toBase58())}</dd>
        </div>
        <div>
          <dt>Term {view.termNumber.toString()}</dt>
          <dd>
            {view.termEnded ? (
              <span className="gz-due">
                ended — anyone may {view.nextAction === 'settle' ? 'settle it' : 'roll it'}
              </span>
            ) : (
              `ends in ${formatDuration(view.secondsToTermEnd)}`
            )}
          </dd>
        </div>
        <div>
          <dt>Standing bid</dt>
          <dd>
            {view.highBidder === null ? (
              'none'
            ) : (
              <>
                {formatEnc(view.highBid)} ENC{' '}
                <span className="gz-bidder">by {shortAddress(view.highBidder.toBase58())}</span>
                {!view.bidClearsReserve ? (
                  <span className="gz-under"> · under the reserve</span>
                ) : null}
              </>
            )}
          </dd>
        </div>
      </dl>

      <Counter view={view} actions={actions} />
    </article>
  )
}

export function AssetGrid({
  assets,
  config,
  vault,
  supply,
  now,
  actions,
}: {
  assets: (EncAsset | null)[]
  config: EncConfig
  vault: PublicKey
  supply: bigint
  now: number
  actions: EncActions
}) {
  const views = assets
    .map((asset) => (asset ? assetView(asset, vault, now) : null))
    .filter((view): view is AssetView => view !== null)
    // Dearest first: the masthead is always the masthead, because every sync
    // rescales all ten by the same factor and the ratios were fixed at genesis.
    .sort((a, b) => b.index - a.index)

  const dateline = new Intl.DateTimeFormat('en-GB', {
    timeZone: 'America/New_York',
    weekday: 'long',
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  }).format(new Date(now * 1_000))

  return (
    <section className="enc-gazette" aria-label="The Imperial Gazette">
      <header className="gz-masthead">
        {/* Never "a currency that only goes up", which is what this line used
            to say: it is the one claim the design pre-commits to never making
            (§4 of the architecture decision), M2 fell in 6.1% of months in the
            record, and the page below already explains that a bid can end up
            under its own reserve. The true version is the better line anyway —
            the prices are a fixed share of the money supply, so a release
            raises the cost of a column by exactly the printed rate. */}
        <p className="gz-rule">Ten columns · sold by the month · when they print, the price of speech prints too</p>
        <h2>The Imperial Gazette</h2>
        <p className="gz-dateline">
          {dateline} · New York · circulation: everyone with an RPC endpoint
        </p>
      </header>

      {views.length === 0 ? (
        <p className="gz-empty">
          No slots have been created yet. The paper exists; nobody has set the type.
        </p>
      ) : (
        <div className="gz-columns">
          {views.map((view) => (
            <Column key={view.index} view={view} supply={supply} actions={actions} />
          ))}
        </div>
      )}

      <footer className="gz-footer">
        <h3>How this page works, stated plainly</h3>
        <p>
          <strong>The price you see is the reserve.</strong> There is not a display price and a
          secret one underneath: an auction settles against this exact number, re-read at the moment
          somebody settles it. A bid that cleared the reserve last week can sit under it by the end
          of the term, because the reserve climbs with the money supply while the bid sits still.
          That is the whole coin in one sentence.
        </p>
        <p>
          <strong>You are reading the last word, not the only word.</strong> Each column holds one
          string, and a new filing overwrites the last — so this front page shows what each slot
          says <em>now</em> and nothing that came before it. That is a limit of the page, not a
          secrecy feature. Every filing that ever happened is a transaction on a public chain, and
          anyone can read the lot back. We are not holding anything you cannot see.
        </p>
        <p>
          <strong>No key over the money; one pen over the words.</strong>{' '}
          {config.editor
            ? `An editor (${shortAddress(config.editor.toBase58())}) may strike any column to a fixed redaction marker, once per column per term. It takes no text — the pen strikes words and never authors them — and it cannot move a single token: not one ENC, not one slot, not one certificate. There is no on-chain answer to vile text, and pretending otherwise is how this gets ugly. A newspaper has an editor.`
            : 'The pen has been broken, irrevocably. Nobody can strike a column now. The paper is feral, and whatever appears above stands.'}
        </p>
      </footer>
    </section>
  )
}
