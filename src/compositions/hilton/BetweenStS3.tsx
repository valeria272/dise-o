/**
 * BETWEEN — S3 · LAS TRES STORIES DE LA SEMANA 3 (14, 16 y 18 de septiembre)
 *
 * Las tres columnas de la hoja STORIES de la grilla
 * (`1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY`, instantánea del 08-09 en
 * `clients/hilton/grillas/between-septiembre-2026.md`):
 *
 *   col M · 14-09 · OK PARA DISEÑAR · «ST INTERACTIVA – ¿CUÁNDO ES HORA DE CAFÉ?»
 *   col N · 16-09 · CORREGIDO       · «ST ESTÁTICA – COWORK | YA ABRIMOS»
 *   col O · 18-09 · OK PARA DISEÑAR · «ST ESTÁTICA - SALUDO 18 SEPT»
 *
 * ══════════════════════════════════════════════════════════════════════════
 * RONDA 2 (08-09-2026) — Eli devolvió las tres y esto se rehizo entero
 * ══════════════════════════════════════════════════════════════════════════
 *
 * «Hazlos de nuevo las 3 stories ya que no cumplen, debes dejar mejores
 * fotografías, mejor imagenes hazlo en conjunto a magnific», con tres referentes
 * adjuntos en Drive (`12S5bEGzPtZmE82U_ZxrboyZwsvOOQoZ0` →
 * `raw/hilton/between/ref-s3-eli/`) y una condición: «deben ser colores y fondos
 * de Between, pero puedes guiarte de elementos de la referencia para hacerlos
 * similar. Con la identidad visual de BW».
 *
 * ⭐ EL DIAGNÓSTICO, Y ES UNO SOLO. La ronda 1 usaba FOTO DE BANCO recortada, y
 * el banco de Between está pensado en 4:5: al llevarlo a 9:16 no queda hueco
 * donde la diagramación lo necesita, así que el texto terminó apoyado en cajas
 * taupe y las tres piezas se parecieron entre sí. **Los tres referentes de Eli
 * hacen lo contrario: la foto está PRODUCIDA con el hueco adentro** —un torso de
 * color liso que llena el cuadro, una pared plana en el tercio de arriba, un
 * plano del local muy desenfocado— y por eso el titular va grande y suelto.
 *
 * O sea que el problema no era la diagramación: era que la foto no se había
 * producido. Ahora las tres escenas se GENERAN con el método que Eli ya tiene
 * escrito en `clients/hilton/PROMPTS-DE-ELI.md` («no se compone: se GENERA»),
 * con las fotos reales como referencia — `scripts/between-st-s3-generar.py` —
 * y el laboratorio va en `scripts/between-st-s3-fotos.py`.
 *
 * ── QUÉ ELEMENTO SE TOMÓ DE CADA REFERENTE ───────────────────────────────
 *
 * `REF 1` (14-09) · torso con camisa azul llenando el cuadro + taza sostenida
 * abajo + tarjeta con la pregunta arriba + línea de cierre al pie.
 *   → El fondo es un CAMPO DE COLOR DE MARCA: sweater **café `#675B49`** que
 *     llena el cuadro, con la taza blanca sostenida en el tercio inferior. La
 *     tarjeta de la pregunta NO se dibuja: es la zona reservada del quiz.
 *
 * `REF 2` (16-09) · pared plana gris en el tercio superior + titular enorme +
 * mesa de madera oscura con notebook y café + horario al pie.
 *   → **Pared beige** limpia en el tercio de arriba (es el vocabulario de Eli:
 *     «debe ser en una pared beige»), y por eso ésta es la única de las tres con
 *     el titular en **tinta café** — el kit lo define así: el café es «texto
 *     sobre fondos muy claros». El titular va grande y SIN caja, que es lo que
 *     el referente hace y lo que la ronda 1 no pudo hacer.
 *
 * `REF 3` (18-09) · panel crema sobre la foto del local + dos manos brindando.
 *   → **Panel beige `#FFF9EB`** con tinta café y el lockup café adentro, sobre
 *     la escena. Y el brindis va con **dos tazas de Between de verdad, en la
 *     fotografía**: el repertorio de línea de la marca son los trazos del `.svg`
 *     de Eli y ahí no hay un brindis, y el manual prohíbe dibujar o generar
 *     trazos nuevos. Pedírselo al generador respeta las dos cosas.
 *
 * ── LO INTERACTIVO: ZONA RESERVADA, NUNCA DIBUJADA ───────────────────────
 * Orden de Eli del 07-09, repetida el 08-09: «eso no va diseñado, solo se deja
 * aire de espacio libre». El sticker real lo pone el CM. Se entrega además una
 * copia `GUIA CM` con la zona marcada, que NO se sube al Drive.
 *
 *   14-09 → QUIZ de 4 alternativas   · 660 × 360   (ahora sí del porte real:
 *           el campo de color liso da 880 px de aire y no hay que apretarlo)
 *   16-09 → sticker de ENLACE (carta) · 660 × 140
 *   18-09 → la grilla no pide interacción → no lleva zona reservada
 *
 * ── LA REJILLA (1080×1920, se entrega a 2250×4000) ───────────────────────
 * Zona segura de Meta: nada de contenido sobre y=250 ni bajo y=1580.
 *    250 ─ zona segura superior
 *    271 ─ wordmark del lockup (plantilla `storyLogoArriba` de Eli)
 *    441 ─ primera línea de tinta (`BETWEEN.bloque.yStory`; deja los 77 px de
 *          aire logo→texto que miden sus plantillas)
 *   1580 ─ empieza la zona segura inferior
 *
 * Los anclajes de abajo no son de gusto: salen del perfil de cada foto por
 * franjas de 80 px (luminancia media y desvío estándar sobre la columna
 * central). Las cifras están en la bitácora del 08-09.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
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
   LA ZONA RESERVADA — mismo aparato que `BetweenStCumpleCarrusel.tsx`, con el
   alto por pieza: un quiz de cuatro alternativas no ocupa lo mismo que una
   pastilla de enlace. Las medidas salen de `StickerQuiz` y `StickerEnlace`.
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

/**
 * Pila de cajas taupe con UN SOLO BORDE DERECHO.
 *
 * Regla del manual § «1 bis. Una pila de cajas va toda del MISMO ANCHO», que
 * salió del «se ve todo desordenado en los textos y no se ve pulcro» de Eli: el
 * desorden no eran los dígitos, era la ESCALERA de anchos distintos. Se resuelve
 * sin medir en JS: el contenedor es `inline-flex` —se encoge al ancho de la caja
 * más ancha— y los hijos van `stretch`.
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

/** Cierre en cursiva, suelto sobre la foto. */
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
   ST 14-09 · ¿CUÁNDO ES HORA DE CAFÉ?  (col M · OK PARA DISEÑAR)

   Textos LITERALES de la grilla. El brief separa tres cosas y sólo dos van
   diseñadas:
     · «Texto» → el titular.
     · «Cierre» → la línea en cursiva al pie, como en el referente.
     · «Respuesta correcta: Obviamente, D. Todo el día.» → NO va en la pieza: es
       la respuesta que el CM marca DENTRO del sticker de quiz. Dibujarla
       reventaría el juego.

   MEDIDO sobre la foto: el campo de sweater café va de y=240 a y=1120 con un
   desvío estándar de 6–16 (o sea liso), la taza en la mano ocupa 1120–1600, y de
   1600 abajo vuelve a oscurecer (L=40). Con 880 px de campo limpio el quiz cabe
   del porte real —660×360— sin apretarlo, que era el problema de la ronda 1.
   ══════════════════════════════════════════════════════════════════════════ */

const ZONA_QUIZ: Zona = {ancho: 660, alto: 360, top: 700};

export const StS3HoraCafe: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: '#241a12'}}>
    {/* `oscurecer` 0: el sweater YA es el café de marca, corregido a #675B49 en
        `between-st-s3-fotos.py`. Un multiply encima lo alejaría del hex exacto,
        que es justo lo que Eli pidió cuidar («deben ser colores de Between»). */}
    <FotoFondo src={F + 'st-14-09-hora-cafe.jpg'} oscurecer={0} />

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

    {guia ? (
      <ZonaReservada zona={ZONA_QUIZ} etiqueta={'QUIZ · 4 alternativas\n660 × 360'} />
    ) : null}

    {/* El cierre del brief, literal, al pie como en el referente. En y=1620 cae
        sobre la zona oscura y calma de abajo (L=40, sd=23) — el único sitio del
        cuadro donde se lee sin ayuda una vez que la taza ocupa el medio.
        ⚠️ Entra 40 px en la franja inferior de 340 px de Meta y `between-qa.py`
        lo marca. Tiene el mismo precedente que el legal de la ST 2 del
        cumpleaños, que Eli aprobó en y=1640: vale en ORGÁNICO. Si esta pieza
        pasa a pauta, hay que subirlo. */}
    {/* Una sola línea a 30 px, no dos a 34. Medido: la frase completa mide ~665 px
        y entra en la columna de 810 sin partirse, así que además desaparece el
        problema de la viuda («Between.» sola en la segunda línea).
        ⚠️ Y sobre todo: en dos líneas el bloque entraba 125 px en la franja
        inferior de 340 px de Meta, y `between-qa.py` lo marcaba. Así entra ~60,
        que es el orden del legal de la ST 2 del cumpleaños (90 px) que Eli
        aprobó. Vale en ORGÁNICO; si esta pieza pasa a pauta, hay que subirlo.
        No se puede subir más: medido, la taza y la mano ocupan hasta y=1600 y de
        ahí para arriba el texto caería sobre la loza. */}
    <Cierre top={1600} size={30}>
      Para cada hora, hay un café esperándote en Between.
    </Cierre>
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 16-09 · COWORK  (col N · CORREGIDO, con un comentario ABIERTO)

   ⚠️ EL COMENTARIO DEL CLIENTE, Y CÓMO SE ATACA.
   `STORIES!N` trae sin tachar: «Se puede entender que estuvimos cerrados,
   démosle una vuelta a ese texto». El copy de la grilla YA está corregido —dice
   «PUEDES VENIR, ¡TE ESPERAMOS!» y no «ya abrimos»; «COWORK | YA ABRIMOS» es
   sólo el NOMBRE INTERNO de la fila y no va en pantalla—. Lo que seguía sin
   corregir era la FOTO: la versión del 31-08 mostraba mesas altas vacías,
   enfocadas y sin nadie. Acá la mesa está SERVIDA y en uso: notebook abierto y
   encendido, taza con su platillo, libreta con lápiz y un croissant.

   ⭐ Y ES LA ÚNICA DE LAS TRES CON TINTA CAFÉ.
   El tercio de arriba es la pared beige que pedía el referente, medida en L=177
   con desvío 9: ahí un texto beige no existe. El kit define el café `#675B49`
   como «texto sobre fondos muy claros», así que el lockup y el titular van en
   café y el titular puede ir grande y SIN caja — que es exactamente lo que hace
   el referente y lo que la foto de banco de la ronda 1 no permitía.

   El bloque de dato baja a y=1080, sobre la mesa: ahí la foto va de L=95 a 136
   con desvío 40–65, o sea ruidosa, y para ese caso la instrucción del cliente es
   literal — «cuando no se logra visualizar los textos, puedes dejarlo en una
   caja del color café #675B49». Una sola pila, no dos como en la ronda 1.
   ══════════════════════════════════════════════════════════════════════════ */

/* top 1330: la taza y su platillo terminan en y=1320 (medido), así que la
   pastilla del enlace arranca justo debajo y cierra en 1470, con 110 px de aire
   antes de la franja inferior de Meta. */
const ZONA_ENLACE: Zona = {ancho: 660, alto: 140, top: 1330};

export const StS3Cowork: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: '#241a12'}}>
    <FotoFondo src={F + 'st-16-09-cowork.jpg'} oscurecer={0.04} />

    {/* Lockup en café, no beige: cae sobre la pared clara. */}
    <LogoBetween formato="story" posicion="arriba" tono="cafe" />

    <Columna top={430}>
      {/* 430 y no 441: el titular en dos líneas tiene que cerrar antes de y=620,
          donde la pared deja de ser plana y entra el follaje. */}
      <TitularBetween
        script="Puedes venir"
        caps="¡Te esperamos!"
        alinear="centro"
        tono="cafe"
        anchoDisponible={BETWEEN.bloque.columna}
      />

      {/* El horario y la bajada, literales de la grilla, como PILA IGUALADA y
          justo bajo el titular. `CajaDato` ya pasa las cifras por la caja
          tabular: son dos «0» dobles y sin eso los dígitos bailan (ronda 6).

          ⛔ NO van abajo, sobre la mesa, aunque el referente ponga el horario al
          pie. Se probó en y=1080 y las dos cajas TAPABAN LA TAZA: medido, la
          taza con su platillo ocupa y=1120–1320, y esconder el café en la pieza
          que habla del café es el defecto que el manual llama «la foto
          contradice su texto». En el referente el pie está vacío; en esta foto
          es donde está el sujeto, así que el bloque de dato sube. */}
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
        cerrando justo por encima de y=1580, fuera de la franja de Meta. */}
    <LegalAlPie formato="story">WiFi · Café · Espacios para trabajar</LegalAlPie>
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 18-09 · SALUDO FIESTAS PATRIAS  (col O · OK PARA DISEÑAR)

   La grilla NO pide interacción, así que no lleva zona reservada.

   Es la traducción del `REF 3`: un PANEL de color sobre la foto del local, con
   todo el texto adentro. El panel es el beige `#FFF9EB` de la marca con tinta
   café, o sea los dos colores de Between y ninguno nuevo — es la caja taupe al
   revés, y la marca ya usa esa inversión en el mock de post crema.

   MEDIDO: el brindis ocupa y=240–860 y de 1440 abajo la foto es calma y oscura
   (L 33–49, desvío 3–13). El panel arranca en 860, justo bajo las tazas, así que
   el brindis —que es el elemento que se tomó del referente— queda entero a la
   vista y el panel no tapa nada del gesto.
   ══════════════════════════════════════════════════════════════════════════ */

const PANEL = {ancho: 810, padX: 54, padY: 44};

export const StS3Dieciocho: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: '#241a12'}}>
    {/* 0,10: la escena ya viene contrastada del generador y arriba hay contraluz.
        Lo mínimo que asienta el follaje detrás de las tazas. */}
    <FotoFondo src={F + 'st-18-09-dieciocho.jpg'} oscurecer={0.1} />

    {/* ⛔ Sin lockup flotante arriba: el logo va DENTRO del panel, como el
        referente pone su identidad dentro del cartel. Poner los dos sería leer
        la marca dos veces, que es la misma razón por la que una pieza con el
        vaso impreso no repite el lockup (manual, regla 8). */}
    <div
      style={{
        position: 'absolute',
        left: (1080 - PANEL.ancho) / 2,
        top: 860,
        width: PANEL.ancho,
        boxSizing: 'border-box',
        background: BETWEEN.colores.beige,
        borderRadius: BETWEEN.cajas.radio,
        padding: `${PANEL.padY}px ${PANEL.padX}px ${PANEL.padY - 6}px`,
        boxShadow: '0 26px 70px rgba(36,26,18,0.42)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <Img
        src={staticFile(BETWEEN.logo.cafe)}
        /* Ancho 196 = el mínimo de la plantilla de story de Eli. Dentro de un
           panel de 810 el lockup no necesita más, y el alto sale del ratio
           3,0298 para que nunca se vea achatado. */
        style={{width: 196, height: 196 / BETWEEN.logo.ratio, objectFit: 'contain'}}
      />
      <div style={{height: 34}} />
      <TitularBetween
        script="Por los sabores"
        caps="Que nos reúnen"
        alinear="centro"
        tono="cafe"
        anchoDisponible={PANEL.ancho - 2 * PANEL.padX}
      />
      {/* El párrafo del brief, literal y completo, en tinta café sobre el beige.
          Los saltos van a mano para repartir las tres líneas parejas: partido
          por el navegador quedaba «compartir.» solo en la última, y la regla de
          la ronda 5 es que la bajada no deja palabras viudas. */}
      <div
        style={{
          marginTop: BETWEEN.aire.tituloABajada,
          textAlign: 'center',
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.semibold,
          fontSize: 32,
          lineHeight: 1.34,
          color: BETWEEN.colores.cafe,
        }}
      >
        Que estas Fiestas Patrias estén llenas de<br />
        buenos momentos, sobremesas y mucho<br />
        para compartir.
      </div>
      {/* El saludo de cierre, literal. Es la línea fuerte del panel, así que va
          en caja taupe: dentro del beige, el café macizo es el énfasis. Una sola
          línea fuerte por pila (manual §1 bis). */}
      <div style={{marginTop: 30}}>
        <CajaDato anchoDisponible={PANEL.ancho - 2 * PANEL.padX}>
          ¡Felices Fiestas Patrias!
        </CajaDato>
      </div>
    </div>
  </AbsoluteFill>
);

/* Variantes «guía» — llevan dibujada la zona del sticker. NO se entregan al
   cliente ni se suben al Drive: son para el CM.
   La 18-09 no tiene guía porque no lleva interacción. */
export const StS3HoraCafeGuia: React.FC = () => <StS3HoraCafe guia />;
export const StS3CoworkGuia: React.FC = () => <StS3Cowork guia />;
