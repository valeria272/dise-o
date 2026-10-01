/**
 * SANTA GOTA · carrusel de pauta «ELIGE TU PECADO» — 5 láminas 4:5 (1080×1350). 01-10-2026.
 *
 * Extiende el carrusel orgánico más nuevo de la cuenta («Cómo abrir tu Santa Gota», 24-09): foto REAL de la
 * jornada del 10-09 con el color subido + una capa dibujada a mano (titular de plumón blanco/lima, cinta de
 * papel con texto a mano, círculo lima, estrellas y rayitas). Nada de packshot recortado sobre fondo plano.
 *
 * Fotos: scripts/santagota-carrusel-paid-fotos.py → public/assets/santagota/paid-carrusel/0N.jpg (2160×2700).
 * Producto: el de la foto o el packshot oficial (lámina 5, sobre la banqueta del set). La IA no toca producto.
 * Precios: leídos de santagota.cl/products.json el 01-10-2026. Se vuelven a leer el día que se publica.
 * Zona segura de pauta: nada clave en los 60 px de borde ni en el 12 % inferior (y > 1188).
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

const DIR = "assets/santagota/paid-carrusel";
export const LIMA = "#C3D600";
const TINTA = "#111108";
const PAPEL = "#F4F1E8";

let cargadas = false;
const cargarFuentes = () => {
  if (cargadas || typeof document === "undefined") return;
  cargadas = true;
  const st = document.createElement("style");
  st.textContent = `
    @font-face{font-family:'Caveat Brush';src:url(${staticFile(`${DIR}/fuentes/CaveatBrush-Regular.ttf`)}) format('truetype');font-display:block}
    @font-face{font-family:'Kalam';font-weight:700;src:url(${staticFile(`${DIR}/fuentes/Kalam-Bold.ttf`)}) format('truetype');font-display:block}`;
  document.head.appendChild(st);
};
cargarFuentes();

export const brush: React.CSSProperties = {fontFamily: "'Caveat Brush'", lineHeight: 0.86, textTransform: "uppercase", whiteSpace: "nowrap"};
export const mano: React.CSSProperties = {fontFamily: "Kalam", fontWeight: 700, lineHeight: 1.02};

/* ───────── la capa dibujada ───────── */

/** Titular de plumón: líneas apiladas, inclinadas, con sombra suave para leerse sobre la foto. */
export const Titular: React.FC<{lineas: {t: string; c: string}[]; x: number; y: number; size: number; rot?: number}> = ({lineas, x, y, size, rot = -6}) => (
  <div style={{position: "absolute", left: x, top: y, transform: `rotate(${rot}deg)`, transformOrigin: "0 0"}}>
    {lineas.map((l, i) => (
      <div key={i} style={{...brush, fontSize: size, color: l.c, textShadow: "0 4px 18px rgba(40,0,10,0.35)", marginLeft: i * size * 0.06}}>
        {l.t}
      </div>
    ))}
  </div>
);

/** Trazo de plumón bajo una palabra. */
export const Subrayado: React.FC<{x: number; y: number; w: number; rot?: number; color?: string; grosor?: number}> = ({x, y, w, rot = -4, color = LIMA, grosor = 16}) => (
  <svg style={{position: "absolute", left: x, top: y, overflow: "visible", transform: `rotate(${rot}deg)`}} width={w} height={40}>
    <path d={`M4 ${24} C ${w * 0.3} 12, ${w * 0.6} 30, ${w - 4} 14`} stroke={color} strokeWidth={grosor} strokeLinecap="round" fill="none" />
    <path d={`M${w * 0.12} ${32} C ${w * 0.45} 24, ${w * 0.7} 34, ${w * 0.9} 26`} stroke={color} strokeWidth={grosor * 0.45} strokeLinecap="round" fill="none" opacity={0.85} />
  </svg>
);

/** Cinta de papel con texto a mano (borde rasgado a los lados). */
export const Cinta: React.FC<{x: number; y: number; rot?: number; size?: number; children: React.ReactNode; ancho?: number}> = ({x, y, rot = -3, size = 74, children, ancho}) => {
  const dientes = Array.from({length: 9}, (_, i) => i / 8);
  const izq = dientes.map((t, i) => `${i % 2 ? 2.2 : 0}% ${t * 100}%`).join(",");
  const der = dientes.reverse().map((t, i) => `${i % 2 ? 97.8 : 100}% ${t * 100}%`).join(",");
  return (
    <div style={{position: "absolute", left: x, top: y, transform: `rotate(${rot}deg)`, filter: "drop-shadow(0 6px 10px rgba(30,0,5,0.28))"}}>
      <div style={{background: PAPEL, padding: "16px 34px 20px", clipPath: `polygon(${izq},${der})`, width: ancho}}>
        <div style={{...mano, fontSize: size, color: TINTA}}>{children}</div>
      </div>
    </div>
  );
};

/** Círculo lima dibujado (contorno irregular) con el precio adentro. */
export const Precio: React.FC<{x: number; y: number; d: number; precio: string; arriba?: string; abajo?: string; antes?: string; rot?: number}> = ({x, y, d, precio, arriba, abajo, antes, rot = -8}) => {
  const r = d / 2;
  const pts = Array.from({length: 14}, (_, i) => {
    const a = (i / 14) * Math.PI * 2;
    const k = 1 + [0.02, -0.03, 0.04, -0.01, 0.03, -0.04, 0.01, 0.03, -0.02, 0.02, -0.03, 0.04, -0.02, 0.01][i];
    return [r + Math.cos(a) * r * k, r + Math.sin(a) * r * k];
  });
  const path = pts.map((p, i) => {
    const n = pts[(i + 1) % pts.length];
    const mx = (p[0] + n[0]) / 2;
    const my = (p[1] + n[1]) / 2;
    return `${i === 0 ? `M${mx} ${my}` : ""} Q${n[0]} ${n[1]} ${(n[0] + pts[(i + 2) % pts.length][0]) / 2} ${(n[1] + pts[(i + 2) % pts.length][1]) / 2}`;
  }).join(" ");
  return (
    <div style={{position: "absolute", left: x, top: y, width: d, height: d, transform: `rotate(${rot}deg)`}}>
      <svg width={d} height={d} style={{position: "absolute", inset: 0, overflow: "visible", filter: "drop-shadow(0 6px 12px rgba(30,0,5,0.3))"}}>
        <path d={path + " Z"} fill={LIMA} />
      </svg>
      <div style={{position: "absolute", inset: 0, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", color: TINTA}}>
        {arriba && <div style={{...mano, fontSize: d * 0.12, marginBottom: d * 0.01}}>{arriba}</div>}
        <div style={{...brush, fontSize: d * 0.27, lineHeight: 0.9}}>{precio}</div>
        {abajo && <div style={{...mano, fontSize: d * 0.1, marginTop: d * 0.02}}>{abajo}</div>}
        {antes && (
          <div style={{...mano, fontSize: d * 0.11, position: "relative", marginTop: d * 0.02}}>
            antes <span style={{textDecoration: "line-through", textDecorationThickness: 4}}>{antes}</span>
          </div>
        )}
      </div>
    </div>
  );
};

/** Rayitas de «¡ojo!» alrededor de un punto. */
export const Rayitas: React.FC<{x: number; y: number; r?: number; color?: string; desde?: number; hasta?: number}> = ({x, y, r = 70, color = "#fff", desde = 200, hasta = 340}) => {
  const n = 4;
  return (
    <svg style={{position: "absolute", left: x - r * 1.6, top: y - r * 1.6, overflow: "visible"}} width={r * 3.2} height={r * 3.2}>
      {Array.from({length: n}, (_, i) => {
        const a = ((desde + ((hasta - desde) * i) / (n - 1)) * Math.PI) / 180;
        const c = r * 1.6;
        return <line key={i} x1={c + Math.cos(a) * r} y1={c + Math.sin(a) * r} x2={c + Math.cos(a) * r * 1.45} y2={c + Math.sin(a) * r * 1.45} stroke={color} strokeWidth={9} strokeLinecap="round" />;
      })}
    </svg>
  );
};

/** Estrella a mano alzada (contorno). */
export const Estrella: React.FC<{x: number; y: number; s?: number; color?: string; rot?: number}> = ({x, y, s = 60, color = TINTA, rot = 0}) => {
  const p = Array.from({length: 10}, (_, i) => {
    const a = -Math.PI / 2 + (i * Math.PI) / 5;
    const rr = i % 2 ? s * 0.42 : s;
    return `${s + Math.cos(a) * rr},${s + Math.sin(a) * rr}`;
  }).join(" ");
  return (
    <svg style={{position: "absolute", left: x - s, top: y - s, transform: `rotate(${rot}deg)`, overflow: "visible"}} width={s * 2} height={s * 2}>
      <polygon points={p} fill="none" stroke={color} strokeWidth={7} strokeLinejoin="round" />
    </svg>
  );
};

/** Flecha curva a mano. */
export const Flecha: React.FC<{x: number; y: number; w: number; h: number; color?: string; espejo?: boolean; rot?: number}> = ({x, y, w, h, color = "#fff", espejo, rot = 0}) => (
  <svg style={{position: "absolute", left: x, top: y, overflow: "visible", transform: `${espejo ? "scaleX(-1) " : ""}rotate(${rot}deg)`}} width={w} height={h}>
    <path d={`M4 ${h * 0.2} C ${w * 0.35} ${h * 1.05}, ${w * 0.7} ${h * 0.95}, ${w - 10} ${h * 0.55}`} stroke={color} strokeWidth={9} fill="none" strokeLinecap="round" />
    <path d={`M${w - 52} ${h * 0.5} L${w - 8} ${h * 0.55} L${w - 34} ${h * 0.9}`} stroke={color} strokeWidth={9} fill="none" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

/** Aureola: la O de GOTA, un anillo blanco a mano. */
const Aureola: React.FC<{cx: number; cy: number; w: number}> = ({cx, cy, w}) => (
  <svg style={{position: "absolute", left: cx - w / 2 - 10, top: cy - w * 0.14 - 10, overflow: "visible"}} width={w + 20} height={w * 0.28 + 20}>
    <ellipse cx={w / 2 + 10} cy={w * 0.14 + 10} rx={w / 2} ry={w * 0.13} fill="none" stroke="#fff" strokeWidth={10} />
    <ellipse cx={w / 2 + 14} cy={w * 0.14 + 6} rx={w / 2 - 8} ry={w * 0.12} fill="none" stroke="#fff" strokeWidth={4} opacity={0.8} />
  </svg>
);

/** Flechas de recarga: dos arcos que se persiguen. */
const Recarga: React.FC<{cx: number; cy: number; r: number}> = ({cx, cy, r}) => (
  <svg style={{position: "absolute", left: cx - r - 20, top: cy - r - 20, overflow: "visible"}} width={r * 2 + 40} height={r * 2 + 40}>
    <g transform={`translate(${r + 20},${r + 20})`} stroke={LIMA} strokeWidth={10} fill="none" strokeLinecap="round" strokeLinejoin="round">
      <path d={`M ${-r} 0 A ${r} ${r} 0 0 1 ${r * 0.7} ${-r * 0.7}`} />
      <path d={`M ${r * 0.7 - 36} ${-r * 0.7 - 10} L ${r * 0.7} ${-r * 0.7} L ${r * 0.7 - 6} ${-r * 0.7 + 38}`} />
      <path d={`M ${r} 0 A ${r} ${r} 0 0 1 ${-r * 0.7} ${r * 0.7}`} />
      <path d={`M ${-r * 0.7 + 36} ${r * 0.7 + 10} L ${-r * 0.7} ${r * 0.7} L ${-r * 0.7 + 6} ${r * 0.7 - 38}`} />
    </g>
  </svg>
);

const Foto: React.FC<{n: string}> = ({n}) => <Img src={staticFile(`${DIR}/${n}.jpg`)} style={{position: "absolute", inset: 0, width: 1080, height: 1350, objectFit: "cover"}} />;

/* ───────── láminas ───────── */

/** 1 · Portada: el gancho. */
export const Lamina1: React.FC = () => (
  <AbsoluteFill>
    <Foto n="01" />
    <Titular x={64} y={96} size={150} lineas={[{t: "ELIGE TU", c: "#fff"}, {t: "PECADO", c: LIMA}]} />
    <Subrayado x={70} y={372} w={380} rot={-7} />
    <Rayitas x={640} y={120} r={42} desde={-50} hasta={50} />
    <Cinta x={500} y={950} rot={-4} size={66}><span style={{whiteSpace: "nowrap"}}>Desliza y elige.</span></Cinta>
    <Flecha x={700} y={1068} w={220} h={86} rot={-6} />
  </AbsoluteFill>
);

/** 2 · Cocinar y saltear, 750 ml. */
export const Lamina2: React.FC = () => (
  <AbsoluteFill>
    <Foto n="02" />
    <Rayitas x={540} y={120} r={44} desde={-60} hasta={30} />
    <Precio x={760} y={120} d={250} precio="$11.990" arriba="750 ml" rot={8} />
    <Cinta x={70} y={880} rot={-4} size={84}>Para el fuego.</Cinta>
    <div style={{position: "absolute", left: 96, top: 1036, ...mano, fontSize: 44, color: "#fff", transform: "rotate(-4deg)", textShadow: "0 3px 12px rgba(30,0,5,0.5)"}}>
      cocinar, saltear, dorar
    </div>
  </AbsoluteFill>
);

/** 3 · Aderezar y terminar, 500 ml. */
export const Lamina3: React.FC = () => (
  <AbsoluteFill>
    <Foto n="03" />
    <Cinta x={430} y={880} rot={3} size={84}>Para el final.</Cinta>
    <div style={{position: "absolute", left: 440, top: 1036, ...mano, fontSize: 42, color: "#fff", transform: "rotate(3deg)", textShadow: "0 3px 12px rgba(30,0,5,0.5)"}}>
      aderezar, terminar, chorrear
    </div>
    <Precio x={80} y={880} d={250} precio="$9.290" arriba="500 ml" rot={-8} />
    <Rayitas x={600} y={690} r={48} color={LIMA} desde={150} hasta={250} />
  </AbsoluteFill>
);

/** 4 · Latas de relleno 473 ml. */
export const Lamina4: React.FC = () => (
  <AbsoluteFill>
    <Foto n="04" />
    <Recarga cx={980} cy={560} r={58} />
    <Cinta x={60} y={70} rot={-3} size={72}>Usa, recarga, repite.</Cinta>
    <Precio x={70} y={860} d={260} precio="$7.490" arriba="desde" abajo="latas 473 ml" rot={-6} />
  </AbsoluteFill>
);

/** 5 · Milagro: los cuatro productos del Pack Completo levitan contra la pared del set (v2, 01-10: la banqueta «se veía fea»). */
export const Lamina5: React.FC = () => (
  <AbsoluteFill>
    <Foto n="05" />
    <Titular x={250} y={96} size={150} rot={-4} lineas={[{t: "MILAGRO.", c: LIMA}]} />
    <Aureola cx={540} cy={262} w={300} />
    <Cinta x={60} y={890} rot={-4} size={62}>Pack Completo</Cinta>
    <div style={{position: "absolute", left: 80, top: 1010, ...mano, fontSize: 40, color: "#fff", transform: "rotate(-4deg)", textShadow: "0 3px 12px rgba(30,0,5,0.5)", width: 380}}>
      los dos aceites + las dos latas de relleno
    </div>
    <Precio x={735} y={880} d={260} precio="$33.790" antes="$43.960" rot={7} />
  </AbsoluteFill>
);
