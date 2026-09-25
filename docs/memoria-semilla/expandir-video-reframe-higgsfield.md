---
name: expandir-video-reframe-higgsfield
description: Quitar el fondo desenfocado de un reel expandiendo con IA — Higgsfield reframe aleja la cámara y baja a 720p; se usa SÓLO la franja pegada al borde y el centro original 4K va encima
metadata:
  node_type: memory
  type: feedback
  originSessionId: 42989a26-f119-4b7e-ae33-ddea9e16aebd
  modified: 2026-09-25T19:31:29.118Z
---

Eli 25-09 (reel BW «La razón»): el relleno desenfocado alrededor del clip le molesta a
contenido. Agrandar el clip para tapar el borde NO sirve, porque corta el vaso y la mano.
Lo que se pide es expandir con IA, con un fondo que siga la escena.

**Why:** `mcp__claude_ai_Higgsfield__reframe` (75 créditos por 8 s) no rellena sólo el
borde: aleja la cámara (la persona queda a la mitad y se asoma la cara, algo prohibido en
Between), entrega 720p a 24 fps, dura 0,3 s menos y redibuja el texto quemado (pierde tildes).

**How to apply:**
1. Recortar el clip nítido (en ese reel: x34 y203, 2092×3434 dentro de 2160×3840) y subirlo sin el desenfoque.
2. Pasarlo por reframe a 9:16.
3. Ubicar el clip dentro de cada frame IA con template matching (escala fija, posición suavizada).
4. Recortar de la IA sólo el rectángulo del lienzo final, con el centro a ancho completo.
5. Poner encima el centro 4K, con un difuminado de 36 px en la unión.

Script: `scratchpad/bw/componer.py` de esa sesión. ⚠️ El ffmpeg de Remotion no trae
`rawvideo`, así que los frames se mandan por `image2pipe` en PNG. Entregar MP4 + GIF ([[video-siempre-con-gif]]).
Relacionado: [[between-sin-rostros-de-modelos]].
