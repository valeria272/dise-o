/**
 * BETWEEN — S5 · LAS DOS STORIES DE LA SEMANA 5 (28 y 30 de septiembre)
 *
 * Las dos últimas columnas de la hoja STORIES de la grilla
 * (`1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY`, leída EN VIVO por CSV el 11-09-2026,
 * `gid=1367300884` — el `.xlsx` está congelado, ver el manual):
 *
 *   col T · 28-09 · OK PARA DISEÑAR · «ST ESTÁTICA – HUMOR | CAFÉ TO GO»
 *   col U · 30-09 · OK PARA DISEÑAR · «ST ESTÁTICA – ANIMADA | PLATEADA AL CARMENERE»
 *
 * Encargo de Eli, 11-09-2026: «una es estática y otra es animada "video" […]
 * no deben durar más de 15 segundos […] puede ser mínimo de 8 a 9 segundos […]
 * recuerdes las reglas de los vasos TOGO, que se vea realista».
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⛔ ESTAS DOS PIEZAS YA EXISTÍAN, Y POR ESO SE REHICIERON
 * ══════════════════════════════════════════════════════════════════════════
 * El lote de 27 del 27-08 las incluía (`StHumorToGo` y `StPlateada` de
 * `BetweenSeptiembre.tsx`), y quedaron en Drive. Nunca pasaron por ninguna de
 * las 13 rondas posteriores, así que arrastran los defectos que el cliente ya
 * corrigió en las demás:
 *
 * | | v0 del 27-08 | acá |
 * |---|---|---|
 * | vaso To Go | kraft **SIN logotipo** — el reclamo que el cliente hizo TRES veces | logotipo real estampado |
 * | lugar | muro de estuco crema con teja y platanera: **no es Between** | el patio real (pizarra + teca + jardín vertical) |
 * | plateada | carne en **cubos**, inventada | la **foto real de Between**: plato blanco, puré a la ciboulette, rábano |
 * | col U | PNG estático | **video de 9 s**, que es lo que pide la grilla |
 * | contraste del beige | 1,4–1,9:1 (ilegible, sostenido por cajas) | 8,1–16,0:1 medido por tercios |
 *
 * Las dos escenas se PRODUJERON con el método de Eli
 * (`clients/hilton/PROMPTS-DE-ELI.md`) en un espacio de Magnific abierto para
 * la semana, con Nano Banana Pro 9:16 · 4K y las fotos reales como referencia.
 * Los prompts, vuelta por vuelta, están en `scripts/between-st-s5-generar.md`.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐⭐ RONDA 2 (11-09, tarde) — ELI MANDÓ DOS SESIONES Y LAS DOS PIEZAS CAMBIARON
 * ══════════════════════════════════════════════════════════════════════════
 * > «en esta carpeta puedes encontrar platos de Between […] creo que acá puedes
 * > encontrar referente del plato o el mismo plato. Para la historia del vaso
 * > togo estática el vaso se ve muy falso y mal el logo. Hazlo más realista y
 * > acerca más a la chica y el vaso, para que el fondo pase a 2do plano.»
 *
 * **30-09 · el plato ESTABA, y era muy distinto del que se había usado.**
 * `Between-131` a `143` de la sesión de platos (carpeta `18SrYXjLYVv…`): plato
 * **BLANCO** redondo, trozos de carne braseada en salsa de vino, puré
 * espolvoreado con **ciboulette**, hojas verdes y dos rodajas de **rábano**. El
 * de QB que se había usado de referencia iba en loza de borde turquesa y con
 * champiñones — nada que ver. Se le pidió al generador cambiar **sólo el
 * plato** y dejar idéntico el resto de la escena, que ya estaba aprobada.
 * ⭐ Y como el plato ocupa el mismo sitio, **la diagramación no se movió**: la
 * banda limpia sigue llegando a y=1058 y el contraste quedó en 12,3–15,8:1.
 *
 * **28-09 · el vaso se veía falso porque el cartón estaba mal.** El generado
 * era kraft anaranjado y liso. El real —`Double Tree 25 jul 25-248.jpg`,
 * recortado de cerca— es **crema pálido con la fibra y las motas a la vista**,
 * borde superior enrollado, **costura vertical**, **anillo blanco** en la base y
 * tapa negra de domo con **nervaduras concéntricas**. Esa lista va en el prompt
 * uno por uno: pedir «cartón kraft» no alcanza, hay que nombrar las piezas.
 *
 * ⭐ **Acercar la cámara le quita sitio al titular, y hay que devolvérselo.**
 * Con el plano cerrado que pidió Eli, la banda limpia se desplomó a **y=443**
 * (el vaso entraba por arriba) y el bloque de texto no cabía. Se resolvió con
 * una vuelta más pidiendo la **cámara apuntando más arriba**: el vaso baja, la
 * tapa queda a media altura y la banda limpia vuelve a **y=960**. El vaso sigue
 * igual de cerca; lo que se movió es el encuadre, no la distancia.
 *
 * ⭐ **El logotipo pasó de 133 a 274 px de ancho** sobre el lienzo de 1080,
 * porque el vaso ocupa el doble. Va **entre la tapa y el brazo** y eso es
 * medido, no estético: a media altura del vaso —donde está en la foto real— lo
 * cruza el brazo, y más abajo cae dentro de la zona segura inferior, donde
 * Instagram pone su barra. La franja limpia entre la tapa y la mano es el único
 * sitio donde se ve entero y nada lo tapa.
 *
 * ⛔ **Los frames 336 · 337 · 338 · 339 de esa sesión siguen vetados.** Son
 * packshots frontales del vaso sobre fondo blanco y parecen la solución, pero
 * son del **vaso ANTIGUO** (cuerpo oscuro con faja de papel). Confirmado otra
 * vez mirándolos.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * DE DÓNDE SALE CADA IMAGEN, Y QUÉ ES REAL EN CADA UNA
 * ══════════════════════════════════════════════════════════════════════════
 * · **28-09 · el VASO es el real, y el logotipo es el archivo oficial.**
 *   Referencias: `togo-vaso-real-nobg.png` (el recorte del vaso vigente) y
 *   `Double Tree 25 jul 25-257.jpg`. El escenario es el patio real de Between
 *   (`espacios/HDT_49.jpg`): muro de pizarra, mesas y sillas de listones de
 *   teca, jardín vertical.
 *   ⭐ **El generador devolvió el vaso LISO, a propósito**, y el logotipo se
 *   estampó después con `scripts/between-s5-logo-vaso.py`. Es la regla del
 *   manual: «se pide el vaso sin marca y se estampa el real». En las dos
 *   primeras vueltas Nano Banana escribió un «BETWEEN» inventado en una sans
 *   cualquiera, sin la Ǝ invertida — exactamente el defecto de la ronda 4.
 *   El logotipo va **rotado 5° y envuelto al cilindro** (ronda 3): rotación
 *   RÍGIDA más proyección cilíndrica medida, proporción 3,0278 intacta.
 *   ⚠️ **La chica no muestra la cara**: el vaso se la tapa. Es lo que hace la
 *   referencia que eligió contenido y de paso deja la pieza fuera del problema
 *   de los rostros.
 *
 * · ✅ **30-09 · el PLATO es el de Between** (ronda 2). Referencias:
 *   `Between-135` (vertical, el plato entero sobre mesa de madera) y
 *   `Between-141` (primer plano del producto), de la sesión de platos que mandó
 *   Eli. ⛔ La ronda 1 usaba `Quotidien-176.jpg res al carmenere`, de la sesión
 *   de **QB**, y estaba mal: ese plato va en loza de borde turquesa y con
 *   champiñones. El de Between es plato BLANCO, con puré a la ciboulette,
 *   hojas verdes y rábano.
 *   ⚠️ **La lección de método:** se dio por inexistente una foto que sí
 *   existía. Se había buscado en `platos-ene` (31 archivos en disco) y no en
 *   las **202 miniaturas** de la misma carpeta, que son la sesión completa.
 *   Antes de decir «no hay foto», mirar la sesión ENTERA en hoja de contacto.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐ RONDA 3 (11-09, tarde) — LA ANIMADA APROBADA, Y EL DETALLE DEL VASO
 * ══════════════════════════════════════════════════════════════════════════
 * > «La historia número dos animada queda aprobada. La número uno tiene un leve
 * > problema en el vaso. Tienes que borrar esa línea que se ve y que el logo se
 * > vea más centrado al vaso, como un mockup. El logo debe verse realista que
 * > está en el vaso, como los originales. El tamaño está ideal del vaso y
 * > también está bien las tipografías y la persona.»
 *
 * **La del 30-09 quedó APROBADA** y no se tocó.
 *
 * ⛔ **La línea la pedí yo.** El prompt de la ronda 2 traía «una costura
 * vertical del cartón» dentro de la lista de detalles físicos que arreglaron el
 * realismo, y el generador la puso **justo al medio de la cara visible**,
 * partiendo el logotipo en «BETW | EEN». En el vaso real esa costura existe pero
 * cae al costado.
 * ⭐⭐ **Regla: a un generador, los detalles DIRECCIONALES hay que ubicarlos.**
 * «Costura», «etiqueta», «asa», «pliegue» — sin un «al costado, fuera de la cara
 * principal» van a parar donde más estorban.
 * Se borra con `scripts/between-s5-vaso-costura.py`, que reconstruye la franja
 * fila a fila interpolando el cartón de sus dos costados y le devuelve el grano.
 * Medido: la caída de luminancia en esa columna pasó de **−13,2 a −2,8**.
 *
 * ⭐⭐ **«Se ve descentrado» no era el logotipo, era la línea.** Estaba en
 * x=1800 y el eje real del vaso está en **x≈1750**: 50 px sobre 1900 de ancho,
 * un 2,6 %. Lo que se leía corrido era el conjunto *logotipo + línea*, porque la
 * costura dejaba un paño ancho a la izquierda y uno angosto a la derecha.
 *
 * ⚠️ **Y el eje de un objeto ocluido se mide donde NO está ocluido.** El borde
 * izquierdo del vaso lo tapa el brazo, así que un detector de cartón sobre esa
 * fila toma el fondo oscuro por vaso y devuelve un centro corrido 200 px — se
 * llegó a estampar sobre ese valor falso. El eje bueno lo da **la tapa**, que es
 * lo único que se ve entero.
 *
 * ⭐ **La envoltura cilíndrica** (`--radio` de `between-s5-logo-vaso.py`): el
 * logotipo se trata como impreso sobre la superficie, así que su ancho es un
 * ARCO y lo que se ve es la CUERDA. **No contradice la regla del 31-08**: el
 * radio se MIDE del propio vaso (948 px), la línea de base queda RECTA y la
 * compresión es del 8 % en el borde y progresiva — contra la sinusoide inventada
 * con 18 % fijo que dejaba «COFFEE & BAR» irreconocible.
 * Parámetros finales: `--centro 1755 3870 --ancho 780 --angulo -5 --radio 948`.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LO INTERACTIVO: ZONA RESERVADA, NUNCA DIBUJADA
 * ══════════════════════════════════════════════════════════════════════════
 * Cuarta vez que Eli lo dice (07-09, 08-09, 09-09 y sigue vigente): el sticker
 * lo pone el CM al publicar, con el sticker REAL de Instagram. La pieza deja la
 * zona limpia y se entrega además una copia `GUIA CM` que NO se sube al Drive.
 *
 *   28-09 → la grilla **no pide interacción** en esta columna. No hay zona.
 *   30-09 → `INTERACCIÓN: LINK CARTA` → 340 × 140 en y=990, CENTRADA. La
 *           medida sale del ÚLTIMO frame, no del primero: con el acercamiento
 *           el plato sube y el corredor libre se encoge de ~300 px a 175 px.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL LOGOTIPO DE MARCA: EN UNA SÍ Y EN LA OTRA NO
 * ══════════════════════════════════════════════════════════════════════════
 * · **28-09 va SIN lockup.** El vaso gigante trae el logotipo impreso y ocupa
 *   media pieza: repetirlo arriba lo dice dos veces. Es la regla 8 de la
 *   gramática y la orden textual de Eli en la ronda 9 («borra el logo
 *   principal ya que está en el vaso TO GO»). Al no haber lockup, el bloque
 *   sube de y=441 a **y=300**, igual que las dos del cumpleaños.
 * · **30-09 va CON lockup arriba.** El plato no firma nada.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REJILLA (1080×1920, se entrega a 2250×4000 · el video a 1080×1920)
 * ══════════════════════════════════════════════════════════════════════════
 *    250 ─ zona segura superior de Meta
 *    271 ─ wordmark del lockup (sólo la del 30-09)
 *    300 ─ primera línea de tinta de la del 28-09 (sin lockup)
 *    441 ─ primera línea de tinta de la del 30-09 (`BETWEEN.bloque.yStory`)
 *   1580 ─ empieza la zona segura inferior
 *
 * Las bandas limpias salen de medir el contraste del beige `#FFF9EB` fila a
 * fila sobre la columna de 810, con el percentil 90 de luminancia (el peor
 * caso), no con el promedio:
 *
 * | | banda limpia | contraste en la banda |
 * |---|---|---|
 * | 28-09 | y=240 a **879** | 8,1 – 14,8:1 |
 * | 30-09 | y=240 a **1058** | 10,6 – 16,0:1 |
 *
 * Por eso las dos van con `oscurecer` 0: la escena ya nace con el hueco
 * oscuro adentro y un multiply encima sólo apagaría el vaso o el plato, que es
 * lo que la pieza está mostrando.
 */
import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  OffthreadVideo,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
import {
  Bajada,
  CajaDato,
  FotoFondo,
  LogoBetween,
  TitularBetween,
} from './BetweenSistema';

const F = 'assets/hilton/between/s5/';

/* ══════════════════════════════════════════════════════════════════════════
   LA ZONA RESERVADA — mismo aparato que `BetweenStS3.tsx` y `BetweenStS4.tsx`.
   Sólo se pinta en la copia `GUIA CM`.
   ══════════════════════════════════════════════════════════════════════════ */
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

/** Cierre en cursiva, como el de `BetweenStS4.tsx`. */
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
   ST 28-09 · HUMOR | CAFÉ TO GO  (col T · OK PARA DISEÑAR)

   Textos LITERALES de la grilla:
     · «Texto principal: POV: / YO CARGANDO EL PESO / DE MIS GANAS DE CAFÉ.»
   La columna no trae fila de INTERACCIÓN, así que no hay zona reservada.

   ⭐ EL PUNTO FINAL NO VA: «los títulos nunca llevan punto final» (regla de
   Eli). `TitularBetween` lo saca solo — no se le pasa `mantenerPunto`.

   ⭐ EL CORTE DE LÍNEA ES EL DEL BRIEF, y el cuerpo sale de ahí.
   «DE MIS GANAS DE CAFÉ» son 20 caracteres, así que en la columna de 810 el
   `ajustarACaber` baja el titular bastante por debajo del token de 117. Se
   respeta igual: el corte en dos líneas es el ritmo del chiste y el texto va
   literal. Para compensar, el bloque usa el ancho MÁXIMO que permite el manual
   —912 px, o sea los 84 px de margen lateral mínimo a cada lado— en vez de la
   columna de 810.
   ══════════════════════════════════════════════════════════════════════════ */

/** 1080 − 2 × 84 (margen lateral mínimo del manual). */
const ANCHO_MAXIMO = 1080 - 2 * BETWEEN.bloque.margenX;

export const StS5HumorToGo: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    {/* `oscurecer` 0: la banda del titular ya da 8,1–14,8:1. Un multiply
        encima sólo apagaría el cartón kraft del vaso, que es el protagonista. */}
    <FotoFondo src={F + 'st-28-09-togo.jpg'} oscurecer={0} />

    {/* SIN `LogoBetween`: el vaso ya trae el logotipo impreso (regla 8). */}

    <Columna top={300}>
      <TitularBetween
        script="POV:"
        caps={'Yo cargando el peso\nde mis ganas de café'}
        alinear="centro"
        tono="beige"
        anchoDisponible={ANCHO_MAXIMO}
      />
    </Columna>
  </AbsoluteFill>
);

/** La copia con la rejilla de medición, sólo para revisar. No se entrega. */
export const StS5HumorToGoGuia: React.FC = () => (
  <AbsoluteFill>
    <StS5HumorToGo />
    <ZonaReservada
      zona={{ancho: 912, alto: 580, top: 300}}
      etiqueta={'BANDA LIMPIA MEDIDA\ny=300 a 880 · 8,1–14,8:1'}
    />
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   ST 30-09 · PLATEADA AL CARMENERE  (col U · OK PARA DISEÑAR) · ANIMADA

   Textos LITERALES de la grilla:
     · «Texto principal: ¿EL ALMUERZO SE QUEDÓ EN CASA?»
     · «Tranqui, el plan B / se ve bastante mejor por acá.»
     · «Plateada al Carmenere»
     · «Cierre / CTA: Haz tu pausa de almuerzo en Between.»
     · «INTERACCIÓN: LINK CARTA» → zona reservada, no se dibuja.

   ⭐ 9 SEGUNDOS, y el número sale del encargo. Eli: «no deben durar más de 15
   segundos […] puede ser mínimo de 8 a 9 segundos». 9 s × 30 fps = 270 frames.

   ⭐ EL MOVIMIENTO ES DE LA FOTO, NO DEL TEXTO QUE BAILA.
   El fondo es un clip real generado desde la MISMA fotografía fija que se
   midió: acercamiento lentísimo, el vapor que sube de la carne y las hojas del
   fondo moviéndose apenas. Todo lo demás está quieto. El texto sólo entra —no
   rebota, no gira, no hace efecto— porque la marca es «juvenil pero con un
   punto de estatus» y una tipografía que se mueve la abarata.

   Los tiempos de entrada, escalonados, en frames:
     ·   0–18  el titular (script + caja alta)
     ·  14–32  la bajada
     ·  28–46  la caja taupe del producto
     ·  42–60  el cierre
   Los 210 frames restantes la pieza queda quieta y legible, que es lo que hace
   falta para leerla en una historia.
   ══════════════════════════════════════════════════════════════════════════ */

export const DURACION_PLATEADA = 270;           // 9 s a 30 fps

/** ⭐ LA ZONA DEL ENLACE SE MIDE EN EL ÚLTIMO FRAME, NO EN EL PRIMERO.
 *
 * Es la diferencia con una pieza estática y costó rehacerla: la cámara hace un
 * acercamiento durante los 9 s, así que el plato SUBE dentro del cuadro y lo
 * que al empezar era mesa limpia al terminar es loza. Midiendo el borde del
 * plato cuadro a cuadro, el corredor libre entre el cierre del bloque (y≈965)
 * y el plato pasa de ~300 px al principio a **175 px al final** (y=965 a
 * y=1140). La pastilla se dimensiona contra ESE peor caso.
 *
 * Va CENTRADA —a diferencia de la del 22-09, donde la copa ocupaba el eje y
 * tuvo que irse al canal izquierdo—: acá la mesa de teca cruza limpia de lado
 * a lado y lo único que hay son el notebook cerrado, el celular y los anteojos,
 * que son elementos de fondo. La regla es que la zona no lleve gráfica NUESTRA,
 * no que la foto esté vacía.
 *
 * 340 × 140 en y=990 deja 25 px de aire con el cierre y 10 px con el plato en
 * el frame más cerrado. */
const ZONA_ENLACE: Zona = {ancho: 340, alto: 140, top: 990};

/** Entrada suave: opacidad + 28 px de subida, con easing de salida. */
const useEntrada = (desde: number, largo = 18) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [desde, desde + largo], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const suave = 1 - Math.pow(1 - t, 3);
  return {opacity: suave, transform: `translateY(${(1 - suave) * 28}px)`};
};

const Entra: React.FC<{desde: number; children: React.ReactNode}> = ({desde, children}) => (
  <div style={{...useEntrada(desde), width: '100%', display: 'flex', justifyContent: 'center'}}>
    {children}
  </div>
);

export const StS5Plateada: React.FC<{guia?: boolean}> = ({guia = false}) => {
  const {durationInFrames} = useVideoConfig();

  return (
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
      <AbsoluteFill>
        <OffthreadVideo
          src={staticFile(F + 'st-30-09-plateada.mp4')}
          style={{width: '100%', height: '100%', objectFit: 'cover'}}
          muted
        />
      </AbsoluteFill>

      {/* El lockup entra con la pieza, no aparece de golpe. */}
      <div style={useEntrada(0, 22)}>
        <LogoBetween formato="story" posicion="arriba" tono="beige" />
      </div>

      <Columna top={BETWEEN.bloque.yStory}>
        <Entra desde={0}>
          <TitularBetween
            script="¿El almuerzo"
            caps="Se quedó en casa?"
            alinear="centro"
            tono="beige"
            anchoDisponible={BETWEEN.bloque.columna}
          />
        </Entra>

        <Entra desde={14}>
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
            {'Tranqui, el plan B\nse ve bastante mejor por acá.'}
          </Bajada>
        </Entra>

        {/* UNA sola caja taupe: es el énfasis, y el énfasis es el producto. */}
        <Entra desde={28}>
          <div style={{marginTop: BETWEEN.aire.tituloACaja}}>
            <CajaDato anchoDisponible={BETWEEN.bloque.columna}>Plateada al Carmenere</CajaDato>
          </div>
        </Entra>

        {/* ⭐ EL CIERRE ENTRA AL BLOQUE DE ARRIBA, no al pie — mismo motivo que
            en la del 22-09: abajo está el plato, y el texto de la marca se
            apoya en el fondo, nunca sobre el producto. */}
        <Entra desde={42}>
          <Cierre style={{marginTop: 26}}>Haz tu pausa de almuerzo en Between.</Cierre>
        </Entra>
      </Columna>

      {guia ? (
        <>
          <ZonaReservada zona={ZONA_ENLACE} etiqueta={'LINK CARTA\n340 × 150'} />
          <div
            style={{
              position: 'absolute',
              left: 0,
              right: 0,
              top: 1580,
              height: 1920 - 1580,
              borderTop: '3px dashed rgba(255,45,141,0.6)',
            }}
          />
          <div
            style={{
              position: 'absolute',
              left: 24,
              top: 1600,
              color: '#ff2d8d',
              fontFamily: BETWEEN.fuentes.sans,
              fontWeight: 700,
              fontSize: 24,
            }}
          >
            {`zona segura inferior de Meta · ${durationInFrames} frames = ${(durationInFrames / 30).toFixed(0)} s`}
          </div>
        </>
      ) : null}
    </AbsoluteFill>
  );
};

export const StS5PlateadaGuia: React.FC = () => <StS5Plateada guia />;
