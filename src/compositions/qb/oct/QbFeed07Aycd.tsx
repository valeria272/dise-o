/**
 * QB · FEED 07-10 · 13:00 · CARRUSEL — ALL YOU CAN DRINK  (C1 S1 N°1 / N°2)
 *
 * BRIEF (grilla octubre, FEED col. E, OK PARA DISEÑAR desde el 28-09 tarde):
 *   Tomar la gráfica anterior de AYCD de QB y actualizarla para que se perciba
 *   más variedad: 3 a 4 tragos distintos en primer plano, con distintas copas y
 *   colores, sobre la barra; fondo QB cálido, nocturno y desenfocado.
 *   Slide 1 — Portada: imagen de tragos de la promo en spot QB.
 *   Slide 2 — Promo: ALL YOU CAN DRINK · TODOS LOS MARTES POR $13.990 ·
 *   18:00 a 21:00 hrs · legal.
 * COMENTARIO DEL CLIENTE: «Que sea como esos carruseles que hicimos antes, en que
 *   la G1 está limpia y luego viene la promo» (R-42).
 *
 * REFERENCIA: Pinterest 1407443630793215 — bartender sirviendo un trago en la
 * barra, fondo de botellas ámbar desenfocado.
 *
 * DIRECCIÓN DE ARTE
 *   · ⛔ RONDA 10 (Eli 28-09): «la G1 no es con los cócteles que van en el All You
 *     Can Drink: es de la selección de dioses… haz la misma foto de la referencia
 *     pero con un cóctel que va en el AYCD. Y la G2 lo mismo, vista cenital o más
 *     bonita». Los tragos del AYCD son los de la ST aprobada de septiembre: schop
 *     Heineken, piscola 35°, Ramazzotti, sangría y copa de espumante.
 *   · G1 LIMPIA: la foto de la ref recreada — el bartender sirviendo en la barra —
 *     preparando un spritz de RAMAZZOTTI Rosato en su copa. Generada → sólo la
 *     leyenda «Imagen referencial», chica, al pie.
 *   · G2 PROMO = el post AYCD aprobado de junio: logo arriba, «ALL YOU / CAN
 *     DRINK» con sus pesos del KV, TODOS LOS MARTES, el botón verde con el precio
 *     y el horario fino. Fondo: los cinco tragos del AYCD en la barra (generada)
 *     → «Imagen referencial» en el legal.
 *   · ⭐ RONDA 19 (Scarlette, hilo en FEED!D14, 29-09): «cambiar la botella de agua
 *     por una de espumante». Nano Banana Pro cambió sólo la botella (espumante verde
 *     con cápsula dorada, etiqueta crema sin marca legible) y se INJERTÓ esa zona
 *     sobre la foto aprobada con máscara difuminada: copa, jigger y barra intactos
 *     (`scripts/qb-oct-r19-nb.py`, `raw/hilton/qb/oct-r19/`). En Drive el carrusel
 *     pasa a C2 S1 AYCD (el C1 S1 es ahora el carrusel de cumpleaños del 05-10).
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BloqueAycd, cargarFuentesQbOct, Legal, Linea, LogoQB, NombreAycd, Velo} from "./QbOctKit";
import {FotoFeed} from "./QbFeedKit";

cargarFuentesQbOct();

const QB_FEED07_DATA: Record<string, Record<string, string>> = {
  pieza: {
  nombre: "ALL YOU CAN DRINK",
  antetitulo: "TODOS LOS MARTES",
  precio: "POR $13.990",
  horario: "18:00 a 21:00 hrs",
  legal: "*Imagen referencial. *Sujeto a consumo de alimentos.",
  legal2: "*Promoción no acumulable con otras ofertas y beneficios.",
  },
};

export const QbFeed07AycdG1: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoFeed src="assets/hilton/qb/oct/feed07-g1-r19.jpg" pos="50% 50%" />
    <Linea top={1150} cuerpo={17} italica ancho={500} color="rgba(255,255,255,0.8)">*Imagen referencial</Linea>
  </AbsoluteFill>
);

export const QbFeed07AycdG2: React.FC = () => {
  const d = QB_FEED07_DATA.pieza;
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoFeed src="assets/hilton/qb/oct/feed07-g2.jpg" pos="50% 60%" filtro="brightness(0.9)" />
      {/* r10: más denso arriba, la copa rosada queda tras «YOU» y «DRINK» */}
      <Velo arriba={[700, 0.93]} abajo={[640, 0.9]} />
      <LogoQB top={96} ancho={170} />
      <NombreAycd top={262} cuerpo={112} />
      <BloqueAycd antetitulo={866} boton={920} horario={1034}
        textoAntetitulo={d.antetitulo} textoBoton={d.precio} textoHorario={d.horario} />
      {/* Constanza 29-09: «no debemos palabras solitas» → corte por frase */}
      <Legal top={1110} cuerpo={19}>{d.legal}<br />{d.legal2}</Legal>
    </AbsoluteFill>
  );
};
