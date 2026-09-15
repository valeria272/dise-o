/**
 * PISO18 — HISTORIA ANIMADA · «TIMELAPSE MONTAJE» (STORIES col M · 23-09 · 18:00)
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL
 * ══════════════════════════════════════════════════════════════════════════
 * Hoja STORIES, columna M, estado **OK PARA DISEÑAR**:
 *
 *     ST ANIMADA - TIMELAPSE MONTAJE
 *     Visual: Timelapse del montaje de un evento en Piso18, desde el salón vacío
 *     hasta completamente ambientado.
 *     Texto principal: Así se monta un evento en Piso18, paso a paso.
 *     Bajada: Dejando todo listo, para que solo te preocupes de celebrar.
 *     CTA: Cotiza el tuyo en piso18.cl
 *     INTERACCIÓN: Sticker de link a cotización.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐⭐ RONDA 2 — «NO SE PARECE A LA REFERENCIA, ÚSALA A MODO DE PLANTILLA»
 * ══════════════════════════════════════════════════════════════════════════
 * La ronda 1 eran cinco fotos a sangre con un acercamiento lento y el titular
 * encima. Eli la rechazó: *«no se parece a la referencia, úsala a modo de
 * plantilla, analiza las transiciones de foto, etc.»*
 *
 * Se midió `ref st 3.mp4` fotograma a fotograma (2 fps, 41 cuadros) y **la
 * referencia tiene una estructura en dos mitades que la ronda 1 no tenía**:
 *
 * | Tiempo | Qué pasa |
 * |---|---|
 * | 0,0–2,5 s | Fondo crema. **Un marco vertical estrecho** a la derecha con foto. A la izquierda, logotipo y titular serif **en versales, alineado a la izquierda**, en líneas cortas |
 * | 2,5–4,5 s | **El marco CRECE** hacia la izquierda y muestra más foto. Sigue el crema |
 * | 4,5–7,0 s | Entra un **segundo marco**; el texto cambia a una frase más corta |
 * | 7,5–10 s | El marco se expande hasta **foto a sangre**. Ya no hay texto |
 * | 10–16 s | Fotos a sangre que se **empujan** lateralmente |
 * | 16–20 s | **Cierre**: velo oscuro, logotipo centrado, frase y CTA |
 *
 * ⭐ **La consecuencia de fondo, y es la que arregla el otro problema:** en la
 * primera mitad **el texto NO va sobre la foto, va al lado**, sobre el crema. Eso
 * es lo que pidió Eli en la misma ronda —*«los textos de esa st animada debes
 * cuidar que no choquen con rostros o logos»*— y acá se resuelve por estructura,
 * no por buscarle un hueco a cada fotograma. En `p18-44` hay un **logotipo PISO18
 * iluminado en la pared**: con el texto fuera del marco, no lo toca nunca.
 *
 * ⚠️ **Duración: 14 s.** Eli fijó el tope en la misma ronda: *«las historias no
 * deben ser de más de 15 segundos»*. La ronda 1 duraba 17.
 *
 * ⚠️ **Zonas seguras de Instagram**, que Eli pidió respetar explícitamente: nada
 * de texto sobre los 250 px de arriba ni los 340 de abajo. Acá el titular vive
 * entre y=560 y y=1180, y el bloque del cierre entre y=980 y y=1430.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LOS CINCO TIEMPOS — de vacío a lleno, con material real
 * ══════════════════════════════════════════════════════════════════════════
 * ⚠️ **No hay ninguna foto del salón vacío** (medido sobre la sesión entera), así
 * que la progresión arranca por lo más desnudo que existe. Decisión de Eli.
 *
 *   1. `p18-44`  el espacio con el logotipo iluminado, sin montar
 *   2. `p18-43`  la barra sola, todavía sin público
 *   3. `p18-73`  las mesas ya vestidas
 *   4. `p18-77`  el detalle de la mesa terminada: centro floral, copas, vajilla
 *   5. `p18-86`  el salón completo ambientado — y el fondo del cierre
 */
import React from 'react';
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  Sequence,
  staticFile,
  useCurrentFrame,
} from 'remotion';
import {P18, cargarFuentesP18} from '../../brand/piso18';

export const P18_MONTAJE_FPS = 30;

const W = 1080;
const H = 1920;

/** ⚠️ 420 frames = **14 s**. El tope que fijó Eli es 15. */
export const P18_MONTAJE_DUR = 420;

/** Los cortes de los cinco actos, en frames. */
const T = {
  acto1: 0,     // marco estrecho + titular
  acto2: 110,   // el marco crece + entra el segundo
  acto3: 180,   // primera foto a sangre
  acto4: 250,   // segunda foto a sangre
  cierre: 320,
} as const;

/** Zona segura de historia, en píxeles de la mesa 1080×1920. */
const SEGURA_ARRIBA = P18.seguras.story.arriba; // 250
const SEGURA_ABAJO = H - P18.seguras.story.abajo; // 1580

const suave = Easing.bezier(0.22, 0.61, 0.36, 1);

/**
 * El logotipo. Centrado arriba, a la geometría medida — **el sistema de marca
 * manda sobre la referencia en identidad**: en `ref st 3.mp4` el logo va arriba a
 * la izquierda, pero las dos piezas aprobadas de Piso18 lo ponen centrado y ahí
 * se queda. Lo que se toma de la referencia es la estructura, no el logotipo.
 */
const Logo: React.FC<{tinta?: boolean; ancho?: number; top?: number}> = ({
  tinta = false,
  ancho = P18.geometria.logoAncho,
  top = P18.geometria.logoYStory,
}) => (
  <Img
    src={staticFile('assets/hilton/piso18/logo.png')}
    style={{
      position: 'absolute',
      width: ancho,
      height: ancho / P18.geometria.logoProporcion,
      left: (W - ancho) / 2,
      top,
      // El PNG es blanco; sobre el crema se invierte a tinta.
      filter: tinta ? 'invert(1) brightness(0.12)' : undefined,
    }}
  />
);

/**
 * Un marco: ventana rectangular con una foto dentro, que puede crecer. Es EL
 * recurso de la referencia — la foto vive contenida, no a sangre, y el aire
 * alrededor es lo que deja sitio al texto.
 */
const Marco: React.FC<{
  src: string;
  x: number;
  y: number;
  ancho: number;
  alto: number;
  pos?: string;
  opacidad?: number;
}> = ({src, x, y, ancho, alto, pos = 'center', opacidad = 1}) => (
  <div
    style={{
      position: 'absolute',
      left: x,
      top: y,
      width: ancho,
      height: alto,
      overflow: 'hidden',
      opacity: opacidad,
      boxShadow: '0 2px 18px rgba(20,17,15,0.13)',
    }}
  >
    <Img
      src={staticFile(src)}
      style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: pos}}
    />
  </div>
);

/** El titular de la primera mitad: IvyPresto en VERSALES, alineado a la izquierda. */
const Titular: React.FC<{lineas: string[]; opacidad: number; top: number}> = ({
  lineas,
  opacidad,
  top,
}) => (
  <div
    style={{
      position: 'absolute',
      left: 92,
      top,
      width: 430,
      opacity: opacidad,
      fontFamily: P18.fuentes.titular,
      fontWeight: 300,
      fontSize: 52,
      lineHeight: 1.26,
      letterSpacing: 2.6,
      textTransform: 'uppercase',
      color: P18.colores.tinta,
    }}
  >
    {lineas.map((l) => (
      <div key={l}>{l}</div>
    ))}
  </div>
);

/** ── ACTO 1 · marco estrecho a la derecha, titular a la izquierda ───────── */
const Acto1: React.FC = () => {
  const f = useCurrentFrame();
  const dur = T.acto2 - T.acto1;
  // El marco entra creciendo desde abajo, muy contenido.
  const entra = interpolate(f, [0, 26], [0, 1], {extrapolateRight: 'clamp', easing: suave});
  const alto = interpolate(entra, [0, 1], [640, 820]);
  const y = interpolate(entra, [0, 1], [560, 470]);
  const texto = interpolate(f, [10, 34, dur - 16, dur], [0, 1, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <AbsoluteFill>
      <Marco
        src="assets/hilton/piso18/p18-44-alto.jpg"
        x={596}
        y={y}
        ancho={392}
        alto={alto}
        pos="center 50%"
        opacidad={entra}
      />
      <Titular lineas={['Así se monta', 'un evento', 'en Piso18']} opacidad={texto} top={620} />
    </AbsoluteFill>
  );
};

/** ── ACTO 2 · el marco crece hacia la izquierda y entra el segundo ──────── */
const Acto2: React.FC = () => {
  const f = useCurrentFrame();
  const dur = T.acto3 - T.acto2;
  const p = interpolate(f, [0, 34], [0, 1], {extrapolateRight: 'clamp', easing: suave});
  // El primero se ensancha hacia la izquierda (x baja, ancho sube).
  const x1 = interpolate(p, [0, 1], [596, 372]);
  const w1 = interpolate(p, [0, 1], [392, 616]);
  const y1 = interpolate(p, [0, 1], [470, 392]);
  const h1 = interpolate(p, [0, 1], [820, 900]);
  // El segundo entra desde el borde izquierdo, más chico y escalonado.
  const p2 = interpolate(f, [18, 48], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: suave});
  const texto = interpolate(f, [24, 46, dur - 14, dur], [0, 1, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <AbsoluteFill>
      <Marco
        src="assets/hilton/piso18/p18-44-alto.jpg"
        x={x1}
        y={y1}
        ancho={w1}
        alto={h1}
        pos="center 50%"
      />
      <Marco
        src="assets/hilton/piso18/p18-43-alto.jpg"
        x={92}
        y={interpolate(p2, [0, 1], [1010, 962])}
        ancho={330}
        alto={430}
        pos="center 55%"
        opacidad={p2}
      />
      <div
        style={{
          position: 'absolute',
          left: 92,
          top: 1436,
          opacity: texto,
          fontFamily: P18.fuentes.titular,
          fontWeight: 400,
          fontStyle: 'italic',
          fontSize: 54,
          letterSpacing: 1.4,
          color: P18.colores.tinta,
        }}
      >
        paso a paso.
      </div>
    </AbsoluteFill>
  );
};

/**
 * Una foto a sangre de la segunda mitad. Entra **empujando** desde abajo, que es
 * la transición de la referencia — no un desvanecido.
 */
const Sangre: React.FC<{src: string; pos: string; dur: number}> = ({src, pos, dur}) => {
  const f = useCurrentFrame();
  const entra = interpolate(f, [0, 22], [0, 1], {extrapolateRight: 'clamp', easing: suave});
  const y = interpolate(entra, [0, 1], [H * 0.16, 0]);
  const escala = interpolate(f, [0, dur], [1.04, 1.0], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{transform: `translateY(${y}px)`}}>
      <AbsoluteFill style={{overflow: 'hidden'}}>
        <Img
          src={staticFile(src)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            objectPosition: pos,
            transform: `scale(${escala})`,
          }}
        />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/** ── CIERRE · velo, logotipo, bajada y botón ────────────────────────────── */
const Cierre: React.FC = () => {
  const f = useCurrentFrame();
  // Cruza con la foto anterior en vez de aparecer de golpe.
  const cruce = interpolate(f, [0, 18], [0, 1], {extrapolateRight: 'clamp', easing: suave});
  const velo = interpolate(f, [6, 34], [0, 0.74], {extrapolateRight: 'clamp', easing: suave});
  const entra = interpolate(f, [14, 40], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: suave,
  });
  const sube = interpolate(entra, [0, 1], [24, 0]);
  return (
    <AbsoluteFill style={{opacity: cruce}}>
      <AbsoluteFill style={{overflow: 'hidden'}}>
        <Img
          src={staticFile('assets/hilton/piso18/p18-86.jpg')}
          style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center 50%'}}
        />
      </AbsoluteFill>
      <AbsoluteFill style={{backgroundColor: `rgba(10,9,8,${velo})`}} />
      <div style={{opacity: entra, transform: `translateY(${sube}px)`}}>
        {/* Logotipo grande y centrado — el gesto del cierre de la referencia. */}
        <Logo ancho={472} top={812} />
        <div
          style={{
            position: 'absolute',
            left: 122,
            right: 122,
            top: 1064,
            textAlign: 'center',
            fontFamily: P18.fuentes.texto,
            fontWeight: 500,
            fontSize: 33,
            lineHeight: 1.5,
            color: P18.colores.blanco,
          }}
        >
          Dejando todo listo, para que solo te preocupes de celebrar.
        </div>
        <div
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            top: 1244,
            display: 'flex',
            justifyContent: 'center',
          }}
        >
          <div
            style={{
              backgroundColor: P18.botones.lleno.fondo,
              color: P18.botones.lleno.texto,
              fontFamily: P18.fuentes.texto,
              fontWeight: 700,
              fontSize: 33,
              letterSpacing: 0.6,
              padding: '26px 58px',
              borderRadius: 999,
            }}
          >
            Cotiza el tuyo en piso18.cl
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const P18StMontaje: React.FC = () => {
  cargarFuentesP18();
  const f = useCurrentFrame();
  // El logotipo de cabecera acompaña sólo la primera mitad; en el cierre hay otro.
  const logoArriba = interpolate(f, [0, 14, T.cierre - 20, T.cierre], [0, 1, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  // Sobre el crema el logotipo va en tinta; sobre las fotos a sangre, en blanco.
  const sobreFoto = f >= T.acto3;

  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tarjeta}}>
      <Sequence from={T.acto1} durationInFrames={T.acto2 - T.acto1}>
        <Acto1 />
      </Sequence>
      <Sequence from={T.acto2} durationInFrames={T.acto3 - T.acto2}>
        <Acto2 />
      </Sequence>
      <Sequence from={T.acto3} durationInFrames={T.acto4 - T.acto3 + 2}>
        <Sangre src="assets/hilton/piso18/p18-73.jpg" pos="center 52%" dur={T.acto4 - T.acto3} />
      </Sequence>
      <Sequence from={T.acto4} durationInFrames={T.cierre - T.acto4 + 20}>
        <Sangre src="assets/hilton/piso18/p18-77.jpg" pos="center 58%" dur={T.cierre - T.acto4} />
      </Sequence>
      <Sequence from={T.cierre} durationInFrames={P18_MONTAJE_DUR - T.cierre}>
        <Cierre />
      </Sequence>

      {/*
        El logotipo de cabecera va POR ENCIMA de todo y cambia de tinta según lo
        que tenga debajo. En las fotos a sangre lleva un velo corto arriba para
        sostenerse — mismo recurso que la plantilla de la marca.
      */}
      <AbsoluteFill style={{opacity: logoArriba, pointerEvents: 'none'}}>
        {sobreFoto ? (
          <div
            style={{
              position: 'absolute',
              inset: 0,
              background:
                'linear-gradient(to bottom, rgba(0,0,0,0.42) 0%, rgba(0,0,0,0.10) 22%, rgba(0,0,0,0) 36%)',
            }}
          />
        ) : null}
        <Logo tinta={!sobreFoto} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/**
 * Guía de QA: las dos zonas seguras de Instagram sobre la pieza animada.
 * ⚠️ En una pieza animada el botón se mide en el **ÚLTIMO fotograma**, no en el
 * primero — por eso esta guía se mira ahí, con `--frame`.
 */
export const P18StMontajeGuia: React.FC = () => (
  <AbsoluteFill>
    <P18StMontaje />
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 0,
          height: SEGURA_ARRIBA,
          background: 'rgba(255,0,0,0.22)',
          borderBottom: '2px solid red',
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: SEGURA_ABAJO,
          bottom: 0,
          background: 'rgba(255,0,0,0.22)',
          borderTop: '2px solid red',
        }}
      />
    </AbsoluteFill>
  </AbsoluteFill>
);
