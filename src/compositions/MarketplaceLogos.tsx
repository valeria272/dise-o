import React from "react";

export type Marketplace = "mercadolibre" | "falabella" | "ripley" | "paris" | "shopify";

const SPECS: Record<Marketplace, {bg: string; fg: string; label: string; mark?: string}> = {
  mercadolibre: {bg: "#FFE600", fg: "#2D3277", label: "ML", mark: "🤝"},
  falabella:    {bg: "#00813F", fg: "#FFFFFF", label: "F"},
  ripley:       {bg: "#E91556", fg: "#FFFFFF", label: "R"},
  paris:        {bg: "#0F2C5C", fg: "#FFFFFF", label: "P"},
  shopify:      {bg: "#95BF47", fg: "#FFFFFF", label: "S"},
};

export const MarketplaceBadge: React.FC<{
  marketplace: Marketplace;
  size?: number;
  glow?: boolean;
  opacity?: number;
}> = ({marketplace, size = 110, glow = true, opacity = 1}) => {
  const s = SPECS[marketplace];
  return (
    <div
      style={{
        width: size,
        height: size,
        borderRadius: "50%",
        background: s.bg,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        boxShadow: glow
          ? `0 0 ${size * 0.25}px rgba(45,212,171,0.35), 0 8px 24px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.3)`
          : "0 6px 18px rgba(0,0,0,0.4)",
        opacity,
        border: `2px solid rgba(255,255,255,0.15)`,
      }}
    >
      <span
        style={{
          color: s.fg,
          fontFamily: "'Inter', system-ui, sans-serif",
          fontSize: size * 0.42,
          fontWeight: 900,
          letterSpacing: "-0.04em",
        }}
      >
        {s.label}
      </span>
    </div>
  );
};

export const MARKETPLACES: Marketplace[] = ["mercadolibre", "falabella", "ripley", "paris", "shopify"];
