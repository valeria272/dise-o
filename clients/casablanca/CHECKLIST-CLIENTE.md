# PISOS CASABLANCA — qué falta para que el sistema corra solo

> Actualizado **26-08-2026**, después de medir 55 piezas aprobadas.
> Marcar `[x]` cuando llegue y borrar la fila al resolverse.
> Contraparte de diseño: **Paulina Bustamante** · KAM: **Serena Abarca** ·
> Medios: **Ignacio Retamal** · Cliente: **Jenny**.

## 🔴 Bloqueantes — sin esto hay que improvisar cada vez

| # | Qué | A quién | Por qué bloquea |
|---|---|---|---|
| 1 | **Las piezas del feed publicado hoy, como PNG.** Son las 3 capturas de Instagram que mandó Valeria: placa gris del logo arriba a la **izquierda**, nombre del piso en **Didone CAJA ALTA**, bloque alineado a la izquierda, barra gris translúcida al pie ("MÁS DETALLES EN LA DESCRIPCIÓN…"). | Paulina | **Es el registro que está publicado y el que se pidió replicar, y es el único que no pude medir.** Lo busqué en todo el Drive del cliente (2025 completo + ene/feb/may/jun/jul/ago 2026), en la carpeta de editables de Paulina, y **abrí las tres grillas de paid de jun/jul/ago 2026** (≈1,4 GB de imágenes incrustadas): sólo contienen los otros dos registros. Todo lo que el manual dice del registro C está estimado a ojo. |
| 2 | **El archivo de la serif itálica de titular** (.otf/.ttf) o su nombre exacto y quién tiene la licencia. | Paulina | Hoy se usa Playfair Display Italic 900 + tracking como sustituto. Calza en altura y en ancho, **pero no en dibujo**: la 'z' real es recta con serifa de pie y la de Playfair lleva cola caligráfica. Se nota en el nombre del piso, que es el elemento más grande de la pieza. |
| 3 | **El archivo de la sans** de bajadas, etiquetas y botones. | Paulina / Grupo Revex | Poppins Regular calza el ancho de las bajadas, pero en el botón la fuente real es **más ancha a igual altura** (hacen falta +7,8 px @2250 de tracking para igualarla). Es una geométrica ancha tipo Futura / Century Gothic — probablemente la corporativa de Grupo Revex. Mientras no llegue, todo texto en sans queda aproximado. |

## 🟡 Importantes — mejoran calidad y velocidad

| # | Qué | A quién | Para qué |
|---|---|---|---|
| 4 | **La script manuscrita** de «Colección Rústico / Italiana / Premium / Clásica». | Paulina | Es la firma del registro de anuncio y hoy no está identificada. |
| 5 | **Confirmar el formato del feed: 1:1 o 4:5.** De 55 piezas, 35 son 1:1 y sólo las 6 de agosto 2026 son 4:5. | Serena | Septiembre ya se entregó en 4:5 sin avisar (ver `feedback/2026-08-25-ronda2.md`, pendiente nº 3). Es un cambio sobre el contrato de entrada, no un detalle. |
| 6 | **Fotos reales de los 4 SKU instalados** (Roble Natural UV 190×1900 y 167×1200, Roble Aserrado, Cumarú). | Jenny | Sin ellas el piso lo genera IA y ya nos costó una ronda completa: la muestra no coincidía con el suelo. Es el error más caro que existe en una marca de pisos. |
| 7 | **Fotos del interior del showroom de Vitacura sin gente** (vista general y zona de muestras). | Jenny | De las 36 fotos disponibles, 32 son la fachada y 4 tienen al equipo posando — y no hay derechos de imagen. Hoy la única salida es borrar personas sobre una foto real. |
| 8 | **Brandbook o manual de marca**, aunque sea una lámina. | Jenny / Grupo Revex | Confirmado con Paulina que **no existe**. Todo lo que sabemos salió de medir piezas. Si aparece uno, manda sobre este manual. |
| 9 | **Los editables `.ai` empaquetados** de un carrusel cualquiera. | Paulina | En su carpeta de editables sólo hay PNG y MP4 exportados. Un `.ai` empaquetado trae el `Informe.txt` con los nombres exactos de fuentes y la mesa de trabajo — resuelve los puntos 2, 3 y 4 de una sola vez. |

## 🟢 Deseables

| # | Qué | Para qué |
|---|---|---|
| 10 | Los logos oficiales en vectorial (SVG/AI) con transparencia, en sus tres versiones (apilado, horizontal, sólo símbolo). | Hoy se usan PNG rasterizados desde las piezas; al escalar a 2250 px se nota. |
| 11 | El banco de fotos de ambiente propio del cliente. | Para dejar de depender de generación IA en el registro editorial. |
| 12 | La grafía definitiva de **Cumarú** por escrito del cliente. | Hoy conviven "Cumarú" (pieza), "CUMARU" (brief) y "Camarú UV" (sitio web). Valeria fijó **Cumarú**; falta que el cliente lo confirme. |

---

## Lo que necesito de ustedes cada vez
1. El brief con los textos **finales** — salen verbatim a la pieza.
2. Qué piezas y en qué formatos.
3. Si hay promoción: precio, vigencia y el legal exacto. *(En Casablanca no debería haber: la marca no habla de precio.)*
4. La carpeta de Drive donde subir.
5. El feedback **en los archivos de Drive** (comentarios), para que quede trazable.

## Lo que devuelvo
- Las piezas en su formato + los editables
- `ENTREGA.md` con qué es cada pieza, de dónde salió cada texto y qué quedó pendiente
- Todo subido a la carpeta del cliente

---

## Higiene de material — leer antes de bajar nada

- La carpeta de referencias vive en **`raw/casablanca/ref/`** y hoy tiene **55 piezas
  aprobadas** verificadas (ago-2025 → ago-2026).
- **El 26-08-2026 había 13 piezas de BETWEEN** (la cafetería del complejo Hilton)
  dentro de `raw/casablanca/ref-ig/`. Se movieron a `raw/hilton/between-ig-feed/`.
  Es la segunda vez que pasa: **correr siempre la compuerta antes de diseñar.**

```bash
python3 scripts/verificar-material.py raw/casablanca/ref
python3 scripts/hoja-contacto.py raw/casablanca/ref out/_verificacion/casablanca-material.png
# y MIRAR la hoja de contacto
```

## Cómo se sacan las gráficas que viven dentro de una grilla de paid

Las grillas de medios son Google Sheets con las piezas **incrustadas en celdas**: la
API no las expone y el archivo pesa >100 MB. Se exporta la hoja como ZIP HTML, que
trae cada imagen en `resources/`:

```bash
curl -sL "https://docs.google.com/spreadsheets/d/<ID>/export?format=zip" -o grilla.zip
unzip -qo grilla.zip 'resources/*' -d grilla && find grilla -name '*.jpg' -size +1M
```
