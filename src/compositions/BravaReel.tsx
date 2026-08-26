import React from "react";
import {
  AbsoluteFill,
  Audio,
  Easing,
  interpolate,
  OffthreadVideo,
  Sequence,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {loadGoogleFont} from "../presets/fonts";

// =============================================================================
// BRAVA — Reel cine MODERNO (v3). Video real (Kling i2v) + tipografía
// contemporánea: revelados con máscara + tracking + blur, layouts asimétricos,
// labels en mono, capa UI mínima (timecode / marca / barra), grade cinemático.
// 9:16 · 30 fps · ~14 s.
// =============================================================================

const DISP = "Archivo, Inter, sans-serif";
const MONO = "'JetBrains Mono', ui-monospace, monospace";
const INK = "#0A0A0C";
const PAPER = "#F4F1EA";
const ACCENT = "#FF7A1A";

const cover: React.CSSProperties = {width: "100%", height: "100%", objectFit: "cover"};

const HOOK = 108, PAW = 96, RUN = 108, CLOSE = 108;
const P0 = HOOK, R0 = HOOK + PAW, C0 = HOOK + PAW + RUN;
export const BRAVA_REEL_DURATION = C0 + CLOSE; // 420

const SCENES = [
  {label: "CASO DE MARCA", n: "01"},
  {label: "EL TRATO", n: "02"},
  {label: "LA MANADA", n: "03"},
  {label: "BRAVA", n: "04"},
];

// ---------------------------------------------------------------------------
// Revelado con máscara (moderno): el texto sube desde detrás de un borde.
const Reveal: React.FC<{
  children: React.ReactNode;
  delay: number;
  size: number;
  color?: string;
  weight?: number;
  tracking?: string;
  lh?: number;
}> = ({children, delay, size, color = PAPER, weight = 900, tracking = "-0.045em", lh = 0.92}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const p = spring({frame, fps, delay, config: {damping: 22, mass: 0.9, stiffness: 95}});
  const y = interpolate(p, [0, 1], [118, 0]);
  const blur = interpolate(p, [0, 1], [10, 0]);
  return (
    <div style={{overflow: "hidden", padding: "0.06em 0"}}>
      <div
        style={{
          transform: `translateY(${y}%)`,
          filter: `blur(${blur}px)`,
          fontFamily: DISP,
          fontWeight: weight,
          fontSize: size,
          lineHeight: lh,
          letterSpacing: tracking,
          color,
          textTransform: "uppercase",
        }}
      >
        {children}
      </div>
    </div>
  );
};

// Kicker mono con tracking-in
const Kicker: React.FC<{children: React.ReactNode; delay: number; color?: string}> = ({children, delay, color = ACCENT}) => {
  const frame = useCurrentFrame();
  const op = interpolate(frame, [delay, delay + 12], [0, 1], {extrapolateRight: "clamp"});
  const ls = interpolate(frame, [delay, delay + 16], [0.55, 0.28], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  return (
    <div style={{opacity: op, display: "flex", alignItems: "center", gap: 14, marginBottom: 18}}>
      <div style={{width: 34, height: 2, background: color}} />
      <span style={{fontFamily: MONO, fontSize: 22, fontWeight: 700, letterSpacing: `${ls}em`, color, textTransform: "uppercase"}}>
        {children}
      </span>
    </div>
  );
};

// grade cinemático moderno (teal en sombras, cálido en luces, viñeta)
const Grade: React.FC = () => (
  <>
    <AbsoluteFill style={{background: "linear-gradient(180deg, rgba(6,18,26,0.30) 0%, transparent 34%, transparent 60%, rgba(4,8,12,0.66) 100%)", pointerEvents: "none"}} />
    <AbsoluteFill style={{background: "radial-gradient(ellipse 80% 65% at 50% 45%, transparent 45%, rgba(0,0,0,0.5) 100%)", pointerEvents: "none"}} />
  </>
);

const Grain: React.FC<{id: string}> = ({id}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{opacity: 0.05, mixBlendMode: "overlay", pointerEvents: "none"}}>
      <svg width="100%" height="100%">
        <filter id={id}><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves={2} seed={frame % 55} stitchTiles="stitch" /><feColorMatrix type="saturate" values="0" /></filter>
        <rect width="100%" height="100%" filter={`url(#${id})`} />
      </svg>
    </AbsoluteFill>
  );
};

const VideoScene: React.FC<{src: string; dur: number; trimBefore?: number; zoom?: [number, number]}> = ({src, dur, trimBefore = 0, zoom = [1.05, 1.12]}) => {
  const frame = useCurrentFrame();
  const s = interpolate(frame, [0, dur], zoom, {extrapolateRight: "clamp"});
  const inBlur = interpolate(frame, [0, 6], [8, 0], {extrapolateRight: "clamp"}); // micro blur-in por corte
  return (
    <AbsoluteFill style={{backgroundColor: INK}}>
      <AbsoluteFill style={{transform: `scale(${s})`, filter: `blur(${inBlur}px) contrast(1.06) saturate(0.92) brightness(1.02)`}}>
        <OffthreadVideo src={staticFile(src)} muted trimBefore={trimBefore} style={cover} />
      </AbsoluteFill>
      <Grade />
    </AbsoluteFill>
  );
};

// bloque de texto alineado a la izquierda, abajo (asimétrico moderno)
const LeftBlock: React.FC<{children: React.ReactNode; bottom?: number}> = ({children, bottom = 210}) => (
  <div style={{position: "absolute", left: 60, right: 120, bottom, textAlign: "left"}}>{children}</div>
);

// ---------------------------------------------------------------------------
const HookScene: React.FC = () => (
  <AbsoluteFill>
    <VideoScene src="assets/brava/hook_video.mp4" dur={HOOK} zoom={[1.04, 1.12]} />
    <LeftBlock bottom={200}>
      <Kicker delay={8}>Nuevo capítulo</Kicker>
      <Reveal delay={16} size={150} color={PAPER}>Brava</Reveal>
      <Reveal delay={30} size={46} weight={600} tracking="-0.02em" color="rgba(244,241,234,0.82)">ya tenía la comida.</Reveal>
      <div style={{height: 14}} />
      <Reveal delay={56} size={72} color={PAPER}>Ahora tiene</Reveal>
      <Reveal delay={68} size={72} color={ACCENT}>las palabras.</Reveal>
    </LeftBlock>
    <Grain id="gA" />
  </AbsoluteFill>
);

const PawScene: React.FC = () => (
  <AbsoluteFill>
    <VideoScene src="assets/brava/paw_video.mp4" dur={PAW} zoom={[1.12, 1.02]} />
    <LeftBlock bottom={210}>
      <Kicker delay={8}>El trato</Kicker>
      <Reveal delay={16} size={78} color={PAPER}>Cerramos</Reveal>
      <Reveal delay={26} size={78} color={PAPER}>el trato con</Reveal>
      <Reveal delay={40} size={96} color={ACCENT}>la pata.</Reveal>
    </LeftBlock>
    <Grain id="gP" />
  </AbsoluteFill>
);

const RunScene: React.FC = () => (
  <AbsoluteFill>
    <VideoScene src="assets/brava/run_video.mp4" dur={RUN} trimBefore={30} zoom={[1.0, 1.08]} />
    <LeftBlock bottom={200}>
      <Kicker delay={10}>Desde hoy</Kicker>
      <Reveal delay={18} size={90} color={PAPER}>Eres parte</Reveal>
      <Reveal delay={30} size={90} color={PAPER}>de la</Reveal>
      <Reveal delay={44} size={132} color={ACCENT}>manada.</Reveal>
    </LeftBlock>
    <Grain id="gR" />
  </AbsoluteFill>
);

const CloseScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const line = interpolate(frame, [8, 40], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic)});
  const markOp = interpolate(frame, [44, 60], [0, 1], {extrapolateRight: "clamp"});
  const p = spring({frame, fps, delay: 6, config: {damping: 20, mass: 0.8}});
  return (
    <AbsoluteFill style={{backgroundColor: INK}}>
      <AbsoluteFill style={{background: `radial-gradient(ellipse 80% 55% at 20% 40%, ${ACCENT}1F 0%, transparent 55%)`}} />
      {/* marco fino moderno */}
      <div style={{position: "absolute", inset: 40, border: "1.5px solid rgba(244,241,234,0.16)", opacity: interpolate(frame, [0, 14], [0, 1], {extrapolateRight: "clamp"})}} />
      <AbsoluteFill style={{justifyContent: "center", padding: "0 68px"}}>
        <div style={{transform: `translateY(${interpolate(p, [0, 1], [30, 0])}px)`}}>
          <div style={{fontFamily: MONO, fontSize: 22, fontWeight: 700, letterSpacing: "0.3em", color: ACCENT, marginBottom: 22}}>BIENVENIDO</div>
          <div style={{fontFamily: DISP, fontWeight: 900, fontSize: 120, lineHeight: 0.9, letterSpacing: "-0.05em", color: PAPER, textTransform: "uppercase"}}>
            a la<br /><span style={{color: ACCENT}}>manada.</span>
          </div>
          <div style={{width: `${line * 100}%`, maxWidth: 460, height: 2, background: "rgba(244,241,234,0.5)", margin: "40px 0 26px"}} />
          <div style={{opacity: markOp}}>
            <div style={{fontFamily: DISP, fontWeight: 900, fontSize: 40, letterSpacing: "-0.03em", color: PAPER}}>copywriters</div>
            <div style={{fontFamily: MONO, fontSize: 20, fontWeight: 500, color: "rgba(244,241,234,0.7)", marginTop: 10, maxWidth: 560}}>le ponemos palabras a las marcas que valen la pena.</div>
          </div>
        </div>
      </AbsoluteFill>
      <Grain id="gC" />
    </AbsoluteFill>
  );
};

// Capa UI persistente (timecode / marca / barra de progreso)
const UI: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const idx = frame < P0 ? 0 : frame < R0 ? 1 : frame < C0 ? 2 : 3;
  const sc = SCENES[idx];
  const prog = interpolate(frame, [0, durationInFrames], [0, 1], {extrapolateRight: "clamp"});
  const op = interpolate(frame, [4, 16], [0, 1], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{pointerEvents: "none", opacity: op}}>
      {/* barra de progreso fina */}
      <div style={{position: "absolute", top: 46, left: 60, right: 60, height: 2, background: "rgba(244,241,234,0.18)"}}>
        <div style={{width: `${prog * 100}%`, height: "100%", background: ACCENT}} />
      </div>
      {/* marca top-left · timecode top-right (mono) */}
      <div style={{position: "absolute", top: 66, left: 60, fontFamily: MONO, fontSize: 20, fontWeight: 700, letterSpacing: "0.14em", color: PAPER}}>BRAVA<span style={{color: ACCENT}}>×</span>CW</div>
      <div style={{position: "absolute", top: 66, right: 60, fontFamily: MONO, fontSize: 20, fontWeight: 500, letterSpacing: "0.1em", color: "rgba(244,241,234,0.75)"}}>{sc.n} / {sc.label}</div>
    </AbsoluteFill>
  );
};

export const BravaReel: React.FC = () => {
  loadGoogleFont("Archivo", "600;700;800;900");
  loadGoogleFont("JetBrains Mono", "500;700");
  return (
    <AbsoluteFill style={{backgroundColor: INK}}>
      <Sequence from={0} durationInFrames={HOOK}><HookScene /></Sequence>
      <Sequence from={P0} durationInFrames={PAW}><PawScene /></Sequence>
      <Sequence from={R0} durationInFrames={RUN}><RunScene /></Sequence>
      <Sequence from={C0} durationInFrames={CLOSE}><CloseScene /></Sequence>
      <UI />
      <Audio
        src={staticFile("assets/brava/music.mp3")}
        volume={(f) => interpolate(f, [0, 10, BRAVA_REEL_DURATION - 24, BRAVA_REEL_DURATION], [0, 0.65, 0.65, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})}
      />
    </AbsoluteFill>
  );
};
