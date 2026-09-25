---
name: ebema-voz-y-musica-stories
description: "EBEMA story animada — locución nativa es-CL (Lorenzo, edge-tts) y música ORIGINAL que pasa Paulina; los presets de Higgsfield/ElevenLabs y el audio de un video terminado fueron rechazados"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f22d10a7-1802-425a-8233-fcdc9ff10223
  modified: 2026-09-24T19:33:18.272Z
---

**24-09-2026, story animada de Click 07/10.** Paulina pidió música «como las
referencias» y locución de lo que dice la pantalla (voz masculina de ~30 años,
«comercial pero no exagerada»).

⛔ **1er intento rechazado: «quedó súper mal».**
1. Usé como música el audio de `storie_click_jun.mp4`, y ese video **trae la locución
   de julio mezclada**. Mi análisis por bandas dijo «sin voz» y estaba mal.
   **Por qué:** una pista sacada de un video terminado casi siempre trae voz o
   efectos. **Cómo aplicar:** nunca sacar la música de un video entregado. Pedir la
   pista original (Drive `EBEMA/2-referencias/musica`) o generarla.
2. Voz «Andre» (preset ElevenLabs vía Higgsfield): «como una persona de habla inglesa
   tratando de hablar en español». **Todos los presets de Higgsfield son de habla
   inglesa**, así que no sirven para locución en español.

✅ **Lo que eligió Paulina:** `es-CL-LorenzoNeural` (Microsoft, `edge-tts` en el venv),
nativa chilena. Las otras nativas que probé fueron es-MX Jorge, es-CO Gonzalo y es-US
Alonso. Antes de montar, siempre se le pasan pruebas para que las escuche: yo no
puedo juzgar el acento.

**Cómo se calza:** se alargan las ESCENAS a lo que mide cada mp3 (no se acelera la
voz); si un clip no alcanza, se ralentiza con interpolación de movimiento. Los textos
entran cuando la voz los nombra, según las pausas medidas en el mp3.
Todo está en `public/assets/ebema/grilla-oct26/story-animada/` (`mezcla.py`, `voz/`).
Ver [[audio-y-post-de-reels]].

**Ronda siguiente (24-09):** la Lorenzo neutra sonó «triste y seria», y «gift card» se
oía «jitcar». Paulina: «no apures lo que dice, enfatiza el entusiasmo». Rechazó
subirle la velocidad (+6/+12/+18 %). **Lo que aprobó:** velocidad normal, `pitch
+11Hz`, `volume +8%`, frases con «¡…!» (la entonación sube sin acelerar) y anglicismos
escritos como suenan: **«guift kard»**. Música: 15 dB bajo la voz «apenas se escucha»;
se dejó en 8 dB. Pista: `audio_fondo3.mp3` desde el segundo 8 (Drive
`EBEMA/2-referencias/musica`, hay 3 pistas de fondo).
