import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

// ============================================================
// GRUPO REVEX — Septiembre 2026
// Brief: "Brief Diseño Septiembre 2026 - REVEX.xlsx" (Drive 9. Septiembre)
// 4 piezas × 2 formatos = 8 artes · feed 1080×1080 · story 1080×1920
//   R1 Concurso alfombra (LCD)   R2 Patio Outlet — remate total
//   R3 Sucursal Temuco (refresh) R4 Sucursal Las Condes Design (refresh)
//
// SISTEMA: el mismo del carrusel de laminados aprobado
// (src/compositions/RevexLaminadosCarrusel.tsx). No inventar otro.
//   · foto de ambiente FULL-BLEED + velo suave hacia abajo
//   · bloque rojo del logo colgando del borde superior, centrado
//   · TODO el texto centrado, en la mitad inferior
//   · titular en MAYÚSCULAS Montserrat 800 + la línea clave en BARRA ROJA
//   · bajada de dos líneas: bold + regular
//   · dato duro en cápsula de borde blanco
//   · CTA en cápsula negra redondeada
//   · gruporevex.cl chico al pie
// ============================================================

const RED = "#D31A2B";
const YELLOW = "#FFD200";

// Fuente auto-hospedada (patrón RevexLaminadosCarrusel — sin delayRender)
const injectFonts = () => {
  if (typeof document === "undefined") return;
  if (document.getElementById("revex-sep-fonts")) return;
  const style = document.createElement("style");
  style.id = "revex-sep-fonts";
  style.textContent = `
    @font-face {
      font-family: 'Montserrat';
      src: url(${JSON.stringify(staticFile("assets/fonts/Montserrat.ttf"))}) format('truetype');
      font-weight: 100 900;
      font-style: normal;
      font-display: block;
    }
  `;
  document.head.appendChild(style);
  document.fonts.load("800 100px Montserrat").catch(() => {});
};
injectFonts();

const FONT = "'Montserrat', 'Helvetica Neue', sans-serif";

export type Fmt = "feed" | "story";
const isStory = (f: Fmt) => f === "story";

// Historias: 250 px de zona segura arriba, tercio inferior libre (brief).
const STORY_LOGO_TOP = 250;
const STORY_FONDO = 1270;

const SOMBRA = "0 4px 18px rgba(0,0,0,0.45)";

// ---------- piezas del sistema ----------

/**
 * Foto de fondo. `banda` sirve para las fotos apaisadas en 9:16: la foto
 * nítida ocupa la banda superior y el resto es la misma foto desenfocada,
 * para que la pieza se lea como una sola imagen y el local no salga recortado.
 */
const Fondo: React.FC<{src: string; veil?: number; banda?: number; pos?: string}> = ({
  src,
  veil = 0.2,
  banda,
  pos = "center",
}) => {
  // en modo banda el desenfoque ya aporta oscuridad: el velo va más suave
  const v = banda ? veil * 0.45 : veil;
  return (
  <>
    {banda ? (
      <>
        <AbsoluteFill style={{overflow: "hidden"}}>
          <Img
            src={staticFile(src)}
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              filter: "blur(56px) brightness(0.66) saturate(0.95)",
              transform: "scale(1.25)",
            }}
          />
        </AbsoluteFill>
        <div
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            width: 1080,
            height: banda,
            overflow: "hidden",
          }}
        >
          <Img
            src={staticFile(src)}
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              objectPosition: pos,
            }}
          />
          <AbsoluteFill
            style={{
              background:
                "linear-gradient(180deg, rgba(0,0,0,0) 62%, rgba(0,0,0,0.22) 84%, rgba(0,0,0,0.55) 100%)",
            }}
          />
        </div>
      </>
    ) : (
      <Img
        src={staticFile(src)}
        style={{
          position: "absolute",
          width: "100%",
          height: "100%",
          objectFit: "cover",
          objectPosition: pos,
        }}
      />
    )}
    <AbsoluteFill
      style={{
        background: `linear-gradient(180deg, rgba(0,0,0,0.04) 0%, rgba(0,0,0,${
          v * 0.5
        }) 30%, rgba(0,0,0,${v}) 55%, rgba(0,0,0,${v + 0.12}) 100%)`,
      }}
    />
  </>
  );
};

/** Bloque rojo del logo colgando del borde superior, centrado. */
const LogoBlock: React.FC<{fmt: Fmt}> = ({fmt}) => (
  <div
    style={{
      position: "absolute",
      top: isStory(fmt) ? STORY_LOGO_TOP : 0,
      left: "50%",
      transform: "translateX(-50%)",
      width: 190,
      height: 185,
      backgroundColor: RED,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      boxShadow: "0 6px 24px rgba(0,0,0,0.25)",
    }}
  >
    <Img src={staticFile("assets/revex/logo_blanco.png")} style={{width: 138, height: "auto"}} />
  </div>
);

/** Logo blanco suelto, centrado (para el fondo rojo del outlet). */
const LogoBlanco: React.FC<{width: number}> = ({width}) => (
  <Img
    src={staticFile("assets/revex/logo_blanco.png")}
    style={{width, height: "auto", display: "block"}}
  />
);

const Titular: React.FC<{
  linea1: React.ReactNode;
  barra: string;
  fmt: Fmt;
  tit?: [number, number];
  bar?: [number, number];
}> = ({linea1, barra, fmt, tit = [56, 60], bar = [50, 52]}) => {
  const story = isStory(fmt);
  return (
    <>
      <div
        style={{
          color: "#fff",
          fontSize: story ? tit[1] : tit[0],
          fontWeight: 800,
          letterSpacing: 1,
          textAlign: "center",
          lineHeight: 1.08,
          textShadow: SOMBRA,
        }}
      >
        {linea1}
      </div>
      <div
        style={{
          marginTop: story ? 12 : 10,
          backgroundColor: RED,
          color: "#fff",
          fontSize: story ? bar[1] : bar[0],
          fontWeight: 800,
          letterSpacing: 1,
          padding: story ? "12px 30px" : "10px 26px",
          textAlign: "center",
          whiteSpace: "nowrap",
        }}
      >
        {barra}
      </div>
    </>
  );
};

const Bajada: React.FC<{bold: string; regular: string; fmt: Fmt}> = ({bold, regular, fmt}) => {
  const story = isStory(fmt);
  return (
    <div
      style={{
        marginTop: story ? 40 : 42,
        color: "#fff",
        textAlign: "center",
        lineHeight: 1.34,
        textShadow: "0 3px 14px rgba(0,0,0,0.5)",
      }}
    >
      <div style={{fontSize: story ? 36 : 34, fontWeight: 700}}>{bold}</div>
      <div style={{fontSize: story ? 34 : 32, fontWeight: 400}}>{regular}</div>
    </div>
  );
};

/** Cápsula de borde blanco: el recurso del sistema para el dato duro. */
const Capsula: React.FC<{children: React.ReactNode; fmt: Fmt}> = ({children, fmt}) => {
  const story = isStory(fmt);
  return (
    <div
      style={{
        marginTop: story ? 34 : 34,
        border: "4px solid #fff",
        borderRadius: 20,
        backgroundColor: "rgba(0,0,0,0.18)",
        color: "#fff",
        fontSize: story ? 29 : 27,
        fontWeight: 500,
        letterSpacing: 0.6,
        padding: story ? "16px 38px" : "15px 34px",
        textAlign: "center",
        lineHeight: 1.35,
      }}
    >
      {children}
    </div>
  );
};

const Cta: React.FC<{texto: string; fmt: Fmt}> = ({texto, fmt}) => {
  const story = isStory(fmt);
  return (
    <div
      style={{
        marginTop: story ? 34 : 36,
        backgroundColor: "rgba(15,15,15,0.92)",
        color: "#fff",
        fontSize: story ? 37 : 36,
        fontWeight: 500,
        padding: story ? "20px 54px" : "19px 50px",
        borderRadius: 16,
        letterSpacing: 0.5,
      }}
    >
      {texto}
    </div>
  );
};

const Pie: React.FC<{texto: string; fmt: Fmt}> = ({texto, fmt}) => {
  const story = isStory(fmt);
  return (
    <div
      style={{
        marginTop: story ? 26 : 26,
        color: "rgba(255,255,255,0.88)",
        fontSize: story ? 26 : 23,
        fontWeight: 500,
        letterSpacing: 1,
        textAlign: "center",
        textShadow: "0 2px 8px rgba(0,0,0,0.5)",
      }}
    >
      {texto}
    </div>
  );
};

/** Columna centrada de texto, anclada por su borde inferior. */
const Columna: React.FC<{fmt: Fmt; fondo: number; children: React.ReactNode}> = ({
  fmt,
  fondo,
  children,
}) => (
  <div
    style={{
      position: "absolute",
      bottom: (isStory(fmt) ? 1920 : 1080) - fondo,
      width: "100%",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      padding: "0 60px",
      boxSizing: "border-box",
    }}
  >
    {children}
  </div>
);

// ============================================================
// R1 · CONCURSO — gana una alfombra dimensionada personalizada
// ============================================================

const R1: React.FC<{fmt: Fmt}> = ({fmt}) => {
  const story = isStory(fmt);
  return (
    <AbsoluteFill style={{fontFamily: FONT, backgroundColor: "#111"}}>
      <Fondo
        src={
          story ? "assets/revex/sep/concurso_story.png" : "assets/revex/sep/concurso_feed.png"
        }
        veil={0.44}
      />
      <LogoBlock fmt={fmt} />

      <Columna fmt={fmt} fondo={story ? STORY_FONDO : 1016}>
        <div
          style={{
            color: "#fff",
            fontSize: story ? 34 : 30,
            fontWeight: 800,
            letterSpacing: 9,
            marginBottom: story ? 20 : 16,
            textShadow: SOMBRA,
          }}
        >
          CONCURSO
        </div>

        <Titular
          linea1="¡GANA UNA ALFOMBRA"
          barra="DIMENSIONADA PERSONALIZADA!"
          fmt={fmt}
          tit={[58, 66]}
          bar={[41, 47]}
        />

        <Bajada
          bold="Del 21 de agosto al 25 de septiembre"
          regular="todas tus compras en Grupo Revex Las Condes Design participan del sorteo."
          fmt={fmt}
        />

        <Capsula fmt={fmt}>AV. LAS CONDES 9765 · PISO 1, LOCAL 112</Capsula>

        <Cta texto="Escríbenos por WhatsApp" fmt={fmt} />

        <Pie texto="Consulta los términos y condiciones en gruporevex.cl" fmt={fmt} />
      </Columna>
    </AbsoluteFill>
  );
};

// ============================================================
// R2 · PATIO OUTLET — remate total (fondo rojo, sin fotografía)
// ============================================================

const R2: React.FC<{fmt: Fmt}> = ({fmt}) => {
  const story = isStory(fmt);
  return (
    <AbsoluteFill style={{fontFamily: FONT, backgroundColor: RED}}>
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(120% 90% at 50% 0%, rgba(255,255,255,0.10) 0%, rgba(255,255,255,0) 62%)",
        }}
      />

      <div
        style={{
          position: "absolute",
          top: story ? STORY_LOGO_TOP : 46,
          left: "50%",
          transform: "translateX(-50%)",
        }}
      >
        <LogoBlanco width={story ? 158 : 148} />
      </div>

      <Columna fmt={fmt} fondo={story ? 1280 : 1030}>
        <div
          style={{
            color: "#fff",
            fontSize: story ? 40 : 35,
            fontWeight: 800,
            letterSpacing: 0.6,
            textAlign: "center",
            lineHeight: 1.18,
          }}
        >
          ¡REMATE TOTAL DE REVESTIMIENTOS!
          <br />
          MÁS DE 300 PRODUCTOS
        </div>

        {/* la cifra: lo más grande, en recuadro blanco */}
        <div
          style={{
            marginTop: story ? 26 : 26,
            backgroundColor: "#fff",
            padding: story ? "22px 50px" : "20px 46px",
            boxShadow: "0 14px 40px rgba(0,0,0,0.22)",
          }}
        >
          <div
            style={{
              color: RED,
              fontSize: story ? 112 : 108,
              fontWeight: 800,
              lineHeight: 0.94,
              letterSpacing: -3,
              textAlign: "center",
            }}
          >
            HASTA
            <br />
            85% OFF
          </div>
        </div>

        <div
          style={{
            marginTop: story ? 24 : 22,
            color: "#fff",
            fontSize: story ? 34 : 31,
            fontWeight: 700,
            letterSpacing: 1.4,
            textAlign: "center",
          }}
        >
          PRECIOS DE LIQUIDACIÓN · PATIO OUTLET
        </div>

        {/* franja amarilla: recurso propio de la línea de outlet */}
        <div
          style={{
            marginTop: story ? 22 : 18,
            width: "100%",
            backgroundColor: YELLOW,
            color: "#111",
            fontSize: story ? 27 : 24,
            fontWeight: 800,
            letterSpacing: 1.2,
            padding: story ? "16px 0" : "13px 0",
            textAlign: "center",
          }}
        >
          PRODUCTOS SELECCIONADOS &nbsp;|&nbsp; LIQUIDACIÓN FINAL
        </div>

        <Capsula fmt={fmt}>
          VENTA EXCLUSIVA EN LUIS OLEA 010, QUILICURA
          <br />
          <span style={{fontWeight: 800}}>WhatsApp +56 9 8902 8227</span>
        </Capsula>

        <Cta texto="Cotiza por WhatsApp" fmt={fmt} />

        <Pie texto="No incluye despacho ni instalación · gruporevex.cl" fmt={fmt} />
      </Columna>
    </AbsoluteFill>
  );
};

// ============================================================
// R3 / R4 · SUCURSALES — misma estructura y tipografía (regla del brief)
// ============================================================

type SucursalData = {
  foto: string;
  posFeed: string;
  posStory: string;
  titulo1: string;
  barra: string;
  bold: string;
  regular: string;
  capsula: React.ReactNode;
};

const SUCURSALES: Record<"temuco" | "condes", SucursalData> = {
  temuco: {
    foto: "assets/revex/sep/temuco_fachada.jpg",
    posFeed: "center 40%",
    posStory: "center 30%",
    titulo1: "TE ESPERAMOS EN TEMUCO",
    barra: "REYES CATÓLICOS 1550",
    bold: "Segundo piso de Ebema",
    regular: "Más espacio, mejor atención y la misma calidad de siempre.",
    capsula: (
      <>
        LUNES Y MARTES 9:30 A 18:00 HRS
        <br />
        MIÉRCOLES, JUEVES Y VIERNES 9:30 A 17:00
      </>
    ),
  },
  condes: {
    foto: "assets/revex/sep/lcd_fachada.jpg",
    posFeed: "center 42%",
    posStory: "center 26%",
    titulo1: "TODO PARA RENOVAR\nTUS ESPACIOS,",
    barra: "EN UN SOLO LUGAR",
    bold: "Pisos, porcelanatos y revestimientos",
    regular: "Lunes a viernes 10:00–19:00 · sábado 10:00–14:30.",
    capsula: <>AV. LAS CONDES 9765 · PISO 1, LOCAL 112</>,
  },
};

const Sucursal: React.FC<{fmt: Fmt; local: "temuco" | "condes"}> = ({fmt, local}) => {
  const story = isStory(fmt);
  const d = SUCURSALES[local];

  return (
    <AbsoluteFill style={{fontFamily: FONT, backgroundColor: "#111"}}>
      <Fondo
        src={d.foto}
        veil={0.58}
        pos={story ? d.posStory : d.posFeed}
        banda={story ? 700 : undefined}
      />
      <LogoBlock fmt={fmt} />

      <Columna fmt={fmt} fondo={story ? STORY_FONDO : 1016}>
        <Titular
          linea1={d.titulo1.split("\n").map((l, i) => (
            <React.Fragment key={l}>
              {i > 0 ? <br /> : null}
              {l}
            </React.Fragment>
          ))}
          barra={d.barra}
          fmt={fmt}
        />
        <Bajada bold={d.bold} regular={d.regular} fmt={fmt} />
        <Capsula fmt={fmt}>{d.capsula}</Capsula>
        <Cta texto="Escríbenos por WhatsApp" fmt={fmt} />
        <Pie texto="gruporevex.cl" fmt={fmt} />
      </Columna>
    </AbsoluteFill>
  );
};

// ============ ENTRY ============

export type RevexSepProps = {
  pieza: "R1" | "R2" | "R3" | "R4";
  fmt: Fmt;
};

export const RevexSepPieza: React.FC<RevexSepProps> = ({pieza, fmt}) => {
  injectFonts();
  if (pieza === "R1") return <R1 fmt={fmt} />;
  if (pieza === "R2") return <R2 fmt={fmt} />;
  if (pieza === "R3") return <Sucursal fmt={fmt} local="temuco" />;
  return <Sucursal fmt={fmt} local="condes" />;
};

export const REVEX_SEP_PIEZAS: {id: string; pieza: RevexSepProps["pieza"]; fmt: Fmt}[] = [
  {id: "RvxSep-R1-Feed", pieza: "R1", fmt: "feed"},
  {id: "RvxSep-R1-Story", pieza: "R1", fmt: "story"},
  {id: "RvxSep-R2-Feed", pieza: "R2", fmt: "feed"},
  {id: "RvxSep-R2-Story", pieza: "R2", fmt: "story"},
  {id: "RvxSep-R3-Feed", pieza: "R3", fmt: "feed"},
  {id: "RvxSep-R3-Story", pieza: "R3", fmt: "story"},
  {id: "RvxSep-R4-Feed", pieza: "R4", fmt: "feed"},
  {id: "RvxSep-R4-Story", pieza: "R4", fmt: "story"},
];
