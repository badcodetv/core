import { ScrollComic, Page, ImageWidget, AnimationWidget, SpeechBubble, NarrationBox, createComic } from '@badcode/comic'
import manifest from './assets.manifest.json'
import { zoom } from '@badcode/comic/effects'
import { fadeOutFadeIn } from '@badcode/comic/transitions'
import { trip } from './effects'
// Recut 2026-07 — 24 slides + stinger, three movements: JUDGE (1–9) · SEE (10–15) ·
// BECOME (16–25). Locked beat list: docs/superpowers/specs/2026-07-25-camping-recut-plan.md §3.
// Per-slide records (scene, prompt, bubble script): docs/camping/storyboard/pNN.md.
// Custom effects live in ./effects.ts. See packages/comic/AUTHORING.md.

const comic = createComic(manifest)

export function CampingComic() {
  return (
    <ScrollComic progressBar pageIndicator scrollHint pageDefaults={{ background: '#0a0f1c' }}>
      {/* ── JUDGE (1–9) ─────────────────────────────────────────────── */}

      {/* 1 — The Shard. transition={null} keeps the hard cut into the opener. */}
      <Page hold={2.8} effect={zoom({ amount: 1.3 })} transition={null}>
        <AnimationWidget animation={comic.resolveAnimation('anim/a01')} />
      </Page>

      {/* 2 — Boardroom. The incantation he'll hear again on the trip. */}
      <Page hold={1.6}>
        <ImageWidget src={comic.resolve('img/i44.png')} />
        <SpeechBubble x={34.45} y={34.42} appearAt={[0, 1]} fade tail="none" fontSize={14}>
          {'Let\'s circle back to synergise our bandwidth…'}
        </SpeechBubble>
      </Page>

      {/* 3 — Lift lobby, applause. */}
      <Page hold={1.8}>
        <ImageWidget src={comic.resolve('img/i45.png')} />
        <SpeechBubble x={54.1} y={72.77} appearAt={[0, 0.5]} fade tail="none" fontSize={14}>
          {'Tarquin, you\'ve done it again. How do you do it?'}
        </SpeechBubble>
        <SpeechBubble x={50.48} y={21.76} appearAt={[0.45, 1]} fade tail="bottom" fontSize={14}>
          {'Easy. You just have to have a "Winning Mentality" (tm)'}
        </SpeechBubble>
      </Page>

      {/* 4 — The camping/glamping setup. Both halves detonate later. */}
      <Page hold={2.8}>
        <ImageWidget src={comic.resolve('img/i46.png')} />
        <SpeechBubble x={18.48} y={55.44} appearAt={[0, 0.25]} fade tail="none" fontSize={14}>
          {'What are you up to this weekend, mate?'}
        </SpeechBubble>
        <SpeechBubble x={48.48} y={72.06} appearAt={[0.2, 0.45]} fade tail="top" fontSize={14}>
          {'A retreat in Wales.'}
        </SpeechBubble>
        <SpeechBubble x={18.48} y={40} appearAt={[0.45, 0.65]} fade tail="none" fontSize={14}>
          {'What, camping?'}
        </SpeechBubble>
        <SpeechBubble x={48.48} y={25} appearAt={[0.6, 0.85]} fade tail="bottom" fontSize={14}>
          {'Glamping. There\'s a difference of about £400 a night.'}
        </SpeechBubble>
        <SpeechBubble x={64.77} y={19.68} appearAt={[0.8, 1]} fade type="thought" tail="none" fontSize={14}>
          {'He is so cool...'}
        </SpeechBubble>
      </Page>

      {/* 5 — The chimp line (answered on slide 18) and the retreat's real price. */}
      <Page hold={2.8}>
        <AnimationWidget animation={comic.resolveAnimation('anim/a02')} />
        <SpeechBubble x={35.79} y={52.55} appearAt={[0, 0.5]} fade type="thought" tail="none">
          {'Another week of impressing these morons. A chimp could do what they do.'}
        </SpeechBubble>
        <SpeechBubble x={60} y={30} appearAt={[0.5, 1]} fade type="thought" tail="none" fontSize={14}>
          {'Three grand to meet myself this weekend. Worth every penny.'}
        </SpeechBubble>
      </Page>

      {/* 6 — The car pulls in beside the tent. */}
      <Page hold={1.6}>
        <AnimationWidget animation={comic.resolveAnimation('anim/a04')} />
      </Page>

      {/* 7 — The sneer. His car straddles two bays; Bob calls it back on slide 20.
           Eyeline goes off-frame left to the tent — slide 8 answers it from inside. */}
      {/* Slow push toward his face: ends the page on the sneer rather than the car,
          and eases the marque mismatch with slide 8's SUV (see record p07). */}
      <Page hold={2} effect={zoom({ amount: 1.25, focal: [0.55, 0.3] })}>
        <ImageWidget src={comic.resolve('img/i47.png')} />
        <SpeechBubble x={30} y={25} appearAt={[0, 0.45]} fade type="thought" tail="none" fontSize={14}>
          {'Two parking spaces. For that.'}
        </SpeechBubble>
        <SpeechBubble x={32} y={40} appearAt={[0.5, 0.9]} fade type="thought" tail="none" fontSize={14}>
          {'Get a job, you piece of—'}
        </SpeechBubble>
      </Page>

      {/* 8 — POV out of Bob's tent. The bookend; slide 16 rhymes with this. */}
      <Page hold={2}>
        <ImageWidget src={comic.resolve('img/i05.png')} />
        <SpeechBubble x={69.9} y={47.15} appearAt={[0.1, 0.7]} fade type="thought" tail="none" fontSize={14}>
          {'At least acknowledge we\'re getting rained on by the same shitty weather.'}
        </SpeechBubble>
      </Page>

      {/* 9 — Bob. One crash, two meanings. Slide 23 rhymes with this framing. */}
      <Page hold={2.2}>
        <ImageWidget src={comic.resolve('img/i07.png')} />
        <SpeechBubble x={18.89} y={39.06} appearAt={[0.1, 0.8]} fade type="thought" tail="none" fontSize={14}>
          {'I remember 2008 like it was yesterday. The crash. Everyone lost something — I lost her.'}
        </SpeechBubble>
      </Page>

      {/* ── SEE (10–15) ─────────────────────────────────────────────── */}

      {/* 10 — Forest road. */}
      <Page hold={1.4}>
        <AnimationWidget animation={comic.resolveAnimation('anim/a06')} />
      </Page>

      {/* 11 — The retreat, in one page: Moonwhisper's pitch, his contempt for it,
           and the promise the medicine actually keeps. (v1 split this across two
           near-identical yurt frames — a scroll stall; merged in review.) */}
      <Page hold={3}>
        <ImageWidget src={comic.resolve('img/i11.png')} />
        <SpeechBubble x={63.55} y={22.29} appearAt={[0, 0.35]} fade tail="none" fontSize={14}>
          {'I\'m Moonwhisper Ascending. I am here to cleanse my soul, also to do research for my new book called "The Wound That Teaches."'}
        </SpeechBubble>
        <SpeechBubble x={44} y={40} appearAt={[0.35, 0.68]} fade type="thought" tail="none" fontSize={14}>
          {'I should have brought Daddy\'s hunting rifle…'}
        </SpeechBubble>
        {/* off-frame facilitator — kept away from Moonwhisper's corner so it reads as a different voice */}
        <SpeechBubble x={26} y={86} appearAt={[0.68, 1]} fade tail="none" fontSize={14}>
          {'Drink deep. The medicine finds whatever you brought with you.'}
        </SpeechBubble>
      </Page>

      {/* 13 — It kicks in. */}
      <Page hold={1.8} effect={trip()}>
        <AnimationWidget animation={comic.resolveAnimation('anim/a08')} />
        <SpeechBubble x={15.47} y={75.02} appearAt={[0.1, 0.8]} fade type="thought" tail="none" fontSize={14}>
          {'Fuck me, that kicked in quick!'}
        </SpeechBubble>
      </Page>

      {/* 14 — THE VISION. He meets himself, exactly as advertised. */}
      <Page hold={3.2} effect={trip()}>
        <ImageWidget src={comic.resolve('img/i35.png')} />
        <NarrationBox x={80} y={20} appearAt={[0.15, 0.45]} fade>
          {'You came here to meet yourself.'}
        </NarrationBox>
        <NarrationBox x={22} y={86} appearAt={[0.45, 0.75]} fade>
          {'He\'s been outside Waitrose the whole time.'}
        </NarrationBox>
        <NarrationBox x={78} y={88} appearAt={[0.8, 1]} fade fontSize={14}>
          {'Let\'s circle back.'}
        </NarrationBox>
      </Page>

      {/* 15 — Asleep on the forest floor, filed like a parking bay. */}
      <Page hold={1.8}>
        <ImageWidget src={comic.resolve('img/i36.png')} />
      </Page>

      {/* ── BECOME (16–25) ──────────────────────────────────────────── */}

      {/* 16 — He wakes. Hard cut (transition={null}); slide 8's shot, dead car, W-AI-trose. */}
      <Page hold={2.2} transition={null}>
        <ImageWidget src={comic.resolve('img/i37.png')} />
        <SpeechBubble x={25} y={20} appearAt={[0.5, 1]} fade type="thought" tail="none" fontSize={14}>
          {'…Wales. I was in Wales.'}
        </SpeechBubble>
      </Page>

      {/* 17 — The mechanism, at his feet. */}
      <Page hold={1.8}>
        <ImageWidget src={comic.resolve('img/i18.png')} />
      </Page>

      {/* 18 — He was right about the chimp. That's the horror. */}
      <Page hold={2}>
        <ImageWidget src={comic.resolve('img/i19.png')} />
        <SpeechBubble x={52.68} y={21.39} appearAt={[0.1, 0.5]} fade type="thought" tail="none" fontSize={14}>
          {'I said a chimp could do it.'}
        </SpeechBubble>
        <SpeechBubble x={30} y={35} appearAt={[0.55, 1]} fade type="thought" tail="none" fontSize={14}>
          {'It didn\'t even need the chimp.'}
        </SpeechBubble>
      </Page>

      {/* 19 — The car park, now a city. */}
      <Page hold={1.6}>
        <AnimationWidget animation={comic.resolveAnimation('anim/a10')} />
      </Page>

      {/* 20 — Bob returns the two-spaces observation, without malice. */}
      <Page hold={2.8}>
        <ImageWidget src={comic.resolve('img/i21.png')} />
        <SpeechBubble x={17.89} y={24.98} appearAt={[0, 0.35]} fade tail="none" fontSize={14}>
          {'Cold ain\'t it? Haven\'t seen you in some time.'}
        </SpeechBubble>
        <SpeechBubble x={15.64} y={45.81} appearAt={[0.35, 0.65]} fade tail="none" fontSize={14}>
          {'You parked next to me once, I think. Big black thing. Took two spaces.'}
        </SpeechBubble>
        <SpeechBubble x={80.69} y={34.57} appearAt={[0.65, 1]} fade tail="none" fontSize={14}>
          {'I don\'t know what to do. For the first time in my life, I genuinely— …Sir. Can you help me?'}
        </SpeechBubble>
      </Page>

      {/* 21 — The name beat. The whole story is built to land this line. */}
      <Page hold={2.4}>
        <ImageWidget src={comic.resolve('img/i21.png')} />
        <SpeechBubble x={15.64} y={45.81} appearAt={[0.1, 0.6]} fade tail="top-right">
          {'Bob. My name\'s Bob, mate.'}
        </SpeechBubble>
      </Page>

      {/* 22 — Slide 5's "why is it always up to me?" gets its answer. */}
      <Page hold={2.4}>
        <ImageWidget src={comic.resolve('img/i22.png')} />
        <SpeechBubble x={15.64} y={55.24} appearAt={[0, 0.5]} fade tail="none" fontSize={14}>
          {'Don\'t show weakness — they can smell it. Blade under your pillow. This ain\'t Eton.'}
        </SpeechBubble>
        <SpeechBubble x={75} y={30} appearAt={[0.6, 1]} fade type="thought" tail="none" fontSize={14}>
          {'Nothing\'s up to me anymore.'}
        </SpeechBubble>
      </Page>

      {/* 23 — He is slide 9. No text: the composition is the line. */}
      <Page hold={2.6}>
        <ImageWidget src={comic.resolve('img/i38.png')} />
      </Page>

      {/* 24 — Badcode in the puddle. */}
      <Page hold={2.4}>
        <AnimationWidget animation={comic.resolveAnimation('anim/a13')} />
      </Page>

      {/* 25 — Stinger: the menu option he actually took, and the thanks for it. */}
      <Page hold={2.4} transition={fadeOutFadeIn()}>
        <ImageWidget src={comic.resolve('img/i39.png')} />
      </Page>
    </ScrollComic>
  )
}
