import React from "react";
import {Img, staticFile} from "remotion";
import {santagota as SG, ensureSantaGotaFonts} from "./santagota";

// ============================================================
// SANTA GOTA — las piezas de UI que se repiten en los 3 formatos de TV.
// Todas salen del feed medido el 11-09-2026; ninguna es nueva:
//   · Halo      → la aureola blanca que flota sobre la botella en el feed
//                 (Snoop en el refri, la chica del supermercado). Acá sobre la monja.
//   · Trazo     → el subrayado de plumón que marca la palabra clave
//                 («pasan cosas», «no al acelerador», «Jaque mate»). En naranja
//                 porque sobre lima el lima desaparece.
//   · Monja     → el recorte del REEL (t = 9,3 s), la monja real del rodaje.
//   · Titular   → Montserrat 800/900, mayúscula, interlínea apretada.
//   · LogoColor → el PNG oficial. Sólo sobre botella, hueso o blanco.
// ============================================================

const C = SG.colors;

/**
 * Aureola. Elipse fina, un poco ladeada, como en el feed. En el feed es blanca
 * sobre foto; en TV va NARANJA: flota sobre el set del programa (blanco en TVN)
 * y además es el mismo anillo que la O de GOTA en el logo.
 */
export const Halo: React.FC<{cx: number; cy: number; w?: number; h?: number; rot?: number; grosor?: number; color?: string}> = ({
  cx, cy, w = 120, h = 30, rot = -10, grosor = 6, color = C.naranja,
}) => (
  <svg style={{position: "absolute", left: cx - w, top: cy - h, overflow: "visible"}} width={w * 2} height={h * 2}>
    <ellipse cx={w} cy={h} rx={w / 2} ry={h / 2} fill="none" stroke={color} strokeWidth={grosor} transform={`rotate(${rot} ${w} ${h})`} />
  </svg>
);

/** Subrayado de plumón: dos pasadas rápidas, la segunda más corta y levemente subida. */
export const Trazo: React.FC<{x: number; y: number; w: number; grosor?: number; color?: string; z?: number}> = ({
  x, y, w, grosor = 12, color = C.naranja, z = 1,
}) => {
  const g = grosor;
  return (
    <svg style={{position: "absolute", left: x, top: y - g * 2, overflow: "visible", zIndex: z}} width={w} height={g * 4}>
      <path d={`M ${g} ${g * 2.4} Q ${w * 0.5} ${g * 1.6} ${w - g} ${g * 2.1}`} fill="none" stroke={color} strokeWidth={g} strokeLinecap="round" />
      <path d={`M ${w * 0.12} ${g * 3.2} Q ${w * 0.55} ${g * 2.5} ${w * 0.9} ${g * 2.9}`} fill="none" stroke={color} strokeWidth={g * 0.75} strokeLinecap="round" />
    </svg>
  );
};

/**
 * La monja del reel (t=8,7 s), recortada. El PNG es 1080×1920; el cuerpo sólido va
 * de la fila 641 (cornette) a la 1766 (hábito bajo la sartén) y la cabeza está en
 * x≈596. La sartén va de la fila ~1400 a la ~1500.
 * `s` escala, `tx`/`ty` trasladan: coordenada en lienzo = original·s + t.
 */
export const Monja: React.FC<{s: number; tx: number; ty: number; z?: number}> = ({s, tx, ty, z = 2}) => (
  <Img
    src={staticFile(SG.monja.plato)}
    style={{position: "absolute", left: tx, top: ty, width: 1080 * s, height: 1920 * s, zIndex: z}}
  />
);
export const MONJA = {cabezaTop: 641, cabezaCx: 596, sartenBase: 1520, pieSolido: 1766} as const;

export const Titular: React.FC<{
  size: number; weight?: number; color?: string; lh?: number; track?: number; style?: React.CSSProperties; children: React.ReactNode;
}> = ({size, weight = 800, color = C.botella, lh = 0.98, track = -0.02, style, children}) => (
  <div style={{
    fontFamily: SG.fonts.display, fontWeight: weight, fontSize: size, lineHeight: lh,
    letterSpacing: `${track}em`, color, textTransform: "uppercase", whiteSpace: "nowrap", ...style,
  }}>
    {children}
  </div>
);

export const LogoColor: React.FC<{x: number; y: number; w: number; z?: number}> = ({x, y, w, z = 3}) => (
  <Img src={staticFile(SG.logo)} style={{position: "absolute", left: x, top: y, width: w, height: w / SG.logoRatio, zIndex: z}} />
);

export const LogoPlano: React.FC<{x: number; y: number; w: number; tono?: "botella" | "blanco"; z?: number}> = ({x, y, w, tono = "botella", z = 3}) => (
  <Img src={staticFile(`assets/santagota/logo-plano-${tono}.png`)} style={{position: "absolute", left: x, top: y, width: w, height: w / SG.logoRatio, zIndex: z}} />
);

export const Url: React.FC<{x: number; y: number; size: number; color?: string; align?: "left" | "right" | "center"; z?: number}> = ({
  x, y, size, color = C.lima, align = "left", z = 3,
}) => (
  <div style={{
    position: "absolute", top: y, zIndex: z, fontFamily: SG.fonts.display, fontWeight: 800, fontSize: size,
    letterSpacing: "0.01em", color, whiteSpace: "nowrap",
    ...(align === "right" ? {right: x} : align === "center" ? {left: 0, right: 0, textAlign: "center"} : {left: x}),
  }}>
    {SG.url}
  </div>
);

export const useSantaGota = () => {
  ensureSantaGotaFonts();
  return C;
};
