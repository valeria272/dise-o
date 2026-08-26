import {staticFile} from "remotion";

// ============================================================
// GRUPO REVEX (gruporevex.cl) — cliente · revestimientos y pavimentos
// Fuente de verdad de la marca. Manual: clients/revex/CLAUDE.md
// Marca hermana: Casablanca (src/brand/casablanca.ts) — NO mezclar.
// Gramática calibrada contra los 8 videos + estáticas de la diseñadora.
// ⭐ VALORES MEDIDOS con PIL sobre 82 referencias (raw/revex/ref/, 26-08-2026).
// Evidencia y examen de admisión: out/revex/adn/. Cada valor lleva su origen.
// ============================================================

export const revex = {
  colors: {
    // Son CUATRO rojos y NO son intercambiables (medidos px a px sobre 82 piezas)
    logoRed: "#D3152B", // el LOGOTIPO oficial — declarado por el archivo del cliente
    blockRed: "#D31A2B", // el CUADRO rojo que se dibuja detrás del logo — medido, 25,8% del corpus
    barRed: "#D31418", // barra de titular, botones y cajas de dato — medido, 46,0% del corpus (el más usado)
    tagRed: "#D92028", // banderola de producto — medido, 10,2% del corpus
    tagFold: "#AD1C27", // pliegue de la banderola — MEDIDO (corrige el #9E1420 anterior)
    outletYellow: "#FFD400", // subrayado marker del outlet, uso excepcional
    outletBlack: "#111111", // cajas inclinadas del outlet
    white: "#FFFFFF",
    ink: "#1A1A1A",
    ctaGray: "rgba(134,134,134,0.85)", // cápsula gris translúcida "¡Cotiza por WhatsApp!" (austral/cemento, se lee ≈#868686)
    // MEDIDO en rvx_post_1.mp4 (frame limpio vs. frame con velo): NO es un degradado
    // de página. Es una banda: 0% hasta y=150, meseta 15% de 150 a 380, a 0 en 590.
    veil: "rgba(0,0,0,0.15)", // la meseta
    veilBand: {start: 150, plateauEnd: 380, end: 590, opacity: 0.15},
  },
  fonts: {
    // ✅ CONFIRMADO por comparación glifo a glifo (18 letras aisladas de una pieza
    // real): la fuente ES Montserrat — error de proporción 3,3%, IoU de forma 91,3%.
    // Gotham queda descartado. Ver clients/revex/CLAUDE.md §ADN MEDIDO §4.
    display: "'Montserrat', 'Helvetica Neue', sans-serif",
    displayWeight: 775, // MEDIDO por grosor de asta de la L (dif −0,1%)
    displayTracking: "-0.045em", // MEDIDO — el titular se ajusta entre −0,04 y −0,05
    bajadaWeight: 400, // MEDIDO — la línea ligera va SIN tracking
    // Cursiva del gancho emocional ("Tu hogar merece", "Calgary")
    script: "'Sacramento', 'Snell Roundhand', cursive",
    mono: "'JetBrains Mono', ui-monospace, monospace",
  },
  name: "Grupo Revex",
  url: "gruporevex.cl",
  tagline: "Revestimientos de excelencia",
  category: "Revestimientos y pavimentos",
  logo: "assets/revex/logo_blanco.png", // NUNCA reescribir el wordmark en texto
  logoRojo: "assets/revex/logo_rojo.png", // logo completo rojo+negro — para el CIERRE ESTÁTICO blanco

  // MEDIDO: Paulina NO entrega a 1080 — entrega a 2250 px de ancho.
  formatos: {
    cuadrado: {w: 2250, h: 2250}, // norm 1080×1080
    feed: {w: 2250, h: 2813}, // norm 1080×1350 (4:5) — el que más usa
    story: {w: 2250, h: 4000}, // norm 1080×1920
  },

  whatsapp: {
    general: "+56 9 3203 5623",
    outlet: "+56 9 8902 8227", // Patio Outlet Quilicura — es OTRO número
  },
  sucursales: {
    lasCondes: "Av. Las Condes 9765 · Piso 1, Local 112 — Las Condes Design",
    // ⛔ Vitacura (Juan XXIII 6359) NO es de Revex — es el showroom de CASABLANCA.
    // Revex tiene 3 locales: Las Condes Design, Temuco y el Patio Outlet de Quilicura.
    // Corregido 25-08-2026 contra el Brief Diseño Septiembre de Serena.
    temuco: "Reyes Católicos 1550, Temuco",
    outlet: "Luis Olea 010, Quilicura",
  },

  // Cierre de video oficial (raw/revex/ref-drive/cierres/ y videos/*):
  // rojo pleno + logo blanco slide-up + dato de cierre (dirección en caja
  // blanca, o "Cotiza por WhatsApp" en cápsula outline).
  cierre: {
    durationInFrames: 151, // ≈5,03 s a 30 fps
    fps: 30,
    bg: "#D31A2B", // en el MP4 se lee #CB1725 por la compresión H.264
    feed: {w: 1080, h: 1350},
    story: {w: 2160, h: 3840}, // master 2× — se entrega a 1080×1920
  },

  // Geometría del sistema, en px sobre lienzo de 1080 de ancho.
  // Revex compone CENTRADO y denso; Casablanca compone abajo y con aire.
  layout: {
    // MEDIDO: cuadrado EXACTO de 187,7 y top=0 en el 100% de las piezas de feed.
    logoBlock: {w: 187.7, h: 187.7, logoW: 142.6, top: 0, logoPadTop: 33.1},
    // MEDIDO: en STORY el bloque NO es cuadrado, es vertical. top=0 también acá.
    logoBlockStory: {w: 214.1, h: 275.0, logoW: 162.7, top: 0},
    // MEDIDO: las tres posiciones horizontales que usa la diseñadora.
    logoBlockCx: {centro: 540, izquierda: 199.9, derecha: 857.0},
    hairline: 2, // filete blanco fino (solo piezas de sucursal)
    // MEDIDO: la barra se ajusta al ancho del texto y va centrada. Nunca ancho fijo.
    barTitular: {h: 79.2, padX: 23.5, padY: 19.5}, // cap-height del titular = 40,3
    barPadding: {x: 23.5, y: 19.5}, // alias histórico — MEDIDO (antes decía 26 × 10)
    barDato: {h: 44.6, padX: 16.1},
    capsula: {h: 52.3, stroke: 1.44, capText: 22.6}, // radio = h/2
    titular: {cap: 40.3, lineHeight: 1.16},
    storySafeBottom: 1270, // nada bajo esta Y en 1080×1920
  },
} as const;

// Fuentes locales vía @font-face — sin delayRender, para que el render no se cuelgue.
let revexFontsInjected = false;
export const ensureRevexFonts = () => {
  if (revexFontsInjected || typeof document === "undefined") return;
  revexFontsInjected = true;
  const style = document.createElement("style");
  style.textContent = `
  @font-face { font-family: 'Montserrat'; font-style: normal; font-weight: 100 900; font-display: block;
    src: url(${staticFile("assets/fonts/Montserrat.ttf")}) format('truetype'); }
  @font-face { font-family: 'Sacramento'; font-style: normal; font-weight: 400; font-display: block;
    src: url(${staticFile("assets/fonts/Sacramento.ttf")}) format('truetype'); }`;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) {
    ["400", "500", "700", "775", "800"].forEach((w) => f.load(`${w} 40px Montserrat`));
    f.load("400 60px Sacramento");
  }
};
