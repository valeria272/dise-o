import React from "react";
import {Img, staticFile} from "remotion";
import {selfie} from "./selfie";

// ============================================================
// SELFIE — componentes de sistema gráfico reutilizables (piezas feed 2250 px)
// Basados en las piezas reales de la diseñadora (raw/selfie/grilla-agosto2026-designs)
// ============================================================

export const FUCSIA = selfie.colors.fucsia; // #FF007C
export const PILL = "#FF66B0";
export const BODY = selfie.fonts.body; // Open Sans

// Asterisco del logo (6 brazos, puntas redondas) — patrón decorativo de marca
export const Asterisco: React.FC<{
  x: number;
  y: number;
  size: number;
  rot?: number;
  color?: string;
  opacity?: number;
}> = ({x, y, size, rot = 0, color = PILL, opacity = 0.55}) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 100 100"
    style={{position: "absolute", left: x, top: y, transform: `rotate(${rot}deg)`, opacity}}
  >
    {[0, 60, 120].map((a) => (
      <line
        key={a}
        x1={50 - 42 * Math.cos((a * Math.PI) / 180)}
        y1={50 - 42 * Math.sin((a * Math.PI) / 180)}
        x2={50 + 42 * Math.cos((a * Math.PI) / 180)}
        y2={50 + 42 * Math.sin((a * Math.PI) / 180)}
        stroke={color}
        strokeWidth="16"
        strokeLinecap="round"
      />
    ))}
  </svg>
);

export const Asteriscos: React.FC = () => (
  <>
    <Asterisco x={-90} y={180} size={330} rot={15} />
    <Asterisco x={1950} y={520} size={260} rot={-20} />
    <Asterisco x={180} y={2380} size={300} rot={30} />
    <Asterisco x={1850} y={2500} size={240} rot={10} />
    <Asterisco x={1050} y={-100} size={220} rot={-15} />
  </>
);

// destello dorado de 4 puntas (piezas editoriales de la marca)
export const Sparkle: React.FC<{x: number; y: number; size: number}> = ({x, y, size}) => (
  <svg width={size} height={size} viewBox="0 0 100 100" style={{position: "absolute", left: x, top: y}}>
    <path d="M50 0 L60 40 L100 50 L60 60 L50 100 L40 60 L0 50 L40 40 Z" fill={selfie.colors.sparkle} />
  </svg>
);

export const LogoVertical: React.FC<{dark?: boolean}> = ({dark}) => (
  <Img
    src={staticFile(`assets/selfie/logo-vertical-${dark ? "negro" : "blanco"}.png`)}
    style={{position: "absolute", right: 70, top: 170, height: 640}}
  />
);

// caja blanca redondeada con contenido fucsia — el bloque central de la marca
export const CajaBlanca: React.FC<{top: number; width: number; children: React.ReactNode}> = ({
  top,
  width,
  children,
}) => (
  <div style={{position: "absolute", top, left: (2250 - width) / 2, width, textAlign: "center"}}>
    <div
      style={{
        display: "inline-block",
        background: "#fff",
        borderRadius: 56,
        padding: "50px 80px 58px",
        boxShadow: "0 30px 60px rgba(0,0,0,0.18)",
      }}
    >
      {children}
    </div>
  </div>
);

export const PillTag: React.FC<{top: number; children: React.ReactNode; fontSize?: number}> = ({
  top,
  children,
  fontSize = 72,
}) => (
  <div style={{position: "absolute", top, left: 0, width: 2250, textAlign: "center"}}>
    <div
      style={{
        display: "inline-block",
        background: PILL,
        borderRadius: 60,
        padding: "22px 70px 30px",
        color: "#fff",
        fontFamily: BODY,
        fontWeight: 800,
        fontSize,
      }}
    >
      {children}
    </div>
  </div>
);
