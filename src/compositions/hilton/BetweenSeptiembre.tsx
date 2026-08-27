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
  Bajada,
  FotoFondo,
  LogoBetween,
  PiezaFeedBodegon,
  PiezaStoryBetween,
  TitularBetween,
  PilaDatos,
} from './BetweenSistema';
import {
  Cuadrantes, Etiqueta, Globos, Ilustra, MarcoIGPost,
  PiezaPartida, PilaEsquina, StickerQuiz, TituloTresPesos,
} from './BetweenRecursos';

/** Fotos YA GRADADAS a los números de Eli (scripts/between-gradar.py). */
const F = 'assets/hilton/between/fotos-gradadas/';
/** Montajes generados: solo lo que NO existe en el banco de fotos del cliente. */
const IA = 'assets/hilton/between/ia-sept/';

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
   Comentario de diseño (D15): «Agregar elementos cumpleañeros como en el
   anterior». Se mantiene la dirección de arte de agosto —globos doodle de la
   propia diseñadora + packshot— y cambian foto y texto, que es justo lo que
   pidió Valeria: misma dirección, no la misma pieza.                          */

export const Cumple1: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={IA + 'cumple-manos.png'} oscurecer={0.1} />
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
        bottom: 150,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <TitularBetween script="Este café" caps="es para ti" alinear="centro" />
      <Bajada style={{marginTop: BETWEEN.aire.tituloABajada, textAlign: 'center'}}>
        Si estás de cumpleaños, en Between te invitamos el café.
      </Bajada>
    </div>
  </AbsoluteFill>
);

/** Segunda pieza del post: las condiciones, en el mockup de IG que usa Eli. */
export const Cumple2: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={IA + 'cumple-manos.png'} posicion="60% center" oscurecer={0.34} />
    <Globos
      posiciones={[
        {cual: 'globoAlt', x: 60, y: 120, ancho: 130, rotacion: -6},
        {cual: 'corazon', x: 900, y: 1080, ancho: 110, rotacion: 8},
      ]}
    />
    <div style={{position: 'absolute', left: 0, right: 0, top: 150, display: 'flex', justifyContent: 'center'}}>
      <MarcoIGPost
        foto={<Img src={staticFile(F + 'togo-vaso.jpg')} style={{width: '100%', height: '100%', objectFit: 'cover'}} />}
        burbujas={[
          'Te regalamos un café para disfrutar en cafetería o To Go.',
          'Accede a este regalo el mismo día de tu cumpleaños.',
          'Disponible de lunes a viernes, en cualquier horario.',
          'Presenta tu carnet en la caja.',
        ]}
        notaLegal="Extras y personalizaciones no incluidas."
      />
    </div>
  </AbsoluteFill>
);

/* ─── 7 sept · POST ESTÁTICO — HUMOR | CAFECITO BETWEEN ───
   Foto con persona: el bloque baja y el logo sube, para no cruzar el rostro.  */

export const HumorCafecito: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'chica-cafe.jpg'}
    // el rostro sube al tercio alto para que el bloque de abajo no lo cruce:
    // regla dura de la diseñadora, ningún texto sobre caras ni ojos
    posicionFoto="60% 22%"
    script="Perdón, esa preocupación"
    caps={'No cabe en mi\ncafecito de Between'}
    anclaje="abajo"
    conLogo
    logoPosicion="abajo"
    oscurecer={0.14}
  />
);

/* ─── 9 sept · CARRUSEL — PRIMERO LA FOTO… ¿O NO? ───
   Punto 4 del feedback: en la portada («Qué rico se ve») el logo va en el
   MARGEN DE ABAJO porque arriba tapa a las personas; y el logo aparece UNA
   sola vez en todo el carrusel.                                              */

export const Foto1: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'desayuno-mesa.jpg'}
    script="Qué rico se ve"
    caps={'Le voy a sacar\nuna foto'}
    anclaje="abajo"
    conLogo
    logoPosicion="abajo"
    oscurecer={0.12}
  />
);

export const Foto2: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'cafe-desayuno.jpg'}
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
    {/* la mesa es clara: sin caja estas dos líneas no se leen (contraste medido 37) */}
    <Etiqueta x={280} y={1010} size={54} enCaja>Ella habló</Etiqueta>
    <Etiqueta x={760} y={1010} size={54} enCaja>Ella escuchó</Etiqueta>
  </AbsoluteFill>
);

/* ─── 14 sept · CARRUSEL — PROMOS TO GO ───
   Punto 5 del feedback, literal: «portada deja el logo, quita la transparencia
   café y centra textos, cuadro café con texto. Y en las demás slides de ese
   carrusel quitar logos, dejar una única vez en la portada principal».
   → portada: logo sí · oscurecer 0,06 (casi nada) · todo centrado · caja taupe
   → slides 2-4: sin logo                                                      */

export const ToGo1: React.FC = () => (
  <PiezaFeedBodegon
    foto={IA + 'togo-salida.png'}
    script="¿Vas con poco tiempo?"
    caps={'Tu desayuno\nva contigo'}
    datos={['Promos To Go', HORARIO_TOGO]}
    conLogo
    logoPosicion="abajo"
    /* la modelo tiene la cara en el tercio alto: el bloque baja casi al centro
       para no cruzarla (feedback de Elisabet, 28-08) */
    topBloque={470}
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
    <Ilustra cual="flechaBucle" x={830} y={1030} ancho={120} rotacion={185} opacidad={0.95} />
    <Etiqueta x={880} y={1150} size={42}>Café grande</Etiqueta>
    <PilaEsquina
      lineas={[{texto: 'Promo To Go'}, {texto: 'Café + Sándwich $4.290', fuerte: true}]}
    />
  </PiezaFeedBodegon>
);


export const ToGo3: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'togo-dulce-actual.jpg'}
    script="Ese gustito que mejora"
    caps="cualquier mañana"
    legal="*Imágenes referenciales."
    oscurecer={0.08}
  >
    {/* el rol: texto ARRIBA del plato (no encima) y la flecha sale del rol */}
    <Etiqueta x={220} y={628} size={42}>Rol de canela</Etiqueta>
    <Ilustra cual="flechaBucle" x={245} y={686} ancho={118} opacidad={0.95} />
    {/* el café: texto DEBAJO del vaso — arriba parecía bajada del titular */}
    <Ilustra cual="flechaBucle" x={870} y={900} ancho={115} rotacion={185} opacidad={0.95} />
    <Etiqueta x={905} y={1015} size={42}>Café grande</Etiqueta>
    <PilaEsquina
      lineas={[{texto: 'Promo To Go'}, {texto: 'Café + Dulce $3.790', fuerte: true}]}
    />
  </PiezaFeedBodegon>
);


export const ToGo4: React.FC = () => (
  <PiezaFeedBodegon
    /**
     * Foto REAL (25-jul-2025) en vez del montaje IA: el montaje traía el vaso
     * sin logo y desentonaba con los otros slides del carrusel, y la etiqueta
     * decía «croissant y sándwich» cuando en la foto solo había croissant.
     */
    foto={F + 'togo-croissant-actual.jpg'}
    script="¿Por qué elegir uno?"
    caps="Llévalo contigo"
    sizeCaps={100}
    /* el vaso ocupa la esquina superior: el titular baja a la banda del medio */
    topBloque={558}
    legal="*Imágenes referenciales."
    oscurecer={0.08}
  >
    <Ilustra cual="flechaBucle" x={600} y={330} ancho={130} opacidad={0.95} />
    <Etiqueta x={545} y={288} size={42}>Café grande</Etiqueta>
    <Ilustra cual="flechaBucle" x={850} y={950} ancho={120} espejo opacidad={0.95} />
    <Etiqueta x={935} y={905} size={42}>Croissant</Etiqueta>
    <PilaEsquina
      lineas={[{texto: 'Promo To Go'}, {texto: 'Café + Salado + Dulce $5.290', fuerte: true}]}
    />
  </PiezaFeedBodegon>
);


/* ════════════════════════ STORIES · 1080×1920 ════════════════════════ */

/* ─── 1 sept · PROMO TO GO | CAFÉ + DULCE ───
   Composición PARTIDA en dos fotos con la script cruzando la costura: es el
   recurso del post «Good Morning» de la marca. Rompe el «titular arriba, foto
   abajo» sin salirse de la línea gráfica.                                     */
export const StToGoDulce: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <PiezaPartida
      eje="horizontal"
      izquierda={IA + 'togo-cafe-dulce.png'}
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

/* ─── 3 sept · CAFÉ DE REGALO POR TU CUMPLEAÑOS ─── */
export const StCumple: React.FC = () => (
  <PiezaStoryBetween
    foto={IA + 'cumple-vela.png'}
    script="¡Disfruta tu cumple"
    caps="desde temprano!"
    bajadaEnCaja
    bajada="Si estás de cumpleaños, tenemos un café de regalo para ti."
    datos={['Presenta tu carnet · Lunes a viernes · Todo el día']}
    oscurecer={0.1}
    legal="Ven a celebrar a Between."
  >
    <Globos
      posiciones={[
        {cual: 'globosPar', x: 70, y: 1180, ancho: 170, rotacion: -10},
        {cual: 'confeti', x: 820, y: 1240, ancho: 190, rotacion: 8},
      ]}
    />
  </PiezaStoryBetween>
);

/* ─── 4 sept · HUMOR | SEGÚN MIS CÁLCULOS ─── */
export const StCalculos: React.FC = () => (
  <PiezaStoryBetween
    foto={IA + 'calculadora-mesa.png'}
    script="Según mis cálculos…"
    caps={'Te hace\nfalta café'}
    bajadaEnCaja
    bajada="Por suerte, sabemos dónde encontrarlo."
    oscurecer={0.12}
  />
);

/* ─── 9 sept · INTERACTIVA — EMERGENCIA BETWEEN ─── */
export const StEmergencia: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={IA + 'emergencia-caja.png'} oscurecer={0.06} />
    <LogoBetween formato="story" posicion="arriba" tono="beige" />
    {/* el gabinete vive en y 512–1240: el titular va ARRIBA de él y la
        pregunta DEBAJO, para que el café y el croissant se vean enteros
        (feedback 28-08: «el texto está sobre el café») */}
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        /* el logo de story termina en y≈370: el titular parte bajo él y su caja
           alta cae sobre el vidrio VACÍO del gabinete, arriba de los productos */
        top: 392,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <TitularBetween script="Romper en caso" caps="de antojo" alinear="centro" sizeCaps={100} />
    </div>
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        top: 1300,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <Bajada style={{textAlign: 'center'}}>Si solo pudieras sacar uno primero…</Bajada>
      <PilaDatos datos={['¿Cuál tomarías?']} style={{marginTop: BETWEEN.aire.tituloACaja}} />
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
