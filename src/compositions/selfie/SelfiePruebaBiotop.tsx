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
import MEDIDAS from "./biotop-prueba.json";

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
type Diseno = {
  curva: string;
  titulo: {y: number; x?: number; w?: number};
  logo: {x: number; y: number};
  cta: {donde: "titulo" | "abajo" | "no"; y?: number};
};
type Medidas = {
  mesaW: number; alto: number; outW: number; t: number;
  p700: {cx: number; cy: number; h: number; rot: number};
  p911: {cx: number; cy: number; h: number; rot: number};
  tip700: {x: number; y: number};
  tip911: {x: number; y: number};
  start700: {x: number; y: number};
  start911: {x: number; y: number};
  ficha700: {x: number; y: number; w: number};
  ficha911: {x: number; y: number; w: number};
};

/** LA flecha: el trazo de la HISTORIA, aprobado por Coni el 24-09. En cada formato se
 *  calca GIRADO y ESCALADO para que salga del borde de su ficha (start) y termine
 *  justo antes de su producto (tip): la flecha lleva la lectura de la ficha al frasco. */
const TRAZO = (MEDIDAS as unknown as {_trazo: Record<"700" | "911", {d: string}>})._trazo;

/** Aplica al trazo la semejanza que lleva su inicio a `start` y su punta a `tip`. */
const calca = (d: string, start: {x: number; y: number}, tip: {x: number; y: number}) => {
  const n = (d.match(/-?\d+(\.\d+)?/g) ?? []).map(Number);
  const pts: [number, number][] = [];
  for (let i = 0; i < n.length; i += 2) pts.push([n[i], n[i + 1]]);
  const [s0, t0] = [pts[0], pts[pts.length - 1]];
  const v0 = [t0[0] - s0[0], t0[1] - s0[1]];
  const v1 = [tip.x - start.x, tip.y - start.y];
  const k = Math.hypot(v1[0], v1[1]) / Math.hypot(v0[0], v0[1]);
  const giro = Math.atan2(v1[1], v1[0]) - Math.atan2(v0[1], v0[0]);
  const [c, sn] = [Math.cos(giro) * k, Math.sin(giro) * k];
  const q = pts.map(([x, y]) => {
    const dx = x - s0[0], dy = y - s0[1];
    return [start.x + c * dx - sn * dy, start.y + sn * dx + c * dy];
  });
  const f = (p: number[]) => `${p[0].toFixed(2)} ${p[1].toFixed(2)}`;
  let out = `M ${f(q[0])}`;
  for (let i = 1; i < q.length; i += 3) out += ` C ${f(q[i])}, ${f(q[i + 1])}, ${f(q[i + 2])}`;
  const penult = q[q.length - 2];
  const ang = (Math.atan2(tip.y - penult[1], tip.x - penult[0]) * 180) / Math.PI;
  return {d: out, ang};
};

const LAYOUT: Record<FormatoSelfie, Diseno> = {
  post: {
    logo: {x: 953, y: 173},
    cta: {donde: "titulo"},
    // curva en S: entra arriba a la derecha del centro, sale abajo a la izquierda
    curva: "M 600 0 C 830 260, 820 470, 560 690 C 330 890, 300 1110, 380 1350",
    titulo: {y: 606},
  },
  story: {
    logo: {x: 953, y: 230},
    cta: {donde: "titulo"},
    curva: "M 610 0 C 860 380, 840 700, 560 960 C 300 1210, 280 1560, 390 1920",
    titulo: {y: 862},
  },
  // MAIL — módulo de 600 de ancho, como MAILSEPT_S2-S3.ai; titular y CTA arriba
  mail: {
    curva: "M 330 0 C 470 200, 460 330, 320 440 C 180 550, 170 700, 220 860",
    titulo: {y: 40, x: 0, w: 530},
    logo: {x: 548, y: 44},
    cta: {donde: "abajo", y: 772},
  },
  // BANNER DESK — 2001×686, como la mesa 1 de BANNER SEPT_S3-S3.ai; titular a la izquierda
  bannerDesk: {
    curva: "M 1060 0 C 1190 170, 1150 320, 1000 390 C 860 450, 840 590, 930 686",
    titulo: {y: 240, x: 60, w: 760},
    logo: {x: 1880, y: 60},
    cta: {donde: "no"},
  },
  // BANNER MOBILE — 1081×1081, como la mesa 2 del mismo .ai
  bannerMobile: {
    curva: "M 600 0 C 830 210, 820 380, 560 550 C 330 710, 300 890, 380 1081",
    titulo: {y: 462},
    logo: {x: 958, y: 110},
    cta: {donde: "no"},
  },
};

/** El frasco llega YA girado y al alto exacto en píxeles de este formato
 *  (scripts/selfie-biotop-productos.py): se pone 1:1, Chrome no lo remuestrea. */
const Producto: React.FC<{src: string; cx: number; cy: number; u: number}> = ({src, cx, cy, u}) => (
  <Img
    src={staticFile(`assets/selfie/2026-nuevo-estilo/biotop/${src}`)}
    style={{
      position: "absolute",
      left: cx * u,
      top: cy * u,
      transform: "translate(-50%, -50%)",
      filter: `drop-shadow(${-14 * u}px ${22 * u}px ${26 * u}px rgba(0,30,29,0.28))`,
    }}
  />
);

/** Ficha de producto de la mesa 8 de la grilla: caja con el nombre (en tinta, no en coral,
 *  para que no se pierda sobre el campo coral) y,
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
  fondo: string;
  tinta: string;
}> = ({nombre, serif, resto, x, y, w, u: g, k, fondo, tinta}) => {
  const u = g * k; // tipografía y cajas escalan con el formato; la posición, no
  return (
  <div style={{position: "absolute", left: x * g, top: y * g, width: w * g, textAlign: "center"}}>
    {/* Resplandor negro al 30 % en MULTIPLICAR alrededor de la caja del nombre, para
        que no se pierda sobre el campo coral (Coni, 24-09). Es una capa propia detrás
        de la caja: así sólo el resplandor multiplica, la caja queda coral puro. */}
    <div style={{position: "relative"}}>
      <div
        style={{
          position: "absolute",
          inset: 0,
          borderRadius: 14 * u,
          boxShadow: `0 0 ${20 * u}px ${7 * u}px rgba(0,0,0,0.30)`,
          mixBlendMode: "multiply",
        }}
      />
      <div
        style={{
          position: "relative",
          background: fondo,
          borderRadius: 14 * u,
          padding: `${20 * u}px ${24 * u}px ${42 * u}px`,
          color: tinta,
          fontFamily: "Krub",
          fontWeight: 700,
          fontSize: 37 * u,
          lineHeight: 1.08,
        }}
      >
        {nombre}
      </div>
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

/** El campo IZQUIERDO de la S. El derecho es siempre salmón #FF8C93.
 *  Sobre un campo claro (damasco) todo lo blanco pasa a tinta, como en la mesa 11
 *  de la grilla (texto #001E1D sobre fondo claro). */
export type Campo = "coral" | "damasco" | "tinta";
export const ESQUEMA: Record<Campo, {campo: string; texto: string; linea2: string; flecha: string}> = {
  coral: {campo: C.coral, texto: C.blanco, linea2: C.nude, flecha: C.blanco},
  // Coni 24-09: sobre el damasco NO va tinta; texto y flechas vuelven a los del inicio
  damasco: {campo: C.nude, texto: C.blanco, linea2: C.nude, flecha: C.blanco},
  tinta: {campo: C.tinta, texto: C.blanco, linea2: C.nude, flecha: C.blanco},
};

/** «Encuéntralos en Selfie.cl» — recuadro de filete blanco fino, como en la grilla.
 *  Post/historia: bajo el titular · mail: al final de la lectura · banners: NO va. */
const Cta: React.FC<{t: number; u: number; color: string}> = ({t, u, color}) => (
  <div
    style={{
      display: "inline-block",
      marginTop: 34 * t * u,
      padding: `${10 * t * u}px ${26 * t * u}px ${12 * t * u}px`,
      border: `${Math.max(1.6 * t * u, 1.4)}px solid ${color}`,
      fontFamily: "Krub",
      fontSize: 36 * t * u,
      fontWeight: 200,
    }}
  >
    Encuéntralos en <span style={{fontWeight: 600, fontStyle: "italic"}}>Selfie.cl</span>
  </div>
);

const Flecha: React.FC<{
  forma: "700" | "911";
  start: {x: number; y: number};
  tip: {x: number; y: number};
  k: number;
  color?: string;
}> = ({forma, start, tip, k, color = C.blanco}) => {
  const {d, ang} = calca(TRAZO[forma].d, start, tip);
  const L = 22 * k;
  const a1 = ((ang + 28) * Math.PI) / 180;
  const a2 = ((ang - 28) * Math.PI) / 180;
  // las alas van HACIA ATRÁS del trazo (ang = dirección de avance en la punta)
  const p = (a: number) => `${tip.x - L * Math.cos(a)} ${tip.y - L * Math.sin(a)}`;
  return (
    <g fill="none" stroke={color} strokeWidth={2.4 * k} strokeLinecap="round" strokeLinejoin="round">
      <path d={d} />
      <path d={`M ${p(a1)} L ${tip.x} ${tip.y} L ${p(a2)}`} />
    </g>
  );
};

/** Máscara de las flechas para el QA: fondo negro, flechas en blanco. */
const MascaraFlechas: React.FC<{L: Diseno & Medidas; u: number}> = ({L, u}) => (
  <AbsoluteFill style={{background: "#000"}}>
    <svg width={L.outW} height={L.alto * u} viewBox={`0 0 ${L.mesaW} ${L.alto}`} style={{position: "absolute", inset: 0}}>
      <Flecha forma="700" start={L.start700} tip={L.tip700} k={L.t} color="#fff" />
      <Flecha forma="911" start={L.start911} tip={L.tip911} k={L.t} color="#fff" />
    </svg>
  </AbsoluteFill>
);

/** capa: "todo" (la pieza) · "sinFlechas" / "flechas" (para el QA de choques: qa/selfie-flechas.py). */
export const SelfiePruebaBiotop: React.FC<{formato: FormatoSelfie; capa?: "todo" | "sinFlechas" | "flechas"; campo?: Campo; cajaDamasco?: boolean; intervenido?: boolean}> = ({
  formato,
  capa = "todo",
  intervenido = false, // PRUEBA aparte: tapa transparente y líquido a nivel (scripts/selfie-biotop-intervenir.py)
  cajaDamasco = false,
  campo = "coral", // Coni 24-09: se probaron damasco y tinta; se vuelve a la 1.ª combinación
}) => {
  const FICHA = cajaDamasco ? {fondo: C.nude, tinta: C.coral} : {fondo: C.coral, tinta: C.blanco};
  const E = ESQUEMA[campo];
  cargaFuentes();
  const M = (MEDIDAS as unknown as Record<FormatoSelfie, Medidas>)[formato];
  const L = {...LAYOUT[formato], ...M};
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
        <path d={`${L.curva} L 0 ${L.alto} L 0 0 Z`} fill={E.campo} />
      </svg>

      <Producto src={`${formato}-700${intervenido ? "-intervenido" : ""}.png`} {...L.p700} u={u} />
      <Producto src={`${formato}-911${intervenido ? "-intervenido" : ""}.png`} {...L.p911} u={u} />

      <Ficha
        nombre="700 Keratin & Kale Serum"
        serif="Controla el frizz"
        resto="y da más fuerza al pelo."
        {...L.ficha700}
        u={u}
        k={t}
        {...FICHA}
      />
      <Ficha
        nombre="911 Quinoa Serum"
        serif="Sella"
        resto="la cutícula y aporta brillo natural."
        {...L.ficha911}
        u={u}
        k={t}
        {...FICHA}
      />

      {/* titular: Scotch Condensed Roman + Medium Italic en nude */}
      <div
        style={{
          position: "absolute",
          top: L.titulo.y * u,
          left: (L.titulo.x ?? 0) * u,
          width: (L.titulo.w ?? L.mesaW) * u,
          textAlign: "center",
          color: E.texto,
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
            color: E.linea2,
          }}
        >
          un pelo en orden.
        </div>
        {L.cta.donde === "titulo" && <Cta t={t} u={u} color={E.texto} />}
      </div>

      {/* CTA al FINAL de la lectura (mail): centrado, bajo todo lo demás */}
      {L.cta.donde === "abajo" && (
        <div style={{position: "absolute", top: (L.cta.y ?? 0) * u, left: 0, width: W, textAlign: "center", color: E.texto}}>
          <Cta t={t} u={u} color={E.texto} />
        </div>
      )}

      {/* logotipo SELFIE vertical — en la grilla va en x 953, y 173 de la mesa de 1080 */}
      <Img
        src={staticFile("assets/selfie/2026-nuevo-estilo/selfie-logo-vertical.svg")}
        style={{position: "absolute", left: L.logo.x * u, top: L.logo.y * u, width: 37 * t * u}}
      />

      {/* flechas ENCIMA de todo: nada puede taparlas */}
      {capa !== "sinFlechas" && (
        <svg width={W} height={L.alto * u} viewBox={`0 0 ${L.mesaW} ${L.alto}`} style={{position: "absolute", inset: 0}}>
          <Flecha forma="700" start={L.start700} tip={L.tip700} k={t} color={E.flecha} />
          <Flecha forma="911" start={L.start911} tip={L.tip911} k={t} color={E.flecha} />
        </svg>
      )}

      {capa === "flechas" && <MascaraFlechas L={L} u={u} />}
    </AbsoluteFill>
  );
};
