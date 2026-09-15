/**
 * PISO18 — HISTORIA · «PLANIFICA TU EVENTO DE FIN DE AÑO»
 * (STORIES col P · 28-09 · 12:00 · S5 · estado OK PARA DISEÑAR)
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL
 * ══════════════════════════════════════════════════════════════════════════
 *     ST ESTÁTICA – PLANIFICA TU EVENTO DE FIN DE AÑO
 *
 *     Visual: Foto del salón Piso18 montado, mostrando su amplitud y buena
 *     iluminación, con vista de Santiago de fondo.
 *     Texto principal: Después de Fiestas Patrias, ¿ya pensaste en tu próximo
 *     evento?
 *     Bajada: Es momento de planificar tu evento de fin de año en Piso18.
 *
 *     INTERACCIÓN: Sticker de link a cotización. - CTA: Cotiza tu evento en
 *     piso18.cl
 *
 *     COMENTARIOS DISEÑO: «Hagamos lo de decir que luego de fiestas patrias
 *     toca pensar en tu evento de fin de año (no pongamos eso de cuántas
 *     personas caben)»
 *
 * ✅ El comentario está aplicado: **no aparece ninguna capacidad ni número de
 * invitados** en la pieza. Era lo único que pedía corregir.
 *
 * ⚠️ El CTA no sale del cuerpo del brief sino de la fila INTERACCIÓN, que es
 * donde esta grilla lo escribe. Va literal: `Cotiza tu evento en piso18.cl`.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REFERENCIA — `ref st n°1 s5.jpg`, la que dejó Eli en Drive el 15-09
 * ══════════════════════════════════════════════════════════════════════════
 * Una **agenda de anillas** de tapa de cuero oscuro, abierta sobre fondo casi
 * negro. Sobre la hoja crema hay una fotografía **sujeta con un clip**, y por
 * el costado derecho asoman **pestañas de índice** rotuladas en versales muy
 * espaciadas (THE STORY · THE STRATEGY · THE DIRECTION…). Abajo, el titular en
 * serif Didone mezclando **itálica y roman** («Behind the Brand»).
 *
 * Lo que se toma, que es lo que hace a la referencia: **el objeto planner** —el
 * papel, las anillas, el clip, las pestañas—, el titular serif mezclando
 * itálica y roman, y el fondo oscuro que lo recorta.
 *
 * ⭐ Y por qué esta referencia calza tan bien con este brief: el asunto de la
 * pieza es **planificar**. Una agenda no es un adorno acá, es el argumento.
 * Además resuelve un problema real de formato: el banco de esta marca es
 * horizontal y la historia es 9:16; metiendo la foto DENTRO de la hoja, sujeta
 * con un clip, la foto entra con su proporción propia y **no hay que recortar
 * un 3:2 a 9:16**, que es justo lo que la regla de la cuenta prohíbe («la foto
 * se PRODUCE, no se recorta»).
 *
 * Lo que se adapta:
 * · La serif es **IvyPresto**, que es la de la marca y es Didone igual que la
 *   de la referencia.
 * · Las pestañas se rotulan con **las cinco verticales del centro de eventos**
 *   —matrimonio, cumpleaños, corporativo, bautizo y fin de año—, con la última
 *   destacada en fucsia. No es un adorno: Eli dictó el 15-09 que «matrimonios
 *   es el foco pero la orden es mostrar más de lo demás», y la auditoría de
 *   septiembre dio bautizo = 0 piezas en todo el mes. Acá las cinco se ven.
 * · El papel es el beige del sistema con la textura generada, no un cuero.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA FOTO
 * ══════════════════════════════════════════════════════════════════════════
 * `banco-2026/0171` — el salón completo montado con mesas redondas, las
 * guirnaldas de luces encendidas y **la ciudad entera por los ventanales**.
 * Es la foto del banco que literalmente dice «amplitud y buena iluminación con
 * vista de Santiago de fondo». Real, sin una gota de IA.
 *
 * ⚠️ Ninguna foto se amplía: entra a 2000 px de ancho y se muestra a 690 @1080
 * → 1438 @2250, factor **0,72**.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {P18, cargarFuentesP18, GranoFondo} from '../../brand/piso18';

const W = 1080;

/** La hoja del planner. Todo lo demás se posiciona contra esta caja. */
const HOJA = {x: 64, y: 330, ancho: 886, alto: 1060};
/** Donde empieza y termina el contenido dentro de la hoja (tras las anillas). */
const CONT = {x: 176, ancho: 726};

/**
 * ⭐ TEXTURA DE PAPEL — la misma receta calibrada en la encuesta de la S4.
 * Va generada con `feTurbulence`, no como archivo: se rinde idéntica en
 * cualquier máquina y no suma megas al repo.
 *
 * ⚠️ Los valores están calibrados sobre la pieza RENDIDA a 2250 (×2,0833): el
 * escalado suaviza el ruido, así que con grano fino y poca opacidad la
 * desviación quedaba en 0,83 — o sea invisible.
 */
const TexturaPapel: React.FC<{x: number; y: number; ancho: number; alto: number}> = ({
  x,
  y,
  ancho,
  alto,
}) => (
  <svg
    width={ancho}
    height={alto}
    style={{position: 'absolute', left: x, top: y, pointerEvents: 'none'}}
  >
    <filter id="p18-fibra-pl">
      <feTurbulence type="fractalNoise" baseFrequency="0.46" numOctaves={4} seed={11} />
      <feColorMatrix type="saturate" values="0" />
    </filter>
    <filter id="p18-veta-pl">
      <feTurbulence type="fractalNoise" baseFrequency="0.009 0.034" numOctaves={3} seed={23} />
      <feColorMatrix type="saturate" values="0" />
    </filter>
    <rect
      width="100%"
      height="100%"
      filter="url(#p18-fibra-pl)"
      opacity={0.13}
      style={{mixBlendMode: 'multiply'}}
    />
    <rect
      width="100%"
      height="100%"
      filter="url(#p18-veta-pl)"
      opacity={0.06}
      style={{mixBlendMode: 'multiply'}}
    />
  </svg>
);

/**
 * Las anillas del planner. Van dibujadas, no como imagen: son seis aros
 * metálicos que perforan la hoja por el canto izquierdo. El aro se lee por el
 * degradado —claro arriba, oscuro abajo— y por la sombra que deja en el papel.
 */
const Anillas: React.FC = () => {
  const cx = HOJA.x + 52;
  const n = 6;
  const primera = HOJA.y + 108;
  const paso = (HOJA.alto - 216) / (n - 1);
  return (
    <svg
      width={140}
      height={HOJA.alto + 40}
      style={{position: 'absolute', left: HOJA.x - 40, top: HOJA.y - 20}}
    >
      <defs>
        <linearGradient id="p18-metal" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="#E7E3DC" />
          <stop offset="38%" stopColor="#9C958A" />
          <stop offset="62%" stopColor="#5E584F" />
          <stop offset="100%" stopColor="#B8B1A6" />
        </linearGradient>
      </defs>
      {Array.from({length: n}).map((_, i) => {
        const cy = primera + i * paso - HOJA.y + 20;
        return (
          <g key={i}>
            {/* la perforación del papel, que es lo que hace creíble el aro */}
            <ellipse cx={cx - HOJA.x + 40} cy={cy} rx={11} ry={13} fill="#D9CFBF" />
            <ellipse cx={cx - HOJA.x + 40} cy={cy + 2} rx={9} ry={11} fill="#C4B8A5" />
            {/* el aro */}
            <rect
              x={cx - HOJA.x + 40 - 30}
              y={cy - 9}
              width={60}
              height={18}
              rx={9}
              fill="url(#p18-metal)"
            />
            <rect
              x={cx - HOJA.x + 40 - 30}
              y={cy - 9}
              width={60}
              height={6}
              rx={3}
              fill="rgba(255,255,255,0.45)"
            />
          </g>
        );
      })}
    </svg>
  );
};

/**
 * El clip que sujeta la fotografía a la hoja. Es el gesto que más define la
 * referencia, así que va dibujado con su forma real —dos vueltas de alambre—
 * y no como un rectángulo: un clip mal dibujado delata la pieza entera.
 */
const Clip: React.FC<{x: number; y: number}> = ({x, y}) => (
  <svg
    width={64}
    height={132}
    style={{
      position: 'absolute',
      left: x,
      top: y,
      // Gira con la foto: un clip puesto a mano sigue el papel que sujeta.
      transform: 'rotate(-1.3deg)',
      // Sin sombra el clip flota sobre la foto en vez de apoyarse en ella.
      filter: 'drop-shadow(2px 4px 5px rgba(0,0,0,0.45))',
    }}
  >
    <defs>
      <linearGradient id="p18-clip" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stopColor="#8E8579" />
        <stop offset="40%" stopColor="#D8D2C7" />
        <stop offset="100%" stopColor="#7C7469" />
      </linearGradient>
    </defs>
    <path
      d="M20,124 L20,26 C20,10 44,10 44,26 L44,104 C44,116 28,116 28,104 L28,38"
      fill="none"
      stroke="url(#p18-clip)"
      strokeWidth={7}
      strokeLinecap="round"
    />
  </svg>
);

/**
 * ⚠️ LA PESTAÑA SE DIMENSIONA SOBRE LA ETIQUETA MÁS LARGA, NO SOBRE EL PROMEDIO.
 *
 * Es la misma regla que las cifras tabulares de esta marca, y acá se cobró: con
 * la pestaña a 128 px, `CORPORATIVO` y `CUMPLEAÑOS` se salían por abajo y se
 * metían en la pestaña siguiente. El rótulo va en vertical, así que su largo
 * ocupa el ALTO de la pestaña:
 *
 *   `CORPORATIVO` = 11 caracteres × (14 px × 0,70 de avance medio en Raleway
 *   + 3,0 de tracking) ≈ 141 px  →  la caja se pone en 176 y quedan 35 de aire.
 *
 * Y se calcula, no se pone a ojo: si mañana entra `ANIVERSARIOS` el número se
 * mueve solo en vez de volver a desbordarse en silencio.
 */
const ROTULO_CUERPO = 14;
const ROTULO_TRACKING = 3.0;

/** Las cinco verticales del centro de eventos, en pestañas de índice. */
const VERTICALES = [
  {rotulo: 'MATRIMONIO', activa: false},
  {rotulo: 'CUMPLEAÑOS', activa: false},
  {rotulo: 'CORPORATIVO', activa: false},
  {rotulo: 'BAUTIZO', activa: false},
  {rotulo: 'FIN DE AÑO', activa: true},
] as const;

export const P18StPlanifica: React.FC = () => {
  cargarFuentesP18();

  const foto = {x: CONT.x + 18, y: HOJA.y + 66, ancho: 690, alto: 460};

  // El alto de la pestaña sale del rótulo más largo, con 35 px de aire.
  const largoMax = Math.max(...VERTICALES.map((v) => v.rotulo.length));
  const altoRotulo = largoMax * (ROTULO_CUERPO * 0.7 + ROTULO_TRACKING);
  const pestana = {
    x: HOJA.x + HOJA.ancho - 8,
    ancho: 104,
    alto: Math.ceil(altoRotulo + 35),
    hueco: 12,
  };
  // Las cinco pestañas se centran verticalmente contra la hoja.
  const bloque = VERTICALES.length * pestana.alto + (VERTICALES.length - 1) * pestana.hueco;
  const pestanaY0 = HOJA.y + (HOJA.alto - bloque) / 2;

  return (
    <AbsoluteFill style={{backgroundColor: '#0B0B0E'}}>
      {/*
        El fondo de la referencia no es negro plano: es un cuero oscuro con una
        luz suave arriba. Acá se resuelve con un radial muy tenue, que además
        levanta el logotipo blanco sin necesidad de velo.
      */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(120% 70% at 50% 8%, rgba(74,66,60,0.55) 0%, rgba(20,18,20,0.35) 42%, rgba(8,8,11,0) 72%)',
        }}
      />

      {/*
        El grano del fondo. Va INMEDIATAMENTE sobre el degradado y debajo de
        todo lo demás: es la materia del soporte —el cuero de la referencia—,
        no un velo encima de la hoja ni del texto.
      */}
      <GranoFondo semilla={5} />

      {/* ── Logotipo: arriba, centrado, geometría medida ────────────────── */}
      <Img
        src={staticFile('assets/hilton/piso18/logo.png')}
        style={{
          position: 'absolute',
          width: P18.geometria.logoAncho,
          height: P18.geometria.logoAncho / P18.geometria.logoProporcion,
          left: (W - P18.geometria.logoAncho) / 2,
          top: P18.geometria.logoYStory,
        }}
      />

      {/* ── Las pestañas de índice ──────────────────────────────────────
          Van DEBAJO de la hoja en el apilado, para que sólo asome la parte que
          sobresale por el canto derecho — que es exactamente lo que se ve en
          la referencia. Si fueran encima se leerían como botones pegados. */}
      {VERTICALES.map((v, i) => (
        <div
          key={v.rotulo}
          style={{
            position: 'absolute',
            left: pestana.x,
            top: pestanaY0 + i * (pestana.alto + pestana.hueco),
            width: pestana.ancho,
            height: pestana.alto,
            borderRadius: '0 10px 10px 0',
            backgroundColor: v.activa ? P18.colores.fucsia : '#E4DACB',
            boxShadow: '4px 3px 14px rgba(0,0,0,0.38)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'flex-end',
            paddingRight: 12,
          }}
        >
          <span
            style={{
              writingMode: 'vertical-rl',
              fontFamily: P18.fuentes.texto,
              fontWeight: 700,
              fontSize: ROTULO_CUERPO,
              letterSpacing: ROTULO_TRACKING,
              color: v.activa ? P18.colores.blanco : '#6B6259',
            }}
          >
            {v.rotulo}
          </span>
        </div>
      ))}

      {/* ── La hoja del planner ─────────────────────────────────────────── */}
      <div
        style={{
          position: 'absolute',
          left: HOJA.x,
          top: HOJA.y,
          width: HOJA.ancho,
          height: HOJA.alto,
          backgroundColor: P18.colores.beige,
          borderRadius: 6,
          boxShadow: '0 26px 70px rgba(0,0,0,0.55)',
        }}
      />
      <TexturaPapel x={HOJA.x} y={HOJA.y} ancho={HOJA.ancho} alto={HOJA.alto} />

      {/* La foto del salón, sujeta con el clip. Levemente girada, como en la
          referencia: una foto puesta a mano nunca queda a escuadra. */}
      <div
        style={{
          position: 'absolute',
          left: foto.x,
          top: foto.y,
          width: foto.ancho,
          height: foto.alto,
          transform: 'rotate(-1.3deg)',
          boxShadow: '0 12px 30px rgba(0,0,0,0.30)',
          backgroundColor: '#FFFFFF',
          padding: 10,
        }}
      >
        <Img
          src={staticFile('assets/hilton/piso18/s5-salon-amplio.jpg')}
          style={{width: '100%', height: '100%', objectFit: 'cover'}}
        />
      </div>
      <Clip x={foto.x + foto.ancho - 132} y={foto.y - 34} />

      <Anillas />

      {/* ── El titular, sobre la hoja y en tinta ─────────────────────────
          La jerarquía de la marca: la línea que importa en ITÁLICA y el resto
          en roman. Verbatim del brief, partido en tres líneas para que ninguna
          pase del ancho de la hoja. */}
      <div
        style={{
          position: 'absolute',
          left: CONT.x,
          width: CONT.ancho,
          top: HOJA.y + 610,
          textAlign: 'center',
          color: P18.colores.tinta,
          fontFamily: P18.fuentes.titular,
        }}
      >
        <div style={{fontSize: 44, fontWeight: 300, lineHeight: 1.14, letterSpacing: 0.2}}>
          Después de Fiestas Patrias,
        </div>
        <div style={{fontSize: 58, fontWeight: 300, lineHeight: 1.12, marginTop: 6}}>
          ¿ya pensaste en
        </div>
        <div style={{fontSize: 58, fontWeight: 400, fontStyle: 'italic', lineHeight: 1.12}}>
          tu próximo evento?
        </div>
      </div>

      {/* ── La bajada, en Raleway ───────────────────────────────────────── */}
      <div
        style={{
          position: 'absolute',
          left: CONT.x + 40,
          width: CONT.ancho - 80,
          top: HOJA.y + 832,
          textAlign: 'center',
          fontFamily: P18.fuentes.texto,
          fontWeight: 500,
          fontSize: 28,
          lineHeight: 1.5,
          color: '#4A443C',
        }}
      >
        Es momento de planificar tu evento de fin de año en Piso18.
      </div>

      {/* ── EL BOTÓN DE COTIZACIÓN ──────────────────────────────────────
          Obligatorio en historias, esquema A (fucsia lleno). Va FUERA de la
          hoja, sobre el fondo oscuro: así es lo último que se lee y queda
          justo encima del corredor donde el CM pega el sticker de enlace.
          Su base cae en y=1516 — los mismos 64 px de holgura sobre la zona
          segura inferior que tiene la historia aprobada de la S4. */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 1440,
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
            fontSize: 31,
            letterSpacing: 0.6,
            padding: '23px 54px',
            borderRadius: 999,
            boxShadow: '0 8px 30px rgba(0,0,0,0.48)',
          }}
        >
          Cotiza tu evento en piso18.cl
        </div>
      </div>

      {/* La dirección, que es el cierre que usa la grilla de esta cuenta. */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 1546,
          textAlign: 'center',
          fontFamily: P18.fuentes.texto,
          fontWeight: 500,
          fontSize: 22,
          letterSpacing: 1.4,
          color: 'rgba(255,255,255,0.70)',
        }}
      >
        {P18.contacto.direccion}
      </div>
    </AbsoluteFill>
  );
};

/** Guía de QA: zonas seguras de historia. No se entrega. */
export const P18StPlanificaGuia: React.FC = () => (
  <AbsoluteFill>
    <P18StPlanifica />
    <AbsoluteFill style={{pointerEvents: 'none'}}>
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
