# EBEMA / EBEMA CLICK — bitácora

> Una entrada por jornada, la más nueva arriba. Lo de hoy se escribe hoy: el
> relevo de mañana lee esto antes de abrir cualquier archivo.

## 2026-09-24 — Serena Abarca

**Qué se hizo:** El **PAID de octubre** (brief de Sebastián Córdova, 16 piezas, producido
el 07-09 y nunca subido) se subió a Drive el 23-09. Sebastián dejó **15 comentarios en las
stories**; se aplicaron: la bajada y el botón de las sucursales pasan de 28/24 a **38/34 px**,
y las stories de Click se llevaron a la medición de Paulina (`ebema_click_st1..st4`):
botón de **494×73 en cápsula con filete blanco** y caja roja solo en la última línea. El
`/qa` encontró además el bloque a 330 px del borde, **dentro de la zona segura** (va a 340),
y el texto de la story de Temuco **encima del letrero BIENVENIDOS/SHOWROOM**. Temuco se
rehízo con una foto nueva que mandó Paulina (`IMG_8542`, recorte elegido midiendo 65
opciones). P15 story lleva velo `.46`.

**Dónde quedó:** `out/ebema/20260907_paid_octubre/` ya **está en git**: generador, CSS,
fuentes, logos y fondos. Las 31 piezas están en Drive (`PERFORMANCE/2026/10.Octubre/graficas
octubre 26`) y las 15 stories se reemplazaron sobre el mismo ID, con md5 verificado y los
comentarios conservados. Los fondos pasaron a **JPEG** (92 → 20 MB) para poder versionarlos; las 30 piezas se re-rindieron desde ellos y se volvieron a subir, así que el repo reproduce byte a byte lo publicado. `ENTREGA.md` trae la ronda 2 y el QA; la ronda 1 quedó respaldada
en `_ronda1/` (sin versionar). Las reglas nuevas de story están en el manual §4 y los
errores 10 y 11 en §9. Feed y reel no cambiaron.

**Qué sigue:** responder o resolver los 15 comentarios de Sebastián en Drive, que siguen
**abiertos y sin respuesta**, y avisarle que el feed va en 4:5 y no en el 1:1 de su planilla.

**Abierto:**
- **Paulina tiene que confirmar que la fachada nueva es Temuco:** no se parece a la foto
  anterior. Si la confirma, pasar también el **feed** de Temuco a esa foto, que hoy sigue
  con la del letrero.
- El **grosor del filete** del botón Click no está medido (va 2,5 px). Medirlo en la story
  original de Paulina.
- A Paulina: recorte 4:5 de Coquimbo y Concepción, fachada de Chillán, los 3 packshots del
  carrito y la música del reel.
- La grilla **orgánica** de octubre es de Paulina (ver su entrada del 23-09 abajo): los 6
  carruseles están versionados y en su ronda 1. Este cierre no los tocó.
- ⛔ Sigue sin existir `clients/ebema/reglas.yaml`.
- Esta bitácora no tenía la entrada del 07-09 (producción del PAID de octubre): lo que se
  sabe de ese día está en `ENTREGA.md`.
## 2026-09-24 — Paulina Bustamante

**Qué se hizo:** Tres frentes de la grilla de octubre.
1. **Carruseles, ronda 2** (9 comentarios nuevos): las **6 láminas finales** con el
   producto como **stock en la bodega**, a los costados, y el centro libre para el
   logo («nunca poner el png del producto así, hace que el logo se pierda»). El saco
   de **CBB corregido al CBB Especial verde** (el INACESA estaba mal, salía de una
   ficha vieja). Fotos rehechas: cbb1, pointfix3, sanjuan1 y sanjuan2. Cierre con
   aire parejo (120) arriba y abajo del anillo. Después, **masisa2** con la bajada en
   2 líneas. Paulina: «lo demás está todo perfecto, no lo modifiques de ninguna manera».
2. **Las 4 stories**: Click estática (14/10), Quilicura (21/10), Concepción (28/10)
   y la **animada de Click (07/10)**, 18,6 s a 2160×3840, calcada de la de julio.
   Ronda 1 de las estáticas aplicada (sin caja del sticker, velo abajo, dirección
   en Helvetica sin picos, flecha rehecha).
3. Paulina pega ella misma las imágenes en la grilla de Slides (el token del estudio
   no puede editar la presentación de Carlos).

**Dónde quedó:**
- Carruseles: misma carpeta de Drive y mismos fileId (los comentarios siguen anclados).
  Lote en `out/ebema/20260923_grilla_octubre/`.
- Stories: Drive `4-entregado / 2026-10 grilla octubre — stories`
  (`ebema_st-07.10.mp4`, `ebema_st-14.10.png`, `-21.10`, `-28.10`). Lote en
  `out/ebema/20260924_grilla_octubre_stories/`.
- **Versionado**: fondos nuevos en `public/assets/ebema/grilla-oct26/` (carruseles,
  `stories/`, `story-animada/` con los 4 clips de Kling, los keyframes y los
  prompts), `stories-grilla.css`, `stories_octubre.py`, `story_animada_fotos.py`
  y la composición `EbemaGrillaStoryClickOct`.

**Cambios al sistema:** lámina final = stock (`stock()` en `generar_fotos.py`;
`cierre_compuesto.py` queda retirado), desenfoque del cierre en post (radio 9, la
toma nítida al lado como `_nitida.jpg`), «una sola fotografía continua» en todo
prompt (Nano Banana devolvía collages), `ZONA_ABAJO` con textura, `bajada_ancho`
por lámina en el motor, QA con el botón en 929,3. `magnific-video.py` ya no se
cae en Windows por la codificación de la consola.

**Hallazgo que destraba:** la vista previa de Drive
(`drive.google.com/thumbnail?id=<id>&sz=w4000`) baja **a resolución completa** los
archivos que sube Paulina, y `drive.usercontent.google.com/download?id=<id>&confirm=t`
baja sus videos. Ya no hace falta pedir los packshots por link.

**Qué sigue:** leer la ronda de comentarios de las 4 stories
(`python scripts/drive-comentarios.py --nombre ebema_st-`). Después, los 3
carruseles de LinkedIn cuando lleguen las referencias.

**Abierto:**
1. **Story animada, escena del gift card (s4):** Kling inventó un logo chico en el
   chaleco del ferretero. Casi no se ve, pero hay que decidir si se rehace el clip.
2. La animada va **sin música**. La de julio tenía pista; la grilla no la pide.
3. **Grilla de noviembre** (Carlos, 23-09): «sin desarrollar brief todavía», con
   5 pendientes de Ariel (líneas Codelpa, VH negros o Galvatec, Black Friday, horarios).
4. Siguen abiertos de ayer: el logo de Masisa no es el vectorial y EBEMA no tiene
   `reglas.yaml`.

## 2026-09-23 — Paulina Bustamante

**Qué se hizo:** los **6 carruseles de feed de la grilla de octubre** — Masisa (4
láminas), Etersol, CBB, Volcanita RH, San Juan y Pointfix (5 cada uno), **29 láminas
a 2250×2813**. Familia A, gramática de §4-bis. Los 3 carruseles de **LinkedIn quedaron
fuera a propósito**: el manual sólo tiene medida la gramática del carrusel de feed con
proveedor y el repo no tiene ninguna referencia de LinkedIn contra la cual medir;
armarlos igual era inventar un sistema. Paulina lo decidió así y va a dejar
referencias.

⚠️ **El brief de Masisa cambió después de estar aprobado.** El 15-09 Paulina aprobó
«línea melamina y cantos», 5 láminas con tip pro; la grilla del 22-09 lo reemplazó por
**«Tablero Estructural Masisa»**, 4 láminas y sin tip pro. Manda la grilla (§0-bis).
Se rehicieron textos y fotos; las reglas de composición aprobadas se conservaron
enteras. Paulina entregó las medidas reales del tablero —**122 × 244 cm, 8 mm**— y
entraron al prompt con la razón de la proporción, no sólo la cifra.

**Dónde quedó:** entrega en Drive, `MATERIAL DISEÑO PAULINA / EBEMA / 4-entregado /
2026-10 grilla octubre — carruseles`, una carpeta `c_<tema>/` por carrusel con la
nomenclatura de Paulina (`ebema_c_<tema><n>.png`). Lote en
`out/ebema/20260923_grilla_octubre/` (`BRIEF.md`, `ENTREGA.md`, `PROMPTS.md`,
`editables/`, `entrega/`). **Versionado:** los 29 fondos en
`public/assets/ebema/grilla-oct26/` (JPEG 2400/q92, 39 MB, excepción en `.gitignore`),
el motor en `clients/ebema/sistema-grilla/_motor.py` y los 6 generadores en
`sistema-grilla/ejemplos/octubre-2026/`.

**El sistema quedó mejor de como estaba.** Los dos generadores aprobados el 15-09
tenían cada uno la mitad: Masisa el arco de 5 láminas, el tip pro y la guarda de
`data-tapa`; Etersol el pre-enunciado. Ahora hay **un motor que no se toca** y un
archivo por carrusel con su brief citado. El ancho de caja de las láminas de
desarrollo pasó a ser campo del carrusel (`ancho_caja_des`), que es lo que §4-bis dice
que es: una decisión por carrusel.

**QA hecho:** los 6 pasan `qa_portada.py` sin fallos, con desvíos de 0,02 a 0,52 px
contra §4-bis, y 29 de 29 con una sola caja roja. **Dos fallos que marcó el QA eran
del QA y quedaron corregidos en el sistema:** (1) medía el recuadro de *todo* el rojo
de la cápsula y **el logo de Volcán también lleva rojo**, así que juntaba el anillo
EBEMA con el del proveedor — ahora toma el primer bloque contiguo; (2) contaba 3 cajas
en la portada de Masisa, donde hay una sola caja alta cuyas letras blancas desmarcan
filas — ahora funde los grupos con el mismo tramo horizontal.

**Reproducibilidad probada, no afirmada:** se reconstruyó Etersol desde cero con el
sistema y los fondos versionados, y las 5 láminas salieron **idénticas byte a byte**
con `cmp`.

**Dos trampas nuevas, ya guardadas en memoria:**
1. **Un prompt de imagen jamás nombra el titular.** Decía «el tercio superior queda
   tranquilo: ahí va el titular» y Nano Banana devolvió las fotos con **el 17 % de
   arriba en blanco puro**, reservando el hueco. Se detectó midiendo la desviación
   estándar por fila, no mirando.
2. **`--aspecto feed` de `scripts/magnific.py` era 1:1**, y montado en 1080×1350
   recorta un 20 % del ancho. Se agregó **`--aspecto carrusel` (4:5)**, probado contra
   la API. Úsalo en toda pieza de feed.

---

### Misma jornada, más tarde: RONDA 1 — entregada

Paulina revisó las 29 y dejó **37 comentarios anclados sobre las piezas en Drive**.
Se leen con `python3 scripts/drive-comentarios.py --nombre ebema_c_`. Reglas que dio
explícitas: **sin comentario = está bien y no se toca**, y «te dejé un mismo
lineamiento para corregir todas las slides finales».

**Cuatro comentarios DEROGAN medidas que §4-bis daba por fijas** — están en el manual
como sección fechada dentro de §4-bis, no sólo en las piezas:

| | Antes | Ahora |
|---|---|---|
| Botón «¡Cotiza por whatsapp» | 653,8 fijo | **430,1** — abraza su texto |
| `<Producto>, disponible en Ebema` | 34 px, una línea | **46 px, dos líneas** |
| «en el link de la bio!» | 28 px / 600 | **34 px / 700**, pegado al botón |
| Pre-enunciado | 0,47 (estimado) | **0,62** + interlineado 1,72 |

**La lámina de cierre es otra:** bodega de materiales al fondo, **producto original
al centro**, todo desenfocado. En CBB y San Juan el saco va **componiendo el packshot
oficial** sobre una bodega generada (`cierre_compuesto.py`): la IA hace sólo el fondo
y la etiqueta del proveedor nunca pasa por el modelo. En las otras cuatro el producto
sí se genera — un tablero o un rollo no tienen etiqueta que falsificar.

**Los packshots.** ⚠️ El token del monorepo (`drive.file`) **no puede bajar lo que
sube Paulina**: al pedirlo por URL vuelve el HTML de permisos. San Juan se resolvió
desde cementossanjuan.cl (los nombres de sus archivos calzaban exactos). CBB salió
de la ficha técnica en PDF, extraído con `pymupdf`, escalado con Magnific y recortado
a mano. **Paulina confirmó que el envase que EBEMA distribuye es el INACESA kraft**,
no el verde que muestra cbb.cl — yo lo había descartado por «antiguo» y estaba mal.
Los dos PNG quedaron versionados en `public/assets/ebema/grilla-oct26/_packshots/`.

**Correcciones de texto:** masisa1 (cápsula y pie se intercambian), masisa2 (dos
líneas), cbb4 y sanjuan2 (orden invertido: manda el beneficio, la enumeración baja a
bajada), sanjuan1 (cápsula a 880), pointfix4. **Imágenes rehechas:** etersol1,
etersol4, cbb2, cbb4, sanjuan2, pointfix3, más las seis finales.

**🔴 Error de método, anotado en el manual.** El «cuadro» del tercio superior lo
había visto yo el mismo día, medí luz y detalle contra las 5 referencias, dio dentro
de banda y lo dejé pasar diciendo que mi impresión estaba equivocada. **Medí la
variable equivocada:** las referencias tienen foto real arriba y las nuestras fondo
vacío — mismo brillo, lectura opuesta. Se arregló en las dos mitades: el velo ya no
arranca plano (entra en rampa) y el prompt pide contexto real con textura.

**QA:** los 6 pasan sin fallos con la medida nueva del botón. Se corrigió además el
umbral de detección, que con el botón angosto **hacía caer el script**.

⚠️ **Susto:** escribiendo el manual, un `io.open(p,"w")` reventó al codificar y dejó
`clients/ebema/CLAUDE.md` en **0 bytes**. Se recuperó con `git checkout HEAD --`
porque estaba commiteado esa mañana. Desde ahora se escribe a temporal + `os.replace`.

**Entrega:** las 29 actualizadas en la misma carpeta de Drive, mismos nombres.

**Qué sigue:** los 3 carruseles de LinkedIn cuando lleguen las referencias.

**Abierto:**
1. **El logo de Masisa** sigue siendo el recortado de una pieza publicada, no el
   vectorial del kit.
2. **EBEMA no tiene `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca ebema`
   se niega a correr. El control se hizo con `qa_portada.py` más el checklist de §8.
3. Los briefs rotulan cuatro L4 como **«(Tip pro)»** pero ninguno es una orden de
   oficio. Paulina confirmó dejarlas en registro normal por ahora. Si contenido quiere
   el registro de consejo, el texto tiene que venir escrito como imperativo.

## 2026-09-22 — Paulina Bustamante

**Qué se hizo:** No se produjeron piezas: se **respaldó la cuenta**. Todo el material
de EBEMA vivía sólo en el PC de Paulina (`raw/`, que está en `.gitignore`), así que
un traspaso o una máquina perdida se lo llevaba entero.

**Dónde quedó:** Carpeta nueva en el Drive de Paulina —`MATERIAL DISEÑO PAULINA`,
compartida con la cuenta del conector— con la estructura `1-marca` · `2-referencias`
· `3-fotos` · `4-entregado` · `5-en-revision`, la misma para sus tres marcas.
Subido y **verificado archivo por archivo: 97 de 97**.

- `1-marca/proveedores/` — los **25 logos** ya recortados y con fondo transparente
- `1-marca/originales/` — los **31 originales**, con los PDF vectoriales
- `2-referencias/grilla/` (39) y `/paid/` (10) · `3-fotos/aprobadas/` (17 ferretero)

**Qué sigue:** nada de EBEMA quedó a medias. Cuando se retome la grilla de octubre,
el material ya no depende de este computador.

**Abierto:** la cuenta del conector **no puede mover archivos que sube Paulina** —
Drive responde «el usuario no tiene permiso» aunque sea Editor de la carpeta. Quedan
17 ferreteros un nivel más abajo de lo debido, en
`3-fotos/aprobadas/ferretero-aprobadas/`. Es prolijidad, no bloquea.

## 2026-09-16 — Paulina Bustamante

**Qué se hizo:** Se cerró la **portada de Etersol** y se levantó la gramática de las
**láminas de desarrollo** (L2, L3 y L4) sobre el carrusel de Masisa, con Paulina
corrigiendo en vivo. **Se paró acá a propósito:** la grilla de octubre sigue en
modificaciones antes de pasar a diseño, y seguir desarrollándola ahora es gastar
recursos. La L5 no se tocó.

**Estado de las piezas** (todas prueba, `out/ebema/20260915_grilla_*_prueba/`):

| | Estado |
|---|---|
| Etersol L1 portada | ✅ **aprobada** |
| Masisa L2 | ✅ texto aprobado · imagen resuelta en la 3.ª vuelta de escala |
| Masisa L3 | ✅ **aprobada** — *«me gustó mucho el hacerle zoom, está perfecta»* |
| Masisa L4 | ✅ visada tras dejar el titular en una línea |
| Masisa L5 | ⛔ sin revisar — plantilla dura, sólo le faltaría la foto |

**Las reglas que dictó Paulina hoy** (todas escritas, con su cita y su medición):

1. **El pre-enunciado** va en cuerpo MENOR y no calza en ancho con el gancho — §4-bis.
   Corrigió un error del manual que decía lo contrario.
2. **El pie es la válvula de escape** del enunciado, no un elemento fijo — §4-bis.
3. **Las 5 reglas de imagen** — §5: minimalista · velo sólo en la zona del texto y sin
   cortes · el producto de proveedor **se genera** fiel al real · **el tipo de imagen
   lo dicta lo que dice el texto** (especificación → zoom · uso → escena) · **la escala
   real del producto entra al prompt**.
4. **La gramática de desarrollo** — §4-bis: la línea blanca calza en CUERPO y la caja
   calza en el ANCHO DE CAJA DEL CARRUSEL. Masisa va en **778**.
5. **El tip pro tiene registro propio** — §4-bis: la orden en versales manda (~60 de
   mayúscula contra ~46) y la condición va en la caja roja **en caja baja**.

**Tres errores míos que quedaron documentados** porque explican cómo se contaminan
las reglas entre láminas:

- La caja de la L2 salía en **910,1** de ancho (máximo medido: 802,6): heredaba el
  «calza en ancho» de la portada.
- Al darles ancho de caja, las de desarrollo entraron al paso que hace **crecer la
  caja hacia arriba**, que es de la portada, y se inflaron a 84 y 95 de alto. Ahora
  ese paso exige `data-tapa`.
- El interlineado **0,72 es de versales**; en caja baja dejaba la caja en 62,9. Va 0,873.

**Dónde quedó:** sistema en `clients/ebema/sistema-grilla/`. Los **prompts de las 4
imágenes generadas hoy están escritos** en `ejemplos/masisa_octubre_BRIEF.md` con su
criterio y el historial de las 3 vueltas de escala. `qa_portada.py` ya no está
amarrado al nombre de una pieza y aguanta carruseles a medias.

**Abierto:**
- 🔴 **Falta el ancho real del canto Masisa.** La L4 se compuso con **22 mm supuestos**
  (el estándar para un tablero de 15 mm). Pedido a Paulina, sin respuesta todavía.
- 🟡 **La portada de Masisa sigue con el velo plano** (`rgba(0,0,0,.30)`, `inset:0`).
  Está aprobada de ayer y no se tocó. Falta decidir si se le aplica el velo nuevo.
- 🟡 Las **4 fotos originales del 15-09** se generaron sin anotar sus prompts y **no se
  pueden reproducir**. El `LEEME.md` decía que estaban escritos; ya se corrigió.
- 🟡 Las imágenes generadas viven en `out/`, que está en `.gitignore`. Se pueden
  rehacer desde los prompts, pero **no salen idénticas**.
- ⛔ **EBEMA sigue sin `clients/ebema/reglas.yaml`** — viene de ayer.
- La **grilla de octubre sigue en modificaciones** y no ha llegado a diseño.

## 2026-09-15 — Paulina Bustamante

**Qué se hizo:** Se construyó la **portada de carrusel de GRILLA (familia A)** de punta
a punta, con Paulina corrigiendo en vivo: **11 rondas** sobre Masisa (melamina y cantos)
hasta dejarla aprobada, y después una **portada de Etersol** (pasto sintético) para
probar el sistema con otro brief — quedó bien salvo un par de cosas por corregir.
Ambas de la grilla de **octubre**, que todavía no llega a diseño: los briefs los pasó
Paulina a mano para probar. Llegaron además **los 26 logos oficiales de proveedores** y
el logo EBEMA con transparencia. De paso se corrió `/al-dia`.

**Dónde quedó:** El sistema en `clients/ebema/sistema-grilla/` (CSS consolidado en un
bloque limpio, un valor por cosa con su medición al lado) y los dos generadores con su
criterio comentado en `sistema-grilla/ejemplos/`. Las reglas nuevas, en **§4-bis** del
manual. Los lotes con fotos y PNG están en `out/ebema/20260915_grilla_masisa_prueba/`
y `..._etersol_prueba/` — **no viajan en git**, pero los prompts de Magnific para
rehacer las fotos están en `ejemplos/masisa_octubre_BRIEF.md`. QA de portada
reutilizable en `sistema-grilla/qa_portada.py`. Página de revisión:
claude.ai/artifact/JrLYrLTk3e3VDZiVEUzQDf (Masisa) y
claude.ai/artifact/SFcWA99oEbpLH9XGDP7ccQ (las dos portadas).

**Qué sigue:** Terminar de corregir la portada de **Etersol** — Paulina dijo que aún
quedan cosas. Después, las láminas **2 a 5** de ambos carruseles, que no se han tocado:
las reglas bajo `.portada` en el CSS valen SÓLO para la lámina 1 y hay que decidir, al
revisarlas, cuáles se suben al resto del sistema.

**Abierto:**
- ⛔ **EBEMA no tiene `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca ebema`
  se niega a correr sobre la marca de referencia del estudio. Las cifras de §4-bis ya
  están verificadas por código en `qa_portada.py`: falta llevarlas al motor.
- El logo de **CMPC** vino en SVG y es el único de los 26 que no se pudo convertir solo.
- **Toro, Vinilit y PointFix** venían a 143–348 px de alto y se escalaron a 300: si
  salen pixelados en una pieza, hay que pedirlos más grandes.
- Las fotos se generaron a 1856 px y la entrega es a 2250 (se escalan un 21 %). Si el
  look se aprueba, hay que regenerarlas en 4k.
- La grilla de octubre **sigue sin llegar a diseño**: el documento del mes dice «temas y
  estructura, sin desarrollar brief todavía».

## 2026-09-14 — Paulina Bustamante

**Qué se hizo:** Se produjo la **story 19** de la grilla de septiembre (Ebema Click,
sticker de enlace) como prueba del pipeline — y esa prueba destapó el problema real
del mes: **todo lo que este manual llamaba «el sistema» era el sistema de PAID**.
`sistema/base.css` lo decía en su primera línea desde siempre («EBEMA PAID —
Septiembre 2026») y las referencias que sostenían §4 salen de
`EBEMA/PERFORMANCE/2026/8. Agosto/`. La story se calcó de anuncios y **queda
descartada como entrega**. A partir de ahí, y con las referencias de grilla que dejó
Paulina (5 carruseles, 3 stories, 6 posts, 5 reels), se **midió la gramática de
grilla completa** y se escribió el **sistema de producción que no existía**.

Tres correcciones de Paulina quedaron codificadas el mismo día:
- **Grilla y paid son sistemas distintos**, y no se organizan por el mismo eje:
  grilla por **familia de contenido** (producto en stock · información de servicio ·
  invitación a plataformas) y paid por **submarca**. **SPC no existe en grilla**: son
  ofertas puntuales que pide el cliente, y van a paid.
- **Acá sólo se diseña** (§0-bis): el brief lo arma contenido y trae decidido el
  proveedor, el formato, el pilar, los textos y el ángulo. Una discrepancia **se
  informa, no se resuelve**.
- **Lo que el brief pide generar va por Magnific**: `text-to-image/nano-banana-pro`
  para imagen, `image-to-video/kling-v2-5-pro` para video.

**Dónde quedó:**
- `clients/ebema/CLAUDE.md` — §0 la matriz y cómo se pide una pieza · §0-bis sólo se
  diseña · §4 el esquema Click de paid corregido · **§4-bis la gramática de grilla
  medida** (ancla de marca, las 3 familias, el arco de carrusel, la story y el reel).
- `clients/ebema/sistema-grilla/` — **nuevo**: `base-grilla.css`, `build_carrusel.py`,
  `render.sh` (diseña a 1080, entrega a 2250). Calibrado contra `ebema_c_cedral5`:
  el botón de WhatsApp sale idéntico al píxel y el anillo con menos de 1 px.
- `raw/ebema/1-referencias/` — partido en `grilla/` y `paid/`, y dentro por formato.
- `out/ebema/20260914_st19_click/` — la story descartada, con el aviso en su
  `ENTREGA.md`. **No se subió al Drive.**
- `scripts/_chrome.sh` — los 5 `render.sh` del estudio tenían quemada la ruta de
  Chrome del Mac y no corrían en Windows. Arreglados y probados.

**Qué sigue:** **aparear la grilla de septiembre con sus piezas** — emparejar cada
diapositiva del deck con la pieza que salió, para aprender la traducción brief →
pieza, que es lo que va a hacer falta en octubre. Lo hace Claude solo; Paulina sólo
revisa el apareo y corrige.

**Abierto:**
- 🔴 **Kling 3.0 no está disponible por API.** Sondeado hoy: no aparece en el
  catálogo de nuestra clave ni como fuera de plan; el tope que responde es Kling 2.5
  Pro. Si Paulina genera con Kling 3.0 lo hace en la **web** de Magnific → hay piezas
  que ella puede hacer a mano y que no se reproducen por código. **Decisión pendiente:
  subir el plan de Magnific, o que ella genere los videos y acá se monte.**
- Faltan los **logos de los proveedores** (Cedral, Cintac, Novoplast, Surpol, Toro,
  Polpaico, CMPC, VH) y el **PNG de la flecha** del pie de portada. Sin ellos la
  cápsula de co-marca queda coja. Van en `raw/ebema/3-logos-y-packshots/`.
- Faltan **rondas con corrección** (piezas rechazadas + su versión corregida). Es lo
  que más enseña y lo único que no se puede deducir midiendo.
- **EBEMA sigue sin `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca ebema`
  se niega a correr y el QA se hace a mano. Viene pendiente desde el 01-09.
- Sin generador para las familias **B** y **C** (sus medidas ya están en el CSS) y sin
  pipeline de reel en Remotion.

## 2026-09-02 — Valeria Traverso

**Qué se hizo:** Valeria pidió **otro diseño** para el carrusel de Cedral de la
grilla de septiembre (slide 6 del deck `1wHJf4hxDgait…`). Se produjeron **dos
rutas completas de 5 láminas cada una**, con los textos verbatim del brief:
**Ruta A «Método»** conserva la gramática de Paulina (marco, caja de logo saliendo
del borde, caja roja detrás de la 2ª línea completa y de la mitad de la 1ª, botón
sin sombra) y le suma portada partida antes/después con corte rojo de 12 px, caja
roja del número **espejo exacto de la caja del logo** (152×186, `top:0`, radio
inferior 14), barra de avance de 5 tramos en el lugar de los puntitos, y cierre en
rojo plano con las planchas en panel. **Ruta B «Zócalo»** rompe el centrado: la
foto limpia hasta 970 px y el texto en un zócalo blanco de 380 px alineado a la
izquierda, con el número de paso en Helvetica Bold al 13 % de ancla.
Los 6 fondos se generaron con **Nano Banana Pro** siguiendo las reglas de imagen
de Paulina (plano amplio, ropa de trabajo, obra ordenada, sin marcas legibles).
El par antes/después de la portada se sacó **usando el «después» como referencia**,
para que la casa, el ángulo y el encuadre sean los mismos.

**Dónde quedó:** entrega en `out/ebema/20260902_carrusel_cedral/` (`ENTREGA.md`,
`editables/build.py`, `editables/carrusel.css`, 10 PNG en `feed/`); la capa nueva
también quedó en el sistema, en `clients/ebema/sistema/carrusel.css`, para reusarla
en los otros carruseles de la grilla; los fondos versionados en
`public/assets/ebema/cedral/` (JPEG 93, excepción de `.gitignore`); el generador en
`scripts/ebema-cedral-fondos.py`. Página comparativa publicada para Paulina y
Carlos: `claude.ai/code/artifact/8c6ca8ad-23f7-4a0e-97a7-7214e52b32a6`.
**QA hecho:** las 10 piezas a 1080×1350 y rojo `#EC1C23` exacto verificado píxel a
píxel — el primer cierre iba en duotono rojo sobre la foto y daba **91 tonos de
rojo**, así que se rehízo en rojo plano con la foto en panel.

**Qué sigue:** que Valeria y Paulina elijan ruta. Elegida una, subir las 5 láminas
a `PERFORMANCE/2026/9. Septiembre/graficas septiembre 26/` con la nomenclatura del
portal, y extender la ruta al resto de los carruseles de septiembre (Novoplast,
Toro, Metalcon, Surpol), que tienen la misma estructura de 5 láminas.

**Abierto:**
1. **⛔ Falta el logo de Cedral** — no está en el kit oficial ni en el banco. Acá
   va como kicker tipográfico. Hay que pedírselo a Paulina o al proveedor y armar
   el lockup EBEMA + CEDRAL.
2. **Las fotos son IA.** Si Pizarreño/Romeral tiene material propio de Cedral,
   ese manda y hay que rehacer los fondos.
3. **El `18` del titular en Helvetica Bold.** La regla dice que *toda* cifra va en
   Helvetica Bold y acá se aplicó también dentro del titular; en la pieza que está
   hoy en la grilla se ve en Raleway. Lo decide Paulina.
4. Los kickers `01 · INSTALACIÓN` / `02 · DURABILIDAD` / `03 · TERMINACIÓN` son
   míos, no del brief. Si el cliente los quiere fuera, se borran sin tocar nada más.

## 2026-09-01 — Serena Abarca

**Qué se hizo:** Paulina pidió por Slack generar las 12 campañas ARIEL de WhatsApp
de septiembre desde una pieza madre suya (`ebema_wtsp_piazza.png`, 2500×4510,
armada con la info de A1), cambiando enunciado ferretero/contratista, precios y
dirección. Se produjeron **6 de 12**: el bloque completo de **LÍNEA PORTEZUELO
(A1–A6)**, por parcheo sobre el píxel de la diseñadora — 0 píxeles modificados
fuera de las zonas de precio, enunciado y dirección. Las tipografías se
identificaron midiendo, no suponiendo: enunciado Raleway SemiBold, dirección
Raleway en peso 450 (que no existe como archivo estático, hubo que traer la
Raleway variable de Google Fonts).

**Dónde quedó:** entrega en `out/ebema/20260901_wsp_A1-A12_piazza/` (`BRIEF.md`
con el brief verbatim del Sheet, `ENTREGA.md` con el QA, `madre/`, `piezas/`,
`qa/`); generador en `scripts/ebema-wsp-piazza-variantes.py`; Raleway variable en
`clients/ebema/sistema/fonts/`. Copia para revisión en el Escritorio de Serena
(`EBEMA Click - WhatsApp Septiembre 2026/`) con `LEEME.txt` y hoja de contacto.
Las 6 piezas de Portezuelo están **rendidas y revisadas**; no hay nada a medias.

**Qué sigue:** cuando Paulina mande **la pieza madre de LÍNEA AZTECA Y CALYX**,
medir su geometría con el mismo método y extender el generador con el bloque
A7–A12 (envío 04/09). La receta de parcheo ya está resuelta, es rápido.

**Abierto:**
- **A7–A12 no son variantes de la madre de Portezuelo** — otro título, otros
  packshots y 3 productos en vez de 4. Esperan su propia madre. Diseñarlas por
  cuenta propia es el error nº1 de §9 de este manual.
- La planilla marca la **Llave Individual Azteca (529779)** como «PRECIO
  PENDIENTE, no incluir hasta recibirlo» → se le pide a Ariel antes del 04/09.
- El brief pide **añadir el logo Piazza** en el bloque Azteca y Calyx.
- **EBEMA no tiene `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca
  ebema` se niega a correr y el QA de hoy se hizo a mano contra el checklist de
  §8. Queda por escribirlas y firmarlas con Paulina.
