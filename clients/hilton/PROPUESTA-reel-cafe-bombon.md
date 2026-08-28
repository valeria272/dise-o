# BETWEEN · Reel Café Bombón (7 de septiembre) — respuesta a la pregunta del cliente

> **Estado en la grilla:** pasó de `EN REVISIÓN` a **`OK PARA DISEÑAR`** el 27-08-2026.
> **Pregunta del cliente (STORIES · H15):** «Cómo mostraremos la leche condensada al principio?»
> **Interacción pedida (H12):** LINK CARTA.

Esta es la única pieza de la grilla que quedó fuera de la ronda de correcciones
del 27-08: es un **reel animado**, no una pieza estática, y el propio cliente
dejó una pregunta abierta que conviene cerrar antes de producir. Se responde
primero, se produce después.

---

## La pregunta, y por qué es una buena pregunta

El brief dice, en la escena 1:

> «Desde lados opuestos entran gráficamente los dos protagonistas: café y leche
> condensada.»

El café se representa solo: un chorro oscuro, una taza, unos granos. **La leche
condensada no.** Si se muestra el tarro, entra una marca de tercero en cuadro —
y en el 90 % de los casos es una marca que Between no vende ni quiere promocionar.
Si se muestra un vaso de leche, se lee como leche normal y se pierde el chiste
(«ELLA: DULCE»). Ese es el problema real detrás de la pregunta.

## Tres caminos, con lo que cuesta cada uno

### A. El hilo de leche condensada cayendo — **la recomendada**

Sin envase. Entra por el borde superior izquierdo un **hilo denso, blanco marfil,
que cae lento y se enrosca** al llegar al fondo del vaso, formando la primera
capa. La densidad se lee sola: la leche condensada cae distinto a la leche —más
lenta, más gruesa, con el pliegue característico.

- **Por qué:** resuelve el «desde lados opuestos» del brief sin meter ninguna
  marca ajena, y el contraste con el chorro de café (oscuro, líquido, rápido)
  es lo que hace la gracia de la escena 2.
- **Cómo se produce:** se filma o se genera el hilo sobre fondo neutro y se
  compone. Es el plano más caro de los tres, pero es el que se ve premium.

### B. La cuchara que se vuelca

Una **cuchara** entra por la izquierda cargada de leche condensada y se vuelca
sobre el vaso. Mantiene el gesto «entra por un lado», no necesita envase y es
mucho más barata de producir: se resuelve con un plano corto real.

- **Contra:** es menos hipnótico que el hilo y la escena 3 ya usa una cuchara
  (la que mezcla), así que el recurso se repite.

### C. El tarro, con la etiqueta fuera de foco

Sólo si el cliente quiere que se identifique el producto. **Requiere que Javier
confirme la marca que usan** y que acepte mostrarla; si no, se difumina la
etiqueta, y una etiqueta difuminada en primer plano se ve barata.

- **No la recomiendo.** Es la que más riesgo trae por la marca de tercero.

---

## Lo que hace falta para producirlo

1. **La decisión del cliente entre A, B y C** (basta un «vamos con la A»).
2. **El producto real.** El Café Bombón terminado, con sus capas, en el vaso en
   que se sirve. En el banco no hay ninguna foto suya. Dos salidas:
   - la buena: que lo fotografíen en el local, aprovechando la sesión del viernes
     que ya mencionaron para «Así se hace tu café» (STORIES · J15);
   - la de respaldo: generarlo, con el riesgo conocido de que el vaso salga sin
     marca — se corrige con `scripts/between-logo-vaso.py`.
3. **Confirmar si el vaso es transparente.** El brief dice «vaso transparente
   vacío» y es correcto para que se vean las capas, pero el vaso To Go de la
   marca es kraft opaco. Hay que saber en qué vaso se sirve realmente el Bombón.

## Lo que ya está resuelto

- La estructura (4 escenas), los textos en pantalla y el cierre vienen literales
  del brief y no hay que tocarlos.
- El sistema de animación existe: `StoryAnimada` en `BetweenSistema.tsx`.
- La interacción es LINK CARTA, y el sticker ya está hecho: `StickerEnlace`, el
  mismo que se estrenó en la story «Según mis cálculos».

## Los otros dos pendientes de septiembre, para no perderlos de vista

- **«Así se hace tu café»** (STORIES · J) sigue en `POR GRABAR`. El comentario
  —«Ok, aprovechemos el viernes de sacar estas fotos para que se vea bonito»—
  está **tachado**, o sea ya se coordinó. Se produce cuando lleguen las fotos.
- **Promociones de desayuno**, feed y story, siguen en `PENDIENTE POR CLIENTE`:
  falta la información comercial.
