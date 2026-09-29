/**
 * BETWEEN · FEED 12-10 · REEL «POR QUÉ VIENES / POR QUÉ TE QUEDAS»
 *
 * Grilla BW OCT, FEED col L (OK PARA DISEÑAR desde el 25-09; antes ST 09-10,
 * «me gusta más para reel»). Brief: pantalla dividida siguiendo la referencia
 * (instagram.com/p/Dc_mPvau3s0): a un lado lo que genera el antojo, al otro
 * todo lo que hace que la experiencia vaya más allá del café. Clips cortos y
 * naturales, manos y momentos reales. Texto en pantalla: los dos rótulos.
 *
 * La referencia manda (R-56): dos mitades verticales de 540 px pegadas, sin
 * marco ni divisor, un rótulo corto centrado en cada mitad. Traducido a
 * Between: Raleway SemiBold en beige de marca con la sombra café del sistema.
 * El rótulo va ARRIBA (no al medio como la ref) porque al medio está el
 * producto (R-41). Cortes secos y sincronizados cada 1,6 s; la última toma
 * se queda un poco más. Sin lockup: el vaso To Go de la última toma firma (R-33).
 * ⛔ R-53: ningún rostro — tramos y encuadres elegidos a mano.
 * Clips: `scripts/bw-fd-12-10-porque-vienes-clips.py`.
 */
import React from 'react';
import {AbsoluteFill, OffthreadVideo, Sequence, staticFile} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
import {useFuentesListas} from './BetweenSistema';

const P = 'assets/hilton/between/oct/porque/';
const C = BETWEEN.colores;
const TOMA = 48; // 1,6 s
const COLA = 18; // la última toma se queda 0,6 s más

type Toma = {clip: string; x?: number}; // x = objectPosition horizontal (%)

const VIENES: Toma[] = [
  {clip: 'v1-cafe', x: 38},
  {clip: 'v2-latte', x: 45},
  {clip: 'v3-desayuno', x: 50},
  {clip: 'v4-croissant', x: 60},
  {clip: 'v5-dulce', x: 52},
  {clip: 'v6-osito', x: 50},
  {clip: 'v7-togo', x: 84},
];
const QUEDAS: Toma[] = [
  {clip: 'q1-barista', x: 40},
  {clip: 'q2-sirviendo', x: 32},
  {clip: 'q3-mesa', x: 55},
  {clip: 'q4-espacio', x: 50},
  {clip: 'q5-detalle', x: 55},
  {clip: 'q6-cowork', x: 50},
  {clip: 'q7-relajo', x: 62},
];

export const DURACION_PORQUE = VIENES.length * TOMA + COLA;

const Mitad: React.FC<{tomas: Toma[]; left: number; rotulo: string}> = ({tomas, left, rotulo}) => (
  <div style={{position: 'absolute', left, top: 0, width: 540, height: 1920, overflow: 'hidden'}}>
    {tomas.map((t, i) => (
      <Sequence
        key={t.clip}
        from={i * TOMA}
        durationInFrames={i === tomas.length - 1 ? TOMA + COLA : TOMA}
        layout="none"
      >
        <OffthreadVideo
          src={staticFile(P + t.clip + '.mp4')}
          muted
          style={{
            position: 'absolute',
            inset: 0,
            width: 540,
            height: 1920,
            objectFit: 'cover',
            objectPosition: `${t.x ?? 50}% 50%`,
          }}
        />
      </Sequence>
    ))}
    <div
      style={{
        position: 'absolute',
        top: 330,
        left: 0,
        width: 540,
        textAlign: 'center',
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: 600,
        fontSize: 40,
        letterSpacing: '0.02em',
        color: C.beige,
        textShadow: '0 2px 18px rgba(36,26,18,0.8), 0 1px 3px rgba(36,26,18,0.6)',
      }}
    >
      {rotulo}
    </div>
  </div>
);

export const FeedOct12PorQue: React.FC = () => {
  useFuentesListas();
  return (
    <AbsoluteFill style={{backgroundColor: C.sombra}}>
      <Mitad tomas={VIENES} left={0} rotulo="POR QUÉ VIENES" />
      <Mitad tomas={QUEDAS} left={540} rotulo="POR QUÉ TE QUEDAS" />
    </AbsoluteFill>
  );
};
