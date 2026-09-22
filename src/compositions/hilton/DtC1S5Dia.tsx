/**
 * DOUBLETREE — CARRUSEL DE VIDEOS · «TU DÍA EN DOUBLETREE» (FEED col M · 28-09 · 12:00)
 *
 * Encargo de Eli, 17-09-2026: «Trabajaremos en el diseño del carrusel de la S5
 * de Doubletree de Septiembre, el último carrusel. Te dejo las referencias
 * visuales de portada y otras slide. Ten en mente que falta un slide que
 * contenido aún no agrega, pero diseña así tenemos adelantado todo lo demás.
 * Son animados, por lo que te pido que uses los espacios de esta sesión, que no
 * duren más de 6 segundos y sean muy lindos, estilo travel.»
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL — no se toca ni una palabra (§G: en DT sólo se DISEÑA)
 * ══════════════════════════════════════════════════════════════════════════
 * Hoja FEED, columna N. Releído de la grilla VIVA el **21-09** (API de Sheets).
 * ESTADO: `CORREGIDA` — el 17-09 decía `REVISAR CONTENIDO`.
 *
 * ⭐⭐ **EL 21-09 CONTENIDO ESCRIBIÓ EL SLIDE QUE FALTABA.** El brief pasó de
 * cuatro slides a **cinco**: entra `SLIDE 4 – SIGUE CON TU RUTINA DIARIA (GYM)`
 * y el cierre en la habitación, que era el 4, pasa a ser el **5**. Es el único
 * cambio del brief; palabra por palabra, lo demás está idéntico (diff contra la
 * instantánea `clients/hilton/grillas/api/dt-sept-20260915.json`).
 *
 *     CARRUSEL DE VIDEOS – TU DÍA EN DOUBLETREE BY HILTON SANTIAGO-VITACURA
 *
 *     Carrusel tipo timeline que recorre un día de estadía enfocado en el
 *     huésped de negocios/eventos, manteniendo el enfoque de detalle y espacios
 *     (sin necesidad de modelos), formato controlable por el equipo. Retoma el
 *     territorio "Vive la experiencia Hilton" pero con hilo narrativo de un día.
 *
 *     SLIDE 1 – DESAYUNO ANTES DE LA REUNIÓN
 *     Visual: Detalle de mesa de desayuno servida o buffet, ambiente luminoso,
 *     fondo desenfocado.
 *     Texto: "Empieza el día con la energía correcta."
 *
 *     SLIDE 2 – REUNIÓN EN SALÓN
 *     Visual: Toma de uno de los salones de eventos, montaje o detalle de la
 *     sala lista para reunión (sin personas, foco en el espacio).
 *     Texto: "Un espacio a la altura de tus reuniones."
 *
 *     SLIDE 3 – TIEMPO PARA TI (COWORK / LOBBY)
 *     Visual: Detalle de zona de lobby o cowork, luz natural, ambiente tranquilo.
 *     Texto: "Entre reunión y reunión, un momento para respirar."
 *
 *     SLIDE 4 - SIGUE CON TU RUTINA DIARIA (GYM)
 *     Visual: Mostrar espacio disponible del GYM (Sin personas)
 *     Texto: "Un espacio para mantenerte en movimiento."
 *
 *     SLIDE 5 – CIERRE EN LA HABITACIÓN
 *     Visual: Toma de la habitación al atardecer o cama tendida con luz cálida,
 *     ambiente de descanso.
 *     Texto: "El día termina como debe: con comodidad."
 *
 * Y la fila COMENTARIOS PARA DISEÑO de la misma columna:
 *
 *     Faltó GYM!
 *     Vamos con distintas cosas que se pueden hacer como ''Tu día en DoubleTree
 *     by Hilton Santiago-Vitacura''
 *     Puede ser como un carrusel de videos en que se ponga en cada slide una
 *     hora, EJ: 8:30 DESAYUNO BUFFET, 9:30 EVENTO EN UNO DE LOS SALONES, 12
 *     TIEMPO PARA COWORK, 16:00 UN RATO PARA ENTRENAR EN EL GYM. (Similar, no
 *     tiene que ser exactamente esto)
 *
 * ⚠️⚠️ LO QUE HAY QUE INFORMAR, NO RESOLVER (§G)
 *
 * 1 · ✅ **RESUELTO EL 21-09 — el GYM ya tiene brief.** Era el punto abierto
 *     desde el 17-09. Entra como slide 4, con su visual y su texto escritos por
 *     contenido, y el carrusel pasa de 5 a **6 láminas** (portada + 5).
 * 2 · **La habitación SIGUE sin HORA.** El comentario da tres —8:30 desayuno,
 *     9:30 salones, 12 cowork— y la cuarta que da es la del gym, que es la que
 *     ahora se usa. Para el cierre en la habitación no hay hora, y ponerle una
 *     sería escribir contenido. Va SIN sello: es un prop, entra en un render.
 * 3 · **Los textos del brief terminan en punto** y la regla F.1 de DT dice que
 *     los títulos no llevan punto. Van LITERALES: corregirlos es editar el
 *     copy. Si el cliente los quiere sin punto, lo pide y se cambia.
 * 4 · **El rótulo del gym va «SIGUE CON TU RUTINA DIARIA», sin el «(GYM)».** Es
 *     la misma regla que ya se aplicó en el slide 3: el brief dice «TIEMPO PARA
 *     TI (COWORK / LOBBY)» y el sello dice «TIEMPO PARA TI». El paréntesis del
 *     brief nombra el ESPACIO, que es lo que muestra la foto, no el rótulo. Los
 *     otros tres rótulos van textuales porque no traen paréntesis.
 *
 * ⚠️ Y una de formato: «12» del comentario se compone **12:00**, para que la
 * columna de horas sea una sola serie junto a 8:30 y 9:30. Es formateo de una
 * cifra, no redacción — pero queda dicho.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * RONDA 5 — EL COMENTARIO DE CONSTANZA LIZANA (22-09, 11:49) SOBRE LA GRILLA
 * ══════════════════════════════════════════════════════════════════════════
 * Y la observación que Eli sumó encima, el mismo día, sobre la portada.
 * Literal, las tres cosas:
 *
 *   1. «en la slide 1 (portada) el texto no me gusta animado, el video detrás
 *      al tener movimiento hace que el texto con más movimiento maree. Me
 *      gustaría el texto estático pero el globo que encierra "tu día" sea
 *      animado.»
 *   2. «en el resto de las slides todo lo veo ok, pero en la parte inferior
 *      donde dice "DT by hilton stgo - vitacura" me gustaría que se eliminara,
 *      para que no tenga tanto elemento por slide.»
 *   3. (Eli) «que en el texto de la portada diga DoubleTree by Hilton en la
 *      misma tipografía del título, ya que se ve como diferente y la idea es
 *      que se vea muy igual. "en DoubleTree by Hilton" sería la segunda
 *      tipografía y la tercera "Santiago Vitacura".»
 *
 * ── 1 · LA PORTADA SE QUEDA QUIETA, Y EL TRAZO ES LO ÚNICO QUE SE MUEVE ────
 * Se van las CUATRO entradas de la portada —la itálica, el titular, la bajada
 * y la píldora—. No sólo las tres de texto: la píldora también lleva texto y
 * también entraba con un fade+subida, y el motivo que da Constanza —el clip de
 * la llegada ya se mueve por debajo— vale igual para ella. Queda en pie
 * `Circulo`, que se dibuja del f8 al f46 y ahora es el único gesto de la
 * lámina. En el bucle de Instagram eso se lee mejor que antes: el trazo se
 * redibuja en cada vuelta y ya no compite con nada.
 *
 * ⚠️ Las CINCO INTERIORES conservan sus entradas: Constanza dice «en el resto
 * de las slides todo lo veo ok». No se tocan.
 *
 * ── 2 · LA VERSALITA AL PIE SALE DE LAS CINCO INTERIORES ───────────────────
 * `<Firma>` se queda sólo en la portada, que es donde el carrusel firma. Y
 * coincide con el manual: §B dice que en feed el logotipo por defecto no va, y
 * la regla del estudio es que en un carrusel la marca firma en la portada.
 *
 * ⚠️ **PENDIENTE DE ELI:** en la portada la firma quedó diciendo
 * «DOUBLETREE BY HILTON SANTIAGO–VITACURA» al pie mientras el bloque de arriba
 * dice, ahora, exactamente lo mismo. Es la única lámina donde el nombre sale
 * dos veces. Constanza acotó su pedido a «el resto de las slides», así que la
 * firma se DEJÓ; va en la revisión como opción B para que ella decida.
 *
 * ── 3 · LA JERARQUÍA DE LA PORTADA, RE-ORDENADA EN TRES NIVELES ────────────
 * El nombre de la marca venía partido entre dos voces tipográficas —«DoubleTree»
 * en el titular a 108 y «by Hilton» en la bajada a 42 Light—, y eso es lo que
 * Eli lee como «se ve diferente». Ahora:
 *
 *   | nivel | ronda 3 | ronda 5 |
 *   |---|---|---|
 *   | 1 | «Tu día» · Stag LightItalic 72, circulada | **igual, intacta** |
 *   | 2 | «en DoubleTree» · Stag Medium 108 | **«en DoubleTree by Hilton»** · Stag Medium **80,606** |
 *   | 3 | «by Hilton Santiago–Vitacura» · Stag Light 42 | **«Santiago–Vitacura»** · Stag Light 42, igual |
 *
 * ⭐⭐ **EL CUERPO ES LA CONSECUENCIA DE LA MEDIDA, NO LA DECISIÓN** — es el
 * criterio que dictó Eli en DT el 15-09 sobre el estático de Honors. «en
 * DoubleTree by Hilton» a cuerpo 108 mide **1211,2 px** de tinta y la columna
 * son **904**: no cabe, y no es negociable. **80,606** es el cuerpo exacto al
 * que la tinta mide 904,00 px y el renglón nace en 88 y muere en 992 — flush
 * contra los dos márgenes. Medido glifo a glifo sobre `Stag-Medium.ttf` con el
 * `letter-spacing` de +0,012em, no estimado.
 *
 * ⛔ **Y por qué NO se justificaron los tres renglones a una medida común**,
 * que es lo que pide ese mismo criterio: porque acá la línea larga es la que
 * tiene que pesar. A una medida común de 904, «Santiago–Vitacura» saldría a
 * cuerpo **109,3** y el nombre de la marca a **80,6** — la ciudad más grande
 * que el hotel. La propia memoria del criterio deja escrita la excepción: «si
 * en otra pieza la línea larga es la que tiene que pesar, se parte en dos
 * ANTES de justificar». Acá se partió: el nivel 2 es el nombre y el 3 la
 * ciudad, cada uno con su cuerpo.
 *
 * ⚠️ Lo que costó, y hay que mirarlo: el titular baja de 108 a 80,6, así que
 * contra «Tu día» (72) la diferencia de cuerpo es chica. Lo que sostiene la
 * jerarquía es el PESO —Medium contra LightItalic— y el trazo, no el tamaño.
 * Es lo mismo que dice el criterio de Honors: «el peso sigue mandando la
 * jerarquía; el tamaño no».
 *
 * ⭐ El ritmo vertical se re-midió sobre el render, no a ojo: el hueco entre el
 * canto del trazo y la tinta del titular vuelve a los **28 px** que aprobó la
 * ronda 3 (`marginBottom` 8 → 15, porque a cuerpo 80,6 la tinta nace más
 * arriba dentro de su caja de línea), y el hueco contra el tercer nivel queda
 * en **42 px** ≈ 1,5× el de arriba, que es la proporción que pide
 * `jerarquia-de-bloque-de-texto`.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA DIRECCIÓN DE ARTE — sale de las DOS REFERENCIAS QUE DEJÓ ELI
 * ══════════════════════════════════════════════════════════════════════════
 * `S5 HILTON SEP 2026 › DT › REFERENCIA CARRUSEL` (subidas el 17-09 a las 14:30):
 *   · `REF PORTADA CARRUSEL.jpg`        — 736×920
 *   · `SLIDE 2 Y SIGUIENTES REF CARRUSEL.jpg` — 736×920
 * Copia de trabajo en `raw/hilton/dt/s5-sept/refs/`.
 *
 * Lo que mandan, elemento por elemento:
 *
 * | Referencia | Cómo entra en DT |
 * |---|---|
 * | Foto a sangre, velo oscuro, registro editorial de viaje | ✅ tal cual, con el velo AZUL DT |
 * | Una palabra manuscrita dentro de un **círculo dibujado a mano** | ✅ el círculo se dibuja; la palabra va en **Stag Italic**, no en una script |
 * | Titular grande en serif, caja baja | ✅ Stag, que ES la serif de la marca |
 * | Píldora blanca «Swipe →» abajo | ✅ «Desliza», mismo objeto |
 * | Firma en versalitas espaciadas abajo a la derecha | ✅ Trade Gothic, que es el recurso de versalita al pie que ya tiene DT (`C1 FT N1`) |
 * | Interiores: UNA línea arriba a la izquierda, sin panel | ✅ tal cual |
 *
 * ⛔⛔ **LO ÚNICO QUE NO SE COPIA ES LA LETRA MANUSCRITA, Y ES A PROPÓSITO.**
 * Las dos referencias resuelven su acento con una script. En DT la tipografía
 * la manda el manual oficial —**Stag + Trade, y nada más**, regla de Eli del
 * 03-09— y meter una tercera familia es abrirle una fuente a la marca, que no
 * lo decide una pieza. El acento va en **Stag Italic**, con el precedente de la
 * ST del 18-09: «las versales fueron en Stag itálica y no en Trade Gothic»
 * porque así lo traía la referencia de Eli. El gesto de la referencia —el
 * trazo a mano— **sí** entra, pero como DIBUJO (`Circulo`), no como fuente.
 * Si ella quiere la manuscrita literal, eso lo aprueba la marca, no la pieza.
 *
 * ⛔ **NO HAY ACENTO DE COLOR. RONDA 2.** La ronda 1 usaba el verde Hilton
 * `#A3CD39` —el 20 % de la paleta oficial— para el trazo de la portada y el
 * guion del sello. Eli lo sacó: «no uses el verde de DT». Todo va en blanco
 * sobre el velo azul. El manual manda en color, pero **qué color de la paleta
 * entra en una pieza es composición, y la composición es de ella**.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA GEOMETRÍA Y LAS REGLAS DE DT QUE SE APLICAN
 * ══════════════════════════════════════════════════════════════════════════
 * · Mesa **1080×1350** (4:5). ⚠️ A diferencia de las piezas estáticas de esta
 *   cuenta, **el máster NO es 2250**: es video para Instagram, que entrega a
 *   **1080×1350**. Rendir a 2250 es dar un archivo que la plataforma vuelve a
 *   comprimir a 1080 igual.
 * · **150 frames a 30 fps = 5,0 s**, bajo el tope de 6 s que puso Eli.
 * · Margen lateral **88 px** (medido en `C1 FT N2`).
 * · Logotipo: ancho **160**, tope **111**, centrado, a su proporción real
 *   **1,2254** — la plantilla `logo-post.png`. **Sólo en la portada**: en feed
 *   el logo no va por defecto, y en un carrusel va en la portada y en ninguna
 *   otra.
 * · Tinta del logotipo: **azul**, §B.4 — el cielo de esa lámina es claro y el
 *   blanco se pierde. Medido: **9,24:1** en azul contra **1,62:1** en blanco.
 * · Titular a **DOS PESOS y UN MISMO CUERPO**: arriba Stag Medium, abajo Stag
 *   Light. Es el recurso de DT y se aplica a cada frase del brief, partiéndola
 *   en gancho + remate.
 * · **La portada NO lleva velo: la tinta es AZUL.** Es la salida que escribe el
 *   propio manual para un titular sobre foto clara, y está medida. En las
 *   láminas interiores la tinta es blanca y el texto va ARRIBA, así que la
 *   rampa de DT va **espejada**: nace en 0 al 70 % de la altura y crece hacia el
 *   borde superior, más un pie que sostiene la versalita de la firma. El
 *   principio no cambia —sin franja plana, sin salto—, sólo el lado.
 * · **La portada firma con el LOCKUP y las interiores con la VERSALITA.** Nunca
 *   las dos en la misma lámina.
 * · Sombra paralela azul, la misma para todas las tintas blancas. El logotipo
 *   va SIN sombra (ronda 3 del estático de Honors).
 * · **En feed orgánico no hay zona segura de Instagram.** Aun así el bloque de
 *   texto se mantiene dentro del 88 y no toca los cantos.
 */
import React from 'react';
import {
  AbsoluteFill,
  Easing,
  getInputProps,
  Img,
  interpolate,
  OffthreadVideo,
  staticFile,
  useCurrentFrame,
} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';

cargarFuentesDT();

// ───────────────────────────────────────────────────────────────────────────
// Constantes de marca
// ───────────────────────────────────────────────────────────────────────────

/**
 * ⭐⭐ EL FOTOGRAMA DE CONTROL — `--props='{"soloFondo":true}'`.
 *
 * Rinde la lámina **sin una sola tinta**: sólo el clip y el velo. No es un
 * modo de entrega, es la regla de medición del QA, y nació de un fallo que el
 * gate cantó en falso en la ronda 5.
 *
 * ⛔⛔ EL PROBLEMA QUE RESUELVE. `peor_tercio` promedia la banda del texto para
 * sacar «el fondo» — y adentro de esa banda está la tinta. Mientras el texto
 * ENTRABA animado, el f0 se medía con la tinta todavía invisible y el número
 * salía limpio. Al dejar la portada quieta (pedido de Constanza) la tinta está
 * en pantalla desde el f0, la banda de «Tu día» pasó a llevar 13–25 % de píxeles
 * blancos y el QA cantó **2,69:1** sobre un fondo que de verdad da **3,52:1**.
 *
 * ⛔ Y no se arregla enmascarando por color: en estas láminas el fondo TIENE
 * blancos legítimos —el cielo entre las vigas de la marquesina, el cielo raso
 * del salón—, así que un umbral «>200 es tinta» borra justo el fondo más claro,
 * que es el que puede hundir el contraste. Sería un gate que se miente a favor.
 *
 * ⭐ La salida es no estimar el fondo: **medirlo**. Con esta bandera la lámina
 * se rinde sin tinta, el QA mide ese fotograma y el número que sale es el fondo
 * real, sin contaminación y sin borrar nada.
 */
const esSoloFondo = (): boolean =>
  Boolean((getInputProps() as {soloFondo?: boolean}).soloFondo);

const MARGEN = DT.geometria.margenLateral;            // 88 @1080
const ANCHO_UTIL = 1080 - MARGEN * 2;                 // 904

/**
 * ⭐⭐ LA SANGRÍA ÓPTICA — «alinea a la izquierda bien» (Eli, ronda 2).
 *
 * Poner tres elementos en el mismo `left: 88` **no los alinea**: cada letra trae
 * su propio hueco a la izquierda (el *side bearing*), y ese hueco depende del
 * glifo y de la fuente. Medido sobre los PNG de la ronda 1, la tinta arrancaba en:
 *
 *   | lámina | sello | titular 1 | titular 2 |
 *   |---|---|---|---|
 *   | Desayuno   | 90 | 89 | 91 |
 *   | Salón      | 90 | 89 | 91 |
 *   | Lobby      | **92** | 89 | 90 |
 *   | Habitación | 89 | 89 | 91 |
 *
 * Hasta **3 px** de diferencia dentro de una misma lámina, y el peor caso es el
 * `12:00` del lobby: el `1` de Trade Gothic Bold Condensed es el glifo con más
 * hueco de todo el carrusel. A tamaño de feed no se «ve», pero el canto
 * izquierdo es lo único que sostiene una diagramación alineada a la izquierda —
 * y ella lo marcó con una regla roja.
 *
 * Cada elemento se corre hacia la izquierda su propio hueco. Los valores salen
 * de MEDIR el render, y `dt-c1-s5-qa.py` los verifica en cada ronda: si alguien
 * cambia un texto, el hueco cambia y el QA lo canta.
 */
const sangria = (px: number) => ({marginLeft: -px});

/** La sombra de DT — una sola para todas las tintas blancas de la pieza. */
const SOMBRA = '0 2px 7px rgba(9,25,78,0.60), 0 0 2px rgba(9,25,78,0.45)';

/**
 * ⭐⭐ LA PORTADA NO LLEVA VELO, Y LA TINTA ES AZUL. Es la salida que el propio
 * manual de DT escribe, no un invento de esta pieza:
 *
 *   «Si el titular queda sin margen sobre foto clara, la salida NO es cargar el
 *    velo: es ponerlo en azul DT como el logotipo.»
 *
 * MEDIDO sobre el recorte, sin velo alguno, por tercios de cada banda:
 *
 *   | banda           | azul `#09194E` | blanco `#FAFAFA` |
 *   |---|---|---|
 *   | «Tu día»        | **9,93:1**  | 1,51:1 |
 *   | «en DoubleTree» | **3,15:1**  | 1,48:1 |
 *   | logotipo        | **9,24:1**  | 1,62:1 |
 *
 * ⛔ **LOS DOS CAMINOS QUE SE PROBARON Y NO SIRVEN, para no repetirlos.**
 * · La rampa CÓNCAVA del Día del Turismo (0,48 a media altura) sí sostiene la
 *   tinta blanca, pero esta foto tiene el sujeto ocupando dos tercios de la
 *   lámina y el velo se lo come: la torre queda gris. Contradice el encargo —
 *   «la foto real del hotel es el argumento de la pieza».
 * · La rampa CONVEXA de Honors deja la foto limpia y la tinta blanca cae a
 *   **1,93:1** en «Tu día» y **2,29:1** en el titular. Medido, no estimado.
 *
 * Con la tinta azul la foto queda intacta y las tres tintas pasan de sobra.
 *
 * ⭐ Y la píldora se INVIERTE: con todo el resto en azul sobre un fondo claro,
 * una píldora blanca se lee como un hueco. Va maciza en azul con tinta blanca,
 * que además es lo que hace que funcione como botón.
 */
/**
 * ⭐ EL VELO DE LA PORTADA — la rampa CÓNCAVA aprobada en la ST del Día del
 * Turismo: α = 0 en el borde superior y de ahí sube, con pendiente en el tercio
 * de arriba y aplanándose hacia el pie, que queda en **0,58**. El pie va cerca
 * de 0,58 y no más: un velo que tapa la foto contradice el encargo.
 *
 * ⚠️ HISTORIA, PORQUE SE FUE Y VOLVIÓ. En la ronda 1 la portada era la FOTO del
 * frontis a pleno día y esta rampa dejaba la torre gris —el sujeto ocupaba dos
 * tercios de la lámina—, así que se quitó el velo entero y la tinta pasó a azul.
 * En la ronda 2 la portada pasó a ser el VIDEO de la llegada, que es una escena
 * de cristal oscuro y sombra de árbol, y ahí el velo vuelve a ser lo correcto:
 * es el registro editorial de la referencia y sostiene la tinta blanca.
 * **La rampa no cambió; cambió la foto de abajo.**
 *
 * ⛔ El error a no repetir (ronda 4 de esa historia): dejarla PLANA en 0 una
 * franja y hacerla arrancar de golpe más abajo. Ese codo es una banda visible —
 * «se ve muy forzado».
 */
const VELO_PORTADA: readonly (readonly [number, number])[] = [
  [0, 0], [10, 0.11], [20, 0.22], [30, 0.33], [40, 0.42], [50, 0.48],
  [60, 0.52], [70, 0.55], [80, 0.57], [90, 0.58], [100, 0.58],
];

/**
 * ⭐ EL VELO DE LOS INTERIORES — la MISMA rampa, espejada, porque acá el texto
 * va arriba. Nace en 0 a media lámina y crece hacia el borde superior. Del 55 %
 * para abajo la foto queda limpia, que es lo que hace la referencia.
 *
 * Del 70 % al 78 % la foto queda completamente limpia, que es lo que hace la
 * referencia, y de ahí al pie vuelve a subir para sostener la versalita de la
 * firma: es la tercera vía entre «nada» y «velo», y se mide como todo lo demás.
 */
const VELO_INTERIOR: readonly (readonly [number, number])[] = [
  [0, 0.66], [8, 0.62], [16, 0.56], [24, 0.49], [32, 0.40], [40, 0.31],
  [48, 0.20], [55, 0.10], [62, 0.03], [70, 0],
  // ⭐ EL PIE: el degradado que sostiene la versalita de la firma. Se subió tres
  // veces y las tres por MEDICIÓN, no por gusto — con 0,16 la firma caía a
  // 2,95:1 sobre el lobby; con 0,34 seguía en 2,24:1 en el desayuno, donde justo
  // ahí abajo hay un canasto de fruta a plena luz; con 0,52 al BORDE todavía
  // daba 3,70:1.
  //
  // ⚠️ Y ahí está la trampa que enseñó esta pieza: **lo que importa no es cuánto
  // vale el velo en el borde, sino cuánto vale EN LA BANDA DEL TEXTO.** La firma
  // vive entre el 93,8 % y el 95,7 % de la altura, no en el 100 %. Despejando la
  // fórmula de contraste sobre el fondo real —L ≈ 0,335— hace falta α ≈ 0,52
  // **ahí**, así que la rampa se adelantó en vez de subirle el tope.
  //
  // Paradas cada 4-6 % para que el degradado no tenga ningún quiebre a la vista.
  [76, 0.06], [82, 0.17], [87, 0.30], [91, 0.41], [95, 0.52], [100, 0.60],
];

const rampa = (paradas: readonly (readonly [number, number])[]) =>
  `linear-gradient(to bottom, ${paradas
    .map(([p, a]) => `rgba(9,25,78,${a}) ${p}%`)
    .join(', ')})`;

// ───────────────────────────────────────────────────────────────────────────
// Movimiento — «estilo travel»: lento, continuo, y que frene al final
// ───────────────────────────────────────────────────────────────────────────

export const DURACION = 150;                          // 5,0 s a 30 fps

/**
 * ⭐ POR QUÉ FRENA AL FINAL. En un carrusel de Instagram cada video se repite
 * en bucle mientras el dedo se queda en esa lámina. Si el movimiento termina a
 * plena velocidad, el corte al primer fotograma se ve como un tirón. Con un
 * `easeOut` fuerte los últimos 30 fotogramas quedan casi quietos y el bucle no
 * se nota.
 */
const CAMARA = Easing.bezier(0.16, 0.62, 0.24, 1);

/** Suavizado de las entradas de texto. */
const ENTRADA = Easing.bezier(0.22, 0.9, 0.3, 1);

type Movimiento = {
  /** Escala inicial y final. Siempre ≥ 1,03 para que la deriva nunca vea borde. */
  z: [number, number];
  /** Deriva en px sobre la mesa de 1080, [x, y] inicial → final. */
  d: [[number, number], [number, number]];
};

const usaCamara = (m: Movimiento) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [0, DURACION - 1], [0, 1], {
    extrapolateRight: 'clamp',
    easing: CAMARA,
  });
  const escala = m.z[0] + (m.z[1] - m.z[0]) * t;
  const x = m.d[0][0] + (m.d[1][0] - m.d[0][0]) * t;
  const y = m.d[0][1] + (m.d[1][1] - m.d[0][1]) * t;
  return `translate(${x}px, ${y}px) scale(${escala})`;
};

/** Fade + subida, con retardo. El recurso de entrada de TODA la pieza. */
const usaEntrada = (desde: number, subida = 18, dura = 26) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [desde, desde + dura], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: ENTRADA,
  });
  return {opacity: t, transform: `translateY(${(1 - t) * subida}px)`};
};

// ───────────────────────────────────────────────────────────────────────────
// Piezas de dibujo
// ───────────────────────────────────────────────────────────────────────────

/**
 * ⭐ EL CÍRCULO A MANO de la referencia de portada.
 *
 * ⛔ **RONDA 2 (Eli, 17-09): «no uses el verde de DT».** El trazo y el guion del
 * sello iban en `#A3CD39`, que es el acento oficial del manual — y aun así ella
 * lo saca. Manda la diseñadora: el manual decide COLOR y TIPOGRAFÍA, pero qué
 * color de la paleta entra en una pieza es composición, y eso es de ella.
 * Los dos elementos pasan a **blanco**, que es la tinta del resto.
 *
 * No es una elipse: es un trazo que da una vuelta y **se pasa**, como cuando se
 * rodea una palabra con lápiz. Va dibujado con cuatro curvas cúbicas de radios
 * distintos —si las cuatro fueran iguales se leería como una forma de programa—
 * y se ANIMA dibujándose, que es de donde sale el gesto.
 *
 */
const Circulo: React.FC<{
  ancho: number;
  alto: number;
  grosor?: number;
  color?: string;
  desde: number;
}> = ({ancho, alto, grosor = 3.4, color = DT.colores.blanco, desde}) => {
  const frame = useCurrentFrame();
  const LARGO = 1000;
  const dibujado = interpolate(frame, [desde, desde + 38], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.3, 0.05, 0.2, 1),
  });
  // Trazo en coordenadas 0–200 × 0–100, escalado por el viewBox.
  const d =
    'M 150.5 14.2 ' +
    'C 108 3.5, 54 5.8, 26.5 22.4 ' +
    'C 1.2 37.6, 6.4 66.8, 36.8 80.6 ' +
    'C 72.5 96.8, 136.6 97.4, 170.9 81.2 ' +
    'C 199.8 67.6, 197.4 40.1, 170.2 25.3 ' +
    'C 158.6 19.0, 144.2 14.6, 129.4 12.6';
  return (
    <svg
      width={ancho}
      height={alto}
      viewBox="0 0 206 104"
      style={{position: 'absolute', left: 0, top: 0, overflow: 'visible'}}
    >
      <path
        d={d}
        fill="none"
        stroke={color}
        strokeWidth={grosor}
        strokeLinecap="round"
        pathLength={LARGO}
        strokeDasharray={LARGO}
        strokeDashoffset={LARGO * (1 - dibujado)}
        style={{filter: 'drop-shadow(0 2px 6px rgba(9,25,78,0.45))'}}
      />
    </svg>
  );
};

/** La flecha de la píldora. Línea limpia — DT no lleva textura de mano. */
const Flecha: React.FC<{tam: number; color: string}> = ({tam, color}) => (
  <svg width={tam} height={tam * 0.5} viewBox="0 0 40 20" fill="none">
    <path
      d="M2 10 H34"
      stroke={color}
      strokeWidth={2.2}
      strokeLinecap="round"
    />
    <path
      d="M26.5 3.5 L34 10 L26.5 16.5"
      stroke={color}
      strokeWidth={2.2}
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);

/** El tracking de la firma. Vive acá porque hay que restárselo al margen. */
const TRACKING_FIRMA = 0.3;
/**
 * Lo que se le resta por la derecha. Es el tracking MÁS el hueco propio del
 * último glifo: sólo con −0,30em la tinta llegaba a x=990 y el margen es 992.
 */
const COMPENSA_FIRMA = 0.33;

/**
 * La firma al pie, derecha — el equivalente de «GOLDEN NEST EXPERIENCES» de la
 * referencia. Usa el recurso de versalita de DT medido en `C1 FT N1`: Trade
 * Gothic, caja **15 px** @1080. No es el logotipo horizontal, que en esta marca
 * es excepción y la pide el cliente (§B.2).
 *
 * ⛔⛔ **LA TRAMPA DEL `letter-spacing`, Y ES LA QUE MARCÓ ELI EN LA RONDA 2.**
 * CSS agrega el espacio de tracking **también después de la ÚLTIMA letra**. En
 * un texto alineado a la derecha eso significa que la tinta NO llega al margen:
 * medido sobre las cuatro láminas de la ronda 1, la firma terminaba en **x=984**
 * cuando el margen es **992** — ocho píxeles de aire fantasma, exactamente donde
 * ella puso la marca roja del pantallazo.
 *
 * Se corrige con un `margin-right` negativo del mismo valor del tracking. Es la
 * misma trampa que ya tiene nombre en el estudio (`tracking-no-llega-a-inline-block`).
 */
const Firma: React.FC = () => {
  // ⚠️ RONDA 5: la firma ya no anima. Tenía una entrada con retardo (`desde`),
  // y se fue con el resto del movimiento de la portada — que es la única lámina
  // donde queda. El prop se borró en vez de dejarlo sin usar.
  return (
    <div
      style={{
        position: 'absolute',
        right: MARGEN,
        bottom: 62,
        fontFamily: DT.fuentes.texto,
        fontSize: 21,                 // caja ≈ 15 px
        letterSpacing: `${TRACKING_FIRMA}em`,
        marginRight: `${-COMPENSA_FIRMA}em`,   // ⛔ ver la nota de arriba
        color: DT.colores.blanco,
        textShadow: SOMBRA,
        whiteSpace: 'nowrap',
      }}
    >
      DOUBLETREE BY HILTON SANTIAGO–VITACURA
    </div>
  );
};

/**
 * ⭐ EL SELLO DE HORA — el recurso que pide la fila COMENTARIOS PARA DISEÑO
 * («que se ponga en cada slide una hora»).
 *
 * Va en **Trade Gothic**, y eso no es preferencia: los nueve cortes de Stag
 * comparten un subconjunto de 354 glifos y en DT las CIFRAS y las VERSALES son
 * trabajo de Trade. La cifra va en el corte Bold Condensed, el rótulo en
 * Regular con tracking, y entre los dos un guion blanco.
 *
 * ⚠️ Es un RÓTULO, no el título: por eso puede ir en versales aunque el título
 * de la lámina vaya en caja baja. La regla F.2 —no mezclar cajas— habla de las
 * líneas de un mismo título.
 */
const Sello: React.FC<{
  hora?: string;
  rotulo: string;
  desde: number;
  /** El hueco del primer glifo, medido. Ver `sangria`. */
  sangriaPx: number;
}> = ({hora, rotulo, desde, sangriaPx}) => (
  <div
    style={{
      display: 'flex',
      alignItems: 'center',
      gap: 16,
      ...sangria(sangriaPx),
      ...usaEntrada(desde, 12),
    }}
  >
    {hora ? (
      <>
        <span
          style={{
            fontFamily: "'Trade Gothic Cn', 'Trade Gothic', Arial, sans-serif",
            fontWeight: 700,
            fontSize: 40,
            letterSpacing: '0.02em',
            color: DT.colores.blanco,
            textShadow: SOMBRA,
            fontVariantNumeric: 'lining-nums tabular-nums',
          }}
        >
          {hora}
        </span>
        <span
          style={{
            width: 30,
            height: 2,
            background: DT.colores.blanco,
            boxShadow: '0 2px 6px rgba(9,25,78,0.45)',
          }}
        />
      </>
    ) : null}
    <span
      style={{
        fontFamily: DT.fuentes.texto,
        fontSize: 23,
        letterSpacing: '0.24em',
        color: DT.colores.blanco,
        textShadow: SOMBRA,
      }}
    >
      {rotulo}
    </span>
  </div>
);

// ───────────────────────────────────────────────────────────────────────────
// LA PORTADA
// ───────────────────────────────────────────────────────────────────────────

/**
 * ⭐⭐⭐ LA PORTADA — RONDA 2: «quiero que sea más igual a la referencia».
 *
 * La ronda 1 se apartaba de `REF PORTADA CARRUSEL.jpg` en cinco cosas, y las
 * cinco se corrigen acá:
 *
 * | | ronda 1 | referencia | ronda 2 |
 * |---|---|---|---|
 * | fondo | FOTO del frontis a pleno día | video con velo, registro editorial | **video de la llegada**, con velo |
 * | tinta | azul sobre cielo claro | blanca sobre velo | **blanca** |
 * | bloque | palabra circulada pegada al titular | circulada arriba, titular al medio, **bajada** debajo | igual que la referencia |
 * | píldora | maciza azul | **clara** con tinta oscura | clara |
 * | firma | lockup centrado arriba | versalitas abajo a la derecha | **versalitas**, sin lockup |
 *
 * ⭐ **EL VIDEO ES LA LLEGADA AL HOTEL.** `CONTENIDO HOTEL 2026 › Exterior
 * hotel` tiene un solo clip y resultó ser el correcto: la cámara llega a la
 * puerta y el **logotipo DoubleTree está grabado en el cristal**, grande. Eso es
 * lo que permite las dos correcciones de una vez — la marca entra por la
 * fotografía, así que el lockup sobrepuesto deja de hacer falta, que es
 * exactamente lo que hace la referencia.
 *
 * ⚠️ **Y por eso la portada YA NO LLEVA LOCKUP.** No es un descuido: §B del
 * manual dice que en feed el logotipo por defecto NO va —«ensucia el feed»— y
 * que sólo aparece en programas del hotel y piezas importantes. Un carrusel de
 * experiencia no es ninguno de los dos. Con esto las cinco láminas firman igual,
 * con la versalita al pie.
 *
 * ⭐ EL TITULAR SALE DEL BRIEF ENTERO, PARTIDO EN TRES — no se inventó ni una
 * palabra. El brief titula «TU DÍA EN DOUBLETREE BY HILTON SANTIAGO-VITACURA»:
 * «Tu día» es lo que rodea el trazo, «en DoubleTree» el titular y «by Hilton
 * Santiago–Vitacura» la bajada, que es el renglón que la referencia pide debajo
 * del título y que la ronda 1 no tenía.
 *
 * ⚠️ La caja pasa de versales (como lo escribe la grilla) a caja baja: eso es
 * diagramación, no redacción — todos los briefs de esta grilla vienen en
 * versales. Y la regla F.2 pide **una sola caja** por título, que se cumple.
 *
 * ⚠️ «Desliza» NO está en el brief: es la traducción del «Swipe» de la
 * referencia que eligió Eli, y el mismo verbo que el cliente usó en esta cuenta
 * («cambiar POSTULA AQUÍ → DESLIZA», Between, 16-09).
 *
 * ⚠️ En el clip entra gente de espaldas al hotel. No se ven rostros y en una
 * toma de llegada es lo que le da vida, pero queda dicho: el brief dice «sin
 * necesidad de modelos» y hay tramo sin nadie si se prefiere.
 */
export const DtC1S5Portada: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul, overflow: 'hidden'}}>
      <OffthreadVideo
        src={staticFile('assets/hilton/dt/s5/clips/portada.mp4')}
        style={{width: '100%', height: '100%', objectFit: 'cover'}}
        muted
      />

      {/*
        El velo de la referencia. Acá sí va —y va la rampa CÓNCAVA aprobada en la
        ST del Día del Turismo, 0 arriba → 0,58 al pie— porque el registro de la
        referencia es editorial y oscuro, y porque el bloque de texto ocupa de la
        mitad hacia abajo. Nace en 0 en el borde y sube sin ningún codo.
      */}
      <AbsoluteFill style={{background: rampa(VELO_PORTADA)}} />

      {/* De acá abajo, TODA la tinta. El fotograma de control la salta. */}
      {esSoloFondo() ? null : <>
      {/*
        ⭐ `top: 330` y no 300: a 300 la palabra circulada caía en la franja donde
        el velo todavía va en α ≈ 0,26 y el contraste quedaba en **3,00:1**,
        clavado en la vara. Bajar el bloque 30 px la mete en la parte del velo que
        ya pesa, y de paso la proporción queda más cerca de la referencia, donde
        el trazo va al 26 % de la altura y el titular al 43 %.
      */}
      <div style={{position: 'absolute', left: MARGEN, top: 330, width: ANCHO_UTIL}}>
        {/* El gesto de la referencia: «Tu día» rodeado a mano, arriba del todo. */}
        {/*
          ⭐⭐ RONDA 3 (Eli, 21-09): «ajusta la línea del Tu día, porque se tapa
          la i; además baja un poco y junta con el título».

          Las dos cosas se midieron con la geometría real —contorno de los
          glifos de Stag LightItalic contra el trazo del `<svg>` muestreado—, no
          a ojo, y las dos tenían número:

          | glifo | ronda 2 | ronda 3 |
          |---|---|---|
          | «í» (la tilde) | **−1,9 px** — la pisa | **+20,8 px** |
          | «a» (la última) | **−2,0 px** — la pisa | **+16,3 px** |
          | «d» | +4,0 px | +27,1 px |

          ⛔ **El trazo no tapaba la i por estar mal dibujado: la palabra no
          cabía.** La tinta llegaba a x=327,6 y el canto derecho del círculo
          estaba en x=319,1 — «día» se salía por la derecha 8,5 px y la curva le
          pasaba por encima justo donde están la tilde y la «a». Por eso NO se
          arregla moviendo la palabra a la izquierda: **el círculo crece un 19 %**
          (258×130 → 306×154) y la palabra se queda EXACTAMENTE donde estaba de
          lado —tinta de x=140,5 a x=327,6, la misma de la ronda 2—, que es lo
          aprobado y lo que el QA mide contra el margen.

          ⭐ **Y el bloque baja sin mover el titular.** El canto inferior del
          trazo pasa de y=450 a **y=484**, así que el hueco contra la tinta del
          titular (y=508) cae de **57,6 px a 24 px** y las dos líneas por fin se
          leen como la frase que son —«Tu día en DoubleTree» es UNA frase
          partida en dos renglones, y venía con más aire adentro del nivel que
          entre el titular y la bajada (45,5 px).

          ⭐⭐ **Y bajar arregló de paso un contraste que venía mal medido.** El
          QA de la ronda 2 leía la banda desde x=162, o sea **se saltaba la «T»**:
          la tinta arranca en 140,5. Medida donde de verdad está, la ronda 2 daba
          **2,71:1** en el f149 —bajo la vara de 3— porque la «T» caía sobre la
          viga clara del cielo. Con el bloque 30 px más abajo entra en la parte
          del velo que ya pesa y sube a **3,35:1**. La banda del QA queda
          corregida a la tinta real (`dt-c1-s5-qa.py`).

          ⚠️ `height` + `marginBottom` sigue sumando **162**, que es lo que clava
          el titular en y=492. Lo aprobado de la ronda 2 no se mueve ni un píxel.
        */}
        {/* ⭐ RONDA 5: el `marginBottom` sube de 8 a **15**. Con el titular a
            cuerpo 80,6 la tinta nace más arriba dentro de su caja de línea y el
            hueco contra el canto del trazo se había cerrado de 28 px a 21 sin
            que nadie lo pidiera. Los 15 px devuelven EXACTAMENTE la separación
            que Eli aprobó en la ronda 3. */}
        <div style={{position: 'relative', height: 154, marginBottom: 15}}>
          {/*
            ⭐ El −12,4 es MEDIDO: el trazo no arranca en el canto del `<svg>`, así
            que a `left: 4` la tinta caía en x=103 y el bloque se leía sangrado
            respecto del titular. Ahora el canto del círculo cae en el margen
            (88) y es el círculo —no la palabra— el que alinea. La palabra va
            deliberadamente adentro, como en la referencia.

            ⚠️ El valor cambió de −11 a −12,87 con el círculo nuevo: el hueco del
            trazo escala con el `viewBox`, así que **se recalcula cada vez que se
            toca `ancho`**. No es un número que se copie.
          */}
          <div style={{position: 'absolute', left: -12.87, top: 13.69}}>
            <Circulo ancho={306} alto={154} desde={8} />
          </div>
          <div
            style={{
              position: 'absolute',
              left: 46,
              top: 54,
              fontFamily: DT.fuentes.titular,
              fontStyle: 'italic',
              fontWeight: DT.pesos.light,
              fontSize: 72,
              lineHeight: 1,
              letterSpacing: '0.012em',
              color: DT.colores.blanco,
              textShadow: SOMBRA,
            }}
          >
            Tu día
          </div>
        </div>

        <div
          style={{
            fontFamily: DT.fuentes.titular,
            fontWeight: DT.pesos.medium,
            // ⭐⭐ RONDA 5 — el cuerpo es la CONSECUENCIA de la medida.
            // «en DoubleTree by Hilton» a 108 mide 1211,2 px de tinta y la
            // columna son 904: no cabe. 80,606 es el cuerpo exacto al que la
            // tinta mide **904,00** y el renglón nace en 88 y muere en 992,
            // justo entre los dos márgenes. Ver la cabecera, § RONDA 5.
            fontSize: 80.606,
            lineHeight: 1.02,
            // ⭐ RONDA 2: venía en −0,012em. «Están muy juntas.»
            letterSpacing: '0.012em',
            color: DT.colores.blanco,
            textShadow: SOMBRA,
            // El hueco propio de la «e» a este cuerpo, medido: 1,048 px.
            ...sangria(1.05),
          }}
        >
          en DoubleTree by Hilton
        </div>

        {/* El tercer nivel: la ciudad. Conserva EXACTAMENTE la tipografía que
            tenía la bajada aprobada en la ronda 2 —Stag Light 42, +0,02em—;
            lo único que cambió es que «by Hilton» se le fue para arriba. */}
        <div
          style={{
            // ⭐ RONDA 5: de 20 a **33**. El salto ENTRE niveles tiene que ser
            // mayor que el salto DENTRO del nivel (`jerarquia-de-bloque-de-texto`):
            // con 20 el hueco caía a 29 px, el mismo que separa «Tu día» del
            // titular, y los tres renglones se leían como una sola escalera.
            // Con 33 el hueco queda en 42 px ≈ 1,5× el de arriba.
            marginTop: 33,
            fontFamily: DT.fuentes.titular,
            fontWeight: DT.pesos.light,
            fontSize: 42,
            lineHeight: 1.1,
            letterSpacing: '0.02em',
            color: DT.colores.blanco,
            textShadow: SOMBRA,
            // La «S» nace 1,30 px adentro; antes la «b» de «by» nacía en −0,55.
            ...sangria(1.3),
          }}
        >
          Santiago–Vitacura
        </div>
      </div>

      {/* La píldora — clara, como la referencia. */}
      <div
        style={{
          position: 'absolute',
          left: MARGEN,
          bottom: 200,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 26,
          height: 78,
          padding: '0 42px',
          borderRadius: 999,
          background: 'rgba(250,250,250,0.94)',
          boxShadow: '0 6px 22px rgba(9,25,78,0.22)',
        }}
      >
        <span
          style={{
            fontFamily: DT.fuentes.texto,
            fontSize: 27,
            letterSpacing: '0.22em',
            marginRight: '-0.22em',       // misma trampa del tracking que la firma
            color: DT.colores.azul,
          }}
        >
          DESLIZA
        </span>
        <Flecha tam={40} color={DT.colores.azul} />
      </div>

      {/*
        ⚠️ PENDIENTE DE ELI — LA ÚNICA LÁMINA DONDE EL NOMBRE SALE DOS VECES.
        Constanza acotó su pedido a «el resto de las slides», así que en la
        portada la versalita al pie se DEJÓ. Pero con la jerarquía nueva el
        bloque de arriba ya dice «en DoubleTree by Hilton / Santiago–Vitacura»
        y el pie repite exactamente lo mismo. La opción B —sin firma— se rinde
        con `--props='{"sinFirmaPortada":true}'` y va en la página de revisión
        para que ella elija. Si dice que sí, esto se borra y queda una línea.
      */}
      {Boolean((getInputProps() as {sinFirmaPortada?: boolean}).sinFirmaPortada)
        ? null
        : <Firma />}
      </>}
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────────────────────────────────────
// LAS LÁMINAS INTERIORES
// ───────────────────────────────────────────────────────────────────────────

type Lamina = {
  /** El clip ya preparado por `scripts/dt-c1-s5-clips.py`. */
  clip: string;
  /** Del comentario de diseño. Sin hora, el sello queda sólo con el rótulo. */
  hora?: string;
  /** El rótulo del propio brief («SLIDE 3 – TIEMPO PARA TI»). */
  rotulo: string;
  /**
   * El texto del brief, partido en gancho + remate para el recurso de DT: DOS
   * PESOS, UN MISMO CUERPO. Arriba Stag Medium, abajo Stag Light. La partición
   * es de diagramación; las palabras no se tocan.
   */
  gancho: string;
  remate: string;
  cuerpo: number;
  /**
   * El hueco del primer glifo de cada elemento, en px @1080, MEDIDO sobre el
   * render. Ver la nota de `sangria`. `dt-c1-s5-qa.py` los verifica.
   */
  sangriaSello: number;
  sangriaGancho: number;
  sangriaRemate: number;
  /**
   * Sólo para una lámina que saliera de una foto: su movimiento. Desde el
   * 21-09 **ninguna la usa** — las seis son video, incluida la del gym. Se deja
   * porque `LaminaInterior` sabe caer a foto si alguna vez falta un clip.
   */
  camara?: Movimiento;
};

/**
 * ⭐⭐ LAS LÁMINAS INTERIORES SON VIDEO DE VERDAD, NO UNA FOTO CON ZOOM.
 *
 * El brief dice «CARRUSEL DE VIDEOS» y el 17-09 Eli pasó la sesión de video que
 * grabó Scarlette el 16-09 (`SESIÓN VIDEOS › SALÓNES · DESAYUNO BUFFET QB ·
 * COWORK · HABITACIONES`). La primera versión de esta pieza resolvía el
 * movimiento con un `Ken Burns` sobre las fotos de la sesión profesional; con
 * material filmado eso ya no se justifica — **una cámara real se nota**, y un
 * zoom digital sobre una foto fija se nota más todavía.
 *
 * ⛔ Y por eso estas láminas **no llevan `camara`**: el movimiento ya está en el
 * clip. Sumarle un zoom encima es mover dos veces la misma imagen.
 *
 * Cada clip viene recortado a 4:5, tonemapeado de HLG a bt709, gradado y puesto
 * a 30 fps y a la velocidad que lo hace durar 5,0 s. Todo eso vive en
 * `scripts/dt-c1-s5-clips.py`, con la razón de cada número.
 *
 * ⚠️ La PORTADA sigue saliendo de una foto: la sesión de video **no tiene
 * exterior del hotel**, y el frontis es lo que dice de qué hotel se habla. Ahí
 * el movimiento sí es de código.
 */
const LAMINAS: Record<string, Lamina> = {
  desayuno: {
    clip: 'desayuno',
    hora: '8:30',
    rotulo: 'DESAYUNO ANTES DE LA REUNIÓN',
    gancho: 'Empieza el día',
    remate: 'con la energía correcta.',
    cuerpo: 78,
    sangriaSello: 2,
    sangriaGancho: 1,
    sangriaRemate: 3,
  },
  salon: {
    clip: 'salon',
    hora: '9:30',
    rotulo: 'REUNIÓN EN SALÓN',
    gancho: 'Un espacio a la altura',
    remate: 'de tus reuniones.',
    cuerpo: 78,
    sangriaSello: 2,
    sangriaGancho: 1,
    sangriaRemate: 3,
  },
  lobby: {
    clip: 'cowork',
    hora: '12:00',
    rotulo: 'TIEMPO PARA TI',
    gancho: 'Entre reunión y reunión,',
    remate: 'un momento para respirar.',
    cuerpo: 74,
    sangriaSello: 4,
    sangriaGancho: 1,
    sangriaRemate: 2,
  },
  /**
   * ⭐⭐ GYM — LA LÁMINA QUE FALTABA, ESCRITA POR CONTENIDO EL 21-09.
   *
   * Va ENTRE el cowork y el cierre, que es donde la pone el brief (slide 4) y
   * donde la pone el reloj: 16:00 después de las 12:00 y antes de dormir.
   *
   * ⭐ **Y es VIDEO, como sus cinco hermanas.** El 17-09 esta lámina estaba
   * armada sobre la foto `HDT_82` con movimiento de código, y quedó anotado que
   * «no hay video de gimnasio en ninguna carpeta». Era falso: `CONTENIDO HOTEL
   * 2026 › GYM` tiene 7 `.MOV` con la MISMA ficha técnica que la sesión del
   * 16-09, y se habían descartado por ser «de iPhone» — cuando los otros cinco
   * clips del carrusel son exactamente eso. Se eligió `IMG_1700`; por qué ése y
   * no los otros seis está en `scripts/dt-c1-s5-clips.py`.
   *
   * La hora la da el propio comentario de diseño: «16:00 UN RATO PARA ENTRENAR
   * EN EL GYM». El rótulo, en cambio, sale del BRIEF, que manda sobre el
   * comentario — ver la nota 4 de la cabecera.
   */
  gym: {
    clip: 'gym',
    hora: '16:00',
    rotulo: 'SIGUE CON TU RUTINA DIARIA',
    /**
     * ⭐ LA PARTICIÓN. Se corta igual que `salon`, que empieza con las mismas
     * dos palabras: el gancho se queda con «Un espacio» y su complemento, y el
     * remate arranca con la PREPOSICIÓN que cierra la frase. Las cuatro frases
     * del brief se parten así —el remate empieza en «con», «de», «un», «con»—
     * y ésta empieza en «en». Partirla en «Un espacio para / mantenerte en
     * movimiento.» deja el gancho colgando de una preposición y le da al remate
     * un verbo de arranque: rompe el patrón de las otras cuatro.
     */
    gancho: 'Un espacio para mantenerte',
    remate: 'en movimiento.',
    /**
     * ⭐⭐ **68 Y NO 74: EL CUERPO ES LA CONSECUENCIA DE LA MEDIDA.** Es el
     * criterio de DT que dictó Eli el 15-09 sobre el estático de Honors —«cada
     * línea se escala hasta una misma medida y el cuerpo es la consecuencia»— y
     * es lo que este carrusel ya venía haciendo sin decirlo: el cuerpo cambia de
     * lámina en lámina (78, 78, 74, 74) para que la línea más larga de cada una
     * caiga en la misma medida.
     *
     * Medido con fontTools sobre Stag, con el `letter-spacing` de la ronda 2 y
     * los 904 px de medida útil:
     *
     *   | lámina | línea más larga | ancho |
     *   |---|---|---|
     *   | desayuno   | «con la energía correcta.»   | 815,8 |
     *   | salón      | «Un espacio a la altura»     | 766,7 |
     *   | lobby      | «un momento para respirar.»  | 892,7 |
     *   | habitación | «El día termina como debe:»  | 883,9 |
     *   | **gym**    | «Un espacio para mantenerte» | **885,1** |
     *
     * Esta frase es la más larga del brief: a 74 el gancho mide 963 px, se pasa
     * de los 904 y Chrome lo parte en dos — el bloque se iba a TRES líneas y sus
     * cinco hermanas son de dos. A 68 entra en una y el BLOQUE queda del mismo
     * ancho que el del lobby y el del cierre, que es lo que el ojo compara al
     * deslizar. El cuerpo menor no se nota; un bloque de otro ancho sí.
     */
    cuerpo: 68,
    /**
     * ⚠️ 4 y no 2 porque el sello arranca en **«16:00»**, y el `1` de Trade
     * Gothic Bold Condensed es el glifo con más hueco propio de todo el
     * carrusel — el mismo caso del `12:00` del lobby, que también lleva 4.
     * Los sellos que empiezan en `8:30` y `9:30` llevan 2.
     */
    sangriaSello: 4,
    sangriaGancho: 1,
    // La «e» de «en movimiento.» — medida sobre el render: con 2 la tinta caía
    // en x=89 y con 3 cae en el margen exacto.
    sangriaRemate: 3,
  },
  habitacion: {
    clip: 'habitacion',
    // ⏸ SIN HORA — contenido no la entregó. Ver la nota 2 de la cabecera.
    rotulo: 'CIERRE EN LA HABITACIÓN',
    gancho: 'El día termina como debe:',
    remate: 'con comodidad.',
    cuerpo: 74,
    sangriaSello: 1,
    sangriaGancho: 1,
    sangriaRemate: 3,
  },
};


const LaminaInterior: React.FC<{clave: keyof typeof LAMINAS}> = ({clave}) => {
  const l = LAMINAS[clave];
  // ⚠️ El hook se llama SIEMPRE, aunque la lámina sea de video: las reglas de
  // los hooks no admiten llamarlo dentro de un `if`. El resultado se usa sólo
  // cuando la lámina no tiene clip.
  const camara = usaCamara(l.camara ?? {z: [1, 1], d: [[0, 0], [0, 0]]});
  const gancho = usaEntrada(26, 20);
  const remate = usaEntrada(36, 20);

  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul, overflow: 'hidden'}}>
      {l.clip ? (
        <OffthreadVideo
          src={staticFile(`assets/hilton/dt/s5/clips/${l.clip}.mp4`)}
          style={{width: '100%', height: '100%', objectFit: 'cover'}}
          muted
        />
      ) : (
        <AbsoluteFill style={{transform: camara}}>
          <Img
            src={staticFile('assets/hilton/dt/s5/gym.jpg')}
            style={{width: '100%', height: '100%', objectFit: 'cover'}}
          />
        </AbsoluteFill>
      )}

      <AbsoluteFill style={{background: rampa(VELO_INTERIOR)}} />

      {/* La tinta de la lámina. El fotograma de control la salta. */}
      {esSoloFondo() ? null : (
      <div
        style={{
          position: 'absolute',
          left: MARGEN,
          top: 128,
          width: ANCHO_UTIL,
        }}
      >
        <Sello
          hora={l.hora}
          rotulo={l.rotulo}
          desde={10}
          sangriaPx={l.sangriaSello}
        />

        <div
          style={{
            marginTop: 34,
            fontFamily: DT.fuentes.titular,
            fontSize: l.cuerpo,
            lineHeight: 1.1,
            // ⭐ RONDA 2: «añade a los textos un poco de espacio entre letras,
            // muy sutil, ya que están muy juntas». Venía en **−0,008em**, o sea
            // apretado a propósito para ganar medida. Pasa a **+0,014em**: a
            // cuerpo 74-78 son ~1 px por letra, que es lo que ella pidió — se
            // nota como aire y no como tracking.
            letterSpacing: '0.014em',
            color: DT.colores.blanco,
            textShadow: SOMBRA,
          }}
        >
          <div
            style={{
              fontWeight: DT.pesos.medium,
              ...sangria(l.sangriaGancho),
              ...gancho,
            }}
          >
            {l.gancho}
          </div>
          <div
            style={{
              fontWeight: DT.pesos.light,
              ...sangria(l.sangriaRemate),
              ...remate,
            }}
          >
            {l.remate}
          </div>
        </div>
      </div>
      )}

      {/*
        ⛔ RONDA 5 (Constanza, 22-09): «en la parte inferior donde dice "DT by
        hilton stgo - vitacura" me gustaría que se eliminara, para que no tenga
        tanto elemento por slide». La versalita al pie SALE de las cinco
        interiores. La marca sigue firmando el carrusel en la portada, que es
        además lo que pide el manual (§B: en feed el logotipo por defecto no va).
      */}
    </AbsoluteFill>
  );
};

export const DtC1S5Desayuno: React.FC = () => <LaminaInterior clave="desayuno" />;
export const DtC1S5Salon: React.FC = () => <LaminaInterior clave="salon" />;
export const DtC1S5Lobby: React.FC = () => <LaminaInterior clave="lobby" />;
/** SLIDE 4 · 16:00 · la lámina que contenido escribió el 21-09. */
export const DtC1S5Gym: React.FC = () => <LaminaInterior clave="gym" />;
/** SLIDE 5 · el cierre. Era la 4 hasta que entró el gym. */
export const DtC1S5Habitacion: React.FC = () => <LaminaInterior clave="habitacion" />;
