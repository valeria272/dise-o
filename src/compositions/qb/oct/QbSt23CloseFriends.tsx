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
 *   · Foto REAL cenital de la terraza de QB: manos, copa de blanco y la mesa de
 *     listones (IMG_3049 t=0,72 s, sesión orgánica 2026).
 *   · La nota se CONSTRUYE en código sobre la madera libre de abajo: papel crema
 *     con grano, girada, con sombra de contacto; la letra es Brushwell, la mano
 *     de QB. Sin IA.
 *   · ⚠️ La toma tiene una copa y no «2 o 3 tragos»: la sesión no trae un cenital
 *     con cócteles. Anotado para Eli.
 *   · Orgánica. Sin punto en título ni bajada (regla Hilton §F).
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

const Nota: React.FC = () => (
  <div style={{position: "absolute", left: 318, top: 1010, width: 470, height: 420,
    transform: "rotate(-7deg)",
    background: "linear-gradient(160deg, #F4EEE2 0%, #EDE5D6 60%, #E4DACA 100%)",
    boxShadow: "0 2px 3px rgba(0,0,0,.35), 14px 22px 38px rgba(0,0,0,.55)",
    color: TINTA_NOTA, fontFamily: "Brushwell", padding: "34px 40px"}}>
    {/* grano del papel */}
    <div style={{position: "absolute", inset: 0, opacity: 0.18, mixBlendMode: "multiply",
      backgroundImage: "repeating-linear-gradient(0deg, rgba(0,0,0,.08) 0 1px, transparent 1px 3px)"}} />
    <div style={{fontSize: 58, lineHeight: 1.05}}>QB Close Friends</div>
    <div style={{marginTop: 6, width: 300, borderTop: `2px solid ${TINTA_NOTA}`, opacity: 0.7,
      transform: "rotate(-1.5deg)"}} />
    <div style={{fontSize: 50, lineHeight: 1.28, marginTop: 18, paddingLeft: 10}}>
      Concursos ✶<br />Beneficios ✶<br />Sorpresas ✶
    </div>
  </div>
);

export const QbSt23CloseFriends: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/23-closefriends.jpg" ratio={2250 / 4000} zoom={1.05} cx={0.5} cy={0.46} />
    <Velo arriba={[760, 0.92]} abajo={[520, 0.9]} />
    <Nota />
    <LogoQB top={200} ancho={140} />
    <Linea top={360} cuerpo={56} peso={300} tracking="0.06em">HAY COSAS QUE</Linea>
    <Linea top={426} cuerpo={56} peso={800} tracking="0.02em">SOLO VAN A</Linea>
    <Linea top={490} cuerpo={112} familia="BellMT" italica>Close Friends</Linea>
    <Linea top={1540} cuerpo={32} peso={500} ancho={800}>{QB_ST23_DATA.pieza.bajada}</Linea>
    <BotonVerde top={1660} ancho={740} alto={84} cuerpo={32} peso={800}>{QB_ST23_DATA.pieza.cta}</BotonVerde>
  </AbsoluteFill>
);
