---
name: qb-fondo-desde-foto-real
description: En QB el fondo de una escena parte de una FOTO REAL de la sesión; la IA sólo agrega plato/trago/gente lejos. Terraza generada = «no se parece a QB»
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8597972c-6a6e-4b1d-843e-64948395dece
  modified: 2026-09-30T13:28:28.434Z
---

En QB, toda escena con la terraza o el salón se arma **sobre una foto real de la
sesión** (p. ej. «QB 13 oct-49» para la terraza de día, en
`raw/hilton/qb/oct-r19/`), recortada al formato. A Nano Banana se le pide
**sólo agregar** lo que falta (el trago, el plato de la carta, invitados lejos y
desenfocados) y «no rediseñar nada». Si hay que dejar mesa libre para el texto,
se sube la foto y se extiende **la misma mesa** por outpainting de esa franja.

**Why:** Eli, 30-09-2026, ST Sunset: «el fondo tiene que ser realista, igual a QB…
es uno de los mayores comentarios que llega, que no se parece a QB». Tres
terrazas generadas con la foto real de referencia seguían viéndose genéricas
(azotea, jardín, techos por la ventana). Además, extender hacia abajo una foto
que termina en el canto de la mesa inventa «otra mesa extraña», y las manos
sirviéndose no le gustaron («sin manos»).

**How to apply:** antes de generar un fondo de QB, buscar la foto real en las
sesiones (ver `clients/qb/CLAUDE.md` §5) y usarla como lienzo. La luz se deja
natural: nada de baño naranja ni «golden hour» saturado. El plato sale de la
carta real de qbrestaurant.cl (la de Terraza para la terraza). Relacionado:
[[foto-se-produce-no-se-recorta]], [[no-generar-producto-que-existe]].
