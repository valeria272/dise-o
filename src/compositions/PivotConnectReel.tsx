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

const FPS = 60;
const SOURCE_DURATION_FRAMES = 42 * FPS;

const INTRO_END = 150; // 2.5s
const OUTRO_START = 37 * FPS;
const CALLOUT_START = 21 * FPS;
const CALLOUT_END = 28 * FPS;

const STRIP_TEXTS: Array<{from: number; to: number; text: string}> = [
  {from: INTRO_END, to: 7 * FPS, text: PC.tagline},
  {from: 7 * FPS, to: 14 * FPS, text: "Tu ERP en sincronía total"},
  {from: 14 * FPS, to: CALLOUT_START, text: "Personaliza lo que necesitas"},
  {from: CALLOUT_END, to: OUTRO_START, text: "Sin fricción. En tiempo real."},
];

// =============================================================================
// SHARED: animated brand environment (used inside top/bottom letterbox areas)
// =============================================================================
const AnimatedMesh: React.FC<{intensity?: number}> = ({intensity = 1}) => {
  const frame = useCurrentFrame();
  const t = frame / 60;
  const x1 = 30 + Math.sin(t * 0.25) * 14;
  const y1 = 30 + Math.cos(t * 0.18) * 10;
  const x2 = 75 + Math.cos(t * 0.22) * 12;
  const y2 = 70 + Math.sin(t * 0.3) * 14;
  return (
    <AbsoluteFill
      style={{
        background: `
          radial-gradient(ellipse 60% 50% at ${x1}% ${y1}%, ${PC.colors.teal}${Math.round(intensity * 38).toString(16).padStart(2, "0")} 0%, transparent 55%),
          radial-gradient(ellipse 50% 45% at ${x2}% ${y2}%, ${PC.colors.navy}${Math.round(intensity * 90).toString(16).padStart(2, "0")} 0%, transparent 60%),
          linear-gradient(180deg, ${PC.colors.navyDeep}, ${PC.colors.navy} 50%, ${PC.colors.navyDeep})
        `,
      }}
    />
  );
};

const FloatingParticles: React.FC<{count?: number; area?: "top" | "bottom" | "full"}> = ({
  count = 8,
  area = "full",
}) => {
  const frame = useCurrentFrame();
  const yRange = area === "top" ? [0, 320] : area === "bottom" ? [1500, 1920] : [0, 1920];
  return (
    <>
      {Array.from({length: count}).map((_, i) => {
        const seed = i * 137.508;
        const baseX = (seed % 1080);
        const baseY = yRange[0] + ((seed * 0.7) % (yRange[1] - yRange[0]));
        const speed = 0.3 + ((i % 3) * 0.18);
        const dy = Math.sin((frame / 60) * speed + i) * 22;
        const dx = Math.cos((frame / 60) * (speed * 0.8) + i * 0.7) * 14;
        const size = 6 + (i % 3) * 4;
        const opacity = 0.32 + (i % 5) * 0.08;
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
              background: PC.colors.teal,
              boxShadow: `0 0 ${size * 2}px ${PC.colors.teal}`,
              opacity,
            }}
          />
        );
      })}
    </>
  );
};

// =============================================================================
// SOURCE LAYER: video with Ken Burns + heavy color grade + vignette + atmosphere
// =============================================================================
const SourceLayer: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  // Slow Ken Burns: 1.00 → 1.045 across whole composition
  const zoom = interpolate(frame, [0, durationInFrames], [1.0, 1.045], {extrapolateRight: "clamp"});
  // Drift horizontally a few px to add life
  const driftX = Math.sin(frame / 240) * 6;

  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      {/* Video with Ken Burns + heavy color grade */}
      <AbsoluteFill
        style={{
          transform: `scale(${zoom}) translateX(${driftX}px)`,
          filter: "contrast(1.16) saturate(1.10) brightness(0.99)",
        }}
      >
        <OffthreadVideo src={staticFile("raw/BSALE_original.mp4")} />
      </AbsoluteFill>

      {/* Brand atmosphere overlay — slight teal cast in shadows */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(circle at 50% 50%, transparent 30%, ${PC.colors.navy}28 100%)`,
          mixBlendMode: "multiply",
        }}
      />

      {/* Vignette — gentle corner darkening, preserves face exposure */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse 95% 105% at 50% 50%, transparent 62%, ${PC.colors.navyDeep}70 100%)`,
        }}
      />

      {/* Subtle teal highlight breath on edges */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(circle at 50% 30%, ${PC.colors.teal}10 0%, transparent 40%)`,
          mixBlendMode: "screen",
        }}
      />
    </AbsoluteFill>
  );
};

// =============================================================================
// INTRO — mask-reveal brand identity, full screen 0-2.5s
// =============================================================================
const Intro: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  // Logo mask reveal (clip-path from left to right)
  const logoReveal = interpolate(frame, [10, 40], [0, 100], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const logoOpacity = interpolate(frame, [8, 20], [0, 1], {extrapolateRight: "clamp"});
  const logoScale = spring({frame, fps, delay: 8, config: {damping: 15, mass: 0.9}});

  // Tagline cascade
  const taglineY = interpolate(frame, [50, 80], [40, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const taglineOpacity = interpolate(frame, [50, 75], [0, 1], {extrapolateRight: "clamp"});

  // Underline draw
  const underlineW = interpolate(frame, [70, 110], [0, 280], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const underlineGlow = interpolate(frame, [105, 125], [0, 1], {extrapolateRight: "clamp"});

  // Exit fade
  const exitOpacity = interpolate(
    frame,
    [INTRO_END - 24, INTRO_END],
    [1, 0],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp"}
  );

  return (
    <AbsoluteFill style={{opacity: exitOpacity}}>
      <AnimatedMesh intensity={1.2} />
      <FloatingParticles count={14} area="full" />

      <AbsoluteFill
        style={{
          background:
            "radial-gradient(circle at 50% 40%, rgba(45,212,171,0.18) 0%, rgba(45,212,171,0) 50%)",
        }}
      />

      <AbsoluteFill style={{justifyContent: "center", alignItems: "center", flexDirection: "column", gap: 56}}>
        {/* Logo with horizontal mask reveal */}
        <div
          style={{
            opacity: logoOpacity,
            transform: `scale(${0.85 + logoScale * 0.15})`,
            filter: `drop-shadow(0 10px 50px ${PC.colors.teal}55)`,
            clipPath: `inset(0 ${100 - logoReveal}% 0 0)`,
            WebkitClipPath: `inset(0 ${100 - logoReveal}% 0 0)`,
          }}
        >
          <Img
            src={staticFile("brand/pivotconnect/logo.png")}
            style={{width: 600, height: "auto", filter: "brightness(0) invert(1)"}}
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
              fontSize: 60,
              fontWeight: 600,
              letterSpacing: "-0.025em",
              textAlign: "center",
            }}
          >
            {PC.tagline}
          </div>
          <div
            style={{
              width: underlineW,
              height: 5,
              borderRadius: 3,
              background: PC.colors.teal,
              boxShadow: `0 0 ${20 + underlineGlow * 20}px ${PC.colors.teal}DD`,
            }}
          />
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// =============================================================================
// TOP COVER — animated brand header that hides baked-in source logo
// =============================================================================
const TopCover: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 18], [0, 1], {extrapolateRight: "clamp"});
  const slideY = interpolate(frame, [0, 18], [-20, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const dotPulse = 0.7 + Math.sin(frame / 14) * 0.3;

  return (
    <div
      style={{
        position: "absolute",
        top: 0,
        left: 0,
        right: 0,
        height: 360,
        opacity,
        transform: `translateY(${slideY}px)`,
        pointerEvents: "none",
      }}
    >
      {/* Solid brand band — hard bottom edge for broadcast-chyron look */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: PC.colors.navyDeep,
          backdropFilter: "blur(36px) saturate(150%)",
          WebkitBackdropFilter: "blur(36px) saturate(150%)",
        }}
      >
        <AnimatedMesh intensity={0.45} />
      </div>

      {/* Teal accent line at the bottom edge */}
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          bottom: 0,
          height: 2,
          background: `linear-gradient(90deg, ${PC.colors.teal}00 0%, ${PC.colors.teal} 50%, ${PC.colors.teal}00 100%)`,
          boxShadow: `0 0 14px ${PC.colors.teal}AA`,
        }}
      />

      {/* Soft glow below the edge (subtle) */}
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 360,
          height: 40,
          background: `linear-gradient(180deg, ${PC.colors.teal}18 0%, transparent 100%)`,
          pointerEvents: "none",
        }}
      />

      <FloatingParticles count={5} area="top" />

      {/* Editorial chip */}
      <div
        style={{
          position: "absolute",
          top: 70,
          left: 44,
          right: 44,
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 14,
            padding: "10px 18px",
            background: `${PC.colors.navy}99`,
            border: `1px solid ${PC.colors.teal}55`,
            borderRadius: 999,
            backdropFilter: "blur(12px)",
            WebkitBackdropFilter: "blur(12px)",
          }}
        >
          <span
            style={{
              width: 8,
              height: 8,
              background: PC.colors.teal,
              borderRadius: "50%",
              boxShadow: `0 0 ${10 + dotPulse * 14}px ${PC.colors.teal}`,
              opacity: dotPulse,
            }}
          />
          <span
            style={{
              color: PC.colors.tealSoft,
              fontFamily: PC.fonts.mono,
              fontSize: 16,
              fontWeight: 700,
              letterSpacing: "0.24em",
              textTransform: "uppercase",
            }}
          >
            Caso de éxito
          </span>
          <span style={{color: `${PC.colors.white}55`, fontSize: 16}}>·</span>
          <span
            style={{
              color: PC.colors.white,
              fontFamily: PC.fonts.display,
              fontSize: 17,
              fontWeight: 700,
              letterSpacing: "0.06em",
            }}
          >
            bsale
          </span>
        </div>

        {/* Small brand mark right */}
        <Img
          src={staticFile("brand/pivotconnect/logo.png")}
          style={{
            width: 100,
            height: "auto",
            filter: "brightness(0) invert(1) drop-shadow(0 2px 8px rgba(0,0,0,0.4))",
            opacity: 0.85,
          }}
        />
      </div>
    </div>
  );
};

// =============================================================================
// STRIP BACKDROP — gradient blur that hides original captions
// =============================================================================
const StripBackdrop: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 18], [0, 1], {extrapolateRight: "clamp"});

  return (
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        bottom: 0,
        height: 580,
        opacity,
        pointerEvents: "none",
      }}
    >
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: `linear-gradient(180deg, transparent 0%, ${PC.colors.navyDeep}55 28%, ${PC.colors.navyDeep}E0 60%, ${PC.colors.navyDeep}FA 100%)`,
          backdropFilter: "blur(28px) saturate(140%)",
          WebkitBackdropFilter: "blur(28px) saturate(140%)",
        }}
      />
      <div style={{position: "absolute", inset: 0, opacity: 0.6}}>
        <FloatingParticles count={6} area="bottom" />
      </div>
    </div>
  );
};

// =============================================================================
// KINETIC STRIP — scene-specific text that animates dramatically per scene change
// =============================================================================
const KineticStrip: React.FC = () => {
  const frame = useCurrentFrame();
  const entryY = interpolate(frame, [0, 22], [80, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const opacity = interpolate(frame, [0, 16], [0, 1], {extrapolateRight: "clamp"});

  const absFrame = frame + INTRO_END;
  const active = STRIP_TEXTS.find((s) => absFrame >= s.from && absFrame < s.to);
  if (!active) return null;

  const localT = absFrame - active.from;
  const sceneLen = active.to - active.from;
  const textIn = interpolate(localT, [0, 22], [0, 1], {extrapolateRight: "clamp"});
  const textOut = interpolate(localT, [sceneLen - 18, sceneLen], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const textVis = Math.min(textIn, textOut);

  // Letter-by-letter stagger
  const words = active.text.split(" ");

  return (
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        bottom: 0,
        height: 280,
        transform: `translateY(${entryY}px)`,
        opacity,
        background: `linear-gradient(180deg, ${PC.colors.navyDeep}E6 0%, ${PC.colors.navyDeep} 100%)`,
        backdropFilter: "blur(34px) saturate(150%)",
        WebkitBackdropFilter: "blur(34px) saturate(150%)",
        borderTop: `1.5px solid ${PC.colors.teal}88`,
        boxShadow: `0 -2px 24px ${PC.colors.teal}33, 0 -20px 50px rgba(0,0,0,0.4)`,
        display: "flex",
        alignItems: "center",
        paddingLeft: 44,
        paddingRight: 44,
        gap: 32,
      }}
    >
      {/* Brand mark left with breath */}
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "flex-start",
          gap: 10,
          flexShrink: 0,
        }}
      >
        <Img
          src={staticFile("brand/pivotconnect/logo.png")}
          style={{
            width: 210,
            height: "auto",
            filter: `brightness(0) invert(1) drop-shadow(0 0 ${8 + Math.sin(frame / 22) * 6}px ${PC.colors.teal}77)`,
          }}
        />
        <div
          style={{
            color: PC.colors.teal,
            fontFamily: PC.fonts.mono,
            fontSize: 17,
            fontWeight: 700,
            letterSpacing: "0.22em",
            textTransform: "uppercase",
          }}
        >
          {PC.url}
        </div>
      </div>

      {/* Vertical divider with gradient + glow */}
      <div
        style={{
          width: 2,
          height: 110,
          background: `linear-gradient(180deg, ${PC.colors.teal}00, ${PC.colors.teal}, ${PC.colors.teal}00)`,
          boxShadow: `0 0 12px ${PC.colors.teal}99`,
          flexShrink: 0,
        }}
      />

      {/* Kinetic text */}
      <div
        style={{
          flex: 1,
          display: "flex",
          flexWrap: "wrap",
          gap: "0 14px",
          color: PC.colors.white,
          fontFamily: PC.fonts.display,
          fontSize: 40,
          fontWeight: 700,
          lineHeight: 1.15,
          letterSpacing: "-0.02em",
          opacity: textVis,
        }}
      >
        {words.map((word, i) => {
          const wordStart = i * 4;
          const wordIn = interpolate(localT, [wordStart, wordStart + 18], [0, 1], {
            extrapolateRight: "clamp",
            easing: Easing.out(Easing.cubic),
          });
          const wordY = interpolate(wordIn, [0, 1], [20, 0]);
          return (
            <span
              key={i}
              style={{
                opacity: wordIn,
                transform: `translateY(${wordY}px)`,
                display: "inline-block",
              }}
            >
              {word}
            </span>
          );
        })}
      </div>
    </div>
  );
};

// =============================================================================
// DATA CALLOUT — PivotConnect ⇄ bsale during sync moment
// =============================================================================
const DataCallout: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 16, mass: 0.8}});
  const exit = interpolate(
    frame,
    [CALLOUT_END - CALLOUT_START - 22, CALLOUT_END - CALLOUT_START],
    [1, 0],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp"}
  );
  const opacity = Math.min(enter, exit);
  const scale = 0.7 + enter * 0.3;
  const floatY = Math.sin(frame / 22) * 6;
  const pulse = 1 + Math.sin(frame / 18) * 0.025;

  // Arrow animation between logos
  const arrowShift = Math.sin(frame / 16) * 4;
  const arrowOpacity = 0.7 + Math.sin(frame / 14) * 0.3;

  return (
    <div
      style={{
        position: "absolute",
        left: "50%",
        top: 420,
        transform: `translate(-50%, ${floatY}px) scale(${scale * pulse})`,
        opacity,
        filter: `drop-shadow(0 24px 60px ${PC.colors.teal}44)`,
      }}
    >
      <div
        style={{
          background: `linear-gradient(180deg, ${PC.colors.navyDeep}F0 0%, ${PC.colors.navy}F0 100%)`,
          backdropFilter: "blur(28px) saturate(170%)",
          WebkitBackdropFilter: "blur(28px) saturate(170%)",
          border: `2px solid ${PC.colors.teal}66`,
          borderRadius: 30,
          padding: "32px 44px",
          boxShadow: `0 30px 80px rgba(0,0,0,0.5), inset 0 1px 0 ${PC.colors.teal}33, 0 0 50px ${PC.colors.teal}40`,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 22,
        }}
      >
        <div style={{display: "flex", alignItems: "center", gap: 28}}>
          <Img
            src={staticFile("brand/pivotconnect/logo.png")}
            style={{width: 160, height: "auto", filter: "brightness(0) invert(1)"}}
          />
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 4,
              color: PC.colors.teal,
              fontFamily: PC.fonts.mono,
              fontSize: 42,
              fontWeight: 800,
              transform: `translateX(${arrowShift}px)`,
              opacity: arrowOpacity,
              textShadow: `0 0 16px ${PC.colors.teal}AA`,
            }}
          >
            ⇄
          </div>
          <Img src={staticFile("brand/pivotconnect/bsale-white.png")} style={{width: 160, height: "auto"}} />
        </div>
        <div
          style={{
            color: PC.colors.white,
            fontFamily: PC.fonts.display,
            fontSize: 34,
            fontWeight: 700,
            letterSpacing: "-0.02em",
            textAlign: "center",
            whiteSpace: "nowrap",
          }}
        >
          Sincronización en tiempo real
        </div>
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 12,
            color: PC.colors.tealSoft,
            fontFamily: PC.fonts.mono,
            fontSize: 19,
            fontWeight: 600,
            letterSpacing: "0.18em",
            textTransform: "uppercase",
            padding: "6px 14px",
            background: `${PC.colors.teal}15`,
            borderRadius: 999,
            border: `1px solid ${PC.colors.teal}55`,
          }}
        >
          <span
            style={{
              width: 12,
              height: 12,
              background: PC.colors.teal,
              borderRadius: "50%",
              boxShadow: `0 0 ${12 + Math.sin(frame / 10) * 8}px ${PC.colors.teal}`,
              opacity: 0.7 + Math.sin(frame / 10) * 0.3,
            }}
          />
          LIVE SYNC
        </div>
      </div>
    </div>
  );
};

// =============================================================================
// OUTRO — branded CTA, mask-reveal logo, dramatic stagger
// =============================================================================
const Outro: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const bgOpacity = interpolate(frame, [0, 22], [0, 1], {extrapolateRight: "clamp"});
  const logoReveal = interpolate(frame, [14, 50], [0, 100], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const logoOpacity = interpolate(frame, [14, 26], [0, 1], {extrapolateRight: "clamp"});
  const logoScale = spring({frame, fps, delay: 14, config: {damping: 14, mass: 0.9}});
  const taglineOpacity = interpolate(frame, [44, 70], [0, 1], {extrapolateRight: "clamp"});
  const taglineY = interpolate(frame, [44, 70], [30, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const lineW = interpolate(frame, [72, 100], [0, 260], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const urlOpacity = interpolate(frame, [85, 115], [0, 1], {extrapolateRight: "clamp"});
  const urlY = interpolate(frame, [85, 115], [20, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const ctaOpacity = interpolate(frame, [120, 150], [0, 1], {extrapolateRight: "clamp"});

  return (
    <AbsoluteFill style={{opacity: bgOpacity}}>
      <AnimatedMesh intensity={1.3} />
      <FloatingParticles count={16} area="full" />

      <AbsoluteFill
        style={{
          background:
            "radial-gradient(circle at 50% 60%, rgba(45,212,171,0.18) 0%, rgba(45,212,171,0) 50%)",
        }}
      />

      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          gap: 42,
          paddingTop: 140,
        }}
      >
        {/* Logo mask reveal */}
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
            style={{width: 620, height: "auto", filter: "brightness(0) invert(1)"}}
          />
        </div>

        <div
          style={{
            opacity: taglineOpacity,
            transform: `translateY(${taglineY}px)`,
            color: PC.colors.white,
            fontFamily: PC.fonts.display,
            fontSize: 60,
            fontWeight: 600,
            letterSpacing: "-0.025em",
            textAlign: "center",
            maxWidth: 920,
          }}
        >
          {PC.tagline}
        </div>

        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 18,
            marginTop: 22,
          }}
        >
          <div
            style={{
              width: lineW,
              height: 4,
              background: PC.colors.teal,
              borderRadius: 2,
              boxShadow: `0 0 22px ${PC.colors.teal}DD`,
            }}
          />
          <div
            style={{
              opacity: urlOpacity,
              transform: `translateY(${urlY}px)`,
              color: PC.colors.teal,
              fontFamily: PC.fonts.mono,
              fontSize: 50,
              fontWeight: 800,
              letterSpacing: "0.05em",
              textShadow: `0 0 24px ${PC.colors.teal}55`,
            }}
          >
            {PC.url}
          </div>
        </div>

        <div
          style={{
            opacity: ctaOpacity,
            color: "rgba(255,255,255,0.55)",
            fontFamily: PC.fonts.display,
            fontSize: 22,
            fontWeight: 500,
            letterSpacing: "0.18em",
            marginTop: 18,
            textAlign: "center",
            textTransform: "uppercase",
          }}
        >
          {PC.corpTagline}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// =============================================================================
// MAIN COMPOSITION
// =============================================================================
export const PivotConnectReel: React.FC = () => {
  loadDefaultFonts();

  return (
    <AbsoluteFill style={{backgroundColor: PC.colors.navyDeep}}>
      {/* Source video with Ken Burns + heavy color grade + vignette */}
      <SourceLayer />

      {/* INTRO 0-2.5s */}
      <Sequence from={0} durationInFrames={INTRO_END}>
        <Intro />
      </Sequence>

      {/* MAIN 2.5s-37s */}
      <Sequence from={INTRO_END} durationInFrames={OUTRO_START - INTRO_END}>
        <TopCover />
        <StripBackdrop />
        <KineticStrip />
      </Sequence>

      {/* Data callout during bsale sync (21-28s) */}
      <Sequence from={CALLOUT_START} durationInFrames={CALLOUT_END - CALLOUT_START}>
        <DataCallout />
      </Sequence>

      {/* OUTRO 37-42s */}
      <Sequence from={OUTRO_START} durationInFrames={SOURCE_DURATION_FRAMES - OUTRO_START}>
        <Outro />
      </Sequence>
    </AbsoluteFill>
  );
};
