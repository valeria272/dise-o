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
  /**
   * ⭐ ESCALA TIPOGRÁFICA — RE-MEDIDA 27-08-2026 sobre las DOS piezas que la
   * diseñadora marcó como «uso correcto de la tipografía»:
   *   raw/hilton/between-adn/ref-tipografia-ok/C1 S3 N°1.png      (feed  2250×2813)
   *   raw/hilton/between-adn/ref-tipografia-ok/ST S1 N°3 BW.png   (story 2250×4000)
   *
   * Valores en px sobre lienzo de 1080 de ancho. Verificados renderizando en Chrome
   * con las fuentes reales y comparando la TINTA contra la de ella:
   *
   *   titular  «PERFECTO»            ella 567×85  · nuestro 568×85
   *   caja     «PARA EMPEZAR EL DÍA» ella 488×33  · nuestro 482×33
   *   script   «El Match»            ella 403×124 · nuestro 406×125
   *
   * ⛔ LO QUE ESTABA MAL Y HUNDIÓ LA GRILLA DE SEPTIEMBRE:
   *   1. La script estaba en 1,92× el titular (186 contra 97). Es ≈ 1,0×.
   *      La script ACOMPAÑA; el titular en caja alta es el que manda.
   *   2. El titular estaba en 97. Es 117.
   *   3. Las dos líneas se solapaban a propósito (solapeScript: 2). NO se solapan:
   *      hay 9 px de aire entre tinta y tinta.
   *   4. El peso del titular era Black (900). Es ExtraBold (800).
   */
  tipos: {
    /** Titular en MAYÚSCULA, Raleway ExtraBold 800. Es el protagonista. */
    tituloCaps: 117,
    /**
     * Script que ACOMPAÑA al titular, encima de él.
     * ⚠️ Va en MENOR escala que el titular y solo para una FRASE CORTA o una
     * PALABRA CLAVE — nunca una frase de apoyo completa.
     */
    scriptAcompana: 123,
    /** Script como protagonista (nombre de producto, una sola palabra). */
    scriptSolo: 134,
    /** Bajada bajo el titular, sin caja. Raleway Medium. */
    bajada: 40,
    /** Texto DENTRO de la caja taupe. Raleway ExtraBold. */
    cajaDato: 45,
    /** Subtítulo en caja alta bajo la script protagonista («DE FRUTOS ROJOS»). */
    subtitulo: 44,
    /** Cierre en cursiva al pie («Una pausa para disfrutar»). */
    cierre: 40,
    /** Texto en arco al pie de la pieza. */
    arco: 51,
    /** Legales al pie. Medido: 11 px de tinta en el feed, 27 en la story. */
    legal: 22,

    /* — alias heredados — */
    get tituloCapsDestacado() { return this.tituloCaps; },
    get tituloCapsSutil() { return 74; },
    get cta() { return this.cajaDato; },
  },

  /**
   * Relación script / caps cuando el título mezcla las dos familias.
   * MEDIDO sobre la pieza aprobada: caps 117 → script 119. Es ≈ 1,0.
   * ⛔ El 1,92 anterior salió de medir una pieza donde los roles estaban INVERTIDOS
   * («EL MATCH» chico arriba + «perfecto» script grande abajo). Esa disposición
   * existe, pero NO es la de referencia. La de referencia es: script chica arriba,
   * caja alta grande abajo.
   */
  proporcionScript: 1.05,

  /** Tracking de la script. Calibrado: +0,036em deja «El Match» en 406 px. */
  trackingScript: 0.036,

  /** Tracking del titular en caja alta. Calibrado: −0,024em deja «PERFECTO» en 568. */
  trackingCaps: -0.024,

  /**
   * ⭐ AIRE ENTRE LÍNEAS — lo que el cliente pidió corregir el 27-08:
   * «los textos están muy juntos y se pierde la legibilidad».
   * Medido en la pieza aprobada, separación de TINTA a TINTA:
   */
  aire: {
    /** Script → titular en caja alta. */
    scriptATitulo: 9,
    /** Titular → caja taupe. */
    tituloACaja: 18,
    /** Titular → bajada sin caja. */
    tituloABajada: 24,
    /** Entre cajas apiladas. */
    entreCajas: 10,
    /** Logo → primer texto (medido en la story: 77). */
    logoATexto: 77,
  },

  /**
   * ⭐ CAJA TAUPE. RE-MEDIDA sobre la pieza aprobada:
   * fondo #675b49 OPACO, 66 px de alto, 54 px de padding lateral,
   * esquinas REDONDEADAS de 16 px de radio (antes estaban rectas).
   * Texto adentro: Raleway ExtraBold 45, beige.
   */
  cajas: {
    alto: 66,
    padX: 54,
    gap: 10,
    radio: 16,
    fondo: '#675b49',
  },

  /**
   * ⭐ GEOMETRÍA DEL BLOQUE DE TEXTO.
   * ⛔ Antes decía «alineado a la izquierda en x = 114». Las dos piezas aprobadas
   * están CENTRADAS sobre el eje (desviación medida: 0 y +3 px). Between compone
   * centrado; el bloque anclado a la izquierda no es su gramática.
   */
  bloque: {
    /** Centrado sobre el eje del lienzo. */
    alineacion: 'center' as const,
    /** Margen lateral mínimo: ningún texto pasa de acá. */
    margenX: 84,
    /** Primera línea de TINTA. Medido: feed y = 180, story y = 441 (bajo el logo). */
    yFeed: 180,
    yStory: 441,
    /** El titular ocupa 50–80 % del ancho del lienzo. */
    anchoMin: 0.5,
    anchoMax: 0.8,
    /**
     * ⭐ LA COLUMNA DE COMPOSICIÓN — añadida 01-09-2026.
     *
     * ⛔ El defecto que arregla: `TitularBetween` y `PanelTaupe` se achicaban
     * hasta **caber en el margen** (1080 − 2×84 = 912 px = 84,4 % del lienzo),
     * que está POR ENCIMA del `anchoMax: 0.8` que declara este mismo kit. Con
     * eso, toda línea larga aterrizaba clavada en el tope y el bloque se leía
     * como un muro. Medido en la entrega del 01-09 del carrusel Cowork:
     *
     *   | | slide 1 | slide 2 | slide 3 | referencia aprobada |
     *   |---|---|---|---|---|
     *   | titular | 55 % | **84 %** | **84 %** | **52 %** |
     *   | alto de caja del titular | 83 | 70 | 62 | **85** |
     *   | caja taupe | 50 % | 77 % | **84 %** (toca los dos márgenes) | **55 %** |
     *
     * Y como cada slide se achicaba por su cuenta, el carrusel salió con TRES
     * cuerpos de titular distintos (117 · 99 · 88): al deslizar, el titular
     * cambiaba de tamaño en cada slide. Eso es lo «desproporcionado» que marcó
     * Eli el 01-09.
     *
     * El margen es un LÍMITE (nada lo cruza); la columna es la MEDIDA en la que
     * se compone. 810 px = 75 % del lienzo: dentro del 50–80 % declarado, por
     * debajo del margen, y deja 135 px de aire a cada lado.
     */
    columna: 810,
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
    /**
     * ⛔ NO volver al .otf. Chrome (OTS) RECHAZA Brushwell.otf — sus contornos son
     * CFF y \`document.fonts.load\` devuelve «A network error occurred». El
     * @font-face falla EN SILENCIO y Remotion rinde con una serif de reemplazo:
     * así salieron las 27 piezas de septiembre que el cliente rechazó.
     * El .woff2 sale de convertir los contornos a TrueType (fontTools + cu2qu).
     */
    src: url('${ruta('Brushwell.woff2')}') format('woff2'),
         url('${ruta('Brushwell.ttf')}') format('truetype');
    font-display: block;
  }
  @font-face {
    font-family: 'ProvisionalScript';
    src: url('${ruta('Provisional-Script.ttf')}') format('truetype');
    font-display: block;
  }
  @font-face {
    /** La estática que entregó la diseñadora. Es la que manda para el titular. */
    font-family: 'Raleway';
    src: url('${ruta('Raleway-ExtraBold.ttf')}') format('truetype');
    font-weight: 800;
    font-style: normal;
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
  document.fonts.load('800 100px Raleway').catch(() => {});
  document.fonts.load('italic 400 100px Raleway').catch(() => {});
  /**
   * ⭐ Guardia anti-silencio. Una fuente que no carga NO rompe el render: deja
   * que el navegador dibuje con la de reemplazo y la pieza sale «casi bien».
   * Eso costó una grilla entera. Si alguna cara falta, que se vea en consola.
   */
  void document.fonts.ready.then(() => {
    (['400 100px Brushwell', '800 100px Raleway'] as const).forEach((cara) => {
      if (!document.fonts.check(cara)) {
        // eslint-disable-next-line no-console
        console.error(`[BETWEEN] La fuente «${cara}» NO cargó. La pieza saldrá con ` +
          `una fuente de reemplazo. NO entregar así.`);
      }
    });
  });
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
