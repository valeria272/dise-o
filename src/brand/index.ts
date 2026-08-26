import {copywriters} from "./copywriters";
import {scopemedia} from "./scopemedia";
import {hypeinfluence} from "./hypeinfluence";
import {rocketdesign} from "./rocketdesign";

export type BrandSlug = "copywriters" | "scopemedia" | "hypeinfluence" | "rocketdesign";

export type BrandTokens = {
  colors: Record<string, string>;
  fonts: {display: string; mono: string};
  name: string;
  url: string;
  tagline: string;
  category?: string;
  [key: string]: unknown;
};

export const BRANDS: Record<BrandSlug, BrandTokens> = {
  copywriters,
  scopemedia,
  hypeinfluence,
  rocketdesign,
};

// Helper: returns the BG/PRIMARY/ACCENT triplet per brand for templates that need uniformity
export const getBrandPalette = (slug: BrandSlug) => {
  const b = BRANDS[slug];
  switch (slug) {
    case "copywriters":
      return {bg: b.colors.cream, primary: b.colors.navy, accent: b.colors.lime, text: b.colors.text, mode: "light" as const};
    case "scopemedia":
      return {bg: b.colors.bg, primary: b.colors.cream, accent: b.colors.teal, text: b.colors.text, mode: "dark" as const};
    case "hypeinfluence":
      return {bg: b.colors.black, primary: b.colors.white, accent: b.colors.pink, text: b.colors.cream, mode: "dark" as const};
    case "rocketdesign":
      return {bg: b.colors.dark, primary: b.colors.cream, accent: b.colors.lime, text: b.colors.cream, mode: "dark" as const};
  }
};
