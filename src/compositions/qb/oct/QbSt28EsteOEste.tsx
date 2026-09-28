/**
 * QB · ST 28-10 · 16:00 · ESTÁTICA — DINÁMICA QB: ¿ESTE O ESTE?  (ST n°3 S4)
 *
 * BRIEF (grilla octubre, STORIES col. AD, OK PARA DISEÑAR desde el 28-09 tarde):
 *   «Adivina el trago» con letras sueltas que forman MOJITO, fondo de bar
 *   desenfocado y caja de preguntas.
 * COMENTARIO DEL CLIENTE: «Busquemos opción de dinámica más afín con QB, veamos
 *   si otros restaurantes hacen cosas así y probemos (últimamente tenemos muy
 *   mala participación)».
 *
 * DECISIÓN (Eli, 28-09): proponer «¿ESTE O ESTE?» — dos tragos de autor REALES
 * de QB lado a lado y el sticker de ENCUESTA para votar. Un toque para
 * participar: la mecánica con menos fricción, la que más usan los restaurantes
 * cuando la caja de preguntas no responde.
 *
 * DIRECCIÓN DE ARTE
 *   · Fotos reales de la sesión de coctelería 11-09: MEDUSA (verde, vaso tallado
 *     con kiwi) y PERSÉFONE (rosado, flores) — mismo set de estudio, misma luz,
 *     así el duelo se lee parejo. Sin «Imagen referencial».
 *   · Titular: antetítulo «DINÁMICA QB» + «¿Este o este?» en Brushwell grande.
 *   · Los nombres de los tragos en Bell MT itálica, como «Afrodita» en septiembre.
 *   · Aire entre 1230 y 1440 para el sticker de encuesta (Medusa / Perséfone).
 *   · ⚠️ El texto del premio es PROPUESTA (el brief decía «El primero en acertar
 *     gana un premio sorpresa»): se adaptó a votar. A confirmar con contenido.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {cargarFuentesQbOct, Grano, Linea, LogoQB} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST28_DATA: Record<string, Record<string, string>> = {
  pieza: {
  antetitulo: "DINÁMICA QB",
  titular: "¿Este o este?",
  a: "Medusa",
  b: "Perséfone",
  cierre: "Vota por tu favorito y participa por un premio sorpresa",
  },
};

const FOTO = {top: 560, w: 520, h: 640, gap: 16};

const Trago: React.FC<{src: string; left: number; pos: string}> = ({src, left, pos}) => (
  <Img src={staticFile(src)} style={{position: "absolute", top: FOTO.top, left, width: FOTO.w,
    height: FOTO.h, objectFit: "cover", objectPosition: pos}} />
);

export const QbSt28EsteOEste: React.FC = () => {
  const d = QB_ST28_DATA.pieza;
  const izq = (1080 - 2 * FOTO.w - FOTO.gap) / 2;
  const der = izq + FOTO.w + FOTO.gap;
  return (
    <AbsoluteFill style={{background: "#0E0C0A"}}>
      <LogoQB top={250} ancho={150} />
      <Linea top={362} cuerpo={32} peso={600} tracking="0.16em">{d.antetitulo}</Linea>
      <Linea top={400} cuerpo={130} familia="Brushwell" interlinea={1}>{d.titular}</Linea>
      <Trago src="assets/hilton/qb/oct/28-medusa.jpg" left={izq} pos="40% 50%" />
      <Trago src="assets/hilton/qb/oct/28-persefone.jpg" left={der} pos="50% 55%" />
      {/* nombres sobre el pie de cada foto */}
      <div style={{position: "absolute", top: FOTO.top + FOTO.h - 150, left: 0, right: 0, height: 150,
        background: "linear-gradient(180deg, rgba(0,0,0,0), rgba(0,0,0,.7))"}} />
      <Linea top={FOTO.top + FOTO.h - 88} cuerpo={58} familia="BellMT" italica ancho={FOTO.w} izquierda={izq}>{d.a}</Linea>
      <Linea top={FOTO.top + FOTO.h - 88} cuerpo={58} familia="BellMT" italica ancho={FOTO.w} izquierda={der}>{d.b}</Linea>
      <Linea top={1480} cuerpo={30} peso={500} italica ancho={820}>{d.cierre}</Linea>
      <Grano />
    </AbsoluteFill>
  );
};
