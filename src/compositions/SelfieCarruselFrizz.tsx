import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {selfie, ensureSelfieFonts} from "../brand/selfie";

// ============================================================
// SELFIE — Carrusel "Frizz: ¿verano o invierno?" · Septiembre 2026 S1
// v3 — SISTEMA DE MARCA REAL: fucsia #FF007C, asteriscos, cajas blancas
// redondeadas, píldoras #FF66B0, productos grandes con borde sticker.
// Referencias: raw/selfie/grilla-agosto2026-designs (piezas S4 fucsia).
// 2250×2813 (4:5) · textos VERBATIM del brief.
// Render:
//   for i in 1 2 3 4 5; do
//     npx remotion still SelfieCarruselFrizz out/selfie/sept/frizz-0$i.png --props='{"slide":'$i'}'
//   done
// ============================================================

const FUCSIA = selfie.colors.fucsia; // #FF007C
const PILL = "#FF66B0";
const BODY = selfie.fonts.body; // Open Sans — el que usan las piezas fucsia reales

// Asterisco del logo (6 brazos, puntas redondas) — patrón decorativo de marca
const Asterisco: React.FC<{x: number; y: number; size: number; rot?: number; color?: string; opacity?: number}> = ({
  x,
  y,
  size,
  rot = 0,
  color = PILL,
  opacity = 0.55,
}) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 100 100"
    style={{position: "absolute", left: x, top: y, transform: `rotate(${rot}deg)`, opacity}}
  >
    {[0, 60, 120].map((a) => (
      <line
        key={a}
        x1={50 - 42 * Math.cos((a * Math.PI) / 180)}
        y1={50 - 42 * Math.sin((a * Math.PI) / 180)}
        x2={50 + 42 * Math.cos((a * Math.PI) / 180)}
        y2={50 + 42 * Math.sin((a * Math.PI) / 180)}
        stroke={color}
        strokeWidth="16"
        strokeLinecap="round"
      />
    ))}
  </svg>
);

const Asteriscos: React.FC = () => (
  <>
    <Asterisco x={-90} y={180} size={330} rot={15} />
    <Asterisco x={1950} y={520} size={260} rot={-20} />
    <Asterisco x={180} y={2380} size={300} rot={30} />
    <Asterisco x={1850} y={2500} size={240} rot={10} />
    <Asterisco x={1050} y={-100} size={220} rot={-15} />
  </>
);

// destello dorado de 4 puntas (piezas editoriales de la marca)
const Sparkle: React.FC<{x: number; y: number; size: number}> = ({x, y, size}) => (
  <svg width={size} height={size} viewBox="0 0 100 100" style={{position: "absolute", left: x, top: y}}>
    <path d="M50 0 L60 40 L100 50 L60 60 L50 100 L40 60 L0 50 L40 40 Z" fill={selfie.colors.sparkle} />
  </svg>
);

const LogoVertical: React.FC = () => (
  <Img
    src={staticFile("assets/selfie/logo-vertical-blanco.png")}
    style={{position: "absolute", right: 70, top: 170, height: 640}}
  />
);

// borde sticker blanco alrededor de un cutout (como el camión rosado de la marca)
export const STICKER =
  "drop-shadow(10px 0 0 #fff) drop-shadow(-10px 0 0 #fff) drop-shadow(0 10px 0 #fff) drop-shadow(0 -10px 0 #fff) drop-shadow(0 34px 44px rgba(0,0,0,0.30))";

// caja blanca redondeada con texto fucsia — el bloque central de la marca
const CajaBlanca: React.FC<{top: number; width: number; children: React.ReactNode}> = ({top, width, children}) => (
  <div style={{position: "absolute", top, left: (2250 - width) / 2, width, textAlign: "center"}}>
    <div
      style={{
        display: "inline-block",
        background: "#fff",
        borderRadius: 56,
        padding: "50px 80px 58px",
        boxShadow: "0 30px 60px rgba(0,0,0,0.18)",
      }}
    >
      {children}
    </div>
  </div>
);

const PillTag: React.FC<{top: number; children: React.ReactNode; left?: number}> = ({top, children, left}) => (
  <div
    style={{
      position: "absolute",
      top,
      ...(left === undefined ? {left: 0, width: 2250, textAlign: "center" as const} : {left}),
    }}
  >
    <div
      style={{
        display: "inline-block",
        background: PILL,
        borderRadius: 60,
        padding: "22px 70px 30px",
        color: "#fff",
        fontFamily: BODY,
        fontWeight: 800,
        fontSize: 72,
      }}
    >
      {children}
    </div>
  </div>
);

// ícono relleno blanco dentro de burbuja fucsia claro
const Burbuja: React.FC<{x: number; y: number; children: React.ReactNode}> = ({x, y, children}) => (
  <div
    style={{
      position: "absolute",
      left: x,
      top: y,
      width: 260,
      height: 260,
      borderRadius: 130,
      background: PILL,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
    }}
  >
    {children}
  </div>
);

const SolBlanco: React.FC<{size: number}> = ({size}) => (
  <svg width={size} height={size} viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="20" fill="#fff" />
    {Array.from({length: 8}).map((_, i) => {
      const a = (i * Math.PI) / 4;
      return (
        <line
          key={i}
          x1={50 + Math.cos(a) * 30}
          y1={50 + Math.sin(a) * 30}
          x2={50 + Math.cos(a) * 44}
          y2={50 + Math.sin(a) * 44}
          stroke="#fff"
          strokeWidth="9"
          strokeLinecap="round"
        />
      );
    })}
  </svg>
);

const CopoBlanco: React.FC<{size: number}> = ({size}) => (
  <svg width={size} height={size} viewBox="0 0 100 100">
    {Array.from({length: 6}).map((_, i) => {
      const a = (i * Math.PI) / 3;
      return (
        <g key={i} stroke="#fff" strokeWidth="9" strokeLinecap="round">
          <line x1="50" y1="50" x2={50 + Math.cos(a) * 42} y2={50 + Math.sin(a) * 42} />
          <line
            x1={50 + Math.cos(a) * 27 - Math.cos(a + 0.55) * 11}
            y1={50 + Math.sin(a) * 27 - Math.sin(a + 0.55) * 11}
            x2={50 + Math.cos(a) * 27}
            y2={50 + Math.sin(a) * 27}
          />
          <line
            x1={50 + Math.cos(a) * 27 - Math.cos(a - 0.55) * 11}
            y1={50 + Math.sin(a) * 27 - Math.sin(a - 0.55) * 11}
            x2={50 + Math.cos(a) * 27}
            y2={50 + Math.sin(a) * 27}
          />
        </g>
      );
    })}
  </svg>
);

const Bodegon: React.FC<{
  tituloL1: string;
  tituloDestacado: string;
  prodA: {src: string; nombre: string; detalle: string};
  prodB: {src: string; nombre: string; detalle: string};
}> = ({tituloL1, tituloDestacado, prodA, prodB}) => (
  <AbsoluteFill style={{background: FUCSIA, fontFamily: BODY}}>
    <Asteriscos />
    {/* titular blanco + destacado en caja blanca, como las piezas reales */}
    <div style={{position: "absolute", top: 200, left: 0, width: 2250, textAlign: "center"}}>
      <div style={{color: "#fff", fontWeight: 800, fontSize: 108, lineHeight: 1.12, padding: "0 200px"}}>
        {tituloL1}
      </div>
    </div>
    <CajaBlanca top={560} width={1500}>
      <span style={{color: FUCSIA, fontWeight: 800, fontSize: 92, lineHeight: 1.1, fontFamily: BODY}}>
        {tituloDestacado}
      </span>
    </CajaBlanca>
    {[
      {p: prodA, x: 170, rot: -8},
      {p: prodB, x: 1160, rot: 8},
    ].map(({p, x, rot}) => (
      <React.Fragment key={p.nombre}>
        <Img
          src={staticFile(p.src)}
          style={{
            position: "absolute",
            left: x,
            top: 1010,
            width: 920,
            height: 1150,
            objectFit: "contain",
            transform: `rotate(${rot}deg)`,
            filter: "drop-shadow(0 40px 60px rgba(0,0,0,0.35))",
          }}
        />
        <div style={{position: "absolute", left: x - 10, top: 2260, width: 940, textAlign: "center"}}>
          <div
            style={{
              display: "inline-block",
              background: "#fff",
              borderRadius: 50,
              padding: "16px 54px 22px",
              color: FUCSIA,
              fontWeight: 800,
              fontSize: 62,
            }}
          >
            {p.nombre}
          </div>
          <div style={{color: "#fff", fontWeight: 600, fontSize: 46, marginTop: 16, lineHeight: 1.25}}>
            {p.detalle}
          </div>
        </div>
      </React.Fragment>
    ))}
    <LogoVertical />
  </AbsoluteFill>
);

export const SelfieCarruselFrizz: React.FC<{slide: number}> = ({slide}) => {
  ensureSelfieFonts();

  if (slide === 1) {
    return (
      <AbsoluteFill style={{background: FUCSIA, fontFamily: BODY}}>
        <Asteriscos />
        {/* titular blanco arriba */}
        <div style={{position: "absolute", top: 210, left: 0, width: 2250, textAlign: "center"}}>
          <div style={{color: "#fff", fontWeight: 800, fontSize: 120, lineHeight: 1.1}}>
            ¿Qué es peor
            <br />
            para el frizz:
          </div>
        </div>
        <CajaBlanca top={640} width={1440}>
          <span style={{color: FUCSIA, fontWeight: 800, fontSize: 104}}>¿el verano o el invierno?</span>
        </CajaBlanca>
        {/* chica con frizz — generada SOBRE el fucsia y con el fondo empalmado
            al #FF007C exacto: cero recorte, los crespos quedan intactos */}
        <Img
          src={staticFile("assets/selfie/sept/chica-frizz-fucsia.png")}
          style={{
            position: "absolute",
            left: 405,
            bottom: 0,
            width: 1440,
            height: 1720,
            objectFit: "cover",
            objectPosition: "center bottom",
          }}
        />
        {/* sol a la izquierda, copo a la derecha, en burbujas de marca */}
        <Burbuja x={230} y={1520}>
          <SolBlanco size={170} />
        </Burbuja>
        <Burbuja x={1720} y={1520}>
          <CopoBlanco size={170} />
        </Burbuja>
        <LogoVertical />
      </AbsoluteFill>
    );
  }

  if (slide === 2) {
    return (
      <AbsoluteFill style={{background: "#22303B", fontFamily: BODY}}>
        <Img
          src={staticFile("assets/selfie/sept/frizz-s2-invierno.png")}
          style={{position: "absolute", inset: 0, width: 2250, height: 2813, objectFit: "cover"}}
        />
        <div
          style={{
            position: "absolute",
            bottom: 0,
            left: 0,
            width: 2250,
            height: 1300,
            background: "linear-gradient(180deg, rgba(15,22,28,0) 0%, rgba(15,22,28,0.85) 70%)",
          }}
        />
        <Sparkle x={1620} y={1780} size={110} />
        <Sparkle x={1760} y={1930} size={64} />
        <div style={{position: "absolute", top: 1930, left: 0, width: 2250, textAlign: "center"}}>
          <div style={{color: "#fff", fontWeight: 800, fontSize: 128, lineHeight: 1.12, padding: "0 180px"}}>
            Spoiler: el invierno
            <br />
            también te traiciona
          </div>
        </div>
        <PillTag top={2400}>frizz, estática y puntas secas</PillTag>
        <LogoVertical />
      </AbsoluteFill>
    );
  }

  if (slide === 3) {
    return (
      <Bodegon
        tituloL1="Si tu pelo es liso o grueso,"
        tituloDestacado="esto es para ti"
        prodA={{
          src: "assets/selfie/sept/keratin-alpha.png",
          nombre: "Keratin Alpha Sleek",
          detalle: "Serie Expert · tratamiento efecto liso",
        }}
        prodB={{
          src: "assets/selfie/sept/bc-frizz-away.png",
          nombre: "BC Frizz Away",
          detalle: "Bonacure · cabello grueso o rebelde",
        }}
      />
    );
  }

  if (slide === 4) {
    return (
      <Bodegon
        tituloL1="Y si buscas algo para"
        tituloDestacado="el día a día o todo en uno"
        prodA={{
          src: "assets/selfie/sept/olix-hydration.png",
          nombre: "Olix Pro Hydration",
          detalle: "Acondicionador · controla el frizz a diario",
        }}
        prodB={{
          src: "assets/selfie/sept/uniq-one.png",
          nombre: "Uniq One",
          detalle: "Revlon Professional · sin enjuague, todo en uno",
        }}
      />
    );
  }

  // slide 5 — resultado + CTA
  return (
    <AbsoluteFill style={{background: FUCSIA, fontFamily: BODY}}>
      <Img
        src={staticFile("assets/selfie/sept/frizz-s5-modelo.png")}
        style={{position: "absolute", inset: 0, width: 2250, height: 2813, objectFit: "cover"}}
      />
      {/* velo fucsia de marca sobre la foto */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: "linear-gradient(180deg, rgba(255,0,124,0) 45%, rgba(255,0,124,0.88) 88%)",
        }}
      />
      <Sparkle x={380} y={1700} size={100} />
      <Sparkle x={520} y={1860} size={60} />
      <CajaBlanca top={1980} width={1760}>
        <span style={{color: FUCSIA, fontWeight: 800, fontSize: 104, lineHeight: 1.12}}>
          Frizz cero, brillo total
          <br />→ en selfie.cl
        </span>
      </CajaBlanca>
      <PillTag top={2500}>guarda este post, te va a servir</PillTag>
      <LogoVertical />
    </AbsoluteFill>
  );
};
