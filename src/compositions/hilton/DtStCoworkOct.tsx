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

/**
 * RONDA 3 (Eli, 28-09): «achicar un poco ese recuadro… si es el mismo texto no es necesario que dure
 * tanto, que sea una transición más rápida para el texto, así queda más tiempo mostrándose lo del fondo».
 * Dos cristales AJUSTADOS a su texto, en vez de uno alto todo el rato: el titular entra, se lee ~3 s y
 * sale; la foto queda sola ~3,5 s; y el cristal final trae la bajada y la ubicación (~6,5 s de lectura).
 */
const T = {c1: 26, c1Sale: 118, c2: 250, ubica: 268} as const;
const C1 = {x: 160, y: 690, ancho: 760, alto: 340} as const;
const C2 = {x: 150, y: 670, ancho: 780, alto: 400} as const;

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

const Cristal: React.FC<{c: {x: number; y: number; ancho: number; alto: number}; p: number; children: React.ReactNode}> = ({
  c,
  p,
  children,
}) => (
  <>
    <div
      style={{
        position: 'absolute',
        left: c.x,
        top: c.y + (1 - p) * 24,
        width: c.ancho,
        height: c.alto,
        borderRadius: 34,
        background: 'linear-gradient(to bottom, rgba(250,246,240,0.08), rgba(250,246,240,0.04)), rgba(9,25,78,0.42)',
        backdropFilter: 'blur(26px) saturate(1.05)',
        WebkitBackdropFilter: 'blur(26px) saturate(1.05)',
        border: '1.5px solid rgba(250,250,250,0.7)',
        boxSizing: 'border-box',
        opacity: p,
      }}
    />
    <div
      style={{
        position: 'absolute',
        left: c.x,
        top: c.y + (1 - p) * 24,
        width: c.ancho,
        height: c.alto,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        textAlign: 'center',
        color: DT.colores.blanco,
        opacity: p,
      }}
    >
      {children}
    </div>
  </>
);

export const DtStCoworkOct: React.FC<{guia?: boolean}> = ({guia = false}) => {
  const f = useCurrentFrame();
  const p1 = Math.min(
    interpolate(f, [T.c1, T.c1 + 14], [0, 1], {...clamp, easing: suave}),
    interpolate(f, [T.c1Sale, T.c1Sale + 12], [1, 0], {...clamp, easing: suave}),
  );
  const p2 = interpolate(f, [T.c2, T.c2 + 14], [0, 1], {...clamp, easing: suave});
  const ubica = useEntrada(T.ubica);

  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul, overflow: 'hidden'}}>
      {ESCENAS.map((_, i) => (
        <Escena key={i} i={i} />
      ))}

      {p1 > 0 ? (
        <Cristal c={C1} p={p1}>
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
        </Cristal>
      ) : null}

      {p2 > 0 ? (
        <Cristal c={C2} p={p2}>
          <div
            style={{
              width: 640,
              fontFamily: DT.fuentes.titular,
              fontWeight: DT.pesos.regular,
              fontSize: 38,
              lineHeight: 1.32,
              wordSpacing: '0.08em',
              textShadow: SOMBRA,
            }}
          >
            Un espacio ambientado especialmente para concentrarte, reunirte o trabajar a tu ritmo
          </div>
          <div style={{...ubica, marginTop: 44}}>
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
        </Cristal>
      ) : null}

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
