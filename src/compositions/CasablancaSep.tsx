import React from "react";
import {AbsoluteFill, useVideoConfig} from "remotion";
import {casablanca, ensureCasablancaFonts} from "../brand/casablanca";
import {BloqueSep, Desliza, FondoSep, TarjetaLogo, type Fmt} from "./casablanca/sep";

/**
 * PISOS CASABLANCA — PAID SEPTIEMBRE 2026
 * =============================================================================
 * Contenido: `Brief Diseño Septiembre 2026 - CASABLANCA.xlsx` (Drive, carpeta
 * "8. Septiembre"). Los textos van como los escribió el brief; las versales son
 * del sistema gráfico, no una reescritura.
 *
 * Sistema gráfico: `casablanca/sep.tsx`, sacado de las piezas reales de la
 * diseñadora que acompañan al brief (carpeta de referencias del Drive).
 *
 * C1 · carrusel de los 4 productos autorizados — MISMO AMBIENTE, cambia la tabla.
 * C2 · carrusel del showroom de Vitacura — fotos reales del local.
 *
 * Sólo estos 4 SKU. El brief lo dice dos veces y la clienta lo pidió textual:
 * "NO MOSTRAR O PUBLICAR OTROS PRODUCTOS QUE NO SEAN ESTOS POR FAVOR."
 */

export type Pieza = "c1a" | "c1b" | "c1c" | "c1d" | "c2a" | "c2b" | "c2c";

type Ficha = {
  bg: {feed: string; story: string};
  etiqueta?: string;
  titulo: string[];
  bajada?: string[];
  medida?: string;
  cta?: string;
  desliza?: boolean;
  focus?: {feed: string; story: string};
  velo?: number;
  centro?: {feed: number; story: number};
};

// La story usa LA MISMA foto que el feed, en encuadre vertical. Es la única
// forma de garantizar que el carrusel vertical sea el mismo ambiente y la misma
// tabla: ni el expand de Freepik ni Mystic con structure_reference respetan el
// 9:16 (ver scripts/casablanca-sep-pipeline.py, paso 4).
const amb = (sku: string) => ({
  feed: `assets/casablanca/sep/amb_${sku}_feed.jpg`,
  story: `assets/casablanca/sep/amb_${sku}_feed.jpg`,
});

const foto = (n: string) => ({
  feed: `assets/casablanca/sep/${n}.jpg`,
  story: `assets/casablanca/sep/${n}.jpg`,
});

export const PIEZAS: Record<Pieza, Ficha> = {
  // ── C1 · los 4 productos autorizados ─────────────────────────────────────
  c1a: {
    bg: amb("natural_uv_grande"),
    etiqueta: "Look Natural UV",
    titulo: ["Roble Natural UV"],
    bajada: ["La calidez del roble con protección UV,", "en formato amplio"],
    medida: "14/3 · 190 × 1900 mm",
    cta: "Cotiza por WhatsApp",
    desliza: true, // lineamiento nº7: indicador de deslizar en la tarjeta 1
  },
  c1b: {
    bg: amb("natural_uv_chico"),
    etiqueta: "Look Natural UV",
    titulo: ["Roble Natural UV"],
    bajada: ["El mismo acabado,", "en una proporción más contenida"],
    medida: "10/1.2 · 167 × 1200 mm",
    cta: "Cotiza por WhatsApp",
  },
  c1c: {
    bg: amb("aserrado"),
    etiqueta: "Look Rústico",
    titulo: ["Roble Aserrado"],
    bajada: ["Textura aserrada y veta a la vista:", "carácter en cada tabla"],
    medida: "14/3 · 190 × 1900 mm",
    cta: "Cotiza por WhatsApp",
  },
  c1d: {
    bg: amb("cumaru"),
    etiqueta: "Look Tradicional",
    titulo: ["Cumaru"],
    // Largo variable, no 2130 (la ficha dice «2.130 LV»). Clienta, 16-09-2026.
    // Sin «tabla corta»: la clienta pidió «dejar solo largo variable en la primera
    // línea» el mismo 16-09.
    bajada: ["Largo variable:", "el entablado de toda la vida"],
    medida: "12/2 · 120 mm",
    cta: "Cotiza por WhatsApp",
  },

  // ── C2 · showroom Vitacura, fotos reales ─────────────────────────────────
  // El brief describe cada tarjeta: 1 vista general del espacio · 2 el interior
  // por dentro, la zona donde se compara · 3 cierre con una vista del local.
  c2a: {
    bg: foto("sr_interior"),
    etiqueta: "Showroom Casablanca · Vitacura",
    titulo: ["Ven a ver tu piso", "en persona"],
    desliza: true,
    focus: {feed: "center 45%", story: "center 45%"},
    velo: 0.34,
  },
  c2b: {
    bg: foto("sr_muestras"),
    titulo: ["Compara texturas,", "tonos y formatos"],
    bajada: ["Con asesoría de nuestro equipo"],
    focus: {feed: "center 62%", story: "center 55%"},
    velo: 0.36,
  },
  c2c: {
    bg: {
      feed: "assets/casablanca/sep/sr_local.jpg",
      story: "assets/casablanca/sep/sr_local_v.jpg", // vertical: no parte el letrero
    },
    titulo: ["Te esperamos"],
    bajada: ["Juan XXIII 6359, Vitacura"],
    medida: "Agenda tu visita por WhatsApp · +56 9 6653 5124",
    focus: {feed: "center 38%", story: "center 30%"},
    // El letrero del local vive en la franja media: el texto baja al pavimento,
    // que es la zona limpia de esta foto.
    centro: {feed: 0.74, story: 0.66},
    velo: 0.38,
  },
};

export const CasablancaSep: React.FC<{pieza: Pieza; fmt: Fmt; qa?: boolean}> = ({
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
        <FondoSep src={d.bg[fmt]} velo={d.velo ?? 0.3} focus={d.focus?.[fmt] ?? "center 55%"} />
      )}

      {!qa && <TarjetaLogo w={w} />}

      <BloqueSep
        w={w}
        h={h}
        fmt={fmt}
        centro={d.centro?.[fmt]}
        etiqueta={d.etiqueta}
        titulo={d.titulo}
        bajada={d.bajada}
        medida={d.medida}
        cta={d.cta}
      />

      {/* Una story no se desliza: el indicador va sólo en feed. */}
      {d.desliza && fmt === "feed" ? <Desliza w={w} h={h} /> : null}
    </AbsoluteFill>
  );
};

/** Registro para Root.tsx. Feed 1080×1080 — la medida que pide el brief. */
export const CB_SEP = (Object.keys(PIEZAS) as Pieza[]).flatMap((pieza) =>
  (["feed", "story"] as Fmt[]).map((fmt) => ({
    id: `CbSep-${pieza}-${fmt}`,
    pieza,
    fmt,
    w: 1080,
    h: fmt === "feed" ? 1080 : 1920,
  })),
);
