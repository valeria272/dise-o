/**
 * QB · LA GRÁFICA QUE VA DENTRO DEL CELULAR — «ALL YOU CAN DRINK»
 *
 * ══════════════════════════════════════════════════════════════════════════
 * No es una pieza de entrega: es una PIEZA-INSUMO.
 * ══════════════════════════════════════════════════════════════════════════
 * Se rinde como still y `scripts/qb-aycd-s5-montar.py` le aplica la homografía
 * a los cuatro vértices de la pantalla verde de la escena generada.
 *
 * ⭐ Existe por una razón concreta: **ningún modelo de imagen escribe
 * «POR $13.990» sin romperlo**, ni reproduce el degradado del botón, ni el
 * logotipo. Si la promo dentro del celular la escribiera la IA, el bloque que
 * Eli declaró intocable saldría alucinado. Acá sale con las fuentes reales y con
 * la geometría medida del KV, y recién después se pega en perspectiva.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL LIENZO
 * ══════════════════════════════════════════════════════════════════════════
 * 1200 × 2557 px — ratio 2,131, que es el que midió el detector de la pantalla
 * verde sobre `escena-2.png` (746 × 1590 px reales). Coincide con un teléfono
 * moderno (19,5:9 = 2,167).
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA GEOMETRÍA — es la del KV, escalada por ancho
 * ══════════════════════════════════════════════════════════════════════════
 * `QB_AYCD` está medido sobre una mesa de 1080 de ancho. Acá el ancho es 1200,
 * o sea ×1,111. **Todo lo horizontal y todos los cuerpos se escalan por ese
 * factor** para que el bloque sea el mismo, no uno parecido.
 *
 * Lo vertical NO se puede escalar igual: la pantalla es más alta de proporción
 * que la historia (2,131 contra 1,778), así que el aire sobra. Ese sobrante se
 * reparte —el titular baja un poco y el bloque de promo se asienta abajo—, que
 * es lo que haría cualquiera al adaptar el KV a un formato más largo.
 *
 * ⛔ Lo que NO cambia: los cortes del nombre (ALL ExtraBold · YOU itálica ·
 * CAN itálica · DRINK ExtraBold), el degradado del botón, sus esquinas vivas y
 * la proporción del logotipo.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LOS TEXTOS
 * ══════════════════════════════════════════════════════════════════════════
 * Los del KV, literales — es el dictado de Eli («que el diseño y textos de AYCD
 * sean igual al KV»). El brief agrega una línea que el KV no tiene y esa sí va:
 * «Tragos seleccionados ilimitados.»
 *
 * ⛔ **El legal NO va acá.** Eli, 17-09-2026: «el legal que esté fuera del
 * celular, que no se lee». Va en la pieza, fuera del teléfono.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA FOTOGRAFÍA DEL FONDO
 * ══════════════════════════════════════════════════════════════════════════
 * Close-up del Ramazzotti Aperitivo Rosato — **recorte de la fotografía real y
 * aprobada de la promo**, no una generada. Es uno de los tragos que la propia
 * lista del KV nombra, así que el brief («uno de los tragos seleccionados de QB,
 * idealmente en close up») se cumple con material propio.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {
  cargarFuentesQB,
  QB_AYCD,
  QB_ASSETS,
  QB_BOTON_FONDO,
  QB_CIFRAS,
  qbColores,
} from "../../brand/qb";

cargarFuentesQB();

export const QB_PANTALLA = {w: 1200, h: 2557} as const;

/**
 * Los textos de la pantalla, en un solo lugar — igual que en `QBStAycdS5`, para
 * que `qa/textos.py` los lea del TSX y la compuerta verifique la grafía y el
 * formato del precio. Los cuatro primeros son literales del KV; el último es la
 * única línea que agrega el brief.
 */
const QB_PANTALLA_AYCD_DATA: Record<string, Record<string, string>> = {
  pantalla: {
    titular: "ALL YOU CAN DRINK",
    antetitulo: "TODOS LOS MARTES",
    etiqueta: "POR $13.990",
    medida: "18:00 a 21:00 hrs",
    texto: "Tragos seleccionados ilimitados.",
  },
};

/** La pantalla mide 1200 de ancho y el KV está medido a 1080. */
const K = QB_PANTALLA.w / 1080; // 1,1111…

/**
 * Posiciones verticales. Se parte de las del KV escaladas por K y se les suma el
 * aire que sobra: la pantalla es 424 px más alta de lo que daría el KV escalado.
 * Arriba se reparte poco (el titular manda) y abajo se asienta el bloque de promo.
 */
const Y = {
  logo: QB_AYCD.logo.top * K + 78,
  titular1: QB_AYCD.titular.linea1Top * K + 96,
  titular2: QB_AYCD.titular.linea2Top * K + 96,
  antetitulo: QB_AYCD.antetitulo.top * K + 355,
  boton: QB_AYCD.boton.top * K + 355,
  horario: QB_AYCD.horario.top * K + 355,
  ilimitados: QB_AYCD.horario.top * K + 355 + 92,
} as const;

const bold: React.CSSProperties = {fontWeight: 800, fontStyle: "normal"};
const italica = (track: string): React.CSSProperties => ({
  fontWeight: 400,
  fontStyle: "italic",
  letterSpacing: track,
});

const Linea: React.FC<{
  top: number;
  estilo: React.CSSProperties;
  children: React.ReactNode;
}> = ({top, estilo, children}) => (
  <div
    style={{
      position: "absolute",
      top,
      left: 0,
      width: "100%",
      textAlign: "center",
      color: qbColores.blanco,
      whiteSpace: "nowrap",
      ...estilo,
    }}
  >
    {children}
  </div>
);

export const QBPantallaAycd: React.FC = () => {
  const cuerpoTitular = QB_AYCD.titular.cuerpo * K;
  const altoLinea = cuerpoTitular * 1.18;

  return (
    <AbsoluteFill style={{backgroundColor: qbColores.negro, overflow: "hidden"}}>
      <Img
        src={staticFile("assets/hilton/qb/fotos/aycd-trago-pantalla.jpg")}
        style={{width: "100%", height: "100%", objectFit: "cover"}}
      />

      {/*
        Velo de lectura. El close-up del trago es más claro que el plano general
        del KV —hay vidrio, hielo y una etiqueta blanca justo donde cae el
        titular—, así que el blanco no aguantaba solo. Es un degradado por los
        dos extremos, no un velo plano: al centro la foto queda intacta.
      */}
      <AbsoluteFill
        style={{
          background:
            // ⭐ Ronda 4: el tramo de abajo se oscurece bastante más. El bloque
            // de la promo cae sobre el cuerpo de la copa, que es rosado claro, y
            // «18:00 a 21:00 hrs» en Raleway Light se perdía encima. Sigue
            // siendo un degradado por los dos extremos —al centro la fotografía
            // queda intacta—, sólo que el pie pesa más.
            "linear-gradient(180deg, rgba(0,0,0,.84) 0%, rgba(0,0,0,.58) 20%," +
            " rgba(0,0,0,.10) 40%, rgba(0,0,0,.22) 56%, rgba(0,0,0,.62) 70%," +
            " rgba(0,0,0,.88) 84%, rgba(0,0,0,.95) 100%)",
        }}
      />

      <Img
        src={staticFile(QB_ASSETS.logoBlanco)}
        style={{
          position: "absolute",
          top: Y.logo,
          left: QB_PANTALLA.w / 2 - (QB_AYCD.logo.ancho * K) / 2,
          width: QB_AYCD.logo.ancho * K,
          height: QB_AYCD.logo.alto * K,
        }}
      />

      <Linea
        top={Y.titular1 - (altoLinea - QB_AYCD.titular.altoVersal * K) * 0.62}
        estilo={{
          fontFamily: "Raleway",
          fontSize: cuerpoTitular,
          lineHeight: `${altoLinea}px`,
        }}
      >
        <span style={bold}>ALL</span>{" "}
        <span style={italica("-0.024em")}>YOU</span>
      </Linea>
      <Linea
        top={Y.titular2 - (altoLinea - QB_AYCD.titular.altoVersal * K) * 0.62}
        estilo={{
          fontFamily: "Raleway",
          fontSize: cuerpoTitular,
          lineHeight: `${altoLinea}px`,
        }}
      >
        <span style={italica("-0.012em")}>CAN</span>{" "}
        <span style={bold}>DRINK</span>
      </Linea>

      <Linea
        top={Y.antetitulo}
        estilo={{
          fontFamily: "Raleway",
          fontWeight: 600,
          fontSize: 45 * K,
          letterSpacing: "0.045em",
        }}
      >
        {QB_PANTALLA_AYCD_DATA.pantalla.antetitulo}
      </Linea>

      {/* ⭐ El botón: degradado horizontal de marca y esquinas vivas. */}
      <div
        style={{
          position: "absolute",
          top: Y.boton,
          left: QB_PANTALLA.w / 2 - (QB_AYCD.boton.ancho * K) / 2,
          width: QB_AYCD.boton.ancho * K,
          height: QB_AYCD.boton.alto * K,
          background: QB_BOTON_FONDO,
        }}
      />
      <div
        style={{
          position: "absolute",
          top: Y.boton,
          left: 0,
          width: "100%",
          height: QB_AYCD.boton.alto * K,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontFamily: "Raleway",
          fontWeight: 800,
          fontSize: 58.8 * K,
          letterSpacing: "0.005em",
          color: qbColores.blanco,
          paddingTop: 6.2 * K,
          ...QB_CIFRAS,
        }}
      >
        {QB_PANTALLA_AYCD_DATA.pantalla.etiqueta}
      </div>

      <Linea
        top={Y.horario}
        estilo={{
          fontFamily: "Raleway",
          fontWeight: 300,
          fontSize: 44 * K,
          letterSpacing: "0.094em",
          ...QB_CIFRAS,
        }}
      >
        {QB_PANTALLA_AYCD_DATA.pantalla.medida}
      </Linea>

      {/* La única línea que agrega el brief y el KV no tiene. */}
      <Linea
        top={Y.ilimitados}
        estilo={{
          fontFamily: "Raleway",
          fontWeight: 300,
          fontStyle: "italic",
          fontSize: 34 * K,
          opacity: 0.95,
        }}
      >
        {QB_PANTALLA_AYCD_DATA.pantalla.texto}
      </Linea>
    </AbsoluteFill>
  );
};
