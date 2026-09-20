/**
 * Kit de marca · COLEGIO HRVATSKA SKOLA SAN ESTEBAN (Antofagasta · cuenta REM)
 *
 * Valores MEDIDOS sobre las 7 gráficas aprobadas de septiembre 2026
 * (raw/san-esteban/ref-sep2026/). Manual: clients/san-esteban/CLAUDE.md
 *
 * ⛔ Colegio hermano: Antonio Rendic College — burdeo #661D33, arco, barra de
 *    valores y firma manuscrita. NO se mezclan. Ver clients/rendic/CLAUDE.md
 */
import {staticFile} from "remotion";

/** El abanico de 110 años: seis colores, siempre los seis. */
export const ABANICO = {
  purpura: "#6B489C",
  celeste: "#2899D5",
  amarillo: "#FED425",
  verde: "#7CC57F",
  naranja: "#F89D45",
  verdeagua: "#6CC0A6",
} as const;

export const COLORES = {
  /** El rojo institucional: caja del nombre y caja de bajada. */
  rojo: "#C0191A",
  /** LA barra del llamado a la acción. No confundir con el azul del escudo. */
  azulCTA: "#011689",
  /** Sólo dentro del logo. */
  azulEscudo: "#2A3E76",
  celesteEscudo: "#D2EDF3",
  /** Variante de CTA con texto azul — excepción documentada de sept-2026. */
  ambarCTA: "#E5B352",
  blanco: "#FFFFFF",
} as const;

export const FUENTES = {
  /** Poppins es SUSTITUTO MEDIDO, no la fuente confirmada del diseñador. */
  display: "Poppins",
  archivos: {
    extraBold: staticFile("assets/fonts/Poppins-ExtraBold.ttf"),
    bold: staticFile("assets/fonts/Poppins-Bold.ttf"),
    medium: staticFile("assets/fonts/Poppins-Medium.ttf"),
    regular: staticFile("assets/fonts/Poppins-Regular.ttf"),
  },
  /** Tracking medido: −0,04em en el titular grande, +0,012em en caja y CTA. */
  trackingTitular: "-0.04em",
  trackingCaja: "0.012em",
} as const;

export const ASSETS = {
  abanicoArriba: staticFile("assets/san-esteban/abanico-arriba.png"),
  abanicoAbajo: staticFile("assets/san-esteban/abanico-abajo.png"),
  escudo: staticFile("assets/san-esteban/escudo.png"),
  sello110: staticFile("assets/san-esteban/sello-110.png"),
  foto: (n: string) => staticFile(`assets/san-esteban/fotos/${n}.jpg`),
} as const;

/**
 * Zonas seguras del BRIEF DEL CLIENTE (manda sobre el estándar de agencia).
 * Reel 9:16 → 120 px arriba, 420 px abajo, columna derecha con los íconos.
 */
export const ZONAS_REEL = {top: 120, bottom: 420, right: 115} as const;

/** Geometría del bloque de identidad — escudo + sello SIEMPRE juntos. */
export const IDENTIDAD = {
  escudoRatio: 0.8353,
  selloRatio: 1.1486,
  /** Aire entre el pie del escudo y el techo del sello, medido en story. */
  aire: 38,
} as const;

export const CLIENTE = {
  nombre: "Colegio San Esteban",
  nombreCompleto: "Hrvatska Skola San Esteban",
  ciudad: "Antofagasta",
  aniversario: "110 años",
  web: "https://hssanesteban.cl",
  postulaciones: "http://sanestebanrem.postulaciones.colegium.com/",
} as const;
