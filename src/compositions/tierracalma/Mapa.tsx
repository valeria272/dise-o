import React from "react";
import {AbsoluteFill, interpolate, useCurrentFrame} from "remotion";
import {TC, SANS, SERIF} from "./kit";

// =============================================================================
// Mapa editorial de Tierra Calma — dibujado a mano en SVG, NO un mapa real.
// Es un esquema de orientación: Santiago arriba a la derecha, la Autopista del
// Sol bajando al surponiente, Padre Hurtado y, al final del camino, el proyecto.
//
// OJO CON LA RUTA: se llega por la **Autopista del Sol (Ruta 78)**, salida
// Padre Hurtado — NO por la Ruta 68 (esa es la Santiago–Valparaíso por
// Curacaví, y no tiene salida a Padre Hurtado). El brief original de la grilla
// decía "Ruta 68"; está corregido acá contra la ficha técnica del proyecto.
//
// El viewBox es 1080×1920 (el mismo del reel) para que nada se recorte.
// =============================================================================

const VB_W = 1080;
const VB_H = 1920;

type Pt = {x: number; y: number};

const P_SANTIAGO: Pt = {x: 838, y: 306};
const P_PEAJE: Pt = {x: 648, y: 706};
const P_PUEBLO: Pt = {x: 452, y: 1014};
const P_CONAF: Pt = {x: 336, y: 1188};
const P_TC: Pt = {x: 236, y: 1352};

// Trazado principal: Santiago → peaje → Padre Hurtado.
const RUTA_78 = `M ${P_SANTIAGO.x} ${P_SANTIAGO.y} C 800 452, 726 590, ${P_PEAJE.x} ${P_PEAJE.y} S 512 918, ${P_PUEBLO.x} ${P_PUEBLO.y}`;
// Tramo final: del pueblo al proyecto, por el camino a la Cuesta Barriga.
const CAMINO = `M ${P_PUEBLO.x} ${P_PUEBLO.y} C 402 1092, ${P_CONAF.x} ${P_CONAF.y}, 300 1240 S ${P_TC.x + 30} 1310, ${P_TC.x} ${P_TC.y}`;

// Relieve: lomas suaves al poniente, que es lo que hay entre el pueblo y el
// proyecto (Cuesta Barriga). Puro grafismo, sin pretensión topográfica.
const LOMAS = [
  "M -60 1180 C 60 1108, 150 1150, 250 1096",
  "M -60 1300 C 70 1222, 170 1268, 280 1208",
  "M -60 1424 C 80 1342, 190 1392, 310 1328",
  "M -60 1552 C 90 1466, 210 1520, 340 1452",
];

const Draw: React.FC<{
  d: string;
  p: number;
  width?: number;
  color?: string;
  opacity?: number;
}> = ({d, p, width = 7, color = TC.colors.navy, opacity = 1}) => (
  <path
    d={d}
    fill="none"
    stroke={color}
    strokeWidth={width}
    strokeLinecap="round"
    pathLength={1}
    strokeDasharray={1}
    strokeDashoffset={1 - p}
    opacity={opacity}
  />
);

// Punto de referencia sobre el mapa: círculo + etiqueta.
const Marca: React.FC<{
  at: Pt;
  label: string;
  sub?: string;
  p: number;
  side?: "left" | "right";
  big?: boolean;
}> = ({at, label, sub, p, side = "right", big}) => {
  if (p <= 0) return null;
  const r = big ? 15 : 9;
  const scale = interpolate(p, [0, 1], [0.2, 1]);
  const dx = side === "right" ? 32 : -32;
  const anchor = side === "right" ? "start" : "end";
  return (
    <g opacity={p} transform={`translate(${at.x} ${at.y})`}>
      {big && <circle r={r * 2.8 * scale} fill={TC.colors.navy} opacity={0.1} />}
      <circle r={r * scale} fill={big ? TC.colors.navy : TC.colors.paper} stroke={TC.colors.navy} strokeWidth={big ? 0 : 5} />
      <text
        x={dx}
        y={big ? 2 : 2}
        textAnchor={anchor}
        fontFamily={big ? SERIF : SANS}
        fontSize={big ? 62 : 25}
        fontWeight={600}
        letterSpacing={big ? "-0.01em" : "0.15em"}
        fill={TC.colors.navy}
      >
        {big ? label : label.toUpperCase()}
      </text>
      {sub && (
        <text
          x={dx}
          y={big ? 48 : 32}
          textAnchor={anchor}
          fontFamily={SANS}
          fontSize={big ? 24 : 21}
          fontWeight={400}
          letterSpacing={big ? "0.2em" : "0.08em"}
          fill={TC.colors.navy}
          opacity={0.6}
        >
          {sub}
        </text>
      )}
    </g>
  );
};

// Malla urbana esquemática de Santiago: unas cuantas manzanas, nada más.
const Ciudad: React.FC<{p: number}> = ({p}) => {
  const cells: React.ReactNode[] = [];
  for (let c = 0; c < 4; c++) {
    for (let r = 0; r < 4; r++) {
      cells.push(
        <rect
          key={`${c}-${r}`}
          x={820 + c * 48}
          y={112 + r * 48}
          width={32}
          height={32}
          fill="none"
          stroke={TC.colors.navy}
          strokeWidth={2}
          opacity={Math.max(0, 1 - (c + r) * 0.13)}
        />,
      );
    }
  }
  return <g opacity={p * 0.42}>{cells}</g>;
};

// Etiqueta de la autopista: horizontal en el aire libre de la izquierda, con
// una línea guía hasta el trazado. Más legible que rotarla sobre el camino.
const EtiquetaRuta: React.FC<{p: number}> = ({p}) => (
  <g opacity={p}>
    <line x1={604} y1={524} x2={744} y2={524} stroke={TC.colors.navy} strokeWidth={1.5} opacity={0.35} />
    <circle cx={744} cy={524} r={5} fill={TC.colors.navy} opacity={0.55} />
    <text x={168} y={512} fontFamily={SANS} fontSize={24} fontWeight={600} letterSpacing="0.15em" fill={TC.colors.navy}>
      AUTOPISTA DEL SOL · RUTA 78
    </text>
    <text x={168} y={568} fontFamily={SANS} fontSize={22} fontWeight={400} letterSpacing="0.08em" fill={TC.colors.navy} opacity={0.6}>
      Salida Padre Hurtado
    </text>
  </g>
);

export const Mapa: React.FC<{
  /** 0→1: avance del dibujo del trazado */
  progress: number;
  /** zoom del encuadre; 1 = mapa completo */
  zoom?: number;
  /** centro del zoom en coordenadas del viewBox */
  focus?: Pt;
  /** qué marcas mostrar (0→1 cada una) */
  show?: {peaje?: number; pueblo?: number; tc?: number; conaf?: number};
  /** etiqueta de la autopista: se apaga en los planos cerrados y cuando ya se dijo */
  showRuta?: boolean;
  /** comprime el trazado en vertical (1 = sin comprimir). Las etiquetas NO se
   *  achican: solo se acerca la geometría, para encuadres menos altos que 9:16. */
  vScale?: number;
}> = ({progress, zoom = 1, focus = {x: VB_W / 2, y: VB_H / 2}, show = {}, showRuta = true, vScale = 1}) => {
  const frame = useCurrentFrame();
  // Deriva lentísima: el mapa nunca queda completamente quieto.
  const drift = Math.sin(frame / 90) * 5;

  const tx = (VB_W / 2 - focus.x) * (zoom - 1);
  const ty = (VB_H / 2 - focus.y) * (zoom - 1);

  // Centro de la compresión: el medio del recorrido, no el del lienzo.
  const CY = (P_SANTIAGO.y + P_TC.y) / 2;
  const vy = (y: number) => CY + (y - CY) * vScale;
  const at = (pt: Pt): Pt => ({x: pt.x, y: vy(pt.y)});

  const pRuta = interpolate(progress, [0, 0.66], [0, 1], {extrapolateRight: "clamp"});
  const pCamino = interpolate(progress, [0.6, 1], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});

  return (
    <AbsoluteFill style={{background: TC.colors.cream, overflow: "hidden"}}>
      <svg
        viewBox={`0 0 ${VB_W} ${VB_H}`}
        width="100%"
        height="100%"
        preserveAspectRatio="xMidYMid slice"
        style={{
          transform: `scale(${zoom}) translate(${tx / zoom + drift}px, ${ty / zoom}px)`,
          transformOrigin: "center",
        }}
      >
        <defs>
          <radialGradient id="tc-paper" cx="40%" cy="30%" r="82%">
            <stop offset="0%" stopColor="#FCF8F0" />
            <stop offset="100%" stopColor={TC.colors.cream} />
          </radialGradient>
        </defs>
        <rect x={-300} y={-300} width={VB_W + 600} height={VB_H + 600} fill="url(#tc-paper)" />

        <g transform={`translate(0 ${CY}) scale(1 ${vScale}) translate(0 ${-CY})`}>
          {/* relieve del poniente */}
          {LOMAS.map((d, i) => (
            <Draw key={i} d={d} p={1} width={2} opacity={0.14 - i * 0.02} />
          ))}
          <Ciudad p={pRuta} />
          <Draw d={RUTA_78} p={pRuta} width={9} />
          <Draw d={CAMINO} p={pCamino} width={5} color={TC.colors.sand} />
        </g>

        {showRuta && vScale === 1 && <EtiquetaRuta p={interpolate(pRuta, [0.3, 0.62], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})} />}

        <Marca at={at(P_SANTIAGO)} label="Santiago" sub="centro" p={pRuta > 0.04 ? 1 : 0} side="left" />
        <Marca at={at(P_PEAJE)} label="Peaje Padre Hurtado" sub="15 min del proyecto" p={show.peaje ?? 0} side="left" />
        <Marca at={at(P_PUEBLO)} label="Padre Hurtado" sub="colegios · super · bancos" p={show.pueblo ?? 0} side="right" />
        <Marca at={at(P_CONAF)} label="Brigada Roble-17 · CONAF" p={show.conaf ?? 0} side="right" />
        <Marca at={at(P_TC)} label="Tierra Calma" sub="PADRE HURTADO · RM" p={show.tc ?? 0} side="right" big />
      </svg>
    </AbsoluteFill>
  );
};

export const MAPA_PUNTOS = {P_SANTIAGO, P_PEAJE, P_PUEBLO, P_CONAF, P_TC};
