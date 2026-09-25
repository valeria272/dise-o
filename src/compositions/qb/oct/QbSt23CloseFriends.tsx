/**
 * QB · ST 23-10 · ESTÁTICA — ÚNETE A NUESTROS CLOSE FRIENDS
 *
 * BRIEF (STORIES col. T, OK PARA DISEÑAR, sin comentario):
 *   Composición cenital o semi cenital sobre una mesa de QB: 2 o 3 tragos, manos
 *   y una nota escrita a mano como elemento protagonista. Íntima, espontánea y
 *   editorial, como un momento real entre amigos. Nocturna, cálida, sofisticada.
 *   Texto principal: HAY COSAS QUE / SOLO VAN A CLOSE FRIENDS. · Dentro de la
 *   nota: QB CLOSE FRIENDS / Concursos ✶ / Beneficios ✶ / Sorpresas ✶ · Bajada:
 *   Únete a nuestros Close Friends y accede a concursos, sorpresas y beneficios
 *   exclusivos. · Interacción: RESPONDE ESTA STORY Y TE AGREGAMOS. 💚
 *
 * REFERENCIA: Pinterest 1114781714032767686 («La noche en Medellín») — manos
 * sobre la barra, cenital, una nota de papel escrita a mano.
 *
 * DIRECCIÓN DE ARTE
 *   · ⭐ Foto REAL (cambiada el 25-09-2026): «Fotos 4 agosto / Editadas»
 *     IMG_4797 — manos brindando con cuatro tragos sobre la mesa de listones,
 *     semicenital y de noche con flash cálido. Antes era IMG_3049, que tenía una
 *     sola copa de blanco y no los «2 o 3 tragos» del brief.
 *   · La nota se CONSTRUYE en código sobre la madera libre de abajo: papel crema
 *     con grano, girada, con sombra de contacto; la letra es Brushwell, la mano
 *     de QB. Sin IA.
 *   · Orgánica. Sin punto en título ni bajada (regla Hilton §F).
 *   · ⭐ Eli 25-09: «ten cuidado con las medidas que aparecen en Instagram» ⇒
 *     todo el texto dentro de 250 arriba · 340 abajo (el botón termina en 1578).
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BotonVerde, cargarFuentesQbOct, FotoQB, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST23_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "HAY COSAS QUE SOLO VAN A CLOSE FRIENDS",
  texto: "QB CLOSE FRIENDS · Concursos · Beneficios · Sorpresas",
  bajada: "Únete a nuestros Close Friends y accede a concursos, sorpresas y beneficios exclusivos",
  cta: "RESPONDE ESTA STORY Y TE AGREGAMOS",
  },
};

const TINTA_NOTA = "#2A2522";
/** ⭐ Eli 25-09: «las estrellitas de la tarjeta podrían ser verdes» — el verde
 *  oscuro del botón de QB, que sobre el papel crema sí se lee. */
const VERDE_NOTA = "#3E6B47";
const Estrella: React.FC = () => <span style={{color: VERDE_NOTA}}>✶</span>;

const Nota: React.FC = () => (
  <div style={{position: "absolute", left: 350, top: 1080, width: 380, height: 318,
    transform: "rotate(-7deg)",
    background: "linear-gradient(160deg, #F4EEE2 0%, #EDE5D6 60%, #E4DACA 100%)",
    boxShadow: "0 2px 3px rgba(0,0,0,.35), 14px 22px 38px rgba(0,0,0,.55)",
    color: TINTA_NOTA, fontFamily: "Brushwell", padding: "24px 32px"}}>
    {/* grano del papel */}
    <div style={{position: "absolute", inset: 0, opacity: 0.18, mixBlendMode: "multiply",
      backgroundImage: "repeating-linear-gradient(0deg, rgba(0,0,0,.08) 0 1px, transparent 1px 3px)"}} />
    <div style={{fontSize: 47, lineHeight: 1.05}}>QB Close Friends</div>
    <div style={{marginTop: 6, width: 246, borderTop: `2px solid ${TINTA_NOTA}`, opacity: 0.7,
      transform: "rotate(-1.5deg)"}} />
    <div style={{fontSize: 40, lineHeight: 1.26, marginTop: 12, paddingLeft: 10}}>
      Concursos <Estrella /><br />Beneficios <Estrella /><br />Sorpresas <Estrella />
    </div>
  </div>
);

export const QbSt23CloseFriends: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/23-closefriends.jpg" ratio={2250 / 3375} zoom={1.12} cx={0.52} cy={0.65} />
    <Velo arriba={[760, 0.92]} abajo={[520, 0.9]} />
    <Nota />
    <LogoQB top={250} ancho={140} />
    <Linea top={404} cuerpo={56} peso={300} tracking="0.06em">HAY COSAS QUE</Linea>
    <Linea top={470} cuerpo={56} peso={800} tracking="0.02em">SOLO VAN A</Linea>
    <Linea top={534} cuerpo={112} familia="BellMT" italica>Close Friends</Linea>
    <Linea top={1420} cuerpo={32} peso={500} ancho={800}>{QB_ST23_DATA.pieza.bajada}</Linea>
    <BotonVerde top={1502} ancho={740} alto={76} cuerpo={31} peso={800}>{QB_ST23_DATA.pieza.cta}</BotonVerde>
  </AbsoluteFill>
);
