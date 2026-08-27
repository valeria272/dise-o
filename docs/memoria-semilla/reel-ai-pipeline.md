---
name: reel-ai-pipeline
description: Pipeline de generación IA + ensamblado en CapCut para reels (estado y decisiones)
metadata: 
  node_type: memory
  type: project
  originSessionId: 7f0a8ad1-4501-42c1-a83e-6739dddf8722
---

Montaje para producir reels: **generar visuales con IA desde guion+referencia → ensamblar en CapCut** para remate PRO. Estado a 2026-07-16:

**Puente CapCut (funcionando):** CapCut Desktop 8.9.1 instalado, cuenta Grupo Copylab PRO. Bridge = **VectCutAPI** en `~/capcut-api` (venv propio `.venv`, `capcut_server.py` puerto 9000 + server HTTP de assets 8787). `build_scope_draft.py` arma un draft y lo guarda en `~/Movies/CapCut/User Data/Projects/com.lveditor.draft` (pasar esa ruta como arg para que enlace medios). Probado: genera draft válido que abre editable en CapCut. La API baja assets desde URL (por eso el server 8787). Transición "Fade" no es válida; omitir o pedir tipos válidos.

**Decisiones de generador (del usuario):**
- **Higgsfield** (plan pago, tiene Nano Banana/Sora/Veo/UGC/avatares) = generador principal. Conectado vía **conector de claude.ai** (`https://mcp.higgsfield.ai/mcp`). ⚠️ Un conector nuevo solo aparece al **abrir conversación nueva** de Claude Code.
- **Magnific/Freepik** (plan pago) = upscale/enhance/relight; pendiente que dé su API key → `~/.magnific_key`.
- **Gemini**: key en `~/.gemini_key` FUNCIONA para texto, pero imagen/video (Nano Banana/Imagen/Veo) dan **429 cuota 0 = free tier**. El usuario **NO quiere pagar** Gemini (ya paga Higgsfield/Magnific) → **no usar Gemini para generar**. `~/capcut-api/gen_image.py` existe pero bloqueado por billing.
- **Canva**: para los visuales IA de ESTE reel Valeria no la quiso (estética gráfica plana). OJO: no es veto general — hay plan pago de Canva con IA/gen. de imágenes, ver [[canva-plan-disponible]].
- Scripts Python usan certifi por el bug SSL de macOS py3.10.

**Reels Scope:** `ScopeReel2` (Remotion) es el reel premium; assets en `EDITOR VIDEOS/public/assets/scope/` (creator.mp4, screen.mp4 normalizado, music.mp3). Ver [[reel-video-gotchas]] y [[project_editor_pro_max]].

**GENERADORES PROBADOS Y CABLEADOS (2026-07-16, funcionan por terminal con certifi):**
- **Magnific imagen** (`~/capcut-api/gen_magnific.py`): `POST api.magnific.com/v1/ai/mystic`, header `x-magnific-api-key`, body `{prompt, resolution:"2k", aspect_ratio:"social_story_9_16"}` (minúsculas!), respuesta async `data.task_id` → poll `GET /v1/ai/mystic/{id}` → `data.generated[0]` URL. Usa tus créditos de plan.
- **Magnific image-to-video** (`~/capcut-api/gen_video.py`): `POST /v1/ai/image-to-video/{model}` (modelo probado `kling-v2-5-pro`), body `{image: base64, prompt, duration:"5"}`, poll `/{model}/{task_id}`. Genera MP4 5s con movimiento real. Más caro/lento (~1-2 min).
- Reel moderno de referencia = **`BravaReel`** (Remotion, `EDITOR VIDEOS`): fuentes Archivo 900 + JetBrains Mono, revelados con máscara, capa UI (timecode/marca/barra), grade. Assets IA en `public/assets/brava/`. Estilo aprobado por la usuaria ("moderno").
- Puente a CapCut para BRAVA: `~/capcut-api/build_brava_draft.py` (sirve assets en :8790, arma draft editable con clips+música+textos en la carpeta de CapCut).

**⚠️ BUG CRÍTICO de VectCutAPI — `draft_meta_info.json` hardcodeado (2026-07-17):** VectCutAPI copia un template con `draft_meta_info.json` de la máquina del AUTOR (`/Users/sunguannan/...`, `draft_name:"0707"`, `tm_duration:0`, `draft_timeline_materials_size_:2851`). CapCut Desktop LISTA los proyectos leyendo ESE archivo (no `draft_info.json`), así que el proyecto aparece **vacío: "2.7K / 00:00"** aunque `draft_info.json` esté perfecto y abra bien. Fix: `~/capcut-api/fix_draft_meta.py <carpeta_draft>` reescribe `draft_meta_info.json` con datos reales (ruta, nombre, `tm_duration`, tamaño real de assets, lista `draft_materials` type 0 desde los videos/audios de draft_info). Los builders (`build_*_draft.py`) ya lo llaman automático tras `save_draft`. Además **CapCut cachea la lista al arrancar** → hay que CERRAR y reabrir CapCut para ver drafts nuevos/modificados. Nota: esquema VectCutAPI `new_version 110.0.0` vs CapCut real `175.0.0` — funciona pero es frágil. **`basename` con rutas que tienen espacios ("User Data") rompe scripts de limpieza — cuidado al borrar drafts (una vez borré el draft recién creado).**

**Texto en CapCut vía VectCutAPI = plano/feo/fuera de margen** (fuente por defecto, `font_size` chico, posición por `transform_y` cruda). NO reproduce la tipografía buena. Regla: la tipografía premium (Montserrat + Cormorant itálica, revelados) va SOLO en el MP4 de Remotion; el draft de CapCut se entrega LIMPIO (clips + motion + música, sin texto) para que se estilice con las herramientas propias de CapCut.

**Música de reels:** de la librería online de CapCut NO se puede extraer por terminal (licenciada/streaming). Alternativas: (a) extraer el audio de los reels fuente del cliente con ffmpeg (`-vn`, detectar voz vs música con `silencedetect`) — on-brand y sin líos de licencia; (b) mp3 cacheados en drafts previos (`~/Movies/CapCut/.../assets/audio/`). Reel Tierra Calma usa la música de su propio reel `r-10-06.mp4` (instrumental continua desde 1.8s), muxeada al MP4 con `afade` in/out.

**Reel de bienvenida Tierra Calma (cliente nuevo, parcelas Padre Hurtado):** `TierraCalmaReel.tsx`. Fuentes AUTO-HOSPEDADAS (ver [[reel-video-gotchas]]). Logo = su MOTION oficial `TIERRA CALMA MOTION.mov` (qtrle/argb, fondo se funde a blanco → compuesto sobre blanco = `tc_motion.mp4`). Navy oficial `#14314C`, verde del JPG `#224E44`. Assets en `public/assets/tierracalma/`.

**Yo (Claude) llevo el criterio** de qué modelo/plataforma usar por escena y qué llevar de una a otra para el ensamblado final.
