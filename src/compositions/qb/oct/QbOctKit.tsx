/**
 * QB · GRILLA OCTUBRE 2026 — piezas compartidas de las historias.
 *
 * No es una plantilla: cada historia es su propio archivo con su dirección de
 * arte escrita en la cabecera. Esto son sólo los ladrillos que SON de la marca y
 * no varían entre piezas (medidos en `src/brand/qb.ts` y `clients/qb/CLAUDE.md`):
 *
 *   · el logotipo oficial, blanco, centrado
 *   · el botón verde con su DEGRADADO y esquinas vivas (Eli: «no varía»)
 *   · las cifras de Raleway en caja alta (`lnum`)
 *   · el legal en itálica chica, centrado
 *   · «Imagen referencial» en todo material que no sea real — pedido del
 *     cliente en la grilla de octubre (STORIES, 22-10)
 *
 * ⛔ El encuadre de las fotos NUNCA se hace con `transform: scale()`: Chrome
 * rasteriza al tamaño del layout y después estira (manual §4e). `FotoQB` da a la
 * imagen su tamaño real.
 *
 * Mesa 1080×1920; se entrega a 2250×4000 con `--scale=2.0833`.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS, QB_BOTON_FONDO, QB_CIFRAS, QB_LOGO, qbColores} from "../../../brand/qb";

// ───────────────────────────────────────────────────────────────────────────
// Fuentes — las de `cargarFuentesQB()` más Brushwell y las itálicas con peso,
// que octubre necesita y la ST de AYCD no.
// ───────────────────────────────────────────────────────────────────────────
let inyectadas = false;
export const cargarFuentesQbOct = () => {
  if (inyectadas || typeof document === "undefined") return;
  inyectadas = true;
  const cara = (familia: string, archivo: string, peso: number, estilo = "normal") => `
  @font-face {
    font-family: '${familia}';
    src: url('${staticFile(`assets/hilton/qb/fonts/${archivo}`)}') format('truetype');
    font-weight: ${peso}; font-style: ${estilo}; font-display: block;
  }`;
  const css = [
    cara("Raleway", "Raleway-Light.ttf", 300),
    cara("Raleway", "Raleway-Regular.ttf", 400),
    cara("Raleway", "Raleway-Medium.ttf", 500),
    cara("Raleway", "Raleway-SemiBold.ttf", 600),
    cara("Raleway", "Raleway-Bold.ttf", 700),
    cara("Raleway", "Raleway-ExtraBold.ttf", 800),
    cara("Raleway", "Raleway-Italic.ttf", 400, "italic"),
    cara("Raleway", "Raleway-SemiBoldItalic.ttf", 600, "italic"),
    cara("Raleway", "Raleway-BoldItalic.ttf", 700, "italic"),
    cara("Raleway", "Raleway-BlackItalic.ttf", 900, "italic"),
    cara("BellMT", "BELL.TTF", 400),
    cara("BellMT", "BELLI.TTF", 400, "italic"),
    // ⚠️ Brushwell va en .ttf: la .otf CFF la rechaza Chrome en silencio.
    cara("Brushwell", "Brushwell.ttf", 400),
  ].join("\n");
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  for (const f of ["300 80px Raleway", "700 80px Raleway", "800 80px Raleway",
    "italic 400 80px Raleway", "italic 700 80px Raleway", "400 80px BellMT",
    "italic 400 80px BellMT", "400 80px Brushwell"]) {
    document.fonts.load(f).catch(() => {});
  }
};

export const MESA = {w: 1080, h: 1920} as const;
/** Zona segura de Meta sobre 1080×1920 (regla de agencia). */
export const SEGURA = {top: 250, bottom: 340, right: 115, left: 60} as const;

export const BLANCO = qbColores.blanco;
export const CIFRAS = QB_CIFRAS;

// ───────────────────────────────────────────────────────────────────────────
// Foto a sangre, encuadrada con su tamaño real
// ───────────────────────────────────────────────────────────────────────────
/**
 * `zoom` = cuánto más grande que la mesa se dibuja la foto; `cx`,`cy` = qué punto
 * de la foto (0–1) queda en el centro de la mesa. Se limita para no dejar bordes.
 */
export const FotoQB: React.FC<{
  src: string;
  /** proporción ancho/alto del archivo */
  ratio: number;
  zoom?: number;
  cx?: number;
  cy?: number;
  filtro?: string;
  /** Si es true, la foto puede quedar más chica que la mesa o corrida (el
   *  lienzo es negro): sirve para dejar aire arriba para el titular. */
  libre?: boolean;
  bajar?: number;
}> = ({src, ratio, zoom = 1, cx = 0.5, cy = 0.5, filtro, libre = false, bajar = 0}) => {
  // tamaño "cover" base
  const mesaRatio = MESA.w / MESA.h;
  let w = ratio > mesaRatio ? MESA.h * ratio : MESA.w;
  let h = ratio > mesaRatio ? MESA.h : MESA.w / ratio;
  w *= zoom;
  h *= zoom;
  let left = MESA.w / 2 - cx * w;
  let top = MESA.h / 2 - cy * h;
  if (!libre) {
    left = Math.min(0, Math.max(MESA.w - w, left));
    top = Math.min(0, Math.max(MESA.h - h, top));
  }
  top += bajar;
  return (
    <Img
      src={staticFile(src)}
      style={{position: "absolute", left, top, width: w, height: h, filter: filtro}}
    />
  );
};

/**
 * Grano de película, muy sutil (±2 niveles). Es textura, no efecto: evita que
 * las zonas donde el velo satura a negro queden como filas idénticas —que el QA
 * de agencia lee, con razón, como una foto estirada— y le quita lo plano al negro.
 * Determinista (feTurbulence con semilla fija): el mismo en cada render.
 * ⛔ 25-09: iba en `overlay` y overlay sobre NEGRO PURO no hace nada (negro sale
 * negro), así que justo donde el velo satura —que es donde el QA mira— las filas
 * seguían idénticas y la 08 y la 14 no pasaban. Va en mezcla normal al 2,5 %:
 * ±2–3 niveles en todas partes, también en el negro.
 */
export const Grano: React.FC<{opacidad?: number}> = ({opacidad = 0.025}) => (
  <svg width={MESA.w} height={MESA.h} style={{position: "absolute", inset: 0, opacity: opacidad,
    pointerEvents: "none"}}>
    <filter id="qb-grano"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7" />
      <feColorMatrix type="saturate" values="0" /></filter>
    <rect width="100%" height="100%" filter="url(#qb-grano)" />
  </svg>
);

/** Oscurecido de arriba y abajo para que el blanco lea (gramática de QB). */
export const Velo: React.FC<{
  arriba?: [number, number]; // [alto en px, opacidad]
  abajo?: [number, number];
  plano?: number;
}> = ({arriba = [700, 0.75], abajo = [800, 0.85], plano = 0}) => (
  <AbsoluteFill>
    {plano > 0 && <AbsoluteFill style={{background: `rgba(0,0,0,${plano})`}} />}
    <div style={{position: "absolute", top: 0, left: 0, right: 0, height: arriba[0],
      background: `linear-gradient(180deg, rgba(0,0,0,${arriba[1]}) 0%, rgba(0,0,0,${arriba[1] * 0.55}) 45%, rgba(0,0,0,0) 100%)`}} />
    <div style={{position: "absolute", bottom: 0, left: 0, right: 0, height: abajo[0],
      background: `linear-gradient(0deg, rgba(0,0,0,${abajo[1]}) 0%, rgba(0,0,0,${abajo[1] * 0.6}) 45%, rgba(0,0,0,0) 100%)`}} />
    <Grano />
  </AbsoluteFill>
);

// ───────────────────────────────────────────────────────────────────────────
// Logotipo — el oficial ya recortado a su alfa (proporción 1,642:1)
// ───────────────────────────────────────────────────────────────────────────
export const LogoQB: React.FC<{top: number; ancho?: number; color?: "blanco"}> = ({
  top,
  ancho = 180,
}) => (
  <Img
    src={staticFile(QB_ASSETS.logoBlanco)}
    style={{position: "absolute", top, left: (MESA.w - ancho) / 2, width: ancho,
      height: ancho / QB_LOGO.proporcion}}
  />
);

// ───────────────────────────────────────────────────────────────────────────
// El botón verde — degradado horizontal borde→centro→borde, esquinas VIVAS
// ───────────────────────────────────────────────────────────────────────────
export const BotonVerde: React.FC<{
  top: number;
  ancho: number;
  alto?: number;
  children: React.ReactNode;
  cuerpo?: number;
  peso?: number;
}> = ({top, ancho, alto = 86, children, cuerpo = 44, peso = 700}) => (
  <div style={{position: "absolute", top, left: (MESA.w - ancho) / 2, width: ancho,
    height: alto, background: QB_BOTON_FONDO, display: "flex", alignItems: "center",
    justifyContent: "center", color: BLANCO, fontFamily: "Raleway", fontWeight: peso,
    fontSize: cuerpo, letterSpacing: "0.02em", ...QB_CIFRAS}}>
    {children}
  </div>
);

// ───────────────────────────────────────────────────────────────────────────
// Texto centrado genérico
// ───────────────────────────────────────────────────────────────────────────
export const Linea: React.FC<{
  top: number;
  children: React.ReactNode;
  cuerpo: number;
  peso?: number;
  familia?: string;
  italica?: boolean;
  tracking?: string;
  interlinea?: number;
  mayus?: boolean;
  color?: string;
  sombra?: boolean;
  ancho?: number;
  izquierda?: number;
}> = ({top, children, cuerpo, peso = 400, familia = "Raleway", italica = false,
  tracking = "0", interlinea = 1.1, mayus = false, color = BLANCO, sombra = true,
  ancho, izquierda}) => (
  <div style={{position: "absolute", top, left: izquierda ?? (ancho ? (MESA.w - ancho) / 2 : SEGURA.left),
    width: ancho ?? MESA.w - 2 * SEGURA.left, textAlign: "center", color, fontFamily: familia,
    fontWeight: peso, fontStyle: italica ? "italic" : "normal", fontSize: cuerpo,
    letterSpacing: tracking, lineHeight: interlinea, textTransform: mayus ? "uppercase" : "none",
    textShadow: sombra ? "0 2px 18px rgba(0,0,0,0.45)" : "none", ...QB_CIFRAS}}>
    {children}
  </div>
);

/** Legal chico en Raleway itálica (el de la ST de AYCD). Sin punto final no:
 *  el legal es párrafo y SÍ lleva punto (regla Hilton §F). */
export const Legal: React.FC<{top: number; children: React.ReactNode; cuerpo?: number}> = ({
  top, children, cuerpo = 21,
}) => (
  <Linea top={top} cuerpo={cuerpo} italica interlinea={1.3} sombra={false}
    color="rgba(255,255,255,0.88)" ancho={880}>
    {children}
  </Linea>
);

/** «Imagen referencial» — obligatorio en material no real (cliente, oct-2026). */
export const ImagenReferencial: React.FC<{top?: number}> = ({top = 1556}) => (
  <Linea top={top} cuerpo={17} italica sombra={false} color="rgba(255,255,255,0.75)"
    ancho={600}>
    *Imagen referencial
  </Linea>
);

// ───────────────────────────────────────────────────────────────────────────
// ⭐ «ALL YOU CAN DRINK» — el nombre y el bloque del KV, con sus medidas
// (QB_AYCD en src/brand/qb.ts). Eli, 17-09: «botón verde con efecto de
// degradado y logo + el nombre no [varían]».
// ───────────────────────────────────────────────────────────────────────────
const AYCD_BOLD: React.CSSProperties = {fontWeight: 800, fontStyle: "normal"};
const aycdItalica = (t: string): React.CSSProperties => ({fontWeight: 400, fontStyle: "italic", letterSpacing: t});

/** Las dos líneas del nombre. `cuerpo` 109,4 es el del KV. `top` = tope de la versal de la línea 1. */
export const NombreAycd: React.FC<{top: number; cuerpo?: number}> = ({top, cuerpo = 109.4}) => {
  const k = cuerpo / 109.4;
  const altoLinea = cuerpo * 1.18;
  const ajuste = (altoLinea - 77.8 * k) * 0.62;
  const linea = (t: number, hijos: React.ReactNode) => (
    <div style={{position: "absolute", top: t - ajuste, left: 0, width: "100%", textAlign: "center",
      color: BLANCO, whiteSpace: "nowrap", fontFamily: "Raleway", fontSize: cuerpo,
      lineHeight: `${altoLinea}px`, textShadow: "0 3px 24px rgba(0,0,0,0.45)"}}>{hijos}</div>
  );
  return (
    <>
      {linea(top, <><span style={AYCD_BOLD}>ALL</span>{" "}<span style={aycdItalica("-0.024em")}>YOU</span></>)}
      {linea(top + 102.7 * k, <><span style={aycdItalica("-0.012em")}>CAN</span>{" "}<span style={AYCD_BOLD}>DRINK</span></>)}
    </>
  );
};

/** «TODOS LOS MARTES» + botón «POR $13.990» + «18:00 a 21:00 hrs», medidas del KV. */
export const BloqueAycd: React.FC<{
  antetitulo?: number; boton?: number; horario?: number;
  textoAntetitulo?: string; textoBoton?: string; textoHorario?: string;
}> = ({antetitulo = 1311.4, boton = 1364.6, horario = 1479.4,
  textoAntetitulo = "TODOS LOS MARTES", textoBoton = "POR $13.990", textoHorario = "18:00 a 21:00 hrs"}) => (
  <>
    <Linea top={antetitulo - 8} cuerpo={45} peso={600} tracking="0.045em">{textoAntetitulo}</Linea>
    <div style={{position: "absolute", top: boton, left: (MESA.w - 477.1) / 2, width: 477.1,
      height: 85.9, background: QB_BOTON_FONDO, display: "flex", alignItems: "center",
      justifyContent: "center", paddingTop: 6, color: BLANCO, fontFamily: "Raleway",
      fontWeight: 800, fontSize: 58.8, letterSpacing: "0.005em", ...QB_CIFRAS}}>{textoBoton}</div>
    <Linea top={horario - 6} cuerpo={44} peso={300} tracking="0.094em">{textoHorario}</Linea>
  </>
);
