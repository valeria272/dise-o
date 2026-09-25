// Texto EN PERSPECTIVA pegado a una superficie trackeada (scripts/seguir-plano.py).
// El JSON trae H[k]: coords del frame de referencia → frame k del clip (px del clip).
// Se proyectan las 4 esquinas del rótulo y se arma un matrix3d rect→cuadrilátero.
import React from "react";

export type Track = {ref: number; w: number; h: number; fps: number; H: Record<string, number[]>};
type P = [number, number];

const aplicar = (H: number[], [x, y]: P): P => {
  const w = H[6] * x + H[7] * y + H[8];
  return [(H[0] * x + H[1] * y + H[2]) / w, (H[3] * x + H[4] * y + H[5]) / w];
};

/** Homografía del cuadrado unitario al cuadrilátero q (Heckbert). */
const cuadradoA = (q: P[]): number[] => {
  const [[x0, y0], [x1, y1], [x2, y2], [x3, y3]] = q;
  const dx1 = x1 - x2, dx2 = x3 - x2, dy1 = y1 - y2, dy2 = y3 - y2;
  const sx = x0 - x1 + x2 - x3, sy = y0 - y1 + y2 - y3;
  const den = dx1 * dy2 - dx2 * dy1;
  const g = (sx * dy2 - dx2 * sy) / den, h = (dx1 * sy - sx * dy1) / den;
  return [x1 - x0 + g * x1, x3 - x0 + h * x3, x0, y1 - y0 + g * y1, y3 - y0 + h * y3, y0, g, h, 1];
};

/** matrix3d que lleva un div de w×h (origen 0,0) al cuadrilátero q (TL, TR, BR, BL). */
export const matrix3d = (w: number, h: number, q: P[]): string => {
  const m = cuadradoA(q);
  const [a, b, c, d, e, f, g, hh] = [m[0] / w, m[1] / h, m[2], m[3] / w, m[4] / h, m[5], m[6] / w, m[7] / h];
  return `matrix3d(${[a, d, 0, g, b, e, 0, hh, 0, 0, 1, 0, c, f, 0, 1].join(",")})`;
};

/** Frame del clip visible en el frame `f` de la secuencia (desde en s, vel = playbackRate). */
export const frameClip = (t: Track, f: number, desde: number, vel: number) =>
  Math.floor((desde + (f / 30) * vel) * t.fps);

/**
 * El rótulo se diseña en un div de w×h y se lleva al cuadrilátero `quad` (coords del
 * frame de referencia, px del clip), transformado por H del frame actual.
 * `dy` corre el cuadrilátero en y antes de proyectar (p. ej. papel que avanza).
 */
export const Superficie: React.FC<{
  track: Track; k: number; quad: P[]; w: number; h: number; offsetY?: number; style?: React.CSSProperties; children: React.ReactNode;
}> = ({track, k, quad, w, h, offsetY = 0, style, children}) => {
  const claves = Object.keys(track.H).map(Number);
  const kk = Math.max(Math.min(...claves), Math.min(Math.max(...claves), k));
  const H = track.H[String(kk)];
  const q = quad.map((p) => aplicar(H, p)).map(([x, y]) => [x, y + offsetY] as P);
  return (
    <div style={{position: "absolute", left: 0, top: 0, width: w, height: h, transformOrigin: "0 0", transform: matrix3d(w, h, q), ...style}}>
      {children}
    </div>
  );
};
