---
name: kling-clip-inverso-cuadro-final
description: "Técnica para que un video de IA TERMINE exacto en un cuadro aprobado: Kling anima el movimiento inverso desde ese cuadro y se reproduce al revés (Kling 2.5 Pro no acepta cuadro final)"
metadata:
  node_type: memory
  type: reference
  originSessionId: 893fcd7a-013c-4712-9b05-1ad8470efeb3
  modified: 2026-09-29T21:44:40.536Z
---

Kling 2.5 Pro rechaza `--fin` (image_tail) y Kling 2.1 Pro, que sí lo acepta, falló de nuevo el
29-09-2026 (teaser EBEMA «La Gota de Color»), como en octubre. Lo que funcionó:

1. Partir del cuadro final aprobado (p. ej. la gota flotando sobre la luz del KV).
2. Pedirle a Kling el movimiento **inverso**: «la gota sube, su punta se recoge hasta ser
   esfera, sale por arriba y la luz del piso se apaga». Una sola gota, sin chorro ni salpicadura.
3. Reproducir el clip **al revés** (`ffmpeg reverse`) + `minterpolate` a 30 fps, con rampa de
   velocidad por tramos (`trim` + `setpts=PTS/k` + `concat`).

Resultado: la acción termina en el cuadro exacto y empalma sin corte con el siguiente clip que
parte de esa misma imagen. Pedir 2 variantes: una de cada dos hace chorro o gotas extra.

**Por qué:** un recorte fijo que se desliza se ve «tosco» y fundir dos formas del objeto «se
corta» (dos rechazos de Paulina). Ver [[ebema-teaser-gota-de-color]] en el cerebro de EBEMA
(R-68) y [[reel-ai-pipeline]].

**Cómo aplicar:** cuando un objeto físico tenga que llegar a una pose aprobada (caer, posarse,
transformarse). Los efectos de sonido se eligen midiéndolos (golpes, ataque, nivel), no a ciegas.
