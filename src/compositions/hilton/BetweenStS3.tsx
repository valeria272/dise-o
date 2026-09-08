/**
 * BETWEEN — S3 · LAS TRES STORIES DE LA SEMANA 3 (14, 16 y 18 de septiembre)
 *
 * Pedido de Eli, 08-09-2026: «Trabajaremos en la grilla S3 de between […]
 * recuerda guiarte del brief, dejar espacio para lo que contenido deba hacer de
 * botón o interacción. Que eso no va diseñado solo se deja aire de espacio
 * libre. Necesito que te guíes de las referencias de pinterest de grilla pero
 * ligado siempre a la marca de Between.»
 *
 * Las tres columnas de la hoja STORIES de la grilla
 * (`1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY`, instantánea del 08-09 en
 * `clients/hilton/grillas/between-septiembre-2026.md`):
 *
 *   col M · 14-09 · OK PARA DISEÑAR · «ST INTERACTIVA – ¿CUÁNDO ES HORA DE CAFÉ?»
 *   col N · 16-09 · CORREGIDO       · «ST ESTÁTICA – COWORK | YA ABRIMOS»
 *   col O · 18-09 · OK PARA DISEÑAR · «ST ESTÁTICA - SALUDO 18 SEPT»
 *
 * ⚠️ ESTAS TRES YA EXISTÍAN Y SE REHACEN DE CERO, A PROPÓSITO.
 * `StHoraCafe`, `StCowork` y `StDieciocho` de `BetweenSeptiembre.tsx` son del
 * set del 31-08 y están entre las **8 historias que ya no se pueden rehacer**
 * porque sus fotos de origen no existen en ningún disco (ver
 * `clients/hilton/CLAUDE.md` § «8 historias de septiembre YA NO SE PUEDEN
 * REHACER»). No se editan: se rehacen. Y hacía falta rehacerlas, porque el mes
 * cambió de sistema por completo entre el 31-08 y el 07-09 — 25 rondas — y esas
 * tres arrastraban tres defectos que hoy son reglas escritas:
 *
 *   1. la del 14-09 llevaba una modelo de la sesión de julio 2023 con la CARA
 *      enfocada, y el cliente pidió el 08-09 «modificar el aspecto de estas
 *      modelos, ya no las podemos usar tal cual»;
 *   2. las tres DIBUJABAN el sticker de Instagram, y desde el 07-09 lo
 *      interactivo va como **zona reservada** (decisión de Eli: «un sticker
 *      dibujado se ve interactivo y no lo es: nadie vota»);
 *   3. la del 16-09 mostraba el local VACÍO y enfocado, que es justo lo que
 *      dispara el comentario abierto del cliente («se puede entender que
 *      estuvimos cerrados»).
 *
 * ── DE DÓNDE SALE CADA FOTO ──────────────────────────────────────────────
 * Las tres son FOTO REAL del banco de la marca, subida a 2× con el upscaler de
 * Freepik y recortada a 9:16 por `scripts/between-st-s3-fotos.py`. Ninguna se
 * generó y ninguna se amplió: las tres salen REDUCIENDO desde la fuente a 2×
 * (×0,90 · ×0,83 · ×1,00). Ver la cabecera de ese script para el por qué del 2×.
 *
 *   14-09 → `mesa-cafe-2piso.jpg`      capuchino en la mesa del lounge
 *   16-09 → `cowork-terraza.jpg`       mesa de la terraza con notebook y café
 *   18-09 → `desayuno-completo-2.jpg`  desayuno para compartir · **KIMBO borrado**
 *
 * Las tres estaban SIN USAR en el mes: ninguna de las 27 piezas de septiembre
 * las ocupa. Se revisó contra `BetweenSeptiembre.tsx` para no repetir foto
 * dentro del mismo mes.
 *
 * ── LAS REFERENCIAS DE PINTEREST, Y QUÉ SE TOMÓ DE CADA UNA ──────────────
 * Los tres enlaces vienen en la propia grilla. No se copian: se traduce su
 * ESTRUCTURA a la gramática de Between (`clients/hilton/CLAUDE.md`
 * § LA GRAMÁTICA MEDIDA), que es lo que pidió Eli — «ligado siempre a la marca».
 *
 *   14-09 · pin 7740630606902519 — manos con una taza abajo, la pregunta en una
 *           tarjeta clara arriba y una línea de cierre chica al pie.
 *           → Between: la pregunta va como titular (script + caja alta), la taza
 *             es héroe en el tercio medio y las alternativas NO se dibujan: son
 *             la zona reservada. El «cierre» del brief entra como bajada, porque
 *             el pie de esta pieza lo ocupa el sticker.
 *   16-09 · pin 1103804189956827376 — antetítulo espaciado, titular enorme en dos
 *           líneas, foto de mesa con notebook y café al medio, y el HORARIO en
 *           bloques al pie.
 *           → Between: antetítulo = la script Brushwell; titular en caja alta;
 *             el horario en caja taupe, que es el bloque de dato de la marca.
 *   18-09 · pin 1011550766329396269 — un PANEL de color sobre la foto del local,
 *           con todo el texto adentro.
 *           → Between: el panel es la caja taupe `#675B49`, que es exactamente el
 *             mecanismo que el cliente autorizó por escrito («cuando no se logra
 *             visualizar los textos, puedes dejarlo en una caja del color café
 *             #675B49»). Sin él esta foto no admite un párrafo de 93 caracteres:
 *             medida por franjas, sólo y=240–560 está calma.
 *
 * ── LO INTERACTIVO: ZONA RESERVADA, NUNCA DIBUJADA ───────────────────────
 * Orden de Eli del 07-09 y repetida el 08-09. El sticker real lo pone el CM al
 * publicar. Acá se deja el hueco, del porte correcto, y se entrega además una
 * copia `GUIA CM` con la zona marcada — que **no se sube al Drive ni se manda al
 * cliente**, igual que en las dos stories del cumpleaños.
 *
 *   14-09 → QUIZ de 4 alternativas  · 660 × 300
 *   16-09 → sticker de ENLACE (carta) · 660 × 140
 *   18-09 → la grilla no pide interacción → no lleva zona reservada
 *
 * ── LA REJILLA (1080×1920, se entrega a 2250×4000) ───────────────────────
 * Zona segura de Meta: nada de contenido sobre y=250 ni bajo y=1580
 * (regla global `paid-media-zonas-seguras`).
 *    250 ─ zona segura superior
 *    271 ─ wordmark del lockup (plantilla `storyLogoArriba` de Eli)
 *    441 ─ primera línea de tinta del bloque de texto (`BETWEEN.bloque.yStory`,
 *          medido: deja los 77 px de aire logo→texto de sus plantillas)
 *   1580 ─ empieza la zona segura inferior
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
import {
  CajaDato,
  FotoFondo,
  LegalAlPie,
  LogoBetween,
  PanelTaupe,
  TitularBetween,
} from './BetweenSistema';

const F = 'assets/hilton/between/st-s3/';

/* ══════════════════════════════════════════════════════════════════════════
   LA ZONA RESERVADA

   Mismo aparato que `BetweenStCumpleCarrusel.tsx`, con el alto por pieza: un
   quiz de cuatro alternativas no ocupa lo mismo que una pastilla de enlace.
   Las medidas salen de `StickerQuiz` y `StickerEnlace` de `BetweenRecursos.tsx`,
   que están calibrados contra los stickers reales de Instagram.
   ══════════════════════════════════════════════════════════════════════════ */
type Zona = {ancho: number; alto: number; top: number};

const ZonaReservada: React.FC<{zona: Zona; etiqueta: string}> = ({zona, etiqueta}) => (
  <div
    style={{
      position: 'absolute',
      left: (1080 - zona.ancho) / 2,
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

/**
 * Pila de cajas taupe con UN SOLO BORDE DERECHO.
 *
 * Regla del manual § «1 bis. Una pila de cajas va toda del MISMO ANCHO», que
 * salió del «se ve todo desordenado en los textos y no se ve pulcro» de Eli: el
 * desorden no eran los dígitos, era la ESCALERA de tres anchos distintos.
 * `PilaEsquina` lo resuelve con `igualarAncho`; acá se hace igual y sin medir en
 * JS: el contenedor es `inline-flex` —así se encoge al ancho de la caja más
 * ancha— y los hijos van `stretch`, o sea que la más angosta crece hasta ese
 * mismo borde. `CajaDato` y `PanelTaupe` ya centran su texto, así que estirarlas
 * no descuadra nada.
 */
const PilaIgualada: React.FC<{children: React.ReactNode; top?: number}> = ({children, top}) => (
  <div
    style={{
      display: 'inline-flex',
      flexDirection: 'column',
      alignItems: 'stretch',
      gap: BETWEEN.cajas.gap,
      marginTop: top,
    }}
  >
    {children}
  </div>
);

/** Bloque de texto centrado en la COLUMNA de composición (810), no en el margen. */
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

/* ══════════════════════════════════════════════════════════════════════════
   ST 14-09 · ¿CUÁNDO ES HORA DE CAFÉ?  (col M · OK PARA DISEÑAR)

   Textos LITERALES de la grilla. El brief separa tres cosas y sólo dos van
   diseñadas:
     · «Texto» → el titular.
     · «Cierre» → la bajada.
     · «Respuesta correcta: Obviamente, D. Todo el día.» → NO va en la pieza:
       es la respuesta que el CM marca dentro del sticker de quiz. Dibujarla
       reventaría el juego.

   POR QUÉ LA BAJADA VA ARRIBA Y NO AL PIE, como en la referencia:
   medida la foto por franjas (script `hoja-contacto` + perfil de desvío
   estándar), la taza y el platillo ocupan y=850–1400 y la madera limpia arranca
   en 1400 — o sea que bajo la taza quedan 180 px antes de la zona segura, y ahí
   no cabe un quiz de cuatro alternativas. El pie es del sticker; el texto sube.
   ══════════════════════════════════════════════════════════════════════════ */

/* top 1280 y no 1240: la zona CIERRA justo en 1580, donde arranca la franja
   inferior de Meta, y así se corre 40 px hacia abajo el borde de arriba — que en
   1240 caía sobre el platillo de la taza. Medido: la taza con su platillo ocupa
   y=850–1400, y el rosetón de la leche termina en 1190, o sea que en 1280 el
   sticker no tapa nada de lo que hace bonita la foto. */
const ZONA_QUIZ: Zona = {ancho: 660, alto: 300, top: 1280};

export const StS3HoraCafe: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: '#241a12'}}>
    {/* 0,10 y no el 0,28 por defecto: la franja del titular ya está en L=45 de
        255 (sillones del lounge desenfocados) y el manual prohíbe apagar la foto
        para que se lea un texto. Lo mínimo que asiente los negros. */}
    <FotoFondo src={F + 'st-14-09-hora-cafe.jpg'} oscurecer={0.1} />

    <LogoBetween formato="story" posicion="arriba" tono="beige" />

    <Columna top={BETWEEN.bloque.yStory}>
      {/* «es…» lleva el carácter … (U+2026) y no tres puntos: así `sinPuntoFinal`
          —que borra /\.+$/— no se lo come, y la elipsis es parte de la pregunta,
          no un punto de titular. */}
      <TitularBetween
        script="El mejor momento"
        caps="Para un café es…"
        alinear="centro"
        tono="beige"
        anchoDisponible={BETWEEN.bloque.columna}
        mantenerPunto
      />
    </Columna>

    {/* El cierre del brief, literal. En cursiva y sobre el sillón oscuro, que es
        la única superficie calma que queda antes de la taza. El salto de línea
        es a mano para no dejar viuda: «esperándote en Between.» sola sería una
        línea de una palabra y media. */}
    <div
      style={{
        position: 'absolute',
        left: (1080 - BETWEEN.bloque.columna) / 2,
        width: BETWEEN.bloque.columna,
        top: 700,
        textAlign: 'center',
        fontFamily: BETWEEN.fuentes.sans,
        fontStyle: 'italic',
        fontWeight: BETWEEN.pesos.semibold,
        fontSize: 36,
        lineHeight: 1.32,
        color: BETWEEN.colores.beige,
        opacity: 0.95,
        textShadow: '0 2px 16px rgba(36,26,18,0.75)',
        whiteSpace: 'pre-line',
      }}
    >
      {'Para cada hora, hay un café\nesperándote en Between.'}
    </div>

    {guia ? (
      <ZonaReservada zona={ZONA_QUIZ} etiqueta={'QUIZ · 4 alternativas\n660 × 300'} />
    ) : null}
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 16-09 · COWORK  (col N · CORREGIDO, con un comentario ABIERTO)

   ⚠️ EL COMENTARIO DEL CLIENTE, Y CÓMO SE ATACA.
   `STORIES!N` trae sin tachar: «Se puede entender que estuvimos cerrados,
   démosle una vuelta a ese texto». El copy de la grilla YA está corregido —dice
   «PUEDES VENIR, ¡TE ESPERAMOS!» y no «ya abrimos»—; «COWORK | YA ABRIMOS» es
   sólo el NOMBRE INTERNO de la fila y no va en pantalla. Lo que seguía sin
   corregir era la FOTO: la versión del 31-08 mostraba mesas altas vacías,
   enfocadas y sin nadie, y eso es lo que se lee como local cerrado.
   Acá entra una mesa SERVIDA y en uso —notebook abierto, taza con su platillo,
   libreta— con las ampolletas encendidas. Es la misma lección que el manual ya
   tiene escrita en «Que se parezca a Between no es que salga el local»: manda el
   plano corto y cálido, no la arquitectura reconocible.

   POR QUÉ ACÁ SÍ HAY CAJA TAUPE Y EN LAS OTRAS DOS NO:
   esta foto es follaje de terraza y no tiene UNA franja calma — el desvío
   estándar por franjas de 80 px va de 45 a 72 en todo el alto. La regla del
   cliente para ese caso es explícita: el texto va en caja `#675B49`, no se
   oscurece la foto.
   ══════════════════════════════════════════════════════════════════════════ */

const ZONA_ENLACE: Zona = {ancho: 660, alto: 140, top: 1320};

export const StS3Cowork: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: '#241a12'}}>
    <FotoFondo src={F + 'st-16-09-cowork.jpg'} oscurecer={0.14} />

    {/* `sombra` es el halo que pidió Eli el 02-09 —«una sombra con opacidad para
        que se vea el logo bien, muy sutil»— y esta pieza es su caso de libro: el
        lockup cae sobre follaje con ampolletas encendidas detrás. 0,22 es el
        valor que el propio componente documenta como «muy sutil». */}
    <LogoBetween formato="story" posicion="arriba" tono="beige" sombra={0.22} />

    <Columna top={BETWEEN.bloque.yStory}>
      <TitularBetween
        script="Puedes venir"
        caps="¡Te esperamos!"
        alinear="centro"
        tono="beige"
        anchoDisponible={BETWEEN.bloque.columna}
      />
      {/* El horario y la bajada, literales de la grilla, como PILA IGUALADA.
          `CajaDato` ya pasa las cifras por la caja tabular: son dos «0» dobles y
          sin eso los dígitos bailan (regla de la ronda 6).
          La interlínea del panel se aprieta a 1,25: con 1,3 el panel crecía
          hasta pisar la mesa del notebook, que es el sujeto de la foto. */}
      <PilaIgualada top={BETWEEN.aire.tituloACaja}>
        <CajaDato anchoDisponible={BETWEEN.bloque.columna}>
          Lunes a viernes · 08:00 a 22:00 hrs.
        </CajaDato>
        <PanelTaupe size={34} ancho={BETWEEN.bloque.columna} interlinea={1.25}>
          Ven a trabajar desde Between.<br />Tenemos una mesa para ti.
        </PanelTaupe>
      </PilaIgualada>
    </Columna>

    {guia ? (
      <ZonaReservada zona={ZONA_ENLACE} etiqueta={'ENLACE · «VER LA CARTA»\n660 × 140'} />
    ) : null}

    {/* El «cierre pequeño» del brief, literal. `LegalAlPie` en story lo deja
        cerrando justo por encima de y=1580, o sea fuera de la franja de Meta. */}
    <LegalAlPie formato="story">WiFi · Café · Espacios para trabajar</LegalAlPie>
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 18-09 · SALUDO FIESTAS PATRIAS  (col O · OK PARA DISEÑAR)

   La grilla NO pide interacción en esta columna, así que no lleva zona
   reservada: es un saludo y la foto puede ocupar el pie.

   Es la única de las tres con el panel de la referencia, y por necesidad
   medida: el párrafo del brief tiene 93 caracteres y en esta foto sólo
   y=240–560 está calma (desvío estándar 4–12 contra 37–91 más abajo). El
   titular cabe libre en esa franja; el párrafo, no. Así que el titular va suelto
   sobre la mesa oscura —que es lo que hace la marca— y el párrafo con el saludo
   baja al panel taupe, que es el «panel» del pin traducido al color de Between.
   ══════════════════════════════════════════════════════════════════════════ */

export const StS3Dieciocho: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: '#241a12'}}>
    {/* 0,08: esta foto ya viene oscura arriba (L=37 en la franja del titular) y
        el sujeto es comida clara — el manual pide mano SUAVE con la comida
        clara, que pierde sus capas si se toca. */}
    <FotoFondo src={F + 'st-18-09-dieciocho.jpg'} oscurecer={0.08} />

    <LogoBetween formato="story" posicion="arriba" tono="beige" />

    <Columna top={BETWEEN.bloque.yStory}>
      <TitularBetween
        script="Por los sabores"
        caps="Que nos reúnen"
        alinear="centro"
        tono="beige"
        anchoDisponible={BETWEEN.bloque.columna}
      />
      {/* El párrafo y el saludo, literales del brief, como PILA IGUALADA: los
          dos son caja taupe, y dos cajas apiladas de anchos distintos son la
          «escalera» que Eli marcó como desorden. Acá el párrafo es el más ancho
          y el saludo se estira hasta su mismo borde.
          Los saltos del párrafo van a mano para repartir las tres líneas
          parejas: partido por el navegador quedaba «compartir.» solo en la
          última, y la regla de la ronda 5 es que la caja de bajada no deja
          palabras viudas. */}
      <PilaIgualada top={BETWEEN.aire.tituloACaja}>
        <PanelTaupe size={32} ancho={BETWEEN.bloque.columna} interlinea={1.3}>
          Que estas Fiestas Patrias estén llenas de<br />
          buenos momentos, sobremesas y mucho<br />
          para compartir.
        </PanelTaupe>
        <CajaDato anchoDisponible={BETWEEN.bloque.columna}>
          ¡Felices Fiestas Patrias!
        </CajaDato>
      </PilaIgualada>
    </Columna>
  </AbsoluteFill>
);

/* Variantes «guía» — llevan dibujada la zona del sticker. NO se entregan al
   cliente ni se suben al Drive: son para el CM.
   La 18-09 no tiene guía porque no lleva interacción. */
export const StS3HoraCafeGuia: React.FC = () => <StS3HoraCafe guia />;
export const StS3CoworkGuia: React.FC = () => <StS3Cowork guia />;
