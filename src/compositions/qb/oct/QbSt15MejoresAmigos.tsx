/**
 * QB · ST 15-10 · 17:00 · ESTÁTICA — ÚNETE A MEJORES AMIGOS QB
 *
 * BRIEF (STORIES col. K, OK PARA DISEÑAR, sin comentario):
 *   Estética nocturna, social y aspiracional: el ambiente de QB y ese mood de
 *   grupo exclusivo / mejores amigos. Grupo brindando, luces bajas / flash,
 *   cocktails en mano, panorama real y espontáneo. Guiño sutil a Close Friends /
 *   Mejores Amigos con el verde, un ícono de estrella o pequeños detalles, sin
 *   que se vea demasiado literal ni muy «Instagram screenshot».
 *   Texto: HAY COSAS QUE SOLO / PASAN EN MEJORES AMIGOS 💚 · Concursos, sorpresas
 *   y contenido exclusivo de QB. · RESPONDE ESTA STORY PARA ENTRAR
 *
 * REFERENCIA: IG safariproductora DdFRnJQIGgT — historias de fiesta con flash y
 * la pastilla verde de «Mejores amigos».
 *
 * DIRECCIÓN DE ARTE
 *   · Foto REAL de noche en la terraza de QB, con las guirnaldas de luces y un
 *     trago en la mano (sesión de Víctor, C4182 t=11,56 s). Look flash en código.
 *   · El guiño: la ESTRELLA blanca en círculo verde —el ícono de Mejores amigos—
 *     chica, junto al titular; el verde es el degradado de la marca, no el verde
 *     de Instagram. Nada de capturas de la interfaz.
 *   · 💚 del brief se reemplaza por la estrella verde (el mismo guiño, ya dibujado).
 *   · Orgánica.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {QB_BOTON_FONDO} from "../../../brand/qb";
import {BotonVerde, cargarFuentesQbOct, FotoQB, Linea, LogoQB, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST15_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "HAY COSAS QUE SOLO PASAN EN MEJORES AMIGOS",
  texto: "Concursos, sorpresas y contenido exclusivo de QB",
  cta: "RESPONDE ESTA STORY PARA ENTRAR",
  },
};

const Estrella: React.FC<{top: number; d?: number}> = ({top, d = 96}) => (
  <div style={{position: "absolute", top, left: (MESA.w - d) / 2, width: d, height: d,
    borderRadius: d, background: QB_BOTON_FONDO, display: "flex", alignItems: "center",
    justifyContent: "center", boxShadow: "0 6px 24px rgba(0,0,0,.4)"}}>
    <svg width={d * 0.56} height={d * 0.56} viewBox="0 0 24 24">
      <path fill="#fff" d="M12 2.2l2.9 6.2 6.8.8-5 4.6 1.3 6.7L12 17.2l-6 3.3 1.3-6.7-5-4.6 6.8-.8z" />
    </svg>
  </div>
);

export const QbSt15MejoresAmigos: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/15-mejoresamigos.jpg" ratio={2250 / 4000} zoom={1.0} />
    <Velo arriba={[820, 0.9]} abajo={[760, 0.92]} />
    <LogoQB top={250} ancho={140} />
    <Linea top={438} cuerpo={56} peso={300} tracking="0.06em">HAY COSAS QUE SOLO</Linea>
    <Linea top={504} cuerpo={56} peso={800} tracking="0.02em">PASAN EN</Linea>
    <Linea top={568} cuerpo={112} familia="BellMT" italica>Mejores amigos</Linea>
    <Estrella top={352} d={58} />
    <Linea top={1414} cuerpo={34} peso={500} ancho={940}>{QB_ST15_DATA.pieza.texto}</Linea>
    <BotonVerde top={1500} ancho={720} alto={76} cuerpo={31} peso={800}>{QB_ST15_DATA.pieza.cta}</BotonVerde>
  </AbsoluteFill>
);
