/**
 * SELFIE · PRUEBA «Biotop 700 + 911» — post 4:5 y story 9:16 (24-09-2026)
 *
 * DIRECCIÓN DE ARTE
 * - Diagramación: la de la REFERENCIA que dejó Coni en PRUEBA/INFORMACIÓN PARA PRUEBA
 *   (dos campos de color partidos por una curva en S, un producto inclinado en cada
 *   campo, beneficio en la esquina opuesta con flecha curva, titular al centro).
 * - Todo lo demás sale del estilo nuevo medido en GRILLA SEPT_S2-S3.ai
 *   (ver clients/selfie/CLAUDE.md § EL ESTILO NUEVO):
 *     titular Scotch Display Condensed Roman 110 + 2.ª línea Medium Italic 118 en nude,
 *     fichas de producto de la mesa 8 (caja coral + caja blanca con el beneficio),
 *     recuadro de filete blanco fino, logotipo SELFIE vertical arriba a la derecha,
 *     paleta #FF4374 / #FF8C93 / #F7D4C0 / #001E1D / blanco.
 * - Lo que NO se trae de la referencia: el patrón de palabras caladas del fondo
 *   (el cliente pidió menos elementos compitiendo) y las flechas de plumón, que acá
 *   son filete fino como la flecha de «Desliza y descúbrelos».
 *
 * Medidas en unidades de la mesa de Coni (1080 de ancho); u() escala a la entrega.
 * ⚠️ Scotch Display está reconstruida desde los subconjuntos del .ai: sólo trae las
 *    letras que Coni ya usó. El titular está escrito con esas letras (sin f, g, z, ñ
 *    en la itálica). Para la entrega final: activar Scotch Display en Creative Cloud.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

export type FormatoSelfie = "post" | "story";

const C = {
  coral: "#FF4374",
  salmon: "#FF8C93",
  nude: "#F7D4C0",
  tinta: "#001E1D",
  blanco: "#FFFFFF",
};

let fuentesListas = false;
const cargaFuentes = () => {
  if (fuentesListas || typeof document === "undefined") return;
  fuentesListas = true;
  const caras: Array<[string, number, string, string]> = [
    ["Scotch Display Condensed", 400, "normal", "ScotchDisplayCond-Rm.ttf"],
    ["Scotch Display Condensed", 500, "italic", "ScotchDisplayCond-MdIt.ttf"],
    ["Scotch Display", 500, "italic", "ScotchDisplay-MediumItalic.ttf"],
    ["Krub", 200, "normal", "Krub-ExtraLight.ttf"],
    ["Krub", 400, "normal", "Krub-Regular.ttf"],
    ["Krub", 500, "normal", "Krub-Medium.ttf"],
    ["Krub", 600, "normal", "Krub-SemiBold.ttf"],
    ["Krub", 600, "italic", "Krub-SemiBoldItalic.ttf"],
    ["Krub", 700, "normal", "Krub-Bold.ttf"],
  ];
  const css = caras
    .map(
      ([fam, w, st, file]) =>
        `@font-face{font-family:'${fam}';font-weight:${w};font-style:${st};font-display:block;` +
        `src:url(${staticFile(`assets/fonts/selfie-2026/${file}`)}) format('truetype');}`,
    )
    .join("\n");
  const s = document.createElement("style");
  s.textContent = css;
  document.head.appendChild(s);
  const f = (document as unknown as {fonts?: {load: (x: string) => void}}).fonts;
  if (f) caras.forEach(([fam, w, st]) => f.load(`${st} ${w} 40px '${fam}'`));
};

// Geometría por formato, en unidades de mesa (ancho 1080).
const LAYOUT = {
  post: {
    alto: 1350,
    // curva en S: entra arriba a la derecha del centro, sale abajo a la izquierda
    curva: "M 600 0 C 830 260, 820 470, 560 690 C 330 890, 300 1110, 380 1350",
    p700: {cx: 245, cy: 292, h: 560, rot: -18},
    p911: {cx: 872, cy: 1090, h: 530, rot: 15},
    ficha700: {x: 400, y: 238, w: 515},
    ficha911: {x: 66, y: 1060, w: 440},
    titulo: {y: 606},
    logoY: 173,
    flecha700: "M 600 205 C 560 150, 490 150, 500 192 C 510 230, 560 214, 540 184 C 520 156, 460 150, 400 186",
    punta700: {x: 400, y: 186, ang: 150},
    flecha911: "M 470 1262 C 520 1318, 600 1310, 590 1270 C 580 1232, 525 1246, 552 1280 C 578 1310, 660 1290, 735 1236",
    punta911: {x: 735, y: 1236, ang: -40},
  },
  story: {
    alto: 1920,
    curva: "M 610 0 C 860 380, 840 700, 560 960 C 300 1210, 280 1560, 390 1920",
    p700: {cx: 262, cy: 470, h: 640, rot: -18},
    p911: {cx: 858, cy: 1478, h: 640, rot: 15},
    ficha700: {x: 400, y: 470, w: 515},
    ficha911: {x: 66, y: 1392, w: 440},
    titulo: {y: 862},
    logoY: 230,
    flecha700: "M 600 436 C 560 380, 490 380, 500 422 C 510 460, 560 444, 540 414 C 520 386, 460 380, 400 416",
    punta700: {x: 400, y: 416, ang: 150},
    flecha911: "M 470 1596 C 520 1652, 600 1644, 590 1604 C 580 1566, 525 1580, 552 1614 C 578 1644, 650 1624, 722 1560",
    punta911: {x: 722, y: 1560, ang: -40},
  },
} as const;

const Producto: React.FC<{src: string; cx: number; cy: number; h: number; rot: number; u: number}> = ({
  src,
  cx,
  cy,
  h,
  rot,
  u,
}) => (
  <Img
    src={staticFile(`assets/selfie/2026-nuevo-estilo/${src}`)}
    style={{
      position: "absolute",
      height: h * u,
      left: cx * u,
      top: cy * u,
      transform: `translate(-50%, -50%) rotate(${rot}deg)`,
      filter: `drop-shadow(${-14 * u}px ${22 * u}px ${26 * u}px rgba(0,30,29,0.28))`,
    }}
  />
);

/** Ficha de producto calcada de la mesa 8 de la grilla: caja coral con el nombre y,
 *  montada encima, caja blanca con el beneficio (Scotch Medium Italic + Krub Medium). */
const Ficha: React.FC<{
  nombre: string;
  serif: string;
  resto: string;
  x: number;
  y: number;
  w: number;
  u: number;
}> = ({nombre, serif, resto, x, y, w, u}) => (
  <div style={{position: "absolute", left: x * u, top: y * u, width: w * u, textAlign: "center"}}>
    <div
      style={{
        background: C.coral,
        borderRadius: 14 * u,
        padding: `${20 * u}px ${24 * u}px ${42 * u}px`,
        color: C.blanco,
        fontFamily: "Krub",
        fontWeight: 700,
        fontSize: 37 * u,
        lineHeight: 1.08,
      }}
    >
      {nombre}
    </div>
    <div
      style={{
        position: "relative",
        margin: `${-22 * u}px ${32 * u}px 0`,
        background: C.blanco,
        borderRadius: 14 * u,
        padding: `${12 * u}px ${20 * u}px ${14 * u}px`,
        color: C.coral,
        fontFamily: "Krub",
        fontWeight: 500,
        fontSize: 34 * u,
        lineHeight: 1.07,
      }}
    >
      <span style={{fontFamily: "Scotch Display", fontStyle: "italic", fontWeight: 500, fontSize: 38 * u}}>
        {serif}
      </span>{" "}
      {resto}
    </div>
  </div>
);

const Flecha: React.FC<{d: string; punta: {x: number; y: number; ang: number}}> = ({d, punta}) => {
  const L = 22;
  const a1 = ((punta.ang + 28) * Math.PI) / 180;
  const a2 = ((punta.ang - 28) * Math.PI) / 180;
  const p = (a: number) => `${punta.x + L * Math.cos(a)} ${punta.y + L * Math.sin(a)}`;
  return (
    <g fill="none" stroke={C.blanco} strokeWidth={2.4} strokeLinecap="round" strokeLinejoin="round">
      <path d={d} />
      <path d={`M ${p(a1)} L ${punta.x} ${punta.y} L ${p(a2)}`} />
    </g>
  );
};

export const SelfiePruebaBiotop: React.FC<{formato: FormatoSelfie}> = ({formato}) => {
  cargaFuentes();
  const L = LAYOUT[formato];
  const W = 2250;
  const u = W / 1080;
  return (
    <AbsoluteFill style={{backgroundColor: C.salmon}}>
      {/* los dos campos */}
      <svg
        width={W}
        height={L.alto * u}
        viewBox={`0 0 1080 ${L.alto}`}
        style={{position: "absolute", inset: 0}}
      >
        <path d={`${L.curva} L 0 ${L.alto} L 0 0 Z`} fill={C.coral} />
        <Flecha d={L.flecha700} punta={L.punta700} />
        <Flecha d={L.flecha911} punta={L.punta911} />
      </svg>

      <Producto src="biotop-700-keratin-kale.png" {...L.p700} u={u} />
      <Producto src="biotop-911-quinoa.png" {...L.p911} u={u} />

      <Ficha
        nombre="700 Keratin & Kale Serum"
        serif="Controla el frizz"
        resto="y da más fuerza al pelo."
        {...L.ficha700}
        u={u}
      />
      <Ficha
        nombre="911 Quinoa Serum"
        serif="Sella"
        resto="la cutícula y aporta brillo natural."
        {...L.ficha911}
        u={u}
      />

      {/* titular: Scotch Condensed Roman + Medium Italic en nude */}
      <div
        style={{
          position: "absolute",
          top: L.titulo.y * u,
          left: 0,
          width: W,
          textAlign: "center",
          color: C.blanco,
        }}
      >
        <div style={{fontFamily: "Scotch Display Condensed", fontWeight: 400, fontSize: 110 * u, lineHeight: 0.86}}>
          Dos aliados para
        </div>
        <div
          style={{
            fontFamily: "Scotch Display Condensed",
            fontWeight: 500,
            fontStyle: "italic",
            fontSize: 118 * u,
            lineHeight: 0.86,
            color: C.nude,
          }}
        >
          un pelo en orden.
        </div>
        <div
          style={{
            display: "inline-block",
            marginTop: 34 * u,
            padding: `${10 * u}px ${26 * u}px ${12 * u}px`,
            border: `${1.6 * u}px solid ${C.blanco}`,
            fontFamily: "Krub",
            fontSize: 36 * u,
            fontWeight: 200,
          }}
        >
          Encuéntralos en <span style={{fontWeight: 600, fontStyle: "italic"}}>Selfie.cl</span>
        </div>
      </div>

      {/* logotipo SELFIE vertical — misma posición que en la grilla (x 953, y 172) */}
      <Img
        src={staticFile("assets/selfie/2026-nuevo-estilo/selfie-logo-vertical.svg")}
        style={{position: "absolute", left: 953 * u, top: L.logoY * u, width: 37 * u}}
      />
    </AbsoluteFill>
  );
};
