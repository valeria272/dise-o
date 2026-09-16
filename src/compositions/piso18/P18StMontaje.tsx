/**
 * PISO18 — HISTORIA ANIMADA · «TIMELAPSE MONTAJE» (STORIES col M · 23-09 · 18:00)
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐ RONDA 4 (16-09-2026) — **el cliente reescribió el texto en la grilla.** La
 * celda pasó a EN CAMBIOS y el brief quedó así (la columna además se corrió del
 * 23-09 al 23-09 con otra letra, es la misma pieza):
 *
 *     ST ANIMADA - TIMELAPSE MONTAJE
 *     Visual: Timelapse del montaje de un evento en Piso18, desde el salón vacío
 *     hasta completamente ambientado.
 *     Texto principal: Arreglos florales que le dan vida al matrimonio de tus
 *                      sueños en Piso18.
 *     CTA: Cotiza el tuyo en piso18.cl
 *     INTERACCIÓN: Sticker de link a cotización.
 *
 * Lo que cambió, medido por diff de conjunto contra la instantánea del 15-09
 * (`clients/hilton/grillas/api/p18-sept-20260915.json`):
 *
 * | Antes (hasta el 15-09) | Ahora |
 * |---|---|
 * | Texto principal: Así se monta un evento en Piso18, paso a paso. | Arreglos florales que le dan vida al matrimonio de tus sueños en Piso18. |
 * | Bajada: Dejando todo listo, para que solo te preocupes de celebrar. | **borrada** — el brief ya no trae bajada |
 *
 * ⚠️ El comentario *«Podría ser un texto orientado a ''Dejando todo listo, para
 * que solo te preocupes de celebrar''»* SIGUE en la celda y sin tachar. Es el
 * que había producido la bajada. Como la grilla la borró, la pieza la quita —
 * pero queda anotado dónde se repone si Eli decide lo contrario.
 *
 * ⛔ «matrimonio», nunca «bodas»: el texto nuevo ya viene correcto.
 *
 * ── El brief anterior, para el historial ─────────────────────────────────
 * Hoja STORIES, columna M, estado **OK PARA DISEÑAR**:
 *
 *     Texto principal: Así se monta un evento en Piso18, paso a paso.
 *     Bajada: Dejando todo listo, para que solo te preocupes de celebrar.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐⭐⭐ RONDA 3 — SEIS CORRECCIONES DE ELI, Y LA PIEZA CAMBIA ENTERA
 * ══════════════════════════════════════════════════════════════════════════
 * *«Me lo estás haciendo muy extraño, mucho zoom y se ve pixelado. Tienes que
 * tener cuidado con las dimensiones para que la foto no se pierda […] que al
 * inicio no aparezca ese fondo blanco. Trata de hacer más rápido esa transición.
 * Si te fijas, hace como una transición de una foto y se mueve hacia el otro lado
 * y aparece la misma foto, u otra con más montaje. Por último, trata de buscar una
 * que se vea más vacía, de manera de que se pueda ver esa transición a más
 * decoración. […] Y de, no, no coloques antes/después. Solamente de todos los
 * montajes.»*
 *
 * | Lo que pidió | Qué se hizo |
 * |---|---|
 * | Sin el fondo crema del inicio | **Abre a sangre** con el salón vacío. No hay ni un fotograma de fondo plano |
 * | Sin zoom | **Cero zoom.** La ronda 2 escalaba 1,04–1,06 dentro de cada plano; acá las fotos están quietas |
 * | Sin pixelado / cuidar dimensiones | Las fotos son **3840×5760** y se muestran a 1080×1920: **reducen a 0,28**. Ninguna se amplía |
 * | Transición de empuje lateral | El plano nuevo **entra desde la derecha** y empuja al anterior fuera por la izquierda — ver `EMPUJE` |
 * | Más rápido | El empuje dura **14 frames** (0,47 s) y cada plano **2,2 s**. Antes eran 3,5 |
 * | Una que se vea más vacía | Abre con el **VIDEO del salón sin montar** |
 *
 * ⭐ **Y «no coloques antes/después, solamente todos los montajes»:** la pieza ya
 * no rotula nada. Es una sola progresión continua de montajes, del espacio vacío
 * al salón terminado, sin etiquetas.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⛔ LA TRAMPA DEL VIDEO — rotación por metadato
 * ══════════════════════════════════════════════════════════════════════════
 * `IMG_4177.MOV` **se declara 3840×2160 en el stream y es 2160×3840 al decodificar**:
 * trae rotación por metadato, como todo `.MOV` de iPhone. Por creerle al stream se
 * recortó tres veces una franja vertical que mostraba techo y cortinas y nada de
 * piso. **Ya es 9:16 exacto: sólo hay que escalarlo, no recortarlo.**
 *
 * Y es HDR HLG (`bt2020nc/arib-std-b67`), así que necesita **tonemap** o sale
 * lavado — el mismo modo de falla del metraje de dron de Tierra Calma.
 *
 * El comando que lo deja listo (3 s del tramo donde entra el sol al piso):
 *
 *     ffmpeg -ss 9.4 -t 3.0 -i IMG_4177.MOV \
 *       -vf "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,\
 *            tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,\
 *            format=yuv420p,scale=1080:1920" \
 *       -r 30 -c:v libx264 -crf 17 -preset slow -an salon-vacio.mp4
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LOS CINCO PLANOS — una sola progresión, de vacío a montado
 * ══════════════════════════════════════════════════════════════════════════
 * Las cuatro fotos salen de **`Piso 18_28 ago decoración 2024`**, la sesión que
 * Eli mandó usar para todo lo de flores. Nada de IA.
 *
 *   1. `salon-vacio.mp4`  el salón SIN MONTAR: piso desnudo, mesas altas sueltas
 *   2. `piso_18-90`       entran las mesas de madera y los primeros arreglos
 *   3. `piso_18-128`      más arreglos, y al fondo las mesas ya vestidas
 *   4. `piso_18-72`       la mesa larga montada, con el follaje colgante
 *   5. `piso_18-153`      el salón terminado — y el fondo del cierre
 *
 * ⚠️ Ninguna de las cinco tiene rostros ni el logotipo de la pared, que es lo que
 * Eli pidió cuidar. El titular además vive **abajo**, sobre su propio velo.
 *
 * ⚠️ Zonas seguras de Instagram: el titular ocupa y 1244–1432 y el bloque del
 * cierre y 812–1394. Nada entra en los 250 de arriba ni en los 340 de abajo.
 */
import React from 'react';
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  OffthreadVideo,
  staticFile,
  useCurrentFrame,
} from 'remotion';
import {P18, cargarFuentesP18} from '../../brand/piso18';

export const P18_MONTAJE_FPS = 30;

const W = 1080;
const H = 1920;

/** ⚠️ 390 frames = **13 s**. El tope que fijó Eli es 15, y la ronda 2 duraba 14. */
export const P18_MONTAJE_DUR = 390;

/** Cuánto dura el empuje de una foto a la siguiente. 14 frames = 0,47 s. */
const EMPUJE = 14;

/** Dónde entra cada plano, en frames. */
const ENTRADA = [0, 84, 150, 216, 282] as const;
/** Cuándo arranca el bloque de cierre (sobre el último plano). */
const CIERRE = 282;

const suave = Easing.bezier(0.3, 0.72, 0.28, 1);

/**
 * El desplazamiento horizontal de un plano, en px, para el frame dado.
 *
 * ⭐ Es LA transición que pidió Eli: *«hace como una transición de una foto y se
 * mueve hacia el otro lado y aparece […] otra con más montaje»*. El plano entra
 * desde la derecha y, cuando entra el siguiente, sale hacia la izquierda — pero
 * **más lento que el que entra** (sale 0,3 del ancho, no 1,0), que es lo que le
 * da profundidad en vez de parecer un pase de diapositivas.
 */
const desplazamiento = (f: number, indice: number) => {
  const entra = ENTRADA[indice];
  const siguiente = ENTRADA[indice + 1];
  // Todavía no le toca: fuera por la derecha.
  if (f < entra) return W;
  // ⛔ El PRIMER plano no entra empujando: **ya está en pantalla en el frame 0**.
  // Si entra como los demás, el primer fotograma de la historia es medio negro —
  // y ese fotograma es la miniatura que ve todo el mundo antes de tocar play.
  const x =
    indice === 0
      ? 0
      : interpolate(f, [entra, entra + EMPUJE], [W, 0], {
          extrapolateRight: 'clamp',
          easing: suave,
        });
  if (siguiente === undefined) return x;
  // Ya entró el siguiente: arrastre hacia la izquierda.
  const salida = interpolate(f, [siguiente, siguiente + EMPUJE], [0, -W * 0.3], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: suave,
  });
  return f < siguiente ? x : salida;
};

/** Un plano: ocupa la pantalla entera y se mueve en bloque. Sin zoom. */
const Plano: React.FC<{indice: number; children: React.ReactNode}> = ({indice, children}) => {
  const f = useCurrentFrame();
  const x = desplazamiento(f, indice);
  const siguiente = ENTRADA[indice + 1];
  // Se apaga cuando ya salió del todo, para no apilar capas.
  const vivo = siguiente === undefined || f < siguiente + EMPUJE + 2;
  if (!vivo || f < ENTRADA[indice] - 1) return null;
  return (
    <AbsoluteFill style={{transform: `translateX(${x}px)`}}>
      <AbsoluteFill style={{overflow: 'hidden', backgroundColor: '#0B0B0D'}}>{children}</AbsoluteFill>
    </AbsoluteFill>
  );
};

/** Una foto a sangre. `objectPosition` es lo único que encuadra — no hay escala. */
const Foto: React.FC<{src: string; pos: string}> = ({src, pos}) => (
  <Img
    src={staticFile(src)}
    style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: pos}}
  />
);

export const P18StMontaje: React.FC = () => {
  cargarFuentesP18();
  const f = useCurrentFrame();

  // El titular acompaña los tres primeros planos y se va antes del cierre.
  const titular = interpolate(f, [16, 40, CIERRE - 34, CIERRE - 12], [0, 1, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  // El logotipo de cabecera vive hasta que entra el cierre, que trae el suyo.
  const logoArriba = interpolate(f, [8, 26, CIERRE - 20, CIERRE], [0, 1, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  // El cierre entra sobre el último plano, que ya está en pantalla.
  const cierre = interpolate(f, [CIERRE + 10, CIERRE + 34], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: suave,
  });
  const sube = interpolate(cierre, [0, 1], [22, 0]);

  return (
    <AbsoluteFill style={{backgroundColor: '#0B0B0D'}}>
      {/* ── LOS CINCO PLANOS, en orden inverso para que el nuevo quede encima ── */}
      <Plano indice={4}>
        <Foto src="assets/hilton/piso18/mt-153.jpg" pos="center 52%" />
      </Plano>
      <Plano indice={3}>
        <Foto src="assets/hilton/piso18/mt-72.jpg" pos="center 55%" />
      </Plano>
      <Plano indice={2}>
        <Foto src="assets/hilton/piso18/mt-128.jpg" pos="center 50%" />
      </Plano>
      <Plano indice={1}>
        <Foto src="assets/hilton/piso18/mt-90.jpg" pos="center 50%" />
      </Plano>
      <Plano indice={0}>
        <OffthreadVideo
          src={staticFile('assets/hilton/piso18/salon-vacio.mp4')}
          style={{width: '100%', height: '100%', objectFit: 'cover'}}
          muted
        />
      </Plano>

      {/*
        ── Velos ────────────────────────────────────────────────────────
        Arriba para el logotipo, abajo para el titular. Van FUERA de los planos
        para que no se desplacen con ellos: si viajaran, el texto quedaría un
        instante sin fondo en cada empuje.
      */}
      <AbsoluteFill
        style={{
          pointerEvents: 'none',
          background:
            'linear-gradient(to bottom, rgba(0,0,0,0.46) 0%, rgba(0,0,0,0.12) 20%, rgba(0,0,0,0) 34%, rgba(0,0,0,0) 56%, rgba(0,0,0,0.30) 76%, rgba(0,0,0,0.66) 100%)',
          opacity: cierre > 0.5 ? 1 - cierre : 1,
        }}
      />

      {/* ── Logotipo de cabecera ───────────────────────────────────────── */}
      <Img
        src={staticFile('assets/hilton/piso18/logo.png')}
        style={{
          position: 'absolute',
          width: P18.geometria.logoAncho,
          height: P18.geometria.logoAncho / P18.geometria.logoProporcion,
          left: (W - P18.geometria.logoAncho) / 2,
          top: P18.geometria.logoYStory,
          opacity: logoArriba,
        }}
      />

      {/*
        ── El titular, abajo y sobre su velo ────────────────────────────
        Verbatim del brief. Va abajo —no encima de la foto— porque es donde el
        velo lo sostiene sobre los cinco planos sin tapar el montaje, que es lo
        que la pieza tiene que mostrar.
      */}
      <div
        style={{
          position: 'absolute',
          left: 96,
          right: 96,
          top: 1244,
          textAlign: 'center',
          opacity: titular,
          color: P18.colores.blanco,
          fontFamily: P18.fuentes.titular,
          fontWeight: 300,
          fontSize: 62,
          lineHeight: 1.18,
          textShadow: '0 2px 26px rgba(0,0,0,0.42)',
        }}
      >
        <span style={{fontStyle: 'italic', fontWeight: 400}}>Arreglos florales</span>{' '}
        que le dan vida al matrimonio de tus sueños en Piso18.
      </div>

      {/* ── CIERRE de marca, sobre el último montaje ───────────────────── */}
      <AbsoluteFill style={{opacity: cierre, pointerEvents: 'none'}}>
        <AbsoluteFill style={{backgroundColor: 'rgba(10,9,8,0.72)'}} />
        <div style={{transform: `translateY(${sube}px)`}}>
          <Img
            src={staticFile('assets/hilton/piso18/logo.png')}
            style={{
              position: 'absolute',
              width: 472,
              height: 472 / P18.geometria.logoProporcion,
              left: (W - 472) / 2,
              top: 812,
            }}
          />
          {/*
            ⛔ Acá vivía la bajada «Dejando todo listo, para que solo te preocupes
            de celebrar.» La RONDA 4 la quita porque **la grilla la borró**: el
            16-09 el cliente reemplazó las dos líneas del brief (texto principal
            + bajada) por una sola. El comentario que la propuso sigue en la
            celda sin tachar, así que si Eli la quiere de vuelta se repone acá y
            el botón baja otra vez a 1244.
          */}
          <div
            style={{
              position: 'absolute',
              left: 0,
              right: 0,
              top: 1100,
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
    </AbsoluteFill>
  );
};

/**
 * Guía de QA: las dos zonas seguras de Instagram sobre la pieza animada.
 * ⚠️ En una pieza animada el botón se mide en el **ÚLTIMO fotograma**, no en el
 * primero — esta guía se mira ahí, con `--frame`.
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
          top: H - P18.seguras.story.abajo,
          bottom: 0,
          background: 'rgba(255,0,0,0.22)',
          borderTop: '2px solid red',
        }}
      />
    </AbsoluteFill>
  </AbsoluteFill>
);
