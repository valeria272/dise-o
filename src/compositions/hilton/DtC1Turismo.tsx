/**
 * DOUBLETREE · CARRUSEL VIDEO — DÍA DEL TURISMO (FEED col M, 27-09 10:00).
 *
 * Brief de la grilla (estado EN EDICIÓN, «Hicimos unos ajustes en brief»):
 *
 *   G1 · Foto del hotel —fachada o lobby—, distinta a la de la story del 27/sept.
 *        Logo del hotel en la imagen, no muy grande.
 *        Texto: Feliz Día del Turismo / Hoy celebramos las ganas de descubrir
 *   G2 · Video MUT                    · Texto: MUT
 *   G3 · Video Parque Bicentenario    · Texto: Parque Bicentenario
 *   G4 · Video Sky Costanera          · Texto: Sky Costanera (sacar videos de otros lados)
 *   G4 · Video Cerro San Cristóbal    · Texto: Cerro San Cristóbal
 *   G5 · Video Barrio El Golf         · Texto: Barrio El Golf
 *
 * El brief numera dos «G4»: son seis láminas y se entregan en el orden en que
 * vienen escritas. No se renumera nada en la grilla (§G, el brief es de contenido).
 *
 * ## La referencia (Eli, 23-09 · `REFERENCIA CARRUSEL TURISMO`)
 *
 * Dos láminas de Bronnuti. Lo que se toma y lo que no:
 *
 * | referencia | acá |
 * |---|---|
 * | TODO centrado en el eje | todo centrado — es lo que la separa del S5, que alinea a la izquierda |
 * | logo chico arriba al centro | portada: logotipo DT blanco a la geometría de `logo-post.png` (160 @1080, tope 111) |
 * | portada: bloque en el medio de la foto | portada: bloque en el medio |
 * | portada: línea en itálica serif | «del Turismo» en **Stag LightItalic** — el gesto entra, la fuente no (regla del S5) |
 * | interior: filete fino + nombre en serif, tercio de abajo | interior: filete blanco + nombre en Stag Medium, tercio de abajo |
 * | interior: párrafo de cuerpo | ⛔ **no va**: el brief sólo da el nombre del lugar, y el copy es de contenido |
 * | logo en todas las láminas | ⚠️ sólo en la portada, por defecto. Ver `conLogo` |
 *
 * ## Por qué el logotipo sólo va en la portada
 *
 * El brief lo pide para G1 y no para el resto. En DT el logo en feed **no va por
 * defecto** (regla del 08-09), y en el carrusel S5 el cliente pidió explícitamente
 * sacar la firma de las interiores «para que no tenga tanto elemento por slide».
 * La referencia lo repite en cada lámina, así que la decisión queda abierta para
 * Eli: `--props='{"conLogo":true}'` lo pone también en las interiores.
 *
 * ## Titular de portada: dos pesos, UN cuerpo
 *
 * «Feliz Día» en Stag Medium y «del Turismo» en Stag LightItalic, **al mismo
 * cuerpo** — la regla de la historia del Día del Turismo («quiero que "¡Feliz
 * día" tenga el mismo peso de "del turismo"… me refería al tamaño»). Sin «¡»: el
 * brief de esta lámina no lo trae, y Stag tampoco lo tiene.
 *
 * ## El texto NO anima (S5, ronda 5, Constanza)
 *
 * «El video detrás al tener movimiento hace que el texto con más movimiento
 * maree.» Toda la tinta está quieta desde el f0. El único gesto es el FILETE de
 * las interiores, que se dibuja desde el centro (la misma idea que el globo de
 * «Tu día»: un trazo, no un texto).
 */
import React from 'react';
import {
  AbsoluteFill,
  Easing,
  getInputProps,
  Img,
  interpolate,
  OffthreadVideo,
  staticFile,
  useCurrentFrame,
} from 'remotion';
import {DT, cargarFuentesDT} from '../../brand/doubletree';

cargarFuentesDT();

export const DURACION = 150;                          // 5,0 s a 30 fps

type Props = {soloFondo?: boolean; conLogo?: boolean};
const props = (): Props => getInputProps() as Props;

/** La sombra de DT — una sola para todas las tintas blancas de la pieza. */
const SOMBRA = '0 2px 7px rgba(9,25,78,0.60), 0 0 2px rgba(9,25,78,0.45)';

const rampa = (paradas: readonly (readonly [number, number])[]) =>
  `linear-gradient(to bottom, ${paradas
    .map(([p, a]) => `rgba(9,25,78,${a}) ${p}%`)
    .join(', ')})`;

/**
 * Velo de las interiores: nace en 0 (regla de Eli del 10-09) a media altura y
 * sube cóncavo hacia el pie, donde vive el nombre del lugar.
 */
const VELO_INTERIOR: readonly (readonly [number, number])[] = [
  [0, 0], [45, 0], [55, 0.08], [63, 0.2], [70, 0.33], [77, 0.44],
  [84, 0.52], [91, 0.57], [100, 0.6],
];

/** Velo de la franja del logotipo: pesa en el 8–18 % y se va a 0 en el 30 %. */
const VELO_LOGO: readonly (readonly [number, number])[] = [
  [0, 0.62], [8, 0.6], [14, 0.54], [19, 0.36], [24, 0.16], [30, 0],
];

/** El logotipo, a la geometría medida de `logo-post.png`. */
const Logo: React.FC = () => (
  <Img
    src={staticFile('assets/hilton/dt/logo-dt-blanco.png')}
    style={{
      position: 'absolute',
      left: 540 - DT.geometria.logoAncho / 2,
      top: DT.geometria.logoYFeed,
      width: DT.geometria.logoAncho,
      height: DT.geometria.logoAncho / DT.geometria.logoProporcion,
      filter: 'drop-shadow(0 2px 8px rgba(9,25,78,0.45))',
    }}
  />
);

// ─────────────────────────────── PORTADA ───────────────────────────────

/** Cuerpo común de las dos líneas del titular. */
const CUERPO_TITULAR = 116;

/**
 * Ken Burns de la portada — la ÚNICA lámina que es foto. Se anima con
 * `left/top/width/height` y NO con `transform: scale()`: Chrome rasteriza al
 * tamaño del layout y después estira (memoria `transform-scale-revienta-la-nitidez`).
 */
const FotoPortada: React.FC = () => {
  const frame = useCurrentFrame();
  const z = interpolate(frame, [0, DURACION - 1], [1.0, 1.06], {
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.33, 0, 0.67, 1),
  });
  const w = 1080 * z;
  const h = 1350 * z;
  return (
    <Img
      src={staticFile('assets/hilton/dt/turismo/portada-hdt42.jpg')}
      style={{
        position: 'absolute',
        width: w,
        height: h,
        left: (1080 - w) / 2,
        top: (1350 - h) * 0.55,
      }}
    />
  );
};

export const DtC1TurismoPortada: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: DT.colores.azul, overflow: 'hidden'}}>
    <FotoPortada />
    {/*
      El velo: un tinte parejo que asienta la fachada clara, más una elipse en
      el centro, que es donde la referencia pone el bloque. La elipse se desvanece
      sola hacia los bordes, así que no tiene canto — no hay «máscara pegada».
    */}
    <AbsoluteFill style={{background: 'rgba(9,25,78,0.16)'}} />
    <AbsoluteFill
      style={{
        background:
          'radial-gradient(ellipse 78% 30% at 50% 52%, rgba(9,25,78,0.62) 0%, rgba(9,25,78,0.40) 50%, rgba(9,25,78,0) 100%)',
      }}
    />
    {/*
      ⭐ El velo del LOGOTIPO. La fachada remata en una cornisa blanca justo donde
      `logo-post.png` pone el logo (tope 111), y con 0,34 las dos líneas chicas
      del lockup —«by Hilton» y «SANTIAGO–VITACURA»— daban 3,5 y 2,9:1. Medido
      con `dt-c1-turismo-qa.py`, no a ojo.
    */}
    <AbsoluteFill style={{background: rampa(VELO_LOGO)}} />
    {props().soloFondo ? null : (
      <>
        <Logo />
        <div
          style={{
            position: 'absolute',
            left: 0,
            width: 1080,
            top: 520,
            textAlign: 'center',
            color: DT.colores.blanco,
            textShadow: SOMBRA,
          }}
        >
          <div
            style={{
              fontFamily: DT.fuentes.titular,
              fontSize: CUERPO_TITULAR,
              lineHeight: 1.02,
              letterSpacing: '0.005em',
            }}
          >
            <div style={{fontWeight: DT.pesos.medium}}>Feliz Día</div>
            <div style={{fontWeight: DT.pesos.light, fontStyle: 'italic'}}>
              del Turismo
            </div>
          </div>
          <div
            style={{
              marginTop: 34,
              fontFamily: DT.fuentes.titular,
              fontWeight: DT.pesos.light,
              fontSize: 40,
              lineHeight: 1.2,
              letterSpacing: '0.02em',
            }}
          >
            Hoy celebramos las ganas de descubrir
          </div>
        </div>
      </>
    )}
  </AbsoluteFill>
);

// ────────────────────────────── INTERIORES ─────────────────────────────

/** Ancho del filete — el mismo en las cinco, para que el carrusel rime. */
const FILETE = 520;
const CUERPO_LUGAR = 80;

const Filete: React.FC<{desde: number}> = ({desde}) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [desde, desde + 30], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.3, 0.05, 0.2, 1),
  });
  return (
    <div
      style={{
        margin: '0 auto',
        width: FILETE * t,
        height: 2,
        background: DT.colores.blanco,
        boxShadow: '0 1px 5px rgba(9,25,78,0.45)',
      }}
    />
  );
};

const Interior: React.FC<{clip: string; lugar: string}> = ({clip, lugar}) => {
  const {soloFondo, conLogo} = props();
  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul, overflow: 'hidden'}}>
      <OffthreadVideo
        src={staticFile(`assets/hilton/dt/turismo/clips/${clip}.mp4`)}
        style={{width: '100%', height: '100%', objectFit: 'cover'}}
        muted
      />
      <AbsoluteFill style={{background: rampa(VELO_INTERIOR)}} />
      {conLogo ? (
        <AbsoluteFill style={{background: rampa(VELO_LOGO)}} />
      ) : null}
      {soloFondo ? null : (
        <>
          {conLogo ? <Logo /> : null}
          <div
            style={{
              position: 'absolute',
              left: 0,
              width: 1080,
              top: 1080,
              textAlign: 'center',
            }}
          >
            <Filete desde={6} />
            <div
              style={{
                marginTop: 30,
                fontFamily: DT.fuentes.titular,
                fontWeight: DT.pesos.medium,
                fontSize: CUERPO_LUGAR,
                lineHeight: 1.05,
                letterSpacing: '0.005em',
                color: DT.colores.blanco,
                textShadow: SOMBRA,
              }}
            >
              {lugar}
            </div>
          </div>
        </>
      )}
    </AbsoluteFill>
  );
};

export const DtC1TurismoMut: React.FC = () => <Interior clip="mut" lugar="MUT" />;
export const DtC1TurismoBicentenario: React.FC = () => (
  <Interior clip="bicentenario" lugar="Parque Bicentenario" />
);
export const DtC1TurismoSky: React.FC = () => (
  <Interior clip="sky" lugar="Sky Costanera" />
);
export const DtC1TurismoSanCristobal: React.FC = () => (
  <Interior clip="sancristobal" lugar="Cerro San Cristóbal" />
);
export const DtC1TurismoGolf: React.FC = () => (
  <Interior clip="golf" lugar="Barrio El Golf" />
);
