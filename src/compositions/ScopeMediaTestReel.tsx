import React from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  Sequence,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {loadDefaultFonts} from "../presets/fonts";
import {scopemedia as SM} from "../brand/scopemedia";

const FPS = 30;
const TOTAL = 30 * FPS; // 900

const HOOK_END = 3 * FPS;       // 90
const SHOCK_END = 7 * FPS;      // 210
const PROBLEM_END = 12 * FPS;   // 360
const SOLUTION_END = 18 * FPS;  // 540
const PROOF_END = 25 * FPS;     // 750
const CTA_END = TOTAL;          // 900

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

const Particles: React.FC<{count?: number}> = ({count = 18}) => {
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
              opacity: 0.35 + (i % 5) * 0.08,
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
// ACT 1 — HOOK (0-3s): "¿Sabes cuánto desperdicias?"
// =============================================================================
const HookAct: React.FC = () => {
  const frame = useCurrentFrame();
  const exitOpacity = interpolate(frame, [HOOK_END - 14, HOOK_END], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const words = ["¿Sabes", "cuánto", "desperdicias", "en", "ads?"];

  // Glitch lines for tension
  const glitchY1 = (Math.sin(frame / 4) * 200 + 1500) % 1920;
  const glitchY2 = (Math.cos(frame / 5) * 200 + 800) % 1920;

  return (
    <AbsoluteFill style={{opacity: exitOpacity}}>
      <NavyBg>
        <Particles count={20} />

        {/* Glitch scan lines */}
        <div
          style={{
            position: "absolute",
            top: glitchY1,
            left: 0,
            right: 0,
            height: 2,
            background: `linear-gradient(90deg, transparent, ${SM.colors.teal}AA, transparent)`,
            opacity: 0.6,
          }}
        />
        <div
          style={{
            position: "absolute",
            top: glitchY2,
            left: 0,
            right: 0,
            height: 1,
            background: `linear-gradient(90deg, transparent, ${SM.colors.teal}66, transparent)`,
            opacity: 0.5,
          }}
        />

        <AbsoluteFill
          style={{
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column",
            gap: 38,
            padding: "0 60px",
          }}
        >
          <EyebrowChip text="ALERTA ADS" delay={6} />

          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              gap: 18,
              justifyContent: "center",
              maxWidth: 1000,
            }}
          >
            {words.map((w, i) => {
              const start = 12 + i * 4;
              const wIn = interpolate(frame, [start, start + 10], [0, 1], {
                extrapolateRight: "clamp",
                easing: Easing.out(Easing.cubic),
              });
              const wY = interpolate(wIn, [0, 1], [30, 0]);
              const isHero = w === "desperdicias";
              return (
                <span
                  key={i}
                  style={{
                    opacity: wIn,
                    transform: `translateY(${wY}px)`,
                    display: "inline-block",
                    color: isHero ? SM.colors.teal : SM.colors.white,
                    fontFamily: SM.fonts.display,
                    fontSize: isHero ? 100 : 84,
                    fontWeight: 900,
                    letterSpacing: "-0.035em",
                    lineHeight: 1.05,
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
// ACT 2 — SHOCK (3-7s): big 80% number counts up
// =============================================================================
const ShockAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const numProgress = interpolate(frame, [8, 38], [0, 1], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const num = Math.round(80 * numProgress);
  const numScale = spring({frame: Math.max(0, frame - 32), fps, config: {damping: 12, mass: 0.7}});

  const subOpacity = interpolate(frame, [42, 60], [0, 1], {extrapolateRight: "clamp"});
  const subY = interpolate(subOpacity, [0, 1], [20, 0]);

  const exitOpacity = interpolate(frame, [(SHOCK_END - HOOK_END) - 14, SHOCK_END - HOOK_END], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{opacity: exitOpacity}}>
      <NavyBg>
        <Particles count={24} />

        {/* Glow halo behind number */}
        <AbsoluteFill
          style={{
            background: `radial-gradient(circle at 50% 45%, ${SM.colors.teal}33 0%, transparent 35%)`,
          }}
        />

        <AbsoluteFill
          style={{
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column",
            gap: 40,
            padding: "0 60px",
          }}
        >
          <div
            style={{
              opacity: interpolate(frame, [0, 16], [0, 1], {extrapolateRight: "clamp"}),
            }}
          >
            <EyebrowChip text="UN DATO INCÓMODO" />
          </div>

          {/* Massive number */}
          <div
            style={{
              display: "flex",
              alignItems: "flex-start",
              gap: 12,
              transform: `scale(${0.85 + numScale * 0.15})`,
            }}
          >
            <span
              style={{
                color: SM.colors.teal,
                fontFamily: SM.fonts.display,
                fontSize: 460,
                fontWeight: 900,
                letterSpacing: "-0.07em",
                lineHeight: 0.85,
                textShadow: `0 0 60px ${SM.colors.teal}88, 0 12px 30px rgba(0,0,0,0.5)`,
              }}
            >
              {num}
            </span>
            <span
              style={{
                color: SM.colors.tealBright,
                fontFamily: SM.fonts.display,
                fontSize: 140,
                fontWeight: 900,
                letterSpacing: "-0.05em",
                lineHeight: 1.0,
                marginTop: 30,
              }}
            >
              %
            </span>
          </div>

          {/* Animated underline */}
          <div
            style={{
              width: interpolate(frame, [44, 70], [0, 380], {
                extrapolateRight: "clamp",
                easing: Easing.out(Easing.cubic),
              }),
              height: 5,
              background: SM.colors.teal,
              borderRadius: 3,
              boxShadow: `0 0 24px ${SM.colors.teal}DD`,
            }}
          />

          {/* Subtitle */}
          <div
            style={{
              opacity: subOpacity,
              transform: `translateY(${subY}px)`,
              color: SM.colors.white,
              fontFamily: SM.fonts.display,
              fontSize: 44,
              fontWeight: 700,
              letterSpacing: "-0.02em",
              lineHeight: 1.15,
              textAlign: "center",
              maxWidth: 900,
            }}
          >
            de las campañas pierden plata
            <br />
            en errores <span style={{color: SM.colors.teal, fontStyle: "italic"}}>invisibles</span>.
          </div>
        </AbsoluteFill>
      </NavyBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 3 — PROBLEM CONTEXT (7-12s): bars revealing types of losses
// =============================================================================
const ProblemAct: React.FC = () => {
  const frame = useCurrentFrame();
  const localFrames = PROBLEM_END - SHOCK_END;
  const exitOpacity = interpolate(frame, [localFrames - 14, localFrames], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const items = [
    {label: "Conversiones mal trackeadas", waste: "42%"},
    {label: "Audiencias mal segmentadas", waste: "31%"},
    {label: "Creativos quemados (fatiga)", waste: "27%"},
  ];

  return (
    <AbsoluteFill style={{opacity: exitOpacity}}>
      <NavyBg>
        <Particles count={14} />

        <AbsoluteFill
          style={{
            padding: "120px 60px 100px",
            display: "flex",
            flexDirection: "column",
            gap: 36,
          }}
        >
          <div
            style={{
              opacity: interpolate(frame, [0, 14], [0, 1], {extrapolateRight: "clamp"}),
            }}
          >
            <EyebrowChip text="DÓNDE SE FUGA" />
          </div>

          <div
            style={{
              color: SM.colors.white,
              fontFamily: SM.fonts.display,
              fontSize: 72,
              fontWeight: 900,
              letterSpacing: "-0.035em",
              lineHeight: 0.98,
              opacity: interpolate(frame, [4, 20], [0, 1], {extrapolateRight: "clamp"}),
            }}
          >
            Cada peso{" "}
            <span style={{color: SM.colors.teal, textShadow: `0 0 24px ${SM.colors.teal}66`}}>
              tiene un destino.
            </span>
          </div>

          <div style={{display: "flex", flexDirection: "column", gap: 22, marginTop: 14}}>
            {items.map((item, i) => {
              const delay = 18 + i * 12;
              const opacity = interpolate(frame, [delay, delay + 14], [0, 1], {
                extrapolateRight: "clamp",
              });
              const x = interpolate(frame, [delay, delay + 18], [-40, 0], {
                extrapolateRight: "clamp",
                easing: Easing.out(Easing.cubic),
              });
              const barWidth = interpolate(frame, [delay + 10, delay + 38], [0, parseInt(item.waste)], {
                extrapolateRight: "clamp",
                easing: Easing.out(Easing.cubic),
              });
              return (
                <div
                  key={i}
                  style={{
                    opacity,
                    transform: `translateX(${x}px)`,
                    background: `${SM.colors.teal}10`,
                    border: `1.5px solid ${SM.colors.teal}33`,
                    borderRadius: 18,
                    padding: "22px 26px",
                  }}
                >
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "center",
                      marginBottom: 12,
                    }}
                  >
                    <div
                      style={{
                        color: SM.colors.cream,
                        fontFamily: SM.fonts.display,
                        fontSize: 28,
                        fontWeight: 700,
                        letterSpacing: "-0.02em",
                      }}
                    >
                      {item.label}
                    </div>
                    <div
                      style={{
                        color: SM.colors.teal,
                        fontFamily: SM.fonts.mono,
                        fontSize: 28,
                        fontWeight: 900,
                        letterSpacing: "-0.02em",
                      }}
                    >
                      {item.waste}
                    </div>
                  </div>
                  <div
                    style={{
                      height: 10,
                      background: `${SM.colors.bg}99`,
                      borderRadius: 6,
                      overflow: "hidden",
                    }}
                  >
                    <div
                      style={{
                        height: "100%",
                        width: `${barWidth}%`,
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
// ACT 4 — SOLUTION (12-18s): brand reveal
// =============================================================================
const SolutionAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const localFrames = SOLUTION_END - PROBLEM_END;

  const bgIn = interpolate(frame, [0, 18], [0, 1], {extrapolateRight: "clamp"});
  const exitOpacity = interpolate(frame, [localFrames - 14, localFrames], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Logo mask reveal
  const logoReveal = interpolate(frame, [14, 50], [0, 100], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const logoOpacity = interpolate(frame, [10, 26], [0, 1], {extrapolateRight: "clamp"});
  const logoScale = spring({frame, fps, delay: 10, config: {damping: 14, mass: 0.9}});

  const taglineOpacity = interpolate(frame, [50, 70], [0, 1], {extrapolateRight: "clamp"});
  const taglineY = interpolate(frame, [50, 70], [30, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const underlineW = interpolate(frame, [68, 100], [0, 320], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const subTagOpacity = interpolate(frame, [95, 120], [0, 1], {extrapolateRight: "clamp"});

  return (
    <AbsoluteFill style={{opacity: Math.min(bgIn, exitOpacity)}}>
      <NavyBg>
        <Particles count={22} />

        <AbsoluteFill
          style={{
            background: `radial-gradient(circle at 50% 45%, ${SM.colors.teal}28 0%, transparent 50%)`,
          }}
        />

        <AbsoluteFill
          style={{
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column",
            gap: 40,
            padding: "0 60px",
          }}
        >
          {/* Logo type — text-based since no logo PNG */}
          <div
            style={{
              opacity: logoOpacity,
              transform: `scale(${0.88 + logoScale * 0.12})`,
              filter: `drop-shadow(0 12px 60px ${SM.colors.teal}88)`,
              clipPath: `inset(0 ${100 - logoReveal}% 0 0)`,
              WebkitClipPath: `inset(0 ${100 - logoReveal}% 0 0)`,
              display: "flex",
              alignItems: "center",
              gap: 16,
            }}
          >
            <div
              style={{
                width: 22,
                height: 22,
                background: SM.colors.teal,
                borderRadius: 6,
                boxShadow: `0 0 24px ${SM.colors.teal}`,
                transform: "rotate(45deg)",
              }}
            />
            <div
              style={{
                color: SM.colors.white,
                fontFamily: SM.fonts.display,
                fontSize: 130,
                fontWeight: 900,
                letterSpacing: "-0.045em",
                lineHeight: 1.0,
              }}
            >
              Scope <span style={{color: SM.colors.teal}}>Media</span>
            </div>
          </div>

          {/* Tagline */}
          <div
            style={{
              opacity: taglineOpacity,
              transform: `translateY(${taglineY}px)`,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              gap: 22,
            }}
          >
            <div
              style={{
                color: SM.colors.cream,
                fontFamily: SM.fonts.display,
                fontSize: 56,
                fontWeight: 600,
                letterSpacing: "-0.025em",
                textAlign: "center",
              }}
            >
              Audita antes de{" "}
              <span style={{color: SM.colors.teal, textShadow: `0 0 24px ${SM.colors.teal}66`}}>
                invertir.
              </span>
            </div>
            <div
              style={{
                width: underlineW,
                height: 5,
                background: SM.colors.teal,
                borderRadius: 3,
                boxShadow: `0 0 22px ${SM.colors.teal}DD`,
              }}
            />
          </div>

          {/* Sub */}
          <div
            style={{
              opacity: subTagOpacity,
              color: SM.colors.tealBright,
              fontFamily: SM.fonts.mono,
              fontSize: 22,
              fontWeight: 700,
              letterSpacing: "0.28em",
              textTransform: "uppercase",
              marginTop: 12,
            }}
          >
            Auditoría de campañas · 48 hrs
          </div>
        </AbsoluteFill>
      </NavyBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 5 — PROOF (18-25s): 3 feature cards entering with stagger
// =============================================================================
const ProofAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const localFrames = PROOF_END - SOLUTION_END;
  const exitOpacity = interpolate(frame, [localFrames - 14, localFrames], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const features = [
    {
      icon: "◎",
      title: "Diagnóstico completo",
      body: "Revisamos cada campaña, audiencia, creatividad y configuración.",
    },
    {
      icon: "◉",
      title: "Detección de leaks",
      body: "Encontramos dónde se va tu plata sin que vos lo veas.",
    },
    {
      icon: "▲",
      title: "Plan de acción claro",
      body: "Reporte ejecutivo con prioridades y próximos pasos.",
    },
  ];

  return (
    <AbsoluteFill style={{opacity: exitOpacity}}>
      <NavyBg>
        <Particles count={14} />

        <AbsoluteFill style={{padding: "120px 60px 100px", display: "flex", flexDirection: "column", gap: 30}}>
          <div
            style={{
              opacity: interpolate(frame, [0, 14], [0, 1], {extrapolateRight: "clamp"}),
            }}
          >
            <EyebrowChip text="QUÉ INCLUYE" />
          </div>

          <div
            style={{
              color: SM.colors.white,
              fontFamily: SM.fonts.display,
              fontSize: 64,
              fontWeight: 900,
              letterSpacing: "-0.035em",
              lineHeight: 0.98,
              opacity: interpolate(frame, [4, 22], [0, 1], {extrapolateRight: "clamp"}),
            }}
          >
            Tu auditoría,{" "}
            <span style={{color: SM.colors.teal}}>de punta a punta.</span>
          </div>

          {/* Feature cards */}
          <div style={{display: "flex", flexDirection: "column", gap: 22, marginTop: 8}}>
            {features.map((f, i) => {
              const delay = 24 + i * 16;
              const enter = spring({
                frame: Math.max(0, frame - delay),
                fps,
                config: {damping: 14, mass: 0.7},
              });
              const opacity = interpolate(frame, [delay, delay + 14], [0, 1], {
                extrapolateRight: "clamp",
              });
              const x = interpolate(enter, [0, 1], [60, 0]);
              return (
                <div
                  key={i}
                  style={{
                    opacity,
                    transform: `translateX(${x}px)`,
                    background: `${SM.colors.teal}10`,
                    border: `1.5px solid ${SM.colors.teal}55`,
                    borderRadius: 22,
                    padding: "26px 26px",
                    display: "flex",
                    gap: 22,
                    alignItems: "center",
                    boxShadow: `0 8px 30px rgba(0,0,0,0.3)`,
                  }}
                >
                  <div
                    style={{
                      width: 72,
                      height: 72,
                      borderRadius: 18,
                      background: SM.colors.teal,
                      color: SM.colors.bg,
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      fontSize: 38,
                      fontWeight: 900,
                      flexShrink: 0,
                      boxShadow: `0 0 20px ${SM.colors.teal}66`,
                    }}
                  >
                    {f.icon}
                  </div>
                  <div style={{flex: 1, display: "flex", flexDirection: "column", gap: 6}}>
                    <div
                      style={{
                        color: SM.colors.white,
                        fontFamily: SM.fonts.display,
                        fontSize: 30,
                        fontWeight: 800,
                        letterSpacing: "-0.02em",
                        lineHeight: 1.1,
                      }}
                    >
                      {f.title}
                    </div>
                    <div
                      style={{
                        color: SM.colors.text,
                        fontFamily: SM.fonts.display,
                        fontSize: 19,
                        fontWeight: 500,
                        opacity: 0.85,
                        lineHeight: 1.35,
                      }}
                    >
                      {f.body}
                    </div>
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
// ACT 6 — CTA (25-30s): URL + activate
// =============================================================================
const CTAAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const bgIn = interpolate(frame, [0, 16], [0, 1], {extrapolateRight: "clamp"});

  const headlineWords = ["Audita", "tu", "campaña."];
  const urlOpacity = interpolate(frame, [60, 80], [0, 1], {extrapolateRight: "clamp"});
  const urlScale = spring({frame, fps, delay: 60, config: {damping: 12, mass: 0.6}});
  const ctaOpacity = interpolate(frame, [85, 110], [0, 1], {extrapolateRight: "clamp"});
  const arrowPulse = 1 + Math.sin(frame / 6) * 0.08;

  return (
    <AbsoluteFill style={{opacity: bgIn}}>
      <NavyBg>
        <Particles count={26} />
        <AbsoluteFill
          style={{
            background: `radial-gradient(circle at 50% 50%, ${SM.colors.teal}22 0%, transparent 50%)`,
          }}
        />

        <AbsoluteFill
          style={{
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column",
            gap: 40,
            padding: "0 60px",
          }}
        >
          {/* Headline */}
          <div style={{display: "flex", flexWrap: "wrap", gap: 20, justifyContent: "center"}}>
            {headlineWords.map((w, i) => {
              const start = 12 + i * 6;
              const wIn = interpolate(frame, [start, start + 14], [0, 1], {
                extrapolateRight: "clamp",
                easing: Easing.out(Easing.cubic),
              });
              const wY = interpolate(wIn, [0, 1], [40, 0]);
              const isHero = w === "Audita";
              return (
                <span
                  key={i}
                  style={{
                    opacity: wIn,
                    transform: `translateY(${wY}px)`,
                    display: "inline-block",
                    color: isHero ? SM.colors.teal : SM.colors.white,
                    fontFamily: SM.fonts.display,
                    fontSize: 110,
                    fontWeight: 900,
                    letterSpacing: "-0.04em",
                    lineHeight: 1.0,
                    textShadow: isHero
                      ? `0 0 36px ${SM.colors.teal}88`
                      : "0 4px 20px rgba(0,0,0,0.5)",
                  }}
                >
                  {w}
                </span>
              );
            })}
          </div>

          {/* Subline */}
          <div
            style={{
              opacity: interpolate(frame, [35, 60], [0, 1], {extrapolateRight: "clamp"}),
              color: SM.colors.cream,
              fontFamily: SM.fonts.display,
              fontSize: 36,
              fontWeight: 500,
              textAlign: "center",
              maxWidth: 800,
              lineHeight: 1.3,
            }}
          >
            Sin compromisos. <span style={{color: SM.colors.teal}}>Sin sorpresas.</span>
          </div>

          {/* URL */}
          <div
            style={{
              opacity: urlOpacity,
              transform: `scale(${0.92 + urlScale * 0.08})`,
              marginTop: 28,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              gap: 16,
            }}
          >
            <div
              style={{
                width: 220,
                height: 4,
                background: SM.colors.teal,
                borderRadius: 2,
                boxShadow: `0 0 22px ${SM.colors.teal}DD`,
              }}
            />
            <div
              style={{
                color: SM.colors.teal,
                fontFamily: SM.fonts.mono,
                fontSize: 56,
                fontWeight: 800,
                letterSpacing: "0.04em",
                textShadow: `0 0 28px ${SM.colors.teal}66`,
              }}
            >
              scopemedia.cl
            </div>
          </div>

          {/* CTA pill */}
          <div
            style={{
              opacity: ctaOpacity,
              marginTop: 14,
              padding: "20px 32px",
              background: SM.colors.teal,
              borderRadius: 999,
              display: "flex",
              alignItems: "center",
              gap: 16,
              boxShadow: `0 8px 36px ${SM.colors.teal}66`,
            }}
          >
            <span
              style={{
                color: SM.colors.bg,
                fontFamily: SM.fonts.display,
                fontSize: 28,
                fontWeight: 800,
                letterSpacing: "-0.01em",
              }}
            >
              Activa tu auditoría gratis
            </span>
            <span
              style={{
                color: SM.colors.bg,
                fontSize: 32,
                fontWeight: 900,
                transform: `scale(${arrowPulse})`,
              }}
            >
              →
            </span>
          </div>
        </AbsoluteFill>
      </NavyBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// MAIN
// =============================================================================
export const ScopeMediaTestReel: React.FC = () => {
  loadDefaultFonts();
  return (
    <AbsoluteFill style={{backgroundColor: SM.colors.bg}}>
      <Sequence from={0} durationInFrames={HOOK_END}>
        <HookAct />
      </Sequence>
      <Sequence from={HOOK_END} durationInFrames={SHOCK_END - HOOK_END}>
        <ShockAct />
      </Sequence>
      <Sequence from={SHOCK_END} durationInFrames={PROBLEM_END - SHOCK_END}>
        <ProblemAct />
      </Sequence>
      <Sequence from={PROBLEM_END} durationInFrames={SOLUTION_END - PROBLEM_END}>
        <SolutionAct />
      </Sequence>
      <Sequence from={SOLUTION_END} durationInFrames={PROOF_END - SOLUTION_END}>
        <ProofAct />
      </Sequence>
      <Sequence from={PROOF_END} durationInFrames={CTA_END - PROOF_END}>
        <CTAAct />
      </Sequence>
    </AbsoluteFill>
  );
};
