/**
 * QB · ST 09-10 · 15:00 · ESTÁTICA — SUNSET QB
 *
 * BRIEF (STORIES col. G, OK PARA DISEÑAR, sin comentario):
 *   Un cocktail protagonista en primer plano, muy bien iluminado por la luz del
 *   atardecer, atmósfera cálida y sofisticada. En segundo plano personas
 *   compartiendo desenfocadas. Golden hour, look más lifestyle que promocional.
 *   Texto: EL VIERNES CAMBIA DE MOOD. DE 16:00 A 21:00, · SUNSET QB · Cocktails
 *   seleccionados al mejor precio. · Bajada: Tu after office, a otro nivel.
 *
 * REFERENCIA: Pinterest 1025976358870898225 (Moksi) — trago sobre mesa de
 * madera con luz de tarde, titular grande arriba.
 *
 * DIRECCIÓN DE ARTE
 *   · ⭐ «Sunset QB» es un bloque de marca: «Sunset» en Brushwell ENLAZADO con el
 *     logotipo — el logo hace de palabra (manual §4b, post de Sunset aprobado).
 *   · Foto REAL: el spritz de la terraza de QB (IMG_3077, sesión orgánica 2026)
 *     llevado a atardecer en código (`qb-oct-fondos.py`: temperatura + sol bajo
 *     sumado como luz). Encuadre cerrado arriba para dejar fuera las costillas.
 *   · ⚠️ LO QUE FALTA DEL BRIEF: las personas desenfocadas detrás. La sesión no
 *     las tiene en esta toma y generarlas quedó bloqueado: la API de Magnific se
 *     quedó sin créditos el 24-09. Cuando haya, se regenera el fondo.
 *   · El horario va en la pastilla verde, que es donde viven las cifras de QB.
 *   · PROMO → zona segura de paid. Títulos sin punto (regla Hilton §F).
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS, QB_LOGO} from "../../../brand/qb";
import {BotonVerde, cargarFuentesQbOct, FotoQB, Linea, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST09_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "EL VIERNES CAMBIA DE MOOD",
  etiqueta: "Sunset QB",
  medida: "DE 16:00 A 21:00 HRS",
  texto: "Cocktails seleccionados al mejor precio",
  bajada: "Tu after office, a otro nivel",
  },
};

/** «Sunset» en Brushwell + el logotipo, en una sola línea centrada. */
const SunsetQB: React.FC<{top: number}> = ({top}) => {
  const logoW = 190;
  const logoH = logoW / QB_LOGO.proporcion;
  return (
    <div style={{position: "absolute", top, left: 0, width: MESA.w, display: "flex",
      justifyContent: "center", alignItems: "center", gap: 14}}>
      <span style={{fontFamily: "Brushwell", fontSize: 150, color: "#fff", lineHeight: 1,
        textShadow: "0 3px 22px rgba(0,0,0,.45)", marginTop: 18}}>Sunset</span>
      <Img src={staticFile(QB_ASSETS.logoBlanco)} style={{width: logoW, height: logoH}} />
    </div>
  );
};

export const QbSt09Sunset: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/09-sunset.jpg" ratio={2250 / 4000} zoom={1.5} cx={0.6} cy={0.22} />
    <Velo arriba={[720, 0.8]} abajo={[1050, 0.98]} />
    <Linea top={262} cuerpo={50} peso={300} tracking="0.07em">EL VIERNES</Linea>
    <Linea top={322} cuerpo={50} peso={800} tracking="0.03em">CAMBIA DE MOOD</Linea>
    <SunsetQB top={392} />
    <Linea top={1320} cuerpo={36} peso={500}>{QB_ST09_DATA.pieza.texto}</Linea>
    <BotonVerde top={1384} ancho={560} alto={80} cuerpo={38} peso={800}>{QB_ST09_DATA.pieza.medida}</BotonVerde>
    <Linea top={1500} cuerpo={40} familia="BellMT" italica>{QB_ST09_DATA.pieza.bajada}</Linea>
  </AbsoluteFill>
);
