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
  LogoBetween,
  TitularBetween,
} from './BetweenSistema';
import {BanderaChile, BrindisTazas, GuirnaldaBanderitas} from './BetweenIlustraS3';

const F = 'assets/hilton/between/st-s3/';

/**
 * ⛔ EL LOGO EN CAFÉ NO SALE DE `BETWEEN.logo.cafe`.
 *
 * Eli, ronda 4: «el color del logo debe ser el café de between ese color». Y el
 * token `BETWEEN.logo.cafe` apunta a `logo-negro.png`, que medido sobre sus
 * píxeles opacos es **negro puro `#000000`** — no el café `#675B49`. O sea que
 * las dos piezas de la S3 venían con el logo NEGRO, fuera de paleta.
 *
 * El archivo correcto lo genera `scripts/between-st-s3-materiales.py` a partir
 * del CANAL ALFA del logo oficial. El token del kit NO se toca: lo usan piezas
 * ya aprobadas y cambiarlo las re-flujaría (misma razón que `columnaTitular`).
 */
const LOGO_CAFE = 'assets/hilton/between/logo-cafe-marca.png';

/** Lockup en el café de marca, en la geometría `storyLogoArriba` de Eli. */
const LogoCafeMarca: React.FC = () => {
  const g = BETWEEN.margenes.storyLogoArriba;
  return (
    <Img
      src={staticFile(LOGO_CAFE)}
      style={{
        position: 'absolute',
        left: (1080 - g.ancho) / 2,
        top: g.wordmarkY,
        width: g.ancho,
        height: g.ancho / BETWEEN.logo.ratio,
        objectFit: 'contain',
      }}
    />
  );
};

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

   ⭐⭐ RONDA 3 (08-09) — Eli: «el logo es el color café de between, y los
   titulos en BEIGE por favor para que se lea y sea visible».

   Las dos cosas juntas obligan a resolverlo así, y la razón es medida. El
   lockup se queda en café porque cae sobre la pared clara (L=177), que es
   justamente para lo que el kit define ese color: «texto sobre fondos muy
   claros». Pero un texto BEIGE sobre esa misma pared no existe — medido, el
   contraste del beige `#FFF9EB` contra la pared da **1,43:1**, y no pasa de
   1,9:1 hasta y≈880, que ya es donde empieza la mesa y a 240 px de la taza.

   O sea que para que los títulos sean beige Y se lean, el beige necesita un
   fondo café. Y ése es un elemento que la marca ya tiene y que el propio cliente
   autorizó por escrito: «cuando no se logra visualizar los textos, puedes
   dejarlo en una caja del color café #675B49».

   Así que el titular, el horario y la bajada entran a UN SOLO CARTEL taupe con
   todo el texto en beige. Un cartel y no tres cajas apiladas: es la regla §1 bis
   («una pila = un borde derecho») llevada al límite, y deja la pared beige de
   arriba como aire con el lockup café, que es lo que hace el referente.
   ══════════════════════════════════════════════════════════════════════════ */

/* ⭐ RONDA 4 — la zona del enlace se va A LA PARED, y es el mejor sitio que
   tiene la pieza. Con el titular fuera del cartel (ver abajo) el pie se ocupa
   con el cartel de dato y el cierre, y ya no queda hueco limpio ahí. La pared
   beige del tercio de arriba, en cambio, es la superficie más limpia de toda la
   pieza: desvío estándar 9 sobre 255, sin un solo objeto detrás. Un sticker de
   enlace ahí se pega sobre nada. Va anotado en la `GUIA CM`. */
const ZONA_ENLACE: Zona = {ancho: 660, alto: 140, top: 650};

export const StS3Cowork: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: '#241a12'}}>
    <FotoFondo src={F + 'st-16-09-cowork.jpg'} oscurecer={0.04} />

    {/* El lockup en el CAFÉ DE MARCA, no en el negro de `BETWEEN.logo.cafe`.
        Ver `LOGO_CAFE` arriba: es el pedido literal de Eli en la ronda 4. */}
    <LogoCafeMarca />

    {guia ? (
      <ZonaReservada
        zona={ZONA_ENLACE}
        etiqueta={'ENLACE · «VER LA CARTA»\n660 × 140'}
      />
    ) : null}

    {/* ⭐⭐ RONDA 4 — EL TITULAR SALE DEL CARTEL, Y BAJA A y=880.
        Eli: «el título de puedes venir... ese debe ir fuera del recuadro café
        between». Suelto sobre la foto sigue teniendo que ser BEIGE, que es lo
        que ella pidió en la ronda anterior, y ahí está el detalle que decide la
        posición: el beige NO se lee en cualquier parte de esta foto.

        Medido por tercios de la columna, contraste del beige contra el fondo:

        | y     | izquierda | centro | derecha |
        |-------|-----------|--------|---------|
        | 620   | 1,36      | 1,50   | 2,20    |
        | 800   | 1,41      | 2,07   | 2,45    |
        | **920** | **2,71** | **2,19** | **2,87** |
        | 980   | 2,73      | 2,82   | 3,27    |

        El tercio IZQUIERDO sigue siendo pared clara hasta y≈860, así que un
        titular beige puesto arriba se leería sólo por la derecha y desaparecería
        por la izquierda — el defecto que Eli marcó. La primera franja donde el
        beige pasa de 2:1 en los TRES tercios es y=880. Ahí va. */}
    <Columna top={880}>
      <TitularBetween
        script="Puedes venir"
        caps="¡Te esperamos!"
        alinear="centro"
        tono="beige"
        anchoDisponible={BETWEEN.bloque.columna}
      />
    </Columna>

    {/* EL CARTEL, ahora sólo con el DATO. Baja a y=1330: la taza con su platillo
        ocupa y=1120–1320 (medido) y la mesa servida —taza con arte latte,
        notebook, libreta y croissant— tiene que quedar a la vista, que es la
        corrección de la ronda 2. */}
    <div
      style={{
        position: 'absolute',
        left: (1080 - BETWEEN.bloque.columna) / 2,
        top: 1330,
        width: BETWEEN.bloque.columna,
        boxSizing: 'border-box',
        background: BETWEEN.cajas.fondo,
        borderRadius: BETWEEN.cajas.radio,
        padding: '24px 44px 22px',
        boxShadow: '0 22px 60px rgba(36,26,18,0.34)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      {/* El horario, literal de la grilla. Va SIN caja: dentro de un cartel que
          ya es taupe, meterle otra caja taupe no agrega jerarquía — es la regla
          «una sola línea fuerte por pila». `sinFondo` conserva la tipografía, la
          caja alta y la altura de fila, y `CajaDato` sigue pasando las cifras
          por la caja tabular (son dos «0» dobles y sin eso los dígitos bailan). */}
      <CajaDato sinFondo anchoDisponible={BETWEEN.bloque.columna - 2 * 44}>
        Lunes a viernes · 08:00 a 22:00 hrs.
      </CajaDato>
      {/* La bajada, literal. Los saltos a mano: partida por el navegador dejaba
          «para ti.» sola en la última línea. */}
      <div
        style={{
          marginTop: 2,
          textAlign: 'center',
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.semibold,
          fontSize: 32,
          lineHeight: 1.24,
          color: BETWEEN.colores.beige,
        }}
      >
        Ven a trabajar desde Between.<br />Tenemos una mesa para ti.
      </div>
    </div>

    {/* El «cierre pequeño» del brief, literal.
        ⭐ RONDA 4 — Eli: «Agrandar un poco el texto de abajo ya que no se lee
        bien. que sea italic pero un poco más grande». `LegalAlPie` lo pintaba a
        **28 px**, que es la medida del legal de una story y acá se leía chico.
        Sube a **38 px** manteniendo la cursiva, y por eso deja de usar
        `LegalAlPie` —que tiene el cuerpo fijo— y pasa a `Cierre`.
        En y=1540 `between-qa.py` marcaba 5 px dentro de la franja inferior de
        Meta (la cursiva a 38 px baja más de lo que uno calcula), así que va en
        1532 y la pieza sale LIMPIA. */}
    <Cierre top={1532} size={38}>
      WiFi · Café · Espacios para trabajar
    </Cierre>
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 18-09 · SALUDO FIESTAS PATRIAS  (col O · OK PARA DISEÑAR)

   La grilla NO pide interacción, así que no lleva zona reservada.

   ⭐⭐ RONDA 3 (08-09) — Eli: «el contexto es 18 de septiembre de fiestas patrias
   de Chile, necesito que sea detalles ILUSTRADOS y haz más similar a la
   referencia con los colores de between».

   Las tres cosas que cambian respecto de la ronda 2, y todas vienen de ahí:

   1. **El cartel manda.** En el `REF 3` el cartel ocupa ~80 % del alto y la foto
      es el marco. La ronda 2 lo tenía al revés —un panel chico en la mitad de
      abajo—, así que el cartel crece a 812 × 1260 y la foto queda alrededor.
   2. **Los detalles son ILUSTRADOS.** El referente resuelve su motivo con un
      dibujo de línea de un solo color, y ahora eso es lo que se pidió: entran
      una **guirnalda de banderitas** y un **brindis de dos tazas de café**,
      dibujados en `BetweenIlustraS3.tsx` y en la tinta café `#675B49` de la
      marca. ⛔ Nada de rojo, azul ni blanco de bandera: Eli pidió los colores de
      Between, y la bandera chilena no es su paleta. El 18 se lee por las
      banderitas, no por el tricolor.
   3. **La foto pasa a ser AMBIENTE.** Como el brindis ya es dibujo, la escena
      fotográfica del brindis sobraba: el fondo es ahora el local muy
      desenfocado, con las ampolletas encendidas convertidas en manchas de luz
      dorada — que es exactamente el papel que cumple el loft del referente.

   El lockup va DENTRO del cartel y en café, como el referente pone su identidad
   dentro del papel. No hay lockup flotante arriba: leerla dos veces es el mismo
   defecto que repetir el logo sobre una foto con el vaso impreso (regla 8).
   ══════════════════════════════════════════════════════════════════════════ */

/* ⛔ El cartel NO lleva alto fijo. Se probó con `minHeight: 1260` —para que
   ocupara la misma proporción que el de la referencia— y dejó 160 px de beige
   muerto al pie, con todo el contenido apretado arriba: se lee como un error de
   diagramación, no como el aire de un cartel. Ahora se ajusta a su contenido
   (≈1130 px) y arranca en y=330, lo que deja 80 px de foto arriba y 119 abajo. */
const CARTEL = {ancho: 812, padX: 52, top: 330};

/**
 * ⭐ RONDA 4 — el cartel es PAPEL, no un plano de color.
 *
 * Eli: «el cuadro beige de texto debe ser una textura de papel beige, similar a
 * la referencia». El cartel del referente es papel crema con grano.
 *
 * La textura la sintetiza `scripts/between-st-s3-materiales.py` con semilla
 * fija —grano fino + fibra horizontal + un manchado muy leve sobre el beige de
 * marca `#FFF9EB`— en vez de generarla con IA, por dos razones: el tinte tiene
 * que caer exacto en el hex de la marca, y con semilla fija esto se reproduce.
 * Desvío medido: 2,86 niveles sobre 255. Se tiene que notar en el canto y a
 * tamaño real, no convertirse en un fondo con dibujo: sobre el texto café un
 * grano fuerte se lee como suciedad.
 *
 * `backgroundColor` va ADEMÁS de la imagen, no en su lugar: si el PNG no cargara
 * el cartel seguiría siendo beige y no un agujero transparente.
 */
const PAPEL = 'assets/hilton/between/papel-beige.png';

export const StS3Dieciocho: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: '#241a12'}}>
    {/* 0,18: el ambiente viene claro y con mucho bokeh dorado, y el cartel beige
        necesita despegarse del fondo. Es velo sobre AMBIENTE, no sobre un texto,
        así que no choca con la regla de no apagar la foto para leer un texto. */}
    <FotoFondo src={F + 'st-18-09-dieciocho.jpg'} oscurecer={0.18} />

    <div
      style={{
        position: 'absolute',
        left: (1080 - CARTEL.ancho) / 2,
        top: CARTEL.top,
        width: CARTEL.ancho,
        boxSizing: 'border-box',
        backgroundColor: BETWEEN.colores.beige,
        backgroundImage: `url(${staticFile(PAPEL)})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        borderRadius: BETWEEN.cajas.radio,
        padding: `40px ${CARTEL.padX}px 34px`,
        boxShadow: '0 30px 80px rgba(36,26,18,0.45)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      {/* El lockup en el CAFÉ DE MARCA, no en el negro de `BETWEEN.logo.cafe`
          — ver `LOGO_CAFE` arriba. 196 px es el mínimo de la plantilla de story
          de Eli y dentro de un cartel no necesita más; el alto sale del ratio
          3,0298 para que nunca se vea achatado. */}
      <Img
        src={staticFile(LOGO_CAFE)}
        style={{width: 196, height: 196 / BETWEEN.logo.ratio, objectFit: 'contain'}}
      />

      {/* LOS DETALLES ILUSTRADOS. La guirnalda primero, colgada bajo el lockup
          como si el cartel estuviera adornado; el brindis después, que es el
          motivo central del referente. */}
      <div style={{marginTop: 18}}>
        <GuirnaldaBanderitas
          ancho={CARTEL.ancho - 2 * CARTEL.padX}
          tinta={BETWEEN.colores.cafe}
        />
      </div>
      <div style={{marginTop: 6}}>
        <BrindisTazas
          ancho={CARTEL.ancho - 2 * CARTEL.padX}
          tinta={BETWEEN.colores.cafe}
        />
      </div>

      {/* ⭐ RONDA 4 — la banderita de Chile. Eli: «añade una ilustración cute de
          la bandera de Chile, similar a la ilustracion».
          Va DEBAJO del brindis y chica (168 px, 21 % del ancho del cartel): es
          un detalle, no un tercer motivo compitiendo con la guirnalda y las
          tazas. Y va en una sola tinta café, con la geometría haciendo el
          trabajo —cantón cuadrado, estrella calada, división horizontal—, porque
          el rojo y el azul de la bandera no están en la paleta de Between y Eli
          pidió los colores de la marca en el mismo mensaje. El `fondo` es el
          beige del papel: la estrella se cala con él, como el blanco de la
          bandera de verdad. */}
      <div style={{marginTop: -6}}>
        <BanderaChile
          ancho={168}
          tinta={BETWEEN.colores.cafe}
          fondo={BETWEEN.colores.beige}
        />
      </div>

      <div style={{marginTop: 8}}>
        <TitularBetween
          script="Por los sabores"
          caps="Que nos reúnen"
          alinear="centro"
          tono="cafe"
          anchoDisponible={CARTEL.ancho - 2 * CARTEL.padX}
        />
      </div>

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

      {/* El saludo de cierre, literal. Es la línea fuerte del cartel, así que va
          en caja taupe: dentro del beige, el café macizo es el énfasis. Una sola
          línea fuerte por pila (manual §1 bis). */}
      <div style={{marginTop: 28}}>
        <CajaDato anchoDisponible={CARTEL.ancho - 2 * CARTEL.padX}>
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
