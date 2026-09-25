// Texto sobre una superficie CURVA (un post-it que se despega del monitor y se curva).
// Una homografía sola aplana el papel; acá el rótulo se corta en tiras horizontales y
// cada tira va a su propio cuadrilátero, sacado del perfil medido fila a fila
// (`scripts/medir-postit.py` → postits.json: perfil = [[y, x_izq, x_der], ...]).
import React from "react";
import {matrix3d} from "./superficie";

export type Perfil = [number, number, number][]; // [y, xIzq, xDer] en px del clip (frame de referencia)
type P = [number, number];

/** Interpola el borde izquierdo y derecho del papel a una altura y (px del clip). */
const bordes = (perfil: Perfil, y: number): [number, number] => {
  if (y <= perfil[0][0]) return [perfil[0][1], perfil[0][2]];
  for (let i = 1; i < perfil.length; i++) {
    if (y <= perfil[i][0]) {
      const [y0, a0, b0] = perfil[i - 1], [y1, a1, b1] = perfil[i];
      const t = (y - y0) / (y1 - y0);
      return [a0 + (a1 - a0) * t, b0 + (b1 - b0) * t];
    }
  }
  const u = perfil[perfil.length - 1];
  return [u[1], u[2]];
};

/**
 * El contenido (w×h) se pega al papel entre `y0` e `y1` (px del clip, sobre el perfil),
 * con `margen` por lado como fracción del ancho del papel. `tiras` = cuántas franjas.
 * `filas` limita el perfil a las filas que NO están tapadas (p. ej. por una mano).
 */
export const SuperficieCurva: React.FC<{
  perfil: Perfil; y0: number; y1: number; w: number; h: number; margen?: number; tiras?: number;
  offsetY?: number; style?: React.CSSProperties; children: React.ReactNode;
}> = ({perfil, y0, y1, w, h, margen = 0.06, tiras = 12, offsetY = 0, style, children}) => {
  const franjas = Array.from({length: tiras}, (_, i) => {
    const ta = i / tiras, tb = (i + 1) / tiras;
    const ya = y0 + (y1 - y0) * ta, yb = y0 + (y1 - y0) * tb;
    const [la, ra] = bordes(perfil, ya), [lb, rb] = bordes(perfil, yb);
    const ma = (ra - la) * margen, mb = (rb - lb) * margen;
    const quad: P[] = [[la + ma, ya + offsetY], [ra - ma, ya + offsetY], [rb - mb, yb + offsetY], [lb + mb, yb + offsetY]];
    const hf = h / tiras;
    return (
      <div key={i} style={{position: "absolute", left: 0, top: 0, width: w, height: hf, overflow: "hidden", transformOrigin: "0 0",
        transform: matrix3d(w, hf, quad), ...style}}>
        <div style={{position: "absolute", left: 0, top: -i * hf, width: w, height: h}}>{children}</div>
      </div>
    );
  });
  return <>{franjas}</>;
};
