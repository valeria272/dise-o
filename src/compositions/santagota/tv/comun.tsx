// ============================================================================
// SANTA GOTA · TV — piezas comunes de PRODUCCIÓN (V3, 11-09-2026)
// ----------------------------------------------------------------------------
// Dirección aprobada: fotografía primero, la gráfica acompaña. Nada de campo
// lima plano. Titular blanco + REVOLUCIONAR en lima, naranja sólo como gesto
// (halo, plumón, la pastilla del CTA). Logo: SOLO el PNG oficial a color.
// Producto: SOLO real, desde el reel (el chorro del squeeze). Monja: la del reel.
//
// V3 agrega lo que pide la edición publicitaria:
//   · MonjaViva   → la monja RECORTADA EN MOVIMIENTO (11 cuadros del reel con alfa,
//                   8,667–8,792 s quieta con la sartén · 8,917–9,167 s lanza la pasta)
//   · Revela      → tipografía cinética: máscara desde abajo / desde la izquierda /
//                   golpe de escala con overshoot leve
//   · Bloque      → losa petróleo con bordes en bisel que se barre (entra/sale)
//   · Latigo      → el trazo lima+naranja que cruza el cuadro y motiva un cambio
//   · Sfx         → un efecto de sonido en un segundo dado
// ============================================================================
import React from "react";
import {Audio, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {santagota as SG, ensureSantaGotaFonts} from "../../../brand/santagota";
import {Halo, Trazo} from "../../../brand/santagotaUI";

export const C = SG.colors;
export const PETROLEO = "#0A2A34";       // azul petróleo de la dirección aprobada (losas y end frame)
export const PETROLEO_OSCURO = "#061C24";
export const FPS = 29.97;
export const REEL = "assets/santagota/reel.mp4"; // 1080×1920 · 24 fps · 12,46 s
export const LOOP = "assets/santagota/loop.mp4"; // 1080×1920 · 24 fps · 13,29 s (mismo rodaje + emplatado del ají al final)

export const seg = (s: number) => Math.round(s * FPS);

/** Resorte estándar: entra con decisión, sin rebote blando. */
export const entra = (frame: number, fps: number, delay = 0, durationInFrames = 18) =>
  spring({frame: frame - delay, fps, config: {damping: 16, stiffness: 140, mass: 0.8}, durationInFrames});

/** Golpe: llega rápido, se pasa un poco y se detiene seco (overshoot leve). */
export const golpe = (frame: number, fps: number, delay = 0, durationInFrames = 16) =>
  spring({frame: frame - delay, fps, config: {damping: 11, stiffness: 190, mass: 0.7}, durationInFrames});

/** Fundido lineal entre dos frames. */
export const fade = (frame: number, a: number, b: number, from = 0, to = 1) =>
  interpolate(frame, [a, b], [from, to], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});

/** Ease-in (acelera): para salidas que se van «cayendo». */
export const cae = (frame: number, a: number, b: number) => {
  const t = fade(frame, a, b);
  return t * t * (1.2 - 0.2 * t);
};

export const useFrameFps = () => {
  ensureSantaGotaFonts(); // Montserrat local vía @font-face (idempotente)
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  return {frame, fps};
};

// ── Video ───────────────────────────────────────────────────────────────────

/**
 * El reel vertical RECORTADO a un cuadro horizontal (nunca estirado): se escala
 * a `w` de ancho y se centra verticalmente en la fila `fila` del original
 * (0–1920). `desde` es el segundo del reel. `zoom`/`dx`/`dy` mueven el cuadro
 * (empujes y micro-desplazamientos que dan energía a los cortes).
 */
export const ReelRecorte: React.FC<{
  desde: number; w: number; h: number; fila: number; rate?: number; src?: string; muted?: boolean;
  zoom?: number; dx?: number; dy?: number; origenY?: number; style?: React.CSSProperties;
}> = ({desde, w, h, fila, rate = 1, src = REEL, muted = true, zoom = 1, dx = 0, dy = 0, origenY = 0.5, style}) => {
  const s = w / 1080;
  return (
    <div style={{position: "absolute", left: 0, top: 0, width: w, height: h, overflow: "hidden", ...style}}>
      <div style={{position: "absolute", inset: 0, transform: `translate(${dx}px, ${dy}px) scale(${zoom})`, transformOrigin: `50% ${origenY * 100}%`}}>
        {/* ⚠ startFrom se cuenta en fotogramas de la COMPOSICIÓN (29,97), no del reel (24). */}
        <OffthreadVideo
          src={staticFile(src)}
          startFrom={Math.round(desde * FPS)}
          playbackRate={rate}
          muted={muted}
          style={{position: "absolute", left: 0, top: h / 2 - fila * s, width: w, height: 1920 * s}}
        />
      </div>
    </div>
  );
};

// ── La monja ────────────────────────────────────────────────────────────────

/** Ping-pong entre n cuadros, `paso` fotogramas por cuadro (micro-vida de la pose quieta). */
export const pingpong = (frame: number, paso: number, n = 4) => {
  const ciclo = 2 * n - 2;
  const i = Math.floor(Math.max(0, frame) / paso) % ciclo;
  return i < n ? i : ciclo - i;
};

/**
 * La monja del reel recortada, EN MOVIMIENTO. Cuadros 0–3: quieta con la sartén
 * (8,667–8,792 s). Cuadros 4–10: lanza la pasta (8,917–9,167 s). Mismo sistema
 * de coordenadas que `Monja` (1080×1920; cabeza en x≈596, cornette en la fila 641).
 */
export const MonjaViva: React.FC<{cuadro: number; s: number; tx: number; ty: number; z?: number; style?: React.CSSProperties}> = ({cuadro, s, tx, ty, z = 2, style}) => {
  const k = Math.max(0, Math.min(10, Math.round(cuadro)));
  return (
    <Img
      src={staticFile(`assets/santagota/monja-seq/m${String(k).padStart(2, "0")}.png`)}
      style={{position: "absolute", left: tx, top: ty, width: 1080 * s, height: 1920 * s, zIndex: z, ...style}}
    />
  );
};

/** Cuadro de la secuencia: quieta (ping-pong 0–3) hasta `lanzaEn`, después el lanzamiento a `rate`× y congela en el 10. */
export const cuadroMonja = (frame: number, lanzaEn: number, rate = 0.5, pasoQuieta = 7, hasta = 10) => {
  if (frame < lanzaEn) return pingpong(frame, pasoQuieta);
  const porCuadro = (FPS / 24) / rate; // fotogramas de composición por cuadro del reel
  return Math.min(hasta, 4 + Math.floor((frame - lanzaEn) / porCuadro));
};

// ── Tipografía ──────────────────────────────────────────────────────────────

/** Titular de TV: Montserrat, mayúscula, blanco; `lima` para la palabra protagonista. */
export const Linea: React.FC<{size: number; weight?: number; lima?: boolean; op?: number; dy?: number; sombra?: boolean; style?: React.CSSProperties; children: React.ReactNode}> = ({
  size, weight = 800, lima = false, op = 1, dy = 0, sombra = true, style, children,
}) => (
  <div style={{
    fontFamily: SG.fonts.display, fontWeight: weight, fontSize: size, lineHeight: 1, letterSpacing: "-0.02em",
    textTransform: "uppercase", whiteSpace: "nowrap", color: lima ? C.lima : "#FFFFFF",
    textShadow: sombra ? "0 2px 18px rgba(0,0,0,0.45)" : "none", opacity: op, transform: `translateY(${dy}px)`, ...style,
  }}>
    {children}
  </div>
);

/**
 * Reveal cinético. `p` 0→1.
 *   abajo: la línea sube desde una máscara (entra rápido, se detiene)
 *   izq:   la línea entra desde la izquierda tras una máscara
 *   golpe: escala 1,35→1 con opacidad rápida (la palabra HERO)
 */
export const Revela: React.FC<{p: number; modo?: "abajo" | "izq" | "golpe"; origen?: string; style?: React.CSSProperties; children: React.ReactNode}> = ({
  p, modo = "abajo", origen = "0% 60%", style, children,
}) => {
  const t = 1 - Math.max(0, Math.min(1.2, p));
  const inner =
    modo === "abajo" ? `translateY(${t * 112}%)` :
    modo === "izq" ? `translateX(${-t * 105}%)` :
    `scale(${1 + t * 0.35})`;
  return (
    <div style={{overflow: modo === "golpe" ? "visible" : "hidden", opacity: modo === "golpe" ? Math.min(1, p * 4) : 1, ...style}}>
      <div style={{transform: inner, transformOrigin: origen, paddingTop: "0.14em", marginTop: "-0.14em"}}>{children}</div>
    </div>
  );
};

/** El plumón naranja que se dibuja de izquierda a derecha (progreso 0–1). */
export const Plumon: React.FC<{x: number; y: number; w: number; grosor?: number; p: number; z?: number; color?: string}> = ({x, y, w, grosor = 12, p, z = 5, color}) => (
  <div style={{position: "absolute", left: x, top: y - grosor * 2, width: Math.max(0, w * Math.min(1, p)), height: grosor * 4, overflow: "hidden", zIndex: z}}>
    <Trazo x={0} y={grosor * 2} w={w} grosor={grosor} z={1} color={color} />
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

// ── Gráfica ─────────────────────────────────────────────────────────────────

/**
 * Losa petróleo con bordes en bisel. `p` la barre desde la izquierda (0→1);
 * `q` la barre hacia afuera desde la izquierda (0→1) para salir.
 */
export const Bloque: React.FC<{x: number; y: number; w: number; h: number; p: number; q?: number; color?: string; bisel?: number; z?: number; op?: number; children?: React.ReactNode}> = ({
  x, y, w, h, p, q = 0, color = PETROLEO, bisel = 14, z = 3, op = 1, children,
}) => (
  <div style={{position: "absolute", left: x, top: y, width: w, height: h, zIndex: z, opacity: op,
    clipPath: `inset(0 ${(1 - Math.min(1, p)) * 100}% 0 ${Math.min(1, q) * 100}%)`}}>
    <div style={{position: "absolute", inset: 0, background: color,
      clipPath: `polygon(${bisel}px 0, 100% 0, calc(100% - ${bisel}px) 100%, 0 100%)`,
      boxShadow: "0 10px 30px rgba(0,0,0,0.35)"}} />
    {children}
  </div>
);

/** El trazo Santa Gota que cruza el cuadro (lima ancho + naranja fino detrás). `p` 0→1. */
export const Latigo: React.FC<{p: number; W: number; H: number; z?: number}> = ({p, W, H, z = 20}) => {
  const e = interpolate(p, [0, 1], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const ease = e < 0.5 ? 2 * e * e : 1 - Math.pow(-2 * e + 2, 2) / 2;
  const x = interpolate(ease, [0, 1], [-2.3 * W, 1.7 * W]);
  return (
    <div style={{position: "absolute", inset: 0, zIndex: z, pointerEvents: "none", overflow: "hidden", opacity: p <= 0 || p >= 1 ? 0 : 1}}>
      <div style={{position: "absolute", left: x - W * 0.22, top: -H * 0.8, width: W * 0.16, height: H * 2.6, background: C.naranja, transform: "rotate(-14deg)"}} />
      <div style={{position: "absolute", left: x, top: -H * 0.8, width: W * 1.9, height: H * 2.6, background: C.lima, transform: "rotate(-14deg)"}} />
    </div>
  );
};

/** Logo oficial a color — el único archivo autorizado. */
export const Logo: React.FC<{x: number; y: number; w: number; op?: number; sc?: number; z?: number; sombra?: boolean}> = ({x, y, w, op = 1, sc = 1, z = 7, sombra = true}) => (
  <Img src={staticFile(SG.logo)} style={{position: "absolute", left: x, top: y, width: w, height: w / SG.logoRatio, opacity: op, transform: `scale(${sc})`, transformOrigin: "50% 50%", zIndex: z,
    filter: sombra ? "drop-shadow(0 6px 22px rgba(0,0,0,0.45))" : "none"}} />
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

// ── Sonido ──────────────────────────────────────────────────────────────────

export const SFX = {
  whoosh: "assets/santagota/sfx/whoosh.mp3",
  whoosh2: "assets/santagota/sfx/whoosh2.mp3",
  sizzle: "assets/santagota/sfx/sizzle.mp3",
  fire: "assets/santagota/sfx/fire.mp3",
  impact: "assets/santagota/sfx/impact.mp3",
  pan: "assets/santagota/sfx/pan.mp3",
  sting: "assets/santagota/sfx/sting.mp3",
  marker: "assets/santagota/sfx/marker.mp3",
} as const;

/** Un efecto de sonido en el segundo `at`. */
export const Sfx: React.FC<{src: string; at: number; vol?: number}> = ({src, at, vol = 1}) => (
  <Sequence from={seg(at)} layout="none">
    <Audio src={staticFile(src)} volume={vol} />
  </Sequence>
);
