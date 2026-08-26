import {staticFile} from "remotion";

// ============================================================
// EBEMA S.A. / EBEMA CLICK — materiales para la construcción
// Manual: clients/ebema/CLAUDE.md · Ficha: clients/ebema/marca.json
// Sistema de gráficas (HTML/CSS): clients/ebema/sistema/base.css
//
// Dos marcas, tres esquemas. Antes de componer, decidir cuál aplica:
//   sucursal → marco blanco + puntitos + píldora de ciudad
//   click    → sin marco, lockup centrado, columna al lado de la persona
//   spc      → sin marco, contenido anclado bajo el logo
// ============================================================

export const ebema = {
  name: "Ebema",
  fullName: "Ebema S.A.",
  clickName: "Ebema Click",
  url: "ebema.cl",
  clickUrl: "ebema.cl/ebemaclick",
  category: "Materiales para la construcción",

  colors: {
    red: "#EC1C23", // EL rojo. Único. No es #ED1C24.
    gray: "#6D6F72", // gris institucional del logo
    yellow: "#FFFF00", // del kit — uso excepcional, sólo si el brief lo pide
    white: "#FFFFFF",
    text: "#1A1A1A",
    veil: "rgba(0,0,0,0.30)", // velo estándar sobre foto
    veilStrong: "rgba(0,0,0,0.36)", // Click
    veilExtra: "rgba(0,0,0,0.46)", // fotos muy claras
  },

  fonts: {
    // Raleway para todo el texto. Helvetica Bold SOLO para cifras.
    display: "'Raleway', 'Helvetica Neue', sans-serif", // 900 en titulares
    sans: "'Raleway', 'Helvetica Neue', sans-serif",
    numbers: "'HelvKit', Helvetica, Arial, sans-serif", // 700 — obligatorio en toda cifra
  },

  // Pesos con nombre, para no escribir números mágicos en las composiciones
  weights: {titular: 900, enfasis: 800, ui: 600, cuerpo: 400, numeros: 700},

  logos: {
    ebemaCirculo: "assets/ebema/logos/logo_ebema_circulo.png",
    click: "assets/ebema/logos/logo_click_2_blanco_acento.png", // sobre imagen — el habitual
    clickGris: "assets/ebema/logos/logo_click_1_gris.png", // sobre fondo blanco
    clickRojo: "assets/ebema/logos/logo_click_3_click_rojo.png", // sobre fondo rojo
  },

  // Geometría del sistema, en px sobre lienzo de 1080 de ancho.
  // Medida sobre ebema_Antofagasta_post.png — espejo exacto de clients/ebema/sistema/base.css
  layout: {
    marco: {borde: 3, radio: 20, insetX: 62, insetTop: 77, insetBottom: 71},
    // La caja del logo SALE del borde superior. top:0 en feed y en story. Nunca flota.
    logoBox: {x: 139, top: 0, w: 152, h: 186, radiusBottom: 14, logoW: 103},
    pildora: {top: 255, borde: 2.5, fontSize: 34, padX: 44, padY: 13},
    titular: {cajaRojaTopEm: 0.55, baseFeed: 74, baseStory: 84},
    bajada: {fontSize: 28, lineHeight: 1.22, maxW: 640},
    boton: {fontSize: 24, radio: 6, shadow: false}, // sin sombra — corrección de Paulina
    puntitos: {n: 3, d: 24, barraW: 108, anillo: 2, right: 95, bottom: 57},
    chipSpc: {d: 132, radio: 12, borde: 5}, // recortado POR DENTRO (por fuera = doble línea)
    // Zonas seguras Meta — protegen el TEXTO, no el logo
    storySafeTop: 250,
    storySafeBottom: 1580, // 1920 - 340
  },

  formats: {
    feed: {w: 1080, h: 1350},
    story: {w: 1080, h: 1920},
    mailing: {w: 1200, h: 1643}, // artboard del kit oficial
  },

  cta: {
    sucursal: "Cotiza por WhatsApp",
    click: "Regístrate Gratis",
  },

  // Cierre oficial de Paulina. TODO reel de EBEMA termina con esto, sin rediseñar.
  cierre: {
    fps: 30,
    ebemaPost: "assets/ebema/cierres/cierre_ebema_post.mp4",
    ebemaStory: "assets/ebema/cierres/cierre_ebema_st.mp4",
    clickPost: "assets/ebema/cierres/cierre_ebemaclick_post.mp4",
    clickStory: "assets/ebema/cierres/cierre_ebemaclick_st.mp4",
    // variantes _mute y último frame _last.png en la misma carpeta
  },

  vo: {voice: "es-CL-Lorenzo", dir: "assets/ebema/vo/"},

  sucursales: [
    "Antofagasta", "Coquimbo", "La Calera", "Quilicura", "San Bernardo",
    "Rancagua", "Talca", "Chillán", "Concepción", "Temuco", "Puerto Montt",
  ],
  // Sin foto real todavía — ver clients/ebema/CHECKLIST-CLIENTE.md
  sucursalesSinFoto: ["Chillán", "Rancagua", "San Bernardo"],
} as const;

/**
 * Envuelve toda cifra del texto en Helvetica Bold.
 * Regla dura de Paulina: precios, códigos, porcentajes, medidas y "24/7" van en
 * Helvetica Bold. Equivale a num() de clients/ebema/sistema/build_ejemplo.py.
 *
 * Devuelve trozos para renderizar; el llamador aplica la fuente a los `isNumber`.
 */
export const splitNumbers = (text: string): {text: string; isNumber: boolean}[] => {
  const parts: {text: string; isNumber: boolean}[] = [];
  const re = /\$?\d[\d.,/%]*/g;
  let last = 0;
  for (let m = re.exec(text); m !== null; m = re.exec(text)) {
    if (m.index > last) parts.push({text: text.slice(last, m.index), isNumber: false});
    parts.push({text: m[0], isNumber: true});
    last = m.index + m[0].length;
  }
  if (last < text.length) parts.push({text: text.slice(last), isNumber: false});
  return parts;
};

/** Rutas absolutas de los assets, listas para <Img src={...}> */
export const ebemaAsset = (path: string) => staticFile(path);
