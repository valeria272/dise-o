import {staticFile} from "remotion";

// ============================================================
// PISOS CASABLANCA (pisoscasablanca.cl) — by Grupo Revex
// Marca PREMIUM de pisos de ingeniería en madera. Manual:
// clients/casablanca/CLAUDE.md
// Hermana de Revex (src/brand/revex.ts) — comparten dueño, NO lenguaje.
// Acá NO existe el rojo, ni el descuento, ni la urgencia.
// ============================================================

export const casablanca = {
  colors: {
    gray: "#626260", // gris institucional: logo, banderola de producto, CTA
    grayDeep: "#4A4A48", // titular serif cuando va sobre fondo claro
    grayText: "#6B6B66", // bajadas sobre fondo claro
    sand: "#E3D9CE", // fondo bodegón/estudio de las piezas
    white: "#FFFFFF",
    // Paulina, 25-08-2026: "el sobreado siempre debe ser negro con opacidad".
    // Este archivo decía "velo cálido, jamás negro duro" y estaba MAL.
    veil: "rgba(0,0,0,0.34)",
    // Gris de la placa lateral del logo en el sistema editorial: es el gris
    // institucional entibiado, medido sobre las publicaciones del feed.
    grayWarm: "#6E6A63",
  },
  fonts: {
    // Dos registros de titular, los dos vivos en la marca:
    //  · display   — serif ITÁLICA, capitalización normal. Es el nombre del piso
    //                en los videos y en los carruseles de Paulina ("Roble Spritz").
    //  · editorial — serif de alto contraste en CAJA ALTA, para las piezas
    //                editoriales del feed ("ROBLE ASERRADO NATURAL UV").
    // Playfair es el sustituto histórico del Didone de la diseñadora; para la
    // caja alta se comparó contra la referencia y Bodoni Moda calza mejor
    // (contraste más alto, caja más ancha). Si la marca entrega su serif real,
    // se cambia acá y nada más.
    display: "'Playfair Display', Georgia, serif",
    editorial: "'Bodoni Moda', 'Playfair Display', Georgia, serif",
    sans: "'Montserrat', 'Helvetica Neue', sans-serif",
  },
  name: "Casablanca",
  fullName: "Pisos Casablanca by Grupo Revex",
  url: "pisoscasablanca.cl",
  tagline: "Elegancia, estilo y calidad es lo que nos diferencia.",
  category: "Pisos de ingeniería en madera natural",
  logo: "assets/casablanca/logo_gris.png", // marca gris + \"Casablanca®\" + \"by GRUPOREVEX\"
  logoOnWhiteCard: "assets/casablanca/logo_gris_fondo_blanco.png",
  logoWhite: "assets/casablanca/logo_blanco.png", // lockup APILADO en blanco
  // Lockup HORIZONTAL en blanco — es el que entra en la placa gris lateral del
  // sistema editorial. Se generó desde logo_horizontal_gris.png pintando el
  // trazo de blanco y conservando el alfa; no es un logo nuevo.
  logoWhiteH: "assets/casablanca/logo_horizontal_blanco.png",

  whatsapp: "+56 9 6653 5124",
  showroom: "Juan XXIII 6359, Vitacura",
  email: "casablanca@pisoscasablanca.cl",

  // Cierre de video oficial (raw/casablanca/ref-drive/cierres/ y videos/*):
  // fondo blanco + logo HORIZONTAL gris + "COTIZA POR WHATSAPP" en versales
  // grises bajo un filete. Sin URL — Casablanca cierra en WhatsApp.
  cierre: {
    durationInFrames: 152, // ≈5,07 s a 30 fps
    fps: 30,
    bg: "#FDFDFD",
    logoGray: "#4A504F",
    logoHorizontal: "assets/casablanca/logo_horizontal_gris.png",
    feed: {w: 1080, h: 1350},
    story: {w: 2160, h: 3840}, // master 2× — se entrega a 1080×1920
  },

  // Geometría del sistema, en px sobre lienzo de 1080 de ancho
  layout: {
    // Medido en las referencias: SIEMPRE cuelga del borde superior (top 0), centrada
    // Ronda 2 (25-08-2026): Paulina pidió achicar la tarjeta −20 % en feed y −15 % en
    // story. El top = 0 no se toca. Valores anteriores: 200×228 y 240×298.
    logoCard: {w: 160, h: 182, radiusBottom: 6, top: 0},
    logoCardStory: {w: 204, h: 253, top: 0}, // igual que feed: pegada al borde, NUNCA flotando
    hairline: 1, // filete finísimo sobre/bajo la bajada en versales
    subtitleTracking: 3.5, // px de letter-spacing en la bajada MAYÚSCULAS
    // Ronda 2: la etiqueta lleva categoría + medida y necesita ancho para que
    // "10/1.2 · 167 × 1200 mm" no deje "mm" solo en la segunda línea.
    tagFlag: {w: 366, h: 78, foldW: 34}, // caja gris de información de la muestra
    plank: {w: 150, borderWhite: 8}, // muestra vertical de la tabla, a la izquierda
    ctaRadiusPill: 999,
    storySafeBottom: 1270,
  },
} as const;

let casablancaFontsInjected = false;
export const ensureCasablancaFonts = () => {
  if (casablancaFontsInjected || typeof document === "undefined") return;
  casablancaFontsInjected = true;
  const style = document.createElement("style");
  style.textContent = `
    @font-face { font-family: 'Playfair Display'; font-style: italic; font-weight: 400 900; font-display: block;
      src: url(${staticFile("assets/fonts/PlayfairDisplay-Italic.ttf")}) format('truetype'); }
    @font-face { font-family: 'Playfair Display'; font-style: normal; font-weight: 400 900; font-display: block;
      src: url(${staticFile("assets/fonts/PlayfairDisplay.ttf")}) format('truetype'); }
    @font-face { font-family: 'Montserrat'; font-style: normal; font-weight: 100 900; font-display: block;
      src: url(${staticFile("assets/fonts/Montserrat.ttf")}) format('truetype'); }
    @font-face { font-family: 'Bodoni Moda'; font-style: normal; font-weight: 400 900; font-display: block;
      src: url(${staticFile("assets/fonts/BodoniModa.ttf")}) format('truetype'); }`;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) {
    f.load("italic 700 80px 'Playfair Display'");
    ["400", "500", "600"].forEach((w) => f.load(`${w} 90px 'Bodoni Moda'`));
    ["400", "600", "700"].forEach((w) => f.load(`${w} 40px Montserrat`));
  }
};
