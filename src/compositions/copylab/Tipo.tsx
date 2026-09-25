// ============================================================================
// TIPO — ronda tipográfica publicitaria (24-09-2026)
// ----------------------------------------------------------------------------
// Feedback: «la tipografía se siente editorial/arte, no publicitaria; le falta
// pegada, contraste y sistema. Una palabra manda. El resto acompaña.»
//
// TRES NIVELES FIJOS (MASTER/03, actualizado este día):
//   TITULAR    Archivo variable · wght 900 · wdth 62–72 · tracking −0,03 ·
//              interlineado 0,8. Archivo Narrow llega a 700 y eso era lo que
//              se leía «liviano».
//   SECUNDARIO Inter 500, chico, neutro.
//   ACENTO     Plex Mono (metadata) o DM Serif Italic, sólo en palabras puntuales.
// El layout NO se repite: cada pieza compone distinto.
// ============================================================================
import React from "react";
import {AbsoluteFill, staticFile} from "remotion";
import {C, asegurarFuentes, VOZ, ancho} from "../../brand/copylab/sistema";
import {Foto, Grano, Velo} from "../../brand/copylab/lienzo";

const A = "assets/copylab/tipo/";
const B = "assets/copylab/posts12/";
const abs = (s: React.CSSProperties): React.CSSProperties => ({position: "absolute", ...s});

/** Nivel 1 — el titular que grita. */
const tit = (size: number, color: string, wdth = 66, extra?: React.CSSProperties): React.CSSProperties => ({
  fontFamily: VOZ.impacto, fontVariationSettings: ancho(wdth, 900), fontWeight: 900,
  fontSize: size, lineHeight: 0.8, letterSpacing: "-0.03em", textTransform: "uppercase",
  color, whiteSpace: "nowrap", ...extra,
});
/** Nivel 2 — secundario limpio. */
const sec = (size: number, color: string, extra?: React.CSSProperties): React.CSSProperties => ({
  fontFamily: VOZ.funcional, fontWeight: 500, fontSize: size, lineHeight: 1.25,
  letterSpacing: "-0.005em", color, ...extra,
});
/** Nivel 3 — acento mono. */
const mono = (color: string, size = 19, extra?: React.CSSProperties): React.CSSProperties => ({
  fontFamily: VOZ.data, fontSize: size, lineHeight: 1.45, letterSpacing: "0.14em",
  textTransform: "uppercase", color, ...extra,
});

/** Homografía: lleva un rectángulo w×h a los cuatro puntos de la foto
 *  (TL, TR, BR, BL). Así el titular queda PEGADO al letrero, con su perspectiva. */
const homografia = (w: number, h: number, q: number[][]) => {
  const [[x0, y0], [x1, y1], [x2, y2], [x3, y3]] = q;
  const dx1 = x1 - x2, dx2 = x3 - x2, dy1 = y1 - y2, dy2 = y3 - y2;
  const sx = x0 - x1 + x2 - x3, sy = y0 - y1 + y2 - y3;
  const den = dx1 * dy2 - dx2 * dy1;
  const g = (sx * dy2 - dx2 * sy) / den, hh = (dx1 * sy - sx * dy1) / den;
  const a = x1 - x0 + g * x1, b = x3 - x0 + hh * x3, c = x0;
  const d = y1 - y0 + g * y1, e = y3 - y0 + hh * y3, f = y0;
  // de coordenadas unitarias a píxeles del rectángulo fuente
  const m = [a / w, d / w, 0, g / w, b / h, e / h, 0, hh / h, 0, 0, 1, 0, c, f, 0, 1];
  return `matrix3d(${m.join(",")})`;
};

// 01 — el diario trae el antetítulo; «VENDEN MÁS.» es el golpe, impreso en la portada.
const T01 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={A + "p01-kicker.jpg"} grado="crudo" />
    {/* La tinta va DEBAJO de los dedos: máscara de piel medida sobre la foto. */}
    <div style={abs({left: 0, top: 0, width: 1080, height: 1350, mixBlendMode: "multiply", opacity: 0.95,
      WebkitMaskImage: `url(${staticFile(A + "p01-mascara-dedos.png")})`, maskImage: `url(${staticFile(A + "p01-mascara-dedos.png")})`,
      WebkitMaskSize: "100% 100%", maskSize: "100% 100%"})}>
      <div style={abs({left: 0, top: 0, width: 1080, height: 1350, clipPath: "polygon(240px 380px, 876px 380px, 876px 1196px, 240px 1196px)"})}>
        <div style={abs({left: 252, top: 520, ...tit(218, "#141414", 60)})}>Venden</div>
        <div style={abs({left: 248, top: 706, ...tit(338, C.rosa, 58)})}>más.</div>
      </div>
    </div>
    <Grano op={0.12} />
  </AbsoluteFill>
);

// 02 — inquieta: «VIRAL» se sale del cuadro y se invierte sobre el papel.
const T02 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={A + "p02-blanca.jpg"} grado="crudo" />
    <div style={abs({left: 64, top: 70, ...sec(44, C.blanco, {mixBlendMode: "difference"})})}>Hagámoslo</div>
    <div style={abs({left: 56, top: 150, ...tit(300, C.blanco, 70, {mixBlendMode: "difference"})})}>más</div>
    <div style={abs({left: 30, top: 470, transform: "skewX(-12deg)", transformOrigin: "0 100%",
      ...tit(560, C.blanco, 62, {mixBlendMode: "difference", letterSpacing: "-0.045em"})})}>viral</div>
    <Grano op={0.12} />
  </AbsoluteFill>
);

// 07 — un comando: la palabra ocupa el ancho y se corta en los bordes.
const T07 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={B + "p07.jpg"} grado="crudo" />
    <Velo desde="abajo" fuerza={0.55} corte={0.55} />
    <div style={abs({left: -26, bottom: 36, ...tit(388, C.offwhite, 62, {letterSpacing: "-0.04em"})})}>Delete</div>
    <div style={abs({left: 60, top: 60, ...mono("rgba(242,244,246,0.8)", 17)})}>Nuestra herramienta favorita.</div>
    <Grano op={0.12} />
  </AbsoluteFill>
);

// 13 — la respuesta, impresa en el letrero vacío. Seca. Sin rosa.
const Q13 = [[137, 172], [933, 199], [933, 588], [122, 515]];
const T13 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={A + "p13-limpio.jpg"} grado="crudo" />
    <div style={abs({left: 0, top: 0, width: 1000, height: 460, transformOrigin: "0 0",
      transform: homografia(1000, 460, Q13), mixBlendMode: "multiply"})}>
      <div style={abs({left: 44, top: 40, ...tit(150, "#16181A", 66)})}>Mejor</div>
      <div style={abs({left: 30, top: 170, ...tit(300, "#16181A", 64)})}>no.</div>
    </div>
    <Grano op={0.1} />
  </AbsoluteFill>
);

// 11 — el cartel es vernacular; el sistema Copywriters sólo cataloga y explica.
const T11 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={B + "p11-llaves.jpg"} grado="crudo" />
    <Velo desde="abajo" fuerza={0.75} corte={0.6} />
    <div style={abs({left: 60, bottom: 196, ...tit(96, C.offwhite, 68)})}>Nadie lo firmó.</div>
    <div style={abs({left: 62, bottom: 116, width: 620, ...sec(27, "rgba(242,244,246,0.86)")})}>Servicio, promesa y plazo en cinco palabras.</div>
    <div style={abs({left: 62, bottom: 60, ...mono("rgba(242,244,246,0.6)", 15)})}>Nº004 · Santiago · recreación</div>
    <Grano op={0.12} />
  </AbsoluteFill>
);

// 08 — caso: titular de sistema, datos sobrios, el trabajo sigue siendo el protagonista.
const T08 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={B + "p08-santagota.jpg"} grado="crudo" />
    <Velo desde="abajo" fuerza={0.78} corte={0.52} />
    <div style={abs({left: 60, bottom: 176, ...tit(118, C.offwhite, 66)})}>¿Y si lo vende<br />una monja?</div>
    <div style={abs({left: 62, bottom: 64, ...sec(24, "rgba(242,244,246,0.82)")})}>
      Santa Gota · aceite de oliva extra virgen<br />Spot para TVN · 2026
    </div>
    <Grano op={0.08} />
  </AbsoluteFill>
);

const PIEZAS: Record<string, React.FC> = {"01": T01, "02": T02, "07": T07, "13": T13, "11": T11, "08": T08};

export const TipoPost: React.FC<{id: string}> = ({id}) => {
  asegurarFuentes();
  const P = PIEZAS[id];
  return <P />;
};
