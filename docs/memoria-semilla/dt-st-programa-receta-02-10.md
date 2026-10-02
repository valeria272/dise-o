---
name: dt-st-programa-receta-02-10
description: "Eli 02-10 «guarda el resultado» — DT: ST de programa con adicionales dentro del panel (aprobada a la primera) y ST partida en dos fotos con la toma completa del brindis; cómo achicar un conjunto con IA para que quepa bajo el titular"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8775ecd8-4e79-4111-8f5e-aa26f9d0b001
  modified: 2026-10-02T13:47:04.860Z
---

Eli, 02-10-2026, sobre las dos historias de DT que salieron de los hilos de Carlos Figueroa
(STORIES!F10 y H10): la de Escapada con adicionales, *«me parece perfecto, me gustó cómo lo
añadiste»* (a la primera); la de Noche de Bodas, dos rondas (*«lo veo bastante bien, pero… utiliza
esa toma: las flores, la botella de champán con las copitas»*, con las copas servidas) y después
*«guarda el resultado en tu memoria»*.

**Why:** quiere que las próximas historias de programa de DT salgan así, sin rondas de más.

**How to apply:**

1. **Tomar la grilla sin preguntar** ([[octubre-ok-para-disenar-se-toma]]): hilos con `includeComments`,
   estado en vivo por Sheets API, cruce con Drive por md5 (el token ya trae `drive.readonly`). Sólo
   se hace lo que no tiene pieza o cambió de brief; avisar el tiempo antes de partir.
2. **Adicionales de un programa (sunset, masajes) van DENTRO del mismo panel azul**, bajo las
   píldoras, en filas separadas por filetes y escritos como en el carrusel aprobado: «Agrega…» a un
   peso (Stag Medium), precio en Trade Cn con «+» en todos, punteo en Stag con punto final. El panel
   crece hacia abajo hasta la zona segura (cierra ≤ 1566) y lo de arriba se aprieta un punto
   («IVA INCLUIDO» al lado del precio); titular, foto y ancho del panel NO se mueven. Variante nueva
   del componente, la anterior intacta (`DtStFeriadoErAdicionales` en `DtStFeriadoOct.tsx`).
3. **ST «dividida en 2»** (`DtStNocheBodasOct.tsx`): corte seco entre dos fotos; arriba logo +
   titular centrado y la toma del producto; abajo la segunda foto con el programa en panel azul
   (nombre del programa en Stag itálica a dos pesos, precio, píldoras, botón con el CTA del brief,
   legal). El panel tapa la zona muerta de la foto de abajo (la ventana) y deja el sujeto (pétalos)
   justo bajo él.
4. ⛔ **Historias que salen en SECUENCIA se ven iguales: logo y titular en BLANCO**, con el mismo velo azul
   (`Velo` pie 0,72, lado arriba) y la misma sombra de las hermanas. Eli, ronda 3: «deja el texto y logo en
   blanco… ya que es una secuencia, no debe verse diferente». Yo los había puesto en azul DT sin velo porque
   la pared era clara (lo que dice el manual para foto clara): en una pieza suelta vale, **en una secuencia
   manda la coherencia con las otras**. Antes de entregar, poner la pieza al lado de sus hermanas de la semana.
5. **«La toma» es el conjunto completo, no un acercamiento.** Si contenido deja una foto con flores,
   botella y copas, Eli quiere verlas todas, y las copas SERVIDAS (la IA las llena).
6. **Cuando el conjunto no cabe bajo el titular** (foto vertical a lo ancho de la historia):
   pedirle a Nano Banana «en la mitad / el tercio de abajo» NO lo achica (sale siempre a ~65 % del
   alto). Funciona en dos pasos: (a) tirada con el cambio de contenido (copas servidas, sin la
   lámpara que caía detrás del titular); (b) esa tirada pegada A MEDIDA en un lienzo (62 %, abajo al
   centro, bordes estirados y borrosos) y la IA **sólo integra** pared y mesa, «no muevas ni agrandes
   ningún objeto». `scripts/dt-oct6-nb-brindis.py <n> integra`. Después medir el tono de la pared
   contra la foto original (salió magenta; verde ×1,08) y correr la foto para que nada vertical
   (cortina) toque el titular.
7. **Entrega en el mismo turno:** QA `qa/motor.py --marca hilton`, Drive con md5, HTML de
   antes/después abierto en Chrome, dudas abajo (texto raro del brief se deja literal y se avisa).

Relacionado: [[dt-octubre-2026]], [[ronda-de-hilos-receta-aprobada]], [[carrusel-objeto-repetido-es-el-mismo]],
[[dt-titulos-de-historia-y-legibilidad]], [[la-tinta-la-manda-el-fondo]], [[dos-sesiones-mismo-arbol]].
