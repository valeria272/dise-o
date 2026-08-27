---
name: abakos-brand
description: "Abakos (abakos.cl) — cliente de préstamos online; paleta, logo, fuentes, assets locales y pauta creativa"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 246beec4-fffd-4629-a8b5-40ada5a6bd4e
  modified: 2026-08-19T01:08:30.432Z
---

**Abakos** (abakos.cl) — préstamos personales 100% online en Chile, "crédito rápido y flexible en 3 pasos". Cliente de Grupo Copylab.

> ⭐ **Manual completo del cliente (fuente de verdad):** `EDITOR VIDEOS/clients/abakos/CLAUDE.md` — reglas duras, personajes con job-ids, receta de música y pipeline. Brand kit en código: `src/brand/abakos.ts`. Esta memoria es el resumen; ante conflicto, manda el manual del repo.

- **Paleta oficial** (Abakos_StyleGuide en Drive): morado `#433491` (wordmark), magenta `#EE00A8`, naranjo `#FC8222`, amarillo `#FFB533`. Estilo **flat**: sin sombras/gradientes en el logo, íconos de línea simples, nada de fondos recargados.
- **Tipografía:** Poppins (el sitio usa 300/400/500/700). TTFs locales en `public/assets/fonts/Poppins-*.ttf`.
- **Logo oficial vectorial:** `public/assets/abakos/logo.svg` (bajado de abakos.cl/logo.svg).
- **Assets IA del personaje** (Higgsfield, agosto 2026): `public/assets/abakos/fila.png` (mujer frustrada en fila de banco, soul_2, job 8a44689f-a1fd-44ad-85dc-9017ced51ea6) y `celular.png` (misma mujer en casa con el celular, nano_banana_pro con referencia). Para mantener el personaje: soul_2 genera, **nano_banana_pro edita con referencia** (soul_2 con referencia copia la escena en vez de cambiarla).
- **Composiciones:** `src/compositions/AbakosReelSeptiembre.tsx` (reel 1 "Tu tiempo también vale", split screen, 15 s) y `AbakosReelGastos.tsx` (video 2 "Septiembre tiene más gastos que días", meme 2 tiempos + lluvia de gastos, 19 s). Entregas en `/Users/Vale/Desktop/ABAKOS VIDEOS/`. Assets extra: `optimista.png`, `agobiada.png`, `dieciocho.png` (anticuchos+terremoto; ojo: la IA saca banderas incorrectas → pedir a nano_banana_pro que las reemplace por la chilena). Brief septiembre completo (incluye video 3 pendiente: carrusel 1:1 "Después del 18, ordena primero") en doc Drive `1IvrSWKrDSk7dLsV6pauUwv6ZYiZ45gz9ZBwlFx8uOQE`.
- **Carpeta Drive del cliente:** `1hpvNzI9IhfHXxXqVxvETGgCPoRIkdbt1` (subcarpeta BRANDING LOGOS/MARCA). Referencias agosto: carpeta `1wmo791dLWCkuk99ahewNK_2YSaHm5yvB` (carrusel Día del Niño + video2/video3-agosto.mp4 — los MP4 no se pueden bajar por MCP, pedirlos descargados).
- **Tono:** cercano, chileno, sin tecnicismos; mensajes ganadores en ads: rapidez, facilidad, "sin papeleos". En videos evitar logos de bancos reales. Guía de testimoniales UGC en Drive (doc `Abakos | Lineamientos para Grabación de Testimoniales`).
- **Música:** Higgsfield NO genera música (solo voz). Reel 1 = "Sounds Good" (Mixkit 1077). Reel 2 = **"Summer's Here" (Mixkit 91)**, `musica-reel2-final.mp3`, volumen 0.7. **Lección (4 iteraciones):** funk "se trababa" → Spanish Heart "muy española" → cumbias FMA (CC0 sonaba doble/saturada; CC BY exigía crédito y tampoco gustó) → al final Valeria pidió **"música normal, movida, SIN temática"** → Mixkit. Para Abakos partir siempre por Mixkit neutro-alegre. Elegir track midiendo continuidad: `afconvert` a WAV + python audioop, RMS por ventanas de 0.5 s; descartar los que tengan ventanas <35 % del promedio ("se traba"). FMA: filtrar licencia (BY-NC abunda), mp3 en JSON `fileUrl`. Pixabay bloquea scraping. No reutilizar música de otros clientes (scope/brava/tierracalma).
- **Anti-repetición de visuales:** si el mismo personaje aparece en escenas seguidas, la segunda debe tener movimiento — image-to-video con **seedance_2_5** (exige `mode: "omni_reference"` + media role `start_image`; 5 s ≈ listo en ~3 min). Clip de ella usando el teléfono: `public/assets/abakos/celular-video.mp4` (usar `OffthreadVideo` muted).
- **Un personaje por reel:** Valeria no quiere el mismo rostro en dos reels de la campaña. Reel 1 = la mujer (`fila/celular*.png`), reel 2 = el hombre (`optimista-h.png`/`agobiado-h.png`, jobs soul_2 a1cd2bab + nano_banana 37ffb029). La mujer también quedó en la portada del carrusel (`billetera.png`) — aprobado así. Ojo con las imágenes 9:16 exactas: `objectPosition` no recorta nada; para despejar la cara bajo los títulos usar `translateY + scale`.
- **Entrega:** la carpeta del escritorio se llama ahora **`REELS Y CARRUSEL/`** (Valeria la renombró desde "ABAKOS VIDEOS").
- **Video 3 listo:** carrusel 1:1 `AbakosCarruselDieciocho.tsx` (6 láminas "Después del 18, ordena primero", ids `AbakosCarrusel1..6`, stills en `ABAKOS VIDEOS/carrusel-despues-del-18/`).
- **CTAs: EXACTOS del brief** — reel 1 "Ingresa a abakos.cl y realiza tu solicitud.", video 2 y carrusel "Conoce las condiciones en abakos.cl" (ver [[ctas-verbatim-del-brief]]).

Relacionado: [[reel-ai-pipeline]], [[reel-video-gotchas]], [[client-welcome-reel-recipe]]
