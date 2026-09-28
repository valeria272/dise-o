/**
 * QB · FEED 16-10 · 18:00 · ESTÁTICO — TRAGO DE AUTOR QB  (Post n°1 S2)
 *
 * BRIEF (grilla octubre, FEED col. M, OK PARA DISEÑAR desde el 28-09 tarde):
 *   Una mano sosteniendo el cocktail en primer plano, el trago protagonista
 *   absoluto; un trago de autor de QB (Zeus, Artemisa o Eros, el más llamativo);
 *   fresco, sofisticado, editorial / premium.
 * COMENTARIO DEL CLIENTE: «Ok pero dejemos gráfica + limpia, sin los textos y
 *   estrellas» (la ref trae cuatro cajas de reseñas con estrellas).
 *
 * REFERENCIA: Pinterest 1075164111061413116 — mano con la palma arriba
 * sosteniendo un vaso tallado, telón de terciopelo ocre, reseñas con estrellas.
 *
 * DIRECCIÓN DE ARTE
 *   · ⚠️ Zeus, Artemisa y Eros NO están en la sesión de coctelería 11-09. Eli
 *     eligió el 28-09 usar AFRODITA (el de la ST de tragos de septiembre).
 *   · Foto: la real «_DSC9911 AFRODITA» puesta en una mano con Seedream (vaso,
 *     humo, romero y flores iguales), barra de QB desenfocada detrás →
 *     «Imagen referencial».
 *   · LIMPIA como pidió el cliente: sin reseñas, sin estrellas, sin titular. Sólo
 *     el logo arriba y la leyenda obligatoria abajo, dentro de la zona segura.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {cargarFuentesQbOct, Grano, Linea, LogoQB} from "./QbOctKit";
import {FotoFeed} from "./QbFeedKit";

cargarFuentesQbOct();

const QB_FEED16_DATA: Record<string, Record<string, string>> = {
  pieza: {
  legal: "*Imagen referencial",
  },
};

export const QbFeed16Autor: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoFeed src="assets/hilton/qb/oct/feed16-autor.jpg" pos="50% 60%" />
    <div style={{position: "absolute", left: 0, right: 0, top: 0, height: 300,
      background: "linear-gradient(180deg, rgba(0,0,0,.55), rgba(0,0,0,0))"}} />
    <LogoQB top={80} ancho={150} />
    <Linea top={1150} cuerpo={17} italica sombra ancho={500} color="rgba(255,255,255,0.8)">
      {QB_FEED16_DATA.pieza.legal}
    </Linea>
    <Grano />
  </AbsoluteFill>
);
