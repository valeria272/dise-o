import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {ensureSelfieFonts} from "../brand/selfie";
import {FUCSIA, BODY, Asteriscos, LogoVertical, CajaBlanca, PillTag} from "../brand/selfieUI";

// ============================================================
// SELFIE — Carrusel "Infaltables de estas Fiestas" · Septiembre 2026 S3
// Brief: "CARRUSEL INFALTABLES DE ESTAS FIESTAS" (ref IG no accesible)
// Line-up: 4 OSiS+ reales de selfie.cl. COPYS PROPUESTOS — validar con KAM.
// ⚠️ Packshot Session solo existe en baja res en el e-commerce: reemplazar en editable.
// Render:
//   for i in 1 2 3 4 5; do
//     npx remotion still SelfieCarruselFiestas out/selfie/sept/fiestas-0$i.png --props='{"slide":'$i'}'
//   done
// ============================================================

type Prod = {asset: string; uso: string; nombre: string; beneficio: string};

const PRODUCTOS: Prod[] = [
  {
    asset: "assets/selfie/sept/osis-refresh-dust.png",
    uso: "el día después 🥲",
    nombre: "OSiS+ Refresh Dust",
    beneficio: "Shampoo en seco: pelo fresco y con cuerpo, sin pasar por la ducha",
  },
  {
    asset: "assets/selfie/sept/osis-flatliner.png",
    uso: "antes de la plancha 🔥",
    nombre: "OSiS+ Flatliner",
    beneficio: "Protector de calor para alisar sin sacrificar tu pelo",
  },
  {
    asset: "assets/selfie/sept/osis-session.png",
    uso: "que aguante la cueca 💃",
    nombre: "OSiS+ Session",
    beneficio: "Laca de fijación extrafuerte: el peinado dura toda la fiesta",
  },
  {
    asset: "assets/selfie/sept/osis-sparkler.png",
    uso: "brillo de fiesta ✨",
    nombre: "OSiS+ Sparkler",
    beneficio: "Spray de brillo instantáneo para el toque final",
  },
];

export const SelfieCarruselFiestas: React.FC<{slide: number}> = ({slide}) => {
  ensureSelfieFonts();

  if (slide === 1) {
    return (
      <AbsoluteFill style={{background: FUCSIA, fontFamily: BODY}}>
        <Asteriscos />
        <div style={{position: "absolute", top: 280, left: 0, width: 2250, textAlign: "center"}}>
          <div style={{color: "#fff", fontWeight: 800, fontSize: 132, lineHeight: 1.1}}>
            Los infaltables
          </div>
        </div>
        <CajaBlanca top={540} width={1500}>
          <span style={{color: FUCSIA, fontWeight: 800, fontSize: 104}}>de estas Fiestas 🇨🇱</span>
        </CajaBlanca>
        {/* line-up de los 4 productos */}
        {PRODUCTOS.map((p, i) => (
          <Img
            key={p.nombre}
            src={staticFile(p.asset)}
            style={{
              position: "absolute",
              left: 210 + i * 480,
              bottom: 560,
              width: 420,
              height: 1050,
              objectFit: "contain",
              objectPosition: "center bottom",
              transform: `rotate(${[-7, 4, -4, 7][i]}deg)`,
              filter: "drop-shadow(0 36px 54px rgba(0,0,0,0.35))",
            }}
          />
        ))}
        <PillTag top={2440}>para que tu pelo sobreviva al 18</PillTag>
        <LogoVertical />
      </AbsoluteFill>
    );
  }

  const p = PRODUCTOS[slide - 2];
  return (
    <AbsoluteFill style={{background: FUCSIA, fontFamily: BODY}}>
      <Asteriscos />
      <PillTag top={230} fontSize={76}>
        {p.uso}
      </PillTag>
      <Img
        src={staticFile(p.asset)}
        style={{
          position: "absolute",
          left: 625,
          top: 480,
          width: 1000,
          height: 1500,
          objectFit: "contain",
          filter: "drop-shadow(0 44px 66px rgba(0,0,0,0.35))",
        }}
      />
      <CajaBlanca top={2080} width={1560}>
        <span style={{color: FUCSIA, fontWeight: 800, fontSize: 92}}>{p.nombre}</span>
      </CajaBlanca>
      <div style={{position: "absolute", top: 2380, left: 325, width: 1600, textAlign: "center"}}>
        <div style={{color: "#fff", fontWeight: 600, fontSize: 56, lineHeight: 1.3}}>{p.beneficio}</div>
      </div>
      <LogoVertical />
    </AbsoluteFill>
  );
};
