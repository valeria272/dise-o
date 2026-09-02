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
import {
  BotonBlanco,
  Checklist, Cuadrantes, Etiqueta, Globos, Ilustra, StickerEnlace,
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
const CAPS_INTERIOR = 79;
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

/* ════════════════════════ FEED · 1080×1350 ════════════════════════ */

/* ─── 1 sept · CARRUSEL DINÁMICO — COWORK EN BETWEEN ───
   (la grilla pide intercambiar fecha con el de To Go: comentario C15)
   Logo SOLO en la portada. La portada tiene personas → el logo va ABAJO.     */

export const Cowork1: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'cowork-laptop.jpg'}
    script="Tu oficina por hoy"
    caps={'Puede ser\nBetween'}
    bajadaEnCaja
    /* ⭐ RONDA 5 (comentario C15 de FEED): «Slide1: dejar el texto consecutivo
       que esta en el cuadro café, es decir, que "pendientes" queda arriba».
       → La caja partía sola y dejaba «pendientes.» SOLA en la segunda línea —
         una viuda, que el manual prohíbe. El corte ahora es el del brief:
         «Espacio, WiFi y café.» / «Tú trae los pendientes.», cada frase en su
         línea. Va con <br /> y no con 
 porque PanelTaupe no lleva
         `white-space: pre-line` y el salto se colapsaría. */
    bajada={<>Espacio, WiFi y café.<br />Tú trae los pendientes.</>}
    /* ⭐ 01-09, Eli: «los textos dentro del recuadro café deben verse más
       ordenados». Con la interlínea de 1,3 por defecto las dos frases quedaban
       flotando separadas dentro de la caja; a 1,16 leen como un bloque. */
    interlineaBajada={1.16}
    columnaCaja={COLUMNA_CAJA}
    columna={COLUMNA_TITULAR}
    aireTituloACaja={AIRE_CAJA}
    anclaje="abajo"
    conLogo
    logoPosicion="abajo"
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
    foto={F + 'mesa-laptop-cafe.jpg'}
    /* ⭐ 01-09, Eli: «desde el slide 2 no agregues la tipografía brushwell, que
       sea de la familia de raleway, así se diferencia de la portada». La script
       queda como marca de la PORTADA. */
    scriptSans
    script="¿Muchos pendientes?"
    caps={'Al menos que sea\ncon buen café'}
    /* ⭐ 01-09 (2ª pasada): cuerpo compartido con la slide 3. Antes cada slide
       se achicaba sola y esta salía en 99 contra 88 de la otra. */
    sizeCaps={CAPS_INTERIOR}
    bajadaEnCaja
    /* El corte va escrito: sin él la caja se partía sola y dejaba «a tu ritmo.»
       colgando en la segunda línea. */
    bajada={<>Encuentra tu mesa<br />y trabaja a tu ritmo.</>}
    interlineaBajada={1.16}
    columnaCaja={COLUMNA_CAJA}
    columna={COLUMNA_TITULAR}
    aireTituloACaja={AIRE_CAJA}
    oscurecer={0.12}
  />
);

export const Cowork3: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'segundo-nivel.jpg'}
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
    interlineaBajada={1.16}
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
    interlineaBajada={1.16}
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
    <FotoFondo src={IA + 'cumple-manos-logo.png'} oscurecer={0.1} />
    <Globos
      posiciones={[
        {cual: 'globosPar', x: 100, y: 96, ancho: 188, rotacion: -8},
        {cual: 'globo', x: 872, y: 150, ancho: 120, rotacion: 10, espejo: true},
        {cual: 'confeti', x: 760, y: 640, ancho: 210, rotacion: 6},
      ]}
    />
    {/* ⛔ SIN lockup. 01-09, Eli: «en el mismo carrusel no agregues en la portada
        el logo, ya que en el vaso está». Es la regla 8 del encabezado —cuando la
        foto trae el vaso con el logotipo impreso, la pieza no lo sobrepone— y con
        esto queda RESUELTA la decisión que estaba abierta desde el 31-08 para las
        tres piezas que la rompían. Además el carrusel ya cumple la regla 5: en
        carrusel el logo va sólo en la portada, y acá la portada no lo necesita. */}
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        bottom: 132,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      {/* ⭐ RONDA 5 (31-08): «Slide1: Texto "¿Estás de cumpleaños en septiembre?
          Este café es para ti. ¡Ven por tu café de regalo!"». Scarlette escribió
          «en agosto»; Eli confirmó el 31-08 que va **septiembre**, que es el mes
          que arranca. Los otros dos textos ya estaban puestos desde la ronda 4. */}
      <TitularBetween
        script="¿Estás de cumpleaños en septiembre?"
        caps="Este café es para ti"
        alinear="centro"
      />
      <PilaDatos
        datos={['¡Ven por tu café de regalo!']}
        style={{marginTop: BETWEEN.aire.tituloACaja}}
      />
    </div>
  </AbsoluteFill>
);

/** Segunda pieza del post: las condiciones del beneficio.
 *  ⭐ RONDA 4 (D15): «En la G2 considerar este listado e incluir emojis
 *  nuevamente» + «Agregar elementos cumpleañeros como en el anterior».
 *  → El listado se mantiene (es el del brief) y cada condición recupera su
 *    emoji; los adornos suben de 2 a 4 para igualar la carga festiva de la G1.
 *  ⭐ RONDA 5 (31-08): «No me gusta como se ve como post, haria un check list
 *  junto con los emojis que piden».
 *  → Fuera el mockup de Instagram: metía una foto dentro de la pieza —un post
 *    dentro de un post— y encima dependía de `togo-vaso.jpg`. Ahora es un
 *    <Checklist> directo sobre la escena, con los emojis intactos. */
export const Cumple2: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    {/* ⭐ RONDA 5: el multiply baja de 0,34 a 0,14. Con la caja taupe del
        checklist ya hay contraste suficiente, y la regla 6 del encabezado manda
        que el texto se resuelva con la caja, no oscureciendo la foto — al 0,34
        la escena se perdía y la pieza parecía una tarjeta lisa. */}
    <FotoFondo src={IA + 'cumple-manos-logo.png'} posicion="60% center" oscurecer={0.14} />
    <Globos
      posiciones={[
        {cual: 'globosPar', x: 100, y: 104, ancho: 174, rotacion: -8},
        {cual: 'globo', x: 872, y: 168, ancho: 116, rotacion: 10, espejo: true},
        {cual: 'confeti', x: 792, y: 1128, ancho: 190, rotacion: 6},
        {cual: 'corazon', x: 96, y: 1196, ancho: 104, rotacion: -10},
      ]}
    />
    {/* Sin logo: en carrusel va SOLO en la portada (regla 5 del encabezado), y
        la portada es la G1. Sin título tampoco — el brief no trae uno para las
        condiciones y no se le inventa copy al cliente. */}
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: 392,
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
     · ⏳ Quedan pendientes de imagen: slide 1 (taza KIMBO, prohibida),
       slide 2 (otro producto «más foto aesthetic») y slide 4 (que se vea
       comido). Ver la nota al pie de este archivo.                           */

export const Foto1: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'desayuno-completo-2.jpg'}
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
       encuadre de la referencia del cliente. La foto es apaisada; se encuadra a
       la izquierda para que el plato y la taza entren enteros en 4:5. */
    foto={F + 'croissant-latte-cenital.jpg'}
    posicionFoto="42% center"
    script="“Está demasiado lindo."
    caps="Foto primero.”"
    scriptSans
    mantenerPunto
    oscurecer={0.12}
  />
);

export const Foto3: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'croissant-plato.jpg'}
    script="“Qué pinta tiene…"
    caps="Esto merece foto.”"
    scriptSans
    mantenerPunto
    oscurecer={0.12}
  />
);

export const Foto4: React.FC = () => (
  <PiezaFeedBodegon
    foto={IA + 'torta-empezada.png'}
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
    <FotoFondo src={IA + 'dos-tazas.png'} oscurecer={0.1} />
    <LogoBetween formato="feed" posicion="arriba" tono="beige" />
    {/* la mesa es clara: sin caja estas dos líneas no se leen (contraste medido 37).
        ESCALONADAS a pedido de Valeria (29-08): una arriba y otra abajo se ve más
        lúdico que las dos en la misma línea. */}
    <Etiqueta x={280} y={1010} size={54} enCaja>Ella habló</Etiqueta>
    <Etiqueta x={800} y={392} size={54} enCaja>Ella escuchó</Etiqueta>
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
    foto={IA + 'togo-salida-2-logo.png'}
    script="¿Vas con poco tiempo?"
    caps={'Tu desayuno\nva contigo'}
    datos={['Promos To Go', HORARIO_TOGO]}
    anclaje="abajo"
    conLogo
    logoPosicion="arriba"
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
    foto={F + 'togo-sandwich-45.jpg'}
    script="Para empezar con algo"
    caps="rico y contundente"
    legal="*Imágenes referenciales."
    oscurecer={0.08}
  >
    {/* ⭐ Regla de la flecha (feedback 28-08): SALE del producto y APUNTA al
        texto — nunca al revés, y nunca montada sobre el producto. */}
    {/* ⭐ RONDA 5 (31-08): «sacar lo que dice "café grande"». Se va la etiqueta
        y con ella su flecha, que ya no apuntaría a nada. El «desde» que pedía la
        misma nota ya estaba puesto desde la ronda 4. */}
    <PilaEsquina
      lineas={[{texto: 'Promo To Go'}, {texto: 'Café + Sándwich desde $4.290', fuerte: true}]}
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
    foto={F + 'togo-dulce-45.jpg'}
    script="Ese gustito que mejora"
    caps="cualquier mañana"
    legal="*Imágenes referenciales."
    oscurecer={0.08}
  >
    {/* el dulce: texto ARRIBA del plato (no encima) y la flecha baja hacia él */}
    <Etiqueta x={140} y={648} size={42}>Croissant</Etiqueta>
    <Ilustra cual="flechaBucle" x={172} y={706} ancho={112} opacidad={0.95} />
    {/* ⭐ RONDA 5 (31-08): «Debe decir "desde $3.790". Sacar lo que dice café
        grande.» El «desde» ya venía de la ronda 4; se va la etiqueta del café y
        su flecha. La del croissant se queda: nadie la objetó. */}
    <PilaEsquina
      lineas={[{texto: 'Promo To Go'}, {texto: 'Café + Dulce desde $3.790', fuerte: true}]}
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
    foto={IA + 'togo-trio-45-logo.png'}
    script="¿Por qué elegir uno?"
    caps="¡Llévate los 3!"
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
      lineas={[
        {texto: 'Promo To Go'},
        {texto: 'Café + Salado + Dulce desde $5.290', fuerte: true},
      ]}
    />
    {/* la cola de la flecha TOCA el producto y apunta al texto — regla del
        manual. Acá nacen del croissant salado y del dulce. */}
    <Ilustra cual="flechaBucle" x={214} y={874} ancho={112} espejo opacidad={0.95} />
    <Etiqueta x={330} y={832} size={40}>Salado</Etiqueta>
    <Ilustra cual="flechaBucle" x={706} y={1072} ancho={112} opacidad={0.95} />
    <Etiqueta x={716} y={1150} size={40}>Dulce</Etiqueta>
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
      {/* ⭐ RONDA 5 (01-09): la CTA sale LITERAL del brief, celda C10 de la hoja
          STORIES: «CTA: Pasa por Between y llévalo contigo.»
          ⭐⭐ Eli, misma fecha: «que la CTA sea "Pasa por Between" y abajo del
          botón "y llévalo contigo". La idea que sea el único botón en blanco y
          textos café del color de la marca».
          → El llamado se parte: la orden va DENTRO del botón blanco y el cierre
            queda fuera, debajo. El texto del botón va en el café de la marca
            (#675b49); el cierre va en beige, porque cae sobre la foto y en café
            no se leería. Es el único elemento blanco macizo de la pieza. */}
      <BotonBlanco style={{marginTop: BETWEEN.aire.tituloACaja}}>Pasa por Between</BotonBlanco>
      <div
        style={{
          marginTop: 16,
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.semibold,
          fontSize: 42,
          lineHeight: 1.1,
          color: BETWEEN.colores.beige,
          textShadow: '0 2px 16px rgba(36,26,18,0.55)',
        }}
      >
        y llévalo contigo.
      </div>
    </div>
    {/* El confeti se corre al hueco de mesa que queda entre el plato y el vaso:
        estaba encima de la media luna y un doodle sobre el producto se ve
        descuidado. */}
    <Ilustra cual="confeti" x={470} y={118} ancho={140} rotacion={-22} opacidad={0.8} />
    <Ilustra cual="corazon" x={898} y={1180} ancho={92} opacidad={0.9} />
    <PilaEsquina
      lineas={[
        {texto: 'Café + Dulce · desde $3.790', fuerte: true},
        {texto: 'Lunes a viernes · 08:00 a 10:00 hrs'},
      ]}
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
       publicación de feed» (D15)—, así que acá también entra «en septiembre». */
    script="¿Estás de cumpleaños en septiembre?"
    caps="Este café es para ti"
    datos={['¡Ven por tu café de regalo!']}
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
export const StEmergencia: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={IA + 'emergencia-caja-2-logo.png'} oscurecer={0.06} />
    {/* el interior de la caja va de y≈185 a y≈1292; el producto arranca en
        y≈765, así que el titular vive en la banda vacía de arriba */}
    {/* el interior de la caja va de x≈244 a x≈849: el titular se ciñe a ese
        ancho para no montarse sobre el marco */}
    <div
      style={{
        position: 'absolute',
        left: 268,
        right: 268,
        top: 268,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      {/* ⭐ RONDA 6: la leyenda va ENTERA en caja alta y en Raleway. Es el
          rótulo impreso de una caja de emergencia real («ROMPER EN CASO DE…»),
          no un titular con script: ahí la tipografía rígida es la que cuenta
          el chiste. Y de paso el bloque baja de dos alfabetos a uno. */}
      <TitularBetween
        caps={'Romper en caso\nde antojo'}
        alinear="centro"
        sizeCaps={76}
        anchoDisponible={544}
      />
    </div>
    {/* ⭐ RONDA 6 (I15): «ojo con la diagramación de los textos, TAPA MUCHO LA
        CAJA». Lo que tapaba era el bloque de abajo: ahora la bajada del brief
        —«Si solo pudieras sacar uno primero…»— y la encuesta viven en la PARED,
        bajo el borde inferior de la caja (y≈1292), y no le pasan por encima.
        Sobre la caja queda solo su rótulo, que es parte del objeto. */}
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        top: 1316,
        textAlign: 'center',
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: BETWEEN.pesos.semibold,
        fontSize: 34,
        lineHeight: 1.15,
        color: BETWEEN.colores.beige,
        textShadow: '0 2px 14px rgba(36,26,18,0.45)',
      }}
    >
      Si solo pudieras sacar uno primero…
    </div>
    {/* la encuesta arranca bajo la bajada y termina antes de y=1580, que es
        donde empieza la zona segura inferior de Meta en historias */}
    <div style={{position: 'absolute', left: 0, right: 0, top: 1376, display: 'flex', justifyContent: 'center'}}>
      <StickerQuiz
        /* ⭐ RONDA 6 — TEXTOS LITERALES DEL BRIEF. La pieza había perdido el
           llamado y había reescrito las opciones:
             · faltaba entero el «¿CUÁL TOMARÍAS?», que es el tercer bloque de
               texto del brief y el que de verdad pregunta;
             · las opciones decían «El café / El croissant / Todas las
               anteriores» cuando el brief pide «☕ Café / 🥐 Algo dulce /
               🥪 Algo salado» — se había perdido ALGO SALADO, que además es uno
               de los tres productos que la pieza muestra dentro de la caja.
           La cuarta opción es la que agregó el cliente en la fila 14
           («Agregar opción todas las anteriores»). */
        pregunta="¿Cuál tomarías?"
        opciones={['☕ Café', '🥐 Algo dulce', '🥪 Algo salado', 'Todas las anteriores']}
        ancho={620}
        compacto
        dosColumnas
      />
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
