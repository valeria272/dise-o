# Piso18 — bitácora

## 2026-09-17 — Elisabet Soto · el barrido del día, y un «Este no va» que llegó tarde

**Qué se hizo:** `/abrir piso18` — sincronizar, sembrar memoria y correr `/al-dia`
acotado a la marca. **No se produjo ninguna pieza en esta sesión**; la ronda 6 de la
animada la hizo otra sesión en paralelo (ver la entrada de arriba). Lo de acá es el
barrido del Drive y de las dos grillas, que encontró cosas que la ronda 6 no cubre.

⚠️ **Dos sesiones trabajaron el mismo árbol hoy.** El commit de la ronda 6 (`35c8bf0`)
se llevó dentro las instantáneas y el `_estado-sync.json` que había dejado este
barrido, sin commitearlos aparte. No se perdió nada, pero conviene saberlo: si dos
sesiones abren la misma marca a la vez, la que commitea primero arrastra lo de la otra.

### ⛔ Lo urgente: el cliente rechazó el post del 23-09

`FEED!M14` (23 de septiembre, **POST ESTÁTICO – PISO18 DE NOCHE**) tiene desde hoy un
comentario nuevo de una línea:

> «Este no va»

**No estaba en la instantánea del 16-09 ni en la de esta mañana** (12:09Z): llegó
después. El estado sigue en `EN REVISIÓN`.

⚠️ **Es una pieza YA ENTREGADA**, y es justo la del nombre que miente: en Drive se
llama `Post S4 PISO18 25-09.png` pero es la pieza del 23-09. La entrada de la ronda 6
lo mencionó al pasar como «aparece un "Este no va"» sin decir sobre qué pieza caía.
Cae sobre ésta.

**No se resolvió, y a propósito:** «Este no va» no dice si se reemplaza el tema, la
foto o el copy. Es una pregunta para Eli, no algo que se deduzca.

### Una corrección de fecha a la entrada de la ronda 6

Esa entrada dice «el carrusel del 22-09 pasa a ser enfocado en arreglos florales de
matrimonio». **Es el del 21-09**: la instrucción vive en `FEED!I14`, y la columna I es
el 21 de septiembre (`MATRIMONIO DE EQUINOCCIO DE PRIMAVERA`). La del 22-09 es la
columna K, `BENEFICIOS DE TU CUMPLEAÑOS`, cuyo comentario habla de la foto de
ambientación de 50 años. Se anota porque en esta cuenta las columnas se corren y la
memoria `comentarios-nativos-de-excel` exige identificar la pieza por su TÍTULO.

### ⭐ La palabra prohibida ahora la firma el cliente

`FEED!I14` trae un comentario nuevo: *«OK, pero no usemos la palabra BODA, cambiando
el hashtag, aprobado»*, y el copy de la celda pasó de `#BodaDePrimavera` a
`#EventoDePrimavera`. La regla `sin-bodas` de `reglas.yaml` la había dictado Eli el
15-09; **ahora está ratificada por escrito por el propio cliente**. Queda anotado en
la regla: ya no depende del criterio de la diseñadora.

### ⭐ Un cuarto formato de la marca: el banner web

Eli entregó anoche (16-09, 20:39–21:10Z) **16 archivos** en
`PISO18 › BANNERS SEP 2026 4.5M` (`10sST2d5K43vVYFgtn084AsAMNRwCYEoe`):

| | |
|---|---|
| Opciones | `BANNER OP1` y `BANNER OP2 FOTO NOVIOS` |
| Por opción | `PC` y `Mobile` |
| Por dispositivo | 72 PPP y 150 PPP, en PNG y JPG |
| Nomenclatura | `Banner web Piso18 <PC o MOBILE> <72 o 150>PPP [OP2].{png,jpg}` |

El contenido es la promo aprobada **«¿Te casas en verano?» $6.000.000 → $4.500.000**,
la misma que el estudio tiene medida como pieza **cuadrada de 1080×1080**. O sea que
Piso18 tiene cuatro formatos, no tres: feed 4:5 · story 2250×4000 · promo 1080×1080 ·
**banner web (PC y mobile, a dos resoluciones)**. Falta medir su geometría — no se
bajó ninguno hoy.

### Material nuevo sin procesar

Scarlette subió el 16-09 (02:03–02:10Z) **24 archivos** a `MATERIAL DE SEPT 15 › PISO18`
(`1YJ-KitWhHic_RJEQbazJb1NzXPzKKYzd`): **10 HEIC + 14 MOV** de iPhone, del evento del
15-09. ⚠️ Los HEIC no los carga Chrome y los MOV traen rotación por metadato y 60 fps
— las dos trampas ya conocidas de esta cuenta. Puede ser justo el material que
necesita el reel orgánico.

### El reel orgánico del 23-09 se movió

`ORGÁNICO!C14` pasó de `PENDIENTE POR CLIENTE` a **`EN EDICIÓN`**, y en `FEED!G14`
(17-09) apareció *«OK este! veamos que la música que le pongan alcance para todo el
video»*. La respuesta a la duda de material ya estaba puesta en la grilla:
*«R: SI HAY MATERIAL SUFICIENTE :)»*. **Hay que confirmar con Eli quién lo está
editando** — los reels de esta cuenta los ha hecho ella a mano.

### La S5 ya estaba entregada — corrección a la bitácora de ayer

La entrada del 16-09 dejó la S5 escrita como «qué sigue». **No es un pendiente:** se
entregó el 15-09 en el commit `872f2ac` (`C1 S5 PISO18` con 3 slides + `ST N°1 S5` y
`ST N°2 S5`, subidas a Drive). En la grilla están como `OK PARA DISEÑAR` (28 y 30-09)
y `PENDIENTE POR CLIENTE` (29-09): entregadas, sin visto del cliente.

### Octubre: los briefs se reescribieron sin dejar comentario

Diff contra `p18-oct-20260915.json`: **15 cadenas nuevas y 12 desaparecidas**, y ni un
comentario que lo avise — el patrón de la memoria `comentarios-nativos-de-excel`.
Cambió el carrusel del cierre de año, el post de wedding planner ahora lleva texto, la
story de checklist se volvió **«PASOS ANTES DEL EVENTO»** (01 · 02 · 03 editorial,
**explícitamente NO íconos de checklist**), la encuesta pasó de «servicio favorito» a
«estación favorita» y el reel del chef quedó rotulado `REEL ORGÁNICO`.

⛔ **Octubre sigue sin ser producible:** las 7 piezas de FEED están todas en
`EN REVISIÓN` y STORIES y ORGÁNICO ni siquiera tienen poblada la fila de estado.

### ⛔ Punto ciego: los hilos nativos no se leen desde esta máquina

`comments().list` da **404 en las dos grillas** (septiembre y octubre). El token del
estudio es scope `drive.file` y los dos Sheets son de Carlos Figueroa; el conector MCP
de Drive **no expone comentarios**. Los 18 hilos abiertos de octubre que se leyeron el
15-09, y cualquier hilo nuevo de septiembre, **quedan sin verificar**. Los comentarios
en celda sí se leen, y son la vía por la que este cliente comenta — pero no es lo
mismo que haber mirado los hilos.

Cero comentarios de Drive, en cambio, sobre las 9 piezas de la S4 y las 5 de la S5.

**Dónde quedó:** nada renderizado en esta sesión. Instantáneas del día en
`clients/hilton/grillas/api/p18-sept-20260917.json` y `p18-oct-20260917.json` (base del
diff de mañana), registro en `clients/_estado-sync.json`, y la autoridad del cliente
anotada en la regla `sin-bodas` de `clients/piso18/reglas.yaml`.

**Qué sigue:** preguntarle a Eli qué significa **«Este no va»** en el post del 23-09 —
es lo único vivo de septiembre. Después, decidir si el banner web entra al manual como
cuarto formato (hay que bajar uno y medirlo) y si el reel orgánico lo toma el estudio.

**Abierto:**

1. ⛔ **«Este no va»** sobre `FEED!M14` (23-09, PISO18 DE NOCHE), pieza ya entregada
   como `Post S4 PISO18 25-09.png`. Sin instrucción de qué reemplazar.
2. El **banner web** es un formato de la marca que no está medido ni escrito en ningún
   lado. 16 archivos en Drive, ninguno bajado.
3. Los **24 archivos nuevos** de Scarlette (HEIC + MOV) sin pasar por la compuerta de
   material.
4. **Quién edita el reel orgánico del 23-09**, que ya está `EN EDICIÓN`.
5. Los **hilos nativos** de las dos grillas, ilegibles con el token actual. Sigue
   abierta la decisión de ampliarlo a `drive.readonly` (viene desde Between).
6. Sigue en pie todo lo del 16-09: **el manual (`CLAUDE.md`) y la ficha (`marca.json`)
   de Piso18 no existen**, y el nombre que miente de `Post S4 PISO18 25-09.png`.
7. En esta máquina **no hay venv**: los scripts corren con `py -3` y
   `PYTHONIOENCODING=utf-8`. El README de `grillas/api/` todavía dice la ruta del Mac.


## 2026-09-17 — Elisabet Soto · S4 ronda 6: la animada del 23-09 abre con arreglos

**Encargo de Eli:** tomar el cambio que dejó el cliente en la grilla para la
historia animada del 23 de septiembre, aplicarlo, subirlo al Drive y mostrarlo.

**Lo que pidió el cliente** (hoja STORIES, columna del 23-09, la celda volvió de
`CORREGIDO` a **EN CAMBIOS**):

> «Aquí, pedimos que cambiaran la primera imagen que sale, que no sea ese video,
> sino que otra foto de arreglos»

⚠️ **Cómo se detectó.** Diff por CONJUNTO de cadenas de la grilla viva contra
`clients/hilton/grillas/api/p18-sept-20260916.json`. El comentario se **prepende**
sobre el anterior, así que ni el diff por celda ni el `modifiedTime` lo delatan.
Es la tercera vez que esta cuenta lo confirma.

**Lo que se hizo.** El plano 1 era `salon-vacio.mp4` —el recorte del `IMG_4177.MOV`
con el salón sin montar, que había entrado en la ronda 3 por pedido de Eli—. Sale,
y entra **`piso_18-101`** de `Piso 18_28 ago decoración 2024`.

⭐ **Por qué esa foto.** El cliente sólo pidió «otra foto de arreglos», así que la
elección tenía que seguir cumpliendo lo que Eli había fijado, y lo cumple entera:

| Criterio de Eli | Cómo lo cumple |
|---|---|
| Que abra por lo más vacío | El piso está desnudo, no hay ni una mesa puesta |
| «Una transición de una foto y aparece la misma foto, u otra con más montaje» | Es **el mismo arreglo del plano 2** (`mt-90`) visto de lejos: el primer empuje hace literalmente eso |
| Sin rostros ni el logotipo de la pared | No aparece ninguno |
| Sin ampliar (tope 1,0) | Recorte **3240×5760 desde (300, 0)**, reduce ×0,333 |

El recorte queda escrito y reproducible en `scripts/p18-s4-r6.py` — regla 3 del
criterio de Eli, la que se saltó dos veces el 16-09.

**Lo que se midió antes de subir.** El fondo bajo la tinta, por tercios y con el
velo aplicado, contra el plano 2 que ya estaba aprobado:

| Franja | Plano 1 nuevo (`mt-101`) | Control: plano 2 (`mt-90`) |
|---|---|---|
| Bajo el logotipo (y 207–316) | **30 / 35 / 52** | 110 / 141 / 121 |
| Bajo el titular (y 1244–1432) | **48 / 65 / 89** | 49 / 138 / 132 |

O sea que el plano nuevo es **más oscuro que uno ya aprobado** en las dos franjas:
no hace falta velo extra. El primer y el último fotograma pasan las 7 reglas de
`qa/motor.py --marca piso18`.

**✅ Y una duda abierta que se cierra:** el comentario *«Podría ser un texto
orientado a ''Dejando todo listo, para que solo te preocupes de celebrar''»*
aparece ahora **TACHADO** en la grilla. En la ronda 4 la bajada se había quitado
porque la grilla la borró, y quedó anotado como decisión pendiente de Eli. El
tachado la confirma: la bajada no vuelve.

**Dónde quedó.** `ST N°3 S4.mp4` **reemplazada en Drive conservando el enlace**
(`1q8V7ibQtVGYijeAgKK0UPCkCyaYMAyTV`, 11,8 MB, versión 51). Duración, planos 2–5,
titular, cierre y botón **sin tocar**. Antes/después publicado como página:

  https://claude.ai/artifact/AjEeQKnLSiCYZGd7oXK1gh

### ✅ APROBADO por Eli — 17-09-2026

*«Aprobado»*, mirando la página de antes/después. La ronda 6 cierra acá: la
pieza que está en Drive es la buena.

**Abierto:**

1. ⚠️ **Se informa, no se decide** — la apertura con el salón vacío era un pedido
   explícito de Eli y es justo lo que el cliente sacó. La foto elegida conserva la
   idea, pero **la pieza ya no tiene video**. `salon-vacio.mp4` sigue en
   `public/assets/` y se repone en una pasada si Eli lo quiere de vuelta.
2. **Rondas nuevas en el FEED que NO se tocaron** (no son de esta pieza): el
   carrusel del 22-09 pasa a ser «enfocado en arreglos florales de matrimonio»,
   aparece un «Este no va», y el copy se corrigió para sacar la palabra prohibida
   del hashtag («aprobado» una vez cambiado).
3. Sigue en pie todo lo del 16-09: el manual y la ficha de la marca, y el nombre
   que miente de `Post S4 PISO18 25-09.png` (es la pieza del 23-09).


## 2026-09-16 — Elisabet Soto · la marca está operativa, pero le falta su manual

**Qué se hizo:** verificación del estudio en el Windows de Eli (`/arranque`). Todo
lo que Piso18 necesita para producir **está y funciona**: se probó
`qa/motor.py --marca piso18` sobre `out/piso18/s4/base/75-durazno.png` y carga sus
**7 reglas** (5 de agencia + 2 de la marca, incluida la de «bodas» con Eli citada
como autoridad). Kit `src/brand/piso18.ts`, `reglas.yaml` v3, 3,8 GB de material
y las entregas S4/S5 están en su lugar.

**Dónde quedó:** nada se tocó de la marca. El hallazgo es que `scripts/doctor.sh`
reporta **Piso18 sin MANUAL ni FICHA**, y es cierto al pie de la letra: no existen
`clients/piso18/CLAUDE.md` ni `clients/piso18/marca.json`. El criterio de la marca
sí existe, pero está **repartido** entre la bitácora, `reglas.yaml` y el kit.

**Qué sigue:** consolidar el manual y la ficha **destilando lo ya medido y
aprobado** — geometría del logotipo (tope y=207 @1080 en historia, y=105 en feed),
el tope de tinta al 3 % con el porqué calibrado, la paleta del kit y la regla de
«bodas». No se inventa nada nuevo: se ordena lo que ya está firmado.

**Abierto:**
1. El manual y la ficha **quedaron ofrecidos, no escritos** — Eli los quiere
   revisar antes de que pasen a ser ley.
2. ⚠️ Mientras no existan, **`/pieza piso18` no carga la gramática de entrada**:
   quien tome la marca sin haberla trabajado tiene que reconstruirla leyendo esta
   bitácora. Para Eli no se nota; para un relevo sí.


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
