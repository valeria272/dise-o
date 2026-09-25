// ============================================================================
// COPYWRITERS — Creative Operating System v1.0
// ----------------------------------------------------------------------------
// Este archivo NO es una plantilla. Es el diccionario del sistema: los colores,
// las cuatro voces y las fuentes. Lo que se compone con esto vive en cada pieza,
// una por archivo, con su propia dirección de arte.
//
// Regla madre del sistema (docs COPYWRITERS_CREATIVE_OS.md §1):
//   La consistencia viene de tipografía, dirección de arte, tratamiento
//   fotográfico, paleta, tono, composición, intervención y jerarquía.
//   NUNCA de repetir el mismo layout.
//
// Los valores viven en tokens.json y no se duplican acá: el agente social
// (Python) lee ese mismo archivo. Un color escrito dos veces es un color que
// algún día va a estar desincronizado.
// ============================================================================
import {staticFile} from "remotion";
import tokens from "./tokens.json";

export const CL = tokens;
export const C = tokens.colores;
export const FORMATOS = tokens.formatos;
export const TOPES = tokens.topes;

/** Las cuatro voces. Se citan por nombre, nunca por string suelto. */
export const VOZ = {
  impacto: "'CL Impacto', 'Archivo', Helvetica, Arial, sans-serif",
  /** Archivo Narrow — la cabeza que fija el pack de marca del 24-09-2026
   *  (03_TYPOGRAPHY). Es OTRA familia, no Archivo con el eje de ancho. */
  narrow: "'CL Narrow', 'Archivo Narrow', Helvetica, Arial, sans-serif",
  editorial: "'CL Editorial', 'DM Serif Display', Georgia, serif",
  data: "'CL Data', 'IBM Plex Mono', ui-monospace, monospace",
  /** Inter — texto funcional (MASTER 03). */
  funcional: "'CL Funcional', 'Inter', Arial, sans-serif",
  /** NO es voz de marca desde el 24-09-2026. Sólo piezas v1 ya entregadas. */
  mano: "'CL Mano', 'Caveat', cursive",
} as const;

export type Voz = keyof typeof VOZ;

// ---------------------------------------------------------------------------
// Fuentes
// ---------------------------------------------------------------------------
// Patrón TierraCalma/Selfie/Abakos: @font-face inyectado, sin delayRender —
// probado en decenas de entregas y no cuelga el render.
//
// ⚠️ Archivo es VARIABLE en dos ejes (wght 100–900, wdth 62–125). Es la razón
// de que exista una sola familia de impacto y no tres archivos distintos: el
// contraste entre condensada negra y extendida sale del mismo tipo, y por eso
// una pieza que juega con el ancho sigue leyéndose como la misma cabeza.
// El rango hay que declararlo en el @font-face o Chrome lo clampea a 100%.
let inyectadas = false;
export const asegurarFuentes = () => {
  if (inyectadas || typeof document === "undefined") return;
  inyectadas = true;
  const base = "assets/fonts/copywriters";
  const css = `
@font-face {
  font-family: 'CL Impacto';
  src: url(${staticFile(`${base}/Archivo-Variable.ttf`)}) format('truetype');
  font-weight: 100 900;
  font-stretch: 62% 125%;
  font-display: block;
}
@font-face {
  font-family: 'CL Narrow';
  src: url(${staticFile(`${base}/ArchivoNarrow-Variable.ttf`)}) format('truetype');
  font-weight: 400 700;
  font-display: block;
}
@font-face {
  font-family: 'CL Funcional';
  src: url(${staticFile(`${base}/Inter-Variable.ttf`)}) format('truetype');
  font-weight: 100 900;
  font-display: block;
}
@font-face {
  font-family: 'CL Editorial';
  src: url(${staticFile(`${base}/DMSerifDisplay-Italic.ttf`)}) format('truetype');
  font-style: italic; font-weight: 400; font-display: block;
}
@font-face {
  font-family: 'CL Editorial';
  src: url(${staticFile(`${base}/DMSerifDisplay-Regular.ttf`)}) format('truetype');
  font-style: normal; font-weight: 400; font-display: block;
}
@font-face {
  font-family: 'CL Data';
  src: url(${staticFile(`${base}/IBMPlexMono-Medium.ttf`)}) format('truetype');
  font-weight: 500; font-display: block;
}
@font-face {
  font-family: 'CL Data';
  src: url(${staticFile(`${base}/IBMPlexMono-Regular.ttf`)}) format('truetype');
  font-weight: 400; font-display: block;
}
@font-face {
  font-family: 'CL Mano';
  src: url(${staticFile(`${base}/Caveat-Variable.ttf`)}) format('truetype');
  font-weight: 400 700; font-display: block;
}`;
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  // Precarga explícita. Sin esto el still se captura con la serif de reemplazo
  // de Chrome y la pieza sale con OTRA tipografía sin avisar — que es
  // exactamente lo que pasó con Brushwell en las 27 piezas de Between.
  const f = (document as unknown as {fonts?: {load: (s: string) => Promise<unknown>}}).fonts;
  if (f) {
    [
      "900 200px 'CL Impacto'", "400 200px 'CL Impacto'",
      "700 200px 'CL Narrow'", "400 40px 'CL Funcional'",
      "italic 400 120px 'CL Editorial'", "400 120px 'CL Editorial'",
      "500 40px 'CL Data'", "400 40px 'CL Data'",
      "700 80px 'CL Mano'",
    ].forEach((s) => f.load(s));
  }
};

// ---------------------------------------------------------------------------
// Utilidades de composición
// ---------------------------------------------------------------------------

/** Eje de ancho de Archivo. 62 = condensada dura · 100 = normal · 125 = extendida. */
export const ancho = (wdth: number, wght = 900) =>
  `'wdth' ${wdth}, 'wght' ${wght}`;

/** Margen base como fracción del ancho. Punto de partida, no retícula:
 *  una pieza puede sangrar al borde si el concepto lo pide. */
export const margen = (W: number, k = 1) => Math.round(W * CL.margen.base * k);

/** Ruta a un asset del repo o URL pública. */
export const src = (f: string) =>
  /^https?:\/\//.test(f) ? f : staticFile(f);

/** Ruido determinista sembrado. Se usa para que las intervenciones a mano
 *  tiemblen como una mano y NO como un vector — pero igual salgan idénticas
 *  en cada render. Un garabato distinto en cada render es un render irreproducible. */
export const temblor = (semilla: number) => {
  let s = semilla * 9301 + 49297;
  return () => {
    s = (s * 9301 + 49297) % 233280;
    return s / 233280 - 0.5;
  };
};
