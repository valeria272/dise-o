---
name: qb-octubre-2026-estado
description: "QB octubre 2026 — estado al 30-09: Banco, Sunset, carrusel CMR, ST 40 % y cumpleaños; qué quedó aprobado, dónde están y cómo se resolvió cada una"
metadata:
  node_type: memory
  type: project
  originSessionId: 8597972c-6a6e-4b1d-843e-64948395dece
  modified: 2026-09-30T13:41:25.224Z
---

Estado de la grilla de QB octubre al **30-09-2026** (rondas 22–28, con Eli). Todo
está reemplazado en Drive (`S1 HILTON OCT 2026 / QB / STS` y `FEED/C1 S1
CUMPLEAÑOS`, `FEED/C3 S1 CMR`) con md5 verificado; los renders, en
`out/qb/oct/r22…r28/` con `_antes/`, y la revisión de cada ronda en
`out/qb/oct/rNN/revision-rNN.html`.

**Aprobado por Eli («okey»):**
- **ST n°1 S1 · Banco de Chile** (r23): tarjetas pegadas al legal sin solapar
  (el reflejo del PNG termina 12 px antes), foto 60 px más arriba, pie oscuro.
- **ST n°4 S1 · CMR 40 %** (r24): «Tu panorama de sábado…» en SemiBold y 50 px
  más abajo (sólo la fecha 08 del componente `QbStAprobadaCmr40`).
- **ST n°5 S1 · Sunset** (r28): foto REAL de la terraza («QB 13 oct-49») con el
  spritz de protagonista nítido, UNA Tabla Argentina (carta Terraza) desenfocada
  detrás y un rayo de sol tibio muy sutil desde la derecha. Costó 6 rondas:
  papas trufadas que no están en la carta → empanadas (no convencen) → tabla con
  manos (no) → terrazas generadas que «no se parecen a QB» → foto real.
- **C3 S1 · carrusel CMR** (r28): logo sólo en la portada; titulares de las 3
  láminas a y=200, Raleway 68; N°1+N°2 = una foto del shooting («American Baby
  ribs 11», sin la mano derecha) partida en panorama; sin degradado negro detrás
  del 40 %; los tres pies en la misma línea (y=1150). ⚠️ el legal de la N°2
  cierra en ≈1255, fuera del 12 % de feed, por pedido de Eli.

**Entregado, con el «okey» general pero sin comentario propio:** C1 S1 carrusel
de cumpleaños r27 (grilla común N°2–N°4, sólo Raleway, pie claro).

**Why:** para retomar QB sin releer la bitácora entera; detalle en
`clients/qb/BITACORA.md` (30-09).

**How to apply:** antes de tocar cualquiera de estas piezas, partir del render
de la última ronda y de su cabecera en `src/compositions/qb/oct/`. Criterio de
la ronda en [[qb-criterio-carruseles-y-escenas]] y [[qb-fondo-desde-foto-real]].
