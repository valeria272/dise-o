// ============================================================================
// SANTA GOTA · TV — piezas comunes de PRODUCCIÓN (Fase 2, 11-09-2026)
// ----------------------------------------------------------------------------
// Dirección aprobada: fotografía primero, la gráfica acompaña. Nada de campo
// lima plano. Titular blanco + REVOLUCIONAR en lima, naranja sólo como gesto
// (halo, plumón, la pastilla del CTA). Logo: SOLO el PNG oficial a color.
// Producto: SOLO real, desde el reel (el chorro del squeeze). Monja: la del reel.
// ============================================================================
import React from "react";
import {Img, OffthreadVideo, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {santagota as SG} from "../../../brand/santagota";
import {Halo, Trazo} from "../../../brand/santagotaUI";

export const C = SG.colors;
export const FPS = 29.97;
export const REEL = "assets/santagota/reel.mp4"; // 1080×1920 · 24 fps · 12,46 s
export const LOOP = "assets/santagota/loop.mp4"; // 1080×1920 · 24 fps · 13,29 s (mismo rodaje, termina con logo a color)

export const seg = (s: number) => Math.round(s * FPS);

/** Resorte estándar de la campaña: entra con decisión, sin rebote blando. */
export const entra = (frame: number, fps: number, delay = 0, durationInFrames = 18) =>
  spring({frame: frame - delay, fps, config: {damping: 16, stiffness: 140, mass: 0.8}, durationInFrames});

/** Fundido lineal entre dos frames. */
export const fade = (frame: number, a: number, b: number, from = 0, to = 1) =>
  interpolate(frame, [a, b], [from, to], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});

/**
 * El reel vertical recortado a un cuadro horizontal SIN estirar: se escala a
 * `w` de ancho y se centra verticalmente en la fila `fila` del original
 * (0–1920). `desde` es el segundo del reel donde arranca.
 */
export const ReelRecorte: React.FC<{
  desde: number; w: number; h: number; fila: number; rate?: number; src?: string; muted?: boolean; style?: React.CSSProperties;
}> = ({desde, w, h, fila, rate = 1, src = REEL, muted = true, style}) => {
  const s = w / 1080;
  return (
    <div style={{position: "absolute", left: 0, top: 0, width: w, height: h, overflow: "hidden", ...style}}>
      {/* ⚠ startFrom se cuenta en fotogramas de la COMPOSICIÓN (29,97), no del reel (24). */}
      <OffthreadVideo
        src={staticFile(src)}
        startFrom={Math.round(desde * FPS)}
        playbackRate={rate}
        muted={muted}
        style={{position: "absolute", left: 0, top: h / 2 - fila * s, width: w, height: 1920 * s}}
      />
    </div>
  );
};

/**
 * Columna 9:16 a altura completa sobre una «placa» del mismo video, desenfocada
 * y oscurecida con tinte petróleo: la forma de llevar el vertical al 16:9 sin
 * estirarlo. `x` es la posición de la columna.
 */
export const ReelColumna: React.FC<{desde: number; x: number; rate?: number; W: number; H: number; src?: string}> = ({
  desde, x, rate = 1, W, H, src = REEL,
}) => {
  const colW = Math.round(H * 9 / 16);
  const s = colW / 1080;
  const plateS = W / 1080;
  return (
    <>
      <div style={{position: "absolute", inset: 0, overflow: "hidden", background: "#07242E"}}>
        <OffthreadVideo
          src={staticFile(src)} startFrom={Math.round(desde * FPS)} playbackRate={rate} muted
          style={{position: "absolute", left: 0, top: H / 2 - 960 * plateS, width: W, height: 1920 * plateS,
            filter: "blur(38px) brightness(0.42) saturate(1.15)", transform: "scale(1.1)"}}
        />
        <div style={{position: "absolute", inset: 0, background: "linear-gradient(180deg, rgba(7,36,46,0.35), rgba(7,36,46,0.15) 50%, rgba(2,12,16,0.6))"}} />
      </div>
      <div style={{position: "absolute", left: x, top: 0, width: colW, height: H, overflow: "hidden", boxShadow: "0 0 80px rgba(0,0,0,0.55)"}}>
        <OffthreadVideo
          src={staticFile(src)} startFrom={Math.round(desde * FPS)} playbackRate={rate} muted
          style={{position: "absolute", left: 0, top: 0, width: colW, height: 1920 * s}}
        />
      </div>
    </>
  );
};

/** Titular de TV: Montserrat, mayúscula, blanco; `lima` para la palabra protagonista. */
export const Linea: React.FC<{size: number; weight?: number; lima?: boolean; op?: number; dy?: number; style?: React.CSSProperties; children: React.ReactNode}> = ({
  size, weight = 800, lima = false, op = 1, dy = 0, style, children,
}) => (
  <div style={{
    fontFamily: SG.fonts.display, fontWeight: weight, fontSize: size, lineHeight: 1, letterSpacing: "-0.02em",
    textTransform: "uppercase", whiteSpace: "nowrap", color: lima ? C.lima : "#FFFFFF",
    textShadow: "0 2px 18px rgba(0,0,0,0.45)", opacity: op, transform: `translateY(${dy}px)`, ...style,
  }}>
    {children}
  </div>
);

/** El plumón naranja que se dibuja de izquierda a derecha (progreso 0–1). */
export const Plumon: React.FC<{x: number; y: number; w: number; grosor?: number; p: number; z?: number}> = ({x, y, w, grosor = 12, p, z = 5}) => (
  <div style={{position: "absolute", left: x, top: y - grosor * 2, width: Math.max(0, w * p), height: grosor * 4, overflow: "hidden", zIndex: z}}>
    <Trazo x={0} y={grosor * 2} w={w} grosor={grosor} z={1} />
  </div>
);

/** La aureola que se dibuja (progreso 0–1) con un rebote chico. */
export const HaloAnim: React.FC<{cx: number; cy: number; w: number; h: number; p: number; grosor?: number; z?: number}> = ({cx, cy, w, h, p, grosor = 7, z = 6}) => {
  const sc = interpolate(p, [0, 0.7, 1], [0, 1.15, 1], {extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", left: 0, top: 0, zIndex: z, transform: `translate(${cx}px, ${cy}px) scale(${sc})`, transformOrigin: "0 0", opacity: p > 0 ? 1 : 0}}>
      <Halo cx={0} cy={0} w={w} h={h} grosor={grosor} />
    </div>
  );
};

/** Logo oficial a color — el único archivo autorizado. */
export const Logo: React.FC<{x: number; y: number; w: number; op?: number; sc?: number; z?: number}> = ({x, y, w, op = 1, sc = 1, z = 7}) => (
  <Img src={staticFile(SG.logo)} style={{position: "absolute", left: x, top: y, width: w, height: w / SG.logoRatio, opacity: op, transform: `scale(${sc})`, transformOrigin: "50% 50%", zIndex: z,
    filter: "drop-shadow(0 6px 22px rgba(0,0,0,0.45))"}} />
);

/** SANTAGOTA.CL en la pastilla naranja del KV aprobado, un poco ladeada. */
export const Cta: React.FC<{x: number; y: number; size: number; op?: number; sc?: number; rot?: number; z?: number}> = ({x, y, size, op = 1, sc = 1, rot = -2.5, z = 7}) => (
  <div style={{
    position: "absolute", left: x, top: y, zIndex: z, opacity: op, transform: `rotate(${rot}deg) scale(${sc})`, transformOrigin: "50% 50%",
    background: C.naranja, color: "#FFFFFF", fontFamily: SG.fonts.display, fontWeight: 800, fontSize: size, letterSpacing: "0.01em",
    padding: `${size * 0.28}px ${size * 0.5}px`, whiteSpace: "nowrap", boxShadow: "0 8px 26px rgba(0,0,0,0.35)",
  }}>
    {SG.url}
  </div>
);

export const useFrameFps = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  return {frame, fps};
};
