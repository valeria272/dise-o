import React from "react";
import {tierracalma as TC} from "../../brand/tierracalma";
import {SANS, SERIF} from "./sistema";

// =============================================================================
// TIERRA CALMA · MAPA EDITORIAL ESTÁTICO (slide 3 del carrusel del 01/09)
//
// No es un mapa real: orienta sin revelar el pin exacto — requisito del brief.
//
// LO QUE SE ARREGLÓ RESPECTO DE LA VERSIÓN ANTERIOR
// Las etiquetas chocaban con la línea de la ruta porque estaban ancladas al
// mismo punto que el nodo. Ahora cada hito declara `lado` y el texto se dibuja
// con `text-anchor` opuesto al trazado, separado por un radio de guarda fijo
// (GUARDA). El trazado, además, corre por una diagonal limpia y las etiquetas
// se reparten a los dos costados, así ninguna cruza la línea.
// =============================================================================

const NAVY = TC.colors.navy;
const ARENA = "#B9A57F";

type Hito = {x: number; y: number; nombre: string; nota?: string; lado: "izq" | "der"; grande?: boolean};

// Diagonal de nororiente (Santiago) a surponiente (el proyecto).
const HITOS: Hito[] = [
  {x: 838, y: 138, nombre: "Santiago", nota: "centro", lado: "izq"},
  {x: 648, y: 330, nombre: "Peaje Padre Hurtado", nota: "15 min del proyecto", lado: "izq"},
  {x: 466, y: 510, nombre: "Padre Hurtado", nota: "colegios · super · bancos", lado: "der"},
  {x: 300, y: 668, nombre: "Tierra Calma", nota: "Padre Hurtado · RM", lado: "der", grande: true},
];

const GUARDA = 44; // separación mínima entre el nodo y su etiqueta

export const MapaEstatico: React.FC = () => (
  <svg width={1080} height={880} viewBox="0 0 1080 880" style={{display: "block"}}>
    {/* retícula tenue, solo como textura de fondo */}
    <defs>
      <pattern id="tc-malla" width="46" height="46" patternUnits="userSpaceOnUse">
        <path d="M46 0H0v46" fill="none" stroke={NAVY} strokeOpacity="0.07" strokeWidth="1" />
      </pattern>
    </defs>
    <rect x="606" y="24" width="450" height="264" fill="url(#tc-malla)" />

    {/* curvas de nivel decorativas, lejos de las etiquetas */}
    <path d="M60 470c120-64 210-36 300-108" fill="none" stroke={ARENA} strokeOpacity="0.5" strokeWidth="1.2" />
    <path d="M46 528c132-70 232-40 330-120" fill="none" stroke={ARENA} strokeOpacity="0.35" strokeWidth="1.2" />

    {/* el trazado: Ruta 78 en navy hasta Padre Hurtado, camino local en arena */}
    <path d={`M${HITOS[0].x} ${HITOS[0].y} L${HITOS[1].x} ${HITOS[1].y} L${HITOS[2].x} ${HITOS[2].y}`} fill="none" stroke={NAVY} strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" />
    <path d={`M${HITOS[2].x} ${HITOS[2].y} L${HITOS[3].x} ${HITOS[3].y}`} fill="none" stroke={ARENA} strokeWidth="5" strokeLinecap="round" strokeDasharray="3 13" />

    {HITOS.map((h) => {
      const der = h.lado === "der";
      const tx = der ? h.x + GUARDA : h.x - GUARDA;
      const anchor = der ? "start" : "end";
      return (
        <g key={h.nombre}>
          {h.grande ? <circle cx={h.x} cy={h.y} r="26" fill={NAVY} opacity="0.14" /> : null}
          <circle cx={h.x} cy={h.y} r={h.grande ? 11 : 8.5} fill={h.grande ? NAVY : "#FFFFFF"} stroke={NAVY} strokeWidth="3.4" />
          {h.grande ? (
            <>
              <text x={tx} y={h.y + 14} textAnchor={anchor} fontFamily={SERIF} fontSize="62" fontWeight="400" fill={NAVY} letterSpacing="-1">
                {h.nombre}
              </text>
              <text x={tx + 4} y={h.y + 58} textAnchor={anchor} fontFamily={SANS} fontSize="26" fontWeight="500" fill={NAVY} opacity="0.62" letterSpacing="3.4">
                {(h.nota ?? "").toUpperCase()}
              </text>
            </>
          ) : (
            <>
              <text x={tx} y={h.y - 4} textAnchor={anchor} fontFamily={SANS} fontSize="30" fontWeight="600" fill={NAVY} letterSpacing="2.2">
                {h.nombre.toUpperCase()}
              </text>
              <text x={tx} y={h.y + 32} textAnchor={anchor} fontFamily={SANS} fontSize="25" fontWeight="400" fill={NAVY} opacity="0.6">
                {h.nota}
              </text>
            </>
          )}
        </g>
      );
    })}

    {/* rosa de los vientos mínima, en una esquina que ninguna etiqueta ocupa */}
    <g transform="translate(96,130)" opacity="0.5">
      <path d="M0 -34 L9 8 L0 0 L-9 8 Z" fill={NAVY} />
      <text x="0" y="38" textAnchor="middle" fontFamily={SANS} fontSize="21" fontWeight="600" fill={NAVY} letterSpacing="2.6">
        N
      </text>
    </g>
  </svg>
);
