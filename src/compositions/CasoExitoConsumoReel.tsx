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
import {copywriters as CW} from "../brand/copywriters";

// =============================================================================
// CASO DE ÉXITO — Ecommerce de consumo (cliente ANONIMIZADO)
// Resultados reales (print Shopify · 18 may → 17 jun 2026, últimos 30 días).
// Sistema implementado: Agente Paid Media multicanal + Agente Email Marketing.
// Look & feel: marca Copywriters (cream / navy / lima). Formato IG Reel 9:16.
// =============================================================================

const C = CW.colors; // cream, navy, navyDeep, lime, limeBright, text, white

// Acentos cálidos (uso SUTIL): fucsia + naranjo como "spark" recurrente
const FUCHSIA = "#E0218A";
const ORANGE = "#FF7A1A";
const SPARK = `linear-gradient(120deg, ${ORANGE}, ${FUCHSIA})`;

const FPS = 30;
const s = (sec: number) => Math.round(sec * FPS);

const HOOK_END = s(3.3); // 99
const RETO_END = s(7.2); // 216
const SISTEMA_END = s(13.7); // 411
const AGENTES_END = s(19.7); // 591
const RESULTS_END = s(29.7); // 891
const CTA_END = s(33.7); // 1011
export const CASO_EXITO_REEL_DURATION = CTA_END;

// =============================================================================
// DATA — cifras del print (no inventar)
// =============================================================================
const VENTAS_TOTAL = 121842700;

const STATS = [
  {label: "Pedidos", value: "1.531", delta: 233, hint: "+233%"},
  {label: "Conversión", value: "1,89%", delta: 289, hint: "+289%"},
  {label: "Ticket promedio", value: "$79.600", delta: 11, hint: "+11%"},
];

const AGENT_FINDINGS = [
  {label: "Bugs técnicos en catálogo y pauta", tag: "DETECTADO"},
  {label: "Fugas de presupuesto, a tiempo", tag: "RESUELTO"},
  {label: "Cuellos de botella invisibles", tag: "DESTRABADO"},
];

const MOTORES = [
  {
    tag: "MOTOR 1",
    title: "Paid Media",
    sub: "Agente autónomo · multicanal",
    points: ["Meta + Google Shopping", "Performance Max + Merchant Center", "Monitoreo y alertas diarias"],
  },
  {
    tag: "MOTOR 2",
    title: "Email lifecycle",
    sub: "Automatización sobre 13.300 contactos",
    points: ["Bienvenida · 2ª compra", "Recompra · Win-back", "9 flujos segmentados"],
  },
];

// Curva de ventas (aprox. del print) — viewBox 0..900 x 0..240 (y=0 arriba)
const CURVE: [number, number][] = [
  [0, 188], [69, 166], [138, 180], [207, 150], [276, 184], [345, 120],
  [414, 150], [483, 58], [552, 108], [621, 176], [690, 158], [759, 138],
  [828, 184], [900, 196],
];

// =============================================================================
// HELPERS
// =============================================================================
const fmtCLP = (n: number) => "$" + Math.round(n).toLocaleString("es-CL");

const smoothPath = (pts: [number, number][]) => {
  if (pts.length < 2) return "";
  let d = `M ${pts[0][0]} ${pts[0][1]}`;
  for (let i = 0; i < pts.length - 1; i++) {
    const [x0, y0] = pts[i];
    const [x1, y1] = pts[i + 1];
    const cx = (x0 + x1) / 2;
    d += ` C ${cx} ${y0}, ${cx} ${y1}, ${x1} ${y1}`;
  }
  return d;
};

// =============================================================================
// SHARED — fondo cream con acentos suaves + grid sutil
// =============================================================================
const CreamBg: React.FC<{children?: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const x1 = 22 + Math.sin(t * 0.22) * 10;
  const y1 = 20 + Math.cos(t * 0.16) * 8;
  const x2 = 80 + Math.cos(t * 0.2) * 10;
  const y2 = 82 + Math.sin(t * 0.26) * 10;
  const x3 = 88 + Math.sin(t * 0.18) * 10;
  const y3 = 14 + Math.cos(t * 0.23) * 8;
  const x4 = 12 + Math.cos(t * 0.19) * 8;
  const y4 = 88 + Math.sin(t * 0.21) * 8;
  return (
    <AbsoluteFill style={{backgroundColor: C.cream}}>
      <AbsoluteFill
        style={{
          background: `
            radial-gradient(ellipse 55% 45% at ${x1}% ${y1}%, ${C.lime}33 0%, transparent 55%),
            radial-gradient(ellipse 42% 38% at ${x3}% ${y3}%, ${ORANGE}1A 0%, transparent 60%),
            radial-gradient(ellipse 42% 40% at ${x4}% ${y4}%, ${FUCHSIA}18 0%, transparent 62%),
            radial-gradient(ellipse 50% 45% at ${x2}% ${y2}%, ${C.navy}12 0%, transparent 60%)
          `,
        }}
      />
      <AbsoluteFill
        style={{
          backgroundImage: `radial-gradient(${C.navy}0F 1.4px, transparent 1.4px)`,
          backgroundSize: "46px 46px",
          opacity: 0.5,
        }}
      />
      {children}
    </AbsoluteFill>
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
        padding: "10px 22px",
        background: C.navy,
        border: `1.5px solid ${C.navyDeep}`,
        borderRadius: 999,
        boxShadow: "0 8px 24px rgba(15,43,76,0.18)",
      }}
    >
      <span
        style={{
          width: 9,
          height: 9,
          background: SPARK,
          borderRadius: "50%",
          boxShadow: `0 0 ${8 + dotPulse * 10}px ${FUCHSIA}`,
          opacity: dotPulse,
        }}
      />
      <span
        style={{
          color: C.lime,
          fontFamily: CW.fonts.mono,
          fontSize: 18,
          fontWeight: 700,
          letterSpacing: "0.26em",
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
  const l1 = interpolate(frame, [8, 24], [0, 1], {extrapolateRight: "clamp"});
  const l2 = interpolate(frame, [30, 48], [0, 1], {extrapolateRight: "clamp"});
  const underline = interpolate(frame, [46, 68], [0, 300], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  return (
    <AbsoluteFill style={{opacity: exit}}>
      <CreamBg>
        <AbsoluteFill
          style={{justifyContent: "center", alignItems: "center", flexDirection: "column", gap: 30, padding: "0 72px"}}
        >
          <EyebrowChip text="Caso de éxito" delay={4} />
          <div style={{textAlign: "center", maxWidth: 940}}>
            <div
              style={{
                opacity: l1,
                transform: `translateY(${interpolate(l1, [0, 1], [32, 0])}px)`,
                color: C.text,
                fontFamily: CW.fonts.display,
                fontSize: 72,
                fontWeight: 800,
                letterSpacing: "-0.035em",
                lineHeight: 1.06,
              }}
            >
              Un e-commerce con <span style={{color: C.navy, fontWeight: 900}}>ventas estancadas.</span>
            </div>
            <div
              style={{
                opacity: l2,
                transform: `translateY(${interpolate(l2, [0, 1], [32, 0])}px)`,
                marginTop: 26,
                color: C.text,
                fontFamily: CW.fonts.display,
                fontSize: 60,
                fontWeight: 700,
                letterSpacing: "-0.03em",
                lineHeight: 1.08,
              }}
            >
              Un objetivo. <span style={{color: C.navy, fontWeight: 900}}>30 días de acción.</span>
            </div>
          </div>
          <div style={{width: underline, height: 6, background: SPARK, borderRadius: 3, boxShadow: `0 0 18px ${FUCHSIA}55`}} />
        </AbsoluteFill>
      </CreamBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 2 — EL RETO
// =============================================================================
const RetoAct: React.FC = () => {
  const frame = useCurrentFrame();
  const local = RETO_END - HOOK_END;
  const exit = interpolate(frame, [local - 14, local], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const l1 = interpolate(frame, [4, 18], [0, 1], {extrapolateRight: "clamp"});
  const l2 = interpolate(frame, [16, 32], [0, 1], {extrapolateRight: "clamp"});
  const underline = interpolate(frame, [30, 52], [0, 360], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  return (
    <AbsoluteFill style={{opacity: exit}}>
      <CreamBg>
        <AbsoluteFill style={{justifyContent: "center", alignItems: "center", flexDirection: "column", gap: 26, padding: "0 80px"}}>
          <EyebrowChip text="El reto" delay={2} />
          <div style={{textAlign: "center", maxWidth: 900}}>
            <div
              style={{
                opacity: l1,
                transform: `translateY(${interpolate(l1, [0, 1], [24, 0])}px)`,
                color: C.text,
                fontFamily: CW.fonts.display,
                fontSize: 70,
                fontWeight: 800,
                letterSpacing: "-0.035em",
                lineHeight: 1.08,
              }}
            >
              Escalar ventas
            </div>
            <div
              style={{
                opacity: l2,
                transform: `translateY(${interpolate(l2, [0, 1], [24, 0])}px)`,
                color: C.navy,
                fontFamily: CW.fonts.display,
                fontSize: 78,
                fontWeight: 900,
                letterSpacing: "-0.04em",
                lineHeight: 1.06,
                marginTop: 10,
              }}
            >
              sin disparar el costo.
            </div>
          </div>
          <div style={{width: underline, height: 6, background: SPARK, borderRadius: 3, marginTop: 6, boxShadow: `0 0 18px ${FUCHSIA}55`}} />
          <div
            style={{
              color: C.text,
              fontFamily: CW.fonts.display,
              fontSize: 32,
              fontWeight: 500,
              textAlign: "center",
              maxWidth: 760,
              lineHeight: 1.32,
              opacity: interpolate(frame, [50, 68], [0, 0.82], {extrapolateRight: "clamp"}),
            }}
          >
            Más tráfico no basta: hay que convertir y retener.
          </div>
        </AbsoluteFill>
      </CreamBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 3 — EL SISTEMA (dos motores)
// =============================================================================
const MotorCard: React.FC<{m: (typeof MOTORES)[number]; delay: number}> = ({m, delay}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const sp = spring({frame, fps, delay, config: {damping: 16, mass: 0.8}});
  const op = interpolate(frame, [delay, delay + 12], [0, 1], {extrapolateRight: "clamp"});
  const y = interpolate(sp, [0, 1], [50, 0]);
  return (
    <div
      style={{
        opacity: op,
        transform: `translateY(${y}px)`,
        background: C.white,
        border: `1.5px solid ${C.navy}1F`,
        borderRadius: 28,
        padding: "34px 36px",
        boxShadow: "0 18px 50px rgba(15,43,76,0.10)",
        flex: 1,
      }}
    >
      <div style={{display: "flex", alignItems: "center", gap: 14, marginBottom: 18}}>
        <span
          style={{
            padding: "7px 14px",
            background: C.lime,
            borderRadius: 999,
            color: C.navy,
            fontFamily: CW.fonts.mono,
            fontSize: 16,
            fontWeight: 800,
            letterSpacing: "0.1em",
          }}
        >
          {m.tag}
        </span>
      </div>
      <div style={{color: C.navy, fontFamily: CW.fonts.display, fontSize: 52, fontWeight: 900, letterSpacing: "-0.03em", lineHeight: 1}}>
        {m.title}
      </div>
      <div style={{color: C.text, fontFamily: CW.fonts.mono, fontSize: 19, opacity: 0.62, marginTop: 8, letterSpacing: "0.02em"}}>
        {m.sub}
      </div>
      <div style={{height: 1, background: `${C.navy}18`, margin: "22px 0"}} />
      <div style={{display: "flex", flexDirection: "column", gap: 14}}>
        {m.points.map((p, i) => {
          const pd = delay + 10 + i * 5;
          const pop = interpolate(frame, [pd, pd + 10], [0, 1], {extrapolateRight: "clamp"});
          const px = interpolate(frame, [pd, pd + 12], [-16, 0], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
          return (
            <div key={i} style={{display: "flex", alignItems: "center", gap: 14, opacity: pop, transform: `translateX(${px}px)`}}>
              <span style={{width: 11, height: 11, borderRadius: 3, background: C.navy, flexShrink: 0}} />
              <span style={{color: C.text, fontFamily: CW.fonts.display, fontSize: 27, fontWeight: 600, letterSpacing: "-0.01em"}}>
                {p}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
};

const SistemaAct: React.FC = () => {
  const frame = useCurrentFrame();
  const local = SISTEMA_END - RETO_END;
  const exit = interpolate(frame, [local - 14, local], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{opacity: exit}}>
      <CreamBg>
        <AbsoluteFill style={{padding: "0 56px", display: "flex", flexDirection: "column", justifyContent: "center", gap: 30}}>
          <div style={{alignSelf: "center", opacity: interpolate(frame, [0, 10], [0, 1], {extrapolateRight: "clamp"})}}>
            <EyebrowChip text="La solución" />
          </div>
          <div
            style={{
              color: C.text,
              fontFamily: CW.fonts.display,
              fontSize: 56,
              fontWeight: 900,
              letterSpacing: "-0.035em",
              lineHeight: 1.04,
              textAlign: "center",
              opacity: interpolate(frame, [4, 16], [0, 1], {extrapolateRight: "clamp"}),
            }}
          >
            Un sistema de <span style={{color: C.navy}}>dos motores.</span>
          </div>
          <div style={{display: "flex", gap: 24, alignItems: "stretch", marginTop: 4}}>
            <MotorCard m={MOTORES[0]} delay={14} />
            <MotorCard m={MOTORES[1]} delay={26} />
          </div>
          <div
            style={{
              textAlign: "center",
              opacity: interpolate(frame, [60, 78], [0, 0.78], {extrapolateRight: "clamp"}),
              color: C.text,
              fontFamily: CW.fonts.display,
              fontSize: 30,
              fontWeight: 500,
              marginTop: 4,
            }}
          >
            Paid trae al cliente. Email construye su valor.
          </div>
        </AbsoluteFill>
      </CreamBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 3.5 — AGENTES IA (el diferenciador)
// =============================================================================
const AgentesAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const local = AGENTES_END - SISTEMA_END;
  const exit = interpolate(frame, [local - 14, local], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const panelIn = interpolate(frame, [10, 26], [0, 1], {extrapolateRight: "clamp"});
  const panelY = interpolate(frame, [10, 28], [34, 0], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  const scan = (frame % 70) / 70; // barrido que se repite cada ~2.3s
  return (
    <AbsoluteFill style={{opacity: exit}}>
      <CreamBg>
        <AbsoluteFill style={{padding: "0 56px", display: "flex", flexDirection: "column", justifyContent: "center", gap: 28}}>
          <div style={{alignSelf: "center", opacity: interpolate(frame, [0, 10], [0, 1], {extrapolateRight: "clamp"})}}>
            <EyebrowChip text="El diferenciador" />
          </div>
          <div
            style={{
              color: C.text,
              fontFamily: CW.fonts.display,
              fontSize: 54,
              fontWeight: 900,
              letterSpacing: "-0.035em",
              lineHeight: 1.06,
              textAlign: "center",
              opacity: interpolate(frame, [4, 16], [0, 1], {extrapolateRight: "clamp"}),
            }}
          >
            Agentes con <span style={{color: C.navy}}>IA</span> que ven <span style={{color: C.navy}}>lo invisible.</span>
          </div>

          {/* Panel escáner */}
          <div
            style={{
              position: "relative",
              background: C.navy,
              borderRadius: 30,
              padding: "30px 32px",
              boxShadow: "0 24px 60px rgba(15,43,76,0.28)",
              opacity: panelIn,
              transform: `translateY(${panelY}px)`,
              overflow: "hidden",
            }}
          >
            {/* línea de barrido */}
            <div
              style={{
                position: "absolute",
                left: 0,
                right: 0,
                top: `${scan * 100}%`,
                height: 3,
                background: SPARK,
                opacity: 0.45,
                boxShadow: `0 0 18px ${FUCHSIA}`,
              }}
            />
            <div style={{color: C.cream, fontFamily: CW.fonts.mono, fontSize: 16, opacity: 0.55, letterSpacing: "0.18em", marginBottom: 20}}>
              › DIAGNÓSTICO AUTÓNOMO
            </div>
            <div style={{display: "flex", flexDirection: "column", gap: 20}}>
              {AGENT_FINDINGS.map((f, i) => {
                const d = 24 + i * 14;
                const op = interpolate(frame, [d, d + 12], [0, 1], {extrapolateRight: "clamp"});
                const x = interpolate(frame, [d, d + 14], [-20, 0], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
                const chipPop = spring({frame, fps, delay: d + 8, config: {damping: 12, mass: 0.6}});
                return (
                  <div key={i} style={{display: "flex", alignItems: "center", gap: 16, opacity: op, transform: `translateX(${x}px)`}}>
                    <span style={{width: 14, height: 14, borderRadius: 4, background: SPARK, flexShrink: 0, boxShadow: `0 0 12px ${FUCHSIA}88`}} />
                    <span style={{flex: 1, color: C.white, fontFamily: CW.fonts.display, fontSize: 30, fontWeight: 600, letterSpacing: "-0.01em"}}>
                      {f.label}
                    </span>
                    <span
                      style={{
                        transform: `scale(${0.8 + chipPop * 0.2})`,
                        padding: "6px 13px",
                        background: C.lime,
                        borderRadius: 9,
                        color: C.navy,
                        fontFamily: CW.fonts.mono,
                        fontSize: 15,
                        fontWeight: 800,
                        letterSpacing: "0.04em",
                        flexShrink: 0,
                        whiteSpace: "nowrap",
                      }}
                    >
                      ✓ {f.tag}
                    </span>
                  </div>
                );
              })}
            </div>
          </div>

          <div
            style={{
              textAlign: "center",
              color: C.text,
              fontFamily: CW.fonts.display,
              fontSize: 30,
              fontWeight: 500,
              opacity: interpolate(frame, [72, 90], [0, 0.82], {extrapolateRight: "clamp"}),
            }}
          >
            Destrabamos lo que antes era imposible de ver.
          </div>
        </AbsoluteFill>
      </CreamBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 4 — RESULTADOS
// =============================================================================
const SalesChart: React.FC<{progress: number}> = ({progress}) => {
  const line = smoothPath(CURVE);
  const area = `${line} L 900 240 L 0 240 Z`;
  const clipW = 900 * progress;
  return (
    <svg viewBox="0 0 900 240" style={{width: "100%", height: 230, display: "block", overflow: "visible"}}>
      <defs>
        <linearGradient id="caseArea" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor={C.lime} stopOpacity={0.55} />
          <stop offset="100%" stopColor={C.lime} stopOpacity={0} />
        </linearGradient>
        <linearGradient id="caseLine" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stopColor={C.lime} />
          <stop offset="62%" stopColor={C.lime} />
          <stop offset="100%" stopColor={ORANGE} />
        </linearGradient>
        <clipPath id="caseReveal">
          <rect x="0" y="-20" width={clipW} height={280} />
        </clipPath>
      </defs>
      {/* gridlines */}
      {[40, 100, 160].map((y) => (
        <line key={y} x1="0" y1={y} x2="900" y2={y} stroke={`${C.navy}14`} strokeWidth={1.5} />
      ))}
      <g clipPath="url(#caseReveal)">
        <path d={area} fill="url(#caseArea)" />
        <path d={line} fill="none" stroke="url(#caseLine)" strokeWidth={6} strokeLinecap="round" strokeLinejoin="round" />
      </g>
      {/* peak dot — acento cálido */}
      <circle cx={483} cy={58} r={progress > 0.55 ? 26 : 0} fill={FUCHSIA} opacity={0.25} />
      <circle cx={483} cy={58} r={progress > 0.55 ? 11 : 0} fill={C.white} stroke={FUCHSIA} strokeWidth={4} />
    </svg>
  );
};

const StatCard: React.FC<{stat: (typeof STATS)[number]; delay: number}> = ({stat, delay}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const sp = spring({frame, fps, delay, config: {damping: 15, mass: 0.7}});
  const op = interpolate(frame, [delay, delay + 12], [0, 1], {extrapolateRight: "clamp"});
  const deltaNow = Math.round(interpolate(frame, [delay + 6, delay + 30], [0, stat.delta], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  }));
  return (
    <div
      style={{
        opacity: op,
        transform: `scale(${0.92 + sp * 0.08})`,
        background: C.white,
        border: `1.5px solid ${C.navy}1A`,
        borderRadius: 24,
        padding: "26px 22px",
        boxShadow: "0 14px 40px rgba(15,43,76,0.09)",
        flex: 1,
        textAlign: "center",
      }}
    >
      <div style={{color: C.text, fontFamily: CW.fonts.mono, fontSize: 17, opacity: 0.6, letterSpacing: "0.04em", marginBottom: 10}}>
        {stat.label}
      </div>
      <div style={{color: C.navy, fontFamily: CW.fonts.display, fontSize: 46, fontWeight: 900, letterSpacing: "-0.03em", lineHeight: 1}}>
        {stat.value}
      </div>
      <div
        style={{
          marginTop: 14,
          display: "inline-flex",
          alignItems: "center",
          gap: 6,
          padding: "6px 14px",
          background: C.lime,
          borderRadius: 999,
          color: C.navy,
          fontFamily: CW.fonts.mono,
          fontSize: 22,
          fontWeight: 800,
        }}
      >
        ▲ +{deltaNow}%
      </div>
    </div>
  );
};

const ResultsAct: React.FC = () => {
  const frame = useCurrentFrame();
  const local = RESULTS_END - AGENTES_END;
  const exit = interpolate(frame, [local - 14, local], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const chartProg = interpolate(frame, [40, 110], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  const ventasNow = interpolate(frame, [20, 96], [0, VENTAS_TOTAL], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const ventasDelta = Math.round(interpolate(frame, [24, 96], [0, 272], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}));
  return (
    <AbsoluteFill style={{opacity: exit}}>
      <CreamBg>
        <AbsoluteFill style={{padding: "0 52px", display: "flex", flexDirection: "column", justifyContent: "center", gap: 26}}>
          <div style={{alignSelf: "center", opacity: interpolate(frame, [0, 10], [0, 1], {extrapolateRight: "clamp"})}}>
            <EyebrowChip text="Resultados · 30 días" />
          </div>

          {/* HERO — ventas totales + chart */}
          <div
            style={{
              background: C.navy,
              borderRadius: 32,
              padding: "32px 36px 18px",
              boxShadow: "0 24px 60px rgba(15,43,76,0.28)",
              opacity: interpolate(frame, [8, 22], [0, 1], {extrapolateRight: "clamp"}),
              transform: `translateY(${interpolate(frame, [8, 26], [30, 0], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)})}px)`,
            }}
          >
            <div style={{display: "flex", justifyContent: "space-between", alignItems: "flex-start"}}>
              <div>
                <div style={{color: C.cream, fontFamily: CW.fonts.mono, fontSize: 19, opacity: 0.7, letterSpacing: "0.08em", textTransform: "uppercase"}}>
                  Ventas totales
                </div>
                <div style={{color: C.white, fontFamily: CW.fonts.display, fontSize: 74, fontWeight: 900, letterSpacing: "-0.04em", lineHeight: 1.02, marginTop: 6}}>
                  {fmtCLP(ventasNow)}
                </div>
              </div>
              <div
                style={{
                  marginTop: 12,
                  padding: "10px 18px",
                  background: C.lime,
                  borderRadius: 999,
                  color: C.navy,
                  fontFamily: CW.fonts.mono,
                  fontSize: 30,
                  fontWeight: 900,
                  boxShadow: `0 0 30px ${C.lime}66`,
                  whiteSpace: "nowrap",
                }}
              >
                ▲ +{ventasDelta}%
              </div>
            </div>
            <div style={{marginTop: 14}}>
              <SalesChart progress={chartProg} />
            </div>
          </div>

          {/* 3 métricas */}
          <div style={{display: "flex", gap: 18}}>
            {STATS.map((st, i) => (
              <StatCard key={st.label} stat={st} delay={70 + i * 12} />
            ))}
          </div>
        </AbsoluteFill>
      </CreamBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 5 — CTA / BRAND
// =============================================================================
const CtaAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const bgIn = interpolate(frame, [0, 10], [0, 1], {extrapolateRight: "clamp"});
  const markScale = spring({frame, fps, delay: 4, config: {damping: 14, mass: 0.9}});
  const markOp = interpolate(frame, [4, 18], [0, 1], {extrapolateRight: "clamp"});
  const tagOp = interpolate(frame, [20, 36], [0, 1], {extrapolateRight: "clamp"});
  const ctaOp = interpolate(frame, [40, 56], [0, 1], {extrapolateRight: "clamp"});
  const ctaScale = spring({frame, fps, delay: 40, config: {damping: 12, mass: 0.6}});
  const arrow = 1 + Math.sin(frame / 6) * 0.1;
  return (
    <AbsoluteFill style={{opacity: bgIn}}>
      <CreamBg>
        <AbsoluteFill style={{justifyContent: "center", alignItems: "center", flexDirection: "column", gap: 34, padding: "0 70px"}}>
          <div
            style={{
              opacity: markOp,
              transform: `scale(${0.9 + markScale * 0.1})`,
              color: C.navy,
              fontFamily: CW.fonts.display,
              fontSize: 84,
              fontWeight: 900,
              letterSpacing: "-0.045em",
              display: "inline-flex",
              alignItems: "flex-end",
              gap: 10,
            }}
          >
            copywriters
            <span
              style={{
                width: 18,
                height: 18,
                borderRadius: "50%",
                background: SPARK,
                marginBottom: 16,
                boxShadow: `0 0 18px ${FUCHSIA}66`,
              }}
            />
          </div>
          <div
            style={{
              opacity: tagOp,
              transform: `translateY(${interpolate(tagOp, [0, 1], [22, 0])}px)`,
              color: C.text,
              fontFamily: CW.fonts.display,
              fontSize: 50,
              fontWeight: 700,
              letterSpacing: "-0.03em",
              textAlign: "center",
              lineHeight: 1.12,
              maxWidth: 880,
            }}
          >
            Marketing digital que <span style={{color: C.navy}}>mide resultados.</span>
          </div>
          <div
            style={{
              opacity: ctaOp,
              transform: `scale(${0.94 + ctaScale * 0.06})`,
              marginTop: 10,
              padding: "22px 38px",
              background: C.navy,
              borderRadius: 999,
              display: "flex",
              alignItems: "center",
              gap: 16,
              boxShadow: "0 14px 44px rgba(15,43,76,0.3)",
            }}
          >
            <span style={{color: C.cream, fontFamily: CW.fonts.display, fontSize: 32, fontWeight: 800}}>
              ¿Tu marca es la próxima?
            </span>
            <span style={{color: C.lime, fontSize: 34, fontWeight: 900, transform: `scale(${arrow})`}}>→</span>
          </div>
          <div
            style={{
              opacity: interpolate(frame, [58, 74], [0, 1], {extrapolateRight: "clamp"}),
              color: C.text,
              fontFamily: CW.fonts.mono,
              fontSize: 26,
              fontWeight: 700,
              letterSpacing: "0.06em",
              marginTop: 4,
            }}
          >
            copywriters.cl
          </div>
        </AbsoluteFill>
      </CreamBg>
    </AbsoluteFill>
  );
};

// =============================================================================
// LOGO PERSISTENTE — Grupo CopyLab (esquina, visible todo el reel)
// El PNG es blanco con transparencia → invert(1) lo vuelve negro sobre crema.
// =============================================================================
const CopyLabBadge: React.FC = () => {
  const frame = useCurrentFrame();
  const op = interpolate(frame, [6, 22], [0, 0.92], {extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", top: 60, left: 60, opacity: op}}>
      <Img
        src={staticFile("brand/copylab/copylab-white.png")}
        style={{width: 250, height: "auto", filter: "invert(1)"}}
      />
    </div>
  );
};

// =============================================================================
// MAIN
// =============================================================================
export const CasoExitoConsumoReel: React.FC = () => {
  loadDefaultFonts();
  return (
    <AbsoluteFill style={{backgroundColor: C.cream}}>
      <Sequence from={0} durationInFrames={HOOK_END}>
        <HookAct />
      </Sequence>
      <Sequence from={HOOK_END} durationInFrames={RETO_END - HOOK_END}>
        <RetoAct />
      </Sequence>
      <Sequence from={RETO_END} durationInFrames={SISTEMA_END - RETO_END}>
        <SistemaAct />
      </Sequence>
      <Sequence from={SISTEMA_END} durationInFrames={AGENTES_END - SISTEMA_END}>
        <AgentesAct />
      </Sequence>
      <Sequence from={AGENTES_END} durationInFrames={RESULTS_END - AGENTES_END}>
        <ResultsAct />
      </Sequence>
      <Sequence from={RESULTS_END} durationInFrames={CTA_END - RESULTS_END}>
        <CtaAct />
      </Sequence>

      {/* Logo Grupo CopyLab — persistente */}
      <CopyLabBadge />
    </AbsoluteFill>
  );
};
