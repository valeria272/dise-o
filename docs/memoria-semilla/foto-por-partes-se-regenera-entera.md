---
name: foto-por-partes-se-regenera-entera
description: "⭐⭐ Una foto con personas armada por partes (cara IA + cuerpo real + recortes) deja parches: la salida aprobada fue REGENERARLA ENTERA con NB Pro 4K usando el armado como referencia y reponer sólo los rótulos reales"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c1ea817e-e510-4cbf-971f-340565ade6be
  modified: 2026-09-29T13:37:23.107Z
---

Pendón cookie DT, 29-09-2026: 6 rondas de parches (mano IA con dedo de más, halos alrededor de la
mano real, fantasma del trozo viejo, emblema del muro cortado, «pegoteado», manchones). Eli: «hazla de
nuevo con la imagen… para mejorar la calidad». Se le pasó el ARMADO a Nano Banana Pro en **4K** como
referencia («re-render this exact photograph as one single clean coherent photo… keep exactly the same
composition… plain clean wall») → misma chica, misma pose, luz y desenfoque coherentes. Sólo la
etiqueta redonda salió con letras inventadas → se repuso la real calzada por SIFT (236 puntos).
Resultado: «quedó perfecto».

**Why:** cada parche pegado arrastra su propia luz, foco y borde; la IA sabe unificar una escena que
ya tiene la composición resuelta, y el ojo de Eli caza cualquier costura.

**How to apply:**
1. Armar primero la composición (qué persona, qué pose, qué producto real), aunque tenga costuras.
2. Si a 1:1 quedan costuras/fantasmas/manchas → no parchar más: regenerar la franja entera con NB Pro
   4K usando el armado como referencia; pedir fondo limpio explícito.
3. Revisar a 1:1 manos (5 dedos, pose real) y todo rótulo (R-80: la IA reescribe texto) y reponer
   desde la foto real sólo lo impreso.
4. Montar con igualación de tono en los bordes y rampas largas (~260 px a ×2).

Trampas medidas ese día: Flux expand con personas o >700 px arma collages y escribe letreros; NB con
la boca real en el lienzo pone una cara encima (dos bocas); una sola homografía no calza mano y bolsa
a la vez. Receta completa: `clients/hilton/RECETA-PENDONES-DT.md` §7.

Relacionado: [[dt-pendones-caras-nuevas]], [[personas-ia-checklist-realismo]], [[cambiar-la-superficie-no-regenerar]], [[foto-aprobada-no-se-retoca]].
