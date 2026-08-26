import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {casablanca, ensureCasablancaFonts} from "../../brand/casablanca";

/**
 * SISTEMA GRÁFICO PISOS CASABLANCA
 * Calibrado contra los 4 videos + carruseles de la diseñadora
 * (raw/casablanca/ref-drive/, 24-08-2026). Manual: clients/casablanca/CLAUDE.md
 *
 * Regla madre: CASABLANCA ES AIRE. Tarjeta blanca de logo grande arriba,
 * UNA idea en serif itálica en el tercio inferior, bajada en versales entre
 * filetes, y nada más. (Revex es lo contrario: centrado y denso — no mezclar.)
 * Acá NO existe el rojo, ni el descuento, ni la urgencia.
 */

const C = casablanca.colors;
const SERIF = casablanca.fonts.display;
const SANS = casablanca.fonts.sans;

/** Ambiente luminoso a sangre con velo cálido suave (nunca negro duro). */
export const FondoCasablanca: React.FC<{
  src: string;
  velo?: number;
  /** Opacidad extra en el tercio superior. En las tarjetas de producto el texto
   *  va arriba, sobre el muro claro, y sin esto la bajada blanca no se lee. */
  veloTop?: number;
  focus?: string;
}> = ({src, velo = 0.3, veloTop = 0.04, focus = "center"}) => (
  <AbsoluteFill>
    <Img
      src={staticFile(src)}
      style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: focus}}
    />
    {/* Ronda 2 (Paulina): «el sobreado siempre debe ser negro con opacidad» */}
    <AbsoluteFill
      style={{
        background: `linear-gradient(180deg, rgba(0,0,0,${veloTop}) 0%, rgba(0,0,0,${
          veloTop * 0.75
        }) 46%, rgba(0,0,0,${velo * 0.4}) 62%, rgba(0,0,0,${velo * 1.5}) 100%)`,
      }}
    />
  </AbsoluteFill>
);

/** Fondo bodegón de estudio (arena plano). */
export const FondoArena: React.FC = () => <AbsoluteFill style={{background: C.sand}} />;

/** Tarjeta BLANCA grande colgando del borde superior, con el logo apilado. */
export const LogoCardCasablanca: React.FC<{story?: boolean}> = ({story = false}) => {
  const g = story ? casablanca.layout.logoCardStory : casablanca.layout.logoCard;
  return (
    <div
      style={{
        position: "absolute",
        top: g.top,
        left: "50%",
        transform: "translateX(-50%)",
        width: g.w,
        height: g.h,
        background: "#fff",
        borderBottomLeftRadius: 6,
        borderBottomRightRadius: 6,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        boxShadow: "0 10px 30px rgba(0,0,0,.12)",
      }}
    >
      <Img
        src={staticFile(casablanca.logo)}
        style={{width: g.w * 0.66, maxHeight: g.h * 0.82, objectFit: "contain"}}
      />
    </div>
  );
};

/** Titular serif itálico. Capitalización normal, NUNCA versales. */
export const TitularCasablanca: React.FC<{
  texto: string;
  size: number;
  sobre?: "foto" | "claro";
}> = ({texto, size, sobre = "foto"}) => {
  ensureCasablancaFonts();
  return (
    <div
      style={{
        font: `italic 700 ${size}px/1.12 ${SERIF}`,
        color: sobre === "foto" ? "#fff" : C.grayDeep,
        textAlign: "center",
        textShadow: sobre === "foto" ? "0 3px 22px rgba(0,0,0,.35)" : "none",
        textWrap: "balance",
      } as React.CSSProperties}
    >
      {texto}
    </div>
  );
};

/** Bajada en VERSALES con tracking amplio, entre dos filetes de 1 px. */
export const BajadaCasablanca: React.FC<{
  texto: string;
  size: number;
  sobre?: "foto" | "claro";
  width?: number | string;
}> = ({texto, size, sobre = "foto", width = "70%"}) => {
  ensureCasablancaFonts();
  const color = sobre === "foto" ? "rgba(255,255,255,.95)" : C.grayText;
  const hair = (
    <div
      style={{
        height: casablanca.layout.hairline,
        background: sobre === "foto" ? "rgba(255,255,255,.75)" : "rgba(98,98,96,.45)",
        width: "100%",
      }}
    />
  );
  return (
    <div style={{width, display: "flex", flexDirection: "column", alignItems: "center", gap: size * 0.7}}>
      {hair}
      <div
        style={{
          font: `500 ${size}px/1.35 ${SANS}`,
          color,
          textTransform: "uppercase",
          letterSpacing: casablanca.layout.subtitleTracking,
          textAlign: "center",
        }}
      >
        {texto}
      </div>
      {hair}
    </div>
  );
};

/**
 * Chip de producto de los videos: muestra HORIZONTAL de la tabla, esquinas
 * redondeadas, flotando con sombra. (La banderola gris vertical es de los
 * carruseles; el chip es de los videos.)
 */
export const PlankChipCasablanca: React.FC<{
  muestra: string;
  ancho?: number;
}> = ({muestra, ancho = 420}) => (
  <Img
    src={staticFile(muestra)}
    style={{
      width: ancho,
      height: ancho * 0.34,
      objectFit: "cover",
      borderRadius: 14,
      boxShadow: "0 20px 44px rgba(0,0,0,.3)",
      display: "block",
    }}
  />
);

/**
 * Etiqueta de carrusel: caja gris de información, pegada a la muestra vertical
 * de la tabla con borde blanco. Va al costado, a media altura.
 *
 * ⛔ Corregido en la ronda 2 (25-08-2026, Paulina):
 *   1. La caja gris va DELANTE de la muestra (zIndex explícito), nunca detrás.
 *   2. El triángulo del lado inferior derecho es una SOMBRA — no un pliegue de
 *      banderola ni una colita de globo. Por eso es negro translúcido y chico.
 *   3. El texto va CENTRADO dentro de la caja gris.
 *   4. La caja tiene que quedar entera y con aire respecto del borde del lienzo:
 *      arranca en x = left + plank.w − tagFlag.w − foldW/2, así que `left` en la
 *      composición nunca puede dejarla a menos de ~90 px del borde.
 */
export const BanderolaCasablanca: React.FC<{
  tabla: string;
  categoria?: string;
  producto: string;
  alto?: number;
}> = ({tabla, categoria = "Piso de Ingeniería", producto, alto = 430}) => {
  ensureCasablancaFonts();
  const w = casablanca.layout.plank.w;
  return (
    <div style={{position: "relative", display: "inline-block"}}>
      <Img
        src={staticFile(tabla)}
        style={{
          width: w,
          height: alto,
          objectFit: "cover",
          border: `${casablanca.layout.plank.borderWhite}px solid #fff`,
          boxShadow: "0 16px 38px rgba(0,0,0,.28)",
          display: "block",
        }}
      />
      <div
        style={{
          position: "absolute",
          top: alto * 0.13,
          right: w * 0.55, // la etiqueta cuelga hacia la IZQUIERDA de la muestra (refs mayo/julio)
          width: casablanca.layout.tagFlag.w,
          background: C.gray,
          padding: "12px 18px 14px",
          textAlign: "center", // ronda 2: el texto va centrado en el cuadro gris
          boxShadow: "0 8px 22px rgba(0,0,0,.25)",
          zIndex: 2, // ronda 2: la caja de información va DELANTE de la muestra
        }}
      >
        {/* Sombra proyectada de la caja — NO es un pliegue ni una colita de globo */}
        <div
          style={{
            position: "absolute",
            right: 0,
            bottom: -casablanca.layout.tagFlag.foldW * 0.4,
            width: 0,
            height: 0,
            borderTop: `${casablanca.layout.tagFlag.foldW * 0.4}px solid rgba(0,0,0,.38)`,
            borderRight: `${casablanca.layout.tagFlag.foldW * 0.4}px solid transparent`,
          }}
        />
        <div style={{font: `400 22px/1.25 ${SANS}`, color: "#fff"}}>{categoria}</div>
        <div style={{font: `700 22px/1.25 ${SANS}`, color: "#fff", marginTop: 2, whiteSpace: "nowrap"}}>{producto}</div>
      </div>
    </div>
  );
};

/** CTA discreta. Versales espaciadas (la de los videos) u outline pill. */
export const CtaCasablanca: React.FC<{
  texto: string;
  variante?: "versales" | "outline" | "gris";
  size?: number;
}> = ({texto, variante = "versales", size = 26}) => {
  ensureCasablancaFonts();
  if (variante === "versales")
    return (
      <div
        style={{
          font: `500 ${size}px/1 ${SANS}`,
          color: "#fff",
          textTransform: "uppercase",
          letterSpacing: 3,
          textAlign: "center",
        }}
      >
        {texto}
      </div>
    );
  const common: React.CSSProperties = {
    font: `500 ${size}px/1 ${SANS}`,
    padding: `${size * 0.66}px ${size * 1.5}px`,
    display: "inline-block",
    letterSpacing: 0.4,
  };
  if (variante === "gris")
    return <span style={{...common, background: C.gray, color: "#fff", borderRadius: 4}}>{texto}</span>;
  return (
    <span style={{...common, border: "2px solid rgba(255,255,255,.9)", color: "#fff", borderRadius: casablanca.layout.ctaRadiusPill}}>
      {texto}
    </span>
  );
};

/**
 * Cierre oficial: fondo blanco, logo HORIZONTAL gris, filete y
 * "COTIZA POR WHATSAPP" en versales grises. Sin URL.
 */
export const CierreCasablanca: React.FC<{cta?: string}> = ({cta = "Cotiza por WhatsApp"}) => {
  ensureCasablancaFonts();
  return (
    <AbsoluteFill style={{background: "#FDFDFD", alignItems: "center", justifyContent: "center", gap: 46}}>
      <Img src={staticFile("assets/casablanca/logo_horizontal_gris.png")} style={{width: 560}} />
      <div style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 18, width: 420}}>
        <div style={{height: 1, background: "rgba(98,98,96,.4)", width: "100%"}} />
        <div
          style={{
            font: `500 24px/1 ${SANS}`,
            color: C.grayDeep,
            textTransform: "uppercase",
            letterSpacing: 3,
          }}
        >
          {cta}
        </div>
      </div>
    </AbsoluteFill>
  );
};
