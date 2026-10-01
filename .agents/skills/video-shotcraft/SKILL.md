---
name: video-shotcraft
description: Biblioteca de 157 fichas de movimiento con parámetros medidos y demo en TSX de Remotion (cámara, tipografía cinética, transiciones, ritmo, efectos, aperturas y cierres), más el método para cortar al beat medido con librosa. Úsala cuando un reel necesite un movimiento concreto ("crash zoom", "texto que entra palabra por palabra", "transición al beat", "glitch", "push-in"), cuando haya que elegir el vocabulario de movimiento de un hook, o cuando haya que sincronizar cortes con la música. De la ficha se toma SOLO el movimiento; tipografía, color y material salen de la marca.
---

# video-shotcraft (adaptación COPYLAB para reels 9:16)

Origen: [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)
(Apache-2.0). Las fichas están en chino; el **índice en español** está en
[`INDICE.md`](INDICE.md). El SKILL original (promos de producto 16:9 con la plantilla
Ink Press) queda en `ORIGINAL-SKILL.md` solo como registro: **acá no se usa la
plantilla ni el export a JianYing** (no sirve con CapCut internacional; para CapCut
está `scripts/capcut_hook_reel.py` + el servidor VectCutAPI).

## Cómo se usa: ficha suelta

1. **Lee primero la marca.** `clients/<marca>/CLAUDE.md`, `APRENDIZAJES.md` y
   `marca.json`. La ficha aporta el movimiento; la marca, todo lo demás.
2. **Busca la ficha en `INDICE.md`** por intención (hook, transición, cierre, ritmo…)
   y energía. Abre `references/shots/<categoría>/<ficha>.md`.
3. **Lee las secciones** 意图 (intención), 动效核心 (núcleo del movimiento), 参数表
   (parámetros) y 踩坑 / 常见问题 (errores conocidos). Respeta los parámetros
   medidos (frames, escalas, curvas): son la razón de que la ficha funcione.
4. **Abre el demo** en `demos/<categoría>/` como referencia de implementación. Reescríbelo
   como componente propio en `src/compositions/...` con las fuentes y colores de la
   marca; nunca copies los colores, textos ni texturas del demo (las texturas no se
   instalaron).
5. **Pásalo a 9:16.** Las fichas están pensadas en 1920×1080: reescala posiciones y
   radios al cuadro 1080×1920 y respeta las zonas seguras de Reels/TikTok (ver
   `short-form-video`). Un movimiento horizontal amplio en vertical suele necesitar
   recorrer el eje Y o reducir amplitud.
6. **QA:** render de frames clave (`npx remotion still`) y revisión frame a frame del
   tramo animado antes de entregar.

## Cortar al beat

`references/music-beat-sync.md`: detectar el tempo real (no el BPM declarado),
separar bombo/caja/hi-hat y verificar **en el video terminado** que los cortes caen
a ≤ 3 frames del golpe. Requiere Python con `librosa` y `scipy` (instalar con
`/Users/Vale/copylab-venv/bin/python3 -m pip install librosa scipy` o con `uv`).
Este método puede reemplazar la medición de beat de `scripts/capcut_hook_reel.py`.

Otros documentos útiles: `references/sound-design.md` (capas de sonido y SFX),
`references/final-review.md` (revisión final), `references/sequences/` (encadenar
fichas en secuencias).

## Reglas COPYLAB

- **Lo que Valeria o el cliente no pidió no se construye.** Una ficha es vocabulario,
  no una invitación a llenar el reel de efectos.
- Todo texto en pantalla, en español de Chile con tuteo.
- `references/shots/ATTRIBUTION.md`: las fichas reimplementan técnicas, no copian
  piezas. Mantén eso: técnica sí, imitar una pieza ajena reconocible no.
