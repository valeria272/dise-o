import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {revex, ensureRevexFonts} from "../../brand/revex";

/**
 * SISTEMA GRÁFICO GRUPO REVEX
 * Calibrado contra los videos y estáticas de la diseñadora
 * (raw/revex/ref-drive/, 24-08-2026). Manual: clients/revex/CLAUDE.md
 *
 * Regla madre: REVEX COMPONE CENTRADO Y DENSO. Todo se apila al eje
 * central: gancho cursivo, titular con barra, bullets, cajas de dato,
 * URL. (Casablanca es lo contrario: aire y tercio inferior — no mezclar.)
 */

const C = revex.colors;
const F = revex.fonts.display;

/** Foto a sangre + velo oscuro (Revex oscurece más que Casablanca). */
export const FondoRevex: React.FC<{
  src: string;
  velo?: number;
  focus?: string;
}> = ({src, velo = 0.55, focus = "center"}) => (
  <AbsoluteFill>
    <Img
      src={staticFile(src)}
      style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: focus}}
    />
    <AbsoluteFill
      style={{
        background: `linear-gradient(180deg, rgba(0,0,0,${velo * 0.55}) 0%, rgba(0,0,0,${
          velo * 0.8
        }) 45%, rgba(0,0,0,${velo}) 100%)`,
      }}
    />
  </AbsoluteFill>
);

/** Bloque rojo del logo. Feed: cuelga del borde. Story: baja a zona segura. */
export const LogoBlockRevex: React.FC<{story?: boolean; align?: "center" | "left"}> = ({
  story = false,
  align = "center",
}) => {
  const g = story ? revex.layout.logoBlockStory : revex.layout.logoBlock;
  return (
    <div
      style={{
        position: "absolute",
        top: g.top,
        ...(align === "center" ? {left: "50%", transform: "translateX(-50%)"} : {left: 90}),
        width: g.w,
        height: g.h,
        background: C.blockRed, // el CUADRO del bloque — no es el rojo del logotipo
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <Img src={staticFile(revex.logo)} style={{width: g.logoW}} />
    </div>
  );
};

/**
 * Gancho emocional: línea cursiva blanca + barra roja en minúsculas.
 * Es la apertura de las piezas de producto ("Tu hogar merece", "Calgary").
 */
export const GanchoScriptRevex: React.FC<{
  cursiva: string;
  barra?: string;
  size?: number;
}> = ({cursiva, barra, size = 96}) => {
  ensureRevexFonts();
  return (
    <div style={{textAlign: "center"}}>
      <div
        style={{
          font: `400 ${size}px/1.1 ${revex.fonts.script}`,
          color: "#fff",
          textShadow: "0 3px 24px rgba(0,0,0,.55)",
        }}
      >
        {cursiva}
      </div>
      {barra ? (
        <div style={{marginTop: size * 0.12}}>
          <span
            style={{
              display: "inline-block",
              background: C.barRed,
              color: "#fff",
              font: `500 ${size * 0.30}px/1 ${F}`,
              padding: `${size * 0.11}px ${size * 0.28}px`,
              whiteSpace: "nowrap",
            }}
          >
            {barra}
          </span>
        </div>
      ) : null}
    </div>
  );
};

/**
 * Titular institucional: versales blancas, la segunda línea dentro de la
 * barra roja. La barra va SIEMPRE en una sola línea, ajustada al texto.
 */
export const TitularRevex: React.FC<{
  linea1?: string;
  linea2: string;
  size: number;
}> = ({linea1, linea2, size}) => {
  ensureRevexFonts();
  const base: React.CSSProperties = {
    font: `800 ${size}px/1.12 ${F}`,
    color: "#fff",
    textTransform: "uppercase",
    letterSpacing: -0.5,
    textAlign: "center",
    margin: 0,
    whiteSpace: "nowrap",
  };
  return (
    <div style={{textAlign: "center"}}>
      {linea1 ? <div style={{...base, textShadow: "0 3px 18px rgba(0,0,0,.45)"}}>{linea1}</div> : null}
      <div style={{marginTop: linea1 ? size * 0.14 : 0}}>
        <span
          style={{
            ...base,
            display: "inline-block",
            background: C.barRed,
            padding: `${revex.layout.barPadding.y}px ${revex.layout.barPadding.x}px`,
          }}
        >
          {linea2}
        </span>
      </div>
    </div>
  );
};

/** Línea con puntos: « • AHORA EN LAS CONDES • » — versales regulares espaciadas. */
export const BulletLineRevex: React.FC<{texto: string; size?: number}> = ({texto, size = 34}) => {
  ensureRevexFonts();
  return (
    <div
      style={{
        font: `400 ${size}px/1.3 ${F}`,
        color: "#fff",
        textTransform: "uppercase",
        letterSpacing: 2,
        textAlign: "center",
      }}
    >
      {"• "}{texto}{" •"}
    </div>
  );
};

/** Pregunta bold + dato dentro de caja roja («¿Cómo llegar?» / dirección). */
export const DatoBoxRevex: React.FC<{
  pregunta?: string;
  dato: string;
  size?: number;
}> = ({pregunta, dato, size = 34}) => {
  ensureRevexFonts();
  return (
    <div style={{textAlign: "center"}}>
      {pregunta ? (
        <div style={{font: `700 ${size}px/1.3 ${F}`, color: "#fff", marginBottom: size * 0.3}}>
          {pregunta}
        </div>
      ) : null}
      <span
        style={{
          display: "inline-block",
          background: C.barRed,
          color: "#fff",
          font: `400 ${size}px/1.3 ${F}`,
          padding: `${size * 0.18}px ${size * 0.5}px`,
        }}
      >
        {dato}
      </span>
    </div>
  );
};

/** Cuerpo centrado con negritas mezcladas (el de los videos de producto). */
export type Parte = {t: string; bold?: boolean};
export const CuerpoRevex: React.FC<{lineas: Parte[][]; size?: number}> = ({lineas, size = 30}) => {
  ensureRevexFonts();
  return (
    <div style={{textAlign: "center"}}>
      {lineas.map((linea, i) => (
        <div key={i} style={{font: `400 ${size}px/1.45 ${F}`, color: "#fff"}}>
          {linea.map((p, j) => (
            <span key={j} style={{fontWeight: p.bold ? 700 : 400}}>
              {p.t}
            </span>
          ))}
        </div>
      ))}
    </div>
  );
};

/** Bajada de sucursal entre dos filetes blancos finos (estáticas jun/jul). */
export const BajadaRevex: React.FC<{
  lineas: Parte[][];
  size: number;
  width?: number | string;
}> = ({lineas, size, width = "82%"}) => {
  ensureRevexFonts();
  const hair = <div style={{height: revex.layout.hairline, background: "rgba(255,255,255,.85)", width: "100%"}} />;
  return (
    <div style={{width, display: "flex", flexDirection: "column", alignItems: "center", gap: size * 0.5}}>
      {hair}
      <div style={{textAlign: "center"}}>
        {lineas.map((linea, i) => (
          <div key={i} style={{font: `400 ${size}px/1.35 ${F}`, color: "#fff"}}>
            {linea.map((p, j) => (
              <span key={j} style={{fontWeight: p.bold ? 700 : 400}}>
                {p.t}
              </span>
            ))}
          </div>
        ))}
      </div>
      {hair}
    </div>
  );
};

/** CTA. Rojo sólido = el de siempre. Outline = URL o cierre. */
export const CtaRevex: React.FC<{
  texto: string;
  variante?: "red" | "outline";
  size?: number;
}> = ({texto, variante = "red", size = 30}) => {
  ensureRevexFonts();
  const common: React.CSSProperties = {
    font: `500 ${size}px/1 ${F}`,
    color: "#fff",
    display: "inline-block",
    letterSpacing: 0.3,
  };
  if (variante === "outline")
    return (
      <span
        style={{
          ...common,
          fontWeight: 700,
          border: "2px solid rgba(255,255,255,.92)",
          borderRadius: 6,
          padding: `${size * 0.5}px ${size * 1.4}px`,
        }}
      >
        {texto}
      </span>
    );
  return (
    <span style={{...common, background: C.barRed, padding: `${size * 0.45}px ${size * 1.0}px`}}>
      {texto}
    </span>
  );
};

/**
 * Ficha de producto de los videos: tabla vertical CENTRADA con borde blanco
 * y la banderola roja con pliegue colgada de su esquina superior,
 * extendiéndose hacia el lado indicado.
 */
export const BanderolaRevex: React.FC<{
  muestra: string;
  categoria: string;
  producto: string;
  ancho?: number;
  alto?: number;
  flagSide?: "left" | "right";
}> = ({muestra, categoria, producto, ancho = 190, alto, flagSide = "left"}) => {
  ensureRevexFonts();
  const h = alto ?? ancho * 2.2;
  const flagW = 300;
  return (
    <div style={{position: "relative", display: "inline-block"}}>
      <Img
        src={staticFile(muestra)}
        style={{
          width: ancho,
          height: h,
          objectFit: "cover",
          border: "7px solid #fff",
          borderRadius: 8,
          boxShadow: "0 18px 40px rgba(0,0,0,.4)",
          display: "block",
        }}
      />
      <div
        style={{
          position: "absolute",
          top: -6,
          ...(flagSide === "left" ? {right: ancho * 0.55} : {left: ancho * 0.55}),
          width: flagW,
          background: C.tagRed,
          padding: "12px 18px 14px",
          textAlign: "center",
          boxShadow: "0 10px 26px rgba(0,0,0,.35)",
        }}
      >
        <div
          style={{
            position: "absolute",
            ...(flagSide === "left" ? {right: 40, borderRight: "16px solid transparent"} : {left: 40, borderLeft: "16px solid transparent"}),
            bottom: -16,
            width: 0,
            height: 0,
            borderTop: `16px solid ${C.tagFold}`,
          }}
        />
        <div style={{font: `400 19px/1.2 ${F}`, color: "#fff", letterSpacing: 1.6, textTransform: "uppercase"}}>
          {categoria}
        </div>
        <div style={{font: `700 26px/1.25 ${F}`, color: "#fff", marginTop: 3, textTransform: "uppercase"}}>
          {producto}
        </div>
      </div>
    </div>
  );
};
