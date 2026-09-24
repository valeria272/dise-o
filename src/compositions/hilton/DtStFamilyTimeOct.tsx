/**
 * DOUBLETREE · STORIES col C · 01-10-2026 11:00 · ANIMADA – PROGRAMA FAMILY TIME
 * (PRIMAVERA). Estado de la grilla: OK PARA DISEÑO.
 *
 * ── Dirección de arte ─────────────────────────────────────────────────────
 * La referencia es el pin `1119989001100496240` (video 9:16 de 19 s): foto de un
 * interior → aparece un CRISTAL ESMERILADO de esquinas redondeadas → el texto se
 * ESCRIBE letra a letra dentro → corte a escenas que pasan de BLANCO Y NEGRO A
 * COLOR.
 *
 * Se toman los tres gestos y se ordenan para el brief:
 *   · el paso del gris al color ES la primavera («colores primaverales»): la
 *     foto nace apagada y se enciende mientras se escribe «Días más largos…»;
 *   · el cristal NO se corta entre escenas: es el mismo objeto que crece y
 *     cambia de contenido. Con dos escenas en 12 s, cortar el cristal se leería
 *     como dos historias pegadas;
 *   · la tipografía y el color siguen siendo DT (Stag + Trade, azul #09194E),
 *     no los de la referencia — el mismo criterio del Día del Turismo.
 *
 * El bloque del programa calca el carrusel VIGENTE de Family Time (`C1 FT N2`,
 * §C del manual: «la fuente de verdad es el último carrusel que dejó Eli»):
 * «Family» Stag itálica gruesa + «Time» Stag itálica liviana, cifra en píldora
 * blanca, «IVA INCLUIDO» en versales, los TRES íconos de Eli (extraídos de esa
 * pieza, no redibujados) y el correo en píldora de filete.
 *
 * ── Textos ───────────────────────────────────────────────────────────────
 * Literales del brief (§G), con dos ajustes que NO son de redacción:
 *   · sin puntos en títulos (§F, regla del cliente del 23-09): «clima
 *     perfecto...» va sin los puntos suspensivos. ⚠️ Avisado a Eli.
 *   · el precio va como en el carrusel vigente («IVA INCLUIDO»); el brief lo
 *     abrevia «IVA Inc.». ⚠️ Avisado a Eli.
 *   · el legal va literal del brief, con su punto (es legal, no título).
 *
 * ⛔ Sin personas: la §D pide foto propia CON EL ROSTRO CAMBIADO y variado, y la
 * familia de septiembre ya se usó. Se resuelve con los espacios que el programa
 * incluye —la habitación doble y el desayuno—, que además son dos de los tres
 * íconos.
 *
 * ⛔ El CTA «deslizar hacia arriba» NO se dibuja: es el sticker de enlace que
 * pone el CM. Queda libre la zona segura de abajo (340 px).
 */
import React from 'react';
import {AbsoluteFill, Easing, Img, interpolate, spring, staticFile, useCurrentFrame} from 'remotion';

import {DT, cargarFuentesDT, volteaApertura} from '../../brand/doubletree';

cargarFuentesDT();

const G = DT.geometria;
const MESA = {ancho: 1080, alto: 1920} as const;
export const FPS = 30;
/** 12 s: 5 s de escena 1, 7 s de escena 2 (la que lleva la información). */
export const DURACION = 360;

const TEXTO1 = ['Días más largos,', 'clima perfecto'] as const;
const TEXTO2 = ['¡El momento exacto', 'para una escapada en familia!'] as const;
const PRECIO = '$125.000';
const IVA = 'IVA INCLUIDO';
const INCLUIDOS = [
  {icono: 'assets/hilton/dt/icono-cama-eli.png', prop: 147 / 120, l: ['Habitación', 'doble']},
  {icono: 'assets/hilton/dt/oct/icono-familia-eli.png', prop: 124 / 114, l: ['2 adultos + 2 niños', 'hasta 12 años']},
  {icono: 'assets/hilton/dt/oct/icono-buffet-eli.png', prop: 130 / 120, l: ['Desayuno', 'buffet']},
] as const;
const CORREO = 'reservas.dtv@hilton.com';
const LEGAL = 'Válido jueves a domingo y festivos. Cupos limitados.';

/** Tiempos (fotogramas). */
const T = {
  cristalEntra: 10,
  escribeDesde: 34,
  escribeHasta: 104,
  colorDesde: 18,
  colorHasta: 120,
  sale1: 138,
  corte: 150,
  corteDura: 16,
  color2Desde: 158,
  color2Hasta: 225,
  crece: 150,
  entra2: 176,
} as const;

/** El cristal: ancho de la referencia adoptado en DT (880, centrado). */
const CRISTAL = {
  x: 100,
  ancho: 880,
  radio: 30,
  filete: 1.5,
  /** escena 1: sólo la frase */
  e1: {y: 760, alto: 400},
  /** escena 2: el programa completo */
  e2: {y: 468, alto: 1000},
  desenfoque: 22,
} as const;

const SOMBRA = '0 2px 7px rgba(9,25,78,0.55), 0 0 2px rgba(9,25,78,0.4)';

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const suave = Easing.bezier(0.33, 0, 0.2, 1);

/** Fundido + subida corta, el mismo gesto de entrada de las piezas animadas de DT. */
const useEntrada = (desde: number, dur = 16, sube = 18) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [desde, desde + dur], [0, 1], {...clamp, easing: suave});
  return {opacity: p, transform: `translateY(${(1 - p) * sube}px)`};
};

/** Stag no trae `¡`: el truco de Eli, el signo de cierre rotado 180°. */
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

/** Stag no trae `+`: ese signo va en Trade (`stagSirve`). */
const ConMas: React.FC<{t: string}> = ({t}) => (
  <>
    {t.split('+').map((p, i, a) => (
      <React.Fragment key={i}>
        {p}
        {i < a.length - 1 ? <span style={{fontFamily: DT.fuentes.texto}}>+</span> : null}
      </React.Fragment>
    ))}
  </>
);

const Foto: React.FC<{src: string; desde: number; hasta: number; zoom: [number, number]}> = ({
  src,
  desde,
  hasta,
  zoom,
}) => {
  const f = useCurrentFrame();
  const sat = interpolate(f, [desde, hasta], [0, 1], {...clamp, easing: suave});
  const z = interpolate(f, [0, DURACION], zoom, clamp);
  return (
    <Img
      src={staticFile(src)}
      style={{
        position: 'absolute',
        width: '100%',
        height: '100%',
        objectFit: 'cover',
        transform: `scale(${z})`,
        // gris → color; el brillo acompaña apenas para que el gris no se vea sucio
        filter: `saturate(${sat}) brightness(${0.94 + 0.06 * sat})`,
      }}
    />
  );
};

export const DtStFamilyTimeOct: React.FC<{guia?: boolean}> = ({guia = false}) => {
  const f = useCurrentFrame();

  // ── el cristal: entra, y en el corte crece hasta el tamaño del programa ──
  const entra = interpolate(f, [T.cristalEntra, T.cristalEntra + 18], [0, 1], {...clamp, easing: suave});
  const crece = spring({frame: f - T.crece, fps: FPS, config: {damping: 200, stiffness: 60}});
  const cy = interpolate(crece, [0, 1], [CRISTAL.e1.y, CRISTAL.e2.y]);
  const calto = interpolate(crece, [0, 1], [CRISTAL.e1.alto, CRISTAL.e2.alto]);
  const relleno = interpolate(crece, [0, 1], [0.22, 0.5]);

  // ── la escritura: carácter a carácter, repartida en las dos líneas ──
  const total = TEXTO1.join('').length;
  const n = Math.floor(interpolate(f, [T.escribeDesde, T.escribeHasta], [0, total], clamp));
  const sale1 = interpolate(f, [T.sale1, T.sale1 + 12], [1, 0], clamp);
  let resto = n;
  const lineas1 = TEXTO1.map((l) => {
    const k = Math.max(0, Math.min(l.length, resto));
    resto -= l.length;
    return {visible: l.slice(0, k), oculto: l.slice(k)};
  });

  // la escena 2 entra ENCIMA y la 1 no se baja (disolvencia sin asomo del fondo)
  const corte = interpolate(f, [T.corte, T.corte + T.corteDura], [0, 1], {...clamp, easing: suave});

  const e = {
    t1: useEntrada(T.entra2),
    t2: useEntrada(T.entra2 + 6),
    marca: useEntrada(T.entra2 + 16),
    precio: useEntrada(T.entra2 + 24),
    iconos: useEntrada(T.entra2 + 32),
    correo: useEntrada(T.entra2 + 40),
    legal: useEntrada(T.entra2 + 44),
  };

  const Y = CRISTAL.e2.y;

  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul, overflow: 'hidden'}}>
      <Foto src="assets/hilton/dt/oct/ft-hab.jpg" desde={T.colorDesde} hasta={T.colorHasta} zoom={[1.0, 1.07]} />
      <AbsoluteFill style={{opacity: corte}}>
        <Foto
          src="assets/hilton/dt/oct/ft-desayuno.jpg"
          desde={T.color2Desde}
          hasta={T.color2Hasta}
          zoom={[1.08, 1.0]}
        />
      </AbsoluteFill>

      {/* El cristal esmerilado: fondo difuminado adentro + tinte azul + filete. */}
      <div
        style={{
          position: 'absolute',
          left: CRISTAL.x,
          top: cy,
          width: CRISTAL.ancho,
          height: calto,
          borderRadius: CRISTAL.radio,
          background: `rgba(9,25,78,${relleno})`,
          backdropFilter: `blur(${CRISTAL.desenfoque}px)`,
          WebkitBackdropFilter: `blur(${CRISTAL.desenfoque}px)`,
          border: `${CRISTAL.filete}px solid rgba(250,250,250,0.85)`,
          boxSizing: 'border-box',
          opacity: entra,
          transform: `translateY(${(1 - entra) * 24}px)`,
        }}
      />

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

      {/* ── ESCENA 1 · la frase que se escribe ── */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          top: CRISTAL.e1.y,
          width: MESA.ancho,
          height: CRISTAL.e1.alto,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
          opacity: sale1,
        }}
      >
        {lineas1.map((l, i) => (
          <div
            key={i}
            style={{
              fontFamily: DT.fuentes.titular,
              fontWeight: i === 0 ? DT.pesos.medium : DT.pesos.light,
              fontSize: 84,
              lineHeight: 1.18,
              color: DT.colores.blanco,
              textShadow: SOMBRA,
              whiteSpace: 'nowrap',
            }}
          >
            {l.visible}
            {/* lo no escrito ocupa su lugar: la línea no baila mientras se escribe */}
            <span style={{opacity: 0}}>{l.oculto}</span>
          </div>
        ))}
      </div>

      {/* ── ESCENA 2 · el programa ── */}
      <div style={{position: 'absolute', left: 0, top: Y + 62, width: MESA.ancho, textAlign: 'center'}}>
        <div
          style={{
            ...e.t1,
            fontFamily: DT.fuentes.titular,
            fontWeight: DT.pesos.medium,
            fontSize: 62,
            lineHeight: 1.16,
            color: DT.colores.blanco,
            textShadow: SOMBRA,
            whiteSpace: 'nowrap',
          }}
        >
          <ConApertura t={TEXTO2[0]} />
        </div>
        <div
          style={{
            ...e.t2,
            fontFamily: DT.fuentes.titular,
            fontWeight: DT.pesos.light,
            fontSize: 62,
            lineHeight: 1.16,
            color: DT.colores.blanco,
            textShadow: SOMBRA,
            whiteSpace: 'nowrap',
          }}
        >
          {TEXTO2[1]}
        </div>

        {/* filete corto que separa la frase del programa */}
        <div
          style={{
            ...e.marca,
            width: 120,
            height: 1.5,
            margin: '44px auto 34px',
            background: 'rgba(250,250,250,0.8)',
          }}
        />

        {/* «Family Time» como en `C1 FT N2` */}
        <div
          style={{
            ...e.marca,
            fontFamily: DT.fuentes.titular,
            fontStyle: 'italic',
            fontSize: 112,
            lineHeight: 1,
            color: DT.colores.blanco,
            textShadow: SOMBRA,
            whiteSpace: 'nowrap',
          }}
        >
          <span style={{fontWeight: DT.pesos.semibold}}>Family</span>
          <span style={{fontWeight: DT.pesos.light}}> Time</span>
        </div>

        {/* la cifra en píldora blanca */}
        <div style={{...e.precio, marginTop: 34}}>
          <div
            style={{
              display: 'inline-block',
              background: DT.colores.blanco,
              color: DT.colores.azul,
              borderRadius: 60,
              padding: '10px 46px 6px',
              fontFamily: "'Trade Gothic Cn', 'Trade Gothic', sans-serif",
              fontWeight: 700,
              fontSize: 86,
              lineHeight: 1,
              letterSpacing: '0.01em',
            }}
          >
            {PRECIO}
          </div>
          <div
            style={{
              marginTop: 16,
              fontFamily: DT.fuentes.texto,
              fontSize: 27,
              letterSpacing: '0.16em',
              textIndent: '0.16em',
              color: DT.colores.blanco,
              textShadow: SOMBRA,
            }}
          >
            {IVA}
          </div>
        </div>

        {/* los tres incluidos: ícono de Eli arriba, rótulo abajo, reglas entre celdas */}
        <div
          style={{
            ...e.iconos,
            margin: '46px auto 0',
            width: CRISTAL.ancho - 60,
            display: 'flex',
            justifyContent: 'space-between',
          }}
        >
          {INCLUIDOS.map((c, i) => (
            <React.Fragment key={c.icono}>
              {i > 0 ? (
                <div style={{width: 1.5, alignSelf: 'stretch', background: 'rgba(250,250,250,0.55)'}} />
              ) : null}
              <div style={{flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
                <Img src={staticFile(c.icono)} style={{height: 74, width: 74 * c.prop}} />
                <div
                  style={{
                    marginTop: 16,
                    fontFamily: DT.fuentes.titular,
                    fontWeight: DT.pesos.regular,
                    fontSize: 29,
                    lineHeight: 1.2,
                    wordSpacing: '0.1em',
                    color: DT.colores.blanco,
                    textShadow: SOMBRA,
                    whiteSpace: 'nowrap',
                  }}
                >
                  {c.l.map((x) => (
                    <div key={x}>
                      <ConMas t={x} />
                    </div>
                  ))}
                </div>
              </div>
            </React.Fragment>
          ))}
        </div>

        {/* el correo, en píldora de filete */}
        <div style={{...e.correo, marginTop: 56}}>
          <div
            style={{
              display: 'inline-block',
              border: `2px solid ${DT.colores.blanco}`,
              borderRadius: 60,
              padding: '14px 44px 11px',
              fontFamily: DT.fuentes.texto,
              fontSize: 40,
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
            marginTop: 26,
            fontFamily: DT.fuentes.texto,
            fontSize: 25,
            letterSpacing: '0.01em',
            color: DT.colores.blanco,
            textShadow: SOMBRA,
          }}
        >
          {LEGAL}
        </div>
      </div>

      {guia ? (
        <>
          {[
            {y: 0, alto: DT.seguras.story.arriba, c: 'rgba(255,0,110,0.35)'},
            {y: MESA.alto - DT.seguras.story.abajo, alto: DT.seguras.story.abajo, c: 'rgba(255,0,110,0.35)'},
          ].map((b) => (
            <div key={b.y} style={{position: 'absolute', top: b.y, left: 0, width: MESA.ancho, height: b.alto, background: b.c}} />
          ))}
          <div style={{position: 'absolute', top: 0, left: MESA.ancho / 2, width: 1, height: MESA.alto, background: 'rgba(255,0,110,0.6)'}} />
        </>
      ) : null}
    </AbsoluteFill>
  );
};

export const DtStFamilyTimeOctGuia: React.FC = () => <DtStFamilyTimeOct guia />;
