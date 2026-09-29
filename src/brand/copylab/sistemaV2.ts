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
 *  ⚠️ `titular` y `mano` NO son las del board todavía: Bebas Neue Pro y URW
 *  Balloon no están activadas en Adobe. Ver `tokens-v2.json → fuentesPendientes`.
 *  El día que se activen, se cambia el @font-face de acá y nada más. */
export const VOZ2 = {
  /** Bebas Neue — títulos principales. Caja alta siempre. */
  titular: "'CL2 Titular', 'Bebas Neue', 'Bebas Neue Pro', Impact, sans-serif",
  /** Caveat — destacados y notas a mano. La voz humana del sistema. */
  mano: "'CL2 Mano', 'Caveat', 'URW Balloon', cursive",
  /** Inter — cuerpo de texto. */
  cuerpo: "'CL2 Cuerpo', 'Inter', Helvetica, Arial, sans-serif",
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
  src: url(${staticFile(`${base}/BebasNeue.ttf`)}) format('truetype');
  font-weight: 400;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Mano';
  src: url(${staticFile(`${base}/Caveat-Variable.ttf`)}) format('truetype');
  font-weight: 400 700;
  font-display: block;
}
@font-face {
  font-family: 'CL2 Cuerpo';
  src: url(${staticFile(`${base}/Inter-Variable.ttf`)}) format('truetype');
  font-weight: 100 900;
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
