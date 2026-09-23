---
name: comentarios-nativos-de-excel
description: Como leer una ronda de verdad en la grilla xlsx: comentarios nativos anclados a celdas, el DIFF contra la copia anterior (los nuevos se prependen), columnas rotadas y las piezas que el cliente pega dentro del archivo
metadata:
  type: feedback
---

En las grillas mensuales, **no todo el feedback está en las filas de comentarios**.
Una ronda completa puede llegar como **comentarios nativos de Excel anclados a
celdas**, que no se ven al leer los valores de las celdas.

**Por qué:** la ronda 5 de Between (31-08-2026) llegó así — 9 comentarios de
Scarlette Muñoz asignados a Eli. La fila 15 `COMENTARIOS DISEÑO` seguía mostrando
los de la ronda 4, la mitad tachados. Leyendo solo esa fila, la ronda entera
pasaba inadvertida y se entregaba de nuevo lo mismo.

**Cómo aplicarlo:** hay que abrir el xlsx como zip y leer `xl/comments1.xml`,
`xl/comments2.xml`, … (uno por hoja, en el orden de las hojas). Traen **autor y
fecha**, que es como se distingue lo nuevo de lo viejo:

```python
import zipfile, re, html
z = zipfile.ZipFile("grilla.xlsx")
for n in [x for x in z.namelist() if re.match(r"xl/comments\d+\.xml", x)]:
    d = z.read(n).decode("utf-8", "replace")
    for m in re.finditer(r'<comment [^>]*ref="([^"]+)"[^>]*>\s*<text>(.*?)</text>', d, re.S):
        print(n, m.group(1), html.unescape(re.sub(r"<[^>]+>", "", m.group(2))))
```

Son **dos mecanismos distintos y hay que mirar los dos**: los comentarios nativos
por un lado y, por otro, el texto de las filas `COMENTARIOS CLIENTE` (14) y
`COMENTARIOS DISEÑO` (15), donde **lo tachado ya está hecho** y se detecta con
`openpyxl.load_workbook(..., rich_text=True)` mirando `font.strike` de cada run.

Estas grillas se bajan **sin autenticación**:
`curl -sL -o g.xlsx "https://drive.google.com/uc?export=download&id=<ID>"`.
El conector de Drive devuelve texto plano que puede venir **desactualizado** — en
esta ronda mostraba estados viejos. El xlsx bajado es la fuente de verdad.

## ⭐⭐ La ronda nueva se detecta por DIFF, no leyendo la celda (02-09-2026)

Lo anterior no basta, y la ronda 7 de Between lo demostró: **los comentarios
nuevos se PREPENDEN sobre los viejos dentro de la misma celda**. La celda `E15`
pasó de un bloque a dos bloques separados por líneas en blanco, con el nuevo
arriba. Leyendo la celda no hay forma de saber cuál llegó hoy — y el bloque viejo
puede estar CONTRADICHO por el nuevo (en E15 el cliente pedía en la ronda 4
agregar «¡Ven por tu café de regalo!» y en la 7 pidió eliminarlo).

**Y el comentario nativo puede ser solo un AVISO, no el contenido.** Los dos
nuevos decían literalmente «dejaron nuevos comentarios acá» y «acá tomar estos
nuevos cambios pliss». El feedback real estaba escrito en la celda.

**Cómo aplicarlo:** guarda cada xlsx que bajes y compara celda a celda contra la
copia anterior. Es lo único que separa ronda nueva de ronda vieja:

```python
import openpyxl
a = openpyxl.load_workbook('grilla-ayer.xlsx', data_only=True)
b = openpyxl.load_workbook('grilla-hoy.xlsx',  data_only=True)
for hoja in ('FEED', 'STORIES'):
    wa, wb = a[hoja], b[hoja]
    for r in range(1, max(wa.max_row, wb.max_row) + 1):
        for c in range(1, max(wa.max_column, wb.max_column) + 1):
            ref = openpyxl.utils.get_column_letter(c) + str(r)
            if wa[ref].value != wb[ref].value:
                print(hoja, ref, repr(wa[ref].value)[:200], '->', repr(wb[ref].value)[:200])
```

Dos cosas más que el diff caza y la lectura no:

1. **Columnas ROTADAS.** El cliente reordenó las 3 primeras stories: el
   contenido de E pasó a C, el de C a D y el de D a E, con sus comentarios y
   estados. Sin diff parece ronda nueva en tres piezas; con diff se ve que dos
   solo cambiaron de fecha y **una sola** tiene feedback real.
2. **Imágenes nuevas = las piezas entregadas.** El xlsx creció 1 MB y `xl/media`
   pasó de 25 a 30: el cliente pega la pieza entregada en la grilla para
   marcarla. Se ubican cruzando `xl/drawings/drawingN.xml` + su `.rels` contra
   `xl/media`. ⚠️ Los anclajes son flotantes y **no coinciden** con la columna de
   la pieza; hay que abrir la imagen para saber cuál es.

⛔ Y antes de rehacer algo, **verifica el pedido contra el código**: dos de los
cambios «nuevos» de la ronda 7 (el «desde» y sacar «Café grande» del To Go) ya
estaban aplicados desde la ronda 5. La pieza que el cliente marcó era un render
viejo que nunca se re-entregó. Media ronda puede ser «rendir y entregar», no
«rediseñar».

## ⛔⛔ La grilla se RE-FECHA entera, y no hay que quemar ninguna fila (04-09-2026)

Dos cosas que pasaron el mismo día en Between y que rompen cualquier lectura
ingenua:

1. **La hoja `FEED` borró la SEMANA 1 y corrió todo el mes** —el cumpleaños pasó
   del 3 al 9, «Primero la foto» del 9 al 14, «Ella habló» del 11 al 16, las
   Promos To Go del 14 al 22—. O sea que la MISMA pieza cambia de columna Y de
   fecha entre una sesión y la siguiente: identifícala por su **brief**, no por
   la fecha ni por la letra de la columna.
2. ⛔ **La fila del ESTADO no es la misma en todas las hojas.** El script de
   instantánea del estudio la tenía quemada («FEED 15») y en esa grilla la de
   FEED es la **16**: la 15 es `COMENTARIOS DISEÑO`. Con eso el encabezado
   imprimía el comentario en vez del estado y —peor— el filtro `if not estado:
   continue` **se saltaba toda columna sin comentario de diseño**: piezas enteras
   desaparecían de la instantánea, en silencio, y el diff salía corrido de
   columna.

**Cómo aplicarlo:** la fila se BUSCA por su rótulo en la columna A
(`next(f for f,c in campos.items() if c.upper().startswith('ESTADO'))`) y el
filtro de columnas pasa a ser «la columna está vacía de punta a punta». Nunca un
índice literal: el cliente reordena la hoja sin avisar.

Relacionado: [[between-sistema-grilla]], [[leer-el-brief-y-su-carpeta-de-referencias]].

## ⚠️ Las dos «pruebas baratas» tienen letra chica (09-09-2026, DOUBLETREE)

La ronda del 08-09 en DT (20:42Z) obligó a corregir los dos atajos que veníamos
usando para saber, sin diffear todo, si una grilla trae algo nuevo:

1. ⛔ **`uniqueCount` de `xl/sharedStrings.xml` NO alcanza.** Quedó en **140 → 140**
   y **sí había texto nuevo**: el cliente **reemplazó** una cadena en vez de agregar
   una, así que el conteo no se movió. Lo que sí delató el cambio fue el **tamaño**
   del XML (23 639 → 23 691 bytes) y, definitivo, el **diff por CONJUNTO de cadenas**
   (1 nueva, 1 desaparecida). Usa el conjunto, no el contador.
2. ✅ **El SET de hashes de `xl/media` sigue siendo la prueba buena para imágenes.**
   Hoy fue idéntico (15 = 15) con **9 archivos renumerados** y 3 cambiando de nombre
   entre `.png` y `.gif`. Sin esa prueba parecía que el cliente había pegado piezas
   nuevas.

⛔ **Y lo más importante: el comentario viejo NO siempre se prepende.** Acá
desapareció — no quedó arriba ni tachado. `K14` pasó de «Podríamos hacer como un
video todo en POV» a «Este que mejor sea un estático, ya hicimos reel hace poco»,
y del texto anterior no quedó rastro. **La regla de que se prependen es de Between,
no una ley del formato.** Por eso el diff por conjunto de cadenas es el que salva:
caza igual el agregado y el reemplazo.

**Y ojo con el cambio de formato escondido en un comentario.** Ese mismo comentario
convirtió un REEL en un ESTÁTICO, pero la fila `DISEÑOS` **seguía diciendo REEL** y
el brief seguía describiendo 5 escenas con rodaje. Cuando un comentario cambia el
formato, **el brief queda contradiciéndose a sí mismo**: hay que redefinirlo con el
cliente, no elegir uno de los dos por cuenta propia.

## ⛔ Un editable propio de Drive no siempre baja (09-09-2026)

`curl "uc?export=download"` funciona con la grilla porque está compartida por
enlace. Con los archivos de la carpeta propia de la diseñadora **llega la página de
login de Google** (la trampa de [[compuerta-de-material]]), y el token local tampoco
los ve porque tiene scope `drive.file`. El camino que funcionó para un `.txt` fue el
conector MCP con `download_file_content` y decodificar el base64 **como `cp1252`**
(los `Informe.txt` de Illustrator no son UTF-8).

⚠️ Pero para un PNG grande no hay camino: `read_file_content` devolvió **contenido
vacío** con los dos PNG del carrusel vigente de Family Time (6,7 y 3,0 MB), y bajarlo
por base64 costaría millones de tokens. **Si hace falta medir píxeles de una pieza
aprobada, hay que pedir que la compartan por enlace o que la copien al repo.**
