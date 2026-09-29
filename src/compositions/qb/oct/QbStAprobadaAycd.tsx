/**
 * QB · ST 13-10 · 27-10 · 12:00 · ESTÁTICA — «ST APROBADA | ALL YOU CAN DRINK»
 *
 * GRILLA (STORIES, 2 columnas en APROBADO, sin brief propio; interacción «LINK
 * RESERVA MESA»): contenido marca que se republica la ST aprobada de AYCD.
 *
 * Eli 29-09: «guíate de las referencias que da contenido, pero hay elementos que
 * conservar: logos, nombres importantes y legales».
 *
 * DIRECCIÓN DE ARTE
 *   · PLANTILLA APROBADA: la ST de AYCD de septiembre 2026
 *     (`raw/hilton/qb/aprobadas/AYCD-ST-sep2026.png`). El bloque del KV no varía
 *     (R-04): logo, nombre con sus cortes, TODOS LOS MARTES / botón POR $13.990 con
 *     degradado / 18:00 a 21:00 hrs, con las medidas de `QB_AYCD`. Se conservan el
 *     legal y la lista de tragos del AYCD (R-56) tal como los trae la aprobada.
 *   · FOTO: la variable, siempre con tragos del AYCD (R-56):
 *       13-10 → la foto limpia de la misma ST aprobada de septiembre (sangría,
 *               Ramazzotti y espumante en la barra), su encuadre de historia.
 *               No consta que sea real → lleva «Imagen referencial» (R-26).
 *       27-10 → la copa de Ramazzotti en la mano, REAL («Fotos 4 agosto»,
 *               IMG_4756), bajada para que el nombre no la pise.
 *     ⛔ Descartadas el 29-09: fotos con personas (el nombre cae en las caras y el
 *     bloque en los tragos) y el brindis IMG_4822, porque el schop es KUNSTMANN y
 *     el del AYCD es Heineken.
 *   · PROMO → paid: logo y nombre bajan 45 px (tope ≥ 250) y el bloque sube 90 px
 *     para que el legal (19 px, R-52) y la lista de tragos cierren antes de 1580.
 *     En la aprobada ambos caían fuera de la zona segura (1635 y 1830): E-06.
 *
 * ⭐ RONDA 16 (Eli 29-09, 13-10): «se ve mucho legal y muy pesado… deja como un
 *   margen», el legal en dos líneas de párrafo como máximo. Con «Imagen referencial»
 *   el legal ocupa 2 líneas y la lista de tragos quedaba pegada debajo: la lista baja
 *   26 px (margen) y cierra en 1580, el borde de la zona segura. La 27-10 no cambia.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BloqueAycd, cargarFuentesQbOct, FotoQB, Legal, Linea, LogoQB, NombreAycd, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_AYCD_AP_DATA = {
  referencial: "*Imagen referencial. ",
  legal: "*Sujeto a consumo de alimentos. *Promoción no acumulable con otras ofertas y beneficios.",
  legal1: "*Sujeto a consumo de alimentos.",
  legal2: "*Promoción no acumulable con otras ofertas y beneficios.",
  tragos: ["Schop Heineken - Piscola 35° (Mistral o Alto del Carmen) - Ramazzotti",
    "Sangría - Copa de espumante (opción de la casa)"],
};

const FOTOS = {
  "13": {src: "ap-aycd13.jpg", ratio: 1575 / 2800, zoom: 1, cx: 0.5, cy: 0.5, referencial: true},
  "27": {src: "ap-aycd27.jpg", ratio: 1866 / 2800, zoom: 1.18, cx: 0.5, cy: 0.436, referencial: false},
} as const;
export type QbAycdFecha = keyof typeof FOTOS;

const BAJA = 45;
const SUBE = 90;

export const QbStAprobadaAycd: React.FC<{fecha: QbAycdFecha}> = ({fecha}) => {
  const f = FOTOS[fecha];
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoQB src={`assets/hilton/qb/oct/${f.src}`} ratio={f.ratio} zoom={f.zoom} cx={f.cx} cy={f.cy} />
      <Velo arriba={[760, 0.88]} abajo={[820, 0.95]} />
      <LogoQB top={207.4 + BAJA} ancho={178.6} />
      <NombreAycd top={376.3 + BAJA} />
      <BloqueAycd antetitulo={1311.4 - SUBE} boton={1364.6 - SUBE} horario={1479.4 - SUBE} />
      <Legal top={1452} cuerpo={19}>{/* Constanza 29-09: con «Imagen referencial» el legal se alarga y dejaba «beneficios» sola → corte por frase */}
        {f.referencial ? <>{QB_AYCD_AP_DATA.referencial}{QB_AYCD_AP_DATA.legal1}<br />{QB_AYCD_AP_DATA.legal2}</> : QB_AYCD_AP_DATA.legal}</Legal>
      <Linea top={f.referencial ? 1526 : 1500} cuerpo={20} italica peso={400} interlinea={1.35} sombra={false}
        color="rgba(255,255,255,0.9)" ancho={900}>
        {QB_AYCD_AP_DATA.tragos[0]}<br />{QB_AYCD_AP_DATA.tragos[1]}
      </Linea>
    </AbsoluteFill>
  );
};
