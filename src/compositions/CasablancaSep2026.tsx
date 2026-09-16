import React from "react";
import {AbsoluteFill} from "remotion";
import {casablanca, ensureCasablancaFonts} from "../brand/casablanca";
import {SafeAreaAds, SAFE_ZONES} from "../components/qa/SafeAreaAds";
import {
  FondoCasablanca,
  LogoCardCasablanca,
  TitularCasablanca,
  BajadaCasablanca,
  BanderolaCasablanca,
} from "./casablanca/sistema";

/**
 * PISOS CASABLANCA — PAID SEPTIEMBRE 2026 · RONDA 2
 * Brief: "Brief Diseño Septiembre 2026 - CASABLANCA.xlsx" (Drive, 8. Septiembre).
 * C1: carrusel de LOS 4 PRODUCTOS AUTORIZADOS — mismo ambiente, cambia el piso.
 * C2: showroom Vitacura con fotos reales.
 *
 * Correcciones de la ronda 2 (ver clients/casablanca/feedback/2026-08-25-ronda2.md):
 *  · El piso del ambiente es la madera REAL de cada SKU, compuesta desde la foto
 *    oficial del cliente — la muestra y el suelo ya no pueden discrepar.
 *  · Feed pasa a 1080 × 1350 (4:5), el formato de la diseñadora.
 *  · Fuera el botón de WhatsApp dibujado: Meta ya pone el suyo.
 *  · "Desliza" sólo en feed — una story no se desliza.
 *  · En story el bloque de texto vive en el segundo cuarto y crece ~25 %.
 *  · La etiqueta gris no repite el nombre del producto: lleva la categoría y la medida.
 *  · Carrusel de showroom: abre la fachada, y ninguna imagen es inventada.
 * Reglas duras: sin precios/urgencia · texto NUNCA sobre la madera · solo estos 4 SKU.
 */

const SANS = casablanca.fonts.sans;

export type CbPieza = "c1a" | "c1b" | "c1c" | "c1d" | "c2a" | "c2b" | "c2c";
export type Fmt = "feed" | "story";

const C1_DATA: Record<string, {
  bg: string;
  tabla: string;
  look: string;
  nombre: string;
  medida: string;
  frase: string;
  indicador?: boolean;
}> = {
  c1a: {
    bg: "assets/casablanca/amb_natural_uv_grande.jpg",
    tabla: "assets/casablanca/tabla_natural_uv_grande.png",
    look: "Look Natural UV",
    nombre: "Roble Natural UV",
    medida: "14/3 · 190 × 1900 mm",
    frase: "La calidez del roble con protección UV,\nen formato amplio.",
    indicador: true,
  },
  c1b: {
    bg: "assets/casablanca/amb_natural_uv_chico.jpg",
    tabla: "assets/casablanca/tabla_natural_uv_chico.png",
    look: "Look Natural UV",
    nombre: "Roble Natural UV",
    medida: "10/1.2 · 167 × 1200 mm",
    frase: "El mismo acabado,\nen una proporción más contenida.",
  },
  c1c: {
    bg: "assets/casablanca/amb_aserrado.jpg",
    tabla: "assets/casablanca/tabla_aserrado.png",
    look: "Look Rústico",
    nombre: "Roble Aserrado",
    medida: "14/3 · 190 × 1900 mm",
    frase: "Textura aserrada y veta a la vista:\ncarácter en cada tabla.",
  },
  c1d: {
    bg: "assets/casablanca/amb_cumaru.jpg",
    tabla: "assets/casablanca/tabla_cumaru.png",
    look: "Look Tradicional",
    nombre: "Cumaru",
    // Largo variable, no 2130 (la ficha dice «2.130 LV»). Clienta, 16-09-2026.
    medida: "12/2 · 120 mm",
    // Sin «tabla corta»: «dejar solo largo variable en la primera línea» (clienta, 16-09).
    frase: "Largo variable:\nel entablado de toda la vida.",
  },
};

/** Tarjeta C1: el texto va sobre el MURO (nunca sobre la madera). */
const C1: React.FC<{k: string; fmt: Fmt; qa: boolean}> = ({k, fmt, qa}) => {
  ensureCasablancaFonts();
  const d = C1_DATA[k];
  const story = fmt === "story";
  return (
    <AbsoluteFill>
      {/* veloTop: el bloque de texto de la tarjeta vive arriba, sobre el muro claro */}
      <FondoCasablanca src={d.bg} velo={0.34} veloTop={0.34} focus={story ? "center 58%" : "center 60%"} />
      <LogoCardCasablanca story={story} />
      {/* Muestra con etiqueta gris, a la izquierda sobre el piso (gramática de carrusel) */}
      <div style={{position: "absolute", left: story ? 360 : 350, top: story ? 1215 : 835}}>
        <BanderolaCasablanca
          tabla={d.tabla}
          producto={d.medida} /* ronda 2: la etiqueta lleva la MEDIDA, no el nombre repetido */
          alto={story ? 360 : 300}
        />
      </div>
      {/* Bloque de texto sobre el muro despejado. En story vive en el segundo cuarto. */}
      <AbsoluteFill
        style={{
          alignItems: "center",
          justifyContent: "flex-start",
          paddingTop: story ? 500 : 300,
          paddingLeft: 90,
          paddingRight: 90,
          gap: story ? 30 : 22,
        }}
      >
        <div
          style={{
            font: `600 ${story ? 32 : 26}px/1 ${SANS}`,
            color: "rgba(255,255,255,.95)",
            textTransform: "uppercase",
            letterSpacing: 4.5,
            textAlign: "center",
            textShadow: "0 2px 12px rgba(0,0,0,.3)",
          }}
        >
          {d.look}
        </div>
        <TitularCasablanca texto={d.nombre} size={story ? 106 : 84} />
        <div
          style={{
            font: `400 ${story ? 33 : 27}px/1.45 ${SANS}`,
            color: "rgba(255,255,255,.92)",
            textAlign: "center",
            whiteSpace: "pre-line",
            maxWidth: story ? 780 : 700,
            textShadow: "0 2px 12px rgba(0,0,0,.3)",
            marginTop: 2,
          }}
        >
          {d.frase}
        </div>
        {/* El indicador de deslizar es del carrusel: en story no va (una story no se desliza). */}
        {d.indicador && !story ? (
          <div
            style={{
              marginTop: 10,
              font: `500 22px/1 ${SANS}`,
              color: "rgba(255,255,255,.85)",
              letterSpacing: 3,
              textTransform: "uppercase",
            }}
          >
            desliza →
          </div>
        ) : null}
      </AbsoluteFill>
      <SafeAreaAds format={story ? "story" : "feed45"} show={qa} />
    </AbsoluteFill>
  );
};

const C2_DATA: Record<string, {
  bg: string;
  bgStory?: string;
  focus?: string;
  focusStory?: string;
  etiqueta?: string;
  titulo: string;
  bajada?: string;
  bajada2?: string;
  sinLogo?: boolean;
}> = {
  // Ronda 2: abre la fachada — es la única imagen que ubica al cliente.
  // Ninguna escena inventada: las tres son fotos reales del local de Vitacura.
  c2a: {
    bg: "assets/casablanca/sr_fachada.jpg",
    focus: "center 45%",
    focusStory: "center 72%", // en 9:16 el letrero sube y el texto cae en la vereda limpia
    etiqueta: "Showroom Casablanca · Vitacura",
    titulo: "Ven a ver tu piso en persona",
    sinLogo: true, // el letrero del local ya dice Casablanca: la tarjeta duplicaba el logo
  },
  c2b: {
    // Foto real del interior con el equipo borrado (no tenemos derechos de imagen).
    bg: "assets/casablanca/sr_interior_limpio.jpg",
    focus: "center 50%",
    focusStory: "center 62%",
    titulo: "Compara texturas, tonos y formatos",
    bajada: "Muestras reales a tamaño real",
  },
  c2c: {
    bg: "assets/casablanca/sr_direccion.jpg",
    focus: "center 48%",
    focusStory: "center 74%",
    titulo: "Te esperamos",
    bajada: "Juan XXIII 6359, Vitacura",
    bajada2: "Agenda tu visita por WhatsApp +56 9 6653 5124",
  },
};

const C2: React.FC<{k: string; fmt: Fmt; qa: boolean}> = ({k, fmt, qa}) => {
  ensureCasablancaFonts();
  const d = C2_DATA[k];
  const story = fmt === "story";
  const z = story ? SAFE_ZONES.story : SAFE_ZONES.feed45;
  return (
    <AbsoluteFill>
      <FondoCasablanca
        src={story ? d.bgStory ?? d.bg : d.bg}
        velo={0.5}
        focus={(story ? d.focusStory : d.focus) ?? "center"}
      />
      {d.sinLogo ? null : <LogoCardCasablanca story={story} />}
      <AbsoluteFill
        style={{
          // Estas tres son fotos de fachada e interior: el letrero del local vive en
          // la franja media-alta, así que acá la zona limpia está ABAJO. La regla del
          // segundo cuarto es para las tarjetas de producto, donde arriba hay muro.
          alignItems: "center",
          justifyContent: "flex-end",
          paddingBottom: story ? z.bottom + 90 : z.bottom + 40,
          paddingLeft: z.left + 30,
          paddingRight: z.right + 30,
          gap: story ? 30 : 24,
        }}
      >
        {d.etiqueta ? (
          <div
            style={{
              font: `600 ${story ? 30 : 24}px/1.3 ${SANS}`,
              color: "rgba(255,255,255,.95)",
              textTransform: "uppercase",
              letterSpacing: 4,
              textAlign: "center",
              textShadow: "0 2px 12px rgba(0,0,0,.35)",
            }}
          >
            {d.etiqueta}
          </div>
        ) : null}
        <TitularCasablanca texto={d.titulo} size={story ? 84 : 78} />
        {d.bajada ? <BajadaCasablanca texto={d.bajada} size={story ? 28 : 25} width="94%" /> : null}
        {d.bajada2 ? (
          <div
            style={{
              font: `500 ${story ? 30 : 25}px/1.4 ${SANS}`,
              color: "rgba(255,255,255,.94)",
              textAlign: "center",
            }}
          >
            {d.bajada2}
          </div>
        ) : null}
      </AbsoluteFill>
      <SafeAreaAds format={story ? "story" : "feed45"} show={qa} />
    </AbsoluteFill>
  );
};

export const CasablancaSep2026: React.FC<{pieza: CbPieza; fmt: Fmt; qa?: boolean}> = ({pieza, fmt, qa = false}) =>
  pieza.startsWith("c1") ? <C1 k={pieza} fmt={fmt} qa={qa} /> : <C2 k={pieza} fmt={fmt} qa={qa} />;

export const CB_SEP26 = (["c1a", "c1b", "c1c", "c1d", "c2a", "c2b", "c2c"] as const).flatMap((pieza) =>
  (["feed", "story"] as const).map((fmt) => ({
    id: `CS26-${pieza.toUpperCase()}-${fmt === "feed" ? "Feed" : "Story"}`,
    pieza,
    fmt,
  })),
);
