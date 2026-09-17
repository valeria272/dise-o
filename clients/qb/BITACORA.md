# QB Restaurant — bitácora

## 2026-09-17 — Elisabet Soto «Eli» (con Claude)

**Qué se hizo:** la **ST ANIMADA de ALL YOU CAN DRINK de la S5 (28-09, 15:00)**,
entregada en la carpeta `QB / STS` del Drive de Eli. Y de paso quedó abierto el
sistema de QB en código: `src/brand/qb.ts` con la geometría del bloque de AYCD
medida al píxel, y las fuentes de la marca versionadas.

**La pieza.** Tres capas y sólo una se mueve: la escena de fondo (manos
sosteniendo un celular en una mesa de QB) → las tres bandas de **UNLIMITED** en
versales gigantes → el cuerpo del celular recortado. Con eso la tipografía queda
*cortada por el borde y por el celular*, que es lo que pide el brief, y dentro
del teléfono no se mueve nada. El legal, el CTA y la línea complementaria van
fuera del celular.

**Lo que se produjo y lo que no.** La escena del celular en la mano **se generó**
(Nano Banana Pro, `scripts/qb-aycd-s5-escena.py`): esa foto no existe en el
material de QB. Pero **la pantalla se pidió en verde** y encima se montó, con
homografía sobre sus cuatro vértices, una gráfica hecha en Remotion con las
fuentes reales (`QB-Pantalla-AYCD`). Por eso el «POR $13.990», el degradado y el
logotipo salen exactos y no alucinados. Y el trago que se ve en la pantalla es un
close-up de **la foto real y aprobada** de la promo.

**⛔ El error de la ronda 1, y la regla que deja.** La grilla traía el comentario
«Muy parecido al de BT, busquemos otra referencia» y la ronda 1 lo ejecutó: sacó
el celular de la pieza. **Estaba tachado** —contenido ya lo había resuelto— y el
CSV de la capa viva no muestra el tachado. Regla: un comentario que **cambia el
concepto** de la pieza se verifica antes de ejecutarse; si contradice al brief,
se pregunta. Quedó en la memoria `comentarios-nativos-de-excel`.

**Dos hallazgos que corrigieron el manual:**

1. ⭐⭐ **El verde de QB no eran tres verdes: es un degradado.** Barrido píxel a
   píxel del botón de AYCD: `#354A3A` en los dos bordes y `#66886B` al centro,
   horizontal y constante en vertical. La franja de la historia y la pastilla del
   feed son **los dos extremos del mismo degradado**. El misterio estaba abierto
   desde el 15-09.
2. ⛔ **El pie de la ST de AYCD no es Bell MT, es Raleway Itálica.** Bell MT es el
   pie del post de *Sunset*. O sea: la letra chica de QB **depende de la pieza**.
   Se cazó comparando el antes y el después de un render, no leyendo el manual.

**Dónde quedó:**
- `src/brand/qb.ts` — el sistema medido: paleta, degradado del botón, geometría
  del bloque de AYCD, cargador de fuentes y verificador
- `src/compositions/qb/QBStAycdS5.tsx` — la historia
- `src/compositions/qb/QBPantallaAycd.tsx` — la gráfica del celular
- `src/QbEntry.tsx` — entry point de la marca
- `scripts/qb-aycd-s5-escena.py` · `scripts/qb-aycd-s5-montar.py` ·
  `scripts/qb-aycd-limpiar-foto.py`
- `public/assets/hilton/qb/` — logo recortado, Raleway, y las capas de la pieza
- `out/qb/rev/index.html` — el antes/después de las dos rondas
- Drive: `QB / STS` → el mp4 y el fotograma a 2250×4000

**Abierto:**
- ⭐ **¿La historia va a paid?** Se compuso como orgánica: el pie con el legal
  entra en los 340 px que Instagram reserva abajo, igual que el KV aprobado, que
  tampoco pasa. Si va a pauta hay que subir el pie
- Las bandas de UNLIMITED quedaron **sólo en la mitad de arriba**: el mate del
  frente es únicamente el teléfono, porque la mano no se aísla limpio. Si Eli
  quiere tipografía también abajo, hay que rehacer la escena con las manos más
  abajo en el encuadre
- Sigue sin resolverse de dónde sale **PANTONE 361 C**, que el `.ai` declara y es
  más brillante que los dos extremos del degradado
- Sigue pendiente la **decisión sobre las cifras** (caja alta en Raleway vs Bell MT)


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
