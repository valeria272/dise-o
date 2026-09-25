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
 * madera con luz de tarde.
 *
 * ⭐⭐ RONDA DE ELI 25-09: «usa tal cual la pieza gráfica seleccionada, sólo
 * cambia los textos que agrega el brief, pero el logo de Sunset QB déjalo tal
 * cual» · «no se parece a nada a la ya aprobada».
 * ⇒ La base es la ST aprobada de agosto (Drive «POST + ST SUNSET PROMO QB /
 *   St n° 1 QB SUNSET.png»):
 *   · FOTO: la del KV, sin texto, sacada del PDF de «Promo Sunset QB digital»
 *     (imagen 1728×2304) con el MISMO encuadre de la ST aprobada.
 *   · LOGO «Sunset QB»: el vectorial de ese PDF, exportado tal cual
 *     (`sunset-qb-logo.png`), en el lugar y tamaño de la ST aprobada.
 *   · TEXTOS: donde la aprobada decía «TUS FAVORITOS / AL MEJOR PRECIO» va el
 *     titular del brief, en la misma Raleway Regular y el mismo cuerpo; la
 *     pastilla verde en el mismo lugar con el horario; debajo, las dos líneas
 *     que el brief agrega. Sólo Raleway.
 *   · El legal sube a la zona segura de Instagram (en la aprobada estaba a 74 px
 *     del borde).
 *   · PROMO → zona segura de paid. Títulos sin punto (regla Hilton §F).
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {BotonVerde, cargarFuentesQbOct, FotoQB, Legal, Linea, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST09_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "EL VIERNES CAMBIA DE MOOD",
  medida: "DE 16:00 A 21:00 HRS",
  texto: "Cocktails seleccionados al mejor precio",
  bajada: "Tu after office, a otro nivel",
  legal: "*Sujeto a consumo de alimentos. *Promoción no acumulable con otras ofertas y beneficios.",
  },
};

/** Logo «Sunset QB» de la pieza aprobada: 767 px de ancho y tope en 346 (mesa). */
const LOGO_W = 767;
const LOGO_H = LOGO_W * 576 / 2556;

export const QbSt09Sunset: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/09-sunset-kv.jpg" ratio={2250 / 4000} />
    {/* el oscurecido suave de la aprobada detrás del bloque de texto */}
    <Velo arriba={[560, 0.35]} abajo={[980, 0.72]} />
    <Img src={staticFile("assets/hilton/qb/oct/sunset-qb-logo.png")}
      style={{position: "absolute", top: 346, left: (MESA.w - LOGO_W) / 2, width: LOGO_W, height: LOGO_H}} />
    <Linea top={1150} cuerpo={84} peso={400} interlinea={1.02} tracking="0.01em">EL VIERNES</Linea>
    <Linea top={1236} cuerpo={84} peso={400} interlinea={1.02} tracking="0.01em">CAMBIA DE MOOD</Linea>
    <BotonVerde top={1338} ancho={560} alto={58} cuerpo={29} peso={700}>{QB_ST09_DATA.pieza.medida}</BotonVerde>
    <Linea top={1420} cuerpo={32} peso={500}>{QB_ST09_DATA.pieza.texto}</Linea>
    <Linea top={1466} cuerpo={32} peso={400} italica>{QB_ST09_DATA.pieza.bajada}</Linea>
    <Legal top={1536} cuerpo={16}>{QB_ST09_DATA.pieza.legal}</Legal>
  </AbsoluteFill>
);
