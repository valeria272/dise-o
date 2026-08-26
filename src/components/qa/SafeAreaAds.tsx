import React from "react";
import {AbsoluteFill, useVideoConfig} from "remotion";

/**
 * Overlay de QA con las zonas seguras de Meta Ads (Instagram + Facebook).
 * NO va en la entrega: es solo para revisar antes de exportar.
 * Cifras: memoria `paid-media-zonas-seguras` (regla global de la agencia).
 */

export type SafeFormat = "story" | "feed45" | "feed11";

// Todo en px sobre el lienzo real de la composición
export const SAFE_ZONES = {
  // 1080 × 1920 — Reels / Stories
  story: {
    top: 250, // nombre de cuenta + barra de progreso
    bottom: 340, // CTA, "Enviar mensaje", barra de UI
    left: 60,
    right: 115, // columna de iconos (like / comentar / compartir)
  },
  // 1080 × 1350 — feed 4:5 (el formato dominante de estas dos marcas)
  feed45: {
    top: 60,
    bottom: 190, // ~14 %: ahí cae el copy del anuncio y el botón
    left: 60,
    right: 60,
  },
  // 1080 × 1080 — feed cuadrado
  feed11: {
    top: 60,
    bottom: 150,
    left: 60,
    right: 60,
  },
} as const;

export const safeZoneFor = (format: SafeFormat) => SAFE_ZONES[format];

export const SafeAreaAds: React.FC<{
  format: SafeFormat;
  show?: boolean;
  label?: boolean;
}> = ({format, show = true, label = true}) => {
  const {width, height} = useVideoConfig();
  if (!show) return null;
  const z = SAFE_ZONES[format];

  const band: React.CSSProperties = {
    position: "absolute",
    background: "rgba(255,0,110,0.16)",
    borderColor: "rgba(255,0,110,0.85)",
    borderStyle: "dashed",
    borderWidth: 0,
  };

  return (
    <AbsoluteFill style={{pointerEvents: "none"}}>
      {/* Bandas prohibidas */}
      <div style={{...band, top: 0, left: 0, right: 0, height: z.top, borderBottomWidth: 3}} />
      <div style={{...band, bottom: 0, left: 0, right: 0, height: z.bottom, borderTopWidth: 3}} />
      <div style={{...band, top: z.top, bottom: z.bottom, left: 0, width: z.left, borderRightWidth: 3}} />
      <div style={{...band, top: z.top, bottom: z.bottom, right: 0, width: z.right, borderLeftWidth: 3}} />

      {/* Caja segura */}
      <div
        style={{
          position: "absolute",
          top: z.top,
          left: z.left,
          width: width - z.left - z.right,
          height: height - z.top - z.bottom,
          border: "3px solid rgba(0,225,150,0.9)",
        }}
      />

      {label ? (
        <div
          style={{
            position: "absolute",
            top: z.top + 12,
            left: z.left + 12,
            font: "600 22px/1.2 'Montserrat', sans-serif",
            color: "rgba(0,225,150,0.95)",
            background: "rgba(0,0,0,0.55)",
            padding: "6px 12px",
            borderRadius: 6,
            letterSpacing: 0.5,
          }}
        >
          ZONA SEGURA {format} · {width}×{height} · arriba {z.top} · abajo {z.bottom} · der {z.right}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
