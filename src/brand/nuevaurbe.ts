import {staticFile} from "remotion";

// ============================================================
// INMOBILIARIA NUEVA URBE (inu.cl) — cliente · casas en Calama
// + RENTAS NUEVA URBE (rentas.inu.cl) — arriendo Valle Altiplánico
// Fuente de verdad para nuevas piezas. Manual: memoria nueva-urbe-brand.
// Drive del cliente: INMOBILIARIA NUEVA URBE (1PR94HGA24__G2OahS20uZM0BPDqrdmU6)
// ============================================================

export const nuevaurbe = {
  colors: {
    blue: "#2050B4", // azul royal de TODAS sus piezas/reels (muestreado de la story INU Days 2026)
    blueDeep: "#0B1686", // azul navy del wordmark (#001080) — para textos sobre blanco / sombras
    lime: "#CCE054", // lima de las piezas (muestreado); el del logo es #C0D000
    sky: "#5AC8D8", // celeste de las cajas de texto en las piezas 2025-26
    paper: "#FFFFFF",
    ink: "#0B1238",
    sand: "#F3EFE6", // claro cálido (paleta tierra de las piezas de valor 2026)
    earth: "#5A3A2A", // café del logo Travesía del Desierto II
  },
  fonts: {
    display: "'Montserrat', 'Helvetica Neue', sans-serif", // la tipografía de TODAS sus piezas (a de dos pisos, geométrica)
    serif: "'Montserrat', 'Helvetica Neue', sans-serif", // sin serif: la marca no la usa (feedback 22-08)
  },
  name: "Inmobiliaria Nueva Urbe",
  url: "inu.cl",
  tagline: "Tu hogar es nuestro norte",
  whatsapp: "+569 9707 9951", // Travesía del Desierto II (Rosa Gana)
  logos: {
    inu: "assets/nuevaurbe/logo_inu.png", // color, fondo transparente (con tagline)
    inuWhite: "assets/nuevaurbe/logo_inu_blanco.png",
    travesia: "assets/nuevaurbe/logo_travesia_.png", // café
    travesiaWhite: "assets/nuevaurbe/logo_travesia_blanco.png",
  },
  // Reglas duras de copy (Sheet "INFORMACIÓN PROYECTOS" del cliente):
  // sin "descuentos" fuera de INU Days · sin "la mejor vista" · sin casino ·
  // seguridad no es producto · NO HAY SUBSIDIO · no usar "hasta" · sin
  // "exclusivo/privilegiado" · aeropuerto nunca como primer atributo.
  // Precios siempre "Desde UF X*" + "*Descuentos aplicados".
};

let fontsInjected = false;
export const ensureNuevaUrbeFonts = () => {
  if (fontsInjected || typeof document === "undefined") return;
  fontsInjected = true;
  // Montserrat variable (wght 100–900) local — sin delayRender, no se cuelga el render.
  const css = `@font-face { font-family: 'Montserrat'; font-style: normal; font-weight: 100 900; font-display: block;
      src: url(${staticFile("assets/fonts/Montserrat.ttf")}) format('truetype'); }`;
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) ["400", "500", "600", "700", "800", "900"].forEach((w) => f.load(`${w} 40px Montserrat`));
};
