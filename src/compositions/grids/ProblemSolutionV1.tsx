import React from "react";
import {AbsoluteFill} from "remotion";
import {loadDefaultFonts} from "../../presets/fonts";
import {BRANDS, BrandSlug, getBrandPalette} from "../../brand";

export type ProblemSolutionV1Props = {
  brand: BrandSlug;
  eyebrow?: string;
  painHeadline?: string;
  painItalic?: string;
  painBody?: string;
  solutionLabel?: string;
  solutionTitle?: string;
  solutionBullets?: string[];
  price?: string;
  priceCurrency?: string;
  priceOriginal?: string;
  cta?: string;
};

export const ProblemSolutionV1: React.FC<ProblemSolutionV1Props> = ({
  brand,
  eyebrow = "SERVICIO PARA EMPRESAS",
  painHeadline = "¿Estás pagando por marketing digital",
  painItalic = "sin saber si realmente funciona?",
  painBody = "La mayoría paga todos los meses por campañas que no puede medir, integraciones que no funcionan y datos que no dicen la verdad.",
  solutionLabel = "LA SOLUCIÓN",
  solutionTitle = "Asesoría Digital",
  solutionBullets = [
    "Revisamos todo tu ecosistema",
    "Detectamos fugas y errores",
    "Te entregamos un plan claro",
  ],
  price = "$590.000",
  priceCurrency = "CLP + IVA",
  priceOriginal = "$890.000",
  cta = "Quiero mi Asesoría →",
}) => {
  loadDefaultFonts();
  const P = getBrandPalette(brand);
  const B = BRANDS[brand];

  return (
    <AbsoluteFill style={{backgroundColor: P.bg, padding: 60, fontFamily: B.fonts.display}}>
      {/* Eyebrow */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 12,
          marginBottom: 32,
        }}
      >
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
            fontSize: 16,
            fontWeight: 800,
            letterSpacing: "0.28em",
          }}
        >
          {eyebrow}
        </span>
      </div>

      {/* Pain headline */}
      <div
        style={{
          fontSize: 72,
          fontWeight: 900,
          lineHeight: 1.0,
          letterSpacing: "-0.035em",
          color: P.primary,
          maxWidth: 900,
        }}
      >
        {painHeadline}{" "}
        <span style={{fontStyle: "italic", fontWeight: 700, color: P.primary}}>
          {painItalic}
        </span>
      </div>

      {/* Pain body */}
      <div
        style={{
          marginTop: 28,
          color: P.text,
          fontSize: 22,
          fontWeight: 500,
          opacity: 0.78,
          lineHeight: 1.4,
          maxWidth: 700,
        }}
      >
        {painBody}
      </div>

      {/* Solution card */}
      <div
        style={{
          marginTop: 44,
          background: P.mode === "light" ? P.primary : `${P.accent}12`,
          borderRadius: 24,
          padding: "36px 36px 30px",
          color: P.mode === "light" ? P.bg : P.text,
          border: P.mode === "dark" ? `1.5px solid ${P.accent}55` : "none",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 14,
            marginBottom: 16,
          }}
        >
          <div
            style={{
              padding: "5px 14px",
              background: P.accent,
              borderRadius: 999,
              color: P.mode === "light" ? P.primary : P.bg,
              fontFamily: B.fonts.mono,
              fontSize: 14,
              fontWeight: 800,
              letterSpacing: "0.2em",
            }}
          >
            {solutionLabel}
          </div>
          <span
            style={{
              fontSize: 32,
              fontWeight: 900,
              letterSpacing: "-0.02em",
              color: P.mode === "light" ? P.bg : P.primary,
            }}
          >
            {solutionTitle}
          </span>
        </div>

        <div style={{display: "flex", flexDirection: "column", gap: 14, marginTop: 18}}>
          {solutionBullets.map((b, i) => (
            <div key={i} style={{display: "flex", alignItems: "center", gap: 14}}>
              <span
                style={{
                  width: 28,
                  height: 28,
                  borderRadius: "50%",
                  background: P.accent,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  color: P.mode === "light" ? P.primary : P.bg,
                  fontSize: 18,
                  fontWeight: 900,
                  flexShrink: 0,
                }}
              >
                ✓
              </span>
              <span
                style={{
                  fontSize: 22,
                  fontWeight: 600,
                  color: P.mode === "light" ? "#FFFFFF" : P.text,
                }}
              >
                {b}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Price + CTA at bottom */}
      <div
        style={{
          position: "absolute",
          bottom: 60,
          left: 60,
          right: 60,
          display: "flex",
          alignItems: "center",
          gap: 20,
        }}
      >
        {price && (
          <div style={{display: "flex", flexDirection: "column"}}>
            <div
              style={{
                display: "flex",
                alignItems: "baseline",
                gap: 10,
              }}
            >
              <span
                style={{
                  color: P.primary,
                  fontSize: 56,
                  fontWeight: 900,
                  letterSpacing: "-0.04em",
                  lineHeight: 1.0,
                }}
              >
                {price}
              </span>
              <span
                style={{
                  color: P.text,
                  fontFamily: B.fonts.mono,
                  fontSize: 18,
                  fontWeight: 600,
                  opacity: 0.7,
                }}
              >
                {priceCurrency}
              </span>
            </div>
            {priceOriginal && (
              <div
                style={{
                  color: P.text,
                  fontFamily: B.fonts.mono,
                  fontSize: 15,
                  marginTop: 4,
                  opacity: 0.55,
                  textDecoration: "line-through",
                }}
              >
                {priceOriginal}
              </div>
            )}
          </div>
        )}
        <div style={{flex: 1}} />
        <div
          style={{
            padding: "22px 30px",
            background: P.accent,
            borderRadius: 16,
            color: P.mode === "light" ? P.primary : P.bg,
            fontSize: 26,
            fontWeight: 800,
            letterSpacing: "-0.01em",
            boxShadow: P.mode === "dark" ? `0 6px 20px ${P.accent}55` : "none",
          }}
        >
          {cta}
        </div>
      </div>
    </AbsoluteFill>
  );
};
