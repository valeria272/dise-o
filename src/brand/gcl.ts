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
export const TITULAR = tokens.tipografia.titular;
export const CUERPO = tokens.tipografia.cuerpo;

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
  const caras: Array<[familia: string, archivo: string]> = [
    ["Space Grotesk", "SpaceGrotesk-Variable.woff2"],
    ["Inter", "Inter-Variable.woff2"],
  ];
  const css = caras
    .map(
      ([familia, archivo]) =>
        `@font-face { font-family: '${familia}'; font-weight: 100 900; font-display: block;
         src: url(${staticFile(`assets/fonts/gcl/${archivo}`)}) format('woff2'); }`,
    )
    .join("\n");
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) caras.forEach(([familia]) => {
    f.load(`700 80px '${familia}'`);
    f.load(`400 40px '${familia}'`);
  });
};
