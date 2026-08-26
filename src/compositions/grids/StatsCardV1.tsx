import React from "react";
import {AbsoluteFill} from "remotion";
import {loadDefaultFonts} from "../../presets/fonts";
import {BRANDS, BrandSlug, getBrandPalette} from "../../brand";

export type Stat = {value: string; label: string; suffix?: string};

export type StatsCardV1Props = {
  brand: BrandSlug;
  eyebrow?: string;
  headlineTop?: string;
  headlineBottom?: string;
  highlight?: string;
  description?: string;
  stats?: Stat[];
  cta?: string;
};

export const StatsCardV1: React.FC<StatsCardV1Props> = ({
  brand,
  eyebrow = "RESULTADOS REALES",
  headlineTop = "Más eficiencia.",
  headlineBottom = "Resultados que crecen.",
  highlight = "crecen.",
  description = "Así lo hemos aplicado con nuestros clientes:",
  stats = [
    {value: "+37%", label: "Mejora en rendimiento"},
    {value: "-45%", label: "Reducción en tiempos"},
    {value: "+28%", label: "Aumento en conversión"},
  ],
  cta = "Hablemos →",
}) => {
  loadDefaultFonts();
  const P = getBrandPalette(brand);
  const B = BRANDS[brand];

  const renderHeadline = (text: string) => {
    if (!highlight || !text.includes(highlight)) {
      return <span style={{color: P.primary}}>{text}</span>;
    }
    const parts = text.split(highlight);
    return (
      <>
        <span style={{color: P.primary}}>{parts[0]}</span>
        <span style={{color: P.accent}}>{highlight}</span>
        <span style={{color: P.primary}}>{parts[1] || ""}</span>
      </>
    );
  };

  return (
    <AbsoluteFill style={{backgroundColor: P.bg, padding: 70, fontFamily: B.fonts.display}}>
      {/* Top accent line */}
      <div
        style={{
          position: "absolute",
          top: 60,
          left: 70,
          right: 70,
          display: "flex",
          alignItems: "center",
          gap: 20,
        }}
      >
        <span
          style={{
            color: P.accent,
            fontFamily: B.fonts.mono,
            fontSize: 18,
            fontWeight: 800,
            letterSpacing: "0.32em",
          }}
        >
          {eyebrow}
        </span>
        <div
          style={{
            flex: 1,
            height: 2,
            background: P.accent,
            opacity: 0.7,
          }}
        />
        <span
          style={{
            color: P.text,
            fontFamily: B.fonts.mono,
            fontSize: 16,
            opacity: 0.6,
          }}
        >
          {B.name.toLowerCase().replace(" ", "")}.cl
        </span>
      </div>

      {/* Headline */}
      <div
        style={{
          marginTop: 130,
          fontSize: 92,
          fontWeight: 900,
          lineHeight: 1.0,
          letterSpacing: "-0.04em",
        }}
      >
        <div>{renderHeadline(headlineTop)}</div>
        {headlineBottom && (
          <div style={{marginTop: 8}}>{renderHeadline(headlineBottom)}</div>
        )}
      </div>

      {description && (
        <div
          style={{
            marginTop: 32,
            color: P.text,
            fontSize: 28,
            fontWeight: 500,
            opacity: 0.8,
            maxWidth: 800,
          }}
        >
          {description}
        </div>
      )}

      {/* Stats row */}
      <div
        style={{
          marginTop: 56,
          display: "flex",
          gap: 22,
        }}
      >
        {stats.slice(0, 3).map((s, i) => (
          <div
            key={i}
            style={{
              flex: 1,
              borderRadius: 24,
              padding: "32px 24px",
              background: P.mode === "dark" ? `${P.accent}10` : `${P.primary}08`,
              border: `1.5px solid ${P.mode === "dark" ? P.accent + "33" : P.primary + "15"}`,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              gap: 16,
            }}
          >
            <div
              style={{
                width: 56,
                height: 56,
                borderRadius: "50%",
                background: P.mode === "dark" ? P.bg : P.primary,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 28,
                color: P.accent,
              }}
            >
              ●
            </div>
            <div
              style={{
                color: P.accent,
                fontSize: 76,
                fontWeight: 900,
                letterSpacing: "-0.04em",
                lineHeight: 1.0,
                textAlign: "center",
              }}
            >
              {s.value}
            </div>
            <div
              style={{
                color: P.text,
                fontSize: 18,
                fontWeight: 500,
                textAlign: "center",
                lineHeight: 1.2,
                opacity: 0.85,
              }}
            >
              {s.label}
            </div>
          </div>
        ))}
      </div>

      {/* CTA */}
      <div
        style={{
          position: "absolute",
          bottom: 70,
          left: 70,
          right: 70,
          padding: "26px 40px",
          background: P.mode === "dark" ? P.primary : P.primary,
          borderRadius: 18,
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <div
          style={{
            color: P.mode === "dark" ? P.bg : P.bg,
            fontFamily: B.fonts.display,
            fontSize: 32,
            fontWeight: 700,
            letterSpacing: "-0.02em",
          }}
        >
          {cta}
        </div>
        <div
          style={{
            color: P.accent,
            fontSize: 38,
            fontWeight: 900,
          }}
        >
          →
        </div>
      </div>
    </AbsoluteFill>
  );
};
