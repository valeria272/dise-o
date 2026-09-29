/**
 * DOUBLETREE · OCTUBRE 2026, segunda tanda — piezas comunes de las 6 que pasaron a
 * OK PARA DISEÑO el 28-09 (feriado ×3, Family Time feed, Coworking, carrusel «5 cosas»).
 *
 * Nada de acá es sistema nuevo: son los mismos aparatos de las piezas aprobadas
 * (`DtStFamilyTimeOct`, `C1 FT N1`, `C1 FT N2`), sacados a un archivo para no copiarlos seis veces.
 */
import React from 'react';
import {Img, staticFile} from 'remotion';

import {DT, volteaApertura} from '../../brand/doubletree';

export const SOMBRA = '0 2px 7px rgba(9,25,78,0.55), 0 0 2px rgba(9,25,78,0.4)';
export const TRADE_CN = "'Trade Gothic Cn', 'Trade Gothic', sans-serif";

/**
 * Texto en Stag con las dos salidas de la familia (R-03): `¿ ¡` como el signo de
 * cierre girado 180° y `$ % @ & + # *` en Trade.
 */
export const Stag: React.FC<{t: string}> = ({t}) => (
  <>
    {volteaApertura(t).map((s, i) =>
      s.flip ? (
        <span key={i} style={{display: 'inline-block', transform: 'rotate(180deg)'}}>
          {s.t}
        </span>
      ) : (
        <React.Fragment key={i}>
          {s.t.split(/([$%@&+#*])/).map((p, j) =>
            /^[$%@&+#*]$/.test(p) ? (
              <span key={j} style={{fontFamily: DT.fuentes.texto}}>
                {p}
              </span>
            ) : (
              <React.Fragment key={j}>{p}</React.Fragment>
            ),
          )}
        </React.Fragment>
      ),
    )}
  </>
);

/**
 * El TITULAR de una historia arranca siempre a la misma distancia del logo (Constanza, 29-09:
 * «deben estar en la misma separación del logo… apliquemos esto a todas las historias») y con
 * menos interlínea que antes (1,14 → 1,06). La norma era la mayúscula en y=488 (la de Servicios
 * 13-10); Eli la SUBIÓ a 440 el mismo día («un poco más arriba… después tapa a la familia»). `topTitulo` convierte eso al `top` de la caja según el cuerpo: Stag usa las métricas
 * win (942/219 sobre 1000) y la versal mide 700, así que la versal cae a
 * `top + fs·((lh − 1,161)/2 + 0,242)`. Medido contra los render: ±1 px.
 */
export const TITULO_STORY = {versal: 440, interlinea: 1.06} as const;
export const topTitulo = (fs: number, lh: number = TITULO_STORY.interlinea) =>
  Math.round(TITULO_STORY.versal - fs * ((lh - 1.161) / 2 + 0.242));

/** Logotipo vertical blanco (R-09), a su proporción real y en la posición de la plantilla. */
export const Logo: React.FC<{formato: 'story' | 'feed'; color?: 'blanco' | 'azul'; top?: number}> = ({
  formato,
  color = 'blanco',
  top,
}) => {
  const G = DT.geometria;
  const ancho = formato === 'story' ? G.logoAnchoStory : G.logoAncho;
  return (
    <Img
      src={staticFile(`assets/hilton/dt/logo-dt-${color}.png`)}
      style={{
        position: 'absolute',
        top: top ?? (formato === 'story' ? G.logoYStory : G.logoYFeed),
        left: (1080 - ancho) / 2,
        width: ancho,
        height: ancho / G.logoProporcion,
      }}
    />
  );
};

/**
 * Velo azul que NACE en α=0 y sube sin quiebre (R-13): paradas cada ~10 %, curva
 * cóncava, pie ≈ `pie`. `desde` es la fracción del alto donde empieza.
 */
export const Velo: React.FC<{desde: number; pie?: number; lado?: 'abajo' | 'arriba'}> = ({
  desde,
  pie = 0.58,
  lado = 'abajo',
}) => {
  const paradas = Array.from({length: 11}, (_, i) => {
    const t = i / 10;
    return `rgba(9,25,78,${(pie * Math.pow(t, 1.6)).toFixed(3)}) ${(desde * 100 + t * (100 - desde * 100)).toFixed(1)}%`;
  });
  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        background: `linear-gradient(to bottom, rgba(9,25,78,0) 0%, ${paradas.join(', ')})`,
        transform: lado === 'arriba' ? 'scaleY(-1)' : undefined,
      }}
    />
  );
};

/** Foto a sangre. */
export const Foto: React.FC<{src: string; style?: React.CSSProperties}> = ({src, style}) => (
  <Img
    src={staticFile(src)}
    style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', ...style}}
  />
);

/** La flecha en píldora de contorno de `C1 FT N1` (portada que invita a deslizar). */
export const FlechaPildora: React.FC<{ancho?: number; color?: string}> = ({ancho = 180, color = DT.colores.blanco}) => (
  <div
    style={{
      width: ancho,
      height: ancho * 0.29,
      border: `2px solid ${color}`,
      borderRadius: 999,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      boxSizing: 'border-box',
    }}
  >
    <svg width={ancho * 0.56} height={ancho * 0.1} viewBox="0 0 100 18">
      <line x1="0" y1="9" x2="92" y2="9" stroke={color} strokeWidth="2.2" />
      <path d="M78 2 L100 9 L78 16 L84 9 Z" fill={color} />
    </svg>
  </div>
);
