# Piso18 — bitácora

## 2026-09-16 — Elisabet Soto · la S4 completa, aprobada

**Qué se hizo:** se tomaron los cambios que dejó el cliente en la grilla y se
cerró la S4 en dos rondas. **Ronda 4** (los 4 cambios del cliente): más zoom en la
G3 del carrusel, la opción B de la encuesta pasa a mesa puesta, titular nuevo en
la historia animada —ahí **no hubo comentario: cambió el brief**— y un post nuevo
con la foto que el cliente eligió por enlace. **Ronda 5** (revisión de Eli): la G3
con el encuadre de su captura y la portada con el velo de marca para que el
logotipo se lea. Eli aprobó. **La S3 no se tocó: la hace ella.**

**Dónde quedó:** las 9 piezas en `S4 HILTON SEP 2026 › PISO18`, las corregidas
reemplazadas **conservando su enlace**. Las 8 estáticas pasan
`qa/motor.py --marca piso18`. Aparato en `src/compositions/piso18/P18StMontaje.tsx`
y `scripts/p18-s4-r4.py` · `p18-s4-r5.py` · `p18-rendir.py` · `p18-s4-subir.py`.
Página de revisión (versión 2): <https://claude.ai/artifact/7Fj6vDyRsdYYmWfMbAW4MG>.
Instantánea base del próximo diff: `clients/hilton/grillas/api/p18-sept-20260916.json`.

**Qué sigue:** la **S5** —`ST-N1-S5` (28-09) y `ST-N2-S5` (30-09) están en
`OK PARA DISEÑAR` y el carrusel del 29-09 en `PENDIENTE POR CLIENTE`—, y correr
`/al-dia piso18` antes de producir: el 16-09 el cliente movió columnas de fecha y
reescribió un brief sin dejar comentario.

**Abierto:**
1. ⚠️ `Post S4 PISO18 25-09.png` **es la pieza del 23-09** — la grilla la movió y
   el nombre quedó mintiendo. No se renombró para no romper el enlace del cliente,
   pero **el portal levanta por NOMBRE**: si esa pieza pasa por el portal, hay que
   arreglarlo antes. Eli lo aprobó sabiéndolo.
2. ⛔ **La carpeta de entrega de Hilton la ve el cliente** (`@hilton.com` y
   `doubletreesantiagovitacura@gmail.com` entre sus 20 permisos de escritura). Las
   piezas van ahí; **nada interno**.
3. `piso_18-128` sale en el post del 25-09 y también como tercer plano de la
   animada del 23-09. El cliente eligió esa foto con nombre y apellido.
4. *«Ese sería para el G3 de la S3»* — se aplicó a la G3 de la **S4**, que es donde
   vive la foto que mandó. Si se refería al `C1 S3`, está sin hacer.
5. **Piso18 sigue sin manual** (`CLAUDE.md`) ni ficha (`marca.json`). Lo aprendido
   hoy quedó en `reglas.yaml`.
6. Documento de Google huérfano en la cuenta del estudio
   (`1CfYeWQ8rbtrpCmNkh4hBIzCLNOx7i1EWSBI47FpM3yk`): se creó en la carpeta del
   cliente por error y se sacó. Decidir si se borra.

---

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

## 2026-09-16 — S4 ronda 5: el carrusel, con el encuadre que mandó Eli

Revisión de Eli sobre la ronda 4: *«Las historias quedaron ok»* y dos cambios al
carrusel. **Las historias y el post quedan como están.**

**1 · La G3, más cerrada todavía.** *«Aumenta más el zoom. No tiene que verse en
los costados ni la mesa. La idea es que se vea la captura que te dejé.»* Mandó
una captura con el encuadre, así que el recorte **se dedujo de ella, no a ojo**:
se midieron tres puntos presentes en los dos encuadres —boca de la vasija, base
del farol de alambre, canto del tablero— y de ahí salió la caja.

| | Ronda 4 | Ronda 5 |
|---|---|---|
| Caja en `piso_18-100` | 3199×4000 desde (0,0) | **2300×2876 desde (600,704)** |
| Reduce a | 0,703 | **0,978** |

⚠️ **0,978 es el último zoom posible sobre esta foto sin ampliar.** Si pidiera
más, hay que ir al banco a buscar un plano más cerrado — forzar éste lo deja
blando. Está escrito en la página de revisión para que no se intente.

**2 · La portada, con velo.** *«Oscurece un poco arriba con una transparencia muy
sutil para que el logo se vea mejor. Con opacidad.»* El problema estaba medido:
la banda del logotipo daba **60 / 64 / 70** de luminancia por tercios, pero el
**percentil 90 llegaba a 253** — detrás del logotipo blanco hay globos de vidrio
y follaje iluminado que tocan el blanco puro. No era falta de oscuridad: eran
reflejos *del mismo valor que la tinta*.

⭐ **El velo no se inventó: es el que la marca ya tiene.** `logo PISO18.png` es
una plantilla de historia con un velo negro en degradado —alfa 150/255 = 0,588 en
y=0, que llega a 0 al **41,7 %** del alto—. Se aplicó ese mismo velo, con la misma
proporción, sobre el 4:5. La banda baja a **35 / 37 / 41** y el degradado se
desvanece antes del primer tercio, así que las flores no se tocan. Sólo lleva
velo la **portada**: las otras tres no tienen logotipo y el brief las quiere limpias.

⛔ **El velo va DEBAJO del logotipo**, así que la portada se rehizo desde la foto
limpia — velar sobre el `slide1.jpg` entregado habría apagado el logotipo blanco
junto con el fondo. El recorte original se recuperó por correlación contra el
origen: `piso_18-72`, ancho completo, **y=594** (residuo 2,0 sobre 255 = ruido de
JPEG). Queda escrito porque es la segunda vez en el día que hace falta reconstruir
un recorte que nadie había anotado.

**Dónde quedó:** `C1 S4 N°1.png` y `C1 S4 N°3.png` reemplazadas en Drive con su
enlace de siempre. Las 4 del carrusel pasan el QA. Revisión (versión 2):
https://claude.ai/artifact/7Fj6vDyRsdYYmWfMbAW4MG

⚠️ **Sin resolver:** Eli dijo *«Ese sería para el G3 de la S3»*. La foto que mandó
es `piso_18-100`, que es la G3 del carrusel de la **S4** —la que veníamos
corrigiendo—, así que se aplicó ahí. Si se refería al carrusel `C1 S3` (el suyo,
que subió a mano el 14-09), hay que preguntarle.

### ✅ APROBADO por Eli — 16-09-2026

La ronda 5 quedó **aprobada**. La S4 de PISO18 cierra así en
`S4 HILTON SEP 2026 › PISO18`:

| Archivo | Fecha de la pieza | Última versión |
|---|---|---|
| `C1 S4 N°1.png` | 21-09 | ronda 5 · portada con velo |
| `C1 S4 N°2.png` | 21-09 | ronda 3 · sin cambios |
| `C1 S4 N°3.png` | 21-09 | ronda 5 · el encuadre de Eli |
| `C1 S4 N°4.png` | 21-09 | ronda 3 · sin cambios |
| `ST N°2 S4.png` | 22-09 | ronda 3 · aprobada en la grilla |
| `ST N°3 S4.mp4` | 23-09 | ronda 4 · titular nuevo |
| `ST N°4 S4.png` | 25-09 | ronda 4 · opción B mesa puesta |
| `Post n°2 S4 PISO18 25-09.png` | 25-09 | ronda 4 · pieza nueva |
| `Post S4 PISO18 25-09.png` | **23-09** | ronda 3 · «Piso18 de noche» |

**Queda abierto, y Eli lo aprobó sabiéndolo** (se le informó y no pidió cambiarlo):

1. ⚠️ `Post S4 PISO18 25-09.png` **es la pieza del 23-09** — la grilla la movió de
   fecha y el nombre quedó mintiendo. No se renombró para no romper el enlace que
   el cliente ya pueda tener. **Ojo: el portal levanta por NOMBRE**
   (`docs/PORTAL-VALIDACIONES.html`), así que si esa pieza pasa por el portal, el
   nombre hay que arreglarlo antes.
2. `piso_18-128` sale en el post del 25-09 y también como tercer plano de la
   animada del 23-09. El cliente eligió esa foto por su nombre.
3. La bajada «Dejando todo listo…» quedó fuera de la animada.
4. *«Ese sería para el G3 de la S3»* — se aplicó a la G3 de la **S4**, que es
   donde vive la foto que mandó. Si se refería al `C1 S3`, está sin hacer.

**Lo de la S3 sigue siendo de Eli:** 16-09 «Quitemos Sujeto a disponibilidad y OK»,
20-09 «Quitar ese CTA, que sea foco reacción», y el reel del 17-09 con el texto
nuevo del brief.
