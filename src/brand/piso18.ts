/**
 * PISO18 Centro de Eventos — brand kit
 *
 * FUENTES DE VERDAD, en este orden:
 *   1. Lo DICTADO por Eli el 15-09-2026 (color, tipografías, logo, botones,
 *      rostros, verticales). Manda sobre cualquier medición.
 *   2. Las piezas APROBADAS del cliente, medidas:
 *        · `raw/hilton/piso18/ref-aprobadas/ST N°1 S1.png`            2250×4000
 *        · `raw/hilton/piso18/ref-aprobadas/carrusel-novios/C2 S1 n°*.png` 2250×2813
 *        · `raw/hilton/piso18/ref-aprobadas/Post-*-1.1-2026-SEP.jpg`  1080×1080
 *   3. Los `Informe.txt` de los `.ai` empaquetados (mesa de trabajo, cortes).
 *   4. `clients/hilton/CLAUDE.md` § «PISO18 — MARCA PROPIA».
 *
 * ⛔ REGLA MADRE DE LA CUENTA: **Piso18 es marca propia y nada de DT se le
 * traspasa** — ni tipografía, ni paleta, ni logo, ni banco, ni «LA LEY DE ELI»,
 * que se dictó para DoubleTree. Comparten edificio, no sistema gráfico.
 * Palabras de Eli: «Todo es propio y diferente a DT, recuerda no mezclar las marcas.»
 *
 * ⛔ Y al revés: el fucsia de acá NO es el de Selfie (`#FF007C`).
 *
 * ── Estado ────────────────────────────────────────────────────────────────
 * Escrito el 15-09-2026 al abrir la S4 (carrusel de arreglos florales + post de
 * noche + 3 historias). Cierra la capa 6 del sistema de marca, que no existía.
 * **Cada número dice de dónde sale.** Lo que no se midió, no está acá.
 */
import React from 'react';
import {staticFile} from 'remotion';

export const P18 = {
  colores: {
    /**
     * ⭐ Fucsia Piso18 — **lo entregó Eli el 15-09 y es el que manda.**
     * La firma de la marca: caja sólida del precio, filete del recuadro, el
     * `piso18.cl` del CTA, el destacado dentro de un titular, y los botones.
     *
     * ⚠️ Medir sobre los JPG aprobados daba `#D6145B` y `#D5135A` — a 2 de
     * distancia, que es exactamente el ruido de compresión. La medición sirve
     * para verificar, nunca para fijar.
     */
    fucsia: '#D4145A',
    /** Tinta sobre foto: logotipo, titulares y cifras. */
    blanco: '#FFFFFF',
    /**
     * Tinta oscura sobre la tarjeta blanca del cierre de carrusel.
     * Medido en `C2 S1 n°2` (el texto «No te quedes sin tu matrimonio 2027»).
     */
    tinta: '#1A1A1A',
    /** El papel de la tarjeta festoneada, medido en `C2 S1 n°2`. */
    tarjeta: '#F7F5F2',
    /**
     * ⭐ El BEIGE de fondo, pedido por Eli en la ronda 2 de la S4: *«al fondo
     * beige añade textura de papel sutil beige»*.
     *
     * ⚠️ No es el mismo que `tarjeta`. El papel de la tarjeta festoneada es casi
     * blanco (`#F7F5F2`, luminancia 242) y sobre él «beige» no se lee como beige
     * —la ronda 2 salió así y había que corregirlo—. Este es un tostado real,
     * cálido, que sigue dejando respirar: es el soporte de la pieza, no un color.
     */
    beige: '#EFE6D9',
    /** El mismo beige un punto más profundo, para la banda que cruza el tercio alto. */
    beigeHondo: '#E6DACA',
  },

  fuentes: {
    /**
     * ⭐ IvyPresto — **LA PRINCIPAL.** Titulares y destacados.
     * Dictado de Eli: «La tipografía principal es Ivy (…) Lo ideal es que se
     * usen poco, sólo para destacar o títulos importantes.»
     *
     * ⚠️ Es Adobe Fonts PROTEGIDA: no se empaqueta y NO viaja en el repo.
     * Vive activada en Creative Cloud; `scripts/p18-ivypresto-link.py` copia los
     * 20 cortes desde `%APPDATA%\Adobe\CoreSync\plugins\livetype\` buscándolos
     * por nombre interno. En otra máquina hay que correr el script de nuevo.
     *
     * ✅ Probada en Chrome headless pese a ser CFF — que es donde falló
     * Brushwell. El antecedente no se repitió, pero la prueba se hace siempre:
     * verificar con `document.fonts.check`.
     */
    titular: "'IvyPresto Headline', 'IvyPresto Display', Georgia, serif",
    /** El corte de texto corrido de la familia, para bajadas serif. */
    titularDisplay: "'IvyPresto Display', Georgia, serif",
    /**
     * Against — la ALTERNA de Ivy, «cuando se utilice mucho la otra».
     * Mismo criterio: poco, sólo destacados.
     *
     * ⛔ LÍMITE MEDIDO: 232 glifos, castellano completo **salvo `¿` y `¡`**.
     * Un titular como «¿Te casas en verano?» NO se puede componer en Against:
     * Chrome sustituye el signo con otra fuente y se nota. Ivy y Raleway sí los
     * traen. Tampoco sirve para cifras alineadas.
     */
    alterna: "'Against', 'IvyPresto Headline', serif",
    /**
     * Raleway — **el caballo de batalla.** Párrafos, textos largos, iconos,
     * cifras, CTA y legal. Dictado de Eli: «Raleway se utiliza para párrafos y
     * demás textos, cuando sean muchos o para iconos. Es más legible.»
     */
    texto: "'Raleway', 'Helvetica Neue', Arial, sans-serif",
  },

  /**
   * ⛔⛔ LAS CIFRAS NO SE ALINEAN CON CSS — `tabular-nums` NO FUNCIONA EN RALEWAY.
   *
   * Medido con `fontTools` sobre los TRES Raleway del estudio (el de Piso18, el
   * de EBEMA y el de Between): **ninguno declara la feature `tnum`**; sólo traen
   * `lnum`. Chrome ignora `font-variant-numeric: tabular-nums` **en silencio** y
   * deja los dígitos proporcionales.
   *
   * Anchos reales de `Raleway-Medium` (em): el `1` mide 0,450 y el `0` 0,614 —
   * el `1` es un **36 % más angosto**. En `$4.500.000` contra `$6.000.000` eso
   * descuadra la columna a simple vista, y es justo la comparación que hacen
   * las promos de esta marca.
   *
   * ⇒ Se alinea POR CÓDIGO: cada dígito en su caja, y esa caja al **máximo** de
   * la fila (`anchoDigitoMax`), nunca al promedio. Es el mismo arreglo que hubo
   * que hacer en Between, donde la caja estaba en el promedio y los ceros se
   * encaballaban en todo horario y precio.
   *
   * ⚠️ Y recordar que **el tracking no llega a un `inline-block`**: en una línea
   * con `letter-spacing` las letras se separan y los números quedan pegados.
   */
  cifras: {
    anchoDigitoMax: 0.614,
    anchos: [0.614, 0.450, 0.535, 0.540, 0.558, 0.548, 0.606, 0.535, 0.598, 0.589],
  },

  /**
   * ⭐ GEOMETRÍA MEDIDA — normalizada a un lienzo de **1080 de ancho**.
   *
   * Método: máscara de tinta blanca (`R,G,B > 225..235`) sobre las piezas
   * aprobadas, bbox por bloque de filas. El mismo método con el que se midieron
   * Revex, Between y DT.
   */
  geometria: {
    /**
     * ⭐⭐ LOGOTIPO — `logo PISO18.png` **NO es un logotipo suelto**: es una
     * PLANTILLA de historia 2250×4000 con un velo negro en degradado (alfa 150
     * arriba → 0 en y≈1667) que ocupa el 99,4 % de sus píxeles con alfa.
     *
     * El velo es INTENCIONAL y parte del sistema — es lo que hace legibles el
     * logotipo y el titular sobre la foto. **No es el defecto que reportó el
     * cliente.** Pero quien monte el PNG creyendo que es un logo le pega encima
     * un velo que oscurece el tercio superior de una pieza que quizá no lo quería.
     *
     * ⇒ El logotipo LIMPIO ya está recortado por `alfa > 200` y recompuesto por
     * luminancia en `public/assets/piso18/logo-piso18-completo.png` (566×228).
     *
     * ⭐ Y mide LO MISMO en historia y en carrusel — verificado en las dos piezas
     * aprobadas: ancho **225,6 @1080** la línea `CENTRO DE EVENTOS` en ambas.
     *
     * |  | ancho conjunto | tope y | centro x |
     * |---|---|---|---|
     * | historia (`ST N°1 S1`)   | **272,2** | **206,9** | 540,7 |
     * | carrusel (`C2 S1 n°1`)   | **~275**  | **105,1** | 535,7 |
     *
     * ⛔ NUNCA se deforma: se escala uniforme desde su proporción real.
     */
    logoAncho: 272,
    /** Proporción real del logotipo completo, medida sobre el alfa. */
    logoProporcion: 2.4825,
    /** Tope del logo en HISTORIA 9:16 (`ST N°1 S1`). */
    logoYStory: 207,
    /** Tope del logo en FEED 4:5 (`C2 S1 n°1`). */
    logoYFeed: 105,
    /** Hueco entre `PISO18` y `CENTRO DE EVENTOS`: 47 px @2250 en la story, 49 en el carrusel. */
    logoHuecoLineas: 23,
    /** La línea 2 mide el 82 % del ancho de la línea 1, en versales muy espaciadas. */
    logoRatioLinea2: 0.82,

    /**
     * TITULAR DE HISTORIA a dos pesos, medido en `ST N°1 S1`
     * («¿Te casas en verano?» / «ESTA ES TU OPORTUNIDAD»):
     *
     *   línea 1 · itálica, caja baja · y 342,2→435,4 · ancho 759,4
     *   línea 2 · VERSALES roman    · y 448,3→507,8 · ancho 1021,9
     *
     * ⭐ Ojo con el ancho de la línea 2: **1021,9 sobre 1080** deja sólo 29 px
     * de margen. El titular de esta marca va prácticamente a sangre.
     */
    tituloLinea1Alto: 93,
    tituloLinea2Alto: 60,

    /** CTA en píldora, medido en `ST N°1 S1`: caja de texto y 1632→1659, ancho 378. */
    ctaAlto: 27,
    ctaAncho: 378,

    /** El legal, en itálica, al pie: alto de caja 21,1 y dos líneas. */
    legalAlto: 21,

    /**
     * ⭐ EL MÁSTER DE ENTREGA ES 2250 — **corrige la lectura del `.ai`.**
     * La mesa de trabajo de los editables es 1080×1350, pero lo que el cliente
     * aprobó y lo que está publicado se entrega a 2250 de ancho:
     *   · feed / carrusel  **2250 × 2813** (4:5)
     *   · historia         **2250 × 4000** (9:16)
     *   · promo cuadrada   1080 × 1080
     */
    escalaMaster: 2250 / 1080,
  },

  formatos: {
    feed: {ancho: 2250, alto: 2813},
    story: {ancho: 2250, alto: 4000},
    promo: {ancho: 1080, alto: 1080},
  },

  /**
   * Zonas seguras de una HISTORIA (normalizadas a 1080×1920). Regla global de
   * paid del estudio; en orgánico son orientación, no ley — las piezas aprobadas
   * de esta marca las invaden y están aprobadas así.
   *
   * ⚠️ **La interacción NO se dibuja.** Se deja el aire y el sticker (encuesta,
   * link a cotización) lo pone el CM con el sticker real de Instagram.
   *
   * ⚠️ Y si la historia es ANIMADA, la posición y el contraste del botón se
   * miden en el **ÚLTIMO fotograma**, no en el primero.
   */
  seguras: {
    story: {arriba: 250, abajo: 340},
  },

  /**
   * ⭐⭐⭐ LOS BOTONES DE COTIZACIÓN — dictado por Eli el 15-09-2026.
   * «Siempre hay que hacer botones en las historias, y en algunos reels.»
   * La marca quiere redirigir a cotizar: es el objetivo comercial de la cuenta.
   *
   * ⛔ Los dos esquemas, y no hay un tercero. Nada de otro color, ni degradado,
   * ni transparente sobre la foto.
   */
  botones: {
    lleno: {fondo: '#D4145A', texto: '#FFFFFF'},
    invertido: {fondo: '#FFFFFF', texto: '#D4145A'},
  },

  /** Contacto y cierre de dirección, literales de la grilla. */
  contacto: {
    sitio: 'piso18.cl',
    correo: 'eventos@piso18.cl',
    direccion: 'Av. Vitacura 2727, Las Condes',
  },
} as const;

// ───────────────────────────────────────────────────────────────────────────
// Fuentes auto-hospedadas
// ───────────────────────────────────────────────────────────────────────────
let fuentesInyectadas = false;

/**
 * Inyecta las fuentes de Piso18. Sin `delayRender` (con auto-hospedadas se
 * cuelga — ver la memoria `reel-video-gotchas` §3).
 *
 * ⚠️ IvyPresto son `.otf` **CFF**, el mismo formato que Chrome (OTS) rechazó en
 * silencio con Brushwell y por el que se rindieron 27 piezas de Between con una
 * serif de reemplazo. Acá SÍ cargan —probado en headless el 15-09— pero hay que
 * **verificarlo en cada render** con `p18FuentesListas()`, nunca darlo por hecho.
 */
export const cargarFuentesP18 = () => {
  if (fuentesInyectadas || typeof document === 'undefined') return;
  fuentesInyectadas = true;
  const ivy = (archivo: string, familia: string, peso: number, estilo = 'normal') => `
  @font-face {
    font-family: '${familia}';
    src: url('${staticFile(`assets/fonts/piso18/ivypresto/${archivo}`)}') format('opentype');
    font-weight: ${peso};
    font-style: ${estilo};
    font-display: block;
  }`;
  const css = [
    ivy('IvyPrestoHeadlineThin.otf', 'IvyPresto Headline', 100),
    ivy('IvyPrestoHeadlineThinItalic.otf', 'IvyPresto Headline', 100, 'italic'),
    ivy('IvyPrestoHeadlineLight.otf', 'IvyPresto Headline', 300),
    ivy('IvyPrestoHeadlineLightItalic.otf', 'IvyPresto Headline', 300, 'italic'),
    ivy('IvyPrestoHeadlineRegular.otf', 'IvyPresto Headline', 400),
    ivy('IvyPrestoHeadlineItalic.otf', 'IvyPresto Headline', 400, 'italic'),
    ivy('IvyPrestoHeadlineSemiBold.otf', 'IvyPresto Headline', 600),
    ivy('IvyPrestoHeadlineSemiBoldItalic.otf', 'IvyPresto Headline', 600, 'italic'),
    ivy('IvyPrestoHeadlineBold.otf', 'IvyPresto Headline', 700),
    ivy('IvyPrestoHeadlineBoldItalic.otf', 'IvyPresto Headline', 700, 'italic'),
    ivy('IvyPrestoDisplayThin.otf', 'IvyPresto Display', 100),
    ivy('IvyPrestoDisplayThinItalic.otf', 'IvyPresto Display', 100, 'italic'),
    ivy('IvyPrestoDisplayLight.otf', 'IvyPresto Display', 300),
    ivy('IvyPrestoDisplayLightItalic.otf', 'IvyPresto Display', 300, 'italic'),
    ivy('IvyPrestoDisplayRegular.otf', 'IvyPresto Display', 400),
    ivy('IvyPrestoDisplayItalic.otf', 'IvyPresto Display', 400, 'italic'),
    ivy('IvyPrestoDisplaySemiBold.otf', 'IvyPresto Display', 600),
    ivy('IvyPrestoDisplaySemiBoldItalic.otf', 'IvyPresto Display', 600, 'italic'),
    ivy('IvyPrestoDisplayBold.otf', 'IvyPresto Display', 700),
    ivy('IvyPrestoDisplayBoldItalic.otf', 'IvyPresto Display', 700, 'italic'),
    `
  @font-face {
    font-family: 'Against';
    src: url('${staticFile('assets/fonts/piso18/against-regular.ttf')}') format('truetype');
    font-weight: 400;
    font-style: normal;
    font-display: block;
  }`,
    `
  @font-face {
    font-family: 'Raleway';
    src: url('${staticFile('assets/fonts/piso18/Raleway-Medium.ttf')}') format('truetype');
    font-weight: 500;
    font-style: normal;
    font-display: block;
  }`,
  ].join('\n');
  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);
  document.fonts.load('400 100px "IvyPresto Headline"').catch(() => {});
  document.fonts.load('400 100px "IvyPresto Display"').catch(() => {});
  document.fonts.load('500 100px Raleway').catch(() => {});
  document.fonts.load('400 100px Against').catch(() => {});
};

/**
 * ¿Cargaron de verdad? Es la comprobación que faltó en Between y costó 27 piezas.
 * Se llama DESPUÉS de `cargarFuentesP18()` y antes de dar un render por bueno.
 */
export const p18FuentesListas = (): boolean => {
  if (typeof document === 'undefined') return false;
  return (
    document.fonts.check('400 100px "IvyPresto Headline"') &&
    document.fonts.check('500 100px Raleway')
  );
};

/**
 * ⛔⛔⛔ LA PALABRA PROHIBIDA — dictado por Eli el 15-09-2026.
 * «Al cliente no le gusta que se escriba bodas. Nunca se escribe.»
 *
 * Y alcanza al MATERIAL DE ENTRADA, no sólo a lo que uno redacta: si la grilla,
 * un brief o una referencia trae «bodas» en un texto que va a ir en la pieza, se
 * reemplaza. Es la única excepción conocida a la regla de que los textos en
 * pantalla van literales del brief.
 *
 * ⛔ Es SÓLO de Piso18. En **DoubleTree**, `Noche de Bodas` es el nombre propio
 * de un programa del hotel y el cliente lo exigió por escrito: corregirlo allá
 * sería romperle el nombre a un producto.
 */
export const sinBodas = (texto: string): string =>
  texto
    .replace(/\bbodas\b/g, 'matrimonios')
    .replace(/\bBodas\b/g, 'Matrimonios')
    .replace(/\bBODAS\b/g, 'MATRIMONIOS')
    .replace(/\bboda\b/g, 'matrimonio')
    .replace(/\bBoda\b/g, 'Matrimonio')
    .replace(/\bBODA\b/g, 'MATRIMONIO');

/** ¿Quedó alguna «boda» viva en el texto? Para el QA, antes de entregar. */
export const tieneBodas = (texto: string): boolean => /\bbodas?\b/i.test(texto);

// ───────────────────────────────────────────────────────────────────────────
// Grano del fondo oscuro
// ───────────────────────────────────────────────────────────────────────────
/**
 * ⭐ GRANO DE FONDO — el `<svg>` que le da materia a un fondo oscuro plano.
 *
 * Nació de dos cosas a la vez, y las dos apuntaban al mismo arreglo:
 *
 * 1. **Dirección de arte.** La referencia que dejó Eli para la historia del
 *    28-09 no tiene un negro digital de fondo: tiene un **cuero**. Un fondo
 *    plano en una marca que compone con papel, velas y cristal se ve barato.
 *
 * 2. **QA.** `qa/motor.py --marca piso18` daba **bloqueante** en las dos
 *    historias de la S5: «foto estirada para llenar el formato — 204 filas
 *    clonadas seguidas». Medido, la racha real de filas idénticas era del
 *    **18 %** del alto en la del 28-09 (desde y=82 %) y del **11 %** en la del
 *    30-09 (desde y=89 %). No había ninguna foto estirada: era el fondo liso.
 *
 * ⛔ **Por eso NO se aflojó el tope de la regla.** Esa regla existe porque en
 * una story de Revex una foto estirada ocupó el 34 % de la pieza, y subirla al
 * 19 % para que pasara esta entrega la dejaba sin filo. Se arregló la pieza,
 * que además es lo que se veía mejor.
 *
 * Es el mismo `feTurbulence` de la textura de papel, pero **en claro y sobre
 * oscuro**: dos capas, fibra fina y veta ancha, muy tenues. A `0,05` y `0,035`
 * de opacidad no se ve como ruido y alcanza para que dos filas contiguas dejen
 * de ser idénticas.
 */
export const GranoFondo: React.FC<{semilla?: number}> = ({semilla = 5}) => (
  React.createElement(
    'svg',
    {
      width: '100%',
      height: '100%',
      style: {position: 'absolute', inset: 0, pointerEvents: 'none'},
      preserveAspectRatio: 'none',
    },
    React.createElement(
      'filter',
      {id: `p18-grano-${semilla}`},
      React.createElement('feTurbulence', {
        type: 'fractalNoise',
        baseFrequency: '0.52',
        numOctaves: 3,
        seed: semilla,
      }),
      React.createElement('feColorMatrix', {type: 'saturate', values: '0'}),
    ),
    React.createElement(
      'filter',
      {id: `p18-veta-fondo-${semilla}`},
      React.createElement('feTurbulence', {
        type: 'fractalNoise',
        baseFrequency: '0.006 0.021',
        numOctaves: 3,
        seed: semilla + 13,
      }),
      React.createElement('feColorMatrix', {type: 'saturate', values: '0'}),
    ),
    React.createElement('rect', {
      width: '100%',
      height: '100%',
      filter: `url(#p18-grano-${semilla})`,
      opacity: 0.05,
      style: {mixBlendMode: 'screen'},
    }),
    React.createElement('rect', {
      width: '100%',
      height: '100%',
      filter: `url(#p18-veta-fondo-${semilla})`,
      opacity: 0.035,
      style: {mixBlendMode: 'screen'},
    }),
  )
);
