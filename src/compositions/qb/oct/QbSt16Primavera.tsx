/**
 * QB · ST 16-10 · 12:00 · ESTÁTICA — TRAGOS PARA DISFRUTAR EN PRIMAVERA  (ST n°5 S2)
 *
 * BRIEF (grilla octubre, STORIES col. O, OK PARA DISEÑAR desde el 28-09 tarde):
 *   La línea de la story de trago de autor de septiembre, más fresca y
 *   estacional: UN solo cocktail protagonista, idealmente un spritz, luminoso,
 *   de tarde de primavera; cítricos o hierbas sutiles. Texto: LA PRIMAVERA SE
 *   SIRVE EN COPA. Interacción: link CARTA.
 * COMENTARIO DEL CLIENTE: «Veamos una opción similar a la que hicimos con trago
 *   de autor en septiembre y que tenga enlace a la carta. Con un texto único que
 *   diga lo de la primavera también se sirve en copa y pongamos solo la foto de
 *   un spritz».
 *
 * DIRECCIÓN DE ARTE
 *   · El molde es la ST3-S3 de septiembre («Revisa nuestra carta de tragos» +
 *     Afrodita): logo arriba, antetítulo chico en Raleway + serif en caja alta,
 *     el trago enmarcado por un filete punteado.
 *   · TEXTO ÚNICO: «LA PRIMAVERA» (Raleway) / «SE SIRVE EN COPA» (Bell MT). Sin
 *     nombre de trago, como pidió el cliente.
 *   · Foto: el spritz REAL de la sesión de la carta (Cerveza Atenea 23), aislado
 *     con Seedream (sin la cerveza ni las costillas), a la luz de una tarde de
 *     primavera sobre la mesa de la terraza → «Imagen referencial».
 *   · Aire bajo el trago para el sticker del link a la carta.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {cargarFuentesQbOct, FotoQB, ImagenReferencial, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST16_DATA: Record<string, Record<string, string>> = {
  pieza: {
  antetitulo: "LA PRIMAVERA",
  titular: "SE SIRVE EN COPA",
  },
};

export const QbSt16Primavera: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/16-primavera.jpg" ratio={1520 / 2736} />
    <Velo arriba={[640, 0.72]} abajo={[420, 0.55]} />
    <LogoQB top={250} ancho={170} />
    <Linea top={384} cuerpo={34} peso={500} tracking="0.12em">{QB_ST16_DATA.pieza.antetitulo}</Linea>
    <Linea top={428} cuerpo={76} familia="BellMT" tracking="0.02em">{QB_ST16_DATA.pieza.titular}</Linea>
    {/* ⭐ r10 (Eli): «que se vean más similares las líneas discontinuas» a la ST3-S3
        de septiembre. Medido allá: trazo de ~1,5 px, guion corto, verde menta
        claro, y el marco CORRIDO a la izquierda de la copa: nace fuera y termina
        dentro de ella (en sept: x 173–724, y 776–1566 con la copa en 244–818). */}
    <svg width={1080} height={1920} style={{position: "absolute", left: 0, top: 0}}>
      <rect x={361} y={548} width={522} height={1150} fill="none" stroke="#A9CDB3"
        strokeOpacity={0.9} strokeWidth={1.6} strokeDasharray="9 6" />
    </svg>
    <ImagenReferencial top={1556} />
  </AbsoluteFill>
);
