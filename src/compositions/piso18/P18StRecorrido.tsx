/**
 * PISO18 — HISTORIA · «VISITA GUIADA VIRTUAL»
 * (STORIES col Q · 30-09 · 18:00 · S5 · estado OK PARA DISEÑAR)
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL — y la corrección del cliente, que MANDA sobre él
 * ══════════════════════════════════════════════════════════════════════════
 *     ST ESTÁTICA - VISITA GUIADA VIRTUAL
 *
 *     Visual: Colección de fotos/video corto recorriendo distintos ángulos del
 *     salón Piso18.
 *     Texto principal: ¿Conocías nuestro recorrido virtual?
 *     Bajada: Descubre cada rincón de Piso18 desde donde estés y vive la
 *     experiencia antes de reservar.
 *
 *     INTERACCIÓN: Sticker de link a visita virtual
 *
 *     COMENTARIOS DISEÑO: «Sin lo de antes de que termine el año. Siempre que
 *     hablemos del recorrido virtual hablémosle a alguien que nunca se ha
 *     metido a verlo, ya que esa es la persona que queremos que entre.
 *     Más como ''¿Conocías nuestro recorrido virtual?'' ''recorre cada rincón
 *     Piso18 desde donde estés''»
 *
 * ✅ Los dos textos son los que pidió el cliente en el comentario, no los del
 * cuerpo del brief: el titular ya coincide y **la bajada se reemplazó** por la
 * suya, que es más corta y saca el «antes de reservar».
 *
 * ⚠️ Él la escribió «recorre cada rincón Piso18 desde donde estés» y acá va
 * **«Recorre cada rincón de Piso18 desde donde estés.»** — se le repuso la
 * preposición que falta y el punto final, porque en su propio brief la frase
 * es «cada rincón **de** Piso18». Es la única libertad que se tomó con el
 * texto y queda anotada: si él la quiere exactamente como la tipeó, se cambia.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⛔ POR QUÉ ESTA PIEZA NO LLEVA BOTÓN — decisión de Eli, 15-09
 * ══════════════════════════════════════════════════════════════════════════
 * La regla dictada dice que **siempre** hay botón en las historias. Acá no lo
 * hay, y es la propia excepción del cliente: sobre la ST del 18-09 escribió
 * *«el botón de cotiza lo eliminamos y dejamos solo el botón de enlace cuando
 * lo subamos, para no redundar»*. Esta historia lleva **sticker de link a
 * visita virtual**, o sea el mismo caso.
 *
 * ⇒ La pieza deja los **400 px** de abajo completamente libres —más que los
 * 340 de la zona segura— para que el sticker de enlace caiga ahí y sea el
 * único llamado a la acción. La interacción NO se dibuja: la pone el CM.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REFERENCIA — `ref st n°2 s5.jpg`, la que dejó Eli en Drive el 15-09
 * ══════════════════════════════════════════════════════════════════════════
 * **Dos teléfonos** en primer plano, uno algo más bajo que el otro, mostrando
 * dos pantallas de un mismo sitio, sobre un fondo fotográfico desaturado.
 * Arriba, una línea corta en versales muy espaciadas, el titular grande en
 * serif, y debajo otra línea en versales espaciadas.
 *
 * Lo que se toma: **los dos teléfonos escalonados** —que es lo que convierte
 * «recorrido virtual» en algo que se ve—, el fondo fotográfico desaturado que
 * los recorta, y el sándwich de versales espaciadas alrededor del titular.
 *
 * Lo que se adapta:
 * · La serif es IvyPresto y no una script — la marca no tiene script.
 *   (`Edwardian Script ITC` es la cuarta voz del sistema y **sigue sin estar
 *   en el repo**; cuando llegue, esta pieza es candidata a revisarse.)
 * · El fondo no es un cielo: es **el propio salón**, desaturado y oscurecido,
 *   porque el recorrido virtual es del salón y no de otra cosa.
 * · Las pantallas muestran **dos ángulos distintos del salón real**, que es
 *   literalmente lo que pide el brief («distintos ángulos del salón Piso18»).
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LAS FOTOS — las tres reales, cero IA
 * ══════════════════════════════════════════════════════════════════════════
 * · Fondo:      `banco-2026/0177` — el salón montado con la ciudad al fondo.
 * · Pantalla A: `banco-2026/0178` — mesa montada contra el ventanal.
 * · Pantalla B: `banco-2026/0171` — el salón completo, plano general.
 *
 * ⚠️ Ninguna se amplía: las pantallas entran a 900 px de ancho y se muestran a
 * 344 @1080 → 717 @2250, factor **0,80**.
 *
 * ⚠️ Y el mockup respeta la regla de la cuenta: la maqueta es del **sitio
 * propio** (`piso18.cl`), no la interfaz de un producto ajeno, y la píldora
 * del 360° se dimensiona con el ancho de la pantalla —`flexShrink: 0` y
 * `nowrap`— para que no se desborde como pasó en el reel de EBEMA Click.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {P18, cargarFuentesP18, GranoFondo} from '../../brand/piso18';

const W = 1080;

/** Geometría del teléfono. El alto sale de la proporción 9:19,5 de la pantalla. */
const TEL = {ancho: 344, alto: 746, radio: 44, marco: 11};

/**
 * ⭐ EL BLOQUE DE TELÉFONOS SE CENTRA POR CÁLCULO, NO CON DOS `x` A MANO.
 *
 * Ronda 2 de Eli: *«segunda necesito que centres el celular y los textos»*.
 * Medido sobre la ronda 1: los dos teléfonos ocupaban de x=150 a x=804, o sea
 * centro en **477 contra los 540 del lienzo — 63 px corridos a la izquierda**.
 * Estaban puestos con dos números escritos a mano y nadie los sumó.
 *
 * Ahora el ancho del bloque sale del solape y el margen izquierdo se deduce, así
 * que cambiar el solape o el ancho del teléfono no vuelve a descentrarlo.
 */
const SOLAPE = 34;
const BLOQUE = TEL.ancho * 2 - SOLAPE;
const BLOQUE_X = (W - BLOQUE) / 2;

/**
 * Un teléfono con su pantalla. El marco va oscuro y mate —no negro puro— para
 * que sobre el fondo desaturado se separe sin recortarse como una silueta.
 */
const Telefono: React.FC<{
  src: string;
  x: number;
  y: number;
  giro: number;
  rotulo: string;
}> = ({src, x, y, giro, rotulo}) => (
  <div
    style={{
      position: 'absolute',
      left: x,
      top: y,
      width: TEL.ancho,
      height: TEL.alto,
      transform: `rotate(${giro}deg)`,
      borderRadius: TEL.radio,
      backgroundColor: '#14141A',
      padding: TEL.marco,
      boxShadow: '0 30px 70px rgba(0,0,0,0.62), 0 0 0 1px rgba(255,255,255,0.10)',
    }}
  >
    <div
      style={{
        position: 'relative',
        width: '100%',
        height: '100%',
        borderRadius: TEL.radio - TEL.marco,
        overflow: 'hidden',
        backgroundColor: '#000',
      }}
    >
      <Img src={staticFile(src)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />

      {/* La isla del sensor. Sin esto el marco no se lee como un teléfono. */}
      <div
        style={{
          position: 'absolute',
          left: '50%',
          top: 14,
          transform: 'translateX(-50%)',
          width: 84,
          height: 22,
          borderRadius: 999,
          backgroundColor: '#0A0A0C',
        }}
      />

      {/*
        La píldora del recorrido. Va abajo en la pantalla, sobre un velo corto,
        y es el único elemento de interfaz: dice qué está viendo el teléfono.
        ⚠️ `flexShrink: 0` + `nowrap` + cuerpo atado al ancho de la pantalla —
        la lección del mock de UI que se desbordó en el reel de EBEMA Click.
      */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 0,
          height: 118,
          background: 'linear-gradient(to top, rgba(6,6,9,0.86) 0%, rgba(6,6,9,0) 100%)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 26,
          display: 'flex',
          justifyContent: 'center',
        }}
      >
        <div
          style={{
            flexShrink: 0,
            whiteSpace: 'nowrap',
            backgroundColor: 'rgba(255,255,255,0.94)',
            color: P18.colores.tinta,
            fontFamily: P18.fuentes.texto,
            fontWeight: 700,
            fontSize: TEL.ancho * 0.052,
            letterSpacing: 1.6,
            textIndent: 1.6, // misma compensación de tracking que el rótulo de arriba
            padding: `${TEL.ancho * 0.026}px ${TEL.ancho * 0.062}px`,
            borderRadius: 999,
          }}
        >
          {rotulo}
        </div>
      </div>
    </div>
  </div>
);

export const P18StRecorrido: React.FC = () => {
  cargarFuentesP18();

  return (
    <AbsoluteFill style={{backgroundColor: '#0C0C10'}}>
      {/*
        ── EL FONDO ──────────────────────────────────────────────────────
        El salón real, desaturado y oscurecido. Va desaturado a propósito: si
        el fondo conserva su color compite con las dos pantallas, que son lo
        que hay que mirar. Es el mismo recurso de la referencia, donde el fondo
        fotográfico está en gris y sólo los teléfonos tienen color.
      */}
      <Img
        src={staticFile('assets/hilton/piso18/s5-fondo-recorrido.jpg')}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          /*
            ⚠️ Además de desaturado va DESENFOCADO, y no es un efecto: sin el
            desenfoque el fondo tiene copas, sillas y mesas del MISMO tamaño
            aparente que las pantallas de los teléfonos, y las dos capas se
            confunden. El desenfoque las separa en profundidad — es lo que hace
            el fondo de la referencia, que es un cielo sin detalle.
            El escalado ×2,0833 de la entrega también agranda el radio, así que
            va calculado sobre la mesa de 1080 y no sobre el máster.
          */
          filter: 'grayscale(0.88) brightness(0.44) contrast(1.04) blur(7px)',
          // el blur come el borde: se escala apenas para que no aparezca halo
          transform: 'scale(1.04)',
        }}
      />
      {/* Velo doble: arriba para el logotipo y el titular, abajo para asentar
          los teléfonos y dejar limpio el corredor del sticker. */}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(6,6,10,0.80) 0%, rgba(6,6,10,0.55) 26%, rgba(6,6,10,0.34) 48%, rgba(6,6,10,0.56) 78%, rgba(6,6,10,0.74) 100%)',
        }}
      />

      {/* El grano, sobre el fondo desenfocado y bajo los teléfonos. */}
      <GranoFondo semilla={31} />

      {/* ── Logotipo ────────────────────────────────────────────────────── */}
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
        ── El sándwich de la referencia ──────────────────────────────────
        Versales muy espaciadas arriba, titular serif grande al medio, versales
        espaciadas abajo. El gesto de las versales espaciadas no es prestado:
        es el de la línea `CENTRO DE EVENTOS` del propio logotipo.
      */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 392,
          textAlign: 'center',
          fontFamily: P18.fuentes.texto,
          fontWeight: 700,
          fontSize: 22,
          letterSpacing: 6.5,
          /*
            ⚠️ EL TRACKING DESCENTRA UNA LÍNEA CENTRADA, y es la segunda causa
            del «centra los textos» de Eli. CSS pone el `letter-spacing` DESPUÉS
            de cada letra, incluida la última: el texto queda con 6,5 px de aire
            muerto a la derecha y `text-align: center` lo reparte mal, corriendo
            la línea 3,25 px a la izquierda (7 px en la entrega a 2250).
            Se devuelve con un `text-indent` del mismo valor.
          */
          textIndent: 6.5,
          color: 'rgba(255,255,255,0.72)',
        }}
      >
        VISITA GUIADA VIRTUAL
      </div>

      <div
        style={{
          position: 'absolute',
          left: 76,
          right: 76,
          top: 452,
          textAlign: 'center',
          color: P18.colores.blanco,
          fontFamily: P18.fuentes.titular,
          textShadow: '0 2px 30px rgba(0,0,0,0.38)',
        }}
      >
        <div style={{fontSize: 74, fontWeight: 300, lineHeight: 1.1}}>¿Conocías</div>
        <div style={{fontSize: 74, fontWeight: 400, fontStyle: 'italic', lineHeight: 1.08}}>
          nuestro recorrido
        </div>
        <div style={{fontSize: 74, fontWeight: 300, lineHeight: 1.1}}>virtual?</div>
      </div>

      {/* La bajada, con las palabras del cliente. */}
      <div
        style={{
          position: 'absolute',
          left: 120,
          right: 120,
          top: 722,
          textAlign: 'center',
          fontFamily: P18.fuentes.texto,
          fontWeight: 500,
          fontSize: 30,
          lineHeight: 1.5,
          color: 'rgba(255,255,255,0.90)',
          textShadow: '0 2px 16px rgba(0,0,0,0.55)',
        }}
      >
        Recorre cada rincón de Piso18 desde donde estés.
      </div>

      {/*
        ── LOS DOS TELÉFONOS ─────────────────────────────────────────────
        Escalonados como en la referencia: el de la izquierda más abajo y
        girado al revés que el de la derecha, para que se lean como dos objetos
        apoyados y no como dos rectángulos pegados. Se superponen 34 px, que es
        lo justo para que haya profundidad sin tapar ninguna pantalla.
      */}
      <Telefono
        src="assets/hilton/piso18/s5-pantalla-b.jpg"
        x={BLOQUE_X}
        y={874}
        giro={-3.4}
        rotulo="EL SALÓN"
      />
      <Telefono
        src="assets/hilton/piso18/s5-pantalla.jpg"
        x={BLOQUE_X + TEL.ancho - SOLAPE}
        y={820}
        giro={3.0}
        rotulo="360°"
      />

      {/*
        ⬇ De y=1620 hacia abajo NO va nada. Son 300 px libres para el sticker
        de enlace a la visita virtual — que es el único llamado de esta pieza,
        por decisión del cliente de no redundar con el botón de cotización.
      */}
    </AbsoluteFill>
  );
};

/** Guía de QA: zonas seguras. El corredor de abajo es el del sticker. */
export const P18StRecorridoGuia: React.FC = () => (
  <AbsoluteFill>
    <P18StRecorrido />
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
