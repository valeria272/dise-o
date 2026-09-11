import {staticFile} from "remotion";

// ============================================================
// SANTA GOTA (santagota.cl) — cliente · aceite de oliva pop
// Fuente de verdad para las piezas de TV y lo que venga después.
// Manual del cliente: clients/santa-gota/CLAUDE.md
//
// TODO lo de abajo está MEDIDO (11-09-2026) sobre el logo oficial
// (logo_lime_naranja.png), las 20 piezas del feed de septiembre y el
// pantallazo del e-commerce. Nada inventado. Si cambias un valor,
// anota de dónde salió.
// ============================================================

export const santagota = {
  colors: {
    lima: "#C3D600", // el subrayado de plumón del feed y la tapa del squeeze — «verde lima Santa Gota»
    limaTapa: "#7ED140", // tapa del 500 ml (medido en el e-commerce); no se usa como fondo
    verdeLogo: "#5C921C", // las letras del logo oficial
    naranja: "#F26513", // la cruz y la O del logo oficial
    botella: "#0E1C03", // el verde casi negro del envase — la tinta sobre lima (el par del packaging)
    tinta: "#000000", // la sombra de semitono del logo
    hueso: "#D2CEC5", // fondo cálido de las piezas de packshot del feed (hot-dog 25-09)
    blanco: "#FFFFFF", // logo plano y halo sobre foto
  },
  fonts: {
    // El feed mezcla Montserrat Bold (palabra clave) + Light (resto). Variable local 100–900.
    display: "'Montserrat', 'Helvetica Neue', sans-serif",
  },
  name: "SANTA GOTA",
  url: "SANTAGOTA.CL",
  concepto: "EL ACEITE QUE LLEGÓ A REVOLUCIONAR TU COCINA.",
  // Logo oficial: PNG 810×510 con sombra de semitono. Solo tenemos ESTE archivo (no hay vector).
  // Sobre fondo lima desaparece (verde sobre verde): va sobre botella, hueso o blanco.
  logo: "assets/santagota/logo-color.png",
  logoRatio: 810 / 510,
  // La monja del REEL (rodaje real, 1080×1920, 24 fps) — no la de las fotos del feed (esa es IA).
  monja: {
    plato: "assets/santagota/monja-sarten-nobg.png", // t=8,7 s: de frente, lentes redondos, sartén en la mano (nítida)
    // t=9,3 s (monja-plato-nobg.png) es el lanzamiento de la pasta: sale borrosa en still, sirve para el video.
  },
  // Formatos de TV (brief 11-09-2026). Los tres con alfa salvo el full screen.
  formatos: {
    huincha: {width: 1920, height: 216, fps: 29.97, seg: 7, alpha: true},
    virtual: {width: 775, height: 1080, fps: 29.97, seg: 20, alpha: true}, // ⚠️ plantilla del canal PENDIENTE
    full: {width: 1920, height: 1080, fps: 29.97, seg: 20, alpha: false}, // MXF NTSC
  },
} as const;

// Montserrat variable local vía @font-face — patrón NuevaUrbe/Casablanca: sin delayRender.
let fontsInjected = false;
export const ensureSantaGotaFonts = () => {
  if (fontsInjected || typeof document === "undefined") return;
  fontsInjected = true;
  const css = `@font-face { font-family: 'Montserrat'; font-style: normal; font-weight: 100 900; font-display: block;
      src: url(${staticFile("assets/fonts/Montserrat.ttf")}) format('truetype'); }`;
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) ["300", "700", "800", "900"].forEach((w) => f.load(`${w} 40px Montserrat`));
};
