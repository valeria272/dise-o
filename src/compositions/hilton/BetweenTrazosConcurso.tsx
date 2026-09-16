/**
 * BETWEEN — los trazos del CARRUSEL CONCURSO (16-09-2026)
 *
 * ⚠️ POR QUÉ ESTO EXISTE, Y POR QUÉ NO CONTRADICE EL MANUAL.
 * La regla de la marca es que «los globos y flechas salen del `.svg` de Eli. No
 * se dibujan a mano ni se generan con IA — ya existen y tienen el trazo de la
 * marca». Se respetó en la primera ronda de este carrusel: no se dibujó nada.
 *
 * En la ronda 2 Eli pidió lo contrario, explícitamente y para estas dos piezas:
 *
 *   «la segunda slide no se parece mucho a esta referencia 2. Solo un poco
 *    ambas, añade esas ilustraciones sencillas de la slide 2.»
 *
 * …y adjuntó el recorte del motivo que quiere: las **tres cuñas** que la `REF 2`
 * pone junto a la cabeza del sujeto. Es la misma excepción que ya se abrió el
 * 08-09 para las banderitas de la S3, con las mismas cuatro condiciones del
 * manual (§ «Cuándo SÍ se dibuja un trazo nuevo para Between»):
 *
 *   1. lo pide la diseñadora, para una pieza — ✅ hoy;
 *   2. el motivo NO existe en el `.svg` de Eli — ✅ no hay cuñas, ni chispas de
 *      cuatro puntas, ni flecha curva, ni estrella de contorno;
 *   3. va en **un solo color de la marca**, el café `#675B49` — ✅ `tinta`;
 *   4. trazo de **grosor constante con puntas redondeadas**, como el referente,
 *      y sin imitar el pincel de Brushwell ni los garabatos del `.svg`.
 *
 * ⚠️ Lo que NO se tomó de la REF 2: el papel arrugado, la cinta adhesiva, las
 * polaroids y los recuadros de programas. Eso no es un trazo: es otra dirección
 * de arte, y el encargo fue «solo un poco».
 *
 * Los cuatro motivos van sobre un `viewBox` fijo y se escalan por ancho, así que
 * se reusan en cualquier formato sin deformarse.
 */
import React from 'react';

export type Motivo = 'cunas' | 'chispa' | 'flecha' | 'estrella';

/** viewBox y proporción de cada motivo — el alto sale del ancho, nunca al revés. */
const VB: Record<Motivo, {w: number; h: number}> = {
  cunas: {w: 100, h: 78},
  chispa: {w: 100, h: 100},
  flecha: {w: 100, h: 92},
  estrella: {w: 100, h: 96},
};

/**
 * ⭐ LAS TRES CUÑAS — el motivo que Eli recortó de la REF 2.
 *
 * Son MACIZAS, no de línea, y eso es del referente: ahí son tres triángulos
 * alargados que se abren desde un punto, más anchos en el extremo de afuera.
 * Se dibujan como cuadriláteros para poder darles ese afinado —una línea de
 * grosor constante no lo consigue— y por eso son el único motivo de este
 * archivo que no lleva `stroke`.
 *
 * El abanico: tres cuñas a −22°, 0° y +22° desde un origen común, con largos
 * 0,86 · 1 · 0,86 para que el conjunto se lea como un gesto y no como tres
 * palos iguales.
 */
const Cunas: React.FC<{tinta: string}> = ({tinta}) => (
  <g fill={tinta}>
    <path d="M6 30 L20 22 L34 62 L24 68 Z" />
    <path d="M46 16 L60 16 L62 64 L52 66 Z" />
    <path d="M84 24 L96 34 L74 66 L66 60 Z" />
  </g>
);

/**
 * ⭐ LA CHISPA de cuatro puntas. Maciza, con los lados cóncavos: es la forma
 * que usa el referente y la que se lee a tamaño chico, donde una estrella de
 * cinco puntas se empasta.
 */
const Chispa: React.FC<{tinta: string}> = ({tinta}) => (
  <path
    fill={tinta}
    d="M50 2 C56 34 66 44 98 50 C66 56 56 66 50 98 C44 66 34 56 2 50 C34 44 44 34 50 2 Z"
  />
);

/** ⭐ LA FLECHA CURVA — trazo de grosor constante y punta redondeada. */
const Flecha: React.FC<{tinta: string}> = ({tinta}) => (
  <g fill="none" stroke={tinta} strokeWidth={7} strokeLinecap="round" strokeLinejoin="round">
    <path d="M8 10 C46 6 78 26 84 66" />
    <path d="M66 54 L85 70 L96 48" />
  </g>
);

/** ⭐ LA ESTRELLA de cinco puntas, de CONTORNO. Mismo grosor que la flecha. */
const Estrella: React.FC<{tinta: string}> = ({tinta}) => (
  <path
    fill="none"
    stroke={tinta}
    strokeWidth={7}
    strokeLinejoin="round"
    d="M50 6 L63 38 L96 40 L70 60 L79 92 L50 73 L21 92 L30 60 L4 40 L37 38 Z"
  />
);

const MOTIVOS: Record<Motivo, React.FC<{tinta: string}>> = {
  cunas: Cunas,
  chispa: Chispa,
  flecha: Flecha,
  estrella: Estrella,
};

/**
 * Un motivo, colocado en el lienzo de 1080.
 *
 * `x` e `y` son la esquina superior izquierda de su caja; `ancho` manda y el
 * alto sale de la proporción del `viewBox`. `giro` es opcional y va en grados.
 */
export const Trazo: React.FC<{
  cual: Motivo;
  x: number;
  y: number;
  ancho: number;
  giro?: number;
  tinta?: string;
  opacidad?: number;
}> = ({cual, x, y, ancho, giro = 0, tinta = '#675B49', opacidad = 1}) => {
  const vb = VB[cual];
  const Dibujo = MOTIVOS[cual];
  return (
    <svg
      viewBox={`0 0 ${vb.w} ${vb.h}`}
      width={ancho}
      height={(ancho * vb.h) / vb.w}
      style={{
        position: 'absolute',
        left: x,
        top: y,
        transform: giro ? `rotate(${giro}deg)` : undefined,
        opacity: opacidad,
        overflow: 'visible',
      }}
    >
      <Dibujo tinta={tinta} />
    </svg>
  );
};
