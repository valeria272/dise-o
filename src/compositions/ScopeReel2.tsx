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
import {loadDefaultFonts} from "../presets/fonts";
import {scopemedia as SM} from "../brand/scopemedia";

// =============================================================================
// SCOPE REEL 2.0 — "Diagnóstico cinematográfico" (craft premium, no plantilla)
// Crossfades manuales (opacity + focus-pull desde desenfoque + push), HUD de
// escaneo sobre la pantalla, tipografía cinética, grano fílmico y cierre con
// barrido de luz. Sin TransitionSeries GL (evita el bug de video negro en la
// escena entrante). Assets reales + clip de pantalla normalizado (screen.mp4).
// 9:16 · 30 fps · 16 s.
// =============================================================================

const C = SM.colors;

// Video full-bleed
const coverVideo: React.CSSProperties = {width: "100%", height: "100%", objectFit: "cover"};

// Escenas: from + duración (con solape OV para el crossfade)
const OV = 14;
const A_FROM = 0;
const A_DUR = 122;
const B_FROM = A_FROM + A_DUR - OV; // 108
const B_DUR = 250;
const C_FROM = B_FROM + B_DUR - OV; // 344
const C_DUR = 140;
export const SCOPE_REEL2_DURATION = C_FROM + C_DUR; // 484

// =============================================================================
// HELPERS
// =============================================================================
// Focus-pull: entra desde desenfoque + leve escala.
const focusReveal = (frame: number, start: number, dur: number) => {
  const p = interpolate(frame, [start, start + dur], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  return {opacity: p, blur: interpolate(p, [0, 1], [16, 0]), scale: interpolate(p, [0, 1], [1.07, 1])};
};

// Crossfade de escena (opacidad) según frame local + duración.
const crossOpacity = (frame: number, dur: number, inF: number, outF: number) => {
  const fin = interpolate(frame, [0, inF], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const fout = outF > 0 ? interpolate(frame, [dur - outF, dur], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 1;
  return Math.min(fin, fout);
};

const fmtCLP = (n: number) => "$" + Math.round(n).toLocaleString("es-CL");

// Grano fílmico animado
const Grain: React.FC<{opacity?: number; id: string}> = ({opacity = 0.055, id}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{opacity, mixBlendMode: "overlay", pointerEvents: "none"}}>
      <svg width="100%" height="100%">
        <filter id={id}>
          <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves={2} seed={frame % 73} stitchTiles="stitch" />
          <feColorMatrix type="saturate" values="0" />
        </filter>
        <rect width="100%" height="100%" filter={`url(#${id})`} />
      </svg>
    </AbsoluteFill>
  );
};

const Vignette: React.FC = () => (
  <AbsoluteFill
    style={{background: "radial-gradient(ellipse 78% 62% at 50% 44%, transparent 40%, rgba(2,8,18,0.55) 100%)", pointerEvents: "none"}}
  />
);

// Barrido de luz diagonal (shine)
const Shine: React.FC<{from: number; dur: number; delay?: number}> = ({from, dur, delay = 0}) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [from + delay, from + delay + dur], [-30, 130], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  });
  return (
    <AbsoluteFill
      style={{background: `linear-gradient(105deg, transparent ${p - 18}%, ${C.white}66 ${p}%, transparent ${p + 18}%)`, mixBlendMode: "screen", pointerEvents: "none"}}
    />
  );
};

// =============================================================================
// ACT A — INTRO creator (cinematográfica)
// =============================================================================
const IntroAct: React.FC = () => {
  const frame = useCurrentFrame();
  const rev = focusReveal(frame, 0, 14);
  const kb = interpolate(frame, [0, A_DUR], [1.0, 1.05]);
  const op = crossOpacity(frame, A_DUR, 6, OV);
  const push = 1 + interpolate(frame, [A_DUR - OV, A_DUR], [0, 0.05], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const wm = focusReveal(frame, 10, 18);
  const dot = 0.6 + Math.sin(frame / 9) * 0.4;
  return (
    <AbsoluteFill style={{backgroundColor: C.bgDeep, opacity: op, transform: `scale(${push})`}}>
      <AbsoluteFill style={{transform: `scale(${kb * rev.scale})`, filter: `blur(${rev.blur}px) brightness(1.22) contrast(1.06) saturate(1.06)`}}>
        <OffthreadVideo src={staticFile("assets/scope/creator.mp4")} muted trimBefore={0} trimAfter={122} style={coverVideo} />
      </AbsoluteFill>
      <Vignette />
      <Grain id="grainA" />
      <div
        style={{
          position: "absolute",
          bottom: 120,
          left: 56,
          opacity: wm.opacity,
          filter: `blur(${wm.blur}px)`,
          display: "inline-flex",
          alignItems: "center",
          gap: 10,
          fontFamily: SM.fonts.display,
          fontSize: 30,
          fontWeight: 800,
          letterSpacing: "-0.02em",
        }}
      >
        <span style={{width: 11, height: 11, borderRadius: "50%", background: C.teal, boxShadow: `0 0 ${7 + dot * 12}px ${C.teal}`, opacity: dot}} />
        <span style={{color: C.white}}>scope</span>
        <span style={{color: C.teal}}>audits</span>
      </div>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT B — PANTALLA diagnóstico + HUD + tipografía cinética
// =============================================================================
const HudBrackets: React.FC<{frame: number}> = ({frame}) => {
  const p = interpolate(frame, [10, 30], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  const inset = interpolate(p, [0, 1], [70, 44]);
  const len = 60;
  const b = (extra: React.CSSProperties): React.CSSProperties => ({position: "absolute", width: len, height: len, borderColor: C.teal, opacity: p * 0.9, boxShadow: `0 0 12px ${C.teal}55`, ...extra});
  return (
    <>
      <div style={b({top: inset, left: inset, borderTop: "3px solid", borderLeft: "3px solid"})} />
      <div style={b({top: inset, right: inset, borderTop: "3px solid", borderRight: "3px solid"})} />
      <div style={b({bottom: inset, left: inset, borderBottom: "3px solid", borderLeft: "3px solid"})} />
      <div style={b({bottom: inset, right: inset, borderBottom: "3px solid", borderRight: "3px solid"})} />
    </>
  );
};

const ScanLine: React.FC<{frame: number}> = ({frame}) => {
  const y = (frame % 85) / 85;
  const op = interpolate(frame, [8, 24], [0, 0.5], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", left: 44, right: 44, top: `${8 + y * 84}%`, height: 2, background: `linear-gradient(90deg, transparent, ${C.tealBright}, transparent)`, opacity: op, boxShadow: `0 0 16px ${C.teal}`}} />
  );
};

const WasteCounter: React.FC<{frame: number}> = ({frame}) => {
  const inP = interpolate(frame, [40, 58], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  const out = interpolate(frame, [150, 164], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const val = interpolate(frame, [46, 120], [0, 920000], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  const underline = interpolate(frame, [64, 120], [0, 340], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  const labelText = "› GASTO DESPERDICIADO";
  const label = Math.min(1, Math.max(0, (frame - 40) / 18));
  const chars = Math.ceil(label * labelText.length);
  return (
    <div style={{position: "absolute", left: 60, right: 60, bottom: 300, textAlign: "center", opacity: inP * out, filter: `blur(${(1 - inP) * 10}px)`}}>
      <div style={{color: C.tealBright, fontFamily: SM.fonts.mono, fontSize: 22, fontWeight: 700, letterSpacing: "0.16em"}}>{labelText.slice(0, chars)}</div>
      <div style={{color: C.white, fontFamily: SM.fonts.display, fontSize: 118, fontWeight: 900, letterSpacing: "-0.05em", lineHeight: 1, marginTop: 8, textShadow: `0 0 40px ${C.teal}66`}}>{fmtCLP(val)}</div>
      <div style={{width: underline, height: 4, background: `linear-gradient(90deg, ${C.teal}, ${C.tealBright})`, borderRadius: 2, margin: "16px auto 0", boxShadow: `0 0 14px ${C.teal}`}} />
      <div style={{color: C.text, fontFamily: SM.fonts.mono, fontSize: 24, marginTop: 14, opacity: 0.8, letterSpacing: "0.04em"}}>al mes · 7% del presupuesto</div>
    </div>
  );
};

const KineticFindings: React.FC<{frame: number}> = ({frame}) => {
  const lines = ["Campañas mal configuradas", "Oportunidades ocultas"];
  return (
    <div style={{position: "absolute", left: 60, right: 60, bottom: 320, textAlign: "center"}}>
      {lines.map((l, i) => {
        const s = 172 + i * 16;
        const rev = focusReveal(frame, s, 16);
        const out = interpolate(frame, [B_DUR - 12, B_DUR], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
        return (
          <div
            key={i}
            style={{
              opacity: rev.opacity * out,
              filter: `blur(${rev.blur}px)`,
              transform: `translateY(${interpolate(rev.opacity, [0, 1], [18, 0])}px)`,
              color: i === 1 ? C.tealBright : C.white,
              fontFamily: SM.fonts.display,
              fontSize: 58,
              fontWeight: 800,
              letterSpacing: "-0.03em",
              lineHeight: 1.16,
              textShadow: "0 6px 30px rgba(0,0,0,0.6)",
            }}
          >
            {l}
          </div>
        );
      })}
    </div>
  );
};

const ScreenAct: React.FC = () => {
  const frame = useCurrentFrame();
  const rev = focusReveal(frame, 0, 18);
  const kb = interpolate(frame, [0, B_DUR], [1.02, 1.09]);
  const op = crossOpacity(frame, B_DUR, OV, OV);
  const push = 1 + interpolate(frame, [B_DUR - OV, B_DUR], [0, 0.05], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{backgroundColor: C.bgDeep, opacity: op, transform: `scale(${push})`}}>
      <AbsoluteFill style={{transform: `scale(${kb * rev.scale})`, filter: `blur(${rev.blur}px)`}}>
        <OffthreadVideo src={staticFile("assets/scope/screen.mp4")} muted trimBefore={18} trimAfter={276} style={coverVideo} />
      </AbsoluteFill>
      <AbsoluteFill style={{background: `linear-gradient(180deg, ${C.bgDeep}F2 0%, transparent 15%, transparent 55%, ${C.bgDeep}F5 100%)`, pointerEvents: "none"}} />
      <HudBrackets frame={frame} />
      <ScanLine frame={frame} />
      <Grain id="grainB" opacity={0.05} />
      <WasteCounter frame={frame} />
      <KineticFindings frame={frame} />
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT C — CIERRE oferta (aurora + barrido de luz)
// =============================================================================
const OfferAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const op = crossOpacity(frame, C_DUR, OV, 0);
  const t = frame / 30;
  const gx = 50 + Math.sin(t * 0.5) * 14;
  const gy = 40 + Math.cos(t * 0.42) * 12;

  const wm = focusReveal(frame, 2, 16);
  const dot = 0.6 + Math.sin(frame / 8) * 0.4;
  const head1 = focusReveal(frame, 16, 14);
  const head2 = focusReveal(frame, 24, 14);
  const priceSp = spring({frame, fps, delay: 34, config: {damping: 11, mass: 0.6}});
  const priceOp = interpolate(frame, [34, 46], [0, 1], {extrapolateRight: "clamp"});
  const ctaOp = interpolate(frame, [58, 70], [0, 1], {extrapolateRight: "clamp"});
  const ctaSp = spring({frame, fps, delay: 58, config: {damping: 12, mass: 0.6}});
  const arrow = 1 + Math.sin(frame / 6) * 0.12;
  const footOp = interpolate(frame, [76, 90], [0, 0.72], {extrapolateRight: "clamp"});

  return (
    <AbsoluteFill style={{backgroundColor: C.bgDeep, opacity: op}}>
      <AbsoluteFill
        style={{
          background: `
            radial-gradient(ellipse 62% 52% at ${gx}% ${gy}%, ${C.teal}2E 0%, transparent 58%),
            radial-gradient(ellipse 50% 46% at 82% 84%, ${C.tealDeep}4D 0%, transparent 62%),
            radial-gradient(ellipse 46% 40% at 16% 22%, ${C.tealBright}1A 0%, transparent 60%),
            linear-gradient(180deg, ${C.bgDeep}, ${C.bg} 50%, ${C.bgDeep})
          `,
        }}
      />
      <Grain id="grainC" opacity={0.05} />
      <AbsoluteFill style={{justifyContent: "center", alignItems: "center", flexDirection: "column", padding: "0 70px"}}>
        <div style={{opacity: wm.opacity, filter: `blur(${wm.blur}px)`, display: "inline-flex", alignItems: "center", gap: 14, fontFamily: SM.fonts.display, fontSize: 54, fontWeight: 900, letterSpacing: "-0.03em", marginBottom: 42}}>
          <span style={{width: 18, height: 18, borderRadius: "50%", background: C.teal, boxShadow: `0 0 ${14 + dot * 16}px ${C.teal}`, opacity: dot}} />
          <span style={{color: C.white}}>scope</span>
          <span style={{color: C.teal}}>audits</span>
        </div>

        <div style={{textAlign: "center", lineHeight: 1.04}}>
          <div style={{opacity: head1.opacity, filter: `blur(${head1.blur}px)`, color: C.white, fontFamily: SM.fonts.display, fontSize: 66, fontWeight: 800, letterSpacing: "-0.035em"}}>Audita tus cuentas</div>
          <div style={{opacity: head2.opacity * 0.9, filter: `blur(${head2.blur}px)`, color: C.text, fontFamily: SM.fonts.display, fontSize: 34, fontWeight: 600, marginTop: 12}}>antes de invertir un peso</div>
        </div>

        <div style={{position: "relative", opacity: priceOp, transform: `scale(${0.82 + priceSp * 0.18})`, marginTop: 22}}>
          <div style={{color: C.teal, fontFamily: SM.fonts.display, fontSize: 148, fontWeight: 900, letterSpacing: "-0.055em", lineHeight: 1, textShadow: `0 0 60px ${C.teal}66`}}>$50.000</div>
          <Shine from={40} dur={26} delay={6} />
        </div>

        <div style={{position: "relative", overflow: "hidden", opacity: ctaOp, transform: `scale(${0.92 + ctaSp * 0.08})`, marginTop: 34, padding: "20px 44px", background: C.teal, borderRadius: 999, display: "flex", alignItems: "center", gap: 14, boxShadow: `0 14px 44px ${C.teal}66`}}>
          <span style={{color: C.bgDeep, fontFamily: SM.fonts.display, fontSize: 40, fontWeight: 900, letterSpacing: "-0.01em"}}>scopeaudits.com</span>
          <span style={{color: C.bgDeep, fontSize: 38, fontWeight: 900, transform: `scale(${arrow})`}}>→</span>
          <Shine from={70} dur={24} delay={8} />
        </div>

        <div style={{opacity: footOp, marginTop: 44, color: C.text, fontFamily: SM.fonts.mono, fontSize: 24, fontWeight: 600, letterSpacing: "0.06em", textAlign: "center"}}>
          Software parte de <span style={{color: C.white, fontWeight: 700}}>Grupo Copylab</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// =============================================================================
// MAIN — Sequences con solape (crossfade manual), sin TransitionSeries GL
// =============================================================================
export const ScopeReel2: React.FC = () => {
  loadDefaultFonts();
  return (
    <AbsoluteFill style={{backgroundColor: C.bgDeep}}>
      <Sequence from={A_FROM} durationInFrames={A_DUR}>
        <IntroAct />
      </Sequence>
      <Sequence from={B_FROM} durationInFrames={B_DUR}>
        <ScreenAct />
      </Sequence>
      <Sequence from={C_FROM} durationInFrames={C_DUR}>
        <OfferAct />
      </Sequence>

      <Audio
        src={staticFile("assets/scope/music.mp3")}
        volume={(f) =>
          interpolate(f, [0, 8, SCOPE_REEL2_DURATION - 22, SCOPE_REEL2_DURATION], [0, 0.7, 0.7, 0], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          })
        }
      />
    </AbsoluteFill>
  );
};
