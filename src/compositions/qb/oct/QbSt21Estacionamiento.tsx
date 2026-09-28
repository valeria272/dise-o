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
  *
 * ⭐ RONDA 4 DE ELI 28-09: parecerse a la ref (Autcomm, las cartas del zodiaco).
 *   · FONDO de plantas tropicales con sol, como la ref: la misma mano y el mismo
 *     ticket de la foto anterior, fondo cambiado con Seedream (edición).
 *   · El TICKET se imprime como la carta de la ref: filete interior, dos reglas
 *     que encierran el texto, serif (Bell MT) con la línea clave en itálica, y la
 *     tinta en el verde de QB. El bloque de texto baja para no quedar bajo el
 *     pulgar, que tapa el tercio derecho a media altura.
 *   · El STICKER de estrella de la ref, en crema, montado en la esquina.
 *   Ticket medido en la foto nueva: centro (529, 987), 294×677, −9,2°.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS, QB_LOGO} from "../../../brand/qb";
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

const TICKET = {cx: 529, cy: 987, w: 294, h: 677, ang: -9.16} as const;
const TINTA = "#2F4635";

/** Estrella de 12 puntas del sticker de la ref. */
const Sticker: React.FC<{x: number; y: number; d: number}> = ({x, y, d}) => {
  const pts: string[] = [];
  for (let k = 0; k < 24; k++) {
    const r = k % 2 === 0 ? d / 2 : d * 0.2;
    const t = (Math.PI * k) / 12 - Math.PI / 2;
    pts.push(`${d / 2 + r * Math.cos(t)},${d / 2 + r * Math.sin(t)}`);
  }
  return (
    <svg style={{position: "absolute", left: x, top: y, filter: "drop-shadow(0 6px 14px rgba(0,0,0,.35))"}}
      width={d} height={d}><polygon points={pts.join(" ")} fill="#F6E6D8" /></svg>
  );
};

export const QbSt21Estacionamiento: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/21-ticket-r4.jpg" ratio={1520 / 2736} />
    <Velo arriba={[640, 0.7]} abajo={[520, 0.8]} />
    <div style={{position: "absolute", left: TICKET.cx - TICKET.w / 2, top: TICKET.cy - TICKET.h / 2,
      width: TICKET.w, height: TICKET.h, transform: `rotate(${TICKET.ang}deg)`,
      mixBlendMode: "multiply", color: TINTA, textAlign: "center", fontFamily: "BellMT",
      filter: "blur(0.3px)", opacity: 0.94, ...CIFRAS}}>
      {/* filete interior, como la carta de la ref */}
      <div style={{position: "absolute", inset: 14, border: `2px solid ${TINTA}`, borderRadius: 10}} />
      <Img src={staticFile(QB_ASSETS.logoBlanco)} style={{position: "absolute", top: 44,
        left: (TICKET.w - 92) / 2, width: 92, height: 92 / QB_LOGO.proporcion, filter: "invert(1)"}} />
      <div style={{position: "absolute", top: 150, left: 44, right: 44, borderTop: `2px solid ${TINTA}`}} />
      <div style={{position: "absolute", top: 168, width: "100%", fontSize: 118, lineHeight: 1}}>50%</div>
      <div style={{position: "absolute", top: 282, width: "100%", fontFamily: "Raleway", fontSize: 40,
        fontWeight: 800, letterSpacing: "0.12em", lineHeight: 1}}>OFF</div>
      {/* pulgar: tapa el tercio derecho entre y≈340 y 470 — el texto va más abajo */}
      <div style={{position: "absolute", top: 470, left: 28, right: 28, fontSize: 34, lineHeight: 1.05}}>
        en tu ticket de<br /><span style={{fontStyle: "italic", fontSize: 36}}>estacionamiento</span>
      </div>
      <div style={{position: "absolute", top: 560, left: 44, right: 44, borderTop: `2px solid ${TINTA}`}} />
      <div style={{position: "absolute", top: 572, left: 20, right: 20, fontFamily: "Raleway", fontSize: 19,
        fontWeight: 400, lineHeight: 1.25}}>Ingreso por<br />Encomenderos 275</div>
    </div>
    <Sticker x={300} y={560} d={150} />
    <LogoQB top={252} ancho={130} />
    <Linea top={356} cuerpo={70} peso={800} tracking="0.01em">{QB_ST21_DATA.pieza.titular}</Linea>
    <Linea top={448} cuerpo={34} peso={400} ancho={880}>{QB_ST21_DATA.pieza.bajada}</Linea>
    <Legal top={1522} cuerpo={20}>{QB_ST21_DATA.pieza.legal}</Legal>
  </AbsoluteFill>
);
