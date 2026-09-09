/**
 * DOUBLETREE by Hilton Santiago–Vitacura — brand kit
 *
 * FUENTES DE VERDAD, en este orden:
 *   1. Las piezas APROBADAS del cliente (`raw/hilton/dt/aprobadas-sept/`,
 *      2250×2813): `C1 FT N1.png`, `C1 FT N2.png`, `DT FT S3.png`.
 *   2. `clients/hilton/CLAUDE.md` § «DT — LA LEY DE ELI» (09-09-2026) y
 *      § «Brand kit DT (del manual oficial Hilton)».
 *   3. El manual oficial Hilton (`raw/hilton/dt/identidad/`).
 *
 * La jerarquía que fijó Eli el 08-09: **el manual oficial manda en COLOR y
 * TIPOGRAFÍA; ella manda en composición, uso de foto y texto.**
 *
 * ⛔ Regla dura de la cuenta (§G, dictada por Eli el 09-09): **en DT sólo se
 * DISEÑA.** Los textos salen LITERALES de la grilla; no se corrige un copy, un
 * precio ni un CTA. Una discrepancia se informa y ahí para.
 *
 * ⛔ Y el criterio de DT no se traspasa a QB, Between ni Piso18, ni al revés.
 *
 * ── Estado ────────────────────────────────────────────────────────────────
 * Escrito el 09-09-2026 al armar la historia del Día del Turismo (STORIES col
 * K). Cierra parte del pendiente que arrastraban los tres cierres de ese día
 * («medir la geometría de DT»). **Cada número dice de dónde sale y con qué
 * confianza** — lo que no se midió, no está acá.
 */
import {staticFile} from 'remotion';

export const DT = {
  colores: {
    /**
     * DoubleTree Blue. El manual oficial declara `#09194E` y la MEDICIÓN lo
     * confirma: cuantizando los píxeles azul-oscuro de las tres piezas
     * aprobadas, la moda cae en `#08-0F / 18-1F / 48-4F` en las tres. ✅
     * Es el color dominante (70 % del uso).
     */
    azul: '#09194E',
    /** Verde Hilton — acento, 20 % del uso. */
    verde: '#A3CD39',
    /** Blanco de marca. Es la tinta por defecto sobre foto. */
    blanco: '#FAFAFA',
    /** Secundarios, sólo piezas clave (10 %). */
    amarillo: '#FFCC00',
    rojoCalido: '#CF4800',
  },

  fuentes: {
    /**
     * Stag — TITULARES, y nada más. Regla de Eli del 03-09: **en DT no se usa
     * Raleway.**
     *
     * ⛔ LÍMITE DE LA FAMILIA, verificado glifo a glifo sobre los archivos de
     * esta máquina (`fontTools`, 09-09-2026): los NUEVE cortes de Stag traen el
     * MISMO subconjunto de 354 glifos y a todos les falta
     * `U+00A1 ¡` y `U+00BF ¿` (además de `$ % @ € º ª # *`).
     * O sea que Stag **no puede escribir `¡Feliz…!`** por diseño de la familia.
     * Salidas, en este orden: `volteaApertura()` (el truco de Eli: el signo de
     * cierre rotado 180°), o pasar esa línea a Trade.
     */
    titular: "'Stag', Georgia, serif",
    /**
     * Trade Gothic — CIFRAS, precios, versales, cuerpo, CTA y legal.
     * Cobertura verificada: 287 glifos, y **sí trae `¡` y `¿`**.
     *
     * ⚠️ Sólo hay dos cortes en esta máquina: Regular y Bold Condensed No. 20.
     * **Falta un Bold de ancho normal**, que es justo el que pide un bloque de
     * precio (por ahí se había colado Raleway). Faltan también `Stag LCG`,
     * `Trade Gothic LT Std Bold` y `Trade Gothic Next LT Pro Bold`, y sólo el
     * cliente los tiene.
     */
    texto: "'Trade Gothic', 'Helvetica Neue', Arial, sans-serif",
  },

  /** Pesos de Stag disponibles como archivo. */
  pesos: {
    light: 300,
    regular: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
  },

  /**
   * ⭐ GEOMETRÍA MEDIDA — valores ya normalizados a un lienzo de **1080 de
   * ancho**. El máster de entrega es 2250 (`escalaMaster`), igual que Between.
   *
   * Método: máscara de tinta blanca (`R,G,B > 225..238`) sobre las piezas
   * aprobadas, bbox por bloque de filas. Es el mismo método con el que se
   * midieron Revex y Between.
   */
  geometria: {
    /**
     * ⭐⭐ LOGOTIPO — sale de las PLANTILLAS DE MÁRGENES de Eli, que es la
     * fuente buena y estaba ahí desde el 08-09:
     * `raw/hilton/dt/identidad/logos/logo-ST.png` (2250×4000, historia) y
     * `logo-post.png` (2250×2813, feed). Son el logo YA COLOCADO en el lienzo
     * de entrega, así que dan posición y tamaño sin estimar nada.
     *
     * |  | ancho | alto | tope y | centro x |
     * |---|---|---|---|---|
     * | historia (`logo-ST.png`)  | **167,0** | 136,3 | **241,0** | 539,8 |
     * | feed (`logo-post.png`)    | **160,3** | 130,6 | **111,4** | 539,8 |
     *
     * ⭐ Y la proporción coincide en CUATRO fuentes independientes: plantilla de
     * historia 1,2254 · plantilla de feed 1,2279 · pieza aprobada `C1 FT N1`
     * 1,226 · archivo del logotipo (bbox opaco) 1,2265. ⇒ **el logo se usa a su
     * proporción real.** Se escala uniforme, jamás por geometría.
     *
     * En los dos formatos va CENTRADO (desvío de 0,2 px sobre 540).
     */
    logoAncho: 160,
    logoAnchoStory: 167,
    /** Proporción real, para no deformarlo nunca. */
    logoProporcion: 1.2254,
    /** Tope del logo en pieza 4:5 (`logo-post.png`; `C1 FT N1` da 111,8). */
    logoYFeed: 111,
    /** Tope del logo en HISTORIA (`logo-ST.png`). */
    logoYStory: 241,

    /**
     * Margen lateral del bloque de texto: **88 px** @1080, simétrico.
     * Medido en `C1 FT N2`, cuya tinta va de x=87 a x=992 (centro 539,5).
     */
    margenLateral: 88,

    /**
     * Panel de esquinas redondeadas con filete blanco fino — el contenedor de
     * DT. Medido en `DT FT S3`: va de x=175 a x=904, o sea **ancho 730** @1080
     * y centrado (centro 539,5).
     */
    panelAncho: 730,

    /**
     * TITULAR A DOS PESOS, medido en `C1 FT N1` («Este es su panorama» /
     * «Ideal en familia»):
     *
     *   línea 1 · y 991,7→1040,6 · alto de bloque 49,4 · ancho 576
     *   línea 2 · y 1055,0→1119,8 · alto de bloque 65,3 · ancho 673
     *
     * ⭐ Ojo con el orden, que es contraintuitivo y es el de la marca: la línea
     * de ARRIBA va en **Bold y más chica**, y la de ABAJO en **Light y más
     * grande**. El énfasis lo lleva la línea liviana.
     */
    tituloBloque1: 49,
    tituloBloque2: 65,
    /** Versales de la dirección al pie, `C1 FT N1`: alto de caja 14,9. */
    versalitaAlto: 15,

    /** El máster de Eli: 2250 / 1080. Las 66 historias entregadas van a 2250×4000. */
    escalaMaster: 2250 / 1080,
  },

  /**
   * Zonas seguras de una HISTORIA (1080×1920). La franja de arriba se la come
   * la interfaz de Instagram y la de abajo el «Enviar mensaje» + las
   * interacciones que pega el CM.
   *
   * ⚠️ Y la regla que Eli repitió tres veces en Between y vale igual acá: **la
   * interacción NO se dibuja.** Se deja el aire y el sticker lo pone el CM con
   * el sticker real de Instagram.
   */
  seguras: {
    story: {arriba: 250, abajo: 340},
  },
} as const;

// ───────────────────────────────────────────────────────────────────────────
// Fuentes auto-hospedadas
// ───────────────────────────────────────────────────────────────────────────
let fuentesInyectadas = false;

/**
 * Inyecta las fuentes de DT. Sin `delayRender` (ver memoria `reel-video-gotchas`
 * §3: con auto-hospedadas se cuelga).
 *
 * ⛔ Trade Gothic entra por **`.woff2`**, no por el `.otf`. Los dos `.otf` de la
 * familia son CFF/PostScript, el mismo formato que Chrome (OTS) rechazó con
 * Brushwell: el `@font-face` falla EN SILENCIO y Remotion rinde con una serif
 * de reemplazo. Así salieron las 27 piezas de Between que el cliente rechazó.
 * Ver la memoria `brushwell-no-cargaba-en-chrome`.
 */
export const cargarFuentesDT = () => {
  if (fuentesInyectadas || typeof document === 'undefined') return;
  fuentesInyectadas = true;
  const ruta = (f: string) => staticFile(`assets/hilton/dt/fonts/${f}`);
  const stag = (archivo: string, peso: number, estilo = 'normal') => `
  @font-face {
    font-family: 'Stag';
    src: url('${ruta(archivo)}') format('truetype');
    font-weight: ${peso};
    font-style: ${estilo};
    font-display: block;
  }`;
  const css = [
    stag('Stag-Light.ttf', 300),
    stag('Stag-Regular.ttf', 400),
    stag('Stag-Medium.ttf', 500),
    stag('Stag-SemiBold.ttf', 600),
    stag('Stag-Bold.ttf', 700),
    stag('Stag-LightItalic.ttf', 300, 'italic'),
    stag('Stag-Italic.ttf', 400, 'italic'),
    stag('Stag-MediumItalic.ttf', 500, 'italic'),
    stag('Stag-SemiBoldItalic.ttf', 600, 'italic'),
    `
  @font-face {
    font-family: 'Trade Gothic';
    src: url('${ruta('TradeGothicLTStd-Regular.woff2')}') format('woff2');
    font-weight: 400;
    font-style: normal;
    font-display: block;
  }`,
    `
  @font-face {
    /** Bold Condensed No. 20. NO es un Bold de ancho normal — ver \`fuentes\`. */
    font-family: 'Trade Gothic Cn';
    src: url('${ruta('TradeGothicLTStd-BoldCn20.woff2')}') format('woff2');
    font-weight: 700;
    font-style: normal;
    font-display: block;
  }`,
  ].join('\n');
  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);
  document.fonts.load('700 100px Stag').catch(() => {});
  document.fonts.load('300 100px Stag').catch(() => {});
  document.fonts.load('400 100px "Trade Gothic"').catch(() => {});
};

/**
 * El truco de Eli para `¡` y `¿`: como Stag no trae los signos de apertura, se
 * dibuja el de CIERRE rotado 180°. «Ya están volteando o reflejando, ya que
 * está bien construida.»
 *
 *   volteaApertura('¡Feliz Día!')
 *   → [{t:'!', flip:true}, {t:'Feliz Día!'}]
 *
 * Es la misma función que usa Between; vive acá también para que una pieza de DT
 * no tenga que importar el kit de otra marca.
 */
export const volteaApertura = (texto: string): {t: string; flip?: boolean}[] => {
  const out: {t: string; flip?: boolean}[] = [];
  let buf = '';
  for (const ch of texto) {
    if (ch === '¿' || ch === '¡') {
      if (buf) {
        out.push({t: buf});
        buf = '';
      }
      out.push({t: ch === '¿' ? '?' : '!', flip: true});
    } else {
      buf += ch;
    }
  }
  if (buf) out.push({t: buf});
  return out;
};

/** ¿Aguanta esta fuente este texto? Para no descubrir el tofu al renderizar. */
export const stagSirve = (texto: string): boolean =>
  ![...texto].some((c) => c === '¡' || c === '¿' || '$%@€ºª#*'.includes(c));
