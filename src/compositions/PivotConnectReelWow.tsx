import React from "react";
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  OffthreadVideo,
  Sequence,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {loadDefaultFonts} from "../presets/fonts";
import {pivotconnect as PC} from "../brand/pivotconnect";
import {MarketplaceBadge, MARKETPLACES} from "./MarketplaceLogos";

const FPS = 30;
const TOTAL = 40 * FPS; // 1200 — paced reel, MAGIC act tightened

const HOOK_END = 4 * FPS; // 120
const PROBLEM_END = 10 * FPS; // 300
const SOLUTION_END = 15 * FPS; // 450 (was 480)
const MAGIC_END = 22 * FPS; // 660 (was 840 — 7s instead of 12s, snappier orbit)
const PROOF_END = 32 * FPS; // 960 (was 1140)
const CTA_END = TOTAL; // 1200

// =============================================================================
// SHARED PRIMITIVES
// =============================================================================

const NavyBg: React.FC<{children?: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const x1 = 30 + Math.sin(t * 0.25) * 14;
  const y1 = 30 + Math.cos(t * 0.18) * 10;
  const x2 = 70 + Math.cos(t * 0.22) * 12;
  const y2 = 75 + Math.sin(t * 0.3) * 14;
  return (
    <AbsoluteFill style={{backgroundColor: PC.colors.navyDeep}}>
      <AbsoluteFill
        style={{
          background: `
            radial-gradient(ellipse 60% 50% at ${x1}% ${y1}%, ${PC.colors.teal}38 0%, transparent 55%),
            radial-gradient(ellipse 50% 45% at ${x2}% ${y2}%, ${PC.colors.navy}90 0%, transparent 60%),
            linear-gradient(180deg, ${PC.colors.navyDeep}, ${PC.colors.navy} 50%, ${PC.colors.navyDeep})
          `,
        }}
      />
      {children}
    </AbsoluteFill>
  );
};

const Particles: React.FC<{count?: number; color?: string}> = ({
  count = 14,
  color = PC.colors.teal,
}) => {
  const frame = useCurrentFrame();
  return (
    <>
      {Array.from({length: count}).map((_, i) => {
        const seed = i * 137.508;
        const baseX = seed % 1080;
        const baseY = (seed * 0.7) % 1920;
        const speed = 0.3 + (i % 3) * 0.18;
        const dy = Math.sin((frame / FPS) * speed + i) * 30;
        const dx = Math.cos((frame / FPS) * (speed * 0.8) + i * 0.7) * 20;
        const size = 4 + (i % 3) * 4;
        const opacity = 0.35 + (i % 5) * 0.08;
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
              background: color,
              boxShadow: `0 0 ${size * 2}px ${color}`,
              opacity,
            }}
          />
        );
      })}
    </>
  );
};

// =============================================================================
// ACT 1 — HOOK (0-4s)
// "¿Vendes en Shopify... pero administras TODO a mano?"
// =============================================================================

const ChaosScene: React.FC = () => {
  const frame = useCurrentFrame();
  // Floating chaotic UI elements
  const items = [
    {icon: "🛒", delay: 0, x: 150, y: 300},
    {icon: "📊", delay: 6, x: 850, y: 420},
    {icon: "📦", delay: 12, x: 220, y: 720},
    {icon: "💸", delay: 18, x: 760, y: 850},
    {icon: "📋", delay: 24, x: 540, y: 1100},
    {icon: "⏰", delay: 30, x: 180, y: 1280},
    {icon: "❓", delay: 36, x: 800, y: 1340},
  ];
  return (
    <>
      {items.map((it, i) => {
        const opacity = interpolate(frame, [it.delay, it.delay + 12], [0, 0.35], {
          extrapolateRight: "clamp",
        });
        const rot = Math.sin((frame + it.delay) / 12) * 8;
        const float = Math.sin((frame + it.delay) / 18) * 16;
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: it.x,
              top: it.y + float,
              fontSize: 110,
              opacity,
              transform: `rotate(${rot}deg)`,
              filter: "blur(1px) saturate(0.6)",
            }}
          >
            {it.icon}
          </div>
        );
      })}
    </>
  );
};

const HookAct: React.FC = () => {
  const frame = useCurrentFrame();

  // Two halves: "¿Vendes en Shopify..." (0-2s) then "...pero administras TODO a mano?" (2-4s)
  const part1Words = ["¿Vendes", "en", "Shopify…"];
  const part2Words = ["…pero", "administras", "TODO", "a", "mano?"];

  return (
    <NavyBg>
      <Particles count={10} />
      <ChaosScene />

      {/* Bottom red gradient suggesting "danger" / overwhelm */}
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(ellipse at 50% 90%, rgba(255,60,60,0.10) 0%, transparent 50%)",
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
        {/* Part 1 0-1.8s */}
        <div style={{display: "flex", gap: 18, flexWrap: "wrap", justifyContent: "center"}}>
          {part1Words.map((w, i) => {
            const wIn = interpolate(frame, [i * 4, i * 4 + 12], [0, 1], {
              extrapolateRight: "clamp",
              easing: Easing.out(Easing.cubic),
            });
            const wY = interpolate(wIn, [0, 1], [40, 0]);
            const out = interpolate(frame, [55, 70], [1, 0], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
            });
            return (
              <span
                key={i}
                style={{
                  opacity: wIn * out,
                  transform: `translateY(${wY}px)`,
                  display: "inline-block",
                  color: PC.colors.white,
                  fontFamily: PC.fonts.display,
                  fontSize: 90,
                  fontWeight: 800,
                  letterSpacing: "-0.035em",
                  lineHeight: 1.05,
                }}
              >
                {w}
              </span>
            );
          })}
        </div>

        {/* Part 2 2-4s */}
        <div style={{display: "flex", gap: 18, flexWrap: "wrap", justifyContent: "center"}}>
          {part2Words.map((w, i) => {
            const startF = 70 + i * 5;
            const wIn = interpolate(frame, [startF, startF + 12], [0, 1], {
              extrapolateRight: "clamp",
              easing: Easing.out(Easing.cubic),
            });
            const wY = interpolate(wIn, [0, 1], [40, 0]);
            const isHero = w === "TODO";
            return (
              <span
                key={i}
                style={{
                  opacity: wIn,
                  transform: `translateY(${wY}px) ${isHero ? "scale(1.05)" : ""}`,
                  display: "inline-block",
                  color: isHero ? PC.colors.teal : PC.colors.white,
                  fontFamily: PC.fonts.display,
                  fontSize: isHero ? 110 : 90,
                  fontWeight: isHero ? 900 : 800,
                  letterSpacing: "-0.035em",
                  lineHeight: 1.05,
                  textShadow: isHero ? `0 0 24px ${PC.colors.teal}99` : "none",
                }}
              >
                {w}
              </span>
            );
          })}
        </div>
      </AbsoluteFill>
    </NavyBg>
  );
};

// =============================================================================
// ACT 2 — PROBLEM (4-10s)
// B-roll speaker (silent) + jump cuts to bsale login + pain captions
// =============================================================================

const PROBLEM_CAPTIONS: Array<{from: number; to: number; text: string; emoji?: string}> = [
  {from: HOOK_END, to: HOOK_END + 50, text: "Horas copiando datos.", emoji: "⏱"},
  {from: HOOK_END + 55, to: HOOK_END + 110, text: "Stock que no cuadra.", emoji: "📉"},
  {from: HOOK_END + 115, to: PROBLEM_END, text: "Documentos perdidos.", emoji: "📄"},
];

const ProblemAct: React.FC = () => {
  const frame = useCurrentFrame();
  const absFrame = frame + HOOK_END;
  // Cycle B-roll: speaker take (Posible 1 at 5s, 18s, 32s, 42s) intercut with bsale login
  // Each slot 1.5s = 45 frames

  // 4 jump-cut slots in this act (6 sec / 1.5s = 4 slots)
  const sourceSlots = [
    {video: "pivotconnect_raw/Posible 1.MOV", startSec: 4, fadeBg: PC.colors.navyDeep}, // 4-5.5s of source
    {video: "pivotconnect_raw/onbording.MOV", startSec: 1.5, fadeBg: PC.colors.navyDeep}, // bsale login zoom
    {video: "pivotconnect_raw/Posible 1.MOV", startSec: 30, fadeBg: PC.colors.navyDeep},
    {video: "pivotconnect_raw/onboarding 2.MOV", startSec: 1, fadeBg: PC.colors.navyDeep},
  ];

  return (
    <NavyBg>
      {/* B-roll layer with jump cuts */}
      {sourceSlots.map((slot, i) => {
        const slotStart = i * 45;
        const slotEnd = slotStart + 45;
        if (frame < slotStart || frame >= slotEnd) return null;
        const fadeIn = interpolate(frame, [slotStart, slotStart + 4], [0, 1], {
          extrapolateRight: "clamp",
        });
        const fadeOut = interpolate(frame, [slotEnd - 5, slotEnd], [1, 0], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });
        return (
          <AbsoluteFill key={i} style={{opacity: Math.min(fadeIn, fadeOut)}}>
            <AbsoluteFill
              style={{
                filter: "contrast(1.16) saturate(1.10) brightness(0.95)",
              }}
            >
              <OffthreadVideo
                src={staticFile(slot.video)}
                startFrom={Math.floor(slot.startSec * 30)}
                playbackRate={1}
                muted
              />
            </AbsoluteFill>
            {/* Light navy tint — keep B-roll visible, captions readable */}
            <AbsoluteFill style={{backgroundColor: `${PC.colors.navyDeep}40`}} />
            {/* Vignette — only darkens edges, preserves center */}
            <AbsoluteFill
              style={{
                background: `radial-gradient(ellipse 95% 105% at 50% 50%, transparent 55%, ${PC.colors.navyDeep}B0 100%)`,
              }}
            />
            {/* Bottom shadow gradient for caption readability */}
            <AbsoluteFill
              style={{
                background: `linear-gradient(180deg, transparent 35%, ${PC.colors.navyDeep}99 100%)`,
              }}
            />
          </AbsoluteFill>
        );
      })}

      {/* Caption overlays */}
      {PROBLEM_CAPTIONS.map((cap, idx) => {
        if (absFrame < cap.from || absFrame >= cap.to) return null;
        const lt = absFrame - cap.from;
        const dur = cap.to - cap.from;
        const inAnim = interpolate(lt, [0, 14], [0, 1], {extrapolateRight: "clamp"});
        const outAnim = interpolate(lt, [dur - 10, dur], [1, 0], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });
        const opacity = Math.min(inAnim, outAnim);
        const yOff = interpolate(inAnim, [0, 1], [30, 0]);
        const words = cap.text.split(" ");
        return (
          <AbsoluteFill
            key={idx}
            style={{
              justifyContent: "center",
              alignItems: "center",
              flexDirection: "column",
              gap: 32,
              opacity,
              transform: `translateY(${yOff}px)`,
            }}
          >
            {cap.emoji && (
              <div style={{fontSize: 90, filter: "grayscale(0.3)"}}>{cap.emoji}</div>
            )}
            <div
              style={{
                display: "flex",
                gap: 18,
                flexWrap: "wrap",
                justifyContent: "center",
                padding: "0 80px",
              }}
            >
              {words.map((w, wi) => {
                const wIn = interpolate(lt, [wi * 4, wi * 4 + 12], [0, 1], {
                  extrapolateRight: "clamp",
                  easing: Easing.out(Easing.cubic),
                });
                const wY = interpolate(wIn, [0, 1], [18, 0]);
                return (
                  <span
                    key={wi}
                    style={{
                      opacity: wIn,
                      transform: `translateY(${wY}px)`,
                      display: "inline-block",
                      color: PC.colors.white,
                      fontFamily: PC.fonts.display,
                      fontSize: 84,
                      fontWeight: 800,
                      letterSpacing: "-0.03em",
                      lineHeight: 1.05,
                      textShadow: "0 4px 20px rgba(0,0,0,0.6)",
                    }}
                  >
                    {w}
                  </span>
                );
              })}
            </div>
          </AbsoluteFill>
        );
      })}
    </NavyBg>
  );
};

// =============================================================================
// ACT 3 — SOLUTION (10-16s)
// Mask reveal logo + tagline + cut to UI dashboard
// =============================================================================

const SolutionAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  // First 3s: branded reveal (logo + tagline)
  // Last 3s: cut to UI dashboard with overlay

  const isReveal = frame < 90;

  if (isReveal) {
    const logoReveal = interpolate(frame, [8, 36], [0, 100], {
      extrapolateRight: "clamp",
      easing: Easing.out(Easing.cubic),
    });
    const logoOpacity = interpolate(frame, [6, 20], [0, 1], {extrapolateRight: "clamp"});
    const logoScale = spring({frame, fps, delay: 6, config: {damping: 14, mass: 0.9}});
    const taglineOpacity = interpolate(frame, [40, 60], [0, 1], {extrapolateRight: "clamp"});
    const taglineY = interpolate(frame, [40, 60], [30, 0], {
      extrapolateRight: "clamp",
      easing: Easing.out(Easing.cubic),
    });
    const underlineW = interpolate(frame, [60, 84], [0, 320], {
      extrapolateRight: "clamp",
      easing: Easing.out(Easing.cubic),
    });
    const exitOpacity = interpolate(frame, [78, 90], [1, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });

    return (
      <NavyBg>
        <Particles count={16} />
        <AbsoluteFill
          style={{
            background:
              "radial-gradient(circle at 50% 45%, rgba(45,212,171,0.25) 0%, rgba(45,212,171,0) 50%)",
            opacity: exitOpacity,
          }}
        />
        <AbsoluteFill
          style={{
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column",
            gap: 50,
            opacity: exitOpacity,
          }}
        >
          <div
            style={{
              opacity: logoOpacity,
              transform: `scale(${0.85 + logoScale * 0.15})`,
              filter: `drop-shadow(0 12px 50px ${PC.colors.teal}66)`,
              clipPath: `inset(0 ${100 - logoReveal}% 0 0)`,
              WebkitClipPath: `inset(0 ${100 - logoReveal}% 0 0)`,
            }}
          >
            <Img
              src={staticFile("brand/pivotconnect/logo.png")}
              style={{width: 640, height: "auto", filter: "brightness(0) invert(1)"}}
            />
          </div>

          <div
            style={{
              opacity: taglineOpacity,
              transform: `translateY(${taglineY}px)`,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              gap: 26,
            }}
          >
            <div
              style={{
                color: PC.colors.white,
                fontFamily: PC.fonts.display,
                fontSize: 64,
                fontWeight: 700,
                letterSpacing: "-0.025em",
                textAlign: "center",
                maxWidth: 900,
                lineHeight: 1.1,
              }}
            >
              Tu venta en{" "}
              <span style={{color: PC.colors.teal, textShadow: `0 0 24px ${PC.colors.teal}66`}}>
                Piloto Automático
              </span>
            </div>
            <div
              style={{
                width: underlineW,
                height: 5,
                borderRadius: 3,
                background: PC.colors.teal,
                boxShadow: `0 0 24px ${PC.colors.teal}DD`,
              }}
            />
          </div>
        </AbsoluteFill>
      </NavyBg>
    );
  }

  // Frames 90-180: cut to dashboard with overlay
  const lt = frame - 90;
  const intro = interpolate(lt, [0, 12], [0, 1], {extrapolateRight: "clamp"});
  const exitOpacity = interpolate(lt, [70, 90], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{opacity: exitOpacity}}>
      <AbsoluteFill style={{filter: "contrast(1.12) saturate(1.10) brightness(1.00)"}}>
        <OffthreadVideo
          src={staticFile("pivotconnect_raw/onboarding 2.MOV")}
          startFrom={0}
          muted
        />
      </AbsoluteFill>
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse 90% 100% at 50% 50%, transparent 55%, ${PC.colors.navyDeep}AA 100%)`,
        }}
      />

      {/* Editorial chip top */}
      <div
        style={{
          position: "absolute",
          top: 80,
          left: "50%",
          transform: `translateX(-50%) translateY(${(1 - intro) * -20}px)`,
          opacity: intro,
          padding: "12px 22px",
          background: `${PC.colors.navy}AA`,
          backdropFilter: "blur(16px)",
          WebkitBackdropFilter: "blur(16px)",
          border: `1px solid ${PC.colors.teal}66`,
          borderRadius: 999,
          display: "flex",
          alignItems: "center",
          gap: 12,
        }}
      >
        <span
          style={{
            width: 10,
            height: 10,
            background: PC.colors.teal,
            borderRadius: "50%",
            boxShadow: `0 0 12px ${PC.colors.teal}`,
          }}
        />
        <span
          style={{
            color: PC.colors.tealSoft,
            fontFamily: PC.fonts.mono,
            fontSize: 18,
            fontWeight: 700,
            letterSpacing: "0.2em",
            textTransform: "uppercase",
          }}
        >
          Dashboard real
        </span>
      </div>

      {/* Bottom caption */}
      <div
        style={{
          position: "absolute",
          bottom: 220,
          left: 0,
          right: 0,
          textAlign: "center",
          opacity: intro,
        }}
      >
        <div
          style={{
            color: PC.colors.white,
            fontFamily: PC.fonts.display,
            fontSize: 60,
            fontWeight: 800,
            letterSpacing: "-0.025em",
            textShadow: "0 4px 20px rgba(0,0,0,0.7)",
            lineHeight: 1.1,
            padding: "0 80px",
          }}
        >
          Una sola pantalla.<br />
          <span style={{color: PC.colors.teal}}>Todo bajo control.</span>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// =============================================================================
// ACT 4 — MAGIC MOMENT (16-28s) ⭐
// bsale center + 5 marketplaces orbiting + sync animation
// =============================================================================

const MagicAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const CENTER_X = 540;
  const CENTER_Y = 880;
  const ORBIT_R = 280;

  // bsale center entrance
  const bsaleScale = spring({frame, fps, delay: 4, config: {damping: 12, mass: 0.7}});
  const bsaleOpacity = interpolate(frame, [4, 18], [0, 1], {extrapolateRight: "clamp"});

  // Title in
  const titleOpacity = interpolate(frame, [0, 20], [0, 1], {extrapolateRight: "clamp"});
  const titleY = interpolate(frame, [0, 20], [-20, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  return (
    <NavyBg>
      <Particles count={20} />

      {/* Title */}
      <div
        style={{
          position: "absolute",
          top: 180,
          left: 0,
          right: 0,
          textAlign: "center",
          opacity: titleOpacity,
          transform: `translateY(${titleY}px)`,
        }}
      >
        <div
          style={{
            color: PC.colors.white,
            fontFamily: PC.fonts.display,
            fontSize: 76,
            fontWeight: 900,
            letterSpacing: "-0.035em",
            lineHeight: 1.0,
          }}
        >
          <span style={{color: PC.colors.teal}}>1 ERP</span>
          <span style={{opacity: 0.7, fontWeight: 600, padding: "0 18px"}}>·</span>
          <span>5+ canales</span>
        </div>
        <div
          style={{
            color: PC.colors.tealSoft,
            fontFamily: PC.fonts.mono,
            fontSize: 22,
            fontWeight: 600,
            letterSpacing: "0.18em",
            textTransform: "uppercase",
            marginTop: 14,
          }}
        >
          Sincronización en tiempo real
        </div>
      </div>

      {/* Orbit lines (animated draw + pulse) */}
      <svg
        width={1080}
        height={1920}
        style={{position: "absolute", inset: 0}}
      >
        {MARKETPLACES.map((mp, i) => {
          const angle = (i / MARKETPLACES.length) * Math.PI * 2 - Math.PI / 2;
          const targetX = CENTER_X + Math.cos(angle) * ORBIT_R;
          const targetY = CENTER_Y + Math.sin(angle) * ORBIT_R;
          const drawDelay = 26 + i * 6;
          const drawProgress = interpolate(frame, [drawDelay, drawDelay + 24], [0, 1], {
            extrapolateRight: "clamp",
            easing: Easing.out(Easing.cubic),
          });
          const endX = CENTER_X + (targetX - CENTER_X) * drawProgress;
          const endY = CENTER_Y + (targetY - CENTER_Y) * drawProgress;
          const lineOpacity = interpolate(frame, [drawDelay, drawDelay + 12], [0, 0.8], {
            extrapolateRight: "clamp",
          });
          return (
            <line
              key={i}
              x1={CENTER_X}
              y1={CENTER_Y}
              x2={endX}
              y2={endY}
              stroke={PC.colors.teal}
              strokeWidth={2.5}
              strokeDasharray="8 6"
              opacity={lineOpacity}
              style={{filter: `drop-shadow(0 0 6px ${PC.colors.teal})`}}
            />
          );
        })}
      </svg>

      {/* Marketplace badges */}
      {MARKETPLACES.map((mp, i) => {
        const angle = (i / MARKETPLACES.length) * Math.PI * 2 - Math.PI / 2;
        const targetX = CENTER_X + Math.cos(angle) * ORBIT_R;
        const targetY = CENTER_Y + Math.sin(angle) * ORBIT_R;
        const enterDelay = 36 + i * 5;
        const enterSpring = spring({
          frame: Math.max(0, frame - enterDelay),
          fps,
          config: {damping: 11, mass: 0.7},
        });
        const opacity = interpolate(frame, [enterDelay, enterDelay + 14], [0, 1], {
          extrapolateRight: "clamp",
        });
        // Subtle orbital wobble
        const wobble = Math.sin((frame + i * 12) / 18) * 4;
        const scale = 0.4 + enterSpring * 0.6;
        return (
          <div
            key={mp}
            style={{
              position: "absolute",
              left: targetX - 55 + wobble,
              top: targetY - 55,
              opacity,
              transform: `scale(${scale})`,
            }}
          >
            <MarketplaceBadge marketplace={mp} size={110} glow />
          </div>
        );
      })}

      {/* Animated data pulses traveling along lines */}
      {MARKETPLACES.map((mp, i) => {
        const angle = (i / MARKETPLACES.length) * Math.PI * 2 - Math.PI / 2;
        const targetX = CENTER_X + Math.cos(angle) * ORBIT_R;
        const targetY = CENTER_Y + Math.sin(angle) * ORBIT_R;
        const pulseStart = 70 + i * 8;
        if (frame < pulseStart) return null;
        const lt = (frame - pulseStart) % 50;
        const pulseT = lt / 50;
        const px = CENTER_X + (targetX - CENTER_X) * pulseT;
        const py = CENTER_Y + (targetY - CENTER_Y) * pulseT;
        const pulseOpacity = interpolate(pulseT, [0, 0.5, 1], [1, 1, 0]);
        return (
          <div
            key={`p-${i}`}
            style={{
              position: "absolute",
              left: px - 7,
              top: py - 7,
              width: 14,
              height: 14,
              borderRadius: "50%",
              background: PC.colors.teal,
              boxShadow: `0 0 18px ${PC.colors.teal}, 0 0 36px ${PC.colors.teal}AA`,
              opacity: pulseOpacity,
            }}
          />
        );
      })}

      {/* bsale logo at center */}
      <div
        style={{
          position: "absolute",
          left: CENTER_X - 130,
          top: CENTER_Y - 60,
          width: 260,
          height: 120,
          opacity: bsaleOpacity,
          transform: `scale(${0.6 + bsaleScale * 0.4})`,
          background: PC.colors.white,
          borderRadius: 28,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          boxShadow: `0 0 60px ${PC.colors.teal}55, 0 16px 40px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.5)`,
          border: `2px solid ${PC.colors.teal}66`,
        }}
      >
        <Img
          src={staticFile("brand/pivotconnect/bsale-orange.png")}
          style={{width: 200, height: "auto"}}
        />
      </div>

      {/* Live tag */}
      <div
        style={{
          position: "absolute",
          bottom: 280,
          left: "50%",
          transform: "translateX(-50%)",
          opacity: titleOpacity,
          display: "flex",
          alignItems: "center",
          gap: 12,
          padding: "10px 22px",
          background: `${PC.colors.teal}22`,
          border: `1.5px solid ${PC.colors.teal}`,
          borderRadius: 999,
        }}
      >
        <span
          style={{
            width: 12,
            height: 12,
            borderRadius: "50%",
            background: PC.colors.teal,
            boxShadow: `0 0 ${12 + Math.sin(frame / 6) * 8}px ${PC.colors.teal}`,
          }}
        />
        <span
          style={{
            color: PC.colors.tealSoft,
            fontFamily: PC.fonts.mono,
            fontSize: 18,
            fontWeight: 700,
            letterSpacing: "0.22em",
            textTransform: "uppercase",
          }}
        >
          LIVE SYNC
        </span>
      </div>
    </NavyBg>
  );
};

// =============================================================================
// ACT 5 — PROOF (28-38s)
// 3 stats kinetic with screen recording behind
// =============================================================================

const STATS: Array<{
  number: number;
  suffix?: string;
  label: string;
  bg: string;
  startSec: number;
}> = [
  {number: 5, suffix: "MIN", label: "implementación", bg: "pivotconnect_raw/onbording.MOV", startSec: 1},
  {number: 60, suffix: "DÍAS", label: "de prueba gratis", bg: "pivotconnect_raw/EDICIÓN BSALE.mp4", startSec: 1},
  {number: 0, suffix: "CÓDIGO", label: "Cero programación", bg: "pivotconnect_raw/onboarding 2.MOV", startSec: 0},
];

const ProofAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const SLOT = 100; // ~3.3s each

  return (
    <NavyBg>
      {STATS.map((stat, idx) => {
        const slotStart = idx * SLOT;
        const slotEnd = slotStart + SLOT;
        if (frame < slotStart || frame >= slotEnd) return null;
        const lt = frame - slotStart;
        const inOpacity = interpolate(lt, [0, 18], [0, 1], {extrapolateRight: "clamp"});
        const outOpacity = interpolate(lt, [SLOT - 14, SLOT], [1, 0], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });
        const opacity = Math.min(inOpacity, outOpacity);

        // Number counts up from 0 to target
        const numProgress = interpolate(lt, [10, 40], [0, 1], {
          extrapolateRight: "clamp",
          easing: Easing.out(Easing.cubic),
        });
        const displayNum = Math.round(stat.number * numProgress);
        const numScale = spring({
          frame: Math.max(0, lt - 35),
          fps,
          config: {damping: 12, mass: 0.6},
        });

        const labelOpacity = interpolate(lt, [40, 60], [0, 1], {extrapolateRight: "clamp"});
        const labelY = interpolate(labelOpacity, [0, 1], [20, 0]);

        return (
          <AbsoluteFill key={idx} style={{opacity}}>
            {/* Background video */}
            <AbsoluteFill
              style={{
                filter: "contrast(1.15) saturate(1.05) brightness(0.6) blur(4px)",
              }}
            >
              <OffthreadVideo
                src={staticFile(stat.bg)}
                startFrom={Math.floor(stat.startSec * 30)}
                muted
              />
            </AbsoluteFill>
            <AbsoluteFill style={{backgroundColor: `${PC.colors.navyDeep}B0`}} />
            <AbsoluteFill
              style={{
                background: `radial-gradient(ellipse 85% 95% at 50% 50%, transparent 35%, ${PC.colors.navyDeep}F0 100%)`,
              }}
            />

            {/* Stat content */}
            <AbsoluteFill
              style={{
                justifyContent: "center",
                alignItems: "center",
                flexDirection: "column",
                gap: 24,
              }}
            >
              <div
                style={{
                  display: "flex",
                  alignItems: "flex-end",
                  gap: 18,
                  transform: `scale(${0.9 + numScale * 0.1})`,
                }}
              >
                <div
                  style={{
                    color: PC.colors.teal,
                    fontFamily: PC.fonts.display,
                    fontSize: 280,
                    fontWeight: 900,
                    letterSpacing: "-0.06em",
                    lineHeight: 0.9,
                    textShadow: `0 0 40px ${PC.colors.teal}55, 0 12px 30px rgba(0,0,0,0.4)`,
                  }}
                >
                  {displayNum}
                </div>
                {stat.suffix && (
                  <div
                    style={{
                      color: PC.colors.white,
                      fontFamily: PC.fonts.display,
                      fontSize: 64,
                      fontWeight: 800,
                      letterSpacing: "-0.02em",
                      marginBottom: 30,
                    }}
                  >
                    {stat.suffix}
                  </div>
                )}
              </div>

              <div
                style={{
                  width: 280,
                  height: 4,
                  background: PC.colors.teal,
                  borderRadius: 2,
                  boxShadow: `0 0 14px ${PC.colors.teal}99`,
                  opacity: labelOpacity,
                }}
              />

              <div
                style={{
                  color: PC.colors.white,
                  fontFamily: PC.fonts.display,
                  fontSize: 46,
                  fontWeight: 700,
                  letterSpacing: "-0.02em",
                  textAlign: "center",
                  opacity: labelOpacity,
                  transform: `translateY(${labelY}px)`,
                }}
              >
                {stat.label}
              </div>
            </AbsoluteFill>
          </AbsoluteFill>
        );
      })}

      {/* Slot indicator at top */}
      <div
        style={{
          position: "absolute",
          top: 100,
          left: "50%",
          transform: "translateX(-50%)",
          display: "flex",
          gap: 10,
        }}
      >
        {STATS.map((_, i) => {
          const isActive = Math.floor(frame / SLOT) === i;
          return (
            <div
              key={i}
              style={{
                width: isActive ? 40 : 12,
                height: 6,
                borderRadius: 3,
                background: isActive ? PC.colors.teal : `${PC.colors.white}44`,
                boxShadow: isActive ? `0 0 10px ${PC.colors.teal}` : "none",
                transition: "width 0.3s",
              }}
            />
          );
        })}
      </div>
    </NavyBg>
  );
};

// =============================================================================
// ACT 6 — CTA (38-45s)
// "Haz click en el link, y activa tu demo" + pivottech.cl + arrow
// =============================================================================

const CTAAct: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const bgOpacity = interpolate(frame, [0, 16], [0, 1], {extrapolateRight: "clamp"});

  // Logo reveal
  const logoReveal = interpolate(frame, [8, 38], [0, 100], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const logoOpacity = interpolate(frame, [8, 22], [0, 1], {extrapolateRight: "clamp"});
  const logoScale = spring({frame, fps, delay: 8, config: {damping: 14, mass: 0.9}});

  // Headline
  const headlineWords = ["Activa", "tu", "demo"];

  // URL
  const urlOpacity = interpolate(frame, [80, 100], [0, 1], {extrapolateRight: "clamp"});
  const urlScale = spring({frame, fps, delay: 80, config: {damping: 12, mass: 0.6}});

  // Subline
  const sublineOpacity = interpolate(frame, [100, 120], [0, 1], {extrapolateRight: "clamp"});

  // Arrow pulse
  const arrowPulse = 1 + Math.sin(frame / 6) * 0.08;

  return (
    <AbsoluteFill style={{opacity: bgOpacity}}>
      <NavyBg>
        <Particles count={22} />
        <AbsoluteFill
          style={{
            background:
              "radial-gradient(circle at 50% 50%, rgba(45,212,171,0.22) 0%, rgba(45,212,171,0) 50%)",
          }}
        />
      </NavyBg>

      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          gap: 40,
          padding: "0 60px",
        }}
      >
        {/* Logo */}
        <div
          style={{
            opacity: logoOpacity,
            transform: `scale(${0.9 + logoScale * 0.1})`,
            filter: `drop-shadow(0 12px 50px ${PC.colors.teal}55)`,
            clipPath: `inset(0 ${100 - logoReveal}% 0 0)`,
            WebkitClipPath: `inset(0 ${100 - logoReveal}% 0 0)`,
          }}
        >
          <Img
            src={staticFile("brand/pivotconnect/logo.png")}
            style={{width: 520, height: "auto", filter: "brightness(0) invert(1)"}}
          />
        </div>

        {/* Headline */}
        <div style={{display: "flex", gap: 22}}>
          {headlineWords.map((w, i) => {
            const start = 38 + i * 5;
            const wIn = interpolate(frame, [start, start + 14], [0, 1], {
              extrapolateRight: "clamp",
              easing: Easing.out(Easing.cubic),
            });
            const wY = interpolate(wIn, [0, 1], [30, 0]);
            return (
              <span
                key={i}
                style={{
                  opacity: wIn,
                  transform: `translateY(${wY}px)`,
                  display: "inline-block",
                  color: PC.colors.white,
                  fontFamily: PC.fonts.display,
                  fontSize: 96,
                  fontWeight: 900,
                  letterSpacing: "-0.035em",
                  lineHeight: 1.0,
                  textShadow: "0 4px 24px rgba(0,0,0,0.4)",
                }}
              >
                {w}
              </span>
            );
          })}
        </div>

        {/* URL */}
        <div
          style={{
            opacity: urlOpacity,
            transform: `scale(${0.9 + urlScale * 0.1})`,
            marginTop: 24,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 18,
          }}
        >
          <div
            style={{
              width: 200,
              height: 3,
              background: PC.colors.teal,
              borderRadius: 2,
              boxShadow: `0 0 18px ${PC.colors.teal}DD`,
            }}
          />
          <div
            style={{
              color: PC.colors.teal,
              fontFamily: PC.fonts.mono,
              fontSize: 56,
              fontWeight: 800,
              letterSpacing: "0.05em",
              textShadow: `0 0 28px ${PC.colors.teal}66`,
            }}
          >
            pivottech.cl
          </div>
        </div>

        {/* Subline + arrow */}
        <div
          style={{
            opacity: sublineOpacity,
            display: "flex",
            alignItems: "center",
            gap: 18,
            marginTop: 12,
            padding: "14px 26px",
            background: `${PC.colors.navy}66`,
            backdropFilter: "blur(14px)",
            WebkitBackdropFilter: "blur(14px)",
            border: `1.5px solid ${PC.colors.teal}55`,
            borderRadius: 999,
          }}
        >
          <span
            style={{
              fontSize: 32,
              transform: `scale(${arrowPulse})`,
              color: PC.colors.teal,
            }}
          >
            →
          </span>
          <span
            style={{
              color: PC.colors.white,
              fontFamily: PC.fonts.display,
              fontSize: 30,
              fontWeight: 700,
              letterSpacing: "-0.01em",
            }}
          >
            Haz click en el link en la bio
          </span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// =============================================================================
// MAIN COMPOSITION
// =============================================================================
export const PivotConnectReelWow: React.FC = () => {
  loadDefaultFonts();

  return (
    <AbsoluteFill style={{backgroundColor: PC.colors.navyDeep}}>
      {/* Silent: music will be added by user when uploading to IG (native audio library) */}

      <Sequence from={0} durationInFrames={HOOK_END}>
        <HookAct />
      </Sequence>

      <Sequence from={HOOK_END} durationInFrames={PROBLEM_END - HOOK_END}>
        <ProblemAct />
      </Sequence>

      <Sequence from={PROBLEM_END} durationInFrames={SOLUTION_END - PROBLEM_END}>
        <SolutionAct />
      </Sequence>

      <Sequence from={SOLUTION_END} durationInFrames={MAGIC_END - SOLUTION_END}>
        <MagicAct />
      </Sequence>

      <Sequence from={MAGIC_END} durationInFrames={PROOF_END - MAGIC_END}>
        <ProofAct />
      </Sequence>

      <Sequence from={PROOF_END} durationInFrames={CTA_END - PROOF_END}>
        <CTAAct />
      </Sequence>
    </AbsoluteFill>
  );
};
