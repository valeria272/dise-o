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
  *
 * ⭐ RONDA 4 DE ELI 28-09: parecerse a la ref (Medellín). Lo que se toma: la toma
 *   CENITAL sobre madera oscura, los tragos en las esquinas, una mano con lápiz a
 *   punto de escribir en la nota y la otra apoyada; y el titular con serif
 *   itálica chica + serif grande. La nota ya viene en la foto (generada en
 *   blanco): se midió su rectángulo (centro 596,1234 en mesa, 567×383, −26,7°) y
 *   se escribe encima en Brushwell con la tinta en multiplicar → «Imagen
 *   referencial».
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

/** La nota de la foto, medida (mesa 1080×1920): centro, lado y giro. */
const NOTA = {cx: 596, cy: 1234, w: 567, h: 383, giro: -26.7};
const Nota: React.FC = () => (
  <div style={{position: "absolute", left: NOTA.cx - NOTA.w / 2, top: NOTA.cy - NOTA.h / 2,
    width: NOTA.w, height: NOTA.h, transform: `rotate(${NOTA.giro}deg)`, mixBlendMode: "multiply",
    color: TINTA_NOTA, fontFamily: "Brushwell", padding: "38px 0 0 70px", opacity: 0.92}}>
    <div style={{fontSize: 58, lineHeight: 1.05}}>QB Close Friends</div>
    <div style={{marginTop: 4, width: 300, borderTop: `2px solid ${TINTA_NOTA}`, opacity: 0.7,
      transform: "rotate(-1.5deg)"}} />
    <div style={{fontSize: 48, lineHeight: 1.22, marginTop: 12, paddingLeft: 12}}>
      Concursos <Estrella /><br />Beneficios <Estrella /><br />Sorpresas <Estrella />
    </div>
  </div>
);

export const QbSt23CloseFriends: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/23-closefriends-r4.jpg" ratio={1520 / 2736} />
    <Velo arriba={[700, 0.6]} abajo={[560, 0.9]} />
    <Nota />
    <LogoQB top={250} ancho={140} />
    {/* r4: como «La noche en / Medellín / no es normal» de la ref */}
    <Linea top={420} cuerpo={60} familia="BellMT" italica>Hay cosas que solo van a</Linea>
    <Linea top={486} cuerpo={140} familia="BellMT" interlinea={1}>Close Friends</Linea>
    <Linea top={1440} cuerpo={32} peso={500} ancho={800}>{QB_ST23_DATA.pieza.bajada}</Linea>
    <BotonVerde top={1510} ancho={740} alto={62} cuerpo={29} peso={800}>{QB_ST23_DATA.pieza.cta}</BotonVerde>
    <Linea top={1548 + 36} cuerpo={15} italica sombra={false} color="rgba(255,255,255,.75)">*Imagen referencial</Linea>
  </AbsoluteFill>
);
