/**
 * BETWEEN Coffee & Bar — brand kit (complejo DoubleTree by Hilton Santiago-Vitacura)
 *
 * FUENTE DE VERDAD: el feedback escrito de Elisabet Soto (diseñadora de la marca),
 * 24-08-2026. Todo lo de este archivo sale de ahí — no inventar valores nuevos.
 * Ver también clients/hilton/CLAUDE.md y la memoria between-sistema-grilla.
 *
 * Regla dura: CTAs, precios y horarios van LITERALES de la grilla mensual.
 */
import {staticFile} from 'remotion';

export const BETWEEN = {
  colores: {
    /** Beige principal de la marca — el color por defecto del texto sobre foto. */
    beige: '#fff9eb',
    /** Café de la marca — cajas de CTA, texto sobre fondos muy claros. */
    cafe: '#675b49',
    /** Solo para el multiply que oscurece la foto. No es un color de marca. */
    sombra: '#241a12',
  },

  fuentes: {
    /**
     * Brushwell Regular. Solo TÍTULOS o una palabra clave de acompañamiento.
     * NUNCA en números ni en párrafos. Trae signos y Ñ.
     * ✅ RESUELTO 25-08-2026: el .otf con licencia ya está en
     * public/assets/hilton/between/fonts/Brushwell.otf (382 glifos, v1.000),
     * bajado de la carpeta «Tipografías» que dejó Eli. Ya no hay provisional.
     */
    script: "'Brushwell', cursive",
    /** Raleway para todo lo demás. Máximo 2 familias por pieza (regla de Javier). */
    sans: "'Raleway', 'Helvetica Neue', sans-serif",
    /**
     * Alternativa con cobertura completa de español. Es MÁS FINA y monolineal que
     * Brushwell: al usarla hay que ABRIR el tracking para que se vea armónica
     * (indicación de Eli, confirmada al renderizar).
     * ⚠ LICENCIA: el archivo del Drive es la versión DEMO — «PERSONAL USE ONLY».
     * Para trabajo de cliente hay que comprar licencia comercial en almarkhatype.com.
     */
    scriptAlterna: "'Cherolina', cursive",
    /**
     * El editable FEED S1 2026.ai declara MÁS scripts que Brushwell:
     * Kallimata Script, Canvas Script, Allura, Backstroke, Pacifico,
     * Brush Script MT Italic, Forte, MV Boli y «against Regular».
     * Brushwell es la principal; el resto aparece en piezas puntuales.
     * ⚠ Pendiente con Eli: cuál va en qué caso. No usar ninguna otra sin preguntar.
     */
    scriptsSecundarias: ["Kallimata Script", "Canvas Script", "Allura", "Backstroke",
                         "Pacifico", "Brush Script MT Italic", "Forte", "MV Boli", "against"],
  },

  /** Pesos de Raleway que usa Eli. ExtraBold es el titular por defecto. */
  pesos: {
    regular: 400,
    semibold: 600,
    bold: 700,
    extrabold: 800,
    black: 900,
  },

  /**
   * ⭐ ESCALA TIPOGRÁFICA — MEDIDA sobre las piezas reales que entregó Eli
   * (raw/hilton/between-adn/ref-piezas/, 19 PNG a 2250×2813 y 2250×4000).
   * Valores en px sobre lienzo de 1080 de ancho.
   *
   * ⛔ ANTES ACÁ HABÍA RANGOS SACADOS DE UNA DESCRIPCIÓN ("40–122") y yo me senté
   * en la mitad. La marca vive en el TECHO del rango: los titulares reales miden
   * 88–96 px, no 56–70. Esa fue la causa de que la grilla de septiembre 2026
   * saliera tímida y "básica". No volver a estimar: medir.
   *
   * Método de verificación (por si hay que re-medir):
   *   1. aislar el texto beige #FFF9EB por umbral de color
   *   2. sacar el bounding box de tinta de cada línea
   *   3. renderizar la misma palabra con PIL a 100 px y comparar alto y ancho
   */
  tipos: {
    /**
     * Titular en MAYÚSCULA, Raleway BLACK. Medido en «EL MATCH»: tinta de 70 px
     * de alto y 448 de ancho → 94 px con tracking −1.
     * Rango observado en las piezas: 84–96.
     */
    tituloCaps: 97,
    /**
     * Script que ACOMPAÑA al titular. Medido en «perfecto»: tinta de 187 px de
     * alto y 614 de ancho → 186 px con tracking +1 en Chrome.
     * ⚠️ Es CASI EL DOBLE del Raleway, no un 20 % más. La script es la línea
     * dominante de la pieza: más ancha y más alta que la caja alta.
     */
    scriptAcompana: 186,
    /** Frase completa solo en Brushwell, sin caps arriba. Rango observado 140–175. */
    scriptSolo: 150,
    /**
     * Texto DENTRO de la caja taupe. Raleway **LIGHT** (no bold — el contraste
     * titular pesado / dato liviano es firma de la marca). Medido en
     * «CAFÉ TO GO + DULCE»: 45 px exactos por alto y por ancho.
     */
    cajaDato: 45,
    /** Bajada / párrafo suelto sobre foto. Máximo 3 líneas. */
    bajada: 38,
    /** Texto en arco al pie de la pieza. Cap-height medido ~45. */
    arco: 51,
    /** Legales en cursiva, al pie. Rango 20–26. */
    legal: 22,

    /* — alias heredados; apuntan a los valores medidos — */
    get tituloCapsDestacado() { return this.tituloCaps; },
    get tituloCapsSutil() { return 60; },
    get cta() { return this.cajaDato; },
  },

  /**
   * Relación script / caps cuando el título mezcla las dos familias.
   * ⚠️ MEDIDO 26-08-2026 sobre «EL MATCH perfecto»: caps 97 → script 186.
   * (Calibrado contra el render propio: la tinta tiene que dar 448 px de ancho
   * en la caja alta y 614 × 187 en la script.)
   * El 1.2 que había acá era una suposición mía y achataba el título: dejaba
   * la script como segunda línea decorativa cuando en realidad es la que manda.
   */
  proporcionScript: 1.92,

  /**
   * Tracking de la script cuando acompaña. Calibrado contra el render:
   * +1 px a 186 de cuerpo deja la tinta en los 614 × 187 px de la pieza real.
   * (Brushwell sale ~20 % más ancha en Chrome que en el cálculo de PIL, así que
   * este valor se ajusta midiendo el render, no estimando.)
   */
  trackingScript: 1,

  /** Tracking del titular en caja alta. Medido: −1 a 94 de cuerpo. */
  trackingCaps: -2,

  /**
   * ⭐ CAJA TAUPE — el elemento más reconocible de Between y el que faltaba.
   * Medido en «CAFÉ TO GO + DULCE» / «DESDE $3.790»:
   * fondo #675b49 OPACO, 74 px de alto, 29 px de padding lateral,
   * 10 px de separación entre cajas apiladas, esquinas rectas.
   * Las cajas de una pila se **centran entre sí**, no se alinean a la izquierda.
   */
  cajas: {
    alto: 74,
    padX: 29,
    gap: 10,
    radio: 0,
    fondo: '#675b49',
  },

  /**
   * ⭐ GEOMETRÍA DEL BLOQUE DE TEXTO — medida en las piezas de feed.
   * El bloque va ANCLADO ARRIBA y ALINEADO A LA IZQUIERDA (o centrado, según
   * plantilla), nunca flotando centrado en el medio del cuadro.
   */
  bloque: {
    /** Margen lateral del bloque de titular. Medido: x = 114 sobre 1080. */
    x: 114,
    /** Primera línea de tinta del titular. Medido: y = 220 en feed, y = 425 en story. */
    yFeed: 220,
    yStory: 425,
    /** Separación de TINTA entre la caja alta y la script: prácticamente 0 (2 px). */
    solapeScript: 2,
    /** El titular ocupa 55–80 % del ancho del lienzo. Bajo 50 % la pieza se ve chica. */
    anchoMin: 0.55,
    anchoMax: 0.8,
  },

  /**
   * ⭐ TEXTO EN ARCO al pie — «VIGILANTES, MUFFIN, BROWNIE Y MÁS».
   * Medido: cuerda 864 px, flecha 135 px → radio ≈ 760 px, arco ≈ 69°.
   */
  arcoPie: {
    radio: 760,
    cuerda: 864,
    y: 1140,
  },

  /** Tracking de horarios: 5 a 10, solo si hace falta compensar jerarquía. */
  trackingHorario: 7,

  logo: {
    beige: 'assets/hilton/between/logo-blanco.png',
    cafe: 'assets/hilton/between/logo-negro.png',
    /** El PNG es el lockup completo (BETWEEN + COFFEE & BAR). */
    ratio: 981 / 324,
    /**
     * Medidas EXACTAS que dio Eli (26-08), ancho × alto del lockup completo,
     * sobre lienzo de 1080 de ancho. Coinciden con lo medido en sus plantillas
     * de márgenes — dos fuentes independientes dieron lo mismo.
     *
     * ⚠️ El «262» NO es alto: es ANCHO. El alto máximo en post es ~87.
     * El logo SIEMPRE va a escala: se escala por ancho y el alto sale del ratio,
     * para que nunca se vea achatado.
     */
    limites: {
      post:  {anchoMin: 162.42, altoMin: 53.61, anchoMax: 262.90, altoMax: 86.77},
      story: {anchoMin: 196.68, altoMin: 64.92, anchoMax: 281.57, altoMax: 92.93},
    },
  },

  /**
   * Cobertura de glifos de las scripts — VERIFICADA con fontTools el 25-08-2026.
   * Determina cuál se puede usar según el texto que lleve la pieza.
   */
  glifos: {
    Cherolina: {Ñ: true, ñ: true, '¿': true, '¡': true, tildes: true, glifos: 345,
                nota: 'la única script completa. Más fina que Brushwell: abrir tracking'},
    Brushwell: {Ñ: true, ñ: true, '¿': true, '¡': false, tildes: true, glifos: 382,
                nota: 'la principal. LE FALTA el ¡ → usar volteaApertura()'},
    KallimataScript: {Ñ: false, ñ: false, '¿': false, '¡': false, tildes: false, glifos: 88,
                nota: 'la original casi no sirve para español'},
    KallimataES: {Ñ: false, ñ: true, '¿': false, '¡': true, tildes: true, glifos: 95,
                nota: 'versión parchada. Sirve salvo que el texto lleve Ñ mayúscula o ¿'},
  },

  /**
   * ⭐ Geometría del logo MEDIDA sobre las plantillas de márgenes de Eli
   * (raw/hilton/between-adn/margenes/, master 2250×2813 y 2250×4000).
   * Valores ya escalados a lienzo de 1080 de ancho.
   *
   * ⛔ OJO — Between NO es como Revex/Casablanca/EBEMA: acá el logo va
   * CENTRADO y CON MARGEN, no pegado al borde. La regla «el logo va pegado
   * arriba» es de esas otras marcas, no de esta.
   *
   * Eli entrega DOS plantillas por formato: logo arriba y logo abajo.
   * La bajada «COFFEE & BAR» es un bloque aparte, bajo el wordmark.
   */
  margenes: {
    postLogoArriba:  {wordmarkY: 93,   wordmarkAlto: 59, bajadaY: 165,  bajadaAlto: 15, ancho: 263, centradoX: true},
    postLogoAbajo:   {wordmarkY: 1173, wordmarkAlto: 47, bajadaY: 1230, bajadaAlto: 12, ancho: 209, centradoX: true},
    storyLogoArriba: {wordmarkY: 271,  wordmarkAlto: 63, bajadaY: 348,  bajadaAlto: 16, ancho: 282, centradoX: true},
    storyLogoAbajo:  {wordmarkY: 1619, wordmarkAlto: 44, bajadaY: 1673, bajadaAlto: 11, ancho: 196, centradoX: true},
    /** El master de Eli es 2× (2250 de ancho); se entrega a 1080. */
    masterScale: 2250 / 1080,
    /** Color del logo en las plantillas: el beige de marca. */
    color: '#FFF9EB',
  },

  /**
   * ⭐ Tamaños del logo — CIFRAS EXACTAS que entregó Eli (25-08-2026).
   * Regla suya: «siempre es a escala, guíate del ALTO, que no se vea achatado.»
   * El ratio es constante 3,0298 — si tu ancho/alto no da eso, está deformado.
   */
  logoTamanos: {
    ratio: 196.6809 / 64.9154, // = 3.02979 — idéntico en las 4 medidas de Eli
    story: {
      min: {w: 196.6809, h: 64.9154},
      max: {w: 281.5732, h: 92.9345},
    },
    post: {
      min: {w: 162.4194, h: 53.6072},
      max: {w: 262.9032, h: 86.7724},
    },
    /** Puede salirse del rango si la pieza lo pide, pero NUNCA deformado. */
    flexible: true,
  },

  /**
   * Formatos de entrega. Todo digital, 150 ppp, RGB.
   * Paid media NO puede pasar los 150 ppp; la grilla orgánica sí admite más peso.
   */
  formatos: {
    feed: {width: 1080, height: 1350},
    story: {width: 1080, height: 1920},
    reel: {width: 1080, height: 1920},
    /** Paid media en post sigue siendo cuadrado, y el logo va en otra posición. */
    paidPost: {width: 1080, height: 1080},
  },

  datos: {
    direccion: 'Av. Vitacura 2727, Las Condes',
    web: 'cafeteriabetween.cl',
  },
} as const;

/**
 * Los títulos de Between NUNCA llevan punto final — al cliente le molesta.
 * Se aplica en los componentes de título, no a mano en cada pieza.
 */
export const sinPuntoFinal = (texto: string) => texto.replace(/\.+\s*$/, '');

let fuentesInyectadas = false;

/** Auto-hospedadas, sin delayRender (ver memoria reel-video-gotchas §3). */
export const cargarFuentesBetween = () => {
  if (fuentesInyectadas || typeof document === 'undefined') return;
  fuentesInyectadas = true;
  const ruta = (f: string) => staticFile(`assets/hilton/between/fonts/${f}`);
  const css = `
  @font-face {
    font-family: 'Brushwell';
    src: url('${ruta('Brushwell.otf')}') format('opentype');
    font-display: block;
  }
  @font-face {
    font-family: 'ProvisionalScript';
    src: url('${ruta('Provisional-Script.ttf')}') format('truetype');
    font-display: block;
  }
  @font-face {
    font-family: 'Raleway';
    src: url('${ruta('Raleway.ttf')}') format('truetype');
    font-weight: 100 900;
    font-style: normal;
    font-display: block;
  }
  @font-face {
    font-family: 'Raleway';
    src: url('${ruta('Raleway-Italic.ttf')}') format('truetype');
    font-weight: 100 900;
    font-style: italic;
    font-display: block;
  }`;
  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);
  document.fonts.load('400 100px Brushwell').catch(() => {});
  document.fonts.load('400 100px ProvisionalScript').catch(() => {});
  document.fonts.load('800 100px Raleway').catch(() => {});
  document.fonts.load('italic 400 100px Raleway').catch(() => {});
};

cargarFuentesBetween();


/**
 * ⭐ El truco de Eli para los signos de apertura.
 *
 * Brushwell no trae el «¡» y Kallimata no trae «¡» ni «¿». Su solución es usar el
 * signo de cierre ROTADO 180°, que en estas fuentes calza perfecto porque están
 * bien construidas.
 *
 * Devuelve los trozos para renderizar: los marcados `flip` se dibujan con
 * `transform: rotate(180deg)` y `display:inline-block`.
 *
 *   volteaApertura("¿Un café? ¡Ya!")
 *   → [{t:"?",flip:true},{t:"Un café? "},{t:"!",flip:true},{t:"Ya!"}]
 */
export const volteaApertura = (texto: string): {t: string; flip?: boolean}[] => {
  const out: {t: string; flip?: boolean}[] = [];
  let buf = "";
  for (const ch of texto) {
    if (ch === "¿" || ch === "¡") {
      if (buf) {
        out.push({t: buf});
        buf = "";
      }
      out.push({t: ch === "¿" ? "?" : "!", flip: true});
    } else {
      buf += ch;
    }
  }
  if (buf) out.push({t: buf});
  return out;
};

/**
 * ¿Esta script aguanta este texto? Evita descubrir el tofu al renderizar.
 * Si devuelve false, usar Cherolina o volteaApertura().
 */
export const scriptSirve = (
  texto: string,
  script: keyof typeof BETWEEN.glifos,
): boolean => {
  const g = BETWEEN.glifos[script];
  if (/Ñ/.test(texto) && !g.Ñ) return false;
  if (/ñ/.test(texto) && !g.ñ) return false;
  if (/¿/.test(texto) && !g["¿"]) return false;
  if (/¡/.test(texto) && !g["¡"]) return false;
  if (/[áéíóúÁÉÍÓÚ]/.test(texto) && !g.tildes) return false;
  return true;
};

/** Alto del logo → ancho, sin deformar. Regla de Eli: guiarse del alto. */
export const anchoLogo = (alto: number) => alto * BETWEEN.logoTamanos.ratio;
