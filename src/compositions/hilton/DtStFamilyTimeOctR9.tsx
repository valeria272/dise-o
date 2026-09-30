/**
 * DOUBLETREE · STORIES col C · 01-10-2026 11:00 · ANIMADA – PROGRAMA FAMILY TIME
 * (PRIMAVERA) — RONDA 8.
 *
 * ── Lo que pidió Eli (28-09, sobre la ronda 7) ─────────────────────────────
 * «mejora la foto de las personas, hay en varias que se ven que desaparecen o no se
 * ven completos… que se vea una ST muy atractiva visualmente y mejora transiciones».
 *
 * ── Cómo se resolvió (ronda 8) ──────────────────────────────────────────────
 * · «No se ven completos»: el recuadro (y≈1110–1568) tapaba a la familia del pecho
 *   para abajo, y en almohadas el borde cortaba al papá. El desayuno y la habitación
 *   se EXPANDIERON con IA hacia abajo y a los lados (`scripts/dt-oct-ft-r8-expandir.py`)
 *   con la foto original pegada encima: la familia sube y queda entera entre el
 *   titular y el recuadro. Almohadas sale; entra el desayuno (es un «incluido»).
 * · «Desaparecen»: el fundido montaba dos familias al 50 % y los cuerpos se veían
 *   transparentes. Ahora es una CORTINA con borde suave de izquierda a derecha y un
 *   empuje leve: en cada punto se ve una sola foto, nadie se vuelve fantasma.
 * · El recuadro entra cuando el desayuno ya terminó de entrar: el lobby queda limpio.
 *
 * ── (historial de la ronda 6) ──
 * ── Lo que pidió Eli (28-09, sobre la ronda 5) ─────────────────────────────
 * «El título principal no lo vas a dejar en esa caja… solamente la información
 * general de Family Time» · «solamente veo videos, no quiero ver mucha animación…
 * varias imágenes a lo largo, que queden bastante tiempo para que no se mareen» ·
 * «no lo dejes con tanto azul, abarca demasiado, tiene que ser algo sutil, una
 * bajada» · «la jerarquía no es sólo que se vea bonito, sino que sea funcional» ·
 * «solo imágenes».
 *
 * ── Cómo se resolvió ──────────────────────────────────────────────────────
 * · SOLO FOTOS: cuatro del banco de la familia aprobado el 25-09 (fondos reales de
 *   DT), ~3,5–4 s cada una, con fundido de 0,5 s y un acercamiento casi quieto
 *   (3 %). Sin barridos ni desenfoque de movimiento.
 * · Los TITULARES van sobre la foto, como toda story de DT: Stag a dos pesos, blanco
 *   con sombra, sobre el velo que nace en 0 (R-13). El texto 1 en la primera foto;
 *   el texto 2 entra en la segunda y se queda hasta el final, arriba: es el mensaje.
 * · La CAJA es sólo el programa y es una BAJADA: angosta de alto, abajo sobre la zona
 *   segura, esmerilado claro con poco azul (α 0,20 en vez de 0,40). Adentro, en tres
 *   filas funcionales: qué es y cuánto vale (Family Time · precio) → qué incluye
 *   (íconos) → cómo se reserva (correo · legal).
 *
 * Textos literales del brief (§G), sin punto en títulos (R-60); el legal con su punto.
 * ⛔ El CTA «deslizar hacia arriba» es el sticker de enlace del CM: no se dibuja.
 */
import React from 'react';
import {AbsoluteFill, Easing, Img, OffthreadVideo, interpolate, staticFile, useCurrentFrame} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';
import {ConTrade} from './dtIconosOct';
import {Logo, SOMBRA, Stag, TITULO_STORY, TRADE_CN, Velo, topTitulo} from './dtOct2';

cargarFuentesDT();

const BLANCO = DT.colores.blanco;
const AZUL = DT.colores.azul;
export const DURACION_R9 = 450;

const TEXTO1 = ['Días más largos,', 'clima perfecto'] as const;
const TEXTO2 = ['¡El momento exacto', 'para una escapada', 'en familia!'] as const;
const INCLUIDOS = [
  {icono: 'assets/hilton/dt/icono-cama-eli.png', prop: 147 / 120, l: ['Habitación', 'doble']},
  {icono: 'assets/hilton/dt/oct/icono-familia-eli.png', prop: 124 / 114, l: ['2 adultos + 2 niños', 'hasta 12 años']},
  {icono: 'assets/hilton/dt/oct/icono-buffet-eli.png', prop: 130 / 120, l: ['Desayuno', 'buffet']},
] as const;

/**
 * Las fotos: `desde` es cuando empieza a entrar (cortina de `CORTINA` fotogramas
 * ENCIMA de la anterior, que no se baja — ver `disolvencia-no-se-baja-la-que-sale`).
 * Se eligieron por tener el tercio de arriba tranquilo (techo, muro), que es donde va
 * el titular, y la gente en el medio, que es lo que la bajada no tapa.
 * Ronda 7 (Eli, 28-09): «utiliza menos imágenes… que se vean más realistas». Quedan
 * TRES (lobby → almohadas → habitación). ⛔ Fuera la cookie: con zoom, la «niña» de
 * la izquierda se lee como una mujer adulta y la foto está sobreprocesada.
 * ⛔ La vista a Santiago quedó fuera: el cuadro y la cabeza del papá caen justo bajo
 * el titular (se probó, «clima perfecto» le cruzaba la cara).
 */
const FOTOS = [
  // Ronda 9 (Eli 29-09: «desapariciones de rostro, de narices… ya tenemos nuestro personaje»):
  // las tres re-rendidas ENTERAS con Nano Banana Pro 4K y la familia aprobada el 25-09
  // (mama-D, papa-A, nina-B, nino-A) — scripts/dt-oct-ft-r9.py.
  {src: 'assets/hilton/dt/oct/ft-r9-lobby.jpg', desde: 0, y: 0, s: 1},
  {src: 'assets/hilton/dt/oct/ft-r9-desayuno.jpg', desde: 92, y: 0, s: 1},
  {src: 'assets/hilton/dt/oct/ft-r9-hab.jpg', desde: 250, y: 0, s: 1},
];

type Escena = {src: string; desde: number; y: number; s: number; video?: boolean};

/**
 * RONDA 10 (Scarlette, hilo en STORIES!C15, 29-09): «cambiemos la imagen de la familia tomando
 * desayuno por [foto del buffet] y la que salen caminando por una de la habitación [video]».
 * El lobby sale; abre el paneo real de la habitación doble (3,7 s, a 0,95 para que llegue a la
 * cortina) y el desayuno es la foto real del buffet, recortada de 3:4 a 9:16. La familia de la
 * cama se queda: Family Time tiene que mostrar una familia.
 */
const FOTOS_R10: Escena[] = [
  {src: 'assets/hilton/dt/oct/ft-r10-hab-video.mp4', desde: 0, y: 0, s: 1, video: true},
  {src: 'assets/hilton/dt/oct/ft-r10-desayuno.jpg', desde: 92, y: 0, s: 1},
  {src: 'assets/hilton/dt/oct/ft-r9-hab.jpg', desde: 250, y: 0, s: 1},
];
/** La cortina: fotogramas que tarda y ancho del borde difuminado. */
const CORTINA = 22;
const BORDE = 100;
const DESENFOQUE = 22;  // px sobre la foto de 1440: pico en el cruce de la cortina  // con 260 se montaban las dos familias en el borde

/**
 * Ronda 7: «Días más largos» dura menos (~2 s) y, cuando entra «¡El momento exacto…»,
 * entra con él el recuadro de Family Time: el programa queda ~12 s en pantalla.
 */
const T = {
  entra1: 8,
  sale1: 72,
  entra2: 112,
  bajada: 112,
} as const;

/** La bajada: ancho de columna, pegada sobre la zona segura de abajo. */
const B = {x: DT.geometria.margenLateral, ancho: 1080 - 2 * DT.geometria.margenLateral, pie: 1920 - DT.seguras.story.abajo - 12};

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const suave = Easing.bezier(0.33, 0, 0.2, 1);

const useEntrada = (desde: number, dur = 18, sube = 16) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [desde, desde + dur], [0, 1], {...clamp, easing: suave});
  return {opacity: p, transform: `translateY(${(1 - p) * sube}px)`};
};

const FotoFija: React.FC<{i: number; fotos: Escena[]}> = ({i, fotos}) => {
  const f = useCurrentFrame();
  const e = fotos[i];
  const sig = fotos[i + 1];
  if (f < e.desde || (sig && f > sig.desde + CORTINA)) return null;
  const hasta = sig ? sig.desde + CORTINA : DURACION_R9;
  const z = interpolate(f, [e.desde, hasta], [1, 1.04], clamp);
  // la que entra: cortina de izquierda a derecha + empuje de 50 px que se asienta
  const p = i === 0 ? 1 : interpolate(f, [e.desde, e.desde + CORTINA], [0, 1], {...clamp, easing: suave});
  const borde = -BORDE + p * (1080 + 2 * BORDE);
  const mascara = i === 0 || p >= 1 ? undefined : `linear-gradient(90deg, #000 ${borde - BORDE}px, transparent ${borde}px)`;
  // se asienta desde la izquierda: el hueco que deja queda del lado aún tapado por la cortina
  const empuje = -(1 - p) * 50;
  // Ronda 9 (QA 29-09): con la familia en otro lugar en cada foto, en el cruce se leía un
  // niño DE MÁS (el del lobby parado junto a la mesa, el del desayuno junto a la cama).
  // Las dos fotos se desenfocan en la cortina: nadie de la otra foto se lee nítido.
  const q = sig ? interpolate(f, [sig.desde, sig.desde + CORTINA], [0, 1], clamp) : 0;
  const desenfoque = Math.max((1 - p) * DESENFOQUE, Math.sin(Math.min(q, 1) * Math.PI / 2) * DESENFOQUE);
  return (
    <AbsoluteFill style={{WebkitMaskImage: mascara, maskImage: mascara}}>
      {e.video ? (
        <OffthreadVideo
          src={staticFile(e.src)}
          muted
          playbackRate={0.95}
          style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', filter: desenfoque > 0.3 ? `blur(${desenfoque}px)` : undefined}}
        />
      ) : (
        <Img
          src={staticFile(e.src)}
          style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', transform: `translate(${empuje}px, ${e.y}px) scale(${z * e.s})`, filter: desenfoque > 0.3 ? `blur(${desenfoque}px)` : undefined}}
        />
      )}
    </AbsoluteFill>
  );
};

const Titular: React.FC<{lineas: readonly string[]; cuerpo: number}> = ({lineas, cuerpo}) => (
  <>
    {lineas.map((t, i) => (
      <div
        key={t}
        style={{
          fontFamily: DT.fuentes.titular,
          fontWeight: i === 0 ? DT.pesos.medium : DT.pesos.light,
          fontSize: cuerpo,
          lineHeight: TITULO_STORY.interlinea,
          color: BLANCO,
          textShadow: SOMBRA,
          whiteSpace: 'nowrap',
        }}
      >
        <Stag t={t} />
      </div>
    ))}
  </>
);

/** `soloGrafica`: velos, textos, bajada y logo sobre transparente, para la V2 de Premiere. */
export const DtStFamilyTimeOctR9: React.FC<{guia?: boolean; soloGrafica?: boolean; fotos?: Escena[]}> = ({guia = false, soloGrafica = false, fotos = FOTOS}) => {
  const f = useCurrentFrame();
  const e1 = useEntrada(T.entra1);
  const sale1 = interpolate(f, [T.sale1, T.sale1 + 12], [1, 0], clamp);
  const e2 = useEntrada(T.entra2);
  const pb = interpolate(f, [T.bajada, T.bajada + 20], [0, 1], {...clamp, easing: suave});
  const eb = {
    marca: useEntrada(T.bajada + 8, 16, 10),
    iconos: useEntrada(T.bajada + 16, 16, 10),
    correo: useEntrada(T.bajada + 24, 16, 10),
  };
  const veloDesayuno = interpolate(
    f,
    [fotos[1].desde, fotos[1].desde + CORTINA, fotos[2].desde, fotos[2].desde + CORTINA],
    [0, 1, 1, 0],
    clamp,
  );
  const velo2 = interpolate(f, [T.bajada - 10, T.bajada + 20], [0, 1], clamp);

  return (
    <AbsoluteFill style={{backgroundColor: soloGrafica ? 'transparent' : AZUL, overflow: 'hidden'}}>
      {soloGrafica ? null : fotos.map((_, i) => <FotoFija key={i} i={i} fotos={fotos} />)}

      {/* velo de arriba para el titular y el logo; el de abajo aparece con la bajada */}
      <Velo desde={0.5} pie={0.5} lado="arriba" />
      <div style={{position: 'absolute', inset: 0, opacity: velo2}}>
        <Velo desde={0.5} pie={0.36} />
      </div>

      {/* el mural del restaurante es claro y cargado: más velo detrás del titular sólo ahí */}
      <div style={{position: 'absolute', inset: 0, opacity: veloDesayuno}}>
        {/* el Velo de arriba se diluye antes de y≈620: aquí va una sombra local, centrada en el titular */}
        <div
          style={{
            position: 'absolute',
            left: -100,
            width: 1280,
            top: 300,
            height: 480,
            background: 'radial-gradient(ellipse 50% 50% at 50% 50%, rgba(9,25,78,0.5) 0%, rgba(9,25,78,0.28) 50%, rgba(9,25,78,0) 100%)',
          }}
        />
      </div>

      <Logo formato="story" />

      {/* RONDA 10 (Constanza, 29-09): «ojo con la ubicación del título… deben estar en la misma separación del
          logo, y le bajaría un poco al interlineado». Los dos textos arrancaban a alturas distintas (versal en 488 y
          416, medido): ahora los dos en la norma común, interlínea 1,06. */}
      {/* ── texto 1 · sobre la primera foto ── */}
      {f < T.sale1 + 12 ? (
        <div style={{position: 'absolute', top: topTitulo(80), width: 1080, textAlign: 'center', ...e1, opacity: e1.opacity * sale1}}>
          <Titular lineas={TEXTO1} cuerpo={80} />
        </div>
      ) : null}

      {/* ── texto 2 · entra en la segunda foto y se queda: es el mensaje ── */}
      {f >= T.entra2 ? (
        <div style={{position: 'absolute', top: topTitulo(72), width: 1080, textAlign: 'center', ...e2}}>
          <Titular lineas={TEXTO2} cuerpo={72} />
        </div>
      ) : null}

      {/* ── la bajada · sólo el programa ── */}
      {f >= T.bajada ? (
        <div
          style={{
            position: 'absolute',
            left: B.x,
            width: B.ancho,
            bottom: 1920 - B.pie,
            padding: '22px 40px 20px',
            boxSizing: 'border-box',
            borderRadius: 26,
            background: 'rgba(9,25,78,0.20)',
            backdropFilter: 'blur(20px) saturate(1.05)',
            WebkitBackdropFilter: 'blur(20px) saturate(1.05)',
            border: '1.5px solid rgba(250,250,250,0.6)',
            opacity: pb,
            transform: `translateY(${(1 - pb) * 24}px)`,
            textAlign: 'center',
          }}
        >
          {/* fila 1 · qué es y cuánto vale */}
          {/* ronda 7: centrados y apilados — el nombre del programa y, debajo, su precio */}
          <div style={{...eb.marca, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
            <div
              style={{
                fontFamily: DT.fuentes.titular,
                fontStyle: 'italic',
                fontSize: 70,
                lineHeight: 1,
                color: BLANCO,
                textShadow: SOMBRA,
                whiteSpace: 'nowrap',
              }}
            >
              <span style={{fontWeight: DT.pesos.semibold}}>Family</span>
              <span style={{fontWeight: DT.pesos.light}}> Time</span>
            </div>
            <div style={{marginTop: 12, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
              <div
                style={{
                  background: BLANCO,
                  color: AZUL,
                  borderRadius: 60,
                  padding: '8px 30px 4px',
                  fontFamily: TRADE_CN,
                  fontWeight: 700,
                  fontSize: 52,
                  lineHeight: 1,
                  letterSpacing: '0.01em',
                }}
              >
                $125.000
              </div>
              <div
                style={{
                  marginTop: 8,
                  fontFamily: DT.fuentes.texto,
                  fontSize: 21,
                  letterSpacing: '0.03em',
                  color: BLANCO,
                  textShadow: SOMBRA,
                }}
              >
                IVA INCLUIDO
              </div>
            </div>
          </div>

          <div style={{...eb.iconos, height: 1.5, background: 'rgba(250,250,250,0.5)', margin: '18px 0 16px'}} />

          {/* fila 2 · qué incluye */}
          <div style={{...eb.iconos, display: 'flex', justifyContent: 'space-between'}}>
            {INCLUIDOS.map((c) => (
              <div key={c.icono} style={{flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
                <Img src={staticFile(c.icono)} style={{height: 48, width: 48 * c.prop}} />
                <div
                  style={{
                    marginTop: 10,
                    fontFamily: DT.fuentes.titular,
                    fontWeight: DT.pesos.regular,
                    fontSize: 22,
                    lineHeight: 1.18,
                    color: BLANCO,
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
            ))}
          </div>

          <div style={{...eb.correo, height: 1.5, background: 'rgba(250,250,250,0.5)', margin: '16px 0 14px'}} />

          {/* fila 3 · cómo se reserva */}
          <div style={eb.correo}>
            <div
              style={{
                fontFamily: DT.fuentes.texto,
                fontSize: 29,
                lineHeight: 1,
                letterSpacing: '0.02em',
                color: BLANCO,
                textShadow: SOMBRA,
              }}
            >
              reservas.dtv@hilton.com
            </div>
            <div
              style={{
                marginTop: 12,
                fontFamily: DT.fuentes.texto,
                fontSize: 20,
                letterSpacing: '0.01em',
                color: BLANCO,
                textShadow: SOMBRA,
              }}
            >
              Válido jueves a domingo y festivos. Cupos limitados.
            </div>
          </div>
        </div>
      ) : null}

      {guia ? (
        <>
          <div style={{position: 'absolute', top: 0, left: 0, width: 1080, height: DT.seguras.story.arriba, background: 'rgba(255,0,110,0.3)'}} />
          <div style={{position: 'absolute', bottom: 0, left: 0, width: 1080, height: DT.seguras.story.abajo, background: 'rgba(255,0,110,0.3)'}} />
        </>
      ) : null}
    </AbsoluteFill>
  );
};

export const DtStFamilyTimeOctR9Guia: React.FC = () => <DtStFamilyTimeOctR9 guia />;
export const DtStFamilyTimeOctR9Grafica: React.FC = () => <DtStFamilyTimeOctR9 soloGrafica />;
export const DtStFamilyTimeOctR10: React.FC = () => <DtStFamilyTimeOctR9 fotos={FOTOS_R10} />;
