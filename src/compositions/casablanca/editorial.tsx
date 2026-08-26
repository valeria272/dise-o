import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {casablanca} from "../../brand/casablanca";

/**
 * PISOS CASABLANCA — SISTEMA EDITORIAL (replanteo 25-08-2026)
 * =============================================================================
 * Reemplaza a `sistema.tsx` para las piezas de producto y de showroom.
 *
 * **Por qué existe.** El sistema anterior venía del carrusel de mayo de Paulina:
 * tarjeta blanca de logo centrada arriba, muestra vertical con borde blanco, caja
 * gris pesada al lado y todo el texto centrado. Valeria lo bajó entero el 25-08
 * contra el feed real de la marca: *"Eliminar el sistema actual de muestra
 * vertical gigante + borde blanco + caja gris pesada. Se siente demasiado como
 * catálogo técnico"*.
 *
 * **De dónde sale este.** De las publicaciones de @pisos_casablanca que mandó
 * como benchmark (Roble Aserrado Natural UV, Roble Margarita) y de los videos
 * oficiales en `raw/casablanca/ref-drive/videos/`:
 *
 *   1. La FOTOGRAFÍA manda: ocupa el 100 % del cuadro y se lleva el 80–90 % de la
 *      atención. La gráfica acompaña, no compite.
 *   2. El logo va en una **placa gris cálida integrada al costado**, no en una
 *      caja blanca centrada colgando del borde.
 *   3. El bloque de texto es **editorial y alineado a la izquierda**, no centrado:
 *      antetítulo en versales chicas → nombre del piso en serif de caja alta y
 *      alto contraste → filete corto → bajada de dos líneas.
 *   4. **El texto se apoya sobre el piso**, en la zona limpia. Ojo: el brief de
 *      Serena decía *"el texto NUNCA va sobre la madera"*; el feed real de la
 *      marca hace exactamente lo contrario y es lo que Valeria pidió replicar.
 *      Si vuelve a mandar el brief, esto se revierte — está aislado en `BLOQUE`.
 *
 * Toda la geometría va en fracciones del ANCHO del lienzo, así feed (1080×1350) y
 * story (1080×1920) comparten sistema sin recalcular nada a mano.
 */

const SANS = casablanca.fonts.sans;
const DISPLAY = casablanca.fonts.editorial;

export type Fmt = "feed" | "story";

/** Geometría medida sobre las publicaciones del benchmark, en fracción del ancho. */
export const ED = {
  /** Placa gris del logo: pegada al borde izquierdo, en el tercio superior. */
  placa: {ancho: 0.250, alto: 0.098, top: {feed: 0.10, story: 0.135}},
  /** Margen del bloque de texto. En story se respeta la zona segura lateral. */
  margen: 0.075,
  /** Dónde arranca el bloque de texto, en fracción del ALTO. */
  bloqueTop: {feed: 0.60, story: 0.50},
  antetitulo: {cuerpo: 0.0195, tracking: 0.17},   // em
  titular: {cuerpo: 0.082, interlinea: 1.04, tracking: 0.012},  // em
  filete: {ancho: 0.155, grosor: 1, margenY: 0.035},
  bajada: {cuerpo: 0.0215, tracking: 0.13, interlinea: 1.5},   // em
  pie: {cuerpo: 0.018, tracking: 0.11, alto: 0.052},   // em
} as const;

// ─────────────────────────────────────────────────────────────────────────────
// Fondo
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Foto a sangre con un degradado MUY sutil sólo donde se apoya el texto.
 *
 * Nada de velo general: la foto es el producto. Paulina fijó que el sombreado es
 * negro con opacidad (25-08), pero acá va dosificado a la zona del bloque — si se
 * apaga la foto entera, la pieza deja de ser fotografía de interiorismo.
 */
export const FotoEditorial: React.FC<{
  src: string;
  fmt: Fmt;
  /** 0 = sin velo. 0.38 es el máximo que tolera una foto clara. */
  velo?: number;
  focus?: string;
  /** El degradado arranca acá (fracción del alto). Por defecto, sobre el bloque. */
  desde?: number;
  /** Acercamiento sobre el encuadre. Sirve para sacar dos piezas distintas de una
   *  misma foto real sin partir el letrero del local en dos. */
  zoom?: number;
}> = ({src, fmt, velo = 0.4, focus = "center", desde, zoom = 1}) => {
  const y0 = desde ?? ED.bloqueTop[fmt] - 0.1;
  return (
    <AbsoluteFill>
      <Img
        src={staticFile(src)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          objectPosition: focus,
          transform: zoom === 1 ? undefined : `scale(${zoom})`,
          transformOrigin: focus,
        }}
      />
      <AbsoluteFill
        style={{
          background: `linear-gradient(180deg,
            rgba(0,0,0,0) ${y0 * 100}%,
            rgba(0,0,0,${velo * 0.72}) ${(y0 + 0.10) * 100}%,
            rgba(0,0,0,${velo}) 100%)`,
        }}
      />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// Logo
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Placa gris cálida con el logo BLANCO, pegada al borde izquierdo.
 *
 * ⚠️ Esto reemplaza a `LogoCardCasablanca` (caja blanca centrada, top 0). La
 * regla vieja —"la tarjeta cuelga del borde superior, nunca flota"— nació de las
 * estáticas de mayo y quedó ratificada dos veces; el feed nuevo de la marca usa
 * la placa lateral. Valeria: *"logo Casablanca blanco sobre una placa gris
 * cálida, integrado lateralmente a la composición"*.
 */
export const PlacaLogo: React.FC<{fmt: Fmt; w: number; h: number}> = ({fmt, w, h}) => {
  const ancho = w * ED.placa.ancho;
  const alto = w * ED.placa.alto;
  return (
    <div
      style={{
        position: "absolute",
        left: 0,
        top: h * ED.placa.top[fmt],
        width: ancho,
        height: alto,
        background: casablanca.colors.grayWarm,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <Img
        src={staticFile(casablanca.logoWhiteH)}
        style={{width: ancho * 0.78, objectFit: "contain"}}
      />
    </div>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// Bloque editorial
// ─────────────────────────────────────────────────────────────────────────────

/**
 * Antetítulo → titular en serif de caja alta → filete → bajada.
 * Todo alineado a la IZQUIERDA: la asimetría es lo que lo saca de "plantilla de
 * Instagram" y lo que hace el benchmark.
 */
export const BloqueEditorial: React.FC<{
  fmt: Fmt;
  w: number;
  h: number;
  antetitulo: string;
  /** Una línea por elemento — los saltos se fijan a mano, sin palabras huérfanas. */
  titular: string[];
  bajada: string[];
  color?: string;
}> = ({fmt, w, h, antetitulo, titular, bajada, color = "#FFFFFF"}) => (
  <div
    style={{
      position: "absolute",
      left: w * ED.margen,
      top: h * ED.bloqueTop[fmt],
      width: w * (1 - ED.margen * 2),
      color,
      // Sombra ancha y suave: sostiene el blanco sobre madera clara sin
      // ensuciar la foto. Es lo que reemplaza al velo pesado.
      textShadow: "0 2px 10px rgba(0,0,0,.42), 0 4px 38px rgba(0,0,0,.55)",
    }}
  >
    <div
      style={{
        fontFamily: SANS,
        fontWeight: 500,
        fontSize: w * ED.antetitulo.cuerpo,
        letterSpacing: w * ED.antetitulo.cuerpo * ED.antetitulo.tracking,
        textTransform: "uppercase",
        opacity: 0.92,
        marginBottom: w * 0.019,
      }}
    >
      {antetitulo}
    </div>

    <div
      style={{
        fontFamily: DISPLAY,
        fontWeight: 500,
        fontSize: w * ED.titular.cuerpo,
        lineHeight: ED.titular.interlinea,
        letterSpacing: w * ED.titular.cuerpo * ED.titular.tracking,
        textTransform: "uppercase",
      }}
    >
      {titular.map((l) => (
        <div key={l}>{l}</div>
      ))}
    </div>

    <div
      style={{
        width: w * ED.filete.ancho,
        height: ED.filete.grosor,
        background: color,
        opacity: 0.75,
        margin: `${w * ED.filete.margenY}px 0`,
      }}
    />

    <div
      style={{
        fontFamily: SANS,
        fontWeight: 500,
        fontSize: w * ED.bajada.cuerpo,
        letterSpacing: w * ED.bajada.cuerpo * ED.bajada.tracking,
        lineHeight: ED.bajada.interlinea,
        textTransform: "uppercase",
        opacity: 0.95,
      }}
    >
      {bajada.map((l) => (
        <div key={l}>{l}</div>
      ))}
    </div>
  </div>
);

/**
 * Línea de pie discreta, dentro de una cápsula gris translúcida.
 * Es el portador de la medida del producto o del dato de contacto: información,
 * no llamado a la acción gritado. Sin botón de WhatsApp dibujado — Meta pone el
 * suyo debajo de la pieza.
 */
export const PieEditorial: React.FC<{
  fmt: Fmt;
  w: number;
  h: number;
  texto: string;
}> = ({fmt, w, h, texto}) => (
  <div
    style={{
      position: "absolute",
      left: w * ED.margen,
      bottom: h * (fmt === "story" ? 0.205 : 0.062),
      maxWidth: w * (1 - ED.margen * 2),
      height: w * ED.pie.alto,
      padding: `0 ${w * 0.026}px`,
      background: "rgba(70,68,64,0.62)",
      display: "flex",
      alignItems: "center",
      fontFamily: SANS,
      fontWeight: 500,
      fontSize: w * ED.pie.cuerpo,
      letterSpacing: w * ED.pie.cuerpo * ED.pie.tracking,
      textTransform: "uppercase",
      color: "#FFFFFF",
      whiteSpace: "nowrap",
    }}
  >
    {texto}
  </div>
);
