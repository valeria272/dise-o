import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {selfie, ensureSelfieFonts} from "../brand/selfie";

// ============================================================
// SELFIE — Banner web "Semana del peluquer@" (réplica de sistema)
// 2001×686 · fondo fucsia #FF007C · packshots reales del e-commerce
// Renderizar: npx remotion still SelfieBannerSemanaPeluquero out/selfie/banner-semana-peluquero.png
// ============================================================

export const PILL = selfie.colors.fucsiaClaro; // #FF64AC medido; el original usa #FF66B0
const BG = selfie.colors.fucsia; // #FF007C

const Tubo: React.FC<{
  x: number;
  y: number;
  h: number;
  rot: number;
}> = ({x, y, h, rot}) => (
  // NUNCA scaleX(-1): espejar el packshot deja "Majirel" al revés
  <Img
    src={staticFile("assets/selfie/majirel-tubo.png")}
    style={{
      position: "absolute",
      left: x,
      top: y,
      height: h,
      transform: `rotate(${rot}deg)`,
      filter: "drop-shadow(0 14px 22px rgba(0,0,0,0.28))",
    }}
  />
);

export const SelfieBannerSemanaPeluquero: React.FC = () => {
  ensureSelfieFonts();
  const openSans = selfie.fonts.body;
  return (
    <AbsoluteFill style={{background: BG, overflow: "hidden", fontFamily: openSans}}>
      {/* pliegue diagonal sutil entre las dos mitades */}
      <div
        style={{
          position: "absolute",
          left: "40%",
          top: -80,
          width: 260,
          height: 900,
          background: "linear-gradient(100deg, rgba(0,0,0,0.16), rgba(0,0,0,0) 55%)",
          transform: "rotate(8deg)",
        }}
      />

      {/* píldora del título, pegada al borde superior izquierdo */}
      <div
        style={{
          position: "absolute",
          left: 0,
          top: 40,
          background: "#FF66B0",
          borderRadius: "0 44px 44px 0",
          padding: "16px 56px 20px 48px",
        }}
      >
        <span style={{color: "#fff", fontWeight: 800, fontSize: 46}}>Semana del peluquer@</span>
      </div>

      {/* mochila real (cutout del material del cliente) */}
      <Img
        src={staticFile("assets/selfie/mochila.png")}
        style={{
          position: "absolute",
          left: 70,
          top: 165,
          height: 420,
          filter: "drop-shadow(0 18px 26px rgba(0,0,0,0.30))",
        }}
      />

      {/* bloque de texto de la mochila */}
      <div style={{position: "absolute", left: 445, top: 185, width: 540, textAlign: "center"}}>
        <div
          style={{
            display: "inline-block",
            background: "#FF66B0",
            borderRadius: 48,
            padding: "8px 40px 12px",
            marginBottom: 14,
          }}
        >
          <span style={{color: "#fff", fontWeight: 700, fontSize: 54}}>compra sobre</span>
        </div>
        <div style={{color: "#fff", fontWeight: 800, fontSize: 116, lineHeight: 1.0, letterSpacing: -2}}>
          $100.000
        </div>
        <div style={{color: "#fff", fontWeight: 700, fontSize: 44, lineHeight: 1.15, marginTop: 12}}>
          y llévate una mochila
          <br />
          Selfie de regalo
        </div>
      </div>

      {/* tubos Majirel reales (packshot selfie.cl) cayendo en V */}
      <Tubo x={1020} y={140} h={300} rot={-34} />
      <Tubo x={1120} y={125} h={300} rot={28} />
      <Tubo x={1035} y={245} h={300} rot={-52} />
      <Tubo x={1150} y={230} h={280} rot={46} />
      {/* caja de la promo de tinturas */}
      <div
        style={{
          position: "absolute",
          left: 1195,
          top: 300,
          background: "#FF66B0",
          borderRadius: 20,
          padding: "18px 46px 22px",
          textAlign: "center",
        }}
      >
        <span style={{color: "#fff", fontWeight: 800, fontSize: 56, lineHeight: 1.12, display: "block"}}>
          4 tinturas y la
          <br />
          5ta a $1
        </span>
      </div>

      {/* legal — regla dura del cliente */}
      <div
        style={{
          position: "absolute",
          left: 1100,
          top: 510,
          width: 580,
          textAlign: "center",
          color: "#fff",
          fontWeight: 400,
          fontSize: 26,
          lineHeight: 1.3,
        }}
      >
        Válido hasta el 31 de agosto. Promociones
        <br />
        no acumulables y sujetas a stock.
      </div>

      {/* tubo grande protagonista — encima de la caja, como el original */}
      <Tubo x={1560} y={85} h={510} rot={14} />

      {/* globo $1 */}
      <div
        style={{
          position: "absolute",
          left: 1730,
          top: 225,
          background: "#FF8FC2",
          borderRadius: 22,
          padding: "6px 26px 10px",
        }}
      >
        <span style={{color: "#fff", fontWeight: 800, fontSize: 52, fontStyle: "italic"}}>$1</span>
        <div
          style={{
            position: "absolute",
            left: 24,
            bottom: -16,
            width: 0,
            height: 0,
            borderLeft: "14px solid transparent",
            borderRight: "14px solid transparent",
            borderTop: "18px solid #FF8FC2",
          }}
        />
      </div>

      {/* logo vertical SELFI3* al borde derecho */}
      <Img
        src={staticFile("assets/selfie/logo-vertical-blanco.png")}
        style={{position: "absolute", right: 26, top: 60, height: 566}}
      />
    </AbsoluteFill>
  );
};
