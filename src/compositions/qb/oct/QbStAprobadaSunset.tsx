/**
 * QB · ST S2 · S3 · S4 · 16:00 · ESTÁTICA — «ST APROBADA | SUNSET QB»
 *
 * GRILLA (STORIES, 3 columnas en APROBADO sin fecha, una por semana: tras el 14-10,
 * tras el 22-10 y tras el 30-10; interacción «LINK SUNSET QB»): contenido marca que
 * se republica la ST aprobada de Sunset.
 *
 * Eli 29-09: «guíate de las referencias que da contenido, pero hay elementos que
 * conservar: logos, nombres importantes y legales».
 *
 * DIRECCIÓN DE ARTE
 *   · PLANTILLA APROBADA: «St n° 1 QB SUNSET» (agosto 2026,
 *     `raw/hilton/qb/aprobadas/St n1 QB SUNSET.png`), medida en mesa:
 *       logo «Sunset QB» 767 px de ancho, tope 346 — el vectorial del PDF de la
 *       promo, tal cual (R-06, «el logo de Sunset QB déjalo tal cual»);
 *       «TUS FAVORITOS / AL MEJOR PRECIO» en Raleway Light, versal de 60 px;
 *       pastilla con el degradado del botón, 560 × 54, «VIERNES DE 16:00 A 21:00 HRS»;
 *       legal de la aprobada.
 *   · FOTO: la variable. Terraza REAL de QB con luz de tarde (R-47), tragos sobre
 *     la mesa de listones — sesión «QB 13 oct» (referencia de Sunset de contenido:
 *     trago sobre mesa de madera a la hora dorada). Una por semana:
 *       S2 → QB 13 oct-57 · S3 → QB 13 oct-67 · S4 → QB 13 oct-52
 *     Foto real → sin «Imagen referencial».
 *   · PROMO → paid: el legal sube de 1855 a la zona segura, a 19 px (R-52, E-06).
 *     Arriba se oscurece para leer el logo (R-53).
 *   · El titular Light cae sobre los tragos (como en la aprobada, donde cruzaba la
 *     copa); con tragos de colores detrás no se leía → velo elíptico local detrás
 *     del titular y la pastilla, sin mover nada de su lugar.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {BotonVerde, cargarFuentesQbOct, FotoQB, Legal, Linea, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_SUNSET_AP_DATA = {
  titular: ["TUS FAVORITOS", "AL MEJOR PRECIO"],
  horario: "VIERNES DE 16:00 A 21:00 HRS",
  legal: "*Sujeto a consumo de alimentos. *Promoción no acumulable con otras ofertas y beneficios.",
};

const FOTOS = {
  S2: {src: "ap-sun2.jpg", zoom: 1.0, cx: 0.5, cy: 0.5, bajar: 0},
  S3: {src: "ap-sun3.jpg", zoom: 1.0, cx: 0.5, cy: 0.5, bajar: 0},
  S4: {src: "ap-sun4.jpg", zoom: 1.0, cx: 0.5, cy: 0.5, bajar: 0},
} as const;
export type QbSunsetSemana = keyof typeof FOTOS;

const LOGO_W = 767;
const LOGO_H = LOGO_W * 576 / 2556;

export const QbStAprobadaSunset: React.FC<{semana: QbSunsetSemana}> = ({semana}) => {
  const f = FOTOS[semana];
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoQB src={`assets/hilton/qb/oct/${f.src}`} ratio={1500 / 2250} zoom={f.zoom} cx={f.cx} cy={f.cy} bajar={f.bajar} />
      <Velo arriba={[760, 0.72]} abajo={[620, 0.8]} />
      <Img src={staticFile("assets/hilton/qb/oct/sunset-qb-logo.png")}
        style={{position: "absolute", top: 346, left: (MESA.w - LOGO_W) / 2, width: LOGO_W, height: LOGO_H}} />
      {/* velo local para leer el titular sobre los tragos */}
      <div style={{position: "absolute", left: -60, width: MESA.w + 120, top: 1080, height: 380,
        background: "radial-gradient(ellipse 50% 50% at 50% 50%, rgba(0,0,0,.62) 0%, rgba(0,0,0,.42) 55%, rgba(0,0,0,0) 100%)"}} />
      <Linea top={1170 - 25} cuerpo={85} peso={300} tracking="0.01em" interlinea={0.94}>
        {QB_SUNSET_AP_DATA.titular[0]}<br />{QB_SUNSET_AP_DATA.titular[1]}
      </Linea>
      <BotonVerde top={1332} ancho={560} alto={54} cuerpo={30} peso={700}>{QB_SUNSET_AP_DATA.horario}</BotonVerde>
      <Legal top={1530} cuerpo={19}>{QB_SUNSET_AP_DATA.legal}</Legal>
    </AbsoluteFill>
  );
};
