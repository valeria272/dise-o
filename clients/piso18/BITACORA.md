# Piso18 — bitácora

## 2026-09-16 — Arranque de la máquina · 11 referencias de cumpleaños ROTAS

**Qué se hizo:** verificación completa del estudio con `/arranque`. No se diseñó
ni se entregó nada de Piso18. El verificador de material encontró que la carpeta
de referencias de cumpleaños está inutilizable.

**Dónde quedó:** los 11 archivos de `raw/hilton/piso18/ref-cumple/` —
`actual-2/3/4.jpg` y `.png`, `benef-1.jpg`, `benef-1/2/3.png`, `viejo-1.png` —
**no son imágenes: son la página de login de Google guardada como `.jpg`/`.png`**
(≈900 KB de HTML cada uno). La descarga falló en su momento y nadie lo notó.
También cayó así la hoja `raw/hilton/piso18/s5-gid-0.csv`.

Es exactamente el fallo de la memoria `compuerta-de-material`.

**Qué sigue:** antes de tocar la pieza de cumpleaños, rebajar las 11 referencias
y el CSV. La vía que sirve para cualquier tamaño y sin token es
`drive.usercontent.google.com/download?…&confirm=t` (memoria
`bajar-grilla-ajena-de-drive`); si devuelve HTML otra vez, bajar por el conector
MCP de Drive. Después correr
`python scripts/verificar-material.py raw/hilton/piso18` y que dé 0 rotos.

**Abierto:** Piso18 todavía no tiene manual (`CLAUDE.md`) ni ficha (`marca.json`)
— solo `reglas.yaml` y `entregas/`. Está pendiente de abrir su sistema.

## 2026-09-16 — S4 ronda 4: los cuatro cambios del cliente, aplicados y en Drive

**Encargo de Eli:** tomar los cambios que dejó el cliente en la grilla de la S3 y
la S4. A media tarea acotó: *«solo toma s4 ya que yo hice la s3 para que no
pierdas tiempo en esa»*.

**Cómo se detectó lo nuevo:** diff por CONJUNTO de cadenas de la grilla viva
(`export?format=csv&gid=`) contra `clients/hilton/grillas/api/p18-sept-20260915.json`.
⚠️ Fue indispensable: **el 16-09 se corrieron las columnas** —«PISO18 DE NOCHE»
pasó del 25-09 al 23-09 y «SECCIÓN FOTOS NOVIOS» ocupó el 25-09—, así que un
diff por fecha o por celda inventa cambios que no existen.

**Los cuatro cambios de la S4, aplicados:**

| Fecha | Pieza | Qué pidió | Qué se hizo |
|---|---|---|---|
| 21-09 | Carrusel G3 | «+ zoom a la G3 para que no sea tan protagonista el mesón, el resto OK!» | Recorte nuevo de `piso_18-100`: el tablero baja del 63 % al 85 % del alto. **Sube a y=0 en vez de bajar el corte**, así el arreglo queda entero |
| 25-09 | Encuesta, opción B | «pongamos una opción más de mesa para cenar» | B nueva de `piso_18-28` (mantel negro, bajoplato dorado). ⭐ **NO se usó `piso_18-85`**, que también servía: es el mismo montaje de la G1 del carrusel y repetía el feed a 4 días |
| 23-09 | Historia animada | *(sin comentario — **cambió el brief**)* | Titular nuevo literal; se quitó la bajada porque la grilla la borró; el botón del cierre sube a y=1100 |
| 25-09 | Post de feed | «Que sea esta foto, con logo y estamos» | El enlace era `piso_18-128.jpg` y **ya estaba en disco** (`raw/hilton/piso18/deco-ago2024/`). Recorte 4:5 abierto a la izquierda —muestra el salón— y logotipo 568 px en y=218 |

**Dónde quedó:** las tres primeras reemplazadas en Drive **conservando el enlace**
(las subió este token, así que `files().update` funciona). El post subió nuevo como
`Post n°2 S4 PISO18 25-09.png`. Las 8 piezas pasan `qa/motor.py --marca piso18`.
Página de revisión en `out/piso18/s4/revision-r4/index.html`.

**Abierto — tres decisiones de Eli:**
1. `Post S4 PISO18 25-09.png` es en realidad el post de **23-09** («Piso18 de
   noche»). No se renombró para no romper enlaces; si se renombra, el nuevo toma
   el nombre limpio.
2. `piso_18-128` es también el **tercer plano de la animada del 23-09**: el
   cliente eligió esa foto por su nombre, pero queda la misma escena el 23 y el 25.
3. La bajada «Dejando todo listo…» se quitó porque la grilla la borró, pero el
   comentario que la pedía sigue vivo en la celda sin tachar.

**Lo de la S3 que NO se tocó** (lo hace Eli): 16-09 «Quitemos Sujeto a
disponibilidad y OK» · 20-09 «Quitar ese CTA, que sea foco reacción» · y el reel
del 17-09 cambió de texto en el brief («La atmósfera indicada» en grande / «puede
cambiar por completo tu celebración» en chico). Sus archivos en Drive los subió
ella a mano y **el token del estudio no puede reemplazarlos** (scope `drive.file`).

**⛔ Lección del día:** el script de recortes pisó `tira-b.jpg` **antes** de que se
guardara el «antes» para la página. Se recuperó con `git show HEAD:…` porque los
fondos de la ronda 3 estaban commiteados. Es exactamente para esto que sirve la
regla de que el render vuelve al repo el mismo día: sin ese commit el antes/después
habría sido una reconstrucción a ojo.

### La revisión se publica como página, y el Drive de Hilton NO es interno

`out/piso18/s4/revision-r4/index.html` se publicó como página —el modo de siempre
para las revisiones de esta cuenta, memoria `antes-y-despues-en-html`—:

  https://claude.ai/artifact/7Fj6vDyRsdYYmWfMbAW4MG

⛔⛔ **Y el hallazgo del día, que vale para las cuatro marcas del complejo:** al
crear un documento de prueba dentro de `S4 HILTON SEP 2026 › PISO18` se vio que
esa carpeta hereda **20 permisos de escritura, y dos son del CLIENTE**:
`magdalena.cordero@hilton.com` y `doubletreesantiagovitacura@gmail.com`. O sea
que **todo lo que se deja en esa carpeta lo ve Hilton**. Está bien para las piezas
—para eso es— pero una página de revisión con notas internas **NO va ahí**. El
documento se sacó de la carpeta a los pocos minutos; quedó huérfano en Mi unidad
de valeria con el id `1CfYeWQ8rbtrpCmNkh4hBIzCLNOx7i1EWSBI47FpM3yk`, sin acceso
para nadie más. Decidir si se borra.

Y un detalle de la API que conviene tener escrito: **`permissions().create` sobre
un permiso que ya venía HEREDADO de la carpeta no crea uno directo** — devuelve el
heredado. Por eso, al sacar el archivo de la carpeta, los accesos «otorgados»
desaparecieron junto con la herencia.
