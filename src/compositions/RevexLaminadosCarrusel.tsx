import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

// ============================================================
// GRUPO REVEX — Carrusel Pisos Laminados AMBRAS y VIENA
// 6 slides 1080x1350 (4:5) — sistema visual oficial del cliente:
// rojo #D31A2B, Montserrat (sustituto de Gotham), foto ambiente
// full-bleed, barra roja de highlight, ficha de producto con
// etiqueta roja plegada y cápsula de specs con borde blanco.
// ============================================================

const RED = "#D31A2B";
const RED_DARK = "#9E1420"; // pliegue de la etiqueta

// Fuente auto-hospedada (patrón TierraCalmaReel — sin delayRender)
const injectFonts = () => {
  if (typeof document === "undefined") return;
  if (document.getElementById("revex-fonts")) return;
  const style = document.createElement("style");
  style.id = "revex-fonts";
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

type ProductData = {
  bg: string;
  plank: string;
  frase1: string; // línea bold
  frase2: string; // línea light
  linea: string; // PISO LAMINADO
  nombre: string; // AMBRAS HAYA
  medidas: string;
  specs: string[];
};

const PRODUCTS: Record<string, ProductData> = {
  haya: {
    bg: "assets/revex/bg2_haya.png",
    plank: "assets/revex/plank_haya.png",
    frase1: "Tono cálido y natural,",
    frase2: "inspirado en la madera de haya.",
    linea: "PISO LAMINADO",
    nombre: "AMBRAS HAYA",
    medidas: "1.215 x 195 x 8,3 mm",
    specs: [
      "terminación biselada • instalación flotante",
      "AC4 • uso interior • 8 tablas por caja.",
    ],
  },
  perla: {
    bg: "assets/revex/bg3_perla.png",
    plank: "assets/revex/plank_perla.png",
    frase1: "Tono claro y luminoso,",
    frase2: "ideal para espacios modernos.",
    linea: "PISO LAMINADO",
    nombre: "AMBRAS PERLA",
    medidas: "1.215 x 195 x 8,3 mm",
    specs: [
      "terminación biselada • instalación flotante",
      "AC4 • uso interior • 8 tablas por caja.",
    ],
  },
  nude: {
    bg: "assets/revex/bg4_nude.png",
    plank: "assets/revex/plank_nude.png",
    frase1: "Tono neutro y suave",
    frase2: "que combina con todo.",
    linea: "PISO LAMINADO",
    nombre: "AMBRAS NUDE",
    medidas: "1.215 x 195 x 8,3 mm",
    specs: [
      "terminación biselada • instalación flotante",
      "AC4 • uso interior • 8 tablas por caja.",
    ],
  },
  eucalipto: {
    bg: "assets/revex/bg5_eucalipto.png",
    plank: "assets/revex/plank_eucalipto.png",
    frase1: "Tono natural con carácter",
    frase2: "para tu hogar.",
    linea: "PISO LAMINADO",
    nombre: "VIENA EUCALIPTO",
    medidas: "1.215 x 195 x 8,3 mm",
    specs: ["terminación recta • uso interior", "8 tablas por caja."],
  },
};

// --- Bloque de logo rojo (esquina / centro superior) ---
const LogoBlock: React.FC<{centered?: boolean}> = ({centered}) => (
  <div
    style={{
      position: "absolute",
      top: 0,
      ...(centered ? {left: "50%", transform: "translateX(-50%)"} : {left: 104}),
      width: 190,
      height: 185,
      backgroundColor: RED,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      boxShadow: "0 6px 24px rgba(0,0,0,0.25)",
    }}
  >
    <Img
      src={staticFile("assets/revex/logo_blanco.png")}
      style={{width: 138, height: "auto"}}
    />
  </div>
);

// --- Fondo con foto + velo para legibilidad ---
const Background: React.FC<{src: string; veil?: number}> = ({src, veil = 0.18}) => (
  <>
    <Img
      src={staticFile(src)}
      style={{
        position: "absolute",
        width: "100%",
        height: "100%",
        objectFit: "cover",
      }}
    />
    <AbsoluteFill
      style={{
        background: `linear-gradient(180deg, rgba(0,0,0,0.05) 0%, rgba(0,0,0,${veil}) 55%, rgba(0,0,0,${veil + 0.22}) 100%)`,
      }}
    />
  </>
);

// ============ SLIDE 1 — PORTADA ============
const SlidePortada: React.FC = () => (
  <AbsoluteFill style={{fontFamily: FONT, backgroundColor: "#111"}}>
    <Background src="assets/revex/bg1_portada.png" veil={0.22} />
    <LogoBlock centered />

    <div
      style={{
        position: "absolute",
        top: 700,
        width: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <div
        style={{
          color: "#fff",
          fontSize: 74,
          fontWeight: 800,
          letterSpacing: 1,
          textShadow: "0 4px 18px rgba(0,0,0,0.45)",
        }}
      >
        RENUEVA TUS PISOS,
      </div>
      <div
        style={{
          marginTop: 10,
          backgroundColor: RED,
          color: "#fff",
          fontSize: 55,
          fontWeight: 800,
          letterSpacing: 1,
          padding: "10px 26px",
        }}
      >
        TRANSFORMA TUS ESPACIOS
      </div>

      <div
        style={{
          marginTop: 88,
          color: "#fff",
          fontSize: 41,
          fontWeight: 400,
          textAlign: "center",
          lineHeight: 1.35,
          textShadow: "0 3px 14px rgba(0,0,0,0.5)",
        }}
      >
        Conoce nuestra línea de pisos laminados
        <br />
        <span style={{fontWeight: 800}}>AMBRAS y VIENA</span>
      </div>

      <div
        style={{
          marginTop: 92,
          backgroundColor: "rgba(15,15,15,0.92)",
          color: "#fff",
          fontSize: 38,
          fontWeight: 500,
          padding: "20px 54px",
          borderRadius: 16,
          letterSpacing: 0.5,
        }}
      >
        Desliza y descubre&nbsp;&nbsp;⟶
      </div>
    </div>
  </AbsoluteFill>
);

// ============ SLIDES 2–5 — PRODUCTO ============
const SlideProducto: React.FC<{data: ProductData}> = ({data}) => (
  <AbsoluteFill style={{fontFamily: FONT, backgroundColor: "#111"}}>
    <Background src={data.bg} veil={0.2} />
    <LogoBlock />

    {/* Frase */}
    <div
      style={{
        position: "absolute",
        top: 742,
        width: "100%",
        textAlign: "center",
        color: "#fff",
        textShadow: "0 3px 14px rgba(0,0,0,0.5)",
        lineHeight: 1.3,
      }}
    >
      <div style={{fontSize: 47, fontWeight: 700}}>{data.frase1}</div>
      <div style={{fontSize: 44, fontWeight: 400}}>{data.frase2}</div>
    </div>

    {/* Ficha: tabla + etiqueta roja plegada */}
    <div style={{position: "absolute", top: 918, left: 100, width: 880, height: 210}}>
      <div
        style={{
          position: "absolute",
          inset: 0,
          borderRadius: 24,
          border: "6px solid #fff",
          overflow: "hidden",
          boxShadow: "0 10px 30px rgba(0,0,0,0.35)",
        }}
      >
        <Img
          src={staticFile(data.plank)}
          style={{width: "100%", height: "100%", objectFit: "cover"}}
        />
      </div>

      {/* Etiqueta roja sobresaliente */}
      <div
        style={{
          position: "absolute",
          top: -52,
          right: -10,
          width: 400,
          backgroundColor: RED,
          color: "#fff",
          textAlign: "center",
          padding: "22px 20px 24px",
          boxShadow: "0 8px 24px rgba(0,0,0,0.3)",
        }}
      >
        <div style={{fontSize: 26, fontWeight: 400, letterSpacing: 2}}>{data.linea}</div>
        <div style={{fontSize: 30, fontWeight: 800, letterSpacing: 1.5, marginTop: 6}}>
          {data.nombre}
        </div>
        <div
          style={{
            marginTop: 14,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            gap: 10,
            fontSize: 29,
            fontWeight: 500,
          }}
        >
          <span style={{fontSize: 24}}>⟵</span>
          {data.medidas}
          <span style={{fontSize: 24}}>⟶</span>
        </div>
        {/* pliegue */}
        <div
          style={{
            position: "absolute",
            right: -0.5,
            bottom: -14,
            width: 0,
            height: 0,
            borderTop: `14px solid ${RED_DARK}`,
            borderRight: "14px solid transparent",
          }}
        />
      </div>
    </div>

    {/* Cápsula de specs */}
    <div
      style={{
        position: "absolute",
        top: 1178,
        left: 100,
        width: 880,
        borderRadius: 20,
        border: "4px solid #fff",
        color: "#fff",
        textAlign: "center",
        fontSize: 34,
        fontWeight: 400,
        lineHeight: 1.45,
        padding: "16px 20px",
        backgroundColor: "rgba(0,0,0,0.12)",
        textShadow: "0 2px 8px rgba(0,0,0,0.4)",
      }}
    >
      {data.specs.map((s) => (
        <div key={s}>{s}</div>
      ))}
    </div>
  </AbsoluteFill>
);

// ============ SLIDE 6 — CIERRE ============
const SlideCierre: React.FC = () => (
  <AbsoluteFill style={{fontFamily: FONT, backgroundColor: "#111"}}>
    <Background src="assets/revex/bg6_cierre.png" veil={0.3} />

    <div
      style={{
        position: "absolute",
        top: 370,
        width: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <Img
        src={staticFile("assets/revex/logo_blanco.png")}
        style={{width: 300, height: "auto", filter: "drop-shadow(0 4px 16px rgba(0,0,0,0.35))"}}
      />

      <div
        style={{
          marginTop: 88,
          color: "#fff",
          fontSize: 88,
          fontWeight: 800,
          letterSpacing: 2,
          textShadow: "0 4px 18px rgba(0,0,0,0.45)",
        }}
      >
        ¿CUÁL ES TU
      </div>
      <div
        style={{
          marginTop: 14,
          backgroundColor: RED,
          color: "#fff",
          fontSize: 88,
          fontWeight: 800,
          letterSpacing: 2,
          padding: "8px 44px",
        }}
      >
        TONO IDEAL?
      </div>

      <div
        style={{
          marginTop: 84,
          backgroundColor: "rgba(15,15,15,0.92)",
          color: "#fff",
          fontSize: 40,
          fontWeight: 500,
          padding: "22px 60px",
          borderRadius: 16,
          letterSpacing: 0.5,
        }}
      >
        Cotízalo por WhatsApp
      </div>

      <div
        style={{
          marginTop: 66,
          color: "rgba(255,255,255,0.85)",
          fontSize: 30,
          fontWeight: 500,
          letterSpacing: 1,
          textShadow: "0 2px 8px rgba(0,0,0,0.4)",
        }}
      >
        gruporevex.cl
      </div>
    </div>
  </AbsoluteFill>
);

// ============ ENTRY ============
export type RevexSlideProps = {
  slide: "portada" | "haya" | "perla" | "nude" | "eucalipto" | "cierre";
};

export const RevexLaminadosSlide: React.FC<RevexSlideProps> = ({slide}) => {
  injectFonts();
  if (slide === "portada") return <SlidePortada />;
  if (slide === "cierre") return <SlideCierre />;
  return <SlideProducto data={PRODUCTS[slide]} />;
};
