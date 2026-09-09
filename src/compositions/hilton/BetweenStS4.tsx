/**
 * BETWEEN — S4 · LAS DOS STORIES ESTÁTICAS DE LA SEMANA 4 (21 y 22 de septiembre)
 *
 * Las dos columnas de la hoja STORIES de la grilla
 * (`1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY`, instantánea del 09-09 en
 * `clients/hilton/grillas/between-septiembre-2026.md`):
 *
 *   col Q · 21-09 · OK PARA DISEÑAR · «ST ESTÁTICO – STRUDEL DE MANZANA»
 *   col R · 22-09 · OK PARA DISEÑAR · «ST ESTÁTICA – PRIMAVERA EN BETWEEN»
 *
 * Encargo de Eli, 09-09-2026: «Trabajaremos con los diseños de las historias
 * estáticas de la s4 de grilla […] y guíate de las referencias que adjunta
 * contenido […] **No tomes como gráficas las interacciones de contenido, solo
 * deja aire visual o espacio para que agreguen esas interacciones.**»
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LO INTERACTIVO: ZONA RESERVADA, NUNCA DIBUJADA
 * ══════════════════════════════════════════════════════════════════════════
 * Es la tercera vez que Eli lo dice (07-09, 08-09 y hoy) y ya es regla de la
 * marca: el sticker lo pone el CM al publicar, con el sticker REAL de Instagram.
 * La pieza deja la zona limpia y se entrega además una copia `GUIA CM` con la
 * zona marcada, que NO se sube al Drive.
 *
 *   21-09 → `INTERACCIÓN: Ícono "🍎"`  → 300 × 180 en y=1395
 *   22-09 → `INTERACCIÓN: LINK CARTA` → 380 × 140 en y=1300, en el CANAL
 *           IZQUIERDO: la copa ocupa el eje del cuadro de y=981 a y=1775, así
 *           que la pastilla centrada del cowork acá le caía encima al vaso
 *
 * ⚠️ Y por lo mismo, el `🍎` NO va dibujado en ninguna parte: es la interacción,
 * no un elemento gráfico. Tampoco va el `🌸` que el brief sugiere dentro del
 * titular del 22-09 — ver la nota de la pieza.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * DE DÓNDE SALE CADA FOTO, Y QUÉ ES REAL EN CADA UNA
 * ══════════════════════════════════════════════════════════════════════════
 * Las dos escenas se PRODUJERON con el método de Eli
 * (`clients/hilton/PROMPTS-DE-ELI.md`), en `scripts/between-st-s4-generar.py`.
 * Es el mismo diagnóstico de la S3: el banco de Between está pensado en 4:5 y
 * recortado a 9:16 no deja el hueco donde la diagramación lo necesita, así que
 * el texto termina apoyado en cajas. **La foto se produce con el hueco adentro.**
 *
 * · **22-09 · el milkshake es REAL.** `Between-214.jpg` de la sesión del 3 de
 *   enero (Canon EOS 5D Mark III, 1500×2250, EXIF verificado) es el milkshake
 *   del cliente: copa de vidrio con pie, borde escarchado de coco, frutilla y
 *   bombilla negra. Sólo se le CAMBIÓ EL FONDO —la pared de piedra oscura por
 *   la terraza real de Between (`espacios/_terraza-base-45.jpg` y `HDT_52.jpg`)—
 *   que es exactamente lo que el manual describe como el método de ella: «no
 *   genera escenas desde cero, EDITA la foto real».
 *
 * · ⚠️ **21-09 · el strudel es GENERADO, y hay que decirlo.** Between no tiene
 *   ninguna fotografía del Strudel de manzana: se buscó en las 202 de
 *   `3 ENERO _ PLATOS - DESAYUNOS`, en `BETWEEN DESAYUNOS AGO 2026`, en
 *   `dulces-tortas` y en la carta. Lo real que entra son el **hojaldre** y el
 *   **plato de cerámica verde oliva con anillos** de `Between-28.jpg`, que van
 *   como referencia para que la masa y la loza sean las del cliente. La regla
 *   del estudio es rotular lo generado como generado, para poder reemplazarlo
 *   el día que llegue la foto de verdad.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LOS CUADRANTES DEL 21-09 NO VAN EN EL ORDEN DEL BRIEF
 * ══════════════════════════════════════════════════════════════════════════
 * El brief numera los ingredientes (1 masa · 2 manzana · 3 canela · 4 nueces)
 * pero **no fija sus posiciones**. Se ordenaron por LUMINANCIA:
 *
 *     canela (oscura)  │  nueces (oscuras)   ← acá cae el titular beige
 *     ─────────────────┼──────────────────
 *     masa dorada      │  manzana verde
 *
 * El titular ancla en y=441 y el mosaico parte los cuadrantes en y=960, así que
 * el bloque cae ENTERO en la mitad de arriba. Con un cuadrante claro y otro
 * oscuro arriba el titular se partiría en dos legibilidades — el defecto que el
 * manual documenta en la pieza del cowork («la foto se PARTE y ninguna de las
 * dos tintas se lee en todo el ancho»). Con los dos oscuros, medido por tercios
 * de la columna: el beige da **8,2 a 12,8:1** de y=240 a y=719. Sin ninguna caja.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REJILLA (1080×1920, se entrega a 2250×4000)
 * ══════════════════════════════════════════════════════════════════════════
 *    250 ─ zona segura superior de Meta
 *    271 ─ wordmark del lockup (plantilla `storyLogoArriba` de Eli)
 *    441 ─ primera línea de tinta (`BETWEEN.bloque.yStory`)
 *   1580 ─ empieza la zona segura inferior
 *
 * Los anclajes de abajo NO son de gusto: salen de medir cada foto.
 *
 * | | 21-09 | 22-09 |
 * |---|---|---|
 * | el cuadro está libre hasta | y=737 (borde del plato) | y=790 (punta de la bombilla) |
 * | tinta que gana arriba | beige 8,2–12,8:1 | beige 8,2–14,1:1 |
 * | costuras (salto entre filas contiguas) | ninguna sobre media+6σ | ninguna sobre media+6σ |
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
import {
  Bajada,
  FotoFondo,
  LogoBetween,
  PilaDatos,
  TitularBetween,
} from './BetweenSistema';

const F = 'assets/hilton/between/s4/';

/* ══════════════════════════════════════════════════════════════════════════
   LA ZONA RESERVADA — mismo aparato que `BetweenStS3.tsx` y que el carrusel del
   cumpleaños. Sólo se pinta en la copia `GUIA CM`.
   ══════════════════════════════════════════════════════════════════════════ */
/**
 * `left` es opt-in. Por defecto la zona va CENTRADA, que es lo que hicieron el
 * carrusel del cumpleaños y las tres de la S3 — pero en la pieza del 22-09 el
 * centro del cuadro está ocupado por la copa de arriba abajo, y una pastilla de
 * enlace centrada le cae encima al vaso. Cuando el producto es alto y central,
 * el aire de la interacción está en el CANAL de un costado.
 */
type Zona = {ancho: number; alto: number; top: number; left?: number};

const ZonaReservada: React.FC<{zona: Zona; etiqueta: string}> = ({zona, etiqueta}) => (
  <div
    style={{
      position: 'absolute',
      left: zona.left ?? (1080 - zona.ancho) / 2,
      top: zona.top,
      width: zona.ancho,
      height: zona.alto,
      border: '3px dashed rgba(255,45,141,0.95)',
      borderRadius: 22,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      whiteSpace: 'pre-line',
      textAlign: 'center',
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: 700,
      fontSize: 26,
      lineHeight: 1.35,
      color: '#ff2d8d',
      background: 'rgba(255,255,255,0.10)',
    }}
  >
    {etiqueta}
  </div>
);

/** Bloque centrado en la COLUMNA de composición (810), no en el margen. */
const Columna: React.FC<{top: number; children: React.ReactNode}> = ({top, children}) => (
  <div
    style={{
      position: 'absolute',
      left: (1080 - BETWEEN.bloque.columna) / 2,
      width: BETWEEN.bloque.columna,
      top,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    }}
  >
    {children}
  </div>
);

/** Cierre en cursiva, suelto sobre la foto. Mismo componente que la S3. */
const Cierre: React.FC<{top: number; size?: number; children: React.ReactNode}> = ({
  top,
  size = 34,
  children,
}) => (
  <div
    style={{
      position: 'absolute',
      left: (1080 - BETWEEN.bloque.columna) / 2,
      width: BETWEEN.bloque.columna,
      top,
      textAlign: 'center',
      fontFamily: BETWEEN.fuentes.sans,
      fontStyle: 'italic',
      fontWeight: BETWEEN.pesos.semibold,
      fontSize: size,
      lineHeight: 1.3,
      color: BETWEEN.colores.beige,
      opacity: 0.95,
      textShadow: '0 2px 16px rgba(36,26,18,0.75)',
      whiteSpace: 'pre-line',
    }}
  >
    {children}
  </div>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 21-09 · STRUDEL DE MANZANA  (col Q · OK PARA DISEÑAR)

   Textos LITERALES de la grilla:
     · «Texto principal: CUATRO INGREDIENTES QUE SABEN MEJOR JUNTOS.»
     · «Texto complementario: Masa · Manzana · Canela · Nueces / Strudel de
       manzana.»
     · «INTERACCIÓN: Ícono "🍎"» → zona reservada, no se dibuja.

   ⭐ EL CUERPO DEL TITULAR ES 100, NO 117, y es una consecuencia MEDIDA.
   El plato arranca en y=737, así que el bloque tiene 296 px (441→737). Con el
   token de titular (117) las dos líneas de caja alta más la script dan ~314 px
   y el titular caería sobre el borde del plato. A 100 el bloque cierra antes.
   La script baja con él —`proporcionScript` 1,05— así que la jerarquía de la
   marca (script arriba, chica; caja alta abajo, protagonista) se conserva.

   ⚠️ LAS DOS LÍNEAS COMPLEMENTARIAS VAN LAS DOS EN CAJA TAUPE, y eso se aparta
   del «una sola línea fuerte por pila» del manual §1 bis. Es a propósito: bajo
   el plato los dos cuadrantes son CLAROS —L=150 a 171 medido por tercios— y el
   beige suelto ahí da 2,1:1, o sea ilegible. La regla que manda es la que el
   propio cliente escribió: «cuando no se logra visualizar los textos, puedes
   dejarlo en una caja del color café #675B49». La jerarquía se hace por ORDEN,
   no por fondo: la enumeración arriba y el nombre del producto abajo.
   ══════════════════════════════════════════════════════════════════════════ */

const ZONA_ICONO: Zona = {ancho: 300, alto: 180, top: 1395};

export const StS4Strudel: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    {/* `oscurecer` 0: los dos cuadrantes de arriba YA están en L=26–45 y el
        beige da 8,2–12,8:1. Un multiply encima sólo apagaría la canela y las
        nueces, que son el ingrediente que la pieza está mostrando. */}
    <FotoFondo src={F + 'st-21-09-strudel.jpg'} oscurecer={0} />

    <LogoBetween formato="story" posicion="arriba" tono="beige" />

    {/* ⭐ EL BLOQUE ARRANCA EN 400, NO EN 441, y son 41 px MEDIDOS.
        Con el ancla del kit el titular cerraba en y=727 y el borde del plato
        está en y=737: **10 px de aire**, que a tamaño real se lee como si la
        caja alta se apoyara en la loza. Subiéndolo, la última línea cierra en
        ~687 y quedan ~50 px, que es el orden del `aire.tituloACaja` (18) por
        dos. El precio es que el aire logo→tinta baja de los 77 px medidos en
        las plantillas de Eli a 72: una concesión de 5 px, muy por debajo de la
        que ya se aceptó en la ST del cowork (41). */}
    <Columna top={400}>
      <TitularBetween
        script="Cuatro ingredientes"
        caps={'Que saben\nmejor juntos.'}
        sizeCaps={100}
        alinear="centro"
        tono="beige"
        anchoDisponible={BETWEEN.bloque.columna}
      />
    </Columna>

    {/* Las dos líneas complementarias, bajo el plato (que cierra en y=1161). */}
    <div style={{position: 'absolute', left: 0, right: 0, top: 1215, display: 'flex', justifyContent: 'center'}}>
      <PilaDatos datos={['Masa · Manzana · Canela · Nueces', 'Strudel de manzana']} />
    </div>

    {guia ? (
      <ZonaReservada zona={ZONA_ICONO} etiqueta={'ÍCONO 🍎\n300 × 180'} />
    ) : null}
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 22-09 · PRIMAVERA EN BETWEEN  (col R · OK PARA DISEÑAR)

   Textos LITERALES de la grilla:
     · «Texto recomendado: LA PRIMAVERA SE DISFRUTA ASÍ. 🌸»
     · «Un milkshake, nuestra terraza / y una pausa al sol.»
     · «Ven a disfrutarlo en Between.»
     · «INTERACCIÓN: LINK CARTA» → zona reservada, no se dibuja.

   ⚠️ EL 🌸 DEL TITULAR NO VA, Y HAY QUE PREGUNTARLO. Between tiene exactamente
   cuatro emojis usables —`cafe`, `estrella`, `regalo` y `sonrisa`, recortados de
   la lámina 2 del carrusel aprobado por `scripts/between-emoji-extraer.py`— y no
   hay flor entre ellos. Los del sistema no sirven: en Windows Chrome resuelve
   `Segoe UI Emoji` y el ☕ sale LILA, defecto que Eli ya cazó, y Apple Color
   Emoji no se puede redistribuir. Meter una flor de otra familia le inventaría a
   la marca un quinto emoji de otro estilo. Además el brief dice «Texto
   recomendado», no obligatorio, y la versión del 27-08 también salió sin él.
   Si Eli lo quiere, basta que mande el PNG y entra en el titular.

   ⭐ Y el punto final del titular tampoco: la regla de Eli es que «los títulos
   NUNCA llevan punto final», y `sinPuntoFinal` lo saca solo (no se pasa
   `mantenerPunto`). En la bajada sí se conserva, que es texto corrido.

   MEDIDO sobre la foto: el cuadro está libre de vaso hasta y=790 (ahí arrancan
   las puntas de la bombilla, en x 575–640) y el borde de coco entra en y=867.
   El bloque de arriba cierra en ~778, o sea 12 px antes del vaso.
   ══════════════════════════════════════════════════════════════════════════ */

/**
 * ⭐ LA ZONA DEL ENLACE SE VA AL CANAL IZQUIERDO, y es medido.
 *
 * La ST del cowork del 16-09 la puso centrada, 660×140, porque ahí el centro
 * bajo era mesa limpia. Acá NO: la copa ocupa el eje del cuadro de y=981 a
 * y=1775 —el batido beige medido de corrido— y la pastilla centrada le caía
 * encima al cuenco y al pie. El canal libre está a la izquierda: de x=0 a
 * x≈330 la foto es mobiliario y follaje muy desenfocados, sin nada nítido.
 * 380×140 es el porte de un sticker de enlace con etiqueta corta.
 */
const ZONA_ENLACE: Zona = {ancho: 380, alto: 140, top: 1300, left: 80};

export const StS4Primavera: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    {/* `oscurecer` 0,03: apenas, para asentar el bokeh de las ampolletas del
        tercio de arriba sin apagar el follaje a contraluz, que es lo que hace
        que la pieza se lea «de primavera». */}
    <FotoFondo src={F + 'st-22-09-primavera.jpg'} oscurecer={0.03} />

    <LogoBetween formato="story" posicion="arriba" tono="beige" />

    <Columna top={BETWEEN.bloque.yStory}>
      <TitularBetween
        script="La primavera"
        caps="Se disfruta así."
        alinear="centro"
        tono="beige"
        anchoDisponible={BETWEEN.bloque.columna}
      />
      <Bajada
        size={40}
        tono="beige"
        style={{marginTop: BETWEEN.aire.tituloABajada, textAlign: 'center', whiteSpace: 'pre-line'}}
      >
        {'Un milkshake, nuestra terraza\ny una pausa al sol.'}
      </Bajada>
    </Columna>

    {guia ? (
      <ZonaReservada zona={ZONA_ENLACE} etiqueta={'STICKER\nDE ENLACE\n(carta)\n380 × 140'} />
    ) : null}

    {/* ⭐ EL CIERRE VA EN 1512, Y ASÍ NO PIDE NINGUNA CONCESIÓN.
        La primera pasada lo puso en 1610, que es donde lo llevan la ST del 14-09
        y el legal de la ST 2 del cumpleaños. `between-qa.py` lo marcó y tenía
        razón: la tinta caía en y=1626–1643, o sea **63 px dentro de la franja
        inferior de 340 px de Meta**. En esas dos piezas la concesión se aceptó
        porque no había otro sitio —la taza ocupaba el cuadro hasta y=1600—; acá
        sí lo hay. Medido por tercios: de y=1440 a 1559 la mesa de madera da
        **beige 6,94:1**, MEJOR que los 5,93:1 de 1560–1679, y a esa altura la
        copa es sólo la caña del pie (~90 px de vidrio translúcido), no el cuenco
        ni el borde de coco. Con la tinta en ~1531–1548 la pieza queda ENTERA
        dentro de la zona segura y además se lee mejor.
        O sea que la concesión heredada no hacía falta: era falta de medir. */}
    <Cierre top={1512} size={34}>
      Ven a disfrutarlo en Between.
    </Cierre>
  </AbsoluteFill>
);

/* Variantes «guía» — llevan dibujada la zona del sticker. NO se entregan al
   cliente ni se suben al Drive: son para el CM. Las dos piezas de la S4 llevan
   interacción, así que las dos tienen guía. */
export const StS4StrudelGuia: React.FC = () => <StS4Strudel guia />;
export const StS4PrimaveraGuia: React.FC = () => <StS4Primavera guia />;
