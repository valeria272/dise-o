// ============================================================================
// COPYLAB — las intervenciones a mano del sistema
// ----------------------------------------------------------------------------
// El MASTER SYSTEM v1.0 dice que el rosado NO es decoración: tiene que hacer
// algo — señalar, subrayar, corregir, conectar, tachar, medir, revelar,
// intervenir. Estos son esos verbos, dibujados.
//
// Todos son SVG con trazo irregular a propósito. Un círculo perfecto se lee
// como forma; uno con el cierre pasado y el grosor desparejo se lee como
// alguien que agarró un plumón y marcó la pieza. Esa diferencia es el sistema
// entero: la mano encima del dato.
//
// Regla de uso: UNA intervención por pieza. Dos ya no marcan nada, decoran.
// ============================================================================
import React from "react";
import {C, MANUSCRITA, MONO} from "./gcl";

type Comun = {color?: string; grosor?: number; op?: number};

/** Círculo a mano alrededor de una palabra. El trazo cierra pasado, como un
 *  óvalo hecho rápido. Va en posición absoluta sobre el texto que marca. */
export const Circulo: React.FC<Comun & {
  x: number; y: number; ancho: number; alto: number;
}> = ({x, y, ancho, alto, color = C.rosado, grosor = 7, op = 1}) => {
  const rx = ancho / 2;
  const ry = alto / 2;
  // Elipse abierta que se pasa ~35° del punto de partida: el gesto de quien
  // cierra el círculo sin levantar la mano.
  const d = [
    `M ${ancho * 0.94} ${ry * 0.72}`,
    `C ${ancho * 0.99} ${ry * 1.5}, ${ancho * 0.82} ${alto * 0.99}, ${rx} ${alto * 0.97}`,
    `C ${ancho * 0.16} ${alto * 0.95}, ${-ancho * 0.02} ${ry * 1.42}, ${ancho * 0.03} ${ry * 0.82}`,
    `C ${ancho * 0.08} ${ry * 0.2}, ${ancho * 0.34} ${alto * 0.02}, ${rx * 1.06} ${alto * 0.04}`,
    `C ${ancho * 0.78} ${alto * 0.06}, ${ancho * 0.98} ${ry * 0.34}, ${ancho * 0.97} ${ry * 1.06}`,
  ].join(" ");
  return (
    <svg
      width={ancho} height={alto} viewBox={`0 0 ${ancho} ${alto}`}
      style={{position: "absolute", left: x, top: y, overflow: "visible", opacity: op}}
    >
      <path d={d} fill="none" stroke={color} strokeWidth={grosor} strokeLinecap="round" />
    </svg>
  );
};

/** Subrayado a mano. Dos pasadas cuando `doble`, como quien recalca. */
export const Subrayado: React.FC<Comun & {
  x: number; y: number; ancho: number; doble?: boolean;
}> = ({x, y, ancho, color = C.rosado, grosor = 6, doble = false, op = 1}) => (
  <svg
    width={ancho} height={26} viewBox={`0 0 ${ancho} 26`}
    style={{position: "absolute", left: x, top: y, overflow: "visible", opacity: op}}
  >
    <path
      d={`M 2 9 C ${ancho * 0.26} 2, ${ancho * 0.62} 14, ${ancho - 3} 6`}
      fill="none" stroke={color} strokeWidth={grosor} strokeLinecap="round"
    />
    {doble ? (
      <path
        d={`M ${ancho * 0.06} 20 C ${ancho * 0.34} 14, ${ancho * 0.7} 24, ${ancho * 0.96} 17`}
        fill="none" stroke={color} strokeWidth={grosor * 0.72} strokeLinecap="round" opacity={0.75}
      />
    ) : null}
  </svg>
);

/** Tachado: corrige. Se usa cuando la pieza niega algo que la gente da por
 *  cierto — es el verbo «corregir» del sistema. */
export const Tachado: React.FC<Comun & {x: number; y: number; ancho: number}> = ({
  x, y, ancho, color = C.rosado, grosor = 7, op = 1,
}) => (
  <svg
    width={ancho} height={20} viewBox={`0 0 ${ancho} 20`}
    style={{position: "absolute", left: x, top: y, overflow: "visible", opacity: op}}
  >
    <path
      d={`M 0 13 C ${ancho * 0.3} 5, ${ancho * 0.66} 15, ${ancho} 6`}
      fill="none" stroke={color} strokeWidth={grosor} strokeLinecap="round"
    />
  </svg>
);

/** Flecha curva a mano. Conecta una nota con lo que señala. `giro` invierte la
 *  curvatura para cuando la nota va al otro lado. */
export const Flecha: React.FC<Comun & {
  x: number; y: number; ancho: number; alto: number; giro?: boolean;
}> = ({x, y, ancho, alto, color = C.rosado, grosor = 5, giro = false, op = 1}) => {
  const d = giro
    ? `M ${ancho} 4 C ${ancho * 0.42} ${alto * 0.1}, ${ancho * 0.12} ${alto * 0.44}, 6 ${alto - 6}`
    : `M 4 4 C ${ancho * 0.58} ${alto * 0.1}, ${ancho * 0.88} ${alto * 0.44}, ${ancho - 6} ${alto - 6}`;
  // La punta se dibuja como dos trazos sueltos, no como un triángulo relleno:
  // un triángulo perfecto delata que la flecha no es a mano.
  const px = giro ? 6 : ancho - 6;
  const py = alto - 6;
  const s = alto * 0.22;
  return (
    <svg
      width={ancho} height={alto} viewBox={`0 0 ${ancho} ${alto}`}
      style={{position: "absolute", left: x, top: y, overflow: "visible", opacity: op}}
    >
      <path d={d} fill="none" stroke={color} strokeWidth={grosor} strokeLinecap="round" />
      <path
        d={`M ${px} ${py} L ${px + (giro ? s * 0.9 : -s * 0.9)} ${py - s * 0.5}`}
        fill="none" stroke={color} strokeWidth={grosor} strokeLinecap="round"
      />
      <path
        d={`M ${px} ${py} L ${px + (giro ? s * 0.15 : -s * 0.15)} ${py - s * 1.05}`}
        fill="none" stroke={color} strokeWidth={grosor} strokeLinecap="round"
      />
    </svg>
  );
};

/** Nota manuscrita. Es la voz de quien hizo la pieza metida dentro de la pieza:
 *  «Buenas ideas acá», «Otro día en terreno», «G.CL on duty». Siempre corta,
 *  siempre en rosado, siempre acompañada de una flecha que apunta a algo. */
export const Nota: React.FC<{
  texto: string; x: number; y: number; tam?: number; color?: string;
  giro?: number; ancho?: number;
}> = ({texto, x, y, tam = 46, color = C.rosado, giro = -6, ancho}) => (
  <div
    style={{
      position: "absolute", left: x, top: y, width: ancho,
      fontFamily: MANUSCRITA, fontWeight: 600, fontSize: tam, lineHeight: 1.08,
      color, transform: `rotate(${giro}deg)`, transformOrigin: "left top",
    }}
  >
    {texto}
  </div>
);

/** El rótulo de sección en mono: SEÑAL / 025, WORK / MY ZOO, FIELD NOTES / PAID.
 *  Es lo que convierte publicaciones sueltas en una cuenta con voz. */
export const Rotulo: React.FC<{
  pilar: string; detalle?: string; color?: string; acento?: string; tam?: number;
}> = ({pilar, detalle, color = "rgba(255,255,255,0.62)", acento = C.rosado, tam = 21}) => (
  <span style={{
    fontFamily: MONO, fontWeight: 500, fontSize: tam, letterSpacing: 2.4,
    textTransform: "uppercase", color, whiteSpace: "nowrap",
  }}>
    {pilar}
    {detalle ? (
      <>
        <span style={{opacity: 0.45}}>{"  /  "}</span>
        <span style={{color: acento}}>{detalle}</span>
      </>
    ) : null}
  </span>
);
