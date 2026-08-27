---
name: tierra-calma-sistema-grafico
description: "El lenguaje gráfico de las piezas de Tierra Calma — estáticos con imagen IA, dron solo para video, y los 6 elementos del sistema"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 80210faa-da68-475c-a8fa-6d323c817476
  modified: 2026-08-19T21:18:08.193Z
---

Lenguaje visual de [[tierra-calma-brand]], sacado por ingeniería inversa de las
grillas de julio y agosto 2026 del diseñador Carlos Figueroa y reimplementado en
`src/compositions/tierracalma/sistema.tsx`.

## La regla que más cuesta: los estáticos NO llevan foto de dron

Valeria, 19-08-2026, después de rechazar una entrega completa:

> *"usemos las tomas de drone solo para videos y mejorando la fachada, sigamos
> usando IA para los estáticos, porque pierde visión premium"*
> *"no uses solo las imagenes de drone porque estan con nebla, haz un mix"*

**Why:** el rodaje del 07-08 fue una mañana nublada (ver
[[tierra-calma-material-dron]]). En video, con grade y movimiento, pasa. En un
estático quieto se lee "con neblina" y la marca vende parcelas premium.

**How to apply:** las fotos de los estáticos se generan con **Magnific**
(`AGENTE CREATIVO RRSS/tools/magnific.py`, key en `~/.magnific_key`), golden
hour, y viven en `public/assets/tierracalma/ia/`. Es lo mismo que hizo el
diseñador: `c-10-08-2` y `p-12-08` de agosto son IA. Para el video, correr
`scripts/tc-regrade.sh`, que baja el punto de negro y saca la calima.

## Los 6 elementos

1. **Marco** — filete blanco 1,5 px, r≈44, margen 54. **Se desplaza entre slides**
   del mismo carrusel (se abre para el logo / se va a un costado / queda en dos
   reglas). Eso es lo que hace que el carrusel se lea como un solo objeto.
2. **Logo** blanco arriba al centro, metido en el hueco del marco.
3. **Titular** — pareja fija: una línea en Inter Tight Light y el remate en
   **IvyOra Display cursiva**, casi siempre en mayúsculas (ver
   [[tierra-calma-tipografia]]).
4. **Píldora** blanca de esquinas completas, ícono de línea + texto en
   mayúsculas espaciadas.
5. **Flecha** en círculo blanco abajo a la derecha, solo si el carrusel sigue.
6. **Slide de proceso** — lavado oliva pesado + círculo con ícono de línea +
   titular en sans BOLD mayúsculas. Rompe la seguidilla de postales.

## Anti-choque: nada se posiciona a ojo

El rechazo fue por eso — íconos encima de texto, etiquetas sobre la línea del
mapa, titulares ilegibles sobre cielo quemado.

- Cada formato declara **zonas verticales que no se solapan** (logo, cuerpo,
  píldora) y el texto se apila con flexbox dentro de su banda.
- El contraste va por degradado (regla del brief), pero **el degradado solo no
  alcanza**: siempre acompañado de un velo parejo de ~0,13.
- Las etiquetas chicas van en **blanco**; la arena solo contrasta sobre crema.
- En mapas, cada hito declara de qué lado va su etiqueta, con radio de guarda
  fijo y `text-anchor` opuesto al trazado.

**Actualización 21-08-2026 — la referencia que manda ahora son las piezas de
Carlos para septiembre** (Valeria: "le quedó harto más linda y lúdica, para que
aprendas"). Guardadas en `raw/tierracalma/ref-carlos-sep2026/` y destiladas en
`clients/tierra-calma/CLAUDE.md` § "4 quater". Lo esencial: texto arriba en el
cielo y centrado; foto real del dron (gradeada) mezclada con IA de estilo de
vida; lúdico = filas de píldoras de palabra + cajas de color de marca (café
#6C473D, oliva #4A553F) + collages (tríptico, ciudad vs parcela); mapa de
cartografía real en sepia con Ruta 78 trazada (archivo guardado, base para
rehacer el nuestro); festivos en diseño plano ilustrado; logo chico y alto;
tipografía igual pero más chica y con aire. Sus piezas traen dos claims a
validar (agua potable / cabañas-Airbnb). [[tierra-calma-septiembre-2026]]
