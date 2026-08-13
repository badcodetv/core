//! File a column. The tenant writes; nobody else does.
//!
//! The ten assets are the ten slots of a newspaper front page, and this is the
//! only instruction that puts words in one. Whoever holds the tenancy may write
//! it **once per term** — and the price of doing so rises by exactly the rate
//! the Fed prints at, which is the whole point of hanging a newspaper off a peg
//! to M2.
//!
//! **Write-once is a decision, not a rate limit.** The alternative is unlimited
//! rewrites, which turns moderation into a war of attrition that only a bot
//! BadCode ran forever could win — and running that bot would re-insert us into
//! the machine as an operational dependency, which is exactly what the rest of
//! this program is built to avoid. One filing per term makes the editor's pen
//! decisive in a single stroke instead.
//!
//! **The Emperor's columns cannot be filed at all.** A slot nobody has won is
//! held by the vault, which is a PDA with no private key, so there is no signer
//! that could satisfy the tenancy check. Those slots keep `copy_len == 0`
//! forever, and the front page renders its own default copy for them.
//!
//! No token moves here, and none can: this instruction takes no mint, no token
//! account and no token program.
use anchor_lang::prelude::*;

use crate::errors::EncError;
use crate::state::*;

pub fn handler(ctx: Context<FileCopy>, index: u8, text: String) -> Result<()> {
    let asset = &mut ctx.accounts.asset;

    require_keys_eq!(
        asset.holder,
        ctx.accounts.tenant.key(),
        EncError::NotTheTenant
    );
    // Checked before `copy_filed` so a tenant whose column was struck is told
    // that rather than "you already filed", which they did not.
    require!(!asset.copy_spiked, EncError::ColumnSpiked);
    require!(!asset.copy_filed, EncError::AlreadyFiled);

    // The bound is on **bytes**, which is what the field holds. Borsh has
    // already proved this is valid UTF-8; nothing else about the text is this
    // program's business, and pretending otherwise is the trap Ruling D names.
    let bytes = text.as_bytes();
    asset.write_copy(bytes)?;
    asset.copy_filed = true;

    // Deliberately does not log the copy itself. Transaction logs are the one
    // place text would be permanent even after a spike, and a pen that leaves
    // the struck words legible one RPC call away is theatre.
    msg!(
        "asset {index}: term {} filed, {} bytes",
        asset.term_number,
        bytes.len()
    );
    Ok(())
}

/// Deliberately thin. There is no `Config` here — nothing in this instruction
/// reads a rule — and no token accounts at all, which is what makes "the
/// Gazette cannot move money" a fact about the account list rather than a
/// promise about the handler.
#[derive(Accounts)]
#[instruction(index: u8)]
pub struct FileCopy<'info> {
    /// The tenancy holder, checked against the asset's own record.
    pub tenant: Signer<'info>,

    /// Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack
    /// frame. See the note in `place_bid.rs`.
    #[account(mut, seeds = [ASSET_SEED, &[index]], bump = asset.bump)]
    pub asset: Box<Account<'info, Asset>>,
}
