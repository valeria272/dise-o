// ============================================================================
// COPYWRITERS · G — «UN CAMBIO CHICO.»
// ----------------------------------------------------------------------------
// DIRECCIÓN DE ARTE
//
// Primera pieza hecha con MATERIAL REAL del estudio: no es una gráfica sobre un
// concepto de marca, es un frame del CAP.02 «Turno de noche» que ya existe
// renderizado en el repo. G no se generó para este post — se estaba usando.
//
// El concepto sale literal del brief de Valeria (pilar G):
//   «G frente a 25 archivos: UN CAMBIO CHICO. Balloon: 23 versiones después.»
//
// La imagen manda: G ocupa el centro y el texto se acomoda al mundo que ya
// estaba ahí — el escritorio del Nivel -1 es el lugar donde cabe el titular,
// no un espacio que se abrió para meterlo.
//
// El rosa NO se agrega: ya está en la escena (el halo, el logo del pecho, la
// luz de las zapatillas). El único rosa nuevo es la Balloon, y por eso remata.
//
// ⛔ Se recorta la cabecera «TEMPORADA 1 · CAPÍTULO 02» quemada en el frame:
//    es exactamente la metadata editorial que el feed ya no lleva.
// ⛔ El canon de G tiene candados propios: gcl-agent/universo/CANON_LOCK.md.
//    El protagonista se llama G — «Gigi» no existe — y G.C.L. es el universo,
//    nunca el personaje.
//
// Territorio: G. Formato 1080×1350.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {C2, VOZ2, asegurarFuentesV2} from "../../brand/copylab/sistemaV2";
import {Foto} from "../../brand/copylab/piezasV2";

export const PostG: React.FC = () => {
  asegurarFuentesV2();
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      {/* El frame es 9:16. Se recorta a 4:5 bajando el encuadre lo suficiente
          para dejar fuera la cabecera quemada, sin perder el halo de G. */}
      <Foto src="assets/copywriters/g/f450.png" foco="50% 46%" />

      {/* Velo sólo en el pie, donde va el titular. La escena está iluminada a
          propósito y oscurecerla entera sería desperdiciar el material. */}
      <AbsoluteFill style={{
        background:
          "linear-gradient(0deg, rgba(11,11,11,0.96) 0%, rgba(11,11,11,0.72) 18%, rgba(11,11,11,0) 38%)",
      }} />

      <div style={{position: "absolute", left: 72, top: 1012}}>
        <div style={{
          fontFamily: VOZ2.titular, fontWeight: 700, fontSize: 132,
          lineHeight: 0.86, color: C2.offwhite, textTransform: "uppercase",
        }}>
          UN CAMBIO<br />CHICO.
        </div>
      </div>

      {/* Balloon como remate, integrada a la línea del titular. */}
      <div style={{
        position: "absolute", left: 500, top: 1240,
        transform: "rotate(-3deg)", transformOrigin: "left top",
        fontFamily: VOZ2.mano, fontWeight: 700, fontSize: 52,
        color: C2.rosa, textTransform: "uppercase", whiteSpace: "nowrap",
      }}>
        23 VERSIONES DESPUÉS.
      </div>
    </AbsoluteFill>
  );
};
