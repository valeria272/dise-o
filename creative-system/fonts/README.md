# FONTS — las cuatro voces

Archivos en `public/assets/fonts/copywriters/`. Todas de licencia abierta (SIL
OFL), así que viajan en el repo sin problema de licencia para el equipo.

| Voz | Archivo | Peso | Para qué |
|---|---|---|---|
| **IMPACTO** | `Archivo-Variable.ttf` | 658 KB | `wght 100–900` · `wdth 62–125` |
| **EDITORIAL** | `DMSerifDisplay-Italic.ttf` (+ Regular) | 71 KB | Cursiva, siempre |
| **DATA** | `IBMPlexMono-Medium.ttf` (+ Regular) | 137 KB | Versales, tracking 0,16em |
| **HUMAN** | `Caveat-Variable.ttf` | 404 KB | `wght 400–700` |

## Por qué Archivo variable y no Archivo Narrow

Archivo Narrow sólo llega a Bold (700) y tiene un ancho fijo. La variable de dos
ejes da **la misma condensada negra** y además el eje de ancho completo. Eso
importa porque el contraste condensada↔extendida sale del **mismo tipo**: una
pieza que juega con el ancho se sigue leyendo como la misma cabeza. Con dos
familias distintas se leería como dos.

Para que el eje funcione hay que declarar el rango en el `@font-face` —
`font-weight: 100 900; font-stretch: 62% 125%` — o Chrome lo clampea a 100%.

## La trampa que ya nos costó una entrega

Una fuente que Chrome rechaza **no da error**: sustituye por una serif y el
render sale con otra tipografía sin avisar. Así se rindieron 27 piezas de
Between con una serif de reemplazo (memoria `brushwell-no-cargaba-en-chrome`).

Por eso `sistema.ts` hace `document.fonts.load()` explícito de las siete caras
después de inyectar el `@font-face`. Y por eso las cuatro voces son **TTF**, no
OTF con outlines CFF.
