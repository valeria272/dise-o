/**
 * QB · ST 12-10 · 14:00 · ESTÁTICA — PLATO DESTACADO  (ST n°1 S2)
 *
 * BRIEF (grilla octubre, STORIES col. I, OK PARA DISEÑAR desde el 28-09 tarde):
 *   Composición editorial y gastronómica, el plato protagonista: pulpo grillado
 *   al chimichurri con puré trufado, pimentones asados y salsa de olivos.
 *   Texto: CONOCE NUESTRA CARTA · PULPO AL CHIMICHURRI · bajada «Una propuesta
 *   del mar con carácter y sabor». Interacción: link reserva.
 * COMENTARIO DEL CLIENTE: «Tomemos esta como referencia, pero démosle una vuelta
 *   (que el vino sea blanco y cambiar escenario), le ponemos el nombre al plato,
 *   de forma similar, y que arriba sea un texto que diga Conoce nuestra carta
 *   (como la story que hicimos de tragos de autor en septiembre)».
 *
 * REFERENCIA: Pinterest 19421842140423323 («Recomendados del mes»): plato y copa
 * sobre mesa de madera negra, hojas desenfocadas en las esquinas, texto al lado.
 *
 * DIRECCIÓN DE ARTE
 *   · Foto: el pulpo REAL de QB («Quotidien-153», carta jul-2024) con el plato
 *     intacto; Seedream le cambió el escenario (mesa negra con veta, hojas en
 *     primer plano, como la ref) y el tinto por BLANCO → «Imagen referencial».
 *   · ✅ APROBADA por Eli el 28-09 (r10) con dos ajustes: «Imagen referencial»
 *     centrada, y la mesa «se ve sucia» → limpiada en la foto (manchas claras y
 *     vetas anaranjadas de la madera, plato/copa/hojas intactos; OpenCV, no IA,
 *     porque la IA reencuadró el plato).
 *   · Arriba, la gramática de «Conoce nuestra carta» de septiembre (ST5-S2):
 *     logo, «Conoce» fino + «nuestra carta» bold.
 *   · El nombre del plato «de forma similar»: en septiembre iba en cursiva serif
 *     entre filetes finos → Bell MT itálica con filetes; bajada en Raleway itálica.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {cargarFuentesQbOct, FotoQB, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST12_DATA: Record<string, Record<string, string>> = {
  pieza: {
  antetitulo: "Conoce",
  titular: "nuestra carta",
  plato: "Pulpo al chimichurri",
  bajada: "Una propuesta del mar con carácter y sabor",
  },
};

const Filete: React.FC<{top: number; left: number}> = ({top, left}) => (
  <div style={{position: "absolute", top, left, width: 120, borderTop: "2px solid rgba(255,255,255,.85)"}} />
);

export const QbSt12Pulpo: React.FC = () => {
  const d = QB_ST12_DATA.pieza;
  return (
    <AbsoluteFill style={{background: "#000"}}>
      {/* la foto BAJA 330 px: la copa queda bajo el titular y no lo tapa; el canto de
          arriba de la foto (mesa casi negra) se funde a negro */}
      <FotoQB src="assets/hilton/qb/oct/12-pulpo.jpg" ratio={1520 / 2736} libre bajar={330} />
      <div style={{position: "absolute", left: 0, right: 0, top: 0, height: 560,
        background: "linear-gradient(180deg, #000 0%, #000 55%, rgba(0,0,0,0) 100%)"}} />
      <Velo arriba={[620, 0.5]} abajo={[380, 0.55]} />
      <LogoQB top={250} ancho={170} />
      <Linea top={372} cuerpo={44} peso={400}>{d.antetitulo}</Linea>
      <Linea top={418} cuerpo={70} peso={700}>{d.titular}</Linea>
      {/* el nombre del plato en la mesa vacía, sobre el plato, entre filetes */}
      <Filete top={544} left={64} />
      <Filete top={544} left={1080 - 64 - 120} />
      <Linea top={512} cuerpo={60} familia="BellMT" italica>{d.plato}</Linea>
      <Linea top={588} cuerpo={30} peso={400} italica>{d.bajada}</Linea>
      {/* la leyenda va CENTRADA (Eli, r10) sobre la mesa, entre la copa y el plato */}
      <Linea top={1190} cuerpo={17} italica sombra={false} color="rgba(255,255,255,0.75)"
        ancho={400}>*Imagen referencial</Linea>
    </AbsoluteFill>
  );
};
