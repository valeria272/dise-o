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
 *
 * ⭐ RONDA 5-6 DE ELI 28-09: la sangría del centro es la REAL de la ronda 3, y las
 *   tres copas van a la MISMA altura (bordes en una línea): escena editada con
 *   Seedream sobre la de la r4, mismo encuadre.
 * ⭐ RONDA 7 (Eli 28-09): «la copa cambió de forma». Se rehízo: la copa del centro
 *   es la de la r3 con su forma real (bowl tallado, pie largo), agrandada pareja
 *   ~12 % para que su borde quede en la línea de los otros dos (±3 px).
 * ⭐ RONDA 8 (Eli 28-09): «la parte de abajo muy gruesa» → el pie de la copa del
 *   centro pasa a ser fino, como el de las otras dos, sin el nudo del medio.
 * ⭐ RONDA 16 (Eli 29-09, tras el comentario de Constanza): «Tus favoritos, las veces
 *   que quieras tiene que verse más alineado, como en las otras historias: darle un
 *   poco de aire» → del nombre a la línea pasa de 21 a 33 px, lo de Cumpleaños.
 *   «El legal está demasiado pequeño… auméntale el tamaño y déjalo mucho más abajo,
 *   que no destaque» → de 14 a 19 px, en dos líneas cortadas por frase (sin palabras
 *   solas), cerrando en ≈1660: sale de la zona de paid (1580) y queda en la de
 *   Instagram orgánico (1670).
 *
 * ⭐ RONDA 19 — NICOLÁS (contenido, hilo en STORIES!D13, 29-09): «el copón de
 *   sangría debería ser un poquito más grande que las otras 2». No se escala a mano
 *   ([[reescalar-un-producto-en-la-foto]]): Nano Banana Pro regeneró la escena
 *   aprobada con el copón ≈20 % más grande, mismo cristal tallado, mismas frutas;
 *   spritz, flauta, campana, telón y mármol iguales (`raw/hilton/qb/oct-r19/`).
 * ⭐ RONDA 20 (Eli 29-09, con rayas rojas sobre la foto): «quedó demasiado grande; lo que
 *   se refería es que la altura de la copa tiene que ser la misma en las tres». Nueva
 *   generación sobre la escena APROBADA: bordes y fondos de las tres copas en la misma
 *   línea, la sangría del mismo alto que las otras (`06-alturas-v1`).
 * ⭐ RONDA 21 (Eli 29-09): «esos cócteles aún no se alinean, haz de nuevo esa imagen». Con
 *   tres modelos de copa distintos la IA no los iguala (medido: el fondo de las copas iba de
 *   662 a 832 px de alto). Solución: los tres tragos en EL MISMO modelo de copón. Medido en
 *   `06-igual-v2` (5504 px de alto): bordes en 2750 / 2745 / 2752 y fondos de copa en
 *   3545 / 3540 / 3560 → misma línea arriba y abajo.
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
  legal: "*Imagen referencial. Sujeto a consumo de alimentos.",
  legal2: "Promoción no acumulable con otras ofertas y beneficios.",
  },
};

const BAJA = 45;

export const QbSt06Aycd: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    {/* r4 (Eli 28-09): la campana de la ref de Sora — mano con guante que la levanta
        sobre los tres tragos. La foto sube para que los tragos queden entre el
        antetítulo y el bloque de precio; lo que queda abajo es mármol y velo. */}
    <FotoQB src="assets/hilton/qb/oct/06-aycd-igual-r21.jpg" ratio={3072 / 5504} zoom={1.2} cx={0.5} cy={0.6} libre />
    <Velo arriba={[820, 0.9]} abajo={[760, 0.95]} />
    <LogoQB top={207.4 + BAJA} ancho={178.6} />
    <NombreAycd top={376.3 + BAJA} />
    <Linea top={622} cuerpo={34} italica peso={400}>{QB_ST06_DATA.pieza.antetitulo}</Linea>
    {/* 25-09: el bloque sube 30 px para que texto y legal entren en la zona segura */}
    <BloqueAycd antetitulo={1281.4} boton={1334.6} horario={1449.4} />
    <Linea top={1508} cuerpo={27} italica peso={300}>{QB_ST06_DATA.pieza.texto}</Linea>
    {/* r20 (Eli 29-09): en HISTORIAS el legal va más abajo, al pie (≈1748), «casi para siempre» */}
    <Legal top={1748} cuerpo={19}>{QB_ST06_DATA.pieza.legal}<br />{QB_ST06_DATA.pieza.legal2}</Legal>
  </AbsoluteFill>
);
