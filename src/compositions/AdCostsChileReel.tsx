import React from "react";
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  Sequence,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {loadDefaultFonts} from "../presets/fonts";
import {scopemedia as SM} from "../brand/scopemedia";

// =============================================================================
// DATA — rangos de REFERENCIA de mercado (CLP), 2026. NO son cifras auditadas.
// Reemplazar por la data real de las cuentas antes de publicar como "dato Scope".
// =============================================================================
const DATA = {
  platforms: [
    {name: "Meta", sub: "IG · Facebook", color: "#1877F2", cpm: 3500, cpc: 280},
    {name: "Google", sub: "Search · PMax", color: "#FBBC05", cpm: 2000, cpc: 650},
    {name: "TikTok", sub: "Feed · Spark", color: "#25F4EE", cpm: 4200, cpc: 300},
    {name: "Pinterest", sub: "Pins", color: "#E60023", cpm: 2800, cpc: 380},
  ],
  cpmMax: 5000, // techo para normalizar barras
  industries: [
    {name: "Retail / E-commerce", index: 0.8},
    {name: "Servicios / PYME", index: 1.0},
    {name: "Inmobiliaria", index: 1.4},
    {name: "Salud / Estética", index: 1.5},
    {name: "Finanzas / Legal", index: 1.9},
  ],
};

const fmtCLP = (n: number) => "$" + n.toLocaleString("es-CL");

// Ritmo rápido / trend (18s total)
const FPS = 30;
const HOOK_END = Math.round(2.3 * FPS);  // 69
const PLAT_END = Math.round(7.8 * FPS);  // 234
const IND_END = 12 * FPS;                // 360
const INSIGHT_END = Math.round(15 * FPS);// 450
const CTA_END = 18 * FPS;                // 540
const TOTAL = CTA_END;

// =============================================================================
// SHARED
// =============================================================================
const NavyBg: React.FC<{children?: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const x1 = 30 + Math.sin(t * 0.25) * 14;
  const y1 = 30 + Math.cos(t * 0.18) * 10;
  const x2 = 75 + Math.cos(t * 0.22) * 12;
  const y2 = 70 + Math.sin(t * 0.3) * 14;
  return (
    <AbsoluteFill style={{backgroundColor: SM.colors.bg}}>
      <AbsoluteFill
        style={{
          background: `
            radial-gradient(ellipse 60% 50% at ${x1}% ${y1}%, ${SM.colors.teal}28 0%, transparent 55%),
            radial-gradient(ellipse 50% 45% at ${x2}% ${y2}%, ${SM.colors.tealDeep}40 0%, transparent 60%),
            linear-gradient(180deg, ${SM.colors.bgDeep}, ${SM.colors.bg} 50%, ${SM.colors.bgDeep})
          `,
        }}
      />
      {children}
    </AbsoluteFill>
  );
};

const Particles: React.FC<{count?: number}> = ({count = 16}) => {
  const frame = useCurrentFrame();
  return (
    <>
      {Array.from({length: count}).map((_, i) => {
        const seed = i * 137.508;
        const baseX = seed % 1080;
        const baseY = (seed * 0.7) % 1920;
        const speed = 0.3 + (i % 3) * 0.18;
        const dy = Math.sin((frame / FPS) * speed + i) * 28;
        const dx = Math.cos((frame / FPS) * (speed * 0.8) + i * 0.7) * 18;
        const size = 4 + (i % 3) * 4;
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: baseX + dx,
              top: baseY + dy,
              width: size,
              height: size,
              borderRadius: "50%",
              background: SM.colors.teal,
              boxShadow: `0 0 ${size * 2}px ${SM.colors.teal}`,
              opacity: 0.3 + (i % 5) * 0.07,
            }}
          />
        );
      })}
    </>
  );
};

const EyebrowChip: React.FC<{text: string; delay?: number}> = ({text, delay = 0}) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [delay, delay + 14], [0, 1], {extrapolateRight: "clamp"});
  const y = interpolate(frame, [delay, delay + 14], [-12, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const dotPulse = 0.7 + Math.sin(frame / 12) * 0.3;
  return (
    <div
      style={{
        opacity,
        transform: `translateY(${y}px)`,
        display: "inline-flex",
        alignItems: "center",
        gap: 12,
        padding: "10px 20px",
        background: `${SM.colors.navy}AA`,
        backdropFilter: "blur(12px)",
        border: `1px solid ${SM.colors.teal}66`,
        borderRadius: 999,
      }}
    >
      <span
        style={{
          width: 9,
          height: 9,
          background: SM.colors.teal,
          borderRadius: "50%",
          boxShadow: `0 0 ${10 + dotPulse * 12}px ${SM.colors.teal}`,
          opacity: dotPulse,
        }}
      />
      <span
        style={{
          color: SM.colors.tealBright,
          fontFamily: SM.fonts.mono,
          fontSize: 18,
          fontWeight: 700,
          letterSpacing: "0.28em",
          textTransform: "uppercase",
        }}
      >
        {text}
      </span>
    </div>
  );
};

// =============================================================================
// ACT 1 — HOOK
// =============================================================================
const HookAct: React.FC = () => {
  const frame = useCurrentFrame();
  const exit = interpolate(frame, [HOOK_END - 14, HOOK_END], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const words = ["¿Cuánto", "cuesta", "REALMENTE", "pautar", "en", "Chile?"];
  return (
    <AbsoluteFill style={{opacity: exit}}>
      <NavyBg>
        <Particles count={20} />
        <AbsoluteFill
          style={{justifyContent: "center", alignItems: "center", flexDirection: "column", gap: 38, padding: "0 70px"}}
        >
          <EyebrowChip text="PRECIOS DE PAUTA · 2026" delay={6} />
          <div style={{display: "flex", flexWrap: "wrap", gap: 16, justifyContent: "center", maxWidth: 940}}>
            {words.map((w, i) => {
              const start = 4 + i * 2.5;
              const wIn = interpolate(frame, [start, start + 7], [0, 1], {
                extrapolateRight: "clamp",
                easing: Easing.out(Easing.cubic),
              });
              const isHero = w === "REALMENTE";
              return (
                <span
                  key={i}
                  style={{
                    opacity: wIn,
                    transform: `translateY(${interpolate(wIn, [0, 1], [30, 0])}px)`,
                    display: "inline-block",
                    color: isHero ? SM.colors.teal : SM.colors.white,
                    fontFamily: SM.fonts.display,
                    fontSize: isHero ? 96 : 82,
                    fontWeight: 900,
                    letterSpacing: "-0.035em",
                    lineHeight: 1.04,
                    fontStyle: isHero ? "italic" : "normal",
                    textShadow: isHero ? `0 0 30px ${SM.colors.teal}88` : "0 4px 18px rgba(0,0,0,0.6)",
                  }}
                >
                  {w}
                </span>
              );
            })}
          </div>
        </AbsoluteFill>
      </NavyBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 2 — PLATFORM COSTS
// =============================================================================
const PlatformsAct: React.FC = () => {
  const frame = useCurrentFrame();
  const local = PLAT_END - HOOK_END;
  const exit = interpolate(frame, [local - 14, local], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{opacity: exit}}>
      <NavyBg>
        <Particles count={12} />
        <AbsoluteFill style={{padding: "0 56px", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "stretch", gap: 22}}>
          <div style={{alignSelf: "center", opacity: interpolate(frame, [0, 10], [0, 1], {extrapolateRight: "clamp"})}}>
            <EyebrowChip text="COSTO POR PLATAFORMA" />
          </div>
          <div
            style={{
              color: SM.colors.white,
              fontFamily: SM.fonts.display,
              fontSize: 54,
              fontWeight: 900,
              letterSpacing: "-0.03em",
              lineHeight: 1.0,
              textAlign: "center",
              marginBottom: 4,
              opacity: interpolate(frame, [3, 14], [0, 1], {extrapolateRight: "clamp"}),
            }}
          >
            CPM y CPC <span style={{color: SM.colors.teal}}>de referencia.</span>
          </div>

          <div style={{display: "flex", flexDirection: "column", gap: 16}}>
            {DATA.platforms.map((p, i) => {
              const delay = 8 + i * 8;
              const op = interpolate(frame, [delay, delay + 10], [0, 1], {extrapolateRight: "clamp"});
              const x = interpolate(frame, [delay, delay + 13], [-34, 0], {
                extrapolateRight: "clamp",
                easing: Easing.out(Easing.cubic),
              });
              const barW = interpolate(
                frame,
                [delay + 7, delay + 26],
                [0, (p.cpm / DATA.cpmMax) * 100],
                {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)},
              );
              return (
                <div
                  key={i}
                  style={{
                    opacity: op,
                    transform: `translateX(${x}px)`,
                    background: `${SM.colors.teal}0E`,
                    border: `1.5px solid ${SM.colors.teal}30`,
                    borderRadius: 20,
                    padding: "20px 24px",
                  }}
                >
                  <div style={{display: "flex", alignItems: "center", gap: 16, marginBottom: 14}}>
                    <div
                      style={{
                        width: 48,
                        height: 48,
                        borderRadius: 12,
                        background: p.color,
                        boxShadow: `0 0 18px ${p.color}77`,
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        color: "#fff",
                        fontFamily: SM.fonts.display,
                        fontSize: 26,
                        fontWeight: 900,
                        flexShrink: 0,
                      }}
                    >
                      {p.name[0]}
                    </div>
                    <div style={{flex: 1}}>
                      <div
                        style={{
                          color: SM.colors.white,
                          fontFamily: SM.fonts.display,
                          fontSize: 32,
                          fontWeight: 800,
                          letterSpacing: "-0.02em",
                          lineHeight: 1,
                        }}
                      >
                        {p.name}
                      </div>
                      <div style={{color: SM.colors.text, fontFamily: SM.fonts.mono, fontSize: 15, opacity: 0.7, letterSpacing: "0.04em"}}>
                        {p.sub}
                      </div>
                    </div>
                    <div style={{textAlign: "right"}}>
                      <div style={{color: SM.colors.teal, fontFamily: SM.fonts.mono, fontSize: 30, fontWeight: 800, letterSpacing: "-0.02em"}}>
                        {fmtCLP(p.cpm)}
                      </div>
                      <div style={{color: SM.colors.text, fontFamily: SM.fonts.mono, fontSize: 16, opacity: 0.75}}>
                        CPM · CPC {fmtCLP(p.cpc)}
                      </div>
                    </div>
                  </div>
                  <div style={{height: 9, background: `${SM.colors.bg}99`, borderRadius: 6, overflow: "hidden"}}>
                    <div
                      style={{
                        height: "100%",
                        width: `${barW}%`,
                        background: `linear-gradient(90deg, ${SM.colors.tealDeep}, ${SM.colors.teal})`,
                        boxShadow: `0 0 14px ${SM.colors.teal}AA`,
                        borderRadius: 6,
                      }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </AbsoluteFill>
      </NavyBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 3 — INDUSTRY
// =============================================================================
const IndustryAct: React.FC = () => {
  const frame = useCurrentFrame();
  const local = IND_END - PLAT_END;
  const exit = interpolate(frame, [local - 14, local], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const maxIdx = Math.max(...DATA.industries.map((d) => d.index));
  return (
    <AbsoluteFill style={{opacity: exit}}>
      <NavyBg>
        <Particles count={12} />
        <AbsoluteFill style={{padding: "0 56px", display: "flex", flexDirection: "column", justifyContent: "center", gap: 24}}>
          <div style={{alignSelf: "center", opacity: interpolate(frame, [0, 10], [0, 1], {extrapolateRight: "clamp"})}}>
            <EyebrowChip text="SEGÚN INDUSTRIA" />
          </div>
          <div
            style={{
              color: SM.colors.white,
              fontFamily: SM.fonts.display,
              fontSize: 58,
              fontWeight: 900,
              letterSpacing: "-0.03em",
              lineHeight: 0.98,
              textAlign: "center",
              opacity: interpolate(frame, [3, 14], [0, 1], {extrapolateRight: "clamp"}),
            }}
          >
            No todas pagan <span style={{color: SM.colors.teal}}>lo mismo.</span>
          </div>
          <div style={{display: "flex", flexDirection: "column", gap: 18, marginTop: 4}}>
            {DATA.industries.map((d, i) => {
              const delay = 10 + i * 7;
              const op = interpolate(frame, [delay, delay + 10], [0, 1], {extrapolateRight: "clamp"});
              const barW = interpolate(frame, [delay + 5, delay + 24], [0, (d.index / maxIdx) * 100], {
                extrapolateRight: "clamp",
                easing: Easing.out(Easing.cubic),
              });
              return (
                <div key={i} style={{opacity: op}}>
                  <div style={{display: "flex", justifyContent: "space-between", alignItems: "flex-end", marginBottom: 8}}>
                    <span style={{color: SM.colors.cream, fontFamily: SM.fonts.display, fontSize: 28, fontWeight: 700, letterSpacing: "-0.02em"}}>
                      {d.name}
                    </span>
                    <span style={{color: SM.colors.teal, fontFamily: SM.fonts.mono, fontSize: 26, fontWeight: 800}}>
                      {d.index.toFixed(1)}x
                    </span>
                  </div>
                  <div style={{height: 14, background: `${SM.colors.bg}99`, borderRadius: 8, overflow: "hidden"}}>
                    <div
                      style={{
                        height: "100%",
                        width: `${barW}%`,
                        background: `linear-gradient(90deg, ${SM.colors.tealDeep}, ${SM.colors.tealBright})`,
                        boxShadow: `0 0 14px ${SM.colors.teal}AA`,
                        borderRadius: 8,
                      }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
          <div
            style={{
              marginTop: 6,
              color: SM.colors.text,
              fontFamily: SM.fonts.mono,
              fontSize: 16,
              opacity: interpolate(frame, [54, 72], [0, 0.7], {extrapolateRight: "clamp"}),
              letterSpacing: "0.04em",
            }}
          >
            índice de costo relativo · base = servicios/PYME
          </div>
        </AbsoluteFill>
      </NavyBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 4 — INSIGHT
// =============================================================================
const InsightAct: React.FC = () => {
  const frame = useCurrentFrame();
  const local = INSIGHT_END - IND_END;
  const exit = interpolate(frame, [local - 14, local], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const l1 = interpolate(frame, [3, 15], [0, 1], {extrapolateRight: "clamp"});
  const l2 = interpolate(frame, [15, 29], [0, 1], {extrapolateRight: "clamp"});
  const underline = interpolate(frame, [28, 50], [0, 420], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  return (
    <AbsoluteFill style={{opacity: exit}}>
      <NavyBg>
        <Particles count={16} />
        <AbsoluteFill style={{background: `radial-gradient(circle at 50% 45%, ${SM.colors.teal}22 0%, transparent 50%)`}} />
        <AbsoluteFill style={{justifyContent: "center", alignItems: "center", flexDirection: "column", gap: 24, padding: "0 70px"}}>
          <EyebrowChip text="LA VERDAD INCÓMODA" delay={2} />
          <div style={{textAlign: "center", maxWidth: 920}}>
            <div
              style={{
                opacity: l1,
                transform: `translateY(${interpolate(l1, [0, 1], [24, 0])}px)`,
                color: SM.colors.white,
                fontFamily: SM.fonts.display,
                fontSize: 76,
                fontWeight: 900,
                letterSpacing: "-0.035em",
                lineHeight: 1.05,
              }}
            >
              El precio no es el problema.
            </div>
            <div
              style={{
                opacity: l2,
                transform: `translateY(${interpolate(l2, [0, 1], [24, 0])}px)`,
                color: SM.colors.teal,
                fontFamily: SM.fonts.display,
                fontSize: 84,
                fontWeight: 900,
                letterSpacing: "-0.04em",
                lineHeight: 1.05,
                marginTop: 14,
                textShadow: `0 0 34px ${SM.colors.teal}77`,
              }}
            >
              El desperdicio sí.
            </div>
          </div>
          <div style={{width: underline, height: 5, background: SM.colors.teal, borderRadius: 3, boxShadow: `0 0 22px ${SM.colors.teal}DD`, marginTop: 8}} />
          <div
            style={{
              opacity: interpolate(frame, [48, 66], [0, 1], {extrapolateRight: "clamp"}),
              color: SM.colors.cream,
              fontFamily: SM.fonts.display,
              fontSize: 34,
              fontWeight: 500,
              textAlign: "center",
              maxWidth: 820,
              lineHeight: 1.3,
              marginTop: 8,
            }}
          >
            Puedes pagar un buen CPM y aun así perder dinero en errores invisibles.
          </div>
        </AbsoluteFill>
      </NavyBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 5 — CTA / BRAND
// =============================================================================
const CTAAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const bgIn = interpolate(frame, [0, 10], [0, 1], {extrapolateRight: "clamp"});
  const logoOp = interpolate(frame, [3, 16], [0, 1], {extrapolateRight: "clamp"});
  const logoScale = spring({frame, fps, delay: 3, config: {damping: 14, mass: 0.9}});
  const tagOp = interpolate(frame, [18, 34], [0, 1], {extrapolateRight: "clamp"});
  const urlOp = interpolate(frame, [36, 52], [0, 1], {extrapolateRight: "clamp"});
  const urlScale = spring({frame, fps, delay: 36, config: {damping: 12, mass: 0.6}});
  const ctaOp = interpolate(frame, [54, 72], [0, 1], {extrapolateRight: "clamp"});
  const arrow = 1 + Math.sin(frame / 6) * 0.08;
  return (
    <AbsoluteFill style={{opacity: bgIn}}>
      <NavyBg>
        <Particles count={24} />
        <AbsoluteFill style={{background: `radial-gradient(circle at 50% 48%, ${SM.colors.teal}22 0%, transparent 50%)`}} />
        <AbsoluteFill style={{justifyContent: "center", alignItems: "center", flexDirection: "column", gap: 34, padding: "0 60px"}}>
          <Img
            src={staticFile("brand/scope_logo_white.png")}
            style={{
              width: 360,
              height: "auto",
              opacity: logoOp,
              transform: `scale(${0.9 + logoScale * 0.1})`,
              filter: `drop-shadow(0 12px 50px ${SM.colors.teal}77)`,
            }}
          />
          <div style={{height: 8}} />
          <div
            style={{
              opacity: tagOp,
              transform: `translateY(${interpolate(tagOp, [0, 1], [22, 0])}px)`,
              color: SM.colors.cream,
              fontFamily: SM.fonts.display,
              fontSize: 58,
              fontWeight: 700,
              letterSpacing: "-0.03em",
              textAlign: "center",
            }}
          >
            Audita antes de <span style={{color: SM.colors.teal, textShadow: `0 0 24px ${SM.colors.teal}66`}}>invertir.</span>
          </div>
          <div style={{opacity: urlOp, transform: `scale(${0.93 + urlScale * 0.07})`, display: "flex", flexDirection: "column", alignItems: "center", gap: 14, marginTop: 14}}>
            <div style={{width: 200, height: 4, background: SM.colors.teal, borderRadius: 2, boxShadow: `0 0 22px ${SM.colors.teal}DD`}} />
            <div style={{color: SM.colors.teal, fontFamily: SM.fonts.mono, fontSize: 50, fontWeight: 800, letterSpacing: "0.02em", textShadow: `0 0 26px ${SM.colors.teal}66`}}>
              scopeaudits.com
            </div>
          </div>
          <div
            style={{
              opacity: ctaOp,
              marginTop: 8,
              padding: "20px 34px",
              background: SM.colors.teal,
              borderRadius: 999,
              display: "flex",
              alignItems: "center",
              gap: 16,
              boxShadow: `0 8px 36px ${SM.colors.teal}66`,
            }}
          >
            <span style={{color: SM.colors.bg, fontFamily: SM.fonts.display, fontSize: 28, fontWeight: 800}}>
              Audita tu campaña · $50 USD
            </span>
            <span style={{color: SM.colors.bg, fontSize: 32, fontWeight: 900, transform: `scale(${arrow})`}}>→</span>
          </div>
        </AbsoluteFill>
      </NavyBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// MAIN
// =============================================================================
export const AdCostsChileReel: React.FC = () => {
  loadDefaultFonts();
  return (
    <AbsoluteFill style={{backgroundColor: SM.colors.bg}}>
      <Sequence from={0} durationInFrames={HOOK_END}>
        <HookAct />
      </Sequence>
      <Sequence from={HOOK_END} durationInFrames={PLAT_END - HOOK_END}>
        <PlatformsAct />
      </Sequence>
      <Sequence from={PLAT_END} durationInFrames={IND_END - PLAT_END}>
        <IndustryAct />
      </Sequence>
      <Sequence from={IND_END} durationInFrames={INSIGHT_END - IND_END}>
        <InsightAct />
      </Sequence>
      <Sequence from={INSIGHT_END} durationInFrames={CTA_END - INSIGHT_END}>
        <CTAAct />
      </Sequence>
    </AbsoluteFill>
  );
};

export const AD_COSTS_REEL_DURATION = TOTAL;
