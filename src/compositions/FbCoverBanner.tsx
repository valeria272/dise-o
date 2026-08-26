import React from "react";
import {AbsoluteFill} from "remotion";
import {loadDefaultFonts} from "../presets/fonts";
import {hypeinfluence} from "../brand/hypeinfluence";
import {rocketdesign} from "../brand/rocketdesign";

type Brand = "hype" | "rocket";

export const brands = {hype: hypeinfluence, rocket: rocketdesign};

const HypeCover: React.FC = () => {
  const b = hypeinfluence.colors;
  const f = hypeinfluence.fonts;
  return (
    <AbsoluteFill style={{backgroundColor: b.black, overflow: "hidden"}}>
      {/* Animated mesh-like background */}
      <AbsoluteFill
        style={{
          background: `
            radial-gradient(ellipse 60% 50% at 20% 30%, ${b.pink}33 0%, transparent 55%),
            radial-gradient(ellipse 50% 45% at 80% 70%, ${b.purple}22 0%, transparent 60%),
            ${b.black}
          `,
        }}
      />
      {/* Gradient accent line on top */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          height: 4,
          background: `linear-gradient(90deg, transparent, ${b.pink}, ${b.purple}, transparent)`,
        }}
      />
      {/* Floating particles */}
      {Array.from({length: 30}).map((_, i) => {
        const x = (i * 137.508) % 1640;
        const y = (i * 89.4) % 856;
        const size = 3 + (i % 4) * 2;
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: x,
              top: y,
              width: size,
              height: size,
              borderRadius: "50%",
              background: i % 3 === 0 ? b.pink : b.white,
              opacity: 0.3 + (i % 5) * 0.08,
              boxShadow: `0 0 ${size * 2}px currentColor`,
            }}
          />
        );
      })}

      {/* Content */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          padding: "60px 100px",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
        }}
      >
        {/* Eyebrow */}
        <div
          style={{
            color: b.pink,
            fontFamily: f.mono,
            fontSize: 22,
            fontWeight: 700,
            letterSpacing: "0.35em",
            textTransform: "uppercase",
            marginBottom: 30,
          }}
        >
          ⚡ Influencer Marketing · Chile
        </div>

        {/* Hero text */}
        <div
          style={{
            color: b.white,
            fontFamily: f.display,
            fontSize: 160,
            fontWeight: 900,
            letterSpacing: "-0.04em",
            lineHeight: 0.95,
            textShadow: `0 6px 30px rgba(0,0,0,0.6)`,
          }}
        >
          SOMOS <span style={{color: b.pink, textShadow: `0 0 40px ${b.pink}66`}}>HYPE</span>.
        </div>

        {/* Subtagline */}
        <div
          style={{
            color: b.cream,
            fontFamily: f.display,
            fontSize: 40,
            fontWeight: 500,
            letterSpacing: "-0.01em",
            marginTop: 24,
            opacity: 0.92,
          }}
        >
          Creamos campañas conscientes y reales.
        </div>

        {/* Bottom URL pill */}
        <div
          style={{
            marginTop: 50,
            display: "flex",
            alignItems: "center",
            gap: 16,
            padding: "16px 28px",
            background: `${b.pink}18`,
            border: `2px solid ${b.pink}`,
            borderRadius: 999,
            alignSelf: "flex-start",
            backdropFilter: "blur(10px)",
          }}
        >
          <span
            style={{
              width: 12,
              height: 12,
              background: b.pink,
              borderRadius: "50%",
              boxShadow: `0 0 14px ${b.pink}`,
            }}
          />
          <span
            style={{
              color: b.white,
              fontFamily: f.mono,
              fontSize: 26,
              fontWeight: 700,
              letterSpacing: "0.1em",
            }}
          >
            hypeinfluence.cl
          </span>
        </div>
      </div>

      {/* Side accent */}
      <div
        style={{
          position: "absolute",
          right: 0,
          top: 0,
          bottom: 0,
          width: 6,
          background: `linear-gradient(180deg, ${b.pink} 0%, ${b.purple} 100%)`,
        }}
      />
    </AbsoluteFill>
  );
};

const RocketCover: React.FC = () => {
  const b = rocketdesign.colors;
  const f = rocketdesign.fonts;
  return (
    <AbsoluteFill style={{backgroundColor: b.black, overflow: "hidden"}}>
      {/* Subtle animated bg */}
      <AbsoluteFill
        style={{
          background: `
            radial-gradient(ellipse 55% 45% at 25% 35%, ${b.lime}25 0%, transparent 55%),
            radial-gradient(ellipse 60% 55% at 75% 75%, ${b.lime}15 0%, transparent 65%),
            ${b.dark}
          `,
        }}
      />

      {/* Grid pattern overlay */}
      <svg
        width={1640}
        height={856}
        style={{position: "absolute", inset: 0, opacity: 0.08}}
      >
        <defs>
          <pattern id="grid" width={60} height={60} patternUnits="userSpaceOnUse">
            <path d="M 60 0 L 0 0 0 60" fill="none" stroke={b.lime} strokeWidth={1} />
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid)" />
      </svg>

      {/* Top accent line */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          height: 4,
          background: `linear-gradient(90deg, transparent, ${b.lime}, transparent)`,
        }}
      />

      {/* Content */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          padding: "60px 100px",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
        }}
      >
        {/* Eyebrow */}
        <div
          style={{
            color: b.lime,
            fontFamily: f.mono,
            fontSize: 22,
            fontWeight: 700,
            letterSpacing: "0.35em",
            textTransform: "uppercase",
            marginBottom: 30,
          }}
        >
          ✦ Branding · Diseño Digital
        </div>

        {/* Hero */}
        <div
          style={{
            color: b.cream,
            fontFamily: f.display,
            fontSize: 130,
            fontWeight: 900,
            letterSpacing: "-0.04em",
            lineHeight: 0.95,
            textShadow: "0 6px 30px rgba(0,0,0,0.6)",
          }}
        >
          ROCKET
          <br />
          <span style={{color: b.lime, textShadow: `0 0 40px ${b.lime}66`}}>DESIGN.</span>
        </div>

        {/* Subtagline */}
        <div
          style={{
            color: b.cream,
            fontFamily: f.display,
            fontSize: 36,
            fontWeight: 500,
            letterSpacing: "-0.01em",
            marginTop: 24,
            opacity: 0.85,
            maxWidth: 1100,
          }}
        >
          Branding y diseño digital que <span style={{color: b.lime, fontWeight: 700}}>marcan la diferencia</span>.
        </div>

        {/* Bottom URL */}
        <div
          style={{
            marginTop: 50,
            display: "flex",
            alignItems: "center",
            gap: 16,
            padding: "16px 28px",
            background: `${b.lime}15`,
            border: `2px solid ${b.lime}`,
            borderRadius: 999,
            alignSelf: "flex-start",
            backdropFilter: "blur(10px)",
          }}
        >
          <span
            style={{
              width: 12,
              height: 12,
              background: b.lime,
              borderRadius: "50%",
              boxShadow: `0 0 14px ${b.lime}`,
            }}
          />
          <span
            style={{
              color: b.cream,
              fontFamily: f.mono,
              fontSize: 26,
              fontWeight: 700,
              letterSpacing: "0.1em",
            }}
          >
            rocketdesign.cl
          </span>
        </div>
      </div>

      {/* Side accent */}
      <div
        style={{
          position: "absolute",
          right: 0,
          top: 0,
          bottom: 0,
          width: 6,
          background: `linear-gradient(180deg, ${b.lime} 0%, transparent 100%)`,
        }}
      />
    </AbsoluteFill>
  );
};

export const FbCoverBanner: React.FC<{brand: Brand}> = ({brand}) => {
  loadDefaultFonts();
  return brand === "hype" ? <HypeCover /> : <RocketCover />;
};
