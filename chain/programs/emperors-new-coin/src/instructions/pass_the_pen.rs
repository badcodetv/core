//! Rotate the pen, or break it.
//!
//! **Rotation is the one thing that had to exist.** By T22 the upgrade
//! authority is burned, so there is no larger key to fall back on: if the
//! editor's key is lost or stolen and cannot be replaced, the paper is stuck
//! with a pen nobody good holds. `pass_the_pen` is therefore signed by the
//! current editor and hands the power to a named successor, once, atomically.
//!
//! **Breaking it is final.** `break_the_pen` sets the field to `None` and
//! nothing in this program can set it back — `pass_the_pen` needs a current
//! editor to sign, and no other instruction writes the field. After that the
//! paper goes feral: every column says whatever its tenant filed, forever, with
//! no editorial recourse at all. That is a real decision with a real cost, and
//! it is available on purpose.
//!
//! Both instructions share one account list because they genuinely need the
//! same two accounts. Neither touches a token.
use anchor_lang::prelude::*;

use crate::errors::EncError;
use crate::state::*;

pub fn pass(ctx: Context<ThePen>, new_editor: Pubkey) -> Result<()> {
    let config = &mut ctx.accounts.config;
    config.require_editor(&ctx.accounts.editor.key())?;

    // Handing the pen to the all-zero key is not "breaking" it — it would leave
    // `editor.is_some()` true while nobody on Earth could sign for it, so the
    // account would claim an editor exists when none does. `break_the_pen` says
    // that honestly; this refuses to say it by accident.
    require_keys_neq!(new_editor, Pubkey::default(), EncError::NotTheEditor);

    config.editor = Some(new_editor);
    msg!("the pen passes to {new_editor}");
    Ok(())
}

pub fn break_it(ctx: Context<ThePen>) -> Result<()> {
    let config = &mut ctx.accounts.config;
    config.require_editor(&ctx.accounts.editor.key())?;

    config.editor = None;
    msg!("the pen is broken; this paper has no editor and never will again");
    Ok(())
}

#[derive(Accounts)]
pub struct ThePen<'info> {
    /// The current editor, and nobody else. Checked in the handler so that "no
    /// pen exists" and "you are not the editor" come back as different errors.
    pub editor: Signer<'info>,

    #[account(mut, seeds = [CONFIG_SEED], bump = config.bump)]
    pub config: Account<'info, Config>,
}
