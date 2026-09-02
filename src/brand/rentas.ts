// ============================================================
// RENTAS NUEVA URBE — Condominio Valle Altiplánico, Calama
// rentas.inu.cl · @rentasnuevaurbe
//
// ⚠️ NO es el kit de INU. Son dos marcas de la misma empresa con dos
// paletas: INU (venta, Travesía del Desierto II) usa #2050B4 + #CCE054;
// Rentas usa el azul brillante #1372F1 + lima #CCDC00. Ver src/brand/nuevaurbe.ts.
//
// Todo lo de acá está MEDIDO sobre las piezas de septiembre 2026 de
// Paulina Bustamante (raw/nuevaurbe/rentas/mail-sep2026/). Manual:
// clients/nueva-urbe/CLAUDE.md · ficha: clients/nueva-urbe/marca.json
// ============================================================
import {staticFile} from "remotion";

export const rentas = {
  colors: {
    /** El azul de la marca — 540.227 px del corpus, el más usado. */
    blue: "#1372F1",
    /** El lima del acento — 135.814 px. */
    lime: "#CCDC00",
    white: "#FFFFFF",
    /** Velo sobre la foto para que el texto blanco se lea. Medido en el tercio izquierdo. */
    veil: "rgba(0,0,0,0.38)",
  },

  fonts: {
    // Confirmada por comparación de glifos: IoU 84,7% contra el botón real.
    display: "'Montserrat', 'Helvetica Neue', sans-serif",
  },

  /** Tracking de las versales del botón — medido, no estimado. */
  trackingVersales: "0.02em",

  /** Los dos lienzos de entrega, medidos sobre las piezas de septiembre. */
  formatos: {
    feed: {ancho: 4500, alto: 5625},
    historia: {ancho: 4500, alto: 8000},
  },

  /**
   * La caja blanca del logo. Es la constante más fuerte de la marca, pero
   * CAMBIA DE SITIO según el formato: en feed cuelga de arriba, en historia
   * cuelga de ABAJO. Medido sobre las 10 piezas de septiembre.
   */
  cajaLogo: (formato: "feed" | "historia" | "mailing", anchoLienzo: number) => {
    const pct = formato === "feed" ? 0.242 : formato === "historia" ? 0.1751 : 0.102;
    const ancho = Math.round(anchoLienzo * pct);
    const altoRel = formato === "feed" ? 0.754 : formato === "historia" ? 0.888 : 0.94;
    const radioRel = formato === "feed" ? 0.179 : formato === "historia" ? 0.142 : 0.225;
    return {
      ancho,
      alto: Math.round(ancho * altoRel),
      /** El radio va en las esquinas OPUESTAS al borde del que cuelga. */
      radio: Math.round(ancho * radioRel),
      ancla: formato === "historia" ? ("abajo" as const) : ("arriba" as const),
      /** Centrada en feed e historia; en mailing va en 0,27. */
      ejeX: formato === "mailing" ? 0.27 : 0.5,
      /** El logotipo ocupa el 54 % del ancho de la caja y deja 17,8 % de aire arriba. */
      anchoLogotipo: Math.round(ancho * 0.542),
      aireSuperior: Math.round(ancho * altoRel * 0.178),
    };
  },

  /**
   * La caja de color abraza al texto: su alto es ~2× la altura de mayúsculas
   * que contiene. No tiene ancho fijo.
   */
  altoCajaColor: (alturaMayusculas: number) => Math.round(alturaMayusculas * 2.05),

  proyecto: {
    nombre: "Condominio Valle Altiplánico",
    ciudad: "Calama",
    direccion: "Av. Circunvalación 1458",
    modelos: "5 modelos disponibles",
    superficie: "desde 59 m²",
    tipologia: "2 y 3 dorms · 2 baños",
    precio: "$715.000",
    precioLargo: "desde $715.000 mensuales",
    amenidades: ["Quincho", "Cancha", "Juegos", "Gimnasio", "Conserjería 24/7"],
    web: "rentas.inu.cl",
    whatsapp: "+56 9 9707 9955",
    horario: "Lunes a viernes · 10:00 a 14:00 y 14:30 a 18:00 hrs.",
  },

  logos: {
    // ⛔ Todavía NO están bajados: viven en LOGOS INU / LOGOS RENTA (Drive cerrado).
    rentas: "assets/rentas/logo_rentas.png",
    rentasBlanco: "assets/rentas/logo_rentas_blanco.png",
    valle: "assets/rentas/logo_valle.png",
    valleBlanco: "assets/rentas/logo_valle_blanco.png",
  },
} as const;

let inyectadas = false;
export const ensureRentasFonts = () => {
  if (inyectadas || typeof document === "undefined") return;
  inyectadas = true;
  const css = `@font-face { font-family: 'Montserrat'; font-style: normal; font-weight: 100 900;
      font-display: block; src: url(${staticFile("assets/fonts/Montserrat.ttf")}) format('truetype'); }`;
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) ["300", "400", "600", "700", "800"].forEach((w) => f.load(`${w} 40px Montserrat`));
};
