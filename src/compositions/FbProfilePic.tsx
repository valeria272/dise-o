import React from "react";
import {AbsoluteFill} from "remotion";
import {loadDefaultFonts} from "../presets/fonts";
import {hypeinfluence} from "../brand/hypeinfluence";
import {rocketdesign} from "../brand/rocketdesign";

type Brand = "hype" | "rocket";

const HypeProfile: React.FC = () => {
  const b = hypeinfluence.colors;
  const f = hypeinfluence.fonts;
  return (
    <AbsoluteFill style={{backgroundColor: b.black}}>
      <AbsoluteFill
        style={{
          background: `
            radial-gradient(circle at 30% 30%, ${b.pink}55 0%, transparent 55%),
            radial-gradient(circle at 70% 70%, ${b.purple}30 0%, transparent 60%),
            ${b.black}
          `,
        }}
      />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          gap: 8,
        }}
      >
        <div
          style={{
            fontFamily: f.display,
            color: b.white,
            fontSize: 180,
            fontWeight: 900,
            letterSpacing: "-0.05em",
            textShadow: `0 0 50px ${b.pink}AA`,
            lineHeight: 0.9,
          }}
        >
          H
        </div>
        <div
          style={{
            color: b.pink,
            fontFamily: f.mono,
            fontSize: 26,
            fontWeight: 800,
            letterSpacing: "0.3em",
            textTransform: "uppercase",
          }}
        >
          HYPE
        </div>
      </AbsoluteFill>
      {/* Outer glow ring */}
      <div
        style={{
          position: "absolute",
          inset: 30,
          borderRadius: "50%",
          border: `4px solid ${b.pink}66`,
          boxShadow: `0 0 60px ${b.pink}55, inset 0 0 60px ${b.pink}33`,
        }}
      />
    </AbsoluteFill>
  );
};

const RocketProfile: React.FC = () => {
  const b = rocketdesign.colors;
  const f = rocketdesign.fonts;
  return (
    <AbsoluteFill style={{backgroundColor: b.dark}}>
      <AbsoluteFill
        style={{
          background: `
            radial-gradient(circle at 35% 35%, ${b.lime}40 0%, transparent 55%),
            radial-gradient(circle at 70% 70%, ${b.lime}20 0%, transparent 60%),
            ${b.dark}
          `,
        }}
      />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          gap: 8,
        }}
      >
        <div
          style={{
            fontFamily: f.display,
            color: b.cream,
            fontSize: 180,
            fontWeight: 900,
            letterSpacing: "-0.05em",
            textShadow: `0 0 50px ${b.lime}AA`,
            lineHeight: 0.9,
          }}
        >
          R
        </div>
        <div
          style={{
            color: b.lime,
            fontFamily: f.mono,
            fontSize: 22,
            fontWeight: 800,
            letterSpacing: "0.32em",
            textTransform: "uppercase",
          }}
        >
          ROCKET
        </div>
      </AbsoluteFill>
      <div
        style={{
          position: "absolute",
          inset: 30,
          borderRadius: "50%",
          border: `4px solid ${b.lime}55`,
          boxShadow: `0 0 60px ${b.lime}55, inset 0 0 60px ${b.lime}33`,
        }}
      />
    </AbsoluteFill>
  );
};

export const FbProfilePic: React.FC<{brand: Brand}> = ({brand}) => {
  loadDefaultFonts();
  return brand === "hype" ? <HypeProfile /> : <RocketProfile />;
};
