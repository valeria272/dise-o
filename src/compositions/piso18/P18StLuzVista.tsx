/**
 * PISO18 — HISTORIA · «LA LUZ DE LA VISTA» (STORIES col L · 22-09 · 18:00)
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL — de la grilla viva, verificada contra la instantánea
 * ══════════════════════════════════════════════════════════════════════════
 * Hoja STORIES, columna L, estado **OK PARA DISEÑAR**:
 *
 *     ST ESTÁTICA - LA LUZ DE LA VISTA
 *     Visual: Foto del atardecer tipo golden hour desde Piso18, luz dorada de
 *     primavera iluminando el salón y la vista de Santiago.
 *     Texto principal: Hay luces que solo se ven desde Piso18
 *     Bajada: La vista panorámica de Santiago se viste de atardecer para tu
 *     celebración.
 *     CTA: Cotiza tu evento en piso18.cl
 *     INTERACCIÓN: Sticker de link a cotización.
 *     COMENTARIOS DISEÑO: «Si va a ser como de ''golden hour'' hablemos de
 *     aterdecer más que de primavera»
 *
 * ⭐ El comentario del cliente ya está resuelto EN EL PROPIO BRIEF: los dos
 * textos hablan de atardecer y ninguno de primavera. No hay nada que reescribir
 * — y los textos van **verbatim**.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REFERENCIA que dejó Eli — `ST 2 S4 REF.jpg` (736×1308)
 * ══════════════════════════════════════════════════════════════════════════
 * Una historia partida por un **corte ondulado**: foto de ciudad arriba, zona
 * de color plano abajo, y la palabra clave en **script manuscrito** cabalgando
 * la línea del corte. La bajada va en sans ligera, alineada a la derecha.
 *
 * Lo que se toma de ella: **la estructura** —foto arriba / onda / color abajo,
 * con el titular montado sobre la curva—. Lo que NO se toma: su paleta (azul
 * turquesa) ni su tipografía script, que no son de esta marca.
 *
 * ⚠️ El script de la referencia sería `Edwardian Script ITC` —la cuarta voz del
 * sistema— pero **ese archivo no está en el repo**. Hasta que Eli lo mande, la
 * palabra destacada va en **IvyPresto itálica**, que es la voz principal de la
 * marca y sostiene el mismo gesto. Queda anotado, no disimulado.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA FOTO — se PRODUJO, no se recortó
 * ══════════════════════════════════════════════════════════════════════════
 * **En todo el material de Piso18 no hay una sola foto de atardecer**: la sesión
 * de agosto 2023 (121 fotos) es de noche o interior oscuro, y el reportaje de
 * matrimonio tampoco trae la vista. Eli resolvió el 15-09: **reiluminar una foto
 * real con ventanal**.
 *
 * La base es `0198.jpg` —la referencia que el propio brief del feed enlaza—, que
 * es el ventanal real de Piso18 con la Torre Titanium y los cerros. Se le cambió
 * SÓLO la hora del día a hora dorada, conservando marcos, pasamanos, mesa,
 * botellas y la forma exacta de la torre. Es el mismo uso de IA que ya hacen los
 * editables de la marca («que se vea iluminado de día»): se retoca lo real, no se
 * inventa la escena.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * GEOMETRÍA — de `src/brand/piso18.ts`, medida sobre las piezas aprobadas
 * ══════════════════════════════════════════════════════════════════════════
 * Mesa 1080×1920; se entrega a 2250×4000 con `--scale=2.0833`.
 *
 * ⚠️ **El botón de cotización es obligatorio** en historias (dictado de Eli,
 * 15-09): la marca quiere redirigir a cotizar. Va en esquema A (fucsia lleno).
 * ⚠️ **La interacción NO se dibuja**: el sticker de link lo pone el CM. Lo que
 * hace la pieza es dejarle el aire.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {P18, cargarFuentesP18} from '../../brand/piso18';

/** Alto de la mesa. La historia es 9:16 exacta. */
const H = 1920;
const W = 1080;

/**
 * Dónde cruza la onda. La referencia la pone a ~57 % del alto; acá baja a 60 %
 * porque el titular de esta marca es de dos líneas y necesita más aire arriba.
 */
const CORTE = 0.6;

/**
 * La onda. Es una curva suave de un solo valle, no un zigzag: sube por la
 * izquierda, cae al centro-derecha y remonta al borde. Se dibuja como `path`
 * sobre el ancho completo para que no se vea una costura en los bordes.
 */
const Onda: React.FC<{y: number; color: string}> = ({y, color}) => (
  <svg
    width={W}
    height={H}
    viewBox={`0 0 ${W} ${H}`}
    style={{position: 'absolute', inset: 0}}
  >
    <path
      d={`M0,${y - 46}
          C ${W * 0.22},${y - 108} ${W * 0.34},${y + 74} ${W * 0.56},${y + 58}
          C ${W * 0.74},${y + 45} ${W * 0.86},${y - 40} ${W},${y - 18}
          L ${W},${H} L 0,${H} Z`}
      fill={color}
    />
  </svg>
);

export const P18StLuzVista: React.FC = () => {
  cargarFuentesP18();
  const yCorte = H * CORTE;

  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.fucsia}}>
      {/* ── La foto, a sangre en la mitad superior ─────────────────────── */}
      <AbsoluteFill>
        <Img
          src={staticFile('assets/hilton/piso18/atardecer.jpg')}
          style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center 38%'}}
        />
      </AbsoluteFill>

      {/*
        Velo superior. Es el mismo recurso que trae la plantilla de la marca
        (`logo PISO18.png`, alfa 150 arriba → 0 hacia el medio) y existe para
        que el logotipo blanco se lea sobre la foto. Acá va más suave porque el
        cielo de hora dorada ya es claro.
      */}
      <AbsoluteFill
        style={{
          background: 'linear-gradient(to bottom, rgba(0,0,0,0.42) 0%, rgba(0,0,0,0.10) 26%, rgba(0,0,0,0) 44%)',
        }}
      />

      {/* ── La onda fucsia ────────────────────────────────────────────── */}
      <Onda y={yCorte} color={P18.colores.fucsia} />

      {/* ── Logotipo: arriba, centrado, a la geometría medida ──────────── */}
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

      {/*
        ── EL TITULAR, montado sobre la curva ──────────────────────────
        Va en dos líneas y con el mismo contraste de la marca: la palabra que
        importa en ITÁLICA, el resto en roman. Verbatim del brief.
      */}
      <div
        style={{
          position: 'absolute',
          left: 84,
          right: 84,
          top: yCorte - 392,
          textAlign: 'center',
          color: P18.colores.blanco,
          fontFamily: P18.fuentes.titular,
          textShadow: '0 3px 18px rgba(0,0,0,0.62), 0 8px 44px rgba(0,0,0,0.42)',
        }}
      >
        <div style={{fontSize: 74, fontWeight: 300, lineHeight: 1.06}}>Hay luces</div>
        <div style={{fontSize: 92, fontWeight: 400, fontStyle: 'italic', lineHeight: 1.04}}>
          que solo se ven
        </div>
        <div style={{fontSize: 74, fontWeight: 300, lineHeight: 1.1, letterSpacing: 1}}>
          desde Piso18
        </div>
      </div>

      {/*
        ── La bajada, ya dentro del fucsia ──────────────────────────────
        Raleway, que es la legible: es el caballo de batalla de la marca para
        todo lo que no sea titular.
      */}
      <div
        style={{
          position: 'absolute',
          left: 128,
          right: 128,
          top: yCorte + 150,
          textAlign: 'center',
          color: P18.colores.blanco,
          fontFamily: P18.fuentes.texto,
          fontWeight: 500,
          fontSize: 35,
          lineHeight: 1.5,
          letterSpacing: 0.2,
        }}
      >
        La vista panorámica de Santiago se viste de atardecer para tu celebración.
      </div>

      {/*
        ── EL BOTÓN DE COTIZACIÓN ───────────────────────────────────────
        Obligatorio en historias. Esquema B (invertido: blanco con texto fucsia),
        porque el fondo de esta pieza ya es el fucsia lleno — el esquema A se
        perdería sobre sí mismo.
        ⚠️ Queda por encima de la zona segura inferior (340 px): su base cae en
        y=1500, o sea 420 px de aire bajo el botón.
      */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: yCorte + 322,
          display: 'flex',
          justifyContent: 'center',
        }}
      >
        <div
          style={{
            backgroundColor: P18.botones.invertido.fondo,
            color: P18.botones.invertido.texto,
            fontFamily: P18.fuentes.texto,
            fontWeight: 700,
            fontSize: 33,
            letterSpacing: 0.6,
            padding: '26px 58px',
            borderRadius: 999,
          }}
        >
          Cotiza tu evento en piso18.cl
        </div>
      </div>
    </AbsoluteFill>
  );
};

/**
 * Guía de QA: zonas seguras de historia y la línea del corte. No se entrega —
 * se mira al lado de la pieza para comprobar que nada cae bajo la interfaz de
 * Instagram ni donde el CM pega el sticker.
 */
export const P18StLuzVistaGuia: React.FC = () => (
  <AbsoluteFill>
    <P18StLuzVista />
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
