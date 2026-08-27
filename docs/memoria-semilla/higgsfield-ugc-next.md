---
name: higgsfield-ugc-next
description: Handoff — test UGC avatar OPPO Reno16 con Higgsfield; estado, guión, correcciones pendientes
metadata:
  node_type: memory
  type: project
  originSessionId: 7f0a8ad1-4501-42c1-a83e-6739dddf8722
  modified: 2026-07-21T13:22:07.380Z
---

**RETOMAR EN CHAT NUEVO (2026-07-20):** test de **avatar UGC para OPPO Reno16**.

**Conexión Higgsfield:** el conector claude.ai está CONECTADO (verificado en claude.ai → Connectors, `https://mcp.higgsfield.ai/mcp`, permisos "Requiere aprobación"). PERO Claude Code congela el set de conectores al inicio de cada conversación → **este chat viejo nunca lo carga aunque se reabra la app**. Solución: **abrir conversación NUEVA** y verificar con `ToolSearch "+higgsfield"`. Balance: **1140 créditos** (plan Plus). Los generados quedan en la cuenta Higgsfield → `show_generations` / web *Generations*.

**Contexto:** propuesta de **Copylab a OPPO Chile** para lanzar el **Reno16** (campaña "Make Your Moment", target jóvenes 18-28, US$45K, oct 2026). Fuente: `https://propuesta-oppo-reno16.vercel.app/`. Insight clave: *"no compite por especificaciones: compite por los momentos que ayuda a crear."*

**Avatar elegido:** mujer chilena ~24, rasgos latinos, hora dorada, selfie UGC. Imagen generada con **Soul (soul_2)**, variante A = job `ae5012e4-0847-4579-b468-19844a85779d` (la B era más europea, descartada). Prompt base: *"Authentic UGC selfie vertical, 24yo Chilean woman, natural Latin features, medium-brown wavy hair, minimal makeup, real skin texture, oversized cream knit sweater, holding phone selfie, Santiago street golden hour, candid half-smile, phone front-camera look, photoreal 9:16."*

**Guión (aprobado, ~11s):** "Anoche saqué esta foto. Sin flash, sin editar. Y no soy fotógrafa: solo tenía el Reno16. No gana por especificaciones… gana porque no te pierdes el momento." → cierre en pantalla **"Make Your Moment"**.

**Modelo video:** **Seedance 2.0** (1080p, 9:16, `generate_audio`, `medias` start_image). Alternativas: Kling v3.0, Minimax Hailuo (emoción facial). El 1er render fue job `7cb3153d-1bf2-4ce2-a44e-85e0fcd69ef5`.

**CORRECCIONES PENDIENTES (lo que pidió Valeria) — ASSETS YA LISTOS EN DISCO:**
1. **Que se VEA el teléfono, y MANTENERLO TAL CUAL (no modificar nada).** Referencia estilo: `instagram.com/p/DY5hkviJwE4` (selfie/espejo con el fono visible). Fotos OFICIALES del Reno16 ya descargadas en **`public/assets/oppo/reno16_blanco.jpg`** (blanco perla, dorso, 1600×883) y **`reno16_lila.jpg`** (lila, frente+dorso, 958×1183). ⚠️ Como Seedance puede deformar un producto real, para mantenerlo EXACTO conviene **cutaway/insert con la foto oficial** (Ken Burns en Remotion/ffmpeg) en el beat del teléfono, y/o pasarlas como `image_references`/`reference_elements` a Seedance — NO dejar que el modelo dibuje un fono inventado. Confirmar color con Valeria (blanco o lila).
2. **Voz CHILENA clonada.** Muestra lista: **`~/Desktop/Voz.m4a`** (49s) — copia también en **`public/assets/oppo/voz_chilena.m4a`**. Clonar con `create_voice` (o subir en Higgsfield web *Voices*), generar la VO del guión y sincronizar el avatar (Seedance `audio_references` / lip-sync).

**Flujo al retomar (todo el material ya está en disco):** (1) verificar Higgsfield conectado con `ToolSearch "+higgsfield"`; (2) subir/clonar `voz_chilena.m4a` → `create_voice`; (3) regenerar imagen de la creadora + insertar/referenciar el Reno16 real (blanco o lila) SIN modificarlo; (4) Seedance con la voz clonada + teléfono exacto → revisar acento y acting. Ver [[reel-ai-pipeline]] y [[client-welcome-reel-recipe]].

⚠️ **BLOQUEO ACTUAL:** Higgsfield NO carga en la conversación vieja (los conectores se congelan al crear el chat). Aunque en claude.ai está conectado, hay que **abrir un CHAT NUEVO** de Claude Code para que aparezca. **`/compact` NO lo arregla** (verificado 2026-07-21): compactar resume el historial pero no recrea la conversación ni reinyecta conectores. Todo lo demás ya está preparado.

**Prompt de arranque listo para pegar:** `EDITOR VIDEOS/RETOMAR-UGC-OPPO.md`. Color sugerido del fono: **lila** (única foto con frente+dorso; mejor para el inserto y para el target 18-28).
