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
  *
 * ⭐ RONDA 4 DE ELI 28-09: parecerse a la ref (Safari Productora: historias con
 *   fotos de flash apiladas y el botón «Mejores amigos» de Instagram). Se toma:
 *   · TRES FOTOS REALES del shooting «QB 13 oct» apiladas a sangre, la del medio
 *     en blanco y negro como en la ref: la terraza llena de noche (98), el
 *     brindis con espumante (101) y los tragos en la mesa (72): las caras quedan
 *     en la banda del medio, donde no hay texto. Todo invitados, nadie de uniforme;
 *   · la PASTILLA «★ Mejores amigos» del botón de compartir de Instagram, sobre
 *     el llamado — el guiño que pedía el brief sin llegar a pantallazo.
 *   Textos del brief sin cambios. Material real → sin «Imagen referencial».
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {BotonVerde, cargarFuentesQbOct, Linea, LogoQB, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST15_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "HAY COSAS QUE SOLO PASAN EN MEJORES AMIGOS",
  texto: "Concursos, sorpresas y contenido exclusivo de QB",
  cta: "RESPONDE ESTA STORY PARA ENTRAR",
  },
};

const BANDA = (1920 - 2 * 8) / 3;
const Banda: React.FC<{i: number; src: string; pos: string; bn?: boolean}> = ({i, src, pos, bn = false}) => (
  <Img src={staticFile(`assets/hilton/qb/oct/${src}`)} style={{position: "absolute", left: 0,
    top: i * (BANDA + 8), width: MESA.w, height: BANDA, objectFit: "cover", objectPosition: pos,
    filter: bn ? "grayscale(1) contrast(1.15) brightness(1.05)" : "contrast(1.06) saturate(1.05)"}} />
);

/** El botón «Mejores amigos» del panel de compartir de Instagram. */
const PastillaIG: React.FC<{top: number}> = ({top}) => (
  <div style={{position: "absolute", top, left: (MESA.w - 400) / 2, width: 400, height: 84,
    borderRadius: 42, background: "rgba(20,20,20,.72)", display: "flex", alignItems: "center",
    gap: 18, padding: "0 30px", boxShadow: "0 6px 24px rgba(0,0,0,.4)"}}>
    <div style={{width: 50, height: 50, borderRadius: 50, background: "#1DBF4E", display: "flex",
      alignItems: "center", justifyContent: "center"}}>
      <svg width={28} height={28} viewBox="0 0 24 24">
        <path fill="#fff" d="M12 2.2l2.9 6.2 6.8.8-5 4.6 1.3 6.7L12 17.2l-6 3.3 1.3-6.7-5-4.6 6.8-.8z" />
      </svg>
    </div>
    <div style={{color: "#fff", fontFamily: "Raleway", fontWeight: 600, fontSize: 32}}>Mejores amigos</div>
  </div>
);

export const QbSt15MejoresAmigos: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <Banda i={0} src="15-amigos-98.jpg" pos="50% 50%" />
    <Banda i={1} src="15-amigos-101.jpg" pos="45% 35%" bn />
    <Banda i={2} src="15-amigos-72.jpg" pos="50% 60%" />
    <Velo arriba={[760, 0.9]} abajo={[560, 0.92]} />
    <LogoQB top={250} ancho={140} />
    <Linea top={420} cuerpo={56} peso={300} tracking="0.06em">HAY COSAS QUE SOLO</Linea>
    <Linea top={486} cuerpo={56} peso={800} tracking="0.02em">PASAN EN</Linea>
    <Linea top={550} cuerpo={112} familia="BellMT" italica>Mejores amigos</Linea>
    <Linea top={1394} cuerpo={32} peso={500} ancho={940}>{QB_ST15_DATA.pieza.texto}</Linea>
    <PastillaIG top={1190} />
    <BotonVerde top={1470} ancho={720} alto={70} cuerpo={30} peso={800}>{QB_ST15_DATA.pieza.cta}</BotonVerde>
  </AbsoluteFill>
);
