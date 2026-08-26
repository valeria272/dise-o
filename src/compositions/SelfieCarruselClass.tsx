import React from "react";
import {AbsoluteFill} from "remotion";
import {ensureSelfieFonts} from "../brand/selfie";
import {FUCSIA, PILL, BODY, Asteriscos, LogoVertical, CajaBlanca, PillTag, Sparkle} from "../brand/selfieUI";

// ============================================================
// SELFIE — Carrusel educativo Selfie Class "Problema → Solución" · Sept 2026 S4
// Brief: "EDUCATIVO SELFIE CLASS / PROBLEMA - SOLUCIÓN"
// Tips PROPUESTOS (técnicos, sin claims de producto) — validar con KAM.
// ⚠️ El tag "SELFIE CLASS" va en texto: reemplazar por el logo oficial de
// Selfie Class (vive en Drive, no accesible por link) en el editable final.
// Render:
//   for i in 1 2 3 4 5; do
//     npx remotion still SelfieCarruselClass out/selfie/sept/class-0$i.png --props='{"slide":'$i'}'
//   done
// ============================================================

type Tip = {problema: string; solucion: string};

const TIPS: Tip[] = [
  {
    problema: "Frizz que aparece a mitad del día",
    solucion: "Cierra el lavado con agua fría y sella medios y puntas con sérum",
  },
  {
    problema: "El color se apaga a las pocas semanas",
    solucion: "Lava con agua tibia (no caliente) y usa shampoo sin sulfatos para teñidos",
  },
  {
    problema: "Puntas secas y quebradizas",
    solucion: "Protector térmico SIEMPRE antes del secador o la plancha",
  },
];

const TagClass: React.FC = () => (
  <div style={{position: "absolute", top: 200, left: 0, width: 2250, textAlign: "center"}}>
    <div
      style={{
        display: "inline-block",
        border: "6px solid #fff",
        borderRadius: 60,
        padding: "18px 64px 24px",
        color: "#fff",
        fontFamily: BODY,
        fontWeight: 800,
        fontSize: 60,
        letterSpacing: 10,
      }}
    >
      SELFIE CLASS
    </div>
  </div>
);

export const SelfieCarruselClass: React.FC<{slide: number}> = ({slide}) => {
  ensureSelfieFonts();

  if (slide === 1) {
    return (
      <AbsoluteFill style={{background: FUCSIA, fontFamily: BODY}}>
        <Asteriscos />
        <TagClass />
        <div style={{position: "absolute", top: 900, left: 0, width: 2250, textAlign: "center"}}>
          <div style={{color: "#fff", fontWeight: 800, fontSize: 150, lineHeight: 1.1}}>
            Problema
          </div>
        </div>
        <Sparkle x={1560} y={950} size={110} />
        <CajaBlanca top={1180} width={1300}>
          <span style={{color: FUCSIA, fontWeight: 800, fontSize: 150}}>→ Solución</span>
        </CajaBlanca>
        <div style={{position: "absolute", top: 1720, left: 325, width: 1600, textAlign: "center"}}>
          <div style={{color: "#fff", fontWeight: 600, fontSize: 62, lineHeight: 1.35}}>
            3 dramas capilares de todos los días,
            <br />
            resueltos como en el salón
          </div>
        </div>
        <PillTag top={2440}>guarda esta clase 📌</PillTag>
        <LogoVertical />
      </AbsoluteFill>
    );
  }

  if (slide >= 2 && slide <= 4) {
    const t = TIPS[slide - 2];
    return (
      <AbsoluteFill style={{background: FUCSIA, fontFamily: BODY}}>
        <Asteriscos />
        <TagClass />
        <PillTag top={620} fontSize={64}>
          problema {slide - 1} de 3
        </PillTag>
        <div style={{position: "absolute", top: 860, left: 275, width: 1700, textAlign: "center"}}>
          <div style={{color: "#fff", fontWeight: 800, fontSize: 108, lineHeight: 1.15}}>“{t.problema}”</div>
        </div>
        <CajaBlanca top={1500} width={1750}>
          <div style={{color: PILL, fontWeight: 800, fontSize: 56, letterSpacing: 6, marginBottom: 20}}>
            SOLUCIÓN
          </div>
          <div style={{color: FUCSIA, fontWeight: 800, fontSize: 84, lineHeight: 1.2}}>{t.solucion}</div>
        </CajaBlanca>
        <LogoVertical />
      </AbsoluteFill>
    );
  }

  // slide 5 — cierre
  return (
    <AbsoluteFill style={{background: FUCSIA, fontFamily: BODY}}>
      <Asteriscos />
      <TagClass />
      <Sparkle x={330} y={920} size={120} />
      <Sparkle x={1680} y={1560} size={80} />
      <div style={{position: "absolute", top: 1050, left: 0, width: 2250, textAlign: "center"}}>
        <div style={{color: "#fff", fontWeight: 800, fontSize: 120, lineHeight: 1.15}}>
          ¿Qué drama capilar
          <br />
          resolvemos en la
          <br />
          próxima clase?
        </div>
      </div>
      <PillTag top={2000}>cuéntanos en comentarios 👇</PillTag>
      <div style={{position: "absolute", top: 2280, left: 0, width: 2250, textAlign: "center"}}>
        <div style={{color: "#fff", fontWeight: 600, fontSize: 54}}>
          Todo lo que tu pelo necesita está en selfie.cl
        </div>
      </div>
      <LogoVertical />
    </AbsoluteFill>
  );
};
