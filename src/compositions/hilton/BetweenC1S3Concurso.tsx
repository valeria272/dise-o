/**
 * BETWEEN — S3 · CARRUSEL CONCURSO «SE BUSCA: CEO DEL CAFÉ» (16-09-2026)
 *
 * Encargo: grilla viva de Between, hoja FEED, columna 10 — estado
 * `OK PARA DISEÑAR`, fecha `X DEFINIR`, tipo CARRUSEL, dos slides.
 * Concurso del 21 al 30-09-2026, ganador el 1 de octubre (Día del Café).
 * Entrega: `C1 S3 CONCURSO N1/N2.png`, 2250×2813, carpeta `S3 · BW` del Drive.
 *
 * ── LAS DOS REFERENCIAS DEL CLIENTE, Y QUÉ SE TOMÓ DE CADA UNA ───────────
 * La grilla trae `REF 1` y `REF2` (Pinterest; bajadas a
 * `raw/hilton/between/refs-concurso-s3/`). Las dos comparten UN recurso, y ése
 * es el encargo real de esta pieza:
 *
 * | Referente | El elemento | Traducido a Between |
 * |---|---|---|
 * | REF 1 — perro recortado con borde blanco sobre pared lisa, titular con contorno de sticker, bajada dentro de una caja de color plano | el **recorte tipo sticker** y la **caja de color con el remate** | la escena se GENERA ya recortada, con su borde blanco; y la caja de color plano es, literal, la **caja taupe `#675B49`** que la marca ya tiene |
 * | REF2 — collage sobre papel: rótulo arriba, titular, y una hoja de cuaderno pegada con la LISTA de ítems | la **hoja con la lista** | la **tarjeta crema con filas taupe y casillas ✓**, que es la que Eli aprobó en `C1 S2 CUMPLE N2` |
 *
 * ⚠️ Lo que NO se tomó: el papel arrugado, la cinta adhesiva, las polaroids y
 * los garabatos de la REF2. El repertorio de línea de Between son los trazos del
 * `.svg` de Eli y el manual prohíbe inventarle otros. La condición que ella dejó
 * escrita el 08-09 vale igual acá: «deben ser colores y fondos de Between, pero
 * puedes guiarte de elementos de la referencia para hacerlos similar».
 *
 * ── DE DÓNDE SALE LA FOTO ────────────────────────────────────────────────
 * Primero se buscó en el material (regla madre de la ronda 10). De persona
 * trabajando NO hay: `sesion-2023` son 298 fotos de plato y barra,
 * `cowork-2do-piso` son 91 fotogramas del local VACÍO. Así que las dos escenas
 * se generaron con Nano Banana Pro y el método de Eli
 * (`clients/hilton/PROMPTS-DE-ELI.md`), pasándole como referencia la foto REAL
 * del segundo piso y las del vaso To Go vigente para que el logotipo llegue
 * impreso y no estampado. Prompts y tiradas descartadas, en
 * `scripts/between-concurso-s3-generar.py`.
 *
 * ⭐ El logotipo del vaso se revisó al 300 % en cada tirada, que es la regla
 * dura de la cuenta. Las tiradas 1 y 2 de la portada salieron mal —«COFREE &
 * BAƟ»— y se volvió a tirar con el candado escrito en el prompt. La tirada 3
 * dice **BƎTWEEN / COFFEE & BAR**, las dos líneas completas.
 *
 * ── LA TINTA ES CAFÉ, Y ESO SE MIDIÓ ─────────────────────────────────────
 * El criterio del manual: «bajo L≈120 va beige suelto; sobre L≈150 va café
 * suelto». La franja del titular mide, por tercios:
 *
 *     portada     215,9 · 208,9 · 196,9   → peor tercio 196,9
 *     escritorio  209,9 · 204,1 · 194,0   → peor tercio 194,0
 *
 * Las dos muy por encima de 150, así que **café suelto** en titular y lockup, y
 * la foto NO se oscurece (el manual lo prohíbe: si un texto no se lee, va en
 * caja taupe, no se apaga la foto).
 *
 * ── SIN LOCKUP EN LA SLIDE 2 ─────────────────────────────────────────────
 * «En carrusel el logo va SOLO en la portada» (gramática §5). En la 2 firma la
 * tarjeta, con el avatar de marca y el handle — igual que en `C1 S2 CUMPLE N2`.
 *
 * ── LA REJILLA (1080×1350, se entrega a 2250×2813) ───────────────────────
 * El hueco limpio se MIDIÓ sobre las dos fotos ya recortadas, franja por franja
 * (`scripts/between-concurso-s3-fotos.py` y la bitácora del 16-09):
 *
 *   PORTADA        libre a todo el ancho hasta y≈550; hasta x≈646 entre 550 y
 *                  700; hasta x≈350 entre 700 y 950. Por eso el bloque
 *                  secundario va ANCLADO A LA IZQUIERDA y no centrado: una caja
 *                  taupe centrada de ~600 px de ancho aterrizaba sobre la cara
 *                  de la persona, y «ningún texto sobre rostros» es regla dura.
 *                  El anclaje a la izquierda no es una excepción inventada: la
 *                  gramática §4 ya lo tiene («o ancladas abajo a la izquierda,
 *                  que es lo que hace el feed real»).
 *   ESCRITORIO     libre a todo el ancho hasta y≈1000. La tarjeta cabe entera
 *                  encima del recorte del escritorio.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
import {CajaDato, FotoFondo, TitularBetween, useFuentesListas} from './BetweenSistema';
import {Trazo} from './BetweenTrazosConcurso';

const F = 'assets/hilton/between/concurso-s3/';

/**
 * ⭐⭐ UN CARRUSEL, UN CUERPO DE TITULAR.
 *
 * `TitularBetween` achica cada pieza POR SU CUENTA hasta que la línea más larga
 * entre en la columna (810). Dejado así, este carrusel salía con la portada en
 * **117** y la slide 2 en **103** —medido sobre los renders: caja alta de 84,0 y
 * de 74,2 px de tinta—, o sea que al deslizar el titular cambiaba de tamaño.
 * Es exactamente lo que Eli marcó como «desproporcionado» en el carrusel Cowork
 * el 01-09 (manual § LA COLUMNA: «el carrusel salió con TRES cuerpos de titular
 * distintos»).
 *
 * 103 es el cuerpo al que entra la línea MÁS LARGA de todo el carrusel
 * —«EMPIEZA AHORA», 778 px de tinta— dentro de la columna. Se fija a mano en
 * las dos láminas y no se deja al autoescalado.
 */
const CUERPO_TITULAR = 103;

/**
 * ⛔ EL LOGO EN CAFÉ NO SALE DE `BETWEEN.logo.cafe`: ese token apunta a
 * `logo-negro.png`, que es negro puro `#000000` y está fuera de paleta. El
 * archivo correcto es el que dejó la S3. El token del kit no se toca porque lo
 * usan piezas ya aprobadas (misma razón que `columnaTitular`).
 */
const LOGO_CAFE = 'assets/hilton/between/logo-cafe-marca.png';
const LOGO_BEIGE = 'assets/hilton/between/logo-blanco.png';

/** Lockup café en la geometría `postLogoArriba` de Eli (y=93, ancho 263). */
const LockupCafe: React.FC = () => {
  const g = BETWEEN.margenes.postLogoArriba;
  return (
    <Img
      src={staticFile(LOGO_CAFE)}
      style={{
        position: 'absolute',
        left: (1080 - g.ancho) / 2,
        top: g.wordmarkY,
        width: g.ancho,
        height: g.ancho / BETWEEN.logo.ratio,
        objectFit: 'contain',
      }}
    />
  );
};

/**
 * ⭐ EL SELLO «CONCURSO» — lo pide el brief con estas palabras: «agregar un
 * pequeño recurso tipo sello o etiqueta que diga CONCURSO».
 *
 * No es un motivo nuevo: es la **caja taupe de la marca** —mismo fondo
 * `#675B49`, mismo radio 16, misma caja alta en Raleway ExtraBold beige—
 * puesta de etiqueta y girada 4°. Dibujar un sello de verdad (anillo, dientes,
 * tipografía en arco) sí habría sido inventarle un recurso a Between, que es
 * justo lo que el manual prohíbe.
 *
 * Va arriba a la IZQUIERDA, en el margen de marca (x=84) y centrado sobre la
 * línea óptica del lockup, que es la posición del rótulo de la REF 1
 * («CUATRO CUATRO STUDIO» a la izquierda, con el año a la derecha).
 */
const SelloConcurso: React.FC<{y: number}> = ({y}) => {
  useFuentesListas();
  return (
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        top: y,
        height: 54,
        padding: '0 30px',
        display: 'flex',
        alignItems: 'center',
        backgroundColor: BETWEEN.cajas.fondo,
        borderRadius: BETWEEN.cajas.radio,
        transform: 'rotate(-4deg)',
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: BETWEEN.pesos.extrabold,
        fontSize: 28,
        lineHeight: 1,
        letterSpacing: '0.16em',
        /* el tracking se aplica TAMBIÉN después de la última letra y corre la
           caja hacia la izquierda; se devuelve con text-indent (memoria
           `tracking-no-llega-a-inline-block`) */
        textIndent: '0.16em',
        color: BETWEEN.colores.beige,
      }}
    >
      CONCURSO
    </div>
  );
};

/* ══════════════════════════════════════════════════════════════════════════
   SLIDE 1 · «SE BUSCA: CEO DEL CAFÉ»

   Textos LITERALES del brief. La única libertad es la caja tipográfica: la
   script de Between va en caja baja («¿Estás de cumpleaños?» en la pieza
   aprobada), así que «SE BUSCA:» se pinta «Se busca:». El punto final de
   «1 MES DE CAFÉ GRATIS.» no entra a la caja taupe: los títulos de esta marca
   no llevan punto final (regla de Eli, `sinPuntoFinal`).
   ══════════════════════════════════════════════════════════════════════════ */
export const C1S3Concurso1: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: '#e8ded2'}}>
    {/* `oscurecer` 0: la pared mide L≈207 y el titular va en café. Oscurecer una
        foto para que se lea un texto está prohibido en esta marca. */}
    <FotoFondo src={F + 'c1-portada.jpg'} oscurecer={0} />

    <LockupCafe />
    <SelloConcurso y={108} />

    {/* EL TITULAR — centrado sobre el eje, en la columna 810.
        Arranca en y=257: el lockup cierra en 93 + 263/3,0298 = 180 y el aire
        logo→texto medido en las plantillas de Eli es 77. */}
    <div
      style={{
        position: 'absolute',
        left: (1080 - BETWEEN.bloque.columna) / 2,
        width: BETWEEN.bloque.columna,
        top: 257,
      }}
    >
      <TitularBetween
        script="Se busca:"
        caps="CEO del café"
        sizeCaps={CUERPO_TITULAR}
        tono="cafe"
        alinear="centro"
        anchoDisponible={BETWEEN.bloque.columna}
      />
    </div>

    {/* EL BLOQUE SECUNDARIO — anclado a la IZQUIERDA (ver la cabecera).
        Ancho tope 540: a partir de y≈550 la pared limpia llega hasta x≈646, y
        84 + 540 = 624 deja 22 px de aire contra el recorte. */}
    <div style={{position: 'absolute', left: BETWEEN.bloque.margenX, top: 556, width: 540}}>
      <div
        style={{
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.semibold,
          fontSize: 44,
          lineHeight: 1,
          color: BETWEEN.colores.cafe,
          marginBottom: 18,
        }}
      >
        ¿El sueldo?
      </div>
      <div style={{display: 'flex'}}>
        <CajaDato anchoDisponible={540}>1 MES DE CAFÉ GRATIS</CajaDato>
      </div>
      {/* La CTA del brief, literal. Va bajo la pila porque es el remate del
          bloque: en y=730 la pared limpia todavía llega a x≈383 y la línea
          mide ~330. */}
      <div
        style={{
          marginTop: 26,
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.bold,
          fontSize: 32,
          lineHeight: 1.1,
          letterSpacing: '0.01em',
          color: BETWEEN.colores.cafe,
        }}
      >
        Postula aquí → Desliza
      </div>
    </div>

    {/* ⭐ RONDA 2 (16-09) — Eli: «solo un poco ambas, añade esas ilustraciones
        sencillas de la slide 2». En la PORTADA van sólo dos, y en el beige
        limpio: el mapa de la foto deja libre todo el ancho hasta y≈640 y hasta
        x≈650 entre 640 y 840.
          · la chispa arriba a la derecha, en la esquina que el titular no usa;
          · las cuñas junto al vaso, que es el gesto que tienen en la REF 2
            (ahí van pegadas a la cabeza del sujeto).
        Ninguna toca el producto ni cruza el margen de 84.
        ⚠️ Las cuñas estuvieron primero en (318, 628) y caían ENCIMA de la caja
        taupe —que va de y=612 a 678 y de x=84 a ~620—, partiendo la palabra
        «CAFÉ». Van al canal de la derecha, en la franja libre que queda entre
        el titular (cierra en ~450) y la figura (entra en y≈640). */}
    <Trazo cual="chispa" x={892} y={286} ancho={62} />
    <Trazo cual="cunas" x={676} y={516} ancho={94} giro={-12} opacidad={0.92} />
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   SLIDE 2 · LA DINÁMICA, EN LA TARJETA

   La tarjeta es la de `C1 S2 CUMPLE N2` —crema `#fff9eb`, filas taupe con
   casilla ✓, avatar de marca y handle—, que es lo que Eli aprobó y lo que el
   cliente ya vio publicado. Acá no lleva ventana de foto: la foto que pide el
   brief («una taza de Between sobre una mesa, acompañada de elementos de
   oficina tipo libreta, lápiz, notebook o credencial») es el recorte del
   escritorio que está DETRÁS, al pie de la pieza. Meter además una ventana
   habría puesto dos mesas en la misma lámina.
   ══════════════════════════════════════════════════════════════════════════ */

/** Geometría de la tarjeta, medida sobre `C1 S2 CUMPLE N2.png` (valores @1080):
 *  marco x 197–883 → ancho 686 · relleno 30 · filas de ancho útil 626. */
const CARD = {ancho: 686, relleno: 28, casilla: 40, cuerpoFila: 28};

const Rotulo: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.extrabold,
      fontSize: 22,
      lineHeight: 1,
      letterSpacing: '0.16em',
      textIndent: '0.16em',
      color: 'rgba(103,91,73,0.65)',
    }}
  >
    {children}
  </div>
);

const FilaCheck: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      width: CARD.ancho - CARD.relleno * 2,
      boxSizing: 'border-box',
      background: 'rgba(103,91,73,0.93)',
      borderRadius: 14,
      padding: '12px 16px',
      display: 'flex',
      alignItems: 'center',
      gap: 14,
    }}
  >
    <div
      style={{
        flexShrink: 0,
        width: CARD.casilla,
        height: CARD.casilla,
        borderRadius: 9,
        border: `3px solid ${BETWEEN.colores.beige}`,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: 24,
        lineHeight: 1,
        color: BETWEEN.colores.beige,
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: BETWEEN.pesos.extrabold,
      }}
    >
      ✓
    </div>
    <div
      style={{
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: BETWEEN.pesos.semibold,
        fontSize: CARD.cuerpoFila,
        /* MEDIDO en la lámina aprobada: con el tracking por defecto la fila
           salía 3,6 % más suelta que la de Eli. */
        letterSpacing: '-0.015em',
        lineHeight: 1.28,
        color: '#ffffff',
      }}
    >
      {children}
    </div>
  </div>
);

const Separador: React.FC = () => (
  <div style={{height: 1, background: 'rgba(103,91,73,0.22)', margin: '18px 0'}} />
);

export const C1S3Concurso2: React.FC = () => {
  useFuentesListas();
  return (
    <AbsoluteFill style={{backgroundColor: '#e8ded2'}}>
      <FotoFondo src={F + 'c1-escritorio.jpg'} oscurecer={0} />

      {/* EL TITULAR — sin script: la script es la marca de la PORTADA y las
          slides interiores bajan a un solo alfabeto (orden de Eli del 01-09
          para el carrusel Cowork). */}
      <div
        style={{
          position: 'absolute',
          left: (1080 - BETWEEN.bloque.columna) / 2,
          width: BETWEEN.bloque.columna,
          top: 150,
        }}
      >
        <TitularBetween
          caps={'Tu entrevista\nempieza ahora'}
          sizeCaps={CUERPO_TITULAR}
          tono="cafe"
          alinear="centro"
          anchoDisponible={BETWEEN.bloque.columna}
        />
      </div>

      {/* LA TARJETA */}
      <div
        style={{
          position: 'absolute',
          left: (1080 - CARD.ancho) / 2,
          top: 320,
          width: CARD.ancho,
          boxSizing: 'border-box',
          background: BETWEEN.colores.beige,
          borderRadius: 10,
          padding: CARD.relleno,
          boxShadow: '0 22px 54px rgba(60,44,28,0.20)',
        }}
      >
        {/* cabecera — avatar café con el logo beige adentro, el handle y los
            tres puntos. Es la que firma la lámina: acá no va lockup. */}
        <div style={{display: 'flex', alignItems: 'center', gap: 16}}>
          <div
            style={{
              width: 58,
              height: 58,
              borderRadius: '50%',
              background: BETWEEN.colores.cafe,
              boxShadow: `0 0 0 3px ${BETWEEN.colores.beige}, 0 0 0 6px ${BETWEEN.colores.cafe}`,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              overflow: 'hidden',
              flexShrink: 0,
            }}
          >
            <Img src={staticFile(LOGO_BEIGE)} style={{width: '76%', objectFit: 'contain'}} />
          </div>
          <div
            style={{
              fontFamily: BETWEEN.fuentes.sans,
              fontWeight: BETWEEN.pesos.bold,
              fontSize: 32,
              color: '#3b2f24',
            }}
          >
            between.coffeebar
          </div>
          <div style={{marginLeft: 'auto', color: '#3b2f24', fontSize: 30, letterSpacing: 3}}>
            •••
          </div>
        </div>

        <Separador />

        <Rotulo>COMPLETA EN LOS COMENTARIOS</Rotulo>
        <div
          style={{
            marginTop: 14,
            fontFamily: BETWEEN.fuentes.sans,
            fontWeight: BETWEEN.pesos.bold,
            fontSize: 36,
            lineHeight: 1.24,
            letterSpacing: '-0.012em',
            color: BETWEEN.colores.cafe,
          }}
        >
          «Si yo fuera CEO de Between,<br />mi primera acción sería…»
        </div>

        <Separador />

        <Rotulo>PARA PARTICIPAR</Rotulo>
        <div style={{display: 'flex', flexDirection: 'column', gap: 11, marginTop: 13}}>
          <FilaCheck>Sigue a @between.coffeebar</FilaCheck>
          <FilaCheck>Déjanos tu respuesta</FilaCheck>
          <FilaCheck>Etiqueta a tu mano derecha</FilaCheck>
        </div>

        {/* EL LEGAL, literal del brief, DENTRO de la tarjeta.
            ⚠️ No va al pie de la lámina, y la razón está medida: el recorte del
            escritorio ocupa de y≈950 hacia abajo y el vaso —con su logotipo
            impreso— va de 990 a 1341. Un legal al pie cruzaba el vaso y le
            partía el wordmark, que es el peor error posible en esta cuenta
            (manual § «el garabato no toca el producto»). Dentro de la tarjeta
            cae sobre crema y se lee a la primera. */}
        <div style={{height: 1, background: 'rgba(103,91,73,0.22)', margin: '18px 0 14px'}} />
        <div
          style={{
            fontFamily: BETWEEN.fuentes.sans,
            fontStyle: 'italic',
            fontWeight: BETWEEN.pesos.semibold,
            fontSize: 21,
            lineHeight: 1.34,
            color: 'rgba(103,91,73,0.85)',
          }}
        >
          <div>Concurso válido desde el 21 hasta el 30 de septiembre de 2026.</div>
          <div>El ganador será anunciado el 1 de octubre de 2026.</div>
        </div>
      </div>

      {/* ⭐ RONDA 2 (16-09) — «la segunda slide no se parece mucho a esta
          referencia 2 […] añade esas ilustraciones sencillas».
          La tarjeta mide 686 y deja 197 px de beige a cada lado; con el margen
          de marca en 84, el canal útil es de 113 px por lado. Los cuatro
          motivos van ahí y en la franja de arriba, rodeando la tarjeta como en
          el referente — nunca encima de ella ni sobre el escritorio.
          ⚠️ La flecha de abajo a la izquierda APUNTA a la tarjeta: en la REF 2
          las flechas son lo que ata los pedazos del collage. */}
      {/* ⚠️ Estuvieron en (900, 236) y tocaban la «A» final de «AHORA»: el titular
          llega a x≈928 y cierra en y≈325. Bajan al canal derecho, ya libre. */}
      <Trazo cual="cunas" x={898} y={372} ancho={90} giro={10} />
      <Trazo cual="chispa" x={104} y={398} ancho={68} />
      <Trazo cual="estrella" x={916} y={608} ancho={58} opacidad={0.9} />
      <Trazo cual="flecha" x={96} y={700} ancho={100} giro={-8} opacidad={0.92} />
    </AbsoluteFill>
  );
};
