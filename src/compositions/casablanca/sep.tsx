import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {casablanca} from "../../brand/casablanca";

/**
 * PISOS CASABLANCA — SEPTIEMBRE 2026
 * =============================================================================
 * Este sistema sale de DOS fuentes, y de ninguna otra:
 *
 *  1. **Las piezas reales de la diseñadora**, en la carpeta de referencias que
 *     acompaña al brief (`raw/casablanca/ref-drive/estaticas/` — carruseles de
 *     mayo, julio y agosto, más los cuatro videos). De ahí sale la gramática:
 *       · tarjeta BLANCA del logo colgando del borde superior, centrada;
 *       · nombre del piso en **serif itálica**, blanco, CENTRADO, como elemento
 *         más grande de la pieza;
 *       · bajada en versales entre dos filetes finos;
 *       · CTA en cápsula de borde blanco.
 *     Medido sobre `Casablanca_pisos-2.png` (2250 × 2250): titular 6,9 % del
 *     ancho de tinta (≈7,3 % de cuerpo), bajada 2,3 %, bloque centrado al 50 %.
 *
 *  2. **El brief de septiembre** (`Brief Diseño Septiembre 2026 - CASABLANCA.xlsx`),
 *     que manda en el QUÉ y en las reglas de armado:
 *       · nº1 un mismo ambiente en las 4 tarjetas, cambia sólo la tabla;
 *       · nº2 plano amplio, el piso ocupa al menos la mitad del cuadro;
 *       · nº5 el texto NUNCA va sobre la madera → el bloque vive sobre el muro;
 *       · nº6 jerarquía: etiqueta del look arriba en versales con tracking amplio
 *         → nombre del producto (lo más grande) → medida abajo en cuerpo menor;
 *       · nº7 logo en la misma posición en las cuatro + indicador de deslizar en
 *         la tarjeta 1;
 *       · nº8 sin precios, sin porcentajes, sin urgencia.
 *
 * Medidas: 1080 × 1080 (lo que pide el brief) y su adaptación a 1080 × 1920.
 *
 * ⚠️ Diferencia consciente con las referencias: la diseñadora apoya el titular
 * sobre el piso; el brief prohíbe texto sobre la madera. Manda el brief, así que
 * el bloque va sobre el muro claro.
 */

const SANS = casablanca.fonts.sans;
const SERIF = casablanca.fonts.display; // Playfair Display — la itálica de la marca

export type Fmt = "feed" | "story";

/** Geometría en fracción del ANCHO, salvo donde diga alto. */
export const SEP = {
  logoCard: {w: 0.148, h: 0.169, top: 0, radius: 6},
  bloque: {
    /**
     * Centro vertical del bloque, en fracción del ALTO.
     * En feed (1080×1080) el bloque tiene que caber entre el borde inferior de
     * la tarjeta del logo (y = 182) y la línea del piso (y ≈ 560): el texto no
     * va sobre la madera (lineamiento nº5). Con el centro en 0,335 el titular
     * se metía debajo del logo.
     */
    centro: {feed: 0.365, story: 0.4},
    ancho: 0.84,
  },
  antetitulo: {cuerpo: 0.0165, tracking: 0.22},
  titular: {cuerpo: 0.063, interlinea: 1.06},
  filete: {ancho: 0.66, grosor: 2, margen: 0.016},
  bajada: {cuerpo: 0.0225, tracking: 0.1, interlinea: 1.4},
  medida: {cuerpo: 0.0195, tracking: 0.06},
  cta: {cuerpo: 0.0195, padY: 0.014, padX: 0.03, borde: 1.5},
} as const;

/** Foto a sangre. El velo apenas sostiene el texto sobre el muro claro. */
export const FondoSep: React.FC<{src: string; velo?: number; focus?: string}> = ({
  src,
  velo = 0.3,
  focus = "center 55%",
}) => (
  <AbsoluteFill>
    <Img
      src={staticFile(src)}
      style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: focus}}
    />
    <AbsoluteFill
      style={{
        background: `linear-gradient(180deg, rgba(0,0,0,${velo * 0.9}) 0%, rgba(0,0,0,${
          velo * 0.55
        }) 46%, rgba(0,0,0,0) 72%)`,
      }}
    />
  </AbsoluteFill>
);

/**
 * Tarjeta BLANCA del logo colgando del borde superior, centrada.
 * Es la gramática de la diseñadora en sus estáticas y en los cuatro videos, y el
 * brief pide además que vaya en la misma posición en las cuatro tarjetas.
 */
export const TarjetaLogo: React.FC<{w: number}> = ({w}) => (
  <div
    style={{
      position: "absolute",
      top: 0,
      left: "50%",
      transform: "translateX(-50%)",
      width: w * SEP.logoCard.w,
      height: w * SEP.logoCard.h,
      background: casablanca.colors.white,
      borderBottomLeftRadius: SEP.logoCard.radius,
      borderBottomRightRadius: SEP.logoCard.radius,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
    }}
  >
    <Img
      src={staticFile(casablanca.logo)}
      style={{width: w * SEP.logoCard.w * 0.68, objectFit: "contain"}}
    />
  </div>
);

/**
 * El bloque de texto, en el orden que fija el lineamiento nº6 del brief.
 * Centrado, como en todas las piezas de la diseñadora.
 */
export const BloqueSep: React.FC<{
  w: number;
  h: number;
  fmt: Fmt;
  /** Override del centro vertical, en fracción del alto (para fotos con el
   *  detalle importante en el medio, como la fachada con su letrero). */
  centro?: number;
  /** "LOOK NATURAL UV" — versales, cuerpo chico, tracking amplio. */
  etiqueta?: string;
  /** Lo más grande de la pieza. Una línea por elemento, saltos fijados a mano. */
  titulo: string[];
  /** El texto en la imagen que pide el brief, en versales entre filetes. */
  bajada?: string[];
  /** La medida, cuerpo menor. */
  medida?: string;
  cta?: string;
}> = ({w, h, fmt, centro, etiqueta, titulo, bajada, medida, cta}) => {
  const filete = (
    <div
      style={{
        width: w * SEP.filete.ancho,
        height: SEP.filete.grosor,
        background: "rgba(255,255,255,.85)",
        margin: `${w * SEP.filete.margen}px auto`,
      }}
    />
  );
  return (
    <div
      style={{
        position: "absolute",
        top: h * (centro ?? SEP.bloque.centro[fmt]),
        left: "50%",
        transform: "translate(-50%, -50%)",
        width: w * SEP.bloque.ancho,
        textAlign: "center",
        color: casablanca.colors.white,
        textShadow: "0 2px 12px rgba(0,0,0,.45), 0 6px 40px rgba(0,0,0,.4)",
      }}
    >
      {etiqueta ? (
        <div
          style={{
            fontFamily: SANS,
            fontWeight: 500,
            fontSize: w * SEP.antetitulo.cuerpo,
            letterSpacing: w * SEP.antetitulo.cuerpo * SEP.antetitulo.tracking,
            textTransform: "uppercase",
            marginBottom: w * 0.011,
            opacity: 0.95,
          }}
        >
          {etiqueta}
        </div>
      ) : null}

      <div
        style={{
          fontFamily: SERIF,
          fontStyle: "italic",
          fontWeight: 700,
          fontSize: w * SEP.titular.cuerpo,
          lineHeight: SEP.titular.interlinea,
        }}
      >
        {titulo.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </div>

      {bajada ? (
        <>
          {filete}
          <div
            style={{
              fontFamily: SANS,
              fontWeight: 500,
              fontSize: w * SEP.bajada.cuerpo,
              letterSpacing: w * SEP.bajada.cuerpo * SEP.bajada.tracking,
              lineHeight: SEP.bajada.interlinea,
              textTransform: "uppercase",
            }}
          >
            {bajada.map((l) => (
              <div key={l}>{l}</div>
            ))}
          </div>
          {filete}
        </>
      ) : null}

      {medida ? (
        <div
          style={{
            fontFamily: SANS,
            fontWeight: 400,
            fontSize: w * SEP.medida.cuerpo,
            letterSpacing: w * SEP.medida.cuerpo * SEP.medida.tracking,
            marginTop: bajada ? w * 0.005 : w * 0.018,
            opacity: 0.95,
          }}
        >
          {medida}
        </div>
      ) : null}

      {cta ? (
        <div
          style={{
            display: "inline-block",
            marginTop: w * 0.024,
            padding: `${w * SEP.cta.padY}px ${w * SEP.cta.padX}px`,
            border: `${SEP.cta.borde}px solid rgba(255,255,255,.9)`,
            borderRadius: 999,
            fontFamily: SANS,
            fontWeight: 500,
            fontSize: w * SEP.cta.cuerpo,
            letterSpacing: w * SEP.cta.cuerpo * 0.04,
          }}
        >
          {cta}
        </div>
      ) : null}
    </div>
  );
};

/** Indicador de deslizar — lineamiento nº7, sólo en la tarjeta 1 y sólo en feed. */
export const Desliza: React.FC<{w: number; h: number}> = ({w, h}) => (
  <div
    style={{
      position: "absolute",
      bottom: h * 0.055,
      left: "50%",
      transform: "translateX(-50%)",
      fontFamily: SANS,
      fontWeight: 500,
      fontSize: w * 0.019,
      letterSpacing: w * 0.019 * 0.14,
      textTransform: "uppercase",
      color: casablanca.colors.white,
      textShadow: "0 2px 14px rgba(0,0,0,.5)",
      opacity: 0.92,
    }}
  >
    Desliza →
  </div>
);
