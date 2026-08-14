//! The editor's pen. To *spike* a story is to kill it before it runs.
//!
//! **The pen strikes words; it never authors them.** This instruction takes no
//! text — the only thing it can write is `SPIKE_MARKER`, a constant compiled
//! into the program. BadCode does not get to put sentences in a column somebody
//! paid for, and the fixed marker is also the better joke: the front page grows
//! redaction bars.
//!
//! **Once per column per term.** The struck column stays struck until the term
//! rolls, which is what stops the pen becoming the opening move of the same war
//! of attrition that `file_copy`'s write-once rule exists to prevent.
//!
//! **Why a key exists here at all.** There is no on-chain answer to vile text
//! and pretending there is, is how this gets ugly. A newspaper has an editor.
//! This was never a decentralisation play: the trustless surface is the money,
//! and the pen does not touch it — the blast radius is ten columns a month, and
//! a stolen pen cannot move one token. `initialize.ts` asserts that against the
//! IDL rather than leaving it as a claim.
use anchor_lang::prelude::*;

use crate::state::*;

pub fn handler(ctx: Context<Spike>, index: u8) -> Result<()> {
    ctx.accounts.config.require_editor(&ctx.accounts.editor.key())?;

    let asset = &mut ctx.accounts.asset;
    require!(!asset.copy_spiked, crate::errors::EncError::ColumnSpiked);

    asset.write_copy(SPIKE_MARKER.as_bytes())?;
    asset.copy_spiked = true;

    msg!("asset {index}: term {} spiked", asset.term_number);
    Ok(())
}

/// Two accounts and a signer. No mint, no token account, no token program —
/// there is nothing here for a stolen key to reach.
#[derive(Accounts)]
#[instruction(index: u8)]
pub struct Spike<'info> {
    pub editor: Signer<'info>,

    #[account(seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,

    /// Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack
    /// frame. See the note in `place_bid.rs`.
    #[account(mut, seeds = [ASSET_SEED, &[index]], bump = asset.bump)]
    pub asset: Box<Account<'info, Asset>>,
}
