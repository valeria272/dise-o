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
  Checklist, Cuadrantes, Etiqueta, Globos, Ilustra, StickerEnlace,
  PiezaPartida, PilaEsquina, StickerQuiz, TituloTresPesos,
} from './BetweenRecursos';

/** Fotos YA GRADADAS a los números de Eli (scripts/between-gradar.py). */
const F = 'assets/hilton/between/fotos-gradadas/';
/** Montajes generados: solo lo que NO existe en el banco de fotos del cliente. */
const IA = 'assets/hilton/between/ia-sept/';
/** Escenas armadas con el VASO REAL recortado de la sesión del cliente (ronda 5). */
const REAL = 'assets/hilton/between/fotos-reales/';

const HORARIO_TOGO = 'Lunes a viernes · 08:00 a 10:00 hrs.';

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
    bajada="Espacio, WiFi y café. Tú trae los pendientes."
    anclaje="abajo"
    conLogo
    logoPosicion="abajo"
    oscurecer={0.1}
  />
);

export const Cowork2: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'winter-garden.jpg'}
    script="¿Muchos pendientes?"
    caps={'Al menos que sea\ncon buen café'}
    bajadaEnCaja
    bajada="Encuentra tu mesa y trabaja a tu ritmo."
    oscurecer={0.12}
  />
);

export const Cowork3: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'segundo-nivel.jpg'}
    script="¿Necesitas cambiar"
    caps="de escenario?"
    bajadaEnCaja
    bajada="También tenemos espacios en nuestro segundo nivel, ideales para trabajar o reunirte."
    oscurecer={0.12}
  />
);

export const Cowork4: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={F + 'servicio-mesa.jpg'} oscurecer={0.12} />
    <div style={{position: 'absolute', left: BETWEEN.bloque.margenX, right: BETWEEN.bloque.margenX, top: 168}}>
      <TituloTresPesos
        arriba="Tú sigue con lo tuyo"
        fuerte={'NOSOTROS\nLLEVAMOS EL CAFÉ'}
        script="a tu mesa"
        size={86}
      />
    </div>
    <PilaEsquina lineas={[{texto: 'Servicio a la mesa mientras trabajas', fuerte: true}]} abajo={120} />
  </AbsoluteFill>
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
        {cual: 'globosPar', x: 62, y: 96, ancho: 190, rotacion: -8},
        {cual: 'globo', x: 872, y: 150, ancho: 120, rotacion: 10, espejo: true},
        {cual: 'confeti', x: 760, y: 640, ancho: 210, rotacion: 6},
      ]}
    />
    <LogoBetween formato="feed" posicion="arriba" tono="beige" />
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
        {cual: 'globosPar', x: 54, y: 104, ancho: 176, rotacion: -8},
        {cual: 'globo', x: 902, y: 168, ancho: 116, rotacion: 10, espejo: true},
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
   Los textos NO se tocan: el cliente objetó la imagen, no el copy.            */

export const HumorCafecito: React.FC = () => (
  <PiezaFeedBodegon
    foto={IA + 'humor-cafecito-2.png'}
    script="Perdón, esa preocupación"
    caps={'No cabe en mi\ncafecito de Between'}
    anclaje="abajo"
    conLogo
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
   El logo aparece UNA sola vez, en la portada; sin caras, vuelve arriba.       */

export const Foto1: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'desayuno-completo-2.jpg'}
    script="Qué rico se ve"
    caps={'Le voy a sacar\nuna foto'}
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
    script="Está demasiado lindo"
    caps="Foto primero"
    oscurecer={0.12}
  />
);

export const Foto3: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'croissant-plato.jpg'}
    script="Qué pinta tiene…"
    caps="Esto merece foto"
    oscurecer={0.12}
  />
);

export const Foto4: React.FC = () => (
  <PiezaFeedBodegon
    foto={IA + 'torta-empezada.png'}
    script="¡Nooo!"
    caps={'Se me olvidó\nla foto'}
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
   ⭐ RONDA 4 (comentario C15 de STORIES): «Café con logo Between!». El montaje
   devolvía el vaso kraft liso; se le estampa el logo real y la composición no
   se toca, que es todo lo que pidió el cliente.                               */
export const StToGoDulce: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <PiezaPartida
      eje="horizontal"
      izquierda={IA + 'togo-cafe-dulce-logo.png'}
      derecha={F + 'rol-canela.jpg'}
    />
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra, opacity: 0.14}} />
    <LogoBetween formato="story" posicion="arriba" tono="beige" />
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
    </div>
    <Ilustra cual="confeti" x={118} y={700} ancho={170} rotacion={-22} opacidad={0.85} />
    <Ilustra cual="corazon" x={946} y={1180} ancho={92} opacidad={0.9} />
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
    /* ⭐⭐ RONDA 5 (31-08): «el vaso no se parece al real… se ve quemado y extraño.
       Debe verse hiperrealista». El vaso ya no es un montaje: es el REAL, recortado
       de `Double Tree 25 jul 25-255` de la sesión del cliente y compuesto sobre la
       escena aprobada. Trae su propia textura de cartón, su logotipo impreso y su
       tapa con relieve — nada de eso se puede estampar encima de un vaso generado.
       Recurso reutilizable: public/assets/hilton/between/togo-vaso-real-nobg.png */
    foto={REAL + 'cumple-vela-real.jpg'}
    /* ⭐ RONDA 5: la story arrastra el mismo titular del feed —«mismos textos de
       la publicación de feed» sigue siendo la orden vigente—, así que acá también
       entra «en septiembre». */
    script="¿Estás de cumpleaños en septiembre?"
    caps="Este café es para ti"
    datos={['¡Ven por tu café de regalo!']}
    oscurecer={0.1}
    /* ⭐ RONDA 5: se va el «Ven a celebrar a Between». La orden vigente es que la
       story lleve LOS MISMOS textos del feed, y el feed son tres, no cuatro. Además
       el legal va anclado a 360 px del pie y con el vaso real —más grande— caía
       justo sobre su logotipo. */
  >
    <Globos
      posiciones={[
        {cual: 'globosPar', x: 70, y: 1180, ancho: 170, rotacion: -10},
        {cual: 'confeti', x: 820, y: 1240, ancho: 190, rotacion: 8},
      ]}
    />
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
      <TitularBetween
        script="Romper en caso"
        caps="de antojo"
        alinear="centro"
        sizeCaps={82}
        anchoDisponible={544}
      />
    </div>
    {/* la encuesta se apoya en el borde inferior de la caja, como el sticker
        real cuando lo pega el community manager, y termina antes de y=1580
        para respetar la zona segura inferior de las historias */}
    <div style={{position: 'absolute', left: 0, right: 0, top: 1318, display: 'flex', justifyContent: 'center'}}>
      <StickerQuiz
        pregunta="Si solo pudieras sacar uno…"
        opciones={['El café', 'El croissant', 'Todas las anteriores']}
        ancho={620}
        compacto
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
