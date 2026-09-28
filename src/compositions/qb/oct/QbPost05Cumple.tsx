/**
 * QB · FEED 05-10 · 15:00 · ESTÁTICO — CUMPLEAÑOS EN QB
 *
 * BRIEF (grilla octubre, FEED col. D, OK PARA DISEÑAR desde el 28-09):
 *   El rótulo dice «ST ESTÁTICA» y el tipo «CARRUSEL», pero el comentario del
 *   cliente manda: «Aquí dejemos un estático de cumpleaños» → POST estático de
 *   feed, 4:5 (1080×1350, entrega 2250×2813).
 *   Visual: una escena real de celebración en QB, la torta con velas llegando o
 *   el cumpleañero/a con su grupo; nocturna, cálida, flash o luz ambiente; mesa
 *   compartida, amigos, torta y ambiente QB.
 *   Texto: TU CUMPLEAÑOS SE CELEBRA EN QB · Bajada: Convierte tu cumpleaños en
 *   una noche inolvidable · Complementario: 5 tragos de cortesía para el
 *   cumpleañero/a · Shots de regalo · Postre · Cuenta separadas · Puedes traer
 *   tu propia torta.
 *
 * REFERENCIA: Pinterest 1107392995886954044 («Yes! Friday», Gatsby Bar) — un
 * collage de polaroids con flash que llena la pieza, y al centro una tarjeta de
 * lino con el título en pincel y el texto chico en caja alta.
 *
 * DIRECCIÓN DE ARTE
 *   · Las POLAROIDS son el recurso de la ref: marco blanco, giro leve, sombra.
 *     Siete fotos: seis reales del shooting «QB 13 oct» (107 grupo, 101 brindis
 *     con espumante, 108 brindis con tinto, 104 la invitada con el celular, 92 y 93 parejas; sólo invitados, la
 *     108 encuadrada para dejar fuera a la persona de camisa blanca del fondo) y
 *     UNA generada, la torta con bengalas llegando a la mesa, porque no hay
 *     cumpleaños en las sesiones → «Imagen referencial».
 *   · La TARJETA de lino al centro, derecha como en la ref. Título con las voces
 *     de QB: «Tu cumpleaños» en Brushwell (el pincel de la ref) y «SE CELEBRA EN
 *     QB» en Raleway ExtraBold, en el verde de QB. Sin punto final (regla Hilton).
 *   · Textos literales del brief. ⚠️ «Cuenta separadas» va como viene: la
 *     concordancia (¿«Cuentas separadas»?) se consulta a contenido.
 *   · Zona segura de feed: 12 % abajo sin texto (la tarjeta cierra en 890).
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS, QB_LOGO} from "../../../brand/qb";
import {cargarFuentesQbOct, Grano, Linea} from "./QbOctKit";

cargarFuentesQbOct();

const QB_POST05_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "TU CUMPLEAÑOS SE CELEBRA EN QB",
  bajada: "Convierte tu cumpleaños en una noche inolvidable",
  texto: "5 tragos de cortesía para el cumpleañero/a",
  pie: "Shots de regalo · Postre · Cuenta separadas · Puedes traer tu propia torta",
  legal: "*Imagen referencial",
  },
};

const W = 1080;
const VERDE = "#2F4635";

const Polaroid: React.FC<{
  src: string; x: number; y: number; w: number; giro: number; pos?: string; alto?: number;
}> = ({src, x, y, w, giro, pos = "50% 50%", alto = 0.78}) => {
  const b = w * 0.045;
  const hImg = (w - 2 * b) * alto;
  return (
    <div style={{position: "absolute", left: x, top: y, width: w, padding: `${b}px ${b}px ${b * 2.6}px`,
      background: "#FBFAF7", transform: `rotate(${giro}deg)`,
      boxShadow: "0 2px 4px rgba(0,0,0,.35), 0 14px 34px rgba(0,0,0,.5)"}}>
      <Img src={staticFile(`assets/hilton/qb/oct/${src}`)} style={{display: "block", width: "100%",
        height: hImg, objectFit: "cover", objectPosition: pos, filter: "contrast(1.08) saturate(1.05)"}} />
    </div>
  );
};

const TARJETA = {x: 150, y: 300, w: 780, h: 590};

export const QbPost05Cumple: React.FC = () => (
  <AbsoluteFill style={{background: "#15110E"}}>
    {/* fila de arriba */}
    <Polaroid src="05-cumple-107.jpg" x={-50} y={-40} w={430} giro={-4} pos="50% 55%" />
    <Polaroid src="05-cumple-101.jpg" x={330} y={-70} w={420} giro={3} pos="55% 40%" />
    <Polaroid src="05-cumple-108.jpg" x={710} y={-30} w={430} giro={-2.5} pos="30% 45%" />
    {/* costados, medio escondidas tras la tarjeta */}
    <Polaroid src="05-cumple-92.jpg" x={-120} y={380} w={330} giro={4} pos="30% 40%" alto={1.1} />
    <Polaroid src="05-cumple-93.jpg" x={880} y={420} w={330} giro={-3.5} pos="45% 35%" alto={1.1} />
    {/* la tarjeta de lino */}
    <div style={{position: "absolute", left: TARJETA.x, top: TARJETA.y, width: TARJETA.w, height: TARJETA.h,
      background: "#EEE6D8", boxShadow: "0 3px 6px rgba(0,0,0,.3), 0 20px 50px rgba(0,0,0,.55)",
      backgroundImage: "repeating-linear-gradient(0deg, rgba(90,70,40,.05) 0 1px, transparent 1px 4px), repeating-linear-gradient(90deg, rgba(90,70,40,.05) 0 1px, transparent 1px 4px)"}} />
    <Img src={staticFile(QB_ASSETS.logoBlanco)} style={{position: "absolute", top: TARJETA.y + 52,
      left: (W - 110) / 2, width: 110, height: 110 / QB_LOGO.proporcion,
      filter: "brightness(0) saturate(100%) invert(22%) sepia(14%) saturate(900%) hue-rotate(83deg) brightness(92%)"}} />
    <Linea top={TARJETA.y + 128} cuerpo={150} familia="Brushwell" color={VERDE} sombra={false} interlinea={1}>
      Tu cumpleaños
    </Linea>
    <Linea top={TARJETA.y + 290} cuerpo={48} peso={800} tracking="0.08em" color={VERDE} sombra={false}>
      SE CELEBRA EN QB
    </Linea>
    <Linea top={TARJETA.y + 358} cuerpo={27} italica peso={400} color="#3A332C" sombra={false} ancho={740}>
      {QB_POST05_DATA.pieza.bajada}
    </Linea>
    <div style={{position: "absolute", top: TARJETA.y + 412, left: (W - 160) / 2, width: 160,
      borderTop: `2px solid ${VERDE}`, opacity: 0.6}} />
    <Linea top={TARJETA.y + 434} cuerpo={21} peso={700} tracking="0.08em" mayus color={VERDE} sombra={false} ancho={740}>
      {QB_POST05_DATA.pieza.texto}
    </Linea>
    <Linea top={TARJETA.y + 470} cuerpo={18} peso={500} tracking="0.08em" mayus color="#3A332C" sombra={false}
      ancho={740} interlinea={1.5}>
      Shots de regalo · Postre · Cuenta separadas<br />Puedes traer tu propia torta
    </Linea>
    <Linea top={TARJETA.y + 546} cuerpo={14} italica color="#6B6259" sombra={false} ancho={400}>
      {QB_POST05_DATA.pieza.legal}
    </Linea>
    {/* fila de abajo: la torta (generada) y un brindis */}
    <Polaroid src="05-cumple-torta.jpg" x={-30} y={912} w={560} giro={-3} pos="50% 55%" />
    <Polaroid src="05-cumple-104.jpg" x={560} y={930} w={540} giro={3.5} pos="50% 40%" />
    <Grano />
  </AbsoluteFill>
);
