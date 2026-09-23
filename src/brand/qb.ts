/**
 * QB RESTAURANT — kit de marca
 * ════════════════════════════════════════════════════════════════════════════
 * QB es MARCA INDEPENDIENTE. Está dentro del complejo Hilton pero su línea
 * gráfica no está ligada a DoubleTree, Between ni Piso18 (Eli, 15-09-2026).
 * Nada se traspasa en ninguna dirección.
 *
 * Manual: clients/qb/CLAUDE.md
 *
 * ════════════════════════════════════════════════════════════════════════════
 * TODO LO DE ESTE ARCHIVO ESTÁ MEDIDO — 17-09-2026
 * ════════════════════════════════════════════════════════════════════════════
 * Fuente de la medición: los editables y finales de Eli, bajados de su Drive:
 *
 *   · `PROMOS QB 2026 AYCD 2026 ST.png`  2250×4000 — la ST de AYCD vigente
 *   · `PROMOS QB 2026 AYCD ST2.png`      2250×4000 — la misma de junio 2026
 *   · `PROMOS QB 2026 1080x1920px.png`   2250×4000 — el KV de pantallas (KV 2)
 *   · `QB BLANCO - SIN FONDO.png`        2250×2250 — el logotipo oficial
 *
 * Copia local en `raw/hilton/qb/aycd/` (no viaja al repo).
 *
 * ⭐ Las dos ST de AYCD —junio y septiembre— tienen el bloque de marca en las
 * MISMAS coordenadas al píxel. Lo único que cambia entre las dos es la
 * fotografía. Eso es lo que hace del bloque un sistema y no una maqueta.
 *
 * ════════════════════════════════════════════════════════════════════════════
 * ⭐⭐ EL VERDE DE QB ERA UN DEGRADADO, NO TRES VERDES
 * ════════════════════════════════════════════════════════════════════════════
 * El manual traía abierto desde el 15-09 que «hay tres verdes y ninguno cuadra»:
 * la franja de historia daba #374C3C, la pastilla de feed ~#66886B y el .ai
 * declaraba PANTONE 361 C. Medido el botón de AYCD barriendo píxel a píxel:
 *
 *   x=630 → (53,73,58)   ·   x=1125 (centro) → (102,136,107)   ·   x=1590 → (58,79,63)
 *
 * **Es un degradado lineal horizontal, simétrico, oscuro en los dos bordes y
 * claro al centro. Y es constante en vertical.** Los dos verdes que no cuadraban
 * son los DOS EXTREMOS del mismo degradado: quien midió la franja tomó el borde
 * y quien midió la pastilla tomó el centro.
 *
 * Es el «efecto de degradado» del botón que Eli nombró como intocable.
 */

import {staticFile} from "remotion";

/** Mesa de trabajo de QB. Se entrega a 2250×4000 (escala 2.0833). */
export const QB_MESA = {w: 1080, h: 1920} as const;
export const QB_ESCALA_ENTREGA = 2250 / 1080; // 2.0833…

/** Paleta. El color de QB es variable por decisión de marca: se anota con fecha. */
export const qbColores = {
  /** Base de la pieza. La foto entra y sale a negro, arriba y abajo. */
  negro: "#000000",
  blanco: "#FFFFFF",
  /** Texto oscuro sobre blanco — medido en la pastilla del KV de pantallas. */
  tinta: "#1D1D1B",

  /** ⭐ El degradado del botón. Medido sobre el botón de AYCD, 17-09-2026. */
  verdeBorde: "#354A3A",
  verdeCentro: "#66886B",
} as const;

/**
 * ⭐ EL BOTÓN VERDE — no varía.
 * Degradado lineal horizontal: borde → centro → borde.
 * Esquinas VIVAS (medido: la primera fila de píxel ya arranca en x=628, sin radio).
 */
export const QB_BOTON_FONDO =
  `linear-gradient(90deg, ${qbColores.verdeBorde} 0%, ${qbColores.verdeCentro} 50%, ${qbColores.verdeBorde} 100%)`;

/**
 * Tipografías.
 *
 * ⚠️ La Raleway de la marca es la de **Adobe Fonts** y la del repo es la de
 * Google Fonts. Se verificó contra la pieza real: a cuerpo 109,4 px la
 * ExtraBold da «DRINK» en 699 px contra los 701 medidos (0,3 % de error) y
 * «ALL» en 416 contra 413. Reproduce.
 *
 * ⚠️ La itálica del repo sale ~3 % más ancha que la de la pieza, así que el
 * bloque lleva `trackingItalica` para calzar. Ver QB_AYCD.titular.
 *
 * ⭐ Toda cifra de Raleway lleva `lnum` (cifras de caja alta). Sin eso el
 * «13.990» y el «18:00» se leen como minúsculas al lado de las versales —
 * es el hallazgo del 15-09 y vale para toda la marca.
 */
export const qbFuentes = {
  principal: "Raleway",
  /** Bell MT — la letra chica de QB (legal y lista de tragos, en itálica). */
  editorial: "BellMT",
  mano: "Brushwell",
} as const;

export const QB_CIFRAS: React.CSSProperties = {
  fontFeatureSettings: '"lnum" 1',
  fontVariantNumeric: "lining-nums",
};

/** Rutas de los archivos versionados en `public/`. */
export const QB_ASSETS = {
  /** El oficial tal cual viene del Drive: lienzo 2250×2250, 92,9 % transparente. */
  logoOriginal: "assets/hilton/qb/logo/QB-BLANCO-SIN-FONDO.png",
  /** ⭐ El mismo, ya recortado a su alfa (1437×875). **Es el que se monta.** */
  logoBlanco: "assets/hilton/qb/logo/qb-blanco.png",
  /**
   * La fotografía aprobada de AYCD, **sin su texto**. Sale de la ST vigente de
   * Eli, limpiada con `scripts/qb-aycd-limpiar-foto.py`, para poder animar el
   * bloque encima sin que asome el texto quemado.
   */
  fotoAycd: "assets/hilton/qb/fotos/aycd-barra-base.jpg",
  /**
   * ⭐ El mate de las copas: la MISMA foto con alfa sacado de su luminancia.
   * Se vuelve a montar encima del texto en movimiento para que la tipografía
   * quede **cortada por las copas**, que es el recurso de la referencia.
   */
  fotoAycdCopas: "assets/hilton/qb/fotos/aycd-barra-copas.png",
  fuentes: "assets/hilton/qb/fonts/",
} as const;

/**
 * El logotipo oficial, medido: lienzo 2250×2250 con el 92,9 % transparente.
 * La marca real mide 1437×875 dentro de él → proporción 1,642:1.
 * ⚠️ Montarlo sin recortar el alfa es montar un lienzo cuadrado entero.
 */
export const QB_LOGO = {
  lienzo: {w: 2250, h: 2250},
  caja: {x: 406, y: 630, w: 1437, h: 875},
  proporcion: 1437 / 875,
} as const;

/**
 * ════════════════════════════════════════════════════════════════════════════
 * ⭐⭐ EL BLOQUE DE «ALL YOU CAN DRINK» — LO QUE NO PUEDE VARIAR
 * ════════════════════════════════════════════════════════════════════════════
 * Dictado por Eli el 17-09-2026, sobre la S5:
 *
 *   «busca que el diseño y textos de AYCD sean igual al KV. Puede variar la
 *    foto o cosas así, pero botón verde con efecto de degradado y logo + el
 *    nombre no.»
 *
 * O sea: **la foto es la variable y el bloque de marca es la constante.**
 * Las dos ST de AYCD medidas lo confirman al píxel.
 *
 * Todas las cifras de abajo están en la mesa de 1080×1920 (medidas a 2250 y
 * multiplicadas por 0,48).
 */
export const QB_AYCD = {
  /** El logotipo, centrado y arriba. */
  logo: {top: 207.4, alto: 108.5, ancho: 178.6, centroX: 540},

  /**
   * El titular. Dos líneas del MISMO cuerpo, centradas, blanco.
   * Lo que separa las palabras es el corte, no el tamaño:
   *   ALL (ExtraBold)  YOU (Italic)
   *   CAN (Italic)     DRINK (ExtraBold)
   */
  titular: {
    cuerpo: 109.4,
    /** Alto de versal medido. Sirve para posicionar por caja, no por línea. */
    altoVersal: 77.8,
    /** Avance de línea (base a base). */
    interlinea: 102.7,
    /** Tope de la versal de cada línea. */
    linea1Top: 376.3,
    linea2Top: 479.0,
    /** La itálica de Google sale ~3 % ancha: se compensa. */
    trackingItalica: "-0.022em",
    anchosMedidos: {ALL: 198.2, YOU: 208.8, CAN: 214.6, DRINK: 336.5},
  },

  /** «TODOS LOS MARTES» — Raleway versales, blanco, centrado. */
  antetitulo: {top: 1311.4, altoVersal: 32.6, ancho: 473.8},

  /** ⭐ El botón. Rectángulo de esquinas vivas con el degradado de marca. */
  boton: {top: 1364.6, alto: 85.9, ancho: 477.1, centroX: 540},

  /** El horario, bajo el botón. Raleway liviana, blanco, centrado. */
  horario: {top: 1479.4, altoVersal: 32.2, ancho: 400.3},

  /**
   * El pie negro. La foto se funde a negro puro y de ahí abajo es lienzo.
   * Medido: la foto llega a 0 de luminancia en y=3350 @2250 → 1608 @1080.
   */
  pieNegro: {top: 1608},

  /** El legal y la lista de tragos — Bell MT Itálica, blanco, centrado. */
  legal: {top: 1629.6, altoCaja: 22.6},
  lista: {linea1Top: 1789.0, linea2Top: 1822.1, interlinea: 33.1},

  /** La foto entra y sale a negro. Medido: ~200 px de fundido @2250 abajo. */
  fundidoFoto: {arribaHasta: 86, abajoDesde: 1512},
} as const;

/**
 * ⚠️ ZONAS SEGURAS DE PAID — regla de agencia, y Eli la nombró para QB.
 * «Ten cuidado… de repente necesitan las medidas de márgenes de paid. El texto
 *  es importante que no pueda ir fuera del margen.» (15-09-2026)
 *
 * ⚠️ En pieza ANIMADA se verifica en el ÚLTIMO fotograma, no en el primero.
 *
 * ⛔ MEDIDO: la ST de AYCD tal como está hoy NO pasa a paid — el logotipo
 * arranca en y=207 (43 px sobre el límite) y la lista de tragos llega a
 * y=1845, que son 265 px dentro de los 340 reservados. Como pieza orgánica
 * está bien. Preguntar «¿va a paid?» ANTES de diagramar.
 */
export const QB_ZONA_SEGURA = {top: 250, bottom: 340, right: 115, respiro: 60} as const;

// ───────────────────────────────────────────────────────────────────────────
// Fuentes auto-hospedadas
// ───────────────────────────────────────────────────────────────────────────
let qbFuentesInyectadas = false;

/**
 * Inyecta las fuentes de QB. Sin `delayRender` — con auto-hospedadas se cuelga
 * (memoria `reel-video-gotchas` §3).
 *
 * ⚠️ Bell MT viaja como `.TTF`, no como la `.otf` CFF que Chrome rechaza en
 * silencio. Ese silencio es lo que costó 27 piezas en Between: acá se verifica
 * con `qbFuentesListas()` antes de dar un render por bueno.
 */
export const cargarFuentesQB = () => {
  if (qbFuentesInyectadas || typeof document === "undefined") return;
  qbFuentesInyectadas = true;

  const cara = (familia: string, archivo: string, peso: number, estilo = "normal") => `
  @font-face {
    font-family: '${familia}';
    src: url('${staticFile(`assets/hilton/qb/fonts/${archivo}`)}') format('truetype');
    font-weight: ${peso};
    font-style: ${estilo};
    font-display: block;
  }`;

  const css = [
    cara("Raleway", "Raleway-Light.ttf", 300),
    cara("Raleway", "Raleway-Regular.ttf", 400),
    cara("Raleway", "Raleway-Medium.ttf", 500),
    cara("Raleway", "Raleway-SemiBold.ttf", 600),
    cara("Raleway", "Raleway-Bold.ttf", 700),
    cara("Raleway", "Raleway-ExtraBold.ttf", 800),
    cara("Raleway", "Raleway-Italic.ttf", 400, "italic"),
    cara("BellMT", "BELL.TTF", 400),
    cara("BellMT", "BELLI.TTF", 400, "italic"),
  ].join("\n");

  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  document.fonts.load("800 100px Raleway").catch(() => {});
  document.fonts.load("italic 400 100px Raleway").catch(() => {});
  document.fonts.load("italic 400 40px BellMT").catch(() => {});
};

/** ¿Cargaron de verdad? Se llama después de `cargarFuentesQB()`. */
export const qbFuentesListas = (): boolean => {
  if (typeof document === "undefined") return false;
  return (
    document.fonts.check("800 100px Raleway") &&
    document.fonts.check("italic 400 100px Raleway") &&
    document.fonts.check("italic 400 40px BellMT")
  );
};
