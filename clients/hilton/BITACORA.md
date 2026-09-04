# Bitácora — HILTON (DT · QB · Between · Piso18)

> Una entrada por sesión, la más nueva arriba. Sirve para que otro diseñador
> retome la cuenta mañana sin preguntar nada. Se escribe en el `/cierre`.

---

## 2026-09-04 · Eli (Windows) — BETWEEN ronda 12: dorado elegante, y se deja de montar

*(Cuarta sesión del día. La ronda 11 está en la entrada de más abajo.)*

**Qué devolvió Eli de la ronda 11**, y las cuatro correcciones eran mías:

| Pieza | Su comentario | Qué se hizo |
|---|---|---|
| **S1 Cumpleaños 1 y 2** | «eso que agregaste, de serpentinas se ve muy infantil y mal diseñado. Debe ser **dorado muy elegante**… como está en el editable» · «se ve un poco **blanco y filtro extraño** y desenfocado el vaso togo y **él es el protagonista**» | Serpentinas de ORO metálico en vez de cinco colores planos; exposición fijada por el PRODUCTO, no por el cuadro; nitidez local sobre el vaso; y en la G2 el desenfoque de fondo baja de 9 a 4 px |
| **S1 Cumpleaños 2** | «el logo del icono de la segunda slide no es los colores que se utiliza. Es **fondo café between + logo en beige**» | Avatar del mock corregido: disco `#675B49` con el lockup en `#FFF9EB` |
| **S2 ST Emergencia** | «el cambio es *que el salado sea un crosant jamon queso y que el dulce sea un muffin*» | El cambio **ya estaba hecho en la ronda 10 y nunca se subió**. Se rindió y se subió |
| **S3 portada** | «la chica tiene **recortes** se ve muy mal editado… los textos están bien en el diseño, solo la foto de fondo estaba extraño» | Escena **generada completa en una pasada**. Fuera el montaje |
| **S3 slide 4** | «se ve **quemada y mal**. Vuelve a hacer ese diseño: los tres productos juntos **en formato To Go**… una mano tomando la bolsa o el café» | Escena nueva desde un editable de ELI, con muffin, mano y los dos logotipos estampados con el vector real |
| **S2 Ella habló** | «queda **aprobado**» | No se toca |

**⛔⛔ El error de fondo, y es medible: fijé la exposición por la mediana del
CUADRO.** En la toma del cumpleaños la mitad de arriba es muro vegetal casi
negro, así que la mediana global daba **62**; para llevarla a 104 hizo falta un
gamma que abrió el sujeto un tercio. Resultado: el vaso pasó de mediana 127 a
**166** y su calidez de 25,5 a **18,7** — o sea, kraft blanquecino y sin calidez.
Eso es exactamente «un poco blanco y filtro extraño». Ahora el objetivo se mide
sobre el PRODUCTO (vaso + comida): 118 → 126, y el vaso queda en 130 con calidez
27,8. Y la calidez sólo se corrige si pasa de 28 — el perfil `neutro` del mes
está pensado para las fotos que venían en 35-49, no para una que ya viene bien.

**⭐⭐ Y el otro aprendizaje, sobre los adornos: lo infantil era el COLOR PLANO.**
Los papelitos los pidió el cliente, la idea estaba bien; la ejecución no. Cinco
colores planos en tiras cortas se leen como **grageas de torta**. La referencia
de la marca para «cumpleaños elegante» está en el propio editable de Eli: globos
champán y cintas doradas. Lo metálico no es el color, es la variación — degradado
a lo largo de la cinta (una cinta gira y toma la luz desigual) más una veta
especular. Y forma de cinta: arqueada, afinada en las puntas y de 4,5 a 8,5 veces
más larga que ancha.

**⛔⛔ Lo de la portada es de método y ya van tres rondas.** Era un montaje: una
figura recortada sobre un fotograma del local. La ronda 11 le fundió el canto con
un mapa de nitidez y no alcanzó, porque **un recorte y su fondo nunca comparten
la luz**. Se dejó de montar:

1. **primero se agotó el material real** — 75 fotogramas de los 25 clips `.MOV`
   del cliente: todos interiores del hotel y del cowork, ni un plano de alguien
   saliendo con un vaso. La escena del brief no existe;
2. se generó **entera en una pasada** con Nano Banana Pro, con un fotograma del
   muro vegetal real como referencia y pidiendo el vaso **kraft liso**;
3. **upscaler ×2 antes de recortar** (el 4:5 sale de una ventana de 2.880 px);
4. el logotipo real **estampado y enmascarado al cartón**, para que la tinta no
   caiga sobre los dedos;
5. y el encuadre **calculado para el bloque de texto que ya está aprobado**: el
   vaso cierra en y=1483 y la script arranca en y≈1595.

**⭐⭐ Y un hallazgo que vale para toda la cuenta: el generador conserva el
logotipo de la referencia, pero REDIBUJADO.** En la slide 4 la base fue un
editable de Eli que ya traía los logotipos impresos. El modelo los mantuvo en su
sitio y con la silueta correcta —incluso la `Ǝ` invertida— pero el trazo y el
tracking no son los de la marca. Es lo que el cliente reclamó en la ronda 5. Así
que se pidió el envase **sin ninguna letra** y se estampó el vector real en la
bolsa (0,58 del ancho de la cara, centro al 54 % del alto, medido en el editable
de Eli) y en el vaso.

⚠️ Y ahí salió una corrección a la regla del manual: **la proporción del logo se
mide sobre la CARA VISIBLE, no sobre la silueta.** El 0,86 del vaso oficial está
medido de frente; en un vaso cercano y girado la cara visible es más angosta, y
aplicando 0,86 el logotipo se pasaba y la máscara lo cortaba — quedaba «ƎTWEEN /
OFFEE & BAR». A 320 px (la cara visible medida) se lee entero.

**✅ SUBIDO AL DRIVE, reemplazando por id** (las 5, verificado):

- **S1** → `C2 CUMPLEAÑOS BW`: Cumpleanos 1 y 2 detalles
- **S2** → Emergencia Between *(la que llevaba dos rondas sin subir)*
- **S3** → Promos To Go 1 portada y 4 los tres

⛔ **No se re-subieron** «Ella hablo Ella escucho» (aprobada) ni las slides 2 y 3
del To Go (nadie las objetó y la versión de la ronda 11 ya está revelada). Mover
la fecha de una pieza que el cliente no pidió cambiar sólo lo hace dudar.

`between-qa.py` limpio en 4 de 5. El aviso de `BW-F-Cumple-1` («texto a 1 px del
borde izquierdo») es el falso positivo ya documentado: son **dos píxeles** del
canto del plato, en y=1575 y 1596, de color (234,227,225) — gris neutro, no el
beige de marca. El texto de esa pieza está arriba, entre y=312 y 964.

**Herramientas nuevas, versionadas:**

- `scripts/between-cumple-r12.py` — las serpentinas doradas (`cinta()` dibuja una
  tira arqueada con acabado metálico) y `revela_por_sujeto()`
- `scripts/between-togo1-r12.py` — la portada generada entera, con el estampado
  enmascarado al cartón (`solo_sobre_el_carton()`)
- `scripts/between-togo4-r12.py` — la escena To Go con los dos logotipos
  estampados
- `scripts/between-r12-entrega-subir.py` — entrega a 150 ppp y reemplazo por id

**Abierto:**

1. **La ST 03-09 del cumpleaños (`BW-S-Cumple`)** sigue siendo una escena
   generada con una vela, mientras el feed de ese día ya es fotografía real.
   Está en CORREGIDO y el cliente no la reabrió.
2. **Los nombres de archivo siguen con las fechas viejas** (la grilla se re-fechó
   el 04-09). El portal levanta por nombre: renombrar hay que hacerlo junto con
   borrar la copia vieja.
3. **El duplicado «BW FEED 14-09 Promos To Go 4 trio.png»** sigue vivo en la
   carpeta antigua: hay que borrarlo a mano.
4. **`FEED!H16` (Primero la foto, 14-09)** sigue en REVISAR CONTENIDO con la
   pregunta de la CM sin responder: «¿Qué plato es el que ya está comido?».
5. **La mano de la portada tapa el canto de la «B»** del vaso. Con el logo a
   y=1300 se lee «BETWEEN / COFFEE & BAR» completo salvo ese borde; si se quiere
   intacto hay que cambiar el gesto, no el montaje.
6. **Avisarle a Scarlette que el mock de post volvió** (lo había pedido fuera en
   la ronda 5; volvió porque lo mandó Eli con su editable).

---

## 2026-09-04 · Eli (Windows) — BETWEEN ronda 11: las tres EN CAMBIOS, subidas

**Qué pedía la ronda.** Eli: corregir lo que está EN CAMBIOS en la S1, S2 y S3,
guiándose del brief, de los comentarios del cliente **sin tachar** y de los
mensajes de Scarlette; rehacer fondos; que se vea realista y no falso; que el
vaso To Go sea el actual; borrar rayones, imperfecciones y migas de las mesas. Y
dejó en el Drive **el editable de la slide 2 del carrusel de cumpleaños**
(`1kjIL3VuLnKH0ED3h8lx9kQ4GPUI5XHVF`) «para que lo mejores».

**Primero hubo que volver a leer la grilla, y ahí apareció el primer problema.**
La hoja `FEED` se **re-fechó entera** el 04-09: borró la SEMANA 1 y corrió el mes
—el cumpleaños del 3 al **9**, «Primero la foto» del 9 al **14**, «Ella habló»
del 11 al **16**, las Promos To Go del 14 al **22**—. Y el diff contra la copia
de la mañana salió corrido de columna porque
**`scripts/grilla-instantanea.py` tenía quemada la fila del ESTADO** (`FEED 15`,
cuando en Between es la **16**; la 15 es `COMENTARIOS DISEÑO`). Con eso el
encabezado imprimía el comentario en vez del estado y —peor— el filtro se
**saltaba toda columna sin comentario de diseño**: piezas enteras no aparecían.
Ya está arreglado: la fila se busca por su rótulo en la columna A. La instantánea
de hoy trae las 33 columnas de las tres hojas y **el diff de mañana ya sirve**.

**Las tres EN CAMBIOS, y qué se hizo en cada una:**

| Pieza | Estado / celda | Qué se hizo |
|---|---|---|
| **S1 · Cumpleaños** (FEED 09-09, carrusel) | `FEED!E16` EN CAMBIOS | Las dos slides pasan a ser **dos recortes 4:5 REALES** de la toma `25-257` (se cae el panorama espejado); mesa sin rayones; revelado por medios; **papelitos de colores** sembrados en la escena —el pedido de Scarlette que llevaba dos rondas anotado y no se veía—; el bloque de texto **sube** al muro libre (abajo caía sobre el hojaldre); y la G2 se rehace con **el mock de post de Eli**, corregido |
| **S2 · Ella habló** (FEED 16-09) | `FEED!J16` EN CAMBIOS | «Arriba ella hablo y abajo ella escuchó»: la escena se **voltea en vertical** para que la taza LLENA quede arriba, que es la que habló según el brief. Etiquetas re-medidas, logo arriba, mesa limpia |
| **S3 · Promos To Go** (FEED 22-09, carrusel) | `FEED!L16` EN CAMBIOS | **El revelado de las cuatro slides** (era el «filtro medio raro»), mesas sin rayones ni migas, el logotipo impreso del vaso de vuelta en las 4, fuera el segundo vaso del canto de la G4, canto de la figura fundido en la portada y re-encuadre para que el titular no le pase por encima al vaso |

**⭐⭐⭐ El hallazgo de la sesión, y cierra un reclamo de cuatro rondas.** El
cliente lleva desde el 31-08 diciendo «se ven quemadas y con un filtro medio
raro» y Eli «el vaso está erróneo». No era un filtro ni el estampado: **tres de
las cuatro fotos del carrusel To Go estaban SIN GRADAR**. Medido, calidez
(R̄ − B̄): la del sándwich 20,9 (gradada a `neutro`, el perfil del mes) contra
49,4, 40,7 y 35,1 de las otras tres. Por eso el vaso de la slide 2 se leía
impreso y el de las 3 y 4 «descolorido» — **es el mismo vaso de la misma
sesión**. No había que re-estampar nada: había que sacarle el velo cálido.

**Herramientas nuevas, versionadas:**

- `scripts/between-togo-r11.py` — el revelado de las 4 slides To Go, con
  `borra_rayones()` (rayones grandes **por CROMA**, que es lo que los separa de
  la veta), `limpia_mesa()` (migas incluidas: la del módulo compartido sólo
  cazaba marcas oscuras), `realza_impresion()`, `funde_canto_figura()` y
  `revive_el_muffin()`
- `scripts/between-cumple-r11.py` — los dos recortes reales del cumpleaños y los
  `papelitos()` con tamaño por cercanía, desenfoque según la profundidad de campo
  real y sombra de contacto
- `scripts/between-ellahablo-r11.py` — el volteo y la limpieza de la mesa
- `scripts/between-r11-entrega-subir.py` — entrega a 150 ppp y **reemplazo por
  id** en el Drive

**✅ SUBIDO AL DRIVE, y reemplazando en su sitio.** Las 7 piezas se actualizaron
**por su id**, así que conservan el enlace y el portal ve la versión nueva sin
que nadie reenvíe nada. Verificado en las tres carpetas (todas marcan 12:48–12:49):

- **S1** → `C2 CUMPLEAÑOS BW` (`1TfFCqNfQw0ucTwqvJD8iqft7Y__voRUw`): Cumpleanos 1
  y 2 detalles
- **S2** → `1Yh2Puq1ZEmbM2HaoTh-LUydKwtZRmpn1`: Ella hablo Ella escucho
- **S3** → `1QOreVz6NVYvuri9RAYQRMNiilV_IN8XZ`: Promos To Go 1, 2, 3 y 4

`between-qa.py` limpio en las 7 (el aviso de «titular 27 %» en `BW-F-EllaHablo`
es el falso positivo conocido: esa pieza **no lleva titular** porque el brief
pide que el chiste se lea en la imagen).

**⚠️ Los nombres de archivo quedaron con las fechas VIEJAS, y es a propósito.**
El portal levanta las piezas **por nombre**: renombrarlas crearía duplicados y
dejaría la versión anterior publicada. Renombrar hay que hacerlo junto con borrar
la copia vieja, y es decisión de Eli.

**Lo que se aprendió está en el manual** ([`CLAUDE.md`](CLAUDE.md) § RONDA 11):
los 10 puntos, con las mediciones. Los tres que más sirven para otras marcas:

1. **una fila de la grilla nunca se quema en un script** — se busca por rótulo,
   porque el cliente reordena la hoja sin avisar;
2. **si para llenar un encuadre hay que espejar más de un 10 % del ancho, el
   encuadre está mal elegido** — se cambia el recorte, no se teje;
3. **antes de retocar, prueba a mover el encuadre.** Sacó el vaso cortado del
   canto de la G4 y despejó el titular de la portada, las dos con un zoom del
   5–11 % y sin inventar un píxel.

**⛔ Y una corrección mía, antes de que causara daño.** Escribí que el editable
de Eli tenía un typo («ien cualquier horario»). **No lo tenía:** medí los
contornos del `exclamdown` de Raleway y el signo está bien construido — en esa
familia el `¡` tiene la misma silueta que una «i» de asta larga. El problema de
lectura sí es real, y se resolvió moviendo el signo al arranque de la frase
(«¡Disponible de lunes a viernes, en cualquier horario!»).

**Abierto, en orden:**

1. **Falta avisarle a Scarlette que el mock de post volvió.** La ronda 5 lo había
   sacado por pedido suyo («no me gusta como se ve como post, haría un check
   list») y ahora vuelve porque lo mandó Eli con su editable. Manda Eli, pero
   conviene que no llegue como sorpresa.
2. **`FEED!H16` (Primero la foto, 14-09) sigue en REVISAR CONTENIDO** con una
   pregunta NUEVA sin responder de la CM: «¿Qué plato es el que ya está comido?».
   Es la única novedad de la grilla de hoy que no se tocó — es contenido, no
   diseño.
3. **`STORIES!I16` (Emergencia, 09-09) sigue en REVISAR CONTENIDO.** Los dos
   productos ya se cambiaron en la ronda 10 (croissant de jamón queso y muffin)
   pero **esa pieza no se re-subió** y la del Drive es la del 02-09.
4. **El duplicado viejo «BW FEED 14-09 Promos To Go 4 trio.png»** sigue vivo en
   la carpeta antigua: hay que borrarlo a mano.
5. **La ST 03-09 del cumpleaños (`BW-S-Cumple`)** sigue siendo una escena
   generada con una vela, mientras el feed de ese día ya es fotografía real. Está
   en CORREGIDO y el cliente no la reabrió; unificarla es decisión de Eli.
6. **La mano tapa parte del «COFFEE & BAR»** del vaso en la portada To Go. Es lo
   que pasa de verdad al sostener un vaso impreso y la palabra se lee, pero si se
   quiere entero hay que cambiar el gesto, no el montaje.

---

## 2026-09-04 · Eli (Windows) — BETWEEN ronda 10 · 2.ª pasada: el revelado

**Qué pasó.** La primera pasada cambió el MATERIAL (producto real en vez de
generado) y Eli devolvió las cinco piezas igual: «se ve mal diagramadas», «no se
ve un retoque que se vea apetitosa las imágenes de comida», «el color está muy
oscuro», «tiene que ser realista y no pegoteado», «borrar los rayones de la
mesa», «hay un plato que se ve cortado».

**El diagnóstico, y es de método: faltaba el REVELADO.** Estábamos entregando la
foto del banco cruda. La sesión viene subexpuesta, la mesa de listones está llena
de marcas negras y el hojaldre sale plano — el paso que en un estudio hace el
retocador no existía. Ahora vive en [`scripts/between_retoque.py`](../../scripts/between_retoque.py)
(limpiar madera → revelar → apetitoso → nitidez) y lo comparten las cuatro piezas.

**Qué se rehizo, pieza por pieza:**

| Pieza | Cambio |
|---|---|
| Cumpleaños 1 y 2 | **Se dejó de montar.** Ya no se mueve el vaso ni se borra el plato: la slide 1 es la foto tal cual —el café CON las medialunas, como pidió Eli— y la slide 2 la misma mesa siguiendo. Mesa sin rayones, exposición arriba, hojaldre con claridad |
| ST Emergencia | Los tres productos con la luz del nicho aplicada, apoyados en una misma línea de base, con el reflejo del cristal ENCIMA (antes quedaban pegados sobre el vidrio) y el muffin aclarado. El café también pasó a ser el vaso real |
| To Go portada | Fondo de 26 a 13 px de desenfoque + **luz envolvente** en el canto de la figura + revelado. Era el «se ve mal montada» |
| To Go slide 4 | El plato del dulce entra ENTERO, mesa limpia, muffin aclarado y **fuera las etiquetas «Salado»/«Dulce»**: no cabían sin apretar la pieza y la caja de la promo ya nombra los tres |

**Lo que se aprendió está en el manual** ([`CLAUDE.md`](CLAUDE.md) § RONDA 10 ·
SEGUNDA PASADA): el orden del revelado; por qué el **gamma de medios** es lo que
arregla «está muy oscuro» y no subir las luces (que quema el hojaldre); por qué
la mesa aguanta el espejo y el muro no; las tres cosas que delatan un recorte
pegado —la luz del destino, lo que va delante, la línea de base—; y las dos
falsas alarmas del «vaso cortado» en la slide 4.

**⚠️ Un aviso del QA que es FALSO POSITIVO.** `between-qa.py` marca «texto a 0 px
del borde izquierdo» en `BW-F-Cumple-1` y `BW-F-ToGo-4`. No es texto: es el
hojaldre (231,228,207) y el borde del plato (210,222,221) pegados al canto, que
caen dentro del umbral con el que el QA aísla el beige de marca. Verificado
midiendo en qué filas cae. El texto de las dos piezas está centrado y con margen.

**Dónde quedó.** Renders en `out/hilton-between-r10/` y la entrega con nombre de
portal en `out/entrega-r10/`. **Sigue sin subirse nada al Drive**, esperando el
visto bueno de Eli.

**Abierto (viene de la pasada anterior):**

1. El duplicado viejo «BW FEED 14-09 Promos To Go 4 trio.png» hay que borrarlo a
   mano en el Drive: la entrega usa el nombre de la ronda 9 («…4 los tres.png»)
   para reemplazar la pieza viva.
2. La ST 03-09 del cumpleaños (`BW-S-Cumple`) quedó como estaba —está en
   CORREGIDO y el cliente no la reabrió— pero ahora el feed de ese día es
   fotografía real y la historia sigue siendo una escena generada con una vela.
3. **Avisarle a la CM que las medialunas se quedan.** Scarlette pidió «sacar el
   plato de los vigilantes» y Eli pidió lo contrario. Manda Eli, pero conviene
   que no llegue como sorpresa en la ronda siguiente.

---

## 2026-09-04 · Eli (Windows) — BETWEEN ronda 10: la cuenta deja de generar producto

**Qué pedía la ronda.** Un comentario NUEVO de Scarlette del 03-09 22:25 —
comentario nativo de Excel en `FEED!E15`, no en la fila 15, así que **leyendo
sólo la fila se pierde** (ya pasó en la ronda 5) — más dos pendientes sin tachar
que llevaban días en la grilla:

| Dónde | Estado | Qué pedía |
|---|---|---|
| `FEED!E15` · Cumpleaños 3-sep (S1) | EN CAMBIOS | «no les gusta la propuesta :( me piden usemos la imagen que te adjunto acá igual hay que retocarla, **cambiar el vaso al nuevo**, **sacar el plato de los vigilantes**, y poderle algo que haga ref a cumpleaños al rededor (quizas en la mesa poner como esos **papelitos de colores** que se lanzan) y la **imagen de la slide 2 tiene que tener relación** igual con la primera» |
| `FEED!L15` · To Go 14-sep (S3) | EN CAMBIOS | «el **fondo no tiene nada que ver con BT**, tenemos algunos videos que hemos hecho en la entrada de BT, saquemos el fondo de ahí?» |
| `STORIES!I15` · Emergencia 9-sep (S2) | REVISAR CONTENIDO | «Cambiaría que el **salado sea un crosant jamon queso** y que el **dulce sea un muffin**» |

Y encima, de Eli: la imagen de las dos slides del cumpleaños **continua**, con el
café en la primera; y del carrusel To Go, arreglar la portada («el vaso está
erróneo») y la slide 4 («mejora la foto y el vaso»).

**⭐⭐⭐ El hallazgo de la sesión, y cambia el método del mes.** El cliente lleva
**desde la ronda 4** reclamando lo mismo por cuatro caminos distintos —el vaso
con logotipo inventado, la taza con marca ajena, «nada que ver jajajaja», «que
no se vea tan IA»— y lo veníamos tratando como un problema de prompt o de
estampado. **No lo era: el producto está fotografiado y no lo estábamos usando.**
La carpeta `BETWEEN 25 JULIO MODELOS` del propio cliente
(`1gI00XGbBV5YjqcSjG3SmmkMuxr-ev_60`, 60 archivos) trae el vaso vigente solo, con
croissant de jamón queso, con muffin, con rol de canela y con los vigilantes —
todo sobre la misma mesa, el mismo muro y el mismo 50 mm.

Y el remate: **la foto que adjuntó Scarlette y `25-257` son la misma toma con 63
segundos de diferencia** (EXIF: 15:45:11 y 15:46:14, mismo cuerpo, mismo lente,
mismo diafragma). El fotógrafo hizo la mesa con el vaso viejo y con el nuevo, así
que «cambiar el vaso al nuevo» **ya estaba disparado**. Cero IA en el producto.

**Las 5 piezas, todas con QA limpio** (`out/hilton-between-r10/`, entrega armada
en `out/entrega-r10/` con el nombre del portal y 150 ppp):

| Pieza | Qué se hizo |
|---|---|
| `BW-F-Cumple-1` y `-2` (S1) | **Una sola fotografía real partida en dos slides.** Base `25-248`, plato de los vigilantes borrado, escena espejada para que el café quede en la slide 1 con su fondo y su sombra reales, y papelitos de cumpleaños sembrados sobre la mesa. Fuera el doodle de confeti: ya está en la escena |
| `BW-S-Emergencia` (S2) | Los dos productos de la vitrina cambiados por **recortes reales**: muffin de chocolate (dulce) y croissant de jamón queso (salado). Los textos de la encuesta no se tocan |
| `BW-F-ToGo-1` (S3) | Fondo = `HDT_56`, la foto de arquitectura del propio local (barra de mármol, mural dorado y el pasillo hacia el muro vegetal de la entrada), desenfocado. Vaso = el REAL de `25-248`, con los dedos devueltos encima |
| `BW-F-ToGo-4` (S3) | Bodegón **enteramente real**: café + croissant jamón queso (de `25-278`) + muffin en su plato (de `25-266`). Las cuatro coordenadas de etiquetas y flechas re-medidas |

**Herramientas nuevas, todas versionadas:**

- `scripts/between-recortes-reales.py` — recorta productos con grabCut y deja el
  alfa limpio en `public/assets/hilton/between/recortes/`
- `scripts/between-cumple-panorama.py` — el panorama continuo del cumpleaños
- `scripts/between-emergencia-productos.py` — cambia los productos de la vitrina
- `scripts/between-togo4-bodegon.py` — el bodegón real de la promo
- `scripts/between-togo1-real.py` — la portada con fondo del local y vaso real

**⭐ Y una de método que sirve a todas las marcas:** con
`https://drive.google.com/thumbnail?id=<ID>&sz=w4000` Drive devuelve **el archivo
ORIGINAL** aunque el token no tenga permiso, siempre que esté compartido por
enlace. Con `sz=w640` se arman hojas de contacto baratas. Así se eligieron las
fotos sin bajar 700 MB.

Todo el detalle técnico —los cuatro intentos fallidos de borrar el plato, por qué
espejar en vez de recortar, la proporción como prueba objetiva de que un vaso es
generado, y las dos trampas de grabCut— quedó en el manual,
[`clients/hilton/CLAUDE.md § RONDA 10`](CLAUDE.md).

**⛔ Lo que NO se hizo, y hay que decidir:**

1. **Nada se subió al Drive todavía.** Las 5 piezas están en `out/entrega-r10/`
   listas. Ojo con un detalle: la slide 4 del To Go está **DUPLICADA en el
   Drive** con dos nombres —«…4 trio.png» (ronda 7, carpeta vieja) y «…4 los
   tres.png» (ronda 9, en `S3 · BW`, que es la carpeta viva)—. El script de
   entrega ya usa el nombre de la ronda 9 para que la corrección REEMPLACE en vez
   de dejar una tercera copia, pero **el duplicado viejo hay que borrarlo a mano**.
2. **La ST 03-09 del cumpleaños (`BW-S-Cumple`) quedó como estaba.** Está en
   CORREGIDO y el cliente no la reabrió, pero ahora el feed del mismo día es
   fotografía real y la historia sigue siendo una escena generada con una vela.
   Es decisión de Eli si se unifica.
3. **El metraje de la entrada que menciona el cliente no está en el repo.** Se
   usó la foto de arquitectura, que es del mismo lugar. Si aparece el video, se
   cambia sólo la placa de fondo en `between-togo1-real.py`.
4. En la portada To Go, **la mano tapa parte del logotipo del vaso** — es lo que
   pasa de verdad al sostener un vaso impreso, y la palabra se lee, pero si Eli
   lo quiere entero hay que cambiar el gesto, no el montaje.
5. **Nano Banana Pro está sin créditos** (`HTTP 502 · Error consuming credits`).
   No hizo falta —todo salió de fotografía— pero conviene saberlo antes de
   planificar una pieza que sí necesite generar ambiente.

---

## 2026-09-03 · Eli (Windows) — DOUBLETREE: la marca entra al estudio, y su tipografía queda cerrada

*(Tercera sesión del día. Las dos de Between están más abajo.)* **Primera sesión de DT
en el estudio**: hasta hoy la marca no tenía ni una entrada en esta bitácora.

**Qué se hizo.**

1. **La grilla de DT es legible y ya tiene línea base.** Se modificó hoy 20:28Z
   (Carlos Figueroa) y no existía copia previa contra la cual diffear. Bajada con
   `export?format=xlsx` (49,5 MB, va a `raw/`, no viaja) y volcada a texto con el
   script nuevo `scripts/grilla-instantanea.py`, que conserva **tachados e
   hipervínculos** — que es justo lo que se pierde al copiar y pegar la celda.
   Queda en `clients/hilton/grillas/dt-septiembre-2026.md`. **Desde mañana la ronda
   nueva se detecta por diff.**

2. **Estado real de septiembre en DT.** Entregado y en Drive: `C1 FT` (APROBADO),
   `C1 ER DT S2` (CORREGIDA), `C2 ER FIESTAS PATRIAS` (EN REVISIÓN) y las 2 historias
   de la S1 (APROBADO). **Producible y sin empezar: 4 piezas** — el estático de
   Opinión Booking (14-09) y las historias de Escapada Romántica (07-09), Gimnasio
   (10-09) y Día del Turismo (27-09). Bloqueadas: los 2 reels (POR GRABAR, con
   Sebastián Serrano, y la grilla prohíbe IA ahí), el saludo de Fiestas Patrias
   (PENDIENTE POR CLIENTE), «Tu día en DoubleTree» (REVISAR CONTENIDO) y el reel
   orgánico del 10-09, que está EN CAMBIOS **con la celda de DISEÑO vacía**.

3. **⭐ La tipografía de DT quedó cerrada por regla de Eli: Stag + Trade. Raleway
   fuera.** Escrito en el manual. Las 11 fuentes están en el repo
   (`public/assets/hilton/dt/fonts/`): 9 cortes de Stag y los 2 de Trade que Eli
   consiguió por su cuenta —el cliente no las entregó—, **más su conversión a WOFF2**,
   porque venían en `.otf` CFF, el formato que hizo que Remotion rindiera 27 piezas de
   Between con una serif de reemplazo sin avisar.

4. **⭐⭐ El reparto Stag/Trade no es estilístico, es de cobertura de glifos.** Los 9
   pesos de Stag traen 354 glifos y **no incluyen `$ % ¿ ¡ @`**. Por eso los precios
   («$125.000»), las preguntas («¿Ya eres Hilton Honors?») y el correo del CTA
   (`reservas.dtv@hilton.com`) **tienen que ser Trade**: Stag no puede escribirlos.

5. **⛔ Un error mío, corregido antes de causar daño.** Medí el ancho `1`/`0` de la
   cifra, vi que no era Stag, y —porque el `Informe.txt` del `.ai` nombraba Raleway—
   escribí en el manual que las piezas entregadas estaban fuera de sistema. **Era
   deducción, no medición.** La segunda huella, alto del `$` ÷ alto del `0` (invariante
   a tamaño y peso), da **1,225** en la pieza contra **1,24 de Trade** y **1,55 de
   Raleway**: era Trade desde el principio. **No hay nada que rehacer.** La regla
   quedó en la memoria `adn-desde-editables`: una huella descarta, dos confirman.

**Dónde quedó.** Manual de la marca con la sección de tipografía de DT completa y
corregida; grilla en texto; fuentes instaladas y verificadas; `_estado-sync.json` al
día. **El ADN no está hecho todavía** — no hay `marca.json`, ni `reglas.yaml`, ni
`src/brand/doubletree.ts`.

**Lo ya medido, para no repetirlo:** mesa **1080×1350** → entrega feed **2250×2813** e
historia **2250×4000** (2,083×); tinta plana **PANTONE 2766 C**; azul medido `#0B194A`
en feed y `#111C4E` en historia (el manual dice `#09194E`, falta afinarlo sobre zona
plana); **logo con proporción 1,2266**, confirmada contra dos archivos distintos
(`JUNIO/DT/S3/logo DT.png` y el de Abril).

**Qué sigue.** El ADN sobre las 7 piezas aprobadas: retícula y márgenes, geometría de
la píldora y de la caja de beneficios con separadores, jerarquía del titular a dos
pesos de Stag. Con eso, `marca.json` + `reglas.yaml` + `src/brand/doubletree.ts` y las
plantillas de feed e historia.

**Abierto.**
- **Falta el Trade Bold de ancho normal.** Es el corte con el que está compuesta la
  cifra de la pieza aprobada (ancho `1`/`0` = 0,764; los dos instalados dan 0,654 y
  0,600). Con lo que hay, el sustituto es Bold Condensed No. 20, pero **al mismo alto
  de dígito la píldora pasa de ~630 px a ~410 px** — cambia la proporción del bloque.
  Decisión de Eli, mirando el render, no leyendo.
- **La grilla se contradice sola:** `VISTA MENSUAL` pone el estático Booking el lunes 7
  y el carrusel Escapada Romántica el 14; la hoja `FEED` los pone al revés. **Lo
  confirma Carlos**, y cambia la fecha de entrega.
- **Falta el contenido de la reseña de Booking**: texto literal, iniciales del huésped
  y rating. El cliente aprobó «el que sugiere Carlos»
  (`imagen_2026-08-14_112424991.png`), pero la carpeta de reseñas
  (`1Dlki995RRdwueFGlZOkF9rybf7maMJ5u`) no devuelve archivos por el conector.
- **`DT-S2.ai` declara Raleway** en su `Informe.txt`. No está verificado en qué
  elemento. Con la regla nueva, revisarlo cuando se toque esa pieza.
- **Licencia:** las fuentes las consiguió Eli, no el cliente. Vale saberlo antes de
  repartirlas a otro diseñador que clone el repo.

---

## 2026-09-03 · Eli (Windows) — BETWEEN: auditoría de reproducibilidad y respaldo

*(Segunda sesión del día. La ronda 9 está en la entrada de más abajo.)*

**Qué se hizo.** Se instaló un segundo estudio en `~/copylab/EDITOR VIDEOS` y,
al verificarlo, apareció el problema de fondo: **el repo no alcanzaba para
reproducir Between**. Se auditaron las 32 imágenes que usa
`BetweenSeptiembre.tsx` cruzándolas contra git, y las 27 composiciones de
`Root.tsx` contra el disco. Resultado: **19 piezas rinden, 8 no** — las 8 son
historias cuyas imágenes de origen no existen en ninguna parte.

**Dónde quedó.**
- `togo-salida-3.png` (18 MB) faltaba en git: `.gitignore:69` tapa
  `public/assets/**` y el `/cierre` anterior subió 21 de 22. Commiteada (`dd36a5a`).
- Los 9 scripts `between-*.py` y las 20 imágenes que existen: verificados en
  GitHub. **Los 16 carruseles se rehacen desde un clon limpio** — comprobado
  rindiendo `BW-F-Cowork-1` y `BW-F-ToGo-1` (1080×1350 ✓).
- Las 8 historias irrecuperables estaban **sólo en el disco externo `F:`**. En el
  disco interno había 3 historias rendidas y eran justo las 3 que sí se rehacen.
  Copiadas a `out/_respaldo-F-between-sept/` (SHA256, 27 de 27 idénticas) y
  **subidas a Drive**: subcarpeta `respaldo` dentro de `S3 · BW`
  (`1vr5rwVu84cmcgQDrj8yjhCfxcFZHGZyE`), 8 de 8 verificadas, con
  `scripts/between-respaldo-historias.py` (`aac0686`). Decisión de Eli: carpeta
  aparte para no interferir con la entrega.
- El manual de la marca ya trae la sección con las 8 composiciones rotas y la
  regla para octubre.

**Qué sigue.** En octubre, guardar las imágenes de origen junto con las piezas y
subirlas con `git add -f` el mismo día — hoy se salvó por el disco externo. Y
antes de cerrar un mes, cruzar composiciones registradas contra archivos en disco.

**Abierto.** Las 12 imágenes de origen de esas 8 historias no aparecieron: se
buscó por nombre y por palabra suelta en las 2.568 imágenes de
`F:\Carpeta de grillas Hilton 2026`. Si están en el Mac, vale la pena traerlas;
si no, esas 8 piezas sólo se pueden rehacer desde cero. **Avisar antes de
comprometer plazo si el cliente pide cambios ahí.**

---

## 2026-09-03 · Eli (Windows) — BETWEEN ronda 9: las 4 piezas EN CAMBIOS de la S1, S2 y S3

**Qué pedía la grilla.** `BETWEEN _ GRILLA SEPTIEMBRE 2026` marcó cuatro piezas
de FEED en `EN CAMBIOS` y ninguna de STORIES:

| | Fecha | Semana | Pieza |
|---|---|---|---|
| FEED C | 01-09 | S1 | Carrusel Cowork — **reabierto hoy** (`CORREGIDO` → `EN CAMBIOS`) |
| FEED H | 09-09 | S2 | Carrusel «Primero la foto… ¿o no?» |
| FEED J | 11-09 | S2 | Ella habló / Ella escuchó |
| FEED L | 14-09 | S3 | Carrusel Promos To Go |

**Las 13 láminas están entregadas y verificadas byte a byte en Drive.** La
portada del Cowork se REEMPLAZÓ en su sitio (mismo enlace,
`1cF7afo5tP4Lixq_YyGWyd7iQJIEw6kb1`); las otras nueve son nuevas, sueltas en la
carpeta de su semana como pidió Eli:

- **S1 · `C1 COWORK`** (`1GB6NtoG3vy35rPj7bw-j8bc76-Jz8332`) — portada nueva.
- **S2 · `BW`** (`1Yh2Puq1ZEmbM2HaoTh-LUydKwtZRmpn1`) — las 4 de «Primero la foto»
  + «Ella habló Ella escuchó».
- **S3 · `BW`** (`1QOreVz6NVYvuri9RAYQRMNiilV_IN8XZ`), que estaba vacía — las 4
  del To Go.

Se sube con `python scripts/between-subir-c1.py s2r9 s3` (el script dejó de tener
la carpeta de render quemada: ahora acepta `--render` y `--solo`).

**⭐⭐ El hallazgo, y es de material: las tazas de loza del cliente traen KIMBO
impreso al costado.** Por eso el reclamo se repite desde la ronda 4 sin que nadie
diera con la causa. En las tomas **cenitales** el logotipo no se ve —queda en la
pared exterior—, así que el reclamo no obliga a generar tazas: **obliga a elegir
cenitales**, que es justo la otra mitad de lo que pide el cliente («desde arriba,
como la refe»). Las cuatro slides del FEED H salen ahora de fotos REALES de la
sesión `3 ENERO _ PLATOS - DESAYUNOS` del propio cliente, todas cenitales, sobre
su mesa de listones — con eso se cae también «el lugar no se parece en nada a
Between». La única sin cenital equivalente (el croissant de jamón y queso) se
resolvió borrándole la marca con `scripts/between-quitar-kimbo.py`, que **rellena
interpolando el esmalte**: clonar una franja vecina dejaba un rectángulo visible
porque la taza tiene degradado lateral.

**La portada del Cowork es el LOUNGE**, por indicación de Eli. Scarlette había
comentado hoy 09:33 «el espacio de la slide 1 ya no existe :((( si vamos a
mostrar de fuera tendría que ser del espacio más amplio de la terraza»; manda lo
que dijo Eli. La foto es `espacios/HDT_37.jpg` y el encuadre se eligió **por
exclusión**: esa toma tiene una placa KIMBO atornillada al muro, una bolsa de café
KIMBO sobre la barra y **una persona con rostro reconocible** tras el vidrio. De
528 encuadres 4:5 anclados abajo, sólo cuatro no tocan ninguna de las tres zonas.

**⛔ Los videos de la entrada de Between NO existen en el material del estudio.**
El cliente los ofreció para la slide 1 del To Go («tenemos algunos videos que
hemos hecho en la entrada de BT»). Se buscaron en las 7 carpetas de `GRILLA IA
BETWEEN` y en todo `raw/` —incluida la sesión BW 2023 de 596 fotos y los 91
fotogramas de los 25 MOV— y **no hay un solo plano exterior**. La slide se
resolvió con el método que el manual ya tenía escrito (ronda 6 §2): el local
real entra **muy desenfocado**, pasado por referencia. **Si Eli consigue esos
videos, la slide se rehace con un fotograma y queda mejor.**

**Lo demás que cambió, por pieza:**
- **FEED J** — escena rehecha entera: dos tazas separadas en diagonal, arte latte
  en la llena y cerco de café seco en la vacía, una mano por taza. Las manos se
  revisaron al 400 % y son **de mujer**, porque el copy dice «etiqueta a esa
  amiga» y la primera generación puso una mano que leía como masculina. Los
  textos van **sin caja**, como pidió el cliente: se pudo porque la escena nueva
  los deja sobre mesa oscura.
- **FEED L slide 4** — entra el **brownie**. Al cambiar la escena hubo que
  **volver a medir** las etiquetas «Salado» y «Dulce»: con las coordenadas viejas
  una caía sobre el producto y la otra dentro de la caja de la promo.
- El logotipo del vaso se **re-estampó desde el archivo real** en las dos slides
  del To Go, aunque la generación lo devolvía legible: proporción 3,0278 exacta.

**QA 12/13 limpias.** La única con aviso es `BW-F-EllaHablo` («el titular ocupa
29 %»), y es **falso positivo**: esa pieza no lleva titular por brief. Queda
escrito en el manual junto al otro falso positivo conocido. `npm run typecheck`
limpio.

**⭐ 2.ª vuelta del mismo día — la portada del To Go.** Eli devolvió tres cosas y
la pieza está **re-subida al mismo enlace** (`1lhUHAgIi_6mXPEpe_Yqxg5eaxyvqxjgG`):

1. **Fuera el lockup de arriba** — «borra el logo principal ya que está en el vaso
   TO GO». Es la regla 8 del manual (el vaso ya firma) aplicada donde más se nota.
2. **El logotipo del vaso, rehecho.** El defecto no era el estampado sino **la
   toma**: la mano envolvía el vaso a media altura y dejaba sólo 70 px de cartón
   limpio, así que el logo entraba al 0,60 del ancho del cuerpo y pegado a la
   tapa. Se editó la foto pidiendo **la mano agarrando abajo y el vaso de
   frente**: el cuerpo pasó de 335 a 670 px y el logo de 200 a 520.
3. **El horario sin caja** — «se ocupó en el texto de promo». `PilaDatos` tiene
   ahora `datosSinFondo`.

⚠️ Y una trampa que costó dos generaciones: **al re-generar la escena completa el
modelo vuelve a meter una persona borrosa al fondo** (los espacios que van de
referencia traen gente). La salida fue dejar de generar y **editar la versión
buena** como única referencia — `between-togo1-salida.py --editar <imagen>`. Salió
a la primera.

**⭐⭐ 3.ª vuelta — el carrusel To Go completo, re-subido a la S3 (mismos enlaces).**

1. **⭐⭐⭐ Las cifras eran de ESTILO ANTIGUO.** «Los números no se ven uno más
   arriba y abajo que los otros» no es avance horizontal: en «$4.290» el 4 y el 9
   bajaban de la línea base. **Raleway las trae así por defecto** —no tiene
   `onum`, y `lnum` es lo que las sube a caja alta— y el `lnum` se había **perdido
   al borrar la declaración que también llevaba el `tnum` inútil**. Ojo: activarlo
   **cambia los anchos** (el «0» de ExtraBold pasa de 614 a 707), así que hubo que
   **re-medir las dos tablas** de `cifrasTabulares` sobre los glifos `.lf`.
   ⚠️ Quedan dos piezas ya entregadas con cifras viejas: `StToGoDulce` (ST 01-09)
   y `StCowork` (ST 16-09). Ninguna otra del mes tiene dígitos.
2. **«Promo To Go» sale de las slides 2, 3 y 4** — sólo va en la portada. Con una
   sola línea, cada pila queda en una caja (la del precio), y de paso se cierra
   solo el choque que había quedado abierto con el «que quede como en la slide 1
   y 2» de Scarlette.
3. **El logotipo del vaso, re-medido contra un vaso REAL** (`Between-67.jpg`): ahí
   va al 0,92 del ancho del cuerpo y **centrado en la vertical (0,485)**. Lo
   entregado iba en 0,13, o sea pegado a la tapa — eso era lo que se veía falso.
   Corregido a 0,72 / 0,32, que es el máximo que deja la mano: el rectángulo de
   cartón limpio de esta foto es `x 1027–1497 · y 2272–2427`.
   ⛔ **La composición no se tocó**: modelo, tamaño de mano y encuadre son los que
   Eli aprobó. Se probó bajar el agarre con otra generación y el modelo volvió a
   agrandar el vaso e inventarle una faja — se descartó.

**⭐ 4.ª vuelta — S2 APROBADA por Eli. En la S3 quedaban dos slides.**

- **Slide 1**: «la mano se ve gigante… y el vaso también». Cierto, y la causa es
  de método: **para que el logotipo entrara al tamaño del manual se había
  agrandado el vaso, y con él la mano.** Eso invierte la jerarquía — la escala de
  un objeto la fija el cuerpo que lo sostiene, no lo que necesita el estampado.
  Se volvió a la toma de escala natural y el logo se corrigió dentro de lo que esa
  foto da: pasa de 200 px **42 px a la derecha del eje** a 230 px **en el eje**.
- **Slide 4**: «se ve extraño el vaso y el logo». El defecto era la **proporción**:
  el vaso generado tenía alto/ancho **1,26** contra **1,02** del vaso real del
  cliente, o sea 24 % estirado. Se regeneró con el vaso real como referencia y el
  cartón liso, y se estampó a los ratios medidos.
- Slides 2 y 3, sin tocar. Las cuatro re-subidas a los mismos enlaces.

⚠️ Dos trampas que quedaron escritas en el manual: `--clonar abajo` trae lo que
haya DEBAJO de la caja (acá pintó el brownie sobre el vaso), y la geometría de
`flechaBucle` —punta en (0,58·0,06), cola en (0,03·0,97)— que costó tres renders
adivinar.

**Abierto:**
0. ✅ RESUELTO en la 3.ª vuelta: al sacar «Promo To Go» de las interiores, las
   cuatro slides quedaron con una sola caja y el carrusel volvió a leerse parejo.
   ⚠️ Pendiente en su lugar: **re-rendir `StToGoDulce` y `StCowork`**, que quedaron
   con las cifras de estilo antiguo.
1. **Los videos de la entrada de BT** — si aparecen, se rehace la slide 1 del To Go.
2. **STORIES no tenía nada `EN CAMBIOS`**: H es el reel Café Bombón esperando que
   el cliente conteste lo de la leche condensada, J está `POR GRABAR` y M/O/Q/R/T/U
   están `OK PARA DISEÑAR` — son piezas nuevas, no correcciones. Falta acordar con
   Eli si se toman.
3. **FEED G (7-sep)** retrocedió de `APROBADO` a `CORREGIDO` en la grilla el
   03-09. Probable error de tipeo del CM: conviene confirmarlo antes de tocarlo.

**⭐⭐ Y lo primero del día, que es lo que hizo posible todo lo demás: la grilla
SÍ se puede leer desde este PC.** El cierre de ayer dejó la S2/S3 sin tomar
declarando un bloqueo de acceso. Era falso. El token da 404 porque tiene alcance
`drive.file`, pero **la grilla está compartida por enlace**: baja entera y con
formato con un `curl` sobre `uc?export=download` (78.206.603 B, calzados contra
el `fileSize` de Drive), y `openpyxl` con `rich_text=True` devuelve el **tachado**
y el color de cada run. Los comentarios vigentes de H, J y L salieron en dos
minutos. Está escrito en el manual, § *CÓMO SE BAJA LA GRILLA*.

De paso, **la ronda de hoy 09:33 fue SOLO DE ESTADO**: 11 celdas cambiadas y cero
comentarios nuevos. El valor estaba en el cambio `REVISAR CONTENIDO` → `EN CAMBIOS`
de H, J y L —luz verde para diseñar con el brief que ya estaba escrito— y en que
lo entregado ayer quedó marcado `CORREGIDO`, la ST Emergencia incluida. Se detectó
por **diff celda a celda** contra la copia de ayer, no leyendo la fila 15.

⭐ Y quedó resuelta una de las 4 decisiones abiertas del documento de Constanza:
**el «Intercambiemos fechas con el de cowork» está TACHADO**, o sea muerto.

> ℹ️ Hallazgo que no es de Hilton pero conviene que se sepa: el `/al-dia`
> consultaba `constanza.lizana@copywriters.cl` y daba cero desde el 28-08. La
> grilla de Selfie es de **`constanza.olivares@`**, que sí tiene movimiento. Hay
> dos Constanzas en el equipo. Anotado en `clients/_estado-sync.json`.

---

## 2026-09-02 (cierre) · Eli (Windows) — BETWEEN: la ST «Emergencia» de la S2, rehecha entera

**Qué se hizo.** La **ST Emergencia (9-sep, S2)** completa. Eli pasó el brief y
los dos comentarios por chat —la grilla sigue sin poder leerse desde acá, ver la
entrada de más abajo—, y los dos decían lo mismo desde dos lados:

    Cliente:   «No se cacha bien al tapar la vitrina con el texto, veamos otra
                diagramación?»
    Scarlette: «no se parece a na ref, hagámosla más simple, NO ambientada en un
                lugar sino que tenga más PROTAGONISMO LA MISMA CAJA, y ojo con la
                diagramación de los textos: tapa mucho la caja.»

Al mirar la versión anterior fallaba en **cinco** cosas, y las cinco están en
esos comentarios: era un **nicho en una pared** —o sea ambientada, y **sin
vidrio** aunque el brief pide «caja de emergencia CON VIDRIO»—, el titular iba
**dentro** de la caja sobre la pared del fondo, y **faltaba un producto**: el
brief pide TRES (café, pastelería y sándwich) y había dos, mientras la encuesta
ofrecía «algo salado» que no estaba en cuadro.

Ahora: vitrina frontal con vidrio sobre fondo liso, tres compartimentos con los
tres productos, y **el texto fuera de la caja** —titular arriba, bajada y
encuesta abajo—. El vaso es el **To Go de Between**: se generó liso y se le
estampó el logotipo real al 0,86 del ancho del cuerpo (la proporción medida del
manual). Cuatro generaciones hasta dar con el encuadre.

⭐ **El tamaño de la caja es una RESTA, no un gusto.** El sticker de la encuesta
mide 196 px y la zona segura inferior de Meta empieza en 1580, así que la
encuesta no puede arrancar después de 1384. Con la generación tal cual —la caja
llegaba a y=1355— `between-qa.py` marcaba «entra 52 px en la zona segura». En
9:16 **o la caja es enorme y el texto la pisa, o el texto respira y la caja cede
altura**; no hay tercera opción. Se monta a 675 px de alto (64 % del ancho).

**Dos cosas de método que quedaron en el código:**
· El fondo se monta **ADITIVO** (`between-emergencia-montar.py`): se suma al
  lienzo sólo lo que el recorte se aparta de su propio fondo, en vez de pegar un
  rectángulo. Pegarlo dejaba una banda donde la sombra se cortaba de golpe.
· `TitularBetween` **deja de poner la sombra cuando el tono es `cafe`**. Esa
  sombra existe para que el beige se lea sobre foto; sobre crema sólo ensucia el
  contorno. Es la única pieza con ese tono, así que no re-fluja nada.

**Dónde quedó.** Drive, carpeta **`BW` de la S2**
(`1Yh2Puq1ZEmbM2HaoTh-LUydKwtZRmpn1`, que Eli abrió hoy y no cuelga del `BW` de
la S1): `BW ST 09-09 Emergencia Between.png`, 3,07 MB verificados byte a byte.
Se sube con `python scripts/between-subir-c1.py s2`.
Código: `StEmergencia` en `BetweenSeptiembre.tsx`. Scripts nuevos:
`between-emergencia-magnific.py` y `between-emergencia-montar.py`. Los tres
assets versionados con excepción en `.gitignore`.
**QA 7/7 limpias, typecheck limpio.**

**Qué sigue.** Las otras cuatro piezas de la S2: **FEED G** (7-sep), **H**
(9-sep), **J** (11-sep) y **L** (14-sep). Están descritas en la entrada de más
abajo con lo que pide cada una.

**Abierto:**
1. ⛔ **La grilla sigue sin poder leerse desde este PC** — es el bloqueo real
   para tomar la S2/S3. El detalle del porqué y cómo se destraba está en la
   entrada siguiente. Hoy la ST salió sólo porque Eli pegó el brief y los
   comentarios en el chat.
2. ⚠️ **La referencia de Pinterest del cliente no se pudo abrir**
   (`cl.pinterest.com/pin/1040683426409551586`): Pinterest sirve una página vacía
   a los bots y lo que se logró bajar era un pin RELACIONADO, no el suyo. La
   pieza se hizo con las indicaciones escritas. **Si Eli quiere que calce con ese
   pin, tiene que pegar la imagen.** Vale para cualquier próxima ref de Pinterest.
3. Las 4 decisiones abiertas del documento de Constanza (tipografía rígida,
   cifras tabulares, interlineado, y si el «intercambiemos fechas» ya está muerto).

---

## 2026-09-02 (noche) · Eli (Windows) — BETWEEN ronda 8b: el C2 Cumpleaños, y por qué la S2/S3 quedó trabada

**C2 CUMPLEAÑOS entregado** en su carpeta `1TfFCqNfQw0ucTwqvJD8iqft7Y__voRUw`.
Los dos cambios de TEXTO que pedía el cliente —sacar «en septiembre» y la
píldora «¡VEN POR TU CAFÉ DE REGALO!»— **ya estaban aplicados desde la ronda 7**;
se verificó sobre la pieza entregada antes de tocar nada.

⭐ **La lección de la sesión: cuando el cliente señala UNA foto como el look
bueno, se EDITA esa foto, no se recrea la escena.** Primero se generó una escena
nueva (una mano, vaso liso) y se le estampó el logotipo con
`between-logo-vaso.py`, que es lo que manda el manual desde la ronda 4. Eli lo
devolvió: «el logo se ve mal montado, utiliza la referencia, solo era que la tapa
no estuviera y fuera cappucino». Tenía razón: **la referencia ya traía el
logotipo REAL impreso, con su perspectiva sobre el cilindro**, y recrear la
escena obligaba a estampar — un sello plano sobre un cilindro se nota. La regla
del estampado sigue viva para cuando hay que generar de cero; **pero si existe
una foto con el vaso ya marcado, se edita esa.**

**Y la G2 cambió de fondo otra vez.** En la ronda 7 se cumplió «distinta a G1»
generando el muro vegetal desenfocado; pero la G1 de hoy pasó a ser el muro
vegetal con globos, así que volvían a chocar. Entra `bar-servicio.jpg`.

**⛔ La S2 y la S3 NO se tomaron, y el motivo es de acceso, no de tiempo.**
Eli pidió aplicar «los comentarios en rojo del cliente, lo que no esté tachado».
**Ese formato no se puede leer desde acá:**

- La grilla `BETWEEN _ GRILLA SEPTIEMBRE 2026.xlsx` (`1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY`)
  es de Sebastián Serrano y pesa **68 MB**. El token del estudio tiene alcance
  `drive.file`: **no puede leer un archivo que no subió** (404).
- El conector de Drive sí lo lee, pero devuelve **texto plano**: se pierden el
  color de fuente y el tachado, que es justamente lo que separa lo pendiente de
  lo ya hecho. Bajarlo en base64 por el conector son ~91 MB, inviable.
- **No existe versión nativa de Google Sheets** de la grilla de septiembre
  (comprobado: sólo hay nativas hasta marzo 2026), así que tampoco sirve la API
  de Sheets, que sí tendría permiso.

⚠️ **Aplicar la ronda a ciegas era el riesgo caro**: la fila de comentarios
mezcla lo pendiente con lo resuelto y lo resuelto va TACHADO. Sin el formato se
rehace trabajo ya aprobado — el error que el manual documenta desde la ronda 4.

**Cómo se destraba, en 10 segundos:** que Eli baje el .xlsx y lo deje en
`raw/hilton/between/`. Con el archivo local, el método ya está escrito en el
manual (`zipfile` sobre `xl/comments1.xml` y `comments2.xml`, más el color y el
tachado de `styles.xml`).

**Lo que sí quedó levantado de la S2/S3**, del documento de Constanza
«BETWEEN S2 septiembre — análisis de cambios en diseño»
(`1PIshvFqHZnLlS3Fz-z6lmkV1O2Aa1mAHwTYzX__alpA`, 02-09 13:04): son **5 piezas**
—FEED G, H, J, L y STORY I— con los comentarios nativos de Scarlette del 31-08
sin aplicar. Ese documento además deja **4 decisiones abiertas para Eli**
(tipografía rígida sí/no en toda la S2, cifras tabulares, unificar interlineado,
y si el «intercambiemos fechas» de L ya está muerto).

⚠️ Y OJO: Scarlette dejó **comentarios NUEVOS el 02-09 a las 17:02 y 17:03**
(«dejaron nuevos comentarios acá», «acá tomar estos nuevos cambios pliss»), o sea
**posteriores** a ese análisis. Hay una ronda más encima de la que el documento
describe.

---

## 2026-09-02 (tarde) · Eli (Windows) — BETWEEN ronda 8: la portada del Cowork, con la terraza real y la jerarquía del texto corregida

**Qué pidió Eli.** Dos cosas en un mensaje: (1) «usa de fondo la terraza de
between, con café en mesa y laptop + celular que sea estilo cowork pero mejor
editada la foto» y (2) «mejoremos cómo se ven los textos, deben verse mejor en
jerarquía visual… ojo crítico con los espacios entre líneas de los textos y
párrafos». Sólo la **C1 (portada)**, y entregada en una carpeta suya.

**⭐⭐ El hallazgo de la sesión: la terraza SÍ es de Between, y estaba probado
dentro de la foto.** El manual venía diciendo que de las 12 tomas de
`espacios/` sólo `HDT_50` estaba identificada, y advertía «varias no son de
Between —la barra de ónix parece de QB— preguntar antes». QB también tiene
terraza, así que la duda era real. No hizo falta preguntar: ampliando
`HDT_52.jpg` a resolución completa aparece un **pizarrón que dice «BƎTWEEN /
COFFEE & BAR / Desde las 17 hrs.»** con la E quebrada del logotipo, y en
`HDT_51.jpg` los portamenús dicen «BƎTWEEN · CAFÉ A $1.000». **Quedan
identificadas las dos como LA TERRAZA** (manual §7), y con ellas el método:
antes de descartar una foto por dudosa, buscarle la marca adentro recortando a
1:1 — una miniatura no muestra un pizarrón de 900 px en una foto de 6719.

**La foto.** Base `HDT_52` (6719×4479), recorte `(200,900)-(3063,4479)` = 4:5
exacto. **El encuadre se eligió midiendo**, no a ojo: se probaron 12 recortes con
las bandas del logo (0,05–0,14) y del texto (0,55–0,92) superpuestas, y en 11 la
mesa caía dentro de la banda del titular. El puesto de trabajo —laptop, taza
blanca lisa, celular, libreta— se generó con Nano Banana Pro **sobre esa misma
foto como referencia** (`scripts/between-portada-terraza.py`): la terraza real
está vacía, es fotografía de arquitectura, y no hay una sola taza en las 12
tomas. Gradada con `neutro`: calidez 30,8 → 20,7, a tono con las otras tres
slides (20,7–21,0).

**⭐⭐⭐ La jerarquía, que era el otro medio pedido y resultó ser un defecto de
sistema.** Medido sobre la entrega anterior, el salto ENTRE niveles era MENOR
que el salto DENTRO del nivel:

    script «Tu oficina por hoy»   alto 124,3   ancho 735 (68 %)
    ↕ 12,0        ← entre niveles
    caps «PUEDE SER»              alto  84,0   ancho 601 (56 %)
    ↕ 29,8        ← dentro del nivel

O sea el ojo agrupaba al revés. Y encima la script —que el kit define como
acompañamiento— salía **más ancha y más alta que el titular al que acompaña**.
Se corrigió con dos props nuevas y OPT-IN en `TitularBetween` /
`PiezaFeedBodegon` (`aireScriptATitulo` y `sizeScript` reenviada), **sin tocar
los tokens**, que habrían re-flujado todo lo aprobado. Ritmo final: 47,0 /
30,2 / 59,0 / 12,0. La caja taupe pasó de 1,16 a 1,24 de interlínea: era el
renglón más apretado de la pieza (ratio 0,24 contra 0,35 del titular).

⛔ **El titular NO se agrandó, y es decisión medida.** 117 da 84 de alto de caja
y 56 % de ancho = la referencia aprobada del manual (85 y 52 %). Cuando dos
elementos compiten se baja el secundario, no se sube el principal.

**Dónde quedó.** Drive, carpeta **`C1 COWORK`** de Eli
(`1GB6NtoG3vy35rPj7bw-j8bc76-Jz8332`, dentro de `BW` de S1 HILTON SEP 2026),
que estaba vacía. **Quedó el CARRUSEL COMPLETO, las 4 piezas**, todas
verificadas byte a byte: la portada nueva (10,53 MB) y las slides 2, 3 y 4 tal
cual se entregaron en la ronda 7 (4,76 · 6,09 · 4,43 MB), sin re-rendir. Se
sube con `scripts/between-subir-c1.py`, que reemplaza en su sitio si se vuelve
a correr. QA limpia y typecheck limpio.

⭐ **`C1` y `C2` son CARRUSELES, no slides.** La carpeta hermana es
`C2 CUMPLEAÑOS BW` (`1TfFCqNfQw0ucTwqvJD8iqft7Y__voRUw`), y hay una `STS`
(`14Z4XnkM9sepmdPV0XjKzoqb1HXMbvIzO`). O sea que Eli está ordenando la S1 **por
carrusel**, y cada carpeta lleva la pieza completa: «súbelas a ese drive, mejor
así tenemos todo». Al entregar una corrección suelta, subir igual las hermanas —
el cliente revisa el carrusel entero, que es como se publica.

**Abierto — tres cosas, en orden:**

1. ⚠️ **El celular queda parcialmente cruzado por la script.** Se hicieron **6
   generaciones** para subirlo a la fila de la taza y el modelo lo devuelve
   siempre al canto cercano de la mesa. Subir el encuadre lo despejaría, pero
   saca la lona oscura de la sombrilla de detrás del logo — y el logo es
   elemento de marca con QA (hoy mide luma 123,3 contra 159,5 de la portada
   anterior, o sea que quedó MEJOR). Se priorizó el logo. **Falta que Eli diga
   si lo da por bueno o si prefiere sacrificar el fondo del logo.**
2. ⚠️ **C1 y C2 ahora muestran las dos una laptop con un café.** C1 es el plano
   general de la terraza y C2 el bodegón a la altura del asiento, así que se
   leen como progresión —dónde estás / tu mesa— y la paleta verde amarra. Pero
   es repetición de sujeto en un carrusel que el cliente ya devolvió por
   cohesión. **Es consecuencia directa de lo que pidió Eli**; si le hace ruido,
   lo que cambia es la C2, no la portada.
3. ⚠️ **La misma inversión de jerarquía está en las slides 2, 3 y 4** (C2: 8,6
   contra ~35,5; C3: 20,2; C4: 8,2). Es una línea por slide, pero re-flujarlas
   mueve piezas que el cliente ya vio. **Falta el OK de Eli.**

## 2026-09-02 (cierre) · Eli (Windows) — BETWEEN ronda 7: la S1 completa, el To Go desbloqueado y las cifras tabulares resueltas de verdad

**Qué se hizo:** Llegó la **RONDA 7 del cliente** y se aplicó entera a lo que se
podía. Se entregaron **12 piezas**: la S1 completa (Cowork 1-4, Cumpleaños 1-2 y
las dos stories) y el **carrusel To Go de la S3, completo por primera vez**.
La **FEED G quedó APROBADA** por el cliente.

· **El Cowork, rehecho por cohesión.** El reclamo por WhatsApp era doble: la
  portada «no la usaría por temas de calidad y porque mostramos a esas personas»
  y «cambiaría las fotos para que tenga más cohesión». Portada nueva: el MISMO
  rincón del muro vegetal en el fotograma donde las dos personas ya salieron de
  cuadro (`IMG_1148-3`, elegido MIDIENDO dominancia de verde sobre los 91
  fotogramas: +9,2 contra +3 del resto). Slide 2 rehecha: era un bodegón de
  ESTUDIO sobre un muro verde INVENTADO —«la del medio que hace ruido», y encima
  el fondo falso imitaba el de la portada—; ahora el muro es el real, entrando
  por referencia y muy desenfocado. Slide 3 regradada a `neutro`: venía 8 puntos
  de calidez más fría (+12,4 contra +21 de las otras) y era la que rompía el
  tono. Y el texto de la portada cambió por pedido de Javier Meza: «Espacio para
  trabajar, WiFi y atención a la mesa».
· ⛔ **La slide 4 NO se regradó, y es decisión medida.** `neutro` le sube la
  luminancia de 77 a 95 y le levanta los negros: el tapete deja de ser negro y el
  latte pierde fuerza. Se probó, se miró y se descartó. El cliente tampoco la
  objetó.
· **Cumpleaños:** fuera «en septiembre» y fuera la píldora «¡Ven por tu café de
  regalo!» (el cliente se desdijo de su propia ronda 4), y la G2 con **fondo
  nuevo**, porque las dos gráficas usaban el mismo archivo con otro recorte.
· **Stories:** se eliminó la CTA «Pasa por Between y llévalo contigo» —el cliente
  borró su propia CTA del brief— y la promo pasó a «Café + Dulce To Go · desde
  $3.790». La story del cumpleaños arrastra los textos del feed por la regla de
  una sola voz.
· ⭐ **El sándwich del To Go, recuperado de raíz.** `togo-sandwich-45.jpg` nunca
  se versionó y sólo existía en el Mac de Valeria, así que la slide 2 no se podía
  rendir acá. La sesión COMPLETA del 25-jul-2025 está en el Drive del cliente
  (carpeta `1YQ_28BQpnBhTPNKnWXZmmaC6Bvr0BodD`, 353 archivos). Se bajaron las
  **353 miniaturas** para elegir sin traer 3,5 GB y el sándwich salió del
  fotograma **-248**: el único con el relleno de palta a la vista («rico y
  contundente», que es el copy) y el logotipo del vaso entero.

**Dónde quedó:**
· Drive, **carpeta única y fechada**, por decisión de Eli («solo deja una carpeta
  con cambios de fecha de 2 de sep»):
  `9. SEPTIEMBRE / CAMBIOS 02-09 BETWEEN v3 (tabular corregida - USAR ESTA)`
  → `1xLp2vSDej0xc6UnHS59RKUN8oM7uSa8H`. Las 12 piezas, **verificadas byte a
  byte**. Las v1 y v2 quedaron renombradas con `_` adelante y «NO USAR».
· ⚠️ **Las carpetas de semana quedaron INTACTAS y eso NO es un olvido.** El token
  del estudio tiene alcance `drive.file`: no puede sobreescribir las 8 piezas que
  Eli subió A MANO el 01-09, y el conector de Drive tampoco puede moverlas («The
  caller does not have permission»). Por eso la entrega va aparte y las viejas
  siguen en `S1/BW` con sus comentarios y sus enlaces.
· ⭐ **De acá en adelante sí se reemplaza en su sitio.** Las 12 las subió nuestro
  token, así que `scripts/between-subir-r7.py --actualizar "<nombre>"` cambia el
  contenido conservando enlace y comentarios. Es la primera vez que la cuenta
  queda en ese estado. El manifiesto con los fileId vive en
  `out/entrega-r7/_subidas*.json`.
· Código: `BetweenSeptiembre.tsx`, `BetweenSistema.tsx`, `BetweenRecursos.tsx`.
  Scripts nuevos: `between-slide2-magnific.py`, `between-cumple2-magnific.py`,
  `between-subir-r7.py`. Assets nuevos versionados con excepción en `.gitignore`
  (7 archivos: las 5 fotos gradadas y las 2 generaciones de Magnific).
· **QA 12/12 limpias** con `between-qa.py`, typecheck limpio.

**Qué sigue:** El **carrusel H (9-sep)** y el **estático J (11-sep)**. No están
bloqueados por archivos que falten: lo que pide el cliente EXIGE generar
imágenes nuevas — fuera la taza Kimbo de la G1 de H, la G4 con el plato más vacío
y cenital «como los 2 anteriores», y las dos tazas de J con arte latte y una que
se vea usada. La clave de Magnific funciona (`scripts/magnific.py check`) y los
dos scripts de esta ronda sirven de plantilla.

**Abierto:**
1. **Borrar las 8 viejas de la S1** para poder mover las nuevas a su sitio con
   `addParents/removeParents` (de las nuevas sí somos dueños).
2. **Desajuste de fechas en 3 stories.** La grilla rotó las tres primeras y los
   nombres de archivo quedaron con las fechas viejas: Promo To Go dice 01-09 y la
   grilla 03-09; Café de regalo dice 03-09 y la grilla 04-09; Según mis cálculos
   dice 04-09 y la grilla 02-09. No se renombraron a propósito: el portal levanta
   por nombre y renombrar DUPLICA en vez de reemplazar.
3. **¿La slide 4 del Cowork lleva logo?** Sin respuesta desde el 01-09.
4. ⭐ **El brownie de la slide 4 del To Go tiene candidato.** Los fotogramas
   **263–269** de la sesión 25-jul traen un dulce de chocolate CON EL VASO
   VIGENTE — el pendiente estaba trabado porque la única foto de brownie era del
   vaso antiguo prohibido. Es un muffin, no un brownie («pongamos un brownie
   aunque sea», dijo Scarlette): falta que Eli decida si sirve.
5. **Faltan 16 de las 31 fotos en este PC** (`public/assets` no viaja completo).
   Es el techo real de lo que se puede rendir en Windows.
6. La **Semana 1 ya no está congelada**: la ronda 7 trajo los cambios que se
   estaban esperando.

---

### Las cifras tabulares: resueltas en la 5.ª pasada (y por qué costó tanto)

Eli lo pidió **tres veces** y se rechazaron **cuatro implementaciones**. El error
nunca fue la idea; fueron dos cosas de implementación y una de diagnóstico.

**1. El ancho de la caja estaba mal.** Se usaba el avance del «0» (0,614 em), el
dígito más gordo, así que el «1» quedaba centrado en una caja que le sobraba por
los dos lados y «10:00» se leía «1 0:00». Lo correcto es el **ancho MEDIO de los
diez dígitos DEL PESO que se está pintando** — y el peso importa mucho: el «1» va
de 518/1000 en ExtraBold a 450 en Medium y 375 en la variable. Se eligió
rindiendo cuatro tratamientos con la fuente real, no de oído.

**2. Faltaba compensar los bordes del grupo.** Con el ancho ya bien puesto
quedaba un espacio doble entre la «a» y el «10»: el hueco de la caja del PRIMER
dígito se suma al espacio de la palabra anterior. Ahora `cifrasTabulares` agrupa
los dígitos consecutivos y les pone un **margen negativo exacto en los dos
bordes**, calculado con el avance real de cada dígito
(`ANCHOS_DIGITO_POR_PESO`). El hueco se reparte sólo por DENTRO del grupo, donde
son ~25 milésimas de em (~1 px a cuerpo 40) y se leen como espaciado normal.

**3. Y el diagnóstico que se me pasó dos veces: el desorden no eran los dígitos,
era la ESCALERA.** Para que la caja de la promo no cruzara el rol de canela había
partido el texto en dos cajas, y quedaron **tres cajas de tres anchos distintos y
las dos primeras en el mismo peso** — sin jerarquía. Eli: «se ve todo desordenado
en los textos y no se ve pulcro… cuidado que los textos se vean bien igual en
jerarquía». Se volvió a **dos cajas con una sola línea fuerte**, y el ancho se
resuelve con la prop nueva **`igualarAncho`** de `PilaEsquina` (todas las cajas al
ancho de la más ancha), no partiendo el texto.

⛔ **El atajo que NO sirve:** sacar la tabular de las líneas livianas. Se probó y
Eli lo devolvió señalando la story del 3-sep. Además el brief de esa pieza APILA
los números en dos líneas, o sea que ahí la tabular tiene que estar. Va en toda
la grilla. Todo escrito en `clients/hilton/CLAUDE.md § Las cifras tabulares`.

### Cinco defectos de margen que venían de antes, cerrados

`between-qa.py` marcó tinta fuera de los 84 px de margen en `ToGo1`, `ToGo3`,
`ToGo4`, `Cumple1` y `Cumple2`. Cuatro tenían la MISMA causa: la cola del «¿» de
Brushwell **sobresale del ancho de avance** con el que el titular se autoescala,
así que la caja cabía y la tinta no. Aparece en toda pieza cuya script abre con
«¿». Se componen en la columna (810) en vez del margen (912) — y para poder
apretarlo en las stories hubo que **agregarle la prop `columnaTitular` a
`PiezaStoryBetween`**, que no la tenía. El quinto era el globo doodle de
`Cumple2`, a 82 px del canto: se corrió 12 px.

### Dos trampas de scripts, cerradas

· `between-entrega.py` hacía `rmtree` de la carpeta de salida y **se llevaba
  `_subidas.json`**, el manifiesto con los fileId de Drive — sin él se pierde la
  capacidad de reemplazar en su sitio. Pasó hoy y hubo que reconstruirlo a mano.
  Ahora el manifiesto se preserva.
· El mismo script tenía la semana **quemada en `'S1'`** en la comprobación de ppp
  y reventó en cuanto entraron piezas de S3.

### Y una de método

**La ronda nueva se detecta por DIFF, no leyendo la grilla.** Los comentarios
nuevos se **prependen** sobre los viejos en la misma celda, así que sin comparar
contra la copia anterior del xlsx se confunde ronda nueva con ronda vieja — y el
bloque viejo puede estar CONTRADICHO por el nuevo (en E15 el cliente pedía en la
ronda 4 agregar «¡Ven por tu café de regalo!» y en la 7 pidió eliminarlo). El
diff también cazó que **dos comentarios nativos nuevos sólo AVISABAN** («dejaron
nuevos comentarios acá»), que la grilla había **ROTADO** las tres primeras
stories, y que **media ronda ya estaba aplicada** desde la ronda 5: lo que el
cliente marcó en el To Go era un render viejo que nunca se re-entregó.

---

## 2026-09-02 — Eli (Windows)

**Qué se hizo:** Arrancó la **ronda 6 de la SEMANA 2** de Between, que son los
comentarios nativos de Scarlette del 31-08 (G15, H15, J15, L15, I15) que seguían
sin aplicar. Se cerraron **2 de 11** piezas y se entregaron a Drive.

· **FEED G (7-sep) APROBADA por Eli.** Foto nueva. El fondo de la r4 era una
  terraza tropical y Scarlette tenía razón, pero mi primera corrección perdió lo
  bueno: quedó una sala vacía y fría. Eli lo marcó —«en el post más se parece la
  ronda 4»— y la versión final es la síntesis: el plano corto y la calidez de la
  r4 con el espacio real del local MUY desenfocado detrás, transferido por
  REFERENCIA desde `raw/hilton/between/espacios/`. Gradada con perfil `neutro`
  (calidez 54,7 → 21,9). Tipografía rígida (fuera Brushwell), comillas y punto
  del brief, bloque abajo.
· **STORY I (9-sep)** rendida y entregada con los textos del brief: el
  «¿CUÁL TOMARÍAS?» que faltaba entero, las 4 opciones literales con «algo
  salado» recuperado, y la encuesta en 2×2 para no invadir la zona segura.
· El **llavero del estudio** quedó funcionando en este PC: `abrir`, `estado`,
  `logins` y `magnific.py check` (✓ VÁLIDA). Los dos scripts nuevos reventaban
  con UnicodeEncodeError al imprimir el «✓» DESPUÉS de haber hecho el trabajo —
  arreglados, van 9 scripts con el fix de cp1252.

**Dónde quedó:**
· Entregadas en Drive **S2 HILTON SEP 2026 / BW**
  (`1Yh2Puq1ZEmbM2HaoTh-LUydKwtZRmpn1`): `BW FEED 07-09 Humor cafecito.png` y
  `BW ST 09-09 Romper en caso de antojo.png`. Verificadas byte a byte.
  ⚠️ Quedan a nombre de **valeria@copywriters.cl**, porque el token del llavero
  es el de la cuenta del estudio, no el de Eli.
· Copia de trabajo para Eli en `COPYLAB-ENTREGAS\BETWEEN-S2-SEP2026` dentro de su
  carpeta de usuario — fuera de OneDrive, Escritorio, Documentos y Descargas, por
  pedido suyo (esos tres se vacían y el estudio se rompe en silencio).
· Código: `BetweenSeptiembre.tsx`, `BetweenSistema.tsx`, `BetweenRecursos.tsx`,
  `scripts/between-qa.py`. Fondo nuevo versionado con excepción en `.gitignore`:
  `ia-sept/humor-cafecito-4.png` (+ el descarte `-3` para documentar por qué).
· Material recuperado de Drive a `raw/hilton/between/desayunos-ago2026/` (28
  tomas) y `raw/hilton/between/togo-25jul2025/` (el original -257 de 5760 px).
  **`raw/` no viaja en git**: quien retome tiene que volver a bajarlo de
  `GRILLA IA BETWEEN`.
· Página de revisión con antes/después:
  https://claude.ai/code/artifact/6c7b1871-1a2c-47b0-8813-c8eca17294a0

**Qué sigue:** El **carrusel L (To Go, 14-sep)**, que es el más avanzado: falta
regradar las 4 slides con `neutro` —es el «se ven quemadas y con un filtro medio
raro» de Scarlette— y recortar el sándwich desde el original de 5760 px que ya
está bajado. Después el **carrusel H (9-sep)**, que necesita 2 imágenes
generadas, y la **J (11-sep)**, que hay que rehacer completa.

**Abierto:**
1. **La STORY I ya está entregada pero SIN visto bueno de Eli.** Scarlette pidió
   «más protagonismo la caja» y el producto se ve chico dentro de un nicho muy
   vacío. Si se regenera, el archivo se reemplaza con `--actualizar` y conserva
   el enlace que el cliente ya tiene.
2. **El croissant de jamón y queso de H3 NO EXISTE en el banco.** Las 28 tomas de
   `BETWEEN DESAYUNOS AGO 2026` son huevos, tostadas y palta — ni un croissant. Y
   vienen en **1620×1080**, o sea que no alcanzan los 2250 px de entrega. Falta
   saber si existen los originales grandes de esa sesión.
3. **La J necesita DOS manos**, porque Scarlette pide que se vea la interacción de
   las personas «aunque sea sus manos» — y dos manos es justo lo que hubo que
   descartar hoy por anatomía. Se le preguntó a Eli si tiene foto real; sin
   respuesta todavía.
4. **El brownie de la slide 4 de L**: Scarlette lo pide, y la única foto de
   brownie del banco es de las del **vaso antiguo**, que está prohibido.
5. **La SEMANA 1 está CONGELADA** por decisión de Eli: vienen cambios nuevos y le
   avisan de nuevo. NO se reemplaza `BW ST 01-09` en Drive, aunque su defecto de
   margen ya esté corregido en el código.
6. Sigue sin respuesta desde el 01-09: **¿la slide 4 lleva logo?**

---

### Los tres bugs de sistema que salieron hoy

**1. `PilaEsquina` nunca aplicó su margen.** Decía `[lado]: BETWEEN.bloque.margenX`
y `lado` vale «izquierda» o «derecha»: la clave calculada salía `izquierda: 84`,
que NO es una propiedad CSS. React la ignoraba y la caja quedaba pegada al borde
del lienzo en x=0, **cortada**. Lo cazó el QA en `BW ST 01-09`, que ya estaba
entregada, con la tinta a 22 px del canto contra los 84 de margen. Afecta a toda
pieza con `PilaEsquina` — las slides 2, 3 y 4 del carrusel To Go se arreglan
solas al rendirlas.

**2. ⛔ Las cifras tabulares NO van en texto corrido.** Eli pidió el 01-09 que los
precios se vieran «opentype tabular, como en Adobe Illustrator». Se construyó a
mano —Raleway **no trae la función `tnum`**, verificado en la tabla GSUB/GPOS de
los 5 pesos instalados y de la variable, así que el CSS que había era decorativo
y el «Tabular Lining» de Illustrator tampoco tendría efecto— y **Eli lo rechazó
al verlo rendido**: «los textos y números vuelven a verse extraños, en la
anterior estaba mejor». Tenía razón. Las tabulares existen para que los números
**cuadren en COLUMNA**; acá van DENTRO de una frase («desde $3.790», «08:00 a
10:00 hrs») y forzar cada dígito al ancho del más gordo dejaba al «1» flotando
con un hueco a cada lado: el «10:00» se leía como una palabra partida. En texto
corrido lo correcto son las PROPORCIONALES, que es lo que Raleway trae de
fábrica. Se retiró de los 8 sitios donde se había aplicado; el helper
`cifrasTabulares` queda en `BetweenSistema.tsx` **documentado y SIN USO**, para
el día en que una pieza apile precios en filas.
Los anchos medidos siguen siendo ciertos (em de 1000): 0=614 · 1=518 · 2=580 ·
3=569 · 4=578 · 5=558 · 6=608 · 7=576 · 8=607 · 9=589. El «1» es 18,5 % más
angosto que el «0».

**3. El QA confundía el logotipo con el titular** — y lo rompí dos veces más al
arreglarlo. El lockup se detecta como UNA banda de 118 px, más alta que una línea
de titular (~85), así que `max(alto)` elegía el logo y reportaba «el titular
ocupa 24 % del ancho» —los 263 px del logo— en piezas con el titular al 73 %.
Filtrar por la zona del lockup falló primero porque mezclé las zonas de los dos
formatos (las del story caen donde el feed pone su texto, y descartaba las tres
líneas correctas de «Cowork 2»), y después porque **«Emergencia» no lleva logo**
—el vaso ya trae el logotipo impreso, regla 8— y su titular ocupa legítimamente
esa franja. Ahora mide **la banda MÁS ANCHA**, que no depende de dónde esté el
logo y es lo que la regla quiere saber.

### Y una de método
Las manos se revisan **con zoom, no a ojo**. Se descartaron DOS versiones de la
G: en una la mano de arriba no resolvía —un dígito con uña, otro parcial al borde
y entre ellos una masa lisa sin nudillos—. Se bajó el riesgo a **una sola mano**,
y la duda que quedaba (dos uñas juntas al lado del asa) se resolvió con zoom 4×:
era un dedo más la sombra del asa.

---

## 2026-09-01 (cierre) · Eli (Windows) — BETWEEN ronda 6: la foto de la slide 2, la gradación neutra, y el brief de la slide 4 que estaba mal anotado

> ⚠️ **Tercera sesión del día sobre el mismo repo.** Mientras ésta trabajaba, otra
> commiteó `f22209e`. No se perdió nada —se verificó archivo por archivo— pero ya
> van dos días seguidos. **Una sola sesión por repo.**

**Qué pidió Eli.** «Mejoremos el carrusel de la S1 según lo que dice Scarlett y lo
que describe el brief. Mantén los textos, están correctos. Pero las fotografías del
fondo no corresponden.»

**El defecto era peor de lo que se veía.** Las slides 1 y 2 usaban **el mismo muro
verde**, y la slide 2 decía «al menos que sea con buen café / encuentra tu mesa»
sobre una foto **sin mesa, sin café y sin PC**. Es literal el comentario C15 de
Scarlette del 31-08: «acá estamos hablando de café como tal, yo cambiaria la imagen
donde se vea una mesa con un pc y un café».

**La foto ya existía.** `raw/hilton/between/ediciones-ia-eli/magnific_agrega-una-laptop-en-la-m_iAi90W63uK.png`
— mesa de madera, laptop, vaso con el logo BETWEEN, muro verde desenfocado atrás.
**No se generó nada con IA**: la regla del manual es agotar el banco antes de
generar, y el banco la tenía. Recortada 4:5 con `--top 0.20` (el follaje queda
ARRIBA, donde se apoya el bloque de texto).

**La gradación: perfil `neutro`, sin tocar el ADN.** El otro reclamo de la ronda 5
—«eliminar el filtro de color cálido que tiene el carrusel completo»— seguía
pendiente. En vez de mover el objetivo por defecto, que está MEDIDO sobre las
piezas aprobadas de Eli y habría re-flujado todo lo entregado, se abrió un segundo
perfil en `between-gradar.py`:

| | `eli` | `neutro` |
|---|---|---|
| calidez (R−B) | 50 | **20** |
| p95 (altas) | 227 | **210** |
| lum · p05 | 118 · 24 | iguales |

La prueba de que +20 no es frío: las fotos crudas del 2.º piso vienen en **+27**, o
sea el perfil las deja **bajo su propio natural**. Saca filtro, no lo suma.

**Qué se movió y qué no.**

| | |
|---|---|
| slide 1 | sólo regradada (+33,2 → +21,4). Diagramación intacta |
| slide 2 | foto nueva. **Texto sin tocar** — la tinta mide 687/721/601 px, igual que la r6 |
| slide 3 | **SIN TOCAR**, idéntica píxel a píxel (delta 0). Ya venía en +12,4 |

QA **4/4** limpias · `tsc` limpio · entregadas a `Escritorio\S1 BETWEEN` (ahí seguían
las de las 15:20, previas a la corrección de jerarquía de la r6).

⚠️ El archivo de la slide 2 **sigue llamándose «Cowork 2 winter garden»** a
propósito: el portal levanta por nombre y renombrarlo crearía un duplicado.

---

### ⭐ La slide 4: el brief pedía otra escena

Eli pasó el brief textual, y no coincidía con lo anotado. El manual, el comentario
del código y el prompt de Magnific decían **«una trabajadora sin rostro preparando
café»** — un pedido dicho al pasar, que mandaba a generar **el bar**. El brief dice:

> «Persona trabajando mientras un colaborador deja un café o plato sobre la mesa.
> El usuario continúa trabajando sin tener que levantarse.»

Son **dos personas y una MESA**, no un mesón. Dicen cosas opuestas: el bar cuenta
que el café *se va a buscar*; el brief vende el **servicio a la mesa**. Y el bar
repite el escenario de la portada.

**La lección, escrita en el manual y en la memoria:** un criterio dicho al pasar
manda sobre el **CÓMO** (tipografía, logo, color, jerarquía), **nunca sobre el QUÉ**
la pieza tiene que mostrar. Si chocan, manda el brief.

Los textos de la slide **ya eran literales del brief**: no se tocó ninguno.

**El banco está agotado, y quedó demostrado:** `espacios/` son 12 tomas de
arquitectura **vacía**; de los 91 fotogramas del 2.º piso, los que tienen gente son
huéspedes **con la cara reconocible**, nadie sirviendo, y son del **1.er piso**. Ahí
sí se justifica generar.

`scripts/between-slide4-magnific.py` **reescrito entero**: escena nueva,
referencias del 2.º piso real, y los tres reclamos de la ronda 4 convertidos en
restricciones (cero caras por construcción · trabajo y no desayuno · las manos
contadas). Más un QA de 5 puntos y la receta de gradado/render/entrega.

---

### ⛔ Magnific: no se pudo, y hay que saber por qué

- `~/.magnific_key` tenía **la contraseña de la cuenta** (`DISEÑO2025-VIDEOS`, 17
  caracteres), no una clave de API. Verificado con `magnific.py check`, que
  **no gasta créditos**: HTTP 401.
- **Magnific muestra la clave UNA SOLA VEZ.** En el menú de la fila sólo hay
  «Editar clave API», «Copiar secreto del webhook» y «Eliminar clave API» — no hay
  forma de volver a verla. Para recuperarla hay que **borrar `claudecw` y crearla
  de nuevo**, copiándola en el momento. El plan está en el tope de claves, así que
  primero se borra.
- Créditos NO son el problema: las 3 claves están activas con **1,8 M disponibles**.
- El MCP `magnific` **ya está registrado** en `~/.claude.json`
  (`http · https://mcp.magnific.com`) pero **sin autorizar**. Se autoriza con `/mcp`
  y después hay que abrir **chat nuevo**.
- ⚠️ El binario `claude` **no existe en este PC** (se usa la extensión de VS Code),
  así que `claude mcp add` no corre. Hay que editar la config a mano.

Queda listo en el Escritorio, carpeta **`SLIDE 4 - para Magnific`**: el `PROMPT.txt`,
las 3 referencias renombradas y un `LEEME.txt` con el QA de 5 puntos. Se genera a
mano en la web y yo hago recorte, gradado, render y QA.

**⭐ Dirección final de Eli:** «una persona dejando el capuccino, que no se vea el
rostro». O sea **UNA sola persona**, no las dos del brief. El prompt se ajustó a
eso, y de paso es más seguro: cada mano de más es una posibilidad de error
anatómico, y «hay una mano de más» ya fue un rechazo.

**Se buscó la mano en el banco y NO estaba.** Revisadas las 42 ediciones con IA de
Eli: las que tienen manos sin rostro son **todas de la serie To Go** —sostienen el
vaso de papel o una bolsa, en el mesón— y ninguna deja una taza de cappuccino en
una mesa. Montar una mano de otra foto es justo como se produce el «hay una mano
de más», así que **no se hizo**.

**⭐ Y NO hizo falta: Eli mandó fotos propias.** Dejó tres en `out/hilton/`
(`between-39/40/42.jpg`, 1500×2250, del bar de Between) y con eso la slide se
resolvió **sin generar nada**. Magnific quedó pendiente para otra cosa, no para
esto.

---

### ⭐ La slide 4, resuelta con foto real de Eli

La dirección fue: «una persona dejando el capuccino, que no se vea el rostro».
De las tres que mandó se eligió **`between-42.jpg`** — dos manos presentando la
taza terminada, con el corazón en el latte, sin ninguna cara.

**Por qué esa y no las otras dos:** la 39 y la 40 son el momento de **PREPARAR**
el café en la máquina, o sea el bar — y el bar cuenta que el café se va a buscar.
La 42 es el de **ENTREGARLO**, que es exactamente lo que dice el titular.

Verificado con zoom, no a ojo: **taza blanca limpia, sin raya ni logotipo** (regla
KIMBO), **dos manos con anatomía correcta y ninguna suelta** — que fue el rechazo
textual de la ronda 4.

**⚠️ NO se gradó, y es a propósito.** Venía en **calidez +8,2**, más FRÍA que el
objetivo del perfil `neutro` (+20). Pasarla por el gradador la habría **calentado**
—justo lo contrario de lo que reclamó el cliente— y le habría subido la luminancia
de 79 a 118, lavando el ambiente oscuro que es lo que la hace buena. Sólo recorte
4:5 y llevada a 2250 px. La ampliación de 1,5× se verificó al 100 %: la crema y el
borde de la taza quedan limpios.

**El recorte va pegado ARRIBA, y eso también se decidió rindiendo las dos:** con el
recorte abajo la taza sube y **la caja taupe le tapa el corazón del latte**. Pegado
arriba la taza cae al ~67 % del alto, el texto se apoya en el tapete oscuro y el
corazón queda libre.

Es la **única slide oscura** del carrusel. No es descuido: cierra la secuencia
—el lugar, tu mesa, los espacios, el café que te llega— y el cambio de clave se lee
como remate. Si algún día se quiere pareja con las otras tres, se sube la luz; se
dejó así con el visto bueno de Eli.

**Quedó `servicio-mesa.jpg` en el repo** (la mesa del 2.º piso con el café servido)
como el paso intermedio del día. No la usa ninguna pieza, pero es una foto válida
del 2.º piso por si sirve.

**APROBADO por Eli.**

---

### El estudio en Windows

- **Séptimo script caído por cp1252.** Windows lee y escribe la consola en cp1252 y
  revienta con «✅», «→» o una «Á» — a veces **después** de haber hecho el trabajo,
  así que parece que falló y estaba listo. Arreglados hoy: `between-qa.py`,
  `hoja-contacto.py`, `verificar-fuentes.py` (reventaba dos veces: al leer la ficha
  y al imprimir el error) y `qa/motor.py`.
  **Quedan ~25 lugares más** en `scripts/` que abren archivos sin declarar
  codificación, casi todos de marcas de Paulina y Coni. **Eli tiene que decidir si
  se hace el barrido completo** — es un cambio grande.
- **`pyyaml` instalado**: faltaba y el motor de QA moría antes de leer una regla.
- **Hilton no tiene `reglas.yaml`** — el motor lo dice claro ahora. Es la única
  marca de Eli sin QA por programa. Hay dos reglas medidas listas para entrar (la
  columna y la gradación), **pendiente que Eli las firme**.
- **Hilton tampoco tiene `marca.json`**, y por eso `verificar-fuentes.py` ni siquiera
  la revisa. Sus fuentes funcionan igual (Brushwell y Raleway están en el repo).
- Las **14 tipografías sin resolver NO son de Hilton**: son de Casablanca y Cava
  (Paulina) y de MyZoo y Selfie (Coni). Vale avisarles: hasta que las activen, sus
  piezas salen con la fuente equivocada sin que nadie lo note — que es exactamente
  lo que pasó con Brushwell y costó 27 piezas.

---

### Qué sigue, en orden

1. **Subir a Drive arrastrando** las **4** Cowork a `C1 COWORK` y las 2 Cumpleaños
   a `C2 CUMPLEAÑOS BW`. Sin token. Es lo primero.
2. **Sacar del medio las de la ronda 4** en `BW` — pedírselo a Valeria.
3. **La clave de Magnific** — ya NO bloquea la S1, pero sigue pendiente para lo que
   venga: borrar `claudecw`, recrearla y copiarla en el acto (Magnific la muestra
   una sola vez), o autorizar el MCP con `/mcp` + chat nuevo.
4. **Cambiar la contraseña** `DISEÑO2025-VIDEOS`: estaba en texto plano y quedó en
   el historial de la conversación. También regenerar el **secreto del webhook** de
   `claudecw`, que se pegó en el chat.
5. `credentials/token.json` — para las correcciones futuras, no para esta entrega.

**Abierto.**

1. ~~Slide 4 sin foto~~ **RESUELTA y aprobada.** El carrusel está completo, 4/4,
   con foto real de Eli. No quedó nada pendiente de esta pieza.
2. **¿La slide 4 lleva logo?** Sigue sin respuesta desde ayer. La regla escrita dice
   que en carrusel el logo va sólo en la portada, y se respetó.
3. **Barrido de codificación** (~25 lugares) — esperando el sí de Eli.
4. **`reglas.yaml` de Hilton** — esperando que Eli firme las reglas.
5. Sin cambios: el **listado del cumpleaños de CINCO ítems** contra los cuatro de
   nuestra pieza, y el **Café Bombón** esperando al cliente.

**Páginas de revisión.** Ronda 6 con antes/después:
`https://claude.ai/code/artifact/2a18c52f-d2c3-49d5-acc4-5a526046b2b6` ·
Paso a paso de lo que le toca a Eli:
`https://claude.ai/code/artifact/44ff22ef-5c0e-437a-93c1-2e360cb48331`

---

## 2026-09-01 (noche) · Eli (Windows) — BETWEEN: la COLUMNA como medida de composición, la slide 4 de vuelta, y dos bugs del doctor

> ⚠️ Esta entrada funde las **dos** que quedaron escritas esta noche: hubo otra vez
> dos sesiones sobre el mismo repo (la otra commiteó en `e14047e`, 16:32). Se
> conserva todo lo de ambas. **Conviene una sola sesión por repo.**

**Qué se hizo.** Segunda pasada del día sobre la S1. Eli marcó el carrusel Cowork
ya entregado: **«los textos están muy grandes y desproporcionados, mejorar la
jerarquía visual y el espacio entre textos»**. Se midió sobre los PNG (no a ojo) y
apareció un defecto de sistema, no de la pieza: `TitularBetween` y `PanelTaupe`
achicaban el texto **hasta caber en el margen** (912 px = 84,4 %), que está por
encima del `anchoMax: 0.8` que declara el propio kit. Resultado: cada slide se
achicaba por su cuenta y el carrusel salió con **tres cuerpos de titular distintos**
(117 · 99 · 88) — al deslizar, el titular cambiaba de tamaño.

| | slide 1 | slide 2 | slide 3 | **ref. aprobada** |
|---|---|---|---|---|
| ancho del titular | 55 % | **84 %** | **84 %** | **52 %** |
| cuerpo real | 117 | **99** | **88** | **117** |
| caja taupe | 50 % | 77 % | **84 %** | **55 %** |

**La regla que quedó escrita** (`clients/hilton/CLAUDE.md § LA COLUMNA`):

- El **margen (84 px) es un LÍMITE**; la **columna (`BETWEEN.bloque.columna` = 810 px
  = 75 %) es la MEDIDA** en la que se compone.
- En un carrusel, **las slides interiores comparten UN cuerpo de titular**. La
  portada puede ser mayor — es la única con Brushwell.
- **La caja taupe va más angosta que el titular** (670 contra 810): dos bandas del
  mismo ancho se leen como bloque; escalonadas, se leen como jerarquía.
- **Todo corte de línea va escrito a mano**, y el texto sigue siendo literal del
  brief: se cambia dónde cae el salto, nunca la palabra.

**⚠️ Es OPT-IN a propósito.** Cambiar el valor por defecto re-flujaba piezas ya
aprobadas (3 de las 4 entregadas de la S1 se movían entre 4,5 % y 5,3 % de sus
píxeles). Así que `PiezaFeedBodegon` sigue trayendo el margen y la columna se pasa
a mano (`columna` / `columnaCaja` / `aireTituloACaja`). **Comprobado:** re-rendidas
las 4 piezas aprobadas en `out/_verif/`, salen **idénticas píxel a píxel** a las
entregadas. `npx tsc --noEmit` limpio.

**La slide 4 volvió al carrusel.** La versión que rechazó el cliente era la única
que no usaba `PiezaFeedBodegon` —por eso no se parecía a ninguna—; ahora comparte
gramática, va **anclada arriba** y sus tres textos son literales del brief. Se
agregó el **velo** que pidió Eli: la transparencia multiplicada de Illustrator,
capa aparte al **10 %**, sobre la foto y **debajo** del logo y del texto.
**No es subir `oscurecer`** — eso el manual lo prohíbe («cuando un texto no se lee,
la solución es la caja taupe»). QA: **4/4 limpias**.

**⚠️ La foto de la slide 4 es INTERINA, no se entrega así.** Eli la pidió
*«una trabajadora sin rostro preparando café, y que se vea el espacio del bar»*.
Hoy lleva el **mesón real de servicio** de Between (`espacios/HDT_56.jpg`, recorte
derecho 4:5 desde el original de 6718 px, gradado →
`fotos-gradadas/bar-servicio.jpg`, con su excepción en `.gitignore`). Se eligió
sobre la barra del bar —más linda pero es una pared de destilados— porque **dice
«servicio»**, que es el mensaje de la slide, y no repite el fondo de la portada.
**Le falta el gesto de la mano.**

**Magnific: registrado pero NO operativo.** Se agregó
`magnific / http / https://mcp.magnific.com` a `mcpServers` del proyecto en
`~/.claude.json` (con respaldo). ⚠️ **El CLI `claude` no existe como binario en
este PC** —se usa la extensión de VS Code—, así que `claude mcp add` no se puede
correr: hay que editar la config a mano. Faltan dos cosas y basta con una:

1. El MCP **no carga hasta reconectar la sesión** (`/mcp` → reconnect, o chat nuevo).
2. La clave de `~/.magnific_key` da **401**. ⛔ **NO es la de Freepik**: la propia
   API responde con la URL buena → `magnific.com/developers/dashboard/api-key`.

El prompt ya está escrito en `scripts/between-slide4-magnific.py`, con las fotos
reales del bar como `--refs` para que no invente un bar de stock, y con la regla
KIMBO explícita (taza blanca total, sin logo).

**⭐ Dos bugs del doctor, y el segundo importaba.**

1. Reportaba **4 fichas «JSON inválido» siendo válidas las 8**: abría el archivo
   sin declarar codificación y en Windows Python lee en **cp1252**, que no tiene
   definidos los bytes `0x81`/`0x8D`/`0x90`. Las marcadas eran justo las que llevan
   `Á`, `Í`, `⭐` o `←`.
2. **Se saltaba EN SILENCIO la verificación de material** —la compuerta que detectó
   las 19 referencias rotas de Revex/Casablanca— porque exigía `~/copylab-venv`, que
   en este PC no existe (los paquetes están **globales**, ver `credentials/LEEME.md`).
   Ahora cae a un Python del sistema con PIL+numpy. **Corrió por primera vez acá:
   295 archivos revisados, 295 válidos, 0 rotos, 0 vacíos.**

También se parchó `between-entrega.py`, que reventaba con `UnicodeEncodeError` al
imprimir el «✓» **después** de haber escrito las piezas: parecía que la entrega
había fallado y en realidad ya estaba hecha.

**Dónde quedó.**

| | |
|---|---|
| Carrusel Cowork r6, las 4 slides | `out/hilton-between-cowork-r6/` |
| Las 3 entregables | `out/entrega-cowork-r6/S1/`, con nombre de portal, 2250 px y 150 ppp |
| Piezas aprobadas re-verificadas | `out/_verif/` — idénticas a la entrega |
| Página de revisión (antes/después con medidas) | `https://claude.ai/code/artifact/9688ec3b-7ebd-4707-8051-f7df8bd8e600` |
| Regla y medición | `clients/hilton/CLAUDE.md § LA COLUMNA` + `src/brand/hilton-between.ts` (`bloque.columna: 810`) |
| Props nuevos | `BetweenSistema.tsx`: `columna`, `columnaCaja`, `aireTituloACaja`, `velo` |
| Herramientas nuevas | `between-medir-bloque.py` (mide la **tinta**, no la caja del layout) · `between-slide4-magnific.py` |
| Segunda `/al-dia` (19:30) | `clients/_estado-sync.json`: **no hay ronda 6** |

**Qué sigue, en orden.**

1. **⛔ Copiar el Cowork r6 a la carpeta de entrega.** `Desktop\S1 BETWEEN` todavía
   tiene las 3 slides **viejas** de las 15:19 — las de la jerarquía mala. Las buenas
   están en `out/entrega-cowork-r6/S1/`. **Esto es lo primero de mañana.**
2. **Destrabar Magnific** y generar la foto de la mano. Después: apuntar
   `FOTO_SERVICIO`, rendir `BW-F-Cowork-4`, QA, y **descomentar `BW-F-Cowork-4` en
   `scripts/between-entrega.py`**.
3. **Subir a Drive.** Sigue faltando `credentials/token.json`, así que **nada de esto
   está en Drive**. Allá las 27 piezas siguen en la versión del **28-08 01:53
   (ronda 4)** y faltan los **5 PNG de feed** (Cowork 1/2/3 y Cumpleaños 1/2) aunque
   la grilla ya marca FEED E como `CORREGIDO`.
4. La ficha `clients/hilton/marca.json` **no existe** (lo marca el doctor; `abakos`
   está igual). Todo lo medido ya está en `src/brand/hilton-between.ts` y en el
   manual: es pasarlo a JSON.

**Abierto.**

1. ⚠️ **La slide 4 lleva foto interina.** No se entrega hasta tener la de la mano.
2. ⚠️ **Duplicados en Drive:** `BW ST 01-09`, `03-09` y `04-09` existen **dos veces**
   en la misma rama (la vieja del 28-08 en `BW` y la nueva en `BW/S1/STS`). El portal
   levanta **por nombre** — hay que limpiar.
3. **¿La slide 4 lleva logo?** Eli dijo «para que se vea el logo y los textos de
   arriba», pero la regla escrita es que **en carrusel el logo va sólo en la
   portada**. Se respetó la regla y quedó sin logo. **Falta que ella confirme.**
4. **`credentials/token.json`** — sin eso no se puede corregir ninguna pieza ya
   entregada en Drive. Mismo bloqueo desde el 31-08.
5. **NO hay ronda 6**: los 9 comentarios nativos de la grilla siguen siendo los del
   31-08 17:34–17:59. El guardado de hoy 19:25 sólo movió estados (FEED E y
   STORIES C y D pasaron a `CORREGIDO`).
6. **Hilton no tiene `reglas.yaml`** (Casablanca, Revex y Cava sí). La regla de la
   columna es medible y debería entrar al motor de QA cuando se abra ese archivo.
7. Sin cambios: el **listado del cumpleaños de CINCO ítems** contra los cuatro de
   nuestra pieza, y el **Café Bombón** esperando al cliente.

---

## 2026-09-01 (tarde) · Eli (Windows) — BETWEEN: la S1 de septiembre corregida entera, y el logo del vaso resuelto de raíz

**Qué se hizo.** Cuatro rondas de correcciones sobre las 7 piezas de la **S1**
(carrusel Cowork 1-sep, post Cumpleaños 3-sep y las dos stories), todas pedidas por
Eli en la sesión. Quedaron **entregadas en `Desktop\S1 BETWEEN`** con el nombre del
portal, 150 ppp verificados. **⛔ NO están en Drive** — sigue faltando el token.

**Lo que se arregló, pieza por pieza:**

| Pieza | Qué se hizo |
|---|---|
| **ST 1-sep** Promo To Go | La **CTA que faltaba**, literal del brief (`STORIES!C10`): «Pasa por Between y llévalo contigo». Pasó a **botón blanco** con la orden dentro y el cierre debajo. Las **medias lunas ya se ven completas** (el render viejo usaba un recorte más apretado de la foto). Confeti corrido: estaba encima del producto |
| **FEED 1-sep** Cowork slide 1 | La caja dejaba **«pendientes.» sola en la segunda línea**. Corte del brief, una frase por línea, interlínea 1,16 |
| **FEED 1-sep** slides 2 y 3 | **Fuera Brushwell**: la línea de acompañamiento pasa a Raleway 500 en caja alta (`scriptSans`). La portada queda como la única con script. En la slide 3 la pregunta estaba partida entre dos pesos y su caja dejaba «reunirte.» viuda |
| **FEED 3-sep** portada | **Fuera el lockup** — la marca ya está en el vaso. Cierra la decisión que estaba abierta desde el 31-08 |
| **ST 3-sep** | Volvió a ser **UNA sola** story con las dos informaciones (titular + listado con emojis). Cabe porque cambió el vaso |
| **Los dos vasos del cumpleaños** | Logo re-estampado de raíz: ver abajo |
| Precios y horas | Cifras `lnum` + `tnum` en las tres cajas |

**⭐⭐ El logo del vaso, la historia completa — porque costó cuatro intentos.**
El reclamo era «se ve sucia el logo» y después «no puedes curvarlo de esa manera».
Las dos cosas tenían una causa distinta y las dos quedaron medidas:

1. **La suciedad era un velo, no el logo.** El re-sellado masivo de la ronda 5
   borró el sello anterior con `--clonar lados`, que interpola cada FILA entre las
   franjas laterales; eso aplana la curvatura del cilindro y deja **un rectángulo
   más claro con los bordes rectos a la vista**. Y el cliente **nunca había
   reclamado por el logo de estas dos piezas** (en FEED E pidió «*incluir*» el
   logo; el «nada que ver» era del carrusel To Go). El arreglo en bloque dañó una
   pieza que estaba bien.
2. **La curvatura venía de la ronda 4.** Al volver a esa versión para rescatar su
   cartón limpio, se restauró el sello viejo con `curvar()`: comba sinusoidal **más
   acortado lateral del 18 %**. Medido: proporción **2,619** y **2,069** contra
   **3,027** real — 13 % y 32 % achatado.

**La salida, y es la lección de la sesión:** un logotipo **no es un bloque, son
líneas de 3–6 px**. Se borran **solo los trazos** con convolución normalizada
—cada píxel se reemplaza por el promedio de sus vecinos conocidos— así el gradiente
del cilindro y el grano del cartón no se inventan, se interpolan a 3 px. Después se
estampa el vector plano. `scripts/between-logo-vaso-plano.py`.

⛔ **Cuatro caminos que NO sirven y no hay que volver a intentar:** re-estampar
borrando un bloque (velo), pegar el recorte del vaso real encima (el vaso de la
escena es más ancho abajo y **asoma por el costado** — el «extraño y doblado»),
rellenar el fondo del vaso viejo (emborrona la estructura vertical), y trasplantar
la banda de cartón real (llega con la línea de base torcida).

**Y tres medidas nuevas que antes se hacían a ojo:**

| | valor |
|---|---|
| logo ÷ ancho visible del vaso, en el vaso oficial | **0,89** → se usa **0,86** (el sello va plano y hay que dejar aire en las puntas) |
| centro | el **eje de la silueta** del cuerpo, no el centro del sello anterior |
| altura | contra **lo que tapa**, no contra el cartón: los dedos suben a y 1236 aunque el cartón llegue a 1300 |

**Dónde quedó.**
- Piezas: `Desktop\S1 BETWEEN` (7 PNG) y `out/entrega-drive/S1/`.
- Assets nuevos versionados: **`logo-negro-vector.png`** (4214×1392, proporción
  3,0273) sacado del editable oficial `Between_logo_oficial.ai` que mandó Eli
  (Drive `1qIIz0OjsoOgRqv0TGFfE4e22xeelpsvE`, **página 1** de 8). El `.ai` es PDF
  1.6 por dentro: se rasteriza con `pypdfium2`, sin Illustrator.
- Scripts nuevos: `between-logo-vaso-plano.py` (borrado de trazos + sello plano +
  `--arco` sutil) y `between-logo-densidad.py`.
- Sistema: `TitularBetween` con `scriptSans`; `PanelTaupe` con `interlinea`;
  `Checklist` con `size`/`gap`; `BotonBlanco` nuevo en `BetweenRecursos`.
- ⛔ `fotos-reales/cumple-vela-real.jpg` **salió de producción** (era el montaje
  del vaso real). El archivo se deja como registro del intento.
- Todo el detalle medido está en `clients/hilton/CLAUDE.md` §§ 6–14.

**Qué sigue, en orden.**
1. **Subir la S1 al Drive.** Falta `credentials/token.json` (traerlo del Mac, ver
   `credentials/LEEME.md`). Después `python scripts\between-subir-drive.py`.
2. **La ilustración de personas del carrusel Cowork.** Eli la pidió con una
   referencia de Pinterest pero **el archivo no está**: no en
   `raw/hilton/between/de-eli` (vacía), ni en Descargas/Escritorio/capturas, ni
   entre las 25 imágenes incrustadas en la grilla. Pinterest bloquea la lectura.
   **Bloqueada hasta que deje el archivo en esa carpeta.**
3. **Slide 2 del Cowork sigue siendo el Winter Garden** y Scarlette pidió «una
   mesa con un pc y un café». La imagen ya está en la carpeta de Eli:
   `raw/hilton/between/ediciones-ia-eli/magnific_agrega-una-laptop-en-la-m_iAi90W63uK.png`.
   No se cambió porque ella acotó el carrusel a los comentarios de textos.
   ⚠️ Y `cowork-laptop.jpg` **no tiene ninguna laptop**: son dos hombres en el muro
   verde. El nombre engaña.
4. Lo que sigue en pie de la ronda 5: regradar bajando calidez y altas, y
   regenerar los montajes rechazados por ambiente (FEED 7-sep, 9-sep slides 2 y 4,
   11-sep, 14-sep slides 1 y 4, ST 9-sep).

**Abierto.**

1. ⚠️ **El listado del cumpleaños que adjuntó el cliente tiene CINCO ítems, no
   cuatro.** Está anclado en `FEED!E13` (`xl/media/image21.png`). Faltan «¡Elige el
   tamaño que quieras!» y «¡Pregúntanos por los cafés disponibles!», y el nuestro
   trae «Presenta tu carnet en la caja» que **no está en el adjunto**. Son dos
   condiciones comerciales sin comunicar. **Hay que resolverlo antes de la próxima
   entrega.**
2. **Del vaso vigente no existe toma frontal aislada en alta resolución.** Lo que
   destrabaría cualquier montaje futuro es una foto: el vaso de frente, superficie
   lisa, luz pareja. Ojo: los packshots frontales 336–339 de la sesión del cliente
   son del **vaso ANTIGUO** (cuerpo negro con faja kraft).
3. **`tnum` no está en los Raleway del proyecto** (sí `lnum`). El avance tabular
   estricto no lo puede dar esta fuente; si alguna vez se necesita una columna de
   precios milimétrica hay que traer la Raleway variable de Google Fonts.
4. **Café Bombón** sigue esperando al cliente (cómo se muestra la leche condensada
   y si va en vaso transparente o kraft).
5. ⚠️ **Hubo DOS sesiones trabajando en este repo hoy.** Los commits `9c0940f` y
   `65d38ae` (13:22 y 13:23) no salieron de esta sesión y uno reescribió la
   bitácora entera. No se perdió nada, pero **conviene trabajar con una sola
   sesión por repo** para no pelear la bitácora.

**Falso positivo conocido.** `between-qa.py` avisa «texto a 22 px del borde
izquierdo» en `BW-S-ToGoDulce`: arma la máscara con píxeles beige de trazo fino y
toma las hojaldres pálidas de las medias lunas por tipografía. Las otras 6 piezas
pasan limpias.

---

## 2026-09-01 · Eli (Windows) — BETWEEN: el conector de Drive NO puede entregar, y quedó probado

**Qué se hizo.** Día de desbloqueo, no de producción. Se cerró la duda que venía
arrastrándose desde el 31-08 sobre por qué no se sube nada al Drive. **No es un
problema de permisos:** Eli le dio permiso de escritura completo al conector de
Drive y no cambió nada. La causa está en el propio conector, verificada en su
esquema:

| Herramienta | Límite real |
|---|---|
| `Crear archivo` | solo acepta el contenido **incrustado en la llamada**, en base64 |
| `Actualizar archivo` | solo cambia **título y carpeta** — nunca el contenido |

Las 3 piezas del cumpleaños pesan 5,5 · 4,4 · 5,2 MB; en base64 son ~7 MB de texto
cada una, del orden de **2 millones de tokens por archivo**. No entran con permisos
ni sin ellos. Y como `Actualizar` no toca el contenido, **por el conector es
imposible reemplazar una pieza conservando su enlace** — que es exactamente lo que
necesitan las 27 piezas de la carpeta BW.

⛔ **Conclusión dura: la entrega a Drive depende de `credentials/token.json` y de
`between-subir-drive.py --actualizar`. No hay atajo por el conector.**

**El desvío que sí sirve hoy.** Las 3 del cumpleaños **no necesitan el token**: la
carpeta S1 (`19Bv7lfMBEIt_4JLRStWKObtCnf4OmPdD`) está vacía, así que son archivos
nuevos y no hay ningún enlace que conservar. Se suben arrastrándolas desde
`out/hilton-between-cumple-r5/entrega S1/` a drive.google.com, con el nombre tal
cual (lo espera el portal). El token solo es imprescindible para corregir piezas
**ya entregadas**.

**Estado del Drive al cierre.** S1 sigue vacía (comprobado). Las 27 piezas del mes
siguen en BW en su versión del 28-08 (ronda 4). Nada nuevo en el Drive después de
las 13:29.

**Dónde quedó.** Se commiteó la cola de la ronda 5 que estaba fuera de git desde el
31-08: las **7 fotos gradadas** nuevas (`segundo-nivel`, `cowork-laptop`,
`winter-garden`, `mesa-cafe-2piso`, `togo-vaso-foto`, `rol-canela`,
`taza-cappuccino-nobg`), sus excepciones en `.gitignore`, los scripts
`between-entrega.py` y `material-a-fotos.py`, y la story nueva `StCumpleDetalles`
registrada en `Root.tsx` y `BetweenEntry.tsx`. `npm run typecheck` limpio.

**Qué sigue.** Rendir el **carrusel Cowork** y la **ST Promo To Go** — el material
local ya está (`cowork-laptop.jpg` y `rol-canela.jpg` se bajaron). Pero no se puede
tocar ninguna de las dos sin resolver antes lo de abajo.

**Abierto.**

1. 🔴 **URGENTE Y NO RESUELTO HOY.** El 1-sep se publicaban el **carrusel Cowork**
   (10:00) y la **ST Promo To Go**, y las dos están *en cambios* por la ronda 5:
   **lo que el cliente tiene en Drive es la versión sin corregir, y el día ya pasó.**
   Hay que decidir con KAM si se corrige y re-sube igual o se deja publicado así.
2. **Siguen sin respuesta las dos preguntas de la regla del lockup** (del 31-08
   tarde), y bloquean `Cumple1`, `ToGo1`, `StToGoDulce` y `StCumple`:
   ¿el carrusel To Go queda sin lockup en las 4 slides, baja a otra slide, o la
   portada es excepción? ¿La regla alcanza a cualquier logotipo legible en la foto,
   solo al vaso, o solo al vaso en primer plano?
3. **Falta `credentials/token.json`** (está en el Mac, en `ASISTENTE PERSONAL/
   credentials/`). Sin él no se corrige nada ya entregado.
4. **Falta `.env`** con `FREEPIK_API_KEY` y `MAGNIFIC_API_KEY`: sin eso no se pueden
   regenerar los 9 montajes rechazados por ambiente.
5. Sin cambios: el **Café Bombón** sigue esperando que el cliente diga cómo se
   muestra la leche condensada y en qué vaso va.

---

## 2026-08-31 (noche) · Eli (Windows) — BETWEEN: el vaso pasó a ser fotografía, y el estudio ya corre en Windows

**Qué se hizo.** El cliente rechazó el vaso otra vez —«el vaso no se parece al
real… se ve quemado y extraño, debe verse hiperrealista»— y al ir a buscarlo a la
sesión del cliente aparecieron **dos vasos distintos**. Eli confirmó que el
vigente es el **B: cuerpo crema con el logotipo impreso directo y tapa negra
plana** (frames 255 · 257 · 264 · 266). El otro —cuerpo negro con faja kraft, el
que ella misma retocó en 245/281/293— es el antiguo. Se recortó el vaso real del
frame **255**, el único donde está entero y sin nada delante, y se montó sobre la
escena aprobada de la story del 3-sep.

**⭐ Y se resolvió por qué un recorte se ve pegado, con números.** No era el
recorte: era cómo estaba puesto. Medido entre recorte y escena:

| | Recorte | Escena | Qué se hizo |
|---|---:|---:|---|
| Nitidez (varianza del laplaciano) | **2095** | 13,5 | desenfoque de 3 px |
| Luz entra por | **derecha** | izquierda | re-iluminado con degradado lateral |
| Sombra de contacto | ninguna | — | elipse suave al lado opuesto de la luz |

⛔ **El vaso no se puede espejar** para arreglar la luz: invertiría el logotipo.
Todo quedó en `scripts/between-montar-vaso.py`, reutilizable.

**La vela se veía rara porque no era una vela:** era un pabilo con llama, sin nada
de cera. Se le dibujó el cuerpo, se subió la llama y se le añadió el resplandor
sobre la tapa.

**Dónde quedó.** Recorte reutilizable en
`public/assets/hilton/between/togo-vaso-real-nobg.png` (1341×1851, sin fondo).
Escena en `public/assets/hilton/between/fotos-reales/cumple-vela-real.jpg`.
`StCumple` apunta ahí. Las 3 piezas del cumpleaños rendidas en
`out/hilton-between-cumple-r5/entrega S1/`, con el nombre del portal.
Comparación visual: <https://claude.ai/code/artifact/71c547d8-0899-42d5-aa90-f9c8408becc1>

**⭐ El estudio ya corre en Windows.** Los scripts eran de Mac y cuatro cosas
fallaban en seco. Todas corregidas y **probadas**, no solo escritas:

1. `_entorno.py` → `python_venv()` caía a la cadena `"python3"`, inexistente acá.
2. `hilton-drive-pull.sh` → llamaba a `/usr/bin/python3` y dejaba un `
` en el
   nombre, que Windows convierte en `_` (`foto.jpg_`). **Usar
   `scripts/drive-carpeta.py`**, que además trae `--miniaturas` para revisar una
   sesión de 353 fotos sin bajar gigas. ⛔ El `.sh` quedó parchado pero el bueno
   es el `.py`.
3. `between-rendir.sh` → ruta de Chrome del Mac y sandbox de iCloud. **Usar
   `scripts/between-rendir.py`**, que fuerza UTF-8 en `subprocess` (con el cp1252
   de Windows la salida de Remotion revienta el hilo lector).
4. ⛔ **`credentials/` NO estaba en `.gitignore`.** Un token ahí se publicaba a
   todo el equipo en el siguiente push. Blindado y verificado con
   `git check-ignore`, junto con `.env` y `client_secret*.json`.

Instalado en la máquina: `google-api-python-client`, `google-auth`,
`google-auth-oauthlib`, `requests`, `python-dotenv`. Instrucciones en
`credentials/LEEME.md`, escrito para Windows, más `scripts/autorizar-google.py`
por si hay client secret pero no token.

**Qué sigue.** Las **dos piezas de feed** con el mismo tratamiento: ahí el vaso va
sujeto entre dos manos, así que hay que devolver los dedos por delante del vaso
real — más delicado que la story. Después, la cola de la ronda 5 que sigue en pie.

**Abierto.**

1. ⚠️ **Mi story choca con la regla 8 de la entrada anterior.** Al cambiar el vaso
   de IA por el real, **el logotipo impreso quedó mucho más legible**, y la pieza
   sigue llevando el lockup arriba. `StCumple` no estaba en las tres que se
   auditaron porque entonces su vaso apenas se leía. Ahora sí aplica: **necesita
   la misma decisión** que `Cumple1`, `ToGo1` y `StToGoDulce`.
2. ✅ **RESUELTO el «¿en agosto?»**: Eli confirmó que va **«¿Estás de cumpleaños en
   septiembre?»**. Ya está aplicado en el feed y en la story. Sale de la lista de
   abiertos de las dos entradas anteriores.
3. **Nada se subió al Drive todavía.** No es permiso —se comprobó subiendo y
   descartando un PNG de prueba en la carpeta S1—: el conector solo acepta el
   archivo incrustado en la llamada y estas piezas pesan 4–6 MB (≈1,5 M de tokens
   cada una). **Falta `credentials/token.json`** y se sube con un comando.
4. Siguen en pie: el Café Bombón esperando al cliente, y las dos preguntas de
   alcance de la regla del lockup.

---

## 2026-08-31 (tarde) · Eli (Windows) — BETWEEN: el vaso ya firma, y septiembre quedó desparejo

**Qué se hizo.** Eli enunció un criterio de la cuenta que nunca estaba escrito:
**cuando la foto trae el vaso con el logotipo impreso, la pieza no sobrepone el
lockup** — se lee dos veces la misma marca y se ve mal. Se auditó toda la grilla
de septiembre contra esa regla y **tres piezas la rompen**: `Cumple1` (FEED 3-sep),
`ToGo1` (FEED 14-sep, portada del carrusel) y `StToGoDulce` (ST 1-sep). Otras
cuatro ya la cumplían. La regla se venía aplicando **a criterio, pieza por pieza**
— `StEmergencia` hasta la trae comentada en el código — y por eso el mes salió
disparejo. Ahora quedó escrita en el manual (§ ⛔ 2), en la gramática como regla 8
y en la lista de QA.

**Dónde quedó.** Comparación visual antes/después publicada en
<https://claude.ai/code/artifact/6d2d656d-b199-421f-b086-79884308c1fc>, con
renders **reales** (`npx remotion still`, no montajes) de `Cumple1` y `ToGo1` con
y sin lockup. `BetweenSeptiembre.tsx` se parcheó solo para rendir y quedó
**restaurado byte a byte** (verificado con `cmp`); `npm run typecheck` limpio.
Los PNG viven en `out/hilton/regla-logo/` (gitignored). **Ninguna pieza se
corrigió todavía y no se subió nada al Drive.**

**Qué sigue.** Sin la respuesta a las dos decisiones de abajo no se tocan las
piezas. Con ellas: corregir las 3, y después retomar la cola que ya venía de la
ronda 5 — bajar el material (`scripts/hilton-drive-pull.sh` sobre GRILLA IA
BETWEEN, `10Wyq-JrVAwkIItMUJH2De6wuxTiBDuDh`), regradar bajando calidez y altas,
regenerar los 9 montajes rechazados por ambiente, rendir, `between-qa.py` y subir
con `between-subir-drive.py --actualizar`.

**Abierto.**

1. **Choca con la regla 5** («en carrusel el logo va SOLO en la portada»): la
   portada del To Go es justo la del vaso con logotipo. ¿El carrusel queda sin
   lockup en las 4 slides, el lockup baja a otra slide, o la portada es excepción?
2. **Alcance de la regla**: ¿cualquier logotipo legible en la foto (letrero del
   local, bolsa, faja), solo el vaso, o solo si además va en primer plano?
3. Sigue en pie lo de la ronda 5: el **«¿Estás de cumpleaños en agosto?»** de
   Scarlette para una pieza de septiembre, y el **Café Bombón** esperando al cliente.

**Notas de máquina.** Este Windows **sí tiene Python** (3.14.7 con PIL, openpyxl y
numpy): los scripts de imagen corren acá. Lo que falta es `requests`/
`googleapiclient`, el token de Google, `raw/` y **22 de las 32 imágenes** — por eso
`StToGoDulce` no se pudo rendir (le falta `rol-canela.jpg`). La memoria decía que
no había entorno de Python y era falso; ya está corregida.

## 2026-08-31 · Eli (Windows) — BETWEEN, ronda 5: el logo del vaso salía deformado

**Dónde quedó.** Llegó la **ronda 5** el mismo 31-08 entre las 17:34 y las 17:59:
**9 comentarios de Scarlette Muñoz**, todos asignados a Eli. Se arregló la causa
del reclamo transversal —el logotipo— y quedó todo el resto documentado y
pendiente de material.

**⚠️ Cómo llegaron los comentarios, que es media lección.** NO están en la fila 15
`COMENTARIOS DISEÑO`: son **comentarios nativos de Excel anclados a celdas**, en
`xl/comments1.xml` (FEED) y `xl/comments2.xml` (STORIES) dentro del propio xlsx.
La fila 15 seguía mostrando los de la ronda 4, la mitad ya tachados. **Leyendo
solo la fila 15, esta ronda entera se pierde.** Traen autor y fecha, que es como
se distingue lo nuevo.

**Lo que se arregló, y era culpa nuestra.** El cliente dijo «el vaso de café tiene
el logo de between **completamente distinto**» y «el vaso de café **nada que ver**
jajajaja». No era el generador: `scripts/between-logo-vaso.py` traía **dos
deformaciones encadenadas**. `resize((ancho, alto))` metía el logo en la caja que
le dieran ignorando su proporción —salió entre **2,59 y 3,02** cuando la real es
**3,0278**, hasta un 15 % achatado— y encima `curvar()` lo arqueaba sobre un
cilindro, con lo que «COFFEE & BAR» quedaba ilegible.

- ✅ Script **reescrito**: escala uniforme (el alto sale de la proporción del
  propio archivo y no hay parámetro para alterarla) e integración **por tono**,
  multiply contra el cartón. `curvar()` se eliminó.
- ✅ Las **5 imágenes con vaso re-estampadas** con el logo real, verificadas a
  escala de pieza: `togo-salida-2`, `togo-cafe-dulce`, `togo-trio-45`,
  `cumple-manos`, `cumple-vela`. Reproducible con
  `python3 scripts/between-relogo-ronda5.py --revisar`.
- ✅ Correcciones de texto en el carrusel To Go: fuera «Café grande» de las
  slides 2 y 3, y la info de promo de la slide 4 unificada con las otras.
  `npm run typecheck` limpio.

**Dos trampas del borrado que costaron dos pasadas**, ya resueltas en el script:
en `cumple-manos` no se puede clonar cartón ni de abajo (hay **dedos**) ni de
arriba (hay **tapa negra**) — hay que usar `--clonar lados`; y el difuminado del
empalme tenía un inset **fijo** de 10 px que en un vaso chico se comía el borde y
dejaba **asomar el logotipo viejo** (pasó en `togo-salida-2`). Ahora va proporcional.

**Las 3 piezas del cumpleaños (3-sep) quedaron RENDIDAS.** Eli confirmó que el
titular va «¿Estás de cumpleaños **en septiembre**?» —Scarlette había escrito «en
agosto»—. Con eso se aplicaron los tres cambios: los textos de la G1, la G2
convertida en **checklist** con emojis (fuera el mockup de Instagram, que metía un
post dentro de un post y encima dependía de una foto que no está acá) y la story
arrastrando el mismo titular. Salidas en `out/hilton-between-cumple-r5/entrega S1/`,
ya con el nombre del portal, en feed 2250×2812 y story 2250×4000.

⭐ **Y se destrabó el render entero.** Faltaban las 8 ilustraciones de
`public/assets/hilton/between/recursos/` (globos, confeti, flechas) y sin ellas no
rinde **ninguna** pieza de Between. Se re-extrajeron del .svg de Eli
(`1EZHJab1Rp8c8vuTHqAehF6tCk-CiRsXa`) rasterizándolo con Chrome headless y
recortando por canal alfa. Pesan 215 KB y **ahora se versionan**, para que no
vuelvan a faltar en la próxima máquina.

**⛔ La entrega al Drive quedó pendiente.** Las 3 piezas NO se subieron a la
carpeta `S1` (`19Bv7lfMBEIt_4JLRStWKObtCnf4OmPdD`): no hay token de Google acá, y
el conector MCP solo acepta el archivo incrustado en la llamada —estos PNG pesan
4–6 MB—. Se resuelve arrastrándolos desde el navegador, o dejando `token.json` en
`credentials/` y corriendo `between-subir-drive.py`.

**⛔ Lo demás que NO se pudo hacer acá, y por qué.** Esta máquina Windows **no tiene 22
de las 32 imágenes** que pide `BetweenSeptiembre.tsx`, ni la carpeta `raw/hilton/`,
ni token de Google. Al repo solo viajan las 10 corregidas en la ronda 4. Por eso:
**no se re-rindió ninguna pieza y no se subió nada al Drive.** Las 27 piezas del
Drive siguen en la versión del 28-08 01:53.

**Lo que falta, en orden.** Todo el detalle con los comentarios verbatim está en
[`feedback/2026-08-31-ronda5.md`](feedback/2026-08-31-ronda5.md).

1. Bajar el material: `scripts/hilton-drive-pull.sh` sobre **GRILLA IA BETWEEN**
   (`10Wyq-JrVAwkIItMUJH2De6wuxTiBDuDh`), que usa el visor público y no pide auth.
2. **Volver a gradar bajando calidez y altas.** Es el segundo reclamo transversal:
   «eliminar el filtro de color cálido» y «se ven quemadas… un filtro medio raro».
3. Regenerar los montajes rechazados por ambiente: FEED 1-sep slides 2 y 3, FEED
   7-sep, FEED 9-sep slides 2 y 4, FEED 11-sep, FEED 14-sep slides 1 y 4, ST 9-sep.
   ⭐ **El 2.º piso del local YA está fotografiado** («tenemos ese material», dice
   ella): se busca en el banco, no se genera.
4. Rendir, `between-qa.py` y subir con `between-subir-drive.py --actualizar` para
   conservar los enlaces.

**Decisiones abiertas.**

- **«¿Estás de cumpleaños en agosto?»** — así lo escribió Scarlette para una pieza
  de **septiembre**. Casi seguro es un lapsus, pero es el titular: hay que
  confirmarlo antes de escribirlo. Y la ST del 3-sep depende de ese mismo texto.
- El **Café Bombón** sigue esperando que el cliente conteste cómo se muestra la
  leche condensada, y nadie ha confirmado si va en vaso transparente o kraft.

## 2026-08-27 · Valeria — BETWEEN, ronda 4 del cliente resuelta

**Dónde quedó.** El cliente escribió comentarios nuevos en la grilla de
septiembre el mismo 27-08 por la tarde, después de que se entregaran las 27
piezas. Se aplicaron todos y **13 piezas están re-subidas al Drive con los mismos
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
