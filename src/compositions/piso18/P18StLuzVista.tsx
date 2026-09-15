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
 * ⭐⭐ RONDA 2 — SON DOS FOTOS, NO FOTO Y COLOR
 * ══════════════════════════════════════════════════════════════════════════
 * La ronda 1 partía la pieza en foto arriba y **fucsia sólido abajo**. Eli la
 * corrigió sobre la propia referencia, marcando a mano un **1** en la mitad de
 * arriba y un **2** en la de abajo:
 *
 * > *«la idea es hacer una transición del fondo del cielo y la ventana, la foto
 * > está correcta, pero abajo, en vez de el color de piso18, otra foto; la idea
 * > es que sea similar a la referencia.»*
 *
 * Y tenía razón contra la referencia: en `ST 2 S4 REF.jpg` la mitad de abajo no
 * es un plano de color, es **otra fotografía** —cielo con nubes— y la onda es la
 * costura entre las dos. La ronda 1 leyó esa mitad como color plano porque el
 * cielo de la referencia es muy saturado.
 *
 * ⇒ Ahora son **dos fotos cosidas por la onda**: arriba la ventana, abajo el
 * cielo abierto. Eso es literalmente «la transición del cielo y la ventana».
 *
 * ⚠️ Y trae una consecuencia de contraste: el fucsia sólido sostenía texto blanco
 * sin pensarlo, y **un cielo de hora dorada no**. Se midió la luminancia de la
 * banda donde cae la bajada (ver `VELO_ABAJO`) y por eso el cielo lleva un velo
 * cálido de refuerzo en su parte baja: sin él la bajada se perdía sobre las nubes.
 *
 * ⭐ El fucsia no desaparece de la pieza: vuelve donde la marca lo quiere, en el
 * **botón de cotización** — y en esquema A (fucsia lleno), que es el principal.
 * En la ronda 1 iba invertido sólo porque el fondo ya era fucsia.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LAS DOS FOTOS — las dos se PRODUJERON, ninguna se recortó de un banco
 * ══════════════════════════════════════════════════════════════════════════
 * **En todo el material de Piso18 no hay una sola foto de atardecer**: la sesión
 * de agosto 2023 (121 fotos) es de noche o interior oscuro. Eli resolvió el 15-09:
 * **reiluminar una foto real con ventanal**.
 *
 * - **Arriba:** `0198.jpg` —la referencia que el propio brief del feed enlaza— que
 *   es el ventanal real de Piso18 con la Torre Titanium y los cerros. Se le cambió
 *   SÓLO la hora del día, conservando marcos, pasamanos, mesa y la forma exacta
 *   de la torre.
 * - **Abajo:** el cielo de esa misma escena, abierto en plano amplio, generado
 *   **con la foto de arriba como referencia de color** para que las dos sean la
 *   misma hora y la misma paleta. Si no, la costura de la onda se nota.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * GEOMETRÍA — de `src/brand/piso18.ts`, medida sobre las piezas aprobadas
 * ══════════════════════════════════════════════════════════════════════════
 * Mesa 1080×1920; se entrega a 2250×4000 con `--scale=2.0833`.
 *
 * ⚠️ **El botón de cotización es obligatorio** en historias (dictado de Eli).
 * ⚠️ **La interacción NO se dibuja**: el sticker de link lo pone el CM.
 *
 * ⚠️ Zonas seguras de Instagram, que Eli pidió respetar: el titular vive entre
 * y=760 y y=1010, la bajada en y=1302 y el botón termina en y=1516 — 64 px por
 * encima de los 340 que Instagram se come abajo.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {P18, cargarFuentesP18} from '../../brand/piso18';

const H = 1920;
const W = 1080;

/**
 * Dónde cruza la onda. La referencia la pone a ~57 % del alto; acá va a 60 %
 * porque el titular de esta marca es de tres líneas y necesita más aire arriba.
 */
const CORTE = 0.6;

/**
 * La curva, como cadena de `path` reutilizable: la dibuja el borde blanco Y la
 * usa el recorte de la foto de abajo, así que **tiene que ser la misma** o
 * aparece una costura de un píxel entre el filo y la foto.
 *
 * ⛔ Y va armada con `join(' ')`, en UNA SOLA LÍNEA, no con un template literal
 * multilínea. `clip-path: path()` con saltos de línea adentro **Chrome lo
 * descarta EN SILENCIO**: la propiedad se ignora, el recorte no se aplica y la
 * foto de abajo tapa la pieza entera. `<path d>` en SVG sí los tolera, así que
 * el filo blanco seguía dibujándose y parecía que todo estaba bien. Pasó en la
 * ronda 2 y costó un render.
 */
const curva = (y: number) =>
  [
    `M0,${y - 46}`,
    `C ${W * 0.22},${y - 108} ${W * 0.34},${y + 74} ${W * 0.56},${y + 58}`,
    `C ${W * 0.74},${y + 45} ${W * 0.86},${y - 40} ${W},${y - 18}`,
  ].join(' ');

export const P18StLuzVista: React.FC = () => {
  cargarFuentesP18();
  const yCorte = H * CORTE;
  const recorte = `path('${curva(yCorte)} L ${W},${H} L 0,${H} Z')`;

  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      {/* ── FOTO 1 · la ventana, a sangre ──────────────────────────────── */}
      <AbsoluteFill>
        <Img
          src={staticFile('assets/hilton/piso18/atardecer.jpg')}
          style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center 38%'}}
        />
      </AbsoluteFill>

      {/*
        Velo superior. Es el mismo recurso que trae la plantilla de la marca
        (`logo PISO18.png`, alfa 150 arriba → 0 hacia el medio) y existe para que
        el logotipo blanco se lea sobre la foto. Acá va suave porque el cielo de
        hora dorada ya es claro.
      */}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(0,0,0,0.42) 0%, rgba(0,0,0,0.10) 26%, rgba(0,0,0,0) 44%)',
        }}
      />

      {/* ── FOTO 2 · el cielo, recortado por la onda ───────────────────── */}
      <AbsoluteFill style={{clipPath: recorte, WebkitClipPath: recorte} as React.CSSProperties}>
        <Img
          src={staticFile('assets/hilton/piso18/cielo.jpg')}
          style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center 62%'}}
        />
        {/*
          ⚠️ VELO_ABAJO — el que hace legible la bajada. Un cielo de hora dorada
          es CLARO: sin esto el texto blanco se pierde sobre las nubes. Va cálido
          y en degradado desde el pie para no ensuciar el cielo de la costura.
        */}
        <AbsoluteFill
          style={{
            background:
              'linear-gradient(to bottom, rgba(26,16,10,0) 0%, rgba(26,16,10,0.20) 34%, rgba(26,16,10,0.52) 66%, rgba(26,16,10,0.66) 100%)',
          }}
        />
      </AbsoluteFill>

      {/* El filo blanco de la costura — el mismo gesto de la referencia. */}
      <svg width={W} height={H} viewBox={`0 0 ${W} ${H}`} style={{position: 'absolute', inset: 0}}>
        <path d={curva(yCorte)} fill="none" stroke="#FFFFFF" strokeWidth={3} opacity={0.92} />
      </svg>

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
        ── EL TITULAR, sobre la ventana y por encima de la curva ─────────
        El contraste de la marca: la línea que importa en ITÁLICA, el resto en
        roman. Verbatim del brief.
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

      {/* ── La bajada, ya sobre el cielo ────────────────────────────────── */}
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
          textShadow: '0 2px 14px rgba(26,16,10,0.55)',
        }}
      >
        La vista panorámica de Santiago se viste de atardecer para tu celebración.
      </div>

      {/*
        ── EL BOTÓN DE COTIZACIÓN ───────────────────────────────────────
        Obligatorio en historias. **Esquema A (fucsia lleno)**, que es el
        principal: acá el fondo ya no es fucsia, así que el fucsia vuelve al
        botón — y es lo único de ese color en la pieza, que es como la marca lo usa.
        Su base cae en y=1516: 64 px por encima de la zona segura inferior.
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
            backgroundColor: P18.botones.lleno.fondo,
            color: P18.botones.lleno.texto,
            fontFamily: P18.fuentes.texto,
            fontWeight: 700,
            fontSize: 33,
            letterSpacing: 0.6,
            padding: '26px 58px',
            borderRadius: 999,
            boxShadow: '0 6px 26px rgba(26,16,10,0.34)',
          }}
        >
          Cotiza tu evento en piso18.cl
        </div>
      </div>
    </AbsoluteFill>
  );
};

/**
 * Guía de QA: zonas seguras de historia. No se entrega — se mira al lado de la
 * pieza para comprobar que nada cae bajo la interfaz de Instagram ni donde el CM
 * pega el sticker.
 */
export const P18StLuzVistaGuia: React.FC = () => (
  <AbsoluteFill>
    <P18StLuzVista />
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
