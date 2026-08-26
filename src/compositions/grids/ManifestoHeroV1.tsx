import React from "react";
import {AbsoluteFill} from "remotion";
import {loadDefaultFonts} from "../../presets/fonts";
import {BRANDS, BrandSlug, getBrandPalette} from "../../brand";

export type ManifestoHeroV1Props = {
  brand: BrandSlug;
  eyebrow?: string;
  line1?: string;
  line2?: string;
  highlight?: string;
  body?: string;
  features?: string[];
  cta?: string;
};

export const ManifestoHeroV1: React.FC<ManifestoHeroV1Props> = ({
  brand,
  eyebrow = "MANIFIESTO",
  line1 = "Influencers que conectan.",
  line2 = "Resultados que importan.",
  highlight = "Resultados que importan.",
  body = "Diseñamos estrategias a medida para que tu marca conecte con las personas correctas y genere impacto real.",
  features = ["Estrategia personalizada", "Influencers alineados", "Resultados medibles"],
  cta = "Hablemos de tu próxima campaña →",
}) => {
  loadDefaultFonts();
  const P = getBrandPalette(brand);
  const B = BRANDS[brand];

  return (
    <AbsoluteFill style={{backgroundColor: P.bg, fontFamily: B.fonts.display}}>
      {/* Animated mesh-like background for drama */}
      <AbsoluteFill
        style={{
          background: `
            radial-gradient(ellipse 60% 50% at 25% 25%, ${P.accent}28 0%, transparent 55%),
            radial-gradient(ellipse 55% 50% at 75% 70%, ${P.accent}18 0%, transparent 60%)
          `,
        }}
      />

      {/* Subtle particles */}
      {Array.from({length: 24}).map((_, i) => {
        const x = (i * 137.508) % 1080;
        const y = (i * 89.4) % 1080;
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
              background: P.accent,
              opacity: 0.3 + (i % 5) * 0.08,
              boxShadow: `0 0 ${size * 2}px ${P.accent}`,
            }}
          />
        );
      })}

      {/* Content */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          padding: 80,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
        }}
      >
        {/* Eyebrow + brand mark */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            marginBottom: 30,
          }}
        >
          <div style={{display: "flex", alignItems: "center", gap: 12}}>
            <span
              style={{
                width: 10,
                height: 10,
                background: P.accent,
                borderRadius: "50%",
                boxShadow: `0 0 12px ${P.accent}`,
              }}
            />
            <span
              style={{
                color: P.accent,
                fontFamily: B.fonts.mono,
                fontSize: 18,
                fontWeight: 800,
                letterSpacing: "0.32em",
                textTransform: "uppercase",
              }}
            >
              {eyebrow}
            </span>
          </div>
          <div
            style={{
              color: P.text,
              fontFamily: B.fonts.mono,
              fontSize: 14,
              opacity: 0.6,
              letterSpacing: "0.18em",
              textTransform: "uppercase",
            }}
          >
            {B.url}
          </div>
        </div>

        {/* Decorative underline */}
        <div
          style={{
            width: 90,
            height: 5,
            background: P.accent,
            borderRadius: 3,
            marginBottom: 36,
            boxShadow: `0 0 18px ${P.accent}AA`,
          }}
        />

        {/* Hero headlines */}
        <div
          style={{
            fontSize: 110,
            fontWeight: 900,
            lineHeight: 0.95,
            letterSpacing: "-0.045em",
          }}
        >
          <div style={{color: line1 === highlight ? P.accent : P.primary}}>{line1}</div>
          {line2 && (
            <div
              style={{
                color: line2 === highlight ? P.accent : P.primary,
                textShadow: line2 === highlight ? `0 0 40px ${P.accent}66` : "none",
                marginTop: 8,
              }}
            >
              {line2}
            </div>
          )}
        </div>

        {/* Body */}
        {body && (
          <div
            style={{
              marginTop: 36,
              color: P.text,
              fontSize: 28,
              fontWeight: 500,
              opacity: 0.85,
              lineHeight: 1.4,
              maxWidth: 820,
            }}
          >
            {body}
          </div>
        )}

        {/* Features row */}
        {features && features.length > 0 && (
          <div
            style={{
              marginTop: 50,
              display: "flex",
              gap: 22,
            }}
          >
            {features.slice(0, 3).map((f, i) => (
              <div
                key={i}
                style={{
                  flex: 1,
                  padding: "20px 18px",
                  background: `${P.accent}10`,
                  border: `1.5px solid ${P.accent}44`,
                  borderRadius: 16,
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  gap: 10,
                }}
              >
                <div
                  style={{
                    color: P.accent,
                    fontSize: 28,
                    fontWeight: 900,
                  }}
                >
                  {["◎", "◉", "▲"][i] || "●"}
                </div>
                <div
                  style={{
                    color: P.text,
                    fontFamily: B.fonts.mono,
                    fontSize: 15,
                    fontWeight: 700,
                    letterSpacing: "0.12em",
                    textTransform: "uppercase",
                    textAlign: "center",
                    lineHeight: 1.25,
                  }}
                >
                  {f}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* CTA pill at bottom */}
      <div
        style={{
          position: "absolute",
          bottom: 60,
          left: 80,
          right: 80,
          padding: "26px 32px",
          background: "transparent",
          border: `2px solid ${P.accent}`,
          borderRadius: 999,
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          boxShadow: `0 0 30px ${P.accent}33`,
        }}
      >
        <div
          style={{
            color: P.accent,
            fontFamily: B.fonts.display,
            fontSize: 28,
            fontWeight: 800,
            letterSpacing: "0.06em",
            textTransform: "uppercase",
          }}
        >
          {cta.replace(" →", "")}
        </div>
        <div
          style={{
            color: P.accent,
            fontSize: 36,
            fontWeight: 900,
          }}
        >
          →
        </div>
      </div>
    </AbsoluteFill>
  );
};
