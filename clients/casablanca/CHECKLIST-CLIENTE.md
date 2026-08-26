# PISOS CASABLANCA — qué falta para que el sistema corra solo

> Actualizado **26-08-2026**, después de medir 55 piezas aprobadas.
> Marcar `[x]` cuando llegue y borrar la fila al resolverse.
> Contraparte de diseño: **Paulina Bustamante** · KAM: **Serena Abarca** ·
> Medios: **Ignacio Retamal** · Cliente: **Jenny**.

## 🔴 Bloqueantes — sin esto hay que improvisar cada vez

| # | Qué | A quién | Por qué bloquea |
|---|---|---|---|
| 1 | **La serif itálica del titular.** Está identificada como Didone de biblioteca pero no exactamente cuál. **Acción concreta en Adobe (5 min):** en la app de Creative Cloud → *Fuentes* → buscar y **activar** estas seis familias: **Bodoni URW**, **Bauer Bodoni**, **ITC Bodoni Seventytwo**, **Walbaum**, **Didot LT Pro**, **Abril Display**. Con eso basta: al activarlas, Creative Cloud las baja al Mac y el identificador (`scripts/casablanca-tipografia.py`) elige la correcta sola. | Valeria (Adobe CC) | Es el elemento más grande de la pieza. El sustituto de hoy (Bodoni Moda Italic w800/opsz18) calza en el 77 % pero **la `z` y la `j` de la marca no llevan cola** y las del sustituto sí — se nota en «Roble Spritz», «Roble Mojito». |

> 🅰️ **Cómo funciona Adobe Fonts acá.** Activar una familia en Creative Cloud la
> sincroniza a `~/Library/Application Support/Adobe/CoreSync/plugins/livetype/.r/`,
> y desde ahí mis scripts la leen directo. Ya funciona así con **IvyOra Display**
> para Tierra Calma. **No hace falta instalar nada más**: en este Mac sólo está la
> app de Creative Cloud, sin Photoshop ni Illustrator.
>
> 🅱️ **Atajo si prefieres cerrarlo en un minuto:** instala **Photoshop** desde
> Creative Cloud, abre cualquier pieza de `raw/casablanca/ref/`, selecciona el
> titular con el marco y usa **Texto → Buscar coincidencia de fuentes**. Te dice el
> nombre exacto. Después la activas y me lo dices.

## 🟡 Importantes — mejoran calidad y velocidad

| # | Qué | A quién | Para qué |
|---|---|---|---|
| 2 | ✅ **Sans resuelto.** Versales = **Futura Medium** (IoU 89,2 %, ya está en el Mac; en Adobe Fonts es **Futura PT**). Caja baja = **Montserrat Regular** (79,7 %, probable). Falta sólo confirmar la caja baja con la misma vuelta del punto 1. | Valeria | Sin bloqueo: se puede producir con lo que hay. |
| 3 | **La script manuscrita** de «Colección Rústico / Italiana / Premium / Clásica». | Paulina | Es la firma del registro de anuncio y hoy no está identificada. |
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
