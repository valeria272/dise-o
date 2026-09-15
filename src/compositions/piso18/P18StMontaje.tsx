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
 *     COMENTARIOS DISEÑO: «Podría ser un texto orientado a ''Dejando todo listo,
 *     para que solo te preocupes de celebrar''»
 *
 * ⭐ El comentario del cliente **ya está aplicado en el propio brief**: esa frase
 * es literalmente la bajada. No hay nada que reescribir.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⚠️ NO ES UN TIMELAPSE, Y ESO LO DECIDIÓ LA REFERENCIA
 * ══════════════════════════════════════════════════════════════════════════
 * No existe metraje de timelapse de Piso18. Y la referencia que dejó Eli
 * —`ref st 3.mp4`, 20 s— **tampoco es un timelapse**: es un montaje animado de
 * FOTOS FIJAS de un centro de eventos sobre fondo crema, con marcos que crecen,
 * titular serif a la izquierda y un cierre de marca con el logotipo y el CTA.
 *
 * Eli confirmó el 15-09: **montaje animado como la referencia**, contando la
 * progresión con las fotos que hay.
 *
 * ⚠️ Y una segunda decisión suya del mismo día: **no hay ninguna foto del salón
 * vacío**. La progresión arranca por los planos más desnudos que sí existen —el
 * espacio con la barra sola— y avanza hasta el salón completo ambientado. Cuenta
 * el «paso a paso» sin inventar un fotograma que nadie tomó.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LOS CINCO TIEMPOS — de vacío a lleno, con material real
 * ══════════════════════════════════════════════════════════════════════════
 *   1. `p18-44`  el espacio con el logotipo iluminado, sin montar
 *   2. `p18-43`  la barra sola, todavía sin público
 *   3. `p18-73`  las mesas ya vestidas, salón a media luz
 *   4. `p18-77`  el detalle de la mesa terminada: centro floral, copas, vajilla
 *   5. `p18-86`  el salón completo ambientado
 *   6. cierre de marca — logotipo + CTA, como hace la referencia
 *
 * ⚠️ Geometría de pieza ANIMADA: la posición y el contraste del botón se miden
 * en el **ÚLTIMO fotograma**, no en el primero. Acá el cierre es fondo oscuro y
 * el botón va en esquema A (fucsia lleno), que es el que sostiene ahí.
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

/** Cada plano dura 2,6 s y el cierre 4 s. Total 17 s — cabe holgado en una historia. */
const PLANO = 78;
const CIERRE = 120;

const PLANOS = [
  {src: 'assets/hilton/piso18/p18-44.jpg', pos: 'center 50%'},
  {src: 'assets/hilton/piso18/p18-43.jpg', pos: 'center 55%'},
  {src: 'assets/hilton/piso18/p18-73.jpg', pos: 'center 52%'},
  {src: 'assets/hilton/piso18/p18-77.jpg', pos: 'center 58%'},
  {src: 'assets/hilton/piso18/p18-86.jpg', pos: 'center 50%'},
] as const;

export const P18_MONTAJE_DUR = PLANO * PLANOS.length + CIERRE;

/**
 * Un plano. Entra con un acercamiento lento (Ken Burns muy contenido) y cruza
 * con el siguiente por opacidad. El acercamiento es del 6 %: más que eso y en
 * 2,6 s se nota el arrastre.
 */
const Plano: React.FC<{src: string; pos: string; indice: number}> = ({src, pos, indice}) => {
  const frame = useCurrentFrame();
  const escala = interpolate(frame, [0, PLANO + 18], [1, 1.06], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.quad),
  });
  // Cruce: los 12 primeros frames entran, salvo el primer plano de todos.
  const opacidad = indice === 0 ? 1 : interpolate(frame, [0, 12], [0, 1], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{opacity: opacidad}}>
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
      {/* Velo para que el titular se sostenga sobre cualquiera de los cinco planos */}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(0,0,0,0.52) 0%, rgba(0,0,0,0.12) 30%, rgba(0,0,0,0.10) 58%, rgba(0,0,0,0.62) 100%)',
        }}
      />
    </AbsoluteFill>
  );
};

/** El logotipo, arriba y centrado, a la geometría medida. Persiste en toda la pieza. */
const Logo: React.FC = () => (
  <Img
    src={staticFile('assets/hilton/piso18/logo.png')}
    style={{
      position: 'absolute',
      width: P18.geometria.logoAncho,
      height: P18.geometria.logoAncho / P18.geometria.logoProporcion,
      left: (1080 - P18.geometria.logoAncho) / 2,
      top: P18.geometria.logoYStory,
    }}
  />
);

/** El cierre de marca: fondo oscuro, logotipo grande, bajada y botón. */
const Cierre: React.FC = () => {
  const frame = useCurrentFrame();
  const entra = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  const sube = interpolate(entra, [0, 1], [26, 0]);
  return (
    <AbsoluteFill style={{opacity: entra}}>
      <AbsoluteFill style={{overflow: 'hidden'}}>
        <Img
          src={staticFile('assets/hilton/piso18/p18-86.jpg')}
          style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center 50%'}}
        />
      </AbsoluteFill>
      <AbsoluteFill style={{backgroundColor: 'rgba(8,8,10,0.72)'}} />
      <div style={{transform: `translateY(${sube}px)`}}>
        <Img
          src={staticFile('assets/hilton/piso18/logo.png')}
          style={{
            position: 'absolute',
            width: 486,
            height: 486 / P18.geometria.logoProporcion,
            left: (1080 - 486) / 2,
            top: 742,
          }}
        />
        <div
          style={{
            position: 'absolute',
            left: 118,
            right: 118,
            top: 1010,
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
            top: 1190,
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
  const frame = useCurrentFrame();
  const finPlanos = PLANO * PLANOS.length;
  // El titular acompaña los cinco planos y se va antes del cierre.
  const salida = interpolate(frame, [finPlanos - 16, finPlanos], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{backgroundColor: '#0B0B0D'}}>
      {PLANOS.map((p, i) => (
        <Sequence key={p.src} from={i * PLANO} durationInFrames={PLANO + 16}>
          <Plano src={p.src} pos={p.pos} indice={i} />
        </Sequence>
      ))}

      <Sequence from={0} durationInFrames={finPlanos}>
        <AbsoluteFill style={{opacity: salida}}>
          <Logo />
          {/*
            El titular, verbatim del brief. Va abajo —no sobre la foto— para que
            los cinco planos se lean: es el espacio que el velo inferior deja
            preparado. Y por encima de la zona segura de 340 px.
          */}
          <div
            style={{
              position: 'absolute',
              left: 96,
              right: 96,
              top: 1318,
              textAlign: 'center',
              color: P18.colores.blanco,
              fontFamily: P18.fuentes.titular,
              fontWeight: 300,
              fontSize: 62,
              lineHeight: 1.16,
              textShadow: '0 4px 26px rgba(0,0,0,0.55)',
            }}
          >
            Así se monta un evento en Piso18,{' '}
            <span style={{fontStyle: 'italic', fontWeight: 400}}>paso a paso.</span>
          </div>
        </AbsoluteFill>
      </Sequence>

      <Sequence from={finPlanos} durationInFrames={CIERRE}>
        <Cierre />
      </Sequence>
    </AbsoluteFill>
  );
};
