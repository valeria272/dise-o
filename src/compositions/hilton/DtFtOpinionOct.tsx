/**
 * DOUBLETREE · FEED col D · 10-10-2026 18:00 · ESTÁTICO – OPINIÓN (Google).
 * Estado de la grilla: OK PARA DISEÑO.
 *
 * ── RONDA 2 (Eli, 24-09): «si es Expedia es así el diseño» ────────────────
 * Eli mandó la opinión de Expedia ya aprobada (`raw/hilton/dt/ref-oct/
 * opinion-expedia-aprobada.png`, 2250×2813). ÉSA es la plantilla de las
 * opiniones de DT, y se calca MEDIDA (valores @1080×1350):
 *
 *   tarjeta clara #E7E4E3 · x 153→926 · y 276→896 · radio ≈30
 *   pestaña azul con el logotipo · y 232→329, centrada, montada sobre el canto
 *   título «Nombre: “cita”» · tinta 348→382 · Stag Regular espaciada + Semibold
 *   la tarjeta se CORTA en y ≈422 (se ve la foto por la ranura) y la valoración
 *   va montada en el corte · círculos de 38 en el verde DT, unidos por una línea
 *   cuerpo en Stag itálica azul · 10 líneas cada 33,1 · 473→795
 *   logotipo de la plataforma, a color · 822→868
 *   foto a sangre, SIN velo
 *
 * Cambios por ser Google y no Expedia (Eli eligió Google el 24-09 porque la
 * reseña que mandó Javier es de Google):
 *   · el logotipo de la plataforma es el de Google, a color como el de Expedia;
 *   · la valoración son ESTRELLAS (la de Google) con el mismo tratamiento de los
 *     círculos: verde DT, contorno azul y la línea que las une;
 *   · ⚠️ SIN bandera: la de Expedia marcaba el país de Gabriel; de Silvana la
 *     reseña no dice el país. Avisado a Eli.
 *
 * Textos literales de la reseña del brief; la cita es su primera oración, sin
 * punto (§F).
 *
 * Foto: el lobby lounge (`HDT_37`), la más cálida del banco («colores cálidos»).
 * ⚠️ QA: `respiro-borde` da falsa alarma (11 %). La regla mide TINTA BLANCA y esta
 * pieza no tiene texto blanco (va azul sobre la tarjeta): lo único blanco es el
 * logo de la pestaña, así que los brillos de la foto en el canto pesan como texto.
 * La opinión de Expedia aprobada pasa la misma regla. Se probaron `HDT_65`
 * (21 %, y se leía a Escapada Romántica) y `HDT_66` (fría, y el cielo raso liso
 * dispara «foto estirada»).
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';

cargarFuentesDT();

const MESA = {ancho: 1080, alto: 1350} as const;

const NOMBRE = 'Silvana:';
const CITA = '“Excelente experiencia”';
const CUERPO = [
  'El hotel tiene una muy buena ubicación, habitaciones cómodas y cuidadas y un desayuno muy completo, pero sin duda lo que más destacaría es la calidad humana y profesional de todo el personal.',
  'Desde nuestra llegada nos sentimos muy bien atendidas. Siempre encontramos amabilidad, disposición y una excelente actitud para ayudarnos en todo lo que necesitábamos. Es ese tipo de atención que realmente hace la diferencia durante una estadía.',
] as const;

const TARJETA = {x: 153, y: 276, ancho: 773, alto: 620, radio: 30, color: '#E7E4E3'} as const;
/** La ranura que parte la tarjeta; la valoración va montada encima. */
const CORTE = {y: 418, alto: 8} as const;
const PESTANA = {ancho: 98, alto: 97, y: 232, radio: 12} as const;
const VALORACION = {y: 399, diam: 46, paso: 60} as const;

const Estrella: React.FC<{x: number}> = ({x}) => (
  <path
    transform={`translate(${x - VALORACION.diam / 2} ${VALORACION.y}) scale(${VALORACION.diam / 24})`}
    d="M12 1.6l3.1 6.5 7.1.9-5.2 4.9 1.3 7.1L12 17.6l-6.3 3.4 1.3-7.1L1.8 9l7.1-.9z"
    fill={DT.colores.verde}
    stroke={DT.colores.azul}
    strokeWidth={1.3}
    strokeLinejoin="round"
  />
);

export const DtFtOpinionOct: React.FC<{guia?: boolean}> = ({guia = false}) => {
  const cx = MESA.ancho / 2;
  const xs = [-2, -1, 0, 1, 2].map((i) => cx + i * VALORACION.paso);
  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
      <Img src={staticFile('assets/hilton/dt/oct/op-fondo.jpg')} style={{width: '100%', height: '100%', objectFit: 'cover'}} />

      {/* la tarjeta, en dos piezas: la ranura deja ver la foto */}
      {[
        {top: TARJETA.y, alto: CORTE.y - TARJETA.y, r: `${TARJETA.radio}px ${TARJETA.radio}px 0 0`},
        {
          top: CORTE.y + CORTE.alto,
          alto: TARJETA.y + TARJETA.alto - CORTE.y - CORTE.alto,
          r: `0 0 ${TARJETA.radio}px ${TARJETA.radio}px`,
        },
      ].map((p) => (
        <div
          key={p.top}
          style={{
            position: 'absolute',
            left: TARJETA.x,
            top: p.top,
            width: TARJETA.ancho,
            height: p.alto,
            background: TARJETA.color,
            borderRadius: p.r,
            boxShadow: '0 6px 22px rgba(9,25,78,0.18)',
          }}
        />
      ))}

      {/* la pestaña azul con el logotipo DT blanco */}
      <div
        style={{
          position: 'absolute',
          left: cx - PESTANA.ancho / 2,
          top: PESTANA.y,
          width: PESTANA.ancho,
          height: PESTANA.alto,
          background: DT.colores.azul,
          borderRadius: PESTANA.radio,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Img
          src={staticFile('assets/hilton/dt/logo-dt-blanco.png')}
          style={{width: 78, height: 78 / DT.geometria.logoProporcion}}
        />
      </div>

      {/* «Nombre: “cita”» */}
      <div
        style={{
          position: 'absolute',
          left: TARJETA.x,
          top: 339,
          width: TARJETA.ancho,
          textAlign: 'center',
          fontFamily: DT.fuentes.titular,
          fontSize: 44,
          lineHeight: 1.2,
          color: DT.colores.azul,
          whiteSpace: 'nowrap',
        }}
      >
        <span style={{fontWeight: DT.pesos.regular, letterSpacing: '0.07em'}}>{NOMBRE} </span>
        <span style={{fontWeight: DT.pesos.semibold, letterSpacing: '0.03em'}}>{CITA}</span>
      </div>

      {/* la valoración montada en el corte */}
      <svg width={MESA.ancho} height={MESA.alto} style={{position: 'absolute', top: 0, left: 0}}>
        <path
          d={`M ${xs[0]} ${CORTE.y + CORTE.alto / 2} H ${xs[4]}`}
          stroke={DT.colores.azul}
          strokeWidth={2.2}
        />
        {xs.map((x) => (
          <Estrella key={x} x={x} />
        ))}
      </svg>

      {/* el cuerpo, en Stag itálica azul */}
      <div
        style={{
          position: 'absolute',
          left: TARJETA.x + 44,
          top: 468,
          width: TARJETA.ancho - 88,
          textAlign: 'center',
          fontFamily: DT.fuentes.titular,
          fontStyle: 'italic',
          fontWeight: DT.pesos.regular,
          fontSize: 29,
          lineHeight: '33.1px',
          color: DT.colores.azul,
        }}
      >
        {CUERPO.map((p) => (
          <div key={p}>{p}</div>
        ))}
      </div>

      {/* Google, a color como el Expedia de la plantilla */}
      <Img
        src={staticFile('assets/hilton/dt/oct/google-logo.svg')}
        style={{position: 'absolute', top: 818, left: cx - (48 * 272) / 92 / 2, height: 48, width: (48 * 272) / 92}}
      />

      {guia ? (
        <div style={{position: 'absolute', top: 0, left: cx, width: 1, height: MESA.alto, background: 'rgba(255,0,110,0.6)'}} />
      ) : null}
    </AbsoluteFill>
  );
};

export const DtFtOpinionOctGuia: React.FC = () => <DtFtOpinionOct guia />;
