/**
 * DOUBLETREE · STORIES 22-10-2026 11:00 · ANIMADA – COWORKING EN DOUBLETREE.
 * Estado de la grilla (28-09): OK PARA DISEÑO. Comentario para diseño: «Cambia de
 * aire y eleva tu productividad durante tu estadía» (el titular, ya en el brief).
 *
 * ⚠️ La grilla NO trae referencia para esta pieza (la celda LINK está vacía). Se usa
 * el aparato animado ya aprobado de DT, la ST Family Time del 01-10
 * (`DtStFamilyTimeOct`): foto sola un momento, cristal ALTO esmerilado que entra,
 * texto arriba dentro del cristal y BARRIDOS con desenfoque entre tomas (R-15/X-24),
 * todo en color desde el primer cuadro, máx. 15 s (R-25).
 *
 * Tomas — RONDA 2 (Eli, 28-09: «la tira se está viendo un poco [repetida]… utiliza imágenes
 * nuevas»): las tres salen de la sesión nueva SEP 2026, el cowork del lobby:
 *   1. `sep_26-270` — el portátil y el café servido sobre la mesa, de cerca.
 *   2. `sep_26-267` — la butaca con el portátil abierto y el café.
 *   3. `sep_26-264` — el lounge del cowork completo.
 * (La ronda 1 usaba el clip del café de «Tu día» y HDT_37/38, ya vistos en el feed.)
 *
 * Textos literales; sin punto en título ni bajadas (R-60).
 * ⛔ El CTA «consulta disponibilidad» es sticker del CM: no se dibuja.
 */
import React from 'react';
import {AbsoluteFill, Easing, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';
import {Logo, SOMBRA} from './dtOct2';

cargarFuentesDT();

export const DURACION = 450;
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const suave = Easing.bezier(0.33, 0, 0.2, 1);
const BARRIDO = 12;

const ESCENAS = [
  {src: 'assets/hilton/dt/oct2/cw-1.jpg', desde: 0, zoom: [1.0, 1.06]},
  {src: 'assets/hilton/dt/oct2/cw-2.jpg', desde: 176, zoom: [1.06, 1.0]},
  {src: 'assets/hilton/dt/oct2/cw-3.jpg', desde: 316, zoom: [1.0, 1.05]},
] as const;

const T = {cristal: 30, titulo: 44, sub: 196, ubica: 226} as const;
const C = {x: 140, y: 452, ancho: 800, alto: 830} as const;

const useEntrada = (desde: number, dur = 16, sube = 18) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [desde, desde + dur], [0, 1], {...clamp, easing: suave});
  return {opacity: p, transform: `translateY(${(1 - p) * sube}px)`};
};

const Escena: React.FC<{i: number}> = ({i}) => {
  const f = useCurrentFrame();
  const e = ESCENAS[i];
  const sig = ESCENAS[i + 1];
  if (sig && f > sig.desde + 2) return null;
  const p = i === 0 ? 1 : interpolate(f, [e.desde - BARRIDO, e.desde], [0, 1], {...clamp, easing: suave});
  if (p <= 0) return null;
  const hasta = sig ? sig.desde : DURACION;
  const z = interpolate(f, [e.desde - BARRIDO, hasta], [...e.zoom], clamp);
  const s = sig ? interpolate(f, [sig.desde - BARRIDO, sig.desde], [0, 1], {...clamp, easing: suave}) : 0;
  const x = (1 - p) * 420 - s * 260;
  const blur = (1 - p) * 26 + s * 18;
  const estilo: React.CSSProperties = {
    position: 'absolute',
    width: '100%',
    height: '100%',
    objectFit: 'cover',
    transform: `translateX(${x}px) scale(${z})`,
    filter: blur > 0.3 ? `blur(${blur}px)` : undefined,
  };
  return (
    <AbsoluteFill style={{opacity: Math.min(1, p * 1.6)}}>
      <Img src={staticFile(e.src)} style={estilo} />
    </AbsoluteFill>
  );
};

export const DtStCoworkOct: React.FC<{guia?: boolean}> = ({guia = false}) => {
  const f = useCurrentFrame();
  const pc = interpolate(f, [T.cristal, T.cristal + 18], [0, 1], {...clamp, easing: suave});
  const e = {t: useEntrada(T.titulo), sub: useEntrada(T.sub), ubica: useEntrada(T.ubica)};

  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul, overflow: 'hidden'}}>
      {ESCENAS.map((_, i) => (
        <Escena key={i} i={i} />
      ))}

      <div
        style={{
          position: 'absolute',
          left: C.x,
          top: C.y + (1 - pc) * 30,
          width: C.ancho,
          height: C.alto,
          borderRadius: 34,
          background: 'linear-gradient(to bottom, rgba(250,246,240,0.08), rgba(250,246,240,0.04)), rgba(9,25,78,0.42)',
          backdropFilter: 'blur(26px) saturate(1.05)',
          WebkitBackdropFilter: 'blur(26px) saturate(1.05)',
          border: '1.5px solid rgba(250,250,250,0.7)',
          boxSizing: 'border-box',
          opacity: pc,
        }}
      />

      <div style={{position: 'absolute', left: C.x, top: C.y + 90, width: C.ancho, textAlign: 'center', color: DT.colores.blanco}}>
        <div style={e.t}>
          {[
            {t: 'Cambia de aire y eleva', w: DT.pesos.medium},
            {t: 'tu productividad', w: DT.pesos.light},
            {t: 'durante tu estadía', w: DT.pesos.light},
          ].map((l) => (
            <div
              key={l.t}
              style={{fontFamily: DT.fuentes.titular, fontWeight: l.w, fontSize: 64, lineHeight: 1.16, textShadow: SOMBRA, whiteSpace: 'nowrap'}}
            >
              {l.t}
            </div>
          ))}
        </div>

        <div style={{...e.sub}}>
          <div style={{width: 120, height: 1.5, margin: '48px auto 40px', background: 'rgba(250,250,250,0.8)'}} />
          <div
            style={{
              width: 620,
              margin: '0 auto',
              fontFamily: DT.fuentes.titular,
              fontWeight: DT.pesos.regular,
              fontSize: 36,
              lineHeight: 1.32,
              wordSpacing: '0.08em',
              textShadow: SOMBRA,
            }}
          >
            Un espacio ambientado especialmente para concentrarte, reunirte o trabajar a tu ritmo
          </div>
        </div>

        <div style={{...e.ubica, marginTop: 64}}>
          <div style={{fontFamily: DT.fuentes.texto, fontSize: 22, letterSpacing: '0.18em', textIndent: '0.18em', textShadow: SOMBRA}}>
            UBICACIÓN
          </div>
          <div
            style={{
              display: 'inline-block',
              marginTop: 16,
              border: `2px solid ${DT.colores.blanco}`,
              borderRadius: 60,
              padding: '14px 34px 11px',
              fontFamily: DT.fuentes.texto,
              fontSize: 27,
              lineHeight: 1.2,
              letterSpacing: '0.02em',
              textShadow: SOMBRA,
            }}
          >
            Te esperamos en el 1er y 2do nivel de la cafetería
          </div>
        </div>
      </div>

      <Logo formato="story" />

      {guia ? (
        <>
          <div style={{position: 'absolute', top: 0, left: 0, width: 1080, height: DT.seguras.story.arriba, background: 'rgba(255,0,110,0.3)'}} />
          <div style={{position: 'absolute', bottom: 0, left: 0, width: 1080, height: DT.seguras.story.abajo, background: 'rgba(255,0,110,0.3)'}} />
        </>
      ) : null}
    </AbsoluteFill>
  );
};

export const DtStCoworkOctGuia: React.FC = () => <DtStCoworkOct guia />;
