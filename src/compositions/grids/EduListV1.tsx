import React from "react";
import {AbsoluteFill} from "remotion";
import {loadDefaultFonts} from "../../presets/fonts";
import {BRANDS, BrandSlug, getBrandPalette} from "../../brand";

export type EduListPoint = {
  num?: string;
  title: string;
  body?: string;
};

export type EduListV1Props = {
  brand: BrandSlug;
  eyebrow?: string;
  headline?: string;
  highlight?: string;
  points?: EduListPoint[];
  cta?: string;
};

export const EduListV1: React.FC<EduListV1Props> = ({
  brand,
  eyebrow = "GUÍA RÁPIDA",
  headline = "3 errores que matan tu ROAS en Meta Ads",
  highlight = "matan tu ROAS",
  points = [
    {
      num: "1",
      title: "Públicos demasiado amplios",
      body: "Si tu audiencia no entiende a quién le hablas, vas a quemar plata en clics que no convierten.",
    },
    {
      num: "2",
      title: "Sin test de creatividades",
      body: "Una sola variación por anuncio = no aprendes. Necesitas A/B testing real cada semana.",
    },
    {
      num: "3",
      title: "Ignorar el funnel completo",
      body: "Top-of-funnel sin retargeting bien armado pierde el 80% del potencial de retorno.",
    },
  ],
  cta = "Guarda este post →",
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
    <AbsoluteFill style={{backgroundColor: P.bg, padding: 60, fontFamily: B.fonts.display}}>
      {/* Eyebrow */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 14,
          marginBottom: 22,
        }}
      >
        <span
          style={{
            padding: "6px 14px",
            background: P.accent,
            borderRadius: 999,
            color: P.mode === "light" ? P.primary : P.bg,
            fontFamily: B.fonts.mono,
            fontSize: 14,
            fontWeight: 800,
            letterSpacing: "0.22em",
          }}
        >
          {eyebrow}
        </span>
        <div style={{flex: 1, height: 1.5, background: P.accent, opacity: 0.5}} />
      </div>

      {/* Headline */}
      <div
        style={{
          fontSize: 70,
          fontWeight: 900,
          lineHeight: 1.02,
          letterSpacing: "-0.035em",
          maxWidth: 900,
        }}
      >
        {renderHeadline(headline)}
      </div>

      {/* Points */}
      <div
        style={{
          marginTop: 50,
          display: "flex",
          flexDirection: "column",
          gap: 22,
        }}
      >
        {points.slice(0, 4).map((p, i) => (
          <div
            key={i}
            style={{
              display: "flex",
              gap: 22,
              padding: "22px 24px",
              borderRadius: 20,
              background: P.mode === "dark" ? `${P.accent}10` : `${P.primary}06`,
              border: `1.5px solid ${P.mode === "dark" ? P.accent + "33" : P.primary + "15"}`,
            }}
          >
            {/* Number */}
            <div
              style={{
                width: 70,
                height: 70,
                borderRadius: 16,
                background: P.accent,
                color: P.mode === "light" ? P.primary : P.bg,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 36,
                fontWeight: 900,
                letterSpacing: "-0.04em",
                flexShrink: 0,
              }}
            >
              {p.num || (i + 1).toString()}
            </div>

            {/* Title + body */}
            <div style={{flex: 1, display: "flex", flexDirection: "column", gap: 6}}>
              <div
                style={{
                  color: P.primary,
                  fontSize: 28,
                  fontWeight: 800,
                  letterSpacing: "-0.02em",
                  lineHeight: 1.15,
                }}
              >
                {p.title}
              </div>
              {p.body && (
                <div
                  style={{
                    color: P.text,
                    fontSize: 18,
                    fontWeight: 500,
                    opacity: 0.78,
                    lineHeight: 1.4,
                  }}
                >
                  {p.body}
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* CTA at bottom */}
      <div
        style={{
          position: "absolute",
          bottom: 60,
          left: 60,
          right: 60,
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <div
          style={{
            color: P.text,
            fontFamily: B.fonts.mono,
            fontSize: 16,
            opacity: 0.6,
            letterSpacing: "0.18em",
            textTransform: "uppercase",
          }}
        >
          {B.url}
        </div>
        <div
          style={{
            padding: "16px 24px",
            background: P.accent,
            color: P.mode === "light" ? P.primary : P.bg,
            borderRadius: 999,
            fontSize: 22,
            fontWeight: 800,
            letterSpacing: "-0.01em",
            display: "flex",
            alignItems: "center",
            gap: 10,
          }}
        >
          {cta.replace(" →", "")} <span style={{fontSize: 26}}>→</span>
        </div>
      </div>
    </AbsoluteFill>
  );
};
