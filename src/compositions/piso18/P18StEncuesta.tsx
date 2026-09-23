/**
 * PISO18 — HISTORIA · «ENCUESTA MESA IDEAL» (STORIES col N · 25-09 · 12:00)
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL
 * ══════════════════════════════════════════════════════════════════════════
 * Hoja STORIES, columna N, estado **OK PARA DISEÑAR**:
 *
 *     ST ESTÁTICA - ENCUESTA MESA IDEAL
 *     Visual: Foto de tres montajes de mesa, cada uno con un arreglo floral
 *     distinto (ej. flores blancas, tonos pastel, flores tropicales), para
 *     comparar.
 *     Texto principal: ¿Cuál arreglo floral te gustaría en tu mesa?
 *     Bajada: Elige tu favorito (encuesta interactiva).
 *     CTA: Cotiza tu evento en piso18.cl
 *     INTERACCIÓN: Encuesta interactiva: arreglo floral A / B / C
 *     COMENTARIOS DISEÑO: «Encuesta de flores (ponemos distintos montajes
 *     enfocados en arreglos florales y los hacemos elegir)»
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REFERENCIA — `ST 4 S4 REF.jpg` (736×736)
 * ══════════════════════════════════════════════════════════════════════════
 * **Paneles verticales escalonados**: tiras de foto de la misma anchura, a
 * alturas alternadas, sobre un fondo claro partido por una banda. El titular va
 * abajo, en serif, con el subtítulo en versales muy espaciadas.
 *
 * Lo que se toma: las tiras verticales escalonadas y el bloque de texto al pie.
 * Lo que se adapta: la referencia tiene CUATRO tiras y acá van **TRES**, porque
 * la encuesta de Instagram es A / B / C.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LAS TRES FOTOS — el arreglo cambió, el salón NO
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐⭐ RONDA 3 — **las flores son REALES y de la sesión que mandó Eli**.
 *
 * Las rondas 1 y 2 usaban el montaje de agosto 2023 —mesas redondas con mantel
 * blanco— y a dos de las tres se les había cambiado la paleta con IA, porque en
 * ese material todo el follaje era del mismo evento. Eli lo rechazó: *«ya la mesa
 * blanca no son las actuales»* y *«usa para todas las que tengan que ver con
 * flores esta sesión»*.
 *
 * ⇒ Ahora las tres salen de **`Piso 18_28 ago decoración 2024`** (110 fotos,
 * 3840×5760), que es la sesión de decoración de verdad: montajes distintos, mesas
 * de madera y arreglos que ya vienen variados. **Cero IA en estas tres.**
 *
 *   A · `piso_18-13`  pampa seca con rosas rosadas y follaje rojo
 *   B · `piso_18-100` arreglo alto escultórico sobre mesa de madera, contra el ventanal
 *   C · `piso_18-62`  centro blanco y verde con velas y cristalería azul
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⚠️ LA INTERACCIÓN NO SE DIBUJA
 * ══════════════════════════════════════════════════════════════════════════
 * La encuesta A/B/C la pega el CM con el **sticker nativo de Instagram**. Lo que
 * hace la pieza es **dejarle el corredor libre**: el bloque de texto termina en
 * y=1436 y de ahí al borde quedan 484 px sin nada, más que los 340 de la zona
 * segura. Las letras A/B/C sí van marcadas sobre cada tira, para que el votante
 * sepa cuál es cuál.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {P18, cargarFuentesP18} from '../../brand/piso18';

const W = 1080;

/** Las tres opciones, en orden de votación. */
const OPCIONES = [
  /*
    ⚠️ Cada tira es un RECORTE DEDICADO, no la foto 4:5 con `objectPosition`.
    La tira es muy vertical (268×700, ratio 0,38): al recortar una foto 4:5 con
    `cover`, el ramo quedaba lejos y descentrado —y el brief pide justamente
    COMPARARLOS, así que un ramo chico no se puede votar.
    Los tres recortes se calcularon para que **el ramo ocupe la mitad del ancho
    de la tira y caiga al 40 % de su alto**, y por eso los tres se leen a la
    misma escala aunque en la foto original estuvieran a distancias distintas.
  */
  {letra: 'A', src: 'assets/hilton/piso18/tira-a.jpg', dy: 0},
  {letra: 'B', src: 'assets/hilton/piso18/tira-b.jpg', dy: 54},
  {letra: 'C', src: 'assets/hilton/piso18/tira-c.jpg', dy: 0},
] as const;

/**
 * ⭐ TEXTURA DE PAPEL — pedida por Eli en la ronda 2: *«al fondo beige añade
 * textura de papel sutil beige»*.
 *
 * Va **generada, no como archivo**: `feTurbulence` de tipo `fractalNoise` da la
 * fibra del papel sin sumar un asset de varios MB al repo, y se rinde idéntica
 * en cualquier máquina.
 *
 * Son dos capas, porque una sola se lee como ruido de cámara y no como papel:
 *   · fibra FINA (frecuencia alta) para el grano del gramaje;
 *   · veta ANCHA (frecuencia baja, muy tenue) para la irregularidad del pliego.
 *
 * ⚠️ Los números están CALIBRADOS sobre la pieza rendida, no puestos a ojo: la
 * entrega va a 2250 (×2,0833) y **el escalado suaviza el ruido**. Con la fibra a
 * `baseFrequency 0.82` y 4,4 % de opacidad la desviación del fondo quedaba en
 * 0,83 — invisible. Con grano más grueso y 13 % sube a un grano que se ve de
 * cerca y sigue leyéndose liso de lejos, que es lo que hace un papel.
 */
const TexturaPapel: React.FC = () => (
  <AbsoluteFill style={{pointerEvents: 'none'}}>
    <svg width={W} height={1920} style={{position: 'absolute', inset: 0}}>
      <filter id="p18-fibra">
        <feTurbulence type="fractalNoise" baseFrequency="0.46" numOctaves={4} seed={7} />
        <feColorMatrix type="saturate" values="0" />
      </filter>
      <filter id="p18-veta">
        <feTurbulence type="fractalNoise" baseFrequency="0.009 0.034" numOctaves={3} seed={19} />
        <feColorMatrix type="saturate" values="0" />
      </filter>
      <rect
        width="100%"
        height="100%"
        filter="url(#p18-fibra)"
        opacity={0.13}
        style={{mixBlendMode: 'multiply'}}
      />
      <rect
        width="100%"
        height="100%"
        filter="url(#p18-veta)"
        opacity={0.06}
        style={{mixBlendMode: 'multiply'}}
      />
    </svg>
  </AbsoluteFill>
);

/** Geometría de las tiras. Escalonadas: la del medio baja `dy`. */
const TIRA = {ancho: 268, alto: 700, hueco: 22, top: 380};

export const P18StEncuesta: React.FC = () => {
  cargarFuentesP18();
  const anchoTotal = TIRA.ancho * 3 + TIRA.hueco * 2;
  const x0 = (W - anchoTotal) / 2;

  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.beige}}>
      {/*
        La banda de la referencia: una franja de tono distinto que cruza el
        tercio superior y contra la que se recortan las tiras. Acá va en el
        off-white más frío para que no compita con la foto.
      */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 0,
          height: TIRA.top + 250,
          backgroundColor: P18.colores.beigeHondo,
        }}
      />

      {/*
        La textura va sobre los DOS beiges —el de base y el de la banda— y por
        debajo de todo lo demás: el papel es el soporte, no un velo encima de las
        fotos ni del texto.
      */}
      <TexturaPapel />

      {/* Logotipo arriba, centrado, a la geometría medida — en tinta sobre claro */}
      <Img
        src={staticFile('assets/hilton/piso18/logo.png')}
        style={{
          position: 'absolute',
          width: P18.geometria.logoAncho,
          height: P18.geometria.logoAncho / P18.geometria.logoProporcion,
          left: (W - P18.geometria.logoAncho) / 2,
          top: P18.geometria.logoYStory,
          // El PNG del logotipo es blanco: sobre fondo claro se invierte a tinta.
          filter: 'invert(1) brightness(0.12)',
        }}
      />

      {/* ── Las tres tiras escalonadas ─────────────────────────────────── */}
      {OPCIONES.map((o, i) => {
        const x = x0 + i * (TIRA.ancho + TIRA.hueco);
        const y = TIRA.top + o.dy;
        return (
          <div key={o.letra}>
            <div
              style={{
                position: 'absolute',
                left: x,
                top: y,
                width: TIRA.ancho,
                height: TIRA.alto,
                overflow: 'hidden',
              }}
            >
              <Img
                src={staticFile(o.src)}
                style={{width: '100%', height: '100%', objectFit: 'cover'}}
              />
            </div>
            {/*
              La letra de la opción. Va en una pastilla fucsia sólida sobre la
              esquina inferior de su tira: es el único elemento que le dice al
              votante qué foto es cuál, y por eso no puede depender del sticker.
            */}
            <div
              style={{
                position: 'absolute',
                left: x + 16,
                top: y + TIRA.alto - 70,
                width: 54,
                height: 54,
                borderRadius: 999,
                backgroundColor: P18.colores.fucsia,
                color: P18.colores.blanco,
                fontFamily: P18.fuentes.texto,
                fontWeight: 700,
                fontSize: 28,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              {o.letra}
            </div>
          </div>
        );
      })}

      {/*
        ── El bloque de texto, al pie ───────────────────────────────────
        La jerarquía de la marca: titular en IvyPresto con la palabra clave en
        itálica, y la bajada en Raleway en versales espaciadas —el mismo gesto
        de la línea `CENTRO DE EVENTOS` del logotipo.
        Los dos textos van verbatim del brief.
      */}
      <div
        style={{
          position: 'absolute',
          left: 96,
          right: 96,
          top: 1218,
          textAlign: 'center',
          color: P18.colores.tinta,
        }}
      >
        <div
          style={{
            fontFamily: P18.fuentes.titular,
            fontWeight: 300,
            fontSize: 60,
            lineHeight: 1.12,
          }}
        >
          ¿Cuál <span style={{fontStyle: 'italic', fontWeight: 400}}>arreglo floral</span>
          <br />
          te gustaría en tu mesa?
        </div>
        <div
          style={{
            marginTop: 26,
            fontFamily: P18.fuentes.texto,
            fontWeight: 500,
            fontSize: 25,
            letterSpacing: 4.2,
            textTransform: 'uppercase',
            color: P18.colores.fucsia,
          }}
        >
          Elige tu favorito
        </div>
      </div>

      {/*
        El CTA del brief. Va discreto al pie, en Raleway: en esta pieza el peso
        se lo lleva la encuesta, y el botón lleno competiría con el sticker que
        el CM va a pegar justo encima.
      */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 1436,
          textAlign: 'center',
          fontFamily: P18.fuentes.texto,
          fontWeight: 700,
          fontSize: 26,
          letterSpacing: 0.4,
          color: P18.colores.tinta,
        }}
      >
        Cotiza tu evento en <span style={{color: P18.colores.fucsia}}>piso18.cl</span>
      </div>
    </AbsoluteFill>
  );
};

/** Guía de QA: zonas seguras. El corredor de abajo es donde va el sticker. */
export const P18StEncuestaGuia: React.FC = () => (
  <AbsoluteFill>
    <P18StEncuesta />
    <AbsoluteFill>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 0,
          height: P18.seguras.story.arriba,
          background: 'rgba(255,0,0,0.22)',
          borderBottom: '2px solid red',
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 0,
          height: P18.seguras.story.abajo,
          background: 'rgba(255,0,0,0.22)',
          borderTop: '2px solid red',
        }}
      />
    </AbsoluteFill>
  </AbsoluteFill>
);
