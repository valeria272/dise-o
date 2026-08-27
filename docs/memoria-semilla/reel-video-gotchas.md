---
name: reel-video-gotchas
description: Gotchas al usar clips de video reales en composiciones Remotion (frames negros)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 7f0a8ad1-4501-42c1-a83e-6739dddf8722
---

Trabajando reels con clips de video reales en el proyecto EDITOR VIDEOS (Remotion 4.0.489), dos causas de **frames negros** que costaron varias vueltas de debug:

1. **Clips de iPhone rotados / 60fps.** IMG_4501 venía 1920×1080 con `rotation=-90` y 60fps → OffthreadVideo/@remotion/media renderiza negro ~2s al inicio. **Fix:** normalizar antes de usar:
   `ffmpeg -i in.mov -vf "fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1" -c:v libx264 -crf 18 -pix_fmt yuv420p -an -metadata:s:v rotate=0 -movflags +faststart out.mp4`

2. **Video como escena ENTRANTE dentro de `<TransitionSeries>` con transiciones GL** (`linearBlur`, `crossZoom`, etc.) → la 2ª secuencia con `OffthreadVideo` (y también `@remotion/media` Video) sale negra ~2s. **Fix:** evitar TransitionSeries GL para escenas con video; usar **crossfades manuales** con `<Sequence>` solapadas + opacity + focus-pull (blur→nítido). Se ve igual de premium y es confiable. Bonus: no requiere `--gl=angle` al render.

Nota: las transiciones GL nuevas de 4.0.489 (crossZoom/dreamyZoom/filmBurn/linearBlur) SÍ requieren `--gl=angle` en render headless (si no: "Failed to create WebGL2 context").

Verificar frames negros midiendo brillo con seek PRECISO (`-ss` DESPUÉS de `-i`): `ffmpeg -i x.mp4 -ss T -frames:v 1 -vf "scale=64:64,format=gray" -f rawvideo - | od -An -tu1 | awk ...`. Ver [[project_editor_pro_max]].

3. **`delayRender()` de fuentes a nivel de módulo se CUELGA de forma intermitente en `remotion render` (video).** Cargar Google Fonts remotas con `<link>` + `delayRender` (esperando `document.fonts.load` o `document.fonts.ready`) funciona en `remotion still` y a veces en el 1er render de video, pero es POCO CONFIABLE: aborta a los ~28-58s con "delayRender was called but not cleared" (y arrastra "Could not extract frame from compositor / Request closed" en OffthreadVideo). Causa: dependencia de red bajo carga + delayRender a nivel de módulo (no per-render). **FIX DEFINITIVO probado en `TierraCalmaReel`: auto-hospedar las fuentes y NO usar delayRender.**
   - Descargar los TTF a `public/assets/fonts/` con **curl** (NO python urllib — muere por el bug SSL de macOS): variable font de GitHub `github.com/google/fonts/raw/main/ofl/<fam>/<Fam>%5Bwght%5D.ttf` (Montserrat, y la itálica variable `<Fam>-Italic%5Bwght%5D.ttf` de Cormorant Garamond). Verificar que NO sea HTML (`file -b`).
   - Inyectar `@font-face` UNA vez con `src:url(${staticFile('assets/fonts/X.ttf')}) format('truetype')`, `font-weight:100 900` (variable) y `font-display:block`; para itálica `font-style:italic`. Precargar con `document.fonts.load('800 100px Montserrat').catch(()=>{})` sin bloquear. Llamar el injector a nivel de módulo Y dentro del componente. Sin `delayRender`: los archivos locales cargan en ms y el texto recién aparece en frame ~10+, así que no hay FOUT visible. Render confiable con `--gl=angle`.
