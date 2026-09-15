# QB Restaurant — bitácora

## 2026-09-15 — Elisabet Soto «Eli» (con Claude)

**Qué se hizo:** Se abrió QB como marca propia del estudio, separada de Hilton, y se
midió su identidad desde los editables. Eli dictó el criterio (marca independiente,
feed minimalista y elegante, cócteles + platos + rostros, verde variable, el video da
fotograma *y* reel, ojo con los márgenes de paid) y pasó el Drive del mundo QB. Se
bajó el paquete de Illustrator **FEED QB S1 agosto**, se leyó su `Informe.txt` y se
midieron dos piezas reales: la historia `ST n°2 S3 QB` y el post `Post n°2 QB SUNSET`.

**El hallazgo del día — las cifras de Raleway.** Eli pidió «agregar OpenType tabular
porque los números se ven extraños». Medido con `fontTools`: `tnum` **no existe** en
ninguno de los 10 cortes, así que ese botón nunca hizo nada. Pero el defecto real es
otro: **las cifras de Raleway son de estilo antiguo por defecto** —el `0` no llega a
la altura de versal y el `3`, `5` y `9` bajan de la línea base—, y eso **sí** se
arregla con **cifras de caja alta (`lnum`)**, que la fuente declara. Además se
descubrió que **Bell MT tiene los diez dígitos a 0,500 em exactos**: es tabular de
fábrica y ya es fuente de QB.

**Dónde quedó:**
- `clients/qb/CLAUDE.md` — manual con el criterio dictado + identidad medida +
  gramática de historia y de feed + el aviso de paid
- `clients/qb/marca.json` — ficha con tipografías, formatos y geometría medidos
- `clients/qb/adn/FEED-QB-S1-agosto-Informe.txt` — el informe del paquete, íntegro
- `clients/qb/adn/cifras-comparacion.png` — las 4 opciones de cifra, renderizadas
- `public/assets/hilton/qb/fonts/BELL.TTF` · `BELLI.TTF` — versionadas
- Brushwell **ya estaba** y es byte a byte la misma (537 296 B): se reusa la de Between
- Material pesado en `raw/hilton/qb/` (no viaja): paquete de fuentes y 3 piezas de
  referencia. Sus IDs de Drive están en `marca.json`

**Qué sigue:** que Eli elija cómo van las cifras —caja alta en Raleway, Bell MT, o
cada una en su caso— mirando `adn/cifras-comparacion.png`. Con eso cerrada, y con el
verde confirmado, QB queda lista para producir la primera pieza en código.

**Abierto:**
- ⭐ **Decisión de Eli sobre las cifras.** Es lo único que bloquea la tipografía
- ⚠️ **El verde no cuadra.** Tres valores distintos: franja de historia `#374C3C`,
  pastilla de feed `~#66886B`, y `PANTONE 361 C` declarado en el `.ai` (más brillante
  que los dos). **Pedido a Eli: el valor del swatch como lo tiene en Illustrator**
- **Falta el Drive de fotos y sesiones** — Eli dijo que lo pasa aparte. El informe
  revela cuáles son: `SESIÓN COCTELERÍA 11-09` y `QB sesión 13-10`
- El paquete de **STORIES no trae `Informe.txt`**, y ninguno de los dos paquetes trae
  carpeta `Links/` (por eso las fotos salen como «enlaces no disponibles»)
- **¿La regla «en DT sólo diseño, el brief no se toca» aplica a QB?** Está dictada
  para DT y no se dio por extendida
- Confirmar qué significó «las promos no son sólo de bancos» (se entendió: convenios
  con tarjetas bancarias)
- Falta el logo vectorial: el único que hay es un PNG blanco dentro de un lienzo de
  historia con el 99,7 % transparente
