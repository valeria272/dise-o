---
name: ebema-reel-promocional-metraje-real
description: "EBEMA — los reels promocionales de sucursal (p. ej. Zona Ofertas San Bernardo) van SÓLO con metraje real, sin IA; cómo elegir las tomas de Seba y qué gramática usar"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0633307d-aabe-4338-9c32-5d4cd298524e
  modified: 2026-09-28T20:22:46.272Z
---

**Reels promocionales de sucursal = metraje real, cero IA.** Paulina, 28-09-2026, sobre el
reel 27/10 «Ebema San Bernardo — Zona Ofertas Constructor»: «no modifiques con IA estos
videos porque este tipo de reel es más promocional, hay que conectar con el cliente y con la
gente que va a ver el video; la idea es que salgan los productos reales».

**Why:** es contenido de cercanía (personas reales, productos reales, la sucursal real). Un
plano generado rompe esa promesa. Distinto de los reels de proveedor (Aza, LP), donde la IA
sí hace escena.

**How to apply:**
- Sólo cortes del metraje (60→30 fps descartando cuadros, sin interpolar ni «mejorar»).
- **Seba (o quien muestre producto): sólo cuando MUESTRA el producto o lo acerca a cámara**,
  nunca cuando lo está dejando o recién tomándolo («eso no es llamativo»). Revisar la toma
  cada 0,25–0,5 s y elegir el tramo.
- Prioridad al lugar del brief (la Zona Ofertas Constructor = el container de productos con
  caja fallada o detalles, en oferta); bodega, sala de ventas y mostrarios valen «entre medio».
- Las tomas del iPhone vienen 3840×2160 con rotación −90 en metadatos: son VERTICALES.
- Gramática: la del reel anterior de esa misma sucursal (logo arriba a la izquierda,
  subtítulo blanco + línea en caja roja, cierre con dirección en caja roja y horarios con
  reloj) + ritmo de un corte y una etiqueta por categoría (referencia Construmart).
- Material en `raw/ebema/san-bernardo-zona-ofertas/`; «AMBIENTE MULTIUSO» es San Bernardo.
- Composición: `EbemaReelSanBernardoOct` en `src/compositions/ebema/EbemaGrillaReelsOct.tsx`.

Ver [[cliente-ebema]], [[ebema-voz-y-musica-stories]] y [[no-inventar-sistema-de-marca]].
