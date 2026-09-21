/**
 * BETWEEN — grilla SEPTIEMBRE 2026 (feed + stories) · REHECHA 27-08-2026
 *
 * Textos LITERALES del brief «BETWEEN _ GRILLA SEPTIEMBRE 2026»
 * (sheet 1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY). Solo se producen las piezas en
 * estado OK PARA DISEÑAR o CORREGIDO.
 *
 * ⛔ Esta grilla se rechazó DOS veces. Lo que cambió acá, punto por punto:
 *
 *  0. LA FUENTE. Chrome rechazaba `Brushwell.otf` y las 27 piezas salieron con
 *     una serif de reemplazo. Ahora carga el .woff2 convertido, y el kit avisa
 *     por consola si alguna cara falla. Era la causa de «cambias tipografías».
 *  1. La SCRIPT va ARRIBA, corta y en MENOR escala; la caja alta va abajo y es
 *     la protagonista. Antes la script iba abajo al doble de tamaño.
 *  2. Raleway ExtraBold (800), no Black. Titular 117, no 97.
 *  3. AIRE: 9 px de tinta entre script y titular, 18 hasta la caja. Antes se
 *     solapaban a propósito y no se leía nada.
 *  4. Todo CENTRADO — es lo que hacen las piezas aprobadas.
 *  5. En CARRUSEL el logo va SOLO en la portada. Y si la portada tiene caras,
 *     el logo baja al margen inferior.
 *  6. Multiply muy bajo: las fotos ya vienen gradadas. Cuando un texto no se
 *     lee, la solución es la CAJA TAUPE #675B49, no oscurecer la foto.
 *
 * Referencias que mandan (las marcó la diseñadora como uso correcto):
 *   raw/hilton/between-adn/ref-tipografia-ok/
 * Referencias del brief (las eligió el community manager):
 *   raw/hilton/between/refs-brief-sept/
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
import {
  FotoFondo,
  LogoBetween,
  PiezaFeedBodegon,
  PiezaStoryBetween,
  TitularBetween,
  PilaDatos,
} from './BetweenSistema';
/* ⛔ `BotonBlanco` ya no se importa: la ronda 7 eliminó la CTA «Pasa por
   Between» de `StToGoDulce`, que era la única pieza del mes que lo usaba. El
   componente se queda en `BetweenRecursos.tsx` —es el botón blanco macizo que
   definió Eli el 01-09 y sirve para cualquier CTA futura—, pero acá el import
   sobraba y `noUnusedLocals` lo marca. */
import {
  Checklist, Cuadrantes, Etiqueta, Globos, Ilustra, MarcoIGPost, StickerEnlace,
  PiezaPartida, PilaEsquina, StickerQuiz,
} from './BetweenRecursos';

/** Fotos YA GRADADAS a los números de Eli (scripts/between-gradar.py). */
const F = 'assets/hilton/between/fotos-gradadas/';
/** Montajes generados: solo lo que NO existe en el banco de fotos del cliente. */
const IA = 'assets/hilton/between/ia-sept/';
/* ⛔ `fotos-reales/` (el vaso real recortado y montado sobre la escena, ronda 5)
   ya no se usa en ninguna pieza: el montaje se leía como un vaso con pestaña y se
   volvió a la escena de la ronda 4 con el logo densificado. El archivo se deja en
   el repo porque documenta el intento y el recorte sirve para otra cosa, pero la
   constante sale para que nadie lo vuelva a enchufar sin leer
   `clients/hilton/CLAUDE.md § EL VASO TO GO`. */

const HORARIO_TOGO = 'Lunes a viernes · 08:00 a 10:00 hrs.';

/* ⭐ 01-09-2026 · JERARQUÍA DEL CARRUSEL COWORK — pedido de Eli: «los textos
   están muy grandes y desproporcionados, mejorar la jerarquía visual y el
   espacio entre textos».

   Lo que estaba mal, MEDIDO sobre la entrega (normalizado a lienzo 1080):

     | | slide 1 | slide 2 | slide 3 | referencia aprobada |
     |---|---|---|---|---|
     | titular          | 55 % | 84 % | 84 % | 52 % |
     | cuerpo real      | 117  |  99  |  88  | 117  |
     | caja taupe       | 50 % | 77 % | 84 % | 55 % |
     | alto de la caja  | 129  |  88  | 178  |  66  |

   Tres defectos encadenados:
   1. El titular se achicaba hasta CABER EN EL MARGEN (912 px = 84,4 %), por
      encima del `anchoMax: 0.8` del propio kit → toda línea larga terminaba
      clavada en el tope y el bloque se leía como un muro.
   2. Como cada slide se achicaba por su cuenta, salieron TRES cuerpos de
      titular distintos: al deslizar, el titular cambiaba de tamaño.
   3. La caja taupe compartía ese tope: la de la slide 3 medía 912 px —tocando
      los dos bordes— y partía en tres líneas, con «segundo nivel,» como
      renglón corto entre dos largos.

   El arreglo:
   - `BETWEEN.bloque.columna` (810 = 75 %) separa el MARGEN —que es un límite—
     de la MEDIDA en la que se compone.
   - `CAPS_INTERIOR`: un solo cuerpo para las slides interiores. La portada
     mantiene el titular de la marca (117) y es la única que lleva Brushwell:
     el carrusel abre fuerte y las interiores acompañan.
   - `COLUMNA_CAJA`: la caja va MÁS ANGOSTA que el titular, con los cortes
     escritos a mano. Ninguna bajada pasa de dos líneas. */

/** Cuerpo compartido por las slides interiores del Cowork.
 *  Es el mayor que deja la línea más larga del carrusel —«¿NECESITAS CAMBIAR»,
 *  10,16 px de avance por unidad de cuerpo— dentro de la columna de 810. */
const CAPS_INTERIOR = 74;
/* ⭐⭐ RONDA 8 — 79 → 76. Eli: «los títulos se ven poco alineados y desordenados».
   No era la alineación —medida, la desviación del eje es de 0,2 a 3,4 px, o sea
   invisible— era que **la slide 4 rendía a otro cuerpo que las otras dos**:

     alto de caja MEDIDO   C2 57,1   C3 57,1   C4 **53,3**

   `encoger` achica hasta CABER en la columna (810), y «NOSOTROS LLEVAMOS» a 79
   pedía ~840, así que sólo esa slide se encogía sola. Al deslizar, el titular
   cambiaba de tamaño en la última — exactamente el defecto que ya se corrigió
   una vez en «LA COLUMNA» (117 · 99 · 88) y que había vuelto por la puerta de
   atrás. A 74 la línea más larga del carrusel («NOSOTROS LLEVAMOS», 803 px de tinta) cabe sin encoger, así que las
   tres interiores rinden idénticas. */
/** La columna del titular. `PiezaFeedBodegon` sigue trayendo el MARGEN (912)
 *  por defecto para no re-flujar lo ya aprobado —comprobado: cambiar el defecto
 *  movía 3 de las 4 piezas entregadas de la S1—, así que acá se pasa a mano. */
const COLUMNA_TITULAR = BETWEEN.bloque.columna;
/** La caja taupe, más angosta que la columna del titular: así el bloque
 *  escalona (titular ancho → caja angosta) en vez de leerse como un muro. */
const COLUMNA_CAJA = 670;
/** Aire titular → caja. El medido (18) es de una caja de UNA línea bajo un
 *  titular de UNA palabra; con dos líneas arriba y dos abajo queda pegado. */
const AIRE_CAJA = 30;
/** El velo multiplicado que pidió Eli: «muy sutil». Ver `PiezaFeedBodegon.velo`.
 *  Se queda deliberadamente bajo — el manual prohíbe ganar contraste apagando
 *  la foto, y por encima de ~0,18 el problema deja de ser el velo. */
const VELO_SUTIL = 0.1;

/* ⭐⭐ RONDA 8 — el aire de la script en las interiores. Mismo defecto que en la
   portada: el salto ENTRE niveles era MENOR que el salto DENTRO del nivel.
   Medido antes: C2 y C4 dejaban ~9 px entre la línea de Raleway y la caja alta,
   contra los ~20 que separan las dos líneas del propio titular.
   0,44 × la altura de caja (≈24 px a cuerpo 76) deja el salto entre niveles por
   encima del salto interno sin abrir tanto como la portada — ahí la script es
   Brushwell y baja colas; acá es Raleway en caja alta y no tiene descendentes. */
const AIRE_SCRIPT_INTERIOR = 24;

/* ════════════════════════ FEED · 1080×1350 ════════════════════════ */

/* ─── 1 sept · CARRUSEL DINÁMICO — COWORK EN BETWEEN ───
   (la grilla pide intercambiar fecha con el de To Go: comentario C15)
   Logo SOLO en la portada. La portada tiene personas → el logo va ABAJO.     */

export const Cowork1: React.FC = () => (
  <PiezaFeedBodegon
    /* ⭐⭐ RONDA 7 (02-09, WhatsApp de Scarlette 10:37): «en cuanto a la primera,
       no la usaría por temas de calidad y porque mostramos a esas personas,
       veamos alternativas de fotos?».
       Dos objeciones distintas y las dos ciertas. `cowork-laptop.jpg` era un
       fotograma con DOS HUÉSPEDES DE CARA RECONOCIBLE sentados a la izquierda
       —derechos de imagen, y el manual ya lo marca ⛔ para esta sesión— y encima
       el encuadre venía estirado.
       → Se cambia por `IMG_1148-3`, del MISMO material y del MISMO rincón: el
         muro vegetal con el techo traslúcido y los sillones de mimbre. Es el
         fotograma de esa toma donde las dos personas YA SALIERON DE CUADRO
         (se eligió midiendo: es el más verde de los 91 fotogramas, +9,2 de
         dominancia sobre +3 del resto, o sea el que tiene el muro más lleno).
       → Se mantiene el espacio a propósito: el cliente objetó la calidad y las
         personas, NO el lugar. Cambiar de rincón habría sido responder algo que
         nadie preguntó.
       Fotograma 4K vertical (2160×3840): el 4:5 sale a 2160 px y sube 4 % para
       llegar a los 2250 de entrega, que es imperceptible. Gradada con `neutro`
       (calidez 40,4 → 20,7), el perfil que el cliente pidió en este carrusel. */
    /* ⭐⭐⭐ RONDA 8 (02-09, Eli): «Usa de fondo la terraza de between, con café
       en mesa y laptop + celular que sea estilo cowork pero mejor editada la
       foto.»
       El muro vegetal sale y entra la TERRAZA REAL: `espacios/HDT_52.jpg`,
       foto profesional de 6719×4479. Que es de Between —y no de QB, que también
       tiene terraza— quedó PROBADO mirando el archivo a resolución completa: en
       (4900,2100)-(5900,2600) hay un pizarrón que dice «BƎTWEEN / COFFEE & BAR /
       Desde las 17 hrs.», con la E quebrada del logotipo. Ver el manual §7.
       Recorte (200,900)-(3063,4479) = 2863×3579, 4:5 exacto, elegido midiendo
       contra las bandas del bloque: sombrilla oscura en la del logo, terraza en
       la libre y suelo parejo bajo el titular. El puesto de trabajo —laptop,
       taza blanca lisa y celular— se generó con Nano Banana Pro sobre esa misma
       foto (`scripts/between-portada-terraza.py`): la terraza vacía es de
       arquitectura y no hay una sola taza en las 12 tomas de la sesión.
       ⚠️ NO repite la slide 2: ésta es el PLANO GENERAL del lugar y aquélla el
       bodegón a la altura del asiento. Portada = dónde estás; slide 2 = tu mesa.
       Gradada con `neutro` (calidez 29,3 → 20,8, igual que las otras tres). */
    /* ⭐⭐ RONDA 9 (03-09) — LA TERRAZA SALE Y ENTRA EL LOUNGE. La grilla reabrió
       esta pieza (`FEED!C16`: CORREGIDO → EN CAMBIOS) y Scarlette comentó el
       mismo día: «el espacio de la slide 1 ya no existe :((( si vamos a mostrar
       de fuera tendria que ser del espacios más amplio de la terraza de
       Between». Eli resolvió por chat que la portada va del **LOUNGE**.
       Base `espacios/HDT_37.jpg` + puesto de trabajo generado sobre ella con
       `scripts/between-portada-lounge.py`. El recorte (2480,1588)+1920×2400 NO
       se eligió por composición sino POR EXCLUSIÓN: esa foto es de cuando
       servían Kimbo —hay una placa KIMBO atornillada al muro y una bolsa de café
       KIMBO sobre la barra— y además tiene una PERSONA con rostro reconocible
       tras el vidrio. De 528 encuadres 4:5 anclados abajo, sólo cuatro no tocan
       ninguna de las tres zonas. Detalle completo en el encabezado del script.
       Gradada con `neutro` (calidez 46,8 → 21,3, a tono con las otras tres). */
    foto={F + 'cowork-lounge.jpg'}
    script="Tu oficina por hoy"
    caps={'Puede ser\nBetween'}
    /* ⭐⭐⭐ RONDA 8 — LA JERARQUÍA, que es el otro medio pedido de Eli: «los
       textos deben verse mejor en jerarquía visual… ojo crítico con los
       espacios entre líneas de los textos y párrafos».
       MEDIDO sobre la entrega anterior, en px de 1080:

         script «Tu oficina por hoy»   alto 124,3   ancho 734,9  (68 %)
         ↕ 12,0                                   ← salto ENTRE niveles
         caps «PUEDE SER»              alto  84,0   ancho 600,5  (56 %)
         ↕ 29,8                                   ← salto DENTRO de un nivel
         caps «BETWEEN»                alto  83,0   ancho 542,9  (50 %)

       Dos defectos, y son los dos de jerarquía:
       1. **El salto entre niveles (12) era MENOR que el salto dentro del nivel
          (29,8).** Al revés de como se lee: las dos líneas del titular son UNA
          unidad y tienen que ir juntas, y la script es OTRO nivel y tiene que
          separarse. Encima «por hoy» baja dos colas —la «p» y la «y»— justo
          dentro de esos 12 px, así que rozaban la «PUEDE SER». Sube a 42, o sea
          la mitad de la altura de caja del titular y 1,4 × el salto interno.
       2. **La script era MÁS ANCHA (68 %) y MÁS ALTA que el titular al que
          acompaña.** El kit lo dice en su propio comentario: «va en MENOR escala
          que el titular». La proporción por defecto (1,05 × el titular) está
          calibrada para una PALABRA CLAVE; con una frase de cuatro palabras
          desborda. A cuerpo 100 la script queda en ~55 %, a la par del titular
          y sin taparlo.
       ⛔ El titular NO se toca: 117 da 84 de alto de caja y 56 % de ancho, que
          es exactamente la referencia aprobada del manual (85 y 52 %). Agrandarlo
          «para que mande» habría roto la proporción medida de la marca. */
    sizeScript={100}
    aireScriptATitulo={42}
    bajadaEnCaja
    /* ⭐ RONDA 5 (comentario C15 de FEED): «Slide1: dejar el texto consecutivo
       que esta en el cuadro café, es decir, que "pendientes" queda arriba».
       → La caja partía sola y dejaba «pendientes.» SOLA en la segunda línea —
         una viuda, que el manual prohíbe. El corte ahora es el del brief:
         «Espacio, WiFi y café.» / «Tú trae los pendientes.», cada frase en su
         línea. Va con <br /> y no con 
 porque PanelTaupe no lleva
         `white-space: pre-line` y el salto se colapsaría. */
    /* ⭐⭐ RONDA 7 (02-09, WhatsApp de Javier Meza 10:41): citó el bloque
       completo —«Espacio, WiFi y café. / Tú trae los pendientes.»— y escribió
       «este texto lo modificaria Espacio para trabajar, WiFi y atención a la
       mesa.». Es un REEMPLAZO del bloque entero, no un agregado: «Tú trae los
       pendientes.» SALE.
       El cambio no es cosmético, cambia la oferta que anuncia la portada: se va
       «café» —que no es noticia en una cafetería— y entra «atención a la mesa»,
       que es exactamente lo que remata la slide 4 («Nosotros llevamos el café»).
       El carrusel queda anunciando arriba lo que cierra abajo.
       El corte quiebra en la coma del propio cliente, que es donde él mismo
       partió la frase al escribirla. */
    bajada={<>Espacio para trabajar,<br />WiFi y atención a la mesa.</>}
    /* ⭐ 01-09, Eli: «los textos dentro del recuadro café deben verse más
       ordenados». Con la interlínea de 1,3 por defecto las dos frases quedaban
       flotando separadas dentro de la caja; a 1,16 leen como un bloque.
       ⭐⭐ RONDA 8: 1,16 → 1,24. Sigue leyendo como un bloque —está lejos del
       1,3 que ella devolvió— pero era el renglón MÁS APRETADO de la pieza y el
       pedido de hoy nombra los párrafos. Medido, de tinta a tinta:
         · dentro del titular   29,8 sobre 84,0 de caja  = 0,35
         · dentro de la caja     9,1 sobre 37,4 de caja  = 0,24  ← el que rompía
       A 1,24 la caja sube a ~0,33 y el ritmo del bloque queda parejo. Ojo que
       acá el aire importa el doble: la primera línea baja las colas de «p» y
       «j» («Espacio para trabajar,») justo sobre la tilde de «atención». */
    interlineaBajada={1.24}
    columnaCaja={COLUMNA_CAJA}
    columna={COLUMNA_TITULAR}
    aireTituloACaja={AIRE_CAJA}
    anclaje="abajo"
    conLogo
    /* ⭐ RONDA 7: el logo VUELVE ARRIBA. Estaba abajo por la regla 5 del
       encabezado —«si la portada tiene caras, el logo baja al margen inferior»—,
       y la foto nueva no tiene caras, así que la excepción ya no aplica y el
       lockup recupera su posición de marca. */
    logoPosicion="arriba"
    /* ⭐⭐ RONDA 8, Eli: «en la portada agrega debajo del logo una sombra con
       opacidad para que se vea el logo bien, muy sutil».
       La terraza trae hojas, cielo y la lona clara justo detrás del lockup. La
       banda ya medía mejor que la portada anterior (luma 123,3 contra 159,5),
       pero el fondo es PICADO —hoja clara, hueco oscuro— y eso es lo que come el
       logotipo, no el promedio. El halo asienta el lockup sin apagar la foto,
       que es lo que el manual prohíbe. 0,22 = «muy sutil». */
    logoSombra={0.22}
    oscurecer={0.1}
  />
);

export const Cowork2: React.FC = () => (
  <PiezaFeedBodegon
    /* ⭐ RONDA 6 (01-09): la foto, no el texto. Scarlette, comentario C15:
       «Slide2: y acá estamos hablando de café como tal, yo cambiaria la imagen
       donde se vea una mesa con un pc y un café». Iba el Winter Garden —el
       MISMO muro verde de la portada, sin mesa, sin PC y sin café— así que el
       carrusel además repetía fondo entre la slide 1 y la 2.
       La foto la tenía Eli hecha desde antes:
       `raw/hilton/between/ediciones-ia-eli/magnific_agrega-una-laptop-en-la-m_iAi90W63uK.png`
       — mesa de madera, laptop, vaso con el logo BETWEEN y el muro verde
       desenfocado atrás, que amarra con la portada sin repetirla.
       Recortada 4:5 con `--top 0.20` (el aire de follaje queda ARRIBA, que es
       donde se apoya el bloque de texto) y gradada con `--perfil neutro`. */
    /* ⭐⭐ RONDA 7 (02-09, WhatsApp de Scarlette 10:37): «las fotos están
       inconexas… quizás sea la de al medio que es FOTO MONTAJE que hace el
       ruido» + «cambiaría las fotos para que tenga más cohesión».
       Ésta era la del medio, y era cierto: `mesa-laptop-cafe.jpg` es un bodegón
       de ESTUDIO —macro, vapor, comida estilizada— sobre un muro verde bokeh
       INVENTADO, mientras las otras tres son interiores reales. Cuatro
       registros fotográficos en cuatro slides.
       ⛔ El diagnóstico fino: lo falso no eran los objetos, era el FONDO. Y el
          fondo inventado imitaba el muro vegetal de la portada, así que el
          carrusel repetía escenario con una copia falsa.
       → Se rehace con `scripts/between-slide2-magnific.py`: la misma escena de
         mesa + notebook + taza —que es el pedido de la ronda 6 de Scarlette,
         «una mesa con un pc y un café», y son los sustantivos del copy— pero
         con el muro vegetal REAL entrando por REFERENCIA y muy desenfocado.
         Es la receta que el cliente ya aprobó en la FEED G del 7-sep.
       → CERO personas, a propósito: el copy no las pide y «hay una mano de más»
         ya fue un rechazo en este carrusel. Una mesa servida y vacía cuenta
         «encuentra tu mesa» mejor que alguien ocupándola.
       → Taza cerámica blanca lisa, sin raya ni letras (regla KIMBO, que el
         cliente acaba de repetir) y notebook sin logotipo: la IA hace ambiente,
         nunca marca. Gradada con `neutro` (calidez 40,1 → 21,0). */
    foto={F + 'cowork-mesa-trabajo.jpg'}
    /* ⭐ 01-09, Eli: «desde el slide 2 no agregues la tipografía brushwell, que
       sea de la familia de raleway, así se diferencia de la portada». La script
       queda como marca de la PORTADA. */
    scriptSans
    script="¿Muchos pendientes?"
    aireScriptATitulo={AIRE_SCRIPT_INTERIOR}
    caps={'Al menos que sea\ncon buen café'}
    /* ⭐ 01-09 (2ª pasada): cuerpo compartido con la slide 3. Antes cada slide
       se achicaba sola y esta salía en 99 contra 88 de la otra. */
    sizeCaps={CAPS_INTERIOR}
    bajadaEnCaja
    /* El corte va escrito: sin él la caja se partía sola y dejaba «a tu ritmo.»
       colgando en la segunda línea. */
    bajada={<>Encuentra tu mesa<br />y trabaja a tu ritmo.</>}
    interlineaBajada={1.24}
    columnaCaja={COLUMNA_CAJA}
    columna={COLUMNA_TITULAR}
    aireTituloACaja={AIRE_CAJA}
    oscurecer={0.12}
  />
);

export const Cowork3: React.FC = () => (
  <PiezaFeedBodegon
    /* ⭐ RONDA 7 (02-09): la MISMA foto, regradada con `neutro`. El reclamo de
       esta ronda es la cohesión del carrusel («las fotos están inconexas… no
       tienen el mismo estilo»), y esta slide era la que se salía del tono.
       MEDIDO, calidez (R−B) de las cuatro antes:
         s1 +20,9 · s2 +21,1 · s3 **+12,4** · s4 +11,9
       La s3 venía 8 puntos más FRÍA que las dos primeras, y con la alfombra gris
       y los listones azules eso se leía como otra cámara y otro día. Regradada
       queda en **+21,1**, o sea clavada con s1 y s2.
       ⛔ La s4 NO se regradó, aunque también da +11,9: probado y descartado
          mirándolo. `neutro` le sube la luminancia de 77 a 95 y le levanta los
          negros — el tapete deja de ser negro, se pone gris lechoso y el latte
          pierde fuerza. Es la decisión ya medida del 01-09 y sigue en pie: esa
          foto cierra el carrusel como remate oscuro y su clave es lo que la hace
          buena. El cliente tampoco la objetó.
       ⚠️ Se guarda como archivo NUEVO y no se sobreescribe `segundo-nivel.jpg`:
          esa versión es la que ya se entregó en la S1 y tiene que seguir
          reproducible. */
    foto={F + 'segundo-nivel-neutro.jpg'}
    /* Sin script y sin partir la pregunta en dos pesos. Con Brushwell arriba y
       caja alta abajo la frase se leía como un solo gesto; en Raleway las dos
       líneas compiten y «¿NECESITAS CAMBIAR / DE ESCENARIO?» quedaba cortada al
       medio con el «¿» en un peso y el «?» en otro. El brief la trae como UNA
       sola frase, así que va entera en la caja alta, en dos líneas. */
    caps={'¿Necesitas cambiar\nde escenario?'}
    sizeCaps={CAPS_INTERIOR}
    bajadaEnCaja
    /* ⭐ 01-09 (2ª pasada): el corte anterior pedía una primera línea de 50
       caracteres (~885 px de tinta) que NO cabe en la caja, así que la caja la
       volvía a partir sola y quedaba «segundo nivel,» como renglón corto entre
       dos largos. Son tres líneas —el máximo que permite el manual— pero ahora
       cortadas a mano y parejas, quebrando en la coma del brief.
       ⚠️ El texto es LITERAL del brief: no se le quita el «nuestro». */
    bajada={<>También tenemos espacios<br />en nuestro segundo nivel,<br />ideales para trabajar o reunirte.</>}
    interlineaBajada={1.24}
    /* Su línea más larga —«ideales para trabajar o reunirte.», 584 px de
       tinta— pide 692 con el padding; con los 670 del resto del carrusel la
       caja la volvía a partir y aparecía un cuarto renglón de 152 px. */
    columnaCaja={740}
    columna={COLUMNA_TITULAR}
    aireTituloACaja={AIRE_CAJA}
    oscurecer={0.12}
  />
);

/* ─── SLIDE 4 · SERVICIO ───
   ⭐ REHECHA 01-09-2026. Eli la pidió de vuelta en el carrusel; la versión de la
   ronda 4 la había rechazado el cliente (comentario C15, FEED):
     «Slide 4: el "A tu mesa" le tapa la cara a la chica y parece más que están
      desayunando que trabajando. Hay una mano de más en la imagen.»

   Qué cambia respecto de esa versión:
   1. ⛔ Fuera `TituloTresPesos` + `PilaEsquina`. Esa composición era la única
      del carrusel que no usaba `PiezaFeedBodegon`, y por eso la slide 4 no se
      parecía a las otras tres. Ahora comparte gramática: script en Raleway
      arriba, caja alta abajo, caja taupe con la bajada.
   2. El bloque va ANCLADO ABAJO. En la versión rechazada el titular caía sobre
      la persona; con el ancla abajo el texto se apoya en la mesa y la regla
      dura «ningún texto sobre una cara o unos ojos» se cumple por construcción.
   3. Los tres textos son LITERALES del brief (`FEED!C11`, SLIDE 4 – SERVICIO).

   ⚠️ FALTA LA FOTO — es lo único que bloquea esta slide. Ver
      `clients/hilton/CLAUDE.md § SLIDE 4 DEL COWORK`. */
/* ⭐ RONDA 6 (01-09): las manos entregando el café. FOTO REAL, de Eli.
   Antes iba el MESÓN de servicio vacío, que contaba lo contrario del copy: un
   mesón dice que el café SE VA A BUSCAR, cuando la slide vende el servicio a la
   mesa. Pasó por una versión intermedia (`servicio-mesa.jpg`, la mesa del 2.º
   piso con el café ya servido) hasta que Eli mandó fotos propias del bar.

   La dirección de Eli fue: «una persona dejando el capuccino, que no se vea el
   rostro». Ésta la cumple con material real, sin generar nada:
   `out/hilton/between-42.jpg` — dos manos presentando la taza terminada, con el
   corazón en el latte. Se eligió sobre las otras dos (39 y 40) porque ésas son
   el momento de PREPARAR el café en la máquina; ésta es el de ENTREGARLO, que
   es lo que dice el titular.

   ⚠️ NO se gradó, y es a propósito. La foto ya venía en **calidez +8,2**, más
   fría que el objetivo del perfil `neutro` (+20): pasarla por el gradador la
   habría CALENTADO —justo lo contrario de lo que reclamó el cliente— y además
   le habría subido la luminancia de 79 a 118, lavando el ambiente oscuro que es
   lo que hace buena la foto. Sólo se recortó 4:5 y se llevó a 2250 px.

   El recorte va pegado ARRIBA, y eso también se decidió mirando: con el recorte
   abajo la taza sube y **la caja taupe le tapa el corazón del latte**. Pegado
   arriba la taza baja al ~67 % del alto, el texto se apoya en el tapete oscuro y
   el corazón queda libre.

   Es la única slide oscura del carrusel. No es un descuido: cierra la secuencia
   —el lugar, tu mesa, los espacios, el café que te llega— y el cambio de clave
   se lee como remate. */
const FOTO_SERVICIO = F + 'servicio-manos.jpg';

export const Cowork4: React.FC = () => (
  <PiezaFeedBodegon
    foto={FOTO_SERVICIO}
    scriptSans
    script="Tú sigue con lo tuyo"
    aireScriptATitulo={AIRE_SCRIPT_INTERIOR}
    /* El corte «NOSOTROS / LLEVAMOS EL CAFÉ» dejaba la primera línea en 38 %
       del lienzo y `between-qa.py` lo marcaba (mínimo 50 %). Partido después de
       «LLEVAMOS» quedan 69 % y 28 %: línea larga y remate corto, y «EL CAFÉ»
       —que es el sujeto de la promesa— cierra solo. */
    caps={'Nosotros llevamos\nel café'}
    sizeCaps={CAPS_INTERIOR}
    bajadaEnCaja
    /* El corte «…a la mesa / mientras trabajas.» no cabía en la caja y ésta lo
       volvía a partir, dejando «mesa» SOLA en un renglón. Se quiebra antes. */
    bajada={<>Disfruta nuestro servicio<br />a la mesa mientras trabajas.</>}
    interlineaBajada={1.24}
    columnaCaja={COLUMNA_CAJA}
    columna={COLUMNA_TITULAR}
    aireTituloACaja={AIRE_CAJA}
    /* ⭐ 01-09 (3ª pasada), Eli: el bloque va ARRIBA. Con la foto nueva —sólo la
       mano preparando café en primer plano— ya no hay cara que esquivar, así que
       el texto vuelve al ancla de la marca (y=180) y la slide queda alineada con
       las slides 2 y 3, que también anclan arriba. */
    /* ⭐ ARRIBA, y ahora con motivo medido. Se probaron las dos: con el ancla
       ABAJO la caja taupe cae justo encima de la taza y TAPA EL CAFÉ, que es el
       sujeto de la pieza. Arriba el texto se apoya en la sala desenfocada y la
       taza queda entera y libre. Además es el mismo ancla de las slides 2 y 3,
       así el carrusel no salta. */
    anclaje="arriba"
    oscurecer={0.12}
    /* El velo que pidió Eli: la transparencia multiplicada de Illustrator, muy
       sutil, para asentar la escena bajo el texto sin apagar la foto. */
    velo={VELO_SUTIL}
  />
);

/* ─── 3 sept · POST ESTÁTICO — CAFÉ DE CUMPLEAÑOS ───
   ⭐ RONDA 4 (27-08, comentario D15): «Haría más énfasis en el cumpleaños, puede
   ser texto principal ¿Estás de cumpleaños? luego complemento con Este café es
   para ti. Luego complemento con ¡Ven por tu café de regalo!».
   → Los tres textos son del cliente, literales, y en SU orden de lectura. El
     cumpleaños estaba enterrado en la bajada; ahora abre la pieza.
     script (arriba, Brushwell) «¿Estás de cumpleaños?» — el `¿` sale del truco
     de Eli, que voltea el signo de cierre.
     caps (protagonista) «ESTE CAFÉ ES PARA TI».
     caja taupe (el llamado) «¡Ven por tu café de regalo!».
   → EL VASO LLEVA LOGO. El montaje IA lo devolvía kraft liso y el cliente lo
     reclamó en tres piezas distintas; se estampa el logo real con
     scripts/between-logo-vaso.py sobre la misma escena ya aprobada.
   Se mantiene la dirección de arte de agosto: globos doodle de la diseñadora.  */

export const Cumple1: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    {/* ⭐⭐⭐ RONDA 8 (02-09) — el cliente, en rojo en la grilla: «La foto está
        extraña, hagamos algo más similar a lo que hicimos el primer post, algo
        más natural que no se vea tan IA, en este caso creo que MENOS ES MÁS».
        Y Eli mandó la referencia: la pieza publicada del vaso en la mano contra
        el muro vegetal con globos (Drive 12Lxot3IaQgXtT34m5q-ZeEamTqR6muRO, que
        además ya estaba en el repo en `ediciones-ia-eli/`), con un cambio
        encima: «puede ser que se vea el capuccino y no la tapa».
        ⛔ Lo que estaba mal en `cumple-manos-logo.png`: eran DOS MANOS pasándose
           el vaso. El manual ya tiene la regla —«las manos: una sola, y
           verificada con zoom»— y «hay una mano de más» fue un rechazo de este
           mismo cliente. Dos manos sin cuerpo encontrándose en el aire es
           exactamente lo que se lee como IA. «Menos es más» = una mano.
        → `scripts/between-cumple1-magnific.py`: UNA mano sosteniendo el vaso
          kraft SIN TAPA con el capuccino y su arte latte a la vista, muro
          vegetal real detrás, globos dorados y blancos y confeti.
        → El vaso se generó LISO y el logotipo se ESTAMPÓ con
          `between-logo-vaso.py --centro 1777 2670 --ancho 873` = 0,86 del ancho
          del cuerpo, que es la proporción medida en el vaso oficial. La IA nunca
          dibuja la marca. Gradada con `neutro` (calidez 32,6 → 21,1). */}
    {/* ⭐⭐⭐ RONDA 10 (04-09) — comentario nativo de Scarlette en `FEED!E15`
        (03-09 22:25): «no les gusta la propuesta :( me piden usemos la imagen
        que te adjunto acá igual hay que retocarla, cambiar el vaso al nuevo,
        sacar el plato de los vigilantes, y poderle algo que haga ref a
        cumpleaños al rededor (quizas en la mesa poner como esos papelitos de
        colores que se lanzan) y la imagen de la slide 2 tiene que tener
        relación igual con la primera.» Más la indicación de Eli: **la imagen de
        las dos slides es CONTINUA y el café va en la primera.**

        → Se acabó la escena generada. Las dos slides son ahora las dos mitades
          de UNA sola fotografía real del cliente, armada por
          `scripts/between-cumple-panorama.py` desde
          `raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-248.jpg`.

        ⭐ El hallazgo que resolvió «cambiar el vaso al nuevo» sin retocar nada:
          la foto que adjuntó Scarlette y las de esa carpeta son **la misma
          sesión, con 63 s de diferencia** (EXIF: 25-07-2025 15:45 y 15:46,
          Canon 5D III, EF50mm f/1.4, f/3,5, ISO 100). El fotógrafo hizo la mesa
          con el vaso viejo y con el nuevo: el vaso vigente ya está fotografiado
          sobre esa misma mesa y ese mismo muro. Cero IA en el producto.

        ⛔ Y por eso esta pieza YA NO comparte fondo con la G2 sin romper la
          regla 1 del manual («dentro de un carrusel no se repite el
          escenario»): no es el mismo fondo repetido, es una imagen que sigue —
          el lector desliza y la mesa continúa. Es un recurso distinto y lo pidió
          el cliente. */}
    {/* ⭐⭐⭐ RONDA 11 (04-09) — SE CAE EL PANORAMA TEJIDO.
        `cumple-continua-1/2.jpg` salían de alargar la toma espejando su flanco
        derecho hasta 4.500 px. De la G2 sólo 858 px eran reales y los otros
        2.214 eran el mismo flanco repetido: el fondo quedaba de AZULEJO
        SIMÉTRICO —follaje en mariposa cinco veces, la veta de la mesa en festón
        reflejado— y eso es lo que Eli leyó como «mal diagramada» y lo que el
        cliente lleva un mes llamando «que no se vea tan IA».
        → `scripts/between-cumple-r11.py` saca las dos slides como dos recortes
          4:5 **REALES** de la misma toma (`25-257`): la G1 en x 1830-4902 y la
          G2 en x 2688-5760. Cero espejo.
        → Y entra por fin el pedido literal de Scarlette que la ronda 10 anotó
          pero no se ve en la entrega: los **papelitos de colores** sobre la
          mesa, con tamaño por cercanía, desenfoque según la profundidad de
          campo real de la toma y sombra de contacto. Sin esas tres cosas un
          papel agregado flota.
        → Mesa sin rayones (corrector por CROMA: la madera de Between es cálida
          y las marcas son grises) y revelado por MEDIOS, que es lo que arregla
          «el color está muy oscuro». */}
    {/* ⭐⭐ RONDA 13 (04-09) — Eli: «pusiste una serpentina dorada que parece un
        plátano… Por último, que sean ILUSTRADAS, con el TRAZADO QUE YA SE SABE Y
        SE CONOCE, punto.»
        Van dos intentos de meter el adorno DENTRO de la foto —papelitos de
        colores planos, después cintas de oro metálico— y los dos se rechazaron.
        El segundo falló justamente por querer ser más realista: una cinta
        dibujada píxel a píxel se mide contra la fotografía que la rodea y pierde
        siempre.
        → El adorno de cumpleaños de esta marca YA EXISTE y es una ilustración:
          los trazos de pincel de Eli (`recursos/confeti.png`, `globos-par.png`).
          La foto vuelve a ser sólo foto y el adorno va ENCIMA, en el beige de
          marca. Un doodle no compite con la fotografía porque no pretende ser
          parte de ella. */}
    <FotoFondo src={F + 'cumple-r18-1.jpg'} oscurecer={0.08} />
    {/* ⛔ RONDA 11 — la G1 va SIN doodles, y es la misma razón que ya escribió la
        ronda 10 pero ahora sí se cumple: los papelitos de cumpleaños están
        DENTRO de la escena, sobre la mesa, que es lo que pidió el cliente.
        Dibujar además globos encima es decir dos veces lo mismo, y con el
        bloque de texto arriba y el confeti abajo la pieza se llena. Los doodles
        se quedan en la G2, donde la foto va desenfocada y no hay confeti a la
        vista.
        Medido, además: el único hueco de mesa libre que quedaba —abajo a la
        derecha, y 1180-1350— da 170 px de alto, y el par de globos pide 176.
        No cabía sin cortarlo por el canto. */}
    <Globos
      posiciones={[
        /* ⭐ RONDA 13 — vuelven los doodles a la G1, y ahora SÍ hacen falta: la
           foto ya no lleva confeti dentro. Dos trazos y en zonas medidas:
             · el par de globos sobre el muro, arriba a la izquierda, por encima
               del bloque de texto (que arranca en y=150 y ocupa x 135-945);
             · el confeti en la mesa libre de la derecha — el vaso termina en
               y=1023 y el plato no pasa de x=790, así que x 806-986 · y 1060+
               es superficie tranquila.
           Se quedan en 2: el manual pide los doodles «en poca proporción». */
        {cual: 'globosPar', x: 96, y: 470, ancho: 150, rotacion: -8},
        {cual: 'confeti', x: 806, y: 1060, ancho: 180, rotacion: 12},
        /* ⭐ RONDA 8: 872 → 856. `between-qa.py` marcó tinta a 77,8 px del canto
           derecho (mínimo 84) y NO era el texto: era este globo, cuyo trazo
           sobresale ~10 px del ancho declarado. Mismo defecto que ya se
           corrigió en la Cumple2 en la ronda 7. */
        /* ⛔ RONDA 10 — fuera el globo suelto de la derecha Y el doodle de
           confeti, por dos razones distintas:
             · el confeti, porque los papelitos ya están DENTRO de la foto, sobre
               la mesa, que es lo que pidió el cliente: dibujarlos encima era
               decir dos veces lo mismo;
             · el globo, porque ahora las dos slides son UNA imagen. Con globos
               arriba a la izquierda y a la derecha en las dos, al deslizar se ve
               cuatro veces el mismo adorno en fila y la continuidad se rompe —
               parece plantilla repetida, que es justo lo que no puede pasar.
               Los adornos se reparten a lo LARGO del par: el par de globos abre
               en el extremo izquierdo (acá) y uno solo cierra en el extremo
               derecho (en la G2). */
      ]}
    />
    {/* ⛔ SIN lockup. 01-09, Eli: «en el mismo carrusel no agregues en la portada
        el logo, ya que en el vaso está». Es la regla 8 del encabezado —cuando la
        foto trae el vaso con el logotipo impreso, la pieza no lo sobrepone— y con
        esto queda RESUELTA la decisión que estaba abierta desde el 31-08 para las
        tres piezas que la rompían. Además el carrusel ya cumple la regla 5: en
        carrusel el logo va sólo en la portada, y acá la portada no lo necesita. */}
    {/* ⭐⭐ RONDA 11 — EL BLOQUE SUBE, y es el «se ve mal diagramada» de Eli.
        Medido sobre el recorte nuevo (lienzo 1080×1350): el plato ocupa
        y 703-1167 y las medialunas y 668-949. Anclado abajo (bottom 132) el
        titular caía JUSTO encima del hojaldre, o sea sobre el producto que la
        pieza quiere vender. Arriba, en cambio, hay 400 px de muro vegetal
        oscuro y libre —el vaso no empieza hasta y=401 y el plato hasta y=703—,
        así que un bloque entre y=150 y y=380 no toca nada. Y el beige de marca
        sobre muro verde oscuro es el contraste más limpio de la pieza, sin
        tener que subir el multiply. */}
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        top: 150,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      {/* ⭐ RONDA 5 (31-08): «Slide1: Texto "¿Estás de cumpleaños en septiembre?
          Este café es para ti. ¡Ven por tu café de regalo!"». Scarlette escribió
          «en agosto»; Eli confirmó el 31-08 que va **septiembre**, que es el mes
          que arranca. Los otros dos textos ya estaban puestos desde la ronda 4.

          ⭐⭐ RONDA 7 (02-09, FEED!E15): «G1: Que diga solo ¿Estás de cumpleaños?
          sin el septiembre, eliminar ¡VEN POR TU CAFÉ DE REGALO!».
          → El cliente se DESDICE de su propia ronda 4, que había pedido los tres
            textos escalonados («luego complemento con… luego complemento con…»).
            Manda el pedido nuevo: se va el mes y se va el tercer bloque.
          → Y tiene razón de fondo: el beneficio no es de septiembre, es
            permanente —el brief dice «el mismo día de tu cumpleaños, lunes a
            viernes, en cualquier horario»—, así que acotarlo al mes lo hacía
            parecer una promo con fecha de vencimiento que no existe. Sin el mes,
            la pieza sirve todo el año.
          → La píldora que sale decía lo mismo que ya dice el titular: «este café
            es para ti» y «ven por tu café de regalo» son la misma frase dos
            veces. El «menos es más» del mismo comentario aplica también acá.
            Las condiciones (carnet, días, horario) siguen enteras en la G2, que
            es la gráfica que existe para eso. */}
      <TitularBetween
        script="¿Estás de cumpleaños?"
        caps="Este café es para ti"
        alinear="centro"
        /* ⭐ RONDA 7 — lo cazó `between-qa.py`, no el ojo: al quitarle «en
           septiembre» la script quedó CORTA, y `TitularBetween` la autoescala
           para llenar el ancho, así que creció hasta sangrar el margen —tinta a
           74 px del canto izquierdo y 72 del derecho, contra los 84 de la marca.
           Brushwell tiene remates que sobresalen de su ancho de avance (las
           colas del «¿» y del «?»), así que la caja cabía y la TINTA no.
           Se compone en la COLUMNA (810) en vez del margen (912), que es el
           opt-in que documenta `BetweenSistema.tsx`. Arregla dos cosas de una:
             · la tinta vuelve a entrar con holgura;
             · y se restaura la jerarquía de la marca. Con el texto corto a
               ancho de margen, la script medía casi lo mismo que la caja alta y
               le competía; la regla 1 del encabezado pide la script «corta y en
               MENOR escala», con el titular como protagonista.
           Re-flujar acá no rompe nada aprobado: esta pieza está en REVISAR
           CONTENIDO y se rehace completa. */
        anchoDisponible={BETWEEN.bloque.columna}
      />
    </div>
  </AbsoluteFill>
);

/**
 * Segunda pieza del carrusel: las condiciones del beneficio.
 *
 * ⭐⭐⭐ RONDA 11 (04-09-2026) — VUELVE EL MOCK DE POST DE INSTAGRAM, y vuelve
 * porque lo mandó la diseñadora: Eli dejó su editable de esta slide en el Drive
 * («te dejaré el editable del segundo slide para que lo mejores»,
 * `1kjIL3VuLnKH0ED3h8lx9kQ4GPUI5XHVF`). La ronda 5 lo había sacado por criterio
 * propio —«un post dentro de un post»— contra su diseño publicado. Manda Eli.
 *
 * ⛔ Lo que se cae con esto: el `<Checklist>` sobre panel taupe. Era una caja
 *    grande y lisa que ocupaba media pieza; el mock cuenta lo mismo y además
 *    dice DÓNDE pasa la promo, que es la gracia de la cuenta.
 *
 * Los CINCO arreglos sobre su editable —todos medidos rasterizando su `.eps` a
 * 1080×1350, no a ojo:
 *
 *  1. ⛔ **Las burbujas se salían del marco.** El marco blanco termina en x=882
 *     y las tres burbujas largas llegaban a 943: 61 px afuera. Es el defecto que
 *     la memoria `ui-mock-anti-desborde` dejó escrito con la píldora del reel de
 *     EBEMA. Ahora las cinco comparten un ancho fijo, calculado desde la ventana
 *     de la foto, y no hay forma de que sangren.
 *  2. Y de paso quedaban con **cinco cantos derechos distintos**, porque cada
 *     una se dimensionaba a su contenido. La regla del manual (§1 bis) es que
 *     una pila de cajas va toda del mismo ancho.
 *  3. ⭐ **La tercera condición se re-puntúa, y NO porque hubiera un typo.**
 *     En su archivo se lee «viernes, ien cualquier horario!» y lo primero que
 *     pensé fue que era una i latina. **No lo era, y conviene que quede
 *     escrito:** medí los contornos del `exclamdown` de Raleway y el signo está
 *     bien construido —punto arriba (y 633-717) y asta abajo (y 0-517)—, o sea
 *     que en esta familia **el «¡» tiene la misma silueta que una «i» con el
 *     asta larga**. No hay nada roto en la fuente ni en su archivo.
 *     Pero el problema de LECTURA es real: «, ¡en» se lee «, ien». La salida no
 *     es cambiar la fuente, es mover el signo al arranque de la frase, donde va
 *     seguido de mayúscula y no se confunde con nada:
 *         «¡Disponible de lunes a viernes, en cualquier horario!»
 *     Se conserva la exclamación que puso Eli y desaparece el tropiezo.
 *  4. La quinta condición era la única **sin emoji** y el cliente pidió emojis
 *     en la ronda 4 («En la G2 considerar este listado e incluir emojis
 *     nuevamente»). Lleva 🤎, que es el que ya usa el copy de la cuenta en la
 *     grilla — 💬 sale en Segoe como una mancha gris.
 *  5. El avatar del mock era «B∃TW» dibujado con letras; ahora es el logotipo
 *     real de la marca.
 *
 * El FONDO es el recorte real de la derecha de la misma toma que la G1
 * (`scripts/between-cumple-r11.py`), desenfocado: es el escenario del post y no
 * el protagonista, así que el listado —que es lo que esta gráfica comunica— se
 * lee sin pelear. Y responde el pedido de Scarlette de que «la imagen de la
 * slide 2 tenga relación igual con la primera»: misma mesa, mismo muro, misma
 * toma, sin un solo píxel espejado.
 *
 * Los textos son los CINCO de su editable, que son los del listado que adjuntó
 * el cliente. La condición del carnet va en la nota legal, como en su archivo.
 */
export const Cumple2: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={F + 'cumple-r18-2.jpg'} oscurecer={0.2} />
    <Globos
      posiciones={[
        /* Las posiciones son las del editable de Eli —el par abre por el flanco
           izquierdo a la altura del pie del mock y el globo suelto cierra por
           el derecho, más abajo— pero METIDAS DENTRO DEL MARGEN. En su archivo
           el par arranca en x=20 y el globo termina en x=1040: `between-qa.py`
           lo marcó como tinta a 11 px del canto izquierdo y a 14 del derecho,
           contra los 84 que mide el margen de sus propias plantillas. Es el
           mismo defecto que las rondas 7 y 8 ya corrigieron dos veces en estas
           dos piezas, y vale para TODA la tinta, doodles incluidos: el trazo de
           pincel sobresale ~10 px del ancho declarado, así que el par va a
           x=100 y el globo a x=860. */
        {cual: 'globosPar', x: 100, y: 645, ancho: 176, rotacion: -6},
        {cual: 'globo', x: 860, y: 872, ancho: 122, rotacion: 10, espejo: true},
        /* ⭐ RONDA 13 — un confeti en la franja libre de la derecha (el marco del
           mock termina en x=882 y el margen de marca está en 996, así que
           x 890-995 es el único hueco que queda). Cierra el par de slides con
           el mismo trazo que abre la G1. */
        /* ⚠️ x 890 + 105 = 995 entraba por 1 px, pero `between-qa.py` midió tinta
           a 79 px del canto (mínimo 84): el trazo de pincel sobresale ~6 px del
           ancho declarado, igual que ya pasó con los globos en las rondas 7 y 8.
           Se corre a 876 con 100 de ancho. */
        {cual: 'confeti', x: 876, y: 372, ancho: 100, rotacion: -14},
      ]}
    />
    {/* Sin lockup sobrepuesto: la marca la firma el avatar y el usuario del
        propio mock, y en carrusel el logo va sólo en la portada (regla 5). */}
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: 203,
        display: 'flex',
        justifyContent: 'center',
      }}
    >
      <MarcoIGPost
        usuario="between.coffeebar"
        /* ⭐ La ventana lleva la foto de la G1, NÍTIDA. Es «el post publicado»:
           el mock enseña la gráfica de la portada y las burbujas explican la
           letra chica encima. Con la misma placa desenfocada del fondo la
           ventana quedaba una mancha marrón que no decía nada, y el mock
           perdía el sentido de ser un post.

           ⛔⛔ RONDA 14 — ACÁ ESTABAN LOS «PLÁTANOS DORADOS». Esta ventana se
           quedó apuntando a `cumple-r12-1.jpg` cuando la ronda 13 cambió el
           fondo de la G1 a `cumple-r13-1.jpg`. O sea: la ronda 13 sacó las
           cintas doradas de la slide 1 y las dejó vivas DENTRO del post de la
           slide 2, que es donde Eli las vio al día siguiente.

           La regla que queda: **una foto de pieza puede estar usada en más de un
           sitio**. Cuando se cambia, hay que hacer el `grep` del nombre viejo
           antes de dar la ronda por cerrada — el mock de post enseña otra pieza
           adentro y no se actualiza solo. */
        foto={
          <Img
            src={staticFile(F + 'cumple-r18-1.jpg')}
            style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: '70% 40%'}}
          />
        }
        burbujas={[
          'Te regalamos un café para disfrutar en cafetería o To Go. ☕',
          'Accede a este regalo el mismo día de tu cumpleaños. 🎁',
          '¡Disponible de lunes a viernes, en cualquier horario! 🤩',
          '¡Elige el tamaño que quieras! 😊',
          '¡Pregúntanos por los cafés disponibles! 🤎',
        ]}
        notaLegal="*Presenta tu cédula de identidad para canjear tu café de cumpleaños. Extras y personalizaciones no incluidas."
      />
    </div>
  </AbsoluteFill>
);

/* ─── 7 sept · POST ESTÁTICO — HUMOR | CAFECITO BETWEEN ───
   ⭐ RONDA 4 (comentario F15): «Tenemos que modificar el aspecto de estas
   modelos, ya no las podemos usar tal cual».
   → La escena se rehízo con otra persona Y con el encuadre que resuelve el
     problema de raíz: de los hombros a la mesa, sin rostro. Es exactamente lo
     que hace la referencia que el propio cliente eligió para el cumpleaños
     (refs-sept-ronda4/D-feed-cumple.jpg): manos y taza, sin cara. Sin rostro no
     hay derechos de imagen que revisar, y el chiste —que es del texto— no
     pierde nada.
   Los textos NO se tocan: el cliente objetó la imagen, no el copy.

   ⭐ RONDA 6 (comentario nativo G15 de Scarlette, 31-08-2026): «siento que
   avisamos en estos contenidos que veo de las 2 tipografías de between,
   dejaría esto escrito por completo con la que es más RÍGIDA. OJO con la
   imagen igual, el espacio que se ve ahí no se parece a Between».
     · tipografía: se va Brushwell y las DOS líneas quedan en Raleway
       (`scriptSans`). «La más rígida» de las dos familias de Between es la
       sans; la script es justamente la blanda.
     · las COMILLAS: el brief escribe este texto como una CITA
       —«Perdón, esa preocupación / no cabe en mi cafecito de Between.»— y la
       pieza las había perdido, junto con el punto. Vuelven las dos cosas:
       `mantenerPunto` evita que `sinPuntoFinal` se coma el punto de la frase,
       que acá va DENTRO de la comilla y es parte de lo que se dice.
     · ⏳ el FONDO sigue pendiente: la escena actual no se parece a Between y
       hay que generarla de nuevo. Ver la nota al pie de este archivo.        */

export const HumorCafecito: React.FC = () => (
  <PiezaFeedBodegon
    /**
     * ⭐ RONDA 6 — FOTO NUEVA. La anterior (`humor-cafecito-2.png`) tenía razón
     * Scarlette: era una terraza tropical genérica —sillas de listones claros y
     * palmeras—, que es lo contrario de Between. El ambiente se transfirió por
     * REFERENCIA, no con adjetivos (la lección de Casablanca): se le pasaron las
     * fotos reales del local de `raw/hilton/between/espacios/` (HDT_50, HDT_56 y
     * HDT_38) y ahora el fondo trae lo que sí es suyo — muro de vegetación viva,
     * boiserie de madera oscura, zócalo azul navy, piso de madera oscura,
     * lámparas colgantes de latón y sillas negras de listones.
     * Se conserva la regla dura: NO se ve rostro, ni mentón, ni cuello. Y la
     * taza es blanca lisa, sin la raya ni el logotipo KIMBO — verificado.
     * Gradada con el perfil `neutro` (calidez 28,2 → 22,2), que es el que
     * responde al «se ven quemadas y con un filtro raro».
     */
    foto={IA + 'humor-cafecito-4.png'}
    script="“Perdón, esa preocupación"
    caps={'No cabe en mi\ncafecito de Between.”'}
    scriptSans
    mantenerPunto
    /* el producto —taza y croissant— quedó en el tercio INFERIOR de la foto
       nueva, así que el bloque sube: abajo el texto le caería encima. */
    /* El bloque vuelve ABAJO, como en la ronda 4: la mesa de madera ocupa el
       tercio inferior y es la única superficie tranquila de la foto. Arriba el
       texto caería sobre el muro verde, que está muy movido. */
    anclaje="abajo"
    conLogo
    columna={BETWEEN.bloque.columna}
    oscurecer={0.14}
  />
);

/* ─── 9 sept · CARRUSEL — PRIMERO LA FOTO… ¿O NO? ───
   ⭐ RONDA 4 (27-08, comentario G15): «Ok los textos, pero las fotos deben ser
   de cosas para comer y no de gente, como en la ref». La referencia que dejó el
   cliente (raw/hilton/between/refs-sept-ronda4/G-feed-fotos.jpg) es un BODEGÓN
   CENITAL de plano corto: croissant relleno + café sobre mesa de madera.
   → Los slides 1 y 2 tenían a las modelos de la sesión de agosto. Se cambian por
     comida real de la sesión de platos (3 de enero), que además resuelve el
     comentario F15: esas modelos ya no se pueden usar.
   Los textos NO se tocan: el cliente los aprobó explícitamente.
   El logo aparece UNA sola vez, en la portada; sin caras, vuelve arriba.

   ⭐ RONDA 6 (comentario nativo H15 de Scarlette, 31-08-2026): «mismo
   comentario con respecto a tipografías, acá hay una tipo más pequeña y simple
   tal como se ve en la ref (NO USEMOS LA CURSIVA) y USEMOS LAS COMILLAS».
     · las cuatro slides pasan a Raleway en las dos líneas (`scriptSans`), que
       además deja el carrusel con UN solo alfabeto, como pide la referencia.
     · vuelven las COMILLAS y la puntuación del brief. Los cuatro textos son
       citas: la comilla abre en la línea de arriba y cierra en la de abajo, y
       `mantenerPunto` conserva el punto que va dentro de la cita.
   ⭐⭐ RONDA 9 (03-09) — LAS CUATRO FOTOS, RESUELTAS. `FEED!H16` pasó a EN
   CAMBIOS y quedaban tres imágenes pendientes: slide 1 (taza KIMBO), slide 2
   («otro producto más foto aesthetic») y slide 4 («que se vea comido»).

   EL HALLAZGO, y vale para todo el mes: **las tazas de loza de Between llevan
   el logotipo KIMBO impreso al costado** — nítido en cualquier toma lateral o
   en 45°. Pero **en las CENITALES no se ve**, porque queda en la pared exterior
   de la taza. O sea que el reclamo que el cliente repite desde la ronda 4 no
   obliga a generar tazas: obliga a elegir tomas cenitales. Que es justo la otra
   mitad de su comentario («desde arriba también como los 2 anteriores») y lo
   que hace que la serie parezca «fotos que sacó una persona natural».

   Las cuatro salen ahora de la sesión profesional del propio cliente
   `3 ENERO _ PLATOS - DESAYUNOS` (Drive 16OSLgXsc_KABBHbPyBRGsG6zthRAcRaW),
   sobre su mesa de listones — con eso se cae también «el lugar no se parece en
   nada a Between»:
     · slide 1 `Between-5`   cenital, desayuno completo intacto y SIN taza en
                             cuadro. Se acabó el problema Kimbo.
     · slide 2 `Between-20`  cenital cerrado del café con arte latte. Lo más
                             «foto aesthetic» de la sesión.
     · slide 3 `Between-42`  el croissant de jamón y queso del brief. Única sin
                             cenital equivalente: se le borró la marca con
                             `scripts/between-quitar-kimbo.py` (interpolación
                             del esmalte, no clonado — el clonado dejaba un
                             rectángulo porque la taza tiene degradado lateral).
     · slide 4 `Between-179` crème brûlée cenital EDITADO para verse empezado
                             (`scripts/between-feedh-slide4.py`): costra rota,
                             dos cucharadas menos y la cuchara dentro.
   Recortes y grados en `scripts/between-feedh-fotos.py`. Las cuatro gradadas
   con `neutro` (calidez 20,9 · 20,4 · 21,1 · 21,6).                          */

export const Foto1: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'h1-desayuno-cenital.jpg'}
    script="“Qué rico se ve."
    caps={'Le voy a sacar\nuna foto.”'}
    scriptSans
    mantenerPunto
    anclaje="abajo"
    conLogo
    oscurecer={0.12}
  />
);

export const Foto2: React.FC = () => (
  <PiezaFeedBodegon
    /* cenital con latte art: es el «está demasiado lindo» del copy, y calca el
       encuadre de la referencia del cliente.
       ⭐ RONDA 9: sale `posicionFoto="42% center"`. Existía porque la foto
       anterior era APAISADA y había que correr el encuadre para que el plato y
       la taza entraran enteros en 4:5. `Between-20` ya viene recortada a 4:5
       con la taza en su eje, así que desencuadrarla la descentraba. */
    foto={F + 'h2-latte-cenital.jpg'}
    script="“Está demasiado lindo."
    caps="Foto primero.”"
    scriptSans
    mantenerPunto
    oscurecer={0.12}
  />
);

export const Foto3: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'h3-croissant-jamon.jpg'}
    /* ⭐ RONDA 7 (02-09, FEED!H15): «G3: Que pinta tiene x Se ve muy bueno...».
       La «x» es «por»: cambia la primera línea de la cita, no la segunda.
       Se respeta la puntuación de la pieza —el «…» de un solo carácter, no tres
       puntos— porque las cuatro slides son citas con el mismo sistema de
       comillas y suspensivos. El texto es más corto que el anterior (13 contra
       15 caracteres de tinta), así que no re-fluje nada. */
    script="“Se ve muy bueno…"
    caps="Esto merece foto.”"
    scriptSans
    mantenerPunto
    oscurecer={0.12}
  />
);

export const Foto4: React.FC = () => (
  <PiezaFeedBodegon
    /* ⭐ RONDA 25 (07-09) — Eli: «debe ser una torta casi en totalidad comida,
       pero que se vea lindo aún». Coincide con el comentario del cliente que
       seguía sin tachar en FEED!H15: «que se vea más vacío el plato […] desde
       arriba también como los 2 anteriores».
       ⚠️ La r24 cumplía las dos condiciones pero estaba sobre MÁRMOL BLANCO, y
       eso no se ve hasta montarla: rompía el mundo del carrusel (sus tres
       hermanas van sobre los listones oscuros) y dejaba el texto blanco casi
       ilegible. «Como los 2 anteriores» no hablaba sólo del ángulo: hablaba de
       la mesa. */
    foto={F + 'h4-torta-comida-r25.jpg'}
    script="“¡Nooo!"
    caps={'Se me olvidó\nla foto.”'}
    scriptSans
    mantenerPunto
    oscurecer={0.12}
  />
);

/* ─── 11 sept · POST ESTÁTICO — ELLA HABLÓ / ELLA ESCUCHÓ ───
   El brief pide EXACTAMENTE dos textos pequeños sobre las tazas y nada más:
   «de manera que el usuario tenga que mirar la imagen para entender el chiste».
   Meterle un titular arriba mataría el chiste, así que la pieza va limpia.    */

export const EllaHablo: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    {/* ⭐⭐ RONDA 9 (03-09) — ESCENA NUEVA. `FEED!J16` pasó a EN CAMBIOS con
        cinco defectos entre el cliente y Scarlette: las tazas «una casi arriba
        de la otra», faltaba «la interacción de las personas, aunque sea sus
        manos», el café «que se vea más lindo, algo con arte latte», el otro
        «como que en algún momento hubo café», y el platillo «enorme y
        completamente limpio».
        La escena se rehizo entera con `scripts/between-ellahablo.py`: cenital
        sobre la mesa de listones REAL del cliente (va como referencia), las dos
        tazas separadas en diagonal, arte latte nítido en la llena y cerco de
        café seco en la vacía, y una mano por taza. Las manos se revisaron al
        400 % —es el rechazo que ya tuvo esta marca— y son de mujer, porque el
        copy dice «etiqueta a esa amiga». */}
    {/* ⭐⭐ RONDA 11 (04-09) — `FEED!J15`, el único comentario SIN TACHAR de la
        celda: «Arriba ella hablo y abajo ella escuchó y queda OK».

        No es mover dos etiquetas: el chiste lo asigna el brief y es de
        contenido — «la taza casi LLENA corresponde a la amiga que pasó gran
        parte del tiempo HABLANDO; la casi VACÍA, a quien estuvo ESCUCHANDO».
        En la ronda 9 la taza llena estaba ABAJO, así que subir sólo el rótulo
        habría dejado «Ella habló» pegado a la taza vacía y el chiste al revés
        — que es el defecto que el propio cliente ya había marcado («que el de
        Ella habló esté más cerca de su respectiva taza»).

        → Para que «arriba ella habló» sea cierto, la escena se VOLTEA en
          vertical (`scripts/between-ellahablo-r11.py`). La mesa es de listones
          VERTICALES: el volteo conserva veta, herrajes y ranuras, y cada mano
          sigue entrando por su propio canto —la del asa por la derecha, la
          palma por la izquierda—, sólo a otra altura. No hay nada
          reconstruido. Ver el script para por qué NO se intercambiaron las dos
          tazas de sitio.
        → Y de paso el pedido transversal de Eli: mesa sin rayones ni motas
          (corrector sólo sobre los listones, loza y manos protegidas) y
          revelado por MEDIOS, que es lo que arregla «el color está muy
          oscuro». */}
    <FotoFondo src={F + 'j-dos-tazas-r11.jpg'} oscurecer={0.08} />
    {/* ⭐ RONDA 11 — el logo SUBE, y por el mismo motivo por el que antes bajó:
        el lockup no puede caer sobre loza blanca. Con la escena volteada la
        banda de abajo (`postLogoAbajo`, y 1173–1242, x 436–645) queda encima
        del platillo de la taza vacía, que ahora ocupa x 440–930 · y 730–1245.
        Arriba la mesa está libre; se compone en y=78 en vez del 93 de la
        plantilla para despegarse del borde del platillo de la taza llena, que
        asoma en y≈172. */}
    <LogoBetween formato="feed" posicion="arriba" tono="beige" y={78} />
    {/* ⭐ RONDA 9 — SIN CAJA, y es pedido textual del cliente: «me gustaría ver
        textos más limpios (sin el recuadro atrás)». Se puede porque la escena
        nueva deja las dos etiquetas sobre MESA OSCURA, no sobre loza blanca:
        ahí la sombra de `Etiqueta` basta y la caja taupe sobraba.
        Y van pegadas a SU taza —«que el de Ella habló esté más cerca de su
        respectiva taza»—, cada una en el hueco de mesa libre que le queda al
        lado. Medido sobre la foto gradada, en lienzo 1080×1350:
          · taza VACÍA  (arriba, derecha) centro ≈ (693, 316) → «Ella escuchó»
            a su izquierda
          · taza LLENA  (abajo, izquierda) centro ≈ (400, 870) → «Ella habló»
            a su derecha
        Siguen ESCALONADAS, que es la nota de Valeria del 29-08. */}
    {/* ⭐ RONDA 11 — posiciones re-medidas sobre la foto volteada, lienzo
        1080×1350. La taza LLENA queda arriba (platillo x 228–712 · y 172–695,
        asa x 640–730 · y 405–450) y la VACÍA abajo (platillo x 440–930 ·
        y 730–1245, con la mano del asa hasta x 1080 · y 1290):
          · «Ella habló»   → hueco de mesa a la DERECHA de la taza llena, por
            debajo del asa (a la altura del asa el platillo llega a x 730 y la
            etiqueta no cabría dentro del margen de 84).
          · «Ella escuchó» → hueco de mesa a la IZQUIERDA de la taza vacía.
        Siguen ESCALONADAS —nota de Valeria del 29-08— y ahora la diagonal va
        de arriba-derecha a abajo-izquierda. El tamaño baja de 54 a 50 porque a
        54 «Ella habló» sangraba el margen derecho: el hueco entre el platillo
        y el margen mide 266 px y la tinta a 54 pide 290. */}
    <Etiqueta x={856} y={488} size={50}>Ella habló</Etiqueta>
    <Etiqueta x={262} y={878} size={50}>Ella escuchó</Etiqueta>
  </AbsoluteFill>
);

/* ─── 14 sept · CARRUSEL — PROMOS TO GO ───
   Punto 5 del feedback, literal: «portada deja el logo, quita la transparencia
   café y centra textos, cuadro café con texto. Y en las demás slides de ese
   carrusel quitar logos, dejar una única vez en la portada principal».
   → portada: logo sí · oscurecer 0,06 (casi nada) · todo centrado · caja taupe
   → slides 2-4: sin logo                                                      */

/**
 * ⭐ RONDA 4 (comentario K15): «Me gusta que sea otra propuesta la G1, pero ella
 * se ve muy derrotada y el fondo no es muy Between, veamos opciones?».
 *   · la actitud: ahora sale sonriendo y con energía, no mirando al suelo;
 *   · el fondo: era una calle europea cualquiera. Ahora sale por la puerta de
 *     madera del local y detrás se ve el interior —madera miel, plantas y
 *     lámparas cálidas—, que es la ambientación real de Between;
 *   · y el vaso lleva el logotipo real estampado, no el liso de la IA.
 * El bloque baja al pie y el logo sube: la cara queda en el tercio alto y
 * ningún texto puede cruzarla (regla dura de la diseñadora).
 */
export const ToGo1: React.FC = () => (
  <PiezaFeedBodegon
    /* ⭐⭐ RONDA 10 (04-09). Dos pedidos que apuntan a lo mismo:
         Cliente (`FEED!L15`, sin tachar): «el fondo no tiene nada que ver con
           BT, tenemos algunos videos que hemos hecho en la entrada de BT,
           saquemos el fondo de ahí?»
         Eli: «errores del fondo con la chica… el vaso está erróneo».
       → `scripts/between-togo1-real.py` rehace la portada con material real:
         · el FONDO es `raw/hilton/between/espacios/HDT_56.jpg`, la fotografía
           del propio local —barra de mármol, mural dorado y el pasillo hacia el
           muro vegetal de la entrada—, desenfocada a la profundidad de campo de
           la escena. Es la entrada de BT que pide el cliente, y es foto suya.
         · el VASO es el REAL, recortado de `25 jul 25-248.jpg`. El generado
           tenía la tapa con una pestaña inventada y la proporción del cuerpo en
           0,79 cuando la real es 1,01. Los dedos se devuelven encima.
       ⚠️ Si aparece el metraje de la entrada que menciona el cliente, se cambia
          sólo la placa de fondo del script: el resto del montaje no depende de
          ella. */
    /* ⭐⭐ RONDA 11 (04-09) — EL REVELADO, y es la causa raíz de un reclamo que
       lleva cuatro rondas. Medido: `togo-sandwich-45.jpg` estaba gradada a
       `neutro` (calidez 20,9) y las otras tres fotos del carrusel iban CRUDAS
       —49,4 la del dulce, 40,7 la del trío, 35,1 la portada—, o sea más del
       doble del perfil del mes. De ahí que el vaso de la slide 2 se lea impreso
       y el de las 3 y 4 «descolorido»: es el MISMO vaso de la MISMA sesión, con
       y sin revelado. Es el «filtro medio raro» que Scarlette pidió sacar el
       31-08 y el «el vaso está erróneo» de Eli.
       `scripts/between-togo-r11.py` iguala las cuatro: mesa sin rayones NI
       migas (corrector de doble polaridad), revelado por medios, claridad sobre
       la comida y contraste local sobre el vaso para devolverle la tinta al
       logotipo impreso —sin re-estamparlo, que es lo que lo deformó en la
       ronda 5. */
    /* ⭐⭐⭐ RONDA 12 (04-09) — Eli: «hiciste que la chica tiene recortes se ve
       muy mal editado… recuerda que los textos están bien en el diseño, solo la
       foto de fondo estaba extraño».
       ⛔ La causa era de método: la portada era un MONTAJE, una figura recortada
          sobre un fotograma del local. Por muy pulido que quede el canto —la
          ronda 11 se lo fundió con un mapa de nitidez— un recorte y su fondo
          NUNCA comparten la luz, y eso se lee. Tres rondas de reclamos sobre
          esta pieza, siempre por lo mismo.
       → `scripts/between-togo1-r12.py`: la escena se **genera COMPLETA en una
         pasada** (Nano Banana Pro, con un fotograma del muro vegetal real como
         referencia), el vaso se pide kraft LISO y el logotipo real se estampa
         después, enmascarado al cartón para que la tinta no caiga sobre los
         dedos. No hay canto que fundir porque no hay canto.
       ⭐ Antes se agotó el material real: 75 fotogramas de los 25 clips del
         cliente son todos interiores del hotel y del cowork — no hay ni un plano
         de alguien saliendo con un vaso. La escena del brief no existe.
       ⭐ Y el encuadre está CALCULADO para el bloque aprobado: el vaso cierra en
         y=1483 y la script arranca en y≈1595, así que ya no se pisan. */
    /* ⭐⭐ RONDA 15 — foto NUEVA. Eli, por cuarta vez: «el logo del vaso sigue
       igual. Utiliza magnific». Y el problema no era el estampado: en la toma
       anterior la banda de cartón limpia entre la tapa y los dedos medía 25 px
       y el lockup de marca pide 56, así que las tres rondas previas sólo
       pudieron elegir por dónde cortarlo. Se regeneró la escena con Nano Banana
       Pro —misma mujer, mismo local, misma luz, misma diagramación— pidiendo
       sólo que tome el vaso MÁS ABAJO. Ahora hay 83 px limpios, el logotipo
       entra entero a 0,86 del ancho del vaso y queda centrado en su eje con 17
       y 16 px de aire. Ver `scripts/between-togo1-r15.py`. */
    /* ⭐⭐⭐ RONDA 23 (14-09) — LA PORTADA DEJA DE SER GENERADA.
       Scarlette: «acá hay que cambiar la portada a alguna de las que saco el
       seba». `FEED!L15` prepended el mismo día: «Ver si podemos armar una foto
       en la G1 conlas fotos sacadas por Seba».
       La ronda 12 había dejado escrito que «la escena del brief NO EXISTE» —75
       fotogramas de los 25 clips del cliente, ni un plano de alguien saliendo
       con un vaso—, y por eso las rondas 12, 15, 16 y 18 la generaron. El
       cliente mandó a grabar eso: el 09-09 Sebastián sacó 39 fotos y la escena
       existe. Ver `scripts/between-togo1-r23.py`.
       ⚠️ La portada PIERDE dos cosas del brief, informadas a Eli: no se le ve la
          cara (las 18 tomas del bloque tienen la cabeza cortada) y no hay bolsa
          To Go. */
    /* ⭐⭐ RONDA 25 (16-09) — LA PORTADA CAMBIA DE FOTO, NO DE DISEÑO.
       `FEED!L15`, prepended arriba de todo (o sea, lo más nuevo):
         «Perdón, se puso mal el enlace: es esta en la G1
          https://drive.google.com/file/d/1ZUClVyKcfy_WNcXw8eKhSxe46H7Dpv3i/view»
       El pedido de la r23 —«armar una foto en la G1 con las fotos sacadas por
       Seba»— seguía en pie, pero la foto elegida era otra: el enlace corregido
       apunta a IMG_4146, el vaso sostenido sobre la mesa de listones, y no a
       IMG_4170, la persona en la entrada que usó la r23. Verificado por md5
       contra `raw/hilton/between/vasos-togo-sep2026/IMG_4146.HEIC`.
       Eli, 16-09: «Haz el ajuste de la portada, las demás slides están okey».
       Los textos NO se tocan: los cerró ella en la r24.
       Ver `scripts/between-togo1-r25.py` — y ahí está por qué la gradación de la
       r23 NO se copia (esta toma ya viene cálida y la receta anterior le metía
       el «filtro» que el cliente mandó eliminar). */
    foto={F + 'togo-portada-r25.jpg'}
    /* ⭐⭐ RONDA 24 — LOS TEXTOS VUELVEN A COMO ESTABAN. Eli, sobre la r23:
       «Quiero los textos de la portada como estaban antes, se va a ver bien. Si
       necesitas algo puedes añadir una transparencia en opacidad o degradado».
       O sea: fuera la caja taupe del bloque (r23) y de vuelta la gramática del
       mes —script y titular en beige sobre la foto, la caja sólo en «PROMOS TO
       GO»—. El problema que la caja resolvía es real y está medido (el tercio
       inferior son pantalones crema, 1,16-1,48:1 con tinta beige), así que lo
       resuelve el DEGRADADO, que es lo que ella autorizó. */
    /* ⭐ RONDA 25 (16-09) — baja de 0,72 a 0,60. Eli: «no se ve nada, la
       portada muy oscura y quemada». Con la foto ya sin gradar, 0,72 dejaba el
       pie en L≈45 y la lámina se leía apagada. Barrido midiendo el contraste
       de la tinta beige (la marca pide 3:1) sobre script · titular · horario:
           0,72 → 5,41 · 5,54 · 4,77      0,60 → 3,27 · 4,79 · 3,95
           0,65 → 3,92 · 4,98 · 4,05      0,55 → 2,91 · 4,28 · 3,84  ⛔ script bajo
       0,60 es lo más suave que deja las tres líneas sobre el mínimo. */
    degradadoPie={0.6}
    script="¿Vas con poco tiempo?"
    /* ⭐⭐ RONDA 19 (07-09) — Eli: «los textos se ven corridos en la portada».
       Y no era el centrado: medido sobre el render, las cinco líneas caen a ±2 px
       del eje del lienzo. Lo corrido era el AIRE, con la jerarquía al revés:

           script → titular   (salto ENTRE niveles) .....  23 px
           línea 1 → línea 2  (salto DENTRO del nivel) ...  63 px

       La script quedaba PEGADA al titular mientras las dos líneas del titular
       estaban casi tres veces más separadas entre sí. Es el defecto que el manual
       ya tiene escrito —«el salto entre niveles es mayor que el salto dentro del
       nivel»— y su causa también: «¿Vas con poco tiempo?» trae descendentes (las
       dos «p» y la cola del «¿») y sus colas bajan dentro del token medido de
       9 px, que se midió sobre una script SIN descendentes.
       Con 44 el salto entre niveles sube a ~95 px contra los 63 de dentro del
       nivel: la relación 1,5× que pide la regla. */
    aireScriptATitulo={44}
    caps={'Tu desayuno\nva contigo'}
    datos={['Promos To Go', HORARIO_TOGO]}
    /* ⭐ RONDA 9 (03-09, Eli): «borra el fondo de este texto "Lunes a viernes ·
       08:00 a 10:00 hrs." ya que se ocupó en el texto de promo».
       La caja taupe es el ÉNFASIS de la pila: puesta en las dos líneas, las dos
       gritan igual y la jerarquía desaparece. Es la misma lógica que el manual
       ya tenía escrita para `PilaEsquina` («una sola línea fuerte por pila»,
       §1 bis), ahora aplicada a `PilaDatos`. Se queda la caja en «PROMOS TO GO»
       —que es la promo— y el horario acompaña sin fondo, con la sombra que usa
       `Etiqueta` cuando va suelta. La altura de la fila NO cambia, así que el
       ritmo del bloque se mantiene. */
    datosSinFondo={[1]}
    /* ⭐ RONDA 7 — defecto de margen PREVIO, que sale a la luz porque esta pieza
       se re-rinde ahora: `between-qa.py` la marcó con tinta a 77 px del canto
       izquierdo y 74 del derecho, contra los 84 de la marca. Medido: la
       infracción está en y≈806–831, o sea en la script, no en la pila de datos.
       Es el mismo defecto que `Cumple1` y `StCumple`: la cola del «¿» de
       Brushwell sobresale del ancho de avance con el que el titular se
       autoescala, así que la caja entra en el margen y la TINTA no.
       Se compone en la columna (810). */
    columna={BETWEEN.bloque.columna}
    anclaje="abajo"
    /* ⛔ RONDA 9 (03-09, Eli): «borra el logo principal ya que está en el vaso
       TO GO». Es la regla 8 del manual —EL VASO YA FIRMA: no se repite el
       logotipo— aplicada a esta portada, que es justo donde el vaso está en
       primer plano y con la marca legible. `PiezaFeedBodegon` ya trae
       `conLogo = false` por defecto por este mismo motivo («en el feed de
       bodegón la marca la pone el vaso, no un logo sobrepuesto»): lo que sale
       es la excepción que se le había puesto encima.
       ⚠️ Y no deja al carrusel sin marca: las slides 2, 3 y 4 llevan el vaso
       con el logotipo impreso. */
    oscurecer={0.06}
  />
);

export const ToGo2: React.FC = () => (
  <PiezaFeedBodegon
    /**
     * Pre-recortada a 4:5 desde la ORIGINAL (5760px): así el logo del vaso queda
     * entero con margen. El borde derecho del vaso se recorta apenas — igual que
     * en la referencia aprobada «El Match». Plato y vaso suman más ancho del que
     * cabe en 4:5, no hay recorte que muestre los dos completos.
     */
    /* ⭐⭐ RONDA 11 (04-09) — EL REVELADO, y es la causa raíz de un reclamo que
       lleva cuatro rondas. Medido: `togo-sandwich-45.jpg` estaba gradada a
       `neutro` (calidez 20,9) y las otras tres fotos del carrusel iban CRUDAS
       —49,4 la del dulce, 40,7 la del trío, 35,1 la portada—, o sea más del
       doble del perfil del mes. De ahí que el vaso de la slide 2 se lea impreso
       y el de las 3 y 4 «descolorido»: es el MISMO vaso de la MISMA sesión, con
       y sin revelado. Es el «filtro medio raro» que Scarlette pidió sacar el
       31-08 y el «el vaso está erróneo» de Eli.
       `scripts/between-togo-r11.py` iguala las cuatro: mesa sin rayones NI
       migas (corrector de doble polaridad), revelado por medios, claridad sobre
       la comida y contraste local sobre el vaso para devolverle la tinta al
       logotipo impreso —sin re-estamparlo, que es lo que lo deformó en la
       ronda 5. */
    /* ⭐⭐ RONDA 23 (14-09) — «se ven un poco OPACADAS las imagenes de las demás
       slides a comparación de los demás materiales» (Scarlette, comentario
       nativo del 14-09 10:29) + Eli: «añade un poco de color sutil… que se vea
       con vida pero sutil».
       Medido contra los materiales aprobados del mes: las tres estaban en
       mediana 123,3 contra 91,7 y croma 18,4 contra 22,1 — o sea UN TERCIO MÁS
       CLARAS y con 17 % menos de color, con el contraste ya correcto (1,03×).
       «Opacadas» era estar LAVADAS, no plana de contraste.
       ⛔ Y la trampa: realzar SUBE la calidez (29,2 → 33,9 con los parámetros
          obvios), que es devolver el «filtro medio raro» del 31-08. Por eso
          `calidez_max=8` en `scripts/between-togo-slides-r23.py`: es la
          precompensación para aterrizar en la calidez de lo aprobado.
       Resultado: mediana 101 · calidez 25,9 · croma 21,5 · 0,00 % de blanco. */
    /* ⭐ RONDA 26 (21-09) — Eli: «ajustes en todas, lo que es sándwich es más
       grande solo un poco». El sándwich con su papel crece 1,10 desde el centro
       de su apoyo (`between-togo2-r26.py`), así no despega de la mesa y al
       crecer contiene su propia silueta anterior: no hay nada que rellenar.
       ⛔ El VASO no se toca: es el patrón de escala contra el que se midieron
       las otras dos slides. */
    foto={F + 'togo-s2-r24.jpg'}
    /* ⭐ RONDA 25 (14-09) — Eli: «para esos textos en todas slides de la 2 en
       adelante crecer un poco y subir manteniendo espacios».
       La bajada sube de 40 a 44 (+10 %) y el BLOQUE ENTERO sube de y=171 a
       y=140, así que los aires internos NO se tocan —titular→bajada sigue en el
       token de 24— y lo que cambia es dónde se apoya el conjunto.
       ⚠️ `anchoBajada` va de la mano: con el cuerpo en 46 y el ancho por defecto
       (820) las bajadas de las slides 2 y 3 SE PARTÍAN EN DOS LÍNEAS mientras la
       4 —texto corto— seguía en una, y el carrusel perdía consistencia. Medido:
       la bajada más larga mide 782 px a cuerpo 40, o sea 860 a cuerpo 44; con
       880 entra en una línea y quedan 32 px hasta el margen. */
    sizeBajada={44}
    anchoBajada={880}
    topBloque={140}
    /* ⭐⭐⭐ RONDA 20 (07-09) — Eli: «recuerda guiarte del brief de lo que pide
       visualmente, los textos armónicos y jerarquía».
       Y ahí había un error de fondo que esta pieza arrastraba desde el principio:
       **la jerarquía del brief estaba INVERTIDA.** El brief de esta slide dice

           titular  CAFÉ + SÁNDWICH
           bajada   Para empezar con algo rico y contundente.
           precio   Desde $4.290

       y la pieza usaba la BAJADA partida en dos (script + caja alta) como
       titular, y metía el TITULAR del brief dentro de la barra del precio. O sea
       que lo que el brief pone primero se leía último y en cuerpo chico.
       Ahora los tres niveles son los del brief, y los tres son iguales en las
       tres slides interiores: titular en caja alta · bajada · precio en la barra.
       ⚠️ Y se va la script: la regla de Eli del 01-09 es «desde el slide 2 no
       agregues la tipografía brushwell, así se diferencia de la portada». La
       script queda como marca de la PORTADA. */
    caps="Café + Sándwich"
    bajada="Para empezar con algo rico y contundente."
    legal="*Imágenes referenciales."
    oscurecer={0.08}
  >
    {/* ⭐ Regla de la flecha (feedback 28-08): SALE del producto y APUNTA al
        texto — nunca al revés, y nunca montada sobre el producto. */}
    {/* ⭐ RONDA 5 (31-08): «sacar lo que dice "café grande"». Se va la etiqueta
        y con ella su flecha, que ya no apuntaría a nada. El «desde» que pedía la
        misma nota ya estaba puesto desde la ronda 4. */}
    <PilaEsquina
      /* ⛔ RONDA 9 · 3.ª vuelta (03-09, Eli): «estás repitiendo "Promo To Go" en
          todas, además de la portada. Bórralo: sólo tiene que aparecer en la
          portada.» El rótulo lo dice la slide 1 —que abre el carrusel—, así que
          en las interiores era ruido repetido cuatro veces. Al quedar UNA línea,
          la pila deja de ser pila: hay una sola caja, la del precio, y de paso
          se resuelve solo lo de «la caja se repite» que Eli marcó en la portada.
          `igualarAncho` se queda porque no estorba con una línea y evita tener
          que reponerlo si vuelve el rótulo. */
      /* ⭐ RONDA 26 (21-09) — CAMBIO DE CONTENIDO DEL CLIENTE, vía Scarlette
         (21-09 10:08): «Slide 2: Desde $3.490». El precio de la promo baja y se
         aplica literal: es cifra de cliente, no se redondea ni se maquilla.
         ⛔ Y no se toca nada más de esta pastilla: ni el rótulo, ni `igualarAncho`,
         ni la posición. La ronda anterior la dejó aprobada. */
      lineas={[{texto: 'Desde $3.490', fuerte: true}]}
      igualarAncho
    />
  </PiezaFeedBodegon>
);


/**
 * ⭐ RONDA 4 — corrección que NO estaba pedida, pero que el comentario K15 deja
 * al descubierto. El cliente pidió que el vaso de la slide 4 fuera «como el del
 * resto de las slides», dando por hecho que el resto estaba bien. No lo estaba:
 * esta slide traía `togo-dulce-actual.jpg`, que es el vaso ANTIGUO (cuerpo gris
 * con faja de papel), no el kraft con logo impreso. El nombre del archivo engaña
 * —dice «actual» y es el viejo—; ver clients/hilton/CLAUDE.md § EL VASO TO GO,
 * cuya tabla estaba invertida y quedó corregida el 27-08-2026.
 * Se cambia por la misma sesión con el vaso vigente, pre-recortada a 4:5 desde la
 * ORIGINAL de 5760 px (`Double Tree 25 jul 25-257`) para que el vaso entre ENTERO
 * con su logotipo: encuadrando la foto ya gradada de 2200 px, el logo quedaba
 * partido por el borde. El plato se corta por la izquierda, igual que en la
 * slide 2 y que en la referencia aprobada «El Match».
 * El brief pide «una alternativa dulce» sin nombrar producto, así que el
 * croissant azucarado cumple; la etiqueta se ajusta a lo que de verdad se ve.
 */
export const ToGo3: React.FC = () => (
  <PiezaFeedBodegon
    /* ⭐⭐ RONDA 11 (04-09) — EL REVELADO, y es la causa raíz de un reclamo que
       lleva cuatro rondas. Medido: `togo-sandwich-45.jpg` estaba gradada a
       `neutro` (calidez 20,9) y las otras tres fotos del carrusel iban CRUDAS
       —49,4 la del dulce, 40,7 la del trío, 35,1 la portada—, o sea más del
       doble del perfil del mes. De ahí que el vaso de la slide 2 se lea impreso
       y el de las 3 y 4 «descolorido»: es el MISMO vaso de la MISMA sesión, con
       y sin revelado. Es el «filtro medio raro» que Scarlette pidió sacar el
       31-08 y el «el vaso está erróneo» de Eli.
       `scripts/between-togo-r11.py` iguala las cuatro: mesa sin rayones NI
       migas (corrector de doble polaridad), revelado por medios, claridad sobre
       la comida y contraste local sobre el vaso para devolverle la tinta al
       logotipo impreso —sin re-estamparlo, que es lo que lo deformó en la
       ronda 5. */
    /* ⭐⭐ RONDA 23 (14-09) — «se ven un poco OPACADAS las imagenes de las demás
       slides a comparación de los demás materiales» (Scarlette, comentario
       nativo del 14-09 10:29) + Eli: «añade un poco de color sutil… que se vea
       con vida pero sutil».
       Medido contra los materiales aprobados del mes: las tres estaban en
       mediana 123,3 contra 91,7 y croma 18,4 contra 22,1 — o sea UN TERCIO MÁS
       CLARAS y con 17 % menos de color, con el contraste ya correcto (1,03×).
       «Opacadas» era estar LAVADAS, no plana de contraste.
       ⛔ Y la trampa: realzar SUBE la calidez (29,2 → 33,9 con los parámetros
          obvios), que es devolver el «filtro medio raro» del 31-08. Por eso
          `calidez_max=8` en `scripts/between-togo-slides-r23.py`: es la
          precompensación para aterrizar en la calidez de lo aprobado.
       Resultado: mediana 101 · calidez 25,9 · croma 21,5 · 0,00 % de blanco. */
    /* ⭐⭐⭐ RONDA 26 (21-09) — LA SLIDE DEJA DE SER UNA GENERACIÓN.
       Scarlette (21-09 10:08), comentario de contenido del cliente:
         «los productos no se ven proporcionales unos con otros, revisar los
          tamaños de los cafés y sus agregados»
         «Slide 3: … Cambiar medialuna por rollo de canela.»
       Los dos pedidos los resuelve la MISMA foto, y la foto ya existía: la
       sesión `25 jul 2025` tiene el rollo de canela con el vaso vigente sobre la
       misma mesa de listones y el mismo muro vegetal — `25-281`, vertical. Es la
       regla madre de la ronda 10 («antes de generar un producto, búscalo en la
       sesión»), y por primera vez esta slide es FOTOGRAFÍA del cliente y no una
       generación: no hay montaje, no hay logotipo estampado, no hay relight.
       ⭐ Y por eso la proporción se arregla sola: el rollo y el vaso están en la
       misma toma, así que su relación es la real y no una decisión de encuadre.
       ⭐⭐ EL PATRÓN DE ESCALA ES EL WORDMARK DEL VASO, que mide lo mismo en los
       tres tamaños de vaso (952 · 892 · 938 px en la sesión de vasos que mandó
       Eli, `raw/hilton/between/cafes-sep2026/`). Contra ese patrón, lo entregado
       medía 835 px en esta slide, 592 en la 2 y 420 en la 4: el MISMO vaso leía
       2,0× más grande en la 3 que en la 4. La ventana de `between-togo3-r26.py`
       está calculada —no elegida a ojo— para que acá aterrice en los 592 px de
       la slide 2, que es la aprobada y hace de patrón.
       ⛔ Adentro de la slide vieja la medialuna medía 0,69 del alto del vaso; en
       la fotografía real el rollo mide 1,11. El agregado se veía un 38 % más
       chico de lo que es. Eso es lo que el cliente estaba viendo.
       ⚠️ La slide 4 NO se acerca, y es decisión tomada: es el plano ABIERTO del
       carrusel y sus proporciones internas están bien (su vaso mide 1,64 de su
       wordmark, igual que el de la 2). Medido: no cabe ampliarla más de 1,08×
       sin cortar el sándwich o el vaso. */
    foto={F + 'togo-s3-r26.jpg'}
    /* ⭐ RONDA 25 (14-09) — Eli: «para esos textos en todas slides de la 2 en
       adelante crecer un poco y subir manteniendo espacios».
       La bajada sube de 40 a 44 (+10 %) y el BLOQUE ENTERO sube de y=171 a
       y=140, así que los aires internos NO se tocan —titular→bajada sigue en el
       token de 24— y lo que cambia es dónde se apoya el conjunto.
       ⚠️ `anchoBajada` va de la mano: con el cuerpo en 46 y el ancho por defecto
       (820) las bajadas de las slides 2 y 3 SE PARTÍAN EN DOS LÍNEAS mientras la
       4 —texto corto— seguía en una, y el carrusel perdía consistencia. Medido:
       la bajada más larga mide 782 px a cuerpo 40, o sea 860 a cuerpo 44; con
       880 entra en una línea y quedan 32 px hasta el margen. */
    sizeBajada={44}
    anchoBajada={880}
    topBloque={140}
    /* ⭐⭐⭐ RONDA 20 — misma corrección de jerarquía que la slide 2: el brief
       pide titular «CAFÉ + DULCE», bajada «Ese gustito que mejora cualquier
       mañana.» y precio «Desde $3.790». Sin script, que es de la portada. */
    caps="Café + Dulce"
    bajada="Ese gustito que mejora cualquier mañana."
    legal="*Imágenes referenciales."
    oscurecer={0.08}
  >
    {/* el dulce: texto ARRIBA del plato (no encima) y la flecha baja hacia él */}
    {/* ⭐ RONDA 7 — defecto de margen PREVIO que cazó `between-qa.py`: tinta a
        49 px del canto izquierdo contra los 84 de la marca, medida en y≈660–683,
        que es exactamente esta etiqueta. `Etiqueta` centra en `x`
        (`translateX(-50%)`), así que «Croissant» —182 px de tinta a size 42—
        arrancaba en 140 − 91 = 49 y sangraba 35 px.
        Se corre a x=182: la tinta arranca en 91, con 7 px de holgura sobre el
        margen. La flecha se mueve lo mismo (+42) para que siga naciendo debajo
        de su etiqueta; su punta sigue cayendo sobre el croissant, que ocupa todo
        el centro del plato. */}
    {/* ⛔ RONDA 19 — FUERA la etiqueta «Croissant» y su flecha. Sus coordenadas
        (x 182 · y 648, flecha en x 214 · y 706) estaban MEDIDAS sobre la foto
        anterior, y esta slide tiene foto nueva: la flecha apuntaría a un sitio
        donde ya no hay croissant. El manual es explícito en que estas etiquetas
        NO son obligatorias (§«las etiquetas con flecha no son obligatorias»), y
        Eli pidió en esta ronda que los rótulos dejen de estar mal puestos. Una
        etiqueta cuya posición no se puede verificar contra la foto no se
        conserva: se saca. */}
    {/* ⭐ RONDA 5 (31-08): «Debe decir "desde $3.790". Sacar lo que dice café
        grande.» El «desde» ya venía de la ronda 4; se va la etiqueta del café y
        su flecha. La del croissant se queda: nadie la objetó. */}
    <PilaEsquina
      /* ⛔ RONDA 9 · 3.ª vuelta (03-09, Eli): «estás repitiendo "Promo To Go" en
          todas, además de la portada. Bórralo: sólo tiene que aparecer en la
          portada.» El rótulo lo dice la slide 1 —que abre el carrusel—, así que
          en las interiores era ruido repetido cuatro veces. Al quedar UNA línea,
          la pila deja de ser pila: hay una sola caja, la del precio, y de paso
          se resuelve solo lo de «la caja se repite» que Eli marcó en la portada.
          `igualarAncho` se queda porque no estorba con una línea y evita tener
          que reponerlo si vuelve el rótulo. */
      /* ⭐ RONDA 26 (21-09) — CAMBIO DE CONTENIDO DEL CLIENTE, vía Scarlette
         (21-09 10:08): «Slide 3: Desde $2.990». El precio de la promo baja y se
         aplica literal: es cifra de cliente, no se redondea ni se maquilla.
         ⛔ Y no se toca nada más de esta pastilla: ni el rótulo, ni `igualarAncho`,
         ni la posición. La ronda anterior la dejó aprobada. */
      lineas={[{texto: 'Desde $2.990', fuerte: true}]}
      igualarAncho
    />
  </PiezaFeedBodegon>
);


/**
 * ⭐ RONDA 4 (comentario K15). Tres cosas en una sola slide:
 *   1. «debemos poner un dulce y un salado en la foto» — la promo es «Café +
 *      Salado + Dulce» y la foto anterior solo mostraba croissants dulces.
 *      Ninguna foto del banco trae los tres juntos, y las que se acercan son
 *      apaisadas: no dan un 4:5 con los tres. Se construyó el bodegón.
 *   2. «que el vaso sea como el del resto de las slides» — la foto anterior
 *      traía el OTRO vaso, el gris oscuro (clients/hilton/CLAUDE.md § EL VASO
 *      TO GO). Ahora es el kraft con tapa negra, y con el logotipo REAL
 *      estampado encima (scripts/between-logo-vaso.py), no el que inventa la IA.
 *   3. «en lugar de llévalo contigo, pongamos algo que haga más sentido con lo
 *      que se está mostrando, podría ser ¡Llévate los 3!» — literal del cliente.
 * La comida ocupa la mitad inferior, así que el bloque de texto sube: misma
 * decisión que ya se tomó en ToGo1 para no cruzar la cara de la modelo.
 */
export const ToGo4: React.FC = () => (
  <PiezaFeedBodegon
    /* ⭐⭐ RONDA 10 (04-09) — Eli: «la slide 4 de ese mismo carrusel, mejora la
       foto y el vaso». La escena generada se cae completa y entra un bodegón de
       FOTOGRAFÍA REAL del cliente, armado por `scripts/between-togo4-bodegon.py`
       desde la sesión 25-jul-2025: café (el vaso vigente con el logotipo
       IMPRESO), salado (croissant de jamón queso) y dulce (muffin de chocolate
       en su plato), todo sobre la misma mesa de listones y el mismo muro
       vegetal, con la misma luz y el mismo 50 mm.
       ⛔ El vaso generado tenía la proporción mal —cuerpo 0,79 de ancho/alto
       cuando el real mide 1,01—, una tapa con pestaña inventada y el logotipo
       plano como calcomanía. Es el reclamo que el cliente repite desde la
       ronda 4, y con foto real se termina. */
    /* ⭐⭐ RONDA 11 (04-09) — EL REVELADO, y es la causa raíz de un reclamo que
       lleva cuatro rondas. Medido: `togo-sandwich-45.jpg` estaba gradada a
       `neutro` (calidez 20,9) y las otras tres fotos del carrusel iban CRUDAS
       —49,4 la del dulce, 40,7 la del trío, 35,1 la portada—, o sea más del
       doble del perfil del mes. De ahí que el vaso de la slide 2 se lea impreso
       y el de las 3 y 4 «descolorido»: es el MISMO vaso de la MISMA sesión, con
       y sin revelado. Es el «filtro medio raro» que Scarlette pidió sacar el
       31-08 y el «el vaso está erróneo» de Eli.
       `scripts/between-togo-r11.py` iguala las cuatro: mesa sin rayones NI
       migas (corrector de doble polaridad), revelado por medios, claridad sobre
       la comida y contraste local sobre el vaso para devolverle la tinta al
       logotipo impreso —sin re-estamparlo, que es lo que lo deformó en la
       ronda 5. */
    /* ⭐⭐⭐ RONDA 12 (04-09) — Eli: «se ve quemada y mal. Vuelve a hacer ese
       diseño: Los tres productos juntos en formato To Go: café, alternativa
       salada y dulce. Una mano tomando la bolsa o el café refuerza la idea de
       llevar.»
       ⛔ Y el defecto de fondo no era el revelado: la pieza mostraba croissant y
          muffin en PLATOS DE CERÁMICA sobre la mesa —eso es consumo en local, no
          «formato To Go»— y no había ninguna mano, que es la mitad de la
          indicación del brief.
       → `scripts/between-togo4-r12.py`. La base es un editable de ELI
         (`ediciones-ia-eli/magnific_haz-que-la-tapa-de-la-img_YVjNsSNWeC.png`):
         bolsa kraft con el logotipo impreso, vaso To Go con el suyo, sándwich
         sobre el papel y la mano en el asa. Le faltaba sólo el dulce, así que se
         editó SU imagen —no se generó de cero— para agregar el muffin y para
         bajar los productos a la mitad inferior, porque la mano y el asa
         llegaban al tercio superior y ahí va este titular. */
    /* ⭐⭐ RONDA 23 (14-09) — «se ven un poco OPACADAS las imagenes de las demás
       slides a comparación de los demás materiales» (Scarlette, comentario
       nativo del 14-09 10:29) + Eli: «añade un poco de color sutil… que se vea
       con vida pero sutil».
       Medido contra los materiales aprobados del mes: las tres estaban en
       mediana 123,3 contra 91,7 y croma 18,4 contra 22,1 — o sea UN TERCIO MÁS
       CLARAS y con 17 % menos de color, con el contraste ya correcto (1,03×).
       «Opacadas» era estar LAVADAS, no plana de contraste.
       ⛔ Y la trampa: realzar SUBE la calidez (29,2 → 33,9 con los parámetros
          obvios), que es devolver el «filtro medio raro» del 31-08. Por eso
          `calidez_max=8` en `scripts/between-togo-slides-r23.py`: es la
          precompensación para aterrizar en la calidez de lo aprobado.
       Resultado: mediana 101 · calidez 25,9 · croma 21,5 · 0,00 % de blanco. */
    /* ⭐⭐ RONDA 26 (21-09) — EL CAFÉ CRECE. Eli: «el ajuste de proporción de
       tamaño es de café y productos, sobre todo de la última slide».
       Medido con el logotipo del vaso de patrón —que mide lo mismo en los tres
       tamaños de vaso—, media unidad de sándwich medía **2,64 anchos de
       logotipo** acá contra **1,41** en la slide 2, que es la aprobada y sale de
       una fotografía real. O sea que el sándwich leía 1,87× de lo que le toca al
       lado de su café: la comida entre sí estaba bien (muffin contra sándwich
       0,53, y lo real es 0,50) y **el vaso era el chico**.
       `between-togo4-r26.py` lo escala 1,30× desde el CENTRO DE SU BASE, así no
       despega de la mesa, y le devuelve el plato del muffin por delante porque
       está más cerca de la cámara. El logotipo pasa de 341 a 443 px y el
       carrusel entero cae en una banda de 1,25× (554 · 476 · 443) donde estaba
       en 2,29×.
       ⚠️ No llega a 1,87× y es por el cuadro: a esa escala la tapa se sale por
       la derecha y la base se le monta al plato. Lo que falta para cerrar la
       cuenta es achicar el sándwich, y eso queda propuesto, no hecho.
       ⛔ No se movió nada más de esta slide: ni bolsa, ni mano, ni muffin, ni
       sándwich, ni encuadre, ni revelado. */
    /* ⛔ RONDA 29 (21-09) — LA FOTO APROBADA, SIN NINGÚN RETOQUE.
       Eli, sobre la r28: «vuelve a la foto anterior a esta». Medido sobre su
       pantallazo, el logotipo del vaso daba 365 px —o sea la versión con el
       café a 1,10—, así que la anterior es la fotografía aprobada tal cual.
       Esta slide vuelve a ser exactamente la que el cliente aprobó el 07-09 y
       lo único que cambia respecto de lo entregado es el PRECIO.
       ⭐ El registro de los tres intentos queda en el repo, porque es de donde
       salió la regla: `between-togo4-r26.py` (escalar tres objetos → 888 k px
       tocados, logotipo duplicado), `-r27-generar.py` (regenerar la escena →
       limpia, pero el sándwich dejaba de ser el de la marca) y `-r28.py`
       (escalar sólo el vaso, con compuerta → limpio, pero movía el pliegue de
       la bolsa hasta que la parcha dejó de llevar fondo).
       ⛔ La conclusión, y vale para toda la cuenta: **una fotografía aprobada
       no se retoca para arreglar una proporción.** Si la proporción está mal,
       se pide otra foto. */
    foto={F + 'togo-s4-r24.jpg'}
    /* ⭐ RONDA 25 (14-09) — Eli: «para esos textos en todas slides de la 2 en
       adelante crecer un poco y subir manteniendo espacios».
       La bajada sube de 40 a 44 (+10 %) y el BLOQUE ENTERO sube de y=171 a
       y=140, así que los aires internos NO se tocan —titular→bajada sigue en el
       token de 24— y lo que cambia es dónde se apoya el conjunto.
       ⚠️ `anchoBajada` va de la mano: con el cuerpo en 46 y el ancho por defecto
       (820) las bajadas de las slides 2 y 3 SE PARTÍAN EN DOS LÍNEAS mientras la
       4 —texto corto— seguía en una, y el carrusel perdía consistencia. Medido:
       la bajada más larga mide 782 px a cuerpo 40, o sea 860 a cuerpo 44; con
       880 entra en una línea y quedan 32 px hasta el margen. */
    sizeBajada={44}
    anchoBajada={880}
    topBloque={140}
    /* ⭐⭐⭐ RONDA 20 — el brief pone «¿POR QUÉ ELEGIR UNO?» como TITULAR y esta
       pieza lo tenía en la script, con «¡Llévate los 3!» de titular. Se invierte
       para que la slide de cierre siga la misma jerarquía que sus hermanas.
       ⚠️ «¡Llévate los 3!» se conserva y NO se cambia por el «Llévalo contigo.»
       del brief: esa línea la reemplazó el cliente (Scarlette, ronda 4 — «en
       lugar de llévalo contigo, pongamos algo que haga más sentido con lo que se
       está mostrando, podría ser ¡Llévate los 3!») y está aplicada y tachada en
       la grilla. La corrección del cliente manda sobre un brief que nunca se
       actualizó. Queda dicho acá para que nadie lo «arregle» de vuelta.
       Y la barra de esta slide conserva las dos líneas del brief («Café + salado
       + dulce» y «Desde $5.290») porque es la que resume el carrusel. */
    caps="¿Por qué elegir uno?"
    /* ⚠️ La bajada es la línea DESCRIPTIVA del brief («Café + salado + dulce»),
       no el llamado. Con «¡Llévate los 3!» de bajada la slide quedaba con tres
       palabras en cuerpo de bajada donde sus hermanas llevan una frase entera:
       se leía tímida y rompía la armonía del carrusel. El llamado del cliente se
       va a la BARRA, que es el sitio fuerte, y ahí queda paralela a las otras
       («Desde $4.290» · «Desde $3.790» · «¡Llévate los 3! desde $5.290»). */
    bajada="Café + salado + dulce"
    /* ⭐ RONDA 7 — mismo defecto previo de margen que `ToGo1`: tinta a 74 px del
       canto izquierdo, medida en y≈244–270, que es la banda de la script («¿Por
       qué elegir uno?», otra que abre con «¿»). Se compone en la columna. */
    columna={BETWEEN.bloque.columna}
    anclaje="arriba"
    legal="*Imágenes referenciales."
    oscurecer={0.1}
  >
    {/* ⭐ RONDA 5 (31-08): «La información de la promo esta mala deberia quedar
        como esta en la slide 1 y 2.» Iba en `datos` —una sola línea pegada bajo
        el titular— mientras las otras slides usan la pila taupe de dos cajas
        abajo a la izquierda. Se unifica con ToGo2 y ToGo3.
        ⚠️ NO verificado en render: esta máquina no tiene las 22 fotos que faltan.
        PilaEsquina se ancla sola abajo-izquierda y no depende de `anclaje`, pero
        hay que mirar que no choque con la etiqueta «Dulce» (x 716, y 1150). */}
    <PilaEsquina
      /* ⛔ RONDA 9 · 3.ª vuelta (03-09, Eli): «estás repitiendo "Promo To Go" en
          todas, además de la portada. Bórralo: sólo tiene que aparecer en la
          portada.» El rótulo lo dice la slide 1 —que abre el carrusel—, así que
          en las interiores era ruido repetido cuatro veces. Al quedar UNA línea,
          la pila deja de ser pila: hay una sola caja, la del precio, y de paso
          se resuelve solo lo de «la caja se repite» que Eli marcó en la portada.
          `igualarAncho` se queda porque no estorba con una línea y evita tener
          que reponerlo si vuelve el rótulo. */
      lineas={[
      /* ⭐ RONDA 26 (21-09) — CAMBIO DE CONTENIDO DEL CLIENTE, vía Scarlette
         (21-09 10:08): «Slide 4: Desde $4.490». El precio de la promo baja y se
         aplica literal: es cifra de cliente, no se redondea ni se maquilla.
         ⛔ Y no se toca nada más de esta pastilla: ni el rótulo, ni `igualarAncho`,
         ni la posición. La ronda anterior la dejó aprobada. */
        {texto: '¡Llévate los 3! desde $4.490', fuerte: true},
      ]}
      igualarAncho
    />
    {/* ⛔ RONDA 10 · 2.ª pasada — FUERA las etiquetas «Salado» y «Dulce» con sus
        flechas de bucle. Eli: «se ve mal diagramada».
        Medido sobre el bodegón nuevo no hay dónde ponerlas sin apretar la pieza:
        el titular baja hasta y=463, el croissant empieza en y=540 —77 px de
        hueco, que no dan para etiqueta más flecha— y el único hueco de mesa
        libre (a la derecha, bajo el vaso) queda tan lejos del producto que la
        flecha ya no conectaría nada.
        Y de fondo: la etiqueta con flecha es el recurso de la marca para NOMBRAR
        un producto cuando hace falta —la slide 3 tiene una sola cosa en cuadro y
        ahí sí—; acá la caja de la promo ya dice «Café + Salado + Dulce» y la
        foto muestra exactamente esos tres. Repetirlo con dos etiquetas era ruido
        sobre una foto que ya está llena. */}
  </PiezaFeedBodegon>
);


/* ════════════════════════ STORIES · 1080×1920 ════════════════════════ */

/* ─── 1 sept · PROMO TO GO | CAFÉ + DULCE ───
   Composición PARTIDA en dos fotos con la script cruzando la costura: es el
   recurso del post «Good Morning» de la marca. Rompe el «titular arriba, foto
   abajo» sin salirse de la línea gráfica.
   ⭐ RONDA 4 (comentario C15 de STORIES): «Café con logo Between!».
   ⭐⭐ RONDA 5 (01-09): el logotipo estampado sobre un vaso generado nunca
   convenció. Las DOS mitades pasan a ser **fotografía real de la sesión del
   cliente**, así que el logo del vaso ya no se pega: viene impreso en el vaso.
     · arriba  `Double Tree 25 jul 25-255` — el vaso vigente (cuerpo crema,
       logotipo impreso directo, tapa negra plana)
     · abajo   `Double Tree 25 jul 25-281` — el rol de canela real
   Misma sesión, misma mesa y mismo muro verde: las dos mitades casan solas.
   El recorte de abajo deja aire libre para que la caja de la promo **no tape el
   rol**, que es el otro comentario del cliente.                               */
export const StToGoDulce: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <PiezaPartida
      eje="horizontal"
      izquierda={F + 'togo-vaso-foto.jpg'}
      derecha={F + 'rol-canela.jpg'}
    />
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra, opacity: 0.14}} />
    {/* ⛔ SIN lockup. Regla 8: cuando la foto trae el vaso con el logotipo
        impreso, la pieza NO lo sobrepone — se lee dos veces la misma marca.
        Con el vaso real la marca ya está en la foto, y el lockup quedaba
        justo encima del impreso, uno debajo del otro. Esta pieza era una de
        las tres que la auditoría del 31-08 marcó por esto. */}
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        top: 820,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <TitularBetween script="Un dulce comienzo" caps="para tu mañana" alinear="centro" />
      {/* ⭐ RONDA 5 (01-09): la CTA salía LITERAL del brief, celda C10 de la hoja
          STORIES —«CTA: Pasa por Between y llévalo contigo.»— partida en dos por
          pedido de Eli: la orden dentro del botón blanco y el cierre debajo.

          ⛔ RONDA 7 (02-09, STORIES!D15): «Eliminar PASA POR BETWEEN y llévalo
          contigo». Se van las DOS partes: el botón y su cierre. El cliente
          borra su propia CTA del brief, y es su derecho — es la única CTA del
          mes que mandaba salir del local cuando la promo justamente es To Go,
          o sea que ya se la llevan puesta. Sin ella la pieza queda en titular +
          promo, que es lo que el mismo comentario aprueba: «Con eso ok!».

          ⚠️ Con esto la story pierde su único elemento blanco macizo, que era la
          decisión de arte de Eli del 01-09. No se sustituye por otro botón: el
          cliente no pidió reemplazo, pidió eliminación. Si Eli quiere devolver
          el blanco a la pieza, es decisión suya y va sobre otro elemento. */}
    </div>
    {/* El confeti se corre al hueco de mesa que queda entre el plato y el vaso:
        estaba encima de la media luna y un doodle sobre el producto se ve
        descuidado. */}
    <Ilustra cual="confeti" x={470} y={118} ancho={140} rotacion={-22} opacidad={0.8} />
    <Ilustra cual="corazon" x={898} y={1180} ancho={92} opacidad={0.9} />
    {/* ⭐ RONDA 7 (02-09, STORIES!D15): «Que diga Café + Dulce To Go - desde».
        Entra el «To Go», que es el nombre real de la promo en la carta y lo que
        la story vende; el «desde» ya venía de la ronda 4.

        ⛔ Y VUELVE A SER UNA SOLA LÍNEA FUERTE. Estuvo partida en dos cajas
        —«Café + Dulce To Go» / «desde $3.790»— para que ninguna cruzara el rol
        de canela, y el remedio fue peor: quedaron TRES cajas de tres anchos
        distintos, y las dos primeras en el MISMO peso, así que la pila perdió
        jerarquía y se leía en escalera. Eli lo marcó: «se ve todo desordenado en
        los textos y no se ve pulcro… cuidado que los textos se vean bien igual
        en jerarquía».
        → Dos cajas y una sola jerarquía: la promo entera en la línea fuerte y el
          horario en la liviana, que es el patrón de las otras tres slides del
          carrusel.
        → El ancho se resuelve con `igualarAncho`, no partiendo el texto: las dos
          cajas quedan del mismo ancho y el bloque tiene UN borde derecho.

        El separador «·» se mantiene —y no el guion que escribió el cliente—
        porque toda la pila de promos del mes usa el punto medio (ToGo2, ToGo3 y
        ToGo4) y un guion solo en esta pieza rompería la serie. */}
    <PilaEsquina
      lineas={[
        {texto: 'Café + Dulce To Go · desde $3.790', fuerte: true},
        {texto: 'Lunes a viernes · 08:00 a 10:00 hrs'},
      ]}
      igualarAncho
      abajo={430}
    />
  </AbsoluteFill>
);

/* ─── 3 sept · CAFÉ DE REGALO POR TU CUMPLEAÑOS ───
   ⭐ RONDA 4 (comentario D15 de STORIES): «Tomemos mismos textos de la
   publicación de feed, manteniendo imagen de fondo de esta propuesta, pero que
   el vaso tenga logo».
   → Los tres textos son ahora IDÉNTICOS a los del post del feed (Cumple1): el
     cliente quiere una sola voz entre feed y story el mismo día.
   → Se conserva la escena aprobada (vaso con vela sobre la mesa) y se le
     estampa el logo real: `cumple-vela-logo.png`.
   Los dos textos que estaban tachados en la grilla ya estaban resueltos —la
   fecha se cambió por la interactiva de emergencia y «cafeína» salió del copy—,
   así que acá solo se aplica lo que sigue vigente.                             */
export const StCumple: React.FC = () => (
  <PiezaStoryBetween
    /* ⭐⭐⭐ 01-09-2026 — EL VASO, resuelto por fin, y NO por montaje.
       Eli: «mejora el vaso togo». El montaje del 31-08 —el vaso real recortado
       del frame 255 pegado sobre esta escena— es lo que se veía «extraño y
       doblado»: el vaso que la escena YA traía es más ancho abajo y asomaba por
       el costado, y taparlo obligaba a inventar fondo.
       → Se volvió a la escena de la RONDA 4 (`git show e699338`), cuyo cartón
         está LIMPIO: sin el velo rectangular que dejó el re-sellado de la ronda
         5. Sobre ese cartón limpio sólo se le subió la carga de tinta al logo
         —de 0,59 a la densidad de una serigrafía— con
         `scripts/between-logo-densidad.py`. Geometría intacta: el logotipo no se
         reescaló, no se movió y no se deformó.
       ⛔ Por qué no se usa el vaso real: del vaso VIGENTE no existe ninguna toma
         frontal y aislada en alta resolución. El único recorte grande sale del
         frame 255, donde está inclinado, y esta escena es frontal. Endererzarlo
         sería deformar el logotipo. Los packshots frontales 336–339 son del vaso
         ANTIGUO (cuerpo negro con faja kraft). */
    foto={IA + 'cumple-vela-logo.png'}
    /* La story arrastra el mismo titular del feed —«mismos textos de la
       publicación de feed» (D15)—, así que TODO cambio del feed baja acá.

       ⭐⭐ RONDA 7 (02-09): el comentario nuevo está escrito en FEED!E15 y habla
       de la G1 del feed, pero por esa regla de «una sola voz» arrastra a esta
       story también. Si no, el mismo día el feed diría «¿Estás de cumpleaños?»
       y la story «¿Estás de cumpleaños EN SEPTIEMBRE?», contradiciéndose sobre
       si el beneficio tiene mes o no. Y no lo tiene: el brief dice «el mismo día
       de tu cumpleaños, lunes a viernes, en cualquier horario».
         · sale «en septiembre»;
         · sale la píldora «¡Ven por tu café de regalo!», que repetía lo que ya
           dice el titular.
       Y necesita la MISMA columna que `Cumple1`: creí que no —la story es
       1080×1920 y compone con su propio ancho— y `between-qa.py` me corrigió,
       tinta a 74 px del canto contra los 84 de la marca. Es el mismo defecto: la
       cola del «¿» de Brushwell sobresale del ancho de avance con el que el
       titular se autoescala. Para poder apretarlo hubo que AGREGARLE la prop
       `columnaTitular` a `PiezaStoryBetween`, que no la tenía. */
    script="¿Estás de cumpleaños?"
    caps="Este café es para ti"
    columnaTitular={BETWEEN.bloque.columna}
    oscurecer={0.1}
  >
    <Globos
      posiciones={[
        {cual: 'globosPar', x: 100, y: 1050, ancho: 162, rotacion: -10},
        {cual: 'confeti', x: 812, y: 1090, ancho: 176, rotacion: 8},
      ]}
    />
    {/* ⭐⭐ 01-09, Eli: «la ST de cumpleaños es uno solo… que se vean las dos
        informaciones que dejaste en una sola ST, no dos como carrusel».
        → Se descarta el segundo frame y el listado entra acá abajo.
        Cabe porque el vaso de ESTA escena es más chico que el montado: su
        logotipo impreso queda en y 1189–1271 de 1920 y la base en ~1610, así que
        la banda baja está libre. Con el vaso montado no cabía —el logo llegaba a
        y 1680— y era el motivo de haberlo partido en dos.
        Cuerpo 27 px (en el feed va a 34): en story el listado convive con el
        titular Y con el producto. */}
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        bottom: 272,
        display: 'flex',
        justifyContent: 'center',
      }}
    >
      <Checklist
        items={[
          '☕ Te regalamos un café para disfrutar en cafetería o To Go.',
          '🎂 Accede a este regalo el mismo día de tu cumpleaños.',
          '🗓️ Disponible de lunes a viernes, en cualquier horario.',
          '🪪 Presenta tu carnet en la caja.',
        ]}
        notaLegal="Extras y personalizaciones no incluidas."
        ancho={912}
        size={27}
        gap={13}
      />
    </div>
  </PiezaStoryBetween>
);

/* ─── 4 sept · HUMOR | SEGÚN MIS CÁLCULOS ───
   ⭐ RONDA 4 (comentario E15): «Ok, enlace a carta!». La pieza quedó aprobada;
   lo único que cambia es que la story pasa a llevar el sticker de enlace, y se
   dibuja para reservarle el sitio — si no, se pega encima del titular.        */
export const StCalculos: React.FC = () => (
  <PiezaStoryBetween
    foto={IA + 'calculadora-mesa.png'}
    script="Según mis cálculos…"
    caps={'Te hace\nfalta café'}
    bajadaEnCaja
    bajada="Por suerte, sabemos dónde encontrarlo."
    oscurecer={0.12}
  >
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        bottom: 470,
        display: 'flex',
        justifyContent: 'center',
      }}
    >
      <StickerEnlace texto="Ver la carta" />
    </div>
  </PiezaStoryBetween>
);

/* ─── 9 sept · INTERACTIVA — EMERGENCIA BETWEEN ───
   ⭐ RONDA 4, dos comentarios sobre la misma pieza:
     · diseño (I15): «No se cacha bien al tapar la vitrina con el texto, veamos
       otra diagramación?»
     · cliente (I14): «Agregar opción todas las anteriores»
   La referencia que dejó el cliente (refs-sept-ronda4/I-story-emergencia.jpg)
   dice exactamente cómo se arma: caja de emergencia FRONTAL y simétrica sobre
   fondo plano, el producto solo y grande al centro, y el texto en las bandas
   del marco — nunca encima del producto. La versión anterior era un gabinete
   lejano, chico y rodeado de plantas y tazas: por eso «no se cachaba».
     · el titular ocupa el vacío de ARRIBA, dentro de la caja;
     · el producto queda entero y sin nada encima;
     · la encuesta baja a la pared, ya con la tercera opción que pidió el
       cliente. Se dibuja para que el sticker no termine puesto sobre la caja.
   Sin logo arriba: el vaso ya lo lleva impreso, y la regla de la diseñadora es
   que cuando el vaso trae el logo, no se repite en la pieza.                  */
/* ⭐⭐⭐ RONDA 16 (07-09) — LA PIEZA SE REHACE CONTRA LA REFERENCIA DE ELI.

   Eli, con el pin en la mano
   (https://cl.pinterest.com/pin/1040683426409551586/):

     «necesito que sean café TOGO, croissant jamón queso y muffin de chocolate,
      debe ser igual a la referencia con los textos del brief»

   ⛔ Y NO SE AJUSTA LA ANTERIOR — SE CAMBIA EL PLANTEAMIENTO. Es la regla de
   proceso que salió de la ronda 15: a la segunda vez que un comentario se
   repite se prohíbe tocar el parámetro. Esta pieza llevaba cuatro rondas de
   escala, piso, sombra y luz sobre una GEOMETRÍA equivocada.

   Lo que la referencia hace y la versión anterior no:

     · la caja es VERTICAL y manda en el cuadro (antes: apaisada, 810×675, con
       292 px de vacío arriba y 465 abajo);
     · el TITULAR va SOBRE EL VIDRIO, dentro de la caja (antes: flotando en la
       pared, y por eso la caja parecía un adorno lejano);
     · el llamado va en la BARRA del marco, que es el gesto que hace que se lea
       como una caja de romper (antes: no había barra);
     · el producto es grande dentro del nicho.

   ⚠️ El escenario —muro, marco con bisel, nicho hundido, los tres productos
   reales apoyados y el vidrio encima— lo arma `scripts/between-emergencia-r16.py`
   y sus cifras son las MISMAS que usa este componente, porque las dos se
   escriben en el espacio lógico de 1080×1920:

     ⭐ RONDA 17: la caja ya NO se dibuja — se GENERA vacía con Nano Banana Pro
     (`ia-sept/emergencia-caja-r17.png`) y `between-emergencia-r17.py` le monta
     los tres productos reales sobre su estante de madera. La caja dibujada con
     degradados era lo que Eli leía como «armada, no diseñada»: su esquina era un
     degradado borroso en vez de una arista, y su «piso» una tira plana donde
     nada podía apoyar. Ver la cabecera de ese script.

     ⭐ RONDA 18 — la caja se compone MÁS CHICA a propósito, porque Eli pidió
     «espacio para que contenido pueda colocar una caja de preguntas». El marco
     cierra en y=1215 y deja 365 px lógicos de muro limpio debajo.

     nicho      x 358..752   y  389..1036     ← el vidrio, donde va el titular
     barra      y 1044..1115                  ← donde va «¿CUÁL TOMARÍAS?»
     muro libre bajo la caja  y 1215..1580   ← para la CAJA DE PREGUNTAS de la CM

   ⚠️ SIN el sticker de encuesta dibujado, y es una decisión, no un olvido.
   La fila INTERACCIÓN de la grilla lo anota entre corchetes —«[STICKER QUIZ /
   ENCUESTA]»—, o sea que lo pone la CM en Instagram. Dibujarlo además obligaba
   a repetir «¿Cuál tomarías?» dos veces (en la barra y en el mock) y sus emojis
   salían mal: el ☕ se rendía como una bola morada y el 🥪 como un plátano.
   La opción «Todas las anteriores» que pidió el cliente en `STORIES!I14` es una
   opción de la ENCUESTA, y va en el sticker que configura la CM. Por eso la
   pared de abajo queda limpia: el sticker cae ahí y no sobre la caja, que era
   el reclamo original («no se cacha bien al tapar la vitrina con el texto»).

   Sin logo: el vaso ya lo lleva impreso y la regla de la diseñadora es que
   cuando el vaso firma, no se repite en la pieza.                            */
export const StEmergencia: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: '#eee2d0'}}>
    <FotoFondo src={IA + 'emergencia-fondo-r18.png'} oscurecer={0} />

    {/* ── EL TITULAR, SOBRE EL VIDRIO ──
        Va dentro del nicho (x 176..904 → columna de 728) y sobre la parte ALTA
        del gradiente, que el script del escenario deja oscura a propósito para
        que el beige de marca se lea. `tono="beige"` y no "cafe": acá el fondo
        es el interior de la caja, no la pared crema. */}
    <div
      style={{
        position: 'absolute',
        left: 358,
        width: 394,
        top: 452,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <TitularBetween
        caps={'Romper en caso\nde antojo'}
        alinear="centro"
        tono="beige"
        sizeCaps={48}
        anchoDisponible={356}
      />
      {/* La bajada del brief, en el mismo vidrio y bajo el titular.
          ⚠️ El salto ENTRE niveles tiene que ser mayor que el salto DENTRO del
          nivel: las dos líneas del titular se separan ~24 px, así que acá van
          38 — es la regla de jerarquía del manual, no un número al gusto. */}
      <div
        style={{
          marginTop: 26,
          textAlign: 'center',
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.semibold,
          fontSize: 23,
          lineHeight: 1.20,
          letterSpacing: '0.005em',
          color: BETWEEN.colores.beige,
          opacity: 0.92,
        }}
      >
        {/* ⚠️ El salto va A MANO. En una línea, dentro del nicho de 567 px, el
            texto rompe solo y deja «primero…» SOLA en la segunda línea — una
            palabra viuda, que la regla de la marca prohíbe en la caja de bajada.
            Partido así, las dos líneas quedan parejas. */}
        Si solo pudieras
        <br />
        sacar uno primero…
      </div>
    </div>

    {/* ── EL LLAMADO, EN LA BARRA DEL MARCO ──
        La barra va de y=1044 a y=1115; el bloque se centra en su eje (1080).
        Es el «QUEBRE O VIDRO» de la referencia: el gesto que convierte un marco
        con vidrio en una caja de emergencia. */}
    <div
      style={{
        position: 'absolute',
        left: 358,
        width: 394,
        top: 1044,
        height: 71,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <div
        style={{
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.extrabold,
          fontSize: 28,
          lineHeight: 1,
          letterSpacing: '0.05em',
          textTransform: 'uppercase',
          color: BETWEEN.colores.beige,
        }}
      >
        ¿Cuál tomarías?
      </div>
    </div>
  </AbsoluteFill>
);


/* ─── 14 sept · INTERACTIVA — ¿CUÁNDO ES HORA DE CAFÉ? ─── */
export const StHoraCafe: React.FC = () => (
  <PiezaStoryBetween
    foto={F + 'cafe-desayuno.jpg'}
    script="El mejor momento"
    caps="para un café es…"
    oscurecer={0.16}
  >
    <div style={{position: 'absolute', left: 0, right: 0, top: 980, display: 'flex', justifyContent: 'center'}}>
      <StickerQuiz
        pregunta="Elige tu respuesta"
        opciones={['En la mañana', 'En la tarde', 'En la noche', 'Todo el día ✨']}
        correcta={3}
      />
    </div>
  </PiezaStoryBetween>
);

/* ─── 16 sept · COWORK ───
   Comentario del cliente (N15): «Se puede entender que estuvimos cerrados,
   démosle una vuelta a ese texto». Por eso NO dice «ya abrimos».             */
export const StCowork: React.FC = () => (
  <PiezaStoryBetween
    foto={F + 'mesas-trabajo.jpg'}
    script="Puedes venir"
    caps="¡te esperamos!"
    bajadaEnCaja
    bajada="Ven a trabajar desde Between. Tenemos una mesa para ti."
    datos={['Lunes a viernes · 08:00 a 22:00 hrs']}
    oscurecer={0.14}
    legal="WiFi · Café · Espacios para trabajar"
  />
);

/* ─── 18 sept · SALUDO FIESTAS PATRIAS ─── */
export const StDieciocho: React.FC = () => (
  <PiezaStoryBetween
    foto={F + 'desayuno-completo.jpg'}
    script="Por los sabores"
    caps="que nos reúnen"
    bajada="Que estas Fiestas Patrias estén llenas de buenos momentos, sobremesas y mucho para compartir."
    datos={['¡Felices Fiestas Patrias!']}
    oscurecer={0.16}
  />
);

/* ─── 21 sept · STRUDEL DE MANZANA ───
   Punto 7 del feedback, literal: «collage de fotos debe ser ordenado y utilizar
   toda la composición con la foto, modo división de 4 y al centro el strudel de
   manzana ya que lo que quiere destacar en grande son sus ingredientes y al
   centro como es el postre. Deben verse apetitosos. Cuando no se logra
   visualizar los textos, puedes dejarlo en una caja del color café #675B49».
   → 4 cuadrantes a sangre + strudel al centro + TODO el texto en caja taupe.  */
export const StStrudel: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <Cuadrantes
      alto={1920}
      gap={8}
      fotos={[
        IA + 'strudel-masa.png',
        IA + 'strudel-manzana.png',
        IA + 'strudel-canela.png',
        IA + 'strudel-nueces.png',
      ]}
    />
    {/* el postre al centro, que es lo que pidió el cliente que se vea entero */}
    <div
      style={{
        position: 'absolute',
        left: '50%',
        top: 960,
        transform: 'translate(-50%, -50%)',
        width: 620,
        height: 620,
        borderRadius: 24,
        overflow: 'hidden',
        boxShadow: '0 24px 70px rgba(36,26,18,0.55)',
        border: `6px solid ${BETWEEN.colores.beige}`,
      }}
    >
      <Img
        src={staticFile(IA + 'strudel-entero.png')}
        style={{width: '100%', height: '100%', objectFit: 'cover'}}
      />
    </div>
    <LogoBetween formato="story" posicion="arriba" tono="beige" />
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        top: 432,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      {/* el collage es muy movido: el cliente pidió expresamente que en ese caso
          el texto vaya en caja del color café de la marca.
          ⚠️ La caja necesita ANCHO EXPLÍCITO: `TitularBetween` posiciona sus
          líneas en absoluto, así que su contenedor no tiene ancho propio y la
          caja salía del tamaño de una estampilla. */}
      <div
        style={{
          /* la caja se achicó y bajó el 28-08: a 912 de ancho y arriba en 370
             pisaba el logo. Ahora despeja el lockup completo. */
          width: 760,
          backgroundColor: BETWEEN.cajas.fondo,
          borderRadius: BETWEEN.cajas.radio,
          padding: '28px 40px 36px',
        }}
      >
        <TitularBetween
          script="Cuatro ingredientes"
          caps={'Que saben\nmejor juntos'}
          alinear="centro"
          anchoDisponible={680}
          sizeCaps={96}
        />
      </div>
    </div>
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        top: 1380,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <PilaDatos datos={['Masa · Manzana · Canela · Nueces', 'Strudel de manzana']} />
    </div>
  </AbsoluteFill>
);

/* ─── 22 sept · PRIMAVERA EN BETWEEN ───
   Punto 6: la terraza y los vasos tienen que ser los ACTUALES. La foto sale de
   la sesión real, no de un montaje inventado.                                */
export const StPrimavera: React.FC = () => (
  <PiezaStoryBetween
    foto={IA + 'milkshake-terraza.png'}
    script="La primavera"
    caps="se disfruta así"
    bajadaEnCaja
    bajada="Un milkshake, nuestra terraza y una pausa al sol."
    anchoBajada={640}
    /* la bombilla del vaso llega hasta y≈480: el bloque baja para no cruzarla */
    topBloque={560}
    oscurecer={0.1}
    legal="Ven a disfrutarlo en Between."
  />
);


/* ─── 28 sept · HUMOR | CAFÉ TO GO ───
   Punto 6: «debe ser similar a la referencia que está en grilla, pero en
   Between con una persona con un café gigante». La referencia del brief es
   raw/hilton/between/refs-brief-sept/T11-cafe-gigante.jpg.                    */
export const StHumorToGo: React.FC = () => (
  <PiezaStoryBetween
    foto={IA + 'cafe-gigante.png'}
    script="POV:"
    caps={'Yo cargando el peso\nde mis ganas de café'}
    anclaje="arriba"
    oscurecer={0.08}
  />
);

/* ─── 30 sept · PLATEADA AL CARMENERE ─── */
export const StPlateada: React.FC = () => (
  <PiezaStoryBetween
    foto={IA + 'plateada.png'}
    script="¿El almuerzo"
    caps="se quedó en casa?"
    bajadaEnCaja
    bajada="Tranqui, el plan B se ve bastante mejor por acá."
    datos={['Plateada al Carmenere']}
    anclaje="arriba"
    oscurecer={0.12}
    legal="Haz tu pausa de almuerzo en Between."
  />
);
