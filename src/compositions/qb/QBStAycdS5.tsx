/**
 * QB · HISTORIA ANIMADA — «ALL YOU CAN DRINK» (STORIES · 28-09 · 15:00)
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL — grilla viva de QB, hoja STORIES, columna del 28 sept
 * ══════════════════════════════════════════════════════════════════════════
 * Estado: **OK PARA DISEÑAR**. Leído por `export?format=csv&gid=49019995`.
 *
 *     ST ESTÁTICA – ALL YOU CAN DRINK | QB
 *
 *     Visual: Inspirarse directamente en la composición de la referencia adjunta.
 *     Fotografía vertical de unas manos sosteniendo un celular en primer plano.
 *     El teléfono debe ocupar gran parte de la pieza y ser el foco principal.
 *     Dentro de la pantalla del celular aparece una fotografía atractiva de uno
 *     de los tragos seleccionados de QB, idealmente en close up, con la promoción
 *     integrada como parte del diseño.
 *     El fondo puede ser una mesa o sector del restaurant, desenfocado, con
 *     elementos que den contexto al panorama: otro trago, plato para compartir o
 *     parte de la terraza.
 *     Sumar tipografía blanca de gran tamaño en el fondo, parcialmente cortada
 *     por los bordes y por el celular, siguiendo el recurso editorial de la
 *     referencia. Puede utilizarse la palabra: UNLIMITED
 *
 *     Texto dentro del celular:
 *       ALL YOU CAN DRINK · $13.990 · Martes · 18:00 a 21:00 hrs.
 *       Tragos seleccionados ilimitados.
 *     Texto complementario pequeño: Los números están claros.
 *     CTA: Reserva tu mesa.
 *     Legal: Sujeto a consumo de alimentos. Promoción no acumulable con otras
 *     promociones y beneficios.
 *
 * ⛔ **El comentario «Muy parecido al de BT, busquemos otra referencia» está
 * TACHADO en la grilla: contenido ya lo resolvió y NO se toma en cuenta.**
 * (Eli, 17-09-2026.) La ronda 1 lo leyó como vigente y sacó el celular de la
 * pieza — estaba mal. El celular es el centro del brief y va.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LO QUE PIDIÓ ELI EL 17-09-2026
 * ══════════════════════════════════════════════════════════════════════════
 *   · «debe ser en un celular la gráfica y guíate del brief»
 *   · «la referencia es por el celular y la escena»
 *   · «UNLIMITED este texto debajo estilo la referencia. **Que se note**»
 *   · «que lo que se vea en el celular sea estático, **sólo el texto de UNLIMITED
 *      en movimiento, nada más**»
 *   · «el legal que esté **fuera** del celular, que no se lee»
 *   · y de antes: «botón verde con efecto de degradado y logo + el nombre NO
 *      [varían]»
 *
 * ⇒ De ahí salen las cuatro decisiones de esta pieza:
 *   1. La pieza **entera** está quieta. Lo único que se mueve son las tres
 *      bandas de UNLIMITED. Nada de acercamientos ni de entradas escalonadas.
 *   2. Las bandas pasan **por detrás del celular** — van entre el fondo y la
 *      capa de frente. Así quedan «cortadas por los bordes y por el celular»,
 *      literal.
 *   3. La promo vive **dentro de la pantalla**, con el bloque de marca medido
 *      del KV (composición `QB-Pantalla-AYCD`).
 *   4. El legal, el CTA y la línea complementaria van **fuera del teléfono**,
 *      en el pie.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LAS CAPAS — se arman con `scripts/qb-aycd-s5-montar.py`
 * ══════════════════════════════════════════════════════════════════════════
 *   `aycd-s5-fondo.jpg`   escena completa, con la gráfica ya dentro del celular
 *   ↓ las tres bandas de UNLIMITED
 *   `aycd-s5-frente.png`  sólo el cuerpo del teléfono, con alfa
 *
 * La escena se **produjo**: el brief pide unas manos sosteniendo un celular
 * dentro de QB y esa foto no existe en el material de la marca (la sesión de
 * julio que hay en Drive es de un matrimonio). La IA hizo la mano, la mesa y el
 * bokeh — que es lo que le toca según `docs/SISTEMA-DE-MARCAS.md` §2.
 * **El trago que se ve en la pantalla NO se generó**: es un close-up de la
 * fotografía real y aprobada de la promo.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⚠️ PAID
 * ══════════════════════════════════════════════════════════════════════════
 * Se compone como ORGÁNICA. El pie con el legal entra en los 340 px que
 * Instagram reserva abajo — igual que el KV aprobado, que tampoco pasa. Si esta
 * historia va a pauta hay que subir el pie, y eso lo decide Eli.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ENTREGA
 * ══════════════════════════════════════════════════════════════════════════
 * Mesa 1080×1920 · 30 fps · 240 f (8 s). El movimiento **cierra en bucle**: cada
 * banda lleva la tira escrita dos veces y avanza un número entero de
 * repeticiones, así que el último fotograma empalma con el primero.
 */
import React from "react";
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from "remotion";

import {cargarFuentesQB, qbColores} from "../../brand/qb";

cargarFuentesQB();

export const QB_ST_AYCD_S5_FPS = 30;
export const QB_ST_AYCD_S5_DURACION = 240;

/**
 * ⭐ LAS BANDAS DE «UNLIMITED»
 *
 * El recurso de la referencia: la palabra en versales enormes, repetida, cortada
 * por los bordes del formato y por el objeto del primer plano.
 *
 * `top` está en px de mesa. Las tres se apilan en la mitad de arriba, con el
 * mismo ritmo de la referencia: la primera sale **cortada por el borde superior**
 * y las otras dos **se las va comiendo el celular**, que con el encuadre de 1,75
 * ocupa **y 335–1399 · x 169–920** (medido sobre el mate de la ronda 6).
 *
 * ⛔⛔ Y NINGUNA BAJA DE y≈723, que es donde empiezan las manos con este
 * encuadre. La probé a y=912 y la banda pasaba por encima del
 * pulgar y del índice: se ve como un error de montaje, no como un recurso. El
 * mate del frente es **sólo el teléfono**, porque la mano no se puede aislar —
 * la segmentación de sujeto se la come y sacarla por tono de piel no sirve: el
 * bokeh ámbar del bar tiene el mismo R>G>B que la piel en sombra. Así que la
 * tipografía se coloca donde el corte ES exacto, y no al revés.
 *
 * `opacidad` sube hacia abajo a propósito: la de más abajo es la que se apoya en
 * el celular, y es la que tiene que «notarse» (Eli, 17-09).
 *
 * `vueltas` es entero para que el bucle cierre.
 */
const BANDAS = [
  {top: -60, opacidad: 0.26, vueltas: 1, sentido: -1},
  {top: 200, opacidad: 0.40, vueltas: 2, sentido: +1},
  {top: 455, opacidad: 0.58, vueltas: 1, sentido: -1},
] as const;

const CUERPO_BANDA = 236;
const ALTO_BANDA = Math.round(CUERPO_BANDA * 1.06);

/**
 * Una banda. La tira va DOS veces y el desplazamiento es del 50 % por vuelta:
 * con eso el bucle es perfecto y no hay salto en el corte del video.
 */
const Banda: React.FC<{
  top: number;
  opacidad: number;
  vueltas: number;
  sentido: number;
}> = ({top, opacidad, vueltas, sentido}) => {
  const frame = useCurrentFrame();
  // ⚠️ El recorrido SIEMPRE vive dentro de [-50·vueltas, 0]. Escribirlo como
  // [0, +50] para la banda que va hacia la derecha dejaba el bloque de texto
  // corrido fuera del lienzo por la derecha: dos de las tres bandas
  // simplemente no se veían, y el render salía con una sola.
  const recorrido: [number, number] =
    sentido < 0 ? [-50 * vueltas, 0] : [0, -50 * vueltas];
  const avance = interpolate(frame, [0, QB_ST_AYCD_S5_DURACION], recorrido);
  const tira = "UNLIMITED   ".repeat(4);

  return (
    <div
      style={{
        position: "absolute",
        top,
        left: 0,
        width: "100%",
        height: ALTO_BANDA,
        overflow: "hidden",
      }}
    >
      <div
        style={{
          display: "inline-block",
          whiteSpace: "pre",
          transform: `translateX(${avance}%)`,
          fontFamily: "Raleway",
          fontWeight: 800,
          fontSize: CUERPO_BANDA,
          lineHeight: `${ALTO_BANDA}px`,
          letterSpacing: "0.01em",
          color: qbColores.blanco,
          opacity: opacidad,
        }}
      >
        {tira + tira}
      </div>
    </div>
  );
};

/**
 * ⭐ LOS TEXTOS DE LA PIEZA, EN UN SOLO LUGAR.
 *
 * Están acá y no sueltos en el JSX para que `qa/textos.py` los pueda leer del
 * propio TSX y la compuerta (`qa/motor.py --marca qb`) verifique de verdad las
 * reglas de copy —la grafía de «ALL YOU CAN DRINK» y el formato del precio— en
 * vez de dejarlas en SIN VERIFICAR. Una copia en un JSON aparte se desincroniza;
 * el TSX es lo que se renderiza, así que es lo único que no puede mentir.
 *
 * `titular` y `antetitulo` describen lo que se ve DENTRO del celular; el resto
 * es lo que va fuera. Los tres de abajo son literales del brief.
 */
const QB_ST_AYCD_S5_DATA: Record<string, Record<string, string>> = {
  // ⚠️ La clave se llama «aycd» y no «pieza» a propósito: `qa/textos.py` empareja
  // el bloque de datos con el archivo rendido **por el slug del nombre**, y el
  // render se llama `ST S5 QB AYCD 28-09.mp4`. Con «pieza» no casaba con nada y
  // las reglas de copy quedaban en SIN VERIFICAR.
  aycd: {
    titular: "ALL YOU CAN DRINK",
    antetitulo: "TODOS LOS MARTES",
    etiqueta: "POR $13.990",
    medida: "18:00 a 21:00 hrs",
    texto: "Tragos seleccionados ilimitados.",
    bajada: "Los números están claros.",
    cta: "RESERVA TU MESA",
    pie: "*Sujeto a consumo de alimentos. * Promoción no acumulable con otras promociones y beneficios.",
  },
};

/**
 * El pie. Va FUERA del celular porque adentro no se lee — dictado de Eli.
 * El degradado a negro es la misma idea del pie del KV de QB (una zona de
 * lectura al cierre), pero fundido en vez de cortado, para no partir la
 * fotografía de la escena.
 */
const Pie: React.FC = () => (
  <>
    <div
      style={{
        position: "absolute",
        left: 0,
        // ⚠️ Arranca justo bajo el celular, que con el encuadre de 1,75 termina
        // en y=1399. Si sube más, le oscurece la parte de abajo al teléfono.
        // Con el mate de la ronda 6 queda justo al canto, y no molesta porque el
        // degradado arranca en opacidad 0.
        top: 1400,
        width: "100%",
        height: 520,
        background:
          "linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,.60) 34%," +
          " rgba(0,0,0,.90) 58%, rgba(0,0,0,.97) 100%)",
      }}
    />

    {/* Texto complementario — literal del brief. */}
    <div
      style={{
        position: "absolute",
        top: 1512,
        left: 0,
        width: "100%",
        textAlign: "center",
        fontFamily: "Raleway",
        fontWeight: 300,
        fontStyle: "italic",
        fontSize: 35,
        color: qbColores.blanco,
        opacity: 0.95,
      }}
    >
      {QB_ST_AYCD_S5_DATA.aycd.bajada}
    </div>

    {/* CTA — literal del brief. La grilla no trae sticker de interacción para
        esta historia, así que el llamado tiene que estar en pantalla. */}
    <div
      style={{
        position: "absolute",
        top: 1586,
        left: 0,
        width: "100%",
        textAlign: "center",
        fontFamily: "Raleway",
        fontWeight: 600,
        fontSize: 46,
        letterSpacing: "0.13em",
        color: qbColores.blanco,
      }}
    >
      {QB_ST_AYCD_S5_DATA.aycd.cta}
    </div>

    {/* Legal — literal, y fuera del celular. */}
    <div
      style={{
        position: "absolute",
        top: 1798,
        left: 0,
        width: "100%",
        textAlign: "center",
        fontFamily: "Raleway",
        fontStyle: "italic",
        fontWeight: 400,
        // ⭐ Ronda 4: el legal va en DOS líneas y más grande, no en una y chico.
        // En una sola línea, al cuerpo que hace falta para leerlo, mide 1054 px
        // de 1080 y queda a 13 px del borde — por debajo de los 60 px de respiro
        // que pide agencia, y pegado. Partido en sus dos frases se lee mejor y
        // respira: la segunda, que es la larga, mide 756 px.
        fontSize: 26,
        lineHeight: "1.34",
        color: qbColores.blanco,
        opacity: 0.92,
      }}
    >
      {QB_ST_AYCD_S5_DATA.aycd.pie.split(" * ").map((linea, i) => (
        <div key={linea}>{i === 0 ? linea : `* ${linea}`}</div>
      ))}
    </div>
  </>
);

/**
 * ⭐⭐ EL ENCUADRE — y por qué NO se hace con `transform: scale()`
 *
 * Ronda 4. Eli: «se ve mal los textos pequeños en el video y en el estático, hay
 * problemas de visibilidad… un poco de zoom que no se ve nada del celular bien».
 *
 * **La causa no era la compresión ni el tamaño: era el `transform: scale()`.**
 * Chrome rasteriza la imagen al tamaño que ocupa en el layout —acá 1080×1920— y
 * recién después estira ESE MAPA DE BITS por el factor del transform. O sea que
 * las dos capas se dibujaban a 1080 de ancho y se ampliaban 1,5 veces: el
 * resultado es un 1080 estirado a 1620, con todo lo fino reventado. Se comía
 * los textos de la pantalla del celular **y** el filo del recorte, que es
 * exactamente lo que ella marcó en rojo las dos veces.
 *
 * ⇒ El encuadre se hace ahora **con el tamaño real del elemento**. La imagen se
 * declara de 1890×3360 y se corre con `left`/`top`, así que Chrome la rasteriza
 * a ese tamaño y baja los 2250 px del máster a 1890 — un DOWNSCALE, que es
 * nítido, en vez de un upscale, que no lo es.
 *
 * La equivalencia con el encuadre anterior: un `scale(Z)` alrededor de un origen
 * `o` lleva el punto `p` a `o + (p − o)·Z`. Con eso, la esquina superior
 * izquierda cae en `o·(1 − Z)` y el tamaño es `1080Z × 1920Z`.
 *
 * ⭐ Y de paso sube de 1,5 a **1,75**, que es el «auméntalo más» de Eli: el
 * teléfono pasa a ocupar **y 335–1399 · x 169–920**, o sea el **55 % del alto** y
 * el 70 % del ancho, y su pantalla mide **641 px** sobre 1080.
 *
 * ⚠️ Esa caja es la del mate de la ronda 6, que sigue el canto REAL del chasis —
 * bisel medido más el costado, cuyo ancho CRECE de arriba hacia abajo. La de la
 * ronda 4 decía «y 300–1387 · x 193–887» y era la de una forma ideal: sobraba
 * arriba y a la izquierda, y faltaba en los flancos.
 *
 * ⚠️ Los dos valores van EXACTAMENTE iguales en el fondo y en el frente, o las
 * capas se despegan y el recorte del celular aparece corrido.
 */
const ENCUADRE = {
  left: -248.4,
  top: -919.8,
  width: 1890,
  height: 3360,
} as const;

/**
 * ⭐ GRANO — contra el bandeo, no por estética.
 *
 * Eli, ronda 3: «se ve de mala calidad el video al reproducirse… baja mucho la
 * calidad de los textos». Parte de eso es Instagram recomprimiendo, pero parte
 * es nuestra: **esta pieza es casi toda negro y degradados oscuros**, que es
 * justo donde el h264 hace escalones. Dos filas contiguas idénticas se
 * cuantizan al mismo valor y el degradado se parte en franjas.
 *
 * Un grano muy fino rompe esa igualdad y el codificador vuelve a interpolar. Es
 * el mismo arreglo que Piso18 le hizo a sus fondos planos.
 *
 * ⚠️ NO se anima: Eli pidió que lo único en movimiento fuera UNLIMITED. Un grano
 * estático cumple y además comprime mejor que uno que titila.
 */
const GRANO =
  "data:image/svg+xml;utf8," +
  encodeURIComponent(
    '<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220">' +
      '<filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.85"' +
      ' numOctaves="3" stitchTiles="stitch"/></filter>' +
      '<rect width="220" height="220" filter="url(#g)"/>' +
      "</svg>",
  );

const Grano: React.FC = () => (
  <AbsoluteFill
    style={{
      backgroundImage: `url("${GRANO}")`,
      backgroundRepeat: "repeat",
      opacity: 0.04,
      mixBlendMode: "overlay",
      pointerEvents: "none",
    }}
  />
);

export const QBStAycdS5: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: qbColores.negro}}>
    {/* 1 · La escena, con la gráfica ya dentro del celular. Quieta. */}
    <Img
      src={staticFile("assets/hilton/qb/fotos/aycd-s5-fondo.jpg")}
      style={{position: "absolute", ...ENCUADRE, objectFit: "cover"}}
    />

    {/* 2 · Lo único que se mueve. */}
    <AbsoluteFill>
      {BANDAS.map((b) => (
        <Banda key={b.top} {...b} />
      ))}
    </AbsoluteFill>

    {/* 3 · El celular, por delante: parte la tipografía. */}
    <Img
      src={staticFile("assets/hilton/qb/fotos/aycd-s5-frente.png")}
      style={{position: "absolute", ...ENCUADRE, objectFit: "cover"}}
    />

    {/* 4 · El pie, fuera del teléfono. */}
    <Pie />

    {/* 5 · Grano, arriba de todo. */}
    <Grano />
  </AbsoluteFill>
);
