// ============================================================================
// RECOMPUESTA — reset de dirección de arte (24-09-2026)
// ----------------------------------------------------------------------------
// «El problema no es el copy: es la dirección de arte.» Se había armado sin
// querer una fórmula: FOTO FULL BLEED + ARCHIVO ENORME + B/N + TEXTO CORTADO.
// Esto la desarma. Mismas fotos, cero imágenes nuevas.
//
// Antes de componer se decide QUÉ MANDA (uno solo):
//   01 OBJETO (el diario)      · comentario en serif, chico, como pie
//   02 OBJETO (la hoja)        · «Lo anotamos.» en serif rosa, respuesta insolente
//   07 IMAGEN (la tecla)       · una línea serif chica. 90/10
//   13A IMAGEN                 · cero diseño: el «mejor no.» manuscrito ya está en la foto
//   13B TEXTO como pie         · página de revista: foto arriba, pie serif con aire
//   11 IMAGEN (el hallazgo)    · sólo catalogación mono. 95/5
//   08 IMAGEN (la monja)       · «Amén.» chico, descubierto después. Crédito mono
// Archivo NO aparece en ninguna: ninguna pieza lo necesitó.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {C, asegurarFuentes, VOZ} from "../../brand/copylab/sistema";
import {Foto, Grano, Velo} from "../../brand/copylab/lienzo";

const P = "assets/copylab/posts12/";
const T = "assets/copylab/tipo/";
const abs = (s: React.CSSProperties): React.CSSProperties => ({position: "absolute", ...s});
const serif = (size: number, color: string, extra?: React.CSSProperties): React.CSSProperties => ({
  fontFamily: VOZ.editorial, fontStyle: "italic", fontSize: size, lineHeight: 1.08, color, ...extra,
});
const mono = (color: string, size = 16, extra?: React.CSSProperties): React.CSSProperties => ({
  fontFamily: VOZ.data, fontSize: size, lineHeight: 1.5, letterSpacing: "0.16em",
  textTransform: "uppercase", color, ...extra,
});

// 01 · manda el diario. Nuestro comentario es un pie editorial.
const R01 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={P + "p01.jpg"} grado="crudo" />
    <Velo desde="abajo" fuerza={0.45} corte={0.78} />
    <div style={abs({left: 64, bottom: 70, ...serif(40, C.offwhite)})}>
      Nadie lee el diario.<br />
      <span style={{color: C.rosa}}>Tú acabas de leer esto.</span>
    </div>
    <Grano op={0.12} />
  </AbsoluteFill>
);

// 02 · manda la hoja. La respuesta, casi insolente, al lado del brief.
const R02 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={P + "p02-sinrosa.jpg"} grado="crudo" />
    <div style={abs({left: 640, top: 1152, transform: "rotate(-4deg)", ...serif(50, C.rosa)})}>Lo anotamos.</div>
    <Grano op={0.1} />
  </AbsoluteFill>
);

// 07 · manda la tecla. Una línea, chica, en la zona oscura.
const R07 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={P + "p07.jpg"} grado="crudo" />
    <div style={abs({left: 66, top: 70, ...serif(38, C.offwhite)})}>Este texto tenía<br />tres párrafos.</div>
    <Grano op={0.1} />
  </AbsoluteFill>
);

// 13A · la foto ya lo dice: el «mejor no.» manuscrito diminuto en la esquina del letrero.
const R13A = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={P + "np13-sinborde.jpg"} grado="crudo" />
    <Grano op={0.08} />
  </AbsoluteFill>
);

// 13B · página de revista: la foto se achica, el pie trae la segunda idea.
const R13B = () => (
  <AbsoluteFill style={{background: C.offwhite}}>
    <div style={abs({left: 0, top: 0, width: 1080, height: 1010, overflow: "hidden"})}>
      <Img src={staticFile(T + "p13-limpio.jpg")} style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 22%"}} />
    </div>
    <div style={abs({left: 64, top: 1072, width: 760, ...serif(46, C.tinta)})}>
      Mejor esto que otro «somos líderes».
    </div>
    <div style={abs({left: 66, bottom: 62, ...mono("rgba(8,15,20,0.55)", 14)})}>Santiago · espacio disponible</div>
    <Grano op={0.08} />
  </AbsoluteFill>
);

// 11 · manda el hallazgo. Sólo lo catalogamos, y declaramos que es recreación.
const R11 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={P + "p11-llaves.jpg"} grado="crudo" />
    <div style={abs({left: 60, bottom: 58, ...mono("rgba(242,244,246,0.78)", 15)})}>Nadie lo firmó · Nº004 · Santiago</div>
    <div style={abs({right: 60, bottom: 58, ...mono("rgba(242,244,246,0.45)", 12)})}>Recreación</div>
    <Grano op={0.12} />
  </AbsoluteFill>
);

// 08 · manda la monja. «Amén.» aparece después, junto al hábito, sin tocar cara ni plato.
const R08 = () => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={P + "p08-santagota.jpg"} grado="crudo" />
    <div style={abs({left: 846, top: 1004, ...serif(46, C.rosa)})}>Amén.</div>
    <div style={abs({right: 58, bottom: 56, textAlign: "right", ...mono("rgba(242,244,246,0.75)", 13)})}>Santa Gota · spot para TVN · 2026</div>
    <Grano op={0.08} />
  </AbsoluteFill>
);

const PIEZAS: Record<string, React.FC> = {"01": R01, "02": R02, "07": R07, "13A": R13A, "13B": R13B, "11": R11, "08": R08};

export const Recompuesta: React.FC<{id: string}> = ({id}) => {
  asegurarFuentes();
  const R = PIEZAS[id];
  return <R />;
};
