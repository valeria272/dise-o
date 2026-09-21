/**
 * ⭐⭐⭐ RONDA 33 (21-09-2026) — EL CUADRO DE VIDRIO DE LA DEL 30-09
 * ═══════════════════════════════════════════════════════════════════════════
 * Eli, revisando la pieza entregada: «no se parece a la ref […] ese recuadro
 * que parece transparente de vidrio. El plato está bien y la mayoría, solo el
 * ajuste del recuadro.»
 *
 * Tenía razón y el defecto era de método: la referencia de la columna U
 * (`raw/hilton/between/refs-s5/st2-ref-s5.jpg`) compone TODO el texto DENTRO
 * de una tarjeta de vidrio, y la pieza lo dejaba suelto sobre la foto. La
 * tarjeta no es decoración: es el contenedor, y es lo único que la ref tiene
 * y nosotros no.
 *
 * ── LA REFERENCIA, MEDIDA (no estimada) ───────────────────────────────────
 * Sobre el JPEG de 736×981, la tarjeta ocupa **x 187→547 · y 363→616**, o sea
 * 360×253 y CENTRADA (su eje cae en 367,0 contra 368,0 del lienzo).
 *
 * | qué | medido en la ref | ⇒ acá, @1080 |
 * |---|---|---|
 * | relleno | **blanco α 0,21** | idem |
 * | filete | 1 px más claro que el relleno (Δ L +10 a +29) | 1,5 px blanco α 0,55 |
 * | radio | 33 px = **9,2 % del ancho** | 84 |
 * | padding lateral | 33 px = **9,2 % del ancho** | 84 |
 * | padding superior | 33 px = 9,2 % | 84 |
 * | padding inferior | 27 px = 7,5 % | 62 (ver `VIDRIO.padBottom`) |
 * | sombra | **NINGUNA** | ninguna |
 *
 * ⭐ **El α salió por canal y los tres dieron lo mismo**, que es lo que
 * confirma que el velo es BLANCO y no un color: fuera RGB (167, 150, 133) y
 * dentro (186, 172, 158) ⇒ α = 0,216 · 0,210 · 0,205. Un velo de marca habría
 * dado tres números distintos.
 *
 * ⭐ **Y lleva el fondo DIFUMINADO**, que es la regla que Eli ya había dictado
 * en DT («faltó el detalle de la referencia de ese cuadro, mira difuminado
 * dentro del cuadro el fondo»). Medido cruzando el borde inferior —el único
 * donde hay textura real a los dos lados, la ensalada— y **descontando el
 * velo**, que por sí solo ya baja el laplaciano al 62 %: dentro la nitidez cae
 * al **0,7–38 % (mediana ≈ 10 %)** de la de afuera. Es el mismo rango que se
 * midió en el pin de DT (4–29 %), así que se adopta su mismo radio: **3,5 px**
 * sobre el lienzo de 1080.
 *   ⛔ El error a no repetir: medir el desenfoque SIN descontar el velo. Un
 *   velo de α 0,21 atenúa la amplitud a 0,79 y la energía a 0,62 sin desenfocar
 *   nada — se lee como «hay blur» donde no lo hay.
 *   ⛔ Y el otro: la primera pasada puso la ventana de «dentro» encima de la
 *   fila de íconos. Son tinta blanca nítida y subían la energía de adentro, o
 *   sea daban MENOS desenfoque del real.
 *
 * ── LO QUE NO SE PUEDE COPIAR, Y POR QUÉ ──────────────────────────────────
 * La ref es 3:4 y su tarjeta ocupa el 48,9 % del ancho. Acá el lienzo es 9:16
 * y el titular de Between es grande: «SE QUEDÓ EN CASA?» mide **788 px de
 * tinta**. Una tarjeta con la generosidad de la ref (texto = 69 % del cuadro)
 * pediría 1142 px de ancho y el lienzo tiene 1080.
 *
 * ✅ Lo que SÍ se transpone es la PROPORCIÓN del padding, y calza exacto:
 * 9,2 % de 912 = **84**, que además es `BETWEEN.bloque.margenX`. O sea que la
 * tarjeta toma la caja de márgenes del manual (912 = 1080 − 2×84) y su aire
 * interior es el mismo margen. No hubo que inventar un número.
 *
 * ⚠️ **COSTO, declarado:** la medida interior queda en 741 y el titular, que
 * venía en 788 px de tinta, tiene que achicarse. En la ronda 33 el padding tuvo
 * que bajar a 72 para que cupiera el sticker; **en la 34 volvió a 84 porque el
 * titular pasó a caja baja y el bloque se acortó** (ver abajo).
 *
 * ── DÓNDE SE PARA ─────────────────────────────────────────────────────────
 * La tinta del lockup cierra en y=364. El panel arranca en **y=399** (35 px de
 * aire) y su primera tinta cae en 485. El `logoATexto` de 77 lo absorbe ahora el
 * padding del panel: el aire ya no es logo→texto sino logo→CUADRO, y dentro
 * manda el cuadro.
 */

/**
 * ⭐⭐⭐ RONDA 34 (21-09-2026) — EL TITULAR SALE DE LA FÓRMULA, Y EL CUADRO SE
 * ACERCA MÁS A LA REFERENCIA
 * ═══════════════════════════════════════════════════════════════════════════
 * Eli, sobre la ronda 33: «que este texto sea en solo la primera mayúscula, la
 * demás no, y en raleway pero no tan gruesa. **ya que hay muchos similares en
 * historias**. más similar el recuadro a la ref. con eso vamos mucho mejor.»
 *
 * Tres cosas, y las tres están documentadas donde se aplican:
 *   1. el titular en CAJA BAJA → `cajaAlta={false}` de `TitularBetween`
 *   2. el titular en SemiBold → `pesoCaps`, con la medición en `StS5Plateada`
 *   3. el cuadro con el aire de la ref → `VIDRIO.padX` vuelve de 72 a **84**
 *
 * ⭐ Y lo tercero sólo se pudo hacer gracias a lo primero: con el titular en caja
 * alta ExtraBold el cuadro medía 637 y el aire de la ref no cabía. **Un cambio
 * tipográfico soltó espacio de diagramación** — por eso se rehacen juntos y no
 * uno por vuelta.
 */

/**
 * ⛔⛔ RONDA 29 (14-09-2026) — LA DEL 28-09 SE GENERA, NO SE COMPONE
 * ═══════════════════════════════════════════════════════════════════════════
 * El fondo `st-28-09-togo.jpg` ya NO es un montaje. Las rondas 27 y 28
 * recortaron el vaso de `IMG_4150` y le corrigieron por código el contorno, el
 * campo de luz, la textura, la sombra y la luz envolvente — incluso con un
 * trasplante de luz de Magnific. Tres rechazos seguidos de Eli: «se ve
 * pegoteado», «parece que tuviera luz de flash», «no aprobado».
 *
 * La respuesta estaba escrita desde el 07-09 en `clients/hilton/PROMPTS-DE-ELI.md`,
 * en su primera línea: **«No se compone: se GENERA.»** Y su regla: cuando algo
 * falla varias veces con materiales distintos, lo que se cambia no es el
 * material ni la posición, es el MÉTODO.
 *
 * Ahora la escena nace unida —vaso, persona, manos, sombra y fondo— con Nano
 * Banana Pro y las fotos de la sesión del 09-09 como referencia, que es de
 * donde llega el logotipo impreso con su Ǝ invertida.
 *   · generación: `scripts/between-st-s5-togo-generar.py`
 *   · acabado de color: `scripts/between-st-s5-togo-acabado.py`
 *   · el montaje descartado queda en `scripts/between-s5-vaso-gigante.py`
 *
 * ⭐ El titular bajó de y=300 a **y=262**: en la escena generada el vaso empieza
 * más arriba y en 300 el bloque chocaba con el brillo de la tapa.
 */

/**
 * BETWEEN — S5 · LAS DOS STORIES DE LA SEMANA 5 (28 y 30 de septiembre)
 *
 * Las dos últimas columnas de la hoja STORIES de la grilla
 * (`1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY`, leída EN VIVO por CSV el 11-09-2026,
 * `gid=1367300884` — el `.xlsx` está congelado, ver el manual):
 *
 *   col T · 28-09 · OK PARA DISEÑAR · «ST ESTÁTICA – HUMOR | CAFÉ TO GO»
 *   col U · 30-09 · OK PARA DISEÑAR · «ST ESTÁTICA – ANIMADA | PLATEADA AL CARMENERE»
 *
 * Encargo de Eli, 11-09-2026: «una es estática y otra es animada "video" […]
 * no deben durar más de 15 segundos […] puede ser mínimo de 8 a 9 segundos […]
 * recuerdes las reglas de los vasos TOGO, que se vea realista».
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⛔ ESTAS DOS PIEZAS YA EXISTÍAN, Y POR ESO SE REHICIERON
 * ══════════════════════════════════════════════════════════════════════════
 * El lote de 27 del 27-08 las incluía (`StHumorToGo` y `StPlateada` de
 * `BetweenSeptiembre.tsx`), y quedaron en Drive. Nunca pasaron por ninguna de
 * las 13 rondas posteriores, así que arrastran los defectos que el cliente ya
 * corrigió en las demás:
 *
 * | | v0 del 27-08 | acá |
 * |---|---|---|
 * | vaso To Go | kraft **SIN logotipo** — el reclamo que el cliente hizo TRES veces | logotipo real estampado |
 * | lugar | muro de estuco crema con teja y platanera: **no es Between** | el patio real (pizarra + teca + jardín vertical) |
 * | plateada | carne en **cubos**, inventada | la **foto real de Between**: plato blanco, puré a la ciboulette, rábano |
 * | col U | PNG estático | **video de 9 s**, que es lo que pide la grilla |
 * | contraste del beige | 1,4–1,9:1 (ilegible, sostenido por cajas) | 8,1–16,0:1 medido por tercios |
 *
 * Las dos escenas se PRODUJERON con el método de Eli
 * (`clients/hilton/PROMPTS-DE-ELI.md`) en un espacio de Magnific abierto para
 * la semana, con Nano Banana Pro 9:16 · 4K y las fotos reales como referencia.
 * Los prompts, vuelta por vuelta, están en `scripts/between-st-s5-generar.md`.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐⭐ RONDA 2 (11-09, tarde) — ELI MANDÓ DOS SESIONES Y LAS DOS PIEZAS CAMBIARON
 * ══════════════════════════════════════════════════════════════════════════
 * > «en esta carpeta puedes encontrar platos de Between […] creo que acá puedes
 * > encontrar referente del plato o el mismo plato. Para la historia del vaso
 * > togo estática el vaso se ve muy falso y mal el logo. Hazlo más realista y
 * > acerca más a la chica y el vaso, para que el fondo pase a 2do plano.»
 *
 * **30-09 · el plato ESTABA, y era muy distinto del que se había usado.**
 * `Between-131` a `143` de la sesión de platos (carpeta `18SrYXjLYVv…`): plato
 * **BLANCO** redondo, trozos de carne braseada en salsa de vino, puré
 * espolvoreado con **ciboulette**, hojas verdes y dos rodajas de **rábano**. El
 * de QB que se había usado de referencia iba en loza de borde turquesa y con
 * champiñones — nada que ver. Se le pidió al generador cambiar **sólo el
 * plato** y dejar idéntico el resto de la escena, que ya estaba aprobada.
 * ⭐ Y como el plato ocupa el mismo sitio, **la diagramación no se movió**: la
 * banda limpia sigue llegando a y=1058 y el contraste quedó en 12,3–15,8:1.
 *
 * **28-09 · el vaso se veía falso porque el cartón estaba mal.** El generado
 * era kraft anaranjado y liso. El real —`Double Tree 25 jul 25-248.jpg`,
 * recortado de cerca— es **crema pálido con la fibra y las motas a la vista**,
 * borde superior enrollado, **costura vertical**, **anillo blanco** en la base y
 * tapa negra de domo con **nervaduras concéntricas**. Esa lista va en el prompt
 * uno por uno: pedir «cartón kraft» no alcanza, hay que nombrar las piezas.
 *
 * ⭐ **Acercar la cámara le quita sitio al titular, y hay que devolvérselo.**
 * Con el plano cerrado que pidió Eli, la banda limpia se desplomó a **y=443**
 * (el vaso entraba por arriba) y el bloque de texto no cabía. Se resolvió con
 * una vuelta más pidiendo la **cámara apuntando más arriba**: el vaso baja, la
 * tapa queda a media altura y la banda limpia vuelve a **y=960**. El vaso sigue
 * igual de cerca; lo que se movió es el encuadre, no la distancia.
 *
 * ⭐ **El logotipo pasó de 133 a 274 px de ancho** sobre el lienzo de 1080,
 * porque el vaso ocupa el doble. Va **entre la tapa y el brazo** y eso es
 * medido, no estético: a media altura del vaso —donde está en la foto real— lo
 * cruza el brazo, y más abajo cae dentro de la zona segura inferior, donde
 * Instagram pone su barra. La franja limpia entre la tapa y la mano es el único
 * sitio donde se ve entero y nada lo tapa.
 *
 * ⛔ **Los frames 336 · 337 · 338 · 339 de esa sesión siguen vetados.** Son
 * packshots frontales del vaso sobre fondo blanco y parecen la solución, pero
 * son del **vaso ANTIGUO** (cuerpo oscuro con faja de papel). Confirmado otra
 * vez mirándolos.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * DE DÓNDE SALE CADA IMAGEN, Y QUÉ ES REAL EN CADA UNA
 * ══════════════════════════════════════════════════════════════════════════
 * · **28-09 · el VASO es el real, y el logotipo es el archivo oficial.**
 *   Referencias: `togo-vaso-real-nobg.png` (el recorte del vaso vigente) y
 *   `Double Tree 25 jul 25-257.jpg`. El escenario es el patio real de Between
 *   (`espacios/HDT_49.jpg`): muro de pizarra, mesas y sillas de listones de
 *   teca, jardín vertical.
 *   ⭐ **El generador devolvió el vaso LISO, a propósito**, y el logotipo se
 *   estampó después con `scripts/between-s5-logo-vaso.py`. Es la regla del
 *   manual: «se pide el vaso sin marca y se estampa el real». En las dos
 *   primeras vueltas Nano Banana escribió un «BETWEEN» inventado en una sans
 *   cualquiera, sin la Ǝ invertida — exactamente el defecto de la ronda 4.
 *   El logotipo va **rotado 5° y envuelto al cilindro** (ronda 3): rotación
 *   RÍGIDA más proyección cilíndrica medida, proporción 3,0278 intacta.
 *   ⚠️ **La chica no muestra la cara**: el vaso se la tapa. Es lo que hace la
 *   referencia que eligió contenido y de paso deja la pieza fuera del problema
 *   de los rostros.
 *
 * · ✅ **30-09 · el PLATO es el de Between** (ronda 2). Referencias:
 *   `Between-135` (vertical, el plato entero sobre mesa de madera) y
 *   `Between-141` (primer plano del producto), de la sesión de platos que mandó
 *   Eli. ⛔ La ronda 1 usaba `Quotidien-176.jpg res al carmenere`, de la sesión
 *   de **QB**, y estaba mal: ese plato va en loza de borde turquesa y con
 *   champiñones. El de Between es plato BLANCO, con puré a la ciboulette,
 *   hojas verdes y rábano.
 *   ⚠️ **La lección de método:** se dio por inexistente una foto que sí
 *   existía. Se había buscado en `platos-ene` (31 archivos en disco) y no en
 *   las **202 miniaturas** de la misma carpeta, que son la sesión completa.
 *   Antes de decir «no hay foto», mirar la sesión ENTERA en hoja de contacto.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐ RONDA 3 (11-09, tarde) — LA ANIMADA APROBADA, Y EL DETALLE DEL VASO
 * ══════════════════════════════════════════════════════════════════════════
 * > «La historia número dos animada queda aprobada. La número uno tiene un leve
 * > problema en el vaso. Tienes que borrar esa línea que se ve y que el logo se
 * > vea más centrado al vaso, como un mockup. El logo debe verse realista que
 * > está en el vaso, como los originales. El tamaño está ideal del vaso y
 * > también está bien las tipografías y la persona.»
 *
 * **La del 30-09 quedó APROBADA** y no se tocó.
 *
 * ⛔ **La línea la pedí yo.** El prompt de la ronda 2 traía «una costura
 * vertical del cartón» dentro de la lista de detalles físicos que arreglaron el
 * realismo, y el generador la puso **justo al medio de la cara visible**,
 * partiendo el logotipo en «BETW | EEN». En el vaso real esa costura existe pero
 * cae al costado.
 * ⭐⭐ **Regla: a un generador, los detalles DIRECCIONALES hay que ubicarlos.**
 * «Costura», «etiqueta», «asa», «pliegue» — sin un «al costado, fuera de la cara
 * principal» van a parar donde más estorban.
 * Se borra con `scripts/between-s5-vaso-costura.py`, que reconstruye la franja
 * fila a fila interpolando el cartón de sus dos costados y le devuelve el grano.
 * Medido: la caída de luminancia en esa columna pasó de **−13,2 a −2,8**.
 *
 * ⭐⭐ **«Se ve descentrado» no era el logotipo, era la línea.** Estaba en
 * x=1800 y el eje real del vaso está en **x≈1750**: 50 px sobre 1900 de ancho,
 * un 2,6 %. Lo que se leía corrido era el conjunto *logotipo + línea*, porque la
 * costura dejaba un paño ancho a la izquierda y uno angosto a la derecha.
 *
 * ⚠️ **Y el eje de un objeto ocluido se mide donde NO está ocluido.** El borde
 * izquierdo del vaso lo tapa el brazo, así que un detector de cartón sobre esa
 * fila toma el fondo oscuro por vaso y devuelve un centro corrido 200 px — se
 * llegó a estampar sobre ese valor falso. El eje bueno lo da **la tapa**, que es
 * lo único que se ve entero.
 *
 * ⭐ **La envoltura cilíndrica** (`--radio` de `between-s5-logo-vaso.py`): el
 * logotipo se trata como impreso sobre la superficie, así que su ancho es un
 * ARCO y lo que se ve es la CUERDA. **No contradice la regla del 31-08**: el
 * radio se MIDE del propio vaso (948 px), la línea de base queda RECTA y la
 * compresión es del 8 % en el borde y progresiva — contra la sinusoide inventada
 * con 18 % fijo que dejaba «COFFEE & BAR» irreconocible.
 * Parámetros finales: `--centro 1755 3870 --ancho 780 --angulo -5 --radio 948`.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐⭐⭐ RONDA 26 (14-09) — EL VASO DEJA DE SER CARTÓN GENERADO
 * ══════════════════════════════════════════════════════════════════════════
 * > Eli: «debemos mejorar el vaso y trata de utilizar una foto como la sesión
 * > nueva de vasos ToGo».
 *
 * Puesto el vaso de la pieza al lado del de la sesión del 09-09 y normalizados
 * al mismo ancho, el generado se delataba en tres cosas MEDIBLES:
 *
 * | | pieza (r3) | vaso real 09-09 | pieza (r26) |
 * |---|---|---|---|
 * | saturación del cartón | 0,21 | 0,46–0,64 | **0,39** |
 * | motas de pulpa | sí, de 5 a 15 px | ninguna | **ninguna** |
 * | logotipo / ancho del vaso | 0,42 | **0,91** | A 0,76 · B 0,88 |
 * | alto del bloque / ancho | 0,140 | 0,377 | A 0,294 · B 0,386 |
 *
 * ⛔ **No se regeneró nada.** `scripts/between-s5-vaso-real.py` le cambia la
 * SUPERFICIE al vaso ya aprobado, partiendo de la misma base limpia de la r4:
 * el campo de luz sale del propio vaso (mediana de 21 px, que borra las motas y
 * deja el pliegue y la sombra de contacto de los dedos), la fibra sale del
 * packshot real y el tono es el kraft medido bajo el iluminante de ESTA escena.
 * La silueta, el tamaño, la inclinación, la tapa, las manos y la chica quedan
 * intactos — es lo que Eli cerró en la ronda 3.
 *
 * ⭐⭐ **El logotipo medía menos de la mitad de lo que mide en el vaso real**, y
 * por eso se leía como calcomanía y no como serigrafía. La proporción sale de
 * medir la altura de las letras contra el diámetro en la foto y de la
 * proporción del archivo oficial (3,0278:1): el bloque abarca **131° del
 * cilindro**, o sea 0,91 del ancho aparente visto de frente.
 *
 * ⚠️ **Pero a su proporción real no cabe acá**, y la razón está medida: el
 * logotipo va a 0,82 del alto del cuerpo, y a esa altura el brazo ya cruza el
 * vaso. En las fotos de la sesión la mano tapa parte del logotipo y se ve
 * natural; en una historia donde el vaso ES la marca, «COFFEE & BAR» a medias
 * no. Por eso hay dos versiones y la decisión es de Eli:
 *   · **A** — `--centro 1704 3798 --ancho 1600 --radio 897` → 0,76 del ancho.
 *     Lo más grande que cabe ENTERO entre la tapa y el brazo: 2 px de holgura
 *     con la sombra de la tapa y 22 px de tinta rozando la piel.
 *   · **B** — `--centro 1697 3860 --ancho 2025 --radio 887` → 0,88 del ancho.
 *     La proporción del vaso real; la mano le come 5 149 px de tinta.
 *
 * ⛔⛔ **Y había un tope mal puesto en `between-s5-logo-vaso.py`.** La envoltura
 * cilíndrica se rendía si `W/2 >= radio`, o sea a **1 radián (57,3°)** de medio
 * arco, cuando el tope real es **90°** (el logotipo dando media vuelta al vaso).
 * Con el logotipo a su proporción —131° de arco— el guardia devolvía el
 * logotipo SIN ENVOLVER y se estampaba plano y más ancho que el vaso. Corregido.
 *
 * ⚠️ **Lo que sigue distinto del vaso real: la TAPA.** La de la pieza es mate y
 * de plástico modelado; la de la sesión es brillante, con un reflejo vivo en el
 * reborde enrollado. Cambiarla es rehacer geometría, no retocar superficie.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LO INTERACTIVO: ZONA RESERVADA, NUNCA DIBUJADA
 * ══════════════════════════════════════════════════════════════════════════
 * Cuarta vez que Eli lo dice (07-09, 08-09, 09-09 y sigue vigente): el sticker
 * lo pone el CM al publicar, con el sticker REAL de Instagram. La pieza deja la
 * zona limpia y se entrega además una copia `GUIA CM` que NO se sube al Drive.
 *
 *   28-09 → la grilla **no pide interacción** en esta columna. No hay zona.
 *   30-09 → `INTERACCIÓN: LINK CARTA` → **340 × 120 en y=1007**, CENTRADA. La
 *           medida sale del ÚLTIMO frame, no del primero: con el acercamiento
 *           el plato sube y el corredor libre se encoge. ⭐ RONDA 33: el cuadro
 *           de vidrio ocupa el sitio donde estaba la zona, así que baja y se
 *           acorta — el borde del plato en el último frame está en y=1127
 *           (medido), y el sticker conserva sus 10 px de aire con él.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL LOGOTIPO DE MARCA: EN UNA SÍ Y EN LA OTRA NO
 * ══════════════════════════════════════════════════════════════════════════
 * · **28-09 va SIN lockup.** El vaso gigante trae el logotipo impreso y ocupa
 *   media pieza: repetirlo arriba lo dice dos veces. Es la regla 8 de la
 *   gramática y la orden textual de Eli en la ronda 9 («borra el logo
 *   principal ya que está en el vaso TO GO»). Al no haber lockup, el bloque
 *   sube de y=441 a **y=300**, igual que las dos del cumpleaños.
 * · **30-09 va CON lockup arriba.** El plato no firma nada.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REJILLA (1080×1920, se entrega a 2250×4000 · el video a 1080×1920)
 * ══════════════════════════════════════════════════════════════════════════
 *    250 ─ zona segura superior de Meta
 *    271 ─ wordmark del lockup (sólo la del 30-09)
 *    300 ─ primera línea de tinta de la del 28-09 (sin lockup)
 *    441 ─ primera línea de tinta de la del 30-09 (`BETWEEN.bloque.yStory`)
 *   1580 ─ empieza la zona segura inferior
 *
 * Las bandas limpias salen de medir el contraste del beige `#FFF9EB` fila a
 * fila sobre la columna de 810, con el percentil 90 de luminancia (el peor
 * caso), no con el promedio:
 *
 * | | banda limpia | contraste en la banda |
 * |---|---|---|
 * | 28-09 | y=240 a **879** | 8,1 – 14,8:1 |
 * | 30-09 | y=240 a **1058** | 10,6 – 16,0:1 |
 *
 * Por eso las dos van con `oscurecer` 0: la escena ya nace con el hueco
 * oscuro adentro y un multiply encima sólo apagaría el vaso o el plato, que es
 * lo que la pieza está mostrando.
 */
import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  OffthreadVideo,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
import {
  Bajada,
  CajaDato,
  FotoFondo,
  LogoBetween,
  TitularBetween,
} from './BetweenSistema';

const F = 'assets/hilton/between/s5/';

/* ══════════════════════════════════════════════════════════════════════════
   LA ZONA RESERVADA — mismo aparato que `BetweenStS3.tsx` y `BetweenStS4.tsx`.
   Sólo se pinta en la copia `GUIA CM`.
   ══════════════════════════════════════════════════════════════════════════ */
type Zona = {ancho: number; alto: number; top: number; left?: number};

const ZonaReservada: React.FC<{zona: Zona; etiqueta: string}> = ({zona, etiqueta}) => (
  <div
    style={{
      position: 'absolute',
      left: zona.left ?? (1080 - zona.ancho) / 2,
      top: zona.top,
      width: zona.ancho,
      height: zona.alto,
      border: '3px dashed rgba(255,45,141,0.95)',
      borderRadius: 22,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      whiteSpace: 'pre-line',
      textAlign: 'center',
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: 700,
      fontSize: 26,
      lineHeight: 1.35,
      color: '#ff2d8d',
      background: 'rgba(255,255,255,0.10)',
    }}
  >
    {etiqueta}
  </div>
);

/** Bloque centrado en la COLUMNA de composición (810), no en el margen. */
const Columna: React.FC<{top: number; children: React.ReactNode}> = ({top, children}) => (
  <div
    style={{
      position: 'absolute',
      left: (1080 - BETWEEN.bloque.columna) / 2,
      width: BETWEEN.bloque.columna,
      top,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    }}
  >
    {children}
  </div>
);

/** Cierre en cursiva, como el de `BetweenStS4.tsx`. */
const Cierre: React.FC<{size?: number; style?: React.CSSProperties; children: React.ReactNode}> = ({
  size = 34,
  style,
  children,
}) => (
  <div
    style={{
      width: BETWEEN.bloque.columna,
      textAlign: 'center',
      fontFamily: BETWEEN.fuentes.sans,
      fontStyle: 'italic',
      fontWeight: BETWEEN.pesos.semibold,
      fontSize: size,
      lineHeight: 1.3,
      color: BETWEEN.colores.beige,
      opacity: 0.95,
      textShadow: '0 2px 16px rgba(36,26,18,0.75)',
      whiteSpace: 'pre-line',
      ...style,
    }}
  >
    {children}
  </div>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 28-09 · HUMOR | CAFÉ TO GO  (col T · OK PARA DISEÑAR)

   Textos LITERALES de la grilla:
     · «Texto principal: POV: / YO CARGANDO EL PESO / DE MIS GANAS DE CAFÉ.»
   La columna no trae fila de INTERACCIÓN, así que no hay zona reservada.

   ⭐ EL PUNTO FINAL NO VA: «los títulos nunca llevan punto final» (regla de
   Eli). `TitularBetween` lo saca solo — no se le pasa `mantenerPunto`.

   ⭐ EL CORTE DE LÍNEA ES EL DEL BRIEF, y el cuerpo sale de ahí.
   «DE MIS GANAS DE CAFÉ» son 20 caracteres, así que en la columna de 810 el
   `ajustarACaber` baja el titular bastante por debajo del token de 117. Se
   respeta igual: el corte en dos líneas es el ritmo del chiste y el texto va
   literal. Para compensar, el bloque usa el ancho MÁXIMO que permite el manual
   —912 px, o sea los 84 px de margen lateral mínimo a cada lado— en vez de la
   columna de 810.
   ══════════════════════════════════════════════════════════════════════════ */

/** 1080 − 2 × 84 (margen lateral mínimo del manual). */
const ANCHO_MAXIMO = 1080 - 2 * BETWEEN.bloque.margenX;

export const StS5HumorToGo: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    {/* `oscurecer` 0: la banda del titular ya da 8,1–14,8:1. Un multiply
        encima sólo apagaría el cartón kraft del vaso, que es el protagonista. */}
    <FotoFondo src={F + 'st-28-09-togo.jpg'} oscurecer={0} />

    {/* SIN `LogoBetween`: el vaso ya trae el logotipo impreso (regla 8). */}

    <Columna top={262}>
      <TitularBetween
        script="POV:"
        caps={'Yo cargando el peso\nde mis ganas de café'}
        alinear="centro"
        tono="beige"
        anchoDisponible={ANCHO_MAXIMO}
      />
    </Columna>
  </AbsoluteFill>
);

/** La copia con la rejilla de medición, sólo para revisar. No se entrega. */
export const StS5HumorToGoGuia: React.FC = () => (
  <AbsoluteFill>
    <StS5HumorToGo />
    <ZonaReservada
      zona={{ancho: 912, alto: 580, top: 300}}
      etiqueta={'BANDA LIMPIA MEDIDA\ny=300 a 880 · 8,1–14,8:1'}
    />
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 30-09 · PLATEADA AL CARMENERE  (col U · OK PARA DISEÑAR) · ANIMADA

   Textos LITERALES de la grilla:
     · «Texto principal: ¿EL ALMUERZO SE QUEDÓ EN CASA?»
     · «Tranqui, el plan B / se ve bastante mejor por acá.»
     · «Plateada al Carmenere»
     · «Cierre / CTA: Haz tu pausa de almuerzo en Between.»
     · «INTERACCIÓN: LINK CARTA» → zona reservada, no se dibuja.

   ⭐ 9 SEGUNDOS, y el número sale del encargo. Eli: «no deben durar más de 15
   segundos […] puede ser mínimo de 8 a 9 segundos». 9 s × 30 fps = 270 frames.

   ⭐ EL MOVIMIENTO ES DE LA FOTO, NO DEL TEXTO QUE BAILA.
   El fondo es un clip real generado desde la MISMA fotografía fija que se
   midió: acercamiento lentísimo, el vapor que sube de la carne y las hojas del
   fondo moviéndose apenas. Todo lo demás está quieto. El texto sólo entra —no
   rebota, no gira, no hace efecto— porque la marca es «juvenil pero con un
   punto de estatus» y una tipografía que se mueve la abarata.

   Los tiempos de entrada, escalonados, en frames:
     ·   0–18  el titular (script + caja alta)
     ·  14–32  la bajada
     ·  28–46  la caja taupe del producto
     ·  42–60  el cierre
   Los 210 frames restantes la pieza queda quieta y legible, que es lo que hace
   falta para leerla en una historia.
   ══════════════════════════════════════════════════════════════════════════ */

export const DURACION_PLATEADA = 270;           // 9 s a 30 fps

/** ⭐ LA ZONA DEL ENLACE SE MIDE EN EL ÚLTIMO FRAME, NO EN EL PRIMERO.
 *
 * Es la diferencia con una pieza estática y costó rehacerla: la cámara hace un
 * acercamiento durante los 9 s, así que el plato SUBE dentro del cuadro y lo
 * que al empezar era mesa limpia al terminar es loza. Midiendo el borde del
 * plato cuadro a cuadro, el corredor libre entre el cierre del bloque (y≈965)
 * y el plato pasa de ~300 px al principio a **175 px al final** (y=965 a
 * y=1140). La pastilla se dimensiona contra ESE peor caso.
 *
 * Va CENTRADA —a diferencia de la del 22-09, donde la copa ocupaba el eje y
 * tuvo que irse al canal izquierdo—: acá la mesa de teca cruza limpia de lado
 * a lado y lo único que hay son el notebook cerrado, el celular y los anteojos,
 * que son elementos de fondo. La regla es que la zona no lleve gráfica NUESTRA,
 * no que la foto esté vacía.
 *
 * ⭐⭐ RONDA 33/34 — LA ZONA BAJA, PORQUE AHORA HAY UN CUADRO ENCIMA.
 * Era 340 × 140 en y=990, que cabía cuando el bloque de texto iba suelto sobre
 * la foto. Con el cuadro de vidrio encima la zona pasa a
 * **340 × 120 en y=1007**.
 *
 * ⛔ Y se corrigieron DOS cosas que estaban mal anotadas:
 *   · el borde del plato en el último frame no está en y=1140 sino en **1127**
 *     (medido: corrida de más de 420 px de loza clara y poco saturada);
 *   · pero el obstáculo de verdad **no es el borde del plato, es la COMIDA**, y
 *     empieza en **y=1230**. Entre 1127 y 1230 hay 103 px de ala de loza limpia,
 *     vacía, medida fracción a fracción (0,00 de comida en todo ese tramo).
 *
 * ✅ **Resuelto al elegir Eli la variante sin Brushwell.** El cuadro mide 35 px
 * menos, así que se subió 12 px más (`VIDRIO.top` 400 → 388) y la zona quedó en
 * **340 × 120 en y=1007 → 1127**: termina justo en el borde del plato y **no lo
 * pisa en ningún fotograma**. El ala de loza limpia que hay entre 1127 y 1230
 * queda de colchón, sin usarse. */
const ZONA_ENLACE: Zona = {ancho: 340, alto: 120, top: 1007};

/** Entrada suave: opacidad + 28 px de subida, con easing de salida. */
const useEntrada = (desde: number, largo = 18) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [desde, desde + largo], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const suave = 1 - Math.pow(1 - t, 3);
  return {opacity: suave, transform: `translateY(${(1 - suave) * 28}px)`};
};

const Entra: React.FC<{desde: number; children: React.ReactNode}> = ({desde, children}) => (
  <div style={{...useEntrada(desde), width: '100%', display: 'flex', justifyContent: 'center'}}>
    {children}
  </div>
);

/* ══════════════════════════════════════════════════════════════════════════
   ⭐⭐⭐ EL CUADRO DE VIDRIO — todos los números salen de medir la referencia.
   Ver la cabecera del archivo: `RONDA 33`.
   ══════════════════════════════════════════════════════════════════════════ */

const VIDRIO = {
  /** La caja de márgenes del manual: 1080 − 2×84. Nada de la pieza la cruza. */
  ancho: 1080 - 2 * BETWEEN.bloque.margenX,
  /**
   * ⭐⭐ RONDA 34 — VUELVE AL 84 DE LA REFERENCIA. Eli: «más similar el recuadro
   * a la ref».
   *
   * 84 es el 9,2 % de 912, que es exactamente la proporción medida en la ref
   * (33 sobre 360) — y además `BETWEEN.bloque.margenX`. En la ronda 33 hubo que
   * bajarlo a 72 porque el titular en caja alta ExtraBold hacía un cuadro de 637
   * de alto y el sticker del enlace ya no cabía. **Con el titular en caja baja y
   * SemiBold el bloque se acorta, así que el aire de la ref vuelve a caber.**
   *
   * ⭐ El de abajo va en 62 (6,8 %) y NO es un descuido: el último elemento del
   * cuadro es el cierre en cursiva, cuyo propio interlineado ya deja ~20 px de
   * aire bajo la tinta, mientras que arriba la tinta del titular arranca clavada
   * en el borde de su caja. 62 + 20 = 82 ≈ los 84 de arriba. **El aire que se VE
   * queda simétrico; el que se ESCRIBE, no.**
   */
  padX: 84,
  padTop: 84,
  padBottom: 62,
  /** Radio = padding, que es la relación que tiene la ref (33 y 33). */
  radio: 84,
  /**
   * Velo BLANCO, α medido por canal: 0,216 · 0,210 · 0,205.
   *
   * ⭐ RONDA 34 — verificado que es PLANO, no un degradado. Cruzando el borde
   * derecho tramo por tramo (mismo material a los dos lados) da 0,182 · 0,183 ·
   * 0,188 · 0,188 · 0,193 · 0,195 · 0,200 · 0,204 de arriba abajo: sin
   * tendencia. El borde izquierdo marca 0,25 en la mitad de arriba, pero ahí la
   * pared de afuera tiene una moldura que la oscurece — no es el velo.
   */
  relleno: 0.21,
  /** El filete de la ref es 1 px @736; acá escala a 1,5. */
  filete: 1.5,
  fileteAlfa: 0.55,
  /** Lo que hace que se lea como CRISTAL y no como un rectángulo pintado. */
  desenfoque: 3.5,
  /** ⭐ La ref NO lleva sombra: el perfil hacia afuera del borde superior es
   *  plano (138 · 138 · … · 139). Una sombra lo volvería una calcomanía. */
  sombra: 'none',
  /**
   * ⭐ RONDA 34 FINAL — 388, o sea 24 px bajo la tinta del lockup (y=364).
   *
   * Venía de 400. Se subió 12 px para que la zona del sticker quepa ENTERA sobre
   * la mesa: con el cuadro cerrando en y=993 y una zona de 120, el sticker
   * termina justo en y=1127, que es el borde del plato. Ni un píxel encima.
   */
  top: 388,
} as const;

/** Medida interior real: hay que descontar también el filete. */
const MEDIDA_VIDRIO = VIDRIO.ancho - 2 * (VIDRIO.padX + VIDRIO.filete);

/**
 * El panel. Se dimensiona SOLO con su contenido —por eso lleva `padding` y no
 * un alto quemado—: si mañana cambia una línea del brief, el cuadro la sigue.
 */
const PanelVidrio: React.FC<{style?: React.CSSProperties; children: React.ReactNode}> = ({
  style,
  children,
}) => (
  <div
    style={{
      position: 'absolute',
      left: (1080 - VIDRIO.ancho) / 2,
      top: VIDRIO.top,
      width: VIDRIO.ancho,
      boxSizing: 'border-box',
      padding: `${VIDRIO.padTop}px ${VIDRIO.padX}px ${VIDRIO.padBottom}px`,
      borderRadius: VIDRIO.radio,
      background: `rgba(255,255,255,${VIDRIO.relleno})`,
      border: `${VIDRIO.filete}px solid rgba(255,255,255,${VIDRIO.fileteAlfa})`,
      backdropFilter: `blur(${VIDRIO.desenfoque}px)`,
      WebkitBackdropFilter: `blur(${VIDRIO.desenfoque}px)`,
      boxShadow: VIDRIO.sombra,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      ...style,
    }}
  >
    {children}
  </div>
);

/**
 * ⭐⭐⭐ RONDA 34 (21-09) — EL TITULAR SALE DE LA FÓRMULA
 *
 * Eli: «que este texto sea en solo la primera mayúscula, la demás no, y en
 * raleway pero no tan gruesa. ya que hay muchos similares en historias.»
 *
 * El motivo NO es estético: **script Brushwell + caja alta ExtraBold es la
 * fórmula que llevan todas sus stories**, y una pieza que quiere distinguirse
 * tiene que salirse de ella. Por eso el titular pasa a caja baja y baja de peso.
 *
 * ⭐ «solo la primera mayúscula» se leyó sobre la FRASE COMPLETA, no sobre la
 * línea: el titular es una sola oración —«¿El almuerzo se quedó en casa?»— así
 * que la mayúscula es la E de «El» y la segunda línea entra en minúscula. Es
 * además lo correcto en castellano.
 *
 * ⭐ **El peso salió medido, y coincide con lo que ella ya había dictado.** Sobre
 * la referencia, grosor de asta dividido por altura de x:
 *
 *   | | asta/x |
 *   |---|---|
 *   | ref · palabras livianas («começa», «e continua») | **0,167–0,182** |
 *   | ref · palabras pesadas («Cuidar de você», «prato») | 0,333–0,364 |
 *   | Raleway Medium 500 | 0,165 |
 *   | Raleway SemiBold 600 | **0,200** |
 *   | Raleway ExtraBold 800 *(lo que tenía)* | 0,257 |
 *
 * O sea que la ref cae entre Medium y SemiBold. Se eligió **SemiBold**, que es
 * lo que Eli pidió por escrito el 09-09 para la ST del 22-09 («los títulos que
 * sean en raleway semi bold»): cuando la medición y su criterio caben los dos,
 * manda su criterio. La variante en Medium se rinde aparte para que elija.
 *
 * ⭐⭐ **ELEGIDO POR ELI (21-09): «B · sin Brushwell, todo Raleway».** La duda era
 * si «en raleway» incluía también la línea que iba en Brushwell, y la respuesta
 * fue que sí. Así que la pieza va con **una sola familia y una sola oración en
 * dos líneas**, que es exactamente lo que hace la referencia — y el precedente
 * ya existía: el 01-09, en el carrusel Cowork, pidió «que sea de la familia de
 * raleway, así se diferencia».
 *
 * ⭐ Y tuvo una consecuencia de diagramación: sin la Brushwell —que sola ocupaba
 * 113 px de tinta— **el cuadro bajó de 640 a 605 de alto**, y con eso la zona del
 * sticker vuelve a caber ENTERA sobre la mesa, sin pisar el plato.
 *
 * Las variantes `pesoTitular` y `script` se quedan en el componente: la decisión
 * está tomada, pero el repertorio queda escrito por si otra pieza lo necesita.
 */
export const StS5Plateada: React.FC<{
  guia?: boolean;
  /** 600 SemiBold (lo entregado) · 500 Medium (lo que mide la ref). */
  pesoTitular?: number;
  /** La línea de acompañamiento: la script de la marca o Raleway. */
  script?: 'brushwell' | 'raleway';
}> = ({guia = false, pesoTitular = BETWEEN.pesos.semibold, script = 'raleway'}) => {
  const {durationInFrames} = useVideoConfig();

  return (
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
      <AbsoluteFill>
        <OffthreadVideo
          src={staticFile(F + 'st-30-09-plateada.mp4')}
          style={{width: '100%', height: '100%', objectFit: 'cover'}}
          muted
        />
      </AbsoluteFill>

      {/* El lockup entra con la pieza, no aparece de golpe. */}
      <div style={useEntrada(0, 22)}>
        <LogoBetween formato="story" posicion="arriba" tono="beige" />
      </div>

      {/* ⭐ EL CUADRO DE VIDRIO ES EL CONTENEDOR, no un adorno detrás. Entra con
          la pieza y después se van escalonando sus contenidos — igual que en la
          ref, donde lo primero que existe es la tarjeta. */}
      <PanelVidrio style={useEntrada(0, 22)}>
        <Entra desde={0}>
          <TitularBetween
            script="¿El almuerzo"
            scriptSans={script === 'raleway'}
            /* ⭐ minúscula: la frase viene de la línea de arriba (ronda 34). */
            caps="se quedó en casa?"
            cajaAlta={false}
            pesoCaps={pesoTitular}
            alinear="centro"
            tono="beige"
            anchoDisponible={MEDIDA_VIDRIO}
          />
        </Entra>

        <Entra desde={14}>
          <Bajada
            size={40}
            tono="beige"
            style={{
              marginTop: BETWEEN.aire.tituloABajada,
              textAlign: 'center',
              whiteSpace: 'pre-line',
              fontWeight: 500,
            }}
          >
            {'Tranqui, el plan B\nse ve bastante mejor por acá.'}
          </Bajada>
        </Entra>

        {/* UNA sola caja taupe: es el énfasis, y el énfasis es el producto.
            Dentro del vidrio sigue siendo el único objeto MACIZO, que es lo que
            la hace leerse como la ficha del plato. */}
        <Entra desde={28}>
          <div style={{marginTop: BETWEEN.aire.tituloACaja}}>
            <CajaDato anchoDisponible={MEDIDA_VIDRIO}>Plateada al Carmenere</CajaDato>
          </div>
        </Entra>

        {/* ⭐ EL CIERRE ENTRA AL BLOQUE DE ARRIBA, no al pie — mismo motivo que
            en la del 22-09: abajo está el plato, y el texto de la marca se
            apoya en el fondo, nunca sobre el producto. */}
        <Entra desde={42}>
          <Cierre style={{marginTop: 26, width: MEDIDA_VIDRIO}}>
            Haz tu pausa de almuerzo en Between.
          </Cierre>
        </Entra>
      </PanelVidrio>

      {guia ? (
        <>
          <ZonaReservada zona={ZONA_ENLACE} etiqueta={'LINK CARTA\n340 × 120'} />
          <div
            style={{
              position: 'absolute',
              left: 0,
              right: 0,
              top: 1580,
              height: 1920 - 1580,
              borderTop: '3px dashed rgba(255,45,141,0.6)',
            }}
          />
          <div
            style={{
              position: 'absolute',
              left: 24,
              top: 1600,
              color: '#ff2d8d',
              fontFamily: BETWEEN.fuentes.sans,
              fontWeight: 700,
              fontSize: 24,
            }}
          >
            {`zona segura inferior de Meta · ${durationInFrames} frames = ${(durationInFrames / 30).toFixed(0)} s`}
          </div>
        </>
      ) : null}
    </AbsoluteFill>
  );
};

export const StS5PlateadaGuia: React.FC = () => <StS5Plateada guia />;

