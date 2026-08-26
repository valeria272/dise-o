import {staticFile} from "remotion";

// ============================================================
// ABAKOS (abakos.cl) — cliente · préstamos personales online
// Fuente de verdad para nuevas piezas: importar desde acá en vez
// de re-declarar colores/fuentes en cada composición.
// Manual completo del cliente: clients/abakos/CLAUDE.md
// ============================================================

export const abakos = {
  colors: {
    purple: "#433491", // morado corporativo (wordmark)
    magenta: "#EE00A8",
    orange: "#FC8222",
    yellow: "#FFB533",
    ink: "#2B2450", // texto oscuro sobre claro
    paper: "#FFFFFF",
    cream: "#F7F5FF", // fondo claro de marca
  },
  fonts: {
    display: "'Poppins', 'Helvetica Neue', sans-serif",
    mono: "'JetBrains Mono', ui-monospace, monospace",
  },
  name: "Abakos",
  url: "abakos.cl",
  tagline: "Préstamo personal online las 24 horas.",
  category: "Fintech / Créditos de consumo",
  logo: "assets/abakos/logo.svg", // vector oficial — NUNCA recrear el wordmark en texto
};

// Poppins local (public/assets/fonts/Poppins-*.ttf) vía @font-face —
// patrón TierraCalma: sin delayRender, no se cuelga el render.
let abakosFontsInjected = false;
export const ensureAbakosFonts = () => {
  if (abakosFontsInjected || typeof document === "undefined") return;
  abakosFontsInjected = true;
  const css = [400, 500, 600, 700, 800]
    .map(
      (w, i) => `@font-face { font-family: 'Poppins'; font-style: normal; font-weight: ${w}; font-display: block;
      src: url(${staticFile(`assets/fonts/Poppins-${["Regular", "Medium", "SemiBold", "Bold", "ExtraBold"][i]}.ttf`)}) format('truetype'); }`,
    )
    .join("\n");
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) ["400", "500", "600", "700", "800"].forEach((w) => f.load(`${w} 40px Poppins`));
};
