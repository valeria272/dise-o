# Bitácora — HILTON (DT · QB · Between · Piso18)

> Una entrada por sesión, la más nueva arriba. Sirve para que otro diseñador
> retome la cuenta mañana sin preguntar nada. Se escribe en el `/cierre`.

---

## 2026-08-27 · Valeria — BETWEEN, ronda 4 del cliente resuelta

**Dónde quedó.** El cliente escribió comentarios nuevos en la grilla de
septiembre el mismo 27-08 por la tarde, después de que se entregaran las 27
piezas. Se aplicaron todos y **14 piezas están re-subidas al Drive con los mismos
enlaces**, así que quien ya tenía el link ve la versión nueva.

**Lo que se hizo, por pieza:**

| Pieza | Qué pidió el cliente | Cómo se resolvió |
|---|---|---|
| FEED 03-09 Cumpleaños G1 | más énfasis en el cumpleaños, con sus tres textos | «¿Estás de cumpleaños?» arriba, «ESTE CAFÉ ES PARA TI» de protagonista, «¡Ven por tu café de regalo!» en la caja |
| FEED 03-09 Cumpleaños G2 | el listado con emojis y más adornos | emojis a color (hubo que nombrar la fuente de emoji) y 4 adornos en vez de 2 |
| FEED 07-09 Humor cafecito | «ya no podemos usar estas modelos tal cual» | escena nueva y **sin rostro**, como la referencia que eligió el propio cliente |
| FEED 09-09 Primero la foto 1 y 2 | «fotos de cosas para comer, no de gente» | bodegones reales de la sesión de platos |
| FEED 14-09 To Go 1 | «se ve muy derrotada y el fondo no es muy Between» | sale del local sonriendo, con el interior real detrás |
| FEED 14-09 To Go 4 | dulce + salado en la foto, vaso como el resto, «¡Llévate los 3!» | bodegón con los tres productos y el titular textual |
| ST 01-09 Promo To Go | «Café con logo Between!» | logotipo real estampado sobre el vaso |
| ST 03-09 Cumpleaños | mismos textos del feed + vaso con logo | unificado con el post, misma escena |
| ST 04-09 Según mis cálculos | «Ok, enlace a carta!» | sticker de enlace nuevo (`StickerEnlace`) |
| ST 09-09 Emergencia | «no se cacha bien al tapar la vitrina» + «todas las anteriores» | rediagramada como la referencia: vitrina frontal, producto entero, texto en las bandas |
| FEED 14-09 To Go 2 y 3 | *(no lo pidió)* | ver abajo |

**El hallazgo de la sesión.** El cliente pidió que el vaso de la slide 4 fuera
«como el del resto de las slides», dando por hecho que el resto estaba bien. No
lo estaba: **la slide 3 llevaba el vaso antiguo**. La causa es que la tabla del
manual tenía las fotos **al revés** y el sufijo `-actual` de los archivos engaña
(`togo-dulce-actual.jpg` es la vieja). Ya está corregido en
`clients/hilton/CLAUDE.md § EL VASO TO GO`. De paso, las tres cajas de precio del
carrusel decían «$4.290» donde el brief dice **«desde $4.290»**; quedaron
alineadas al brief.

**Y la causa raíz de media ronda:** los generadores de imagen devuelven el vaso
To Go **sin marca**, y a veces con un logotipo inventado. Por eso el cliente
reclamó lo mismo en tres piezas distintas. Se resolvió con
`scripts/between-logo-vaso.py`, que envuelve el logotipo real sobre el cilindro
del vaso. **La regla ahora es: foto real siempre que exista; si hay que generar,
se pide el vaso liso y se estampa.**

**Qué quedó pendiente.**

1. **Reel Café Bombón (7-sep).** Pasó a `OK PARA DISEÑAR` y el cliente preguntó
   «¿Cómo mostraremos la leche condensada al principio?». Hay propuesta escrita
   con tres caminos y una recomendación en
   [`PROPUESTA-reel-cafe-bombon.md`](PROPUESTA-reel-cafe-bombon.md). **Falta que
   el cliente elija** y que exista una foto del Café Bombón real.
2. **«Así se hace tu café»** sigue `POR GRABAR` (el comentario de coordinar la
   sesión del viernes ya está tachado, o sea resuelto).
3. **Promociones de desayuno**, feed y story: `PENDIENTE POR CLIENTE`.
4. **Las miniaturas dentro de la grilla del Sheet no se tocaron.** El archivo es
   de Sebastián Serrano y reescribirlo desde fuera le borra imágenes y formato de
   todas las columnas. Las piezas nuevas están en el Drive con los mismos
   enlaces; el reemplazo de las miniaturas lo tiene que hacer alguien desde
   Sheets.

**Decisión abierta.** Nadie ha confirmado si el Café Bombón se sirve en vaso
transparente (el brief lo asume) o en el vaso kraft de la marca. De eso depende
todo el planteamiento visual del reel.

**Dónde está todo.**
- Piezas: carpeta `BW` de `S1 HILTON SEP 2026` — `1fQqtl-2X2A4o1L5hH7jlz9xUh_YzXRjq`
- Portal de revisión: https://portal-hilton.vercel.app/between-revision.html
- Código: `src/compositions/hilton/BetweenSeptiembre.tsx`
- Referencias que dejó el cliente: `raw/hilton/between/refs-sept-ronda4/`
- Render: `bash scripts/between-rendir.sh` · QA: `scripts/between-qa.py`
- Subir correcciones: `scripts/between-subir-drive.py --actualizar <ID> ...`

> ⚠️ **Antes de aplicar un comentario de la grilla, mira si está TACHADO.** La
> fila COMENTARIOS DISEÑO mezcla lo pendiente con lo ya resuelto, y lo resuelto
> va tachado. La fila 14 es del cliente y la 15 del equipo de diseño.
