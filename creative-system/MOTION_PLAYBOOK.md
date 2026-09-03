# MOTION PLAYBOOK

> Los reels tienen **dirección**, no fórmula.
> Nunca por defecto: HOOK → 3 BULLETS → CTA.

---

## Los números

- **Duración:** 6–20 s. Casi siempre más cerca de 12 que de 20.
- **Primer impacto:** 0–1,5 s. Si a los 1,5 s no pasó algo, el reel ya se perdió.
- **Formato:** 1080×1920 · 30 fps.
- **Zonas seguras:** 250 arriba · 340 abajo · 115 derecha. El margen derecho de
  la marca en 9:16 es **155 px**.

## El repertorio

hard cuts · macro photography · encuadre inesperado · tipografía cinética ·
**silencio** · sound design · transiciones rápidas · remate visual.

El silencio es una herramienta, no un error. Un corte a negro de 0,4 s con la
banda cortada de golpe hace más que cualquier transición.

## Lo que no se hace

- Transiciones de plantilla (zoom-blur, glitch de preset, whip-pan genérico).
- Texto que aparece letra por letra «porque queda bonito». Si no hay una razón
  de lectura, aparece de una.
- Sobreproducir. Un reel de 6 planos bien elegidos gana a uno de 20.
- Barras de progreso, flechas de «desliza», contadores decorativos.

## Estructura de referencia

```
0:00   TODOS ESTÁN USANDO IA.          ← tipografía a sangre, sin música
0:02   imagen absurda: cien outputs idénticos
0:04   ESE NO ES EL PROBLEMA.
0:06   rostro / detalle / corte duro
0:08   EL PROBLEMA ES QUE SE NOTA.
0:11   negro · COPYWRITERS
```

El cierre es **uno de los cuatro casos** en que el logo está permitido
(`COPYWRITERS_CREATIVE_OS.md` §7).

## El cover

Un cover tiene dos trabajos a la vez y **si sólo cumple uno, está mal hecho**:

1. ser el primer fotograma del reel,
2. ser una baldosa de la grilla del perfil.

Instagram recorta el 9:16 a 4:5 centrado en el perfil. Se comprueba antes de
exportar: hay que mirar el recorte, no el archivo completo.

Ejemplo trabajado: `src/compositions/copylab/ReelCover.tsx`.

## Producción

- **Tipografía y composición:** Remotion, con el mismo motor que los estáticos
  (`src/brand/copylab/`). Las cuatro voces y la paleta son las mismas: un reel
  que no comparte tipografía con el feed es otro sistema.
- **Video generado:** Freepik/Magnific hace **image-to-video** (Kling 2.1,
  Hailuo, Wan, Pixverse) — `scripts/magnific-video.py`. Está incluido en el plan
  que ya se paga.
- **Personaje G.CL en movimiento:** SÓLO image-to-video desde un keyframe
  aprobado, clips de 3–6 s. Nunca text-to-video (candado 4 de la biblia).
- **Audio:** nada de ruido blanco ni ducking por envolvente. Para la voz,
  MMSE-LSA (memoria `audio-y-post-de-reels`).

## Render en este Mac

El repo vive en iCloud y el equipo corre macOS 14: hay que usar el sandbox y el
Chrome del sistema, o el render muere sin escribir nada en el log.

```bash
SB=/private/tmp/clrender   # ver la receta completa en la memoria render-remotion-fix-mac
./node_modules/.bin/remotion render CL-<Comp> out/x.mp4 \
  --browser-executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```
