import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {ensureSelfieFonts} from "../brand/selfie";
import {FUCSIA, BODY, Asteriscos, LogoVertical, CajaBlanca, PillTag} from "../brand/selfieUI";

// ============================================================
// SELFIE — Carrusel interactivo "Elige un emoji" · Septiembre 2026 S1
// Brief (verbatim portada): "ELIGE UN EMOJI Y DESCUBRE LO QUE TU PELITO NECESITA"
// Slides 2-5: propuesta de mapeo emoji → necesidad → producto REAL de selfie.cl
// (mapeo propio, marcado para revisión de la KAM — la ref Pinterest no era accesible)
// Render:
//   for i in 1 2 3 4 5; do
//     npx remotion still SelfieCarruselEmoji out/selfie/sept/emoji-0$i.png --props='{"slide":'$i'}'
//   done
// ============================================================

type Opcion = {
  emoji: string;
  necesidad: string;
  detalle: string;
  producto: string;
  productoDetalle: string;
  asset: string;
};

const OPCIONES: Opcion[] = [
  {
    emoji: "💧",
    necesidad: "hidratación",
    detalle: "pelo seco u opaco que pide agua",
    producto: "Olix Pro Hydration",
    productoDetalle: "Acondicionador · hidratación diaria",
    asset: "assets/selfie/sept/olix-hydration.png",
  },
  {
    emoji: "🥵",
    necesidad: "control del frizz",
    detalle: "humedad, calor y pelitos rebeldes",
    producto: "BC Frizz Away",
    productoDetalle: "Bonacure · tratamiento anti-frizz",
    asset: "assets/selfie/sept/bc-frizz-away.png",
  },
  {
    emoji: "✨",
    necesidad: "efecto liso brillante",
    detalle: "alisado parejo con brillo espejo",
    producto: "Keratin Alpha Sleek",
    productoDetalle: "Serie Expert · tratamiento efecto liso",
    asset: "assets/selfie/sept/keratin-alpha.png",
  },
  {
    emoji: "🙃",
    necesidad: "un todo en uno",
    detalle: "cero tiempo, todos los beneficios",
    producto: "Uniq One",
    productoDetalle: "Revlon Professional · sin enjuague",
    asset: "assets/selfie/sept/uniq-one.png",
  },
];

const BurbujaEmoji: React.FC<{x: number; y: number; emoji: string; size?: number}> = ({x, y, emoji, size = 420}) => (
  <div
    style={{
      position: "absolute",
      left: x,
      top: y,
      width: size,
      height: size,
      borderRadius: size / 2,
      background: "#fff",
      boxShadow: "0 26px 50px rgba(0,0,0,0.20)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      fontSize: size * 0.55,
    }}
  >
    {emoji}
  </div>
);

export const SelfieCarruselEmoji: React.FC<{slide: number}> = ({slide}) => {
  ensureSelfieFonts();

  if (slide === 1) {
    return (
      <AbsoluteFill style={{background: FUCSIA, fontFamily: BODY}}>
        <Asteriscos />
        <div style={{position: "absolute", top: 260, left: 0, width: 2250, textAlign: "center"}}>
          <div style={{color: "#fff", fontWeight: 800, fontSize: 130, lineHeight: 1.12}}>
            Elige un emoji
          </div>
        </div>
        <CajaBlanca top={520} width={1560}>
          <span style={{color: FUCSIA, fontWeight: 800, fontSize: 96, lineHeight: 1.1}}>
            y descubre lo que
            <br />
            tu pelito necesita
          </span>
        </CajaBlanca>
        {/* los 4 emojis en burbujas blancas, grilla 2×2 */}
        <BurbujaEmoji x={440} y={1260} emoji="💧" />
        <BurbujaEmoji x={1390} y={1260} emoji="🥵" />
        <BurbujaEmoji x={440} y={1850} emoji="✨" />
        <BurbujaEmoji x={1390} y={1850} emoji="🙃" />
        <PillTag top={2480}>comenta el tuyo 👇</PillTag>
        <LogoVertical />
      </AbsoluteFill>
    );
  }

  const o = OPCIONES[slide - 2];
  return (
    <AbsoluteFill style={{background: FUCSIA, fontFamily: BODY}}>
      <Asteriscos />
      <BurbujaEmoji x={925} y={170} emoji={o.emoji} size={400} />
      <div style={{position: "absolute", top: 660, left: 0, width: 2250, textAlign: "center"}}>
        <div style={{color: "#fff", fontWeight: 800, fontSize: 100, lineHeight: 1.1}}>
          Tu pelito necesita
        </div>
      </div>
      <CajaBlanca top={810} width={1500}>
        <span style={{color: FUCSIA, fontWeight: 800, fontSize: 104}}>{o.necesidad}</span>
      </CajaBlanca>
      <div style={{position: "absolute", top: 1120, left: 0, width: 2250, textAlign: "center"}}>
        <div style={{color: "#fff", fontWeight: 600, fontSize: 58}}>{o.detalle}</div>
      </div>
      <Img
        src={staticFile(o.asset)}
        style={{
          position: "absolute",
          left: 625,
          top: 1290,
          width: 1000,
          height: 1080,
          objectFit: "contain",
          filter: "drop-shadow(0 40px 60px rgba(0,0,0,0.35))",
        }}
      />
      <PillTag top={2450} fontSize={66}>
        {o.producto}
      </PillTag>
      <div style={{position: "absolute", top: 2600, left: 0, width: 2250, textAlign: "center"}}>
        <div style={{color: "#fff", fontWeight: 600, fontSize: 46}}>{o.productoDetalle}</div>
      </div>
      <LogoVertical />
    </AbsoluteFill>
  );
};
