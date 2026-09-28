/**
 * QB · FEED 12-10 · 13:00 · CARRUSEL — SUNSET QB  (C1 S2 N°1 / N°2)
 *
 * BRIEF (grilla octubre, FEED col. J, OK PARA DISEÑAR desde el 28-09 tarde):
 *   Momento social, 4 cocktails brindando en primer plano, atmósfera cálida tipo
 *   golden hour; sensación de viernes y panorama; tragos frescos y distintos.
 *   Slide 1 — Portada: imagen de tragos de la promo en spot QB.
 *   Slide 2 — Promo: SUNSET QB · EL VIERNES SE ALARGA CUANDO EL PLAN ESTÁ BUENO ·
 *   DE 16:00 A 21:00 HRS · legal.
 * COMENTARIO DEL CLIENTE: «Mismo comentario que para AYCD» → G1 limpia y la
 *   promo después (R-42).
 *
 * REFERENCIAS: imagen Pinterest 426012446024699408 (brindis) y diseño
 * 1027876314974509589 (mesa con gente, primer plano desenfocado).
 *
 * DIRECCIÓN DE ARTE
 *   · G1 LIMPIA: foto real «Fotos 4 agosto» IMG_4796 — cuatro manos brindando con
 *     cuatro tragos distintos sobre la mesa de madera de QB, luz cálida.
 *   · G2 = el post Sunset aprobado («Post n°2 QB SUNSET»): el logo «Sunset QB»
 *     tal cual, titular en Raleway fina en caja alta, la pastilla verde con el
 *     horario y el legal chico. Fondo: la toma hermana IMG_4797 con velo.
 *   · Sin punto final en el titular (regla Hilton). Todo real → sin «Imagen
 *     referencial».
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {BotonVerde, cargarFuentesQbOct, Legal, Linea, Velo} from "./QbOctKit";
import {FEED, FotoFeed} from "./QbFeedKit";

cargarFuentesQbOct();

const QB_FEED12_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "EL VIERNES SE ALARGA CUANDO EL PLAN ESTÁ BUENO",
  horario: "DE 16:00 A 21:00 HRS",
  legal: "*Sujeto a consumo de alimentos. *Promoción no acumulable con otras ofertas y beneficios.",
  },
};

const LOGO_W = 700;
const LOGO_H = LOGO_W * 576 / 2556;

export const QbFeed12SunsetG1: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoFeed src="assets/hilton/qb/oct/feed12-g1.jpg" pos="50% 45%" />
  </AbsoluteFill>
);

export const QbFeed12SunsetG2: React.FC = () => {
  const d = QB_FEED12_DATA.pieza;
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoFeed src="assets/hilton/qb/oct/feed12-g2.jpg" pos="50% 40%" />
      <Velo arriba={[520, 0.8]} abajo={[700, 0.9]} />
      <Img src={staticFile("assets/hilton/qb/oct/sunset-qb-logo.png")}
        style={{position: "absolute", top: 110, left: (FEED.w - LOGO_W) / 2, width: LOGO_W, height: LOGO_H}} />
      <Linea top={846} cuerpo={60} peso={300} tracking="0.01em" interlinea={1.05}>
        EL VIERNES SE ALARGA<br />CUANDO EL PLAN ESTÁ BUENO
      </Linea>
      <BotonVerde top={1000} ancho={470} alto={52} cuerpo={28} peso={700}>{d.horario}</BotonVerde>
      <Legal top={1090} cuerpo={19}>{d.legal}</Legal>
    </AbsoluteFill>
  );
};
