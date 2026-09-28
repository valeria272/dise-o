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
 *   · G1 LIMPIA: sólo la foto. Real, «QB 13 oct-57»: cinco tragos distintos
 *     (verde, espresso martini, rojo, rosado, naranjo) sobre la mesa de listones,
 *     con el salón de QB de noche detrás. Nada de texto ni logo.
 *   · G2 PROMO = el post AYCD aprobado de junio: logo arriba, «ALL YOU / CAN
 *     DRINK» con sus pesos del KV, TODOS LOS MARTES, el botón verde con el precio
 *     y el horario fino. Fondo: la toma hermana «QB 13 oct-54», con velo para
 *     leer. Todo es foto real → sin «Imagen referencial».
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BloqueAycd, cargarFuentesQbOct, Legal, LogoQB, NombreAycd, Velo} from "./QbOctKit";
import {FotoFeed} from "./QbFeedKit";

cargarFuentesQbOct();

const QB_FEED07_DATA: Record<string, Record<string, string>> = {
  pieza: {
  nombre: "ALL YOU CAN DRINK",
  antetitulo: "TODOS LOS MARTES",
  precio: "POR $13.990",
  horario: "18:00 a 21:00 hrs",
  legal: "*Sujeto a consumo de alimentos. *Promoción no acumulable con otras ofertas y beneficios.",
  },
};

export const QbFeed07AycdG1: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoFeed src="assets/hilton/qb/oct/feed07-g1.jpg" pos="50% 62%" />
  </AbsoluteFill>
);

export const QbFeed07AycdG2: React.FC = () => {
  const d = QB_FEED07_DATA.pieza;
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoFeed src="assets/hilton/qb/oct/feed07-g2.jpg" pos="50% 0%" filtro="brightness(0.92)" />
      <Velo arriba={[620, 0.82]} abajo={[640, 0.9]} />
      <LogoQB top={96} ancho={170} />
      <NombreAycd top={262} cuerpo={112} />
      <BloqueAycd antetitulo={866} boton={920} horario={1034}
        textoAntetitulo={d.antetitulo} textoBoton={d.precio} textoHorario={d.horario} />
      <Legal top={1110} cuerpo={19}>{d.legal}</Legal>
    </AbsoluteFill>
  );
};
