---
name: tt-hook-scripter
description: "Script the first 1-3 second TikTok hook: the spoken line, the on-screen text, and the opening visual firing at once so the viewer cannot swipe. Picks a 2026 hook formula (cold-open result, pattern interrupt, number reveal, open-loop question, relatable call-out, story) by goal of completion, saves, comments, or shares. The single biggest retention lever on TikTok. Use to script a hook from a video idea. Not for the caption (use tt-caption-writer) or scrubbing a script (use tt-humanizer)."
---

> **Nota COPYLAB (adaptación local, 01-10-2026).** Esta skill viene de un repo
> público y se adaptó para el estudio:
> - **El sistema de la marca manda el CÓMO.** Tipografía, color, logo y composición
>   salen de `clients/<marca>/` (CLAUDE.md, APRENDIZAJES.md, marca.json). Lo que esta
>   skill diga de estética es orientación, nunca regla sobre la marca.
> - **Todo texto para la pieza o el cliente va en español de Chile con tuteo**, aunque
>   la skill esté escrita en inglés. Nada de voseo.
> - **No publica.** Entrega guiones, hooks y piezas; publicar es de `AGENTE SOCIAL MEDIA`.
> - Las cifras de retención o de algoritmo que cite son heurísticas del autor, no datos
>   medidos en nuestras cuentas. Los trends vivos se miden con Higgsfield
>   (`tiktok_music_trending`, `virality_predictor`, `video_analysis_create`).
> - `tt-humanizer` y `tt-caption-writer` no están instalados: en el paso humanizer, revisa a mano que la línea suene a habla chilena natural; para el caption usa `viral-captions-and-ctas`.


# TikTok Hook Scripter

Write the first 1 to 3 seconds of a TikTok video: the spoken line, the on-screen
text, and the opening visual, all firing at once. This is the single biggest
lever on the whole platform. TikTok's ranker runs on completion rate, and a
viewer decides to stay or swipe before second three. If the hook does not win,
nothing downstream gets watched.

## When to use

- User has a video idea and needs the opening to stop the scroll
- User's videos "die in the first second" and they want a stronger open
- User wants to pick a proven hook shape and fill it with their own angle
- Before filming, to lock the spoken line and the on-screen text

## What this skill produces

For one video idea, a ready-to-film hook block:

- **Spoken line** (what you say to camera in the first 1-3 seconds)
- **On-screen text** (the muted-first promise, 3 to 7 words)
- **Opening visual** (what is in frame one: result, tension, or interrupt)
- **The formula used** and its primary goal
- **A loop-close note** (how to end the video so it restarts for a rewatch)

It does not write the caption (hand to `tt-caption-writer`) or the full body
script beat-by-beat unless asked; it locks the open, which is where retention is
won or lost.

## Formulas this skill uses

| Code | Formula | Primary goal | Best for |
|---|---|---|---|
| T1 | Cold-Open Result | completion | show the finished outcome first, promise the how |
| T2 | Pattern Interrupt | completion | break the expected frame so the thumb stops |
| T3 | Specific-Number Reveal | saves | one odd, concrete number that reframes the topic |
| T4 | Open Loop Question | comments | ask the exact question the video answers |
| T5 | Relatable Call-Out | shares | a hyper-specific shared moment worth sending |
| T6 | Bold Claim, No Hedge | comments | a flat contrarian claim the comments will argue |
| T7 | Listicle Promise | saves | a numbered payoff with on-screen counters |
| T8 | Story In Medias Res | completion | drop into the peak of a real story |
| T9 | Tutorial Cold Start | saves | start step one with the result previewed |
| T10 | Trend-Ride With A Twist | shares | a trending sound bent to your niche |

Full skeletons (three layers each) in `references/hook-formulas.md`.

### Pick by goal first

| Goal | Reach for |
|---|---|
| Completion | T1, T2, T8 |
| Saves | T3, T7, T9 |
| Comments | T4, T6 |
| Shares | T5, T10 |

## Steps

**Voz:** usa la voz de la marca desde `clients/<marca>/` (manual y APRENDIZAJES). Salida en español de Chile con tuteo.

1. **Gather inputs.** The video idea, the niche/audience, the one promise the
   video delivers, and the goal (completion / saves / comments / shares).
2. **Pick the formula.** Use the goal table to shortlist, then suggest 2-3 that
   also fit the idea and let the user choose. For a trend ride (T10), hand the
   sound-fit question to `tt-trend-mapper` first.
3. **Write all three layers.** Spoken line, on-screen text, opening visual. The
   spoken line and the on-screen text MUST differ (muted-first viewing). Respect
   the 2026 rules:
   - The result or the tension is in frame one. No greeting, no logo, no zoom.
   - One specific number where the claim allows it.
   - Say it the way a person talks; read it out loud.
   - No AI vocabulary cluster (one marker is a slip; three in the hook is a
     script). Em dashes: `..` for a breath in the spoken line, at most one on
     the on-screen card.
   - No sincerity opener ("not gonna lie", "real talk") and no "Here's what
     nobody tells you" reveal bridge; say the thing.
4. **Write the loop-close note.** How the last frame should land so a rewatch
   feels natural (a rewatch is almost a second view).
5. **Humanizer pass.** Run the spoken line through the `tt-humanizer` V3
   rules to strip script tells before it ever reaches camera: AI vocab by
   density, stacked triads, reveal bridges, sincerity openers, written-not-
   spoken phrasing. Make it sayable; never insert a punch line for rhythm.
6. **Approval card.** Show: formula, the three layers, primary goal, the
   loop-close note, and an estimated hook duration.
7. **Hand off.** Offer `tt-caption-writer` for the caption and settings, and
   `tt-content-planner` if they are batching multiple hooks.

## Hard rules

Voz: la de la marca (`clients/<marca>/`), en español de Chile con tuteo. Reglas propias de esta skill:

- The hook is the first 1-3 seconds of the **video**, not the caption. Never let
  the caption do the hook's job.
- The spoken line and the on-screen text are two different jobs. Do not repeat the
  same words in both.
- Frame one shows something (result, tension, interrupt). No dead air, no intro.
- One specific number in the hook beats any adjective.
- The hook opens the loop; it never answers itself.

## Anti-patterns (skill will refuse)

- "Hey guys" / "welcome back" / "in this video" openers.
- A logo animation or slow zoom before the words start.
- Reading the caption aloud as the hook.
- Promising a result the video never shows on screen.
- ALL CAPS spoken scripts (you cannot shout for 30 seconds).
- More than one em dash, or an AI vocabulary cluster, in the on-screen text.
- A staged punch line or "The result?" reveal inserted for rhythm.
- Five stacked calls to action.

## Resources

- `references/hook-formulas.md` - all 10 TikTok hook formulas (three layers each)
- `references/algorithm-heuristics.md` - why completion and the first second rule everything
- `references/hook-anatomy.md` - the three-layer hook teardown and timing budget

## Related skills

- `tt-caption-writer` - the caption, TikTok settings, and hashtags
- `tt-trend-mapper` - check sound fit before a trend-ride hook (T10)
- `tt-humanizer` - scrub the spoken script so it sounds human on camera
- `tt-content-planner` - batch multiple hooks for the week
