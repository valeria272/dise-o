---
name: client-welcome-reel-recipe
description: Receta reusable para reels de bienvenida/caso de cliente de Copywriters (estructura, tipografía, proceso, feedback de diseño)
metadata:
  node_type: memory
  type: project
  originSessionId: 7f0a8ad1-4501-42c1-a83e-6739dddf8722
---

Valeria pide seguido **reels de bienvenida a clientes nuevos** (y casos de éxito) con la MISMA estructura reusable. Receta probada (Tierra Calma, 2026-07-17):

**Estilo (propio de Copywriters, NO plantilla):** 9:16, 30fps, ~16s. **Montserrat** con juego de grosores (fino 300 + black 800/900 en la misma frase) **+ cursiva editorial** (Cormorant Garamond itálica) para 1 palabra emotiva por beat. Revelados con máscara (blur+slide), grade cálido, grano, cortes al beat con **disolvencias suaves** (crossfade manual ~9f, NO TransitionSeries GL con video). Cierra con el **logo del cliente sin transformar** (idealmente su motion oficial) + firma [[copywriters-agency-positioning]].

**Proceso:** (1) pedir a la clienta: tomas/reels fuente + **logo oficial** (idealmente animado) + música. (2) Extraer tomas LIMPIAS (sin texto quemado) de los reels fuente; normalizar 60→30fps y quitar rotación (ver [[reel-video-gotchas]]). (3) Auto-hospedar fuentes. (4) Guion corto por beats, poco texto. (5) Render Remotion → MP4. (6) Música de su propio material. (7) CapCut LIMPIO opcional (ver [[reel-ai-pipeline]]).

**Feedback de diseño acumulado (aplicar de entrada):**
- **Constanza (líder de diseño):** los bordes del texto NO se pueden cortar (agrandar la caja de `overflow:hidden` del revelado con padding+márgenes negativos); NO saturar de tipografía ("too much") — pocos beats, alguna escena solo-paisaje.
- **Valeria:** le gusta Montserrat + cursiva con **presencia** (que no quede plano/chico); tipografía con carácter, no subtítulos estáticos; nada aplantillado "de Claude".
- Tensión Constanza (menos texto) vs Valeria (más presencia) → resolver con **pocas palabras pero bien diseñadas** (contraste de grosor fuerte, tamaño generoso en la línea-héroe, dentro de margen ~66px).
- El logo va con **SU animación oficial** si existe; no inventar animación.
- Errores hard-to-reverse: NO borrar drafts de CapCut con `basename` sobre rutas con espacios; confirmar antes de borrar.
