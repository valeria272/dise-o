/**
 * QB · ST 06-10 · 13:00 · ESTÁTICA — ALL YOU CAN DRINK
 *
 * BRIEF (STORIES col. D, OK PARA DISEÑAR, sin comentario):
 *   Tomar como referencia la imagen adjunta: propuesta más sofisticada, limpia y
 *   llamativa, estética más editorial. 2 o 3 tragos protagonistas sobre una
 *   superficie elegante, iluminación más dramática y nocturna.
 *   Texto: Tus favoritos, las veces que quieras. · ALL YOU CAN DRINK · Todos los
 *   martes por $13.990 · 18:00 a 21:00 hrs · En tragos seleccionados · legal.
 *
 * REFERENCIA: Pinterest 12525705209726454 (Sora «Happy Hour») — cortina de
 * terciopelo, luz de foco, tragos al centro.
 *
 * DIRECCIÓN DE ARTE
 *   · ⭐ El bloque de AYCD es el del KV y NO varía (Eli, 17-09): logo + nombre con
 *     sus cortes + botón con degradado + TODOS LOS MARTES / POR $13.990 /
 *     18:00 a 21:00 hrs, en las coordenadas medidas (QB_AYCD). Del brief se toma
 *     sólo lo que el KV no cubre: «Tus favoritos, las veces que quieras» y «En
 *     tragos seleccionados» (manual §4c, corolario de copy).
 *   · La foto es la variable: escena GENERADA (Seedream 5 Pro) con los tragos del
 *     KV —spritz de Ramazzotti, sangría y espumante— sobre mármol negro y
 *     cortina burdeo, como la referencia → lleva «Imagen referencial».
 *   · PROMO → puede ir a paid: logo y nombre bajan 45 px para entrar en y≥250.
 *     El bloque de abajo queda en sus coordenadas del KV y el legal cierra en 1580.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BloqueAycd, cargarFuentesQbOct, FotoQB, Legal, Linea, LogoQB, NombreAycd, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST06_DATA: Record<string, Record<string, string>> = {
  pieza: {
  antetitulo: "Tus favoritos, las veces que quieras",
  titular: "ALL YOU CAN DRINK",
  etiqueta: "POR $13.990",
  medida: "TODOS LOS MARTES · 18:00 a 21:00 hrs",
  texto: "En tragos seleccionados",
  legal: "*Imagen referencial. Sujeto a consumo de alimentos. Promoción no acumulable con otras ofertas y beneficios.",
  },
};

const BAJA = 45;

export const QbSt06Aycd: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/06-aycd.jpg" ratio={2250 / 4050} zoom={1.12} cx={0.5} cy={0.5} />
    <Velo arriba={[820, 0.9]} abajo={[760, 0.95]} />
    <LogoQB top={207.4 + BAJA} ancho={178.6} />
    <NombreAycd top={376.3 + BAJA} />
    <Linea top={610} cuerpo={34} italica peso={400}>{QB_ST06_DATA.pieza.antetitulo}</Linea>
    {/* 25-09: el bloque sube 30 px para que texto y legal entren en la zona segura */}
    <BloqueAycd antetitulo={1281.4} boton={1334.6} horario={1449.4} />
    <Linea top={1508} cuerpo={27} italica peso={300}>{QB_ST06_DATA.pieza.texto}</Linea>
    <Legal top={1546} cuerpo={14}>{QB_ST06_DATA.pieza.legal}</Legal>
  </AbsoluteFill>
);
