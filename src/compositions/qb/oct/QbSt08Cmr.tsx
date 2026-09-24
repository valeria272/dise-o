/**
 * QB · ST 08-10 · 18:00 · ESTÁTICA — DESCUENTO CMR FALABELLA
 *
 * BRIEF (STORIES col. F, OK PARA DISEÑAR, sin comentario):
 *   Composición más editorial y atmosférica, la barra o una escena interior de QB
 *   con fondo desenfocado, luces cálidas y ambiente nocturno. Panorama atractivo
 *   y accesible cualquier día. Puede aparecer un cocktail protagonista en primer
 *   plano. Texto: TU MESA TIENE BENEFICIOS / TODOS LOS DÍAS · CMR FALABELLA ·
 *   20% OFF · TODOS LOS DÍAS · legal.
 *
 * REFERENCIA: Pinterest 344877283982097898 (Buenavista) — escena de barra
 * oscura con bokeh, titular grande arriba, datos abajo.
 *
 * DIRECCIÓN DE ARTE
 *   · Foto REAL: el cóctel naranja en copa tallada de la terraza de QB, con el
 *     bokeh de las luces (sesión de Víctor, C4146 t=5,5 s, Sony 4K; 9:16 sacado
 *     del 16:9 centrado en la copa). Sin IA.
 *   · El trago es el protagonista absoluto al centro; el titular arriba sobre el
 *     bokeh oscuro y el beneficio abajo en el botón verde de la marca.
 *   · PROMO → zona segura de paid.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BotonVerde, cargarFuentesQbOct, FotoQB, Legal, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST08_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "TU MESA TIENE BENEFICIOS TODOS LOS DÍAS",
  etiqueta: "CMR FALABELLA",
  texto: "20% OFF · TODOS LOS DÍAS",
  legal: "Sujeto a consumo de alimentos. Promoción no acumulable con otras ofertas y beneficios.",
  },
};

export const QbSt08Cmr: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/08-cmr.jpg" ratio={2250 / 4000} zoom={1.0} cx={0.5} cy={0.5} />
    <Velo arriba={[900, 0.96]} abajo={[820, 0.95]} />
    <LogoQB top={252} ancho={150} />
    <Linea top={372} cuerpo={62} peso={800} tracking="0.02em">TU MESA TIENE</Linea>
    <Linea top={440} cuerpo={62} peso={800} tracking="0.02em">BENEFICIOS</Linea>
    <Linea top={514} cuerpo={62} peso={300} tracking="0.06em">TODOS LOS DÍAS</Linea>
    <Linea top={1364} cuerpo={44} peso={800} tracking="0.12em">{QB_ST08_DATA.pieza.etiqueta}</Linea>
    <BotonVerde top={1436} ancho={580} alto={82} cuerpo={40} peso={800}>{QB_ST08_DATA.pieza.texto}</BotonVerde>
    <Legal top={1548} cuerpo={17}>{QB_ST08_DATA.pieza.legal}</Legal>
  </AbsoluteFill>
);
