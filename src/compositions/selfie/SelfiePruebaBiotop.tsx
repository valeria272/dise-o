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

export type FormatoSelfie = "post" | "story" | "mail" | "bannerDesk" | "bannerMobile";

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
type Punto = {x: number; y: number; ang: number};
type Layout = {
  mesaW: number; alto: number; outW: number; t: number; curva: string;
  p700: {cx: number; cy: number; h: number; rot: number};
  p911: {cx: number; cy: number; h: number; rot: number};
  ficha700: {x: number; y: number; w: number};
  ficha911: {x: number; y: number; w: number};
  titulo: {y: number; x?: number; w?: number};
  logo: {x: number; y: number};
  flecha700: string; punta700: Punto; flecha911: string; punta911: Punto;
};

/** Flecha de filete con un rulo al medio, de A a B (formatos nuevos). */
const rulo = (ax: number, ay: number, bx: number, by: number, r: number, lado = 1): [string, Punto] => {
  const mx = (ax + bx) / 2, my = (ay + by) / 2;
  const nx = -(by - ay), ny = bx - ax, n = Math.hypot(nx, ny) || 1;
  const k = 0.18 * lado;
  const c1x = (ax + mx) / 2 + (nx / n) * k * n, c1y = (ay + my) / 2 + (ny / n) * k * n;
  const c2x = (mx + bx) / 2 - (nx / n) * k * n * 0.6, c2y = (my + by) / 2 - (ny / n) * k * n * 0.6;
  const d = `M ${ax} ${ay} Q ${c1x} ${c1y} ${mx} ${my} a ${r} ${r} 0 1 ${lado > 0 ? 1 : 0} 0.1 0 Q ${c2x} ${c2y} ${bx} ${by}`;
  return [d, {x: bx, y: by, ang: (Math.atan2(by - c2y, bx - c2x) * 180) / Math.PI}];
};
const [m7d, m7p] = rulo(360, 400, 225, 372, 16, -1);
const [m9d, m9p] = rulo(250, 790, 385, 742, 16, 1);
const [bd7d, bd7p] = rulo(1215, 300, 1030, 262, 20, -1);
const [bd9d, bd9p] = rulo(1440, 640, 1668, 572, 14, 1);
const [bm7d, bm7p] = rulo(575, 118, 368, 128, 20, -1);
const [bm9d, bm9p] = rulo(470, 1020, 735, 960, 20, 1);

const LAYOUT: Record<FormatoSelfie, Layout> = {
  post: {
    mesaW: 1080, alto: 1350, outW: 2250, t: 1,
    logo: {x: 953, y: 173},
    // curva en S: entra arriba a la derecha del centro, sale abajo a la izquierda
    curva: "M 600 0 C 830 260, 820 470, 560 690 C 330 890, 300 1110, 380 1350",
    p700: {cx: 245, cy: 292, h: 560, rot: -18},
    p911: {cx: 872, cy: 1090, h: 530, rot: 15},
    ficha700: {x: 400, y: 238, w: 515},
    ficha911: {x: 66, y: 1060, w: 440},
    titulo: {y: 606},
    flecha700: "M 600 205 C 560 150, 490 150, 500 192 C 510 230, 560 214, 540 184 C 520 156, 460 150, 400 186",
    punta700: {x: 400, y: 186, ang: 150},
    flecha911: "M 470 1262 C 520 1318, 600 1310, 590 1270 C 580 1232, 525 1246, 552 1280 C 578 1310, 660 1290, 735 1236",
    punta911: {x: 735, y: 1236, ang: -40},
  },
  story: {
    mesaW: 1080, alto: 1920, outW: 2250, t: 1,
    logo: {x: 953, y: 230},
    curva: "M 610 0 C 860 380, 840 700, 560 960 C 300 1210, 280 1560, 390 1920",
    p700: {cx: 262, cy: 470, h: 640, rot: -18},
    p911: {cx: 858, cy: 1478, h: 640, rot: 15},
    ficha700: {x: 400, y: 470, w: 515},
    ficha911: {x: 66, y: 1392, w: 440},
    titulo: {y: 862},
    flecha700: "M 600 436 C 560 380, 490 380, 500 422 C 510 460, 560 444, 540 414 C 520 386, 460 380, 400 416",
    punta700: {x: 400, y: 416, ang: 150},
    flecha911: "M 470 1596 C 520 1652, 600 1644, 590 1604 C 580 1566, 525 1580, 552 1614 C 578 1644, 650 1624, 722 1560",
    punta911: {x: 722, y: 1560, ang: -40},
  },
  // MAIL — módulo de 600 de ancho, como MAILSEPT_S2-S3.ai; titular y CTA arriba
  mail: {
    mesaW: 600, alto: 860, outW: 1200, t: 0.56,
    curva: "M 330 0 C 470 200, 460 330, 320 440 C 180 550, 170 700, 220 860",
    p700: {cx: 150, cy: 408, h: 320, rot: -18},
    p911: {cx: 470, cy: 660, h: 310, rot: 15},
    ficha700: {x: 258, y: 262, w: 300},
    ficha911: {x: 26, y: 612, w: 268},
    titulo: {y: 40, x: 0, w: 530},
    logo: {x: 548, y: 44},
    flecha700: m7d, punta700: m7p, flecha911: m9d, punta911: m9p,
  },
  // BANNER DESK — 2001×686, como la mesa 1 de BANNER SEPT_S3-S3.ai; titular a la izquierda
  bannerDesk: {
    mesaW: 2001, alto: 686, outW: 2001, t: 0.82,
    curva: "M 1060 0 C 1190 170, 1150 320, 1000 390 C 860 450, 840 590, 930 686",
    p700: {cx: 915, cy: 336, h: 560, rot: -18},
    p911: {cx: 1745, cy: 352, h: 540, rot: 15},
    ficha700: {x: 1110, y: 70, w: 440},
    ficha911: {x: 1100, y: 420, w: 370},
    titulo: {y: 150, x: 60, w: 760},
    logo: {x: 1880, y: 60},
    flecha700: bd7d, punta700: bd7p, flecha911: bd9d, punta911: bd9p,
  },
  // BANNER MOBILE — 1081×1081, como la mesa 2 del mismo .ai
  bannerMobile: {
    mesaW: 1081, alto: 1081, outW: 1081, t: 0.9,
    curva: "M 600 0 C 830 210, 820 380, 560 550 C 330 710, 300 890, 380 1081",
    p700: {cx: 222, cy: 240, h: 440, rot: -18},
    p911: {cx: 872, cy: 858, h: 410, rot: 15},
    ficha700: {x: 410, y: 160, w: 470},
    ficha911: {x: 60, y: 800, w: 410},
    titulo: {y: 478},
    logo: {x: 958, y: 110},
    flecha700: bm7d, punta700: bm7p, flecha911: bm9d, punta911: bm9p,
  },
};

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
  k: number;
}> = ({nombre, serif, resto, x, y, w, u: g, k}) => {
  const u = g * k; // tipografía y cajas escalan con el formato; la posición, no
  return (
  <div style={{position: "absolute", left: x * g, top: y * g, width: w * g, textAlign: "center"}}>
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
};

const Flecha: React.FC<{d: string; punta: Punto; k: number}> = ({d, punta, k}) => {
  const L = 22 * Math.max(k, 0.7);
  const a1 = ((punta.ang + 28) * Math.PI) / 180;
  const a2 = ((punta.ang - 28) * Math.PI) / 180;
  // las alas van HACIA ATRÁS del trazo (ang = dirección de avance en la punta)
  const p = (a: number) => `${punta.x - L * Math.cos(a)} ${punta.y - L * Math.sin(a)}`;
  return (
    <g fill="none" stroke={C.blanco} strokeWidth={2.4 * Math.max(k, 0.7)} strokeLinecap="round" strokeLinejoin="round">
      <path d={d} />
      <path d={`M ${p(a1)} L ${punta.x} ${punta.y} L ${p(a2)}`} />
    </g>
  );
};

export const SelfiePruebaBiotop: React.FC<{formato: FormatoSelfie}> = ({formato}) => {
  cargaFuentes();
  const L = LAYOUT[formato];
  const W = L.outW;
  const u = W / L.mesaW;
  const t = L.t;
  return (
    <AbsoluteFill style={{backgroundColor: C.salmon}}>
      {/* los dos campos */}
      <svg
        width={W}
        height={L.alto * u}
        viewBox={`0 0 ${L.mesaW} ${L.alto}`}
        style={{position: "absolute", inset: 0}}
      >
        <path d={`${L.curva} L 0 ${L.alto} L 0 0 Z`} fill={C.coral} />
        <Flecha d={L.flecha700} punta={L.punta700} k={t} />
        <Flecha d={L.flecha911} punta={L.punta911} k={t} />
      </svg>

      <Producto src="biotop-700-keratin-kale.png" {...L.p700} u={u} />
      <Producto src="biotop-911-quinoa.png" {...L.p911} u={u} />

      <Ficha
        nombre="700 Keratin & Kale Serum"
        serif="Controla el frizz"
        resto="y da más fuerza al pelo."
        {...L.ficha700}
        u={u}
        k={t}
      />
      <Ficha
        nombre="911 Quinoa Serum"
        serif="Sella"
        resto="la cutícula y aporta brillo natural."
        {...L.ficha911}
        u={u}
        k={t}
      />

      {/* titular: Scotch Condensed Roman + Medium Italic en nude */}
      <div
        style={{
          position: "absolute",
          top: L.titulo.y * u,
          left: (L.titulo.x ?? 0) * u,
          width: (L.titulo.w ?? L.mesaW) * u,
          textAlign: "center",
          color: C.blanco,
        }}
      >
        <div style={{fontFamily: "Scotch Display Condensed", fontWeight: 400, fontSize: 110 * t * u, lineHeight: 0.86}}>
          Dos aliados para
        </div>
        <div
          style={{
            fontFamily: "Scotch Display Condensed",
            fontWeight: 500,
            fontStyle: "italic",
            fontSize: 118 * t * u,
            lineHeight: 0.86,
            color: C.nude,
          }}
        >
          un pelo en orden.
        </div>
        <div
          style={{
            display: "inline-block",
            marginTop: 34 * t * u,
            padding: `${10 * t * u}px ${26 * t * u}px ${12 * t * u}px`,
            border: `${Math.max(1.6 * t * u, 1.4)}px solid ${C.blanco}`,
            fontFamily: "Krub",
            fontSize: 36 * t * u,
            fontWeight: 200,
          }}
        >
          Encuéntralos en <span style={{fontWeight: 600, fontStyle: "italic"}}>Selfie.cl</span>
        </div>
      </div>

      {/* logotipo SELFIE vertical — en la grilla va en x 953, y 173 de la mesa de 1080 */}
      <Img
        src={staticFile("assets/selfie/2026-nuevo-estilo/selfie-logo-vertical.svg")}
        style={{position: "absolute", left: L.logo.x * u, top: L.logo.y * u, width: 37 * t * u}}
      />
    </AbsoluteFill>
  );
};
