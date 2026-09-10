/**
 * DOUBLETREE — HISTORIA · DÍA DEL TURISMO (STORIES col K · 27-09 · 10:00)
 *
 * Encargo de Eli, 09-09-2026: «Trabajaremos diseñando la historia de la S4 de DT
 * […] solamente la última historia del día del turismo, guíate de la referencia
 * para la gráfica, pero siguiendo lineamientos de DT».
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL — no se toca ni una palabra (§G: en DT sólo se DISEÑA)
 * ══════════════════════════════════════════════════════════════════════════
 * De la hoja STORIES, columna K, estado **OK PARA DISEÑO**, sin comentarios
 * para diseño (instantánea `clients/hilton/grillas/dt-septiembre-2026.md`):
 *
 *     ESTÁTICA - DÍA DEL TURISMO
 *     Diseño con imagen institucional o paisaje relacionado a turismo/Santiago.
 *     Saludo simple por el Día del Turismo, sin promoción ni concurso asociado.
 *     Texto principal: "¡Feliz Día del Turismo!"
 *     Subtexto: Gracias por elegir vivir experiencias con nosotros.
 *
 * Los dos textos van **verbatim**. No entra dirección, ni correo, ni CTA, ni
 * legal: el brief no los pide y «saludo simple […] sin promoción» es una
 * instrucción, no un descuido. Añadirlos sería inventar contenido.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REFERENCIA: QUÉ SE TOMA Y QUÉ SE DEJA
 * ══════════════════════════════════════════════════════════════════════════
 * El pin que el brief enlaza es el MISMO archivo que Eli dejó en
 * `REFERENCIAS S4 DT` (`raw/hilton/dt/ref-s4/`): un folleto de arquitectura e
 * interiores (KAPCHER, «Crafting / Sophisticated Spaces»), 1080×1350.
 *
 * SE TOMA (es la gramática que pidió Eli):
 *   · foto de ambiente a sangre, protagonista;
 *   · logotipo centrado arriba, chico;
 *   · un **marco de esquinas redondeadas en filete fino** que contiene el texto;
 *   · titular grande en caja baja + bajada mucho más chica.
 *
 * NO SE TOMA:
 *   · su sans geométrica → en DT el titular es **Stag** y el cuerpo **Trade**;
 *   · su pie con teléfono, correo y ciudades → el brief no los pide;
 *   · su formato 4:5 → esto es historia 9:16, compuesta como 9:16.
 *
 * ⭐ El marco redondeado NO es un elemento importado: **ya existe en DT.** Las
 * piezas aprobadas del Family Time usan exactamente eso — caja de esquinas
 * redondeadas con filete blanco, medida en `DT FT S3` con **ancho 730 @1080** y
 * centrada. O sea que la referencia y el sistema pedían lo mismo, y el elemento
 * entra traducido, no inventado.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA FOTO: REAL, DEL CLIENTE, Y NADA GENERADO
 * ══════════════════════════════════════════════════════════════════════════
 * `HDT_43.jpg` de la sesión profesional — **el frontis del hotel**, 4475×6718,
 * Canon. Es «imagen institucional» tal cual la pide el brief. Recortada a 9:16
 * (ventana centrada, offset 348) y REDUCIDA a 2250×4000: nunca ampliada, nunca
 * estirada. Ver `scripts/dt-st-turismo-foto.py`.
 *
 * ⭐ Esto corrige la bitácora del 09-09, que cerró con «⛔ Del FRONTIS casi no
 * hay nada y no baja». Sí hay, y en alta. No estaba en el banco maestro
 * `Imágenes` (que efectivamente pide login) sino en la carpeta de la sesión
 * profesional. Se encontró mirando las MINIATURAS de Drive en vez de bajar 40
 * archivos de 20-37 MB a ciegas.
 *
 * ⛔ Y por eso acá **no hay nada generado con IA**: existe la foto, manda la
 * foto (`no-generar-producto-que-existe`).
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LAS DOS TINTAS, Y POR QUÉ EL LOGO VA AZUL
 * ══════════════════════════════════════════════════════════════════════════
 * Medido sobre la foto ya recortada, luminancia relativa **por tercios de la
 * columna**, y manda el peor tercio (regla `la-tinta-la-manda-el-fondo`):
 *
 * | banda | fondo desnudo | blanco encima |
 * |---|---|---|
 * | logo (y 241-377)   | Y = 0,538 | **1,79:1 — no se lee** |
 * | texto (y 1150-1503)| Y = 0,337 | 2,72:1 — no se lee |
 *
 * · **El logotipo va en AZUL DoubleTree**, no en blanco. No es gusto: es la
 *   regla §B.4 del manual —«va en azul cuando el fondo es demasiado blanco y el
 *   logo se pierde»— y el cielo pálido es exactamente ese caso. Medido, el azul
 *   sobre el cielo da **6,71 a 9,33:1** en los tres tercios, sin ningún velo
 *   encima. Así la mitad de arriba de la foto queda limpia, que es lo que pide
 *   el tono de la marca: «elegante, minimalista y sencillo».
 *
 * · **El texto va en blanco sobre el velo azul** que sube desde abajo — el
 *   recurso de las tres piezas aprobadas. Con el velo al 0,72 en la banda del
 *   texto, el blanco da **más de 10:1**.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL TITULAR: DOS PESOS DE STAG, Y EL `¡` QUE STAG NO TIENE
 * ══════════════════════════════════════════════════════════════════════════
 * Medido en `C1 FT N1` («Este es su panorama» / «Ideal en familia»), calibrado
 * contra el render propio con la misma máscara de tinta:
 *
 *     línea 1 · Stag **Bold**  · cuerpo ≈ 58 · tinta 49,4 de alto · 576 de ancho
 *     línea 2 · Stag **Light** · cuerpo ≈ 94 · tinta 65,3 de alto · 673 de ancho
 *
 * ⭐ El orden es contraintuitivo y es el de la marca: **arriba Bold y más
 * chica, abajo Light y más grande.** El énfasis lo lleva la línea liviana.
 * Acá el titular se parte «¡Feliz Día» / «del Turismo!» para calcar ese ritmo.
 *
 * Y se respetan las dos reglas de redacción de §F:
 *   · **sin punto** en el titular (termina en `!`, que no es punto);
 *   · **sin mezclar cajas** — las dos líneas van en caja baja.
 *
 * ⛔ **Stag no puede escribir `¡`.** Verificado glifo a glifo con `fontTools`
 * sobre los archivos de esta máquina: los nueve cortes traen el mismo
 * subconjunto de 354 glifos y a todos les falta `U+00A1 ¡` y `U+00BF ¿`. Se
 * resuelve con **el truco de Eli**: el signo de cierre rotado 180°
 * (`volteaApertura`). Trade Gothic sí lo trae, pero pasar la línea a Trade
 * cambiaría el titular de familia — el truco es lo que ella misma hace.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐ RONDA 4 (10-09): «LA LÍNEA DE UNA ESQUINA A LA OTRA», Y EL BLOQUE ARRIBA
 * ══════════════════════════════════════════════════════════════════════════
 * Marca de Eli sobre el PNG entregado: «necesito que la línea comience de una
 * esquina y termine en la otra. Como la referencia. Aumenta el tamaño del texto
 * más pequeño y súbelos incluso el título que están muy abajo. Hazlo más
 * similar a la referencia no se está pareciendo mucho.»
 *
 * Se volvió a MEDIR la referencia en vez de ajustar a ojo (`ref-dia-turismo.png`,
 * 1080×1350). Tres hallazgos, y los tres explican el pedido:
 *
 * 1 · **El marco de la referencia NO está contenido: SANGRA.** Sus tramos
 *     horizontales se van fuera del lienzo. Ampliadas las cuatro esquinas al
 *     200 %, el borde inferior sale por el borde izquierdo y por el derecho, y
 *     el superior corre hasta perderse en la pared iluminada (tramo contiguo
 *     medido: 508 px, x=294→801, filete de realce 203 ⇒ blanco pleno).
 *     Lo que había acá era un rectángulo cerrado de 800 px centrado — o sea
 *     justo lo contrario. **Eso es «de una esquina a la otra».**
 *
 * 2 · **El bloque de texto de la referencia arranca al 35,6 % de la altura**
 *     (y=481 de 1350). El de la entrega arrancaba en y=931 de 1920 = **48,5 %**,
 *     casi 250 px más abajo. La causa es de código, no de gusto: el texto iba
 *     `justifyContent: center` dentro de un marco de 880 de alto, así que se
 *     hundía hasta la mitad. Ahora el bloque se **ancla arriba** con aire
 *     medido, y el marco sube.
 *
 * 3 · Aire arriba/abajo del texto DENTRO del marco en la referencia: 183 y 284
 *     ⇒ razón **0,64**. Acá queda 215 / 314 = 0,68. Se calca la proporción, no
 *     el número: la referencia es 4:5 y esto es 9:16.
 *
 * ⛔ Lo que NO se toca: el titular **no crece**. Ella pidió agrandar «el texto
 * más pequeño», y además ya no cabe: «del Turismo!» mide 593 px @1080 (55 % del
 * ancho) contra los 553 (51 %) de «Crafting» en la referencia — el titular ya
 * iba MÁS ancho que el del pin. Lo que estaba mal era su altura, no su cuerpo.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REJILLA (1080×1920; se entrega a 2250×4000, ×2,0833)
 * ══════════════════════════════════════════════════════════════════════════
 *    250 ─ fin de la zona segura superior de Instagram
 *    241 ─ tope del logotipo  ← plantilla `logo-ST.png` de Eli
 *    377 ─ pie del logotipo
 *    470 ─ tope del marco (ronda 4: subió 210 px; deja 93 de aire bajo el logo)
 *    685 ─ tope de la tinta del titular  = **35,7 %**, el 35,6 % de la referencia
 *   1420 ─ pie del marco (alto 950)
 *   1580 ─ empieza la zona segura inferior (1920 − 340)
 *
 * ⚠️ La columna K del brief **no trae campo INTERACCIÓN**, así que no hay
 * sticker que reservar. Igual la franja de abajo queda limpia: es donde
 * Instagram pone su barra y donde el CM pega lo que necesite. **La interacción
 * no se dibuja nunca** — Eli lo dijo tres veces en Between y vale igual acá.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

import {DT, cargarFuentesDT, volteaApertura} from '../../brand/doubletree';

cargarFuentesDT();

const G = DT.geometria;

/** Textos LITERALES del brief. No se editan (§G). */
const TITULO_1 = '¡Feliz Día';
const TITULO_2 = 'del Turismo!';
/**
 * El subtexto va literal, pero el CORTE DE LÍNEA se fija a mano: dejado al
 * navegador cae «…experiencias con / nosotros.» y una palabra sola en la
 * segunda línea es un defecto documentado. Partido así quedan dos líneas
 * parejas (24 y 26 caracteres).
 */
const SUBTEXTO = ['Gracias por elegir vivir', 'experiencias con nosotros.'];

/**
 * Marco redondeado. **Ronda 2 (09-09): Eli pidió que la línea blanca se
 * pareciera más a la referencia.** Se midió la del pin en vez de estimarla:
 *
 *   · en el borde superior (y=298, x=520) el píxel es **rgb(255,253,250)** y
 *     las filas de arriba y abajo están en 18 y 12 ⇒ **filete de 1 px, blanco
 *     PLENO**. Lo que había era 2 px al 55 %, y por eso se veía blando.
 *   · el marco de la referencia va de x=175 a x=941 ⇒ **ancho 766** sobre un
 *     lienzo de 1080 (71 %). El de DT medido en `DT FT S3` es 730 (67,6 %).
 *     Se adopta el 766 de la referencia, que es lo que ella pidió.
 */
const MARCO = {
  /** Verticales del marco. Se conservan las del rectángulo aprobado (140 y 940). */
  izquierda: 140,
  derecha: 940,
  /** ⭐ Ronda 4: sube 210 px. El texto ya no se hunde en el centro de la caja. */
  y: 470,
  alto: 950,
  /**
   * Radio medido en la referencia ampliada al 200 %: la curva de la esquina
   * superior izquierda va de x≈232 a x≈290 ⇒ **≈56**. Antes iba en 48.
   */
  radio: 56,
  /**
   * ⭐ Ronda 2, y sigue vigente: en el borde superior de la referencia (y=298,
   * x=520) el píxel es **rgb(255,253,250)** y las filas vecinas están en 18 y
   * 12 ⇒ filete de **1 px, blanco PLENO**. Lo que había eran 2 px al 55 %, y
   * por eso se veía blando.
   */
  filete: 1,
} as const;

/** Pie del marco. */
const MARCO_PIE = MARCO.y + MARCO.alto;

/**
 * ⭐⭐ RONDA 4 — LAS DOS LECTURAS DE «QUE LA LÍNEA VAYA DE UNA ESQUINA A LA OTRA».
 *
 * Su marca roja extiende una horizontal del marco hasta el borde de la pieza, y
 * la referencia hace exactamente eso. Pero admite dos resoluciones, y las dos
 * son defendibles, así que se rinden LAS DOS y ella elige de una mirada:
 *
 * · `escuadras` — dos escuadras opuestas, que es lo que hay MEDIDO en el pin.
 *   La superior lleva su esquina redondeada arriba a la izquierda y su
 *   horizontal se va hasta el borde DERECHO; la inferior lleva la esquina
 *   abajo a la derecha y su horizontal se va hasta el borde IZQUIERDO. Cada
 *   línea nace en una esquina redondeada y muere en el canto del lienzo.
 *
 * · `lineas` — sólo las dos horizontales, de canto a canto, sin verticales.
 *   Es la lectura literal de la frase y la más cercana al tono declarado de la
 *   marca en el manual: «elegante, minimalista y sencillo».
 *
 * ⛔ Lo que NO se hace: dejar el rectángulo cerrado y colgarle un par de alas
 * hasta los bordes. Deja las curvas de las esquinas EN MEDIO de una línea
 * horizontal continua, y eso se lee como un error de trazado.
 */
export type VarianteMarco = 'escuadras' | 'lineas';

/**
 * Cuerpos.
 *
 * ⭐⭐ RONDA 6: LAS DOS LÍNEAS DEL TITULAR VAN AL MISMO CUERPO — 130.
 * «Me refería al tamaño de la tipografía, no a cambiar el grosor.» O sea que el
 * pedido de la ronda 5 («mismo peso») era **de tamaño**, y la ronda 5 lo leyó
 * como grosor: se le bajó el corte a Light y no era eso. El grosor vuelve a
 * **Medium**, que es como ella lo dejó en la ronda 3.
 *
 * ⛔ Y por lo tanto **la razón de cuerpos 1,62 de `C1 FT N1` (58/94) ya no rige
 * en esta pieza**: las dos líneas miden lo mismo y lo único que las distingue
 * es el peso. Vuelve a ser el recurso de DT de siempre —titular a dos pesos de
 * la misma familia— sólo que a un único cuerpo.
 *
 * · El subtexto se queda en 46 (ronda 4): normalizada a 1920, la referencia
 *   lleva su nivel más chico en ≈30 px de mayúscula y con 46 da ≈32.
 */
const CUERPO = {titulo1: 130, titulo2: 130, subtexto: 46} as const;

/**
 * ⭐ RONDA 3, y sigue siendo lo vigente: «el feliz día que sea menos grueso».
 * La línea de arriba va en **Medium (500)** — bajó de Bold, no más.
 *
 * ⛔ NO va en Light. La ronda 5 la pasó a Light leyendo «mismo peso» como
 * grosor, y Eli corrigió: hablaba del TAMAÑO. Se mantiene el recurso de la
 * marca —titular a DOS PESOS de la misma familia— y ahora a un mismo cuerpo.
 */
const PESO_TITULO_1 = DT.pesos.medium;

/**
 * Espaciado.
 *
 * · `tituloASubtexto: 74` — rondas 2 y 3. Regla `jerarquia-de-bloque-de-texto`:
 *   el salto ENTRE niveles va ~1,5× el salto DENTRO del nivel. Las dos líneas
 *   del titular son UN nivel y van pegadas (2 px).
 *
 * · ⭐ `sobreTitular: 215` — **ronda 4, y es el arreglo del «están muy abajo».**
 *   El bloque ya NO se centra vertical dentro del marco: se ancla arriba con
 *   este aire, y así la tinta del titular arranca en **y=685 = 35,7 %** de la
 *   altura, contra el 35,6 % de la referencia. Antes caía en el 48,5 %.
 *   Aire abajo resultante: 314 ⇒ razón 215/314 = 0,68, contra el 0,64 del pin.
 */
const AIRE = {entreTitulares: 2, tituloASubtexto: 74, interlineado: 1.3, sobreTitular: 215} as const;

/**
 * Dibuja un texto que lleva `¡` o `¿` en Stag, volteando el signo de apertura.
 * Es el truco de Eli; sin esto sale un tofu o Chrome cae a una serif de reemplazo.
 */
const TextoStag: React.FC<{
  texto: string;
  style: React.CSSProperties;
}> = ({texto, style}) => (
  <div style={{...style, whiteSpace: 'nowrap'}}>
    {volteaApertura(texto).map((t, i) =>
      t.flip ? (
        <span
          key={i}
          style={{display: 'inline-block', transform: 'rotate(180deg)'}}
        >
          {t.t}
        </span>
      ) : (
        <span key={i}>{t.t}</span>
      ),
    )}
  </div>
);

/**
 * El marco, en SVG. Se dibuja con `path` y no con `border` porque un borde de
 * CSS no puede SALIRSE de su propia caja, y salirse es justamente el pedido.
 *
 * `vectorEffect="non-scaling-stroke"` mantiene el filete en 1 px de la mesa al
 * escalar a 2250 — el mismo criterio con el que se midió en la ronda 2.
 */
const Marco: React.FC<{variante: VarianteMarco}> = ({variante}) => {
  const {izquierda: L, derecha: R, y: T, radio: r, filete} = MARCO;
  const B = MARCO_PIE;
  const trazo = {
    fill: 'none',
    stroke: DT.colores.blanco,
    strokeWidth: filete,
    vectorEffect: 'non-scaling-stroke' as const,
  };

  return (
    <svg
      width={1080}
      height={1920}
      viewBox="0 0 1080 1920"
      style={{position: 'absolute', top: 0, left: 0}}
    >
      {variante === 'escuadras' ? (
        <>
          {/*
            Escuadra SUPERIOR: sube por la vertical izquierda, dobla en la
            esquina redondeada y su horizontal se va hasta el borde DERECHO.
          */}
          <path d={`M ${L} 1100 L ${L} ${T + r} Q ${L} ${T} ${L + r} ${T} L 1080 ${T}`} {...trazo} />
          {/*
            Escuadra INFERIOR: baja por la vertical derecha, dobla abajo y su
            horizontal se va hasta el borde IZQUIERDO.
          */}
          <path d={`M ${R} 790 L ${R} ${B - r} Q ${R} ${B} ${R - r} ${B} L 0 ${B}`} {...trazo} />
        </>
      ) : (
        <>
          {/* Sólo las dos horizontales, de canto a canto. */}
          <path d={`M 0 ${T} L 1080 ${T}`} {...trazo} />
          <path d={`M 0 ${B} L 1080 ${B}`} {...trazo} />
        </>
      )}
    </svg>
  );
};

export const DtStTurismo: React.FC<{guia?: boolean; variante?: VarianteMarco}> = ({
  guia = false,
  variante = 'escuadras',
}) => (
  <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
    {/* 1 · La foto real del frontis, a sangre */}
    <Img
      src={staticFile('assets/hilton/dt/st-turismo-frontis.jpg')}
      style={{width: '100%', height: '100%', objectFit: 'cover'}}
    />

    {/*
      2 · El velo azul.

      ⭐⭐ RONDA 5 (10-09): «BAJA LA OPACIDAD ARRIBA, SE VE MUY FORZADO. LA
      TRANSPARENCIA DEBE SER DE 0 ARRIBA Y AJUSTAR.»

      Tenía razón y el defecto era mío: la rampa de la ronda 4 se quedaba plana
      en 0 hasta el 21 % y de ahí saltaba a 0,44 en el 33 %. Ese codo es una
      banda visible — el velo «empezaba» en un punto en vez de nacer.

      Ahora **arranca en 0 en el borde de arriba** y sube cóncava: pendiente
      constante en el tercio superior y se va aplanando hacia el pie, que es el
      comportamiento de una luz y no de una máscara. Paradas cada ~10 % para que
      no quede ningún quiebre a la vista.

      ⭐ Y el pie queda en **0,58**, más CLARO que el 0,66 que ella aprobó en la
      ronda 2: se ve más foto que antes, arriba y abajo.

      ⚠️ EL LÍMITE, MEDIDO, PORQUE ACÁ HAY UNA TENSIÓN REAL. El titular está en
      el 36-46 % de la altura, o sea sobre la punta dorada del edificio y el
      cielo: lo más claro de la foto. Con el velo naciendo en 0 no se puede
      cargar esa banda sin volver a forzar la parte de arriba. Lo verificado:

      | rampa | «¡Feliz Día» |
      |---|---|
      | lineal 0→0,80 | 2,88:1 — no llega |
      | lineal 0→1,00 (¡pie opaco!) | 3,43:1 |
      | **ésta, cóncava, pie 0,58** | **3,61:1** |

      El umbral que corresponde es **3:1**, no 4,5: el titular va a cuerpo 80 y
      130 px y eso es texto grande (≥24 px). El subtexto, que es el más chico,
      se queda con la vara de 4,5 y da 5,49:1.

      ⛔ Y se descartó reencuadrar, que era la otra salida: se barrieron los 25
      encuadres 9:16 posibles de `HDT_43` y el mejor deja el titular en 2,60:1
      sin velo. No hay ventana en esta toma donde el titular caiga sobre zona
      oscura — el edificio no llega tan arriba.
    */}
    <AbsoluteFill
      style={{
        background:
          `linear-gradient(to bottom,` +
          ` rgba(9,25,78,0) 0%,` +
          ` rgba(9,25,78,0.11) 10%,` +
          ` rgba(9,25,78,0.22) 20%,` +
          ` rgba(9,25,78,0.33) 30%,` +
          ` rgba(9,25,78,0.42) 40%,` +
          ` rgba(9,25,78,0.48) 50%,` +
          ` rgba(9,25,78,0.52) 60%,` +
          ` rgba(9,25,78,0.55) 72%,` +
          ` rgba(9,25,78,0.57) 86%,` +
          ` rgba(9,25,78,0.58) 100%)`,
      }}
    />

    {/*
      2b · ⛔ EL RÓTULO DEL PROPIO EDIFICIO.
      La torre lleva su letrero vertical «DOUBLETREE» en la fachada, y cae
      justo detrás del titular (medido: tinta metálica de luminancia 229 sobre
      una columna de 134, alrededor de x 690-730, y 1230-1400 @1080).

      En la ronda 1 lo tapaba el velo fuerte. Al bajarlo —que es lo que pidió
      Eli para que se viera la foto— volvió a leerse, y ahí sí es un defecto:
      es «el logotipo del local detrás del titular», y además REPITE el logo que
      ya va arriba.

      La salida NO es volver a subir el velo de toda la pieza: es una sombra
      SUAVE y LOCAL, con caída amplia para que se lea como el degradado natural
      de la luz y no como una mancha. El resto de la foto —los árboles, la
      calle, el edificio vecino— se mantiene visible.
    */}
    <AbsoluteFill
      style={{
        background:
          'radial-gradient(ellipse 330px 300px at 700px 1300px,' +
          ' rgba(9,25,78,0.62) 0%,' +
          ' rgba(9,25,78,0.42) 45%,' +
          ' rgba(9,25,78,0) 100%)',
      }}
    />

    {/*
      3 · Logotipo principal, CENTRADO y en AZUL DoubleTree (§B.4: el cielo es
      demasiado claro para el blanco). Geometría de la plantilla `logo-ST.png`.
    */}
    <Img
      src={staticFile('assets/hilton/dt/logo-dt-azul.png')}
      style={{
        position: 'absolute',
        top: G.logoYStory,
        left: (1080 - G.logoAnchoStory) / 2,
        width: G.logoAnchoStory,
        height: G.logoAnchoStory / G.logoProporcion,
      }}
    />

    {/* 4 · El marco — ronda 4: sus horizontales salen por los bordes */}
    <Marco variante={variante} />

    {/*
      5 · El saludo. ⭐ RONDA 4: el bloque se ANCLA ARRIBA (`flex-start` + el
      aire medido), no se centra en la caja. Centrado, con un marco de 950 de
      alto, la tinta del titular se hundía hasta el 48,5 % de la pieza — que es
      el «están muy abajo» de Eli. Anclado arriba cae en el 35,7 %, que es donde
      lo pone la referencia (35,6 %).
    */}
    <div
      style={{
        position: 'absolute',
        left: MARCO.izquierda,
        top: MARCO.y,
        width: MARCO.derecha - MARCO.izquierda,
        height: MARCO.alto,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'flex-start',
        paddingTop: AIRE.sobreTitular,
        boxSizing: 'border-box',
      }}
    >
      <TextoStag
        texto={TITULO_1}
        style={{
          fontFamily: DT.fuentes.titular,
          fontWeight: PESO_TITULO_1,
          fontSize: CUERPO.titulo1,
          lineHeight: 1,
          color: DT.colores.blanco,
        }}
      />
      <TextoStag
        texto={TITULO_2}
        style={{
          fontFamily: DT.fuentes.titular,
          fontWeight: DT.pesos.light,
          fontSize: CUERPO.titulo2,
          lineHeight: 1.12,
          letterSpacing: '0.03em',
          color: DT.colores.blanco,
          marginTop: AIRE.entreTitulares,
        }}
      />
      <div
        style={{
          fontFamily: DT.fuentes.texto,
          fontWeight: 400,
          fontSize: CUERPO.subtexto,
          lineHeight: AIRE.interlineado,
          color: DT.colores.blanco,
          textAlign: 'center',
          /* Con cuerpo 46 la línea larga necesita más caja que los 690 de antes. */
          maxWidth: 780,
          marginTop: AIRE.tituloASubtexto,
          opacity: 0.94,
        }}
      >
        {SUBTEXTO.map((linea) => (
          <div key={linea}>{linea}</div>
        ))}
      </div>
    </div>

    {/* 6 · Guía de zonas seguras — sólo para revisar, NO se entrega */}
    {guia ? (
      <>
        <div
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: 1080,
            height: DT.seguras.story.arriba,
            background: 'rgba(255,0,110,0.22)',
            borderBottom: '2px dashed rgba(255,0,110,0.9)',
          }}
        />
        <div
          style={{
            position: 'absolute',
            bottom: 0,
            left: 0,
            width: 1080,
            height: DT.seguras.story.abajo,
            background: 'rgba(255,0,110,0.22)',
            borderTop: '2px dashed rgba(255,0,110,0.9)',
          }}
        />
      </>
    ) : null}
  </AbsoluteFill>
);

export const DtStTurismoGuia: React.FC = () => <DtStTurismo guia />;
