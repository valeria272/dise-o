/**
 * SANTA GOTA · spot de TV «UNA GOTA. CAMBIA TODO.» — base común.
 *
 * Full screen 1920×1080 · NTSC 29,97 · máx. 20 s (599 cuadros = 19,987 s).
 * Ruta final SIN MONJA (handoff 15-09-2026, Production Bible V2).
 *
 * Reglas que este módulo impone por construcción:
 *  - El packaging entra SOLO como packshot oficial (public/assets/santagota/producto/),
 *    escalado uniforme: nunca `width` y `height` a la vez → la proporción no se toca.
 *  - Zona defensiva: el canal monta la huincha del auspiciador sobre los 216 px
 *    superiores del full screen (medido en el ejemplo de TVN del 09-02-2026).
 *    Ningún copy ni logo vive arriba de HUINCHA_Y.
 *  - Title safe 5 % (96 px a los lados, 54 px arriba/abajo).
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {santagota as SG, ensureSantaGotaFonts} from "../../../brand/santagota";

export const W = 1920;
export const H = 1080;
export const FPS = 29.97;
export const DUR_SPOT = 599; // 19,987 s — 20,000 s serían 599,4 cuadros y no se pasa ni uno
export const C = SG.colors;

export const SAFE_X = 96;
export const SAFE_Y = 54;
export const HUINCHA_Y = 216; // reserva defensiva: la huincha del canal puede tapar hasta acá

export const PLATES = "assets/santagota/spot/plates";
export const PROD = "assets/santagota/spot/producto"; // packshots oficiales con luz integrada (PIL)

export const useSpot = () => {
  ensureSantaGotaFonts();
};

/** Placa de fondo a sangre (foto generada: comida, aceite, fuego, set). */
export const Placa: React.FC<{src: string; op?: number; style?: React.CSSProperties}> = ({src, op = 1, style}) => (
  <Img src={staticFile(`${PLATES}/${src}`)}
       style={{position: "absolute", inset: 0, width: W, height: H, objectFit: "cover", opacity: op, ...style}} />
);

/** Viñeta suave para asentar el copy sin tapar la foto. */
export const Vineta: React.FC<{op?: number; lado?: "izq" | "der" | "abajo" | "centro"}> = ({op = 0.55, lado = "abajo"}) => {
  const g =
    lado === "izq" ? `linear-gradient(90deg, rgba(0,0,0,${op}) 0%, rgba(0,0,0,0) 55%)` :
    lado === "der" ? `linear-gradient(270deg, rgba(0,0,0,${op}) 0%, rgba(0,0,0,0) 55%)` :
    lado === "centro" ? `radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0) 30%, rgba(0,0,0,${op}) 100%)` :
    `linear-gradient(0deg, rgba(0,0,0,${op}) 0%, rgba(0,0,0,0) 50%)`;
  return <div style={{position: "absolute", inset: 0, background: g, pointerEvents: "none"}} />;
};

/**
 * Copy del spot. Montserrat 900, mayúscula, tracking −0,02 em, sombra de TV.
 * `lima` colorea la palabra protagonista. Cap height ≥ 40 px siempre (size ≥ 56).
 */
export const Copy: React.FC<{
  x: number; y: number; size: number; weight?: number; align?: "left" | "center" | "right";
  lh?: number; op?: number; style?: React.CSSProperties; children: React.ReactNode;
}> = ({x, y, size, weight = 900, align = "left", lh = 0.96, op = 1, style, children}) => (
  <div style={{
    position: "absolute", top: y, zIndex: 20, opacity: op,
    ...(align === "center" ? {left: 0, right: 0, textAlign: "center"} : align === "right" ? {right: x, textAlign: "right"} : {left: x}),
    fontFamily: SG.fonts.display, fontWeight: weight, fontSize: size, lineHeight: lh, letterSpacing: "-0.02em",
    textTransform: "uppercase", color: "#FFFFFF", whiteSpace: "nowrap",
    textShadow: "0 3px 24px rgba(0,0,0,0.55), 0 1px 2px rgba(0,0,0,0.6)", ...style,
  }}>
    {children}
  </div>
);
export const Lima: React.FC<{children: React.ReactNode}> = ({children}) => <span style={{color: C.lima}}>{children}</span>;

/**
 * Packshot oficial de pie sobre una superficie reflectante.
 * `h` fija la ALTURA; el ancho sale de la proporción real del PNG (nunca se estira).
 * `pisoY` es la fila donde apoya. El reflejo es una copia invertida con máscara.
 */
export const Producto: React.FC<{
  src: string; ratio: number; cx: number; pisoY: number; h: number; z?: number;
  reflejo?: number; rot?: number; op?: number;
}> = ({src, ratio, cx, pisoY, h, z = 10, reflejo = 0.28, rot = 0, op = 1}) => {
  const w = h / ratio; // ratio = alto/ancho del PNG recortado
  const x = cx - w / 2;
  const y = pisoY - h;
  const img = staticFile(`${PROD}/${src}`);
  return (
    <>
      {reflejo > 0 && (
        <Img src={img} style={{
          position: "absolute", left: x, top: pisoY, width: w, height: h, zIndex: z - 1, opacity: reflejo * op,
          transform: `scaleY(-1) rotate(${-rot}deg)`, transformOrigin: "50% 0%",
          WebkitMaskImage: "linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 55%)",
          maskImage: "linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 55%)",
          filter: "blur(1.2px)",
        }} />
      )}
      {/* sombra de contacto: el pie de la botella oscurece la superficie */}
      <div style={{
        position: "absolute", left: cx - w * 0.62, top: pisoY - 10, width: w * 1.24, height: 26, zIndex: z - 2, opacity: 0.75 * op,
        background: "radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 70%)",
      }} />
      <Img src={img} style={{
        position: "absolute", left: x, top: y, width: w, height: h, zIndex: z, opacity: op,
        transform: `rotate(${rot}deg)`, transformOrigin: "50% 100%",
      }} />
    </>
  );
};

/** Logo oficial (PNG a color, único original). Nunca sobre lima. */
export const LogoOficial: React.FC<{x: number; y: number; w: number; z?: number; align?: "left" | "center"}> = ({x, y, w, z = 20, align = "left"}) => (
  <Img src={staticFile(SG.logo)} style={{
    position: "absolute", top: y, width: w, height: w / SG.logoRatio, zIndex: z,
    ...(align === "center" ? {left: (W - w) / 2} : {left: x}),
    filter: "drop-shadow(0 8px 28px rgba(0,0,0,0.55))",
  }} />
);

export const Fondo: React.FC<{color?: string; children?: React.ReactNode}> = ({color = "#000", children}) => (
  <AbsoluteFill style={{backgroundColor: color, overflow: "hidden"}}>{children}</AbsoluteFill>
);

// Proporciones reales de los packshots recortados (alto/ancho) — medidas el 15-09-2026.
export const RATIO = {
  s750: 1431 / 434, // squeeze 750 cocinar (naranja / tapa amarilla)
  s500: 1398 / 511, // squeeze 500 aderezar (lima / tapa lima)
  lCoc: 1396 / 593, // lata cocinar
  lAde: 1395 / 592, // lata aderezar
} as const;
