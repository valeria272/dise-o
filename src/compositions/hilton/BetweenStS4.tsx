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
 *   22-09 → `INTERACCIÓN: LINK CARTA` → 300 × 140 en y=1020, en el CANAL
 *           IZQUIERDO: la copa ocupa el eje del cuadro de y=860 a y=1560, así
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
 * · **22-09 · el milkshake es REAL, y es EL de Between.** Sale de la sesión del
 *   producto que mandó Eli el 09-09 (`raw/hilton/between/milkshakes-jun2025/`,
 *   35 fotos de Ámbar Gallardo del 30-06-2025, iPhone 4284×5712): copa alta
 *   ACANALADA con PIE ESCALONADO, batido de moras, brocheta con dos moras y una
 *   frambuesa, sin bombilla. La ronda 1 usó `Between-214.jpg` de la sesión del
 *   3 de enero —real, pero **otro producto**— y por eso se cayó entera.
 *   Se le cambió el entorno: de la barra a la TERRAZA real del local
 *   (`espacios/_terraza-base-45.jpg` y `HDT_52.jpg`), que es lo que el manual
 *   describe como el método de ella: «no genera escenas desde cero, EDITA la
 *   foto real».
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
 * | el cuadro está libre hasta | y≈717 (borde del plato) | y=860 (la brocheta de moras) |
 * | tinta que gana arriba | beige 8,2–12,8:1 | beige 14,6–15,7:1 |
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
import {Ilustra} from './BetweenRecursos';

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

/**
 * Cierre en cursiva. A diferencia del de `BetweenStS3.tsx`, este NO va
 * posicionado en absoluto al pie: va como último hijo de la `Columna`, porque en
 * esta pieza el sitio libre está ARRIBA y no abajo. Ver la nota del 22-09.
 */
const Cierre: React.FC<{size?: number; style?: React.CSSProperties; children: React.ReactNode}> = ({
  size = 34,
  style,
  children,
}) => (
  <div
    style={{
      width: BETWEEN.bloque.columna,
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
      ...style,
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
        está en y≈717: la caja alta se apoyaba en la loza. Subiéndolo, la última
        línea cierra en **686** y el azúcar flor del strudel entra en **721**, o
        sea **35 px de aire** — medido sobre la pieza ENTREGADA, a 2250: la
        tinta del titular termina en y=1430 y el bloque siguiente arranca en
        1503. Es el orden del `aire.tituloACaja` (18) por dos.
        El precio es el aire logo→tinta: la tinta arranca en 403 y el lockup
        completo —wordmark + «COFFEE & BAR»— cierra en y=364, así que quedan
        **39 px** contra los 77 que miden las plantillas de Eli. Es exactamente
        la concesión que ya se aceptó en la ST del cowork (41 px), y por el
        mismo motivo: entre respetar el token de aire y que el titular no se
        apoye en la loza, gana que no se apoye.
        ⚠️ Ojo con medir esto: el bloque de tinta del lockup que devuelve un
        umbral de beige es sólo el WORDMARK (271–330). La bajada «COFFEE & BAR»
        es más fina y no pasa el umbral, así que si se mide contra 330 el aire
        parece 72 px y no lo es. El valor bueno sale de la plantilla:
        `bajadaY 348 + bajadaAlto 16 = 364`. */}
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

   ⛔⛔ RONDA 2 (09-09) — EL PRODUCTO DE LA RONDA 1 NO ERA UN MILKSHAKE DE
   BETWEEN. Eli mandó la sesión del producto («te dejo acá la sesión que tenemos
   de cómo son») y con eso cayó la pieza entera: el milkshake del cliente va en
   una copa ACANALADA con PIE ESCALONADO, sin bombilla y sin borde escarchado, y
   se adorna con una BROCHETA de moras y una frambuesa. Se eligió el de moras
   —`IMG_3607` de `raw/hilton/between/milkshakes-jun2025/`— porque el morado es
   el que más lee «primavera» contra el verde y porque separa esta pieza de la
   del 21-09, que es toda marrón y verde manzana. El detalle completo, con la
   tabla de lo que estaba mal, está en `scripts/between-st-s4-generar.py`.

   MEDIDO sobre la foto nueva: aislando el batido morado por color, el cuadro
   está **libre de copa hasta y=860** (ahí entra la brocheta con las moras), así
   que el bloque de arriba, que cierra en ~778, deja **82 px de aire**. Y el
   contraste del beige en la banda del titular subió a **14,6–15,7:1** (era
   8,2–14,1 en la ronda 1): el fondo nuevo es follaje profundo a contraluz, no
   bokeh claro con lona de quitasol.
   ══════════════════════════════════════════════════════════════════════════ */

/**
 * ⭐ LA ZONA DEL ENLACE SE VA AL CANAL IZQUIERDO, y es medido.
 *
 * La ST del cowork del 16-09 la puso centrada, 660×140, porque ahí el centro
 * bajo era mesa limpia. Acá NO: aislando el batido morado por color, la copa
 * ocupa el eje del cuadro de y=860 a y=1560 y su borde izquierdo nunca pasa de
 * x=360, así que una pastilla centrada le caería encima. El canal libre está a
 * la izquierda —de x=0 a x≈355 la foto es mesa y follaje muy desenfocados— y en
 * la franja y=1020–1160 el borde de la copa está en x≈374, o sea que una zona
 * de 300 px que cierra en x=350 deja 24 px de aire.
 */
const ZONA_ENLACE: Zona = {ancho: 300, alto: 140, top: 1020, left: 50};

export const StS4Primavera: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    {/* `oscurecer` 0,03: apenas, para asentar el bokeh de las ampolletas del
        tercio de arriba sin apagar el follaje a contraluz, que es lo que hace
        que la pieza se lea «de primavera». */}
    <FotoFondo src={F + 'st-22-09-primavera.jpg'} oscurecer={0.03} />

    <LogoBetween formato="story" posicion="arriba" tono="beige" />

    {/* ⭐ EL CONTENEDOR VUELVE A 441, Y EL MOTIVO ES LA TIPOGRAFÍA.
        `BETWEEN.bloque.yStory` (441) es la primera línea de TINTA, no el borde
        del contenedor, y el desfase entre las dos cosas depende de la FUENTE:
          · con Brushwell (rondas 1 y 2) el acompañamiento traía un hueco de
            ascendente de 39 px, así que el contenedor tenía que ir en 402 para
            que la tinta cayera en 441;
          · con el acompañamiento en Raleway y en CAJA ALTA —lo que pidió Eli en
            la ronda 3— ese hueco desaparece: la tinta arranca donde arranca el
            contenedor.
        Medido en los dos casos, el aire bajo el lockup queda en los 77 px de
        sus plantillas (el lockup completo —wordmark + «COFFEE & BAR»— cierra en
        y=364). ⚠️ O sea que el ancla NO se copia entre piezas si cambia la
        fuente del acompañamiento: se rinde y se mide la tinta. */}
    <Columna top={BETWEEN.bloque.yStory}>
      {/* ⭐ RONDA 3 (09-09) — Eli: «los títulos que sean en raleway semi bold».
          Dos cambios en una frase, y los dos van con la gramática que la marca
          ya tiene escrita:
            · `scriptSans` pasa el acompañamiento de Brushwell a Raleway. Es el
              mismo recurso que ella pidió el 01-09 para las slides interiores
              del Cowork («que sea de la familia de raleway»), así que la script
              queda como marca de PORTADA y esta historia va a un solo alfabeto.
            · `pesoCaps` 600 baja la caja alta del ExtraBold de siempre a
              SemiBold. Es opt-in a propósito: el 800 está calibrado con el
              tracking y los anchos de cifra del kit, y moverlo por defecto
              re-flujaría toda pieza aprobada.
          ⚠️ SemiBold es más angosto, así que `ajustarACaber` sube el cuerpo
          dentro de la misma columna de 810: la línea pesa menos pero ocupa
          igual, y la jerarquía la sostiene el TAMAÑO. */}
      <TitularBetween
        script="La primavera"
        caps="Se disfruta así."
        scriptSans
        pesoCaps={600}
        alinear="centro"
        tono="beige"
        anchoDisponible={BETWEEN.bloque.columna}
      />
      {/* «segundo texto añádele un poco más de grosor»: Regular (400) → Medium
          (500). Un paso, no dos: con el titular en SemiBold (600), 500 mantiene
          el salto de peso entre título y párrafo, y 600 los igualaría. */}
      <Bajada
        size={40}
        tono="beige"
        style={{
          marginTop: BETWEEN.aire.tituloABajada,
          textAlign: 'center',
          whiteSpace: 'pre-line',
          fontWeight: 500,
        }}
      >
        {'Un milkshake, nuestra terraza\ny una pausa al sol.'}
      </Bajada>
      {/* ⭐ EL CIERRE ENTRA AL BLOQUE DE ARRIBA, no al pie.
          Primero fue al pie en y=1512, que es donde la ST del 14-09 lleva el
          suyo. Pero en esa pieza el pie es sweater liso: acá la copa ocupa el
          eje del cuadro de y=860 a y=1560, así que el cierre caía ENCIMA del
          producto — y la regla de la marca es que el garabato y el texto se
          apoyan en el fondo, nunca sobre el producto ni sobre quien lo
          sostiene. Arriba sí hay sitio medido: la tinta del bloque cierra en
          ~830 y la brocheta de moras entra en y=860, o sea 30 px de aire.
          De paso la franja de abajo queda de pura fotografía, que es lo que
          hace la ST del cowork del 16-09. */}
      {/* ⭐ RONDA 3 — «el último que sea más abajo estilo un poco más grande, no
          se lee bien». Las dos cosas son la misma: la bajada estaba a 34 px y a
          20 px del párrafo, o sea pegada y más chica que él, y así no se leía
          como tercer nivel — se leía como una nota al pie del párrafo.
          Sube a 38 px y el aire sobre ella pasa de 20 a 44: el salto ENTRE
          niveles queda mayor que el salto DENTRO del párrafo (interlínea ~56 a
          40 px de cuerpo), que es la regla de jerarquía del manual.
          El sitio para bajarla sale de que el titular ahora es SemiBold en
          Raleway y no Brushwell: el acompañamiento en caja alta es más bajo que
          la script y libera ~24 px de alto de bloque. */}
      <Cierre
        style={{marginTop: 44}}
        size={38}
      >
        Ven a disfrutarlo en Between.
      </Cierre>
    </Columna>

    {/* ⭐ SOL Y NUBES — «la referencia de la ST tenía líneas de dibujo como BW,
        debes añadir sol y nubes como ilustración». Dibujados con su mano en
        `scripts/between-trazos-sol-nubes.py` (ver la nota de `ILUSTRACIONES`).

        Las tres posiciones salen de la silueta MEDIDA de la copa —el batido
        morado ocupa x 360–730 de y=860 a y=1560— y de las dos franjas que el
        texto y el sticker ya ocupan. Ninguno toca el producto: la regla de la
        marca es que el repertorio de línea se apoya en el FONDO.
          · el sol arriba a la izquierda, como en la referencia, cerrando en
            y=432 (la primera tinta del titular entra en 441);
          · la nube grande a la derecha del vaso, sobre el follaje oscuro
            (L=82 medido, o sea que el trazo beige se lee);
          · la nube chica abajo a la izquierda, en y=1400–1536, que es más
            oscuro que la franja de 1200 (L=67 contra L=143) y queda dentro de
            la zona segura.
        Los TAMAÑOS también son el hueco que hay, no un gusto. Medida la tinta
        del texto sobre el render: la script entra en y=441 y su primera letra
        en x=238, así que en la esquina de arriba a la izquierda caben 185 px
        de sol y ni uno más — y el sol es el único que se deja ENTERO, porque
        es el que está pegado a la franja donde Instagram pone su interfaz.

        ⭐ LAS NUBES SANGRAN POR EL BORDE, y eso lo dice la referencia: sus dos
        nubes tienen bbox `x 0–192` y `x 736–1079`, o sea que las DOS se salen
        del cuadro. Es lo que les permite leerse grandes sin apretar la pieza.
        Acá van a 330 y 300 px saliéndose 80 y 58 px por su lado, contra los
        260 y 250 que caben enteras — con las mismas medidas de la referencia
        (192 y 342 normalizados a 1080).
        `opacidad` 0,85–0,9: la regla de uso de Eli es que las ilustraciones
        «acompañan, no dominan». */}
    <Ilustra cual="sol" x={50} y={248} ancho={185} opacidad={0.9} />
    <Ilustra cual="nube" x={828} y={876} ancho={330} opacidad={0.88} />
    <Ilustra cual="nubeChica" x={-58} y={1330} ancho={300} opacidad={0.85} />

    {guia ? (
      <ZonaReservada zona={ZONA_ENLACE} etiqueta={'STICKER\nDE ENLACE\n(carta)\n300 × 140'} />
    ) : null}

    {/* ⚠️ La franja de abajo queda de PURA FOTOGRAFÍA, a propósito: el cierre se
        subió al bloque de arriba (ver la nota ahí) y así la copa se ve entera,
        sin nada encima. Es lo mismo que hace la ST del cowork del 16-09. */}
  </AbsoluteFill>
);

/* Variantes «guía» — llevan dibujada la zona del sticker. NO se entregan al
   cliente ni se suben al Drive: son para el CM. Las dos piezas de la S4 llevan
   interacción, así que las dos tienen guía. */
export const StS4StrudelGuia: React.FC = () => <StS4Strudel guia />;
export const StS4PrimaveraGuia: React.FC = () => <StS4Primavera guia />;
