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
 *   · ⭐ RONDA 29 (CLIENTE, celda FEED!E14, 01-10; el comentario anterior quedó tachado):
 *     «Están fuera de proporciones los tragos en la G2; en la G1, mantener más simple,
 *     creo que está muy literal con la refe, veamos algo más de este estilo» + pin
 *     1068760555331775825 (UN vaso solo en la esquina de la barra, fondo cálido fuera
 *     de foco).
 *     G1: una copa de sangría (trago del AYCD) sola sobre la barra perforada de QB.
 *     Base: la foto REAL «QB oct-31» (terraza 10-oct), que es ese mismo plano; Nano
 *     Banana Pro la llevó a vertical y cambió el trago de autor por la sangría. Sin
 *     bartender, sin botella, sin manos.
 *     G2: los cinco tragos del AYCD en UNA fila, de frente, en el mismo plano y sobre la
 *     misma barra, para que cada vaso tenga su tamaño real (copones iguales, flauta
 *     angosta, vaso alto y schop más bajos). La fila va entera entre el nombre y el
 *     bloque de la promo (foto al 80 %, bordes completados por reflejo): nada la tapa.
 *     Con el fondo ya oscuro el velo baja al mínimo. Fotos y pasos en
 *     `raw/hilton/qb/oct-r29/`. Textos: sin cambios.
 *   · ⭐ RONDA 30 (Eli 01-10): «usar el material real que dejaste, porque es la más
 *     similar [a la referencia]… en la segunda slide pondría todo lo mismo, esa misma
 *     foto del octubre 31 sirve para ambas y que sea una transición bonita».
 *     G1 + G2 = la foto REAL «QB oct-31» partida en PANORAMA (recorte 2700×1688 desde
 *     x=300, y=300 → 4500×2812): el vaso sobre la barra en la G1 y la barra que sigue,
 *     fuera de foco, detrás de la promo en la G2. Salen los cinco tragos en fila.
 *     El trago de la foto es de autor (no entra en el AYCD, R-56): Nano Banana Pro
 *     cambió SÓLO el líquido por sangría, mismo vaso tallado y mismo romero; la franja
 *     del empalme con la G2 es la foto real. `feed07-g1-r30-real.jpg` = la foto tal cual.
 *     Pasos en `raw/hilton/qb/oct-r30/`.
 *   · RONDA 31 (Eli 01-10): «lo de imagen referencial abajo al centro y mejora la
 *     posición del cóctel». El panorama se corre 70 px de foto a la izquierda (x=230)
 *     para que el vaso quede CENTRADO en la G1; la leyenda baja al centro del pie.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BloqueAycd, cargarFuentesQbOct, Legal, Linea, LogoQB, NombreAycd} from "./QbOctKit";
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
    <FotoFeed src="assets/hilton/qb/oct/feed07-g1-r31.jpg" pos="50% 50%" />
    {/* r31 (Eli): abajo al centro. Ahí la barra tiene puntos de luz: cajita translúcida sutil (R-94) */}
    <div style={{position: "absolute", top: 1268, left: 0, width: 1080, display: "flex", justifyContent: "center"}}>
      <span style={{fontFamily: "Raleway", fontStyle: "italic", fontSize: 17, color: "rgba(255,255,255,0.92)",
        background: "rgba(0,0,0,0.38)", backdropFilter: "blur(6px)", padding: "5px 14px"}}>*Imagen referencial</span>
    </div>
  </AbsoluteFill>
);

export const QbFeed07AycdG2: React.FC = () => {
  const d = QB_FEED07_DATA.pieza;
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoFeed src="assets/hilton/qb/oct/feed07-g2-r31.jpg" pos="50% 50%" />
      {/* r30: el velo entra de izquierda a derecha y parte en 0 en el borde del empalme,
          para que la unión con la G1 no se note al deslizar */}
      <AbsoluteFill style={{background:
        "linear-gradient(90deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.5) 24%, rgba(0,0,0,0.5) 100%)"}} />
      <LogoQB top={96} ancho={170} />
      <NombreAycd top={262} cuerpo={112} />
      <BloqueAycd antetitulo={866} boton={920} horario={1034}
        textoAntetitulo={d.antetitulo} textoBoton={d.precio} textoHorario={d.horario} />
      {/* Constanza 29-09: «no debemos palabras solitas» → corte por frase */}
      <Legal top={1110} cuerpo={19}>{d.legal}<br />{d.legal2}</Legal>
    </AbsoluteFill>
  );
};
