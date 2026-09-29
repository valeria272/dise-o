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
 * ⭐ RONDA 17 (Eli 29-09, 13-10): «que imagen referencial, sujeto a consumo de alimentos
 *   y promoción no acumulable estén en la misma línea… y luego los tragos, porque son
 *   distintos del legal… los cócteles no son tanto legal: aumenta un poco el tamaño y
 *   ordénalos mejor». → El legal va en UNA línea (18 px, 1000 de ancho) y debajo, con
 *   margen, la lista de tragos a 24 px en Raleway recta (no itálica, para que no se lea
 *   como legal), en dos líneas parejas separadas por «·».
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BloqueAycd, cargarFuentesQbOct, FotoQB, Legal, Linea, LogoQB, NombreAycd, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_AYCD_AP_DATA = {
  referencial: "*Imagen referencial. ",
  legal: "*Sujeto a consumo de alimentos. *Promoción no acumulable con otras ofertas y beneficios.",
  tragos: ["Schop Heineken - Piscola 35° (Mistral o Alto del Carmen) - Ramazzotti",
    "Sangría - Copa de espumante (opción de la casa)"],
  /** r17: los mismos tragos, reordenados en dos líneas parejas. */
  tragosOrden: ["Schop Heineken · Piscola 35° (Mistral o Alto del Carmen)",
    "Ramazzotti · Sangría · Copa de espumante (opción de la casa)"],
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
      {/* r17-r18 (Eli 29-09): el legal entero en UNA línea (19 px con «Imagen referencial»,
          22 sin) y la lista de tragos aparte, más grande y recta. La 27-10 igual que la 13-10 */}
      <Legal top={1452} cuerpo={f.referencial ? 19 : 22} unaLinea>
        {f.referencial ? QB_AYCD_AP_DATA.referencial : ""}{QB_AYCD_AP_DATA.legal}
      </Legal>
      <Linea top={1500} cuerpo={24} peso={400} interlinea={1.4} sombra={false}
        color="rgba(255,255,255,0.95)" ancho={960}>
        {QB_AYCD_AP_DATA.tragosOrden[0]}<br />{QB_AYCD_AP_DATA.tragosOrden[1]}
      </Linea>
    </AbsoluteFill>
  );
};
