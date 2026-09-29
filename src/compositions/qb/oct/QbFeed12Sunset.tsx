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
 *   · ⭐ RONDA 10 (Eli 28-09): «el texto… que sea igual a la referencia y déjalo más
 *     abajo, tal cual la referencia; unos 5 px o menos de espacio abajo con el de
 *     16 a 21 hrs; eso en puntas redondeadas, más abajo y con el verde clarito de
 *     QB; y el legal más abajo, cerca del fondo negrito». Medido sobre «Post n°2 QB
 *     SUNSET»: titular Raleway Light grande con el interlineado apretado (casi sin
 *     aire entre líneas), la pastilla pegada debajo y el legal al pie. El titular
 *     es más largo que «TUS FAVORITOS AL MEJOR PRECIO», así que va en 3 líneas.
 *     Pastilla en #66886B, redondeada.
 *   · ⭐ RONDA 11 (Eli 28-09): «el tamaño estaba bien el anterior, sólo decía que lo
 *     bajaras más, que no tape ni esté cerca de las manos: desde "el viernes" hasta
 *     el "sujeto a", todo más abajo». → titular de vuelta a 60 px en 2 líneas (r9)
 *     y el bloque entero baja: titular, pastilla a 5 px y legal al pie.
 *   · Sin punto final en el titular (regla Hilton). Todo real → sin «Imagen
 *     referencial».
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {cargarFuentesQbOct, CIFRAS, Legal, Linea, Velo} from "./QbOctKit";
import {FEED, FotoFeed} from "./QbFeedKit";

cargarFuentesQbOct();

const QB_FEED12_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "EL VIERNES SE ALARGA CUANDO EL PLAN ESTÁ BUENO",
  horario: "DE 16:00 A 21:00 HRS",
  legal: "*Sujeto a consumo de alimentos. *Promoción no acumulable con otras ofertas y beneficios.",
  },
};

/** Tope de la caja del titular y de la pastilla (medidos en el render: 5 px entre la
 *  base de «ESTÁ BUENO» y la pastilla). */
const TIT = 1030;
/** r12 (Eli 28-09): «centra el botón verde» → al medio entre la base del titular
 *  (1144) y el tope del legal (≈1256). */
const PASTILLA = 1175;

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
      <Velo arriba={[520, 0.8]} abajo={[620, 0.94]} />
      <Img src={staticFile("assets/hilton/qb/oct/sunset-qb-logo.png")}
        style={{position: "absolute", top: 110, left: (FEED.w - LOGO_W) / 2, width: LOGO_W, height: LOGO_H}} />
      <Linea top={TIT} cuerpo={60} peso={300} tracking="0.01em" interlinea={1.05}>
        EL VIERNES SE ALARGA<br />CUANDO EL PLAN ESTÁ BUENO
      </Linea>
      {/* pastilla redondeada en el verde claro de QB, ~5 px bajo el titular */}
      {/* r13 (Eli marcó el ancho con dos rayas en la captura): 585 px, centrado */}
      <div style={{position: "absolute", top: PASTILLA, left: (FEED.w - 585) / 2, width: 585, height: 50,
        borderRadius: 25, background: "#66886B", display: "flex", alignItems: "center",
        justifyContent: "center", paddingTop: 2, color: "#fff", fontFamily: "Raleway", fontWeight: 700,
        fontSize: 28, letterSpacing: "0.02em", ...CIFRAS}}>{d.horario}</div>
      {/* r18 (Eli 29-09): de 19 a 22 px, en una línea */}
      <Legal top={1248} cuerpo={22} unaLinea>{d.legal}</Legal>
    </AbsoluteFill>
  );
};
