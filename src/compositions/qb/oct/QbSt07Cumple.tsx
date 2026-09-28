/**
 * QB · ST 07-10 · 16:00 · ESTÁTICA — CUMPLEAÑOS EN QB  (ST n°3 S1)
 *
 * BRIEF (grilla octubre, STORIES col. E, OK PARA DISEÑAR desde el 28-09 tarde):
 *   Collage de 3 momentos de una celebración con cortes orgánicos y dibujos a
 *   mano. Texto: «Convierte tu cumpleaños en una noche inolvidable» · «5 tragos
 *   de cortesía para el cumpleañero/a» · «Shots de regalo · Postre · Cuenta
 *   separadas · Puedes traer tu propia torta». Interacción: ARMA EL GRUPO Y
 *   RESERVA AHORA (link reserva mesas).
 * COMENTARIO DEL CLIENTE: «veamos opción más simple, siendo una story mostraría
 *   la información más importante de inmediato» (R-43) → sin collage.
 *
 * DIRECCIÓN DE ARTE
 *   · UNA foto a sangre: la torta con bengalas llegando a la mesa, la misma del
 *     post de cumpleaños 05-10 (generada, no hay cumpleaños en las sesiones) →
 *     «Imagen referencial».
 *   · La información va ARRIBA y de inmediato: logo, titular de dos voces
 *     («Convierte tu cumpleaños» Raleway fina en caja alta + «en una noche
 *     inolvidable» en Brushwell, como el post), el beneficio principal en el
 *     botón verde y los otros cuatro en una línea.
 *   · Aire entre 1330 y 1480 para el sticker del link («ARMA EL GRUPO Y RESERVA
 *     AHORA»), dentro de la zona segura.
 *   · «Cuenta separadas» va literal del brief (concordancia consultada a contenido).
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BotonVerde, cargarFuentesQbOct, FotoQB, ImagenReferencial, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST07_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "Convierte tu cumpleaños en una noche inolvidable",
  beneficio: "5 tragos de cortesía para el cumpleañero/a",
  resto: "Shots de regalo · Postre · Cuenta separadas · Puedes traer tu propia torta",
  },
};

export const QbSt07Cumple: React.FC = () => {
  const d = QB_ST07_DATA.pieza;
  const [r1, r2, r3, r4] = d.resto.split(" · ");
  return (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/05-cumple-torta.jpg" ratio={1} zoom={1} cx={0.5} cy={0.5} />
    <Velo arriba={[1050, 0.88]} abajo={[560, 0.8]} />
    <LogoQB top={250} ancho={170} />
    <Linea top={392} cuerpo={52} peso={300} tracking="0.05em" interlinea={1.1}>
      CONVIERTE TU<br />CUMPLEAÑOS
    </Linea>
    <Linea top={502} cuerpo={112} familia="Brushwell" interlinea={1}>en una noche inolvidable</Linea>
    <BotonVerde top={660} ancho={900} alto={66} cuerpo={31} peso={700}>
      {d.beneficio.toUpperCase()}
    </BotonVerde>
    <Linea top={752} cuerpo={30} peso={500} interlinea={1.45}>
      {r1} · {r2} · {r3}<br />{r4}
    </Linea>
    <ImagenReferencial top={1556} />
  </AbsoluteFill>
  );
};
