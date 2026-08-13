import {
  type AssetView,
  COPY_BYTES,
  type EncBid,
  bidCost,
  bidView,
  certificateIssuable,
  filingBlock,
  formatEnc,
  parseEnc,
  withdrawView,
} from '@badcode/enc'
import type { PublicKey } from '@solana/web3.js'
import { type ReactNode, useState } from 'react'
import type { EncActions } from './useEncActions'

/**
 * The machine, intruding on the paper.
 *
 * Every column carries one of these once a wallet is connected: the auction and
 * the Gazette's one writable field, set in the printer's monospace against the
 * newsprint, because that join is the page's whole idea. A public ledger set as
 * a front page, with a counter at the bottom of every story.
 *
 * **Every guard the program has is mirrored here before a button is offered.**
 * Not to hide the refusal — the program is the authority and its refusals are
 * mapped into English elsewhere — but because charging somebody a fee to be
 * told a thing this page already knew is rude, and because the interesting
 * answers ("your money is not stuck") are worth saying without being asked.
 */

function Row({ label, children }: { label: string; children: ReactNode }) {
  return (
    <div className="gz-counter-row">
      <span className="gz-counter-label">{label}</span>
      <span className="gz-counter-body">{children}</span>
    </div>
  )
}

/** Bid, or raise. The minimum is computed, prefilled, and explained. */
function Bidding({
  view,
  bid,
  wallet,
  actions,
}: {
  view: AssetView
  bid: EncBid | null
  wallet: PublicKey
  actions: EncActions
}) {
  const state = bidView(view, wallet, bid)
  const [text, setText] = useState('')
  const typed = parseEnc(text)
  const amount = typed ?? state.minimum
  const cost = bidCost(state, amount)
  const tooLow = typed !== null && typed < state.minimum
  const tooPoor = cost > actions.balance

  if (state.blocked === 'term-ended') {
    return (
      <Row label="Bidding">
        Closed — the term is over. It reopens the second somebody settles or rolls this column,
        which anyone may do, including you.
      </Row>
    )
  }
  if (state.blocked === 'stale-bid') {
    return (
      <Row label="Bidding">
        Blocked until you take back the escrow you left here in an earlier term. It is not stuck; it
        is just not re-entered into an auction you never chose to join.
      </Row>
    )
  }

  return (
    <Row label={state.escrowIsCurrentTerm ? 'Raise' : 'Bid'}>
      <span className="gz-counter-form">
        <input
          className="gz-input"
          inputMode="decimal"
          placeholder={formatEnc(state.minimum, { fractionDigits: 2, padFraction: true })}
          value={text}
          onChange={(e) => setText(e.target.value)}
          aria-label={`Bid on slot ${view.index}, in ENC`}
        />
        <button
          type="button"
          className="gz-do"
          disabled={actions.pending || tooLow || tooPoor}
          onClick={() => void actions.placeBid(view.index, amount).then(() => setText(''))}
        >
          {state.escrowIsCurrentTerm ? 'Raise it' : 'Bid'}
        </button>
      </span>
      <span className="gz-counter-note">
        {tooLow ? (
          <>Under the floor. The least that stands is {formatEnc(state.minimum)} ENC.</>
        ) : tooPoor ? (
          <>
            That costs {formatEnc(cost)} ENC and you hold {formatEnc(actions.balance)}.
          </>
        ) : state.escrowIsCurrentTerm ? (
          <>
            {formatEnc(state.escrowed)} ENC already escrowed here, so this moves only the{' '}
            {formatEnc(cost)} ENC difference.
          </>
        ) : (
          <>
            At least {formatEnc(state.minimum)} ENC — the reserve, and strictly over the standing
            bid. It escrows your own coin, in its own pocket, not the Emperor&rsquo;s.
          </>
        )}
      </span>
    </Row>
  )
}

/**
 * The tenant's one filing.
 *
 * Two-step on purpose: **once per term** is the design, so the page has to make
 * that final before submission rather than explaining it afterwards.
 */
function Filing({ view, actions }: { view: AssetView; actions: EncActions }) {
  const [text, setText] = useState('')
  const [confirming, setConfirming] = useState(false)
  const bytes = new TextEncoder().encode(text).length
  const overlong = bytes > COPY_BYTES

  return (
    <Row label="Your column">
      <textarea
        className="gz-textarea"
        rows={3}
        value={text}
        placeholder="Whatever you want the front page to say for a month."
        onChange={(e) => {
          setText(e.target.value)
          setConfirming(false)
        }}
        aria-label={`Copy for slot ${view.index}`}
      />
      <span className="gz-counter-form">
        <button
          type="button"
          className="gz-do"
          disabled={actions.pending || text.trim() === '' || overlong}
          onClick={() => {
            if (!confirming) {
              setConfirming(true)
              return
            }
            void actions.fileCopy(view.index, text).then(() => {
              setText('')
              setConfirming(false)
            })
          }}
        >
          {confirming ? 'Yes — file it, finally' : 'File it'}
        </button>
        <span className="gz-counter-note">
          {/* Bytes, not characters: the field is 280 bytes and an emoji is four
              of them, which is a surprise best delivered before submission. */}
          {bytes}/{COPY_BYTES} bytes
        </span>
      </span>
      <span className="gz-counter-note">
        {overlong ? (
          <>Longer than a column. It is 280 bytes, and an emoji costs four of them.</>
        ) : confirming ? (
          <strong>
            One filing per term, and this is it. There is no edit, no delete, and no second go until
            the term rolls. The editor may strike it; nobody may rewrite it, including you.
          </strong>
        ) : (
          <>
            One filing per term. No edits afterwards — that is the design, not a rate limit, and it
            is what keeps a moderation war of attrition from being winnable.
          </>
        )}
      </span>
    </Row>
  )
}

export function Counter({
  view,
  actions,
}: {
  view: AssetView
  actions: EncActions
}) {
  const wallet = actions.wallet
  if (!wallet) return null

  const bid = actions.bids[view.index] ?? null
  const escrow = withdrawView(view, wallet, bid)
  const filing = filingBlock(view, wallet)
  const certDue = certificateIssuable(view, actions.certificates[view.index] === true)

  return (
    <div className="gz-counter">
      {/* Not "the counter" — that is the wallet panel above, and two things
          with one name is one thing too many. This is the same idea in the
          paper's own furniture, and it echoes the line T19 already put next to
          the connect button: a wallet becomes useful when you want to take
          part. */}
      <p className="gz-counter-head">Taking part</p>

      {escrow.amount > 0n ? (
        <Row label="Your escrow">
          <span className="gz-counter-form">
            <strong>{formatEnc(escrow.amount)} ENC</strong>
            <button
              type="button"
              className="gz-do"
              disabled={!escrow.withdrawable || actions.pending}
              onClick={() => void actions.withdrawBid(view.index)}
            >
              Take it back
            </button>
          </span>
          <span className="gz-counter-note">
            {/* The obvious support question is "my money is stuck", and the
                answer is usually "it isn't" — so say which case this is. */}
            {escrow.fromEarlierTerm ? (
              <>
                From an earlier term, so it is <strong>free to leave whenever you like</strong>. A
                bid dies when its term rolls, whatever it was.
              </>
            ) : escrow.withdrawable ? (
              <>
                Outbid, so it is <strong>free to leave whenever you like</strong>. Nothing here is
                holding it.
              </>
            ) : (
              <>
                You are winning, which is the one thing that locks escrow in this program — and only
                until the term settles. Anyone may settle it the moment the clock runs out, so the
                lock has a permissionless exit and does not depend on us.
              </>
            )}
          </span>
        </Row>
      ) : null}

      <Bidding view={view} bid={bid} wallet={wallet} actions={actions} />

      {view.termEnded ? (
        <Row label="The clock">
          <button
            type="button"
            className="gz-do"
            disabled={actions.pending}
            onClick={() =>
              void (view.nextAction === 'settle' && view.highBidder
                ? actions.settleAuction(view.index, view.highBidder, view.holder)
                : actions.rollTerm(view.index))
            }
          >
            {view.nextAction === 'settle' ? 'Settle this term' : 'Roll this term'}
          </button>
          <span className="gz-counter-note">
            {view.nextAction === 'settle' ? (
              <>
                A bid cleared the reserve. Settling pays the outgoing holder and hands the column
                over. <strong>Anyone may run it</strong> — including you, with nothing at stake here
                — because a tenancy that only ends when the person losing it cooperates is not a
                tenancy.
              </>
            ) : (
              <>
                Nothing cleared the reserve, so the incumbent keeps it another term and any standing
                escrow is released. <strong>Anyone may run it</strong>; the instruction takes no
                signer at all.
              </>
            )}
          </span>
        </Row>
      ) : null}

      {certDue ? (
        <Row label="The receipt">
          <button
            type="button"
            className="gz-do"
            disabled={actions.pending}
            onClick={() => void actions.mintCertificate(view.index, view.termNumber, view.holder)}
          >
            Mint the certificate
          </button>
          <span className="gz-counter-note">
            You never really owned the column; all anyone keeps is the receipt. Anyone may pay for
            it and it always lands in the holder&rsquo;s wallet, never the payer&rsquo;s. One per
            term, ever, and it can never be reissued or rewritten.
          </span>
        </Row>
      ) : null}

      {filing === null ? (
        <Filing view={view} actions={actions} />
      ) : filing === 'already-filed' ? (
        <Row label="Your column">
          Filed for this term. One filing per term — the next one gets a fresh page.
        </Row>
      ) : filing === 'spiked' ? (
        <Row label="Your column">
          Struck by the editor. Nothing more goes in it this term; the next term starts clean.
        </Row>
      ) : null}
    </div>
  )
}
