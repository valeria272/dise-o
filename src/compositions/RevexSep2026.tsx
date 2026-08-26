import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {revex, ensureRevexFonts} from "../brand/revex";
import {SafeAreaAds, SAFE_ZONES} from "../components/qa/SafeAreaAds";
import {
  FondoRevex,
  LogoBlockRevex,
  TitularRevex,
  BulletLineRevex,
  BajadaRevex,
} from "./revex/sistema";

/**
 * GRUPO REVEX — PAID SEPTIEMBRE 2026 · RONDA 2
 * Brief: "Brief Diseño Septiembre 2026 - REVEX.xlsx" (Drive, 9. Septiembre).
 * R1 concurso · R2 outlet (rojo pleno) · R3 Temuco · R4 Las Condes (serie).
 * Textos LITERALES del brief — no inventar copys ni cifras.
 *
 * Correcciones de la ronda 2 (ver clients/revex/feedback/2026-08-25-ronda2.md):
 *  · El logo va SIEMPRE sobre el cuadro rojo pegado al borde superior central.
 *    Deroga el "logo blanco suelto" del lineamiento 8 del brief — el brief manda
 *    el QUÉ, el sistema manda el CÓMO. Única excepción: el outlet, que es rojo
 *    pleno y un cuadro rojo sobre rojo no existiría.
 *  · Rojo en cuadros, nunca en textos.
 *  · Bloque de texto siempre centrado, y con aire respecto del logo.
 *  · Titular de dos líneas como máximo.
 *  · Nunca dos bloques con cuadro pegados: si el titular ya lleva barra roja, el
 *    dato de abajo va en negrita sin caja.
 *  · Fuera el botón de WhatsApp dibujado: Meta ya pone el suyo.
 *  · En story el bloque de texto vive en el segundo cuarto.
 *  · Feed a 1080 × 1350 (4:5).
 */

const C = revex.colors;
const F = revex.fonts.display;

export type RevexPieza = "r1" | "r2" | "r3" | "r4";
export type Fmt = "feed" | "story";

// ─── R1 · CONCURSO ───
const R1: React.FC<{fmt: Fmt; qa: boolean}> = ({fmt, qa}) => {
  ensureRevexFonts();
  const story = fmt === "story";
  const z = story ? SAFE_ZONES.story : SAFE_ZONES.feed45;
  const sc = story ? 1.0 : 0.94;
  return (
    <AbsoluteFill>
      {/* Ronda 2: showroom claro con muestras, minimalista — ya no el render moody */}
      <FondoRevex
        src={story ? "assets/revex/sep/concurso_story.png" : "assets/revex/sep/concurso_feed.png"}
        velo={0.55}
        focus="center 55%"
      />
      <LogoBlockRevex story={story} />
      <AbsoluteFill
        style={{
          alignItems: "center",
          justifyContent: story ? "flex-start" : "center",
          paddingTop: story ? 540 : 300, // aire bajo el logo
          paddingLeft: z.left + 26,
          paddingRight: z.right + 26,
          paddingBottom: story ? 0 : z.bottom,
        }}
      >
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            textAlign: "center",
            gap: 28 * sc,
            maxWidth: 900,
          }}
        >
          <div style={{font: `700 ${32 * sc}px/1 ${F}`, color: "#fff", letterSpacing: 6, textTransform: "uppercase"}}>
            Concurso
          </div>
          {/* Máximo dos líneas */}
          <div
            style={{
              font: `800 ${story ? 46 : 44}px/1.16 ${F}`,
              color: "#fff",
              textTransform: "uppercase",
              whiteSpace: "pre-line",
            }}
          >
            {"¡Gana una alfombra\ndimensionada personalizada!"}
          </div>
          <div style={{font: `400 ${29 * sc}px/1.5 ${F}`, color: "#fff", whiteSpace: "pre-line"}}>
            Todas tus compras realizadas <b>del 21 de agosto al 25 de septiembre</b>
            <br />
            en Gruporevex Las Condes Design participan automáticamente del sorteo.
          </div>
          <div style={{display: "flex", alignItems: "center", gap: 16, flexWrap: "wrap", justifyContent: "center"}}>
            <span style={{font: `400 ${28 * sc}px/1.3 ${F}`, color: "#fff"}}>Av. Las Condes 9765, Las Condes</span>
            {/* El rojo va en el cuadro, nunca en el texto */}
            <span
              style={{
                display: "inline-block",
                background: C.barRed,
                color: "#fff",
                padding: "10px 22px",
                font: `700 ${26 * sc}px/1 ${F}`,
              }}
            >
              PISO 1, LOCAL 112
            </span>
          </div>
          <div style={{font: `700 ${32 * sc}px/1.35 ${F}`, color: "#fff", marginTop: 4}}>
            ¡No pierdas la oportunidad de ganar! Te esperamos
          </div>
          <div style={{font: `400 ${19 * sc}px/1.4 ${F}`, color: "rgba(255,255,255,.78)"}}>
            Consulta los términos y condiciones del concurso en www.gruporevex.cl
          </div>
        </div>
      </AbsoluteFill>
      <SafeAreaAds format={story ? "story" : "feed45"} show={qa} />
    </AbsoluteFill>
  );
};

// ─── R2 · OUTLET (rojo pleno, recuadro blanco, franja amarilla — según brief) ───
const R2: React.FC<{fmt: Fmt; qa: boolean}> = ({fmt, qa}) => {
  ensureRevexFonts();
  const story = fmt === "story";
  return (
    <AbsoluteFill style={{background: C.blockRed}}>
      {/* Excepción del sistema: sobre rojo pleno el logo va suelto, pegado arriba */}
      <Img
        src={staticFile(revex.logo)}
        style={{position: "absolute", top: 34, left: "50%", transform: "translateX(-50%)", width: story ? 190 : 148}}
      />
      <AbsoluteFill
        style={{
          alignItems: "center",
          justifyContent: "center",
          // Ronda 2: aire bajo el logo — el titular venía pegado a él
          paddingTop: story ? 420 : 300,
          paddingBottom: story ? 380 : 210,
          paddingLeft: 70,
          paddingRight: 70,
          gap: story ? 42 : 30,
        }}
      >
        <div style={{font: `800 ${story ? 44 : 38}px/1.3 ${F}`, color: "#fff", textAlign: "center", textTransform: "uppercase"}}>
          ¡Remate total de revestimientos!
          <br />
          Más de 300 productos
        </div>
        <div style={{background: "#fff", padding: story ? "46px 90px" : "40px 84px", textAlign: "center"}}>
          <div style={{font: `800 ${story ? 150 : 108}px/1.02 ${F}`, color: C.barRed, textTransform: "uppercase"}}>
            Hasta
            <br />
            85% OFF
          </div>
        </div>
        <div style={{font: `700 ${story ? 36 : 33}px/1.3 ${F}`, color: "#fff", textAlign: "center", textTransform: "uppercase", letterSpacing: 1.5}}>
          Precios de liquidación · Patio Outlet
        </div>
        <div
          style={{
            background: C.outletYellow,
            color: "#111",
            font: `700 ${story ? 30 : 27}px/1 ${F}`,
            padding: "16px 34px",
            textTransform: "uppercase",
            letterSpacing: 1,
            whiteSpace: "nowrap",
          }}
        >
          Productos seleccionados | Liquidación final
        </div>
        <div style={{font: `400 ${story ? 32 : 29}px/1.5 ${F}`, color: "#fff", textAlign: "center"}}>
          <b>VENTA EXCLUSIVA EN LUIS OLEA 010, QUILICURA</b>
          <br />
          WhatsApp <b>+56 9 8902 8227</b>
        </div>
      </AbsoluteFill>
      <SafeAreaAds format={story ? "story" : "feed45"} show={qa} />
    </AbsoluteFill>
  );
};

// ─── R3/R4 · SUCURSALES (serie refresh: misma estructura, cambian foto y datos) ───
const Sucursal: React.FC<{
  fmt: Fmt;
  qa: boolean;
  foto: {feed: string; story: string};
  focus?: string;
  focusStory?: string;
  antetitulo: string;
  linea1: string;
  barra: string;
  direccion: string;
  bajada1: string;
  bajada1b: string;
  horario: string;
}> = ({fmt, qa, foto, focus, focusStory, antetitulo, linea1, barra, direccion, bajada1, bajada1b, horario}) => {
  const story = fmt === "story";
  const z = story ? SAFE_ZONES.story : SAFE_ZONES.feed45;
  return (
    <AbsoluteFill>
      <FondoRevex src={story ? foto.story : foto.feed} velo={0.62} focus={(story ? focusStory : focus) ?? focus ?? "center"} />
      <LogoBlockRevex story={story} />
      <AbsoluteFill
        style={{
          alignItems: "center",
          // Ronda 2: en story el bloque sube al segundo cuarto
          justifyContent: story ? "flex-start" : "flex-end",
          paddingTop: story ? 560 : 0,
          paddingBottom: story ? 0 : z.bottom + 30,
          paddingLeft: z.left,
          paddingRight: z.right,
          gap: story ? 36 : 30,
        }}
      >
        <BulletLineRevex texto={antetitulo} size={story ? 32 : 30} />
        <TitularRevex linea1={linea1} linea2={barra} size={story ? 47 : 44} />
        {/* El titular ya lleva la barra roja: el dato va en negrita, sin cuadro */}
        <div
          style={{
            font: `700 ${story ? 34 : 32}px/1.3 ${F}`,
            color: "#fff",
            textAlign: "center",
            textShadow: "0 2px 14px rgba(0,0,0,.45)",
          }}
        >
          {direccion}
        </div>
        <BajadaRevex
          size={story ? 29 : 27}
          width="86%"
          lineas={[
            [{t: bajada1}],
            [{t: bajada1b, bold: true}],
            ...(horario ? [[{t: horario}]] : []),
          ]}
        />
      </AbsoluteFill>
      <SafeAreaAds format={story ? "story" : "feed45"} show={qa} />
    </AbsoluteFill>
  );
};

export const RevexSep2026: React.FC<{pieza: RevexPieza; fmt: Fmt; qa?: boolean}> = ({pieza, fmt, qa = false}) => {
  switch (pieza) {
    case "r1":
      return <R1 fmt={fmt} qa={qa} />;
    case "r2":
      return <R2 fmt={fmt} qa={qa} />;
    case "r3":
      return (
        <Sucursal
          fmt={fmt}
          qa={qa}
          // El local REAL de Temuco, sacado del video oficial del showroom
          // (`rvx_storie_temuco.mp4`, 2160 × 3840, dice en pantalla «Visítanos en
          // Reyes Católicos 1550») — ver scripts/revex-temuco-fondo.py. Ya no hace
          // falta el placeholder ni el collage que rechazó Paulina.
          foto={{feed: "assets/revex/sep/temuco_local_feed.jpg", story: "assets/revex/sep/temuco_local_story.jpg"}}
          focus="center 62%"
          focusStory="center 58%"
          antetitulo="Grupo Revex · Temuco"
          linea1="TE ESPERAMOS EN"
          barra="REYES CATÓLICOS 1550"
          direccion="Segundo piso de Ebema"
          bajada1="Más espacio, mejor atención y la misma"
          bajada1b="calidad de siempre en pisos y revestimientos."
          horario="Lun y mar 9:30–18:00 · Mié a vie 9:30–17:00"
        />
      );
    case "r4":
      return (
        <Sucursal
          fmt={fmt}
          qa={qa}
          foto={{feed: "assets/revex/sep/lcd_fachada.jpg", story: "assets/revex/sep/lcd_fachada.jpg"}}
          focus="center 22%"
          focusStory="center 74%" /* en 9:16 el letrero sube y deja libre el segundo cuarto */
          antetitulo="Grupo Revex · Las Condes Design"
          linea1="TODO PARA RENOVAR TUS ESPACIOS,"
          barra="EN UN SOLO LUGAR"
          direccion="Av. Las Condes 9765 · Piso 1, Local 112"
          bajada1="Pisos, porcelanatos y revestimientos."
          bajada1b="Lun a vie 10:00–19:00 · Sáb 10:00–14:30"
          horario=""
        />
      );
  }
};

export const REVEX_SEP26 = (["r1", "r2", "r3", "r4"] as const).flatMap((pieza) =>
  (["feed", "story"] as const).map((fmt) => ({
    id: `RS26-${pieza.toUpperCase()}-${fmt === "feed" ? "Feed" : "Story"}`,
    pieza,
    fmt,
  })),
);
