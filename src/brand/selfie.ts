import {staticFile} from "remotion";

// ============================================================
// SELFIE (selfie.cl) — cliente · belleza y cuidado capilar
// Fuente de verdad para nuevas piezas: importar desde acá en vez
// de re-declarar colores/fuentes en cada composición.
// Manual completo del cliente: clients/selfie/CLAUDE.md
// ============================================================

export const selfie = {
  colors: {
    fucsia: "#FF007C", // fondo pleno del modo comercial (medido de piezas reales)
    fucsiaClaro: "#FF64AC", // píldoras/globos de diálogo y patrón de asteriscos
    paper: "#FFFFFF", // cajas redondeadas del mensaje central
    ink: "#1A1A1A", // texto oscuro sobre claro
    darkStudio: "#2E2A28", // fondo del modo editorial oscuro (Selfie Pro / fechas emotivas)
    sparkle: "#F5C544", // destellos dorados del modo editorial
  },
  fonts: {
    // Confirmado desde los editables del cliente (Drive > Editables Diseño > Fonts):
    // titulares en Agrandir (Pangram Pangram) — Grand Heavy 800 para display,
    // Wide Black Italic 900 para acentos, Narrow 400 para secundarios.
    display: "'Agrandir Grand', 'Poppins', 'Helvetica Neue', sans-serif",
    displayAccent: "'Agrandir Wide', 'Poppins', 'Helvetica Neue', sans-serif",
    narrow: "'Agrandir Narrow', 'Helvetica Neue', sans-serif",
    // Cuerpo, legales y subtítulos de reels "Selfie Clean Premium"
    body: "'Open Sans', 'Helvetica Neue', sans-serif",
    captions: "'Open Sans', 'Helvetica Neue', sans-serif",
  },
  name: "SELFIE",
  wordmark: "SELFI3*", // la E final invertida + asterisco — usar SIEMPRE el PNG oficial, nunca recrearlo
  url: "SELFIE.cl",
  instagram: "@selfie.beauty.pro",
  category: "E-commerce belleza y cuidado capilar",
  // Logos oficiales en Drive (bajar vía MCP; ver clients/selfie/CLAUDE.md):
  // negro: 15WMog1qrZoLXQYaZuvFDE09LKYqD1YNb · blanco: 1RjOjoUvOaXSdU29B77w3PORZyks3qCPa
  logo: "assets/selfie/logo-blanco.png",
  legales: {
    // Regla dura: toda promo lleva este legal (ajustar fecha), pequeño, centrado abajo
    promo: "No acumulable con otras promociones. Sujeto a stock por marca.",
  },
  formatos: {
    feed: {width: 2250, height: 2813}, // 4:5 — carruseles y posts
    story: {width: 2250, height: 4000}, // 9:16 — stories y banners verticales
    reel: {width: 1080, height: 1920},
  },
} as const;

// Fuentes locales (public/assets/fonts/selfie/, gitignored — Agrandir es de pago,
// licencia del cliente; los OTF vienen de sus editables) vía @font-face —
// patrón TierraCalma/Abakos: sin delayRender, no se cuelga el render.
let selfieFontsInjected = false;
export const ensureSelfieFonts = () => {
  if (selfieFontsInjected || typeof document === "undefined") return;
  selfieFontsInjected = true;
  const faces: Array<[family: string, weight: number, style: string, file: string, format: string]> = [
    ["Agrandir Grand", 800, "normal", "Agrandir-GrandHeavy-800.otf", "opentype"],
    ["Agrandir Wide", 900, "italic", "Agrandir-WideBlackItalic-900.otf", "opentype"],
    ["Agrandir Narrow", 400, "normal", "Agrandir-Narrow-400.otf", "opentype"],
    ["Open Sans", 400, "normal", "OpenSans-Regular.ttf", "truetype"],
    ["Open Sans", 600, "normal", "OpenSans-SemiBold.ttf", "truetype"],
    ["Open Sans", 700, "normal", "OpenSans-Bold.ttf", "truetype"],
    ["Open Sans", 800, "normal", "OpenSans-ExtraBold.ttf", "truetype"],
  ];
  const css = faces
    .map(
      ([family, weight, style, file, format]) =>
        `@font-face { font-family: '${family}'; font-style: ${style}; font-weight: ${weight}; font-display: block;
        src: url(${staticFile(`assets/fonts/selfie/${file}`)}) format('${format}'); }`,
    )
    .join("\n");
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) faces.forEach(([family, weight, st]) => f.load(`${st} ${weight} 40px '${family}'`));
};
