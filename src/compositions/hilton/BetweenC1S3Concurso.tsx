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
export type SelloVariante = 'taupe' | 'tag' | 'caja' | 'cajaXL' | 'cajaXLtaupe';

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
  /**
   * ⭐ RONDA 7 (21-09) — Eli: «el texto del concurso podría ir un poco más
   * destacado […] que destaque más porque es un concurso que tiene que
   * destacar». El cuerpo sube de 52 a **68** (+31 %) y la caja de 84 a 96.
   * El alto no es libre: son los mismos ~24 px de aire por lado que tiene la
   * caja de 52, o la caja se ve inflada.
   * A 68 mide 515 px de ancho, contra los 419 del titular nuevo — o sea que el
   * rótulo pasa a ser el objeto más ancho de la lámina, que es lo que se pidió.
   */
  cajaXL: {alto: 96, cuerpo: 68, padX: 36, track: 0.1, giro: 0,
           fondo: BETWEEN.colores.beige, tinta: BETWEEN.colores.cafe},
  /**
   * La misma caja, invertida. Contra el papel `#DFC9BB` el taupe da **4,08:1**
   * y el beige **1,51:1**: si «destacar» se mide como salto contra el fondo,
   * ésta es la que lo da. Va a revisión junto con la beige.
   * ⚠️ Repite el color de la caja «1 MES DE CAFÉ GRATIS», que es lo que la
   * ronda 5 había resuelto separando los dos colores. Hoy los distingue el
   * tamaño (68 contra 45) y el sticker beige del titular entremedio.
   */
  cajaXLtaupe: {alto: 96, cuerpo: 68, padX: 36, track: 0.1, giro: 0,
                fondo: BETWEEN.cajas.fondo, tinta: BETWEEN.colores.beige},
};

/**
 * ⭐⭐⭐ EL RÓTULO SUELTO — RONDA 8 (21-09), y es el cambio que pidió Eli:
 *
 *   «Que el concurso, la letra del concurso, se mantenga café, pero **borra el
 *    recuadro beige que tiene, para que destaque mucho más**. Un poco más
 *    grande el texto del concurso. Necesito que se vea más grueso, más grande,
 *    incluso como la referencia.»
 *
 * Es lo contrario de lo que venía haciendo la pieza desde la ronda 4 —donde el
 * sello era una CAJA— y tiene su lógica: una caja beige sobre un papel beige
 * aporta 1,50:1 de salto, o sea casi nada; lo que estaba haciendo destacar a la
 * palabra era el contorno de la caja, no la palabra. **Sacada la caja, la que
 * trabaja es la tipografía**, y ahí sí se puede crecer sin que el objeto se
 * coma la lámina: el texto pasa de 68 a 104 y de ExtraBold (800) a
 * **Black (900)**, que es el peso del titular de la `REF 1`.
 *
 * A 104 en Black mide 610 px de tinta, contra los 480 del titular nuevo: manda
 * por tamaño, por peso y por posición, con 4,17:1 contra el papel — casi tres
 * veces el contraste que daba la caja beige.
 *
 * ⛔ El Black es del RÓTULO, no del titular. El titular de Between es ExtraBold
 * y eso está medido (manual § la gramática: «el peso del titular era Black
 * (900). Es ExtraBold (800)» fue uno de los errores que hundió una grilla).
 */
const RotuloConcurso: React.FC<{y: number; cuerpo: number}> = ({y, cuerpo}) => {
  useFuentesListas();
  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: y,
        textAlign: 'center',
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: 900,
        fontSize: cuerpo,
        lineHeight: 1,
        letterSpacing: '0.02em',
        textIndent: '0.02em',
        color: BETWEEN.colores.cafe,
      }}
    >
      CONCURSO
    </div>
  );
};

/**
 * ⭐⭐ EL TITULAR DENTRO DE LA CAJA PLANA — RONDA 8, opción «caja».
 *
 * Eli: «que quede como el texto de **“menos organizar mis archivos”**, con ese
 * tipo de recurso. Quiero ver esa opción. Y uno como el que dice **“estoy
 * haciendo de todo…”**. Esas dos opciones.»
 *
 * Son, literal, los dos recursos de la `REF 1` — y ahí están repartidos así:
 * el de arriba va con CONTORNO y el de abajo dentro de una CAJA PLANA RELLENA,
 * con la tinta clara sobre el color saturado. Esta es la segunda.
 *
 * Por eso la caja va **taupe con tinta beige** y no al revés: en el referente
 * lo que hace la caja es meter un bloque de color lleno en la lámina. Con caja
 * beige sería otra vez 1,50:1 contra el papel, que es el problema que acabamos
 * de sacar del rótulo.
 *
 * ⚠️ Repite el color de «1 MES DE CAFÉ GRATIS». En el referente pasa lo mismo
 * —la caja y el titular son del mismo azul— y lo que las separa es el tamaño:
 * 72 contra 45.
 *
 * La script queda FUERA de la caja, suelta y en café, como en el referente:
 * ahí la caja envuelve una sola línea de mensaje, no el bloque entero.
 */
const TitularEnCaja: React.FC<{
  y: number;
  cuerpo: number;
  /** La línea de arriba en Raleway en vez de Brushwell (opción `cajaSans`). */
  sans?: boolean;
  /** Halo del sticker para la línea de arriba. */
  halo?: number;
  /** Cuerpo de la línea de arriba; por defecto, la proporción de la script. */
  cuerpoScript?: number;
  /**
   * ⭐⭐ EL ÁNGULO DE LA CAJA — RONDA 9 (21-09). Eli: «ese texto en cajita con un
   * **leve ángulo como la referencia**».
   *
   * Se MIDIÓ sobre la `REF 1` en vez de estimarlo: aislando el azul de la caja
   * y ajustando sus bordes por mínimos cuadrados, el borde superior da −2,20° y
   * el inferior −3,34° (`between-concurso-s3-medir.py angulo-ref`). Se toma **−3°**, que cae dentro del rango
   * medido y coincide con el registro que la marca ya usa en sus etiquetas
   * (el sello de la ronda 4 gira −4°).
   *
   * ⚠️ `transform` NO cambia la caja del layout: la caja rotada sobresale
   * `ancho·sen(giro)/2` por arriba y por abajo —12 px acá— y eso hay que
   * descontarlo del aire, o la caja se le acerca a «¿El sueldo?» más de lo que
   * dicen los números.
   */
  giro?: number;
  /** Aire entre la línea de arriba y el canto de la caja. */
  aireCaja?: number;
  /**
   * ⭐ RONDA 10 — Eli: «deja puntas rectas a la caja del CEO».
   * Es lo que hace la `REF 1`: su bloque de color no tiene radio. El radio de
   * la marca (16) se queda para las cajas de dato, que sí lo llevan.
   */
  radio?: number;
  /**
   * Relleno vertical de la caja, como fracción del cuerpo. El de la marca es
   * 0,23 —`CajaDato` mide 66 de alto con cuerpo 45— y ése es el que vale.
   */
  padV?: number;
}> = ({y, cuerpo, sans = false, halo = 0, cuerpoScript, giro = 0, aireCaja, padV = 0.28,
       radio = BETWEEN.cajas.radio}) => {
  useFuentesListas();
  return (
    <div style={{position: 'absolute', left: 0, right: 0, top: y, display: 'flex',
                 flexDirection: 'column', alignItems: 'center'}}>
      <TitularBetween
        script="Se busca:"
        scriptSans={sans}
        pesoCaps={sans ? BETWEEN.pesos.extrabold : undefined}
        sizeScript={cuerpoScript ?? Math.round(cuerpo * BETWEEN.proporcionScript)}
        contorno={halo}
        tono="cafe"
        alinear="centro"
        anchoDisponible={BETWEEN.bloque.columna}
      />
      <div
        style={{
          marginTop: aireCaja ?? BETWEEN.aire.scriptATitulo,
          transform: giro ? `rotate(${giro}deg)` : undefined,
          padding: `${Math.round(cuerpo * padV)}px ${Math.round(cuerpo * 0.47)}px`,
          backgroundColor: BETWEEN.cajas.fondo,
          borderRadius: radio,
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.extrabold,
          fontSize: cuerpo,
          lineHeight: 1,
          letterSpacing: `${BETWEEN.trackingCaps}em`,
          textIndent: `${BETWEEN.trackingCaps}em`,
          color: BETWEEN.colores.beige,
          whiteSpace: 'nowrap',
        }}
      >
        CEO DEL CAFÉ
      </div>
    </div>
  );
};

const SelloConcurso: React.FC<{
  variante: SelloVariante;
  x?: number;
  y: number;
  /** Centra la caja sobre el eje en vez de anclarla a `x` (jerarquía `A`). */
  centrado?: boolean;
}> = ({
  variante,
  x = BETWEEN.bloque.margenX,
  y,
  centrado = false,
}) => {
  useFuentesListas();
  const v = SELLO[variante];
  return (
    <div
      style={{
        position: 'absolute',
        left: centrado ? '50%' : x,
        top: y,
        height: v.alto,
        padding: `0 ${v.padX}px`,
        display: 'flex',
        alignItems: 'center',
        backgroundColor: v.fondo,
        borderRadius: BETWEEN.cajas.radio,
        transform: [centrado ? 'translateX(-50%)' : '', v.giro ? `rotate(${v.giro}deg)` : '']
          .filter(Boolean)
          .join(' ') || undefined,
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
/* Sólo para la lámina de la ronda 5: las cajas grandes de la ronda 7 ya no
   encabezan la pila, así que su valor es el mismo y nunca se usa. */
const PILA: Record<SelloVariante, number> = {taupe: 556, tag: 556, caja: 594,
                                            cajaXL: 594, cajaXLtaupe: 594};

/* ══════════════════════════════════════════════════════════════════════════
   ⭐⭐⭐ RONDA 6 (21-09-2026) — CONTENIDO REORDENA LA JERARQUÍA DE LA PORTADA

   Nicolás Ávila, por Slack, con Scarlette en copia y a pedido del cliente:

     «Nos pidieron algunos cambios para el carrusel del concurso. Son
      principalmente ajustes de texto […] La idea es darle mayor relevancia a
      la efeméride. […] Sí, dejaría como principal CONCURSO, para que se
      entienda de inmediato que es un concurso y que deben participar. Después,
      como segunda jerarquía, las bajadas: SE ACERCA EL DÍA INTERNACIONAL DEL
      CAFÉ Y SE ABRIÓ LA VACANTE MÁS IMPORTANTE. Y desde ahí seguiría con
      "SE BUSCA: CEO DEL CAFÉ" y los otros textos.»

   O sea que no es un texto que se agrega: es el ORDEN DE LECTURA de la lámina
   el que cambia.

     hoy (ronda 5)          Se busca: CEO DEL CAFÉ · CONCURSO · ¿El sueldo? …
     lo que pide contenido  CONCURSO · bajada · Se busca: CEO DEL CAFÉ · …

   ⚠️ Esto MUEVE la decisión que tomó Eli en la ronda 5 —la caja beige grande
   encabezando la pila de la izquierda— porque ahora el sello sube a rótulo de
   la lámina. El tamaño que ella eligió (52) se conserva; lo que cambia es el
   sitio. La caja de la ronda 5 sigue viva en `jerarquia: 'ronda5'`.

   ── EL PRESUPUESTO VERTICAL, QUE ES LO QUE MANDA ─────────────────────────
   Medido sobre el render de la ronda 5 (1080×1350) y sobre el mapa de papel
   limpio de la foto (`between-concurso-s3-medir.py papel`, el mismo método de las rondas anteriores):

     · el lockup cierra su tinta en           y=180
     · la figura recortada —su halo blanco—
       entra en la columna izquierda en       y=850  (y el vaso, en x=478/y=868)
     · así que la última línea de la CTA
       no puede pasar de                      y=842

   Entre 180 y 842 hay **662 px** y adentro tienen que caber, con su aire:
   sello 84 + bajada 78 + titular + «¿El sueldo?» 44 + caja taupe 66 + CTA 78.
   La pila de abajo mide 228 px cerrada (medida sobre el render: 594→826).

   ⛔ Con el titular en los 103 de la ronda 5 quedan **80 px para cuatro aires**
   —20 px cada uno— y eso es una portada apretada, que es exactamente lo que
   Eli marca como «desordenado». Por eso las dos salidas que van a revisión no
   discuten el texto: discuten **QUÉ CEDE** para que la jerarquía nueva entre.

     A · APILADO    todo en el eje, como manda la gramática (§3 «todo
                    centrado»): sello centrado, bajada centrada de dos líneas
                    y el titular **baja de 103 a 88**. El titular cede 15 px y
                    a cambio la lámina conserva su eje y respira.
                    ⚠️ Un carrusel lleva UN cuerpo de titular, así que la
                    slide 2 baja con él (regla de la propia pieza, ronda 4).

     B · BANDA      el sello se queda a la izquierda y la bajada se le pone
                    AL LADO, en tres líneas, usando el papel limpio de la
                    derecha que hoy está vacío (x 507–996, y 218–343). Cuesta
                    117 px en vez de los 188 que cuesta apilarla, y con eso
                    **el titular se queda en 103**. Lo que cede es el eje: la
                    cabecera pasa a dos columnas.

   No es una elección de gusto: A obedece la jerarquía que pidió el cliente
   (el titular deja de ser lo más grande de la lámina); B protege el titular
   que ya está aprobado. Las dos van rendidas a la página de revisión.
   ══════════════════════════════════════════════════════════════════════════ */
export type Jerarquia = 'ronda5' | 'A' | 'B';

/**
 * ⭐ LA BAJADA — texto LITERAL de contenido, y la caja tipográfica es lo único
 * que se decide acá.
 *
 * Llega en versales («SE ACERCA EL DÍA INTERNACIONAL DEL CAFÉ Y SE ABRIÓ LA
 * VACANTE MÁS IMPORTANTE.») pero en esta marca las versales son del TITULAR y
 * de la caja taupe; una bajada va en caja baja y en Raleway Medium
 * (`BETWEEN.tipos.bajada`). Es la misma traducción que ya se le hizo a
 * «SE BUSCA:» → «Se busca:» en la ronda 1, y la que Eli pidió explícitamente
 * el 21-09 para la ST del 30-09 («que este texto sea en solo la primera
 * mayúscula»). El punto final se va: los remates de esta marca no lo llevan.
 *
 * ⚠️ EL CORTE DE LÍNEA SE COMPONE, NO SE DEJA AL NAVEGADOR. En `A` es el del
 * propio mensaje de contenido y deja dos líneas parejas (547 y 521 px de tinta
 * a 30, dentro de la columna de 810). En `B` la bajada vive en una caja de 489
 * px, así que el texto corrido dejaba «importante» sola en la tercera línea
 * —una viuda— y hubo que cortarlo a mano: 424 · 264 · 382, y los cortes caen
 * donde la frase respira, no donde cabe.
 */
const BAJADA = {
  A: ['Se acerca el Día Internacional del Café', 'y se abrió la vacante más importante'],
  B: ['Se acerca el Día Internacional', 'del Café y se abrió', 'la vacante más importante'],
} as const;

/**
 * La geometría de cada jerarquía, en px sobre el lienzo de 1080.
 *
 * `titular` es el cuerpo de la caja alta; la altura de TINTA del bloque
 * script+caps sale de medirlo: 192 px a 103, y escala lineal (88 → 164).
 * `pila` es el `top` del bloque de la izquierda, que ya NO encabeza el sello.
 */
const JERARQUIAS = {
  /* ⚠️ Estos números NO son los de la primera tirada: se corrigieron MIDIENDO
     el render. Con 218/324/424/614 la última línea de la CTA cerraba su tinta
     en y=844 y el halo blanco del recorte empieza en **y=847** (medido en
     `between-concurso-s3-medir.py holgura`, x 492–495): tres píxeles, o sea el texto apoyado en el
     sticker. La cabecera subió 17 px y la holgura quedó en 20, que es la que
     tiene la lámina aprobada de la ronda 5 (26).

     ⭐⭐ RONDA 7 (21-09) — Eli eligió la A y le pidió tres cosas, que son las
     que dan esta geometría:

       «el texto del concurso podría ir un poco más destacado»      → 52 → 68
       «el se acerca el Día Internacional […] aumentar el tamaño,
        porque se lee muy poco, no es tan visible»                  → 30 → 36
       «que se busca CEO del café esté en un marco beige […] como
        el sticker, igual que la referencia. Así se achica más»     → 88 → 64
                                                                      + contorno

     El presupuesto no cambió —del lockup (180) al techo de la CTA (827) hay
     647 px— pero ahora adentro hay MÁS objeto: caja 96 + bajada 94 + titular
     128 (119 de tinta + 8 de contorno, 4 por lado) + 230 de pila = 548, así
     que quedan **99 px para cuatro aires**. Se reparten 30 · 20 · 20 · 29: el
     rótulo, la bajada y el titular son UN bloque —aire interno 20— y el salto
     al mensaje es mayor, que es la jerarquía correcta (manual § jerarquía de
     un bloque de texto: el salto ENTRE niveles manda sobre el salto DENTRO). */
  /* ⭐⭐⭐ RONDA 8 (21-09) — el rótulo pierde la caja y el titular gana cuerpo.
     Sacada la caja beige (96 px de alto) entran los 104 del rótulo suelto (75
     de tinta) y sobran 21 px, que se reparten como aire. El presupuesto sigue
     siendo el mismo: del lockup (180) al techo de la CTA (827).

       sticker   180 + 26 + 75 + 26 + 94 + 26 + 144 + 26 + 230 = 827
       caja      180 + 20 + 75 + 20 + 94 + 20 + 166 + 22 + 230 = 827

     La de caja va más apretada porque el bloque mide 166 en vez de 144: la
     caja rellena le suma su propio relleno (28 px arriba y abajo), que es lo
     que hace que se lea como un objeto y no como una línea de texto. */
  A: {
    /* ⚠️ RONDA 9: el rótulo sube y la bajada baja porque con 22 px entremedio se
       leían pegados — bajo una palabra de 104 px eso es poco. El aire entre los
       dos niveles queda en 32, que es 1,5× el aire ENTRE LÍNEAS de la propia
       bajada (21), que es la proporción del manual.
       ⚠️ RONDA 10: la cajita del CEO crece de 54 a 60 y su bloque pasa de 96 a
       112 px de alto. Los 16 px salen de apretar los aires que NO son el de la
       jerarquía: el de arriba del rótulo (25→21), el de la bajada al bloque
       (25→20) y el interno del bloque (30→10, que además es lo que hace la REF,
       donde la caja monta sobre el texto). **El aire rótulo→bajada se mantiene
       en 32**: es el único que está atado a una proporción y no se negocia. */
    /* ⚠️ RONDA 11: Eli marcó el rótulo y la bajada —«están muy cerca del logo»—
       y bajaron 10 y 6 px, con el aire lockup→CONCURSO de 21 a 31.

       ⚠️⚠️ RONDA 12: no alcanzaba. Sobre el pantallazo marcó otra vez la flecha
       hacia abajo —«se está viendo muy muy junto el concurso al logo»— y pidió
       además **juntar «SE BUSCA:» con la cajita**, «así como está en la
       referencia, para que se entienda que es un texto junto».

       ⭐ Y el segundo pedido PAGA el primero: en la `REF 1` la caja monta sobre
       el texto, así que juntarlos de verdad —solape de 8 px— le devuelve al
       bloque 12 px de alto, que son exactamente los que necesitaba el rótulo
       para despegarse del logo. El aire lockup→CONCURSO queda en **46** sin
       mover la pila ni tocar el cuerpo de nada.

       Los cuatro aires quedan 46 · 30 · 20 · 18: el salto grande es el del
       logo, y de ahí para abajo el bloque se cierra de a poco, que es la
       jerarquía que pidió («todo bien ordenadito»). */
    selloY: 211, selloCentrado: true, selloVariante: 'cajaXL' as SelloVariante,
    selloSuelto: true, selloCuerpo: 104,
    bajadaY: 321, bajadaCuerpo: 36, bajadaAncho: BETWEEN.bloque.columna, bajadaCentrada: true,
    titularY: 425, titular: 72, contorno: 12,
    /* ⚠️ Cada estilo de titular tiene su propio `top` y su propio cuerpo, y los
       tres salen de MEDIR el render, no de estimarlos. Entre la bajada (cierra
       en y=400) y la pila (su tinta abre en 602) hay 202 px, y cada bloque los
       reparte distinto:
         sticker      135 de bloque → 33 de aire por lado
         stickerSans  110 de bloque (la línea en Raleway es más baja que la
                      Brushwell, que trae ascendentes y colas) → 46 por lado
         caja         148 de bloque a cuerpo 64 → 27 por lado
       ⛔ La primera tirada de `caja` iba a cuerpo 72 y dejaba **9 px** entre la
       caja del titular y «¿El sueldo?»: dos cajas casi tocándose. El cuerpo de
       esta opción es 64 y no 72 por eso — la caja rellena le suma 36 px de
       relleno propio que el sticker no tiene. */
    titularYSans: 437,
    titularYCaja: 420, titularCuerpoCaja: 64,
    /* ⭐ RONDA 9 — el híbrido, con los números CORREGIDOS sobre el render.
       La bajada cierra en 391 y la pila abre en 603: 212 px para el bloque.

       ⛔ La primera tirada calculó la caja con la CAJA ALTA del texto (43 px a
       cuerpo 60) y la caja medía 116, no 101: un `div` con `lineHeight: 1` mide
       el CUERPO entero, no la caja alta. La caja quedaba a 10 px de «¿El
       sueldo?». Con el cuerpo en 54 y el relleno de la marca (0,23 del cuerpo,
       que es el de `CajaDato`), la caja da 78 de alto y 385 de ancho, y rotada
       −3° ocupa 78 + 385·sen3° = **98**.

       El bloque queda: «SE BUSCA:» 37 + 16 de halo = 53, aire 12, caja 98 →
       163, con 25 px de aire arriba y 24 abajo. */
    /* ⭐ RONDA 12 — «juntes el se busca con el CEO del café, así como está en la
       referencia». `aireCajaSans` baja de 30 a 12, que sobre la tinta es un
       **solape de 8 px**: el canto de la caja entra bajo el halo de «SE BUSCA:»,
       igual que la caja azul de la REF 1 monta sobre su titular. Las dos líneas
       pasan a leerse como una sola frase. */
    titularYCajaSans: 436, titularCuerpoCajaSans: 60, aireCajaSans: 12, haloSans: 16,
    pila: 597,
  },
  B: {
    selloY: 218, selloCentrado: false, selloVariante: 'caja' as SelloVariante,
    selloSuelto: false, selloCuerpo: 52,
    bajadaY: 218, bajadaCuerpo: 30, bajadaAncho: 489, bajadaCentrada: false,
    titularY: 369, titular: 103, contorno: 0,
    titularYSans: 369, titularYCaja: 369, titularCuerpoCaja: 103,
    titularYCajaSans: 369, titularCuerpoCajaSans: 103, aireCajaSans: 9, haloSans: 0,
    pila: 587,
  },
} as const;

/** La bajada, en la caja baja de la marca y sin sombra: el papel es plano. */
const BajadaConcurso: React.FC<{
  x?: number; y: number; ancho: number; cuerpo: number; centrada: boolean;
  lineas: readonly string[];
}> = ({x, y, ancho, cuerpo, centrada, lineas}) => {
  useFuentesListas();
  return (
    <div
      style={{
        position: 'absolute',
        left: centrada ? (1080 - ancho) / 2 : x,
        top: y,
        width: ancho,
        fontFamily: BETWEEN.fuentes.sans,
        /* Medium (500): el token dice «bajada sin caja, Raleway Medium», y la
           Regular a este cuerpo se apaga contra un papel de L≈205. */
        fontWeight: 500,
        fontSize: cuerpo,
        /* 1,4 es el interlineado del componente `Bajada`, pensado para párrafo
           sobre foto. Acá son DOS líneas de una misma frase: 1,25 las mantiene
           como un bloque y no como dos renglones sueltos — y los 6 px que
           ahorra contra 1,30 son parte de lo que dejó bajar el rótulo en la
           ronda 11. */
        lineHeight: 1.25,
        letterSpacing: '0.005em',
        color: BETWEEN.colores.cafe,
        textAlign: centrada ? 'center' : 'left',
      }}
    >
      {lineas.map((l, i) => (
        <React.Fragment key={l}>
          {i ? <br /> : null}
          {l}
        </React.Fragment>
      ))}
    </div>
  );
};



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
export const C1S3Concurso1: React.FC<{
  sello?: SelloVariante;
  jerarquia?: Jerarquia;
  /**
   * ⭐ RONDA 7 — «que destaque más porque es un concurso que tiene que
   * destacar» admite dos lecturas y las dos van a revisión: crecer (beige, la
   * caja que Eli ya aprobó) o invertirse (taupe, que contra el papel salta de
   * 1,51:1 a 4,08:1). Sólo aplica cuando el sello es la caja grande.
   */
  selloTono?: 'beige' | 'taupe';
  /**
   * ⭐⭐ RONDA 8 — las tres lecturas del titular que pidió Eli, y las tres salen
   * de la `REF 1`:
   *
   *   `caja`         como «menos organizar mis archivos»: la caja plana
   *                  rellena, tinta clara sobre color saturado.
   *   `sticker`      como «ESTOY HACIENDO DE TODO…»: contorno pegado a las
   *                  letras, con la script en Brushwell.
   *   `stickerSans`  el mismo sticker pero con «Se busca:» en Raleway.
   *                  «Haz otra donde el se busca no sea Brushwell, tal vez con
   *                  eso se pueda ver mejor» — y es lo que hace el referente,
   *                  que resuelve sus dos líneas con UNA sola tipografía.
   *                  No es un recurso inventado: `scriptSans` ya existe y es el
   *                  que Eli aprobó para el carrusel Cowork el 01-09.
   */
  titularEstilo?: 'caja' | 'sticker' | 'stickerSans' | 'cajaSans';
}> = ({
  sello = 'caja',
  jerarquia = 'A',
  selloTono = 'beige',
  titularEstilo = 'sticker',
}) => {
  const r5 = jerarquia === 'ronda5';
  const J = JERARQUIAS[r5 ? 'A' : jerarquia];
  return (
  <AbsoluteFill style={{backgroundColor: FONDO_PAPEL}}>
    {/* `oscurecer` 0: el papel mide L≈205 y el titular va en café. Oscurecer una
        foto para que se lea un texto está prohibido en esta marca. */}
    <FotoFondo src={F + 'c1-portada-papel.jpg'} oscurecer={0} />

    <LockupCafe />

    {/* El sello.
        · ronda 5: en `taupe` y `tag` va en la línea óptica del lockup —centro 135
          contra el 136,5 del logotipo—; en `caja` encabeza la pila de la izquierda.
          En `tag` sube a 101 porque creció de 54 a 70 de alto y el centro manda.
        · rondas A y B: sube a RÓTULO de la lámina, que es lo que pidió contenido
          el 21-09. Mismo cuerpo que aprobó Eli (52) y misma caja beige; lo que
          cambia es el sitio, y en A además el eje.
        ⚠️ El giro NO saca la caja del margen: medido sobre el render, su canto
        izquierdo cae en x=84 exacto, igual que la caja taupe y la CTA. */}
    {!r5 && J.selloSuelto ? (
      <RotuloConcurso y={J.selloY} cuerpo={J.selloCuerpo} />
    ) : !r5 ? (
      <SelloConcurso
        variante={J.selloVariante === 'cajaXL' && selloTono === 'taupe' ? 'cajaXLtaupe' : J.selloVariante}
        y={J.selloY}
        centrado={J.selloCentrado}
      />
    ) : sello === 'caja' ? (
      <SelloConcurso variante="caja" y={492} />
    ) : (
      <SelloConcurso variante={sello} y={sello === 'tag' ? 101 : 108} />
    )}

    {/* LA BAJADA — segunda jerarquía, pedido de contenido del 21-09.
        En A va centrada bajo el sello, en dos líneas; en B va AL LADO del sello,
        en el papel limpio de la derecha (x 507–996), en tres. */}
    {!r5 ? (
      <BajadaConcurso
        x={507}
        y={J.bajadaY}
        ancho={J.bajadaAncho}
        cuerpo={J.bajadaCuerpo}
        centrada={J.bajadaCentrada}
        lineas={BAJADA[jerarquia === 'B' ? 'B' : 'A']}
      />
    ) : null}

    {/* EL TITULAR — centrado sobre el eje, en la columna 810.
        En la ronda 5 arranca en y=257: el lockup cierra en 93 + 263/3,0298 = 180
        y el aire logo→texto medido en las plantillas de Eli es 77. Con la
        jerarquía nueva el titular ya no abre la lámina y baja a su sitio. */}
    {!r5 && titularEstilo === 'caja' ? (
      <TitularEnCaja y={J.titularYCaja} cuerpo={J.titularCuerpoCaja} />
    ) : null}
    {/* ⭐⭐⭐ LA ELEGIDA — RONDA 9 (21-09). Eli: «quiero la opción 3, pero con lo
        del CEO ese texto en cajita con un leve ángulo como la referencia, y el
        se busca aumenta un poco el grosor del beige».
        O sea el híbrido: la línea de arriba de la opción 3 —Raleway, una sola
        tipografía, como el referente— y el bloque de color de la opción 1, que
        en la REF 1 va inclinado. El halo sube de 12 a **16**. */}
    {!r5 && titularEstilo === 'cajaSans' ? (
      <TitularEnCaja
        y={J.titularYCajaSans}
        cuerpo={J.titularCuerpoCajaSans}
        cuerpoScript={Math.round(J.titular * 0.72)}
        sans
        halo={J.haloSans}
        giro={-3}
        aireCaja={J.aireCajaSans}
        padV={0.23}
        radio={0}
      />
    ) : null}
    <div
      style={{
        position: 'absolute',
        left: (1080 - BETWEEN.bloque.columna) / 2,
        width: BETWEEN.bloque.columna,
        top: r5 ? 257 : titularEstilo === 'stickerSans' ? J.titularYSans : J.titularY,
        display: !r5 && (titularEstilo === 'caja' || titularEstilo === 'cajaSans')
          ? 'none'
          : undefined,
      }}
    >
      {/* ⭐⭐ EL TITULAR ES UN STICKER — RONDA 7 (21-09).
          Eli: «que se busca CEO del café sea el que esté en un marco beige […]
          que sea como el sticker, como igual que la referencia».
          En la `REF 1` el titular NO va en una caja rectangular: lleva un
          contorno claro pegado a las letras, y ése es el «marco». Se pinta con
          `contorno`, que es el recurso nuevo de `TitularBetween`.
          8 px es el grosor: 4 por fuera del glifo, que a un cuerpo de 64 es el
          mismo 6 % que tiene el contorno del recorte de la figura contra su
          propio ancho de trazo — así el titular y la foto se leen como piezas
          del mismo collage y no como dos recursos distintos. */}
      {/* ⚠️ En `stickerSans` la línea de arriba va al MISMO peso que el titular
          (ExtraBold) y no al Medium con que `scriptSans` la pinta por defecto:
          en la `REF 1` las dos líneas son del mismo peso y lo único que cambia
          es el tamaño, y con Medium el contorno de 12 px queda grueso contra un
          trazo liviano. El caps no se mueve: 800 ya es su peso. */}
      <TitularBetween
        script="Se busca:"
        scriptSans={titularEstilo === 'stickerSans'}
        pesoCaps={titularEstilo === 'stickerSans' ? BETWEEN.pesos.extrabold : undefined}
        caps="CEO del café"
        sizeCaps={r5 ? CUERPO_TITULAR : J.titular}
        contorno={r5 ? 0 : J.contorno}
        /* ⭐⭐ EL CONTORNO SE DESCUENTA DEL AIRE, Y ESO SE VIO AMPLIANDO EL
           RENDER. El aire medido entre la script y la caja alta es de 9 px de
           TINTA A TINTA — pero el contorno crece 6 px por lado, así que con 12
           px de trazo las dos líneas quedaban a −3: los contornos se montaban y
           la zona de encuentro se leía sucia. Se abre a 9 + 12 + 6 = 27, que
           deja los mismos 9 px de aire limpio que tiene la pieza aprobada. */
        aireScriptATitulo={!r5 && J.contorno
          ? BETWEEN.aire.scriptATitulo + J.contorno + 6
          : undefined}
        tono="cafe"
        alinear="centro"
        anchoDisponible={BETWEEN.bloque.columna}
      />
    </div>

    {/* EL BLOQUE SECUNDARIO — anclado a la IZQUIERDA (ver la cabecera).
        Ancho tope 540: a partir de y≈550 la pared limpia llega hasta x≈646, y
        84 + 540 = 624 deja 22 px de aire contra el recorte. */}
    <div style={{position: 'absolute', left: BETWEEN.bloque.margenX, top: r5 ? PILA[sello] : J.pila, width: 540}}>
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
      {/* ⭐⭐ RONDA 10 (21-09) — Eli, sobre esta caja: «invierte el color, el
          texto café y el fondo beige».
          Queda BEIGE con tinta café, y la taupe pasa a ser la del titular. No
          es un capricho de color: con las dos cajas del mismo taupe ninguna
          mandaba sobre la otra —es el defecto que la ronda 5 ya había
          diagnosticado en el sello— y ahora el énfasis macizo es del titular,
          que es el nivel de arriba. Medido: la caja beige da 1,50:1 contra el
          papel y 6,31:1 por dentro; el conjunto se lee por su tinta, no por su
          canto.
          ⚠️ Va por `style` y no tocando `CajaDato`: ese componente lo usan
          piezas ya aprobadas y su caja es taupe. */}
      <div style={{display: 'flex'}}>
        <CajaDato
          anchoDisponible={540}
          style={{backgroundColor: BETWEEN.colores.beige, color: BETWEEN.colores.cafe}}
        >
          1 MES DE CAFÉ GRATIS
        </CajaDato>
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
        así que no se movieron.
        ⚠️⚠️ RONDA 6: con la jerarquía nueva los dos motivos se MUEVEN, porque el
        canal que ocupaban ahora es del titular. No es decoración reubicada a
        ojo: en A flanquean el rótulo —el papel a los lados de la caja centrada
        (x 84–330 y 760–996, y 210–310) está limpio y no lo pisa nada—, y en B,
        donde la cabecera ocupa las dos columnas, bajan a los canales laterales
        que deja el titular (su tinta llega a x 203–878). */}
    {jerarquia === 'A' && !r5 ? (
      <>
        {/* ⭐⭐ RONDA 12 — EL GIRO SALE DE MEDIR EL GARABATO, NO DE LA REF.
            En la ronda 11 se dedujo el ángulo de la `REF 2` (+40°) y estaba al
            revés. Eli lo dibujó encima del pantallazo, así que esta vez se
            midió el trazo rojo: aislando el rojo y sacándole el eje principal a
            cada marca por PCA (`between-concurso-s3-medir.py rojo`), las tres dan **22°, 40° y 87°**
            contra los 67°, 88° y 120° del dibujo sin girar. La diferencia media
            es de **−42°**, y ése es el giro: el abanico se abre hacia
            arriba-IZQUIERDA, como un destello que sale de la palabra, no hacia
            la palabra.
            ⚠️ Rotadas ocupan x 104–222 e y 215–332: no cruzan el margen de 84
            ni tocan la «C» de CONCURSO, que abre en x≈235. */}
        <Trazo cual="cunas" x={116} y={237} ancho={94} giro={-42} opacidad={0.92} />
        <Trazo cual="chispa" x={892} y={249} ancho={62} />
      </>
    ) : null}
    {jerarquia === 'B' && !r5 ? (
      <>
        <Trazo cual="chispa" x={908} y={392} ancho={62} />
        {/* ⚠️ Las cuñas NO caben a la derecha del titular de 103: su tinta llega
            a x=878 y el halo del recorte entra en y=649, así que el hueco es de
            12 px. Se van al papel vacío de abajo a la izquierda, que la CTA
            deja libre desde y=817 y el recorte no toca hasta y≈974. */}
        <Trazo cual="cunas" x={110} y={848} ancho={94} giro={-12} opacidad={0.92} />
      </>
    ) : null}
    {r5 ? (
      <>
        <Trazo cual="chispa" x={892} y={286} ancho={62} />
        <Trazo cual="cunas" x={676} y={516} ancho={94} giro={-12} opacidad={0.92} />
      </>
    ) : null}
  </AbsoluteFill>
  );
};

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

export const C1S3Concurso2: React.FC<{jerarquia?: Jerarquia}> = ({jerarquia = 'A'}) => {
  useFuentesListas();
  /* ⭐⭐ POR QUÉ ESTA LÁMINA YA NO SIGUE EL CUERPO DE LA PORTADA — RONDA 7.
     La regla del carrusel es «un carrusel, un cuerpo de titular», y por eso en
     la ronda 6 esta slide bajó con la portada de 103 a 88. En la ronda 7 la
     portada mete su titular DENTRO de un sticker con contorno y lo baja a 64:
     ahí deja de ser «el titular suelto de la lámina» y pasa a ser un rótulo
     enmarcado, o sea otro objeto. La regla compara objetos iguales, así que no
     aplica — y Eli lo confirmó mirando: «en la segunda slide quedó perfecta».
     Se fija en los 88 que ella aprobó y no se deja colgando de la portada. */
  const cuerpo = jerarquia === 'ronda5' ? CUERPO_TITULAR : 88;
  void JERARQUIAS;
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
          sizeCaps={cuerpo}
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

        {/* ⭐ RONDA 6 (21-09-2026) — cambio de contenido, literal:
            «En la Slide 2, cambiar: "SI YO FUERA CEO DE BETWEEN" →
             "SI YO FUERA CEO DEL CAFÉ"».
            Es la frase que la gente copia en los comentarios, así que va tal
            cual la mandó contenido; lo único que se conserva es la caja baja de
            la tarjeta y el corte de línea, que no se movió porque la frase
            nueva es 2 caracteres más corta. */}
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
          «Si yo fuera CEO del café,<br />mi primera acción sería…»
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
