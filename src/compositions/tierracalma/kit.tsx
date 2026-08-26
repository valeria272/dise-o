import React from "react";
import {AbsoluteFill, Img, interpolate, OffthreadVideo, Sequence, staticFile, useCurrentFrame} from "remotion";
import {tierracalma as TC, ensureTierraCalmaFonts} from "../../brand/tierracalma";

ensureTierraCalmaFonts();

export {TC};

export const SERIF = TC.fonts.display;
export const SANS = TC.fonts.body;

// ---------------------------------------------------------------------------
// Grano de película — mismo patrón que TierraCalmaReel (SVG feTurbulence).
export const Grain: React.FC<{id: string; opacity?: number}> = ({id, opacity = 0.04}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{opacity, mixBlendMode: "overlay", pointerEvents: "none"}}>
      <svg width="100%" height="100%">
        <filter id={id}>
          <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves={2} seed={frame % 55} stitchTiles="stitch" />
          <feColorMatrix type="saturate" values="0" />
        </filter>
        <rect width="100%" height="100%" filter={`url(#${id})`} />
      </svg>
    </AbsoluteFill>
  );
};

// Grade sereno: scrims arriba/abajo para legibilidad + viñeta suave.
// Menos cálido que el reel de bienvenida — acá manda la claridad del dato.
// `calido` sube la temperatura de una escena concreta. Se usa cuando un plano de
// dron convive en el mismo reel con imagen IA de golden hour: sin esto el aéreo
// se ve gris al lado de la escena generada y el reel parece de dos marcas.
export const Grade: React.FC<{strength?: number; calido?: number}> = ({strength = 1, calido = 1}) => (
  <>
    {/* calidez: el rodaje fue una mañana nublada y el proxy viene plano */}
    <AbsoluteFill style={{background: `linear-gradient(180deg, rgba(255,196,128,${0.1 * calido}) 0%, rgba(255,168,96,${0.06 * calido}) 55%, rgba(20,40,60,0.10) 100%)`, mixBlendMode: "soft-light", pointerEvents: "none"}} />
    {calido > 1 ? (
      <AbsoluteFill style={{background: `rgba(255,172,92,${0.06 * (calido - 1)})`, mixBlendMode: "overlay", pointerEvents: "none"}} />
    ) : null}
    <AbsoluteFill
      style={{
        background: `linear-gradient(180deg, rgba(8,16,22,${0.44 * strength}) 0%, rgba(8,16,22,${0.12 * strength}) 24%, rgba(6,12,18,${0.34 * strength}) 52%, rgba(6,12,18,${0.74 * strength}) 100%)`,
        pointerEvents: "none",
      }}
    />
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse 92% 72% at 50% 44%, transparent 48%, rgba(0,0,0,${0.34 * strength}) 100%)`,
        pointerEvents: "none",
      }}
    />
    {/* velo parejo — sin él ningún degradado alcanza sobre cielo quemado */}
    <AbsoluteFill style={{background: `rgba(8,14,18,${0.06 * strength})`, pointerEvents: "none"}} />
  </>
);

// Clip de paisaje con push-in continuo. `dur` en frames de ESTA secuencia.
export const Clip: React.FC<{
  src: string;
  dur: number;
  zoom?: [number, number];
  pan?: [number, number];
}> = ({src, dur, zoom = [1.05, 1.14], pan = [0, 0]}) => {
  const frame = useCurrentFrame();
  const s = interpolate(frame, [0, dur], zoom, {extrapolateRight: "clamp"});
  const x = interpolate(frame, [0, dur], [0, pan[0]], {extrapolateRight: "clamp"});
  const y = interpolate(frame, [0, dur], [0, pan[1]], {extrapolateRight: "clamp"});
  // Micro blur-in en el corte: disimula el primer frame decodificado.
  const blur = interpolate(frame, [0, 8], [10, 0], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      <OffthreadVideo
        src={staticFile(src)}
        muted
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: `scale(${s}) translate(${x}px, ${y}px)`,
          filter: `blur(${blur}px) saturate(1.14) contrast(1.07) brightness(1.02)`,
        }}
      />
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// Revelado con máscara. La caja lleva padding generoso + márgenes negativos
// para que NUNCA se corten los bordes de la tipografía (feedback de Constanza).
const PAD = 40;

export const Reveal: React.FC<{
  delay?: number;
  exitAt?: number;
  children: React.ReactNode;
  from?: number;
}> = ({delay = 0, exitAt, children, from = 44}) => {
  const frame = useCurrentFrame();
  const f = frame - delay;
  const inP = interpolate(f, [0, 20], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const outP = exitAt === undefined ? 0 : interpolate(frame, [exitAt, exitAt + 12], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const y = interpolate(inP, [0, 1], [from, 0]) + interpolate(outP, [0, 1], [0, -22]);
  const opacity = Math.min(inP, 1 - outP);
  const blur = interpolate(inP, [0, 1], [12, 0]);
  return (
    <div style={{overflow: "hidden", padding: PAD, margin: -PAD}}>
      <div style={{transform: `translateY(${y}px)`, opacity, filter: `blur(${blur}px)`, willChange: "transform"}}>{children}</div>
    </div>
  );
};

// Titular editorial en serif de marca. Cifras y titulares SIEMPRE en serif.
export const Headline: React.FC<{
  size?: number;
  weight?: number;
  color?: string;
  italic?: boolean;
  lh?: number;
  tracking?: string;
  align?: "left" | "center";
  children: React.ReactNode;
}> = ({size = 92, weight = 400, color = "#FFFFFF", italic, lh = 1.04, tracking = "-0.02em", align = "left", children}) => (
  <div
    style={{
      fontFamily: SERIF,
      fontSize: size,
      fontWeight: weight,
      fontStyle: italic ? "italic" : "normal",
      color,
      lineHeight: lh,
      letterSpacing: tracking,
      textAlign: align,
      textShadow: color === "#FFFFFF" ? "0 3px 44px rgba(0,0,0,0.55), 0 1px 3px rgba(0,0,0,0.35)" : "none",
    }}
  >
    {children}
  </div>
);

// Kicker / etiqueta: sans en mayúsculas con tracking amplio, como el "PADRE
// HURTADO" del logotipo. Nunca compite con el titular.
export const Kicker: React.FC<{
  size?: number;
  color?: string;
  align?: "left" | "center";
  children: React.ReactNode;
}> = ({size = 24, color = TC.colors.sand, align = "left", children}) => (
  <div
    style={{
      fontFamily: SANS,
      fontSize: size,
      fontWeight: 600,
      color,
      letterSpacing: "0.26em",
      textTransform: "uppercase",
      textAlign: align,
      // Sombra en capas: la etiqueta en arena se comía sobre neblina y nieve.
      textShadow: "0 1px 3px rgba(0,0,0,0.6), 0 2px 14px rgba(0,0,0,0.5), 0 0 34px rgba(0,0,0,0.4)",
    }}
  >
    {children}
  </div>
);

// Bajada / dato en sans. Legible, discreta, nunca del tamaño del titular.
export const Body: React.FC<{
  size?: number;
  color?: string;
  weight?: number;
  align?: "left" | "center";
  lh?: number;
  children: React.ReactNode;
}> = ({size = 34, color = "rgba(255,255,255,0.88)", weight = 400, align = "left", lh = 1.35, children}) => (
  <div
    style={{
      fontFamily: SANS,
      fontSize: size,
      fontWeight: weight,
      color,
      lineHeight: lh,
      textAlign: align,
      letterSpacing: "0.005em",
      textShadow: "0 1px 3px rgba(0,0,0,0.55), 0 2px 20px rgba(0,0,0,0.5), 0 0 36px rgba(0,0,0,0.35)",
    }}
  >
    {children}
  </div>
);

// Filete fino color arena — separador de marca.
export const Rule: React.FC<{width?: number; color?: string; align?: "left" | "center"}> = ({
  width = 96,
  color = TC.colors.sand,
  align = "left",
}) => (
  <div style={{display: "flex", justifyContent: align === "center" ? "center" : "flex-start"}}>
    <div style={{width, height: 1.5, background: color, opacity: 0.9}} />
  </div>
);

// Zona segura de reel: 14% libre arriba y abajo (regla del brief de diseño).
export const SAFE_TOP = 270;
export const SAFE_BOTTOM = 270;
export const MARGIN = 84;

export const SafeBlock: React.FC<{top: number; children: React.ReactNode; align?: "left" | "center"}> = ({
  top,
  children,
  align = "left",
}) => (
  <div
    style={{
      position: "absolute",
      left: MARGIN,
      right: MARGIN,
      top,
      textAlign: align,
      display: "flex",
      flexDirection: "column",
      alignItems: align === "center" ? "center" : "flex-start",
      gap: 22,
    }}
  >
    {children}
  </div>
);

// Franja oscura a media altura: el Grade cubre arriba y abajo, pero el texto
// que cae al centro queda sin respaldo sobre cielos claros y nieve.
export const BandScrim: React.FC<{from?: number; to?: number; strength?: number}> = ({
  from = 26,
  to = 82,
  strength = 0.52,
}) => (
  <AbsoluteFill
    style={{
      background: `linear-gradient(180deg, transparent ${from}%, rgba(6,12,18,${strength}) ${from + 16}%, rgba(6,12,18,${strength}) ${to - 16}%, transparent ${to}%)`,
      pointerEvents: "none",
    }}
  />
);

// Cierre oficial: el motion del logo del cliente, sin re-animar.
export const LogoOutro: React.FC<{dur: number}> = ({dur}) => {
  const frame = useCurrentFrame();
  const fade = interpolate(frame, [0, 12], [0, 1], {extrapolateRight: "clamp"});
  const out = interpolate(frame, [dur - 14, dur], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{background: "#FFFFFF", opacity: Math.min(fade, out)}}>
      <OffthreadVideo
        src={staticFile(TC.logoMotion)}
        muted
        style={{width: "100%", height: "100%", objectFit: "contain"}}
      />
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// Montaje: disolvencias A MANO. Nunca TransitionSeries con GL sobre video —
// mete frames negros (ver memoria reel-video-gotchas).
export const FADE = 10;

const FadeIn: React.FC<{dur: number; children: React.ReactNode}> = ({dur, children}) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, dur], [0, 1], {extrapolateRight: "clamp"});
  return <AbsoluteFill style={{opacity: o}}>{children}</AbsoluteFill>;
};

// Escena que arranca FADE frames antes y sube opacidad sobre la anterior.
export const Scene: React.FC<{cut: {from: number; dur: number}; children: React.ReactNode}> = ({cut, children}) => (
  <Sequence from={Math.max(0, cut.from - FADE)} durationInFrames={cut.dur + FADE} layout="none">
    <FadeIn dur={FADE}>{children}</FadeIn>
  </Sequence>
);

// El contenido arranca en el frame 0 real de la escena, no en el del cruce:
// así los textos no entran durante la disolvencia.
export const Inner: React.FC<{children: React.ReactNode}> = ({children}) => (
  <Sequence from={FADE} layout="none">
    {children}
  </Sequence>
);

// Cifra grande: el elemento más grande de la pieza, en serif de marca.
// Regla del brief de pauta — las piezas con cifra concreta rinden 4,5× mejor.
export const BigFigure: React.FC<{
  figure: React.ReactNode;
  label?: React.ReactNode;
  kicker?: string;
  delay?: number;
  size?: number;
}> = ({figure, label, kicker, delay = 8, size = 168}) => (
  <SafeBlock top={720} align="center">
    {kicker && (
      <Reveal delay={delay}>
        <Kicker align="center">{kicker}</Kicker>
      </Reveal>
    )}
    <Reveal delay={delay + 8}>
      <Headline size={size} weight={400} align="center" lh={0.98} tracking="-0.035em">
        {figure}
      </Headline>
    </Reveal>
    {label && (
      <>
        <Reveal delay={delay + 26}>
          <Rule width={120} align="center" />
        </Reveal>
        <Reveal delay={delay + 32}>
          <Body size={33} align="center">
            {label}
          </Body>
        </Reveal>
      </>
    )}
  </SafeBlock>
);

// ---------------------------------------------------------------------------
// Plano fijo animado a partir de una imagen IA. Mismo lenguaje que `Clip`, pero
// con foto: se usa donde no hay metraje propio (por ejemplo la mesa montada del
// reel del 18, que el rodaje del 07-08 no cubrió). El zoom va SIEMPRE hacia
// afuera o muy lento hacia adentro: un push-in rápido delata que es un fijo.
export const ClipFoto: React.FC<{
  src: string;
  dur: number;
  zoom?: [number, number];
  pan?: [number, number];
  foco?: string;
}> = ({src, dur, zoom = [1.16, 1.04], pan = [0, 0], foco = "50% 50%"}) => {
  const frame = useCurrentFrame();
  const s = interpolate(frame, [0, dur], zoom, {extrapolateRight: "clamp"});
  const x = interpolate(frame, [0, dur], [0, pan[0]], {extrapolateRight: "clamp"});
  const y = interpolate(frame, [0, dur], [0, pan[1]], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      <Img
        src={staticFile(src)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          objectPosition: foco,
          transform: `scale(${s}) translate(${x}px, ${y}px)`,
        }}
      />
    </AbsoluteFill>
  );
};
