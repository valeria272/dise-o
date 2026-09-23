/**
 * BETWEEN — S2 · CUMPLEAÑOS · DOS STORIES DE SECUENCIA (07-09-2026)
 *
 * Pedido de Eli, 07-09-2026: «Se actualizó carrusel de cumpleaños […] necesito
 * que hagas dos Stories de carrusel estático. Para que sea interactivo, igual
 * al carrusel aprobado.»
 *
 * ⚠️ ESTO REVIERTE UNA ORDEN ANTERIOR, Y ES A PROPÓSITO.
 * El 01-09 Eli había pedido lo contrario —«la ST de cumpleaños es uno solo… que
 * se vean las dos informaciones que dejaste en una sola ST, no dos como
 * carrusel»— y por eso `StCumple` mete el listado en la misma pieza que el vaso.
 * El 07-09 el carrusel del feed se rehizo (`C1 S2 CUMPLE N1/N2.png`, subidos por
 * ella a Drive `1P5NSpKHGCRwqCVZYlPU4zKkH09-YcqKk`) y la orden nueva es la de
 * arriba. `StCumple` NO se toca: sigue siendo la pieza aprobada de su ronda.
 * Estas dos son piezas nuevas, hermanas del carrusel nuevo.
 *
 * ── DE DÓNDE SALE CADA COSA ──────────────────────────────────────────────
 * Las escenas NO se compusieron: se GENERARON con Nano Banana Pro pasándole el
 * carrusel aprobado como referencia, que es el método de Eli documentado en
 * `clients/hilton/PROMPTS-DE-ELI.md` («no se compone: se GENERA»). Así el vaso
 * llega con su logotipo impreso, su carga de tinta y su luz, sin recortes
 * pegados encima — que es lo que produjo cinco rechazos en agosto.
 * ⭐⭐ RONDA 2 (07-09, misma tarde) — Eli: «debe ser una TRANSICIÓN de la foto
 * el slide 1 y la 2». Las dos escenas separadas se botaron: ahora hay UNA sola
 * fotografía continua (`st-cumple-panorama-v2.png`, 4096×4096) y los dos fondos
 * son sus dos mitades, cortadas con `scripts/between-st-cumple-panorama.py`.
 * La mesa, las cintas, el follaje y la luz siguen de una historia a la otra, así
 * que al deslizar la cámara parece moverse por la mesa: el vaso a la izquierda,
 * el plato con medialunas a la derecha.
 * Es la MISMA orden que ya había dado el 04-09 para el carrusel de feed («que
 * sea una continuidad con la slide dos»), y se resuelve igual.
 *   · `st-cumple-1-fondo.png`   ← mitad IZQUIERDA del panorama
 *   · `st-cumple-2-fondo.png`   ← mitad DERECHA del panorama
 *   · `st-cumple-2-ventana.png` ← recorte del MISMO panorama, para la ventana
 *      de la tarjeta (así comparte luz con el fondo).
 * Los prompts textuales quedaron en `clients/hilton/PROMPTS-DE-ELI.md` §3.
 *
 * ⛔ SIN LOGOTIPO, EN NINGUNA DE LAS DOS. Eli: «no agregues logo en portada por
 * el vaso». En la 1 firma el vaso, que lleva el logotipo impreso grande y
 * centrado; en la 2 firma la tarjeta, con el avatar de marca y el handle dos
 * veces. Y coincide con las dos láminas del carrusel aprobado, que tampoco
 * llevan lockup arriba. Al sacarlo, el titular sube a ocupar su sitio.
 *
 * ── LO INTERACTIVO: ZONA RESERVADA, NO STICKER DIBUJADO ──────────────────
 * Decisión de Eli el 07-09: el sticker lo pone el CM al publicar, con el
 * sticker REAL de Instagram. Acá se deja la zona limpia y del tamaño correcto.
 * Un sticker dibujado en el PNG se ve interactivo y no lo es: nadie vota.
 * Es lo mismo que se hizo en la ST EMERGENCIA («deja espacio abajo para dar
 * aire», para la caja de preguntas).
 *   · ST 1 → DESLIZADOR con emoji 🎂
 *   · ST 2 → ENCUESTA «¿Ya lo canjeaste?» · Sí / Voy en camino
 *
 * ── LA REJILLA VERTICAL (1080×1920, se entrega a 2250×4000) ──────────────
 * Zona segura Meta: nada de contenido bajo y=1580 ni sobre y=250
 * (regla global `paid-media-zonas-seguras`, y `StickerQuiz` ya la documenta).
 *   250 ─ zona segura superior
 *   300 ─ ancla del bloque de titular (sube desde 441: sin logotipo arriba, el
 *         titular toma su sitio y le deja aire a la tapa del vaso, en y≈564)
 *  1310 ─ arranca la ZONA RESERVADA del sticker (660×210)
 *  1520 ─ termina la zona reservada  ← quedan 60 px de aire antes del límite
 *  1580 ─ empieza la zona segura inferior de Meta
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
/* `LogoBetween` ya no se importa: ninguna de las dos lleva lockup — ver la
   cabecera. `noUnusedLocals` marcaría el import. */
import {FotoFondo, TitularBetween} from './BetweenSistema';
import {Globos} from './BetweenRecursos';

const IA = 'assets/hilton/between/ia-sept/';

/** Alto y ancho del sticker real de Instagram, medidos sobre `StickerQuiz`:
 *  una encuesta de dos opciones y un deslizador ocupan lo mismo, ~660×210. */
/* top 1280 y no 1310: con la zona más abajo, la dirección de la ST1 y el legal
   de la ST2 quedaban obligados a arrancar en ~1590 y `between-qa.py` los marcó
   («entra 48 px en la zona segura inferior»). Subiendo la zona 30 px entra todo
   por encima de 1580. */
const ZONA_STICKER = {ancho: 660, alto: 210, top: 1280};

/**
 * Marca de la zona reservada. NO va en la pieza que se publica: sólo en la
 * variante `-guia`, para que el CM sepa dónde y de qué porte va el sticker.
 */
const ZonaReservada: React.FC<{etiqueta: string}> = ({etiqueta}) => (
  <div
    style={{
      position: 'absolute',
      left: (1080 - ZONA_STICKER.ancho) / 2,
      top: ZONA_STICKER.top,
      width: ZONA_STICKER.ancho,
      height: ZONA_STICKER.alto,
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

/* ══════════════════════════════════════════════════════════════════════════
   ST 1 · EL VASO ES HÉROE
   Réplica en 9:16 de la lámina 1: misma script arriba, misma caja alta abajo,
   mismo vaso en la mano con las hojas de oro. Los textos son LITERALES de la
   pieza aprobada — no se reescriben.
   ══════════════════════════════════════════════════════════════════════════ */
export const StCumpleC1: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: '#1d1a14'}}>
    {/* `oscurecer` bajo: la escena ya viene gradada del generador y el manual
        prohíbe apagar la foto para que se lea un texto. El titular cae sobre el
        follaje oscuro del fondo, así que 0,12 basta. */}
    <FotoFondo src={IA + 'st-cumple-1-fondo.png'} oscurecer={0.12} />

    {/* EL TITULAR — en y=300, no en 441. El ancla de 441 de la plantilla de Eli
        está calculada para caer BAJO el logotipo; acá no hay logotipo (lo firma
        el vaso), así que el bloque sube a ocuparlo y queda a 64 px de la tapa.
        `anchoDisponible` = 810 es obligatorio en toda script que empieza con
        «¿»: la cola del signo sobresale del ancho de avance de Brushwell y sin
        esto `between-qa.py` marca tinta a <84 px del canto. */}
    <div
      style={{
        position: 'absolute',
        left: (1080 - BETWEEN.bloque.columna) / 2,
        width: BETWEEN.bloque.columna,
        top: 300,
      }}
    >
      <TitularBetween
        script="¿Estás de cumpleaños?"
        caps="Este café es para ti"
        alinear="centro"
        tono="beige"
        anchoDisponible={BETWEEN.bloque.columna}
      />
    </div>

    {/* El globo va a la IZQUIERDA, sobre el follaje, y no a la derecha del vaso
        como en la lámina 1 del carrusel.
        ⛔ Dos posiciones descartadas, las dos por lo mismo — el garabato de
        Between se apoya en el FONDO, nunca sobre el producto ni sobre quien lo
        sostiene:
          · x 88 · y 1120 → caía sobre la MANO, como una mancha sobre la piel;
          · x 806 · y 690 → con el encuadre nuevo el vaso llega hasta x=900 y el
            globo se le montaba encima del logotipo impreso: se leía «BETWEENS»
            y la cuerda cruzaba el wordmark. Romper el logotipo del vaso es el
            peor error posible en esta pieza.
        A la derecha ya no cabe: entre el vaso (x≈900) y el canto quedan 180 px y
        el margen de marca son 84. A la izquierda, en cambio, hay follaje limpio
        entre el titular y la mano. */}
    <Globos
      posiciones={[{cual: 'globosPar', x: 100, y: 620, ancho: 140, rotacion: -8}]}
    />

    {guia ? <ZonaReservada etiqueta={'DESLIZADOR 🎂\n660 × 210'} /> : null}

    {/* La dirección, igual que en la lámina 1. Va bajo la zona del sticker y
        TERMINA antes de 1580: a 30 px de cuerpo ocupa ~36, así que 1534 la deja
        cerrando en 1570. Estaba en 1596 y la compuerta la rebotó. */}
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: 1534,
        textAlign: 'center',
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: BETWEEN.pesos.semibold,
        fontSize: 30,
        letterSpacing: '0.01em',
        color: BETWEEN.colores.beige,
        opacity: 0.94,
        textShadow: '0 2px 14px rgba(0,0,0,0.55)',
      }}
    >
      AV. Vitacura 2727, Las Condes
    </div>
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 2 · LAS CONDICIONES, EN EL MOCK DE POST

   ⚠️ POR QUÉ ESTA TARJETA NO USA `MarcoIGPost`.
   El componente compartido se quedó atrás respecto de la pieza que Eli aprobó,
   en dos cosas que ella escribió explícitamente:
     · su fondo es `#ffffff` y el mock aprobado es CREMA `#fff9eb`
       («el mock de post es CREMA, no blanco, con la UI en taupe»);
     · sus ítems son `BurbujaChat`, o sea VIÑETAS «•», y el aprobado lleva
       CASILLAS DE VERIFICACIÓN («los ítems van en casillas de verificación
       (✓ en cuadrado redondeado), no en viñetas»).
   No se corrigió `MarcoIGPost` en su lugar porque lo usan piezas YA APROBADAS
   (`BetweenCumple.tsx` y la G2 de `BetweenSeptiembre.tsx`) y cambiarle el
   defecto las re-flujaría — es la misma razón por la que `columnaTitular` entró
   como opt-in. Cuando esas piezas se rehagan, esto se sube al componente.

   GEOMETRÍA — medida sobre `C1 S2 CUMPLE N2.png` (master 2250, valores @1080):
     tarjeta      x 197–883  → ancho 686 · relleno 30
     ventana      alto 640 en el carrusel
     filas taupe  ancho 486, centradas (100 px de aire a cada lado)
     alto de fila 95 con dos líneas · 66 con una · separación 18
     cuerpo       26 px, interlínea 1,28 · casilla ✓ de 46
   ══════════════════════════════════════════════════════════════════════════ */

const CARD = {ancho: 686, relleno: 30, fila: 486, gap: 18, cuerpo: 26, casilla: 46};

/**
 * Los emojis van como IMAGEN, no como glifo de fuente.
 *
 * ⛔ En Windows, Chrome resuelve la pila `…, 'Segoe UI Emoji'` y el ☕ sale
 * LILA. Es exactamente el defecto que Eli ya había cazado en los renders del
 * estudio —«el ☕ lila […] es un defecto de la pila de fuentes en Windows, no de
 * diseño»— y que su pieza no tiene, porque ella trabaja con emojis de Apple.
 * Apple Color Emoji no se puede redistribuir, así que estos cuatro se RECORTAN
 * de la lámina 2 aprobada con `scripts/between-emoji-extraer.py`: son la obra
 * del propio cliente y calzan exacto con el carrusel.
 *
 * La caja reserva el ancho pero mide `1em` de ALTO, y la imagen va dentro en
 * posición absoluta. Así el emoji puede sobresalir de la línea sin estirarla:
 * en la pieza aprobada las filas de dos líneas miden 95 px, y un `inline-block`
 * de 40 px las empujaría a ~104.
 */
const EMOJI = {
  cafe: 1.172,
  regalo: 1.053,
  estrella: 1.0,
  sonrisa: 1.0,
} as const;

const Emoji: React.FC<{cual: keyof typeof EMOJI; alto?: number}> = ({cual, alto = 40}) => (
  <span
    style={{
      display: 'inline-block',
      /* Reserva 12 px MENOS de los que ocupa la imagen, a propósito: así el
         emoji se mete en el relleno derecho de la fila en vez de empujar el
         salto de línea. Es lo que hace la pieza aprobada — ahí el ☕ termina en
         x=779 y la fila en 783, o sea pisa el relleno y queda a 4 px del canto.
         Sin esto, «…o To Go.» y «…en la caja.» mandaban el emoji SOLO a una
         línea nueva y las filas crecían de 95 a 132 px. */
      width: Math.round(alto * EMOJI[cual]) - 12,
      height: '1em',
      position: 'relative',
      marginLeft: 5,
      verticalAlign: 'baseline',
    }}
  >
    <Img
      src={staticFile(`assets/hilton/between/emoji/${cual}.png`)}
      style={{position: 'absolute', left: 0, bottom: '-0.30em', height: alto, width: 'auto'}}
    />
  </span>
);

const FilaCheck: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      width: CARD.fila,
      boxSizing: 'border-box',
      background: 'rgba(103,91,73,0.93)',
      borderRadius: 16,
      /* 16 de relleno lateral (no 20): medido sobre la fila aprobada, donde el
         texto arranca en x=398 con la fila en 297. */
      padding: '14px 16px',
      marginBottom: CARD.gap,
      display: 'flex',
      alignItems: 'flex-start',
      gap: 14,
    }}
  >
    <div
      style={{
        flexShrink: 0,
        width: CARD.casilla,
        height: CARD.casilla,
        borderRadius: 10,
        border: `3px solid ${BETWEEN.colores.beige}`,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: 26,
        lineHeight: 1,
        color: BETWEEN.colores.beige,
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: 800,
      }}
    >
      ✓
    </div>
    {/* Sin pila de emojis: acá los emojis entran como <Emoji/>, que es una
        imagen. Ver el comentario de `EMOJI` más arriba. */}
    <div
      style={{
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: 600,
        fontSize: CARD.cuerpo,
        /* ⭐ MEDIDO, no al gusto. Con el tracking por defecto la misma línea
           («Accede a este regalo el mismo») salía 361 px contra los 348,5 de la
           pieza aprobada: 3,6 % más suelta. Esos 12 px de más eran justo los que
           echaban el emoji a la línea siguiente. */
        letterSpacing: '-0.015em',
        lineHeight: 1.28,
        color: '#ffffff',
        paddingTop: 4,
      }}
    >
      {children}
    </div>
  </div>
);

export const StCumpleC2: React.FC<{guia?: boolean}> = ({guia = false}) => {
  const anchoVentana = CARD.ancho - CARD.relleno * 2;
  /* La ventana baja de 640 (carrusel) a 520. En story la tarjeta convive con el
     logo ARRIBA y con la zona del sticker ABAJO: a 640 la tarjeta mide 899 y,
     arrancando en y=430, termina en 1329 — se come el sticker que empieza en
     1310. Se achica la VENTANA, no el marco ni el cuerpo del texto, que es lo
     que el sistema ya hace en story con el listado (27 px en vez de 34).

     ⭐ RONDA 2: baja otra vez, de 520 a 460, y la tarjeta sube a y=330 (puede,
     porque ya no hay logotipo encima). Las dos cosas juntas dejan ver el PLATO
     entre el pie de la tarjeta y la mesa — que es el sentido de la transición:
     si la tarjeta lo tapa entero, la historia 2 deja de continuar a la 1.
     Las cuatro filas suman 422 px, así que quedan 19 de aire arriba y abajo. */
  const altoVentana = 460;

  return (
    <AbsoluteFill style={{backgroundColor: '#1d1a14'}}>
      <FotoFondo src={IA + 'st-cumple-2-fondo.png'} oscurecer={0.18} />

      {/* UN solo grupo, a la izquierda, igual que en la ST 1.
          ⛔ El confeti de la derecha se descartó. La tarjeta termina en x=883 y
          el margen de marca son 84, así que en esa franja de 197 px no existe
          posición que no quede pegada a la esquina de la tarjeta (x 880) o
          cruzando el margen (x 898 → tinta a 74 px del canto, marcado por
          `between-qa.py`). Y no hace falta: las cintas doradas de la escena ya
          hacen todo el trabajo festivo de ese lado. */}
      <Globos
        /* `between-qa.py` mide la tinta contra un margen de 84 px y los
           garabatos de borde SIEMPRE lo cruzan — la propia lámina 2 aprobada da
           39 px a la izquierda y 60 a la derecha. No es un defecto de la pieza,
           es que la regla mide texto y acá hay ilustración. Aun así se meten
           hacia adentro para no quedar MÁS afuera que la pieza de Eli. */
        posiciones={[{cual: 'globosPar', x: 100, y: 396, ancho: 132, rotacion: -8}]}
      />

      <div
        style={{
          position: 'absolute',
          left: (1080 - CARD.ancho) / 2,
          top: 330,
          width: CARD.ancho,
          boxSizing: 'border-box',
          background: BETWEEN.colores.beige,
          borderRadius: 10,
          padding: `${CARD.relleno}px ${CARD.relleno}px ${Math.round(CARD.relleno * 0.9)}px`,
          boxShadow: '0 26px 64px rgba(0,0,0,0.38)',
        }}
      >
        {/* cabecera — avatar con anillo, fondo café y logo beige adentro
            (ronda 12: «el logo del icono […] es fondo café between + logo en
            beige»), el handle y los tres puntos. */}
        <div style={{display: 'flex', alignItems: 'center', gap: 16, marginBottom: 18}}>
          <div
            style={{
              width: 62,
              height: 62,
              borderRadius: '50%',
              background: BETWEEN.colores.cafe,
              border: `3px solid ${BETWEEN.colores.cafe}`,
              boxShadow: `0 0 0 3px ${BETWEEN.colores.beige}, 0 0 0 6px ${BETWEEN.colores.cafe}`,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              overflow: 'hidden',
              flexShrink: 0,
            }}
          >
            <Img
              src={staticFile(BETWEEN.logo.beige)}
              style={{width: '76%', objectFit: 'contain'}}
            />
          </div>
          <div
            style={{
              fontFamily: BETWEEN.fuentes.sans,
              fontWeight: 700,
              fontSize: 34,
              color: '#3b2f24',
            }}
          >
            between.coffeebar
          </div>
          <div style={{marginLeft: 'auto', color: '#3b2f24', fontSize: 34, letterSpacing: 3}}>
            •••
          </div>
        </div>

        {/* la ventana, con las cuatro casillas centradas encima */}
        <div
          style={{
            position: 'relative',
            width: anchoVentana,
            height: altoVentana,
            borderRadius: 3,
            overflow: 'hidden',
          }}
        >
          <Img
            src={staticFile(IA + 'st-cumple-2-ventana.png')}
            style={{width: '100%', height: '100%', objectFit: 'cover'}}
          />
          <div
            style={{
              position: 'absolute',
              inset: 0,
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'center',
              alignItems: 'center',
            }}
          >
            {/* Los CUATRO ítems de la pieza aprobada, literales y en su orden.
                Cuatro, no cinco: «¡Pregúntanos por los cafés disponibles!»
                está descartado desde la ronda 5. */}
            <FilaCheck>
              Te regalamos un café para disfrutar en cafetería o To Go.
              <Emoji cual="cafe" />
            </FilaCheck>
            <FilaCheck>
              Accede a este regalo el mismo día de tu cumpleaños.
              <Emoji cual="regalo" />
            </FilaCheck>
            <FilaCheck>
              Disponible de lunes a viernes, ¡en cualquier horario!
              <Emoji cual="estrella" />
            </FilaCheck>
            <FilaCheck>
              Presenta tu carnet en la caja.
              <Emoji cual="sonrisa" />
            </FilaCheck>
          </div>
        </div>

        {/* barra de acciones */}
        <div style={{display: 'flex', alignItems: 'center', gap: 26, marginTop: 22, color: '#3b2f24'}}>
          <span style={{fontSize: 42, color: '#e0443a', lineHeight: 1}}>♥</span>
          <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#3b2f24" strokeWidth="1.8">
            <path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5 8.6 8.6 0 0 1-3.9-.95L3 21l1.95-5.6A8.38 8.38 0 0 1 4 11.5 8.5 8.5 0 0 1 12.5 3 8.38 8.38 0 0 1 21 11.5z" />
          </svg>
          <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#3b2f24" strokeWidth="1.8">
            <path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z" />
          </svg>
          <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#3b2f24" strokeWidth="1.8" style={{marginLeft: 'auto'}}>
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
          </svg>
        </div>
        <div
          style={{
            fontFamily: BETWEEN.fuentes.sans,
            fontWeight: 700,
            fontSize: 30,
            color: '#7a6a58',
            marginTop: 12,
          }}
        >
          between.coffeebar
        </div>
      </div>

      {guia ? <ZonaReservada etiqueta={'ENCUESTA\n«¿Ya lo canjeaste?»\n660 × 210'} /> : null}

      {/* El legal, literal de la lámina 2 aprobada. En cursiva y al pie.
          ⭐ 08-09-2026: son DOS líneas, cada una con su propio asterisco, calcadas
          del carrusel de feed que Eli subió hoy 12:31 («C1 S2 CUMPLE N2.png»).
          El cliente reclamó que «sacaron el legal de los extras 😭, hay que
          dejarlo»: la corrección de la mañana reescribió la frase completa y en
          el camino borró la segunda oración, que las versiones viejas sí traían.
          ⛔ El legal es ACUMULATIVO — se le agrega, no se redacta de cero. */}
      <div
        style={{
          position: 'absolute',
          left: 84,
          right: 84,
          /* ⭐ Eli, ronda 2: «el legal más abajo donde se lea mejor». En 1524
             caía sobre el plato y las cintas y peleaba con el hojaldre. Acá, en
             1640, cae sobre la MESA de madera limpia y oscura, que es el único
             sitio del cuadro donde un texto beige se lee sin ayuda.
             ⚠️ Entra en la franja inferior de 340 px de Meta y por eso
             `between-qa.py` lo marca. Es una decisión de ella y tiene
             precedente: la plantilla de story con logo abajo de la propia Eli
             entra 104 px. **Medido con el legal de DOS líneas (08-09):** la
             tinta va de y=1646,4 a y=1702,1 y cierra a 218 px del borde, o sea
             122 px dentro de la franja — antes, con una línea, eran 93.
             El bloque creció HACIA ABAJO a propósito: la línea 1 queda
             exactamente donde Eli la aprobó (0 px de diferencia contra el
             render anterior) y la banda de la línea 2 está MÁS oscura que la de
             la 1 (luminancia 0,071 contra 0,155 midiendo por tercios), así que
             el beige se lee mejor abajo que arriba. Subir el bloque para
             ganar franja lo devolvería sobre el plato y las cintas, que es
             justo lo que ella mandó corregir. Si esta pieza pasara a pauta, hay
             que rehacer el pie — 122 px es más que sus propios 104. */
          top: 1640,
          textAlign: 'center',
          fontFamily: BETWEEN.fuentes.sans,
          fontStyle: 'italic',
          fontWeight: BETWEEN.pesos.semibold,
          fontSize: 25,
          lineHeight: 1.3,
          color: BETWEEN.colores.beige,
          opacity: 0.93,
          textShadow: '0 2px 14px rgba(0,0,0,0.6)',
        }}
      >
        {/* Cada línea en su propio div: con un <br/> suelto, JSX deja el salto
            de línea del código como espacio y descentra la línea. */}
        <div>*Presenta tu cédula de identidad para canjear tu café el día de tu cumpleaños.</div>
        <div>*Extras y personalizaciones no incluidas.</div>
      </div>
    </AbsoluteFill>
  );
};

/* Variantes «guía» — llevan dibujada la zona del sticker. NO se entregan al
   cliente ni se suben al portal: son para el CM. */
export const StCumpleC1Guia: React.FC = () => <StCumpleC1 guia />;
export const StCumpleC2Guia: React.FC = () => <StCumpleC2 guia />;
