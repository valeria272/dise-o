// ============================================================================
// COPYWRITERS — intervenciones manuales
// ----------------------------------------------------------------------------
// Círculo, subrayado, tachado, flecha, garabato, nota, destello. Siempre en
// COPY PINK y siempre con una razón semántica: no se decora, se INTERVIENE.
//
// Tope duro: 1–2 intervenciones por pieza (tokens.json → topes). Una tercera
// marca no agrega énfasis, lo diluye — y convierte la pieza en una lámina de
// PowerPoint anotada.
//
// ── Por qué no son elipses ni líneas rectas ──────────────────────────────────
// Una elipse perfecta en rosado se lee como un óvalo de Illustrator, y ahí es
// donde una pieza empieza a oler a plantilla. Estos trazos se construyen así:
//
//   1. Se samplea el recorrido y se le suma ruido SEMBRADO (mismo `semilla`,
//      mismo dibujo — un garabato distinto en cada render sería irreproducible).
//   2. Los puntos se unen con Catmull-Rom convertido a Bézier: da la curva
//      continua de una muñeca, no la poligonal de un plotter.
//   3. Cada trazo se pinta 2–3 veces con grosor y opacidad decrecientes y un
//      micro-desfase. Eso imita la carga desigual de un marcador y produce
//      remates afinados en vez de topes planos.
//   4. El círculo SOBREPASA el punto de partida. Una mano nunca cierra justo.
// ============================================================================
import React from "react";
import {C, temblor, VOZ} from "./sistema";

type P = [number, number];

/** Catmull-Rom → Bézier cúbica. Es lo que convierte puntos en muñeca. */
const suavizar = (pts: P[], cerrar = false): string => {
  if (pts.length < 2) return "";
  const d: string[] = [`M ${pts[0][0].toFixed(2)} ${pts[0][1].toFixed(2)}`];
  const n = pts.length;
  for (let i = 0; i < n - 1; i++) {
    const p0 = pts[i === 0 ? (cerrar ? n - 1 : 0) : i - 1];
    const p1 = pts[i];
    const p2 = pts[i + 1];
    const p3 = pts[i + 2 < n ? i + 2 : cerrar ? (i + 2) % n : n - 1];
    const c1: P = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6];
    const c2: P = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
    d.push(
      `C ${c1[0].toFixed(2)} ${c1[1].toFixed(2)}, ${c2[0].toFixed(2)} ${c2[1].toFixed(2)}, ${p2[0].toFixed(2)} ${p2[1].toFixed(2)}`,
    );
  }
  return d.join(" ");
};

/** Pinta el mismo recorrido varias veces: carga desigual del marcador. */
const Pasadas: React.FC<{d: string; w: number; color: string; pasadas?: number}> = ({
  d, w, color, pasadas = 3,
}) => (
  <>
    {Array.from({length: pasadas}).map((_, i) => (
      <path
        key={i}
        d={d}
        fill="none"
        stroke={color}
        strokeWidth={w * (1 - i * 0.26)}
        strokeLinecap="round"
        strokeLinejoin="round"
        opacity={i === 0 ? 1 : 0.5 - i * 0.12}
        transform={`translate(${i * 0.9} ${i * -0.7})`}
      />
    ))}
  </>
);

const Lienzo: React.FC<{
  x: number; y: number; w: number; h: number; rot?: number; children: React.ReactNode;
}> = ({x, y, w, h, rot = 0, children}) => (
  <svg
    width={w} height={h} viewBox={`0 0 ${w} ${h}`}
    style={{position: "absolute", left: x, top: y, overflow: "visible",
            transform: rot ? `rotate(${rot}deg)` : undefined}}
  >
    {children}
  </svg>
);

// ---------------------------------------------------------------------------

/** RODEAR. Óvalo abierto que sobrepasa el arranque, como una mano de verdad. */
export const Circulo: React.FC<{
  x: number; y: number; w: number; h: number;
  color?: string; grosor?: number; semilla?: number; rot?: number; vueltas?: number;
}> = ({x, y, w, h, color = C.rosa, grosor = 7, semilla = 7, rot = -3, vueltas = 1}) => {
  const r = temblor(semilla);
  const cx = w / 2, cy = h / 2, rx = w / 2 - grosor, ry = h / 2 - grosor;
  const desde = -0.45, hasta = Math.PI * 2 * vueltas + 0.62; // el sobrepaso
  const n = Math.round(30 * vueltas);
  const pts: P[] = Array.from({length: n + 1}, (_, i) => {
    const a = desde + ((hasta - desde) * i) / n;
    const j = 1 + r() * 0.075;
    // El arranque y el remate se aprietan: la muñeca acelera al entrar y al salir.
    const k = i === 0 || i === n ? 0.955 : 1;
    return [cx + Math.cos(a) * rx * j * k, cy + Math.sin(a) * ry * j * k] as P;
  });
  return (
    <Lienzo x={x} y={y} w={w} h={h} rot={rot}>
      <Pasadas d={suavizar(pts)} w={grosor} color={color} />
    </Lienzo>
  );
};

/** SUBRAYAR. Arco leve, nunca recta: una regla no es una mano. */
export const Subrayado: React.FC<{
  x: number; y: number; w: number; color?: string; grosor?: number;
  semilla?: number; curva?: number; rot?: number;
}> = ({x, y, w, color = C.rosa, grosor = 8, semilla = 3, curva = 0.045, rot = 0}) => {
  const r = temblor(semilla);
  const n = 14;
  const pts: P[] = Array.from({length: n + 1}, (_, i) => {
    const t = i / n;
    return [
      t * w,
      grosor * 2 + Math.sin(t * Math.PI) * -w * curva + r() * grosor * 0.85,
    ] as P;
  });
  return (
    <Lienzo x={x} y={y} w={w} h={grosor * 6} rot={rot}>
      <Pasadas d={suavizar(pts)} w={grosor} color={color} />
    </Lienzo>
  );
};

/** TACHAR. Una sola pasada decidida, con ángulo. Anula lo que cruza. */
export const Tachado: React.FC<{
  x: number; y: number; w: number; color?: string; grosor?: number;
  semilla?: number; angulo?: number;
}> = ({x, y, w, color = C.rosa, grosor = 8, semilla = 11, angulo = -2.2}) => {
  const r = temblor(semilla);
  const n = 12;
  const pts: P[] = Array.from({length: n + 1}, (_, i) => {
    const t = i / n;
    return [t * w * 1.04 - w * 0.02, grosor * 2 + r() * grosor * 1.15] as P;
  });
  return (
    <Lienzo x={x} y={y} w={w} h={grosor * 5} rot={angulo}>
      <Pasadas d={suavizar(pts)} w={grosor} color={color} pasadas={2} />
    </Lienzo>
  );
};

/** DIRIGIR. Flecha curva con punta de dos trazos, no un triángulo relleno. */
export const Flecha: React.FC<{
  x: number; y: number; w: number; h: number;
  color?: string; grosor?: number; semilla?: number; rot?: number; curva?: number;
}> = ({x, y, w, h, color = C.rosa, grosor = 7, semilla = 5, rot = 0, curva = 0.55}) => {
  const r = temblor(semilla);
  const n = 16;
  const pts: P[] = Array.from({length: n + 1}, (_, i) => {
    const t = i / n;
    return [t * w + r() * 2.2, h * (1 - t) * curva + h * 0.2 + r() * 2.2] as P;
  });
  const [fx, fy] = pts[n];
  const [px, py] = pts[n - 2];
  const ang = Math.atan2(fy - py, fx - px);
  const L = Math.min(w, h) * 0.3;
  const punta = (giro: number) =>
    suavizar([
      [fx, fy],
      [fx - Math.cos(ang + giro) * L * 0.55 + r(), fy - Math.sin(ang + giro) * L * 0.55 + r()],
      [fx - Math.cos(ang + giro) * L, fy - Math.sin(ang + giro) * L],
    ]);
  return (
    <Lienzo x={x} y={y} w={w} h={h} rot={rot}>
      <Pasadas d={suavizar(pts)} w={grosor} color={color} pasadas={2} />
      <Pasadas d={punta(0.44)} w={grosor * 0.92} color={color} pasadas={2} />
      <Pasadas d={punta(-0.44)} w={grosor * 0.92} color={color} pasadas={2} />
    </Lienzo>
  );
};

/** ANULAR. Garabato denso — más violento que el tachado. Úsalo poco. */
export const Garabato: React.FC<{
  x: number; y: number; w: number; h: number;
  color?: string; grosor?: number; semilla?: number; zigzags?: number;
}> = ({x, y, w, h, color = C.rosa, grosor = 6, semilla = 13, zigzags = 7}) => {
  const r = temblor(semilla);
  const pts: P[] = [];
  for (let i = 0; i <= zigzags * 2; i++) {
    const t = i / (zigzags * 2);
    pts.push([t * w + r() * 12, (i % 2 ? h * 0.86 : h * 0.14) + r() * 14]);
  }
  return (
    <Lienzo x={x} y={y} w={w} h={h}>
      <Pasadas d={suavizar(pts)} w={grosor} color={color} pasadas={2} />
    </Lienzo>
  );
};

/** DESTACAR. El destello de seis puntas del sistema. Marca una anomalía. */
export const Destello: React.FC<{
  x: number; y: number; r?: number; color?: string; grosor?: number;
  semilla?: number; puntas?: number;
}> = ({x, y, r: R = 46, color = C.rosa, grosor = 5, semilla = 17, puntas = 6}) => {
  const t = temblor(semilla);
  return (
    <Lienzo x={x - R} y={y - R} w={R * 2} h={R * 2}>
      {Array.from({length: puntas}).map((_, i) => {
        const a = (i / puntas) * Math.PI * 2 + 0.2;
        const largo = R * (0.72 + Math.abs(t()) * 0.5);
        const d = suavizar([
          [R - Math.cos(a) * largo * 0.94, R - Math.sin(a) * largo * 0.94],
          [R + t() * 3, R + t() * 3],
          [R + Math.cos(a) * largo, R + Math.sin(a) * largo],
        ]);
        return <Pasadas key={i} d={d} w={grosor} color={color} pasadas={2} />;
      })}
    </Lienzo>
  );
};

/** ANOTAR. Texto a mano. La voz HUMAN — nunca como tipografía principal. */
export const Anotacion: React.FC<{
  x: number; y: number; texto: string;
  color?: string; size?: number; rot?: number; ancho?: number;
}> = ({x, y, texto, color = C.rosa, size = 46, rot = -4, ancho: w}) => (
  <div
    style={{
      position: "absolute", left: x, top: y, width: w,
      fontFamily: VOZ.mano, fontWeight: 700, fontSize: size, lineHeight: 0.98,
      color, transform: `rotate(${rot}deg)`, transformOrigin: "left top",
      whiteSpace: w ? "normal" : "pre",
    }}
  >
    {texto}
  </div>
);
