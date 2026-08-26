import React from "react";
import {
  AbsoluteFill,
  interpolate,
  OffthreadVideo,
  Sequence,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

// =============================================================================
// TIERRA CALMA — Reel de BIENVENIDA (Copywriters da voz a un nuevo cliente).
// Estética PROPIA de Copywriters: Montserrat (juego de grosores) + Cormorant
// Garamond itálica como acento editorial. Tipografía cinética con movimiento
// (revelados con máscara + blur, salidas animadas — NO subtítulos estáticos),
// cortes al beat sobre tomas aéreas reales, grade cálido, cierre en crema con
// el logotipo real de Tierra Calma sin transformar.
// 9:16 · 30 fps · 16 s.
// =============================================================================

const SANS = "Montserrat, Inter, sans-serif";
const SERIF = "'Cormorant Garamond', 'Playfair Display', serif";

const PAPER = "#F6F1E7"; // crema Copywriters (tipografía sobre el paisaje)
const NAVY = "#14314C"; // navy oficial del motion del logo Tierra Calma
const WHITE = "#FFFFFF"; // fondo del motion del logo
const INK = "#0C1216";

// ---- fuentes AUTO-HOSPEDADAS (locales, sin red ni delayRender) --------------
// Montserrat variable + Cormorant Garamond itálica variable en public/assets/fonts.
// Se inyecta @font-face una sola vez; los archivos locales cargan en ms (el texto
// recién aparece en el frame ~10+, así que no hay FOUT visible). Además precargamos
// vía FontFace para acelerar el registro.
let tcFontsInjected = false;
const ensureTierraCalmaFonts = () => {
  if (tcFontsInjected || typeof document === "undefined") return;
  tcFontsInjected = true;
  const style = document.createElement("style");
  style.textContent = `
    @font-face {
      font-family: 'Montserrat';
      font-style: normal;
      font-weight: 100 900;
      font-display: block;
      src: url(${staticFile("assets/fonts/Montserrat.ttf")}) format('truetype');
    }
    @font-face {
      font-family: 'Cormorant Garamond';
      font-style: italic;
      font-weight: 300 700;
      font-display: block;
      src: url(${staticFile("assets/fonts/CormorantGaramond-Italic.ttf")}) format('truetype');
    }
  `;
  document.head.appendChild(style);
  const f = (document as any).fonts;
  if (f?.load) {
    f.load("400 100px Montserrat").catch(() => undefined);
    f.load("800 100px Montserrat").catch(() => undefined);
    f.load('italic 600 100px "Cormorant Garamond"').catch(() => undefined);
  }
};
ensureTierraCalmaFonts();

const cover: React.CSSProperties = {width: "100%", height: "100%", objectFit: "cover"};

// ---------------------------------------------------------------------------
// Grano de película
const Grain: React.FC<{id: string; opacity?: number}> = ({id, opacity = 0.045}) => {
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

// Grade cálido + scrims para legibilidad (arriba y abajo) + viñeta suave
const Grade: React.FC = () => (
  <>
    <AbsoluteFill
      style={{
        background:
          "linear-gradient(180deg, rgba(8,14,18,0.34) 0%, transparent 26%, transparent 52%, rgba(6,10,14,0.62) 100%)",
        pointerEvents: "none",
      }}
    />
    <AbsoluteFill
      style={{
        background: "radial-gradient(ellipse 90% 70% at 50% 45%, transparent 52%, rgba(0,0,0,0.42) 100%)",
        pointerEvents: "none",
      }}
    />
    <AbsoluteFill
      style={{
        background: "radial-gradient(ellipse 70% 50% at 60% 30%, rgba(255,214,150,0.10) 0%, transparent 60%)",
        mixBlendMode: "soft-light",
        pointerEvents: "none",
      }}
    />
  </>
);

// Clip con push-in continuo + micro blur-in por corte
const Clip: React.FC<{src: string; dur: number; zoom?: [number, number]; pan?: [number, number]}> = ({
  src,
  dur,
  zoom = [1.06, 1.14],
  pan = [0, 0],
}) => {
  const frame = useCurrentFrame();
  const s = interpolate(frame, [0, dur], zoom, {extrapolateRight: "clamp"});
  const ty = interpolate(frame, [0, dur], [pan[0], pan[1]], {extrapolateRight: "clamp"});
  const inBlur = interpolate(frame, [0, 7], [9, 0], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{backgroundColor: INK}}>
      <AbsoluteFill
        style={{
          transform: `scale(${s}) translateY(${ty}px)`,
          filter: `blur(${inBlur}px) contrast(1.05) saturate(1.02) brightness(1.02)`,
        }}
      >
        <OffthreadVideo src={staticFile(src)} muted style={cover} />
      </AbsoluteFill>
      <Grade />
    </AbsoluteFill>
  );
};

// Línea con revelado por máscara (entra desde abajo + blur) y salida animada
const Line: React.FC<{
  children: React.ReactNode;
  delay: number;
  exitAt: number;
  size: number;
  weight?: number;
  color?: string;
  tracking?: string;
  lh?: number;
  serif?: boolean;
}> = ({children, delay, exitAt, size, weight = 800, color = PAPER, tracking = "-0.03em", lh = 1.04, serif = false}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const p = spring({frame, fps, delay, config: {damping: 22, mass: 0.9, stiffness: 90}});
  const y = interpolate(p, [0, 1], [124, 0]);
  const blur = interpolate(p, [0, 1], [12, 0]);
  const out = interpolate(frame, [exitAt, exitAt + 12], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const outY = out * -46;
  const outOp = 1 - out;
  // La caja de recorte (overflow hidden) se agranda con padding para que NO corte
  // ascendentes/descendentes (g, y, j, tildes ni las colas de la cursiva). Los
  // márgenes negativos compensan ese padding para mantener el interlineado justo.
  return (
    <div
      style={{
        overflow: "hidden",
        paddingTop: "0.14em",
        paddingBottom: "0.26em",
        marginTop: "-0.14em",
        marginBottom: "-0.22em",
      }}
    >
      <div
        style={{
          transform: `translateY(${y + outY}px)`,
          filter: `blur(${blur}px)`,
          opacity: outOp,
          fontFamily: serif ? SERIF : SANS,
          fontWeight: weight,
          fontSize: size,
          lineHeight: lh,
          letterSpacing: tracking,
          color,
          textShadow: "0 3px 40px rgba(0,0,0,0.5), 0 1px 2px rgba(0,0,0,0.3)",
        }}
      >
        {children}
      </div>
    </div>
  );
};

// acento en cursiva editorial (Cormorant itálica)
const Em: React.FC<{children: React.ReactNode; k?: number}> = ({children, k = 1.14}) => (
  <span style={{fontFamily: SERIF, fontStyle: "italic", fontWeight: 500, fontSize: `${k}em`, letterSpacing: "-0.01em"}}>
    {children}
  </span>
);

const Block: React.FC<{children: React.ReactNode; bottom?: number; center?: boolean}> = ({
  children,
  bottom = 230,
  center = false,
}) => (
  <div
    style={{
      position: "absolute",
      left: 66,
      right: 96,
      bottom,
      textAlign: center ? "center" : "left",
      ...(center ? {left: 66, right: 66} : {}),
    }}
  >
    {children}
  </div>
);

// Dip a blanco al final de la última escena (empalma con el motion del logo,
// que ya trae su propio fondo blanco).
const WhiteDip: React.FC<{from: number; to: number}> = ({from, to}) => {
  const frame = useCurrentFrame();
  const op = interpolate(frame, [from, to], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return <AbsoluteFill style={{backgroundColor: WHITE, opacity: op, pointerEvents: "none"}} />;
};

// Transición sutil por escena: la toma ENTRANTE hace fade + micro-scale + blur
// sobre la saliente (disolvencia suave, no corte seco). Confiable con OffthreadVideo
// (crossfade manual, sin TransitionSeries GL).
const XF = 9; // frames de disolvencia (~0.3s) — cabe en el metraje sobrante de cada clip
const FadeIn: React.FC<{children: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const op = interpolate(frame, [0, XF], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const s = interpolate(frame, [0, XF], [1.03, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{opacity: op, transform: `scale(${s})`}}>{children}</AbsoluteFill>
  );
};

// Tag de esquina superior derecha ("new partner")
const CornerTag: React.FC<{children: React.ReactNode; exitAt: number}> = ({children, exitAt}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const p = spring({frame, fps, delay: 8, config: {damping: 200, stiffness: 90}});
  const out = interpolate(frame, [exitAt, exitAt + 12], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <div
      style={{
        position: "absolute",
        top: 82,
        right: 60,
        display: "flex",
        alignItems: "center",
        gap: 12,
        opacity: p * out,
      }}
    >
      <div style={{width: 7, height: 7, borderRadius: "50%", background: PAPER}} />
      <span
        style={{
          fontFamily: SANS,
          fontWeight: 600,
          fontSize: 21,
          letterSpacing: "0.32em",
          textTransform: "uppercase",
          color: PAPER,
          textShadow: "0 2px 18px rgba(0,0,0,0.5)",
        }}
      >
        {children}
      </span>
    </div>
  );
};

// ---------------------------------------------------------------------------
// Duraciones de escena (frames @30fps). Con menos texto el ritmo va más ágil;
// cada clip tiene metraje de sobra para el solapamiento de XF frames.
const D1 = 78, D2 = 66, D3 = 78, D4 = 84, D5 = 42;

// Escenas
const S1: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/tc1_mist.mp4" dur={D1} zoom={[1.08, 1.16]} pan={[10, -6]} />
    <CornerTag exitAt={66}>new partner</CornerTag>
    <Block bottom={244}>
      <Line delay={14} exitAt={64} size={66} weight={300}>Hay lugares</Line>
      <Line delay={24} exitAt={66} size={78} weight={800}>
        que se viven <Em k={1.24}>distinto</Em>.
      </Line>
    </Block>
    <Grain id="g1" />
  </AbsoluteFill>
);

// Escena 2: sin texto — puro paisaje, para que el reel respire.
const S2: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/tc2_meadow.mp4" dur={D2} zoom={[1.14, 1.05]} pan={[-8, 6]} />
    <Grain id="g2" />
  </AbsoluteFill>
);

const S3: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/tc3_golden.mp4" dur={D3} zoom={[1.05, 1.14]} pan={[8, -8]} />
    <Block bottom={244}>
      <Line delay={12} exitAt={64} size={60} weight={300} tracking="-0.01em">
        Donde el tiempo
      </Line>
      <Line delay={24} exitAt={66} size={98} weight={900} tracking="-0.045em">
        baja la voz.
      </Line>
    </Block>
    <Grain id="g3" />
  </AbsoluteFill>
);

const S4: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/tc4_sunset.mp4" dur={D4} zoom={[1.12, 1.04]} pan={[-6, 8]} />
    <Block bottom={250}>
      <Line delay={12} exitAt={70} size={68} weight={300}>Un refugio</Line>
      <Line delay={26} exitAt={72} size={94} weight={800}>
        con <Em k={1.22}>raíces</Em>.
      </Line>
    </Block>
    <Grain id="g4" />
  </AbsoluteFill>
);

const S5: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/tc5_flare.mp4" dur={D5} zoom={[1.06, 1.16]} pan={[6, -6]} />
    <div style={{position: "absolute", left: 66, right: 66, top: 790, textAlign: "center"}}>
      <Line delay={4} exitAt={54} size={56} weight={300} lh={1.12}>
        Hoy le damos
      </Line>
      <Line delay={12} exitAt={54} size={76} weight={800} lh={1.06}>
        la bienvenida a
      </Line>
    </div>
    {/* dip a BLANCO para empalmar con el motion del logo (que trae fondo blanco) */}
    <WhiteDip from={32} to={42} />
    <Grain id="g5" />
  </AbsoluteFill>
);

// Cierre — MOTION OFICIAL de Tierra Calma (su propia animación de logo, tal cual,
// sin re-animarla). Sobre su fondo blanco entra sólo la firma de Copywriters,
// discreta y una vez que el lockup ya está armado.
// Variantes: "signature" (con firma) | "logoOnly" (solo el motion de la marca).
const SClose: React.FC<{closeStyle: CloseStyle}> = ({closeStyle}) => {
  const frame = useCurrentFrame();
  const sig = interpolate(frame, [96, 116], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const rule = interpolate(frame, [92, 118], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const withSig = closeStyle === "signature";
  return (
    <AbsoluteFill style={{backgroundColor: WHITE}}>
      <OffthreadVideo src={staticFile("assets/tierracalma/tc_motion.mp4")} muted style={cover} />
      {withSig ? (
        <div style={{position: "absolute", left: 80, right: 80, top: 1330, textAlign: "center"}}>
          <div
            style={{
              width: rule * 220,
              height: 1.5,
              background: NAVY,
              opacity: 0.35,
              margin: "0 auto 30px",
            }}
          />
          <div style={{opacity: sig}}>
            <div
              style={{
                fontFamily: SANS,
                fontWeight: 700,
                fontSize: 24,
                letterSpacing: "0.4em",
                textTransform: "uppercase",
                color: NAVY,
              }}
            >
              Copywriters
            </div>
            <div
              style={{
                fontFamily: SERIF,
                fontStyle: "italic",
                fontWeight: 500,
                fontSize: 30,
                color: NAVY,
                opacity: 0.75,
                marginTop: 10,
                lineHeight: 1.3,
              }}
            >
              estrategia, creatividad y resultados.
            </div>
          </div>
        </div>
      ) : null}
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// D6 = 155 = largo exacto del motion oficial del logo (tc_motion.mp4 @30fps)
const D6 = 155;
const F1 = 0;
const F2 = F1 + D1;
const F3 = F2 + D2;
const F4 = F3 + D3;
const F5 = F4 + D4;
const F6 = F5 + D5;
export const TIERRACALMA_REEL_DURATION = F6 + D6; // 348 + 155 = 503 (~16.8s)

export type CloseStyle = "signature" | "logoOnly";
export type TierraCalmaReelProps = {closeStyle?: CloseStyle};

export const TierraCalmaReel: React.FC<TierraCalmaReelProps> = ({closeStyle = "signature"}) => {
  ensureTierraCalmaFonts();
  return (
  <AbsoluteFill style={{backgroundColor: INK}}>
    {/* Cada escena (menos la 1ª) entra con disolvencia sobre la saliente, que se
        extiende XF frames para solaparse. Transiciones suaves, sin cortes secos. */}
    <Sequence from={F1} durationInFrames={D1 + XF}>
      <S1 />
    </Sequence>
    <Sequence from={F2} durationInFrames={D2 + XF}>
      <FadeIn>
        <S2 />
      </FadeIn>
    </Sequence>
    <Sequence from={F3} durationInFrames={D3 + XF}>
      <FadeIn>
        <S3 />
      </FadeIn>
    </Sequence>
    <Sequence from={F4} durationInFrames={D4 + XF}>
      <FadeIn>
        <S4 />
      </FadeIn>
    </Sequence>
    <Sequence from={F5} durationInFrames={D5}>
      <FadeIn>
        <S5 />
      </FadeIn>
    </Sequence>
    <Sequence from={F6} durationInFrames={D6}>
      <SClose closeStyle={closeStyle} />
    </Sequence>
  </AbsoluteFill>
  );
};
