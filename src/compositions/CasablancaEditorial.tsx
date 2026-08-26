import React from "react";
import {AbsoluteFill, useVideoConfig} from "remotion";
import {casablanca, ensureCasablancaFonts} from "../brand/casablanca";
import {
  BloqueEditorial,
  FotoEditorial,
  PieEditorial,
  PlacaLogo,
  type Fmt,
} from "./casablanca/editorial";

/**
 * PISOS CASABLANCA — SEPTIEMBRE 2026, REPLANTEO EDITORIAL
 * =============================================================================
 * Sustituye a `CasablancaSep2026.tsx`, que Valeria bajó entero el 25-08-2026
 * contra el feed real de la marca. El QUÉ no cambia —los mismos 4 SKU
 * autorizados del brief de Serena y el mismo carrusel de showroom—; cambia el
 * CÓMO: fotografía de interiorismo primero, producto segundo, gráfica después.
 *
 * Lo que se fue, y por qué:
 *  · La tarjeta blanca del logo centrada arriba → placa gris lateral.
 *  · La muestra vertical con borde blanco y la caja gris → nada. El producto se
 *    ve instalado, a escala real, en la propia fotografía.
 *  · El texto centrado → bloque editorial alineado a la izquierda.
 *  · El mismo ambiente en las 4 tarjetas → un ambiente propio por producto.
 *    ⚠️ Esto contradice el lineamiento nº 1 del brief ("UN MISMO AMBIENTE EN LAS
 *    4 TARJETAS"). Manda la instrucción del 25-08: *"NO USAR EL MISMO INTERIOR
 *    PARA TODOS LOS PRODUCTOS. Cada producto debe vivir en un ambiente
 *    diferente"*. Queda dicho para que nadie lo lea como un descuido.
 *
 * Copys: salen del brief. Se pasaron a versales y se cortaron a dos líneas
 * porque el sistema lo pide ("textos cortos"), sin agregar promesas nuevas.
 */

export type Pieza = "c1a" | "c1b" | "c1c" | "c1d" | "c2a" | "c2b" | "c2c";

type Ficha = {
  bg: {feed: string; story: string};
  antetitulo: string;
  titular: string[];
  bajada: string[];
  pie?: string;
  /** La fachada NO lleva placa: el letrero real del local ya dice Casablanca. */
  sinPlaca?: boolean;
  focus?: {feed: string; story: string};
  velo?: number;
  zoom?: {feed: number; story: number};
  bloqueTop?: {feed: number; story: number};
};

const amb = (sku: string) => ({
  feed: `assets/casablanca/editorial/amb_${sku}_feed.jpg`,
  story: `assets/casablanca/editorial/amb_${sku}_story.jpg`,
});

export const PIEZAS: Record<Pieza, Ficha> = {
  // ── C1 · los 4 SKU autorizados ────────────────────────────────────────────
  c1a: {
    bg: amb("natural_uv_grande"),
    antetitulo: "Piso de ingeniería",
    titular: ["ROBLE", "NATURAL UV"],
    bajada: ["La calidez del roble", "en formato amplio"],
    pie: "14/3 · 190 × 1900 mm",
    // El living es el ambiente más claro de la tanda: sin un punto más de velo
    // el titular blanco se diluye sobre el muro y la madera pálida.
    velo: 0.5,
  },
  c1b: {
    bg: amb("natural_uv_chico"),
    antetitulo: "Piso de ingeniería",
    titular: ["ROBLE", "NATURAL UV"],
    bajada: ["El mismo acabado,", "en proporción contenida"],
    pie: "10/1.2 · 167 × 1200 mm",
  },
  c1c: {
    bg: amb("aserrado"),
    antetitulo: "Piso de ingeniería",
    titular: ["ROBLE", "ASERRADO"],
    bajada: ["Textura aserrada", "y veta a la vista"],
    pie: "14/3 · 190 × 1900 mm",
  },
  c1d: {
    bg: amb("cumaru"),
    antetitulo: "Piso de ingeniería",
    titular: ["CUMARÚ"],
    bajada: ["Tabla larga y angosta,", "del formato clásico"],
    pie: "12/2 · 120 × 2130 mm",
  },

  // ── C2 · showroom Vitacura, con las fotos REALES ─────────────────────────
  c2a: {
    bg: {
      feed: "assets/casablanca/sr_fachada.jpg",       // apaisada: entra entera en 4:5
      story: "assets/casablanca/sr_direccion.jpg",    // vertical: no corta el letrero
    },
    antetitulo: "Showroom Casablanca · Vitacura",
    titular: ["VEN A CONOCER", "TU PISO", "EN PERSONA"],
    bajada: ["Juan XXIII 6359, Vitacura"],
    sinPlaca: true,
    focus: {feed: "center 58%", story: "center 46%"},
    velo: 0.4,
    bloqueTop: {feed: 0.6, story: 0.56},
  },
  c2b: {
    bg: {
      feed: "assets/casablanca/sr_interior_limpio.jpg",
      story: "assets/casablanca/sr_exhibidores.jpg",  // vertical y en más resolución
    },
    antetitulo: "Showroom Casablanca",
    titular: ["TOCA.", "COMPARA.", "ELIGE."],
    bajada: ["Descubre cada madera", "en tamaño real"],
    focus: {feed: "center 62%", story: "center 64%"},
    velo: 0.42,
  },
  c2c: {
    bg: {
      feed: "assets/casablanca/sr_direccion.jpg",
      // Misma foto vertical que c2a, pero cerrada sobre el número: sr_fachada es
      // apaisada y en 9:16 siempre parte el letrero del local por la mitad.
      story: "assets/casablanca/sr_direccion.jpg",
    },
    // Cierre del carrusel. No repite el número: la foto ya lo grita, y "Casablanca
    // cierra en WhatsApp" es la gramática de la marca (nunca una URL).
    antetitulo: "Showroom Vitacura",
    titular: ["COTIZA", "POR WHATSAPP"],
    bajada: ["Juan XXIII 6359, Vitacura"],
    pie: "+56 9 6653 5124",
    bloqueTop: {feed: 0.6, story: 0.57},
    sinPlaca: true,
    focus: {feed: "center 30%", story: "42% 52%"},
    zoom: {feed: 1, story: 1.45},
    velo: 0.44,
  },
};

/**
 * `qa` rinde la MISMA pieza con la foto apagada, sobre negro. Sirve para que
 * `scripts/casablanca-qa.py` mida la tinta real: sobre la fotografía, una
 * cortina blanca o un cielo se confunden con texto y el QA tira falsos
 * positivos (pasó en la primera corrida: acusaba "texto a 3 px del borde" que
 * era el visillo del living).
 */
export const CasablancaEditorial: React.FC<{pieza: Pieza; fmt: Fmt; qa?: boolean}> = ({
  pieza,
  fmt,
  qa = false,
}) => {
  ensureCasablancaFonts();
  const {width: w, height: h} = useVideoConfig();
  const d = PIEZAS[pieza];

  return (
    <AbsoluteFill style={{background: casablanca.colors.white}}>
      {qa ? (
        <AbsoluteFill style={{background: "#000"}} />
      ) : (
        <FotoEditorial
          src={d.bg[fmt]}
          fmt={fmt}
          velo={d.velo ?? 0.4}
          focus={d.focus?.[fmt] ?? "center 55%"}
          desde={(d.bloqueTop?.[fmt] ?? undefined) && d.bloqueTop![fmt] - 0.1}
          zoom={d.zoom?.[fmt] ?? 1}
        />
      )}

      {!d.sinPlaca && !qa && <PlacaLogo fmt={fmt} w={w} h={h} />}

      <BloqueEditorial
        fmt={fmt}
        w={w}
        h={h}
        antetitulo={d.antetitulo}
        titular={d.titular}
        bajada={d.bajada}
      />

      {d.pie ? <PieEditorial fmt={fmt} w={w} h={h} texto={d.pie} /> : null}
    </AbsoluteFill>
  );
};

/** Registro para Root.tsx: 7 piezas × 2 formatos. */
export const CB_ED = (Object.keys(PIEZAS) as Pieza[]).flatMap((pieza) =>
  (["feed", "story"] as Fmt[]).map((fmt) => ({
    id: `CbEd-${pieza}-${fmt}`,
    pieza,
    fmt,
    w: 1080,
    h: fmt === "feed" ? 1350 : 1920,
  })),
);
