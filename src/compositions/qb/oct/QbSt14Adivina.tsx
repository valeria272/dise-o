/**
 * QB · ST 14-10 · 13:00 · ESTÁTICA — DINÁMICA «ADIVINA EL TRAGO»
 *
 * BRIEF (STORIES col. J, OK PARA DISEÑAR):
 *   Trago Aperol. La pieza debe mostrar el trago desenfocado al fondo, ocupando
 *   buena parte de la composición, para que se intuya su forma, color o tipo de
 *   copa, pero sin revelar demasiado. En primer plano o al centro: un título
 *   claro + las pistas en formato emojis.
 *   Texto: ADIVINA EL TRAGO · PISTAS: 🍊 🫧 🥂 · Bajada: ¿Sabes cuál es?
 *   Responde y participa por xxxx · Interacción: [STICKER ENCUESTA]
 *
 * ⭐ COMENTARIO DEL CLIENTE: «Ok, pero con alternativas, siento que cuadro de
 * respuesta no responden». ⇒ Se pasa de caja de respuesta a ENCUESTA CON
 * ALTERNATIVAS, como la trivia de septiembre (ST n°7 S2: «Al Mojito · Al
 * Margarita · Al Terremoto»). Las tres alternativas las propone diseño y las
 * valida contenido: Aperol Spritz (la correcta) · Mimosa · Negroni — las dos
 * falsas calzan con alguna pista (naranja, burbujas) para que no sea obvia.
 * En la pieza queda el espacio del sticker de encuesta de Instagram.
 *
 * ⭐ RONDA DEL CLIENTE (grilla leída el 25-09-2026): borró «Responde y participa
 * por xxxx» de la bajada y fijó las alternativas en INTERACCIÓN:
 *   «Aperol ✅ · Ramazzotti Rosato · St. Germain · Sangría»
 * ⇒ van las cuatro, literales y en ese orden, y el pie se va. El ✅ es la
 * respuesta para contenido: NO se marca en la pieza (regalaría la adivinanza).
 *
 * REFERENCIA: Pinterest 57280226507224461 («Guess the Destination») — título +
 * pastilla con los emojis.
 *
 * DIRECCIÓN DE ARTE
 *   · Foto REAL desenfocada: el spritz de Aperol de la terraza (IMG_3077 t=2 s).
 *   · ⭐ Ronda de Eli 25-09: «se ve un poco feo… estás usando muchas tipografías,
 *     sólo usa Raleway; en ADIVINA puede ir la distinta, Bell». ⇒ Bell MT itálica
 *     SÓLO en «Adivina»; todo lo demás en Raleway. Fuera el formulario de cajas
 *     con letras: las pistas van en tres círculos de línea fina y las cuatro
 *     alternativas en una grilla 2×2 de fichas limpias.
 *   · Todo dentro de la zona segura de Instagram (250 arriba · 340 abajo).
 *   · Orgánica.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {cargarFuentesQbOct, FotoQB, Linea, LogoQB, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST14_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "ADIVINA EL TRAGO",
  etiqueta: "PISTAS",
  texto: "¿Sabes cuál es?",
  frase: "Aperol · Ramazzotti Rosato · St. Germain · Sangría",
  },
};

const Ficha: React.FC<{x: number; y: number; texto: string}> = ({x, y, texto}) => (
  <div style={{position: "absolute", left: x, top: y, width: 404, height: 96,
    border: "1.5px solid rgba(255,255,255,.75)", background: "rgba(10,14,11,.38)",
    display: "flex", alignItems: "center", justifyContent: "center", color: "#fff",
    fontFamily: "Raleway", fontWeight: 600, fontSize: 32, letterSpacing: "0.06em",
    textTransform: "uppercase"}}>{texto}</div>
);

const Pista: React.FC<{x: number; e: string}> = ({x, e}) => (
  <div style={{position: "absolute", left: x, top: 846, width: 150, height: 150, borderRadius: "50%",
    border: "1.5px solid rgba(255,255,255,.8)", background: "rgba(10,14,11,.3)",
    display: "flex", alignItems: "center", justifyContent: "center", fontSize: 78,
    fontFamily: "'Segoe UI Emoji','Noto Color Emoji',sans-serif"}}>{e}</div>
);

const G = 24;                         // separación entre fichas
const X0 = (MESA.w - 404 * 2 - G) / 2;
const P0 = (MESA.w - 150 * 3 - 60 * 2) / 2;

export const QbSt14Adivina: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/14-adivina.jpg" ratio={2250 / 4000} zoom={1.25} cx={0.58} cy={0.32} />
    <Velo arriba={[620, 0.72]} abajo={[760, 0.86]} plano={0.14} />
    <LogoQB top={250} ancho={130} />
    <Linea top={392} cuerpo={176} familia="BellMT" italica>Adivina</Linea>
    <Linea top={600} cuerpo={56} peso={800} tracking="0.3em">EL TRAGO</Linea>
    <div style={{position: "absolute", top: 706, left: (MESA.w - 120) / 2, width: 120, height: 2,
      background: "rgba(255,255,255,.7)"}} />
    <Linea top={770} cuerpo={28} peso={600} tracking="0.4em">PISTAS</Linea>
    <Pista x={P0} e="🍊" />
    <Pista x={P0 + 210} e="🫧" />
    <Pista x={P0 + 420} e="🥂" />
    <Linea top={1070} cuerpo={46} peso={500} italica>{QB_ST14_DATA.pieza.texto}</Linea>
    <Ficha x={X0} y={1162} texto="Aperol" />
    <Ficha x={X0 + 404 + G} y={1162} texto="Ramazzotti Rosato" />
    <Ficha x={X0} y={1162 + 96 + G} texto="St. Germain" />
    <Ficha x={X0 + 404 + G} y={1162 + 96 + G} texto="Sangría" />
  </AbsoluteFill>
);
