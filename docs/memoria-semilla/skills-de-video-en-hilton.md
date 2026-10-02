---
name: skills-de-video-en-hilton
description: "Eli 02-10-2026 — usar por iniciativa propia las skills de reels, Remotion y Figma (instaladas el 01-10) en todo video, pieza animada y grilla de Hilton; qué skill para qué y qué no tocan"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 014fe5c4-2560-44cc-960a-aa0f2ced0489
  modified: 2026-10-02T12:52:33.871Z
---

En todo reel, pieza animada o grilla de Hilton (DT, QB, Between, Piso 18) se cargan las skills nuevas **sin que Eli lo pida**, antes de armar. El listado completo vive en el `CLAUDE.md` del repo; acá va cómo se aplican a Hilton.

**Why:** Valeria las anunció por Slack el 02-10-2026 (instaladas el 01-10, Remotion con plan pro) y Eli pidió guardarlo «para hacer mejores videos y grillas». Están en `.claude/skills/` y `.agents/skills/`, llegan con el repo: no hay nada que instalar.

**How to apply:**

- **Reel (QB DJ/Sunset, Between, Piso 18):** `short-form-video` (hook en el frame 1, cortes irregulares, zonas seguras, loop) + `tt-hook-scripter` / `viral-hooks` para el primer segundo.
- **Un movimiento concreto o corte al beat:** `video-shotcraft` (157 fichas, índice en `INDICE.md`; el corte al beat se mide con librosa). Se toma SÓLO el movimiento.
- **Subtítulos palabra a palabra:** `caption-animation`, con fuentes y colores de la marca.
- **Markup, render y captions en Remotion:** `remotion-markup`, `remotion-render` (siempre en local), `remotion-captions`; planificación de escena con `motion-designer`; proceso de video con `ffmpeg`.
- **¿Nos subimos a un trend?** `tt-trend-mapper` (pauta 0–8, se sube con 6+). Mecánica de Reels: `viral-instagram-reels`.
- **Variantes de pauta:** `ad-creative-video`, respetando [[paid-media-zonas-seguras]].
- **Figma:** `figma-use` antes de cualquier `use_figma`; ver [[figma-conector-como-funciona]].

**Límites que no cambian:**

- El sistema de la marca manda: tipografía, color y material salen de `clients/hilton/` y de las recetas aprobadas ([[between-reel-texto-animado-receta]], [[qb-reels-dj-en-canva-de-eli]], [[audio-y-post-de-reels]]). Una skill no reabre una receta aprobada.
- `viral-captions-and-ctas` NO se usa para escribir caption ni CTA en Hilton: el brief es de contenido ([[solo-diseno-el-brief-no-es-mio]], [[cta-solo-si-el-brief-lo-pide]]). Sirve sólo para el texto en pantalla que ya viene en la grilla.
- La música en tendencia de TikTok sale de Higgsfield, que al 02-10-2026 estaba sin autorizar en la cuenta de Eli.
- Las skills `remotion-*` son de la 4.0.532 y el proyecto está en 4.0.489; actualizar es decisión de Valeria.
- Video se entrega siempre MP4 + GIF ([[video-siempre-con-gif]]).
