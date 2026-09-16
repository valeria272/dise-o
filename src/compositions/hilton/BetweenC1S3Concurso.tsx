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
 * ⭐ Con la hoja de papel de la ronda 4 (ver `FONDO_PAPEL`) la franja quedó
 * PAREJA, y ésa es la medida que manda ahora:
 *
 *     portada     203,7 · 204,7 · 205,7
 *     escritorio  204,7 · 204,7 · 202,7
 *
 * El peor tercio subió de 194,0 a 202,7 y la dispersión entre tercios bajó de
 * 19 niveles a 3, así que el café se lee igual en toda la línea y en las dos
 * láminas. La decisión de tinta no cambia.
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
 * ⭐⭐ EL FONDO ES UNA HOJA DE PAPEL, Y ES UNA SOLA PARA LAS DOS — RONDA 4 (16-09).
 *
 * Eli: «El fondo debe ser el mismo beige papel para ambas slides, que sea plano
 * y transicione.»
 *
 * Las dos escenas se generaron por separado y traían dos superficies distintas:
 * la portada, una pared lisa; la slide 2, un panel de **veta vertical de madera**
 * más rosado. La ronda 3 igualó la ILUMINACIÓN de las dos (salto en la costura
 * 18,7 → 0,95) pero no el MATERIAL, y eso es lo que ella siguió viendo.
 *
 * `scripts/between-concurso-s3-fondo-papel.py` cambia sólo la superficie de
 * atrás —el retrato y el bodegón no se re-generan, están aprobados— y lo hace
 * con UNA hoja sintetizada de 4500 px de ancho, cortada en dos. La continuidad
 * no se corrige: existe por construcción, porque la última columna de la portada
 * y la primera de la slide 2 son vecinas de la misma hoja.
 *
 * `FONDO_PAPEL` es el color de relleno bajo la imagen, y es el **tono exacto de
 * la hoja**: la mediana medida de las dos paredes aprobadas. Antes había un
 * `#e8ded2` puesto a ojo que no era el de ninguna de las dos.
 * Los contrastes, medidos: café del titular 4,17:1 · contorno blanco del recorte
 * 1,59:1 · tarjeta crema de la slide 2, 1,51:1.
 */
const FONDO_PAPEL = '#dfc9bb';

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
 * ⭐ LA POLAROID DE LA SLIDE 2 — RONDA 3 (16-09).
 *
 * Eli: «para el slide 2 añade la polaroid de foto de la misma chica de frente,
 * feliz, que es igual a la referencia del slide 2. Muy sutil, donde no tape
 * textos.»
 *
 * Es el último elemento que le faltaba a la REF 2 y el más literal de todos:
 * ahí hay una polaroid pegada abajo a la izquierda, ladeada, con un retrato de
 * la misma persona del recorte grande.
 *
 * ⚠️ El retrato es la MISMA mujer, no otra. Se generó pasándole como referencia
 * la portada aprobada y un recorte de su cara —que es la forma práctica de fijar
 * el personaje (memoria `generar-personas-nombrar-el-tipo`: «el perfil aprobado
 * se fija como referencia de personaje o cada generación da una cara distinta»).
 *
 * DÓNDE VA, y por qué ahí: es el único hueco de la lámina que no tiene texto ni
 * producto. Medido, el beige limpio de abajo a la izquierda llega hasta x≈270
 * entre y=1000 y y=1250, y el legal vive DENTRO de la tarjeta, así que acá no
 * hay nada que tapar. La esquina de la polaroid monta apenas sobre el canto del
 * escritorio, que es lo que hace el referente: en un collage las piezas se
 * solapan.
 *
 * La geometría es la de una polaroid de verdad: marco parejo arriba y a los
 * lados, y el pie MÁS ANCHO. Sin eso se lee como un marco blanco cualquiera.
 */
const POLAROID = {ancho: 188, marco: 12, pie: 34, x: 96, y: 1012, giro: -7};

const Polaroid: React.FC = () => {
  const anchoFoto = POLAROID.ancho - POLAROID.marco * 2;
  return (
    <div
      style={{
        position: 'absolute',
        left: POLAROID.x,
        top: POLAROID.y,
        width: POLAROID.ancho,
        padding: `${POLAROID.marco}px ${POLAROID.marco}px ${POLAROID.pie}px`,
        boxSizing: 'border-box',
        background: '#ffffff',
        transform: `rotate(${POLAROID.giro}deg)`,
        boxShadow: '0 10px 26px rgba(60,44,28,0.22)',
      }}
    >
      <Img
        src={staticFile(F + 'c1-polaroid-foto.jpg')}
        style={{width: anchoFoto, height: anchoFoto * 1.16, objectFit: 'cover', display: 'block'}}
      />
    </div>
  );
};

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
 * ⭐⭐ EL SELLO «CONCURSO» — RONDA 5 (16-09), pedido del cliente.
 *
 * Nicolás y Scarlette, sobre la portada: «darle más protagonismo a la palabra
 * CONCURSO. Que sea más grande y quizás usar otro tono de café, o algún recurso
 * visual que haga que destaque más y se vea llamativo de inmediato.»
 * Y Eli, en la misma vuelta: «haz una opción donde CONCURSO esté en una caja
 * beige más grande estilo la ref.»
 *
 * El origen del encargo sigue siendo el brief —«agregar un pequeño recurso tipo
 * sello o etiqueta que diga CONCURSO»— y el recurso sigue siendo el de la marca:
 * la caja de color plano de la REF 1. Lo que cambia es CUÁL de los dos colores
 * de Between va de fondo y cuál de tinta.
 *
 * ⛔ Por qué NO se inventó un café nuevo, que es lo que el cliente sugería como
 * primera vía: la paleta de Between son DOS tintas —beige `#FFF9EB` y café
 * `#675B49`— y un tercer marrón es cambiarle la paleta a la marca, no corregir
 * una pieza. La inversión da el mismo salto sin inventar nada, y encima resuelve
 * un defecto que el cliente estaba viendo sin nombrarlo: hoy el sello y la caja
 * del sueldo son **la misma caja taupe**, así que ninguna manda sobre la otra.
 * Medido contra el papel `#DFC9BB` de la hoja:
 *
 *   | | fondo vs papel | tinta dentro |
 *   |---|---|---|
 *   | sello taupe de hoy | 4,08:1 | beige sobre taupe, 6,31:1 |
 *   | caja beige nueva | 1,50:1 | **café sobre beige, 6,31:1** |
 *
 * El 1,50:1 de la caja no es un defecto: es exactamente el contraste de la
 * tarjeta crema de la N2, que Eli aprobó y el cliente ya vio. Una caja plana de
 * este tipo no se lee por su canto sino por la tinta que lleva dentro, y ésa es
 * la que crece: de 28 px de caja alta a **36** (tag) o **52** (caja).
 *
 * ── LAS DOS OPCIONES QUE VAN A REVISIÓN ──────────────────────────────────
 *
 * `tag`   — la etiqueta se queda donde está, en la línea del lockup y en el
 *           margen de marca, y sólo se invierte y crece. Cuerpo 36 (hoy 28),
 *           alto 70 (hoy 54). Es el cambio mínimo sobre una lámina aprobada.
 *           ⚠️ 36 es el TECHO de esta posición, y está medido: la caja da 287 px
 *           y el lockup arranca en x=408, así que con el giro quedan 32 px de
 *           aire. A 40 px el sello toca el logotipo.
 *
 * `caja`  — la caja plana grande de la REF 1, y por eso baja a la columna del
 *           mensaje: ahí no la limita el logotipo y el cuerpo puede llegar a 52.
 *           Encabeza la pila —CONCURSO · ¿El sueldo? · 1 MES DE CAFÉ GRATIS— y
 *           queda beige contra taupe, que es la pareja que da la jerarquía.
 *           Cabe sin apretar nada: el titular cierra en y=450, la figura entra
 *           en la columna izquierda en y=869, y la pila completa ocupa 480–823.
 *
 * En las dos, el giro de −4° del sello original se conserva sólo en el `tag`:
 * la caja plana de la REF 1 va derecha, y «plano» es la palabra que Eli usó para
 * el fondo de esta misma pieza.
 */
export type SelloVariante = 'taupe' | 'tag' | 'caja';

const SELLO = {
  /** El de la ronda 4, que es lo que el cliente está mirando. */
  taupe: {alto: 54, cuerpo: 28, padX: 30, track: 0.16, giro: -4,
          fondo: BETWEEN.cajas.fondo, tinta: BETWEEN.colores.beige},
  /** Invertido y más grande, en el mismo sitio. */
  tag: {alto: 70, cuerpo: 36, padX: 22, track: 0.12, giro: -4,
        fondo: BETWEEN.colores.beige, tinta: BETWEEN.colores.cafe},
  /** La caja plana de la REF 1, en la columna del mensaje. */
  caja: {alto: 84, cuerpo: 52, padX: 28, track: 0.1, giro: 0,
         fondo: BETWEEN.colores.beige, tinta: BETWEEN.colores.cafe},
};

const SelloConcurso: React.FC<{variante: SelloVariante; x?: number; y: number}> = ({
  variante,
  x = BETWEEN.bloque.margenX,
  y,
}) => {
  useFuentesListas();
  const v = SELLO[variante];
  return (
    <div
      style={{
        position: 'absolute',
        left: x,
        top: y,
        height: v.alto,
        padding: `0 ${v.padX}px`,
        display: 'flex',
        alignItems: 'center',
        backgroundColor: v.fondo,
        borderRadius: BETWEEN.cajas.radio,
        transform: v.giro ? `rotate(${v.giro}deg)` : undefined,
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: BETWEEN.pesos.extrabold,
        fontSize: v.cuerpo,
        lineHeight: 1,
        letterSpacing: `${v.track}em`,
        /* el tracking se aplica TAMBIÉN después de la última letra y corre la
           caja hacia la izquierda; se devuelve con text-indent (memoria
           `tracking-no-llega-a-inline-block`) */
        textIndent: `${v.track}em`,
        color: v.tinta,
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
/**
 * ⭐⭐ LA PILA DE LA IZQUIERDA — RONDA 5 (16-09).
 *
 * Con el sello en variante `caja` la pila arranca con CONCURSO y todo lo demás
 * baja 32 px. El presupuesto vertical está medido sobre la lámina rendida y no
 * estimado: el titular cierra su tinta en **y=450** y el recorte de la figura
 * entra en la columna izquierda (x 84–640) en **y=869**. En medio hay 419 px y
 * la pila completa —caja 84 + aire + «¿El sueldo?» + caja taupe + la CTA de dos
 * líneas— ocupa 480–823. Quedan 30 px de aire arriba y 46 abajo.
 *
 * El tope lateral tampoco se movió: el mapa de la foto deja limpio hasta x≈630
 * entre y=750 y y=849, y la línea más larga de la CTA nueva mide 435 px, así que
 * cierra en 519.
 */
const PILA = {taupe: 556, tag: 556, caja: 594} as const;

/**
 * ✅ ELI ELIGIÓ LA `caja` — RONDA 5, 16-09-2026. Es lo que se entrega.
 *
 * Se le pusieron las dos delante, rendidas y al tamaño de publicación
 * (`out/hilton/between/concurso-s3-r5/revision-r5.html`), y eligió la caja
 * grande: CONCURSO a **52 px**, +86 % contra los 28 de la ronda 4, en caja beige
 * plana encabezando la pila del mensaje.
 *
 * ⚠️ Yo había recomendado la otra —`tag`, la etiqueta invertida en la línea del
 * lockup— con el argumento de que el sello es el rótulo de la lámina y que
 * bajarlo lo pone a competir con el premio. Mandó ella, y la razón por la que
 * tenía razón queda escrita para la próxima: **el cliente pidió tamaño y `tag`
 * no lo daba**. En esa posición el techo son 36 px, porque el lockup arranca en
 * x=408 — y contra los 28 de hoy, 36 px no es un cambio que se vea «de
 * inmediato», que era literalmente lo que pedían. La posición que limita el
 * tamaño es la que se cede, no el tamaño.
 *
 * `tag` se queda en el archivo: es la variante correcta si alguna vez hay que
 * rotular una lámina de esta marca sin robarle sitio al mensaje.
 */
export const C1S3Concurso1: React.FC<{sello?: SelloVariante}> = ({sello = 'caja'}) => (
  <AbsoluteFill style={{backgroundColor: FONDO_PAPEL}}>
    {/* `oscurecer` 0: el papel mide L≈205 y el titular va en café. Oscurecer una
        foto para que se lea un texto está prohibido en esta marca. */}
    <FotoFondo src={F + 'c1-portada-papel.jpg'} oscurecer={0} />

    <LockupCafe />

    {/* El sello: en `taupe` y `tag` va en la línea óptica del lockup —centro 135
        contra el 136,5 del logotipo—; en `caja` encabeza la pila de la izquierda.
        En `tag` sube a 101 porque creció de 54 a 70 de alto y el centro manda.
        ⚠️ El giro NO saca la caja del margen: medido sobre el render, su canto
        izquierdo cae en x=84 exacto, igual que la caja taupe y la CTA. */}
    {sello === 'caja' ? (
      <SelloConcurso variante="caja" y={492} />
    ) : (
      <SelloConcurso variante={sello} y={sello === 'tag' ? 101 : 108} />
    )}

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
    <div style={{position: 'absolute', left: BETWEEN.bloque.margenX, top: PILA[sello], width: 540}}>
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
      {/* ⭐ LA CTA — RONDA 5 (16-09), texto LITERAL del cliente:
          «Cambiar el texto "POSTULA AQUÍ → DESLIZA" por: "¿Quieres el puesto? →
          Desliza para tu entrevista"».

          Va en DOS líneas y el corte cae en la flecha, que es la bisagra de la
          frase: arriba la pregunta, abajo la acción. A 32 px en Raleway Bold la
          frase entera mide 700 px y el canal limpio de esa franja termina en
          x≈630; partida, la línea larga mide 435 y cierra en 519.

          ⭐ El interlineado sube de 1,1 a 1,22 porque ahora hay DOS líneas: con
          1,1 la pregunta y la acción se leían como un párrafo pegado, y el salto
          dentro de un mismo nivel es lo que le da aire (manual § jerarquía).

          ⚠️ El remate enlaza con la slide 2, que se titula «TU ENTREVISTA
          EMPIEZA AHORA». No es casualidad y conviene no romperlo. */}
      <div
        style={{
          marginTop: 26,
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.bold,
          fontSize: 32,
          lineHeight: 1.22,
          letterSpacing: '0.01em',
          color: BETWEEN.colores.cafe,
        }}
      >
        ¿Quieres el puesto?
        <br />→ Desliza para tu entrevista
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
        el titular (cierra en ~450) y la figura (entra en y≈640).
        ⚠️ RONDA 5: con el sello en `caja` la pila baja 32 px y la caja taupe
        pasa a 653–719; las cuñas siguen en 516–589 y en el canal de la derecha,
        así que no se movieron. */}
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
    <AbsoluteFill style={{backgroundColor: FONDO_PAPEL}}>
      <FotoFondo src={F + 'c1-escritorio-papel.jpg'} oscurecer={0} />

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
      <Polaroid />
    </AbsoluteFill>
  );
};
