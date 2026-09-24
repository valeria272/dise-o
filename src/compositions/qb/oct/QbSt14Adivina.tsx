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
 * ⚠️ «Responde y participa por xxxx»: el premio lo confirma Eli (24-09). Va
 * literal con «xxxx» para que nadie lo publique por error.
 *
 * REFERENCIA: Pinterest 57280226507224461 («Guess the Destination») — título +
 * pastilla con los emojis.
 *
 * DIRECCIÓN DE ARTE
 *   · Foto REAL desenfocada: el spritz de Aperol de la terraza (IMG_3077 t=2 s).
 *   · Título con los dos pesos de la marca; las pistas en una pastilla verde de
 *     esquinas vivas (el botón de QB), las alternativas en Bell MT itálica.
 *   · Orgánica.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {QB_BOTON_FONDO} from "../../../brand/qb";
import {cargarFuentesQbOct, FotoQB, Linea, LogoQB, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST14_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "ADIVINA EL TRAGO",
  etiqueta: "PISTAS",
  texto: "¿Sabes cuál es?",
  pie: "Responde y participa por xxxx",
  frase: "Aperol Spritz · Mimosa · Negroni",
  },
};

const Opcion: React.FC<{top: number; letra: string; texto: string}> = ({top, letra, texto}) => (
  <div style={{position: "absolute", top, left: (MESA.w - 600) / 2, width: 600, height: 78,
    border: "2px solid rgba(255,255,255,.85)", display: "flex", alignItems: "center",
    color: "#fff", background: "rgba(0,0,0,.28)"}}>
    <span style={{width: 78, textAlign: "center", fontFamily: "Raleway", fontWeight: 800,
      fontSize: 34}}>{letra}</span>
    <span style={{fontFamily: "BellMT", fontStyle: "italic", fontSize: 40}}>{texto}</span>
  </div>
);

export const QbSt14Adivina: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/14-adivina.jpg" ratio={2250 / 4000} zoom={1.25} cx={0.58} cy={0.32} />
    <Velo arriba={[560, 0.7]} abajo={[700, 0.85]} plano={0.12} />
    <LogoQB top={210} ancho={150} />
    <Linea top={390} cuerpo={112} peso={800} tracking="0.01em">ADIVINA</Linea>
    <Linea top={508} cuerpo={112} peso={400} italica tracking="-0.01em">el trago</Linea>
    <Linea top={690} cuerpo={32} peso={600} tracking="0.3em">PISTAS</Linea>
    <div style={{position: "absolute", top: 744, left: (MESA.w - 520) / 2, width: 520, height: 150,
      background: QB_BOTON_FONDO, display: "flex", alignItems: "center", justifyContent: "center",
      gap: 46, fontSize: 92, fontFamily: "'Segoe UI Emoji','Noto Color Emoji',sans-serif"}}>
      <span>🍊</span><span>🫧</span><span>🥂</span>
    </div>
    <Linea top={1010} cuerpo={52} familia="BellMT" italica>{QB_ST14_DATA.pieza.texto}</Linea>
    <Opcion top={1100} letra="A" texto="Aperol Spritz" />
    <Opcion top={1196} letra="B" texto="Mimosa" />
    <Opcion top={1292} letra="C" texto="Negroni" />
    <Linea top={1420} cuerpo={32} peso={500}>{QB_ST14_DATA.pieza.pie}</Linea>
  </AbsoluteFill>
);
