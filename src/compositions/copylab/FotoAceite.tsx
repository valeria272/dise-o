// ============================================================================
// COPYWRITERS · «BUEN CONTENIDO TAMBIÉN VENDE.»
// ----------------------------------------------------------------------------
// DIRECCIÓN DE ARTE
//
// Manda la IMAGEN. Es el mecanismo de la primera tarjeta del board: fotografía
// de campaña a sangre y una sola anotación a mano encima. El diseño no rescata
// la foto — la remata.
//
// La foto es food photography de luz dura lateral, con la comida cayendo a
// negro por la izquierda. Esa caída NO es fondo sobrante: es el lugar donde
// vive la mano, y por eso el titular no existe. Una pieza, una voz.
//
// El rosa aparece una sola vez, en la mano, y es lo único que no estaba en la
// escena. Copy literal del board.
//
// Territorio: EDITORIAL. Formato 1080×1350.
// Foto: Seedream 5 Pro (30-09-2026) — ambiente generado, sin producto de marca,
// sin logo, sin dato. Rotulada como generada en raw/copywriters/v2-foto/.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {asegurarFuentesV2} from "../../brand/copylab/sistemaV2";
import {Foto, Mano, Subrayado} from "../../brand/copylab/piezasV2";

export const FotoAceite: React.FC = () => {
  asegurarFuentesV2();
  return (
    <AbsoluteFill>
      {/* La foto sale 3:4 de Seedream. Se recorta por abajo para llegar a 4:5:
          arriba está el chorro de aceite y la zona oscura que sostiene la mano. */}
      <Foto src="assets/copywriters/v2/01-aceite.png" foco="50% 18%" />

      {/* Velo sólo en la esquina superior izquierda, donde va la mano. Es un
          degradado corto, no un filtro sobre toda la pieza: oscurecer la foto
          entera para poder escribir encima es admitir que la foto no servía. */}
      <AbsoluteFill style={{
        background:
          "radial-gradient(ellipse 62% 44% at 12% 8%, rgba(11,11,11,0.72) 0%, rgba(11,11,11,0.0) 100%)",
      }} />

      {/* Cuatro líneas, no tres: con «TAMBIÉN VENDE.» en una sola, el remate
          se subía al pan iluminado y perdía contraste. La columna de texto
          tiene que caber en la zona oscura, no invadir la comida. */}
      <Mano x={72} y={132} cuerpo={86} interlineado={1.06}>
        BUEN<br />CONTENIDO<br />TAMBIÉN<br />VENDE.
      </Mano>
      <Subrayado x={78} y={502} ancho={248} alto={32} grosor={12} giro={-2} />

    </AbsoluteFill>
  );
};
