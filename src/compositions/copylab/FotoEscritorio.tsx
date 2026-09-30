// ============================================================================
// COPYWRITERS · «LA IA ACELERA. LAS IDEAS DIRIGEN.»
// ----------------------------------------------------------------------------
// DIRECCIÓN DE ARTE
//
// Manda el TEXTO, y la foto es el papel donde está escrito. Al revés que la
// pieza del aceite, y a propósito: si las dos piezas con foto se resolvieran
// igual, el sistema sería una plantilla con fotos distintas.
//
// La escena es cenital de escritorio en lino beige — y el beige NO es casual:
// es el color que el board le asigna a IA / PROCESO. Acá el color del
// territorio no se pinta encima, ya está en la mesa. Es la forma más limpia de
// cumplir la taxonomía de color sin ensuciar la fotografía.
//
// El titular ocupa la mitad inferior, que la foto deja deliberadamente vacía.
// No hay velo: el texto se apoya en tela clara, en negro tinta.
//
// El cuaderno tiene bocetos, no datos. Nada de lo que se ve es un resultado.
//
// Territorio: IA / PROCESO (beige). Formato 1080×1350.
// Foto: Seedream 5 Pro (30-09-2026) — ambiente generado.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {C2, asegurarFuentesV2} from "../../brand/copylab/sistemaV2";
import {Foto, Linea, Subrayado} from "../../brand/copylab/piezasV2";

export const FotoEscritorio: React.FC = () => {
  asegurarFuentesV2();
  return (
    <AbsoluteFill>
      {/* Recorte por abajo: arriba están el laptop y el cuaderno, que son la
          escena; lo que sobra es tela lisa y ésa sí se puede perder. */}
      <Foto src="assets/copywriters/v2/02-escritorio.png" foco="50% 22%" />

      <div style={{position: "absolute", left: 80, top: 790}}>
        <Linea cuerpo={128} color={C2.negro}>LA IA ACELERA.</Linea>
        <Linea cuerpo={128} color={C2.negro}>LAS IDEAS</Linea>
        <Linea cuerpo={128} color={C2.rosa}>DIRIGEN.</Linea>
      </div>
      <Subrayado x={76} y={1120} ancho={366} alto={34} grosor={12} />


    </AbsoluteFill>
  );
};
