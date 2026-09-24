/**
 * DOUBLETREE · STORIES col C · 01-10-2026 11:00 · ANIMADA – PROGRAMA FAMILY TIME
 * (PRIMAVERA). Estado de la grilla: OK PARA DISEÑO.
 *
 * ── RONDA 2 (Eli, 24-09) ──────────────────────────────────────────────────
 * «Se trata de ver alguna familia» · «lo único que no me gusta es la transición
 * de oscuro a color» · «guíate bien de las referencias dejadas». Los textos, la
 * dinámica, los íconos y el bloque del programa quedaron aprobados tal cual.
 *
 * Lo que la ronda 1 NO había tomado de la referencia (pin `1119989001100496240`,
 * medida cuadro a cuadro a 4 fps), y ahora sí:
 *   · el cristal es VERTICAL y alto (≈ 30–82 % del ancho, desde el 28 % del
 *     alto), no una franja apaisada;
 *   · el esmerilado es CLARO y cálido: se ve la foto a través, muy difuminada;
 *   · el texto va arriba DENTRO del cristal, a un cuerpo moderado;
 *   · la foto se ve SOLA un momento antes de que entre el cristal;
 *   · entre escenas hay BARRIDOS con desenfoque de movimiento que encadenan
 *     varias tomas cortas.
 * Lo que NO se toma, por pedido de Eli: el paso de blanco y negro a color. Todo
 * va en color desde el primer cuadro.
 *
 * ── La familia ────────────────────────────────────────────────────────────
 * §D: foto propia con el rostro cambiado y variado. Es la MISMA habitación y la
 * misma escena de la foto de `C1 FT N1` (septiembre), regenerada en Seedream 5
 * Pro con cuatro rostros nuevos (`raw/hilton/dt/oct-familia/familia-v1/v2`).
 *
 * ── Textos ───────────────────────────────────────────────────────────────
 * Literales del brief (§G), sin puntos en títulos (§F); precio como el carrusel
 * vigente («IVA INCLUIDO»); legal literal del brief, con su punto.
 *
 * ⛔ El CTA «deslizar hacia arriba» es el sticker de enlace del CM: no se dibuja.
 */
import React from 'react';
import {AbsoluteFill, Easing, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';

import {DT, cargarFuentesDT, volteaApertura} from '../../brand/doubletree';
import {ConTrade} from './dtIconosOct';

cargarFuentesDT();

const G = DT.geometria;
const MESA = {ancho: 1080, alto: 1920} as const;
export const FPS = 30;
/** 15 s, el tope que dio Eli (ronda 3): el programa queda ~6,7 s en pantalla. */
export const DURACION = 450;

const TEXTO1 = ['Días más largos,', 'clima perfecto'] as const;
const TEXTO2 = ['¡El momento exacto', 'para una escapada', 'en familia!'] as const;
const PRECIO = '$125.000';
const IVA = 'IVA INCLUIDO';
const INCLUIDOS = [
  {icono: 'assets/hilton/dt/icono-cama-eli.png', prop: 147 / 120, l: ['Habitación', 'doble']},
  {icono: 'assets/hilton/dt/oct/icono-familia-eli.png', prop: 124 / 114, l: ['2 adultos + 2 niños', 'hasta 12 años']},
  {icono: 'assets/hilton/dt/oct/icono-buffet-eli.png', prop: 130 / 120, l: ['Desayuno', 'buffet']},
] as const;
const CORREO = 'reservas.dtv@hilton.com';
const LEGAL = 'Válido jueves a domingo y festivos. Cupos limitados.';

/**
 * Las escenas, en orden. `desde` es el fotograma en que la escena ya está
 * entera; el barrido que la trae ocupa los `BARRIDO` fotogramas anteriores.
 */
const ESCENAS = [
  {src: 'assets/hilton/dt/oct/ft-familia.jpg', desde: 0, zoom: [1.0, 1.06]},
  {src: 'assets/hilton/dt/oct/ft-familia-2.jpg', desde: 158, zoom: [1.06, 1.0]},
  {src: 'assets/hilton/dt/oct/ft-hab.jpg', desde: 190, zoom: [1.0, 1.05]},
  {src: 'assets/hilton/dt/oct/ft-desayuno.jpg', desde: 222, zoom: [1.06, 1.0]},
] as const;
const BARRIDO = 12;

const T = {
  cristal1: 30,
  escribeDesde: 48,
  escribeHasta: 108,
  sale1: 138,
  cristal2: 232,
  entra2: 246,
} as const;

/** Los dos cristales, verticales como el de la referencia. */
const C1 = {x: 190, y: 560, ancho: 700, alto: 900} as const;
const C2 = {x: 140, y: 452, ancho: 800, alto: 1100} as const;
const RADIO = 34;

const SOMBRA = '0 2px 7px rgba(9,25,78,0.55), 0 0 2px rgba(9,25,78,0.4)';
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const suave = Easing.bezier(0.33, 0, 0.2, 1);

const useEntrada = (desde: number, dur = 16, sube = 18) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [desde, desde + dur], [0, 1], {...clamp, easing: suave});
  return {opacity: p, transform: `translateY(${(1 - p) * sube}px)`};
};

const ConApertura: React.FC<{t: string}> = ({t}) => (
  <>
    {volteaApertura(t).map((s, i) =>
      s.flip ? (
        <span key={i} style={{display: 'inline-block', transform: 'rotate(180deg)'}}>
          {s.t}
        </span>
      ) : (
        <span key={i}>{s.t}</span>
      ),
    )}
  </>
);

/**
 * Una escena con su barrido de entrada: llega desde la derecha con desenfoque
 * que se apaga, ENCIMA de la anterior (que no se baja: disolvencia sin asomo).
 */
const Escena: React.FC<{i: number}> = ({i}) => {
  const f = useCurrentFrame();
  const e = ESCENAS[i];
  const sig = ESCENAS[i + 1];
  if (sig && f > sig.desde + 2) return null;
  const p = i === 0 ? 1 : interpolate(f, [e.desde - BARRIDO, e.desde], [0, 1], {...clamp, easing: suave});
  if (p <= 0) return null;
  const hasta = sig ? sig.desde : DURACION;
  const z = interpolate(f, [e.desde - BARRIDO, hasta], [...e.zoom], clamp);
  // al irse, la escena también se corre y se barre hacia la izquierda
  const s = sig ? interpolate(f, [sig.desde - BARRIDO, sig.desde], [0, 1], {...clamp, easing: suave}) : 0;
  const x = (1 - p) * 420 - s * 260;
  const blur = (1 - p) * 26 + s * 18;
  return (
    <AbsoluteFill style={{opacity: Math.min(1, p * 1.6)}}>
      <Img
        src={staticFile(e.src)}
        style={{
          position: 'absolute',
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          transform: `translateX(${x}px) scale(${z})`,
          filter: blur > 0.3 ? `blur(${blur}px)` : undefined,
        }}
      />
    </AbsoluteFill>
  );
};

const Cristal: React.FC<{c: typeof C1 | typeof C2; p: number}> = ({c, p}) => (
  <div
    style={{
      position: 'absolute',
      left: c.x,
      top: c.y + (1 - p) * 30,
      width: c.ancho,
      height: c.alto,
      borderRadius: RADIO,
      // esmerilado claro y cálido de la ref + un velo azul fino para la tinta blanca
      background: 'linear-gradient(to bottom, rgba(250,246,240,0.08), rgba(250,246,240,0.04)), rgba(9,25,78,0.40)',
      backdropFilter: 'blur(26px) saturate(1.05)',
      WebkitBackdropFilter: 'blur(26px) saturate(1.05)',
      border: '1.5px solid rgba(250,250,250,0.7)',
      boxSizing: 'border-box',
      opacity: p,
    }}
  />
);

export const DtStFamilyTimeOct: React.FC<{guia?: boolean}> = ({guia = false}) => {
  const f = useCurrentFrame();

  const p1 = interpolate(f, [T.cristal1, T.cristal1 + 18], [0, 1], {...clamp, easing: suave});
  const sale1 = interpolate(f, [T.sale1, T.sale1 + 14], [1, 0], clamp);
  const p2 = interpolate(f, [T.cristal2, T.cristal2 + 18], [0, 1], {...clamp, easing: suave});

  const total = TEXTO1.join('').length;
  const n = Math.floor(interpolate(f, [T.escribeDesde, T.escribeHasta], [0, total], clamp));
  let resto = n;
  const lineas1 = TEXTO1.map((l) => {
    const k = Math.max(0, Math.min(l.length, resto));
    resto -= l.length;
    return {visible: l.slice(0, k), oculto: l.slice(k)};
  });

  const e = {
    t: useEntrada(T.entra2),
    marca: useEntrada(T.entra2 + 14),
    precio: useEntrada(T.entra2 + 22),
    iconos: useEntrada(T.entra2 + 30),
    correo: useEntrada(T.entra2 + 38),
    legal: useEntrada(T.entra2 + 42),
  };

  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul, overflow: 'hidden'}}>
      {ESCENAS.map((_, i) => (
        <Escena key={i} i={i} />
      ))}

      {/* ── ESCENA 1 · cristal alto + la frase que se escribe ── */}
      {f < T.sale1 + 14 ? (
        <AbsoluteFill style={{opacity: sale1}}>
          <Cristal c={C1} p={p1} />
          <div style={{position: 'absolute', left: C1.x, top: C1.y + 96, width: C1.ancho, textAlign: 'center', opacity: p1}}>
            {lineas1.map((l, i) => (
              <div
                key={i}
                style={{
                  fontFamily: DT.fuentes.titular,
                  fontWeight: i === 0 ? DT.pesos.medium : DT.pesos.light,
                  fontSize: 66,
                  lineHeight: 1.18,
                  color: DT.colores.blanco,
                  textShadow: SOMBRA,
                  whiteSpace: 'nowrap',
                }}
              >
                {l.visible}
                <span style={{opacity: 0}}>{l.oculto}</span>
              </div>
            ))}
          </div>
        </AbsoluteFill>
      ) : null}

      {/* ── ESCENA FINAL · el programa, en el cristal ── */}
      {f >= T.cristal2 ? (
        <>
          <Cristal c={C2} p={p2} />
          <div style={{position: 'absolute', left: C2.x, top: C2.y + 64, width: C2.ancho, textAlign: 'center'}}>
            <div style={{...e.t}}>
              {TEXTO2.map((t, i) => (
                <div
                  key={t}
                  style={{
                    fontFamily: DT.fuentes.titular,
                    fontWeight: i === 0 ? DT.pesos.medium : DT.pesos.light,
                    fontSize: 58,
                    lineHeight: 1.16,
                    color: DT.colores.blanco,
                    textShadow: SOMBRA,
                    whiteSpace: 'nowrap',
                  }}
                >
                  {i === 0 ? <ConApertura t={t} /> : t}
                </div>
              ))}
            </div>

            <div style={{...e.marca, width: 120, height: 1.5, margin: '40px auto 30px', background: 'rgba(250,250,250,0.8)'}} />

            <div
              style={{
                ...e.marca,
                fontFamily: DT.fuentes.titular,
                fontStyle: 'italic',
                fontSize: 104,
                lineHeight: 1,
                color: DT.colores.blanco,
                textShadow: SOMBRA,
                whiteSpace: 'nowrap',
              }}
            >
              <span style={{fontWeight: DT.pesos.semibold}}>Family</span>
              <span style={{fontWeight: DT.pesos.light}}> Time</span>
            </div>

            <div style={{...e.precio, marginTop: 30}}>
              <div
                style={{
                  display: 'inline-block',
                  background: DT.colores.blanco,
                  color: DT.colores.azul,
                  borderRadius: 60,
                  padding: '10px 44px 6px',
                  fontFamily: "'Trade Gothic Cn', 'Trade Gothic', sans-serif",
                  fontWeight: 700,
                  fontSize: 82,
                  lineHeight: 1,
                  letterSpacing: '0.01em',
                }}
              >
                {PRECIO}
              </div>
              <div
                style={{
                  marginTop: 14,
                  fontFamily: DT.fuentes.texto,
                  fontSize: 26,
                  letterSpacing: '0.16em',
                  textIndent: '0.16em',
                  color: DT.colores.blanco,
                  textShadow: SOMBRA,
                }}
              >
                {IVA}
              </div>
            </div>

            <div style={{...e.iconos, margin: '40px auto 0', width: C2.ancho - 50, display: 'flex', justifyContent: 'space-between'}}>
              {INCLUIDOS.map((c, i) => (
                <React.Fragment key={c.icono}>
                  {i > 0 ? <div style={{width: 1.5, alignSelf: 'stretch', background: 'rgba(250,250,250,0.55)'}} /> : null}
                  <div style={{flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
                    <Img src={staticFile(c.icono)} style={{height: 70, width: 70 * c.prop}} />
                    <div
                      style={{
                        marginTop: 14,
                        fontFamily: DT.fuentes.titular,
                        fontWeight: DT.pesos.regular,
                        fontSize: 26,
                        lineHeight: 1.2,
                        wordSpacing: '0.08em',
                        color: DT.colores.blanco,
                        textShadow: SOMBRA,
                        whiteSpace: 'nowrap',
                      }}
                    >
                      {c.l.map((x) => (
                        <div key={x}>
                          <ConTrade t={x} />
                        </div>
                      ))}
                    </div>
                  </div>
                </React.Fragment>
              ))}
            </div>

            <div style={{...e.correo, marginTop: 46}}>
              <div
                style={{
                  display: 'inline-block',
                  border: `2px solid ${DT.colores.blanco}`,
                  borderRadius: 60,
                  padding: '13px 40px 10px',
                  fontFamily: DT.fuentes.texto,
                  fontSize: 38,
                  lineHeight: 1,
                  letterSpacing: '0.02em',
                  color: DT.colores.blanco,
                  textShadow: SOMBRA,
                }}
              >
                {CORREO}
              </div>
            </div>
            <div
              style={{
                ...e.legal,
                marginTop: 22,
                fontFamily: DT.fuentes.texto,
                fontSize: 23,
                letterSpacing: '0.01em',
                color: DT.colores.blanco,
                textShadow: SOMBRA,
              }}
            >
              {LEGAL}
            </div>
          </div>
        </>
      ) : null}

      {/* Logotipo DT, plantilla `logo-ST.png`: 167 de ancho, tope 241, centrado. */}
      <Img
        src={staticFile('assets/hilton/dt/logo-dt-blanco.png')}
        style={{
          position: 'absolute',
          top: G.logoYStory,
          left: (MESA.ancho - G.logoAnchoStory) / 2,
          width: G.logoAnchoStory,
          height: G.logoAnchoStory / G.logoProporcion,
        }}
      />

      {guia ? (
        <>
          <div style={{position: 'absolute', top: 0, left: 0, width: MESA.ancho, height: DT.seguras.story.arriba, background: 'rgba(255,0,110,0.3)'}} />
          <div style={{position: 'absolute', bottom: 0, left: 0, width: MESA.ancho, height: DT.seguras.story.abajo, background: 'rgba(255,0,110,0.3)'}} />
        </>
      ) : null}
    </AbsoluteFill>
  );
};

export const DtStFamilyTimeOctGuia: React.FC = () => <DtStFamilyTimeOct guia />;
