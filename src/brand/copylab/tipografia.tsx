// ============================================================================
// COPYWRITERS — composición tipográfica
// ----------------------------------------------------------------------------
// Esto NO pinta titulares "bien ordenados". Es un instrumento para COMPONER:
// romper líneas, cambiar de escala, comprimir, estirar, desplazar, encerrar,
// tachar y usar el espacio negativo.
//
// Por eso <Bloque> no recibe `titulo` y `bajada` — recibe un ARREGLO de líneas
// donde cada línea decide su propia voz, escala, ancho, peso, color y
// desplazamiento. La diferencia no es cosmética: con `titulo/bajada` sólo se
// puede rellenar una plantilla; con líneas se puede componer.
//
// El tope está en el sistema, no en el gusto: máximo UNA anomalía fuerte por
// composición (tokens.json → topes.anomaliasFuertesPorPieza). Sin ese tope, el
// feed deja de ser sofisticado y pasa a ser un experimento tipográfico.
// ============================================================================
import React from "react";
import {C, VOZ, Voz, CL, ancho} from "./sistema";

// ---------------------------------------------------------------------------
// Métricas por voz. Salen de tokens.json para que Python las lea igual.
// ---------------------------------------------------------------------------
const M = CL.voces;

export type Linea = {
  /** El texto. Una línea = una decisión de quiebre. */
  t: string;
  /** Voz. Por defecto `impacto`. */
  voz?: Voz;
  /** Multiplicador sobre el tamaño base del bloque. 1 = base. */
  esc?: number;
  color?: string;
  /** Eje de ancho de Archivo (62 condensada dura ↔ 125 extendida). Sólo `impacto`. */
  wdth?: number;
  /** Eje de peso (100–900). Sólo `impacto`. */
  wght?: number;
  /** Desplazamiento horizontal en px. Así se rompe el eje sin romper el bloque. */
  dx?: number;
  /** Ajuste vertical en px contra la línea anterior. Negativo = aprieta. */
  dy?: number;
  /** Tracking en em. Sobreescribe el de la voz. */
  track?: number;
  /** Interlineado. Sobreescribe el de la voz. */
  alto?: number;
  /** Fondo macizo detrás de la línea — el gesto de "encerrar". */
  caja?: string;
  /** Color del texto cuando hay caja. */
  enCaja?: string;
  op?: number;
  /** Versales forzadas. `impacto` casi siempre va en versales. */
  versales?: boolean;
};

const familia = (v: Voz) => VOZ[v];

const metricas = (v: Voz) => {
  const m = M[v] as {tracking: number; interlineado: number};
  return {track: m.tracking, alto: m.interlineado};
};

/** Una línea suelta. Rara vez se usa sola: existe para que <Bloque> la componga. */
export const Linea: React.FC<{l: Linea; base: number}> = ({l, base}) => {
  const v = l.voz ?? "impacto";
  const m = metricas(v);
  const size = base * (l.esc ?? 1);
  const esImpacto = v === "impacto";
  const esMano = v === "mano";

  const estilo: React.CSSProperties = {
    fontFamily: familia(v),
    fontSize: size,
    lineHeight: l.alto ?? m.alto,
    letterSpacing: `${l.track ?? m.track}em`,
    color: l.caja ? (l.enCaja ?? C.tinta) : (l.color ?? C.offwhite),
    opacity: l.op ?? 1,
    marginLeft: l.dx ?? 0,
    marginTop: l.dy ?? 0,
    whiteSpace: "pre",
    // Caveat es una manuscrita de trazo fino: a igual cuerpo pesa la mitad que
    // Archivo. Se compensa acá y no en cada pieza, o la anotación desaparece.
    ...(esMano ? {fontWeight: 700} : null),
    ...(esImpacto
      ? {
          fontVariationSettings: ancho(l.wdth ?? 70, l.wght ?? 900),
          fontWeight: l.wght ?? 900,
          textTransform: (l.versales ?? true) ? "uppercase" : "none",
        }
      : {fontStyle: v === "editorial" ? "italic" : "normal"}),
    ...(v === "data"
      ? {textTransform: "uppercase" as const, fontWeight: 500}
      : null),
  };

  if (!l.caja) return <div style={estilo}>{l.t}</div>;

  // "Encerrar" = bloque macizo pegado al texto, sin esquinas redondeadas.
  // El radio es de las cards de SaaS y está prohibido en tokens.json.
  return (
    <div style={{marginLeft: l.dx ?? 0, marginTop: l.dy ?? 0}}>
      <span
        style={{
          ...estilo,
          marginLeft: 0,
          marginTop: 0,
          display: "inline-block",
          background: l.caja,
          padding: `${size * 0.06}px ${size * 0.14}px ${size * 0.14}px`,
        }}
      >
        {l.t}
      </span>
    </div>
  );
};

/**
 * El compositor. Recibe líneas, no campos.
 *
 *   <Bloque base={168} lineas={[
 *     {t: "NADIE RECUERDA"},
 *     {t: "TU ÚLTIMO POST.", wdth: 110, esc: 0.62},
 *     {t: "Se acuerdan de tu última idea.", voz: "editorial", color: C.rosa, esc: 0.5},
 *   ]} />
 */
export const Bloque: React.FC<{
  lineas: Linea[];
  base: number;
  /** Compensa el side bearing de Archivo para que el bloque quede ópticamente
   *  alineado con el margen y no matemáticamente alineado (que se ve corrido). */
  sangria?: number;
  style?: React.CSSProperties;
}> = ({lineas, base, sangria = 0.045, style}) => (
  <div style={{marginLeft: -base * sangria, ...style}}>
    {lineas.map((l, i) => (
      <Linea key={i} l={l} base={base} />
    ))}
  </div>
);

/**
 * ÍNDICE — la línea de metadata en mono.
 *
 * Es la firma silenciosa del sistema y la razón por la que la mayoría de las
 * piezas NO llevan logo: dos piezas sin nada en común se reconocen como la
 * misma cuenta porque las dos tienen esta línea arriba, con el mismo tracking
 * y el mismo cuerpo. Identificar antes que logotipar (COPYWRITERS_CREATIVE_OS §9).
 */
export const Indice: React.FC<{
  familia: string;
  ref?: string;
  color?: string;
  size?: number;
  acento?: string;
  style?: React.CSSProperties;
}> = ({familia: fam, ref: r, color = "rgba(242,244,246,0.55)", size = 22, acento, style}) => (
  <div
    style={{
      fontFamily: VOZ.data,
      fontSize: size,
      fontWeight: 500,
      letterSpacing: `${M.data.tracking}em`,
      textTransform: "uppercase",
      color,
      ...style,
    }}
  >
    {fam}
    {r ? (
      <>
        <span style={{opacity: 0.45}}>{"  /  "}</span>
        <span style={acento ? {color: acento} : undefined}>{r}</span>
      </>
    ) : null}
  </div>
);
