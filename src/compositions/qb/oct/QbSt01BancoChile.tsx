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
 * ⭐⭐ RONDA DE ELI 25-09: «se ve como quemado, muy saturado… usa del shooting
 * nuevo, una foto mucho más bonita, más elegante» · «Banco de Chile y todos los
 * bancos ya tenemos los diseños aprobados, los logos que hay que utilizar».
 *
 * DIRECCIÓN DE ARTE
 *   · PLANTILLA APROBADA: «ST n°1 S1 QB JUL» (carpeta BANCOS que pasó Eli): logo
 *     QB arriba, marco de vidrio con filete verde, pastilla «Banco de Chile»
 *     montada sobre el filete, titular Raleway ExtraBold + Regular, dos cajas
 *     verdes 20%OFF / 30%OFF con el día en una franja oscura debajo, legal en
 *     Raleway itálica y las tarjetas del banco abajo. Medidas tomadas del PNG
 *     aprobado; todo el bloque baja 30 px para que el logo entre en la zona
 *     segura (en la aprobada estaba a 221).
 *   · Pastilla del banco = recorte exacto de la aprobada; tarjetas = «TARJETAS
 *     VISA.png» de los Links del editable de bancos. Nada redibujado.
 *   · FOTO del shooting de la carta de enero 2026 («Ostiones parmesanos a la
 *     batayaki 20»): brindis con vino blanco sobre el risotto y la trucha, mesa
 *     negra. Sin gradación (sólo +4 % de luz).
 *   · Textos literales del brief. «Lunes a viernes» (la aprobada decía «Lunes y
 *     viernes»: errata de esa pieza; manda el brief).
 *   · PROMO → texto dentro de la zona segura de paid (250 · 340).
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {cargarFuentesQbOct, FotoQB, Legal, Linea, LogoQB, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST01_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "TU SEMANA TIENE MÁS DE UN BUEN MOMENTO EN QB",
  etiqueta: "Banco de Chile",
  texto: "20%OFF · Lunes a viernes",
  pie: "30%OFF · Sábados y domingos",
  legal: "Sujeto a consumo de alimentos. Promoción no acumulable con otras ofertas y beneficios.",
  },
};

/** Medidas de la plantilla aprobada (mesa 1080×1920), bajadas 30 px. */
const B = 30;
const MARCO = {x: 87, y: 398 + B, w: 899, h: 322};
const CAJA = {w: 383, h: 92, g: 26, y: 676 + B};
const VERDE_CAJA = "#2F4635";
const VERDE_FILETE = "#35493A";

const Caja: React.FC<{x: number; cifra: string; dia: string}> = ({x, cifra, dia}) => (
  <>
    <div style={{position: "absolute", left: x, top: CAJA.y, width: CAJA.w, height: CAJA.h,
      background: VERDE_CAJA, display: "flex", alignItems: "center", justifyContent: "center",
      color: "#fff", fontFamily: "Raleway", fontWeight: 800, fontSize: 60, letterSpacing: "-0.01em"}}>{cifra}</div>
    <div style={{position: "absolute", left: x, top: CAJA.y + CAJA.h, width: CAJA.w, height: 86,
      background: "rgba(0,0,0,.62)", display: "flex", alignItems: "center", justifyContent: "center",
      color: "#fff", fontFamily: "Raleway", fontWeight: 400, fontSize: 30}}>{dia}</div>
  </>
);

const TARJ_W = 540;

export const QbSt01BancoChile: React.FC = () => {
  const x1 = (MESA.w - (CAJA.w * 2 + CAJA.g)) / 2;
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoQB src="assets/hilton/qb/oct/01-bancochile.jpg" ratio={2250 / 3375} zoom={1.0} cx={0.5} cy={0.5} />
      <Velo arriba={[420, 0.55]} abajo={[620, 0.9]} />
      <LogoQB top={221 + B} ancho={168} />
      {/* marco de vidrio con filete verde */}
      <div style={{position: "absolute", left: MARCO.x, top: MARCO.y, width: MARCO.w, height: MARCO.h,
        border: `5px solid ${VERDE_FILETE}`, borderRadius: 14, background: "rgba(0,0,0,.55)"}} />
      <Img src={staticFile("assets/hilton/qb/oct/logo-banco-chile.png")}
        style={{position: "absolute", left: (MESA.w - 244) / 2, top: 366 + B, width: 244, height: 85}} />
      <Linea top={492 + B} cuerpo={50} peso={800} tracking="0.01em">TU SEMANA TIENE MÁS</Linea>
      <Linea top={552 + B} cuerpo={50} peso={400} tracking="0.01em">DE UN BUEN MOMENTO EN QB</Linea>
      <Caja x={x1} cifra="20%OFF" dia="Lunes a viernes" />
      <Caja x={x1 + CAJA.w + CAJA.g} cifra="30%OFF" dia="Sábados y domingos" />
      <Legal top={1530} cuerpo={22}>{QB_ST01_DATA.pieza.legal}</Legal>
      <Img src={staticFile("assets/hilton/qb/oct/tarjetas-banco-chile.png")}
        style={{position: "absolute", left: (MESA.w - TARJ_W) / 2, top: 1620, width: TARJ_W, height: TARJ_W / 2}} />
    </AbsoluteFill>
  );
};
