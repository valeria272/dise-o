// ============================================================================
// 08 · COVER DE REEL — «Ninguna de estas ideas era la buena»
// ----------------------------------------------------------------------------
// REGLA    Un cover tiene dos trabajos a la vez: ser el primer fotograma del
//          reel (impacto antes de 1,5 s) y ser una baldosa de la grilla. Si
//          sólo cumple uno, está mal hecho.
// IDEA     Confesar el proceso en vez de vender el resultado. Nadie publica las
//          ocho ideas malas; decirlo en portada es lo que hace que se toque.
// ANOMALÍA El bloque de cuatro líneas a sangre, casi sin aire lateral. La
//          tipografía ocupa el lienzo, que es justo lo que pide la voz IMPACTO.
// INTERV.  Una: el círculo rosado alrededor de «la buena». Rodear es señalar lo
//          que importa; acá señala lo único que sobrevivió.
// ZONAS    9:16 respeta las zonas seguras de Meta — 250 px arriba, 340 abajo,
//          115 a la derecha. No es criterio estético: es dónde Meta dibuja su
//          propia interfaz encima (qa/agencia.yaml → zona-segura-meta).
// ============================================================================
import React from "react";
import {useVideoConfig} from "remotion";
import {C, asegurarFuentes, margen, VOZ} from "../../brand/copylab/sistema";
import {Bloque, Indice} from "../../brand/copylab/tipografia";
import {Pieza} from "../../brand/copylab/lienzo";
import {Circulo} from "../../brand/copylab/mano";

export const ReelCover: React.FC = () => {
  asegurarFuentes();
  const {width: W} = useVideoConfig();
  const M = margen(W);

  return (
    <Pieza fondo={C.tinta} grano={0.2}>
      {/* En 9:16 el margen derecho NO es el margen de la marca: son los 115 px de
          interfaz de Meta más respiro. Alinear al margen de 80 metía la hora
          debajo de los botones (medido en el primer render: 30 px adentro). */}
      <div style={{position: "absolute", left: M, top: 286, right: 155,
                   display: "flex", justifyContent: "space-between"}}>
        <Indice familia="Reel" ref="018" />
        <div style={{fontFamily: VOZ.data, fontSize: 22, fontWeight: 400,
                     letterSpacing: "0.16em", color: "rgba(242,244,246,0.45)"}}>
          0:14
        </div>
      </div>

      <div style={{position: "absolute", left: M, top: 636}}>
        <Bloque
          base={200}
          lineas={[
            {t: "Ninguna", wdth: 66},
            {t: "de estas", wdth: 66},
            {t: "ideas era", wdth: 66},
            {t: "la buena.", wdth: 66},
          ]}
        />
      </div>

      {/* Lo único que sobrevivió. */}
      <Circulo x={M - 40} y={1156} w={824} h={210} grosor={8} semilla={31} rot={-1.6} />

      <div style={{position: "absolute", left: M, top: 1414}}>
        <Bloque
          base={200}
          sangria={0.012}
          lineas={[{t: "La buena vino después.", voz: "editorial", esc: 0.37, color: C.rosa}]}
        />
      </div>
    </Pieza>
  );
};
