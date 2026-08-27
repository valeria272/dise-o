---
name: ui-mock-anti-desborde
description: Regla dura para mocks de UI en reels (celulares, píldoras, tarjetas): escalar con el ancho de pantalla y flexShrink 0, si no el texto se sale de su caja en el formato feed
metadata:
  type: feedback
---

# Mocks de UI en reels: nunca medidas fijas dentro de una pantalla que cambia de ancho

Valeria detectó el 24-08-2026 en el reel de **EBEMA CLICK** que la píldora roja
"✓ Agregado" mostraba el texto **fuera de la caja** en el ítem "Antióxido
Maestranza" (formato feed). Dos causas, las dos típicas:

1. **`width: 120` sin `flexShrink: 0`** — al ser un ítem flex, el navegador lo
   comprime cuando el vecino (el nombre del producto) es largo, y el texto
   desborda la píldora.
2. **Medidas fijas en una pantalla que cambia de tamaño** — el mismo teléfono se
   dibuja a 492 px de ancho en story y 412 px en feed; con fuentes y paddings
   fijos el layout que calza en story se ahoga en feed.

**Cómo se hace ahora** (patrón en `src/compositions/EbemaClickReel.tsx`):
- `const k = w / <ancho de referencia>; const px = (n) => Math.round(n * k);` y
  todas las medidas de esa UI pasan por `px()`.
- Las píldoras/botones: `flexShrink: 0`, `minWidth`, `padding` lateral y
  `whiteSpace: "nowrap"` — el ancho lo manda el texto, no un número.
- El texto vecino: `flex: 1, minWidth: 0, overflowWrap: "anywhere"` para que
  corte en vez de empujar.
- Etiquetas dentro de tarjetas cuadradas: `fontSize: Math.min(px(base), tile * 0.155)`.

**QA:** renderizar el fotograma donde la UI está completa y mirarlo a zoom, en
los DOS formatos (feed y story). Ver también [[paid-media-zonas-seguras]] y
[[tierra-calma-qa-grafico]] — es la misma familia de errores de revisión.
