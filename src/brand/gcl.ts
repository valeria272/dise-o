// ============================================================================
// GCL — sistema visual del feed de Grupo Copylab (@copywriters.cl)
// ----------------------------------------------------------------------------
// Decisión Valeria, 02-09-2026: el feed adopta el sistema del **Agente G**
// (negro profundo + rosado eléctrico + coral), que ya estaba escrito y era
// obligatorio en `gcl-agent/GCL_CHARACTER_BIBLE.md` y que la propuesta externa
// reprodujo casi exacta. El lime + navy de `copywriters.ts` **se queda en la web
// y en la pauta**; en el feed no se usa más.
//
// Los valores viven en `gcl.tokens.json` y NO se duplican acá: el agente social
// (Python) lee ese mismo archivo para escribir los copys y validar las piezas.
// Un color escrito dos veces es un color que algún día va a estar desincronizado.
// ============================================================================
import {staticFile} from "remotion";
import tokens from "./gcl.tokens.json";

export const GCL = tokens;
export const C = tokens.colores;

// Las cuatro voces del MASTER SYSTEM v1.0. Cada una tiene un trabajo y no se
// intercambian: display afirma, editorial opina, sans informa, mono rotula.
export const DISPLAY = tokens.tipografia.display;
export const EDITORIAL = tokens.tipografia.editorial;
export const SANS = tokens.tipografia.sans;
export const MONO = tokens.tipografia.mono;
/** La mano encima de la pieza: sólo para las notas al margen. */
export const MANUSCRITA = tokens.tipografia.manuscrita;

// Nombres del sistema anterior. GclPost y el agente social los usan; se dejan
// apuntando a lo nuevo para no romperlos de golpe.
export const TITULAR = tokens.tipografia.titular;
export const CUERPO = tokens.tipografia.cuerpo;

/** Archivo variable apretado: es como se consigue «Archivo Narrow Black» sin
 *  comprar una licencia aparte. `ancho` 62 es lo más angosto que da la fuente;
 *  75-80 es el punto donde todavía se lee cómodo en un titular grande. */
export const narrow = (peso = 900, ancho = 76) => ({
  fontFamily: DISPLAY,
  fontWeight: peso,
  fontVariationSettings: `"wdth" ${ancho}, "wght" ${peso}`,
});

export const gradiente = (par: readonly string[], angulo = 135) =>
  `linear-gradient(${angulo}deg, ${par[0]} 0%, ${par[1]} 100%)`;

export const CALOR = gradiente(tokens.gradientes.calor);
export const PROFUNDO = gradiente(tokens.gradientes.profundo);

// Fuentes locales vía @font-face, patrón TierraCalma/Selfie: sin delayRender,
// así el render no se cuelga esperando a la red. Son variables (un archivo cubre
// todos los pesos), por eso el rango 100–900.
let inyectadas = false;
export const asegurarFuentesGcl = () => {
  if (inyectadas || typeof document === "undefined") return;
  inyectadas = true;
  // [familia, archivo, rango de pesos, estilo]. Archivo e Inter son variables
  // (un archivo cubre todos los pesos); DM Serif e IBM Plex vienen en cortes.
  const caras: Array<[string, string, string, string]> = [
    ["Archivo", "Archivo-Variable.woff2", "100 900", "normal"],
    ["Inter", "Inter-Variable.woff2", "100 900", "normal"],
    ["DM Serif Display", "DMSerifDisplay-Regular.woff2", "400", "normal"],
    ["DM Serif Display", "DMSerifDisplay-Italic.woff2", "400", "italic"],
    ["IBM Plex Mono", "IBMPlexMono-Regular.woff2", "400", "normal"],
    ["IBM Plex Mono", "IBMPlexMono-Medium.woff2", "500", "normal"],
    ["Caveat", "Caveat-Variable.woff2", "400 700", "normal"],
    // Space Grotesk se queda mientras GclPost siga usándola.
    ["Space Grotesk", "SpaceGrotesk-Variable.woff2", "100 900", "normal"],
  ];
  const css = caras
    .map(
      ([familia, archivo, peso, estilo]) =>
        `@font-face { font-family: '${familia}'; font-weight: ${peso}; font-style: ${estilo};
         font-display: block;
         src: url(${staticFile(`assets/fonts/gcl/${archivo}`)}) format('woff2'); }`,
    )
    .join("\n");
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) caras.forEach(([familia]) => {
    f.load(`900 120px '${familia}'`);
    f.load(`700 80px '${familia}'`);
    f.load(`400 40px '${familia}'`);
    f.load(`italic 400 60px '${familia}'`);
  });
};
