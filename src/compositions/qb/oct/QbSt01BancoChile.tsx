/**
 * QB · ST 01-10 · 19:00 · ESTÁTICA — DESCUENTOS BANCO DE CHILE
 *
 * BRIEF (grilla octubre, STORIES col. C, OK PARA DISEÑAR, sin comentario):
 *   Tomar como referencia la imagen adjunta, mostrando una escena más sofisticada
 *   y aspiracional, con foco en la experiencia QB. Mesa elegante con platos
 *   servidos y copas de vino blanco o cocktail en primer plano, ambiente cálido,
 *   íntimo y premium. Fondo levemente desenfocado, iluminación tenue.
 *   Texto: TU SEMANA TIENE MÁS DE UN BUEN MOMENTO EN QB · Banco de Chile ·
 *   20% OFF · Lunes a viernes · 30% OFF · Sábados y domingos · legal.
 *   Interacción: LINK RESERVA MESAS
 *
 * REFERENCIA: Pinterest 926474954604695142 (Lobster) — mesa oscura, dos copas de
 * blanco y platos abajo, el titular arriba sobre el ambiente oscuro.
 *
 * DIRECCIÓN DE ARTE
 *   · Foto REAL: brindis con vino blanco sobre el pescado y el risotto de camarón
 *     (sesión «2026 | Shooting QB orgánico», IMG_3088, t=3,61 s, HLG tonemapeado),
 *     gradada tenue y cálida en `scripts/qb-oct-fondos.py`. Sin IA → sin
 *     «Imagen referencial».
 *   · La foto se achica y baja (lienzo negro arriba) para dejar el aire del
 *     titular, como en la referencia; la mesa negra se funde con el negro.
 *   · ⭐ El logotipo hace de PALABRA en la frase («…EN [QB]») — el recurso más
 *     propio de la marca (manual §4b).
 *   · PROMO → puede ir a paid (Eli, 24-09): todo el texto dentro de 250/340/115.
 *   · Regla Hilton §F: títulos y bajadas sin punto; el legal sí.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BotonVerde, cargarFuentesQbOct, FotoQB, Legal, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST01_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "TU SEMANA TIENE MÁS DE UN BUEN MOMENTO EN QB",
  etiqueta: "Banco de Chile",
  texto: "20% OFF · LUNES A VIERNES",
  pie: "30% OFF · SÁBADOS Y DOMINGOS",
  legal: "Sujeto a consumo de alimentos. Promoción no acumulable con otras ofertas y beneficios.",
  },
};

export const QbSt01BancoChile: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/01-bancochile.jpg" ratio={2250 / 4000} zoom={1.18} libre
      cx={0.5} cy={0.42} bajar={215} />
    {/* la costura de arriba de la foto se funde a negro */}
    <div style={{position: "absolute", top: 0, left: 0, right: 0, height: 215 + 260,
      background: "linear-gradient(180deg, #000 0%, #000 45%, rgba(0,0,0,0) 100%)"}} />
    <div style={{position: "absolute", top: 0, bottom: 0, left: 0, width: 220,
      background: "linear-gradient(90deg, rgba(0,0,0,.85), rgba(0,0,0,0))"}} />
    <Velo arriba={[760, 1]} abajo={[1000, 1]} />
    <Linea top={262} cuerpo={50} peso={300} tracking="0.06em">TU SEMANA TIENE</Linea>
    <Linea top={322} cuerpo={50} peso={800} tracking="0.03em">MÁS DE UN BUEN MOMENTO EN</Linea>
    <LogoQB top={398} ancho={190} />
    <Linea top={1300} cuerpo={60} familia="BellMT" italica>{QB_ST01_DATA.pieza.etiqueta}</Linea>
    <BotonVerde top={1386} ancho={640} alto={72} cuerpo={36} peso={800}>{QB_ST01_DATA.pieza.texto}</BotonVerde>
    <BotonVerde top={1466} ancho={640} alto={72} cuerpo={36} peso={800}>{QB_ST01_DATA.pieza.pie}</BotonVerde>
    <Legal top={1552} cuerpo={17}>{QB_ST01_DATA.pieza.legal}</Legal>
  </AbsoluteFill>
);
