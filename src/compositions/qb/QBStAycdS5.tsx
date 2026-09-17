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
 * y la tercera queda **partida por el celular**, que arranca en y=655 (el mate
 * mide y 688–1327 y el acercamiento de 1,12 lo sube a 655–1371).
 *
 * ⛔⛔ Y NINGUNA BAJA DE y≈900. La probé a y=912 y la banda pasaba por encima del
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
  {top: -46, opacidad: 0.26, vueltas: 1, sentido: -1},
  {top: 232, opacidad: 0.38, vueltas: 2, sentido: +1},
  {top: 520, opacidad: 0.55, vueltas: 1, sentido: -1},
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
        top: 1360,
        width: "100%",
        height: 560,
        background:
          "linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,.60) 34%," +
          " rgba(0,0,0,.90) 58%, rgba(0,0,0,.97) 100%)",
      }}
    />

    {/* Texto complementario — literal del brief. */}
    <div
      style={{
        position: "absolute",
        top: 1596,
        left: 0,
        width: "100%",
        textAlign: "center",
        fontFamily: "Raleway",
        fontWeight: 300,
        fontStyle: "italic",
        fontSize: 31,
        color: qbColores.blanco,
        opacity: 0.9,
      }}
    >
      Los números están claros.
    </div>

    {/* CTA — literal del brief. La grilla no trae sticker de interacción para
        esta historia, así que el llamado tiene que estar en pantalla. */}
    <div
      style={{
        position: "absolute",
        top: 1664,
        left: 0,
        width: "100%",
        textAlign: "center",
        fontFamily: "Raleway",
        fontWeight: 600,
        fontSize: 38,
        letterSpacing: "0.13em",
        color: qbColores.blanco,
      }}
    >
      RESERVA TU MESA
    </div>

    {/* Legal — literal, y fuera del celular. */}
    <div
      style={{
        position: "absolute",
        top: 1806,
        left: 0,
        width: "100%",
        textAlign: "center",
        fontFamily: "Raleway",
        fontStyle: "italic",
        fontWeight: 400,
        fontSize: 22,
        color: qbColores.blanco,
        opacity: 0.72,
      }}
    >
      *Sujeto a consumo de alimentos. * Promoción no acumulable con otras
      promociones y beneficios.
    </div>
  </>
);

/**
 * Acercamiento fijo de la escena. El brief pide que el teléfono «ocupe gran
 * parte de la pieza»; en el encuadre generado se queda en un 33 % del alto y con
 * 1,12 sube a 37 % sin perder el trago, el plato para compartir ni la vela, que
 * son los «elementos que dan contexto al panorama» que el mismo brief pide.
 *
 * ⚠️ Va EXACTAMENTE igual en el fondo y en el frente, o las dos capas se
 * despegan y el recorte del celular aparece corrido.
 */
const ACERCAMIENTO = "scale(1.12)";

export const QBStAycdS5: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: qbColores.negro}}>
    {/* 1 · La escena, con la gráfica ya dentro del celular. Quieta. */}
    <Img
      src={staticFile("assets/hilton/qb/fotos/aycd-s5-fondo.jpg")}
      style={{
        width: "100%",
        height: "100%",
        objectFit: "cover",
        transform: ACERCAMIENTO,
      }}
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
      style={{
        position: "absolute",
        inset: 0,
        width: "100%",
        height: "100%",
        objectFit: "cover",
        transform: ACERCAMIENTO,
      }}
    />

    {/* 4 · El pie, fuera del teléfono. */}
    <Pie />
  </AbsoluteFill>
);
