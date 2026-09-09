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
 * LA REJILLA (1080×1920; se entrega a 2250×4000, ×2,0833)
 * ══════════════════════════════════════════════════════════════════════════
 *    250 ─ fin de la zona segura superior de Instagram
 *    241 ─ tope del logotipo  ← plantilla `logo-ST.png` de Eli
 *    377 ─ pie del logotipo
 *    680 ─ tope del marco redondeado (ronda 3: subió y creció, marca de Eli)
 *   1560 ─ pie del marco (alto fijo 880)
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
  ancho: 800,
  y: 680,
  alto: 880,
  radio: 48,
  filete: 1,
} as const;

/**
 * Cuerpos del titular. **Ronda 2: Eli lo vio chico y se subió.**
 * La referencia compone «Crafting» a **700 px de ancho sobre 1080 (65 %)**;
 * la ronda 1 iba en 540 (50 %). Con cuerpo 116 la línea grande mide 666 px
 * (**61,7 %**) y deja 50 px de aire a cada lado dentro del marco — se queda un
 * punto por debajo de la referencia, que lleva el titular casi al ras del filete.
 *
 * ⭐ La proporción entre las dos líneas se mantiene en **1,62**, que es la de la
 * marca medida en `C1 FT N1` (58 / 94). Se subieron las dos juntas, no una.
 */
const CUERPO = {titulo1: 80, titulo2: 130, subtexto: 38} as const;

/**
 * ⭐ RONDA 3: «el feliz día que sea menos grueso».
 * La línea de arriba baja de **Bold (700) a Medium (500)**. Se mantiene el
 * recurso de la marca —titular a DOS PESOS de la misma familia— y se mantiene
 * el orden de DT (arriba la chica, abajo la grande y liviana); lo que cambia es
 * cuánto pesa la de arriba.
 */
const PESO_TITULO_1 = DT.pesos.medium;

/**
 * Espaciado. **Ronda 2: Eli pidió ajustarlo.**
 * Regla `jerarquia-de-bloque-de-texto`: el salto ENTRE niveles tiene que ser
 * ~1,5× el salto DENTRO del nivel. El interlineado del subtexto es 30 × 1,3 =
 * 39, así que el salto del titular al subtexto va en **58** (≈1,5×). Antes era
 * 30 — más chico que el salto interno, o sea la jerarquía al revés.
 * Las dos líneas del titular son UN nivel: van pegadas (2 px).
 */
const AIRE = {entreTitulares: 2, tituloASubtexto: 74, interlineado: 1.3} as const;

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

export const DtStTurismo: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
    {/* 1 · La foto real del frontis, a sangre */}
    <Img
      src={staticFile('assets/hilton/dt/st-turismo-frontis.jpg')}
      style={{width: '100%', height: '100%', objectFit: 'cover'}}
    />

    {/*
      2 · El velo azul que sube desde abajo — el recurso de las piezas
      aprobadas. Arranca transparente en el 42 % para no tocar el cielo ni el
      logotipo, y llega al 0,94 al borde inferior.
    */}
    <AbsoluteFill
      style={{
        background:
          `linear-gradient(to bottom,` +
          ` rgba(9,25,78,0) 28%,` +
          ` rgba(9,25,78,0.20) 40%,` +
          ` rgba(9,25,78,0.44) 50%,` +
          ` rgba(9,25,78,0.58) 64%,` +
          ` rgba(9,25,78,0.66) 100%)`,
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

    {/* 4 · El marco de esquinas redondeadas con el saludo adentro */}
    <div
      style={{
        position: 'absolute',
        left: (1080 - MARCO.ancho) / 2,
        top: MARCO.y,
        width: MARCO.ancho,
        height: MARCO.alto,
        border: `${MARCO.filete}px solid ${DT.colores.blanco}`,
        borderRadius: MARCO.radio,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
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
          maxWidth: MARCO.ancho - 110,
          marginTop: AIRE.tituloASubtexto,
          opacity: 0.94,
        }}
      >
        {SUBTEXTO.map((linea) => (
          <div key={linea}>{linea}</div>
        ))}
      </div>
    </div>

    {/* 5 · Guía de zonas seguras — sólo para revisar, NO se entrega */}
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
