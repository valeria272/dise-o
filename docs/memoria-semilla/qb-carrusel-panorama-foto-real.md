---
name: qb-carrusel-panorama-foto-real
description: "Eli 01-10 «okey, guárdalo»: carrusel de promo de QB = UNA foto real partida en panorama (G1 producto centrado, G2 la misma foto detrás de la promo); «Imagen referencial» abajo al centro"
metadata:
  type: feedback
---

Carrusel All You Can Drink de QB (FEED 06-10, C2 S1), aprobado por Eli el 01-10-2026 tras tres
rondas (r29 → r31). El cliente había dicho «tragos fuera de proporciones en la G2; G1 más simple,
muy literal con la refe» y mandó un pin de un vaso solo en la barra.

**La receta que quedó:**
- **Una sola foto REAL para las dos láminas, partida en panorama** («QB oct-31», barra de QB con un
  vaso tallado y romero). G1 = el trago; G2 = la misma foto que sigue, fuera de foco, detrás del
  bloque de la promo. Eli: «esa misma foto sirve para ambas y que sea una transición bonita».
- **El cóctel va CENTRADO en la G1** (no cargado a un lado).
- **«*Imagen referencial» abajo al centro** de la G1; si cae sobre luces, cajita translúcida sutil
  (negro 38 % + blur 6, [[boton-al-ancho-de-la-linea]]).
- El velo de la G2 parte en 0 en el borde del empalme (degradado horizontal), para que la unión
  no se note al deslizar. El bloque del KV (logo, nombre, botón, horario, legal) no se mueve.
- Si el trago de la foto real no es de la promo, se cambia SÓLO el líquido con IA dentro del mismo
  vaso, y el empalme con la otra lámina queda en foto real.

**Why:** la r29 (copa generada «basada en» la foto real + cinco tragos en fila) no era lo que Eli
quería: cuando existe una foto real que ya es la referencia, va la foto real ([[qb-fondo-desde-foto-real]]).
Sacar los tragos de la G2 resolvió el comentario de proporciones sin tener que dibujarlos bien.

**How to apply:** en un carrusel de promo de QB con portada limpia + promo, buscar primero una foto
horizontal real de la sesión que dé para las dos láminas (3:2 alcanza para 2 × 4:5). Código de
referencia: `src/compositions/qb/oct/QbFeed07Aycd.tsx` (r30–r31); estado en [[qb-octubre-2026-estado]];
criterio general en [[qb-criterio-carruseles-y-escenas]].
