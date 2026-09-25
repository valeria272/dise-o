/**
 * QB · ST 21-10 · 18:00 · ESTÁTICA — DESCUENTO ESTACIONAMIENTO
 *
 * BRIEF (STORIES col. R, OK PARA DISEÑAR, sin comentario):
 *   Un ticket de estacionamiento en primer plano sostenido por una mano,
 *   inspirado en la referencia. El texto principal del beneficio va DENTRO del
 *   ticket. Arriba, una pregunta corta que conecte con el usuario.
 *   Texto superior: ¿VIENES EN AUTO? / Tenemos un beneficio para disfrutar más tu
 *   visita. · Dentro del ticket: 50% OFF / EN TU TICKET DE / ESTACIONAMIENTO /
 *   Ingreso por Encomenderos 275 · Legal: Solicita tu ticket a nuestro personal.
 *
 * REFERENCIA: Pinterest 679480662574801544 (tarjeta naranja sostenida en mano).
 *
 * DIRECCIÓN DE ARTE
 *   · Escena GENERADA (Seedream 5 Pro): mano con un ticket en blanco sobre el bar
 *     desenfocado → lleva «Imagen referencial».
 *   · ⛔ El texto del ticket NO lo escribe la IA (manual §4c): se imprime acá con
 *     las fuentes reales, montado sobre el ticket medido por color
 *     (centro 521,990 · 350×678 · −9,8°) y en «multiply», como tinta.
 *   · El ticket lleva el logo de QB impreso arriba y un troquel punteado: se lee
 *     como un ticket y no como una tarjeta.
 *   · PROMO → zona segura de paid.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS, QB_LOGO, qbColores} from "../../../brand/qb";
import {cargarFuentesQbOct, CIFRAS, FotoQB, Legal, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST21_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "¿VIENES EN AUTO?",
  bajada: "Tenemos un beneficio para disfrutar más tu visita",
  etiqueta: "50% OFF",
  texto: "EN TU TICKET DE ESTACIONAMIENTO",
  pie: "Ingreso por Encomenderos 275",
  legal: "*Imagen referencial. Solicita tu ticket a nuestro personal.",
  },
};

const TICKET = {cx: 521, cy: 990, w: 350, h: 678, ang: -9.8} as const;
const TINTA = qbColores.tinta;

export const QbSt21Estacionamiento: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/21-ticket.jpg" ratio={2250 / 4050} zoom={1.0} />
    <Velo arriba={[640, 0.7]} abajo={[520, 0.8]} />
    <div style={{position: "absolute", left: TICKET.cx - TICKET.w / 2, top: TICKET.cy - TICKET.h / 2,
      width: TICKET.w, height: TICKET.h, transform: `rotate(${TICKET.ang}deg)`,
      mixBlendMode: "multiply", color: TINTA, textAlign: "center", fontFamily: "Raleway",
      filter: "blur(0.35px)", opacity: 0.93, ...CIFRAS}}>
      {/* logo impreso — el blanco se invierte a tinta */}
      <Img src={staticFile(QB_ASSETS.logoBlanco)} style={{position: "absolute", top: 46,
        left: (TICKET.w - 96) / 2, width: 96, height: 96 / QB_LOGO.proporcion, filter: "invert(1)"}} />
      <div style={{position: "absolute", top: 128, left: 30, right: 30, borderTop: `2px dashed ${TINTA}`}} />
      <div style={{position: "absolute", top: 150, width: "100%", fontSize: 26, fontWeight: 600,
        letterSpacing: "0.2em"}}>TICKET</div>
      <div style={{position: "absolute", top: 196, width: "100%", fontSize: 92, fontWeight: 800,
        lineHeight: 1, letterSpacing: "-0.01em"}}>50%</div>
      <div style={{position: "absolute", top: 290, width: "100%", fontSize: 50, fontWeight: 800,
        lineHeight: 1}}>OFF</div>
      <div style={{position: "absolute", top: 362, left: 24, right: 24, fontSize: 25, fontWeight: 600,
        lineHeight: 1.3, letterSpacing: "0.04em"}}>EN TU TICKET DE<br />ESTACIONAMIENTO</div>
      <div style={{position: "absolute", top: 452, left: 30, right: 30, borderTop: `2px dashed ${TINTA}`}} />
      <div style={{position: "absolute", top: 470, left: 20, right: 20, fontSize: 22, fontStyle: "italic",
        lineHeight: 1.3}}>Ingreso por<br />Encomenderos 275</div>
    </div>
    <LogoQB top={252} ancho={130} />
    <Linea top={356} cuerpo={70} peso={800} tracking="0.01em">{QB_ST21_DATA.pieza.titular}</Linea>
    <Linea top={448} cuerpo={34} peso={400} ancho={880}>{QB_ST21_DATA.pieza.bajada}</Linea>
    <Legal top={1522} cuerpo={20}>{QB_ST21_DATA.pieza.legal}</Legal>
  </AbsoluteFill>
);
