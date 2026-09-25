// ============================================================================
// POSTS 12 — la grilla como dirección creativa (24-09-2026, 3er feedback)
// ----------------------------------------------------------------------------
// CAMBIO DE MÉTODO: nada de sistemas. Cada post nace de una idea distinta y
// comparte sólo el criterio: idea entendible + imagen memorable + UNA
// intervención gráfica precisa. Referencia de ley: la grilla del director
// (creative-system/MASTER/reference/REF_GRILLA_POSTS_24-09.png) + la lámina.
//
// El texto vive DENTRO del objeto fotografiado (diario, hoja, etiqueta, hoja
// rosa) — Nano Banana Pro, ortografía revisada a mano. El diseño sólo pone lo
// que el objeto no puede decir.
// Clientes con material real: Traverso (cuadro del reel «Los de siempre»; su
// línea de cierre ES «Ahora también en nuestra mesa.») y Santa Gota (seg. 7).
// ⚠️ P05: «2,29 MM» viene del brief del director y NO está verificado.
// ⚠️ P10: referencia de dirección — se fotografía a una persona real del equipo.
// ⚠️ P11: recreación declarada.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {C, asegurarFuentes, VOZ} from "../../brand/copylab/sistema";
import {Foto, Grano, Velo} from "../../brand/copylab/lienzo";
import {Anotacion, Flecha} from "../../brand/copylab/mano";

const A = "assets/copylab/posts12/";
const abs = (s: React.CSSProperties): React.CSSProperties => ({position: "absolute", ...s});
const mono = (color: string, extra?: React.CSSProperties): React.CSSProperties => ({
  fontFamily: VOZ.data, fontSize: 21, lineHeight: 1.45, letterSpacing: "0.14em",
  textTransform: "uppercase", color, ...extra,
});
const narrow = (size: number, color: string, extra?: React.CSSProperties): React.CSSProperties => ({
  fontFamily: VOZ.narrow, fontWeight: 700, fontSize: size, lineHeight: 0.86,
  letterSpacing: "-0.02em", textTransform: "uppercase", color, whiteSpace: "nowrap", ...extra,
});

const Solo: React.FC<{img: string; grano?: number; children?: React.ReactNode}> = ({img, grano = 0.12, children}) => (
  <AbsoluteFill style={{background: C.tinta}}>
    <Foto src={A + img} grado="crudo" />
    {children}
    <Grano op={grano} />
  </AbsoluteFill>
);

// 01 — el diario lo dice todo.
const P01 = () => <Solo img="p01.jpg" />;

// 02 — el humor está en la foto.
const P02 = () => <Solo img="p02.jpg" />;

// 03 — sólo la metadata.
const P03 = () => (
  <Solo img="p03.jpg">
    <Velo desde="abajo" fuerza={0.35} corte={0.8} color={C.offwhite} />
    <div style={abs({left: 60, bottom: 64, background: "rgba(242,244,246,0.92)", padding: "14px 18px", ...mono(C.tinta, {fontSize: 30})})}>La que publicamos<br />fue la 38.</div>
  </Solo>
);

// 04 — campaña primero, case study después.
const P04 = () => (
  <Solo img="p04-traverso.jpg">
    <Velo desde="abajo" fuerza={0.8} corte={0.5} />
    <div style={abs({left: 40, bottom: 170, ...narrow(118, C.offwhite)})}>Ahora también<br />en nuestra mesa.</div>
    <div style={abs({left: 44, bottom: 66, ...mono("rgba(242,244,246,0.8)")})}>Traverso × Copywriters.cl<br />Reel «Los de siempre» · 2026</div>
  </Solo>
);

// 05 — la cifra es la imagen; la foto la cruza.
const P05 = () => (
  <AbsoluteFill style={{background: C.offwhite}}>
    <div style={abs({left: 18, top: 270, ...narrow(330, C.tinta, {letterSpacing: "-0.05em", lineHeight: 0.8})})}>2,29 MM</div>
    <div style={abs({left: 430, top: 430, width: 380, height: 300, overflow: "hidden",
      boxShadow: "0 18px 36px rgba(8,15,20,0.28)", transform: "rotate(-3deg)"})}>
      <Img src={staticFile(A + "p05.jpg")} style={{width: "100%", height: "100%", objectFit: "cover"}} />
    </div>
    <div style={abs({left: 60, top: 930, ...mono(C.tinta, {fontSize: 28})})}>Personas alcanzadas</div>
    <div style={abs({left: 56, top: 990, fontFamily: VOZ.editorial, fontStyle: "italic", fontSize: 104, color: C.rosa, lineHeight: 1})}>pero personas.</div>
    <Grano op={0.1} />
  </AbsoluteFill>
);

// 06 — la foto cuenta la historia.
const P06 = () => <Solo img="p06.jpg" />;

// 07 — sin titular.
const P07 = () => (
  <Solo img="p07.jpg">
    <div style={abs({left: 60, bottom: 64, ...mono(C.offwhite)})}>Nuestra herramienta favorita.</div>
  </Solo>
);

// 08 — cliente: la intervención se sale del lienzo.
const P08 = () => (
  <Solo img="p08-santagota.jpg">
    <Velo desde="abajo" fuerza={0.7} corte={0.45} />
    <div style={abs({left: -18, bottom: 176, ...narrow(250, C.offwhite, {lineHeight: 0.82, letterSpacing: "-0.035em"})})}>De un<br />“¿Y si…?”</div>
    <div style={abs({right: 56, bottom: 104, ...narrow(64, C.offwhite)})}>a TVN.</div>
    <div style={abs({left: 44, bottom: 60, ...mono("rgba(242,244,246,0.8)")})}>Santa Gota × Copywriters.cl · 2026</div>
  </Solo>
);

// 09 — sin robots.
const P09 = () => <Solo img="p09.jpg" />;

// 10 — la anotación señala lo que pasa en la foto.
const P10 = () => (
  <Solo img="p10.jpg" grano={0.16}>
    <Anotacion x={60} y={120} texto={"se le acaba\nde ocurrir."} size={78} rot={-6} />
    <Flecha x={220} y={290} w={230} h={300} grosor={6} semilla={11} rot={35} curva={0.8} />
    <div style={abs({left: 60, bottom: 60, ...mono("rgba(242,244,246,0.7)", {fontSize: 16})})}>Referencia de dirección · se fotografía al equipo real</div>
  </Solo>
);

// 11 — la frase encontrada es la protagonista; Copywriters sólo cataloga.
const P11 = () => (
  <Solo img="p11-llaves.jpg" grano={0.14}>
    <div style={abs({left: 56, bottom: 56, ...mono("rgba(242,244,246,0.85)", {fontSize: 17})})}>
      Nadie lo firmó<br />Nº004 · Santiago · recreación
    </div>
  </Solo>
);

// 12 — manifiesto: la etiqueta está en la bolsa.
const P12 = () => <Solo img="p12.jpg" />;

const POSTS = [P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12];

// ---------------------------------------------------------------------------
// v2 · 16 posts (4º feedback). NO EXISTE «EL LOOK COPYWRITERS»: máximo 5 con
// rosa evidente (quedan 01 · 07 · 09 · 12). Se rehacen 03 05 06 08 10 y
// entran 13–16. Una intervención o ninguna.
// ---------------------------------------------------------------------------

// 02 · refinado: el subrayado rosa pasa a negro (recoloreado por máscara).
const Q02 = () => <Solo img="p02-sinrosa.jpg" />;

// 03 · 37 versiones que visten a una persona. B&N, flash.
const Q03 = () => (
  <Solo img="np03.jpg" grano={0.18}>
    <div style={abs({left: 56, bottom: 56, ...mono("rgba(242,244,246,0.85)", {fontSize: 20})})}>La que publicamos fue la 38.</div>
  </Solo>
);

// 05 · la escala sin dashboard: miles, y una sola te saluda.
const Q05 = () => (
  <Solo img="np05.jpg" grano={0.1}>
    <div style={abs({left: 56, bottom: 60, ...mono(C.tinta, {fontSize: 20, background: "rgba(242,244,246,0.9)", padding: "10px 14px"})})}>2,29 MM de personas alcanzadas</div>
    <div style={abs({left: 600, top: 690, fontFamily: VOZ.editorial, fontStyle: "italic", fontSize: 64, color: C.blanco, lineHeight: 1,
      textShadow: "0 2px 18px rgba(0,0,0,0.35)"})}>pero personas.</div>
  </Solo>
);

// 06 · la reunión: la evidencia es la tapa de la pizza.
const Q06 = () => <Solo img="np06.jpg" grano={0.14} />;

// 08 · Santa Gota: la fotografía manda. Sólo metadata editorial mínima
//      (el director sacó también «El brief decía…»: la foto ya es rara sola).
const Q08 = () => (
  <Solo img="p08-santagota.jpg" grano={0.08}>
    <div style={abs({right: 56, bottom: 64, textAlign: "right", ...mono("rgba(242,244,246,0.85)", {fontSize: 17})})}>Santa Gota<br />spot para TVN · 2026</div>
  </Solo>
);

// 10 · cómo piensa una persona: el brazo como borrador, en la micro.
const Q10 = () => (
  <Solo img="np10.jpg" grano={0.14}>
    <div style={abs({left: 56, bottom: 56, ...mono("rgba(242,244,246,0.7)", {fontSize: 16})})}>Referencia · se fotografía a alguien real del equipo</div>
  </Solo>
);

const Q13 = () => <Solo img="np13.jpg" grano={0.1} />;
const Q14 = () => <Solo img="np14.jpg" grano={0.08} />;
const Q15 = () => (
  <Solo img="np15.jpg" grano={0.12}>
    <div style={abs({right: 56, bottom: 56, ...mono(C.tinta, {fontSize: 20})})}>Publicamos igual.</div>
  </Solo>
);
const Q16 = () => <Solo img="np16.jpg" grano={0.05} />;

const POSTS16 = [P01, Q02, Q03, P04, Q05, Q06, P07, Q08, P09, Q10, P11, P12, Q13, Q14, Q15, Q16];

export const Post16: React.FC<{n: number}> = ({n}) => {
  asegurarFuentes();
  const P = POSTS16[n - 1];
  return <P />;
};

export const Post12: React.FC<{n: number}> = ({n}) => {
  asegurarFuentes();
  const P = POSTS[n - 1];
  return <P />;
};
