/**
 * DOUBLETREE · OCTUBRE 2026 — íconos de línea de las historias de Servicios y
 * Hilton Honors.
 *
 * Todos calcan el trazo de la cama de Eli (2,4 px @1080, puntas y uniones
 * redondas) y se dibujan en un cuadrado propio, sin estirarse a la ranura
 * (ronda 3 del Honors de septiembre: «esos íconos se ven achatados»).
 *
 * La etiqueta, el regalo y las monedas son los MISMOS dibujos del estático de
 * Hilton Honors aprobado (`DtFtHonors.tsx`), copiados tal cual. Los nuevos
 * —copa y cubiertos, taza y portátil, mancuerna— siguen su misma familia:
 * objetos con estructura interior, no siluetas.
 */
import React from 'react';
import {Img, staticFile} from 'remotion';

import {DT} from '../../brand/doubletree';

export const SOMBRA_IMG =
  'drop-shadow(0 2px 7px rgba(9,25,78,0.55)) drop-shadow(0 0 2px rgba(9,25,78,0.4))';

const trazo = {
  fill: 'none',
  stroke: DT.colores.blanco,
  strokeWidth: 2.4,
  strokeLinecap: 'round' as const,
  strokeLinejoin: 'round' as const,
};

const Svg: React.FC<{alto: number; children: React.ReactNode}> = ({alto, children}) => (
  <svg
    width={(alto * 71) / 57}
    height={alto}
    viewBox="0 0 71 57"
    style={{flexShrink: 0, filter: SOMBRA_IMG, overflow: 'visible'}}
  >
    <g {...trazo} strokeWidth={2.4 * (57 / alto)}>{children}</g>
  </svg>
);

export type NombreIcono =
  | 'etiqueta'
  | 'regalo'
  | 'monedas'
  | 'cama'
  | 'copa'
  | 'taza'
  | 'mancuerna';

export const Icono: React.FC<{n: NombreIcono; alto?: number}> = ({n, alto = 57}) => {
  if (n === 'cama') {
    // la cama es de Eli: PNG extraído de `C1 FT N2`, a su proporción real
    return (
      <Img
        src={staticFile('assets/hilton/dt/icono-cama-eli.png')}
        style={{height: alto, width: alto * (147 / 120), flexShrink: 0, filter: SOMBRA_IMG}}
      />
    );
  }
  const dibujo: Record<Exclude<NombreIcono, 'cama'>, React.ReactNode> = {
    etiqueta: (
      <>
        <path d="M11 24.5 L31.5 4 a4.6 4.6 0 0 1 3.3-1.4 H56 a4.6 4.6 0 0 1 4.6 4.6 V27 a4.6 4.6 0 0 1-1.4 3.3 L38.7 50.9 a4.6 4.6 0 0 1-6.5 0 L11 31 a4.6 4.6 0 0 1 0-6.5 Z" />
        <circle cx="51" cy="12.5" r="3.9" />
        <path d="M24.5 40 L40 24.5" />
        <circle cx="25" cy="25.5" r="2.7" />
        <circle cx="39.5" cy="39.5" r="2.7" />
      </>
    ),
    regalo: (
      <>
        <rect x="11.5" y="20" width="48" height="10.5" rx="2.6" />
        <path d="M16 30.5 V50.5 a2.6 2.6 0 0 0 2.6 2.6 h33.8 a2.6 2.6 0 0 0 2.6-2.6 V30.5" />
        <path d="M35.5 20 V53.1" />
        <path d="M35.5 20 c-8.2 0-12.8-2-12.8-6.6 a5.1 5.1 0 0 1 9-3.4 c2.4 2.8 3.8 6.7 3.8 10 Z" />
        <path d="M35.5 20 c8.2 0 12.8-2 12.8-6.6 a5.1 5.1 0 0 0-9-3.4 c-2.4 2.8-3.8 6.7-3.8 10 Z" />
      </>
    ),
    monedas: (
      <>
        <ellipse cx="35.5" cy="13.5" rx="23" ry="7.4" />
        <path d="M12.5 13.5 v10 a23 7.4 0 0 0 46 0 v-10" />
        <path d="M12.5 23.5 v10 a23 7.4 0 0 0 46 0 v-10" />
        <path d="M12.5 33.5 v10 a23 7.4 0 0 0 46 0 v-10" />
      </>
    ),
    // Restaurante & Bar: copa de cóctel + tenedor y cuchillo
    copa: (
      <>
        <path d="M12 6 H40 L26 24 Z" />
        <path d="M17.5 13 H34.5" />
        <path d="M26 24 V47" />
        <path d="M17 51 H35" />
        <path d="M49 5 V20 a4 4 0 0 0 4 4 a4 4 0 0 0 4-4 V5" />
        <path d="M53 5 V51" />
        <path d="M63.5 51 V5 c-3.8 2.6-5.6 8.4-5.6 15.4 c0 5 1.8 7.2 5.6 7.2" />
      </>
    ),
    // Coffee & Work Lounge: portátil abierto + taza humeante
    taza: (
      <>
        <rect x="6" y="10" width="36" height="24" rx="2.4" />
        <path d="M1.5 40 H46.5 l-3.4 4.6 H4.9 Z" />
        <path d="M49 28 H64 V44 a6 6 0 0 1-6 6 H55 a6 6 0 0 1-6-6 Z" />
        <path d="M64 32 h2.4 a3.6 3.6 0 0 1 0 7.2 H64" />
        <path d="M53 22 c-1.8-2.2 1.8-3.6 0-6" />
        <path d="M59.5 22 c-1.8-2.2 1.8-3.6 0-6" />
      </>
    ),
    // Wellness & Fitness: mancuerna
    mancuerna: (
      <>
        <path d="M22 28.5 H49" />
        <rect x="14" y="14" width="8" height="29" rx="2.4" />
        <rect x="49" y="14" width="8" height="29" rx="2.4" />
        <rect x="6" y="20" width="8" height="17" rx="2.4" />
        <rect x="57" y="20" width="8" height="17" rx="2.4" />
      </>
    ),
  };
  return <Svg alto={alto}>{dibujo[n]}</Svg>;
};

/**
 * Los signos que Stag NO trae (`+`, `&` — ver `stagSirve`) se componen en Trade
 * dentro de la misma línea; lo demás sigue en la fuente del bloque.
 */
export const ConTrade: React.FC<{t: string}> = ({t}) => (
  <>
    {t.split(/([+&])/).map((p, i) =>
      p === '+' || p === '&' ? (
        <span key={i} style={{fontFamily: DT.fuentes.texto}}>
          {p}
        </span>
      ) : (
        <React.Fragment key={i}>{p}</React.Fragment>
      ),
    )}
  </>
);
