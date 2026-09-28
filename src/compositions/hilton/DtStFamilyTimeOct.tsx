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
import {AbsoluteFill, Easing, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from 'remotion';

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
type EscenaDef = {src: string; desde: number; zoom: readonly [number, number]};
type Tiempos = {cristal1: number; escribeDesde: number; escribeHasta: number; sale1: number; cristal2: number; entra2: number};
/** Cuánto se corre y se desenfoca la toma que llega (x1, b1) y la que se va (x2, b2). */
type Barrido = {x1: number; x2: number; b1: number; b2: number};
type Montaje = {escenas: readonly EscenaDef[]; t: Tiempos; barrido?: Barrido; grande?: boolean};
const BARRIDO_R3: Barrido = {x1: 420, x2: 260, b1: 26, b2: 18};

/** Ronda 3 (24-09, entregada): fotos fijas con zoom. */
const FOTOS: Montaje = {
  escenas: [
    {src: 'assets/hilton/dt/oct/ft-familia.jpg', desde: 0, zoom: [1.0, 1.06]},
    {src: 'assets/hilton/dt/oct/ft-familia-2.jpg', desde: 158, zoom: [1.06, 1.0]},
    {src: 'assets/hilton/dt/oct/ft-hab.jpg', desde: 190, zoom: [1.0, 1.05]},
    {src: 'assets/hilton/dt/oct/ft-desayuno.jpg', desde: 222, zoom: [1.06, 1.0]},
  ],
  t: {cristal1: 30, escribeDesde: 48, escribeHasta: 108, sale1: 138, cristal2: 232, entra2: 246},
};

/**
 * Ronda 4 (Eli, 28-09): «utiliza los nuevos personajes… vuélvelas video para que se
 * vea más realista, más bonito, más sutil». Las 5 escenas son clips de Kling 2.5 Pro
 * sacados de las story del banco aprobado el 25-09 (familia sobre fotos REALES de DT,
 * `scripts/dt-oct-ft-clips.py`). La cámara ya se mueve en el clip: sin zoom encima.
 * Orden: la tarde larga (vista) lleva «Días más largos, clima perfecto»; después
 * llegada, juego y desayuno en tomas cortas; la habitación tranquila sostiene el
 * programa ~5,9 s (clip de 10 s, a velocidad real).
 */
const CLIPS: Montaje = {
  escenas: [
    {src: 'assets/hilton/dt/oct/ft-v-vista.mp4', desde: 0, zoom: [1, 1]},
    {src: 'assets/hilton/dt/oct/ft-v-lobby.mp4', desde: 146, zoom: [1, 1]},
    {src: 'assets/hilton/dt/oct/ft-v-almohadas.mp4', desde: 176, zoom: [1, 1]},
    {src: 'assets/hilton/dt/oct/ft-v-restaurante.mp4', desde: 206, zoom: [1, 1]},
    {src: 'assets/hilton/dt/oct/ft-v-hab.mp4', desde: 236, zoom: [1, 1]},
  ],
  // la familia de la habitación queda justo DETRÁS del cristal: se la deja ver sola
  // ~1 s (f236→258) antes de que entre, como la foto sola de la referencia.
  // la frase se apaga ENTERA antes de que arranque el barrido del lobby (f134):
  // en la primera pasada quedaba un fantasma del texto sobre la familia caminando
  t: {cristal1: 30, escribeDesde: 44, escribeHasta: 100, sale1: 118, cristal2: 258, entra2: 272},
};
/**
 * Ronda 5 (Eli, 28-09) sobre la de video: «dura muy extraño… si hay texto importante
 * que se mantenga más el tiempo… no lo hagas todo video, usa las mismas imágenes, que
 * pasen como transición, y la primera toma sí sea un video… que no se vea todo tan
 * exagerado… mejor en jerarquía».
 *   · SOLO la primera toma es video (la vista, la tarde larga de «Días más largos»),
 *     y la frase queda ~2,6 s entera en pantalla, no ~0,6.
 *   · lobby, almohadas y desayuno son FOTOS del banco que pasan en ~0,7 s cada una:
 *     son el puente, no escenas que haya que leer.
 *   · el barrido es la mitad de corto y de borroso (nada de «exagerado»).
 *   · el programa cierra sobre la foto de la habitación y queda ~7,6 s: es el texto
 *     importante. La familia se ve sola ~0,5 s antes de que entre el cristal.
 *   · jerarquía del bloque (`grande`): Family Time manda, el precio segundo, el
 *     titular baja a antetítulo y los incluidos y el contacto van en grupos aparte.
 */
const R5: Montaje = {
  escenas: [
    {src: 'assets/hilton/dt/oct/ft-v-vista.mp4', desde: 0, zoom: [1, 1]},
    {src: 'assets/hilton/dt/oct/ft-f-lobby.jpg', desde: 146, zoom: [1.0, 1.02]},
    {src: 'assets/hilton/dt/oct/ft-f-almohadas.jpg', desde: 166, zoom: [1.0, 1.02]},
    {src: 'assets/hilton/dt/oct/ft-f-restaurante.jpg', desde: 186, zoom: [1.0, 1.02]},
    {src: 'assets/hilton/dt/oct/ft-f-hab.jpg', desde: 206, zoom: [1.0, 1.035]},
  ],
  t: {cristal1: 18, escribeDesde: 30, escribeHasta: 72, sale1: 120, cristal2: 220, entra2: 230},
  barrido: {x1: 180, x2: 110, b1: 10, b2: 7},
  grande: true,
};
const BARRIDO = 12;

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
const Escena: React.FC<{i: number; escenas: readonly EscenaDef[]; b: Barrido}> = ({i, escenas, b}) => {
  const f = useCurrentFrame();
  const e = escenas[i];
  const sig = escenas[i + 1];
  if (sig && f > sig.desde + 2) return null;
  const p = i === 0 ? 1 : interpolate(f, [e.desde - BARRIDO, e.desde], [0, 1], {...clamp, easing: suave});
  if (p <= 0) return null;
  const hasta = sig ? sig.desde : DURACION;
  const z = interpolate(f, [e.desde - BARRIDO, hasta], [...e.zoom], clamp);
  // al irse, la escena también se corre y se barre hacia la izquierda
  const s = sig ? interpolate(f, [sig.desde - BARRIDO, sig.desde], [0, 1], {...clamp, easing: suave}) : 0;
  const x = (1 - p) * b.x1 - s * b.x2;
  const blur = (1 - p) * b.b1 + s * b.b2;
  const estilo: React.CSSProperties = {
    position: 'absolute',
    width: '100%',
    height: '100%',
    transform: z === 1 ? `translateX(${x}px)` : `translateX(${x}px) scale(${z})`,
    filter: blur > 0.3 ? `blur(${blur}px)` : undefined,
  };
  return (
    <AbsoluteFill style={{opacity: Math.min(1, p * 1.6)}}>
      {e.src.endsWith('.mp4') ? (
        // el clip arranca cuando empieza su barrido, no en el fotograma 0
        <Sequence from={Math.max(0, e.desde - BARRIDO)} layout="none">
          <OffthreadVideo muted src={staticFile(e.src)} style={{...estilo, objectFit: 'cover'}} />
        </Sequence>
      ) : (
        <Img src={staticFile(e.src)} style={{...estilo, objectFit: 'cover'}} />
      )}
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

/**
 * `soloGrafica`: la capa de texto, cristal y logo sobre transparente, para la pista V2
 * de la secuencia de Premiere (`scripts/dt-oct-ft-premiere.py`). Sin foto debajo el
 * esmerilado no tiene qué difuminar: en Premiere el cristal es el velo y el filete.
 */
export const DtStFamilyTimeOct: React.FC<{guia?: boolean; montaje?: Montaje; soloGrafica?: boolean}> = ({
  guia = false,
  montaje = FOTOS,
  soloGrafica = false,
}) => {
  const f = useCurrentFrame();
  const T = montaje.t;
  // jerarquía del bloque final: la de la ronda 3 o la de la ronda 5 (`grande`)
  const J = montaje.grande
    ? {tit: 48, filete: '30px auto 24px', marca: 126, precioArriba: 24, precio: 90, grupo: 62, correo: 36}
    : {tit: 58, filete: '40px auto 30px', marca: 104, precioArriba: 30, precio: 82, grupo: 40, correo: 38};

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
    <AbsoluteFill style={{backgroundColor: soloGrafica ? 'transparent' : DT.colores.azul, overflow: 'hidden'}}>
      {soloGrafica
        ? null
        : montaje.escenas.map((_, i) => <Escena key={i} i={i} escenas={montaje.escenas} b={montaje.barrido ?? BARRIDO_R3} />)}

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
                    fontSize: J.tit,
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

            <div style={{...e.marca, width: 120, height: 1.5, margin: J.filete, background: 'rgba(250,250,250,0.8)'}} />

            <div
              style={{
                ...e.marca,
                fontFamily: DT.fuentes.titular,
                fontStyle: 'italic',
                fontSize: J.marca,
                lineHeight: 1,
                color: DT.colores.blanco,
                textShadow: SOMBRA,
                whiteSpace: 'nowrap',
              }}
            >
              <span style={{fontWeight: DT.pesos.semibold}}>Family</span>
              <span style={{fontWeight: DT.pesos.light}}> Time</span>
            </div>

            <div style={{...e.precio, marginTop: J.precioArriba}}>
              <div
                style={{
                  display: 'inline-block',
                  background: DT.colores.blanco,
                  color: DT.colores.azul,
                  borderRadius: 60,
                  padding: '10px 44px 6px',
                  fontFamily: "'Trade Gothic Cn', 'Trade Gothic', sans-serif",
                  fontWeight: 700,
                  fontSize: J.precio,
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

            <div style={{...e.iconos, margin: `${J.grupo}px auto 0`, width: C2.ancho - 50, display: 'flex', justifyContent: 'space-between'}}>
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

            <div style={{...e.correo, marginTop: J.grupo}}>
              <div
                style={{
                  display: 'inline-block',
                  border: `2px solid ${DT.colores.blanco}`,
                  borderRadius: 60,
                  padding: '13px 40px 10px',
                  fontFamily: DT.fuentes.texto,
                  fontSize: J.correo,
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

/** Ronda 4 (28-09): la familia fija en video. Reemplaza a la de fotos en Drive. */
export const DtStFamilyTimeOctVideo: React.FC = () => <DtStFamilyTimeOct montaje={CLIPS} />;
export const DtStFamilyTimeOctVideoGrafica: React.FC = () => <DtStFamilyTimeOct montaje={CLIPS} soloGrafica />;

/** Ronda 5 (28-09): video sólo en la primera toma, fotos de transición, jerarquía nueva. */
export const DtStFamilyTimeOctR5: React.FC = () => <DtStFamilyTimeOct montaje={R5} />;
export const DtStFamilyTimeOctR5Guia: React.FC = () => <DtStFamilyTimeOct montaje={R5} guia />;
export const DtStFamilyTimeOctR5Grafica: React.FC = () => <DtStFamilyTimeOct montaje={R5} soloGrafica />;
export const DtStFamilyTimeOctVideoGuia: React.FC = () => <DtStFamilyTimeOct montaje={CLIPS} guia />;
