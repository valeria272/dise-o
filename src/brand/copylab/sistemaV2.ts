// ============================================================================
// COPYWRITERS — Sistema Visual (29-09-2026)
// ----------------------------------------------------------------------------
// El diccionario del sistema nuevo: colores, voces y fuentes. Reemplaza al
// Creative OS v1.0 (sistema.ts + tokens.json), que queda vivo SÓLO para no
// romper las piezas ya entregadas.
//
// Regla madre, del propio board: «Menos ruido. Más criterio.» La consistencia
// sale de la tipografía, la paleta, el gesto a mano y la jerarquía — no de
// repetir el mismo layout.
//
// Los valores viven en tokens-v2.json y no se duplican acá: un color escrito
// dos veces es un color que algún día va a estar desincronizado.
// ============================================================================
import {staticFile} from "remotion";
import tokens from "./tokens-v2.json";

export const CL2 = tokens;
export const C2 = tokens.colores;
export const FORMATOS2 = tokens.formatos;

/** Las cuatro voces. Se citan por nombre, nunca por string suelto.
 *
 *  Desde el 30-09-2026 `titular` y `mano` SÍ son las del board: Bebas Neue Pro y
 *  Balloon URW, sacadas de Adobe Fonts. Los archivos viven en public/ y NO van a
 *  git (ver .gitignore): la licencia de Adobe cubre renderizar local, no
 *  redistribuir el .otf. Si alguien clona el repo en otra máquina, las piezas
 *  caen al sustituto libre que quedó de fallback y no se rompe nada. */
export const VOZ2 = {
  /** Bebas Neue Pro — títulos principales. Caja alta siempre.
   *  Ancho normal: para líneas largas que tienen que caber. */
  titular: "'CL2 Titular', 'Bebas Neue Pro', 'Bebas Neue', Impact, sans-serif",
  /** Bebas Neue Pro SemiExpanded — LA VOZ DE LOS TITULARES Y LOS KPI.
   *  La referencia del 30-09 no es condensada: es ancha y pesada. Un KPI en el
   *  ancho normal se lee flaco y pierde la presencia publicitaria. */
  impacto: "'CL2 Impacto', 'Bebas Neue Pro SemiExp', Impact, sans-serif",
  /** Bebas Neue Pro Expanded ExtraBold — cuando el número ES la pieza. */
  bloque: "'CL2 Bloque', 'Bebas Neue Pro Exp', Impact, sans-serif",
  /** Balloon URW — destacados y notas a mano. La voz humana del sistema. */
  mano: "'CL2 Mano', 'Balloon URW', 'Caveat', cursive",
  /** Neue Haas Grotesk Text Pro — cuerpo de texto. El corte «Text» está dibujado
   *  para leerse en cuerpo chico; el «Display» es otro y NO va acá. */
  cuerpo: "'CL2 Cuerpo', 'Neue Haas Grotesk Text Pro', 'Inter', Helvetica, Arial, sans-serif",
  /** IBM Plex Mono — metadata y rótulos. Nunca es héroe. */
  data: "'CL2 Data', 'IBM Plex Mono', ui-monospace, monospace",
} as const;

export type Voz2 = keyof typeof VOZ2;

// ---------------------------------------------------------------------------
// Fuentes
// ---------------------------------------------------------------------------
// Patrón TierraCalma/Selfie/Abakos: @font-face inyectado, sin delayRender —
// probado en decenas de entregas y no cuelga el render.
let inyectadas = false;
export const asegurarFuentesV2 = () => {
  if (inyectadas || typeof document === "undefined") return;
  inyectadas = true;
  const base = "assets/fonts/copywriters";
  const css = `
@font-face {
  font-family: 'CL2 Titular';
  src: url(${staticFile(`${base}/BebasNeuePro-Light.otf`)}) format('opentype');
  font-weight: 300;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Titular';
  src: url(${staticFile(`${base}/BebasNeuePro-Regular.otf`)}) format('opentype');
  font-weight: 400;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Titular';
  src: url(${staticFile(`${base}/BebasNeuePro-Middle.otf`)}) format('opentype');
  font-weight: 500;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Titular';
  src: url(${staticFile(`${base}/BebasNeuePro-Bold.otf`)}) format('opentype');
  font-weight: 700;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Impacto';
  src: url(${staticFile(`${base}/BebasNeuePro-SemiExpBold.otf`)}) format('opentype');
  font-weight: 700;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Impacto';
  src: url(${staticFile(`${base}/BebasNeuePro-SemiExpExtraBold.otf`)}) format('opentype');
  font-weight: 800;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Bloque';
  src: url(${staticFile(`${base}/BebasNeuePro-ExpExtraBold.otf`)}) format('opentype');
  font-weight: 800;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Mano';
  src: url(${staticFile(`${base}/BalloonURW-Light.otf`)}) format('opentype');
  font-weight: 400;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Mano';
  src: url(${staticFile(`${base}/BalloonD-ExtraBold.otf`)}) format('opentype');
  font-weight: 800;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Mano';
  src: url(${staticFile(`${base}/BalloonURW-Bold.otf`)}) format('opentype');
  font-weight: 700;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Cuerpo';
  src: url(${staticFile(`${base}/NeueHaasGroteskText-Roman.otf`)}) format('opentype');
  font-weight: 400;
  font-style: normal;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Cuerpo';
  src: url(${staticFile(`${base}/NeueHaasGroteskText-Italic.otf`)}) format('opentype');
  font-weight: 400;
  font-style: italic;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Cuerpo';
  src: url(${staticFile(`${base}/NeueHaasGroteskText-Medium.otf`)}) format('opentype');
  font-weight: 500;
  font-style: normal;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Cuerpo';
  src: url(${staticFile(`${base}/NeueHaasGroteskText-Bold.otf`)}) format('opentype');
  font-weight: 700;
  font-style: normal;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Data';
  src: url(${staticFile(`${base}/IBMPlexMono-Medium.ttf`)}) format('truetype');
  font-weight: 500;
  font-display: block;
}`;
  const el = document.createElement("style");
  el.setAttribute("data-fuentes", "copywriters-v2");
  el.textContent = css;
  document.head.appendChild(el);
};

// ---------------------------------------------------------------------------
// Grano de papel
// ---------------------------------------------------------------------------
// El board pide textura de papel y de film. Se resuelve por código (SVG
// fractalNoise) y no con un JPG: así ninguna pieza depende de un asset que
// alguien puede mover, y el grano escala con el lienzo.
export const granoSVG = (opacidad: number, semilla = 7) =>
  `url("data:image/svg+xml;utf8,${encodeURIComponent(
    `<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>
      <filter id='g'>
        <feTurbulence type='fractalNoise' baseFrequency='0.82' numOctaves='4' seed='${semilla}'/>
        <feColorMatrix type='saturate' values='0'/>
      </filter>
      <rect width='300' height='300' filter='url(#g)' opacity='${opacidad}'/>
    </svg>`,
  )}")`;

// ---------------------------------------------------------------------------
// Trazos a mano
// ---------------------------------------------------------------------------
// Los elementos gráficos del board (flecha, subrayado, círculo) son trazo de
// marcador, NO iconos. Se dibujan como path con remate redondo y un temblor
// leve: una curva perfecta se lee como vector y delata el molde.

/** Subrayado de marcador: un solo trazo que cruza por debajo de la palabra. */
export const pathSubrayado = (ancho: number, alto: number) =>
  `M ${ancho * 0.02} ${alto * 0.62}` +
  ` C ${ancho * 0.22} ${alto * 0.12}, ${ancho * 0.48} ${alto * 0.92}, ${ancho * 0.72} ${alto * 0.38}` +
  ` S ${ancho * 0.93} ${alto * 0.2}, ${ancho * 0.99} ${alto * 0.5}`;

/**
 * Subrayado GRUESO con punta — el de la referencia del 30-09.
 *
 * No es un trazo de grosor parejo: un plumón real deja la marca ancha en el
 * medio y afilada donde entra y donde sale. Por eso va como área cerrada y no
 * como línea, con el vientre en el centro y las dos puntas en cero.
 */
export const pathTrazoGrueso = (ancho: number, alto: number, grosor: number) => {
  const p: string[] = [];
  const n = 26;
  const y = (t: number) =>
    alto * 0.5 + Math.sin(t * Math.PI * 1.35 + 0.4) * alto * 0.2 - t * alto * 0.1;
  // Filo de arriba, de izquierda a derecha.
  for (let i = 0; i <= n; i++) {
    const t = i / n;
    const g = grosor * Math.sin(Math.PI * Math.min(1, Math.max(0, t))) ** 0.55;
    p.push(`${i ? "L" : "M"} ${ancho * t} ${y(t) - g / 2}`);
  }
  // Y de vuelta por abajo.
  for (let i = n; i >= 0; i--) {
    const t = i / n;
    const g = grosor * Math.sin(Math.PI * Math.min(1, Math.max(0, t))) ** 0.55;
    p.push(`L ${ancho * t} ${y(t) + g / 2}`);
  }
  return p.join(" ") + " Z";
};

/** Sombra suave para separar tipografía clara de una fotografía clara.
 *  En la referencia el titular no flota: tiene una caída corta debajo. */
export const SOMBRA_SOBRE_FOTO = "0 6px 26px rgba(0,0,0,0.55), 0 2px 6px rgba(0,0,0,0.4)";

/** Flecha de anotación: cuerpo curvo + dos plumas. Devuelve los tres paths. */
export const pathsFlecha = (ancho: number, alto: number) => {
  const xf = ancho * 0.9;
  const yf = alto * 0.78;
  return {
    cuerpo:
      `M ${ancho * 0.06} ${alto * 0.16}` +
      ` C ${ancho * 0.38} ${alto * 0.06}, ${ancho * 0.7} ${alto * 0.3}, ${xf} ${yf}`,
    pluma1: `M ${xf} ${yf} L ${ancho * 0.6} ${alto * 0.68}`,
    pluma2: `M ${xf} ${yf} L ${ancho * 0.84} ${alto * 0.36}`,
  };
};
