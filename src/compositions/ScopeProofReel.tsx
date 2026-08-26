import React from "react";
import {
  AbsoluteFill,
  Audio,
  Easing,
  interpolate,
  Sequence,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {loadDefaultFonts} from "../presets/fonts";
import {scopemedia as SM} from "../brand/scopemedia";
import {VideoClip} from "../components/media/VideoClip";

// =============================================================================
// SCOPE AUDITS — Reel de prueba social (MAQUETA · sin VO, para trend)
// Material: cara del chico (sorpresa) + scroll de auditoría Andes Outdoor.
// Estructura: HOOK (cara sorprendida) → SCROLL auditoría → CIERRE (oferta).
// Sin voz en off: se le pone audio de trend por encima.
// Formato IG Reel 9:16 · 30 fps · ~15 s.
// =============================================================================

const C = SM.colors;

// --- Segmentos (frames) -------------------------------------------------------
const A_END = 117;            // INTRO content creator · 0–3.9s (su video + su audio)
const B_END = 357;            // SCROLL · 3.9–11.9s
const C_END = 477;            // CIERRE · 11.9–15.9s
export const SCOPE_PROOF_DURATION = C_END;

// =============================================================================
// OVERLAYS PERSISTENTES — vignette + wordmark + barra de progreso
// =============================================================================
const Wordmark: React.FC<{hide?: boolean}> = ({hide}) => {
  const frame = useCurrentFrame();
  const op = interpolate(frame, [4, 18], [0, 0.96], {extrapolateRight: "clamp"});
  const pulse = 0.7 + Math.sin(frame / 11) * 0.3;
  if (hide) return null;
  return (
    <div
      style={{
        position: "absolute",
        top: 66,
        left: 56,
        opacity: op,
        display: "inline-flex",
        alignItems: "center",
        gap: 11,
        fontFamily: SM.fonts.display,
        fontSize: 34,
        fontWeight: 800,
        letterSpacing: "-0.02em",
      }}
    >
      <span
        style={{
          width: 12,
          height: 12,
          borderRadius: "50%",
          background: C.teal,
          boxShadow: `0 0 ${8 + pulse * 12}px ${C.teal}`,
          opacity: pulse,
        }}
      />
      <span style={{color: C.white}}>scope</span>
      <span style={{color: C.teal}}>audits</span>
    </div>
  );
};

const ProgressBar: React.FC = () => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [0, C_END], [0, 1], {extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", bottom: 0, left: 0, right: 0, height: 6, background: `${C.white}1A`}}>
      <div style={{width: `${p * 100}%`, height: "100%", background: C.teal, boxShadow: `0 0 14px ${C.teal}`}} />
    </div>
  );
};

// =============================================================================
// HELPERS de caption
// =============================================================================
const Caption: React.FC<{
  from: number;
  to: number;
  children: React.ReactNode;
  fontSize?: number;
  bottom?: number;
}> = ({from, to, children, fontSize = 58, bottom = 230}) => {
  const frame = useCurrentFrame();
  const op = interpolate(
    frame,
    [from, from + 8, to - 8, to],
    [0, 1, 1, 0],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp"}
  );
  const y = interpolate(frame, [from, from + 10], [26, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  return (
    <div
      style={{
        position: "absolute",
        left: 60,
        right: 60,
        bottom,
        textAlign: "center",
        opacity: op,
        transform: `translateY(${y}px)`,
        color: C.white,
        fontFamily: SM.fonts.display,
        fontSize,
        fontWeight: 800,
        lineHeight: 1.12,
        letterSpacing: "-0.025em",
        textShadow: "0 6px 30px rgba(0,0,0,0.6)",
      }}
    >
      {children}
    </div>
  );
};

const Teal: React.FC<{children: React.ReactNode}> = ({children}) => (
  <span style={{color: C.teal}}>{children}</span>
);

// =============================================================================
// ACT A — INTRO del content creator (su video + su audio + su caption quemado)
// =============================================================================
const IntroAct: React.FC = () => {
  return (
    <AbsoluteFill>
      {/* audio de la intro silenciado: la música la pone una sola pista continua (abajo) */}
      <VideoClip src={staticFile("assets/scope/creator.mp4")} trimStartSeconds={0} trimEndSeconds={3.9} fit="cover" muted />
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT B — PANTALLA (IMG_4501) limpia y legible · captions bajos que no la tapan
// =============================================================================
// Scrim solo en el borde superior (oculta la URL/chrome) e inferior (legibilidad
// de captions sobre el teclado). El centro queda libre para ver el reporte.
const ScreenScrim: React.FC = () => (
  <AbsoluteFill
    style={{
      background: `linear-gradient(180deg, ${C.bgDeep}F2 0%, transparent 13%, transparent 63%, ${C.bgDeep}F2 100%)`,
      pointerEvents: "none",
    }}
  />
);

const ScrollAct: React.FC = () => {
  return (
    <AbsoluteFill>
      <VideoClip src={staticFile("assets/scope/scroll.mov")} trimStartSeconds={0.6} trimEndSeconds={8.6} fit="cover" muted />
      <ScreenScrim />
      {/* captions compactos, abajo (zona del teclado) — no cubren la pantalla */}
      <Caption from={4} to={116} fontSize={46} bottom={140}>
        Esto encontró <Teal>ScopeAudits</Teal> en una auditoría
      </Caption>
      <Caption from={122} to={240} fontSize={50} bottom={140}>
        <Teal>$920.000</Teal>/mes en gasto desperdiciado
      </Caption>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT C — CIERRE · oferta (sin cara) + CTA scopeaudits.com
// =============================================================================
const OfferAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const t = frame / 30;
  const gx = 50 + Math.sin(t * 0.5) * 12;
  const gy = 38 + Math.cos(t * 0.4) * 10;

  const bgIn = interpolate(frame, [0, 10], [0, 1], {extrapolateRight: "clamp"});
  const markSp = spring({frame, fps, delay: 2, config: {damping: 14, mass: 0.9}});
  const markOp = interpolate(frame, [2, 16], [0, 1], {extrapolateRight: "clamp"});
  const headOp = interpolate(frame, [14, 28], [0, 1], {extrapolateRight: "clamp"});
  const headY = interpolate(frame, [14, 30], [22, 0], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  const priceSp = spring({frame, fps, delay: 26, config: {damping: 11, mass: 0.6}});
  const priceOp = interpolate(frame, [26, 40], [0, 1], {extrapolateRight: "clamp"});
  const ctaOp = interpolate(frame, [48, 60], [0, 1], {extrapolateRight: "clamp"});
  const ctaSp = spring({frame, fps, delay: 48, config: {damping: 12, mass: 0.6}});
  const arrow = 1 + Math.sin(frame / 6) * 0.12;
  const footOp = interpolate(frame, [64, 78], [0, 0.7], {extrapolateRight: "clamp"});

  return (
    <AbsoluteFill style={{opacity: bgIn, backgroundColor: C.bgDeep}}>
      {/* fondo navy con glow teal */}
      <AbsoluteFill
        style={{
          background: `
            radial-gradient(ellipse 60% 50% at ${gx}% ${gy}%, ${C.teal}26 0%, transparent 58%),
            radial-gradient(ellipse 50% 45% at 80% 80%, ${C.tealDeep}40 0%, transparent 62%),
            linear-gradient(180deg, ${C.bgDeep}, ${C.bg} 50%, ${C.bgDeep})
          `,
        }}
      />
      <AbsoluteFill style={{justifyContent: "center", alignItems: "center", flexDirection: "column", padding: "0 70px"}}>
        {/* wordmark grande */}
        <div
          style={{
            opacity: markOp,
            transform: `scale(${0.9 + markSp * 0.1})`,
            display: "inline-flex",
            alignItems: "center",
            gap: 14,
            fontFamily: SM.fonts.display,
            fontSize: 56,
            fontWeight: 900,
            letterSpacing: "-0.03em",
            marginBottom: 40,
          }}
        >
          <span style={{width: 18, height: 18, borderRadius: "50%", background: C.teal, boxShadow: `0 0 22px ${C.teal}`}} />
          <span style={{color: C.white}}>scope</span>
          <span style={{color: C.teal}}>audits</span>
        </div>

        {/* headline */}
        <div
          style={{
            opacity: headOp,
            transform: `translateY(${headY}px)`,
            color: C.white,
            fontFamily: SM.fonts.display,
            fontSize: 62,
            fontWeight: 800,
            letterSpacing: "-0.03em",
            textAlign: "center",
            lineHeight: 1.08,
          }}
        >
          Audita tus cuentas
        </div>

        {/* precio */}
        <div style={{opacity: priceOp, transform: `scale(${0.85 + priceSp * 0.15})`, textAlign: "center", marginTop: 14}}>
          <div style={{color: C.text, fontFamily: SM.fonts.display, fontSize: 34, fontWeight: 600, opacity: 0.85}}>
            por solo
          </div>
          <div style={{color: C.teal, fontFamily: SM.fonts.display, fontSize: 132, fontWeight: 900, letterSpacing: "-0.05em", lineHeight: 1, textShadow: `0 0 50px ${C.teal}55`}}>
            $50.000
          </div>
        </div>

        {/* CTA */}
        <div
          style={{
            opacity: ctaOp,
            transform: `scale(${0.92 + ctaSp * 0.08})`,
            marginTop: 38,
            padding: "20px 42px",
            background: C.teal,
            borderRadius: 999,
            display: "flex",
            alignItems: "center",
            gap: 14,
            boxShadow: `0 14px 44px ${C.teal}55`,
          }}
        >
          <span style={{color: C.bgDeep, fontFamily: SM.fonts.display, fontSize: 40, fontWeight: 900, letterSpacing: "-0.01em"}}>
            scopeaudits.com
          </span>
          <span style={{color: C.bgDeep, fontSize: 38, fontWeight: 900, transform: `scale(${arrow})`}}>→</span>
        </div>

        {/* footer */}
        <div
          style={{
            opacity: footOp,
            marginTop: 44,
            color: C.text,
            fontFamily: SM.fonts.mono,
            fontSize: 24,
            fontWeight: 600,
            letterSpacing: "0.06em",
            textAlign: "center",
          }}
        >
          Software parte de <span style={{color: C.white, fontWeight: 700}}>Grupo Copylab</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// =============================================================================
// MAIN
// =============================================================================
export const ScopeProofReel: React.FC = () => {
  loadDefaultFonts();
  return (
    <AbsoluteFill style={{backgroundColor: C.bgDeep}}>
      <Sequence from={0} durationInFrames={A_END}>
        <IntroAct />
      </Sequence>
      <Sequence from={A_END} durationInFrames={B_END - A_END}>
        <ScrollAct />
      </Sequence>
      <Sequence from={B_END} durationInFrames={C_END - B_END}>
        <OfferAct />
      </Sequence>

      {/* Música: UNA sola pista continua desde el segundo 0 del tema, todo el reel.
          Fade in corto + volumen estable + fade out al final. No se reinicia. */}
      <Audio
        src={staticFile("assets/scope/music.mp3")}
        volume={(f) =>
          interpolate(
            f,
            [0, 8, C_END - 22, C_END],
            [0, 0.7, 0.7, 0],
            {extrapolateLeft: "clamp", extrapolateRight: "clamp"}
          )
        }
      />

      {/* Wordmark solo sobre el scroll (la intro trae su propia caption; el cierre su propio mark) */}
      <Sequence from={A_END} durationInFrames={B_END - A_END}>
        <Wordmark />
      </Sequence>
      <ProgressBar />
    </AbsoluteFill>
  );
};
